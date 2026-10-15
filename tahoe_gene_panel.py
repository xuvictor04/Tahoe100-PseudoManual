#!/usr/bin/env python3
r"""
tahoe_gene_panel.py - the MTAP / Gankyrin trial (tahoe_mtap_gankyrin.py) generalized to a gene panel: ferroptosis,
pyroptosis and p53 genes plus NAPEPLD (NAPE-PLD) and TRIM72 (MG53), with the same artifact corrections, cross-linked
to the earlier MTAP / Gankyrin run, and one Claude agent per pathway that writes a report.

Put this file next to tahoe_mtap_gankyrin.py (and tahoe_atlas.py, which the agents step uses) in your Tahoe-100M
folder and run from there:

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
Every run appends to gene_panel/gene_panel.log and keeps the computer from sleeping while it runs.

The earlier MTAP / Gankyrin output (<data>/mtap_gankyrin) is read when present (--prior DIR; --prior none ignores
it). Extra genes: --genes "SYM[:pathway],..." (aliases FSP1, DFNA5, ASC, MG53, NAPE-PLD, P21, PUMA, NOXA accepted),
into a NEW --out: per-cell files of an earlier gene list are never mixed with a new one.
Same corrections as tahoe_mtap_gankyrin.py: plate baseline = median of the plate's drug wells (never DMSO);
leave-drug-out well-position correction; robust z against all drug wells; Stouffer over plates; BH FDR; failed wells
removed; lines that do not express a gene left out for that gene; growth z with counting noise; toxicity,
transcription-drop and cell-cycle flags on every drug-dose.
Agents (same options as tahoe_atlas.py): --model sonnet|opus --budget 5 (USD cap per agent) --max-turns 80
--parallel 3 --angles ferroptosis,p53 --dry-run --redo --skip-overview --web --sandbox (Linux/macOS only).
Requires numpy, pandas, pyarrow (claude-agent-sdk and tahoe_atlas.py for the agents step).
"""

import argparse
import glob
import json
import math
import os
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
    ("CDKN1A", "p53", "(p21) Best single reporter of p53 activity"),
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
                "PSMD10": "(Gankyrin) proteasome assembly chaperone; promotes MDM2-mediated p53 degradation "
                          "(earlier analysis)",
                "CDKN2A": "p16INK4a / p14ARF (ARF restrains MDM2); 9p21 neighbour of MTAP",
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
# PMAIP1, GADD45A and SESN2 are left out of P53_ACTIVITY on purpose: they are also strongly ATF4/stress-driven
P53_ACTIVITY = ["CDKN1A", "MDM2", "FDXR", "ZMAT3", "SESN1", "BBC3", "BAX"] + \
    [g for g in CONTEXT["P53_EXT"] if g not in ("CCNG1", "BTG2", "TIGAR")]
SCORES = {"P53_ACTIVITY": P53_ACTIVITY, "FERRO_MARKERS": ["PTGS2", "CHAC1", "SLC7A11"],
          "INFLAMMASOME": ["NLRP3", "AIM2", "PYCARD", "CASP1", "CASP4", "CASP5", "IL1B", "IL18", "GSDMD"],
          "NRF2": CONTEXT["NRF2_CORE"], "ISR": CONTEXT["ISR_ATF4"], "UPR": CONTEXT["UPR_ER"],
          "HEAT_SHOCK": CONTEXT["HSF1_HEAT"], "IFN": CONTEXT["IFN"], "NFKB": CONTEXT["NFKB"]}
MODULES = ["PROTEASOME", "S_PHASE", "G2M_PHASE"]          # summed modules of tahoe_mtap_gankyrin.py
CONTEXT_SCORES = ["ISR", "NRF2", "UPR", "HEAT_SHOCK", "IFN", "NFKB", "P53_ACTIVITY", "FERRO_MARKERS", "INFLAMMASOME",
                  "PROTEASOME", "S_PHASE", "G2M_PHASE"]
CTX_VARS = ["cells_log2_vs_plate", "genes_per_cell_log2_vs_plate", "umi_per_cell_log2_vs_plate"]
FERRO_LEVEL_GENES = ["GPX4", "ACSL4", "AIFM2", "SLC7A11", "NFE2L2", "LPCAT3", "TFRC"]
MIN_EXPR_CPM = 1.0        # a line expresses a gene if its level (all wells) is >= this many CPM ...
EXPR_FRAC = 0.25          # ... and >= this fraction of the median line
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
          "crosslinks": "Cross-links to the earlier MTAP / Gankyrin analysis"}
DNA_DAMAGE = {"names": ["Doxorubicin", "Epirubicin", "Idarubicin", "Daunorubicin", "Mitoxantrone", "Topotecan",
                        "Irinotecan", "Etoposide", "Teniposide", "Amsacrine", "Camptothecin", "Oxaliplatin", "Cisplatin",
                        "Carboplatin", "5-Fluorouracil", "Floxuridine", "Gemcitabine", "Cytarabine", "Hydroxyurea",
                        "Methotrexate", "Pemetrexed", "Fludarabine", "Clofarabine", "Cladribine"],
              "targets": r"\bTOP1\b|\bTOP2[AB]?\b|\bTYMS\b|\bDHFR\b|\bRRM[12]\b"}
PROTEASOME_I = {"names": ["Bortezomib", "Ixazomib", "Carfilzomib"], "moa": "Proteasome inhibitor"}
DNMT_I = {"names": ["Decitabine", "5-Azacytidine"], "moa": "DNA methyltransferase"}
CONTROLS = [  # (expectation, readout kind, readout, direction (+1 up, -1 down, 0 either), drug finder)
    ("DNA-damaging drugs (TOP1/TOP2 poisons, antimetabolites, platinum) raise P53_ACTIVITY", "score",
     "P53_ACTIVITY", 1, DNA_DAMAGE),
    ("... and raise it more in TP53-wild-type than in TP53-altered lines (p53_wt_vs_altered.csv)", "p53wt", "",
     1, DNA_DAMAGE),
    ("Dimethyl fumarate (NRF2 activator) raises NRF2 target genes", "score", "NRF2", 1,
     {"names": ["Dimethyl fumarate"]}),
    ("Dimethyl fumarate raises HMOX1", "gene", "HMOX1", 1, {"names": ["Dimethyl fumarate"]}),
    ("Proteasome inhibitors raise proteasome subunits (bounce-back)", "score", "PROTEASOME", 1, PROTEASOME_I),
    ("Proteasome inhibitors raise heat-shock genes", "score", "HEAT_SHOCK", 1, PROTEASOME_I),
    ("Proteasome inhibitors raise HMOX1", "gene", "HMOX1", 1, PROTEASOME_I),
    ("HSP90 inhibitors (Pimitespib) raise heat-shock genes", "score", "HEAT_SHOCK", 1,
     {"names": ["Pimitespib"], "targets": r"\bHSP90"}),
    ("Ciclopirox (iron chelator) raises TFRC (iron starvation)", "gene", "TFRC", 1, {"names": ["Ciclopirox"]}),
    ("DNMT inhibitors raise GSDME in the GSDME-low (silenced) lines", "reexpr", "GSDME", 1, DNMT_I),
    ("DNMT inhibitors raise interferon genes (viral mimicry)", "score", "IFN", 1, DNMT_I),
    ("COX inhibitors change PTGS2 (report only: the direction is not certain)", "gene", "PTGS2", 0,
     {"moa": "Cyclooxygenase"}),
    ("Antimitotics (taxanes, vinca alkaloids) raise G2/M genes", "score", "G2M_PHASE", 1,
     {"names": ["Paclitaxel", "Docetaxel", "Vinblastine", "Vincristine", "Vinorelbine", "Eribulin"],
      "moa": "Microtubule inhibitor"}),
    ("Dinaciclib (CDK9) causes a transcription drop (UMIs per cell fall)", "ctx", "umi_per_cell_log2_vs_plate", -1,
     {"names": ["Dinaciclib"]}),
]


# ============================================================================= small helpers
def quiet():
    """Silence numpy's all-NaN warnings (lines missing from some wells) and pandas' fragmentation hints."""
    warnings.filterwarnings("ignore", category=RuntimeWarning)
    warnings.filterwarnings("ignore", category=pd.errors.PerformanceWarning)
    np.seterr(all="ignore")


def atlas(required=True):
    """tahoe_atlas.py (agent runner, hints), imported only by check / agents / bundle."""
    try:
        import tahoe_atlas as A
        return A
    except ImportError:
        if required:
            sys.exit("This step needs tahoe_atlas.py in the same folder as tahoe_gene_panel.py")
        return None


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
    logf = rel_path(os.path.join(out, "gene_panel.log"))
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
        sys.exit("No expression parquet files found under " + os.path.abspath(args.data))
    gm = T.read_tables(idx["gene"], ["token_id", "gene_symbol", "ensembl_id"])
    if gm is None:
        sys.exit("Gene metadata (token_id -> gene_symbol) not found")
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
    """TP53 status per line from the cell-line metadata (any TP53 driver row = altered), protein changes, CDKN2A
    deletion; --tp53-wt / --tp53-altered override (names or Cellosaurus ids)."""
    out = pd.DataFrame(index=index)
    out["in_cell_line_metadata"] = False
    out["tp53_status"] = "unknown (line not in the cell-line metadata)"
    out["tp53_changes"] = ""
    out["cdkn2a_deleted"] = False
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
        dele = (sym == "CDKN2A") & (vt.str.contains("del", case=False) | ch.str.upper().eq("DEL"))
        inm = out.index.isin(set(cid))
        out.loc[inm, "in_cell_line_metadata"] = True
        out.loc[inm, "tp53_status"] = "wild type (no TP53 driver call)"
        out.loc[out.index.isin(set(tpch.index)), "tp53_status"] = "altered"
        out["tp53_changes"] = tpch.reindex(out.index).fillna("").astype(str)
        out["cdkn2a_deleted"] = out.index.isin(set(cid[dele.to_numpy()]))
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
    return out


def step_baseline(S):
    base, S.null_source = T.baseline_by_line(S.wl, S.sm, S.cl, S.targets, S.args.mtap_null)
    for c in ["cell_name", "Organ", "drivers", "Cell_ID_DepMap"]:
        base[c] = base[c].fillna("").astype(str) if c in base else ""
    S.name = pd.Series([n or i for i, n in zip(base.index, base["cell_name"])], index=base.index)
    geno = genotypes(S.idx, base.index, S.name, S.args.tp53_wt, S.args.tp53_altered)
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
    thr = np.maximum(EXPR_FRAC * med, MIN_EXPR_CPM)
    E = C.ge(thr, axis=1)
    S.C, S.Cd, S.med, S.thr, S.E = C, Cd, med, thr, E
    d = S.wl.merge(S.sm[["sample", "is_dmso"]], on="sample")
    S.dmso_counts = d[d["is_dmso"]].groupby("cell_line_id")[genes].sum().reindex(base.index).fillna(0.0)
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
            "vs_median_line": (C[g] / med[g]).values if med[g] > 0 else np.nan, "expressed": E[g].values}))
    S.save(pd.concat(long, ignore_index=True), "expression_by_line.csv")


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


def step_effects(S):
    """T.expression_effects for the modules, anchors, panel and context genes (non-expressing lines left out)."""
    order = [m for m in MODULES if m in S.cols] + [g for g in S.main if g in S.targets] + \
        [g for g in S.ctx_genes if g in S.targets]
    t0 = time.time()
    todo = [g for g in order if g in MODULES or g in ("MTAP", "PSMD10") or has_effects(S, g)]
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
        if g == "MTAP":
            excl = S.null_lines                               # as T.cmd_analyze
        elif g in MODULES or g == "PSMD10":
            excl = []                                          # as T.cmd_analyze
        else:
            excl = list(S.E.index[~S.E[g]])
        extra = None
        if g == "PSMD10" and "PROTEASOME" in S.WS:
            extra = S.WS["PROTEASOME"][["W2", "z"]].rename(columns={"W2": "PROTEASOME_log2FC", "z": "PROTEASOME_z"})
        res, W, d, cal = T.expression_effects(S.wl, S.sm, g, excl, S.ctx, S.drugs, extra)
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
    wells = S.sm.set_index("sample")[["plate", "drug", "conc", "slot", "well", "is_dmso"]]
    S.score_members = {}
    for name, members in SCORES.items():
        mem = [g for g in members if g in S.RES and S.status.get(g) == "testable"]
        if not mem:
            mem = [g for g in members if g in S.RES]
        S.score_members[name] = mem
        if not mem:
            S.skipped[name] = "no member gene is expressed"
            continue
        M = pd.concat({g: S.WS[g]["W2"] for g in mem}, axis=1)
        Pe = pd.concat({g: S.WS[g]["slot_effect"] for g in mem}, axis=1)
        W = wells.reindex(M.index).copy()
        W["W2"] = M.mean(axis=1)
        W["position_effect_removed"] = Pe.mean(axis=1)
        c, s = T.robust_center_scale(W.loc[~W["is_dmso"], "W2"])
        W["z"] = (W["W2"] - c) / s
        W = W.join(S.ctx, how="left")
        vals = ["W2", "position_effect_removed"] + [c for c in S.ctx.columns if c in W]
        res = T.per_dose_table(W, vals).rename(columns={"W2": "log2FC"})
        lf = pd.concat([S.RES[g][["drug", "conc", "log2FC_corrected"]].assign(gene=g) for g in mem])
        Lm = lf.pivot_table(index=["drug", "conc"], columns="gene", values="log2FC_corrected")
        Lm = Lm.reindex(pd.MultiIndex.from_arrays([res["drug"], res["conc"]]))
        arr, gcols = Lm.to_numpy(dtype=float), list(Lm.columns)
        order = np.argsort(-np.abs(np.nan_to_num(arr)), axis=1)[:, :3]
        res["top_members"] = ["; ".join(f"{gcols[j]} {2 ** arr[i, j]:.2f}x" for j in order[i]
                                        if np.isfinite(arr[i, j])) for i in range(len(res))]
        res["n_members"] = len(mem)
        S.SW[name] = W
        S.SC[name] = finish_score(res, name, S.drugs)
    for m in MODULES:                                      # T's summed modules, from their own drug-effect tables
        if m in S.RES:
            r = S.RES[m].rename(columns={"log2FC_corrected": "log2FC", "z_corrected": "z"})
            keep = ["drug", "conc", "log2FC", "z", "position_effect_removed", "wells", "plates"] + \
                [c for c in S.ctx.columns if c in r]
            r = r[[c for c in keep if c in r]].copy()
            r["top_members"] = "(summed module)"
            r["n_members"] = len(S.modules.get(m, []))
            S.SW[m] = S.WS[m]
            S.SC[m] = finish_score(r, m, S.drugs)
    long = pd.concat([t for t in S.SC.values()], ignore_index=True) if S.SC else pd.DataFrame()
    S.save(long, "pathway_scores_by_dose.csv")
    log(f"  scores: {', '.join(f'{k} ({len(v)})' for k, v in S.score_members.items())}")


def finish_score(res, name, drugs):
    res = res.copy()
    res["fold_change"] = 2.0 ** res["log2FC"]
    res["p_up"] = T.norm_sf(res["z"].values)
    res["p_down"] = T.norm_sf(-res["z"].values)
    res["fdr_up"] = T.bh(res["p_up"].values)
    res["fdr_down"] = T.bh(res["p_down"].values)
    res["flags"] = [T.flag_row(r, name) for r in res.to_dict("records")]
    res = dose_columns(res, "z", "p_up", "p_down")
    res = res.join(drugs[[c for c in ("moa_fine", "targets") if c in drugs]], on="drug")
    res.insert(0, "score", name)
    lead = ["score", "drug", "conc", "fold_change", "log2FC", "z", "fdr_up", "fdr_down", "z_by_dose", "dose_pattern_up",
            "dose_pattern_down", "fdr_drug_up", "fdr_drug_down", "n_members", "top_members", "flags"]
    return res[[c for c in lead if c in res] + [c for c in res.columns if c not in lead]].sort_values(
        "z", ascending=False)


def step_context(S):
    """Per drug-dose context (module scores, cell loss, transcription, cell cycle) joined onto every gene table."""
    wells = S.sm.set_index("sample")[["plate", "drug", "conc", "slot", "well", "is_dmso"]]
    Wc = wells.join(S.ctx, how="left")
    for v in CTX_VARS:                                     # robust z per variable, combined per drug-dose below
        c, s = T.robust_center_scale(Wc.loc[~Wc["is_dmso"], v])
        Wc[f"{v}_z"] = (Wc[v] - c) / s
    Wc["z"] = 0.0
    ct = T.per_dose_table(Wc, [c for c in S.ctx.columns] + [f"{v}_z" for v in CTX_VARS])
    g = Wc.loc[~Wc["is_dmso"]].assign(dose=T.dose_key(Wc.loc[~Wc["is_dmso"]])).groupby(["drug", "dose"])
    for v in CTX_VARS:                                     # Stouffer over the drug-dose's plates
        ct[f"{v}_z"] = (g[f"{v}_z"].sum() / np.sqrt(g[f"{v}_z"].count())).values
    ct = ct.drop(columns=["z"])
    for m in CONTEXT_SCORES:
        if m in S.SC:
            t = S.SC[m][["drug", "conc", "log2FC", "z"]].drop_duplicates(["drug", "conc"])
            ct = ct.merge(t.rename(columns={"log2FC": f"{m}_log2FC", "z": f"{m}_z"}), on=["drug", "conc"], how="left")
    ct["flags"] = [T.flag_row(r, "") for r in ct.to_dict("records")]
    ct["context"] = context_text(ct)
    ct = ct.join(S.drugs[[c for c in ("moa_fine", "targets") if c in S.drugs]], on="drug")
    lead = ["drug", "conc", "flags", "context"] + CTX_VARS
    ct = ct[[c for c in lead if c in ct] + [c for c in ct.columns if c not in lead]]
    S.ctab = ct
    S.save(ct.sort_values(["drug", "conc"]), "drug_context_by_dose.csv")
    cols = [c for c in ct.columns if c.endswith("_log2FC") or (c.endswith("_z") and c[:-2] in CONTEXT_SCORES)]
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
    """FERRO_MARKERS per drug-dose with the ISR / NRF2 / UPR context: ferroptosis-like or a stress program?"""
    t = S.SC["FERRO_MARKERS"].copy()
    ct = S.ctab[["drug", "conc"] + [c for c in S.ctab.columns if c.split("_")[0] in ("ISR", "NRF2", "UPR", "HEAT")
                                    and (c.endswith("_z") or c.endswith("_log2FC"))]]
    t = t.merge(ct.drop_duplicates(["drug", "conc"]), on=["drug", "conc"], how="left")
    read = []
    for r in t.to_dict("records"):
        if not (r["z"] >= 3):
            read.append("")
            continue
        with_ = [m for m in ("ISR", "NRF2", "UPR", "HEAT_SHOCK") if (r.get(f"{m}_z", np.nan) or 0) >= CONTEXT_Z]
        read.append("markers with " + " + ".join(with_) if with_ else "markers without ISR / NRF2 / UPR / heat shock")
    t["reading"] = read
    lead = ["drug", "conc", "fold_change", "z", "fdr_up", "reading", "top_members", "ISR_z", "NRF2_z", "UPR_z",
            "HEAT_SHOCK_z", "ISR_log2FC", "NRF2_log2FC", "flags", "z_by_dose", "dose_pattern_up"]
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
    wells = S.sm.set_index("sample")[["plate", "drug", "conc", "slot", "well", "is_dmso"]]
    W = wells.reindex(P.index).copy()
    W["wt_mean"] = P[wt].mean(axis=1)
    W["altered_median"] = P[alt].median(axis=1)
    W["delta"] = W["wt_mean"] - W["altered_median"]
    W["n_wt_lines"] = P[wt].notna().sum(axis=1)
    W["n_altered_lines"] = P[alt].notna().sum(axis=1)
    eff, _ = T.loo_slot(W["delta"].values, W["slot"].values, W["drug"].values, ~W["is_dmso"].values)
    W["position_effect_removed"] = eff
    W["delta_corrected"] = W["delta"] - eff
    c, s = T.robust_center_scale(W.loc[~W["is_dmso"], "delta_corrected"])
    W["z"] = (W["delta_corrected"] - c) / s
    W = W.join(S.ctx[["cells_log2_vs_plate", "genes_per_cell_log2_vs_plate", "umi_per_cell_log2_vs_plate",
                      "G2M_PHASE_shift_log2"]] if "G2M_PHASE_shift_log2" in S.ctx else S.ctx[CTX_VARS], how="left")
    vals = ["delta_corrected", "delta", "wt_mean", "altered_median", "position_effect_removed", "n_wt_lines",
            "n_altered_lines"] + [c for c in S.ctx.columns if c in W and c != "cells"]
    res = T.per_dose_table(W, vals)
    res["p_wt_more"] = T.norm_sf(res["z"].values)
    res["fdr"] = T.bh(res["p_wt_more"].values)
    res["flags"] = [T.flag_row(r, "") for r in res.to_dict("records")]
    res = res.rename(columns={"delta_corrected": "extra_log2_p53_induction_in_WT", "z": "z_wt_more",
                              "wt_mean": "wt_mean_log2", "altered_median": "altered_median_log2"})
    res = T.add_dose_columns(res, "z_wt_more", "p_wt_more", "up")
    sc = S.SC["P53_ACTIVITY"][["drug", "conc", "fold_change", "z"]].rename(
        columns={"fold_change": "all_lines_P53_ACTIVITY_fold_change", "z": "all_lines_P53_ACTIVITY_z"})
    res = res.merge(sc.drop_duplicates(["drug", "conc"]), on=["drug", "conc"], how="left")
    res = res.join(S.drugs[[c for c in ("moa_fine", "targets") if c in S.drugs]], on="drug")
    lead = ["drug", "conc", "extra_log2_p53_induction_in_WT", "z_wt_more", "fdr", "fdr_drug", "z_by_dose",
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
    ok = sc[~sc["flags"].astype(str).str.contains("toxic") & np.isfinite(sc["z"])].sort_values("z", ascending=False)
    ref = ok.head(N_P53_DOSES)
    S.p53_ref = ref
    S.save(ref[["drug", "conc", "fold_change", "z", "fdr_up", "flags", "wells", "plates"]], "p53_reference_doses.csv")
    keys = set(zip(ref["drug"], ref["conc"]))
    sel = [s for s, d, c, dm in zip(S.sm["sample"], S.sm["drug"], S.sm["conc"], S.sm["is_dmso"])
           if (d, c) in keys and not dm]
    Ps = P.reindex(sel)
    resp = Ps.mean(axis=0)
    nw = Ps.notna().sum(axis=0)
    mem = [g for g in S.score_members["P53_ACTIVITY"] if f"{g}_cpm_dmso" in base]
    basal = basal_activity(S, mem)
    t = pd.DataFrame({"cell_name": S.name, "organ": base["Organ"], "tp53_annotation": base["tp53_status"],
                      "tp53_changes": base["tp53_changes"], "cdkn2a_deleted": base["cdkn2a_deleted"],
                      "mtap_null": base["MTAP_null"], "basal_p53_activity_log2": basal,
                      "p53_responsiveness_log2": resp.reindex(base.index), "n_reference_wells": nw.reindex(base.index)})
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
    t["functional_call"] = np.where(t["p53_responsiveness_log2"].isna(), "not measured",
                                    np.where(t["p53_responsiveness_log2"] >= cut, "responsive", "unresponsive"))
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


def basal_activity(S, members):
    """Per line, untreated (DMSO): mean over the expressed members of log2(cpm / median line)."""
    if not members:
        return pd.Series(np.nan, index=S.base.index)
    Cd = S.Cd[members]
    med = Cd[S.enough.to_numpy()].median()
    L = np.log2((Cd + 0.5) / (med + 0.5))
    return L.where(S.E[members]).mean(axis=1)


# ============================================================================= growth: group screens
def group_growth_screen(n, base, sm, drugs, ctx, group, rest, per_line_max=PER_LINE_MAX):
    """T.mtap_null_screen for any group of lines vs reference lines in the same wells, with the same statistics
    (mean of the group minus median of the reference, counting variance, tissue-matched delta, leave-drug-out
    position correction, well noise + counting noise z, Stouffer per drug-dose, FDR, drug-level FDR). With
    group = MTAP-null lines and rest = the other lines it reproduces T.mtap_null_screen."""
    wells = sm.set_index("sample")[["plate", "drug", "conc", "slot", "well", "is_dmso"]]
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
    drug_w = ~W["is_dmso"]
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
    or a clean 2x separation; >= 3 lost lines and >= 3 expressing lines in the growth analysis."""
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
    clean = len(lost) >= 3 and rest.size >= 3 and ratio[lost].max() < 0.5 * rest.min()
    if len(lost) >= 3 and rest.size >= 3 and (np.isfinite(gap) or clean):
        return {"gene": g, "lines": lost, "n_lines": len(lost), "threshold_vs_median": thr,
                "gap_log2": gap, "clean_2x_separation": bool(clean),
                "lost_lines_vs_median": "; ".join(f"{S.name[c]} {ratio[c]:.2f}" for c in sorted(lost, key=ratio.get)),
                "lowest_expressing_vs_median": float(rest.min())}
    return None


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
                      columns=["gene", "n_lines", "lines", "cell_line_ids", "threshold_vs_median", "gap_log2",
                               "clean_2x_separation", "lost_lines_vs_median", "lowest_expressing_vs_median"])
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
        lost = lost_of[g]
        res = T.expression_effects(S.wl, S.sm, g, [c for c in S.base.index if c not in set(lost)], S.ctx, S.drugs)[0]
        return reexpression_table(S, g, lost, res)
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


def reexpression_table(S, g, lost, res):
    """Drug effect on a gene measured only in the lines that have lost it (silenced: e.g. GSDME and DNMT
    inhibitors). Ambient RNA from the other lines rises with them, so the expressing lines' change is shown too."""
    t = res.copy()
    main = S.RES.get(g)
    if main is not None:
        m = main[["drug", "conc", "fold_change", "z_corrected"]].rename(
            columns={"fold_change": "expressing_lines_fold_change", "z_corrected": "expressing_lines_z"})
        t = t.merge(m.drop_duplicates(["drug", "conc"]), on=["drug", "conc"], how="left")
    else:
        t["expressing_lines_fold_change"], t["expressing_lines_z"] = np.nan, np.nan
    if hasattr(S, "ctab"):
        t = t.merge(S.ctab[["drug", "conc", "context"]].drop_duplicates(["drug", "conc"]), on=["drug", "conc"],
                    how="left")
    lf = np.log2(t["fold_change"])
    le = np.log2(t["expressing_lines_fold_change"]).fillna(0)
    t["reading"] = np.where((t["z_corrected"] >= 3) & (lf >= 0.5) & (lf > 2 * le.clip(lower=0) + 0.25),
                            "re-expression in the lost lines (expressing lines change less)",
                            np.where(t["z_corrected"] >= 3, "rises in all lines (ambient RNA follows)", ""))
    t.insert(0, "lines", ", ".join(S.name[c] for c in lost))
    t.insert(0, "gene", g)
    lead = ["gene", "lines", "drug", "conc", "fold_change", "z_corrected", "fdr_up", "reading",
            "expressing_lines_fold_change", "expressing_lines_z", "n_lines", "n_lines_up", "frac_lines_positive",
            "flags", "context", "wells", "plates", "moa_fine", "targets"]
    return t[[c for c in lead if c in t]].sort_values("z_corrected", ascending=False)


# ============================================================================= growth: level vs growth
def level_screen(n, base, sm, drugs, level, gene="PSMD10", organ=None, g2m=None):
    """T.gankyrin_level_screen for any gene's untreated level (a Series per line), plus a within-lineage version
    (organ effects removed from both rank vectors). g2m: proliferation level per line for the partial correlation
    (default: base['G2M_PHASE_cpm_dmso'], as T). With level = base['PSMD10_cpm_dmso'] it reproduces
    T.gankyrin_level_screen (rho, rho_partial_G2M, z_corrected)."""
    wells = sm.set_index("sample")[["plate", "drug", "conc", "slot", "well", "is_dmso"]]
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
        c, s = T.robust_center_scale(W.loc[~W["is_dmso"], f"fisher_corrected_{zc}"])
        W[zc] = (W[f"fisher_corrected_{zc}"] - c) / s
    vals = ["rho"] + (["rho_partial_G2M"] if gcol else []) + ["rho_within_lineage"]
    res = T.per_dose_table(W, vals)
    res["z_within_lineage"] = T.per_dose_table(W, ["rho_within_lineage"], zcol="z_within")["z"].values
    res["p"] = 2 * T.norm_sf(np.abs(res["z"].values))
    res["fdr"] = T.bh(res["p"].values)
    res = res.join(drugs, on="drug").rename(columns={"z": "z_corrected"})
    res["reading"] = np.where(res["z_corrected"] < 0, f"high-{gene} lines depleted more", f"high-{gene} lines spared")
    res = T.add_dose_columns(res, "z_corrected", "p", "down")
    res = res.rename(columns={"dose_pattern": "dose_pattern_depleted_more"})
    lead = ["drug", "conc", "rho", "rho_partial_G2M", "rho_within_lineage", "z_corrected", "z_within_lineage", "fdr",
            "fdr_drug", "z_by_dose", "dose_pattern_depleted_more", "reading"]
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

    def one(g):
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
        top = top[["gene", "drug", "conc", "rho", "rho_partial_G2M", "rho_within_lineage", "z", "z_within_lineage",
                   "fdr", "fdr_drug", "z_by_dose", "reading", "n_lines", "moa_fine"]
                  if "rho_partial_G2M" in top else [c for c in top.columns]].sort_values("fdr")
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
    for g in S.main + S.ctx_genes + MODULES:
        if g in S.WS:
            feats[g] = S.WS[g]["W2"]
    for name in SCORES:
        if name in S.SW:
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


def compare(rows, label, mine, prior, cols, key=("drug", "conc")):
    """Max |difference| and Spearman between this run's and the earlier run's numbers (same drug-doses)."""
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
                     "expected": "0 (same data, same code)",
                     "reading": "identical" if d <= 1e-6 else ("near-identical" if r > 0.99 else "differs")})


def step_crosslinks(S):
    rows = []
    P = prior_dir(S.args)
    S.prior = P
    pr = os.path.join(P, "results") if P else None
    dst = os.path.join(S.out, "angles", "crosslinks", "prior")
    shutil.rmtree(dst, ignore_errors=True)                 # never leave an older run's copy behind
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
                [("z_corrected", "z_corrected"), ("log2FC_corrected", "log2FC_corrected")])
        compare(rows, "PSMD10 drug effects", S.RES.get("PSMD10"),
                _read(os.path.join(pr, "Gankyrin_PSMD10_drug_effects_by_dose.csv")),
                [("z_corrected", "z_corrected"), ("log2FC_corrected", "log2FC_corrected")])
        compare(rows, "MTAP-null screen", getattr(S, "mres", None),
                _read(os.path.join(pr, "MTAP_null_selective_drugs.csv")),
                [("z_selective", "z_selective"), ("extra_log2_depletion_of_MTAP_null",
                                                  "extra_log2_depletion_of_MTAP_null")])
        lv = S.lvl[S.lvl["gene"] == "PSMD10"] if len(getattr(S, "lvl", [])) else None
        compare(rows, "Gankyrin level screen", lv, _read(os.path.join(pr, "Gankyrin_level_vs_drug_response.csv")),
                [("rho", "rho"), ("rho_partial_G2M", "rho_partial_G2M"), ("z", "z_corrected")])
    else:
        rows.append({"category": "reproducibility", "comparison": "earlier MTAP / Gankyrin run",
                     "reading": "not found (--prior); MTAP and PSMD10 were recomputed here with the same code"})
    biology_links(S, rows)
    shared_drugs(S, rows, pr)
    cols = ["category", "comparison", "n", "statistic", "value", "spearman", "auc", "p", "expected", "reading"]
    S.xl = pd.DataFrame(rows).reindex(columns=cols)
    S.save(S.xl, "crosslinks.csv")


def biology_links(S, rows):
    base, f = S.base, getattr(S, "p53f", None)
    wt = base["tp53_group"] == "WT"
    basal_p53 = f["basal_p53_activity_log2"].reindex(base.index) if f is not None else \
        basal_activity(S, [g for g in P53_ACTIVITY if g in S.Cd])
    resp = f["p53_responsiveness_log2"].reindex(base.index) if f is not None else pd.Series(np.nan, index=base.index)
    nrf2 = basal_activity(S, [g for g in CONTEXT["NRF2_CORE"] if g in S.Cd])
    gk = np.log2(base["PSMD10_cpm_dmso"].astype(float) + 0.5) if "PSMD10_cpm_dmso" in base else None

    def corr_row(label, a, b, expected, mask=None):
        mask = np.ones(len(base), bool) if mask is None else np.asarray(mask, bool)
        r, n, p = spearman_p(np.asarray(a)[mask], np.asarray(b)[mask])
        rows.append({"category": "biology", "comparison": label, "n": n, "statistic": "Spearman rho", "value": r,
                     "p": p, "expected": expected,
                     "reading": "" if not np.isfinite(r) else ("as expected" if (r < 0) == expected.startswith("neg")
                                                               and p < 0.05 else ("same direction, not significant"
                                                                                  if (r < 0) == expected.startswith(
                                                                                      "neg") else "opposite"))})
    if gk is not None:
        corr_row("PSMD10 (Gankyrin) baseline vs basal p53 activity, TP53-WT lines", gk, basal_p53,
                 "negative (Gankyrin promotes MDM2-mediated p53 degradation)", wt)
        corr_row("PSMD10 baseline vs p53 responsiveness to the reference activators, TP53-WT lines", gk, resp,
                 "negative", wt)
        corr_row("PSMD10 baseline vs basal NRF2 core activity, all lines", gk, nrf2,
                 "positive (reported Gankyrin-KEAP1 link)")
    nul = base["MTAP_null"].astype(bool)

    def group_row(label, v, mask, expected):
        v = pd.Series(np.asarray(v, dtype=float), index=base.index)
        a, b = v[mask & nul], v[mask & ~nul]
        u, p = auc(a, b)
        rows.append({"category": "biology", "comparison": label, "n": int(a.notna().sum() + b.notna().sum()),
                     "statistic": "median null - intact",
                     "value": float(a.median() - b.median()) if a.notna().any() and b.notna().any() else np.nan,
                     "auc": u, "p": p, "expected": expected,
                     "reading": f"{int(a.notna().sum())} null vs {int(b.notna().sum())} intact lines"})
    group_row("MTAP-null (9p21 / CDKN2A-ARF loss) vs basal p53 activity, TP53-WT lines", basal_p53, wt,
              "lower in null (ARF loss frees MDM2)")
    group_row("MTAP-null vs p53 responsiveness, TP53-WT lines", resp, wt, "lower in null")
    for g in ["SLC7A11", "GPX4", "ACSL4", "AIFM2", "CHAC1"]:
        if f"{g}_cpm_dmso" in base and g in S.C:
            lev, _ = gene_level(S, g)
            group_row(f"MTAP-null vs {g} baseline (log2 CPM)", np.log2(lev.astype(float) + 0.5),
                      np.ones(len(base), bool), "unknown (MTA / transsulfuration -> cysteine)")


def shared_drugs(S, rows, pr):
    """Drugs on both the earlier MTAP / Gankyrin top lists and the panel's top lists."""
    prior = {}

    def top_drugs(t, col, asc, k):
        if t is None or col not in t:
            return []
        return list(dict.fromkeys(t.sort_values(col, ascending=asc)["drug"].astype(str)))[:k]
    src = "earlier run" if pr else "this run (no earlier run found)"
    for g, f in (("MTAP", "MTAP_drug_summary.csv"), ("PSMD10", "Gankyrin_PSMD10_drug_summary.csv")):
        t = _read(os.path.join(pr, f)) if pr else S.DS.get(g)
        prior[f"{g} up"] = top_drugs(t, "best_up_z", False, TOP)
        prior[f"{g} down"] = top_drugs(t, "best_down_z", True, TOP)
    t = _read(os.path.join(pr, "MTAP_null_selective_drugs.csv")) if pr else getattr(S, "mres", None)
    prior["MTAP-null selective"] = top_drugs(t, "z_selective", True, TOP)
    t = _read(os.path.join(pr, "Gankyrin_level_vs_drug_response.csv")) if pr else None
    prior["Gankyrin level: depleted more"] = top_drugs(t, "z_corrected", True, 10)
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
            panel[f"{g} up"] = list(d.loc[d["up_call"] == "up", "drug"].astype(str))[:5]
            panel[f"{g} down"] = list(d.loc[d["down_call"] == "down", "drug"].astype(str))[:5]
    hits = []
    for d in sorted({x for v in prior.values() for x in v}):
        pl = [k for k, v in panel.items() if d in v]
        if pl:
            hits.append((len(pl), d, [k for k, v in prior.items() if d in v], pl))
    for npl, d, a, b in sorted(hits, key=lambda t: (-t[0], t[1]))[:25]:
        rows.append({"category": "shared top drugs", "comparison": d, "n": npl,
                     "statistic": f"top lists ({src})", "value": len(a), "expected": "",
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
    for exp, kind, name, sign, spec in CONTROLS:
        drugs = find_drugs(present, S.drugs, spec)
        t = readout(S, kind, name)
        low = kind == "reexpr" and len(getattr(S, "reex", [])) and (S.reex["gene"] == name).any()
        what = {"score": f"{name} score", "gene": f"{name} mRNA",
                "reexpr": f"{name} mRNA in the {name}-low lines" if low else
                f"{name} mRNA (expressing lines: no {name}-low group found)",
                "p53wt": "p53 targets, WT minus altered lines", "ctx": "UMIs per cell vs plate"}[kind]
        if not drugs:
            rows.append({"expectation": exp, "readout": what, "drug": "not in data", "verdict": "not in data"})
            continue
        if t is None:
            rows.append({"expectation": exp, "readout": what, "drug": ", ".join(drugs),
                         "verdict": f"not testable ({S.status.get(name, S.skipped.get(name, 'readout missing'))})"})
            continue
        sz = t["z"] * (sign if sign else 1)
        rank = (sz if sign else t["z"].abs()).rank(ascending=False, method="min")
        for d in drugs:
            g = t[(t["drug"] == d) & np.isfinite(t["z"].astype(float))]
            if not len(g):
                rows.append({"expectation": exp, "readout": what, "drug": d, "verdict": "not measured"})
                continue
            k = (g["z"] * sign if sign else g["z"].abs()).idxmax()
            r = t.loc[k]
            dz = r["z"] * sign if sign else abs(r["z"])
            fdr = r["fdr_up"] if (sign > 0 or (sign == 0 and r["z"] > 0)) else r["fdr_down"]
            lf = math.log2(r["fold_change"]) if r["fold_change"] > 0 else np.nan
            big = abs(lf) >= T.LFC_MIN if kind not in ("ctx", "p53wt") else (lf <= -0.5 if kind == "ctx" else True)
            verdict = "clear" if dz >= 3 and fdr < T.FDR_CUT and big else ("weak" if dz >= 2 else "absent")
            rows.append({"expectation": exp, "readout": what, "drug": d, "best_dose": r["conc"],
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
        f"over lines), >= 60% of lines moving that way. Expressed: >= {EXPR_FRAC:.0%} of the median line and >= "
        f"{MIN_EXPR_CPM:g} CPM (all wells).")
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
    title("1. CHECKS: artifacts, calibration, agreement with the earlier run")
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
    if xl is not None and len(xl):
        r = xl[xl["category"] == "reproducibility"]
        say("Agreement with the earlier MTAP / Gankyrin run" + (f" ({S.prior}):" if S.prior else ":"))
        say(table(r, ["comparison", "n", "statistic", "value", "spearman", "reading"], TOP, 6))


def sec_expression(S, say, title):
    title("2. EXPRESSION (all wells pooled; lines expressing = >= 25% of the median line and >= 1 CPM)")
    pg = getattr(S, "pg", None)
    if pg is None:
        say("  not available")
        return
    for pw in ["ferroptosis", "pyroptosis", "p53"]:
        t = pg[pg["pathway"] == pw]
        say(f"{pw}:")
        say(table(t, ["gene", "also_known_as", "median_line_cpm", "n_lines_expressing", "n_lines",
                      "median_pct_cells_dmso", "median_counts_per_profile", "status"], TOP, 2))
    t = pg[~pg["pathway"].isin(["ferroptosis", "pyroptosis", "p53"])]
    say("NAPEPLD, TRIM72, anchors" + (" and added genes" if (pg["gene_set"] == "added").any() else "") + ":")
    say(table(t, ["gene", "also_known_as", "median_line_cpm", "n_lines_expressing", "n_lines", "median_pct_cells_dmso",
                  "median_counts_per_profile", "status"], TOP, 2))
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
    sign = {e: sg for e, _k, _n, sg, _s in CONTROLS}
    z = pd.to_numeric(t["z"], errors="coerce") if "z" in t else pd.Series(np.nan, index=t.index)
    sg = t["expectation"].map(sign).fillna(1)
    t["_z"] = np.where(sg == 0, z.abs(), z * sg)
    t["_z"] = t["_z"].fillna(-99)
    order = {e: i for i, (e, *_r) in enumerate(CONTROLS)}
    best = t.sort_values("_z", ascending=False).drop_duplicates("expectation")
    best = best.assign(_o=best["expectation"].map(order)).sort_values("_o")
    n_clear = t.groupby("expectation")["verdict"].agg(lambda s: f"{(s == 'clear').sum()}/{len(s)} clear")
    best["drugs_clear"] = best["expectation"].map(n_clear)
    best["exp"] = best["expectation"].str.slice(0, 62)
    say(table(best, ["exp", "drug", "best_dose", "fold_change", "z", "fdr", "rank_among_drug_doses", "verdict",
                     "drugs_clear"], TOP, 3))


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
    title("4. FERROPTOSIS (mRNA after 24 h: 'ferroptosis-like signature' at most; no lipid peroxidation, no death mode)")
    fer = [g for g, p, _ in PANEL if p == "ferroptosis"]
    say("Best increase and decrease per gene (drug summary; fdr = drug-level):")
    say(table(gene_best(S, fer), ["gene", "best_up", "up_flags_context", "best_down"], TOP))
    f = getattr(S, "ferro", None)
    if f is not None:
        say("FERRO_MARKERS (PTGS2, CHAC1, SLC7A11) top drug-doses with their stress context ('without ISR' = the more "
            "specific pattern):")
        say(table(f, ["drug", "conc", "fold_change", "z", "fdr_up", "ISR_z", "NRF2_z", "UPR_z", "reading", "flags"], 10))
    iron = gene_best(S, ["TFRC", "FTH1", "FTL", "NCOA4"])
    say("Iron genes (iron starvation: TFRC up with FTH1/FTL down; iron load: the reverse):")
    say(table(iron, ["gene", "best_up", "best_down"], 4))
    lv = getattr(S, "lvl", None)
    if lv is not None and len(lv):
        t = lv[lv["gene"].isin(FERRO_LEVEL_GENES)].sort_values("fdr").drop_duplicates("gene")
        say("Does a line's baseline level predict which lines a drug depletes? (best drug-dose per gene; rho < 0 = "
            "high-level lines depleted more; within lineage = organ removed):")
        say(table(t, ["gene", "drug", "conc", "rho", "rho_within_lineage", "z", "fdr", "z_by_dose", "reading"], 7))


def sec_pyroptosis(S, say, title):
    title("5. PYROPTOSIS (mRNA only: no caspase cleavage, no pore formation, no IL-1b release)")
    pg = getattr(S, "pg", None)
    if pg is not None:
        t = pg[pg["pathway"] == "pyroptosis"]
        say("Who expresses the machinery (lines expressing / lines; lines lacking it):")
        for r in t.itertuples():
            hl = high_lines(S, r.gene)
            say(f"  {label_of(r.gene):16s} {r.n_lines_expressing}/{r.n_lines} lines; {r.status}"
                + (f"; lost in: {r.loss_group_lines}" if isinstance(r.loss_group_lines, str) and r.loss_group_lines
                   else "") + (f"; >= 8x the median line in: {hl}" if hl else ""))
    say("GSDME inducers in the expressing lines:")
    d = S.DS.get("GSDME") if hasattr(S, "DS") else None
    say(table(d, ["drug", "doses", "z_by_dose", "best_up_fold_change", "fdr_up_drug", "up_pattern", "up_flags"], 5)
        if d is not None else "  not available")
    rx = getattr(S, "reex", None)
    if rx is not None and len(rx):
        for g, t in rx.groupby("gene"):
            say(f"{g} measured only in the lines that lost it ({t['lines'].iloc[0]}): top drug-doses")
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
        say(f"More p53-target induction in TP53-wild-type ({len(wt)}) than TP53-altered ({len(alt)}) lines in the same "
            "wells (p53-dependent):")
        say(table(t, ["drug", "conc", "extra_log2_p53_induction_in_WT", "z_wt_more", "fdr", "z_by_dose",
                      "wt_mean_log2", "altered_median_log2", "flags"], 10))
    f = getattr(S, "p53f", None)
    if f is not None:
        a, p = S.p53_auc
        say(f"Functional p53 status: responsiveness = mean p53-target shift over the {N_P53_DOSES} strongest non-toxic "
            f"P53_ACTIVITY drug-doses (genotype-blind; p53_reference_doses.csv). AUC WT vs altered = {fnum(a)} "
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
    say("Specific p53 reporters vs stress-generic targets (best increase):")
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
                t = lv[lv["gene"] == g].sort_values("fdr").head(3)
                say("  level vs growth: " + "; ".join(f"{d} {c:g} rho {r:.2f} (fdr {q:.2g})" for d, c, r, q in
                                                      zip(t["drug"], t["conc"], t["rho"], t["fdr"])))
    if S.status.get("TRIM72", "") != "testable":
        say("TRIM72 is a muscle/heart gene; in cancer lines it is expected to be absent. Nothing more can be said from "
            "these data.")


def sec_crosslinks(S, say, title):
    title("8. CROSS-LINKS to the earlier MTAP / Gankyrin analysis")
    xl = getattr(S, "xl", None)
    if xl is None:
        say("  not available")
        return
    say(table(xl[xl["category"] == "biology"], ["comparison", "n", "statistic", "value", "auc", "p", "expected"],
              TOP))
    sh = xl[xl["category"] == "shared top drugs"]
    say(f"Drugs on both the MTAP / Gankyrin top lists and the panel top lists: {len(sh)}")
    for r in sh.head(10).itertuples():
        say(f"  {r.comparison}: {r.reading}"[:200])
    if getattr(S, "pc1", None):
        say(f"Co-regulation: the first principal component of the panel's drug responses explains "
            f"{100 * S.pc1['share']:.0f}% (mostly global stress / shutdown): {S.pc1['top'][:150]}")
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
                      "expression_threshold_cpm": S.thr[g], "median_counts_per_profile": S.counts.get(g, np.nan),
                      "testable": S.status.get(g) == "testable",
                      "lowest_lines": "; ".join(f"{S.name[i]} {v:.2f}x" for i, v in ok.head(3).items()),
                      "highest_lines": "; ".join(f"{S.name[i]} {v:.2f}x" for i, v in ok.iloc[::-1].head(3).items()),
                      "lines_not_expressing": ", ".join(ne) if len(ne) <= 25 else f"{len(ne)} lines",
                      "lines_8x_above_median": high_lines(S, g),
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
- Lines that do not express a gene read 10-25% of a typical line from ambient RNA of the other lines in the well;
  they are left out of that gene's drug effects (expressed rule below).
"""

PANEL_RULEBOOK = """## Rules for interpreting (learned on this dataset; follow them)
1. Artifacts first. Before calling an effect real, check: toxicity (flag 'toxic': < half the plate's usual cells);
   transcription shutdown ('transcription drop': genes or UMIs per cell fall; short stable mRNAs then rise and long
   or unstable ones fall, in relative terms); cell-cycle composition (S or G2/M arrest raises every cycle-linked
   mRNA); well position (H1 shifted MTAP, D10 PSMD10 on every plate; corrected, see ../../results/
   well_position_effects.csv). The DMSO wells sit in corners and some plates' DMSO is off: never use DMSO-based
   numbers (log2FC_vs_DMSO_uncorrected is there only for comparison).
2. Dose consistency. Real effects usually grow with dose or appear at the top dose. A hit at a low dose only is
   most likely noise. Say what the dose pattern is (z_by_dose: doses in ascending order).
3. Breadth. Check how many lines move (n_lines_up / n_lines, frac_lines_positive). One or two lines = a
   line-specific observation.
4. Specific vs broad. Many drugs move big programs together (ISR/ATF4, NRF2, UPR, heat shock, interferon, NF-kB,
   proteasome, cell cycle, p53). The 'context' column names the programs that moved strongly in the same drug-dose:
   say whether a gene's change belongs to such a program or stands alone.
5. Statistics. With ~1,100 drug-doses per gene, z > 3 happens by chance: rely on FDR, effect size and dose
   consistency. Report fold changes (not log2) with FDR and the number of lines.
6. Known biology as a check: positive_controls.csv lists the expected effects and whether the data show them; use
   them to calibrate how much to trust a new finding, and say when an expected effect is absent.
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
Tahoe-100M single-cell drug perturbation atlas (mRNA of ~50 cancer cell lines 24 h after 379 drugs at 3 doses). You run
unattended: nobody will answer questions or grant permissions, so never ask; decide, state your assumptions in the
report, and keep going. Work in your current folder (write your scripts and report.md there); the results/ folder
and the other files of the gene-panel folder may be read. {shell}Compute every number you report with Python: write a
.py script in this folder and run it with `{py} script.py` (always allowed). If any command is refused, do the same
thing in Python instead; never stop because of a refusal.
Do not install packages, use the network, delete files or touch anything outside the gene-panel folder. Your job is
finished only when report.md exists and follows brief.md; a precise, well-checked report matters more than a long
one."""

PANEL_SYNTH = """Read every report in this folder (all *.md files except 00_overview.md) and write 00_overview.md: a
single overview of what Tahoe-100M shows about the gene panel (ferroptosis, pyroptosis, p53, NAPEPLD and TRIM72) and
how it connects to the earlier MTAP / Gankyrin findings. Start with the top findings per pathway (each with its
numbers and which report it comes from), then where the reports agree or disagree, the main caveats (mRNA after 24 h
only: no protein, lipid peroxidation, cleavage or death mode; genes that are not expressed or not testable), and a
ranked list of the 10 best leads to test experimentally (drug, dose, cell line, readout). At most ~1,500 words, plain
language, Markdown. Do not invent numbers: use only what the reports state. Run unattended; never ask questions."""

TASKS = {
    "ferroptosis": """
Which drugs induce the ferroptosis markers (PTGS2, CHAC1, SLC7A11), and does that look ferroptosis-like or is it
explained by the ISR/ATF4, NRF2 or UPR programs (ferro_markers_with_context.csv: 'markers without ISR / NRF2 / UPR'
is the more specific pattern)? Which drugs move the defences (GPX4, AIFM2/FSP1, NFE2L2 and its targets), lipid
remodelling (ACSL4, LPCAT3) and iron handling (TFRC, FTH1/FTL, NCOA4: iron starvation = TFRC up with ferritin down;
iron load = the reverse)? Do baseline GPX4, ACSL4, AIFM2, SLC7A11, NFE2L2, LPCAT3, TFRC levels predict which lines a
drug depletes, within lineage (level_vs_growth.csv)? Known biology to check: dimethyl fumarate -> NRF2; auranofin ->
TXNRD -> NRF2/ISR; ciclopirox -> TFRC; statins and the mevalonate / selenoprotein / CoQ10-FSP1 axis; artesunate /
dihydroartemisinin; proteasome inhibitors -> HMOX1. mRNA after 24 h cannot show lipid peroxidation or the death
mode: say 'ferroptosis-like signature' and label hypotheses.""",
    "pyroptosis": """
Which lines express which parts of the pyroptosis machinery (many carcinoma lines silence GSDME and the inflammasome
genes; expression_by_line.csv, loss_groups.csv)? Which drugs change them: DNMT inhibitors -> GSDME re-expression in
the silenced lines (reexpression_in_silenced_lines.csv: compare with the expressing lines, ambient RNA follows any
change in the others); interferon / NF-kB inducers -> CASP1/CASP4/GSDMD/IL1B/IL18 (INFLAMMASOME, IFN, NFKB scores)?
Does GSDME level predict which lines DNA-damaging chemotherapy depletes (level_vs_growth.csv, gene GSDME)? Are lines
lacking a component selectively depleted by any drug (loss_screens.csv)? mRNA cannot show caspase cleavage, pore
formation or cytokine release.""",
    "p53": """
Which drugs activate p53 transcription, and is it p53-dependent (p53_wt_vs_altered.csv: TP53-wild-type vs
TP53-altered lines in the same wells)? How does the functional p53 status (p53_functional_status.csv: responsiveness
to the strongest non-toxic activators, genotype-blind) agree with the annotation (AUC, discordant lines: annotated
wild type but unresponsive, altered but responsive - check protein changes, CDKN2A deletion, MTAP status)? Specific
targets (FDXR, ZMAT3, MDM2, CDKN1A) vs stress-generic ones (PMAIP1, GADD45A, SESN2, also ATF4-driven: compare with
the ISR context). TP53 mRNA itself (truncating mutants and deletions lower it). Which drugs deplete TP53-WT lines
selectively (p53_wt_selective_growth.csv)? The library has no MDM2 inhibitor: DNA damage and antimetabolites are the
expected activators.""",
    "napepld_trim72": """
NAPEPLD and TRIM72 (MG53): expression across lines (if TRIM72 is not expressed, say so plainly and keep that part
short), drug effects if testable (dose pattern, breadth, context), co-regulation partners across drug wells
(coregulation_top_partners.csv; genome-wide partners need the atlas), level vs growth, and plausible links
(rimonabant / CNR1 and the NAPE-PLD pathway; TRIM72 and insulin / IRS1 / PI3K-AKT drugs). Keep the report short if
the data say little.""",
    "crosslinks": """
How does the panel connect to the earlier MTAP and Gankyrin (PSMD10) findings (the earlier run's files are in
prior/)? Gankyrin vs p53 activity (Gankyrin promotes MDM2-mediated p53 degradation: expect lower basal p53 activity
and responsiveness in high-PSMD10 TP53-WT lines), Gankyrin vs NRF2 (reported KEAP1 link), MTAP/CDKN2A(ARF)-null vs
p53 (ARF loss frees MDM2), MTAP loss vs ferroptosis genes (methionine salvage and transsulfuration feed cysteine),
drugs on both top lists, and reproducibility vs the earlier run (crosslinks.csv). With ~50 lines, correlations
below ~0.3 are weak: say so.""",
}


def deeper_queries(S):
    py = agent_python()
    o = os.path.abspath(S.out)
    R = os.path.join(o, "results")
    atl = os.path.join(os.path.abspath(S.args.data), "atlas")
    me = os.path.join(HERE, "tahoe_atlas.py")
    s = f"""## Deeper queries
- Python: run scripts as `{py} script.py` (numpy, pandas and pyarrow are available; scipy may be missing: check
  first). Keep the scripts you write in this folder.
- All results: `{R}` (read `{os.path.join(R, 'README_columns.txt')}` first). Every panel gene and anchor has
  `<GENE>_drug_effects_by_dose.csv` (every drug-dose, all columns) and `<GENE>_drug_summary.csv` (one row per drug).
- Counts per well x cell line: `{os.path.join(o, 'well_line.parquet')}` (sample, cell_line_id, n_cells,
  total_counts, raw counts of every extracted gene, det_<GENE> = cells with >= 1 count); wells:
  `{os.path.join(o, 'sample_map.csv')}` (sample, plate, drug, conc, well, n_cells, is_dmso).
- Per cell (large: read only the columns and rows you need, e.g. pyarrow.parquet.read_table(f, columns=[...],
  filters=[('drug', 'in', [...])])): `{os.path.join(o, 'cells')}{os.sep}*.parquet`; columns barcode, sample, plate,
  drug, cell_line_id, n_genes, total_counts, the extracted genes and the PROTEASOME / S_PHASE / G2M_PHASE sums.
"""
    if os.path.isdir(os.path.join(atl, "effects")) and os.path.exists(me):
        s += (f"- Genome-wide (the atlas has been computed): `{py} {quote(me)} --out {quote(atl)} lookup gene <SYMBOL>` "
              "(also `corr <SYMBOL>`, `drug <NAME>`, `line <NAME>`).\n")
    else:
        s += "- Genome-wide partners or other genes: not available here (tahoe_atlas.py has not been run).\n"
    return s


def high_lines(S, g, fold=8.0):
    """Lines far above the median line (genes most lines express only at ambient level, e.g. IL1B)."""
    if g not in S.C or not S.med.get(g, 0) > 0:
        return ""
    r = (S.C[g] / S.med[g]).sort_values(ascending=False)
    r = r[r >= fold]
    return ", ".join(f"{S.name[c]} {v:.0f}x" for c, v in r.head(6).items()) + (" ..." if len(r) > 6 else "")


def gene_status_md(S, genes):
    rows = ["| gene | role | lines expressing | median line CPM | far above the median line | status |",
            "|---|---|---|---|---|---|"]
    role = dict(zip(S.gt["gene"], S.gt["role"]))
    for g in genes:
        n = f"{int(S.E[g].sum())}/{len(S.E)}" if g in S.E else "-"
        r = str(role.get(g, S.set_of.get(g, "")))
        r = r[len(AKA[g]) + 3:] if g in AKA and r.startswith(f"({AKA[g]}) ") else r
        rows.append(f"| {label_of(g)} | {r} | {n} | {fnum(S.med.get(g, np.nan), '{:.1f}')}"
                    f" | {high_lines(S, g)} | {S.status.get(g, '')} |")
    return "\n".join(rows) + "\n"


def write_brief(S, folder, name, files, genes):
    info = S.info
    head = (f"This run: {int(S.wl['n_cells'].sum()):,} cells, {S.sm['sample'].nunique()} wells, "
            f"{S.sm['plate'].nunique()} plates, {S.wl['cell_line_id'].nunique()} cell lines"
            + (f" (TRIAL: first {info['limit_files']} files only)" if info.get("limit_files") else "") + ".")
    ndd = len(S.SC["P53_ACTIVITY"]) if "P53_ACTIVITY" in S.SC else len(next(iter(S.RES.values())))
    methods = PANEL_METHODS.replace("< 30 cells", f"< {T.MIN_CELLS} cells").replace("~1,100", f"{ndd:,}")
    rules = PANEL_RULEBOOK.replace("~1,100", f"{ndd:,}")
    with open(os.path.join(folder, "brief.md"), "w", encoding="utf-8") as fh:
        added = [g for g in genes if S.set_of.get(g) == "added"]
        task = TASKS[name].strip() + (f"\nGenes added with --genes ({', '.join(added)}) are in this folder too: report "
                                      "them the same way, briefly." if added else "")
        fh.write(f"# Angle: {TITLES[name]}\n\n## Your task\n{task}\n\n{head}\n\n{WHAT_DATA_SHOW}\n"
                 f"## Genes of this angle\n{gene_status_md(S, genes)}\n## Data in this folder\n")
        for f, desc in files:
            fh.write(f"- `{f}`: {desc}\n")
        fh.write("\n" + methods + "\n" + rules + "\n" + deeper_queries(S) + "\n" + PANEL_REPORT_RULES)


PANEL_METHODS = """## How the numbers were made
- Cells of one line in one well are summed into a profile (profiles with < 30 cells are left out).
- Drug effect on a gene (log2FC_corrected; fold_change = 2^log2FC): the profile's log2 CPM minus the median of all
  drug wells on the same plate for the same line (NOT the DMSO wells), minus the leave-drug-out well-position effect
  (median of the other drugs that sat in the same position on other plates), median across lines. z_corrected:
  scored against the spread of all drug wells (median/MAD), Stouffer over the drug-dose's plates; fdr_up /
  fdr_down: Benjamini-Hochberg over the ~1,100 drug-doses of that gene. call: up/down when FDR < 0.10, >= 1.2x and
  >= 60% of lines moving that way. Drug summaries: best dose, Bonferroni over doses, BH over drugs (fdr_*_drug).
- Expressed: a line expresses a gene when its level over all wells is >= 25% of the median line and >= 1 CPM.
  Lines that do not are left out of that gene's drug effects; genes expressed in < 3 lines get none; genes whose
  profiles hold a median of < 2 counts are flagged 'low counts'. MTAP follows the earlier run (MTAP-null lines left
  out); PSMD10 keeps every line and carries the rest-of-proteasome change (PROTEASOME_log2FC / PROTEASOME_z).
- Pathway scores (pathway_scores_by_dose.csv): per well the mean of the expressed member genes' corrected shifts,
  robust z over drug wells, Stouffer per drug-dose. P53_ACTIVITY = CDKN1A MDM2 FDXR ZMAT3 SESN1 BBC3 BAX + 15 more
  p53 targets (PMAIP1, GADD45A, SESN2 left out: also ATF4-driven); FERRO_MARKERS = PTGS2 CHAC1 SLC7A11;
  INFLAMMASOME = NLRP3 AIM2 PYCARD CASP1 CASP4 CASP5 IL1B IL18 GSDMD; NRF2, ISR (ATF4), UPR, HEAT_SHOCK, IFN, NFKB
  context sets; PROTEASOME, S_PHASE, G2M_PHASE = summed modules. 'context' on each gene's drug-dose names the
  programs with |z| >= 3 (scores that contain the gene itself excluded).
- p53 WT vs altered (p53_wt_vs_altered.csv): per well and line the mean corrected shift of the P53_ACTIVITY genes;
  per well the mean of the TP53-wild-type lines minus the median of the TP53-altered lines (any TP53 driver row in
  the cell-line metadata = altered), position-corrected, robust z, Stouffer, one-sided (more induction in WT).
- Growth (selective depletion; loss_screens.csv, p53_wt_selective_growth.csv, MTAP_null_selective_drugs.csv): each
  line's share of the cells in a well vs its usual share on that plate (log2 relative abundance); mean of the group
  minus median of the other lines in the same well, position-corrected; the z includes counting noise. Negative =
  the group was depleted more.
- Level vs growth (level_vs_growth.csv): Spearman across lines of a gene's untreated level (DMSO CPM) and relative
  abundance after the drug (rho < 0: high-level lines depleted more); partial on the G2M level (proliferation);
  within lineage (organ effects removed from both ranks); Fisher z, position-corrected, robust z, Stouffer; FDR
  within gene.
- Flags: toxic (< half the plate's typical cells), transcription drop (genes per cell -0.3 log2 or UMIs per cell
  -0.5 log2), cell-cycle shift (G2M module > 1.4x), position effect removed (> 1.15x), plate DMSO offset (affects
  only the uncorrected column), low counts.
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
        "level of each gene in each line (DMSO and all wells, CPM), % cells expressing, vs the median line, expressed")
    if hasattr(S, "lvl") and len(S.lvl):
        put(S.lvl[S.lvl["gene"].isin(gset)], "level_vs_growth.csv",
            "does a line's untreated level predict how a drug-dose affects its growth? rho (Spearman across lines), "
            "rho_partial_G2M, rho_within_lineage, z, FDR within gene, z at every dose")
    if hasattr(S, "coreg") and len(S.coreg):
        put(S.coreg[S.coreg["gene"].isin(gset)], "coregulation_top_partners.csv",
            "top co-regulated genes / programs across drug wells (rank < 0: most negative), raw and after removing "
            "the first principal component (global stress / shutdown)")
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
             "per drug-dose: cells / genes / UMIs per cell vs plate (with z), every program's fold change and z, flags, "
             "context")
    if name == "ferroptosis":
        put(getattr(S, "ferro", None), "ferro_markers_with_context.csv",
            "FERRO_MARKERS per drug-dose with ISR / NRF2 / UPR / heat-shock z and a reading (markers with or without "
            "a stress program)")
    if name == "pyroptosis":
        put(getattr(S, "reex", None), "reexpression_in_silenced_lines.csv",
            "drug effects measured only in the lines that lost a gene (e.g. GSDME-silenced lines), with the expressing "
            "lines' change for comparison (ambient RNA follows the other lines)")
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
                        ("p53_reference_doses.csv", "the drug-doses that define responsiveness (strongest non-toxic "
                                                    "all-line P53_ACTIVITY)"),
                        ("p53_wt_selective_growth.csv", "drugs that deplete TP53-WT lines more than TP53-altered lines")):
            put_file(os.path.join(S.R, f), f, desc)
    if name == "crosslinks":
        for f, desc in (("crosslinks.csv", "reproducibility vs the earlier run, biology links (Gankyrin vs p53 / NRF2, "
                                           "MTAP-null vs p53 and ferroptosis genes), shared top drugs"),
                        ("MTAP_null_selective_drugs.csv", "the MTAP-null screen recomputed here (same statistics as the "
                                                          "earlier run)"),
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
gene_panel.log           The run log (every step, warnings, tracebacks of failed steps).
angles/<pathway>/        Agent folders: brief.md (task, methods, rules), the tables of that pathway, report.md once
                         the agents have run. reports/: NN_<pathway>.md and 00_overview.md.

Files in results/
=================
summary.txt                       Key checks and results. Start here.
panel_genes.csv                   One row per panel gene and anchor: pathway, role, also_known_as, symbol_used,
                                  in_gene_metadata, extracted, median_line_cpm (all wells), median_line_cpm_dmso,
                                  median_pct_cells_dmso, n_lines, n_lines_expressing, expression_threshold_cpm,
                                  median_counts_per_profile (raw counts per well x line profile, expressing lines),
                                  testable, status (testable / low counts / expressed in too few lines / not expressed /
                                  not in the gene metadata), lowest_lines / highest_lines (x the median line),
                                  lines_not_expressing, lines_8x_above_median (where a gene most lines lack is high,
                                  e.g. IL1B), loss_group_lines, drug_effects (file or why none), n_calls_up/down
                                  (low-count genes get no calls: their changes are dominated by the pseudocount).
expression_by_line.csv            Long: gene, gene_set, cell line, organ, tp53_status, cpm_dmso, cpm_all_wells,
                                  pct_cells_dmso, vs_median_line, expressed (>= 25% of the median line and >= 1 CPM).
baseline_by_cell_line.csv         Per line: tahoe_mtap_gankyrin.py's baseline table for every extracted gene
                                  (<GENE>_cpm_dmso, <GENE>_pct_cells_dmso, <GENE>_cpm_all_wells), MTAP_null, organ,
                                  drivers, and the TP53 annotation (tp53_status, tp53_changes, tp53_group, cdkn2a_deleted).
<GENE>_drug_effects_by_dose.csv   One row per drug and dose (every panel gene with drug effects and the anchors MTAP,
                                  PSMD10, CDKN2A, CDKN2B): the columns of tahoe_mtap_gankyrin.py (below), plus the
                                  context of that drug-dose: <SCORE>_log2FC / <SCORE>_z for ISR, NRF2, UPR, HEAT_SHOCK,
                                  IFN, NFKB, P53_ACTIVITY, FERRO_MARKERS, INFLAMMASOME, PROTEASOME, S_PHASE, G2M_PHASE,
                                  and 'context' = the programs with |z| >= 3 (scores containing the gene left out).
<GENE>_drug_summary.csv           One row per drug (tahoe_mtap_gankyrin.drug_summary) + up_context / down_context.
context_genes_top.csv             Each context gene (P53_EXT, NRF2_CORE, ISR_ATF4, UPR_ER, HSF1_HEAT, IFN, NFKB): lines
                                  expressing, top 3 increases and decreases, number of calls. They feed the scores.
pathway_scores_by_dose.csv        Long: score, drug, conc, fold_change, log2FC (mean of the expressed members'
                                  corrected shifts), z (robust z over drug wells, Stouffer over plates), fdr_up/fdr_down,
                                  z_by_dose (ascending doses), dose_pattern_up/down, fdr_drug_up/down (best dose,
                                  Bonferroni over doses, BH over drugs), n_members, top_members (largest member fold
                                  changes), flags, cells/genes/UMIs per cell vs plate, cell-cycle shifts. PROTEASOME,
                                  S_PHASE and G2M_PHASE rows are the summed modules (tahoe_mtap_gankyrin.py).
drug_context_by_dose.csv          Per drug-dose: cells_log2_vs_plate, genes_per_cell_log2_vs_plate,
                                  umi_per_cell_log2_vs_plate (each with a robust z, Stouffer), S/G2M shifts, every score's
                                  log2FC and z, flags, context.
ferro_markers_with_context.csv    FERRO_MARKERS per drug-dose with ISR_z, NRF2_z, UPR_z, HEAT_SHOCK_z and reading:
                                  'markers with ISR (+ ...)' or 'markers without ISR / NRF2 / UPR / heat shock' (z >= 3).
p53_wt_vs_altered.csv             Per drug-dose: extra_log2_p53_induction_in_WT = per well mean p53-target shift of the
                                  TP53-wild-type lines minus the median of the TP53-altered lines, position-corrected;
                                  z_wt_more (robust z, Stouffer), fdr, fdr_drug, z_by_dose, dose_pattern, wt_mean_log2,
                                  altered_median_log2, the all-line P53_ACTIVITY fold change and z, flags.
p53_functional_status.csv         Per line: tp53_annotation, tp53_changes, cdkn2a_deleted, mtap_null,
                                  basal_p53_activity_log2 (DMSO: mean log2 of the expressed p53 targets vs the median
                                  line), p53_responsiveness_log2 (mean p53-target shift over the reference drug-doses),
                                  n_reference_wells, responsiveness_rank, functional_call (vs the cut halfway between the
                                  WT and altered medians), discordant, PSMD10_cpm_dmso.
p53_reference_doses.csv           The 10 strongest non-toxic all-line P53_ACTIVITY drug-doses used for responsiveness.
p53_wt_selective_growth.csv       Growth screen TP53-WT vs TP53-altered lines (columns as MTAP_null_selective_drugs.csv;
                                  extra_log2_depletion_of_TP53_WT < 0 = WT lines depleted more).
MTAP_null_selective_drugs.csv     The earlier MTAP-null screen recomputed (same columns as in the earlier run).
loss_groups.csv                   Genes (panel, CDKN2A/B) that most lines express but >= 3 lines have lost: lines,
                                  threshold_vs_median, gap_log2 (T.null_threshold), clean_2x_separation, levels.
loss_screens.csv                  Per loss group and drug-dose: extra_log2_depletion (mean of the lost lines minus median
                                  of the others in the same well, position-corrected; < 0 = lost lines depleted more),
                                  z_selective (well noise + counting noise), fdr_selective, fdr_drug, z_by_dose,
                                  dose_pattern, delta_tissue_matched (vs other lines of the same organ), group_mean_log2,
                                  rest_median_log2, all_cells_log2_vs_plate.
reexpression_in_silenced_lines.csv  Per loss-group gene and drug-dose: the drug effect measured only in the lines that
                                  lost the gene (fold_change, z_corrected, fdr_up, lines up), the expressing lines'
                                  fold change and z, reading ('re-expression in the lost lines' when they rise much more
                                  than the expressing lines; else ambient RNA following the others), flags, context.
level_vs_growth.csv               Long: gene, drug, conc, rho (Spearman across lines of the untreated level vs relative
                                  abundance after the drug), rho_partial_G2M (proliferation removed), rho_within_lineage
                                  (organ removed from both ranks), z (Fisher z, position-corrected, robust z, Stouffer),
                                  z_within_lineage, fdr (within gene, two-sided), fdr_drug, z_by_dose,
                                  dose_pattern_depleted_more, reading, n_lines, level_source (DMSO CPM; all-wells CPM
                                  for lines with < 20 DMSO counts).
level_vs_growth_top.csv           The 5 strongest 'depleted more' and 2 'spared' drug-doses per gene, sorted by fdr.
cell_cycle_by_line.csv            Untreated (DMSO) cells, per line and gene: log2 level in G2M-high vs G2M-low quartile
                                  cells (and S), cell-level Spearman with the G2M and S scores (normalised by counts
                                  outside the cycle genes), expressed.
cell_cycle_summary.csv            Per gene: medians over the expressing lines, lines higher in G2M cells.
coregulation_matrix.csv           Pearson r across drug wells of the corrected per-well shifts (W2) of every gene,
                                  score and module; coregulation_matrix_minus_pc1.csv: after removing the first
                                  principal component (global stress / shutdown).
coregulation_top_partners.csv     Per panel gene and anchor: top 10 partners (rank 1-10) and most negative (rank -1..-3),
                                  raw r and after removing PC1 (scores containing the gene left out).
crosslinks.csv                    category (reproducibility / biology / shared top drugs), comparison, n, statistic,
                                  value, spearman (reproducibility), auc (MTAP-null vs intact: P(null > intact)), p,
                                  expected, reading.
                                  Reproducibility: well positions, MTAP-null calls, MTAP / PSMD10 drug z, MTAP-null
                                  screen and Gankyrin level screen vs the earlier run (max |difference|).
positive_controls.csv             expectation, readout, drug (found by name, mechanism or target; 'not in data'),
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
log2FC_corrected       Plate baseline = median of the plate's drug wells for the same line; minus the leave-drug-out
                       well-position effect; median over the expressing lines. fold_change = 2 ** log2FC_corrected.
z_corrected            Robust z against all drug wells (median/MAD); Stouffer over plates.
fdr_up, fdr_down       Benjamini-Hochberg over all drug-doses of the gene, one-sided.
n_lines_up/down        Lines with a per-line z > 2 and > 1.2x (down: < -2, < 1/1.2). n_lines = lines measured.
frac_lines_positive    Share of lines whose corrected change is above zero (frac_lines_negative: below).
call                   up/down when FDR < 0.10, >= 1.2x and >= 60% of lines move that way.
flags                  toxic: < half the plate's typical cells; transcription drop: genes or UMIs per cell fell;
                       cell-cycle shift: G2M module changed > 1.4x; whole proteasome up/down (PSMD10 only); position
                       effect removed / plate DMSO offset: how much the corrections changed the estimate; low counts.
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
    log("Well covariates ...")
    S.ctx = core("well covariates", lambda: T.well_context(S.wl, S.sm, S.cols))
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
    S.attempt("panel genes table", lambda: step_panel_genes(S))
    log("Writing summary and agent folders ...")
    S.attempt("summary", lambda: write_summary(S))
    with open(os.path.join(S.R, "README_columns.txt"), "w", encoding="utf-8") as fh:
        fh.write(README)
    step_angles(S)
    if S.failures:
        S.attempt("summary (failures)", lambda: write_summary(S))
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
        say(False, f"only {ne:,} expression files (the full dataset has ~3,388): is the download complete?", fatal=False)
    for k, fatal, why in (("gene", True, "needed"), ("sample", True, "needed (doses, well positions)"),
                          ("cell_line", False, "missing: no organ, no TP53 annotation (use --tp53-wt / --tp53-altered)"),
                          ("drug", False, "missing: no mechanisms / targets; positive controls by name only")):
        say(bool(idx[k]), f"{k} metadata: {len(idx[k])} file(s)" + ("" if idx[k] else f" - {why}"), fatal=fatal)
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
    say(mem is None or mem >= 4, f"memory: {mem or 0:.0f} GB free, {cpus} CPUs -> {w} extract workers; analyze needs "
                                 "~2-4 GB", fatal=mem is not None and mem < 2)
    A = atlas(required=False)
    todo = []
    if A is None:
        say(False, "tahoe_atlas.py not next to this script (needed only for the agents step)", fatal=False)
        todo.append("put tahoe_atlas.py next to tahoe_gene_panel.py")
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
          ("extract_info.json", None), ("extracted_columns.json", None), ("well_position_check.csv", None),
          ("sample_map.csv", None)]


def cmd_bundle(args):
    """One small zip to upload to Claude: the key tables (to check the numbers before the agents), then the reports
    and agent logs once the agents have run."""
    out = args.out
    path = os.path.join(out, "gene_panel_bundle.zip")
    if not os.path.isdir(out):
        sys.exit(f"{out} does not exist: run 'all' first")
    A = atlas(required=False)
    reps = sorted(glob.glob(os.path.join(out, "reports", "*.md")))
    items = list(BUNDLE) + [(os.path.relpath(f, out), None) for f in
                            sorted(glob.glob(os.path.join(out, "results", "*_drug_summary.csv")))]
    n_tables = 0
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as z:
        for rel, nrows in items:
            src = os.path.join(out, rel)
            if not os.path.exists(src):
                continue
            arc = os.path.join("computation", rel).replace(os.sep, "/")
            if nrows and src.endswith(".csv"):
                z.writestr(arc, pd.read_csv(src, nrows=nrows).to_csv(index=False))
            else:
                z.write(src, arc)
            n_tables += 1
        logf = os.path.join(out, "gene_panel.log")
        if os.path.isfile(logf):
            if A is not None:
                A.add_log(z, logf, "computation/gene_panel.log")
            else:
                z.write(logf, "computation/gene_panel.log")
        for f in reps + [os.path.join(out, "reports", "agents_summary.csv")]:
            if os.path.exists(f):
                z.write(f, "reports/" + os.path.basename(f))
        for f in sorted(glob.glob(os.path.join(out, "angles", "*", "agent.log"))):
            z.write(f, "agent_logs/" + os.path.basename(os.path.dirname(f)) + ".log")
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
    T.start_run_log(os.path.join(args.out, "gene_panel.log"), "tahoe_gene_panel.py " + " ".join(sys.argv[1:]))
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
