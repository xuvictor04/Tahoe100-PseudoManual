"""query - the look-ups of a finished run, answered as plain text (no colours, 80-120 columns, aligned tables).

    tahoe gene SYMBOL     what the gene is (reference annotation, module and arm of the nodal map), the drug-doses
                          that raise it and lower it (pooled over the cell lines: fold, z, q, lines that move / lines
                          measured, dose pattern, alert, soft caveats), the cell lines where drug-doses move it most
                          (with each line's strongest drug-dose), the genes that move with it and opposite to it (cos,
                          evidence, fdr, locus / read-through / known / novel), and where the full tables are
    tahoe drug NAME       targets and mechanism; per dose: wells, flags, genes up / down, top genes up / down; the
                          drugs with the most similar vector, the modules it moves, the lines it depletes and the
                          lines that show its response most. NAME is case-insensitive; a salt form can be left out
                          ('Doxorubicin' = 'Doxorubicin (hydrochloride)'); a part of a name lists the matches
    tahoe line NAME       organ, drivers, TP53 status; genes specifically high (and low) at baseline; drug-doses
                          that deplete it; its strongest responses. NAME = cell name or Cellosaurus id
    tahoe pair A B        the two genes' cosine, its two compound halves, evidence, fdr, known / novel flags and
                          genomic distance; the drug-doses that move both (same / opposite direction); how far the
                          two agree inside each cell line
    tahoe module N        size, arms, label (validation stage), top genes per arm, top drug-doses up / down and the
                          lines where it responds most

Alerts, not removal. An item with a reason for doubt - an artifact flag of the drug-dose for that gene (toxic,
transcription drop, cell-cycle shift where it explains the change, unreliable plate only, position not correctable,
position correction uncertain, wells disagree), a relation seen in one random half of the compounds only or in
neither, two partners next to each other on the genome (locus, read-through), a gene outside the vector space or in it
only through flagged drug-doses, a noise-class RNA or a level that is only ambient RNA, a drug vector from few
significant genes or a flagged dose - stays in its ranked place with an alert: ALERT ('⚠') and the reason in plain
words (for a cell-cycle shift, the share of this change it would explain: tables cc_share). Counts say how many items
there are in all and how many carry an alert. A list capped at N shows the N strongest overall and also any of the N
strongest without an alert that would fall outside them, all in rank order (_capped), so flagged items never push
clean ones out of view. Estimates (correlations, the module's main drug-doses for 'follows') may still leave flagged
drug-doses out; where they do, the text says so.

Nothing is computed afresh that a stage already wrote: the look-ups read OUT/tables, OUT/embed, OUT/relations,
OUT/graph, OUT/reference and OUT/validation (each optional where the answer can do without it; a missing stage is
named with the command that makes it; a column an older stage version did not write is done without), plus a few
columns of the atlas matrices (atlas/effects DD_z, DD_lfc, DD_posunc, DD_A, DD_Az, DD_beta, line_cpm, expr_mask),
tensor/line_measured.npy, and two genes' rows of tensor/DDL_lfc for `pair`. Every read is a filtered
parquet read or a memory-mapped slice: one look-up stays well under 1 GB at full scale. Unknown names get close matches
(difflib). Nothing is written.

An answer states the stages' own rules, never more: per-line counts and 'strongest' use the per-line |z| cut the
tables stage calibrated (tables/info.json, with the expected chance calls); 'both' halves = same sign with fdr <=
0.10 in two random halves of the compounds, 'one' = strong in one random half only (not replicated, no error
estimate); NOVEL only when relations/info.json says novelty could be assessed (else which sources were missing); a
gene outside the vector space gets the embed stage's rule with its counts (embed/info.json); a module's arms are
called opposite only when graph/modules.parquet says so (arms_opposite); pooled = median over the cell lines; the
gene-level flags of a drug-dose (the cell-cycle rule included) are the tables stage's (tables.cc_rule where `pair`
needs them for a drug-dose that drug_effects does not list).
"""

import difflib
import errno
import glob
import json
import os
import re
import shutil
import sys
import textwrap
import warnings

import numpy as np
import pandas as pd

from . import atlas_core as A
from . import tables as TB
from . import tlib as T
from .common import read_effects_index, safe_filename
from .relations import REPRO_FDR             # evidence 'both halves' needs fdr <= this

WIDTH = 118                 # set from the terminal in main(): 80..120 columns
LFC_MIN = A.LFC_MIN
Q_CUT = A.Q_CUT
PAIR_Z = 2.0                # pair: a drug-dose "moves" a gene at pooled |z| >= this
PAIR_MIN_N = 5              # pair: a per-line correlation needs this many active drug-doses measured in both
DEPLETE_Z = -3.0            # DD_Az <= this: the drug-dose depletes the line (as tables.lines.n_dd_depleted)
LINE_Z_FALLBACK = 4.0       # per-line |z| cut when tables/info.json has none (older tables stage: not calibrated)
SHORT_POOLED = 3            # gene: fewer clean significant pooled drug-doses than this -> also the single-line view
SPECIFIC_MIN_CPM = 10.0     # line: genes specifically high need at least this level in the line
UNTRUSTED = ("unreliable plate only", "position not correctable", "wells disagree")   # embed's rule
_TAG = re.compile(r"^\s*\[[^\]]{1,80}\]:\s*")    # UniProt isoform tag before a FUNCTION text ('[Isoform 2]: ')
ALERT = "\u26a0"            # the alert sign: an item kept in its place although there is a reason to doubt it
ALERT_ASCII = "!"           # what it becomes on a console that cannot show it (_emit; one character, so that
                            # tables stay aligned)

# the file whose presence says a stage has run (look-ups must not depend on stage stamps: an output folder can be
# assembled from finished stage folders)
STAGE_FILE = {"effects": "atlas/effects/drugdose.csv", "tensor": "tensor/DDL_lfc.npy",
              "tables": "tables/genes.parquet", "embed": "embed/gene_unit.npy",
              "reference": "reference/annotations.parquet", "relations": "relations/gene_relations.parquet",
              "graph": "graph/nodes.parquet", "validate": "validation/module_labels.csv", "vault": "vault",
              "map": "map/gene_map.html"}


class Missing(Exception):
    """A stage the answer needs has not run."""


class NotFound(Exception):
    """A name that matches nothing (the message holds the suggestions)."""


# ----------------------------------------------------------------------------- formatting
def _s(v, na="-"):
    if v is None:
        return na
    if isinstance(v, float) and not np.isfinite(v):
        return na
    s = str(v)
    return na if s in ("nan", "None", "<NA>") else s


def _num(x):
    try:
        x = float(x)
    except (TypeError, ValueError):
        return float("nan")
    return x


def _f(x, fmt="{:.2f}", na="-"):
    x = _num(x)
    return na if not np.isfinite(x) else fmt.format(x)


def _fold(x, na="-"):
    x = _num(x)
    if not np.isfinite(x):
        return na
    return f"{x:.1f}x" if x >= 10 else f"{x:.2f}x"


def _q(x, na="-"):
    x = _num(x)
    if not np.isfinite(x):
        return na
    if x < 1e-3:
        return f"{x:.0e}"
    return f"{x:.3f}"


def _z(x):
    return _f(x, "{:+.1f}")


def _cos(x):
    return _f(x, "{:+.2f}")


def _int(x, na="-"):
    x = _num(x)
    return na if not np.isfinite(x) else f"{int(round(x)):,}"


def _cut(s, n):
    s = str(s)
    if n <= 0:
        return ""
    if len(s) <= n:
        return s
    return s[:max(1, n - 3)] + "..." if n > 3 else s[:n]


def _text(v):
    """A text cell: '' for missing values."""
    s = _s(v, "")
    return s.strip()


def _wrap(text, indent=2, sub=None, max_lines=None):
    sub = indent if sub is None else sub
    lines = textwrap.wrap(str(text), width=WIDTH, initial_indent=" " * indent, subsequent_indent=" " * sub,
                          break_on_hyphens=False) or [""]
    if max_lines and len(lines) > max_lines:
        lines = lines[:max_lines]
        last = _cut(lines[-1], WIDTH - 4)
        lines[-1] = last if last.endswith("...") else last + " ..."
    return lines


def _table(head, rows, align, flex=(), indent=2, gap=2, mins=None, drop=()):
    """Aligned columns ('l' / 'r' per column); columns in `flex` shrink (widest first, not below `mins`) to keep
    within WIDTH; columns in `drop` are left out, in that order, while the table cannot fit otherwise."""
    rows = [[_s(v, "-") if not isinstance(v, str) else v for v in r] for r in rows]
    mins = dict(mins or {})
    keep = list(range(len(head)))
    for dcol in drop:
        w = {i: max([len(head[i])] + [len(r[i]) for r in rows]) for i in keep}
        need = indent + gap * (len(keep) - 1) + sum(min(w[i], max(len(head[i]), mins.get(i, 8))) if i in flex
                                                    else w[i] for i in keep)
        if need <= WIDTH:
            break
        keep.remove(dcol)
    if len(keep) < len(head):
        head = [head[i] for i in keep]
        align = "".join(align[i] for i in keep)
        rows = [[r[i] for i in keep] for r in rows]
        pos = {c: j for j, c in enumerate(keep)}
        flex = [pos[i] for i in flex if i in pos]
        mins = {pos[i]: v for i, v in mins.items() if i in pos}
    n = len(head)
    w = [max([len(head[i])] + [len(r[i]) for r in rows]) for i in range(n)]
    over = indent + sum(w) + gap * (n - 1) - WIDTH
    floor = {i: max(len(head[i]), mins.get(i, 8)) for i in flex}
    while over > 0:                              # water-filling: always trim the widest flexible column
        cand = [i for i in flex if w[i] > floor[i]]
        if not cand:
            break
        i = max(cand, key=lambda j: w[j])
        w[i] -= 1
        over -= 1

    def line(cells):
        parts = []
        for i, v in enumerate(cells):
            v = _cut(v, w[i])
            parts.append(v.rjust(w[i]) if align[i] == "r" else v.ljust(w[i]))
        return (" " * indent + (" " * gap).join(parts)).rstrip()
    out = [line(head), " " * indent + "-" * (sum(w) + gap * (n - 1))]
    out += [line(r) for r in rows]
    return out


def _title(P, title, note=""):
    P.append("")
    if note:
        P += _wrap(f"{title}  ({note})", indent=0, sub=2)
    else:
        P.append(title)


def _artifacts(flags):
    """Only the artifact flags of a flags string (the soft caveats left out)."""
    fl = [f for f in str(flags or "").split("; ") if f]
    return "; ".join(f for f in fl if f in A.ARTIFACT_FLAGS)


CC_WORDS = {"full": "cell-cycle shift, explains ~{p}% of this change", "table": "cell-cycle shift, explains ~{p}%",
            "short": "cell cycle ~{p}%"}       # the cell-cycle alert with the share of the change it would explain


def _alert(flags, cc_share=None, words="full"):
    """The reason for an item's alert in plain words: its artifact flags ('' = no alert); a cell-cycle shift with the
    share of this change it would explain (tables cc_share). words: 'full' (sentences), 'table' (an alert column),
    'short' (narrow side-by-side tables: 'cell cycle ~87%', 'position uncertain')."""
    out = []
    for f in str(flags or "").split("; "):
        if f not in A.ARTIFACT_FLAGS:
            continue
        if f == TB.CC_FLAG:
            sh = _num(cc_share)
            f = CC_WORDS[words].format(p=int(round(100 * sh))) if np.isfinite(sh) else \
                ("cell cycle" if words == "short" else TB.CC_FLAG)
        elif words == "short" and f == "position correction uncertain":
            f = "position uncertain"
        out.append(f)
    return "; ".join(out)


def _alert_cell(flags, cc_share=None, words="table", none=""):
    """An alert column's cell: ALERT + the reason, or `none`."""
    a = _alert(flags, cc_share, words)
    return f"{ALERT} {a}" if a else none


def _caveats(flags):
    """The flags that are no artifact flag: soft caveats, and a cell-cycle shift that is not the explanation."""
    return "; ".join(f for f in str(flags or "").split("; ") if f and f not in A.ARTIFACT_FLAGS)


def _flags_shown(flags, cc_share=None, none="-"):
    """A flags cell: the alert first (ALERT + artifact flags in plain words), then the soft caveats."""
    a, c = _alert(flags, cc_share, "table"), _caveats(flags)
    if a:
        return f"{ALERT} {a}" + (f"; {c}" if c else "")
    return c or none


def _capped(n, top, ok):
    """Positions to show of a ranked list of n items (strongest first) capped at top: the top strongest overall plus
    any of the top strongest without an alert (ok True) that would fall outside them, in rank order. Flagged items
    thus never push clean ones out of view."""
    ok = np.asarray(ok, dtype=bool)[:n]
    keep = np.arange(n) < top
    keep[np.flatnonzero(ok)[:top]] = True
    return np.flatnonzero(keep)


def _more(n, shown, n_alert_rest, what="", opt=" (--top)"):
    """'... k more[ what] (j of them with an alert)' for the items a capped list leaves out ('' when none)."""
    k = n - shown
    if k <= 0:
        return ""
    return (f"  ... {k} more" + (f" {what}" if what else "") + (f" ({n_alert_rest} of them with an alert)"
                                                                 if n_alert_rest else "") + opt)


def _n_alert(n, n_alert, what=""):
    """'N[ what], k of them with an alert' - the counts of a list ('0[ what]' for an empty one)."""
    if n == 1 and what.endswith("s") and not what.endswith("ss"):
        what = what[:-1]
    return f"{n}{' ' + what if what else ''}" + (f", {n_alert} of them with an alert ({ALERT})" if n else "")


def _norm(s):
    return re.sub(r"[^a-z0-9]", "", str(s).lower())


def _suggest(name, choices, n=6, cutoff=0.6, key=str.upper):
    """Close matches of name among choices (difflib on the key form), original spellings."""
    m = {}
    for c in choices:
        m.setdefault(key(c), c)
    hits = difflib.get_close_matches(key(name), list(m), n=n, cutoff=cutoff)
    return [m[h] for h in hits]


# ----------------------------------------------------------------------------- the run's files
class Out:
    """Lazy, cached access to one output folder."""

    def __init__(self, out, data=None):
        self.out = out
        self.data = data
        self._c = {}

    def p(self, *parts):
        return os.path.join(self.out, *parts)

    def has(self, rel):
        return os.path.exists(self.p(rel))

    def ran(self, stage):
        return self.has(STAGE_FILE[stage])

    def how(self, stage):
        cmd = f"python -m tahoemap run --out {self.out}" + (f" --data {self.data}" if self.data else "")
        extra = ""
        if stage == "reference":
            extra = (" The reference stage downloads public annotations (network; optional, skipped with --offline): "
                     "`tahoe run --from reference` with network access.")
        return (f"Run it with `tahoe run` (every missing stage in order; or: {cmd}); `tahoe status` shows what is "
                f"done." + extra)

    def missing_note(self, stage, what=""):
        cmd = "tahoe run --from reference` with network access (optional)" if stage == "reference" else \
            "tahoe run` makes it"
        return f"[{what or stage}: the {stage} stage has not run here; `{cmd}]"

    def require(self, *stages):
        for s in stages:
            if not self.ran(s):
                raise Missing(f"The {s} stage has not run for {self.out} (no {STAGE_FILE[s]}).\n"
                              + "\n".join(_wrap(self.how(s), indent=0)))

    def _cached(self, key, fn):
        if key not in self._c:
            self._c[key] = fn()
        return self._c[key]

    def pq(self, rel, columns=None, filters=None):
        """A parquet table (whole tables cached; filtered reads are not)."""
        path = self.p(rel)
        if columns:                              # tolerate a column an older stage version did not write
            import pyarrow.parquet as pq
            have = set(pq.ParquetFile(path).schema_arrow.names)
            columns = [c for c in columns if c in have]
        if filters is not None:
            return pd.read_parquet(path, columns=columns, filters=filters)
        return self._cached(("pq", rel, tuple(columns) if columns else None),
                            lambda: pd.read_parquet(path, columns=columns))

    def npy(self, rel):
        return self._cached(("npy", rel), lambda: np.load(self.p(rel), mmap_mode="r"))

    def ix(self):
        return self._cached("ix", lambda: read_effects_index(self.p("atlas", "effects")))

    # --- index tables
    def genes(self):
        def load():
            if self.ran("tables"):
                g = pd.read_parquet(self.p("tables", "genes.parquet"))
            else:
                g = self.ix()["genes"]
                g = g[g["kind"] == "gene"].copy()
                g["col"] = np.arange(len(g))
            for c in ("symbol", "label"):
                g[c] = g[c].fillna("").astype(str)
            g["ensembl_id"] = g["ensembl_id"].fillna("").astype(str) if "ensembl_id" in g else ""
            return g.set_index("col", drop=False)
        return self._cached("genes", load)

    def ann(self):
        if not self.ran("reference"):
            return None
        cols = ["col", "symbol", "hgnc_id", "hgnc_symbol", "name", "locus_type", "location", "chrom", "start",
                "end", "strand", "biotype", "aliases", "prev_symbols", "protein_name", "function", "ncbi_summary",
                "matched_by"]

        return self._cached("ann", lambda: self.pq("reference/annotations.parquet", columns=cols).set_index(
            "col", drop=False))

    def ann_name(self, c):
        a = self.ann()
        if a is None or c not in a.index or "name" not in a:
            return ""
        return _text(a.at[c, "name"])

    def lines(self):
        def load():
            if self.ran("tables") and self.has("tables/lines.parquet"):
                ln = pd.read_parquet(self.p("tables", "lines.parquet"))
            else:
                ln = self.ix()["lines"].copy()
            ln = ln.reset_index(drop=True)
            ln["line"] = np.arange(len(ln))
            ln["name"] = ln["cell_name"].where(ln["cell_name"].notna(), ln["cell_line_id"]).astype(str)
            return ln
        return self._cached("lines", load)

    def drugdoses(self):
        def load():
            if self.has("tables/drugdoses.parquet"):
                d = pd.read_parquet(self.p("tables", "drugdoses.parquet"))
            else:
                d = self.ix()["drugdose"].copy()
                d["dd"] = np.arange(len(d))
                d["salt_base"] = [T.salt_base(x) for x in d["drug"]]
            d = d.reset_index(drop=True)
            d["flags"] = d["flags"].fillna("").astype(str)
            d["drug"] = d["drug"].fillna("").astype(str)
            d["dose"] = d["dose"].fillna("").astype(str)
            d["artifact"] = [A.has_artifact(f) for f in d["flags"]]
            d["label"] = d["drug"] + " " + d["dose"]
            return d
        return self._cached("drugdoses", load)

    def active_dd(self):
        """Active, trustworthy drug-doses (embed's contexts), as a boolean over dd."""
        def load():
            dd = self.drugdoses()
            if self.has("embed/drugdoses.parquet"):
                e = pd.read_parquet(self.p("embed", "drugdoses.parquet"), columns=["dd", "active_context"])
                act = np.zeros(len(dd), dtype=bool)
                act[e["dd"].to_numpy()[e["active_context"].to_numpy().astype(bool)]] = True
                return act
            bad = np.array([any(u in f.split("; ") for u in UNTRUSTED) for f in dd["flags"]])
            return (dd["n_sig_genes"].to_numpy() >= self.embed_info().get("min_active", 10)) & ~bad
        return self._cached("active", load)

    def flagged_only(self):
        """Gene cols in the vector space only through significant pooled drug-doses that carry an alert (embed
        genes.parquet evidence_flagged_only; empty when an older embed stage did not write it)."""
        def load():
            if not self.has("embed/genes.parquet"):
                return frozenset()
            eg = self.pq("embed/genes.parquet", columns=["col", "evidence_flagged_only"])
            if "evidence_flagged_only" not in eg:
                return frozenset()
            return frozenset(int(c) for c in eg.loc[eg["evidence_flagged_only"].fillna(False).astype(bool), "col"])
        return self._cached("flagged_only", load)

    def embed_info(self):
        def load():
            p = self.p("embed", "info.json")
            if os.path.exists(p):
                with open(p, encoding="utf-8") as fh:
                    return json.load(fh)
            return {}
        return self._cached("embed_info", load)

    def _info(self, rel):
        def load():
            p = self.p(rel)
            if os.path.exists(p):
                try:
                    with open(p, encoding="utf-8") as fh:
                        return json.load(fh) or {}
                except (OSError, ValueError):
                    return {}
            return {}
        return self._cached(("info", rel), load)

    def line_cut(self):
        """(t, expected chance calls per gene x line or None, calibrated?): the tables stage's per-line |z| cut."""
        ti = self._info("tables/info.json")
        t = _num(ti.get("line_z_threshold"))
        ch = _num(ti.get("line_z_expected_chance"))
        if np.isfinite(t):
            return t, (ch if np.isfinite(ch) else None), True
        return LINE_Z_FALLBACK, None, False

    def line_cut_note(self):
        t, ch, cal = self.line_cut()
        if not cal:
            return "not calibrated in this run: a per-line z of 4-5 can arise by chance"
        return "calibrated on this run" + (f": about {ch:.2g} chance calls expected per gene and line"
                                           if ch is not None else "")

    def line_cut_text(self):
        return f"per-line |z| >= {self.line_cut()[0]:.1f} ({self.line_cut_note()})"

    def novelty(self):
        """(assessed?, missing sources) from relations/info.json; older runs: assessed when reference ran."""
        ri = self._info("relations/info.json")
        if "novel_assessed" in ri:
            return bool(ri["novel_assessed"]), [str(x) for x in ri.get("novel_blocked_by") or []]
        ok = self.ran("reference")
        return ok, ([] if ok else ["the reference stage"])

    def module_arms(self, m):
        """(arms opposite?, mean cos between the sides) of module m (graph/modules.parquet)."""
        mods = self.modules()
        if mods is None or not (mods["module"] == m).any():
            return False, float("nan")
        r = mods[mods["module"] == m].iloc[0]
        opp = bool(r["arms_opposite"]) if "arms_opposite" in r and r["arms_opposite"] is not None else \
            int(r.get("n_minus", 0)) > 0
        return opp, _num(r.get("mean_cos_between_arms"))

    def arms_text(self, m):
        opp, b = self.module_arms(m)
        if opp:
            return f"the + arm and the - arm move in opposite directions under the same drugs (mean cos between them " \
                   f"{_cos(b)})"
        if not np.isfinite(b):
            return "single-armed: all its genes lie on one side of its main direction"
        return (f"single-armed: the two sides of its main direction are not two opposite arms (mean cos between them "
                f"{_cos(b)}; a - arm needs >= 5 genes on its side and <= -0.2), so all its genes count as +")

    def measured(self):
        """lines x genes: the line truly expresses the gene (tensor/line_measured.npy; else the atlas expr_mask)."""
        if self.has("tensor/line_measured.npy"):
            return self.npy("tensor/line_measured.npy")
        return self.eff("expr_mask")

    def nodes(self):
        if not self.ran("graph"):
            return None
        return self._cached("nodes", lambda: pd.read_parquet(self.p("graph", "nodes.parquet")).set_index(
            "col", drop=False))

    def modules(self):
        if not self.has("graph/modules.parquet"):
            return None
        return self._cached("modules", lambda: pd.read_parquet(self.p("graph", "modules.parquet")).reset_index(
            drop=True))

    def labels(self):
        """module -> row of validation/module_labels.csv (or None)."""
        if not self.ran("validate"):
            return None

        def load():
            t = pd.read_csv(self.p("validation", "module_labels.csv"))
            return t.set_index("module", drop=False) if "module" in t else None
        return self._cached("labels", load)

    def module_label(self, m, set_only=False):
        """validation/module_labels.csv label; else (unless set_only) the module's top genes."""
        lab = self.labels()
        if lab is not None and m in lab.index and "label" in lab and _text(lab.at[m, "label"]):
            src = _text(lab.at[m, "label_source"]) if "label_source" in lab else "set"
            if not set_only or src not in ("", "top genes"):
                return _text(lab.at[m, "label"])
        if set_only:
            return ""
        mods = self.modules()
        if mods is not None:
            r = mods[mods["module"] == m]
            if len(r):
                tp = _text(r.iloc[0]["top_plus"]).split(", ")[:3]
                tm = _text(r.iloc[0]["top_minus"]).split(", ")[:2]
                return "genes: " + ", ".join([x for x in tp + tm if x])
        return ""

    def eff(self, name):
        return self.npy(f"atlas/effects/{name}.npy")


# ----------------------------------------------------------------------------- name resolution
def resolve_gene(o, name):
    """Gene cols for a name: label, symbol (case-insensitive), Ensembl id, previous symbol, alias. Returns
    (cols, how); raises NotFound with suggestions."""
    g = o.genes()
    key = name.strip().strip(",;")
    hit = g.index[g["label"] == key]
    if len(hit):
        return list(hit), ""
    up = key.upper()

    def sym_index():
        d = {}
        for c, s in zip(g["col"].to_numpy(), g["symbol"].str.upper().to_numpy()):
            d.setdefault(s, []).append(int(c))
        return d
    sx = o._cached("sym_index", sym_index)
    if up in sx:
        return sx[up], ""
    if up.startswith("ENSG"):
        e = g["ensembl_id"].str.upper().str.split(".").str[0]
        hit = g.index[e == up.split(".")[0]]
        if len(hit):
            return list(hit), f"{key} is the Ensembl id of {g.at[hit[0], 'label']}"
    ann = o.ann()
    if ann is not None:
        def alias_index():
            d = {}
            for kind in ("prev_symbols", "aliases"):
                if kind not in ann:
                    continue
                for c, s in zip(ann["col"].to_numpy(), ann[kind].fillna("").astype(str).to_numpy()):
                    for x in s.split("|"):
                        x = x.strip().upper()
                        if x:
                            d.setdefault(x, []).append((int(c), "previous symbol" if kind == "prev_symbols"
                                                        else "alias"))
            if "hgnc_symbol" in ann:
                for c, s in zip(ann["col"].to_numpy(), ann["hgnc_symbol"].fillna("").astype(str).to_numpy()):
                    if s and s.upper() not in sx:
                        d.setdefault(s.upper(), []).insert(0, (int(c), "current HGNC symbol"))
            return d
        ax = o._cached("alias_index", alias_index)
        if up in ax:
            seen, cols, kinds = set(), [], []
            for c, kd in ax[up]:
                if c not in seen:
                    seen.add(c)
                    cols.append(c)
                    kinds.append(kd)
            how = f"{key} is the {kinds[0]} of {g.at[cols[0], 'label']} (HGNC)"
            if len(cols) > 1:
                how += "; it also names " + ", ".join(g.at[c, "label"] for c in cols[1:6])
            return cols, how
    sug = _suggest(key, g["label"].tolist(), n=8, cutoff=0.75)
    raise NotFound(f"No gene '{key}' in this run (symbol, label, Ensembl id"
                   + (", previous symbol or alias" if ann is not None else "") + ")."
                   + (" Close matches: " + ", ".join(sug) if sug else ""))


def resolve_drug(o, name):
    """Drug names for a query: exact (case-insensitive), then the salt-free name, then a part of a name."""
    dd = o.drugdoses()
    names = sorted(dd["drug"].unique(), key=str.lower)
    q = name.strip()
    low = q.lower()
    exact = [d for d in names if d.lower() == low]
    if exact:
        return exact
    base = T.salt_base(q).lower()
    salt = [d for d in names if T.salt_base(d).lower() in (low, base)]
    if salt:
        return salt
    nq = _norm(q)
    norm = [d for d in names if _norm(d) == nq or _norm(T.salt_base(d)) == nq]
    if norm:
        return norm
    sub = [d for d in names if low in d.lower() or (nq and nq in _norm(d))]
    if len(sub) == 1:
        return sub
    if len(sub) > 1:
        more = f" and {len(sub) - 5} more" if len(sub) > 5 else ""
        raise NotFound(f"'{q}' is part of {len(sub)} drug names: " + "; ".join(sub[:5]) + more
                       + ". Ask for one of them (quote names with spaces).")
    sug = _suggest(q, names, n=6, cutoff=0.6, key=str.lower)
    sug += [d for d in _suggest(q, [T.salt_base(x) for x in names], n=6, cutoff=0.6, key=str.lower)
            if d not in sug]
    raise NotFound(f"No drug '{q}' in this run." + (" Close matches: " + "; ".join(sug[:6]) if sug else ""))


def resolve_line(o, name):
    ln = o.lines()
    q = name.strip()
    nq = _norm(q)
    for c in ("cell_name", "cell_line_id", "Cell_ID_DepMap"):
        if c in ln:
            hit = ln.index[ln[c].fillna("").astype(str).str.lower() == q.lower()]
            if len(hit):
                return int(hit[0])
    for c in ("cell_name", "cell_line_id", "Cell_ID_DepMap"):
        if c in ln:
            hit = ln.index[[_norm(x) == nq for x in ln[c].fillna("").astype(str)]]
            if len(hit):
                return int(hit[0])
    choices = ln["name"].tolist() + ln["cell_line_id"].astype(str).tolist()
    sug = _suggest(q, choices, n=6, cutoff=0.5, key=_norm)
    raise NotFound(f"No cell line '{q}' in this run (cell name or Cellosaurus id)."
                   + (" Close matches: " + ", ".join(sug) if sug else
                      " Lines: " + ", ".join(ln["name"].tolist()[:20]) + (" ..." if len(ln) > 20 else "")))


# ----------------------------------------------------------------------------- shared pieces
def _rel_flags(r, novel_ok=True):
    """A relation's flags; a reason to doubt that the two genes are linked in function (one locus: shared chromatin
    or read-through can make neighbours correlate) carries ALERT."""
    f = []
    if bool(r.get("locus", False)):
        d = _num(r.get("distance_bp"))
        f.append(f"{ALERT} locus" + (f" {d / 1000:.0f} kb" if np.isfinite(d) else ""))
    if bool(r.get("readthrough_risk", False)):
        f.append(f"{ALERT} readthrough?")
    if novel_ok and bool(r.get("novel_candidate", False)):
        f.append("NOVEL")
    known = []
    s = _num(r.get("string_score"))
    if np.isfinite(s):
        known.append(f"STRING {int(s)}")
    if bool(r.get("shared_gene_group", False)):
        known.append("same family")
    pw = _text(r.get("shared_pathway", ""))
    if pw:
        known.append(_cut(pw.replace("HALLMARK_", "H:"), 24))
    if known:
        f.append("known: " + ", ".join(known))
    return "; ".join(f)


def _module_arm(o, c):
    """(module, arm): arm is '' in module 0 and in a single-armed module (graph/modules.parquet arms_opposite)."""
    nd = o.nodes()
    if nd is None or c not in nd.index:
        return None, ""
    m = int(nd.at[c, "module"])
    return m, (_text(nd.at[c, "arm"]) if m > 0 and o.module_arms(m)[0] else "")


def _gene_module(o, c):
    m, arm = _module_arm(o, c)
    return "" if m is None else (f"{m}{arm}" if m > 0 else "0")


def _not_in_space(o, c):
    """Why a gene is not in the vector space."""
    if not o.has("embed/genes.parquet"):
        return "the embed stage has not run"
    eg = o.pq("embed/genes.parquet")
    r = eg[eg["col"] == c]
    if not len(r):
        return "not in embed/genes.parquet"
    r = r.iloc[0]
    if bool(r.get("included", False)):
        return ""
    if bool(r.get("noise_rna", False)):
        return "noise-class RNA (left out of the space)"
    ei = o.embed_info()
    need = int(ei.get("min_responsive", 5))
    n = int(r["n_responsive_contexts"]) if np.isfinite(_num(r.get("n_responsive_contexts"))) else 0
    nd = ei.get("drugdoses_active")
    txt = (f"it reaches per-line |z| >= 3 in {n} of the " +
           (f"{nd} active, trustworthy drug-doses x {ei.get('lines', len(o.lines()))} lines the space is built "
            f"from (drug-doses with >= {ei.get('min_active', 10)} significant genes, pooled or in single lines, and "
            f"no untrusted flag; {ei.get('contexts', '?')} of these contexts have data)" if nd is not None else
            "(drug-dose, line) contexts the space is built from"))
    if n < need:
        return txt + f"; the space needs {need}"
    lz = _num(ei.get("line_z_responsive"))
    # an embed stage that writes evidence_flagged_only counts flagged significant drug-doses too (with an alert)
    kind = "pooled drug-dose, flagged or not" if "evidence_flagged_only" in eg else "clean pooled drug-dose"
    txt += (f"; that count (>= {need}) is not enough on its own: the space also needs a significant {kind} "
            f"(q < {Q_CUT:g}, >= 1.2x)" +
            (f" or a per-line |z| >= {lz:.1f} in >= 2 lines of one trustworthy drug-dose" if np.isfinite(lz) else "")
            + ", and it has neither")
    if np.isfinite(_num(ei.get("null_rate"))):
        txt += f" (chance rate of |z| >= 3 per context {_num(ei['null_rate']):.2g})"
    if ei.get("n_genes_excluded_chance") is not None:
        txt += f"; {int(ei['n_genes_excluded_chance']):,} genes of this run reach the count without either"
    return txt


def _partner_alert(o, x):
    """True when a partner row carries an alert: not replicated in both random halves, or the partner is in the
    vector space only through flagged drug-doses."""
    return _text(x.get("evidence")) != "both halves" or int(x["col_b"]) in o.flagged_only()


def _partner_rows(o, rel, top, sign):
    """The partner table of one side (cos > 0 or < 0), strongest |cos| first, capped as _capped; returns (rows, the
    side's partners, how many of them carry an alert)."""
    r = rel[rel["cos"] > 0].sort_values("cos", ascending=False) if sign > 0 else \
        rel[rel["cos"] < 0].sort_values("cos")
    r = r.reset_index(drop=True)
    ok = np.array([not _partner_alert(o, x) for _, x in r.iterrows()], dtype=bool)
    fo = o.flagged_only()
    rows = []
    for i in _capped(len(r), top, ok):
        x = r.iloc[i]
        cb = int(x["col_b"])
        ev = _text(x.get("evidence"))
        rows.append([(o.genes().at[cb, "label"] if cb in o.genes().index else _text(x["symbol_b"]))
                     + (f" {ALERT}" if cb in fo else ""),
                     _cos(x["cos"]), f"{_cos(x.get('cos_half1'))}/{_cos(x.get('cos_half2'))}",
                     EVIDENCE_SHORT.get(ev, f"{ALERT} {ev}" if ev and ev != "both halves" else ev), _q(x.get("fdr")),
                     _gene_module(o, cb), _rel_flags(x, o.novelty()[0]),
                     o.ann_name(cb)])
    return rows, len(r), int((~ok).sum())


REL_COLS = ["col_a", "col_b", "symbol_b", "rank", "cos", "cos_half1", "cos_half2", "evidence", "fdr", "locus",
            "distance_bp", "readthrough_risk", "shared_gene_group", "shared_pathway", "string_score", "known",
            "novel_candidate"]
PARTNER_HEAD = ["gene", "cos", "halves 1/2", "repro", "fdr", "module", "flags", "name"]
EVIDENCE_SHORT = {"both halves": "both", "one half": f"{ALERT} one half", "not reproduced": f"{ALERT} not repro"}


def _where(o, P, tb):
    """The FULL TABLES block: paths relative to the output folder, which is named once."""
    _title(P, "FULL TABLES", f"under {o.out}")
    rows = []
    for what, path, key in tb:
        path, extra = path if isinstance(path, tuple) else (path, "")    # (path, text after it: not a path part)
        rel = os.path.relpath(path, o.out) if os.path.isabs(path) and path.startswith(o.out) else path
        rows.append([what, rel + extra, key])
    P += _table(["", "file", "rows"], rows, "lll", flex=(1, 2), mins={1: 24, 2: 10})


def _vault_note(o, folder_name, label):
    if not o.ran("vault"):
        return ""
    hits = glob.glob(o.p("vault", folder_name, "*", safe_filename(label) + ".md")) + \
        glob.glob(o.p("vault", folder_name, safe_filename(label) + ".md"))
    return hits[0] if hits else ""


def _single_lines(o, c, direction, k=3):
    """The single-line view of a gene: the drug-doses that pass the calibrated per-line cut in the most lines
    (tables/drug_line_top.parquet; flagged ones in their place with their alert, capped as _capped), as one sentence
    ('' when none). An older tables stage listed clean drug-doses only."""
    if not o.has("tables/drug_line_top.parquet"):
        return ""
    t = o.pq("tables/drug_line_top.parquet", filters=[("col", "==", int(c))],
             columns=["col", "direction", "dd", "drug", "dose", "cell_name", "lfc", "z", "flags", "clean", "cc_share"])
    t = t[t["direction"].astype(str) == direction]
    if not len(t):
        return ""
    older = "clean" not in t
    t = t.assign(az=t["z"].abs(), clean=True if older else t["clean"].astype(bool))
    t = t.sort_values("az", ascending=False)
    g = t.groupby("dd", sort=False)
    order = sorted(g.groups, key=lambda d: (-len(g.groups[d]), -float(g.get_group(d)["az"].max()), d))
    okd = [bool(g.get_group(d)["clean"].iloc[0]) for d in order]
    parts = []
    for i in _capped(len(order), k, okd):
        x = g.get_group(order[i])
        r0 = x.iloc[0]
        al = "" if okd[i] else _alert(r0.get("flags"), r0.get("cc_share"))
        cells = ", ".join(f"{_text(r['cell_name'])} {_fold(2 ** _num(r['lfc']))}" for _, r in x.head(4).iterrows())
        parts.append(f"{T.salt_base(_text(r0['drug']))} {_text(r0['dose'])} uM" + (f" ({ALERT} {al})" if al else "")
                     + f" in {len(x)} line{'s' if len(x) != 1 else ''} ({cells}{', ...' if len(x) > 4 else ''})")
    n_al = sum(not v for v in okd)
    what = (_n_alert(len(order), n_al, "drug-doses") if not older else
            f"{len(order)} clean drug-doses; an older tables stage left flagged ones out")
    return (f"in single lines, at per-line |z| >= {o.line_cut()[0]:.1f} ({o.line_cut_note()}; "
            f"tables/drug_line_top, {what}): " + ("raised by " if direction == "up" else "lowered by ")
            + "; ".join(parts))


# ----------------------------------------------------------------------------- gene
def gene_report(o, c, top, how=""):
    g = o.genes()
    gr = g.loc[c]
    lab = gr["label"]
    P = []
    ens = _text(gr.get("ensembl_id", ""))
    P.append(f"{lab}   gene col {c}" + (f"   {ens}" if ens else ""))
    if how:
        P.append(f"  ({how})")
    ann = o.ann()
    if ann is not None and c in ann.index:
        a = ann.loc[c]
        bits = []
        if _text(a.get("name")):
            bits.append(_text(a.get("name")))
        loc = _text(a.get("location"))
        st, en = _num(a.get("start")), _num(a.get("end"))
        ch = _text(a.get("chrom"))
        if ch and np.isfinite(st) and np.isfinite(en):
            loc = (loc + "  " if loc else "") + f"chr{ch}:{int(st):,}-{int(en):,} ({_text(a.get('strand')) or '?'})"
        if loc:
            bits.append(loc)
        bt = _text(a.get("biotype")) or _text(a.get("locus_type"))
        if bt:
            bits.append(bt)
        mb = _text(a.get("matched_by"))
        if _text(a.get("hgnc_id")):
            bits.append(f"{_text(a.get('hgnc_id'))}" + (" (matched by alias: tentative)" if mb == "alias_symbol"
                                                       else ""))
        elif mb == "none":
            bits.append("no HGNC record")
        if bits:
            P += _wrap(" | ".join(bits), indent=2, sub=4)
        al = [_text(a.get("aliases")).replace("|", ", "), _text(a.get("prev_symbols")).replace("|", ", ")]
        if al[0] or al[1]:
            P += _wrap("aliases: " + (al[0] or "-") + ("   previous symbols: " + al[1] if al[1] else ""), 2, 4)
        fn = _TAG.sub("", _text(a.get("function"))) or _text(a.get("ncbi_summary"))
        if fn:
            pn = _text(a.get("protein_name"))
            P += _wrap(("protein: " + pn + ". " if pn else "") + "function: " + fn, 2, 4, max_lines=3)
    elif ann is None:
        P.append("  " + o.missing_note("reference", "name, location and function"))
    lvl = (f"level: {_f(gr.get('pooled_cpm'), '{:,.1f}')} CPM pooled over every well and line, "
           f"{_f(gr.get('median_line_cpm'), '{:,.1f}')} CPM in the median line; expressed in "
           f"{_int(gr.get('n_lines_expressing'))} of {len(o.lines())} lines")
    P += _wrap(lvl, 2, 4)
    if "n_dd_up_clean" in gr:
        nu, nd, nuc, ndc = (int(gr[k]) for k in ("n_dd_up", "n_dd_down", "n_dd_up_clean", "n_dd_down_clean"))
        P += _wrap(f"significant drug-doses (q < {Q_CUT:g} and fold >= {2 ** LFC_MIN:.1f}x or <= "
                   f"1/{2 ** LFC_MIN:.1f}): {nu} raise it ({nu - nuc} of them with an alert {ALERT}: an artifact "
                   f"flag for this gene), {nd} lower it ({nd - ndc} with an alert)", 2, 4)
    if bool(gr.get("noise_rna", False)):
        P.append(f"  {ALERT} noise-class RNA (snoRNA / mitochondrial / pseudogene / ...): read its responses with care")
    for k, nm in (("corr_with_S", "S-phase"), ("corr_with_G2M", "G2/M")):
        r = _num(gr.get(k))
        if np.isfinite(r) and abs(r) >= 0.5:
            P.append(f"  tracks the {nm} programme across drug wells (r = {r:+.2f}): drugs that shift the cell cycle "
                     "move it")
    why = _not_in_space(o, c)
    nd = o.nodes()
    if not o.ran("embed"):
        P += _wrap(o.missing_note("embed", "vector space, module and arm"), 2, 4)
    elif why:
        P += _wrap(f"{ALERT} vector space / nodal map: not included - {why}", 2, 4)
    elif nd is not None and c in nd.index:
        m, arm = int(nd.at[c, "module"]), _text(nd.at[c, "arm"])
        if m > 0:
            mods = o.modules()
            mr = mods[mods["module"] == m].iloc[0] if mods is not None and (mods["module"] == m).any() else None
            opp, _b = o.module_arms(m)
            txt = f"nodal map: module {m}" + (f", arm {arm}" if opp else "")
            if mr is not None:
                txt += (f" ({int(mr['n_genes'])} genes: {int(mr['n_plus'])} +, {int(mr['n_minus'])} -)" if opp else
                        f" ({int(mr['n_genes'])} genes)")
            lb = o.module_label(m, set_only=True)
            if lb:
                txt += f"; label: {lb}"
            P += _wrap(txt + "; " + o.arms_text(m), 2, 4)
            if mr is not None:
                same = [x for x in _text(mr["top_plus" if arm == "+" else "top_minus"]).split(", ")
                        if x and x != gr["symbol"]]
                other = [x for x in _text(mr["top_minus" if arm == "+" else "top_plus"]).split(", ") if x]
                if same:
                    P += _wrap((f"its arm ({arm}): " if opp else "module genes: ") + ", ".join(same[:8]), 4, 6)
                if other and opp:
                    P += _wrap(f"opposite arm ({'-' if arm == '+' else '+'}, moves the other way): "
                               + ", ".join(other[:8]), 4, 6)
        else:
            P.append("  nodal map: in the vector space, not in a module (module 0)")
    elif nd is None:
        P.append("  " + o.missing_note("graph", "module and arm"))
    if not why and c in o.flagged_only():
        P += _wrap(f"{ALERT} in the vector space only through significant drug-doses that carry an alert (artifact "
                   "flags for this gene; embed evidence_flagged_only): its partners and module may reflect the "
                   "artifact", 2, 4)

    # drug-doses
    cols = ["dd", "drug", "dose", "lfc", "fold", "z", "q_up", "q_down", "flags", "clean", "n_lines_measured",
            "n_lines_up", "n_lines_down", "pattern_up", "pattern_down", "cc_share"]
    de = o.pq("tables/drug_effects.parquet", columns=cols, filters=[("col", "==", int(c))])
    de["flags"] = de["flags"].fillna("").astype(str)
    de["clean"] = de["clean"].astype(bool)
    if "cc_share" not in de:                     # an older tables stage
        de["cc_share"] = np.nan
    for sign, word in ((1, "RAISED BY"), (-1, "LOWERED BY")):
        sub = de[np.sign(de["z"]) == sign].sort_values("z", ascending=(sign < 0)).reset_index(drop=True)
        qc = "q_up" if sign > 0 else "q_down"
        sig = ((sub[qc] < Q_CUT) & (sign * sub["lfc"] >= LFC_MIN)).to_numpy()
        ok = sub["clean"].to_numpy()
        _title(P, f"{word} - every drug-dose, pooled over the cell lines (median); {ALERT} = an artifact flag for "
                  "this gene, kept in its ranked place",
               f"{_n_alert(len(sub), int((~ok).sum()), f'with |z| >= 3 or q < {Q_CUT:g}')}; {int(sig.sum())} "
               f"significant (*), {int((sig & ok).sum())} of them without an alert; a response in fewer than about "
               "half of the measured lines does not reach the pooled data")
        one = _single_lines(o, c, "up" if sign > 0 else "down") if int((sig & ok).sum()) < SHORT_POOLED else ""
        if not len(sub):
            P.append("  none")
            P += _wrap(one, 2, 4) if one else []
            continue
        show = _capped(len(sub), top, ok)
        rows = []
        for i in show:
            r = sub.iloc[i]
            nl = r["n_lines_up"] if sign > 0 else r["n_lines_down"]
            rows.append([str(i + 1), r["drug"], r["dose"], _fold(r["fold"]), _z(r["z"]),
                         _q(r[qc]) + ("*" if sig[i] else " "), f"{int(nl)}/{int(r['n_lines_measured'])}",
                         "" if ok[i] else _alert_cell(r["flags"], r["cc_share"], none=f"{ALERT} flagged"),
                         _text(r["pattern_up" if sign > 0 else "pattern_down"]), _caveats(r["flags"]) or "-"])
        if ok[show].all():                       # no alert among the rows shown: no alert column
            P += _table(["#", "drug", "uM", "fold", "z", "q", "lines", "dose pattern", "caveats"],
                        [r_[:7] + r_[8:] for r_ in rows], "rlrrrrrll", flex=(1, 7, 8), mins={1: 14, 7: 12, 8: 10})
        else:
            P += _table(["#", "drug", "uM", "fold", "z", "q", "lines", "alert", "dose pattern", "caveats"], rows,
                        "rlrrrrrlll", flex=(1, 8, 9), mins={1: 14, 8: 12, 9: 10}, drop=(8,))
        more = _more(len(sub), len(show), int((~ok).sum()) - int((~ok[show]).sum()))
        if more:
            P.append(more)
        if len(show) > top:
            P += _wrap(f"rows beyond #{top}: the strongest without an alert, shown so that flagged drug-doses do not "
                       "push them out", 2, 4)
        P += _wrap(one, 2, 4) if one else []

    # lines
    le = o.pq("tables/line_effects.parquet", filters=[("col", "==", int(c))])
    ln = o.lines()
    organ = dict(zip(ln["line"], ln["Organ"].fillna("").astype(str))) if "Organ" in ln else {}
    t_line = o.line_cut()[0]
    has_all = "n_dd_up_all" in le                # older tables: the clean drug-doses only
    sfx = "_all" if has_all else ""
    _title(P, f"IN WHICH CELL LINES - number of drug-doses moving it >= 1.5x at per-line |z| >= {t_line:.1f}, and "
              "the strongest of them in the line",
           f"the cut is {o.line_cut_note()}; flagged drug-doses are counted and shown in their place, {ALERT} = an "
           "artifact flag for this gene (reasons below); per-line fold change vs the same line's plate median, "
           "per-line z; salt form left out; - = none" + ("" if has_all else
                                                       "; an older tables stage counted clean drug-doses only"))
    if len(le):
        le = le.copy()
        le["n"] = le[f"n_dd_up{sfx}"].fillna(0) + le[f"n_dd_down{sfx}"].fillna(0)
        le["n_clean"] = le["n_dd_up"].fillna(0) + le["n_dd_down"].fillna(0)
        le["mz"] = np.fmax(le[f"best_up_z{sfx}"].abs(), le[f"best_down_z{sfx}"].abs())
        expd = le[le["expressed"].astype(bool)].sort_values(["n", "mz"], ascending=[False, False])
        rows, legend, n_extra = [], {}, 0

        def best(r, k, s_):
            """(cell text, fold, z, alert) of the strongest drug-dose of a line in direction k ('' when none)."""
            if not s_ * _num(r.get(f"best_{k}_z{sfx}")) >= t_line:
                return None
            al = "" if not has_all or bool(r.get(f"best_{k}_clean_all")) else \
                _alert(r.get(f"best_{k}_flags_all"), r.get(f"best_{k}_cc_share_all"))
            nm = f"{T.salt_base(_text(r[f'best_{k}_drug{sfx}']))} {_text(r[f'best_{k}_dose{sfx}'])}"
            if al:
                legend.setdefault(nm, al)
            return ((f"{ALERT} " if al else "") + nm, _fold(2 ** _num(r[f"best_{k}_lfc{sfx}"])),
                    _z(r[f"best_{k}_z{sfx}"]), al)

        def count(r, k):
            n, nc = (np.nan_to_num(_num(r.get(x))) for x in (f"n_dd_{k}{sfx}", f"n_dd_{k}"))
            return f"{int(n)}" + (f" ({int(n - nc)}{ALERT})" if has_all and n > nc else "")

        for _, r in expd.head(top).iterrows():
            row = [_text(r["cell_name"]) or _text(r["cell_line_id"]), organ.get(int(r["line"]), ""),
                   _f(r["baseline_cpm"], "{:,.0f}"), count(r, "up"), count(r, "down")]
            extra = ["", "", "", "", ""]
            need = False
            for k, s_ in (("up", 1), ("down", -1)):
                b = best(r, k, s_)
                row += list(b[:3]) if b else ["-", "", ""]
                cleanb = None
                if b and b[3] and s_ * _num(r.get(f"best_{k}_z")) >= t_line:      # the strongest has an alert: the
                    cleanb = (f"no alert: {T.salt_base(_text(r[f'best_{k}_drug']))} {_text(r[f'best_{k}_dose'])}",
                              _fold(2 ** _num(r[f"best_{k}_lfc"])), _z(r[f"best_{k}_z"]))   # strongest without one
                    need = True
                extra += list(cleanb) if cleanb else ["", "", ""]
            rows.append(row)
            if need:
                rows.append(extra)
                n_extra += 1
        P += _table(["line", "organ", "CPM", "up", "down", "strongest up", "fold", "z", "strongest down", "fold",
                     "z"], rows, "llrrrlrrlrr", flex=(1, 5, 8), mins={1: 6, 5: 14, 8: 14}, drop=(1, 2))
        if legend:
            P += _wrap(f"{ALERT} " + "; ".join(f"{k} uM: {v}" for k, v in legend.items()) + " (for this gene)"
                       + ("; a 'no alert' row under a line names its strongest drug-dose without an alert"
                          if n_extra else ""), 2, 4)
        nexp = le[~le["expressed"].astype(bool)]
        if len(nexp):
            P += _wrap("not measured (not expressed, or only ambient RNA: no per-line values): " +
                       ", ".join(nexp["cell_name"].fillna(nexp["cell_line_id"]).astype(str)), 2, 4)
        n_any = int((expd["n"] > 0).sum())
        P.append(f"  {n_any} of {len(expd)} measured lines have a drug-dose moving it >= 1.5x at per-line "
                 f"|z| >= {t_line:.1f}" + (f"; in {int((expd['n_clean'] > 0).sum())} of them a drug-dose without "
                                           "an alert does" if has_all else ""))
    else:
        P.append("  no rows")

    # partners
    if not o.ran("relations") or why:
        _title(P, "MOVES WITH / MOVES OPPOSITE - genes that go up and down with it, or the other way")
        P += _wrap(o.missing_note("relations", "partners") if not o.ran("relations") or not o.ran("embed") else
                   f"none: {lab} is not in the vector space ({why})", 2, 4)
    for sign, word in ((1, "MOVES WITH"), (-1, "MOVES OPPOSITE")):
        if not o.ran("relations") or why:
            break
        _title(P, f"{word} - " + ("goes up and down together with it" if sign > 0 else
                                  "goes down when it goes up, and vice versa"),
               ("cos of the gene vectors; halves = the same in two random halves of the compounds (a hash split of "
                f"the compound names); repro: both = same sign with fdr <= {REPRO_FDR:g} in both halves, {ALERT} one "
                "half = strong in one of the two random halves only (not replicated, no error estimate), "
                f"{ALERT} not repro = neither; {ALERT} after a gene = it is in the vector space only through "
                f"drug-doses with an artifact flag; {ALERT} locus / readthrough? = neighbours on the genome, which "
                "can correlate for that reason alone; module = the partner's module and arm; rows with an alert "
                "keep their place") if sign > 0 else "the same columns")
        rel = o.pq("relations/gene_relations.parquet", columns=REL_COLS, filters=[("col_a", "==", int(c))])
        rows, n, n_al = _partner_rows(o, rel, top, sign)
        if not rows:
            P.append(f"  none among its top {len(rel)} partners by |cos|")
            continue
        P += _table(PARTNER_HEAD, rows, "lrrlrlll", flex=(6, 7, 0), mins={6: 18, 7: 14, 0: 8}, drop=(7, 5))
        if len(rows) < n:
            P.append(f"  ... {n - len(rows)} more on this side (--top)")
        rep = rel[(np.sign(rel["cos"]) == sign) & (rel["evidence"] == "both halves")]
        if "fdr" in rep:
            rep = rep[rep["fdr"].fillna(1.0) <= REPRO_FDR]
        P.append(f"  {n} of its top {len(rel)} partners by |cos| are on this side, {n_al} of them with an alert "
                 f"({ALERT}); {len(rep)} replicated (same sign with fdr <= {REPRO_FDR:g} in two random halves of the "
                 "compounds)" + (f", {int((rep['fdr'] <= 0.05).sum())} of them at fdr <= 0.05" if "fdr" in rep else ""))
        ok_nov, blocked = o.novelty()
        if sign < 0 and not ok_nov:
            P += _wrap(f"novelty not assessed: {', '.join(blocked) or 'reference sources'} missing "
                       "(relations/info.json), so no pair is called NOVEL", 2, 4)

    # where
    tb = [["drug-doses (pooled)", o.p("tables", "drug_effects.parquet"), f"col == {c}"],
          ["per line", o.p("tables", "line_effects.parquet"), f"col == {c}"],
          ["drug-dose x line", o.p("tables", "drug_line_top.parquet"), f"col == {c}"]]
    if o.ran("relations"):
        tb.append(["partners", o.p("relations", "gene_relations.parquet"), f"col_a == {c}"])
    if o.ran("tensor"):
        tb.append(["every drug-dose x line", (o.p("tensor", "DDL_lfc.npy"), " / DDL_z.npy"), f"[{c}] (dd x line)"])
    vn = _vault_note(o, "Genes", lab)
    if vn:
        tb.append(["vault note", vn, ""])
    if o.ran("map"):
        tb.append(["map", o.p("map", "gene_map.html") + "#" + lab, ""])
    _where(o, P, tb)
    return P


def cmd_gene(o, names, top):
    o.require("effects", "tables")
    P = []
    for i, nm in enumerate(names):
        cols, how = resolve_gene(o, nm)
        if len(cols) > 1 and not how:
            how = f"{nm} also names " + ", ".join(f"{o.genes().at[x, 'label']} (col {x})" for x in cols[1:]) + \
                  ": ask by label for those"
        if i:
            P += ["", "=" * min(WIDTH, 100), ""]
        P += gene_report(o, cols[0], top, how)
    return P


# ----------------------------------------------------------------------------- drug
def drug_report(o, drug, top):
    P = []
    dd = o.drugdoses()
    rows_dd = dd[dd["drug"] == drug].copy()
    rows_dd["conc_num"] = pd.to_numeric(rows_dd["conc"], errors="coerce")
    rows_dd = rows_dd.sort_values("conc_num")
    dds = rows_dd["dd"].astype(int).tolist()
    sb = T.salt_base(drug)
    others = sorted(set(dd.loc[(dd["salt_base"] == sb) & (dd["drug"] != drug), "drug"]))
    dr = None
    if o.has("tables/drugs.parquet"):
        t = o.pq("tables/drugs.parquet")
        t = t[t["drug"] == drug]
        dr = t.iloc[0] if len(t) else None
    r0 = rows_dd.iloc[0]
    P.append(drug + (f"   (compound {sb}; other salt forms in Tahoe: {', '.join(others)})" if others else
                     (f"   (compound {sb})" if sb != drug else "")))
    meta = []
    for k, nm in (("targets", "targets"), ("moa_fine", "mechanism"), ("moa_broad", "class"),
                  ("approved", "approved")):
        v = _text(r0.get(k, ""))
        if v:
            meta.append(f"{nm}: {v}")
    if meta:
        P += _wrap("   ".join(meta), 2, 4)
    if dr is not None:
        P += _wrap(f"doses (uM): {_text(dr['doses'])}   significant genes: {_text(dr['n_sig_by_dose'])}   best dose: "
                   f"{_text(dr['best_dose'])}   lowest active dose: {_text(dr['lowest_active_dose']) or 'none'}   "
                   f"signature r between doses: {_text(dr['signature_r_between_doses']) or '-'}", 2, 4)
    _title(P, "PER DOSE", "genes: significant at q < 0.10 and fold >= 1.2x / <= 1/1.2; cells: log2 vs the plate")
    rows = []
    for _, r in rows_dd.iterrows():
        nw = _int(r.get("n_wells"))
        nwa = _num(r.get("n_wells_all"))
        if np.isfinite(nwa) and nwa != _num(r.get("n_wells")):
            nw += f" of {int(nwa)}"
        rows.append([r["dose"], nw, _text(r.get("plates")).replace(",", ", "), _int(r.get("n_genes_up")),
                     _int(r.get("n_genes_down")), _f(r.get("replicate_r")), _f(r.get("cells_log2_vs_plate"), "{:+.2f}"),
                     _flags_shown(r["flags"])])
    P += _table(["uM", "wells", "plates", "up", "down", "rep r", "cells", "flags"], rows, "lllrrrrl",
                flex=(2, 7), mins={2: 8, 7: 16})
    if rows_dd["artifact"].any():
        P += _wrap(f"{ALERT} = an artifact flag of the drug-dose; it is shown with all its genes below. For a "
                   "cell-cycle shift the tables decide per gene whether the shift explains the change (genes whose "
                   f"change it does not explain carry no {ALERT})", 2, 4)

    # top genes per dose
    cols = ["col", "symbol", "dd", "lfc", "fold", "z", "q_up", "q_down", "flags", "clean", "n_lines_measured",
            "n_lines_up", "n_lines_down", "cc_share"]
    de = o.pq("tables/drug_effects.parquet", columns=cols, filters=[("dd", "in", dds)])
    if "cc_share" not in de:                     # an older tables stage
        de["cc_share"] = np.nan
    de["flags"] = de["flags"].fillna("").astype(str) if "flags" in de else ""
    g = o.genes()
    for _, r in rows_dd.iterrows():
        d = int(r["dd"])
        x = de[de["dd"] == d]
        up = x[(x["q_up"] < Q_CUT) & (x["lfc"] >= LFC_MIN)].sort_values("z", ascending=False).reset_index(drop=True)
        dn = x[(x["q_down"] < Q_CUT) & (x["lfc"] <= -LFC_MIN)].sort_values("z").reset_index(drop=True)
        note = _artifacts(r["flags"])
        dose_art = set(note.split("; ")) - {TB.CC_FLAG} if note else set()
        n_al = [int((~p_["clean"].astype(bool)).sum()) for p_ in (up, dn)]
        _title(P, f"TOP GENES at {r['dose']} uM", (f"{ALERT} drug-dose flags: {note}; " if note else "") +
               f"significant genes: {_n_alert(len(up), n_al[0], 'raised')}, {_n_alert(len(dn), n_al[1], 'lowered')}; "
               f"lines = lines moving / measured; alert = an artifact flag for that gene: {ALERT} alone = the "
               "drug-dose's flags named here, 'cell cycle ~N%' = its cell-cycle shift would explain ~N% of this "
               "change, 'position uncertain' = position correction uncertain for that gene")

        def gene_alert(y):
            """The alert of a gene at this drug-dose, without repeating the drug-dose's own flags."""
            if bool(y["clean"]):
                return ""
            own = [f for f in str(y["flags"]).split("; ") if f in A.ARTIFACT_FLAGS and f not in dose_art]
            words = _alert("; ".join(own), y["cc_share"], "short")
            return ALERT + (f" {words}" if words else "")
        if not len(up) and not len(dn):
            P.append("  no significant genes")
            continue
        sides = []
        for part in (up, dn):
            ok = part["clean"].astype(bool).to_numpy()
            sides.append((part, _capped(len(part), top, ok)))
        rows = []
        for i in range(max(len(sides[0][1]), len(sides[1][1]))):
            row = []
            for (part, show), key in zip(sides, ("n_lines_up", "n_lines_down")):
                if i < len(show):
                    j = show[i]
                    y = part.iloc[j]
                    row += [str(j + 1), g.at[int(y["col"]), "label"], _fold(y["fold"]), _z(y["z"]),
                            f"{int(y[key])}/{int(y['n_lines_measured'])}", gene_alert(y)]
                else:
                    row += ["", "", "", "", "", ""]
            rows.append(row[:6] + ["|"] + row[6:])
        P += _table(["#", "raised", "fold", "z", "lines", "alert", "|", "#", "lowered", "fold", "z", "lines", "alert"],
                    rows, "rlrrrllrlrrrl", flex=(1, 5, 8, 12), mins={1: 8, 5: 5, 8: 8, 12: 5})
        for (part, show), word in zip(sides, ("raised", "lowered")):
            al = ~part["clean"].astype(bool).to_numpy()
            more = _more(len(part), len(show), int(al.sum()) - int(al[show].sum()), word)
            if more:
                P.append(more)

    # similar drugs
    _title(P, "MOST SIMILAR DRUGS - cosine of the drug vectors (each drug's best dose) in the gene space")
    if not (o.has("embed/drug_vectors.npy") and o.has("embed/drugs.parquet")):
        P.append("  " + o.missing_note("embed"))
    else:
        ed = o.pq("embed/drugs.parquet").reset_index(drop=True)
        V = np.asarray(o.npy("embed/drug_vectors.npy"), dtype=np.float64)
        nrm = np.sqrt((V ** 2).sum(axis=1))
        hit = np.flatnonzero(ed["drug"].to_numpy() == drug)
        min_act = o.embed_info().get("min_active", 10)
        if not len(hit) or nrm[hit[0]] <= 0:
            P.append("  this drug has no vector (no effect on the genes of the space)")
        else:
            i = hit[0]
            with np.errstate(invalid="ignore", divide="ignore"):
                cs = V @ V[i] / (nrm * nrm[i])
            nsig = ed["n_sig_genes"].to_numpy() if "n_sig_genes" in ed else np.full(len(ed), min_act)
            trusted = ed["trusted"].fillna(True).astype(bool).to_numpy() if "trusted" in ed else \
                np.ones(len(ed), dtype=bool)
            vflags = dict(zip(dd["dd"].astype(int), dd["flags"]))

            def why(j):
                """The alert of drug j's vector: few significant genes at its vector dose, an untrusted vector dose or
                artifact flags there ('' = none)."""
                w = []
                if nsig[j] < min_act:
                    w.append(f"only {int(nsig[j])} significant gene{'s' if nsig[j] != 1 else ''}")
                ddj = int(_num(ed.iloc[j].get("dd"))) if np.isfinite(_num(ed.iloc[j].get("dd"))) else -1
                art = _artifacts(vflags.get(ddj, ""))
                if art:
                    w.append(f"dose flagged: {art}")
                elif not trusted[j]:
                    w.append("dose not trustworthy")
                return "; ".join(w)
            if why(i):
                P += _wrap(f"{ALERT} this drug's own vector: {why(i)} at its vector dose: read its neighbours with "
                           "that in mind", 2, 4)
            cand = [j for j in np.argsort(-np.where(np.isfinite(cs), cs, -np.inf))
                    if j != i and np.isfinite(cs[j]) and nrm[j] > 0]
            ok = np.array([not why(j) for j in cand], dtype=bool)
            show = _capped(len(cand), min(top, 12), ok)
            rows = []
            for k in show:
                j = cand[k]
                e = ed.iloc[j]
                same = " (same compound)" if T.salt_base(e["drug"]) == sb else ""
                rows.append([str(k + 1), e["drug"] + same, _text(e["dose"]), _cos(cs[j]), _int(nsig[j]),
                             f"{ALERT} {why(j)}" if why(j) else "", _text(e.get("moa_fine", "")),
                             _text(e.get("targets", ""))])
            if rows:
                P += _table(["#", "drug", "uM", "cos", "genes", "alert", "mechanism", "targets"], rows, "rlrrrlll",
                            flex=(1, 6, 7), mins={1: 14, 6: 12, 7: 8}, drop=(7,))
                P += _wrap(f"among {_n_alert(len(cand), int((~ok).sum()), 'other drugs with a vector')}; genes = "
                           f"significant genes at the drug's vector dose; {ALERT} only N significant genes (< "
                           f"{min_act}): the vector is mostly noise; {ALERT} dose flagged: artifact flags at the "
                           "vector dose", 2, 4)
            else:
                P.append("  no other drug has a vector")

    # modules
    _title(P, "MODULES IT MOVES - module score = mean pooled z of the + arm minus the - arm (of all members in a "
              "single-armed module)", "> 0: the module's + arm goes up and its - arm down; < 0: the reverse")
    mods = o.modules()
    if mods is None or not o.has("graph/module_pooled_z.npy"):
        P.append("  " + o.missing_note("graph"))
    else:
        M = np.asarray(o.npy("graph/module_pooled_z.npy")[:, dds], dtype=np.float32)
        with np.errstate(invalid="ignore"):
            best = np.nanmax(np.abs(M), axis=1) if M.size else np.zeros(len(mods))
        best = np.nan_to_num(best, nan=0.0)
        order = [m for m in np.argsort(-best) if best[m] > 0][:min(top, 10)]
        rows = []
        for m in order:
            mr = mods.iloc[m]
            rows.append([str(int(mr["module"])), _int(mr["n_genes"])] + [_z(v) for v in M[m]] +
                        [o.module_label(int(mr["module"]))])
        P += _table(["module", "genes"] + [f"{x} uM" for x in rows_dd["dose"]] + ["label"], rows,
                    "rr" + "r" * len(dds) + "l", flex=(2 + len(dds),), mins={2 + len(dds): 16})

    # lines
    ln = o.lines()
    _title(P, f"LINES IT DEPLETES - relative abundance z <= {DEPLETE_Z:g} vs the other lines in the same wells",
           "abundance = cells of the line relative to the other lines (2 ** DD_A)")
    DA, DAz = o.eff("DD_A"), o.eff("DD_Az")
    rows = []
    for _, r in rows_dd.iterrows():
        d = int(r["dd"])
        az = np.asarray(DAz[d], dtype=np.float32)
        a_ = np.asarray(DA[d], dtype=np.float32)
        art = _artifacts(r["flags"])
        for l in np.flatnonzero(np.nan_to_num(az, nan=0.0) <= DEPLETE_Z):
            rows.append((az[l], not art, [r["dose"], ln.at[l, "name"],
                                          _text(ln.at[l, "Organ"]) if "Organ" in ln else "", _fold(2 ** a_[l]),
                                          _z(az[l]), f"{ALERT} {art}" if art else ""]))
    rows.sort(key=lambda t: t[0])
    if rows:
        ok = np.array([x[1] for x in rows], dtype=bool)
        show = _capped(len(rows), top, ok)
        P += _table(["uM", "line", "organ", "abundance", "z", "alert (drug-dose artifact flags)"],
                    [rows[i][2] for i in show], "lllrrl", flex=(2, 5), mins={2: 6, 5: 12})
        P.append(f"  {_n_alert(len(rows), int((~ok).sum()), 'dose x line pairs')}"
                 + (f"; {len(rows) - len(show)} more (--top)" if len(rows) > len(show) else ""))
    else:
        P.append("  none")
    _title(P, "LINES THAT SHOW ITS RESPONSE MOST - DD_beta",
           "slope of the line's change on the drug's consensus over its significant genes; 1 = typical line, "
           "0 = no response; needs >= 20 significant genes")
    Db = o.eff("DD_beta")
    any_beta = False
    for _, r in rows_dd.iterrows():
        b = np.asarray(Db[int(r["dd"])], dtype=np.float32)
        if not np.isfinite(b).any():
            continue
        any_beta = True
        o_ = [l for l in np.argsort(-np.nan_to_num(b, nan=-np.inf), kind="stable") if np.isfinite(b[l])]
        k = min(8, len(o_) // 2)                       # 'most' and 'least' never share a line
        fl = _artifacts(r["flags"])
        P += _wrap(f"{r['dose']} uM ({len(o_)} lines{f'; {ALERT} ' + fl if fl else ''}): most: "
                   + ", ".join(f"{ln.at[l, 'name']} {b[l]:.2f}" for l in (o_[:k] if k else o_))
                   + (";  least: " + ", ".join(f"{ln.at[l, 'name']} {b[l]:.2f}" for l in o_[::-1][:k]) if k else ""),
                   2, 4)
    if not any_beta:
        P.append("  no estimate at any dose (fewer than 20 significant genes)")

    tb = [["per dose", o.p("tables", "drugdoses.parquet"), "dd in " + str(dds)],
          ["genes", o.p("tables", "drug_effects.parquet"), "dd in " + str(dds)]]
    vn = _vault_note(o, "Drugs", drug + " (drug)")
    if vn:
        tb.append(["vault note", vn, ""])
    _where(o, P, tb)
    return P


def cmd_drug(o, names, top):
    o.require("effects", "tables")
    q = " ".join(names)
    try:
        drugs = resolve_drug(o, q)
    except NotFound:
        if len(names) < 2:
            raise
        drugs = []
        for nm in names:                       # several drugs in one call
            drugs += [d for d in resolve_drug(o, nm) if d not in drugs]
    P = []
    for i, d in enumerate(drugs):
        if i:
            P += ["", "=" * min(WIDTH, 100), ""]
        P += drug_report(o, d, top)
    return P


# ----------------------------------------------------------------------------- line
def cmd_line(o, names, top):
    o.require("effects", "tables")
    l = resolve_line(o, " ".join(names))
    ln = o.lines()
    r = ln.iloc[l]
    P = []
    nm = r["name"]
    head = f"{nm}   {r['cell_line_id']}"
    if _text(r.get("Cell_ID_DepMap")):
        head += f"   DepMap {r['Cell_ID_DepMap']}"
    P.append(head)
    P += _wrap(f"organ: {_text(r.get('Organ')) or '-'}   TP53: {_text(r.get('tp53_status')) or 'unknown'}", 2, 4)
    if _text(r.get("drivers")):
        P += _wrap("drivers: " + _text(r.get("drivers")), 2, 4)
    if _text(r.get("driver_changes")):
        P += _wrap("driver changes: " + _text(r.get("driver_changes")), 2, 4)
    bits = [f"cells: {_int(r.get('n_cells_total'))} in total"]
    if np.isfinite(_num(r.get("wells_usable"))):
        bits.append(f"usable expression in {_int(r.get('wells_usable'))} wells "
                    f"({_f(r.get('pct_wells_usable'), '{:.1f}')}%)")
    if "in_growth_analysis" in r:
        bits.append("in the growth analysis" if bool(r.get("in_growth_analysis")) else "not in the growth analysis")
    P += _wrap("; ".join(bits), 2, 4)
    Db = np.asarray(o.eff("DD_beta"), dtype=np.float32)
    with np.errstate(invalid="ignore"):
        med = np.nanmedian(Db, axis=0)
    if np.isfinite(med[l]):
        rank = int((np.nan_to_num(med, nan=-np.inf) > med[l]).sum()) + 1
        P += _wrap(f"response strength: median DD_beta {med[l]:.2f} over the drug-doses with >= 20 significant genes "
                   f"(1 = typical line); rank {rank} of {int(np.isfinite(med).sum())} lines", 2, 4)

    # baseline
    g = o.genes()
    gK = len(g)
    cpm = np.asarray(o.eff("line_cpm")[:, :gK], dtype=np.float64)
    em = np.asarray(o.measured()[:, :gK], dtype=bool)          # the line truly expresses it (not ambient only)
    noise = g["noise_rna"].to_numpy().astype(bool) if "noise_rna" in g else \
        np.array([bool(A.NOISE_RNA_RE.match(s)) for s in g["symbol"]])
    lg = np.log2(cpm + 1.0)
    others = np.delete(np.arange(len(ln)), l)
    with np.errstate(invalid="ignore"):
        med_o = np.median(lg[others], axis=0)
        spec = lg[l] - med_o
    nxt = others[np.argmax(cpm[others], axis=0)] if len(others) else np.zeros(gK, dtype=int)
    nexp = em.sum(axis=0)
    def gene_alert(i):
        """Why a baseline call of gene i may mislead: a noise-class RNA, or a level that is only ambient RNA here."""
        w = (["noise-class RNA"] if noise[i] else []) + ([] if em[l, i] else ["only ambient RNA here (not measured)"])
        return f"{ALERT} " + "; ".join(w) if w else ""

    ok = (cpm[l] >= SPECIFIC_MIN_CPM) & np.isfinite(spec)
    order = [i for i in np.argsort(-np.where(ok, spec, -np.inf)) if ok[i]]
    show = _capped(len(order), top, [not gene_alert(i) for i in order])
    _title(P, "SPECIFICALLY HIGH AT BASELINE - this line's level vs the median of the other lines",
           f"atlas line_cpm, all wells; >= {SPECIFIC_MIN_CPM:g} CPM here; {ALERT} = noise-class RNA, or the line "
           "reads only ambient RNA of the gene (tensor/line_measured)")
    rows = []
    for k in show:
        i = order[k]
        rows.append([str(k + 1), g.at[i, "label"], _f(cpm[l, i], "{:,.0f}"), _f(2 ** med_o[i] - 1, "{:,.1f}"),
                     _fold(2 ** spec[i]), f"{ln.at[nxt[i], 'name']} {cpm[nxt[i], i]:,.0f}", f"{int(nexp[i])}",
                     gene_alert(i), o.ann_name(i)])
    if rows:
        P += _table(["#", "gene", "CPM here", "median other", "x median", "next highest line (CPM)", "lines expr",
                     "alert", "name"], rows, "rlrrrlrll", flex=(5, 8), mins={5: 12, 8: 10})
    else:
        P.append("  none")
    okl = (med_o >= np.log2(20 + 1)) & (nexp >= 0.5 * len(ln)) & np.isfinite(spec)
    kl = min(top, 10)
    order = [i for i in np.argsort(np.where(okl, spec, np.inf)) if okl[i] and spec[i] < -1]
    show = _capped(len(order), kl, [not noise[i] for i in order])
    _title(P, "SPECIFICALLY LOW AT BASELINE - absent or low here, expressed in most lines",
           "deletions, silencing; >= 20 CPM in the median other line; expressed here = measured "
           f"(tensor/line_measured: not ambient RNA only); {ALERT} = noise-class RNA")
    if show.size:
        P += _table(["#", "gene", "CPM here", "median other", "x median", "expressed here", "alert", "name"],
                    [[str(k + 1), g.at[order[k], "label"], _f(cpm[l, order[k]], "{:,.1f}"),
                      _f(2 ** med_o[order[k]] - 1, "{:,.0f}"), _fold(2 ** spec[order[k]]),
                      "yes" if em[l, order[k]] else "no", f"{ALERT} noise-class RNA" if noise[order[k]] else "",
                      o.ann_name(order[k])] for k in show], "rlrrrlll", flex=(7,), mins={7: 10})
    else:
        P.append("  none at < 0.5x the median line")

    # depletion
    dd = o.drugdoses()
    az = np.asarray(o.eff("DD_Az")[:, l], dtype=np.float32)
    a_ = np.asarray(o.eff("DD_A")[:, l], dtype=np.float32)
    hit = np.flatnonzero(np.nan_to_num(az, nan=0.0) <= DEPLETE_Z)
    hit = hit[np.argsort(az[hit])]
    okd = ~dd["artifact"].to_numpy()[hit]
    _title(P, f"DRUG-DOSES THAT DEPLETE IT - relative abundance z <= {DEPLETE_Z:g} vs the other lines in the wells",
           f"{_n_alert(len(hit), int((~okd).sum()), 'drug-doses')}; {ALERT} = an artifact flag of the drug-dose")
    if len(hit):
        show = _capped(len(hit), top, okd)
        P += _table(["#", "drug", "uM", "abundance", "z", "significant genes", "drug-dose flags"],
                    [[str(k + 1), dd.at[hit[k], "drug"], dd.at[hit[k], "dose"], _fold(2 ** a_[hit[k]]),
                      _z(az[hit[k]]), _int(dd.at[hit[k], "n_sig_genes"]), _flags_shown(dd.at[hit[k], "flags"])]
                     for k in show], "rllrrrl", flex=(1, 6), mins={1: 14, 6: 12})
        more = _more(len(hit), len(show), int((~okd).sum()) - int((~okd[show]).sum()))
        if more:
            P.append(more)
    else:
        P.append("  none")

    # strongest responses
    _title(P, "ITS STRONGEST RESPONSES - (gene, drug-dose) cells of this line, by per-line |z|",
           f"tables/drug_line_top: each gene's 15 strongest cells up and down at {o.line_cut_text()}, over all "
           f"drug-doses ({ALERT} = an artifact flag for that gene, kept in its place); fold = per-line fold change")
    dlt = o.pq("tables/drug_line_top.parquet",
               columns=["col", "symbol", "direction", "drug", "dose", "line", "lfc", "z", "pooled_lfc", "pooled_z",
                        "flags", "clean", "cc_share"],
               filters=[("line", "==", int(l))])
    if len(dlt):
        older = "clean" not in dlt
        if older:
            dlt = dlt.assign(clean=True, flags="", cc_share=np.nan)
        dlt = dlt.assign(az=dlt["z"].abs()).sort_values("az", ascending=False).reset_index(drop=True)
        okc = dlt["clean"].astype(bool).to_numpy()
        show = _capped(len(dlt), top, okc)
        P += _table(["#", "gene", "", "drug", "uM", "fold", "z", "pooled fold", "pooled z", "alert"],
                    [[str(k + 1), g.at[int(x["col"]), "label"], x["direction"], x["drug"], x["dose"],
                      _fold(2 ** _num(x["lfc"])), _z(x["z"]), _fold(2 ** _num(x["pooled_lfc"])), _z(x["pooled_z"]),
                      "" if okc[k] else _alert_cell(x["flags"], x["cc_share"], none=f"{ALERT} flagged")]
                     for k, x in ((k, dlt.iloc[k]) for k in show)],
                    "rlllrrrrrl", flex=(1, 3, 9), mins={1: 8, 3: 14, 9: 20})
        P.append(f"  {_n_alert(len(dlt), int((~okc).sum()), 'cells')}"
                 + (" (an older tables stage: clean drug-doses only)" if older else "")
                 + "; a large per-line fold change with a small pooled one = a response specific to this line")
        more = _more(len(dlt), len(show), int((~okc).sum()) - int((~okc[show]).sum()))
        if more:
            P.append(more)
    else:
        P.append("  none")
    tb = [["per gene", o.p("tables", "line_effects.parquet"), f"line == {l}"],
          ["cells", o.p("tables", "drug_line_top.parquet"), f"line == {l}"],
          ["line", o.p("tables", "lines.parquet"), f"line == {l}"]]
    vn = _vault_note(o, "Cell lines", f"{nm} (line)")
    if vn:
        tb.append(["vault note", vn, ""])
    _where(o, P, tb)
    return P


# ----------------------------------------------------------------------------- pair
def _pair_relation(o, a, b):
    """The relations row of (a, b), or the same numbers computed from the embed vectors (pair outside the top)."""
    if o.ran("relations"):
        rel = o.pq("relations/gene_relations.parquet", columns=REL_COLS + ["z_gene"],
                   filters=[("col_a", "in", [int(a), int(b)]), ("col_b", "in", [int(a), int(b)])])
        rel = rel[rel["col_a"] != rel["col_b"]]
        ab = rel[(rel["col_a"] == a) & (rel["col_b"] == b)]
        ba = rel[(rel["col_a"] == b) & (rel["col_b"] == a)]
        if len(ab) or len(ba):
            r = (ab if len(ab) else ba).iloc[0].to_dict()
            r["rank_ab"] = int(ab.iloc[0]["rank"]) if len(ab) else None
            r["rank_ba"] = int(ba.iloc[0]["rank"]) if len(ba) else None
            r["z_ab"] = _num(ab.iloc[0]["z_gene"]) if len(ab) else np.nan
            r["z_ba"] = _num(ba.iloc[0]["z_gene"]) if len(ba) else np.nan
            r["source"] = "relations"
            return r
    if not o.ran("embed"):
        return None
    from .relations import ONE_HALF, REPRO_MIN
    U = o.npy("embed/gene_unit.npy")
    ua, ub = np.asarray(U[a], dtype=np.float64), np.asarray(U[b], dtype=np.float64)
    if not (np.isfinite(ua).all() and np.isfinite(ub).all()):
        return None
    r = {"cos": float(ua @ ub), "source": "embed", "rank_ab": None, "rank_ba": None, "z_ab": np.nan,
         "z_ba": np.nan}
    if o.has("embed/gene_unit_half1.npy"):
        H1, H2 = o.npy("embed/gene_unit_half1.npy"), o.npy("embed/gene_unit_half2.npy")
        h1 = float(np.asarray(H1[a], dtype=np.float64) @ np.asarray(H1[b], dtype=np.float64))
        h2 = float(np.asarray(H2[a], dtype=np.float64) @ np.asarray(H2[b], dtype=np.float64))
        fdr = np.nan
        if o.has("relations/fdr_curve.csv"):
            cv = pd.read_csv(o.p("relations", "fdr_curve.csv"))
            fdr = float(np.interp(min(abs(h1), abs(h2)), cv["t"], cv["fdr"])) if np.sign(h1) == np.sign(h2) else 1.0
        sg = np.sign(r["cos"])
        both = bool(np.sign(h1) == sg and np.sign(h2) == sg and min(abs(h1), abs(h2)) >= REPRO_MIN
                    and np.isfinite(fdr) and fdr <= REPRO_FDR)  # as relations.py: replication needs the fdr too
        one = not both and max(abs(h1), abs(h2)) >= ONE_HALF and min(abs(h1), abs(h2)) < REPRO_MIN
        r.update(cos_half1=h1, cos_half2=h2,
                 evidence="both halves" if both else ("one half" if one else "not reproduced"))
        r["fdr"] = fdr
    return r


def _gene_flags_at(o, c, dds):
    """(flags, cc_share) per drug-dose in dds for gene c: drug_effects' flags and cc_share where the tables stage
    lists the drug-dose for the gene; else the same artifact rules applied here - the drug-dose's flags plus
    'position correction uncertain' for the gene (atlas DD_posunc) and the cell-cycle rule (tables.cc_rule on the
    gene's slopes, genes.parquet cc_slope_*). The soft caveats that depend on the gene (its plate factor, a position
    effect removed) are left out of that fallback: it serves the alert, which holds artifact flags only."""
    dd = o.drugdoses()
    dds = np.asarray(dds, dtype=np.int64)
    flags = dd["flags"].to_numpy(dtype=object)[dds].copy() if len(dds) else np.array([], dtype=object)
    share = np.full(len(dds), np.nan)
    pu = np.asarray(o.eff("DD_posunc")[:, c], dtype=bool)[dds] if o.has("atlas/effects/DD_posunc.npy") else \
        np.zeros(len(dds), dtype=bool)
    flags = np.array([A.gene_flags(f, bool(u)) for f, u in zip(flags, pu)], dtype=object)
    g = o.genes()
    cc = np.array([TB.CC_FLAG in str(f).split("; ") for f in flags], dtype=bool)
    if cc.any() and {"cc_slope_S", "cc_slope_G2M"} <= set(g.columns) and \
            {"S_PHASE_lfc", "G2M_PHASE_lfc"} <= set(dd.columns):
        bS, bG = _num(g.at[c, "cc_slope_S"]), _num(g.at[c, "cc_slope_G2M"])
        lf = np.asarray(o.eff("DD_lfc")[:, c], dtype=np.float64)[dds]
        S = pd.to_numeric(dd["S_PHASE_lfc"], errors="coerce").to_numpy()[dds]
        G = pd.to_numeric(dd["G2M_PHASE_lfc"], errors="coerce").to_numpy()[dds]
        sh, cleared = TB.cc_rule(lf, bS * S + bG * G)
        share = np.where(cc, sh, np.nan)
        for i in np.flatnonzero(cc & cleared):
            flags[i] = "; ".join(TB.CC_CLEARED.format(pct=int(round(100 * sh[i]))) if x == TB.CC_FLAG else x
                                 for x in str(flags[i]).split("; "))
    if o.has("tables/drug_effects.parquet") and len(dds):        # the stage's own strings where it wrote them
        de = o.pq("tables/drug_effects.parquet", columns=["col", "dd", "flags", "cc_share"],
                  filters=[("col", "==", int(c)), ("dd", "in", [int(x) for x in dds])])
        pos = {int(d): i for i, d in enumerate(dds)}
        for _, r in de.iterrows():
            i = pos[int(r["dd"])]
            flags[i] = _text(r["flags"])
            if "cc_share" in r:
                share[i] = _num(r["cc_share"])
    return flags, share


def cmd_pair(o, names, top):
    if len(names) != 2:
        raise NotFound("pair needs two genes: tahoe pair GENE_A GENE_B")
    o.require("effects")
    (ca, *more_a), how_a = resolve_gene(o, names[0])
    (cb, *more_b), how_b = resolve_gene(o, names[1])
    g = o.genes()
    hows = [how_a, how_b]
    for i, (nm, more) in enumerate(((names[0], more_a), (names[1], more_b))):
        if more:                                     # an ambiguous symbol: say which gene was taken
            note = (f"{nm} also names " + ", ".join(f"{g.at[x, 'label']} (col {x})" for x in more[:5]) +
                    (f" and {len(more) - 5} more" if len(more) > 5 else "") + "; ask by label to choose")
            hows[i] = f"{hows[i]}; {note}" if hows[i] else note
    how_a, how_b = hows
    la, lb = g.at[ca, "label"], g.at[cb, "label"]
    P = [f"{la} (col {ca}) x {lb} (col {cb})"]
    for h in (how_a, how_b):
        if h:
            P.append(f"  ({h})")
    if ca == cb:
        P.append("  the same gene twice")
        return P
    na, nb = o.ann_name(ca), o.ann_name(cb)
    if na or nb:
        P += _wrap(f"{la}: {na or '-'};  {lb}: {nb or '-'}", 2, 4)

    # relation
    _title(P, "RELATION IN THE VECTOR SPACE", "cos > 0: they move together; < 0: opposite; halves = two random "
                                              "halves of the compounds; both halves = same sign there with fdr <= "
                                              f"{REPRO_FDR:g}; one half = strong in one only, not replicated")
    r = None
    if not o.ran("embed"):
        P.append("  " + o.missing_note("embed"))
    else:
        r = _pair_relation(o, ca, cb)
        if r is None:
            why = [f"{x}: {_not_in_space(o, c)}" for x, c in ((la, ca), (lb, cb)) if _not_in_space(o, c)]
            P += _wrap(f"{ALERT} not both in the vector space - " + "; ".join(why), 2, 4)
        else:
            ev = _text(r.get("evidence")) or "-"
            P.append(f"  cos {_cos(r['cos'])}   halves {_cos(r.get('cos_half1'))} / {_cos(r.get('cos_half2'))}   "
                     f"evidence: {'' if ev in ('both halves', '-') else ALERT + ' '}{ev}   fdr {_q(r.get('fdr'))}")
            if ev == "one half":
                P += _wrap(f"{ALERT} seen in one random half of the compounds only: not replicated, no error "
                           "estimate", 2, 4)
            fo = [x for x, c in ((la, ca), (lb, cb)) if c in o.flagged_only()]
            if fo:
                P += _wrap(f"{ALERT} {' and '.join(fo)} {'is' if len(fo) == 1 else 'are'} in the vector space only "
                           "through drug-doses with an artifact flag: the relation may reflect the artifact", 2, 4)
            ranks = []
            if r.get("rank_ab"):
                ranks.append(f"{lb} is {la}'s partner #{r['rank_ab']} (z {_f(r['z_ab'], '{:+.1f}')})")
            if r.get("rank_ba"):
                ranks.append(f"{la} is {lb}'s partner #{r['rank_ba']} (z {_f(r['z_ba'], '{:+.1f}')})")
            if ranks:
                P += _wrap("; ".join(ranks), 2, 4)
            else:
                P.append("  not among either gene's top partners by |cos| (computed from the vectors)")
            if r["source"] == "relations":
                ok_nov, blocked = o.novelty()
                fl = _rel_flags(r, ok_nov)
                miss = ", ".join(blocked) or "reference sources"
                P.append("  flags: " + (fl or "none") + (
                    "" if bool(r.get("known")) or (ok_nov and bool(r.get("novel_candidate"))) else
                    "  (no known link in the reference)" if ok_nov else f"  (novelty not assessed: {miss} missing)"))
                if ok_nov and bool(r.get("novel_candidate")):
                    P += _wrap("NOVEL CANDIDATE: same sign in two random halves of the compounds, fdr <= 0.05, "
                               "|cos| >= 0.5, no shared gene group / pathway / STRING link, not one locus", 2, 4)
    ma, mb = _module_arm(o, ca), _module_arm(o, cb)
    if o.nodes() is not None and ma[0] is not None and mb[0] is not None:
        same = ma[0] == mb[0] and ma[0] > 0
        P.append(f"  nodal map: {la} module {_gene_module(o, ca)}, {lb} module {_gene_module(o, cb)}" +
                 ((" - same module, " + ("single-armed" if not ma[1] else "same arm" if ma[1] == mb[1] else
                                         "opposite arms")) if same else ""))

    # known / genome
    ann = o.ann()
    _title(P, "GENOME AND KNOWN LINKS", "reference annotation")
    if ann is None:
        P.append("  " + o.missing_note("reference"))
    else:
        x, y = ann.loc[ca], ann.loc[cb]
        cha, chb = _text(x.get("chrom")), _text(y.get("chrom"))
        sa, sb_, ea, eb = (_num(x.get("start")), _num(y.get("start")), _num(x.get("end")), _num(y.get("end")))
        if cha and chb and cha == chb and np.isfinite([sa, sb_, ea, eb]).all():
            gap = max(0.0, max(sa, sb_) - min(ea, eb))
            strand = "same strand" if _text(x.get("strand")) == _text(y.get("strand")) else "opposite strands"
            txt = f"same chromosome ({cha}), {gap:,.0f} bp apart, {strand}"
            if gap <= 50_000:
                txt += " - one locus (<= 50 kb): shared chromatin or read-through can make them correlate"
            P += _wrap(txt, 2, 4)
        else:
            P.append(f"  chromosomes {cha or '?'} and {chb or '?'}" + (" (different)" if cha and chb else ""))
        bits = []
        if o.has("reference/string_pairs.parquet"):
            lo, hi = min(ca, cb), max(ca, cb)
            sp = o.pq("reference/string_pairs.parquet", filters=[("col_a", "==", int(lo)), ("col_b", "==", int(hi))])
            bits.append(f"STRING {int(sp['score'].max())}" if len(sp) else "no STRING link (>= 400)")
        if o.has("reference/gene_sets.parquet"):
            gs = o.pq("reference/gene_sets.parquet", columns=["source", "set", "col"],
                      filters=[("col", "in", [int(ca), int(cb)])])
            sa_ = set(map(tuple, gs.loc[gs["col"] == ca, ["source", "set"]].to_numpy()))
            sb2 = set(map(tuple, gs.loc[gs["col"] == cb, ["source", "set"]].to_numpy()))
            shared = sorted(sa_ & sb2)
            if shared:
                bits.append(f"{len(shared)} shared sets: " + "; ".join(f"{s} ({src})" for src, s in shared[:6])
                            + (" ..." if len(shared) > 6 else ""))
            else:
                bits.append("no shared gene set (Hallmark, Reactome, HGNC group)")
        if bits:
            P += _wrap("; ".join(bits), 2, 4)

    # shared drug-doses
    dd = o.drugdoses()
    Z = o.eff("DD_z")
    Lf = o.eff("DD_lfc")
    za, zb = np.asarray(Z[:, ca], dtype=np.float64), np.asarray(Z[:, cb], dtype=np.float64)
    fa, fb = np.asarray(Lf[:, ca], dtype=np.float64), np.asarray(Lf[:, cb], dtype=np.float64)
    with np.errstate(invalid="ignore"):
        both = (np.abs(za) >= PAIR_Z) & (np.abs(zb) >= PAIR_Z)
        prod = za * zb
    moved = np.flatnonzero(both & np.isfinite(prod))
    fl_a, sh_a = _gene_flags_at(o, ca, moved)
    fl_b, sh_b = _gene_flags_at(o, cb, moved)
    at = {int(d): i for i, d in enumerate(moved)}

    def pair_alert(d):
        """The alert of drug-dose d for the pair: each gene's artifact flags (one text when they are the same)."""
        i = at[int(d)]
        a, b = _alert(fl_a[i], sh_a[i], "short"), _alert(fl_b[i], sh_b[i], "short")
        if not a and not b:
            return ""
        if a == b:
            return f"{ALERT} {a}"
        return f"{ALERT} " + "; ".join(x for x in (f"{la}: {a}" if a else "", f"{lb}: {b}" if b else "") if x)

    k = min(top, 10)
    for sign, word in ((1, "SAME DIRECTION"), (-1, "OPPOSITE DIRECTIONS")):
        idx = np.flatnonzero(both & (np.sign(prod) == sign))
        idx = idx[np.argsort(-np.abs(prod[idx]))]
        ok = np.array([not pair_alert(d) for d in idx], dtype=bool)
        show = _capped(len(idx), k, ok)
        _title(P, f"DRUG-DOSES THAT MOVE BOTH, {word} - every drug-dose with pooled |z| >= {PAIR_Z:g} for each",
               f"{_n_alert(len(idx), int((~ok).sum()), 'drug-doses')}; {ALERT} = an artifact flag for one or both "
               f"genes ('cell cycle ~N%': the drug-dose's cell-cycle shift would explain ~N% of the gene's change), "
               f"kept in its place; top {k} by z({la}) x z({lb})")
        if len(idx):
            P += _table(["#", "drug", "uM", f"{la} fold", "z", f"{lb} fold", "z", "alert", "caveats"],
                        [[str(j + 1), dd.at[d, "drug"], dd.at[d, "dose"], _fold(2 ** fa[d]), _z(za[d]),
                          _fold(2 ** fb[d]), _z(zb[d]), pair_alert(d), _caveats(dd.at[d, "flags"]) or "-"]
                         for j, d in ((j, idx[j]) for j in show)], "rllrrrrll", flex=(1, 8),
                        mins={1: 12, 8: 8})
            more = _more(len(idx), len(show), int((~ok).sum()) - int((~ok[show]).sum()))
            if more:
                P.append(more)
        else:
            P.append("  none")

    # per line
    act = o.active_dd()
    _title(P, "AGREEMENT INSIDE EACH CELL LINE - Pearson r of the per-line log2 fold changes (tensor DDL_lfc)",
           f"over the {int(act.sum())} active, trustworthy drug-doses (the embed stage's contexts: an estimate, so "
           f"drug-doses whose wells are untrusted - {', '.join(UNTRUSTED)} - are left out of it); each entry: line, "
           "r, drug-doses measured in both")
    mp = act & np.isfinite(fa) & np.isfinite(fb)
    ra = np.nan
    if mp.sum() >= PAIR_MIN_N and fa[mp].std() > 0 and fb[mp].std() > 0:
        ra = float(np.corrcoef(fa[mp], fb[mp])[0, 1])
    if not o.ran("tensor"):
        P.append("  " + o.missing_note("tensor"))
    else:
        D = o.npy("tensor/DDL_lfc.npy")
        Xa = np.asarray(D[ca], dtype=np.float64)[act]
        Xb = np.asarray(D[cb], dtype=np.float64)[act]
        ln = o.lines()
        res = []
        for l in range(Xa.shape[1]):
            m = np.isfinite(Xa[:, l]) & np.isfinite(Xb[:, l])
            n = int(m.sum())
            rr = np.nan
            if n >= PAIR_MIN_N:
                x, y = Xa[m, l], Xb[m, l]
                if x.std() > 0 and y.std() > 0:
                    rr = float(np.corrcoef(x, y)[0, 1])
            res.append((ln.at[l, "name"], rr, n))
        fin = [t for t in res if np.isfinite(t[1])]
        fin.sort(key=lambda t: -t[1])
        if fin:
            rs = np.array([t[1] for t in fin])
            P += _wrap(f"median r {np.median(rs):+.2f} over {len(fin)} lines; r >= 0.3 in {int((rs >= 0.3).sum())}, "
                       f"r <= -0.3 in {int((rs <= -0.3).sum())}; pooled over the lines (DD_lfc): r {_cos(ra)}", 2, 4)
            nw = max(len(str(t[2])) for t in fin)
            cells = [f"{_cut(nm_, 12):<12} {r_:+.2f} {n_:>{nw}}" for nm_, r_, n_ in fin]
            cw = max(len(c_) for c_ in cells) + 3
            ncol = max(1, (WIDTH - 2) // cw)
            nrow = -(-len(cells) // ncol)
            for i in range(nrow):
                P.append("  " + "".join(cells[j * nrow + i].ljust(cw) for j in range(ncol)
                                        if j * nrow + i < len(cells)).rstrip())
            miss = [t[0] for t in res if not np.isfinite(t[1])]
            if miss:
                P += _wrap(f"too few shared measurements (< {PAIR_MIN_N}) or a gene not expressed: " + ", ".join(miss),
                           2, 4)
        else:
            P.append("  no line has both genes measured in enough active drug-doses")
    return P


# ----------------------------------------------------------------------------- module
def cmd_module(o, names, top):
    o.require("effects", "graph")
    mods = o.modules()
    nd = o.nodes()
    P = []
    for qi, nm in enumerate(names):
        try:
            m = int(str(nm).strip().lstrip("Mm").lstrip("odule").strip())
        except ValueError:
            raise NotFound(f"module needs a number (1 .. {len(mods)}), not '{nm}'")
        if qi:
            P += ["", "=" * min(WIDTH, 100), ""]
        if m == 0:
            un = nd[nd["module"] == 0]
            fo = o.flagged_only()
            n_fo = int(un["col"].isin(fo).sum())
            P.append("MODULE 0 = genes in the vector space but in no module of >= 5 genes: "
                     + (_n_alert(len(un), n_fo) if n_fo else f"{len(un)}"))
            if len(un):
                P += _wrap(", ".join(f"{sy}{' ' + ALERT if int(c_) in fo else ''}" for sy, c_ in
                                     zip(un["symbol"].astype(str).head(60), un["col"].head(60)))
                           + (" ..." if len(un) > 60 else ""), 2, 2)
                if un["col"].isin(fo).any():
                    P += _wrap(f"{ALERT} = in the vector space only through drug-doses with an artifact flag", 2, 4)
            continue
        hit = np.flatnonzero(mods["module"].to_numpy() == m)
        if not len(hit):
            raise NotFound(f"No module {m}: modules run 1 .. {int(mods['module'].max())} (0 = unassigned)")
        i = int(hit[0])
        mr = mods.iloc[i]
        opp, _b = o.module_arms(m)
        P.append(f"MODULE {m}   {int(mr['n_genes'])} genes" +
                 (f": {int(mr['n_plus'])} in the + arm, {int(mr['n_minus'])} in the - arm" if opp else
                  " (single-armed)") + f"   map centre ({_f(mr['x'], '{:.1f}')}, {_f(mr['y'], '{:.1f}')})")
        lab = o.labels()
        if lab is not None and m in lab.index:
            lr = lab.loc[m]
            src = _text(lr.get("label_source"))
            txt = f"label: {_text(lr.get('label'))}"
            if src and src != "top genes":
                txt += (f"  ({src}; {_int(lr.get('label_overlap'))} of {_int(lr.get('label_n_set'))} set genes "
                        f"here; q {_q(lr.get('label_q'))})")
            P += _wrap(txt, 2, 4)
            arms = []
            for arm, k in (("+", "plus"), ("-", "minus")):
                if _text(lr.get(f"{k}_label")):
                    arms.append(f"{arm} arm: {_text(lr.get(f'{k}_label'))} (q {_q(lr.get(f'{k}_q'))})")
            if arms:
                P += _wrap("   ".join(arms), 2, 4)
        else:
            P += _wrap(f"label: {o.module_label(m)}   " + o.missing_note("validate", "set-based label"), 2, 4)
        P += _wrap(o.arms_text(m), 2, 4)

        mem = nd[nd["module"] == m].copy()
        mem["ap"] = mem["axis_proj"].abs() if "axis_proj" in mem else 0.0
        plus = mem[mem["arm"] == "+"].sort_values("ap", ascending=False).head(top)
        minus = mem[mem["arm"] == "-"].sort_values("ap", ascending=False).head(top)
        fo = o.flagged_only()
        n_fo = int(mem["col"].isin(fo).sum())
        _title(P, "TOP GENES PER ARM" if opp else "TOP GENES (single-armed module)",
               "by |projection on the module's main direction|; name from the reference" +
               (f"; {_n_alert(len(mem), n_fo, 'members')}: {ALERT} after a gene = in the vector space only through "
                "drug-doses with an artifact flag" if n_fo else ""))
        rows = []
        for j in range(max(len(plus), len(minus))):
            row = [str(j + 1)]
            for part in ((plus, minus) if opp else (plus,)):
                if j < len(part):
                    y = part.iloc[j]
                    row += [o.genes().at[int(y["col"]), "label"] + (f" {ALERT}" if int(y["col"]) in fo else ""),
                            _f(y.get("axis_proj"), "{:+.2f}"), o.ann_name(int(y["col"]))]
                else:
                    row += ["", "", ""]
            rows.append(row[:4] + ["|"] + row[4:] if opp else row)
        if opp:
            P += _table(["#", "+ arm", "proj", "name", "|", "- arm", "proj", "name"], rows, "rlrlllrl",
                        flex=(3, 7), mins={3: 8, 7: 8})
        else:
            P += _table(["#", "gene", "proj", "name"], rows, "rlrl", flex=(3,), mins={3: 8})

        dd = o.drugdoses()
        art = dd["artifact"].to_numpy()
        if o.has("graph/module_pooled_z.npy"):
            pz = np.asarray(o.npy("graph/module_pooled_z.npy")[i], dtype=np.float64)
            order = np.argsort(-np.nan_to_num(pz, nan=0.0))
            k = min(top, 12)
            up_all = [d for d in order if np.isfinite(pz[d]) and pz[d] > 0]
            dn_all = [d for d in order[::-1] if np.isfinite(pz[d]) and pz[d] < 0]
            sides = [(lst, _capped(len(lst), k, [not art[d] for d in lst])) for lst in (up_all, dn_all)]
            _title(P, "DRUG-DOSES THAT MOVE IT - module score = " +
                   ("mean pooled z of the + arm minus the - arm" if opp else "mean pooled z of its genes"),
                   ("raise: + arm up, - arm down; lower: the reverse" if opp else "raise: its genes up; lower: down")
                   + f"; {ALERT} = an artifact flag of the drug-dose (reasons below), kept in its place; raise: "
                   f"{_n_alert(len(up_all), int(sum(art[d] for d in up_all)))}; lower: "
                   f"{_n_alert(len(dn_all), int(sum(art[d] for d in dn_all)))}")
            rows = []
            for j in range(max(len(sides[0][1]), len(sides[1][1]))):
                row = []
                for lst, show in sides:
                    if j < len(show):
                        d = lst[show[j]]
                        row += [str(show[j] + 1), dd.at[d, "label"] + " uM" + (f" {ALERT}" if art[d] else ""),
                                _z(pz[d])]
                    else:
                        row += ["", "", ""]
                rows.append(row[:3] + ["|"] + row[3:])
            P += _table(["#", "raises it", "score", "|", "#", "lowers it", "score"], rows, "rlrlrlr", flex=(1, 5),
                        mins={1: 14, 5: 14})
            shown = [lst[x] for lst, show in sides for x in show]
            fl = {}
            for d in shown:
                if art[d]:
                    fl.setdefault(_artifacts(dd.at[d, "flags"]), []).append(dd.at[d, "label"] + " uM")
            if fl:
                P += _wrap(f"{ALERT} " + "; ".join(f"{', '.join(v)}: {a_}" for a_, v in fl.items()), 2, 4)
        pz = np.asarray(o.npy("graph/module_pooled_z.npy")[i], dtype=np.float64) \
            if o.has("graph/module_pooled_z.npy") else None
        if o.has("graph/module_scores.npy"):
            S = np.asarray(o.npy("graph/module_scores.npy")[i], dtype=np.float32)        # Dn x L
            act = o.active_dd()
            ln = o.lines()
            with np.errstate(invalid="ignore"):
                spread = np.nanmedian(np.abs(S[act] if act.any() else S), axis=0)
                # the module's main clean drug-doses (5 raising, 5 lowering it, pooled): does the line follow them?
                main = []
                if pz is not None:
                    okd = np.isfinite(pz) & ~dd["artifact"].to_numpy()
                    o_ = np.argsort(-np.where(okd, pz, -np.inf))
                    main = [d for d in o_[:5] if okd[d] and pz[d] > 0] + \
                        [d for d in np.argsort(np.where(okd, pz, np.inf))[:5] if okd[d] and pz[d] < 0]
                follow = np.nanmean(S[main] * np.sign(pz[main])[:, None], axis=0) if main else \
                    np.full(S.shape[1], np.nan)
            key = np.where(np.isfinite(follow), follow, spread)
            ol = [l for l in np.argsort(-np.nan_to_num(key, nan=-np.inf)) if np.isfinite(key[l])][:min(top, 10)]
            _title(P, "RESPONSIVE LINES - how strongly each line shows the module's response",
                   f"follows = mean per-line score on the module's {len(main)} main clean drug-doses (an estimate: "
                   "drug-doses with an artifact flag are left out of it), signed so that > 0 = the line moves the "
                   "way the pooled lines do; per (drug-dose, line) score = mean per-line z of the + arm minus the - "
                   "arm, or of its genes if single-armed (tensor DDL_z); median |score| over the "
                   f"{int(act.sum())} active drug-doses (untrusted ones left out); strongest drug-dose over all, "
                   f"{ALERT} = an artifact flag of the drug-dose")
            rows = []
            for l in ol:
                col = np.nan_to_num(np.abs(S[:, l]), nan=-1.0)
                d = int(np.argmax(col))
                al = _artifacts(dd.at[d, "flags"]) if dd.at[d, "artifact"] else ""
                rows.append([ln.at[l, "name"], _text(ln.at[l, "Organ"]) if "Organ" in ln else "",
                             _f(follow[l], "{:+.2f}"), _f(spread[l]),
                             f"{dd.at[d, 'label']} uM ({_z(S[d, l])})" + (f" {ALERT} {al}" if al else "")])
                okd = np.flatnonzero(~art & np.isfinite(S[:, l])) if al else []
                if len(okd):                     # the strongest has an alert: also the strongest without one
                    d2 = int(okd[np.argmax(np.abs(S[okd, l]))])
                    rows.append(["", "", "", "", f"no alert: {dd.at[d2, 'label']} uM ({_z(S[d2, l])})"])
            P += _table(["line", "organ", "follows", "median |score|", "strongest drug-dose (score)"], rows,
                        "llrrl", flex=(1, 4), mins={1: 6, 4: 16}, drop=(1,))
        tb = [["members", o.p("graph", "nodes.parquet"), f"module == {m}"],
              ["module", o.p("graph", "modules.parquet"), f"module == {m}"],
              ["scores", o.p("graph", "module_scores.npy"), f"[{i}] (drug-dose x line)"]]
        if o.ran("validate"):
            tb.append(["enrichment", o.p("validation", "module_enrichment.csv"), f"module == {m}"])
        vn = glob.glob(o.p("vault", "Modules", f"Module {m:03d}.md")) if o.ran("vault") else []
        if vn:
            tb.append(["vault note", vn[0], ""])
        _where(o, P, tb)
    return P


# ----------------------------------------------------------------------------- entry
COMMANDS = {"gene": cmd_gene, "drug": cmd_drug, "line": cmd_line, "pair": cmd_pair, "module": cmd_module}
USAGE = {"gene": "tahoe gene SYMBOL [SYMBOL ...]", "drug": "tahoe drug NAME", "line": "tahoe line NAME",
         "pair": "tahoe pair GENE_A GENE_B", "module": "tahoe module N"}


def _fit(lines):
    """Any line still wider than WIDTH (free text built in one piece) is wrapped, keeping its indentation."""
    out = []
    for ln in lines:
        if len(ln) <= WIDTH:
            out.append(ln)
            continue
        ind = len(ln) - len(ln.lstrip(" "))
        out += textwrap.wrap(ln.strip(), width=WIDTH, initial_indent=" " * ind, subsequent_indent=" " * (ind + 2),
                             break_on_hyphens=False)
    return out


def _printable(text, stream=None):
    """text as the output stream can show it: on a console or a redirect whose encoding has no ALERT (a Windows code
    page), ALERT becomes ALERT_ASCII and any other character it cannot show a '?'."""
    stream = sys.stdout if stream is None else stream
    enc = getattr(stream, "encoding", None) or "utf-8"
    try:
        text.encode(enc)
        return text
    except UnicodeEncodeError:
        return text.replace(ALERT, ALERT_ASCII).encode(enc, errors="replace").decode(enc)
    except LookupError:
        return text


def _emit(lines):
    text = _printable("\n".join(_fit(lines)))
    try:
        print(text, flush=True)
    except OSError as e:                         # the reader went away: piped into head, or `| more` and q
        if not (isinstance(e, BrokenPipeError) or e.errno in (errno.EPIPE, errno.EINVAL)):
            raise                                # (Windows: a pipe closed by its reader is EINVAL, not EPIPE)
        try:
            sys.stdout = open(os.devnull, "w")
        except OSError:
            pass


def main(a):
    """The look-up commands of cli.py: a.command in gene | drug | line | pair | module, a.names, a.top, a.out."""
    global WIDTH
    WIDTH = max(80, min(120, shutil.get_terminal_size((120, 24)).columns)) - 2
    warnings.filterwarnings("ignore", category=RuntimeWarning)
    top = int(a.top) if getattr(a, "top", None) and int(a.top) > 0 else 15
    names = [n for n in (getattr(a, "names", None) or []) if str(n).strip()]
    if not names:
        _emit([f"usage: {USAGE[a.command]}   (options: --top N rows per table, --out OUTPUT folder)"])
        sys.exit(2)
    o = Out(a.out, getattr(a, "data", None))
    if not os.path.isdir(a.out):
        _emit([f"No output folder {a.out}: nothing has run there yet.",
               *_wrap(o.how("effects"), indent=0)])
        sys.exit(1)
    try:
        lines = COMMANDS[a.command](o, names, top)
    except Missing as e:
        _emit([str(e)])
        sys.exit(1)
    except NotFound as e:
        _emit(_wrap(str(e), indent=0, sub=2))
        sys.exit(1)
    _emit(lines)
    return 0
