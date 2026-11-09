"""dossier - what one run's outputs say about one gene, drug or cell line, for a literature-review agent.

    entities(out, kinds=("gene", "drug", "line")) -> DataFrame
        kind, name, entity_id ('gene:<col>', 'drug:<name>', 'line:<cell_line_id>'), label, priority (higher first),
        then detail columns (col, in_space, n_sig_clean, n_novel, n_specific, n_repro, module, labelled).
        Lines first, then drugs (most significant genes first), then genes by
            100 x novel-candidate pairs + 3 x specific replicated partners (both halves, fdr <= 0.05, mutual rank
            <= 10) + 1 x replicated partners (both halves; at most 50) + 20 if its module has a set label (not just
            top genes) + 0.5 x significant clean pooled drug-doses (at most 100) + 10 if in the vector space + 2 if
            it has a calibrated single-line response (tables/drug_line_top).
        Genes with nothing to review are left out: noise-class RNAs, and genes that are neither in the vector space
        nor have a significant clean pooled drug-dose nor a calibrated single-line response (all_genes=True keeps
        them, at priority 0).
    build(out, kind, name) -> Dossier(kind, name, entity_id, text, data)
        text = markdown, at most MAX_CHARS characters (~8,000 tokens; list lengths shrink until it fits); data = the
        same facts as a JSON-serialisable dict. `name` is the entity's name (gene label or symbol, drug name, cell
        name or Cellosaurus id) or its entity_id.
    summary(out, kind, name) -> str
        the short version (at most SUMMARY_CHARS) that the tahoe_lookup tool returns; kind 'pair' with name 'A|B'
        gives the relation of two genes, with any probable-direction arrow between them (either way, every alert in
        full).
    Dossier.user_message() -> str
        the first user message of a review: one line of task + the dossier in <dossier> tags.

A gene dossier ends with its probable direction (the direction stage, read through direction_view, which the vault,
the map and the look-ups use too, so all of them show the same arrows in the same order and words): what probably
acts on the gene (upstream), the genes it probably acts on (downstream) and how it probably acts on the cells under
drug-doses, each capped by the cap rule (LIMITS['direction'], plus any of that many strongest without an alert beyond
them) with grade, sign words, evidence, the stage's numbers, q, the alerts' and the notes' short labels (notes:
reasons kept below their thresholds, no warning sign), then each label's reason in full once, and the caveats of the
kinds listed stated once above them; data['direction'] holds the same rows with every alert, note, caveat and support
in full and their edge ids. The reviewing agent
judges each arrow against the literature (agents/gene-reviewer.md, skills reading-tahoe-data and connection-audit);
its verdict is an ordinary connection verdict, so the review format is unchanged. An output without the stage gets
one sentence.

Built only from the run's own outputs (tables, relations, graph, direction, validation, reference, embed and a few
atlas matrices), read the way `query.py` reads them (filtered parquet reads, memory-mapped arrays; OUT/direction is
read whole once per process): one dossier stays around 1 GB and a few seconds at full scale (15,000 genes, 1,100
drug-doses, 100 partners per gene). Every stage except tables is optional; a missing one is named in the text. The
text holds no dates or paths, so its sha256 changes only when the data do.
"""

import hashlib
import json
import os
import re
import threading
from dataclasses import dataclass, field

import numpy as np
import pandas as pd

from .. import atlas_core as A
from .. import direction_view as DV
from .. import tlib as T
from .. import query as Q
from ..common import cap_keep, replace_file
from ..relations import REPRO_FDR

MAX_CHARS = 24_000             # ~7,000-8,000 tokens of markdown tables with numbers (~3-3.5 characters a token)
SUMMARY_CHARS = 4_000
KNOWN_STRING = 700             # "known" partners for the known-but-absent list: STRING combined score >= this ...
KNOWN_SET_MAX = 100            # ... or a shared Hallmark / Reactome set of <= this many genes
KNOWN_MAX = 30
DEPLETE_Z = Q.DEPLETE_Z
LFC_MIN = A.LFC_MIN
Q_CUT = A.Q_CUT
CELLOSAURUS_URL = "https://www.cellosaurus.org/{}"   # a line's entry; + ".txt" for the plain-text record

# list lengths at scale 1.0 (build shrinks them to fit MAX_CHARS)
LIMITS = {"drugs": 12, "single": 10, "partners": 25, "known": KNOWN_MAX, "novel": 10, "members": 6,
          "lines_hi": 5, "top_genes": 25, "top_genes_other": 10, "modules": 8, "deplete": 15, "beta": 6,
          "near_drugs": 10, "baseline_hi": 25, "baseline_lo": 15, "responses": 25, "components": 5, "targets": 12,
          "direction": 10, "dir_reasons": 20, "text": 600}
SHORT = {"drugs": 5, "single": 4, "partners": 8, "known": 6, "novel": 5, "members": 0, "lines_hi": 3,
         "top_genes": 10, "top_genes_other": 0, "modules": 4, "deplete": 6, "beta": 4, "near_drugs": 5,
         "baseline_hi": 10, "baseline_lo": 5, "responses": 8, "components": 3, "targets": 6, "direction": 4,
         "dir_reasons": 0, "text": 300}


@dataclass
class Dossier:
    kind: str
    name: str
    entity_id: str
    text: str
    data: dict = field(default_factory=dict)

    @property
    def sha256(self):
        return hashlib.sha256(self.text.encode("utf-8")).hexdigest()

    def user_message(self):
        """The first user message of a review (stable text: cacheable, and its hash identifies the data)."""
        what = {"line": "cell line"}.get(self.kind, self.kind)
        return (f"Review the {what} {self.name} ({self.entity_id}). The dossier below is everything this run of "
                f"the Tahoe-100M gene map says about it. Work as your instructions describe, and finish by calling "
                f"submit_review.\n\n<dossier entity_id=\"{self.entity_id}\">\n{self.text.rstrip()}\n</dossier>\n")


# ----------------------------------------------------------------------------- shared, cached access
class _Ctx:
    """One output folder: query.Out plus the indices the dossiers need, built once per process (thread-safe)."""

    def __init__(self, out):
        self.out = out
        self.o = Q.Out(out)
        self._lock = threading.Lock()
        self._locks = {}
        self._c = {}

    def get(self, key, fn):
        if key in self._c:
            return self._c[key]
        with self._lock:
            lk = self._locks.setdefault(key, threading.Lock())
        with lk:
            if key not in self._c:
                self._c[key] = fn()
        return self._c[key]

    # --- small helpers over query.Out
    def has(self, rel):
        return self.o.has(rel)

    def genes(self):
        return self.get("genes", self.o.genes)

    def ann(self):
        """reference/annotations.parquet indexed by col (all the columns a dossier shows), or None."""
        def load():
            if not self.has("reference/annotations.parquet"):
                return None
            import pyarrow.parquet as pq
            p = self.o.p("reference", "annotations.parquet")
            have = set(pq.ParquetFile(p).schema_arrow.names)
            want = ["col", "symbol", "hgnc_id", "name", "locus_type", "location", "chrom", "start", "end", "strand",
                    "biotype", "aliases", "prev_symbols", "gene_groups", "entrez_id", "uniprot", "protein_name",
                    "function", "ncbi_summary", "matched_by"]
            return pd.read_parquet(p, columns=[c for c in want if c in have]).set_index("col", drop=False)
        return self.get("ann", load)

    def lines(self):
        return self.get("lines", self.o.lines)

    def dd(self):
        return self.get("dd", self.o.drugdoses)

    def nodes(self):
        return self.get("nodes", self.o.nodes)

    def modules(self):
        return self.get("modules", self.o.modules)

    def ref_ok(self):
        """The reference sources that loaded (status cached / downloaded in reference/sources.json); None when the
        file is missing (an older run: assume what is on disk loaded)."""
        def load():
            p = self.o.p("reference", "sources.json")
            try:
                with open(p, encoding="utf-8") as fh:
                    st = {k: (v or {}).get("status", "") for k, v in json.load(fh).get("sources", {}).items()}
            except (OSError, ValueError):
                return None
            return {k for k, v in st.items() if v in ("cached", "downloaded")}
        return self.get("ref_ok", load)

    def loaded(self, *sources):
        """True when any of these reference sources loaded (or the run does not say)."""
        ok = self.ref_ok()
        return ok is None or any(x in ok for x in sources)

    def in_space(self):
        """bool over gene cols: in the vector space (embed/genes.parquet included)."""
        def load():
            g = self.genes()
            m = np.zeros(int(g["col"].max()) + 1 if len(g) else 0, dtype=bool)
            if self.has("embed/genes.parquet"):
                e = pd.read_parquet(self.o.p("embed", "genes.parquet"), columns=["col", "included"])
                m[e["col"].to_numpy()[e["included"].to_numpy().astype(bool)]] = True
            return m
        return self.get("in_space", load)

    def unit(self):
        return self.o.npy("embed/gene_unit.npy") if self.has("embed/gene_unit.npy") else None

    def moa(self):
        """drug -> (moa_fine, targets) from the drug-dose table."""
        def load():
            d = self.dd().drop_duplicates("drug")
            return {r["drug"]: (Q._text(r.get("moa_fine")), Q._text(r.get("targets"))) for _, r in d.iterrows()}
        return self.get("moa", load)

    def sym_index(self):
        def load():
            d = {}
            g = self.genes()
            for c, s in zip(g["col"].to_numpy(), g["symbol"].str.upper().to_numpy()):
                d.setdefault(s, []).append(int(c))
            return d
        return self.get("sym_index", load)

    def string_known(self):
        """(cols sorted, partner, score) arrays of STRING pairs >= KNOWN_STRING in both directions, for slicing."""
        def load():
            if not self.has("reference/string_pairs.parquet"):
                return None
            s = pd.read_parquet(self.o.p("reference", "string_pairs.parquet"), filters=[("score", ">=", KNOWN_STRING)])
            a = np.concatenate([s["col_a"].to_numpy(), s["col_b"].to_numpy()]).astype(np.int64)
            b = np.concatenate([s["col_b"].to_numpy(), s["col_a"].to_numpy()]).astype(np.int64)
            sc = np.concatenate([s["score"].to_numpy(), s["score"].to_numpy()]).astype(np.int32)
            o = np.argsort(a, kind="stable")
            return a[o], b[o], sc[o]
        return self.get("string_known", load)

    def small_sets(self):
        """(col -> list of (set label, source, size)), (set key -> member cols) for Hallmark / Reactome sets of
        <= KNOWN_SET_MAX genes."""
        def load():
            if not self.has("reference/gene_sets.parquet"):
                return None
            s = pd.read_parquet(self.o.p("reference", "gene_sets.parquet"))
            s = s[s["source"].isin(["hallmark", "reactome"]) & (s["set_size"] <= KNOWN_SET_MAX)]
            members, by_col = {}, {}
            for (src, st), x in s.groupby(["source", "set"], sort=False):
                key = (src, st)
                members[key] = x["col"].to_numpy().astype(np.int64)
                size = int(x["set_size"].iloc[0])
                for c in members[key]:
                    by_col.setdefault(int(c), []).append((key, size))
            return by_col, members
        return self.get("small_sets", load)

    def labels(self):
        return self.get("labels", self.o.labels)

    def enrichment(self):
        def load():
            p = self.o.p("validation", "module_enrichment.csv")
            return pd.read_csv(p) if os.path.exists(p) else None
        return self.get("enrichment", load)

    def novel_members(self):
        def load():
            p = self.o.p("validation", "novel_members.csv")
            return pd.read_csv(p) if os.path.exists(p) else None
        return self.get("novel_members", load)


_CTX = {}
_CTX_LOCK = threading.Lock()


def context(out):
    """The cached _Ctx of an output folder (one per process)."""
    key = os.path.realpath(out)
    with _CTX_LOCK:
        if key not in _CTX:
            _CTX[key] = _Ctx(out)
        return _CTX[key]


def clear_cache():
    with _CTX_LOCK:
        _CTX.clear()


# ----------------------------------------------------------------------------- formatting
_num, _text, _fold, _z, _q, _cos = Q._num, Q._text, Q._fold, Q._z, Q._q, Q._cos


def _cut(s, n):
    s = _text(s)
    return s if len(s) <= n else s[:max(0, n - 3)].rstrip() + "..."


def _md(head, rows):
    def esc(v):
        return str(v).replace("|", "/").replace("\n", " ").strip()
    out = ["| " + " | ".join(head) + " |", "|" + "|".join("---" for _ in head) + "|"]
    out += ["| " + " | ".join(esc(v) or " " for v in r) + " |" for r in rows]
    return out


def _f(x, fmt="{:.2f}"):
    x = _num(x)
    return None if not np.isfinite(x) else float(fmt.format(x))


def _jsonable(v):
    if isinstance(v, (np.integer,)):
        return int(v)
    if isinstance(v, (np.floating,)):
        v = float(v)
    if isinstance(v, float):
        return v if np.isfinite(v) else None
    if isinstance(v, (np.bool_,)):
        return bool(v)
    if isinstance(v, dict):
        return {str(k): _jsonable(x) for k, x in v.items()}
    if isinstance(v, (list, tuple)):
        return [_jsonable(x) for x in v]
    if v is pd.NA or v is pd.NaT:
        return None
    return v


def _artifacts(flags):
    return Q._artifacts(flags)


def _caveats(flags):
    fl = [f for f in str(flags or "").split("; ") if f]
    return "; ".join(f for f in fl if f not in A.ARTIFACT_FLAGS)


def _moa_text(C, drug):
    m, t = C.moa().get(drug, ("", ""))
    m = "" if m in ("unclear", "") else m
    if m:
        return m + (f" ({t})" if t else "")
    return f"targets {t}" if t else ""


def _sb(drug):
    return T.salt_base(_text(drug))


def _line_cut(C):
    t, ch, cal = C.o.line_cut()
    return t, (f"calibrated on this run: ~{ch:.2g} chance calls per gene and line" if cal and ch is not None else
               ("calibrated on this run" if cal else "NOT calibrated in this run"))


def _tp53(C, line_name):
    """'wt' / 'altered' / '' for a cell name (tables/lines.parquet tp53_status)."""
    def load():
        ln = C.lines()
        if "tp53_status" not in ln:
            return {}
        return {n: {"wild type": "wt", "altered": "altered"}.get(_text(t), "")
                for n, t in zip(ln["name"].astype(str), ln["tp53_status"])}
    return C.get("tp53", load).get(str(line_name), "")


def _gene_name(C, c):
    a = C.ann()
    if a is None or c not in a.index or "name" not in a:
        return ""
    return _text(a.at[c, "name"])


def _function(txt):
    """The UniProt FUNCTION text without isoform tags and infection notes ('[Isoform 2]: ...', '(Microbial
    infection) ...')."""
    parts = [Q._TAG.sub("", p).strip() for p in re.split(r";\s*(?=\[[^\]]{1,80}\]:)", _text(txt))]
    parts = [p for p in parts if p and not p.startswith("(Microbial infection)")]
    return " ".join(parts)


def _label(C, c):
    g = C.genes()
    return g.at[c, "label"] if c in g.index else str(c)


def _module_txt(C, c):
    """'12+' / '12-' (module and arm; the arm only in a module whose arms are opposite), '0', or '' (not placed)."""
    def load():
        nd, mods = C.nodes(), C.modules()
        if nd is None:
            return {}
        opp = {}
        if mods is not None and "arms_opposite" in mods:
            opp = dict(zip(mods["module"].astype(int), mods["arms_opposite"].fillna(False).astype(bool)))
        elif mods is not None:
            opp = dict(zip(mods["module"].astype(int), mods["n_minus"].fillna(0).astype(int) > 0))
        out = {}
        for cc, m, a in zip(nd["col"].astype(int), nd["module"].astype(int), nd["arm"].fillna("").astype(str)):
            out[cc] = "0" if m == 0 else f"{m}{a if opp.get(m, False) else ''}"
        return out
    return C.get("module_txt", load).get(int(c), "")


# ----------------------------------------------------------------------------- name resolution
def resolve(out, kind, name):
    """(name, entity_id, key) for a kind and a name or entity_id; key = gene col, drug name or line index.
    Raises query.NotFound (with suggestions) for unknown names."""
    C = context(out)
    name = str(name).strip()
    if ":" in name and name.split(":", 1)[0] in ("gene", "drug", "line"):
        k2, rest = name.split(":", 1)
        if k2 != kind:
            raise Q.NotFound(f"{name} is a {k2}, not a {kind}")
        if kind == "gene" and rest.strip().isdigit():
            c = int(rest)
            if c not in C.genes().index:
                raise Q.NotFound(f"No gene col {c} in this run")
            return C.genes().at[c, "label"], f"gene:{c}", c
        if kind == "line":
            ln = C.lines()
            hit = ln.index[ln["cell_line_id"].astype(str) == rest.strip()]
            if len(hit):
                i = int(hit[0])
                return ln.at[i, "name"], f"line:{ln.at[i, 'cell_line_id']}", i
        name = rest.strip()
    if kind == "gene":
        cols, _how = Q.resolve_gene(C.o, name)
        c = int(cols[0])
        return C.genes().at[c, "label"], f"gene:{c}", c
    if kind == "drug":
        drugs = Q.resolve_drug(C.o, name)
        exact = [d for d in drugs if d == name]
        d = exact[0] if exact else drugs[0]
        return d, f"drug:{d}", d
    if kind == "line":
        i = Q.resolve_line(C.o, name)
        ln = C.lines()
        return ln.at[i, "name"], f"line:{ln.at[i, 'cell_line_id']}", i
    raise ValueError(f"kind must be gene, drug or line, not {kind!r}")


# ----------------------------------------------------------------------------- entities
def entities(out, kinds=("gene", "drug", "line"), all_genes=False):
    """The entities to review, highest priority first (see the module docstring for the order)."""
    if isinstance(kinds, str):
        kinds = [k.strip() for k in kinds.split(",") if k.strip()]
    bad = [k for k in kinds if k not in ("gene", "drug", "line")]
    if bad:
        raise ValueError(f"unknown kinds {bad}: use gene, drug, line")
    C = context(out)
    C.o.require("effects", "tables")
    rows = []
    if "line" in kinds:
        ln = C.lines()
        for i, r in ln.iterrows():
            nd = _num(r.get("n_dd_depleted"))
            rows.append({"kind": "line", "name": r["name"], "entity_id": f"line:{r['cell_line_id']}",
                         "label": f"{r['name']} ({_text(r.get('Organ')) or 'organ unknown'})",
                         "priority": 3_000_000.0 + (nd if np.isfinite(nd) and nd > 0 else 0.0)})
    if "drug" in kinds:
        if C.has("tables/drugs.parquet"):
            dr = C.o.pq("tables/drugs.parquet")
            for _, r in dr.iterrows():
                ms = _num(r.get("max_sig"))
                m = _text(r.get("moa_fine"))
                rows.append({"kind": "drug", "name": r["drug"], "entity_id": f"drug:{r['drug']}",
                             "label": r["drug"] + (f" ({m})" if m and m != "unclear" else ""),
                             "priority": 2_000_000.0 + (min(ms, 999_999) if np.isfinite(ms) else 0.0)})
    if "gene" in kinds:
        rows += _gene_entities(C, all_genes)
    df = pd.DataFrame(rows)
    if not len(df):
        return pd.DataFrame(columns=["kind", "name", "entity_id", "label", "priority"])
    lead = ["kind", "name", "entity_id", "label", "priority"]
    df = df[lead + [c for c in df.columns if c not in lead]]
    order = {"line": 0, "drug": 1, "gene": 2}
    df["_k"] = df["kind"].map(order)
    df = df.sort_values(["priority", "_k", "name"], ascending=[False, True, True], kind="stable")
    df = df.drop(columns="_k").reset_index(drop=True)
    for c in ("col", "n_sig_clean", "n_novel", "n_specific", "n_repro", "module"):
        if c in df:
            df[c] = df[c].astype("Int64")
    for c in ("in_space", "labelled"):
        if c in df:
            df[c] = df[c].astype("boolean")
    return df


def _gene_entities(C, all_genes):
    g = C.genes()
    gK = len(g)
    cols = g["col"].to_numpy().astype(np.int64)
    n_sig = (g["n_dd_up_clean"].fillna(0).to_numpy() + g["n_dd_down_clean"].fillna(0).to_numpy()) \
        if "n_dd_up_clean" in g else np.zeros(gK)
    noise = g["noise_rna"].to_numpy().astype(bool) if "noise_rna" in g else np.zeros(gK, dtype=bool)
    space = C.in_space()
    in_space = np.array([c < len(space) and bool(space[c]) for c in cols])
    single = np.zeros(gK, dtype=bool)
    if C.has("tables/drug_line_top.parquet"):          # a calibrated single-line cell at a clean drug-dose (the
        t = C.o.pq("tables/drug_line_top.parquet", columns=["col", "clean"])    # table also ranks flagged ones)
        if "clean" in t:
            t = t[t["clean"].astype(bool)]
        single[np.isin(cols, t["col"].unique())] = True
    n_novel = np.zeros(gK)
    n_spec = np.zeros(gK)
    n_rep = np.zeros(gK)
    if C.has("relations/gene_relations.parquet"):
        import pyarrow.parquet as pq
        have = set(pq.ParquetFile(C.o.p("relations", "gene_relations.parquet")).schema_arrow.names)
        want = [c for c in ("col_a", "evidence", "fdr", "mutual_rank", "novel_candidate") if c in have]
        r = pd.read_parquet(C.o.p("relations", "gene_relations.parquet"), columns=want)
        both = (r["evidence"] == "both halves").to_numpy()
        ca = r["col_a"].to_numpy().astype(np.int64)
        pos = {int(c): i for i, c in enumerate(cols)}
        idx = np.array([pos.get(int(c), -1) for c in np.unique(ca)])
        uc = np.unique(ca)

        def per(mask):
            v = np.bincount(ca[mask], minlength=int(cols.max()) + 1 if len(cols) else 0)
            out = np.zeros(gK)
            ok = idx >= 0
            out[idx[ok]] = v[uc[ok]]
            return out
        n_rep = per(both)
        if "fdr" in r and "mutual_rank" in r:
            n_spec = per(both & (r["fdr"].fillna(1.0).to_numpy() <= 0.05) &
                         (r["mutual_rank"].fillna(np.inf).to_numpy() <= 10))
        if "novel_candidate" in r and C.o.novelty()[0]:
            n_novel = per(r["novel_candidate"].fillna(False).to_numpy().astype(bool))
    labelled = np.zeros(gK, dtype=bool)
    module = np.zeros(gK, dtype=np.int64)
    nd = C.nodes()
    if nd is not None:
        mod = dict(zip(nd["col"].to_numpy().astype(np.int64), nd["module"].to_numpy().astype(np.int64)))
        module = np.array([mod.get(int(c), 0) for c in cols])
        lab = C.labels()
        if lab is not None and "label_source" in lab:
            good = set(int(m) for m, s in zip(lab["module"], lab["label_source"].fillna("").astype(str))
                       if s and s != "top genes")
            labelled = np.array([m > 0 and int(m) in good for m in module])
    pr = 100.0 * n_novel + 3.0 * n_spec + np.minimum(n_rep, 50) + 20.0 * labelled + \
        0.5 * np.minimum(n_sig, 100) + 10.0 * in_space + 2.0 * single
    keep = all_genes | (~noise & (in_space | (n_sig > 0) | single))
    if all_genes:
        pr = np.where(~noise & (in_space | (n_sig > 0) | single), pr, 0.0)
    rows = []
    for i in np.flatnonzero(keep):
        c = int(cols[i])
        rows.append({"kind": "gene", "name": g.at[c, "label"], "entity_id": f"gene:{c}", "label": g.at[c, "label"],
                     "priority": float(pr[i]), "col": c, "in_space": bool(in_space[i]), "n_sig_clean": int(n_sig[i]),
                     "n_novel": int(n_novel[i]), "n_specific": int(n_spec[i]), "n_repro": int(n_rep[i]),
                     "module": int(module[i]), "labelled": bool(labelled[i])})
    return rows


# ----------------------------------------------------------------------------- build
def build(out, kind, name, max_chars=MAX_CHARS):
    """The dossier of one entity: markdown text <= max_chars + the same facts as a dict."""
    C = context(out)
    C.o.require("effects", "tables")
    nm, eid, key = resolve(out, kind, name)
    fn = {"gene": _gene, "drug": _drug, "line": _line}[kind]
    text, data = "", {}
    for scale in (1.0, 0.75, 0.55, 0.4, 0.3, 0.2, 0.1):
        lim = {k: (max(1, int(round(v * scale))) if v else 0) for k, v in LIMITS.items()}
        lim["text"] = max(200, int(LIMITS["text"] * max(scale, 0.5)))
        P, data = fn(C, key, lim, short=False)
        text = "\n".join(P).rstrip() + "\n"
        if len(text) <= max_chars:
            break
    if len(text) > max_chars:                      # a hard stop (should not happen with the limits above)
        text = text[:max_chars - 80].rsplit("\n", 1)[0] + "\n\n[dossier truncated to its size bound]\n"
    data = _jsonable(data)
    data.update({"kind": kind, "name": nm, "entity_id": eid})
    return Dossier(kind=kind, name=nm, entity_id=eid, text=text, data=data)


def summary(out, kind, name, max_chars=SUMMARY_CHARS):
    """The short dossier (tahoe_lookup). kind 'pair': name 'GENE_A|GENE_B' (also ',' or ' vs ')."""
    C = context(out)
    C.o.require("effects", "tables")
    if kind == "pair":
        text = _pair(C, name)
    else:
        try:
            nm, eid, key = resolve(out, kind, name)
        except Q.NotFound:
            alt = _unmeasured_source(C, name) if kind == "gene" else None
            if not alt:                              # (a source that is no gene of this run: its arrows, as the CLI)
                raise
            return alt if len(alt) <= max_chars else \
                alt[:max_chars - 60].rsplit("\n", 1)[0] + "\n[summary truncated]\n"
        fn = {"gene": _gene, "drug": _drug, "line": _line}[kind]
        for scale in (1.0, 0.75, 0.5, 0.35, 0.25):        # shorter lists until it fits, as build does
            lim = {k: (max(1, int(round(v * scale))) if v else 0) for k, v in SHORT.items()}
            lim["text"] = max(150, int(SHORT["text"] * max(scale, 0.5)))
            P, _ = fn(C, key, lim, short=True)
            text = "\n".join(P).rstrip() + "\n"
            if len(text) <= max_chars:
                break
    if len(text) > max_chars:
        text = text[:max_chars - 60].rsplit("\n", 1)[0] + "\n[summary truncated]\n"
    return text


# ----------------------------------------------------------------------------- gene
def _gene(C, c, lim, short=False):
    o = C.o
    g = C.genes()
    gr = g.loc[c]
    lab, sym = gr["label"], _text(gr["symbol"])
    D = {"col": int(c), "label": lab, "symbol": sym}
    P = [f"# {'Summary' if short else 'Dossier'}: gene {lab}", f"entity_id gene:{c}"]
    space = C.in_space()
    in_space = c < len(space) and bool(space[c])
    why = "" if in_space else Q._not_in_space(o, c)

    # identity
    ann = C.ann()
    if ann is not None and not C.loaded("hgnc", "uniprot", "ncbi"):
        ann = None                                 # the reference stage ran offline: its table holds no annotation
    ident = {}
    P += ["", "## Identity"]
    if ann is not None and c in ann.index:
        a = ann.loc[c]
        nm = _text(a.get("name"))
        loc = _text(a.get("location"))
        ch, st, en = _text(a.get("chrom")), _num(a.get("start")), _num(a.get("end"))
        coords = f"chr{ch}:{int(st):,}-{int(en):,} ({_text(a.get('strand')) or '?'} strand)" \
            if ch and np.isfinite(st) and np.isfinite(en) else ""
        bt = _text(a.get("locus_type")) or _text(a.get("biotype"))
        hg = _text(a.get("hgnc_id"))
        mb = _text(a.get("matched_by"))
        bits = [f"**{sym}**" + (f" - {nm}" if nm else "")]
        bits += [x for x in (hg + (" (matched by alias only: tentative)" if mb == "alias_symbol" else ""),
                             loc, coords, bt) if x]
        P.append("- " + " · ".join(bits))
        al = _text(a.get("aliases")).replace("|", ", ")
        pv = _text(a.get("prev_symbols")).replace("|", ", ")
        P.append(f"- Aliases (search with these too): {al or '-'} · previous symbols: {pv or '-'}")
        ids = [f"Ensembl {_text(gr.get('ensembl_id'))}" if _text(gr.get("ensembl_id")) else ""]
        ez = _num(a.get("entrez_id"))
        ids += [f"Entrez {int(ez)}" if np.isfinite(ez) else "", f"UniProt {_text(a.get('uniprot'))}"
                if _text(a.get("uniprot")) else ""]
        if any(ids):
            P.append("- Ids: " + " · ".join(x for x in ids if x))
        gg = _text(a.get("gene_groups")).replace("|", "; ")
        if gg and not short:
            P.append(f"- HGNC gene groups: {gg}")
        fn_ = _function(a.get("function"))
        pn = _text(a.get("protein_name"))
        if fn_:
            P.append(f"- Function (UniProt{', ' + pn if pn else ''}): {_cut(fn_, lim['text'])}")
        ns = _text(a.get("ncbi_summary"))
        if ns and (not fn_ or not short):
            P.append(f"- NCBI summary: {_cut(ns, lim['text'] // (2 if fn_ else 1))}")
        if not hg:
            P.append("- No HGNC record for this gene (matched by: " + (mb or "none") + "): it may be an Ensembl-only "
                     "id, a readthrough or novel transcript, or a synthetic test gene; literature under this symbol "
                     "may not exist.")
        ident = {"symbol": sym, "name": nm, "hgnc_id": hg, "location": loc, "coords": coords, "locus_type": bt,
                 "aliases": al, "prev_symbols": pv, "ensembl_id": _text(gr.get("ensembl_id")),
                 "entrez_id": int(ez) if np.isfinite(ez) else None, "uniprot": _text(a.get("uniprot")),
                 "function": _cut(fn_, 1200), "ncbi_summary": _cut(ns, 800), "matched_by": mb}
    else:
        P.append(f"- **{sym}** · Ensembl {_text(gr.get('ensembl_id')) or '-'}")
        P.append("- Reference annotations (HGNC, UniProt, NCBI, STRING, pathways) were not loaded for this run "
                 "(offline or failed): no name, aliases or function here, and the known / novel flags below are "
                 "unavailable. Search the literature by the symbol." if ann is None else
                 "- Not in the reference annotation table.")
        ident = {"symbol": sym, "ensembl_id": _text(gr.get("ensembl_id"))}
    D["identity"] = ident

    # expression
    nl = len(C.lines())
    P += ["", "## Expression in Tahoe"]
    P.append(f"- Level: {Q._f(gr.get('pooled_cpm'), '{:,.1f}')} CPM pooled over all wells and lines; "
             f"{Q._f(gr.get('median_line_cpm'), '{:,.1f}')} CPM in the median line; measured (truly expressed, not "
             f"ambient RNA) in {Q._int(gr.get('n_lines_expressing'))} of {nl} lines.")
    le = o.pq("tables/line_effects.parquet", columns=["col", "line", "cell_name", "cell_line_id", "baseline_cpm",
                                                      "expressed", "n_dd_up", "n_dd_down", "best_up_drug",
                                                      "best_up_dose", "best_up_lfc", "best_up_z", "best_down_drug",
                                                      "best_down_dose", "best_down_lfc", "best_down_z"],
              filters=[("col", "==", int(c))])
    le = le.assign(nm=le["cell_name"].fillna(le["cell_line_id"]).astype(str))
    expd = le[le["expressed"].astype(bool)].sort_values("baseline_cpm", ascending=False)
    nexp = le[~le["expressed"].astype(bool)]
    if len(expd):
        k = lim["lines_hi"]
        hi = ", ".join(f"{r['nm']} {r['baseline_cpm']:,.0f}" for _, r in expd.head(k).iterrows())
        lo = ", ".join(f"{r['nm']} {r['baseline_cpm']:,.0f}" for _, r in expd.tail(min(k, max(0, len(expd) - k)))
                       .iloc[::-1].iterrows())
        P.append(f"- Baseline CPM, highest: {hi}" + (f" · lowest measured: {lo}" if lo else ""))
    if len(nexp):
        P.append("- Not measured (not expressed, or only ambient RNA; no per-line values): "
                 + _cut(", ".join(nexp["nm"]), 400))
    for k, nm_ in (("corr_with_S", "S-phase"), ("corr_with_G2M", "G2/M")):
        r = _num(gr.get(k))
        if np.isfinite(r) and abs(r) >= 0.4:
            P.append(f"- Tracks the {nm_} programme across drug wells (r = {r:+.2f}): drugs that change the share of "
                     "cycling cells move it, whatever their target.")
    if bool(gr.get("noise_rna", False)):
        P.append("- Noise-class RNA (snoRNA / mitochondrial / pseudogene / replication histone ...): its responses "
                 "need care.")
    D["expression"] = {"pooled_cpm": _f(gr.get("pooled_cpm")), "median_line_cpm": _f(gr.get("median_line_cpm")),
                       "n_lines_expressing": int(_num(gr.get("n_lines_expressing")))
                       if np.isfinite(_num(gr.get("n_lines_expressing"))) else None, "n_lines": nl,
                       "not_measured": nexp["nm"].tolist(), "corr_with_S": _f(gr.get("corr_with_S")),
                       "corr_with_G2M": _f(gr.get("corr_with_G2M")), "noise_rna": bool(gr.get("noise_rna", False))}

    # map
    P += ["", "## Place in the vector space and the nodal map"]
    D["map"] = {"in_space": in_space}
    if not o.ran("embed"):
        P.append("- The embed stage has not run: no vector space, partners, module or arm.")
    elif not in_space:
        P.append(f"- Not in the vector space: {why}. So it has no data partners, module or arm.")
        D["map"]["why_not"] = why
    else:
        fo = int(c) in o.flagged_only()
        D["map"]["evidence_flagged_only"] = fo
        P.append("- In the vector space." + (
            f" {Q.ALERT} Only through drug-doses that carry an alert (an artifact flag for this gene at every "
            "significant pooled drug-dose and per-line response; embed evidence_flagged_only): its vector, partners "
            "and module may reflect the artifact." if fo
            else ""))
        nd = C.nodes()
        if nd is not None and c in nd.index:
            m, arm = Q._module_arm(o, c)
            D["map"].update({"module": m, "arm": arm})
            if m and m > 0:
                mods = C.modules()
                mr = mods[mods["module"] == m].iloc[0] if mods is not None and (mods["module"] == m).any() else None
                opp, bcos = o.module_arms(m)
                lb = o.module_label(m, set_only=True)
                txt = f"- Module {m}" + (f", arm {arm}" if opp else "")
                if mr is not None:
                    txt += (f" ({int(mr['n_genes'])} genes: {int(mr['n_plus'])} on +, {int(mr['n_minus'])} on -)"
                            if opp else f" ({int(mr['n_genes'])} genes, single-armed)")
                txt += f"; label: {lb}" if lb else "; no enriched gene set (labelled by its top genes)"
                P.append(txt + ".")
                if opp:
                    P.append(f"- Its two arms move in opposite directions under the same drugs (mean cos between "
                             f"arms {_cos(bcos)}).")
                enr = _module_sets(C, m, arm if opp else "", 3)
                if enr:
                    P.append("- Enriched sets (validation): " + "; ".join(enr))
                if mr is not None:
                    same = Q._arm_names(o, mr["top_plus" if arm != "-" else "top_minus"], 8, sym)
                    other = Q._arm_names(o, mr["top_minus" if arm != "-" else "top_plus"], 8)
                    note = f" ({Q.ALERT} = in the vector space only through drug-doses with an artifact flag)" \
                        if any(Q.ALERT in x for x in same + (other if opp else [])) else ""
                    if same:
                        P.append(("- Its arm's top genes: " if opp else "- Module's top genes: ")
                                 + ", ".join(same) + (note if not (other and opp) else ""))
                    if other and opp:
                        P.append("- Opposite arm's top genes: " + ", ".join(other) + note)
                    D["map"].update({"label": lb, "arms_opposite": bool(opp), "n_genes": int(mr["n_genes"]),
                                     "enriched_sets": enr})
            else:
                P.append("- Not in any module (module 0: too few strong neighbours to join one).")

    # drug responses
    _gene_drugs(C, c, lim, short, P, D)

    # partners
    rel = None
    if o.ran("relations") and in_space:
        cols = ["col_b", "symbol_b", "rank", "cos", "cos_half1", "cos_half2", "fdr", "evidence", "z_gene",
                "mutual_rank", "specificity", "locus", "readthrough_risk", "distance_bp", "same_strand",
                "shared_gene_group", "shared_pathway", "string_score", "known", "novel_candidate", "alert"]
        rel = o.pq("relations/gene_relations.parquet", columns=["col_a"] + cols, filters=[("col_a", "==", int(c))])
    _gene_partners(C, c, rel, in_space, why, lim, short, P, D)
    if not short:
        _gene_known_absent(C, c, rel, in_space, lim, P, D)
    _gene_novel(C, c, rel, lim, short, P, D)
    _gene_direction(C, c, lim, short, P, D)
    return P, D


def _module_sets(C, m, arm, k):
    e = C.enrichment()
    if e is None or not len(e):
        return []
    x = e[(e["module"] == m)]
    if arm and "arm" in x:
        x = x[x["arm"].astype(str).isin([arm, "all"])]
    x = x.sort_values("q").drop_duplicates("set_label").head(k)
    return [f"{_cut(r['set_label'], 60)} ({_text(r['source'])}; {int(r['overlap'])}/{int(r['n_set'])} genes, "
            f"q {_q(r['q'])})" for _, r in x.iterrows()]


def _row_alert(flags, clean, cc_share=None):
    """The alert of a drug_effects / drug_line_top row in plain words ('' = none): its artifact flags for this gene,
    the cell-cycle shift with the share of the change it would explain (tables cc_share). A row the tables stage did
    not call clean always gets one."""
    if clean:
        return ""
    return Q._alert(flags, cc_share, "table") or "artifact flag"


def _gene_drugs(C, c, lim, short, P, D):
    """The gene's drug-doses: one ranked list per direction over every drug-dose, flagged ones kept in their ranked
    place with an alert (ALERT + the reason), capped at lim['drugs'] plus any of the lim['drugs'] strongest without
    an alert beyond them; then its strongest single-line cells, the same way."""
    o = C.o
    g = C.genes()
    gr = g.loc[c]
    cols = ["dd", "drug", "dose", "lfc", "fold", "z", "q_up", "q_down", "flags", "clean", "cc_share",
            "n_lines_measured", "n_lines_up", "n_lines_down", "pattern_up", "pattern_down"]
    de = o.pq("tables/drug_effects.parquet", columns=cols, filters=[("col", "==", int(c))])
    de["flags"] = de["flags"].fillna("").astype(str)
    de["clean"] = de["clean"].astype(bool)
    cc = de["cc_share"] if "cc_share" in de else pd.Series(np.nan, index=de.index)
    de["alert"] = [_row_alert(f, cl, s) for f, cl, s in zip(de["flags"], de["clean"], cc)]
    P += ["", "## Drug responses, pooled over the cell lines (median of the measured lines)"]
    nu, nd_ = int(_num(gr.get("n_dd_up_clean")) or 0), int(_num(gr.get("n_dd_down_clean")) or 0)
    nua, nda = int(_num(gr.get("n_dd_up")) or 0), int(_num(gr.get("n_dd_down")) or 0)
    P.append(f"- Significant (q < {Q_CUT:g} and fold >= 1.2x or <= 1/1.2x) drug-doses: {nua} raise it, {nda} lower "
             f"it; of them without an alert (no artifact flag for this gene): {nu} raise it, {nd_} lower it. "
             "Fold changes are against the same line's median drug well on the plate (not DMSO), at 24 h.")
    P.append(f"- {Q.ALERT} = an artifact flag for this gene (toxic, transcription drop, cell-cycle shift, unreliable "
             "plate only, position not correctable / correction uncertain, wells disagree): the change may be the "
             "artifact. Such a drug-dose keeps its ranked place; weigh it, do not drop it. 'cell-cycle shift, "
             "explains ~N%' = the share of this gene's change the drug-dose's cell-cycle shift would explain, from "
             "the gene's own slopes on the S-phase and G2/M programmes; a shift that is not the explanation is no "
             "alert (it reads 'cell-cycle shift (explains ~N% here)' among the caveats).")
    ti = C.o._info("tables/info.json")
    cu, cd = _num(ti.get("lines_up_chance_rate")), _num(ti.get("lines_down_chance_rate"))
    if not short and np.isfinite(cu) and np.isfinite(cd):
        P.append(f"- 'Lines moved' = lines with per-line z >= 2 and >= 1.2x (descriptive): a line with no effect "
                 f"passes by chance {100 * cu:.1f}% of the time upwards and {100 * cd:.1f}% downwards in this run.")
    D["drugs"] = {"n_up": nua, "n_down": nda, "n_up_clean": nu, "n_down_clean": nd_,
                  "lines_up_chance_rate": _f(cu, "{:.4f}"), "lines_down_chance_rate": _f(cd, "{:.4f}"),
                  "n_flagged": int((de["alert"] != "").sum())}
    for sign, word, key in ((1, "Raised by", "up"), (-1, "Lowered by", "down")):
        sub = de[np.sign(de["z"]) == sign].sort_values("z", ascending=(sign < 0), kind="stable")
        qc = "q_up" if sign > 0 else "q_down"
        k = lim["drugs"]
        ok = (sub["alert"] == "").to_numpy()
        pos = Q._capped(len(sub), k, ok)
        shown = sub.iloc[pos]
        sig = (shown[qc] < Q_CUT) & (sign * shown["lfc"] >= LFC_MIN)
        recs = []
        for (_, r), s, rank in zip(shown.iterrows(), sig, pos + 1):
            nl_ = r["n_lines_up"] if sign > 0 else r["n_lines_down"]
            recs.append({"rank": int(rank), "drug": r["drug"], "dose": r["dose"], "fold": _f(r["fold"], "{:.3f}"),
                         "z": _f(r["z"]), "q": _f(r[qc], "{:.3g}"), "significant": bool(s), "lines": int(nl_),
                         "lines_measured": int(r["n_lines_measured"]),
                         "pattern": _text(r["pattern_up" if sign > 0 else "pattern_down"]),
                         "moa": _moa_text(C, r["drug"]), "alert": r["alert"], "caveats": _caveats(r["flags"])})
        D["drugs"][key] = recs
        D["drugs"]["n_" + key + "_listed"] = int(len(sub))
        D["drugs"]["n_" + key + "_alert"] = int((~ok).sum())
        if short:
            if recs:
                P.append(f"- {word}: " + "; ".join(
                    f"{x['drug']} {x['dose']} uM {_fold(x['fold'])} (z {_z(x['z'])}"
                    f"{', sig' if x['significant'] else ''}{', ' + Q.ALERT + ' ' + x['alert'] if x['alert'] else ''}"
                    f"{', ' + _cut(x['moa'], 40) if x['moa'] else ''})" for x in recs))
            continue
        P += ["", f"### {word} (every drug-dose with |z| >= 3 or q < {Q_CUT:g}: {len(sub)}, {int((~ok).sum())} of "
                  f"them with an alert {Q.ALERT}; the strongest {k}, plus any of the {k} strongest without an alert "
                  "beyond them; # = rank among all; * = significant)"]
        if recs:
            P += _md(["#", "drug", "uM", "alert", "fold", "z", "q", "lines moved / measured", "dose pattern",
                      "mechanism (targets)", "caveats"],
                     [[x["rank"], x["drug"], x["dose"], f"{Q.ALERT} {x['alert']}" if x["alert"] else "-",
                       _fold(x["fold"]), _z(x["z"]), _q(x["q"]) + ("*" if x["significant"] else ""),
                       f"{x['lines']}/{x['lines_measured']}", x["pattern"] or "-", _cut(x["moa"], 60) or "-",
                       x["caveats"] or "-"]
                      for x in recs])
            rest = len(sub) - len(recs)
            if rest > 0:
                n_al = int((~ok).sum()) - sum(bool(x["alert"]) for x in recs)
                P.append(f"({rest} more in tables/drug_effects.parquet"
                         + (f", {n_al} of them with an alert" if n_al else "") + ")")
        else:
            P.append("none")
    # single lines: drug_line_top ranks every drug-dose (flags / clean columns); an older tables stage held only
    # clean drug-doses
    t, note = _line_cut(C)
    dlt = o.pq("tables/drug_line_top.parquet", columns=["col", "direction", "rank", "drug", "dose", "cell_name",
                                                        "lfc", "z", "pooled_lfc", "pooled_z", "flags", "clean",
                                                        "cc_share"],
               filters=[("col", "==", int(c))]) if C.has("tables/drug_line_top.parquet") else pd.DataFrame()
    recs, older, n_cells, n_cells_alert = [], "clean" not in dlt, len(dlt), 0
    if len(dlt):
        dlt = _with_alert(dlt)
        n_cells_alert = int((dlt["alert"] != "").sum())
        dlt = dlt.assign(az=dlt["z"].abs()).sort_values("az", ascending=False, kind="stable")
        dlt = dlt.iloc[Q._capped(len(dlt), lim["single"], (dlt["alert"] == "").to_numpy())]
        recs = [{"direction": r["direction"], "line": r["cell_name"], "tp53": _tp53(C, r["cell_name"]),
                 "drug": r["drug"], "dose": r["dose"],
                 "fold": _f(2 ** _num(r["lfc"]), "{:.3f}"), "z": _f(r["z"]),
                 "pooled_fold": _f(2 ** _num(r["pooled_lfc"]), "{:.3f}"), "pooled_z": _f(r["pooled_z"]),
                 "alert": r["alert"]}
                for _, r in dlt.iterrows()]
    D["drugs"]["single_line"] = recs
    if short:
        if recs:
            P.append(f"- Strongest single-line cells (|z| >= {t:.1f}): " + "; ".join(
                f"{x['line']} {_sb(x['drug'])} {x['dose']} {_fold(x['fold'])}"
                f"{' ' + Q.ALERT + ' ' + x['alert'] if x['alert'] else ''}" for x in recs))
        return
    which = ("clean drug-doses only: an older tables stage" if older else
             f"every drug-dose: {n_cells} cells, {n_cells_alert} of them with an alert {Q.ALERT}; the strongest "
             f"{lim['single']}, plus any of the {lim['single']} strongest without an alert beyond them")
    P += ["", f"### Strongest single-line responses (per-line |z| >= {t:.1f}, {note}; {which})"]
    if recs:
        P += _md(["dir", "line", "TP53", "drug", "uM", "alert", "per-line fold", "z", "pooled fold", "pooled z"],
                 [[x["direction"], x["line"], x["tp53"] or "-", x["drug"], x["dose"],
                   f"{Q.ALERT} {x['alert']}" if x["alert"] else "-", _fold(x["fold"]), _z(x["z"]),
                   _fold(x["pooled_fold"]), _z(x["pooled_z"])] for x in recs])
        P.append("A large per-line fold with a small pooled one = a response confined to a few lines.")
    else:
        P.append("none passes the per-line cut")


def _with_alert(dlt):
    """drug_line_top rows with an 'alert' column (their flags for this gene in plain words; '' = none). An older
    tables stage wrote clean cells only and no flags: then every alert is ''."""
    if "clean" not in dlt:
        return dlt.assign(alert="")
    fl = dlt["flags"].fillna("").astype(str) if "flags" in dlt else pd.Series("", index=dlt.index)
    cc = dlt["cc_share"] if "cc_share" in dlt else pd.Series(np.nan, index=dlt.index)
    return dlt.assign(alert=[_row_alert(f, bool(cl), s) for f, cl, s in zip(fl, dlt["clean"], cc)])


def _gene_flags(r, novel_ok):
    gen = []
    if bool(r.get("locus", False)):
        d = _num(r.get("distance_bp"))
        gen.append("same locus" + (f" {d / 1000:.0f} kb" if np.isfinite(d) else ""))
    if bool(r.get("readthrough_risk", False)):
        gen.append("READTHROUGH RISK")
    known = []
    s = _num(r.get("string_score"))
    if np.isfinite(s):
        known.append(f"STRING {int(s)}")
    if bool(r.get("shared_gene_group", False)):
        known.append("same HGNC group")
    pw = _text(r.get("shared_pathway"))
    if pw:
        known.append(_cut(pw.replace("HALLMARK_", "Hallmark "), 45))
    if novel_ok and bool(r.get("novel_candidate", False)):
        known.append("NOVEL CANDIDATE")
    return "; ".join(gen), "; ".join(known)


_PAIR_ALERT_SHORT = [(re.compile(r"strong in one random half of the compounds only \(not replicated\)"),
                      "one half only"),
                     (re.compile(r"not reproduced in both random halves of the compounds"), "not reproduced"),
                     (re.compile(r"read-through risk \([^)]*\)"), "read-through risk"),
                     (re.compile(r"same locus \([^)]*\)"), "same locus"),
                     (re.compile(r" is in the vector space only through drug-doses that carry an alert"),
                      " in the space only via flagged drug-doses")]


def _pair_alert_short(t):
    """relations' alert of a pair in a few words (the dossier's partner tables): '' = none."""
    t = str(t or "").replace(Q.ALERT, "").strip()
    for rx, short in _PAIR_ALERT_SHORT:
        t = rx.sub(short, t)
    return t


def _short_evidence(evidence, alert):
    """A partner's evidence in a summary line: ALERT before a pair not replicated in both halves, then the alert's
    other reasons (a locus, a gene in the space only through flagged drug-doses)."""
    ev = evidence or "-"
    rest = [x for x in str(alert or "").split("; ") if x and x not in ("one half only", "not reproduced")]
    return ((f"{Q.ALERT} " if ev in ("one half", "not reproduced") else "") + ev
            + (f"; {Q.ALERT} " + "; ".join(rest) if rest else ""))


def _gene_partners(C, c, rel, in_space, why, lim, short, P, D):
    o = C.o
    P += ["", "## Data partners (genes that move with it / opposite to it across the drug-doses and lines)"]
    D["partners"] = {}
    if rel is None:
        P.append("- " + ("none: the gene is not in the vector space (see above)" if not in_space else
                         "the relations stage has not run"))
        return
    novel_ok, blocked = o.novelty()
    n_with, n_opp = int((rel["cos"] > 0).sum()), int((rel["cos"] < 0).sum())
    both = rel["evidence"] == "both halves"
    weakest = float(rel["cos"].abs().min()) if len(rel) else float("nan")
    P.append(f"- Of its {len(rel)} strongest partners by |cos|: {n_with} move with it, {n_opp} opposite; replicated "
             f"(both halves, fdr <= {REPRO_FDR:g}): {int((both & (rel['cos'] > 0)).sum())} with, "
             f"{int((both & (rel['cos'] < 0)).sum())} opposite; strong in one random half only: "
             f"{int((rel['evidence'] == 'one half').sum())}. Its {len(rel)}th partner has |cos| {weakest:.2f}; "
             "random pairs have cos ~0.")
    if not novel_ok:
        P.append(f"- Novelty not assessed in this run (missing: {', '.join(blocked) or 'reference sources'}): no pair "
                 "is called a novel candidate, and the 'known' column may be incomplete.")
    D["partners"].update({"n": int(len(rel)), "n_with": n_with, "n_opposite": n_opp,
                          "n_replicated": int(both.sum()), "weakest_abs_cos": _f(weakest, "{:.3f}"),
                          "novelty_assessed": bool(novel_ok)})
    # every reason to doubt a pair (relations' alert column: not replicated, same locus, read-through risk, a gene in
    # the space only through flagged drug-doses); an older relations stage: not replicated in both halves
    if "alert" in rel:
        alert = rel["alert"].fillna("").astype(str).map(_pair_alert_short)
    else:
        alert = pd.Series(np.where(rel["evidence"].fillna("").astype(str) == "both halves", "",
                                   "not replicated in both random halves of the compounds"), index=rel.index)
    # the gene's own 'in the space only through flagged drug-doses' is said once above, not on every pair
    own = f"{_label(C, c)} in the space only via flagged drug-doses"
    alert = alert.map(lambda t: "; ".join(x for x in t.split("; ") if x and x != own))
    rel = rel.assign(_alert=alert)
    for sign, word, key in ((1, "Moves with it", "with"), (-1, "Moves opposite to it", "opposite")):
        sub = rel[np.sign(rel["cos"]) == sign].sort_values("cos", ascending=(sign < 0), kind="stable")
        ok = (sub["_alert"] == "").to_numpy()
        pos = Q._capped(len(sub), lim["partners"], ok)
        recs = []
        for (_, r), rank in zip(sub.iloc[pos].iterrows(), pos + 1):
            cb = int(r["col_b"])
            gen, known = _gene_flags(r, novel_ok)
            recs.append({"rank": int(rank), "partner": _label(C, cb), "col": cb, "cos": _f(r["cos"], "{:.3f}"),
                         "half1": _f(r.get("cos_half1"), "{:.3f}"), "half2": _f(r.get("cos_half2"), "{:.3f}"),
                         "evidence": _text(r.get("evidence")), "fdr": _f(r.get("fdr"), "{:.3g}"),
                         "mutual_rank": _f(r.get("mutual_rank"), "{:.0f}"), "specificity": _f(r.get("specificity")),
                         "module": _module_txt(C, cb), "genomic": gen, "known": known,
                         "name": _gene_name(C, cb), "alert": r["_alert"]})
        D["partners"][key] = recs
        D["partners"]["n_" + key + "_alert"] = int((~ok).sum())
        if short:
            if recs:
                P.append(f"- {word}: " + "; ".join(
                    f"{x['partner']} {_cos(x['cos'])} ({_short_evidence(x['evidence'], x['alert'])}"
                    f"{', ' + x['genomic'] if x['genomic'] else ''}{', ' + x['known'] if x['known'] else ''})"
                    for x in recs))
            continue
        P += ["", f"### {word} ({len(sub)}, {int((~ok).sum())} of them with an alert {Q.ALERT}; the strongest "
                  f"{lim['partners']}, plus any of the {lim['partners']} strongest without an alert beyond them; "
                  "# = rank on this side)"]
        if recs:
            P += _md(["#", "partner", "cos", "half 1 / half 2", "evidence", "alert", "fdr", "mutual rank",
                      "specificity", "module", "genomic", "known (STRING / pathway / group)", "name"],
                     [[x["rank"], x["partner"], _cos(x["cos"]), f"{_cos(x['half1'])} / {_cos(x['half2'])}",
                       x["evidence"], f"{Q.ALERT} {x['alert']}" if x["alert"] else "-",
                       _q(x["fdr"]), Q._int(x["mutual_rank"]) if x["mutual_rank"] is not None else ">100",
                       Q._f(x["specificity"], "{:.1f}"), x["module"] or "-", x["genomic"] or "-",
                       x["known"] or "-", _cut(x["name"], 40) or "-"] for x in recs])
        else:
            P.append("none")
    if not short:
        P.append("Mutual rank = the larger of the two genes' ranks for each other (>100: the partner does not have it "
                 "among its 100); specificity = how exceptional the pair is for both genes (robust z, smaller of the "
                 f"two). Genomic flags mean the pair can correlate without regulation. {Q.ALERT} = a reason to doubt "
                 "the pair (not replicated in both random halves of the compounds, neighbours on the genome, or a "
                 "gene in the vector space only through drug-doses with an artifact flag); it keeps its ranked place.")


def _gene_known_absent(C, c, rel, in_space, lim, P, D):
    o = C.o
    sk = C.string_known() if C.loaded("string_links") else None
    ss = C.small_sets() if C.loaded("hallmark", "reactome") else None
    P += ["", "## Known but absent (literature-known partners that are not among its data partners)"]
    D["known_absent"] = []
    if sk is None and ss is None:
        P.append("- Not available: STRING, Hallmark and Reactome were not loaded for this run (the reference stage "
                 "ran offline, failed or did not run).")
        return
    if sk is None or ss is None:
        P.append(f"- Only {'Hallmark / Reactome sets' if sk is None else 'STRING'} loaded for this run; "
                 f"{'STRING' if sk is None else 'Hallmark / Reactome'} partners are missing from this list.")
    known = {}                                     # partner col -> {"string": score, "sets": [(label, size)]}
    if sk is not None:
        a, b, sc = sk
        lo, hi = np.searchsorted(a, c, "left"), np.searchsorted(a, c, "right")
        for p, s in zip(b[lo:hi], sc[lo:hi]):
            if int(p) != c:
                known.setdefault(int(p), {"string": None, "sets": []})["string"] = int(s)
    if ss is not None:
        by_col, members = ss
        for key, size in by_col.get(int(c), []):
            for p in members[key]:
                if int(p) != c:
                    known.setdefault(int(p), {"string": None, "sets": []})["sets"].append((key[1], key[0], size))
    present = set(rel["col_b"].astype(int)) if rel is not None else set()
    absent = [p for p in known if p not in present]
    n_str = sum(1 for v in known.values() if v["string"] is not None)
    P.append(f"- Known partners: {len(known)} (STRING combined score >= {KNOWN_STRING}: {n_str}; sharing a Hallmark or "
             f"Reactome set of <= {KNOWN_SET_MAX} genes: {sum(1 for v in known.values() if v['sets'])}); "
             + (f"{len(known) - len(absent)} are among its {len(rel)} data partners, {len(absent)} are not."
                if rel is not None else "none can be a data partner: the gene has no partners."))
    if not absent:
        return

    def order(p):
        v = known[p]
        return (-(v["string"] or 0), min((s[2] for s in v["sets"]), default=10 ** 6), p)
    absent.sort(key=order)
    U = C.unit()
    space = C.in_space()
    g = C.genes()
    allc = None
    if U is not None and in_space:
        u = np.asarray(U[c], dtype=np.float64)
        Um = np.asarray(U, dtype=np.float32)
        with np.errstate(invalid="ignore"):
            allc = np.abs(Um @ u.astype(np.float32))
        allc[c] = np.nan
        n_space = int(np.isfinite(allc).sum())
        weakest = float(rel["cos"].abs().min()) if rel is not None and len(rel) else float("nan")
        P.append(f"- cos = cosine to {g.at[c, 'label']} in the vector space; rank = rank of |cos| among the "
                 f"{n_space:,} genes in the space (its data partners are ranks 1-{len(rel) if rel is not None else 0}, "
                 f"down to |cos| {weakest:.2f}).")
    elif not in_space:
        P.append(f"- {g.at[c, 'label']} itself is not in the vector space, so no cosine can be given; the status "
                 "column says whether each known partner responds in these data (is in the space) or not.")
    H1 = o.npy("embed/gene_unit_half1.npy") if C.has("embed/gene_unit_half1.npy") else None
    H2 = o.npy("embed/gene_unit_half2.npy") if C.has("embed/gene_unit_half2.npy") else None
    rows, recs = [], []
    for p in absent[:lim["known"]]:
        v = known[p]
        why = []
        if v["string"] is not None:
            why.append(f"STRING {v['string']}")
        for st, src, size in sorted(v["sets"], key=lambda s: s[2])[:2]:
            why.append(f"{'Hallmark' if src == 'hallmark' else 'Reactome'}: {_cut(st.replace('HALLMARK_', ''), 50)} "
                       f"({size} genes)")
        cosv = h1 = h2 = rank = None
        nle = _num(g.at[p, "n_lines_expressing"]) if p in g.index and "n_lines_expressing" in g else np.nan
        p_in = p < len(space) and bool(space[p])
        if p_in and allc is not None:
            cosv = float(np.asarray(U[p], dtype=np.float64) @ np.asarray(U[c], dtype=np.float64))
            rank = int(np.nansum(allc > abs(cosv))) + 1
            if H1 is not None:
                h1 = float(np.asarray(H1[p], dtype=np.float64) @ np.asarray(H1[c], dtype=np.float64))
                h2 = float(np.asarray(H2[p], dtype=np.float64) @ np.asarray(H2[c], dtype=np.float64))
            status = "in the space"
        elif p_in:
            status = "in the space (responds)"
        elif np.isfinite(nle) and nle == 0:
            status = "not measured (expressed in no line)"
        else:
            status = "not in the vector space: " + _short_why(Q._not_in_space(o, p))
        rec = {"partner": _label(C, p), "col": int(p), "known_by": "; ".join(why), "string_score": v["string"],
               "cos": _f(cosv, "{:.3f}"), "rank": rank, "half1": _f(h1, "{:.3f}"), "half2": _f(h2, "{:.3f}"),
               "status": status, "name": _gene_name(C, p)}
        recs.append(rec)
        rows.append([rec["partner"], rec["known_by"], _cos(cosv) if cosv is not None else "-",
                     f"{rank:,}" if rank else "-",
                     f"{_cos(h1)} / {_cos(h2)}" if h1 is not None else "-", status, _cut(rec["name"], 40) or "-"])
    P += [""] + _md(["partner", "known by", "cos", "rank", "half 1 / half 2", "status", "name"], rows)
    if len(absent) > lim["known"]:
        P.append(f"({len(absent) - lim['known']} more known partners are absent; listed: strongest STRING first, then "
                 "the smallest shared sets)")
    D["known_absent"] = recs


def _short_why(txt):
    t = txt.lower()
    if "noise" in t:
        return "noise-class RNA"
    m = re.search(r"\|z\| >= 3 in (\d+) of", txt)
    n = m.group(1) if m else "?"
    if "the space needs" in t:
        return f"responds in too few contexts (z beyond +-3 in {n})"
    if "has neither" in t:
        return f"no significant clean drug-dose or strong single-line response (z beyond +-3 in {n} contexts)"
    return _cut(txt, 80)


def _gene_novel(C, c, rel, lim, short, P, D):
    novel_ok, _ = C.o.novelty()
    recs = []
    if rel is not None and novel_ok and "novel_candidate" in rel:
        nv = rel[rel["novel_candidate"].fillna(False).astype(bool)].sort_values("rank")
        for _, r in nv.head(lim["novel"]).iterrows():
            cb = int(r["col_b"])
            recs.append({"partner": _label(C, cb), "col": cb, "cos": _f(r["cos"], "{:.3f}"),
                         "half1": _f(r["cos_half1"], "{:.3f}"), "half2": _f(r["cos_half2"], "{:.3f}"),
                         "fdr": _f(r["fdr"], "{:.3g}"), "mutual_rank": _f(r["mutual_rank"], "{:.0f}"),
                         "specificity": _f(r["specificity"]), "name": _gene_name(C, cb)})
    D["novel"] = recs
    mem = []
    nm = C.novel_members()
    if nm is not None and len(nm) and lim.get("members"):
        x = nm[nm["col"] == c].sort_values("set_q").head(lim["members"])
        mem = [{"module": int(r["module"]), "arm": _text(r["arm"]), "set": _text(r["set_label"]),
                "source": _text(r["source"]), "set_q": _f(r["set_q"], "{:.3g}"),
                "n_annotated_in_arm": int(r["n_annotated_in_arm"]), "mean_cos": _f(r["mean_cos"], "{:.3f}")}
               for _, r in x.iterrows()]
    D["novel_members"] = mem
    if short:
        if recs:
            P.append("- Novel candidate partners: " + ", ".join(f"{x['partner']} {_cos(x['cos'])}" for x in recs))
        return
    P += ["", "## Novel candidate relations"]
    if not novel_ok:
        P.append("- Not assessed in this run (reference sources missing).")
    elif recs:
        P.append("Mutually among each other's 10 strongest partners, exceptional for both (specificity >= 4), "
                 "replicated in both halves at fdr <= 0.05, |cos| >= 0.5, with no STRING link, shared gene group or "
                 "pathway, and not the same locus:")
        for x in recs:
            P.append(f"- {x['partner']} ({x['name'] or 'no name'}): cos {_cos(x['cos'])} (halves {_cos(x['half1'])} / "
                     f"{_cos(x['half2'])}, fdr {_q(x['fdr'])}, mutual rank {Q._int(x['mutual_rank'])}, specificity "
                     f"{Q._f(x['specificity'], '{:.1f}')})")
    else:
        P.append("- none")
    if mem:
        P += ["", "## Guilt by association (validation: its module is enriched for a set it is not annotated to)"]
        for x in mem:
            P.append(f"- module {x['module']}{x['arm']}: {x['set']} ({x['source']}, q {_q(x['set_q'])}; "
                     f"{x['n_annotated_in_arm']} annotated members on its arm; its mean cos to them "
                     f"{_cos(x['mean_cos'])})")


# ----------------------------------------------------------------------------- probable direction (direction stage)
DIR_LISTS = (("upstream", "Upstream: what probably acts on {g}", "upstream - what probably acts on it"),
             ("downstream", "Downstream: genes {g} probably acts on", "downstream - genes it probably acts on"),
             ("cells", "Cells under drugs: how {g} probably acts on the cells' growth under a drug-dose",
              "cells under drugs - how it probably acts on the cells' growth under a drug-dose"))


def _direction(C):
    """(direction_view.Direction or None, why) of the output (query._direction: one load per process)."""
    return C.get("direction", lambda: Q._direction(C.o))


def _dir_rec(r, rank):
    """One display row as the dossier's data: direction_view's texts and the stage's own numbers."""
    t = DV.texts(r, max_names=None)
    return {"rank": int(rank), "arrow": t["arrow"], "source": t["source"], "sources": list(r["sources"]),
            "target": t["target"], "kind": t["kind"], "evidence": t["kind_short"], "grade": t["grade"],
            "sign": t["sign"], "sign_text": t["sign_text"], "kind_text": t["kind_text"],
            "reading": Q._dir_reading(r), "group": _text(r.get("group")), "q": _num(r.get("q")),
            "q_group": _num(r.get("q_group")), "p": _num(r.get("p")), "q_text": t["q_text"],
            "alerts": t["alerts_long"], "alerts_short": t["alerts_short"], "notes": t["notes_long"],
            "notes_short": t["notes_short"], "caveats": t["caveats_long"], "support": t["support_long"],
            "support_short": t["support_short"],
            "target_drug": _text(r.get("target_drug")), "target_dose": _text(r.get("target_dose")),
            "drugdoses": _text(r.get("top_drugdoses")) if r.get("kind") in DV.RESPONSE else "",
            "rise_share": _num(r.get("rise_share")), "edge_ids": [int(x) for x in r["members"]]}


def _gene_direction(C, c, lim, short, P, D):
    """The gene's probable direction (the direction stage, read through direction_view, which the vault, the map and
    the look-ups use too): what probably acts on it (upstream), the genes it probably acts on (downstream) and how it
    probably acts on the cells under drug-doses, each in direction_view's ORDER and capped by the cap rule (the
    lim['direction'] strongest plus any of that many strongest without an alert beyond them), with the grade, the
    sign words, the evidence, the stage's numbers, q and the alerts (short labels in the table, every reason in full
    once below the tables); the caveat. An output without the stage: one sentence."""
    lab = _label(C, c)
    dv, why = _direction(C)
    D["direction"] = {"available": dv is not None}
    if dv is None:
        txt = ("the direction stage has not run for this output: no probable direction (which gene acts on which) is "
               "available" if not why else f"the direction stage's files cannot be read ({why})")
        if short:
            P.append(f"- Probable direction: {txt}.")
        else:
            P += ["", "## Probable direction", f"- Not available: {txt}."]
        D["direction"]["why"] = txt
        return
    lists = {"upstream": dv.upstream(int(c)), "downstream": dv.downstream(int(c)), "cells": dv.cells(int(c))}
    n = lim.get("direction", 0) or 1
    D["direction"].update({f"n_{k}": int(len(v)) for k, v in lists.items()})
    D["direction"].update({f"n_{k}_alert": int(v["has_alert"].sum()) if len(v) else 0 for k, v in lists.items()})
    D["direction"].update({f"n_{k}_note": int(v["has_note"].sum()) if len(v) and "has_note" in v else 0
                           for k, v in lists.items()})
    D["direction"]["caveat"] = DV.CAVEAT
    kinds = [k_ for v in lists.values() if len(v) for k_ in v["kind"].astype(str).unique()]
    kcav = DV.caveat_header(kinds)
    D["direction"]["kind_caveats"] = kcav
    if short:
        if not any(len(v) for v in lists.values()):
            P.append(f"- Probable direction: no arrow involves {lab} in this run.")
            return
        if kcav:
            P.append(f"- Probable direction, the caveat of every arrow of a kind (stated once): "
                     f"{DV.caveat_header(kinds, short=True)}")
        resp = any(k_ in DV.RESPONSE for k_ in kinds)
        for key, _h, word in DIR_LISTS:
            rows = lists[key]
            if not len(rows):
                continue
            shown, n_more, n_more_al = DV.cap(rows, n)
            more = DV.more_text(n_more, n_more_al, "arrows")
            P.append(f"- Probable direction, {word} ({DV.counts_text(rows, 'arrows')}): "
                     + "; ".join(DV.edge_line(r, alerts="short", max_names=4) for _, r in shown.iterrows())
                     + (f" ... {more}" if more else ""))
        P.append(f"- ({DV.CAVEAT_SHORT}; the sign is what the source's activity probably does to the target"
                 + (": strengthens / weakens a drug response in the target's own direction at each drug-dose - a "
                    "higher rise or a deeper fall -, which says nothing of induction or repression where it rises at "
                    "some drug-doses and falls at others)" if resp else ")"))
        return
    P += ["", "## Probable direction (which genes probably act on it, and what it probably acts on)",
          f"Arrows SOURCE {DV.ARROW} TARGET of the direction stage. The source is what a test conditions on: a "
          "recorded mutation of the source in Tahoe's cell-line genetics (lines with it against lines with no record "
          "of the gene), lines that do not express the source (natural knockouts), compounds that target the "
          "source's protein, or the source's natural level across the lines (a glimpse). The target is what differs "
          "with it: "
          "its level, its drug response, or the cells' numbers under a drug-dose. The sign (column 'probable "
          "direction') is what the source's ACTIVITY probably does to the target; 'not inferred' when the mechanism "
          f"is not recorded. {DV.SIGN_RESPONSE_NOTE} Grades: " + "; ".join(DV.grade_legend("long"))
          + ". q = Benjamini-Hochberg over the "
          f"kind's whole table of tests. {Q.ALERT} = a reason to doubt the arrow, kept in its ranked place (short "
          "labels in the table, each reason in full below). Notes (no warning sign) = reasons kept below their "
          "thresholds, and context: read them too (each in full below). " + DV.CAVEAT]
    if not any(len(v) for v in lists.values()):
        P.append(f"- No arrow involves {lab} in this run (each arrow needs a test result at q < 0.10).")
        return
    if kcav:
        P.append(f"- Caveats, stated once for the lists below: {kcav}")
    reasons = {}                                   # short label -> [its first reason in full, rows with it]
    notes = {}                                     # the same for the notes
    for key, head, _w in DIR_LISTS:
        rows = lists[key]
        recs = []
        if len(rows):
            al = rows["has_alert"].to_numpy(dtype=bool)
            keep = cap_keep(al, n)
            rest = np.setdiff1d(np.arange(len(rows)), keep)
            recs = [_dir_rec(rows.iloc[int(k)], k + 1) for k in keep]
            for x in recs:
                for rs in DV.alert_reasons(x["alerts"]):
                    lb = DV.alert_short(rs)[len(Q.ALERT) + 1:]
                    reasons.setdefault(lb, [rs, 0])[1] += 1
                for rs in DV.note_reasons(x["notes"]):
                    notes.setdefault(DV.notes_short(rs), [rs, 0])[1] += 1
            more = DV.more_text(int(rest.size), int(al[rest].sum()), "arrows")
        D["direction"][key] = recs
        P += ["", f"### {head.format(g=lab)} ({DV.counts_text(rows, 'arrows')}"
                  + (f"; the strongest {n}, plus any of the {n} strongest without an alert beyond them" if recs and
                     len(recs) < len(rows) else "") + ")"]
        if not recs:
            P.append("none")
            continue
        body, last = [], None
        for x in recs:
            cmp_ = x["kind_text"] if x["kind_text"] != last else "(same comparison as the row above)"
            last = x["kind_text"]
            # the drug-doses carrying the difference beyond the one the reading already gives
            more_dd = [t for t in x["drugdoses"].split("; ") if t and f"at {t.rsplit(': ', 1)[0]}" not in x["reading"]]
            dds = f"also at {'; '.join(more_dd)}" if more_dd else ""
            if np.isfinite(x["rise_share"]):
                dds += ("; " if dds else "") + f"{x['rise_share']:.0%} of the evidence from drug-doses where it rises"
            sup = f"support: {x['support_short']}" if x["support_short"] else ""
            body.append([x["rank"], x["arrow"], x["grade"], x["sign_text"], x["evidence"],
                         "; ".join(t for t in (cmp_, x["reading"], dds, sup) if t),
                         x["q_text"][2:] if x["q_text"].startswith("q ") else x["q_text"], x["alerts_short"] or "-",
                         x["notes_short"] or "-"])
        P += _md(["#", "arrow", "grade", "probable direction", "evidence", "comparison and numbers", "q", "alerts",
                  "notes"], body)
        if more:
            P.append(f"({more}, later in the order)")
    if reasons:
        k = lim.get("dir_reasons", 0) or len(reasons)
        P += ["", "Alert reasons in full: each short label of the tables above with its first reason (rows with the "
                  "same label give the same reason with their own numbers):"]
        P += [f"- {lb}: {rs}" + (f" ({n_} rows)" if n_ > 1 else "") for lb, (rs, n_) in list(reasons.items())[:k]]
        if len(reasons) > k:
            P.append(f"- ({len(reasons) - k} more labels; each keeps its place in the tables above)")
    if notes:
        k = lim.get("dir_reasons", 0) or len(notes)
        P += ["", "Notes in full (no warning sign: each is below the threshold at which it would be an alert; the "
                  "thresholds are in direction/README.md): each note label of the tables above with its first reason:"]
        P += [f"- {lb}: {rs}" + (f" ({n_} rows)" if n_ > 1 else "") for lb, (rs, n_) in list(notes.items())[:k]]
        if len(notes) > k:
            P.append(f"- ({len(notes) - k} more note labels; each keeps its place in the tables above)")


# ----------------------------------------------------------------------------- drug
def _drug(C, drug, lim, short=False):
    o = C.o
    dd = C.dd()
    rows_dd = dd[dd["drug"] == drug].copy()
    rows_dd["conc_num"] = pd.to_numeric(rows_dd["conc"], errors="coerce")
    rows_dd = rows_dd.sort_values("conc_num")
    dds = rows_dd["dd"].astype(int).tolist()
    sb = T.salt_base(drug)
    others = sorted(set(dd.loc[(dd["salt_base"] == sb) & (dd["drug"] != drug), "drug"])) if "salt_base" in dd else []
    r0 = rows_dd.iloc[0]
    dr = None
    if C.has("tables/drugs.parquet"):
        t = o.pq("tables/drugs.parquet")
        t = t[t["drug"] == drug]
        dr = t.iloc[0] if len(t) else None
    best_dd = int(dr["best_dd"]) if dr is not None and np.isfinite(_num(dr.get("best_dd"))) else dds[-1]
    trusted_dd = None
    if C.has("embed/drugs.parquet"):
        e = o.pq("embed/drugs.parquet")
        e = e[(e["drug"] == drug)]
        if len(e) and bool(e.iloc[0].get("trusted", True)):
            trusted_dd = int(e.iloc[0]["dd"])
    # The dose whose genes get the full lists: a trustworthy one has no artifact flag (toxic, transcription drop,
    # cell-cycle shift ... - not only the embedding's 'untrusted' flags) and moved genes. The drug's vector dose
    # when it is clean, else the clean dose with the most significant genes; with none, the vector (or best) dose,
    # said plainly to be untrustworthy. A flagged vector dose keeps its full lists too (marked FLAGGED): its
    # response can be the drug's own effect (an antimitotic's cell-cycle shift).
    def _count(x):
        v = _num(x)
        return int(v) if np.isfinite(v) else 0
    art_dd = {int(r["dd"]): _artifacts(r["flags"]) for _, r in rows_dd.iterrows()}
    n_sig = {int(r["dd"]): _count(r.get("n_genes_up")) + _count(r.get("n_genes_down")) for _, r in rows_dd.iterrows()}
    clean = [d for d in dds if not art_dd[d] and n_sig[d] > 0]
    vec_dd = trusted_dd if trusted_dd is not None else best_dd
    if vec_dd not in dds:
        vec_dd = dds[-1]
    if vec_dd in clean:
        show_dd = vec_dd
    elif clean:
        show_dd = max(clean, key=lambda d: (n_sig[d], dds.index(d)))
    else:
        show_dd = vec_dd
    trustworthy = show_dd in clean
    D = {"drug": drug, "salt_base": sb, "other_salt_forms": others, "drugdoses": dds}
    P = [f"# {'Summary' if short else 'Dossier'}: drug {drug}", f"entity_id drug:{drug}", "",
         "## Identity (Tahoe drug metadata: may be incomplete or wrong; verify)"]
    meta = {k: _text(r0.get(k)) for k in ("targets", "moa_fine", "moa_broad", "approved")}
    D["identity"] = meta
    P.append(f"- Compound: {sb}" + (f" · other salt forms in Tahoe: {', '.join(others)}" if others else ""))
    P.append(f"- Targets: {meta['targets'] or '-'} · mechanism: {meta['moa_fine'] or '-'} · class: "
             f"{meta['moa_broad'] or '-'} · approved: {meta['approved'] or '-'}")
    if dr is not None:
        P.append(f"- Doses (uM): {_text(dr['doses'])} · significant genes per dose: {_text(dr['n_sig_by_dose'])} · "
                 f"best dose (most significant genes): {_text(dr['best_dose'])} · lowest active dose: "
                 f"{_text(dr['lowest_active_dose']) or 'none'} · signature r between consecutive doses: "
                 f"{_text(dr['signature_r_between_doses']) or '-'}")
        D["identity"].update({"doses": _text(dr["doses"]), "n_sig_by_dose": _text(dr["n_sig_by_dose"]),
                              "best_dose": _text(dr["best_dose"]),
                              "lowest_active_dose": _text(dr["lowest_active_dose"]),
                              "signature_r_between_doses": _text(dr["signature_r_between_doses"])})
    sdd = rows_dd[rows_dd["dd"] == show_dd].iloc[0]
    vdose = rows_dd[rows_dd["dd"] == vec_dd].iloc[0]["dose"]
    flagged = " · ".join(f"{r['dose']} uM: {art_dd[int(r['dd'])]}" for _, r in rows_dd.iterrows()
                        if art_dd[int(r["dd"])])
    if trustworthy:
        P.append(f"- Best trustworthy dose (no artifact flag; its full gene lists come first below): {sdd['dose']} uM"
                 + (" (also the drug's vector)" if show_dd == vec_dd else
                    f" (the drug's vector uses {vdose} uM, flagged: {art_dd[vec_dd]}; its full lists follow, "
                    "marked FLAGGED)" if art_dd[vec_dd] else f" (the drug's vector uses {vdose} uM)"))
    else:
        P.append("- No trustworthy dose: no dose that moved genes is free of artifact flags ("
                 + (flagged or "no dose moved any gene significantly")
                 + f"). The full gene lists below use {sdd['dose']} uM, the "
                 + ("drug's vector dose" if trusted_dd is not None else "best dose")
                 + ", and may show the artifact (a flag can also be the drug's own effect, e.g. a cell-cycle shift "
                   "from a CDK4/6 inhibitor: say which).")
    D["shown_dose"] = sdd["dose"]
    D["shown_dose_trustworthy"] = bool(trustworthy)
    D["vector_dose"] = vdose
    D["dose_artifact_flags"] = {str(r["dose"]): art_dd[int(r["dd"])] for _, r in rows_dd.iterrows()}

    # per dose
    per = []
    for _, r in rows_dd.iterrows():
        per.append({"dose": r["dose"], "dd": int(r["dd"]), "n_wells": int(_num(r.get("n_wells")) or 0),
                    "plates": _text(r.get("plates")), "n_up": int(_num(r.get("n_genes_up")) or 0),
                    "n_down": int(_num(r.get("n_genes_down")) or 0), "replicate_r": _f(r.get("replicate_r")),
                    "cells_log2": _f(r.get("cells_log2_vs_plate")), "S_z": _f(r.get("S_PHASE_z"), "{:.1f}"),
                    "G2M_z": _f(r.get("G2M_PHASE_z"), "{:.1f}"), "proteasome_z": _f(r.get("PROTEASOME_z"), "{:.1f}"),
                    "flags": _text(r.get("flags"))})
    D["per_dose"] = per
    if short:
        P.append("- Per dose: " + "; ".join(f"{x['dose']} uM {x['n_up']} up / {x['n_down']} down"
                                           f"{' [' + x['flags'] + ']' if x['flags'] else ''}" for x in per))
    else:
        P += ["", "## Per dose (genes: significant at q < 0.10 and >= 1.2x; cells: log2 vs the plate's median drug "
                  "well; module z: S-phase, G2/M and proteasome programmes)"]
        P += _md(["uM", "wells", "plates", "genes up", "down", "replicate r", "cells", "S-phase z", "G2/M z",
                  "proteasome z", "flags"],
                 [[x["dose"], x["n_wells"], x["plates"].replace(",", ", "), x["n_up"], x["n_down"],
                   Q._f(x["replicate_r"]), Q._f(x["cells_log2"], "{:+.2f}"), Q._f(x["S_z"], "{:+.1f}"),
                   Q._f(x["G2M_z"], "{:+.1f}"), Q._f(x["proteasome_z"], "{:+.1f}"), x["flags"] or "-"] for x in per])
        P.append("Artifact flags (toxic, transcription drop, cell-cycle shift, unreliable plate only, position not "
                 "correctable, wells disagree) mean a dose's gene changes may be the artifact; 'replicate r' exists "
                 "only with >= 2 wells.")

    # top genes
    cols = ["col", "symbol", "dd", "lfc", "fold", "z", "q_up", "q_down", "clean", "flags", "n_lines_measured",
            "n_lines_up", "n_lines_down"]
    de = o.pq("tables/drug_effects.parquet", columns=cols, filters=[("dd", "in", dds)])
    D["top_genes"] = {}
    full = [show_dd] + ([vec_dd] if vec_dd != show_dd else [])        # the doses with the full lists
    order = full + [d for d in dds if d not in full]
    for d in order:
        k = lim["top_genes"] if d in full else lim["top_genes_other"]
        if not k:
            continue
        r = rows_dd[rows_dd["dd"] == d].iloc[0]
        x = de[de["dd"] == d]
        up = x[(x["q_up"] < Q_CUT) & (x["lfc"] >= LFC_MIN)].sort_values("z", ascending=False)
        dn = x[(x["q_down"] < Q_CUT) & (x["lfc"] <= -LFC_MIN)].sort_values("z")
        rec = {}
        dose_art = set(_artifacts(r["flags"]).split("; ")) - {""}
        for part, key, nlk in ((up, "up", "n_lines_up"), (dn, "down", "n_lines_down")):
            rec[key] = [{"gene": _label(C, int(y["col"])), "col": int(y["col"]), "fold": _f(y["fold"], "{:.3f}"),
                         "z": _f(y["z"]), "q": _f(y["q_up"] if key == "up" else y["q_down"], "{:.3g}"),
                         "lines": int(y[nlk]), "lines_measured": int(y["n_lines_measured"]),
                         "gene_flags": "; ".join(f for f in _artifacts(y["flags"]).split("; ")
                                                 if f and f not in dose_art),
                         "name": _gene_name(C, int(y["col"]))} for _, y in part.head(k).iterrows()]
            rec["n_" + key] = int(len(part))
        D["top_genes"][r["dose"]] = rec
        art = _artifacts(r["flags"])
        if short:
            for key, word in (("up", "raised"), ("down", "lowered")):
                if rec[key]:
                    P.append(f"- {r['dose']} uM {word} ({rec['n_' + key]}): " + ", ".join(
                        f"{y['gene']} {_fold(y['fold'])}" for y in rec[key]))
            continue
        tag = " (best trustworthy dose)" if trustworthy else " (best dose; NO dose is trustworthy)"
        head = f"## Top genes at {r['dose']} uM" + (tag if d == show_dd else " (the drug's vector dose)"
                                                    if d == vec_dd else "")
        P += ["", head + (f" - FLAGGED: {art}: these changes may be the artifact" if art else "")]
        for key, word in (("up", "Raised"), ("down", "Lowered")):
            n_ = rec["n_" + key]
            P.append(f"### {word}: {n_} significant gene{'s' if n_ != 1 else ''}"
                     + (f", strongest {k} shown" if n_ > k else ""))
            if rec[key]:
                P += _md(["gene", "fold", "z", "q", "lines moved / measured", "gene artifact flags", "name"],
                         [[y["gene"], _fold(y["fold"]), _z(y["z"]), _q(y["q"]), f"{y['lines']}/{y['lines_measured']}",
                           y["gene_flags"] or "-", _cut(y["name"], 45) or "-"] for y in rec[key]])
            else:
                P.append("none")

    # targets
    tg = [t.strip() for t in re.split(r"[,;/|]", meta["targets"] or "") if t.strip()]
    trec = []
    if tg and lim["targets"]:
        DL, DZ = o.eff("DD_lfc"), o.eff("DD_z")
        Qu, Qd = o.eff("DD_qup"), o.eff("DD_qdn")
        g = C.genes()
        sx = C.sym_index()
        for t in tg[:lim["targets"]]:
            cs = sx.get(t.upper())
            if not cs:
                try:
                    cs, _ = Q.resolve_gene(o, t)
                except Q.NotFound:
                    cs = None
            if not cs:
                trec.append({"target": t, "status": "not among the run's genes"})
                continue
            tc = int(cs[0])
            vals = []
            for d in dds:
                lf, zz = _num(DL[d, tc]), _num(DZ[d, tc])
                sig = (_num(Qu[d, tc]) < Q_CUT and lf >= LFC_MIN) or (_num(Qd[d, tc]) < Q_CUT and lf <= -LFC_MIN)
                vals.append({"dose": dd.at[d, "dose"], "fold": _f(2 ** lf, "{:.3f}") if np.isfinite(lf) else None,
                             "z": _f(zz), "significant": bool(sig)})
            nle = _num(g.at[tc, "n_lines_expressing"]) if "n_lines_expressing" in g else np.nan
            trec.append({"target": _label(C, tc), "col": tc, "n_lines_expressing": int(nle) if np.isfinite(nle)
                         else None, "by_dose": vals, "status": "measured" if np.isfinite(nle) and nle > 0 else
                         "not expressed in any line"})
    D["targets"] = trec
    if trec and not short:
        P += ["", "## The targets' own mRNA (pooled fold (z) per dose; * = significant). Inhibitors often leave their "
                  "target's mRNA unchanged; feedback can raise it"]
        P += _md(["target", "lines expressing"] + [f"{x['dose']} uM" for x in per],
                 [[t["target"], Q._int(t.get("n_lines_expressing"))] +
                  ([f"{_fold(v['fold'])} ({_z(v['z'])}){'*' if v['significant'] else ''}" for v in t["by_dose"]]
                   if "by_dose" in t else [t["status"]] + [""] * (len(per) - 1)) for t in trec])
    elif trec and short:
        P.append("- Targets' own mRNA at the top dose: " + "; ".join(
            f"{t['target']} {_fold(t['by_dose'][-1]['fold'])}" if "by_dose" in t else f"{t['target']} ({t['status']})"
            for t in trec))

    # modules
    mods = C.modules()
    mrec = []
    if mods is not None and C.has("graph/module_pooled_z.npy") and lim["modules"]:
        M = np.asarray(o.npy("graph/module_pooled_z.npy")[:, dds], dtype=np.float32)
        with np.errstate(invalid="ignore"):
            best = np.nan_to_num(np.nanmax(np.abs(M), axis=1), nan=0.0) if M.size else np.zeros(len(mods))
        for m in [m for m in np.argsort(-best) if best[m] >= 2.0][:lim["modules"]]:
            mr = mods.iloc[m]
            mm = int(mr["module"])
            opp, _b = o.module_arms(mm)
            mrec.append({"module": mm, "n_genes": int(mr["n_genes"]), "label": o.module_label(mm),
                         "arms_opposite": bool(opp), "scores": [_f(v, "{:.1f}") for v in M[m]]})
    D["modules"] = mrec
    if not short:
        P += ["", "## Modules it moves (module score = mean pooled z of the + arm minus the - arm; |score| >= 2 "
                  "listed)"]
        if mrec:
            P += _md(["module", "genes", "label", "arms"] + [f"{x['dose']} uM" for x in per],
                     [[x["module"], x["n_genes"], _cut(x["label"], 60), "+/- opposite" if x["arms_opposite"]
                       else "single", *[Q._f(v, "{:+.1f}") for v in x["scores"]]] for x in mrec])
        else:
            P.append("none")
    elif mrec:
        P.append("- Modules: " + "; ".join(f"{x['module']} {_cut(x['label'], 40)} ({Q._f(x['scores'][-1], '{:+.1f}')})"
                                           for x in mrec))

    # lines
    ln = C.lines()
    DA, DAz, Db = o.eff("DD_A"), o.eff("DD_Az"), o.eff("DD_beta")
    dep = []
    for _, r in rows_dd.iterrows():
        d = int(r["dd"])
        az = np.asarray(DAz[d], dtype=np.float32)
        a_ = np.asarray(DA[d], dtype=np.float32)
        for l in np.flatnonzero(np.nan_to_num(az, nan=0.0) <= DEPLETE_Z):
            dep.append({"dose": r["dose"], "line": ln.at[l, "name"], "organ": _text(ln.at[l, "Organ"])
                        if "Organ" in ln else "", "tp53": _text(ln.at[l, "tp53_status"]) if "tp53_status" in ln
                        else "", "abundance": _f(2 ** a_[l], "{:.3f}"), "z": _f(az[l]),
                        "dose_flags": _artifacts(r["flags"])})
    dep.sort(key=lambda x: x["z"])
    D["depleted"] = dep[:lim["deplete"]]
    b = np.asarray(Db[show_dd], dtype=np.float32)
    beta = {}
    if np.isfinite(b).any():
        o_ = [l for l in np.argsort(-np.nan_to_num(b, nan=-np.inf), kind="stable") if np.isfinite(b[l])]
        k = min(lim["beta"], len(o_) // 2)
        beta = {"dose": sdd["dose"], "most": [(ln.at[l, "name"], _f(b[l]), _tp53(C, ln.at[l, "name"]))
                                              for l in o_[:k]],
                "least": [(ln.at[l, "name"], _f(b[l]), _tp53(C, ln.at[l, "name"])) for l in o_[::-1][:k]]}
    D["response_strength"] = beta
    if short:
        if dep:
            P.append("- Depletes: " + ", ".join(f"{x['line']} ({x['dose']} uM, z {_z(x['z'])})"
                                                for x in dep[:lim["deplete"]]))
    else:
        P += ["", f"## Lines it depletes (relative abundance z <= {DEPLETE_Z:g} vs the other lines in the same wells, "
                  "24 h)"]
        if dep:
            P += _md(["uM", "line", "organ", "TP53", "abundance", "z", "dose artifact flags"],
                     [[x["dose"], x["line"], x["organ"], x["tp53"], _fold(x["abundance"]), _z(x["z"]),
                       x["dose_flags"] or "-"] for x in dep[:lim["deplete"]]])
            if len(dep) > lim["deplete"]:
                P.append(f"({len(dep) - lim['deplete']} more)")
        else:
            P.append("none")
        P += ["", f"## Lines that show its transcriptional response most / least (DD_beta at {sdd['dose']} uM: 1 = "
                  "typical line, 0 = no response; needs >= 20 significant genes)"]
        if beta:
            P.append("- most: " + ", ".join(f"{n} {v:.2f}" + (f" (TP53 {t})" if t else "") for n, v, t in beta["most"]))
            P.append("- least: " + ", ".join(f"{n} {v:.2f}" + (f" (TP53 {t})" if t else "")
                                            for n, v, t in beta["least"]))
        else:
            P.append("- no estimate (fewer than 20 significant genes)")

    # nearest drugs
    near = []
    if C.has("embed/drug_vectors.npy") and C.has("embed/drugs.parquet") and lim["near_drugs"]:
        ed = o.pq("embed/drugs.parquet").reset_index(drop=True)
        V = np.asarray(o.npy("embed/drug_vectors.npy"), dtype=np.float64)
        nrm = np.sqrt((V ** 2).sum(axis=1))
        hit = np.flatnonzero(ed["drug"].to_numpy() == drug)
        min_act = o.embed_info().get("min_active", 10)
        if len(hit) and nrm[hit[0]] > 0:
            i = hit[0]
            with np.errstate(invalid="ignore", divide="ignore"):
                cs = V @ V[i] / (nrm * nrm[i])
            nsig = ed["n_sig_genes"].to_numpy() if "n_sig_genes" in ed else np.full(len(ed), min_act)
            ok = (nsig >= min_act) & (np.arange(len(ed)) != i) & np.isfinite(cs)
            for j in [j for j in np.argsort(-np.where(ok, cs, -np.inf)) if ok[j]][:lim["near_drugs"]]:
                e_ = ed.iloc[j]
                near.append({"drug": e_["drug"], "dose": _text(e_["dose"]), "cos": _f(cs[j], "{:.3f}"),
                             "n_sig": int(nsig[j]), "same_compound": T.salt_base(e_["drug"]) == sb,
                             "moa": _text(e_.get("moa_fine")), "targets": _text(e_.get("targets"))})
            D["vector_note"] = (f"its best dose has only {int(nsig[i])} significant genes (< {min_act}): its vector "
                                "and neighbours are mostly noise") if nsig[i] < min_act else ""
        else:
            D["vector_note"] = "no drug vector (no effect on the genes of the space)"
    D["nearest_drugs"] = near
    if short:
        if near:
            P.append("- Nearest drugs: " + ", ".join(f"{x['drug']} {_cos(x['cos'])}" for x in near))
        return P, D
    P += ["", "## Nearest drugs by transcriptional effect (cosine of drug vectors, each at the drug's vector dose; "
              "drugs with >= 10 significant genes)"]
    if D.get("vector_note"):
        P.append(f"- NOTE: {D['vector_note']}")
    if near:
        P += _md(["drug", "uM", "cos", "sig genes", "mechanism", "targets"],
                 [[x["drug"] + (" (same compound)" if x["same_compound"] else ""), x["dose"], _cos(x["cos"]),
                   x["n_sig"], x["moa"] or "-", _cut(x["targets"], 50) or "-"] for x in near])
    elif not D.get("vector_note"):
        P.append("none")
    return P, D


# ----------------------------------------------------------------------------- line
def _line(C, l, lim, short=False):
    o = C.o
    ln = C.lines()
    r = ln.iloc[l]
    nm = r["name"]
    D = {"line": int(l), "cell_line_id": _text(r.get("cell_line_id")), "cell_name": nm}
    P = [f"# {'Summary' if short else 'Dossier'}: cell line {nm} ({_text(r.get('cell_line_id'))})",
         f"entity_id line:{_text(r.get('cell_line_id'))}", "", "## Identity (Tahoe cell-line metadata)"]
    ident = {k: _text(r.get(k)) for k in ("Organ", "Cell_ID_DepMap", "tp53_status", "drivers", "driver_changes")}
    D["identity"] = ident
    P.append(f"- Organ: {ident['Organ'] or '-'} · Cellosaurus {D['cell_line_id']} · DepMap "
             f"{ident['Cell_ID_DepMap'] or '-'} · TP53: {ident['tp53_status'] or 'unknown'} (from the drivers list)")
    cvcl = D["cell_line_id"].strip()
    if re.fullmatch(r"CVCL_[A-Z0-9]{4,6}", cvcl):
        # written out in full: web_fetch only opens URLs that are already in the conversation (the dossier, a
        # tool result), never one the model composes from a template
        D["cellosaurus_urls"] = [CELLOSAURUS_URL.format(cvcl) + ".txt", CELLOSAURUS_URL.format(cvcl)]
        P.append(f"- Cellosaurus entry (mutations, synonyms, misidentification / contamination warnings): "
                 f"{D['cellosaurus_urls'][0]} (plain text) · {D['cellosaurus_urls'][1]}")
    if ident["drivers"]:
        P.append(f"- Drivers: {ident['drivers']}")
    if ident["driver_changes"]:
        P.append(f"- Driver protein changes: {ident['driver_changes']}")
    bits = [f"{Q._int(r.get('n_cells_total'))} cells in total"]
    if np.isfinite(_num(r.get("wells_usable"))):
        bits.append(f"usable expression in {Q._int(r.get('wells_usable'))} wells "
                    f"({Q._f(r.get('pct_wells_usable'), '{:.1f}')}%)")
    if "in_growth_analysis" in r:
        bits.append("in the growth analysis" if bool(r.get("in_growth_analysis")) else "NOT in the growth analysis "
                    "(too few cells: depletion not measured)")
    P.append("- " + "; ".join(bits))
    Db = np.asarray(o.eff("DD_beta"), dtype=np.float32)
    with np.errstate(invalid="ignore"):
        med = np.nanmedian(Db, axis=0) if np.isfinite(Db).any() else np.full(len(ln), np.nan)
    if np.isfinite(med[l]):
        rank = int((np.nan_to_num(med, nan=-np.inf) > med[l]).sum()) + 1
        P.append(f"- Response strength: median DD_beta {med[l]:.2f} over drug-doses with >= 20 significant genes (1 = "
                 f"typical line); rank {rank} of {int(np.isfinite(med).sum())} lines.")
        D["response_strength"] = {"median_beta": _f(med[l], "{:.3f}"), "rank": rank}

    g = C.genes()
    gK = len(g)
    cpm = np.asarray(o.eff("line_cpm")[:, :gK], dtype=np.float64)
    em = np.asarray(o.measured()[:, :gK], dtype=bool)
    noise = g["noise_rna"].to_numpy().astype(bool) if "noise_rna" in g else np.zeros(gK, dtype=bool)
    lg = np.log2(cpm + 1.0)
    others = np.delete(np.arange(len(ln)), l)
    with np.errstate(invalid="ignore"):
        med_o = np.median(lg[others], axis=0)
        spec = lg[l] - med_o
    nexp = em.sum(axis=0)

    # drivers' own mRNA
    drv = []
    for part in [p.strip() for p in ident["drivers"].split(";") if p.strip()]:
        m = re.match(r"^([A-Za-z0-9\-\.]+)\s*\(([^)]*)\)", part)
        sym, change = (m.group(1), m.group(2)) if m else (part, "")
        cs = C.sym_index().get(sym.upper())
        if not cs:
            drv.append({"gene": sym, "change": change, "status": "not among the run's genes"})
            continue
        i = int(cs[0])
        drv.append({"gene": sym, "change": change, "cpm": _f(cpm[l, i], "{:.1f}"),
                    "median_other": _f(2 ** med_o[i] - 1, "{:.1f}"), "x_median": _f(2 ** spec[i], "{:.3f}"),
                    "measured": bool(em[l, i])})
    D["drivers"] = drv
    if drv and not short:
        P += ["", "## The driver genes' own mRNA here (line_cpm vs the median of the other lines; a deletion or a "
                  "nonsense change often lowers it, an amplification raises it)"]
        P += _md(["gene", "change", "CPM here", "median other lines", "x median", "measured here"],
                 [[x["gene"], x["change"], Q._f(x.get("cpm"), "{:,.1f}"), Q._f(x.get("median_other"), "{:,.1f}"),
                   _fold(x.get("x_median")), ("yes" if x.get("measured") else "no (ambient only)")
                   if "cpm" in x else x["status"]] for x in drv])

    # baseline high / low
    ok = (cpm[l] >= Q.SPECIFIC_MIN_CPM) & em[l] & ~noise & np.isfinite(spec)
    hi = [i for i in np.argsort(-np.where(ok, spec, -np.inf)) if ok[i]][:lim["baseline_hi"]]
    nxt = others[np.argmax(cpm[others], axis=0)] if len(others) else np.zeros(gK, dtype=int)
    D["baseline_high"] = [{"gene": g.at[i, "label"], "col": int(i), "cpm": _f(cpm[l, i], "{:.1f}"),
                           "median_other": _f(2 ** med_o[i] - 1, "{:.1f}"), "x_median": _f(2 ** spec[i], "{:.3f}"),
                           "next_line": ln.at[nxt[i], "name"], "next_cpm": _f(cpm[nxt[i], i], "{:.1f}"),
                           "lines_expressing": int(nexp[i]), "name": _gene_name(C, i)} for i in hi]
    okl = (med_o >= np.log2(20 + 1)) & (nexp >= 0.5 * len(ln)) & ~noise & np.isfinite(spec)
    lo = [i for i in np.argsort(np.where(okl, spec, np.inf)) if okl[i] and spec[i] < -1][:lim["baseline_lo"]]
    D["baseline_low"] = [{"gene": g.at[i, "label"], "col": int(i), "cpm": _f(cpm[l, i], "{:.1f}"),
                          "median_other": _f(2 ** med_o[i] - 1, "{:.1f}"), "x_median": _f(2 ** spec[i], "{:.3f}"),
                          "measured_here": bool(em[l, i]), "name": _gene_name(C, i)} for i in lo]
    if short:
        P.append("- Specifically high at baseline: " + ", ".join(f"{x['gene']} {_fold(x['x_median'])}"
                                                               for x in D["baseline_high"]))
        if D["baseline_low"]:
            P.append("- Specifically low: " + ", ".join(f"{x['gene']} {_fold(x['x_median'])}"
                                                       for x in D["baseline_low"]))
    else:
        P += ["", f"## Genes specifically high at baseline (this line vs the median of the other lines; >= "
                  f"{Q.SPECIFIC_MIN_CPM:g} CPM here; noise-class RNA left out)"]
        P += _md(["gene", "CPM here", "median other", "x median", "next highest line (CPM)", "lines expressing",
                  "name"],
                 [[x["gene"], Q._f(x["cpm"], "{:,.0f}"), Q._f(x["median_other"], "{:,.1f}"), _fold(x["x_median"]),
                   f"{x['next_line']} {Q._f(x['next_cpm'], '{:,.0f}')}", x["lines_expressing"],
                   _cut(x["name"], 40) or "-"] for x in D["baseline_high"]] or [["none"] + [""] * 6])
        P += ["", "## Genes specifically low or absent here (>= 20 CPM in the median other line, expressed in most "
                  "lines; 'measured here' no = below the ambient-RNA floor)"]
        if D["baseline_low"]:
            P += _md(["gene", "CPM here", "median other", "x median", "measured here", "name"],
                     [[x["gene"], Q._f(x["cpm"], "{:,.1f}"), Q._f(x["median_other"], "{:,.0f}"), _fold(x["x_median"]),
                       "yes" if x["measured_here"] else "no", _cut(x["name"], 40) or "-"] for x in D["baseline_low"]])
        else:
            P.append("none below 0.5x the median line")

    # depletion
    dd = C.dd()
    az = np.asarray(o.eff("DD_Az")[:, l], dtype=np.float32)
    a_ = np.asarray(o.eff("DD_A")[:, l], dtype=np.float32)
    hit = np.flatnonzero(np.nan_to_num(az, nan=0.0) <= DEPLETE_Z)
    hit = hit[np.argsort(az[hit])]
    D["depleted_by"] = [{"drug": dd.at[d, "drug"], "dose": dd.at[d, "dose"], "abundance": _f(2 ** a_[d], "{:.3f}"),
                         "z": _f(az[d]), "n_sig_genes": int(_num(dd.at[d, "n_sig_genes"]) or 0),
                         "flags": _text(dd.at[d, "flags"]), "moa": _moa_text(C, dd.at[d, "drug"])}
                        for d in hit[:lim["deplete"]]]
    D["n_depleting"] = int(len(hit))
    if short:
        if len(hit):
            P.append(f"- Depleted by {len(hit)} drug-doses: " + ", ".join(
                f"{x['drug']} {x['dose']} (z {_z(x['z'])})" for x in D["depleted_by"]))
    else:
        P += ["", f"## Drug-doses that deplete it (relative abundance z <= {DEPLETE_Z:g} vs the other lines in the "
                  f"same wells, 24 h): {len(hit)}, {int((~dd['artifact'].to_numpy()[hit]).sum())} without artifact "
                  "flags"]
        if len(hit):
            P += _md(["drug", "uM", "abundance", "z", "sig genes", "flags", "mechanism (targets)"],
                     [[x["drug"], x["dose"], _fold(x["abundance"]), _z(x["z"]), x["n_sig_genes"], x["flags"] or "-",
                       _cut(x["moa"], 60) or "-"] for x in D["depleted_by"]])
        else:
            P.append("none")

    # strongest responses
    t, note = _line_cut(C)
    dlt = o.pq("tables/drug_line_top.parquet", columns=["col", "direction", "drug", "dose", "line", "lfc", "z",
                                                        "pooled_lfc", "pooled_z", "flags", "clean", "cc_share"],
               filters=[("line", "==", int(l))]) if C.has("tables/drug_line_top.parquet") else pd.DataFrame()
    resp, older, n_cells, n_cells_alert = [], "clean" not in dlt, len(dlt), 0
    if len(dlt):
        dlt = _with_alert(dlt)
        n_cells_alert = int((dlt["alert"] != "").sum())
        dlt = dlt.assign(az=dlt["z"].abs()).sort_values("az", ascending=False, kind="stable")
        dlt = dlt.iloc[Q._capped(len(dlt), lim["responses"], (dlt["alert"] == "").to_numpy())]
        resp = [{"gene": _label(C, int(x["col"])), "direction": x["direction"], "drug": x["drug"], "dose": x["dose"],
                 "fold": _f(2 ** _num(x["lfc"]), "{:.3f}"), "z": _f(x["z"]),
                 "pooled_fold": _f(2 ** _num(x["pooled_lfc"]), "{:.3f}"), "pooled_z": _f(x["pooled_z"]),
                 "alert": x["alert"]}
                for _, x in dlt.iterrows()]
    D["strongest_responses"] = resp
    if short:
        if resp:
            P.append("- Strongest responses: " + "; ".join(f"{x['gene']} {x['direction']} {_sb(x['drug'])} {x['dose']} "
                                                          f"{_fold(x['fold'])}"
                                                          f"{' ' + Q.ALERT + ' ' + x['alert'] if x['alert'] else ''}"
                                                          for x in resp))
    else:
        which = ("clean drug-doses only: an older tables stage" if older else
                 f"every drug-dose: {n_cells} cells, {n_cells_alert} of them with an alert {Q.ALERT} (an artifact "
                 f"flag for that gene: the change may be the artifact); the strongest {lim['responses']}, plus any "
                 f"of the {lim['responses']} strongest without an alert beyond them")
        P += ["", f"## Its strongest responses (gene x drug-dose cells of this line at per-line |z| >= {t:.1f}, "
                  f"{note}; {which}; pooled = median over all lines)"]
        if resp:
            P += _md(["gene", "dir", "drug", "uM", "alert", "fold here", "z here", "pooled fold", "pooled z"],
                     [[x["gene"], x["direction"], x["drug"], x["dose"],
                       f"{Q.ALERT} {x['alert']}" if x["alert"] else "-", _fold(x["fold"]), _z(x["z"]),
                       _fold(x["pooled_fold"]), _z(x["pooled_z"])] for x in resp])
            P.append("A large fold here with a small pooled one = a response specific to this line (or a few).")
        else:
            P.append("none")

    # components
    comp = []
    if C.has("embed/line_response_vectors.npy") and C.has("embed/components.parquet") and lim["components"]:
        S = np.asarray(o.npy("embed/line_response_vectors.npy"), dtype=np.float64)
        cp = o.pq("embed/components.parquet").reset_index(drop=True)
        k = min(S.shape[1], len(cp))
        var = cp["variance_pct_of_space"].to_numpy()[:k]
        s = S[l, :k]
        ranks = (S[:, :k] > s[None, :]).sum(axis=0) + 1
        main = np.flatnonzero(var >= max(1.0, np.sort(var)[::-1][min(len(var) - 1, 15)]))   # the larger ones
        for sign, word in ((1, "more"), (-1, "less")):
            dev = sign * (s[main] - 1.0)
            for j in main[np.argsort(-dev)]:
                if sign * (s[j] - 1.0) < 0.3 or len([x for x in comp if x["direction"] == word]) >= lim["components"]:
                    continue
                c_ = cp.iloc[j]
                comp.append({"direction": word, "component": int(c_["component"]), "variance_pct": _f(var[j], "{:.1f}"),
                             "slope": _f(s[j], "{:.2f}"), "rank": int(ranks[j]), "n_lines": int(S.shape[0]),
                             "top_pos_genes": _cut(c_.get("top_pos_genes"), 90),
                             "top_neg_genes": _cut(c_.get("top_neg_genes"), 90),
                             "top_pos_drugdoses": _cut(c_.get("top_pos_drugdoses"), 90),
                             "top_neg_drugdoses": _cut(c_.get("top_neg_drugdoses"), 90)})
    D["components"] = comp
    if short:
        if comp:
            P.append("- Responds more / less than the typical line to: " + "; ".join(
                f"component {x['component']} ({x['slope']:.2f}; genes {_cut(x['top_pos_genes'], 40)})" for x in comp))
        return P, D
    P += ["", "## Programmes (components of the vector space) it responds to more / less than the typical line "
              "(slope 1 = typical, 0 = no response; components with >= 1% of the space)"]
    if comp:
        P += _md(["", "component", "% of space", "slope", "rank (of lines)", "genes (+ side)", "genes (- side)",
                  "drug-doses driving it (+ side)"],
                 [[x["direction"], x["component"], Q._f(x["variance_pct"], "{:.1f}"), Q._f(x["slope"], "{:.2f}"),
                   f"{x['rank']}/{x['n_lines']}", x["top_pos_genes"], x["top_neg_genes"], x["top_pos_drugdoses"]]
                  for x in comp])
    else:
        P.append("none deviates by >= 0.3 from the typical line")
    return P, D


# ----------------------------------------------------------------------------- pair (tahoe_lookup only)
def _unmeasured_source(C, name):
    """The summary of a name that is no gene of this run but the source of probable-direction arrows (a drug target
    the screen does not measure, a recorded driver gene whose own mRNA is not measured) - the gene dossiers name such
    sources in their arrows, and `tahoe gene NAME` lists them (query._unmeasured_source). None when it is not one."""
    key = str(name).strip().strip(",;")
    if not key or not Q._is_direction_source(C.o, key):
        return None
    dv, _why = _direction(C)
    if dv is None:
        return None
    down, cells = dv.downstream(key), dv.cells(key)
    if not (len(down) or len(cells)):
        return None
    first = down if len(down) else cells
    lab = next((s_ for s_ in first.iloc[0]["sources"] if str(s_).upper() == key.upper()), key)
    n = SHORT.get("direction") or 4
    P = [f"# Summary: {lab} (not a measured gene of this run)",
         f"- No gene of this run has this symbol, label, Ensembl id or alias, but {lab} is the source of "
         "probable-direction arrows: a gene that compounds of the screen target, or a driver gene recorded in Tahoe's "
         "cell-line genetics, whose own mRNA is not among the genes measured here. Its arrows (pair look-up "
         f"'{lab}|GENE' gives the arrows to one gene with every alert in full):"]
    kcav = DV.caveat_header([k_ for v in (down, cells) if len(v) for k_ in v["kind"].astype(str).unique()])
    if kcav:
        P.append(f"- Caveats, stated once for the lists below: {kcav}")
    for word, rows in (("downstream (genes it probably acts on)", down),
                       ("on the cells under drug-doses", cells)):
        if not len(rows):
            continue
        shown, n_more, n_more_al = DV.cap(rows, n)
        more = DV.more_text(n_more, n_more_al, "arrows")
        P.append(f"- Probable direction, {word} ({DV.counts_text(rows, 'arrows')}): "
                 + "; ".join(DV.edge_line(r, alerts="short", max_names=4) for _, r in shown.iterrows())
                 + (f" ... {more}" if more else ""))
    P.append(f"- ({DV.CAVEAT_SHORT}; the sign is what the source's activity probably does to the target. "
             f"{DV.SIGN_RESPONSE_NOTE})")
    return "\n".join(P) + "\n"


def _dir_pair_tail(d):
    """Below a pair's arrows (edge_line: alerts in full, notes as short labels): each note and support reason in full,
    and the caveats of their kinds - nothing of a row is left out."""
    if d is None or not len(d):
        return []
    out = []
    nr = list(dict.fromkeys(x for _, r in d.iterrows() for x in DV.note_reasons(r)))
    sr = list(dict.fromkeys(x for _, r in d.iterrows() for x in DV.support_reasons(r)))
    if nr:
        out.append("- notes of these arrows in full (no warning sign: below the threshold at which each would be an "
                   "alert): " + "; ".join(nr))
    if sr:
        out.append("- support of these arrows: " + "; ".join(sr))
    kc = DV.caveat_header(d)
    if kc:
        out.append(f"- caveats: {kc}")
    return out


def _pair_unmeasured(C, src, cb):
    """A pair whose one name is a direction source that is not a measured gene (src) and the other a gene (col cb):
    the arrows src -> cb with every alert in full (none can point the other way: an arrow's target is a measured
    gene or the cells). None when src is not such a source."""
    key = str(src).strip().strip(",;")
    if not Q._is_direction_source(C.o, key):
        return None
    dv, _why = _direction(C)
    if dv is None:
        return None
    lb = _label(C, cb)
    d = dv.downstream(key)
    d = d[d["target_col"].to_numpy() == int(cb)] if len(d) else d
    P = [f"# Pair: {key} x {lb}",
         f"- {key} is not a measured gene of this run (no expression data of its own), but the source of "
         "probable-direction arrows; only the probable direction can link the two.",
         f"- probable direction {DV.arrow(key, lb)}: " + (
             "; ".join(DV.edge_line(r, alerts="long", max_names=4) for _, r in d.iterrows()) or "none"),
         f"- probable direction {DV.arrow(lb, key)}: none can exist (an arrow's target is a measured gene or the "
         "cells)"] + _dir_pair_tail(d) + [
         f"- ({DV.CAVEAT_SHORT}; the sign is what the source's activity probably does to the target. "
         f"{DV.SIGN_RESPONSE_NOTE})"]
    return "\n".join(P) + "\n"


def _pair(C, name):
    parts = [p.strip() for p in re.split(r"\s*\|\s*|\s*,\s*|\s+vs\.?\s+", str(name).strip()) if p.strip()]
    if len(parts) != 2:
        parts = str(name).split()
    if len(parts) != 2:
        raise Q.NotFound("a pair look-up needs two genes: name = 'GENE_A|GENE_B'")
    o = C.o
    found = []
    for p_ in parts:
        try:
            found.append(int(Q.resolve_gene(o, p_)[0][0]))
        except Q.NotFound as e:
            found.append(e)
    bad = [i for i, f in enumerate(found) if isinstance(f, Exception)]
    if bad:
        i = bad[0]
        if len(bad) == 1:                            # a direction source that is no gene, and a gene
            alt = _pair_unmeasured(C, parts[i], found[1 - i])
            if alt:
                return alt
        if Q._is_direction_source(o, parts[i]):
            raise Q.NotFound(f"{str(found[i]).rstrip('.')}. {parts[i]} is not a measured gene of this run, but the "
                             f"source of probable-direction arrows: a gene look-up of {parts[i]} lists them")
        raise found[i]
    ca, cb = found
    la, lb = _label(C, ca), _label(C, cb)
    P = [f"# Pair: {la} x {lb}"]
    if ca == cb:
        return "\n".join(P + ["- the same gene twice"]) + "\n"
    space = C.in_space()
    for c in (ca, cb):
        if not (c < len(space) and space[c]):
            P.append(f"- {_label(C, c)} is not in the vector space: {_short_why(Q._not_in_space(o, c))}")
    r = Q._pair_relation(o, ca, cb) if all(c < len(space) and space[c] for c in (ca, cb)) else None
    if r is not None:
        bits = [f"cos {_cos(r.get('cos'))}"]
        if r.get("cos_half1") is not None:
            bits.append(f"halves {_cos(r.get('cos_half1'))} / {_cos(r.get('cos_half2'))}")
        bits += [f"evidence: {_text(r.get('evidence')) or '-'}", f"fdr {_q(r.get('fdr'))}"]
        rk = [f"{lb} is {la}'s partner #{r['rank_ab']}" if r.get("rank_ab") else
              f"{lb} is not among {la}'s 100 strongest partners",
              f"{la} is {lb}'s partner #{r['rank_ba']}" if r.get("rank_ba") else
              f"{la} is not among {lb}'s 100 strongest partners"]
        P.append("- " + "; ".join(bits))
        P.append("- " + "; ".join(rk))
        if r.get("source") == "relations":
            gen, known = _gene_flags(r, C.o.novelty()[0])
            if gen:
                P.append(f"- genomic: {gen}")
            if C.loaded("string_links", "hallmark", "reactome", "hgnc"):
                P.append(f"- known: {known or 'no STRING link (>= 400), shared group or pathway recorded'}")
            else:
                P.append("- known: not assessed (reference annotations not loaded for this run)")
    sk = C.string_known() if C.loaded("string_links") else None
    if sk is not None and not (r is not None and r.get("source") == "relations"):
        a, b, sc = sk
        lo, hi = np.searchsorted(a, ca, "left"), np.searchsorted(a, ca, "right")
        s = [int(x) for p, x in zip(b[lo:hi], sc[lo:hi]) if int(p) == cb]
        if s:
            P.append(f"- STRING combined score {s[0]} (>= {KNOWN_STRING})")
    de = o.pq("tables/drug_effects.parquet", columns=["col", "drug", "dose", "z", "q_up", "q_down", "lfc", "clean",
                                                      "flags", "cc_share"],
              filters=[("col", "in", [ca, cb])])
    de = de[((de["q_up"] < Q_CUT) & (de["lfc"] >= LFC_MIN)) | ((de["q_down"] < Q_CUT) & (de["lfc"] <= -LFC_MIN))]
    de = de.assign(alert=[_row_alert(f, bool(cl), s) for f, cl, s in
                          zip(de["flags"].fillna("").astype(str) if "flags" in de else [""] * len(de), de["clean"],
                              de["cc_share"] if "cc_share" in de else [np.nan] * len(de))])
    A_ = de[de["col"] == ca].set_index(["drug", "dose"])
    B_ = de[de["col"] == cb].set_index(["drug", "dose"])
    both = A_.index.intersection(B_.index)
    same = [k for k in both if np.sign(A_.at[k, "z"]) == np.sign(B_.at[k, "z"])]
    opp = [k for k in both if np.sign(A_.at[k, "z"]) != np.sign(B_.at[k, "z"])]

    def n_al(x):
        return int((x["alert"] != "").sum())
    n_al_shared = {w: sum(bool(A_.at[k, "alert"] or B_.at[k, "alert"]) for k in ks)
                   for w, ks in (("same", same), ("opp", opp))}
    P.append(f"- significant drug-doses: {len(A_)} for {la} ({n_al(A_)} with an alert {Q.ALERT}), {len(B_)} for {lb} "
             f"({n_al(B_)} with an alert); shared: {len(same)} same direction ({n_al_shared['same']} with an alert "
             f"for either gene), {len(opp)} opposite ({n_al_shared['opp']} with an alert)")

    def one(k):
        al = "; ".join(f"{g_}: {x}" for g_, x in ((la, A_.at[k, "alert"]), (lb, B_.at[k, "alert"])) if x)
        return f"{k[0]} {k[1]} uM ({_z(A_.at[k, 'z'])} / {_z(B_.at[k, 'z'])}{', ' + Q.ALERT + ' ' + al if al else ''})"
    for word, ks in (("same direction", same), ("opposite", opp)):
        if ks:
            ks = sorted(ks, key=lambda k: -min(abs(A_.at[k, "z"]), abs(B_.at[k, "z"])))
            pos = Q._capped(len(ks), 8, [not (A_.at[k, "alert"] or B_.at[k, "alert"]) for k in ks])
            P.append(f"  - {word}: " + "; ".join(one(ks[i]) for i in pos)
                     + (f" ... {len(ks) - len(pos)} more" if len(ks) > len(pos) else ""))
    dv, why = _direction(C)
    if dv is None:
        P.append("- probable direction: " + ("the direction stage has not run for this output" if not why else
                                             f"the direction stage's files cannot be read ({why})"))
    else:
        both = []
        for x, y, lx, ly in ((ca, cb, la, lb), (cb, ca, lb, la)):
            d = dv.downstream(int(x))
            d = d[d["target_col"].to_numpy() == int(y)]
            both.append(d)
            P.append(f"- probable direction {DV.arrow(lx, ly)}: " + (
                "; ".join(DV.edge_line(r, alerts="long", max_names=4) for _, r in d.iterrows()) or "none"))
        P += _dir_pair_tail(pd.concat(both) if any(len(d) for d in both) else both[0])
        P.append(f"- ({DV.CAVEAT_SHORT}; the sign is what the source's activity probably does to the target. "
                 f"{DV.SIGN_RESPONSE_NOTE})")
    return "\n".join(P) + "\n"


def write_text(path, text):
    """Atomic text write (dry runs: the dossiers go to OUT/review/dry_run/)."""
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        fh.write(text)
    replace_file(tmp, path)


def to_json(d):
    """The dossier as a JSON-serialisable dict (text + data)."""
    return {"kind": d.kind, "name": d.name, "entity_id": d.entity_id, "sha256": d.sha256, "text": d.text,
            "data": json.loads(json.dumps(d.data, default=str))}
