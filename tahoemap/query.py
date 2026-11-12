"""query - the look-ups of a finished run, answered as plain text (no colours, 80-120 columns, aligned tables).

    tahoe gene SYMBOL     what the gene is (reference annotation, module and arm of the nodal map), the drug-doses
                          that raise it and lower it (pooled over the cell lines: fold, z, q, lines that move / lines
                          measured, dose pattern, alert, soft caveats), the cell lines where drug-doses move it most
                          (with each line's strongest drug-dose), the genes that move with it and opposite to it (cos,
                          evidence, fdr, locus / read-through / known / novel), its PROBABLE DIRECTION (what
                          probably acts on it, what it probably acts on, how it probably sets the cells' growth under
                          drug-doses), and where the full tables are. A name that is no gene of the run but the
                          source of direction arrows (a drug target the screen does not measure) gets those arrows
    tahoe drug NAME       targets and mechanism; per dose: wells, flags, genes up / down, top genes up / down
                          (fold, the rough DMSO-referenced fold as a sign check, z, lines, alert); the drug-doses
                          most similar to its best dose (none as a ranking when it has no pooled signature); the
                          drugs with the most similar vector, the modules it moves, the lines it depletes and the
                          lines that show its response most; the genes that probably set how the cells fare under it
                          and what acting on its targets probably does. NAME is case-insensitive; a salt form can be
                          left out ('Doxorubicin' = 'Doxorubicin (hydrochloride)'); a part of a name lists the matches
    tahoe line NAME       organ, drivers, TP53 status; genes specifically high (and low) at baseline; drug-doses
                          that deplete it; its strongest responses; its recorded alterations and the genes it does
                          not express as the direction stage compared them, with their arrows. NAME = cell name or
                          Cellosaurus id
    tahoe pair A B        the two genes' cosine, its two compound halves, evidence, fdr, known / novel flags and
                          genomic distance; any probable-direction arrow between them, either way (every alert in
                          full), and the genes with an arrow to both; the drug-doses that move both (same / opposite
                          direction); how far the two agree inside each cell line
    tahoe module N        size, arms, label (validation stage: its source, weak or not, its alerts, the drug class
                          that drives it, its lineage; what it moves with), top genes per arm, top drug-doses up / down
                          and the lines where it responds most
    tahoe similar DRUG [DOSE]   the drug-doses most similar to one drug-dose (embed/drug_similarity.parquet: cos of
                          the pooled signatures and over the per-line contexts, shared genes, classes, flags); a
                          drug-dose that moves no gene at |z| >= 3 or q < 0.10 has no pooled signature, hence no
                          ranking: it says so, and where its stored rows are (--top N lists them in row order)
    tahoe signature --up A,B [--down C,D] [--lines]   which drug-doses mimic or reverse a gene signature: score =
                          mean z of the up genes minus the down genes (atlas DD_z; else the drug_effects rows, z = 0
                          elsewhere), p from 1,000 random gene sets of the same sizes matched by expression level
                          (pooled-CPM decile); --lines: the lines that show the strongest mimics most (tensor DDL_z)

Lists and the explorer. Every list shows --top rows (default 15; the probable-direction lists 10 unless --top is
given; --top all, or 0, shows every row of every list: no cap at all), cut by the cap rule below, and a list that
leaves rows out says how many, with 'all N: <explorer URL>' - the explorer (pipeline stage `explorer`,
tahoemap/links.py: its site URL, else the output's own explorer/web/index.html) holds every list in full.

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

Probable direction (the direction stage, OUT/direction): every row, its order, the merging of rows that are one test
for several sources, the cap rule and every word (the edge line: SOURCE → TARGET [grade] what the source's activity
probably does (the evidence; q), the comparison, the alerts' short labels, the counts, the grade legend and the
caveat) come from direction_view, so the look-ups say what the vault, the map and the review dossiers say; the
numbers are the stage's own sentences (edges.parquet reading). A direction is probable - from the screen's cell
lines, not proof of direct regulation - and every list says so. On a console or redirect that cannot show '→' or
ALERT (a Windows code page such as cp1252) these texts are built in ASCII ('->', '!') before they are laid out, so
that every line stays within WIDTH. An output made before the direction stage existed gets one sentence instead.

Nothing is computed afresh that a stage already wrote: the look-ups read OUT/tables, OUT/embed, OUT/relations,
OUT/graph, OUT/direction, OUT/reference and OUT/validation (each optional where the answer can do without it; a
missing stage is named with the command that makes it; a column an older stage version did not write is done
without), plus a few columns of the atlas matrices (atlas/effects DD_z, DD_lfc, DD_posunc, DD_A, DD_Az, DD_beta,
line_cpm, expr_mask), tensor/line_measured.npy, and two genes' rows of tensor/DDL_lfc for `pair`. Every read is a
filtered parquet read or a memory-mapped slice (OUT/direction is read whole: direction_view.load, ~1 GB and a few
seconds on a full-scale table of ~100,000 edges): one look-up stays around 1 GB at full scale. Unknown names get close
matches (difflib). Nothing is written.

An answer states the stages' own rules, never more: per-line counts and 'strongest' use the per-line |z| cut the
tables stage calibrated (tables/info.json, with the expected chance calls); 'both' halves = same sign with fdr <=
0.10 in two random halves of the compounds, 'one' = strong in one random half only (not the same sign in both, no error
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
from . import common as CM
from . import direction_view as DV
from . import links as LK
from . import mechanisms as MECH
from . import tables as TB
from . import tlib as T
from .common import ARROW, cap_keep, encodable, marked_names, printable, read_effects_index, safe_filename
from .relations import REPRO_FDR, SAME_SIGN, SAME_SIGN_NOTE   # evidence 'both halves' needs fdr <= this

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
SET_SOURCES = ("control", "hallmark", "reactome")   # validate version 7: a gene-set label (its q is the label's own)
DMSO_MIN = np.log2(1.2)     # gene: 'other sign' against DMSO needs |lfc_vs_dmso| >= this (the atlas's 1.2x)
N_SIMILAR = 10              # drug: the most similar drug-doses of its best dose shown by default (of 50)
_TAG = re.compile(r"^\s*\[[^\]]{1,80}\]:\s*")    # UniProt isoform tag before a FUNCTION text ('[Isoform 2]: ')
ALERT = "\u26a0"            # the alert sign: an item kept in its place although there is a reason to doubt it
ALERT_ASCII = "!"           # what it becomes on a console that cannot show it (_emit; one character, so that
                            # tables stay aligned)
ASCII = False               # set in main(): the output cannot show the arrow or ALERT (a Windows code page, e.g. a
                            # cp1252 redirect): the direction texts are built in ASCII ('->', '!') before they are
                            # laid out, so that every line keeps within WIDTH
N_DIRECTION = 10            # rows per probable-direction list (the cap rule) unless --top is given (then --top)
TOP_GIVEN = False           # set in main(): the user gave --top (the direction lists then show that many)
TOP_ALL = 10 ** 9           # --top all (or 0): no list is capped
SITE = None                 # set in main(): the explorer's site URL (links.site_url), None = none
LOCAL_X = os.path.join("OUT", "explorer", "web", "index.html")   # set in main(): the output's own explorer

# the file whose presence says a stage has run (look-ups must not depend on stage stamps: an output folder can be
# assembled from finished stage folders)
STAGE_FILE = {"effects": "atlas/effects/drugdose.csv", "tensor": "tensor/DDL_lfc.npy",
              "tables": "tables/genes.parquet", "embed": "embed/gene_unit.npy",
              "reference": "reference/annotations.parquet", "relations": "relations/gene_relations.parquet",
              "graph": "graph/nodes.parquet", "direction": "direction/edges.parquet",
              "validate": "validation/module_labels.csv", "vault": "vault", "map": "map/gene_map.html"}


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
    """A q value: common.Q_ZERO ('< 1e-45') for a stored 0 (below what a float32 holds), '3e-05' below 0.001, else
    3 decimals."""
    x = _num(x)
    if not np.isfinite(x):
        return na
    if x == 0:
        return CM.Q_ZERO
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


_ADDRESS = re.compile(r"://|[\\/]\S*\.html")


def _wrap(text, indent=2, sub=None, max_lines=None):
    sub = indent if sub is None else sub
    text = re.sub(r" (?=[µu]M\b)", "\u00a0", str(text))        # a dose stays with its unit ('5 µM')
    lines = [x.replace("\u00a0", " ") for x in textwrap.wrap(      # a web address or a file path (the output's own
        text, width=WIDTH, initial_indent=" " * indent, subsequent_indent=" " * sub, break_on_hyphens=False,
        break_long_words=not _ADDRESS.search(text))] or [""]        # explorer) is never broken over two lines
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
    return "; ".join(f for f in fl if f in CM.ARTIFACT_FLAGS)


CC_WORDS = {"full": "cell-cycle shift, explains ~{p}% of this change", "table": "cell-cycle shift, explains ~{p}%",
            "short": "cell cycle ~{p}%"}       # the cell-cycle alert with the share of the change it would explain


def _alert(flags, cc_share=None, words="full"):
    """The reason for an item's alert in plain words: its artifact flags ('' = no alert); a cell-cycle shift with the
    share of this change it would explain (tables cc_share). words: 'full' (sentences), 'table' (an alert column),
    'narrow' (as 'table', but 'neighbouring well' for 'like a neighbouring well': a crowded table, whose legend gives
    the words), 'short' (narrow side-by-side tables: 'cell cycle ~87%', 'position uncertain')."""
    out = []
    for f in str(flags or "").split("; "):
        if f not in CM.ARTIFACT_FLAGS:
            continue
        if f == TB.CC_FLAG:
            sh = _num(cc_share)
            f = CC_WORDS["table" if words == "narrow" else words].format(p=int(round(100 * sh))) \
                if np.isfinite(sh) else ("cell cycle" if words == "short" else TB.CC_FLAG)
        elif words == "short" and f == "position correction uncertain":
            f = "position uncertain"
        elif words in ("short", "narrow") and f == CM.NB_FLAG:
            f = "neighbouring well"                  # a table cell; its words stand under the table
        out.append(f)
    return "; ".join(out)


def _alert_cell(flags, cc_share=None, words="table", none=""):
    """An alert column's cell: ALERT + the reason, or `none`."""
    a = _alert(flags, cc_share, words)
    return f"{ALERT} {a}" if a else none


def _caveats(flags):
    """The flags that are no artifact flag: soft caveats, a cell-cycle shift that is not the explanation, and the
    caveat tokens of common.CAVEAT_FLAGS (neighbouring well at the top dose / not this gene, translation inhibitor;
    _flag_legend gives their words, common.FLAG_TEXT)."""
    return "; ".join(f for f in str(flags or "").split("; ") if f and f not in CM.ARTIFACT_FLAGS)


def _flag_legend(P, flags_list, indent=2):
    """Under a table: the words (common.FLAG_TEXT) of each neighbouring-well or translation-inhibitor token that occurs
    in its flags, once each ('' -> nothing)."""
    seen = set()
    for f in flags_list:
        seen.update(x.strip() for x in str(f or "").split("; "))
    for t, txt in CM.FLAG_TEXT.items():
        if t in seen:
            kind = f"{ALERT} an artifact flag" if t in CM.ARTIFACT_FLAGS else "a caveat, not an artifact flag"
            P += _wrap(f"'{t}' ({kind}): {txt}", indent, indent + 2)


def _flags_shown(flags, cc_share=None, none="-"):
    """A flags cell: the alert first (ALERT + artifact flags in plain words), then the soft caveats."""
    a, c = _alert(flags, cc_share, "table"), _caveats(flags)
    if a:
        return f"{ALERT} {a}" + (f"; {c}" if c else "")
    return c or none


def _wells(n):
    """' · one well' / ' · 2 wells' after a lines count ('' when unknown)."""
    n = _num(n)
    if not np.isfinite(n) or n <= 0:
        return ""
    return " · one well" if int(n) == 1 else f" · {int(n)} wells"


def _dmso(x, lfc, short=False):
    """The rough DMSO-referenced fold of a row ('1.23x'; ' (other sign)', short: '*', when it is at least 1.2x the
    other way; 'none' when the plate has no DMSO value)."""
    x, lfc = _num(x), _num(lfc)
    if not np.isfinite(x):
        return "none"
    t = _fold(2 ** x)
    if abs(x) >= DMSO_MIN and np.isfinite(lfc) and lfc != 0 and np.sign(x) != np.sign(lfc):
        t += "*" if short else " (other sign)"
    return t


def _top_genes_table(side_rows, has_dmso):
    """The drug look-up's TOP GENES table: [raised rows, lowered rows], each row [#, gene, fold, vs DMSO, z, lines,
    alert]. [one table side by side] when that fits within WIDTH with every column at its full width; else (a long
    alert, long lines counts) [the raised table, the lowered one] (an empty side: []), so that no column is left out
    and no alert is cut more. has_dmso False (tables older than version 5): no vs DMSO column, side by side as
    before."""
    keep = [k for k in range(7) if has_dmso or k != 3]
    head = [["#", "raised", "fold", "vs DMSO", "z", "lines", "alert"],
            ["#", "lowered", "fold", "vs DMSO", "z", "lines", "alert"]]
    al = "rlrrrrl"
    sides = [[[r_[k] for k in keep] for r_ in rr] for rr in side_rows]
    hd = [[h[k] for k in keep] for h in head]
    a1 = "".join(al[k] for k in keep)
    n1 = len(keep)
    gene_i, alert_i = keep.index(1), keep.index(6)
    n = max(len(sides[0]), len(sides[1]))
    rows = [(sides[0][i] if i < len(sides[0]) else [""] * n1) + ["|"]
            + (sides[1][i] if i < len(sides[1]) else [""] * n1) for i in range(n)]
    full = [max([len(x)] + [len(r_[i]) for r_ in rows]) for i, x in enumerate(hd[0] + ["|"] + hd[1])]
    if 2 + sum(full) + 2 * (len(full) - 1) <= WIDTH or not has_dmso:
        return [_table(hd[0] + ["|"] + hd[1], rows, a1 + "l" + a1,
                       flex=(gene_i, alert_i, n1 + 1 + gene_i, n1 + 1 + alert_i),
                       mins={gene_i: 8, alert_i: 5, n1 + 1 + gene_i: 8, n1 + 1 + alert_i: 5})]
    return [_table(h, rr, a1, flex=(gene_i, alert_i), mins={gene_i: 10, alert_i: 12}) if rr else []
            for h, rr in zip(hd, sides)]


def _share_plate(o):
    """{drug: True} for drugs whose doses share a plate (tables drugs.parquet doses_share_a_plate)."""
    def load():
        if not o.has("tables/drugs.parquet"):
            return {}
        t = o.pq("tables/drugs.parquet")
        if "doses_share_a_plate" not in t:
            return {}
        return {str(d): bool(v) for d, v in zip(t["drug"], t["doses_share_a_plate"].fillna(False)) if bool(v)}
    return o._cached("share_plate", load)


def _capped(n, top, ok):
    """Positions to show of a ranked list of n items (strongest first) capped at top: the top strongest overall plus
    any of the top strongest without an alert (ok True) that would fall outside them, in rank order. Flagged items
    thus never push clean ones out of view."""
    ok = np.asarray(ok, dtype=bool)[:n]
    keep = np.arange(n) < top
    keep[np.flatnonzero(ok)[:top]] = True
    return np.flatnonzero(keep)


def _more(n, shown, n_alert_rest, what="", opt=" (--top N, or --top all)", url=None):
    """'... k more[ what] (j of them with an alert) (--top N, or --top all); all N: <explorer URL>' for the items a
    capped list leaves out ('' when none)."""
    k = n - shown
    if k <= 0:
        return ""
    return (f"  ... {k} more" + (f" {what}" if what else "") + (f" ({n_alert_rest} of them with an alert)"
                                                                 if n_alert_rest else "") + opt
            + (f"; {_all_at(n, url)}" if url else ""))


def parse_top(v):
    """The --top value: a whole number of rows per list, or 'all' (also 0) for every row (TOP_ALL). For cli.py's
    argument parser (type=query.parse_top)."""
    if v is None:
        return None
    t = str(v).strip().lower()
    if t in ("all", "0"):
        return 0
    try:
        n = int(t)
    except ValueError:
        raise ValueError(f"--top takes a whole number of rows or 'all', not {v!r}") from None
    if n < 0:
        raise ValueError(f"--top takes a whole number of rows (>= 0) or 'all', not {v!r}")
    return n


def _xu(fn, *a, **k):
    """An explorer address (fn: a links builder, links.gene ...); without a site URL the output's own explorer."""
    return fn(SITE or LOCAL_X, *a, **k)


def _all_at(n, url):
    """'all N: <url>' - where every item of a capped list is (the explorer)."""
    return f"all {n:,}: {url}" + ("" if SITE else " (this output's explorer, once the explorer stage has run)")


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
            extra = (" The reference stage downloads public annotations and the drugs' ChEMBL mechanisms (network; "
                     "optional, skipped with --offline): `tahoe run --from reference` with network access. It runs "
                     "right after tensor, so that also redoes tables and every later stage.")
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
            d["artifact"] = [CM.has_artifact(f) for f in d["flags"]]             # the flags of record
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
        """Gene cols in the vector space only through drug-doses that carry an alert for them, pooled and per line
        (embed genes.parquet evidence_flagged_only; empty when an older embed stage did not write it)."""
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
        return f"per-line |z| >= {self.line_cut()[0]:.2f} ({self.line_cut_note()})"

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
        """validation/module_labels.csv label (label_display: with its alert tags, when the table has it); else
        (unless set_only) the module's top genes. set_only: only a gene-set label (label_source control / hallmark /
        reactome; an older validate stage: any source but the top genes)."""
        lab = self.labels()
        if lab is not None and m in lab.index and "label" in lab and _text(lab.at[m, "label"]):
            src = _text(lab.at[m, "label_source"]) if "label_source" in lab else "set"
            v7 = "label_display" in lab
            ok = src in SET_SOURCES if v7 else src not in ("", "top genes")
            if not set_only or ok:
                return (_text(lab.at[m, "label_display"]) if v7 else "") or _text(lab.at[m, "label"])
        if set_only:
            return ""
        mods = self.modules()
        if mods is not None:
            r = mods[mods["module"] == m]
            if len(r):
                tp = _arm_names(self, r.iloc[0]["top_plus"], 3)
                tm = _arm_names(self, r.iloc[0]["top_minus"], 2)
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
    if _yes(r.get("lineage_pair")):
        p_ = _num(r.get("lineage_p"))
        f.append(f"{ALERT} lineage (lines {_int(r.get('n_lines_a'))}/{_int(r.get('n_lines_b'))}, J "
                 f"{_f(r.get('lines_jaccard'))}" + (f", p {_q(p_)}" if np.isfinite(p_) else "") + ")")
    if _text(r.get("read_sharing")):
        f.append(f"{ALERT} copies ({_text(r.get('read_sharing'))})")
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
            (f" or a per-line |z| >= {lz:.2f} in >= 2 lines of one trustworthy drug-dose" if np.isfinite(lz) else "")
            + ", and it has neither")
    if np.isfinite(_num(ei.get("null_rate"))):
        txt += f" (chance rate of |z| >= 3 per context {_num(ei['null_rate']):.2g})"
    if ei.get("n_genes_excluded_chance") is not None:
        txt += f"; {int(ei['n_genes_excluded_chance']):,} genes of this run reach the count without either"
    return txt


def _arm_names(o, txt, n, exclude=""):
    """The top genes of a module arm (graph/modules.parquet top_plus / top_minus, strongest first) cut at n with the cap
    rule: a gene in the vector space only through flagged drug-doses reads 'SYMBOL ⚠' (written so by the graph stage;
    an older graph stage: marked here from embed evidence_flagged_only). `exclude`: a symbol to leave out (the gene
    itself)."""
    names = marked_names(txt, None, exclude)
    fo = o.flagged_only()
    if fo and not any(x.endswith(ALERT) for x in names):
        g = o.genes()
        col = dict(zip(g["symbol"].astype(str), g.index))
        names = [x + (f" {ALERT}" if col.get(x, -1) in fo else "") for x in names]
    return marked_names(", ".join(names), n)


def _partner_alert(o, x):
    """True when a partner row carries an alert: not the same sign in both halves of the compounds, the partner in
    the vector space only through flagged drug-doses, a lineage pair or read-sharing copies (relations version 5)."""
    return (_text(x.get("evidence")) != "both halves" or int(x["col_b"]) in o.flagged_only()
            or _yes(x.get("lineage_pair")) or _yes(x.get("read_sharing_risk")))


def _yes(v):
    """A boolean cell (bool, numpy bool, 0/1, NaN / None = False)."""
    return bool(np.isfinite(_num(v)) and _num(v) != 0) if not isinstance(v, str) else v.lower() in ("true", "1")


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
            "novel_candidate", "n_lines_a", "n_lines_b", "lines_jaccard", "lineage_pair", "lineage_p", "read_sharing",
            "read_sharing_risk", "alert"]
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
    (tables/drug_line_top.parquet; flagged ones in their place with their alert, capped as _capped at k: 3, every
    one with --top all), as one sentence ('' when none), with how many it names and the explorer address of all of
    them. An older tables stage listed clean drug-doses only."""
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
    show = _capped(len(order), k, okd)
    for i in show:
        x = g.get_group(order[i])
        r0 = x.iloc[0]
        al = "" if okd[i] else _alert(r0.get("flags"), r0.get("cc_share"))
        cells = ", ".join(f"{_text(r['cell_name'])} {_fold(2 ** _num(r['lfc']))}" for _, r in x.head(4).iterrows())
        parts.append(f"{T.salt_base(_text(r0['drug']))} {_text(r0['dose'])} uM" + (f" ({ALERT} {al})" if al else "")
                     + f" in {len(x)} line{'s' if len(x) != 1 else ''} ({cells}"
                     + (f", ... {len(x) - 4} more lines" if len(x) > 4 else "") + ")")
    n_al = sum(not v for v in okd)
    what = (_n_alert(len(order), n_al, "drug-doses") if not older else
            f"{len(order)} clean drug-doses; an older tables stage left flagged ones out")
    lab = o.genes().at[int(c), "label"]
    return (f"in single lines, at per-line |z| >= {o.line_cut()[0]:.2f} ({o.line_cut_note()}; "
            f"tables/drug_line_top, {what}): " + ("raised by " if direction == "up" else "lowered by ")
            + "; ".join(parts) + (f" ({len(show)} of {len(order)} drug-doses named; "
                                  f"{_all_at(len(order), _xu(LK.gene, lab, 'lines'))})" if len(show) < len(order)
                                  else ""))


# ----------------------------------------------------------------------------- probable direction (direction stage)
def _direction(o):
    """(direction_view.Direction or None, why): None with why '' when the direction stage has not run (an older
    output), with why = the error when its files cannot be read."""
    def load():
        if not o.ran("direction"):
            return None, ""
        try:
            return DV.load(o.out), ""
        except Exception as e:  # noqa: BLE001  (a damaged or partial folder: a sentence, not a traceback)
            return None, f"{type(e).__name__}: {_cut(str(e), 160)}"
    return o._cached("direction", load)


def _dir_missing(o, why, what="probable direction"):
    """The sentence for an output without the direction stage (or with one that cannot be read)."""
    if why:
        return (f"[{what}: OUT/direction cannot be read here ({why}); `tahoe run --from direction` makes it "
                "again]")
    return o.missing_note("direction", what)


def _dt(text):
    """A direction text as the output can show it: in ASCII ('->', '!', '>=') when the console cannot show the signs
    (ASCII, set in main), so that it is laid out at its printed width; a q of 0 reads common.Q_ZERO."""
    text = str(text).replace("q 0e+00", f"q {CM.Q_ZERO}")
    return DV.ascii_signs(text) if ASCII else text


_SIGN_CLAUSE = re.compile(r"; [^;]*\bactivity (?:raises|lowers|strengthens|weakens|protects|makes) [^;]*$")


def _dir_n(top):
    """Rows per probable-direction list: N_DIRECTION, or --top when the user gave it (more or fewer)."""
    return int(top) if TOP_GIVEN else min(int(top), N_DIRECTION)


def _top_hint(total):
    """Where the rows a capped list leaves out are: '--top N' lists them all (so does --top all)."""
    return f"(`--top {int(total)}` lists them all)"


def _dir_reading(r):
    """The stage's own sentence for a row (direction.py's reading: its numbers), without its closing clause on what
    the source's activity does, which the row's edge line already says (DV.sign_text)."""
    return _SIGN_CLAUSE.sub("", _text(r.get("reading", "")))


def _dir_rows(P, rows, n, alerts="short", extra=None, max_names=4):
    """A probable-direction list, rows in direction_view's ORDER, capped by the cap rule (the n strongest, and any of
    the n strongest without an alert beyond them; DV.cap): per row its rank and edge line (arrow, grade, what the
    source's activity probably does, the kind of evidence, q), then the comparison (kind_text, where it differs from
    the row above) and its numbers (the stage's reading), extra(row) when given, the alerts (ALERT + short labels;
    alerts='long': every reason in full, and the notes in full too) and the support (short labels; with alerts='long'
    in full). The texts are direction_view's (and direction.py's readings); lines are wrapped, never cut. Returns
    (shown, n_more, n_more_alert)."""
    if rows is None or not len(rows):
        return 0, 0, 0
    al = rows["has_alert"].to_numpy(dtype=bool)
    keep = cap_keep(al, n)
    last = None
    for k in keep:
        r = rows.iloc[int(k)]
        P += _wrap(f"{k + 1:>3}  " + DV.edge_line(r, ASCII, alerts="none", max_names=max_names).replace(
            "q 0e+00", f"q {CM.Q_ZERO}"), 2, 7)
        ev = DV.kind_text(r)
        ev, last = ("" if ev == last else ev), ev        # the comparison is named where it changes
        rd = _dir_reading(r)
        x = extra(r) if extra else ""
        P += _wrap(_dt("; ".join(t for t in (ev, rd, x) if t)), 7, 7)
        a = DV.alert_long(r, ASCII) if alerts == "long" else DV.alert_short(r, ASCII)
        if a:
            P += _wrap(a, 7, 9)
        nl = DV.notes_long(r, ASCII) if alerts == "long" else ""
        if nl:
            P += _wrap(_dt(f"notes in full: {nl}"), 7, 9)
        sp = DV.support_long(r, ASCII) if alerts == "long" else DV.support_short(r, ASCII)
        if sp:
            P += _wrap(_dt(f"support: {sp}"), 7, 9)
    rest = np.setdiff1d(np.arange(len(rows)), keep)
    return len(keep), int(rest.size), int(al[rest].sum())


def _dir_list(P, title, rows, n, what="arrows", url=None, **kw):
    """One list: its title with the counts (DV.counts_text), the caveats every arrow of its kinds carries (stated
    once: DV.caveat_header), the rows (_dir_rows: each edge line with the short labels of its notes, its alerts
    below), and what the cap leaves out (DV.more_text) with the explorer address of all of them (url)."""
    P += _wrap(_dt(f"{title}: {DV.counts_text(rows, what)}"), 2, 4)
    if rows is None or not len(rows):
        return 0
    cav = DV.caveat_header(rows, ASCII)
    if cav:
        P += _wrap(_dt(cav), 4, 4)
    shown, n_more, n_more_al = _dir_rows(P, rows, n, **kw)
    more = DV.more_text(n_more, n_more_al, what)
    if more:
        P += _wrap(_dt(f"... {more} {_top_hint(len(rows))}" + (f"; {_all_at(len(rows), url)}" if url else "")), 2, 6)
    if n is not None and shown > n:
        P += _wrap(f"rows beyond #{n}: among the {n} strongest without an alert, shown so that rows with an alert do "
                   "not push them out", 4, 6)
    return len(rows)


def _dir_legend(P):
    """How to read a probable-direction list: the row layout, the grades, the kinds, the order and the caveat."""
    arrow = DV.arrow("SOURCE", "TARGET", ASCII)
    P += _wrap(f"how to read: {arrow}  [grade]  what the source's ACTIVITY probably does to the target - raises or "
               "lowers its level or the cells' numbers under a drug-dose (lowers = makes the cells more sensitive), "
               "strengthens or weakens its drug response, or 'not inferred' (mechanism not recorded) - (the evidence; "
               "q: Benjamini-Hochberg over the kind's whole table of tests); below it the comparison (where it "
               f"changes) and its numbers; {_dt(ALERT)} = a reason to doubt the arrow (an alert), in short labels; "
               "'notes:' = reasons kept below their thresholds, and context; 'support:' = evidence for the arrow "
               "(for example the compounds that agree); a caveat that every arrow of a kind "
               "carries is stated once above the list (every reason in full: `tahoe pair SOURCE TARGET`, the "
               f"explorer or direction/edges.parquet); a row keeps its ranked place; order: {DV.ORDER}", 2, 4)
    P += _wrap(DV.SIGN_RESPONSE_NOTE, 2, 4)
    P += _wrap("grades: " + "; ".join(DV.grade_legend("long")), 2, 4)
    P += _wrap("evidence: mutation = a recorded mutation of the source (Tahoe's cell-line genetics: lines with it vs "
               "lines with no record of the gene); not expressed = lines that do not express the source (natural "
               "knockouts); drug target = compounds that target the source's protein; natural level = the source's "
               "level across the lines (a glimpse)", 2, 4)
    P += _wrap(_dt(DV.CAVEAT), 2, 4)


def _gene_tests_text(o, col):
    """'tested in 4,850 comparisons (mutation: response 2,376, ...): no arrow passed' from direction/gene_tests.parquet
    (direction version 5): every test the gene took part in, as the source or the target, by kind ('' without the
    file)."""
    if not o.has("direction/gene_tests.parquet"):
        return ""
    gt = o.pq("direction/gene_tests.parquet", filters=[("col", "==", int(col))])
    if not len(gt):
        return "tested in no comparison of the direction stage"
    by = gt.groupby("kind")["n_tests"].sum()
    n, n_e = int(by.sum()), int(gt["n_edges"].sum())
    parts = ", ".join(f"{DV.KIND_SHORT.get(k, k)} {int(by[k]):,}" for k in DV.KINDS if k in by.index and by[k])
    return (f"tested in {n:,} comparison{'s' if n != 1 else ''} ({parts})"
            + (": no arrow passed" if not n_e else f"; {n_e:,} arrow{'s' if n_e != 1 else ''} passed (q < 0.10)"))


def _dir_where(o, tb, key):
    if o.ran("direction"):
        tb.append(["direction (arrows)", o.p("direction", "edges.parquet"), key])


def _dir_gene(o, P, gene, lab, top):
    """The gene's PROBABLE DIRECTION: upstream (rows whose target is the gene: what probably acts on it), downstream
    (gene targets it is the source of, or one of the sources of a row that names several) and the cells under
    drug-doses (sensitivity rows it is the source of), each in direction_view's ORDER with the cap rule and counts,
    then the legend and the caveat. gene: its col (exact) or, for a source that is not a measured gene, its symbol."""
    _title(P, f"PROBABLE DIRECTION - what probably acts on {lab}, and what it probably acts on", DV.CAVEAT_SHORT
           + "; direction/edges.parquet")
    dv, why = _direction(o)
    if dv is None:
        P += _wrap(_dir_missing(o, why), 2, 4)
        return
    tested = _gene_tests_text(o, gene) if isinstance(gene, (int, np.integer)) else ""
    if tested:
        P += _wrap(tested, 2, 4)
    n = _dir_n(top)
    lists = [(f"upstream - what probably acts on {lab} ({lab} is the target)", dv.upstream(gene)),
             (f"downstream - genes {lab} probably acts on", dv.downstream(gene)),
             (f"cells under drugs - how {lab} probably acts on the cells' growth under a drug-dose, or on how "
              "strongly the lines respond to it (their numbers "
              "relative to the other lines in the same wells)", dv.cells(gene))]
    if not any(len(r) for _t, r in lists):
        P += _wrap(f"none: no arrow involves {lab} in this run. Arrows come from recorded mutations of a gene, from "
                   "lines that do not express it (natural knockouts), from compounds that target it and from its "
                   "natural level across the lines; each needs a test result at q < 0.10.", 2, 4)
        P += _wrap(_dt(DV.CAVEAT), 2, 4)
        return
    url = _xu(LK.gene, lab, "direction") if isinstance(gene, (int, np.integer)) else _xu(LK.search, lab)
    for title, rows in lists:
        _dir_list(P, title, rows, n, url=url)
    _dir_legend(P)


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
        P += _wrap(f"significant drug-doses, pooled over the lines and against the typical drug well on the same "
                   f"plate, not DMSO (q < {Q_CUT:g} and fold >= {2 ** LFC_MIN:.1f}x or <= 1/{2 ** LFC_MIN:.1f}): "
                   f"{nu} raise it ({nu - nuc} of them with an alert {ALERT}: an artifact flag for this gene), {nd} "
                   f"lower it ({nd - ndc} with an alert); the lists below hold every drug-dose with |z| >= 3 or q < "
                   f"{Q_CUT:g}, a wider rule", 2, 4)
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
            lb = o.module_label(m)
            if lb and not lb.startswith("genes: "):          # a gene set, a driving drug class or a lineage
                txt += f"; label: {lb}"
            P += _wrap(txt + "; " + o.arms_text(m), 2, 4)
            if mr is not None:
                same = _arm_names(o, mr["top_plus" if arm == "+" else "top_minus"], 8, gr["symbol"])
                other = _arm_names(o, mr["top_minus" if arm == "+" else "top_plus"], 8)
                note = f" ({ALERT} = in the vector space only through drug-doses with an artifact flag)" \
                    if any(ALERT in x for x in same + (other if opp else [])) else ""
                if same:
                    P += _wrap((f"its arm ({arm}): " if opp else "module genes: ") + ", ".join(same)
                               + (note if not (other and opp) else ""), 4, 6)
                if other and opp:
                    P += _wrap(f"opposite arm ({'-' if arm == '+' else '+'}, moves the other way): "
                               + ", ".join(other) + note, 4, 6)
        else:
            P.append("  nodal map: in the vector space, not in a module (module 0)")
    elif nd is None:
        P.append("  " + o.missing_note("graph", "module and arm"))
    if not why and c in o.flagged_only():
        P += _wrap(f"{ALERT} in the vector space only through drug-doses that carry an alert (artifact flags for this "
                   "gene at every significant pooled drug-dose and per-line response; embed evidence_flagged_only): "
                   "its partners and module may reflect the artifact", 2, 4)

    # drug-doses
    cols = ["dd", "drug", "dose", "lfc", "fold", "z", "q_up", "q_down", "flags", "clean", "n_lines_measured",
            "n_lines_up", "n_lines_down", "pattern_up", "pattern_down", "cc_share", "n_wells", "lfc_vs_dmso"]
    de = o.pq("tables/drug_effects.parquet", columns=cols, filters=[("col", "==", int(c))])
    de["flags"] = de["flags"].fillna("").astype(str)
    de["clean"] = de["clean"].astype(bool)
    if "cc_share" not in de:                     # an older tables stage
        de["cc_share"] = np.nan
    has_dmso = "lfc_vs_dmso" in de               # tables version 5: n_wells and the rough DMSO-referenced lfc
    if "n_wells" not in de:
        nw = o.drugdoses()["n_wells"] if "n_wells" in o.drugdoses() else pd.Series(np.nan, index=o.drugdoses().index)
        de["n_wells"] = nw.to_numpy()[de["dd"].astype(int).to_numpy()] if len(de) else np.nan
    share = _share_plate(o)
    all_flags = []
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
        one = _single_lines(o, c, "up" if sign > 0 else "down", k=TOP_ALL if top >= TOP_ALL else 3) \
            if int((sig & ok).sum()) < SHORT_POOLED else ""
        if not len(sub):
            P.append("  none")
            P += _wrap(one, 2, 4) if one else []
            continue
        show = _capped(len(sub), top, ok)
        rows, cavs = [], []
        for i in show:
            r = sub.iloc[i]
            nl = r["n_lines_up"] if sign > 0 else r["n_lines_down"]
            all_flags.append(r["flags"])
            pat = _text(r["pattern_up" if sign > 0 else "pattern_down"])
            if share.get(_text(r["drug"])):
                pat += " (doses share a plate)"
            rows.append([str(i + 1), f"{r['drug']} {r['dose']}", _fold(r["fold"]),
                         _dmso(r.get("lfc_vs_dmso"), r["lfc"]) if has_dmso else "", _z(r["z"]),
                         _q(r[qc]) + ("*" if sig[i] else " "),
                         f"{int(nl)}/{int(r['n_lines_measured'])}{_wells(r.get('n_wells'))}",
                         "" if ok[i] else _alert_cell(r["flags"], r["cc_share"], words="narrow",
                                                      none=f"{ALERT} flagged"),
                         pat])
            cav = _caveats(r["flags"])
            if cav:
                cavs.append(f"#{i + 1} {cav}")
        head = ["#", "drug uM", "fold", "vs DMSO", "z", "q", "lines", "alert", "pattern over doses"]
        keep_c = [k for k in range(len(head)) if not (k == 3 and not has_dmso) and not (k == 7 and ok[show].all())]
        rows = [[r_[k] for k in keep_c] for r_ in rows]       # no alert among the rows shown: no alert column
        hd = [head[k] for k in keep_c]
        al = "".join("rlrrrrrll"[k] for k in keep_c)
        ix = {k: j for j, k in enumerate(keep_c)}
        P += _table(hd, rows, al, flex=tuple(ix[k] for k in (1, 7, 8) if k in ix),
                    mins={ix[k]: m_ for k, m_ in ((1, 16), (7, 26), (8, 14)) if k in ix})
        if cavs:                                 # the soft caveats of the rows shown, in full, under the table
            P += _wrap("caveats (no alert): " + "; ".join(cavs), 2, 4)
        more = _more(len(sub), len(show), int((~ok).sum()) - int((~ok[show]).sum()),
                     url=_xu(LK.gene, lab, "drugs"))
        if more:
            P += _wrap(more.strip(), 2, 6)
        if len(show) > top:
            P += _wrap(f"rows beyond #{top}: the strongest without an alert, shown so that flagged drug-doses do not "
                       "push them out", 2, 4)
        P += _wrap(one, 2, 4) if one else []
    P += _wrap("lines = lines moving it / lines measured, inside the drug-dose's well(s) ('one well': the lines are "
               "not replicate treatments); pattern over doses = how it behaves over the drug's doses, each dose on "
               "its own plate (so plates as much as doses)" + ("; vs DMSO = the rough DMSO-referenced fold (a sign "
                                                               "check against the plate's two DMSO wells, not a "
                                                               "replacement), 'other sign' = at least 1.2x the "
                                                               "other way" if has_dmso else ""), 2, 4)
    _flag_legend(P, all_flags)

    # lines
    le = o.pq("tables/line_effects.parquet", filters=[("col", "==", int(c))])
    ln = o.lines()
    organ = dict(zip(ln["line"], ln["Organ"].fillna("").astype(str))) if "Organ" in ln else {}
    t_line = o.line_cut()[0]
    has_all = "n_dd_up_all" in le                # older tables: the clean drug-doses only
    sfx = "_all" if has_all else ""
    _title(P, f"IN WHICH CELL LINES - number of drug-doses moving it >= 1.5x at per-line |z| >= {t_line:.2f}, and "
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
        le["mz_clean"] = np.fmax(le["best_up_z"].abs(), le["best_down_z"].abs())
        expd = le[le["expressed"].astype(bool)].sort_values(["n", "mz"], ascending=[False, False]) \
            .reset_index(drop=True)
        # the cap rule: the `top` lines by the count over all drug-doses, and also any of the `top` lines by the count
        # over drug-doses without an alert that fall beyond them, in the first ranking's order
        keep = np.arange(len(expd)) < top
        if has_all:
            cl = expd[expd["n_clean"] > 0].sort_values(["n_clean", "mz_clean"], ascending=[False, False])
            keep[cl.index[:top].to_numpy()] = True
        shown = expd[keep]
        rest = expd[~keep]
        rows, legend, cav_legend, n_extra = [], {}, {}, 0

        def caveat_mark(nm, flags):
            """' +' after a name whose cell carries a caveat (no artifact flag: e.g. a rise under a translation
            inhibitor, read from this line's own change); its words go to the legend under the table."""
            cv = _caveats(flags)
            if not cv:
                return ""
            names = cav_legend.setdefault(cv, [])
            if nm not in names:
                names.append(nm)
            return " +"

        def best(r, k, s_):
            """(cell text, fold, z, alert) of the strongest drug-dose of a line in direction k ('' when none), its
            alert (⚠ before the name) and its caveats (' +' after it, words under the table)."""
            if not s_ * _num(r.get(f"best_{k}_z{sfx}")) >= t_line:
                return None
            fl_ = r.get(f"best_{k}_flags_all") if has_all else None
            al = "" if not has_all or bool(r.get(f"best_{k}_clean_all")) else \
                _alert(fl_, r.get(f"best_{k}_cc_share_all"))
            nm = f"{T.salt_base(_text(r[f'best_{k}_drug{sfx}']))} {_text(r[f'best_{k}_dose{sfx}'])}"
            if al:
                legend.setdefault(nm, al)
            return ((f"{ALERT} " if al else "") + nm + caveat_mark(nm, fl_),
                    _fold(2 ** _num(r[f"best_{k}_lfc{sfx}"])), _z(r[f"best_{k}_z{sfx}"]), al)

        def count(r, k):
            n, nc = (np.nan_to_num(_num(r.get(x))) for x in (f"n_dd_{k}{sfx}", f"n_dd_{k}"))
            return f"{int(n)}" + (f" ({int(n - nc)}{ALERT})" if has_all and n > nc else "")

        for _, r in shown.iterrows():
            row = [_text(r["cell_name"]) or _text(r["cell_line_id"]), organ.get(int(r["line"]), ""),
                   _f(r["baseline_cpm"], "{:,.0f}"), count(r, "up"), count(r, "down")]
            extra = ["", "", "", "", ""]
            need = False
            for k, s_ in (("up", 1), ("down", -1)):
                b = best(r, k, s_)
                row += list(b[:3]) if b else ["-", "", ""]
                cleanb = None
                if b and b[3] and s_ * _num(r.get(f"best_{k}_z")) >= t_line:      # the strongest has an alert: the
                    cnm = f"{T.salt_base(_text(r[f'best_{k}_drug']))} {_text(r[f'best_{k}_dose'])}"
                    cleanb = (f"no artifact flag: {cnm}" + caveat_mark(cnm, r.get(f"best_{k}_flags")),
                              _fold(2 ** _num(r[f"best_{k}_lfc"])), _z(r[f"best_{k}_z"]))   # strongest without one
                    need = True
                extra += list(cleanb) if cleanb else ["", "", ""]
            rows.append(row)
            if need:
                rows.append(extra)
                n_extra += 1
        P += _table(["line", "organ", "CPM", "up", "down", "strongest up", "fold", "z", "strongest down", "fold",
                     "z"], rows, "llrrrlrrlrr", flex=(1, 5, 8), mins={1: 6, 5: 14, 8: 14}, drop=(1, 2))
        n_only = int(((rest["n"] > 0) & (rest["n_clean"] == 0)).sum())
        if len(rest):
            P += _wrap(f"... {len(rest)} more lines" + (f" ({n_only} of them with only flagged drug-doses)"
                                                          if n_only else "") + " (--top N, or --top all); "
                       + _all_at(len(expd), _xu(LK.gene, lab, "lines")), 2, 6)
        if len(shown) > top:
            P += _wrap(f"lines beyond #{top}: among the {top} lines with the most drug-doses without an alert, shown "
                       "so that lines moved only by flagged drug-doses do not push them out", 2, 4)
        if legend:
            P += _wrap(f"{ALERT} " + "; ".join(f"{k} uM: {v}" for k, v in legend.items()) + " (for this gene)"
                       + ("; a 'no artifact flag' row under a line names its strongest drug-dose without an artifact "
                          "flag" if n_extra else ""), 2, 4)
        if cav_legend:
            P += _wrap("+ = a caveat, no artifact flag (read from the line's own change): " + "; ".join(
                f"{', '.join(v)} uM: {k}" for k, v in cav_legend.items()), 2, 4)
            _flag_legend(P, list(cav_legend))
        nexp = le[~le["expressed"].astype(bool)]
        if len(nexp):
            P += _wrap("not measured (not expressed, or only ambient RNA: no per-line values): " +
                       ", ".join(nexp["cell_name"].fillna(nexp["cell_line_id"]).astype(str)), 2, 4)
        n_any = int((expd["n"] > 0).sum())
        P.append(f"  {n_any} of {len(expd)} measured lines have a drug-dose moving it >= 1.5x at per-line "
                 f"|z| >= {t_line:.2f}" + (f"; in {int((expd['n_clean'] > 0).sum())} of them a drug-dose without "
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
                "half = strong in one of the two random halves only (not the same sign in both, no error estimate), "
                f"{ALERT} not repro = neither; {ALERT} after a gene = it is in the vector space only through "
                f"drug-doses with an artifact flag; {ALERT} locus / readthrough? = neighbours on the genome, which "
                f"can correlate for that reason alone; {ALERT} lineage = both genes are expressed in few lines, "
                "mostly the same (lines of each, overlap J, lineage p); "
                f"{ALERT} copies = paralogues, pseudogenes or read-through transcripts whose reads can be counted for "
                "either gene; module = the partner's module and arm; rows with an alert "
                "keep their place") if sign > 0 else "the same columns")
        rel = o.pq("relations/gene_relations.parquet", columns=REL_COLS, filters=[("col_a", "==", int(c))])
        rows, n, n_al = _partner_rows(o, rel, top, sign)
        if not rows:
            P.append(f"  none among its top {len(rel)} partners by |cos|")
            continue
        P += _table(PARTNER_HEAD, rows, "lrrlrlll", flex=(6, 7, 0), mins={6: 18, 7: 14, 0: 8}, drop=(7, 5))
        if len(rows) < n:
            P += _wrap(f"... {n - len(rows)} more on this side (--top N, or --top all); "
                       + _all_at(n, _xu(LK.gene, lab, "partners")), 2, 6)
        rep = rel[(np.sign(rel["cos"]) == sign) & (rel["evidence"] == "both halves")]
        if "fdr" in rep:
            rep = rep[rep["fdr"].fillna(1.0) <= REPRO_FDR]
        P.append(f"  {n} of its top {len(rel)} partners by |cos| are on this side, {n_al} of them with an alert "
                 f"({ALERT}); {len(rep)} with the {SAME_SIGN} (fdr <= {REPRO_FDR:g})"
                 + (f", {int((rep['fdr'] <= 0.05).sum())} of them at fdr <= 0.05" if "fdr" in rep else ""))
        if sign < 0:
            P += _wrap(f"{SAME_SIGN}: {SAME_SIGN_NOTE}", 2, 4)
        ok_nov, blocked = o.novelty()
        if sign < 0 and not ok_nov:
            P += _wrap(f"novelty not assessed: {', '.join(blocked) or 'reference sources'} missing "
                       "(relations/info.json), so no pair is called NOVEL", 2, 4)

    # probable direction
    _dir_gene(o, P, int(c), lab, top)

    # where
    tb = [["drug-doses (pooled)", o.p("tables", "drug_effects.parquet"), f"col == {c}"],
          ["per line", o.p("tables", "line_effects.parquet"), f"col == {c}"],
          ["drug-dose x line", o.p("tables", "drug_line_top.parquet"), f"col == {c}"]]
    if o.ran("relations"):
        tb.append(["partners", o.p("relations", "gene_relations.parquet"), f"col_a == {c}"])
    if o.ran("tensor"):
        tb.append(["every drug-dose x line", (o.p("tensor", "DDL_lfc.npy"), " / DDL_z.npy"), f"[{c}] (dd x line)"])
    _dir_where(o, tb, f"source_col == {c} or target_col == {c}")
    vn = _vault_note(o, "Genes", lab)
    if vn:
        tb.append(["vault note", vn, ""])
    if o.ran("map"):
        tb.append(["map", o.p("map", "gene_map.html") + "#" + lab, ""])
    _where(o, P, tb)
    return P


def _is_direction_source(o, name):
    """The name (any case) is the source of a probable-direction edge. Reads one column only, so that a mistyped
    name does not load the whole direction table. Read by Arrow from the path, in this thread: a pandas read hands
    Arrow a Python file object, which Arrow may still be releasing in a thread of its own when the process ends
    right after (a name not found), and that can hang the exit."""
    if not o.ran("direction"):
        return False
    try:
        import pyarrow.parquet as pq
        srcs = pq.read_table(o.p("direction", "edges.parquet"), columns=["source"], use_threads=False,
                             pre_buffer=False).column("source").to_pylist()
    except Exception:  # noqa: BLE001  (unreadable: the name is simply not found)
        return False
    return name.strip().strip(",;").upper() in {str(x).upper() for x in srcs}


def _unmeasured_source(o, name, top):
    """The look-up of a name that is no gene of this run but the source of probable-direction arrows (a drug target
    or a recorded driver gene the screen does not measure): its arrows, else [] (the caller reports the name as not
    found)."""
    key = name.strip().strip(",;")
    if not _is_direction_source(o, key):
        return []
    dv, _w = _direction(o)
    if dv is None or not (len(dv.downstream(key)) or len(dv.cells(key))):
        return []
    rows = dv.downstream(key)
    rows = rows if len(rows) else dv.cells(key)
    lab = next((s_ for s_ in rows.iloc[0]["sources"] if str(s_).upper() == key.upper()), key)
    P = [f"{lab}   not a measured gene of this run"]
    P += _wrap("No gene of this run has this symbol, label, Ensembl id or alias, but it is the source of "
               "probable-direction arrows: a gene that compounds of the screen target, or a driver gene recorded in "
               "Tahoe's cell-line genetics, whose own mRNA is not among the genes measured here.", 2, 4)
    _dir_gene(o, P, key, lab, top)
    tb = []
    _dir_where(o, tb, f"source == '{lab}' (or among the names of a row naming several)")
    _where(o, P, tb)
    return P


def cmd_gene(o, names, top):
    o.require("effects", "tables")
    P = []
    for i, nm in enumerate(names):
        try:
            cols, how = resolve_gene(o, nm)
        except NotFound:
            alt = _unmeasured_source(o, nm, top)
            if not alt:
                raise
            P += (["", "=" * min(WIDTH, 100), ""] if i else []) + alt
            continue
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
    for k, nm in (("approved", "approved"),):
        v = _text(r0.get(k, ""))
        if v:
            meta.append(f"{nm}: {v}")
    if meta:
        P += _wrap("   ".join(meta), 2, 4)
    salt = _salt_alert(o, drug)
    if salt:
        P += _wrap(f"{ALERT} salt forms: {salt}", 2, 4)
    P += _annotations(o, drug, dr, r0)
    if dr is not None:
        P += _wrap(f"doses (uM): {_text(dr['doses'])}   significant genes: {_text(dr['n_sig_by_dose'])}   best dose: "
                   f"{_text(dr['best_dose'])}   lowest active dose: {_text(dr['lowest_active_dose']) or 'none'}   "
                   f"signature r between doses: {_text(dr['signature_r_between_doses']) or '-'}", 2, 4)
    by_dose = _parse_dose_plates(_text(dr.get("dose_plates")) if dr is not None else "")
    _title(P, "PER DOSE", "genes: significant at q < 0.10 and fold >= 1.2x / <= 1/1.2; cells: log2 vs the plate; "
                          "plate well: where the dose sits (each dose of a drug on its own plate, so a pattern over "
                          "the "
                          "doses compares plates as much as doses)"
           + ("; this drug's doses share a plate" if dr is not None and _yes(dr.get("doses_share_a_plate")) else ""))
    rows = []
    for _, r in rows_dd.iterrows():
        nw = _int(r.get("n_wells"))
        nwa = _num(r.get("n_wells_all"))
        if np.isfinite(nwa) and nwa != _num(r.get("n_wells")):
            nw += f" of {int(nwa)}"
        pw = by_dose.get(_text(r["dose"]))
        where = ", ".join(pw) if pw else _text(r.get("plates")).replace(",", ", ") + " (wells " + \
            _text(r.get("wells")).replace(",", ", ") + ")"
        rows.append([r["dose"], nw, where, _int(r.get("n_genes_up")),
                     _int(r.get("n_genes_down")), _f(r.get("replicate_r")), _f(r.get("cells_log2_vs_plate"), "{:+.2f}"),
                     _flags_shown(r["flags"])])
    P += _table(["uM", "wells", "plate well", "up", "down", "rep r", "cells", "flags"], rows, "lllrrrrl",
                flex=(2, 7), mins={2: 12, 7: 16})
    if rows_dd["artifact"].any():
        P += _wrap(f"{ALERT} = an artifact flag of the drug-dose; it is shown with all its genes below. For a "
                   "cell-cycle shift the tables decide per gene whether the shift explains the change (genes whose "
                   f"change it does not explain carry no {ALERT})", 2, 4)
    _flag_legend(P, rows_dd["flags"].tolist())
    _per_dose_notes(o, P, rows_dd)

    # top genes per dose
    cols = ["col", "symbol", "dd", "lfc", "fold", "z", "q_up", "q_down", "flags", "clean", "n_lines_measured",
            "n_lines_up", "n_lines_down", "cc_share", "n_wells", "lfc_vs_dmso"]
    de = o.pq("tables/drug_effects.parquet", columns=cols, filters=[("dd", "in", dds)])
    if "cc_share" not in de:                     # an older tables stage
        de["cc_share"] = np.nan
    has_dmso = "lfc_vs_dmso" in de               # tables version 5: the rough DMSO-referenced lfc (a sign check)
    de["flags"] = de["flags"].fillna("").astype(str) if "flags" in de else ""
    g = o.genes()
    n_tabs = 0                                   # doses with a TOP GENES table (the vs DMSO legend follows them)
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
            own = [f for f in str(y["flags"]).split("; ") if f in CM.ARTIFACT_FLAGS and f not in dose_art]
            words = _alert("; ".join(own), y["cc_share"], "short")
            return ALERT + (f" {words}" if words else "")
        if not len(up) and not len(dn):
            P.append("  no significant genes")
            continue
        sides = []
        for part in (up, dn):
            ok = part["clean"].astype(bool).to_numpy()
            sides.append((part, _capped(len(part), top, ok)))
        side_rows = []
        for (part, show), key in zip(sides, ("n_lines_up", "n_lines_down")):
            rr = []
            for j in show:
                y = part.iloc[j]
                rr.append([str(j + 1), g.at[int(y["col"]), "label"], _fold(y["fold"]),
                           _dmso(y.get("lfc_vs_dmso"), y["lfc"], short=True) if has_dmso else "", _z(y["z"]),
                           f"{int(y[key])}/{int(y['n_lines_measured'])}{_wells(y.get('n_wells', r.get('n_wells')))}",
                           gene_alert(y)])
            side_rows.append(rr)
        tabs = _top_genes_table(side_rows, has_dmso)       # one table side by side, or [raised, lowered]
        n_tabs += 1
        for k, ((part, show), word) in enumerate(zip(sides, ("raised", "lowered"))):
            if len(tabs) == 2 or k == 0:
                P += tabs[k]
            al = ~part["clean"].astype(bool).to_numpy()
            more = _more(len(part), len(show), int(al.sum()) - int(al[show].sum()), word, url=_xu(LK.dd, d))
            if more:
                P += _wrap(more.strip(), 2, 6)
        P += _wrap(f"every gene at {r['dose']} uM (pooled and per line, exact): {_xu(LK.dd, d)}", 2, 6)
    if has_dmso and n_tabs:
        P += _wrap("vs DMSO = the rough DMSO-referenced fold (tables/drug_effects lfc_vs_dmso: a sign check against "
                   "the plate's two DMSO wells, not a replacement); * = at least 1.2x the other way (other sign); "
                   "none = the plate has no DMSO value", 2, 4)

    _similar(o, P, drug, dr, top)
    _line_controls(o, P, drug)

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
            show = _capped(len(cand), top, ok)
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
                more = _more(len(cand), len(show), int((~ok).sum()) - int((~ok[show]).sum()), "drugs",
                             url=_xu(LK.drug, drug))
                if more:
                    P += _wrap(more.strip(), 2, 6)
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
        moved = [m for m in np.argsort(-best, kind="stable") if best[m] > 0]
        order = moved[:top]
        rows = []
        for m in order:
            mr = mods.iloc[m]
            rows.append([str(int(mr["module"])), _int(mr["n_genes"])] + [_z(v) for v in M[m]] +
                        [o.module_label(int(mr["module"]))])
        P += _table(["module", "genes"] + [f"{x} uM" for x in rows_dd["dose"]] + ["label"], rows,
                    "rr" + "r" * len(dds) + "l", flex=(2 + len(dds),), mins={2 + len(dds): 16})
        P += _wrap(f"{len(moved):,} of the {len(mods):,} modules have a score at its doses, ranked by the largest "
                   f"|score|; {len(order):,} shown", 2, 4)
        more = _more(len(moved), len(order), 0, "modules", url=_xu(LK.drug, drug))
        if more:
            P += _wrap(more.strip(), 2, 6)

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
        P += _wrap(f"{_n_alert(len(rows), int((~ok).sum()), 'dose x line pairs')}"
                   + (f"; {len(rows) - len(show)} more (--top N, or --top all); "
                      + _all_at(len(rows), _xu(LK.drug, drug)) if len(rows) > len(show) else ""), 2, 6)
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
        k = min(top, 8 if not TOP_GIVEN else top, len(o_) // 2)   # 'most' and 'least' never share a line
        fl = _artifacts(r["flags"])
        P += _wrap(f"{r['dose']} uM ({len(o_)} lines{f'; {ALERT} ' + fl if fl else ''}): most: "
                   + ", ".join(f"{ln.at[l, 'name']} {b[l]:.2f}" for l in (o_[:k] if k else o_))
                   + (";  least: " + ", ".join(f"{ln.at[l, 'name']} {b[l]:.2f}" for l in o_[::-1][:k]) if k else "")
                   + (f" ({2 * k} of {len(o_)} lines named, --top N; {_all_at(len(o_), _xu(LK.dd, int(r['dd'])))})"
                      if k and 2 * k < len(o_) else ""), 2, 4)
    if not any_beta:
        P.append("  no estimate at any dose (fewer than 20 significant genes)")

    _dir_drug(o, P, drug, dds, top)

    tb = [["per dose", o.p("tables", "drugdoses.parquet"), "dd in " + str(dds)],
          ["genes", o.p("tables", "drug_effects.parquet"), "dd in " + str(dds)]]
    _dir_where(o, tb, f"target_dd in {dds}; drug_target: compounds")
    vn = _vault_note(o, "Drugs", drug + " (drug)")
    if vn:
        tb.append(["vault note", vn, ""])
    _where(o, P, tb)
    return P


def _older(o, stage, what, version):
    """'[what: ...]' for a file a stage writes from `version` on: the stage has not run, or ran with an older version
    (then `tahoe run` redoes it)."""
    if not o.ran(stage):
        return o.missing_note(stage, what)
    return (f"[{what}: this output's {stage} stage is older than version {version}, which writes it; `tahoe run` "
            "redoes it]")


def _parse_dose_plates(text):
    """tables drugs.parquet dose_plates ('0.05: plate1 H6, plate2 B2 / 0.5: plate3 C9') as
    {dose: ['plate1 H6', ...]}."""
    out = {}
    for part in str(text or "").split(" / "):
        dose, sep, rest = part.partition(": ")
        if sep:
            out[dose.strip()] = [x.strip() for x in rest.split(", ") if x.strip()]
    return out


def _salt_alert(o, drug):
    """embed/drugs.parquet salt_form_alert of the drug ('' when none or an older embed stage)."""
    if not o.has("embed/drugs.parquet"):
        return ""
    e = o.pq("embed/drugs.parquet")
    if "salt_form_alert" not in e:
        return ""
    hit = e[e["drug"].astype(str) == drug]
    return _text(hit["salt_form_alert"].iloc[0]) if len(hit) else ""


def _chembl_release(o):
    """'ChEMBL 37' (tables/info.json chembl_release; reference/sources.json) or 'ChEMBL'."""
    rel = _text(o._info("tables/info.json").get("chembl_release"))
    if not rel:
        rel = _text(((o._info("reference/sources.json").get("sources") or {}).get("chembl") or {}).get(
            "chembl_release"))
    return rel if rel.lower().startswith("chembl") else (f"ChEMBL {rel}" if rel else "ChEMBL")


def _annotations(o, drug, dr, r0):
    """ANNOTATIONS of a drug: Tahoe's (verbatim) and ChEMBL's side by side, an alert where they disagree, the notes,
    and its mechanism classes with their sources (tables/drugs.parquet; else mechanisms.drug_annotations)."""
    a = {}
    if dr is None or "annotation_status" not in dr:
        try:
            ann = MECH.drug_annotations(o.out)
            hit = ann[ann["drug"].astype(str) == drug]
            a = hit.iloc[0].to_dict() if len(hit) else {}
        except Exception:  # noqa: BLE001
            a = {}

    def g(k):
        return _text(dr.get(k)) if dr is not None and k in dr else _text(a.get(k))
    P = []
    _title(P, "ANNOTATIONS - Tahoe's and ChEMBL's, side by side", "neither replaces the other; "
           f"{ALERT} where they disagree; tables/drugs.parquet, reference/drug_annotations.parquet")
    P += _wrap(f"Tahoe: targets {_text(r0.get('targets')) or 'none listed'}; mechanism "
               f"{_text(r0.get('moa_fine')) or 'none listed'}"
               + (f" ({_text(r0.get('moa_broad'))})" if _text(r0.get("moa_broad")) else "") + ".", 2, 4)
    status, cid = g("annotation_status"), g("chembl_id")
    if not status or status == MECH.NOT_LOADED:
        P += _wrap("ChEMBL: not loaded in this run (`tahoe run --from reference` with network access fetches it)",
                   2, 4)
    elif not cid:
        P += _wrap("ChEMBL: not found in ChEMBL.", 2, 4)
    else:
        P += _wrap(f"{_chembl_release(o)}: {g('chembl_name') or '-'} ({cid}); mechanisms "
                   f"{g('chembl_mechanisms') or 'none curated'}; targets {g('chembl_targets') or 'none listed'}. "
                   f"Matched by {g('chembl_matched_by') or 'name'}.", 2, 4)
    if g("annotation_alert"):
        P += _wrap(f"{ALERT} the two annotations disagree: {g('annotation_alert')}", 2, 4)
    for x in [y.strip() for y in g("annotation_note").split(" | ") if y.strip()]:
        P += _wrap(f"note: {x}", 2, 4)
    if g("mechanism_classes"):
        P += _wrap(f"class: {g('mechanism_classes')}", 2, 4)
    return P


def _per_dose_notes(o, P, rows_dd):
    """Under PER DOSE: each dose's neighbouring-well reading (drugdoses.parquet nb_alert: tier 'artifact' is an
    artifact flag, the others a note), an unexpected similarity to another class (embed/drugdoses.parquet
    resembles_note), its selective lines (drugdoses.parquet selective_lines) and the comparison groups that explain
    them (direction/selectivity.parquet)."""
    res = {}
    if o.has("embed/drugdoses.parquet"):
        e = o.pq("embed/drugdoses.parquet")
        if "resembles_note" in e:
            res = {int(d): _text(t) for d, t in zip(e["dd"], e["resembles_note"]) if _text(t)}
    sel = {}
    if o.has("direction/selectivity.parquet"):
        sp_ = o.pq("direction/selectivity.parquet")
        sel = {int(r["dd"]): r for r in sp_.to_dict("records")}
    dd = o.drugdoses()
    lab = dict(zip(dd["dd"].astype(int), dd["label"]))
    any_ = False
    for _, r in rows_dd.iterrows():
        d = int(r["dd"])
        items = []
        tier = _text(r.get("nb_tier"))
        if tier:
            p_ = int(_num(r.get("nb_partner_dd"))) if np.isfinite(_num(r.get("nb_partner_dd"))) else -1
            head = f"{ALERT} like a neighbouring well" if tier == "artifact" else f"neighbouring well ({tier})"
            items.append(f"{head}: {_text(r.get('nb_alert'))}" + (f" [the neighbour: {lab[p_]} uM]" if p_ in lab
                                                                 else ""))
        if res.get(d):
            items.append(f"resembles another class: {res[d]}")
        if np.isfinite(_num(r.get("n_selective_lines"))) and int(_num(r.get("n_selective_lines"))) > 0:
            items.append(f"selective lines ({int(_num(r.get('n_selective_lines')))}): "
                         f"{_text(r.get('selective_lines'))}")
            x = sel.get(d)
            if x is not None:
                if _text(x.get("organs_enriched")):
                    items.append(f"organs enriched among them: {_text(x.get('organs_enriched'))}")
                if _text(x.get("groups")):
                    items.append(f"comparison groups that explain them: {_text(x.get('groups'))}")
        if items:
            if not any_:
                _title(P, "NOTES PER DOSE", "neighbouring wells, an unexpected similarity, lines that respond out of "
                                            "proportion (selective: sel_z >= 3 with >= 20 genes)")
                any_ = True
            P += _wrap(f"{r['dose']} uM: " + items[0], 2, 6)
            for x in items[1:]:
                P += _wrap(x, 6, 8)
    return any_


def _similar(o, P, drug, dr, top):
    """MOST SIMILAR DRUG-DOSES of the drug's best dose (embed/drug_similarity.parquet: the 50 most similar, rank
    order): cos of the pooled signatures and of the per-line contexts, shared significant genes, same compound, the
    other's classes and flags; --top N rows (default N_SIMILAR), '{k} of 50 shown'. A best dose with no pooled
    signature (every cos_pooled NaN) has no ranking: _similar_rows says so."""
    note = ("embed/drug_similarity.parquet; shared = genes significant in both; class = the other's mechanism classes; "
            "alert = the other's artifact flags")
    if not o.has("embed/drug_similarity.parquet"):
        _title(P, "MOST SIMILAR DRUG-DOSES - of its best dose, by the cosine of the pooled signatures", note)
        P += _wrap(_older(o, "embed", "drug-dose similarity", 5), 2, 4)
        return
    bdd = int(_num(dr.get("best_dd"))) if dr is not None and np.isfinite(_num(dr.get("best_dd"))) else -1
    if bdd < 0:
        _title(P, "MOST SIMILAR DRUG-DOSES - of its best dose, by the cosine of the pooled signatures", note)
        P.append("  no best dose (no dose with significant genes)")
        return
    sim = _sim_rows_of(o, bdd)                          # read once: the title and the rows
    if _sim_no_signature(sim):
        _title(P, "MOST SIMILAR DRUG-DOSES - of its best dose: no ranking (it has no pooled signature)",
               "embed/drug_similarity.parquet")
    else:
        _title(P, "MOST SIMILAR DRUG-DOSES - of its best dose, by the cosine of the pooled signatures", note)
    _similar_rows(o, P, bdd, top if TOP_GIVEN else N_SIMILAR, sim)


def _line_controls(o, P, drug):
    """LINE-SELECTIVE CONTROLS that use the drug (validation/line_controls.csv; nothing when none)."""
    if not o.has("validation/line_controls.csv"):
        return
    lc = pd.read_csv(o.p("validation", "line_controls.csv"))
    lc = lc[lc["drug"].astype(str) == drug] if "drug" in lc else lc.iloc[:0]
    if not len(lc):
        return
    _title(P, "LINE-SELECTIVE CONTROLS - known line-selective responses the validation stage checks with this drug",
           "validation/line_controls.csv: AUROC of the lines' selectivity, group lines vs the others, permutation p")
    P += _table(["control", "uM", "AUROC", "p", "AUROC (strength)", "selective lines", "note"],
                [[_text(r.get("control")), _text(r.get("dose")), _f(r.get("auroc")), _q(r.get("p")),
                  _f(r.get("auroc_response_strength")), _text(r.get("selective_lines")) or "-",
                  _text(r.get("note")) or "-"] for r in lc.to_dict("records")], "llrrrll", flex=(0, 5, 6),
                mins={0: 16, 5: 10, 6: 8})


def _class_labels(o):
    """{drug: 'label; label'} of the mechanism classes (mechanisms.classes_by_drug: reference/'s files, else the code
    constants for the drugs of atlas/effects; an exported results folder without either: the code constants for the
    drugs of tables/drugs.parquet)."""
    def load():
        try:
            keys = MECH.classes_by_drug(o.out)
        except Exception:  # noqa: BLE001
            keys = {}
        if not keys and o.has("tables/drugs.parquet"):
            try:
                t = o.pq("tables/drugs.parquet").copy()
                for c in ("targets", "moa_fine", "moa_broad", "pubchem_cid"):
                    if c not in t:
                        t[c] = ""
                K = MECH.assign_classes(t[["drug", "targets", "moa_fine", "moa_broad", "pubchem_cid"]], None)[2]
                for d, c in zip(K["drug"].astype(str), K["class"].astype(str)):
                    keys.setdefault(d, []).append(c)
            except Exception:  # noqa: BLE001
                keys = {}
        return {d: "; ".join(MECH.class_info(k).get("label", k) for k in dict.fromkeys(v)) for d, v in keys.items()}
    return o._cached("class_labels", load)


def _sim_rows_of(o, dd):
    """The rows of embed/drug_similarity.parquet for drug-dose dd, in rank order."""
    return o.pq("embed/drug_similarity.parquet", filters=[("dd", "==", int(dd))]).sort_values("rank")


def _sim_nan(sim):
    """True per row where cos_pooled is NaN: one of the two drug-doses has no pooled signature."""
    return ~np.isfinite(pd.to_numeric(sim["cos_pooled"], errors="coerce").to_numpy(float)) if len(sim) else \
        np.zeros(0, bool)


def _sim_no_signature(sim):
    """True when every stored cos_pooled of the drug-dose is NaN: it moves no gene at |z| >= KEEP_Z or q < Q_CUT
    (embed's pooled signature), so every cosine with it is undefined and the embed stage's 50 rows are the first
    other drug-doses in row order, not a ranking (the explorer's Similar drug-doses tab says the same)."""
    return bool(len(sim)) and bool(_sim_nan(sim).all())


def _sim_cut():
    return f"|z| >= {TB.KEEP_Z:g} or q < {Q_CUT:.2f}"


def _dd_row_count(o, rel, dd):
    """The rows of drug-dose dd in the parquet table rel, from its dd column read by one thread with the file reader
    (pyarrow ParquetFile.read). A threaded read of that one column after other reads left the look-up hanging at its
    exit (in pyarrow's thread pools) in about 1 run in 10 on the test machine; with this read, 0 of 200 runs hung."""
    import pyarrow.parquet as pq
    t = pq.ParquetFile(o.p(rel)).read(columns=["dd"], use_threads=False)
    return int((t.column("dd").to_numpy() == int(dd)).sum())


def _sim_noise(o, dd):
    """'' or, when drug-dose dd has rows in tables/drug_effects although it has no pooled signature (they are all
    noise-class RNAs, which the signature leaves out), ' other than noise-class RNAs (its N rows of ...)'."""
    try:
        n = _dd_row_count(o, "tables/drug_effects.parquet", dd)
    except Exception:  # noqa: BLE001  (an output without the table: the plain words)
        n = 0
    return (f" other than noise-class RNAs (its {n} row{'s' if n != 1 else ''} of tables/drug_effects, which the "
            "signature leaves out)" if n else "")


def _similar_rows(o, P, dd, n, sim=None):
    """The rows of embed/drug_similarity.parquet for drug-dose dd, the n first (TOP_ALL: all), with the counts. A
    drug-dose with no pooled signature (every cos_pooled NaN): 'no similarity ranking: ...', where the stored rows
    are, and the rows (as stored, in row order) only when --top is given. Rows whose other drug-dose has no pooled
    signature (cos_pooled NaN, last in rank order) are counted and named as such."""
    sim = _sim_rows_of(o, dd) if sim is None else sim    # sim: the rows already read (_sim_rows_of)
    if not len(sim):
        P.append("  no row in embed/drug_similarity.parquet for this drug-dose")
        return
    dl = o.drugdoses()
    nm = f"{dl.at[int(dd), 'label']} uM" if int(dd) in dl.index else f"drug-dose {dd}"
    nan = _sim_nan(sim)
    if nan.all():
        P += _wrap(f"no similarity ranking: {nm} moves no gene at {_sim_cut()}{_sim_noise(o, dd)} (no pooled "
                   f"signature); the {len(sim)} stored rows are the first other drug-doses in row order, not a ranking",
                   2, 4)
        suf = "" if SITE else " (this output's explorer, once the explorer stage has run)"
        P += _wrap(f"the {len(sim)} stored rows: embed/drug_similarity.parquet (dd == {int(dd)}) and the explorer's "
                   f"Similar drug-doses tab: {_xu(LK.dd, int(dd), 'similar')}; the cosine of its vector with all "
                   f"{len(dl) - 1:,} other drug-doses: the explorer's Vector space tab: "
                   f"{_xu(LK.dd, int(dd), 'space')}{suf}"
                   + ("" if TOP_GIVEN else "; --top N or --top all lists the stored rows here, in row order"), 2, 4)
        if not TOP_GIVEN:
            return
    lab = _class_labels(o)
    shown = sim.head(n)
    rows, cavs, fls = [], [], []
    for r in shown.to_dict("records"):
        fl = _text(r.get("other_flags"))
        fls.append(fl)
        if _caveats(fl):
            cavs.append(f"{'row ' if nan.all() else '#'}{int(r['rank'])} {_caveats(fl)}")
        rows.append([str(int(r["rank"])), f"{_text(r['other_drug'])} {_text(r['other_dose'])}",
                     _cos(r.get("cos_pooled")), _cos(r.get("cos_contexts")), _int(r.get("n_shared_sig")),
                     "yes" if _yes(r.get("same_salt_base")) else "",
                     lab.get(_text(r["other_drug"]), "") or "-", _alert_cell(fl)])
    al_any = any(x[-1] for x in rows)
    P += _table(["#" if not nan.all() else "row", "drug uM", "cos", "lines", "shared", "same", "class"]
                + (["alert"] if al_any else []),
                [x if al_any else x[:-1] for x in rows], "rlrrrlll"[:8 if al_any else 7],
                flex=(1, 6) + ((7,) if al_any else ()), mins={1: 16, 6: 14, 7: 14})
    if cavs:
        P += _wrap("caveats (no alert): " + "; ".join(cavs), 2, 4)
    _flag_legend(P, fls)
    if nan.all():
        P += _wrap(f"{len(shown)} of the {len(sim)} stored rows shown, as stored (row = the order of the stored rows, "
                   f"not a ranking; cos '-': {nm} has no pooled signature)"
                   + (f"; {_all_at(len(sim), _xu(LK.dd, int(dd), 'similar'))}" if len(shown) < len(sim) else ""),
                   2, 4)
        return
    if nan.any():
        k_nan = int(nan.sum())
        P += _wrap(f"{k_nan} of the {len(sim)} stored rows (rank {int(sim['rank'].iloc[int(np.argmax(nan))])} on) have "
                   f"no cos: those other drug-doses have no pooled signature (they move no gene at {_sim_cut()}), so "
                   "they come last, in row order, not ranked; "
                   f"{int(nan[:len(shown)].sum())} of them shown", 2, 4)
    P += _wrap(f"{len(shown)} of {len(sim)} shown (the {len(sim)} most similar to {nm}; cos = of the pooled "
               "signatures, lines = over the per-line contexts ('-' where they share too few); same = another dose or "
               "salt form of the same compound)"
               + (f"; --top N or --top all for more; {_all_at(len(sim), _xu(LK.dd, int(dd)))}" if len(shown) < len(sim)
                  else ""), 2, 4)


def _dir_drug(o, P, drug, dds, top):
    """The drug's PROBABLE DIRECTION: the genes that set how the cells fare under it (sensitivity rows whose target is
    one of its drug-doses: dv.for_drugdose) and the drug-target rows of the compound classes it belongs to
    (dv.drug_targets: by name or salt base), each saying whether this drug is one of the compounds that move the
    gene that way."""
    _title(P, "PROBABLE DIRECTION - genes that set how the cells fare under it, and what acting on its targets "
              "probably does", DV.CAVEAT_SHORT + "; direction/edges.parquet")
    dv, why = _direction(o)
    if dv is None:
        P += _wrap(_dir_missing(o, why), 2, 4)
        return
    n = _dir_n(top)
    pos = np.unique(np.concatenate([np.zeros(0, dtype=np.int64)] + [
        dv.for_drugdose(int(d))["order"].to_numpy(dtype=np.int64) for d in dds]))
    cells = dv.rows.iloc[pos]
    tg = dv.drug_targets(drug)
    if not len(cells) and not len(tg):
        P += _wrap("none: no gene was found to set how the cells fare under it, and it is not one of the compounds of "
                   "a drug-target arrow (a class of >= 2 compounds sharing a listed target and mechanism).", 2, 4)
        P += _wrap(_dt(DV.CAVEAT), 2, 4)
        return
    url = _xu(LK.drug, drug, "direction")
    _dir_list(P, "genes that set how the cells fare under it (arrows gene → the cells under one of its doses: their "
                 "numbers relative to the other lines in the same wells)", cells, n, url=url)
    keys = {drug.lower(), str(T.salt_base(drug)).lower()}

    def mine(r):
        sup = [y for x in _text(r.get("compounds_supporting", "")).split("; ") for y in x.split(" / ") if y]
        ok = any(k in keys for x in sup for k in (x.lower(), str(T.salt_base(x)).lower()))
        return "this drug moves it that way too" if ok else \
            "this drug does not move it that way (the class's other compounds do)"
    _dir_list(P, "its targets: what acting on them probably does (drug-target arrows of the compound classes it "
                 "belongs to - compounds sharing a listed target and mechanism, one molecule counted once under all "
                 "its names: the target → a gene whose level those compounds move; a row naming several targets is "
                 "one test, any of them could be the cause)", tg, n, extra=mine, url=url)
    _dir_legend(P)


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


def _in_lines(name, txt):
    """True when the line `name` is one of the ', '-joined cell names of a groups.parquet line list (a name that
    itself contains ', ' too)."""
    txt = _text(txt)
    return bool(name) and (name in txt.split(", ") or f", {name}, " in f", {txt}, ")


def _dir_group_rows(o, dv):
    """groups.parquet description -> positions (in ORDER) of the genotype and expression-null display rows that came
    out of the comparison (cached)."""
    def load():
        r = dv.rows
        out = {}
        if len(r):
            sub = r["kind"].astype(str).str.startswith(("genotype", "null")).to_numpy()
            for i, g in zip(np.flatnonzero(sub), r["group"].astype(str).to_numpy()[sub]):
                out.setdefault(g, []).append(int(i))
        return {k: np.array(v, dtype=np.int64) for k, v in out.items()}
    return o._cached("dir_group_rows", load)


def _dir_groups_block(o, P, dv, recs, n, what, url=None):
    """Comparison groups (groups.parquet records) as a ranked list - most arrows first, then the best grade, then the
    gene - capped by the cap rule on the groups' own alerts: per group its comparison, its arrows by target (a gene's
    drug response / its level / the cells) and grade, how it was compared, and its alerts. Returns the positions of
    all their rows (in ORDER)."""
    gpos = _dir_group_rows(o, dv)
    rows = dv.rows

    def info(rec):
        pos = gpos.get(_text(rec.get("description")), np.zeros(0, dtype=np.int64))
        kinds = rows["kind"].to_numpy()[pos].astype(str)
        grades = rows["grade"].to_numpy()[pos].astype(str)
        return pos, kinds, grades
    ranked = []
    for rec in recs:
        pos, kinds, grades = info(rec)
        best = min((DV.GRADES.index(g_) for g_ in grades if g_ in DV.GRADES), default=9)
        ranked.append((-len(pos), best, _text(rec.get("gene")).lower(), _text(rec.get("description")), rec, pos,
                       kinds, grades))
    ranked.sort(key=lambda t: t[:4])
    al = np.array([bool(_text(t[4].get("alerts"))) for t in ranked], dtype=bool)
    keep = cap_keep(al, n)
    allpos = [t[5] for t in ranked]
    for k in keep:
        _a, _b, _c, desc, rec, pos, kinds, grades = ranked[int(k)]
        pre = "genotype" if rec.get("kind") == "genotype" else "null"
        by = ", ".join(f"{w} {int((kinds == f'{pre}_{x}').sum())}" for x, w in (
            ("response", "response"), ("baseline", "level"), ("sensitivity", "cells"),
            ("selectivity", "selectivity")))
        gr = ", ".join(f"{g_} {int((grades == g_).sum())}" for g_ in DV.GRADES)
        n_al = int(rows["has_alert"].to_numpy()[pos].sum()) if len(pos) else 0
        txt = f"{k + 1:>3}  {desc}: " + (f"{len(pos)} arrow{'s' if len(pos) != 1 else ''} ({by}; grade {gr}"
                                         + (f"; {n_al} with an alert {ALERT}" if n_al else "") + ")"
                                         if len(pos) else "no arrow")
        P += _wrap(_dt(txt), 2, 7)
        bits = []
        if pre == "null":
            names = [x for x in _text(rec.get("genes_same_lines")).split(", ") if x] or [_text(rec.get("gene"))]
            if len(names) > 1:                   # every gene of the set (no name is left out)
                bits.append(f"genes absent from exactly these lines: {', '.join(names)}; any of them could be the "
                            "cause")
        bits.append("compared within organs" if bool(rec.get("stratified")) else "compared across organs")
        if _text(rec.get("note")):
            bits.append(_text(rec.get("note")))
        P += _wrap(_dt("; ".join(bits)), 7, 7)
        a = DV.alert_short(_text(rec.get("alerts")), ASCII)
        if a:
            P += _wrap(a, 7, 9)
        nt = DV.notes_short(_text(rec.get("notes")), ASCII)
        if nt:
            P += _wrap(("- " if ASCII else "· ") + f"notes: {nt}", 7, 9)
    rest = np.setdiff1d(np.arange(len(ranked)), keep)
    more = DV.more_text(int(rest.size), int(al[rest].sum()), what)
    if more:
        P += _wrap(_dt(f"... {more} {_top_hint(len(ranked))}" + (f"; {_all_at(len(ranked), url)}" if url else "")),
                   2, 6)
    if len(keep) > n:
        P += _wrap(f"{what} beyond #{n}: among the {n} with the most arrows without an alert, shown so that {what} "
                   "with an alert do not push them out", 4, 6)
    return np.unique(np.concatenate([np.zeros(0, dtype=np.int64)] + allpos))


def _dir_line(o, P, r, top):
    """The line's PROBABLE DIRECTION: its recorded driver alterations as the direction stage grouped them (loss / gain
    of function / any record, each against the lines with no record of the gene) and the genes it does not express
    that served as natural knockouts, each with what came out of it, then the strongest arrows of those groups."""
    _title(P, "PROBABLE DIRECTION - its recorded alterations and the genes it does not express, as the direction stage "
              "compared them", DV.CAVEAT_SHORT + "; direction/groups.parquet, edges.parquet")
    dv, why = _direction(o)
    if dv is None:
        P += _wrap(_dir_missing(o, why), 2, 4)
        return
    names = {x for x in (_text(r.get("cell_name")), _text(r.get("name"))) if x}
    g = dv.groups
    recs = [x for x in (g.to_dict("records") if len(g) else []) if x.get("kind") in ("genotype", "null")]
    alt = [x for x in recs if any(_in_lines(nm, x.get("altered_lines")) for nm in names)]
    n_other = sum(1 for x in recs if x.get("kind") == "genotype"
                  and any(_in_lines(nm, x.get("intact_lines")) for nm in names))
    geno = [x for x in alt if x.get("kind") == "genotype"]
    null = [x for x in alt if x.get("kind") == "null"]
    n = _dir_n(top)
    url = _xu(LK.line, _text(r.get("cell_name")) or _text(r.get("name")))
    P += _wrap(f"recorded alterations - the comparison groups that count this line as altered (Tahoe's cell-line "
               f"genetics: a gene's loss of function, gain of function, or any record, against the lines with no "
               f"record of the gene; a group needs >= 3 lines on each side): "
               f"{_n_alert(len(geno), sum(1 for x in geno if _text(x.get('alerts'))), 'groups')}; in "
               f"{n_other} other groups it is on the 'not recorded' side", 2, 4)
    pos_g = _dir_groups_block(o, P, dv, geno, n, "groups", url) if geno else np.zeros(0, dtype=np.int64)
    P += _wrap(f"genes it does not express (natural knockouts) - genes this line does not express (it reads only the "
               f"well's ambient RNA) while >= 3 other lines do, compared as lines without the gene vs lines "
               f"expressing it: "
               f"{_n_alert(len(null), sum(1 for x in null if _text(x.get('alerts'))), 'line sets')}", 2, 4)
    pos_n = _dir_groups_block(o, P, dv, null, n, "line sets", url) if null else np.zeros(0, dtype=np.int64)
    pos = np.unique(np.concatenate([pos_g, pos_n]))
    if len(pos):
        _dir_list(P, "the strongest arrows of these groups (the same arrows for every line of a group)",
                  dv.rows.iloc[pos], n, url=url)
        _dir_legend(P)
    else:
        P += _wrap(_dt(DV.CAVEAT), 2, 4)


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
    tp = _text(r.get("tp53_status")) or "unknown"
    tp = {"not recorded": "not recorded (presumed wild type, not confirmed)",
          "wild type": "wild type (an older tables stage's word for 'no TP53 alteration recorded')"}.get(tp, tp)
    P += _wrap(f"organ: {_text(r.get('Organ')) or '-'}   TP53: {tp}", 2, 4)
    if _text(r.get("drivers")):
        P += _wrap("drivers: " + _text(r.get("drivers")), 2, 4)
    if _text(r.get("driver_changes")):
        P += _wrap("driver changes: " + _text(r.get("driver_changes")), 2, 4)
    hv = (o._info("direction/info.json").get("heavily_mutated_lines") or {}).get(nm)
    if hv is not None:
        P += _wrap(f"{ALERT} heavily mutated: it records alterations in {int(hv)} driver genes (15 or more): in a "
                   "comparison of genotypes any of its many changes, or the mutation load itself, could be the cause",
                   2, 4)
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
    lurl = _xu(LK.line, _text(r.get("cell_name")) or nm)
    if rows:
        P += _table(["#", "gene", "CPM here", "median other", "x median", "next highest line (CPM)", "lines expr",
                     "alert", "name"], rows, "rlrrrlrll", flex=(5, 8), mins={5: 12, 8: 10})
        n_al = sum(1 for i in order if gene_alert(i))
        P += _wrap(_n_alert(len(order), n_al, f"genes at >= {SPECIFIC_MIN_CPM:g} CPM here, ranked by x median"), 2, 4)
        more = _more(len(order), len(show), n_al - sum(1 for k in show if gene_alert(order[k])), "genes",
                     url=lurl)
        if more:
            P += _wrap(more.strip(), 2, 6)
    else:
        P.append("  none")
    okl = (med_o >= np.log2(20 + 1)) & (nexp >= 0.5 * len(ln)) & np.isfinite(spec)
    kl = top                                   # the cap follows --top (it was 10 at most)
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
        n_al = int(sum(bool(noise[i]) for i in order))
        P += _wrap(_n_alert(len(order), n_al, "genes below 0.5x the median line here"), 2, 4)
        more = _more(len(order), len(show), n_al - int(sum(bool(noise[order[k]]) for k in show)), "genes",
                     url=lurl)
        if more:
            P += _wrap(more.strip(), 2, 6)
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
        more = _more(len(hit), len(show), int((~okd).sum()) - int((~okd[show]).sum()), url=lurl)
        if more:
            P += _wrap(more.strip(), 2, 6)
    else:
        P.append("  none")

    # out of proportion (tables version 5: drug_line_response.parquet)
    _title(P, "RESPONDS OUT OF PROPORTION - drug-doses at which this line moves many more genes than the other lines",
           "tables/drug_line_response.parquet: selective = sel_z >= 3 with >= 20 genes beyond the per-line cut; "
           "abundance z = how its cells fare against the other lines in the same wells (growth); response strength = "
           "slope of its changes on the drug-dose's consensus (1 = a typical line)")
    if not o.has("tables/drug_line_response.parquet"):
        P += _wrap(_older(o, "tables", "line selectivity", 5), 2, 4)
    else:
        dlr = o.pq("tables/drug_line_response.parquet", filters=[("line", "==", int(l))])
        sel = dlr[dlr["selective"].fillna(False).astype(bool)].sort_values("sel_z", ascending=False)
        if len(sel):
            okd = np.array([not CM.has_artifact(f) for f in sel["flags"].fillna("")], dtype=bool)
            show = _capped(len(sel), top, okd)
            P += _table(["#", "drug uM", "genes", "sel_z", "abundance z", "strength", "flags"],
                        [[str(k + 1), f"{_text(x['drug'])} {_text(x['dose'])}", _int(x["n_genes"]),
                          _f(x["sel_z"], "{:.1f}"), _z(x["abundance_z"]), _f(x["response_strength"]),
                          _flags_shown(x["flags"])] for k, x in ((k, sel.iloc[k]) for k in show)],
                        "rlrrrrl", flex=(1, 6), mins={1: 14, 6: 12})
            P += _wrap(_n_alert(len(sel), int((~okd).sum()), "selective drug-doses"), 2, 4)
            more = _more(len(sel), len(show), int((~okd).sum()) - int((~okd[show]).sum()), url=lurl)
            if more:
                P += _wrap(more.strip(), 2, 6)
        else:
            P.append("  none: at no drug-dose does this line respond out of proportion")
        n_dep = int(dlr["depleted"].fillna(False).astype(bool).sum()) if "depleted" in dlr else 0
        if "in_growth_analysis" in dlr:
            ing = bool(dlr["in_growth_analysis"].fillna(False).astype(bool).any())
            P += _wrap(("growth: " + (f"depleted (abundance z <= -3) at {n_dep} of {len(dlr)} drug-doses" if ing else
                                      "not in the growth analysis (no abundance values)")), 2, 4)

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
        more = _more(len(dlt), len(show), int((~okc).sum()) - int((~okc[show]).sum()), url=lurl)
        if more:
            P += _wrap(more.strip(), 2, 6)
    else:
        P.append("  none")
    _dir_line(o, P, r, top)

    tb = [["per gene", o.p("tables", "line_effects.parquet"), f"line == {l}"],
          ["cells", o.p("tables", "drug_line_top.parquet"), f"line == {l}"],
          ["line", o.p("tables", "lines.parquet"), f"line == {l}"]]
    if o.ran("direction") and o.has("direction/groups.parquet"):
        tb.append(["direction (groups)", o.p("direction", "groups.parquet"), "altered_lines / intact_lines"])
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
    lists the drug-dose for the gene; else the same rules applied here with tables.flag_strings: the drug-dose's
    flags of record (tables.dd_flags_of_record) plus 'position correction uncertain' for the gene (atlas DD_posunc),
    the cell-cycle rule (tables.cc_rule on the gene's full-fit slopes, genes.parquet cc_slope_*; the tables stage
    itself judges each drug-dose it lists with the slopes fitted without it), the neighbouring-well genes
    (tables.nb_gene_mask of the gene's DD_z column with drugdoses.parquet nb_partners) and the rise under a
    translation inhibitor (DD_lfc > 0), so the look-up's flags equal drug_effects'. The soft caveats that depend on
    the gene (its plate factor, a position effect removed) are left out of that fallback: it serves the alert, which
    holds artifact flags only."""
    dd = o.drugdoses()
    dds = np.asarray(dds, dtype=np.int64)
    base = TB.dd_flags_of_record(o.out)                      # the flags of record (tables version 5)
    share = np.full(len(dds), np.nan)
    pu = np.asarray(o.eff("DD_posunc")[:, c], dtype=bool)[dds] if o.has("atlas/effects/DD_posunc.npy") else \
        np.zeros(len(dds), dtype=bool)
    lf = np.asarray(o.eff("DD_lfc")[:, c], dtype=np.float64)[dds] if len(dds) else np.zeros(0)
    g = o.genes()
    cc = np.array([TB.CC_FLAG in str(base[d]).split("; ") for d in dds], dtype=bool)
    pct = np.full(len(dds), -1, dtype=np.int64)
    if cc.any() and {"cc_slope_S", "cc_slope_G2M"} <= set(g.columns) and \
            {"S_PHASE_lfc", "G2M_PHASE_lfc"} <= set(dd.columns):
        bS, bG = _num(g.at[c, "cc_slope_S"]), _num(g.at[c, "cc_slope_G2M"])
        S = pd.to_numeric(dd["S_PHASE_lfc"], errors="coerce").to_numpy()[dds]
        G = pd.to_numeric(dd["G2M_PHASE_lfc"], errors="coerce").to_numpy()[dds]
        sh, cleared = TB.cc_rule(lf, bS * S + bG * G)
        share = np.where(cc, sh, np.nan)
        pct = np.where(cc, TB.cc_pct(sh, cleared), -1)
    nb = None                                    # the neighbouring-well genes: a partner moves this gene that way
    if "nb_partners" in dd and len(dds) and o.has("atlas/effects/DD_z.npy"):
        zc = np.asarray(o.eff("DD_z")[:, c], dtype=np.float64)[:, None]
        nb = TB.nb_gene_mask(zc, TB.parse_partners(dd["nb_partners"].fillna("").astype(str).tolist(), len(dd)))[
            :, 0][dds]
    nan = np.full(len(dds), np.nan)
    flags, _clean = TB.flag_strings(base, dds, pu, nan, nan, pct, nb, lf > 0)
    flags = np.asarray(flags, dtype=object).copy()
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


def _dir_pair(o, P, ca, cb, la, lb):
    """PROBABLE DIRECTION between two genes: every display row from one to the other, either way (a row naming
    several sources counts when the gene is one of them), with every alert in full; then the genes with an arrow to
    both (a shared upstream gene, e.g. both follow TP53)."""
    _title(P, "PROBABLE DIRECTION BETWEEN THEM - an arrow from one to the other, either way", DV.CAVEAT_SHORT
           + "; direction/edges.parquet")
    dv, why = _direction(o)
    if dv is None:
        P += _wrap(_dir_missing(o, why), 2, 4)
        return
    any_row = False
    for x, y, lx, ly in ((ca, cb, la, lb), (cb, ca, lb, la)):
        d = dv.downstream(int(x))
        d = d[d["target_col"].to_numpy() == int(y)]
        any_row |= bool(len(d))
        _dir_list(P, DV.arrow(lx, ly, ASCII), d, None, alerts="long")
    if not any_row:
        P += _wrap(f"no arrow between {la} and {lb} in either direction in this run (an arrow needs a test result at "
                   "q < 0.10: a recorded mutation, lines that do not express the source, compounds that target it, or "
                   "its natural level; level arrows are tested for related pairs only)", 2, 4)
    ua, ub = dv.upstream(int(ca)), dv.upstream(int(cb))
    srcs = {}
    for rows, who in ((ua, 0), (ub, 1)):
        for _, r in rows.iterrows():
            for s_ in r["sources"]:
                srcs.setdefault(str(s_), [None, None])
                if srcs[str(s_)][who] is None:
                    srcs[str(s_)][who] = r
    both = [(k, v) for k, v in srcs.items() if v[0] is not None and v[1] is not None and k not in (la, lb)]
    both.sort(key=lambda t: (min(int(t[1][0]["order"]), int(t[1][1]["order"])), t[0]))
    if both:
        k = 8

        def side(r, lab):
            return (f"{DV.arrow('', lab, ASCII).strip()} [{r['grade']}] {DV.sign_word(r['sign'], r['kind'])}"
                    + (f" {ALERT}" if bool(r["has_alert"]) else ""))
        al = np.array([bool(v[0]["has_alert"]) or bool(v[1]["has_alert"]) for _s, v in both], dtype=bool)
        keep = cap_keep(al, k)                     # the cap rule: the k strongest, and unflagged ones beyond them
        rest = np.setdiff1d(np.arange(len(both)), keep)
        txt = "; ".join(f"{both[i][0]} ({side(both[i][1][0], la)}, {side(both[i][1][1], lb)})" for i in keep)
        more = DV.more_text(int(rest.size), int(al[rest].sum()), "genes")
        beyond = f", then any of the {k} strongest without an alert after them" if len(keep) > k else ""
        P += _wrap(_dt(f"shared upstream - genes with an arrow to both ({_n_alert(len(both), int(al.sum()), 'genes')}"
                       f"; strongest first{beyond}; {ALERT} = an alert on that arrow): {txt}"
                       + (f"; {more} (`tahoe gene {la}` and `tahoe gene {lb}` list them)" if more else "")
                       + ": two genes that follow one source can move together without acting on each other"), 2, 4)
    P += _wrap(_dt(f"[grade] and words as in `tahoe gene`: A strong, B read its alerts, C a glimpse; the sign is what "
                   f"the source's activity probably does to the target. {DV.CAVEAT}"), 2, 4)


def _pair_unmeasured(o, src, gname, found):
    """`tahoe pair SOURCE GENE` where SOURCE is not a measured gene but the source of probable-direction arrows (a drug
    target the screen does not measure, a recorded driver gene): the arrows SOURCE -> GENE with every alert in full
    (an arrow's target is always a measured gene or the cells, so none can point to SOURCE). [] when there is none to
    show (the caller then names the source's look-up)."""
    dv, _w = _direction(o)
    if dv is None:
        return []
    key = src.strip().strip(",;")
    (cb, *_more), how = found
    lb = o.genes().at[cb, "label"]
    rows = dv.downstream(key)
    rows = rows[rows["target_col"].to_numpy() == int(cb)] if len(rows) else rows
    lab = next((s_ for s_ in (rows.iloc[0]["sources"] if len(rows) else ()) if str(s_).upper() == key.upper()), key)
    P = [f"{lab} (not a measured gene of this run) x {lb} (col {cb})"]
    if how:
        P.append(f"  ({how})")
    P += _wrap(f"{lab} is no gene of this run (no symbol, label, Ensembl id or alias matches), but it is the source of "
               f"probable-direction arrows (`tahoe gene {lab}` lists them all); only the probable direction can link "
               "the two.", 2, 4)
    _title(P, "PROBABLE DIRECTION BETWEEN THEM", DV.CAVEAT_SHORT + "; direction/edges.parquet")
    _dir_list(P, DV.arrow(lab, lb, ASCII), rows, None, alerts="long")
    if not len(rows):
        P += _wrap(f"no arrow from {lab} to {lb} in this run", 2, 4)
    P += _wrap(_dt(f"{DV.arrow(lb, lab, ASCII)}: none can exist (an arrow's target is a measured gene or the cells)"),
               2, 4)
    _dir_legend(P)
    return P


def cmd_pair(o, names, top):
    if len(names) != 2:
        raise NotFound("pair needs two genes: tahoe pair GENE_A GENE_B")
    o.require("effects")
    found, unmeasured = [], []
    for nm in names:
        try:
            found.append(resolve_gene(o, nm))
        except NotFound as e:                    # a drug target the screen does not measure: say where its arrows are
            if _is_direction_source(o, nm):
                unmeasured.append((nm, e))
                found.append(None)
                continue
            raise
    if unmeasured:
        if len(unmeasured) == 1:                 # an unmeasured source and a gene: the arrows between them, in full
            P = _pair_unmeasured(o, *(names if found[1] is not None else names[::-1]),
                                 found[1] if found[1] is not None else found[0])
            if P:
                return P
        nm, e = unmeasured[0]
        raise NotFound(f"{str(e).rstrip('.')}. {nm.strip()} is not a measured gene of this run, but the source of "
                       f"probable-direction arrows: `tahoe gene {nm.strip()}` lists them")
    ((ca, *more_a), how_a), ((cb, *more_b), how_b) = found
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
                                              f"{REPRO_FDR:g}; one half = strong in one only, not the same sign in "
                                              "both")
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
                P += _wrap(f"{ALERT} seen in one random half of the compounds only: not the same sign in both "
                           "halves, no error estimate", 2, 4)
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
                if _text(r.get("alert")):              # every reason of the relations stage, in full
                    P += _wrap(f"reasons to doubt the pair (relations): {_text(r.get('alert'))}", 2, 4)
                if ok_nov and bool(r.get("novel_candidate")):
                    P += _wrap("NOVEL CANDIDATE: same sign in two random halves of the compounds, fdr <= 0.05, "
                               "|cos| >= 0.5, no shared gene group / pathway / STRING link, not one locus", 2, 4)
    ma, mb = _module_arm(o, ca), _module_arm(o, cb)
    if o.nodes() is not None and ma[0] is not None and mb[0] is not None:
        same = ma[0] == mb[0] and ma[0] > 0
        P.append(f"  nodal map: {la} module {_gene_module(o, ca)}, {lb} module {_gene_module(o, cb)}" +
                 ((" - same module, " + ("single-armed" if not ma[1] else "same arm" if ma[1] == mb[1] else
                                         "opposite arms")) if same else ""))

    # probable direction
    _dir_pair(o, P, ca, cb, la, lb)

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

    k = top if TOP_GIVEN else min(top, 10)          # 10 by default; --top N (or --top all) sets it
    for sign, word in ((1, "SAME DIRECTION"), (-1, "OPPOSITE DIRECTIONS")):
        idx = np.flatnonzero(both & (np.sign(prod) == sign))
        idx = idx[np.argsort(-np.abs(prod[idx]))]
        ok = np.array([not pair_alert(d) for d in idx], dtype=bool)
        show = _capped(len(idx), k, ok)
        _title(P, f"DRUG-DOSES THAT MOVE BOTH, {word} - every drug-dose with pooled |z| >= {PAIR_Z:g} for each",
               f"{_n_alert(len(idx), int((~ok).sum()), 'drug-doses')}; {ALERT} = an artifact flag for one or both "
               f"genes ('cell cycle ~N%': the drug-dose's cell-cycle shift would explain ~N% of the gene's change), "
               f"kept in its place; " + (f"top {k} by z({la}) x z({lb})" if k < TOP_ALL else
                                         f"by z({la}) x z({lb})"))
        if len(idx):
            P += _table(["#", "drug", "uM", f"{la} fold", "z", f"{lb} fold", "z", "alert", "caveats"],
                        [[str(j + 1), dd.at[d, "drug"], dd.at[d, "dose"], _fold(2 ** fa[d]), _z(za[d]),
                          _fold(2 ** fb[d]), _z(zb[d]), pair_alert(d), _caveats(dd.at[d, "flags"]) or "-"]
                         for j, d in ((j, idx[j]) for j in show)], "rllrrrrll", flex=(1, 8),
                        mins={1: 12, 8: 8})
            more = _more(len(idx), len(show), int((~ok).sum()) - int((~ok[show]).sum()), url=_xu(LK.pair, la, lb))
            if more:
                P += _wrap(more.strip(), 2, 6)
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
            weak = _yes(lr.get("label_weak"))
            txt = f"label: {_text(lr.get('label_display')) or _text(lr.get('label'))}"
            if src in SET_SOURCES or (src and src != "top genes" and "label_display" not in lr):
                txt += (f"  ({src}{', weak' if weak else ''}; {_int(lr.get('label_overlap'))} of "
                        f"{_int(lr.get('label_n_set'))} set genes here; q {_q(lr.get('label_q'))})")
            elif src:
                txt += f"  ({src}{', weak' if weak else ''})"
            P += _wrap(txt, 2, 4)
            if weak and _text(lr.get("label_weak_why")):
                P += _wrap(f"why weak: {_text(lr.get('label_weak_why'))}", 4, 6)
            for x in [y.strip() for y in _text(lr.get("label_alert")).split(f"; {ALERT}") if y.strip()]:
                P += _wrap(x if x.startswith(ALERT) else f"{ALERT} {x}", 2, 4)
            st = _text(lr.get("set_label"))
            if st and st != _text(lr.get("label")):
                P += _wrap(f"best gene set (not the label): {st} ({_int(lr.get('label_overlap'))} of "
                           f"{_int(lr.get('label_n_set'))} set genes here; q {_q(lr.get('label_q'))})", 2, 4)
            if _text(lr.get("label_drugs")):
                P += _wrap(f"driven by: {_text(lr.get('label_drugs'))}", 2, 4)
            if np.isfinite(_num(lr.get("median_lines_expressing"))):
                med = int(round(_num(lr.get("median_lines_expressing"))))
                P += _wrap(f"lineage: its median gene is expressed in {med} of {len(o.lines())} lines"
                           + (f"; {_text(lr.get('lineage_organs'))}" if _text(lr.get("lineage_organs")) else "")
                           + (f"; {_text(lr.get('lineage_label'))}" if _text(lr.get("lineage_label")) else ""), 2, 4)
            if _text(lr.get("chrY_genes")):
                P += _wrap(f"{ALERT} Y-chromosome genes: {_text(lr.get('chrY_genes'))}", 2, 4)
            if _text(lr.get("read_sharing_genes")):
                P += _wrap(f"{ALERT} read-sharing copies: {_text(lr.get('read_sharing_genes'))}", 2, 4)
            arms = []
            for arm, k in (("+", "plus"), ("-", "minus")):
                if _text(lr.get(f"{k}_label")):
                    arms.append(f"{arm} arm: {_text(lr.get(f'{k}_label'))} (q {_q(lr.get(f'{k}_q'))})")
            if arms:
                P += _wrap("   ".join(arms), 2, 4)
        else:
            P += _wrap(f"label: {o.module_label(m)}   " + o.missing_note("validate", "set-based label"), 2, 4)
        P += _wrap(o.arms_text(m), 2, 4)
        tag = _text(mr.get("covariate_tag"))
        if tag:
            P += _wrap(f"moves with: {re.sub(r'^moves with ', '', tag)} (graph/modules.parquet covariate_tag)", 2, 4)
        covs = [f"{w} {_f(mr.get(f'cov_{k}_r'), '{:+.2f}')}" for k, w in (
            ("umi_per_cell", "UMI per cell"), ("genes_per_cell", "genes per cell"), ("cells", "cells per well"),
            ("composition", "composition"), ("S_phase", "S-phase"), ("G2M_phase", "G2/M"))
            if np.isfinite(_num(mr.get(f"cov_{k}_r")))]
        if covs:
            P += _wrap("r of its score with: " + ", ".join(covs) + " (across drug-doses); its genes as a set: "
                       "graph/modules.gmt", 2, 4)

        mem = nd[nd["module"] == m].copy()
        mem["ap"] = mem["axis_proj"].abs() if "axis_proj" in mem else 0.0
        fo = o.flagged_only()
        n_fo = int(mem["col"].isin(fo).sum())
        arms_ = []                                  # per arm: (all members ranked, positions shown), cap rule
        for a_ in (("+", "-") if opp else ("+",)):
            part = mem[mem["arm"] == a_].sort_values("ap", ascending=False).reset_index(drop=True)
            arms_.append((part, _capped(len(part), top, ~part["col"].isin(fo).to_numpy())))
        _title(P, "TOP GENES PER ARM" if opp else "TOP GENES (single-armed module)",
               "by |projection on the module's main direction|; # = rank in the arm; name from the reference" +
               (f"; {_n_alert(len(mem), n_fo, 'members')}: {ALERT} after a gene = in the vector space only through "
                "drug-doses with an artifact flag" if n_fo else ""))
        rows = []
        for j in range(max(len(sh) for _p, sh in arms_)):
            row = []
            for part, sh in arms_:
                if j < len(sh):
                    y = part.iloc[int(sh[j])]
                    row += [str(int(sh[j]) + 1),
                            o.genes().at[int(y["col"]), "label"] + (f" {ALERT}" if int(y["col"]) in fo else ""),
                            _f(y.get("axis_proj"), "{:+.2f}"), o.ann_name(int(y["col"]))]
                else:
                    row += ["", "", "", ""]
            rows.append(row[:4] + ["|"] + row[4:] if opp else row)
        if opp:
            P += _table(["#", "+ arm", "proj", "name", "|", "#", "- arm", "proj", "name"], rows, "rlrllrlrl",
                        flex=(3, 8), mins={3: 8, 8: 8})
        else:
            P += _table(["#", "gene", "proj", "name"], rows, "rlrl", flex=(3,), mins={3: 8})
        for (part, sh), a_ in zip(arms_, ("+", "-")):
            n_al = int(part["col"].isin(fo).sum())
            n_al_shown = int(part["col"].iloc[sh].isin(fo).sum()) if len(sh) else 0
            line = f"{a_} arm: {_n_alert(len(part), n_al, 'genes')}" if opp else _n_alert(len(part), n_al, "genes")
            more = _more(len(part), len(sh), n_al - n_al_shown, "genes", url=_xu(LK.module, m))
            P.append(f"  {line}" + (f"; shown {len(sh)}" if len(sh) < len(part) else "") + (
                f"; rows beyond #{top}: the strongest without an alert, shown so that flagged members do not push "
                "them out" if len(sh) > top else ""))
            if more:
                P += _wrap(more.strip(), 2, 6)

        dd = o.drugdoses()
        art = dd["artifact"].to_numpy()
        if o.has("graph/module_pooled_z.npy"):
            pz = np.asarray(o.npy("graph/module_pooled_z.npy")[i], dtype=np.float64)
            order = np.argsort(-np.nan_to_num(pz, nan=0.0))
            k = top if TOP_GIVEN else min(top, 12)      # 12 by default; --top N (or --top all) sets it
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
            for (lst, show), word in zip(sides, ("raising it", "lowering it")):
                more = _more(len(lst), len(show), int(sum(art[d] for d in lst)) - int(sum(art[lst[x]] for x in show)),
                             f"drug-doses {word}", url=_xu(LK.module, m))
                if more:
                    P += _wrap(more.strip(), 2, 6)
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
            ol_all = [l for l in np.argsort(-np.nan_to_num(key, nan=-np.inf)) if np.isfinite(key[l])]
            ol = ol_all[:top if TOP_GIVEN else min(top, 10)]       # 10 by default; --top N (or --top all) sets it
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
            more = _more(len(ol_all), len(ol), 0, "lines", url=_xu(LK.module, m))
            if more:
                P += _wrap(more.strip(), 2, 6)
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


# ----------------------------------------------------------------------------- similar
def _resolve_drugdose(o, names):
    """(dd, how) for 'DRUG [DOSE]': the drug (resolve_drug: one drug), and the dose when the last word is one of its
    doses (else its best dose, tables/drugs.parquet best_dd; else its strongest dose by significant genes)."""
    names = [str(x) for x in names]
    dose = None
    if len(names) > 1:
        try:
            float(names[-1].lower().replace("um", "").replace("µm", ""))
            dose = names[-1].lower().replace("um", "").replace("µm", "")
            names = names[:-1]
        except ValueError:
            dose = None
    drugs = resolve_drug(o, " ".join(names))
    if len(drugs) > 1:
        raise NotFound(f"'{' '.join(names)}' names {len(drugs)} drugs: " + "; ".join(drugs) + ". Ask for one.")
    drug = drugs[0]
    dd = o.drugdoses()
    mine = dd[dd["drug"] == drug]
    if dose is not None:
        hit = mine[[(_num(x) == _num(dose)) for x in mine["dose"]]]
        if not len(hit):
            raise NotFound(f"{drug} has no dose {dose} uM (its doses: {', '.join(mine['dose'].astype(str))})")
        return int(hit["dd"].iloc[0]), ""
    if o.has("tables/drugs.parquet"):
        t = o.pq("tables/drugs.parquet")
        t = t[t["drug"] == drug]
        if len(t) and np.isfinite(_num(t["best_dd"].iloc[0])):
            return int(_num(t["best_dd"].iloc[0])), f"its best dose ({_text(t['best_dose'].iloc[0])} uM)"
    best = mine.sort_values("n_sig_genes", ascending=False)
    return int(best["dd"].iloc[0]), "its dose with the most significant genes"


def cmd_similar(o, names, top):
    """tahoe similar DRUG [DOSE] [--top N|all]: the drug-doses most similar to one drug-dose (embed/
    drug_similarity.parquet, the embed stage's 50 per drug-dose), with the cosines, shared genes, classes and
    flags. Needs the tables stage only (works on an exported results folder)."""
    o.require("tables")
    dd, how = _resolve_drugdose(o, names)
    lab = o.drugdoses().at[dd, "label"]
    P = [f"SIMILAR TO {lab} uM" + (f"   ({how})" if how else "")]
    if not o.has("embed/drug_similarity.parquet"):
        P += _wrap(_older(o, "embed", "drug-dose similarity", 5), 2, 4)
        return P
    fl = o.drugdoses().at[dd, "flags"]
    if _alert(fl):
        P += _wrap(f"{ALERT} this drug-dose: {_alert(fl)}: read its neighbours with that in mind", 2, 4)
    sim = _sim_rows_of(o, dd)                           # read once: the title and the rows
    if _sim_no_signature(sim):
        _title(P, "SIMILAR DRUG-DOSES - no ranking: it has no pooled signature", "embed/drug_similarity.parquet")
    else:
        _title(P, "MOST SIMILAR DRUG-DOSES - by the cosine of the pooled signatures (each clipped at +-10)",
               "embed/drug_similarity.parquet; shared = genes significant in both; class = the other's mechanism "
               "classes (tahoemap/data/drug_classes.json); alert = the other's artifact flags")
    _similar_rows(o, P, dd, top, sim)
    tb = [["similarity", o.p("embed", "drug_similarity.parquet"), f"dd == {dd}"]]
    _where(o, P, tb)
    return P


# ----------------------------------------------------------------------------- signature
SIG_UP, SIG_DOWN, SIG_LINES = "", "", False   # set in main(): --up, --down (comma lists or @FILE), --lines
SIG_NULL = 1000             # signature: random gene sets of the same sizes, matched by pooled-CPM decile
SIG_CLIP = 10.0             # signature: each z clipped at +-this before the means
SIG_SHOW = 25               # signature: mimics and reversers listed by default (--top N or --top all)
SIG_P = 0.01                # signature: the p the counts name
SIG_LINES_TOP = 5           # signature --lines: the hits whose lines are listed, and lines named per hit


def _gene_list(v):
    """--up / --down: 'A,B,C' or '@FILE' (names separated by commas, spaces or new lines) -> names."""
    v = str(v or "").strip()
    if not v:
        return []
    if v.startswith("@"):
        from .common import read_text_file
        v = read_text_file(os.path.expanduser(v[1:]))
    return [x for x in re.split(r"[,\s;]+", v) if x]


def signature_scores(Z, up, dn, clip=SIG_CLIP):
    """Score per drug-dose (rows of Z, drug-doses x genes; NaN = 0): mean clipped z over the up genes minus the mean
    over the down genes (a side with no genes adds 0)."""
    Zc = np.clip(np.nan_to_num(np.asarray(Z, dtype=np.float64)), -clip, clip)
    s = np.zeros(Zc.shape[0])
    if len(up):
        s += Zc[:, up].mean(axis=1)
    if len(dn):
        s -= Zc[:, dn].mean(axis=1)
    return s


def signature_null(Z, up, dn, cpm, n_null=SIG_NULL, seed=0, clip=SIG_CLIP):
    """The scores of n_null random gene sets of the same sizes, each gene drawn from the pooled-CPM decile of a query
    gene (without the query genes, no repeat within a set): drug-doses x n_null."""
    import scipy.sparse as sp
    gK = Z.shape[1]
    cpm = np.asarray(cpm, dtype=np.float64)
    ok = np.isfinite(cpm)
    edges = np.quantile(cpm[ok], np.linspace(0, 1, 11)[1:-1]) if ok.any() else np.zeros(9)
    dec = np.where(ok, np.searchsorted(edges, cpm, side="right"), -1)
    query = set(int(x) for x in up) | set(int(x) for x in dn)
    pool = {k: np.array([g for g in np.flatnonzero(dec == k) if g not in query], dtype=np.int64) for k in range(10)}
    allg = np.array([g for g in range(gK) if g not in query], dtype=np.int64)
    rng = np.random.default_rng(seed)
    rows, cols, vals = [], [], []
    for j in range(n_null):
        used = set()
        for side, w in ((up, 1.0 / max(len(up), 1)), (dn, -1.0 / max(len(dn), 1))):
            for g in side:
                pl = pool.get(int(dec[int(g)]), allg)
                pl = pl if len(pl) else allg
                for _t in range(20):                    # no repeat within a set
                    h = int(pl[rng.integers(len(pl))])
                    if h not in used:
                        break
                used.add(h)
                rows.append(h)
                cols.append(j)
                vals.append(w)
    W = sp.csr_matrix((vals, (rows, cols)), shape=(gK, n_null))
    Zc = np.clip(np.nan_to_num(np.asarray(Z, dtype=np.float64)), -clip, clip)
    return np.asarray((W.T @ Zc.T).T)


def _sig_matrix(o, cols):
    """(Z drug-doses x the gene cols needed, source text): atlas/effects/DD_z.npy when present, else the rows of
    tables/drug_effects.parquet (|z| >= 3 or q < 0.10; z = 0 elsewhere)."""
    gK = len(o.genes())
    if o.has("atlas/effects/DD_z.npy"):
        Z = np.asarray(o.eff("DD_z")[:, :gK], dtype=np.float32)
        return Z, "atlas/effects/DD_z.npy (every drug-dose x gene)"
    de = o.pq("tables/drug_effects.parquet", columns=["col", "dd", "z"])
    Z = np.zeros((len(o.drugdoses()), gK), dtype=np.float32)
    Z[de["dd"].to_numpy(dtype=np.int64), de["col"].to_numpy(dtype=np.int64)] = de["z"].to_numpy(dtype=np.float32)
    return Z, ("tables/drug_effects.parquet rows only (|z| >= 3 or q < 0.10; z = 0 elsewhere, so weaker changes "
               "count as none): the scores are rough; the full matrix atlas/effects/DD_z.npy stays on the computer "
               "that made the run")


def cmd_signature(o, names, top):
    """tahoe signature --up A,B --down C,D [--top N|all] [--lines]: which drug-doses mimic (and which reverse) a gene
    signature. Score per drug-dose = mean z over the up genes minus the mean over the down genes (each z clipped at
    +-10); null = 1,000 random gene sets of the same sizes matched by pooled-CPM decile; p_mimic = (1 + #null >= s) /
    1001, p_reverse = (1 + #null <= s) / 1001. Needs the tables stage only (an exported results folder without
    atlas/ uses the drug_effects rows)."""
    o.require("tables")
    up_n, dn_n = _gene_list(SIG_UP) + [str(x) for x in names], _gene_list(SIG_DOWN)
    if not up_n and not dn_n:
        raise NotFound("signature needs genes: tahoe signature --up A,B[,...] [--down C,D] (or --up @FILE)")
    g = o.genes()
    found, unknown = {"up": [], "down": []}, []
    for side, lst in (("up", up_n), ("down", dn_n)):
        for nm in lst:
            try:
                c = int(resolve_gene(o, nm)[0][0])
                if c not in found["up"] and c not in found["down"]:
                    found[side].append(c)
            except NotFound:
                unknown.append(nm)
    up, dn = found["up"], found["down"]
    if not up and not dn:
        raise NotFound("none of the genes is in this run: " + ", ".join(unknown))
    Z, src = _sig_matrix(o, up + dn)
    s = signature_scores(Z, up, dn)
    seed = CM.stable_seed("signature", *sorted(up), "|", *sorted(dn))
    N = signature_null(Z, up, dn, g["pooled_cpm"].to_numpy() if "pooled_cpm" in g else np.ones(len(g)),
                       seed=seed)
    n_null = N.shape[1]
    p_mim = (1 + (N >= s[:, None] - 1e-12).sum(axis=1)) / (n_null + 1)
    p_rev = (1 + (N <= s[:, None] + 1e-12).sum(axis=1)) / (n_null + 1)
    with np.errstate(invalid="ignore", divide="ignore"):
        nz = (s - N.mean(axis=1)) / N.std(axis=1)
    dd = o.drugdoses()
    lab = _class_labels(o)
    P = ["SIGNATURE - which drug-doses mimic it, and which reverse it"]
    P += _wrap(f"up ({len(up)}): " + (", ".join(g.at[c, "label"] for c in up) or "-"), 2, 4)
    P += _wrap(f"down ({len(dn)}): " + (", ".join(g.at[c, "label"] for c in dn) or "-"), 2, 4)
    if unknown:
        P += _wrap(f"{ALERT} not genes of this run (left out): " + ", ".join(unknown), 2, 4)
    P += _wrap(f"source: {src}", 2, 4)
    P += _wrap(f"score = mean z of the up genes minus mean z of the down genes (each z clipped at +-{SIG_CLIP:g}; "
               f"pooled over the lines, against the typical drug well on the same plate). null = {n_null:,} random "
               "gene sets of the same sizes, each gene from the pooled-CPM decile of a query gene "
               "(tables/genes.parquet "
               f"pooled_cpm; seed {seed}); null z = (score - null mean) / null sd for that drug-dose; p mimic = (1 + "
               f"random sets scoring as high) / {n_null + 1}, p reverse the same the other way. The smallest p "
               f"possible is 1/{n_null + 1}. Rows are ranked by p, then by score. null z '-': every random set scores "
               "the same at that drug-dose (with the drug_effects rows only: few genes are listed there).", 2, 4)
    n_show = top if TOP_GIVEN else SIG_SHOW
    res = {}                                   # embed version 5: an unexpected similarity to another class
    if o.has("embed/drugdoses.parquet"):
        e = o.pq("embed/drugdoses.parquet")
        if "resembles_note" in e:
            res = {int(d): _text(t) for d, t in zip(e["dd"], e["resembles_note"]) if _text(t)}
    # ranked by p (each drug-dose against its own null: a drug-dose that moves many genes scores high for any set),
    # then by score
    for word, order, pv in (("MIMIC IT", np.lexsort((-s, p_mim)), p_mim),
                            ("REVERSE IT", np.lexsort((s, p_rev)), p_rev)):
        n_sig = int((pv <= SIG_P).sum())
        _title(P, f"DRUG-DOSES THAT {word} - by p, then by score", f"{n_sig} of {len(s)} drug-doses with p <= "
                                                                    f"{SIG_P:g}")
        show = order[:n_show]
        rows, fls, cavs = [], [], []
        for k, d in enumerate(show):
            fl = dd.at[int(d), "flags"]
            fls.append(fl)
            if _caveats(fl):
                cavs.append(f"#{k + 1} {_caveats(fl)}")
            rows.append([str(k + 1), f"{dd.at[int(d), 'label']}", _f(s[d], "{:+.2f}"), _f(nz[d], "{:+.1f}"),
                         _q(pv[d]), lab.get(dd.at[int(d), "drug"], "") or "-", _alert_cell(fl)])
        P += _table(["#", "drug uM", "score", "null z", "p", "class", "alert"], rows, "rlrrrll", flex=(1, 5, 6),
                    mins={1: 16, 5: 14, 6: 14})
        if cavs:
            P += _wrap("caveats (no alert): " + "; ".join(cavs), 2, 4)
        notes = [f"#{k + 1} {dd.at[int(d), 'label']} uM: {res[int(d)]}" for k, d in enumerate(show) if int(d) in res]
        if notes:
            P += _wrap(f"{ALERT} resembles another class (embed/drugdoses.parquet): " + "; ".join(notes), 2, 4)
        P += _wrap(f"{len(show)} of {n_sig} with p <= {SIG_P:g} shown" if len(show) <= n_sig else
                   f"{len(show)} shown ({n_sig} of {len(s)} drug-doses have p <= {SIG_P:g})", 2, 4)
        if len(show) < len(s):
            P += _wrap("--top all for every one of the " + f"{len(s):,} drug-doses (or --top N)", 2, 4)
        _flag_legend(P, fls)
    if SIG_LINES:
        _sig_lines(o, P, up, dn, np.argsort(-s, kind="stable")[:SIG_LINES_TOP], top)
    _where(o, P, [["scores from", src.split(" ")[0], "drug-dose x gene"]])
    return P


def _sig_lines(o, P, up, dn, hits, n_lines=SIG_LINES_TOP):
    """--lines: for the top hits, the lines with the largest per-line score (tensor/DDL_z.npy: the same score inside
    each line)."""
    _title(P, "IN WHICH LINES - per-line score of the strongest mimics (tensor/DDL_z.npy)",
           "the same score inside each cell line; NaN (a line that does not measure a gene) counts as 0")
    if not o.has("tensor/DDL_z.npy"):
        P += _wrap(o.missing_note("tensor", "per-line scores"), 2, 4)
        return
    D = o.npy("tensor/DDL_z.npy")                    # genes x drug-doses x lines
    ln = o.lines()
    dd = o.drugdoses()
    k = TOP_ALL if TOP_GIVEN and n_lines >= TOP_ALL else (n_lines if TOP_GIVEN else SIG_LINES_TOP)
    for d in hits:
        X = np.asarray(D[up + dn][:, int(d), :], dtype=np.float64).T          # lines x genes
        sc = signature_scores(X, list(range(len(up))), list(range(len(up), len(up) + len(dn))))
        oo = np.argsort(-sc, kind="stable")
        kk = min(k, len(oo))
        P += _wrap(f"{dd.at[int(d), 'label']} uM: " + ", ".join(f"{ln.at[l, 'name']} {sc[l]:+.2f}" for l in oo[:kk])
                   + (f" ({kk} of {len(oo)} lines, --top N or --top all for more; weakest: "
                      + ", ".join(f"{ln.at[l, 'name']} {sc[l]:+.2f}" for l in oo[::-1][:min(3, len(oo) - kk)]) + ")"
                      if kk < len(oo) else f" (all {len(oo)} lines)"), 2, 4)


# ----------------------------------------------------------------------------- entry
COMMANDS = {"gene": cmd_gene, "drug": cmd_drug, "line": cmd_line, "pair": cmd_pair, "module": cmd_module,
            "similar": cmd_similar, "signature": cmd_signature}
USAGE = {"gene": "tahoe gene SYMBOL [SYMBOL ...]", "drug": "tahoe drug NAME", "line": "tahoe line NAME",
         "pair": "tahoe pair GENE_A GENE_B", "module": "tahoe module N",
         "similar": "tahoe similar DRUG [DOSE] [--top N|all]",
         "signature": "tahoe signature --up A,B[,...] [--down C,D] [--top N|all] [--lines] (or --up @FILE)"}


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
    """text as the output stream can show it (common.printable): on a console or a redirect whose encoding lacks
    ALERT or the arrow (a Windows code page) they become '!' and '->', and any other character it cannot show a
    '?'."""
    return printable(text, stream)


def _needs_ascii(stream=None):
    """True when the stream (default stdout) cannot show the arrow or ALERT: the direction texts are then built in
    ASCII before they are laid out (ASCII)."""
    stream = sys.stdout if stream is None else stream
    sign = ARROW + ALERT
    return encodable(sign, getattr(stream, "encoding", None) or "utf-8") != sign


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
    """The look-up commands of cli.py: a.command in gene | drug | line | pair | module | similar | signature, a.names,
    a.top, a.out (signature: a.up, a.down, a.lines)."""
    global WIDTH, ASCII, TOP_GIVEN
    WIDTH = max(80, min(120, shutil.get_terminal_size((120, 24)).columns)) - 2
    ASCII = _needs_ascii()
    warnings.filterwarnings("ignore", category=RuntimeWarning)
    global SITE, LOCAL_X
    t = parse_top(getattr(a, "top", None))
    TOP_GIVEN = t is not None
    top = TOP_ALL if t == 0 else (t if TOP_GIVEN else 15)
    SITE = LK.site_url(getattr(a, "site_url", None))
    LOCAL_X = os.path.join(a.out, "explorer", "web", "index.html")
    names = [n for n in (getattr(a, "names", None) or []) if str(n).strip()]
    global SIG_UP, SIG_DOWN, SIG_LINES
    SIG_UP, SIG_DOWN = getattr(a, "up", None) or "", getattr(a, "down", None) or ""
    SIG_LINES = bool(getattr(a, "lines", False))
    if not names and not (a.command == "signature" and (SIG_UP or SIG_DOWN)):
        _emit([f"usage: {USAGE[a.command]}   (options: --top N rows per table, or --top all; --out OUTPUT "
               "folder)"])
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
