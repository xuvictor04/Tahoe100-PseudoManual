"""vault - the Obsidian vault: one note per gene, drug, cell line, plate and module, built from the run's tables.

The vault (OUT/vault/) is the reading room of a run. Everything a gene note says is read from the tables the earlier
stages wrote; nothing is re-estimated here. Two layers, kept apart on purpose (the convention of the earlier
MG53/p53 vault):

    generated   every note's frontmatter and data sections, the indexes, Home, How to read this vault, the module
                canvases. Rebuilt on every run, so always consistent with the data; never edit them by hand.
    written     tahoemap/vault_seed/: genes/<SYMBOL>.md fragments (what a gene IS) spliced under the gene note's
                title, and notes/<Title>.md concept notes copied to Concepts/. They survive every rebuild.

Notes (basenames are unique vault-wide, case-insensitively, because Obsidian resolves [[links]] by basename):

    Genes/<chrom>/<name>.md            every gene column of atlas/effects/genes.csv (name = label: the symbol, or
                                       'SYM (ENSG...)' when Tahoe lists the symbol twice); chrom from the reference
                                       annotation, else 'unplaced'
    Genes/<chrom>/<name> — plates.md   the gene's raw CPM and corrected well effect (W2) in every well, as 8 x 12
                                       grids per plate
    Drugs/<drug> (drug).md, Cell lines/<cell name> (line).md, Plates/Plate NN.md,
    Modules/Module NNN.md + Module NNN.canvas, Indexes/..., Home.md, How to read this vault.md, Concepts/...

Rules: frontmatter values are json.dumps'ed (valid YAML); wikilinks are bare [[basename]]; a gene note links only
to its partners, its drugs, the cell lines, its module and its plates note (never to boilerplate notes, which would
turn them into hubs of 16,000 links); output is sorted and carries no timestamps, so an unchanged run rewrites
nothing; generated files carry `generated_by: "tahoemap"` and only such files are ever deleted as stale.

What a note claims is the earlier stages' own rule, quoted with this run's numbers, so that a sentence never says
more than the data behind it: per-line counts and 'strongest' use the per-line |z| cut the tables stage calibrated
(tables/info.json line_z_threshold, with the expected number of chance calls); a partner is called reliable only with
evidence 'both halves' (same sign with fdr <= 0.10 in two random halves of the compounds) and its fdr is printed;
'one half' is never called replication; 'novel candidate' is shown only when relations/info.json says novelty could be
assessed (else which reference sources were missing); 'not in the vector space' states the embed stage's rule with
its counts (embed/info.json); a module's arms are said to move opposite only when graph/modules.parquet says so
(arms_opposite); pooled lists are named as medians over the lines, with the single-line view (drug_line_top) beside a
short one; lines that are not measured (tensor/line_measured.npy: ambient-only) are marked. A written gene fragment
that speaks of a score, rank, regulon or association of the earlier MG53/p53 study is spliced under a callout that
says so.

Literature reviews (optional; tahoemap/review, docs/review.md): when OUT/review holds reviews (review/notes/<kind>/,
review/reviews/<kind>/, review/connections.parquet), the note of every reviewed gene, drug or cell line gets a section
"## What the literature says": a callout (written by an AI agent: which agent, model and effort, the date, the
verification counts, relative links to the run's history file and review JSON) above the agent's note body (its
headings demoted below the note's own, its wikilinks kept only where a note exists), then its connection verdicts.
The partner tables of a gene note get a Literature column (the connection verdict of the gene's review, else of the
partner's, with linked citations) when a shown partner has a verdict. The vault and map stamps record
review_fingerprint(OUT), so a review run makes both out of date. Without reviews no note changes.
"""

import hashlib
import json
import math
import os
import re
import time
import urllib.parse
import warnings

import numpy as np
import pandas as pd

from . import atlas_core as A
from . import graph as GR
from . import relations as REL
from . import tensor as TN
from . import tlib as T
from .common import folder, log, read_effects_index, safe_filename, stamp_stage

VERSION = 2
GEN = "tahoemap"
SEED_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "vault_seed")
MANIFEST = ".tahoemap-manifest.json"

LFC_MIN = A.LFC_MIN                  # log2(1.2): the atlas's smallest counted change
Q_CUT = A.Q_CUT                      # 0.10
N_DRUGS = 15                         # drug-doses per direction in a gene note
N_FLAGGED = 5
N_PARTNERS = 12
N_PRED = 5
N_GLANCE = 3                         # partners per direction in 'At a glance'
LINE_Z_FALLBACK = 4.0                # per-line |z| cut for a run whose tables/info.json has no calibrated
                                     # line_z_threshold (older tables stage); then it is NOT calibrated
LINE_FOLD_FALLBACK = math.log2(1.5)  # per-line counts need >= 1.5x (tables/info.json line_fold_min)
REPRO_FDR = REL.REPRO_FDR            # 'both halves' = same sign in two random halves of the compounds, fdr <= this
SHORT_POOLED = 3                     # fewer clean significant pooled drug-doses than this: add the single-line view
N_SINGLE = 3                         # drug-doses in the 'In single lines' sentence
ARMS_OPPOSITE = GR.ARMS_OPPOSITE     # graph stage: a - arm needs a mean cosine between the sides <= this ...
ARM_MIN = GR.MIN_MODULE              # ... and >= this many genes on the - side
OLD_STUDY_RE = re.compile(r"regulon|activity score|\brank\b|this batch|the association|MG53", re.I)
OLD_STUDY_NOTE = ("> [!note] Written for the earlier MG53/p53 study\n"
                  "> The written section below was written for an earlier study on the same data (MG53/TRIM72 and "
                  "p53). Where it mentions a score, a rank, a regulon, an association or \"this batch\", it refers "
                  "to that study's analysis (transcription-factor activity inferred from target sets, and MG53 as the "
                  "exposure), which tahoemap does not compute. This run's own numbers are in the generated sections "
                  "below.")
MAX_TEXT = 500                       # registry text (UniProt function, NCBI summary) is cut here in a gene note
GENES_PER_INDEX = 1000              # entries per 'Genes X' index note
NAMES_PER_INDEX = 5000              # names per 'Below detection X' index note
CANVAS_SPAN = 3000
NODE_W, NODE_H = 180, 50
ROWS = "ABCDEFGH"
CHROMS = {str(i) for i in range(1, 23)} | {"X", "Y", "MT"}
UNTRUSTED = ("unreliable plate only", "position not correctable", "wells disagree")


# ----------------------------------------------------------------------------- formatting
def _finite(x):
    try:
        return x is not None and math.isfinite(float(x))
    except (TypeError, ValueError):
        return False


def g3(x, dash="—"):
    """3 significant digits, plain notation down to 0.001."""
    if not _finite(x):
        return dash
    x = float(x)
    if x == 0:
        return "0"
    a = abs(x)
    if a >= 1000:
        return f"{x:,.0f}"
    if a < 0.001:
        return f"{x:.1e}"
    d = max(0, 2 - int(math.floor(math.log10(a))))
    return f"{x:.{d}f}"


def ffold(fold):
    return g3(fold) + "×" if _finite(fold) else "—"


def flfc_fold(lfc):
    return ffold(2.0 ** float(lfc)) if _finite(lfc) else "—"


def fz(z):
    return f"{float(z):+.1f}" if _finite(z) else "—"


def fq(q):
    if not _finite(q):
        return "—"
    q = float(q)
    if q < 1e-3:
        return f"{q:.0e}"
    return f"{q:.3f}" if q < 0.1 else f"{q:.2f}"


def flog(x):
    return f"{float(x):+.2f}" if _finite(x) else "—"


def fcos(c):
    return f"{float(c):+.2f}" if _finite(c) else "—"


def fdose(d):
    s = str(d)
    return f"{s} µM" if s and s != "nan" else ""


def fint(x, dash="—"):
    return f"{int(x):,}" if _finite(x) else dash


def cell(s):
    """Text safe inside a markdown table cell."""
    return str(s).replace("|", "/").replace("\n", " ").strip()


def clip_text(s, n=MAX_TEXT):
    s = re.sub(r"\s+", " ", str(s)).strip()
    if len(s) <= n:
        return s
    cut = s[:n].rsplit(" ", 1)[0]
    return cut + " …"


def jval(v):
    """A frontmatter value (json.dumps-able; NaN -> null)."""
    if isinstance(v, (list, tuple)):
        return [jval(x) for x in v]
    if isinstance(v, (np.integer,)):
        return int(v)
    if isinstance(v, (np.bool_,)):
        return bool(v)
    if isinstance(v, (float, np.floating)):
        return float(v) if math.isfinite(float(v)) else None
    return v


def _parse_simple_yaml(block):
    """The flat frontmatter of a written note (key: value, key: [a, b]) as a dict, so it can be re-emitted with
    json.dumps values like every generated note."""
    out = {}
    for line in block.split("\n"):
        k, sep, v = line.partition(":")
        if not sep or not k.strip() or k.startswith(" "):
            continue
        v = v.strip()
        if v.startswith("[") and v.endswith("]"):
            out[k.strip()] = [x.strip().strip("'\"") for x in v[1:-1].split(",") if x.strip()]
        elif v.lower() in ("true", "false"):
            out[k.strip()] = v.lower() == "true"
        else:
            try:
                out[k.strip()] = json.loads(v)
            except ValueError:
                out[k.strip()] = v.strip("'\"")
    out.pop("generated_by", None)
    return out


def frontmatter(d):
    lines = ["---"]
    for k, v in d.items():
        lines.append(f"{k}: {json.dumps(jval(v), ensure_ascii=False)}")
    lines.append(f"generated_by: {json.dumps(GEN)}")
    lines.append("---")
    return "\n".join(lines) + "\n"


def table(header, rows):
    out = ["| " + " | ".join(header) + " |", "|" + "|".join("---" for _ in header) + "|"]
    out += ["| " + " | ".join(cell(x) for x in r) + " |" for r in rows]
    return out


def sval(x):
    """A string value or '' for missing."""
    if x is None:
        return ""
    if isinstance(x, float) and not math.isfinite(x):
        return ""
    s = str(x)
    return "" if s in ("nan", "None", "<NA>") else s


# ----------------------------------------------------------------------------- names and files
class Names:
    """Unique, safe note basenames (case-insensitive), as Obsidian resolves [[links]] by basename."""

    def __init__(self):
        self.taken = {}

    def add(self, want, alt=None):
        base = safe_filename(want)
        name = base
        if name.lower() in self.taken and alt:
            name = safe_filename(alt)
        i = 2
        while name.lower() in self.taken:
            name = safe_filename(f"{base} ({i})")
            i += 1
        self.taken[name.lower()] = name
        return name


class Writer:
    """Writes notes atomically, only when their text changed; remembers every path it owns."""

    def __init__(self, root):
        self.root = root
        self.paths = set()
        self.n_written = 0
        self.n_same = 0
        self.bytes = 0

    def write(self, rel, text):
        if not text.endswith("\n"):
            text += "\n"
        path = os.path.join(self.root, rel)
        assert path not in self.paths, f"two notes at {rel}"
        self.paths.add(path)
        data = text.encode("utf-8")
        self.bytes += len(data)
        try:
            if os.path.getsize(path) == len(data):
                with open(path, "rb") as fh:
                    if fh.read() == data:
                        self.n_same += 1
                        return
        except OSError:
            pass
        os.makedirs(os.path.dirname(path), exist_ok=True)
        tmp = path + ".tmp"
        with open(tmp, "wb") as fh:
            fh.write(data)
        os.replace(tmp, path)
        self.n_written += 1


def _is_generated(path):
    try:
        with open(path, encoding="utf-8", errors="replace") as fh:
            head = fh.read(4096)
    except OSError:
        return False
    if not head.startswith("---"):
        return False
    end = head.find("\n---", 3)
    return re.search(r'(?m)^generated_by:\s*"?' + GEN + r'\b', head[:end if end > 0 else len(head)]) is not None


def _clean_stale(root, keep, old_manifest):
    """Delete generated notes of an earlier build that this build did not write; never touch anything else."""
    removed = 0
    for dp, dn, fn in os.walk(root):
        dn[:] = [d for d in dn if not d.startswith(".")]
        for f in fn:
            p = os.path.join(dp, f)
            if p in keep:
                continue
            rel = os.path.relpath(p, root)
            if f.endswith(".md.tmp") or f.endswith(".canvas.tmp"):
                os.remove(p)
            elif f.endswith(".md") and _is_generated(p):
                os.remove(p)
                removed += 1
            elif f.endswith(".canvas") and rel in old_manifest:
                os.remove(p)
                removed += 1
    for dp, dn, fn in sorted(os.walk(root), key=lambda t: -len(t[0])):
        rel = os.path.relpath(dp, root)
        if dp != root and not any(x.startswith(".") for x in rel.split(os.sep)) and not os.listdir(dp):
            os.rmdir(dp)
    return removed


# ----------------------------------------------------------------------------- loading
def _read_json(path):
    if not os.path.exists(path):
        return None
    try:
        with open(path, encoding="utf-8") as fh:
            return json.load(fh)
    except (OSError, ValueError):
        return None


def _read(path, columns=None):
    return pd.read_parquet(path, columns=columns) if os.path.exists(path) else None


def _factor(s):
    """A string column as an object array that shares one str per distinct value ('' for missing)."""
    codes, uniq = pd.factorize(s, use_na_sentinel=True)
    lut = np.array([sval(x) for x in uniq] + [""], dtype=object)
    return lut[np.where(codes < 0, len(uniq), codes)]


def _chunks(groups, size, prefix, names):
    """Split letter groups into index notes of at most `size` entries: [(note name, tag, entries)]."""
    out = []
    for k, lst in groups.items():
        n = max(1, math.ceil(len(lst) / size))
        for i in range(n):
            tag = k if n == 1 else f"{k} {i + 1}"
            out.append((names.add(f"{prefix} {tag}"), tag, lst[i * size:(i + 1) * size]))
    return out


def _slices(keys, n):
    """Start offsets of each key 0..n-1 in a sorted key array: rows of key c are [s[c], s[c+1])."""
    return np.searchsorted(keys, np.arange(n + 1), side="left")


# ----------------------------------------------------------------------------- literature reviews (OUT/review)
REVIEW_KINDS = ("gene", "drug", "line")
LIT_CITES = 3                        # citations linked in a partner-table cell (the rest are counted)
LIT_HEADING = "What the literature says"
VERDICTS = ("established", "indirect", "plausible", "unexpected", "contradicted")   # submit_review's verdicts


def review_fingerprint(out):
    """What of OUT/review the vault and the map show: None when there is no review (no folder, or only a queue, dry
    run or cache), else {"notes": n, "reviews": n, "sha": ...} over the names, sizes and modification times of the
    review notes and JSONs and the content of connections.parquet (rewritten at the end of every review run). The
    vault and map stamps record it, so a review run makes both out of date (cli.stage_state)."""
    rd = os.path.join(out, "review")
    if not os.path.isdir(rd):
        return None
    items, n = [], {"notes": 0, "reviews": 0}
    for sub in ("notes", "reviews"):
        for kind in REVIEW_KINDS:
            d = os.path.join(rd, sub, kind)
            if not os.path.isdir(d):
                continue
            for e in os.scandir(d):
                if e.is_file() and e.name.endswith((".md", ".json")):
                    st = e.stat()
                    items.append(f"{sub}/{kind}/{e.name}\t{st.st_size}\t{st.st_mtime_ns}")
                    n[sub] += 1
    if not items:
        return None
    h = hashlib.sha256("\n".join(sorted(items)).encode("utf-8"))
    p = os.path.join(rd, "connections.parquet")
    if os.path.exists(p):
        with open(p, "rb") as fh:
            h.update(fh.read())
    return {**n, "sha": h.hexdigest()[:16]}


def review_connections(out, gene_col=None):
    """The connection verdicts of the reviews in OUT/review, one dict per verdict with the columns of
    review/connections.parquet (entity_id, kind, name, partner, partner_kind, partner_col, verdict, citations as
    'PMID:1;DOI:x', check, unverified, ...): from that table, else (not built yet: `tahoe review tables`) from the
    review JSONs. gene_col(name) -> col or None resolves gene partners the table left unresolved."""
    rd = os.path.join(out, "review")
    rows = []
    p = os.path.join(rd, "connections.parquet")
    if os.path.exists(p):
        try:
            rows = pd.read_parquet(p).to_dict("records")
        except Exception as e:  # noqa: BLE001
            log(f"  vault: cannot read {p} ({type(e).__name__}: {e}); verdicts read from the review JSONs")
            rows = None
    if not os.path.exists(p) or rows is None:
        rows = []
        for kind in REVIEW_KINDS:
            d = os.path.join(rd, "reviews", kind)
            for f in sorted(os.listdir(d)) if os.path.isdir(d) else []:
                r = _read_json(os.path.join(d, f)) if f.endswith(".json") else None
                if not isinstance(r, dict):
                    continue
                meta = r.get("meta") or {}
                for it in r.get("connection_verdicts") or []:
                    pt = str(it.get("partner") or "")
                    pk = pt.split(":", 1)[0] if pt.split(":", 1)[0] in ("drug", "line") and ":" in pt else "gene"
                    cits = [str(x) for x in it.get("citations") or []]
                    rows.append({"entity_id": meta.get("entity_id"), "kind": kind, "name": meta.get("name"),
                                 "partner": pt, "partner_kind": pk, "partner_col": None, "verdict": it.get("verdict"),
                                 "citations": ";".join(cits), "n_citations": len(cits),
                                 "check": (it.get("check") or {}).get("verdict", ""),
                                 "unverified": bool(it.get("unverified")), "model": meta.get("model"),
                                 "run_id": meta.get("run_id"), "reviewed": meta.get("reviewed")})
    if gene_col is not None:
        for r in rows:
            if sval(r.get("partner_kind")) in ("", "gene") and not _finite(r.get("partner_col")):
                c = gene_col(sval(r.get("partner")))
                r["partner_col"] = c if c is not None else None
    return rows


def citation_link(cid):
    """'PMID:123' -> [PMID:123](https://pubmed.ncbi.nlm.nih.gov/123/); 'DOI:10.x/y' -> a doi.org link; other text
    as it is."""
    s = str(cid).strip()
    m = re.match(r"(?i)^(?:PMID\s*:?\s*)?(\d{1,9})$", s)
    if m:
        return f"[PMID:{int(m.group(1))}](https://pubmed.ncbi.nlm.nih.gov/{int(m.group(1))}/)"
    m = re.match(r"(?i)^(?:DOI\s*:\s*|https?://(?:dx\.)?doi\.org/)?(10\.\d{4,9}/\S+)$", s)
    if m:
        doi = m.group(1)
        return f"[DOI:{doi}](https://doi.org/{urllib.parse.quote(doi, safe='/:;._-')})"
    return cell(s)


class Run:
    """Everything the vault draws on, loaded once and indexed by gene col / drug-dose row / line / plate."""

    def __init__(self, out):
        t0 = time.time()
        self.out = out
        fxd = os.path.join(out, "atlas", "effects")
        ix = read_effects_index(fxd)
        genes = ix["genes"]
        self.gK = gK = int((genes["kind"] == "gene").sum())
        self.dd = ix["drugdose"]
        self.lines_ix = ix["lines"]
        self.wells = ix["wells"]
        self.Dn, self.L, self.N = len(self.dd), len(self.lines_ix), len(self.wells)
        td = os.path.join(out, "tables")
        tg = pd.read_parquet(os.path.join(td, "genes.parquet"))
        tg = tg.set_index("col").reindex(np.arange(gK))
        self.tg = tg
        self.sym = tg["symbol"].fillna("").astype(str).to_numpy()
        self.label = tg["label"].fillna(pd.Series(self.sym, index=tg.index)).astype(str).to_numpy()
        self.token = genes["token"].to_numpy()[:gK]

        # reference annotation (optional)
        ann = _read(os.path.join(out, "reference", "annotations.parquet"))
        self.ann = ann.set_index("col").reindex(np.arange(gK)) if ann is not None else None
        self.sources = _read_json(os.path.join(out, "reference", "sources.json")) or {}
        st = ((self.sources.get("sources") or {}).get("hgnc") or {}).get("status")
        self.hgnc_status = st if st is not None else ("cached" if ann is not None else "not run")
        self.hallmark = [[] for _ in range(gK)]
        self.reactome = [[] for _ in range(gK)]
        gs = _read(os.path.join(out, "reference", "gene_sets.parquet"),
                   ["source", "set", "col", "n_present"])
        if gs is not None and len(gs):
            gs = gs.dropna(subset=["col"])
            gs = gs[gs["source"].isin(["hallmark", "reactome"])].sort_values(["col", "n_present", "set"])
            for src, c, s in zip(gs["source"].to_numpy(), gs["col"].astype(int).to_numpy(),
                                 gs["set"].astype(str).to_numpy()):
                if 0 <= c < gK:
                    (self.hallmark if src == "hallmark" else self.reactome)[c].append(s)

        # chromosome buckets and coordinates
        if self.ann is not None and "chrom" in self.ann:
            ch = self.ann["chrom"].astype(str).str.replace("^chr", "", regex=True).to_numpy()
            self.bucket = np.array([f"chr{c}" if c in CHROMS else "unplaced" for c in ch], dtype=object)
            self.start = pd.to_numeric(self.ann["start"], errors="coerce").to_numpy()
            self.end = pd.to_numeric(self.ann["end"], errors="coerce").to_numpy()
            self.strand = self.ann["strand"].astype(str).to_numpy()
        else:
            self.bucket = np.array(["unplaced"] * gK, dtype=object)
            self.start = self.end = np.full(gK, np.nan)
            self.strand = np.array([""] * gK, dtype=object)

        # lines, drugs, plates
        self.tl = pd.read_parquet(os.path.join(td, "lines.parquet")).sort_values("line").reset_index(drop=True)
        self.cell = self.tl["cell_name"].fillna(self.tl["cell_line_id"]).astype(str).to_numpy()
        self.tp53 = self.tl["tp53_status"].fillna("unknown").astype(str).to_numpy() \
            if "tp53_status" in self.tl else np.array(["unknown"] * self.L)
        self.tdd = pd.read_parquet(os.path.join(td, "drugdoses.parquet")).sort_values("dd").reset_index(drop=True)
        self.tdrugs = pd.read_parquet(os.path.join(td, "drugs.parquet")).sort_values("drug").reset_index(drop=True)
        self.tplates = pd.read_parquet(os.path.join(td, "plates.parquet"))
        self.dd_drug = self.tdd["drug"].astype(str).to_numpy()
        self.dd_dose = self.tdd["dose"].astype(str).to_numpy()
        self.dd_flags = self.tdd["flags"].fillna("").astype(str).to_numpy()
        self.dd_artifact = np.array([A.has_artifact(f) for f in self.dd_flags])
        self.dd_nsig = self.tdd["n_sig_genes"].to_numpy()

        # embed / graph / relations
        ed = os.path.join(out, "embed")
        eg = pd.read_parquet(os.path.join(ed, "genes.parquet")).set_index("col").reindex(np.arange(gK))
        self.included = eg["included"].fillna(False).astype(bool).to_numpy()
        self.n_resp = eg["n_responsive_contexts"].to_numpy()
        self.vnorm = eg["vector_norm"].to_numpy()
        self.vrep = eg["represented_fraction"].to_numpy()
        self.noise = eg["noise_rna"].fillna(False).astype(bool).to_numpy() if "noise_rna" in eg else \
            tg["noise_rna"].fillna(False).astype(bool).to_numpy()
        self.embed_info = _read_json(os.path.join(ed, "info.json")) or {}
        # the stages' own cuts (tables: calibrated per-line |z|; relations: was novelty assessable; tensor: masks)
        ti = _read_json(os.path.join(td, "info.json")) or {}
        self.line_z_calibrated = _finite(ti.get("line_z_threshold"))
        self.line_z = float(ti["line_z_threshold"]) if self.line_z_calibrated else LINE_Z_FALLBACK
        self.line_z_chance = float(ti["line_z_expected_chance"]) if _finite(ti.get("line_z_expected_chance")) \
            else None
        self.line_z_ndd = ti.get("line_z_n_clean_drugdoses")
        self.line_fold = 2.0 ** float(ti.get("line_fold_min", LINE_FOLD_FALLBACK) or LINE_FOLD_FALLBACK)
        ri = _read_json(os.path.join(out, "relations", "info.json")) or {}
        if "novel_assessed" in ri:
            self.novel_assessed = bool(ri["novel_assessed"])
            self.novel_blocked = [str(x) for x in (ri.get("novel_blocked_by") or [])]
        else:                                          # older relations stage: novelty needed the reference stage
            self.novel_assessed = ann is not None
            self.novel_blocked = [] if ann is not None else ["the reference stage"]
        tni = _read_json(os.path.join(out, "tensor", "info.json")) or {}
        self.amb_frac = float(tni.get("amb_frac", TN.AMB_FRAC) or TN.AMB_FRAC)
        self.e_min = float(tni.get("e_min", TN.E_MIN) or TN.E_MIN)
        gd = os.path.join(out, "graph")
        nodes = pd.read_parquet(os.path.join(gd, "nodes.parquet")).set_index("col").reindex(np.arange(gK))
        self.module = nodes["module"].fillna(-1).astype(int).to_numpy()
        self.arm = nodes["arm"].fillna("").astype(str).to_numpy()
        self.xy = nodes[["x", "y"]].to_numpy(dtype=float)
        self.xys = nodes[["xs", "ys"]].to_numpy(dtype=float)
        self.axis_proj = nodes["axis_proj"].to_numpy(dtype=float) if "axis_proj" in nodes else np.full(gK, np.nan)
        self.modules = pd.read_parquet(os.path.join(gd, "modules.parquet")).sort_values("module")
        # per module: do its two sides really move opposite (graph: arms_opposite, mean cos between the sides)?
        self.mod_opp, self.mod_between = {}, {}
        for r in self.modules.to_dict("records"):
            m = int(r["module"])
            self.mod_between[m] = float(r["mean_cos_between_arms"]) if _finite(r.get("mean_cos_between_arms")) \
                else np.nan
            if "arms_opposite" in r and r["arms_opposite"] is not None:
                self.mod_opp[m] = bool(r["arms_opposite"])
            else:                                      # older graph stage: a - arm was kept whenever it existed
                self.mod_opp[m] = int(r.get("n_minus", 0) or 0) > 0
        self.edges = pd.read_parquet(os.path.join(gd, "edges.parquet"))
        mpz = os.path.join(gd, "module_pooled_z.npy")
        self.mod_z = np.load(mpz) if os.path.exists(mpz) else None

        # validation (optional)
        vd = os.path.join(out, "validation")
        self.mod_label = {}
        p = os.path.join(vd, "module_labels.csv")
        if os.path.exists(p):
            ml = pd.read_csv(p)
            for r in ml.itertuples(index=False):
                self.mod_label[int(r.module)] = (sval(r.label), sval(getattr(r, "label_source", "")),
                                                 getattr(r, "label_q", np.nan))
        p = os.path.join(vd, "module_enrichment.csv")
        self.mod_enrich = pd.read_csv(p) if os.path.exists(p) else None
        p = os.path.join(vd, "novel_members.csv")
        self.novel_members = pd.read_csv(p) if os.path.exists(p) else None
        self.novel_by_col = {}
        if self.novel_members is not None:
            for r in self.novel_members.itertuples(index=False):
                self.novel_by_col.setdefault(int(r.col), []).append(r)
        self.mod_size = dict(zip(self.modules["module"].astype(int), self.modules["n_genes"].astype(int)))
        self.metrics = _read_json(os.path.join(vd, "metrics.json"))
        self.have_validation = os.path.isdir(vd) and self.metrics is not None
        log(f"  vault: indexes loaded ({time.time() - t0:.1f} s)")

    def load_gene_tables(self):
        """The per-gene tables, sorted once by gene so a gene's rows are one slice."""
        t0 = time.time()
        gK = self.gK
        td = os.path.join(self.out, "tables")
        de = pd.read_parquet(os.path.join(td, "drug_effects.parquet"),
                             columns=["col", "dd", "lfc", "fold", "z", "q_up", "q_down", "flags", "clean",
                                      "n_lines_measured", "n_lines_up", "n_lines_down", "lines_up", "lines_down",
                                      "pattern_up", "pattern_down"])
        o = np.lexsort((-de["z"].to_numpy(dtype=float), de["col"].to_numpy()))
        self.de = {}
        for c in de.columns:
            if c in ("flags", "lines_up", "lines_down", "pattern_up", "pattern_down"):
                self.de[c] = _factor(de[c])[o]          # one string object per distinct value
            else:
                self.de[c] = de[c].to_numpy()[o]
        self.de_s = _slices(self.de["col"], gK)
        del de
        le = pd.read_parquet(os.path.join(td, "line_effects.parquet"),
                             columns=["col", "line", "baseline_cpm", "expressed", "n_dd_up", "n_dd_down",
                                      "best_up_dd", "best_up_lfc", "best_up_z", "best_down_dd", "best_down_lfc",
                                      "best_down_z"])
        o = np.lexsort((le["line"].to_numpy(), le["col"].to_numpy()))
        self.le = {c: le[c].to_numpy()[o] for c in le.columns}
        self.le_s = _slices(self.le["col"], gK)
        del le
        rel = pd.read_parquet(os.path.join(self.out, "relations", "gene_relations.parquet"),
                              columns=["col_a", "col_b", "rank", "cos", "cos_half1", "cos_half2", "evidence", "fdr",
                                       "z_gene", "locus", "readthrough_risk", "distance_bp", "same_strand",
                                       "shared_gene_group", "shared_pathway", "string_score", "novel_candidate"])
        o = np.lexsort((rel["rank"].to_numpy(), rel["col_a"].to_numpy()))
        self.rel = {c: (_factor(rel[c]) if c in ("shared_pathway", "evidence") else rel[c].to_numpy())[o]
                    for c in rel.columns}
        self.rel_s = _slices(self.rel["col_a"], gK)
        del rel
        # the strongest (drug-dose, line) cells per gene (clean, per-line |z| >= the calibrated cut): the single-line
        # view of a gene whose pooled (median-over-lines) list is empty or short
        p = os.path.join(td, "drug_line_top.parquet")
        dlt = pd.read_parquet(p, columns=["col", "direction", "dd", "line", "lfc", "z"]) if os.path.exists(p) \
            else pd.DataFrame({"col": [], "direction": [], "dd": [], "line": [], "lfc": [], "z": []})
        o = np.lexsort((-np.abs(dlt["z"].to_numpy(dtype=float)), dlt["col"].to_numpy()))
        self.dlt = {c: dlt[c].to_numpy()[o] for c in dlt.columns}
        self.dlt["direction"] = self.dlt["direction"].astype(str)
        self.dlt_s = _slices(self.dlt["col"].astype(np.int64), gK)
        del dlt
        log(f"  vault: gene tables indexed ({time.time() - t0:.1f} s; {len(self.de['col']):,} drug-effect rows, "
            f"{len(self.rel['col_a']):,} relation rows)")

    def load_predictions(self, chunk=2048):
        """The drug-doses whose vectors predict the largest rise / fall of each gene (gene vector . drug-dose
        vector, scaled back to z units with the gene's row centre and scale of the embed stage)."""
        ed = os.path.join(self.out, "embed")
        gK, Dn = self.gK, self.Dn
        self.pred_up = np.full((gK, N_PRED), -1, dtype=np.int64)
        self.pred_dn = np.full((gK, N_PRED), -1, dtype=np.int64)
        self.pred_up_z = np.full((gK, N_PRED), np.nan, dtype=np.float32)
        self.pred_dn_z = np.full((gK, N_PRED), np.nan, dtype=np.float32)
        try:
            G = np.load(os.path.join(ed, "gene_vectors.npy"))
            Dv = np.load(os.path.join(ed, "drugdose_vectors.npy")).astype(np.float32)
            inc = np.load(os.path.join(ed, "included_cols.npy"))
            mu = np.load(os.path.join(ed, "gene_row_mean.npy"))
            sc = np.load(os.path.join(ed, "gene_row_scale.npy"))
        except OSError as e:
            log(f"  vault: no vector-space predictions ({e})")
            return
        k = min(N_PRED, Dn)
        for i0 in range(0, len(inc), chunk):
            cc = inc[i0:i0 + chunk]
            P = (G[cc].astype(np.float32) @ Dv.T) * sc[i0:i0 + chunk, None] + mu[i0:i0 + chunk, None]
            P = np.nan_to_num(P, nan=0.0)
            top = np.argpartition(-P, k - 1, axis=1)[:, :k]
            top = np.take_along_axis(top, np.argsort(-np.take_along_axis(P, top, 1), axis=1), 1)
            bot = np.argpartition(P, k - 1, axis=1)[:, :k]
            bot = np.take_along_axis(bot, np.argsort(np.take_along_axis(P, bot, 1), axis=1), 1)
            self.pred_up[cc, :k] = top
            self.pred_dn[cc, :k] = bot
            self.pred_up_z[cc, :k] = np.take_along_axis(P, top, 1)
            self.pred_dn_z[cc, :k] = np.take_along_axis(P, bot, 1)
        self.DD_z = np.load(os.path.join(self.out, "atlas", "effects", "DD_z.npy"), mmap_mode="r")


# ----------------------------------------------------------------------------- the vault
class Vault:
    def __init__(self, out):
        self.out = out
        self.root = os.path.join(out, "vault")
        self.R = Run(out)
        self.names = Names()
        self.W = Writer(self.root)
        self.n_fragments = 0
        self.n_old_study = 0
        self.gene_sizes = []
        self.plates_sizes = []

    # ------------------------------------------------------------------ names
    def assign_names(self):
        R, N = self.R, self.names
        self.fixed = {}
        for t in ("Home", "How to read this vault", "Genes by letter", "Genes by module", "Drugs by mechanism",
                  "Lines by organ", "Genes below the detection limit"):
            self.fixed[t] = N.add(t)
            assert self.fixed[t] == t
        # seed concept notes keep their titles
        self.seed_notes = {}
        nd = os.path.join(SEED_DIR, "notes")
        if os.path.isdir(nd):
            for f in sorted(os.listdir(nd)):
                if f.endswith(".md"):
                    title = f[:-3]
                    name = N.add(title)
                    assert name == safe_filename(title), f"seed note title clashes: {title}"
                    self.seed_notes[title] = name
        self.plate_rows = self._plate_list()
        self.plate_name = {p: N.add(f"Plate {num:02d}") for p, num in self.plate_rows}
        mods = [int(m) for m in R.modules["module"]]
        self.module_name = {m: N.add(f"Module {m:03d}") for m in mods}
        self.line_name = [N.add(f"{c} (line)") for c in R.cell]
        drugs = sorted(set(R.tdrugs["drug"].astype(str)) | set(R.dd_drug))
        self.drug_name = {d: N.add(f"{d} (drug)") for d in drugs}
        self.gene_name = [N.add(R.label[c], alt=f"{R.label[c]} (gene {c})") for c in range(R.gK)]
        self.plates_note = [N.add(f"{self.gene_name[c]} — plates") for c in range(R.gK)]
        self.gene_path = [f"Genes/{R.bucket[c]}/{self.gene_name[c]}.md" for c in range(R.gK)]
        # a written link [[SYMBOL]] goes to the first note of that symbol
        self.sym_note = {}
        for c in range(R.gK):
            self.sym_note.setdefault(R.sym[c], self.gene_name[c])

    def _plate_list(self):
        R = self.R
        plates = [str(p) for p in R.tplates["plate"]]
        for p in R.wells["plate"].astype(str).unique():
            if p not in plates:
                plates.append(p)
        out, used = [], set()
        for i, p in enumerate(plates):
            m = re.search(r"(\d+)", p)
            num = int(m.group(1)) if m else i + 1
            while num in used:
                num += 100
            used.add(num)
            out.append((p, num))
        return out

    def dlink(self, drug):
        n = self.drug_name.get(str(drug))
        return f"[[{n}]]" if n else cell(drug)

    def ddlink(self, dd):
        dd = int(dd)
        return f"{self.dlink(self.R.dd_drug[dd])} {fdose(self.R.dd_dose[dd])}"

    def glink(self, c):
        return f"[[{self.gene_name[int(c)]}]]"

    def llink(self, line):
        return f"[[{self.line_name[int(line)]}]]"

    def mlink(self, m):
        n = self.module_name.get(int(m))
        return f"[[{n}]]" if n else f"module {int(m)}"

    def mod_label_text(self, m):
        """The validation stage's enrichment label of a module ('' when it only names the module's top genes)."""
        lab = self.R.mod_label.get(int(m))
        if not lab or not lab[0] or lab[1] in ("top genes", "") or lab[0].startswith("genes: "):
            return ""
        return lab[0]

    def arms_text(self, m):
        """Whether a module's two sides move opposite, as the graph stage measured it (modules.parquet)."""
        R = self.R
        b = R.mod_between.get(int(m), np.nan)
        if R.mod_opp.get(int(m)):
            return (f"Its + and − arms move opposite to each other under the same drugs (mean cos between them "
                    f"{fcos(b)}).")
        if not _finite(b):
            return "A single-armed module: all its genes lie on one side of its main direction."
        return (f"A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos "
                f"between them {fcos(b)}; a − arm needs ≥ {ARM_MIN} genes on its side and a mean cos ≤ "
                f"{ARMS_OPPOSITE:+.1f}), so all its genes count as +.")

    # ------------------------------------------------------------------ written layer
    def resolve_written(self, text):
        """Wikilinks of a written file: keep seed notes and genes that have a note; anything else -> plain text."""
        seed = set(self.seed_notes)
        pat = re.compile(r"\[\[([^\]|#]+)((?:#[^\]|]*)?)(?:(\\?\|)([^\]]*))?\]\]")
        out = []
        for line in text.split("\n"):
            in_table = line.lstrip().startswith("|")

            def fix(m):
                tgt, anchor, alias = m.group(1).strip(), m.group(2) or "", m.group(4)
                if tgt in seed:
                    return m.group(0)
                n = self.sym_note.get(tgt)
                if n:
                    if n == tgt and not alias:
                        return f"[[{n}{anchor}]]"
                    bar = "\\|" if in_table else "|"
                    return f"[[{n}{anchor}{bar}{alias or tgt}]]"
                return alias or tgt
            out.append(pat.sub(fix, line))
        return "\n".join(out)

    # ------------------------------------------------------------------ literature reviews (OUT/review)
    def load_literature(self):
        """The reviews of OUT/review (tahoemap/review): per reviewed gene / drug / line its note body, the facts of
        its callout and its connection verdicts. With no review, nothing is loaded and no note changes."""
        R = self.R
        self.lit, self.lit_pairs, self.lit_verdicts = {}, {}, {}
        self.n_lit_notes = self.n_lit_cells = 0
        self.lit_fp = review_fingerprint(self.out)
        if self.lit_fp is None:
            return
        rd = os.path.join(self.out, "review")
        self._gene_by_name = {}
        for c in range(R.gK):                                  # symbol or label -> the first gene note's col
            for k in (R.label[c], R.sym[c]):
                if k:
                    self._gene_by_name.setdefault(k.upper(), c)
        self._drug_by_name = {d.lower(): d for d in self.drug_name}
        ids = self.R.tl["cell_line_id"].astype(str).tolist() if "cell_line_id" in self.R.tl else []
        self._line_by_id = {x: i for i, x in enumerate(ids)}
        self._line_by_name, self._lit_stems = {}, {}
        for i, nm in enumerate(R.cell):
            self._line_by_name.setdefault(str(nm).lower(), i)
        for kind in REVIEW_KINDS:
            nd, jd = os.path.join(rd, "notes", kind), os.path.join(rd, "reviews", kind)
            stems = set()
            for d, ext in ((nd, ".md"), (jd, ".json")):
                if os.path.isdir(d):
                    stems |= {f[:-len(ext)] for f in os.listdir(d) if f.endswith(ext)}
            for stem in sorted(stems):
                js = _read_json(os.path.join(jd, stem + ".json")) or {}
                meta = js.get("meta") or {}
                key = self.lit_key(kind, meta.get("entity_id"), meta.get("name") or stem)
                if key is None:
                    log(f"  vault: review {kind}/{stem} matches no {kind} note of this run; left out")
                    continue
                np_ = os.path.join(nd, stem + ".md")
                text = ""
                if os.path.exists(np_):
                    with open(np_, encoding="utf-8") as fh:
                        text = fh.read()
                text = text.strip() or str(js.get("note_markdown") or "").strip()
                if not text:
                    continue
                old = self.lit.get((kind, key))
                if old and str(old["meta"].get("reviewed", "")) > str(meta.get("reviewed", "")):
                    continue                                    # two files for one entity: the latest review
                self.lit[(kind, key)] = {
                    "kind": kind, "stem": stem, "text": text, "meta": meta,
                    "verification": js.get("verification") or {}, "summary": str(js.get("summary") or ""),
                    "review_rel": f"review/reviews/{kind}/{stem}.json" if js else None,
                    "note_rel": f"review/notes/{kind}/{stem}.md" if os.path.exists(np_) else None}
        for r in review_connections(self.out, gene_col=lambda s: self._gene_by_name.get(str(s).upper())):
            eid = sval(r.get("entity_id"))
            kind = eid.split(":", 1)[0] if ":" in eid else sval(r.get("kind"))
            key = self.lit_key(kind, eid, sval(r.get("name")))
            if key is None or not sval(r.get("verdict")):
                continue
            pk, pt = sval(r.get("partner_kind")) or "gene", sval(r.get("partner"))
            if pk == "gene":
                pc = r.get("partner_col")
                pkey = int(pc) if _finite(pc) and 0 <= int(pc) < R.gK else None
            else:
                pkey = self.lit_key(pk, pt, pt.split(":", 1)[1] if ":" in pt else pt)
            uv = r.get("unverified")
            v = {"partner": pt, "pkey": (pk, pkey) if pkey is not None else None, "verdict": sval(r.get("verdict")),
                 "citations": [x.strip() for x in sval(r.get("citations")).split(";") if x.strip()],
                 "check": sval(r.get("check")), "unverified": _finite(uv) and bool(float(uv))}
            self.lit_verdicts.setdefault((kind, key), []).append(v)
            if kind == "gene" and v["pkey"] and v["pkey"][0] == "gene":
                self.lit_pairs.setdefault((key, v["pkey"][1]), v)
        log(f"  vault: literature reviews of {len(self.lit):,} entities "
            f"({', '.join(f'{sum(1 for k in self.lit if k[0] == kd)} {kd}s' for kd in REVIEW_KINDS)}), "
            f"{sum(len(v) for v in self.lit_verdicts.values()):,} connection verdicts")

    def lit_key(self, kind, eid, name):
        """The note key of a reviewed entity: gene col, drug name or line index (None if this run has no note)."""
        eid, name = sval(eid).strip(), sval(name).strip()
        if eid.startswith(kind + ":"):
            rest = eid.split(":", 1)[1].strip()
            if kind == "gene" and rest.isdigit() and int(rest) < self.R.gK:
                return int(rest)
            if kind == "drug" and rest in self.drug_name:
                return rest
            if kind == "line" and rest in self._line_by_id:
                return self._line_by_id[rest]
            name = name or rest
        if not name or kind not in REVIEW_KINDS:
            return None
        if kind == "gene":
            key = self._gene_by_name.get(name.upper())
        elif kind == "drug":
            key = self._drug_by_name.get(name.lower())
        else:
            key = self._line_by_name.get(name.lower(), self._line_by_id.get(name))
        if key is None:                                          # a file stem: safe_filename of the name
            if kind not in self._lit_stems:
                self._lit_stems[kind] = {}
                items = (enumerate(self.R.label) if kind == "gene" else ((d, d) for d in self.drug_name)
                         if kind == "drug" else enumerate(self.R.cell))
                for k, nm in items:
                    self._lit_stems[kind].setdefault(safe_filename(nm), k)
            key = self._lit_stems[kind].get(name)
        return key

    def resolve_any(self, text):
        """Wikilinks of an agent's note: kept where this vault has the note (any note name, a gene symbol, a drug
        or cell-line name), else plain text, so no link is broken."""
        taken = self.names.taken
        pat = re.compile(r"\[\[([^\]|#]+)((?:#[^\]|]*)?)(?:(\\?\|)([^\]]*))?\]\]")
        out = []
        for line in text.split("\n"):
            in_table = line.lstrip().startswith("|")

            def fix(m):
                tgt, anchor, alias = m.group(1).strip(), m.group(2) or "", m.group(4)
                n = taken.get(tgt.lower())
                if n is None and tgt in self.sym_note:
                    n = self.sym_note[tgt]
                if n is None:
                    c = self._gene_by_name.get(tgt.upper())
                    d = self._drug_by_name.get(tgt.lower())
                    i = self._line_by_name.get(tgt.lower())
                    n = self.gene_name[c] if c is not None else self.drug_name[d] if d is not None else \
                        self.line_name[i] if i is not None else None
                if n is None:
                    return alias or tgt
                if n == tgt and not alias:
                    return f"[[{n}{anchor}]]"
                bar = "\\|" if in_table else "|"
                return f"[[{n}{anchor}{bar}{alias or tgt}]]"
            out.append(pat.sub(fix, line))
        return "\n".join(out)

    def _run_link(self, note_rel, target_rel):
        """A markdown link target from a vault note to a file of the run folder: relative, URL-encoded."""
        here = os.path.dirname(os.path.join(self.root, note_rel))
        rel = os.path.relpath(os.path.join(self.out, target_rel), here).replace(os.sep, "/")
        return urllib.parse.quote(rel, safe="/")

    def lit_frontmatter(self, kind, key, fm):
        """A reviewed entity's frontmatter: the literature_review date and tag (nothing for the others)."""
        rec = self.lit.get((kind, key))
        if rec is not None:
            fm["literature_review"] = sval(rec["meta"].get("reviewed"))[:10] or None
            fm["tags"] = list(fm.get("tags") or []) + ["literature-review"]
        return fm

    def _verdict_text(self, v, partner_review=None):
        cits = v["citations"]
        s = v["verdict"]
        if v["unverified"]:
            s += " (unverified)"
        if v["check"] and v["check"] != "supported":
            s += f" (check: {v['check']})"
        if partner_review:
            s += f" ({partner_review}'s review)"
        if cits:
            s += " · " + " ".join(citation_link(x) for x in cits[:LIT_CITES]) + \
                (f" +{len(cits) - LIT_CITES}" if len(cits) > LIT_CITES else "")
        return s

    def lit_partner_cell(self, c, b):
        """The Literature cell of partner b in gene c's tables: c's review's verdict on b, else b's on c; '' if none."""
        v = self.lit_pairs.get((int(c), int(b)))
        if v is not None:
            return self._verdict_text(v)
        v = self.lit_pairs.get((int(b), int(c)))
        if v is not None:
            return self._verdict_text(v, partner_review=self.R.label[int(b)])
        return ""

    def _plink(self, v):
        pk = v["pkey"]
        if pk is None:
            return cell(v["partner"])
        kind, key = pk
        return self.glink(key) if kind == "gene" else self.dlink(key) if kind == "drug" else self.llink(key)

    def sec_literature(self, kind, key, note_rel):
        """'## What the literature says' of a reviewed entity: the callout, the agent's note, its verdicts."""
        rec = self.lit.get((kind, key))
        if rec is None:
            return []
        self.n_lit_notes += 1
        meta, ver = rec["meta"], rec["verification"]
        cnt = ver.get("counts") or {}
        ids = ver.get("ids") or {}
        llm = ver.get("llm") or {}
        mode = ver.get("mode")
        agent = sval(meta.get("agent")) or f"{kind}-reviewer"
        model = sval(meta.get("model"))
        served = [m for m in (meta.get("served_models") or []) if m and m != model]
        when = sval(meta.get("reviewed"))[:10]
        n = lambda k: int(cnt.get(k) or 0)  # noqa: E731
        how = ", ".join(([f"model `{model}`"] if model else [])
                        + ([f"in part by the fallback `{'`, `'.join(served)}`"] if served else [])
                        + ([f"effort {sval(meta.get('effort'))}"] if sval(meta.get("effort")) else []))
        C = ["> [!info] AI-agent literature review",
             f"> Written by the `{agent}` agent" + (f" ({how})" if how else "") + (f" on {when}" if when else "")
             + ", from this run's data on it and the papers it retrieved. It is not checked by a person: read it as "
               "a lead, and check a claim in the cited paper before relying on it."]
        if not rec["review_rel"]:
            C.append(f"> No review record (`review/reviews/{kind}/{rec['stem']}.json`) was found for this note: its "
                     "model, date and verification are unknown.")
        elif mode in ("ids", "llm"):
            s = f"> Verification: {n('n_citations')} paper{'s' if n('n_citations') != 1 else ''} cited"
            if ids and not ids.get("error"):
                s += (f"; every cited id looked up in PubMed / Crossref: {int(ids.get('found') or 0)} found, "
                      f"{n('removed_citations')} removed as not found")
                if n("retracted_citations"):
                    s += f", {n('retracted_citations')} retracted"
            elif ids.get("error"):
                s += "; the id check failed (" + cell(sval(ids.get("error")))[:120] + ")"
            if n("unverified_items"):
                s += f"; {n('unverified_items')} item{'s' if n('unverified_items') != 1 else ''} left unverified"
            if mode == "llm" and llm.get("status") == "done":
                checker = sval(meta.get("checker_model"))
                s += (". Claims checked against the abstracts they cite (`citation-checker`"
                      + (f", `{checker}`" if checker else "") + f"): of {n('claims_checked')} claim"
                      + ("s" if n("claims_checked") != 1 else "") + f", {n('supported')} supported, {n('partly')} "
                      f"partly, {n('not supported')} not supported, {n('not checkable')} not checkable.")
            elif mode == "llm":
                why = cell(sval(llm.get("status")) or "not run")
                s += f". The claims were not checked against the abstracts ({why})."
            else:
                s += ". The claims were not checked against the abstracts (`--verify ids`)."
            C.append(s)
        else:
            C.append("> Verification: none (the review ran with `--verify off`): its citations were not checked.")
        links = []
        hist = sval(meta.get("history"))
        if hist and os.path.exists(os.path.join(self.out, hist)):
            links.append(f"the full history of the run (every request, response and tool call): "
                         f"[{os.path.basename(hist)}]({self._run_link(note_rel, hist)})")
        if rec["review_rel"]:
            links.append(f"the review as data: [{os.path.basename(rec['review_rel'])}]"
                         f"({self._run_link(note_rel, rec['review_rel'])})")
        if links:
            C.append("> Files: " + "; ".join(links) + ". They are in the run folder, outside the vault ("
                     + ", ".join(f"`{p}`" for p in (hist, rec["review_rel"]) if p) + "): open them in a text editor.")
        body = []
        fence = False
        for line in self.resolve_any(rec["text"]).split("\n"):
            if line.lstrip().startswith(("```", "~~~")):
                fence = not fence
            m = None if fence else re.match(r"^(#{1,6})\s+(.*?)\s*#*\s*$", line)
            if m:
                if not any(x.strip() for x in body) and m.group(2).strip().rstrip(":").lower() == LIT_HEADING.lower():
                    continue                                    # the vault supplies this heading
                if len(m.group(1)) < 3:                         # below the note's own '##' sections
                    line = "### " + m.group(2)
            body.append(line)
        while body and not body[0].strip():
            body.pop(0)
        L = [f"## {LIT_HEADING}", ""] + C + [""] + body + [""]
        vs = self.lit_verdicts.get((kind, key)) or []
        if vs:
            L += ["**Connection verdicts** of this review (`review/connections.parquet`): " +
                  "; ".join(f"{self._plink(v)} {self._verdict_text(v)}" for v in vs) + ".", ""]
        return L

    def load_fragments(self):
        self.fragments = {}
        gd = os.path.join(SEED_DIR, "genes")
        if os.path.isdir(gd):
            for f in sorted(os.listdir(gd)):
                if f.endswith(".md"):
                    with open(os.path.join(gd, f), encoding="utf-8") as fh:
                        self.fragments[f[:-3]] = fh.read().strip()

    def write_concepts(self):
        nd = os.path.join(SEED_DIR, "notes")
        for title, name in sorted(self.seed_notes.items()):
            with open(os.path.join(nd, title + ".md"), encoding="utf-8") as fh:
                text = fh.read()
            text = self.resolve_written(text)
            src = f"tahoemap/vault_seed/notes/{title}.md"
            fm = {}
            if text.startswith("---\n") and "\n---" in text[4:]:
                end = text.index("\n---", 4)
                fm = _parse_simple_yaml(text[4:end])
                text = text[end + 4:].lstrip("\n")
            fm["source"] = src
            text = frontmatter(fm) + "\n" + text
            text = text.rstrip() + (f"\n\n---\n*Written note, copied from `{src}` by `tahoemap vault`. Edit it "
                                    "there, not here: this copy is replaced on every build.*\n")
            self.W.write(f"Concepts/{name}.md", text)

    # ------------------------------------------------------------------ gene notes
    def gene_notes(self):
        R = self.R
        t0 = time.time()
        self.prep_plates()
        for c in range(R.gK):
            text = self.gene_note(c)
            self.W.write(self.gene_path[c], text)
            self.gene_sizes.append(len(text.encode("utf-8")))
            ptxt = self.plates_text(c)
            self.W.write(f"Genes/{R.bucket[c]}/{self.plates_note[c]}.md", ptxt)
            self.plates_sizes.append(len(ptxt.encode("utf-8")))
            if c and c % 2000 == 0:
                log(f"  vault: {c:,} / {R.gK:,} genes ({time.time() - t0:.0f} s)")
        log(f"  vault: {R.gK:,} gene notes and plates notes ({time.time() - t0:.0f} s)")

    def gene_note(self, c):
        R = self.R
        tg = R.tg.iloc[c]
        sym, name = R.sym[c], self.gene_name[c]
        an = R.ann.iloc[c] if R.ann is not None else None
        gname = sval(an["name"]) if an is not None else ""
        loc = sval(an["location"]) if an is not None else ""
        m, arm = int(R.module[c]), R.arm[c]
        inc = bool(R.included[c])
        frag = self.fragments.get(sym)
        tags = ["gene"]
        if m > 0:
            tags.append(f"module/{m:03d}")
        if frag:
            tags.append("written")
        if R.noise[c]:
            tags.append("noise-rna")
        if not inc:
            tags.append("not-in-vector-space")
        fm = {"symbol": sym, "type": "gene", "col": c, "ensembl_id": sval(tg.get("ensembl_id")),
              "name": gname, "location": loc,
              "module": (m if m > 0 else 0) if inc else None, "arm": arm if (inc and m > 0) else None,
              "pooled_cpm": round(float(tg["pooled_cpm"]), 2) if _finite(tg["pooled_cpm"]) else None,
              "n_lines_expressing": int(tg["n_lines_expressing"]) if _finite(tg["n_lines_expressing"]) else None,
              "n_dd_up_clean": int(tg["n_dd_up_clean"]) if _finite(tg["n_dd_up_clean"]) else 0,
              "n_dd_down_clean": int(tg["n_dd_down_clean"]) if _finite(tg["n_dd_down_clean"]) else 0,
              "in_vector_space": inc}
        if name != sym:
            fm["aliases"] = [sym]
        fm["tags"] = tags
        self.lit_frontmatter("gene", c, fm)
        L = [frontmatter(fm), f"# {R.label[c]}", ""]
        sub = []
        if gname and gname != sym:
            sub.append(f"*{gname}*")
        if loc:
            sub.append(loc)
        if R.label[c] != sym:
            sub.append(f"Tahoe lists the symbol {sym} more than once; this note is col {c}")
        if sub:
            L += [" — ".join(sub), ""]
        if frag:
            if OLD_STUDY_RE.search(frag):              # its score / rank / regulon belong to the earlier study
                L += [OLD_STUDY_NOTE, ""]
                self.n_old_study += 1
            L += [self.resolve_written(frag), ""]
            self.n_fragments += 1
        s = R.de_s
        rows = np.arange(s[c], s[c + 1])
        L += self.sec_glance(c, tg, rows)
        L += self.sec_drugs(c, tg, rows)
        L += self.sec_lines(c)
        L += self.sec_partners(c)
        L += self.sec_where(c)
        L += self.sec_literature("gene", c, self.gene_path[c])
        L += self.sec_record(c, an)
        L += self.sec_data(c, len(rows))
        L += ["## Sources", "",
              f"Generated by `tahoemap vault` (v{VERSION}) from the tables of the run; do not edit this note, it is "
              "rebuilt on every run. " +
              (f"The written part above is `tahoemap/vault_seed/genes/{sym}.md`." if frag else
               f"No written note yet: write `tahoemap/vault_seed/genes/{safe_filename(sym)}.md` and rerun "
               "`tahoe vault`."),
              "Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download "
              "dates in `reference/sources.json`). Paths are relative to the run folder."]
        if ("gene", c) in self.lit:
            L += ["", f"\"{LIT_HEADING}\" is an AI agent's review of this gene (tahoemap/review): "
                  + (f"`{self.lit[('gene', c)]['note_rel']}`, " if self.lit[("gene", c)]["note_rel"] else "")
                  + "spliced in by `tahoe vault`; a new review replaces it."]
        return "\n".join(L)

    def _de_row(self, rows, dd):
        de = self.R.de
        hit = rows[de["dd"][rows] == dd]
        return int(hit[0]) if len(hit) else None

    def sec_glance(self, c, tg, rows):
        R, de = self.R, self.R.de
        S = []
        for d, key, n_clean, n_all in (("up", "best_clean_up", "n_dd_up_clean", "n_dd_up"),
                                       ("down", "best_clean_down", "n_dd_down_clean", "n_dd_down")):
            verb = "Raised" if d == "up" else "Lowered"
            nc = int(tg[n_clean]) if _finite(tg[n_clean]) else 0
            na = int(tg[n_all]) if _finite(tg[n_all]) else 0
            bdd = int(tg[f"{key}_dd"]) if _finite(tg[f"{key}_dd"]) else -1
            if nc > 0 and bdd >= 0:
                r = self._de_row(rows, bdd)
                lines = ""
                if r is not None:
                    nl = de["n_lines_up" if d == "up" else "n_lines_down"][r]
                    lines = f", {d} in {int(nl)} of {int(de['n_lines_measured'][r])} measured lines"
                S.append(f"Pooled over the cell lines (median), {verb.lower()} significantly by {nc} clean "
                         f"drug-dose{'s' if nc != 1 else ''}{f' ({na} counting flagged ones)' if na != nc else ''}; "
                         f"the strongest is {self.ddlink(bdd)}: {ffold(tg[f'{key}_fold'])} (z {fz(tg[f'{key}_z'])}, "
                         f"q {fq(tg[f'{key}_q'])}{lines}).")
            else:
                extra = f" ({na} flagged ones do)" if na else ""
                S.append(f"No clean drug-dose {'raises' if d == 'up' else 'lowers'} it significantly in the pooled "
                         f"(median-over-lines) data{extra}.")
            if nc < SHORT_POOLED:
                one = self._single_lines(c, d)
                if one:
                    S.append(one)
        if R.included[c]:
            s0, s1 = R.rel_s[c], R.rel_s[c + 1]
            rr = np.arange(s0, s1)
            fdr = R.rel["fdr"][rr].astype(float)
            ok = rr[(R.rel["evidence"][rr] == "both halves") & (np.nan_to_num(fdr, nan=1.0) <= REPRO_FDR)]
            pos = [i for i in ok if R.rel["cos"][i] > 0][:N_GLANCE]
            neg = [i for i in ok if R.rel["cos"][i] < 0][:N_GLANCE]

            def plist(ii):
                return ", ".join(f"{self.glink(R.rel['col_b'][i])} ({fcos(R.rel['cos'][i])}, fdr "
                                 f"{fq(R.rel['fdr'][i])})" for i in ii)
            if pos or neg:
                parts = []
                if pos:
                    parts.append("moves with " + plist(pos))
                if neg:
                    parts.append("moves opposite to " + plist(neg))
                S.append(f"Its most reliable partners (same sign, fdr ≤ {REPRO_FDR:.2f}, in two random halves of "
                         "the compounds): it " + "; ".join(parts) + ".")
            else:
                S.append(f"No partner reaches fdr ≤ {REPRO_FDR:.2f} with the same sign in two random halves of the "
                         "compounds (see the tables below).")
            m = int(R.module[c])
            if m > 0:
                lab = self.mod_label_text(m)
                where = (f"It sits in the **{R.arm[c]}** arm of {self.mlink(m)}" if R.mod_opp.get(m) else
                         f"It is in {self.mlink(m)}, a single-armed module")
                S.append(where + (f" ({lab})" if lab else "") + ".")
            else:
                S.append("Its neighbourhood forms no module of 5 or more genes (module 0, unassigned).")
        else:
            S.append(f"It is not in the vector space: {self._why_out(c)}. So it has no partners and no module.")
        return ["## At a glance", "", "> [!summary] In this data"] + ["> " + x for x in S] + [""]

    def _single_lines(self, c, d):
        """'In single lines' sentence: the drug-doses that move the gene in the most lines at the calibrated per-line
        cut (tables/drug_line_top.parquet, clean drug-doses), '' when there are none."""
        R, t = self.R, self.R.dlt
        rr = np.arange(R.dlt_s[c], R.dlt_s[c + 1])
        rr = rr[t["direction"][rr] == d]
        if not len(rr):
            return ""
        by = {}
        for r in rr:                                       # rows are strongest |z| first
            by.setdefault(int(t["dd"][r]), []).append(r)
        top = sorted(by.items(), key=lambda kv: (-len(kv[1]), -abs(float(t["z"][kv[1][0]])), kv[0]))[:N_SINGLE]
        parts = []
        for dd, lst in top:
            cells = ", ".join(f"{R.cell[int(t['line'][r])]} {flfc_fold(t['lfc'][r])}" for r in lst[:4]) + \
                (", …" if len(lst) > 4 else "")
            parts.append(f"{self.ddlink(dd)} in {len(lst)} line{'s' if len(lst) != 1 else ''} ({cells})")
        verb = "raise" if d == "up" else "lower"
        cut = f"per-line |z| ≥ {R.line_z:.1f}" + ("" if R.line_z_calibrated else " (uncalibrated)")
        return (f"In single lines ({cut}, clean drug-doses; `tables/drug_line_top.parquet`), these {verb} it: "
                + "; ".join(parts) + ".")

    def _why_out(self, c):
        """Why a gene is not in the vector space: the embed stage's rule, with its counts (embed/info.json)."""
        R, ei = self.R, self.R.embed_info
        if R.noise[c]:
            return "it is a noise-class RNA (snoRNA, mitochondrial, histone, ribosomal pseudogene or ENSG-only name)"
        need = int(ei.get("min_responsive", 5))
        n = int(R.n_resp[c]) if _finite(R.n_resp[c]) else 0
        nd, nl = ei.get("drugdoses_active"), ei.get("lines", R.L)
        space = (f"the {fint(nd)} active, trustworthy drug-doses × {nl} lines the space is built from (drug-doses with "
                 f"≥ {ei.get('min_active', 10)} significant genes, pooled or in single lines, and no untrusted flag; "
                 f"{fint(ei.get('contexts'))} of these contexts have data)" if _finite(nd) else
                 "the (drug-dose, line) contexts of the active, trustworthy drug-doses the space is built from")
        txt = f"it reaches |z| ≥ 3 in {n} of {space}"
        if n < need:
            return txt + f"; the space needs {need}"
        lz = ei.get("line_z_responsive")
        txt += (f"; that count (≥ {need}) is not enough on its own: the space also needs a significant clean pooled "
                f"drug-dose (q < {Q_CUT:.2f}, ≥ 1.2×)" +
                (f" or a per-line |z| ≥ {float(lz):.1f} in ≥ 2 lines of one trustworthy drug-dose" if _finite(lz)
                 else "") + ", and it has neither")
        if _finite(ei.get("null_rate")):
            txt += f" (chance rate of |z| ≥ 3 per context: {g3(ei['null_rate'])})"
        if _finite(ei.get("n_genes_excluded_chance")):
            txt += (f"; {fint(ei['n_genes_excluded_chance'])} genes of this run reach the count without either "
                    "(at full scale almost every expressed gene does, by chance)")
        return txt

    def sec_drugs(self, c, tg, rows):
        de = self.R.de
        L = []
        clean = de["clean"][rows].astype(bool)
        z = de["z"][rows].astype(float)
        for d in ("up", "down"):
            title = "## Drugs that raise it" if d == "up" else "## Drugs that lower it"
            if d == "up":
                sel = rows[clean & (z > 0)][:N_DRUGS]
            else:
                sel = rows[clean & (z < 0)][::-1][:N_DRUGS]
            nc = tg["n_dd_up_clean" if d == "up" else "n_dd_down_clean"]
            L += [title, ""]
            one = self._single_lines(c, d) if (nc if _finite(nc) else 0) < SHORT_POOLED else ""
            if not len(sel):
                L += [f"No clean drug-dose {'raises' if d == 'up' else 'lowers'} it in the pooled data (pooled over "
                      f"the cell lines, median: none with |z| ≥ 3 or q < {Q_CUT:.2f}). A response seen in fewer than "
                      "about half of the measured lines does not reach the pooled data; see "
                      "[[#In which cell lines]].", ""]
                L += [one, ""] if one else []
                continue
            L += [f"*Pooled over the cell lines (median). {fint(nc, '0')} clean drug-doses "
                  f"{'raise' if d == 'up' else 'lower'} it significantly (**bold**: q < {Q_CUT:.2f}, ≥ 1.2×); clean "
                  f"rows with |z| ≥ 3 or q < {Q_CUT:.2f}, strongest first. `tables/drug_effects.parquet` col == "
                  f"{c}.*", ""]
            L += [one, ""] if one else []
            body = []
            for r in sel:
                q = de["q_up" if d == "up" else "q_down"][r]
                lfc = de["lfc"][r]
                sig = _finite(q) and q < Q_CUT and (lfc >= LFC_MIN if d == "up" else lfc <= -LFC_MIN)
                fo = ffold(de["fold"][r])
                nl = de["n_lines_up" if d == "up" else "n_lines_down"][r]
                names = [x for x in de["lines_up" if d == "up" else "lines_down"][r].split(", ") if x]
                ln = f"{int(nl)}/{int(de['n_lines_measured'][r])}"
                if names:
                    ln += " (" + ", ".join(names[:2]) + (", …" if len(names) > 2 else "") + ")"
                body.append([self.ddlink(de["dd"][r]), f"**{fo}**" if sig else fo, fz(de["z"][r]), fq(q), ln,
                             de["pattern_up" if d == "up" else "pattern_down"][r] or "—",
                             de["flags"][r] or ""])
            L += table(["Drug-dose", "Fold", "z", "q", "Lines " + d + " / measured", "Dose pattern", "Caveats"],
                       body) + [""]
        flagged = rows[~clean]
        L += ["## Flagged drug-doses", ""]
        if not len(flagged):
            L += ["None of the drug-doses that move it carries an artifact flag.", ""]
        else:
            flagged = flagged[np.argsort(-np.abs(de["z"][flagged].astype(float)), kind="stable")][:N_FLAGGED]
            L += ["*They move it but carry an artifact flag: the change may come from cell death, a transcription "
                  "drop, a cell-cycle shift or a well-position problem, not from regulation of this gene.*", ""]
            body = []
            for r in flagged:
                up = de["z"][r] > 0
                q = de["q_up" if up else "q_down"][r]
                body.append([self.ddlink(de["dd"][r]), ffold(de["fold"][r]), fz(de["z"][r]), fq(q),
                             "up" if up else "down", de["flags"][r]])
            L += table(["Drug-dose", "Fold", "z", "q", "Direction", "Flags"], body) + [""]
        return L

    def line_cut_text(self):
        """The per-line cut as the tables stage set it, with the number of chance calls it lets through."""
        R = self.R
        if not R.line_z_calibrated:
            return (f"per-line |z| ≥ {R.line_z:.1f} (this run's tables carry no calibrated cut: a per-line z of 4-5 "
                    "can arise by chance)")
        ch = (f"; about {g3(R.line_z_chance)} such calls per gene and line are expected by chance over the "
              f"{fint(R.line_z_ndd)} clean drug-doses" if R.line_z_chance is not None else "")
        return f"per-line |z| ≥ {R.line_z:.1f} (calibrated on this run, `tables/info.json`{ch})"

    def sec_lines(self, c):
        R, le = self.R, self.R.le
        rows = np.arange(R.le_s[c], R.le_s[c + 1])
        L = ["## In which cell lines", "",
             f"*`tables/line_effects.parquet` col == {c}. CPM = the line's own level (n.m. = not measured: the line "
             f"does not express it, or below {R.amb_frac:g} × its pooled level, where its reads are mostly ambient "
             f"RNA; no per-line values). Up / down = clean drug-doses moving it ≥ {R.line_fold:.3g}× at "
             f"{self.line_cut_text()}; the strongest of them is shown. Most responsive lines first.*", ""]
        if not len(rows):
            return L + ["No per-line values.", ""]
        nu = le["n_dd_up"][rows].astype(float)
        nd = le["n_dd_down"][rows].astype(float)
        order = sorted(range(len(rows)), key=lambda i: (-(np.nan_to_num(nu[i]) + np.nan_to_num(nd[i])),
                                                         R.cell[int(le["line"][rows[i]])].lower()))
        tp = {"altered": "alt", "wild type": "wt"}
        body = []
        for i in order:
            r = rows[i]
            line = int(le["line"][r])
            ex = bool(le["expressed"][r])

            def best(d):
                dd, z, lfc = le[f"best_{d}_dd"][r], le[f"best_{d}_z"][r], le[f"best_{d}_lfc"][r]
                if not (_finite(dd) and int(dd) >= 0 and _finite(z) and abs(float(z)) >= R.line_z):
                    return "—"
                return f"{self.ddlink(dd)} {flfc_fold(lfc)} (z {fz(z)})"
            body.append([self.llink(line), tp.get(R.tp53[line], "?"),
                         g3(le["baseline_cpm"][r]) + ("" if ex else " n.m."),
                         fint(nu[i], "—") if ex else "—", fint(nd[i], "—") if ex else "—",
                         best("up") if ex else "—", best("down") if ex else "—"])
        return L + table(["Line", "TP53", "CPM", "Up", "Down", "Strongest up", "Strongest down"], body) + [""]

    def _locus_note(self, c, b, r):
        R, rel = self.R, self.R.rel
        notes = []
        dist = rel["distance_bp"][r]
        if bool(rel["locus"][r]):
            kb = f"{float(dist) / 1000:.1f} kb" if _finite(dist) else "near"
            if bool(rel["readthrough_risk"][r]) and R.strand[c] in ("+", "-"):
                plus = R.strand[c] == "+"
                c_is_5p = (R.start[c] < R.start[b]) if plus else (R.end[c] > R.end[b])
                if c_is_5p:
                    where = f"{R.sym[b]} lies {kb} 3′ of this gene"
                else:
                    where = f"this gene lies {kb} 3′ of {R.sym[b]}"
                notes.append(f"**readthrough risk**: {where} on the same strand (can correlate by spillover, "
                             "not regulation)")
            else:
                notes.append(f"same locus ({kb}{', same strand' if bool(rel['same_strand'][r]) else ''})")
        return notes

    def sec_partners(self, c):
        R, rel = self.R, self.R.rel
        if not R.included[c]:
            return ["## Genes that move with it", "", "Not in the vector space, so no gene relations.", "",
                    "## Genes that move opposite", "", "Not in the vector space, so no gene relations.", ""]
        rows = np.arange(R.rel_s[c], R.rel_s[c + 1])
        L = []
        shown = [r for sign in (1, -1) for r in [r for r in rows if np.sign(rel["cos"][r]) == sign][:N_PARTNERS]]
        lit = {int(rel["col_b"][r]): self.lit_partner_cell(c, rel["col_b"][r]) for r in shown} \
            if self.lit_pairs else {}
        if not any(lit.values()):                      # the Literature column only where a shown partner has one
            lit = {}
        self.n_lit_cells += sum(1 for v in lit.values() if v)
        for sign in (1, -1):
            sel = [r for r in rows if np.sign(rel["cos"][r]) == sign][:N_PARTNERS]
            if sign > 0:
                L += ["## Genes that move with it", "",
                      f"*Strongest of its {len(rows)} nearest partners by |cos| (`relations/gene_relations.parquet` "
                      f"col_a == {c}); halves = cos in the spaces fitted on two random halves of the compounds (a "
                      "hash split of the compound names). Evidence: `both halves` = the same sign in both, |cos| ≥ "
                      f"{REL.REPRO_MIN:g} in each and fdr ≤ {REPRO_FDR:.2f}; `one half` = strong in one of the two "
                      "random halves only — not replicated, no error estimate; `not reproduced` = neither. A "
                      "correlation across "
                      "drugs and lines, not evidence that one gene regulates the other.*", ""]
                if not R.novel_assessed:
                    L += [f"*Novelty not assessed: {', '.join(R.novel_blocked) or 'reference sources'} missing "
                          "(`relations/info.json`), so no pair is called a novel candidate; the known-link notes "
                          "below cover only the sources that loaded.*", ""]
            else:
                L += ["## Genes that move opposite", ""]
            if not sel:
                L += ["None among its nearest partners." if sign > 0 else
                      "None among its nearest partners: everything close to it moves the same way.", ""]
                continue
            body = []
            for r in sel:
                b = int(rel["col_b"][r])
                notes = []
                if R.novel_assessed and bool(rel["novel_candidate"][r]):
                    notes.append("**novel candidate**")
                if bool(rel["shared_gene_group"][r]):
                    notes.append("same gene group")
                if rel["shared_pathway"][r]:
                    notes.append("pathway: " + rel["shared_pathway"][r])
                if _finite(rel["string_score"][r]):
                    notes.append(f"STRING {int(rel['string_score'][r])}")
                notes += self._locus_note(c, b, r)
                body.append([self.glink(b), fcos(rel["cos"][r]),
                             f"{fcos(rel['cos_half1'][r])} / {fcos(rel['cos_half2'][r])}", rel["evidence"][r],
                             fq(rel["fdr"][r]), "; ".join(notes)] + ([lit.get(b) or "—"] if lit else []))
            L += table(["Gene", "cos", "Halves", "Evidence", "fdr", "Notes"] + (["Literature"] if lit else []),
                       body) + [""]
        if lit:
            L += [f"*Literature = the connection verdict of the AI-agent literature review of this gene (see "
                  f"\"{LIT_HEADING}\"), else of the partner's review (named), with the papers it cites "
                  "(`review/connections.parquet`): "
                  "established, indirect, plausible, unexpected or contradicted; \"check\" = what the citation checker "
                  "found in the abstracts when it did not find the claim supported.*", ""]
        return L

    def sec_where(self, c):
        R = self.R
        L = ["## Where it sits", ""]
        if not R.included[c]:
            return L + [f"Not in the vector space: {self._why_out(c)}. Its drug and cell-line tables above are "
                        "complete all the same.", ""]
        m = int(R.module[c])
        if m > 0:
            n = R.mod_size.get(m, 0)
            lab = self.mod_label_text(m)
            arm = (f"this gene is in the **{R.arm[c]}** arm" if R.mod_opp.get(m) else "every member is in the + arm")
            L.append(f"- **Module**: {self.mlink(m)}" + (f" — {lab}" if lab else "") +
                     f"; {n} genes; {arm} (projection on the module's main direction {g3(R.axis_proj[c])}). "
                     + self.arms_text(m))
        else:
            L.append("- **Module**: none (module 0: its neighbourhood formed no community of ≥ 5 genes).")
        L.append(f"- **Nodal map** (x, y) = ({R.xy[c, 0]:.1f}, {R.xy[c, 1]:.1f}); signed map ({R.xys[c, 0]:.1f}, "
                 f"{R.xys[c, 1]:.1f}). **Vector** length {g3(R.vnorm[c])}, {g3(100 * R.vrep[c])}% of its response "
                 f"variance represented; |z| ≥ 3 in {fint(R.n_resp[c])} contexts (`embed/genes.parquet`).")
        nm = R.novel_by_col.get(c)
        if nm:
            L.append("- **Candidate new member** (not annotated, but close to the annotated members of its arm; "
                     "`validation/novel_members.csv`): " + "; ".join(
                         f"*{cell(r.set_label)}* ({r.source}, mean cos {fcos(r.mean_cos)} to "
                         f"{int(r.n_annotated_in_arm)})" for r in nm[:3]) + ".")
        L.append("")
        if hasattr(R, "pred_up") and R.pred_up[c, 0] >= 0:
            L += ["**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall "
                  "(gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`). "
                  "† = artifact flag.", ""]
            body = []
            for d, idx, pz in (("rise", R.pred_up[c], R.pred_up_z[c]), ("fall", R.pred_dn[c], R.pred_dn_z[c])):
                for j, dd in enumerate(idx):
                    if dd < 0:
                        continue
                    obs = float(R.DD_z[dd, c])
                    body.append([d if j == 0 else "", self.ddlink(dd) + (" †" if R.dd_artifact[dd] else ""),
                                 fz(pz[j]), fz(obs)])
            L += table(["", "Drug-dose", "Predicted z", "Observed z"], body) + [""]
        return L

    def sec_record(self, c, an):
        R = self.R
        L = ["## What is on record", ""]
        if an is None:
            return L + ["The reference stage did not run, so there is no registry annotation in this run.", ""]
        if sval(an.get("matched_by")) in ("", "none") and R.hgnc_status not in ("cached", "downloaded"):
            return L + [f"The HGNC registry was not available to this run (reference stage: {R.hgnc_status}), so "
                        "nothing is on record here; run `tahoe run --from reference` with network access to fill this "
                        "in.", ""]
        if sval(an.get("matched_by")) in ("", "none"):
            return L + [f"> [!warning] No registry record\n> {cell(R.sym[c])} has no HGNC entry matched to it: no "
                        "approved name, no gene group, no cross-references. The quantification assigned reads to "
                        "this identifier and that is what is known; nothing more is claimed.", ""]
        rows = [["Name", sval(an["name"]) or "—"]]
        lt = sval(an["locus_type"])
        lg = sval(an["locus_group"])
        rows.append(["Locus type", (lt + (f" ({lg})" if lg and lg != lt else "")) or "—"])
        pos = sval(an["location"])
        ch = sval(an["chrom"])
        if ch and _finite(an["start"]):
            pos += f" — chr{ch}:{int(an['start']):,}-{int(an['end']):,} ({sval(an['strand']) or '?'})"
        rows.append(["Location", pos or "—"])
        bt = sval(an.get("biotype"))
        if bt:
            rows.append(["Ensembl biotype", bt])
        al = [x for x in sval(an["aliases"]).split("|") if x]
        pv = [x for x in sval(an["prev_symbols"]).split("|") if x]
        if al or pv:
            rows.append(["Also known as", ", ".join(al[:8]) + (f"; previously {', '.join(pv[:5])}" if pv else "")])
        gg = [x for x in sval(an["gene_groups"]).split("|") if x]
        if gg:
            rows.append(["Gene groups (HGNC)", "; ".join(gg[:6])])
        hm = R.hallmark[c]
        if hm:
            rows.append(["Hallmark sets", ", ".join(h.replace("HALLMARK_", "") for h in hm)])
        rc = R.reactome[c]
        if rc:
            rows.append(["Reactome", f"{len(rc)} pathways, smallest: " + "; ".join(rc[:3])])
        mb = sval(an["matched_by"])
        if mb:
            rows.append(["Matched by", mb + (" (alias only: tentative)" if mb == "alias_symbol" else "")])
        L += table(["", ""], rows) + [""]
        up = sval(an["uniprot"]).split("|")[0]
        fn = sval(an["function"])
        pn = sval(an.get("protein_name"))
        if fn:
            L += [f"**Function**, from UniProt [{up}](https://www.uniprot.org/uniprotkb/{up})"
                  + (f" ({pn})" if pn else "") + ":", "", "> " + clip_text(fn), ""]
        elif up:
            L += [f"UniProt [{up}](https://www.uniprot.org/uniprotkb/{up}) carries no function annotation.", ""]
        ez = an["entrez_id"]
        ns = sval(an["ncbi_summary"])
        if ns:
            src = f"[{int(ez)}](https://www.ncbi.nlm.nih.gov/gene/{int(ez)})" if _finite(ez) else ""
            L += [f"**Summary**, from NCBI Gene {src}:", "",
                  "> " + clip_text(ns), ""]
        else:
            L += ["NCBI Gene carries no summary paragraph for it.", ""]
        acc = []
        hid = sval(an["hgnc_id"])
        if hid:
            acc.append(f"[{hid}](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/{hid})")
        if _finite(ez):
            acc.append(f"Entrez [{int(ez)}](https://www.ncbi.nlm.nih.gov/gene/{int(ez)})")
        if up:
            acc.append(f"UniProt [{up}](https://www.uniprot.org/uniprotkb/{up})")
        ens = sval(an["ensembl_id"])
        if ens:
            acc.append(f"Ensembl [{ens}](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g={ens})")
        if acc:
            L += ["**Accessions** — " + " · ".join(acc), ""]
        return L

    def sec_data(self, c, n_de):
        R = self.R
        nrel = R.rel_s[c + 1] - R.rel_s[c]
        return ["## Data", "",
                f"Gene col {c}: `tables/genes.parquet`, `tables/line_effects.parquet` ({R.L} rows) and "
                f"`tables/drug_line_top.parquet` (col == {c}); `tables/drug_effects.parquet` ({n_de} rows, flagged "
                f"included); `relations/gene_relations.parquet` (col_a == {c}, {nrel} rows); "
                f"`atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, {c}]; `tensor/DDL_lfc|DDL_z.npy` [{c}]; "
                f"`embed/gene_vectors.npy` [{c}]; `graph/nodes.parquet`. Every well: [[{self.plates_note[c]}]].",
                ""]

    # ------------------------------------------------------------------ plates notes (per gene)
    def prep_plates(self):
        R = self.R
        w = R.wells
        slot = np.array([T.slot_from_well(x) for x in w["well"]], dtype=float)
        self.grid = []                                  # per plate: 96 well rows (-1 = none) and is_dmso
        pl = w["plate"].astype(str).to_numpy()
        dm = w["is_dmso"].to_numpy(dtype=bool)
        tp = R.tplates.set_index(R.tplates["plate"].astype(str))
        for p, num in self.plate_rows:
            idx = np.full(96, -1, dtype=np.int64)
            ii = np.flatnonzero((pl == p) & np.isfinite(slot))
            idx[(slot[ii] - 1).astype(int)] = ii
            info = tp.loc[p] if p in tp.index else None
            self.grid.append((p, num, idx, idx >= 0, np.where(idx >= 0, dm[np.maximum(idx, 0)], False), info))
        tn = os.path.join(self.out, "tensor")
        wc = np.load(os.path.join(tn, "well_counts.npy"), mmap_mode="r")
        wu = np.load(os.path.join(tn, "well_umi.npy")).astype(np.float64)
        scale = np.where(wu > 0, 1e6 / np.maximum(wu, 1e-9), np.nan)
        # gene-major copies: one gene's wells are one contiguous read
        self.cpmT = np.empty((R.gK, R.N), dtype=np.float32)
        W2 = np.load(os.path.join(self.out, "atlas", "effects", "W2.npy"), mmap_mode="r")
        self.w2T = np.empty((R.gK, R.N), dtype=np.float32)
        for g0 in range(0, R.gK, 2048):
            g1 = min(R.gK, g0 + 2048)
            self.cpmT[g0:g1] = (np.asarray(wc[:, g0:g1], dtype=np.float64) * scale[:, None]).T
            self.w2T[g0:g1] = np.asarray(W2[:, g0:g1], dtype=np.float32).T
        self._fmt_cache = {}
        self._w2_tab = [f"{i / 100:+.2f}" for i in range(-999, 1000)]

    def _fmt_cpm(self, v):
        out = []
        cache = self._fmt_cache
        for x in v.tolist():
            if x != x:
                out.append("·")
                continue
            k = float(f"{x:.3g}") if x else 0.0
            s = cache.get(k)
            if s is None:
                s = g3(k)
                cache[k] = s
            out.append(s)
        return out

    def _fmt_w2(self, v):
        tab = self._w2_tab
        out = []
        for x in v.tolist():
            if x != x:
                out.append("·")
            else:
                i = int(round(x * 100))
                out.append(tab[i + 999] if -999 <= i <= 999 else f"{x:+.1f}")
        return out

    def _grid(self, vals, have, dmso):
        head = "| |" + "|".join(str(j) for j in range(1, 13)) + "|"
        out = [head, "|-" * 13 + "|"]
        for r in range(8):
            cells = []
            for j in range(12):
                k = r * 12 + j
                if not have[k]:
                    cells.append("·")
                else:
                    s = vals[k]
                    cells.append(f"**{s}**" if dmso[k] and s != "·" else s)
            out.append(f"|{ROWS[r]}|" + "|".join(cells) + "|")
        return out

    def plates_text(self, c):
        R = self.R
        name = self.gene_name[c]
        cpm_all = self._fmt_cpm(self.cpmT[c])
        w2_all = self._fmt_w2(self.w2T[c])
        L = [frontmatter({"symbol": R.sym[c], "type": "gene plates", "col": c}),
             f"# {name} — plates", "",
             f"Back to [[{name}]]. Per plate, two 8 × 12 grids laid out as the plate (rows A–H, columns 1–12). "
             f"**Raw CPM** = this gene's counts per million in the well, pooled over every cell line in it "
             f"(`tensor/well_counts.npy` column {c} ÷ `tensor/well_umi.npy` × 10⁶; uncorrected). **W2** = the "
             f"corrected well effect (`atlas/effects/W2.npy` column {c}; log2; median over the lines of each line's "
             "change against its own baseline on the plate, composition- and position-corrected; 0 = a typical drug "
             "well). **Bold** = DMSO well; · = no analysed well. Which drug and dose is in each well: the Plate "
             "notes.", ""]
        cpm = self.cpmT[c]
        for p, num, idx, have, dmso, info in self.grid:
            ii = np.where(have, idx, 0)
            v_cpm = [cpm_all[i] for i in ii]
            v_w2 = [w2_all[i] for i in ii]
            dose = sval(info["doses"]) if info is not None else ""
            sel = idx[have & ~dmso]
            seld = idx[have & dmso]
            with warnings.catch_warnings():
                warnings.simplefilter("ignore", category=RuntimeWarning)
                md = np.nanmedian(cpm[sel]) if len(sel) else np.nan
                mdm = np.nanmedian(cpm[seld]) if len(seld) else np.nan
            extra = []
            if info is not None and bool(info.get("unreliable", False)):
                extra.append("unreliable plate")
            L += [f"## Plate {num:02d}" + (f" — {fdose(dose)}" if dose else ""), "",
                  f"[[{self.plate_name[p]}]] · median raw CPM: drug wells {g3(md)}, DMSO wells {g3(mdm)}" +
                  ("".join(f" · **{e}**" for e in extra)), "", "Raw CPM", ""]
            L += self._grid(v_cpm, have, dmso) + ["", "W2 (log2)", ""]
            L += self._grid(v_w2, have, dmso) + [""]
        return "\n".join(L)

    # ------------------------------------------------------------------ drug notes
    def drug_notes(self):
        R = self.R
        de = R.de
        # group drug-effect rows by drug-dose once
        o = np.argsort(de["dd"], kind="stable")
        dd_sorted = de["dd"][o]
        dds = _slices(dd_sorted, R.Dn)
        self._dd_rows = (o, dds)
        # drug vectors: cosine among active drugs
        ed = os.path.join(self.out, "embed")
        self.drug_near = {}
        try:
            dv = np.load(os.path.join(ed, "drug_vectors.npy")).astype(np.float64)
            dt = pd.read_parquet(os.path.join(ed, "drugs.parquet"))
            act = dt["n_sig_genes"].to_numpy() >= 10
            nrm = np.linalg.norm(dv, axis=1)
            ok = act & (nrm > 0)
            U = np.where(ok[:, None], dv / np.maximum(nrm[:, None], 1e-12), 0.0)
            C = U @ U.T
            names = dt["drug"].astype(str).to_numpy()
            for i in np.flatnonzero(ok):
                cc = C[i].copy()
                cc[i] = -np.inf
                cc[~ok] = -np.inf
                top = np.argsort(-cc)[:8]
                self.drug_near[names[i]] = [(names[j], cc[j]) for j in top if np.isfinite(cc[j])]
        except (OSError, KeyError) as e:
            log(f"  vault: no drug-vector neighbours ({e})")
        Az = self._load_opt(os.path.join(self.out, "atlas", "effects", "DD_Az.npy"))
        beta = self._load_opt(os.path.join(self.out, "atlas", "effects", "DD_beta.npy"))
        by_drug = {}
        for i, d in enumerate(R.dd_drug):
            by_drug.setdefault(d, []).append(i)
        tdr = R.tdrugs.set_index(R.tdrugs["drug"].astype(str))
        for d in sorted(self.drug_name):
            rows = sorted(by_drug.get(d, []), key=lambda i: float(R.tdd["conc"].iloc[i])
                          if _finite(R.tdd["conc"].iloc[i]) else 0.0)
            info = tdr.loc[d] if d in tdr.index else None
            self.W.write(f"Drugs/{self.drug_name[d]}.md", self.drug_note(d, rows, info, Az, beta))

    @staticmethod
    def _load_opt(p):
        return np.load(p) if os.path.exists(p) else None

    def drug_note(self, d, rows, info, Az, beta):
        R, de = self.R, self.R.de
        o, dds = self._dd_rows
        g = (lambda k: sval(info.get(k)) if info is not None else "")
        doses = [R.dd_dose[i] for i in rows]
        fm = {"drug": d, "type": "drug", "salt_base": g("salt_base") or T.salt_base(d), "targets": g("targets"),
              "moa_fine": g("moa_fine"), "moa_broad": g("moa_broad"), "approved": g("approved"),
              "doses": doses, "best_dose": g("best_dose"),
              "max_sig_genes": int(info["max_sig"]) if info is not None and _finite(info.get("max_sig")) else None,
              "tags": ["drug"] + ([f"moa/{safe_filename(g('moa_broad')).replace(' ', '-').lower()}"]
                                  if g("moa_broad") else [])}
        self.lit_frontmatter("drug", d, fm)
        L = [frontmatter(fm), f"# {d}", ""]
        sub = [x for x in (" ".join(y for y in (g("moa_fine"), g("moa_broad") and f"({g('moa_broad')})") if y),)
               if x]
        if g("targets"):
            sub.append("targets: " + g("targets"))
        if g("approved"):
            sub.append("approved: " + g("approved"))
        if sub:
            L += ["*" + cell(" · ".join(sub)) + "*", ""]
        S = []
        if info is not None:
            lad = g("lowest_active_dose")
            lad = fdose(lad) if lad[:1].isdigit() else (lad or "none")
            S.append(f"Significant genes by dose ({' / '.join(fdose(x) for x in doses)}): "
                     f"{cell(g('n_sig_by_dose')) or '—'}; best dose {fdose(g('best_dose')) or '—'}; lowest active "
                     f"dose (it and every higher dose with ≥ 10 significant genes): {lad}.")
            if g("signature_r_between_doses"):
                S.append(f"Signature similarity between consecutive doses (low–mid / mid–high): "
                         f"{g('signature_r_between_doses')}.")
            if g("flags_by_dose") and set(g("flags_by_dose").replace("/", "").split()) != {"-"}:
                S.append(f"Flags by dose: {cell(g('flags_by_dose'))}.")
        if S:
            L += ["> [!summary] At a glance"] + ["> " + x for x in S] + [""]
        # doses table
        body = []
        for i in rows:
            t = R.tdd.iloc[i]
            wells = []
            pls = [x.strip() for x in re.split(r"[,;]", sval(t["plates"])) if x.strip()]
            wl = [x.strip() for x in re.split(r"[,;]", sval(t["wells"])) if x.strip()]
            for k, w in enumerate(wl):
                p = pls[k].strip() if k < len(pls) else (pls[0].strip() if pls else "")
                pn = self.plate_name.get(p)
                wells.append(f"[[{pn}]]:{w.strip()}" if pn else f"{p}:{w.strip()}")
            mods = "/".join(fz(t.get(f"{m}_z")) for m in ("S_PHASE", "G2M_PHASE", "PROTEASOME"))
            body.append([fdose(R.dd_dose[i]), ", ".join(wells) or "—",
                         f"{fint(t['n_genes_up'], '0')} / {fint(t['n_genes_down'], '0')}", g3(t.get("replicate_r")),
                         flog(t.get("cells_log2_vs_plate")), mods, R.dd_flags[i] or "—"])
        L += ["## Doses", "",
              "*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = "
              "log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle "
              "mix and proteasome load).*", ""]
        L += table(["Dose", "Wells", "Sig. genes up / down", "Replicate r", "Cells (log2)", "S / G2M / prot. z",
                    "Flags"], body) + [""]
        # genes per dose
        for dname, sgn in (("raises", 1), ("lowers", -1)):
            L += [f"## Genes it {dname}", "",
                  "*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the "
                  "row of the dose). † = not clean: an artifact flag on the drug-dose or on the gene.*", ""]
            anyrow = False
            for i in rows:
                rr = o[dds[i]:dds[i + 1]]
                if not len(rr):
                    continue
                z = de["z"][rr].astype(float)
                lfc = de["lfc"][rr].astype(float)
                q = de["q_up" if sgn > 0 else "q_down"][rr].astype(float)
                sig = (q < Q_CUT) & ((lfc >= LFC_MIN) if sgn > 0 else (lfc <= -LFC_MIN))
                rr, z = rr[sig], z[sig]
                if not len(rr):
                    continue
                rr = rr[np.argsort(-sgn * z, kind="stable")][:12]
                anyrow = True
                items = []
                for r in rr:
                    nl = de["n_lines_up" if sgn > 0 else "n_lines_down"][r]
                    items.append(f"{self.glink(de['col'][r])}{'' if de['clean'][r] else ' †'} "
                                 f"{ffold(de['fold'][r])} (z {fz(de['z'][r])}, {int(nl)}/"
                                 f"{int(de['n_lines_measured'][r])} lines)")
                n_all = int(R.tdd["n_genes_up" if sgn > 0 else "n_genes_down"].iloc[i])
                L += [f"**{fdose(R.dd_dose[i])}** ({n_all} gene{'s' if n_all != 1 else ''}): " + ", ".join(items),
                      ""]
            if not anyrow:
                L += [f"No gene is significantly {'raised' if sgn > 0 else 'lowered'} at any dose.", ""]
        # modules
        if R.mod_z is not None and len(self.module_name):
            body = []
            mods = R.modules["module"].astype(int).to_numpy()
            for i in rows:
                z = R.mod_z[:, i]
                if not np.isfinite(z).any():
                    continue
                oo = np.argsort(-np.nan_to_num(z, nan=0.0))
                up = [f"{self.mlink(mods[j])} ({fz(z[j])})" for j in oo[:3] if z[j] >= 2]
                dn = [f"{self.mlink(mods[j])} ({fz(z[j])})" for j in oo[::-1][:3] if z[j] <= -2]
                body.append([fdose(R.dd_dose[i]), ", ".join(up) or "—", ", ".join(dn) or "—"])
            L += ["## Modules it moves", "",
                  "*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module "
                  "(`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm "
                  "down (its genes up, in a single-armed module).*", ""]
            L += table(["Dose", "Raises", "Lowers"], body) + [""]
        # lines
        if Az is not None or beta is not None:
            body = []
            for i in rows:
                dep = resp = "—"
                if Az is not None:
                    a = Az[i]
                    oo = [j for j in np.argsort(np.nan_to_num(a, nan=0.0)) if _finite(a[j]) and a[j] <= -3][:5]
                    dep = ", ".join(f"{self.llink(j)} ({fz(a[j])})" for j in oo) or "—"
                if beta is not None and R.dd_nsig[i] >= 20:
                    b = beta[i]
                    fin = [j for j in np.argsort(-np.nan_to_num(b, nan=-np.inf), kind="stable") if _finite(b[j])]
                    k = min(4, len(fin) // 2)                  # strongest and weakest never share a line
                    oo, lo = (fin[:k], fin[::-1][:min(3, k)]) if k else (fin, [])
                    resp = ", ".join(f"{self.llink(j)} ({g3(b[j])})" for j in oo) or "—"
                    if lo:
                        resp += " · weakest: " + ", ".join(f"{self.llink(j)} ({g3(b[j])})" for j in lo)
                body.append([fdose(R.dd_dose[i]), dep, resp])
            L += ["## In which cell lines", "",
                  "*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or "
                  "stops that line more than the others). Response strength β = slope of the line's changes on the "
                  "drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no "
                  "response; drug-doses with ≥ 20 significant genes).*", ""]
            L += table(["Dose", "Most depleted lines (Az)", "Strongest responders (β)"], body) + [""]
        near = self.drug_near.get(d)
        if near:
            L += ["## Nearest drugs in the vector space", "",
                  "*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; "
                  "`embed/drug_vectors.npy`): drugs that move the same genes the same way.*", ""]
            moa = R.tdrugs.set_index(R.tdrugs["drug"].astype(str))["moa_fine"] if "moa_fine" in R.tdrugs else None
            L += ["- " + "; ".join(f"{self.dlink(n)} ({fcos(v)}"
                                   + (f", {cell(sval(moa.get(n)))}" if moa is not None and sval(moa.get(n)) else "")
                                   + ")" for n, v in near), ""]
        L += self.sec_literature("drug", d, f"Drugs/{self.drug_name[d]}.md")
        L += ["## Data", "",
              "- `tables/drugs.parquet` — drug == " + json.dumps(d),
              "- `tables/drugdoses.parquet` — dd in " + ", ".join(str(i) for i in rows),
              "- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows",
              "- `embed/drugdose_vectors.npy` — those rows", ""]
        return "\n".join(L)

    # ------------------------------------------------------------------ line notes
    def line_notes(self):
        R = self.R
        le = R.le
        Az = self._load_opt(os.path.join(self.out, "atlas", "effects", "DD_Az.npy"))
        A_ = self._load_opt(os.path.join(self.out, "atlas", "effects", "DD_A.npy"))
        beta = self._load_opt(os.path.join(self.out, "atlas", "effects", "DD_beta.npy"))
        # gene x line baseline and counts
        gK, L_ = R.gK, R.L
        base = np.full((gK, L_), np.nan)
        expr = np.zeros((gK, L_), dtype=bool)
        nup = np.zeros((gK, L_))
        ndn = np.zeros((gK, L_))
        cc, ll = le["col"].astype(int), le["line"].astype(int)
        base[cc, ll] = le["baseline_cpm"]
        expr[cc, ll] = le["expressed"].astype(bool)
        nup[cc, ll] = np.nan_to_num(le["n_dd_up"].astype(float))
        ndn[cc, ll] = np.nan_to_num(le["n_dd_down"].astype(float))
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", category=RuntimeWarning)
            med = np.nanmedian(base, axis=1)
        comp = _read(os.path.join(self.out, "embed", "components.parquet"))
        sens = self._load_opt(os.path.join(self.out, "embed", "line_response_vectors.npy"))
        clean_dd = ~R.dd_artifact
        for line in range(L_):
            self.W.write(f"Cell lines/{self.line_name[line]}.md",
                         self.line_note(line, base, expr, med, nup, ndn, Az, A_, beta, clean_dd, comp, sens))

    @staticmethod
    def _depleted_text(t):
        """lines.parquet n_dd_depleted (-1 = the line is not in the growth analysis) and n_dd_depleted_clean."""
        n = t.get("n_dd_depleted")
        if not _finite(n):
            return "—"
        if int(n) < 0:
            return "not measured (the line is not in the growth analysis)"
        nc = t.get("n_dd_depleted_clean")
        return (f"{int(n):,} (abundance z ≤ −3; drug-doses whose flags make abundance untrustworthy left out)"
                + (f"; {int(nc):,} without any artifact flag" if _finite(nc) else ""))

    def line_note(self, line, base, expr, med, nup, ndn, Az, A_, beta, clean_dd, comp, sens):
        R = self.R
        t = R.tl.iloc[line]
        drivers = [x.strip() for x in sval(t.get("drivers")).split(";") if x.strip()]
        fm = {"cell_line": R.cell[line], "type": "cell line", "cell_line_id": sval(t.get("cell_line_id")),
              "depmap_id": sval(t.get("Cell_ID_DepMap")), "organ": sval(t.get("Organ")),
              "tp53_status": R.tp53[line], "drivers": drivers,
              "n_dd_depleted": int(t["n_dd_depleted"]) if _finite(t.get("n_dd_depleted")) and
              int(t["n_dd_depleted"]) >= 0 else None,
              "median_response": round(float(t["median_response"]), 3) if _finite(t.get("median_response")) else None,
              "tags": ["cell-line"] + ([f"organ/{safe_filename(sval(t.get('Organ'))).replace(' ', '-').lower()}"]
                                       if sval(t.get("Organ")) else [])}
        self.lit_frontmatter("line", line, fm)
        L = [frontmatter(fm), f"# {R.cell[line]}", "",
             f"*{cell(sval(t.get('Organ')) or 'organ unknown')} · TP53 {R.tp53[line]} · "
             f"{cell(sval(t.get('cell_line_id')))} · {cell(sval(t.get('Cell_ID_DepMap')))}*", ""]
        rows = [["Organ", sval(t.get("Organ")) or "—"], ["TP53 status", R.tp53[line]],
                ["Drivers", sval(t.get("drivers")) or "—"], ["Driver changes", sval(t.get("driver_changes")) or "—"],
                ["Cells over all wells", fint(t.get("n_cells_total"))],
                ["Wells with usable expression", f"{fint(t.get('wells_usable'))} ({g3(t.get('pct_wells_usable'))}%)"],
                ["Median response strength (β)", g3(t.get("median_response")) + " (1 = a typical line)"],
                ["Drug-doses that deplete it", self._depleted_text(t)],
                ["Genes it measures (expresses above the ambient level)", f"{int(expr[:, line].sum()):,} of {R.gK:,}"]]
        L += table(["", ""], rows) + [""]
        if Az is not None:
            a = np.where(clean_dd, Az[:, line], np.nan)
            oo = [i for i in np.argsort(np.nan_to_num(a, nan=np.inf)) if _finite(a[i]) and a[i] <= -3][:12]
            L += ["## Drug-doses that deplete it", "",
                  "*Clean drug-doses with relative-abundance z ≤ −3 (`atlas/effects/DD_Az.npy`, column "
                  f"{line}): the line loses cells relative to the other lines in the same wells.*", ""]
            if oo:
                L += table(["Drug-dose", "Abundance z", "log2 relative abundance"],
                           [[self.ddlink(i), fz(a[i]), flog(A_[i, line]) if A_ is not None else "—"] for i in oo]) + [""]
            else:
                L += ["None.", ""]
        if beta is not None:
            b = np.where(clean_dd & (R.dd_nsig >= 20), beta[:, line], np.nan)
            fin = [i for i in np.argsort(-np.nan_to_num(b, nan=-np.inf), kind="stable") if _finite(b[i])]
            k = min(8, len(fin) // 2)                          # strongest and weakest never share a drug-dose
            hi, lo = (fin[:k], fin[::-1][:k]) if k else (fin, [])
            L += ["## How strongly it responds", "",
                  "*β = slope of the line's changes on the drug-dose's consensus (`atlas/effects/DD_beta.npy`; 1 = "
                  "typical, 0 = no response), clean drug-doses with ≥ 20 significant genes.*", ""]
            if hi:
                L += ["- Strongest: " + "; ".join(f"{self.ddlink(i)} ({g3(b[i])})" for i in hi)]
                L += (["- Weakest: " + "; ".join(f"{self.ddlink(i)} ({g3(b[i])})" for i in lo)] if lo else []) + [""]
            else:
                L += ["No drug-dose qualifies.", ""]
        # genes it moves most
        L += ["## Genes it moves most", "",
              f"*Genes with the most clean drug-doses moving them ≥ {R.line_fold:.3g}× at {self.line_cut_text()} "
              f"in this line (`tables/line_effects.parquet`, line == {line}).*", ""]
        for nm, M in (("up", nup), ("down", ndn)):
            v = M[:, line]
            oo = [i for i in np.argsort(-v, kind="stable")[:12] if v[i] > 0]
            L += [f"- {nm}: " + (", ".join(f"{self.glink(i)} ({int(v[i])})" for i in oo) or "none")]
        L += [""]
        # line-specific levels
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", category=RuntimeWarning)
            ratio = np.log2((base[:, line] + 1.0) / (med + 1.0))
        hi = [i for i in np.argsort(-np.nan_to_num(ratio, nan=-np.inf)) if _finite(ratio[i]) and ratio[i] >= 1
              and base[i, line] >= 10][:15]
        lo = [i for i in np.argsort(np.nan_to_num(ratio, nan=np.inf)) if _finite(ratio[i]) and ratio[i] <= -1
              and med[i] >= 20 and not expr[i, line]][:15]
        L += ["## Its own level", "",
              "*Baseline CPM in this line vs the median line (`tables/line_effects.parquet` baseline_cpm; log2 "
              "ratio). Lacks = expressed at ≥ 20 CPM in the median line, not measured here (below 25% of the "
              f"median line, or below {R.amb_frac:g} × the gene's pooled level, where the line reads only ambient "
              "RNA; deletion, silencing or lineage).*", "",
              "- Highest relative to other lines: " + (", ".join(f"{self.glink(i)} ({ratio[i]:+.1f})" for i in hi)
                                                       or "none"),
              "- Lacks: " + (", ".join(f"{self.glink(i)} ({ratio[i]:+.1f})" for i in lo) or "none"), ""]
        if sens is not None and comp is not None and np.isfinite(sens[line]).any():
            s = sens[line]

            def comp_text(j):
                cr = comp.iloc[j]
                return (f"component {int(cr['component'])} ({g3(s[j])}; genes "
                        f"{cell(', '.join(sval(cr['top_pos_genes']).split(', ')[:4]))} / "
                        f"{cell(', '.join(sval(cr['top_neg_genes']).split(', ')[:4]))})")
            ok = [j for j in range(min(len(s), len(comp))) if _finite(s[j])]
            low = sorted([j for j in ok if s[j] < 0.7], key=lambda j: s[j])[:4]
            high = sorted([j for j in ok if s[j] > 1.5], key=lambda j: -s[j])[:4]
            L += ["## In the vector space", "",
                  "*Response sensitivity per component of the space (`embed/line_response_vectors.npy` row "
                  f"{line}): 1 = the programme responds as in a typical line, 0 = it does not respond here. Genes = "
                  "the component's top + / − genes.*", ""]
            if low:
                L += ["- Weak here (< 0.7): " + "; ".join(comp_text(j) for j in low)]
            if high:
                L += ["- Strong here (> 1.5): " + "; ".join(comp_text(j) for j in high)]
            if not low and not high:
                L += [f"- Every component responds within 0.7–1.5 of a typical line (range {g3(np.nanmin(s))} to "
                      f"{g3(np.nanmax(s))})."]
            L += [""]
        L += self.sec_literature("line", line, f"Cell lines/{self.line_name[line]}.md")
        L += ["## Data", "",
              f"- `tables/lines.parquet` — line == {line}; `tables/line_effects.parquet` — line == {line}",
              f"- `atlas/effects/DD_A.npy`, `DD_Az.npy`, `DD_beta.npy`, `line_cpm.npy` — column / row {line}; "
              f"`tensor/DDL_lfc.npy`, `DDL_z.npy` — [:, :, {line}]", ""]
        return "\n".join(L)

    # ------------------------------------------------------------------ plate notes
    def plate_notes(self):
        R = self.R
        sm_p = os.path.join(self.out, "atlas", "sample_map.csv")
        sm = pd.read_csv(sm_p, dtype={"plate": str, "well": str, "drug": str}) if os.path.exists(sm_p) else None
        w = R.wells.copy()
        w["w"] = np.arange(len(w))
        for p, num, idx, have, dmso, info in self.grid:
            self.W.write(f"Plates/{self.plate_name[p]}.md", self.plate_note(p, num, w[w["plate"] == p], sm, info))

    def plate_note(self, p, num, w, sm, info):
        g = (lambda k: info.get(k) if info is not None else None)
        failed = [x.strip() for x in sval(g("failed_wells")).split(",") if x.strip()]
        fm = {"plate": p, "type": "plate", "number": num, "dose": sval(g("doses")),
              "unreliable": bool(g("unreliable")) if g("unreliable") is not None else None,
              "plate_factor": round(float(g("plate_factor")), 3) if _finite(g("plate_factor")) else None,
              "n_wells": int(g("n_wells")) if _finite(g("n_wells")) else len(w),
              "dmso_wells": sval(g("dmso_wells")), "failed_wells": failed, "tags": ["plate"]}
        L = [frontmatter(fm), f"# Plate {num:02d}", ""]
        sub = [f"`{p}`", f"dose {fdose(sval(g('doses')))}" if sval(g("doses")) else "",
               f"{fint(g('n_wells'))} wells analysed", f"plate factor {g3(g('plate_factor'))}",
               "**unreliable**" if g("unreliable") else "reliable"]
        L += [" · ".join(x for x in sub if x), ""]
        L += ["The plate factor divides every z of this plate (1 = as noisy as its peers; > 1.2 sets the drug-dose "
              "flag `noisy plate (z scaled)`). An unreliable plate's wells are used only for drug-doses with no other "
              f"well (flag `unreliable plate only`). DMSO wells: {sval(g('dmso_wells')) or '—'}. Failed wells "
              f"(excluded: < 1/8 of the plate's typical cells while the drug did fine elsewhere): "
              f"{', '.join(failed) or 'none'}. Median cells per analysed well: {g3(g('median_cells_per_well'))}. "
              "Source: `tables/plates.parquet`, `tables/wells.parquet`.", ""]
        # all wells of the plate: analysed (wells.csv) + the rest of the sample map
        rec = {}
        for r in w.itertuples(index=False):
            s = T.slot_from_well(r.well)
            if not _finite(s):
                continue
            fl = []
            if r.is_dmso:
                fl.append("DMSO")
            if bool(getattr(r, "unreliable_plate", False)):
                fl.append("unreliable plate")
            if bool(getattr(r, "position_not_correctable", False)):
                fl.append("position not correctable")
            if not r.is_dmso and not bool(getattr(r, "used_in_drugdose", True)):
                fl.append("not used in its drug-dose")
            cl = getattr(r, "cells_log2_vs_plate", np.nan)
            if _finite(cl) and cl < -1 and not r.is_dmso:
                fl.append("low cells")
            rec[int(s)] = (r.well, str(r.drug), sval(r.dose), getattr(r, "cells", np.nan), cl, fl, bool(r.is_dmso))
        if sm is not None:
            for r in sm[sm["plate"].astype(str) == p].itertuples(index=False):
                s = T.slot_from_well(r.well)
                if _finite(s) and int(s) not in rec:
                    fl = ["failed (excluded)" if str(r.well) in failed else "not analysed"]
                    dmso_ = str(r.drug).upper().startswith("DMSO")
                    dose_ = ("%.6g" % float(r.conc)) if _finite(r.conc) and not dmso_ else ""
                    rec[int(s)] = (r.well, str(r.drug), dose_, r.n_cells, np.nan, fl, dmso_)
        # layout grid
        grid = ["| |" + "|".join(str(j) for j in range(1, 13)) + "|", "|-" * 13 + "|"]
        for r in range(8):
            cells_ = []
            for j in range(12):
                x = rec.get(r * 12 + j + 1)
                if x is None:
                    cells_.append("·")
                else:
                    nm = "DMSO" if x[6] else cell(x[1])[:10].strip()
                    cells_.append(f"**{nm}**" if x[6] else nm)
            grid.append(f"|{ROWS[r]}|" + "|".join(cells_) + "|")
        L += ["## Layout", "", "*Drug in each well (names cut to 10 characters; the table below has them in full). "
              "The per-gene plates notes use the same 8 × 12 layout.*", ""] + grid + [""]
        body = []
        for s in sorted(rec):
            wl, drug, dose, cells_, cl, fl, dm = rec[s]
            body.append([wl, "DMSO" if dm else self.dlink(drug), fdose(dose) if not dm else "—", fint(cells_),
                         flog(cl), ", ".join(fl)])
        L += ["## Wells", "", "*Cells = cells of the analysed lines in the well; log2 vs plate = cells vs the plate's "
              "median drug well.*", ""]
        L += table(["Well", "Drug", "Dose", "Cells", "log2 vs plate", "Flags"], body) + [""]
        return "\n".join(L)

    # ------------------------------------------------------------------ module notes and canvases
    def module_notes(self):
        R = self.R
        mods = R.modules["module"].astype(int).to_numpy()
        members = {m: np.flatnonzero(R.module == m) for m in mods}
        ed = R.edges
        ea, eb = ed["col_a"].to_numpy(), ed["col_b"].to_numpy()
        es = np.sign(ed["cos"].to_numpy())
        ma, mb = R.module[ea], R.module[eb]
        for k, m in enumerate(mods):
            mem = members[m]
            sel = np.flatnonzero((ma == m) & (mb == m))
            row = R.modules.iloc[k]
            self.W.write(f"Modules/{self.module_name[m]}.md", self.module_note(m, k, row, mem))
            self.W.write(f"Modules/{self.module_name[m]}.canvas", self.canvas(m, mem, ea[sel], eb[sel], es[sel]))

    def module_note(self, m, k, row, mem):
        R = self.R
        lab = R.mod_label.get(m, ("", "", np.nan))
        plus = sorted([c for c in mem if R.arm[c] == "+"], key=lambda c: (-abs(R.axis_proj[c]), c))
        minus = sorted([c for c in mem if R.arm[c] == "-"], key=lambda c: (-abs(R.axis_proj[c]), c))
        lt = self.mod_label_text(m)
        opp = bool(R.mod_opp.get(m))
        fm = {"module": m, "type": "module", "n_genes": len(mem), "n_plus": len(plus), "n_minus": len(minus),
              "arms_opposite": opp, "mean_cos_between_arms": R.mod_between.get(m, np.nan),
              "label": lt, "label_source": lab[1] if lt else "", "tags": ["module"]}
        name = self.module_name[m]
        armline = (f"{len(plus)} in the + arm, {len(minus)} in the − arm" if opp else "single-armed")
        L = [frontmatter(fm), f"# {name}", "",
             f"*{cell(lt) + ' · ' if lt else ''}{len(mem)} genes ({armline}) · [[{name}.canvas|open the canvas]]*", "",
             "A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| "
             f"that are replicated (`both halves`: same sign, fdr ≤ {REPRO_FDR:.2f}, in two random halves of the "
             "compounds) or very strong in one random half (`graph/`). " + self.arms_text(m) +
             (" The + arm rises where the − arm falls. Arm = the side of the module's main direction a gene sits on."
              if opp else ""), ""]
        if self.mod_label_text(m):
            L += [f"Label from the validation stage: **{cell(lab[0])}** ({lab[1]}"
                  + (f", q {fq(lab[2])}" if _finite(lab[2]) else "") + "; `validation/module_labels.csv`).", ""]
        elif R.have_validation:
            L += ["No gene set is enriched enough to label it (`validation/module_labels.csv`).", ""]
        if R.mod_enrich is not None:
            e = R.mod_enrich[(R.mod_enrich["module"] == m) & (R.mod_enrich["q"] < 0.05)].sort_values("q").head(8)
            if len(e):
                L += ["## Enriched for", "", "*Hypergeometric test per arm, BH q (`validation/module_enrichment.csv`).*",
                      ""]
                L += table(["Arm", "Set", "Source", "Overlap", "Fold", "q"],
                           [[r.arm, r.set_label, r.source, f"{int(r.overlap)}/{int(r.n_unit)}", g3(r.fold), fq(r.q)]
                            for r in e.itertuples(index=False)]) + [""]
        if R.mod_z is not None:
            z = R.mod_z[k]
            oo = np.argsort(-np.nan_to_num(z, nan=0.0))
            L += ["## Drugs that move it", "",
                  ("*Mean pooled z of the + arm minus the − arm" if opp else "*Mean pooled z of its genes") +
                  f" (`graph/module_pooled_z.npy`, row {k}), the 10 strongest with |z| ≥ 1. † = artifact flag.*", ""]
            up = [i for i in oo[:10] if _finite(z[i]) and z[i] >= 1]
            dn = [i for i in oo[::-1][:10] if _finite(z[i]) and z[i] <= -1]
            L += [("- Raise it (+ arm up, − arm down): " if opp else "- Raise it: ") + ("; ".join(
                f"{self.ddlink(i)}{' †' if R.dd_artifact[i] else ''} ({fz(z[i])})" for i in up) or "none"),
                  "- Lower it: " + ("; ".join(
                      f"{self.ddlink(i)}{' †' if R.dd_artifact[i] else ''} ({fz(z[i])})" for i in dn) or "none"), ""]
        rl = [x.strip() for x in sval(row.get("responsive_lines")).split(",") if x.strip()]
        if rl:
            idx = {n: i for i, n in enumerate(R.cell)}
            L += ["## Cell lines where it responds most", "",
                  "*The lines with the largest mean |module score| over the module's 8 strongest drug-doses "
                  "(`graph/modules.parquet` responsive_lines), strongest first.*", "",
                  "- " + ", ".join(self.llink(idx[n]) if n in idx else cell(n) for n in rl), ""]
        if R.novel_members is not None:
            nm = R.novel_members[R.novel_members["module"] == m].sort_values("mean_cos", ascending=False)
            nm = nm.drop_duplicates("col").head(15)
            if len(nm):
                L += ["## Candidate new members", "",
                      "*Members not annotated to the set their arm is enriched for, ranked by mean cos to the "
                      "annotated members (`validation/novel_members.csv`).*", ""]
                L += table(["Gene", "Set", "Mean cos"], [[self.glink(r.col), r.set_label, fcos(r.mean_cos)]
                                                         for r in nm.itertuples(index=False)]) + [""]
        for arm_name, lst in (("+ arm", plus), ("− arm", minus)):
            L += [f"## {arm_name} ({len(lst)})", ""]
            if not lst:
                L += ["Empty." if opp else "None: a single-armed module.", ""]
                continue
            body = []
            for c in lst:
                nmx = sval(R.ann["name"].iloc[c]) if R.ann is not None else ""
                body.append([self.glink(c), g3(R.axis_proj[c]), nmx or "—"])
            L += table(["Gene", "Projection", "Name"], body) + [""]
        L += ["## Data", "", f"- `graph/nodes.parquet` — module == {m}; `graph/modules.parquet` — module == {m}; "
              f"`graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [{k}] (drug-dose × line)",
              ""]
        return "\n".join(L)

    def canvas(self, m, mem, ea, eb, es):
        """Obsidian canvas: one file node per member at its nodal-map position, edges of the module graph."""
        R = self.R
        xy = R.xy[mem]
        ok = np.isfinite(xy).all(axis=1)
        xy = np.where(ok[:, None], xy, np.nanmean(xy, axis=0) if ok.any() else 0.0)
        lo = xy.min(axis=0)
        span = float(max((xy.max(axis=0) - lo).max(), 1e-9))
        n = len(mem)
        need = math.sqrt(n * NODE_W * NODE_H * 3.0)              # room for the nodes without overlap
        scale = max(CANVAS_SPAN, need) / span
        cw, ch = NODE_W + 20, NODE_H + 20
        taken = set()
        nodes, ids = [], {}
        order = sorted(range(n), key=lambda i: (-abs(R.axis_proj[mem[i]]), mem[i]))
        for i in order:
            c = int(mem[i])
            gx = int(round((xy[i, 0] - lo[0]) * scale / cw))
            gy = int(round((xy[i, 1] - lo[1]) * scale / ch))
            pos = None
            for rad in range(0, 200):
                cand = [(gx + dx, gy + dy) for dx in range(-rad, rad + 1) for dy in range(-rad, rad + 1)
                        if max(abs(dx), abs(dy)) == rad]
                cand.sort(key=lambda t: ((t[0] - gx) ** 2 + (t[1] - gy) ** 2, t))
                for t in cand:
                    if t not in taken:
                        pos = t
                        break
                if pos:
                    break
            taken.add(pos)
            nid = f"g{c}"
            ids[c] = nid
            nodes.append({"id": nid, "type": "file", "file": self.gene_path[c], "x": pos[0] * cw,
                          "y": pos[1] * ch, "width": NODE_W, "height": NODE_H,
                          "color": "4" if R.arm[c] == "+" else "1"})
        lab = self.mod_label_text(m)
        arms = ("Green = + arm, red = − arm (the arms move opposite under the same drugs)." if R.mod_opp.get(int(m))
                else "A single-armed module: every gene is + (green).")
        nodes.insert(0, {"id": "legend", "type": "text", "x": -40, "y": -260, "width": 560, "height": 200,
                         "text": f"**{self.module_name[m]}**" + (f" — {lab}" if lab else "") +
                                 f"\n\n{n} genes at their nodal-map positions. {arms} Edge label + = move together, "
                                 "− = opposite."})
        edges = []
        for a, b, s in sorted(zip(ea.tolist(), eb.tolist(), es.tolist())):
            if a in ids and b in ids:
                edges.append({"id": f"e{a}_{b}", "fromNode": ids[a], "toNode": ids[b],
                              "label": "+" if s > 0 else "-"})
        dump = (lambda x: json.dumps(x, ensure_ascii=False, separators=(", ", ": ")))
        return ('{\n"nodes": [\n' + ",\n".join(dump(x) for x in nodes) + '\n],\n"edges": [\n' +
                ",\n".join(dump(x) for x in edges) + "\n]\n}")

    # ------------------------------------------------------------------ indexes
    @staticmethod
    def _letter(s):
        ch = s[:1].upper()
        if ch.isalpha() and ch.isascii():
            return ch
        return "0-9" if ch.isdigit() else "other"

    def index_notes(self):
        R = self.R
        N = self.names
        # genes by letter
        groups = {}
        for c in range(R.gK):
            groups.setdefault(self._letter(R.label[c]), []).append(c)
        keys = sorted(groups, key=lambda k: (len(k) > 1, k))
        parts = _chunks({k: sorted(groups[k], key=lambda c: (R.label[c].lower(), c)) for k in keys}, GENES_PER_INDEX,
                        "Genes", N)
        L = [frontmatter({"type": "index", "tags": ["index"]}), "# Genes by letter", "",
             f"{R.gK:,} gene notes, one per gene that Tahoe detected (gene columns of `atlas/effects/genes.csv`). "
             "Genes below the detection limit have no note: [[Genes below the detection limit]].", ""]
        L += ["- " + " · ".join(f"[[{nm}|{tag}]] ({len(lst):,})" for nm, tag, lst in parts), ""]
        self.W.write("Indexes/Genes by letter.md", "\n".join(L))
        for nm, tag, lst in parts:
            body = []
            for c in lst:
                nmx = sval(R.ann["name"].iloc[c]) if R.ann is not None else ""
                m = int(R.module[c])
                tail = f" · module {m:03d} {R.arm[c]}" if m > 0 else ""
                body.append(f"- {self.glink(c)}" + (f" — {cell(nmx)}" if nmx else "") + tail)
            self.W.write(f"Indexes/{nm}.md",
                         "\n".join([frontmatter({"type": "index", "tags": ["index"]}), f"# Genes {tag}", "",
                                    f"{len(lst):,} genes. Back to [[Genes by letter]].", ""] + body))
        # genes by module
        L = [frontmatter({"type": "index", "tags": ["index"]}), "# Genes by module", "",
             "Modules of the nodal map (`graph/modules.parquet`), largest first, with every member by arm. "
             f"{int(R.included.sum()):,} genes are in the vector space; {int(((R.module == 0) & R.included).sum()):,} "
             f"of them are in no module (module 0); {int((~R.included).sum()):,} genes are not in the vector space.",
             ""]
        for r in R.modules.itertuples(index=False):
            m = int(r.module)
            mem = np.flatnonzero(R.module == m)
            lab = self.mod_label_text(m)
            L += [f"## {self.mlink(m)}" + (f" — {cell(lab)}" if lab else "") + f" ({len(mem)}"
                  + ("" if R.mod_opp.get(m) else ", single-armed") + ")", ""]
            for a in (("+", "-") if R.mod_opp.get(m) else ("+",)):
                lst = sorted([c for c in mem if R.arm[c] == a], key=lambda c: (-abs(R.axis_proj[c]), c))
                L += [f"- **{a}** ({len(lst)}): " + (", ".join(self.glink(c) for c in lst) or "—")]
            L += [""]
        self.W.write("Indexes/Genes by module.md", "\n".join(L))
        # drugs by mechanism
        d = R.tdrugs.copy()
        d["moa_broad"] = d["moa_broad"].map(sval).replace("", "unknown") if "moa_broad" in d else "unknown"
        d["moa_fine"] = d["moa_fine"].map(sval).replace("", "unknown") if "moa_fine" in d else "unknown"
        L = [frontmatter({"type": "index", "tags": ["index"]}), "# Drugs by mechanism", "",
             f"{len(d)} drugs (`tables/drugs.parquet`), by broad then fine mechanism of action (Tahoe drug "
             "metadata). In brackets: the most significant genes at any dose.", ""]
        for broad, sub in d.groupby("moa_broad", sort=True):
            L += [f"## {cell(broad)}", ""]
            for fine, s2 in sub.groupby("moa_fine", sort=True):
                L += [f"- **{cell(fine)}**: " + ", ".join(
                    f"{self.dlink(x)} ({fint(ms, '0')})" for x, ms in
                    sorted(zip(s2["drug"].astype(str), s2.get("max_sig", pd.Series([np.nan] * len(s2))))))]
            L += [""]
        self.W.write("Indexes/Drugs by mechanism.md", "\n".join(L))
        # lines by organ
        t = R.tl.copy()
        t["Organ"] = t["Organ"].map(sval).replace("", "unknown") if "Organ" in t else "unknown"
        L = [frontmatter({"type": "index", "tags": ["index"]}), "# Lines by organ", "",
             f"{len(t)} cell lines (`tables/lines.parquet`), pooled in every well. TP53 status from the Tahoe "
             "cell-line metadata.", ""]
        for organ, sub in t.groupby("Organ", sort=True):
            L += [f"## {cell(organ)}", ""]
            L += table(["Line", "TP53", "Drivers"],
                       [[self.llink(int(r.line)), R.tp53[int(r.line)], sval(r.drivers) or "—"]
                        for r in sub.sort_values("cell_name").itertuples(index=False)]) + [""]
        self.W.write("Indexes/Lines by organ.md", "\n".join(L))
        # below the detection limit
        self.below_detection(N)

    def below_detection(self, N):
        R = self.R
        fi = {}
        p = os.path.join(self.out, "atlas", "file_index.json")
        if os.path.exists(p):
            try:
                with open(p, encoding="utf-8") as fh:
                    fi = json.load(fh)
            except (OSError, ValueError):
                fi = {}
        files = [f for f in fi.get("gene", []) or [] if os.path.exists(f)]
        L = [frontmatter({"type": "index", "tags": ["index"]}), "# Genes below the detection limit", ""]
        if not files:
            L += ["The Tahoe gene metadata is not reachable from this run (`atlas/file_index.json` → gene), so the "
                  "list of undetected genes cannot be made.", ""]
            self.W.write("Indexes/Genes below the detection limit.md", "\n".join(L))
            return
        gm = T.read_tables(files, ["token_id", "gene_symbol", "ensembl_id"])
        gm = gm[~gm["token_id"].isin(set(R.token.tolist()))]
        sy = gm["gene_symbol"].fillna(gm["ensembl_id"]).astype(str)
        groups = {}
        for s in sorted(set(sy), key=lambda x: (x.lower(), x)):
            groups.setdefault(self._letter(s), []).append(s)
        keys = sorted(groups, key=lambda k: (len(k) > 1, k))
        parts = _chunks({k: groups[k] for k in keys}, NAMES_PER_INDEX, "Below detection", N)
        L += [f"{len(gm):,} genes of the Tahoe gene metadata are not among the {R.gK:,} gene columns: too few counts "
              "in the build for the atlas to keep them (pooled level below its cut). They have no note and no "
              "effects; listed here, without links, so that an absent note is not mistaken for a missing gene.", "",
              "- " + " · ".join(f"[[{nm}|{tag}]] ({len(lst):,})" for nm, tag, lst in parts), ""]
        self.W.write("Indexes/Genes below the detection limit.md", "\n".join(L))
        for nm, tag, lst in parts:
            self.W.write(f"Indexes/{nm}.md",
                         "\n".join([frontmatter({"type": "index", "tags": ["index"]}), f"# Below detection {tag}", "",
                                    f"{len(lst):,} genes. Back to [[Genes below the detection limit]].", "",
                                    ", ".join(cell(x) for x in lst), ""]))

    # ------------------------------------------------------------------ Home, How to read, .obsidian
    def home(self):
        R = self.R
        ei = R.embed_info
        n_written = sum(1 for c in range(R.gK) if R.sym[c] in self.fragments)
        stamps = {}
        for s in ("build", "effects", "tensor", "tables", "embed", "reference", "relations", "graph", "validate"):
            p = os.path.join(self.out, "stages", s + ".json")
            if os.path.exists(p):
                try:
                    with open(p, encoding="utf-8") as fh:
                        st = json.load(fh)
                    stamps[s] = f"v{st.get('version')}, {st.get('finished', '')}"
                except (OSError, ValueError):
                    pass
        L = [frontmatter({"type": "index", "tags": ["index", "home"]}), "# Home", "",
             "The reading room of a **tahoemap** run on [[Tahoe-100M]]: for every gene, which drugs raise or lower it "
             "and in which cell lines, which genes move with it or opposite to it, and where it sits in the vector "
             "space and the nodal map.", "",
             f"Run folder: `{self.out}`. Every path quoted in a note is relative to it.", "",
             "| | |", "|---|---|",
             f"| Genes with a note | {R.gK:,} ({n_written} with a written section) |",
             f"| Genes in the vector space | {int(R.included.sum()):,} ({ei.get('dims', '?')} dimensions, "
             f"{fint(ei.get('contexts'))} (drug-dose, line) contexts) |",
             f"| Modules | {len(self.module_name)} |",
             f"| Drugs / drug-doses | {len(self.drug_name)} / {R.Dn:,} |",
             f"| Cell lines | {R.L} |", f"| Plates / wells | {len(self.plate_name)} / {R.N:,} |"]
        if self.lit:
            nk = {k: sum(1 for x in self.lit if x[0] == k) for k in REVIEW_KINDS}
            L += ["| Literature reviews (AI agents; `review/`) | " + ", ".join(
                f"{nk[k]:,} {w if nk[k] == 1 else w + 's'}" for k, w in (("gene", "gene"), ("drug", "drug"),
                                                                        ("line", "cell line")))
                  + " (tag `#literature-review`) |"]
        L += ["",
             "## Start here", "",
             "| If you want | Read |", "|---|---|",
             "| what every section of a note means, and the baseline of every fold change | [[How to read this vault]] |",
             "| a gene | the quick switcher (Ctrl/Cmd-O), or [[Genes by letter]] |",
             "| the modules of the nodal map | [[Genes by module]] |",
             "| a drug | [[Drugs by mechanism]] |", "| a cell line | [[Lines by organ]] |",
             "| why a gene has no note | [[Genes below the detection limit]] |",
             "| a plate's layout and its failed wells | " + ", ".join(f"[[{n}]]" for n in self.plate_name.values())
             + " |", "",
             "## Concepts", "",
             "Written notes (from `tahoemap/vault_seed/notes/`), each explained once:", ""]
        L += ["- " + ", ".join(f"[[{n}]]" for n in sorted(self.seed_notes.values())), ""]
        if R.have_validation:
            mt = R.metrics
            cs = mt.get("control_sets", {}) or {}
            ml = mt.get("module_labels", {}) or {}
            nv = mt.get("novel", {}) or {}
            L += ["## Validation", "",
                  "From `validation/report.md` (curated control programmes not derived from Tahoe):", "",
                  f"- Control sets: {cs.get('n_sets', '?')} scored; median AUROC (signed cos) "
                  f"{g3(cs.get('median_auroc_cos'))}; {cs.get('n_auroc_cos_ge_0.6', '?')} with AUROC ≥ 0.6.",
                  f"- Modules labelled by enrichment: {ml.get('labelled', '?')} of {ml.get('modules', '?')}.",
                  ("- Novel candidate relations: " + (f"{fint(nv.get('edges'))} edges" if R.novel_assessed else
                                                       "not assessed (" + (", ".join(R.novel_blocked) or
                                                                           "reference sources") + " missing)")
                   + f"; candidate new set members: {fint(nv.get('member_genes'))} genes."), ""]
            ops = [op for op in (mt.get("opposite_pairs") or []) if _finite(op.get("mean_cross_cos"))]
            for op in ops[:3]:
                L += [f"- Opposite-arm test {op.get('a')} / {op.get('b')}: mean cross-set cos "
                      f"{fcos(op.get('mean_cross_cos'))} (expect < 0); share of cross pairs in one module "
                      f"{g3(op.get('share_same_module'))} (random pairs {g3(op.get('random_same_module'))})."]
            if ops:
                L += [""]
        L += ["## Largest modules", ""]
        top = R.modules.sort_values(["n_genes", "module"], ascending=[False, True]).head(12)
        L += table(["Module", "Label", "Genes", "+ arm (top)", "− arm (top)"],
                   [[self.mlink(int(r.module)), self.mod_label_text(int(r.module)) or "—", int(r.n_genes),
                     ", ".join(sval(r.top_plus).split(", ")[:4]), ", ".join(sval(r.top_minus).split(", ")[:4])]
                    for r in top.itertuples(index=False)]) + [""]
        L += ["## The run", "", "Stage stamps (`stages/*.json`):", ""]
        L += [f"- {k}: {v}" for k, v in stamps.items()] + [""]
        src = (R.sources or {}).get("sources") or {}
        if src:
            L += ["Registry downloads (`reference/sources.json`):", ""]
            L += [f"- {k}: " + ", ".join(x for x in (sval(v.get("status")), sval(v.get("date"))[:10],
                                                      f"{fint(v.get('n_rows'))} rows" if _finite(v.get("n_rows"))
                                                      else "", cell(sval(v.get("error")))[:120]) if x)
                  for k, v in sorted(src.items()) if isinstance(v, dict)] + [""]
        L += ["## Honesty ledger", "",
              "Corrections to the written layer are recorded, not hidden: [[Corrections and retractions]]."
              if "Corrections and retractions" in self.seed_notes else "", ""]
        self.W.write(f"{self.fixed['Home']}.md", "\n".join(L))

    def how_to_read(self):
        R = self.R
        if R.line_z_calibrated:
            line_cut = ("The per-line cut is calibrated on this run (`tables/info.json`): a per-line z rests on one or "
                        "two wells and its tails are heavier than a normal's, so with ~1,100 drug-doses per gene and "
                        "line a fixed cut of 3 or 4 is passed by chance; at this cut about "
                        f"{g3(R.line_z_chance)} chance calls are expected per gene and line over the "
                        f"{fint(R.line_z_ndd)} clean drug-doses." if R.line_z_chance is not None else
                        "The per-line cut is calibrated on this run (`tables/info.json`).")
        else:
            line_cut = ("This run's tables carry no calibrated per-line cut, so it is a fixed one: a per-line z of 4-5 "
                        "can arise by chance.")
        novel_status = ("" if R.novel_assessed else
                        "; **in this run novelty was not assessed**: " + (", ".join(R.novel_blocked) or
                                                                          "reference sources") + " missing")
        txt = HOW_TO_READ.format(q=Q_CUT, n_drugs=N_DRUGS, n_flag=N_FLAGGED, n_part=N_PARTNERS, n_pred=N_PRED,
                                 line_z=R.line_z, fold=f"{R.line_fold:.3g}", line_cut=line_cut, short=SHORT_POOLED,
                                 amb_frac=R.amb_frac, e_min=R.e_min, repro_fdr=REPRO_FDR, repro_min=REL.REPRO_MIN,
                                 one_half=REL.ONE_HALF, novel_fdr=REL.NOVEL_FDR, novel_cos=REL.NOVEL_COS,
                                 novel_status=novel_status, arm_min=ARM_MIN, arms_opp=ARMS_OPPOSITE,
                                 n_old=self.n_old_study,
                                 artifacts=", ".join(f"`{a}`" for a in A.ARTIFACT_FLAGS))
        if self.lit:
            txt = txt.rstrip("\n") + "\n\n" + LIT_HOWTO
        self.W.write(f"{self.fixed['How to read this vault']}.md",
                     frontmatter({"type": "index", "tags": ["index", "help"]}) + "\n" + txt)

    def obsidian(self):
        od = os.path.join(self.root, ".obsidian")
        os.makedirs(od, exist_ok=True)
        ignore = "/ — plates\\.md$/"

        def merge(name, base, merge_fn):
            p = os.path.join(od, name)
            cur = None
            if os.path.exists(p):
                try:
                    with open(p, encoding="utf-8") as fh:
                        cur = json.load(fh)
                except (OSError, ValueError):
                    cur = None
            new = merge_fn(cur) if cur is not None else base
            if new != cur:
                tmp = p + ".tmp"
                with open(tmp, "w", encoding="utf-8") as fh:
                    json.dump(new, fh, indent=2, ensure_ascii=False)
                os.replace(tmp, p)
        app = {"useMarkdownLinks": False, "newLinkFormat": "shortest", "attachmentFolderPath": "attachments",
               "alwaysUpdateLinks": True, "showUnsupportedFiles": True, "defaultViewMode": "preview",
               "strictLineBreaks": False, "readableLineLength": True, "userIgnoreFilters": [ignore]}

        def app_merge(cur):
            cur = dict(cur)
            f = list(cur.get("userIgnoreFilters", []) or [])
            if ignore not in f:
                f.append(ignore)
            cur["userIgnoreFilters"] = f
            return cur
        merge("app.json", app, app_merge)
        graph = {"collapse-filter": False,
                 "search": '-path:"Indexes" -path:"Plates" -path:"Cell lines" -file:"— plates" '
                           '-file:"Home" -file:"How to read this vault"',
                 "showTags": False, "showAttachments": False, "hideUnresolved": True, "showOrphans": False,
                 "colorGroups": [{"query": 'path:"Drugs"', "color": {"a": 1, "rgb": 14725458}},
                                 {"query": 'path:"Modules"', "color": {"a": 1, "rgb": 5431378}},
                                 {"query": 'path:"Concepts"', "color": {"a": 1, "rgb": 11621088}}],
                 "scale": 0.5}
        merge("graph.json", graph, lambda cur: cur)
        types = {"types": {"aliases": "aliases", "tags": "tags", "symbol": "text", "type": "text", "col": "number",
                           "ensembl_id": "text", "name": "text", "location": "text", "module": "number",
                           "arm": "text", "pooled_cpm": "number", "n_lines_expressing": "number",
                           "n_dd_up_clean": "number", "n_dd_down_clean": "number", "in_vector_space": "checkbox",
                           "generated_by": "text", "source": "text", "drug": "text", "doses": "multitext",
                           "max_sig_genes": "number", "cell_line": "text", "drivers": "multitext",
                           "tp53_status": "text", "n_dd_depleted": "number", "median_response": "number",
                           "plate": "text", "number": "number", "unreliable": "checkbox", "plate_factor": "number",
                           "failed_wells": "multitext", "n_genes": "number", "n_plus": "number",
                           "n_minus": "number", "arms_opposite": "checkbox", "mean_cos_between_arms": "number",
                           "label": "text"}}

        def types_merge(cur):
            cur = dict(cur)
            t = dict(cur.get("types", {}) or {})
            for k, v in types["types"].items():
                t.setdefault(k, v)
            cur["types"] = t
            return cur
        merge("types.json", types, types_merge)
        core = {"file-explorer": True, "global-search": True, "switcher": True, "graph": True, "backlink": True,
                "outgoing-link": True, "tag-pane": True, "properties": True, "outline": True, "word-count": True,
                "bookmarks": True, "canvas": True, "random-note": False, "templates": False}
        merge("core-plugins.json", core, lambda cur: cur)

    # ------------------------------------------------------------------ the build
    def build(self):
        t0 = time.time()
        os.makedirs(self.root, exist_ok=True)
        old_manifest = set()
        mp = os.path.join(self.root, MANIFEST)
        if os.path.exists(mp):
            try:
                with open(mp, encoding="utf-8") as fh:
                    old_manifest = set(json.load(fh).get("files", []))
            except (OSError, ValueError):
                old_manifest = set()
        self.R.load_gene_tables()
        self.R.load_predictions()
        self.load_fragments()
        self.assign_names()
        self.load_literature()
        self.write_concepts()
        self.gene_notes()
        self.drug_notes()
        self.line_notes()
        self.plate_notes()
        self.module_notes()
        self.index_notes()
        self.home()
        self.how_to_read()
        # every basename unique, case-insensitively (Obsidian resolves links by basename)
        seen = {}
        for p in self.W.paths:
            b = os.path.splitext(os.path.basename(p))[0].lower() + os.path.splitext(p)[1]
            assert b not in seen, f"two notes share the basename {b}: {seen[b]} and {p}"
            seen[b] = p
        removed = _clean_stale(self.root, self.W.paths, old_manifest)
        self.obsidian()
        files = sorted(os.path.relpath(p, self.root) for p in self.W.paths)
        tmp = mp + ".tmp"
        with open(tmp, "w", encoding="utf-8") as fh:
            json.dump({"generated_by": GEN, "version": VERSION, "files": files}, fh, indent=0)
        os.replace(tmp, mp)
        gs = np.array(self.gene_sizes)
        ps = np.array(self.plates_sizes)
        info = {"version": VERSION, "notes": len(files), "gene_notes": self.R.gK, "drug_notes": len(self.drug_name),
                "line_notes": self.R.L, "plate_notes": len(self.plate_name), "module_notes": len(self.module_name),
                "concept_notes": len(self.seed_notes), "fragments_spliced": self.n_fragments,
                "fragments_marked_earlier_study": self.n_old_study,
                "fragments_available": len(self.fragments), "written": self.W.n_written,
                "literature_notes": self.n_lit_notes, "literature_partner_cells": self.n_lit_cells,
                "review": self.lit_fp,
                "unchanged": self.W.n_same, "stale_removed": removed, "mb": round(self.W.bytes / 1e6, 1),
                "gene_note_kb_median": round(float(np.median(gs)) / 1e3, 1) if len(gs) else None,
                "gene_note_kb_max": round(float(gs.max()) / 1e3, 1) if len(gs) else None,
                "plates_note_kb_median": round(float(np.median(ps)) / 1e3, 1) if len(ps) else None,
                "plates_note_kb_max": round(float(ps.max()) / 1e3, 1) if len(ps) else None,
                "minutes": round((time.time() - t0) / 60, 2)}
        return info


HOW_TO_READ = """# How to read this vault

Everything here is generated from one run of **tahoemap** on [[Tahoe-100M]], except the written sections (a
gene's "In one line / What it is / What is uncertain / References", and the Concepts notes), which come from
`tahoemap/vault_seed/`. Generated notes are rebuilt on every run: do not edit them; write in `vault_seed/` instead.

The written gene sections come from an **earlier study on the same data** (MG53/TRIM72 and p53). Where one
speaks of a score, a rank, a regulon, an association or "this batch", it means that study's analysis
(transcription-factor activity inferred from target sets, with MG53 as the exposure), which tahoemap does **not**
compute; such sections carry a "Written for the earlier MG53/p53 study" callout ({n_old} in this vault). This run's
own numbers are always in the generated sections.

## The baseline of every fold change

Every fold change is relative to **the same cell line's median over the plate's drug wells** — the typical treated
well, since most drugs leave most genes alone — **not DMSO** (two DMSO wells per plate are too few). For each line
and well: log2 CPM minus that line's plate median, minus the profile's composition (library-size) shift, minus the
well-position effect. So "2× up" means "twice the level of a typical drug well on that plate, in the same line".
*Pooled* values take the median over the lines in each well, then the mean (fold) or a Stouffer sum (z) over the
drug-dose's wells; *per-line* values keep each line. fold = 2^lfc (1 = no change, 0.5 = halved).

*Pooled* means the **median over the cell lines**: a response seen in fewer than about half of the measured lines
(for example one confined to the TP53-wild-type lines) does not reach the pooled lists, the "raised / lowered by"
counts or `tables/drug_effects.parquet`. It appears in the per-line tables (`tables/line_effects.parquet`,
`tables/drug_line_top.parquet`) and in a note's "In which cell lines" section.

## Which lines are measured for a gene

A cell line is **measured** for a gene (`tensor/line_measured.npy`; `expressed` in `tables/line_effects.parquet`;
`n_lines_expressing` in the frontmatter) only when it truly expresses it: at least 25% of the median line (the
atlas's rule) **and** at least {amb_frac:g} × the gene's pooled level. Every well also holds ambient RNA, the average
of all its cells, so a line that does not make the gene still reads about a tenth of the pooled level; that reading
moves with the other lines and with cell loss, not with the line's own regulation. Such **ambient-only** lines have no
per-line values ("n.m." = not measured, in a note). A per-line value is also left out where the profile's **expected
count** of the gene (the line's level × the profile's total UMI ÷ 10⁶) is below {e_min:g}: with 0-1 expected reads
the log2 CPM is the pseudocount and a single read, and a line thinned out by a drug would show false rises. So the
number of lines measured can differ between drug-doses, and re-expression of a gene that a line has silenced is not
seen.

## z, q, significant, clean

- **z** — a robust z against the spread of this gene over the other drug wells on reliable plates (median and
  1.4826 × MAD), Stouffer-combined over the drug-dose's wells and divided by the plate factor on noisy plates. Most
  drug-doses sit in **one well**, so z rests on the spread of other wells, not on replicates.
- **q** — Benjamini–Hochberg within the gene, across all drug-doses (q_up for a rise, q_down for a fall).
- **Significant** — q < {q:.2f} and a change of at least 1.2× (the atlas's rule).
- **Clean** — no artifact flag on the drug-dose, and none of the gene's own ("position correction uncertain").
  Artifact flags: {artifacts}. They mark changes that may come from cell death, a global drop in transcription, a
  shift in the cell-cycle mix, a plate that does not reproduce, or a well-position problem — not regulation of the
  gene. Soft caveats that do **not** make a value unclean: `low cells (technical?)`, `plate-row cell shift`,
  `composition shift`, `noisy plate (z scaled)`, `position effect removed`. The exact definitions are in
  `docs/method.md` of the tahoemap repository.

## A gene note, section by section

- **Frontmatter** — symbol, Ensembl id, registry name and cytoband, module and arm, pooled level (CPM),
  lines expressing it, clean drug-doses raising / lowering it, whether it is in the vector space.
- **Title, name, location**, then the **written section** when someone has written one.
- **At a glance** — a generated "In this data" callout: the strongest clean raiser and lowerer pooled over the cell
  lines (median; fold, z, q, in how many of the measured lines it moves); when fewer than {short} clean drug-doses
  are significant pooled, an "In single lines" sentence names the clean drug-doses that pass the per-line cut in the
  most lines (`tables/drug_line_top.parquet`); its most reliable partners — evidence `both halves`, i.e. the same
  sign with fdr ≤ {repro_fdr:.2f} in two random halves of the compounds, with each partner's fdr; its module and arm.
  (The "In one line" callout above it, when there is one, is the written layer.)
- **Drugs that raise it / lower it** — pooled over the cell lines (median): up to {n_drugs} clean drug-doses with
  |z| ≥ 3 or q < {q:.2f}, strongest first.
  Bold fold = significant. *Lines up / measured* = lines where that drug-dose moves it ≥ 1.2× at per-line z ≥ 2,
  out of the lines measured for it (see above) with enough cells; the first names are the strongest. This count is
  descriptive (per-line z ≥ 2 is not a significance cut). *Dose pattern* = how the
  effect behaves across the drug's doses (rises with dose, top dose only, all doses, single dose, inconsistent).
- **Flagged drug-doses** — the {n_flag} strongest (by |z|) drug-doses that move it but carry an artifact flag. Read
  them as "something happened to the cells", not as regulation.
- **In which cell lines** — one row per line: TP53 status, the line's own level (CPM; "n.m." = not measured, see
  above), how many clean drug-doses move it ≥ {fold}× at per-line |z| ≥ {line_z:.1f} in that line, and the strongest
  of them up and down. {line_cut}
- **Genes that move with it / opposite** — up to {n_part} partners each, from the gene's 100 nearest by |cos|.
  *cos* = signed cosine of the two gene vectors = the correlation of their denoised responses over every
  (drug-dose, cell line) context (+1 always together, −1 always opposite). *Halves* = the same cosine in two vector
  spaces fitted on two random halves of the compounds (a hash split of the compound names; drug families fall in
  both); *evidence* = `both halves` (the same sign in the full space and in both halves, |cos| ≥ {repro_min:g} in
  each, **and** fdr ≤ {repro_fdr:.2f}), `one half` (strong, |cos| ≥ {one_half:g}, in one of the two random halves
  only: not replicated, no error estimate; often one compound), `not reproduced`. *fdr* = the estimated share of
  false relations among pairs at least this strong in both halves, from sign concordance between the halves (see
  [[FDR calibration and the inflated null]]). *Notes*: known links (shared HGNC gene group, shared Hallmark/Reactome
  pathway, STRING score), **novel candidate** (both halves, fdr ≤ {novel_fdr:.2f}, |cos| ≥ {novel_cos:g}, no known
  link, not the same locus, both genes described by HGNC and placed on the genome; assessed only when HGNC, Ensembl,
  STRING and Hallmark or Reactome all loaded{novel_status}), same locus (≤ 50 kb) and **readthrough risk** (same
  strand, ≤ 20 kb, the 5′ gene ≥ 8×
  more expressed: the 3′ gene's counts can be the 5′ gene's transcription; see [[Readthrough spillover]]). A
  relation is a correlation across drugs and lines; it is never evidence that one gene regulates the other.
- **Where it sits** — its module and arm, its positions on the two maps, the length of its vector, and the {n_pred}
  drug-doses whose vectors **predict** the largest rise and fall of the gene (gene vector · drug-dose vector, in z
  units; † = the drug-dose carries an artifact flag) next to the **observed** z. Agreement means the gene follows the programme it shares with its partners; a
  gap means it departs from it for that drug.
- **What is on record** — the registries' own words (HGNC, Ensembl, UniProt, NCBI Gene), with accession links. When
  there is no record the note says so and claims nothing more.
- **Data** — the exact files and rows behind every number, and the link to the gene's **plates note**: its raw CPM
  and its corrected well effect (W2) in every well of every plate, as 8 × 12 grids (bold = DMSO wells).

## The vector space and the nodal map

- **Vector space** (`embed/`): each gene is a vector whose direction is its response pattern across all active,
  trustworthy (drug-dose, line) contexts. Two genes that respond oppositely point in opposite directions (cos near
  −1). Drug-doses live in the same space: the dot product of a gene vector and a drug-dose vector approximately
  reproduces the observed z (the part of it that the space's shared programmes explain).
- **Nodal map** (`graph/`, x and y): a 2D layout of 1 − |cos|. Opposite genes count as related, so the two arms of
  one pathway — the genes it switches on and the genes it switches off — land in **one island**. Islands are
  **modules**. A module has a **− arm** only when ≥ {arm_min} of its genes sit on the negative side of its main
  direction **and** the two sides anti-correlate (mean cos between them ≤ {arms_opp:+.1f}): then the + arm rises where
  the − arm falls. Otherwise it is **single-armed** (every gene +), and its notes say so with the measured mean cos
  between the sides (`graph/modules.parquet`). The **signed map** (xs, ys) uses 1 − cos and puts opposite genes far
  apart.
- A **module canvas** (Modules/…canvas) shows the module's genes at their nodal-map positions (green = + arm, red =
  − arm, in modules with two opposite arms) with the graph's edges (+ together, − opposite).

## Drug, line, plate and module notes

- **Drug** — doses (wells, significant genes, replicate agreement, cell loss, cell-cycle and proteasome module z,
  flags), the genes each dose raises and lowers, the modules it moves, the lines it depletes and the lines that
  respond most, and the nearest drugs in the vector space.
- **Cell line** — organ, TP53 status, drivers, the drug-doses that deplete it, how strongly it responds, the genes
  it moves most, the genes it has unusually high or lacks, and the programmes that do not respond in it.
- **Plate** — dose, reliability, plate factor, DMSO and failed wells, an 8 × 12 layout and a 96-row well table.
- **Module** — label from the validation stage, enrichment, the drugs that raise or lower it, the lines where it
  responds most, candidate new members, and every member by arm.

## Conventions

- Wikilinks are note names; drugs end in "(drug)", cell lines in "(line)".
- "Upstream" and "downstream" are regulatory words; chromosomal position is "5′ of" / "3′ of".
- A number in a note is read from the table named next to it, or is a simple function of it named with it (CPM =
  counts ÷ total × 10⁶, a predicted z = a dot product, a level ratio); nothing is re-estimated by the vault.
- The global graph view starts filtered: no indexes, Plate notes, plates notes or cell lines (every gene note links
  every line, so lines would pull all genes into one ball); change the filter in the graph settings to see them. Plates notes are excluded from search and the quick switcher (Settings → Files and links →
  Excluded files); open them from a gene note.
"""


LIT_HOWTO = """## What the literature says (AI-agent reviews)

A gene, drug or cell line tagged `#literature-review` has a section **What the literature says**, written by an AI
agent (tahoemap's literature-review agents, `tahoe review`; see `docs/review.md` of the tahoemap repository). The
agent read the entity's dossier (what this run's data say about it), searched PubMed, Europe PMC and the web, read
abstracts, and reported what is established, what in the data is unexpected, which expected connections are missing
and what is contradicted. The callout at the top of the section names the agent, the model, the date and the
verification: every cited PMID / DOI was looked up (a nonexistent one is removed and its claim marked unverified),
and a second agent, the citation checker, compared each claim with the abstracts it cites (supported / partly / not
supported / not checkable). It also links the run's full history (every request, response and tool call) and the
review as data; both are in the run folder (`review/`), outside the vault.

In a gene note the partner tables then have a **Literature** column: the agent's verdict on that pair (established,
indirect, plausible, unexpected or contradicted) with its citations, from `review/connections.parquet`; a verdict
from the partner's review is marked with the partner's name. The reviews are leads, not established facts: no person
has checked them. A new review replaces the section at the next `tahoe vault` (or `tahoe run`).
"""


def run(out, **_):
    """Build OUT/vault/ from the run's tables (see the module docstring)."""
    t0 = time.time()
    warnings.filterwarnings("ignore", category=RuntimeWarning)
    folder(out, "vault")
    log("Vault: building the Obsidian vault")
    with np.errstate(all="ignore"):
        info = Vault(out).build()
    info["minutes"] = round((time.time() - t0) / 60, 2)
    stamp_stage(out, "vault", VERSION, info)
    log(f"Vault done: {info['notes']:,} notes ({info['mb']} MB; gene notes median {info['gene_note_kb_median']} KB, "
        f"max {info['gene_note_kb_max']} KB; plates notes max {info['plates_note_kb_max']} KB), "
        f"{info['fragments_spliced']} written gene sections spliced ({info['fragments_available']} fragments), "
        + (f"{info['literature_notes']} literature reviews spliced ({info['literature_partner_cells']} partner-table "
           "verdicts), " if info.get("literature_notes") else "")
        + f"{info['stale_removed']} stale notes removed ({info['minutes']} min)")
    return info
