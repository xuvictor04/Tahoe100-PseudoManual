#!/usr/bin/env python3
"""Fetch citable annotation for every gene in the vault, from the three authoritative registries.

Why this exists. Most of the 343 genes the study touches have no literature worth a written note, and for
those the honest citation is **not a paper** - it is a database accession. An accession is stable, checkable,
and cannot be hallucinated: HGNC:16166 either is TRIM72 or it is not. So rather than ask a model what it
remembers about MBOAT1, this fetches what the registries actually record and stores it, with the accession
that backs each field.

    HGNC   genenames.org   the naming authority: official name, aliases, locus type, chromosomal location,
                           gene family membership (`gene_group` - the relation data the vault organises on),
                           and cross-references to everything else, including PubMed IDs for the gene's
                           naming/characterisation papers.
    NCBI   E-utilities     the summary paragraph. For an obscure gene this is usually the only prose that
                           exists, and much of it is explicitly marked as inferred ("Predicted to ...").
    UniProt                the reviewed protein function text, where a reviewed (Swiss-Prot) entry exists.
                           Unreviewed TrEMBL entries are recorded as such and their text is not used.

Output is `annotations.json` next to this script, committed to the repository so the vault builds without
network access and so every claim in a generated note can be audited against what was actually returned.
Each record carries `fetched_utc` and the exact query used.

Usage:
    python3 knowledge/_build/fetch_annotations.py                      # all genes in gene_universe.csv
    python3 knowledge/_build/fetch_annotations.py --only TRIM72,MDM2   # refresh a few
    python3 knowledge/_build/fetch_annotations.py --missing-only       # only genes not already cached
"""
import argparse
import datetime
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "annotations.json")
UNIVERSE = os.path.join(HERE, "gene_universe.csv")

#: A contact-free, descriptive agent string. NCBI asks that automated clients identify themselves; it asks
#: for a tool name and an email, and we send only the tool name - the user's address is not ours to publish.
UA = "Tahoe100-PseudoManual-vault-builder/1.0 (research; see repository README)"
HGNC = "https://rest.genenames.org/fetch/%s/%s"
NCBI = ("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
        "?db=gene&retmode=json&id=%s")
UNIP = ("https://rest.uniprot.org/uniprotkb/search?format=json&size=%d"
        "&fields=accession,reviewed,protein_name,cc_function,gene_names&query=%s")


def get(url, tries=4, pause=0.4):
    """One GET with retries. Returns parsed JSON, or None after the last failure."""
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={"Accept": "application/json", "User-Agent": UA})
            with urllib.request.urlopen(req, timeout=40) as fh:
                return json.loads(fh.read().decode("utf-8", "replace"))
        except (urllib.error.URLError, urllib.error.HTTPError, ValueError, TimeoutError) as e:
            if i == tries - 1:
                print("    failed: %s (%s)" % (url[:90], e), file=sys.stderr)
                return None
            time.sleep(pause * (2 ** i))
    return None


def hgnc_one(sym):
    """HGNC by symbol, then by Ensembl gene id for the ENSG-only identifiers, then by alias."""
    for field, value in (("symbol", sym), ("ensembl_gene_id", sym), ("alias_symbol", sym),
                         ("prev_symbol", sym)):
        if field == "ensembl_gene_id" and not sym.startswith("ENSG"):
            continue
        if field in ("alias_symbol", "prev_symbol") and sym.startswith("ENSG"):
            continue
        d = get(HGNC % (field, urllib.parse.quote(sym)))
        docs = ((d or {}).get("response") or {}).get("docs") or []
        if docs:
            return docs[0], field
    return None, None


def ncbi_batch(entrez_ids):
    """One esummary call for up to 100 Entrez gene ids. Returns {id: record}."""
    out = {}
    for i in range(0, len(entrez_ids), 100):
        chunk = [str(x) for x in entrez_ids[i:i + 100]]
        d = get(NCBI % ",".join(chunk))
        res = (d or {}).get("result") or {}
        for k, v in res.items():
            if k != "uids" and isinstance(v, dict):
                out[str(k)] = v
        time.sleep(0.4)                     # NCBI asks for <= 3 requests/second without an API key
    return out


def uniprot_batch(accessions):
    """Reviewed-first lookup for up to 50 accessions at a time. Returns {accession: record}."""
    out = {}
    for i in range(0, len(accessions), 50):
        chunk = [a for a in accessions[i:i + 50] if a]
        if not chunk:
            continue
        q = urllib.parse.quote(" OR ".join("accession:%s" % a for a in chunk))
        d = get(UNIP % (len(chunk) * 2, q))
        for r in (d or {}).get("results") or []:
            out[r.get("primaryAccession", "")] = r
        time.sleep(0.3)
    return out


def function_text(rec):
    """The FUNCTION comment from a UniProt record, flattened, with its review status."""
    if not rec:
        return None, None
    reviewed = str(rec.get("entryType", "")).startswith("UniProtKB reviewed")
    for c in rec.get("comments") or []:
        if c.get("commentType") == "FUNCTION":
            bits = [t.get("value", "") for t in c.get("texts") or []]
            txt = " ".join(b for b in bits if b).strip()
            if txt:
                return txt, reviewed
    return None, reviewed


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--only", default="", help="comma-separated symbols to fetch")
    ap.add_argument("--missing-only", action="store_true", help="skip symbols already in annotations.json")
    a = ap.parse_args()

    cache = {}
    if os.path.exists(OUT):
        cache = json.load(open(OUT))

    if a.only:
        syms = [s.strip() for s in a.only.split(",") if s.strip()]
    else:
        syms = sorted(pd.read_csv(UNIVERSE)["symbol"].astype(str))
    if a.missing_only:
        syms = [s for s in syms if s not in cache]
    print("fetching %d symbols" % len(syms))

    now = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")

    # --- pass 1: HGNC, one per symbol. This is what everything else keys off.
    for n, sym in enumerate(syms, 1):
        doc, matched_by = hgnc_one(sym)
        rec = {"symbol": sym, "fetched_utc": now,
               "hgnc": None if doc is None else {
                   "hgnc_id": doc.get("hgnc_id"), "name": doc.get("name"),
                   "symbol": doc.get("symbol"), "aliases": doc.get("alias_symbol") or [],
                   "alias_names": doc.get("alias_name") or [],
                   "prev_names": doc.get("prev_name") or [],
                   "location": doc.get("location"), "locus_type": doc.get("locus_type"),
                   "locus_group": doc.get("locus_group"),
                   "gene_family": doc.get("gene_group") or [],
                   "gene_family_ids": doc.get("gene_group_id") or [],
                   "entrez_id": doc.get("entrez_id"), "ensembl_gene_id": doc.get("ensembl_gene_id"),
                   "uniprot_ids": doc.get("uniprot_ids") or [], "omim_id": doc.get("omim_id") or [],
                   "pubmed_id": doc.get("pubmed_id") or [], "status": doc.get("status"),
                   "matched_by": matched_by}}
        cache[sym] = rec
        if n % 25 == 0 or n == len(syms):
            print("  HGNC %d/%d" % (n, len(syms)))
            json.dump(cache, open(OUT, "w"), indent=1, sort_keys=True)
        time.sleep(0.15)

    # --- pass 2: NCBI summaries, batched by Entrez id
    ids = [str(cache[s]["hgnc"]["entrez_id"]) for s in syms
           if cache[s].get("hgnc") and cache[s]["hgnc"].get("entrez_id")]
    print("NCBI esummary for %d ids" % len(ids))
    nc = ncbi_batch(ids)
    for s in syms:
        h = cache[s].get("hgnc") or {}
        r = nc.get(str(h.get("entrez_id"))) if h.get("entrez_id") else None
        cache[s]["ncbi"] = None if not r else {
            "entrez_id": str(h.get("entrez_id")), "description": r.get("description"),
            "summary": (r.get("summary") or "").strip() or None,
            "maplocation": r.get("maplocation"), "other_aliases": r.get("otheraliases"),
            "chromosome": r.get("chromosome")}

    # --- pass 3: UniProt function text, batched by accession
    accs = []
    for s in syms:
        h = cache[s].get("hgnc") or {}
        accs += [x for x in (h.get("uniprot_ids") or [])][:1]
    accs = [a for a in accs if a]
    print("UniProt for %d accessions" % len(accs))
    up = uniprot_batch(accs)
    for s in syms:
        h = cache[s].get("hgnc") or {}
        acc = (h.get("uniprot_ids") or [None])[0]
        rec = up.get(acc) if acc else None
        txt, reviewed = function_text(rec)
        cache[s]["uniprot"] = None if not acc else {
            "accession": acc, "reviewed": reviewed, "function": txt,
            "protein_name": (((rec or {}).get("proteinDescription") or {}).get("recommendedName") or {})
            .get("fullName", {}).get("value")}

    json.dump(cache, open(OUT, "w"), indent=1, sort_keys=True)

    have_h = sum(1 for s in syms if cache[s].get("hgnc"))
    have_n = sum(1 for s in syms if (cache[s].get("ncbi") or {}).get("summary"))
    have_u = sum(1 for s in syms if (cache[s].get("uniprot") or {}).get("function"))
    fam = sum(1 for s in syms if (cache[s].get("hgnc") or {}).get("gene_family"))
    print("\nwrote %s" % OUT)
    print("  HGNC record:      %d of %d" % (have_h, len(syms)))
    print("  NCBI summary:     %d" % have_n)
    print("  UniProt function: %d" % have_u)
    print("  gene family:      %d" % fam)


if __name__ == "__main__":
    main()
