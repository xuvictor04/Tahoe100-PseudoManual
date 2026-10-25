#!/usr/bin/env python3
"""qPCR reference genes for the MG53 (TRIM72) perturbation experiment, screened in Tahoe-100M (mRNA, 24 h).

ddCt is only valid if the reference genes do not move under the treatments. This script screens every gene that a
qPCR assay can read comfortably in the candidate cell lines for the smallest change under the drugs of the MG53
experiment (DMSO, idarubicin, doxorubicin, epirubicin, homoharringtonine, auranofin, dinaciclib, selinexor), and
reports how the classic reference genes behave under the same drugs.

    python3 reference_gene_screen.py [--data DIR] [--out DIR] [--steps extract,screen]

--data   the Tahoe-100M folder with atlas/ (effects + pseudobulk) and gene_panel/ (default: $MG53_DATA, $TAHOE_DATA
         or ~/Tahoe-100M). Read only.
--out    where tables go (default: this folder). cache/ (~0.4 GB, compressed counts) and external/ go there too.

Steps
  extract  One read-only pass over <data>/atlas/pseudobulk/groupNNN.npy (mmap, row chunks; split (well, line) profiles
           summed): counts of the screened genes for every (well, cell line) on the plates that hold the drugs above
           (plates 4-12 and 14), with each profile's total counts and cells. ~15 min. -> cache/counts.npz
  screen   Per-line effects of every screened gene in every target drug-dose, in two frames:
           (1) method v3 ("corrected"): log2 CPM minus the plate's drug-well median for that line (MIN_CELLS 30, the
               atlas's expressed mask), minus the profile's composition shift (atlas composition_shift.parquet), minus
               the atlas's own well-position effect of the gene (W1 - W2); mean over the drug-dose's used wells. This is
               exactly tahoe_atlas.per_line_columns for atlas genes; the well-level median is checked against the atlas
               W1 (validation.csv).
           (2) DMSO-referenced raw CPM ratio ("raw", closest to qPCR ddCt with equal RNA input): log2 CPM of the drug
               well minus log2 CPM of the same line pooled over the plate's DMSO wells; no composition or position
               correction; mean over the used wells.
           Counting noise of each value is estimated from its counts (Poisson) and taken out of the RMS ("adj").
           Then filters (expression, p53 target, immediate-early / stress, readthrough, cell cycle, noise RNA, locus),
           a rank by instability, a pick of 3 references from different functions plus 2 backups, geNorm M values,
           and the classic references.

Outputs (all written by this script)
  reference_gene_screen.csv         one row per screened gene: levels, both frames' RMS / worst shift / worst
                                    condition, all-Tahoe responsiveness, TP53 WT-vs-altered test, flags, eligible,
                                    rank, role (reference / backup), why
  classic_references.csv            one row per classic reference gene (15): level, per-drug-dose median shift in both
                                    frames, which conditions move it, verdict, why
  reference_by_condition.csv        long: gene x condition (picked, backups, top 30 eligible, classics, positive
                                    controls): median / range over candidate lines, both frames, pooled atlas fold/q
  genorm.csv                        geNorm M (Vandesompele 2002) per gene within the pool of top eligible + classics,
                                    on the DMSO-referenced per-well ratios, mean over candidate lines; and the pair V
  candidate_lines.csv, conditions.csv, validation.csv, run_info.json
"""
import argparse
import json
import os
import re
import subprocess
import sys
import time

import numpy as np
import pandas as pd
from scipy import stats

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, REPO)
import tahoe_atlas as A               # noqa: E402  (read-only helpers: FX, log_cpm, NOISE_RNA_RE)
import tahoe_mtap_gankyrin as T       # noqa: E402  (S / G2M gene lists)
import tahoe_gene_panel as P          # noqa: E402  (stress context gene sets, P53_ACTIVITY)

sys.path.insert(0, os.path.join(REPO, "mg53_p53", "upstream_perturbations"))
try:
    from trim72_upstream_landscape import IEG as REPO_IEG     # noqa: E402  the repo's immediate-early gene list
except Exception:                                             # pragma: no cover
    REPO_IEG = ["FOS", "FOSB", "JUN", "JUNB", "EGR1", "EGR2", "EGR3", "IER2", "IER3", "IER5", "DUSP1", "KLF6",
                "ZFP36", "NR4A1"]

DOG_TABLE = os.path.join(REPO, "mg53_p53", "upstream_coregulation", "tables", "c_DoG_gene_exposure_classes.csv")
FISCHER_LOCAL = os.path.join(REPO, "mg53_p53", "literature", "downloads", "fischer2017")
FISCHER_URL = ("https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fonc.2016.502/"
               "MediaObjects/41388_2017_BFonc2016502_MOESM{}_ESM.xlsx")
HGNC_LOCAL = os.path.join(REPO, "mg53_p53", "upstream_coregulation", "external", "hgnc_complete_set.txt")
HGNC_URL = "https://storage.googleapis.com/public-download-files/hgnc/tsv/tsv/hgnc_complete_set.txt"

CLASSIC = ["GAPDH", "ACTB", "B2M", "HPRT1", "TBP", "PPIA", "RPLP0", "YWHAZ", "GUSB", "HMBS", "SDHA", "UBC", "TFRC",
           "PGK1", "POLR2A"]
# positive controls: genes that should move (p53 targets, stress genes, TRIM72) - extracted to show the screen sees
# movers; never eligible
CONTROLS = ["TRIM72", "MDM2", "CDKN1A", "TP53I3", "FDXR", "BBC3", "ATF3", "FOS", "PMAIP1", "HSPA1A", "DDIT3", "MYC"]
NAMED_LINES = ["A549", "NCI-H460", "HCT15", "LoVo", "RKO", "SW48", "MIA PaCa-2", "PANC-1"]
DRUGS = {"Idarubicin (hydrochloride)": "Idarubicin", "Doxorubicin (hydrochloride)": "Doxorubicin",
         "Epirubicin (hydrochloride)": "Epirubicin", "Homoharringtonine": "Homoharringtonine",
         "Auranofin": "Auranofin", "Dinaciclib": "Dinaciclib", "Selinexor": "Selinexor"}
# primary conditions (the score): idarubicin at every dose, the others at 0.5 and 5 uM; 0.05 uM is reported only
PRIMARY_DOSES = {"Idarubicin": (0.05, 0.5, 5.0)}
OTHER_DOSES = (0.5, 5.0)
P53_ARM = ("Idarubicin", "Doxorubicin", "Epirubicin", "Selinexor")    # D1 / U2: p53 activators (+ DMSO)
STRESS_ARM = ("Homoharringtonine", "Auranofin", "Dinaciclib")            # U3: the other TRIM72 raisers
PRESELECT_CPM = 30.0      # extract: genes at >= this level (all wells pooled, atlas line_cpm) in every candidate line
MIN_DMSO_CPM = 50.0       # eligible: DMSO level >= this in every candidate line (qPCR-friendly, Ct ~< 25 typical)
MAX_SHIFT = 0.30          # eligible: no p53-arm condition (or DMSO) may shift the median candidate line more than
                          # this (log2, 1.23x) in either frame; the stress arm moves almost every gene more (reported)
P53_DIFF = 0.25           # flag: TP53 WT - altered per-line difference >= this (log2) with BH q < 0.05
FISCHER_DIRECT = 3        # flag: Fischer 2017 S2 'sum direct target' >= this ...
FISCHER_EXPR = 5          # ... or |p53 Expression Score| >= this (net datasets up minus down), or in S1 / S3
TRIM72_LOCUS = ("16", 31214017, 31231537)     # GRCh38; genes within 1 Mb are left out (readthrough question U1)
CHUNK = 256
DATA = os.environ.get("MG53_DATA") or os.environ.get("TAHOE_DATA") or os.path.expanduser("~/Tahoe-100M")


def log(*a):
    print(time.strftime("%H:%M:%S"), *a, flush=True)


def bh(p):
    p = np.asarray(p, dtype=float)
    out = np.full(p.shape, np.nan)
    ok = np.isfinite(p)
    if ok.any():
        q = p[ok]
        o = np.argsort(q)
        r = q[o] * ok.sum() / np.arange(1, ok.sum() + 1)
        r = np.minimum.accumulate(r[::-1])[::-1]
        res = np.empty_like(q)
        res[o] = np.minimum(r, 1)
        out[ok] = res
    return out


def curl(url, dest, tries=4):
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    tmp = dest + ".part"
    for k in range(tries):
        r = subprocess.run(["curl", "-sSfL", "-m", "300", "-o", tmp, url], capture_output=True, text=True)
        if r.returncode == 0:
            os.replace(tmp, dest)
            return True
        log("  download failed:", (r.stderr or "").strip()[-200:])
        time.sleep(10 * (k + 1))
    return False


# ============================================================================= setup shared by both steps
class Setup:
    def __init__(self, data, out):
        self.data, self.out = data, out
        self.cache = os.path.join(out, "cache")
        self.ext = os.path.join(out, "external")
        self.fx = A.FX(os.path.join(data, "atlas"))
        A.MIN_CELLS = int(self.fx.info.get("min_cells", 30))
        fx = self.fx
        self.genes = fx.genes
        self.lines = fx.lines["cell_line_id"].astype(str).tolist()
        self.lname = dict(zip(self.lines, fx.lines["cell_name"].astype(str)))
        st = pd.read_csv(os.path.join(data, "gene_panel", "results", "p53_functional_status.csv"),
                         dtype={"cell_line_id": str})
        base = pd.read_csv(os.path.join(data, "gene_panel", "results", "baseline_by_cell_line.csv"),
                           dtype={"cell_line_id": str}, usecols=["cell_line_id", "cell_name", "tp53_status",
                                                                 "tp53_changes", "tp53_group"])
        st = st.merge(base[["cell_line_id", "tp53_group"]], on="cell_line_id", how="left")
        self.status = st.set_index("cell_line_id")
        name_to_id = {v: k for k, v in self.lname.items()}
        named = [name_to_id[n] for n in NAMED_LINES]
        resp = st.loc[st["functional_call"] == "responsive", "cell_line_id"].tolist()
        self.cand = list(dict.fromkeys(named + resp))          # named lines first, then responsive TP53-WT lines
        self.cand_i = np.array([self.lines.index(c) for c in self.cand])
        self.why_line = {c: ("named in the task" + ("; TP53-WT, p53-responsive" if c in resp else ""))
                         if c in named else "TP53-WT, p53-responsive (functional_call == responsive)"
                         for c in self.cand}
        self.wt = np.array([self.status["tp53_group"].get(c) == "WT" for c in self.lines])
        self.alt = np.array([self.status["tp53_group"].get(c) == "altered" for c in self.lines])
        # target drug-doses
        dd = fx.dd
        rows = []
        for d, short in DRUGS.items():
            for conc in (0.05, 0.5, 5.0):
                r = dd.index[(dd["drug"] == d) & np.isclose(dd["conc"].astype(float), conc)]
                if not len(r):
                    raise SystemExit(f"drug-dose missing in the atlas: {d} {conc}")
                r = int(r[0])
                prim = conc in PRIMARY_DOSES.get(short, OTHER_DOSES)
                rows.append({"condition": f"{short} {conc:g} uM", "drug": d, "drug_short": short, "conc_uM": conc,
                             "dd_row": r, "primary": prim, "plates": dd.loc[r, "plates"],
                             "wells": dd.loc[r, "wells"], "n_wells": int(dd.loc[r, "n_wells"]),
                             "flags": dd.loc[r, "flags"], "n_sig_genes": int(dd.loc[r, "n_sig_genes"]),
                             "cells_log2_vs_plate": float(dd.loc[r, "cells_log2_vs_plate"]),
                             "composition_shift_log2": float(dd.loc[r, "composition_shift_log2"])})
        self.cond = pd.DataFrame(rows)
        plates = set()
        for p in self.cond["plates"]:
            plates |= set(str(p).split(","))
        self.plates = sorted(plates, key=lambda s: int(s.replace("plate", "")))
        w = fx.wells
        self.wsel = np.flatnonzero(w["plate"].isin(self.plates).to_numpy())     # atlas well rows kept
        self.wells = w.iloc[self.wsel].reset_index(drop=True)
        self.dmso_w = self.wells["is_dmso"].astype(bool).to_numpy()

    def gene_columns(self):
        """Atlas gene columns screened: >= PRESELECT_CPM (all wells pooled) in every candidate line, no noise RNA;
        plus the classic references and the positive controls."""
        g = self.genes
        lc = np.asarray(self.fx.line_cpm)
        isg = (g["kind"] == "gene").to_numpy()
        sym = g["symbol"].astype(str)
        noise = sym.map(lambda s: bool(A.NOISE_RNA_RE.match(s))).to_numpy()
        ok = isg & ~noise & (lc[self.cand_i] >= PRESELECT_CPM).all(axis=0)
        extra = g["symbol"].isin(CLASSIC + CONTROLS).to_numpy() & isg
        cols = np.flatnonzero(ok | extra)
        missing = set(CLASSIC + CONTROLS) - set(sym.iloc[cols])
        if missing:
            log("not atlas genes (left out):", sorted(missing))
        return cols


# ============================================================================= extract
def step_extract(S):
    os.makedirs(S.cache, exist_ok=True)
    path = os.path.join(S.cache, "counts.npz")
    cols = S.gene_columns()
    toks = S.genes["token"].to_numpy(dtype=np.int64)[cols]
    if os.path.exists(path):
        z = np.load(path)
        if np.array_equal(z["cols"], cols) and list(z["samples"]) == S.wells["sample"].astype(str).tolist():
            log("extract: cache present and current (delete cache/ to redo)")
            return
    prof = A.load_profiles(os.path.join(S.data, "atlas", "pseudobulk"))
    samples = S.wells["sample"].astype(str).tolist()
    wi = {s: i for i, s in enumerate(samples)}
    li = {s: i for i, s in enumerate(S.lines)}
    prof = prof[prof["sample"].isin(wi) & prof["cell_line_id"].isin(li)].copy()
    N, L, C = len(samples), len(S.lines), len(cols)
    log(f"extract: {len(prof)} profiles, {N} wells x {L} lines x {C} genes")
    counts = np.zeros((N * L, C), dtype=np.float32)
    tot = np.zeros(N * L)
    nc = np.zeros(N * L)
    prof["k"] = prof["sample"].map(wi).to_numpy() * L + prof["cell_line_id"].map(li).to_numpy()
    t0 = time.time()
    done = 0
    for f, g in prof.groupby("file"):
        g = g.sort_values("row")
        arr = np.load(f, mmap_mode="r")
        rows, ks = g["row"].to_numpy(), g["k"].to_numpy()
        for s0 in range(0, len(rows), CHUNK):
            r_, k_ = rows[s0:s0 + CHUNK], ks[s0:s0 + CHUNK]
            sub = np.array(arr[r_])[:, toks]
            if len(np.unique(k_)) == len(k_):
                counts[k_] += sub
            else:
                np.add.at(counts, k_, sub)
            del sub
        np.add.at(tot, ks, g["total_counts"].to_numpy())
        np.add.at(nc, ks, g["n_cells"].to_numpy())
        done += len(g)
        log(f"  {os.path.basename(f)}: {done}/{len(prof)} profiles ({time.time() - t0:.0f} s)")
    np.savez_compressed(path, counts=counts.reshape(N, L, C), total=tot.reshape(N, L), cells=nc.reshape(N, L),
                        cols=cols, tokens=toks, samples=np.array(samples), lines=np.array(S.lines))
    log(f"extract done in {time.time() - t0:.0f} s -> {path}")


# ============================================================================= annotations
STRESS_RE = re.compile(r"^(HSPA\d|HSPH\d|HSPB\d|HSP90|DNAJ[AB]\d|MT1[A-Z]?$|MT2A$|GADD45|IER\d|DUSP\d|NR4A\d|"
                       r"ZFP36|EGR\d|FOS|JUN|ATF[345]$|HMOX1$|SQSTM1$|TXNRD1$|SRXN1$|CHAC1$|TRIB3$|DDIT[34]$|"
                       r"SESN2$|PPP1R15A$|XBP1$|HERPUD1$|BAG3$|TXNIP$|ARRDC[34]$|KLF[246]$|CYR61$|CCN[12]$|"
                       r"SERTAD1$|BTG[12]$|PLK[23]$|HEXIM1$|MCL1$|MYC$)")


def stress_set():
    s = set(REPO_IEG)
    for k in ("P53_EXT", "NRF2_CORE", "ISR_ATF4", "UPR_ER", "HSF1_HEAT", "IFN", "NFKB"):
        s |= set(P.CONTEXT[k])
    for k in ("P53_ACTIVITY", "FERRO_MARKERS", "INFLAMMASOME"):
        s |= set(P.SCORES[k])
    s |= {"ATF3", "DDIT3", "PMAIP1", "CDKN1A", "MDM2", "TP53", "MYC", "MCL1", "HEXIM1", "JUN", "FOS", "EGR1",
          "GADD45A", "BTG2", "SESN2", "PPM1D"}
    return s


# genes of the D2 screen read-outs (MG53 pathways named in the plan): a reference must not be one of them
D2_READOUTS = {
    "NF-kB": "NFKB1 NFKB2 RELA RELB REL NFKBIA NFKBIB NFKBIE TNFAIP3 BIRC2 BIRC3 IKBKB CHUK IKBKG".split(),
    "PI3K-AKT / IRS1 / FAK": "PIK3CA PIK3CB PIK3CD PIK3R1 PIK3R2 AKT1 AKT2 AKT3 PTEN IRS1 IRS2 PTK2 MTOR RPTOR "
                             "RICTOR PDK1 PDPK1 TSC1 TSC2 INSR IGF1R FOXO1 FOXO3 GSK3B".split(),
    "cyclin D1 / cell cycle": "CCND1 CCND2 CCND3 CDK4 CDK6 RB1 E2F1 CCNE1 CCNE2 CDKN1B CDKN2A".split(),
    "RAC1": "RAC1 RAC2 RAC3 CDC42 RHOA PAK1 PAK2 WASL".split(),   # WASL (N-WASP): Cdc42 effector (Rohatgi 1999)
    "AMPK": "PRKAA1 PRKAA2 PRKAB1 PRKAB2 PRKAG1 PRKAG2 STK11".split(),
    "G3BP2 / KIF11": "G3BP1 G3BP2 KIF11 CAPRIN1 USP10".split(),   # Caprin1 / USP10: G3BP partners (Kedersha 2016)
    "ferroptosis": "SLC7A11 SLC3A2 GPX4 ACSL4 LPCAT3 AIFM2 TFRC FTH1 FTL NCOA4 HMOX1 NFE2L2 KEAP1 GCLC GCLM".split(),
    "apoptosis": "BAX BAK1 BCL2 BCL2L1 BCL2L11 MCL1 BID BBC3 PMAIP1 CASP3 CASP7 CASP8 CASP9 XIAP APAF1 CYCS "
                 "FAS TNFRSF10B".split(),
    "p53 axis": "TP53 MDM2 MDM4 CDKN1A TP53I3 FDXR ZMAT3 SESN1 RRM2B GDF15 PPM1D USP7".split(),
    "MG53 itself / locus": "TRIM72 FUS PYCARD PYCARD-AS1 ITGAM".split(),
}

sys.path.insert(0, os.path.join(REPO, "mg53_p53", "upstream_coregulation"))
try:                     # the repo's signalling classes on HGNC gene groups (kinase, phosphatase, GTPase, receptor, ...)
    from upstream_coregulation import SIGNAL_RULES          # noqa: E402
except Exception:                                           # pragma: no cover
    SIGNAL_RULES = [
        ("protein kinase", r"kinase", r"anchoring|guanylate kinase|Carbohydrate kinases|phosphatase|Nucleoside|"
                                      r"inhibitor|regulatory subunit"),
        ("phosphatase", r"phosphatase", r"HAD Asp-based|Acid phosphatases|Alkaline"),
        ("small GTPase / GAP / GEF", r"GTPase|guanine nucleotide exchange|Rho guanine", r"Translational GTPases"),
        ("receptor (non-olfactory)", r"receptor", r"Olfactory|Vomeronasal|T cell receptor|Receptor ligands|Taste"),
        ("E3 ligase / ubiquitin", r"E3 ubiquitin|ubiquitin|Ring finger|Tripartite motif", r"$^"),
        ("cytokine / growth factor", r"Interleukin|Chemokine|growth factor|cytokine|Receptor ligands",
         r"receptor$|receptors"),
    ]


def signalling_class(groups):
    out = []
    for name, inc, exc in SIGNAL_RULES:
        for gname in str(groups or "").split("|"):
            if gname and re.search(inc, gname, re.I) and not re.search(exc, gname, re.I):
                out.append(name)
                break
    return "; ".join(out)


FUNCTION_RULES = [   # coarse function classes (for 'different pathways'); first match wins
    ("ribosome (cytosolic)", r"^(RPL\d|RPS\d|RPLP\d|RPSA$|RACK1$|FAU$|UBA52$)"),
    ("mitochondrial ribosome", r"^(MRPL|MRPS)"),
    ("translation factor", r"^(EIF\d|EEF\d|ETF1$|PABPC)"),
    ("proteasome", r"^(PSM[A-G]\d)"),
    ("ubiquitin", r"^(UBB$|UBC$|UBA\d|UBE\d|USP\d|UBQLN)"),
    ("spliceosome / mRNA processing", r"^(SNRP|SF3|SF1$|HNRNP|SRSF|PRPF|LSM\d|U2AF|SNRNP|DDX\d|DHX\d|NONO$|SFPQ$)"),
    ("respiratory chain / ATP synthase", r"^(NDUF|COX\d|COX[4-8][A-Z]|UQCR|SDH[A-D]$|ATP5|CYC1$|CYCS$)"),
    ("glycolysis", r"^(GAPDH$|PGK1$|ENO1$|PKM$|ALDOA$|TPI1$|LDHA$|LDHB$|PGAM1$|GPI$|HK[12]$|PFK[LMP]$)"),
    ("cytoskeleton / actin", r"^(ACT[BG]\d?$|TUB[AB]|MYL\d|MYH9$|TPM\d|CFL\d|PFN\d|VIM$|KRT\d|ACTN|TMSB)"),
    ("chaperone / chaperonin", r"^(HSP|CCT\d|DNAJ|TCP1$|PPI[ABDEFGH]$|FKBP)"),
    ("14-3-3", r"^YWHA"),
    ("nucleo-cytoplasmic transport", r"^(NUP\d|KPNA|KPNB|XPO\d|RAN$|RANBP|CSE1L$)"),
    ("histone / chromatin", r"^(H[1-4]|H2A|H2B|HMG[AB N])"),
    ("RNA polymerase II", r"^(POLR2)"),
    ("MHC / antigen presentation", r"^(B2M$|HLA-)"),
    ("V-ATPase / vesicle", r"^(ATP6V|SEC\d|COP[ABEGZ]|AP[1-4][MS])"),
]


def function_class(sym, group):
    for lab, rx in FUNCTION_RULES:
        if re.match(rx, sym):
            return lab
    g = str(group or "").split("|")[0].strip()
    return f"HGNC: {g}" if g and g.lower() != "nan" else f"other ({sym})"


def load_fischer(S):
    files = {}
    for n, name in [(5, "S1"), (6, "S2"), (7, "S3")]:
        f = f"TableS{name[-1]}_MOESM{n}.xlsx"
        p = os.path.join(FISCHER_LOCAL, f)
        if not os.path.exists(p):
            p = os.path.join(S.ext, "fischer2017", f)
            if not os.path.exists(p) and not curl(FISCHER_URL.format(n), p):
                raise SystemExit("could not download the Fischer 2017 p53 census tables; rerun later")
        files[name] = p
    s1 = pd.read_excel(files["S1"], header=0)
    s2 = pd.read_excel(files["S2"], header=0)
    s3 = pd.read_excel(files["S3"], header=0)
    sym1 = set(s1["Gene Symbol"].dropna().astype(str))
    sym3 = set(s3["Gene Symbol"].dropna().astype(str))
    s2 = s2.drop_duplicates("Gene Symbol").set_index(s2.drop_duplicates("Gene Symbol")["Gene Symbol"].astype(str))
    return sym1, sym3, s2


def load_hgnc(S):
    p = HGNC_LOCAL
    if not os.path.exists(p):
        p = os.path.join(S.ext, "hgnc_complete_set.txt")
        if not os.path.exists(p) and not curl(HGNC_URL, p):
            raise SystemExit("could not download the HGNC complete set; rerun later")
    h = pd.read_csv(p, sep="\t", dtype=str, usecols=["symbol", "name", "locus_group", "gene_group", "location",
                                                     "ensembl_gene_id"])
    pseudo = h[h["locus_group"] == "pseudogene"]["symbol"].astype(str)
    return h, pseudo


def n_pseudogenes(sym, pseudo_syms):
    rx = re.compile(r"^" + re.escape(sym) + r"P\d+$")
    return int(sum(bool(rx.match(s)) for s in pseudo_syms))


# ============================================================================= screen
def step_screen(S):
    import warnings
    warnings.filterwarnings("ignore", category=RuntimeWarning)
    fx = S.fx
    z = np.load(os.path.join(S.cache, "counts.npz"))
    cols = z["cols"]
    if list(z["samples"]) != S.wells["sample"].astype(str).tolist():
        raise SystemExit("cache/counts.npz does not match the atlas wells; run --steps extract again")
    counts, tot, nc = z["counts"], z["total"], z["cells"]
    N, L, C = counts.shape
    g = S.genes.iloc[cols].reset_index(drop=True)
    sym = g["label"].astype(str).to_numpy()           # unique display name (symbol; + Ensembl id if duplicated)
    bare = g["symbol"].astype(str).to_numpy()         # plain symbol for matching gene lists
    w = S.wells
    plate = w["plate"].astype(str).to_numpy()
    drug_w = ~S.dmso_w
    em = np.asarray(fx.expr_mask)[:, cols]
    W1a = np.asarray(fx.W1)[S.wsel][:, cols].astype(np.float32)
    effa = np.nan_to_num(W1a - np.asarray(fx.W2)[S.wsel][:, cols]).astype(np.float32)
    Scomp = A.composition_matrix(fx)[S.wsel]
    loc = {int(r): i for i, r in enumerate(S.wsel)}
    cond = S.cond.copy()
    cond_wells = [np.array([loc[int(i)] for i in fx.wells_of_dd[int(r)]]) for r in cond["dd_row"]]
    dmso_by_plate = {p: np.flatnonzero(S.dmso_w & (plate == p)) for p in S.plates}
    plate_rows = {p: np.flatnonzero(plate == p) for p in S.plates}
    K = len(cond)
    LN2 = np.log(2.0) ** 2
    # outputs: corrected per line (K drug-doses + DMSO), raw per line (K), Poisson variances, DMSO replicates
    corr = np.full((K + 1, L, C), np.nan, dtype=np.float32)
    corr_var = np.full((K + 1, L, C), np.nan, dtype=np.float32)
    raw = np.full((K, L, C), np.nan, dtype=np.float32)
    raw_var = np.full((K, L, C), np.nan, dtype=np.float32)
    tw = np.concatenate(cond_wells)                       # target wells (for geNorm)
    tw_cond = np.concatenate([[k] * len(x) for k, x in enumerate(cond_wells)])
    raw_well = np.full((len(tw), L, C), np.nan, dtype=np.float32)
    P_ = len(S.plates)
    rep = np.full((P_, L, C), np.nan, dtype=np.float32)
    rep_var = np.full((P_, L, C), np.nan, dtype=np.float32)
    dmso_cpm = np.zeros((L, C))
    val = []
    B = 300
    t0 = time.time()
    for b0 in range(0, C, B):
        b = slice(b0, min(C, b0 + B))
        cb = np.asarray(counts[:, :, b], dtype=np.float32)
        Y = A.log_cpm(cb, tot, nc)                         # nan where < MIN_CELLS cells
        ok = nc >= A.MIN_CELLS
        Ye = Y.copy()
        Ye[:, ~em[:, b]] = np.nan
        r1 = np.full_like(Ye, np.nan)
        for p, rows in plate_rows.items():
            d = rows[drug_w[rows]]
            base = np.nanmedian(Ye[d], axis=0)
            r1[rows] = Ye[rows] - base[None] - Scomp[rows][:, :, None]
        W1 = np.nanmedian(r1, axis=1)
        W1[np.isfinite(r1).sum(axis=1) < A.MIN_LINES] = np.nan
        both = np.isfinite(W1) & np.isfinite(W1a[:, b])
        dif = np.where(both, np.abs(W1 - W1a[:, b]), 0.0)
        val.append(pd.DataFrame({"gene": sym[b], "max_abs_diff_W1_vs_atlas": dif.max(axis=0),
                                 "wells_both_finite": both.sum(axis=0),
                                 "wells_finite_mismatch": (np.isfinite(W1) != np.isfinite(W1a[:, b])).sum(axis=0)}))
        r2 = np.where(np.isfinite(W1)[:, None, :], r1 - effa[:, b][:, None, :], np.nan)
        vpois = np.where(ok[:, :, None], 1.0 / (cb + 0.5) / LN2, np.nan).astype(np.float32)
        # DMSO pool per plate and line (counts summed over the plate's DMSO wells with >= MIN_CELLS cells)
        Yd = np.full((P_, L, cb.shape[2]), np.nan, dtype=np.float32)
        cd_ = np.full_like(Yd, np.nan)
        for pi, p in enumerate(S.plates):
            dw = dmso_by_plate[p]
            m = ok[dw]                                     # (2, L)
            c_sum = (cb[dw] * m[:, :, None]).sum(axis=0)
            t_sum = (tot[dw] * m).sum(axis=0)
            n_sum = (nc[dw] * m).sum(axis=0)
            good = n_sum >= A.MIN_CELLS
            Yd[pi] = np.where(good[:, None], np.log2((c_sum + 0.5) / (t_sum[:, None] + 1.0) * 1e6), np.nan)
            cd_[pi] = np.where(good[:, None], c_sum, np.nan)
            if len(dw) == 2:
                a_, b_ = dw
                rep[pi, :, b] = Y[a_] - Y[b_]
                rep_var[pi, :, b] = vpois[a_] + vpois[b_]
        pidx = {p: i for i, p in enumerate(S.plates)}
        wp = np.array([pidx[p] for p in plate])
        ratio = Y - Yd[wp]
        rvar = vpois + 1.0 / (cd_[wp] + 0.5) / LN2
        for k, ii in enumerate(cond_wells):
            x = r2[ii]
            n = np.isfinite(x).sum(axis=0)
            corr[k, :, b] = np.where(n > 0, np.nanmean(x, axis=0), np.nan)
            corr_var[k, :, b] = np.where(n > 0, np.nansum(np.where(np.isfinite(x), vpois[ii], np.nan), axis=0)
                                         / np.maximum(n, 1) ** 2, np.nan)
            x = ratio[ii]
            n = np.isfinite(x).sum(axis=0)
            raw[k, :, b] = np.where(n > 0, np.nanmean(x, axis=0), np.nan)
            raw_var[k, :, b] = np.where(n > 0, np.nansum(np.where(np.isfinite(x), rvar[ii], np.nan), axis=0)
                                        / np.maximum(n, 1) ** 2, np.nan)
        dw_all = np.flatnonzero(S.dmso_w)
        x = r2[dw_all]
        n = np.isfinite(x).sum(axis=0)
        corr[K, :, b] = np.where(n > 0, np.nanmean(x, axis=0), np.nan)
        corr_var[K, :, b] = np.where(n > 0, np.nansum(np.where(np.isfinite(x), vpois[dw_all], np.nan), axis=0)
                                     / np.maximum(n, 1) ** 2, np.nan)
        raw_well[:, :, b] = ratio[tw]
        m = ok[dw_all]
        dmso_cpm[:, b] = (cb[dw_all] * m[:, :, None]).sum(axis=0) / (tot[dw_all] * m).sum(axis=0)[:, None] * 1e6
        log(f"  screen: genes {b0 + 1}-{min(C, b0 + B)} of {C} ({time.time() - t0:.0f} s)")
        del cb, Y, Ye, r1, r2, ratio, rvar, vpois
    del counts
    validation = pd.concat(val, ignore_index=True)
    np.savez_compressed(os.path.join(S.cache, "per_line_effects.npz"), corrected=corr, corrected_var=corr_var,
                        raw=raw, raw_var=raw_var, dmso_rep=rep, dmso_rep_var=rep_var, dmso_cpm=dmso_cpm,
                        genes=np.array(sym, dtype=str), lines=np.array(S.lines, dtype=str), conditions=np.array(
                            cond["condition"].tolist() + ["DMSO (vs plate drug-well median)"]))

    ci = S.cand_i
    prim = np.flatnonzero(cond["primary"].to_numpy())
    corr_rows = np.concatenate([prim, [K]])                # + DMSO
    cond_names = cond["condition"].tolist() + ["DMSO (vs plate drug-well median)"]

    def frame_metrics(X, V, rows, names, lines_i):
        """X, V: (conditions, lines, genes). RMS over all (condition, line) cells, noise-adjusted RMS, median line
        per condition, worst |median| and where, 95th percentile of |value|."""
        x = X[rows][:, lines_i]
        v = V[rows][:, lines_i]
        ms = np.nanmean(x ** 2, axis=(0, 1))
        mv = np.nanmean(np.where(np.isfinite(x), v, np.nan), axis=(0, 1))
        med = np.nanmedian(x, axis=1)                         # (cond, genes)
        am = np.abs(med)
        worst = np.nanargmax(np.where(np.isfinite(am), am, -1), axis=0)
        return {"rms": np.sqrt(ms), "rms_adj": np.sqrt(np.maximum(0, ms - mv)), "noise": np.sqrt(mv),
                "max_shift": am[worst, np.arange(x.shape[2])],
                "max_shift_signed": med[worst, np.arange(x.shape[2])],
                "worst": np.array([names[r] for r in np.asarray(rows)[worst]]),
                "p95": np.nanpercentile(np.abs(x).reshape(-1, x.shape[2]), 95, axis=0),
                "n_cells": np.isfinite(x).sum(axis=(0, 1)), "median": med}

    fc = frame_metrics(corr, corr_var, corr_rows, cond_names, ci)
    fr = frame_metrics(raw, raw_var, prim, cond_names, ci)
    instab = np.sqrt((fc["rms_adj"] ** 2 + fr["rms_adj"] ** 2) / 2)
    is_a = cond["drug_short"].isin(P53_ARM).to_numpy()
    prim_a = np.array([k for k in prim if is_a[k]])
    prim_b = np.array([k for k in prim if not is_a[k]])
    arms = {}
    for lab, rows_c, rows_r in (("p53arm", np.concatenate([prim_a, [K]]), prim_a), ("stressarm", prim_b, prim_b)):
        a_ = frame_metrics(corr, corr_var, rows_c, cond_names, ci)
        b_ = frame_metrics(raw, raw_var, rows_r, cond_names, ci)
        use_raw = b_["max_shift"] > a_["max_shift"]
        arms[lab] = {"instability": np.sqrt((a_["rms_adj"] ** 2 + b_["rms_adj"] ** 2) / 2),
                     "worst": np.where(use_raw, b_["max_shift_signed"], a_["max_shift_signed"]),
                     "worst_cond": np.where(use_raw, np.char.add(b_["worst"].astype(str), " (raw)"),
                                            np.char.add(a_["worst"].astype(str), " (corrected)"))}

    # all 50 lines (each line where the gene reads >= 10 CPM in DMSO)
    expr10 = dmso_cpm >= 10
    def rms_lines(X, rows):
        x = X[rows]
        x = np.where(expr10[None], x, np.nan)
        return np.sqrt(np.nanmean(x ** 2, axis=(0, 1)))
    raw_rms_all = rms_lines(raw, prim)
    corr_rms_all = rms_lines(corr, corr_rows)

    # DMSO replicate wells (same plate, same line): per-well SD, Poisson part out
    rc = rep[:, ci]
    rv = rep_var[:, ci]
    rep_sd = np.sqrt(np.nanmean(rc ** 2, axis=(0, 1)) / 2)
    rep_sd_adj = np.sqrt(np.maximum(0, np.nanmean(rc ** 2, axis=(0, 1)) - np.nanmean(
        np.where(np.isfinite(rc), rv, np.nan), axis=(0, 1))) / 2)

    # TP53 WT vs altered, per primary drug-dose (corrected frame, all lines expressing the gene)
    p53_rows = []
    best_diff = np.zeros(C)
    best_q = np.ones(C)
    best_c = np.array([""] * C, dtype=object)
    for k in prim:
        X = np.where(em, corr[k], np.nan)
        a = X[S.wt]
        bb = X[S.alt]
        diff = np.nanmean(a, axis=0) - np.nanmean(bb, axis=0)
        okc = (np.isfinite(a).sum(axis=0) >= 8) & (np.isfinite(bb).sum(axis=0) >= 8)
        p = np.full(C, np.nan)
        if okc.any():
            p[okc] = stats.mannwhitneyu(a[:, okc], bb[:, okc], axis=0, nan_policy="omit").pvalue
        q = bh(p)
        hit = (np.abs(diff) >= P53_DIFF) & (q < 0.05)
        better = hit & (np.abs(diff) > np.abs(best_diff) * (best_q < 0.05))
        best_diff = np.where(better, diff, best_diff)
        best_q = np.where(better, q, best_q)
        best_c = np.where(better, cond_names[k], best_c)
        p53_rows.append(pd.DataFrame({"gene": sym, "condition": cond_names[k], "wt_minus_altered_log2": diff,
                                      "p": p, "q": q}))
    p53_long = pd.concat(p53_rows, ignore_index=True)
    max_abs_diff = p53_long.groupby("gene", sort=False)["wt_minus_altered_log2"].apply(
        lambda s: s.abs().max()).reindex(sym).to_numpy()

    # all of Tahoe: pooled per drug-dose (atlas, method v3), drug-doses not only on the unreliable plate
    ddok = ~fx.dd["unreliable_plate_only"].to_numpy()
    L_ = np.asarray(fx.DD_lfc)[ddok][:, cols]
    Qu = np.asarray(fx.DD_qup)[ddok][:, cols]
    Qd = np.asarray(fx.DD_qdn)[ddok][:, cols]
    sig = ((Qu < A.Q_CUT) & (L_ >= A.LFC_MIN)) | ((Qd < A.Q_CUT) & (L_ <= -A.LFC_MIN))
    pct_sig_all = 100 * sig.mean(axis=0)
    rms_all_dd = np.sqrt(np.nanmean(L_ ** 2, axis=0))
    trows = cond.loc[cond["primary"], "dd_row"].to_numpy()
    Lt = np.asarray(fx.DD_lfc)[trows][:, cols]
    sig_t = (((np.asarray(fx.DD_qup)[trows][:, cols] < A.Q_CUT) & (Lt >= A.LFC_MIN)) |
             ((np.asarray(fx.DD_qdn)[trows][:, cols] < A.Q_CUT) & (Lt <= -A.LFC_MIN)))
    n_sig_target = sig_t.sum(axis=0)
    # co-variation across all drug-doses (for picking references from different programmes)
    Zall = np.nan_to_num(np.asarray(fx.DD_z)[ddok][:, cols])

    # ---------------------------------------------------------------- annotations and filters
    log("annotations: Fischer 2017 census, HGNC, readthrough classes")
    sym1, sym3, s2 = load_fischer(S)
    hg, pseudo = load_hgnc(S)
    hgi = hg.drop_duplicates("symbol").set_index("symbol")
    dog = pd.read_csv(DOG_TABLE).set_index("col")
    stress = stress_set()
    d2 = {gg: k for k, v in D2_READOUTS.items() for gg in v}
    sg = set(T.S_GENES) | set(T.G2M_GENES)
    res = pd.DataFrame({"gene": sym, "atlas_col": cols, "token": g["token"].to_numpy()})
    res["dmso_cpm_min_candidate_lines"] = dmso_cpm[ci].min(axis=0)
    res["dmso_cpm_median_candidate_lines"] = np.median(dmso_cpm[ci], axis=0)
    res["dmso_cpm_lowest_line"] = [S.lname[S.cand[i]] for i in dmso_cpm[ci].argmin(axis=0)]
    res["dmso_cpm_min_all_lines"] = dmso_cpm.min(axis=0)
    res["n_lines_dmso_ge50cpm_of50"] = (dmso_cpm >= MIN_DMSO_CPM).sum(axis=0)
    for lab, f in (("raw", fr), ("corrected", fc)):
        res[f"{lab}_rms_log2"] = f["rms"]
        res[f"{lab}_rms_adj_log2"] = f["rms_adj"]
        res[f"{lab}_counting_noise_log2"] = f["noise"]
        res[f"{lab}_worst_median_shift_log2"] = f["max_shift_signed"]
        res[f"{lab}_worst_condition"] = f["worst"]
        res[f"{lab}_p95_abs_log2"] = f["p95"]
    res["instability_log2"] = instab
    for lab in ("p53arm", "stressarm"):
        res[f"{lab}_instability_log2"] = arms[lab]["instability"]
        res[f"{lab}_worst_median_shift_log2"] = arms[lab]["worst"]
        res[f"{lab}_worst_condition"] = arms[lab]["worst_cond"]
    res["raw_rms_log2_all_lines_expressing"] = raw_rms_all
    res["corrected_rms_log2_all_lines_expressing"] = corr_rms_all
    res["dmso_replicate_sd_log2"] = rep_sd
    res["dmso_replicate_sd_adj_log2"] = rep_sd_adj
    res["tp53_wt_minus_altered_max_abs_log2"] = max_abs_diff
    res["tp53_wt_minus_altered_flag_log2"] = np.where(best_c != "", best_diff, np.nan)
    res["tp53_wt_minus_altered_flag_q"] = np.where(best_c != "", best_q, np.nan)
    res["tp53_wt_minus_altered_flag_condition"] = best_c
    res["pooled_target_drugdoses_sig_of15"] = n_sig_target
    res["alltahoe_pct_drugdoses_sig"] = pct_sig_all
    res["alltahoe_rms_pooled_log2"] = rms_all_dd
    # flags
    res["fischer2017_p53_target"] = [
        (s in sym1) or (s in sym3) or (s in s2.index and (float(s2.loc[s, "sum direct target (0..16)"]) >= FISCHER_DIRECT
                                                          or abs(float(s2.loc[s, "p53 Expression Score (-20..0..20)"]))
                                                          >= FISCHER_EXPR)) for s in bare]
    res["fischer2017_detail"] = [
        "; ".join(([f"S1 literature"] if s in sym1 else []) + ([f"S3 high-confidence"] if s in sym3 else []) +
                  ([f"S2 direct-target datasets {int(s2.loc[s, 'sum direct target (0..16)'])}, expression score "
                    f"{int(s2.loc[s, 'p53 Expression Score (-20..0..20)'])}"] if s in s2.index else []))
        for s in bare]
    res["immediate_early_or_stress"] = [s in stress or bool(STRESS_RE.match(s)) for s in bare]
    res["cell_cycle_gene"] = [s in sg for s in bare]
    res["d2_readout_pathway"] = [d2.get(s, "") for s in bare]
    dg = dog.reindex(cols)
    res["dog_class"] = dg["class"].fillna("no coordinates").to_numpy()
    upr = (dg["up_cpm"] / dg["pooled_cpm"]).to_numpy()
    cvr = (dg["conv_cpm"] / dg["pooled_cpm"]).to_numpy()
    sense = (dg["up_dist"].to_numpy() <= 20_000) & (upr >= 0.5)
    anti = (dg["conv_dist"].to_numpy() <= 20_000) & (cvr >= 0.5)
    ovl = dg["overlaps_same_strand_expressed_gene"].astype(str).str.lower().eq("true").to_numpy()
    rt = []
    for i in range(C):
        r_ = []
        if res["dog_class"].iloc[i] in ("sense_exposed", "antisense_exposed_only"):
            r_.append(f"repo DoG class {res['dog_class'].iloc[i]}")
        if sense[i]:
            r_.append(f"same-strand {dg['up_same_strand_gene'].iloc[i]} ends {dg['up_dist'].iloc[i] / 1000:.1f} kb "
                      f"upstream ({upr[i]:.1f}x its level)")
        if anti[i]:
            r_.append(f"convergent {dg['conv_opp_strand_gene'].iloc[i]} {dg['conv_dist'].iloc[i] / 1000:.1f} kb "
                      f"downstream ({cvr[i]:.1f}x; matters for strand-agnostic RT)")
        if ovl[i]:
            r_.append("overlaps another expressed same-strand gene")
        rt.append("; ".join(r_))
    res["readthrough_exposure"] = rt
    chrom = dg["chrom"].astype(str).to_numpy()
    st_, en_ = dg["start"].to_numpy(dtype=float), dg["end"].to_numpy(dtype=float)
    c0, s0, e0 = TRIM72_LOCUS
    res["trim72_locus_1Mb"] = (chrom == c0) & (en_ >= s0 - 1_000_000) & (st_ <= e0 + 1_000_000)
    res["chromosome"] = chrom
    res["noise_rna"] = [bool(A.NOISE_RNA_RE.match(s)) for s in bare]
    res["hgnc_name"] = [hgi["name"].get(s, "") if isinstance(hgi["name"].get(s, ""), str) else "" for s in bare]
    res["hgnc_gene_group"] = [hgi["gene_group"].get(s, "") if isinstance(hgi["gene_group"].get(s, ""), str) else ""
                              for s in bare]
    res["function_class"] = [function_class(s, gg) for s, gg in zip(bare, res["hgnc_gene_group"])]
    res["signalling_class"] = [signalling_class(gg) for gg in res["hgnc_gene_group"]]
    res.loc[res["function_class"].isin(["ubiquitin"]) & (res["signalling_class"] == ""), "signalling_class"] = \
        "E3 ligase / ubiquitin"
    pseudo_list = pseudo.tolist()
    res["hgnc_named_pseudogenes"] = [n_pseudogenes(s, pseudo_list) for s in bare]

    # eligibility
    reasons = []
    for i, r in res.iterrows():
        x = []
        if r["dmso_cpm_min_candidate_lines"] < MIN_DMSO_CPM:
            x.append(f"DMSO level {r['dmso_cpm_min_candidate_lines']:.0f} CPM < {MIN_DMSO_CPM:g} in "
                     f"{r['dmso_cpm_lowest_line']}")
        if bare[i] in CONTROLS:
            x.append("positive control (expected to move)")
        if r["fischer2017_p53_target"]:
            x.append(f"p53 target (Fischer 2017: {r['fischer2017_detail']})")
        if r["tp53_wt_minus_altered_flag_condition"]:
            x.append(f"TP53-status-dependent in Tahoe (WT - altered {r['tp53_wt_minus_altered_flag_log2']:+.2f} log2 "
                     f"under {r['tp53_wt_minus_altered_flag_condition']}, q {r['tp53_wt_minus_altered_flag_q']:.1g})")
        if r["immediate_early_or_stress"]:
            x.append("immediate-early / stress gene")
        if r["cell_cycle_gene"]:
            x.append("cell-cycle (S/G2M) gene")
        if r["d2_readout_pathway"]:
            x.append(f"D2 read-out pathway ({r['d2_readout_pathway']})")
        if r["readthrough_exposure"]:
            x.append(f"readthrough exposure ({r['readthrough_exposure']})")
        if r["trim72_locus_1Mb"]:
            x.append("within 1 Mb of TRIM72")
        if r["noise_rna"]:
            x.append("noise RNA class (mito / histone / pseudogene)")
        if abs(r["p53arm_worst_median_shift_log2"]) > MAX_SHIFT:
            x.append(f"moves in the p53 arm: {r['p53arm_worst_median_shift_log2']:+.2f} log2 under "
                     f"{r['p53arm_worst_condition']}")
        reasons.append(x)
    res["eligible"] = [len(x) == 0 for x in reasons]
    res["exclusion_reasons"] = ["; ".join(x) for x in reasons]
    res["rank_all_screened"] = res["instability_log2"].rank(method="min").astype(int)
    el = res["eligible"].to_numpy()
    res["rank_eligible"] = np.nan
    res.loc[el, "rank_eligible"] = res.loc[el, "instability_log2"].rank(method="min")

    # ---------------------------------------------------------------- pick 3 + 2 from different functions
    order = res.loc[el].sort_values("instability_log2").index.to_numpy()
    zc = Zall - Zall.mean(axis=0)
    zc = zc / np.maximum(np.linalg.norm(zc, axis=0), 1e-9)
    picked, why_skip = [], {}
    for i in order:
        if len(picked) == 5:
            break
        if res.loc[i, "signalling_class"]:
            why_skip[i] = (f"signalling gene ({res.loc[i, 'signalling_class']}): D2 reads MG53 signalling pathways and "
                           "MG53 is an E3 ligase, so it is not picked")
            continue
        fcl = res.loc[i, "function_class"]
        clash = [j for j in picked if res.loc[j, "function_class"] == fcl]
        if clash:
            why_skip[i] = f"same function class as {res.loc[clash[0], 'gene']} ({fcl})"
            continue
        rr = [float(zc[:, i] @ zc[:, j]) for j in picked]
        if rr and max(np.abs(rr)) >= 0.4:
            j = picked[int(np.argmax(np.abs(rr)))]
            why_skip[i] = f"co-varies with {res.loc[j, 'gene']} across all Tahoe drug-doses (r {max(rr, key=abs):+.2f})"
            continue
        picked.append(i)
    res["role"] = ""
    for k, i in enumerate(picked):
        res.loc[i, "role"] = "reference" if k < 3 else "backup"
    res["max_abs_r_with_picked_alltahoe"] = np.nan
    for i in order[:60]:
        rr = [abs(float(zc[:, i] @ zc[:, j])) for j in picked if j != i]
        res.loc[i, "max_abs_r_with_picked_alltahoe"] = max(rr) if rr else np.nan
    why = []
    for i, r in res.iterrows():
        if r["eligible"]:
            s = (f"eligible, rank {int(r['rank_eligible'])}: instability {r['instability_log2']:.3f} log2 over all "
                 f"primary conditions (raw RMS {r['raw_rms_adj_log2']:.3f}, corrected RMS "
                 f"{r['corrected_rms_adj_log2']:.3f}, counting noise out); p53 arm worst "
                 f"{r['p53arm_worst_median_shift_log2']:+.2f} ({r['p53arm_worst_condition']}); stress arm worst "
                 f"{r['stressarm_worst_median_shift_log2']:+.2f} ({r['stressarm_worst_condition']}); "
                 f"DMSO >= {r['dmso_cpm_min_candidate_lines']:.0f} CPM in all candidate lines")
            if r["role"]:
                s = f"PICKED as {r['role']} ({r['function_class']}); " + s
            elif i in why_skip:
                s += f"; not picked: {why_skip[i]}"
        else:
            s = "excluded: " + r["exclusion_reasons"]
        why.append(s)
    res["why"] = why
    lead = ["gene", "role", "eligible", "rank_eligible", "instability_log2", "why", "function_class"]
    res = res[lead + [c for c in res.columns if c not in lead]]
    res = res.sort_values(["eligible", "instability_log2"], ascending=[False, True])
    rs = res.set_index("gene")
    os.makedirs(S.out, exist_ok=True)
    res.to_csv(os.path.join(S.out, "reference_gene_screen.csv"), index=False, float_format="%.4g")
    log(f"screened {C} genes; eligible {int(el.sum())}; picked {[sym[i] for i in picked]}")

    # ---------------------------------------------------------------- robustness of the ranking
    def combo(rows_c, rows_r, lines_i):
        a_ = frame_metrics(corr, corr_var, rows_c, cond_names, lines_i)
        b_ = frame_metrics(raw, raw_var, rows_r, cond_names, lines_i)
        return np.sqrt((a_["rms_adj"] ** 2 + b_["rms_adj"] ** 2) / 2)
    cand_wt = np.array([i for i in ci if S.wt[i]])
    cand_alt = np.array([i for i in ci if S.alt[i]])
    all_k = np.arange(K)
    variants = {
        "default: both frames, 14 candidate lines, primary doses": instab,
        "raw (DMSO-referenced) frame only": fr["rms_adj"],
        "corrected (method v3) frame only": fc["rms_adj"],
        "p53 arm only (DMSO, anthracyclines, selinexor)": arms["p53arm"]["instability"],
        "stress arm only (homoharringtonine, auranofin, dinaciclib)": arms["stressarm"]["instability"],
        "all 50 lines": combo(corr_rows, prim, np.arange(L)),
        "0.05 uM doses added": combo(np.concatenate([all_k, [K]]), all_k, ci),
        "TP53-WT candidate lines only": combo(corr_rows, prim, cand_wt),
        "TP53-altered candidate lines only": combo(corr_rows, prim, cand_alt),
        "without counting-noise adjustment": np.sqrt((fc["rms"] ** 2 + fr["rms"] ** 2) / 2),
    }
    show_r = list(dict.fromkeys(list(picked) + list(order[:25])))
    rob = []
    for lab, v in variants.items():
        rk = pd.Series(v[el]).rank(method="min").to_numpy()
        rank_of = dict(zip(np.flatnonzero(el), rk))
        for i in show_r:
            rob.append({"gene": sym[i], "role": res.loc[i, "role"], "variant": lab,
                        "rank_among_eligible": int(rank_of[i]), "n_eligible": int(el.sum()),
                        "instability_log2": float(v[i])})
    rob = pd.DataFrame(rob)
    rob["why"] = ("rank of the gene among all eligible genes when the instability score is computed this way "
                  "(lower = more stable); the picks should stay near the top under every variant")
    rob.to_csv(os.path.join(S.out, "robustness.csv"), index=False, float_format="%.4g")

    # ---------------------------------------------------------------- long table per condition
    gi = {s: i for i, s in enumerate(sym)}
    show = list(dict.fromkeys([sym[i] for i in picked] + [sym[i] for i in order[:30]] +
                              [s for s in CLASSIC if s in gi] + [s for s in CONTROLS if s in gi]))
    long = []
    all_rows = list(range(K)) + [K]
    for s in show:
        i = gi[s]
        for k in all_rows:
            xc = corr[k, ci, i]
            rec = {"gene": s, "role": rs.loc[s, "role"],
                   "condition": cond_names[k], "primary": bool(k == K or cond["primary"].iloc[k]),
                   "corrected_median_log2_candidate_lines": np.nanmedian(xc),
                   "corrected_min_log2": np.nanmin(xc), "corrected_max_log2": np.nanmax(xc),
                   "n_candidate_lines": int(np.isfinite(xc).sum())}
            if k < K:
                xr = raw[k, ci, i]
                rec.update({"raw_dmso_ratio_median_log2_candidate_lines": np.nanmedian(xr),
                            "raw_min_log2": np.nanmin(xr), "raw_max_log2": np.nanmax(xr),
                            "raw_fold_median": 2 ** np.nanmedian(xr),
                            "pooled_atlas_log2FC_all_lines": float(fx.DD_lfc[cond["dd_row"].iloc[k], cols[i]]),
                            "pooled_atlas_z": float(fx.DD_z[cond["dd_row"].iloc[k], cols[i]]),
                            "pooled_atlas_q_up": float(fx.DD_qup[cond["dd_row"].iloc[k], cols[i]]),
                            "pooled_atlas_q_down": float(fx.DD_qdn[cond["dd_row"].iloc[k], cols[i]])})
            long.append(rec)
    long = pd.DataFrame(long)
    long["why"] = np.where(long["condition"].str.startswith("DMSO"),
                           "DMSO wells vs the plate's drug-well median (corrected frame only; raw frame is DMSO-referenced)",
                           np.where(long["primary"], "primary condition (in the score)",
                                    "0.05 uM: reported, not in the score"))
    long.to_csv(os.path.join(S.out, "reference_by_condition.csv"), index=False, float_format="%.4g")

    # per line, picked + classics, every condition (both frames)
    pl = []
    for s in list(dict.fromkeys([sym[i] for i in picked] + [x for x in CLASSIC if x in gi])):
        i = gi[s]
        for k in all_rows:
            for li_ in range(L):
                pl.append({"gene": s, "condition": cond_names[k], "cell_line": S.lname[S.lines[li_]],
                           "candidate_line": S.lines[li_] in S.cand,
                           "tp53_group": S.status["tp53_group"].get(S.lines[li_], ""),
                           "dmso_cpm": dmso_cpm[li_, i], "corrected_log2": corr[k, li_, i],
                           "raw_dmso_ratio_log2": raw[k, li_, i] if k < K else np.nan})
    pd.DataFrame(pl).to_csv(os.path.join(S.out, "reference_per_line.csv"), index=False, float_format="%.4g")

    # ---------------------------------------------------------------- geNorm M (Vandesompele 2002)
    pool = list(dict.fromkeys([sym[i] for i in picked] + [sym[i] for i in order[:40]] +
                              [s for s in CLASSIC if s in gi]))
    pidx_ = np.array([gi[s] for s in pool])
    wprim = np.isin(tw_cond, prim)
    Ms, Vpair = [], []
    for li_ in ci:
        X = raw_well[wprim][:, li_, :][:, pidx_]            # wells x genes (log2 ratio vs DMSO)
        X = X[np.isfinite(X).all(axis=1)]
        if len(X) < 5:
            continue
        D = X[:, :, None] - X[:, None, :]
        V = D.std(axis=0, ddof=1)
        M = V.sum(axis=1) / (len(pool) - 1)
        Ms.append(M)
        Vpair.append(V)
    Ms = np.array(Ms)
    gen = pd.DataFrame({"gene": pool, "geNorm_M_mean_over_candidate_lines": Ms.mean(axis=0),
                        "geNorm_M_max_over_candidate_lines": Ms.max(axis=0),
                        "classic_reference": [s in CLASSIC for s in pool],
                        "role": [rs.loc[s, "role"] for s in pool],
                        "eligible": [bool(rs.loc[s, "eligible"]) for s in pool]})
    gen["geNorm_rank"] = gen["geNorm_M_mean_over_candidate_lines"].rank(method="min").astype(int)
    gen["why"] = ("M = mean SD of the log2 ratio to each other pool gene over the primary drug wells (DMSO-referenced),"
                  f" per candidate line ({len(Ms)} lines), averaged; lower = more stable; pool = picked + top 40 "
                  "eligible + classic references")
    gen = gen.sort_values("geNorm_M_mean_over_candidate_lines")
    gen.to_csv(os.path.join(S.out, "genorm.csv"), index=False, float_format="%.4g")

    # normalisation factor error: geometric mean of the picked references (and of single classics), per condition
    nf = []
    sets = {"picked 3 (geometric mean)": [sym[i] for i in picked[:3]],
            "picked 3 + 2 backups (geometric mean)": [sym[i] for i in picked],
            "GAPDH + ACTB (geometric mean)": ["GAPDH", "ACTB"]}
    for s in CLASSIC:
        if s in gi:
            sets[s] = [s]
    for lab, mem in sets.items():
        idx = [gi[m] for m in mem if m in gi]
        for k in prim:
            x = np.nanmean(raw[k][:, idx], axis=1)[ci]
            xc = np.nanmean(corr[k][:, idx], axis=1)[ci]
            nf.append({"normaliser": lab, "genes": " ".join(mem), "condition": cond_names[k],
                       "raw_median_log2_candidate_lines": np.nanmedian(x), "raw_max_abs_log2": np.nanmax(np.abs(x)),
                       "corrected_median_log2_candidate_lines": np.nanmedian(xc),
                       "corrected_max_abs_log2": np.nanmax(np.abs(xc)),
                       "why": "a shift s of the normaliser biases every target's ddCt by -s (log2 units = cycles)"})
    nf = pd.DataFrame(nf)
    nfs = nf.groupby("normaliser", sort=False).agg(
        genes=("genes", "first"),
        raw_rms_median_shift_log2=("raw_median_log2_candidate_lines", lambda v: float(np.sqrt(np.mean(v ** 2)))),
        raw_worst_median_shift_log2=("raw_median_log2_candidate_lines", lambda v: float(v.iloc[np.argmax(np.abs(v))])),
        raw_worst_single_line_log2=("raw_max_abs_log2", "max"),
        corrected_rms_median_shift_log2=("corrected_median_log2_candidate_lines",
                                         lambda v: float(np.sqrt(np.mean(v ** 2)))),
        corrected_worst_median_shift_log2=("corrected_median_log2_candidate_lines",
                                           lambda v: float(v.iloc[np.argmax(np.abs(v))]))).reset_index()
    nfs["worst_condition_raw"] = [nf[nf["normaliser"] == n].set_index("condition")[
        "raw_median_log2_candidate_lines"].abs().idxmax() for n in nfs["normaliser"]]
    nfs["why"] = "normaliser shift across the primary conditions (median candidate line); ddCt error = -shift"
    nf.to_csv(os.path.join(S.out, "normaliser_by_condition.csv"), index=False, float_format="%.4g")
    nfs.to_csv(os.path.join(S.out, "normaliser_summary.csv"), index=False, float_format="%.4g")

    # ---------------------------------------------------------------- classic references
    cl = []
    gen_i = gen.set_index("gene")
    for s in CLASSIC:
        if s not in gi:
            cl.append({"gene": s, "verdict": "not in the atlas (< 2 CPM pooled)"})
            continue
        i = gi[s]
        r = rs.loc[s]
        rec = {"gene": s, "function_class": r["function_class"],
               "dmso_cpm_min_candidate_lines": r["dmso_cpm_min_candidate_lines"],
               "dmso_cpm_median_candidate_lines": r["dmso_cpm_median_candidate_lines"],
               "dmso_cpm_lowest_line": r["dmso_cpm_lowest_line"],
               "instability_log2": r["instability_log2"], "rank_all_screened": int(r["rank_all_screened"]),
               "n_screened": C, "raw_rms_adj_log2": r["raw_rms_adj_log2"],
               "corrected_rms_adj_log2": r["corrected_rms_adj_log2"],
               "raw_worst_median_shift_log2": r["raw_worst_median_shift_log2"],
               "raw_worst_condition": r["raw_worst_condition"],
               "corrected_worst_median_shift_log2": r["corrected_worst_median_shift_log2"],
               "corrected_worst_condition": r["corrected_worst_condition"],
               "geNorm_M": gen_i.loc[s, "geNorm_M_mean_over_candidate_lines"] if s in gen_i.index else np.nan,
               "geNorm_rank_in_pool": int(gen_i.loc[s, "geNorm_rank"]) if s in gen_i.index else np.nan,
               "geNorm_pool_size": len(gen),
               "tp53_wt_minus_altered_max_abs_log2": r["tp53_wt_minus_altered_max_abs_log2"],
               "alltahoe_pct_drugdoses_sig": r["alltahoe_pct_drugdoses_sig"],
               "pooled_target_drugdoses_sig_of15": int(r["pooled_target_drugdoses_sig_of15"]),
               "fischer2017_detail": r["fischer2017_detail"], "hgnc_named_pseudogenes": r["hgnc_named_pseudogenes"],
               "readthrough_exposure": r["readthrough_exposure"]}
        moves = {"p53arm": [], "stressarm": []}
        for k in prim:
            rv_ = np.nanmedian(raw[k, ci, i])
            cv_ = np.nanmedian(corr[k, ci, i])
            rec[f"raw_log2_{cond_names[k]}"] = rv_
            rec[f"corrected_log2_{cond_names[k]}"] = cv_
            if abs(rv_) >= MAX_SHIFT or abs(cv_) >= MAX_SHIFT:
                moves["p53arm" if is_a[k] else "stressarm"].append(
                    f"{cond_names[k]} ({rv_:+.2f} raw / {cv_:+.2f} corr)")
        cv_ = np.nanmedian(corr[K, ci, i])
        rec["corrected_log2_DMSO_vs_drug_median"] = cv_
        if abs(cv_) >= MAX_SHIFT:
            moves["p53arm"].append(f"DMSO vs drug median ({cv_:+.2f} corr)")
        for lab in ("p53arm", "stressarm"):
            rec[f"{lab}_worst_median_shift_log2"] = r[f"{lab}_worst_median_shift_log2"]
            rec[f"{lab}_worst_condition"] = r[f"{lab}_worst_condition"]
            rec[f"{lab}_conditions_moving_ge_0.3_log2"] = "; ".join(moves[lab])
        if r["dmso_cpm_min_candidate_lines"] < MIN_DMSO_CPM:
            lvl = f"low in Tahoe (min {r['dmso_cpm_min_candidate_lines']:.0f} CPM)"
        else:
            lvl = f">= {r['dmso_cpm_min_candidate_lines']:.0f} CPM"

        def say(lab, name):
            m = moves[lab]
            if not m:
                return f"{name}: stable"
            return f"{name}: moves under " + ", ".join(x.split(" (")[0] for x in m)
        verdict = say("p53arm", "p53 arm") + "; " + say("stressarm", "stress arm")
        rec["verdict"] = verdict
        rec["why"] = (f"{lvl}; instability {r['instability_log2']:.3f} log2 (rank {int(r['rank_all_screened'])} of {C} "
                      f"screened); worst p53-arm shift {r['p53arm_worst_median_shift_log2']:+.2f} "
                      f"({r['p53arm_worst_condition']}), worst stress-arm shift "
                      f"{r['stressarm_worst_median_shift_log2']:+.2f} ({r['stressarm_worst_condition']}); "
                      + ("filters: " + r["exclusion_reasons"] if r["exclusion_reasons"] else "passes every filter"))
        cl.append(rec)
    cl = pd.DataFrame(cl)
    lead = ["gene", "verdict", "why"]
    cl = cl[lead + [c for c in cl.columns if c not in lead]]
    cl.to_csv(os.path.join(S.out, "classic_references.csv"), index=False, float_format="%.4g")

    # ---------------------------------------------------------------- small tables
    cl_ = pd.DataFrame({"cell_line_id": S.cand, "cell_line": [S.lname[c] for c in S.cand],
                        "tp53_group": [S.status["tp53_group"].get(c) for c in S.cand],
                        "tp53_changes": [S.status["tp53_changes"].get(c) for c in S.cand],
                        "p53_responsiveness_log2": [S.status["p53_responsiveness_log2"].get(c) for c in S.cand],
                        "functional_call": [S.status["functional_call"].get(c) for c in S.cand],
                        "why": [S.why_line[c] for c in S.cand]})
    cl_.to_csv(os.path.join(S.out, "candidate_lines.csv"), index=False, float_format="%.4g")
    co = cond.drop(columns=["dd_row"]).copy()
    co["why"] = np.where(co["primary"], "primary: in the stability score",
                         "0.05 uM: reported in reference_by_condition.csv, not scored")
    co = pd.concat([co, pd.DataFrame([{"condition": "DMSO (vs plate drug-well median)", "drug": "DMSO_TF",
                                       "drug_short": "DMSO", "primary": True, "plates": ",".join(S.plates),
                                       "n_wells": int(S.dmso_w.sum()),
                                       "why": "control: corrected frame only (the raw frame is referenced to DMSO)"}])],
                   ignore_index=True)
    co.to_csv(os.path.join(S.out, "conditions.csv"), index=False, float_format="%.4g")
    validation["why"] = ("well-level median of this script's per-line corrected values vs the atlas W1 (same steps; "
                         "differences ~1e-6 are float32 rounding)")
    validation.to_csv(os.path.join(S.out, "validation.csv"), index=False, float_format="%.4g")
    p53_long.to_csv(os.path.join(S.cache, "tp53_wt_vs_altered_all_genes.csv.gz"), index=False, float_format="%.4g")
    info = {"data": S.data, "candidate_lines": [S.lname[c] for c in S.cand], "plates": S.plates,
            "n_genes_screened": int(C), "n_eligible": int(el.sum()), "picked": [sym[i] for i in picked],
            "rules": {"preselect_cpm_all_wells": PRESELECT_CPM, "min_dmso_cpm": MIN_DMSO_CPM,
                      "max_median_shift_log2": MAX_SHIFT, "p53_diff_log2": P53_DIFF,
                      "fischer_direct": FISCHER_DIRECT, "fischer_expr": FISCHER_EXPR, "min_cells": A.MIN_CELLS},
            "validation_max_abs_diff_W1": float(validation["max_abs_diff_W1_vs_atlas"].max()),
            "validation_wells_finite_mismatch": int(validation["wells_finite_mismatch"].sum()),
            "seconds": round(time.time() - t0, 1)}
    with open(os.path.join(S.out, "run_info.json"), "w", encoding="utf-8") as fh:
        json.dump(info, fh, indent=1)
    log(json.dumps(info))


# ============================================================================= main
def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--data", default=DATA)
    ap.add_argument("--out", default=HERE)
    ap.add_argument("--steps", default="extract,screen")
    a = ap.parse_args()
    steps = [s.strip() for s in a.steps.split(",") if s.strip()]
    S = Setup(os.path.abspath(os.path.expanduser(a.data)), os.path.abspath(a.out))
    if "extract" in steps:
        step_extract(S)
    if "screen" in steps:
        step_screen(S)


if __name__ == "__main__":
    main()
