#!/usr/bin/env python3
r"""
tahoe_gene_panel.py - the MTAP / Gankyrin trial (tahoe_mtap_gankyrin.py) generalized to a gene panel: ferroptosis,
pyroptosis and p53 genes plus NAPEPLD (NAPE-PLD) and TRIM72 (MG53), with the same artifact corrections, cross-linked
to the earlier MTAP / Gankyrin run, and one Claude agent per pathway that writes a report.

Put this file next to the CURRENT tahoe_mtap_gankyrin.py and tahoe_atlas.py (copy them over older versions: the
method is v3 now, see README 'Method v3') in your Tahoe-100M folder and run from there:

    python3 tahoe_gene_panel.py check      # preflight: data, panel genes, disk, memory, earlier run, agents
    python3 tahoe_gene_panel.py all        # extract + analyze + bundle (start here; ~1 h, mostly reading cells)
    python3 tahoe_gene_panel.py extract    # one pass over the ~96M cells: ~115 genes per cell (resumable)
    python3 tahoe_gene_panel.py analyze    # corrected analyses -> gene_panel/results/summary.txt (minutes)
    python3 tahoe_gene_panel.py bundle     # gene_panel_bundle.zip: upload it to Claude to check the numbers
    python3 tahoe_gene_panel.py agents     # one agent per pathway writes a report (needs ANTHROPIC_API_KEY)

Quick trial on a few files first:   python3 tahoe_gene_panel.py all --limit-files 30 --out panel_trial
Long run that survives logout:      nohup python3 tahoe_gene_panel.py all > /dev/null 2>&1 &
                                    then: tail -f gene_panel/gene_panel.log
On Windows (PowerShell; leave the window open, no nohup):
                                    C:\tahoe\.venv\Scripts\python.exe tahoe_gene_panel.py all
                                    log: Get-Content gene_panel\gene_panel.log -Wait
Every run appends to gene_panel/gene_panel.log (the agents to gene_panel/agents.log) and keeps the computer from
sleeping while it runs. Rerunning analyze moves the earlier results to gene_panel/results/previous_run/ and makes
every agent report out of date (to remake a bundle, use 'bundle', not 'all').

The earlier MTAP / Gankyrin output (<data>/mtap_gankyrin) is read when present (--prior DIR; --prior none ignores
it); the computed atlas (<data>/atlas; --atlas DIR or none) supplies the composition shift, the plate factors and
'wells disagree' once its effects are method v3; --unreliable-plates LIST|none (default plate13).
Extra genes: --genes "SYM[:pathway],..." (aliases FSP1, DFNA5, ASC, MG53, NAPE-PLD, P21, PUMA, NOXA accepted), into a
NEW --out: per-cell files of an earlier gene list are never mixed with a new one.
Same corrections as tahoe_mtap_gankyrin.py (method v3): plate baseline = median of the plate's drug wells (never
DMSO); composition shift from the atlas (<data>/atlas or --atlas; effects computed with method v3); two-pass
leave-drug-out well-position correction (clean donors only); robust z against the drug wells of the reliable plates,
divided by the plate x dose factor (the atlas's, else fitted over the panel's genes); unreliable plates
(--unreliable-plates, default plate13) left out of every drug-dose that has another well; Stouffer over plates; BH
FDR; failed wells removed; lines that do not express a gene left out for that gene; growth z with counting noise;
the v3 artifact flags on every drug-dose.
Agents (same options as tahoe_atlas.py): --model sonnet|opus --budget 5 (USD cap per agent) --max-turns 80
--parallel 3 --angles ferroptosis,p53 --dry-run --redo --skip-overview --web --sandbox (Linux/macOS only).
Requires numpy, pandas, pyarrow (claude-agent-sdk and tahoe_atlas.py for the agents step).
"""

import argparse
import glob
import json
import math
import os
import re
import shlex
import shutil
import sys
import time
import traceback
import warnings
import zipfile
from concurrent.futures import ThreadPoolExecutor

import numpy as np
import pandas as pd
import pyarrow.compute as pc
import pyarrow.parquet as pq

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)
try:
    import tahoe_mtap_gankyrin as T
except ImportError:
    sys.exit("tahoe_gene_panel.py needs tahoe_mtap_gankyrin.py in the same folder")
OLD_COPY = "{f} next to tahoe_gene_panel.py is an older version: copy the current one over it{why}"
PANEL_METHOD = 3          # results/run_info.json method_version; needs tahoe_mtap_gankyrin.METHOD_VERSION >= this
if not all(hasattr(T, f) for f in ("safe_console", "start_run_log", "keep_awake", "py_cmd", "log_exit", "disk_kind",
                                    "REDUCE_EVERY", "REINDEX_HINT", "data_parquets", "Method", "flag_rows")) \
        or getattr(T, "METHOD_VERSION", 0) < PANEL_METHOD:
    sys.exit(OLD_COPY.format(f="tahoe_mtap_gankyrin.py", why=f" (the gene panel needs method v{PANEL_METHOD}; the "
                                                          "earlier mtap_gankyrin/ output may stay: it is compared, "
                                                          "not reused)"))

log = T.log

# ----------------------------------------------------------------------------- settings
PANEL = [  # (gene, pathway, role): the user's list
    ("PTGS2", "ferroptosis", "Most consistent transcriptional marker of ferroptosis"),
    ("CHAC1", "ferroptosis", "ATF4-driven stress response, glutathione degradation"),
    ("SLC7A11", "ferroptosis", "Cystine import, system xc- subunit"),
    ("GPX4", "ferroptosis", "Central lipid peroxide detox enzyme"),
    ("ACSL4", "ferroptosis", "Determines PUFA-phospholipid content; sensitivity marker"),
    ("LPCAT3", "ferroptosis", "Works with ACSL4 on lipid remodeling"),
    ("AIFM2", "ferroptosis", "(FSP1) GPX4-independent protection"),
    ("NFE2L2", "ferroptosis", "Master antioxidant TF, drives resistance"),
    ("HMOX1", "ferroptosis", "NRF2 target; high levels can drive iron release"),
    ("TFRC", "ferroptosis", "Iron import"),
    ("FTH1", "ferroptosis", "Iron storage (FTH1 / FTL)"),
    ("FTL", "ferroptosis", "Iron storage (FTH1 / FTL)"),
    ("NCOA4", "ferroptosis", "Ferritinophagy receptor"),
    ("GSDMD", "pyroptosis", "Canonical pore-forming executioner"),
    ("GSDME", "pyroptosis", "Caspase-3-cleaved; key in chemo-induced pyroptosis"),
    ("NLRP3", "pyroptosis", "Inflammasome sensor"),
    ("AIM2", "pyroptosis", "DNA-sensing inflammasome"),
    ("PYCARD", "pyroptosis", "(ASC) Inflammasome adaptor"),
    ("CASP1", "pyroptosis", "Canonical inflammasome caspase"),
    ("CASP4", "pyroptosis", "Non-canonical, LPS-sensing (CASP4 / CASP5)"),
    ("CASP5", "pyroptosis", "Non-canonical, LPS-sensing (CASP4 / CASP5)"),
    ("CASP3", "pyroptosis", "Pyroptosis / apoptosis: links apoptosis to GSDME cleavage"),
    ("IL1B", "pyroptosis", "Inflammasome output cytokine"),
    ("IL18", "pyroptosis", "Inflammasome output cytokine"),
    ("TP53", "p53", "The gene itself; mutation status matters more than level"),
    ("CDKN1A", "p53", "(p21) Sensitive p53 reporter; also induced without p53 (HDAC inhibitors)"),
    ("MDM2", "p53", "Negative feedback loop"),
    ("BBC3", "p53", "(PUMA) Pro-apoptotic effector"),
    ("PMAIP1", "p53", "(NOXA) Pro-apoptotic effector"),
    ("BAX", "p53", "Apoptosis execution"),
    ("GADD45A", "p53", "DNA-damage response"),
    ("SESN1", "p53", "Antioxidant, mTOR suppression (SESN1 / SESN2)"),
    ("SESN2", "p53", "Antioxidant, mTOR suppression (SESN1 / SESN2)"),
    ("FDXR", "p53", "Highly specific p53 reporter"),
    ("ZMAT3", "p53", "Specific, less context-dependent target"),
    ("NAPEPLD", "additional", "(NAPE-PLD) N-acyl phosphatidylethanolamine phospholipase D: makes anandamide and "
                              "other N-acylethanolamines"),
    ("TRIM72", "additional", "(MG53) Membrane-repair E3 ligase (also IRS1 ubiquitination); muscle/heart-enriched, "
                             "may be absent in cancer lines"),
]
ANCHORS = list(T.TARGET_GENES)   # MTAP, PSMD10 (Gankyrin), CDKN2A, CDKN2B: the earlier analysis, extracted again
ANCHOR_ROLES = {"MTAP": "Methionine salvage; co-deleted with CDKN2A at 9p21 (earlier analysis)",
                "PSMD10": "(Gankyrin) 19S proteasome assembly chaperone; oncoprotein reported to bind RB and CDK4 "
                          "and to promote MDM2-mediated p53 degradation (earlier analysis)",
                "CDKN2A": "p16INK4a / p14ARF (one mRNA; ARF restrains MDM2 mainly after oncogene signalling); 9p21 "
                          "neighbour of MTAP",
                "CDKN2B": "p15INK4b; 9p21 neighbour of MTAP"}
AKA = {"AIFM2": "FSP1", "GSDME": "DFNA5", "PYCARD": "ASC", "TRIM72": "MG53", "NAPEPLD": "NAPE-PLD", "CDKN1A": "p21",
       "BBC3": "PUMA", "PMAIP1": "NOXA", "PSMD10": "Gankyrin"}
ALIASES = {"FSP1": "AIFM2", "DFNA5": "GSDME", "ASC": "PYCARD", "MG53": "TRIM72", "NAPE-PLD": "NAPEPLD",
           "P21": "CDKN1A", "PUMA": "BBC3", "NOXA": "PMAIP1", "GANKYRIN": "PSMD10"}
CONTEXT = {  # context gene sets (no panel gene inside); each gene is extracted as its own column
    "P53_EXT": "TP53I3 RRM2B AEN DDB2 XPC TNFRSF10B PHLDA3 SPATA18 TRIAP1 RPS27L ACER2 TP53INP1 PLK3 POLH EDA2R "
               "CCNG1 BTG2 TIGAR".split(),
    "NRF2_CORE": "NQO1 GCLM GCLC TXNRD1 SRXN1 OSGIN1 AKR1C1 AKR1C2 AKR1B10 G6PD ME1 PIR ABCC3".split(),
    "ISR_ATF4": "DDIT3 ASNS TRIB3 ATF3 PSAT1 PHGDH PSPH SLC3A2 SLC7A5 VEGFA CEBPB".split(),
    "UPR_ER": "HSPA5 HERPUD1 DNAJB9 SDF2L1 SEL1L PDIA4 XBP1".split(),
    "HSF1_HEAT": "HSPA1A HSPA1B DNAJB1 HSPH1 HSPA6 BAG3".split(),
    "IFN": "ISG15 IFIT1 IFIT3 MX1 OAS1 IFI6 IFI44L STAT1 IRF7 IFITM1".split(),
    "NFKB": "NFKBIA TNFAIP3 RELB NFKB2 BIRC3 CXCL8 ICAM1 IER3".split(),
}
# PMAIP1, GADD45A, SESN2 and TNFRSF10B are left out of P53_ACTIVITY on purpose: they are also strongly ATF4/CHOP- or
# stress-driven (TNFRSF10B stays a reported context gene)
P53_ACTIVITY = ["CDKN1A", "MDM2", "FDXR", "ZMAT3", "SESN1", "BBC3", "BAX"] + \
    [g for g in CONTEXT["P53_EXT"] if g not in ("CCNG1", "BTG2", "TIGAR", "TNFRSF10B")]
SCORES = {"P53_ACTIVITY": P53_ACTIVITY, "FERRO_MARKERS": ["PTGS2", "CHAC1", "SLC7A11"],
          "INFLAMMASOME": ["NLRP3", "AIM2", "PYCARD", "CASP1", "CASP4", "CASP5", "IL1B", "IL18", "GSDMD"],
          "NRF2": CONTEXT["NRF2_CORE"], "ISR": CONTEXT["ISR_ATF4"], "UPR": CONTEXT["UPR_ER"],
          "HEAT_SHOCK": CONTEXT["HSF1_HEAT"], "IFN": CONTEXT["IFN"], "NFKB": CONTEXT["NFKB"]}
MODULES = ["PROTEASOME", "S_PHASE", "G2M_PHASE"]          # summed modules of tahoe_mtap_gankyrin.py
CONTEXT_SCORES = ["ISR", "NRF2", "UPR", "HEAT_SHOCK", "IFN", "NFKB", "P53_ACTIVITY", "FERRO_MARKERS", "INFLAMMASOME",
                  "PROTEASOME", "S_PHASE", "G2M_PHASE"]
CTX_VARS = ["cells_log2_vs_plate", "genes_per_cell_log2_vs_plate", "umi_per_cell_log2_vs_plate"]
FERRO_CONTEXT = ["ISR", "NRF2", "UPR", "HEAT_SHOCK", "NFKB", "IFN", "P53_ACTIVITY"]   # programs named with the markers
FERRO_CONTEXT_PREFIX = ("ISR", "NRF2", "UPR", "HEAT", "NFKB", "IFN", "P53")
FERRO_NOTES = {"ISR": "ISR: fits cystine starvation or any other ISR trigger, not separable from mRNA",
               "NRF2": "NRF2: antioxidant / protective response", "NFKB": "NF-kB: PTGS2 is NF-kB-inducible"}
NRF2_LEVEL = "NRF2_basal_score"   # level-vs-growth row for basal NRF2 activity (NFE2L2 mRNA is not NRF2 activity)
FERRO_LEVEL_GENES = ["GPX4", "ACSL4", "AIFM2", "SLC7A11", "NFE2L2", NRF2_LEVEL, "LPCAT3", "TFRC"]
MIN_EXPR_CPM = 1.0        # a line expresses a gene if its level (all wells) is >= this many CPM ...
EXPR_FRAC = 0.25          # ... and >= this fraction of the median line ...
AMBIENT_MULT = 2.0        # ... and >= this many times the ambient level: af x the gene's pooled CPM (all lines), with
AMBIENT_DEFAULT = 0.12    # af = what the MTAP-null lines read of the pooled MTAP (median; clipped to AMBIENT_CLIP);
AMBIENT_CLIP = (0.05, 0.3)  # this default when < 2 MTAP-null lines. Lines with a deleted CDKN2A read ~5-10%.
MIN_EXPR_LINES = 3        # genes expressed in fewer lines get no drug-effect calls
MIN_LEVEL_LINES = 5       # level-vs-growth needs a gene expressed in at least this many lines
MIN_COUNTS = 2.0          # 'testable': median raw counts per (well, line) profile among expressing lines
MIN_DMSO_COUNTS = 20      # baseline level from DMSO cells unless the line has fewer counts there (then all wells)
CONTEXT_Z = 3.0           # modules with |z| >= this are named in the 'context' column
N_P53_DOSES = 10          # drug-doses that define p53 responsiveness (strongest all-line P53_ACTIVITY, not toxic)
MIN_DRUG_WELLS = 20       # analyze stops (clearly) below this many drug wells with >= 3 profiled lines
PER_LINE_MAX = 10         # growth screens list each group line separately up to this many lines
TOP = 15                  # rows per table in summary.txt
BYTES_PER_CELL = 8.0      # per-cell files: measured on a real file, ~25 bytes per cell with 117 columns ...
BYTES_PER_COLUMN = 0.15   # ... (zstd; most values are zero)
PANEL_ANGLES = ["ferroptosis", "pyroptosis", "p53", "napepld_trim72", "crosslinks"]
TITLES = {"ferroptosis": "Ferroptosis genes: markers, defences, lipid remodelling, iron",
          "pyroptosis": "Pyroptosis machinery: gasdermins, inflammasome, caspases",
          "p53": "p53 activity: which drugs, which lines, genotype vs function",
          "napepld_trim72": "NAPEPLD (NAPE-PLD) and TRIM72 (MG53)",
          "crosslinks": "Cross-links to MTAP / Gankyrin"}
DNA_DAMAGE = {"names": ["Doxorubicin", "Epirubicin", "Idarubicin", "Daunorubicin", "Mitoxantrone", "Topotecan",
                        "Irinotecan", "Etoposide", "Teniposide", "Amsacrine", "Camptothecin", "Oxaliplatin", "Cisplatin",
                        "Carboplatin", "5-Fluorouracil", "Floxuridine", "Gemcitabine", "Cytarabine", "Hydroxyurea",
                        "Methotrexate", "Pemetrexed", "Fludarabine", "Clofarabine", "Cladribine"],
              "targets": r"\bTOP1\b|\bTOP2[AB]?\b|\bTYMS\b|\bDHFR\b|\bRRM[12]\b"}
PROTEASOME_I = {"names": ["Bortezomib", "Ixazomib", "Carfilzomib"], "moa": "Proteasome inhibitor"}
DNMT_I = {"names": ["Decitabine", "5-Azacytidine"], "moa": "DNA methyltransferase"}
CONTROLS = [  # (expectation, readout kind, readout, direction (+1 up, -1 down, 0 either), drug finder, at 24 h)
    ("DNA-damaging drugs (TOP1/TOP2 poisons, antimetabolites, platinum) raise P53_ACTIVITY", "score",
     "P53_ACTIVITY", 1, DNA_DAMAGE, "robust"),
    ("... and raise it more in TP53-wild-type than in TP53-altered lines (p53_wt_vs_altered.csv)", "p53wt", "",
     1, DNA_DAMAGE, "robust"),
    ("Dimethyl fumarate (NRF2 activator) raises NRF2 target genes", "score", "NRF2", 1,
     {"names": ["Dimethyl fumarate"]}, "uncertain"),
    ("Dimethyl fumarate raises HMOX1", "gene", "HMOX1", 1, {"names": ["Dimethyl fumarate"]}, "uncertain"),
    ("Proteasome inhibitors raise proteasome subunits (bounce-back)", "score", "PROTEASOME", 1, PROTEASOME_I,
     "robust"),
    ("Proteasome inhibitors raise heat-shock genes", "score", "HEAT_SHOCK", 1, PROTEASOME_I, "robust"),
    ("Proteasome inhibitors raise HMOX1", "gene", "HMOX1", 1, PROTEASOME_I, "robust"),
    ("HSP90 inhibitors (Pimitespib) raise heat-shock genes", "score", "HEAT_SHOCK", 1,
     {"names": ["Pimitespib"], "targets": r"\bHSP90"}, "robust"),
    ("Ciclopirox (iron chelator) raises TFRC (iron starvation)", "gene", "TFRC", 1, {"names": ["Ciclopirox"]},
     "robust"),
    ("DNMT inhibitors raise GSDME in the GSDME-low lines (uncertain at 24 h: demethylation needs several divisions)",
     "reexpr", "GSDME", 1, DNMT_I, "uncertain"),
    ("DNMT inhibitors raise interferon genes (viral mimicry; usually seen after days, uncertain at 24 h)", "score",
     "IFN", 1, DNMT_I, "uncertain"),
    ("COX inhibitors change PTGS2 (report only: the direction is not certain)", "gene", "PTGS2", 0,
     {"moa": "Cyclooxygenase"}, "uncertain"),
    ("Antimitotics (taxanes, vinca alkaloids) raise G2/M genes", "score", "G2M_PHASE", 1,
     {"names": ["Paclitaxel", "Docetaxel", "Vinblastine", "Vincristine", "Vinorelbine", "Eribulin"],
      "moa": "Microtubule inhibitor"}, "robust"),
    ("Dinaciclib (CDK9) causes a transcription drop (UMIs per cell fall)", "ctx", "umi_per_cell_log2_vs_plate", -1,
     {"names": ["Dinaciclib"]}, "robust"),
]


# ============================================================================= small helpers
def quiet():
    """Silence numpy's all-NaN warnings (lines missing from some wells) and pandas' fragmentation hints."""
    warnings.filterwarnings("ignore", category=RuntimeWarning)
    warnings.filterwarnings("ignore", category=pd.errors.PerformanceWarning)
    np.seterr(all="ignore")


_WARNED = {}


def atlas(required=True, quiet=False):
    """tahoe_atlas.py (agent runner, hints), imported only by check / agents / bundle (and analyze, to see whether
    the atlas has been computed). An older copy without the agent runner counts as missing (warning unless quiet)."""
    try:
        import tahoe_atlas as A
    except ImportError:
        if required:
            sys.exit("This step needs tahoe_atlas.py in the same folder as tahoe_gene_panel.py")
        return None
    except SystemExit as e:                     # tahoe_atlas.py refuses an older tahoe_mtap_gankyrin.py
        if required:
            raise
        if not quiet and not _WARNED.get("atlas"):
            _WARNED["atlas"] = True
            log(f"  WARNING: tahoe_atlas.py could not be loaded: {e}")
        return None
    old = getattr(A, "EFFECTS_VERSION", 0) < PANEL_METHOD
    if old or not all(hasattr(A, f) for f in ("agent_text", "add_log", "key_hint", "sdk_hint", "sandbox_problem",
                                              "cmd_agents", "effects_ready")):
        msg = OLD_COPY.format(f="tahoe_atlas.py", why=f" (method v{PANEL_METHOD}: needed for the agents step and the "
                                                      "briefs' genome-wide look-ups)")
        if required:
            sys.exit(msg)
        if (old or not quiet) and not _WARNED.get("atlas"):     # an older copy: always said once
            _WARNED["atlas"] = True
            log("  WARNING: " + msg)
        return None
    return A


def atlas_ready(atl, need_script=False):
    """True when <atl> holds a complete method-v3 atlas computation: tahoe_atlas.effects_ready of the current
    tahoe_atlas.py; when that copy is missing or older, the version in its stamp effects/complete.json (the panel
    reads the atlas's tables by path). need_script: also the current tahoe_atlas.py itself (the briefs' look-ups)."""
    A = atlas(required=False, quiet=True)
    if A is not None:
        try:
            return bool(A.effects_ready(atl))
        except Exception:  # noqa: BLE001
            return False
    return not need_script and T.atlas_effects_version(atl) >= T.METHOD_VERSION


def bpath(p):
    """A path as written in the agents' briefs: forward slashes on Windows (PowerShell and Python both accept them,
    and a pasted 'C:\\tahoe\\results' would turn \\t and \\r into control characters in a Python string)."""
    p = str(p)
    return p.replace("\\", "/") if sys.platform == "win32" else p


def quote(p):
    """A path as the shell needs it: PowerShell on Windows ("..." when needed), sh elsewhere (as tahoe_atlas.py)."""
    p = str(p)
    if sys.platform == "win32":
        return f'"{p}"' if not p or any(c in p for c in " &();,'{}") else p
    return shlex.quote(p)


def agent_python():
    """How agents run this Python (as tahoe_atlas.agent_python): PowerShell needs & "..." for paths with spaces."""
    exe = sys.executable or "python3"
    if sys.platform == "win32":
        q = quote(exe)
        return f"& {q}" if q != exe else exe
    return shlex.quote(exe)


def rel_path(p):
    try:
        r = os.path.relpath(p)
    except ValueError:                          # another drive (Windows)
        return os.path.abspath(p)
    return os.path.abspath(p) if r.startswith("..") else r


def user_cmd(command, extra=""):
    me = os.path.abspath(__file__)
    here = os.path.normcase(os.path.dirname(me)) == os.path.normcase(os.getcwd())
    return f"{T.py_cmd()} {os.path.basename(me) if here else quote(me)} {command}{extra}"


def long_run_hint(command, extra="", out="gene_panel"):
    logf = rel_path(os.path.join(out, "agents.log" if command == "agents" else "gene_panel.log"))
    if sys.platform == "win32":
        return f"{user_cmd(command, extra)}   (leave the window open; log in {logf})"
    return f"nohup {user_cmd(command, extra)} > /dev/null 2>&1 &   then: tail -f {quote(logf)}"


def same_folders(args, workers=0):
    s = ""
    if os.path.abspath(args.data) != os.path.abspath("."):
        s += " --data " + quote(args.data)
    if os.path.abspath(args.out) != os.path.abspath(os.path.join(args.data, "gene_panel")):
        s += " --out " + quote(args.out)
    return s + (f" --workers {workers}" if workers else "")


def fnum(v, fmt="{:.2f}"):
    try:
        return "NA" if v is None or not np.isfinite(float(v)) else fmt.format(float(v))
    except (TypeError, ValueError):
        return str(v)


def by_fdr(t, fdr="fdr", z="z"):
    """Rows by FDR, ties (common: BH gives many rows the same q) broken by the larger |z|."""
    if t is None or not len(t):
        return t
    return t.assign(_a=-t[z].abs()).sort_values([fdr, "_a"], kind="stable").drop(columns="_a")


def table(df, cols, n=TOP, digits=3):
    cols = [c for c in cols if c in df]
    if df is None or not len(df) or not cols:
        return "  (none)"
    return df.head(n)[cols].round(digits).to_string(index=False)


def rowcorr(M, v):
    """Pearson correlation of every row of M with v (as in T.gankyrin_level_screen)."""
    Mc = M - M.mean(axis=1, keepdims=True)
    vc = v - v.mean()
    den = np.sqrt((Mc ** 2).sum(axis=1) * (vc ** 2).sum())
    with np.errstate(invalid="ignore", divide="ignore"):
        return (Mc @ vc) / den


def spearman_p(a, b):
    """Spearman rho, n and a two-sided p (Fisher z approximation) over the finite pairs."""
    a, b = np.asarray(a, dtype=float), np.asarray(b, dtype=float)
    ok = np.isfinite(a) & np.isfinite(b)
    n = int(ok.sum())
    if n < 4:
        return np.nan, n, np.nan
    ra, rb = pd.Series(a[ok]).rank().to_numpy(), pd.Series(b[ok]).rank().to_numpy()
    if ra.std() == 0 or rb.std() == 0:
        return np.nan, n, np.nan
    r = float(np.corrcoef(ra, rb)[0, 1])
    z = math.atanh(max(min(r, 0.999999), -0.999999)) * math.sqrt(max(n - 3, 1))
    return r, n, float(2 * T.norm_sf([abs(z)])[0])


def auc(pos, neg):
    """Mann-Whitney: P(pos > neg) (+ half the ties) and a two-sided normal-approximation p."""
    a = np.asarray(pos, dtype=float)
    b = np.asarray(neg, dtype=float)
    a, b = a[np.isfinite(a)], b[np.isfinite(b)]
    if not len(a) or not len(b):
        return np.nan, np.nan
    r = pd.Series(np.concatenate([a, b])).rank().to_numpy()
    u = r[:len(a)].sum() - len(a) * (len(a) + 1) / 2
    n1, n2 = len(a), len(b)
    z = (u - n1 * n2 / 2) / math.sqrt(n1 * n2 * (n1 + n2 + 1) / 12)
    return u / (n1 * n2), float(2 * T.norm_sf([abs(z)])[0])


def dose_columns(res, zcol, p_up, p_down):
    """z at every dose + dose pattern + drug-level FDR, for increases and decreases (T.add_dose_columns twice)."""
    res = T.add_dose_columns(res, zcol, p_up, "up").rename(columns={"dose_pattern": "dose_pattern_up",
                                                                    "fdr_drug": "fdr_drug_up"})
    dn = T.add_dose_columns(res, zcol, p_down, "down")
    res["dose_pattern_down"] = dn["dose_pattern"].values
    res["fdr_drug_down"] = dn["fdr_drug"].values
    return res


def context_text(df, skip=()):
    """'ISR up z 4.1; NRF2 up z 6.0': the context modules with |z| >= CONTEXT_Z, strongest first."""
    Z = {m: pd.to_numeric(df[f"{m}_z"], errors="coerce").to_numpy(dtype=float) for m in CONTEXT_SCORES
         if f"{m}_z" in df and m not in skip}
    out = []
    for i in range(len(df)):
        items = sorted(((abs(z[i]), f"{m} {'up' if z[i] > 0 else 'down'} z {z[i]:.1f}") for m, z in Z.items()
                        if np.isfinite(z[i]) and abs(z[i]) >= CONTEXT_Z), reverse=True)
        out.append("; ".join(t for _, t in items))
    return out


def find_drugs(present, drugs, spec):
    """Drugs in the data matching a control's names (prefix, case-insensitive), mechanism or targets."""
    hit = set()
    low = {d.lower().strip(): d for d in present}
    for nm in spec.get("names", []):
        hit |= {d for k, d in low.items() if k.startswith(nm.lower())}
    meta = drugs.reindex(list(present))
    if spec.get("moa"):
        m = meta.get("moa_fine", pd.Series("", index=meta.index)).fillna("").astype(str)
        hit |= set(m.index[m.str.contains(spec["moa"], case=False, regex=False)])
    if spec.get("targets"):
        t = meta.get("targets", pd.Series("", index=meta.index)).fillna("").astype(str).str.upper()
        hit |= set(t.index[t.str.contains(spec["targets"], regex=True)])
    return sorted(hit)


# ============================================================================= the gene lists
def gene_table(args, symbols=None):
    """Panel + anchors + genes added with --genes: gene, pathway, role, gene_set, also_known_as, symbol_used.
    symbols (the gene metadata's) lets a --genes entry typed in another case match the metadata symbol."""
    rows = [{"gene": g, "pathway": p, "role": r, "gene_set": "panel", "symbol_used": g} for g, p, r in PANEL]
    rows += [{"gene": g, "pathway": "anchor (MTAP / Gankyrin run)", "role": ANCHOR_ROLES.get(g, ""),
              "gene_set": "anchor", "symbol_used": g} for g in ANCHORS]
    have = {r["gene"] for r in rows}
    for item in [x.strip() for x in (getattr(args, "genes", "") or "").split(",") if x.strip()]:
        sym, _, pw = item.partition(":")
        sym = sym.strip()
        g = ALIASES.get(sym.upper(), sym)
        if symbols:
            g = resolve_symbols([g], symbols).get(g, g)
        if g in have:
            continue
        have.add(g)
        rows.append({"gene": g, "pathway": pw.strip() or "added", "role": f"added with --genes ({item})",
                     "gene_set": "added", "symbol_used": g})
    t = pd.DataFrame(rows)
    t.insert(1, "also_known_as", t["gene"].map(AKA).fillna(""))
    return t


def context_genes():
    seen, out = set(), []
    for s, gs in CONTEXT.items():
        for g in gs:
            if g not in seen:
                seen.add(g)
                out.append((g, s))
    return out


def resolve_symbols(genes, symbols):
    """Map each wanted gene to the gene-metadata symbol (exact, else case-insensitive). Returns {gene: symbol}."""
    exact = set(symbols)
    upper = {}
    for s in symbols:
        upper.setdefault(s.upper(), s)
    out = {}
    for g in genes:
        if g in exact:
            out[g] = g
        elif g.upper() in upper:
            out[g] = upper[g.upper()]
    return out


def label_of(g):
    return f"{g} ({AKA[g]})" if g in AKA else g


# ============================================================================= extract
REINDEX_HINT = T.REINDEX_HINT


def cells_estimate_gb(n_files, n_cols):
    return n_files * 28_000 * (BYTES_PER_CELL + BYTES_PER_COLUMN * n_cols) / 1e9


def mixed_gene_list_problem(out, report, cols):
    """A message when out/cells holds per-cell files of a different gene list (they cannot be mixed), else None."""
    cells = sorted(glob.glob(os.path.join(out, "cells", "*.parquet")))
    if not cells:
        return None
    jf = os.path.join(out, "extracted_columns.json")
    if os.path.exists(jf):
        with open(jf, encoding="utf-8") as fh:
            old = json.load(fh)
        old_t, new_t = set(old.get("targets", [])), set(report["targets"])
        same = old_t == new_t and {k: set(v) for k, v in old.get("modules", {}).items()} == \
            {k: set(v) for k, v in report["modules"].items()}
        added, dropped = sorted(new_t - old_t), sorted(old_t - new_t)
    else:
        have = set(pq.read_schema(cells[0]).names)
        same = set(cols) <= have
        added, dropped = sorted(set(cols) - have), []
    if same:
        return None
    what = "; ".join(x for x in [f"new genes: {', '.join(added[:12])}" + (" ..." if len(added) > 12 else "")
                                 if added else "", f"genes no longer asked for: {', '.join(dropped[:12])}"
                                 if dropped else "", "" if added or dropped else "gene modules differ"] if x)
    return (f"{os.path.abspath(out)} already holds per-cell files ({len(cells)}) extracted with a different gene list "
            f"({what}). The old files lack the new columns, so the two cannot be mixed. Either extract into a new "
            f"folder (--out {quote(os.path.abspath(out) + '_2')}) or delete {quote(os.path.join(out, 'cells'))} "
            f"to start over.")


def wanted_genes(args, symbols):
    """Panel (+ --genes) and context genes resolved against the gene metadata; logs the ones missing."""
    gt = gene_table(args, symbols)
    want = [g for g in gt["gene"] if g not in ANCHORS] + [g for g, _ in context_genes()]
    want = list(dict.fromkeys(want))
    sym = resolve_symbols(want + ANCHORS, symbols)
    missing = [g for g in want if g not in sym]
    for g in missing:
        log(f"  WARNING: {label_of(g)} not found in the gene metadata: not extracted (listed as missing in the "
            "results)")
    return [sym[g] for g in want if g in sym], missing


def cmd_extract(args):
    out = args.out
    os.makedirs(out, exist_ok=True)
    idx = T.discover(args.data, out, refresh=args.reindex)
    if not idx["expression"]:
        sys.exit("No expression parquet files found under " + os.path.abspath(args.data) + REINDEX_HINT)
    gm = T.read_tables(idx["gene"], ["token_id", "gene_symbol", "ensembl_id"])
    if gm is None:
        sys.exit("Gene metadata (token_id -> gene_symbol) not found" + REINDEX_HINT)
    genes, missing = wanted_genes(args, gm["gene_symbol"].dropna().astype(str).tolist())
    _targets, cols, _lut, report = T.build_columns(gm, genes)
    problem = mixed_gene_list_problem(out, report, cols)
    if problem:
        sys.exit(problem)
    n_files = min(len(idx["expression"]), args.limit_files or len(idx["expression"]))
    log(f"Gene panel extraction: {len(report['targets'])} genes + {sum(bool(v) for v in report['modules'].values())}"
        f" modules per cell ({len(missing)} not in the gene metadata); per-cell files ~"
        f"{cells_estimate_gb(n_files, len(cols)):.1f} GB for {n_files} files")
    a = argparse.Namespace(**vars(args))
    a.extra_genes, a.reindex = genes, False
    T.cmd_extract(a)


# ============================================================================= analyze: the shared state
class Run:
    """What one analyze run computes; the steps below fill it in."""

    def __init__(self, args):
        self.args, self.out = args, args.out
        self.R = os.path.join(args.out, "results")
        self.failures = {}
        self.RES, self.WS, self.CAL, self.R2 = {}, {}, {}, {}      # per gene: drug effects, wells, calibration
        self.SW, self.SC = {}, {}                                   # per score: wells, per drug-dose
        self.skipped = {}                                           # gene -> why no drug effects
        self.notes = []                                             # steps not applicable to these data
        self.prior, self.facts = None, {}                           # earlier run (cross-links); method v3 facts

    def save(self, df, name, index=False):
        df.to_csv(os.path.join(self.R, name), index=index)

    def attempt(self, label, fn):
        """Run one analysis; if it fails, log it (traceback in the run log) and carry on with the others."""
        try:
            return fn()
        except Exception as e:  # noqa: BLE001
            log(f"  WARNING: {label} failed: {e!r}")
            T._to_log_file(traceback.format_exc().rstrip())
            self.failures[label] = repr(e)
            return None

    def attempt_each(self, label, items, fn):
        """fn(item) for every item; a failure is logged once per distinct error (traceback in the run log) and
        recorded as one entry, so one cause failing for 40 genes gives one line, not 40."""
        out, errs = {}, {}
        for it in items:
            try:
                out[it] = fn(it)
            except Exception as e:  # noqa: BLE001
                if repr(e) not in errs:
                    T._to_log_file(traceback.format_exc().rstrip())
                errs.setdefault(repr(e), []).append(str(it))
        for e, its in errs.items():
            names = ", ".join(its[:6]) + (" ..." if len(its) > 6 else "")
            log(f"  WARNING: {label} failed: {len(its)} of {len(items)} ({names}): {e}")
            self.failures[f"{label} ({names})"] = e
        return out


def load(S):
    args, out = S.args, S.out
    for f in ["well_line.parquet", "sample_map.csv", "extract_info.json"]:
        if not os.path.exists(os.path.join(out, f)):
            sys.exit(f"{f} not found in {out}; run the 'extract' step first")
    os.makedirs(S.R, exist_ok=True)
    prev = os.path.join(S.R, "previous_run")         # an earlier run's tables never pass as this run's
    old = [f for f in glob.glob(os.path.join(S.R, "*")) if os.path.isfile(f)]
    if old:
        new = prev + "_new"
        shutil.rmtree(new, ignore_errors=True)
        os.makedirs(new)
        for f in old:
            try:
                shutil.move(f, os.path.join(new, os.path.basename(f)))
            except OSError as e:                     # Windows: a results file is open in another program
                for g in glob.glob(os.path.join(new, "*")):
                    shutil.move(g, os.path.join(S.R, os.path.basename(g)))
                shutil.rmtree(new, ignore_errors=True)
                sys.exit(f"Cannot move {f} ({e.strerror or e}): close it (open in Excel?) and run analyze again")
        shutil.rmtree(prev, ignore_errors=True)
        os.replace(new, prev)
        log(f"  the earlier results ({len(old)} files) moved to {prev}")
    S.idx = T.discover(args.data, out)
    with open(os.path.join(out, "extract_info.json"), encoding="utf-8") as fh:
        S.info = json.load(fh)
    wl = pd.read_parquet(os.path.join(out, "well_line.parquet"))
    wl["sample"] = wl["sample"].astype(str)
    wl["cell_line_id"] = wl["cell_line_id"].astype(str)
    sm = pd.read_csv(os.path.join(out, "sample_map.csv"), dtype={"sample": str, "plate": str, "drug": str,
                                                                  "plate_num": str})
    sm["is_dmso"] = sm["is_dmso"].astype(bool)
    sm["well"] = sm["well"].fillna("")
    S.sm_all = sm.copy()
    S.targets = list(S.info["targets"])
    S.cols = list(S.info["columns"])
    gm = T.read_tables(S.idx["gene"], ["gene_symbol"])
    S.symbols = set(gm["gene_symbol"].dropna().astype(str)) if gm is not None else set()
    gt = gene_table(args, S.symbols)
    S.gt = gt
    S.panel = [g for g in gt["gene"] if g not in ANCHORS]           # panel + added
    S.main = ANCHORS + S.panel                                       # genes with full tables
    S.ctx_genes = [g for g, _ in context_genes()]
    S.set_of = {g: s for g, s in context_genes()}
    S.set_of.update({g: "anchor" for g in ANCHORS})
    S.set_of.update({g: s for g, s in zip(gt["gene"], gt["gene_set"])})
    S.cl = T.load_cell_lines(S.idx)
    S.drugs = T.load_drugs(S.idx)
    S.failed = T.find_failed_wells(sm)
    S.save(S.failed[["sample", "plate", "well", "drug", "conc", "n_cells", "cells_log2_vs_plate"]],
           "excluded_failed_wells.csv")
    if len(S.failed):
        log(f"Excluding {len(S.failed)} failed wells (almost no cells recovered; same drug fine elsewhere)")
        sm = sm[~sm["sample"].isin(S.failed["sample"])].reset_index(drop=True)
        wl = wl[wl["sample"].isin(sm["sample"])].reset_index(drop=True)
    S.unreliable = T.unreliable_plates(sm, getattr(args, "unreliable_plates", None))
    sm = T.mark_unreliable(sm, S.unreliable)
    S.sm_all = T.mark_unreliable(S.sm_all, S.unreliable)
    if S.unreliable:
        log(f"Unreliable plates (kept per well; left out of the reference spread, the plate-factor peers and the "
            f"drug-doses that also have a well elsewhere): {', '.join(S.unreliable)}")
    S.atl = T.atlas_dir(args)                         # the atlas's v3 exports (read by path), when computed
    S.ax = T.load_atlas_inputs(S.atl if S.atl and atlas_ready(S.atl) else None, S.unreliable,
                               "--atlas none" if not S.atl else "")
    if S.atl and not S.ax["dir"]:
        S.ax["version"] = T.atlas_effects_version(S.atl)
    for w_ in S.ax["warnings"]:
        log(f"  WARNING: {w_}")
    S.comp_note = T.composition_note(S.ax)
    S.M = T.Method(sm, S.ax["shift"], S.ax["plate_scale"], S.ax["dd_extra"])
    log(f"  composition: {S.comp_note}; plate factors: "
        + ("imported from the atlas" if S.ax["plate_scale"] is not None else "fitted over the panel's genes")
        + ("; 'wells disagree' imported from the atlas" if S.ax["dd_extra"] is not None else ""))
    S.wl, S.sm = wl, sm
    prof = wl[wl["n_cells"] >= T.MIN_CELLS]
    good = prof.groupby("sample").size()
    good = set(good.index[good >= 3])
    nd = int((~sm["is_dmso"] & sm["sample"].isin(good)).sum())
    trial = f" (a trial with --limit-files {S.info['limit_files']})" if S.info.get("limit_files") else ""
    if nd < MIN_DRUG_WELLS:
        sys.exit(f"Only {nd} drug wells have >= 3 cell lines with >= {T.MIN_CELLS} cells each{trial}: too few for "
                 f"the corrected statistics, which score every well against the other wells of its plate and well "
                 f"position. Extract more files (e.g. --limit-files 30 into a new --out) or the full data; for a "
                 f"quick look, --min-cells 10 counts smaller profiles.")
    if sm["plate"].nunique() < 4:
        log(f"  note: only {sm['plate'].nunique()} plate(s){trial}: the well-position correction needs the same "
            f"position on >= {T.MIN_SLOT_WELLS} other plates and is mostly inactive")
    missing = [g for g in S.main if g not in S.targets]
    if missing:
        log(f"  not extracted (absent from the gene metadata, or added after the extraction): {', '.join(missing)}")


def genotypes(idx, index, names, wt_override, alt_override):
    """TP53 status per line from the cell-line metadata (any TP53 driver row = altered), protein changes, CDKN2A and
    CDKN2B deletion; --tp53-wt / --tp53-altered override (names or Cellosaurus ids). Returns (table, deleted):
    deleted = {gene: lines with a deletion driver row for it}."""
    out = pd.DataFrame(index=index)
    out["in_cell_line_metadata"] = False
    out["tp53_status"] = "unknown (line not in the cell-line metadata)"
    out["tp53_changes"] = ""
    out["cdkn2a_deleted"] = False
    out["cdkn2b_deleted"] = False
    deleted = {}
    raw = T.read_tables(idx["cell_line"]) if idx.get("cell_line") else None
    if raw is not None and {"Cell_ID_Cellosaur", "Driver_Gene_Symbol"} <= set(raw.columns):
        cid = raw["Cell_ID_Cellosaur"].map(T.to_text).astype(str)
        sym = raw["Driver_Gene_Symbol"].map(T.to_text).astype(str).str.strip().str.upper()
        pcol = next((c for c in raw.columns if "ProtEffect" in c), None)
        ch = raw[pcol].map(T.to_text).astype(str).str.strip() if pcol else pd.Series("", index=raw.index)
        vt = raw["Driver_VarType"].map(T.to_text).astype(str).str.strip() if "Driver_VarType" in raw \
            else pd.Series("", index=raw.index)
        txt = ch.where(ch != "", vt)
        tp = pd.DataFrame({"cid": cid, "ch": txt})[(sym == "TP53").to_numpy()]
        tpch = tp.groupby("cid")["ch"].agg(lambda s: "; ".join(sorted({x for x in s if x})))
        isdel = (vt.str.contains("del", case=False) | ch.str.upper().eq("DEL")).to_numpy()
        for g, c in zip(sym[isdel], cid[isdel]):
            deleted.setdefault(g, set()).add(c)
        inm = out.index.isin(set(cid))
        out.loc[inm, "in_cell_line_metadata"] = True
        out.loc[inm, "tp53_status"] = "wild type (no TP53 driver call)"
        out.loc[out.index.isin(set(tpch.index)), "tp53_status"] = "altered"
        out["tp53_changes"] = tpch.reindex(out.index).fillna("").astype(str)
        out["cdkn2a_deleted"] = out.index.isin(deleted.get("CDKN2A", set()))
        out["cdkn2b_deleted"] = out.index.isin(deleted.get("CDKN2B", set()))
    for opt, status in ((wt_override, "wild type (set by --tp53-wt)"), (alt_override, "altered (set by --tp53-altered)")):
        if opt:
            want = {x.strip().upper() for x in opt.split(",") if x.strip()}
            hit = [i for i in out.index if i.upper() in want or str(names.get(i, "")).upper() in want]
            out.loc[hit, "tp53_status"] = status
            found = {i.upper() for i in hit} | {str(names.get(i, "")).upper() for i in hit}
            if want - found:
                log(f"  WARNING: TP53 override: no line called {', '.join(sorted(want - found))}")
    st = out["tp53_status"].astype(str)
    out["tp53_group"] = np.where(st.str.startswith("wild type"), "WT", np.where(st.str.startswith("altered"),
                                                                                "altered", ""))
    return out, deleted


def step_baseline(S):
    base, S.null_source = T.baseline_by_line(S.wl, S.sm, S.cl, S.targets, S.args.mtap_null)
    for c in ["cell_name", "Organ", "drivers", "Cell_ID_DepMap"]:
        base[c] = base[c].fillna("").astype(str) if c in base else ""
    S.name = pd.Series([n or i for i, n in zip(base.index, base["cell_name"])], index=base.index)
    geno, S.deleted = genotypes(S.idx, base.index, S.name, S.args.tp53_wt, S.args.tp53_altered)
    S.base = base.join(geno)
    S.null_lines = list(base.index[base["MTAP_null"]])
    log(f"  {len(base)} lines: TP53 wild type {int((S.base['tp53_group'] == 'WT').sum())}, altered "
        f"{int((S.base['tp53_group'] == 'altered').sum())}, unknown {int((S.base['tp53_group'] == '').sum())}; "
        f"MTAP-null {len(S.null_lines)} ({S.null_source})")


def step_expression(S):
    """Expressed rule, levels, counts per profile, status of every extracted gene; expression_by_line.csv."""
    base, genes = S.base, [g for g in S.targets if f"{g}_cpm_all_wells" in S.base]
    enough = (base["n_cells_total"] >= T.MIN_LINE_CELLS).to_numpy()
    if enough.sum() < 3:
        enough = (base["n_cells_total"] > 0).to_numpy()
    S.enough = pd.Series(enough, index=base.index)
    C = pd.DataFrame({g: base[f"{g}_cpm_all_wells"].astype(float) for g in genes}, index=base.index)
    Cd = pd.DataFrame({g: base[f"{g}_cpm_dmso"].astype(float) for g in genes}, index=base.index)
    med = C[enough].median()
    # ambient RNA: every line reads some of the well's pooled RNA. af = what the MTAP-null lines (no MTAP mRNA of
    # their own) read of the pooled MTAP level; a line must read >= AMBIENT_MULT x af x the gene's pooled level
    pooled = (1e6 * S.wl[genes].sum() / S.wl["total_counts"].sum()).astype(float)
    nl = [c for c in S.null_lines if c in C.index]
    if len(nl) >= 2 and "MTAP" in C and pooled.get("MTAP", 0) > 0:
        raw = float(C.loc[nl, "MTAP"].median() / pooled["MTAP"])
        S.af = float(np.clip(raw, *AMBIENT_CLIP))
        S.af_source = (f"median MTAP of the {len(nl)} MTAP-null lines / pooled MTAP = {raw:.3f}"
                       + (f", clipped to {S.af:.2f}" if S.af != raw else ""))
    else:
        S.af = AMBIENT_DEFAULT
        S.af_source = f"default {AMBIENT_DEFAULT:g} (fewer than 2 MTAP-null lines to measure it)"
    S.pooled, S.ambient = pooled, S.af * pooled
    thr = np.maximum(np.maximum(EXPR_FRAC * med, MIN_EXPR_CPM), AMBIENT_MULT * S.ambient)
    E = C.ge(thr, axis=1)
    S.C, S.Cd, S.med, S.thr, S.E = C, Cd, med, thr, E
    log(f"  ambient RNA fraction af = {S.af:.3f} ({S.af_source}); a line expresses a gene at >= "
        f"{EXPR_FRAC:.0%} of the median line, >= {MIN_EXPR_CPM:g} CPM and >= {AMBIENT_MULT:g} x af x its pooled CPM")
    d = S.wl.merge(S.sm[["sample", "is_dmso"]], on="sample")
    S.dmso_counts = d[d["is_dmso"]].groupby("cell_line_id")[genes].sum().reindex(base.index).fillna(0.0)
    nw = max(1, S.sm["sample"].nunique())                 # share of wells where a line has a usable profile
    S.line_well_frac = (S.wl[S.wl["n_cells"] >= T.MIN_CELLS].groupby("cell_line_id")["sample"].nunique() / nw) \
        .reindex(base.index).fillna(0.0)
    S.g2m = None                                   # proliferation per line: DMSO G2M level (as T), else all wells
    if "G2M_PHASE" in S.wl:
        al = S.wl.groupby("cell_line_id")[["G2M_PHASE", "total_counts"]].sum().reindex(base.index)
        allw = 1e6 * al["G2M_PHASE"] / al["total_counts"]
        dm = base["G2M_PHASE_cpm_dmso"] if "G2M_PHASE_cpm_dmso" in base else allw * np.nan
        S.g2m = dm.where(np.isfinite(dm.astype(float)) & (dm > 0), allw)
    P = S.wl.loc[S.wl["n_cells"] >= T.MIN_CELLS, ["cell_line_id"] + genes]
    M = P[genes].to_numpy(dtype=float, copy=True)
    M[~E.reindex(P["cell_line_id"]).fillna(False).to_numpy(dtype=bool)] = np.nan
    S.counts = pd.Series(np.nanmedian(M, axis=0) if len(M) else np.full(len(genes), np.nan), index=genes)
    del M
    S.status = {}
    for g in S.main + S.ctx_genes:
        S.status[g] = gene_status(S, g)
    S.n_expr = E.sum()
    long = []
    for g in genes:
        long.append(pd.DataFrame({
            "gene": g, "gene_set": S.set_of.get(g, ""), "cell_line_id": base.index, "cell_name": S.name.values,
            "organ": base["Organ"].values, "tp53_status": base["tp53_status"].values,
            "cpm_dmso": Cd[g].values, "cpm_all_wells": C[g].values,
            "pct_cells_dmso": base[f"{g}_pct_cells_dmso"].values,
            "vs_median_line": (C[g] / med[g]).values if med[g] > 0 else np.nan,
            "vs_pooled_level": (C[g] / pooled[g]).values if pooled[g] > 0 else np.nan, "expressed": E[g].values}))
    S.save(pd.concat(long, ignore_index=True), "expression_by_line.csv")


def effective_lines(S, g):
    """The expressing lines that actually carry a gene's drug effects: a usable profile (>= MIN_CELLS cells) in most
    wells and > 0 counts in the DMSO wells (a line 'expressed' only through its all-wells level rarely enters)."""
    if g not in S.E or g not in S.dmso_counts:
        return []
    return [c for c in S.E.index[S.E[g]] if S.line_well_frac.get(c, 0) > 0.5 and S.dmso_counts.at[c, g] > 0]


def gene_status(S, g):
    if g not in S.targets:
        return ("not in the gene metadata" if S.symbols and g not in S.symbols else
                "not extracted (not in this extraction's gene list: extract into a new --out)")
    n = int(S.E[g].sum())
    if n == 0:
        return "not expressed in any line"
    if n < MIN_EXPR_LINES:
        return f"expressed in only {n} line(s): no drug-effect calls (needs >= {MIN_EXPR_LINES})"
    c = S.counts.get(g, np.nan)
    if not c >= MIN_COUNTS:
        return f"low counts (median {fnum(c, '{:.1f}')} per well x line profile): effects flagged 'low counts'"
    return "testable"


def has_effects(S, g):
    st = S.status.get(g, "")
    return st == "testable" or st.startswith("low counts")


def effect_genes(S):
    """(every extracted feature in analysis order, the ones that get drug effects)."""
    order = [m for m in MODULES if m in S.cols] + [g for g in S.main if g in S.targets] + \
        [g for g in S.ctx_genes if g in S.targets]
    return order, [g for g in order if g in MODULES or g in ("MTAP", "PSMD10") or has_effects(S, g)]


def gene_exclusions(S, g):
    """Lines left out of a gene's drug effects: MTAP-null lines for MTAP and none for PSMD10 and the modules (as
    T.cmd_analyze), the non-expressing lines for every other gene."""
    if g == "MTAP":
        return S.null_lines
    if g in MODULES or g == "PSMD10":
        return []
    return list(S.E.index[~S.E[g]])


def step_prepare(S):
    """Method v3 for every feature at once (T.Method): both position passes and, unless the atlas exported them,
    the plate factors fitted over the testable genes and the modules."""
    _order, todo = effect_genes(S)
    S.attempt_each("position passes", todo, lambda g: S.M.add(S.wl, g, gene_exclusions(S, g)))
    fit_on = [g for g in todo if g in MODULES or S.status.get(g) == "testable"]
    S.M.complete(fit_on)
    why = "" if S.ax["plate_scale"] is not None else \
        "; --atlas none" if not S.atl else \
        "; not imported: " + "; ".join(S.ax["warnings"]) if S.ax["warnings"] else \
        "; the atlas's are used once it is computed with method v3" if S.ax["version"] < T.METHOD_VERSION else \
        "; the atlas has no plate_scale.csv"
    S.plate_scale_note = S.M.factor_source + why
    log(f"  plate factors {S.plate_scale_note}; > {T.NOISY_PLATE:g}: {T.plate_factor_text(S.M)}")


def step_effects(S):
    """T.expression_effects for the modules, anchors, panel and context genes (non-expressing lines left out)."""
    order, todo = effect_genes(S)
    t0 = time.time()
    for g in order:
        if g not in todo:
            S.skipped[g] = S.status.get(g, "")
    log(f"Drug effects (corrected) for {len(todo)} genes and modules "
        f"({len(order) - len(todo)} left out: not expressed / too few lines) ...")
    p53set = set(P53_ACTIVITY)
    state = {"k": 0, "last": time.time()}

    def one(g):
        state["k"] += 1
        if time.time() - state["last"] > 30:
            log(f"  {state['k']}/{len(todo)} genes ({time.time() - t0:.0f} s)")
            state["last"] = time.time()
        extra = None
        if g == "PSMD10" and "PROTEASOME" in S.WS:
            extra = S.WS["PROTEASOME"][["W2", "z"]].rename(columns={"W2": "PROTEASOME_log2FC", "z": "PROTEASOME_z"})
        res, W, d, cal = T.expression_effects(S.wl, S.sm, g, gene_exclusions(S, g), S.ctx, S.drugs, extra,
                                              method=S.M)
        if S.status.get(g, "").startswith("low counts"):       # pseudocount-dominated: shutdown wells look 'up'
            res["flags"] = ["; ".join(x for x in (f, "low counts") if x) for f in res["flags"]]
            res["call"] = ""
        if g in p53set:
            S.R2[g] = d.pivot_table(index="sample", columns="cell_line_id", values="r2")
        S.RES[g], S.WS[g], S.CAL[g] = res, W, cal
    S.attempt_each("drug effects", todo, one)
    log(f"  {len(S.RES)}/{len(todo)} done ({time.time() - t0:.0f} s)")


# ============================================================================= pathway scores and context
def step_scores(S):
    """Pathway scores (method v3): per well, the mean over the testable members of (W2 - c) / s (each member on its
    own noise scale, so a few noisy low-count members cannot dominate), robust z over the drug wells of the reliable
    plates, divided by the plate factor; the score's fold change stays the mean member log2FC."""
    wells = T.wells_of(S.sm)
    S.score_members, S.score_low = {}, set()
    for name, members in SCORES.items():
        mem = [g for g in members if g in S.RES and S.status.get(g) == "testable"]
        if not mem:                                        # only low-count members: kept, flagged 'low counts'
            mem = [g for g in members if g in S.RES]
            if mem:
                S.score_low.add(name)
        S.score_members[name] = mem
        if not mem:
            S.skipped[name] = "no member gene is expressed"
            continue
        M = pd.concat({g: S.WS[g]["W2"] for g in mem}, axis=1)
        Zm = pd.concat({g: (S.WS[g]["W2"] - S.CAL[g]["null_center"]) / S.CAL[g]["null_scale"] for g in mem}, axis=1)
        Pe = pd.concat({g: S.WS[g]["slot_effect"] for g in mem}, axis=1)
        Pu = pd.concat({g: S.WS[g]["position_correction_uncertain"].astype(float) for g in mem}, axis=1)
        W = wells.reindex(M.index).copy()
        W["W2"] = M.mean(axis=1)
        W["member_z"] = Zm.mean(axis=1)
        W["position_effect_removed"] = Pe.mean(axis=1)
        W["position_correction_uncertain"] = Pu.mean(axis=1) >= 0.5      # most members left uncorrected
        c, s = T.robust_center_scale(W.loc[T.reference_wells(W), "member_z"])
        W["plate_scale"] = S.M.well_factor(2, W.index)
        W["plate_scale_gene"] = S.M.factor_for(W["member_z"], c, name)   # the score's own spread per plate group
        W["z"] = (W["member_z"] - c) / (s * W["plate_scale_gene"])
        W = W.join(S.ctx.drop(columns=[x for x in S.ctx.columns if x in W]), how="left")
        vals = ["W2", "member_z", "position_effect_removed", "position_correction_uncertain", "plate_scale_gene"] + \
            [x for x in S.ctx.columns if x in W and x not in ("position_effect_removed",)]
        res = T.per_dose_table(W, list(dict.fromkeys(vals))).rename(columns={"W2": "log2FC"})
        lf = pd.concat([S.RES[g][["drug", "conc", "log2FC_corrected", "z_corrected"]].assign(gene=g) for g in mem])
        idx = pd.MultiIndex.from_arrays([res["drug"], res["conc"]])
        Lm = lf.pivot_table(index=["drug", "conc"], columns="gene", values="log2FC_corrected").reindex(idx)
        Lz = lf.pivot_table(index=["drug", "conc"], columns="gene", values="z_corrected").reindex(idx)[Lm.columns]
        arr, za, gcols = Lm.to_numpy(dtype=float), Lz.to_numpy(dtype=float), list(Lm.columns)
        order = np.argsort(-np.abs(np.nan_to_num(za)), axis=1)[:, :3]   # ranked by the member's own z
        res["top_members"] = ["; ".join(f"{gcols[j]} {2 ** arr[i, j]:.2f}x z {za[i, j]:.1f}" for j in order[i]
                                        if np.isfinite(arr[i, j]) and np.isfinite(za[i, j])) for i in range(len(res))]
        res["n_members"] = len(mem)
        S.SW[name] = W
        S.SC[name] = finish_score(res, name, S.drugs, S.M)
        if name in S.score_low:                            # pseudocount-dominated members: shutdown wells look 'up'
            S.SC[name]["flags"] = ["; ".join(x for x in (f, "low counts") if x) for f in S.SC[name]["flags"]]
    for m in MODULES:                                      # T's summed modules, from their own drug-effect tables
        if m in S.RES:
            r = S.RES[m].rename(columns={"log2FC_corrected": "log2FC", "z_corrected": "z"})
            keep = ["drug", "conc", "log2FC", "z", "position_effect_removed", "position_correction_uncertain",
                    "wells", "plates", "unreliable_plate_only", "n_wells_left_out_unreliable"] + \
                [c for c in S.ctx.columns if c in r]
            r = r[[c for c in dict.fromkeys(keep) if c in r]].copy()
            r["top_members"] = "(summed module)"
            r["n_members"] = len(S.modules.get(m, []))
            S.SW[m] = S.WS[m]
            S.SC[m] = finish_score(r, m, S.drugs, S.M)
    long = pd.concat([t for t in S.SC.values()], ignore_index=True) if S.SC else pd.DataFrame()
    S.save(long, "pathway_scores_by_dose.csv")
    log(f"  scores: {', '.join(f'{k} ({len(v)})' for k, v in S.score_members.items())}")


def finish_score(res, name, drugs, method=None):
    res = res.copy()
    res["fold_change"] = 2.0 ** res["log2FC"]
    res["p_up"] = T.norm_sf(res["z"].values)
    res["p_down"] = T.norm_sf(-res["z"].values)
    res["fdr_up"] = T.bh(res["p_up"].values)
    res["fdr_down"] = T.bh(res["p_down"].values)
    if method is not None:
        res = method.add_dd_columns(res)
    res["flags"] = T.flag_rows(res, name)
    res = dose_columns(res, "z", "p_up", "p_down")
    res = res.join(drugs[[c for c in ("moa_fine", "targets") if c in drugs]], on="drug")
    res.insert(0, "score", name)
    lead = ["score", "drug", "conc", "fold_change", "log2FC", "z", "fdr_up", "fdr_down", "z_by_dose", "dose_pattern_up",
            "dose_pattern_down", "fdr_drug_up", "fdr_drug_down", "n_members", "top_members", "flags"]
    return res[[c for c in lead if c in res] + [c for c in res.columns if c not in lead]].sort_values(
        "z", ascending=False)


def step_context(S):
    """Per drug-dose context (module scores, cell loss, transcription, cell cycle) joined onto every gene table."""
    Wc = T.wells_of(S.sm).join(S.ctx, how="left")
    for v in CTX_VARS:                                     # robust z per variable (reliable plates); Stouffer per
        c, s = T.robust_center_scale(Wc.loc[T.reference_wells(Wc), v])   # drug-dose in per_dose_table
        Wc[f"{v}_z"] = (Wc[v] - c) / s
    Wc["z"] = 0.0
    ct = T.per_dose_table(Wc, [c for c in S.ctx.columns] + [f"{v}_z" for v in CTX_VARS]).drop(columns=["z"])
    for m in CONTEXT_SCORES:
        if m in S.SC:
            t = S.SC[m][["drug", "conc", "log2FC", "z"]].drop_duplicates(["drug", "conc"])
            ct = ct.drop(columns=[c for c in (f"{m}_log2FC", f"{m}_z") if c in ct])
            ct = ct.merge(t.rename(columns={"log2FC": f"{m}_log2FC", "z": f"{m}_z"}), on=["drug", "conc"], how="left")
    ct = S.M.add_dd_columns(ct)
    ct["flags"] = T.flag_rows(ct, "")
    ct["context"] = context_text(ct)
    ct = ct.join(S.drugs[[c for c in ("moa_fine", "targets") if c in S.drugs]], on="drug")
    lead = ["drug", "conc", "flags", "context"] + CTX_VARS
    ct = ct[[c for c in lead if c in ct] + [c for c in ct.columns if c not in lead]]
    S.ctab = ct
    S.save(ct.sort_values(["drug", "conc"]), "drug_context_by_dose.csv")
    cols = [c for c in ct.columns if c.endswith("_log2FC") or (c.endswith("_z") and c[:-2] in CONTEXT_SCORES)]
    if "PSMD10" in S.RES and "PROTEASOME_z" in S.RES["PSMD10"]:   # T's plate mean (its flags used it); the context
        S.RES["PSMD10"] = S.RES["PSMD10"].rename(columns={         # below gets the Stouffer z like every other gene
            "PROTEASOME_z": "PROTEASOME_z_plate_mean", "PROTEASOME_log2FC": "PROTEASOME_log2FC_plate_mean"})
    for gname, res in list(S.RES.items()):
        add = [c for c in cols if c not in res]
        r = res.merge(ct[["drug", "conc"] + add].drop_duplicates(["drug", "conc"]), on=["drug", "conc"], how="left")
        r["context"] = context_text(r, skip={s for s, m in SCORES.items() if gname in m} | {gname})
        S.RES[gname] = r


def safe_for_summary(res):
    """T.drug_summary needs whole numbers of lines: drug-doses with no measurable line get 0 instead of NaN."""
    r = res.copy()
    for c in ["n_lines", "n_lines_up", "n_lines_down", "frac_lines_positive", "frac_lines_negative"]:
        if c in r:
            r[c] = r[c].fillna(0)
    return r


def step_gene_tables(S):
    """results/<GENE>_drug_effects_by_dose.csv and <GENE>_drug_summary.csv; context_genes_top.csv."""
    S.DS = {}
    for g in S.main:
        if g not in S.RES:
            continue
        res = S.RES[g]
        res.sort_values("z_corrected", ascending=False).to_csv(os.path.join(S.R, f"{g}_drug_effects_by_dose.csv"),
                                                                index=False)
        ds = T.drug_summary(safe_for_summary(res))
        cmap = dict(zip(zip(res["drug"], res["conc"]), res["context"]))
        ds["up_context"] = [cmap.get((d, c), "") for d, c in zip(ds["drug"], ds["best_up_dose"])]
        ds["down_context"] = [cmap.get((d, c), "") for d, c in zip(ds["drug"], ds["best_down_dose"])]
        S.DS[g] = ds
        ds.to_csv(os.path.join(S.R, f"{g}_drug_summary.csv"), index=False)
    rows = []
    for g in S.ctx_genes:
        if g not in S.RES:
            rows.append({"gene": g, "gene_set": S.set_of.get(g, ""), "status": S.status.get(g, "")})
            continue
        r = S.RES[g].sort_values("z_corrected", ascending=False)

        def fmt(t):
            return "; ".join(f"{d} {c:g} ({fc:.2f}x, z {z:.1f})" for d, c, fc, z in
                             zip(t["drug"], t["conc"], t["fold_change"], t["z_corrected"]))
        rows.append({"gene": g, "gene_set": S.set_of.get(g, ""), "status": S.status.get(g, ""),
                     "n_lines_expressing": int(S.E[g].sum()), "median_line_cpm": S.med.get(g, np.nan),
                     "top_up": fmt(r.head(3)), "top_down": fmt(r.tail(3).iloc[::-1]),
                     "n_calls_up": int((r["call"] == "up").sum()), "n_calls_down": int((r["call"] == "down").sum())})
    S.save(pd.DataFrame(rows), "context_genes_top.csv")


def step_ferro_context(S):
    """FERRO_MARKERS per drug-dose with the programs that rose with them (context, not a verdict: CHAC1 and SLC7A11
    are ATF4 targets - cystine starvation raises them through the ISR -, SLC7A11 is an NRF2 target, PTGS2 is
    NF-kB-inducible). Artifact flags come first."""
    t = S.SC["FERRO_MARKERS"].copy()
    ct = S.ctab[["drug", "conc"] + [c for c in S.ctab.columns if c.split("_")[0] in FERRO_CONTEXT_PREFIX
                                    and (c.endswith("_z") or c.endswith("_log2FC"))]]
    t = t.merge(ct.drop_duplicates(["drug", "conc"]), on=["drug", "conc"], how="left")
    read = []
    for r in t.to_dict("records"):
        fdr = r.get("fdr_up", np.nan)
        if not (r["z"] >= 3 and fdr < T.FDR_CUT):
            read.append("")
            continue
        fl = str(r.get("flags", "") or "")
        art = [f for f in ("toxic", "transcription drop", "cell-cycle shift") if f in fl]
        if art:
            read.append("markers with " + " / ".join(art) + " (artifact likely)")
            continue
        with_ = [m for m in FERRO_CONTEXT if (r.get(f"{m}_z", np.nan) or 0) >= CONTEXT_Z]
        notes = [FERRO_NOTES[m] for m in with_ if m in FERRO_NOTES]
        read.append("markers with " + " + ".join(with_) + (f" ({'; '.join(notes)})" if notes else "") if with_ else
                    "markers without ISR / NRF2 / UPR / heat shock / NF-kB (not explained by these programs)")
    t["reading"] = read
    lead = ["drug", "conc", "fold_change", "z", "fdr_up", "reading", "top_members"] + \
        [f"{m}_z" for m in FERRO_CONTEXT] + ["ISR_log2FC", "NRF2_log2FC", "flags", "z_by_dose", "dose_pattern_up"]
    t = t[[c for c in lead if c in t] + [c for c in t.columns if c not in lead and c != "score"]]
    S.ferro = t.sort_values("z", ascending=False)
    S.save(S.ferro, "ferro_markers_with_context.csv")


# ============================================================================= p53
def p53_matrix(S):
    """Per (well, line): mean corrected shift r2 of the P53_ACTIVITY genes the line expresses."""
    mem = [g for g in S.score_members.get("P53_ACTIVITY", []) if g in S.R2]
    if not mem:
        raise ValueError("no P53_ACTIVITY gene has drug effects")
    idx = S.sm["sample"].tolist()
    lines = list(S.base.index)
    stack = np.stack([S.R2[g].reindex(index=idx, columns=lines).to_numpy(dtype=float) for g in mem])
    return pd.DataFrame(np.nanmean(stack, axis=0), index=idx, columns=lines), mem


def step_p53(S):
    P, mem = p53_matrix(S)
    S.P53 = P
    base = S.base
    wt = [c for c in P.columns if base.at[c, "tp53_group"] == "WT"]
    alt = [c for c in P.columns if base.at[c, "tp53_group"] == "altered"]
    S.p53_groups = (wt, alt)
    if len(wt) < 2 or len(alt) < 2:
        raise ValueError(f"needs >= 2 TP53-wild-type and >= 2 TP53-altered lines (have {len(wt)} and {len(alt)}; "
                         "without cell-line metadata set them with --tp53-wt / --tp53-altered)")
    W = T.wells_of(S.sm).reindex(P.index).copy()
    W["wt_mean"] = P[wt].mean(axis=1)
    W["altered_median"] = P[alt].median(axis=1)
    W["delta"] = W["wt_mean"] - W["altered_median"]
    W["n_wt_lines"] = P[wt].notna().sum(axis=1)
    W["n_altered_lines"] = P[alt].notna().sum(axis=1)
    eff, _ = T.loo_slot(W["delta"].values, W["slot"].values, W["drug"].values, ~W["is_dmso"].values)
    W["position_effect_removed"] = eff
    W["delta_corrected"] = W["delta"] - eff
    c, s = T.robust_center_scale(W.loc[T.reference_wells(W), "delta_corrected"])
    W["plate_scale"] = S.M.well_factor(2, W.index)        # the genes' plate factors: a noisy plate widens it too,
    W["plate_scale_gene"] = S.M.factor_for(W["delta_corrected"], c, "P53_WT_VS_ALTERED")   # and its own spread
    W["z"] = (W["delta_corrected"] - c) / (s * W["plate_scale_gene"])
    W = W.join(S.ctx.drop(columns=[x for x in S.ctx.columns if x in W]), how="left")
    vals = ["delta_corrected", "delta", "wt_mean", "altered_median", "position_effect_removed", "n_wt_lines",
            "n_altered_lines", "plate_scale", "plate_scale_gene"] + [c for c in S.ctx.columns
                                                 if c in W and c not in ("cells", "plate_scale")]
    res = T.per_dose_table(W, vals)
    res["p_wt_more"] = T.norm_sf(res["z"].values)
    res["fdr"] = T.bh(res["p_wt_more"].values)
    res = S.M.add_dd_columns(res)
    res["flags"] = T.flag_rows(res, "")
    res = res.rename(columns={"delta_corrected": "extra_log2_p53_induction_in_WT", "z": "z_wt_more",
                              "wt_mean": "wt_mean_log2", "altered_median": "altered_median_log2"})
    res = T.add_dose_columns(res, "z_wt_more", "p_wt_more", "up")
    sc = S.SC["P53_ACTIVITY"][["drug", "conc", "fold_change", "z"]].rename(
        columns={"fold_change": "all_lines_P53_ACTIVITY_fold_change", "z": "all_lines_P53_ACTIVITY_z"})
    res = res.merge(sc.drop_duplicates(["drug", "conc"]), on=["drug", "conc"], how="left")
    # a high z_wt_more can also mean that the altered lines FELL more than the WT lines rose (p53-dependent sparing
    # under a global drop): 'WT induction' only when the WT lines rose >= 1.2x and the all-line P53 score went up
    res["pattern"] = np.where((res["wt_mean_log2"] >= T.LFC_MIN) & (res["all_lines_P53_ACTIVITY_z"] > 0),
                              "WT induction", "relative (altered lines fall)")
    res = res.join(S.drugs[[c for c in ("moa_fine", "targets") if c in S.drugs]], on="drug")
    lead = ["drug", "conc", "extra_log2_p53_induction_in_WT", "z_wt_more", "fdr", "pattern", "fdr_drug", "z_by_dose",
            "dose_pattern", "wt_mean_log2", "altered_median_log2", "all_lines_P53_ACTIVITY_fold_change",
            "all_lines_P53_ACTIVITY_z", "flags"]
    S.p53wt = res[[c for c in lead if c in res] + [c for c in res.columns if c not in lead]].sort_values(
        "z_wt_more", ascending=False)
    S.save(S.p53wt, "p53_wt_vs_altered.csv")
    log(f"  p53 WT vs altered: {len(wt)} vs {len(alt)} lines, {len(mem)} p53 target genes; top: "
        + "; ".join(f"{d} {c:g} (z {z:.1f})" for d, c, z in S.p53wt[["drug", "conc", "z_wt_more"]].head(3).values))


def step_p53_function(S):
    """Functional p53 status per line: responsiveness to the strongest non-toxic p53 activators (genotype-blind)."""
    P, base = S.P53, S.base
    sc = S.SC["P53_ACTIVITY"]
    fl = sc["flags"].fillna("").astype(str).str.split("; ")
    bad = fl.map(lambda x: "toxic" in x or "unreliable plate only" in x)   # v3 'toxic': dose-consistent cell loss
    ok = sc[~bad & np.isfinite(sc["z"])].sort_values("z", ascending=False)
    ref = ok[ok["fdr_up"] < T.FDR_CUT].head(N_P53_DOSES)            # significant doses only (noise dilutes)
    S.p53_ref_rule = (f"the {len(ref)} strongest non-toxic P53_ACTIVITY drug-doses with FDR < {T.FDR_CUT:g} (not on "
                      "unreliable plates only)")
    if len(ref) < 3:
        ref = ok.head(N_P53_DOSES)
        S.p53_ref_rule = (f"the {len(ref)} strongest non-toxic P53_ACTIVITY drug-doses (fewer than 3 with FDR < "
                          f"{T.FDR_CUT:g}; not on unreliable plates only)")
    log(f"  p53 reference doses: {S.p53_ref_rule}")
    S.p53_ref = ref
    S.save(ref[["drug", "conc", "fold_change", "z", "fdr_up", "flags", "wells", "plates"]], "p53_reference_doses.csv")
    keys = set(zip(ref["drug"], ref["conc"]))
    Wd = T.wells_of(S.sm)
    Wd = Wd[~Wd["is_dmso"]].assign(dose=lambda x: T.dose_key(x))
    used = set(Wd.index[T.used_wells(Wd)])                 # the drug-doses' used wells (not their plate-13 wells)
    sel = [(s, (d, c)) for s, d, c, dm in zip(S.sm["sample"], S.sm["drug"], S.sm["conc"], S.sm["is_dmso"])
           if (d, c) in keys and not dm and s in used]
    Ps = P.reindex([s for s, _ in sel])
    resp = Ps.mean(axis=0)
    nw = Ps.notna().sum(axis=0)
    # SE of the responsiveness: residuals of a rank-1 fit (well strength x line response) of the per-well-centred
    # scores, so the spread between weaker and stronger reference doses does not count as noise for responding lines
    R = Ps.sub(Ps.median(axis=1), axis=0)
    Rm = R.to_numpy(dtype=float)
    fin = np.isfinite(Rm)
    r = np.nan_to_num(np.nanmean(np.where(fin, Rm, np.nan), axis=0))
    num = np.where(fin, np.nan_to_num(Rm) * r[None, :], 0).sum(axis=1)
    den = np.where(fin, r[None, :] ** 2, 0).sum(axis=1)
    sj = np.where(den > 0, num / np.where(den > 0, den, 1), np.nan)
    sj = sj / np.nanmean(sj) if np.isfinite(sj).any() and np.nanmean(sj) > 0 else np.ones(len(sj))
    E = np.where(fin, Rm - np.nan_to_num(sj, nan=1.0)[:, None] * r[None, :], np.nan)
    with np.errstate(invalid="ignore", divide="ignore"):
        se = pd.Series(np.nanstd(E, axis=0, ddof=1) / np.sqrt(fin.sum(axis=0)), index=R.columns)
    dose_of = pd.Series([k for _, k in sel], index=Ps.index)
    nd = pd.Series({c: dose_of[Ps[c].notna().to_numpy()].nunique() for c in Ps.columns}, dtype=float)
    mem = [g for g in S.score_members["P53_ACTIVITY"] if f"{g}_cpm_dmso" in base]
    basal = basal_activity(S, mem)
    t = pd.DataFrame({"cell_name": S.name, "organ": base["Organ"], "tp53_annotation": base["tp53_status"],
                      "tp53_changes": base["tp53_changes"], "cdkn2a_deleted": base["cdkn2a_deleted"],
                      "mtap_null": base["MTAP_null"], "basal_p53_activity_log2": basal,
                      "p53_responsiveness_log2": resp.reindex(base.index),
                      "p53_responsiveness_se": se.reindex(base.index), "n_reference_wells": nw.reindex(base.index),
                      "n_reference_doses": nd.reindex(base.index)})
    t.index.name = "cell_line_id"
    t["responsiveness_rank"] = t["p53_responsiveness_log2"].rank(ascending=False)
    wt = t.loc[base["tp53_group"] == "WT", "p53_responsiveness_log2"]
    alt = t.loc[base["tp53_group"] == "altered", "p53_responsiveness_log2"]
    S.p53_auc = auc(wt, alt)
    if wt.notna().sum() >= 2 and alt.notna().sum() >= 2:
        cut = (wt.median() + alt.median()) / 2
    else:
        cut = 0.5 * t["p53_responsiveness_log2"].quantile(0.9)
    S.p53_cut = cut
    v = t["p53_responsiveness_log2"]
    near = ((v - cut).abs() < 2 * t["p53_responsiveness_se"]).fillna(False).to_numpy(dtype=bool)
    t["functional_call"] = np.where(v.isna(), "not measured", np.where(near, "uncertain (within 2 SE of the cut)",
                                                                       np.where(v >= cut, "responsive",
                                                                                "unresponsive")))
    grp = base["tp53_group"]
    t["discordant"] = np.where((grp == "WT") & (t["functional_call"] == "unresponsive"),
                               "annotated wild type but unresponsive",
                               np.where((grp == "altered") & (t["functional_call"] == "responsive"),
                                        "TP53 altered but responsive", ""))
    if "PSMD10_cpm_dmso" in base:
        t["PSMD10_cpm_dmso"] = base["PSMD10_cpm_dmso"]
    S.p53f = t.sort_values("p53_responsiveness_log2", ascending=False)
    S.save(S.p53f, "p53_functional_status.csv", index=True)
    log(f"  p53 responsiveness: AUC WT vs altered {fnum(S.p53_auc[0])} (p {fnum(S.p53_auc[1], '{:.2g}')}); "
        f"discordant lines: {int((t['discordant'] != '').sum())}")


def basal_activity(S, members, C=None):
    """Per line, untreated (DMSO; or the levels C given): mean over the expressed members of log2(cpm / median
    line)."""
    if not members:
        return pd.Series(np.nan, index=S.base.index)
    Cd = (S.Cd if C is None else C)[members]
    med = Cd[S.enough.to_numpy()].median()
    L = np.log2((Cd + 0.5) / (med + 0.5))
    return L.where(S.E[members]).mean(axis=1)


# ============================================================================= growth: group screens
def group_growth_screen(n, base, sm, drugs, ctx, group, rest, per_line_max=PER_LINE_MAX):
    """T.mtap_null_screen for any group of lines vs reference lines in the same wells, with the same statistics
    (mean of the group minus median of the reference, counting variance, tissue-matched delta, leave-drug-out
    position correction, well noise + counting noise z, Stouffer per drug-dose, FDR, drug-level FDR). With
    group = MTAP-null lines and rest = the other lines it reproduces T.mtap_null_screen."""
    wells = T.wells_of(sm)
    grp = set(group) & set(base.index)
    ref = set(rest) & set(base.index)
    A = n.pivot_table(index="sample", columns="cell_line_id", values="A")
    V = n.pivot_table(index="sample", columns="cell_line_id", values="varA")
    nl = [c for c in A.columns if c in grp]
    il = [c for c in A.columns if c in ref]
    if not nl or len(il) < 2:
        raise ValueError(f"needs >= 1 group line and >= 2 reference lines with growth data (have {len(nl)}, "
                         f"{len(il)})")
    W = wells.reindex(A.index).copy()
    W["group_mean_log2"] = A[nl].mean(axis=1)
    W["rest_median_log2"] = A[il].median(axis=1)
    W["delta"] = W["group_mean_log2"] - W["rest_median_log2"]
    k, m = max(len(nl), 1), max(len(il), 1)
    W["delta_counting_var"] = V[nl].sum(axis=1) / k ** 2 + (math.pi / 2) * V[il].sum(axis=1) / m ** 2
    organ = base.get("Organ", pd.Series("", index=base.index)).fillna("")
    parts, wts = [], []
    for o in sorted(set(organ[list(grp)])):
        if not o:
            continue
        on = [c for c in nl if organ.get(c, "") == o]
        oi = [c for c in il if organ.get(c, "") == o]
        if on and len(oi) >= 2:
            parts.append(A[on].mean(axis=1) - A[oi].median(axis=1))
            wts.append(len(on))
    if parts:
        W["delta_tissue_matched"] = sum(p * w for p, w in zip(parts, wts)) / sum(wts)
    eff, _n_used = T.loo_slot(W["delta"].values, W["slot"].values, W["drug"].values, ~W["is_dmso"].values)
    W["position_effect_removed"] = eff
    W["delta_corrected"] = W["delta"] - eff
    drug_w = T.reference_wells(W)                       # drug wells on reliable plates (as T.mtap_null_screen)
    c, s = T.robust_center_scale(W.loc[drug_w, "delta_corrected"])
    typical_count_var = float(np.nanmedian(W.loc[drug_w, "delta_counting_var"]))
    well_var = max(s ** 2 - typical_count_var, (0.25 * s) ** 2)
    W["z"] = (W["delta_corrected"] - c) / np.sqrt(well_var + W["delta_counting_var"])
    W = W.join(ctx[["cells_log2_vs_plate"]], how="left")
    names = base.get("cell_name", pd.Series(index=base.index, dtype=object)).fillna("")
    per = []
    if len(nl) <= per_line_max:
        for cid in nl:
            col = f"{names.get(cid) or cid}_log2"
            W[col] = A[cid]
            per.append(col)
    vals = ["delta_corrected", "delta", "group_mean_log2", "rest_median_log2", "position_effect_removed",
            "cells_log2_vs_plate"] + (["delta_tissue_matched"] if "delta_tissue_matched" in W else []) + per
    res = T.per_dose_table(W, vals)
    res["p_selective"] = T.norm_sf(-res["z"].values)
    res["fdr_selective"] = T.bh(res["p_selective"].values)
    res = res.join(drugs, on="drug")
    res = res.rename(columns={"z": "z_selective", "delta_corrected": "extra_log2_depletion",
                              "cells_log2_vs_plate": "all_cells_log2_vs_plate"})
    res = T.add_dose_columns(res, "z_selective", "p_selective", "down")
    res["n_group_lines"] = len(nl)
    res["n_reference_lines"] = len(il)
    lead = ["drug", "conc", "extra_log2_depletion", "z_selective", "fdr_selective", "fdr_drug", "z_by_dose",
            "dose_pattern", "delta_tissue_matched", "group_mean_log2", "rest_median_log2", "all_cells_log2_vs_plate"]
    res = res[[c for c in lead if c in res] + [c for c in res.columns if c not in lead]]
    return res.sort_values("z_selective"), W, sorted(nl), sorted(il)


def mtap_null_screen(S):
    """The earlier MTAP-null screen through group_growth_screen, written with T's column names."""
    nl = S.base.index[S.base["MTAP_null"]]
    il = S.base.index[~S.base["MTAP_null"]]
    res, _W, gl, rl = group_growth_screen(S.n, S.base, S.sm, S.drugs, S.ctx, nl, il)
    res = res.rename(columns={"extra_log2_depletion": "extra_log2_depletion_of_MTAP_null",
                              "group_mean_log2": "null_mean_log2", "rest_median_log2": "intact_median_log2"})
    tgt = res.get("targets", pd.Series("", index=res.index)).fillna("").astype(str).str.upper()
    moa = res.get("moa_fine", pd.Series("", index=res.index)).fillna("").astype(str).str.upper()
    res.insert(8, "PRMT5_or_MAT2A_drug", tgt.str.contains("PRMT5|MAT2A") | moa.str.contains("PRMT5|MAT2A"))
    S.mres, S.mtap_groups = res, (gl, rl)
    S.save(res, "MTAP_null_selective_drugs.csv")


def step_p53_growth(S):
    wt, alt = (list(S.base.index[S.base["tp53_group"] == g]) for g in ("WT", "altered"))
    res, _W, gl, rl = group_growth_screen(S.n, S.base, S.sm, S.drugs, S.ctx, wt, alt, per_line_max=0)
    res = res.rename(columns={"extra_log2_depletion": "extra_log2_depletion_of_TP53_WT",
                              "group_mean_log2": "wt_mean_log2", "rest_median_log2": "altered_median_log2"})
    S.p53g = res
    S.save(res, "p53_wt_selective_growth.csv")


def loss_group(S, g):
    """Lines that have lost a gene most lines express (as tahoe_atlas.angle_focus): below T.null_threshold's gap,
    >= 3 lost lines and >= 3 expressing lines in the growth analysis, and one of: a clean 2x separation; a gap with
    every lost line at the ambient floor (<= 1.5 x af x pooled CPM: they read ambient RNA only, not merely a low
    level); >= 3 lost lines with a deletion driver row for the gene in the cell-line metadata."""
    base = S.base
    lc = S.C[g]
    enough = S.enough
    med = lc[enough].median()
    if not med > 0:
        return None
    ratio = lc / med
    thr, gap = T.null_threshold(ratio[enough])
    use = set(S.n["cell_line_id"].unique()) if getattr(S, "n", None) is not None else set(base.index)
    lost = [c for c in ratio.index[(ratio < thr) & enough] if c in use]
    rest = ratio[(ratio >= thr) & enough & ratio.index.isin(list(use))]
    if len(lost) < 3 or rest.size < 3:
        return None
    clean = bool(ratio[lost].max() < 0.5 * rest.min())
    floor = float(S.ambient.get(g, np.nan))                # af x pooled CPM (step_expression)
    at_floor = bool(np.isfinite(gap) and np.isfinite(floor) and floor > 0 and lc[lost].max() <= 1.5 * floor)
    n_del = len(set(lost) & getattr(S, "deleted", {}).get(g.upper(), set()))
    rule = "clean 2x" if clean else "gap at ambient floor" if at_floor else "metadata deletion" if n_del >= 3 else ""
    if not rule:
        return None
    return {"gene": g, "lines": lost, "n_lines": len(lost), "rule": rule, "threshold_vs_median": thr,
            "gap_log2": gap, "clean_2x_separation": clean, "ambient_floor_vs_median": floor / med,
            "n_lines_deleted_in_metadata": n_del,
            "lost_lines_vs_median": "; ".join(f"{S.name[c]} {ratio[c]:.2f}" for c in sorted(lost, key=ratio.get)),
            "lowest_expressing_vs_median": float(rest.min())}


def step_loss(S):
    """Loss groups of panel genes (and CDKN2A/B); selective depletion of the lost lines; re-expression there."""
    groups = []
    for g in [x for x in S.main if x != "MTAP"]:
        if g in S.targets and g in S.C and S.status.get(g) == "testable":
            lg = loss_group(S, g)
            if lg:
                groups.append(lg)
    S.loss = groups
    gt = pd.DataFrame([{**{k: v for k, v in x.items() if k != "lines"},
                        "lines": ", ".join(S.name[c] for c in x["lines"]),
                        "cell_line_ids": ", ".join(x["lines"])} for x in groups],
                      columns=["gene", "n_lines", "lines", "cell_line_ids", "rule", "threshold_vs_median", "gap_log2",
                               "clean_2x_separation", "ambient_floor_vs_median", "n_lines_deleted_in_metadata",
                               "lost_lines_vs_median", "lowest_expressing_vs_median"])
    S.save(gt, "loss_groups.csv")
    lost_of = {x["gene"]: x["lines"] for x in groups}

    def screen(g):
        lost = lost_of[g]
        res = group_growth_screen(S.n, S.base, S.sm, S.drugs, S.ctx, lost, [c for c in S.base.index if c not in
                                                                            set(lost)])[0]
        res.insert(0, "lines", ", ".join(S.name[c] for c in lost))
        res.insert(0, "gene", g)
        return res

    def reexpress(g):
        """Lost lines with a deletion driver row cannot re-express the gene: left out (all of them: one row). The
        deleted lines in the same wells read pure ambient RNA: the comparator when >= 2 of them have data."""
        dele = S.deleted.get(g.upper(), set())
        lost = [c for c in lost_of[g] if c not in dele]
        if not lost:
            return pd.DataFrame([{"gene": g, "lines": ", ".join(S.name[c] for c in lost_of[g]),
                                  "reading": "deleted in the cell-line metadata: re-expression impossible (any rise "
                                             "is ambient RNA)"}])
        res = T.expression_effects(S.wl, S.sm, g, [c for c in S.base.index if c not in set(lost)], S.ctx, S.drugs,
                                   method=S.M, min_lines=1)[0]         # within the lost lines: any one measured
        dl = [c for c in S.base.index if c in dele and S.enough.get(c, False)]
        amb = None
        if len(dl) >= 2:
            amb = T.expression_effects(S.wl, S.sm, g, [c for c in S.base.index if c not in set(dl)], S.ctx, S.drugs,
                                       method=S.M, min_lines=1)[0]
            if not len(amb) or not (amb["n_lines"].fillna(0) >= 2).any():
                amb = None
        return reexpression_table(S, g, lost, res, len(lost_of[g]) - len(lost), amb, dl)
    screens = list(S.attempt_each("loss screen", list(lost_of), screen).values())
    reex = list(S.attempt_each("re-expression in lost lines", list(lost_of), reexpress).values())
    S.loss_res = pd.concat(screens, ignore_index=True) if screens else pd.DataFrame()
    if len(S.loss_res):
        S.loss_res = S.loss_res[[c for c in S.loss_res.columns if not c.endswith("_log2") or c in
                                 ("group_mean_log2", "rest_median_log2")]]
        S.loss_res = S.loss_res.sort_values(["gene", "z_selective"])
    S.save(S.loss_res, "loss_screens.csv")
    S.reex = pd.concat(reex, ignore_index=True) if reex else pd.DataFrame()
    S.save(S.reex, "reexpression_in_silenced_lines.csv")
    log("  loss groups: " + (", ".join(f"{x['gene']} ({x['n_lines']} lines)" for x in groups) or "none"))


def reexpression_table(S, g, lost, res, n_deleted=0, amb=None, deleted_lines=()):
    """Drug effect on a gene measured only in the lines that have lost it (silenced: e.g. GSDME and DNMT
    inhibitors). Ambient RNA from the other lines rises with them, so the comparator is the change in lines that
    read pure ambient RNA: the lines DELETED for the gene in the same wells (amb, when >= 2 have data), else the
    expressing lines. 'Re-expression' needs z >= 3, a rise >= 1.41x and > 2x the comparator's change, FDR < 0.10, no
    toxic / transcription-drop flag, >= max(2, half the lost lines) measured, >= 2 lost lines up, >= 60% of them above
    zero, and a dose pattern that is not inconsistent (e.g. middle dose only; the drug's top dose with its strongest z
    is consistent whatever the lower doses' noise). When the lost lines' untreated level is at the ambient floor
    (median DMSO CPM <= 1.5 x ambient_cpm; with or without deleted lines) or, when >= 2 lines are deleted, inside the
    deleted lines' range, they cannot be told from ambient RNA: 'lost lines read ambient only: not interpretable'."""
    t = res.copy()
    main = S.RES.get(g)
    if main is not None:
        m = main[["drug", "conc", "fold_change", "z_corrected"]].rename(
            columns={"fold_change": "expressing_lines_fold_change", "z_corrected": "expressing_lines_z"})
        t = t.merge(m.drop_duplicates(["drug", "conc"]), on=["drug", "conc"], how="left")
    else:
        t["expressing_lines_fold_change"], t["expressing_lines_z"] = np.nan, np.nan
    if amb is not None:
        m = amb[["drug", "conc", "fold_change", "z_corrected"]].rename(
            columns={"fold_change": "deleted_lines_fold_change", "z_corrected": "deleted_lines_z"})
        t = t.merge(m.drop_duplicates(["drug", "conc"]), on=["drug", "conc"], how="left")
        comp, t["comparator"] = "deleted_lines_fold_change", f"deleted lines ({len(deleted_lines)}: pure ambient)"
    else:
        t["deleted_lines_fold_change"], t["deleted_lines_z"] = np.nan, np.nan
        comp, t["comparator"] = "expressing_lines_fold_change", "expressing lines (fewer than 2 deleted lines)"
    if hasattr(S, "ctab"):
        t = t.merge(S.ctab[["drug", "conc", "context"]].drop_duplicates(["drug", "conc"]), on=["drug", "conc"],
                    how="left")
    t = T.add_dose_columns(t, "z_corrected", "p_up", "up")
    cd = S.Cd[g] if g in S.Cd else pd.Series(dtype=float)
    lost_cpm = float(cd.reindex(lost).median()) if len(lost) else np.nan
    dcpm = cd.reindex(list(deleted_lines)).dropna()
    amb_cpm = float(S.ambient.get(g, np.nan))
    ambient_only = bool(np.isfinite(lost_cpm) and ((np.isfinite(amb_cpm) and lost_cpm <= 1.5 * amb_cpm) or
                                                   (len(dcpm) >= 2 and dcpm.min() <= lost_cpm <= dcpm.max())))
    lf = np.log2(t["fold_change"])
    le = np.log2(t[comp]).fillna(0)
    nmin = max(2, int(math.ceil(len(lost) / 2)))
    fl = t["flags"].fillna("").astype(str).str.split("; ")
    hit = (t["z_corrected"] >= 3) & (lf >= 0.5) & (lf > 2 * le.clip(lower=0) + 0.25)
    # the drug's top dose carrying its strongest z is a top-dose effect, whatever the noise of the lower doses
    # (a z of 2 at 0.05 uM and 1 at 0.5 uM reads 'inconsistent across doses'); a middle-dose-only rise stays out
    g_ = t.groupby("drug")
    top = (t["conc"] >= g_["conc"].transform("max")) & (t["z_corrected"] >= g_["z_corrected"].transform("max"))
    pats = np.where(top & (t["dose_pattern"] == "inconsistent across doses"), "strongest at the top dose",
                    t["dose_pattern"])
    read = []
    for z, h, f, q, n, nu, fp, pat in zip(t["z_corrected"], hit, fl, t["fdr_up"], t["n_lines"], t["n_lines_up"],
                                          t["frac_lines_positive"], pats):
        if not z >= 3:
            read.append("")
            continue
        if ambient_only:
            read.append("lost lines read ambient only: not interpretable")
            continue
        why = [x for x in ("toxic", "transcription drop") if x in f] + \
            ([f"FDR >= {T.FDR_CUT:g}"] if not q < T.FDR_CUT else []) + \
            ([f"only {int(n) if n >= 0 else 0} of {len(lost)} lost lines measured"] if not n >= nmin else []) + \
            ([f"{int(nu) if nu >= 0 else 0} lost line(s) up"] if not nu >= 2 else []) + \
            ([f"dose pattern: {pat}"] if pat == "inconsistent across doses" else [])
        note = "; strongest at the top dose, lower doses noisy" if pat == "strongest at the top dose" else ""
        read.append(f"not interpretable ({', '.join(why)})" if why else
                    f"re-expression in the lost lines (the comparator changes less{note})" if h and fp >= 0.6 else
                    "rises in the lost lines (ambient RNA / toxicity?)" if h else
                    "rises in all lines (ambient RNA follows)")
    t["reading"] = read
    t["lost_lines_median_cpm_dmso"] = lost_cpm
    t["deleted_lines_cpm_dmso_range"] = f"{dcpm.min():.2f}-{dcpm.max():.2f}" if len(dcpm) else ""
    t["ambient_cpm"] = amb_cpm
    t.insert(0, "lines", ", ".join(S.name[c] for c in lost))
    t.insert(0, "gene", g)
    t["n_lost_lines_deleted_left_out"] = n_deleted
    lead = ["gene", "lines", "drug", "conc", "fold_change", "z_corrected", "fdr_up", "reading", "comparator",
            "deleted_lines_fold_change", "deleted_lines_z", "expressing_lines_fold_change", "expressing_lines_z",
            "n_lines", "n_lines_up", "frac_lines_positive", "z_by_dose", "dose_pattern", "flags", "context", "wells",
            "plates", "moa_fine", "targets", "n_lost_lines_deleted_left_out", "lost_lines_median_cpm_dmso",
            "deleted_lines_cpm_dmso_range", "ambient_cpm"]
    return t[[c for c in lead if c in t]].sort_values("z_corrected", ascending=False)


# ============================================================================= growth: level vs growth
def level_screen(n, base, sm, drugs, level, gene="PSMD10", organ=None, g2m=None):
    """T.gankyrin_level_screen for any gene's untreated level (a Series per line), plus a within-lineage version
    (organ effects removed from both rank vectors). g2m: proliferation level per line for the partial correlation
    (default: base['G2M_PHASE_cpm_dmso'], as T). With level = base['PSMD10_cpm_dmso'] it reproduces
    T.gankyrin_level_screen (rho, rho_partial_G2M, z_corrected)."""
    wells = T.wells_of(sm)
    A = n.pivot_table(index="sample", columns="cell_line_id", values="A")
    lines = [c for c in A.columns if c in level.index and np.isfinite(level[c])]
    if len(lines) < MIN_LEVEL_LINES:
        raise ValueError(f"{gene}: only {len(lines)} lines with a level")
    A = A[lines]
    with np.errstate(divide="ignore"):
        x = np.log2(level[lines].values)
    if g2m is None and "G2M_PHASE_cpm_dmso" in base:
        g2m = base["G2M_PHASE_cpm_dmso"]
    gcol = g2m is not None and bool(np.isfinite(g2m.reindex(lines).to_numpy(dtype=float)).all())
    rA = A.rank(axis=1).values
    rx = pd.Series(x).rank().values
    W = wells.reindex(A.index).copy()
    W["rho"] = rowcorr(rA, rx)
    if gcol:
        rg = pd.Series(np.log2(g2m.reindex(lines).values)).rank().values
        G = np.column_stack([np.ones_like(rg), rg])
        P = G @ np.linalg.pinv(G)
        W["rho_partial_G2M"] = rowcorr(rA - rA @ P.T, rx - P @ rx)
    org = organ.reindex(lines).fillna("").astype(str).to_numpy() if organ is not None else np.array([""] * len(lines))
    big = [o for o in pd.unique(org) if o and (org == o).sum() >= 3]
    Dm = np.column_stack([np.ones(len(lines))] + [(org == o).astype(float) for o in big])
    H = Dm @ np.linalg.pinv(Dm)
    W["rho_within_lineage"] = rowcorr(rA - rA @ H, rx - H @ rx)
    for col, zc in (("rho", "z"), ("rho_within_lineage", "z_within")):
        fz = np.arctanh(np.clip(W[col].values, -0.999, 0.999))
        eff, _ = T.loo_slot(fz, W["slot"].values, W["drug"].values, ~W["is_dmso"].values)
        W[f"fisher_corrected_{zc}"] = fz - eff
        c, s = T.robust_center_scale(W.loc[T.reference_wells(W), f"fisher_corrected_{zc}"])
        W[zc] = (W[f"fisher_corrected_{zc}"] - c) / s
    vals = ["rho"] + (["rho_partial_G2M"] if gcol else []) + ["rho_within_lineage"]
    res = T.per_dose_table(W, vals)
    res["z_within_lineage"] = T.per_dose_table(W, ["rho_within_lineage"], zcol="z_within")["z"].values
    res["p"] = 2 * T.norm_sf(np.abs(res["z"].values))
    res["fdr"] = T.bh(res["p"].values)
    res["p_within_lineage"] = 2 * T.norm_sf(np.abs(res["z_within_lineage"].values))
    res["fdr_within_lineage"] = T.bh(res["p_within_lineage"].values)
    res["fdr_drug_within_lineage"] = T.add_dose_columns(res, "z_within_lineage", "p_within_lineage",
                                                        "down")["fdr_drug"].values
    res = res.join(drugs, on="drug").rename(columns={"z": "z_corrected"})
    res["reading"] = np.where(res["z_corrected"] < 0, f"high-{gene} lines depleted more", f"high-{gene} lines spared")
    res = T.add_dose_columns(res, "z_corrected", "p", "down")
    res = res.rename(columns={"dose_pattern": "dose_pattern_depleted_more"})
    lead = ["drug", "conc", "rho", "rho_partial_G2M", "rho_within_lineage", "z_corrected", "z_within_lineage", "fdr",
            "fdr_within_lineage", "fdr_drug", "fdr_drug_within_lineage", "z_by_dose", "dose_pattern_depleted_more",
            "reading"]
    res = res[[c for c in lead if c in res] + [c for c in res.columns if c not in lead]]
    return res.sort_values("z_corrected"), len(lines)


def gene_level(S, g):
    """Untreated level per line: DMSO CPM, or all-wells CPM for lines with < MIN_DMSO_COUNTS counts in DMSO."""
    dm = S.base[f"{g}_cpm_dmso"]
    low = (S.dmso_counts[g] < MIN_DMSO_COUNTS) | ~np.isfinite(dm.astype(float))
    lev = dm.where(~low, S.base[f"{g}_cpm_all_wells"])
    src = "DMSO CPM" + (f"; all-wells CPM for {int(low.sum())} line(s) with < {MIN_DMSO_COUNTS} DMSO counts: "
                        + ", ".join(S.name[c] for c in low.index[low][:8]) + (" ..." if low.sum() > 8 else "")
                        if low.any() else " (every line)")
    return lev, src


def step_levels(S):
    out, tops = [], []
    S.level_src = {}
    genes = [g for g in S.main if g in S.targets and int(S.E[g].sum()) >= MIN_LEVEL_LINES]
    nrf2 = [g for g in CONTEXT["NRF2_CORE"] if g in S.Cd]   # NRF2 activity (KEAP1 acts on the protein), not NFE2L2
    nb, nsrc = basal_activity(S, nrf2), "DMSO"                # mRNA: untreated level of the NRF2 targets
    if np.isfinite(nb).sum() < MIN_LEVEL_LINES:
        nb, nsrc = basal_activity(S, nrf2, S.C), "all wells (too few DMSO counts)"
    if nrf2 and np.isfinite(nb).sum() >= MIN_LEVEL_LINES:
        genes.append(NRF2_LEVEL)

    def one(g):
        if g == NRF2_LEVEL:
            return (level_screen(S.n, S.base, S.sm, S.drugs, 2.0 ** nb, g, S.base["Organ"], S.g2m),
                    f"basal NRF2 target score ({nsrc}: mean log2 of the expressed NRF2_CORE genes vs the median line)")
        lev, src = gene_level(S, g)
        return level_screen(S.n, S.base, S.sm, S.drugs, lev, g, S.base["Organ"], S.g2m), src
    done = S.attempt_each("level vs growth", genes, one)
    for g, ((res, nlines), src) in done.items():
        S.level_src[g] = src
        res = res.rename(columns={"z_corrected": "z"})
        res.insert(0, "gene", g)
        res["n_lines"] = nlines
        res["level_source"] = src
        out.append(res)
        tops.append(res.sort_values("z").head(5))
        tops.append(res.sort_values("z", ascending=False).head(2))
    S.lvl = pd.concat(out, ignore_index=True) if out else pd.DataFrame()
    S.save(S.lvl, "level_vs_growth.csv")
    top = pd.concat(tops, ignore_index=True) if tops else pd.DataFrame()
    if len(top):
        top = by_fdr(top[["gene", "drug", "conc", "rho", "rho_partial_G2M", "rho_within_lineage", "z",
                          "z_within_lineage", "fdr", "fdr_within_lineage", "fdr_drug", "z_by_dose", "reading",
                          "n_lines", "moa_fine"] if "rho_partial_G2M" in top else [c for c in top.columns]])
    S.lvl_top = top
    S.save(top, "level_vs_growth_top.csv")
    log(f"  level vs growth: {len(out)} genes")


# ============================================================================= cell cycle in untreated cells
def _dmso_cells(path, dmso, cols):
    """DMSO rows of one per-cell file: only the 'drug' column is read first; most files have no DMSO cells."""
    try:
        d = pq.read_table(path, columns=["drug"]).column(0)
        if not pc.any(pc.starts_with(pc.utf8_upper(pc.cast(d, "string")), T.DMSO_PREFIX)).as_py():
            return None
        have = set(pq.read_schema(path).names)
        t = pq.read_table(path, columns=[c for c in cols if c in have], filters=[("drug", "in", dmso)])
        return t.to_pandas() if t.num_rows else None
    except Exception as e:  # noqa: BLE001
        log(f"  WARNING: could not read {path}: {e!r}")
        return None


def step_cell_cycle(S):
    """T.cell_cycle_by_line for the panel genes and anchors: in untreated cells, G2M-/S-high vs -low quartiles."""
    files = sorted(glob.glob(os.path.join(S.out, "cells", "*.parquet")))
    dmso = sorted(set(S.sm_all.loc[S.sm_all["is_dmso"], "drug"].astype(str)))
    genes = [g for g in S.main if g in S.targets]
    why = ("no per-cell files in " + os.path.join(S.out, "cells") if not files else
           "no DMSO wells in this extraction" if not dmso else
           "no S_PHASE / G2M_PHASE modules" if not {"S_PHASE", "G2M_PHASE"} <= set(S.cols) else "")
    if why:
        S.notes.append(f"cell cycle in untreated cells ({why})")
        log(f"  cell cycle: not run ({why})")
        return
    cols = ["drug", "cell_line_id", "total_counts", "S_PHASE", "G2M_PHASE"] + genes
    with ThreadPoolExecutor(max(1, min(8, os.cpu_count() or 2))) as ex:
        parts = [p for p in ex.map(lambda f: _dmso_cells(f, dmso, cols), files) if p is not None]
    if not parts:
        S.notes.append("cell cycle in untreated cells (no DMSO cells in the per-cell files)")
        return
    df = pd.concat(parts, ignore_index=True)
    genes = [g for g in genes if g in df]
    df["den"] = df["total_counts"] - df["S_PHASE"] - df["G2M_PHASE"]
    df = df[df["den"] > 0]
    df["cell_line_id"] = df["cell_line_id"].astype(str)
    rows = []
    for cid, x in df.groupby("cell_line_id"):
        if len(x) < 100:
            continue
        r = {"cell_line_id": cid, "n_dmso_cells": len(x)}
        X = x[genes]
        rk = X.div(x["den"], axis=0).rank()
        for score, tag in (("G2M_PHASE", "G2M"), ("S_PHASE", "S")):
            sc = x[score] / x["den"]
            lo, hi = sc.quantile(0.25), sc.quantile(0.75)
            top, bot = sc >= hi, sc <= lo
            a = X[top.values].sum() / x.loc[top, "den"].sum()
            b = X[bot.values].sum() / x.loc[bot, "den"].sum()
            with np.errstate(divide="ignore", invalid="ignore"):
                r[f"log2_{tag}_high_vs_low"] = np.where((a > 0) & (b > 0), np.log2(a / b), np.nan)
            r[f"spearman_vs_{tag}"] = rk.corrwith(sc.rank()).to_numpy()
        rows.append(r)
    if not rows:
        raise ValueError("no line has >= 100 untreated cells")
    long = []
    for r in rows:
        long.append(pd.DataFrame({"cell_line_id": r["cell_line_id"], "gene": genes, "n_dmso_cells": r["n_dmso_cells"],
                                  "log2_G2M_high_vs_low": r["log2_G2M_high_vs_low"],
                                  "log2_S_high_vs_low": r["log2_S_high_vs_low"],
                                  "spearman_vs_G2M": r["spearman_vs_G2M"], "spearman_vs_S": r["spearman_vs_S"]}))
    t = pd.concat(long, ignore_index=True)
    t.insert(1, "cell_name", t["cell_line_id"].map(S.name))
    t["expressed"] = [bool(S.E.at[c, g]) if c in S.E.index else False for c, g in zip(t["cell_line_id"], t["gene"])]
    S.cc = t
    S.save(t, "cell_cycle_by_line.csv")
    e = t[t["expressed"]]
    summ = e.groupby("gene").agg(n_lines=("cell_line_id", "size"),
                                 median_log2_G2M_high_vs_low=("log2_G2M_high_vs_low", "median"),
                                 n_lines_higher_in_G2M=("log2_G2M_high_vs_low", lambda s: int((s > 0).sum())),
                                 median_log2_S_high_vs_low=("log2_S_high_vs_low", "median"),
                                 median_spearman_vs_G2M=("spearman_vs_G2M", "median"),
                                 median_spearman_vs_S=("spearman_vs_S", "median")).reset_index()
    summ["testable"] = summ["gene"].map(lambda g: S.status.get(g) == "testable")
    S.ccs = summ.sort_values(["testable", "median_log2_G2M_high_vs_low"], ascending=False)
    S.save(S.ccs, "cell_cycle_summary.csv")


# ============================================================================= co-regulation across drug wells
def step_coreg(S):
    dw = S.sm.loc[~S.sm["is_dmso"], "sample"]
    feats = {}
    for g in S.main + S.ctx_genes + MODULES:          # low-count genes left out: their W2 follows the pseudocount
        if g in S.WS and (g in MODULES or S.status.get(g) == "testable"):
            feats[g] = S.WS[g]["W2"]
    for name in SCORES:
        if name in S.SW and name not in getattr(S, "score_low", set()):
            feats[name] = S.SW[name]["W2"]
    X = pd.DataFrame(feats).reindex(dw)
    X = X.loc[:, X.notna().sum() >= 10]
    raw = X.corr()
    Z = (X - X.mean()) / X.std().replace(0, 1)
    Z = Z.fillna(0.0).to_numpy()
    U, sv, Vt = np.linalg.svd(Z, full_matrices=False)
    Z1 = Z - sv[0] * np.outer(U[:, 0], Vt[0])
    nrm = np.linalg.norm(Z1, axis=0)
    nrm[nrm == 0] = 1
    Zn = Z1 / nrm
    r1 = pd.DataFrame(Zn.T @ Zn, index=X.columns, columns=X.columns)
    S.save(raw.round(4), "coregulation_matrix.csv", index=True)
    S.save(r1.round(4), "coregulation_matrix_minus_pc1.csv", index=True)
    var = sv ** 2 / (sv ** 2).sum()
    load = pd.Series(Vt[0], index=X.columns)
    sign = 1 if load[load.abs().idxmax()] > 0 else -1
    S.pc1 = {"share": float(var[0]),
             "top": ", ".join(f"{k} {sign * v:+.2f}" for k, v in load.reindex(load.abs().sort_values(
                 ascending=False).index).head(10).items())}
    wl_ = S.sm.set_index("sample").reindex(dw)
    sc = pd.Series(sign * U[:, 0] * sv[0], index=dw.values)
    o = sc.sort_values(ascending=False)
    S.pc1["wells_high"] = "; ".join(f"{wl_.at[s, 'drug']} {wl_.at[s, 'conc']:g}" for s in o.index[:6])
    S.pc1["wells_low"] = "; ".join(f"{wl_.at[s, 'drug']} {wl_.at[s, 'conc']:g}" for s in o.index[::-1][:6])
    rows = []
    for g in S.main:
        if g not in X.columns:
            continue
        own = {s for s, m in SCORES.items() if g in m} | {g}
        a = raw[g].drop(labels=[c for c in own if c in raw.index]).sort_values(ascending=False)
        b = r1[g].drop(labels=[c for c in own if c in r1.index]).sort_values(ascending=False)
        for k in range(min(10, len(a))):
            rows.append({"gene": g, "rank": k + 1, "partner": a.index[k], "r": a.iloc[k],
                         "partner_minus_pc1": b.index[k], "r_minus_pc1": b.iloc[k]})
        for k in range(min(3, len(a))):
            rows.append({"gene": g, "rank": -(k + 1), "partner": a.index[-(k + 1)], "r": a.iloc[-(k + 1)],
                         "partner_minus_pc1": b.index[-(k + 1)], "r_minus_pc1": b.iloc[-(k + 1)]})
    S.coreg = pd.DataFrame(rows)
    S.save(S.coreg, "coregulation_top_partners.csv")


# ============================================================================= earlier run: cross-links
def prior_dir(args):
    p = args.prior
    if p and p.strip().lower() == "none":
        return None
    q = p or os.path.join(args.data, "mtap_gankyrin")
    if os.path.isdir(os.path.join(q, "results")) or os.path.exists(os.path.join(q, "sample_map.csv")):
        return q
    if p:
        log(f"  WARNING: --prior {p}: no MTAP/Gankyrin output there (results/ or sample_map.csv): cross-links use "
            "this run only")
    return None


def _read(path, **kw):
    return pd.read_csv(path, **kw) if os.path.exists(path) else None


def prior_differences(S, P):
    """Why this run and the earlier one cannot give identical numbers ('' when they read the same files with the
    same --min-cells): a --limit-files trial on either side, another file count, another --min-cells."""
    why = []
    jf = os.path.join(P, "extract_info.json")
    if os.path.exists(jf):
        try:
            with open(jf, encoding="utf-8") as fh:
                pi = json.load(fh)
        except (OSError, ValueError):
            pi = {}
        a, b = (S.info.get("n_files"), S.info.get("limit_files") or 0), (pi.get("n_files"), pi.get("limit_files") or 0)
        if None not in (a[0], b[0]) and a != b:
            why.append(f"this run read {a[0]} files" + (" (--limit-files trial)" if a[1] else "") +
                       f", the earlier run {b[0]}" + (" (--limit-files trial)" if b[1] else ""))
    sf = os.path.join(P, "results", "summary.txt")
    if os.path.exists(sf):
        with open(sf, encoding="utf-8", errors="replace") as fh:
            m = re.search(r"Min cells per cell line per well: (\d+)", fh.read())
        if m and int(m.group(1)) != T.MIN_CELLS:
            why.append(f"--min-cells {T.MIN_CELLS} here, {m.group(1)} in the earlier run")
    ri = {}
    try:
        with open(os.path.join(P, "results", "run_info.json"), encoding="utf-8") as fh:
            ri = json.load(fh)
    except (OSError, ValueError):
        pass
    v = int(ri.get("method_version") or 2)                 # runs before v3 wrote no run_info.json
    if v < T.METHOD_VERSION:
        why.append(f"the earlier run used method v{v}, this one v{T.METHOD_VERSION} (README 'Method v3')")
    else:
        if str(ri.get("composition_normalisation", "")).startswith("applied") != (S.ax.get("shift") is not None):
            why.append("composition normalisation applied in one run only")
        if sorted(ri.get("unreliable_plates") or []) != sorted(S.unreliable):
            why.append(f"unreliable plates {', '.join(ri.get('unreliable_plates') or []) or 'none'} in the earlier "
                       f"run, {', '.join(S.unreliable) or 'none'} here")
        if ri.get("plate_scale_source") and ri["plate_scale_source"] != S.M.factor_source or \
                "fitted" in str(ri.get("plate_scale_source", "")):
            why.append("plate factors from other genes (the earlier run fitted them over its own few features)"
                       if "fitted" in str(ri.get("plate_scale_source", "")) else "plate factors from another source")
    return "; ".join(why)


def compare(rows, label, mine, prior, cols, key=("drug", "conc"), why=""):
    """Max |difference| and Spearman between this run's and the earlier run's numbers (same drug-doses). why: the
    reason the runs differ by design (different input), or '' (then 0 is expected)."""
    if mine is None or prior is None:
        rows.append({"category": "reproducibility", "comparison": label, "reading": "not available"})
        return
    cols = [c for c in cols if c[0] in mine and c[1] in prior]
    if not cols or not set(key) <= set(mine) or not set(key) <= set(prior):
        rows.append({"category": "reproducibility", "comparison": label, "reading": "columns missing in one run"})
        return
    m = mine[list(key) + [c[0] for c in cols]].merge(prior[list(key) + [c[1] for c in cols]], on=list(key),
                                                     suffixes=("", "_prior"))
    for a, b in cols:
        x = m[a].astype(float)
        y = m[b + ("_prior" if a == b else "")].astype(float)
        d = float(np.nanmax(np.abs(x - y))) if len(m) else np.nan
        r, n, _ = spearman_p(x, y)
        rows.append({"category": "reproducibility", "comparison": f"{label}: {a}", "n": n,
                     "statistic": "max |difference|", "value": d, "spearman": r,
                     "expected": f"differs by design ({why})" if why else "0 (same data, same code)",
                     "reading": "identical" if d <= 1e-6 else ("near-identical" if r > 0.99 else
                                                               "differs (different input; expected)" if why else
                                                               "differs")})


def step_crosslinks(S):
    rows = []
    P = prior_dir(S.args)
    S.prior = P
    pr = os.path.join(P, "results") if P else None
    dst = os.path.join(S.out, "angles", "crosslinks", "prior")
    shutil.rmtree(dst, ignore_errors=True)                 # never leave an older run's copy behind
    S.prior_why = prior_differences(S, P) if P else ""
    why = S.prior_why
    if why:
        log(f"  cross-links: the earlier run read other input ({why}): its numbers differ by design")
    if P:
        os.makedirs(dst, exist_ok=True)
        for f in glob.glob(os.path.join(pr, "*.csv")) + [os.path.join(pr, x) for x in ("summary.txt",
                                                                                        "README_columns.txt")]:
            if os.path.exists(f):
                shutil.copy2(f, dst)
        sm0 = _read(os.path.join(P, "sample_map.csv"), dtype={"sample": str, "well": str})
        if sm0 is not None:
            m = S.sm_all[["sample", "well"]].merge(sm0[["sample", "well"]], on="sample", suffixes=("", "_prior"))
            same = (m["well"].fillna("") == m["well_prior"].fillna("")).mean() * 100 if len(m) else np.nan
            rows.append({"category": "reproducibility", "comparison": "well positions (sample_map.csv)", "n": len(m),
                         "statistic": "% wells at the same position", "value": same, "expected": "100",
                         "reading": f"{len(S.sm_all) - len(m)} wells only in this run, "
                                    f"{len(sm0) - len(m)} only in the earlier run"})
        b0 = _read(os.path.join(pr, "baseline_by_cell_line.csv"), dtype={"cell_line_id": str})
        if b0 is not None and "MTAP_null" in b0:
            p0 = set(b0.loc[b0["MTAP_null"].astype(str).str.lower() == "true", "cell_line_id"])
            p1 = set(S.null_lines)
            rows.append({"category": "reproducibility", "comparison": "MTAP-null calls", "n": len(p0 | p1),
                         "statistic": "lines called in both / either", "value": len(p0 & p1),
                         "expected": "identical", "reading": "identical" if p0 == p1 else
                         f"only earlier: {', '.join(sorted(p0 - p1))}; only now: {', '.join(sorted(p1 - p0))}"})
        compare(rows, "MTAP drug effects", S.RES.get("MTAP"), _read(os.path.join(pr, "MTAP_drug_effects_by_dose.csv")),
                [("z_corrected", "z_corrected"), ("log2FC_corrected", "log2FC_corrected")], why=why)
        compare(rows, "PSMD10 drug effects", S.RES.get("PSMD10"),
                _read(os.path.join(pr, "Gankyrin_PSMD10_drug_effects_by_dose.csv")),
                [("z_corrected", "z_corrected"), ("log2FC_corrected", "log2FC_corrected")], why=why)
        compare(rows, "MTAP-null screen", getattr(S, "mres", None),
                _read(os.path.join(pr, "MTAP_null_selective_drugs.csv")),
                [("z_selective", "z_selective"), ("extra_log2_depletion_of_MTAP_null",
                                                  "extra_log2_depletion_of_MTAP_null")], why=why)
        lv = S.lvl[S.lvl["gene"] == "PSMD10"] if len(getattr(S, "lvl", [])) else None
        compare(rows, "Gankyrin level screen", lv, _read(os.path.join(pr, "Gankyrin_level_vs_drug_response.csv")),
                [("rho", "rho"), ("rho_partial_G2M", "rho_partial_G2M"), ("z", "z_corrected")], why=why)
    else:
        rows.append({"category": "reproducibility", "comparison": "earlier MTAP / Gankyrin run",
                     "reading": "not found (--prior); MTAP and PSMD10 were recomputed here with the same code"})
    biology_links(S, rows)
    shared_drugs(S, rows, pr)
    cols = ["category", "comparison", "n", "statistic", "value", "spearman", "rho_within_lineage", "p_within_lineage",
            "auc", "p", "p_bh", "expected", "reading"]
    S.xl = pd.DataFrame(rows).reindex(columns=cols)
    bio = (S.xl["category"] == "biology").to_numpy()          # BH over the biology comparisons, on the p that is
    if bio.any():                                             # read: within lineage for correlations, else the test's
        pr = pd.to_numeric(S.xl.loc[bio, "p_within_lineage"], errors="coerce").fillna(
            pd.to_numeric(S.xl.loc[bio, "p"], errors="coerce"))
        S.xl.loc[bio, "p_bh"] = T.bh(pr.to_numpy(dtype=float))
    S.save(S.xl, "crosslinks.csv")


def spearman_within(a, b, organ):
    """Spearman rho with lineage removed (organ effects of organs with >= 3 lines projected out of both rank
    vectors, as level_screen does) and a two-sided p (Fisher z, organ terms taken off the degrees of freedom)."""
    a, b = np.asarray(a, dtype=float), np.asarray(b, dtype=float)
    ok = np.isfinite(a) & np.isfinite(b)
    n = int(ok.sum())
    if n < 4:
        return np.nan, np.nan
    ra, rb = pd.Series(a[ok]).rank().to_numpy(), pd.Series(b[ok]).rank().to_numpy()
    org = pd.Series(np.asarray(organ, dtype=object)[ok]).fillna("").astype(str).to_numpy()
    big = [o for o in pd.unique(org) if o and (org == o).sum() >= 3]
    Dm = np.column_stack([np.ones(n)] + [(org == o).astype(float) for o in big])
    H = Dm @ np.linalg.pinv(Dm)
    xa, xb = ra - H @ ra, rb - H @ rb
    den = math.sqrt(float((xa ** 2).sum() * (xb ** 2).sum()))
    if den == 0:
        return np.nan, np.nan
    r = float(xa @ xb / den)
    df = n - 2 - int(np.linalg.matrix_rank(Dm))
    if df < 1:
        return r, np.nan
    z = math.atanh(max(min(r, 0.999999), -0.999999)) * math.sqrt(df)
    return r, float(2 * T.norm_sf([abs(z)])[0])


def biology_links(S, rows):
    """Hypotheses linking the panel to the earlier MTAP / Gankyrin analysis, across lines. Correlations are read
    within lineage (lineage and KEAP1-mutant lung lines dominate basal NRF2); group contrasts are AUCs."""
    base, f = S.base, getattr(S, "p53f", None)
    wt = (base["tp53_group"] == "WT").to_numpy()
    organ = base["Organ"].to_numpy() if "Organ" in base else np.array([""] * len(base))
    basal_p53 = f["basal_p53_activity_log2"].reindex(base.index) if f is not None else \
        basal_activity(S, [g for g in P53_ACTIVITY if g in S.Cd])
    resp = f["p53_responsiveness_log2"].reindex(base.index) if f is not None else pd.Series(np.nan, index=base.index)
    nrf2 = basal_activity(S, [g for g in CONTEXT["NRF2_CORE"] if g in S.Cd])
    gk = np.log2(base["PSMD10_cpm_dmso"].astype(float) + 0.5) if "PSMD10_cpm_dmso" in base else None

    def corr_row(label, a, b, expected, mask=None):
        mask = np.ones(len(base), bool) if mask is None else np.asarray(mask, bool)
        a, b = np.asarray(a, dtype=float)[mask], np.asarray(b, dtype=float)[mask]
        r, n, p = spearman_p(a, b)
        rw, pw = spearman_within(a, b, organ[mask])
        same = np.isfinite(rw) and (rw < 0) == expected.startswith("neg")
        rows.append({"category": "biology", "comparison": label, "n": n, "statistic": "Spearman rho", "value": r,
                     "rho_within_lineage": rw, "p_within_lineage": pw, "p": p, "expected": expected,
                     "reading": "" if not np.isfinite(rw) else ("consistent (within lineage)" if same and pw < 0.05
                                                                else "same direction (within lineage), not "
                                                                     "significant" if same else
                                                                "not consistent (within lineage)")})
    if gk is not None:
        corr_row("PSMD10 (Gankyrin) baseline vs basal p53 activity, TP53-WT lines", gk, basal_p53,
                 "negative if Gankyrin-MDM2 degradation of p53 (a protein-level mechanism) sets basal target levels: "
                 "a hypothesis", wt)
        corr_row("PSMD10 baseline vs p53 responsiveness to the reference activators, TP53-WT lines", gk, resp,
                 "negative if Gankyrin-MDM2 degradation of p53 limits its induction: a hypothesis", wt)
        corr_row("PSMD10 baseline vs basal NRF2 core activity, all lines", gk, nrf2,
                 "positive if the reported Gankyrin-KEAP1/NRF2 feedback matters; KEAP1-mutant lung lines (e.g. A549, "
                 "NCI-H460; not annotated here) dominate basal NRF2: use the within-lineage rho")

    def group_row(label, v, mask, grp, expected, what):
        v = pd.Series(np.asarray(v, dtype=float), index=base.index)
        mask, grp = np.asarray(mask, bool), np.asarray(grp, bool)
        a, b = v[mask & grp], v[mask & ~grp]
        u, p = auc(a, b)
        rows.append({"category": "biology", "comparison": label, "n": int(a.notna().sum() + b.notna().sum()),
                     "statistic": f"median {what[0]} - {what[1]}",
                     "value": float(a.median() - b.median()) if a.notna().any() and b.notna().any() else np.nan,
                     "auc": u, "p": p, "expected": expected,
                     "reading": f"{int(a.notna().sum())} {what[0]} vs {int(b.notna().sum())} {what[1]} lines"})
    nul = base["MTAP_null"].astype(bool).to_numpy()
    cdk = base["cdkn2a_deleted"].astype(bool).to_numpy()
    low = "possibly slightly lower (hypothesis)"
    nodiff = "no difference (DNA-damage activation of p53 does not need ARF)"
    group_row("CDKN2A-deleted (p16 and ARF lost) vs CDKN2A-present, TP53-WT lines: basal p53 activity", basal_p53, wt,
              cdk, low, ("deleted", "present"))
    group_row("CDKN2A-deleted vs CDKN2A-present, TP53-WT lines: p53 responsiveness", resp, wt, cdk, nodiff,
              ("deleted", "present"))
    group_row("MTAP-null (9p21 proxy) vs MTAP-intact, TP53-WT lines: basal p53 activity", basal_p53, wt, nul, low,
              ("null", "intact"))
    group_row("MTAP-null (9p21 proxy) vs MTAP-intact, TP53-WT lines: p53 responsiveness", resp, wt, nul, nodiff,
              ("null", "intact"))
    for g in ["SLC7A11", "GPX4", "ACSL4", "AIFM2", "CHAC1"]:
        if f"{g}_cpm_dmso" in base and g in S.C:
            lev, _ = gene_level(S, g)
            group_row(f"MTAP-null vs {g} baseline (log2 CPM)", np.log2(lev.astype(float) + 0.5),
                      np.ones(len(base), bool), nul, "speculative: no difference likely (MTAP loss mainly raises MTA; "
                      "in cystine-rich medium any effect on cysteine supply is small)", ("null", "intact"))


def drug_activity(S):
    """How much each drug moves expression: the atlas's genome-wide n_sig_genes (max over doses) when the atlas is
    computed, else the number of this run's testable genes with a call at any dose. (Series drug -> activity,
    source text.)"""
    present = sorted(set(S.sm.loc[~S.sm["is_dmso"], "drug"].astype(str)))
    dd = S.ax.get("drugdose")
    if dd is None and S.atl and atlas_ready(S.atl):
        dd = _read(os.path.join(S.atl, "effects", "drugdose.csv"), dtype={"drug": str})
    if dd is not None and {"drug", "n_sig_genes"} <= set(dd.columns):
        a = pd.to_numeric(dd["n_sig_genes"], errors="coerce").groupby(dd["drug"].astype(str)).max()
        return a.reindex(present).fillna(0), "the atlas's genome-wide significant genes (max over doses)"
    n = pd.Series(0.0, index=present)
    for g, r in S.RES.items():
        if g in MODULES or S.status.get(g) != "testable":
            continue
        hit = set(r.loc[r["call"].isin(["up", "down"]), "drug"].astype(str))
        n[n.index.isin(hit)] += 1
    return n, "the number of this run's genes with a call at any dose"


def stratified_expected(a, b, act, n_bins=10):
    """Drugs expected in both lists by chance when potent drugs are more likely to be in any list: the sum over
    deciles of drug activity of |a in bin| x |b in bin| / |bin|."""
    r = act.rank(method="average")
    bins = pd.qcut(r, min(n_bins, max(1, r.nunique())), labels=False, duplicates="drop") if len(r) else r
    e = 0.0
    for _b, idx in pd.Series(act.index, index=act.index).groupby(bins).groups.items():
        k = set(idx)
        e += len(a & k) * len(b & k) / max(len(k), 1)
    return e


def shared_drugs(S, rows, pr):
    """Drugs in both an MTAP / Gankyrin list (drug-level FDR < 0.10; the earlier run's, else this run's) and a panel
    list (dose-level FDR < 0.10, or a call), with the number expected by chance matched for drug activity (deciles
    of drug_activity): potent drugs appear in nearly every list."""
    prior = {}

    def top_drugs(t, col, asc, k, fdr=None):
        if t is None or col not in t:
            return []
        if fdr and fdr in t:
            t = t[t[fdr] < T.FDR_CUT]
        return list(dict.fromkeys(t.sort_values(col, ascending=asc)["drug"].astype(str)))[:k]
    src = "earlier run" if pr else "this run's MTAP / PSMD10 lists"
    for g, f in (("MTAP", "MTAP_drug_summary.csv"), ("PSMD10", "Gankyrin_PSMD10_drug_summary.csv")):
        t = _read(os.path.join(pr, f)) if pr else S.DS.get(g)
        prior[f"{g} up"] = top_drugs(t, "best_up_z", False, TOP, "fdr_up_drug")
        prior[f"{g} down"] = top_drugs(t, "best_down_z", True, TOP, "fdr_down_drug")
    t = _read(os.path.join(pr, "MTAP_null_selective_drugs.csv")) if pr else getattr(S, "mres", None)
    prior["MTAP-null selective"] = top_drugs(t, "z_selective", True, TOP, "fdr_drug")
    t = _read(os.path.join(pr, "Gankyrin_level_vs_drug_response.csv")) if pr else None
    prior["Gankyrin level: depleted more"] = top_drugs(t, "z_corrected", True, 10, "fdr_drug")
    panel = {}
    for name, t in S.SC.items():
        if name in ("P53_ACTIVITY", "FERRO_MARKERS", "INFLAMMASOME", "NRF2", "ISR", "IFN", "HEAT_SHOCK"):
            panel[f"{name} up"] = top_drugs(t[t["fdr_up"] < 0.1], "z", False, TOP)
    if hasattr(S, "p53wt"):
        panel["p53 WT-selective induction"] = top_drugs(S.p53wt[S.p53wt["fdr"] < 0.1], "z_wt_more", False, TOP)
    if hasattr(S, "p53g"):
        panel["TP53-WT-selective depletion"] = top_drugs(S.p53g[S.p53g["fdr_selective"] < 0.1], "z_selective", True,
                                                         TOP)
    for g in S.panel:
        if g in S.DS and S.status.get(g) == "testable":
            d = S.DS[g]
            panel[f"{g} up"] = list(d[d["up_call"] == "up"].sort_values("best_up_z", ascending=False)["drug"]
                                    .astype(str))[:5]
            panel[f"{g} down"] = list(d[d["down_call"] == "down"].sort_values("best_down_z")["drug"].astype(str))[:5]
    n_drugs = max(1, S.sm.loc[~S.sm["is_dmso"], "drug"].nunique())
    any_prior = {x for v in prior.values() for x in v}
    any_panel = {x for v in panel.values() for x in v}
    act, S.activity_src = drug_activity(S)
    S.shared_expected_naive = len(any_prior) * len(any_panel) / n_drugs
    S.shared_expected = stratified_expected(any_prior, any_panel, act)
    exp = (f"~{S.shared_expected:.1f} drugs shared by chance, matched for drug activity (deciles of "
           f"{S.activity_src}; {S.shared_expected_naive:.1f} if all drugs were alike: {len(any_prior)} x "
           f"{len(any_panel)} / {n_drugs})")
    hits = []
    for d in sorted(any_prior):
        pl = [k for k, v in panel.items() if d in v]
        if pl:
            hits.append((len(pl), d, [k for k, v in prior.items() if d in v], pl))
    S.shared_n = len(hits)
    for npl, d, a, b in sorted(hits, key=lambda t: (-t[0], t[1]))[:25]:
        rows.append({"category": "shared top drugs", "comparison": d, "n": npl,
                     "statistic": f"significant lists ({src})", "value": len(a), "expected": exp,
                     "reading": f"MTAP/Gankyrin: {', '.join(a)} | panel: {', '.join(b)}"})


# ============================================================================= positive controls
READOUT_COLS = ["drug", "conc", "fold_change", "z", "fdr_up", "fdr_down", "z_by_dose", "flags"]


def readout(S, kind, name):
    """Per drug-dose table (READOUT_COLS) for a control's readout, or None when it was not computed."""
    t = _readout(S, kind, name)
    return None if t is None else t.reindex(columns=READOUT_COLS)


def _readout(S, kind, name):
    if kind in ("score",):
        t = S.SC.get(name)
        return None if t is None else t[["drug", "conc", "fold_change", "z", "fdr_up", "fdr_down", "z_by_dose", "flags"]]
    if kind in ("gene", "reexpr"):
        t = None
        if kind == "reexpr" and len(getattr(S, "reex", [])):
            t = S.reex[S.reex["gene"] == name]
            t = t if len(t) else None
        t = S.RES.get(name) if t is None else t
        if t is None:
            return None
        t = t.rename(columns={"z_corrected": "z"})
        if "z_by_dose" not in t:
            t = T.add_dose_columns(t, "z", "fdr_up", "up")
        return t[[c for c in ["drug", "conc", "fold_change", "z", "fdr_up", "fdr_down", "z_by_dose", "flags"] if c in t]]
    if kind == "p53wt":
        t = getattr(S, "p53wt", None)
        if t is None:
            return None
        t = t.rename(columns={"z_wt_more": "z", "fdr": "fdr_up"})
        t["fold_change"] = 2.0 ** t["extra_log2_p53_induction_in_WT"]
        t["fdr_down"] = np.nan
        return t[["drug", "conc", "fold_change", "z", "fdr_up", "fdr_down", "z_by_dose", "flags"]]
    if kind == "ctx":
        t = S.ctab.rename(columns={f"{name}_z": "z"}).copy()
        t["fold_change"] = 2.0 ** t[name]
        t["fdr_up"] = T.bh(T.norm_sf(t["z"].values))
        t["fdr_down"] = T.bh(T.norm_sf(-t["z"].values))
        t = T.add_dose_columns(t, "z", "fdr_down", "down")
        return t[["drug", "conc", "fold_change", "z", "fdr_up", "fdr_down", "z_by_dose", "flags"]]
    return None


def step_controls(S):
    present = sorted(set(S.sm.loc[~S.sm["is_dmso"], "drug"].astype(str)))
    rows = []
    for exp, kind, name, sign, spec, at24 in CONTROLS:
        drugs = find_drugs(present, S.drugs, spec)
        t = readout(S, kind, name)
        low = kind == "reexpr" and len(getattr(S, "reex", [])) and (S.reex["gene"] == name).any()
        what = {"score": f"{name} score", "gene": f"{name} mRNA",
                "reexpr": f"{name} mRNA in the {name}-low lines" if low else
                f"{name} mRNA (expressing lines: no {name}-low group found)",
                "p53wt": "p53 targets, WT minus altered lines", "ctx": "UMIs per cell vs plate"}[kind]
        if not drugs:
            rows.append({"expectation": exp, "expected_at_24h": at24, "readout": what, "drug": "not in data",
                         "verdict": "not in data"})
            continue
        if t is None:
            rows.append({"expectation": exp, "expected_at_24h": at24, "readout": what, "drug": ", ".join(drugs),
                         "verdict": f"not testable ({S.status.get(name, S.skipped.get(name, 'readout missing'))})"})
            continue
        sz = t["z"] * (sign if sign else 1)
        rank = (sz if sign else t["z"].abs()).rank(ascending=False, method="min")
        for d in drugs:
            g = t[(t["drug"] == d) & np.isfinite(t["z"].astype(float))]
            if not len(g):
                rows.append({"expectation": exp, "expected_at_24h": at24, "readout": what, "drug": d,
                             "verdict": "not measured"})
                continue
            k = (g["z"] * sign if sign else g["z"].abs()).idxmax()
            r = t.loc[k]
            dz = r["z"] * sign if sign else abs(r["z"])
            fdr = r["fdr_up"] if (sign > 0 or (sign == 0 and r["z"] > 0)) else r["fdr_down"]
            lf = math.log2(r["fold_change"]) if r["fold_change"] > 0 else np.nan
            big = abs(lf) >= T.LFC_MIN if kind not in ("ctx", "p53wt") else (lf <= -0.5 if kind == "ctx" else True)
            verdict = "clear" if dz >= 3 and fdr < T.FDR_CUT and big else ("weak" if dz >= 2 else "absent")
            rows.append({"expectation": exp, "expected_at_24h": at24, "readout": what, "drug": d, "best_dose": r["conc"],
                         "fold_change": r["fold_change"], "z": r["z"], "fdr": fdr, "rank_among_drug_doses": rank[k],
                         "of": len(t), "z_by_dose": r["z_by_dose"], "flags": r["flags"],
                         "direction": "up" if r["z"] > 0 else "down", "verdict": verdict})
    S.pcs = pd.DataFrame(rows)
    S.save(S.pcs, "positive_controls.csv")


# ============================================================================= quality tables
def step_quality(S):
    genes = [g for g in S.main + S.ctx_genes if g in S.WS]
    pos = pd.concat([T.slot_table(S.WS[g], g) for g in genes])
    pos.index.name = "well"
    S.pos = pos.reset_index()
    S.save(S.pos, "well_position_effects.csv")
    S.plates = pd.concat([T.plate_table(S.WS[g], g) for g in genes]).reset_index()
    S.save(S.plates, "plate_dmso_offsets.csv")
    cal = pd.DataFrame(S.CAL).T
    cal.index.name = "gene"
    S.cal = cal.reset_index()
    S.save(S.cal, "calibration.csv")
    S.save(S.base, "baseline_by_cell_line.csv", index=True)
    ps = T.write_plate_scale(S.M, os.path.join(S.R, "plate_scale.csv"))
    if len(ps):                                    # calibration per plate group, before and after the plate factor
        feats = [g for g in S.WS if g in MODULES or S.status.get(g) == "testable"]
        rows = []
        for g in feats:
            W = S.WS[g]
            dw = ~W["is_dmso"].astype(bool) & W["z"].notna()        # shares of the measured z only
            zu = (W["W2"] - S.CAL[g]["null_center"]) / S.CAL[g]["null_scale"]
            rows.append(pd.DataFrame({"group": S.M.group.reindex(W.index)[dw].values, "zu": zu[dw].values,
                                      "z": W.loc[dw, "z"].values}))
        if rows:
            z = pd.concat(rows, ignore_index=True)
            agg = z.assign(u=z["zu"].abs() > 1.96, s=z["z"].abs() > 1.96, u3=z["zu"].abs() > 3,
                           s3=z["z"].abs() > 3).groupby("group")[["u", "s", "u3", "s3"]].mean() * 100
            agg.columns = ["pct_abs_z_gt_1.96_before_scaling", "pct_abs_z_gt_1.96", "pct_abs_z_gt_3_before_scaling",
                           "pct_abs_z_gt_3"]
            ps = ps.join(agg.round(2), on="group")
            S.save(ps, "plate_scale.csv")
    S.plate_scale_table = ps
    T.write_plate_scale_by_gene(S.M, os.path.join(S.R, "plate_scale_by_gene.csv"))   # each gene's own factor


def replicate_pairs(S):
    """Agreement of the wells of the same drug-dose: Pearson r over the testable genes' per-well z, per well pair,
    with the pair type ('unreliable plate' when either well is on one, 'same plate', 'same position, other plate',
    'different position'). Same-position pairs share any residual position artifact; only different positions are
    independent."""
    feats = [g for g in S.WS if g not in MODULES and S.status.get(g) == "testable"]
    if len(feats) < 10:
        return pd.DataFrame()
    Z = pd.DataFrame({g: S.WS[g]["z"] for g in feats})
    W = T.wells_of(S.sm)
    W = W[~W["is_dmso"]].assign(dose=lambda x: T.dose_key(x))
    nc = S.M.not_correctable().reindex(W.index).fillna(False).astype(bool)
    rows = []
    for (d_, k), g in W.groupby(["drug", "dose"]):
        if len(g) < 2:
            continue
        ss = list(g.index)
        for i in range(len(ss)):
            for j in range(i + 1, len(ss)):
                a, b = ss[i], ss[j]
                if a not in Z.index or b not in Z.index:
                    continue
                x, y = Z.loc[a].to_numpy(dtype=float), Z.loc[b].to_numpy(dtype=float)
                ok = np.isfinite(x) & np.isfinite(y)
                if ok.sum() < 10:
                    continue
                pa, pb = W.at[a, "plate"], W.at[b, "plate"]
                kind = ("unreliable plate" if W.at[a, "unreliable_plate"] or W.at[b, "unreliable_plate"] else
                        "same plate" if pa == pb else
                        "same position, other plate" if W.at[a, "well"] == W.at[b, "well"] else "different position")
                rows.append({"drug": d_, "conc": W.at[a, "conc"], "plate_a": pa, "well_a": W.at[a, "well"],
                             "plate_b": pb, "well_b": W.at[b, "well"], "pair_type": kind, "n_genes": int(ok.sum()),
                             "r": float(np.corrcoef(x[ok], y[ok])[0, 1]),
                             "position_not_correctable": bool(nc.at[a] or nc.at[b])})
    return pd.DataFrame(rows)


def v3_facts(S):
    """The facts of this run the briefs and the summary state (method v3): every one computed from these data."""
    F = {}
    sm_all, sm = S.sm_all, S.sm
    rp = S.attempt("replicate pairs", lambda: replicate_pairs(S))
    S.reps = rp if rp is not None else pd.DataFrame()
    if len(S.reps):
        S.save(S.reps, "replicate_pairs.csv")
        F["replicates"] = T.replicate_text(T.replicate_summary(S.reps))   # each drug-dose counted once
        un = []
        for p in S.unreliable:
            t = S.reps[(S.reps["plate_a"] == p) | (S.reps["plate_b"] == p)]
            un.append(f"{p} ({T.replicate_text(T.replicate_summary(t.assign(pair_type='replicate r with its wells')))})"
                      if len(t) else f"{p} (no replicate pairs)")
        F["unreliable"] = ", ".join(un)
    else:
        F["replicates"] = "not available (fewer than 10 testable genes or no drug-dose with 2 wells)"
        F["unreliable"] = ", ".join(S.unreliable)
    if not S.unreliable:
        F["unreliable"] = "none"
    F["factors"] = T.plate_factor_text(S.M)
    F["factor_source"] = S.M.factor_source
    F["composition"] = S.comp_note
    dm = sm_all[sm_all["is_dmso"]].groupby("plate")["well"].agg(lambda s: "/".join(sorted(map(str, s))))
    if len(dm):
        common = dm.value_counts().index[0]
        other = [f"{p}: {w}" for p, w in dm.items() if w != common]
        F["dmso"] = f"{common} on every plate" + (f" except {'; '.join(other)}" if other else "")
    else:
        F["dmso"] = "none in these data"
    a = sm_all[~sm_all["is_dmso"]].assign(dose=lambda x: T.dose_key(x))
    gone = a.groupby(["drug", "dose"])["sample"].agg(lambda s: set(s) <= set(S.failed["sample"]))
    nd = [f"{d_} {k}" for (d_, k), v in gone.items() if v]
    F["no_data"] = ", ".join(nd) if nd else "none"
    thin = S.line_well_frac[S.line_well_frac < 0.25].sort_values()   # share of wells with a usable profile
    F["thin_lines"] = ", ".join(f"{S.name[c]} ({100 * v:.0f}% of wells)" for c, v in thin.items()) or "none"
    names = sorted(set(sm.loc[~sm["is_dmso"], "drug"].astype(str)))
    base_of = pd.Series([T.salt_base(n).lower() for n in names], index=names)     # one definition (T)
    dup = base_of[base_of.duplicated(keep=False)]
    F["salts"] = (f"{dup.nunique()} drugs appear under two or more names (salt forms), e.g. "
                  + "; ".join(" = ".join(g.index) for _, g in list(dup.groupby(dup))[:4])) if len(dup) else \
        "no drug appears twice under a salt-form name"
    F["mtap_cut"] = S.null_source
    Wc = T.wells_of(S.sm).join(S.ctx[["cells_log2_beyond_row"]], how="left") if "cells_log2_beyond_row" in S.ctx \
        else None
    if Wc is not None:
        Wc = Wc.assign(dose=T.dose_key(Wc))
        Wc = Wc[Wc["is_dmso"].astype(bool) | T.used_wells(Wc).reindex(Wc.index).fillna(True)]
    F["cell_rep"] = T.cell_loss_replication_text(*T.cell_loss_replication(Wc)) if Wc is not None else \
        "how well wells agree on cell loss is not known here: treat a one-well 'toxic' as weak evidence alone"
    nc = S.ctx["position_not_correctable"].reindex(sm.set_index("sample").index[~sm["is_dmso"].to_numpy()])
    ncw = sm.set_index("sample").reindex(nc.index[nc.fillna(False).astype(bool)])
    F["not_correctable"] = (f"{len(ncw)} drug wells (" + ", ".join(sorted({f'{r.drug} {r.conc:g} at {r.well}'
                                                                           for r in ncw.itertuples()})[:6])
                            + (" ..." if len(ncw) > 6 else "") + ")") if len(ncw) else "none"
    F["n_genes"] = (f"{sum(1 for g in S.RES if g not in MODULES)} genes with drug effects, "
                    f"{sum(1 for g in S.main if S.status.get(g) == 'testable')} of the {len(S.main)} panel genes and "
                    "anchors testable")
    return F


def step_well_effects(S):
    """results/well_effects.csv.gz: one row per well with the method-v3 inputs (unreliable plate, plate factor,
    composition shift) and every panel gene's, anchor's, score's and module's corrected log2FC (W2) and z, plus for
    genes and modules the value before the position correction (W1) and its position state (0 corrected,
    1 uncertain: too few clean donors, 2 not correctable), so the method can be checked outside this script."""
    W = T.wells_of(S.sm)
    out = W[["plate", "well", "drug", "conc", "unreliable_plate"]].copy()
    out["plate_scale"] = S.M.well_factor(2, out.index)
    out["composition_shift_log2"] = S.ctx["composition_shift_log2"].reindex(out.index) \
        if "composition_shift_log2" in S.ctx else np.nan
    cols = {}
    for g in S.main + list(SCORES) + MODULES:
        Wg = S.WS.get(g) if g in S.WS else S.SW.get(g)
        if Wg is not None:
            cols[f"{g}_log2FC"] = Wg["W2"].reindex(out.index)
            cols[f"{g}_z"] = Wg["z"].reindex(out.index)
            if "W1" in Wg and "pos_state" in Wg:
                cols[f"{g}_log2FC_uncorrected"] = Wg["W1"].reindex(out.index)
                cols[f"{g}_position_state"] = Wg["pos_state"].reindex(out.index)
    out = pd.concat([out, pd.DataFrame(cols, index=out.index)], axis=1)
    out.index.name = "sample"
    out.reset_index().to_csv(os.path.join(S.R, "well_effects.csv.gz"), index=False, compression="gzip")


def write_panel_run_info(S):
    """results/run_info.json (written last): method version 3 and this run's settings (tahoe_status.py reads it)."""
    T.write_run_info(os.path.join(S.R, "run_info.json"), method_version=PANEL_METHOD,
                     tahoe_mtap_gankyrin_method_version=T.METHOD_VERSION, script=os.path.abspath(__file__),
                     tahoe_mtap_gankyrin=os.path.abspath(T.__file__), data=os.path.abspath(S.args.data),
                     out=os.path.abspath(S.out), min_cells=T.MIN_CELLS, n_files=S.info.get("n_files"),
                     limit_files=S.info.get("limit_files") or 0, unreliable_plates=S.unreliable,
                     composition_normalisation=S.comp_note, plate_scale_source=S.M.factor_source,
                     plate_factors_above_1={g: round(float(f), 4) for g, f in (S.M.factors[2] or {}).items() if f > 1},
                     wells_disagree_from_atlas=S.ax["dd_extra"] is not None, atlas=S.ax["dir"] or None,
                     atlas_effects_version=S.ax["version"], prior=os.path.abspath(S.prior) if S.prior else None,
                     facts=getattr(S, "facts", {}), failed_steps=list(S.failures))


# ============================================================================= summary
def write_summary(S):
    pd.set_option("display.width", 250)
    pd.set_option("display.max_columns", 30)
    pd.set_option("display.max_colwidth", 70)
    L = []

    def say(s=""):
        L.append(s)

    def title(s):
        say()
        say(s)
        say("-" * 100)
    info, wl, sm, base = S.info, S.wl, S.sm, S.base
    say("Tahoe-100M gene panel: ferroptosis, pyroptosis, p53, NAPEPLD and TRIM72 (artifact-corrected), built on the")
    say("MTAP / Gankyrin run")
    say("=" * 100)
    say(f"Cells: {int(wl['n_cells'].sum()):,}   wells: {sm['sample'].nunique()}   plates: {sm['plate'].nunique()}   "
        f"cell lines: {wl['cell_line_id'].nunique()}   (files used: {info['n_files']}"
        + (f", TRIAL limited to {info['limit_files']} files" if info.get("limit_files") else "") + ")")
    say(f"Well position source: {info['well_position_source']}")
    say(f"Min cells per line per well: {T.MIN_CELLS}. Drug call: FDR < {T.FDR_CUT}, >= {2 ** T.LFC_MIN:.1f}x (median "
        f"over lines), >= 60% of lines moving that way. Expressed: >= {EXPR_FRAC:.0%} of the median line, >= "
        f"{MIN_EXPR_CPM:g} CPM and >= {AMBIENT_MULT:g}x the ambient level (all wells).")
    say(f"Ambient RNA: lines read af = {S.af:.3f} of a gene's pooled level without expressing it ({S.af_source}); "
        f"ambient level = af x pooled CPM (panel_genes.csv ambient_cpm).")
    say(f"Failed wells excluded: {len(S.failed)}" + (" -> " + ", ".join(
        f"{r.drug} {r.conc:g} ({r.plate} {r.well}, {int(r.n_cells)} cells)" for r in S.failed.itertuples())
        if len(S.failed) else ""))
    say(f"TP53 annotation (cell-line metadata; any TP53 driver row = altered): {len(S.p53_groups[0]) if hasattr(S, 'p53_groups') else int((base['tp53_group'] == 'WT').sum())} wild type, "
        f"{int((base['tp53_group'] == 'altered').sum())} altered, {int((base['tp53_group'] == '').sum())} unknown. "
        f"MTAP-null: {len(S.null_lines)} lines ({S.null_source}).")
    for nt in S.notes:
        say(f"Not run: {nt}")
    fl = [f"{k}: {v[:100]}" for k, v in S.failures.items()]
    say("Steps that failed: " + ("; ".join(fl[:6]) + (f"; {len(fl) - 6} more" if len(fl) > 6 else "")
                                  + " (tracebacks in gene_panel.log)" if fl else "none"))
    S_ = S
    sec_checks(S_, say, title)
    sec_expression(S_, say, title)
    sec_controls(S_, say, title)
    sec_ferroptosis(S_, say, title)
    sec_pyroptosis(S_, say, title)
    sec_p53(S_, say, title)
    sec_napepld(S_, say, title)
    sec_crosslinks(S_, say, title)
    title("9. FILES")
    say("results/README_columns.txt explains every file and column. Start with positive_controls.csv and panel_genes.csv,")
    say("then <GENE>_drug_summary.csv (one row per drug) and pathway_scores_by_dose.csv. Agent briefs: angles/<pathway>/.")
    with open(os.path.join(S.R, "summary.txt"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(L) + "\n")


def testable_genes(S):
    return {g for g, st in S.status.items() if st == "testable"} | set(MODULES)


def sec_checks(S, say, title):
    title("1. CHECKS: artifacts, calibration" + (", agreement with the earlier run" if S.prior else ""))
    F = getattr(S, "facts", {}) or {}
    say(f"Method v{T.METHOD_VERSION} (README 'Method v3'; results/run_info.json):")
    say(f"  Unreliable plates (--unreliable-plates; kept per well, left out of every drug-dose that has a well "
        f"elsewhere, of the reference spread and of the plate-factor peers): "
        f"{F.get('unreliable', ', '.join(S.unreliable) or 'none')}")
    say(f"  Replicate agreement of the same drug-dose's wells (Pearson r over the testable genes' z; results/"
        f"replicate_pairs.csv): {F.get('replicates', 'not available')}")
    say(f"  Composition: {S.comp_note}.")
    for w_ in S.ax.get("warnings", []):
        say(f"  WARNING: {w_}.")
    say(f"  Plate factors ({getattr(S, 'plate_scale_note', S.M.factor_source)}): > {T.NOISY_PLATE:g}: "
        f"{F.get('factors', T.plate_factor_text(S.M))} (results/plate_scale.csv, with % |z| > 1.96 before and after).")
    say(f"  Position not correctable (< {T.MIN_SLOT_WELLS} other-drug wells at the position): "
        f"{F.get('not_correctable', 'not available')}.")
    pos = getattr(S, "pos", None)
    if pos is not None and len(pos):
        for g, w in (("MTAP", "H1"), ("PSMD10", "D10")):
            t = pos[pos["gene"] == g].head(3)
            say(f"{g}: top well positions " + ", ".join(f"{a} ({b:+.2f} log2, z {c:.1f})" for a, b, c in
                                                     zip(t["well"], t["median_effect_plate_corrected"],
                                                         t["z_vs_other_positions"]))
                + f"   (earlier finding: {w})")
        top = pos[pos["gene"].isin(testable_genes(S))]
        top = top.sort_values("z_vs_other_positions", ascending=False).drop_duplicates("gene")
        top = top[(top["z_vs_other_positions"] >= 4) & (top["median_effect_plate_corrected"].abs() >= 0.2)]
        say("Testable genes with a strong position effect (the largest median shift of all drugs at one position; "
            "removed by the leave-drug-out correction):")
        say(table(top, ["gene", "well", "median_effect_plate_corrected", "z_vs_other_positions", "n_wells"]))
    pl = getattr(S, "plates", None)
    if pl is not None and len(pl):
        t = pl[pl["gene"].isin(testable_genes(S))].dropna(subset=["dmso_offset"]).copy()
        t["abs"] = t["dmso_offset"].abs()
        t = t.sort_values("abs", ascending=False).drop_duplicates("gene").head(8)
        say("Largest plate DMSO offsets (> 0: the plate's DMSO wells read low; corrected values never use DMSO):")
        say(table(t, ["gene", "plate", "dmso_offset", "dmso_wells"], 8))
    cal = getattr(S, "cal", None)
    if cal is not None and len(cal):
        c = cal[cal["gene"].isin(S.main + list(SCORES) + MODULES)]
        say(f"Calibration (drug wells with |z| > 1.96: ~5% expected if most drugs do nothing): median "
            f"{c['pct_drug_wells_abs_z_gt_1.96'].median():.1f}% over {len(c)} panel genes / anchors / modules "
            f"(range {c['pct_drug_wells_abs_z_gt_1.96'].min():.1f}-{c['pct_drug_wells_abs_z_gt_1.96'].max():.1f}%); "
            f"|z| > 3: median {c['pct_drug_wells_abs_z_gt_3'].median():.1f}%. Per gene: calibration.csv.")
    xl = getattr(S, "xl", None)
    if xl is not None and len(xl) and S.prior:
        r = xl[xl["category"] == "reproducibility"]
        say(f"Agreement with the earlier MTAP / Gankyrin run ({S.prior}):")
        if getattr(S, "prior_why", ""):
            say(f"  the two runs differ by design (other input or method), so their numbers differ: {S.prior_why}")
        say(table(r, ["comparison", "n", "statistic", "value", "spearman", "reading"], TOP, 6))
    elif xl is not None:
        say("No earlier MTAP / Gankyrin run (--prior): MTAP and PSMD10 were computed in this run only.")


def sec_expression(S, say, title):
    title(f"2. EXPRESSION (all wells pooled; lines expressing = above ambient: >= {EXPR_FRAC:.0%} of the median "
          f"line, >= {MIN_EXPR_CPM:g} CPM and >= {AMBIENT_MULT:g} x af x pooled CPM, af = {S.af:.2f} from the "
          "MTAP-null lines)")
    pg = getattr(S, "pg", None)
    if pg is None:
        say("  not available")
        return
    for pw in ["ferroptosis", "pyroptosis", "p53"]:
        t = pg[pg["pathway"] == pw]
        say(f"{pw}:")
        say(table(t, ["gene", "also_known_as", "median_line_cpm", "ambient_cpm", "n_lines_expressing", "n_lines",
                      "median_pct_cells_dmso", "median_counts_per_profile", "status"], TOP, 2))
    t = pg[~pg["pathway"].isin(["ferroptosis", "pyroptosis", "p53"])]
    say("NAPEPLD, TRIM72, anchors" + (" and added genes" if (pg["gene_set"] == "added").any() else "") + ":")
    say(table(t, ["gene", "also_known_as", "median_line_cpm", "ambient_cpm", "n_lines_expressing", "n_lines",
                  "median_pct_cells_dmso", "median_counts_per_profile", "status"], TOP, 2))
    bad = pg[pg["status"] != "testable"]
    say("Not testable as drug targets of mRNA change (and why):" if len(bad) else "Every panel gene is testable.")
    for r in bad.itertuples():
        say(f"  {label_of(r.gene)}: {r.status}")


def sec_controls(S, say, title):
    title("3. POSITIVE CONTROLS (sanity checks of the method, not tuning targets; one line per expectation: best drug)")
    p = getattr(S, "pcs", None)
    if p is None or not len(p):
        say("  not available")
        return
    t = p.copy()
    sign = {e: sg for e, _k, _n, sg, *_r in CONTROLS}
    z = pd.to_numeric(t["z"], errors="coerce") if "z" in t else pd.Series(np.nan, index=t.index)
    sg = t["expectation"].map(sign).fillna(1)
    t["_z"] = np.where(sg == 0, z.abs(), z * sg)
    t["_z"] = t["_z"].fillna(-99)
    order = {e: i for i, (e, *_r) in enumerate(CONTROLS)}
    best = t.sort_values("_z", ascending=False).drop_duplicates("expectation")
    best = best.assign(_o=best["expectation"].map(order)).sort_values("_o")
    n_clear = t.groupby("expectation")["verdict"].agg(lambda s: f"{(s == 'clear').sum()}/{len(s)} clear")
    best["drugs_clear"] = best["expectation"].map(n_clear)
    best["exp"] = best["expectation"].map(lambda s: s if len(s) <= 62 else s[:59].rsplit(" ", 1)[0] + " ...")
    best["at_24h"] = best.get("expected_at_24h", "")
    say(table(best, ["exp", "at_24h", "drug", "best_dose", "fold_change", "z", "fdr", "rank_among_drug_doses",
                     "verdict", "drugs_clear"], TOP, 3))
    say("Readout of each expectation (what was measured):")
    for r in best.itertuples():
        say(f"  {r.exp}: {r.readout}")
    say("at_24h: 'robust' controls that are absent lower the trust in the method; 'uncertain' ones (DNMT inhibitors: "
        "demethylation needs several divisions; dimethyl fumarate at <= 5 uM; COX inhibitors) say little when absent.")


def gene_best(S, genes):
    rows = []
    for g in genes:
        d = S.DS.get(g) if hasattr(S, "DS") else None
        if d is None or not len(d):
            rows.append({"gene": g, "best_up": S.status.get(g, "")})
            continue
        u = d.sort_values("best_up_z", ascending=False).iloc[0]
        w = d.sort_values("best_down_z").iloc[0]
        rows.append({"gene": g,
                     "best_up": f"{u['drug']} {u['best_up_dose']:g}: {u['best_up_fold_change']:.2f}x z "
                                f"{u['best_up_z']:.1f} fdr {u['fdr_up_drug']:.2g} {u['up_call'] or ''}".strip(),
                     "up_flags_context": "; ".join(x for x in (u["up_flags"], u["up_context"]) if x)[:70],
                     "best_down": f"{w['drug']} {w['best_down_dose']:g}: {w['best_down_fold_change']:.2f}x z "
                                  f"{w['best_down_z']:.1f} fdr {w['fdr_down_drug']:.2g} {w['down_call'] or ''}".strip()})
    return pd.DataFrame(rows)


def score_top(S, name, n=10, cols=None):
    t = S.SC.get(name)
    if t is None:
        return f"  {name}: not available ({S.skipped.get(name, '')})"
    return table(t, cols or ["drug", "conc", "fold_change", "z", "fdr_up", "z_by_dose", "top_members", "flags"], n)


def sec_ferroptosis(S, say, title):
    title("4. FERROPTOSIS (mRNA after 24 h: 'ferroptosis-like signature' at most; no lipid peroxidation, no death "
          "mode; calls use the dose-level FDR)")
    fer = [g for g, p, _ in PANEL if p == "ferroptosis"]
    say("Best increase and decrease per gene (drug summary; fdr = drug-level: best dose, Bonferroni over doses, BH "
        "over drugs; the up/down call uses the DOSE-LEVEL FDR of that dose (fdr_up/fdr_down < 0.10), so a call can "
        "sit next to a drug-level fdr >= 0.10):")
    say(table(gene_best(S, fer), ["gene", "best_up", "up_flags_context", "best_down"], TOP))
    f = getattr(S, "ferro", None)
    if f is not None:
        say("FERRO_MARKERS (PTGS2, CHAC1, SLC7A11) top drug-doses with their stress context (CHAC1/SLC7A11 are ATF4 "
            "and NRF2 targets, PTGS2 is NF-kB-inducible: context, not a verdict):")
        say(table(f, ["drug", "conc", "fold_change", "z", "fdr_up", "ISR_z", "NRF2_z", "UPR_z", "NFKB_z", "reading",
                      "flags"], 10))
    iron = gene_best(S, ["TFRC", "FTH1", "FTL", "NCOA4"])
    say("Iron genes (mRNA: TFRC up = iron-starvation-like; FTH1/FTL mRNA mostly follow NRF2, not iron):")
    say(table(iron, ["gene", "best_up", "best_down"], 4))
    lv = getattr(S, "lvl", None)
    if lv is not None and len(lv):
        t = by_fdr(lv[lv["gene"].isin(FERRO_LEVEL_GENES)]).drop_duplicates("gene")
        say("Does a line's baseline level predict which lines a drug depletes? (best drug-dose per gene; rho < 0 = "
            f"high-level lines depleted more; within lineage = organ removed; {NRF2_LEVEL} = basal NRF2 target "
            "activity):")
        say(table(t, ["gene", "drug", "conc", "rho", "rho_within_lineage", "z", "fdr", "fdr_within_lineage",
                      "z_by_dose", "reading"], len(FERRO_LEVEL_GENES)))


def sec_pyroptosis(S, say, title):
    title("5. PYROPTOSIS (mRNA only: no caspase cleavage, no pore formation, no IL-1b release)")
    pg = getattr(S, "pg", None)
    if pg is not None:
        t = pg[pg["pathway"] == "pyroptosis"]
        say("Who expresses the machinery (lines expressing / lines; the lines that carry its effects: usable in most "
            "wells, > 0 DMSO counts; lines lacking it):")
        for r in t.itertuples():
            hl = high_lines(S, r.gene)
            ef = effective_lines(S, r.gene) if r.gene in S.E else []
            say(f"  {label_of(r.gene):16s} {r.n_lines_expressing}/{r.n_lines} lines; {r.status}"
                + (f"; effects carried by {len(ef)}: {', '.join(S.name[c] for c in ef)}" if 0 < len(ef) <= 10 else "")
                + (f"; lost in: {r.loss_group_lines}" if isinstance(r.loss_group_lines, str) and r.loss_group_lines
                   else "") + (f"; >= 8x the median line in: {hl}" if hl else ""))
    say("GSDME inducers in the expressing lines:")
    d = S.DS.get("GSDME") if hasattr(S, "DS") else None
    say(table(d, ["drug", "doses", "z_by_dose", "best_up_fold_change", "fdr_up_drug", "up_pattern", "up_flags"], 5)
        if d is not None else "  not available")
    rx = getattr(S, "reex", None)
    if rx is not None and len(rx):
        for g, t in rx.groupby("gene"):
            rd = t["reading"].astype(str)
            if rd.str.startswith("deleted in the cell-line metadata").all():
                say(f"{g}: all lost lines ({t['lines'].iloc[0]}) are deleted in the cell-line metadata; "
                    "re-expression not analysed")
                continue
            say(f"{g} in the lines that silence it (deleted lines excluded; {t['lines'].iloc[0]}): top drug-doses")
            say(table(t, ["drug", "conc", "fold_change", "z_corrected", "fdr_up", "expressing_lines_fold_change",
                          "reading"], 5))
    say("INFLAMMASOME score (expressed members: " + ", ".join(S.score_members.get("INFLAMMASOME", [])) + "):")
    say(score_top(S, "INFLAMMASOME", 8))
    lv = getattr(S, "lvl", None)
    if lv is not None and len(lv) and "GSDME" in set(lv["gene"]):
        dd = set(find_drugs(set(lv["drug"]), S.drugs, DNA_DAMAGE))
        t = lv[(lv["gene"] == "GSDME") & lv["drug"].isin(dd)].sort_values("z")
        say("GSDME level vs depletion by DNA-damaging chemotherapy (rho < 0: GSDME-high lines depleted more):")
        say(table(t, ["drug", "conc", "rho", "rho_within_lineage", "z", "fdr", "z_by_dose"], 5))
    ls = getattr(S, "loss_res", None)
    if ls is not None and len(ls):
        t = ls[ls["gene"].isin([g for g, p, _ in PANEL if p == "pyroptosis"])]
        if len(t):
            say("Selective depletion of lines lacking a component (top 3 per gene):")
            say(table(t.groupby("gene").head(3), ["gene", "drug", "conc", "extra_log2_depletion", "z_selective",
                                                  "fdr_selective", "fdr_drug"], TOP))


def sec_p53(S, say, title):
    title("6. p53 (TP53 status from the cell-line metadata; mRNA of p53 targets after 24 h)")
    say("P53_ACTIVITY (all lines) top drug-doses:")
    say(score_top(S, "P53_ACTIVITY", 10))
    t = getattr(S, "p53wt", None)
    if t is not None:
        wt, alt = S.p53_groups
        say(f"More p53-target change in TP53-wild-type ({len(wt)}) than TP53-altered ({len(alt)}) lines in the same "
            "wells (p53-dependent). pattern: 'WT induction' = the WT lines rose >= 1.2x and the all-line P53 score "
            "went up; 'relative (altered lines fall)' = the altered lines fell more than the WT lines rose (sparing, "
            "not induction):")
        say(table(t, ["drug", "conc", "extra_log2_p53_induction_in_WT", "z_wt_more", "fdr", "pattern", "z_by_dose",
                      "wt_mean_log2", "altered_median_log2", "flags"], 10))
    f = getattr(S, "p53f", None)
    if f is not None:
        a, p = S.p53_auc
        say(f"Functional p53 status: responsiveness = mean p53-target shift over {S.p53_ref_rule} "
            f"(p53_reference_doses.csv; responsiveness is genotype-blind; the responsive / unresponsive cut is halfway "
            f"between the WT and altered medians; within 2 SE of it = 'uncertain'). AUC WT vs altered = {fnum(a)} "
            f"(p {fnum(p, '{:.2g}')}); cut {fnum(S.p53_cut)} log2.")
        d = f[f["discordant"] != ""].reset_index()
        say("Discordant lines:" if len(d) else "Discordant lines: none")
        if len(d):
            say(table(d, ["cell_name", "tp53_annotation", "tp53_changes", "p53_responsiveness_log2",
                          "basal_p53_activity_log2", "discordant"], TOP))
    g = getattr(S, "p53g", None)
    if g is not None:
        say("Growth: drugs that deplete TP53-WT lines more than TP53-altered lines (negative = WT lost more):")
        say(table(g, ["drug", "conc", "extra_log2_depletion_of_TP53_WT", "z_selective", "fdr_selective", "fdr_drug",
                      "z_by_dose", "all_cells_log2_vs_plate"], 8))
    say("p53 reporters (FDXR, ZMAT3, MDM2) vs targets with p53-independent inducers (CDKN1A: HDAC inhibitors; "
        "PMAIP1, GADD45A, SESN2: ATF4) (best increase):")
    say(table(gene_best(S, ["CDKN1A", "MDM2", "FDXR", "ZMAT3", "PMAIP1", "GADD45A", "SESN2", "TP53"]),
              ["gene", "best_up", "up_flags_context"], 8))


def sec_napepld(S, say, title):
    title("7. NAPEPLD (NAPE-PLD) and TRIM72 (MG53)")
    for g in ["NAPEPLD", "TRIM72"]:
        st = S.status.get(g, "not extracted")
        say(f"{label_of(g)}: {st}; median line {fnum(S.med.get(g, np.nan), '{:.1f}')} CPM, expressed in "
            f"{int(S.E[g].sum()) if g in S.E else 0}/{len(S.base)} lines.")
        if g in getattr(S, "DS", {}):
            say(table(gene_best(S, [g]), ["best_up", "up_flags_context", "best_down"], 1))
            cr = getattr(S, "coreg", None)
            if cr is not None and len(cr):
                c = cr[(cr["gene"] == g) & (cr["rank"] > 0)].head(5)
                say("  co-regulated across drug wells: " + ", ".join(f"{p} {r:.2f}" for p, r in zip(c["partner"], c["r"]))
                    + " | after removing PC1: " + ", ".join(f"{p} {r:.2f}" for p, r in zip(c["partner_minus_pc1"],
                                                                                         c["r_minus_pc1"])))
            lv = getattr(S, "lvl", None)
            if lv is not None and len(lv) and g in set(lv["gene"]):
                t = by_fdr(lv[lv["gene"] == g]).head(3)
                say("  level vs growth: " + "; ".join(f"{d} {c:g} rho {r:.2f} (fdr {q:.2g})" for d, c, r, q in
                                                      zip(t["drug"], t["conc"], t["rho"], t["fdr"])))
    if S.status.get("TRIM72", "") != "testable":
        n = int(S.E["TRIM72"].sum()) if "TRIM72" in S.E else 0
        if n == 0:
            say("TRIM72 (MG53) is muscle/heart-enriched and is not detected above ambient in any line here.")
        else:
            names = ", ".join(S.name[c] for c in S.E.index[S.E["TRIM72"]][:8])
            say(f"TRIM72 (MG53) is muscle/heart-enriched; it is detected at low level in {n} line(s) ({names}); "
                f"status: {S.status.get('TRIM72', '')}. Treat any drug effect as exploratory.")


def sec_crosslinks(S, say, title):
    title("8. CROSS-LINKS to MTAP / Gankyrin" + (" (and the earlier MTAP / Gankyrin run)" if S.prior else
                                                  " (no earlier run: this run's MTAP / PSMD10 results)"))
    xl = getattr(S, "xl", None)
    if xl is None:
        say("  not available")
        return
    say("Hypotheses, not tests (correlations read within lineage; p_bh = BH over these rows of p_within_lineage, or "
        "of p for group comparisons):")
    say(table(xl[xl["category"] == "biology"], ["comparison", "n", "statistic", "value", "rho_within_lineage",
                                                "p_within_lineage", "auc", "p", "p_bh", "expected"], TOP))
    sh = xl[xl["category"] == "shared top drugs"]
    src = "the earlier MTAP / Gankyrin run's lists" if S.prior else "this run's MTAP / PSMD10 lists"
    say(f"Drugs in both {src} (drug-level FDR < {T.FDR_CUT:g}) and a panel list (FDR < {T.FDR_CUT:g} at a dose, or "
        f"a call): {getattr(S, 'shared_n', len(sh))} (~{getattr(S, 'shared_expected', np.nan):.1f} expected by "
        f"chance, matched for drug activity: deciles of {getattr(S, 'activity_src', 'activity')}; "
        f"{getattr(S, 'shared_expected_naive', np.nan):.1f} if all drugs were alike)"
        + ("" if S.prior else ". Both lists come from this run, so an overlap is not replication."))
    for r in sh.head(10).itertuples():
        say(f"  {r.comparison}: {r.reading}"[:200])
    if getattr(S, "pc1", None):
        say(f"Co-regulation (low-count genes left out): the first principal component of the panel's drug responses "
            f"explains {100 * S.pc1['share']:.0f}% (often a global stress / shutdown axis; check its loadings): "
            f"{S.pc1['top'][:150]}")
        say(f"  wells scoring highest on it: {S.pc1.get('wells_high', '')}")
        say("Partners per gene: coregulation_top_partners.csv; genome-wide partners: tahoe_atlas.py lookup corr GENE "
            "(once the atlas has been computed).")


# ============================================================================= panel_genes.csv
def step_panel_genes(S):
    rows = []
    loss = {x["gene"]: x for x in getattr(S, "loss", [])}
    for r in S.gt.itertuples():
        g = r.gene
        d = {"gene": g, "also_known_as": r.also_known_as, "pathway": r.pathway, "role": r.role,
             "gene_set": r.gene_set, "symbol_used": r.symbol_used, "in_gene_metadata": g in S.symbols if S.symbols
             else np.nan, "extracted": g in S.targets, "status": S.status.get(g, "")}
        if g in S.C:
            c = S.C[g]
            en = S.enough
            ratio = c / S.med[g] if S.med[g] > 0 else c * np.nan
            ok = ratio[en].dropna().sort_values()
            ne = [S.name[i] for i in S.E.index[~S.E[g] & en]]
            d.update({"median_line_cpm": S.med[g], "median_line_cpm_dmso": S.Cd[g][en].median(),
                      "median_pct_cells_dmso": S.base[f"{g}_pct_cells_dmso"][en].median(),
                      "n_lines": int(en.sum()), "n_lines_expressing": int(S.E[g][en].sum()),
                      "pooled_cpm": S.pooled[g], "ambient_fraction": S.af, "ambient_cpm": S.ambient[g],
                      "expression_threshold_cpm": S.thr[g], "median_counts_per_profile": S.counts.get(g, np.nan),
                      "testable": S.status.get(g) == "testable",
                      "lowest_lines": "; ".join(f"{S.name[i]} {v:.2f}x" for i, v in ok.head(3).items()),
                      "highest_lines": "; ".join(f"{S.name[i]} {v:.2f}x" for i, v in ok.iloc[::-1].head(3).items()),
                      "lines_not_expressing": ", ".join(ne) if len(ne) <= 25 else f"{len(ne)} lines",
                      "lines_8x_above_median": high_lines(S, g),
                      "n_effective_lines": len(effective_lines(S, g)),
                      "effective_lines": ", ".join(S.name[c] for c in effective_lines(S, g))
                      if len(effective_lines(S, g)) <= 12 else f"{len(effective_lines(S, g))} lines",
                      "loss_group_lines": ", ".join(S.name[c] for c in loss[g]["lines"]) if g in loss else "",
                      "drug_effects": f"{g}_drug_effects_by_dose.csv" if g in S.RES else "none: " + S.status.get(g, ""),
                      "n_calls_up": int((S.RES[g]["call"] == "up").sum()) if g in S.RES else np.nan,
                      "n_calls_down": int((S.RES[g]["call"] == "down").sum()) if g in S.RES else np.nan})
        rows.append(d)
    S.pg = pd.DataFrame(rows)
    S.save(S.pg, "panel_genes.csv")


# ============================================================================= angles (agent folders)
WHAT_DATA_SHOW = """## What these data can and cannot show
- They are mRNA counts 24 h after the drug, in ~50 cancer cell lines pooled in each well. They show which genes go
  up or down, in which lines, and which lines lose ground (relative cell numbers) - nothing else.
- They cannot show protein, enzyme activity, lipid peroxidation, iron levels, caspase or gasdermin cleavage, pore
  formation, cytokine release or the mode of cell death. Say 'ferroptosis-like / stress signature', never
  'ferroptosis'; say 'depleted', never 'killed by pyroptosis'.
- Fewer cells after 24 h = slower growth or death; the two cannot be told apart.
- Lines that do not express a gene still read it from ambient RNA (the pooled RNA of all lines in the well): here
  <AF> of the gene's pooled level, measured on the MTAP-null lines. For a gene that only a few lines express, those
  reads just follow the few expressers. A line therefore counts as expressing a gene only when it reads >= 25% of the
  median line, >= 1 CPM and >= 2x that ambient level ('lines above ambient'); the others are left out of the gene's
  drug effects. When a drug is toxic or causes a transcription drop, ambient RNA becomes a larger share of every
  line's reads, and absent genes appear to rise.
"""

PANEL_RULEBOOK = """## Rules for interpreting (learned on this dataset; follow them)
1. Artifacts first. Read the flags column of every row you report (the same definitions as in the atlas):
   - 'toxic': the drug-dose kept < half the plate's usual cells (also < half of its plate row's where that row, the
     other drugs in the same row A-H, itself lost or gained cells), every used well lost cells, and no higher dose of
     the drug kept more than half: dose-consistent cell loss. Its expression changes may be secondary to dying or
     arrested cells. At the top dose there is no higher dose to check and most drug-doses have one well: 'toxic'
     then rests on one well's cell count (<CELL_REP>).
   - 'low cells (technical?)': fewer than half the cells, but not confirmed as dose-consistent loss beyond its plate
     row. It may be technical (the row lost cells), a non-monotonic dose response (antimitotics), a row of toxic
     neighbours at a high dose, or a well that did not replicate. Do not call the drug toxic from it alone. A
     drug-dose with many significant genes is active: read its effects with the cell-loss caveat and check
     row_cells_log2 and another dose or plate.
   - 'plate-row cell shift': the well's plate row gained or lost cells or UMIs per cell as a whole: be wary.
   - 'transcription drop': genes or UMIs per cell fell (vs the plate and vs the row). Short stable mRNAs then rise and
     long or unstable ones fall, in relative terms.
   - 'cell-cycle shift': the S or G2/M module moved; every cycle-linked mRNA follows.
   - 'composition shift': a few genes took a large share of the reads. The effects shown are relative to the median
     gene of each profile (composition-normalised), so the raw CPM view of the same well would differ.
   - 'noisy plate (z scaled)': the drug-dose's plate x dose group is noisier than the same dose on other plates; its
     z was divided by that factor (plates: <FACTORS>), or by more for a gene that is noisier there than the plate's
     median gene (plate_scale_gene; plate_scale_by_gene.csv). Do not report a hit seen only on such a plate unless
     another plate agrees.
   - 'unreliable plate only': every well of the drug-dose sits on an unreliable plate (<UNRELIABLE>): never report
     it as a finding; drug-doses with another well use only the reliable wells.
   - 'position not correctable' / 'position correction uncertain': the well position could not be corrected (too few
     other-drug wells there, or too few that do not move this gene themselves): a position artifact may remain. Check
     which drugs share the well (sample_map.csv): a flat all-dose effect of a drug with no expected activity can be
     the mirror image of a strong drug at the same position.
   - 'position effect removed': the correction moved the estimate by > 1.15x (compare log2FC_plate_corrected_only).
   - 'wells disagree' (imported from the atlas): the drug-dose's wells do not agree genome-wide: unreplicated.
   - 'low counts' (pseudocount-dominated gene), 'whole proteasome up/down' (PSMD10: not Gankyrin-specific).
   Never use the DMSO wells as the reference for drug effects: they sit at <DMSO> (uncorrected positions) and some
   plates' DMSO is off (log2FC_vs_DMSO_uncorrected is there only for comparison). Baseline levels per line (cpm_dmso,
   basal_p53_activity_log2, the level in level_vs_growth.csv) come from untreated cells and are fine for comparing
   lines.
2. Dose consistency, and its limit. Real effects usually grow with dose or appear at the top dose; a hit at a low
   dose only is most likely noise (z_by_dose: doses in ascending order). But plates that share a layout put a drug
   at the same well position at all its doses, so dose consistency does NOT exclude a position artifact; agreement
   at a different position (another layout; replicate_pairs.csv pair_type 'different position') is the stronger
   test.
3. Breadth. Check how many lines move (n_lines_up / n_lines, frac_lines_positive). One or two lines = a
   line-specific observation. For genes few lines express, gene_roles.csv names the lines that carry the effects.
4. Specific vs broad. Many drugs move big programs together (ISR/ATF4, NRF2, UPR, heat shock, interferon, NF-kB,
   proteasome, cell cycle, p53). The 'context' column names the programs that moved strongly in the same drug-dose:
   say whether a gene's change belongs to such a program or stands alone.
5. Statistics. With ~1,100 drug-doses per gene, z > 3 happens by chance: rely on FDR, effect size and dose
   consistency. Report fold changes (not log2) with FDR and the number of lines. 'call' uses the dose-level FDR; the
   drug summaries' fdr_*_drug is drug-level (best dose, Bonferroni over doses, BH over drugs).
6. Known biology as a check: positive_controls.csv lists expected effects and whether the data show them
   (expected_at_24h). Robust at 24 h: DNA damage -> p53 targets; proteasome inhibitors -> proteasome, heat-shock and
   HMOX1 genes; HSP90 inhibitor -> heat shock; ciclopirox -> TFRC; antimitotics -> G2/M; dinaciclib -> transcription
   drop. Uncertain at 24 h or at <= 5 uM: DNMT inhibitors (demethylation needs several divisions), dimethyl fumarate
   and COX inhibitors (report only). Cytostatic drugs (BRAF/MEK, EGFR inhibitors) deplete lines only weakly at 24 h.
   A robust control that is absent lowers trust; an uncertain one that is absent says nothing about the method.
7. mRNA after 24 h only: no claims about protein, function or causality. Label hypotheses as hypotheses.
8. Every number in your report must come from a query you ran on the files; name the file it came from.
"""

PANEL_REPORT_RULES = """## Your report
Write `report.md` in this folder, in Markdown:
- `# <title>`, then a first paragraph that answers the angle's main question with numbers.
- Short sections with the findings, most important first; tables (at most 15 rows each) for ranked items;
  fold changes with FDR and the number of cell lines; the file each number came from.
- `## Not testable`: the genes of this angle that could not be tested here, and why (from the gene table above).
- `## Caveats`: which artifact checks you ran and what they showed.
- `## Leads to test`: up to 5 concrete follow-ups (drug, dose, cell line, readout - e.g. a protein or functional
  assay that mRNA cannot replace).
- Plain language, at most ~1,500 words, no methods recap beyond one sentence. Do not pad.
Work unattended: never ask questions; if something is unclear, decide, and say what you assumed.
"""

PANEL_APPEND = """You are a careful computational biologist analysing one pathway of a gene-panel analysis of the
Tahoe-100M single-cell drug perturbation atlas (mRNA of about 50 cancer cell lines 24 h after several hundred drugs,
mostly at 3 doses; brief.md gives this run's numbers). You run
unattended: nobody will answer questions or grant permissions, so never ask; decide, state your assumptions in the
report, and keep going. Work in your current folder (write your scripts and report.md there); the results/ folder
and the other files of the gene-panel folder may be read. {shell}Compute every number you report with Python: write a
.py script in this folder and run it with `{py} script.py` (always allowed). If any command is refused, do the same
thing in Python instead; never stop because of a refusal.
Do not install packages, use the network, delete files or write anything outside the gene-panel folder (reading files
and running the look-up commands named in brief.md is allowed). Your job is finished only when report.md exists and
follows brief.md; a precise, well-checked report matters more than a long one."""

PANEL_SYNTH = """Read every report in this folder (all *.md files except 00_overview.md) and write 00_overview.md: a
single overview of what Tahoe-100M shows about the gene panel (ferroptosis, pyroptosis, p53, NAPEPLD and TRIM72) and
how it connects to MTAP and Gankyrin (the crosslinks report; the earlier MTAP / Gankyrin analysis of these data was
inconclusive). Start with the top findings per pathway (each with its
numbers and which report it comes from), then where the reports agree or disagree, the main caveats (mRNA after 24 h
only: no protein, lipid peroxidation, cleavage or death mode; genes that are not expressed or not testable), and a
ranked list of the 10 best leads to test experimentally (drug, dose, cell line, readout). At most ~1,500 words, plain
language, Markdown. Do not invent numbers: use only what the reports state. Run unattended; never ask questions."""

TASKS = {
    "ferroptosis": """
Which drugs induce the ferroptosis markers (PTGS2, CHAC1, SLC7A11), and with which programs
(ferro_markers_with_context.csv)? Read the context, not a verdict. CHAC1 and SLC7A11 are ATF4 targets that cystine
starvation (system xc- inhibition, e.g. erastin) induces through the ISR, so 'with ISR' fits cystine starvation as
well as any other ISR trigger. 'With NRF2' is an antioxidant (protective) response, since SLC7A11 is an NRF2 target.
PTGS2 is also an NF-kB/AP-1 target and rises after COX inhibition, so check NFKB_z and top_members. Rows flagged
'(artifact likely)' rose with toxicity, a transcription drop or a cell-cycle shift. Which drugs move the defences
(GPX4, AIFM2/FSP1, NFE2L2 and its targets), lipid remodelling (ACSL4, LPCAT3) and iron handling (TFRC, FTH1/FTL,
NCOA4)? At the mRNA level only TFRC reads iron status: iron starvation stabilises TFRC mRNA through IRP binding (TFRC
up). TFRC also follows HIF and proliferation, so check the cell-cycle context. Ferritin is controlled mainly at
translation, and FTH1/FTL mRNA rise with NRF2 (check NRF2_z) and inflammation. Do not read 'TFRC down with ferritin
up' as iron load. Do baseline GPX4, ACSL4, AIFM2, SLC7A11, NFE2L2, LPCAT3, TFRC levels predict which lines a drug
depletes, within lineage (level_vs_growth.csv: rho_within_lineage, fdr_within_lineage)? The library has no direct
ferroptosis inducer (no erastin, sulfasalazine, sorafenib, RSL3, ML162/ML210, FIN56 or BSO); the nearest are
artesunate / dihydroartemisinin, auranofin, statins and altretamine. A level-vs-depletion association is therefore
not evidence of ferroptosis sensitivity. NFE2L2 mRNA is not NRF2 activity (KEAP1 acts on the protein): use the basal
NRF2 target score (gene NRF2_basal_score in level_vs_growth.csv). Known biology to check: dimethyl fumarate -> NRF2;
auranofin -> TXNRD -> NRF2/ISR; ciclopirox -> TFRC; statins (pitavastatin; pravastatin is hydrophilic and barely
enters non-liver cells): their effects on GPX4 (selenoprotein translation) and CoQ10/FSP1 are not visible in mRNA, and
their on-target mRNA readout (SREBP2 targets HMGCR, HMGCS1, LDLR, INSIG1) is not extracted here (use the atlas look-up
below if the atlas exists); artesunate / dihydroartemisinin; proteasome inhibitors -> HMOX1. mRNA after 24 h cannot
show lipid peroxidation or the death mode: say 'ferroptosis-like signature' and label hypotheses.""",
    "pyroptosis": """
Which lines express which parts of the pyroptosis machinery (many carcinoma lines silence GSDME and the inflammasome
genes; expression_by_line.csv, loss_groups.csv)? Which drugs change them: DNMT inhibitors -> GSDME re-expression in
the silenced lines (reexpression_in_silenced_lines.csv: lines with a deletion row in the cell-line metadata are left
out, since a deleted gene cannot be re-expressed; compare with the comparator lines (below), ambient RNA follows any
change in the others; 'not interpretable' rows rose with toxicity, a transcription drop, FDR >= 0.10 or too few lines;
re-expression after demethylation usually needs several divisions, so it is uncertain at 24 h); NF-kB inducers ->
IL1B and NLRP3 (priming); interferon (IRF1/IRF2) -> CASP1, CASP4 and GSDMD; IL18 is mostly constitutive (INFLAMMASOME =
mean mRNA of the machinery, not activation; IFN and NFKB scores). Imiquimod acts through TLR7, which most carcinoma
lines lack. Does GSDME level predict which lines DNA-damaging chemotherapy depletes (level_vs_growth.csv, gene GSDME;
use rho_within_lineage, since GSDME silencing is lineage-linked)? GSDME mainly decides whether caspase-3 activation
ends as pyroptosis or apoptosis, not whether cells die, so a weak or absent relationship is not evidence against
GSDME-mediated pyroptosis. Are lines lacking a component selectively depleted by any drug (loss_screens.csv)? mRNA
cannot show caspase cleavage, pore formation or cytokine release. Many of these genes are low: name the lines that
actually carry each low-expressed gene's effects (the gene table above, 'lines that carry its effects': usable in
most wells and > 0 DMSO counts) instead of the number of 'expressing' lines.<EFFECTIVE>
Re-expression readings compare the lost lines with lines that read pure ambient RNA (comparator column: the deleted
lines in the same wells when there are >= 2, else the expressing lines); 'lost lines read ambient only' means the
lost lines' untreated level is at the ambient-RNA floor (or inside the deleted lines' range): a rise there cannot be
told from ambient RNA.""",
    "p53": """
Which drugs activate p53 transcription, and is it p53-dependent (p53_wt_vs_altered.csv: TP53-wild-type vs
TP53-altered lines in the same wells)? Read the pattern column: a high z_wt_more with pattern 'relative (altered lines
fall)' (WT lines up < 1.2x, i.e. wt_mean_log2 < 0.26, or a negative all-line P53_ACTIVITY z) means the altered lines
fell more than the WT lines rose: p53-dependent sparing under a global drop, not induction; adjacent wells with
near-identical signatures count once. How does the functional p53 status (p53_functional_status.csv: responsiveness
to the strongest significant non-toxic activators, genotype-blind; 'uncertain' = within 2 SE of the cut) agree with
the annotation (AUC, discordant lines: annotated wild type but unresponsive, altered but responsive - check protein
changes, CDKN2A deletion, MTAP status)? Specific targets (FDXR, ZMAT3, MDM2; context targets DDB2, XPC, PHLDA3, EDA2R,
SPATA18) vs targets with strong p53-independent inducers: CDKN1A (HDAC inhibitors panobinostat, belinostat,
tucidinostat; also TGF-b, MEK/ERK), PMAIP1, SESN2 and TNFRSF10B (ATF4/CHOP), and GADD45A (ATF4, FOXO, NF-kB). Check
the ISR context and p53_wt_vs_altered.csv before calling a change p53-driven. TP53 mRNA itself (truncating mutants and
deletions lower it). Which drugs deplete TP53-WT lines selectively (p53_wt_selective_growth.csv)? The library has no
MDM2 inhibitor: the expected activators are DNA damage and antimetabolites, plus selinexor (XPO1 inhibitor: nuclear
p53 retention) and possibly mitotic-arrest drugs (volasertib, antimitotics).""",
    "napepld_trim72": """
NAPEPLD and TRIM72 (MG53): expression across lines (if TRIM72 is not expressed, say so plainly and keep that part
short), drug effects if testable (dose pattern, breadth, context), co-regulation partners across drug wells
(coregulation_top_partners.csv; genome-wide partners need the atlas), level vs growth, and plausible links
(hypotheses only: rimonabant is a CB1 (CNR1) inverse agonist, but CB1 is barely expressed in most cancer lines (CNR1
was not extracted; one real Tahoe file has CNR1 at 0 CPM in 39 of 50 lines), so a rimonabant effect on NAPEPLD at
0.5-5 uM is more likely CB1-independent. NAPE-PLD is one of several routes to N-acylethanolamines, so its mRNA does
not report anandamide levels. TRIM72 and insulin / IRS1 / PI3K-AKT drugs: the library has no insulin.) When a drug
raises TRIM72 strongly, ambient RNA lifts the low-expressing lines with it, so the count of lines up is not evidence
of breadth; TRIM72 reads in carcinoma lines may also come from a non-canonical transcript: confirm MG53 protein before
claiming induction. Keep the report short if the data say little.""",
    "crosslinks": """
How does the panel connect to MTAP and Gankyrin (PSMD10)<PRIOR>? These are hypotheses, read within lineage
(crosslinks.csv: rho_within_lineage, p_bh). For context, the earlier MTAP / Gankyrin analysis of these data was
inconclusive: no drug convincingly raised MTAP or Gankyrin; test this without assuming it (a PSMD10 rise that comes
with the whole proteasome, a cell-cycle shift or another flag is not a Gankyrin-specific inducer). Gankyrin vs p53
activity (Gankyrin-MDM2 degradation of p53 is a protein-level mechanism: lower basal p53 activity and responsiveness
in high-PSMD10 TP53-WT lines would fit it, but cannot test it), Gankyrin vs NRF2 (reported KEAP1/NRF2 feedback;
KEAP1-mutant lung lines dominate basal NRF2 and are not annotated), CDKN2A deletion (cdkn2a_deleted; not MTAP-null:
NCI-H460, A498 and A-427 lost CDKN2A but keep MTAP) vs p53. ARF restrains MDM2 mainly after oncogene signalling, so
equal responsiveness to DNA damage is the expected result. CDKN2A mRNA counts p16INK4a and p14ARF together and is high
in TP53- or RB-defective lines, so low CDKN2A in TP53-WT lines is common and is not by itself a deletion. MTAP loss vs
ferroptosis gene baselines (speculative: MTAP loss mainly raises MTA; in cystine-rich medium any effect on cysteine
supply is expected to be small, so no difference is the likely result; five comparisons, so one p < 0.05 is expected
by chance). <SHARED> <RCRIT>""",
}


def r_crit(n):
    """|rho| needed for a two-sided p < 0.05 over n lines (Fisher z, as the p values in crosslinks.csv)."""
    return math.tanh(1.96 / math.sqrt(n - 3)) if n > 3 else np.nan


def deeper_queries(S):
    py = bpath(agent_python())
    o = os.path.abspath(S.out)
    R = os.path.join(o, "results")
    atl = os.path.abspath(S.atl) if S.atl else ""
    me = os.path.join(HERE, "tahoe_atlas.py")
    s = f"""## Deeper queries
- Python: run scripts as `{py} script.py` (numpy, pandas and pyarrow are available; scipy may be missing: check
  first). Keep the scripts you write in this folder.
- All results: `{bpath(R)}` (read `{bpath(os.path.join(R, 'README_columns.txt'))}` first). Every panel gene and
  anchor has `<GENE>_drug_effects_by_dose.csv` (every drug-dose, all columns) and `<GENE>_drug_summary.csv` (one row
  per drug).
- Counts per well x cell line: `{bpath(os.path.join(o, 'well_line.parquet'))}` (sample, cell_line_id, n_cells,
  total_counts, raw counts of every extracted gene, det_<GENE> = cells with >= 1 count); wells:
  `{bpath(os.path.join(o, 'sample_map.csv'))}` (sample, plate, drug, conc, well, n_cells, is_dmso).
- Per cell (large: read only the columns and rows you need, e.g. pyarrow.parquet.read_table(f, columns=[...],
  filters=[('drug', 'in', [...])])): `{bpath(os.path.join(o, 'cells'))}/*.parquet`; columns barcode, sample, plate,
  drug, cell_line_id, n_genes, total_counts, the extracted genes and the PROTEASOME / S_PHASE / G2M_PHASE sums.
"""
    if atl and os.path.exists(me) and atlas_ready(atl, need_script=True):
        s += (f"- Genome-wide (the atlas has been computed): `{py} {quote(bpath(me))} --out {quote(bpath(atl))} lookup "
              "gene <SYMBOL>` (also `corr <SYMBOL>`, `drug <NAME>`, `line <NAME>`).\n")
    elif not atl:
        s += "- Genome-wide partners or other genes: not available ('analyze' ran with --atlas none).\n"
    elif atlas_ready(atl):
        s += ("- Genome-wide partners or other genes: not available (the atlas is computed, but tahoe_atlas.py next "
              "to this script is missing or older: copy the current one, then rerun this script's analyze).\n")
    else:
        s += ("- Genome-wide partners or other genes: not available (no computed atlas in <data>/atlas or --atlas "
              "when 'analyze' ran; compute the atlas, then rerun this script's analyze).\n")
    return s


def high_lines(S, g, fold=8.0):
    """Lines far above the median line (genes most lines express only at ambient level, e.g. IL1B)."""
    if g not in S.C or not S.med.get(g, 0) > 0:
        return ""
    r = (S.C[g] / S.med[g]).sort_values(ascending=False)
    r = r[r >= fold]
    return ", ".join(f"{S.name[c]} {v:.0f}x" for c, v in r.head(6).items()) + (" ..." if len(r) > 6 else "")


def gene_status_md(S, genes):
    rows = ["| gene | role | lines above ambient | lines that carry its effects | median line CPM | far above the "
            "median line | status |", "|---|---|---|---|---|---|---|"]
    role = dict(zip(S.gt["gene"], S.gt["role"]))
    for g in genes:
        n = f"{int(S.E[g].sum())}/{len(S.E)}" if g in S.E else "-"
        r = str(role.get(g, S.set_of.get(g, "")))
        r = r[len(AKA[g]) + 3:] if g in AKA and r.startswith(f"({AKA[g]}) ") else r
        ef = effective_lines(S, g) if g in S.E else []
        eft = (f"{len(ef)}: " + ", ".join(S.name[c] for c in ef)) if 0 < len(ef) <= 10 else str(len(ef)) if g in S.E \
            else "-"
        rows.append(f"| {label_of(g)} | {r} | {n} | {eft} | {fnum(S.med.get(g, np.nan), '{:.1f}')}"
                    f" | {high_lines(S, g)} | {S.status.get(g, '')} |")
    return "\n".join(rows) + "\n"


def write_brief(S, folder, name, files, genes):
    info = S.info
    head = (f"This run: {int(S.wl['n_cells'].sum()):,} cells, {S.sm['sample'].nunique()} wells, "
            f"{S.sm['plate'].nunique()} plates, {S.wl['cell_line_id'].nunique()} cell lines"
            + (f" (TRIAL: first {info['limit_files']} files only)" if info.get("limit_files") else "") + ".")
    ndd = len(S.SC["P53_ACTIVITY"]) if "P53_ACTIVITY" in S.SC else len(next(iter(S.RES.values())))
    F = getattr(S, "facts", {}) or {}
    unrel = ", ".join(S.unreliable) or "none"
    methods = PANEL_METHODS.replace("< 30 cells", f"< {T.MIN_CELLS} cells").replace("~1,100", f"{ndd:,}") \
        .replace("<COMPOSITION>", S.comp_note).replace("<UNRELIABLE>", unrel)
    rules = PANEL_RULEBOOK.replace("~1,100", f"{ndd:,}").replace("<FACTORS>", F.get("factors", "see plate_scale.csv")) \
        .replace("<UNRELIABLE>", unrel).replace("<DMSO>", F.get("dmso", "the plates' DMSO positions")) \
        .replace("<CELL_REP>", F.get("cell_rep", "weak evidence alone"))
    facts = PANEL_FACTS
    for k, v in (("<NGENES>", F.get("n_genes", "")), ("<UNRELIABLE_R>", F.get("unreliable", unrel)),
                 ("<REPLICATES>", F.get("replicates", "not available")),
                 ("<FACTOR_SOURCE>", getattr(S, "plate_scale_note", S.M.factor_source)),
                 ("<FACTORS>", F.get("factors", "")), ("<COMPOSITION>", S.comp_note), ("<DMSO>", F.get("dmso", "")),
                 ("<NOTCORR>", F.get("not_correctable", "")), ("<NODATA>", F.get("no_data", "")),
                 ("<THIN>", F.get("thin_lines", "")), ("<SALTS>", F.get("salts", "")),
                 ("<MTAPCUT>", F.get("mtap_cut", S.null_source))):
        facts = facts.replace(k, str(v))
    with open(os.path.join(folder, "brief.md"), "w", encoding="utf-8") as fh:
        added = [g for g in genes if S.set_of.get(g) == "added"]
        task = TASKS[name].strip() + (f"\nGenes added with --genes ({', '.join(added)}) are in this folder too: report "
                                      "them the same way, briefly." if added else "")
        n_all, n_wt = int(S.enough.sum()), int((S.base["tp53_group"] == "WT").sum())
        task = task.replace("<RCRIT>", f"Correlations over all {n_all} lines need |rho| >= {fnum(r_crit(n_all))}, and "
                                       f"those over the {n_wt} TP53-WT lines need |rho| >= {fnum(r_crit(n_wt))}, for "
                                       "p < 0.05; below that, say the result is weak.")
        if S.prior:
            task = task.replace("<PRIOR>", " (the earlier MTAP / Gankyrin run's files are in prior/)").replace(
                "<SHARED>", "Drugs in both the earlier run's MTAP / PSMD10 lists and a panel list (crosslinks.csv, "
                            "category shared top drugs) against the number expected by chance, which is matched for "
                            "drug activity (potent drugs appear in nearly every list), and reproducibility vs the "
                            "earlier run (crosslinks.csv, category reproducibility; 'differs by design' when the two "
                            "runs used other input or another method version).")
        else:
            task = task.replace("<PRIOR>", "").replace(
                "<SHARED>", "Drugs in both this run's MTAP / PSMD10 lists and a panel list (crosslinks.csv, category "
                            "shared top drugs) against the number expected by chance, which is matched for drug "
                            "activity (potent drugs appear in nearly every list); both lists come from this run, so "
                            "an overlap is not replication.")
        eff = [f"{label_of(g)}: {', '.join(S.name[c] for c in effective_lines(S, g))}" for g in genes
               if g in S.E and 0 < len(effective_lines(S, g)) <= 10]
        task = task.replace("<EFFECTIVE>", (" In these data: " + "; ".join(eff) + ".") if eff else "")
        what = WHAT_DATA_SHOW.replace("<AF>", f"about {S.af:.0%}")
        me = bpath(os.path.abspath(__file__))
        fh.write(f"# Angle: {TITLES[name]}\n\nWritten by `{me}` (method v{T.METHOD_VERSION}, with "
                 f"`{bpath(os.path.abspath(T.__file__))}`) on {time.strftime('%Y-%m-%d %H:%M')}.\n\n"
                 f"## Your task\n{task}\n\n{head}\n\n{what}\n"
                 f"## Genes of this angle\n{gene_status_md(S, genes)}\n## Data in this folder\n")
        for f, desc in files:
            fh.write(f"- `{f}`: {desc}\n")
        fh.write("\n" + methods + "\n" + facts + "\n" + rules + "\n" + deeper_queries(S) + "\n" + PANEL_REPORT_RULES)


PANEL_METHODS = """## How the numbers were made (method v3)
- Cells of one line in one well are summed into a profile (profiles with < 30 cells are left out).
- Drug effect on a gene (log2FC_corrected; fold_change = 2^log2FC): the profile's log2 CPM minus the median of all
  drug wells on the same plate for the same line (NOT the DMSO wells), minus the profile's library-composition shift
  (median-of-ratios over the line's well-expressed genes, from the atlas: <COMPOSITION>), median across lines, minus
  the leave-drug-out well-position effect: the median of the other drugs that sat in the same position on other
  plates, using only those that do not move this gene themselves (first-pass |z| < 3; with fewer than 3 such wells
  the well is left uncorrected and flagged). z_corrected: scored against the spread of the drug wells on the
  reliable plates (median/MAD) and divided by the plate factor of the well's plate x dose group (its spread vs the
  same dose on the other plates, never below 1; plate_scale), Stouffer over the drug-dose's used wells; fdr_up /
  fdr_down: Benjamini-Hochberg over the ~1,100 drug-doses of that gene. call: up/down when the dose-level FDR < 0.10,
  >= 1.2x and >= 60% of lines moving that way. Drug summaries: best dose, Bonferroni over doses, BH over drugs
  (fdr_*_drug).
- Used wells: a drug-dose with a well on a reliable plate uses only its reliable wells; unreliable plates
  (<UNRELIABLE>) count only for drug-doses that have no other well (flag 'unreliable plate only').
- Expressed: a line expresses a gene when its level over all wells is >= 25% of the median line, >= 1 CPM and >= 2x
  the level ambient RNA alone gives (af x the gene's pooled CPM over all lines; af = what the MTAP-null lines read of
  the pooled MTAP). Lines that do not are left out of that gene's drug effects; genes expressed in < 3 lines get none;
  genes whose profiles hold a median of < 2 counts are flagged 'low counts' (so is a score built only from them).
  MTAP follows tahoe_mtap_gankyrin.py (MTAP-null lines left out); PSMD10 keeps every line and carries the
  rest-of-proteasome change (PROTEASOME_log2FC_plate_mean / PROTEASOME_z_plate_mean as in tahoe_mtap_gankyrin.py;
  PROTEASOME_z = Stouffer, as for every other gene).
- Pathway scores (pathway_scores_by_dose.csv): per well the mean over the expressed members of each member's own z
  ((corrected shift - its centre) / its spread), robust z over the reliable drug wells, divided by the plate factor,
  Stouffer per drug-dose; fold_change = the mean member fold change; top_members ranked by the member's z.
  P53_ACTIVITY = CDKN1A MDM2 FDXR ZMAT3 SESN1 BBC3 BAX + 14 more p53 targets (PMAIP1, GADD45A, SESN2, TNFRSF10B left
  out: also ATF4/CHOP-driven); FERRO_MARKERS = PTGS2 CHAC1 SLC7A11; INFLAMMASOME = NLRP3 AIM2 PYCARD CASP1 CASP4
  CASP5 IL1B IL18 GSDMD; NRF2, ISR (ATF4), UPR, HEAT_SHOCK, IFN, NFKB context sets; PROTEASOME, S_PHASE, G2M_PHASE =
  summed modules. 'context' on each gene's drug-dose names the programs with |z| >= 3 (scores that contain the gene
  itself excluded).
- p53 WT vs altered (p53_wt_vs_altered.csv): per well and line the mean corrected shift of the P53_ACTIVITY genes;
  per well the mean of the TP53-wild-type lines minus the median of the TP53-altered lines (any TP53 driver row in
  the cell-line metadata = altered), position-corrected, robust z divided by the plate factor, Stouffer, one-sided
  (more in WT). pattern: 'WT induction' (WT lines up >= 1.2x and the all-line P53_ACTIVITY z > 0) or 'relative
  (altered lines fall)'.
- Growth (selective depletion; loss_screens.csv, p53_wt_selective_growth.csv, MTAP_null_selective_drugs.csv): each
  line's share of the cells in a well vs its usual share on that plate (log2 relative abundance); mean of the group
  minus median of the other lines in the same well, position-corrected; the z includes counting noise (spread over
  the reliable plates). Negative = the group was depleted more.
- Level vs growth (level_vs_growth.csv): Spearman across lines of a gene's untreated level (DMSO CPM) and relative
  abundance after the drug (rho < 0: high-level lines depleted more); partial on the G2M level (proliferation);
  within lineage (organ effects removed from both ranks); Fisher z, position-corrected, robust z, Stouffer; FDR
  within gene (fdr; fdr_within_lineage for the within-lineage z).
- Flags: the rulebook below says what each one means and what to do with it.
"""

PANEL_FACTS = """## These data (method v3 facts, computed from this run)
- <NGENES>.
- Unreliable plates: <UNRELIABLE_R>. Replicate agreement of the same drug-dose's wells (Pearson r over the testable
  genes' z, replicate_pairs.csv; each drug-dose counted once): <REPLICATES>. Same-position pairs share any position
  artifact, and few drug-doses have a replicate at a different position on reliable plates (only those named), so
  these medians are not the reproducibility of a typical drug.
- Plate factors > 1.2 (<FACTOR_SOURCE>): <FACTORS>. Part of a noisy plate's spread may be real activity (the
  factor only ever widens), but a hit seen only there needs another plate.
- Composition: <COMPOSITION>.
- DMSO wells: <DMSO>. Wells whose position could not be corrected: <NOTCORR>.
- Drug-doses with no data (their only well failed): <NODATA>.
- Lines with usable expression (>= the minimum cells) in < 25% of wells, so they rarely enter: <THIN>.
- Drug names: <SALTS> (count each drug once).
- MTAP-null cut: <MTAPCUT>.
"""

def step_angles(S):
    A = os.path.join(S.out, "angles")
    fer = [g for g, p, _ in PANEL if p == "ferroptosis"]
    pyr = [g for g, p, _ in PANEL if p == "pyroptosis"]
    p53 = [g for g, p, _ in PANEL if p == "p53"]
    groups = {"ferroptosis": fer, "pyroptosis": pyr, "p53": p53, "napepld_trim72": ["NAPEPLD", "TRIM72"],
              "crosslinks": ANCHORS}
    added = [g for g in S.panel if g not in {x for x, _, _ in PANEL}]
    if added:
        groups["napepld_trim72"] = groups["napepld_trim72"] + added
    for name in PANEL_ANGLES:
        try:
            folder = os.path.join(A, name)
            os.makedirs(folder, exist_ok=True)
            angle_files(S, name, folder, groups[name])
        except Exception as e:  # noqa: BLE001
            log(f"  WARNING: angle {name} failed: {e!r}")
            T._to_log_file(traceback.format_exc().rstrip())
            S.failures[f"angle {name}"] = repr(e)


def angle_files(S, name, folder, genes):
    files = []
    for f in glob.glob(os.path.join(folder, "*.csv")) + glob.glob(os.path.join(folder, "*.parquet")):
        os.remove(f)                   # an earlier run's tables; brief.md, report.md, agent.log, *.py and prior/ stay

    def put(df, fname, desc):
        if df is None or not len(df):
            return
        df.to_csv(os.path.join(folder, fname), index=False)
        files.append((fname, desc))

    def put_file(src, fname, desc):
        if os.path.exists(src):
            shutil.copy2(src, os.path.join(folder, fname))
            files.append((fname, desc))
    gset = set(genes)
    put(S.pg[S.pg["gene"].isin(gset)] if hasattr(S, "pg") else None, "gene_roles.csv",
        "the genes of this angle: role, expression level, lines expressing, status (testable or why not), loss group")
    put(S.pcs if hasattr(S, "pcs") else None, "positive_controls.csv",
        "expected effects (known biology) and whether the data show them: best dose, fold change, z, FDR, verdict")
    eff = []
    for g in genes:
        if g in S.RES:
            r = S.RES[g]
            cols = ["drug", "conc", "call", "fold_change", "z_corrected", "fdr_up", "fdr_down", "n_lines", "n_lines_up",
                    "n_lines_down", "frac_lines_positive", "flags", "context", "position_effect_removed", "wells",
                    "moa_fine", "targets"] + [c for c in r.columns if c.endswith("_z") and c[:-2] in CONTEXT_SCORES]
            eff.append(r[[c for c in cols if c in r]].assign(gene=g))
    if eff:
        e = pd.concat(eff, ignore_index=True)
        e = e[["gene"] + [c for c in e.columns if c != "gene"]]
        put(e, "gene_drug_effects.csv", "every gene x drug-dose: fold change, z, FDR, call, lines up/down, flags and "
            "the context programs (their z per drug-dose); full columns in ../../results/<GENE>_drug_effects_by_dose.csv")
    ds = [S.DS[g].assign(gene=g) for g in genes if g in getattr(S, "DS", {})]
    if ds:
        d = pd.concat(ds, ignore_index=True)
        put(d[["gene"] + [c for c in d.columns if c != "gene"]], "gene_drug_summary.csv",
            "one row per gene x drug: z and fold change at every dose (ascending), best increase / decrease, "
            "dose pattern, drug-level FDR, flags and context at the best dose")
    exl = pd.read_csv(os.path.join(S.R, "expression_by_line.csv"))
    put(exl[exl["gene"].isin(gset)], "expression_by_line.csv",
        "level of each gene in each line (DMSO and all wells, CPM), % cells expressing, vs the median line, vs the "
        "pooled level (ambient RNA alone gives ~af of it), expressed (above ambient)")
    if hasattr(S, "lvl") and len(S.lvl):
        lg = gset | ({NRF2_LEVEL} if name == "ferroptosis" else set())
        put(S.lvl[S.lvl["gene"].isin(lg)], "level_vs_growth.csv",
            "does a line's untreated level predict how a drug-dose affects its growth? rho (Spearman across lines), "
            "rho_partial_G2M, rho_within_lineage, z, FDR within gene (fdr, fdr_within_lineage), z at every dose"
            + (f"; {NRF2_LEVEL} = basal NRF2 target activity" if name == "ferroptosis" else ""))
    if hasattr(S, "coreg") and len(S.coreg):
        put(S.coreg[S.coreg["gene"].isin(gset)], "coregulation_top_partners.csv",
            "top co-regulated genes / programs across drug wells (rank < 0: most negative; low-count genes left out), "
            "raw and after removing the first principal component (see ../../results/summary.txt section 8 for what "
            "it loads on)")
    if hasattr(S, "ccs"):
        put(S.ccs[S.ccs["gene"].isin(gset)], "cell_cycle_summary.csv",
            "untreated cells: level in G2M-/S-high vs -low cells (median over expressing lines): cell-cycle-linked genes")
    pw = os.path.join(S.R, "pathway_scores_by_dose.csv")
    sc = {"ferroptosis": ["FERRO_MARKERS", "NRF2", "ISR", "UPR", "HEAT_SHOCK"],
          "pyroptosis": ["INFLAMMASOME", "IFN", "NFKB"], "p53": ["P53_ACTIVITY", "ISR"],
          "napepld_trim72": [], "crosslinks": ["P53_ACTIVITY", "NRF2", "PROTEASOME"]}[name]
    if sc and os.path.exists(pw):
        t = pd.read_csv(pw)
        put(t[t["score"].isin(sc)], "pathway_scores_by_dose.csv",
            f"scores {', '.join(sc)} per drug-dose: fold change, z, FDR up/down, z at every dose, top member genes, flags")
    put_file(os.path.join(S.R, "drug_context_by_dose.csv"), "drug_context_by_dose.csv",
             "per drug-dose: cells / genes / UMIs per cell vs plate (with z) and vs the plate row (row_*), composition "
             "shift, plate factor, every program's fold change and z, flags, context")
    put_file(os.path.join(S.R, "replicate_pairs.csv"), "replicate_pairs.csv",
             "every pair of wells of the same drug-dose: r over the testable genes' z and pair_type (same position, "
             "other plate / different position / same plate / unreliable plate)")
    put_file(os.path.join(S.R, "plate_scale.csv"), "plate_scale.csv",
             "plate x dose groups: plate factor (z divided by it), its source, % |z| > 1.96 before and after")
    if name == "ferroptosis":
        put(getattr(S, "ferro", None), "ferro_markers_with_context.csv",
            "FERRO_MARKERS per drug-dose with ISR / NRF2 / UPR / heat-shock / NF-kB / IFN / P53 z and a reading (the "
            "programs that rose with the markers, or an artifact flag first; FDR < 0.10 and z >= 3 only)")
    if name == "pyroptosis":
        put(getattr(S, "reex", None), "reexpression_in_silenced_lines.csv",
            "drug effects measured only in the lines that silence a gene (e.g. GSDME; lines with a deletion row in the "
            "cell-line metadata left out), with the comparator's change (the deleted lines, pure ambient RNA, when "
            ">= 2 have data, else the expressing lines) and a reading ('re-expression' only when FDR < 0.10, not "
            "toxic, enough lines rise)")
    if name in ("pyroptosis", "ferroptosis", "p53"):
        lr = getattr(S, "loss_res", None)
        if lr is not None and len(lr):
            put(lr[lr["gene"].isin(gset)], "loss_screens.csv",
                "drugs that deplete the lines lacking a gene more than the other lines in the same wells "
                "(extra_log2_depletion < 0), z with counting noise, FDR")
        put_file(os.path.join(S.R, "loss_groups.csv"), "loss_groups.csv",
                 "genes most lines express but some lines have lost (deletion / silencing), the lines and the gap")
    if name == "p53":
        for f, desc in (("p53_wt_vs_altered.csv", "per drug-dose: extra p53-target induction in TP53-WT vs altered lines "
                                                  "in the same wells (z_wt_more, FDR, z at every dose)"),
                        ("p53_functional_status.csv", "per line: TP53 annotation and protein changes, CDKN2A deletion, "
                                                      "MTAP-null, basal p53 activity, responsiveness, functional call, "
                                                      "discordant"),
                        ("p53_reference_doses.csv", "the drug-doses that define responsiveness (strongest significant "
                                                    "non-toxic all-line P53_ACTIVITY)"),
                        ("p53_wt_selective_growth.csv", "drugs that deplete TP53-WT lines more than TP53-altered lines")):
            put_file(os.path.join(S.R, f), f, desc)
    if name == "crosslinks":
        xdesc = ("reproducibility vs the earlier run, biology links (hypotheses: Gankyrin vs p53 / NRF2 within "
                 "lineage, CDKN2A deletion / MTAP-null vs p53, MTAP-null vs ferroptosis genes; p_bh), drugs in both "
                 "the earlier run's and the panel's lists" if S.prior else
                 "biology links (hypotheses: Gankyrin vs p53 / NRF2 within lineage, CDKN2A deletion / MTAP-null vs "
                 "p53, MTAP-null vs ferroptosis genes; p_bh), drugs in both this run's MTAP / PSMD10 lists and the "
                 "panel's (no earlier run was found)")
        for f, desc in (("crosslinks.csv", xdesc),
                        ("MTAP_null_selective_drugs.csv", "the MTAP-null screen (same statistics as "
                                                          "tahoe_mtap_gankyrin.py)"),
                        ("p53_functional_status.csv", "per line: p53 annotation, basal activity, responsiveness, "
                                                      "PSMD10 level, MTAP-null"),
                        ("baseline_by_cell_line.csv", "per line: untreated levels of every extracted gene, MTAP-null "
                                                      "call, organ, drivers, TP53 annotation")):
            put_file(os.path.join(S.R, f), f, desc)
        if os.path.isdir(os.path.join(folder, "prior")):
            files.append(("prior/", "the earlier MTAP / Gankyrin run's results (summary.txt, *.csv)"))
    write_brief(S, folder, name, files, genes)


# ============================================================================= README_columns.txt
README = """Gene panel output (this folder's parent)
======================================
cells/*.parquet          One row per cell: barcode, sample (well), plate, drug, cell_line_id, n_genes, total_counts,
                         raw counts of every extracted gene (panel, anchors, context genes) and the summed PROTEASOME,
                         S_PHASE and G2M_PHASE modules. Read with pyarrow (columns=..., filters=[('drug', 'in', ...)]).
well_line.parquet / .csv One row per well x cell line: n_cells, summed counts, det_<GENE> = cells with >= 1 count.
sample_map.csv           One row per well: plate, drug, dose, well position, cells.
extracted_columns.json   The extracted genes and the members of each summed module. extract_info.json: run facts.
gene_panel.log           The run log (every step, warnings, tracebacks of failed steps); agents.log: the agents' log.
angles/<pathway>/        Agent folders: brief.md (task, methods, rules), the tables of that pathway, report.md once
                         the agents have run. reports/: NN_<pathway>.md and 00_overview.md.

Files in results/
=================
summary.txt                       Key checks and results. Start here.
panel_genes.csv                   One row per panel gene and anchor: pathway, role, also_known_as, symbol_used,
                                  in_gene_metadata, extracted, median_line_cpm (all wells), median_line_cpm_dmso,
                                  median_pct_cells_dmso, n_lines, n_lines_expressing, pooled_cpm (all lines pooled),
                                  ambient_fraction (af: what the MTAP-null lines read of the pooled MTAP), ambient_cpm
                                  (af x pooled_cpm: what a line reads from ambient RNA alone), expression_threshold_cpm
                                  (max of 25% of the median line, 1 CPM and 2 x ambient_cpm),
                                  median_counts_per_profile (raw counts per well x line profile, expressing lines),
                                  testable, status (testable / low counts / expressed in too few lines / not expressed /
                                  not in the gene metadata), lowest_lines / highest_lines (x the median line),
                                  lines_not_expressing, lines_8x_above_median (where a gene most lines lack is high,
                                  e.g. IL1B), n_effective_lines / effective_lines (the expressing lines that carry the
                                  gene's effects: a usable profile in > 50% of wells and > 0 DMSO counts),
                                  loss_group_lines, drug_effects (file or why none), n_calls_up/down
                                  (low-count genes get no calls: their changes are dominated by the pseudocount).
run_info.json                     Method version (3; tahoe_status.py reads it) and this run's settings: unreliable
                                  plates, composition normalisation, plate-factor source, atlas, earlier run, the facts
                                  the briefs state (written last: a run without it did not finish).
plate_scale.csv                   Plate x dose groups (group = plate|dose; a group with < 20 drug wells joins its
                                  plate's largest): n_wells, reliable, n_peers (the same dose on other reliable plates),
                                  factor_raw (median over genes of the group's spread / its peers' median spread),
                                  factor = max(1, factor_raw) (every z of the group is divided by it), factor_pass1,
                                  source (the atlas's plate_scale.csv, or fitted over this run's testable genes and
                                  modules), % |z| > 1.96 and > 3 before and after scaling.
plate_scale_by_gene.csv           Per gene / module / score and group: its own spread ratio (spread_ratio, as
                                  factor_raw but for this feature alone), group_factor and factor = max(group factor,
                                  spread_ratio / 1.3), the divisor of its z (plate_scale_gene in the tables): a gene
                                  noisier on one plate than the group's median gene is widened further, never
                                  narrowed; % of drug wells beyond |z| 1.96 with the group factor only and its own.
replicate_pairs.csv               Every pair of wells of the same drug-dose: plates, wells, pair_type ('same position,
                                  other plate' / 'different position' / 'same plate' / 'unreliable plate'), Pearson r of
                                  the testable genes' z, n_genes. Only 'different position' pairs are independent of a
                                  residual position artifact.
well_effects.csv.gz               One row per well: sample, plate, well, drug, conc, unreliable_plate, plate_scale,
                                  composition_shift_log2, then <GENE>_log2FC (W2) and <GENE>_z for every panel gene,
                                  anchor, score and module, and for genes and modules <GENE>_log2FC_uncorrected (W1,
                                  before the position correction) and <GENE>_position_state (0 corrected, 1 uncertain,
                                  2 not correctable) (for checking the method outside this script).
expression_by_line.csv            Long: gene, gene_set, cell line, organ, tp53_status, cpm_dmso, cpm_all_wells,
                                  pct_cells_dmso, vs_median_line, vs_pooled_level (ambient RNA alone gives ~af),
                                  expressed (>= 25% of the median line, >= 1 CPM and >= 2x the ambient level).
baseline_by_cell_line.csv         Per line: tahoe_mtap_gankyrin.py's baseline table for every extracted gene
                                  (<GENE>_cpm_dmso, <GENE>_pct_cells_dmso, <GENE>_cpm_all_wells), MTAP_null, organ,
                                  drivers, the TP53 annotation (tp53_status, tp53_changes, tp53_group) and the
                                  deletion rows of the cell-line metadata (cdkn2a_deleted, cdkn2b_deleted).
<GENE>_drug_effects_by_dose.csv   One row per drug and dose (every panel gene with drug effects and the anchors MTAP,
                                  PSMD10, CDKN2A, CDKN2B): the columns of tahoe_mtap_gankyrin.py (below), plus the
                                  context of that drug-dose: <SCORE>_log2FC / <SCORE>_z for ISR, NRF2, UPR, HEAT_SHOCK,
                                  IFN, NFKB, P53_ACTIVITY, FERRO_MARKERS, INFLAMMASOME, PROTEASOME, S_PHASE, G2M_PHASE,
                                  and 'context' = the programs with |z| >= 3 (scores containing the gene left out).
                                  PSMD10: PROTEASOME_z / _log2FC are the Stouffer context values like every gene's;
                                  PROTEASOME_z_plate_mean / _log2FC_plate_mean are tahoe_mtap_gankyrin.py's (plate
                                  mean).
<GENE>_drug_summary.csv           One row per drug (tahoe_mtap_gankyrin.drug_summary) + up_context / down_context.
context_genes_top.csv             Each context gene (P53_EXT, NRF2_CORE, ISR_ATF4, UPR_ER, HSF1_HEAT, IFN, NFKB): lines
                                  expressing, top 3 increases and decreases, number of calls. They feed the scores.
pathway_scores_by_dose.csv        Long: score, drug, conc, fold_change, log2FC (mean of the expressed members'
                                  corrected shifts), z (per well the mean of the members' own z = (shift - centre) /
                                  spread, robust z over the reliable drug wells, divided by the plate factor; Stouffer
                                  over the used wells), member_z, fdr_up/fdr_down, z_by_dose (ascending doses),
                                  dose_pattern_up/down, fdr_drug_up/down (best dose, Bonferroni over doses, BH over
                                  drugs), n_members, top_members (members with the largest |z|: fold change and z),
                                  flags (position correction uncertain: most members left uncorrected), cells/genes/
                                  UMIs per cell vs plate and vs the plate row, cell-cycle shifts. PROTEASOME, S_PHASE
                                  and G2M_PHASE rows are the summed modules (tahoe_mtap_gankyrin.py).
drug_context_by_dose.csv          Per drug-dose: cells_log2_vs_plate, genes_per_cell_log2_vs_plate,
                                  umi_per_cell_log2_vs_plate (each with a robust z, Stouffer), S/G2M shifts, every score's
                                  log2FC and z, flags, context.
ferro_markers_with_context.csv    FERRO_MARKERS per drug-dose with ISR_z, NRF2_z, UPR_z, HEAT_SHOCK_z, NFKB_z, IFN_z,
                                  P53_ACTIVITY_z and reading (z >= 3 and FDR < 0.10 only; context, not a verdict):
                                  'markers with <flag> (artifact likely)' when toxic / transcription drop / cell-cycle
                                  shift; else 'markers with ISR (+ ...)' (the programs with z >= 3: CHAC1/SLC7A11 are
                                  ATF4 targets, SLC7A11 an NRF2 target, PTGS2 NF-kB-inducible) or 'markers without ISR /
                                  NRF2 / UPR / heat shock / NF-kB'.
p53_wt_vs_altered.csv             Per drug-dose: extra_log2_p53_induction_in_WT = per well mean p53-target shift of the
                                  TP53-wild-type lines minus the median of the TP53-altered lines, position-corrected;
                                  z_wt_more (robust z over the reliable plates divided by the plate factor, Stouffer),
                                  fdr, pattern ('WT induction': wt_mean_log2 >= log2 1.2 and the all-line P53_ACTIVITY
                                  z > 0; else 'relative (altered lines fall)': sparing, not induction), fdr_drug,
                                  z_by_dose, dose_pattern, wt_mean_log2, altered_median_log2, the all-line
                                  P53_ACTIVITY fold change and z, flags.
p53_functional_status.csv         Per line: tp53_annotation, tp53_changes, cdkn2a_deleted, mtap_null,
                                  basal_p53_activity_log2 (DMSO: mean log2 of the expressed p53 targets vs the median
                                  line), p53_responsiveness_log2 (mean p53-target shift over the reference drug-doses),
                                  p53_responsiveness_se (residuals of a well-strength x line-response fit),
                                  n_reference_wells, n_reference_doses,
                                  responsiveness_rank, functional_call (vs the cut halfway between the WT and altered
                                  medians; 'uncertain' within 2 SE of it), discordant, PSMD10_cpm_dmso.
p53_reference_doses.csv           The (up to 10) strongest non-toxic all-line P53_ACTIVITY drug-doses with FDR < 0.10
                                  used for responsiveness (all non-toxic ones when fewer than 3 are significant).
p53_wt_selective_growth.csv       Growth screen TP53-WT vs TP53-altered lines (columns as MTAP_null_selective_drugs.csv;
                                  extra_log2_depletion_of_TP53_WT < 0 = WT lines depleted more).
MTAP_null_selective_drugs.csv     The earlier MTAP-null screen recomputed (same columns as in the earlier run).
loss_groups.csv                   Genes (panel, CDKN2A/B) that most lines express but >= 3 lines have lost: lines, rule
                                  ('clean 2x': lost lines < half the lowest expressing line; 'gap at ambient floor':
                                  a gap (T.null_threshold) and every lost line <= 1.5x the ambient level; 'metadata
                                  deletion': >= 3 lost lines with a deletion row), threshold_vs_median, gap_log2,
                                  clean_2x_separation, ambient_floor_vs_median, n_lines_deleted_in_metadata, levels.
loss_screens.csv                  Per loss group and drug-dose: extra_log2_depletion (mean of the lost lines minus median
                                  of the others in the same well, position-corrected; < 0 = lost lines depleted more),
                                  z_selective (well noise + counting noise), fdr_selective, fdr_drug, z_by_dose,
                                  dose_pattern, delta_tissue_matched (vs other lines of the same organ), group_mean_log2,
                                  rest_median_log2, all_cells_log2_vs_plate.
reexpression_in_silenced_lines.csv  Per loss-group gene and drug-dose: the drug effect measured only in the lines that
                                  lost the gene and have no deletion row for it in the cell-line metadata (a deleted
                                  gene cannot be re-expressed: one row 'deleted in the cell-line metadata' when every
                                  lost line is deleted, e.g. CDKN2A/B), fold_change, z_corrected, fdr_up, lines up,
                                  comparator (the lines DELETED for the gene in the same wells, which read pure ambient
                                  RNA, when >= 2 have data; else the expressing lines) with deleted_lines_fold_change /
                                  _z and expressing_lines_fold_change / _z, reading (z >= 3 only): 're-expression in
                                  the lost lines' (>= 1.41x, > 2x the comparator's change, FDR < 0.10, no toxic /
                                  transcription-drop flag, >= half the lost lines measured, >= 2 of them up, >= 60%
                                  above zero, a dose pattern that is not 'inconsistent across doses', unless the row
                                  is the drug's top dose with its strongest z); 'lost lines read
                                  ambient only: not interpretable' (the lost lines' median DMSO CPM is <= 1.5 x
                                  ambient_cpm, or, with >= 2 deleted lines, inside their range: they cannot be told
                                  from ambient RNA); 'not interpretable (why)'; 'rises in the lost lines (ambient RNA /
                                  toxicity?)'; 'rises in all lines (ambient RNA follows)'. z_by_dose, dose_pattern,
                                  flags, context, lost_lines_median_cpm_dmso, deleted_lines_cpm_dmso_range,
                                  ambient_cpm.
level_vs_growth.csv               Long: gene, drug, conc, rho (Spearman across lines of the untreated level vs relative
                                  abundance after the drug), rho_partial_G2M (proliferation removed), rho_within_lineage
                                  (organ removed from both ranks), z (Fisher z, position-corrected, robust z, Stouffer),
                                  z_within_lineage, fdr (within gene, two-sided), fdr_within_lineage (the same for
                                  z_within_lineage), fdr_drug, fdr_drug_within_lineage, z_by_dose,
                                  dose_pattern_depleted_more, reading, n_lines, level_source (DMSO CPM; all-wells CPM
                                  for lines with < 20 DMSO counts). Gene NRF2_basal_score = basal NRF2 target activity
                                  (DMSO; NFE2L2 mRNA does not report NRF2 activity).
level_vs_growth_top.csv           The 5 strongest 'depleted more' and 2 'spared' drug-doses per gene, sorted by fdr.
cell_cycle_by_line.csv            Untreated (DMSO) cells, per line and gene: log2 level in G2M-high vs G2M-low quartile
                                  cells (and S), cell-level Spearman with the G2M and S scores (normalised by counts
                                  outside the cycle genes), expressed.
cell_cycle_summary.csv            Per gene: medians over the expressing lines, lines higher in G2M cells.
coregulation_matrix.csv           Pearson r across drug wells of the corrected per-well shifts (W2) of every gene,
                                  score and module (low-count genes left out); coregulation_matrix_minus_pc1.csv: after
                                  removing the first principal component (summary.txt section 8: what it loads on).
coregulation_top_partners.csv     Per panel gene and anchor: top 10 partners (rank 1-10) and most negative (rank -1..-3),
                                  raw r and after removing PC1 (scores containing the gene left out).
crosslinks.csv                    category (reproducibility / biology / shared top drugs), comparison, n, statistic,
                                  value, spearman (reproducibility), rho_within_lineage and p_within_lineage (biology
                                  correlations; the reading uses them), auc (group vs other lines: P(group > other)), p,
                                  p_bh (BH over the biology rows of p_within_lineage, or of p for group comparisons),
                                  expected, reading.
                                  Reproducibility: well positions, MTAP-null calls, MTAP / PSMD10 drug z, MTAP-null
                                  screen and Gankyrin level screen vs the earlier run (max |difference|; 0 expected
                                  when both runs read the same files with the same --min-cells and method, else
                                  'differs by design'). Shared top drugs: drugs in both an MTAP / PSMD10 list (drug-level
                                  FDR < 0.10; the earlier run's, else this run's) and a panel list (FDR < 0.10 at a
                                  dose, or a call); expected = the number shared by chance, matched for drug activity
                                  (deciles of the atlas's n_sig_genes, else of this run's genes with a call).
positive_controls.csv             expectation, expected_at_24h (robust / uncertain: an absent uncertain control says
                                  little), readout, drug (found by name, mechanism or target; 'not in data'),
                                  best_dose (strongest in the expected direction), fold_change, z, fdr,
                                  rank_among_drug_doses (of 'of'), z_by_dose, flags, direction, verdict (clear: z >= 3,
                                  FDR < 0.10 and >= 1.2x; weak: z >= 2; absent; not in data; not testable).
well_position_effects.csv         Per gene and well position: median plate-corrected shift of all drugs at that
                                  position, z vs other positions (the artifact the leave-drug-out correction removes).
plate_dmso_offsets.csv            Per gene and plate: how far the plate's DMSO wells sit from its drug-well median.
calibration.csv                   Per gene: % drug wells with |z| > 1.96 (~5% expected) and > 3, DMSO wells, null spread.
excluded_failed_wells.csv         Wells with < 1/8 of the plate's usual cells while the same drug was fine elsewhere.

Columns of the drug-effect tables (from tahoe_mtap_gankyrin.py)
---------------------------------------------------------------
log2FC_corrected       Method v3: plate baseline = median of the plate's drug wells for the same line; minus the
                       profile's composition shift (from the atlas, when computed); median over the expressing lines
                       (a well needs >= 5 of them measured; a gene measured in fewer lines in a typical well, e.g.
                       one carried by a few lines (panel_genes.csv effective_lines): one); minus the
                       leave-drug-out well-position effect (only donor wells whose own first-pass |z| < 3
                       for this gene). fold_change = 2 ** log2FC_corrected. Mean over the drug-dose's used wells
                       (reliable plates; unreliable ones only when the drug-dose has no other well).
z_corrected            Robust z against the drug wells of the reliable plates (median/MAD), divided by the gene's plate
                       factor of the well's plate x dose group (plate_scale_gene: the group's factor, plate_scale,
                       or more where this gene alone is noisier there; plate_scale_by_gene.csv); Stouffer over the
                       used wells.
fdr_up, fdr_down       Benjamini-Hochberg over all drug-doses of the gene, one-sided.
n_lines_up/down        Lines with a per-line z > 2 and > 1.2x (down: < -2, < 1/1.2). n_lines = lines measured.
frac_lines_positive    Share of lines whose corrected change is above zero (frac_lines_negative: below).
call                   up/down when FDR < 0.10 (dose-level), >= 1.2x and >= 60% of lines move that way.
flags                  toxic: < half the plate's usual cells, also < half the plate row's where that row is itself
                       shifted (|row_cells_log2| > 0.8), the best used well lost cells too (cells_log2_best_well <
                       -0.5), and no
                       higher dose of the drug kept > half (dose-consistent); else < half = low cells (technical?):
                       not confirmed as drug-caused (a row that lost cells, a lower dose killing more than a higher
                       one as with antimitotics, one well of several) - not a reason to dismiss the expression
                       changes; 'toxic' at the top dose rests on one well's cell count (weak evidence alone);
                       plate-row cell shift: the row's other drug wells moved (|row_cells_log2| > 0.8 or
                       row_umi_per_cell_log2 < -0.4); transcription drop: genes per cell -0.3 / UMIs per cell -0.5
                       log2 vs the plate and vs the row; cell-cycle shift: S or G2M module > 1.41x (> 1.19x with
                       |z| >= 4); composition shift: |composition_shift_log2| >= 0.2; noisy plate (z scaled):
                       plate_scale or plate_scale_gene > 1.2; unreliable plate only; whole proteasome up/down (PSMD10
                       only); position not
                       correctable / position correction uncertain (a used well had < 3 other-drug / clean donor
                       wells: left uncorrected); position effect removed (> 0.2 log2); wells disagree (from the
                       atlas); low counts. ('plate DMSO offset' is a column only; it never changes corrected values.)
plate_scale, plate_scale_gene, composition_shift_log2, row_cells_log2, row_umi_per_cell_log2, row_genes_per_cell_log2,
cells_log2_best_well, position_clean_donors, position_effect_pass1, unreliable_plate_only, n_wells_left_out_unreliable,
wells_disagree, replicate_r   The method-v3 inputs of the flags (tahoe_mtap_gankyrin.py README_columns.txt).
log2FC_vs_DMSO_uncorrected   Old-style estimate against the plate's DMSO wells (for comparison only).
position_effect_removed, plate_dmso_offset, pct_cells_expressing_change, level_in_expressing_cells_log2,
cells_log2_vs_plate, genes_per_cell_log2_vs_plate, umi_per_cell_log2_vs_plate, S_PHASE_shift_log2,
G2M_PHASE_shift_log2   As in tahoe_mtap_gankyrin.py (see its README_columns.txt).
Drug summaries         z_by_dose / log2FC_by_dose in ascending dose order; up_pattern / down_pattern; p/fdr_*_drug:
                       best dose, Bonferroni over doses, then BH over drugs.
"""


# ============================================================================= analyze
def core(label, fn):
    """A step every later analysis needs: if it fails, stop with a clear message (traceback in the run log)."""
    try:
        return fn()
    except Exception as e:  # noqa: BLE001
        T._to_log_file(traceback.format_exc().rstrip())
        sys.exit(f"analyze stopped: {label} failed: {e!r} (traceback in the run log, gene_panel.log)")


def cmd_analyze(args):
    quiet()
    t0 = time.time()
    S = Run(args)
    core("loading the extraction", lambda: load(S))
    log("Baseline by cell line ...")
    core("baseline by cell line", lambda: step_baseline(S))
    log("Expression of every extracted gene by line ...")
    core("expression by line", lambda: step_expression(S))
    log("Position passes and plate factors (method v3) ...")
    core("position passes and plate factors", lambda: step_prepare(S))
    log("Well covariates ...")
    S.ctx = core("well covariates", lambda: T.well_context(S.wl, S.sm, S.cols, S.M))
    jf = os.path.join(S.out, "extracted_columns.json")
    S.modules = json.load(open(jf, encoding="utf-8")).get("modules", {}) if os.path.exists(jf) else {}
    step_effects(S)
    if not S.RES:
        sys.exit("No gene could be analysed (see the warnings above)")
    log("Pathway scores and drug context ...")
    S.attempt("pathway scores", lambda: step_scores(S))
    S.attempt("drug context", lambda: step_context(S))
    S.attempt("gene tables", lambda: step_gene_tables(S))
    if "FERRO_MARKERS" in S.SC and hasattr(S, "ctab"):
        S.attempt("ferroptosis markers context", lambda: step_ferro_context(S))
    log("p53: WT vs altered, functional status ...")
    if "P53_ACTIVITY" in S.SC:
        S.attempt("p53 WT vs altered", lambda: step_p53(S))
        if hasattr(S, "P53"):
            S.attempt("p53 functional status", lambda: step_p53_function(S))
    log("Growth: MTAP-null, TP53-WT, loss groups, level vs growth ...")
    S.n = S.attempt("abundance table", lambda: T.abundance(S.wl, S.sm, S.base))
    if S.n is not None:
        S.attempt("MTAP-null screen", lambda: mtap_null_screen(S))
        S.attempt("TP53-WT selective growth", lambda: step_p53_growth(S))
        S.attempt("loss screens", lambda: step_loss(S))
        S.attempt("level vs growth", lambda: step_levels(S))
    log("Cell cycle (DMSO cells) ...")
    S.attempt("cell cycle", lambda: step_cell_cycle(S))
    log("Co-regulation, cross-links, positive controls ...")
    S.attempt("co-regulation", lambda: step_coreg(S))
    S.attempt("cross-links", lambda: step_crosslinks(S))
    S.attempt("positive controls", lambda: step_controls(S))
    S.attempt("quality tables", lambda: step_quality(S))
    S.facts = S.attempt("method v3 facts", lambda: v3_facts(S)) or {}
    S.attempt("per-well table", lambda: step_well_effects(S))
    S.attempt("panel genes table", lambda: step_panel_genes(S))
    log("Writing summary and agent folders ...")
    S.attempt("summary", lambda: write_summary(S))
    with open(os.path.join(S.R, "README_columns.txt"), "w", encoding="utf-8") as fh:
        fh.write(README)
    step_angles(S)
    if S.failures:
        S.attempt("summary (failures)", lambda: write_summary(S))
    write_panel_run_info(S)
    log(f"Analysis done in {(time.time() - t0) / 60:.1f} min" + (f"; {len(S.failures)} step(s) failed: "
                                                                 + ", ".join(S.failures) if S.failures else "")
        + f". Start with {os.path.join(S.R, 'summary.txt')}")


# ============================================================================= check
def cmd_check(args):
    """Preflight: is this machine ready for the panel run? One line per check ([ok] / [warn] / [FAIL])."""
    bad = []

    def say(ok, msg, fatal=True):
        if not ok and fatal:
            bad.append(msg)
        print(f"[{'ok  ' if ok else ('FAIL' if fatal else 'warn')}] {msg}", flush=True)

    import pyarrow as pa
    v = sys.version_info
    say(v >= (3, 9), f"Python {v.major}.{v.minor}.{v.micro}" + ("" if v >= (3, 10) else " (agents need 3.10+)"),
        fatal=v < (3, 9))
    say(True, f"numpy {np.__version__}, pandas {pd.__version__}, pyarrow {pa.__version__}; tahoe_mtap_gankyrin.py "
              f"found ({os.path.abspath(T.__file__)})")
    os.makedirs(args.out, exist_ok=True)
    idx = T.discover(args.data, args.out, refresh=args.reindex)
    ne = len(idx["expression"])
    say(ne > 0, f"{ne:,} expression files under {os.path.abspath(args.data)}" + ("" if ne else ": wrong --data folder?"))
    if 0 < ne < 3000 and not args.limit_files:
        say(False, f"only {ne:,} expression files (the full dataset has ~3,388): is the download complete? When it "
                   "is, run again with --reindex", fatal=False)
    for k, fatal, why in (("gene", True, "needed"), ("sample", True, "needed (doses, well positions)"),
                          ("cell_line", False, "missing: no organ, no TP53 annotation (use --tp53-wt / --tp53-altered)"),
                          ("drug", False, "missing: no mechanisms / targets; positive controls by name only")):
        say(bool(idx[k]), f"{k} metadata: {len(idx[k])} file(s)" + ("" if idx[k] else f" - {why}" + REINDEX_HINT),
            fatal=fatal)
    n_cols = 120
    if idx["gene"]:
        gm = T.read_tables(idx["gene"], ["token_id", "gene_symbol"])
        symbols = gm["gene_symbol"].dropna().astype(str).tolist()
        gt = gene_table(args, symbols)
        sym = resolve_symbols(list(gt["gene"]) + [g for g, _ in context_genes()], symbols)
        miss = [g for g in gt["gene"] if g not in sym]
        aka = ", ".join(f"{g} = {AKA[g]}" for g in gt["gene"] if g in AKA and g in sym)
        say(not miss, f"panel genes in the gene metadata: {len(gt) - len(miss)}/{len(gt)}" +
            (f"; missing: {', '.join(miss)} (they will be reported as missing)" if miss else f" (aliases: {aka})"),
            fatal=False)
        cmiss = [g for g, _ in context_genes() if g not in sym]
        if cmiss:
            say(False, f"context genes missing from the gene metadata: {', '.join(cmiss)}", fatal=False)
        n_cols = len(sym) + 3
        targets = [g for g in ANCHORS] + [sym[g] for g in list(gt["gene"]) + [g for g, _ in context_genes()]
                                          if g in sym and g not in ANCHORS]
        gm2 = T.read_tables(idx["gene"], ["token_id", "gene_symbol", "ensembl_id"])
        _t, cols, _l, report = T.build_columns(gm2, list(dict.fromkeys(targets[len(ANCHORS):])))
        prob = mixed_gene_list_problem(args.out, report, cols)
        say(prob is None, "no earlier extraction with another gene list in --out" if prob is None else prob)
    if idx["cell_line"]:
        cl = T.read_tables(idx["cell_line"])
        if {"Cell_ID_Cellosaur", "Driver_Gene_Symbol"} <= set(cl.columns):
            tp = cl.loc[cl["Driver_Gene_Symbol"].astype(str).str.upper() == "TP53", "Cell_ID_Cellosaur"].nunique()
            n = cl["Cell_ID_Cellosaur"].nunique()
            say(tp > 0, f"TP53 annotation: {tp} of {n} lines have a TP53 driver row (= altered; the others count as "
                        "wild type)", fatal=False)
        else:
            say(False, "cell-line metadata has no driver columns: no TP53 annotation", fatal=False)
    p = prior_dir(args)
    if p:
        have = [f for f in ("MTAP_null_selective_drugs.csv", "Gankyrin_level_vs_drug_response.csv",
                            "MTAP_drug_effects_by_dose.csv") if os.path.exists(os.path.join(p, "results", f))]
        say(True, f"earlier MTAP / Gankyrin run found: {os.path.abspath(p)} ({len(have)}/3 key result files)")
    else:
        say(False, "earlier MTAP / Gankyrin run not found (" + ("--prior none" if (args.prior or "").lower() == "none"
                   else f"looked in {os.path.abspath(args.prior or os.path.join(args.data, 'mtap_gankyrin'))}")
            + "): cross-links will use this run only", fatal=False)
    atl = T.atlas_dir(args)
    if atl:
        v = T.atlas_effects_version(atl)
        say(v >= T.METHOD_VERSION, f"atlas {os.path.abspath(atl)}: " + (
            f"effects v{v}: its composition shift, plate factors and 'wells disagree' will be used" if v >= 3 else
            f"effects v{v}, older than method v3: run the atlas first (tahoe_atlas.py effects) to use its composition "
            "shift and plate factors" if v else "not computed: no composition normalisation, plate factors fitted "
                                                "over the panel's genes (run the atlas first to use its)"), fatal=False)
    n_files = min(ne, args.limit_files or ne) or 3388
    need = cells_estimate_gb(n_files, n_cols) * 1.3 + 1.0
    free = shutil.disk_usage(args.out).free / 1e9
    say(free >= need, f"disk: {free:.0f} GB free at {os.path.abspath(args.out)}, ~{need:.1f} GB needed (per-cell "
                      f"files ~{cells_estimate_gb(n_files, n_cols):.1f} GB for {n_files:,} files, {n_cols} columns)")
    kind = T.disk_kind(args.data)
    if kind == "hdd":
        say(False, "disk type: the data seem to sit on a hard drive (HDD); parallel readers make it seek, so "
                   "--workers 2 usually reads faster (some cloud SSDs also report as HDD)", fatal=False)
    else:
        say(True, "disk type: SSD" if kind == "ssd" else "disk type: could not be determined (on a hard drive "
                                                          "--workers 2 usually reads faster)")
    mem, cpus = T.mem_available_gb(), os.cpu_count() or 1
    w = args.workers or T.auto_workers()
    say(mem is None or mem >= 4, f"memory: {mem or 0:.0f} GB free, {cpus} CPUs -> {w} extract workers; extract: up to "
                                 "~3 GB per worker + ~1 GB main process; analyze ~2-4 GB",
        fatal=mem is not None and mem < 2)
    A = atlas(required=False, quiet=True)
    todo = []
    if A is None:
        old = os.path.exists(os.path.join(HERE, "tahoe_atlas.py"))
        say(False, "tahoe_atlas.py next to this script is an older version (needed only for the agents step)" if old
            else "tahoe_atlas.py not next to this script (needed only for the agents step)", fatal=False)
        todo.append(("copy the current tahoe_atlas.py over the old one" if old else "put tahoe_atlas.py") +
                    " next to tahoe_gene_panel.py")
    else:
        try:
            import claude_agent_sdk
            say(True, f"claude-agent-sdk {getattr(claude_agent_sdk, '__version__', '?')}")
        except ImportError:
            todo.append(A.sdk_hint())
            say(False, f"claude-agent-sdk not installed (needed only for the agents step): {A.sdk_hint()}", fatal=False)
        keys = ["ANTHROPIC_API_KEY", "ANTHROPIC_AUTH_TOKEN", "CLAUDE_CODE_USE_BEDROCK", "CLAUDE_CODE_USE_VERTEX",
                "CLAUDE_CODE_OAUTH_TOKEN"]
        auth = any(os.environ.get(k) for k in keys)
        if not auth:
            todo.append(A.key_hint())
        say(auth, "API key found in the environment" if auth else "ANTHROPIC_API_KEY not set (needed only for the "
                                                                   "agents step)", fatal=False)
        if args.sandbox:
            prob = A.sandbox_problem()
            say(prob is None, prob or "--sandbox: available", fatal=False)
    print()
    if bad:
        print(f"{len(bad)} problem(s) to fix first (see FAIL lines above).")
        sys.exit(1)
    hint_workers = args.workers or (2 if kind == "hdd" else 0)
    print("Ready:  " + long_run_hint("all", same_folders(args, hint_workers), args.out))
    print("Agents step: " + (f"ready too, after 'all':  {long_run_hint('agents', same_folders(args), args.out)}"
                             if not todo else "before it: " + ";  ".join(todo)))


# ============================================================================= bundle
BUNDLE = [("results/summary.txt", None), ("results/README_columns.txt", None), ("results/positive_controls.csv", None),
          ("results/panel_genes.csv", None), ("results/crosslinks.csv", None), ("results/calibration.csv", None),
          ("results/pathway_scores_by_dose.csv", None), ("results/drug_context_by_dose.csv", None),
          ("results/ferro_markers_with_context.csv", 300), ("results/p53_wt_vs_altered.csv", 400),
          ("results/p53_functional_status.csv", None), ("results/p53_reference_doses.csv", None),
          ("results/p53_wt_selective_growth.csv", 300), ("results/MTAP_null_selective_drugs.csv", 300),
          ("results/loss_groups.csv", None), ("results/loss_screens.csv", 3000),
          ("results/reexpression_in_silenced_lines.csv", 1500), ("results/level_vs_growth_top.csv", None),
          ("results/cell_cycle_summary.csv", None), ("results/coregulation_top_partners.csv", None),
          ("results/context_genes_top.csv", None), ("results/well_position_effects.csv", None),
          ("results/plate_dmso_offsets.csv", None), ("results/excluded_failed_wells.csv", None),
          ("results/baseline_by_cell_line.csv", None), ("results/expression_by_line.csv", None),
          ("results/run_info.json", None), ("results/plate_scale.csv", None), ("results/replicate_pairs.csv", None),
          ("results/plate_scale_by_gene.csv", None),
          ("results/well_effects.csv.gz", None),
          ("extract_info.json", None), ("extracted_columns.json", None), ("well_position_check.csv", None),
          ("sample_map.csv", None)]


def cmd_bundle(args):
    """One small zip to upload to Claude: the key tables (to check the numbers before the agents), then the reports
    and agent logs once the agents have run (only reports newer than this analysis: a rerun of analyze makes the
    earlier ones out of date)."""
    out = args.out
    path = os.path.join(out, "gene_panel_bundle.zip")
    if not os.path.isdir(out):
        sys.exit(f"{out} does not exist: run 'all' first")
    A = atlas(required=False)
    summ = os.path.join(out, "results", "summary.txt")
    t_an = os.path.getmtime(summ) if os.path.exists(summ) else 0.0

    def current(fs):
        return [f for f in fs if os.path.exists(f) and os.path.getmtime(f) >= t_an]
    allreps = sorted(glob.glob(os.path.join(out, "reports", "*.md")))
    reps = current(allreps)
    items = list(BUNDLE) + [(os.path.relpath(f, out), None) for f in
                            sorted(glob.glob(os.path.join(out, "results", "*_drug_summary.csv")))]
    n_tables = 0
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as z:
        for rel, nrows in items:
            src = os.path.join(out, rel)
            if not os.path.exists(src):
                continue
            arc = os.path.join("computation", rel).replace(os.sep, "/")
            try:
                df = pd.read_csv(src) if nrows and src.endswith(".csv") else None
            except pd.errors.EmptyDataError:               # an empty table (e.g. no loss group): kept as it is
                df = None
            if df is not None:
                if "gene" in df and df["gene"].nunique() > 1:      # cap per gene, so no gene drops out
                    df = df.groupby("gene", sort=False, group_keys=False).head(max(100, nrows // df["gene"].nunique()))
                else:
                    df = df.head(nrows)
                z.writestr(arc, df.to_csv(index=False))
            else:
                z.write(src, arc)
            n_tables += 1
        for f in sorted(glob.glob(os.path.join(out, "angles", "*", "brief.md"))):   # the agents' briefs (analyze)
            z.write(f, "briefs/" + os.path.basename(os.path.dirname(f)) + ".md")
        for f, arc in ((os.path.join(out, "gene_panel.log"), "computation/gene_panel.log"),
                       (os.path.join(out, "agents.log"), "agent_logs/agents.log")):
            if os.path.isfile(f):
                if A is not None:
                    A.add_log(z, f, arc)
                else:
                    z.write(f, arc)
        for f in reps + current([os.path.join(out, "reports", "agents_summary.csv")]):
            z.write(f, "reports/" + os.path.basename(f))
        for f in current(sorted(glob.glob(os.path.join(out, "angles", "*", "agent.log")))):
            z.write(f, "agent_logs/" + os.path.basename(os.path.dirname(f)) + ".log")
    if len(allreps) > len(reps):
        log(f"  {len(allreps) - len(reps)} report(s) older than this analysis left out of the bundle (out of date; "
            "rerun the agents for new ones)")
    if not n_tables and not reps:
        os.remove(path)
        log("Nothing to bundle yet: run 'all' (or 'analyze') first")
        return
    what = f"{n_tables} result files" + (f" and {len(reps)} reports" if reps else "")
    log(f"Bundled {what} -> {os.path.abspath(path)} ({os.path.getsize(path) / 1e6:.1f} MB). "
        + ("Upload it" if sys.platform == "win32" else "Download it (e.g. scp) and upload it") + " to Claude"
        + (" to turn the reports into a document." if reps else " to check the numbers before running the agents."))


# ============================================================================= agents
def cmd_agents(args):
    A = atlas()
    D = {"ang": os.path.join(args.out, "angles"), "rep": os.path.join(args.out, "reports")}
    if not glob.glob(os.path.join(D["ang"], "*", "brief.md")):
        sys.exit(f"No agent folders with a brief.md under {D['ang']}: run 'analyze' (or 'all') first")
    A.cmd_agents(args, D=D, order=PANEL_ANGLES, synth_task=PANEL_SYNTH, append=A.agent_text(PANEL_APPEND))
    if not args.dry_run:
        cmd_bundle(args)


# ============================================================================= main
def next_steps(args):
    lim = args.limit_files
    try:                                       # 'analyze' alone on a trial extraction is a trial too
        with open(os.path.join(args.out, "extract_info.json"), encoding="utf-8") as fh:
            lim = lim or json.load(fh).get("limit_files") or 0
    except (OSError, ValueError):
        pass
    if lim:                                    # a trial: the next step is the full run, not the agents
        full = os.path.join(args.data, "gene_panel")
        return (f"Trial done ({lim} file{'s' if lim != 1 else ''}): check "
                f"{os.path.join(args.out, 'results', 'summary.txt')}, then start the full run: "
                + long_run_hint("all", same_folders(argparse.Namespace(data=args.data, out=full),
                                                    getattr(args, "workers", 0)), full))
    A = atlas(required=False)
    key = A.key_hint() if A else "set ANTHROPIC_API_KEY"
    sdk = A.sdk_hint() if A else "pip install claude-agent-sdk"
    return (f"Next: send {os.path.join(args.out, 'gene_panel_bundle.zip')} to Claude to check the numbers; then the "
            f"agents: {key}, {sdk}, then {long_run_hint('agents', same_folders(args), args.out)}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("command", choices=["check", "extract", "analyze", "all", "agents", "bundle"])
    ap.add_argument("--data", default=".", help="Tahoe-100M download folder (default: current folder)")
    ap.add_argument("--out", default=None, help="output folder (default: <data>/gene_panel)")
    ap.add_argument("--workers", type=int, default=0, help="extract: parallel processes (default: auto)")
    ap.add_argument("--batch-size", type=int, default=20000, help="extract: cells per batch per worker")
    ap.add_argument("--limit-files", type=int, default=0, help="trial run on the first N expression files "
                                                               "(use a separate --out)")
    ap.add_argument("--layout", default=None, help="CSV with columns sample,well to override well positions")
    ap.add_argument("--min-cells", type=int, default=T.MIN_CELLS, help="min cells per line per well (default 30)")
    ap.add_argument("--reindex", action="store_true", help="rescan the download folder for its parquet files")
    ap.add_argument("--genes", default="", help="extra genes 'SYM[:pathway],...' (aliases accepted); extract into a "
                                                "new --out")
    ap.add_argument("--mtap-null", default=None, help="comma-separated cell lines to treat as MTAP-null")
    ap.add_argument("--tp53-wt", default=None, help="comma-separated cell lines to treat as TP53 wild type")
    ap.add_argument("--tp53-altered", default=None, help="comma-separated cell lines to treat as TP53 altered")
    ap.add_argument("--prior", default=None, help="earlier MTAP/Gankyrin output (default: <data>/mtap_gankyrin when "
                                                  "it exists; 'none' to ignore)")
    ap.add_argument("--unreliable-plates", default=None,
                    help="plates kept per well but left out of pooled drug-doses, comma-separated, or 'none' "
                         f"(default: {', '.join(T.UNRELIABLE_PLATES)} when present)")
    ap.add_argument("--atlas", default=None, help="computed atlas whose method-v3 exports (composition shift, plate "
                                                  "factors, 'wells disagree') to use, and whose look-ups the briefs "
                                                  "offer (default: <data>/atlas; 'none')")
    ap.add_argument("--angles", default="", help="agents: comma-separated subset of " + ",".join(PANEL_ANGLES))
    ap.add_argument("--model", default="sonnet", help="agent model: sonnet, opus, or a full model ID")
    ap.add_argument("--budget", type=float, default=5.0, help="USD cap per agent")
    ap.add_argument("--max-turns", type=int, default=80, help="turns per agent")
    ap.add_argument("--parallel", type=int, default=3, help="agents running at once")
    ap.add_argument("--permission-mode", default="dontAsk", help="Claude Code permission mode of the agents")
    ap.add_argument("--web", action="store_true", help="let agents use web search to check the literature")
    ap.add_argument("--sandbox", action="store_true", help="run agent shell commands sandboxed (not on Windows)")
    ap.add_argument("--redo", action="store_true", help="agents: rerun even if a report is up to date")
    ap.add_argument("--skip-overview", action="store_true", help="agents: no overview report")
    ap.add_argument("--dry-run", action="store_true", help="agents: write the prompts, call nothing")
    args = ap.parse_args()
    args.out = args.out or os.path.join(args.data, "gene_panel")
    T.MIN_CELLS = args.min_cells
    T.safe_console()
    if args.command == "check":
        return cmd_check(args)
    if args.command == "bundle":
        return cmd_bundle(args)
    os.makedirs(args.out, exist_ok=True)
    T.start_run_log(os.path.join(args.out, "agents.log" if args.command == "agents" else "gene_panel.log"),
                    "tahoe_gene_panel.py " + " ".join(sys.argv[1:]))
    try:
        with T.keep_awake(f"tahoe_gene_panel.py {args.command}"):
            if args.command in ("extract", "all"):
                cmd_extract(args)
            if args.command in ("analyze", "all"):
                cmd_analyze(args)
                cmd_bundle(args)
                log(next_steps(args))
            if args.command == "agents":
                cmd_agents(args)
    except SystemExit as e:
        T.log_exit(e)
        raise


if __name__ == "__main__":
    main()
