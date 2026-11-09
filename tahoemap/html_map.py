"""html_map - the interactive gene map: one self-contained HTML file, OUT/map/gene_map.html.

No network, no external script or style: vanilla JavaScript on a <canvas>, with every number the page shows computed
here and embedded as one compact JSON block. Open the file in any current browser (also from a USB stick / offline).

What the page shows
    seven tabs (docs/DESIGN-review-and-physics.md, part 1); the search box and the side panel belong to all of them,
    and a gene selected on one tab is selected on every tab:
      Nodal map / Signed vector map   the two t-SNE layouts of the graph stage (below), and their spread layouts
                                      (graph xm, ym / xsm, ysm: the modules moved apart as blocks); one canvas,
                                      switching tabs animates every gene from one layout to the other; the Spread
                                      slider (0 = t-SNE, 1 = spread) mixes the two linearly, Spread ⇄ animates 0 <-> 1
      k-D tour                        the unit gene vectors of the vector space (embed stage, k dimensions: 64 at full
                                      scale) through a moving 2D projection: a grand tour (geodesic interpolation
                                      between random 2D planes, from the principal angles of the 2 x 2 matrix Fa' Fz;
                                      fixed seeds), or two axes of the space chosen by the user (axis mode: the window
                                      turns there along the geodesic, then within the plane, so that x = axis i and
                                      y = axis j exactly); play / pause (space), speed, new direction, pan / zoom, a
                                      compass of the axes, colour by module or arm, the same selection, hover and
                                      side panel; one projection (n x k multiply-adds) and one pixel-buffer draw per
                                      frame (about 3 + 3 ms at 15,000 genes x 64)
      Physics: neighbourhood          a live force simulation of the selected gene, its partners and (depth 2-4)
                                      their partners, one depth at a time, strongest first (the product of |cos|
                                      along the way), at most Max genes (default 300, up to 2,000) (springs = the
                                      embedded top-partner lists, `rel`); Direction (probable direction, below):
                                      off / arrows (between the genes shown) / + its genes (the default: also the
                                      selected gene's up- and downstream genes of its side-panel lists, held by a
                                      link that is no relation and not drawn, so that a gene not on the map, such as
                                      a recorded mutation's gene, is shown with its arrows)
      Physics: module                 a live force simulation of one module (springs = graph/edges.parquet among its
                                      genes; optional dimmed ring of 1-hop outside genes)
      Physics: all genes              every map gene, started from the nodal-map positions (springs = every edge of
                                      graph/edges.parquet; edges drawn for the selected gene only)
      How to read this                the help text (also: how the modules are made, the spread, the tour, alerts)
    The physics engine (vanilla JS, typed arrays, one engine for the three tabs): springs on edges (force ∝ |cos| x
    (distance - rest length) / min(degree of the two genes), as d3-force's link force, so hubs stay stable; rest
    length s0 x (1.6 - |cos|): shorter for stronger edges), 1/d repulsion between every pair through a Barnes-Hut
    quadtree (theta 0.8; genes visited in tree order for cache locality), a weak pull to the centre, velocity damping
    and a cooling alpha (d3-force's integration). The sign switch makes red (cos < 0) edges either springs ("opposite
    genes attract": the nodal view) or pushers ("opposite genes repel": push up to 6 rest lengths, no pull beyond: the
    signed view, the - arm parts from the + arm). Drag (a gene's partners follow), double-click to pin (also a slow
    one: a click selects only after 400 ms without a second click, and the double-click pins the gene clicked first
    without re-centring), click to select, pan / zoom, pause (space), re-heat, reset, fit; sliders for repulsion,
    springs and minimum |cos|; an evidence filter (both halves / also one half / every relation; the neighbourhood's
    info box counts the selected gene's listed partners it leaves out, and a spring's tooltip shows an alert when it
    is not replicated); colour by module or arm; labels for the selected gene, its partners, pinned genes and (zoomed
    in) everyone. Each tab runs at most 120 steps a second (so a small simulation plays a re-heat or the sign switch
    over ~2 s instead of settling in a few frames) and as many per frame as fit in a ~13 ms budget (one step every
    other frame when one step takes > 45 ms: the all-genes tab at 15,000 genes).
    window.TAHOE_MAP exposes, for tests (tests/checks.py drives the page with Playwright when it is installed):
    select(i), search(q), data, tab(name), bench(n), state(), sim(tab), screen(tab, i), stats(tab), benchTick(tab, n);
    spread(v) (set the Spread slider; no argument: read it), hasSpread(), positions() (the map's drawn positions),
    mapScreen(i) (where gene i is drawn on the map canvas);
    tour(), tourPositions(), tourVector(i), tourAxes(i, j) (0-based), tourMode('tour' | 'axes'), tourPlay(bool),
    tourBench(n) (mean ms of one tour frame: projection and drawing), tourScreen(i); panel() (the side panel's text);
    direction(i) (gene i's up / dn / ce lists: every row as direction_view.edge_line, *_shown = the positions the
    capped list shows, *_more = [rows left out, of them with an alert], *_counts = counts_text), dirArrows(tab) (the
    arrows a physics tab draws: mode, genes added, ids, [{s, t, k, grade, sign, n, line}]), mapArrows() (the
    selected gene's arrows on the maps).
    The maps: the NODAL map (graph x, y: genes that respond to the same drugs sit together whether they go up together
    or in opposite directions; the two arms of a pathway form one island) and the SIGNED vector map (graph xs, ys:
    genes that move in opposite directions are pushed apart; a two-armed module is labelled once per arm there). Pan
    (drag), zoom (wheel / pinch), hover (symbol, module and arm, name), colour by module (a fixed palette of 20 colours
    cycled, unassigned grey) or by arm (+ / -), a module legend (labels from validation/module_labels.csv, else the
    module's top genes; click = highlight), a search box with autocomplete (symbol, alias, previous symbol, name), and
    a side panel for the selected gene: name and function (reference stage), module and arm, its top partners (green
    line = moves with it, red = moves opposite; cos, evidence, fdr, locus / readthrough / known / novel flags), its top
    drug-doses up and down (tables/drug_effects.parquet: fold, z, lines moving) and the cell lines where it responds
    most (tables/line_effects.parquet). Genes that are not in the vector space (too few responsive contexts, no
    evidence of a response beyond that count, noise RNA) are searchable too: the panel then gives their drug-doses and
    lines, and why they are not on the map, as the embed stage's rule with its counts.
    The URL hash selects a gene (gene_map.html#HMOX1), so other documents can link to a gene.
    Probable direction (direction stage, OUT/direction; read, ordered, collapsed and worded by direction_view, so the
    page says what the vault notes and the look-ups say): the side panel lists the selected gene's Upstream rows (it is
    the target: what probably acts on it), Downstream rows (it is a source, the target a gene) and Cells rows (it is a
    source, the target the cells under a drug-dose), each in direction_view.ORDER and capped at N_DIR by the cap rule
    (direction_view.cap) with its counts (counts_text, more_text) and a 'show all'; a row reads 'SOURCE → TARGET', its
    grade badge (A / B / C, the grade's words as its tooltip), the sign word, the kind and q, the sentence of
    sign_text, the short alerts (⚠; the full reasons as tooltip) and, on click, the evidence (kind_text, the reading,
    every alert); a gene's name selects it. Arrows: on the neighbourhood tab between the genes shown (one per ordered
    pair, its strongest row; at most 3,000, the info box counts any more), on the two maps the selected gene's rows of
    its lists (the 'Direction arrows' box); line style by grade (A thick, B thin, C dashed), head by sign (raises: a
    filled head, lowers: a bar, not inferred: an open circle), in one violet. An output without the stage: the panel,
    the help and the disabled toggles say so.

Alerts, not removal. An item with a reason for doubt stays in its ranked place with a visible alert, '⚠' and the
reason in plain words, and every list says how many items there are in all and how many carry an alert:
    drug-doses       every row of tables/drug_effects.parquet, flagged or not; ⚠ + the gene-level flags string when
                     the row holds an artifact flag (not 'clean': atlas_core.has_artifact); a cell-cycle shift reads
                     'cell-cycle shift, explains ~N% of this change' (N = round(100 x cc_share) when the tables stage
                     measured it), and a shift the tables stage cleared ('cell-cycle shift (explains ~N% here)': no
                     artifact flag) is noted in grey without ⚠; other flags are in the row's tooltip
    cell lines       counts over all drug-doses (how many carry an artifact flag in brackets) and the strongest
                     drug-dose, flagged or not (line_effects *_all columns; an older tables stage: clean only, said so)
    partners         ⚠ for a relation seen in one random half only, not reproduced, between two neighbouring genes
                     (same locus, read-through risk), or with a partner in the space only through flagged drug-doses
                     (relations' 'alert' rule without the selected gene's own reason: when the selected gene is in
                     the space only through flagged drug-doses, the panel says so once and the cap and the counts
                     look at the partners' reasons)
    module drugs     ⚠ + the drug-dose's own flags (tables/drugdoses.parquet) for an artifact flag
    direction rows   ⚠ + direction_view.alert_short (the stage's reasons as short labels; the full reasons in the
                     tooltip and in the row's evidence), cut by direction_view's cap rule with its counts
    genes            ⚠ not on the map (not in the vector space; also in the search list); ⚠ in the vector space only
                     through flagged drug-doses (embed/genes.parquet evidence_flagged_only, when the column is there)
A list capped at N (partners 15, drug-doses 8 per direction, lines 5, module drug-doses 10 per direction, direction
rows 8 per list) holds the N strongest overall AND any of the N strongest without an alert that would otherwise fall
beyond them, all in one ranking (cap_keep), so flagged items never push unflagged ones out of view. The physics
springs use the Evidence filter (computing, not showing): the info box says how many listed partners it leaves out.

What the page says is the stages' own rule, never more: the per-line counts and 'strongest' use the per-line |z| cut
the tables stage calibrated (tables/info.json; '-' below it); 'both' halves = same sign with fdr <= 0.10 in two random
halves of the compounds, 'one' = strong in one random half only (not replicated); 'novel?' only when
relations/info.json says novelty could be assessed (else which sources were missing); a module's arms are called
opposite only when graph/modules.parquet says so (arms_opposite), and its drug lists are the pooled module z
(graph/module_pooled_z.npy) with |z| >= 1; the help's account of how modules are made uses graph/info.json's numbers.

Inputs (read only): graph/nodes.parquet, graph/modules.parquet, graph/module_pooled_z.npy, graph/edges.parquet,
graph/info.json, relations/gene_relations.parquet, relations/info.json,
tables/{genes,drug_effects,line_effects,drugdoses,lines}.parquet, tables/info.json, embed/genes.parquet,
embed/info.json, embed/gene_unit.npy, embed/components.parquet; optional: reference/annotations.parquet,
validation/module_labels.csv, direction/ (edges.parquet, groups.parquet, controls.json, info.json; and
atlas/effects/drugdose.csv for the cells rows' drug-doses: direction_view.load). Without graph/edges.parquet (an
older graph stage) the module and all-genes tabs fall back to the top-partner lists; without the spread columns of
graph/nodes.parquet the Spread slider is off; without embed/gene_unit.npy the tour tab says so; without direction/
the panel, the help and the (disabled) arrow toggles say that the stage has not run.

The embedded JSON (<script id="tm-data" type="application/json">; "<" is written as \\u003c). Entries 0..n-1 are
the genes on the map in graph/nodes.parquet order, entries n..n_all-1 the genes that are not on the map (by col).
Scaled integers: cos x100, fdr x100 (-1 = none), lfc x100 (log2), z x10.
    v, title, made, n, scale       version, title, date, number of map genes, the integer scales
    col, sym                       per entry: gene col (atlas/effects/genes.csv row), label (unique symbol)
    x, y, xs, ys                   per map gene: nodal and signed layout, rounded to 2 decimals
    xm, ym, xsm, ysm               per map gene: the spread layouts (graph/nodes.parquet; left out when absent)
    mod, arm                       per map gene: module (0 = unassigned); arm string, one char each: + - or .
    name, fn, alias                per entry (empty lists without the reference stage): HGNC name, a function
                                   snippet (UniProt function, else NCBI summary), aliases and previous symbols "|"
    cpm, nup, nupa, ndn, ndna, nlx per entry: pooled CPM; drug-doses raising it significantly (tables/genes n_dd_up)
                                   and how many of them carry an artifact flag (n_dd_up - n_dd_up_clean); the same
                                   lowering it; lines expressing it (tables/genes)
    why                            per off-map entry: -1 noise-class RNA, -2 included but not laid out, else the
                                   number of responsive contexts (embed needs `min_responsive`)
    efo                            entries in the vector space only through flagged drug-doses (embed/genes.parquet
                                   evidence_flagged_only; [] without that column)
    rel                            per map gene: flat [partner entry, cos, fdr, flags] x top partners (by rank; the
                                   first n_partners, plus any of the first n_partners without an alert beyond them:
                                   cap_keep; an alert = not both halves, same locus, read-through risk, or the
                                   partner in the space only through flagged drug-doses: relations' 'alert'
                                   reasons without the gene's own).
                                   flags = evidence (0 not reproduced, 1 one half, 2 both halves) + 4 locus +
                                   8 readthrough_risk + 16 shared_gene_group + 32 known + 64 novel_candidate +
                                   256 * round(STRING score / 10) + 32768 * (index into pw + 1)
    reln                           per map gene: flat [partners in relations, how many of them with an alert (the
                                   partners' reasons, as in rel)]
    pw                             shared pathway names (rel flags point here)
    up, dn                         per entry: flat [dd, lfc, z, lines moving, flag code] x top drug-doses (every row
                                   of tables/drug_effects, strongest first, cut by cap_keep at n_drugs); in dn lfc
                                   and z are stored NEGATED (positive, saves the signs)
    dct                            per entry: flat [rows up, of them with an alert, rows down, with an alert]
    ln                             per entry: flat [line, n dd up, of them flagged, n dd down, of them flagged, dd,
                                   lfc, z, flag code, clean dd, clean lfc, clean z] x top lines (LN_WIDTH = lnw
                                   ints; measured lines only; the lines with the most responding drug-doses, plus
                                   any of the n_lines with the most clean ones beyond them; n dd up / down at the
                                   calibrated per-line cut, over all drug-doses when ln_all, else over the clean
                                   ones; dd, lfc, z = the line's strongest drug-dose, up or down, flagged or not
                                   when ln_all; dd -1 = none at |z| >= line_z; clean dd, lfc, z = when that
                                   strongest carries an alert, the line's strongest drug-dose without one at
                                   |z| >= line_z, by the same up-or-down rule, else -1, 0, 0)
    ln_all                         whether tables/line_effects has the *_all columns (else counts are clean only)
    fl                             the flag texts the rows point to (flag code c > 0: fl[c - 1] = [text, kind]; kind
                                   1 = alert (an artifact flag: ⚠ + text), 2 = a cell-cycle shift that is no
                                   artifact flag here (a grey note), 0 = other flags (tooltip); FlagTable)
    dd, ddf, lines, organ          labels: drug-dose by dd row ("Drug dose uM") and its own flags (flag code),
                                   cell line by line index, organ
    mods                           per module: id, n, np, nm, label, genes (top-gene label), plus, minus, opp
                                   (arms_opposite), cb (mean cos between the sides), up, dn (flat [dd, pooled module
                                   z x 10] with z >= 1 / <= -1, cut by cap_keep at n_mod_drugs), nup, ndn ([how many
                                   reach |z| >= 1, of them flagged]), lines (graph/modules); an older graph stage
                                   without module_pooled_z.npy: up_txt, dn_txt (its lists as text) instead
    palette, ref, labels_from, min_responsive
    embed                          the embed stage's inclusion rule and counts (embed/info.json)
    line_z, line_z_cal, line_chance  the per-line |z| cut, whether it is calibrated, the expected chance calls per
                                   gene x line
    novel_ok, novel_blocked        relations/info.json novel_assessed, novel_blocked_by
    mod_z                          the module card's |z| floor
    edges                          graph/edges.parquet between two map genes, one row per pair (a < b), sorted:
                                   {"m": rows, "bytes": 2 or 4 (index width), "a", "b": base64 of little-endian
                                   unsigned entry indices, "cos": base64 of int8 round(cos x 100), "ev": base64 of
                                   uint8 evidence of the pair in relations (0 not reproduced, 1 one half, 2 both
                                   halves)}: ~6 bytes per edge before base64 (~1.4 MB at 177,000 edges)
    k_edges                        graph/info.json k_edges (partners per gene in the kNN graph), or null
    grule                          graph/info.json's module rule (k_edges, min_edge, one_half_edge, max_module,
                                   loose_cos, split_depth, min_module, arms_opposite_cos) and spread statistics
    n_partners, n_drugs, n_lines, n_mod_drugs  the list caps
    halves                         embed/info.json halves (false: no half spaces, so evidence was not tested)
    tour                           the vector-space tour (_tour_block): {"k", "n", "sc": per-axis scale, "q": base64
                                   of int8 round(127 x v / sc) of the map genes' unit vectors (n x k, row-major; ~1.3
                                   MB at 15,000 x 64), "ax": per-axis top genes (+ / −, embed/components.parquet),
                                   "var": per-axis % of the space}, or {} without embed/gene_unit.npy
    dir                            the probable direction (DirBlock.encode): {"ok": false, "why"} without the
                                   stage; else direction_view's display rows (collapsed, in ORDER) that touch a gene
                                   of the page, as "r": flat ints, w = DIR_FIELDS per row: [kind + 16 x grade + 64 x
                                   (sign + 1) + 256 x has_alert (kind, grade: indices into "kinds", "grades"),
                                   source set (index into "ss"), target name (index into "nm"), target entry (gene
                                   targets; -1 = not a gene of the page) or drug-dose row (cells targets: target_dd),
                                   sign_text, kind_text, q_text, alert_short, alert_long, reading (indices into "tx";
                                   -1 = left out to keep the page small)]; "ss": [source text (nm), then per source
                                   name (nm), entry (-1 = not a gene of the page)]; "nm", "tx": the strings, the most
                                   frequent first (tx[0] = ""); a text is a template: \u0001 = the row's source text,
                                   \u0002 = its target name (for a cells target the drug-dose after 'cells under '),
                                   put back as T then S (_templ / _fill: exact); "cmore": flat [entry, rows left out,
                                   of them with an alert, A, B, C] when the cells rows beyond the cap were left out;
                                   "cap" N_DIR; the words of direction_view: kinds, kshort, kwords, sens (sensitivity
                                   kinds), grades, gwords, gshort, signw (for -1, 0, +1), caveat, caveat_short,
                                   caveat_lines, order; counts (direction_view.counts), n_rows_stage, n_edges_stage,
                                   n_rows, n_edges (on the page), n_rows_out (rows that touch no gene of the page: a
                                   source that is no measured gene and a cells target; rows_out_sources, their first
                                   sources), short (what was shortened, in words), lines (the stage's lines). About
                                   40 bytes a row without its texts; at full scale (an estimate with ~115,000 edges,
                                   ~94,000 display rows) 13.6 MB with every text, 7.8 MB without the grade C rows'
                                   readings, 6.5 MB without any reading (run: the shortening steps, in order)
    lit, lit_v                     only when OUT/review holds literature reviews (tahoemap/review): flat [entry a,
                                   entry b, kind, citations] x the connection verdicts of gene a's review on gene b
                                   (review/connections.parquet, of each gene's latest review, one per partner by
                                   vault.pick_verdict: the vault's rules, vault.review_connections) where a and b are
                                   partners in `rel` (one way or the other); lit_v[kind]
                                   = [label, explanation, shown verdict, check_status] (vault.verdict_label: e.g.
                                   "established (supported)", "indirect (ids not checked)", "unverified" when the
                                   citation check found it not supported, every citation was removed as not found,
                                   or every paper it cites is retracted; " (cites a retracted paper)" follows the
                                   label when one is, and the explanation names it).
                                   The side panel's partner list shows them as a small "lit:" badge (a's verdict on b,
                                   else b's on a). The stamp records vault.review_fingerprint, so a review run makes
                                   the map out of date.
"""

import base64
import json
from collections import Counter
import os
import re
import time
import warnings

import numpy as np
import pandas as pd

from . import atlas_core as A
from . import direction_view as DV
from . import vault as V
from .common import ALERT, cap_keep as cap_rule, folder, log, marked_names, replace_file, stamp_stage

VERSION = 6                    # 3: tabs, the physics simulations, graph/edges.parquet embedded; 4: a slow
                               # double-click pins, at most 120 steps a second, literature badges with their check;
                               # 5: alerts instead of removal, the Spread slider, the k-D tour, neighbourhood depth 4;
                               # 6: probable direction (direction stage): side-panel lists and arrows
N_PARTNERS = 15
N_DRUGS = 8
N_LINES = 5
LN_WIDTH = 12                  # ints per row of the `ln` lists (module docstring)
N_MOD_DRUGS = 10               # module card: drug-doses per direction, with |pooled module z| >= MOD_Z
MOD_Z = 1.0
LINE_Z_FALLBACK = 4.0          # per-line |z| cut when tables/info.json has none (older tables stage: uncalibrated)
FN_CHARS = 110
MAX_BYTES = 20_000_000         # above this the function snippets are shortened, then the line lists (a 20 MB page
                               # opens in about a second; version 5 adds ~1.3 MB of tour vectors at full scale)
N_DIR = 8                      # side panel: probable-direction rows per list (upstream, downstream, cells), cap rule
DIR_FIELDS = 10                # ints per row of the `dir` block's r (module docstring)
EVIDENCE = {"not reproduced": 0, "one half": 1, "both halves": 2}
# 20 colours for modules (cycled: module m gets PALETTE[(m - 1) % 20]); the first 8 are a CVD-checked categorical
# set on the light surface, the next 12 darker / other hues. Modules are numbered by size, so the big ones get these.
PALETTE = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4", "#008300", "#6250d6", "#e34948",
           "#104281", "#9a6324", "#00695c", "#7d8f00", "#a3307a", "#18a7c9", "#8b1a1a", "#9c7ce8",
           "#7cb518", "#37474f", "#5e2b97", "#bf8040"]


# ----------------------------------------------------------------------------- reading
def _read(path, columns, filters=None):
    """The listed columns that exist in the file (older runs may lack some), optionally row-filtered."""
    import pyarrow.parquet as pq
    have = set(pq.read_schema(path).names)
    cols = [c for c in columns if c in have]
    if filters:
        filters = [f for f in filters if f[0] in have] or None
    return pd.read_parquet(path, columns=cols, filters=filters)


def _bool(df, c):
    if c not in df:
        return np.zeros(len(df), dtype=bool)
    return df[c].fillna(False).astype(bool).to_numpy()


def _num(df, c, fill=np.nan):
    if c not in df:
        return np.full(len(df), fill, dtype=np.float64)
    return pd.to_numeric(df[c], errors="coerce").to_numpy(dtype=np.float64)


def _scaled(x, scale, fill=0):
    """Round x * scale to int; NaN / inf -> fill."""
    x = np.asarray(x, dtype=np.float64) * scale
    ok = np.isfinite(x)
    return np.where(ok, np.rint(np.where(ok, x, 0.0)), fill).astype(np.int64)


def _str(v):
    if v is None:
        return ""
    if isinstance(v, float) and not np.isfinite(v):
        return ""
    s = str(v).strip()
    return "" if s.lower() in ("nan", "none", "<na>") else s


# ----------------------------------------------------------------------------- per-entry lists
def _first_k(ent, k):
    """ent sorted ascending: mask of the first k rows of every run of equal values."""
    ent = np.asarray(ent)
    if ent.size == 0:
        return np.zeros(0, dtype=bool)
    start = np.searchsorted(ent, ent, "left")
    return (np.arange(ent.size) - start) < k


def _lists(ent, mat, n):
    """Rows sorted by entry (ent ascending, rows in display order) -> one flat int list per entry 0..n-1."""
    if len(ent) == 0:
        return [[] for _ in range(n)]
    m = mat.shape[1]
    flat = np.asarray(mat, dtype=np.int64).ravel().tolist()
    lo = np.searchsorted(ent, np.arange(n), "left").tolist()
    hi = np.searchsorted(ent, np.arange(n), "right").tolist()
    return [flat[a * m:b * m] for a, b in zip(lo, hi)]


_TAG = re.compile(r"^\s*\[[^\]]{1,80}\]:\s*")
_REFS = re.compile(r"\s*\((?:PubMed|ECO|By similarity)[^)]*\)")


def _snippet(s, n):
    """The first sentence(s) of a function text, cut at a word boundary to <= n characters."""
    s = _str(s)
    if not s:
        return ""
    s = _TAG.sub("", s)
    s = _REFS.sub("", s)
    s = re.sub(r"\s+", " ", s).strip()
    if len(s) <= n:
        return s
    end = s.rfind(". ", 0, n)
    if end >= n * 0.5:
        return s[:end + 1]
    cut = s[:n].rsplit(" ", 1)[0].rstrip(",;:(")
    return cut + "…"


# ----------------------------------------------------------------------------- module labels
_LABEL_COLS = ("label", "module_label", "name", "title", "top_set", "best_set", "set", "term", "description")


def _validation_labels(out):
    """{module: label} from validation/module_labels.csv (whatever its label column is called), else {}."""
    p = os.path.join(out, "validation", "module_labels.csv")
    if not os.path.exists(p):
        return {}
    try:
        df = pd.read_csv(p)
    except (OSError, ValueError, pd.errors.ParserError) as e:
        log(f"  module_labels.csv unreadable ({e}); labelling modules by their top genes")
        return {}
    low = {c.lower(): c for c in df.columns}
    mcol = low.get("module") or next((c for c in df.columns if "module" in c.lower()
                                      and pd.api.types.is_numeric_dtype(df[c])), None)
    lcol = next((low[c] for c in _LABEL_COLS if c in low and low[c] != mcol), None)
    if lcol is None:
        lcol = next((c for c in df.columns if c != mcol and df[c].dtype == object), None)
    if mcol is None or lcol is None:
        log("  module_labels.csv has no module / label column; labelling modules by their top genes")
        return {}
    out_ = {}
    for m, lab in zip(pd.to_numeric(df[mcol], errors="coerce"), df[lcol]):
        lab = _str(lab)
        if np.isfinite(m) and lab and int(m) not in out_:
            out_[int(m)] = lab[:90]
    return out_


def _top_genes_label(plus, minus, k_plus=3, k_minus=2):
    """'A, B, C | − D, E' from a module's top_plus / top_minus, each cut with the cap rule (a member with an alert,
    'SYMBOL ⚠', keeps its place, and the strongest without one are not pushed out)."""
    p = marked_names(_str(plus), k_plus)
    m = marked_names(_str(minus), k_minus)
    s = ", ".join(p)
    if m:
        s += " | − " + ", ".join(m)
    return s


def _arm_text(txt, fo_sym):
    """A module arm's top genes (graph modules.parquet top_plus / top_minus) as shown: a member in the vector space
    only through flagged drug-doses reads 'SYMBOL ⚠' (the graph stage writes the marks; an older graph stage: marked
    here from embed evidence_flagged_only, fo_sym = those symbols)."""
    names = marked_names(_str(txt))
    if fo_sym and not any(x.endswith(ALERT) for x in names):
        names = [x + (f" {ALERT}" if x in fo_sym else "") for x in names]
    return ", ".join(names)


def _info(path):
    """A stage's info.json as a dict ({} when missing or unreadable)."""
    try:
        with open(path, encoding="utf-8") as fh:
            return json.load(fh) or {}
    except (OSError, ValueError):
        return {}


# ----------------------------------------------------------------------------- alerts
_CC_CLEARED = re.compile(r"cell-cycle shift \(explains ~(\d+)% here\)")


def flag_text(flags, cc_share=np.nan):
    """A flags string in plain words for the page: 'cell-cycle shift' gains the share of this change the shift would
    explain when the tables stage measured it (cc_share; 'cell-cycle shift, explains ~87% of this change'), and the
    tables stage's 'cell-cycle shift (explains ~N% here)' reads 'cell-cycle shift, explains ~N% of this change'."""
    out = []
    for p in [p for p in _str(flags).split("; ") if p]:
        m = _CC_CLEARED.fullmatch(p)
        if m:
            p = f"cell-cycle shift, explains ~{m.group(1)}% of this change"
        elif p == "cell-cycle shift" and cc_share is not None and np.isfinite(cc_share):
            p = f"cell-cycle shift, explains ~{int(round(100 * float(cc_share)))}% of this change"
        out.append(p)
    return "; ".join(out)


class FlagTable:
    """The flag texts the page shows, numbered once (data block `fl`): code 0 = no flags, else 1 + index into rows;
    rows[i] = [text, kind], kind 1 = an alert (the row holds an artifact flag: '⚠' + the text, visible), 2 = a
    cell-cycle shift that is not the explanation (visible, muted), 0 = other flags (in the row's tooltip)."""

    def __init__(self):
        self.rows, self._ix = [], {}

    def code(self, flags, alert, cc_share=np.nan):
        text = flag_text(flags, cc_share)
        if not text and not alert:
            return 0
        text = text or "artifact flag"
        kind = 1 if alert else (2 if "cell-cycle shift" in text else 0)
        key = (text, kind)
        if key not in self._ix:
            self._ix[key] = len(self.rows)
            self.rows.append([text, kind])
        return self._ix[key] + 1

    def codes(self, flags, alert, cc_share=None):
        """Vectorised code(): one call per distinct (flags, alert, cc_share) combination."""
        flags = pd.Series(flags, dtype=object).map(_str).to_numpy()
        alert = np.asarray(alert, dtype=bool)
        cc = np.full(len(flags), np.nan) if cc_share is None else np.asarray(cc_share, dtype=np.float64)
        ccp = np.where(np.isfinite(cc), np.rint(100 * np.nan_to_num(cc)), -1).astype(np.int64)
        # the key's separator is \x1f, not \x00: pandas hashes an all-string column as C strings, which end at the
        # first \x00, so every key with the same flags would become one (and share the first row's percentage)
        codes, uniq = pd.factorize(pd.Series([f"{f}\x1f{int(a)}\x1f{c}" for f, a, c in zip(flags, alert, ccp)],
                                             dtype=object))
        val = np.zeros(len(uniq), dtype=np.int64)
        for u, k in enumerate(uniq):
            f, a, c = k.split("\x1f")
            val[u] = self.code(f, a == "1", int(c) / 100 if int(c) >= 0 else np.nan)
        return val[codes] if len(codes) else np.zeros(0, dtype=np.int64)


def cap_keep(ent, ok, k):
    """Rows sorted by entry (ent ascending, strongest first within an entry): the mask of the rows the page keeps,
    the first k of each entry plus any of its first k rows without an alert (ok) that fall beyond them. So a flagged
    row keeps its ranked place and never pushes an unflagged one out of view."""
    ent = np.asarray(ent)
    ok = np.asarray(ok, dtype=bool)
    if ent.size == 0:
        return np.zeros(0, dtype=bool)
    start = np.searchsorted(ent, ent, "left")
    rank = np.arange(ent.size) - start
    c = np.cumsum(ok)
    before = np.where(start > 0, c[np.maximum(start - 1, 0)], 0)
    rank_ok = c - before - ok                                  # unflagged rows before this one in its entry
    return (rank < k) | (ok & (rank_ok < k))


def _module_drugs(z, dalert, sign, k=N_MOD_DRUGS, zmin=MOD_Z):
    """The module card's drug-doses one way: those with sign * pooled module z >= zmin, strongest first, capped at k
    by cap_keep (flagged ones keep their place, unflagged ones of the first k beyond them are added): flat
    [drug-dose, z x 10] rows, and [how many reach zmin, how many of them carry an artifact flag]."""
    v = np.nan_to_num(sign * np.asarray(z, dtype=np.float64), nan=-np.inf)
    o = np.array([i for i in np.argsort(-v, kind="stable") if v[i] >= zmin], dtype=np.int64)
    al = np.array([i < len(dalert) and bool(dalert[i]) for i in o], dtype=bool)
    keep = cap_keep(np.zeros(len(o), dtype=np.int64), ~al, k) if len(o) else np.zeros(0, dtype=bool)
    rows = []
    for i in o[keep]:
        rows += [int(i), int(_scaled([z[i]], 10)[0])]
    return rows, [int(len(o)), int(al.sum())]


# ----------------------------------------------------------------------------- the vector-space tour
def _tour_block(out, cols, k_axes_genes=3):
    """The unit gene vectors of the map genes (embed/gene_unit.npy rows `cols`, map order), quantised per axis:
    {"k", "n", "sc": per-axis scale, "q": base64 of int8 round(127 x v / sc) row-major (n x k), "ax": per-axis
    label from embed/components.parquet, "var": per-axis % of the space's variance}; {} without the embed vectors."""
    ed = os.path.join(out, "embed")
    p = os.path.join(ed, "gene_unit.npy")
    if not os.path.exists(p) or len(cols) == 0:
        log("  no embed/gene_unit.npy: the vector-space tour is left out")
        return {}
    U = np.load(p, mmap_mode="r")
    cols = np.asarray(cols, dtype=np.int64)
    if cols.max() >= U.shape[0]:
        log("  embed/gene_unit.npy does not cover the map genes: the vector-space tour is left out")
        return {}
    V = np.nan_to_num(np.asarray(U[cols], dtype=np.float64), nan=0.0)
    V /= np.maximum(np.sqrt((V ** 2).sum(axis=1)), 1e-12)[:, None]
    k = V.shape[1]
    sc = np.maximum(np.abs(V).max(axis=0), 1e-9)
    q = np.clip(np.rint(V / sc * 127), -127, 127).astype(np.int8)
    ax, var = [""] * k, [None] * k
    cp = os.path.join(ed, "components.parquet")
    if os.path.exists(cp):
        comp = _read(cp, ["component", "variance_pct_of_space", "top_pos_genes", "top_neg_genes"])
        for r in comp.to_dict("records"):
            j = int(r.get("component", 0)) - 1
            if 0 <= j < k:
                pos = [g.strip() for g in _str(r.get("top_pos_genes")).split(",") if g.strip()][:k_axes_genes]
                neg = [g.strip() for g in _str(r.get("top_neg_genes")).split(",") if g.strip()][:k_axes_genes]
                ax[j] = "+ " + ", ".join(pos) + (" | − " + ", ".join(neg) if neg else "") if pos else ""
                v = r.get("variance_pct_of_space")
                var[j] = round(float(v), 2) if v is not None and np.isfinite(float(v)) else None
    log(f"  tour: {len(cols):,} genes x {k} dimensions ({q.nbytes / 1e6:.2f} MB as int8)")
    return {"k": int(k), "n": int(len(cols)), "sc": [float(f"{s:.6g}") for s in sc], "q": _b64(q), "ax": ax,
            "var": var}


# ----------------------------------------------------------------------------- graph edges (physics tabs)
def _b64(arr):
    return base64.b64encode(np.ascontiguousarray(arr).tobytes()).decode("ascii")


def _edge_block(gd, ent, gK, n, pair_keys, pair_ev):
    """graph/edges.parquet between two map genes as compact base64 arrays (module docstring: `edges`).
    pair_keys / pair_ev: sorted keys lo * n + hi of the relations pairs and their best evidence code."""
    p = os.path.join(gd, "edges.parquet")
    if n == 0 or not os.path.exists(p):
        log("  no graph/edges.parquet: the module and all-genes tabs use the top-partner lists")
        return {"m": 0}
    e = _read(p, ["col_a", "col_b", "cos"])
    if not {"col_a", "col_b", "cos"} <= set(e.columns):
        log("  graph/edges.parquet lacks col_a / col_b / cos: the module and all-genes tabs use the top-partner lists")
        return {"m": 0}
    a = e["col_a"].to_numpy(dtype=np.int64)
    b = e["col_b"].to_numpy(dtype=np.int64)
    c = _num(e, "cos")
    ok = (a >= 0) & (a < gK) & (b >= 0) & (b < gK) & np.isfinite(c)
    ea = np.where(ok, ent[np.clip(a, 0, gK - 1)], -1)
    eb = np.where(ok, ent[np.clip(b, 0, gK - 1)], -1)
    ok &= (ea >= 0) & (ea < n) & (eb >= 0) & (eb < n) & (ea != eb)
    lo, hi, c = np.minimum(ea, eb)[ok], np.maximum(ea, eb)[ok], c[ok]
    key = lo * n + hi
    o = np.lexsort((-np.abs(c), key))                       # one row per pair: the strongest
    key, lo, hi, c = key[o], lo[o], hi[o], c[o]
    first = np.r_[True, key[1:] != key[:-1]] if len(key) else np.zeros(0, dtype=bool)
    key, lo, hi, c = key[first], lo[first], hi[first], c[first]
    ev = np.full(len(key), 2, dtype=np.uint8)                 # a graph edge missing from relations: as replicated
    if len(pair_keys) and len(key):
        pos = np.clip(np.searchsorted(pair_keys, key), 0, len(pair_keys) - 1)
        hit = pair_keys[pos] == key
        ev[hit] = pair_ev[pos[hit]]
    width, dt = (2, "<u2") if n <= 65535 else (4, "<u4")
    q = np.clip(np.rint(c * 100), -100, 100).astype(np.int8)
    log(f"  graph edges: {len(key):,} between map genes ({(ev == 2).sum():,} both halves, "
        f"{(ev == 1).sum():,} one half)")
    return {"m": int(len(key)), "bytes": width, "a": _b64(lo.astype(dt)), "b": _b64(hi.astype(dt)), "cos": _b64(q),
            "ev": _b64(ev)}


# ----------------------------------------------------------------------------- probable direction (direction stage)
S_MARK, T_MARK = "\x01", "\x02"      # in a text template: the row's source text / target name (module docstring)
_CELLS = "cells under "


def _templ(text, s, t):
    """A text of a row with its source text s and its target name t replaced by the marks; the page puts them back
    (first T_MARK -> t, then S_MARK -> s), which gives the text exactly (the marks never occur in a text)."""
    text = str(text or "")
    if s:
        text = text.replace(s, S_MARK)
    if t:
        text = text.replace(t, T_MARK)
    return text


def _fill(text, s, t):
    """The inverse of _templ (the page's fillT)."""
    return text.replace(T_MARK, t).replace(S_MARK, s)


def dir_missing(why):
    """The `dir` block of a page without the direction stage (an older output, or no stage run): the side panel and
    the arrow toggles say so."""
    return {"ok": False, "why": why}


class DirBlock:
    """The direction stage's display rows (direction_view: collapsed, in ORDER, with its wording) that touch a gene of
    the page (on the map or searchable), kept as texts, so that the `dir` block can be made again with shorter texts
    when the page would be too large (encode). A row is a gene's upstream row (it is the target), downstream row (it
    is a source, the target a gene) or cells row (it is a source, the target the cells under a drug-dose)."""

    def __init__(self, out, ent, gK):
        self.why = "no direction stage in this output (direction/edges.parquet is missing)"
        try:
            self.dv = dv = DV.load(out, cache=False)
        except (OSError, ValueError, KeyError, TypeError) as e:       # unreadable: the page says so, the map is made
            self.dv = dv = None
            self.why = f"the direction stage's files could not be read ({type(e).__name__}: {str(e)[:160]})"
            log(f"  direction: {self.why}")
        self.ok = dv is not None
        if not self.ok:
            return
        rows = dv.rows
        self.n_stage = len(rows)
        self.n_edges_stage = len(dv.edges)
        sens = set(DV.SENSITIVITY)
        kix = {k: i for i, k in enumerate(DV.KINDS)}
        gix = {g: i for i, g in enumerate(DV.GRADES)}

        def entry(c):
            c = int(c)
            return int(ent[c]) if 0 <= c < gK else -1
        al_cache = {}
        self.rows, self.out_rows = [], []
        for r in rows.itertuples(index=False):
            kind = str(r.kind)
            cells = kind in sens or str(r.target_type) == "cells"
            srcs = [str(x) for x in (r.sources or (r.source,))]
            se = [entry(c) for c in (r.source_cols or (r.source_col,))]
            tgt = str(r.target)
            te = int(r.target_dd) if cells else entry(r.target_col)
            if max(se + ([] if cells else [te])) < 0:
                self.out_rows.append(r)                     # touches no gene of the page (counted, said so)
                continue
            s = DV.source_text(r)
            t = tgt[len(_CELLS):] if cells and tgt.startswith(_CELLS) else tgt
            a = str(r.alerts or "")
            if a not in al_cache:
                al_cache[a] = (DV.alert_short(a), DV.alert_long(a))
            ash, alg = al_cache[a]
            sg = DV._sign(r)
            self.rows.append({
                "kgs": kix.get(kind, 15) + 16 * gix.get(str(r.grade), 3) + 64 * (sg + 1) + 256 * bool(r.has_alert),
                "cells": cells,
                "grade": str(r.grade), "alert": bool(r.has_alert), "srcs": list(zip(srcs, se)), "s": s, "tgt": tgt,
                "te": te, "edges": len(r.members or (0,)),
                "sign": _templ(DV.sign_text(r), s, t), "kind": _templ(DV.kind_text(r), s, t),
                "q": DV.q_text(r), "ash": _templ(ash, s, t), "alg": _templ(alg, s, t),
                "rd": _templ(str(r.reading or ""), s, t)})

    def encode(self, readings="all", long_alerts=True, cells_cap=None):
        """The `dir` block (module docstring). readings: 'all', 'AB' (grade A and B rows only) or 'none'; long_alerts
        False: the long alert texts are left out (the short labels stay); cells_cap n: a cells row is embedded only
        when it is among the rows a gene's capped list shows (the cap rule at n), the others are counted per gene
        (`cmore`)."""
        if not self.ok:
            return dir_missing(self.why)
        rows = self.rows
        keep = [True] * len(rows)
        cmore = []
        if cells_cap is not None:
            by = {}
            for k, r in enumerate(rows):
                if r["cells"]:
                    for _n, e in r["srcs"]:
                        if e >= 0:
                            by.setdefault(e, []).append(k)
            keep = [not r["cells"] for r in rows]
            for e, ks in by.items():
                for p in cap_rule([rows[k]["alert"] for k in ks], cells_cap):
                    keep[ks[p]] = True
            for e, ks in sorted(by.items()):
                miss = [k for k in ks if not keep[k]]
                if miss:
                    g = [sum(rows[k]["grade"] == x for k in miss) for x in DV.GRADES]
                    cmore += [e, len(miss), sum(rows[k]["alert"] for k in miss), *g]
        use = [r for r, k in zip(rows, keep) if k]
        # interned strings, the most frequent first (small ids): names (nm), texts (tx), source sets (ss)
        nm_c, tx_c = Counter(), Counter()
        for r in use:
            nm_c[r["s"]] += 1
            nm_c[r["tgt"]] += 1
            for n_, _e in r["srcs"]:
                nm_c[n_] += 1
            for f in ("sign", "kind", "q", "ash"):
                tx_c[r[f]] += 1
            if long_alerts:
                tx_c[r["alg"]] += 1
            if readings == "all" or (readings == "AB" and r["grade"] in ("A", "B")):
                tx_c[r["rd"]] += 1
        tx_c[""] += 0
        nm = [x for x, _ in nm_c.most_common()]
        tx = [""] + [x for x, _ in tx_c.most_common() if x != ""]
        nmi = {x: i for i, x in enumerate(nm)}
        txi = {x: i for i, x in enumerate(tx)}
        ss, ssi, flat = [], {}, []
        for r in use:
            key = (r["s"], tuple(r["srcs"]))
            if key not in ssi:
                ssi[key] = len(ss)
                v = [nmi[r["s"]]]
                for n_, e in r["srcs"]:
                    v += [nmi[n_], e]
                ss.append(v)
            rd = txi.get(r["rd"], -1) if (readings == "all" or (readings == "AB" and r["grade"] in ("A", "B"))) \
                else -1
            flat += [r["kgs"], ssi[key], nmi[r["tgt"]], r["te"], txi[r["sign"]], txi[r["kind"]], txi[r["q"]],
                     txi[r["ash"]], txi[r["alg"]] if long_alerts else -1, rd]
        short = []
        if readings != "all":
            short.append("the readings (each row's sentence with its numbers) of the grade C rows" if readings == "AB"
                         else "the readings (each row's sentence with its numbers)")
        if not long_alerts:
            short.append("the alerts' full wording (each alert keeps its short label)")
        n_c = sum(cmore[1::6])
        if cells_cap is not None and n_c:
            short.append(f"{n_c:,} cells rows beyond the {cells_cap} a gene's list shows (each gene's list counts "
                         "them)")
        dv = self.dv
        nd = sum(r["edges"] for r in use)
        out_names = sorted({str(r.source) for r in self.out_rows})
        return {
            "ok": True, "w": DIR_FIELDS, "r": flat, "nm": nm, "tx": tx, "ss": ss, "cmore": cmore, "cap": N_DIR,
            "kinds": list(DV.KINDS), "kshort": [DV.KIND_SHORT[k] for k in DV.KINDS],
            "kwords": [DV.KIND_WORDS[k] for k in DV.KINDS], "sens": [k in DV.SENSITIVITY for k in DV.KINDS],
            "grades": list(DV.GRADES), "gwords": [DV.GRADE_WORDS[g] for g in DV.GRADES],
            "gshort": [DV.GRADE_SHORT[g] for g in DV.GRADES], "signw": [DV.sign_word(s) for s in (-1, 0, 1)],
            "signw_resp": [DV.sign_word(s, DV.RESPONSE[0]) for s in (-1, 0, 1)],
            "resp": [k in DV.RESPONSE for k in DV.KINDS],
            "caveat": DV.CAVEAT, "caveat_short": DV.CAVEAT_SHORT, "caveat_lines": DV.caveat_lines(),
            "order": DV.ORDER, "counts": dv.counts(), "n_rows_stage": self.n_stage, "n_edges_stage": self.n_edges_stage,
            "n_rows": len(use), "n_edges": nd, "n_rows_out": len(self.out_rows),
            "n_rows_out_alert": int(sum(bool(r.has_alert) for r in self.out_rows)),
            "rows_out_sources": out_names[:12], "n_rows_out_sources": len(out_names), "short": short,
            "lines": (dv.info or {}).get("lines")}


# ----------------------------------------------------------------------------- the data block
def build_data(out, partners=N_PARTNERS, drugs=N_DRUGS, lines=N_LINES, fn_chars=FN_CHARS):
    """Everything the page shows, as one dict of lists (see the module docstring for the layout)."""
    gd, td, ed = (os.path.join(out, d) for d in ("graph", "tables", "embed"))
    for p in (os.path.join(gd, "nodes.parquet"), os.path.join(td, "genes.parquet"),
              os.path.join(out, "relations", "gene_relations.parquet")):
        if not os.path.exists(p):
            raise SystemExit(f"map: {p} is missing; run the earlier stages first")

    # ---- entries: map genes (graph order), then every other gene col
    nodes = _read(os.path.join(gd, "nodes.parquet"), ["col", "module", "arm", "x", "y", "xs", "ys", "xm", "ym", "xsm",
                                                       "ysm"])
    tg = _read(os.path.join(td, "genes.parquet"), ["col", "symbol", "label", "pooled_cpm", "noise_rna", "n_dd_up",
                                                    "n_dd_down", "n_dd_up_clean", "n_dd_down_clean",
                                                    "n_lines_expressing"]).sort_values("col")
    gK = int(max(tg["col"].max(), nodes["col"].max())) + 1
    on = nodes["col"].to_numpy(dtype=np.int64)
    is_on = np.zeros(gK, dtype=bool)
    is_on[on] = True
    off = np.array([c for c in tg["col"].to_numpy(dtype=np.int64) if not is_on[c]], dtype=np.int64)
    order = np.concatenate([on, off])
    n, na = len(on), len(order)
    ent = np.full(gK, -1, dtype=np.int64)
    ent[order] = np.arange(na)
    log(f"Map: {n:,} genes on the map, {len(off):,} more searchable")

    lab = np.array([""] * gK, dtype=object)
    lab[tg["col"].to_numpy()] = tg["label"].fillna(tg["symbol"]).astype(str).to_numpy() if "label" in tg else \
        tg["symbol"].astype(str).to_numpy()
    sym = [s or f"col{c}" for s, c in zip(lab[order].tolist(), order.tolist())]

    def per_col(values, fill):
        arr = np.full(gK, fill, dtype=np.float64)
        arr[tg["col"].to_numpy()] = values
        return arr[order]

    cpm = per_col(_num(tg, "pooled_cpm"), np.nan)
    cpm = [round(v, 1) if v < 10 else int(round(v)) for v in np.nan_to_num(cpm, nan=0.0).tolist()]
    # significant drug-doses raising / lowering it: all of them, and how many carry an artifact flag
    counts = {}
    for d in ("up", "down"):
        clean_n = np.nan_to_num(per_col(_num(tg, f"n_dd_{d}_clean", 0), 0), nan=0).astype(np.int64)
        all_n = np.nan_to_num(per_col(_num(tg, f"n_dd_{d}", np.nan), np.nan), nan=-1).astype(np.int64)
        all_n = np.where(all_n >= 0, all_n, clean_n)              # an older tables stage: the clean count only
        counts[d] = (all_n.tolist(), np.maximum(all_n - clean_n, 0).tolist())
    (nup, nupa), (ndn, ndna) = counts["up"], counts["down"]
    nlx = per_col(np.nan_to_num(_num(tg, "n_lines_expressing", -1), nan=-1), -1).astype(np.int64).tolist()

    # ---- the stages' own rules and cuts (embed: inclusion; tables: calibrated per-line cut; relations: novelty)
    einfo = _info(os.path.join(ed, "info.json"))
    min_resp = einfo.get("min_responsive")
    embed_rule = {k: einfo.get(k) for k in ("min_responsive", "min_active", "contexts", "drugdoses_active",
                                            "drugdoses_total", "lines", "line_z_responsive", "n_genes_excluded_chance",
                                            "null_rate", "n_genes_evidence_flagged_only")}
    tinfo = _info(os.path.join(td, "info.json"))
    line_z_cal = tinfo.get("line_z_threshold") is not None
    line_z = float(tinfo["line_z_threshold"]) if line_z_cal else LINE_Z_FALLBACK
    line_chance = tinfo.get("line_z_expected_chance")
    rinfo = _info(os.path.join(out, "relations", "info.json"))
    if "novel_assessed" in rinfo:
        novel_ok, novel_blocked = bool(rinfo["novel_assessed"]), [str(x) for x in rinfo.get("novel_blocked_by") or []]
    else:                                         # older relations stage: novelty needed the reference stage
        novel_ok = os.path.exists(os.path.join(out, "reference", "annotations.parquet"))
        novel_blocked = [] if novel_ok else ["the reference stage"]
    why, efo, fo_sym = [-2] * len(off), [], set()
    if os.path.exists(os.path.join(ed, "genes.parquet")):
        eg = _read(os.path.join(ed, "genes.parquet"), ["col", "symbol", "included", "n_responsive_contexts",
                                                        "noise_rna", "evidence_flagged_only"])
        ec = eg["col"].to_numpy(dtype=np.int64)
        okc = (ec >= 0) & (ec < gK)
        nr = np.full(gK, -2, dtype=np.int64)
        resp = np.nan_to_num(_num(eg, "n_responsive_contexts", 0), nan=0).astype(np.int64)
        v = np.where(_bool(eg, "noise_rna"), -1, np.where(_bool(eg, "included"), -2, resp))
        nr[ec[okc]] = v[okc]
        why = nr[off].tolist()
        fo = np.zeros(gK, dtype=bool)
        fo[ec[okc]] = _bool(eg, "evidence_flagged_only")[okc]
        efo = np.flatnonzero(fo[order]).tolist()          # entries in the space only through flagged drug-doses
        if "symbol" in eg:
            fo_sym = set(eg["symbol"].astype(str)[_bool(eg, "evidence_flagged_only")])

    # ---- reference annotations (optional)
    name, fn, alias = [], [], []
    ap = os.path.join(out, "reference", "annotations.parquet")
    have_ref = os.path.exists(ap)
    if have_ref:
        an = _read(ap, ["col", "symbol", "hgnc_symbol", "name", "protein_name", "function", "ncbi_summary",
                        "aliases", "prev_symbols"])
        acol = an["col"].to_numpy(dtype=np.int64)
        keep = (acol >= 0) & (acol < gK)
        an, acol = an[keep], acol[keep]
        nm = np.array([""] * gK, dtype=object)
        fx = np.array([""] * gK, dtype=object)
        al = np.array([""] * gK, dtype=object)
        cols = {c: (an[c].tolist() if c in an else [None] * len(an)) for c in
                ("symbol", "hgnc_symbol", "name", "protein_name", "function", "ncbi_summary", "aliases",
                 "prev_symbols")}
        for i, c in enumerate(acol.tolist()):
            nm[c] = _str(cols["name"][i]) or _str(cols["protein_name"][i])
            fx[c] = _snippet(cols["function"][i], fn_chars) or _snippet(cols["ncbi_summary"][i], fn_chars)
            own = _str(cols["symbol"][i]).upper()
            names = []
            hs = _str(cols["hgnc_symbol"][i])
            if hs and hs.upper() != own:
                names.append(hs)
            for f in ("aliases", "prev_symbols"):
                names += [t.strip() for t in re.split(r"[|,;]", _str(cols[f][i])) if t.strip()]
            seen, keep_ = {own}, []
            for t in names:
                if t.upper() not in seen:
                    seen.add(t.upper())
                    keep_.append(t)
            al[c] = "|".join(keep_)
        name, fn, alias = nm[order].tolist(), fx[order].tolist(), al[order].tolist()
        log(f"  reference: {sum(1 for s in name if s):,} names, {sum(1 for s in fn if s):,} function snippets")
    else:
        log("  no reference annotations: names, functions and aliases are left out")

    # ---- relations: top partners per map gene (by the relations rank)
    rel = _read(os.path.join(out, "relations", "gene_relations.parquet"),
                ["col_a", "col_b", "rank", "cos", "abs_cos", "evidence", "fdr", "locus", "readthrough_risk",
                 "shared_gene_group", "shared_pathway", "string_score", "known", "novel_candidate", "alert"])
    a = rel["col_a"].to_numpy(dtype=np.int64)
    b = rel["col_b"].to_numpy(dtype=np.int64)
    ok = (a >= 0) & (a < gK) & (b >= 0) & (b < gK)
    ea = np.where(ok, ent[np.clip(a, 0, gK - 1)], -1)
    eb = np.where(ok, ent[np.clip(b, 0, gK - 1)], -1)
    ok &= (ea >= 0) & (ea < n) & (eb >= 0) & (eb < n)
    rel = rel[ok].reset_index(drop=True)
    ea, eb = ea[ok], eb[ok]
    # every pair's best evidence (before the top-k cut): the graph edges below carry it
    ev_all = rel["evidence"].map(EVIDENCE).fillna(0).astype(np.int64).to_numpy() if "evidence" in rel else \
        np.zeros(len(rel), dtype=np.int64)
    pev = pd.Series(ev_all).groupby(np.minimum(ea, eb) * n + np.maximum(ea, eb)).max()
    pair_keys, pair_ev = pev.index.to_numpy(dtype=np.int64), pev.to_numpy().astype(np.uint8)
    del ev_all, pev
    rank = _num(rel, "rank") if "rank" in rel else -np.abs(_num(rel, "cos"))
    o = np.lexsort((np.nan_to_num(rank, nan=1e9), ea))
    rel, ea, eb = rel.iloc[o].reset_index(drop=True), ea[o], eb[o]
    # a partner's alert (the reasons of relations' 'alert' column): not replicated in both halves, a genomic reason
    # (same locus, read-through) for the correlation, or the PARTNER in the space only through flagged drug-doses.
    # The selected gene's own such reason is in every one of its rows; it is stated once in the panel instead, so it
    # neither marks every partner nor stops the cap from adding the strongest partners without an alert.
    ev = rel["evidence"].map(EVIDENCE).fillna(0).astype(np.int64).to_numpy() if "evidence" in rel else \
        np.zeros(len(rel), dtype=np.int64)
    efo_m = np.zeros(na, dtype=bool)
    efo_m[efo] = True
    r_alert = (ev < 2) | _bool(rel, "locus") | _bool(rel, "readthrough_risk") | efo_m[eb]
    reln = np.zeros((n, 2), dtype=np.int64)                  # per map gene: partners in relations, with an alert
    np.add.at(reln, ea, np.column_stack([np.ones(len(ea), dtype=np.int64), r_alert.astype(np.int64)]))
    k = cap_keep(ea, ~r_alert, partners)
    rel, ea, eb, ev = rel[k].reset_index(drop=True), ea[k], eb[k], ev[k]
    pw_names = rel["shared_pathway"].map(_str) if "shared_pathway" in rel else pd.Series([""] * len(rel))
    codes, pw = pd.factorize(pw_names.where(pw_names != "", None))
    sscore = np.clip(_scaled(_num(rel, "string_score"), 0.1, 0), 0, 127)
    flags = (ev + 4 * _bool(rel, "locus") + 8 * _bool(rel, "readthrough_risk") + 16 * _bool(rel, "shared_gene_group")
             + 32 * _bool(rel, "known") + 64 * _bool(rel, "novel_candidate") + 256 * sscore
             + 32768 * (codes.astype(np.int64) + 1))
    rmat = np.column_stack([eb, _scaled(_num(rel, "cos"), 100), _scaled(_num(rel, "fdr"), 100, -1), flags])
    rel_lists = _lists(ea, rmat, n)
    shown_pairs = np.unique(np.minimum(ea, eb) * n + np.maximum(ea, eb))   # the side panel's partner pairs
    log(f"  relations: {len(rel):,} partner rows for {int((np.diff(np.r_[-1, ea]) != 0).sum()):,} genes, "
        f"{len(pw):,} shared pathways")
    del rel
    edges = _edge_block(gd, ent, gK, n, pair_keys, pair_ev)
    del pair_keys, pair_ev
    k_edges = _info(os.path.join(gd, "info.json")).get("k_edges")

    # ---- drug-doses up / down: every row of the fold-change table, flagged ones in their ranked place with an alert
    ft = FlagTable()
    de = _read(os.path.join(td, "drug_effects.parquet"),
               ["col", "dd", "lfc", "z", "clean", "flags", "cc_share", "n_lines_up", "n_lines_down"])
    dc = de["col"].to_numpy(dtype=np.int64)
    de_ent = np.where((dc >= 0) & (dc < gK), ent[np.clip(dc, 0, gK - 1)], -1)
    z = _num(de, "z")
    de_flags = de["flags"].map(_str).to_numpy() if "flags" in de else np.array([""] * len(de), dtype=object)
    de_alert = ~_bool(de, "clean") if "clean" in de else np.array([A.has_artifact(f) for f in de_flags], dtype=bool)
    up_lists, dn_lists, dct = [], [], np.zeros((na, 4), dtype=np.int64)
    for t, (sign, nl_col, store) in enumerate(((1, "n_lines_up", up_lists), (-1, "n_lines_down", dn_lists))):
        m = (de_ent >= 0) & np.isfinite(z) & (sign * z > 0)
        e, zz = de_ent[m], sign * z[m]
        np.add.at(dct, (e, 2 * t), 1)
        np.add.at(dct, (e, 2 * t + 1), de_alert[m].astype(np.int64))
        o = np.lexsort((-zz, e))
        idx = np.flatnonzero(m)[o]
        e = e[o]
        kk = cap_keep(e, ~de_alert[idx], drugs)
        idx, e = idx[kk], e[kk]
        sub = de.iloc[idx]
        f = ft.codes(de_flags[idx], de_alert[idx], _num(sub, "cc_share"))
        mat = np.column_stack([_num(sub, "dd").astype(np.int64), _scaled(sign * _num(sub, "lfc"), 100),
                               _scaled(sign * _num(sub, "z"), 10), _scaled(_num(sub, nl_col), 1), f])
        store.extend(_lists(e, mat, na))
    log(f"  drug-doses: {len(de):,} rows ({int(de_alert.sum()):,} with an artifact flag) -> the {drugs} strongest up / "
        f"down per gene, plus unflagged ones of the first {drugs} beyond them")
    del de

    # ---- cell lines where the gene responds most: counts over all drug-doses (how many of them carry an artifact
    # flag) and the strongest drug-dose, flagged or not, when the tables stage has them (the *_all columns)
    best = [f"best_{d}_{c}{x}" for d in ("up", "down") for c in ("dd", "lfc", "z", "flags", "clean", "cc_share")
            for x in ("", "_all")]
    le = _read(os.path.join(td, "line_effects.parquet"),
               ["col", "line", "expressed", "response_sd", "n_dd_up", "n_dd_down", "n_dd_up_all", "n_dd_down_all"]
               + best)
    if "expressed" in le:
        le = le[le["expressed"].fillna(False).astype(bool)]
    ln_all = "n_dd_up_all" in le and "best_up_dd_all" in le
    x = "_all" if ln_all else ""
    lc = le["col"].to_numpy(dtype=np.int64)
    le_ent = np.where((lc >= 0) & (lc < gK), ent[np.clip(lc, 0, gK - 1)], -1)
    nu_c = np.nan_to_num(_num(le, "n_dd_up", 0), nan=0)
    nd_c = np.nan_to_num(_num(le, "n_dd_down", 0), nan=0)
    nu = np.maximum(np.nan_to_num(_num(le, "n_dd_up" + x, 0), nan=0), nu_c)
    nd = np.maximum(np.nan_to_num(_num(le, "n_dd_down" + x, 0), nan=0), nd_c)
    sd = np.nan_to_num(_num(le, "response_sd"), nan=-1)
    score, score_c = nu + nd, nu_c + nd_c
    m = le_ent >= 0
    # the lines with the most responding drug-doses (up to `lines`), plus any of the `lines` with the most unflagged
    # ones that fall beyond them; a gene with none in any line keeps its 2 most variable lines
    o = np.lexsort((-sd[m], -score_c[m], le_ent[m]))
    idx_c = np.flatnonzero(m)[o]
    top_c = np.zeros(len(le), dtype=bool)
    top_c[idx_c[_first_k(le_ent[idx_c], lines) & (score_c[idx_c] > 0)]] = True
    o = np.lexsort((-sd[m], -score[m], le_ent[m]))
    idx = np.flatnonzero(m)[o]
    e = le_ent[idx]
    has_any = np.zeros(na, dtype=bool)
    has_any[e[score[idx] > 0]] = True
    keep = (_first_k(e, lines) & ((score[idx] > 0) | (~has_any[e] & _first_k(e, 2)))) | top_c[idx]
    idx, e = idx[keep], e[keep]
    bu, bd = _num(le, "best_up_z" + x)[idx], _num(le, "best_down_z" + x)[idx]
    use_up = np.nan_to_num(bu, nan=-np.inf) >= -np.nan_to_num(bd, nan=np.inf)
    bv = {c: np.where(use_up, _num(le, f"best_up_{c}{x}")[idx], _num(le, f"best_down_{c}{x}")[idx])
          for c in ("dd", "lfc", "cc_share")}
    bdd, blfc, bz = bv["dd"], bv["lfc"], np.where(use_up, bu, bd)
    has_best = np.isfinite(bdd) & np.isfinite(bz) & (np.abs(np.nan_to_num(bz)) >= line_z)
    bdd = np.where(has_best, bdd, -1)
    if ln_all:
        sub = le.iloc[idx]
        bfl = np.where(use_up, sub["best_up_flags_all"].map(_str).to_numpy() if "best_up_flags_all" in sub else "",
                       sub["best_down_flags_all"].map(_str).to_numpy() if "best_down_flags_all" in sub else "")
        bal = ~np.where(use_up, _bool(sub, "best_up_clean_all"), _bool(sub, "best_down_clean_all")) \
            if "best_up_clean_all" in sub else np.array([A.has_artifact(f_) for f_ in bfl], dtype=bool)
        bf = np.where(has_best, ft.codes(bfl, bal, bv["cc_share"]), 0)
    else:
        bal = np.zeros(len(idx), dtype=bool)
        bf = np.zeros(len(idx), dtype=np.int64)
    # when the strongest carries an alert: the line's strongest drug-dose without one (the clean best_* columns, by the
    # same direction rule), so the flagged one does not push it out of view
    cu, cdn = _num(le, "best_up_z")[idx], _num(le, "best_down_z")[idx]
    c_up = np.nan_to_num(cu, nan=-np.inf) >= -np.nan_to_num(cdn, nan=np.inf)
    cdd = np.where(c_up, _num(le, "best_up_dd")[idx], _num(le, "best_down_dd")[idx])
    clfc = np.where(c_up, _num(le, "best_up_lfc")[idx], _num(le, "best_down_lfc")[idx])
    cz = np.where(c_up, cu, cdn)
    has_c = bool(ln_all) & has_best & bal & np.isfinite(cdd) & np.isfinite(cz) & \
        (np.abs(np.nan_to_num(cz)) >= line_z)
    cdd, clfc, cz = np.where(has_c, cdd, -1), np.where(has_c, clfc, 0.0), np.where(has_c, cz, 0.0)
    lmat = np.column_stack([_num(le, "line")[idx].astype(np.int64), nu[idx].astype(np.int64),
                            (nu - nu_c)[idx].astype(np.int64), nd[idx].astype(np.int64),
                            (nd - nd_c)[idx].astype(np.int64), bdd.astype(np.int64),
                            _scaled(blfc, 100), _scaled(bz, 10), bf, cdd.astype(np.int64),
                            _scaled(clfc, 100), _scaled(cz, 10)])
    ln_lists = _lists(e, lmat, na)
    log(f"  cell lines: {len(le):,} gene x line rows -> up to {lines} lines per gene"
        + (f" (counts over all drug-doses, flagged ones counted apart; {int(has_c.sum()):,} shown lines whose "
           "strongest drug-dose carries an alert also name their strongest without one)" if ln_all else
           " (an older tables stage: counts over the clean drug-doses only)"))
    del le

    # ---- labels: drug-doses, lines, modules
    dlab, dart, ddf = [], [], []
    dp = os.path.join(td, "drugdoses.parquet")
    if os.path.exists(dp):
        dd = _read(dp, ["dd", "drug", "dose", "flags"])
        ddi = dd["dd"].to_numpy(dtype=np.int64) if "dd" in dd else np.arange(len(dd))
        dlab = [""] * (int(ddi.max()) + 1 if len(ddi) else 0)
        dart, ddf = [False] * len(dlab), [0] * len(dlab)
        fl = dd["flags"].map(_str) if "flags" in dd else pd.Series([""] * len(dd))
        for i, d_, s_, f_ in zip(ddi.tolist(), dd["drug"].map(_str), dd["dose"].map(_str), fl):
            dlab[i] = f"{d_} {s_} uM".strip()
            dart[i] = A.has_artifact(f_)
            ddf[i] = ft.code(f_, dart[i])                     # the drug-dose's own flags (module card)
    llab, organ = [], []
    lp = os.path.join(td, "lines.parquet")
    if os.path.exists(lp):
        li = _read(lp, ["line", "cell_name", "cell_line_id", "Organ"])
        lii = li["line"].to_numpy(dtype=np.int64) if "line" in li else np.arange(len(li))
        size = int(lii.max()) + 1 if len(lii) else 0
        llab, organ = [""] * size, [""] * size
        cn = li["cell_name"].map(_str) if "cell_name" in li else pd.Series([""] * len(li))
        cid = li["cell_line_id"].map(_str) if "cell_line_id" in li else pd.Series([""] * len(li))
        org = li["Organ"].map(_str) if "Organ" in li else pd.Series([""] * len(li))
        for i, c_, d_, o_ in zip(lii.tolist(), cn, cid, org):
            llab[i], organ[i] = c_ or d_ or f"line {i}", o_

    vlab = _validation_labels(out)
    mods = []
    mp = os.path.join(gd, "modules.parquet")
    if os.path.exists(mp):
        md = pd.read_parquet(mp).sort_values("module").reset_index(drop=True)
        zp = os.path.join(gd, "module_pooled_z.npy")
        MZ = np.load(zp) if os.path.exists(zp) else None
        if MZ is not None and MZ.shape[0] != len(md):
            log(f"  module_pooled_z.npy has {MZ.shape[0]} rows for {len(md)} modules: drug lists from modules.parquet")
            MZ = None
        for k, r in enumerate(md.to_dict("records")):
            mid = int(r["module"])
            fallback = _top_genes_label(r.get("top_plus"), r.get("top_minus"))
            opp = bool(r["arms_opposite"]) if r.get("arms_opposite") is not None else int(r.get("n_minus", 0)) > 0
            cb = r.get("mean_cos_between_arms")
            cb = round(float(cb), 2) if cb is not None and np.isfinite(float(cb)) else None
            drugs_ = {}
            if MZ is not None:
                (drugs_["up"], drugs_["nup"]), (drugs_["dn"], drugs_["ndn"]) = \
                    _module_drugs(MZ[k], dart, 1), _module_drugs(MZ[k], dart, -1)
            else:                                 # older graph stage: its lists as text
                drugs_ = {"up_txt": _str(r.get("drugs_up")), "dn_txt": _str(r.get("drugs_down"))}
            mods.append({"id": mid, "n": int(r.get("n_genes", 0)), "np": int(r.get("n_plus", 0)),
                         "nm": int(r.get("n_minus", 0)), "label": vlab.get(mid) or fallback,
                         "genes": fallback, "plus": _arm_text(r.get("top_plus"), fo_sym),
                         "minus": _arm_text(r.get("top_minus"), fo_sym),
                         "opp": opp, "cb": cb, **drugs_, "lines": _str(r.get("responsive_lines"))})
    labels_from = "validation" if vlab else "graph"

    def xy(c):
        v = nodes[c].to_numpy(dtype=np.float64)
        return np.round(np.nan_to_num(v, nan=0.0, posinf=0.0, neginf=0.0), 2).tolist()

    arm = "".join(a if a in ("+", "-") else "." for a in nodes["arm"].fillna("").astype(str).tolist())
    lit = _literature(out, tg, ent, gK, n, shown_pairs)
    spread = {c: xy(c) for c in ("xm", "ym", "xsm", "ysm")} if {"xm", "ym", "xsm", "ysm"} <= set(nodes.columns) else {}
    if not spread:
        log("  graph/nodes.parquet has no spread layouts (an older graph stage): the Spread slider is off")
    ginfo = _info(os.path.join(gd, "info.json"))
    grule = {k: ginfo.get(k) for k in ("k_edges", "min_edge", "one_half_edge", "max_module", "loose_cos",
                                        "split_depth", "min_module", "arms_opposite_cos", "spread")}
    tour = _tour_block(out, on)
    dblock = DirBlock(out, ent, gK)
    if dblock.ok:
        log(f"  direction: {len(dblock.rows):,} of the stage's {dblock.n_stage:,} display rows touch a gene of the "
            f"page ({len(dblock.out_rows):,} do not: their source is no measured gene and their target none of the "
            "page's genes)")
    elif "missing" in dblock.why:
        log("  no direction/edges.parquet (the direction stage has not run): the page says so")
    return {
        "v": VERSION, "title": "Tahoe-100M gene map", "made": time.strftime("%Y-%m-%d"),
        "n": n, "scale": {"cos": 100, "fdr": 100, "lfc": 100, "z": 10},
        "col": order.tolist(), "sym": sym,
        "x": xy("x"), "y": xy("y"), "xs": xy("xs"), "ys": xy("ys"), **spread,
        "mod": nodes["module"].fillna(0).astype(np.int64).tolist(), "arm": arm,
        "name": name, "fn": fn, "alias": alias,
        "cpm": cpm, "nup": nup, "nupa": nupa, "ndn": ndn, "ndna": ndna, "nlx": nlx, "why": why, "efo": efo,
        "rel": rel_lists, "reln": reln.ravel().tolist(), "pw": [str(p) for p in pw],
        "up": up_lists, "dn": dn_lists, "dct": dct.ravel().tolist(), "ln": ln_lists, "lnw": LN_WIDTH,
        "ln_all": bool(ln_all),
        "fl": ft.rows, "dd": dlab, "ddf": ddf, "lines": llab, "organ": organ, "mods": mods,
        "palette": PALETTE, "ref": bool(have_ref), "labels_from": labels_from, "min_responsive": min_resp,
        "embed": embed_rule, "line_z": round(line_z, 2), "line_z_cal": line_z_cal,
        "line_chance": round(float(line_chance), 3) if line_chance is not None else None,
        "novel_ok": novel_ok, "novel_blocked": novel_blocked, "mod_z": MOD_Z,
        "edges": edges, "k_edges": int(k_edges) if isinstance(k_edges, (int, float)) else None,
        "grule": grule, "tour": tour, "n_partners": partners, "n_drugs": drugs, "n_lines": lines,
        "halves": bool(einfo.get("halves", True)),
        "n_mod_drugs": N_MOD_DRUGS,
        "dir": dblock.encode(), "_dir": dblock,
        **lit,
    }


def _literature(out, tg, ent, gK, n, shown_pairs):
    """The gene-gene connection verdicts of the literature reviews (OUT/review) on the side panel's partner pairs
    (shown_pairs: sorted min(a, b) * n + max(a, b) of the embedded top-partner lists), as the {"lit": [...],
    "lit_v": [...]} entries of the page data; {} without reviews (the page is then as before). The verdicts of each
    gene's latest review (vault.review_rank: a gene reviewed twice shows what its vault note shows), one per partner,
    chosen by vault.pick_verdict (the vault's rule); each is shown as vault.verdict_label says:
    the shown verdict (shown_verdict: 'unverified' when the citation check found it not supported, every citation
    was removed as not found, or every paper it cites is retracted) and its check_status, then ' (cites a retracted
    paper)' when a paper it cites is retracted (the badge and its tooltip)."""
    if V.review_fingerprint(out) is None:
        return {}
    by = {}
    labels = tg["label"] if "label" in tg else tg["symbol"]
    for c, s_, lab in zip(tg["col"].to_numpy(dtype=np.int64), tg["symbol"].map(_str), labels.map(_str)):
        for k in (lab, s_):
            if k:
                by.setdefault(k.upper(), int(c))
    kinds, flat = {}, []
    for r in V.review_connections(out, gene_col=lambda x: by.get(str(x).upper())):
        eid, pk = _str(r.get("entity_id")), _str(r.get("partner_kind")) or "gene"
        pc = r.get("partner_col")
        if not eid.startswith("gene:") or pk != "gene" or not eid[5:].isdigit() or pc is None or pd.isna(pc):
            continue
        a, b = int(eid[5:]), int(pc)
        if not (0 <= a < gK and 0 <= b < gK) or ent[a] < 0 or ent[a] >= n or ent[b] < 0 or ent[b] >= n:
            continue
        key = min(ent[a], ent[b]) * n + max(ent[a], ent[b])
        i = np.searchsorted(shown_pairs, key)
        if i >= len(shown_pairs) or shown_pairs[i] != key:
            continue                                       # not a pair the side panel lists
        if not _str(r.get("verdict")):
            continue
        label, expl = V.verdict_label(r)
        k = kinds.setdefault((label, expl, r["shown_verdict"], r["check_status"]), len(kinds))
        n_c = len([x for x in _str(r.get("citations")).split(";") if x.strip()])
        flat += [int(ent[a]), int(ent[b]), k, n_c]
    log(f"  literature: {len(flat) // 4:,} connection verdicts on the side panel's partner pairs "
        "(review/connections.parquet, one per review and partner)")
    return {"lit": flat, "lit_v": [list(k) for k in kinds]}


def _encode(data):
    """Compact JSON that is safe inside a <script> element (keys starting with '_' are the builder's, not the
    page's)."""
    s = json.dumps({k: v for k, v in data.items() if not k.startswith("_")}, separators=(",", ":"),
                   ensure_ascii=False, allow_nan=False)
    return s.replace("<", "\\u003c")


def _shrink(data, fn_chars, lines):
    """Shorter function snippets and line lists (only when the page would be too large)."""
    data["fn"] = [s if len(s) <= fn_chars else _snippet(s, fn_chars) for s in data["fn"]]
    if lines is not None:
        data["ln"] = [v[:LN_WIDTH * lines] for v in data["ln"]]
    return data


def render(data):
    payload = _encode(data)
    title = data.get("title", "gene map").replace("<", "").replace("&", "and")
    return _TEMPLATE.replace("__TITLE__", title).replace("__DATA__", payload)


def _shrink_steps(data):
    """The ways to make a too-large page smaller, in order, each on top of the ones before: (what is shortened, in
    words; a function that shortens it). Texts only: no gene, partner, drug-dose or direction row is left out; the
    last step leaves out the cells rows beyond a gene's capped list, and each gene's list counts them."""
    db, opt = data.get("_dir"), {}

    def direction(**kw):
        def f(d):
            opt.update(kw)
            d["dir"] = db.encode(**opt)
        return f
    steps = []
    if db is not None and db.ok:
        steps += [("the direction readings of the grade C rows", direction(readings="AB")),
                  ("every direction reading", direction(readings="none"))]
    steps += [(f"the function snippets to {fc} characters" + (f" and the line lists to {nl}" if nl else ""),
               (lambda fc_, nl_: lambda d: _shrink(d, fc_, nl_))(fc, nl)) for fc, nl in ((80, None), (60, 3), (40, 2))]
    if db is not None and db.ok:
        steps += [("the direction alerts' full wording (their short labels stay)", direction(long_alerts=False)),
                  (f"the cells rows beyond the {N_DIR} of a gene's list (counted there)", direction(cells_cap=N_DIR))]
    return steps


def run(out, partners=N_PARTNERS, drugs=N_DRUGS, lines=N_LINES, fn_chars=FN_CHARS, max_bytes=MAX_BYTES):
    t0 = time.time()
    warnings.filterwarnings("ignore", category=RuntimeWarning)
    md = folder(out, "map")
    with np.errstate(invalid="ignore", divide="ignore"):
        data = build_data(out, partners=partners, drugs=drugs, lines=lines, fn_chars=fn_chars)
    page = render(data)
    size = len(page.encode("utf-8"))
    shortened = []
    for what, step in _shrink_steps(data):                 # keep the page loadable on a laptop
        if size <= max_bytes:
            break
        log(f"  page is {size / 1e6:.1f} MB: shortening {what}")
        step(data)
        shortened.append(what)
        page = render(data)
        size = len(page.encode("utf-8"))
    dr = data.get("dir") or {}
    path = os.path.join(md, "gene_map.html")
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        fh.write(page)
    replace_file(tmp, path)
    n_rel = sum(1 for r in data["rel"] if r)
    info = {"version": VERSION, "file": path, "bytes": size, "mb": round(size / 1e6, 2),
            "genes_on_map": data["n"], "genes_searchable": len(data["sym"]), "genes_with_partners": n_rel,
            "graph_edges": data["edges"].get("m", 0), "graph_edges_bytes": sum(len(data["edges"].get(k, ""))
                                                                              for k in ("a", "b", "cos", "ev")),
            "modules": len(data["mods"]), "module_labels_from": data["labels_from"], "reference": data["ref"],
            "partners": partners, "drugs": drugs, "lines": lines,
            "literature_verdicts": len(data.get("lit") or []) // 4, "review": V.review_fingerprint(out),
            "spread_layouts": "xm" in data, "tour_dims": (data.get("tour") or {}).get("k"),
            "tour_bytes": len((data.get("tour") or {}).get("q", "")), "flag_texts": len(data.get("fl") or []),
            "direction": bool(dr.get("ok")), "direction_rows": dr.get("n_rows", 0),
            "direction_rows_stage": dr.get("n_rows_stage", 0), "direction_rows_no_page_gene": dr.get("n_rows_out", 0),
            "direction_bytes": len(_encode({"dir": dr}).encode("utf-8")), "shortened": shortened,
            "minutes": round((time.time() - t0) / 60, 2)}
    stamp_stage(out, "map", VERSION, info)
    log(f"Map done: {path} ({info['mb']} MB, {data['n']:,} genes on the map, {info['minutes']} min)")
    return info


# ----------------------------------------------------------------------------- the page
_TEMPLATE = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="icon" href="data:,">
<title>__TITLE__</title>
<style>
:root{--surface:#fcfcfb;--page:#f9f9f7;--ink:#0b0b0b;--ink2:#52514e;--muted:#898781;--grid:#e1e0d9;--axis:#c3c2b7;
--ring:rgba(11,11,11,.12);--with:#0ca30c;--opp:#d03b3b;--accent:#2a78d6;--hl:#eef3fb}
*{box-sizing:border-box}
html,body{margin:0;height:100%;font:13px/1.4 system-ui,-apple-system,"Segoe UI",sans-serif;color:var(--ink);background:var(--page)}
body{display:flex;flex-direction:column;overflow:hidden}
header{display:flex;align-items:flex-end;gap:4px 16px;padding:0 12px;border-bottom:1px solid var(--grid);background:var(--surface);flex-wrap:wrap}
header h1{font-size:15px;margin:0 2px 11px 0;font-weight:600;white-space:nowrap}
#tabs{display:flex;flex-wrap:wrap}
#tabs button{border:0;border-bottom:2px solid transparent;background:transparent;padding:12px 9px 9px;font:inherit;cursor:pointer;color:var(--ink2);white-space:nowrap}
#tabs button:hover{color:var(--ink);background:var(--hl)}
#tabs button[aria-selected="true"]{color:var(--ink);border-bottom-color:var(--ink);font-weight:600}
#tabs .ph{color:var(--muted);font-weight:400}
.grp{display:flex;align-items:center;gap:6px;color:var(--ink2);white-space:nowrap}
.seg{display:inline-flex;border:1px solid var(--axis);border-radius:6px;overflow:hidden;flex:none}
.seg button{border:0;background:transparent;padding:5px 10px;font:inherit;cursor:pointer;color:var(--ink2);white-space:nowrap}
.seg button+button{border-left:1px solid var(--axis)}
.seg button[aria-pressed="true"]{background:var(--ink);color:#fff}
.btn{border:1px solid var(--axis);background:transparent;border-radius:6px;padding:5px 10px;font:inherit;cursor:pointer;color:var(--ink2);white-space:nowrap}
.btn:hover,.seg button:hover{background:var(--hl);color:var(--ink)}
.seg button[aria-pressed="true"]:hover{background:var(--ink);color:#fff}
#sw{position:relative;margin:7px 0 7px auto}
#q{width:230px;padding:5px 8px;border:1px solid var(--axis);border-radius:6px;font:inherit;background:#fff}
#q:focus{outline:2px solid var(--accent);outline-offset:-1px}
#ac{position:absolute;top:calc(100% + 3px);right:0;z-index:30;background:#fff;border:1px solid var(--axis);border-radius:6px;box-shadow:0 6px 18px rgba(0,0,0,.12);max-height:360px;overflow:auto;display:none;min-width:340px}
#ac div{padding:5px 9px;cursor:pointer;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
#ac div.on,#ac div:hover{background:var(--hl)}
#ac b{font-weight:600}
#ac .m{color:var(--muted)}
main{flex:1;display:flex;min-height:0}
#stage{flex:1;display:flex;flex-direction:column;min-width:0}
.pane{flex:1;display:none;flex-direction:column;min-height:0}
.pane.on{display:flex}
.bar{display:flex;flex-wrap:wrap;align-items:center;gap:6px 14px;padding:6px 10px;border-bottom:1px solid var(--grid);background:var(--surface);color:var(--ink2)}
.bars{border-bottom:1px solid var(--grid);background:var(--surface)}
.bars .bar{border-bottom:0}
.bars .bar+.bar{padding-top:0}
.bar .seg button{padding:3px 9px}
.bar .btn{padding:3px 9px}
.bar select,.bar input[type=number]{font:inherit;padding:2px 4px;border:1px solid var(--axis);border-radius:5px;background:#fff;color:var(--ink)}
.rng{display:inline-flex;align-items:center;gap:5px;white-space:nowrap}
.rng input{width:84px;accent-color:#52514e;margin:0}
.rng output{display:inline-block;min-width:26px;color:var(--ink);font-variant-numeric:tabular-nums}
.wrap{flex:1;position:relative;min-height:0;background:var(--surface);overflow:hidden}
.wrap canvas{position:absolute;inset:0;width:100%;height:100%;display:block;cursor:grab;touch-action:none}
.wrap canvas.drag{cursor:grabbing}
.wrap canvas.onnode{cursor:pointer}
.tip{position:absolute;pointer-events:none;background:#fff;border:1px solid var(--ring);border-radius:6px;padding:5px 8px;box-shadow:0 2px 10px rgba(0,0,0,.14);display:none;max-width:340px;z-index:5}
.tip b{font-size:13px}
.tip .m{color:var(--ink2)}
.status{position:absolute;right:10px;bottom:5px;max-width:calc(100% - 20px);color:var(--ink2);font-size:12px;pointer-events:none;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;background:rgba(252,252,251,.88);border-radius:4px;padding:1px 6px}
.status:empty{display:none}
.info{position:absolute;left:10px;top:10px;max-width:min(470px,calc(100% - 20px));background:rgba(252,252,251,.94);border:1px solid var(--ring);border-radius:8px;padding:6px 9px;z-index:4;color:var(--ink2);pointer-events:none}
.info.none{display:none}
.info b{color:var(--ink)}
.info .ky{margin-top:3px;font-size:12px;color:var(--muted)}
.info .ky span.it{white-space:nowrap;margin-right:9px}
.info .ictl{pointer-events:auto;display:flex;flex-wrap:wrap;align-items:center;gap:5px 8px;margin:0 0 6px;padding:0 0 6px;border-bottom:1px solid var(--grid)}
.info .ictl select{font:inherit;padding:2px 4px;border:1px solid var(--axis);border-radius:5px;background:#fff;color:var(--ink);max-width:290px}
.info .ictl .btn{padding:2px 8px}
.info .ictl label{display:flex;align-items:center;gap:4px;white-space:nowrap}
.msg{position:absolute;inset:0;display:none;align-items:center;justify-content:center;text-align:center;padding:40px 15%;color:var(--ink2);font-size:14px;pointer-events:none}
.msg.on{display:flex}
.key{display:inline-block;width:16px;height:0;border-top:3px solid;vertical-align:middle;margin:0 3px 0 0}
.keyd{display:inline-block;width:16px;height:0;border-top:2px dashed;vertical-align:middle;margin:0 3px 0 0}
#legend{position:absolute;left:10px;top:10px;max-height:calc(100% - 46px);width:270px;display:flex;flex-direction:column;background:rgba(252,252,251,.95);border:1px solid var(--ring);border-radius:8px;z-index:4}
#legend .hd{display:flex;align-items:center;justify-content:space-between;padding:6px 8px;border-bottom:1px solid var(--grid);font-weight:600}
#legend .hd button{border:0;background:transparent;cursor:pointer;color:var(--ink2);font:inherit;padding:0 4px}
#lgbody{overflow:auto;padding:4px 0}
#legend.closed #lgbody,#legend.closed #armkey{display:none}
#armkey{padding:6px 8px;border-bottom:1px solid var(--grid);display:none;color:var(--ink2)}
.li{display:flex;align-items:center;gap:7px;padding:2px 8px;cursor:pointer;white-space:nowrap}
.li:hover{background:var(--hl)}
.li.on{background:#dde8f8}
.li .t{overflow:hidden;text-overflow:ellipsis;flex:1;color:var(--ink)}
.li .n{color:var(--muted);font-variant-numeric:tabular-nums}
.sw{display:inline-block;width:10px;height:10px;border-radius:50%;flex:none}
aside{width:440px;flex:none;border-left:1px solid var(--grid);overflow:auto;background:var(--surface);padding:12px 16px 30px}
aside h2{font-size:20px;margin:0 0 2px}
aside h3{font-size:13px;margin:16px 0 5px;color:var(--ink);font-weight:600;border-bottom:1px solid var(--grid);padding-bottom:3px}
aside .nm{color:var(--ink2);font-size:14px}
aside .fn{color:var(--ink2);margin:6px 0}
.note{color:var(--muted);font-size:12px}
aside p{margin:6px 0}
table{border-collapse:collapse;width:100%;font-variant-numeric:tabular-nums}
th{text-align:left;font-weight:600;color:var(--ink2);font-size:12px;border-bottom:1px solid var(--grid);padding:3px 4px}
td{padding:2px 4px;border-bottom:1px solid #f0efea;vertical-align:top}
td.r,th.r{text-align:right}
tr.ck{cursor:pointer}
tr.ck:hover td{background:var(--hl)}
.k{display:inline-block;width:9px;height:9px;border-radius:2px;margin-right:4px;vertical-align:baseline}
.bd{display:inline-block;font-size:11px;line-height:15px;padding:0 5px;border-radius:9px;border:1px solid var(--axis);color:var(--ink2);margin:1px 2px 1px 0;white-space:nowrap}
table.pt td:first-child{white-space:nowrap}
.bd.nov{border-color:#6250d6;color:#4a3aa7}
.bd.loc{border-color:#eda100;color:#7a5200}
.bd.rt{border-color:#d03b3b;color:#a02020}
.bd.lit{border-color:#2a78d6;color:#104281;background:#eef4fb}
.bd.lit.lit-contradicted{border-color:#d03b3b;color:#a02020;background:#fbeeee}
.bd.lit.lit-unverified{border-color:#b98a2e;color:#6b4d0f;background:#fbf4e6;border-style:dashed}
.bd.lit.lit-st-unchecked,.bd.lit.lit-st-not_checkable{border-style:dashed}
a,.lk{color:var(--accent);cursor:pointer;text-decoration:none}
a:hover,.lk:hover{text-decoration:underline}
.mcard{background:#f4f6f9;border:1px solid var(--grid);border-radius:8px;padding:8px 10px;margin:0 0 10px}
.mcard .row{margin:3px 0}
.mcard .lbl{color:var(--muted);font-size:12px}
.al{color:#8a4600;font-size:12px;line-height:1.3;margin:1px 0 0}
.fnote{color:var(--muted);font-size:12px;line-height:1.3;margin:1px 0 0}
.alc{color:#8a4600;white-space:nowrap}
.bd.warn{border-color:#c77800;color:#7a4300;background:#fdf3e4}
.cnt{font-weight:400;color:var(--muted);font-size:12px}
.tsel{font:inherit;padding:2px 4px;border:1px solid var(--axis);border-radius:5px;background:#fff;color:var(--ink)}
.helpwrap{flex:1;overflow:auto;padding:14px 28px 40px;background:var(--surface)}
.howto{max-width:880px}
.howto h3{font-size:15px;margin:14px 0 4px}
.howto h4{margin:12px 0 3px;font-size:13px}
.howto p,.howto li{color:var(--ink2);margin:3px 0}
.howto ul{padding-left:18px;margin:4px 0}
.dh4{font-size:12px;margin:10px 0 3px;color:var(--ink);font-weight:600}
.dkey{position:absolute;right:10px;top:10px;max-width:min(600px,calc(100% - 320px));background:rgba(252,252,251,.88);border:1px solid var(--ring);border-radius:8px;padding:4px 8px;z-index:4;color:var(--ink2);font-size:12px;display:none}
.dkey span.it{white-space:nowrap;margin-right:9px}
.dkey .dkx{float:right;border:0;background:transparent;cursor:pointer;color:var(--ink2);font:inherit;padding:0 2px 0 8px}
.dkey.closed .dkb{display:none}
.dr{padding:4px 2px 5px;border-bottom:1px solid #f0efea;cursor:pointer}
.dr:hover{background:var(--hl)}
.dr .dtx{color:var(--ink2);font-size:12px;line-height:1.3;margin:1px 0 0}
.dr .dx{display:none;color:var(--ink2);font-size:12px;line-height:1.35;margin:3px 0 0 4px;padding:3px 0 2px 7px;border-left:2px solid #c9c1ee}
.dr.open .dx{display:block}
.dr .dx div{margin:1px 0}
.gb{display:inline-block;min-width:17px;text-align:center;font-size:11px;font-weight:700;line-height:15px;border-radius:4px;margin-right:3px;border:1px solid #5b3fc4}
.gb.g0{background:#5b3fc4;color:#fff}
.gb.g1{background:#ece8fb;color:#3a2a8a}
.gb.g2{background:#fff;color:#5b3fc4;border-style:dashed}
.sgn{font-size:11px;padding:0 5px;border-radius:8px;border:1px solid var(--axis);color:var(--ink2);white-space:nowrap;margin-left:3px}
.dsel{font-weight:700}
.dnm{color:var(--muted)}
@media (max-width:1280px){#tabs button{padding:12px 6px 9px}#q{width:165px}#ac{min-width:300px}header{gap:4px 10px}}
</style>
</head>
<body>
<header>
  <h1>Tahoe-100M gene map</h1>
  <nav id="tabs" role="tablist" aria-label="Displays">
    <button role="tab" data-tab="nodal" aria-selected="true" title="t-SNE of 1 - |cos|: genes that respond to the same drugs sit together, also when they move in opposite directions">Nodal map</button>
    <button role="tab" data-tab="signed" aria-selected="false" title="t-SNE of 1 - cos: genes that move in opposite directions are pushed apart">Signed vector map</button>
    <button role="tab" data-tab="tour" aria-selected="false" title="The gene vectors in their full vector space, seen through a slowly rotating 2D window (a grand tour), or any two of its axes" id="tourtab">Vector-space tour</button>
    <button role="tab" data-tab="nbr" aria-selected="false" title="A live force simulation of the selected gene, its partners and their partners"><span class="ph">Physics:</span> neighbourhood</button>
    <button role="tab" data-tab="mod" aria-selected="false" title="A live force simulation of one module: its genes and the graph edges among them"><span class="ph">Physics:</span> module</button>
    <button role="tab" data-tab="all" aria-selected="false" title="A live force simulation of every gene on the map, started from the nodal-map positions"><span class="ph">Physics:</span> all genes</button>
    <button role="tab" data-tab="help" aria-selected="false">How to read this</button>
  </nav>
  <div class="grp" id="sw"><input id="q" type="search" placeholder="Search a gene (symbol, alias, name)" autocomplete="off" spellcheck="false" aria-label="Search a gene"><div id="ac" role="listbox"></div></div>
</header>
<main>
  <section id="stage">
    <div class="pane on" id="pane-map" role="tabpanel">
      <div class="bar">
        <div class="grp">Colour <span class="seg"><button id="c0" aria-pressed="true">Module</button><button id="c1" aria-pressed="false">Arm (+ / &minus;)</button></span></div>
        <button class="btn" id="fitb" title="Show every gene">Reset view</button>
        <label class="rng" id="sprl" title="0 = the t-SNE layout; 1 = every module moved apart as a block, keeping its own arrangement, to a place set by how far apart the modules are in the full vector space">Spread <input type="range" id="spr" min="0" max="100" step="1" value="0" aria-label="Spread the modules apart"><output id="spro">0.00</output></label>
        <button class="btn" id="sprb" title="Animate between the t-SNE layout (0) and the spread layout (1)">Spread &#8644;</button>
        <label class="grp" id="dirml" title="Draw the selected gene's probable-direction arrows (direction stage) to and from the genes on the map: the rows its side-panel lists show"><input type="checkbox" id="dirm" checked> Direction arrows</label>
        <span class="note" id="mapnote"></span>
      </div>
      <div class="wrap" id="mapwrap">
        <canvas id="cv"></canvas>
        <div id="legend"><div class="hd"><span id="lgtitle">Modules</span><button id="lgx" title="Collapse / expand">&#8722;</button></div><div id="armkey"></div><div id="lgbody"></div></div>
        <div id="tip" class="tip"></div>
        <div id="dirkey" class="dkey"></div>
        <div id="status" class="status"></div>
      </div>
    </div>
    <div class="pane" id="pane-tour" role="tabpanel"></div>
    <div class="pane" id="pane-nbr" role="tabpanel"></div>
    <div class="pane" id="pane-mod" role="tabpanel"></div>
    <div class="pane" id="pane-all" role="tabpanel"></div>
    <div class="pane" id="pane-help" role="tabpanel"><div class="helpwrap"><div id="helptext" class="howto"></div></div></div>
  </section>
  <aside id="panel"></aside>
</main>
<noscript><p style="padding:20px">This map needs JavaScript.</p></noscript>
<script id="tm-data" type="application/json">__DATA__</script>
<script>
"use strict";
(function () {
const D = JSON.parse(document.getElementById("tm-data").textContent);
const N = D.n, NA = D.sym.length, PAL = D.palette, GREY = "#bdbcb6";
const ARMC = {"+": "#eb6834", "-": "#2a78d6"};
const WITH = "#0ca30c", OPP = "#d03b3b", SURF = "#fcfcfb", INK = "#0b0b0b", INK2 = "#52514e";
const WITH_T = "#05600a", OPP_T = "#8f1d1d";
const EVS = ["none", "one", "both"];
const FF = "system-ui,-apple-system,sans-serif";
const $ = id => document.getElementById(id);
const esc = s => String(s == null ? "" : s).replace(/[&<>"']/g, c => ({"&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;"}[c]));
const has = a => a && a.length > 0;
const MODS = new Map(D.mods.map(m => [m.id, m]));
const modColour = m => m > 0 ? PAL[(m - 1) % PAL.length] : GREY;
const isMap = t => t === "nodal" || t === "signed";

// ---------------------------------------------------------------- shared by every tab: the selection and the highlighted module
let sel = -1, hlMod = -1, P = [], pset = new Set(), focus = "gene", active = "nodal", mapSelPending = false, selGen = 0;
const PHYS = {};                                   // the three physics tabs, by key
let TOUR = null;                                   // the vector-space tour tab
function partnersOf(i) {
  const a = (i >= 0 && i < N) ? (D.rel[i] || []) : [], out = [];
  for (let t = 0; t + 3 < a.length; t += 4) {
    const f = a[t + 3];
    out.push({j: a[t], cos: a[t + 1] / 100, fdr: a[t + 2] < 0 ? null : a[t + 2] / 100, ev: f & 3,
      locus: !!(f & 4), rt: !!(f & 8), group: !!(f & 16), known: !!(f & 32), novel: !!(f & 64),
      string: (Math.floor(f / 256) % 128) * 10, pw: Math.floor(f / 32768) - 1});
  }
  return out;
}

// ---------------------------------------------------------------- one frame loop, for the visible tab only
let pendingFrame = false;
function req() { if (!pendingFrame) { pendingFrame = true; requestAnimationFrame(loop); } }
function loop(now) {
  pendingFrame = false;
  let more = false;
  if (isMap(active)) more = mapFrame(now);
  else if (active === "tour" && TOUR) more = TOUR.frame(now);
  else if (PHYS[active]) more = PHYS[active].frame(now);
  if (more) req();
}

// ---------------------------------------------------------------- drawing helpers
// Points are written straight into one pixel buffer (a single putImageData per frame): no canvas call per point,
// so 16k+ points stay fast also where the canvas is not GPU-accelerated. Lines, rings and labels go on top.
const LITTLE = new Uint8Array(new Uint32Array([1]).buffer)[0] === 1;
const pack = (r, g, b) => LITTLE ? (((255 << 24) | (b << 16) | (g << 8) | r) >>> 0) : (((r << 24) | (g << 16) | (b << 8) | 255) >>> 0);
const rgbOf = hex => { const v = parseInt(hex.slice(1), 16); return [(v >> 16) & 255, (v >> 8) & 255, v & 255]; };
const SURF_RGB = rgbOf(SURF), SURF_PACKED = pack(SURF_RGB[0], SURF_RGB[1], SURF_RGB[2]);
function PointLayer(cv, ctx) {
  let img = null, buf8 = null, buf32 = null, mask = null;
  function getMask(R, Wd) {
    if (mask && mask.R === R && mask.Wd === Wd) return mask;
    const e = Math.ceil(R + 0.5), m = {R: R, Wd: Wd, e: e, full: [], fdx: [], fdy: [], part: [], cov: [], pdx: [], pdy: []};
    for (let dy = -e; dy <= e; dy++) for (let dx = -e; dx <= e; dx++) {
      const c = Math.max(0, Math.min(1, R + 0.5 - Math.hypot(dx, dy)));
      if (c >= 0.98) { m.full.push(dy * Wd + dx); m.fdx.push(dx); m.fdy.push(dy); }
      else if (c > 0.04) { m.part.push(dy * Wd + dx); m.cov.push(c); m.pdx.push(dx); m.pdy.push(dy); }
    }
    for (const key of ["full", "fdx", "fdy", "part", "pdx", "pdy"]) m[key] = Int32Array.from(m[key]);
    m.cov = Float32Array.from(m.cov);
    return (mask = m);
  }
  // XA, YA: world coordinates; screen = (XA * k + tx, ys * YA * k + ty) in CSS pixels; groups: [{c, a, idx}]
  return function (XA, YA, ys, groups, kk, txx, tyy, dpr, R) {
    const Wd = cv.width, Hd = cv.height;
    if (!img || img.width !== Wd || img.height !== Hd) { img = ctx.createImageData(Wd, Hd); buf8 = img.data; buf32 = new Uint32Array(buf8.buffer); }
    buf32.fill(SURF_PACKED);
    if (groups) {
      const k = kk * dpr, ky = ys * k, tx = txx * dpr, ty = tyy * dpr, M = getMask(R * dpr, Wd), e = M.e;
      const full = M.full, part = M.part, cov = M.cov, fdx = M.fdx, fdy = M.fdy, pdx = M.pdx, pdy = M.pdy;
      const nf = full.length, np = part.length;
      for (const g of groups) {
        const a = g.a * 0.92, rgb = rgbOf(g.c);
        const cr = rgb[0] * a + SURF_RGB[0] * (1 - a), cg = rgb[1] * a + SURF_RGB[1] * (1 - a), cb = rgb[2] * a + SURF_RGB[2] * (1 - a);
        const solid = pack(Math.round(cr), Math.round(cg), Math.round(cb)), idx = g.idx;
        for (let j = 0; j < idx.length; j++) {
          const i = idx[j], X = Math.round(XA[i] * k + tx), Y = Math.round(YA[i] * ky + ty);
          if (X < -e || Y < -e || X >= Wd + e || Y >= Hd + e) continue;
          if (X >= e && Y >= e && X < Wd - e && Y < Hd - e) {
            const base = Y * Wd + X;
            for (let t = 0; t < nf; t++) buf32[base + full[t]] = solid;
            for (let t = 0; t < np; t++) {
              const o = (base + part[t]) << 2, c = cov[t];
              buf8[o] += (cr - buf8[o]) * c; buf8[o + 1] += (cg - buf8[o + 1]) * c; buf8[o + 2] += (cb - buf8[o + 2]) * c;
            }
          } else {                                            // near the edge: clip pixel by pixel
            for (let t = 0; t < nf; t++) {
              const x = X + fdx[t], y = Y + fdy[t];
              if (x >= 0 && y >= 0 && x < Wd && y < Hd) buf32[y * Wd + x] = solid;
            }
            for (let t = 0; t < np; t++) {
              const x = X + pdx[t], y = Y + pdy[t];
              if (x < 0 || y < 0 || x >= Wd || y >= Hd) continue;
              const o = (y * Wd + x) << 2, c = cov[t];
              buf8[o] += (cr - buf8[o]) * c; buf8[o + 1] += (cg - buf8[o + 1]) * c; buf8[o + 2] += (cb - buf8[o + 2]) * c;
            }
          }
        }
      }
    }
    ctx.putImageData(img, 0, 0);
  };
}
function halo(ctx, text, x, y, font, colour) {
  ctx.font = font; ctx.lineJoin = "round"; ctx.lineWidth = 3.5; ctx.strokeStyle = "rgba(252,252,251,.92)";
  ctx.strokeText(text, x, y); ctx.fillStyle = colour || INK; ctx.fillText(text, x, y);
}
// labels that would overlap one already drawn are skipped
function Labeler(ctx) {
  const placed = [];
  return function (text, x, y, font, colour, hgt) {
    ctx.font = font;
    const w = ctx.measureText(text).width, b = [x - 1, y - hgt / 2, x + w + 1, y + hgt / 2];
    for (const q of placed) if (b[0] < q[2] && b[2] > q[0] && b[1] < q[3] && b[3] > q[1]) return false;
    placed.push(b); halo(ctx, text, x, y, font, colour);
    return true;
  };
}
function quant(sorted, q) { return sorted[Math.min(sorted.length - 1, Math.max(0, Math.round(q * (sorted.length - 1))))]; }

// ---------------------------------------------------------------- probable direction (direction stage; D.dir)
// Rows are direction_view's display rows in its ORDER; their texts are its own (templates: \u0001 = the row's source
// text, \u0002 = its target name), so the page words them exactly as the vault and the look-ups do.
const DR = D.dir || {ok: false};
const HAS_DIR = !!DR.ok;
const DIRC = "#5b3fc4", DIRC_T = "#3a2a8a";        // arrows, and the ring of genes added for their direction rows
const DW = DR.w || 10, NDR = HAS_DIR ? Math.floor(DR.r.length / DW) : 0;
const ALERT_S = "⚠", ARROW_S = "→";
const fillT = (t, S, T) => (t.indexOf("\u0001") < 0 && t.indexOf("\u0002") < 0) ? t : t.split("\u0002").join(T).split("\u0001").join(S);
const fmtN = v => String(v).replace(/\B(?=(\d{3})+(?!\d))/g, ",");
let DX = null;                                     // per entry: its upstream, downstream and cells rows, in ORDER
function dirIndex() {
  if (DX) return DX;
  const up = new Map(), dn = new Map(), ce = new Map(), more = new Map();
  const push = (m, e, k) => { let a = m.get(e); if (!a) { a = []; m.set(e, a); } a.push(k); };
  for (let k = 0; k < NDR; k++) {
    const b = k * DW, kind = DR.r[b] & 15, cells = !!DR.sens[kind], ss = DR.ss[DR.r[b + 1]];
    for (let t = 2; t < ss.length; t += 2) if (ss[t] >= 0) push(cells ? ce : dn, ss[t], k);
    if (!cells && DR.r[b + 3] >= 0) push(up, DR.r[b + 3], k);
  }
  const cm = DR.cmore || [];
  for (let t = 0; t + 5 < cm.length; t += 6) more.set(cm[t], cm.slice(t + 1, t + 6));
  return (DX = {up: up, dn: dn, ce: ce, more: more});
}
const dirRowsOf = (i, which) => HAS_DIR ? (dirIndex()[which].get(i) || []) : [];
const dirAlert = k => (DR.r[k * DW] & 256) !== 0;
// a row whose target is a gene's drug response (direction_view.RESPONSE): its sign is strengthens / weakens, drawn
// with its own heads (an open head, a double bar); headSign: the sign the ArrowBatch draws (+-2 for those rows)
const dirResp = k => !!(DR.resp && DR.resp[DR.r[k * DW] & 15]);
const headSign = a => a.sign * (dirResp(a.k) ? 2 : 1);
function dirRow(k) {
  const r = DR.r, b = k * DW, kgs = r[b], ss = DR.ss[r[b + 1]];
  const kind = kgs & 15, gi = (kgs >> 4) & 3, sign = ((kgs >> 6) & 3) - 1, cells = !!DR.sens[kind];
  const S = DR.nm[ss[0]], tgt = DR.nm[r[b + 2]], T = cells && tgt.indexOf("cells under ") === 0 ? tgt.slice(12) : tgt;
  const tx = id => id >= 0 ? fillT(DR.tx[id], S, T) : "";
  const src = [];
  for (let t = 1; t + 1 < ss.length; t += 2) src.push({name: DR.nm[ss[t]], e: ss[t + 1]});
  return {k: k, kind: kind, gi: gi, grade: DR.grades[gi] || "?", sign: sign, cells: cells, S: S, src: src, tgt: tgt,
    te: cells ? -1 : r[b + 3], dd: cells ? r[b + 3] : -1, signText: tx(r[b + 4]), kindText: tx(r[b + 5]), q: tx(r[b + 6]),
    alShort: tx(r[b + 7]), alLong: tx(r[b + 8]), reading: tx(r[b + 9]), alert: (kgs & 256) !== 0};
}
// direction_view.edge_line(row): 'TP53 → CDKN1A  [A]  TP53 activity raises ... (mutation: response; q 0.025)  ⚠ ...'
const dirLine = w => w.S + " " + ARROW_S + " " + w.tgt + "  [" + w.grade + "]  " + w.signText + " (" + DR.kshort[w.kind] + "; " + w.q + ")" + (w.alShort ? "  " + w.alShort : "");
// direction_view.cap (rule 1): the n strongest, and any of the n strongest without an alert that come after them
function dirCap(list, n) {
  const shown = [];
  let clean = 0, more = 0, moreAl = 0;
  for (let t = 0; t < list.length; t++) {
    const al = dirAlert(list[t]);
    if (t < n || (!al && clean < n)) shown.push(list[t]); else { more++; if (al) moreAl++; }
    if (!al) clean++;
  }
  return {shown: shown, more: more, moreAl: moreAl};
}
// direction_view.more_text / counts_text (extra: rows counted but not embedded: [n, with an alert, A, B, C])
function dirMoreText(n, nAl, what) {
  if (n <= 0) return "";
  const w = n === 1 && /s$/.test(what) && !/ss$/.test(what) ? what.slice(0, -1) : what;
  return fmtN(n) + " more " + w + (nAl ? " (" + fmtN(nAl) + " of them with an alert " + ALERT_S + ")" : "");
}
function dirCountsText(list, what, extra) {
  const g = [0, 0, 0];
  let n = list.length, k = 0;
  for (const r of list) { g[(DR.r[r * DW] >> 4) & 3]++; if (dirAlert(r)) k++; }
  if (extra) { n += extra[0]; k += extra[1]; g[0] += extra[2]; g[1] += extra[3]; g[2] += extra[4]; }
  if (!n) return "none";
  const w = n === 1 && /s$/.test(what) ? what.slice(0, -1) : what;
  return fmtN(n) + " " + w + (k ? ", " + fmtN(k) + " of them with an alert " + ALERT_S : "") + "; grade " + DR.grades.map((x, t) => x + " " + fmtN(g[t])).join(", ");
}
// the genes a row links to the gene i: the sources of an upstream row, the target of a downstream row
function dirOthers(w, i) {
  if (w.cells) return [];
  if (w.te === i) return w.src.map(s => s.e).filter(e => e >= 0 && e !== i);
  return w.te >= 0 && w.te !== i ? [w.te] : [];
}
// arrows from (x0, y0) to (x1, y1), ending r1 before the target's centre: the grade sets the line (A thick, B thin,
// C dashed), the sign the head (raises: a filled head; lowers: a bar, as an inhibition; not inferred: an open circle;
// for a drug response, sign +-2: strengthens an open head, weakens a double bar).
// Collected, then drawn grouped by style: the dimmed ones first and plain, the selected gene's on top with a pale
// casing that lifts them off the springs (one stroke per arrow rasterizes faster than one path of thousands).
const AW = [2.4, 1.6, 1.15], AA = [0.95, 0.85, 0.75];
function ArrowBatch() {
  const L = [];
  return {
    add: (x0, y0, x1, y1, r0, r1, gi, sign, dim, off) => {
      let dx = x1 - x0, dy = y1 - y0;
      const len = Math.hypot(dx, dy);
      gi = gi >= 0 && gi < 3 ? gi : 2;
      if (!(len > r0 + r1 + 6)) return;
      dx /= len; dy /= len;
      const px = -dy * (off || 0), py = dx * (off || 0);
      L.push({ax: x0 + dx * r0 + px, ay: y0 + dy * r0 + py, bx: x1 - dx * r1 + px, by: y1 - dy * r1 + py, dx: dx, dy: dy, gi: gi, sign: sign, dim: dim ? 1 : 0});
    },
    draw: g => {
      L.sort((p, q) => (q.dim - p.dim) || (q.gi - p.gi));
      g.lineCap = "butt";
      let style = -1;
      for (const a of L) {
        const resp = Math.abs(a.sign) === 2, sg = Math.sign(a.sign);
        const w = AW[a.gi], hl = 6.5 + 1.2 * w, al = AA[a.gi] * (a.dim ? 0.6 : 1), back = sg > 0 ? hl * 0.85 : sg < 0 ? 0 : 6;
        const ex = a.bx - a.dx * back, ey = a.by - a.dy * back;
        if (style !== 3 * a.dim + a.gi) { style = 3 * a.dim + a.gi; g.setLineDash(a.gi === 2 ? [4, 3] : []); }
        if (!a.dim) {
          g.strokeStyle = SURF; g.lineWidth = w + 2.6; g.globalAlpha = al * 0.85;
          g.beginPath(); g.moveTo(a.ax, a.ay); g.lineTo(ex, ey); g.stroke();
        }
        g.strokeStyle = DIRC; g.fillStyle = DIRC; g.lineWidth = w; g.globalAlpha = al;
        g.beginPath(); g.moveTo(a.ax, a.ay); g.lineTo(ex, ey); g.stroke();
        const bx = a.bx, by = a.by, dx = a.dx, dy = a.dy;
        if (sg > 0) {
          g.beginPath(); g.moveTo(bx, by); g.lineTo(bx - dx * hl - dy * hl * 0.45, by - dy * hl + dx * hl * 0.45);
          g.lineTo(bx - dx * hl + dy * hl * 0.45, by - dy * hl - dx * hl * 0.45); g.closePath();
          if (resp) { g.setLineDash([]); style = -1; g.fillStyle = SURF; g.fill(); g.lineWidth = 1.5; g.stroke(); }
          else g.fill();
        } else {
          if (a.gi === 2) { g.setLineDash([]); style = -1; }
          if (sg < 0) {
            g.lineWidth = w + 0.9; g.beginPath(); g.moveTo(bx - dy * 5.5, by + dx * 5.5); g.lineTo(bx + dy * 5.5, by - dx * 5.5);
            if (resp) { g.moveTo(bx - dx * 4.5 - dy * 5.5, by - dy * 4.5 + dx * 5.5); g.lineTo(bx - dx * 4.5 + dy * 5.5, by - dy * 4.5 - dx * 5.5); }
            g.stroke();
          }
          else { g.lineWidth = 1.4; g.beginPath(); g.arc(bx - dx * 3, by - dy * 3, 3, 0, 2 * Math.PI); g.stroke(); }
        }
      }
      g.setLineDash([]); g.globalAlpha = 1;
    }};
}
// the legend of the arrows (small inline drawings)
function dirKey() {
  const svg = (inner, w) => "<svg width='" + (w || 26) + "' height='10' style='vertical-align:middle;margin-right:3px'>" + inner + "</svg>";
  const ln = (dash, wd) => "<line x1='1' y1='5' x2='19' y2='5' stroke='" + DIRC + "' stroke-width='" + wd + "'" + (dash ? " stroke-dasharray='4 3'" : "") + "/>";
  const it = s => "<span class='it'>" + s + "</span> ";
  return it(svg(ln(0, 1.6) + "<path d='M25 5 L17 1.4 L17 8.6 Z' fill='" + DIRC + "'/>") + "raises (a level, the cells)") +
    it(svg(ln(0, 1.6) + "<line x1='20' y1='0' x2='20' y2='10' stroke='" + DIRC + "' stroke-width='2.5'/>") + "lowers") +
    it(svg(ln(0, 1.6) + "<path d='M25 5 L17 1.4 L17 8.6 Z' fill='#fff' stroke='" + DIRC + "' stroke-width='1.3'/>") + "strengthens a drug response") +
    it(svg(ln(0, 1.6) + "<line x1='16' y1='0' x2='16' y2='10' stroke='" + DIRC + "' stroke-width='2.5'/><line x1='21' y1='0' x2='21' y2='10' stroke='" + DIRC + "' stroke-width='2.5'/>") + "weakens it") +
    it(svg(ln(0, 1.6) + "<circle cx='22' cy='5' r='3' fill='none' stroke='" + DIRC + "' stroke-width='1.4'/>") + "sign not inferred") +
    it(svg(ln(0, 2.4), 21) + "A " + svg(ln(0, 1.6), 21) + "B " + svg(ln(1, 1.15), 21) + "C");
}

// ================================================================ tabs 1-2: the two t-SNE maps (one canvas, two layouts)
function norm(xa, ya) {
  const n = xa.length, X = new Float32Array(n), Y = new Float32Array(n);
  if (!n) return {x: X, y: Y};
  const sx = Float64Array.from(xa).sort(), sy = Float64Array.from(ya).sort();
  const x0 = quant(sx, .005), x1 = quant(sx, .995), y0 = quant(sy, .005), y1 = quant(sy, .995);
  const cx = (x0 + x1) / 2, cy = (y0 + y1) / 2, s = Math.max(x1 - x0, y1 - y0, 1e-9) / 2;
  for (let i = 0; i < n; i++) { X[i] = (xa[i] - cx) / s; Y[i] = (ya[i] - cy) / s; }
  return {x: X, y: Y};
}
const LAY = [norm(D.x, D.y), norm(D.xs, D.ys)];
// the spread layouts (graph xm, ym / xsm, ysm): every module moved apart as a block; the Spread slider mixes them in
const HAS_SPREAD = !!(has(D.xm) && D.xm.length === N && has(D.xsm) && D.xsm.length === N);
const LAYM = HAS_SPREAD ? [norm(D.xm, D.ym), norm(D.xsm, D.ysm)] : LAY;
let spread = 0;
const MIX = [0, 1].map(() => ({x: new Float32Array(N), y: new Float32Array(N), s: -1}));
function lay(l) {                                  // layout l at the current spread
  const t = MIX[l];
  if (t.s !== spread) {
    const A = LAY[l], B = LAYM[l], s = spread;
    for (let i = 0; i < N; i++) { t.x[i] = A.x[i] + (B.x[i] - A.x[i]) * s; t.y[i] = A.y[i] + (B.y[i] - A.y[i]) * s; }
    t.s = spread;
  }
  return t;
}
const PX = new Float32Array(N), PY = new Float32Array(N);
PX.set(LAY[0].x); PY.set(LAY[0].y);
let layout = 0, anim = null;
const cv = $("cv"), ctx = cv.getContext("2d"), wrap = $("mapwrap"), tip = $("tip"), mapLayer = PointLayer(cv, ctx);

// view (screen = world * k + t; y up)
let W = 1, H = 1, DPR = 1, K0 = 1, mapSized = false;
const V = {k: 1, tx: 0, ty: 0}, T = {k: 1, tx: 0, ty: 0};
const legendW = () => $("legend").classList.contains("closed") ? 0 : 290;
function fitTarget() {
  const lw = W > 700 ? legendW() : 0, w = W - lw;
  K0 = Math.max(10, Math.min(w, H) / 2 * 0.9);
  return {k: K0, tx: lw + w / 2, ty: H / 2};
}
function fit(now) { Object.assign(T, fitTarget()); if (now) Object.assign(V, T); req(); }
function resize() {
  const r = wrap.getBoundingClientRect();
  if (r.width < 2 || r.height < 2) return;                 // the map tab is hidden
  DPR = window.devicePixelRatio || 1;
  W = r.width; H = r.height;
  cv.width = Math.round(W * DPR); cv.height = Math.round(H * DPR);
  if (!mapSized) {
    mapSized = true; fit(true);
    if (sel >= 0 && sel < N) { centreOn(sel, layout); Object.assign(V, T); mapSelPending = false; }
  } else { const f = fitTarget(); K0 = f.k; }
  req();
}
const sx = i => PX[i] * V.k + V.tx, sy = i => -PY[i] * V.k + V.ty;

let colourMode = 0, hover = -1, groups = null;
function colourOf(i) {
  if (colourMode === 1) return ARMC[D.arm[i]] || GREY;
  return modColour(D.mod[i]);
}
function regroup() {
  const g = new Map();
  const selOn = sel >= 0 && sel < N;
  for (let i = 0; i < N; i++) {
    let a = 1;
    if (hlMod >= 0 && D.mod[i] !== hlMod) a = 0.13;
    if (selOn && i !== sel && !pset.has(i)) a = Math.min(a, 0.4);
    const c = colourOf(i), key = a + c;
    let e = g.get(key);
    if (!e) { e = {c: c, a: a, idx: []}; g.set(key, e); }
    e.idx.push(i);
  }
  groups = [...g.values()].sort((p, q) => (p.a - q.a) || ((q.c === GREY) - (p.c === GREY)));
  for (const e of groups) e.idx = Int32Array.from(e.idx);
  req();
}
const pointR = () => Math.min(5, Math.round(4 * 2 * Math.pow(V.k / K0, 0.3)) / 4);
function ease(t) { return t < .5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2; }
function mapFrame(now) {
  if (!mapSized) resize();
  let more = false;
  if (anim) {
    const t = anim.dur > 0 ? Math.min(1, Math.max(0, (now - anim.t0) / anim.dur)) : 1, e = ease(t), A = anim.A, B = anim.B;
    for (let i = 0; i < N; i++) { PX[i] = A.x[i] + (B.x[i] - A.x[i]) * e; PY[i] = A.y[i] + (B.y[i] - A.y[i]) * e; }
    const f = anim.follow;                       // keep the selected gene where it is on the screen (Spread)
    if (f) {
      T.tx = f.sx - PX[f.i] * T.k; T.ty = f.sy + PY[f.i] * T.k;
      V.tx = f.sx - PX[f.i] * V.k; V.ty = f.sy + PY[f.i] * V.k;
    }
    if (t >= 1) anim = null; else more = true;
  }
  for (const key of ["k", "tx", "ty"]) {
    const d = T[key] - V[key];
    if (Math.abs(d) > (key === "k" ? V.k * 1e-3 : 0.3)) { V[key] += d * 0.28; more = true; } else V[key] = T[key];
  }
  mapDraw();
  return more;
}
function mapDraw() {
  ctx.setTransform(1, 0, 0, 1, 0, 0);
  mapLayer(PX, PY, -1, groups, V.k, V.tx, V.ty, DPR, pointR());
  const r = pointR();
  ctx.globalAlpha = 1;
  ctx.setTransform(DPR, 0, 0, DPR, 0, 0);
  drawModuleLabels();
  if (sel >= 0 && sel < N) drawSelection(r);
  mapKey(sel >= 0 && sel < N ? mapArrowList().length : 0);
  if (hover >= 0 && hover !== sel) {
    ctx.beginPath(); ctx.arc(sx(hover), sy(hover), r + 3, 0, 2 * Math.PI);
    ctx.lineWidth = 1.5; ctx.strokeStyle = INK; ctx.stroke();
  }
}
const nModLabels = 40;
function drawModuleLabels() {
  // one label per module at its centre; on the signed map, where the two arms of a two-armed module sit apart, one
  // label per arm ("M3 +", "M3 −") at the arm's centre
  if (!D.mods.length) return;
  const sum = new Map(), byArm = layout === 1;
  for (let i = 0; i < N; i++) {
    const m = D.mod[i];
    if (m <= 0) continue;
    const md = MODS.get(m), key = byArm && md && md.opp ? m + D.arm[i] : m;
    let s = sum.get(key);
    if (!s) { s = [0, 0, 0]; sum.set(key, s); }
    s[0] += PX[i]; s[1] += PY[i]; s[2]++;
  }
  ctx.textAlign = "center"; ctx.textBaseline = "middle";
  const zoomed = V.k / K0 > 2.2, selOn = sel >= 0 && sel < N;
  for (const m of D.mods) {
    if (hlMod >= 0 && m.id !== hlMod) continue;
    if (hlMod < 0 && !zoomed && m.id > nModLabels) continue;
    const parts = byArm && m.opp ? [[m.id + "+", " +"], [m.id + "-", " −"]] : [[m.id, ""]];
    for (const [key, suffix] of parts) {
      const s = sum.get(key);
      if (!s) continue;
      const X = s[0] / s[2] * V.k + V.tx, Y = -s[1] / s[2] * V.k + V.ty;
      if (X < 0 || Y < 0 || X > W || Y > H) continue;
      // the full label only for the highlighted module; otherwise the module number (muted while a gene is selected)
      let text = hlMod === m.id ? "M" + m.id + suffix + " " + m.label : "M" + m.id + suffix;
      if (text.length > 60) text = text.slice(0, 58) + "…";
      halo(ctx, text, X, Y, "600 11px " + FF, selOn && hlMod !== m.id ? "#898781" : "#2b2b2a");
    }
  }
}
// the maps: the selected gene's probable-direction arrows, for the rows its side-panel lists show (all of them after
// 'show all'), to and from the genes on the map; one arrow per ordered pair (its strongest row)
let mapArrows = null;
function mapArrowsDirty() { mapArrows = null; }
let mapKeyN = -1;
function mapKey(n) {                               // the arrows' legend on the map, while it draws any
  if (n === mapKeyN) return;
  mapKeyN = n;
  const el = $("dirkey");
  el.style.display = n ? "block" : "none";
  if (n) el.innerHTML = "<button class='dkx' title='Collapse / expand the key'>" + (el.classList.contains("closed") ? "+" : "&#8722;") + "</button><span style='color:" + DIRC_T + "'>Probable direction</span>: " + fmtN(n) + " arrow" + (n === 1 ? "" : "s") + " of " + esc(D.sym[sel] || "") +
    "'s side-panel rows to and from genes on the map<div class='dkb'>" + dirKey() + "</div>";
}
$("dirkey").addEventListener("click", e => {          // the key collapses to its first line, out of the arrows' way
  if (!e.target.closest(".dkx")) return;
  const el = $("dirkey");
  el.classList.toggle("closed");
  e.target.innerHTML = el.classList.contains("closed") ? "+" : "&#8722;";
});
function mapArrowList() {
  if (mapArrows) return mapArrows;
  const out = [], seen = new Set();
  if (HAS_DIR && sel >= 0 && $("dirm").checked) {
    const ks = [];
    for (const which of ["up", "dn"]) {
      const rows = dirRowsOf(sel, which);
      for (const k of (dirAll[which] ? rows : dirCap(rows, DR.cap || 8).shown)) ks.push([k, which]);
    }
    ks.sort((a, b) => a[0] - b[0]);
    for (const [k, which] of ks) {
      const w = dirRow(k);
      for (const j of dirOthers(w, sel)) {
        if (j >= N) continue;
        const a = which === "up" ? {s: j, t: sel} : {s: sel, t: j}, key = a.s * NA + a.t;
        if (seen.has(key)) continue;
        seen.add(key); a.k = k; a.gi = w.gi; a.sign = w.sign; out.push(a);
      }
    }
    for (const a of out) a.rev = seen.has(a.t * NA + a.s);
  }
  return (mapArrows = out);
}
function drawSelection(r) {
  const x0 = sx(sel), y0 = sy(sel);
  for (const p of P) {
    const a = Math.abs(p.cos);
    ctx.strokeStyle = p.cos > 0 ? WITH : OPP; ctx.globalAlpha = 0.35 + 0.6 * a; ctx.lineWidth = 0.8 + 2.4 * a;
    ctx.beginPath(); ctx.moveTo(x0, y0); ctx.lineTo(sx(p.j), sy(p.j)); ctx.stroke();
  }
  ctx.globalAlpha = 1;
  const arrows = mapArrowList(), ab = ArrowBatch();
  for (const a of arrows) ab.add(sx(a.s), sy(a.s), sx(a.t), sy(a.t), a.s === sel ? r + 5 : r + 2, a.t === sel ? r + 6 : r + 3, a.gi, headSign(a), false, a.rev ? 3 : 0);
  ab.draw(ctx);
  for (const p of P) {
    ctx.beginPath(); ctx.arc(sx(p.j), sy(p.j), r + 1.5, 0, 2 * Math.PI);
    ctx.fillStyle = colourOf(p.j); ctx.fill(); ctx.lineWidth = 2; ctx.strokeStyle = p.cos > 0 ? WITH : OPP; ctx.stroke();
  }
  const ends = arrows.map(a => a.s === sel ? a.t : a.s).filter(j => !pset.has(j));
  for (const j of ends) {
    ctx.beginPath(); ctx.arc(sx(j), sy(j), r + 1.5, 0, 2 * Math.PI);
    ctx.fillStyle = colourOf(j); ctx.fill(); ctx.lineWidth = 2; ctx.strokeStyle = DIRC; ctx.stroke();
  }
  ctx.beginPath(); ctx.arc(x0, y0, r + 4, 0, 2 * Math.PI);
  ctx.fillStyle = colourOf(sel); ctx.fill(); ctx.lineWidth = 2.5; ctx.strokeStyle = INK; ctx.stroke();
  // labels: the selected gene first, then partners by |cos|, then its arrows' other genes, skipping any that would
  // overlap one already drawn
  ctx.textAlign = "left"; ctx.textBaseline = "middle";
  const label = Labeler(ctx);
  label(D.sym[sel], x0 + r + 7, y0, "700 13px " + FF, INK, 15);
  for (const p of P) label(D.sym[p.j], sx(p.j) + r + 4, sy(p.j), "11px " + FF, p.cos > 0 ? WITH_T : OPP_T, 12);
  for (const j of ends) label(D.sym[j], sx(j) + r + 4, sy(j), "600 11px " + FF, DIRC_T, 12);
}

// hit testing, pointer, wheel
function nearest(mx, my) {
  const r = Math.max(6, pointR() + 3), r2 = r * r;
  let best = -1, bd = r2;
  const k = V.k, tx = V.tx, ty = V.ty, dim = hlMod >= 0;
  for (let i = 0; i < N; i++) {
    const dx = PX[i] * k + tx - mx, dy = -PY[i] * k + ty - my, d = dx * dx + dy * dy;
    if (d < bd || (d === bd && dim && D.mod[i] === hlMod)) { bd = d; best = i; }
  }
  return best;
}
const ptrs = new Map();
let dragged = false, pinch = null, downAt = null;
function local(e, el) { const r = el.getBoundingClientRect(); return [e.clientX - r.left, e.clientY - r.top]; }
cv.addEventListener("pointerdown", e => {
  cv.setPointerCapture(e.pointerId);
  ptrs.set(e.pointerId, local(e, cv));
  dragged = false; downAt = local(e, cv);
  if (ptrs.size === 2) { const [a, b] = [...ptrs.values()]; pinch = {d: Math.hypot(a[0] - b[0], a[1] - b[1]), k: T.k}; }
  cv.classList.add("drag");
});
cv.addEventListener("pointermove", e => {
  const p = local(e, cv);
  if (ptrs.has(e.pointerId)) {
    const q = ptrs.get(e.pointerId);
    ptrs.set(e.pointerId, p);
    if (ptrs.size === 2 && pinch) {
      const [a, b] = [...ptrs.values()], d = Math.hypot(a[0] - b[0], a[1] - b[1]), mx = (a[0] + b[0]) / 2, my = (a[1] + b[1]) / 2;
      zoomAt(mx, my, (pinch.k * d / Math.max(pinch.d, 1)) / T.k, true);
      dragged = true;
      return;
    }
    const dx = p[0] - q[0], dy = p[1] - q[1];
    if (Math.abs(p[0] - downAt[0]) + Math.abs(p[1] - downAt[1]) > 3) dragged = true;
    V.tx += dx; V.ty += dy; T.tx += dx; T.ty += dy;
    hideTip(); req();
    return;
  }
  const h = nearest(p[0], p[1]);
  if (h !== hover) { hover = h; req(); }
  if (h >= 0) showTip(h, p[0], p[1]); else hideTip();
});
function endPtr(e) {
  ptrs.delete(e.pointerId);
  if (ptrs.size < 2) pinch = null;
  if (ptrs.size === 0) cv.classList.remove("drag");
}
cv.addEventListener("pointerup", e => {
  const p = local(e, cv), wasDrag = dragged;
  endPtr(e);
  if (!wasDrag && e.button === 0) { const h = nearest(p[0], p[1]); if (h >= 0) select(h, false, "map"); else if (sel >= 0) select(-1, false, "map"); }
});
cv.addEventListener("pointercancel", endPtr);
cv.addEventListener("pointerleave", () => { if (hover >= 0) { hover = -1; req(); } hideTip(); });
function zoomAt(mx, my, f, immediate) {
  const k = Math.min(K0 * 400, Math.max(K0 * 0.3, T.k * f)), g = k / T.k;
  T.tx = mx - (mx - T.tx) * g; T.ty = my - (my - T.ty) * g; T.k = k;
  if (immediate) Object.assign(V, T);
  req();
}
cv.addEventListener("wheel", e => {
  e.preventDefault();
  const [mx, my] = local(e, cv), dy = e.deltaMode === 1 ? e.deltaY * 33 : e.deltaY;
  zoomAt(mx, my, Math.exp(-dy * 0.0016), false);
  hideTip();
}, {passive: false});
cv.addEventListener("dblclick", e => { const [mx, my] = local(e, cv); zoomAt(mx, my, 2, false); });

function tipHtml(i) {
  const m = D.mod[i], arm = D.arm[i], mod = MODS.get(m);
  let h = "<b>" + esc(D.sym[i]) + "</b>";
  if (has(D.name) && D.name[i]) h += " <span class='m'>" + esc(D.name[i]) + "</span>";
  if (i >= N) return h + "<br><span class='alc'>&#9888; not on the map</span> <span class='m'>(not in the vector space: no partners or module)</span>";
  h += "<br><span class='k' style='background:" + modColour(m) + "'></span>" +
       (m > 0 ? "Module " + m + (arm !== "." && mod && mod.opp ? ", arm " + (arm === "-" ? "&minus;" : "+") : "") + (mod ? " <span class='m'>" + esc(mod.label) + "</span>" : "") : "<span class='m'>no module</span>");
  if (EFO.has(i)) h += "<br><span class='alc'>&#9888; " + EFO_TXT + "</span>";
  return h;
}
function placeTip(el, html, mx, my, Wd, Hd) {
  el.innerHTML = html; el.style.display = "block";
  const tw = el.offsetWidth, th = el.offsetHeight;
  let x = mx + 14, y = my + 14;
  if (x + tw > Wd - 4) x = mx - tw - 12;
  if (y + th > Hd - 4) y = my - th - 12;
  el.style.left = Math.max(2, x) + "px"; el.style.top = Math.max(2, y) + "px";
}
function showTip(i, mx, my) { placeTip(tip, tipHtml(i) + ($("dirm").checked ? dirTip(i) : ""), mx, my, W, H); }
// the probable-direction rows between the selected gene and gene i (either way, gene targets), in ORDER
function dirBetween(a, b) {
  if (!HAS_DIR || a < 0 || b < 0 || a === b) return [];
  const te = k => DR.r[k * DW + 3];
  return dirRowsOf(a, "dn").filter(k => te(k) === b).concat(dirRowsOf(b, "dn").filter(k => te(k) === a)).sort((x, y) => x - y);
}
function dirTip(i) {
  // the cap rule (rule 1): the 3 strongest, and any of the 3 strongest without an alert that come after them
  const ks = dirBetween(sel, i), c = dirCap(ks, 3);
  let h = "";
  for (const k of c.shown) {
    const w = dirRow(k);
    h += "<br><span style='color:" + DIRC_T + "'>[" + esc(w.grade) + "] " + esc(w.S + " " + ARROW_S + " " + w.tgt) + "</span>: " + esc(w.signText) + (w.alShort ? " <span class='alc'>" + esc(w.alShort) + "</span>" : "");
  }
  if (c.more) h += "<br><span class='m'>" + esc(dirMoreText(c.more, c.moreAl, "rows")) + " between them in the side panel</span>";
  return h;
}
function hideTip() { tip.style.display = "none"; }

// views, colours, legend
function animateTo(l, dur) {
  // from the current (possibly mid-animation) positions to layout l at the current spread
  anim = {A: {x: Float32Array.from(PX), y: Float32Array.from(PY)}, B: lay(l), t0: performance.now(), dur: dur};
  req();
}
function setLayout(l) {
  if (l === layout && !anim && MIX[l].s === spread) return;
  layout = l;
  animateTo(l, 750);
  if (sel >= 0 && sel < N) { centreOn(sel, l); mapSelPending = false; }   // follow the selected gene to the new layout
  status(); req();
}
function setSpread(v, dur) {
  if (!HAS_SPREAD) return;
  spread = Math.max(0, Math.min(1, +v || 0));
  $("spr").value = Math.round(spread * 100); $("spro").textContent = spread.toFixed(2);
  if (isMap(active)) {
    animateTo(layout, dur == null ? 160 : dur);
    // the selected gene stays where it is on the screen while the groups move apart (its partner lines with it)
    if (sel >= 0 && sel < N) anim.follow = {i: sel, sx: V.tx + PX[sel] * V.k, sy: V.ty - PY[sel] * V.k};
  }
  else { const t = lay(layout); PX.set(t.x); PY.set(t.y); anim = null; }
  status();
}
function setColour(c) {
  colourMode = c;
  $("c0").setAttribute("aria-pressed", c === 0); $("c1").setAttribute("aria-pressed", c === 1);
  $("armkey").style.display = c === 1 ? "block" : "none";
  regroup();
}
function buildLegend() {
  const body = $("lgbody"), counts = new Map();
  let nArm = {"+": 0, "-": 0, ".": 0};
  for (let i = 0; i < N; i++) { counts.set(D.mod[i], (counts.get(D.mod[i]) || 0) + 1); nArm[D.arm[i]] = (nArm[D.arm[i]] || 0) + 1; }
  $("armkey").innerHTML =
    "<div><span class='sw' style='background:" + ARMC["+"] + "'></span> + arm (" + nArm["+"].toLocaleString() + ")" +
    " &nbsp; <span class='sw' style='background:" + ARMC["-"] + "'></span> &minus; arm (" + nArm["-"].toLocaleString() + ")" +
    (nArm["."] ? " &nbsp; <span class='sw' style='background:" + GREY + "'></span> none" : "") + "</div>" +
    "<div class='note' style='margin-top:3px'>A module has a &minus; arm only where its two sides move in opposite directions under the same drugs (mean cos between them &le; &minus;0.2); otherwise all its genes are +.</div>";
  let h = "";
  for (const m of D.mods) {
    h += "<div class='li' data-m='" + m.id + "' title='" + esc("M" + m.id + ": " + m.label + " (" + m.n + " genes)") + "'>" +
      "<span class='sw' style='background:" + modColour(m.id) + "'></span><span class='t'><b>M" + m.id + "</b> " + esc(m.label) +
      "</span><span class='n'>" + (counts.get(m.id) || m.n) + "</span></div>";
  }
  if (counts.get(0)) h += "<div class='li' data-m='0'><span class='sw' style='background:" + GREY + "'></span><span class='t'>no module</span><span class='n'>" + counts.get(0) + "</span></div>";
  if (!h) h = "<div class='note' style='padding:4px 8px'>No modules.</div>";
  body.innerHTML = h;
  $("lgtitle").innerHTML = "Modules (" + D.mods.length + ")" + (D.labels_from === "validation" ? "" : " <span class='note' style='font-weight:400'>labels: top genes</span>");
  body.addEventListener("click", e => {
    const li = e.target.closest(".li");
    if (li) highlight(+li.dataset.m === hlMod ? -1 : +li.dataset.m);
  });
}
function highlight(m) {
  hlMod = m; focus = "module"; srcSel = "";
  for (const li of document.querySelectorAll("#lgbody .li")) li.classList.toggle("on", +li.dataset.m === m);
  if (m >= 0) { const li = document.querySelector("#lgbody .li[data-m='" + m + "']"); if (li) li.scrollIntoView({block: "nearest"}); }
  regroup(); renderPanel(); status();
  for (const k in PHYS) PHYS[k].onHighlight(m);
  if (TOUR) TOUR.onHighlight();
}
function centreOn(i, l) {
  // zoom so that the gene and its partners fill the free part of the canvas, centred on the gene
  const lw = W > 700 ? legendW() : 0, w = W - lw, X = lay(l).x, Y = lay(l).y;
  let far = 0;
  for (const p of P) far = Math.max(far, Math.abs(X[p.j] - X[i]), Math.abs(Y[p.j] - Y[i]));
  const k = far > 0 ? Math.min(K0 * 40, Math.max(K0 * 1.2, 0.42 * Math.min(w, H) / far)) : Math.max(T.k, K0 * 4);
  T.k = k; T.tx = lw + w / 2 - X[i] * k; T.ty = H / 2 + Y[i] * k;
}

// ================================================================ tabs 3-5: one force simulation, three views of it
function mulberry(seed) {
  let a = seed >>> 0;
  return () => { a = (a + 0x6D2B79F5) >>> 0; let t = a; t = Math.imul(t ^ (t >>> 15), t | 1); t ^= t + Math.imul(t ^ (t >>> 7), t | 61); return ((t ^ (t >>> 14)) >>> 0) / 4294967296; };
}
// graph/edges.parquet (the kNN graph that defines the modules): index pairs, cos x100, evidence; decoded on first use
let EG = null;
function b64bytes(s) { const t = atob(s || ""), u = new Uint8Array(t.length); for (let i = 0; i < t.length; i++) u[i] = t.charCodeAt(i); return u; }
function graphEdges() {
  if (EG) return EG;
  const e = D.edges || {}, w = e.bytes || 2;
  let m = e.m || 0;
  const A = new Int32Array(m), B = new Int32Array(m), C = new Float32Array(m), EV = new Uint8Array(m);
  if (m) {
    const ua = b64bytes(e.a), ub = b64bytes(e.b), uc = b64bytes(e.cos), ue = b64bytes(e.ev);
    let k2 = 0;
    for (let k = 0; k < m; k++) {
      let a = 0, b = 0;
      for (let t = w - 1; t >= 0; t--) { a = a * 256 + ua[k * w + t]; b = b * 256 + ub[k * w + t]; }
      if (a >= N || b >= N || a === b) continue;
      const c = uc[k];
      A[k2] = a; B[k2] = b; C[k2] = (c > 127 ? c - 256 : c) / 100; EV[k2] = ue.length > k ? ue[k] : 2; k2++;
    }
    m = k2;
  }
  const off = new Int32Array(N + 1);
  for (let k = 0; k < m; k++) { off[A[k] + 1]++; off[B[k] + 1]++; }
  for (let i = 0; i < N; i++) off[i + 1] += off[i];
  const adj = new Int32Array(2 * m), fill = off.slice(0, N);
  for (let k = 0; k < m; k++) { adj[fill[A[k]]++] = k; adj[fill[B[k]]++] = k; }
  return (EG = {m: m, A: A, B: B, C: C, EV: EV, off: off, adj: adj});
}

// The engine. Velocity Verlet with friction, as d3-force: every force adds to the velocities, scaled by alpha; alpha
// cools toward alphaTarget (0 unless a gene is dragged); positions move by the damped velocities.
//   springs     every edge: (d - L) / d * spr * |cos| / min(degree) (shared by the two ends by degree), rest length
//               L = s0 * (1.6 - |cos|): stronger relations are shorter springs. With oppRepel, an edge with cos < 0
//               only pushes: rest length s0 * pushLen, and no pull beyond it.
//   repulsion   every pair: -rep / d (2D Coulomb), Barnes-Hut quadtree with theta 0.8 (a cell of width w at distance
//               d counts as one body when w / d < theta)
//   centre      -centre * position: a weak pull that keeps the layout together
function makeSim() {
  const S = {n: 0, m: 0, alpha: 0, alphaMin: 0.002, alphaTarget: 0, alphaDecay: 1 - Math.pow(0.002, 1 / 300),
    vDecay: 0.4, rep: 30, spr: 1, centre: 0.03, theta2: 0.64, oppRepel: false, s0: 30, pushLen: 6, dmin2: 4, ticks: 0};
  let cap = 0, cnt = 0, qx0, qy0, qw, qcx, qcy, qm, qkid, qpt, qint, nxt;
  const stack = new Int32Array(4 * 64 + 8), MAXD = 52;
  let seed = 7;
  const jiggle = () => { seed = (seed * 1103515245 + 12345) & 0x7fffffff; return (seed / 0x7fffffff - 0.5) * 1e-3; };
  function grow(c) {                                     // only while the tree is built: centres of mass come after
    const o = cnt;
    const nx0 = new Float64Array(c), ny0 = new Float64Array(c), nw = new Float64Array(c), ncx = new Float64Array(c), ncy = new Float64Array(c);
    const nm = new Float64Array(c), nkid = new Int32Array(4 * c), npt = new Int32Array(c), nint = new Uint8Array(c);
    if (qx0) { nx0.set(qx0.subarray(0, o)); ny0.set(qy0.subarray(0, o)); nw.set(qw.subarray(0, o)); nkid.set(qkid.subarray(0, 4 * o)); npt.set(qpt.subarray(0, o)); nint.set(qint.subarray(0, o)); }
    qx0 = nx0; qy0 = ny0; qw = nw; qcx = ncx; qcy = ncy; qm = nm; qkid = nkid; qpt = npt; qint = nint; cap = c;
  }
  function cell(x0, y0, w) {
    if (cnt >= cap) grow(Math.max(64, cap * 2));
    const c = cnt++;
    qx0[c] = x0; qy0[c] = y0; qw[c] = w; qkid[4 * c] = qkid[4 * c + 1] = qkid[4 * c + 2] = qkid[4 * c + 3] = -1;
    qpt[c] = -1; qint[c] = 0;
    return c;
  }
  function insert(i) {
    const x = S.x, y = S.y, px = x[i], py = y[i];
    let c = 0, depth = 0;
    for (;;) {
      if (qint[c]) {
        const h = qw[c] / 2, q = (px >= qx0[c] + h ? 1 : 0) + (py >= qy0[c] + h ? 2 : 0);
        let k = qkid[4 * c + q];
        if (k < 0) { k = cell(qx0[c] + (q & 1) * h, qy0[c] + (q >> 1) * h, h); qkid[4 * c + q] = k; qpt[k] = i; nxt[i] = -1; return; }
        c = k; depth++;
        continue;
      }
      const j = qpt[c];
      if (j < 0) { qpt[c] = i; nxt[i] = -1; return; }
      if (depth >= MAXD || (x[j] === px && y[j] === py)) { nxt[i] = j; qpt[c] = i; return; }
      // split the leaf: its point (and any coincident ones chained to it) moves down one level
      qint[c] = 1; qpt[c] = -1;
      const h = qw[c] / 2, q = (x[j] >= qx0[c] + h ? 1 : 0) + (y[j] >= qy0[c] + h ? 2 : 0);
      const k = cell(qx0[c] + (q & 1) * h, qy0[c] + (q >> 1) * h, h);
      qkid[4 * c + q] = k; qpt[k] = j;
    }
  }
  function buildTree() {
    const n = S.n, x = S.x, y = S.y;
    let x0 = Infinity, y0 = Infinity, x1 = -Infinity, y1 = -Infinity;
    for (let i = 0; i < n; i++) { const a = x[i], b = y[i]; if (a < x0) x0 = a; if (a > x1) x1 = a; if (b < y0) y0 = b; if (b > y1) y1 = b; }
    let w = Math.max(x1 - x0, y1 - y0);
    if (!(w > 0)) w = 1;
    w = w * 1.0001 + 1e-6;
    cnt = 0; cell(x0, y0, w);
    for (let i = 0; i < n; i++) insert(i);
    // centres of mass, children before parents (a child always has a higher index than its parent)
    for (let c = cnt - 1; c >= 0; c--) {
      let m = 0, sx = 0, sy = 0;
      if (qint[c]) {
        for (let q = 0; q < 4; q++) { const k = qkid[4 * c + q]; if (k >= 0 && qm[k] > 0) { m += qm[k]; sx += qcx[k] * qm[k]; sy += qcy[k] * qm[k]; } }
      } else for (let j = qpt[c]; j >= 0; j = nxt[j]) { m++; sx += x[j]; sy += y[j]; }
      qm[c] = m; qcx[c] = m ? sx / m : 0; qcy[c] = m ? sy / m : 0;
    }
  }
  let ordBuf = null;
  function treeOrder() {                                 // the genes leaf by leaf, depth first: neighbours in space are neighbours in memory
    if (!ordBuf || ordBuf.length !== S.n) ordBuf = new Int32Array(S.n);
    let k = 0, sp = 0;
    stack[sp++] = 0;
    while (sp > 0) {
      const c = stack[--sp];
      if (!qint[c]) { for (let j = qpt[c]; j >= 0; j = nxt[j]) ordBuf[k++] = j; continue; }
      for (let q = 3; q >= 0; q--) { const kk = qkid[4 * c + q]; if (kk >= 0) stack[sp++] = kk; }
    }
    return ordBuf;
  }
  function repulse(alpha) {
    buildTree();
    const n = S.n, x = S.x, y = S.y, vx = S.vx, vy = S.vy, str = -S.rep * alpha, th2 = S.theta2, dmin2 = S.dmin2;
    const QM = qm, QI = qint, QP = qpt, QK = qkid, QX = qcx, QY = qcy, QW = qw, NX = nxt, st = stack;
    const ord = treeOrder();
    for (let oi = 0; oi < n; oi++) {
      const i = ord[oi], xi = x[i], yi = y[i];
      let ax = 0, ay = 0, sp = 0;
      st[sp++] = 0;
      while (sp > 0) {
        const c = st[--sp], m = QM[c];
        if (!m) continue;
        if (!QI[c]) {                                    // a leaf: every gene in it, one by one
          for (let j = QP[c]; j >= 0; j = NX[j]) {
            if (j === i) continue;
            let dx = x[j] - xi, dy = y[j] - yi, l = dx * dx + dy * dy;
            if (l === 0) { dx = jiggle(); dy = jiggle(); l = dx * dx + dy * dy; }
            if (l < dmin2) l = Math.sqrt(dmin2 * l);
            ax += dx * str / l; ay += dy * str / l;
          }
          continue;
        }
        const dx = QX[c] - xi, dy = QY[c] - yi, w = QW[c];
        let l = dx * dx + dy * dy;
        if (w * w < th2 * l) {                           // far enough: the whole cell as one body at its centre of mass
          if (l < dmin2) l = Math.sqrt(dmin2 * l);
          const f = str * m / l;
          ax += dx * f; ay += dy * f;
          continue;
        }
        const b = 4 * c;
        for (let q = 0; q < 4; q++) { const k = QK[b + q]; if (k >= 0) st[sp++] = k; }
      }
      vx[i] += ax; vy[i] += ay;
    }
  }
  S.load = function (n, px, py, ea, eb, ec) {
    S.n = n; S.x = Float32Array.from(px); S.y = Float32Array.from(py);
    S.vx = new Float32Array(n); S.vy = new Float32Array(n); S.fx = new Float32Array(n); S.fy = new Float32Array(n);
    S.fixed = new Uint8Array(n);                         // 1 pinned by the user, 2 being dragged, 4 the centre gene (pinned at the start)
    const m = ea.length;
    S.m = m; S.ea = Int32Array.from(ea); S.eb = Int32Array.from(eb); S.ec = Float32Array.from(ec);
    const deg = new Float32Array(n);
    for (let k = 0; k < m; k++) { deg[S.ea[k]]++; deg[S.eb[k]]++; }
    S.deg = deg;
    S.estr = new Float32Array(m); S.ebias = new Float32Array(m); S.elen = new Float32Array(m);
    for (let k = 0; k < m; k++) {
      const a = S.ea[k], b = S.eb[k], w = Math.abs(S.ec[k]);
      S.estr[k] = w / Math.max(1, Math.min(deg[a], deg[b]));
      S.ebias[k] = deg[a] / (deg[a] + deg[b]);
      S.elen[k] = S.s0 * (1.6 - w);
    }
    // incident edges per node (CSR)
    const off = new Int32Array(n + 1);
    for (let k = 0; k < m; k++) { off[S.ea[k] + 1]++; off[S.eb[k] + 1]++; }
    for (let i = 0; i < n; i++) off[i + 1] += off[i];
    const adj = new Int32Array(2 * m), fill = off.slice(0, n);
    for (let k = 0; k < m; k++) { adj[fill[S.ea[k]]++] = k; adj[fill[S.eb[k]]++] = k; }
    S.off = off; S.adj = adj;
    nxt = new Int32Array(Math.max(1, n));
    if (cap < 2 * n + 16) { cnt = 0; grow(2 * n + 16); }
  };
  S.tick = function () {
    const n = S.n;
    if (!n) return;
    S.alpha += (S.alphaTarget - S.alpha) * S.alphaDecay;
    const alpha = S.alpha, x = S.x, y = S.y, vx = S.vx, vy = S.vy;
    // springs
    const ea = S.ea, eb = S.eb, ec = S.ec, estr = S.estr, ebias = S.ebias, elen = S.elen, ks = S.spr * alpha;
    const rep = S.oppRepel, push = S.s0 * S.pushLen;
    if (ks > 0) for (let k = 0, m = S.m; k < m; k++) {
      const a = ea[k], b = eb[k];
      let dx = x[b] + vx[b] - x[a] - vx[a], dy = y[b] + vy[b] - y[a] - vy[a], l = Math.sqrt(dx * dx + dy * dy);
      if (l < 1e-9) { dx = jiggle(); dy = jiggle(); l = Math.sqrt(dx * dx + dy * dy); }
      let L = elen[k];
      if (rep && ec[k] < 0) { if (l >= push) continue; L = push; }
      const f = (l - L) / l * ks * estr[k], bb = ebias[k];
      dx *= f; dy *= f;
      vx[b] -= dx * bb; vy[b] -= dy * bb;
      vx[a] += dx * (1 - bb); vy[a] += dy * (1 - bb);
    }
    // repulsion between every pair, and the pull to the centre
    if (S.rep > 0 && n > 1) repulse(alpha);
    const c = S.centre * alpha;
    for (let i = 0; i < n; i++) { vx[i] -= x[i] * c; vy[i] -= y[i] * c; }
    // move
    const keep = 1 - S.vDecay, fixed = S.fixed, fx = S.fx, fy = S.fy;
    for (let i = 0; i < n; i++) {
      if (fixed[i]) { x[i] = fx[i]; y[i] = fy[i]; vx[i] = 0; vy[i] = 0; continue; }
      let a = vx[i] * keep, b = vy[i] * keep;
      if (!(a === a && b === b)) { a = 0; b = 0; }
      vx[i] = a; vy[i] = b; x[i] += a; y[i] += b;
    }
    S.ticks++;
  };
  S.heat = a => { S.alpha = Math.max(S.alpha, a); };
  S.moving = () => S.n > 0 && (S.alpha >= S.alphaMin || S.alphaTarget > 0);
  return S;
}

// springs among a set of genes (loc: entry -> index in the set, -1 outside), as three arrays
function relSprings(ids, loc, minCos, evMin) {               // each gene's top partners (relations, as in the side panel)
  const ea = [], eb = [], ec = [], ev = [], seen = new Set(), n = ids.length;
  for (let u = 0; u < n; u++) {
    const a = D.rel[ids[u]] || [];
    for (let t = 0; t + 3 < a.length; t += 4) {
      const v = loc[a[t]];
      if (v < 0 || v === u) continue;
      const c = a[t + 1] / 100;
      if (Math.abs(c) < minCos || (a[t + 3] & 3) < evMin) continue;
      const lo = Math.min(u, v), hi = Math.max(u, v), key = lo * n + hi;
      if (seen.has(key)) continue;
      seen.add(key); ea.push(lo); eb.push(hi); ec.push(c); ev.push(a[t + 3] & 3);
    }
  }
  return {ea: ea, eb: eb, ec: ec, ev: ev, src: "rel"};
}
function graphSprings(ids, loc, minCos, evMin) {             // the kNN graph (graph/edges.parquet)
  const G = graphEdges();
  if (!G.m) return relSprings(ids, loc, minCos, evMin);
  const ea = [], eb = [], ec = [], ev = [];
  for (let u = 0; u < ids.length; u++) {
    const i = ids[u];
    for (let p = G.off[i]; p < G.off[i + 1]; p++) {
      const k = G.adj[p];
      if (G.A[k] !== i) continue;                              // each edge once, from its first gene
      const v = loc[G.B[k]];
      if (v < 0 || Math.abs(G.C[k]) < minCos || G.EV[k] < evMin) continue;
      ea.push(u); eb.push(v); ec.push(G.C[k]); ev.push(G.EV[k]);
    }
  }
  return {ea: ea, eb: eb, ec: ec, ev: ev, src: "graph"};
}

function physBar(kind) {
  const seg = (k, labels, on, titles) => "<span class='seg'>" + labels.map((l, t) => "<button data-k='" + k + t + "' aria-pressed='" + (t === on) + "'" +
    (titles ? " title='" + titles[t] + "'" : "") + ">" + l + "</button>").join("") + "</span>";
  const rng = (k, label, min, max, step, val, title) => "<label class='rng' title='" + title + "'>" + label + " <input type='range' data-k='" + k +
    "' min='" + min + "' max='" + max + "' step='" + step + "' value='" + val + "'><output data-k='" + k + "o'></output></label>";
  let h = "<div class='bars'><div class='bar'>";
  h += "<div class='grp'>Opposite genes " + seg("opp", ["attract", "repel"], 0, [
    "Red (opposite) relations are springs like green ones: both arms of a pathway form one cluster (the nodal view)",
    "Red (opposite) relations push their two genes apart: the minus arm separates from the plus arm (the signed view)"]) + "</div>";
  h += "<div class='grp'>Colour " + seg("col", ["Module", "Arm"], kind === "mod" ? 1 : 0) + "</div>";
  h += "<span class='seg'><button data-k='pause' aria-pressed='false' title='Pause / resume the simulation (space)'>Pause</button>" +
    "<button data-k='heat' title='Re-heat: let the layout move again'>Re-heat</button>" +
    "<button data-k='reset' title='Start the layout again and unpin every gene'>Reset</button>" +
    "<button data-k='fit' title='Fit the view to all genes'>Fit</button></span>";
  if (kind === "nbr") h += "<div class='grp' title='1: the selected gene and its partners; 2: also their partners; 3, 4: and theirs, one more step each'>Depth " +
    seg("dep", ["1", "2", "3", "4"], 1) + "</div>" +
    rng("max", "Max genes", 20, 2000, 10, 300, "At most this many genes, the strongest partners first (the product of the |cos| along the way)") +
    "<div class='grp' title='Probable direction (direction stage): arrows between the genes shown; + its genes also adds the selected gene&#39;s probable up- and downstream genes'>Direction " +
    seg("dir", ["off", "arrows", "+ its genes"], HAS_DIR ? 2 : 0, ["No direction arrows", "Arrows between the genes shown (their probable direction rows)",
      "Arrows, and the selected gene&#39;s probable up- and downstream genes (the rows its side-panel lists show) added to the neighbourhood"]) + "</div>";
  h += "</div><div class='bar'>";
  h += rng("rep", "Repulsion", 0, 150, 5, 30, "Strength of the push between every pair of genes") +
    rng("spr", "Springs", 0, 300, 10, 100, "Strength of the springs, in % of the default") +
    rng("min", "Min |cos|", 0, 95, 5, 30, "Relations weaker than this are not springs");
  h += "<label class='grp' title='both halves: same sign with fdr &lt;= 0.10 in two random halves of the compounds; one half: strong in one random half only (not replicated); not reproduced: neither. Relations left out are still listed, with an alert, in the side panel'>Evidence <select data-k='ev'>" +
    "<option value='1'>both or one half</option><option value='2'>both halves only</option><option value='0'>every relation (also not reproduced)</option></select></label>";
  return h + "</div></div>";
}
// the module tab's picker sits on the canvas, above the module's label and arms
const MOD_CTL = "<div class='ictl'><label>Module <select data-k='msel'></select></label>" +
  "<button class='btn' data-k='mselg' title='Show the module of the selected gene'>Selected gene's module</button>" +
  "<label title='Also show, dimmed, the genes outside the module that its genes link to'><input type='checkbox' data-k='ring'> outside genes (1 hop)</label></div>";

function PhysPane(kind) {
  const pane = $("pane-" + kind);
  pane.innerHTML = physBar(kind) + "<div class='wrap'><canvas></canvas><div class='info none'>" + (kind === "mod" ? MOD_CTL : "") +
    "<div class='itxt'></div></div><div class='msg'></div><div class='tip'></div><div class='status'></div></div>";
  const q = k => pane.querySelector("[data-k='" + k + "']");
  const wrapEl = pane.querySelector(".wrap"), cvs = pane.querySelector("canvas"), g2 = cvs.getContext("2d");
  const tipEl = pane.querySelector(".tip"), infoEl = pane.querySelector(".info"), itxt = pane.querySelector(".itxt");
  const msgEl = pane.querySelector(".msg"), statusEl = pane.querySelector(".status");
  const S = makeSim(), layer = kind === "all" ? PointLayer(cvs, g2) : null;
  const st = {colour: kind === "mod" ? 1 : 0, paused: false, dirty: true, fresh: true, autoFit: true, follow: false,
    depth: 2, maxN: 300, minCos: 0.3, ev: 1, module: -1, ring: false,
    ids: new Int32Array(0), dim: new Uint8Array(0), level: new Uint8Array(0), byDeg: new Int32Array(0), centre: -1,
    msg: "", info: "", hover: -1, drag: -1, groups: null, groupsDirty: true, avgTick: 0, tpf: 0, drawMs: 0, frames: [],
    skip: 0, centreSel: false, lastStatus: 0, src: "", lastRun: 0, debt: 0,
    dir: kind === "nbr" && HAS_DIR ? 2 : 0, nRel: 0, extraFrom: 0, arrows: [], arrowsMore: 0, dirInfo: ""};
  const loc = new Int32Array(NA).fill(-1), nloc = new Int32Array(NA).fill(-1);
  let W = 1, H = 1, DPR = 1, fitK = 1, sized = false, clickTimer = 0, dragged = false, downAt = null, pinch = null, lastFit = null;
  // a click on a gene selects it after DBL_MS without a second click; the last two press-releases (a micro-drag too)
  // are kept so that a double-click - even a slow one, after the first click's selection re-centred the view - pins
  // the gene clicked first
  const DBL_MS = 400;
  let prevClick = null, lastClick = null;
  const V = {k: 1, tx: 0, ty: 0}, T = {k: 1, tx: 0, ty: 0}, ptrs = new Map();
  const visible = () => active === kind;
  const nodeColour = i => st.colour === 1 ? (ARMC[D.arm[i]] || GREY) : modColour(D.mod[i]);

  // ---------------------------------------------------------------- what to simulate
  function dirGenes(i) {                                        // the genes of the selected gene's shown direction rows
    const out = [];
    if (!HAS_DIR || i < 0) return out;
    for (const which of ["up", "dn"]) {
      const rows = dirRowsOf(i, which);
      for (const k of (dirAll[which] ? rows : dirCap(rows, DR.cap || 8).shown)) for (const j of dirOthers(dirRow(k), i)) if (out.indexOf(j) < 0) out.push(j);
    }
    return out;
  }
  function buildNbr() {
    if (sel < 0) return {msg: "Select a gene (search above, or click one on another tab) to see it with its partners and their partners."};
    const dg = st.dir === 2 ? dirGenes(sel) : [];
    if (sel >= N && !dg.length) return {msg: "<b>" + esc(D.sym[sel]) + "</b> is not on the map (not in the vector space), so it has no partners to simulate. Its drug-doses and cell lines are in the side panel." +
      (!HAS_DIR ? "" : st.dir === 2 ? " It has no probable up- or downstream gene either." : " <i>Direction: + its genes</i> shows its probable up- and downstream genes, if it has any.")};
    // breadth first, one depth at a time: each depth's genes by the product of the |cos| along the way, strongest
    // first, until Max genes
    const ids = [sel], parent = [-1], level = [0], score = [1], perLevel = [1];
    nloc[sel] = 0;
    const ok = p => Math.abs(p.cos) >= st.minCos && p.ev >= st.ev;
    let frontier = [0], full = false;
    for (let L = 1; L <= st.depth && frontier.length; L++) {
      const cand = [];
      for (const u of frontier) for (const p of partnersOf(ids[u])) if (ok(p) && nloc[p.j] < 0) cand.push([p.j, u, Math.abs(p.cos) * score[u]]);
      cand.sort((a, b) => b[2] - a[2]);
      const nxt = [];
      for (const c of cand) {
        if (ids.length >= st.maxN) { full = true; break; }
        if (nloc[c[0]] >= 0) continue;
        nloc[c[0]] = ids.length; nxt.push(ids.length); ids.push(c[0]); parent.push(c[1]); level.push(L); score.push(c[2]);
      }
      perLevel.push(nxt.length);
      frontier = nxt;
    }
    // Direction '+ its genes': the selected gene's probable up- and downstream genes, placed around it and held by a
    // link that is no relation (not drawn: its arrow is)
    const nPart = ids.length;
    for (const j of dg) if (nloc[j] < 0 && ids.length - nPart < 80) { nloc[j] = ids.length; ids.push(j); parent.push(0); level.push(1); score.push(0); }
    const sp = relSprings(ids, nloc, st.minCos, st.ev), own = partnersOf(sel), left = own.filter(p => !ok(p)).length;
    sp.nRel = sp.ea.length;
    for (let u = nPart; u < ids.length; u++) { sp.ea.push(0); sp.eb.push(u); sp.ec.push(0.35); sp.ev.push(2); }
    const dl = perLevel.slice(1).map((c, t) => c + (t === 0 ? " partner" + (c === 1 ? "" : "s") : " at depth " + (t + 1))).join(", ");
    const info = "<b>" + esc(D.sym[sel]) + "</b>: " + (sel >= N ? "not on the map (no partners)" : dl) + " &middot; " + ids.length + " genes" + (full ? " (Max genes reached)" : "") +
      " &middot; " + sp.nRel + " springs (top partners, |cos| &ge; " + st.minCos.toFixed(2) + ", " + ["every relation", "both or one half", "both halves"][st.ev] + ")" +
      (left ? "<br><span class='alc'>&#9888; " + left + " of its " + own.length + " listed partners are left out by Min |cos| / Evidence</span> (they stay in the side panel, with their alerts)" : "");
    return {ids: ids, parent: parent, level: level, centre: 0, springs: sp, info: info, extraFrom: nPart};
  }
  function buildMod() {
    if (!D.mods.length || !N) return {msg: "This run has no modules."};
    if (!MODS.has(st.module)) st.module = (sel >= 0 && sel < N && D.mod[sel] > 0) ? D.mod[sel] : (hlMod > 0 ? hlMod : D.mods[0].id);
    const m = st.module, ids = [], parent = [], dim = [];
    syncPicker();
    for (let i = 0; i < N; i++) if (D.mod[i] === m) { nloc[i] = ids.length; ids.push(i); parent.push(-1); dim.push(0); }
    const nIn = ids.length;
    if (st.ring && nIn) {
      const G = graphEdges(), cand = [];
      for (let u = 0; u < nIn; u++) {
        const i = ids[u];
        if (G.m) {
          for (let p = G.off[i]; p < G.off[i + 1]; p++) {
            const k = G.adj[p], j = G.A[k] === i ? G.B[k] : G.A[k];
            if (D.mod[j] !== m && Math.abs(G.C[k]) >= st.minCos && G.EV[k] >= st.ev) cand.push([j, u, Math.abs(G.C[k])]);
          }
        } else for (const p of partnersOf(i)) if (p.j < N && D.mod[p.j] !== m && Math.abs(p.cos) >= st.minCos && p.ev >= st.ev) cand.push([p.j, u, Math.abs(p.cos)]);
      }
      cand.sort((a, b) => b[2] - a[2]);
      const cap = Math.max(30, 2 * nIn);
      for (const c of cand) {
        if (ids.length - nIn >= cap) break;
        if (nloc[c[0]] >= 0) continue;
        nloc[c[0]] = ids.length; ids.push(c[0]); parent.push(c[1]); dim.push(1);
      }
    }
    const sp = graphSprings(ids, nloc, st.minCos, st.ev);
    if (ids.length > nIn) {                                    // outside genes hang on the module only
      const ea = [], eb = [], ec = [], ev = [];
      for (let k = 0; k < sp.ea.length; k++) if (sp.ea[k] < nIn || sp.eb[k] < nIn) { ea.push(sp.ea[k]); eb.push(sp.eb[k]); ec.push(sp.ec[k]); ev.push(sp.ev[k]); }
      sp.ea = ea; sp.eb = eb; sp.ec = ec; sp.ev = ev;
    }
    const md = MODS.get(m);
    let info = "<b>M" + m + "</b> " + esc(md ? md.label : "") + "<br>";
    if (md) info += md.opp ? md.np + " genes in the <b style='color:" + ARMC["+"] + "'>+ arm</b>, " + md.nm + " in the <b style='color:" + ARMC["-"] + "'>&minus; arm</b>: the arms move opposite" +
      (md.cb != null ? " (mean cos between them " + (md.cb > 0 ? "+" : "") + md.cb.toFixed(2) + ")" : "") : md.n + " genes, single-armed";
    info += " &middot; " + sp.ea.length + " springs" + (ids.length > nIn ? " &middot; " + (ids.length - nIn) + " outside genes (dimmed)" : "");
    return {ids: ids, parent: parent, dim: dim, centre: -1, springs: sp, info: info};
  }
  function buildAll() {
    if (!N) return {msg: "No genes on the map."};
    const ids = new Int32Array(N);
    for (let i = 0; i < N; i++) { ids[i] = i; nloc[i] = i; }
    const sp = graphSprings(ids, nloc, st.minCos, st.ev);
    return {ids: ids, parent: null, centre: -1, springs: sp,
      info: "All <b>" + N.toLocaleString() + "</b> genes on the map &middot; " + sp.ea.length.toLocaleString() + " springs (" +
        (sp.src === "graph" ? "the kNN graph that defines the modules" : "each gene's top partners") + "); edges are drawn for the selected gene only"};
  }
  // start positions for genes that were not in the simulation before
  function place(g, px, py, keep) {
    const n = g.ids.length, rnd = mulberry(1234 + n), s0 = S.s0;
    const done = Uint8Array.from(keep);
    if (kind !== "nbr") {
      // nodal-map coordinates (y up there, down here), scaled to about the simulation's equilibrium size
      const L = LAY[0];
      let cx = 0, cy = 0, c = 0, r2 = 0;
      for (let u = 0; u < n; u++) if (!(g.dim && g.dim[u])) { cx += L.x[g.ids[u]]; cy += L.y[g.ids[u]]; c++; }
      if (c) { cx /= c; cy /= c; }
      for (let u = 0; u < n; u++) if (!(g.dim && g.dim[u])) { const dx = L.x[g.ids[u]] - cx, dy = L.y[g.ids[u]] - cy; r2 += dx * dx + dy * dy; }
      const rms = Math.sqrt(r2 / Math.max(1, c)) || 1, sc = 0.5 * Math.sqrt(Math.max(S.rep, 10) * Math.max(c, 2) / S.centre) / rms;
      for (let u = 0; u < n; u++) if (!done[u] && !(g.dim && g.dim[u])) {
        px[u] = (L.x[g.ids[u]] - cx) * sc + jit(rnd); py[u] = -(L.y[g.ids[u]] - cy) * sc + jit(rnd); done[u] = 1;
      }
    }
    // the rest around the gene they were reached from (which comes first); level-1 partners on a circle
    let n1 = 0;
    if (g.level) for (let u = 0; u < n; u++) if (g.level[u] === 1) n1++;
    let t1 = 0;
    for (let u = 0; u < n; u++) {
      if (done[u]) continue;
      const p = g.parent ? g.parent[u] : -1, bx = p >= 0 ? px[p] : 0, by = p >= 0 ? py[p] : 0;
      if (p < 0) { px[u] = bx; py[u] = by; done[u] = 1; continue; }
      let a, r;
      if (g.level && g.level[u] === 1) { a = 2 * Math.PI * (t1++ + 0.5 * rnd()) / Math.max(1, n1); r = s0 * 2.2; }
      else { a = 2 * Math.PI * rnd(); r = s0 * (0.8 + 0.6 * rnd()); }
      px[u] = bx + r * Math.cos(a); py[u] = by + r * Math.sin(a); done[u] = 1;
    }
  }
  const jit = rnd => (rnd() - 0.5) * 0.5;
  function rebuild(fresh) {
    st.dirty = false;
    const g = kind === "nbr" ? buildNbr() : kind === "mod" ? buildMod() : buildAll();
    const oldIds = st.ids, oldN = oldIds.length, ox = S.x, oy = S.y, ofx = S.fx, ofy = S.fy, ofix = S.fixed;
    if (!g.ids) {
      for (let u = 0; u < oldN; u++) loc[oldIds[u]] = -1;
      st.ids = new Int32Array(0); st.dim = new Uint8Array(0); st.level = new Uint8Array(0); st.byDeg = new Int32Array(0);
      S.load(0, [], [], [], [], []); S.alpha = 0;
      st.msg = g.msg || ""; st.info = ""; st.centre = -1;
      st.arrows = []; st.arrowsMore = 0; st.arrowsMoreAl = 0; st.dirInfo = ""; st.extraFrom = 0; st.nRel = 0;
      showText(); req();
      return;
    }
    const ids = Int32Array.from(g.ids), n = ids.length;
    const px = new Float32Array(n), py = new Float32Array(n), keep = new Uint8Array(n), old = new Int32Array(n).fill(-1);
    let kept = 0;
    if (!fresh) for (let u = 0; u < n; u++) { const o = loc[ids[u]]; if (o >= 0) { old[u] = o; px[u] = ox[o]; py[u] = oy[o]; keep[u] = 1; kept++; } }
    for (let u = 0; u < oldN; u++) loc[oldIds[u]] = -1;
    for (let u = 0; u < n; u++) { loc[ids[u]] = u; nloc[ids[u]] = -1; }
    place(g, px, py, keep);
    S.load(n, px, py, g.springs.ea, g.springs.eb, g.springs.ec);
    for (let u = 0; u < n; u++) if (old[u] >= 0 && (ofix[old[u]] & 1)) { S.fixed[u] = 1; S.fx[u] = ofx[old[u]]; S.fy[u] = ofy[old[u]]; }
    if (g.centre >= 0) { const c = g.centre; S.fixed[c] |= 4; S.fx[c] = S.x[c]; S.fy[c] = S.y[c]; }
    st.ids = ids; st.dim = g.dim ? Uint8Array.from(g.dim) : new Uint8Array(n); st.level = g.level ? Uint8Array.from(g.level) : new Uint8Array(n);
    st.centre = g.centre; st.info = g.info || ""; st.msg = ""; st.src = g.springs.src; st.sev = Uint8Array.from(g.springs.ev || []);
    st.nRel = g.springs.nRel != null ? g.springs.nRel : g.springs.ea.length; st.extraFrom = g.extraFrom != null ? g.extraFrom : n;
    const order = Array.from({length: n}, (_, u) => u);
    order.sort((a, b) => (st.dim[a] - st.dim[b]) || (S.deg[b] - S.deg[a]));
    st.byDeg = Int32Array.from(order);
    const most = kept >= 0.6 * n;
    S.alpha = most ? 0.5 : (kind === "all" ? 0.3 : 1);
    if (fresh || !most) {
      st.follow = false;
      st.autoFit = !(kind === "all" && sel >= 0 && sel < N);
      if (kind === "all") st.centreSel = sel >= 0 && sel < N;
    }
    st.groupsDirty = true;
    computeArrows();
    showText(); req();
  }
  // the probable-direction arrows between the genes shown: one per ordered pair, its strongest row (rows in ORDER);
  // past MAXA pairs the cap rule (rule 1), on the pairs in the order of their strongest rows: the MAXA strongest, and
  // any of the MAXA strongest without an alert that come after them; the rest are counted (with their alerts)
  function computeArrows() {
    st.arrows = []; st.arrowsMore = 0; st.arrowsMoreAl = 0; st.dirInfo = "";
    const n = st.ids.length;
    if (!HAS_DIR || !st.dir || !n) return;
    const seen = new Map(), MAXA = 3000, cnt = [0, 0, 0], cands = [];
    for (let u = 0; u < n; u++) for (const k of dirRowsOf(st.ids[u], "dn")) {
      const te = DR.r[k * DW + 3], v = te >= 0 ? loc[te] : -1;
      if (v < 0 || v === u) continue;
      const key = u * n + v, o = seen.get(key);
      if (o) { o.n++; if (k < o.k) o.k = k; continue; }
      const a = {u: u, v: v, k: k, n: 1, rev: false};
      seen.set(key, a); cands.push(a);
    }
    cands.sort((p, q) => p.k - q.k);
    let clean = 0;
    const drawn = new Set();
    for (let t = 0; t < cands.length; t++) {
      const a = cands[t], al = dirAlert(a.k), kgs = DR.r[a.k * DW];
      if (t < MAXA || (!al && clean < MAXA)) {
        a.gi = (kgs >> 4) & 3; a.sign = ((kgs >> 6) & 3) - 1;
        st.arrows.push(a); cnt[a.gi]++; drawn.add(a.u * n + a.v);
      } else { st.arrowsMore++; if (al) st.arrowsMoreAl++; }
      if (!al) clean++;
    }
    for (const a of st.arrows) a.rev = drawn.has(a.v * n + a.u);
    // the selected gene's direction rows whose other gene is not shown here
    let out = 0, tot = 0;
    if (sel >= 0) for (const which of ["up", "dn"]) for (const k of dirRowsOf(sel, which)) {
      tot++;
      if (!dirOthers(dirRow(k), sel).some(j => loc[j] >= 0)) out++;
    }
    const added = st.ids.length - st.extraFrom, nce = sel >= 0 ? dirRowsOf(sel, "ce").length : 0;
    const capped = st.arrows.length > MAXA ? " (the " + fmtN(MAXA) + " strongest pairs, then the strongest without " + ALERT_S + " after them)" : "";
    st.dirInfo = "<br><span style='color:" + DIRC_T + "'>Probable direction</span>: " + (st.arrows.length ? fmtN(st.arrows.length) + " arrow" + (st.arrows.length === 1 ? "" : "s") +
      " between these genes (grade " + DR.grades.map((g, t) => g + " " + fmtN(cnt[t])).join(", ") + ")" + capped : "no arrow between these genes") +
      (st.arrowsMore ? "; <span class='alc'>" + esc(dirMoreText(st.arrowsMore, st.arrowsMoreAl, "pairs")) + " not drawn (too many to read; each gene's side panel lists its rows)</span>" : "") +
      (added > 0 ? "; " + fmtN(added) + " of its probable up- and downstream genes added (violet ring: held by a link that is no relation)" : "") +
      (out ? "; " + fmtN(out) + " of its " + fmtN(tot) + " gene rows point to genes not shown here" : "") + (nce ? "; its " + fmtN(nce) + " cells row" + (nce === 1 ? "" : "s") : "") + (out || nce ? " (side panel)" : "");
  }
  function showText() {
    msgEl.innerHTML = st.msg ? "<div>" + st.msg + "</div>" : ""; msgEl.classList.toggle("on", !!st.msg);
    let key = "";
    if (S.n) {
      const it = s => "<span class='it'>" + s + "</span> ";
      key = "<div class='ky'>" + it("<span class='key' style='border-color:" + WITH + "'></span>moves with") +
        it(S.oppRepel ? "<span class='keyd' style='border-color:" + OPP + "'></span>moves opposite: pushes apart" : "<span class='key' style='border-color:" + OPP + "'></span>moves opposite: pulls together") +
        it("thickness = |cos|") + (st.colour === 1 ? it("<span class='sw' style='background:" + ARMC["+"] + "'></span> + arm") +
        it("<span class='sw' style='background:" + ARMC["-"] + "'></span> &minus; arm") : "") + "</div>";
    }
    if (S.n && st.dir) key += "<div class='ky'>" + dirKey() + "</div>";
    itxt.innerHTML = st.info ? st.info + (st.dir ? st.dirInfo : "") + key : "";
    infoEl.classList.toggle("none", !st.info && kind !== "mod");
    st.infoH = infoEl.classList.contains("none") ? 0 : infoEl.offsetHeight;
  }

  // ---------------------------------------------------------------- view
  function computeFit() {
    const n = S.n, x = S.x, y = S.y, top = (st.infoH ? st.infoH + 10 : 0) + 22, bot = 26, side = 24;
    if (!n) return {k: 1, tx: W / 2, ty: H / 2};
    let x0 = Infinity, x1 = -Infinity, y0 = Infinity, y1 = -Infinity;
    if (n > 3000) {                                            // robust bounds from a sample
      const step = Math.ceil(n / 3000), xs = [], ys = [];
      for (let u = 0; u < n; u += step) { xs.push(x[u]); ys.push(y[u]); }
      xs.sort((a, b) => a - b); ys.sort((a, b) => a - b);
      x0 = quant(xs, .01); x1 = quant(xs, .99); y0 = quant(ys, .01); y1 = quant(ys, .99);
    } else for (let u = 0; u < n; u++) { const a = x[u], b = y[u]; if (a < x0) x0 = a; if (a > x1) x1 = a; if (b < y0) y0 = b; if (b > y1) y1 = b; }
    const w = Math.max(x1 - x0, S.s0 * 3), h = Math.max(y1 - y0, S.s0 * 3);
    const k = Math.max(0.002, Math.min(3, (W - 2 * side) / w, (H - top - bot) / h));
    fitK = k;
    return (lastFit = {k: k, tx: W / 2 - (x0 + x1) / 2 * k, ty: top + (H - top - bot) / 2 - (y0 + y1) / 2 * k});
  }
  function resize() {
    const r = wrapEl.getBoundingClientRect();
    if (r.width < 2 || r.height < 2) return;
    DPR = window.devicePixelRatio || 1;
    const w0 = W, h0 = H;
    W = r.width; H = r.height;
    cvs.width = Math.round(W * DPR); cvs.height = Math.round(H * DPR);
    if (!sized) { sized = true; Object.assign(T, computeFit()); Object.assign(V, T); }
    else if (!st.autoFit && !st.follow) { const dx = (W - w0) / 2, dy = (H - h0) / 2; V.tx += dx; V.ty += dy; T.tx += dx; T.ty += dy; }
    if (visible()) req();
  }
  new ResizeObserver(resize).observe(wrapEl);
  const SX = u => S.x[u] * V.k + V.tx, SY = u => S.y[u] * V.k + V.ty;
  // node radius: grows a little when zoomed in; smaller when there are many genes
  const nodeR = () => kind === "all" ? Math.max(1.6, Math.min(5, 2.2 * Math.pow(V.k / fitK, 0.4))) :
    Math.max(2.2, Math.min(9, 5 * Math.min(1, Math.sqrt(300 / Math.max(1, S.n))) * Math.pow(V.k / fitK, 0.3)));
  function centreSel() {
    st.centreSel = false;
    const u = sel >= 0 ? loc[sel] : -1;
    if (u < 0 || !sized) return;
    let far = 0;
    for (let p = S.off[u]; p < S.off[u + 1]; p++) {
      const k = S.adj[p], v = S.ea[k] === u ? S.eb[k] : S.ea[k];
      far = Math.max(far, Math.abs(S.x[v] - S.x[u]), Math.abs(S.y[v] - S.y[u]));
    }
    const f = computeFit(), k = far > 0 ? Math.min(f.k * 60, Math.max(f.k * 2, 0.4 * Math.min(W, H) / far)) : f.k * 6;
    T.k = k; T.tx = W / 2 - S.x[u] * k; T.ty = H / 2 - S.y[u] * k;
    st.autoFit = false; st.follow = true;
  }

  // ---------------------------------------------------------------- frame: simulation steps within a time budget, then draw
  // at most TPS steps a second, whatever the size: alpha cools from a re-heat (0.8) in ~290 steps, so a small
  // simulation (cheap steps) plays the sign switch or a re-heat over ~2.4 s instead of settling in a few frames
  const BUDGET = 13, MAXT = 12, TPS = 120;
  function frame(now) {
    if (!sized) resize();
    const run = S.moving() && !st.paused;
    if (run) {
      st.frames.push(now);
      while (st.frames.length > 2 && st.frames[0] < now - 1000) st.frames.shift();
      st.debt = Math.min(MAXT, st.debt + (st.lastRun ? Math.min(100, now - st.lastRun) : 1000 / 60) * TPS / 1000);
      st.lastRun = now;
      // several steps per frame when fast (up to the TPS allowance); one step every other frame when one step takes
      // longer than ~3 frames
      if (st.debt >= 1 && (st.avgTick < 45 || (st.skip ^= 1))) {
        const t0 = performance.now();
        let k = 0;
        do { S.tick(); k++; } while (k < MAXT && k + 1 <= st.debt && performance.now() - t0 + st.avgTick < BUDGET);
        st.debt = Math.max(0, st.debt - k);
        const dt = (performance.now() - t0) / k;
        st.avgTick = st.avgTick ? 0.8 * st.avgTick + 0.2 * dt : dt; st.tpf = k;
      }
    } else { st.frames.length = 0; st.lastRun = 0; st.debt = 0; }
    const f = computeFit();
    if (st.autoFit) Object.assign(T, f);
    let moving = false;
    for (const key of ["k", "tx", "ty"]) {
      const d = T[key] - V[key];
      if (Math.abs(d) > (key === "k" ? V.k * 1e-3 : 0.3)) { V[key] += d * 0.25; moving = true; } else V[key] = T[key];
    }
    if (st.follow && sel >= 0 && loc[sel] >= 0) {               // keep the selected gene where it is on the screen ...
      const u = loc[sel];
      let far = 0;                                               // ... and zoom out when its partners drift out of view
      for (let p = S.off[u]; p < S.off[u + 1]; p++) {
        const k = S.adj[p], v = S.ea[k] === u ? S.eb[k] : S.ea[k];
        far = Math.max(far, Math.abs(S.x[v] - S.x[u]), Math.abs(S.y[v] - S.y[u]));
      }
      if (far > 0) T.k = Math.max(f.k, Math.min(T.k, 0.45 * Math.min(W, H) / far));
      T.tx = W / 2 - S.x[u] * T.k; T.ty = H / 2 - S.y[u] * T.k;
      if (!moving) { V.tx = T.tx; V.ty = T.ty; }
    }
    if (st.groupsDirty && kind === "all") makeGroups();
    const t1 = performance.now();
    draw();
    st.drawMs = performance.now() - t1;
    if (!run || now - st.lastStatus > 300) status();
    return run || moving;
  }
  function makeGroups() {
    st.groupsDirty = false;
    const g = new Map(), n = S.n, u0 = sel >= 0 ? loc[sel] : -1, near = new Set();
    if (u0 >= 0) for (let p = S.off[u0]; p < S.off[u0 + 1]; p++) { const k = S.adj[p]; near.add(S.ea[k] === u0 ? S.eb[k] : S.ea[k]); }
    for (let u = 0; u < n; u++) {
      const i = st.ids[u];
      let a = 1;
      if (hlMod >= 0 && D.mod[i] !== hlMod) a = 0.13;
      if (u0 >= 0 && u !== u0 && !near.has(u)) a = Math.min(a, 0.45);
      const c = nodeColour(i), key = a + c;
      let e = g.get(key);
      if (!e) { e = {c: c, a: a, idx: []}; g.set(key, e); }
      e.idx.push(u);
    }
    st.groups = [...g.values()].sort((p, q) => (p.a - q.a) || ((q.c === GREY) - (p.c === GREY)));
    for (const e of st.groups) e.idx = Int32Array.from(e.idx);
  }
  function selNeighbours() {                                    // [node, cos] of the selected gene's springs, strongest first
    const u = sel >= 0 ? loc[sel] : -1, out = [];
    if (u < 0) return out;
    for (let p = S.off[u]; p < S.off[u + 1]; p++) { const k = S.adj[p]; if (k < st.nRel) out.push([S.ea[k] === u ? S.eb[k] : S.ea[k], S.ec[k]]); }
    return out.sort((a, b) => Math.abs(b[1]) - Math.abs(a[1]));
  }
  function draw() {
    const n = S.n;
    g2.setTransform(1, 0, 0, 1, 0, 0);
    if (layer) layer(S.x || [], S.y || [], 1, n ? st.groups : null, V.k, V.tx, V.ty, DPR, nodeR());
    else { g2.fillStyle = SURF; g2.fillRect(0, 0, cvs.width, cvs.height); }
    g2.setTransform(DPR, 0, 0, DPR, 0, 0);
    if (!n) return;
    const r = nodeR(), nb = selNeighbours();
    if (kind !== "all") { drawEdges(); drawArrowsP(r); drawNodes(r); }
    else drawSelected(r, nb);
    if (kind === "mod") drawArmLabels(r);
    drawLabels(r, nb);
    if (st.hover >= 0 && st.hover < n) {
      g2.beginPath(); g2.arc(SX(st.hover), SY(st.hover), r + 3, 0, 2 * Math.PI);
      g2.lineWidth = 1.5; g2.strokeStyle = INK; g2.stroke();
    }
  }
  function drawArrowsP(r) {
    if (!st.dir || !st.arrows.length) return;
    const u0 = sel >= 0 ? loc[sel] : -1, ab = ArrowBatch();     // the selected gene's arrows on top, the others paler
    for (const a of st.arrows) {
      const X0 = SX(a.u), Y0 = SY(a.u), X1 = SX(a.v), Y1 = SY(a.v);
      if ((X0 < -20 && X1 < -20) || (Y0 < -20 && Y1 < -20) || (X0 > W + 20 && X1 > W + 20) || (Y0 > H + 20 && Y1 > H + 20)) continue;
      ab.add(X0, Y0, X1, Y1, (a.u === u0 ? r + 3 : r) + 1.5, (a.v === u0 ? r + 3 : r) + 2.5, a.gi, headSign(a), u0 >= 0 && a.u !== u0 && a.v !== u0, a.rev ? 3 : 0);
    }
    ab.draw(g2);
  }
  function drawEdges() {
    const m = Math.min(S.m, st.nRel), ea = S.ea, eb = S.eb, ec = S.ec, dim = st.dim, paths = [];
    const dens = Math.max(0.08, Math.min(1, Math.sqrt(160 / Math.max(1, m))));   // many edges: each one lighter
    for (let b = 0; b < 16; b++) paths.push(null);
    for (let e = 0; e < m; e++) {
      const a = ea[e], b = eb[e], c = ec[e], wb = Math.min(3, Math.floor(Math.abs(c) * 4));
      const bk = ((dim[a] || dim[b]) ? 8 : 0) + (c < 0 ? 4 : 0) + wb;
      const p = paths[bk] || (paths[bk] = new Path2D());
      p.moveTo(SX(a), SY(a)); p.lineTo(SX(b), SY(b));
    }
    g2.lineCap = "round";
    for (let bk = 0; bk < 16; bk++) {
      if (!paths[bk]) continue;
      const dimmed = bk >= 8, neg = (bk & 4) !== 0, w = ((bk & 3) + 0.5) / 4, push = neg && S.oppRepel;
      g2.strokeStyle = neg ? OPP : WITH;
      g2.lineWidth = push ? 0.3 + 1.8 * w : 0.35 + 3 * w;    // thickness proportional to |cos|; pushers thinner
      g2.globalAlpha = dimmed ? 0.14 : dens * (push ? 0.1 + 0.25 * w : 0.3 + 0.5 * w);
      g2.setLineDash(push ? [5, 4] : []);
      g2.stroke(paths[bk]);
    }
    g2.setLineDash([]); g2.globalAlpha = 1;
  }
  function drawNodes(r0) {
    const n = S.n, ids = st.ids, dim = st.dim, fixed = S.fixed;
    for (let pass = 0; pass < 2; pass++) for (let u = 0; u < n; u++) {
      if ((dim[u] ? 0 : 1) !== pass) continue;
      const i = ids[u], X = SX(u), Y = SY(u);
      if (X < -20 || Y < -20 || X > W + 20 || Y > H + 20) continue;
      const r = i === sel ? r0 + 3 : (pset.has(i) && kind === "nbr") ? r0 + 1 : r0;
      g2.beginPath(); g2.arc(X, Y, r, 0, 2 * Math.PI);
      g2.globalAlpha = dim[u] ? 0.5 : 1;
      g2.fillStyle = dim[u] ? GREY : nodeColour(i); g2.fill();
      if (n < 800) { g2.lineWidth = 1; g2.strokeStyle = SURF; g2.stroke(); }
      g2.globalAlpha = 1;
      if (fixed[u] & 5) { g2.beginPath(); g2.arc(X, Y, r + (i === sel ? 4.5 : 2.2), 0, 2 * Math.PI); g2.lineWidth = 1.6; g2.strokeStyle = INK2; g2.stroke(); }
      if (u >= st.extraFrom) { g2.beginPath(); g2.arc(X, Y, r + 1.2, 0, 2 * Math.PI); g2.lineWidth = 2; g2.strokeStyle = DIRC; g2.stroke(); }
      if (i === sel) { g2.beginPath(); g2.arc(X, Y, r + 1, 0, 2 * Math.PI); g2.lineWidth = 2.5; g2.strokeStyle = INK; g2.stroke(); }
    }
  }
  function drawSelected(r, nb) {                                // all-genes tab: edges only for the selected gene
    const u0 = sel >= 0 ? loc[sel] : -1;
    if (u0 < 0) return;
    const X0 = SX(u0), Y0 = SY(u0);
    for (const [v, c] of nb) {
      const a = Math.abs(c);
      g2.strokeStyle = c > 0 ? WITH : OPP; g2.globalAlpha = 0.35 + 0.55 * a; g2.lineWidth = 0.6 + 2.6 * a;
      g2.setLineDash(c < 0 && S.oppRepel ? [5, 4] : []);
      g2.beginPath(); g2.moveTo(X0, Y0); g2.lineTo(SX(v), SY(v)); g2.stroke();
    }
    g2.setLineDash([]); g2.globalAlpha = 1;
    for (const [v, c] of nb) {
      g2.beginPath(); g2.arc(SX(v), SY(v), r + 1.5, 0, 2 * Math.PI);
      g2.fillStyle = nodeColour(st.ids[v]); g2.fill(); g2.lineWidth = 2; g2.strokeStyle = c > 0 ? WITH : OPP; g2.stroke();
    }
    for (let u = 0; u < S.n; u++) if (S.fixed[u] & 5) { g2.beginPath(); g2.arc(SX(u), SY(u), r + 2.2, 0, 2 * Math.PI); g2.lineWidth = 1.6; g2.strokeStyle = INK2; g2.stroke(); }
    g2.beginPath(); g2.arc(X0, Y0, r + 4, 0, 2 * Math.PI);
    g2.fillStyle = nodeColour(sel); g2.fill(); g2.lineWidth = 2.5; g2.strokeStyle = INK; g2.stroke();
  }
  function armSplit() {                                       // per arm: [sum x, sum y, n, sum x^2 + y^2, top screen y]
    const s = {"+": [0, 0, 0, 0, Infinity], "-": [0, 0, 0, 0, Infinity]};
    for (let u = 0; u < S.n; u++) {
      if (st.dim[u]) continue;
      const v = s[D.arm[st.ids[u]]];
      if (!v) continue;
      const x = S.x[u], y = S.y[u], Y = SY(u);
      v[0] += x; v[1] += y; v[2]++; v[3] += x * x + y * y; if (Y < v[4]) v[4] = Y;
    }
    return s;
  }
  function drawArmLabels(r) {
    // "+ arm" / "- arm" over each arm, once the two arms have parted (centroids further apart than the arms are wide)
    const md = MODS.get(st.module);
    if (!md || !md.opp) return;
    const s = armSplit(), p = s["+"], m = s["-"];
    if (p[2] < 2 || m[2] < 2) return;
    const c = v => [v[0] / v[2], v[1] / v[2]], sd = v => { const q = c(v); return Math.sqrt(Math.max(0, v[3] / v[2] - q[0] * q[0] - q[1] * q[1])); };
    const cp = c(p), cm = c(m);
    if (Math.hypot(cp[0] - cm[0], cp[1] - cm[1]) < 1.3 * (sd(p) + sd(m)) / 2) return;
    g2.textAlign = "center"; g2.textBaseline = "middle";
    halo(g2, "+ arm (" + p[2] + ")", cp[0] * V.k + V.tx, Math.max(14, p[4] - r - 14), "700 13px " + FF, ARMC["+"]);
    halo(g2, "− arm (" + m[2] + ")", cm[0] * V.k + V.tx, Math.max(14, m[4] - r - 14), "700 13px " + FF, ARMC["-"]);
  }
  function drawLabels(r, nb) {
    const n = S.n, label = Labeler(g2), seen = new Uint8Array(n), ids = st.ids;
    g2.textAlign = "left"; g2.textBaseline = "middle";
    const zoom = V.k / fitK, everyone = kind === "all" ? zoom > 5 : (n <= 150 || zoom > 1.8);
    let placed = 0;
    const put = (u, font, colour, hgt) => {
      if (seen[u] || placed > 450) return;
      seen[u] = 1;
      const X = SX(u), Y = SY(u);
      if (X < -40 || Y < -10 || X > W || Y > H + 10) return;
      if (label(D.sym[ids[u]], X + r + 4, Y, font, colour, hgt)) placed++;
    };
    const u0 = sel >= 0 ? loc[sel] : -1;
    if (u0 >= 0) put(u0, "700 13px " + FF, INK, 15);
    for (const [v, c] of nb) put(v, "600 11px " + FF, c > 0 ? WITH_T : OPP_T, 12);
    for (let u = st.extraFrom; u < n; u++) put(u, "600 11px " + FF, DIRC_T, 12);
    if (st.dir && u0 >= 0) for (const a of st.arrows) if (a.u === u0 || a.v === u0) put(a.u === u0 ? a.v : a.u, "600 11px " + FF, DIRC_T, 12);
    if (st.hover >= 0 && st.hover < n) put(st.hover, "600 11px " + FF, INK, 12);
    for (let u = 0; u < n; u++) if (S.fixed[u] & 5) put(u, "600 11px " + FF, INK2, 12);
    if (everyone) for (const u of st.byDeg) { if (placed > 450) break; put(u, "11px " + FF, st.dim[u] ? "#a3a29b" : INK2, 12); }
  }

  // ---------------------------------------------------------------- status line and tooltip
  function fps() { const f = st.frames; return f.length > 2 ? (f.length - 1) * 1000 / (f[f.length - 1] - f[0]) : 0; }
  function status() {
    st.lastStatus = performance.now();
    if (!S.n) { statusEl.textContent = ""; return; }
    const s = [S.n.toLocaleString() + " genes", st.nRel.toLocaleString() + " springs" + (S.m > st.nRel ? " + " + (S.m - st.nRel) + " direction links" : ""),
      st.paused ? "paused" : S.moving() ? "moving (alpha " + S.alpha.toFixed(2) + ")" : "settled"];
    const f = fps();
    if (f && !st.paused && S.moving()) s.push(Math.round(f) + " frames/s, " + st.tpf + " step" + (st.tpf === 1 ? "" : "s") + " per frame");
    s.push("drag a gene = move it, double-click = pin, click = select, wheel = zoom");
    statusEl.textContent = s.join("  ·  ");
  }
  function springOf(a, b) {                                   // [cos, evidence code] of the spring a-b, or null
    if (a < 0 || b < 0) return null;
    for (let p = S.off[a]; p < S.off[a + 1]; p++) { const k = S.adj[p]; if (k < st.nRel && (S.ea[k] === a ? S.eb[k] : S.ea[k]) === b) return [S.ec[k], st.sev && k < st.sev.length ? st.sev[k] : 2]; }
    return null;
  }
  function showTipP(u, mx, my) {
    const i = st.ids[u];
    let h = tipHtml(i);
    if (sel >= 0 && i !== sel) {
      const sp = springOf(loc[sel], u), c = sp ? sp[0] : null;
      if (c != null) h += "<br>" + (c > 0 ? "moves with " : "moves opposite to ") + esc(D.sym[sel]) + " (cos " + (c > 0 ? "+" : "") + c.toFixed(2) + ")" +
        (sp[1] < 2 ? " <span class='alc'>&#9888; " + EV_ALERT[sp[1]] + "</span>" : "");
    }
    if (st.dim[u]) h += "<br><span class='m'>outside the module</span>";
    if (st.dir) h += dirTip(i);
    if (u >= st.extraFrom) h += "<br><span class='m' style='color:" + DIRC_T + "'>added for its probable direction (no relation spring)</span>";
    h += "<br><span class='m'>" + ((S.fixed[u] & 5) ? "pinned: double-click to unpin" : "drag to move, double-click to pin") + "</span>";
    placeTip(tipEl, h, mx, my, W, H);
  }
  const hideTipP = () => { tipEl.style.display = "none"; };

  // ---------------------------------------------------------------- pointer: drag a gene, pan, zoom, click, double-click
  function hit(mx, my) {
    const n = S.n, r = Math.max(7, nodeR() + 3);
    let best = -1, bd = r * r;
    for (let u = 0; u < n; u++) {
      const dx = SX(u) - mx, dy = SY(u) - my, d = dx * dx + dy * dy;
      if (d < bd) { bd = d; best = u; }
    }
    return best;
  }
  const world = p => [(p[0] - V.tx) / V.k, (p[1] - V.ty) / V.k];
  function zoomAtP(mx, my, f, immediate) {
    const k = Math.min(fitK * 400, Math.max(fitK * 0.2, T.k * f)), g = k / T.k;
    T.tx = mx - (mx - T.tx) * g; T.ty = my - (my - T.ty) * g; T.k = k;
    if (immediate) Object.assign(V, T);
    st.autoFit = false; st.follow = false;
    req();
  }
  cvs.addEventListener("pointerdown", e => {
    cvs.setPointerCapture(e.pointerId);
    const p = local(e, cvs);
    ptrs.set(e.pointerId, p);
    downAt = p; dragged = false;
    if (ptrs.size === 2) {
      const [a, b] = [...ptrs.values()];
      pinch = {d: Math.hypot(a[0] - b[0], a[1] - b[1]), k: T.k};
      if (st.drag >= 0) { S.fixed[st.drag] &= ~2; S.alphaTarget = 0; st.drag = -1; }
      return;
    }
    const u = e.button === 0 ? hit(p[0], p[1]) : -1;
    if (u >= 0) { st.drag = u; S.fx[u] = S.x[u]; S.fy[u] = S.y[u]; S.fixed[u] |= 2; }
    cvs.classList.add("drag");
  });
  cvs.addEventListener("pointermove", e => {
    const p = local(e, cvs);
    if (ptrs.has(e.pointerId)) {
      const q0 = ptrs.get(e.pointerId);
      ptrs.set(e.pointerId, p);
      if (ptrs.size === 2 && pinch) {
        const [a, b] = [...ptrs.values()], d = Math.hypot(a[0] - b[0], a[1] - b[1]);
        zoomAtP((a[0] + b[0]) / 2, (a[1] + b[1]) / 2, (pinch.k * d / Math.max(pinch.d, 1)) / T.k, true);
        dragged = true;
        return;
      }
      if (Math.abs(p[0] - downAt[0]) + Math.abs(p[1] - downAt[1]) > 3) dragged = true;
      if (st.drag >= 0) {
        if (!dragged) return;
        const u = st.drag, w = world(p);
        S.fx[u] = w[0]; S.fy[u] = w[1];
        if (st.paused) { S.x[u] = w[0]; S.y[u] = w[1]; }
        else { S.alphaTarget = 0.3; S.heat(0.15); }
        st.autoFit = false;
        hideTipP(); req();
        return;
      }
      const dx = p[0] - q0[0], dy = p[1] - q0[1];
      V.tx += dx; V.ty += dy; T.tx += dx; T.ty += dy;
      st.autoFit = false; st.follow = false;
      hideTipP(); req();
      return;
    }
    const u = hit(p[0], p[1]);
    if (u !== st.hover) { st.hover = u; cvs.classList.toggle("onnode", u >= 0); req(); }
    if (u >= 0) showTipP(u, p[0], p[1]); else hideTipP();
  });
  function endP(e) {
    ptrs.delete(e.pointerId);
    if (ptrs.size < 2) pinch = null;
    if (ptrs.size === 0) cvs.classList.remove("drag");
  }
  cvs.addEventListener("pointerup", e => {
    const wasDrag = dragged, u = st.drag;
    endP(e);
    if (u >= 0) { S.fixed[u] &= ~2; S.alphaTarget = 0; st.drag = -1; req(); }
    if (e.button !== 0) return;
    // every press-release is kept, a micro-drag too (the browser may count it as one click of a double-click): the
    // double-click then pins the gene of its own first click, not that of an earlier click
    const i = u >= 0 ? st.ids[u] : -1;
    prevClick = lastClick; lastClick = {id: i, t: performance.now(), pinned: u >= 0 && (S.fixed[u] & 5) !== 0};
    if (!wasDrag) {
      if (i >= 0 && i !== sel) {
        clearTimeout(clickTimer);
        const g0 = selGen;                                       // wait: a double-click pins instead; any other
        clickTimer = setTimeout(() => { if (selGen === g0) select(i, false, kind); }, DBL_MS);   // selection meanwhile wins
      }
    }
  });
  cvs.addEventListener("pointercancel", e => { endP(e); if (st.drag >= 0) { S.fixed[st.drag] &= ~2; S.alphaTarget = 0; st.drag = -1; } });
  cvs.addEventListener("pointerleave", () => { if (st.hover >= 0) { st.hover = -1; req(); } hideTipP(); });
  cvs.addEventListener("dblclick", e => {
    clearTimeout(clickTimer);                                    // the second click selects nothing (no re-centring)
    const p = local(e, cvs);
    // the gene of the double-click's first click, wherever it is now (its selection may have rebuilt the view)
    const c = prevClick && lastClick && lastClick.t - prevClick.t < 1000 && performance.now() - lastClick.t < 1000 ? prevClick : null;
    prevClick = lastClick = null;
    const u = c ? (c.id >= 0 ? loc[c.id] : -1) : hit(p[0], p[1]);
    if (u < 0) { zoomAtP(p[0], p[1], 2, false); return; }
    if (c ? c.pinned : (S.fixed[u] & 5)) S.fixed[u] &= ~5;      // pinned (by you, or the centre) before: unpin
    else { S.fixed[u] = (S.fixed[u] & ~4) | 1; S.fx[u] = S.x[u]; S.fy[u] = S.y[u]; }   // else pinned by you
    S.heat(0.1); setPaused(false); req();
    if (st.hover === u) showTipP(u, p[0], p[1]);
  });
  cvs.addEventListener("wheel", e => {
    e.preventDefault();
    const [mx, my] = local(e, cvs), dy = e.deltaMode === 1 ? e.deltaY * 33 : e.deltaY;
    zoomAtP(mx, my, Math.exp(-dy * 0.0016), false);
    hideTipP();
  }, {passive: false});

  // ---------------------------------------------------------------- controls
  function segSet(k, on, nb) { for (let t = 0; t < nb; t++) { const b = q(k + t); if (b) b.setAttribute("aria-pressed", t === on); } }
  function setPaused(p) {
    st.paused = p;
    const b = q("pause");
    b.textContent = p ? "Resume" : "Pause"; b.setAttribute("aria-pressed", p);
    status(); req();
  }
  function setOpp(rep) {
    S.oppRepel = rep; segSet("opp", rep ? 1 : 0, 2);
    S.heat(kind === "all" ? 0.5 : 0.8); setPaused(false); showText(); req();
  }
  function setModule(m) {
    if (!MODS.has(m)) return;
    if (m !== st.module) { st.module = m; st.dirty = true; }
    syncPicker();
    if (m !== hlMod) highlight(m);                             // the side panel shows the module card
    if (st.dirty && visible()) rebuild(false);
  }
  function syncPicker() {
    const s = q("msel");
    if (!s) return;
    if (!s.options.length) s.innerHTML = D.mods.map(m => "<option value='" + m.id + "'>" + esc("M" + m.id + " · " + (m.label.length > 48 ? m.label.slice(0, 46) + "…" : m.label) + " (" + m.n + ")") + "</option>").join("");
    s.value = String(st.module);
  }
  pane.addEventListener("click", e => {
    const b = e.target.closest("button[data-k]");
    if (!b) return;
    const k = b.dataset.k;
    if (k === "opp0" || k === "opp1") setOpp(k === "opp1");
    else if (k === "col0" || k === "col1") { st.colour = k === "col1" ? 1 : 0; segSet("col", st.colour, 2); st.groupsDirty = true; showText(); req(); }
    else if (k === "pause") setPaused(!st.paused);
    else if (k === "heat") { S.heat(kind === "all" ? 0.5 : 0.8); setPaused(false); }
    else if (k === "reset") { rebuild(true); st.autoFit = true; st.follow = false; setPaused(false); }
    else if (k === "fit") { st.autoFit = true; st.follow = false; req(); }
    else if (/^dep[0-3]$/.test(k)) { st.depth = +k.slice(3) + 1; segSet("dep", st.depth - 1, 4); rebuild(false); }
    else if (/^dir[0-2]$/.test(k) && HAS_DIR) { const m = +k.slice(3), was = st.dir; st.dir = m; segSet("dir", m, 3); if ((m === 2) !== (was === 2)) rebuild(false); else { computeArrows(); showText(); req(); } }
    else if (k === "mselg") { if (sel >= 0 && sel < N && D.mod[sel] > 0) setModule(D.mod[sel]); }
  });
  const out = (k, v) => { const o = q(k + "o"); if (o) o.textContent = v; };
  const sliders = () => {
    S.rep = +q("rep").value; S.spr = +q("spr").value / 100; st.minCos = +q("min").value / 100;
    out("rep", S.rep); out("spr", S.spr.toFixed(1) + "×"); out("min", st.minCos.toFixed(2));
    if (q("max")) out("max", q("max").value);
  };
  sliders();
  q("rep").addEventListener("input", () => { sliders(); S.heat(0.3); setPaused(false); });
  q("spr").addEventListener("input", () => { sliders(); S.heat(0.3); setPaused(false); });
  q("min").addEventListener("input", sliders);
  q("min").addEventListener("change", () => { sliders(); rebuild(false); });
  q("ev").addEventListener("change", () => { st.ev = +q("ev").value; rebuild(false); });
  if (q("max")) {
    q("max").addEventListener("input", sliders);
    q("max").addEventListener("change", () => { st.maxN = Math.max(20, Math.min(2000, +q("max").value || 300)); q("max").value = st.maxN; sliders(); rebuild(false); });
  }
  if (q("msel")) q("msel").addEventListener("change", () => setModule(+q("msel").value));
  if (!HAS_DIR) for (let t = 0; t < 3; t++) { const b = q("dir" + t); if (b) { b.disabled = true; b.title = "Not available: this output has no direction stage"; } }
  if (q("ring")) q("ring").addEventListener("change", () => { st.ring = q("ring").checked; rebuild(false); });

  // ---------------------------------------------------------------- the rest of the page talks to the tab through these
  return {
    frame: frame,
    show: () => {
      resize();
      const first = !S.n && !st.msg;
      if (st.dirty || first) rebuild(st.fresh);
      st.fresh = false;
      if (first) { Object.assign(T, computeFit()); Object.assign(V, T); }
      if (kind === "all" && st.centreSel) { centreSel(); Object.assign(V, T); }
      showText(); status(); req();
    },
    onSelect: origin => {
      if (kind === "nbr") st.dirty = true;
      else if (kind === "mod") {
        if (origin !== "mod" && sel >= 0 && sel < N && D.mod[sel] > 0 && D.mod[sel] !== st.module) { st.module = D.mod[sel]; st.dirty = true; syncPicker(); }
      } else if (origin !== "all") st.centreSel = sel >= 0 && sel < N;
      st.groupsDirty = true;
      if (visible()) { if (st.dirty) rebuild(false); if (st.centreSel) centreSel(); req(); }
    },
    onHighlight: m => {
      if (kind === "mod" && m > 0 && m !== st.module && MODS.has(m)) { st.module = m; st.dirty = true; syncPicker(); }
      st.groupsDirty = true;
      if (visible()) { if (st.dirty) rebuild(false); req(); }
    },
    togglePause: () => setPaused(!st.paused),
    state: () => ({kind: kind, n: S.n, m: S.m, ids: Array.from(st.ids), x: Array.from(S.x || []), y: Array.from(S.y || []),
      fixed: Array.from(S.fixed || []), alpha: S.alpha, moving: S.moving(), paused: st.paused, opposite: S.oppRepel ? "repel" : "attract",
      module: st.module, depth: st.depth, msg: st.msg, springs: st.src, ticks: S.ticks}),
    screen: i => { const u = i >= 0 && i < NA ? loc[i] : -1; return u < 0 ? null : {x: SX(u), y: SY(u), w: W, h: H}; },
    stats: () => ({fps: fps(), tickMs: st.avgTick, drawMs: st.drawMs, ticksPerFrame: st.tpf, alpha: S.alpha, n: S.n, m: S.m}),
    benchTick: k => { const a = S.alpha; S.alpha = Math.max(a, 0.5); const t0 = performance.now(); for (let r = 0; r < k; r++) S.tick(); const ms = (performance.now() - t0) / k; return ms; },
    arrows: () => ({mode: st.dir, more: st.arrowsMore, moreAlert: st.arrowsMoreAl || 0, added: st.ids.length - st.extraFrom, ids: Array.from(st.ids),
      arrows: st.arrows.map(a => ({s: st.ids[a.u], t: st.ids[a.v], k: a.k, grade: DR.grades[a.gi], sign: a.sign, n: a.n, line: dirLine(dirRow(a.k))}))}),
    redir: () => { if (kind === "nbr") st.dirty = true; if (visible() && st.dirty) rebuild(false); },
  };
}

// ================================================================ the vector-space tour: the gene vectors in k dimensions
// A grand tour (Asimov; Buja et al.): the unit gene vectors (embed stage) projected onto a 2D plane that moves along
// the geodesic between random planes (principal angles of the 2 x 2 matrix Fa' Fz, a closed-form SVD), so every
// view is a true linear projection of the space; or, in axis mode, onto two of the space's axes (components).
function svd2(a, b, c, d) {                         // [[a, b], [c, d]] = R(ph) diag(s1, s2) R(th), R = rotation
  const E = (a + d) / 2, F = (a - d) / 2, G = (c + b) / 2, H = (c - b) / 2;
  const Q = Math.hypot(E, H), R = Math.hypot(F, G), a1 = Math.atan2(G, F), a2 = Math.atan2(H, E);
  return {s1: Q + R, s2: Q - R, th: (a2 - a1) / 2, ph: (a2 + a1) / 2};
}
function TourPane() {
  const pane = $("pane-tour"), TD = D.tour || {}, K = TD.k || 0, n = Math.min(N, TD.n || 0);
  const opt = labels => labels.map((l, t) => "<option value='" + t + "'>" + l + "</option>").join("");
  const axl = a => "axis " + (a + 1) + (TD.var && TD.var[a] != null ? " (" + TD.var[a] + "%)" : "");
  let h = "<div class='bars'><div class='bar'>" +
    "<span class='seg'><button data-k='play' aria-pressed='true' title='Play / pause the tour (space)'>Pause</button>" +
    "<button data-k='new' title='Turn toward a new random direction'>New direction</button></span>" +
    "<div class='grp'>View <span class='seg'><button data-k='m0' aria-pressed='true' title='A slowly rotating 2D window on the full space'>Tour</button>" +
    "<button data-k='m1' aria-pressed='false' title='Two axes of the space, chosen below'>Axes</button></span></div>" +
    "<label class='grp' title='Horizontal axis'>x <select class='tsel' data-k='ai'>" + opt(Array.from({length: K}, (_, a) => axl(a))) + "</select></label>" +
    "<label class='grp' title='Vertical axis'>y <select class='tsel' data-k='aj'>" + opt(Array.from({length: K}, (_, a) => axl(a))) + "</select></label>" +
    "<label class='rng' title='How fast the window turns (radians per second)'>Speed <input type='range' data-k='spd' min='2' max='100' step='1' value='20'><output data-k='spdo'></output></label>" +
    "<div class='grp'>Colour <span class='seg'><button data-k='c0' aria-pressed='true'>Module</button><button data-k='c1' aria-pressed='false'>Arm</button></span></div>" +
    "<button class='btn' data-k='fit' title='Undo pan and zoom'>Reset view</button></div></div>";
  h += "<div class='wrap'><canvas></canvas><div class='info'><div class='itxt'></div></div><div class='msg'></div><div class='tip'></div><div class='status'></div></div>";
  pane.innerHTML = h;
  const q = k => pane.querySelector("[data-k='" + k + "']");
  const wrapEl = pane.querySelector(".wrap"), cvs = pane.querySelector("canvas"), g2 = cvs.getContext("2d");
  const tipEl = pane.querySelector(".tip"), itxt = pane.querySelector(".itxt"), msgEl = pane.querySelector(".msg"), statusEl = pane.querySelector(".status");
  const layer = PointLayer(cvs, g2);
  const st = {mode: 0, playing: true, speed: 0.2, colour: 0, ai: 0, aj: 1, zoom: 1, panX: 0, panY: 0, rmsS: 0, hover: -1,
    frames: [], projMs: 0, drawMs: 0, last: 0, groups: null, groupsDirty: true, moves: 0};
  let W = 1, H = 1, DPR = 1, sized = false, VV = null, SCL = 1, TX = 0, TY = 0, rms = 0;
  const PXt = new Float32Array(n), PYt = new Float32Array(n);
  const F = new Float64Array(2 * K), f1 = new Float32Array(K), f2 = new Float32Array(K);
  let move = null;                                  // {len, at(t, out), t}
  const queue = [];                                 // moves still to make (axis mode: orient after the plane)
  const rnd = mulberry(20261109);
  if (K >= 2) { F[0] = 1; F[K + 1] = 1; }
  if (!K || !n) {
    msgEl.innerHTML = "<div>This run has no gene vectors to tour (embed/gene_unit.npy was not found when the map was made).</div>";
    msgEl.classList.add("on");
  }
  q("ai").value = "0"; q("aj").value = String(Math.min(1, K - 1));

  function decode() {
    if (VV || !K || !n) return;
    const Q8 = b64bytes(TD.q), sc = TD.sc || [];
    VV = new Float32Array(n * K);
    for (let i = 0, o = 0; i < n; i++) for (let a = 0; a < K; a++, o++) { const v = Q8[o]; VV[o] = (v > 127 ? v - 256 : v) * (sc[a] || 1) / 127; }
  }
  // ---------------------------------------------------------------- frames (k x 2, columns orthonormal)
  const col = (M, c, a) => M[c * K + a];
  function orth(M) {                                // Gram-Schmidt on the two columns, in place
    let s = 0;
    for (let a = 0; a < K; a++) s += M[a] * M[a];
    s = Math.sqrt(s) || 1;
    for (let a = 0; a < K; a++) M[a] /= s;
    let d = 0;
    for (let a = 0; a < K; a++) d += M[a] * M[K + a];
    for (let a = 0; a < K; a++) M[K + a] -= d * M[a];
    s = 0;
    for (let a = 0; a < K; a++) s += M[K + a] * M[K + a];
    s = Math.sqrt(s) || 1;
    for (let a = 0; a < K; a++) M[K + a] /= s;
    return M;
  }
  function gauss() { const u = Math.max(1e-12, rnd()), v = rnd(); return Math.sqrt(-2 * Math.log(u)) * Math.cos(2 * Math.PI * v); }
  function randomFrame() { const M = new Float64Array(2 * K); for (let a = 0; a < 2 * K; a++) M[a] = gauss(); return orth(M); }
  function axisFrame(i, j, sj) { const M = new Float64Array(2 * K); M[i] = 1; M[K + j] = sj || 1; return M; }
  const dot = (A, ca, B, cb) => { let s = 0; for (let a = 0; a < K; a++) s += A[ca * K + a] * B[cb * K + a]; return s; };
  function geo(Fa, Fz) {
    // the geodesic from plane Fa to plane Fz: principal directions Ga = Fa U, Gz = Fz V of Fa' Fz = U S V',
    // then F(t) = [Ga_c cos(t th_c) + Gp_c sin(t th_c)] U' (F(0) = Fa)
    const r = svd2(dot(Fa, 0, Fz, 0), dot(Fa, 0, Fz, 1), dot(Fa, 1, Fz, 0), dot(Fa, 1, Fz, 1));
    let u = [[Math.cos(r.ph), -Math.sin(r.ph)], [Math.sin(r.ph), Math.cos(r.ph)]], s2 = r.s2;
    if (s2 < 0) { s2 = -s2; u = [[u[0][0], -u[0][1]], [u[1][0], -u[1][1]]]; }
    const v = [[Math.cos(r.th), Math.sin(r.th)], [-Math.sin(r.th), Math.cos(r.th)]];
    const th = [Math.acos(Math.min(1, Math.max(-1, r.s1))), Math.acos(Math.min(1, s2))];
    const Ga = new Float64Array(2 * K), Gp = new Float64Array(2 * K);
    for (let c = 0; c < 2; c++) {
      let nn = 0;
      for (let a = 0; a < K; a++) {
        const ga = col(Fa, 0, a) * u[0][c] + col(Fa, 1, a) * u[1][c], gz = col(Fz, 0, a) * v[0][c] + col(Fz, 1, a) * v[1][c];
        Ga[c * K + a] = ga; Gp[c * K + a] = gz - Math.cos(th[c]) * ga; nn += Gp[c * K + a] * Gp[c * K + a];
      }
      nn = Math.sqrt(nn);
      for (let a = 0; a < K; a++) Gp[c * K + a] = nn > 1e-9 ? Gp[c * K + a] / nn : 0;
    }
    return {len: Math.hypot(th[0], th[1]), at: (t, out) => {
      const c0 = Math.cos(t * th[0]), s0 = Math.sin(t * th[0]), c1 = Math.cos(t * th[1]), s1 = Math.sin(t * th[1]);
      for (let a = 0; a < K; a++) {
        const h0 = Ga[a] * c0 + Gp[a] * s0, h1 = Ga[K + a] * c1 + Gp[K + a] * s1;
        out[a] = h0 * u[0][0] + h1 * u[0][1]; out[K + a] = h0 * u[1][0] + h1 * u[1][1];
      }
    }};
  }
  function rot(F0, alpha) {                         // F0 R(alpha t): a turn within the plane
    const A0 = Float64Array.from(F0);
    return {len: Math.abs(alpha), at: (t, out) => {
      const c = Math.cos(alpha * t), s = Math.sin(alpha * t);
      for (let a = 0; a < K; a++) { out[a] = A0[a] * c + A0[K + a] * s; out[K + a] = -A0[a] * s + A0[K + a] * c; }
    }};
  }
  function flip(F0, b) {                            // the second column turns by 180 degrees through direction b
    const A0 = Float64Array.from(F0);
    return {len: Math.PI, at: (t, out) => {
      const c = Math.cos(Math.PI * t), s = Math.sin(Math.PI * t);
      for (let a = 0; a < K; a++) { out[a] = A0[a]; out[K + a] = A0[K + a] * c + b[a] * s; }
    }};
  }
  function start(m) { move = m; move.t = 0; st.moves++; }
  function next() {
    // the next move: queued (axis mode), else a new random plane while the tour plays
    move = null;
    while (queue.length && !move) {
      const job = queue.shift();
      if (job.kind === "plane") start(geo(orth(F), job.Fz));
      else if (job.kind === "orient") {
        // the plane is reached; turn within it so that x = axis i and y = axis j exactly (a mirror image: turn to
        // (axis i, -axis j), then swing the y axis round through a third axis)
        const i = job.i, j = job.j, w00 = F[i], w01 = F[K + i], w10 = F[j], w11 = F[K + j], det = w00 * w11 - w01 * w10;
        if (det >= 0) { const al = Math.atan2(w01, w00); if (Math.abs(al) > 1e-6) start(rot(F, al)); }
        else {
          const al = Math.atan2(w01, w00);
          if (Math.abs(al) > 1e-6) start(rot(F, al));
          let l = 0; while (l === i || l === j) l++;
          queue.unshift({kind: "flip", l: l});
        }
      } else if (job.kind === "flip" && K >= 3) {
        const b = new Float64Array(K); b[job.l] = 1;
        start(flip(F, b));
      } else if (job.kind === "snap") F.set(axisFrame(job.i, job.j));   // exact axes (the moves end within rounding)
    }
    if (!move && st.mode === 0 && st.playing) start(geo(orth(F), randomFrame()));
  }
  function setAxes(i, j) {
    i = Math.max(0, Math.min(K - 1, i | 0)); j = Math.max(0, Math.min(K - 1, j | 0));
    if (i === j) j = (i + 1) % K;
    st.ai = i; st.aj = j; q("ai").value = String(i); q("aj").value = String(j);
    queue.length = 0;
    queue.push({kind: "plane", Fz: axisFrame(i, j)}, {kind: "orient", i: i, j: j}, {kind: "snap", i: i, j: j});
    next();
    if (!st.playing) setPlaying(true);           // choosing axes is a request to turn there (Pause holds the turn)
    showText(); req();
  }
  function setMode(m) {
    st.mode = m;
    for (let t = 0; t < 2; t++) q("m" + t).setAttribute("aria-pressed", t === m);
    if (m === 1) setAxes(st.ai, st.aj);
    else { queue.length = 0; if (!move) next(); showText(); req(); }
  }
  function setPlaying(p) {
    st.playing = p; const b = q("play");
    b.textContent = p ? "Pause" : "Play"; b.setAttribute("aria-pressed", p);
    if (p && st.mode === 0 && !move) next();
    st.last = 0; req();
  }

  // ---------------------------------------------------------------- projection and drawing
  function project() {
    for (let a = 0; a < K; a++) { f1[a] = F[a]; f2[a] = F[K + a]; }
    const V_ = VV;
    let ss = 0;
    for (let i = 0, o = 0; i < n; i++, o += K) {
      let x = 0, y = 0;
      for (let a = 0; a < K; a++) { const v = V_[o + a]; x += v * f1[a]; y += v * f2[a]; }
      PXt[i] = x; PYt[i] = y; ss += x * x + y * y;
    }
    rms = Math.sqrt(ss / Math.max(1, 2 * n));
  }
  function view() {
    if (!st.rmsS) st.rmsS = rms || 0.1;
    st.rmsS += (rms - st.rmsS) * 0.06;
    SCL = st.zoom * 0.45 * Math.min(W, H) / (3.2 * Math.max(st.rmsS, 1e-6));
    TX = W / 2 + st.panX; TY = H / 2 + st.panY;
  }
  const sxT = i => PXt[i] * SCL + TX, syT = i => -PYt[i] * SCL + TY;
  function makeGroups() {
    st.groupsDirty = false;
    const g = new Map(), selOn = sel >= 0 && sel < n;
    for (let i = 0; i < n; i++) {
      let a = 1;
      if (hlMod >= 0 && D.mod[i] !== hlMod) a = 0.13;
      if (selOn && i !== sel && !pset.has(i)) a = Math.min(a, 0.4);
      const c = st.colour === 1 ? (ARMC[D.arm[i]] || GREY) : modColour(D.mod[i]), key = a + c;
      let e = g.get(key);
      if (!e) { e = {c: c, a: a, idx: []}; g.set(key, e); }
      e.idx.push(i);
    }
    st.groups = [...g.values()].sort((p, q2) => (p.a - q2.a) || ((q2.c === GREY) - (p.c === GREY)));
    for (const e of st.groups) e.idx = Int32Array.from(e.idx);
  }
  const ptR = () => Math.max(1.4, Math.min(4, 2.2 * Math.pow(st.zoom, 0.35) * Math.min(1, Math.sqrt(4000 / Math.max(1, n)) * 1.3)));
  function draw() {
    g2.setTransform(1, 0, 0, 1, 0, 0);
    if (st.groupsDirty) makeGroups();
    layer(PXt, PYt, -1, VV ? st.groups : null, SCL, TX, TY, DPR, ptR());
    g2.setTransform(DPR, 0, 0, DPR, 0, 0);
    if (!VV) return;
    drawCompass();
    const r = ptR();
    if (sel >= 0 && sel < n) {
      const x0 = sxT(sel), y0 = syT(sel);
      for (const p of P) {
        if (p.j >= n) continue;
        const a = Math.abs(p.cos);
        g2.strokeStyle = p.cos > 0 ? WITH : OPP; g2.globalAlpha = 0.3 + 0.55 * a; g2.lineWidth = 0.8 + 2 * a;
        g2.beginPath(); g2.moveTo(x0, y0); g2.lineTo(sxT(p.j), syT(p.j)); g2.stroke();
      }
      g2.globalAlpha = 1;
      for (const p of P) {
        if (p.j >= n) continue;
        g2.beginPath(); g2.arc(sxT(p.j), syT(p.j), r + 1.5, 0, 2 * Math.PI);
        g2.fillStyle = st.colour === 1 ? (ARMC[D.arm[p.j]] || GREY) : modColour(D.mod[p.j]); g2.fill();
        g2.lineWidth = 2; g2.strokeStyle = p.cos > 0 ? WITH : OPP; g2.stroke();
      }
      g2.beginPath(); g2.arc(x0, y0, r + 4, 0, 2 * Math.PI); g2.lineWidth = 2.5; g2.strokeStyle = INK; g2.stroke();
      g2.textAlign = "left"; g2.textBaseline = "middle";
      const label = Labeler(g2);
      label(D.sym[sel], x0 + r + 7, y0, "700 13px " + FF, INK, 15);
      for (const p of P) if (p.j < n) label(D.sym[p.j], sxT(p.j) + r + 4, syT(p.j), "11px " + FF, p.cos > 0 ? WITH_T : OPP_T, 12);
    }
    if (st.hover >= 0 && st.hover !== sel) {
      g2.beginPath(); g2.arc(sxT(st.hover), syT(st.hover), r + 3, 0, 2 * Math.PI); g2.lineWidth = 1.5; g2.strokeStyle = INK; g2.stroke();
    }
  }
  function drawCompass() {
    // where the space's axes point in this view: the 6 longest projected axes, from a corner
    const o = [58, H - 58], R0 = 44, ax = [];
    for (let a = 0; a < K; a++) ax.push([Math.hypot(F[a], F[K + a]), a]);
    ax.sort((p, q2) => q2[0] - p[0]);
    g2.strokeStyle = "#a3a29b"; g2.lineWidth = 1; g2.globalAlpha = 1;
    g2.beginPath(); g2.arc(o[0], o[1], R0, 0, 2 * Math.PI); g2.stroke();
    g2.textAlign = "center"; g2.textBaseline = "middle";
    for (const [len, a] of ax.slice(0, 6)) {
      if (len < 0.05) continue;
      const x = o[0] + R0 * F[a], y = o[1] - R0 * F[K + a];
      g2.strokeStyle = INK2; g2.lineWidth = 1.4; g2.beginPath(); g2.moveTo(o[0], o[1]); g2.lineTo(x, y); g2.stroke();
      if (len >= 0.3) halo(g2, String(a + 1), o[0] + (R0 * len + 9) * F[a] / len, o[1] - (R0 * len + 9) * F[K + a] / len, "600 10px " + FF, INK2);
    }
  }
  function showText() {
    if (!K || !n) { itxt.innerHTML = ""; return; }
    const desc = a => "<b>axis " + (a + 1) + "</b>" + (TD.var && TD.var[a] != null ? " (" + TD.var[a] + "% of the space)" : "") +
      (TD.ax && TD.ax[a] ? " <span class='note'>" + esc(TD.ax[a]) + "</span>" : "");
    itxt.innerHTML = "<b>" + n.toLocaleString() + "</b> genes in the " + K + "-dimensional vector space (unit gene vectors, embed stage), " +
      (st.mode === 0 ? "seen through a 2D window that turns slowly through the whole space: every view is a true projection, so genes that stay together while it turns are close in all " + K + " dimensions." :
        "projected onto two of its axes:<br>&rarr; x: " + desc(st.ai) + "<br>&uarr; y: " + desc(st.aj)) +
      "<div class='ky'>The circle (bottom left) shows where the space's axes point in this view.</div>";
  }
  function fps() { const f = st.frames; return f.length > 2 ? (f.length - 1) * 1000 / (f[f.length - 1] - f[0]) : 0; }
  function status() {
    if (!K || !n) { statusEl.textContent = ""; return; }
    const s = [n.toLocaleString() + " genes", K + " dimensions", st.mode === 0 ? (st.playing ? "touring" : "paused") : "axis " + (st.ai + 1) + " vs axis " + (st.aj + 1) + (move && !st.playing ? " (turning there, paused)" : "")];
    const f = fps();
    if (f && move) s.push(Math.round(f) + " frames/s (projection " + st.projMs.toFixed(1) + " ms, drawing " + st.drawMs.toFixed(1) + " ms)");
    s.push("drag = pan, wheel = zoom, click = select");
    statusEl.textContent = s.join("  ·  ");
  }
  let lastStatus = 0;
  function frame(now) {
    if (!sized) resize();
    if (!K || !n) return false;
    decode();
    let moving = false;
    if (move && st.playing) {                   // Pause holds every move, the turn to chosen axes too
      const dt = st.last ? Math.min(0.1, (now - st.last) / 1000) : 1 / 60;
      move.t = Math.min(1, move.t + dt * st.speed * (st.mode === 1 ? 3 : 1) / Math.max(move.len, 0.15));
      move.at(move.t, F);
      if (move.t >= 1) next();
      moving = true;
      st.frames.push(now);
      while (st.frames.length > 2 && st.frames[0] < now - 1000) st.frames.shift();
    } else { st.frames.length = 0; if (!move && st.mode === 0 && st.playing) { next(); moving = true; } }
    st.last = moving ? now : 0;
    const t0 = performance.now();
    project();
    const t1 = performance.now();
    view();
    draw();
    const t2 = performance.now();
    st.projMs = st.projMs ? 0.9 * st.projMs + 0.1 * (t1 - t0) : t1 - t0;
    st.drawMs = st.drawMs ? 0.9 * st.drawMs + 0.1 * (t2 - t1) : t2 - t1;
    if (now - lastStatus > 400 || !moving) { lastStatus = now; status(); }
    return moving || Math.abs(rms - st.rmsS) > 1e-4 * Math.max(rms, 1e-6);
  }
  function resize() {
    const r = wrapEl.getBoundingClientRect();
    if (r.width < 2 || r.height < 2) return;
    DPR = window.devicePixelRatio || 1; W = r.width; H = r.height;
    cvs.width = Math.round(W * DPR); cvs.height = Math.round(H * DPR); sized = true;
    if (active === "tour") req();
  }
  new ResizeObserver(resize).observe(wrapEl);

  // ---------------------------------------------------------------- pointer
  function hitT(mx, my) {
    const r = Math.max(6, ptR() + 3);
    let best = -1, bd = r * r;
    for (let i = 0; i < n; i++) { const dx = sxT(i) - mx, dy = syT(i) - my, d = dx * dx + dy * dy; if (d < bd) { bd = d; best = i; } }
    return best;
  }
  const tptr = new Map();
  let tdown = null, tdragged = false;
  cvs.addEventListener("pointerdown", e => { cvs.setPointerCapture(e.pointerId); const p = local(e, cvs); tptr.set(e.pointerId, p); tdown = p; tdragged = false; cvs.classList.add("drag"); });
  cvs.addEventListener("pointermove", e => {
    const p = local(e, cvs);
    if (tptr.has(e.pointerId)) {
      const q0 = tptr.get(e.pointerId); tptr.set(e.pointerId, p);
      if (Math.abs(p[0] - tdown[0]) + Math.abs(p[1] - tdown[1]) > 3) tdragged = true;
      st.panX += p[0] - q0[0]; st.panY += p[1] - q0[1];
      tipEl.style.display = "none"; req();
      return;
    }
    if (!VV) return;
    const u = hitT(p[0], p[1]);
    if (u !== st.hover) { st.hover = u; cvs.classList.toggle("onnode", u >= 0); req(); }
    if (u >= 0) placeTip(tipEl, tipHtml(u), p[0], p[1], W, H); else tipEl.style.display = "none";
  });
  const tend = e => { tptr.delete(e.pointerId); if (!tptr.size) cvs.classList.remove("drag"); };
  cvs.addEventListener("pointerup", e => {
    const p = local(e, cvs), was = tdragged; tend(e);
    if (!was && e.button === 0 && VV) { const u = hitT(p[0], p[1]); if (u >= 0) select(u, false, "tour"); else if (sel >= 0) select(-1, false, "tour"); }
  });
  cvs.addEventListener("pointercancel", tend);
  cvs.addEventListener("pointerleave", () => { if (st.hover >= 0) { st.hover = -1; req(); } tipEl.style.display = "none"; });
  cvs.addEventListener("wheel", e => {
    e.preventDefault();
    const [mx, my] = local(e, cvs), dy = e.deltaMode === 1 ? e.deltaY * 33 : e.deltaY, f = Math.exp(-dy * 0.0016);
    const z = Math.min(60, Math.max(0.2, st.zoom * f)), g = z / st.zoom;
    st.panX = (mx - W / 2) - ((mx - W / 2) - st.panX) * g; st.panY = (my - H / 2) - ((my - H / 2) - st.panY) * g; st.zoom = z;
    tipEl.style.display = "none"; req();
  }, {passive: false});

  // ---------------------------------------------------------------- controls
  pane.addEventListener("click", e => {
    const b = e.target.closest("button[data-k]");
    if (!b) return;
    const k = b.dataset.k;
    if (k === "play") setPlaying(!st.playing);
    else if (k === "new") { if (st.mode !== 0) setMode(0); queue.length = 0; start(geo(orth(F), randomFrame())); setPlaying(true); }
    else if (k === "m0" || k === "m1") setMode(k === "m1" ? 1 : 0);
    else if (k === "c0" || k === "c1") { st.colour = k === "c1" ? 1 : 0; for (let t = 0; t < 2; t++) q("c" + t).setAttribute("aria-pressed", t === st.colour); st.groupsDirty = true; req(); }
    else if (k === "fit") { st.zoom = 1; st.panX = 0; st.panY = 0; req(); }
  });
  q("ai").addEventListener("change", () => { st.ai = +q("ai").value; if (st.mode === 1) setAxes(st.ai, st.aj); else setMode(1); });
  q("aj").addEventListener("change", () => { st.aj = +q("aj").value; if (st.mode === 1) setAxes(st.ai, st.aj); else setMode(1); });
  const spd = () => { st.speed = +q("spd").value / 100; q("spdo").textContent = st.speed.toFixed(2); };
  q("spd").addEventListener("input", spd); spd();
  showText();
  return {
    frame: frame,
    show: () => { resize(); decode(); showText(); status(); req(); },
    onSelect: () => { st.groupsDirty = true; if (active === "tour") req(); },
    onHighlight: () => { st.groupsDirty = true; if (active === "tour") req(); },
    togglePause: () => setPlaying(!st.playing),
    state: () => ({k: K, n: n, mode: st.mode === 0 ? "tour" : "axes", playing: st.playing, moving: !!move, ai: st.ai, aj: st.aj,
      frame: Array.from(F), moves: st.moves, rms: rms, fps: fps(), projMs: st.projMs, drawMs: st.drawMs}),
    positions: () => ({x: Array.from(PXt), y: Array.from(PYt)}),
    vector: i => { decode(); return VV && i >= 0 && i < n ? Array.from(VV.subarray(i * K, (i + 1) * K)) : null; },
    axes: (i, j) => { if (st.mode !== 1) { st.ai = i; st.aj = j; setMode(1); } else setAxes(i, j); },
    mode: m => setMode(m === "axes" || m === 1 ? 1 : 0),
    play: p => setPlaying(!!p),
    bench: k => { decode(); if (!sized) resize(); const t0 = performance.now(); for (let r = 0; r < k; r++) { if (move) { move.t = Math.min(1, move.t + 0.01); move.at(move.t, F); } project(); view(); draw(); } return (performance.now() - t0) / Math.max(1, k); },
    screen: i => (i >= 0 && i < n && VV) ? {x: sxT(i), y: syT(i), w: W, h: H} : null,
  };
}

// ================================================================ selection (shared by every tab) and the side panel
function select(i, centre, origin) {
  sel = i; focus = "gene"; selGen++; dirAll = {}; mapArrowsDirty(); mapKeyN = -1; srcSel = "";
  P = partnersOf(i); pset = new Set(P.map(p => p.j));
  qi.value = i >= 0 ? D.sym[i] : "";
  if (i >= 0 && i < N) {
    if (isMap(active)) { if (centre) centreOn(i, layout); mapSelPending = false; }
    else mapSelPending = true;                     // centre the map on it when the map tab is shown again
  }
  try { history.replaceState(null, "", i >= 0 ? "#" + encodeURIComponent(D.sym[i]) : location.pathname + location.search); } catch (err) { /* file:// in some browsers */ }
  regroup(); renderPanel(); status();
  for (const k in PHYS) PHYS[k].onSelect(origin || "");
  if (TOUR) TOUR.onSelect();
}
const ddLabel = d => (d >= 0 && D.dd[d]) ? D.dd[d] : (d >= 0 ? "drug-dose " + d : "");
const foldOf = l100 => Math.pow(2, l100 / 100);
const fdrTxt = f => f == null ? "" : (f < 0.01 ? "&lt;0.01" : f.toFixed(2));
// ---------------------------------------------------------------- alerts: an item with a reason for doubt stays in its
// ranked place and says why ("⚠" + the reason in plain words); lists capped at N also hold any of the N strongest
// items without an alert that fall beyond the first N
const EV_ALERT = [D.halves === false ? "reproducibility not tested (no half spaces)" : "not reproduced in the two random halves of the compounds",
  "seen in one random half of the compounds only: not replicated"];
// relations' alert rule, without the selected gene's own reason (the panel states that once)
const pAlert = p => p.ev < 2 || p.locus || p.rt || EFO.has(p.j);
const flagRow = f => (f > 0 && D.fl && D.fl[f - 1]) ? D.fl[f - 1] : null;   // [text, kind]: 1 alert, 2 note, 0 other
const isAlert = f => { const r = flagRow(f); return !!r && r[1] === 1; };
function flagHtml(f) {
  const r = flagRow(f);
  if (!r) return "";
  if (r[1] === 1) return "<div class='al'>&#9888; " + esc(r[0]) + "</div>";
  if (r[1] === 2) return "<div class='fnote'>" + esc(r[0]) + " (so it is no artifact flag here)</div>";
  return "";
}
const flagTitle = f => { const r = flagRow(f); return r ? " title='" + esc((r[1] === 1 ? "alert: " : "flags: ") + r[0]) + "'" : ""; };
const cntTxt = (nAll, nAl, what) => nAll + " " + what + (nAl ? ", <span class='alc'>" + nAl + " with &#9888;</span>" : "");
function capNote(shown, nAl, cap) {
  // how the list was cut: the cap, and the unflagged rows added beyond it
  const extra = Math.max(0, shown - cap);
  return extra ? "; the " + cap + " strongest shown, plus " + extra + " without &#9888; that come after them" : "";
}
function moduleDrugs(md, dir) {
  const a = dir > 0 ? md.up : md.dn, c = (dir > 0 ? md.nup : md.ndn) || [0, 0];
  if (!a) { const t = dir > 0 ? md.up_txt : md.dn_txt; return t ? esc(t) : ""; }        // older graph stage: as text
  if (!a.length) return "none with |z| &ge; " + D.mod_z;
  let h = "", rows = 0;
  for (let t = 0; t + 1 < a.length; t += 2) {
    const d = a[t], f = D.ddf ? D.ddf[d] || 0 : 0;
    rows++;
    h += (h ? " &middot; " : "") + "<span" + flagTitle(f) + ">" + esc(ddLabel(d)) + " (" + (a[t + 1] > 0 ? "+" : "") + (a[t + 1] / 10).toFixed(1) + ")" +
      (isAlert(f) ? " <span class='alc'>(&#9888; " + esc(flagRow(f)[0]) + ")</span>" : "") + "</span>";
  }
  return h + " <span class='cnt'>(" + cntTxt(c[0], c[1], "with |z| &ge; " + D.mod_z) + capNote(rows, c[1], D.n_mod_drugs || 10) + ")</span>";
}
function moduleCard(m) {
  const md = MODS.get(m);
  if (!md) return "";
  const cb = md.cb == null ? "" : "mean cos between the two sides " + (md.cb > 0 ? "+" : "") + md.cb.toFixed(2);
  const arms = md.opp ? md.np + " in the + arm, " + md.nm + " in the &minus; arm; the arms move opposite (" + cb + ")" :
    "single-armed: " + (cb ? "the two sides of its main direction are not two opposite arms (" + cb + "; a &minus; arm needs &ge; 5 genes on its side and &le; &minus;0.2)" : "all genes on one side of its main direction");
  const up = moduleDrugs(md, 1), dn = moduleDrugs(md, -1);
  return "<div class='mcard'><div><span class='sw' style='background:" + modColour(m) + "'></span> <b>Module " + m + "</b> " +
    "<span class='note'>" + md.n + " genes: " + arms + "</span>" +
    " <span class='lk' data-hl='-1' style='float:right'>clear</span></div>" +
    "<div class='row'><b>" + esc(md.label) + "</b> <span class='lk' data-mtab='" + m + "'>simulate</span></div>" +
    (md.plus ? "<div class='row'><span class='lbl'>" + (md.opp ? "+ arm" : "genes") + ":</span> " + esc(md.plus) + "</div>" : "") +
    (md.minus ? "<div class='row'><span class='lbl'>&minus; arm:</span> " + esc(md.minus) + "</div>" : "") +
    ((md.plus + md.minus).indexOf("\u26a0") >= 0 ? "<div class='row note'>&#9888; after a gene = " + EFO_TXT + "; such genes keep their place by |projection|, and the strongest without an alert are listed too</div>" : "") +
    (up ? "<div class='row'><span class='lbl'>Drug-doses that raise it (" + (md.opp ? "+ arm up, &minus; arm down; mean pooled z of the + arm minus the &minus; arm" : "mean pooled z of its genes") + "; |z| &ge; " + D.mod_z + "; &#9888; = the drug-dose carries an artifact flag, named after it):</span> " + up + "</div>" : "") +
    (dn ? "<div class='row'><span class='lbl'>... that lower it:</span> " + dn + "</div>" : "") +
    (md.lines ? "<div class='row'><span class='lbl' title='largest mean |module score| over its 8 strongest drug-doses'>Most responsive cell lines:</span> " + esc(md.lines) + "</div>" : "") +
    "</div>";
}
function drugTable(i, dir) {
  const a = dir > 0 ? D.up[i] : D.dn[i], c = D.dct ? D.dct.slice(4 * i + (dir > 0 ? 0 : 2), 4 * i + (dir > 0 ? 2 : 4)) : [0, 0];
  if (!has(a)) return "<p class='note'>No drug-dose " + (dir > 0 ? "raises" : "lowers") + " it pooled over the cell lines (median; |z| &ge; 3 or q &lt; 0.1). A response in fewer than about half of the lines does not reach the pooled data: see the cell lines below.</p>";
  let h = "<table><tr><th>Drug-dose</th><th class='r' title='fold change pooled over the cell lines (median)'>fold</th><th class='r'>z</th><th class='r' title='cell lines that move the same way (per-line z &ge; 2 and &ge; 1.2x)'>lines</th></tr>";
  let rows = 0;
  for (let t = 0; t + 4 < a.length; t += 5) {
    const f = a[t + 4];
    rows++;
    h += "<tr" + flagTitle(f) + "><td>" + esc(ddLabel(a[t])) + flagHtml(f) + "</td><td class='r'>" + foldOf(dir * a[t + 1]).toFixed(2) + "&times;</td><td class='r'>" +
      (dir * a[t + 2] / 10).toFixed(1) + "</td><td class='r'>" + a[t + 3] + "</td></tr>";
  }
  return h + "</table><p class='note'>" + cntTxt(c[0], c[1], (c[0] === 1 ? "drug-dose " + (dir > 0 ? "raises" : "lowers") : "drug-doses " + (dir > 0 ? "raise" : "lower")) + " it (pooled |z| &ge; 3 or q &lt; 0.1)") +
    capNote(rows, c[1], D.n_drugs || 8) + ". &#9888; = the drug-dose carries an artifact flag for this gene (named under it): it keeps its place in the ranking; read it with that in mind.</p>";
}
function lineTable(a) {
  if (!has(a)) return "<p class='note'>Not measured in any line (not expressed, or only ambient RNA), or no per-line data.</p>";
  const all = !!D.ln_all, what = all ? "drug-doses" : "clean drug-doses";
  let h = "<table><tr><th>Cell line</th><th class='r' title='" + what + " raising it in this line (per-line z &ge; " + D.line_z + ", &ge; 1.5x)" + (all ? "; how many of them carry an artifact flag in brackets" : "") + "'>&uarr;</th><th class='r' title='... lowering it'>&darr;</th><th>strongest drug-dose here</th></tr>";
  const W = D.lnw || 9;
  let nClean = 0;
  for (let t = 0; t + W - 1 < a.length; t += W) {
    const l = a[t], org = D.organ[l] ? " <span class='note'>" + esc(D.organ[l]) + "</span>" : "", f = a[t + 8];
    const n_ = (v, w) => v + (w ? " <span class='alc' title='" + w + " of them carry an artifact flag'>(&#9888;" + w + ")</span>" : "");
    let best = a[t + 5] >= 0 ? esc(ddLabel(a[t + 5])) + " <span class='note'>" + foldOf(a[t + 6]).toFixed(2) + "&times;, z " + (a[t + 7] / 10).toFixed(1) + "</span>" + flagHtml(f) : "&ndash;";
    if (W >= 12 && a[t + 9] >= 0) {               // the strongest carries an alert: the strongest without one too
      best += "<br><span class='note'>no alert: </span>" + esc(ddLabel(a[t + 9])) + " <span class='note'>" + foldOf(a[t + 10]).toFixed(2) + "&times;, z " + (a[t + 11] / 10).toFixed(1) + "</span>";
      nClean++;
    }
    h += "<tr" + flagTitle(f) + "><td>" + esc(D.lines[l] || ("line " + l)) + org + "</td><td class='r'>" + n_(a[t + 1], a[t + 2]) + "</td><td class='r'>" + n_(a[t + 3], a[t + 4]) +
      "</td><td>" + best + "</td></tr>";
  }
  return h + "</table><p class='note'>&uarr; / &darr; = " + what + " moving it &ge; 1.5&times; at per-line |z| &ge; " + D.line_z +
    (D.line_z_cal ? " (calibrated on this run" + (D.line_chance != null ? ": about " + D.line_chance + " chance calls per gene and line among the clean drug-doses" : "") + ")" : " (not calibrated in this run: a per-line z of 4-5 can arise by chance)") +
    (all ? "; (&#9888;n) = n of them carry an artifact flag; the strongest of them all is shown, flagged or not (&#9888; and the flag under it)" + (nClean ? "; when it carries an alert, the line's strongest drug-dose without one follows ('no alert:')" : "") : "; the strongest of them is shown (an older tables stage: flagged drug-doses are not counted here)") +
    "; &ndash; = none.</p>";
}
const LIT = new Map();                             // literature verdicts (OUT/review): a * NA + b -> [kind, citations]
if (D.lit) for (let t = 0; t + 3 < D.lit.length; t += 4) LIT.set(D.lit[t] * NA + D.lit[t + 1], [D.lit[t + 2], D.lit[t + 3]]);
function litBadge(i, j) {
  // lit_v[kind] = [label, explanation, shown verdict, check_status] (vault.verdict_label): an unverified verdict reads "unverified"
  let v = LIT.get(i * NA + j), from = "";
  if (!v) { v = LIT.get(j * NA + i); if (v) from = " (in " + D.sym[j] + "'s review)"; }
  if (!v) return "";
  const k = D.lit_v[v[0]] || ["?", "", "", ""];
  return "<span class='bd lit lit-" + esc(k[2]) + " lit-st-" + esc(k[3]) + "' title='AI-agent literature review" + esc(from) + ": " + esc(k[1]) + "; " + v[1] +
    " citation" + (v[1] === 1 ? "" : "s") + " (review/connections.parquet; the vault note has the review and its links)'>lit: " + esc(k[0]) + "</span>";
}
function partnerTable() {
  if (!P.length) return "<p class='note'>No partners recorded.</p>";
  let h = "<table class='pt'><tr><th>Gene</th><th class='r' title='signed cosine: +1 = same direction, -1 = opposite'>cos</th><th title='both = same sign with fdr &le; 0.10 in two random halves of the compounds; one = strong in one random half only (not replicated, no error estimate); none = neither'>halves</th><th class='r' title='estimated share of false relations among pairs at least this strong in both halves'>fdr</th><th>flags</th></tr>";
  let nLit = 0;
  for (const p of P) {
    let f = LIT.size ? litBadge(sel, p.j) : "";
    if (f) nLit++;
    if (p.novel && D.novel_ok) f += "<span class='bd nov' title='both halves, fdr <= 0.05, |cos| >= 0.5, not in any reference set, not the same locus'>novel?</span>";
    if (p.ev < 2) f += "<span class='bd warn' title='" + EV_ALERT[p.ev] + ": this relation may not hold up'>&#9888; " + (p.ev === 1 ? "one half only" : "not reproduced") + "</span>";
    if (p.locus) f += "<span class='bd loc' title='within 50 kb of each other: neighbouring genes can correlate for genomic reasons'>&#9888; same locus</span>";
    if (p.rt) f += "<span class='bd rt' title='same strand, <= 20 kb, the 5-prime gene much more expressed: read-through can make them correlate'>&#9888; read-through risk</span>";
    if (EFO.has(p.j)) f += "<span class='bd warn' title='" + esc(D.sym[p.j]) + " is " + EFO_TXT + "'>&#9888; via flagged drug-doses</span>";
    if (p.known) {
      if (p.string) f += "<span class='bd' title='known: STRING combined score " + p.string + "'>STRING " + p.string + "</span>";
      if (p.pw >= 0 && D.pw[p.pw]) f += "<span class='bd' title='known: shared pathway " + esc(D.pw[p.pw]) + "'>pathway</span>";
      if (p.group) f += "<span class='bd' title='known: same HGNC gene group'>family</span>";
      if (!p.string && p.pw < 0 && !p.group) f += "<span class='bd'>known</span>";
    }
    h += "<tr class='ck' data-g='" + p.j + "'><td><span class='k' style='background:" + (p.cos > 0 ? WITH : OPP) + "'></span>" + esc(D.sym[p.j]) +
      "</td><td class='r'>" + (p.cos > 0 ? "+" : "") + p.cos.toFixed(2) + "</td><td>" + EVS[p.ev] + "</td><td class='r'>" + fdrTxt(p.fdr) + "</td><td>" + f + "</td></tr>";
  }
  h += "</table>";
  const rn = D.reln ? [D.reln[2 * sel], D.reln[2 * sel + 1]] : [P.length, 0], nAl = P.filter(pAlert).length;
  h += "<p class='note'>" + P.length + " shown (" + (nAl ? "<span class='alc'>" + nAl + " with &#9888;</span>" : "none with &#9888;") + ") of its " + rn[0] + " strongest partners in the relations table (" + rn[1] + " with &#9888;)" +
    capNote(P.length, nAl, D.n_partners || 15) + ". &#9888; = a reason for doubt: not replicated in both random halves of the compounds, the two genes are neighbours in the genome, or the partner is in the vector space only through flagged drug-doses; such a relation keeps its place in the ranking." +
    (EFO.has(sel) ? " <span class='alc'>&#9888; " + esc(D.sym[sel]) + " itself is " + EFO_TXT + ", so all its partners rest on those drug-doses (said here once, not counted on each row).</span>" : "") + "</p>";
  if (nLit) h += "<p class='note'><span class='bd lit'>lit:</span> = the verdict of an AI-agent literature review on the pair (established, indirect, plausible, unexpected, contradicted) and its check: supported / partly supported (the citation checker read the cited abstracts), not checked (ids exist, claim not checked), ids not checked (not looked up); <i>unverified</i> = the abstracts do not support it, none of its papers exists, or all of them are retracted; (cites a retracted paper) = a paper it cites is retracted, which is no support. Not checked by a person; hover for details. The review itself is in the gene's vault note.</p>";
  if (!D.novel_ok) h += "<p class='note'>Novelty not assessed: " + esc((D.novel_blocked || []).join(", ") || "reference sources") + " missing, so no pair is called novel.</p>";
  return h;
}
function whyOut(w) {
  // the embed stage's inclusion rule, with its counts (embed/info.json)
  const E = D.embed || {}, need = E.min_responsive || D.min_responsive || 5;
  let h = "it reaches per-line |z| &ge; 3 in " + w + " of the " + (E.drugdoses_active != null ?
    E.drugdoses_active + " active, trustworthy drug-doses &times; " + (E.lines != null ? E.lines : D.lines.length) + " lines the space is built from (drug-doses with &ge; " + (E.min_active || 10) + " significant genes, pooled or in single lines, and no untrusted flag)" :
    "(drug-dose, cell line) contexts the space is built from");
  if (w < need) return h + "; the space needs " + need + ".";
  // since embed VERSION 3 (embed/info.json n_genes_evidence_flagged_only) a flagged significant drug-dose counts too
  h += "; that count is not enough on its own: the space also needs a significant " + (E.n_genes_evidence_flagged_only != null ?
    "pooled drug-dose (q &lt; 0.1, &ge; 1.2&times;; one that carries an alert counts too, and a gene whose evidence all carries an alert is marked &#9888;)" :
    "clean pooled drug-dose (q &lt; 0.1, &ge; 1.2&times;)") +
    (E.line_z_responsive != null ? " or a per-line |z| &ge; " + (+E.line_z_responsive).toFixed(1) + " in &ge; 2 lines of one drug-dose" : "") + ", and it has neither";
  if (E.null_rate != null) h += " (chance rate of |z| &ge; 3 per context " + (+E.null_rate).toPrecision(2) + ")";
  if (E.n_genes_excluded_chance != null) h += "; " + E.n_genes_excluded_chance.toLocaleString() + " genes of this run reach the count without either";
  return h + ".";
}
const EFO = new Set(D.efo || []);                 // entries in the space only through drug-doses with an alert
const EFO_TXT = "in the vector space only through drug-doses that carry an alert (artifact flags at every significant pooled drug-dose and per-line response)";
// ---------------------------------------------------------------- the side panel's probable direction
let dirAll = {};                                  // the lists opened with 'show all' (reset when the gene changes)
const DIR_LISTS = {up: ["Upstream (probable)", "what acts on "], dn: ["Downstream (probable)", "what ", " acts on"],
  ce: ["Cells under drug-doses (probable)", "how ", " acts on the cells' numbers"]};
function dirNames(w, i) {
  // a row's source names (each a link when it is a gene of the page; the selected gene in bold), at most 5 of them
  const one = s => s.e === i ? "<span class='dsel'>" + esc(s.name) + "</span>" :
    s.e >= 0 ? "<span class='lk' data-g='" + s.e + "'>" + esc(s.name) + "</span>" : "<span class='dnm' title='not a measured gene of this run'>" + esc(s.name) + "</span>";
  const shown = w.src.length > 6 ? w.src.slice(0, 5) : w.src;
  let h = shown.map(one).join(", ");
  if (shown.length < w.src.length) h += " <span class='note' title='" + esc(w.S) + "'>(+" + (w.src.length - shown.length) + " more)</span>";
  return h;
}
function dirRowHtml(k, i) {
  const w = dirRow(k), tgt = w.cells ? esc(w.tgt) : w.te === i ? "<span class='dsel'>" + esc(w.tgt) + "</span>" :
    w.te >= 0 ? "<span class='lk' data-g='" + w.te + "'>" + esc(w.tgt) + "</span>" : esc(w.tgt);
  const sw = ((dirResp(k) && DR.signw_resp) ? DR.signw_resp : DR.signw)[w.sign + 1] || "";
  let h = "<div class='dr' data-dk='" + k + "' title='" + esc(w.kindText) + " (click for the evidence)'><div><span class='gb g" + w.gi + "' title='" +
    esc("grade " + w.grade + ": " + (DR.gwords[w.gi] || "")) + "'>" + esc(w.grade) + "</span> " + dirNames(w, i) + " &rarr; " + tgt +
    " <span class='sgn' title='" + esc(w.signText) + "'>" + esc(sw) + "</span> <span class='note'>" + esc(DR.kshort[w.kind]) + " &middot; " + esc(w.q) + "</span></div>" +
    "<div class='dtx'>" + esc(w.signText) + "</div>";
  if (w.alShort) h += "<div class='al' title='" + esc(w.alLong || w.alShort) + "'>" + esc(w.alShort) + "</div>";
  h += "<div class='dx'><div>" + esc(w.kindText) + "</div>" + (w.reading ? "<div>" + esc(w.reading) + "</div>" : "") +
    (w.alLong ? "<div class='alc' style='white-space:normal'>" + esc(w.alLong) + "</div>" : "") + "</div>";
  return h + "</div>";
}
function dirListHtml(i, which) {
  // one list: the cap rule (N strongest, plus any of the N strongest without an alert after them), its counts and a
  // 'show all'; a list the page holds only in part (shortened) says how many rows it leaves out
  const L = DIR_LISTS[which], rows = dirRowsOf(i, which), extra = which === "ce" ? dirIndex().more.get(i) : null;
  const title = L[0] + ": " + L[1] + esc(D.sym[i]) + (L[2] || "");
  const cnt = dirCountsText(rows, "rows", extra);
  if (!rows.length && !extra) return "<div class='dlw' id='dlw-" + which + "'><div class='dh4'>" + title + " <span class='cnt'>none</span></div></div>";
  const all = !!dirAll[which], c = dirCap(rows, DR.cap || 8), list = all ? rows : c.shown;
  let h = "<div class='dlw' id='dlw-" + which + "'><div class='dh4'>" + title + " <span class='cnt'>(" + esc(cnt) + ")</span></div><div id='dl-" + which + "'>" + list.map(k => dirRowHtml(k, i)).join("") + "</div>";
  const notes = [];
  if (!all && c.more) notes.push(esc(dirMoreText(c.more, c.moreAl, "rows")) + " <span class='lk' data-dall='" + which + "'>show all</span>");
  else if (all && c.more) notes.push("all " + fmtN(rows.length) + " shown <span class='lk' data-dall='" + which + "'>show fewer</span>");
  if (!all && c.shown.length > (DR.cap || 8)) { const nx = c.shown.length - (DR.cap || 8); notes.push("the " + (DR.cap || 8) + " strongest shown, plus " + nx + " without " + ALERT_S + " that come" + (nx === 1 ? "s" : "") + " after them"); }
  if (extra && extra[0]) notes.push("<span class='alc'>" + esc(dirMoreText(extra[0], extra[1], "rows")) + " are not in this page (left out to keep it small): <code>tahoe gene " + esc(D.sym[i]) + " --top " + (rows.length + extra[0]) + "</code> and <code>direction/edges.parquet</code> list them all</span>");
  return h + (notes.length ? "<p class='note'>" + notes.join("; ") + ".</p>" : "") + "</div>";
}
function dirSection(i) {
  if (!HAS_DIR) return "<h3>Probable direction</h3><p class='note'>No probable directions here: " + esc(DR.why || "this output has no direction stage") +
    ". <code>python -m tahoemap run --out OUT</code> runs the direction stage (newer than this output) and makes the map again.</p>";
  const cv = String(DR.caveat_short || "probable direction"), c2 = cv.indexOf(": ");
  let h = "<h3>" + esc(cv.charAt(0).toUpperCase() + (c2 > 0 ? cv.slice(1, c2) : cv.slice(1))) + (c2 > 0 ? " <span class='cnt'>(" + esc(cv.slice(c2 + 2)) + ")</span>" : "") + "</h3>";
  h += dirListHtml(i, "up") + dirListHtml(i, "dn") + dirListHtml(i, "ce");
  h += "<p class='note'>Grades: " + DR.grades.map((g, t) => "<span class='gb g" + t + "' title='" + esc(DR.gwords[t]) + "'>" + g + "</span> " + esc(DR.gshort[t])).join(" &middot; ") +
    ". Sign: what the source's activity does to the target. &#9888; = a reason for doubt; the row keeps its place. In order: " + esc(DR.order) +
    ". Click a row for its evidence. " + (DR.short && DR.short.length ? "<span class='alc'>Shortened to keep the page small: " + esc(DR.short.join("; ")) + ".</span> " : "") +
    "<span class='lk' data-help='dir'>How to read the arrows</span></p>";
  return h;
}
function geneCard(i) {
  let h = "<h2>" + esc(D.sym[i]) + "</h2>";
  if (has(D.name) && D.name[i]) h += "<div class='nm'>" + esc(D.name[i]) + "</div>";
  if (has(D.fn) && D.fn[i]) h += "<p class='fn'>" + esc(D.fn[i]) + "</p>";
  if (has(D.alias) && D.alias[i]) h += "<p class='note'>Also: " + esc(D.alias[i].split("|").join(", ")) + "</p>";
  if (i < N) {
    const m = D.mod[i], arm = D.arm[i], md = MODS.get(m);
    h += "<p><span class='k' style='background:" + modColour(m) + "'></span>" + (m > 0 ? "<span class='lk' data-hl='" + m + "'>Module " + m + "</span>" +
      (md && !md.opp ? ", single-armed" : arm !== "." ? ", " + (arm === "-" ? "&minus;" : "+") + " arm" : "") + (md ? " &middot; " + esc(md.label) : "") : "No module") + "</p>";
    if (EFO.has(i)) h += "<p class='al'>&#9888; " + EFO_TXT + ": its place on the map and its partners rest on those drug-doses.</p>";
  } else {
    const w = D.why[i - N];
    h += "<p class='al'>&#9888; <b>Not on the map</b> (not in the vector space, so no partners or module): " + (w === -1 ? "a noise-class RNA (left out of the vector space by design)." :
      w === -2 ? "in the vector space but not laid out." : whyOut(w)) + " Its drug-doses and cell lines are below.</p>";
  }
  const c = D.cpm[i];
  const nl = D.nlx[i];
  const na = (v, w) => v + (w ? " (<span class='alc'>" + w + " with &#9888;</span>)" : "");
  h += "<p class='note'>Level " + (c == null ? "?" : c.toLocaleString()) + " CPM (pooled)" + (nl >= 0 ? ", expressed in " + nl + " of " + D.lines.length + " cell lines" : "") +
    ". Raised significantly by " + na(D.nup[i], D.nupa ? D.nupa[i] : 0) + " and lowered by " + na(D.ndn[i], D.ndna ? D.ndna[i] : 0) + " drug-doses (q &lt; 0.1, &ge; 1.2x; &#9888; = an artifact flag for this gene).</p>";
  if (i < N) {
    h += "<h3>Moves with (<span style='color:" + WITH + "'>green</span>) or opposite to (<span style='color:" + OPP + "'>red</span>) &mdash; top " + P.length + "</h3>" + partnerTable();
  }
  h += dirSection(i);
  h += "<h3>Drug-doses that raise it</h3>" + drugTable(i, 1);
  h += "<h3>Drug-doses that lower it</h3>" + drugTable(i, -1);
  h += "<h3>Cell lines where it responds most</h3>" + lineTable(D.ln[i]);
  h += "<p class='note' style='margin-top:12px'>Fold = vs the same cell line's typical treated well on the plate (not DMSO), pooled over the cell lines (median). Drug-doses with a technical-artifact flag are listed in their ranked place, marked &#9888; with the flag. <span class='lk' data-help='1'>How to read this</span></p>";
  return h;
}
function renderPanel() {
  if (srcSel && sel < 0) { $("panel").innerHTML = srcCard(srcSel); $("panel").scrollTop = 0; return; }
  const g = sel >= 0 ? geneCard(sel) : "", m = hlMod >= 0 ? moduleCard(hlMod) : "";
  let h = (focus === "module" || !g) ? m + g : g + (m ? "<h3>Highlighted module</h3>" + m : "");
  if (!h) h = "<p class='note'>Click a gene on the map or search for one. <span class='lk' data-help='1'>How to read this</span></p>" + HOWTO_MAPS;
  $("panel").innerHTML = h;
  $("panel").scrollTop = 0;
}
$("panel").addEventListener("click", e => {
  const g = e.target.closest("[data-g]"), m = e.target.closest("[data-hl]"), hp = e.target.closest("[data-help]"), mt = e.target.closest("[data-mtab]");
  const da = e.target.closest("[data-dall]"), dr = e.target.closest(".dr");
  if (g) select(+g.dataset.g, true, "panel");
  else if (mt) { if (+mt.dataset.mtab !== hlMod) highlight(+mt.dataset.mtab); showTab("mod"); }
  else if (m) highlight(+m.dataset.hl === hlMod ? -1 : +m.dataset.hl);
  else if (da) {                                   // 'show all' / 'show fewer' of one direction list
    const w = da.dataset.dall, el = $("dlw-" + w);
    dirAll[w] = !dirAll[w];
    if (w === "src") { renderPanel(); return; }
    if (el && sel >= 0) el.outerHTML = dirListHtml(sel, w);
    mapArrowsDirty(); req();
    if (PHYS.nbr) PHYS.nbr.redir();
  }
  else if (hp) { showTab("help"); const t = hp.dataset.help === "dir" ? $("help-dir") : null; if (t) t.scrollIntoView({block: "start"}); }
  else if (dr && !e.target.closest("a,.lk")) dr.classList.toggle("open");   // a row: its evidence
});

// ---------------------------------------------------------------- search
const SYM_L = D.sym.map(s => s.toLowerCase());
const ALI = [];
if (has(D.alias)) D.alias.forEach((s, i) => { if (s) for (const a of s.split("|")) if (a) ALI.push([a.toLowerCase(), a, i]); });
function search(q) {
  q = q.trim().toLowerCase();
  if (!q) return [];
  const out = [], seen = new Set(), MAX = 14;
  const add = (i, via) => { if (!seen.has(i) && out.length < MAX) { seen.add(i); out.push({i: i, via: via}); } };
  const bylen = (a, b) => (D.sym[a].length - D.sym[b].length) || (a >= N) - (b >= N) || (D.sym[a] < D.sym[b] ? -1 : 1);
  for (let i = 0; i < NA; i++) if (SYM_L[i] === q) add(i);
  for (const [l, a, i] of ALI) if (l === q) add(i, a);
  let pre = [];
  for (let i = 0; i < NA; i++) if (SYM_L[i].startsWith(q)) pre.push(i);
  pre.sort(bylen).forEach(i => add(i));
  for (const [l, a, i] of ALI) { if (out.length >= MAX) break; if (l.startsWith(q)) add(i, a); }
  for (let i = 0; i < NA && out.length < MAX; i++) if (SYM_L[i].includes(q)) add(i);
  if (q.length >= 3 && has(D.name)) for (let i = 0; i < NA && out.length < MAX; i++) if (D.name[i] && D.name[i].toLowerCase().includes(q)) add(i, "name");
  // sources of probable-direction rows that are no gene of this page (a drug target the screen does not measure)
  const srcs = [];
  for (const [nm, ks] of dirSources()) { const l = nm.toLowerCase(); if (l === q || l.startsWith(q)) srcs.push({i: -1, src: nm, n: ks.length, ex: l === q}); }
  srcs.sort((a, b) => (b.ex - a.ex) || (a.src.length - b.src.length) || (a.src < b.src ? -1 : 1));
  for (const r of srcs) if (out.length < MAX || r.ex) out.splice(r.ex ? 0 : out.length, 0, r);
  return out.slice(0, Math.max(MAX, 1));
}
// the direction rows' sources that are no gene of this page: name -> its rows (in ORDER), built on first use
let DSRC = null;
function dirSources() {
  if (DSRC) return DSRC;
  DSRC = new Map();
  if (!HAS_DIR) return DSRC;
  const nr = DR.r.length / DW;
  for (let k = 0; k < nr; k++) {
    const ss = DR.ss[DR.r[k * DW + 1]];
    for (let t = 1; t + 1 < ss.length; t += 2) if (ss[t + 1] < 0) {
      const nm = DR.nm[ss[t]];
      if (!DSRC.has(nm)) DSRC.set(nm, []);
      DSRC.get(nm).push(k);
    }
  }
  return DSRC;
}
let srcSel = "";                                  // the panel shows such a source (its rows) instead of a gene
function srcCard(nm) {
  const ks = dirSources().get(nm) || [], all = !!dirAll.src, c = dirCap(ks, DR.cap || 8), list = all ? ks : c.shown;
  let h = "<h2>" + esc(nm) + "</h2><p class='al'>&#9888; <b>Not a measured gene of this run</b>: no expression data of its own, so no place on the map, but the source of probable-direction rows (a gene that compounds of the screen target, or a recorded driver gene whose own mRNA is not measured). <code>tahoe gene " + esc(nm) + "</code> lists them too.</p>";
  h += "<h3>What " + esc(nm) + " probably acts on <span class='cnt'>(" + esc(dirCountsText(ks, "rows")) + ")</span></h3><div id='dl-src'>" + list.map(k => dirRowHtml(k, -2)).join("") + "</div>";
  const notes = [];
  if (!all && c.more) notes.push(esc(dirMoreText(c.more, c.moreAl, "rows")) + " <span class='lk' data-dall='src'>show all</span>");
  else if (all && c.more) notes.push("all " + fmtN(ks.length) + " shown <span class='lk' data-dall='src'>show fewer</span>");
  if (!all && c.shown.length > (DR.cap || 8)) { const nx = c.shown.length - (DR.cap || 8); notes.push("the " + (DR.cap || 8) + " strongest shown, plus " + nx + " without " + ALERT_S + " that come" + (nx === 1 ? "s" : "") + " after them"); }
  return h + (notes.length ? "<p class='note'>" + notes.join("; ") + ".</p>" : "") + "<p class='note'>Click a row for its evidence; click a gene's name to select it. Its rows to the cells under drug-doses (when it has any) link no gene of this page: <code>tahoe gene " + esc(nm) + "</code>. <span class='lk' data-help='dir'>How to read the arrows</span></p>";
}
function showSource(nm) {
  select(-1, false, "search");
  srcSel = nm; qi.value = nm;
  renderPanel();
}
let acItems = [], acOn = 0;
const qi = $("q"), ac = $("ac");
function acRender() {
  if (!acItems.length) { ac.style.display = "none"; return; }
  ac.innerHTML = acItems.map((r, k) => "<div data-k='" + k + "' class='" + (k === acOn ? "on" : "") + "'>" +
    (r.src ? "<b>" + esc(r.src) + "</b> <span class='alc'>&#9888; not a measured gene: the source of " + fmtN(r.n) + " probable-direction row" + (r.n === 1 ? "" : "s") + "</span></div>" :
    (r.via && r.via !== "name" ? "<span class='m'>" + esc(r.via) + " &rarr; </span>" : "") + "<b>" + esc(D.sym[r.i]) + "</b>" +
    (has(D.name) && D.name[r.i] ? " <span class='m'>" + esc(D.name[r.i]) + "</span>" : "") +
    (r.i >= N ? " <span class='alc'>&#9888; not on the map</span>" : "") + "</div>")).join("");
  ac.style.display = "block";
}
qi.addEventListener("input", () => { acItems = search(qi.value); acOn = 0; acRender(); });
qi.addEventListener("keydown", e => {
  if (e.key === "ArrowDown" || e.key === "ArrowUp") {
    if (acItems.length) { acOn = (acOn + (e.key === "ArrowDown" ? 1 : acItems.length - 1)) % acItems.length; acRender(); }
    e.preventDefault();
  } else if (e.key === "Enter") {
    if (!acItems.length) acItems = search(qi.value);
    if (acItems.length) pick(acItems[acOn] ? acOn : 0);
    e.preventDefault();
  } else if (e.key === "Escape") { acItems = []; acRender(); qi.blur(); }
});
ac.addEventListener("mousedown", e => { const d = e.target.closest("[data-k]"); if (d) { pick(+d.dataset.k); e.preventDefault(); } });
qi.addEventListener("blur", () => setTimeout(() => { ac.style.display = "none"; }, 150));
qi.addEventListener("focus", () => qi.select());              // typing replaces the selected gene's symbol
function pick(k) {
  const r = acItems[k];
  if (!r) return;
  if (r.src) { acItems = []; acRender(); showSource(r.src); return; }
  qi.value = D.sym[r.i]; acItems = []; acRender();
  select(r.i, true, "search");
}

// ---------------------------------------------------------------- help
const GR = D.grule || {}, gv = (k, d) => GR[k] != null ? GR[k] : d;
const HOWTO_MAPS = "<div class='howto'><h3>How to read this</h3>" +
  "<p>Each dot is a gene. Its place comes from how it responds to about 1,100 drug-doses (379 drugs &times; 3 doses, 24 h) in each of 50 cancer cell lines (Tahoe-100M): two genes that rise and fall under the same treatments in the same lines are related.</p>" +
  "<h4>Nodal map</h4><p>Genes that respond to the <b>same</b> drugs sit together, <b>whether they move in the same direction or in opposite directions</b>. A pathway whose activated genes go up while the genes it represses go down forms one island. That island is a <b>module</b>. When its two sides move opposite (mean cos between them &le; &minus;0.2, &ge; 5 genes on each side) they are the module's <b>+ arm</b> and <b>&minus; arm</b> (colour by arm to see them); otherwise the module is single-armed and all its genes are +.</p>" +
  "<h4>Signed vector map</h4><p>The same genes, but now genes that move in <b>opposite</b> directions are pushed <b>apart</b>: only genes that go up and down together stay close. An island of the nodal map that splits in two here has two opposite arms. Switching between the two map tabs animates each gene from one place to the other.</p>" +
  "<h4>Distances</h4><p>Both maps keep each gene's near neighbours faithfully; the distance between two far-apart islands means little.</p>" +
  "<h4>Spread</h4><p>t-SNE packs the groups against each other, so on both maps the modules look mushed. The <b>Spread</b> slider moves them apart while keeping the map 2D: at 0 the t-SNE layout; at 1 every module is a block that keeps its own t-SNE arrangement, placed by how far apart the modules are in the <b>full vector space</b> (all its dimensions: the distance between the modules' main directions, 1 &minus; |cos| on the nodal map, 1 &minus; cos on the signed map, laid out in 2D by multidimensional scaling) then pushed apart until no two blocks overlap and drawn together until little empty space is left between them. On the signed map each arm of a two-armed module is its own block, because its arms sit apart there. A module that the t-SNE map split into separate islands keeps each island's own arrangement, with its islands packed into one block. A gene without a module moves with one module, the one it is most alike in the vector space among the modules of its nearest module genes, and keeps its place next to them. In between, every gene moves along a straight line; <i>Spread &#8644;</i> animates the whole way, and a selected gene stays where it is on the screen while the others move. Neighbouring blocks are similar modules; how far apart two dissimilar blocks are means little.</p>" +
  "<h4>How the modules are made</h4><p>Every gene is linked to its " + gv("k_edges", 15) + " strongest partners with |cos| &ge; " + gv("min_edge", 0.3) + " whose relation is replicated (the same sign with fdr &le; 0.10 in both random halves of the compounds) or very strong in one half (|cos| &ge; " + gv("one_half_edge", 0.5) + "); each link is weighted by |cos|, so genes that move opposite are linked as strongly as genes that move together. Louvain community detection on that graph gives the modules. A module of more than " + gv("max_module", 300) + " genes, or whose members' mean |cos| is below " + gv("loose_cos", 0.3) + ", is split again by Louvain on its own links (up to " + gv("split_depth", 4) + " times); pieces of fewer than " + gv("min_module", 5) + " genes are left without a module. Inside a module, the first principal axis of its genes' vectors splits it into a + side and a &minus; side; they are two arms only when the &minus; side has &ge; " + gv("min_module", 5) + " genes and the two sides anti-correlate (mean cos &le; " + gv("arms_opposite_cos", -0.2) + "). Modules are numbered by size; their labels are the best-matching gene set (validation stage), else their top genes.</p>" +
  "<h4>Alerts (&#9888;)</h4><p>Nothing is left out of a list because of a reason for doubt: such an item keeps its ranked place and carries <span class='alc'>&#9888;</span> with the reason in plain words. Drug-doses: an artifact flag for this gene (toxic, transcription drop, cell-cycle shift, unreliable plate only, position not correctable, position correction uncertain, wells disagree); for a cell-cycle shift, how much of this change the drug-dose's shift would explain (from the gene's own slopes on the S-phase and G2/M modules; a shift that explains little is no artifact flag and is noted in grey). Partners: a relation not replicated in both halves, two neighbouring genes, or a partner in the vector space only through flagged drug-doses. Genes: not in the vector space (no partners, no module), or in it only through flagged drug-doses. Counts say how many there are in all and how many carry an alert. A list capped at <i>N</i> shows the <i>N</i> strongest, flagged or not, and also any of the <i>N</i> strongest without an alert that come after them, all in one ranking. What is computed from the data can still leave out what is technically broken: the vector space (and with it the maps, partners and modules) is fitted on trustworthy drug-doses only, without those whose only wells are on an unreliable plate, whose position effect could not be corrected, or whose wells disagree (embed stage).</p>" +
  "<h4>A selected gene</h4><ul><li><b style='color:" + WITH + "'>Green lines</b>: genes that move <b>with</b> it; <b style='color:" + OPP + "'>red lines</b>: genes that move <b>opposite</b> to it.</li>" +
  "<li><b>cos</b>: similarity of the two genes' responses across every drug-dose &times; cell line, from +1 (always together) to &minus;1 (always opposite).</li>" +
  "<li><b>halves</b>: the compounds were split at random into two halves (a hash of the compound name) and the space fitted on each; <i>both</i> = the same sign in both halves with fdr &le; 0.10; <i>one</i> = strong in one of the two random halves only: not replicated, no error estimate (&#9888;); <i>none</i> = neither (&#9888;). <b>fdr</b>: the estimated share of false relations among pairs at least this strong in both halves.</li>" +
  "<li><b>same locus</b> / <b>read-through risk</b> (&#9888;): neighbouring genes can correlate for genomic reasons. <b>known</b>: shared pathway, gene family or STRING interaction; <b>novel?</b>: a strong relation seen in both halves (fdr &le; 0.05) and not found in those references; shown only when the references needed to rule out known links loaded.</li>" +
  "<li><b>Drug-doses</b>: fold change and z of the gene, pooled over the cell lines (median: a response in fewer than about half of the lines does not show here), against the same line's typical treated well on the plate (not DMSO); every drug-dose, those with an artifact flag marked &#9888; with the flag. <b>lines</b> = number of cell lines moving the same way.</li>" +
  "<li><b>Probable direction</b>: which genes probably act on it (upstream), which it probably acts on (downstream), and how it probably acts on the cells' numbers under a drug; see <i>Probable direction</i> in the help.</li>" +
  "<li><b>Cell lines</b>: where the gene responds most: how many drug-doses raise (&uarr;) or lower (&darr;) it at least 1.5&times; in that line at the per-line |z| cut calibrated on this run, how many of them carry an artifact flag, and the strongest one, flagged or not; when that one carries an alert, the line's strongest drug-dose without one follows ('no alert:'). Lines that do not express the gene, or read only ambient RNA for it, are not measured.</li></ul>" +
  "<h4>Using the map</h4><p>Drag to pan, scroll or pinch to zoom, double-click to zoom in, click a gene to select it (Esc clears), click a module in the legend to highlight it. Search finds symbols, aliases, previous symbols and names; genes that are not on the map (&#9888;, too few responses) still open their drug and cell-line tables. A link ending in <code>#SYMBOL</code> opens that gene. The selected gene is the same on every tab.</p></div>";
const KTXT = D.k_edges ? "each gene's " + D.k_edges + " strongest replicated partners" : "each gene's strongest replicated partners";
const TK = D.tour && D.tour.k ? D.tour.k : "k";
const HOWTO_PHYS = "<div class='howto'><h3>The tabs</h3><ul>" +
  "<li><b>Nodal map</b>: the t-SNE layout of 1 &minus; |cos|: opposite genes together.</li>" +
  "<li><b>Signed vector map</b>: the t-SNE layout of 1 &minus; cos: opposite genes apart.</li>" +
  "<li><b>" + TK + "-D tour</b>: the gene vectors in their full " + TK + "-dimensional space, through a slowly turning 2D window, or on any two of its axes.</li>" +
  "<li><b>Physics: neighbourhood</b>: a live force simulation of the selected gene, its partners and (depth 2 to 4) their partners, step by step; with the probable-direction arrows between them (<i>Direction</i>).</li>" +
  "<li><b>Physics: module</b>: a live force simulation of one module, all its genes and the edges among them.</li>" +
  "<li><b>Physics: all genes</b>: a live force simulation of every gene on the map, started from the nodal-map positions.</li></ul>" +
  "<p>The side panel and the search box belong to every tab: a gene selected on one tab is selected on all of them.</p>" +
  "<h4>The " + TK + "-D tour</h4><p>Each gene is a unit vector in the " + TK + "-dimensional vector space (embed stage: its direction is its response pattern over every drug-dose &times; cell line; the cosine between two genes is the cos of the side panel). A <b>tour</b> shows the space through a 2D window that turns slowly through all " + TK + " dimensions: each view is an exact linear projection (no fitting, unlike t-SNE), and the window moves along the shortest path (a geodesic) from one random plane to the next, so the motion is smooth. Genes that stay together while the window turns are close in every dimension; a group that comes apart in some views is only close in some. <i>New direction</i> turns toward a new random plane; <i>Speed</i> sets how fast; <i>Pause</i> (space) stops it. <b>Axes</b> shows two axes of the space of your choice (x = axis i, y = axis j); the axes are the space's components, largest first (with their share of the space and their top genes at either end); the window turns there smoothly. The circle at the bottom left shows where the axes point in the current view. Colours, search, selection (its partners as green and red lines), hover and the side panel work as on the maps; the view zooms to keep the cloud in frame (wheel = zoom, drag = pan).</p>" +
  "<h4>What moves the genes in the physics tabs</h4><p>One simulation engine runs all three. Every relation is a <b>spring</b>: it pulls in proportion to |cos| &times; (distance &minus; rest length), and a stronger relation has a shorter rest length. <b>Every pair of genes repels</b> (like charges: force &prop; 1/distance; computed with a Barnes-Hut quadtree, &theta; = 0.8, so 15,000 genes stay interactive). A weak pull holds everything near the centre, and friction slows the genes. The motion cools down (alpha) until the layout settles; any change re-heats it.</p>" +
  "<p>A force layout is a picture of the graph, not a measurement: which genes hold together means a lot, where two groups end up relative to each other means little, and a Reset may land the groups in other places.</p>" +
  "<h4>The sign switch</h4><p><b>Opposite genes attract</b> (the default): red relations (genes that move opposite) are springs like green ones, so a gene and the genes that move opposite to it gather into one cluster: the nodal view, where both arms of a pathway form one island. <b>Opposite genes repel</b>: red relations push their two genes apart (drawn dashed; they push up to six rest lengths and do not pull beyond), so a module's &minus; arm separates from its + arm: the signed view. Flipping the switch re-heats the simulation so you can watch the arms part.</p>" +
  "<h4>Colours</h4><ul><li>Edges: <b style='color:" + WITH + "'>green</b> = the two genes move together, <b style='color:" + OPP + "'>red</b> = they move opposite; thickness &prop; |cos|.</li>" +
  "<li>Genes: by module (the legend's colours) or by arm (<b style='color:" + ARMC["+"] + "'>+ arm</b>, <b style='color:" + ARMC["-"] + "'>&minus; arm</b>, grey = no module). A dark ring = the selected gene; a grey ring = a pinned gene; grey dots in the module tab = genes outside the module.</li></ul>" +
  "<h4>Neighbourhood</h4><p>The selected gene (pinned at the start), its partners (depth 1), their partners (depth 2) and so on up to depth 4, one depth at a time; within a depth the strongest first (the product of the |cos| along the way), at most <i>Max genes</i> (default 300, up to 2,000). The springs are the genes' top partners from the relations table (the lists in the side panel) that pass <i>Min |cos|</i> and <i>Evidence</i>; the info box says how many of the selected gene's listed partners these leave out (they stay in the side panel, with their alerts). Click another gene to move the neighbourhood to it; the genes already there keep their places. <i>Direction</i>: <i>arrows</i> draws the probable-direction arrows between the genes shown, styled by grade; <i>+ its genes</i> also adds the selected gene's probable up- and downstream genes (a violet ring), so that a gene not on the map but with arrows (for example a recorded mutation's gene) can be shown with them; <i>off</i> hides them (see <span class='lk' onclick=\"document.getElementById('help-dir').scrollIntoView()\">Probable direction</span>).</p>" +
  "<h4>Module</h4><p>One module: pick it from the list, use <i>Selected gene's module</i>, click <i>simulate</i> on a module card in the side panel, or click a module in the map legend. Its springs are the edges of the kNN graph that defines the modules (" + KTXT + ", |cos| &ge; 0.3), among the module's genes. Coloured by arm by default; <i>outside genes (1 hop)</i> adds, dimmed, the genes outside the module that its genes link to.</p>" +
  "<h4>All genes</h4><p>Every gene on the map, starting from its place on the nodal map, with every kNN-graph edge as a spring. Edges are drawn for the selected gene only (while the layout moves, 177,000 lines would hide everything). Each frame runs as many simulation steps as fit in about 13 ms (at most 120 a second in every tab, so a re-heat or the sign switch plays out over about two seconds), so the page stays responsive at any size; the status line shows frames per second.</p>" +
  "<h4>Controls</h4><ul><li><b>Drag a gene</b> to move it: its partners follow. <b>Double-click</b> a gene to pin or unpin it (a slow double-click works too: it pins the gene you clicked first). <b>Click</b> a gene to select it (after a short pause, in case a second click follows). Drag the background to pan; wheel or pinch to zoom.</li>" +
  "<li><b>Pause / Resume</b> (space bar), <b>Re-heat</b> (let it move again), <b>Reset</b> (start the layout again and unpin everything), <b>Fit</b> (show every gene).</li>" +
  "<li><b>Repulsion</b> and <b>Springs</b>: the strengths of the two forces. <b>Min |cos|</b>: weaker relations are not springs. <b>Evidence</b>: only relations replicated in both random halves of the compounds, also those strong in one half (the default), or every relation; a spring that is not replicated says so (&#9888;) in the tooltip.</li>" +
  "<li>Labels: the selected gene, its springs' partners and pinned genes; everyone when zoomed in (labels that would overlap are left out).</li></ul></div>";
// the probable direction (direction stage): its words are direction_view's (grades, caveat, order), embedded in D.dir
const HOWTO_DIR = "<div class='howto' id='help-dir'><h3>Probable direction: which gene probably acts on which</h3>" + (!HAS_DIR ?
  "<p>No arrows on this map: " + esc(DR.why || "this output has no direction stage") + ". <code>python -m tahoemap run --out OUT</code> runs the direction stage (newer than this output) and makes the map again.</p></div>" :
  "<p>A relation (cos) has no direction: two genes rise together, but which one drives the other? The direction stage adds arrows <b>SOURCE &rarr; TARGET</b>, each from a statistical test across the screen's " + (DR.lines || "") + " cell lines (q &lt; 0.10 in its family of tests), with a grade and its alerts. The source is what the test compares the lines by:</p><ul>" +
  "<li><b>mutation</b>: lines with a recorded mutation of the source (loss or gain of function) against lines without one recorded;</li>" +
  "<li><b>not expressed</b>: lines that do not express the source at all (natural knockouts) against lines that do;</li>" +
  "<li><b>drug target</b>: compounds that target the source's protein, and what they do to the target's level;</li>" +
  "<li><b>natural level</b>: lines with more or less of the source, after allowing for the lines' tissue lineage &mdash; a glimpse of a direction without any known mutation.</li></ul>" +
  "<p>The target is another gene (its <i>level</i>: at baseline for a mutation or a natural knockout, under the compounds for a drug target; or how strongly it responds to the drugs: <i>response</i>) or the cells themselves (<i>cells</i>: how many cells of the line remain under a drug-dose, against the other lines in the same wells). The sign is what the source's <b>activity</b> does to the target: <b>raises</b> / <b>lowers</b> a level or the cells' numbers (an inhibitor that raises a gene means the source's activity lowers it); <b>strengthens</b> / <b>weakens</b> a drug response, in the target's own direction at each drug-dose &mdash; where it falls under the drugs, <i>strengthens</i> means it falls further (the source deepens the fall), where it rises, that it rises more. Read which from all the drug-doses a row lists; a row alerted <i>rises at some drug-doses, falls at others</i> says only how strongly the target responds, not whether the source induces or represses it; <b>not inferred</b> = the mechanism is not recorded, so the sign is not known.</p>" +
  "<p>Grades: " + DR.grades.map((g, t) => "<span class='gb g" + t + "'>" + g + "</span> " + esc(DR.gwords[t])).join("; ") + ". An arrow with a reason for doubt keeps its place and carries <span class='alc'>&#9888;</span> with the reason (hover for the full text; click a row for its evidence: the comparison, the reading with its numbers, every alert).</p>" +
  "<p><b>What an arrow does not say</b> (" + esc(DR.caveat_short) + "):</p><ul>" + DR.caveat_lines.map(x => "<li>" + esc(x) + "</li>").join("") + "</ul>" +
  "<h4>In the side panel</h4><p>Three lists for the selected gene: <b>Upstream</b> (what probably acts on it), <b>Downstream</b> (what it probably acts on) and <b>Cells under drug-doses</b> (how it probably acts on the cells' numbers under a drug). Each is in this order: " + esc(DR.order) + ". A list shows the " + (DR.cap || 8) + " strongest rows and also any of the " + (DR.cap || 8) + " strongest without an alert that come after them; it says how many more rows there are and how many of them carry an alert, and <i>show all</i> lists every one. A row that is one test for several genes (the targets of the same compounds; genes absent from exactly the same lines) names all of them. Click a gene's name to select it.</p>" +
  "<h4>Arrows</h4><p>" + dirKey() + "</p><p>On the <b>neighbourhood</b> tab, <i>Direction: arrows</i> draws the arrows between the genes shown (one per pair and direction: its strongest row); <i>+ its genes</i> (the default) also adds the selected gene's probable up- and downstream genes of its side-panel lists to the simulation (a violet ring; they are held by a link that is no relation, so they show where the arrow points, not a similar response). On the two <b>maps</b>, <i>Direction arrows</i> draws the selected gene's arrows to and from the genes on the map. Hover a gene to read the rows between it and the selected gene.</p>" +
  (DR.n_rows_out ? "<p>" + fmtN(DR.n_rows_out) + " of the stage's " + fmtN(DR.n_rows_stage) + " rows link no gene of this page" + (DR.n_rows_out_alert ? " (" + fmtN(DR.n_rows_out_alert) + " of them with an alert <span class='alc'>&#9888;</span>)" : "") + ": their source is not a measured gene and their target is the cells (sources: " + esc((DR.rows_out_sources || []).join(", ")) + (DR.n_rows_out_sources > (DR.rows_out_sources || []).length ? ", and " + fmtN(DR.n_rows_out_sources - (DR.rows_out_sources || []).length) + " more" : "") + "); they are in <code>direction/edges.parquet</code>, and <code>tahoe gene SOURCE</code> lists them.</p>" : "") +
  "<p>A source that is not a measured gene (a drug target the screen does not measure, say) has no place on the map; the search finds it, and its panel lists its arrows.</p>" +
  (DR.short && DR.short.length ? "<p class='alc'>Shortened to keep the page small: " + esc(DR.short.join("; ")) + ". Nothing else is left out; <code>tahoe pair SOURCE TARGET</code> gives a row's every reason in full, <code>tahoe gene SYMBOL --top N</code> lists a gene's rows, and <code>direction/edges.parquet</code> holds everything.</p>" : "") + "</div>");
$("helptext").innerHTML = HOWTO_PHYS + HOWTO_MAPS + HOWTO_DIR;

// ---------------------------------------------------------------- tabs, status, keys, start
const TABS = ["nodal", "signed", "tour", "nbr", "mod", "all", "help"];
const PANE = {nodal: "map", signed: "map", tour: "tour", nbr: "nbr", mod: "mod", all: "all", help: "help"};
function showTab(t) {
  if (!TABS.includes(t)) return;
  active = t;
  for (const b of document.querySelectorAll("#tabs [data-tab]")) b.setAttribute("aria-selected", b.dataset.tab === t);
  for (const p of ["map", "tour", "nbr", "mod", "all", "help"]) $("pane-" + p).classList.toggle("on", PANE[t] === p);
  hideTip();
  if (isMap(t)) {
    resize();
    const l = t === "nodal" ? 0 : 1;
    if (l !== layout || anim || MIX[l].s !== spread) setLayout(l);
    else if (mapSelPending && sel >= 0 && sel < N) { centreOn(sel, layout); mapSelPending = false; }
    status();
  } else if (t === "tour") TOUR.show();
  else if (PHYS[t]) PHYS[t].show();
  req();
}
for (const b of document.querySelectorAll("#tabs [data-tab]")) b.addEventListener("click", () => showTab(b.dataset.tab));
function status() {
  const nm = D.mods.length, s = [(N).toLocaleString() + " genes on the map", (NA - N).toLocaleString() + " more searchable",
    nm + " modules", layout === 0 ? "nodal map" : "signed vector map"];
  if (hlMod >= 0) s.push("module " + hlMod + " highlighted");
  if (spread > 0) s.push("modules spread apart (" + spread.toFixed(2) + "; their places from the full vector space)");
  s.push("drag = pan, wheel = zoom, click = select, Esc = clear");
  $("status").textContent = s.join("  ·  ");
  // the note's length does not depend on the spread (the spread is in the status line), so the control bar never
  // wraps or unwraps, and the canvas keeps its size, while the slider moves
  $("mapnote").textContent = layout === 0 ? "distance = 1 − |cos|: genes that move opposite sit together" : "distance = 1 − cos: genes that move opposite sit apart";
}
if (HAS_DIR) $("dirm").addEventListener("change", () => { mapArrowsDirty(); req(); });
else { $("dirm").checked = false; $("dirm").disabled = true; $("dirml").title = "Not available: this output has no direction stage"; }
$("c0").addEventListener("click", () => setColour(0));
$("c1").addEventListener("click", () => setColour(1));
$("fitb").addEventListener("click", () => fit(false));
if (HAS_SPREAD) {
  $("spr").addEventListener("input", () => setSpread(+$("spr").value / 100, 160));
  $("sprb").addEventListener("click", () => setSpread(spread < 0.5 ? 1 : 0, 900));
} else {
  $("spr").disabled = true; $("sprb").disabled = true;
  $("sprl").title = $("sprb").title = "Not available: this map's graph stage made no spread layouts (re-run the graph stage)";
}
$("lgx").addEventListener("click", () => { const l = $("legend"); l.classList.toggle("closed"); $("lgx").innerHTML = l.classList.contains("closed") ? "+" : "&#8722;"; });
document.addEventListener("keydown", e => {
  if (e.target === qi) return;
  const tag = e.target && e.target.tagName;
  if (e.key === "Escape") { if (sel >= 0) select(-1, false, "key"); else if (hlMod >= 0) highlight(-1); }
  else if (e.key === "/") { qi.focus(); e.preventDefault(); }
  else if (e.key === " " && (PHYS[active] || active === "tour") && !/^(INPUT|SELECT|BUTTON|TEXTAREA)$/.test(tag)) { (PHYS[active] || TOUR).togglePause(); e.preventDefault(); }
});
new ResizeObserver(resize).observe(wrap);
window.addEventListener("hashchange", fromHash);
function fromHash() {
  const h = decodeURIComponent((location.hash || "").slice(1)).trim().toLowerCase();
  if (!h) return;
  let i = SYM_L.indexOf(h);
  if (i < 0) { const r = search(h); if (r.length && (SYM_L[r[0].i] === h || (r[0].via && r[0].via.toLowerCase() === h))) i = r[0].i; }
  if (i >= 0 && i !== sel) select(i, true, "hash");
}
for (const k of ["nbr", "mod", "all"]) PHYS[k] = PhysPane(k);
TOUR = TourPane();
if (D.tour && D.tour.k) $("tourtab").textContent = D.tour.k + "-D tour";
buildLegend(); resize(); setColour(0); renderPanel(); status(); fromHash();
window.TAHOE_MAP = {select: i => select(i, true, "api"), search: search, data: D, tab: showTab,
  bench: n => { const t0 = performance.now(); for (let r = 0; r < n; r++) mapDraw(); return (performance.now() - t0) / n; },
  state: () => ({layout: layout, sel: sel, hlMod: hlMod, colourMode: colourMode, k: V.k / K0, tab: active}),
  sim: key => PHYS[key] ? PHYS[key].state() : null,
  screen: (key, i) => PHYS[key] ? PHYS[key].screen(i) : null,
  stats: key => PHYS[key] ? PHYS[key].stats() : null,
  benchTick: (key, n) => PHYS[key] ? PHYS[key].benchTick(n) : null,
  // the Spread slider (0 = t-SNE, 1 = modules apart; no argument: the current value) and the map's drawn positions
  spread: v => { if (v != null) setSpread(v, 0); return spread; },
  hasSpread: () => HAS_SPREAD,
  positions: () => ({x: Array.from(PX), y: Array.from(PY), animating: !!anim}),
  mapScreen: i => ({x: sx(i), y: sy(i)}),          // where gene i is drawn on the map canvas (CSS pixels)
  // the vector-space tour: its state, projected positions, a gene's decoded vector, axis mode (0-based axes),
  // tour / axes mode, play / pause, and the mean milliseconds of one frame (projection and drawing)
  tour: () => TOUR.state(), tourPositions: () => TOUR.positions(), tourVector: i => TOUR.vector(i),
  tourAxes: (i, j) => TOUR.axes(i, j), tourMode: m => TOUR.mode(m), tourPlay: p => TOUR.play(p),
  tourBench: n => TOUR.bench(n || 30), tourScreen: i => TOUR.screen(i),
  panel: () => $("panel").innerText,
  // probable direction: a gene's three lists (every row as direction_view.edge_line, in ORDER; shown = the positions the
  // capped list shows), the arrows a physics tab draws, and the selected gene's arrows on the maps
  direction: i => {
    if (!HAS_DIR) return {ok: false, why: DR.why || ""};
    const out = {ok: true};
    for (const w of ["up", "dn", "ce"]) {
      const rows = dirRowsOf(i, w), c = dirCap(rows, DR.cap || 8), pos = new Map(rows.map((k, t) => [k, t]));
      out[w] = rows.map(k => dirLine(dirRow(k))); out[w + "_shown"] = c.shown.map(k => pos.get(k));
      out[w + "_more"] = [c.more, c.moreAl]; out[w + "_counts"] = dirCountsText(rows, "rows", w === "ce" ? dirIndex().more.get(i) : null);
    }
    return out;
  },
  dirArrows: key => PHYS[key] && PHYS[key].arrows ? PHYS[key].arrows() : null,
  mapArrows: () => mapArrowList().map(a => ({s: a.s, t: a.t, k: a.k, line: dirLine(dirRow(a.k))}))};
})();
</script>
</body>
</html>
"""
