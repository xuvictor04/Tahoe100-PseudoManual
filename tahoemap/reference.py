"""reference - public annotation for every Tahoe gene: names, loci, protein function, pathways and known
interactions, so that a relation found in the data can be called known or new.

The data say which genes move together; whether that is already known needs outside knowledge. This stage fetches
it once from the authoritative public sources, caches the raw files, and reduces them to three tables keyed by the
gene col of atlas/effects/genes.csv (never by symbol: symbols repeat and change):

    HGNC complete set          approved symbol, name, locus group/type, cytoband, aliases, previous symbols, gene
                               groups (families), Entrez and Ensembl ids, UniProt accessions
    Ensembl GRCh38 r112 GTF    gene coordinates and biotype (gene rows), and ENSP -> ENSG (CDS rows) for STRING
    UniProt (reviewed, human)  recommended protein name and the FUNCTION text (evidence tags removed)
    NCBI gene_summary          the RefSeq summary paragraph (human rows), joined on the Entrez id
    Reactome, MSigDB Hallmark  pathway / hallmark gene sets (GMT)
    STRING v12                 human protein links with combined score >= 400 (protein.info for names)

Every source is optional. A download that fails is logged and skipped; --offline uses only what is in the cache,
and with an empty cache the stage still writes one row per gene from Tahoe's own gene metadata (symbol, Ensembl id).

Matching a Tahoe gene to HGNC, strongest evidence first (each HGNC record goes to one gene col at most; a name
that is some record's approved symbol is never read as a previous symbol or alias, HGNC's own precedence):
    ensembl_id    Tahoe's Ensembl id (gene metadata, joined on token) = HGNC ensembl_gene_id
    symbol        Tahoe symbol = approved symbol
    prev_symbol   Tahoe symbol = a previous symbol of exactly one record
    alias_symbol  Tahoe symbol = an alias of exactly one record (aliases are reused across genes: treat as tentative)
    none          no HGNC record
Coordinates come from the GTF by Tahoe's Ensembl id, then HGNC's Ensembl id, then a unique gene_name (primary
chromosomes); without the GTF, chrom alone is read from the HGNC cytoband. uniprot = the reviewed (Swiss-Prot) entry,
found by HGNC id (else by gene name), or the accessions HGNC lists when there is none. Gene-set members and STRING
proteins are placed on cols by Ensembl id where possible (STRING: ENSP -> ENSG via the GTF CDS rows), else by the
approved symbol, Tahoe's symbol (unless it is another gene's approved symbol), or a unique previous symbol.

Outputs in <out>/reference/:
    annotations.parquet    one row per gene col: col, symbol, ensembl_id, hgnc_id, hgnc_symbol, name, locus_group,
                           locus_type, location, chrom, start, end, strand, biotype, aliases, prev_symbols,
                           gene_groups (multi-valued fields "|"-joined, as HGNC writes them), entrez_id, uniprot,
                           protein_name, function, ncbi_summary, matched_by
    gene_sets.parquet      source (hallmark | reactome | hgnc_group), set, col, symbol, set_id, set_size (genes in
                           the set at the source), n_present (its genes among Tahoe genes; only sets with 3..1000)
    string_pairs.parquet   col_a < col_b, score (STRING combined score, best over the genes' proteins)
    sources.json           per source: url, file, status, date, last_modified, bytes, n_rows (+ error)
    downloads/             the raw files (default cache; cache_dir moves it), each with a .meta.json (url, date,
                           Last-Modified), and the GTF reduced to two parquet files (re-read in seconds)
"""

import datetime
import gzip
import http.client
import io
import json
import os
import re
import time
import urllib.error
import urllib.request
import zipfile

import numpy as np
import pandas as pd

from .common import (_cert_failure, describe_url_error, folder, log, read_effects_index, replace_file, stamp_stage,
                     urlopen, write_json, write_parquet)

VERSION = 1

UA = "tahoemap-reference/1 (research pipeline; Python urllib)"
UNIPROT_FIELDS = "accession,reviewed,gene_primary,protein_name,cc_function,xref_hgnc,xref_geneid"
UNIPROT_QUERY = "organism_id:9606%20AND%20reviewed:true"
SOURCES = [
    {"key": "hgnc", "file": "hgnc_complete_set.txt",
     "url": "https://storage.googleapis.com/public-download-files/hgnc/tsv/tsv/hgnc_complete_set.txt"},
    {"key": "ensembl", "file": "Homo_sapiens.GRCh38.112.gtf.gz",
     "url": "https://ftp.ensembl.org/pub/release-112/gtf/homo_sapiens/Homo_sapiens.GRCh38.112.gtf.gz"},
    # the stream endpoint builds the whole answer before the first byte and is often rate limited (HTTP 429): no
    # size probe, one try, then the paginated search endpoint (same fields, 500 per page, ~2 min)
    {"key": "uniprot", "file": "uniprot_human_reviewed.tsv", "probe": False, "tries": 1, "timeout": 180,
     "url": f"https://rest.uniprot.org/uniprotkb/stream?format=tsv&fields={UNIPROT_FIELDS}&query={UNIPROT_QUERY}",
     "paged": f"https://rest.uniprot.org/uniprotkb/search?format=tsv&size=500&fields={UNIPROT_FIELDS}"
              f"&query={UNIPROT_QUERY}"},
    {"key": "ncbi", "file": "gene_summary.gz", "url": "https://ftp.ncbi.nlm.nih.gov/gene/DATA/gene_summary.gz"},
    {"key": "reactome", "file": "ReactomePathways.gmt.zip",
     "url": "https://reactome.org/download/current/ReactomePathways.gmt.zip"},
    {"key": "hallmark", "file": "h.all.v2024.1.Hs.symbols.gmt",
     "url": "https://data.broadinstitute.org/gsea-msigdb/msigdb/release/2024.1.Hs/h.all.v2024.1.Hs.symbols.gmt"},
    {"key": "string_links", "file": "9606.protein.links.v12.0.txt.gz",
     "url": "https://stringdb-downloads.org/download/protein.links.v12.0/9606.protein.links.v12.0.txt.gz"},
    {"key": "string_info", "file": "9606.protein.info.v12.0.txt.gz",
     "url": "https://stringdb-downloads.org/download/protein.info.v12.0/9606.protein.info.v12.0.txt.gz"},
]
SET_MIN, SET_MAX = 3, 1000          # gene sets kept: this many of their genes among Tahoe genes
FUNCTION_MAX = 1200                 # characters of UniProt FUNCTION text kept
PRIMARY_CHROMS = {str(i) for i in range(1, 23)} | {"X", "Y", "MT"}
ANN_COLUMNS = ["col", "symbol", "ensembl_id", "hgnc_id", "hgnc_symbol", "name", "locus_group", "locus_type",
               "location", "chrom", "start", "end", "strand", "biotype", "aliases", "prev_symbols", "gene_groups",
               "entrez_id", "uniprot", "protein_name", "function", "ncbi_summary", "matched_by"]
SET_COLUMNS = ["source", "set", "col", "symbol", "set_id", "set_size", "n_present"]
_NO_RETRY = (400, 401, 403, 404, 405, 410)


# ----------------------------------------------------------------------------- downloads
def _mb(n):
    if n is None:
        return "size unknown"
    return f"{n / 1e6:.1f} MB" if n >= 1e6 else f"{n / 1e3:.0f} kB"


def _now():
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _retry(fn, tries, what):
    """fn() with retries; returns (result, "") or (None, last error). HTTP 4xx other than 408/429 are final;
    a Retry-After header is honoured (capped at 5 min)."""
    err = ""
    for k in range(tries):
        wait = min(120, 10 * 2 ** k)
        try:
            return fn(), ""
        except urllib.error.HTTPError as e:
            err = f"HTTP {e.code} {e.reason or ''}".strip()
            if e.code in _NO_RETRY:
                break
            ra = str((e.headers or {}).get("Retry-After", "") or "")
            if ra.isdigit():
                wait = min(300, max(wait, int(ra)))
        except (urllib.error.URLError, OSError, http.client.HTTPException, ValueError) as e:
            err = describe_url_error(e)
            if _cert_failure(e):
                break                       # not transient: the same certificate fails on every try
        if k + 1 < tries:
            log(f"    {what}: {err}; retry {k + 1}/{tries - 1} in {wait} s")
            time.sleep(wait)
    return None, err


def _probe(url, timeout=20):
    """(bytes, Last-Modified) from a HEAD request, else from a one-byte range request; (None, "") if neither says."""
    for method, extra in (("HEAD", {}), ("GET", {"Range": "bytes=0-0"})):
        try:
            req = urllib.request.Request(url, method=method, headers={"User-Agent": UA, **extra})
            with urlopen(req, timeout) as r:
                lm = r.headers.get("Last-Modified", "") or ""
                if method == "HEAD":
                    cl = r.headers.get("Content-Length", "") or ""
                    if cl.isdigit() and int(cl) > 0:
                        return int(cl), lm
                else:
                    total = (r.headers.get("Content-Range", "") or "").rpartition("/")[2]
                    if total.isdigit():
                        return int(total), lm
        except (urllib.error.URLError, OSError, http.client.HTTPException, ValueError):
            continue
    return None, ""


def _stream_to(url, tmp, timeout):
    """One GET of url into tmp; checks the length against Content-Length and that it is not an HTML error page."""
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    n, step, t0 = 0, 50 << 20, time.time()
    with urlopen(req, timeout) as r, open(tmp, "wb") as fh:
        cl = r.headers.get("Content-Length", "") or ""
        lm = r.headers.get("Last-Modified", "") or ""
        nxt = step
        while True:
            b = r.read(1 << 20)
            if not b:
                break
            fh.write(b)
            n += len(b)
            if n >= nxt:
                log(f"      {n / 1e6:,.0f} MB" + (f" of {int(cl) / 1e6:,.0f}" if cl.isdigit() else "")
                    + f" ({time.time() - t0:.0f} s)")
                nxt += step
    if cl.isdigit() and int(cl) != n:
        raise http.client.IncompleteRead(b"", int(cl) - n)
    if n == 0:
        raise ValueError("empty response")
    with open(tmp, "rb") as fh:
        head = fh.read(512).lower()
    if b"<html" in head or b"<!doctype html" in head:
        raise ValueError("the server returned an HTML page instead of data")
    return n, lm


def _uniprot_paged(url, tmp, timeout, tries):
    """The UniProt search endpoint, page by page (cursor in the Link header), into one TSV with one header line."""
    nxt_re = re.compile(r'<([^>]+)>;\s*rel="next"')
    n_pages, n_lines, total = 0, 0, None
    with open(tmp, "w", encoding="utf-8") as fh:
        while url:
            def get(u=url):
                req = urllib.request.Request(u, headers={"User-Agent": UA})
                with urlopen(req, timeout) as r:
                    return r.read().decode("utf-8"), dict(r.headers)
            res, err = _retry(get, tries, f"uniprot page {n_pages + 1}")
            if res is None:
                raise OSError(f"page {n_pages + 1}: {err}")
            body, hdr = res
            hdr = {k.lower(): v for k, v in hdr.items()}
            total = total or hdr.get("x-total-results")
            lines = body.splitlines(keepends=True)
            if n_pages and lines and lines[0].startswith("Entry\t"):
                lines = lines[1:]
            if lines and not lines[-1].endswith("\n"):
                lines[-1] += "\n"
            fh.writelines(lines)
            n_lines += len(lines)
            n_pages += 1
            if n_pages % 10 == 0:
                log(f"      uniprot: {n_pages} pages, {n_lines - 1:,} of {total or '?'} entries")
            m = nxt_re.search(hdr.get("link", "") or "")
            url = m.group(1) if m else None
    if n_lines < 2:
        raise ValueError("no entries")
    if total and str(total).isdigit() and int(total) != n_lines - 1:
        log(f"      uniprot: WARNING {n_lines - 1:,} entries received, the server announced {int(total):,}")
    return os.path.getsize(tmp), ""


def _read_sidecar(dest):
    p = dest + ".meta.json"
    meta = {}
    if os.path.exists(p):
        try:
            with open(p, encoding="utf-8") as fh:
                meta = json.load(fh)
        except (OSError, ValueError):
            meta = {}
    if "downloaded" not in meta:
        meta["downloaded"] = datetime.datetime.fromtimestamp(
            os.path.getmtime(dest), datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    return meta


def fetch(src, cache_dir, offline=False, refresh=False, tries=4, timeout=120, size=None, last_modified=""):
    """Path of the source's file in the cache (downloading it unless cached / offline) and its record."""
    dest = os.path.join(cache_dir, src["file"])
    rec = {"url": src["url"], "file": dest}
    if not refresh and os.path.exists(dest) and os.path.getsize(dest) > 0:
        meta = _read_sidecar(dest)
        rec.update(status="cached", date=meta.get("downloaded", ""), last_modified=meta.get("last_modified", ""),
                   bytes=os.path.getsize(dest))
        if meta.get("url") and meta["url"] != src["url"]:
            rec["fetched_from"] = meta["url"]
        return dest, rec
    if offline:
        rec.update(status="offline, not cached")
        return None, rec
    tries = int(src.get("tries", tries))
    timeout = float(src.get("timeout", timeout))
    tmp = dest + ".part"
    t0 = time.time()
    log(f"  {src['key']}: downloading {src['url']} ({_mb(size)})")
    res, err = _retry(lambda: _stream_to(src["url"], tmp, timeout), tries, src["key"])
    used = src["url"]
    if res is None and src.get("paged"):
        log(f"    {src['key']}: {err}; trying the paginated endpoint")
        used = src["paged"]
        try:
            res = _uniprot_paged(src["paged"], tmp, timeout=min(timeout, 120), tries=4)
        except (OSError, ValueError, http.client.HTTPException) as e:
            res, err = None, f"{err}; paginated: {e}"
    if res is None:
        if os.path.exists(tmp):
            os.remove(tmp)
        log(f"  {src['key']}: download FAILED ({err}); continuing without it")
        rec.update(status="failed", error=err)
        return None, rec
    n, lm = res
    replace_file(tmp, dest)
    meta = {"url": used, "downloaded": _now(), "last_modified": lm or last_modified, "bytes": n}
    with open(dest + ".meta.json", "w", encoding="utf-8") as fh:
        json.dump(meta, fh, indent=1)
    log(f"  {src['key']}: {_mb(n)} in {time.time() - t0:.0f} s")
    rec.update(status="downloaded", date=meta["downloaded"], last_modified=meta["last_modified"], bytes=n)
    if used != src["url"]:
        rec["fetched_from"] = used
    return dest, rec


# ----------------------------------------------------------------------------- Tahoe genes
def tahoe_genes(out):
    """col, token, symbol, label, ensembl_id (version stripped; "" when unknown) for every gene col, col order."""
    g = read_effects_index(os.path.join(out, "atlas", "effects"))["genes"]
    g = g[g["kind"] == "gene"].sort_values("col")
    t = g[["col", "token", "symbol", "label"]].reset_index(drop=True)
    t["col"] = t["col"].astype(np.int64)
    t["symbol"] = t["symbol"].fillna("").astype(str)
    t["ensembl_id"] = ""
    fi = os.path.join(out, "atlas", "file_index.json")
    paths = []
    if os.path.exists(fi):
        with open(fi, encoding="utf-8") as fh:
            paths = [p for p in (json.load(fh).get("gene") or []) if os.path.exists(p)]
    if not paths:
        log("  gene metadata: not found via atlas/file_index.json; Ensembl ids unknown (symbol matching only)")
        return t
    gm = pd.concat([pd.read_parquet(p, columns=["token_id", "ensembl_id"]) for p in paths], ignore_index=True)
    gm = gm.drop_duplicates("token_id")
    ens = gm.set_index("token_id")["ensembl_id"]
    t["ensembl_id"] = (t["token"].astype(np.int64).map(ens).fillna("").astype(str)
                       .str.strip().str.replace(r"\.\d+$", "", regex=True))
    return t


# ----------------------------------------------------------------------------- source readers
def read_hgnc(path):
    h = pd.read_csv(path, sep="\t", dtype=str, keep_default_na=False, na_values=[""], low_memory=False)
    miss = {"hgnc_id", "symbol", "ensembl_gene_id"} - set(h.columns)
    if miss:
        raise ValueError(f"not an HGNC complete set (no column {', '.join(sorted(miss))})")
    if "status" in h:
        h = h[h["status"].fillna("Approved") == "Approved"]
    for c in ("hgnc_id", "symbol", "name", "locus_group", "locus_type", "location", "alias_symbol", "prev_symbol",
              "gene_group", "gene_group_id", "entrez_id", "ensembl_gene_id", "uniprot_ids"):
        h[c] = h[c].fillna("").astype(str).str.strip() if c in h else ""
    h["ensembl_gene_id"] = h["ensembl_gene_id"].str.replace(r"\.\d+$", "", regex=True)
    return h.reset_index(drop=True)


_GTF_ATTR = re.compile(r'(gene_id|gene_name|gene_biotype) "([^"]*)"')


def read_gtf(path):
    """Gene rows (gene_id, gene_name, gene_biotype, seqname, start, end, strand) and CDS-derived protein_id ->
    gene_id, parsed streaming; both cached as parquet next to the GTF so later runs skip the 1.5 GB of text."""
    gp, pp = path + ".genes.parquet", path + ".proteins.parquet"
    if all(os.path.exists(p) and os.path.getmtime(p) >= os.path.getmtime(path) for p in (gp, pp)):
        return pd.read_parquet(gp), pd.read_parquet(pp)
    cols = {k: [] for k in ("gene_id", "gene_name", "gene_biotype", "seqname", "start", "end", "strand")}
    prot = {}
    tag = 'protein_id "'
    with gzip.open(path, "rt", encoding="utf-8", errors="replace") as fh:
        for line in fh:
            if line.startswith("#"):
                continue
            p = line.split("\t", 8)
            if len(p) < 9:
                continue
            if p[2] == "gene":
                a = dict(_GTF_ATTR.findall(p[8]))
                cols["gene_id"].append(a.get("gene_id", ""))
                cols["gene_name"].append(a.get("gene_name", ""))
                cols["gene_biotype"].append(a.get("gene_biotype", ""))
                cols["seqname"].append(p[0])
                cols["start"].append(int(p[3]))
                cols["end"].append(int(p[4]))
                cols["strand"].append(p[6])
            elif p[2] == "CDS":
                s = p[8]
                i = s.find(tag)
                if i < 0:
                    continue
                pid = s[i + len(tag):s.find('"', i + len(tag))]
                if pid not in prot:
                    m = _GTF_ATTR.search(s)
                    prot[pid] = m.group(2) if m and m.group(1) == "gene_id" else ""
    genes = pd.DataFrame(cols)
    genes["start"] = genes["start"].astype(np.int64)
    genes["end"] = genes["end"].astype(np.int64)
    prots = pd.DataFrame({"protein_id": list(prot), "gene_id": list(prot.values())})
    write_parquet(genes, gp)
    write_parquet(prots, pp)
    return genes, prots


def read_uniprot(path):
    u = pd.read_csv(path, sep="\t", dtype=str, keep_default_na=False, na_values=[""])
    ren = {"Entry": "accession", "Reviewed": "reviewed", "Gene Names (primary)": "gene_primary",
           "Protein names": "protein_names", "Function [CC]": "cc_function", "HGNC": "xref_hgnc",
           "GeneID": "xref_geneid"}
    if "Entry" not in u.columns:
        raise ValueError("not a UniProt TSV (no 'Entry' column)")
    u = u.rename(columns=ren)
    for c in ren.values():
        u[c] = u[c].fillna("").astype(str) if c in u else ""
    u = u[u["reviewed"].str.lower().isin(["reviewed", "true", ""])].reset_index(drop=True)
    u["protein_name"] = u["protein_names"].map(_recommended_name)
    u["function"] = u["cc_function"].map(clean_function)
    return u


def _recommended_name(s):
    """UniProt 'Protein names' = recommended name, then (alternative names) and [Cleaved into: ...]: keep the first
    part, cutting at the first ' (' or ' [' outside brackets."""
    s = str(s or "")
    depth = 0
    for i, ch in enumerate(s):
        if ch in "([" and depth == 0 and i > 0 and s[i - 1] == " ":
            return s[:i].strip()
        if ch in "([":
            depth += 1
        elif ch in ")]":
            depth = max(0, depth - 1)
    return s.strip()


_ECO = re.compile(r"\s*\{ECO:[^}]*\}")
_REFS = re.compile(r"\s*\((?:PubMed:\d+|Ref\.\d+)(?:\s*,\s*(?:PubMed:\d+|Ref\.\d+))*\)")


def clean_function(s, maxlen=FUNCTION_MAX):
    """UniProt FUNCTION text without the 'FUNCTION: ' labels and the {ECO:...} / (PubMed:...) evidence tags,
    at most maxlen characters (cut at a sentence end when one is in the second half)."""
    s = str(s or "")
    if not s:
        return ""
    s = re.sub(r"(^|\s)FUNCTION:\s*", r"\1", s)
    s = _ECO.sub("", s)
    s = _REFS.sub("", s)
    s = re.sub(r"\s+", " ", s)
    s = re.sub(r"\s+([.,;:])", r"\1", s)
    s = re.sub(r"\.(?:\s*\.)+", ".", s).strip()                  # 'text. {ECO:...}.' leaves '..'
    if len(s) > maxlen:
        cut = s.rfind(". ", 0, maxlen - 1)
        s = s[:cut + 1] if cut >= maxlen // 2 else s[:maxlen - 1].rstrip() + "…"
    return s


def read_ncbi(path):
    """Human (#tax_id 9606) rows of NCBI gene_summary: GeneID -> Summary. Streams the all-species file."""
    ids, summ = [], []
    with gzip.open(path, "rt", encoding="utf-8", errors="replace") as fh:
        header = fh.readline().lstrip("#").rstrip("\n").split("\t")
        ix = {c: i for i, c in enumerate(header)}
        gi, si = ix.get("GeneID", 1), ix.get("Summary", 3)
        for line in fh:
            if not line.startswith("9606\t"):
                continue
            p = line.rstrip("\n").split("\t")
            if len(p) > max(gi, si):
                ids.append(p[gi])
                summ.append(p[si].strip())
    s = pd.Series(summ, index=pd.Index(ids, name="entrez_id"), name="ncbi_summary")
    return s[~s.index.duplicated()]


def read_gmt(path):
    """(name, id or url, [genes]) per line of a GMT file, or of the single .gmt inside a .zip."""
    if path.endswith(".zip"):
        with zipfile.ZipFile(path) as z:
            name = next(n for n in z.namelist() if n.lower().endswith(".gmt"))
            text = io.TextIOWrapper(z.open(name), encoding="utf-8", errors="replace").read()
    else:
        with open(path, encoding="utf-8", errors="replace") as fh:
            text = fh.read()
    sets = []
    for line in text.splitlines():
        p = line.rstrip("\n").split("\t")
        if len(p) >= 3 and p[0]:
            genes = [g.strip() for g in p[2:] if g.strip()]
            sets.append((p[0].strip(), p[1].strip(), list(dict.fromkeys(genes))))
    return sets


# ----------------------------------------------------------------------------- matching
def _split_explode(s, sep="|"):
    """Series of sep-joined strings -> long Series (index kept) of single non-empty values."""
    e = s.str.split(sep).explode().str.strip()
    return e[e.notna() & (e != "")]


def _assign(idx, how, taken, cand, label):
    """cand: DataFrame i (Tahoe row), j (HGNC row), pri (lower = better). Gives each unmatched Tahoe gene its best
    untaken record; a record claimed by two genes in the same step goes to the first."""
    if cand.empty:
        return 0
    cand = cand[(idx[cand["i"].to_numpy()] < 0) & ~taken[cand["j"].to_numpy()]]
    cand = cand.sort_values(["pri", "i"], kind="stable").drop_duplicates("i").drop_duplicates("j")
    i, j = cand["i"].to_numpy(), cand["j"].to_numpy()
    idx[i] = j
    how[i] = label
    taken[j] = True
    return len(i)


def match_hgnc(t, h):
    """Index into h (or -1) and matched_by for each row of t (ensembl_id, then symbol, prev, alias)."""
    n = len(t)
    idx = np.full(n, -1, dtype=np.int64)
    how = np.array(["none"] * n, dtype=object)
    taken = np.zeros(len(h), dtype=bool)
    ti = pd.DataFrame({"i": np.arange(n), "ensembl_id": t["ensembl_id"].to_numpy(), "sym": t["symbol"].to_numpy()})
    hj = pd.DataFrame({"j": np.arange(len(h)), "ensembl_id": h["ensembl_gene_id"].to_numpy(),
                       "hsym": h["symbol"].to_numpy()})
    c = ti[ti["ensembl_id"] != ""].merge(hj[hj["ensembl_id"] != ""], on="ensembl_id")
    c["pri"] = (c["sym"] != c["hsym"]).astype(int)               # the same id twice in HGNC: prefer same symbol
    _assign(idx, how, taken, c[["i", "j", "pri"]], "ensembl_id")
    c = ti[ti["sym"] != ""].merge(hj.rename(columns={"hsym": "sym"})[["j", "sym"]], on="sym")
    c["pri"] = 0
    _assign(idx, how, taken, c[["i", "j", "pri"]], "symbol")
    shadow = set(h["symbol"])          # HGNC's own precedence: approved symbol > previous symbol > alias
    for field, label in (("prev_symbol", "prev_symbol"), ("alias_symbol", "alias_symbol")):
        e = _split_explode(h[field])
        keys = pd.DataFrame({"j": e.index.to_numpy(), "sym": e.to_numpy()}).drop_duplicates()
        keys = keys[~keys["sym"].duplicated(keep=False)]        # a name shared by two records says nothing
        keys = keys[~keys["sym"].isin(shadow)]
        shadow |= set(e)
        c = ti[ti["sym"] != ""].merge(keys, on="sym")
        c["pri"] = 0
        _assign(idx, how, taken, c[["i", "j", "pri"]], label)
    return idx, how


def _coords(ann, gtf):
    """chrom/start/end/strand/biotype from the GTF: Tahoe Ensembl id, HGNC Ensembl id, then a unique gene_name."""
    g = gtf.drop_duplicates("gene_id").set_index("gene_id")
    pos = pd.Series(-1, index=ann.index, dtype=np.int64)
    gpos = pd.Series(np.arange(len(g)), index=g.index)
    for key in ("ensembl_id", "hgnc_ensembl"):
        miss = pos < 0
        pos[miss] = ann.loc[miss, key].map(gpos).fillna(-1).astype(np.int64)
    named = g[g["gene_name"] != ""].assign(p=np.arange(len(g))[(g["gene_name"] != "").to_numpy()])
    prim = named[named["seqname"].isin(PRIMARY_CHROMS)]
    uniq = prim[~prim["gene_name"].duplicated(keep=False)].set_index("gene_name")["p"]
    for key in ("symbol", "hgnc_symbol"):
        miss = pos < 0
        pos[miss] = ann.loc[miss, key].map(uniq).fillna(-1).astype(np.int64)
    ok = (pos >= 0).to_numpy()
    p = pos.to_numpy()[ok]
    ann.loc[ok, "chrom"] = g["seqname"].to_numpy()[p]
    ann.loc[ok, "start"] = g["start"].to_numpy()[p]
    ann.loc[ok, "end"] = g["end"].to_numpy()[p]
    ann.loc[ok, "strand"] = g["strand"].to_numpy()[p]
    ann.loc[ok, "biotype"] = g["gene_biotype"].to_numpy()[p]
    return int(ok.sum())


def _chrom_from_location(loc):
    s = loc.fillna("").astype(str)
    c = s.str.extract(r"^(\d{1,2}|X|Y)(?=[pqc ]|$)", expand=False).fillna("")
    return c.mask(s.str.startswith("mitochondria"), "MT")


def _uniprot(ann, u, approved=()):
    """Each gene's reviewed UniProt entry: via HGNC id (prefer an accession HGNC lists), else the primary gene name
    = approved or Tahoe symbol. Fills uniprot, protein_name, function; entrez_id where HGNC had none."""
    ui = pd.DataFrame({"u": np.arange(len(u)), "acc": u["accession"].to_numpy()})
    x = _split_explode(u["xref_hgnc"], ";")
    by_id = pd.DataFrame({"u": x.index.to_numpy(), "hgnc_id": x.to_numpy()})
    a = pd.DataFrame({"i": np.arange(len(ann)), "hgnc_id": ann["hgnc_id"].to_numpy(),
                      "hgnc_uniprot": ann["hgnc_uniprot"].to_numpy()})
    c = a[a["hgnc_id"] != ""].merge(by_id, on="hgnc_id").merge(ui, on="u")
    c["pri"] = [0 if acc in hu.split("|") else 1 for acc, hu in zip(c["acc"], c["hgnc_uniprot"])]
    c = c.sort_values(["pri", "acc"], kind="stable").drop_duplicates("i")
    pick = pd.Series(-1, index=np.arange(len(ann)), dtype=np.int64)
    pick[c["i"].to_numpy()] = c["u"].to_numpy()
    gp = u["gene_primary"].str.strip()
    by_name = pd.Series(np.arange(len(u)), index=gp)
    by_name = by_name[(by_name.index != "") & ~by_name.index.duplicated(keep=False)]
    for key in ("hgnc_symbol", "symbol"):
        miss = (pick < 0).to_numpy()
        if key == "symbol":                    # Tahoe's symbol only for genes HGNC does not know, never as a name
            miss = miss & ann["hgnc_id"].eq("").to_numpy() & ~ann["symbol"].isin(approved).to_numpy()  # of another
        pick[miss] = ann.loc[miss, key].map(by_name).fillna(-1).astype(np.int64).to_numpy()
    ok = (pick >= 0).to_numpy()
    p = pick.to_numpy()[ok]
    ann.loc[ok, "uniprot"] = u["accession"].to_numpy()[p]
    ann.loc[ok, "protein_name"] = u["protein_name"].to_numpy()[p]
    ann.loc[ok, "function"] = u["function"].to_numpy()[p]
    gid = u["xref_geneid"].str.split(";").str[0].str.strip().to_numpy()[p]
    fill = ann.loc[ok, "entrez_id"].isna().to_numpy() & (gid != "")
    rows = ann.index[ok][fill]
    ann.loc[rows, "entrez_id"] = pd.to_numeric(pd.Series(gid[fill]), errors="coerce").to_numpy()
    return int(ok.sum())


def symbol_to_col(ann, h=None):
    """symbol -> col for placing external gene lists: the approved symbol of matched genes; then Tahoe's symbol
    (lowest col on repeats) unless it is the approved symbol of another HGNC gene; then a previous symbol that is
    unique in HGNC, is nobody's approved symbol, and whose record is matched."""
    approved = set(h["symbol"]) if h is not None else set()
    m = {}
    for s, c in zip(ann["hgnc_symbol"], ann["col"]):
        if s and s not in m:
            m[s] = int(c)
    for s, c in zip(ann["symbol"], ann["col"]):
        if s and s not in m and s not in approved:
            m[s] = int(c)
    if h is not None and "matched_j" in ann:
        e = _split_explode(h["prev_symbol"])
        e = e[~e.duplicated(keep=False) & ~e.isin(approved)]
        jcol = pd.Series(ann["col"].to_numpy(), index=ann["matched_j"].to_numpy())
        jcol = jcol[jcol.index >= 0].to_dict()
        for s, j in zip(e.to_numpy(), e.index.to_numpy()):
            if s not in m and j in jcol:
                m[s] = int(jcol[j])
    return m


def _sets_long(source, sets, symmap, ann):
    """GMT sets -> long rows (source, set, col, symbol, set_id, set_size, n_present), sizes 3..1000 present."""
    sym = ann.set_index("col")["symbol"]
    rows = []
    for name, sid, genes in sets:
        cols = sorted({symmap[g] for g in genes if g in symmap})
        if SET_MIN <= len(cols) <= SET_MAX:
            rows.append(pd.DataFrame({"source": source, "set": name, "col": cols, "set_id": sid,
                                      "set_size": len(genes), "n_present": len(cols)}))
    if not rows:
        return pd.DataFrame(columns=SET_COLUMNS)
    d = pd.concat(rows, ignore_index=True)
    d["symbol"] = d["col"].map(sym)
    return d[SET_COLUMNS]


def _hgnc_groups(ann, h):
    """HGNC gene groups as sets: group name, id, size = approved genes in the group, members = matched cols."""
    if not (h["gene_group"] != "").any():
        return pd.DataFrame(columns=SET_COLUMNS)
    names = h["gene_group"].str.split("|")
    ids = h["gene_group_id"].str.split("|")
    ok = names.str.len() == ids.str.len()
    e = pd.DataFrame({"j": np.repeat(np.arange(len(h))[ok.to_numpy()], names[ok].str.len().to_numpy()),
                      "set": np.concatenate(names[ok].to_numpy()) if ok.any() else [],
                      "set_id": np.concatenate(ids[ok].to_numpy()) if ok.any() else []})
    e = e[e["set"].str.strip() != ""]
    size = e.groupby("set_id")["j"].nunique()
    jc = ann[ann["matched_j"] >= 0]
    e = e.merge(pd.DataFrame({"j": jc["matched_j"].to_numpy(), "col": jc["col"].to_numpy(),
                              "symbol": jc["symbol"].to_numpy()}), on="j")
    e["set_size"] = e["set_id"].map(size).astype(np.int64)
    e["n_present"] = e.groupby("set_id")["col"].transform("nunique")
    e = e[(e["n_present"] >= SET_MIN) & (e["n_present"] <= SET_MAX)]
    e["source"] = "hgnc_group"
    return e.drop_duplicates(["set_id", "col"])[SET_COLUMNS]


def string_pairs(links_path, info_path, ann, prots, symmap, min_score=400):
    """STRING links (both directions in the file) -> unique (col_a < col_b, best score) with score >= min_score.
    Protein -> col by ENSP -> ENSG (Ensembl GTF) -> col, else STRING's preferred_name -> col."""
    import pyarrow as pa
    import pyarrow.compute as pc
    import pyarrow.csv as pacsv

    info = pd.read_csv(info_path, sep="\t", usecols=[0, 1], dtype=str, keep_default_na=False)
    info.columns = ["sid", "name"]
    ens2col = {}
    for key in ("hgnc_ensembl", "ensembl_id"):                # Tahoe's own id wins
        ens2col.update({e: int(c) for e, c in zip(ann[key], ann["col"]) if e})
    col = pd.Series(-1, index=info.index, dtype=np.int64)
    if prots is not None and len(prots):
        p2g = prots.set_index("protein_id")["gene_id"]
        ensp = info["sid"].str.split(".", n=1).str[1]
        col = ensp.map(p2g).map(ens2col).fillna(-1).astype(np.int64)
    miss = col < 0
    col[miss] = info.loc[miss, "name"].map(symmap).fillna(-1).astype(np.int64)
    by_ens, by_name = int((~miss).sum()), int(((col >= 0) & miss).sum())
    keep = (col >= 0).to_numpy()
    value_set = pa.array(info["sid"].to_numpy()[keep].tolist(), type=pa.string())
    colv = col.to_numpy()[keep]
    reader = pacsv.open_csv(links_path, read_options=pacsv.ReadOptions(block_size=1 << 24),
                            parse_options=pacsv.ParseOptions(delimiter=" "),
                            convert_options=pacsv.ConvertOptions(column_types={
                                "protein1": pa.string(), "protein2": pa.string(), "combined_score": pa.int32()}))
    A, B, S = [], [], []
    n_rows = n_hi = 0
    for b in reader:
        n_rows += b.num_rows
        b = b.filter(pc.greater_equal(b.column("combined_score"), min_score))
        n_hi += b.num_rows
        i1 = pc.index_in(b.column("protein1"), value_set=value_set).fill_null(-1).to_numpy(zero_copy_only=False)
        i2 = pc.index_in(b.column("protein2"), value_set=value_set).fill_null(-1).to_numpy(zero_copy_only=False)
        s = b.column("combined_score").to_numpy(zero_copy_only=False)
        m = (i1 >= 0) & (i2 >= 0)
        a, c = colv[i1[m]], colv[i2[m]]
        m2 = a != c
        A.append(np.minimum(a, c)[m2])
        B.append(np.maximum(a, c)[m2])
        S.append(s[m][m2])
    a = np.concatenate(A) if A else np.zeros(0, np.int64)
    c = np.concatenate(B) if B else np.zeros(0, np.int64)
    s = np.concatenate(S) if S else np.zeros(0, np.int32)
    d = pd.DataFrame({"col_a": a.astype(np.int64), "col_b": c.astype(np.int64), "score": s.astype(np.int32)})
    d = (d.sort_values("score", ascending=False, kind="stable").drop_duplicates(["col_a", "col_b"])
         .sort_values(["col_a", "col_b"]).reset_index(drop=True))
    stats = {"n_links_file": n_rows, "n_links_ge_min": n_hi, "proteins": len(info), "proteins_by_ensembl": by_ens,
             "proteins_by_name": by_name}
    return d, stats


# ----------------------------------------------------------------------------- the stage
def _add_hgnc(ann, t, path):
    """Match to HGNC and fill the HGNC fields of ann; returns the HGNC table."""
    h = read_hgnc(path)
    n = len(ann)
    idx, how = match_hgnc(t, h)
    ok = idx >= 0
    j = idx[ok]
    ann["matched_j"] = idx
    ann["matched_by"] = how
    for dst, src in (("hgnc_id", "hgnc_id"), ("hgnc_symbol", "symbol"), ("name", "name"),
                     ("locus_group", "locus_group"), ("locus_type", "locus_type"), ("location", "location"),
                     ("aliases", "alias_symbol"), ("prev_symbols", "prev_symbol"), ("gene_groups", "gene_group"),
                     ("hgnc_ensembl", "ensembl_gene_id"), ("hgnc_uniprot", "uniprot_ids")):
        ann.loc[ok, dst] = h[src].to_numpy()[j]
    ann.loc[ok, "entrez_id"] = pd.to_numeric(pd.Series(h["entrez_id"].to_numpy()[j]), errors="coerce").to_numpy()
    ann.loc[ok, "uniprot"] = h["uniprot_ids"].to_numpy()[j]          # replaced by the reviewed entry, if any
    vc = pd.Series(how).value_counts()
    named = ~t["symbol"].str.match(r"^ENSG\d+").to_numpy()
    log(f"  HGNC: {len(h):,} approved records; {int(ok.sum()):,} of {n:,} genes matched ({100 * ok.mean():.1f}%; "
        f"of genes with a symbol {100 * ok[named].mean() if named.any() else 0:.1f}%): "
        + ", ".join(f"{k} {int(vc.get(k, 0)):,}" for k in ("ensembl_id", "symbol", "prev_symbol", "alias_symbol")))
    return h


def _add_ensembl(ann, path):
    gtf, prots = read_gtf(path)
    k = _coords(ann, gtf)
    log(f"  Ensembl: {len(gtf):,} genes in the GTF; coordinates for {k:,} of {len(ann):,} Tahoe genes "
        f"({100 * k / max(len(ann), 1):.1f}%)")
    return gtf, prots


def _add_uniprot(ann, path, approved):
    u = read_uniprot(path)
    k = _uniprot(ann, u, approved)
    log(f"  UniProt: {len(u):,} reviewed entries; {k:,} Tahoe genes have one "
        f"({int((ann['function'] != '').sum()):,} with FUNCTION text)")
    return len(u)


def _add_ncbi(ann, path):
    s = read_ncbi(path)
    key = ann["entrez_id"].astype("string").fillna("")
    ann["ncbi_summary"] = key.map(s).fillna("").astype(str).to_numpy()
    log(f"  NCBI: {len(s):,} human summaries; {int((ann['ncbi_summary'] != '').sum()):,} Tahoe genes have one")
    return len(s)


def _guard(key, recs, fn, *args):
    """fn(*args); on any error log it, mark the source failed and return None (every source is optional)."""
    try:
        return fn(*args)
    except Exception as e:  # noqa: BLE001 - a broken or unexpected file must not stop the pipeline
        msg = f"{type(e).__name__}: {e}"
        log(f"  {key}: could not be used ({msg}); continuing without it (a damaged cached file is downloaded "
            "again after deleting it, or with refresh)")
        recs.setdefault(key, {}).update(status="unusable", error=msg)
        return None


def run(out, offline=False, cache_dir=None, refresh=False, sources=None, min_string_score=400, tries=4,
        timeout=120):
    """out = the tahoemap output folder. Writes out/reference/.
    offline: use only cached files; cache_dir: download cache (default out/reference/downloads); refresh: download
    again even if cached; sources: subset of SOURCES keys (default all); min_string_score: STRING cut (400 = medium
    confidence); tries / timeout: per download (seconds per socket read)."""
    t0 = time.time()
    rd = folder(out, "reference")
    cache_dir = cache_dir or os.path.join(rd, "downloads")
    os.makedirs(cache_dir, exist_ok=True)
    t = tahoe_genes(out)
    n = len(t)
    log(f"Reference: {n:,} genes ({int((t['ensembl_id'] != '').sum()):,} with an Ensembl id); cache {cache_dir}"
        + (" (offline)" if offline else ""))

    todo = [s for s in SOURCES if not sources or s["key"] in sources]
    need = [s for s in todo if refresh or not (os.path.exists(os.path.join(cache_dir, s["file"]))
                                               and os.path.getsize(os.path.join(cache_dir, s["file"])) > 0)]
    probes = {}
    if need and not offline:
        log(f"  sizes of the {len(need)} file(s) to download:")
        for s in need:
            probes[s["key"]] = _probe(s["url"]) if s.get("probe", True) else (None, "")
            log(f"    {s['key']:<13} {_mb(probes[s['key']][0]):>12}  {s['url'][:100]}"
                + ("  (streamed query: no size)" if not s.get("probe", True) else ""))
        known = [v[0] for v in probes.values() if v[0]]
        log(f"    total {_mb(sum(known))}" + (" + unknown" if len(known) < len(need) else ""))
    files, recs = {}, {}
    for s in todo:
        size, lm = probes.get(s["key"], (None, ""))
        files[s["key"]], recs[s["key"]] = fetch(s, cache_dir, offline=offline, refresh=refresh, tries=tries,
                                                timeout=timeout, size=size, last_modified=lm)
        if recs[s["key"]]["status"] == "cached":
            log(f"  {s['key']}: cached ({_mb(recs[s['key']]['bytes'])}, {recs[s['key']]['date'][:10]})")
        elif recs[s["key"]]["status"].startswith("offline"):
            log(f"  {s['key']}: not cached; skipped (offline)")

    def rows(key, k):
        if key in recs and k is not None:
            recs[key]["n_rows"] = int(k)

    # ---- annotations: Tahoe's own symbol and Ensembl id, then each source in turn
    ann = pd.DataFrame({"col": t["col"].to_numpy(), "symbol": t["symbol"].to_numpy(),
                        "ensembl_id": t["ensembl_id"].to_numpy()})
    for c in ANN_COLUMNS:
        if c not in ann:
            ann[c] = ""
    for c in ("start", "end", "entrez_id"):
        ann[c] = pd.array([pd.NA] * n, dtype="Int64")
    ann["matched_by"] = "none"
    ann["hgnc_ensembl"] = ""
    ann["hgnc_uniprot"] = ""
    ann["matched_j"] = -1
    h = _guard("hgnc", recs, _add_hgnc, ann, t, files["hgnc"]) if files.get("hgnc") else None
    rows("hgnc", None if h is None else len(h))
    gtf, prots = None, None
    if files.get("ensembl"):
        log("  Ensembl GTF: reading gene rows (streaming; cached as parquet after the first run) ...")
        res = _guard("ensembl", recs, _add_ensembl, ann, files["ensembl"])
        if res is not None:
            gtf, prots = res
            rows("ensembl", len(gtf))
    loc_chrom = _chrom_from_location(ann["location"])
    fill = (ann["chrom"] == "") & (loc_chrom != "")
    ann.loc[fill, "chrom"] = loc_chrom[fill]
    approved = set(h["symbol"]) if h is not None else set()
    if files.get("uniprot"):
        rows("uniprot", _guard("uniprot", recs, _add_uniprot, ann, files["uniprot"], approved))
    if files.get("ncbi"):
        rows("ncbi", _guard("ncbi", recs, _add_ncbi, ann, files["ncbi"]))

    # ---- gene sets
    symmap = symbol_to_col(ann, h)
    parts = []
    for key, label in (("hallmark", "hallmark"), ("reactome", "reactome")):
        if files.get(key):
            sets = _guard(key, recs, read_gmt, files[key])
            if sets is not None:
                rows(key, len(sets))
                d = _sets_long(label, sets, symmap, ann)
                parts.append(d)
                log(f"  {label}: {len(sets):,} sets; {d['set'].nunique():,} with {SET_MIN}-{SET_MAX} Tahoe genes "
                    f"({len(d):,} memberships, {d['col'].nunique():,} genes)")
    if h is not None:
        d = _guard("hgnc_group", recs, _hgnc_groups, ann, h)
        if d is not None:
            parts.append(d)
            log(f"  HGNC gene groups: {d['set'].nunique():,} with {SET_MIN}-{SET_MAX} Tahoe genes "
                f"({len(d):,} memberships)")
    gs = pd.concat([p for p in parts if len(p)], ignore_index=True) if any(len(p) for p in parts) \
        else pd.DataFrame(columns=SET_COLUMNS)
    gs = gs.astype({"source": str, "set": str, "col": np.int64, "symbol": str, "set_id": str,
                    "set_size": np.int64, "n_present": np.int64})

    # ---- STRING
    sp = pd.DataFrame({"col_a": np.zeros(0, np.int64), "col_b": np.zeros(0, np.int64), "score": np.zeros(0, np.int32)})
    sstats = {}
    if files.get("string_links") and files.get("string_info"):
        res = _guard("string_links", recs, string_pairs, files["string_links"], files["string_info"], ann, prots,
                     symmap, int(min_string_score))
        if res is not None:
            sp, sstats = res
            rows("string_links", sstats["n_links_ge_min"])
            rows("string_info", sstats["proteins"])
            nk = len(set(sp["col_a"]) | set(sp["col_b"]))
            log(f"  STRING: {sstats['n_links_file']:,} links, {sstats['n_links_ge_min']:,} with score >= "
                f"{min_string_score}; proteins on genes {sstats['proteins_by_ensembl']:,} by Ensembl id + "
                f"{sstats['proteins_by_name']:,} by name of {sstats['proteins']:,}; {len(sp):,} gene pairs over "
                f"{nk:,} genes")
    elif files.get("string_links") or files.get("string_info"):
        log("  STRING: needs both protein.links and protein.info; skipped")

    ann = ann[ANN_COLUMNS].copy()
    for c in ANN_COLUMNS:
        if c not in ("col", "start", "end", "entrez_id"):
            ann[c] = ann[c].fillna("").astype(str)
    write_parquet(ann, os.path.join(rd, "annotations.parquet"))
    write_parquet(gs, os.path.join(rd, "gene_sets.parquet"))
    write_parquet(sp, os.path.join(rd, "string_pairs.parquet"))
    for s in todo:
        recs[s["key"]].setdefault("n_rows", None)
    vc = ann["matched_by"].value_counts()
    info = {"version": VERSION, "genes": n, "offline": bool(offline), "cache_dir": cache_dir,
            "hgnc_matched": int((ann["matched_by"] != "none").sum()),
            "matched_by": {k: int(v) for k, v in vc.items()},
            "with_coordinates": int(ann["start"].notna().sum()), "with_chrom": int((ann["chrom"] != "").sum()),
            "with_uniprot_function": int((ann["function"] != "").sum()),
            "with_ncbi_summary": int((ann["ncbi_summary"] != "").sum()),
            "gene_sets": {k: int(v) for k, v in gs.groupby("source")["set"].nunique().items()},
            "gene_set_memberships": int(len(gs)), "string_pairs": int(len(sp)), "string": sstats,
            "sources": {k: v.get("status") for k, v in recs.items()},
            "minutes": round((time.time() - t0) / 60, 2)}
    write_json({"written": _now(), "cache_dir": cache_dir, "sources": recs, "summary": info},
               os.path.join(rd, "sources.json"))
    stamp_stage(out, "reference", VERSION, info)
    log(f"Reference done: {info['hgnc_matched']:,}/{n:,} genes matched to HGNC, {len(gs):,} set memberships, "
        f"{len(sp):,} STRING pairs -> {rd} ({info['minutes']} min)")
    return info
