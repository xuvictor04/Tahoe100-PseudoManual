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
    Concepts/Probable direction.md     generated (not written): the direction stage's arrows explained, with this
                                       run's counts and controls

Rules: frontmatter values are json.dumps'ed (valid YAML); wikilinks are bare [[basename]]; a gene note links only
to its partners, its drugs, the cell lines, its module, its plates note and the genes and drugs of its direction
arrows (never to boilerplate notes, which would turn them into hubs of 16,000 links; the one exception, the
direction section's [[Probable direction]], is left out of the default graph view); output is sorted and carries no
timestamps, so an unchanged run rewrites nothing; generated files carry `generated_by: "tahoemap"` and only such
files are ever deleted as stale.

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

Nothing is left out of a note for a reason to doubt it. An item that carries one - a drug-dose with an artifact flag
(the flags of record, common.ARTIFACT_FLAGS: atlas_core's seven and 'like a neighbouring well'; for this gene: a
'cell-cycle shift' the tables stage found not to explain the gene's change reads 'cell-cycle shift (explains ~N%
here)' and is clean; the caveat tokens of common.CAVEAT_FLAGS carry no alert and their words, common.FLAG_TEXT, stand
once under the list), a partner without the same sign in both halves of the compounds, a lineage pair or read-sharing
copies, a gene
in the vector space only through flagged drug-doses (embed: evidence_flagged_only), a well on an unreliable plate -
keeps its ranked place with an alert: ALERT ('⚠') and the reason in plain words (alert_text; with cc_share,
'cell-cycle shift, explains ~60% of this change'). Counts give the number in all and how many carry an alert. A list
capped at N shows the N strongest and any of the N strongest without an alert that rank below them (cap_keep), so
flagged items never push unflagged ones out of view. Where an estimate of an earlier stage left technically broken
data out, the note says so beside it. Tables of an older tables stage (no cc_share, line_effects counts over clean
drug-doses only, drug_line_top without flags) are read as they are, and the notes say what they lack.

Links into the explorer (version 5; tahoemap/links.py). The explorer (pipeline stage `explorer`) is the searchable
site of the run and holds every list in full. Every gene, drug, cell-line and module note starts with 'Explorer:
<url> · Map: <url>'; every list a note caps ends with '(k of N shown; all N in the explorer: <url>)'; a registry
text cut at MAX_TEXT characters ends in ' …' with the address of the full text; the Data sections name the explorer
pages, the explorer's data-repository file of the gene or drug-dose, and the files that stay on the computer that
made the run (atlas/effects, tensor: not exported to GitHub). The site URL is run(site_url=...) (None: the GitHub
Pages address of the code's repository, links.site_url_default); without one the notes name the run folder's
explorer/web/index.html. vault/.tahoemap-paths.json maps every gene (col), plates note (col), drug (name), cell
line (line index), module and plate to its note's path (relative to the vault folder), for the explorer.

Probable direction (the direction stage, OUT/direction; read through direction_view, which collapses, orders, caps
and words the arrows the same way for every surface): a gene note's "Direction (probable)" section lists the arrows
whose target is the gene (upstream: [[source]], its grade, what the source's activity does, the evidence with the
lines on each side, the size of the effect, q, the short labels of its alerts, notes and support) and those whose
source it is (downstream: [[target]], or the cells under [[drug]] at a dose), each list capped by the cap rule with its
counts and the caveats every arrow of its kinds carries (stated once above the list: direction_view.caveat_header);
At a glance names the strongest of each in one sentence; the frontmatter counts them (direction_upstream /
direction_downstream; null when the stage has not run). A drug note lists the genes that set how the cells fare under
it (sensitivity arrows at its doses) and the drug-target arrows of its compound classes (whether it moves the gene
that way too); a cell-line note its genotype groups (loss / gain of function / any record) and the genes it lacks
that served as natural knockouts, with the arrows each gave. A row that is one test for several sources names them
all. Concepts/Probable direction.md (linked from Home and from every direction section) explains kinds, grades, sign
and alerts, with this run's controls (direction/controls.json). The arrows of a gene are looked up by position
(direction_positions, built once; the same rows as dv.upstream / downstream / cells) and each row is worded once,
so 16,643 gene notes do not scan the edges. On an output without the stage every such section says that the stage
has not run there.

Version 7 (the second review wave) adds, each read from the stage that writes it and shown with its source: the
flags of record (common.ARTIFACT_FLAGS and the caveat tokens, whose words, common.FLAG_TEXT, stand once under the list
that shows them; the drug-doses and wells of a neighbouring-well flag); q 0 as '< 1e-45'; the per-line cut with 2
decimals; TP53 'not recorded (presumed wild type, not confirmed)'; in a gene's drug tables the wells behind 'lines up /
measured' (' · one well'), 'Pattern over the doses (each on its own plate)' and 'vs DMSO (rough)' (tables
lfc_vs_dmso: a sign check); At a glance's count rule (called: q < 0.10 and >= 1.2x; listed: |z| >= 3 or q < 0.10);
lineage-pair and read-sharing partners with their numbers; in a drug note both annotations (Tahoe verbatim, ChEMBL
with its release), an alert where they disagree, the mechanism classes with their sources, the salt-form note, each
dose's plate and well (drugs.parquet dose_plates), its neighbouring-well reading, unexpected similarity and selective
lines, the 10 most similar drug-doses of its best dose (of 50), the line-selective controls; in a line note the
drug-doses where it responds out of proportion (tables/drug_line_response.parquet) and its selectivity arrows; in a
module note the label as validate version 7 chose it, part by part, with its alerts and covariates; in the direction
tables 'false (group)', each family's caveat once, and how often a gene was tested (direction/gene_tests.parquet);
the counts on Home and the words in How to read this vault.

Literature reviews (optional; tahoemap/review, docs/review.md): when OUT/review holds reviews (review/notes/<kind>/,
review/reviews/<kind>/, review/connections.parquet), the note of every reviewed gene, drug or cell line gets a section
"## What the literature says": a callout (written by an AI agent: which agent, model and effort, the date, the
verification from the review's "verification" counts - ids checked, removed, not looked up, the citation check's
status and counts -, relative links to the run's history file and review JSON) above the agent's note body
(sanitize_note: no raw HTML, comment, image or link other than to PubMed / doi.org / Europe PMC / NCBI /
Cellosaurus, no autolinked URL, '//host' or e-mail address, no Dataview inline query, code fences closed; its
headings demoted below the note's own, its wikilinks kept only where a note exists), then its connection verdicts
(of the entity's latest review, review_rank; one per partner, pick_verdict), then the provenance line generated from the
verification (the review's note_footer; never the agent's own). A verdict is shown as verdict_label says: the shown
verdict (shown_verdict: 'unverified' when the citation check found it not supported or every citation was removed)
and its check_status, then ' (cites a retracted paper)' when one of its papers is retracted (a verdict whose only
papers are retracted reads 'unverified': a retracted paper is no support). The partner tables of a gene note get a
Literature column (the verdict of the gene's review, else of the partner's, with linked citations) when a shown
partner has a verdict; the map's badges use the same choice and labels. Verdicts come from
review/connections.parquet, or from the review JSONs when that table is older than a review (connections_stale) or
lacks the retracted column. The vault and map stamps record review_fingerprint(OUT), so a review run (or a new
LIT_RENDER) makes both out of date. Without reviews no note changes.
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
from . import common as CM
from . import direction_view as DV
from . import graph as GR
from . import links as LK
from . import mechanisms as MECH
from . import relations as REL
from . import tables as TB
from . import tensor as TN
from . import tlib as T
from .common import cap_keep as _cap_keep, folder, log, read_effects_index, replace_file, safe_filename, stamp_stage
# the sentence-level rule the runner applies to the notes it stores (verify imports only the standard library)
from .review.verify import ITEM_SECTIONS, drop_self_check as _verify_drop_self_check

VERSION = 8                          # 3: nothing is left out for a flag; flagged items carry an alert (ALERT);
#                                      4: the direction stage's arrows (gene, drug and line notes, Probable direction)
#                                      5: links into the explorer; every capped list says 'k of N shown' with a link
#                                         to all N; .tahoemap-paths.json; direction notes and kind caveats
#                                      6: Home's module table and its opposite-arm tests say 'k of N' too
#                                      7: the flags of record (common.ARTIFACT_FLAGS: + 'like a neighbouring well';
#                                         the caveat tokens with common.FLAG_TEXT); q 0 = '< 1e-45'; per-line cut with
#                                         2 decimals; TP53 'not recorded'; one well / pattern over the doses / vs DMSO
#                                         (rough); both drug annotations (Tahoe, ChEMBL) and classes; neighbouring
#                                         wells; similar drug-doses; line selectivity; module label parts and alerts;
#                                         lineage and read-sharing partners; false (group); gene tests
#                                      8: every named value (At a glance, In single lines, In which cell lines, the
#                                         predicted z) carries its caveats next to its alert; 'without an artifact flag'
GEN = "tahoemap"
SEED_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "vault_seed")
MANIFEST = ".tahoemap-manifest.json"
PATHS = ".tahoemap-paths.json"        # every note's path by entity (gene col, drug, line, module, plate): the explorer
LOCAL_EXPLORER = "explorer/web/index.html"   # the explorer of the run folder, when there is no site URL
LOCAL_MAP = "map/gene_map.html"

LFC_MIN = A.LFC_MIN                  # log2(1.2): the atlas's smallest counted change
Q_CUT = A.Q_CUT                      # 0.10
HOME_MODULES = 12                    # Home: the largest modules in its table ('k of N' and links to all N)
ARM_NAMES = 4                        # Home: genes named per module arm ('k of N' when the arm has more)
N_DRUGS = 15                         # drug-doses per direction in a gene note (cap_keep: + the strongest unflagged)
N_PARTNERS = 12
N_PRED = 5
N_GLANCE = 3                         # partners per direction in 'At a glance'
N_NEAR_DRUGS = 8                     # nearest drugs in a drug note (cap_keep: + the most similar without an alert)
N_SIMILAR = 10                       # most similar drug-doses of a drug's best dose (embed/drug_similarity: 10 of 50)
N_CANDIDATES = 15                    # candidate new members in a module note (cap_keep)
N_OWN_LEVEL = 15                     # genes per list in a line note's 'Its own level' (cap_keep)
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
ALERT = "⚠"                         # marks an item shown with a reason for doubt (it is never left out for one)
CC_FLAG = "cell-cycle shift"         # the drug-dose flag the tables stage refines per gene (cc_share)
N_GENES_DOSE = 12                    # genes per dose and direction in a drug note
N_LINE_LIST = 12                     # drug-doses / genes per list in a cell-line note
N_MOD_DRUGS = 10                     # drug-doses per direction in a module note
N_DIRECTION = 12                     # arrows per list (upstream / downstream) in a gene note (DV.cap: + the strongest
#                                      without an alert)
N_DIR_DRUG = 15                      # arrows per list in a drug note (DV.cap)
N_DIR_LINE = 15                      # groups per list in a cell-line note (cap_keep on the groups' alerts)
N_DIR_NAMES = 8                      # genes named per line set in a cell-line note (the rest counted)
DIR_NOTE = "Probable direction"      # the generated concept note on the direction stage's arrows (Concepts/)
DIR_NOT_RUN = ("The direction stage has not run on this output: `tahoe run` adds it, then rebuilds the validation "
               "report, this vault and the map.")
# a well of a plate note that carries one of these is shown with an alert
WELL_ALERTS = ("unreliable plate", "position not correctable", "not used in its drug-dose", "failed (excluded)")
# partner evidence that is a reason for doubt, in plain words (relations: evidence)
EVIDENCE_ALERT = {"one half": "one half only", "not reproduced": "not reproduced"}
SET_LABEL_SOURCES = ("control", "hallmark", "reactome")   # validate: a gene-set label (its q is the label's own)
COV_WORDS = (("umi_per_cell", "UMI per cell"), ("genes_per_cell", "genes per cell"), ("cells", "cells per well"),
             ("composition", "composition shift"), ("S_phase", "S-phase shift"), ("G2M_phase", "G2/M shift"))


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
    """A q (or fdr) value: '—' when missing, common.Q_ZERO ('< 1e-45') for a stored 0 (below what a float32 holds),
    '3e-05' below 0.001, else 3 decimals (2 from 0.1)."""
    if not _finite(q):
        return "—"
    q = float(q)
    if q == 0:
        return CM.Q_ZERO
    if q < 1e-3:
        return f"{q:.0e}"
    return f"{q:.3f}" if q < 0.1 else f"{q:.2f}"


def fq_text(t):
    """A q text made elsewhere (direction_view) with a stored 0 written as common.Q_ZERO, never '0e+00'."""
    return str(t).replace("0e+00", CM.Q_ZERO)


def fwells(n):
    """' · one well' / ' · 2 wells' after a 'lines up / measured' count: the lines are counted inside these wells
    (tables n_wells; '' when unknown)."""
    if not _finite(n) or int(n) <= 0:
        return ""
    return " · one well" if int(n) == 1 else f" · {int(n)} wells"


def fwells_of(n):
    """' of one well' / ' of 2 wells' after 'N of M measured lines' ('' when unknown)."""
    if not _finite(n) or int(n) <= 0:
        return ""
    return " of one well" if int(n) == 1 else f" of {int(n)} wells"


DMSO_MIN = math.log2(1.2)            # 'other sign against DMSO' needs |lfc_vs_dmso| >= this (the atlas's 1.2x)


def fdmso(lfc_vs_dmso, lfc):
    """The rough DMSO-referenced fold of a row (tables drug_effects lfc_vs_dmso: a sign check, not a replacement):
    '1.23×', with ' · other sign against DMSO' when its sign differs from lfc's and it is at least 1.2× either way;
    'no DMSO value' when the plate has none."""
    if not _finite(lfc_vs_dmso):
        return "no DMSO value"
    x = float(lfc_vs_dmso)
    t = f"{2.0 ** x:.2f}×"
    if _finite(lfc) and abs(x) >= DMSO_MIN and np.sign(x) != np.sign(float(lfc)) and float(lfc) != 0:
        t += " · other sign against DMSO"
    return t


def fpct(x):
    """A share as the direction stage prints it: 'under 1%' below 0.005, else whole percent."""
    if not _finite(x):
        return ""
    x = float(x)
    return "under 1%" if x < 0.005 else f"{int(round(100 * x))}%"


def tp53_text(status, short=False):
    """TP53 status of a line (tables lines.parquet tp53_status): 'not recorded' means no TP53 alteration in the
    metadata (presumed wild type, not confirmed); an older tables stage wrote 'wild type' for it."""
    s = str(status or "unknown")
    if short:
        return {"altered": "alt", "not recorded": "not rec.", "wild type": "wt", "unknown": "?"}.get(s, s)
    if s == "not recorded":
        return "not recorded (presumed wild type, not confirmed)"
    if s == "wild type":
        return "wild type (as an older tables stage wrote it: no TP53 alteration recorded, not confirmed)"
    return s


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


def _short_error(t, n=120):
    """An error message cut at n characters, ending in ' … (the full message: reference/sources.json)' when cut."""
    return t if len(t) <= n else t[:n].rstrip() + " … (the full message: `reference/sources.json`)"


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


# ----------------------------------------------------------------------------- alerts (nothing is left out for a flag)
def fshare(s):
    """A share (0..1) of a change as a percentage for an alert: '~60%', '<1%', 'all'."""
    s = float(s)
    if s >= 0.995:
        return "all"
    if 0 < s < 0.005:
        return "<1%"
    return f"~{round(100 * max(s, 0.0))}%"


def flag_parts(flags, cc_share=None):
    """A flags string (the flags of record: '; '-joined, the drug-dose's flags plus a gene's own) as (reasons,
    caveats). reasons: its artifact flags (common.ARTIFACT_FLAGS: atlas_core's seven and 'like a neighbouring well')
    in plain words, the items an alert names; a 'cell-cycle shift' with a finite cc_share (tables/drug_effects.parquet:
    the share of this gene's change the drug-dose's cell-cycle shift would explain) reads 'cell-cycle shift, explains
    ~N% of this change'. caveats: the other flags as they are, among them the gene-aware 'cell-cycle shift (explains
    ~N% here)' and common.CAVEAT_FLAGS ('like a neighbouring well (top dose)', '... (not this gene)', 'translation
    inhibitor', 'rise under a translation inhibitor'), which are no artifact flags (flag_legend gives their words)."""
    reasons, caveats = [], []
    for x in str(flags or "").split("; "):
        x = x.strip()
        if not x:
            continue
        if x in CM.ARTIFACT_FLAGS:
            if x == CC_FLAG and _finite(cc_share):
                share = fshare(cc_share)
                x = f"{CC_FLAG}, explains {share} of this change" if share != "all" else \
                    f"{CC_FLAG}, would explain all of this change"
            reasons.append(x)
        else:
            caveats.append(x)
    return reasons, caveats


def alert_text(flags, cc_share=None):
    """'⚠ ' and the artifact flags of a flags string in plain words (flag_parts), '' when it holds none."""
    reasons = flag_parts(flags, cc_share)[0]
    return f"{ALERT} " + "; ".join(reasons) if reasons else ""


def caveat_text(flags):
    """The flags of a flags string that are no artifact flags (soft caveats), '; '-joined."""
    return "; ".join(flag_parts(flags)[1])


def flag_tokens(flags_list):
    """The tokens of common.FLAG_TEXT (the neighbouring-well and translation-inhibitor flags) that occur in any of the
    flags strings, in FLAG_TEXT's order."""
    seen = set()
    for f in flags_list:
        seen.update(x.strip() for x in str(f or "").split("; "))
    return [t for t in CM.FLAG_TEXT if t in seen]


def flag_legend(flags_list, prefix="*", suffix="*"):
    """One line per new flag token present in the flags strings: '`token` (⚠, an artifact flag | a caveat, not an
    artifact flag): its words (common.FLAG_TEXT)'; [] when none. A note states each once, under its list."""
    out = []
    for t in flag_tokens(flags_list):
        kind = f"{ALERT} an artifact flag" if t in CM.ARTIFACT_FLAGS else "a caveat, not an artifact flag"
        out.append(f"{prefix}`{t}` ({kind}): {CM.FLAG_TEXT[t]}{suffix}")
    return out


def value_marks(flags, cc_share=None):
    """What a sentence prints right after one named value: its alert (alert_text) and its caveats, the flags that are
    no artifact flag ('caveat: rise under a translation inhibitor'), joined by ' · '; '' when it has neither. So a
    caveat such as a neighbouring well at the top dose or a rise under a translation inhibitor reaches the sentence
    a reader quotes, not only the table under it."""
    a, c = alert_text(flags, cc_share), caveat_text(flags)
    cv = (f"caveat{'s' if '; ' in c else ''}: {c}") if c else ""
    return " · ".join(x for x in (a, cv) if x)


def after_value(marks):
    """value_marks as they follow a value in a sentence: ' ⚠ toxic …' after an alert, ', caveat: …' otherwise ('' for
    none)."""
    if not marks:
        return ""
    return f" {marks}" if marks.startswith(ALERT) else f", {marks}"


def flags_cell(flags, cc_share=None, dash="—"):
    """A flags string for one table cell: the alert first (alert_text), then the soft caveats after ' · '."""
    a, c = alert_text(flags, cc_share), caveat_text(flags)
    return " · ".join(x for x in (a, c) if x) or dash


def cap_keep(alert, n):
    """Which items of a list ranked strongest first a note shows when the list is capped at n: the n strongest, and
    any of the n strongest without an alert (alert[i] True: item i carries one) that would fall outside them, in
    ranked order. So no item is pushed out of view by flagged ones. Returns their positions (common.cap_keep: the
    same rule everywhere)."""
    return _cap_keep(alert, n)


def n_alerts(k):
    """'3 with an alert ⚠' / 'none with an alert'."""
    return f"{k:,} with an alert {ALERT}" if k else "none with an alert"


def shown_text(n_all, n_alert, n_shown, n, extra):
    """The counts sentence of a capped list: how many in all, how many carry an alert, which are shown."""
    if not n_all:
        return "none"
    s = f"{n_all:,} in all, {n_alerts(n_alert)}"
    if n_shown < n_all:
        s += f"; shown: the {min(n, n_all):,} strongest"
        if extra:
            s += f" and the {extra:,} next strongest without an alert"
    return s


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
        self.keys = set()           # _pkey of every path: one note per file, also where names differ only in case
        self.n_written = 0
        self.n_same = 0
        self.bytes = 0

    def write(self, rel, text):
        if not text.endswith("\n"):
            text += "\n"
        path = os.path.normpath(os.path.join(self.root, rel))
        assert _pkey(path) not in self.keys, f"two notes at {rel}"
        self.paths.add(path)
        self.keys.add(_pkey(path))
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
        replace_file(tmp, path)
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


def _pkey(path):
    """A path as a comparison key: one separator, and case-folded where the file system ignores case (Windows), so
    'vault\\Genes/A/X.md' (a note path joined from a '/' name) and the 'vault\\Genes\\A\\X.md' os.walk yields are the
    same file."""
    return os.path.normcase(os.path.normpath(path))


def _rel_posix(path, root):
    """path relative to root with '/' separators (the manifest's form on every system)."""
    return os.path.relpath(path, root).replace(os.sep, "/")


def _clean_stale(root, keep, old_manifest):
    """Delete generated notes of an earlier build that this build did not write; never touch anything else."""
    removed = 0
    keep = {_pkey(p) for p in keep}
    old_manifest = {str(x).replace("\\", "/") for x in old_manifest}
    for dp, dn, fn in os.walk(root):
        dn[:] = [d for d in dn if not d.startswith(".")]
        for f in fn:
            p = os.path.join(dp, f)
            if _pkey(p) in keep:
                continue
            rel = _rel_posix(p, root)
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


def _columns(path):
    """The column names of a parquet file (empty when it is missing or unreadable)."""
    try:
        import pyarrow.parquet as pq
        return set(pq.read_schema(path).names)
    except Exception:  # noqa: BLE001
        return set()


def _factor(s):
    """A string column as an object array that shares one str per distinct value ('' for missing)."""
    codes, uniq = pd.factorize(s, use_na_sentinel=True)
    lut = np.array([sval(x) for x in uniq] + [""], dtype=object)
    return lut[np.where(codes < 0, len(uniq), codes)]


def parse_dose_plates(text):
    """tables drugs.parquet dose_plates ('0.05: plate1 H6, plate2 B2 / 0.5: plate3 C9') as {dose: [(plate, well)]}."""
    out = {}
    for part in str(text or "").split(" / "):
        dose, sep, rest = part.partition(": ")
        if not sep:
            continue
        pw = []
        for x in rest.split(", "):
            p_, _s, w_ = x.strip().rpartition(" ")
            if x.strip():
                pw.append((p_, w_) if p_ else (x.strip(), ""))
        out[dose.strip()] = pw
    return out


def _columns_csv(path):
    """The column names of a CSV file (its header line), as a set."""
    try:
        return set(pd.read_csv(path, nrows=0).columns)
    except (OSError, ValueError):
        return set()


def split_top(text, sep="; "):
    """text split at sep where no bracket is open ('a (x; y); b' -> ['a (x; y)', 'b'])."""
    out, depth, cur, i = [], 0, [], 0
    while i < len(text):
        ch = text[i]
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth = max(0, depth - 1)
        if depth == 0 and text.startswith(sep, i):
            out.append("".join(cur))
            cur = []
            i += len(sep)
            continue
        cur.append(ch)
        i += 1
    out.append("".join(cur))
    return [x.strip() for x in out if x.strip()]


def class_label_of(part):
    """The label of one '{label} ({sources})' class text: everything before its last top-level bracket."""
    part = part.strip()
    if not part.endswith(")"):
        return part
    depth = 0
    for i in range(len(part) - 1, -1, -1):
        if part[i] == ")":
            depth += 1
        elif part[i] == "(":
            depth -= 1
            if depth == 0:
                return part[:i].strip() or part
    return part


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
LIT_RENDER = 4                       # how reviews are drawn into notes and the map: part of review_fingerprint
RETRACTED_MARK = " (cites a retracted paper)"   # after the label of a verdict that cites a retracted paper
VERDICTS = ("established", "indirect", "plausible", "unexpected", "contradicted")   # submit_review's verdicts
STRENGTH = {"established": 5, "contradicted": 4, "indirect": 3, "plausible": 2, "unexpected": 1}
CHECK_STATUSES = ("supported", "partly", "not_supported", "not_checkable", "unchecked", "citations_removed")
VERIFIED = {"supported": 3, "partly": 2, "not_checkable": 1}        # check_status whose verdict stands, best first
UNVERIFIED = ("not_supported", "citations_removed")                 # shown as 'unverified'
CHECK_SHORT = {"supported": "supported", "partly": "partly supported", "not_checkable": "not checked",
               "unchecked": "ids not checked", "not_supported": "not supported",
               "citations_removed": "citations not found"}
CHECK_LONG = {"supported": "the citation checker found that the cited abstracts support it",
              "partly": "the citation checker found that the cited abstracts support only part of it",
              "not_checkable": "its cited ids exist, but the claim was not (or could not be) checked against the "
                               "abstracts",
              "unchecked": "its cited ids were not looked up (verification off, or PubMed / Crossref could not be "
                           "reached): not verified",
              "not_supported": "the citation checker found that the cited abstracts do not support it",
              "citations_removed": "every paper it cited was removed: the ids were not found in PubMed / Crossref"}
# markdown links the agent may keep in a note (anything else becomes its text): PubMed, DOIs, Europe PMC, NCBI,
# Cellosaurus
LIT_LINK_PREFIXES = ("https://pubmed.ncbi.nlm.nih.gov/", "https://doi.org/", "https://europepmc.org/",
                     "https://www.ncbi.nlm.nih.gov/", "https://www.cellosaurus.org/")
GENERIC_FOOTER = ("_AI-generated literature review of this run's data, not checked by a person. Verify before relying "
                  "on it._")                    # under a review stored without a generated note_footer


def review_fingerprint(out):
    """What of OUT/review the vault and the map show: None when there is no review (no folder, or only a queue, dry
    run or cache), else {"notes": n, "reviews": n, "sha": ...} over the names, sizes and modification times of the
    review notes and JSONs, the content of connections.parquet (rewritten at the end of every review run) and
    LIT_RENDER (how the reviews are drawn). The vault and map stamps record it, so a review run - or a change in how
    reviews are drawn - makes both out of date (cli.stage_state)."""
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
    h = hashlib.sha256("\n".join(sorted(items) + [f"render {LIT_RENDER}"]).encode("utf-8"))
    p = os.path.join(rd, "connections.parquet")
    if os.path.exists(p):
        with open(p, "rb") as fh:
            h.update(fh.read())
    return {**n, "sha": h.hexdigest()[:16]}


def _truthy(x):
    if isinstance(x, (bool, np.bool_)):
        return bool(x)
    if isinstance(x, str):
        return x.strip().lower() in ("true", "1", "yes")
    return _finite(x) and bool(float(x))


def connections_stale(out):
    """True when review/connections.parquet is older than a review JSON or than a change of the review folders (a
    review written, replaced or deleted after the table was last rebuilt: a run that was killed before its end,
    `tahoe review run` interrupted hard). The table is then ignored and the verdicts read from the JSONs."""
    rd = os.path.join(out, "review")
    p = os.path.join(rd, "connections.parquet")
    try:
        t = os.stat(p).st_mtime_ns
    except OSError:
        return False
    for kind in REVIEW_KINDS:
        d = os.path.join(rd, "reviews", kind)
        if not os.path.isdir(d):
            continue
        if os.stat(d).st_mtime_ns > t:
            return True
        for e in os.scandir(d):
            if e.name.endswith(".json") and e.stat().st_mtime_ns > t:
                return True
    return False


def _cid_list(x):
    """Citation ids from a list or from the 'PMID:1;DOI:x' string of review/connections.parquet; [] for anything
    else (missing, NaN)."""
    if isinstance(x, str):
        return [c.strip() for c in x.split(";") if c.strip()]
    if isinstance(x, (list, tuple, np.ndarray)):
        return [sval(c).strip() for c in x if sval(c).strip()]
    return []


def _cid_key(c):
    return re.sub(r"\s+", "", c).upper()


def retracted_cited(v):
    """The retracted papers among a connection verdict's citations, in the order recorded: verify.check_ids lists
    them in a review item's "retracted_citations" (a review/connections.parquet row: "retracted", 'PMID:1;DOI:x').
    [] when it cites none - also for a review or a table written before retractions were recorded."""
    ret = _cid_list(v.get("retracted")) or _cid_list(v.get("retracted_citations"))
    if not ret:
        return []
    cited = {_cid_key(c) for c in _cid_list(v.get("citations"))}
    return [c for c in ret if _cid_key(c) in cited]


def retracted_only(v):
    """True when a connection verdict cites papers and every one of them is retracted. A retracted paper is no
    support (the citations skill), so such a verdict has none: it is shown as 'unverified' (lit_status) and never
    picked as a verified verdict (pick_verdict)."""
    ret = retracted_cited(v)
    return bool(ret) and {_cid_key(c) for c in _cid_list(v.get("citations"))} <= {_cid_key(c) for c in ret}


def lit_status(v):
    """(check_status, shown_verdict) of a connection verdict - a review item or a review/connections.parquet row -
    as the shared verification contract defines them (docs/review.md, Verification). For a review stored before the
    contract (no check_status): from its older fields - the citation checker's 'check', 'unverified' with no
    citation left (every one removed) - else 'unchecked'. A verdict whose status is not_supported or
    citations_removed, or whose every citation is a retracted paper (retracted_only), is always shown as
    'unverified', whatever shown_verdict says; check_status stays the checker's."""
    verdict = sval(v.get("verdict")).strip()
    st = sval(v.get("check_status")).strip()
    if st not in CHECK_STATUSES:
        ck = v.get("check")
        ck = sval(ck.get("verdict") if isinstance(ck, dict) else ck).strip()
        cits = v.get("citations")
        n = len([x for x in (cits.split(";") if isinstance(cits, str) else cits or []) if str(x).strip()])
        if ck in ("supported", "partly", "not supported", "not checkable"):
            st = ck.replace(" ", "_")
        elif _truthy(v.get("unverified")) and not n:
            st = "citations_removed"
        else:
            st = "unchecked"
    shown = sval(v.get("shown_verdict")).strip()
    if st in UNVERIFIED or retracted_only(v):
        shown = "unverified"
    elif not shown:
        shown = verdict
    return st, shown


def _partner_id(r):
    pk = sval(r.get("partner_kind")) or "gene"
    pc = r.get("partner_col")
    if pk == "gene" and _finite(pc):
        return ("gene", int(pc))
    return (pk, sval(r.get("partner")).strip().upper())


def pick_verdict(vs):
    """The one verdict shown for a review's verdicts on one partner (the vault's partner tables and verdict list and
    the map's badge all use this rule): the strongest verified verdict - established, contradicted, indirect,
    plausible, unexpected, among those whose check_status is supported, partly or not_checkable and that cite
    something besides retracted papers (retracted_only); then the better check; then one that cites no retracted
    paper; then the first given - else, when none is verified, the agent's first."""
    ok = [(i, v) for i, v in enumerate(vs) if v.get("check_status") in VERIFIED and not retracted_only(v)]
    if not ok:
        return vs[0]
    return max(ok, key=lambda t: (STRENGTH.get(sval(t[1].get("verdict")), 0), VERIFIED[t[1]["check_status"]],
                                  not retracted_cited(t[1]), -t[0]))[1]


def review_rank(meta):
    """The order of two reviews of one entity (a review JSON's meta, or a review/connections.parquet row): the later
    'reviewed' time, then the later run_id. The vault's note and the verdicts of the vault and the map are the
    latest review's."""
    return (sval(meta.get("reviewed")), sval(meta.get("run_id")))


def _review_entity(d):
    """The entity a review (its meta) or a verdict row is about: its entity_id, else its kind and name."""
    return sval(d.get("entity_id")).strip() or f"{sval(d.get('kind'))}:{sval(d.get('name')).strip()}"


def _same_review(a, b):
    """Two review_rank()s of one entity name the same review: the same run (run_id), else the same time."""
    return (a[1] == b[1]) if a[1] and b[1] else a == b


def one_verdict_per_partner(rows):
    """rows (connection verdicts with check_status) -> one per (review, partner) by pick_verdict, in the order the
    partners first appear; each kept row gets n_verdicts (how many the review gave on that partner)."""
    groups = {}
    for r in rows:
        groups.setdefault((sval(r.get("entity_id")), _partner_id(r)), []).append(r)
    out = []
    for vs in groups.values():
        v = dict(pick_verdict(vs))
        v["n_verdicts"] = len(vs)
        out.append(v)
    return out


def review_connections(out, gene_col=None, one_per_partner=True):
    """The connection verdicts of the reviews in OUT/review, one dict per verdict with the columns of
    review/connections.parquet (entity_id, kind, name, partner, partner_kind, partner_col, verdict, citations as
    'PMID:1;DOI:x', retracted (the retracted ones among them, in the same form), check, unverified, check_status,
    shown_verdict, ...): from that table, else from the review JSONs - when the table is missing (not built yet:
    `tahoe review tables`), unreadable, older than a review (connections_stale: a review run that was killed before
    rebuilding it) or written before it had the retracted column. check_status / shown_verdict are always set
    (lit_status, also for reviews stored before they existed). Only the latest review of each entity counts
    (review_rank over the review JSONs, as the vault's note: an entity reviewed twice, in two files, shows the verdicts
    of the latest, in the vault and the map alike - even when the latest gave none). gene_col(name) -> col or None
    resolves gene partners the table left unresolved. one_per_partner: one verdict per (review, partner), by
    pick_verdict."""
    rd = os.path.join(out, "review")
    rows = None
    p = os.path.join(rd, "connections.parquet")
    if os.path.exists(p):
        if connections_stale(out):
            log(f"  literature: {p} is older than the review JSONs (the run that wrote them stopped before rebuilding "
                "it; `tahoe review tables` rebuilds it): verdicts read from the JSONs")
        else:
            try:
                tab = pd.read_parquet(p)
            except Exception as e:  # noqa: BLE001
                tab = None
                log(f"  literature: cannot read {p} ({type(e).__name__}: {e}); verdicts read from the review JSONs")
            if tab is not None and "retracted" not in tab.columns:
                log(f"  literature: {p} was written before it recorded retracted papers (`tahoe review tables` "
                    "rebuilds it): verdicts read from the review JSONs")
            elif tab is not None:
                rows = tab.to_dict("records")
    from_json, latest = rows is None, {}
    rows = [] if rows is None else rows
    for kind in REVIEW_KINDS:
        d = os.path.join(rd, "reviews", kind)
        for f in sorted(os.listdir(d)) if os.path.isdir(d) else []:
            r = _read_json(os.path.join(d, f)) if f.endswith(".json") else None
            if not isinstance(r, dict):
                continue
            meta = r.get("meta") or {}
            e, rank = _review_entity({"kind": kind, **meta}), review_rank(meta)
            if e not in latest or rank > latest[e]:
                latest[e] = rank
            if from_json:
                for it in r.get("connection_verdicts") or []:
                    if not isinstance(it, dict):
                        continue
                    pt = str(it.get("partner") or "")
                    pk = pt.split(":", 1)[0] if pt.split(":", 1)[0] in ("drug", "line") and ":" in pt else "gene"
                    cits = [str(x) for x in it.get("citations") or []]
                    ck = it.get("check")
                    rows.append({"entity_id": meta.get("entity_id"), "kind": kind, "name": meta.get("name"),
                                 "partner": pt, "partner_kind": pk, "partner_col": None, "verdict": it.get("verdict"),
                                 "citations": ";".join(cits), "n_citations": len(cits),
                                 "retracted": ";".join(_cid_list(it.get("retracted_citations"))),
                                 "check": ck.get("verdict", "") if isinstance(ck, dict) else sval(ck),
                                 "unverified": bool(it.get("unverified")),
                                 "check_status": it.get("check_status") or "",
                                 "shown_verdict": it.get("shown_verdict") or "", "model": meta.get("model"),
                                 "run_id": meta.get("run_id"), "reviewed": meta.get("reviewed")})
    own = {}                                    # an entity whose review JSON is gone (a table not rebuilt): its rows'
    for r in rows:
        e, rank = _review_entity(r), review_rank(r)
        if e not in latest and (e not in own or rank > own[e]):
            own[e] = rank
    latest.update(own)
    rows = [r for r in rows if _same_review(review_rank(r), latest[_review_entity(r)])]
    for r in rows:
        r["check_status"], r["shown_verdict"] = lit_status(r)
    if gene_col is not None:
        for r in rows:
            if sval(r.get("partner_kind")) in ("", "gene") and not _finite(r.get("partner_col")):
                c = gene_col(sval(r.get("partner")))
                r["partner_col"] = c if c is not None else None
    return one_verdict_per_partner(rows) if one_per_partner else rows


def md_text(s):
    """Text from a review (a partner's name, a citation id, an error) safe inline in a note or a table cell: no HTML,
    link, emphasis, tag or wikilink syntax survives, and no '|' or line break."""
    s = re.sub(r"\s+", " ", sval(s)).strip().replace("|", "/")
    s = re.sub(r"([\\`*_\[\]#~=%$!])", r"\\\1", s)
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def citation_link(cid):
    """'PMID:123' -> [PMID:123](https://pubmed.ncbi.nlm.nih.gov/123/); 'DOI:10.x/y' -> a doi.org link (the DOI
    escaped in the text, percent-encoded in the URL); other text escaped (md_text)."""
    s = str(cid).strip()
    m = re.match(r"(?i)^(?:PMID\s*:?\s*)?(\d{1,9})$", s)
    if m:
        return f"[PMID:{int(m.group(1))}](https://pubmed.ncbi.nlm.nih.gov/{int(m.group(1))}/)"
    m = re.match(r"(?i)^(?:DOI\s*:\s*|https?://(?:dx\.)?doi\.org/)?(10\.\d{4,9}/[^\s<>\"'`\[\]{}|\\]+)$", s)
    if m:
        doi = m.group(1)
        return f"[DOI:{md_text(doi)}](https://doi.org/{urllib.parse.quote(doi, safe='/:;._-')})"
    return md_text(s)


def verdict_label(v):
    """(label, explanation) of a connection verdict (with check_status / shown_verdict, see lit_status): the label
    the vault's Literature column and the map's 'lit:' badge show - the shown verdict and the check, e.g.
    'established (supported)', 'indirect (ids not checked)', 'unverified' - followed by RETRACTED_MARK ' (cites a
    retracted paper)' when a paper it cites is retracted, and a sentence saying what the agent said and what the
    verification found. A verdict whose only papers are retracted (retracted_only) reads 'unverified (cites a
    retracted paper)': a retracted paper is no support."""
    st, shown = v.get("check_status") or "unchecked", v.get("shown_verdict") or sval(v.get("verdict"))
    verdict = sval(v.get("verdict")) or "?"
    n = int(v.get("n_citations") or 0) if _finite(v.get("n_citations")) else len(_cid_list(v.get("citations")))
    ret, only = retracted_cited(v), retracted_only(v)
    if st in UNVERIFIED or only:
        label = "unverified"
    elif st == "not_checkable" and not n:
        label = shown                                          # it cites nothing: nothing to check
    else:
        label = f"{shown} ({CHECK_SHORT.get(st, st)})"
    expl = f"the agent's verdict: {verdict}; " + ("it cites no paper" if st == "not_checkable" and not n
                                                  else CHECK_LONG.get(st, st))
    if ret:
        label += RETRACTED_MARK
        what = "a retracted paper" if len(ret) == 1 else f"{len(ret)} retracted papers"
        expl += (f"; it cites {what} ({', '.join(ret)}) and nothing else: a retracted paper is no support, so the "
                 "verdict is shown as unverified" if only else
                 f"; it cites {what} ({', '.join(ret)}), which is no support: the verdict rests on its other papers")
    return label, expl


# -- the agent's note: sanitised before it is spliced into a vault note
_FENCE_RE = re.compile(r"^[ \t]*(`{3,}|~{3,})(.*)$")
SAFE_FENCE_INFO = {"text", "txt", "plain", "python", "py", "r", "bash", "sh", "shell", "json", "yaml", "yml", "tsv",
                   "csv", "markdown", "md"}             # languages Obsidian shows as code (no plugin renders them)
# the opening tag of an element removed with its content (_drop_raw_elements); its closing tag: _RAW_CLOSE[name]
_RAW_OPEN = re.compile(r"<(script|style|iframe|object|embed|template|textarea|noscript|svg|math|xmp|title|select|"
                       r"frameset|noframes|applet|canvas|audio|video)\b[^<>]*>", re.I)
_RAW_CLOSE = {}
# any other tag, declaration or processing instruction; each alternative stops at the next '<' or '>', so no opener
# rescans the text after it (one left unclosed is escaped by the '&lt;' pass)
_TAG = re.compile(r"</?[A-Za-z][A-Za-z0-9:-]*(?:\s[^<>]*)?/?>|<![A-Za-z][^<>]*>|<\?[^<>]*\?>")
_BR = r"(?:[^\[\]\\]|\\.)"
# link text: escapes and one level of nested brackets, at most 300 items, never backtracked (possessive: no item can
# end on ']', so giving one back cannot find another match) and not started at an escaped '\[' - so a long run of
# '[' / '\[' costs linear time; longer or deeper link text is left to the catch-all in _sanitize_chunk
_LINK_TEXT = rf"(?<!\\)\[((?:{_BR}|\[{_BR}{{0,300}}+\]){{0,300}}+)\]"
_LINK_DEST = (r"\(\s*(<[^<>\n]*>|(?:[^\s()\\]|\\.|\((?:[^\s()\\]|\\.)*\))*)"          # destination
              r"(?:\s+(?:\"[^\"]*\"|'[^']*'|\([^()]*\)))?\s*\)")                     # optional title
_IMAGE = re.compile(r"!(?=\[(?!\^))" + _LINK_TEXT + rf"(?:{_LINK_DEST}|\[[^\]]*\])?", re.S)   # ![a](u), ![a][r], ![a]
_LINK = re.compile(_LINK_TEXT + _LINK_DEST, re.S)
# a line's container prefix: blockquote / callout markers ('>'), list markers, footnote labels ('[^1]:') and
# indentation, in any mix
_MARK = r"(?:>|(?:[-+*]|\d{1,9}[.)])(?=[ \t])|\[\^[^\[\]\s]+\]:)"
_CONTAINER = rf"(?:[ \t]*{_MARK})*[ \t]*"
# a reference definition '[label]: destination' at any container depth (top level, in a blockquote, callout or list
# item); its destination may be on the next line (after that line's own container prefix). A label starting with '^'
# is one too unless it is a footnote's ('[^1]:': no space, bracket or backslash in it) - '[^a b]:' and '[^a\]b]:' are
# definitions to a renderer with footnotes as well as to one without
_REFDEF = re.compile(rf"^({_CONTAINER})\[(?!\^[^\[\]\s\\]+\]:)((?:[^\[\]\\]|\\.)++)\]:[^\S\n]*(?:\n(?:[^\S\n]|>)*)?"
                     r"(<[^<>\n]*>|\S+)[^\n]*$", re.M)
# a fence opened inside a container ('> ```lang', '- ```lang', '1. ~~~lang'): sanitize_note handles top-level fences
_NESTED_FENCE = re.compile(rf"^((?:[ \t]*{_MARK})+[ \t]*)(`{{3,}}|~{{3,}})(.*)$", re.M)
# a footnote: a renderer without footnotes reads '[^1]: text' as a reference definition to its first word (entities
# decoded: 'javascript&colon;...'), so that word gets a zero-width space in front unless it is an allowed link
_FOOTNOTE_URL = re.compile(rf"^({_CONTAINER}\[\^[^\[\]\s]+\]:[^\S\n]*(?:\n(?:[^\S\n]|>)*)?)(?=\S)(\S*)", re.M)
# a markdown link (kept as it is: _LINK left only allowed ones), else what an autolinker may start a link at: a URL,
# a '//host' (linkify-it), an e-mail address's '@' (GFM, linkify-it) or 'mailto:' / 'xmpp:'
_LINK_OR_URL = re.compile(rf"({_LINK_TEXT}{_LINK_DEST})|(?:(?:https?|ftp)://|www\.)[^\s<>\[\]]*"
                          r"|(?<!\u200b)(?P<sl>//)|(?<!\u200b)(?P<at>@)(?=\S)|(?P<mt>mailto|xmpp)(?=:)", re.S | re.I)
# where a renderer's autolinker starts a URL (some start one inside a word: 'xhttps://...'): defanged with a zero-width
# space, so no bare URL to another site becomes a link
_URL_START = re.compile(r"(?i)((?:https?|ftp):)(//)|(www)(\.)")
# '/' and '@' written as a backslash escape or an entity: a renderer that autolinks after decoding them (markdown-it's
# linkify) would see '//host' or an e-mail address, so they are written plainly before the defanging
_SLASH_AT = re.compile(r"\\(.)|&(?:#0*(47|64)|#[xX]0*(2[fF]|40)|(sol|commat));", re.S)


def _plain_slash_at(t):
    """t with '\\/', '\\@', '&#47;', '&sol;', '&#64;', '&commat;' ... written as '/' and '@' (_SLASH_AT)."""
    def one(m):
        if m.group(1) is not None:                     # a backslash escape (pairs read left to right: '\\' stays)
            return m.group(1) if m.group(1) in "/@" else m.group(0)
        return "/" if (m.group(2) or m.group(3) or m.group(4)).lower() in ("47", "2f", "sol") else "@"
    return _SLASH_AT.sub(one, t)


# a Dataview inline query: a <code> whose text, trimmed (JavaScript's trim: any Unicode space, line break or BOM),
# starts with '=' or '$=' (Dataview runs them in code blocks too). A zero-width space before the '=' ends that: in a
# code span (after its backtick and any space or line break) and at the start of a line (after its container prefix:
# an indented or fenced code block, or a code span's next line)
_JS_WS = r"(?:\s|\ufeff)"
_DV_SPAN = re.compile(rf"(`)({_JS_WS}*+)(\$?=)")
_DV_LINE = re.compile(rf"^((?:[ \t]*+{_MARK})*+{_JS_WS}*+)(\$?=)")


def _fence_info(info):
    """A fence's info string kept only when it names a plain code language (SAFE_FENCE_INFO), else ''."""
    w = info.strip().split()
    return w[0].lower() if w and w[0].lower() in SAFE_FENCE_INFO else ""


def _refdef(m):
    """A reference definition (_REFDEF): to an allowed site, kept as '[label]: url' and closed by a blank line (no
    title, which some renderers let run over the lines after it, a fence included); else removed (a blockquote keeps
    its '>')."""
    quote = re.sub(r"[^>]", "", m.group(1))
    if not _lit_link_ok(m.group(3)):
        return quote
    return f"{m.group(1)}[{m.group(2)}]: {m.group(3)}\n{quote}"


def _plain_nested_fences(t):
    """t with the fences opened inside a container (_NESTED_FENCE) keeping only a plain code language."""
    return _NESTED_FENCE.sub(lambda m: m.group(0) if m.group(2)[0] == "`" and "`" in m.group(3) else
                             m.group(1) + m.group(2) + _fence_info(m.group(3)), t)


def _lit_link_ok(url):
    u = url.strip().strip("<>").strip()
    return u.startswith(LIT_LINK_PREFIXES) and not re.search(r"[\s\\<>\"']", u)


_DEST_AT = re.compile(_LINK_DEST)


def _inline_dest_ok(t, i):
    """True when t[i:] starts with an inline link destination '(url "title")' to an allowed site."""
    d = _DEST_AT.match(t, i)
    return bool(d) and _lit_link_ok(d.group(1))


def _drop_spans(t, start, end):
    """t without each span from `start` to the first `end` after it, left to right (as re.sub(start.*?end, '')
    would), in linear time: at the first opener with no `end` after it the scan stops (no later opener has one), and
    what is left unclosed stays (an unclosed '<!--' is escaped by the '&lt;' pass)."""
    out, keep = [], 0
    while True:
        i = t.find(start, keep)
        j = t.find(end, i + len(start)) if i >= 0 else -1
        if j < 0:
            break
        out.append(t[keep:i])
        keep = j + len(end)
    out.append(t[keep:])
    return "".join(out)


def _drop_raw_elements(t):
    """t without its script, style, iframe ... elements (_RAW_OPEN), each with its content up to the first closing tag
    of its name. An element left unclosed stays (the '&lt;' pass makes it text); a name whose closing tag is not
    found after one opener is not looked for again (none follows a later opener either): linear time, however many
    openers are left unclosed."""
    out, keep, pos, dead = [], 0, 0, set()
    while True:
        m = _RAW_OPEN.search(t, pos)
        if m is None:
            break
        name = m.group(1).lower()
        e = None
        if name not in dead:
            if name not in _RAW_CLOSE:
                _RAW_CLOSE[name] = re.compile(rf"</{name}\s*>", re.I)
            e = _RAW_CLOSE[name].search(t, m.end())
        if e is None:
            dead.add(name)
            pos = m.end()
            continue
        out.append(t[keep:m.start()])
        keep = pos = e.end()
    out.append(t[keep:])
    return "".join(out)


def _escape_lt(t):
    """'<' escaped wherever it could start a tag, a comment, a declaration or an autolink."""
    return re.sub(r"<(?=[A-Za-z/!?%])", "&lt;", t)


def _sanitize_chunk(t):
    """Text outside code fences (sanitize_note). Removals first; links and images are made text before reference
    definitions are removed (a link made text cannot leave a definition behind); then the defanging, and the '&lt;'
    pass once more at the end, so a tag or autolink that a removal or an un-escape put together ('<[img](x) src=x
    onerror=...>', '<\\url ...>') is text."""
    t = _drop_spans(t, "<!--", "-->")                              # HTML comments
    t = _drop_spans(t, "%%", "%%")                                 # Obsidian comments
    t = t.replace("%%", "")                                        # ... and an unclosed one
    t = _drop_raw_elements(t)                                      # script, style, iframe ... with their content
    t = re.sub(r"<([A-Za-z][A-Za-z0-9+.-]{1,31}:[^\s<>]*)>", lambda m: f"[{m.group(1)}]({m.group(1)})"
               if _lit_link_ok(m.group(1)) else m.group(1), t)   # autolinks: allowed ones as links, others text
    t = _TAG.sub("", t)                                            # any other HTML tag (its text is kept)
    t = _escape_lt(t)                                              # whatever could still start a tag
    t = t.replace("![[", "[[")                                     # no embedded notes
    t = _IMAGE.sub(lambda m: m.group(1), t)                        # no images (remote or not): their alt text
    t = _LINK.sub(lambda m: m.group(0) if _lit_link_ok(m.group(2)) else m.group(1), t)
    t = _REFDEF.sub(_refdef, t)                                    # ('[[r](x)]: url' is a definition by now)
    t = _plain_nested_fences(t)
    # what the patterns above cannot parse (link text with a code span, deeper brackets ...) is still no image or link:
    # '![' never starts an image, '](' never starts a destination other than an allowed one
    t = t.replace("![", "!\\[")
    t = re.sub(r"\]\(", lambda m: m.group(0) if _inline_dest_ok(t, m.end() - 1) else "]\\(", t)
    t = _FOOTNOTE_URL.sub(lambda m: m.group(0) if _lit_link_ok(m.group(2)) else m.group(1) + "\u200b" + m.group(2), t)
    t = re.sub(r"\\+(href|url)\b", r"\1", t)                   # no link from a LaTeX formula ('\\url' too)
    if t.count("$$") % 2:                                        # an unclosed display formula
        i = t.rfind("$$")
        t = t[:i] + "\\$\\$" + t[i + 2:]
    # what a removal above may have made: an Obsidian comment ('%<b></b>%'), a nested fence with a plugin language
    # ('> [```dataviewjs](x)'), a fence at the start of a line ('<b></b>```' - it would hide all that follows: text)
    t = _plain_nested_fences(re.sub(r"%{2,}", "%", t))

    def bare(m):                                                   # a bare URL elsewhere is not made a link
        if m.group(1) is not None:
            return m.group(0)
        if m.group("sl") or m.group("mt"):                         # '//host', 'mailto:'
            return "\u200b//" if m.group("sl") else m.group("mt") + "\u200b"
        if m.group("at"):                                          # an e-mail address (before the '@': no
            return "\u200b@"                                      # name of one ends there, for linkify-it too)
        u = m.group(0)
        keep = next((len(x) for x in LIT_LINK_PREFIXES if u.startswith(x)), 0) if _lit_link_ok(u) else 0
        rest = _URL_START.sub(lambda k: (k.group(1) or k.group(3)) + "\u200b" + (k.group(2) or k.group(4)), u[keep:])
        if not keep:                                               # (an allowed one: a URL inside it is defanged)
            rest = re.sub(r"(?<!\u200b)(//|@)", "\u200b\\1", rest)
        return u[:keep] + rest
    t = _LINK_OR_URL.sub(bare, _plain_slash_at(t))
    t = _DV_SPAN.sub("\\1\\2\u200b\\3", t)                         # no Dataview inline query (`= ...`, `$= ...`)
    t = _escape_lt(t)                                              # what the steps above may have put together
    out, prev = [], ""
    for line in t.split("\n"):
        f = _FENCE_RE.match(line)
        if f and not (f.group(1)[0] == "`" and "`" in f.group(2)):
            line = line[:f.start(1)] + "\\" + line[f.start(1):]
        if re.match(r"^ {0,3}(?:=+|-+)[ \t]*$", line) and prev.strip():   # no setext heading ('text' over '---')
            out.append("")
        line = _DV_LINE.sub("\\1\u200b\\2", line)                  # ... nor one in a code block
        out.append(line)
        prev = line
    return "\n".join(out)


def sanitize_note(md):
    """An agent's note made safe to splice into a vault note: code fences closed (an unclosed one closed at the
    end) and written plainly (no plugin languages such as dataviewjs or mermaid, nested fences in a blockquote,
    callout or list item too); outside them no HTML comment or Obsidian %% comment, no raw HTML (script, iframe, img,
    a, style ... any tag), no image (inline, reference or shortcut '![name]') or embedded note, no link or reference
    definition (at any container depth) other than to PubMed, doi.org, Europe PMC, NCBI and Cellosaurus (links keep
    their text; a bare URL, '//host' or e-mail address is not made a link), no Dataview inline query (a code span or
    code block whose text starts with '=' or '$=': the first line of a fence's code too) and no setext heading."""
    lines = sval(md).replace("\r\n", "\n").replace("\r", "\n").split("\n")
    out, chunk, fence, code = [], [], None, False
    for line in lines:
        m = _FENCE_RE.match(line)
        if fence is None:
            if m and not (m.group(1)[0] == "`" and "`" in m.group(2)):
                if chunk:
                    out.append(_sanitize_chunk("\n".join(chunk)))
                    if out[-1].split("\n")[-1].strip():       # a blank line first: no definition, link label or
                        out.append("")                          # title of the text above runs into the fence
                chunk = []
                fence, code = m.group(1), False
                out.append(fence + _fence_info(m.group(2)))
            else:
                chunk.append(line)
        elif m and m.group(1)[0] == fence[0] and len(m.group(1)) >= len(fence) and not m.group(2).strip():
            out.append(fence)
            fence = None
        else:
            if not code and not re.fullmatch(rf"{_JS_WS}*", line):    # the code's first text: Dataview reads it
                code = True                                           # trimmed, so its first '=' after spaces
                line = re.sub(rf"^({_JS_WS}*+)(\$?=)", "\\1\u200b\\2", line)
            out.append(line)
    if chunk:
        out.append(_sanitize_chunk("\n".join(chunk)))
    if fence is not None:
        out.append(fence)
    return "\n".join(out)


def drop_self_check(md):
    """The note without the sentences in which the agent vouches for its own verification (the vault appends the line
    generated from the verification instead), by the rule the runner applies to the notes it stores,
    verify.drop_self_check: a sentence made only of such a claim ('Citations were checked against PubMed and their
    abstracts.') and, in the same paragraph, disclaimer sentences ('AI-generated ...', 'Verify before relying on
    it'). A sentence that says anything more - a finding, a gene, a number ('Citations were checked, but none links
    PIR to HMOX1 in hypoxia.') - is kept whole, and so is the rest of its paragraph. Applied again here for notes
    stored before the runner applied it."""
    return _verify_drop_self_check(sval(md))


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
        self.dd_artifact = np.array([CM.has_artifact(f) for f in self.dd_flags])   # the flags of record
        self.dd_nsig = self.tdd["n_sig_genes"].to_numpy()
        # the drug's doses share a plate (tables version 5: drugs.parquet doses_share_a_plate; most drugs have each
        # dose on its own plate, so a pattern over the doses compares plates as much as doses)
        share = dict(zip(self.tdrugs["drug"].astype(str), self.tdrugs["doses_share_a_plate"].fillna(False)
                         .astype(bool))) if "doses_share_a_plate" in self.tdrugs else {}
        self.dd_share_plate = np.array([bool(share.get(d, False)) for d in self.dd_drug], dtype=bool)
        self.has_dose_plates = "dose_plates" in self.tdrugs
        # the neighbouring-well reading of each drug-dose (tables version 5; '' / -1 on an older tables stage)
        self.dd_nb_tier = self.tdd["nb_tier"].fillna("").astype(str).to_numpy() if "nb_tier" in self.tdd else \
            np.array([""] * self.Dn, dtype=object)
        self.dd_nb_partner = pd.to_numeric(self.tdd["nb_partner_dd"], errors="coerce").fillna(-1).astype(int) \
            .to_numpy() if "nb_partner_dd" in self.tdd else np.full(self.Dn, -1)

        # embed / graph / relations
        ed = os.path.join(out, "embed")
        eg = pd.read_parquet(os.path.join(ed, "genes.parquet")).set_index("col").reindex(np.arange(gK))
        self.included = eg["included"].fillna(False).astype(bool).to_numpy()
        self.n_resp = eg["n_responsive_contexts"].to_numpy()
        self.vnorm = eg["vector_norm"].to_numpy()
        self.vrep = eg["represented_fraction"].to_numpy()
        self.noise = eg["noise_rna"].fillna(False).astype(bool).to_numpy() if "noise_rna" in eg else \
            tg["noise_rna"].fillna(False).astype(bool).to_numpy()
        # in the space only through drug-doses that carry an alert, pooled and per line (newer embed stage)
        self.flagged_only = eg["evidence_flagged_only"].fillna(False).astype(bool).to_numpy() \
            if "evidence_flagged_only" in eg else np.zeros(gK, dtype=bool)
        self.has_flagged_only = "evidence_flagged_only" in eg
        # the gene's fitted slopes on the S-phase / G2-M module lfc (newer tables stage)
        self.cc_slopes = tg[["cc_slope_S", "cc_slope_G2M"]].to_numpy(dtype=float) \
            if {"cc_slope_S", "cc_slope_G2M"} <= set(tg.columns) else None
        self.embed_info = _read_json(os.path.join(ed, "info.json")) or {}
        # the stages' own cuts (tables: calibrated per-line |z|; relations: was novelty assessable; tensor: masks)
        ti = _read_json(os.path.join(td, "info.json")) or {}
        self.line_z_calibrated = _finite(ti.get("line_z_threshold"))
        self.line_z = float(ti["line_z_threshold"]) if self.line_z_calibrated else LINE_Z_FALLBACK
        self.line_z_chance = float(ti["line_z_expected_chance"]) if _finite(ti.get("line_z_expected_chance")) \
            else None
        self.line_z_ndd = ti.get("line_z_n_clean_drugdoses")
        self.line_fold = 2.0 ** float(ti.get("line_fold_min", LINE_FOLD_FALLBACK) or LINE_FOLD_FALLBACK)
        cc = ti.get("cell_cycle_rule") if isinstance(ti.get("cell_cycle_rule"), dict) else {}
        self.cc_safety = float(cc["safety_factor"]) if _finite(cc.get("safety_factor")) else 2.0   # the tables
        self.cc_max = float(cc["share_max"]) if _finite(cc.get("share_max")) else 0.5            # stage's rule
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
        self.mod_label_row = {}                        # every column of module_labels.csv (validate version 7)
        p = os.path.join(vd, "module_labels.csv")
        if os.path.exists(p):
            ml = pd.read_csv(p)
            for r in ml.to_dict("records"):
                self.mod_label[int(r["module"])] = (sval(r.get("label")), sval(r.get("label_source", "")),
                                                    r.get("label_q", np.nan))
                self.mod_label_row[int(r["module"])] = r
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
        p = os.path.join(td, "drug_effects.parquet")
        have = _columns(p)
        self.has_cc_share = "cc_share" in have          # newer tables stage: the cell-cycle share per row
        self.has_dmso = "lfc_vs_dmso" in have           # tables version 5: n_wells and the rough DMSO-referenced lfc
        de = pd.read_parquet(p, columns=["col", "dd", "lfc", "fold", "z", "q_up", "q_down", "flags", "clean",
                                         "n_lines_measured", "n_lines_up", "n_lines_down", "lines_up", "lines_down",
                                         "pattern_up", "pattern_down"] + (["cc_share"] if self.has_cc_share else [])
                             + [c for c in ("n_wells", "lfc_vs_dmso") if c in have])
        o = np.lexsort((-de["z"].to_numpy(dtype=float), de["col"].to_numpy()))
        self.de = {}
        for c in de.columns:
            if c in ("flags", "lines_up", "lines_down", "pattern_up", "pattern_down"):
                self.de[c] = _factor(de[c])[o]          # one string object per distinct value
            else:
                self.de[c] = de[c].to_numpy()[o]
        if not self.has_cc_share:
            self.de["cc_share"] = np.full(len(o), np.nan, dtype=np.float32)
        if "n_wells" not in self.de:                    # an older tables stage: the drug-dose's wells
            nw = pd.to_numeric(self.tdd["n_wells"], errors="coerce").to_numpy() if "n_wells" in self.tdd else \
                np.full(self.Dn, np.nan)
            self.de["n_wells"] = nw[self.de["dd"].astype(np.int64)]
        if "lfc_vs_dmso" not in self.de:
            self.de["lfc_vs_dmso"] = np.full(len(o), np.nan, dtype=np.float32)
        self.de_s = _slices(self.de["col"], gK)
        del de
        # line_effects: counts and bests over the clean drug-doses; a newer tables stage adds the same over all
        # drug-doses (suffix _all), which the notes then show, with how many of them carry an alert
        p = os.path.join(td, "line_effects.parquet")
        have = _columns(p)
        base = ["n_dd_up", "n_dd_down", "best_up_dd", "best_up_lfc", "best_up_z", "best_down_dd", "best_down_lfc",
                "best_down_z"]
        self.le_all = all(f"{c}_all" in have for c in base)
        opt = [f"best_{d}_{k}_all" for d in ("up", "down") for k in ("flags", "cc_share") if self.le_all
               and f"best_{d}_{k}_all" in have]                  # the flags of the strongest over all drug-doses
        opt += [f"best_{d}_flags" for d in ("up", "down") if f"best_{d}_flags" in have]   # the clean best's caveats
        le = pd.read_parquet(p, columns=["col", "line", "baseline_cpm", "expressed"] + base
                             + ([f"{c}_all" for c in base] if self.le_all else []) + opt)
        o = np.lexsort((le["line"].to_numpy(), le["col"].to_numpy()))
        self.le = {c: (_factor(le[c]) if c.endswith(("_flags_all", "_flags")) else le[c].to_numpy())[o]
                   for c in le.columns}
        self.le_s = _slices(self.le["col"], gK)
        del le
        rp = os.path.join(self.out, "relations", "gene_relations.parquet")
        rhave = _columns(rp)
        rel = pd.read_parquet(rp, columns=["col_a", "col_b", "rank", "cos", "cos_half1", "cos_half2", "evidence",
                                           "fdr", "z_gene", "locus", "readthrough_risk", "distance_bp", "same_strand",
                                           "shared_gene_group", "shared_pathway", "string_score", "novel_candidate"]
                              + [c for c in ("alert", "n_lines_a", "n_lines_b", "lines_jaccard", "lineage_pair",
                                             "lineage_p", "read_sharing") if c in rhave])
        o = np.lexsort((rel["rank"].to_numpy(), rel["col_a"].to_numpy()))
        self.rel = {c: (_factor(rel[c]) if c in ("shared_pathway", "evidence", "alert", "read_sharing")
                        else rel[c].to_numpy())[o] for c in rel.columns}
        self.rel_s = _slices(self.rel["col_a"], gK)
        del rel
        # the strongest (drug-dose, line) cells per gene (per-line |z| >= the calibrated cut): the single-line view of
        # a gene whose pooled (median-over-lines) list is empty or short. An older tables stage ranked only clean
        # drug-doses and wrote no flags; a newer one ranks all of them and writes each cell's flags and clean
        p = os.path.join(td, "drug_line_top.parquet")
        have = _columns(p)
        self.dlt_flags = {"flags", "clean"} <= have
        cols = ["col", "direction", "dd", "line", "lfc", "z"] + (["flags", "clean"] if self.dlt_flags else []) \
            + (["cc_share"] if self.dlt_flags and "cc_share" in have else []) \
            + (["pooled_lfc"] if "pooled_lfc" in have else [])
        dlt = pd.read_parquet(p, columns=cols) if os.path.exists(p) else pd.DataFrame({c: [] for c in cols})
        o = np.lexsort((-np.abs(dlt["z"].to_numpy(dtype=float)), dlt["col"].to_numpy()))
        self.dlt = {c: (_factor(dlt[c]) if c == "flags" else dlt[c].to_numpy())[o] for c in dlt.columns}
        if not self.dlt_flags:
            self.dlt["flags"] = np.array([""] * len(o), dtype=object)
            self.dlt["clean"] = np.ones(len(o), dtype=bool)
        if "cc_share" not in self.dlt:
            self.dlt["cc_share"] = np.full(len(o), np.nan, dtype=np.float32)
        cl = self.dlt["clean"]
        self.dlt["clean"] = cl if cl.dtype == bool else np.array([_truthy(x) for x in cl], dtype=bool)
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
        for k_ in ("pred_up", "pred_dn", "pred_up_c", "pred_dn_c"):         # _c: over drug-doses without an
            setattr(self, k_, np.full((gK, N_PRED), -1, dtype=np.int64))    # artifact flag (the cap rule)
            setattr(self, k_ + ("z" if k_.endswith("_c") else "_z"), np.full((gK, N_PRED), np.nan, dtype=np.float32))
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
        ok_dd = ~self.dd_artifact
        kc = min(N_PRED, int(ok_dd.sum()))

        def ends(P, k, sgn):
            """The k largest (sgn 1) or smallest (sgn -1) of each row of P, strongest first, and their values."""
            t = np.argpartition(-sgn * P, k - 1, axis=1)[:, :k]
            t = np.take_along_axis(t, np.argsort(-sgn * np.take_along_axis(P, t, 1), axis=1), 1)
            return t, np.take_along_axis(P, t, 1)
        for i0 in range(0, len(inc), chunk):
            cc = inc[i0:i0 + chunk]
            P = (G[cc].astype(np.float32) @ Dv.T) * sc[i0:i0 + chunk, None] + mu[i0:i0 + chunk, None]
            P = np.nan_to_num(P, nan=0.0)
            self.pred_up[cc, :k], self.pred_up_z[cc, :k] = ends(P, k, 1)
            self.pred_dn[cc, :k], self.pred_dn_z[cc, :k] = ends(P, k, -1)
            if kc:
                for sgn, ix, iz in ((1, self.pred_up_c, self.pred_up_cz), (-1, self.pred_dn_c, self.pred_dn_cz)):
                    t, v = ends(np.where(ok_dd[None, :], P, -sgn * np.inf), kc, sgn)
                    ix[cc, :kc], iz[cc, :kc] = t, v
        self.DD_z = np.load(os.path.join(self.out, "atlas", "effects", "DD_z.npy"), mmap_mode="r")


# ----------------------------------------------------------------------------- direction (OUT/direction)
DIR_STR = ("source", "target", "target_type", "kind", "grade", "mechanism", "alerts", "top_drugdoses", "compounds",
           "compounds_supporting", "drug_effect", "target_drug", "target_dose", "group", "notes", "caveats",
           "support", "reading")                                                        # dv.rows, read as text
DIR_NUM = ("source_col", "target_col", "target_dd", "sign", "n_altered", "n_intact", "n_lines", "contrast",
           "retained_fraction", "rise_share", "baseline_log2_diff", "r", "r_reverse", "n_compounds", "n_supporting",
           "background_rate", "p", "q", "q_group", "n_sources", "order", "n_notes", "false_share",
           "false_share_upper", "nonspecific_share")                                  # ... and as numbers
_NO_ROWS = np.zeros(0, dtype=np.int64)


def direction_positions(dv):
    """Per gene col, the positions in dv.rows (= their rank in ORDER, ascending) of the display rows that
    direction_view's upstream / downstream / cells return for that col: {'up': {col: positions}, 'down': ...,
    'cells': ...}, built in one pass over the rows, so that 16,643 gene notes look their arrows up without a
    DataFrame each (tests/checks.py compares them with the look-ups)."""
    out = {"up": {}, "down": {}, "cells": {}}
    r = dv.rows
    if not len(r):
        return out
    cells = r["target_type"].astype(str).isin(DV.DRUGDOSE_TARGETS).to_numpy()     # cells and the response to a dd
    tc = r["target_col"].to_numpy(dtype=np.int64)
    for i, (cols, isc) in enumerate(zip(r["source_cols"].tolist(), cells)):
        d = out["cells" if isc else "down"]
        for c_ in cols:
            if int(c_) >= 0:
                d.setdefault(int(c_), []).append(i)
        if not isc and tc[i] >= 0:
            out["up"].setdefault(int(tc[i]), []).append(i)
    for d in out.values():
        for k in d:
            d[k] = np.unique(np.array(d[k], dtype=np.int64))
    return out


# ----------------------------------------------------------------------------- the vault
class Vault:
    def __init__(self, out, site_url=None):
        self.out = out
        self.site = LK.site_url(site_url)        # the explorer's site URL (None: no site; links name the local files)
        self.data_url = LK.data_url_default() if self.site else None
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
                  "Lines by organ", "Genes below the detection limit", DIR_NOTE):
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

    # ------------------------------------------------------------------ links into the explorer (tahoemap/links.py)
    def xu(self, fn, *a, **k):
        """An explorer address: fn is a links builder (links.gene, links.drug, ...); without a site URL the same route
        in the run folder's own explorer (explorer/web/index.html#/...)."""
        return fn(self.site or LOCAL_EXPLORER, *a, **k)

    def xl(self, url):
        """An address as the note writes it: <url> (a link in Obsidian), or the local file in code when there is no
        site URL."""
        if self.site:
            return f"<{url}>"
        return f"`{url}` (in the run folder, once the explorer stage has run)"

    def xgene(self, c, tab=None, sub=None):
        return self.xu(LK.gene, self.R.label[int(c)], tab, sub)

    def xdrug(self, d, tab=None):
        return self.xu(LK.drug, d, tab)

    def xdd(self, dd, tab=None):
        return self.xu(LK.dd, int(dd), tab)

    def xline(self, line, tab=None):
        return self.xu(LK.line, self.R.cell[int(line)], tab)

    def xmodule(self, m):
        return self.xu(LK.module, int(m))

    def kofn(self, k, n, url, what=""):
        """'(15 of 41 shown; all 41 in the explorer: <url>)' after a capped list."""
        w = f" {what}" if what else ""
        return f"({k:,} of {n:,}{w} shown; all {n:,} in the explorer: {self.xl(url)})"

    def clip_full(self, text, c):
        """A registry text cut at MAX_TEXT characters (clip_text: it then ends in ' …'), followed by where the full
        text is when it was cut."""
        t = clip_text(text)
        if t.endswith(" …") and len(t) < len(re.sub(r"\s+", " ", str(text)).strip()):
            t += f" (cut at {MAX_TEXT} characters; the full text: {self.xl(self.xgene(c, 'annotation'))})"
        return t

    def top_line(self, xurl, map_label=None):
        """The first line of a gene, drug, line or module note: where its complete data are, and the map."""
        m = LK.map_gene(self.site, map_label) if self.site else (
            LOCAL_MAP + (f"#{LK.q(map_label)}" if map_label else ""))
        return f"Explorer: {self.xl(xurl)} · Map: {self.xl(m) if self.site else f'`{m}` (in the run folder)'}"

    def mod_label_text(self, m):
        """The validation stage's label of a module, as label_display shows it (the label with its ⚠ tags; validate
        version 7: a gene set, a driving drug class or a lineage); '' when it only names the module's top genes."""
        lab = self.R.mod_label.get(int(m))
        if not lab or not lab[0] or lab[1] in ("top genes", "") or lab[0].startswith("genes: "):
            return ""
        disp = sval((self.R.mod_label_row.get(int(m)) or {}).get("label_display"))
        return disp or lab[0]

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
                if old and review_rank(old["meta"]) > review_rank(meta):
                    continue                                    # two files for one entity: the latest review
                ftr = js.get("note_footer")
                self.lit[(kind, key)] = {
                    "kind": kind, "stem": stem, "text": text, "meta": meta,
                    "verification": js.get("verification") or {}, "summary": str(js.get("summary") or ""),
                    "items": {sec: [it for it in js.get(sec) or [] if isinstance(it, dict)] for sec in ITEM_SECTIONS}
                    if js else None,
                    "footer": ftr.strip() if isinstance(ftr, str) and ftr.strip() else GENERIC_FOOTER,
                    "review_rel": f"review/reviews/{kind}/{stem}.json" if js else None,
                    "note_rel": f"review/notes/{kind}/{stem}.md" if os.path.exists(np_) else None}
        # one verdict per (review, partner): review_connections applies pick_verdict, the rule the map uses too
        for r in review_connections(self.out, gene_col=lambda s: self._gene_by_name.get(str(s).upper())):
            eid = sval(r.get("entity_id"))
            kind = eid.split(":", 1)[0] if ":" in eid else sval(r.get("kind"))
            key = self.lit_key(kind, eid, sval(r.get("name")))
            if key is None or not sval(r.get("verdict")):
                continue
            rec = self.lit.get((kind, key))
            if rec is not None and sval(r.get("run_id")) and sval(rec["meta"].get("run_id")) and \
                    sval(r.get("run_id")) != sval(rec["meta"].get("run_id")):
                continue                                        # an older review of the same entity
            pk, pt = sval(r.get("partner_kind")) or "gene", sval(r.get("partner"))
            if pk == "gene":
                pc = r.get("partner_col")
                pkey = int(pc) if _finite(pc) and 0 <= int(pc) < R.gK else None
            else:
                pkey = self.lit_key(pk, pt, pt.split(":", 1)[1] if ":" in pt else pt)
            v = {"partner": pt, "pkey": (pk, pkey) if pkey is not None else None, "verdict": sval(r.get("verdict")),
                 "citations": [x.strip() for x in sval(r.get("citations")).split(";") if x.strip()],
                 "retracted": retracted_cited(r),
                 "check": sval(r.get("check")), "unverified": _truthy(r.get("unverified")),
                 "check_status": r["check_status"], "shown_verdict": r["shown_verdict"],
                 "n_verdicts": int(r.get("n_verdicts") or 1)}
            v["n_citations"] = len(v["citations"])
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
        """A connection verdict as the vault shows it (verdict_label: the shown verdict and its check, and ' (cites a
        retracted paper)' when it does; for an unverified one what the agent said), then the papers it cites, a
        retracted one marked '(retracted)'."""
        label, _expl = verdict_label(v)
        s = md_text(label)
        if v["check_status"] in UNVERIFIED:
            s += f" (agent: {md_text(v['verdict'])}; {CHECK_SHORT[v['check_status']]})"
        elif retracted_only(v):
            s += f" (agent: {md_text(v['verdict'])}; only retracted papers cited)"
        if int(v.get("n_verdicts") or 1) > 1:
            s += f" (of {int(v['n_verdicts'])} verdicts it gave)"
        if partner_review:
            s += f" ({md_text(partner_review)}'s review)"
        cits = v["citations"]
        ret = {_cid_key(x) for x in retracted_cited(v)}
        if cits:
            s += " · " + " ".join(citation_link(x) + (" (retracted)" if _cid_key(x) in ret else "")
                                  for x in cits[:LIT_CITES]) + \
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
            return md_text(v["partner"])
        kind, key = pk
        return self.glink(key) if kind == "gene" else self.dlink(key) if kind == "drug" else self.llink(key)

    @staticmethod
    def _verification_text(ver, meta, items=None):
        """The callout's verification sentence, from the review JSON's "verification" (the id look-ups: checked,
        removed, could not be checked, retracted; the citation check: done / not run / failed and its counts), for
        reviews stored before that form too. items: the review's items by section (connection_verdicts,
        established ...), when known: the claims shown as "unverified" are counted from them by the rule of the
        verdict labels (lit_status: not supported, every cited paper not found, or every cited paper retracted), and
        of the claims citing an id that was not looked up, those marked "ids not checked" are told from those the
        citation checker graded all the same (its verdict is shown: verify._item_status)."""
        cnt, ids, llm = ver.get("counts") or {}, ver.get("ids") or {}, ver.get("llm") or {}
        mode = ver.get("mode")

        def num(x):
            return len(x) if isinstance(x, (list, tuple)) else int(float(x)) if _finite(x) else 0

        def pl(k, one):
            return f"{k} {one}" + ("" if k == 1 else "s")

        def why(x):
            t = md_text(x)
            return t if len(t) <= 120 else t[:117] + "..."
        every = [(sec, it) for sec, its in (items or {}).items() for it in its or []]

        def ids_not_checked(all_citing):
            """What the claims citing an id not looked up show: all claims that cite (all_citing: no id was looked
            up), else those listing one in unchecked_citations."""
            its = [it for _sec, it in every if _cid_list(it.get("citations"))
                   and (all_citing or _cid_list(it.get("unchecked_citations")))]
            k = sum(1 for it in its if lit_status(it)[0] == "unchecked")
            g = sum(1 for it in its if lit_status(it)[0] != "unchecked" and sval(
                it["check"].get("verdict") if isinstance(it.get("check"), dict) else it.get("check")))
            if items is None or not g:
                return "the claims citing them are marked \"ids not checked\""
            gr = f"{'was' if g == 1 else 'were'} graded by the citation checker all the same (its verdict is shown)"
            if not k:
                return f"the {'claim' if g == 1 else 'claims'} citing them {gr}"
            return f"{pl(k, 'claim')} citing them {'is' if k == 1 else 'are'} marked \"ids not checked\", {g} {gr}"
        n_cited = num(cnt.get("n_citations")) if "n_citations" in cnt else num(ids.get("n_cited"))
        unchecked = num(ids.get("unchecked"))
        if mode not in ("ids", "llm"):
            return ("> Verification: none (the review ran with `--verify off`): its " + pl(n_cited, "cited paper")
                    + " were not looked up and its claims were not checked against the abstracts, so its verdicts "
                    "are marked \"ids not checked\".")
        ist = sval(ids.get("status"))
        if ist not in ("done", "not_run", "failed"):
            ist = "failed" if ids.get("error") else "done" if ids else "not_run"
        idet = sval(ids.get("detail") or ids.get("error"))
        s = f"> Verification: {pl(n_cited, 'paper')} cited"
        if ist == "done":
            removed = num(ids["removed"]) if "removed" in ids else num(ids.get("missing"))
            checked = num(ids["checked"]) if "checked" in ids else max(0, n_cited - unchecked)
            found = num(ids["found"]) if "found" in ids else max(0, checked - removed)
            if not unchecked:
                s += (f"; every cited id looked up in PubMed / Crossref: {found} found, {removed} removed as not "
                      "found")
            else:
                s += (f"; {checked} of the {pl(n_cited, 'cited id')} looked up in PubMed / Crossref ({found} found, "
                      f"{removed} removed as not found), {unchecked} could not be looked up (the service did not "
                      f"answer): {ids_not_checked(False)}")
            if num(ids.get("retracted")):
                s += f", {num(ids.get('retracted'))} retracted (still cited)"
            nr = num(ids.get("note_removed")) if "note_removed" in ids else num(cnt.get("note_removed"))
            if nr:
                s += f"; {pl(nr, 'paper')} cited only in the text removed"
        elif ist == "not_run":
            s += f"; the cited ids were not looked up ({why(idet or 'not run')}): {ids_not_checked(True)}"
        else:
            s += (f"; the id check failed ({why(idet or 'failed')}): no cited id was verified, and "
                  f"{ids_not_checked(True)}")
        if "not_retrieved_in_session" in ids:                # the id check ran: what it left cited
            nrs = num(ids["not_retrieved_in_session"])
        else:                                                # else the session's list, less the ids removed
            gone = {_cid_key(c) for c in _cid_list(ids.get("missing"))}
            nrs = len([c for c in _cid_list(meta.get("not_retrieved")) if _cid_key(c) not in gone])
        if nrs:
            s += f"; {pl(nrs, 'paper')} cited without having been read in the session (flagged)"
        if items is not None:
            kv = sum(1 for sec, it in every if sec == "connection_verdicts" and lit_status(it)[1] == "unverified")
            ko = sum(1 for sec, it in every if sec != "connection_verdicts" and lit_status(it)[1] == "unverified")
            what = " and ".join(([pl(kv, "connection verdict")] if kv else [])
                                + ([pl(ko, "other claim")] if ko else []))
            if what:
                s += (f"; {what} shown as \"unverified\" (no cited paper found, the cited abstracts do not support "
                      "it, or every paper it cites is retracted)")
        elif "status_not_supported" in cnt or "status_citations_removed" in cnt:
            k = num(cnt.get("status_not_supported")) + num(cnt.get("status_citations_removed"))
            if k:
                s += (f"; {k} shown as \"unverified\" (no cited paper found, or the cited abstracts do not "
                      "support it)")
        elif num(cnt.get("unverified_items")):
            k = num(cnt.get("unverified_items"))
            s += f"; {pl(k, 'item')} left unverified"
        raw = sval(llm.get("status"))
        if raw in ("done", "not_run", "failed") and "detail" in llm:
            lst, ldet = raw, sval(llm.get("detail"))
        elif raw == "done":
            lst, ldet = "done", ""
        elif raw.startswith("no claims"):
            lst, ldet = "done", "no claim cites a paper"
        elif not raw or raw.startswith(("not run", "not_run")):
            lst, ldet = "not_run", raw[7:].lstrip(": ") or "not run"
        else:
            lst, ldet = "failed", raw + (f": {sval(llm.get('error'))}" if llm.get("error") else "")
        if mode == "llm" and lst == "done" and ldet:
            s += ". No claim cites a paper, so none was checked against the abstracts."
        elif mode == "llm" and lst == "done":
            c4 = [num(llm[k]) if k in llm else num(cnt.get(k2)) for k, k2 in (
                ("supported", "supported"), ("partly", "partly"), ("not_supported", "not supported"),
                ("not_checkable", "not checkable"))]
            nc = num(cnt.get("claims_checked")) or sum(c4)
            checker = sval(meta.get("checker_model"))
            s += (". Claims checked against the abstracts they cite (`citation-checker`"
                  + (f", `{md_text(checker)}`" if checker else "") + f"): of {pl(nc, 'claim')}, {c4[0]} supported, "
                  f"{c4[1]} partly, {c4[2]} not supported, {c4[3]} not checkable.")
        elif mode == "llm":
            s += (". The claims were not checked against the abstracts (" + ("the check failed: " if lst == "failed"
                                                                              else "") + why(ldet or lst)
                  + "); `tahoe review run --recheck` completes the check without reviewing again.")
        else:
            s += ". The claims were not checked against the abstracts (`--verify ids`)."
        return s

    def sec_literature(self, kind, key, note_rel):
        """'## What the literature says' of a reviewed entity: the callout, the agent's note (sanitised:
        sanitize_note), its connection verdicts, and the provenance line generated from the verification counts
        (the review's note_footer; a paragraph in which the agent vouches for its own verification is dropped)."""
        rec = self.lit.get((kind, key))
        if rec is None:
            return []
        self.n_lit_notes += 1
        meta, ver = rec["meta"], rec["verification"]
        agent = md_text(sval(meta.get("agent")) or f"{kind}-reviewer")
        model = md_text(sval(meta.get("model")))
        served = [md_text(m) for m in (meta.get("served_models") or []) if m and m != sval(meta.get("model"))]
        when = md_text(sval(meta.get("reviewed"))[:10])
        how = ", ".join(([f"model `{model}`"] if model else [])
                        + ([f"in part by the fallback `{'`, `'.join(served)}`"] if served else [])
                        + ([f"effort {md_text(meta.get('effort'))}"] if sval(meta.get("effort")) else []))
        C = ["> [!info] AI-agent literature review",
             f"> Written by the `{agent}` agent" + (f" ({how})" if how else "") + (f" on {when}" if when else "")
             + ", from this run's data on it and the papers it retrieved. It is not checked by a person: read it as "
               "a lead, and check a claim in the cited paper before relying on it."]
        if not rec["review_rel"]:
            C.append(f"> No review record (`review/reviews/{kind}/{rec['stem']}.json`) was found for this note: its "
                     "model, date and verification are unknown.")
        else:
            C.append(self._verification_text(ver, meta, rec.get("items")))
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
        fence = None
        for line in sanitize_note(self.resolve_any(drop_self_check(rec["text"]))).split("\n"):
            f = re.match(r"^(`{3,}|~{3,})", line)
            if fence is None and f:
                fence = f.group(1)
            elif fence is not None and line == fence:
                fence = None
            m = None if fence is not None else re.match(r"^ {0,3}(#{1,6})(?:[ \t]+(.*?))?[ \t]*(?:[ \t]#+)?[ \t]*$",
                                                        line)
            if m:
                title = (m.group(2) or "").strip()
                if not any(x.strip() for x in body) and title.rstrip(":").lower() == LIT_HEADING.lower():
                    continue                                    # the vault supplies this heading
                if not title:
                    continue                                    # an empty heading
                if len(m.group(1)) < 3:                         # below the note's own '##' sections
                    line = "### " + title
            body.append(line)
        while body and not body[0].strip():
            body.pop(0)
        while body and not body[-1].strip():
            body.pop()
        L = [f"## {LIT_HEADING}", ""] + C + [""] + body + [""]
        vs = self.lit_verdicts.get((kind, key)) or []
        if vs:
            L += ["**Connection verdicts** of this review (`review/connections.parquet`; one per partner): " +
                  "; ".join(f"{self._plink(v)} {self._verdict_text(v)}" for v in vs) + ".", ""]
        L += [sanitize_note(rec["footer"]).strip() or GENERIC_FOOTER, ""]
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
        if inc and R.flagged_only[c]:
            tags.append("evidence-flagged-only")

        def num(k):
            return int(tg[k]) if k in tg and _finite(tg[k]) else 0
        fm = {"symbol": sym, "type": "gene", "col": c, "ensembl_id": sval(tg.get("ensembl_id")),
              "name": gname, "location": loc,
              "module": (m if m > 0 else 0) if inc else None, "arm": arm if (inc and m > 0) else None,
              "pooled_cpm": round(float(tg["pooled_cpm"]), 2) if _finite(tg["pooled_cpm"]) else None,
              "n_lines_expressing": int(tg["n_lines_expressing"]) if _finite(tg["n_lines_expressing"]) else None,
              "n_dd_up": num("n_dd_up"), "n_dd_down": num("n_dd_down"),
              "n_dd_up_clean": num("n_dd_up_clean"), "n_dd_down_clean": num("n_dd_down_clean"),
              "in_vector_space": inc}
        up, dn = self._dir_gene_rows(c) if self.dv is not None else (None, None)
        fm["direction_upstream"] = len(up) if up is not None else None      # arrows (None: the stage has not run)
        fm["direction_downstream"] = len(dn) if dn is not None else None
        if name != sym:
            fm["aliases"] = [sym]
        fm["tags"] = tags
        self.lit_frontmatter("gene", c, fm)
        L = [frontmatter(fm), f"# {R.label[c]}", "", self.top_line(self.xgene(c), R.label[c]), ""]
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
        L += self.sec_glance(c, tg, rows, self.dir_glance(c, up, dn) if up is not None else "")
        L += self.sec_drugs(c, tg, rows)
        L += self.sec_lines(c)
        L += self.sec_partners(c)
        L += self.sec_direction(c, up, dn)
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

    def gene_dd_flags(self, c, dd, rows=None):
        """(flags, cc_share) of drug-dose dd for gene c: the gene-level flags of its tables/drug_effects.parquet row
        (with the cell-cycle share), else of a tables/drug_line_top.parquet cell that carries flags, else the
        drug-dose's own flags (tables/drugdoses.parquet; then without the gene's position flags)."""
        R = self.R
        dd = int(dd)
        if rows is None:
            rows = np.arange(R.de_s[c], R.de_s[c + 1])
        r = self._de_row(rows, dd)
        if r is not None:
            return R.de["flags"][r], R.de["cc_share"][r]
        if R.dlt_flags:
            rr = np.arange(R.dlt_s[c], R.dlt_s[c + 1])
            hit = rr[R.dlt["dd"][rr] == dd]
            if len(hit):                     # a per-line cell reads the translation-inhibitor token from its own
                h = hit[0]                   # per-line sign: read it again from the pooled change (pooled_lfc)
                toks = [x for x in str(R.dlt["flags"][h] or "").split("; ") if x and x != CM.TL_RISE]
                pl_ = R.dlt["pooled_lfc"][h] if "pooled_lfc" in R.dlt else np.nan
                if CM.TL_DD in str(R.dd_flags[dd] or "").split("; ") and _finite(pl_) and float(pl_) > 0:
                    toks.append(CM.TL_RISE)
                return "; ".join(toks), R.dlt["cc_share"][h]
        return R.dd_flags[dd], np.nan

    def dd_alert(self, c, dd, rows=None):
        """The alert of drug-dose dd for gene c ('' when none; see gene_dd_flags and alert_text)."""
        return alert_text(*self.gene_dd_flags(c, dd, rows))

    def _strongest(self, c, tg, rows, key, d):
        """'X 5 µM: 2.1× (z +4.0, q 0.01, up in 5 of 9 measured lines)' for genes.parquet's best_* / best_clean_*,
        with its alert and its caveats (value_marks); (text, dd, alert). alert = the artifact flags only ('' when
        none), which decides whether the strongest without an artifact flag is named too."""
        de = self.R.de
        bdd = int(tg[f"{key}_dd"]) if _finite(tg.get(f"{key}_dd")) else -1
        if bdd < 0:
            return "", -1, ""
        r = self._de_row(rows, bdd)
        lines = ""
        if r is not None:
            nl = de["n_lines_up" if d == "up" else "n_lines_down"][r]
            lines = (f", {d} in {int(nl)} of {int(de['n_lines_measured'][r])} measured lines"
                     + fwells_of(de["n_wells"][r]))
            fl_, cs_ = de["flags"][r], de["cc_share"][r]
        else:
            fl_, cs_ = tg.get(f"{key}_flags"), None
        al, mk = alert_text(fl_, cs_), value_marks(fl_, cs_)
        txt = (f"{self.ddlink(bdd)}: {ffold(tg[f'{key}_fold'])} (z {fz(tg[f'{key}_z'])}, q {fq(tg[f'{key}_q'])}"
               f"{lines})" + after_value(mk))
        return txt, bdd, al

    def sec_glance(self, c, tg, rows, direction=""):
        R = self.R
        S = []
        if R.included[c] and R.flagged_only[c]:
            S.append(f"{ALERT} It is in the vector space only through drug-doses that carry an alert for it (its "
                     "significant pooled drug-doses and per-line responses; `embed/genes.parquet` "
                     "evidence_flagged_only): its vector, partners and module rest on "
                     "changes that may come from what those drug-doses did to the cells rather than from its own "
                     "regulation.")
        de = R.de
        zz = de["z"][rows].astype(float)
        for d in ("up", "down"):
            verb = "raised" if d == "up" else "lowered"
            nc = int(tg[f"n_dd_{d}_clean"]) if _finite(tg[f"n_dd_{d}_clean"]) else 0
            na = int(tg[f"n_dd_{d}"]) if _finite(tg[f"n_dd_{d}"]) else nc
            best, bdd, bal = self._strongest(c, tg, rows, f"best_{d}", d)
            side = (zz > 0) if d == "up" else (zz < 0)          # the rows of the list below (drug_effects)
            n_list = int(side.sum())
            k_list = int((~de["clean"][rows].astype(bool) & side).sum())
            base = " (vs the typical drug well on the same plate, not DMSO)" if d == "up" else ""
            listed = (f"The list below holds {n_list} drug-dose{'s' if n_list != 1 else ''} (|z| ≥ 3 or q < "
                      f"{Q_CUT:.2f}), {k_list} with {ALERT}.")
            rule = (f"by {na} drug-dose{'s' if na != 1 else ''} (q < {Q_CUT:.2f} and at least 1.2×; {na - nc} with "
                    f"{ALERT}). {listed}")
            if na > 0 and bdd >= 0:
                s = (f"Pooled over the cell lines (median), {verb} significantly{base} {rule} The strongest is "
                     f"{best}.")
                if bal:
                    cbest, cdd, _ = self._strongest(c, tg, rows, f"best_clean_{d}", d)
                    if nc > 0 and cdd >= 0 and cdd != bdd:
                        s += f" The strongest without an artifact flag is {cbest}."
                    elif nc == 0:
                        s += (" None of them is without an artifact flag." if na > 1 else "")
                S.append(s)
            elif na > 0:
                S.append(f"Pooled over the cell lines (median), {verb} significantly{base} {rule}")
            else:
                S.append(f"No drug-dose {'raises' if d == 'up' else 'lowers'} it significantly in the pooled "
                         f"(median-over-lines) data{base} (q < {Q_CUT:.2f} and at least 1.2×). {listed}")
            if nc < SHORT_POOLED:
                one = self._single_lines(c, d)
                if one:
                    S.append(one)
        if R.included[c]:
            rr = np.arange(R.rel_s[c], R.rel_s[c + 1])
            rep = self._replicated(rr)
            why = self._partner_alerts(c, rr, rep)
            parts, n_named = [], 0
            for sign, what in ((1, "moves with "), (-1, "moves opposite to ")):
                m_ = np.sign(R.rel["cos"][rr]) == sign
                ii, wy = rr[m_], why[m_]
                keep = cap_keep(wy != "", N_GLANCE)
                n_named += len(keep)
                if len(keep):
                    parts.append(what + ", ".join(
                        f"{self.glink(R.rel['col_b'][ii[k]])} ({fcos(R.rel['cos'][ii[k]])}, fdr "
                        f"{fq(R.rel['fdr'][ii[k]])}" + (f", {ALERT} {wy[k]}" if wy[k] else "") + ")"
                        for k in keep))
            if parts:
                S.append(f"Its strongest partners by |cos| ({int(rep.sum())} of its {len(rr)} nearest have the "
                         f"{REL.SAME_SIGN} with fdr ≤ {REPRO_FDR:.2f}; {int((why != '').sum())} carry an alert, "
                         f"{ALERT} + the reason: not the same sign in both halves, same locus, lineage, read-sharing "
                         "copies, or the partner in the vector space only through flagged drug-doses): it "
                         + "; ".join(parts) + " " + self.kofn(n_named, len(rr), self.xgene(c, "partners"), "partners")
                         + ".")
            else:
                S.append("It has no partner among its nearest genes (see the tables below).")
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
        if direction:
            S.append(direction)
        return ["## At a glance", "", "> [!summary] In this data"] + ["> " + x for x in S] + [""]

    def _single_lines(self, c, d):
        """'In single lines' sentence: the drug-doses that move the gene in the most lines at the calibrated per-line
        cut (tables/drug_line_top.parquet), '' when there are none. A drug-dose whose cells carry an artifact flag
        stays in its place with an alert, and the N_SINGLE strongest without one are named too (cap_keep). An older
        tables stage wrote only clean drug-doses to that table: then the sentence says so."""
        R, t = self.R, self.R.dlt
        rr = np.arange(R.dlt_s[c], R.dlt_s[c + 1])
        rr = rr[t["direction"][rr] == d]
        if not len(rr):
            return ""
        by = {}
        for r in rr:                                       # rows are strongest |z| first
            by.setdefault(int(t["dd"][r]), []).append(r)
        top = sorted(by.items(), key=lambda kv: (-len(kv[1]), -abs(float(t["z"][kv[1][0]])), kv[0]))
        al = [alert_text(t["flags"][lst[0]], t["cc_share"][lst[0]]) if not t["clean"][lst[0]] else ""
              for _, lst in top]
        mk = [value_marks(t["flags"][lst[0]], t["cc_share"][lst[0]]) for _, lst in top]   # alert and caveats
        keep = cap_keep([bool(x) for x in al], N_SINGLE)
        parts = []
        for k in keep:
            dd, lst = top[k]
            cells = ", ".join(f"{R.cell[int(t['line'][r])]} {flfc_fold(t['lfc'][r])}" for r in lst[:4]) + \
                (f", … ({len(lst) - 4} more lines)" if len(lst) > 4 else "")
            parts.append(f"{self.ddlink(dd)} in {len(lst)} line{'s' if len(lst) != 1 else ''} ({cells}"
                         + (f"; {mk[k]}" if mk[k] else "") + ")")
        verb = "raise" if d == "up" else "lower"
        cut = f"per-line |z| ≥ {R.line_z:.2f}" + ("" if R.line_z_calibrated else " (uncalibrated)")
        if R.dlt_flags:
            n_al = sum(1 for x in al if x)
            which = (f"all drug-doses: {len(top)} here, {n_alerts(n_al)}"
                     + (f"; the {len(keep)} shown" if len(keep) < len(top) else ""))
        else:
            which = "clean drug-doses only: this run's table, from an older tables stage, holds no flagged ones"
        return (f"In single lines ({cut}, {which}; `tables/drug_line_top.parquet`), these {verb} it: "
                + "; ".join(parts) + " " + self.kofn(len(keep), len(top), self.xgene(c, "lines"), "drug-doses")
                + ". The explorer shows every line at every drug-dose.")

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
        sig = (f"a significant pooled drug-dose (q < {Q_CUT:.2f}, ≥ 1.2×; one that carries an alert counts too, and "
               "then the gene is marked)" if R.has_flagged_only else
               f"a significant clean pooled drug-dose (q < {Q_CUT:.2f}, ≥ 1.2×)")
        txt += (f"; that count (≥ {need}) is not enough on its own: the space also needs {sig}" +
                (f" or a per-line |z| ≥ {float(lz):.2f} in ≥ 2 lines of one trustworthy drug-dose" if _finite(lz)
                 else "") + ", and it has neither")
        if _finite(ei.get("null_rate")):
            txt += f" (chance rate of |z| ≥ 3 per context: {g3(ei['null_rate'])})"
        if _finite(ei.get("n_genes_excluded_chance")):
            txt += (f"; {fint(ei['n_genes_excluded_chance'])} genes of this run reach the count without either "
                    "(at full scale almost every expressed gene does, by chance)")
        return txt

    def sec_drugs(self, c, tg, rows):
        """'Drugs that raise it / lower it': one ranked list per direction over every drug-dose of
        tables/drug_effects.parquet for the gene (|z| >= 3 or q < Q_CUT, flagged ones included). A drug-dose with an
        artifact flag stays in its ranked place with an alert (ALERT and the flags in plain words); the list shows the
        N_DRUGS strongest and any of the N_DRUGS strongest without an alert below them (cap_keep)."""
        R = self.R
        de = R.de
        L = []
        clean = de["clean"][rows].astype(bool)
        z = de["z"][rows].astype(float)
        cc_rows, shown_flags, shown_dd = [], [], []
        for d in ("up", "down"):
            title = "## Drugs that raise it" if d == "up" else "## Drugs that lower it"
            if d == "up":
                sel, al = rows[z > 0], ~clean[z > 0]
            else:
                sel, al = rows[z < 0][::-1], ~clean[z < 0][::-1]
            nc = int(tg[f"n_dd_{d}_clean"]) if _finite(tg[f"n_dd_{d}_clean"]) else 0
            na = int(tg[f"n_dd_{d}"]) if _finite(tg[f"n_dd_{d}"]) else nc
            L += [title, ""]
            one = self._single_lines(c, d) if nc < SHORT_POOLED else ""
            if not len(sel):
                L += [f"No drug-dose {'raises' if d == 'up' else 'lowers'} it in the pooled data (pooled over the "
                      f"cell lines, median: none with |z| ≥ 3 or q < {Q_CUT:.2f}). A response seen in fewer than "
                      "about half of the measured lines does not reach the pooled data; see "
                      f"[[#In which cell lines]]. Its value at every one of the {self.R.Dn:,} drug-doses: "
                      f"{self.xl(self.xgene(c, 'drugs'))}.", ""]
                L += [one, ""] if one else []
                continue
            keep = cap_keep(al, N_DRUGS)
            extra = int(np.sum(keep >= N_DRUGS))
            L += [f"*Pooled over the cell lines (median), against the typical drug well on the same plate (not "
                  f"DMSO). Every drug-dose with |z| ≥ 3 or q < {Q_CUT:.2f}, strongest "
                  f"first: {shown_text(len(sel), int(al.sum()), len(keep), N_DRUGS, extra)}. {na:,} of them "
                  f"{('raise' if d == 'up' else 'lower') + ('s' if na == 1 else '')} it significantly (**bold**: "
                  f"q < {Q_CUT:.2f}, ≥ 1.2×), {n_alerts(na - nc)}. "
                  + (f"{ALERT} = an artifact flag on the drug-dose or on this gene: the change may come from cell "
                     "death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce, "
                     "a well-position problem or a neighbouring well rather than from regulation of this gene; it is "
                     "shown, not left out. Lines up / measured: counted inside the drug-dose's well(s) (one well = "
                     "the lines are not replicate treatments). Each dose of a drug sits on its own plate, so the "
                     "pattern over the doses compares plates as much as doses. "
                     + ("vs DMSO (rough) = the same change measured against the plate's two DMSO wells "
                        "(`lfc_vs_dmso`): a sign check, not a replacement. " if R.has_dmso else "")
                     if d == "up" else f"{ALERT} and the columns as above. ")
                  + f"`tables/drug_effects.parquet` col == {c}.*", ""]
            L += [one, ""] if one else []
            body = []
            for k in keep:
                r = sel[k]
                q = de["q_up" if d == "up" else "q_down"][r]
                lfc = de["lfc"][r]
                sig = _finite(q) and q < Q_CUT and (lfc >= LFC_MIN if d == "up" else lfc <= -LFC_MIN)
                fo = ffold(de["fold"][r])
                nl = de["n_lines_up" if d == "up" else "n_lines_down"][r]
                names = [x for x in de["lines_up" if d == "up" else "lines_down"][r].split(", ") if x]
                ln = f"{int(nl)}/{int(de['n_lines_measured'][r])}" + fwells(de["n_wells"][r])
                if names:                          # every name the table holds (it names at most 12)
                    ln += " (" + ", ".join(names) + (f"; {int(nl) - len(names)} more" if int(nl) > len(names)
                                                     else "") + ")"
                fl = de["flags"][r] or ""
                if CC_FLAG in fl:
                    cc_rows.append(r)
                shown_flags.append(fl)
                ddr = int(de["dd"][r])
                shown_dd.append(ddr)
                pat = de["pattern_up" if d == "up" else "pattern_down"][r] or "—"
                if R.dd_share_plate[ddr]:
                    pat += " (doses share a plate)"
                body.append([self.ddlink(ddr), alert_text(fl, de["cc_share"][r]), f"**{fo}**" if sig else fo]
                            + ([fdmso(de["lfc_vs_dmso"][r], de["lfc"][r])] if R.has_dmso else [])
                            + [fz(de["z"][r]), fq(q), ln, pat, caveat_text(fl)])
            L += table(["Drug-dose", "Alert", "Fold"] + (["vs DMSO (rough)"] if R.has_dmso else [])
                       + ["z", "q", "Lines " + d + " / measured", "Pattern over the doses (each on its own plate)",
                          "Caveats"], body) + [""]
            L += [self.kofn(len(keep), len(sel), self.xgene(c, "drugs"), "drug-doses") + " The explorer's Drugs tab "
                  f"lists every one of the {self.R.Dn:,} drug-doses with its exact fold, z and q, flagged or not, and "
                  f"each one's {self.R.L} cell lines.", ""]
        if cc_rows:
            L += [self._cc_text(c), ""]
        L += self.flag_notes(shown_flags, shown_dd)
        return L

    def nb_text(self, dd, link=True):
        """The neighbouring-well reading of drug-dose dd in one line ('' when it has none): its tier, the partner
        drug-dose (linked to its drug note) and the wells (tables drugdoses.parquet nb_*)."""
        R = self.R
        dd = int(dd)
        tier = R.dd_nb_tier[dd] if 0 <= dd < R.Dn else ""
        if not tier:
            return ""
        p = int(R.dd_nb_partner[dd])
        t = R.tdd.iloc[dd]
        part = self.ddlink(p) if link and 0 <= p < R.Dn else cell(sval(t.get("nb_partner")))
        where = sval(t.get("nb_where"))
        return f"{self.ddlink(dd)} is like {part} in the well next to it" + (f" ({where})" if where else "") + \
            f"; tier '{tier}'"

    def flag_notes(self, flags_list, dds=()):
        """Under a list: the words of each new flag token in it (flag_legend), and for the neighbouring-well tokens the
        drug-doses and the wells that carry them (nb_text). [] when none."""
        lg = flag_legend(flags_list)
        if not lg:
            return []
        out = list(lg)
        nb = [t for t in (CM.NB_FLAG, CM.NB_TOP, CM.NB_CLEARED) if t in flag_tokens(flags_list)]
        if nb:
            seen, here = set(), []
            for f, dd in zip(flags_list, dds):
                if int(dd) in seen or not any(t in str(f).split("; ") for t in nb):
                    continue
                seen.add(int(dd))
                x = self.nb_text(dd)
                if x:
                    here.append(x)
            if here:
                out.append("*Neighbouring wells here: " + "; ".join(here) + ".*")
        return out + [""]

    def _cc_text(self, c):
        """What 'cell-cycle shift' means in a gene's lists (the tables stage's gene-aware rule), with the gene's own
        fitted cell-cycle slopes when the tables carry them."""
        R = self.R
        s = ("*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. "
             + ("Its alert says how much of this gene's change that shift would explain (`cc_share`), from the "
                "gene's own slopes on the S-phase and G2/M modules"
                + (f" (`tables/genes.parquet`: {flog(R.cc_slopes[c, 0])} per unit of S-phase module lfc, "
                   f"{flog(R.cc_slopes[c, 1])} per unit of G2/M module lfc)"
                   if R.cc_slopes is not None and np.isfinite(R.cc_slopes[c]).all() else "")
                + f". Fitted slopes are attenuated by noise, so the rule multiplies them by {R.cc_safety:g}: a row "
                  f"keeps the alert when the shift would then explain {100 * R.cc_max:g}% of the change or more, or "
                  "leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). "
                  "`cell-cycle shift (explains ~N% here)` = the "
                  f"shift explains only about N% of this change, and even with the slopes multiplied by "
                  f"{R.cc_safety:g} less than {100 * R.cc_max:g}%, so for this gene it is no artifact and carries no "
                  "alert."
                if R.has_cc_share else
                "This run's tables (an older tables stage) do not say how much of this gene's change the shift "
                "explains, so every such row carries the alert."))
        return s + "*"

    def line_cut_text(self):
        """The per-line cut as the tables stage set it, with the number of chance calls it lets through."""
        R = self.R
        if not R.line_z_calibrated:
            return (f"per-line |z| ≥ {R.line_z:.2f} (this run's tables carry no calibrated cut: a per-line z of 4-5 "
                    "can arise by chance)")
        ch = (f"; about {g3(R.line_z_chance)} such calls per gene and line are expected by chance over the "
              f"{fint(R.line_z_ndd)} clean drug-doses" if R.line_z_chance is not None else "")
        return f"per-line |z| ≥ {R.line_z:.2f} (calibrated on this run, `tables/info.json`{ch})"

    def _line_count(self, n_all, n_clean):
        """A per-line count cell: all drug-doses, and how many of them carry an alert ('3 (2 ⚠)')."""
        if not _finite(n_all):
            return "—"
        k = int(n_all) - int(n_clean if _finite(n_clean) else 0)
        return f"{int(n_all):,}" + (f" ({k:,} {ALERT})" if k > 0 else "")

    def sec_lines(self, c):
        """'In which cell lines': per line its level, how many drug-doses move the gene beyond the per-line cut and the
        strongest of them. With a tables stage that counts over all drug-doses (line_effects *_all) the counts and the
        strongest are over all of them, with how many carry an alert, and the strongest without an alert beside a
        flagged strongest one; an older tables stage counted only clean drug-doses, and the note says so."""
        R, le = self.R, self.R.le
        rows = np.arange(R.le_s[c], R.le_s[c + 1])
        drows = np.arange(R.de_s[c], R.de_s[c + 1])
        if R.le_all:
            what = (f"Up / down = drug-doses moving it ≥ {R.line_fold:.3g}× at {self.line_cut_text()}, all of them; in "
                    f"brackets how many of those carry an alert ({ALERT}: an artifact flag on the drug-dose or on "
                    "this gene). The strongest of them is shown, with its alert and its caveats (no artifact flag, "
                    "e.g. a rise under a translation inhibitor, read from the line's own change), and after it the "
                    "strongest without an artifact flag when that is another one, with its caveats.")
        else:
            what = (f"Up / down = clean drug-doses moving it ≥ {R.line_fold:.3g}× at {self.line_cut_text()}; the "
                    "strongest of them is shown. This run's `tables/line_effects.parquet` (an older tables stage) "
                    "counts only drug-doses without an artifact flag; a rebuilt tables stage counts all of them, with "
                    "alerts.")
        L = ["## In which cell lines", "",
             f"*`tables/line_effects.parquet` col == {c}. TP53: alt = altered; not rec. = no TP53 alteration "
             "recorded (presumed wild type, not confirmed). CPM = the line's own level (n.m. = not measured: the line "
             f"does not express it, or below {R.amb_frac:g} × its pooled level, where its reads are mostly ambient "
             f"RNA; no per-line values). {what} Most responsive lines first.*", ""]
        if not len(rows):
            return L + ["No per-line values.", ""]
        sfx = "_all" if R.le_all else ""
        nu = le["n_dd_up" + sfx][rows].astype(float)
        nd = le["n_dd_down" + sfx][rows].astype(float)
        order = sorted(range(len(rows)), key=lambda i: (-(np.nan_to_num(nu[i]) + np.nan_to_num(nd[i])),
                                                         R.cell[int(le["line"][rows[i]])].lower()))
        body = []
        for i in order:
            r = rows[i]
            line = int(le["line"][r])
            ex = bool(le["expressed"][r])

            def one(d, sx):
                """(dd, text with its alert and caveats, alert) of the line's strongest drug-dose (sx '_all': over
                all of them; '': without an artifact flag); the cell's own flags as the tables stage wrote them."""
                dd, z, lfc = le[f"best_{d}_dd{sx}"][r], le[f"best_{d}_z{sx}"][r], le[f"best_{d}_lfc{sx}"][r]
                if not (_finite(dd) and int(dd) >= 0 and _finite(z) and abs(float(z)) >= R.line_z):
                    return None, "", ""
                if not sx:
                    al = ""
                    mk = value_marks(le[f"best_{d}_flags"][r]) if f"best_{d}_flags" in le else ""
                elif f"best_{d}_flags_all" in le:              # the tables stage wrote the cell's own flags
                    cs = le.get(f"best_{d}_cc_share_all")
                    fl_, cs_ = le[f"best_{d}_flags_all"][r], cs[r] if cs is not None else None
                    al, mk = alert_text(fl_, cs_), value_marks(fl_, cs_)
                else:
                    al = mk = self.dd_alert(c, dd, drows)
                return int(dd), f"{self.ddlink(dd)} {flfc_fold(lfc)} (z {fz(z)})" + after_value(mk), al

            def best(d):
                dd, txt, al = one(d, sfx)
                if dd is None:
                    return "—"
                if al:
                    cdd, ctxt, _ = one(d, "")
                    if cdd is not None and cdd != dd:
                        txt += f" · without an artifact flag: {ctxt}"
                return txt
            if R.le_all:
                cu = self._line_count(le["n_dd_up_all"][r], le["n_dd_up"][r])
                cd = self._line_count(le["n_dd_down_all"][r], le["n_dd_down"][r])
            else:
                cu, cd = fint(nu[i], "—"), fint(nd[i], "—")
            body.append([self.llink(line), tp53_text(R.tp53[line], short=True),
                         g3(le["baseline_cpm"][r]) + ("" if ex else " n.m."),
                         cu if ex else "—", cd if ex else "—",
                         best("up") if ex else "—", best("down") if ex else "—"])
        return L + table(["Line", "TP53", "CPM", "Up", "Down", "Strongest up", "Strongest down"], body) + [
            "", f"Every line ({len(rows)}) is listed above, with its strongest drug-dose each way. Every drug-dose in "
            f"every line, with the exact per-line fold and z: {self.xl(self.xgene(c, 'lines'))}.", ""]

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
                notes.append(f"{ALERT} **readthrough risk**: {where} on the same strand (can correlate by "
                             "spillover, not regulation)")
            else:
                notes.append(f"{ALERT} same locus ({kb}{', same strand' if bool(rel['same_strand'][r]) else ''}: "
                             "neighbours can correlate without regulation)")
        return notes

    def _replicated(self, rr):
        """Per relation row: evidence 'both halves' (relations.SAME_SIGN: the same sign in both halves of the
        compounds, with fdr <= REPRO_FDR). Any other relation is shown with an alert."""
        rel = self.R.rel
        fdr = np.nan_to_num(rel["fdr"][rr].astype(float), nan=1.0)
        return (rel["evidence"][rr] == "both halves") & (fdr <= REPRO_FDR)

    def _partner_alerts(self, c, rr, rep=None):
        """Per relation row rr of gene c: the reasons to doubt the partner, in plain words ('; '-joined, '' = none):
        not the same sign in both halves of the compounds, same locus / read-through risk, the PARTNER in the vector
        space only through flagged drug-doses, and (relations version 5) the lineage and read-sharing reasons, which
        arrive through relations' 'alert' column (their words avoid the substrings filtered here). The
        note's own gene being in the space only through flagged drug-doses is said once in the note, not on every
        row (it would mark every partner, and the cap could then never add the strongest without an alert)."""
        R, rel = self.R, self.R.rel
        rep = self._replicated(rr) if rep is None else rep
        own = f"{R.sym[int(c)]} is in the vector space only through drug-doses that carry an alert"
        known = ("not replicated", "not reproduced", "reproducibility not tested", "read-through risk", "same locus",
                 "is in the vector space only through")
        out = []
        for k, r in enumerate(rr):
            why = []
            if not rep[k]:
                ev = rel["evidence"][r]
                why.append(EVIDENCE_ALERT.get(ev, f"{ev}, fdr above {REPRO_FDR:.2f}") + (
                    " (not the same sign in both halves)" if ev == "one half" else ""))
            if bool(rel["readthrough_risk"][r]):
                why.append("read-through risk")
            elif bool(rel["locus"][r]):
                why.append("same locus")
            b = int(rel["col_b"][r])
            if R.flagged_only[b]:
                why.append(f"{R.sym[b]} in the vector space only through flagged drug-doses")
            if "alert" in rel:                         # reasons of a newer relations stage that the above lacks
                for t in str(rel["alert"][r] or "").lstrip(ALERT).strip().split("; "):
                    if t and t != own and not any(x in t for x in known):
                        why.append(t)
            out.append("; ".join(why))
        return np.array(out, dtype=object)

    def _pair_numbers(self, r):
        """The numbers behind a pair's lineage and read-sharing alerts (relations version 5): 'lineage pair: lines 3 /
        3 of 18, J 1.00, lineage p 0.40' and 'read-sharing copies (paralogue)'; [] when the pair has neither."""
        R, rel = self.R, self.R.rel
        out = []
        if "lineage_pair" in rel and bool(rel["lineage_pair"][r]):
            p_ = rel["lineage_p"][r] if "lineage_p" in rel else np.nan
            j = rel["lines_jaccard"][r] if "lines_jaccard" in rel else np.nan
            na_, nb_ = ((rel[k][r] if k in rel else np.nan) for k in ("n_lines_a", "n_lines_b"))
            out.append(f"{ALERT} lineage pair: lines {fint(na_)} / {fint(nb_)} of {R.L}"
                       + (f", J {float(j):.2f}" if _finite(j) else "")
                       + (f", lineage p {fq(p_)}" if _finite(p_) else ""))
        if "read_sharing" in rel and sval(rel["read_sharing"][r]):
            out.append(f"{ALERT} read-sharing copies ({rel['read_sharing'][r]})")
        return out

    def sec_partners(self, c):
        R, rel = self.R, self.R.rel
        if not R.included[c]:
            return ["## Genes that move with it", "", "Not in the vector space, so no gene relations.", "",
                    "## Genes that move opposite", "", "Not in the vector space, so no gene relations.", ""]
        rows = np.arange(R.rel_s[c], R.rel_s[c + 1])
        L = []
        rep = self._replicated(rows)
        why = self._partner_alerts(c, rows, rep)
        alert = why != ""
        sels = {}
        for sign in (1, -1):                           # the N_PARTNERS strongest + the strongest without an alert
            m_ = np.sign(rel["cos"][rows]) == sign
            sels[sign] = (rows[m_][cap_keep(alert[m_], N_PARTNERS)], int(m_.sum()), int((m_ & alert).sum()),
                          int((m_ & ~rep).sum()))
        shown = [r for sign in (1, -1) for r in sels[sign][0]]
        lit = {int(rel["col_b"][r]): self.lit_partner_cell(c, rel["col_b"][r]) for r in shown} \
            if self.lit_pairs else {}
        if not any(lit.values()):                      # the Literature column only where a shown partner has one
            lit = {}
        self.n_lit_cells += sum(1 for v in lit.values() if v)
        for sign in (1, -1):
            sel, n_side, n_al, n_nrep = sels[sign]
            extra = max(0, len(sel) - N_PARTNERS)
            cnt = (f"*{n_side:,} of its nearest partners move {'with it' if sign > 0 else 'opposite'}, {n_al:,} of "
                   f"them with an alert ({ALERT}; {n_nrep:,} without the same sign in both halves of the compounds)"
                   + (f"; shown: the {N_PARTNERS} strongest" + (f" and the {extra} next strongest without an alert"
                                                                if extra else "") if len(sel) < n_side else "")
                   + ".* " + self.kofn(len(sel), n_side, self.xgene(c, "partners"))
                   + " The explorer also gives its correlation with every other gene.")
            if sign > 0:
                L += ["## Genes that move with it", "",
                      f"*Strongest of its {len(rows)} nearest partners by |cos| (`relations/gene_relations.parquet` "
                      f"col_a == {c}), and any of the {N_PARTNERS} strongest without an alert below them; halves = cos "
                      "in the spaces fitted on two random halves of the compounds (a hash split of the compound "
                      f"names). Evidence: `both halves` = the {REL.SAME_SIGN}: the same sign in both, |cos| ≥ "
                      f"{REL.REPRO_MIN:g} in each and fdr ≤ {REPRO_FDR:.2f} ({REL.SAME_SIGN_NOTE}); {ALERT} "
                      "`one half` = strong in one of the two random halves only — not the same sign in both, no error "
                      f"estimate; {ALERT} `not reproduced` = neither. Other alerts: {ALERT} same locus / read-through "
                      "risk (neighbours on the genome can correlate for that reason alone), lineage (both genes are "
                      "expressed in few lines, mostly the same: such genes move together whatever their regulation), "
                      "read-sharing copies (paralogues, pseudogenes or read-through transcripts: reads can be counted "
                      f"for either gene), and `GENE {ALERT}` = the partner is in the vector space only "
                      "through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with "
                      "an alert is shown in its place, not left out. A correlation across drugs and lines, not "
                      "evidence that one gene regulates the other.*",
                      ""]
                if not R.novel_assessed:
                    L += [f"*Novelty not assessed: {', '.join(R.novel_blocked) or 'reference sources'} missing "
                          "(`relations/info.json`), so no pair is called a novel candidate; the known-link notes "
                          "below cover only the sources that loaded.*", ""]
            else:
                L += ["## Genes that move opposite", ""]
            if not len(sel):
                L += ["None among its nearest partners." if sign > 0 else
                      "None among its nearest partners: everything close to it moves the same way.", ""]
                continue
            L += [cnt, ""]
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
                notes += self._pair_numbers(r)
                ev = rel["evidence"][r]
                if rep[r - rows[0]]:                   # rows is one contiguous slice of the relation table
                    ev_cell = ev
                elif ev == "one half":
                    ev_cell = f"{ALERT} one half (not the same sign in both halves)"
                elif ev == "not reproduced":
                    ev_cell = f"{ALERT} not reproduced"
                else:
                    ev_cell = f"{ALERT} {ev} (fdr above {REPRO_FDR:.2f}: not counted as the same sign in both halves)"
                if R.flagged_only[b]:
                    notes.append(f"{ALERT} in the vector space only through flagged drug-doses")
                body.append([self.glink(b) + (f" {ALERT}" if R.flagged_only[b] else ""), fcos(rel["cos"][r]),
                             f"{fcos(rel['cos_half1'][r])} / {fcos(rel['cos_half2'][r])}", ev_cell,
                             fq(rel["fdr"][r]), "; ".join(notes)] + ([lit.get(b) or "—"] if lit else []))
            L += table(["Gene", "cos", "Halves", "Evidence", "fdr", "Notes"] + (["Literature"] if lit else []),
                       body) + [""]
        if lit:
            L += [f"*Literature = the connection verdict of the AI-agent literature review of this gene (see "
                  f"\"{LIT_HEADING}\"), else of the partner's review (named), with the papers it cites "
                  "(`review/connections.parquet`): established, indirect, plausible, unexpected or contradicted, "
                  "and in brackets its check: supported / partly supported (the citation checker read the cited "
                  "abstracts), not checked (the ids exist; the claim was not checked against the abstracts), ids not "
                  "checked (not looked up). **unverified** = the cited abstracts do not support the agent's verdict, "
                  "or none of its papers exists, or all of them are retracted (the agent's verdict follows in "
                  "brackets). (cites a retracted paper) = a paper it cites is retracted, marked (retracted) after its "
                  "link: a retracted paper is no support.*", ""]
        return L

    # ------------------------------------------------------------------ direction (direction_view; OUT/direction)
    def load_direction(self):
        """The direction stage's arrows (direction_view.load: collapsed, in ORDER, indexed), and once per build: per
        gene col the positions of its rows (direction_positions: what dv.upstream / downstream / cells return), the
        columns the notes read as plain arrays (one str object per distinct value), the arrows per comparison group
        and the groups per cell line. So a note looks its arrows up and reads its rows from arrays instead of
        scanning the edges or building a DataFrame per note. self.dv is None when the stage has not run."""
        self.dv = DV.load(self.out)
        self.gene_tests, self.selectivity = {}, {}
        self.dir_by_group, self.dir_line_groups, self.dir_line_intact = {}, {}, {}
        self.dir_pos, self.dir_col, self._dir_memo, self._dir_cnt_memo = {"up": {}, "down": {}, "cells": {}}, {}, \
            {}, {}
        if self.dv is None:
            log("  vault: no direction stage in this output (direction/edges.parquet): its sections say so")
            return
        r = self.dv.rows
        self.dir_pos = direction_positions(self.dv)
        # direction version 5: per gene the tests it took part in (gene_tests.parquet) and per drug-dose its selective
        # lines and the groups that explain them (selectivity.parquet)
        gtp = os.path.join(self.out, "direction", "gene_tests.parquet")
        if os.path.exists(gtp):
            gt = pd.read_parquet(gtp)
            for c_, kind, role, n_t, n_e in zip(gt["col"].astype(int), gt["kind"].astype(str), gt["role"].astype(str),
                                                gt["n_tests"].astype(int), gt["n_edges"].astype(int)):
                if c_ >= 0:
                    self.gene_tests.setdefault(int(c_), []).append((kind, role, int(n_t), int(n_e)))
        sp_ = os.path.join(self.out, "direction", "selectivity.parquet")
        if os.path.exists(sp_):
            for rec in pd.read_parquet(sp_).to_dict("records"):
                self.selectivity[int(rec["dd"])] = rec
        for c_ in DIR_STR:
            self.dir_col[c_] = _factor(r[c_]) if c_ in r else np.full(len(r), "", dtype=object)
        for c_ in DIR_NUM:
            self.dir_col[c_] = pd.to_numeric(r[c_], errors="coerce").to_numpy(dtype=float) if c_ in r else \
                np.full(len(r), np.nan)
        for c_ in ("sources", "source_cols"):
            self.dir_col[c_] = r[c_].to_numpy(dtype=object)
        self.dir_col["has_alert"] = r["has_alert"].to_numpy(dtype=bool)
        self.dir_col["direction_clear"] = np.array([x is True or (isinstance(x, (bool, np.bool_)) and bool(x))
                                                    for x in r["direction_clear"].tolist()], dtype=bool) \
            if "direction_clear" in r else np.zeros(len(r), dtype=bool)
        if len(r):
            sub = r[r["kind"].astype(str).str.startswith(("genotype", "null"))]
            for (grp, kind, grade, al), n in sub.groupby(["group", "kind", "grade", "has_alert"]).size().items():
                d = self.dir_by_group.setdefault(str(grp), {"kinds": {}, "grades": {}, "n": 0, "n_alert": 0})
                d["kinds"][kind] = d["kinds"].get(kind, 0) + int(n)
                d["grades"][grade] = d["grades"].get(grade, 0) + int(n)
                d["n"] += int(n)
                d["n_alert"] += int(n) if al else 0
        g = self.dv.groups
        if len(g):
            line_ix = {str(nm): i for i, nm in enumerate(self.R.cell)}
            with_sep = [(nm, i) for nm, i in line_ix.items() if ", " in nm]

            def lines_of(txt):
                txt = str(txt or "")
                out = {line_ix[x] for x in txt.split(", ") if x in line_ix}
                return out | {i for nm, i in with_sep if f", {nm}, " in f", {txt}, "}
            for rec in g[g["kind"].isin(["genotype", "null"])].to_dict("records"):
                for i in lines_of(rec.get("altered_lines")):
                    self.dir_line_groups.setdefault(i, []).append(rec)
                for i in lines_of(rec.get("intact_lines")):
                    self.dir_line_intact.setdefault((i, rec["kind"]), []).append(rec)
        log(f"  vault: direction arrows loaded ({len(r):,} arrows from {len(self.dv.edges):,} edges)")

    def _dir_rec(self, i):
        """Display row i of dv.rows (its position = its rank in ORDER) as a dict of the columns the notes read."""
        return {k: v[i] for k, v in self.dir_col.items()}

    def _dir_gene(self, col, name):
        """A gene of an arrow: its note's link (col: genes.csv), or its name as text (a drug target that is not a
        measured gene)."""
        col = int(col) if _finite(col) else -1
        return self.glink(col) if 0 <= col < self.R.gK else cell(name)

    def _dir_sources(self, r, skip=None):
        """Every source of a row, linked where it has a note (a collapsed row names them all); skip: a gene col shown
        as plain text (the note's own gene)."""
        srcs = list(r.get("sources") or ()) or [str(r.get("source", ""))]
        cols = list(r.get("source_cols") or ()) or [r.get("source_col", -1)]
        return ", ".join(cell(s_) if skip is not None and _finite(c_) and int(c_) == int(skip) else
                         self._dir_gene(c_, s_) for s_, c_ in zip(srcs, cols))

    def _dir_target(self, r):
        """The target of a row: a gene's link, 'cells under [[DRUG (drug)]] DOSE' for the sensitivity kinds, or 'the
        response to [[DRUG (drug)]] DOSE' for the selectivity kinds (target_type 'response')."""
        dd = int(r.get("target_dd", -1)) if _finite(r.get("target_dd")) else -1
        tt = str(r.get("target_type", ""))
        if tt == "cells":
            return f"cells under {self.ddlink(dd)}" if 0 <= dd < self.R.Dn else cell(r.get("target", ""))
        if tt == "response":
            return f"the response to {self.ddlink(dd)}" if 0 <= dd < self.R.Dn else cell(r.get("target", ""))
        return self._dir_gene(r.get("target_col", -1), r.get("target", ""))

    @staticmethod
    def _dir_false(r):
        """The 'false (group)' cell of a row: for a genotype kind the share of its group's arrows that may be false
        (false_share, with its 95% upper bound: '1% (up to 1%)'); for an expression-null kind the share of such arrows
        random genes give ('non-specific 19%'); '—' elsewhere."""
        f, u, ns = r.get("false_share"), r.get("false_share_upper"), r.get("nonspecific_share")
        if _finite(f):
            return fpct(f) + (f" (up to {fpct(u)})" if _finite(u) else "")
        if _finite(ns):
            return f"non-specific {fpct(ns)}"
        return "—"

    @staticmethod
    def _dir_effect(r):
        """The size of a row's effect in words, from its numbers (edges.parquet; the units differ by kind)."""
        kind = str(r.get("kind", ""))
        src = DV.source_text(r, 3)
        side = f"the lines without {src}" if kind.startswith("null") else f"the {src}-altered lines"
        ct = r.get("contrast")
        if kind in ("genotype_response", "null_response"):
            rf = r.get("retained_fraction")
            s = (f"{side} respond {float(rf):.2f}× as strongly" if _finite(rf) and float(rf) >= 0 else
                 f"{side} respond the other way" if _finite(rf) else "")
            s += (f" (z diff {flog(ct)})" if _finite(ct) else "")
            tops = [t for t in str(r.get("top_drugdoses", "") or "").split("; ") if t]
            rs = r.get("rise_share")
            if tops and _finite(rs) and DV.MIXED <= float(rs) <= 1.0 - DV.MIXED:
                return s + f"; rises at some drug-doses, falls at others ({float(rs):.0%} from rises): " + \
                    "; ".join(tops)
            return s + (f"; strongest at {tops[0]}" if tops else "")
        if kind in ("genotype_baseline", "null_baseline"):
            d = r.get("baseline_log2_diff")
            d = d if _finite(d) else ct
            if not _finite(d):
                return "—"
            return f"{2.0 ** abs(float(d)):.2f}× {'lower' if float(d) > 0 else 'higher'} at baseline in {side}"
        if kind in ("genotype_sensitivity", "null_sensitivity"):
            return f"{side}: {2.0 ** -float(ct):.2f}× the cells of the other lines" if _finite(ct) else "—"
        if kind == "level":
            rr = r.get("r_reverse")
            return (f"r {fcos(r.get('r'))}" + (f", reverse {fcos(rr)}" if _finite(rr) else "")
                    + ("; direction clear" if bool(r.get("direction_clear")) else "; direction not clear"))
        if kind == "level_sensitivity":
            return f"r {fcos(r.get('r'))}"
        if kind == "drug_target":
            bg = r.get("background_rate")
            return (f"{100 * float(ct):.0f}% of the class's compounds" if _finite(ct) else "—") + (
                f" vs {100 * float(bg):.1f}% of all compounds" if _finite(bg) else "")
        if kind in DV.SELECTIVITY:
            m = re.search(r"\((median [^)]*)\)", str(r.get("reading", "") or ""))
            return m.group(1) if m else "—"
        return "—"

    def _dir_words(self, i):
        """The texts of display row i that do not depend on the note (direction_view's wording); the short alerts
        are worded once per distinct alerts text (rows of one comparison share theirs)."""
        r = self._dir_rec(i)
        q = DV.q_text(r)
        al = str(r["alerts"])
        a = self._dir_memo.get(al)
        if a is None:
            a = self._dir_memo[al] = DV.alert_short(al) or "—"
        nt = str(r.get("notes", "") or "")
        n = self._dir_memo.get(("notes", nt))
        if n is None:
            n = self._dir_memo[("notes", nt)] = DV.notes_short(nt) or "—"
        sp = str(r.get("support", "") or "")
        su = self._dir_memo.get(("support", sp))
        if su is None:
            su = self._dir_memo[("support", sp)] = DV.support_short(sp) or "—"
        q = fq_text(q)
        return {"rec": r, "grade": str(r["grade"]), "sign": DV.sign_text(r), "kind": DV.kind_text(r),
                "effect": self._dir_effect(r), "q": q[2:] if q.startswith("q ") else q, "alerts": a, "notes": n,
                "support": su, "source": self._dir_sources(r), "target": self._dir_target(r),
                "false": self._dir_false(r)}

    def _dir_table(self, pos, first, skip=None, extra=None, first_head=None):
        """A table of arrows (display rows at positions pos, in ORDER). first: 'source' (the sources linked) or
        'target' (the target linked; a collapsed row's other sources linked in its direction text). extra:
        [(header, fn(row dict) -> text)] columns after the first."""
        extra = extra or []
        head = [first_head or ("Source" if first == "source" else "Target")] + [h for h, _ in extra] + [
            "Grade", "Direction (probable)", "Evidence", "Effect", "q", "false (group)", "Alerts", "Notes", "Support"]
        body = []
        for i in pos:
            w = self._dir_words(int(i))
            r = w["rec"]
            st = w["sign"]
            if first == "target" and int(r.get("n_sources", 1) or 1) > 1:
                st = st.replace(DV.source_text(r), self._dir_sources(r, skip), 1)
            body.append([w[first]] + [fn(r) for _, fn in extra]
                        + [w["grade"], st, w["kind"], w["effect"], w["q"], w["false"], w["alerts"], w["notes"],
                           w["support"]])
        return table(head, body)

    def _dir_list(self, pos, n, what="arrows", url=None):
        """(shown positions, the counts sentence) of a list capped by the cap rule (cap_keep, as DV.cap: the n
        strongest, and any of the n strongest without an alert beyond them; DV.counts_text and DV.more_text: how
        many there are, how many carry an alert or notes, how many more, how many of them with an alert), then 'k of
        N shown' with the explorer address of the complete list (url) and the caveats every arrow of a kind in the
        list carries (DV.caveat_header: stated once here, not on every row)."""
        al = self.dir_col["has_alert"][pos]
        keep = cap_keep(al, n)
        n_more = len(pos) - len(keep)
        n_more_al = int(al.sum()) - int(al[keep].sum())
        gr = self.dir_col["grade"][pos]
        nn = np.nan_to_num(self.dir_col["n_notes"][pos], nan=0.0)
        kinds = tuple(sorted(set(self.dir_col["kind"][pos].tolist())))
        key = (len(pos), int(al.sum()), int((nn > 0).sum()), what, kinds) + tuple(int((gr == g_).sum())
                                                                               for g_ in DV.GRADES)
        s = self._dir_cnt_memo.get(key)
        if s is None:
            s = self._dir_cnt_memo[key] = DV.counts_text(pd.DataFrame({"has_alert": al, "grade": gr, "n_notes": nn,
                                                                       "kind": self.dir_col["kind"][pos]}), what)
        if n_more:
            extra = len(keep) - min(n, len(pos))
            s += (f". Shown: the {min(n, len(pos)):,} strongest" + (
                f" and the {extra:,} next strongest without an alert" if extra else "")
                  + f"; {DV.more_text(n_more, n_more_al, what)} not shown")
        s += "."
        if url:
            s += " " + self.kofn(len(keep), len(pos), url, what) + (". There every alert, note and support reason "
                                                                    "is in full.")
        cav = DV.caveat_header(pd.DataFrame({"kind": self.dir_col["kind"][pos],
                                             "caveats": self.dir_col["caveats"][pos]}))   # each family's own
        if cav:
            s += " " + cav
        s += (f" Alerts ({ALERT}): reasons for doubt, as short labels; notes: reasons kept below their thresholds, "
              "and context; support: evidence for the arrow (for example the compounds that agree). false (group): "
              "the share of the arrows of its comparison group that may be false (with the 95% upper bound), from "
              "random comparison groups; non-specific: the share random genes would give.")
        return pos[keep], s

    def _dir_gene_rows(self, c):
        """(upstream positions, downstream positions: gene targets and cells together), in ORDER, of gene c."""
        p = self.dir_pos
        up = p["up"].get(int(c), _NO_ROWS)
        dn, ce = p["down"].get(int(c), _NO_ROWS), p["cells"].get(int(c), _NO_ROWS)
        return up, (np.union1d(dn, ce) if len(dn) and len(ce) else (dn if len(dn) else ce))

    def _dir_intro(self):
        return (f"*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < "
                "0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) "
                "of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that "
                f"target a gene, or a gene's natural level. A {DV.CAVEAT_SHORT}. Grades: "
                + ", ".join(DV.grade_legend("short")) + f"; {ALERT} = a reason for doubt, shown in place. How to "
                f"read them, and this run's controls: [[{self.fixed[DIR_NOTE]}]].*")

    def dir_glance(self, c, up, dn):
        """The At-a-glance sentence of a gene with arrows ('' without)."""
        if self.dv is None or not (len(up) or len(dn)):
            return ""
        parts = []
        if len(up):
            w = self._dir_words(int(up[0]))
            parts.append(f"{len(up):,} arrow{'s point' if len(up) != 1 else ' points'} to it, the strongest "
                         f"{w['source']} → it (grade {w['grade']}" + (f" {ALERT}" if w["rec"]["has_alert"] else "")
                         + ")")
        else:
            parts.append("none points to it")
        if len(dn):
            w = self._dir_words(int(dn[0]))
            parts.append(f"{len(dn):,} go{'es' if len(dn) == 1 else ''} from it, the strongest it → "
                         f"{w['target']} (grade {w['grade']}" + (f" {ALERT}" if w["rec"]["has_alert"] else "") + ")")
        else:
            parts.append("none goes from it")
        return (f"Probable direction (from the cell lines, not proof of direct regulation): {parts[0]}; {parts[1]}. "
                "See Direction (probable) below.")

    def gene_tests_text(self, c):
        """'Tested in 4,850 comparisons (mutation: response 2,376, ...)' from direction/gene_tests.parquet: every test
        the gene took part in, as the source or the target, by kind; with ': no arrow passed.' or '; N arrows passed
        (q < 0.10).' ('' on an older direction stage)."""
        rows = self.gene_tests.get(int(c))
        if not rows:
            return ""
        by, n_e = {}, 0
        for kind, _role, n_t, e_ in rows:
            by[kind] = by.get(kind, 0) + n_t
            n_e += e_
        n = sum(by.values())
        parts = ", ".join(f"{DV.KIND_SHORT.get(k, k)}: {by[k]:,}" for k in DV.KINDS if by.get(k)) or \
            ", ".join(f"{k}: {v:,}" for k, v in by.items())
        head = f"Tested in {n:,} comparison{'s' if n != 1 else ''} ({parts}"
        if not n_e:
            return head + "): no arrow passed."
        return head + f"); {n_e:,} arrow{'s' if n_e != 1 else ''} passed (q < 0.10 in its family of tests)."

    def sec_direction(self, c, up, dn):
        """The gene note's 'Direction (probable)': the arrows whose target is this gene (upstream) and those whose
        source it is (downstream: genes, and the cells under drug-doses), capped by the cap rule, with counts; and how
        often the gene was tested (gene_tests_text)."""
        L = ["## Direction (probable)", ""]
        if self.dv is None:
            return L + [DIR_NOT_RUN, ""]
        tested = self.gene_tests_text(c)
        if not len(up) and not len(dn):
            return L + ([tested, ""] if tested else []) + [
                f"No arrow points to or from this gene in this run (how the arrows are made: "
                f"[[{self.fixed[DIR_NOTE]}]]).", ""]
        L += [self._dir_intro(), ""] + ([tested, ""] if tested else [])
        for head, pos, first, none in (
                ("Upstream of this gene", up, "source", "None: no arrow points to this gene."),
                ("Downstream of this gene", dn, "target",
                 "None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).")):
            L += [f"### {head}", ""]
            if not len(pos):
                L += [none, ""]
                continue
            shown, cnt = self._dir_list(pos, N_DIRECTION, url=self.xgene(c, "direction"))
            L += [f"*{cnt}*", ""] + self._dir_table(shown, first, skip=c) + [""]
        return L

    # ---- drug notes
    def sec_direction_drug(self, d, rows):
        """A drug note's 'Direction (probable)': the genes that set how the cells fare under this drug (sensitivity
        arrows at its doses: dv.for_drugdose) and the drug-target arrows in which it is one of the compounds
        (dv.drug_targets: by name or salt base)."""
        L = ["## Direction (probable)", ""]
        if self.dv is None:
            return L + [DIR_NOT_RUN, ""]
        dv = self.dv
        cells = np.unique(np.concatenate([_NO_ROWS] + [dv.for_drugdose(i)["order"].to_numpy(dtype=np.int64)
                                                       for i in rows]))
        tg = np.unique(dv.drug_targets(d)["order"].to_numpy(dtype=np.int64))
        if not len(cells) and not len(tg):
            return L + ["No arrow involves this drug in this run: no gene was found to set how the cells fare under "
                        "it, and it is not one of the compounds of a drug-target arrow (how the arrows are made: "
                        f"[[{self.fixed[DIR_NOTE]}]]).", ""]
        L += [self._dir_intro(), ""]
        L += ["### Genes that set how the cells fare under it, or how strongly its lines respond", ""]
        if len(cells):
            shown, cnt = self._dir_list(cells, N_DIR_DRUG, url=self.xdrug(d, "direction"))
            L += ["*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the "
                  "other lines in the same wells), and gene → the response to one of its doses (how many genes a "
                  f"line moves, against the other lines: line selectivity). {cnt}*", ""]
            L += self._dir_table(shown, "source", extra=[("Dose", lambda r: fdose(r.get("target_dose")) or "—")],
                                 first_head="Gene") + [""]
        else:
            L += ["None: no gene was found to set how the cells fare under it.", ""]
        L += ["### Its targets: what acting on them probably does", ""]
        if len(tg):
            keys = {d.lower(), str(T.salt_base(d)).lower()}

            def mine(r):
                sup = [y for x in str(r.get("compounds_supporting", "") or "").split("; ") for y in x.split(" / ")
                       if y]
                ok = any(k in keys for x in sup for k in (x.lower(), str(T.salt_base(x)).lower()))
                return "moves it that way too" if ok else "does not move it that way (the class's other compounds do)"
            shown, cnt = self._dir_list(tg, N_DIR_DRUG, url=self.xdrug(d, "direction"))
            L += [f"*Drug-target arrows of the compound classes it belongs to (compounds sharing a listed target and "
                  f"mechanism; one molecule counts once, under all its names): the target → a gene whose level those "
                  f"compounds move. A row that names several targets is one test: the compounds share them all, and "
                  f"any of them could be the cause. {cnt}*", ""]
            L += self._dir_table(shown, "source", extra=[("Gene it moves", self._dir_target), ("This drug", mine)],
                                 first_head="Its target") + [""]
        else:
            L += ["None: it is not one of the compounds of a drug-target arrow.", ""]
        return L

    # ---- cell-line notes
    def _dir_group_rank(self, recs):
        """Groups ranked: those with more arrows first, then by their best grade, then by name."""
        def key(rec):
            d = self.dir_by_group.get(str(rec.get("description", "")), {})
            best = min((DV.GRADES.index(g_) for g_ in d.get("grades", {}) if g_ in DV.GRADES), default=9)
            return (-d.get("n", 0), best, str(rec.get("gene", "")).lower(), str(rec.get("description", "")))
        return sorted(recs, key=key)

    def _dir_group_cells(self, rec):
        """(arrows by kind 'response / level / cells', grades) of a comparison group, from its display rows."""
        d = self.dir_by_group.get(str(rec.get("description", "")), {})
        k = d.get("kinds", {})
        pre = "genotype" if rec.get("kind") == "genotype" else "null"
        arrows = " / ".join(str(k.get(f"{pre}_{x}", 0)) for x in ("response", "baseline", "sensitivity",
                                                                  "selectivity"))
        gr = d.get("grades", {})
        grades = ", ".join(f"{g_} {gr[g_]}" for g_ in DV.GRADES if gr.get(g_)) or "—"
        return arrows, grades + (f"; {d['n_alert']:,} with an alert {ALERT}" if d.get("n_alert") else "")

    def _dir_group_genes(self, rec):
        """The genes of an expression-null line set (every gene absent from exactly these lines), linked."""
        names = [x for x in str(rec.get("genes_same_lines", "") or "").split(", ") if x] or [str(rec.get("gene", ""))]
        out = []
        for k_, nm in enumerate(names[:N_DIR_NAMES]):
            col = int(rec.get("gene_col", -1)) if k_ == 0 and nm == str(rec.get("gene", "")) else -1
            if col < 0:
                n_ = self.sym_note.get(nm)
                out.append(f"[[{n_}]]" if n_ else cell(nm))
            else:
                out.append(self._dir_gene(col, nm))
        more = ""
        if len(names) > N_DIR_NAMES:
            gid = sval(rec.get("group_id")) or sval(rec.get("description"))
            more = " " + self.kofn(N_DIR_NAMES, len(names), self.xu(LK.group, gid), "genes")
        return ", ".join(out) + more

    @staticmethod
    def _dir_hidden(al, keep, what):
        """'; 3 more groups (2 of them with an alert ⚠) not shown' for a capped list (al: every item's alert flag,
        keep: the shown positions); '' when nothing is left out."""
        n_more = len(al) - len(keep)
        if n_more <= 0:
            return ""
        return f"; {DV.more_text(n_more, int(al.sum()) - int(al[keep].sum()), what)} not shown"

    def sec_direction_line(self, line):
        """A cell-line note's 'Direction (probable)': its recorded driver alterations as the direction stage
        grouped them (loss / gain of function / any record), and the genes it does not express that served as
        natural knockouts, each with what came out of it."""
        L = ["## Direction (probable)", ""]
        if self.dv is None:
            return L + [DIR_NOT_RUN, ""]
        recs = self.dir_line_groups.get(line, [])
        geno = self._dir_group_rank([x for x in recs if x.get("kind") == "genotype"])
        null = self._dir_group_rank([x for x in recs if x.get("kind") == "null"])
        L += [self._dir_intro(), ""]
        n_other = len(self.dir_line_intact.get((line, "genotype"), []))
        L += ["### Its recorded alterations", ""]
        if geno:
            al = np.array([bool(str(x.get("alerts", "") or "")) for x in geno], dtype=bool)
            keep = cap_keep(al, N_DIR_LINE)
            cnt = shown_text(len(geno), int(al.sum()), len(keep), N_DIR_LINE, max(0, len(keep) - N_DIR_LINE))
            cnt += self._dir_hidden(al, keep, "groups")
            cnt += " " + self.kofn(len(keep), len(geno), self.xline(line), "groups")
            L += [f"*The comparison groups that count this line as altered (Tahoe's cell-line genetics; "
                  f"`direction/groups.parquet`): {cnt}. "
                  "Each group is its gene's recorded loss of function, gain of function, or any record (some records "
                  "carry no mechanism), against the lines with no record of the gene. Arrows = the arrows that "
                  f"came out of the group, by target: a gene's drug response / its level / the cells under a "
                  f"drug-dose. In {n_other:,} other groups this line is on the 'not recorded' side.*", ""]
            body = []
            for k_ in keep:
                x = geno[k_]
                arrows, grades = self._dir_group_cells(x)
                body.append([self._dir_gene(x.get("gene_col", -1), x.get("gene", "")), cell(x.get("description", "")),
                             arrows, grades, DV.alert_short(str(x.get("alerts", "") or "")) or "—",
                             DV.notes_short(str(x.get("notes", "") or "")) or "—"])
            L += table(["Gene", "Group", "Arrows (response / level / cells / selectivity)", "Grades", "Alerts",
                        "Notes"],
                       body) + [""]
        else:
            L += [f"None: no recorded alteration of this line forms a group (a group needs at least 3 altered lines "
                  f"and 3 without a record). In {n_other:,} groups it is on the 'not recorded' side.", ""]
        L += ["### Genes it does not express (natural knockouts)", ""]
        if null:
            al = np.array([bool(str(x.get("alerts", "") or "")) for x in null], dtype=bool)
            keep = cap_keep(al, N_DIR_LINE)
            n_genes = sum(max(1, len([y for y in str(x.get("genes_same_lines", "") or "").split(", ") if y]))
                          for x in null)
            n_with = sum(1 for x in null if self.dir_by_group.get(str(x.get("description", "")), {}).get("n"))
            cnt = shown_text(len(null), int(al.sum()), len(keep), N_DIR_LINE, max(0, len(keep) - N_DIR_LINE))
            cnt += self._dir_hidden(al, keep, "line sets")
            cnt += " " + self.kofn(len(keep), len(null), self.xline(line), "line sets")
            L += [f"*Genes this line does not express (it reads only the ambient RNA of the well) while at least 3 "
                  f"other lines do: the stage compared the lines lacking each gene with the lines expressing it "
                  f"(genes absent from exactly the same lines share one test). Line sets that include this line: "
                  f"{cnt}; "
                  f"{n_genes:,} genes; {n_with:,} of the sets gave arrows. Ranked by the number of arrows.*", ""]
            body = []
            for k_ in keep:
                x = null[k_]
                arrows, grades = self._dir_group_cells(x)
                how = "within organs" if bool(x.get("stratified")) else "across organs"
                note = sval(x.get("note"))
                body.append([self._dir_group_genes(x), f"{fint(x.get('n_altered'))} vs {fint(x.get('n_intact'))}",
                             arrows, grades, how + (f"; {note}" if note else ""),
                             DV.alert_short(str(x.get("alerts", "") or "")) or "—",
                             DV.notes_short(str(x.get("notes", "") or "")) or "—"])
            L += table(["Gene(s)", "Lines without vs expressing", "Arrows (response / level / cells / selectivity)",
                        "Grades",
                        "Compared", "Alerts", "Notes"], body) + [""]
        else:
            L += ["None: no gene that this line lacks was tested as a natural knockout (a gene needs at least 3 lines "
                  "without it and 3 expressing it).", ""]
        return L

    # ---- the concept note
    @staticmethod
    def _dir_label_family(label):
        """An alert's short label with its numbers and gene names left out, to count the labels of a run."""
        f = re.sub(r"\d+", "N", label)
        f = re.sub(r"^co-occurs with .+", "co-occurs with (another gene's altered lines)", f)
        f = re.sub(r"^mostly lines without an? .+ alteration$", "mostly lines without (another gene's) alteration", f)
        f = re.sub(r"^.+ alterations on the other side$", "(another gene's) alterations on the other side", f)
        f = re.sub(r"^also absent: .+", "also absent: (other genes absent from most of these lines)", f)
        return re.sub(r"^\S+ not expressed in N of the N altered lines$",
                      "(the source) not expressed in N of the N altered lines", f)

    @staticmethod
    def _dir_num(x):
        """A control's count or rate: three significant digits, no trailing zeros ('—' when missing)."""
        return f"{float(x):.3g}" if _finite(x) else "—"

    def _dir_positive(self, k, v):
        """One positive control of controls.json as a list item; every arrow it names marked ALERT when it carries an
        alert (rule 1: the doubt is shown in place)."""
        marks = self.dv.control_alerts(k, v) if self.dv is not None else {}

        def mk(nm):
            return f" {ALERT}" if marks.get(str(nm)) else ""
        k = k.replace(" -> ", " → ")
        if "per_gene" in v:
            want = -1 if str(v.get("expected", "")).startswith("sign -1") else 1
            per = sorted(v["per_gene"], key=lambda x: (x.get("rank") if _finite(x.get("rank")) else 10 ** 9))
            if any("counted" in x for x in per):       # direction version 5: the stricter counting, with why_not
                rec = [x for x in per if x.get("counted")]
                miss = [x for x in per if not x.get("counted")]
            else:
                rec = [x for x in per if x.get("edge") and x.get("sign") == want]
                miss = [x for x in per if not (x.get("edge") and x.get("sign") == want)]

            def gl(nm):
                n_ = self.sym_note.get(str(nm))
                return f"[[{n_}]]" if n_ else cell(nm)
            found = ", ".join(f"{gl(x['gene'])} (rank {fint(x.get('rank'))}, grade {x.get('grade') or '—'}"
                              f"{mk(x['gene'])})" for x in rec) or "none"
            rest = "; ".join(f"{gl(x['gene'])} (rank {fint(x.get('rank'))}"
                             + (f": {cell(x.get('why_not'))}" if sval(x.get("why_not")) else "") + ")" for x in miss)
            return (f"- {k}: {fint(v.get('recovered_right_sign'))} of the {fint(v.get('targets_present'))} target "
                    f"genes present come back as arrows with the expected sign ({cell(v.get('expected', ''))}), "
                    f"{fint(v.get('wrong_sign'))} with the other sign; their median rank among the "
                    f"{fint(v.get('genes_ranked'))} genes tested: {self._dir_num(v.get('median_rank'))}. Counted "
                    f"(rank, grade; {ALERT} = the arrow carries an alert): "
                    f"{found}. Not counted ({len(miss)}; rank, and why not): {rest or 'none'}.")
        if "drugdoses_tested" in v:
            return (f"- {k}: {fint(v.get('edges'))} arrows among the {fint(v.get('drugdoses_tested'))} drug-doses "
                    f"tested, {fint(v.get('right_sign'))} with the expected sign ({cell(v.get('expected', ''))})"
                    + (": " + ", ".join(cell(x) + mk(x) for x in v.get("drugdoses") or []) if v.get("drugdoses")
                       else "") + ".")
        if v.get("assessable") is False:
            return f"- {k}: not assessable here ({cell(v.get('why', ''))})."
        return (f"- {k}: {fint(v.get('recovered_right_sign'))} of {fint(v.get('targets_present'))} come back with "
                f"the expected sign, {fint(v.get('wrong_sign'))} with the other sign"
                + (": " + ", ".join(cell(x) + mk(x) for x in v.get("genes") or []) if v.get("genes") else "")
                + ".")

    def direction_note(self):
        """Concepts/Probable direction.md (generated): what the arrows are (kinds, grades, sign, alerts), this run's
        counts, its controls (direction/controls.json: the positive controls; per kind the arrows written against
        the false arrows the negative controls expect) and what an arrow does not say. Linked from Home and from
        every direction section; rebuilt on every run."""
        dv = self.dv
        fm = {"type": "concept", "tags": ["concept", "direction"], "source": "direction/ (tahoemap/direction.py)"}
        L = [frontmatter(fm), f"# {DIR_NOTE}", "",
             "Which gene probably acts on which. The partners of a gene note move with it, but a correlation has no "
             "direction: CDKN1A and MDM2 rise together, and the cosine does not say that both follow TP53. The "
             "**direction** stage (`direction/`; the method is tahoemap/direction.py, explained in "
             "`docs/direction.md` of the tahoemap repository) adds arrows **SOURCE → TARGET**, computed by code "
             "from this run's own tables. Every arrow comes from a statistical test, with a p-value and a "
             "Benjamini-Hochberg q (q < 0.10 in its family of tests: a pair without such a result has no arrow), "
             "and carries a grade and its alerts.", "", f"> [!warning] {DV.CAVEAT}", "",
             "## Where the arrows are", "",
             "- A gene note's **Direction (probable)** section: *upstream of this gene* (the arrows whose target it "
             "is) and *downstream of this gene* (the arrows whose source it is: to other genes, and to the cells "
             "under a drug-dose); a sentence in its At a glance when it has arrows.",
             "- A drug note: the genes that set how the cells fare under the drug, and the drug-target arrows of the "
             "compound classes it belongs to.",
             "- A cell-line note: its recorded alterations as the comparison groups the stage formed, and the genes "
             "it does not express that served as natural knockouts, each with the arrows that came out of it.",
             "- Every list is in one order: grade A, B, C, then q (smallest first), then the size of the effect. A "
             f"list capped at N shows the N strongest and any of the N strongest without an alert ({ALERT}) beyond "
             "them, and says how many more there are and how many of those carry an alert. Nothing is left out "
             "for a reason to doubt it.",
             "- An arrow is one test. Where one test stands for several sources (compounds that share several "
             "listed targets; genes absent from exactly the same lines) the arrow names them all, and any of them "
             "could be the cause.", ""]
        cnt = dv.counts() if dv is not None else None
        L += ["## The kinds of evidence", ""]
        body = []
        for k in DV.KINDS:
            row = [f"`{k}`", DV.KIND_SHORT[k], DV.KIND_WORDS[k]]
            if cnt is not None:
                bk = cnt["by_kind"].get(k, {})
                row.append(" / ".join(str(bk.get(g_, 0)) for g_ in DV.GRADES))
            body.append(row)
        L += table(["Kind", "Short", "The source, and what it is set against"]
                   + (["Arrows A / B / C (this run)"] if cnt is not None else []), body) + [""]
        L += ["## Grades", ""] + [f"- **{x[0]}**{x[1:]}" for x in DV.grade_legend("long")] + [""]
        L += ["## The sign: what the source's activity does", "",
              "Every arrow says what the source's **activity** does to the target. For a level (the target's baseline "
              "level, or its level under the compounds that target the source) and for the cells' numbers: *raises* "
              "or *lowers*. For a drug response: *strengthens* or *weakens* - how strongly the target responds, in "
              "its own direction at each drug-dose. Where the target falls under the drugs, *strengthens* means it "
              "falls further (the source deepens the fall, i.e. represses it there), and *weakens* means it falls "
              "less; where it rises, *strengthens* means it rises more. Read which from all the drug-doses an arrow "
              "lists (e.g. 0.49x vs 0.80x: a fall), not the first alone: a target can rise under some drugs and "
              "fall under others, and such an arrow is alerted *rises at some drug-doses, falls at others* - its "
              "sign then says how strongly the target responds, not whether the source induces or represses it. "
              "*Not inferred*: the mechanism of the alteration is not recorded.", "",
              "For a loss-of-function mutation, the source's activity raises (strengthens) the target when the "
              "target is higher (responds more strongly) where the source is intact; for a gain of function it is "
              "the reverse. For a gene that some lines do not express, the same with the lines that express it. For "
              "compounds that target the source: an inhibitor that raises the target means the source's activity "
              "lowers it. For the cells: *raises the cells' numbers* = the source protects the cells under that "
              "drug-dose; *lowers* = it makes them more sensitive. For a natural level: the lines with more of the "
              "source respond more strongly (strengthens) or less (weakens), or have more (raises) or fewer "
              "(lowers) cells.", ""]
        L += ["## Alerts, notes, caveats and support", "",
              f"An arrow with a reason for doubt keeps its place, marked {ALERT} with the reason (an alert); the "
              "doubts lower its grade where the grade rules say so. Notes are reasons kept below their thresholds, "
              "and context: they are shown with the arrow but are not a doubt by themselves. Caveats are what every "
              "arrow of a kind carries; each list states them once above it. Support is evidence for the arrow (for "
              "example the compounds that agree). The tables show each reason by a short label; every reason in "
              "full is in `direction/edges.parquet` (columns alerts, notes, caveats and support; alerts_all holds "
              "every reason in the stage's order) and in the explorer.", ""]
        if dv is not None and len(dv.rows):
            tiers = (("alerts", f"alert ({ALERT})", DV.alert_reasons), ("notes", "note", DV.note_reasons),
                     ("support", "support", DV.support_reasons))
            for col, what, reasons_of in tiers:
                if col not in dv.rows:
                    continue
                fam, ex, cache = {}, {}, {}
                for txt in dv.rows[col].fillna("").astype(str):
                    seen = set()
                    for rsn in reasons_of(txt):
                        f_ = cache.get(rsn)
                        if f_ is None:
                            f_ = cache[rsn] = self._dir_label_family(DV._labels([rsn]))
                        if f_ in seen:
                            continue
                        seen.add(f_)
                        fam[f_] = fam.get(f_, 0) + 1
                        ex.setdefault(f_, rsn)
                if fam:
                    L += [f"The {what} labels in this run, with the number of arrows that carry each, and one reason "
                          "in full (from the strongest arrow that carries it):", ""]
                    L += table(["Label", "Arrows", "In full (an example)"],
                               [[f_, f"{n_:,}", clip_text(ex[f_], 400)] for f_, n_ in
                                sorted(fam.items(), key=lambda t: (-t[1], t[0]))]) + [""]
        L += ["## This run, and how much to trust it", ""]
        if dv is None:
            L += [DIR_NOT_RUN, ""]
        else:
            ctl = dv.controls or {}
            L += [f"{cnt['rows']:,} arrows ({cnt['edges']:,} edges of `direction/edges.parquet`: an arrow that names "
                  f"several sources stands for one edge per source), {cnt['with_alert']:,} of them with an alert "
                  f"{ALERT}; grade " + ", ".join(
                      f"{g_} {sum(v.get(g_, 0) for v in cnt['by_kind'].values()):,}" for g_ in DV.GRADES) + ".", ""]
            pos = ctl.get("positive") or {}
            if pos:
                L += ["**Positive controls** (known biology that has to come back):", ""]
                L += [self._dir_positive(k, v) for k, v in pos.items()] + [""]
            exp = ctl.get("expected_false_edges") or {}
            if exp:
                L += ["**Arrows against the false arrows the controls expect.** Random pseudo-genotype groups (line "
                      "sets drawn at random, tested exactly like the recorded groups and counted at the real table's "
                      "cut) give the false arrows a group without any real effect adds; for the natural levels, the "
                      "same tests with every gene's level shuffled over its lines.", ""]
                body = []
                for key, x in exp.items():
                    kind, part = key, "over the whole table"
                    for suf, what in (("_within_group_only", "significant only within its group (grade C: leads)"),
                                      ("_within_drugdose_only",
                                       "significant only within its drug-dose (grade C: leads)")):
                        if key.endswith(suf):
                            kind, part = key[:-len(suf)], what
                    n_, f_, u_ = x.get("edges"), x.get("expected_false"), x.get("expected_false_upper")
                    nonspec = not _finite(f_) and _finite(x.get("expected_nonspecific"))
                    if nonspec:                         # natural knockouts: arrows random genes would give as often
                        f_ = x.get("expected_nonspecific")
                    bad = _finite(f_) and _finite(n_) and n_ and float(f_) >= 0.5 * float(n_)
                    body.append([DV.KIND_SHORT.get(kind, kind), part, fint(n_),
                                 self._dir_num(f_) + (f" (up to {self._dir_num(u_)})" if _finite(u_) else "")
                                 + (" non-specific (random genes give them as often)" if nonspec else ""),
                                 f"{ALERT} about half or more may be false: read them as leads" if bad else ""])
                L += table(["Evidence", "Which arrows", "Written", "Expected false", ""], body) + [""]
                L += [DV.CONTROLS_CAVEAT, ""]
                L += ["The drug-target arrows have no random control: each arrow's alerts say what to doubt.", ""]
            nc = ctl.get("null_controls") or {}
            if nc:
                L += ["**Random controls for the natural knockouts.** The same tests with random genes that are not "
                      "partners (for the levels and drug responses), and with random line sets of the real sets' sizes "
                      "(for the cells and the line selectivity):", ""]
                bins = nc.get("bins") or []
                for k_, rates in (nc.get("rates") or {}).items():
                    hits = (nc.get("hits") or {}).get(k_) or []
                    tests = (nc.get("tests") or {}).get(k_) or []
                    per_bin = ", ".join(f"{b} other line sets: {self._dir_num(r_)}" for b, r_ in zip(bins, rates))
                    L.append(f"- {DV.KIND_SHORT.get(k_, k_)}: random genes reached the cut in "
                             f"{fint(sum(int(h) for h in hits))} of {fint(sum(int(t) for t in tests))} tests; the rate "
                             f"per test by how many other line sets overlap the set ({per_bin}).")
                for k_, v_ in (nc.get("line_sets") or {}).items():
                    L.append(f"- {DV.KIND_SHORT.get(k_, k_)}: {fint(v_.get('pseudo_sets'))} random line sets gave "
                             f"{fint(v_.get('arrows'))} arrows ({self._dir_num(v_.get('rate_per_set'))} per set, up "
                             f"to {self._dir_num(v_.get('upper_per_set'))}); over the "
                             f"{fint(v_.get('real_sets_tested'))} real line sets about "
                             f"{self._dir_num(v_.get('expected_false'))} (up to "
                             f"{self._dir_num(v_.get('expected_false_upper'))}) of the arrows may be false.")
                if sval(nc.get("how")):
                    L.append(f"- How: {cell(nc.get('how'))}")
                L.append("")
            neg = (ctl.get("negative") or {}).get("summary") or {}
            if neg:
                L += [f"**Random pseudo-groups** ({fint((dv.info.get('groups_tested') or {}).get('pseudo_controls'))} "
                      "groups): arrows per group, random vs recorded groups:", ""]
                for k, v in neg.items():
                    L.append(f"- {k}: over the whole table {self._dir_num(v.get('pseudo_edges_mean_per_group'))} vs "
                             f"{self._dir_num(v.get('real_edges_mean_per_group'))}; within the group only "
                             f"{self._dir_num(v.get('pseudo_within_group_edges_mean_per_group'))} vs "
                             f"{self._dir_num(v.get('real_within_group_edges_mean_per_group'))}"
                             + (f" {ALERT} the random groups do as well as the recorded ones"
                                if v.get("pseudo_at_or_above_real") else "") + ".")
                L.append("")
            lv = ctl.get("level_controls") or {}
            if lv:
                L += ["**Natural levels, shuffled** (every gene's level permuted over its lines, the same tests):", ""]
                for k, v in lv.items():
                    L.append(f"- {DV.KIND_SHORT.get(k, k)}: {fint(v.get('tests'))} tests, {fint(v.get('edges'))} "
                             f"arrows; with the levels shuffled {fint(v.get('control_permuted_levels_edges'))}"
                             + (f" (and {fint(v.get('control_permuted_levels_within_drugdose_only'))} within a "
                                f"drug-dose only, against {fint(v.get('edges_within_drugdose_only'))})"
                                if "control_permuted_levels_within_drugdose_only" in v else "") + ".")
                L.append("")
        L += ["## What an arrow does not say", ""] + [f"- {x}" for x in DV.caveat_lines()] + [""]
        L += ["## Files", "",
              "- `direction/edges.parquet`: one row per edge (its README.md lists every column); "
              "`direction/groups.parquet`: the comparison groups (recorded alterations, natural knockouts, random "
              "pseudo-groups); `direction/controls.json`; `direction/info.json`.",
              f"- Generated by `tahoe vault` (v{VERSION}) from `direction/`; rebuilt on every run: do not edit it.", ""]
        self.W.write(f"Concepts/{self.fixed[DIR_NOTE]}.md", "\n".join(L))

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
        if R.flagged_only[c]:
            L.append(f"- {ALERT} **In the space only through flagged drug-doses**: its significant pooled drug-doses "
                     "and per-line responses all carry an alert (`embed/genes.parquet` evidence_flagged_only), so its "
                     "module and partners may reflect what those drug-doses did to the cells.")
        L.append(f"- **Nodal map** (x, y) = ({R.xy[c, 0]:.1f}, {R.xy[c, 1]:.1f}); signed map ({R.xys[c, 0]:.1f}, "
                 f"{R.xys[c, 1]:.1f}). **Vector** length {g3(R.vnorm[c])}, {g3(100 * R.vrep[c])}% of its response "
                 f"variance represented; |z| ≥ 3 in {fint(R.n_resp[c])} contexts (`embed/genes.parquet`).")
        nm = R.novel_by_col.get(c)
        if nm:
            L.append("- **Candidate new member** (not annotated, but close to the annotated members of its arm; "
                     "`validation/novel_members.csv`): " + "; ".join(
                         f"*{cell(r.set_label)}* ({r.source}, mean cos {fcos(r.mean_cos)} to "
                         f"{int(r.n_annotated_in_arm)})" for r in nm[:3]) + "."
                     + (" " + self.kofn(3, len(nm), self.xgene(c, "partners"), "sets") if len(nm) > 3 else ""))
        L.append("")
        if hasattr(R, "pred_up") and R.pred_up[c, 0] >= 0:
            L += ["**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall "
                  "(gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): "
                  f"the {N_PRED} strongest predictions over all drug-doses and the {N_PRED} strongest of those "
                  f"without an artifact flag, together. {ALERT} = an artifact flag on the drug-dose (or on this gene, "
                  "where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose "
                  "did to the cells. A caveat is no artifact flag (e.g. a neighbouring well at the drug's top dose): "
                  "it is shown in the same column.", ""]
            body = []
            drows = np.arange(R.de_s[c], R.de_s[c + 1])
            for d, sgn, idx, pz, idc, pzc in (("rise", 1, R.pred_up[c], R.pred_up_z[c], R.pred_up_c[c],
                                               R.pred_up_cz[c]),
                                              ("fall", -1, R.pred_dn[c], R.pred_dn_z[c], R.pred_dn_c[c],
                                               R.pred_dn_cz[c])):
                cand = {}
                for dd, v in list(zip(idx, pz)) + list(zip(idc, pzc)):
                    if dd >= 0 and _finite(v):
                        cand[int(dd)] = float(v)
                for j, dd in enumerate(sorted(cand, key=lambda k: (-sgn * cand[k], k))):
                    obs = float(R.DD_z[dd, c])
                    body.append([d if j == 0 else "", self.ddlink(dd),
                                 value_marks(*self.gene_dd_flags(c, dd, drows)), fz(cand[dd]), fz(obs)])
            L += table(["", "Drug-dose", "Alert / caveat", "Predicted z", "Observed z"], body) + [""]
            L += [self.kofn(len(body), R.Dn, self.xgene(c, "drugs"), "drug-doses") + " The explorer gives the "
                  "predicted and the observed z at every drug-dose.", ""]
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
        if al or pv:                                   # every alias and previous symbol
            rows.append(["Also known as", ", ".join(al) + (f"; previously {', '.join(pv)}" if pv else "")])
        gg = [x for x in sval(an["gene_groups"]).split("|") if x]
        if gg:
            rows.append(["Gene groups (HGNC)", "; ".join(gg)])
        hm = R.hallmark[c]
        if hm:
            rows.append(["Hallmark sets", ", ".join(h.replace("HALLMARK_", "") for h in hm)])
        rc = R.reactome[c]
        if rc:
            rows.append(["Reactome", f"{len(rc)} pathways, smallest: " + "; ".join(rc[:3])
                         + (" " + self.kofn(min(3, len(rc)), len(rc), self.xgene(c, "annotation"), "pathways named")
                            if len(rc) > 3 else "")])
        mb = sval(an["matched_by"])
        if mb:
            rows.append(["Matched by", mb + (" (alias only: tentative)" if mb == "alias_symbol" else "")])
        L += table(["", ""], rows) + [""]
        up = sval(an["uniprot"]).split("|")[0]
        fn = sval(an["function"])
        pn = sval(an.get("protein_name"))
        if fn:
            L += [f"**Function**, from UniProt [{up}](https://www.uniprot.org/uniprotkb/{up})"
                  + (f" ({pn})" if pn else "") + ":", "", "> " + self.clip_full(fn, c), ""]
        elif up:
            L += [f"UniProt [{up}](https://www.uniprot.org/uniprotkb/{up}) carries no function annotation.", ""]
        ez = an["entrez_id"]
        ns = sval(an["ncbi_summary"])
        if ns:
            src = f"[{int(ez)}](https://www.ncbi.nlm.nih.gov/gene/{int(ez)})" if _finite(ez) else ""
            L += [f"**Summary**, from NCBI Gene {src}:", "",
                  "> " + self.clip_full(ns, c), ""]
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

    def data_repo(self, path):
        """Where a file of the explorer's data repository is: '`x/16/16642.js` in <https://raw...-data/main/>'."""
        if self.data_url:
            return f"`{path}` of the data repository {self.xl(self.data_url + path)}"
        return f"`explorer/data/{path}` in the run folder"

    def sec_data(self, c, n_de):
        R = self.R
        nrel = R.rel_s[c + 1] - R.rel_s[c]
        return ["## Data", "",
                f"- **Explorer** (every value as stored, sortable, with CSV downloads): the pooled fold, z and q at "
                f"all {R.Dn:,} drug-doses {self.xl(self.xgene(c, 'drugs'))}; the {R.L} cell lines × {R.Dn:,} "
                f"drug-doses {self.xl(self.xgene(c, 'lines'))}; every well (corrected and raw) and the baseline "
                f"{self.xl(self.xgene(c, 'baseline'))}.",
                f"- **Its per-line and per-well values as a file**: {self.data_repo(LK.data_gene_path(c))} (the "
                "explorer reads it; `tsf_reader.py` on the explorer site reads it too).",
                f"- **Tables of this run** (gene col {c}): `tables/genes.parquet`, `tables/line_effects.parquet` "
                f"({R.L} rows) and `tables/drug_line_top.parquet` (col == {c}); `tables/drug_effects.parquet` "
                f"({n_de} rows, flagged included: the rows with |z| ≥ 3 or q < {Q_CUT:.2f}); "
                f"`relations/gene_relations.parquet` (col_a == {c}, {nrel} rows); `embed/gene_vectors.npy` [{c}]; "
                "`graph/nodes.parquet`"
                + (f"; `direction/edges.parquet` (source_col == {c} or target_col == {c})" if self.dv is not None
                   else "") + f". Every well: [[{self.plates_note[c]}]].",
                f"- **On the computer that made the run** (not exported to GitHub; their values are in the explorer): "
                f"`atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, {c}]; `tensor/DDL_lfc|DDL_z.npy` [{c}].",
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
        # drug vectors: cosine among every drug with a vector; a drug whose vector rests on few significant genes or
        # on a flagged or untrustworthy dose keeps its place with an alert (as the `drug` look-up)
        ed = os.path.join(self.out, "embed")
        self.drug_near = {}
        try:
            dv = np.load(os.path.join(ed, "drug_vectors.npy")).astype(np.float64)
            dt = pd.read_parquet(os.path.join(ed, "drugs.parquet"))
            min_act = int(R.embed_info.get("min_active", 10) or 10)
            self.drug_min_act = min_act
            nsig = pd.to_numeric(dt["n_sig_genes"], errors="coerce").fillna(0).to_numpy() \
                if "n_sig_genes" in dt else np.full(len(dt), min_act)
            trusted = dt["trusted"].fillna(True).astype(bool).to_numpy() if "trusted" in dt else \
                np.ones(len(dt), dtype=bool)
            vfl = dt["flags"].fillna("").astype(str).to_numpy() if "flags" in dt else np.array([""] * len(dt))
            valert = dt["alert"].fillna("").astype(str).to_numpy() if "alert" in dt else np.array([""] * len(dt))
            why = []
            for k in range(len(dt)):
                w = [f"only {int(nsig[k])} significant gene{'s' if nsig[k] != 1 else ''}"] if nsig[k] < min_act \
                    else []
                art = "; ".join(f for f in vfl[k].split("; ") if f in CM.ARTIFACT_FLAGS)
                if not trusted[k]:
                    w.append("no trustworthy dose" + (f" (vector dose flagged: {art})" if art else ""))
                elif art:
                    w.append(f"vector dose flagged: {art}")
                elif valert[k] and "flags" not in dt:
                    w.append(valert[k].lstrip(ALERT).strip())
                why.append("; ".join(w))
            nrm = np.linalg.norm(dv, axis=1)
            ok = nrm > 0
            U = np.where(ok[:, None], dv / np.maximum(nrm[:, None], 1e-12), 0.0)
            C = U @ U.T
            names = dt["drug"].astype(str).to_numpy()
            for i in np.flatnonzero(ok):
                cc = C[i].copy()
                cc[i] = -np.inf
                cc[~ok] = -np.inf
                order = [j for j in np.argsort(-cc, kind="stable") if np.isfinite(cc[j])]
                al = np.array([bool(why[j]) for j in order], dtype=bool)
                keep = cap_keep(al, N_NEAR_DRUGS)
                self.drug_near[names[i]] = ([(names[order[k]], cc[order[k]], why[order[k]]) for k in keep],
                                            len(order), int(al.sum()), why[i])
        except (OSError, KeyError) as e:
            log(f"  vault: no drug-vector neighbours ({e})")
        Az = self._load_opt(os.path.join(self.out, "atlas", "effects", "DD_Az.npy"))
        beta = self._load_opt(os.path.join(self.out, "atlas", "effects", "DD_beta.npy"))
        self.load_drug_extras()
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

    def load_drug_extras(self):
        """What a drug note shows beyond the tables of its doses, each optional (an older stage did not write it):
        the drug annotations (tables/drugs.parquet; else mechanisms.drug_annotations: reference/ or the code
        constants), the class labels (mechanisms.classes_by_drug), the ChEMBL release (tables/info.json), the most
        similar drug-doses (embed/drug_similarity.parquet), the unexpected-similarity notes (embed/drugdoses.parquet
        resembles_note), the salt-form notes (embed/drugs.parquet salt_form_alert), the line-selective controls
        (validation/line_controls.csv) and the control sets whose raisers are translation inhibitors
        (validation/control_sets.csv best_dd_up_without_tl)."""
        R, out = self.R, self.out
        self.ann_by_drug = {}
        if "annotation_status" not in R.tdrugs:
            try:
                for rec in MECH.drug_annotations(out).to_dict("records"):
                    self.ann_by_drug[str(rec["drug"])] = rec
            except Exception as e:  # noqa: BLE001  (no annotations at all: the notes say so)
                log(f"  vault: no drug annotations ({type(e).__name__}: {e})")
        try:
            keys = MECH.classes_by_drug(out)
            self.class_labels = {d: [MECH.class_info(k).get("label", k) for k in v] for d, v in keys.items()}
        except Exception:  # noqa: BLE001
            self.class_labels = {}
        ti = _read_json(os.path.join(out, "tables", "info.json")) or {}
        self.chembl_release = sval(ti.get("chembl_release")) or sval(
            (((R.sources or {}).get("sources") or {}).get("chembl") or {}).get("chembl_release"))
        if self.chembl_release and not self.chembl_release.lower().startswith("chembl"):
            self.chembl_release = f"ChEMBL {self.chembl_release}"
        self.similar = {}
        p = os.path.join(out, "embed", "drug_similarity.parquet")
        if os.path.exists(p):
            sim = pd.read_parquet(p).sort_values(["dd", "rank"])
            for dd, g_ in sim.groupby("dd", sort=False):
                self.similar[int(dd)] = g_
        self.resembles, self.salt_alert = {}, {}
        p = os.path.join(out, "embed", "drugdoses.parquet")
        if os.path.exists(p) and "resembles_note" in _columns(p):
            e = pd.read_parquet(p, columns=["dd", "resembles_note"])
            self.resembles = {int(a): sval(b) for a, b in zip(e["dd"], e["resembles_note"]) if sval(b)}
        p = os.path.join(out, "embed", "drugs.parquet")
        if os.path.exists(p) and "salt_form_alert" in _columns(p):
            e = pd.read_parquet(p, columns=["drug", "salt_form_alert"])
            self.salt_alert = {str(a): sval(b) for a, b in zip(e["drug"], e["salt_form_alert"]) if sval(b)}
        self.line_controls = {}
        p = os.path.join(out, "validation", "line_controls.csv")
        if os.path.exists(p):
            lc = pd.read_csv(p)
            for rec in lc.to_dict("records"):
                if sval(rec.get("drug")):
                    self.line_controls.setdefault(str(rec["drug"]), []).append(rec)
        self.sets_without_tl = []
        p = os.path.join(out, "validation", "control_sets.csv")
        if os.path.exists(p) and "best_dd_up_without_tl" in _columns_csv(p):
            cs = pd.read_csv(p)
            self.sets_without_tl = [r_ for r_ in cs.to_dict("records") if sval(r_.get("best_dd_up_without_tl"))]

    def per_dose_notes(self, d, rows):
        """'## Notes per dose': under each dose its neighbouring-well reading (tables drugdoses.parquet nb_alert; the
        'artifact' tier is an artifact flag, the others are shown as notes), an unexpected similarity to another class
        (embed/drugdoses.parquet resembles_note), the lines that respond out of proportion (selective_lines) and the
        comparison groups that explain them (direction/selectivity.parquet)."""
        R = self.R
        L = ["## Notes per dose", "",
             "*Neighbouring wells (`tables/drugdoses.parquet` nb_*), an unexpected similarity to another class "
             "(`embed/drugdoses.parquet` resembles_note), and the lines that respond out of proportion at the dose "
             "(selective: sel_z ≥ 3 with ≥ 20 genes beyond the per-line cut; `tables/drug_line_response.parquet`), "
             "with the comparison groups of the direction stage that explain them (`direction/selectivity.parquet`).*",
             ""]
        n0 = len(L)
        for i in rows:
            t = R.tdd.iloc[i]
            items = []
            tier = R.dd_nb_tier[i]
            if tier:
                p_ = int(R.dd_nb_partner[i])
                part = f" (the neighbour: {self.ddlink(p_)})" if 0 <= p_ < R.Dn else ""
                head = f"{ALERT} Like a neighbouring well" if tier == "artifact" else "Neighbouring well"
                items.append(f"{head}: {cell(sval(t.get('nb_alert')))}{part}")
            if self.resembles.get(int(i)):
                items.append(f"Resembles another class: {cell(self.resembles[int(i)])}")
            nsel = t.get("n_selective_lines")
            if _finite(nsel) and int(nsel) > 0:
                items.append(f"Selective lines ({int(nsel)}): {cell(sval(t.get('selective_lines')))}")
                sel = self.selectivity.get(int(i)) if hasattr(self, "selectivity") else None
                if sel is not None:
                    if sval(sel.get("organs_enriched")):
                        items.append(f"Organs enriched among them: {cell(sval(sel.get('organs_enriched')))}")
                    grp = split_top(sval(sel.get("groups")))
                    if grp:
                        items.append(f"Comparison groups that explain them ({len(grp)}): " + "; ".join(cell(x)
                                                                                                    for x in grp))
                    elif _truthy(sel.get("tested")):
                        items.append("No comparison group of the direction stage explains them.")
            if items:
                L += [f"- **{fdose(R.dd_dose[i])}**"] + [f"  - {x}" for x in items]
        if len(L) == n0:
            L += ["None of its doses has a neighbouring-well reading, an unexpected similarity or a selective line.",
                  ""]
        else:
            L += [""]
        return L

    def similar_block(self, d, info):
        """'## Most similar drug-doses': for the drug's best dose, the most similar drug-doses of
        embed/drug_similarity.parquet (cosine of the pooled signatures, and of the per-line contexts; genes significant
        in both; same compound; the other's classes and flags, its alert first): the N_SIMILAR strongest, '10 of 50;
        all 50 in the explorer'."""
        R = self.R
        g = (lambda k: sval(info.get(k)) if info is not None else "")
        bdd = int(float(g("best_dd"))) if _finite(g("best_dd")) else -1
        sim = self.similar.get(bdd) if bdd >= 0 else None
        if sim is None or not len(sim):
            return []
        n_all = len(sim)
        top = sim.head(N_SIMILAR)
        body = []
        for r_ in top.to_dict("records"):
            od = int(r_["other_dd"])
            fl = sval(r_.get("other_flags"))
            body.append([str(int(r_["rank"])), self.ddlink(od) if 0 <= od < R.Dn else cell(r_.get("other_drug")),
                         fcos(r_.get("cos_pooled")), fcos(r_.get("cos_contexts")), fint(r_.get("n_shared_sig")),
                         "yes" if _truthy(r_.get("same_salt_base")) else "",
                         cell(self.classes_short(sval(r_.get("other_drug")), sval(r_.get("other_classes")))) or "—",
                         flags_cell(fl)])
        L = ["## Most similar drug-doses", "",
             f"*For its best dose ({self.ddlink(bdd)}): the drug-doses with the most similar signature "
             "(`embed/drug_similarity.parquet`). cos pooled = cosine of the pooled z signatures (clipped at ±10); "
             "cos lines = cosine over the per-line contexts (— where they share too few); shared = genes significant "
             "in both; same compound = another dose or salt form of it. Class = the other's mechanism classes "
             f"(sources in its note). Flags: the other's flags of record, {ALERT} first.*", ""]
        L += table(["#", "Drug-dose", "cos pooled", "cos lines", "Shared", "Same compound", "Class", "Flags"],
                   body) + [""]
        L += [self.kofn(len(top), n_all, self.xdd(bdd), "drug-doses"), ""]
        return L

    def line_controls_block(self, d, rows=()):
        """The line-selective positive controls of the validation stage that use this drug
        (validation/line_controls.csv), and the control sets where it is one of the strongest raisers while being a
        translation inhibitor (control_sets.csv best_dd_up_without_tl)."""
        L = []
        rows_ = self.line_controls.get(str(d), [])
        if rows_:
            L += ["## Line-selective controls", "",
                  "*`validation/line_controls.csv`: a known line-selective response the validation stage checks "
                  "(AUROC of the lines' selectivity, group lines vs the others, with a permutation p).*", ""]
            L += table(["Control", "Dose", "AUROC", "p", "AUROC (response strength)", "Selective lines", "Note"],
                       [[cell(sval(r_.get("control"))), fdose(sval(r_.get("dose"))), g3(r_.get("auroc")),
                         g3(r_.get("p")), g3(r_.get("auroc_response_strength")),
                         cell(sval(r_.get("selective_lines"))) or "—", cell(sval(r_.get("note"))) or "—"]
                        for r_ in rows_]) + [""]
        tl = any(CM.TL_DD in str(self.R.dd_flags[i]).split("; ") for i in rows)
        mine = [r_ for r_ in self.sets_without_tl if tl and any(
            x.strip().startswith(f"{d} ") for x in split_top(sval(r_.get("best_dd_up"))))]
        if mine:
            L += ["## Control sets it raises as a translation inhibitor", "",
                  "*`validation/control_sets.csv`: sets whose strongest raisers include this drug. A translation "
                  "inhibitor raises many short-lived mRNAs whatever their pathway, so the stage also lists the "
                  "strongest raisers without translation inhibitors.*", ""]
            L += [f"- {cell(sval(r_.get('set')))}: without translation inhibitors: "
                  f"{cell(sval(r_.get('best_dd_up_without_tl')))}" for r_ in mine] + [""]
        return L

    def classes_short(self, drug, text=""):
        """The class labels of a drug ('; '-joined; '' when none): mechanisms.classes_by_drug, else the labels of a
        class text '{label} ({sources}); ...' (its last bracket at the top level is the sources)."""
        lab = self.class_labels.get(str(drug))
        if lab:
            return "; ".join(lab)
        return "; ".join(class_label_of(x) for x in split_top(sval(text)) if x)

    def annotations_block(self, d, info):
        """A drug note's 'Annotations' section: Tahoe's annotation verbatim, ChEMBL's (with the release, its name and
        id, how the molecule was matched), an alert where the two disagree, the notes, and the drug's mechanism
        classes with the source of each. Tahoe's own annotation is never overwritten."""
        g = (lambda k: sval(info.get(k)) if info is not None else "")
        a = self.ann_by_drug.get(str(d), {})
        ga = (lambda k: g(k) if info is not None and k in info.index else sval(a.get(k)))
        tg_, mf, mb = g("targets"), g("moa_fine"), g("moa_broad")
        L = ["## Annotations", "",
             "*Two annotations of the drug, side by side: Tahoe's drug metadata (verbatim) and ChEMBL's curated "
             "mechanisms (`tables/drugs.parquet`; `reference/drug_annotations.parquet`). Neither replaces the other; "
             f"{ALERT} marks where they disagree.*", "",
             f"- Tahoe: targets {tg_ or 'none listed'}; mechanism {mf or 'none listed'}"
             + (f" ({mb})" if mb else "") + "."]
        status = ga("annotation_status")
        cid, cname = ga("chembl_id"), ga("chembl_name")
        rel = self.chembl_release or "ChEMBL"
        if not status or status == MECH.NOT_LOADED:
            L.append("- ChEMBL: not loaded in this run (the reference stage ran offline without a cache, or before "
                     "ChEMBL was added: `tahoe run --from reference` with network access).")
        elif not cid:
            L.append("- ChEMBL: not found in ChEMBL" + (f" ({status})" if status and "not found" not in status
                                                         else "") + ".")
        else:
            L.append(f"- {rel}: {cname or '—'} ({cid}); mechanisms {ga('chembl_mechanisms') or 'none curated'}; "
                     f"targets {ga('chembl_targets') or 'none listed'}. Matched by "
                     f"{ga('chembl_matched_by') or 'name'}.")
        al = ga("annotation_alert")
        if al:
            L.append(f"- {ALERT} The two annotations disagree: {al}")
        for x in [y.strip() for y in ga("annotation_note").split(" | ") if y.strip()]:
            L.append(f"- Note: {x}")
        cls = ga("mechanism_classes")
        if cls:
            L.append(f"- Class: {cls}")
        return L + [""]

    def drug_note(self, d, rows, info, Az, beta):
        R, de = self.R, self.R.de
        o, dds = self._dd_rows
        g = (lambda k: sval(info.get(k)) if info is not None else "")
        doses = [R.dd_dose[i] for i in rows]
        a_ = self.ann_by_drug.get(str(d), {})
        ga = (lambda k: g(k) if info is not None and k in info.index else sval(a_.get(k)))
        cls_short = self.classes_short(d, ga("mechanism_classes"))
        fm = {"drug": d, "type": "drug", "salt_base": g("salt_base") or T.salt_base(d), "targets": g("targets"),
              "moa_fine": g("moa_fine"), "moa_broad": g("moa_broad"), "approved": g("approved"),
              "chembl_id": ga("chembl_id"), "chembl_mechanisms": ga("chembl_mechanisms"),
              "classes": [x for x in cls_short.split("; ") if x],
              "annotation_alert": bool(ga("annotation_alert")),
              "doses": doses, "best_dose": g("best_dose"),
              "max_sig_genes": int(info["max_sig"]) if info is not None and _finite(info.get("max_sig")) else None,
              "tags": ["drug"] + ([f"moa/{safe_filename(g('moa_broad')).replace(' ', '-').lower()}"]
                                  if g("moa_broad") else [])
              + (["annotations-disagree"] if ga("annotation_alert") else [])}
        self.lit_frontmatter("drug", d, fm)
        L = [frontmatter(fm), f"# {d}", "", self.top_line(self.xdrug(d)), ""]
        sub = [x for x in (" ".join(y for y in (g("moa_fine"), g("moa_broad") and f"({g('moa_broad')})") if y),)
               if x]
        if g("targets"):
            sub.append("targets: " + g("targets"))
        if g("approved"):
            sub.append("approved: " + g("approved"))
        if sub:
            L += ["*Tahoe: " + cell(" · ".join(sub)) + "*", ""]
        if self.salt_alert.get(str(d)):
            L += [f"{ALERT} Salt forms: {self.salt_alert[str(d)]} (`embed/drugs.parquet` salt_form_alert)", ""]
        L += self.annotations_block(d, info)
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
                al = [f"{fdose(R.dd_dose[i])}: {'; '.join(flag_parts(R.dd_flags[i])[0])}" for i in rows
                      if R.dd_artifact[i]]          # the flags of record (common.has_artifact)
                S.append(f"Flags by dose: {cell(g('flags_by_dose'))}." + (
                    f" {ALERT} " + "; ".join(al) + " (artifact flags: its changes there are shown with an alert, not "
                    "left out)." if al else ""))
        if S:
            L += ["> [!summary] At a glance"] + ["> " + x for x in S] + [""]
        # doses table
        body = []
        by_dose = parse_dose_plates(g("dose_plates"))         # tables version 5: 'dose: plate well, ...' per dose
        for i in rows:
            t = R.tdd.iloc[i]
            wells = []
            pw = by_dose.get(str(R.dd_dose[i]))
            if pw is None:      # an older tables stage: drugdoses.parquet plates and wells, each sorted on its own,
                pls = [x.strip() for x in re.split(r"[,;]", sval(t["plates"])) if x.strip()]   # so a well's plate
                wl = [x.strip() for x in re.split(r"[,;]", sval(t["wells"])) if x.strip()]     # is known only when
                pw = [(pls[0], w) for w in wl] if len(pls) == 1 else \
                    [(", ".join(pls), "wells " + ", ".join(wl))]                                 # there is one plate
            for p, w in pw:
                pn = self.plate_name.get(p)
                wells.append(f"[[{pn}]] {w}" if pn else f"{p} {w}".strip())
            mods = "/".join(fz(t.get(f"{m}_z")) for m in ("S_PHASE", "G2M_PHASE", "PROTEASOME"))
            body.append([fdose(R.dd_dose[i]), ", ".join(wells) or "—",
                         f"{fint(t['n_genes_up'], '0')} / {fint(t['n_genes_down'], '0')}", g3(t.get("replicate_r")),
                         flog(t.get("cells_log2_vs_plate")), mods, flags_cell(R.dd_flags[i])])
        share = bool(info is not None and "doses_share_a_plate" in info.index and _truthy(info.get(
            "doses_share_a_plate")))
        L += ["## Doses", "",
              "*`tables/drugdoses.parquet`. Plate, well = where each dose sits: each dose of a drug sits on its own "
              "plate (for most drugs the same well on the plates of that dose), so a pattern over the doses compares "
              "plates as much as doses"
              + (f"; {ALERT} here some of its doses share a plate (`tables/drugs.parquet` dose_plates: "
                 f"{cell(g('dose_plates'))})" if share else
                 (f" (`tables/drugs.parquet` dose_plates: {cell(g('dose_plates'))})" if g("dose_plates") else ""))
              + ". Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = "
              "log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle "
              f"mix and proteasome load). Flags: {ALERT} = artifact flags (the changes may come from cell death, a "
              "drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce, a "
              "well-position problem or a neighbouring well); after · the caveats. A `cell-cycle shift` is weighed "
              "per gene: the gene lists below say for which genes it explains the change.*", ""]
        L += table(["Dose", "Plate, well", "Sig. genes up / down", "Replicate r", "Cells (log2)", "S / G2M / prot. z",
                    "Flags"], body) + [""]
        L += self.flag_notes([R.dd_flags[i] for i in rows], rows)
        L += self.per_dose_notes(d, rows)
        # genes per dose
        for dname, sgn in (("raises", 1), ("lowers", -1)):
            L += [f"## Genes it {dname}", "",
                  "*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the "
                  f"row of the dose): the {N_GENES_DOSE} strongest, and any of the {N_GENES_DOSE} strongest without "
                  f"an alert below them. {ALERT} = an artifact flag on the drug-dose or on the gene: shown, not left "
                  "out; its reasons are the dose's own alert, named once after the dose, unless they are given in "
                  "the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift "
                  "explains; a gene without the alert at such a dose is one whose change the shift does not "
                  "explain.*", ""]
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
                rr = rr[np.argsort(-sgn * z, kind="stable")]
                als = [alert_text(de["flags"][r], de["cc_share"][r]) for r in rr]
                keep = cap_keep([bool(a) for a in als], N_GENES_DOSE)
                anyrow = True
                dose_al = alert_text(R.dd_flags[i])
                items = []
                for k in keep:
                    r = rr[k]
                    nl = de["n_lines_up" if sgn > 0 else "n_lines_down"][r]
                    a = als[k]                      # ⚠ after the gene; its reasons when they are not the dose's
                    why = a[len(ALERT) + 1:] if a and a != dose_al else ""
                    cav_ = caveat_text(de["flags"][r]).split("; ")
                    cc_ = [x for x in cav_ if x.startswith(CC_FLAG)]
                    nbc = ["the neighbour does not move this gene"] if CM.NB_CLEARED in cav_ else []
                    items.append(f"{self.glink(de['col'][r])}{f' {ALERT}' if a else ''} {ffold(de['fold'][r])} "
                                 f"(z {fz(de['z'][r])}, {int(nl)}/{int(de['n_lines_measured'][r])} lines"
                                 + fwells_of(de["n_wells"][r])
                                 + "".join(f"; {x}" for x in [why] + cc_[:1] + nbc if x) + ")")
                n_all, n_al = len(rr), sum(1 for a in als if a)
                dcav = [t for t in CM.FLAG_TEXT if t not in CM.ARTIFACT_FLAGS and t in R.dd_flags[i].split("; ")]
                head = (f"**{fdose(R.dd_dose[i])}** ({n_all} gene{'s' if n_all != 1 else ''}, {n_alerts(n_al)}"
                        + (f"; the drug-dose carries {dose_al}" if dose_al else "")
                        + (f"; caveat: {', '.join(dcav)} (see the doses above)" if dcav else "") + "): ")
                L += [head + ", ".join(items) + " " + self.kofn(len(keep), n_all, self.xdd(i), "genes"), ""]
            if not anyrow:
                L += [f"No gene is significantly {'raised' if sgn > 0 else 'lowered'} at any dose.", ""]
            if sgn < 0:
                L += [f"*Every one of the {R.gK:,} genes at each dose, with its exact pooled fold, z, q and flags, "
                      "and its value in each cell line: the dose's page in the explorer, "
                      + "; ".join(f"{fdose(R.dd_dose[i])} {self.xl(self.xdd(i))}" for i in rows) + ".*", ""]
        # modules
        if R.mod_z is not None and len(self.module_name):
            body = []
            mods = R.modules["module"].astype(int).to_numpy()
            for i in rows:
                z = R.mod_z[:, i]
                if not np.isfinite(z).any():
                    continue
                oo = np.argsort(-np.nan_to_num(z, nan=0.0))
                n_up, n_dn = int((np.nan_to_num(z) >= 2).sum()), int((np.nan_to_num(z) <= -2).sum())
                up = [f"{self.mlink(mods[j])} ({fz(z[j])})" for j in oo[:3] if z[j] >= 2]
                dn = [f"{self.mlink(mods[j])} ({fz(z[j])})" for j in oo[::-1][:3] if z[j] <= -2]
                body.append([fdose(R.dd_dose[i]),
                             (", ".join(up) + (f" ({len(up)} of {n_up})" if n_up > len(up) else "")) or "—",
                             (", ".join(dn) + (f" ({len(dn)} of {n_dn})" if n_dn > len(dn) else "")) or "—"])
            L += ["## Modules it moves", "",
                  "*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module "
                  "(`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm "
                  "down (its genes up, in a single-armed module).*", ""]
            L += table(["Dose", "Raises", "Lowers"], body) + [""]
            L += ["*The 3 strongest each way per dose; (k of N) = N modules reach |z| ≥ 2. Every module's score at "
                  "each dose: " + "; ".join(f"{fdose(R.dd_dose[i])} {self.xl(self.xdd(i))}" for i in rows) + ".*",
                  ""]
        # lines
        if Az is not None or beta is not None:
            body = []
            for i in rows:
                dep = resp = "—"
                if Az is not None:
                    a = Az[i]
                    dep_all = [j for j in np.argsort(np.nan_to_num(a, nan=0.0)) if _finite(a[j]) and a[j] <= -3]
                    oo = dep_all[:5]
                    dep = ", ".join(f"{self.llink(j)} ({fz(a[j])})" for j in oo) or "—"
                    if len(dep_all) > len(oo):
                        dep += f" ({len(oo)} of {len(dep_all)})"
                if beta is not None and R.dd_nsig[i] >= 20:
                    b = beta[i]
                    fin = [j for j in np.argsort(-np.nan_to_num(b, nan=-np.inf), kind="stable") if _finite(b[j])]
                    k = min(4, len(fin) // 2)                  # strongest and weakest never share a line
                    oo, lo = (fin[:k], fin[::-1][:min(3, k)]) if k else (fin, [])
                    resp = ", ".join(f"{self.llink(j)} ({g3(b[j])})" for j in oo) or "—"
                    if lo:
                        resp += " · weakest: " + ", ".join(f"{self.llink(j)} ({g3(b[j])})" for j in lo)
                    if len(fin) > len(oo) + len(lo):
                        resp += f" ({len(oo) + len(lo)} of {len(fin)} lines)"
                body.append([fdose(R.dd_dose[i]), dep, resp])
            L += ["## In which cell lines", "",
                  "*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or "
                  "stops that line more than the others). Response strength β = slope of the line's changes on the "
                  "drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no "
                  "response; drug-doses with ≥ 20 significant genes).*", ""]
            L += table(["Dose", "Most depleted lines (Az)", "Strongest responders (β)"], body) + [""]
            L += ["*(k of N) = k lines named of the N that qualify. Every line at each dose (abundance A, its z, β, "
                  "the cell-cycle and proteasome modules): " + "; ".join(f"{fdose(R.dd_dose[i])} "
                                                                         f"{self.xl(self.xdd(i))}" for i in rows)
                  + ".*", ""]
        L += self.similar_block(d, info)
        L += self.line_controls_block(d, rows)
        near = self.drug_near.get(d)
        if near and near[0]:
            lst, n_all, n_al, own = near
            extra = max(0, len(lst) - N_NEAR_DRUGS)
            L += ["## Nearest drugs in the vector space", "",
                  "*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; "
                  "`embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector "
                  f"is ranked; {ALERT} = its vector rests on fewer than the space's {self.drug_min_act} "
                  "significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` "
                  "alert); such a drug keeps its place.*", ""]
            if own:
                L += [f"{ALERT} This drug's own vector: {own}. Read its neighbours with that in mind.", ""]
            L += [f"*{n_all:,} other drugs have a vector, {n_alerts(n_al)}; shown: the {min(N_NEAR_DRUGS, n_all)} "
                  "most similar" + (f" and the {extra} next most similar without an alert" if extra else "") + ".* "
                  + self.kofn(len(lst), n_all, self.xdrug(d), "drugs"), ""]
            moa = R.tdrugs.set_index(R.tdrugs["drug"].astype(str))["moa_fine"] if "moa_fine" in R.tdrugs else None
            L += ["- " + "; ".join(f"{self.dlink(n)} ({fcos(v)}"
                                   + (f", {cell(sval(moa.get(n)))}" if moa is not None and sval(moa.get(n)) else "")
                                   + (f", {ALERT} {w}" if w else "") + ")" for n, v, w in lst), ""]
        L += self.sec_direction_drug(d, rows)
        L += self.sec_literature("drug", d, f"Drugs/{self.drug_name[d]}.md")
        L += ["## Data", "",
              "- **Explorer** (every gene at every dose, exact, sortable, with CSV downloads): "
              + self.xl(self.xdrug(d))
              + "".join(f"; {fdose(R.dd_dose[i])}: {self.xl(self.xdd(i))}" for i in rows),
              "- **Every gene at each dose as a file**: " + "; ".join(
                  f"{fdose(R.dd_dose[i])} {self.data_repo(LK.data_dd_path(i))}" for i in rows),
              "- `tables/drugs.parquet` — drug == " + json.dumps(d),
              "- `tables/drugdoses.parquet` — dd in " + ", ".join(str(i) for i in rows),
              "- `tables/drug_effects.parquet` — rows with dd in those rows (|z| ≥ 3 or q < 0.10 only); "
              "`embed/drugdose_vectors.npy` — those rows",
              "- On the computer that made the run (not exported to GitHub; their values are in the explorer): "
              "`atlas/effects/DD_*.npy` — those rows"]
        if self.dv is not None:
            L += ["- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include "
                  "it"]
        return "\n".join(L + [""])

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
        cc, ll = le["col"].astype(int), le["line"].astype(int)
        base[cc, ll] = le["baseline_cpm"]
        expr[cc, ll] = le["expressed"].astype(bool)
        # per direction: (count over all drug-doses, count over the clean ones); an older tables stage has only the
        # clean counts, which then stand for both
        counts = {}
        for d in ("up", "down"):
            M = {}
            for sx in ("", "_all"):
                k = f"n_dd_{d}{sx}"
                if k in le:
                    M[sx] = np.zeros((gK, L_))
                    M[sx][cc, ll] = np.nan_to_num(le[k].astype(float))
            counts[d] = (M.get("_all", M[""]), M[""])
        nup, ndn = counts["up"], counts["down"]
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", category=RuntimeWarning)
            med = np.nanmedian(base, axis=1)
        comp = _read(os.path.join(self.out, "embed", "components.parquet"))
        sens = self._load_opt(os.path.join(self.out, "embed", "line_response_vectors.npy"))
        clean_dd = ~R.dd_artifact
        # tables version 5: per (drug-dose, line) the response strength and the line selectivity
        self.dlr_sel, self.has_dlr = {}, False
        p = os.path.join(self.out, "tables", "drug_line_response.parquet")
        if os.path.exists(p):
            self.has_dlr = True
            dlr = pd.read_parquet(p, columns=["dd", "line", "n_genes", "sel_z", "selective", "abundance_z",
                                              "response_strength", "flags"])
            dlr = dlr[dlr["selective"].fillna(False).astype(bool)].sort_values(["line", "sel_z"],
                                                                                ascending=[True, False])
            for ln_, g_ in dlr.groupby("line", sort=False):
                self.dlr_sel[int(ln_)] = g_
        di = (self.dv.info or {}) if self.dv is not None else {}
        self.heavy = {str(k): v for k, v in (di.get("heavily_mutated_lines") or {}).items()}
        for line in range(L_):
            self.W.write(f"Cell lines/{self.line_name[line]}.md",
                         self.line_note(line, base, expr, med, nup, ndn, Az, A_, beta, clean_dd, comp, sens))

    def sec_line_selective(self, line):
        """'Drug-doses where this line responds out of proportion': every selective (drug-dose, line) row of
        tables/drug_line_response.parquet for the line (sel_z >= 3 with >= 20 genes beyond the per-line cut), by sel_z,
        with its genes, sel_z, abundance z, response strength and flags; then the selectivity arrows of the direction
        stage's groups that hold this line."""
        L = ["## Drug-doses where this line responds out of proportion", ""]
        if not getattr(self, "has_dlr", False):
            return L + ["This run's tables (an older tables stage) have no `tables/drug_line_response.parquet`.", ""]
        g_ = self.dlr_sel.get(int(line))
        L += ["*`tables/drug_line_response.parquet` (line == "
              f"{line}, selective): the line moves many more genes beyond the per-line cut than the other lines at "
              "that drug-dose (sel_z = its log2 gene count against the drug-dose's lines, in robust z units; "
              "selective = sel_z ≥ 3 and ≥ 20 genes). Every such drug-dose, strongest first. Abundance z = how its "
              "cells fare against the other lines in the same wells; response strength = the slope of its changes on "
              f"the drug-dose's consensus (1 = a typical line). {ALERT} = the drug-dose's artifact flags.*", ""]
        if g_ is None or not len(g_):
            L += ["None: at no drug-dose does this line respond out of proportion.", ""]
        else:
            L += table(["Drug-dose", "Genes", "sel_z", "Abundance z", "Response strength", "Flags"],
                       [[self.ddlink(int(x["dd"])), fint(x["n_genes"]), g3(x["sel_z"]), fz(x["abundance_z"]),
                         g3(x["response_strength"]), flags_cell(sval(x["flags"]))] for x in g_.to_dict("records")]) \
                + [""]
        if self.dv is not None:
            descs = {str(x.get("description", "")) for x in self.dir_line_groups.get(line, [])}
            if descs:
                if not hasattr(self, "_sel_pos"):
                    self._sel_pos = np.flatnonzero(np.isin(self.dir_col["kind"].astype(str), list(DV.SELECTIVITY)))
                sp_ = self._sel_pos
                pos = sp_[np.array([str(self.dir_col["group"][i]) in descs for i in sp_], dtype=bool)] \
                    if len(sp_) else sp_
                if len(pos):
                    shown, cnt = self._dir_list(pos, N_DIR_LINE, url=self.xline(line))
                    L += ["### Its selectivity arrows", "",
                          "*Arrows gene → the response to a drug-dose (line selectivity) from the comparison groups "
                          f"that count this line as altered or lacking the gene. {cnt}*", ""]
                    L += self._dir_table(shown, "source", extra=[("Response to", self._dir_target)],
                                         first_head="Gene") + [""]
        return L

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
        L = [frontmatter(fm), f"# {R.cell[line]}", "", self.top_line(self.xline(line)), "",
             f"*{cell(sval(t.get('Organ')) or 'organ unknown')} · TP53 {tp53_text(R.tp53[line])} · "
             f"{cell(sval(t.get('cell_line_id')))} · {cell(sval(t.get('Cell_ID_DepMap')))}*", ""]
        hv = self.heavy.get(R.cell[line])
        if hv is not None:
            L += [f"{ALERT} Heavily mutated: it records alterations in {fint(hv)} driver genes (15 or more; "
                  "`direction/info.json` heavily_mutated_lines). Such lines carry many recorded and unrecorded "
                  "changes: in a comparison of genotypes any of them, or the mutation load itself, could be the "
                  "cause.", ""]
        rows = [["Organ", sval(t.get("Organ")) or "—"], ["TP53 status", tp53_text(R.tp53[line])],
                ["Drivers", sval(t.get("drivers")) or "—"], ["Driver changes", sval(t.get("driver_changes")) or "—"],
                ["Cells over all wells", fint(t.get("n_cells_total"))],
                ["Wells with usable expression", f"{fint(t.get('wells_usable'))} ({g3(t.get('pct_wells_usable'))}%)"],
                ["Median response strength (β)", g3(t.get("median_response")) + " (1 = a typical line)"],
                ["Drug-doses that deplete it", self._depleted_text(t)],
                ["Genes it measures (expresses above the ambient level)", f"{int(expr[:, line].sum()):,} of {R.gK:,}"]]
        L += table(["", ""], rows) + [""]
        if Az is not None:
            a = Az[:, line]
            oo = np.array([i for i in np.argsort(np.nan_to_num(a, nan=np.inf), kind="stable")
                           if _finite(a[i]) and a[i] <= -3], dtype=np.int64)
            al = ~clean_dd[oo]
            keep = oo[cap_keep(al, N_LINE_LIST)]
            L += ["## Drug-doses that deplete it", "",
                  f"*Drug-doses with relative-abundance z ≤ −3 (`atlas/effects/DD_Az.npy`, column {line}): the line "
                  "loses cells relative to the other lines in the same wells. Drug-doses: "
                  f"{shown_text(len(oo), int(al.sum()), len(keep), N_LINE_LIST, max(0, len(keep) - N_LINE_LIST))}"
                  f". {ALERT} = the drug-dose's artifact flags. Of them `unreliable plate only`, `position not "
                  "correctable` and `wells disagree` make its cell counts untrustworthy: the count in the table above "
                  "leaves such drug-doses out, this list shows them.*", ""]
            if len(keep):
                L += table(["Drug-dose", "Alert", "Abundance z", "log2 relative abundance"],
                           [[self.ddlink(i), alert_text(R.dd_flags[i]), fz(a[i]),
                             flog(A_[i, line]) if A_ is not None else "—"] for i in keep]) + [""]
                L += [self.kofn(len(keep), len(oo), self.xline(line), "drug-doses") + f" The explorer lists all "
                      f"{R.Dn:,} drug-doses for this line, with abundance, its z and β.", ""]
            else:
                L += ["None.", ""]
        if beta is not None:
            b = np.where(R.dd_nsig >= 20, beta[:, line], np.nan)
            fin = np.array([i for i in np.argsort(-np.nan_to_num(b, nan=-np.inf), kind="stable") if _finite(b[i])],
                           dtype=np.int64)
            k = min(8, len(fin) // 2)                          # strongest and weakest never share a drug-dose
            if k:
                half = len(fin) // 2
                top, bot = fin[:half], fin[::-1][:half]
                hi, lo = top[cap_keep(~clean_dd[top], k)], bot[cap_keep(~clean_dd[bot], k)]
            else:
                hi, lo = fin, fin[:0]

            def item(i):
                al_ = alert_text(R.dd_flags[i])
                return f"{self.ddlink(i)} ({g3(b[i])}" + (f", {al_}" if al_ else "") + ")"
            L += ["## How strongly it responds", "",
                  "*β = slope of the line's changes on the drug-dose's consensus (`atlas/effects/DD_beta.npy`; 1 = "
                  f"typical, 0 = no response), drug-doses with ≥ 20 significant genes: {len(fin):,}, "
                  f"{n_alerts(int((~clean_dd[fin]).sum()))}. The {k or len(fin)} strongest and weakest, and any of "
                  f"the {k or len(fin)} strongest and weakest without an alert beyond them; {ALERT} = the drug-dose's "
                  "artifact flags.*", ""]
            if len(hi):
                L += ["- Strongest: " + "; ".join(item(i) for i in hi)]
                L += (["- Weakest: " + "; ".join(item(i) for i in lo)] if len(lo) else []) + [""]
                L += [self.kofn(len(hi) + len(lo), len(fin), self.xline(line), "drug-doses"), ""]
            else:
                L += ["No drug-dose qualifies.", ""]
        L += self.sec_line_selective(line)
        # genes it moves most
        if R.le_all:
            what = (f"Genes with the most drug-doses moving them ≥ {R.line_fold:.3g}× at {self.line_cut_text()} in "
                    f"this line (`tables/line_effects.parquet`, line == {line}): in brackets the number of drug-doses, "
                    f"and how many of them carry an alert ({ALERT}); the {N_LINE_LIST} with the most, and any of the "
                    f"{N_LINE_LIST} with the most drug-doses without an alert beyond them.")
        else:
            what = (f"Genes with the most clean drug-doses moving them ≥ {R.line_fold:.3g}× at {self.line_cut_text()} "
                    f"in this line (`tables/line_effects.parquet`, line == {line}; this run's table, from an older "
                    "tables stage, counts only drug-doses without an artifact flag).")
        L += ["## Genes it moves most", "", f"*{what}*", ""]
        for nm, (Ma, Mc) in (("up", nup), ("down", ndn)):
            va, vc = Ma[:, line], Mc[:, line]
            top = [i for i in np.argsort(-va, kind="stable")[:N_LINE_LIST] if va[i] > 0]
            st = set(top)
            more = [i for i in np.argsort(-vc, kind="stable")[:N_LINE_LIST] if vc[i] > 0 and i not in st]
            oo = sorted(top + more, key=lambda i: (-va[i], -vc[i], i))
            n_all = int((va > 0).sum())
            L += [f"- {nm}: " + (", ".join(f"{self.glink(i)} ({int(va[i])}"
                                           + (f", {int(va[i] - vc[i])} {ALERT}" if va[i] > vc[i] else "") + ")"
                                           for i in oo) or "none")
                  + (" " + self.kofn(len(oo), n_all, self.xline(line), "genes") if n_all else "")]
        L += [""]
        # line-specific levels
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", category=RuntimeWarning)
            ratio = np.log2((base[:, line] + 1.0) / (med + 1.0))
        hi_all = [i for i in np.argsort(-np.nan_to_num(ratio, nan=-np.inf), kind="stable") if _finite(ratio[i])
                  and ratio[i] >= 1 and base[i, line] >= 10]
        lo_all = [i for i in np.argsort(np.nan_to_num(ratio, nan=np.inf), kind="stable") if _finite(ratio[i])
                  and ratio[i] <= -1 and med[i] >= 20 and not expr[i, line]]

        def lvl_alert(i, own=True):
            """Why a baseline call may mislead: a noise-class RNA; (own) a level here that is only ambient RNA."""
            return "; ".join((["noise-class RNA"] if R.noise[i] else []) +
                             (["only ambient RNA here"] if own and not expr[i, line] else []))

        def lvl_list(lst, own):
            why = [lvl_alert(i, own) for i in lst]
            keep = cap_keep([bool(w) for w in why], N_OWN_LEVEL)
            n_al = sum(1 for w in why if w)
            items = ", ".join(f"{self.glink(lst[k])} ({ratio[lst[k]]:+.1f}" + (f", {ALERT} {why[k]}" if why[k] else "")
                              + ")" for k in keep) or "none"
            cnt = (f" ({len(lst):,} genes, {n_alerts(n_al)}" + (f"; shown: the {N_OWN_LEVEL} strongest"
                                                                 + (" and the next strongest without an alert"
                                                                    if len(keep) > N_OWN_LEVEL else "")
                                                                 if len(keep) < len(lst) else "") + ")") if lst else ""
            return items + cnt + (" " + self.kofn(len(keep), len(lst), self.xline(line), "genes") if lst else "")
        L += ["## Its own level", "",
              "*Baseline CPM in this line vs the median line (`tables/line_effects.parquet` baseline_cpm; log2 "
              "ratio). Highest = at least 2× the median line and ≥ 10 CPM here. Lacks = expressed at ≥ 20 CPM in "
              "the median line, not measured here (below 25% of the "
              f"median line, or below {R.amb_frac:g} × the gene's pooled level, where the line reads only ambient "
              f"RNA; deletion, silencing or lineage). {ALERT} = a noise-class RNA, or a level here that is only "
              "ambient RNA (kept in its rank).*", "",
              "- Highest relative to other lines: " + lvl_list(hi_all, True),
              "- Lacks: " + lvl_list(lo_all, False), ""]
        if sens is not None and comp is not None and np.isfinite(sens[line]).any():
            s = sens[line]

            def comp_text(j):
                cr = comp.iloc[j]
                pos, neg = ([x for x in sval(cr[k]).split(", ") if x] for k in ("top_pos_genes", "top_neg_genes"))
                return (f"component {int(cr['component'])} ({g3(s[j])}; genes "
                        f"{cell(', '.join(pos[:4]))}{f' (4 of {len(pos)})' if len(pos) > 4 else ''} / "
                        f"{cell(', '.join(neg[:4]))}{f' (4 of {len(neg)})' if len(neg) > 4 else ''})")
            ok = [j for j in range(min(len(s), len(comp))) if _finite(s[j])]
            low_all = sorted([j for j in ok if s[j] < 0.7], key=lambda j: s[j])
            high_all = sorted([j for j in ok if s[j] > 1.5], key=lambda j: -s[j])
            low, high = low_all[:4], high_all[:4]
            L += ["## In the vector space", "",
                  "*Response sensitivity per component of the space (`embed/line_response_vectors.npy` row "
                  f"{line}): 1 = the programme responds as in a typical line, 0 = it does not respond here. Genes = "
                  "the component's top + / − genes.*", ""]
            if low:
                L += ["- Weak here (< 0.7): " + "; ".join(comp_text(j) for j in low)
                      + (" " + self.kofn(len(low), len(low_all), self.xline(line), "components")
                         if len(low_all) > len(low) else "")]
            if high:
                L += ["- Strong here (> 1.5): " + "; ".join(comp_text(j) for j in high)
                      + (" " + self.kofn(len(high), len(high_all), self.xline(line), "components")
                         if len(high_all) > len(high) else "")]
            if not low and not high:
                L += [f"- Every component responds within 0.7–1.5 of a typical line (range {g3(np.nanmin(s))} to "
                      f"{g3(np.nanmax(s))})."]
            L += [""]
        L += self.sec_direction_line(line)
        L += self.sec_literature("line", line, f"Cell lines/{self.line_name[line]}.md")
        L += ["## Data", "",
              f"- **Explorer** (every drug-dose and every gene for this line, exact, sortable, with CSV downloads): "
              f"{self.xl(self.xline(line))}. One gene in this line at every drug-dose: the gene's page, "
              "Cell lines tab.",
              f"- `tables/lines.parquet` — line == {line}; `tables/line_effects.parquet` — line == {line}",
              f"- On the computer that made the run (not exported to GitHub; their values are in the explorer): "
              f"`atlas/effects/DD_A.npy`, `DD_Az.npy`, `DD_beta.npy`, `line_cpm.npy` — column / row {line}; "
              f"`tensor/DDL_lfc.npy`, `DDL_z.npy` — [:, :, {line}]"]
        if self.dv is not None:
            L += ["- `direction/groups.parquet` — the genotype and natural-knockout groups whose altered_lines "
                  f"include {R.cell[line]}"]
        return "\n".join(L + [""])

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
               f"{ALERT} **unreliable** (its replicate wells do not reproduce)" if g("unreliable") else "reliable"]
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
        body, n_al = [], 0
        for s in sorted(rec):
            wl, drug, dose, cells_, cl, fl, dm = rec[s]
            al = [x for x in fl if x in WELL_ALERTS]
            n_al += bool(al)
            rest = [x for x in fl if x not in WELL_ALERTS]
            body.append([wl, "DMSO" if dm else self.dlink(drug), fdose(dose) if not dm else "—", fint(cells_),
                         flog(cl), " · ".join(x for x in ((f"{ALERT} " + ", ".join(al)) if al else "",
                                                          ", ".join(rest)) if x)])
        L += ["## Wells", "", "*Cells = cells of the analysed lines in the well; log2 vs plate = cells vs the plate's "
              f"median drug well. Every well of the plate is listed: {len(body)}, {n_alerts(n_al)} (on an unreliable "
              "plate, without a position correction, not used in its drug-dose or failed: what the run did with it "
              "is said, nothing is hidden).*", ""]
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
        lr = R.mod_label_row.get(int(m)) or {}
        alerts = [x.strip() for x in sval(lr.get("label_alert")).split(f"; {ALERT}") if x.strip()]
        alerts = [x if x.startswith(ALERT) else f"{ALERT} {x}" for x in alerts]
        if alerts:
            fm["label_alert"] = True
            fm["tags"] = fm["tags"] + ["label-alert"]
        L = [frontmatter(fm), f"# {name}" + (f": {cell(lt)}" if lt else ""), "", self.top_line(self.xmodule(m)), ""] \
            + [f"> {x}" for x in alerts] + ([""] if alerts else []) + [
            f"*{cell(lt) + ' · ' if lt else ''}{len(mem)} genes ({armline}) · [[{name}.canvas|open the canvas]]*", "",
            "A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| "
            f"that have the {REL.SAME_SIGN} (`both halves`, fdr ≤ {REPRO_FDR:.2f}) or are very strong in one random "
            "half (`graph/`). " + self.arms_text(m) +
            (" The + arm rises where the − arm falls. Arm = the side of the module's main direction a gene sits on."
             if opp else ""), ""]
        L += self.module_label_lines(m, lab, lr)
        if R.mod_enrich is not None:
            e_all = R.mod_enrich[(R.mod_enrich["module"] == m) & (R.mod_enrich["q"] < 0.05)].sort_values("q")
            e = e_all.head(8)
            if len(e):
                L += ["## Enriched for", "",
                      "*Hypergeometric test per arm, BH q (`validation/module_enrichment.csv`): the 8 with the "
                      f"smallest q of the {len(e_all):,} sets with q < 0.05.*", ""]
                L += table(["Arm", "Set", "Source", "Overlap", "Fold", "q"],
                           [[r.arm, r.set_label, r.source, f"{int(r.overlap)}/{int(r.n_unit)}", g3(r.fold), fq(r.q)]
                            for r in e.itertuples(index=False)]) + [""]
                L += [self.kofn(len(e), len(e_all), self.xmodule(m), "sets") + " The explorer lists every "
                      "enrichment row of the module.", ""]
        if R.mod_z is not None:
            z = R.mod_z[k]
            oo = np.argsort(-np.nan_to_num(z, nan=0.0), kind="stable")
            up = np.array([i for i in oo if _finite(z[i]) and z[i] >= 1], dtype=np.int64)
            dn = np.array([i for i in oo[::-1] if _finite(z[i]) and z[i] <= -1], dtype=np.int64)

            def items(ii):
                kk = ii[cap_keep(R.dd_artifact[ii], N_MOD_DRUGS)]
                txt = "; ".join(f"{self.ddlink(i)} ({fz(z[i])}" + (f", {alert_text(R.dd_flags[i])}"
                                                                   if R.dd_artifact[i] else "") + ")" for i in kk)
                cnt = shown_text(len(ii), int(R.dd_artifact[ii].sum()), len(kk), N_MOD_DRUGS,
                                 max(0, len(kk) - N_MOD_DRUGS))
                return (f"{txt} ({cnt}) " + self.kofn(len(kk), len(ii), self.xmodule(m), "drug-doses")
                        if txt else "none")
            L += ["## Drugs that move it", "",
                  ("*Mean pooled z of the + arm minus the − arm" if opp else "*Mean pooled z of its genes") +
                  f" (`graph/module_pooled_z.npy`, row {k}), drug-doses with |z| ≥ 1: the {N_MOD_DRUGS} strongest, "
                  f"and any of the {N_MOD_DRUGS} strongest without an alert beyond them. {ALERT} = the drug-dose's "
                  "artifact flags: the module may move because of what the drug-dose did to the cells (cell death, "
                  "a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*", ""]
            L += [("- Raise it (+ arm up, − arm down): " if opp else "- Raise it: ") + items(up),
                  "- Lower it: " + items(dn), ""]
        rl = [x.strip() for x in sval(row.get("responsive_lines")).split(",") if x.strip()]
        if rl:
            idx = {n: i for i, n in enumerate(R.cell)}
            L += ["## Cell lines where it responds most", "",
                  "*The lines with the largest mean |module score| over the module's 8 strongest drug-doses "
                  "(`graph/modules.parquet` responsive_lines, the graph stage's list), strongest first.*", "",
                  "- " + ", ".join(self.llink(idx[n]) if n in idx else cell(n) for n in rl)
                  + " " + self.kofn(len(rl), R.L, self.xmodule(m), "lines")
                  + " The explorer shows the module's score in every line at every drug-dose.", ""]
        if R.novel_members is not None:
            nm = R.novel_members[R.novel_members["module"] == m].sort_values("mean_cos", ascending=False,
                                                                              kind="stable")
            nm = nm.drop_duplicates("col").reset_index(drop=True)
            if len(nm):
                # the alert of validate (a gene in the space only through flagged drug-doses; an older validate
                # stage: from embed evidence_flagged_only), in its ranked place; capped by cap_keep
                def cand_alert(r):
                    t = sval(getattr(r, "alert", "")).lstrip(ALERT).strip()
                    if not t and R.flagged_only[int(r.col)]:
                        t = "in the vector space only through drug-doses that carry an alert"
                    return t.replace(f"{R.sym[int(r.col)]} is in the vector space", "in the vector space")
                recs = list(nm.itertuples(index=False))
                why = [cand_alert(r) for r in recs]
                keep = cap_keep([bool(w) for w in why], N_CANDIDATES)
                n_al = sum(1 for w in why if w)
                extra = max(0, len(keep) - N_CANDIDATES)
                L += ["## Candidate new members", "",
                      "*Members not annotated to the set their arm is enriched for, ranked by mean cos to the "
                      f"annotated members (`validation/novel_members.csv`); {ALERT} = a reason to doubt the gene's "
                      "place (in the vector space only through flagged drug-doses), kept in its rank. "
                      f"{len(recs):,} candidates, {n_alerts(n_al)}"
                      + (f"; shown: the {N_CANDIDATES} strongest" + (f" and the {extra} next strongest without an "
                                                                    "alert" if extra else "")
                         if len(keep) < len(recs) else "") + ".* "
                      + self.kofn(len(keep), len(recs), self.xmodule(m), "candidates"), ""]
                L += table(["#", "Gene", "Set", "Mean cos"] + (["Alert"] if n_al else []),
                           [[str(k + 1), self.glink(recs[k].col) + (f" {ALERT}" if why[k] else ""),
                             recs[k].set_label, fcos(recs[k].mean_cos)]
                            + ([f"{ALERT} {why[k]}" if why[k] else ""] if n_al else []) for k in keep]) + [""]
        n_fo = int(sum(1 for c in mem if R.flagged_only[c]))
        if n_fo:
            L += [f"*{ALERT} {n_fo} of its {len(mem)} genes are in the vector space only through drug-doses that "
                  "carry an alert (`embed/genes.parquet` evidence_flagged_only): their place here may reflect what "
                  "those drug-doses did to the cells. They are marked in the tables of this note.*", ""]
        for arm_name, lst in (("+ arm", plus), ("− arm", minus)):
            L += [f"## {arm_name} ({len(lst)})", ""]
            if not lst:
                L += ["Empty." if opp else "None: a single-armed module.", ""]
                continue
            body = []
            for c in lst:
                nmx = sval(R.ann["name"].iloc[c]) if R.ann is not None else ""
                body.append([self.glink(c), g3(R.axis_proj[c]), nmx or "—"]
                            + ([f"{ALERT} only flagged evidence" if R.flagged_only[c] else ""] if n_fo else []))
            L += table(["Gene", "Projection", "Name"] + (["Alert"] if n_fo else []), body) + [""]
        L += ["## Data", "",
              f"- **Explorer** (every member, every enrichment row, the module's score at every drug-dose and in every "
              f"line): {self.xl(self.xmodule(m))}",
              f"- `graph/nodes.parquet` — module == {m}; `graph/modules.parquet` — module == {m}; "
              f"`graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [{k}] (drug-dose × line)",
              ""]
        return "\n".join(L)

    def module_label_lines(self, m, lab, lr):
        """The label of a module as the validation stage chose it (validate version 7, validation/module_labels.csv),
        part by part: 'Label: {label} ({label_source}{, weak})' with its q only for a gene-set label (else the q would
        be the set's, not the label's), the best gene set when the label is not that set, the drug classes that drive
        it (label_drugs), its lineage, Y-chromosome genes and read-sharing copies, and what it moves with
        (graph/modules.parquet covariate_tag and the cov_*_r values)."""
        R = self.R
        L = []
        src = lab[1] if lab else ""
        if lab and lab[0]:
            weak = _truthy(lr.get("label_weak"))
            setq = src in SET_LABEL_SOURCES
            L.append(f"- Label: **{cell(lab[0])}** ({src or 'top genes'}" + (", weak" if weak else "")
                     + (f"; q {fq(lab[2])}" if setq and _finite(lab[2]) else "") + ")"
                     + (f". Why weak: {cell(sval(lr.get('label_weak_why')))}" if weak and sval(lr.get("label_weak_why"))
                        else "") + ".")
            st = sval(lr.get("set_label"))
            if st and st != lab[0]:
                L.append(f"- Best gene set (not chosen as the label): {cell(st)}"
                         + (f" ({int(lr['label_overlap'])} of {int(lr['label_n_set'])} set genes here; q "
                            f"{fq(lr.get('label_q'))})" if _finite(lr.get("label_overlap"))
                            and _finite(lr.get("label_n_set")) and int(lr["label_n_set"]) > 0 else "") + ".")
            if sval(lr.get("label_drugs")):
                L.append(f"- Driven by: {cell(sval(lr.get('label_drugs')))}.")
        elif R.have_validation:
            L.append("- No gene set, drug class or lineage labels it (`validation/module_labels.csv`).")
        med = lr.get("median_lines_expressing")
        if _finite(med):
            org = sval(lr.get("lineage_organs"))
            L.append(f"- Lineage: its median gene is expressed in {int(round(float(med)))} of {R.L} lines"
                     + (f"; {cell(org)}" if org else "")
                     + (f"; {cell(sval(lr.get('lineage_label')))}" if sval(lr.get("lineage_label")) else "") + ".")
        if sval(lr.get("chrY_genes")):
            L.append(f"- {ALERT} Y-chromosome genes: {cell(sval(lr.get('chrY_genes')))} (expressed only in lines "
                     "from male donors).")
        if sval(lr.get("read_sharing_genes")):
            L.append(f"- {ALERT} Read-sharing copies: {cell(sval(lr.get('read_sharing_genes')))} (reads can be counted "
                     "for either copy).")
        mr = R.modules[R.modules["module"] == int(m)]
        tag = sval(mr["covariate_tag"].iloc[0]) if len(mr) and "covariate_tag" in mr else sval(lr.get("covariate_tag"))
        covs = []
        if len(mr):
            for k_, w_ in COV_WORDS:
                v_ = mr[f"cov_{k_}_r"].iloc[0] if f"cov_{k_}_r" in mr else np.nan
                if _finite(v_):
                    covs.append(f"{w_} {float(v_):+.2f}")
        if tag:
            L.append(f"- Moves with: {cell(re.sub(r'^moves with ', '', tag))} (`graph/modules.parquet` covariate_tag).")
        if covs:
            L.append("- Correlation of its score with technical and cell-cycle measures across drug-doses (r): "
                     + ", ".join(covs) + ". Its genes as a gene set: `graph/modules.gmt`.")
        if L:
            L = ["`validation/module_labels.csv`:", ""] + L + [""]
        return L

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
             f"of them are in no module (module 0); {int((~R.included).sum()):,} genes are not in the vector space."
             + (f" {ALERT} = in the vector space only through significant pooled drug-doses that carry an alert "
                f"({int((R.flagged_only & R.included).sum()):,} genes; `embed/genes.parquet` evidence_flagged_only)."
                if R.has_flagged_only else ""), ""]
        for r in R.modules.itertuples(index=False):
            m = int(r.module)
            mem = np.flatnonzero(R.module == m)
            lab = self.mod_label_text(m)
            L += [f"## {self.mlink(m)}" + (f" — {cell(lab)}" if lab else "") + f" ({len(mem)}"
                  + ("" if R.mod_opp.get(m) else ", single-armed") + ")", ""]
            for a in (("+", "-") if R.mod_opp.get(m) else ("+",)):
                lst = sorted([c for c in mem if R.arm[c] == a], key=lambda c: (-abs(R.axis_proj[c]), c))
                L += [f"- **{a}** ({len(lst)}): " + (", ".join(
                    self.glink(c) + (f" {ALERT}" if R.flagged_only[c] else "") for c in lst) or "—")]
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

    def paths_index(self):
        """vault/.tahoemap-paths.json: the path of every gene, plates, drug, cell-line, module and plate note, relative
        to the vault folder with '/' (note names come from the Names registry, with its collision fallbacks, so they
        cannot be worked out elsewhere): {"gene": {col: path}, "plates": {col: path}, "drug": {name: path}, "line":
        {line: path}, "module": {m: path}, "plate": {plate: path}}. The explorer links each page to its note with it.
        Sorted, so an unchanged run rewrites nothing."""
        R = self.R
        idx = {"generated_by": GEN, "version": VERSION, "root": "vault", "site_url": self.site or "",
               "gene": {str(c): self.gene_path[c] for c in range(R.gK)},
               "plates": {str(c): f"Genes/{R.bucket[c]}/{self.plates_note[c]}.md" for c in range(R.gK)},
               "drug": {d: f"Drugs/{n}.md" for d, n in self.drug_name.items()},
               "line": {str(i): f"Cell lines/{n}.md" for i, n in enumerate(self.line_name)},
               "module": {str(m): f"Modules/{n}.md" for m, n in self.module_name.items()},
               "plate": {str(p): f"Plates/{n}.md" for p, n in self.plate_name.items()}}
        self.W.write(PATHS, json.dumps(idx, ensure_ascii=False, sort_keys=True, indent=0))

    # ------------------------------------------------------------------ Home, How to read, .obsidian
    def home(self):
        R = self.R
        ei = R.embed_info
        n_written = sum(1 for c in range(R.gK) if R.sym[c] in self.fragments)
        stamps = {}
        for s in CM.STAGES[:CM.STAGES.index("validate") + 1]:              # the pipeline's own order
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
             self.top_line(self.site or LOCAL_EXPLORER), "",
             "The explorer is the searchable site of this run: every gene at every drug-dose and in every cell line, "
             "every partner and arrow, every value as stored, nothing left out. A note shows the strongest items of "
             "each list and says how many there are ('k of N shown'), with a link to all of them there.", "",
             f"Run folder: `{self.out}`. Every path quoted in a note is relative to it.", "",
             "| | |", "|---|---|",
             f"| Genes with a note | {R.gK:,} ({n_written} with a written section) |",
             f"| Genes in the vector space | {int(R.included.sum()):,} ({ei.get('dims', '?')} dimensions, "
             f"{fint(ei.get('contexts'))} (drug-dose, line) contexts"
             + (f"; {int((R.flagged_only & R.included).sum()):,} of them only through drug-doses that carry an alert "
                f"{ALERT}" if R.has_flagged_only else "") + ") |",
             f"| Modules | {len(self.module_name)} |",
             f"| Drugs / drug-doses | {len(self.drug_name)} / {R.Dn:,} |",
             f"| Cell lines | {R.L} |", f"| Plates / wells | {len(self.plate_name)} / {R.N:,} |"]
        ti = _read_json(os.path.join(self.out, "tables", "info.json")) or {}
        nb = ((ti.get("neighbour_rule") or {}).get("drugdoses") or {})
        if nb:
            L += ["| Drug-doses like a neighbouring well (`tables/info.json` neighbour_rule) | "
                  + ", ".join(f"{k}: {int(v):,}" for k, v in nb.items()) + f" ({ALERT} only the tier 'artifact') |"]
        tl = ti.get("translation_inhibitors") or {}
        if tl:
            L += [f"| Drug-doses of translation inhibitors (rises there may be mRNA stabilisation) | "
                  f"{fint(tl.get('drugdoses'))} ("
                  + ", ".join(self.dlink(x) for x in sorted(tl.get("members") or {})) + ") |"]
        an = ti.get("annotations") or {}
        if an:
            L += [f"| Drugs whose Tahoe and ChEMBL annotations disagree ({ALERT}; tag `#annotations-disagree`) | "
                  f"{fint(an.get('alerts'))} of {fint(an.get('drugs'))} ({fint(an.get('chembl_matched'))} found in "
                  f"{sval(ti.get('chembl_release')) or 'ChEMBL'}) |"]
        ri = _read_json(os.path.join(self.out, "relations", "info.json")) or {}
        if _finite(ri.get("pairs_total")):
            L += [f"| Gene partners (`relations/`; pairs = distinct gene pairs) | {fint(ri.get('pairs_total'))} pairs, "
                  f"{fint(ri.get('pairs_both_halves'))} with the {REL.SAME_SIGN}"
                  + (f", {fint(ri.get('pairs_lineage'))} lineage pairs" if _finite(ri.get("pairs_lineage")) else "")
                  + (f", {fint(ri.get('pairs_read_sharing'))} read-sharing copies"
                     if _finite(ri.get("pairs_read_sharing")) else "") + " |"]
        if self.dv is not None:
            dc = self.dv.counts()
            L += [f"| Probable direction (arrows SOURCE → TARGET; [[{self.fixed[DIR_NOTE]}]]) | {dc['rows']:,} arrows: "
                  "grade " + ", ".join(f"{g_} {sum(v.get(g_, 0) for v in dc['by_kind'].values()):,}"
                                       for g_ in DV.GRADES)
                  + f"; {dc['with_alert']:,} with an alert {ALERT} |"]
        else:
            L += [f"| Probable direction ([[{self.fixed[DIR_NOTE]}]]) | not computed: the direction stage has not run "
                  "on this output |"]
        if self.lit:
            nk = {k: sum(1 for x in self.lit if x[0] == k) for k in REVIEW_KINDS}
            L += ["| Literature reviews (AI agents; `review/`) | " + ", ".join(
                f"{nk[k]:,} {w if nk[k] == 1 else w + 's'}" for k, w in (("gene", "gene"), ("drug", "drug"),
                                                                        ("line", "cell line")))
                  + " (tag `#literature-review`) |"]
        L += ["",
             "## Start here", "",
             "| If you want | Read |", "|---|---|",
             "| what every section of a note means, and the baseline of every fold change "
             "| [[How to read this vault]] |",
             "| a gene | the quick switcher (Ctrl/Cmd-O), or [[Genes by letter]] |",
             "| the modules of the nodal map | [[Genes by module]] |",
             f"| which gene probably acts on which (from the cell lines; not proof of direct regulation) "
             f"| [[{self.fixed[DIR_NOTE]}]], and a gene note's Direction (probable) |",
             "| a drug | [[Drugs by mechanism]] |", "| a cell line | [[Lines by organ]] |",
             "| why a gene has no note | [[Genes below the detection limit]] |",
             "| a plate's layout and its failed wells | " + ", ".join(f"[[{n}]]" for n in self.plate_name.values())
             + " |", "",
             "## Concepts", "",
             "Written notes (from `tahoemap/vault_seed/notes/`), each explained once:", ""]
        L += ["- " + ", ".join(f"[[{n}]]" for n in sorted(self.seed_notes.values())), "",
              f"Generated from this run: [[{self.fixed[DIR_NOTE]}]] (the direction stage's arrows, their grades, "
              "alerts and controls).", ""]
        if R.have_validation:
            mt = R.metrics
            cs = mt.get("control_sets", {}) or {}
            ml = mt.get("module_labels", {}) or {}
            nv = mt.get("novel", {}) or {}
            L += ["## Validation", "",
                  "From `validation/report.md` (curated control programmes not derived from Tahoe):", "",
                  f"- Control sets: {cs.get('n_sets', '?')} scored; median AUROC (signed cos) "
                  f"{g3(cs.get('median_auroc_cos'))}; {cs.get('n_auroc_cos_ge_0.6', '?')} with AUROC ≥ 0.6.",
                  f"- Modules with a gene-set label: {ml.get('labelled', '?')} of {ml.get('modules', '?')}"
                  + (f" ({fint(ml.get('strong_set'))} strong, {fint(ml.get('weak_set'))} weak); labelled by a driving "
                     f"drug class: {fint(ml.get('drug_class'))}; by a lineage: {fint(ml.get('lineage'))}; by their top "
                     f"genes only: {fint(ml.get('top_genes'))}; with an alert {ALERT}: {fint(ml.get('with_alert'))}"
                     if "strong_set" in ml else "") + ".",
                  ("- Novel candidate relations: " + (f"{fint(nv.get('edges'))} edges" if R.novel_assessed else
                                                       "not assessed (" + (", ".join(R.novel_blocked) or
                                                                           "reference sources") + " missing)")
                   + f"; candidate new set members: {fint(nv.get('member_genes'))} genes."), ""]
            ops = [op for op in (mt.get("opposite_pairs") or []) if _finite(op.get("mean_cross_cos"))]
            for op in ops[:3]:
                L += [f"- Opposite-arm test {op.get('a')} / {op.get('b')}: mean cross-set cos "
                      f"{fcos(op.get('mean_cross_cos'))} (expect < 0); share of cross pairs in one module "
                      f"{g3(op.get('share_same_module'))} (random pairs {g3(op.get('random_same_module'))})."]
            if len(ops) > 3:
                L += [f"- (3 of {len(ops)} opposite-arm tests shown; all {len(ops)}: `validation/report.md` and "
                      "`validation/opposite_pairs.csv`)"]
            if ops:
                L += [""]
        L += ["## Largest modules", ""]
        n_mod = len(R.modules)
        top = R.modules.sort_values(["n_genes", "module"], ascending=[False, True]).head(HOME_MODULES)

        def arm(txt, n_arm):
            """The arm's first ARM_NAMES genes (the strongest; ⚠ marks kept), and '(k of N)' when the arm has more."""
            names = [x for x in sval(txt).split(", ") if x]
            k = min(ARM_NAMES, len(names))
            n_arm = int(n_arm) if _finite(n_arm) else len(names)
            return ", ".join(names[:k]) + (f" … ({k} of {n_arm:,}; all in the module note)" if n_arm > k else "")
        L += table(["Module", "Label", "Genes", "+ arm (strongest)", "− arm (strongest)"],
                   [[self.mlink(int(r.module)), self.mod_label_text(int(r.module)) or "—", int(r.n_genes),
                     arm(r.top_plus, getattr(r, "n_plus", np.nan)), arm(r.top_minus, getattr(r, "n_minus", np.nan))]
                    for r in top.itertuples(index=False)])
        if n_mod > len(top):
            L += ["", f"({len(top)} of {n_mod:,} modules shown, the largest; all {n_mod:,}: [[Genes by module]] and "
                      f"the explorer: {self.xl(self.xu(LK.browse, 'modules'))})"]
        L += [""]
        L += ["## The run", "", "Stage stamps (`stages/*.json`):", ""]
        L += [f"- {k}: {v}" for k, v in stamps.items()] + [""]
        src = (R.sources or {}).get("sources") or {}
        if src:
            L += ["Registry downloads (`reference/sources.json`):", ""]
            L += [f"- {k}: " + ", ".join(x for x in (sval(v.get("status")), sval(v.get("date"))[:10],
                                                      f"{fint(v.get('n_rows'))} rows" if _finite(v.get("n_rows"))
                                                      else "", _short_error(cell(sval(v.get("error"))))) if x)
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
        txt = HOW_TO_READ.format(q=Q_CUT, n_drugs=N_DRUGS, n_part=N_PARTNERS, n_pred=N_PRED,
                                 line_z=R.line_z, fold=f"{R.line_fold:.3g}", line_cut=line_cut, short=SHORT_POOLED,
                                 amb_frac=R.amb_frac, e_min=R.e_min, repro_fdr=REPRO_FDR, repro_min=REL.REPRO_MIN,
                                 one_half=REL.ONE_HALF, novel_fdr=REL.NOVEL_FDR, novel_cos=REL.NOVEL_COS,
                                 novel_status=novel_status, arm_min=ARM_MIN, arms_opp=ARMS_OPPOSITE,
                                 n_old=self.n_old_study, cc_safety=R.cc_safety,
                                 cc_max_pct=f"{100 * R.cc_max:g}%" if R.cc_max != 0.5 else "half",
                                 artifacts=", ".join(f"`{a}`" for a in CM.ARTIFACT_FLAGS), n_dir=N_DIRECTION,
                                 dir_note=self.fixed[DIR_NOTE])
        txt = txt.rstrip("\n") + "\n\n" + "\n".join(words_section()) + "\n"
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
                replace_file(tmp, p)
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
                           '-file:"Home" -file:"How to read this vault" -file:"Probable direction"',
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
                           "n_dd_up": "number", "n_dd_down": "number", "direction_upstream": "number",
                           "direction_downstream": "number",
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
        self.load_direction()
        self.write_concepts()
        self.direction_note()
        self.gene_notes()
        self.drug_notes()
        self.line_notes()
        self.plate_notes()
        self.module_notes()
        self.index_notes()
        self.home()
        self.how_to_read()
        self.paths_index()
        # every basename unique, case-insensitively (Obsidian resolves links by basename)
        seen = {}
        for p in self.W.paths:
            b = os.path.splitext(os.path.basename(p))[0].lower() + os.path.splitext(p)[1]
            assert b not in seen, f"two notes share the basename {b}: {seen[b]} and {p}"
            seen[b] = p
        removed = _clean_stale(self.root, self.W.paths, old_manifest)
        self.obsidian()
        files = sorted(_rel_posix(p, self.root) for p in self.W.paths)
        tmp = mp + ".tmp"
        with open(tmp, "w", encoding="utf-8") as fh:
            json.dump({"generated_by": GEN, "version": VERSION, "files": files}, fh, indent=0)
        replace_file(tmp, mp)
        gs = np.array(self.gene_sizes)
        ps = np.array(self.plates_sizes)
        info = {"version": VERSION, "notes": len(files), "gene_notes": self.R.gK, "drug_notes": len(self.drug_name),
                "line_notes": self.R.L, "plate_notes": len(self.plate_name), "module_notes": len(self.module_name),
                "concept_notes": len(self.seed_notes), "fragments_spliced": self.n_fragments,
                "fragments_marked_earlier_study": self.n_old_study,
                "fragments_available": len(self.fragments), "written": self.W.n_written,
                "literature_notes": self.n_lit_notes, "literature_partner_cells": self.n_lit_cells,
                "direction_arrows": len(self.dv.rows) if self.dv is not None else None,
                "review": self.lit_fp, "site_url": self.site or "", "paths_index": PATHS,
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

## The explorer: every list in full

A note shows the strongest items of each list. Every note of a gene, drug, cell line or module starts with a line
"Explorer: ... · Map: ...": the explorer is the searchable site of this run, and it shows everything - every gene at
every drug-dose (the exact corrected fold, z and q, flagged or not), every cell line at every drug-dose, every
partner, every arrow with every reason in full, the wells. Every list a note cuts ends with "(k of N shown; all N in
the explorer: ...)". Nothing is left out because of a flag: a flagged item keeps its place with an alert (⚠).

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
- **Clean** — no artifact flag on the drug-dose for this gene (a `cell-cycle shift` counts only where it explains
  the gene's change, see below), and none of the gene's own ("position correction uncertain"). Artifact flags:
  {artifacts}. They mark changes that may come from cell death, a global drop in transcription, a
  shift in the cell-cycle mix, a plate that does not reproduce, or a well-position problem — not regulation of the
  gene. Soft caveats that do **not** make a value unclean: `low cells (technical?)`, `plate-row cell shift`,
  `composition shift`, `noisy plate (z scaled)`, `position effect removed`. The exact definitions are in
  `docs/method.md` of the tahoemap repository.
- **Flagged, and the alert ⚠** — nothing is left out of a list, a table or a count because of a flag. A drug-dose
  (or a partner, a well, a single-line cell) that carries a reason for doubt stays in its ranked place and is marked
  **⚠** followed by the reason in plain words, e.g. `⚠ toxic; transcription drop` or `⚠ cell-cycle shift, explains
  ~60% of this change`. Read such a row as "something may have happened to the cells", not as regulation of the
  gene; but read it: a strong, reproducible change at a flagged drug-dose can be real. Counts say how many there are
  in all and how many carry an alert. A list capped at N shows the N strongest and also any of the N strongest
  without an alert that rank below them, all in one order, so flagged rows never push unflagged ones out of view.
  Where an estimate leaves technically broken data out (e.g. cell counts of drug-doses whose wells disagree), the
  note says so next to the number.
- **The cell-cycle shift, gene by gene** — `cell-cycle shift` is a flag of the drug-dose: its cells moved into or
  out of S or G2/M (the S-phase and G2/M modules' pooled change). A gene's change at such a drug-dose may then only
  reflect the new mix of phases — for genes that go with the cell cycle. The tables stage measures how much a gene
  goes with it: its slopes on the two modules, fitted over the drug-doses without another artifact flag
  (`cc_slope_S` / `cc_slope_G2M` in `tables/genes.parquet`), and per row the share of the gene's change that the
  drug-dose's shift would explain with those slopes (`cc_share` in `tables/drug_effects.parquet`; 0 when the
  predicted part goes the other way, at most 1). Fitted slopes are attenuated by noise, so the rule multiplies them
  by {cc_safety:g}. **`cell-cycle shift (explains ~N% here)`** means: the drug-dose's shift explains only about N%
  of this gene's change, and even with the gene's fitted cycle slopes multiplied by {cc_safety:g} it would explain
  less than {cc_max_pct}, with a change of at least 1.2× left over. For this gene the shift is then **no artifact**:
  the row is clean and carries no alert (the token stays in its caveats). Where the shift may be the explanation
  the plain artifact flag stays, and the alert says how much it explains: `⚠ cell-cycle shift, explains ~60% of
  this change`. Tables from an older tables stage have no such share: there every row of a `cell-cycle shift`
  drug-dose carries the plain alert.

## A gene note, section by section

- **Frontmatter** — symbol, Ensembl id, registry name and cytoband, module and arm, pooled level (CPM),
  lines expressing it, drug-doses raising / lowering it significantly (`n_dd_up` / `n_dd_down`, all of them;
  `n_dd_up_clean` / `n_dd_down_clean`, those without an alert), whether it is in the vector space (tag
  `evidence-flagged-only` when it is there only through significant drug-doses that carry an alert).
- **Title, name, location**, then the **written section** when someone has written one.
- **At a glance** — a generated "In this data" callout: how many drug-doses raise and lower it significantly pooled
  over the cell lines (median; q < {q:.2f} and at least 1.2×), how many of them carry an alert, how many the list
  below holds (|z| ≥ 3 or q < {q:.2f}: a wider rule, so the list is longer than the count), and the strongest (fold,
  z, q, in how many of the
  measured lines it moves) with its alert — and, when that one carries an alert, the strongest without one; when
  fewer than {short} drug-doses without an alert are significant pooled, an "In single lines" sentence names the
  drug-doses that pass the per-line cut in the most lines (`tables/drug_line_top.parquet`), with their alerts; its
  strongest partners by |cos| with each partner's fdr, ⚠ marking those without the same sign in both halves of the
  compounds (evidence other than `both halves`, i.e. not the same sign with fdr ≤ {repro_fdr:.2f} in two random
  halves of the compounds); its
  module and arm. A gene that is in the vector space only through significant drug-doses that carry an alert says
  so here, with ⚠. (The "In one line" callout above it, when there is one, is the written layer.)
- **Drugs that raise it / lower it** — pooled over the cell lines (median): one ranked list per direction over every
  drug-dose with |z| ≥ 3 or q < {q:.2f}, flagged ones included, strongest first: the {n_drugs} strongest, and any of
  the {n_drugs} strongest without an alert that rank below them. *Alert* = ⚠ and the artifact flags in plain words
  (see above); *Caveats* = the soft caveats. Bold fold = significant. *vs DMSO (rough)* = the same change against
  the plate's two DMSO wells (see Words below). *Lines up / measured* = lines where that
  drug-dose moves it ≥ 1.2× at per-line z ≥ 2, out of the lines measured for it (see above) with enough cells,
  followed by the number of wells (`· one well`: all the lines sit in one well, so they are not replicate
  treatments); the first names are the strongest. This count is descriptive (per-line z ≥ 2 is not a significance
  cut). *Pattern over the doses (each on its own plate)* = how the effect behaves across the drug's doses (rises with
  dose, top dose only, all doses, single dose, inconsistent); each dose sits on its own plate, so the pattern compares
  plates as much as doses ("(doses share a plate)" where they do not). Under the table, the words of any
  neighbouring-well or translation-inhibitor flag in it, and the wells. When a listed row carries
  `cell-cycle shift`, a line under the lists gives the gene's fitted
  cell-cycle slopes. (There is no separate "flagged" section: flagged drug-doses are in these lists.)
- **In which cell lines** — one row per line: TP53 status (alt = altered; not rec. = not recorded: presumed wild
  type, not confirmed), the line's own level (CPM; "n.m." = not measured, see
  above), how many drug-doses move it ≥ {fold}× at per-line |z| ≥ {line_z:.2f} in that line (with the number that
  carry an alert in brackets; tables from an older tables stage count only clean drug-doses, and the note says so),
  and the strongest of them up and down with its alert and caveats, then the strongest without an artifact flag when
  that is another drug-dose, with its caveats (a caveat is no artifact flag: e.g. `rise under a translation
  inhibitor`, read from that line's own change, or a neighbouring well at the drug's top dose). {line_cut}
- **Genes that move with it / opposite** — its strongest partners each way, from the gene's 100 nearest by |cos|.
  *cos* = signed cosine of the two gene vectors = the correlation of their denoised responses over every
  (drug-dose, cell line) context (+1 always together, −1 always opposite). *Halves* = the same cosine in two vector
  spaces fitted on two random halves of the compounds (a hash split of the compound names; drug families fall in
  both); *evidence* = `both halves` (the same sign in the full space and in both halves, |cos| ≥ {repro_min:g} in
  each, **and** fdr ≤ {repro_fdr:.2f}), `⚠ one half` (strong, |cos| ≥ {one_half:g}, in one of the two random halves
  only: not the same sign in both, no error estimate; often one compound), `⚠ not reproduced`. Other alerts:
  `⚠ lineage pair` and `⚠ read-sharing copies` (see Words below), `⚠ same locus` /
  `⚠ readthrough risk` (neighbours on the genome), and ⚠ after the partner's name = the partner is in the vector space
  only through drug-doses that carry an alert. The tables show the {n_part} strongest per side and any of the
  {n_part} strongest without an alert below them; a partner with an alert keeps its place with it. *fdr* = the
  estimated share of false relations among pairs at least this strong in both halves, from sign concordance between
  the halves (see
  [[FDR calibration and the inflated null]]). *Notes*: known links (shared HGNC gene group, shared Hallmark/Reactome
  pathway, STRING score), **novel candidate** (both halves, fdr ≤ {novel_fdr:.2f}, |cos| ≥ {novel_cos:g}, no known
  link, not the same locus, both genes described by HGNC and placed on the genome; assessed only when HGNC, Ensembl,
  STRING and Hallmark or Reactome all loaded{novel_status}), same locus (≤ 50 kb) and **readthrough risk** (same
  strand, ≤ 20 kb, the 5′ gene ≥ 8×
  more expressed: the 3′ gene's counts can be the 5′ gene's transcription, marked ⚠; see
  [[Readthrough spillover]]). A
  relation is a correlation across drugs and lines; it is never evidence that one gene regulates the other.
- **Direction (probable)** — the arrows of the direction stage (`direction/`): **upstream of this gene**, the arrows
  whose target it is, and **downstream of this gene**, the arrows whose source it is (to another gene, or to the
  cells under a drug-dose). Each arrow names its source or target (linked), its grade (A strong, B read its alerts,
  C a glimpse), what the source's activity does (raises, lowers, or not inferred), the evidence (a recorded mutation
  and the lines on each side, lines that do not express the source, compounds that target it, or its natural level
  across the lines), the size of the effect, q, and its alerts (⚠ and a short label per reason; every reason in full
  is in `direction/edges.parquet`). Each list shows the {n_dir} strongest and any of the {n_dir} strongest without an
  alert beyond them, and says how many more there are. An arrow is a **probable** direction, from the screen's cell
  lines: not proof of direct regulation (A → B → C looks like A → C). Kinds, grades, sign, alerts and this run's
  controls: [[{dir_note}]]. When the gene has arrows, At a glance says so in one sentence.
- **Where it sits** — its module and arm, its positions on the two maps, the length of its vector, and the {n_pred}
  drug-doses whose vectors **predict** the largest rise and fall of the gene (gene vector · drug-dose vector, in z
  units), with the {n_pred} strongest predictions among drug-doses without an artifact flag (⚠ = the drug-dose, or
  the gene at it, carries one), next to the **observed** z. Agreement means the gene follows the programme it shares
  with its partners; a gap means it departs from it for that drug.
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

- **Drug** — its two annotations (Tahoe's and ChEMBL's, side by side, ⚠ where they disagree) and its mechanism
  classes with their sources; doses (plate and well, significant genes, replicate agreement, cell loss, cell-cycle
  and proteasome module z, flags with ⚠ before the artifact flags); notes per dose (a neighbouring well, an unexpected
  similarity to another class, the lines that respond out of proportion); the 10 most similar drug-doses of its best
  dose (of 50); the genes each dose raises and lowers (every significant gene counts;
  those with an alert are marked, a bare ⚠ standing for the dose's own alert named after the dose), the modules it
  moves, the lines it depletes and the lines that respond most, the nearest drugs in the vector space, and (Direction
  (probable)) the genes that set how the cells fare under it and the drug-target arrows of its compound classes.
- **Cell line** — organ, TP53 status, drivers, the drug-doses that deplete it, how strongly it responds (both over
  all drug-doses, flagged ones marked ⚠), the drug-doses where it responds out of proportion (selective), the genes
  it moves most, the genes it has unusually high or lacks, and the
  programmes that do not respond in it; and (Direction (probable)) its recorded alterations as the direction stage
  grouped them, and the genes it does not express that served as natural knockouts, with the arrows each gave.
- **Plate** — dose, reliability, plate factor, DMSO and failed wells, an 8 × 12 layout and a 96-row well table
  (wells on an unreliable plate, without a position correction, not used in their drug-dose or failed are marked ⚠).
- **Module** — label from the validation stage (its source, weak or not, the drug class that drives it, its
  lineage, and its alerts under the title), what it moves with (technical and cell-cycle measures), enrichment, the
  drugs that raise or lower it (flagged ones marked ⚠), the lines where it responds most, candidate new members, and
  every member by arm.

## Conventions

- Wikilinks are note names; drugs end in "(drug)", cell lines in "(line)".
- "Upstream" and "downstream" are regulatory words; chromosomal position is "5′ of" / "3′ of".
- A number in a note is read from the table named next to it, or is a simple function of it named with it (CPM =
  counts ÷ total × 10⁶, a predicted z = a dot product, a level ratio); nothing is re-estimated by the vault.
- The global graph view starts filtered: no indexes, Plate notes, plates notes or cell lines (every gene note links
  every line, so lines would pull all genes into one ball); change the filter in the graph settings to see them.
  Plates notes are excluded from search and the quick switcher (Settings → Files and links → Excluded files); open
  them from a gene note.
"""


def words_section():
    """'## Words used in the notes' of How to read this vault: one short entry per word the notes use for the newer
    readings (the flag tokens with common.FLAG_TEXT; the tables, relations, embed, validate and direction stages'
    readings, in their own words where a stage defines them)."""
    W = ["## Words used in the notes", "",
         f"- **q `{CM.Q_ZERO}`** — a q stored as 0: {CM.Q_ZERO_TEXT}.",
         "- **vs the typical drug well, not DMSO** — every fold change, z and q of a note compares a drug well with "
         "the "
         "typical drug well of the same plate and line (see The baseline of every fold change).",
         "- **vs DMSO (rough)** — the same change against the plate's two DMSO wells (`tables/drug_effects.parquet` "
         f"lfc_vs_dmso): {getattr(TB, 'DMSO_DOC', 'a sign check, not a replacement')}. `· other sign against DMSO` "
         "marks a row whose DMSO-referenced change is at least 1.2× the other way; `no DMSO value` = the plate has "
         "none. Read such a row with care, not as a wrong value: two DMSO wells are a small reference.",
         f"- **Pattern over the doses (each on its own plate)** — {getattr(TB, 'DOSE_PLATE', '')} \"(doses share a "
         "plate)\" marks a drug whose doses do share one.",
         f"- **One well** (`· one well`, `· 2 wells`) — {getattr(TB, 'ONE_WELL', '')}",
         "- **Flag words** — the drug-dose and gene flags of the tables stage (the flags of record). The two that "
         "concern a neighbouring well and the two that concern a translation inhibitor:"]
    for t, txt in CM.FLAG_TEXT.items():
        W.append(f"  - `{t}`" + (f" ({ALERT} an artifact flag)" if t in CM.ARTIFACT_FLAGS else " (a caveat)")
                 + f": {txt}")
    W += [
        "- **Neighbouring wells** — the tables stage compares each drug-dose with the wells next to it on its plate. "
        "Tier `artifact`: most of its significant genes move the same way, more strongly, in a neighbouring well of "
        f"another compound, and its higher doses do not move them: {ALERT} on the genes the neighbour moves "
        "(`like a neighbouring well`), not on the others (`... (not this gene)`). Tier `top dose`: the same at a "
        "drug's top dose, where no higher dose can tell (a caveat; its alert gives the rate at which pairs 3 or more "
        "wells apart pass the same test). Tier `same mechanism`: the two compounds share a mechanism, so a shared "
        "signature is expected (a note). Tier `dose response`: at the top dose, but the drug's lower doses already "
        "move its strongest shared genes the same way, so its own effect grows with the dose (a note). A drug note "
        "names the neighbour and the wells.",
        "- **Annotations (Tahoe and ChEMBL)** — a drug note shows Tahoe's own annotation (targets, mechanism) "
        "verbatim and ChEMBL's curated mechanisms and targets next to it, with the ChEMBL release and how the "
        f"molecule was matched. {ALERT} where they disagree; neither overwrites the other.",
        "- **Class** — a drug's mechanism class (`tahoemap/data/drug_classes.json`: for example TOP2 poison, "
        "glucocorticoid receptor agonist, translation inhibitor), each with its source: a code constant with its "
        "citation, a ChEMBL mechanism, or a WHO ATC code via ChEMBL. Tahoe's own annotation is never a class rule.",
        "- **Poison classes** — TOP1 and TOP2 poisons, PARP trappers and microtubule stabilisers do not simply "
        "inhibit their target: they trap it (on DNA, or on the microtubule) and cause damage. A drug-target arrow of "
        "such a class follows the damage, so the sign of the target's own effect is not inferred.",
        "- **Response strength and selective lines** — per drug-dose and line (`tables/drug_line_response.parquet`): "
        "response strength = the slope of the line's changes on the drug-dose's consensus (1 = a typical line); a "
        "line is selective when it moves many more genes beyond the per-line cut than the other lines (sel_z ≥ 3 "
        "and ≥ 20 genes): it responds out of proportion.",
        f"- **Same sign in both halves of the compounds** (`both halves`) — {REL.SAME_SIGN_NOTE}.",
        "- **Lineage pair** — both genes are expressed in few lines, mostly the same: such genes move together "
        "whatever their regulation. The note gives the lines of each, their overlap (J) and how often random "
        "lineage pairs reach the same |cos| (lineage p).",
        "- **Read-sharing copies** — paralogues, a pseudogene and its parent, or a read-through transcript: reads can "
        "be counted for either gene, so the two can move together for that reason alone.",
        "- **Same locus** (direction) — two genes within 1 Mb are deleted or gained together, so an arrow between "
        "them can be a shared deletion, not regulation: which acts on which cannot be told.",
        "- **Programme (direction not identifiable)** — the lines lacking a gene overlap the lines lacking many other "
        "genes (an expression programme): any gene of it, or the lineage, can be the cause, so the direction is not "
        "identifiable.",
        "- **false (group)** — in a direction table, the share of the arrows of its comparison group that may be false "
        "(from random comparison groups, with the 95% upper bound); for genes that some lines do not express, the "
        "share random genes would give (non-specific).",
        "- **TP53 not recorded** — no TP53 alteration in Tahoe's cell-line metadata: presumed wild type, not "
        "confirmed (`not rec.` in a table).",
        "- **Module label** — the validation stage's label: a gene set (strong, or weak: a small overlap or a q above "
        "0.01), else the drug class that drives the module, else a lineage, else its top genes; its alerts (lineage-"
        "restricted, read-sharing copies, Y-chromosome genes) stand under the module note's title.", ""]
    return W


LIT_HOWTO = """## What the literature says (AI-agent reviews)

A gene, drug or cell line tagged `#literature-review` has a section **What the literature says**, written by an AI
agent (tahoemap's literature-review agents, `tahoe review`; see `docs/review.md` of the tahoemap repository). The
agent read the entity's dossier (what this run's data say about it), searched PubMed, Europe PMC and the web, read
abstracts, and reported what is established, what in the data is unexpected, which expected connections are missing
and what is contradicted. The callout at the top of the section names the agent, the model, the date and the
verification: how many cited PMIDs / DOIs were looked up, removed as not found, or could not be looked up (a service
down), and whether a second agent, the citation checker, compared each claim with the abstracts it cites (supported
/ partly / not supported / not checkable) or why it did not. It also links the run's full history (every request,
response and tool call) and the review as data; both are in the run folder (`review/`), outside the vault. The
agent's text is shown without HTML, images or links other than to PubMed, doi.org, Europe PMC, NCBI and Cellosaurus;
the line under it, on what was checked, is generated from the verification, not written by the agent.

In a gene note the partner tables then have a **Literature** column: the agent's verdict on that pair (established,
indirect, plausible, unexpected or contradicted) with its check in brackets and its citations, from
`review/connections.parquet`; a verdict from the partner's review is marked with the partner's name. A verdict the
citation checker found not supported, or whose papers do not exist, reads **unverified**. A verdict that cites a
retracted paper says "(cites a retracted paper)" (the paper is marked "(retracted)"): a retracted paper is no
support, so a verdict whose only papers are retracted reads **unverified** too. When a review gave one partner
several verdicts, the strongest verified one is shown (else its first), here and in the map. The reviews are
leads, not established facts: no person has checked them. A new review replaces the section at the next `tahoe
vault` (or `tahoe run`).
"""


def run(out, site_url=None, **_):
    """Build OUT/vault/ from the run's tables (see the module docstring). site_url: the explorer's site URL the notes
    link to (None: links.site_url_default of the code checkout; '' or 'none': no site, the notes then name the run
    folder's explorer/web/index.html)."""
    t0 = time.time()
    warnings.filterwarnings("ignore", category=RuntimeWarning)
    folder(out, "vault")
    log("Vault: building the Obsidian vault")
    with np.errstate(all="ignore"):
        info = Vault(out, site_url=site_url).build()
    info["minutes"] = round((time.time() - t0) / 60, 2)
    stamp_stage(out, "vault", VERSION, info)
    log(f"Vault done: {info['notes']:,} notes ({info['mb']} MB; gene notes median {info['gene_note_kb_median']} KB, "
        f"max {info['gene_note_kb_max']} KB; plates notes max {info['plates_note_kb_max']} KB), "
        f"{info['fragments_spliced']} written gene sections spliced ({info['fragments_available']} fragments), "
        + (f"{info['literature_notes']} literature reviews spliced ({info['literature_partner_cells']} partner-table "
           "verdicts), " if info.get("literature_notes") else "")
        + f"{info['stale_removed']} stale notes removed ({info['minutes']} min)")
    return info
