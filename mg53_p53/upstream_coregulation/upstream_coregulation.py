#!/usr/bin/env python3
"""MG53 (TRIM72) in Tahoe-100M: co-regulation, candidate upstream regulators, and a readthrough check of the locus.

    python3 mg53_p53/upstream_coregulation/upstream_coregulation.py     # every step (prep ~20 min once, then ~10 min)
    python3 .../upstream_coregulation.py --steps a,b                    # steps: fetch, prep, a, b, c (comma list;
                                                                        # c = c_dog, c_locus, c_genome_in_wells)
Steps (all outputs in tables/; every number is computed here, nothing is typed in by hand)
  fetch  Downloads (cached in external/): Lambert et al. 2018 human TF list (humantfs.ccbr.utoronto.ca v1.01,
         DatabaseExtract 'Is TF?' == Yes), HGNC complete set (gene groups, cytobands), Ensembl GRCh38 gene coordinates
         (BioMart) and the TRIM72 +-200 kb region (Ensembl REST overlap). Nothing else is downloaded.
  prep   One read-only pass over <data>/atlas/pseudobulk/groupNNN.npy (mmap, row chunks; sample ->
         plate from atlas/sample_map.csv; split (sample, line) rows summed) that writes cache/: per plate x line
         summed counts of every gene over 'quiet' wells (DMSO + drug wells of drug-doses with < 1000 significant
         genes, failed wells out) and over the DMSO wells; per (well, line) counts of the +-1 Mb locus genes and a
         muscle / p53 list; full profiles of the TRIM72-raising 5 uM wells (and idarubicin 0.05 / 0.5 uM).
  a      Genome-wide co-regulation across drug-doses (atlas DD_z, method v3; 1,086 drug-doses, unreliable-plate-only
         and position-not-correctable ones left out): raw, covariate-partialled (cell loss, UMI, genes/cell,
         composition, S/G2M/proteasome z, n significant genes, RMS z) and top-1/3/10-PC-removed correlations with
         TRIM72; drug-block permutation null (whole drugs swapped, 1000x) -> BH q; 300 expression-matched random
         genes as a second null; robustness within plate groups and without the 10 strongest TRIM72 drug-doses;
         readthrough pairs (every DoG-exposed gene vs its upstream same-strand gene, vs level-matched random genes);
         gene-set tests (p53 targets, stress programs, muscle TFs / structural genes, AP-1) vs level-matched sets.
         a_coreg_genomewide.csv (all genes), a_top_partners.csv, a_regulator_partners_TF_signalling.csv,
         a_null_summary.csv, a_pc_variance.csv, a_robustness_summary.csv, a_upstream_pair_coregulation.csv,
         a_upstream_pair_summary.csv, a_gene_set_tests.csv, a_TRIM72_by_drugdose_global_removed.csv.
  b      Untreated (baseline) covariation across the 50 lines: per plate (13 reliable plates) Spearman over lines of
         TRIM72 vs every gene with >= 200 counts (quiet wells pooled per plate), median over plates, line-permutation
         null (2000x, same permutation on every plate) -> BH q; organ-adjusted and DMSO-only versions; percentile
         among genes of the same level; DoG-exposure of the partners; readthrough pairs at baseline; plate batch
         (plates 1-3,14 vs 4-12) genome-wide and by DoG class; TP53 status / p53 activity / organ tests.
         b_baseline_coexpression_genomewide.csv, b_baseline_focus_genes.csv, b_gene_set_tests.csv,
         b_TRIM72_baseline_per_line.csv, b_TRIM72_baseline_tests.csv, b_upstream_pair_baseline.csv,
         b_plate_batch_gap_genomewide.csv.
  c      Locus / readthrough check. c_dog: every atlas gene classed by readthrough exposure (sense_exposed = an
         expressed (>= 5 CPM) same-strand gene ends <= 20 kb upstream and is >= 8x its level; unexposed = none within
         100 kb on either strand), a DoG index per drug-dose, TRIM72's rank among DoG-exposed genes per raiser
         (c_DoG_gene_exposure_classes.csv, c_DoG_index_by_drugdose.csv, c_DoG_tests.csv, c_DoG_raisers_TRIM72_rank.csv).
         c_locus: chr16p11.2 genes within 200 kb (Ensembl) with corrected effects (the atlas's per_line_columns
         steps re-implemented on the cached counts; checked against the atlas in c_validation_locus_vs_atlas.csv)
         under idarubicin and the other raisers, untreated plate batch per gene, correlation with TRIM72 across
         drug-doses, per line in both idarubicin 5 uM wells (c_locus_neighbours_effects*.csv,
         c_idarubicin5_per_line_locus.csv, c_idarubicin5_locus_tests.csv). c_genome_in_wells: line-matched observed /
         expected counts of every gene in the raiser wells, reads added per locus gene, strand summary, and which
         genes' per-line gains track TRIM72's (c_locus_obs_over_exp_raiser_wells.csv,
         c_raiser_wells_genomewide_OE_summary.csv, c_locus_strand_summary_raiser_wells.csv,
         c_per_line_gain_corr_with_TRIM72_genomewide.csv).

All associations; there is no MG53 perturbation in Tahoe. Nothing is written outside $MG53_OUT (default this folder); the data folder
is read only.
"""
import argparse
import json
import os
import subprocess
import sys
import time

import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, REPO)
DATA = os.environ.get("MG53_DATA") or os.environ.get("TAHOE_DATA") or os.path.expanduser("~/Tahoe-100M")   # the Tahoe-100M folder with atlas/ and gene_panel/
FXD = os.path.join(DATA, "atlas", "effects")
PB = os.path.join(DATA, "atlas", "pseudobulk")
OUTDIR = os.environ.get("MG53_OUT") or HERE      # tables/ (and cache/, external/) go here; run_mg53_p53.py sets it
EXT = os.path.join(OUTDIR, "external")
CACHE = os.path.join(OUTDIR, "cache")
TAB = os.path.join(OUTDIR, "tables")
SEED = 7

TRIM72_REGION = ("16", 31214017, 31231537)       # GRCh38, + strand (Ensembl ENSG00000177238)
MUSCLE_TFS = ["MYOD1", "MYOG", "MYF5", "MYF6", "MEF2A", "MEF2B", "MEF2C", "MEF2D", "SRF", "MYOCD", "TEAD1",
              "TEAD4", "SIX1", "SIX4", "PAX3", "PAX7", "NFATC1", "PPARGC1A", "TCF12", "TCF3", "TCF4", "HDAC4",
              "HDAC5", "HDAC9", "CDKN1C", "DES", "MYH3", "CKM", "ACTA1", "TNNT1", "TNNT2", "CAV3", "DYSF",
              "RYR1", "ATP2A1", "MSTN", "IGF1", "AKT1", "PIK3CA", "PRKAA1", "FOXO1", "FOXO3", "MYC"]
# 5 uM wells of the TRIM72 raisers (README of trim72_idarubicin) + panobinostat / harringtonine, and idarubicin's
# lower doses; full profiles are kept for these (all genes)
RAISERS = {"smp_2010": "Idarubicin 5 (plate6)", "smp_2778": "Idarubicin 5 (plate14)",
           "smp_1914": "Idarubicin 0.5 (plate5)", "smp_1818": "Idarubicin 0.05 (plate4)",
           "smp_2047": "Homoharringtonine 5 (plate6)", "smp_2815": "Homoharringtonine 5 (plate14)",
           "smp_2297": "Harringtonine 5 (plate9)", "smp_2580": "Auranofin 5 (plate12)",
           "smp_2277": "Dinaciclib 5 (plate9)", "smp_2298": "Epirubicin 5 (plate9)",
           "smp_2337": "Doxorubicin 5 (plate9)", "smp_2285": "Topotecan 5 (plate9)",
           "smp_2030": "Mitoxantrone 5 (plate6)", "smp_2798": "Mitoxantrone 5 (plate14)",
           "smp_2642": "Panobinostat 5 (plate12)"}


def log(*a):
    print(time.strftime("%H:%M:%S"), *a, flush=True)


def bh(p):
    p = np.asarray(p, dtype=float)
    q = np.full_like(p, np.nan)
    ok = np.isfinite(p)
    pv = p[ok]
    n = pv.size
    if n == 0:
        return q
    o = np.argsort(pv)
    r = pv[o] * n / np.arange(1, n + 1)
    r = np.minimum.accumulate(r[::-1])[::-1]
    out = np.empty(n)
    out[o] = np.minimum(r, 1)
    q[ok] = out
    return q


def ensure_dir(*p):
    for x in p:
        os.makedirs(x, exist_ok=True)


# ============================================================================= fetch
def curl(url, dest, get_query=None, timeout=300, tries=5):
    """Download to dest via a temporary file. HTTP errors fail (curl -f) and are retried; an HTML page (a service
    error such as Ensembl's '503 Service Unavailable') is never saved as data."""
    tmp = dest + ".part"
    cmd = ["curl", "-sSfL", "-m", str(timeout), "-o", tmp]
    if get_query is not None:
        cmd += ["-G", "--data-urlencode", "query=" + get_query]
    cmd.append(url)
    err = ""
    for k in range(tries):
        r = subprocess.run(cmd, capture_output=True, text=True)
        if r.returncode == 0:
            with open(tmp, "rb") as fh:
                head = fh.read(512).lower()
            if b"<html" not in head and b"<!doctype html" not in head and b"service unavailable" not in head:
                os.replace(tmp, dest)
                return True
            err = "the server returned an HTML page instead of data"
        else:
            err = (r.stderr or "").strip()[-200:]
        log(f"  download failed ({err}); retry {k + 1}/{tries - 1}" if k + 1 < tries else f"  download failed ({err})")
        time.sleep(min(60, 10 * (k + 1)))
    if os.path.exists(tmp):
        os.remove(tmp)
    return False


def step_fetch():
    ensure_dir(EXT)
    files = {
        "lambert_DatabaseExtract_v_1.01.csv":
            "http://humantfs.ccbr.utoronto.ca/download/v_1.01/DatabaseExtract_v_1.01.csv",
        "hgnc_complete_set.txt":
            "https://storage.googleapis.com/public-download-files/hgnc/tsv/tsv/hgnc_complete_set.txt",
        "ensembl_trim72_region.json":
            "https://rest.ensembl.org/overlap/region/human/16:31014017-31431537?feature=gene;"
            "content-type=application/json",
    }
    for f, url in files.items():
        p = os.path.join(EXT, f)
        if not os.path.exists(p) or os.path.getsize(p) < 1000:
            log("download", url)
            if not curl(url, p) and f != "ensembl_trim72_region.json":   # the region falls back on BioMart
                raise SystemExit(f"could not download {url}; rerun the step later (finished files are kept)")
    p = os.path.join(EXT, "ensembl_biomart_genes_GRCh38.tsv")
    if not os.path.exists(p) or os.path.getsize(p) < 100000:
        q = ('<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE Query><Query virtualSchemaName="default" '
             'formatter="TSV" header="1" uniqueRows="1" datasetConfigVersion="0.6"><Dataset '
             'name="hsapiens_gene_ensembl" interface="default"><Attribute name="ensembl_gene_id"/><Attribute '
             'name="external_gene_name"/><Attribute name="chromosome_name"/><Attribute name="start_position"/>'
             '<Attribute name="end_position"/><Attribute name="strand"/><Attribute name="gene_biotype"/>'
             '</Dataset></Query>')
        log("download Ensembl BioMart gene coordinates")
        if not curl("https://www.ensembl.org/biomart/martservice", p, get_query=q):
            raise SystemExit("could not download the Ensembl BioMart gene coordinates; rerun the step later")
    log("fetch done")


def load_coords():
    b = pd.read_csv(os.path.join(EXT, "ensembl_biomart_genes_GRCh38.tsv"), sep="\t", dtype={"Chromosome/scaffold name": str})
    b.columns = ["ensembl_id", "ens_name", "chrom", "start", "end", "strand", "biotype"]
    prim = [str(i) for i in range(1, 23)] + ["X", "Y"]
    return b[b["chrom"].isin(prim)].drop_duplicates("ensembl_id").reset_index(drop=True)


def gene_meta():
    gm = pd.read_parquet(os.path.join(DATA, "metadata", "gene_metadata.parquet"))
    return gm


# ============================================================================= prep (one pass over the pseudobulk)
def load_profiles():
    import glob
    parts = []
    for m in sorted(glob.glob(os.path.join(PB, "group*_profiles.csv"))):
        t = pd.read_csv(m, dtype={"sample": str, "cell_line_id": str})
        t["file"] = m.replace("_profiles.csv", ".npy")
        parts.append(t)
    return pd.concat(parts, ignore_index=True)


def selected_tokens():
    """Tokens of the genes kept per (well, line): every gene within 1 Mb of TRIM72 plus muscle / p53 context."""
    gm = gene_meta()
    co = load_coords()
    c, s, e = TRIM72_REGION
    loc = co[(co["chrom"] == c) & (co["end"] >= s - 1_000_000) & (co["start"] <= e + 1_000_000)]
    m = gm.merge(loc[["ensembl_id"]], on="ensembl_id")
    extra = gm[gm["gene_symbol"].isin(MUSCLE_TFS + ["TP53", "MDM2", "CDKN1A", "FUS", "ACTB", "GAPDH"])]
    tok = sorted(set(m["token_id"].astype(int)) | set(extra["token_id"].astype(int)))
    return np.array(tok, dtype=np.int64)


def step_prep():
    ensure_dir(CACHE)
    out = os.path.join(CACHE, "prep_done.json")
    if os.path.exists(out):
        log("prep: cache present (delete cache/ to redo)")
        return
    lines = pd.read_csv(os.path.join(FXD, "lines.csv"), dtype={"cell_line_id": str})["cell_line_id"].tolist()
    plates = pd.read_csv(os.path.join(FXD, "plates.csv"))["plate"].tolist()
    sm = pd.read_csv(os.path.join(DATA, "atlas", "sample_map.csv"), dtype={"sample": str})
    wells = pd.read_csv(os.path.join(FXD, "wells.csv"), dtype={"sample": str})
    dd = pd.read_csv(os.path.join(FXD, "drugdose.csv"))
    failed = set(pd.read_csv(os.path.join(FXD, "failed_wells.csv"), dtype={"sample": str})["sample"])
    nsig = wells["drugdose_row"].map(lambda r: dd["n_sig_genes"].iloc[int(r)] if r >= 0 else np.nan)
    quiet = set(wells.loc[wells["is_dmso"].astype(bool) | (nsig < 1000), "sample"]) - failed
    dmso = set(sm.loc[sm["is_dmso"].astype(bool), "sample"]) - failed
    plate_of = dict(zip(sm["sample"], sm["plate"]))
    prof = load_profiles()
    prof = prof[prof["cell_line_id"].isin(lines)].copy()
    prof["plate"] = prof["sample"].map(plate_of)
    pi = {p: i for i, p in enumerate(plates)}
    li = {l: i for i, l in enumerate(lines)}
    prof["pi"] = prof["plate"].map(pi)
    prof["li"] = prof["cell_line_id"].map(li)
    toks = selected_tokens()
    G = int(np.load(prof["file"].iloc[0], mmap_mode="r").shape[1])
    P, L = len(plates), len(lines)
    acc_q = np.zeros((P * L, G))
    acc_d = np.zeros((P * L, G))
    tot_q = np.zeros(P * L)
    tot_d = np.zeros(P * L)
    cells_q = np.zeros(P * L)
    rw = list(RAISERS)
    full = np.zeros((len(rw) * L, G))
    full_tot = np.zeros(len(rw) * L)
    full_cells = np.zeros(len(rw) * L)
    sel_rows = []
    for f, g in prof.groupby("file"):
        log("reading", os.path.basename(f), len(g), "profiles")
        g = g.sort_values("row")
        arr = np.load(f, mmap_mode="r")
        rows = g["row"].to_numpy()
        for s0 in range(0, len(rows), 400):
            gg = g.iloc[s0:s0 + 400]
            sub = np.asarray(arr[gg["row"].to_numpy()], dtype=np.float64)
            k = (gg["pi"].to_numpy() * L + gg["li"].to_numpy())
            isq = gg["sample"].isin(quiet).to_numpy()
            isd = gg["sample"].isin(dmso).to_numpy()
            if isq.any():
                np.add.at(acc_q, k[isq], sub[isq])
                np.add.at(tot_q, k[isq], gg["total_counts"].to_numpy()[isq])
                np.add.at(cells_q, k[isq], gg["n_cells"].to_numpy()[isq])
            if isd.any():
                np.add.at(acc_d, k[isd], sub[isd])
                np.add.at(tot_d, k[isd], gg["total_counts"].to_numpy()[isd])
            isr = gg["sample"].isin(RAISERS).to_numpy()
            if isr.any():
                kr = np.array([rw.index(s) for s in gg["sample"].to_numpy()[isr]]) * L + gg["li"].to_numpy()[isr]
                np.add.at(full, kr, sub[isr])
                np.add.at(full_tot, kr, gg["total_counts"].to_numpy()[isr])
                np.add.at(full_cells, kr, gg["n_cells"].to_numpy()[isr])
            t = pd.DataFrame(sub[:, toks].astype(np.float32), columns=[str(x) for x in toks])
            t.insert(0, "sample", gg["sample"].to_numpy())
            t.insert(1, "cell_line_id", gg["cell_line_id"].to_numpy())
            t.insert(2, "n_cells", gg["n_cells"].to_numpy())
            t.insert(3, "total_counts", gg["total_counts"].to_numpy())
            sel_rows.append(t)
            del sub
    sel = pd.concat(sel_rows, ignore_index=True)
    # split profiles of one (sample, line) across group files: sum them
    sel = sel.groupby(["sample", "cell_line_id"], as_index=False).sum(numeric_only=True)
    sel.to_parquet(os.path.join(CACHE, "selected_genes_per_well_line.parquet"), index=False)
    np.savez_compressed(os.path.join(CACHE, "plate_line_quiet.npz"), counts=acc_q.reshape(P, L, G).astype(np.float32),
                        total=tot_q.reshape(P, L), cells=cells_q.reshape(P, L))
    np.savez_compressed(os.path.join(CACHE, "plate_line_dmso.npz"), counts=acc_d.reshape(P, L, G).astype(np.float32),
                        total=tot_d.reshape(P, L))
    np.savez_compressed(os.path.join(CACHE, "raiser_wells_full.npz"),
                        counts=full.reshape(len(rw), L, G).astype(np.float32), total=full_tot.reshape(len(rw), L),
                        cells=full_cells.reshape(len(rw), L), samples=np.array(rw))
    with open(out, "w") as fh:
        json.dump({"plates": plates, "lines": lines, "tokens_selected": [int(x) for x in toks],
                   "n_quiet_wells": len(quiet), "n_dmso_wells": len(dmso), "raiser_wells": RAISERS,
                   "quiet_rule": "DMSO + drug wells whose drug-dose has n_sig_genes < 1000; failed wells out"}, fh,
                  indent=1)
    log("prep done")


# ============================================================================= annotation
SIGNAL_RULES = [   # (category, regex on HGNC gene_group, regex of groups to exclude)
    ("protein kinase", r"kinase", r"anchoring|guanylate kinase|Carbohydrate kinases|phosphatase|Nucleoside|"
                                  r"inhibitor|regulatory subunit"),
    ("phosphatase", r"phosphatase", r"HAD Asp-based|Acid phosphatases|Alkaline"),
    ("small GTPase / GAP / GEF", r"GTPase|guanine nucleotide exchange|Rho guanine", r"Translational GTPases"),
    ("receptor (non-olfactory)", r"receptor", r"Olfactory|Vomeronasal|T cell receptor|Receptor ligands|Taste"),
    ("E3 ligase / ubiquitin", r"E3 ubiquitin|ubiquitin|Ring finger|Tripartite motif", r"$^"),
    ("cytokine / growth factor", r"Interleukin|Chemokine|growth factor|cytokine|Receptor ligands", r"receptor$|receptors"),
]


def annotation():
    """symbol -> is_TF (Lambert 2018), TF_family (DBD), HGNC groups, signalling category, panel / p53 sets."""
    import re
    import tahoe_gene_panel as P
    lam = pd.read_csv(os.path.join(EXT, "lambert_DatabaseExtract_v_1.01.csv"))
    lam = lam[lam["Is TF?"].astype(str).str.strip().eq("Yes")]
    tf = dict(zip(lam["HGNC symbol"].astype(str), lam["DBD"].astype(str)))
    h = pd.read_csv(os.path.join(EXT, "hgnc_complete_set.txt"), sep="\t", low_memory=False,
                    usecols=["symbol", "gene_group", "location", "ensembl_gene_id"])
    grp_sym = dict(zip(h["symbol"], h["gene_group"].fillna("")))
    grp_ens = dict(zip(h["ensembl_gene_id"].fillna(""), h["gene_group"].fillna("")))
    band_sym = dict(zip(h["symbol"], h["location"].fillna("")))

    def cats(groups):
        out = []
        for name, inc, exc in SIGNAL_RULES:
            for gname in str(groups).split("|"):
                if gname and re.search(inc, gname, re.I) and not re.search(exc, gname, re.I):
                    out.append(name)
                    break
        return "; ".join(out)

    sets = {"P53_ACTIVITY": set(P.P53_ACTIVITY)}
    sets.update({k: set(v) for k, v in P.CONTEXT.items()})
    return tf, grp_sym, grp_ens, band_sym, cats, sets


def annotate(df, sym_col="gene", ens_col=None):
    tf, grp_sym, grp_ens, band_sym, cats, sets = annotation()
    s = df[sym_col].astype(str)
    df["is_TF_Lambert2018"] = s.isin(tf)
    df["TF_DBD_family"] = s.map(tf).fillna("")
    groups = s.map(grp_sym)
    if ens_col is not None:
        groups = groups.fillna(df[ens_col].map(grp_ens))
    df["HGNC_gene_groups"] = groups.fillna("")
    df["signalling_category"] = df["HGNC_gene_groups"].map(cats)
    df["cytoband"] = s.map(band_sym).fillna("")
    df["gene_sets"] = s.map(lambda x: "; ".join(k for k, v in sets.items() if x in v))
    return df


SETS_EXTRA = {
    "MUSCLE_TF": ["MYOD1", "MYOG", "MYF5", "MYF6", "MEF2A", "MEF2B", "MEF2C", "MEF2D", "SRF", "MYOCD"],
    "MUSCLE_STRUCTURAL": ["ACTA1", "CKM", "MYH3", "DES", "TNNT1", "TNNT2", "CAV3", "RYR1", "ATP2A1", "DYSF", "MYL11",
                          "MSTN"],
    "AP1_IEG": ["FOS", "FOSB", "JUN", "JUNB", "EGR1", "EGR2", "EGR3", "ATF3", "IER2", "NR4A1"]}


def gene_set_tests(stat, sym, lvl, rng, label, B=2000):
    """Mean of `stat` over each gene set's members vs B random sets in which every member is replaced by a random
    gene of its level (within 2x; nearest levels when fewer). Returns rows (set, n, mean, null mean/sd, z, p)."""
    import tahoe_gene_panel as Pn
    sets = {"P53_ACTIVITY": list(Pn.P53_ACTIVITY)}
    sets.update({k: list(v) for k, v in Pn.CONTEXT.items()})
    sets.update(SETS_EXTRA)
    sym = np.asarray(sym).astype(str)
    stat = np.asarray(stat, dtype=float)
    ok = np.isfinite(stat)
    rows = []
    for nm, members in sets.items():
        idx = [int(np.flatnonzero(sym == g)[0]) for g in members if (sym == g).any() and ok[sym == g][0]]
        if len(idx) < 3:
            continue
        allowed = ok & ~np.isin(np.arange(len(sym)), idx)
        draws = np.stack([rng.choice(level_pool(lvl, i, allowed), size=B, replace=True) for i in idx],
                         axis=1)                                                         # B x members
        null = stat[draws].mean(axis=1)
        obs = float(stat[idx].mean())
        rows.append({"statistic": label, "gene_set": nm, "n_genes": len(idx),
                     "genes": ", ".join(f"{sym[i]} {stat[i]:+.2f}" for i in idx), "mean_stat": obs,
                     "null_mean": float(null.mean()), "null_sd": float(null.std()),
                     "z_vs_level_matched": (obs - null.mean()) / null.std(),
                     "p_two_sided_empirical": (1 + int((np.abs(null - null.mean()) >= abs(obs - null.mean())).sum()))
                     / (B + 1)})
    return rows


def level_pool(lvl, i, allowed, k=20):
    """Genes (indices) among `allowed` whose level is within 2x of gene i's; when fewer than k such genes exist
    (very highly expressed genes), the k genes of the nearest level."""
    a = np.flatnonzero(allowed)
    d = np.abs(np.log2(np.maximum(lvl[a], 1e-6)) - np.log2(max(lvl[i], 1e-6)))
    c = a[d <= 1]
    if c.size < k:
        c = a[np.argsort(d)[:k]]
    return c


def level_matched(lvl, i, allowed, k, rng):
    """k random genes of gene i's level (level_pool), without replacement."""
    return rng.choice(level_pool(lvl, i, allowed, k), size=k, replace=False)


# ============================================================================= (a) genome-wide co-regulation
def colcorr(y, X):
    """Pearson r of vector y with every column of X (columns centred here)."""
    y = y - y.mean()
    Xc = X - X.mean(axis=0)
    num = y @ Xc
    den = np.sqrt((y @ y) * (Xc * Xc).sum(axis=0))
    return num / np.where(den > 0, den, np.nan)


def standardise(X):
    Xc = X - X.mean(axis=0)
    sd = Xc.std(axis=0)
    sd[sd == 0] = 1
    return Xc / sd


def drug_block_perms(dd, B, rng):
    """B permutations of the drug-dose rows that move whole drugs: a drug's doses go together to another drug with
    the same set of doses (keeps the dose structure; drug-doses of one drug are not independent)."""
    sig = dd.groupby("drug")["conc"].apply(lambda s: tuple(sorted(s.round(3))))
    rows_of = {d: dd.index[dd["drug"] == d].to_numpy() for d in sig.index}
    conc_of = dd["conc"].round(3).to_dict()
    pos = {i: k for k, i in enumerate(dd.index)}
    perms = np.empty((B, len(dd)), dtype=np.int64)
    groups = {}
    for d, s in sig.items():
        groups.setdefault(s, []).append(d)
    for b in range(B):
        p = np.arange(len(dd))
        for s, drugs in groups.items():
            if len(drugs) < 2:
                continue
            shuf = rng.permutation(drugs)
            for src, dst in zip(drugs, shuf):        # rows of drug src get the values of drug dst
                for i in rows_of[src]:
                    j = next(j for j in rows_of[dst] if conc_of[j] == conc_of[i])
                    p[pos[i]] = pos[j]
        perms[b] = p
    return perms


def step_a(B=1000, n_random=300):
    log("(a) genome-wide co-regulation across drug-doses")
    rng = np.random.default_rng(SEED)
    genes = pd.read_csv(os.path.join(FXD, "genes.csv"))
    dd = pd.read_csv(os.path.join(FXD, "drugdose.csv"))
    for c in ("unreliable_plate_only", "position_not_correctable"):
        dd[c] = dd[c].astype(str).str.lower().eq("true")
    keep = ~(dd["unreliable_plate_only"] | dd["position_not_correctable"])
    gi = np.flatnonzero((genes["kind"] == "gene").to_numpy())
    gsym = genes["symbol"].astype(str).to_numpy()[gi]
    t = int(np.flatnonzero(gsym == "TRIM72")[0])
    ddk = dd[keep].reset_index(drop=True)
    Z = np.asarray(np.load(os.path.join(FXD, "DD_z.npy"), mmap_mode="r"))[keep.to_numpy()][:, gi].astype(np.float64)
    Lf = np.asarray(np.load(os.path.join(FXD, "DD_lfc.npy"), mmap_mode="r"))[keep.to_numpy()][:, gi].astype(np.float64)
    Z = np.nan_to_num(Z)
    Lf = np.nan_to_num(Lf)
    n = Z.shape[0]
    log(f"  {n} drug-doses (left out: {int((~keep).sum())} unreliable-plate-only / position not correctable), "
        f"{len(gi)} genes")
    # covariates of global activity
    cov = pd.DataFrame({
        "log_n_sig": np.log1p(ddk["n_sig_genes"].fillna(0)),
        "cells": ddk["cells_log2_vs_plate"].fillna(0), "umi": ddk["umi_per_cell_log2_vs_plate"].fillna(0),
        "genes_pc": ddk["genes_per_cell_log2_vs_plate"].fillna(0), "comp": ddk["composition_shift_log2"].fillna(0),
        "S": ddk["S_PHASE_z"].fillna(0), "G2M": ddk["G2M_PHASE_z"].fillna(0),
        "PROT": ddk["PROTEASOME_z"].fillna(0), "rms_z": np.sqrt((Z ** 2).mean(axis=1))})
    C = np.column_stack([np.ones(n), cov.to_numpy()])
    variants = {}
    Zs = standardise(Z)
    variants["raw"] = Zs
    variants["covariates"] = standardise(Zs - C @ np.linalg.lstsq(C, Zs, rcond=None)[0])
    U, S, Vt = np.linalg.svd(Zs, full_matrices=False)
    var_expl = S ** 2 / (S ** 2).sum()
    pcs = pd.DataFrame({"pc": np.arange(1, 21), "variance_explained": var_expl[:20],
                        "TRIM72_loading_r": [np.corrcoef(U[:, k], Zs[:, t])[0, 1] for k in range(20)],
                        "r_with_log_n_sig_genes": [np.corrcoef(U[:, k], cov["log_n_sig"])[0, 1] for k in range(20)],
                        "r_with_rms_z": [np.corrcoef(U[:, k], cov["rms_z"])[0, 1] for k in range(20)],
                        "r_with_cells_log2": [np.corrcoef(U[:, k], cov["cells"])[0, 1] for k in range(20)],
                        "r_with_S_PHASE_z": [np.corrcoef(U[:, k], cov["S"])[0, 1] for k in range(20)],
                        "top_drugdoses_pos": ["; ".join(f"{ddk.drug[i]} {ddk.conc[i]:g}" for i in np.argsort(-U[:, k])[:4])
                                              for k in range(20)],
                        "top_drugdoses_neg": ["; ".join(f"{ddk.drug[i]} {ddk.conc[i]:g}" for i in np.argsort(U[:, k])[:4])
                                              for k in range(20)]})
    pcs.to_csv(os.path.join(TAB, "a_pc_variance.csv"), index=False)
    for k in (1, 3, 10):
        variants[f"minus_{k}pc"] = standardise(Zs - (U[:, :k] * S[:k]) @ Vt[:k])
    res = pd.DataFrame({"gene": gsym, "atlas_col": gi,
                        "median_line_cpm": genes["median_line_cpm"].to_numpy()[gi],
                        "n_lines_expressing": genes["n_lines_expressing"].to_numpy()[gi]})
    res["r_lfc_raw"] = colcorr(Lf[:, t], Lf)
    from scipy.stats import rankdata
    Zr = rankdata(Z, axis=0)
    res["rho_z_raw_spearman"] = colcorr(Zr[:, t], Zr)
    perms = drug_block_perms(ddk, B, rng)
    # expression-matched random genes: median line CPM within 2x of TRIM72's, expressed in >= 45 lines
    lvl = res["median_line_cpm"].to_numpy()
    cand = np.flatnonzero((lvl >= lvl[t] / 2) & (lvl <= lvl[t] * 2) & (res["n_lines_expressing"] >= 45) &
                          (np.arange(len(gi)) != t))
    rnd = rng.choice(cand, size=min(n_random, cand.size), replace=False)
    # readthrough position class of every gene (c): used to ask whether TRIM72's partners are downstream-of-gene
    ex = dog_exposure(atlas_genes_with_coords())
    ex = ex.set_index("col").reindex(gi)
    dog_cls = ex["class"].fillna("no coordinates").to_numpy()
    sense = dog_cls == "sense_exposed"
    nulls = []
    for name, X in variants.items():
        y = X[:, t]
        r = (y @ X) / n                                   # X columns standardised: r = mean product
        res[f"r_z_{name}"] = r
        # drug-block permutation null
        Yp = y[perms]                                      # B x n
        Rn = (Yp @ X) / n                                  # B x genes
        sd0 = Rn.std(axis=0)
        res[f"null_sd_{name}"] = sd0
        res[f"zperm_{name}"] = r / sd0
        res[f"p_perm_{name}"] = (1 + (np.abs(Rn) >= np.abs(r)[None]).sum(axis=0)) / (B + 1)
        from scipy.stats import norm
        p_norm = 2 * norm.sf(np.abs(r / sd0))
        res[f"p_{name}"] = p_norm                         # permutation-calibrated normal p (finer than 1/(B+1))
        res[f"q_{name}"] = bh(p_norm)
        # random expression-matched genes: where does r(TRIM72, g) sit among r(random gene, g)?
        Rr = (X[:, rnd].T @ X) / n                         # n_random x genes
        Rr[np.arange(len(rnd)), rnd] = np.nan
        res[f"pct_vs_matched_{name}"] = 100 * (np.nanmean(Rr < r[None], axis=0))
        # share of the top-100 positive partners that sit downstream of an expressed same-strand gene
        rt = r.copy()
        rt[t] = -np.inf
        top_t = np.argsort(-rt)[:100]
        frac_t = float(sense[top_t].mean())
        Rr2 = np.nan_to_num(Rr, nan=-np.inf)
        Rr2[:, t] = -np.inf
        frac_r = np.array([sense[np.argsort(-Rr2[i])[:100]].mean() for i in range(len(rnd))])
        rnd_sense = sense[rnd]
        thr = 0.3
        sig_t = int(np.delete(((res[f"q_{name}"] < 0.05) & (np.abs(r) >= thr)).to_numpy(), t).sum())
        cnt_r = (np.abs(Rr) >= thr).sum(axis=1)
        top_r = np.nanmax(Rr, axis=1)
        nulls.append({"variant": name, "TRIM72_n_partners_absr_ge_0.3": int((np.abs(np.delete(r, t)) >= thr).sum()),
                      "matched_genes_median_n_partners_absr_ge_0.3": float(np.median(cnt_r)),
                      "matched_genes_p90_n_partners": float(np.percentile(cnt_r, 90)),
                      "TRIM72_pctile_n_partners": float(100 * np.mean(cnt_r < (np.abs(np.delete(r, t)) >= thr).sum())),
                      "TRIM72_max_r": float(np.max(np.delete(r, t))),
                      "matched_genes_median_max_r": float(np.median(top_r)),
                      "TRIM72_pctile_max_r": float(100 * np.mean(top_r < np.max(np.delete(r, t)))),
                      "TRIM72_n_q_lt_0.05_and_absr_ge_0.3": sig_t, "n_matched_genes": len(rnd),
                      "TRIM72_top100_pct_sense_exposed": 100 * frac_t,
                      "pct_sense_exposed_all_genes": 100 * float(sense.mean()),
                      "matched_genes_top100_pct_sense_exposed_median": 100 * float(np.median(frac_r)),
                      "matched_sense_exposed_genes_top100_pct_sense_exposed_median":
                          100 * float(np.median(frac_r[rnd_sense])) if rnd_sense.any() else np.nan,
                      "matched_unexposed_genes_top100_pct_sense_exposed_median":
                          100 * float(np.median(frac_r[dog_cls[rnd] == "unexposed"])),
                      "n_matched_sense_exposed": int(rnd_sense.sum()),
                      "TRIM72_pctile_top100_sense_vs_matched": float(100 * np.mean(frac_r < frac_t)),
                      "TRIM72_pctile_top100_sense_vs_matched_sense_exposed":
                          float(100 * np.mean(frac_r[rnd_sense] < frac_t)) if rnd_sense.any() else np.nan,
                      "n_drugdoses": n, "n_permutations": B})
        log(f"  {name}: top partners", ", ".join(res.drop(index=t).nlargest(8, f"r_z_{name}")["gene"]))
    # --- robustness: the same correlations within plate groups (TRIM72's untreated level is ~10x lower on plates
    # 4-12 than on 1-3 / 14) and without the 10 drug-doses that raise TRIM72 most
    pl = ddk["plates"].astype(str)
    top10 = np.argsort(-Z[:, t])[:10]
    subsets = {"all": np.ones(n, dtype=bool),
               "plates4to12_only": pl.isin([f"plate{i}" for i in range(4, 13)]).to_numpy(),
               "plates1to3_only": pl.isin(["plate1", "plate2", "plate3"]).to_numpy(),
               "without_top10_TRIM72_drugdoses": ~np.isin(np.arange(n), top10)}
    rob_cols = {}
    rob_sum = []
    for vname in ("raw", "covariates", "minus_3pc"):
        X = variants[vname]
        for sname, m in subsets.items():
            r_s = colcorr(X[m, t], X[m])
            rob_cols[f"r_{vname}_{sname}"] = r_s
            rr = r_s.copy()
            rr[t] = -np.inf
            top = np.argsort(-rr)[:100]
            rob_sum.append({"variant": vname, "subset": sname, "n_drugdoses": int(m.sum()),
                            "top100_pct_sense_exposed": 100 * float(sense[top].mean()),
                            "pct_sense_exposed_all_genes": 100 * float(sense.mean()),
                            "top10_partners": ", ".join(gsym[top[:10]]),
                            "r_FUS": float(r_s[gsym == "FUS"][0]),
                            "rank_FUS": int((rr > r_s[gsym == "FUS"][0]).sum() + 1),
                            "r_ATF3": float(r_s[gsym == "ATF3"][0]), "r_TP53": float(r_s[gsym == "TP53"][0]),
                            "r_PMAIP1": float(r_s[gsym == "PMAIP1"][0])})
    pd.DataFrame(rob_sum).to_csv(os.path.join(TAB, "a_robustness_summary.csv"), index=False, float_format="%.4g")
    log("  robustness:", "; ".join(f"{d['variant']}/{d['subset']}: top100 {d['top100_pct_sense_exposed']:.0f}% DoG, "
                                   f"FUS r {d['r_FUS']:.2f}" for d in rob_sum))
    # --- readthrough pairs: every DoG-exposed gene vs its upstream same-strand expressed gene, against random
    # partners of the upstream gene's level on another chromosome
    pos_of = {int(c): k for k, c in enumerate(gi)}
    upc = ex["up_col"].fillna(-1).astype(int).to_numpy()
    se = np.flatnonzero(sense & np.isin(upc, gi))
    gp = se
    up = np.array([pos_of[c] for c in upc[se]])
    pooled_lvl = genes["pooled_cpm"].to_numpy()[gi]
    chrom = ex["chrom"].astype(str).to_numpy()
    n_rand_pair = 20
    rpart = np.full((len(gp), n_rand_pair), -1)
    for k, (g_, u_) in enumerate(zip(gp, up)):
        rpart[k] = level_matched(pooled_lvl, u_, chrom != chrom[g_], n_rand_pair, rng)
    k_t = int(np.flatnonzero(gp == t)[0])
    c_t = np.flatnonzero((pooled_lvl >= pooled_lvl[up[k_t]] / 2) & (pooled_lvl <= pooled_lvl[up[k_t]] * 2) &
                         (chrom != chrom[t]))
    pair = pd.DataFrame({"gene": gsym[gp], "upstream_gene": gsym[up], "distance_bp": ex["up_dist"].to_numpy()[gp],
                         "gene_pooled_cpm": pooled_lvl[gp], "upstream_pooled_cpm": pooled_lvl[up]})
    psum = []
    from scipy.stats import wilcoxon
    for vname in ("raw", "covariates", "minus_3pc", "minus_10pc"):
        X = variants[vname]
        obs = (X[:, gp] * X[:, up]).mean(axis=0)
        rnd_r = np.stack([(X[:, gp] * X[:, rpart[:, j]]).mean(axis=0) for j in range(n_rand_pair)], axis=1)
        pair[f"r_{vname}"] = obs
        pair[f"r_random_median_{vname}"] = np.median(rnd_r, axis=1)
        rt_ = (X[:, [t]] * X[:, c_t]).mean(axis=0)          # TRIM72 with every level-matched gene of FUS's level
        d_ = obs - np.median(rnd_r, axis=1)
        psum.append({"variant": vname, "n_pairs": len(gp), "median_r_DoG_gene_vs_upstream_gene": np.median(obs),
                     "median_r_DoG_gene_vs_random_level_matched": np.median(rnd_r),
                     "pct_pairs_obs_gt_random_median": 100 * float((d_ > 0).mean()),
                     "wilcoxon_p_obs_vs_random": float(wilcoxon(d_).pvalue),
                     "TRIM72_FUS_r": float(obs[k_t]),
                     "TRIM72_FUS_pctile_among_DoG_pairs": 100 * float((obs < obs[k_t]).mean()),
                     "TRIM72_FUS_pctile_vs_all_FUS_level_genes": 100 * float((rt_ < obs[k_t]).mean()),
                     "n_FUS_level_genes": int(c_t.size)})
    pair.sort_values("r_minus_3pc", ascending=False).to_csv(os.path.join(TAB, "a_upstream_pair_coregulation.csv"),
                                                            index=False, float_format="%.4g")
    pd.DataFrame(psum).to_csv(os.path.join(TAB, "a_upstream_pair_summary.csv"), index=False, float_format="%.4g")
    log("  DoG pairs:", "; ".join(f"{d['variant']}: median r {d['median_r_DoG_gene_vs_upstream_gene']:.2f} vs random "
                                  f"{d['median_r_DoG_gene_vs_random_level_matched']:.2f}, TRIM72-FUS "
                                  f"{d['TRIM72_FUS_r']:.2f}" for d in psum))
    for k_, v_ in rob_cols.items():
        if not k_.endswith("_all"):
            res[k_] = v_
    res["DoG_class"] = dog_cls
    res["up_same_strand_expressed_gene"] = ex["up_same_strand_gene"].to_numpy()
    res["up_gene_distance_bp"] = ex["up_dist"].to_numpy()
    res["up_gene_pooled_cpm"] = ex["up_cpm"].to_numpy()
    res = res.drop(index=t).reset_index(drop=True)
    res = annotate(res, "gene")
    res = res.sort_values("r_z_minus_3pc", ascending=False)
    res.to_csv(os.path.join(TAB, "a_coreg_genomewide.csv"), index=False, float_format="%.5g")
    pd.DataFrame(nulls).to_csv(os.path.join(TAB, "a_null_summary.csv"), index=False, float_format="%.4g")
    st_rows = []
    for v_ in ("raw", "covariates", "minus_3pc", "minus_10pc"):
        st_rows += gene_set_tests(res[f"r_z_{v_}"].to_numpy(), res["gene"].to_numpy(),
                                  res["median_line_cpm"].to_numpy(), rng, f"r with TRIM72 across drug-doses ({v_})")
    pd.DataFrame(st_rows).to_csv(os.path.join(TAB, "a_gene_set_tests.csv"), index=False, float_format="%.4g")
    # top partner lists per variant (positive and negative)
    rows = []
    for name in variants:
        for sign, lab in ((1, "positive"), (-1, "negative")):
            sub = res[res[f"q_{name}"] < 0.05].copy()
            sub = sub.sort_values(f"r_z_{name}", ascending=(sign < 0))
            sub = sub[np.sign(sub[f"r_z_{name}"]) == sign].head(50)
            for rk, (_, rr) in enumerate(sub.iterrows(), 1):
                rows.append({"variant": name, "direction": lab, "rank": rk, "gene": rr["gene"],
                             "r": rr[f"r_z_{name}"], "q": rr[f"q_{name}"], "p_perm": rr[f"p_perm_{name}"],
                             "pct_vs_matched_genes": rr[f"pct_vs_matched_{name}"],
                             "r_raw": rr["r_z_raw"], "r_lfc_raw": rr["r_lfc_raw"],
                             "rho_spearman_raw": rr["rho_z_raw_spearman"], "median_line_cpm": rr["median_line_cpm"],
                             "DoG_class": rr["DoG_class"], "up_same_strand_gene": rr["up_same_strand_expressed_gene"],
                             "up_gene_distance_bp": rr["up_gene_distance_bp"],
                             "is_TF": rr["is_TF_Lambert2018"], "TF_family": rr["TF_DBD_family"],
                             "signalling": rr["signalling_category"], "gene_sets": rr["gene_sets"],
                             "cytoband": rr["cytoband"]})
    pd.DataFrame(rows).to_csv(os.path.join(TAB, "a_top_partners.csv"), index=False, float_format="%.4g")
    # regulators: TFs and signalling genes among the partners (any variant with q < 0.05)
    strong = np.zeros(len(res), dtype=bool)
    for v_ in ("covariates", "minus_3pc", "minus_10pc"):
        strong |= ((res[f"q_{v_}"] < 0.05) & (res[f"r_z_{v_}"].abs() >= 0.3)).to_numpy()
    reg = res[(res["is_TF_Lambert2018"] | (res["signalling_category"] != "")).to_numpy() & strong].copy()
    reg["best_r_after_global_removal"] = reg[["r_z_covariates", "r_z_minus_3pc", "r_z_minus_10pc"]].abs().max(axis=1)
    cols = ["gene", "is_TF_Lambert2018", "TF_DBD_family", "signalling_category", "gene_sets", "median_line_cpm",
            "r_z_raw", "q_raw", "r_z_covariates", "q_covariates", "r_z_minus_1pc", "r_z_minus_3pc", "q_minus_3pc",
            "pct_vs_matched_minus_3pc", "r_z_minus_10pc", "q_minus_10pc", "rho_z_raw_spearman",
            "r_minus_3pc_plates4to12_only", "r_minus_3pc_plates1to3_only", "r_minus_3pc_without_top10_TRIM72_drugdoses",
            "cytoband", "DoG_class", "up_same_strand_expressed_gene", "up_gene_distance_bp"]
    reg.sort_values("r_z_minus_3pc", ascending=False)[cols].to_csv(
        os.path.join(TAB, "a_regulator_partners_TF_signalling.csv"), index=False, float_format="%.4g")
    # which drug-doses raise TRIM72 beyond the global components
    out = ddk[["drug", "conc", "plates", "n_sig_genes", "cells_log2_vs_plate", "flags", "moa_fine", "targets"]].copy()
    out["TRIM72_lfc"] = Lf[:, t]
    out["TRIM72_z"] = Z[:, t]
    for k in (1, 3, 10):
        Xk = Zs - (U[:, :k] * S[:k]) @ Vt[:k]
        out[f"TRIM72_resid_minus_{k}pc_sd"] = Xk[:, t] / Xk[:, t].std()
    out["TRIM72_resid_covariates_sd"] = variants["covariates"][:, t]
    out.sort_values("TRIM72_z", ascending=False).to_csv(os.path.join(TAB, "a_TRIM72_by_drugdose_global_removed.csv"),
                                                        index=False, float_format="%.4g")
    log("(a) done")


# ============================================================================= (c) readthrough: genome-wide DoG index
def atlas_genes_with_coords():
    genes = pd.read_csv(os.path.join(FXD, "genes.csv"))
    genes = genes[genes["kind"] == "gene"].copy()
    gm = gene_meta()
    co = load_coords()
    g = genes.merge(gm[["token_id", "ensembl_id"]], left_on="token", right_on="token_id", how="left")
    g = g.merge(co, on="ensembl_id", how="left")
    g["tss"] = np.where(g["strand"] == 1, g["start"], g["end"])
    g["tes"] = np.where(g["strand"] == 1, g["end"], g["start"])
    return g


def dog_exposure(g, expr_min=5.0, near=20_000, far=100_000):
    """Per atlas gene: nearest upstream same-strand expressed gene (3' end before this gene's TSS, no overlap) and
    nearest convergent opposite-strand expressed gene (its 3' end beyond this gene's 3' end), with distances.
    expressed = atlas pooled CPM >= expr_min (genes outside the atlas are < 2 CPM)."""
    G = g.dropna(subset=["chrom"]).copy()
    E = G[G["pooled_cpm"] >= expr_min]
    by = {k: v.sort_values("start") for k, v in E.groupby(["chrom", "strand"])}
    rec = []
    for r in G.itertuples():
        s = int(r.strand)
        same = by.get((r.chrom, s))
        opp = by.get((r.chrom, -s))
        up = conv = None
        inside = False
        if same is not None:
            inside = bool(((same["start"] < r.end) & (same["end"] > r.start) & (same["col"] != r.col)).any())
            if s == 1:
                c = same[(same["end"] < r.start)]
                if len(c):
                    u = c.loc[c["end"].idxmax()]
                    up = (u["symbol"], r.start - u["end"], u["pooled_cpm"], int(u["col"]))
            else:
                c = same[(same["start"] > r.end)]
                if len(c):
                    u = c.loc[c["start"].idxmin()]
                    up = (u["symbol"], u["start"] - r.end, u["pooled_cpm"], int(u["col"]))
        if opp is not None:
            if s == 1:      # convergent: minus-strand gene downstream, its 3' end (start) beyond our 3' end
                c = opp[(opp["start"] > r.end)]
                if len(c):
                    u = c.loc[c["start"].idxmin()]
                    conv = (u["symbol"], u["start"] - r.end, u["pooled_cpm"])
            else:
                c = opp[(opp["end"] < r.start)]
                if len(c):
                    u = c.loc[c["end"].idxmax()]
                    conv = (u["symbol"], r.start - u["end"], u["pooled_cpm"])
        rec.append({"col": r.col, "overlaps_same_strand_expressed_gene": inside,
                    "up_same_strand_gene": up[0] if up else "", "up_dist": up[1] if up else np.nan,
                    "up_cpm": up[2] if up else np.nan, "up_col": up[3] if up else -1,
                    "conv_opp_strand_gene": conv[0] if conv else "", "conv_dist": conv[1] if conv else np.nan,
                    "conv_cpm": conv[2] if conv else np.nan})
    X = G.merge(pd.DataFrame(rec), on="col", how="left").reset_index(drop=True)
    ratio_up = X["up_cpm"] / X["pooled_cpm"]
    ratio_cv = X["conv_cpm"] / X["pooled_cpm"]
    no_up = ~(X["up_dist"] <= far) & ~X["overlaps_same_strand_expressed_gene"]
    X["class"] = np.select(
        [(X["up_dist"] <= near) & (ratio_up >= 8) & ~X["overlaps_same_strand_expressed_gene"],
         no_up & (X["conv_dist"] <= near) & (ratio_cv >= 8),
         no_up & ~(X["conv_dist"] <= far)],
        ["sense_exposed", "antisense_exposed_only", "unexposed"], default="other")
    return X


def dog_index(X, M, low_max=10.0, nbins=5):
    """Per drug-dose (rows of M = genes in X order): expression-stratified mean difference of M between
    sense-exposed and unexposed low genes, and between antisense-exposed and unexposed."""
    low = X["median_line_cpm"].to_numpy() <= low_max
    lvl = np.log2(X["median_line_cpm"].to_numpy())
    edges = np.quantile(lvl[low], np.linspace(0, 1, nbins + 1))
    b = np.clip(np.searchsorted(edges, lvl, side="right") - 1, 0, nbins - 1)
    cls = X["class"].to_numpy()
    out = {}
    for lab in ("sense_exposed", "antisense_exposed_only"):
        diffs, wts = [], []
        for k in range(nbins):
            e = low & (b == k) & (cls == lab)
            u = low & (b == k) & (cls == "unexposed")
            if e.sum() >= 5 and u.sum() >= 5:
                diffs.append(np.nanmean(M[:, e], axis=1) - np.nanmean(M[:, u], axis=1))
                wts.append(e.sum())
        out[lab] = np.average(np.column_stack(diffs), axis=1, weights=wts)
    return out


def step_c_dog():
    log("(c) genome-wide downstream-of-gene (readthrough) index")
    g = atlas_genes_with_coords()
    X = dog_exposure(g)
    dd = pd.read_csv(os.path.join(FXD, "drugdose.csv"))
    cols = X["col"].to_numpy()
    Z = np.asarray(np.load(os.path.join(FXD, "DD_z.npy"), mmap_mode="r"))[:, cols].astype(np.float64)
    Lf = np.asarray(np.load(os.path.join(FXD, "DD_lfc.npy"), mmap_mode="r"))[:, cols].astype(np.float64)
    iz = dog_index(X, Z)
    il = dog_index(X, Lf)
    t = int(np.flatnonzero(X["symbol"].to_numpy() == "TRIM72")[0])
    out = dd[["drug", "conc", "plates", "n_sig_genes", "cells_log2_vs_plate", "flags", "moa_fine"]].copy()
    out["DoG_sense_index_z"] = iz["sense_exposed"]
    out["DoG_antisense_index_z"] = iz["antisense_exposed_only"]
    out["DoG_sense_index_log2"] = il["sense_exposed"]
    out["DoG_antisense_index_log2"] = il["antisense_exposed_only"]
    out["DoG_sense_index_robust_z"] = (out["DoG_sense_index_z"] - out["DoG_sense_index_z"].median()) / \
        (1.4826 * (out["DoG_sense_index_z"] - out["DoG_sense_index_z"].median()).abs().median())
    out["TRIM72_z"] = Z[:, t]
    out["TRIM72_lfc"] = Lf[:, t]
    out["rank_sense_index"] = out["DoG_sense_index_z"].rank(ascending=False).astype(int)
    out.sort_values("DoG_sense_index_z", ascending=False).to_csv(os.path.join(TAB, "c_DoG_index_by_drugdose.csv"),
                                                                 index=False, float_format="%.4g")
    X.drop(columns=["token_id"], errors="ignore").to_csv(os.path.join(TAB, "c_DoG_gene_exposure_classes.csv"),
                                                         index=False, float_format="%.5g")
    # TRIM72 module (a) vs exposure class
    a = os.path.join(TAB, "a_coreg_genomewide.csv")
    summ = []
    from scipy.stats import fisher_exact, spearmanr, mannwhitneyu
    keep = ~(dd["unreliable_plate_only"].astype(str).str.lower().eq("true"))
    for nm, v in (("raw", out["DoG_sense_index_z"]), ("antisense", out["DoG_antisense_index_z"])):
        rho, p = spearmanr(v[keep], out.loc[keep, "TRIM72_z"])
        summ.append({"test": f"Spearman over drug-doses: DoG {nm} index vs TRIM72 z", "n": int(keep.sum()),
                     "estimate": rho, "p": p})
    if os.path.exists(a):
        A = pd.read_csv(a, usecols=["gene", "r_z_raw", "r_z_minus_3pc", "r_z_minus_10pc"])
        Y = X.merge(A, left_on="symbol", right_on="gene", how="inner")
        low = Y["median_line_cpm"] <= 10
        for v in ("r_z_raw", "r_z_minus_3pc", "r_z_minus_10pc"):
            mod = Y[v] >= 0.4
            for lab in ("sense_exposed", "antisense_exposed_only"):
                sel = low & Y["class"].isin([lab, "unexposed"])
                tab = pd.crosstab(mod[sel], Y.loc[sel, "class"] == lab).reindex(index=[False, True],
                                                                                 columns=[False, True], fill_value=0)
                orr, p = fisher_exact(tab.to_numpy())
                summ.append({"test": f"TRIM72 module ({v} >= 0.4) among low genes (<= 10 CPM): {lab} vs unexposed",
                             "n": int(sel.sum()), "n_module": int(mod[sel].sum()),
                             "n_module_exposed": int(tab.loc[True, True]),
                             "pct_module_exposed": 100 * tab.loc[True, True] / max(tab.loc[True].sum(), 1),
                             "pct_rest_exposed": 100 * tab.loc[False, True] / max(tab.loc[False].sum(), 1),
                             "estimate": orr, "p": p})
            sel = low & Y["class"].isin(["sense_exposed", "unexposed"])
            u, p = mannwhitneyu(Y.loc[sel & (Y["class"] == "sense_exposed"), v],
                                Y.loc[sel & (Y["class"] == "unexposed"), v])
            summ.append({"test": f"{v} (corr. with TRIM72) of low genes: sense_exposed vs unexposed (Mann-Whitney)",
                         "n": int(sel.sum()),
                         "estimate": float(Y.loc[sel & (Y["class"] == "sense_exposed"), v].median() -
                                           Y.loc[sel & (Y["class"] == "unexposed"), v].median()), "p": p})
    for d_ in ("Idarubicin (hydrochloride)", "Homoharringtonine", "Auranofin", "Dinaciclib",
               "Epirubicin (hydrochloride)", "Doxorubicin (hydrochloride)", "Topotecan (hydrochloride)",
               "Mitoxantrone (dihydrochloride)", "Harringtonine", "Panobinostat"):
        r = out[(out["drug"] == d_) & np.isclose(out["conc"], 5.0)]
        for _, rr in r.iterrows():
            summ.append({"test": f"DoG sense index, {d_} 5 uM ({rr['plates']})", "n": len(out),
                         "estimate": rr["DoG_sense_index_z"], "rank_of_1132": int(rr["rank_sense_index"]),
                         "robust_z_vs_drugdoses": rr["DoG_sense_index_robust_z"],
                         "antisense_index": rr["DoG_antisense_index_z"]})
    # TRIM72 among the DoG-exposed genes under each raiser: is it special, or one of many induced DoG-exposed genes?
    Q = np.asarray(np.load(os.path.join(FXD, "DD_qup.npy"), mmap_mode="r"))[:, cols].astype(np.float64)
    sense_m = (X["class"] == "sense_exposed").to_numpy()
    unexp_m = (X["class"] == "unexposed").to_numpy()
    lowm = (X["median_line_cpm"] <= 10).to_numpy()
    rk = []
    for d_ in ("Idarubicin (hydrochloride)", "Homoharringtonine", "Auranofin", "Dinaciclib",
               "Epirubicin (hydrochloride)", "Doxorubicin (hydrochloride)", "Topotecan (hydrochloride)",
               "Mitoxantrone (dihydrochloride)", "Harringtonine", "Panobinostat"):
        rr_ = dd.index[(dd["drug"] == d_) & np.isclose(dd["conc"], 5.0)]
        if not len(rr_):
            continue
        r_ = int(rr_[0])
        z_, l_, q_ = Z[r_], Lf[r_], Q[r_]
        up_call = (q_ < 0.05) & (l_ > 1)
        top = np.flatnonzero(sense_m)[np.argsort(-z_[sense_m])[:8]]
        rk.append({"drug": d_, "conc": 5.0, "plates": dd.loc[r_, "plates"], "TRIM72_z": z_[t], "TRIM72_log2FC": l_[t],
                   "TRIM72_z_pctile_among_DoG_exposed": 100 * float((z_[sense_m] < z_[t]).mean()),
                   "TRIM72_z_pctile_among_all_genes": 100 * float((z_ < z_[t]).mean()),
                   "pct_low_DoG_exposed_up_q05_2x": 100 * float(up_call[sense_m & lowm].mean()),
                   "pct_low_unexposed_up_q05_2x": 100 * float(up_call[unexp_m & lowm].mean()),
                   "top_DoG_exposed_genes (upstream gene, z)": "; ".join(
                       f"{X['symbol'].iloc[i]} ({X['up_same_strand_gene'].iloc[i]}, {z_[i]:.1f})" for i in top)})
    pd.DataFrame(rk).to_csv(os.path.join(TAB, "c_DoG_raisers_TRIM72_rank.csv"), index=False, float_format="%.4g")
    cnt = X["class"].value_counts()
    for k, v in cnt.items():
        summ.append({"test": f"genes in class {k} (all atlas genes)", "n": int(v)})
    summ.append({"test": "TRIM72 class", "estimate": np.nan,
                 "note": f"{X.loc[t, 'class']}; upstream same-strand expressed gene {X.loc[t, 'up_same_strand_gene']} "
                         f"{X.loc[t, 'up_dist']:.0f} bp, {X.loc[t, 'up_cpm']:.0f} CPM vs TRIM72 "
                         f"{X.loc[t, 'pooled_cpm']:.1f} CPM"})
    pd.DataFrame(summ).to_csv(os.path.join(TAB, "c_DoG_tests.csv"), index=False, float_format="%.4g")
    log("(c) DoG done")


# ============================================================================= (b) baseline covariation over lines
def load_prep():
    with open(os.path.join(CACHE, "prep_done.json")) as fh:
        meta = json.load(fh)
    q = np.load(os.path.join(CACHE, "plate_line_quiet.npz"))
    return meta, q


def zrank(M, axis):
    from scipy.stats import rankdata
    R = rankdata(M, axis=axis)
    R = R - R.mean(axis=axis, keepdims=True)
    sd = R.std(axis=axis, keepdims=True)
    sd[sd == 0] = np.nan
    return R / sd


def step_b(B=2000):
    log("(b) untreated covariation with TRIM72 across the 50 lines (per plate, then median over plates)")
    rng = np.random.default_rng(SEED + 1)
    meta, q = load_prep()
    plates, lines = meta["plates"], meta["lines"]
    info = json.load(open(os.path.join(FXD, "info.json")))
    use_p = [i for i, p in enumerate(plates) if p not in info.get("unreliable_plates", [])]
    counts = q["counts"][use_p]                       # P x L x G
    tot = q["total"][use_p]
    cells = q["cells"][use_p]
    P, L, G = counts.shape
    cpm = counts / tot[:, :, None] * 1e6
    genes = pd.read_csv(os.path.join(FXD, "genes.csv"))
    genes = genes[genes["kind"] == "gene"]
    gm = gene_meta()
    sym = pd.Series(gm["gene_symbol"].values, index=gm["token_id"].values)
    t_tok = int(gm.loc[gm["gene_symbol"] == "TRIM72", "token_id"].iloc[0])
    extra = gm.loc[gm["gene_symbol"].isin(MUSCLE_TFS), "token_id"].astype(int).tolist()
    # every gene with >= 200 counts in the quiet wells of the reliable plates (atlas genes are >= 2 CPM; this adds
    # the low genes so that each gene can be compared with genes of its own level) + the muscle list
    csum = counts.sum(axis=(0, 1))
    named = np.zeros(G, dtype=bool)
    named[gm["token_id"].astype(int).to_numpy()] = True
    toks = np.array(sorted(set(np.flatnonzero((csum >= 200) & named)) | set(genes["token"].astype(int)) | set(extra)))
    toks = toks[toks != t_tok]
    # within plate: log CPM (pseudo 0.5 count on the plate's line total), ranks over lines
    lt = np.log2((counts[:, :, toks] + 0.5) / tot[:, :, None] * 1e6)
    yt = np.log2((counts[:, :, t_tok] + 0.5) / tot * 1e6)
    ZG = zrank(lt, axis=1)                              # P x L x g
    ZT = zrank(yt, axis=1)                              # P x L
    rho_p = np.einsum("pl,plg->pg", ZT, np.nan_to_num(ZG)) / L
    rho_med = np.median(rho_p, axis=0)
    # organ-adjusted: residual ranks after organ means (organs with >= 3 lines; the rest one group)
    ln = pd.read_csv(os.path.join(FXD, "lines.csv"), dtype={"cell_line_id": str}).set_index("cell_line_id")
    organ = ln.loc[lines, "Organ"].fillna("other").to_numpy()
    vc = pd.Series(organ).value_counts()
    organ = np.where(pd.Series(organ).map(vc).to_numpy() >= 3, organ, "other")
    D = pd.get_dummies(organ).to_numpy(dtype=float)
    H = np.eye(L) - D @ np.linalg.pinv(D)               # residual maker
    ZGa = np.einsum("kl,plg->pkg", H, np.nan_to_num(ZG))
    ZTa = ZT @ H.T
    ZGa /= np.maximum(np.sqrt((ZGa ** 2).mean(axis=1, keepdims=True)), 1e-9)
    ZTa /= np.maximum(np.sqrt((ZTa ** 2).mean(axis=1, keepdims=True)), 1e-9)
    rho_adj = np.median(np.einsum("pl,plg->pg", ZTa, ZGa) / L, axis=0)
    # line-permutation null (the same permutation of lines on every plate), and within-organ permutation for adj
    exceed = np.zeros(len(toks))
    exceed_a = np.zeros(len(toks))
    null_sd = np.zeros(len(toks))
    null_sq = np.zeros(len(toks))
    groups = [np.flatnonzero(organ == o) for o in np.unique(organ)]
    ZGn = np.nan_to_num(ZG)
    for b in range(B):
        pm = rng.permutation(L)
        r = np.median(np.einsum("pl,plg->pg", ZT[:, pm], ZGn) / L, axis=0)
        exceed += np.abs(r) >= np.abs(rho_med)
        null_sq += r ** 2
        if b < B // 2:
            pa = np.arange(L)
            for gidx in groups:
                pa[gidx] = rng.permutation(gidx)
            ra = np.median(np.einsum("pl,plg->pg", ZTa[:, pa], ZGa) / L, axis=0)
            exceed_a += np.abs(ra) >= np.abs(rho_adj)
    null_sd = np.sqrt(null_sq / B)
    p_perm = (1 + exceed) / (B + 1)
    p_adj = (1 + exceed_a) / (B // 2 + 1)
    from scipy.stats import norm
    p_norm = 2 * norm.sf(np.abs(rho_med / null_sd))
    pooled = 1e6 * counts.sum(axis=(0, 1)) / tot.sum()
    med_line_cpm = np.median(cpm.mean(axis=0), axis=0)
    res = pd.DataFrame({"gene": sym.reindex(toks).values, "token": toks,
                        "median_line_cpm_quiet_wells": med_line_cpm[toks], "pooled_cpm": pooled[toks],
                        "rho_median_over_plates": rho_med,
                        "rho_plate_q25": np.quantile(rho_p, 0.25, axis=0),
                        "rho_plate_q75": np.quantile(rho_p, 0.75, axis=0),
                        "n_plates_same_sign": (np.sign(rho_p) == np.sign(rho_med)[None]).sum(axis=0),
                        "null_sd_line_perm": null_sd, "p_perm_lines": p_perm, "p_norm_calibrated": p_norm,
                        "rho_organ_adjusted": rho_adj, "p_perm_within_organ": p_adj})
    lvl_b = res["pooled_cpm"].to_numpy()
    lb = np.log2(np.maximum(lvl_b, 1e-6))
    order = np.argsort(lb)
    pct = np.empty(len(res))
    for i in range(len(res)):                         # percentile of rho among genes within 2x of the gene's level
        lo, hi_ = np.searchsorted(lb[order], [lb[i] - 1, lb[i] + 1])
        pct[i] = 100 * float((rho_med[order[lo:hi_]] < rho_med[i]).mean())
    res["pct_rho_vs_level_matched_genes"] = pct
    res["q_perm_lines"] = bh(res["p_norm_calibrated"])
    res["q_organ_adjusted"] = bh(res["p_perm_within_organ"])
    res["in_atlas"] = res["token"].isin(genes["token"])
    # robustness: DMSO wells only (2 per plate), the same per-plate Spearman over lines, median over plates
    dq = np.load(os.path.join(CACHE, "plate_line_dmso.npz"))
    dcounts, dtot = dq["counts"][use_p], dq["total"][use_p]
    okp = (dtot > 0).all(axis=1)                        # plates where every line has DMSO counts
    ZGd = np.nan_to_num(zrank(np.log2((dcounts[okp][:, :, toks] + 0.5) / dtot[okp][:, :, None] * 1e6), axis=1))
    ZTd = zrank(np.log2((dcounts[okp][:, :, t_tok] + 0.5) / dtot[okp] * 1e6), axis=1)
    res["rho_dmso_only_median_over_plates"] = np.median(np.einsum("pl,plg->pg", ZTd, ZGd) / L, axis=0)
    res["n_plates_dmso"] = int(okp.sum())
    del ZGd, dcounts
    # readthrough exposure of every gene (as in c): DoG-exposed genes among TRIM72's untreated partners
    Xd = dog_exposure(atlas_genes_with_coords())
    cls_tok = dict(zip(Xd["token"].astype(int), Xd["class"]))
    res["DoG_class"] = res["token"].map(cls_tok).fillna("not in atlas / no coordinates")
    upsym = dict(zip(Xd["token"].astype(int), Xd["up_same_strand_gene"]))
    res["up_same_strand_expressed_gene"] = res["token"].map(upsym).fillna("")
    col2tok = dict(zip(genes["col"].astype(int), genes["token"].astype(int)))
    tpos = {int(x): k for k, x in enumerate(toks)}
    se = Xd[(Xd["class"] == "sense_exposed") & (Xd["up_col"] >= 0)]
    pairs = [(tpos.get(int(a)), tpos.get(col2tok.get(int(b), -1)), sa, sb, d)
             for a, b, sa, sb, d in zip(se["token"], se["up_col"], se["symbol"], se["up_same_strand_gene"], se["up_dist"])]
    pairs = [p_ for p_ in pairs if p_[0] is not None and p_[1] is not None]
    gp_ = np.array([p_[0] for p_ in pairs])
    up_ = np.array([p_[1] for p_ in pairs])
    lvl_t = pooled[toks]
    obs = np.median((ZGn[:, :, gp_] * ZGn[:, :, up_]).mean(axis=1), axis=0)
    rnd_med = np.zeros(len(gp_))
    for k, (g_, u_) in enumerate(zip(gp_, up_)):
        jj = level_matched(lvl_t, u_, (np.arange(len(toks)) != g_) & (np.arange(len(toks)) != u_), 20, rng)
        rnd_med[k] = np.median(np.median((ZGn[:, :, [g_]] * ZGn[:, :, jj]).mean(axis=1), axis=0))
    pr = pd.DataFrame({"gene": [p_[2] for p_ in pairs], "upstream_gene": [p_[3] for p_ in pairs],
                       "distance_bp": [p_[4] for p_ in pairs], "gene_pooled_cpm": lvl_t[gp_],
                       "upstream_pooled_cpm": lvl_t[up_], "rho_baseline_with_upstream_gene": obs,
                       "rho_baseline_random_level_matched_median": rnd_med})
    f_i = int(np.flatnonzero(sym.reindex(toks).values == "FUS")[0])
    rho_tf = float(rho_med[f_i])
    cf = np.flatnonzero((lvl_t >= lvl_t[f_i] / 2) & (lvl_t <= lvl_t[f_i] * 2))
    xt = Xd[Xd["symbol"] == "TRIM72"].iloc[0]
    pr = pd.concat([pd.DataFrame([{"gene": "TRIM72", "upstream_gene": xt["up_same_strand_gene"],
                                   "distance_bp": xt["up_dist"],
                                   "gene_pooled_cpm": float(pooled[t_tok]), "upstream_pooled_cpm": float(lvl_t[f_i]),
                                   "rho_baseline_with_upstream_gene": rho_tf,
                                   "rho_baseline_random_level_matched_median": float(np.median(rho_med[cf]))}]),
                    pr], ignore_index=True)
    pr.to_csv(os.path.join(TAB, "b_upstream_pair_baseline.csv"), index=False, float_format="%.4g")
    from scipy.stats import wilcoxon, fisher_exact
    d_ = obs - rnd_med
    pair_tests = [
        {"test": "baseline: DoG-exposed genes vs their upstream same-strand gene, Spearman over lines (median over "
                 "plates); median over pairs vs level-matched random partners (Wilcoxon on the differences)",
         "n1": len(gp_), "estimate": float(np.median(obs)), "unit": "median rho (pairs)",
         "p": float(wilcoxon(d_).pvalue),
         "groups": f"random partners median rho {np.median(rnd_med):.3f}; pairs above their random median "
                   f"{100 * (d_ > 0).mean():.0f}%"},
        {"test": "baseline: TRIM72 vs FUS (upstream same-strand gene, 17 kb), Spearman over lines, median over plates",
         "n1": L, "estimate": rho_tf, "unit": "rho",
         "p": float(res.loc[res["gene"] == "FUS", "p_norm_calibrated"].iloc[0]),
         "groups": f"percentile among {cf.size} genes of FUS's level (within 2x): "
                   f"{100 * (rho_med[cf] < rho_tf).mean():.1f}; among DoG pairs: {100 * (obs < rho_tf).mean():.1f}"}]
    lv = res["pooled_cpm"].to_numpy()
    classed = res["token"].isin(cls_tok).to_numpy()            # atlas genes with coordinates (have a DoG class)
    top = res[classed].nlargest(100, "rho_median_over_plates")
    lowm = (lv >= 1) & (lv <= 20) & classed
    for nm_, sel_ in (("top 100 positive among classed atlas genes", res.index.isin(top.index)),
                      ("q < 0.05 (line permutation), positive, classed atlas genes",
                       ((res["q_perm_lines"] < 0.05) & (res["rho_median_over_plates"] > 0)).to_numpy() & classed)):
        a_ = int((sel_ & (res["DoG_class"] == "sense_exposed")).sum())
        b_ = int((sel_ & (res["DoG_class"] != "sense_exposed")).sum())
        c_ = int((~sel_ & lowm & (res["DoG_class"] == "sense_exposed")).sum())
        e_ = int((~sel_ & lowm & (res["DoG_class"] != "sense_exposed")).sum())
        orr, pf_ = fisher_exact([[a_, b_], [c_, e_]])
        pair_tests.append({"test": f"baseline partners of TRIM72 ({nm_}): DoG-exposed (sense) share vs other "
                                   f"classed atlas genes at 1-20 CPM in the quiet wells (Fisher)", "n1": a_ + b_, "n2": c_ + e_,
                           "estimate": orr,
                           "unit": "odds ratio", "p": pf_,
                           "groups": f"{100 * a_ / max(a_ + b_, 1):.1f}% of partners vs "
                                     f"{100 * c_ / max(c_ + e_, 1):.1f}% of other 1-20 CPM genes"})
    res = annotate(res, "gene")
    res = res.sort_values("rho_median_over_plates", ascending=False)
    res.to_csv(os.path.join(TAB, "b_baseline_coexpression_genomewide.csv"), index=False, float_format="%.5g")
    log("  top baseline partners:", ", ".join(res.head(15)["gene"].astype(str)))
    # focus genes
    import tahoe_gene_panel as Pn
    focus = set(MUSCLE_TFS) | set(Pn.P53_ACTIVITY) | set(Pn.CONTEXT["P53_EXT"]) | \
        {"TP53", "MDM2", "MDM4", "FUS", "PYCARD", "ITGAM", "PYDC1", "KAT8", "BCKDK", "PRSS8", "PRSS36", "STX4",
         "VKORC1", "ZNF646", "ZNF668", "PRSS53", "ITGAX", "ATF3", "PMAIP1"}
    st_rows = []
    for c_, lab_ in (("rho_median_over_plates", "baseline rho with TRIM72 over lines (quiet wells)"),
                     ("rho_organ_adjusted", "baseline rho with TRIM72 over lines, organ-adjusted"),
                     ("rho_dmso_only_median_over_plates", "baseline rho with TRIM72 over lines (DMSO wells only)")):
        st_rows += gene_set_tests(res[c_].to_numpy(), res["gene"].to_numpy(), res["pooled_cpm"].to_numpy(), rng, lab_)
    pd.DataFrame(st_rows).to_csv(os.path.join(TAB, "b_gene_set_tests.csv"), index=False, float_format="%.4g")
    res[res["gene"].isin(focus)].to_csv(os.path.join(TAB, "b_baseline_focus_genes.csv"), index=False,
                                         float_format="%.4g")
    # per line consensus TRIM72 level (within-plate centred log CPM, mean over plates) and line features
    ylc = yt - yt.mean(axis=1, keepdims=True)
    per = pd.DataFrame({"cell_line_id": lines, "cell_name": ln.loc[lines, "cell_name"].values, "organ": organ,
                        "TRIM72_log2cpm_vs_plate_mean": ylc.mean(axis=0),
                        "TRIM72_log2cpm_sd_over_plates": ylc.std(axis=0),
                        "TRIM72_cpm_median_over_plates": np.median(2 ** yt, axis=0),
                        "TRIM72_mean_rank_within_plate": (np.argsort(np.argsort(yt, axis=1), axis=1) + 1).mean(axis=0),
                        "TRIM72_counts_total": counts[:, :, t_tok].sum(axis=0), "cells_total": cells.sum(axis=0)})
    base = pd.read_csv(os.path.join(DATA, "gene_panel", "results", "baseline_by_cell_line.csv"),
                       dtype={"cell_line_id": str})
    pf = pd.read_csv(os.path.join(DATA, "gene_panel", "results", "p53_functional_status.csv"),
                     dtype={"cell_line_id": str})
    bcols = [c for c in ("cell_line_id", "tp53_status", "tp53_group", "tp53_changes") if c in base]
    per = per.merge(base[bcols], on="cell_line_id", how="left")
    pcols = [c for c in ("cell_line_id", "basal_p53_activity_log2", "p53_responsiveness_log2", "functional_call")
             if c in pf]
    per = per.merge(pf[pcols], on="cell_line_id", how="left")
    # FUS (upstream same-strand neighbour) level per line, the same way
    f_tok = int(gm.loc[gm["gene_symbol"] == "FUS", "token_id"].iloc[0])
    yf = np.log2((counts[:, :, f_tok] + 0.5) / tot * 1e6)
    per["FUS_log2cpm_vs_plate_mean"] = (yf - yf.mean(axis=1, keepdims=True)).mean(axis=0)
    per.to_csv(os.path.join(TAB, "b_TRIM72_baseline_per_line.csv"), index=False, float_format="%.4g")
    # tests on line features
    from scipy.stats import mannwhitneyu, kruskal, spearmanr
    tests = list(pair_tests)
    v = per["TRIM72_log2cpm_vs_plate_mean"]
    if "tp53_group" in per:
        grp = per["tp53_group"].astype(str)
        levels = sorted(grp.dropna().unique())
        wt = v[grp.str.upper().str.startswith("WT")]
        alt = v[~grp.str.upper().str.startswith("WT") & grp.ne("nan")]
        u, p = mannwhitneyu(wt, alt)
        tests.append({"test": "TRIM72 baseline: TP53 WT vs altered lines (Mann-Whitney)", "n1": len(wt), "n2": len(alt),
                      "estimate": float(wt.median() - alt.median()), "unit": "log2 (median WT - median altered)",
                      "p": p, "groups": "; ".join(levels)})
    for c in ("basal_p53_activity_log2", "p53_responsiveness_log2", "FUS_log2cpm_vs_plate_mean"):
        if c in per:
            ok = per[c].notna()
            rho, p = spearmanr(v[ok], per.loc[ok, c])
            tests.append({"test": f"TRIM72 baseline vs {c} (Spearman over lines)", "n1": int(ok.sum()),
                          "estimate": rho, "unit": "rho", "p": p})
    h, p = kruskal(*[v[per["organ"] == o] for o in np.unique(organ)])
    tests.append({"test": "TRIM72 baseline by organ (Kruskal-Wallis; organs with < 3 lines pooled as 'other')",
                  "n1": L, "estimate": h, "unit": "H", "p": p,
                  "groups": "; ".join(f"{o}: {v[per['organ'] == o].median():+.2f} (n={int((per['organ'] == o).sum())})"
                                      for o in np.unique(organ))})
    # plate batch of the untreated level: plates 1-3 + 14 vs 4-12 (median line CPM), genome-wide rank of TRIM72
    pn = [plates[i] for i in use_p]
    hi = np.array([p in ("plate1", "plate2", "plate3", "plate14") for p in pn])
    lc = np.log2(np.median(cpm[:, :, :], axis=1) + 0.1)      # P x G median line CPM per plate
    gap = lc[hi].mean(axis=0) - lc[~hi].mean(axis=0)
    expressed = (pooled >= 2)
    gtab = pd.DataFrame({"gene": sym.reindex(np.arange(G)).values, "token": np.arange(G),
                         "pooled_cpm": pooled, "plate_gap_log2_p1to3_14_vs_p4to12": gap})
    gtab = gtab[expressed & gtab["gene"].notna()].copy()
    gtab["gap_rank_desc"] = gtab["plate_gap_log2_p1to3_14_vs_p4to12"].rank(ascending=False).astype(int)
    gtab["gap_percentile"] = 100 * gtab["plate_gap_log2_p1to3_14_vs_p4to12"].rank(pct=True)
    gtab["DoG_class"] = gtab["token"].map(cls_tok).fillna("not in atlas / no coordinates")
    gtab["up_same_strand_expressed_gene"] = gtab["token"].map(upsym).fillna("")
    gv = gtab["plate_gap_log2_p1to3_14_vs_p4to12"]
    lowg = gtab["pooled_cpm"] <= 20
    for cl_ in ("sense_exposed", "antisense_exposed_only", "other"):
        a_ = gv[lowg & (gtab["DoG_class"] == cl_)]
        b_ = gv[lowg & (gtab["DoG_class"] == "unexposed")]
        tests.append({"test": f"untreated plate batch (plates 1-3,14 minus 4-12, log2) of 2-20 CPM genes: {cl_} vs "
                              f"unexposed (Mann-Whitney)", "n1": len(a_), "n2": len(b_),
                      "estimate": float(a_.median() - b_.median()), "unit": "difference of medians (log2)",
                      "p": float(mannwhitneyu(a_, b_).pvalue),
                      "groups": f"medians {a_.median():.3f} vs {b_.median():.3f}"})
    t100 = gtab.nsmallest(100, "gap_rank_desc")
    tests.append({"test": "untreated plate batch: DoG-exposed (sense) share among the 100 genes with the largest gap",
                  "n1": 100, "estimate": 100 * float((t100["DoG_class"] == "sense_exposed").mean()), "unit": "%",
                  "groups": f"all genes >= 2 CPM: {100 * float((gtab['DoG_class'] == 'sense_exposed').mean()):.1f}%"})
    gtab.sort_values("gap_rank_desc").to_csv(os.path.join(TAB, "b_plate_batch_gap_genomewide.csv"), index=False,
                                             float_format="%.4g")
    tt = gtab[gtab["gene"] == "TRIM72"].iloc[0]
    tests.append({"test": "TRIM72 untreated plate batch: mean log2 median-line CPM, plates 1-3,14 minus plates 4-12",
                  "n1": int(len(gtab)), "estimate": tt["plate_gap_log2_p1to3_14_vs_p4to12"], "unit": "log2",
                  "p": np.nan, "groups": f"rank {int(tt['gap_rank_desc'])} of {len(gtab)} genes >= 2 CPM"})
    pd.DataFrame(tests).to_csv(os.path.join(TAB, "b_TRIM72_baseline_tests.csv"), index=False, float_format="%.4g")
    log("(b) done")


# ============================================================================= (c) locus: corrected effects of neighbours
def locus_table():
    """Ensembl genes within 200 kb of TRIM72 (REST overlap result) joined to Tahoe tokens. Without a usable REST
    result (Ensembl REST down), the same window is taken from the BioMart coordinates of the same release."""
    c, s, e = TRIM72_REGION
    p = os.path.join(EXT, "ensembl_trim72_region.json")
    try:
        with open(p) as fh:
            reg = pd.DataFrame(json.load(fh))
        reg = reg.rename(columns={"id": "ensembl_id", "external_name": "ens_name"})
    except (OSError, ValueError):
        log("  Ensembl REST region not available: taking the TRIM72 +-200 kb window from the BioMart coordinates")
        b = load_coords()
        reg = b[(b["chrom"] == c) & (b["end"] >= s - 200000) & (b["start"] <= e + 200000)].copy()
    gm = gene_meta()
    reg = reg.merge(gm, on="ensembl_id", how="left")
    reg["rel_to_TRIM72"] = np.where(reg["end"] < s, "upstream (5')", np.where(reg["start"] > e, "downstream (3')",
                                                                               "overlapping"))
    reg["same_strand_as_TRIM72"] = reg["strand"] == 1
    reg["distance_bp"] = np.where(reg["end"] < s, s - reg["end"], np.where(reg["start"] > e, reg["start"] - e, 0))
    reg["label"] = reg["gene_symbol"].fillna(reg["ens_name"]).fillna(reg["ensembl_id"])
    return reg.sort_values("start").reset_index(drop=True)


def corrected_effects(counts, tot, nc, expressed=None):
    """The atlas's per_line_columns steps (method v3) on counts (atlas wells x lines x C): plate drug-well
    baseline per line, composition shift, two-pass leave-drug-out position correction on the column's own
    well-level values; returns per (well, line) r2, well-level W1/W2, per-well z (robust over reliable drug wells),
    per drug-dose per-line means and Stouffer z. expressed (lines x C, bool): lines that do not express a column
    are left out (as the atlas's expr_mask), so a well-level effect is the median over expressing lines only."""
    import tahoe_atlas as A
    fx = A.FX(os.path.join(DATA, "atlas"))
    A.MIN_CELLS = fx.info.get("min_cells", 30)
    w = fx.wells
    Y = A.log_cpm(counts, tot, nc)
    if expressed is not None:
        Y[:, ~expressed] = np.nan
    S = A.composition_matrix(fx)
    r1 = np.full_like(Y, np.nan)
    for p in fx.plates:
        rows = np.flatnonzero((w["plate"] == p).to_numpy())
        drug = rows[fx.drug_w[rows]]
        base = np.nanmedian(Y[drug], axis=0)
        r1[rows] = Y[rows] - base[None] - S[rows][:, :, None]
    W1 = np.nanmedian(r1, axis=1)
    W1[np.isfinite(r1).sum(axis=1) < A.MIN_LINES] = np.nan
    slot, dname = w["slot"].to_numpy(dtype=float), w["drug"].to_numpy(dtype=object)
    f1 = w["plate_scale_pass1"].to_numpy(dtype=float)
    e1, _, _ = A.loo_effect(W1, slot, dname, fx.drug_w)
    c, s = A.robust_cols(W1 - e1, fx.ref_w)
    clean = np.abs((W1 - e1 - c) / (s * f1[:, None])) < A.POS_CLEAN_Z
    eff = A.loo_effect(W1, slot, dname, fx.drug_w, clean=clean)[0]
    W2 = W1 - eff
    r2 = np.where(np.isfinite(W1)[:, None, :], r1 - eff[:, None, :], np.nan)
    c2, s2 = A.robust_cols(W2, fx.ref_w)
    zw = (W2 - c2) / (s2 * w["plate_scale"].to_numpy(dtype=float)[:, None])
    nd = len(fx.dd)
    per = np.full((nd, r2.shape[1], r2.shape[2]), np.nan, dtype=np.float32)
    ddl = np.full((nd, r2.shape[2]), np.nan)
    ddz = np.full((nd, r2.shape[2]), np.nan)
    for d, ii in fx.wells_of_dd.items():
        if len(ii):
            per[d] = np.nanmean(r2[ii], axis=0)
            ddl[d] = np.nanmean(W2[ii], axis=0)
            ddz[d] = np.nansum(zw[ii], axis=0) / np.sqrt(np.isfinite(zw[ii]).sum(axis=0).clip(1))
    return fx, r1, r2, W2, zw, per, ddl, ddz


def step_c_locus():
    log("(c) TRIM72 locus: neighbours under idarubicin and the other raisers")
    meta, q = load_prep()
    lines = meta["lines"]
    reg = locus_table()
    sel = pd.read_parquet(os.path.join(CACHE, "selected_genes_per_well_line.parquet"))
    fxw = pd.read_csv(os.path.join(FXD, "wells.csv"), dtype={"sample": str})
    wi = {s_: i for i, s_ in enumerate(fxw["sample"])}
    li = {l_: i for i, l_ in enumerate(lines)}
    sel = sel[sel["sample"].isin(wi) & sel["cell_line_id"].isin(li)]
    toks = [t for t in reg["token_id"].dropna().astype(int) if str(t) in sel.columns]
    reg = reg[reg["token_id"].isin(toks)].reset_index(drop=True)
    N, L, C = len(fxw), len(lines), len(toks)
    counts = np.zeros((N, L, C), dtype=np.float32)
    tot = np.zeros((N, L))
    nc = np.zeros((N, L))
    a_ = sel["sample"].map(wi).to_numpy()
    b_ = sel["cell_line_id"].map(li).to_numpy()
    counts[a_, b_] = sel[[str(t) for t in toks]].to_numpy(dtype=np.float32)
    tot[a_, b_] = sel["total_counts"].to_numpy()
    nc[a_, b_] = sel["n_cells"].to_numpy()
    # baseline level per line (quiet wells, plates pooled except unreliable) and 'expressed' lines per gene
    info = json.load(open(os.path.join(FXD, "info.json")))
    use_p = [i for i, p in enumerate(meta["plates"]) if p not in info.get("unreliable_plates", [])]
    qc = q["counts"][use_p][:, :, toks].sum(axis=0)            # L x C
    qt = q["total"][use_p].sum(axis=0)
    line_cpm = qc / qt[:, None] * 1e6
    expressed = (line_cpm >= 1.0) & (qc >= 20)
    fx, r1, r2, W2, zw, per, ddl, ddz = corrected_effects(counts, tot, nc, expressed)
    dd = fx.dd
    reg["pooled_cpm_quiet_wells"] = qc.sum(axis=0) / qt.sum() * 1e6
    reg["median_line_cpm"] = np.median(line_cpm, axis=0)
    reg["n_lines_expressing_ge1cpm"] = expressed.sum(axis=0)
    # untreated plate batch of each locus gene (quiet wells): median line CPM per plate, plates 1-3,14 vs 4-12
    pn = [meta["plates"][i] for i in use_p]
    cpm_p = q["counts"][use_p][:, :, toks] / q["total"][use_p][:, :, None] * 1e6       # P x L x C
    mlc = np.median(cpm_p, axis=1)                                                       # P x C
    hi = np.array([p_ in ("plate1", "plate2", "plate3", "plate14") for p_ in pn])
    reg["median_line_cpm_plates_1to3_14"] = np.median(mlc[hi], axis=0)
    reg["median_line_cpm_plates_4to12"] = np.median(mlc[~hi], axis=0)
    reg["plate_gap_log2_p1to3_14_vs_p4to12"] = (np.log2(mlc[hi] + 0.1).mean(axis=0) -
                                                np.log2(mlc[~hi] + 0.1).mean(axis=0))
    reg["median_line_cpm_plate6"] = mlc[pn.index("plate6")]
    reg["median_line_cpm_plate14"] = mlc[pn.index("plate14")]
    t_i = int(np.flatnonzero(reg["gene_symbol"].to_numpy() == "TRIM72")[0])
    raisers = [("Idarubicin (hydrochloride)", 5.0), ("Idarubicin (hydrochloride)", 0.5),
               ("Idarubicin (hydrochloride)", 0.05), ("Homoharringtonine", 5.0), ("Auranofin", 5.0),
               ("Dinaciclib", 5.0), ("Epirubicin (hydrochloride)", 5.0), ("Doxorubicin (hydrochloride)", 5.0),
               ("Topotecan (hydrochloride)", 5.0), ("Mitoxantrone (dihydrochloride)", 5.0), ("Harringtonine", 5.0),
               ("Panobinostat", 5.0)]
    long = []
    from scipy.stats import spearmanr
    for drug, conc in raisers:
        r = dd.index[(dd["drug"] == drug) & np.isclose(dd["conc"], conc)]
        if not len(r):
            continue
        d = int(r[0])
        for j in range(C):
            em = expressed[:, j]
            v = per[d, :, j]
            ok = em & np.isfinite(v)
            vt = per[d, :, t_i]
            ok2 = ok & expressed[:, t_i] & np.isfinite(vt)
            rho = spearmanr(v[ok2], vt[ok2])[0] if ok2.sum() >= 8 and j != t_i else np.nan
            long.append({"drug": drug, "conc": conc, "plates": dd.loc[d, "plates"], "gene": reg.loc[j, "label"],
                         "pooled_log2FC_corrected": ddl[d, j], "fold_change": 2 ** ddl[d, j], "z": ddz[d, j],
                         "median_per_line_log2FC_expressing": np.nanmedian(v[ok]) if ok.any() else np.nan,
                         "n_lines_expressing_measured": int(ok.sum()),
                         "n_lines_up_1.2x": int((v[ok] > np.log2(1.2)).sum()),
                         "n_lines_down_1.2x": int((v[ok] < -np.log2(1.2)).sum()),
                         "spearman_per_line_vs_TRIM72": rho, "n_lines_for_spearman": int(ok2.sum())})
    lg = pd.DataFrame(long)
    wide = reg[["label", "ensembl_id", "biotype", "start", "end", "strand", "rel_to_TRIM72", "same_strand_as_TRIM72",
                "distance_bp", "pooled_cpm_quiet_wells", "median_line_cpm", "n_lines_expressing_ge1cpm",
                "median_line_cpm_plates_1to3_14", "median_line_cpm_plates_4to12", "plate_gap_log2_p1to3_14_vs_p4to12",
                "median_line_cpm_plate6", "median_line_cpm_plate14"]].copy()
    # check: this re-implementation against the atlas's own corrected effects for the locus genes the atlas holds
    ag = pd.read_csv(os.path.join(FXD, "genes.csv"))
    ag = ag[ag["kind"] == "gene"]
    tok2col = dict(zip(ag["token"].astype(int), ag["col"].astype(int)))
    A_l = np.load(os.path.join(FXD, "DD_lfc.npy"), mmap_mode="r")
    A_z = np.load(os.path.join(FXD, "DD_z.npy"), mmap_mode="r")
    val = []
    for j, tk in enumerate(reg["token_id"].astype(int)):
        if tk in tok2col:
            al = np.asarray(A_l[:, tok2col[tk]], dtype=float)
            az = np.asarray(A_z[:, tok2col[tk]], dtype=float)
            m = np.isfinite(al) & np.isfinite(ddl[:, j])
            mz = np.isfinite(az) & np.isfinite(ddz[:, j])
            val.append({"gene": reg.loc[j, "label"], "n_drugdoses": int(m.sum()),
                        "pearson_r_log2FC_vs_atlas": float(np.corrcoef(al[m], ddl[m, j])[0, 1]),
                        "median_abs_diff_log2FC": float(np.median(np.abs(al[m] - ddl[m, j]))),
                        "max_abs_diff_log2FC": float(np.max(np.abs(al[m] - ddl[m, j]))),
                        "pearson_r_z_vs_atlas": float(np.corrcoef(az[mz], ddz[mz, j])[0, 1]),
                        "n_lines_expressing_here": int(expressed[:, j].sum()),
                        "n_lines_expressing_atlas": int(np.asarray(np.load(os.path.join(FXD, "expr_mask.npy"),
                                                                           mmap_mode="r")[:, tok2col[tk]]).sum())})
    pd.DataFrame(val).to_csv(os.path.join(TAB, "c_validation_locus_vs_atlas.csv"), index=False, float_format="%.4g")
    for drug, conc in raisers:
        x = lg[(lg["drug"] == drug) & (lg["conc"] == conc)].set_index("gene")
        if x.empty:
            continue
        tag = f"{drug.split(' ')[0]}_{conc:g}"
        wide[f"{tag}_log2FC"] = wide["label"].map(x["pooled_log2FC_corrected"])
        wide[f"{tag}_z"] = wide["label"].map(x["z"])
    # across drug-doses: does the neighbour's corrected effect track TRIM72's? (reliable drug-doses)
    okd = ~dd["unreliable_plate_only"].to_numpy() & ~dd["position_not_correctable"].to_numpy()
    rz, rl = [], []
    for j in range(C):
        a_, b_ = ddz[okd, j], ddz[okd, t_i]
        m = np.isfinite(a_) & np.isfinite(b_)
        rz.append(np.corrcoef(a_[m], b_[m])[0, 1] if m.sum() > 20 else np.nan)
        a_, b_ = ddl[okd, j], ddl[okd, t_i]
        m = np.isfinite(a_) & np.isfinite(b_)
        rl.append(spearmanr(a_[m], b_[m])[0] if m.sum() > 20 else np.nan)
    wide["r_z_with_TRIM72_over_drugdoses"] = rz
    wide["spearman_log2FC_with_TRIM72_over_drugdoses"] = rl
    a_path = os.path.join(TAB, "a_coreg_genomewide.csv")
    if os.path.exists(a_path):
        A_ = pd.read_csv(a_path, usecols=["gene", "r_z_raw", "r_z_minus_3pc", "pct_vs_matched_minus_3pc"],
                         low_memory=False).set_index("gene")
        for c_ in A_.columns:
            wide[f"atlas_{c_}"] = wide["label"].map(A_[c_])
    wide.to_csv(os.path.join(TAB, "c_locus_neighbours_effects.csv"), index=False, float_format="%.4g")
    lg.to_csv(os.path.join(TAB, "c_locus_neighbours_effects_long.csv"), index=False, float_format="%.4g")
    # per line, both idarubicin 5 uM wells: CPM in the well, plate baseline CPM, corrected r2, for key genes
    key = ["FUS", "PYCARD-AS1", "PYCARD", "TRIM72", "PYDC1", "ITGAM", "ITGAX", "KAT8", "BCKDK", "PRSS8", "PRSS36",
           "ZNF646", "VKORC1", "STX4", "ENSG00000260304", "ENSG00000310348"]
    w = fx.wells
    rows = []
    for smp in ("smp_2010", "smp_2778"):
        i = int(np.flatnonzero(w["sample"].to_numpy() == smp)[0])
        p = w.loc[i, "plate"]
        prow = np.flatnonzero((w["plate"] == p).to_numpy() & fx.drug_w)
        for l_ in range(L):
            rec = {"sample": smp, "plate": p, "cell_line_id": lines[l_],
                   "cell_name": fx.lines.loc[l_, "cell_name"], "n_cells": nc[i, l_], "total_counts": tot[i, l_]}
            for j in range(C):
                lab = reg.loc[j, "label"]
                if lab not in key:
                    continue
                cpm_w = counts[i, l_, j] / max(tot[i, l_], 1) * 1e6
                base = np.nanmedian(counts[prow, l_, j] / np.maximum(tot[prow, l_], 1) * 1e6)
                rec[f"{lab}_counts"] = counts[i, l_, j]
                rec[f"{lab}_cpm"] = cpm_w
                rec[f"{lab}_plate_median_cpm"] = base
                rec[f"{lab}_r2"] = r2[i, l_, j] if expressed[l_, j] else np.nan
            rows.append(rec)
    pl = pd.DataFrame(rows)
    pl.to_csv(os.path.join(TAB, "c_idarubicin5_per_line_locus.csv"), index=False, float_format="%.4g")
    # tests: is the induced TRIM72 level set by TRIM72's own baseline, or by FUS (readthrough source)?
    tests = []
    for smp in ("smp_2010", "smp_2778"):
        x = pl[(pl["sample"] == smp) & (pl["n_cells"] >= 30)].copy()
        x = x[x["TRIM72_plate_median_cpm"] > 0]
        gain = x["TRIM72_cpm"] - x["TRIM72_plate_median_cpm"]
        for nm, other in (("TRIM72 plate-baseline CPM", x["TRIM72_plate_median_cpm"]),
                          ("FUS CPM in the idarubicin well", x["FUS_cpm"]),
                          ("FUS plate-baseline CPM", x["FUS_plate_median_cpm"]),
                          ("PYCARD-AS1 CPM in the idarubicin well", x.get("PYCARD-AS1_cpm")),
                          ("ITGAM CPM in the idarubicin well", x.get("ITGAM_cpm")),
                          ("PYCARD CPM in the idarubicin well", x.get("PYCARD_cpm"))):
            if other is None:
                continue
            rho, p = spearmanr(gain, other)
            tests.append({"well": smp, "test": f"per line: TRIM72 CPM gained (idarubicin well - plate median) vs {nm}",
                          "n_lines": len(x), "spearman_rho": rho, "p": p})
        rho, p = spearmanr(x["TRIM72_cpm"], x["TRIM72_plate_median_cpm"])
        tests.append({"well": smp, "test": "per line: TRIM72 CPM in the idarubicin well vs its plate-baseline CPM",
                      "n_lines": len(x), "spearman_rho": rho, "p": p,
                      "median_TRIM72_cpm_well": x["TRIM72_cpm"].median(),
                      "median_TRIM72_cpm_plate_baseline": x["TRIM72_plate_median_cpm"].median()})
        for g_ in ("FUS", "PYCARD-AS1", "PYCARD", "PYDC1", "ITGAM", "KAT8", "BCKDK"):
            if f"{g_}_cpm" in x:
                s_tot = x["total_counts"].sum()
                tests.append({"well": smp, "test": f"pooled over lines: {g_} counts / TRIM72 counts in the well",
                              "n_lines": len(x), "ratio": x[f"{g_}_counts"].sum() / max(x["TRIM72_counts"].sum(), 1),
                              "pooled_cpm_well": 1e6 * x[f"{g_}_counts"].sum() / s_tot,
                              "pooled_cpm_plate_baseline": float((x[f"{g_}_plate_median_cpm"] *
                                                                  x["total_counts"]).sum() / s_tot)})
    pd.DataFrame(tests).to_csv(os.path.join(TAB, "c_idarubicin5_locus_tests.csv"), index=False, float_format="%.4g")
    log("(c) locus done")


def step_c_genome_in_wells():
    """Line-matched observed / expected counts of every gene in each raiser well (full profiles from prep):
    expected = sum over lines (>= 30 cells) of the well's line total x the line's CPM in the plate's quiet wells.
    Ranks TRIM72 and its neighbours among all genes and among genes of similar level, gives the reads added (O - E,
    CPM of the well), a strand summary of the locus, and, per line, whose gain tracks TRIM72's gain."""
    log("(c) genome-wide O/E in the raiser wells")
    from scipy.stats import rankdata
    meta, q = load_prep()
    f = np.load(os.path.join(CACHE, "raiser_wells_full.npz"))
    plates = meta["plates"]
    sm = pd.read_csv(os.path.join(DATA, "atlas", "sample_map.csv"), dtype={"sample": str}).set_index("sample")
    gm = gene_meta()
    sym = pd.Series(gm["gene_symbol"].values, index=gm["token_id"].values)
    reg = locus_table()
    loc = reg.dropna(subset=["token_id"])
    loc_tok = {int(t): l for t, l in zip(loc["token_id"], loc["label"])}
    loc_info = loc.set_index(loc["token_id"].astype(int))[["start", "strand", "rel_to_TRIM72", "distance_bp"]]
    fus_end = int(reg.loc[reg["label"] == "FUS", "end"].iloc[0])
    g = atlas_genes_with_coords()
    Xc = dog_exposure(g)
    cls = dict(zip(Xc["token"].astype(int), Xc["class"]))
    qc_all = q["counts"].astype(np.float64)
    lvl = 1e6 * qc_all.sum(axis=(0, 1)) / q["total"].sum()
    t_tok = int(gm.loc[gm["gene_symbol"] == "TRIM72", "token_id"].iloc[0])
    rows, summ, strand_rows, gain_cols = [], [], [], {}
    for k, smp in enumerate(f["samples"]):
        p = sm.loc[str(smp), "plate"]
        pi = plates.index(p)
        cnt = f["counts"][k].astype(np.float64)          # L x G
        tw = f["total"][k]
        okl = f["cells"][k] >= 30
        base = qc_all[pi] / q["total"][pi][:, None]       # L x G fraction in the plate's quiet wells
        O = cnt[okl].sum(axis=0)
        E = (tw[okl][:, None] * base[okl]).sum(axis=0)
        ok = (E >= 5)
        lr = np.log2((O + 0.5) / (E + 0.5))
        df = pd.DataFrame({"token": np.arange(len(O)), "gene": sym.reindex(np.arange(len(O))).values, "observed": O,
                           "expected": E, "log2_obs_over_exp": lr, "added_cpm": 1e6 * (O - E) / tw[okl].sum(),
                           "pooled_cpm": lvl})
        df = df[ok & df["gene"].notna()].copy()
        med_all = df["log2_obs_over_exp"].median()
        df["log2_OE_minus_well_median_gene"] = df["log2_obs_over_exp"] - med_all
        df["rank_desc_all"] = df["log2_obs_over_exp"].rank(ascending=False).astype(int)
        df["lvl_bin"] = np.floor(np.log2(df["pooled_cpm"].clip(1e-3)))
        df["pct_within_level_bin"] = df.groupby("lvl_bin")["log2_obs_over_exp"].rank(pct=True) * 100
        df["DoG_class"] = df["token"].map(cls).fillna("not in atlas")
        lab = RAISERS[str(smp)]
        # locus genes: all of them (also those with E < 5, flagged), so the strand picture is complete
        for t_, nm in loc_tok.items():
            r = df[df["token"] == t_]
            rec = {"well": lab, "sample": str(smp), "gene": nm, "start": loc_info.loc[t_, "start"],
                   "strand": loc_info.loc[t_, "strand"], "rel_to_TRIM72": loc_info.loc[t_, "rel_to_TRIM72"],
                   "distance_bp": loc_info.loc[t_, "distance_bp"], "observed": O[t_], "expected": E[t_],
                   "expected_ge_5": bool(E[t_] >= 5), "log2_obs_over_exp": lr[t_],
                   "log2_OE_minus_well_median_gene": lr[t_] - med_all,
                   "added_cpm": 1e6 * (O[t_] - E[t_]) / tw[okl].sum(), "pooled_cpm": lvl[t_]}
            if len(r):
                rec.update({"rank_of_genes": int(r.iloc[0]["rank_desc_all"]), "n_genes": len(df),
                            "pct_within_level_bin": r.iloc[0]["pct_within_level_bin"]})
            rows.append(rec)
        lw = pd.DataFrame([x for x in rows if x["sample"] == str(smp)])
        lw = lw[lw["expected_ge_5"]]
        downstream_plus = (lw["strand"] == 1) & (lw["start"] > fus_end) & (lw["gene"] != "TRIM72")
        minus_win = (lw["strand"] == -1) & (lw["start"] > fus_end)
        upstream = lw["start"] < fus_end
        tr = lw[lw["gene"] == "TRIM72"]
        strand_rows.append({
            "well": lab, "sample": str(smp), "well_median_gene_log2OE": med_all,
            "TRIM72_log2OE": float(tr["log2_obs_over_exp"].iloc[0]) if len(tr) else np.nan,
            "FUS_log2OE": float(lw.loc[lw["gene"] == "FUS", "log2_obs_over_exp"].iloc[0]),
            "plus_strand_downstream_of_FUS_genes": ", ".join(lw.loc[downstream_plus, "gene"]),
            "plus_strand_downstream_of_FUS_median_log2OE": lw.loc[downstream_plus, "log2_obs_over_exp"].median(),
            "minus_strand_downstream_of_FUS_genes": ", ".join(lw.loc[minus_win, "gene"]),
            "minus_strand_downstream_of_FUS_median_log2OE": lw.loc[minus_win, "log2_obs_over_exp"].median(),
            "genes_upstream_of_FUS_end": ", ".join(lw.loc[upstream, "gene"]),
            "upstream_of_FUS_median_log2OE": lw.loc[upstream, "log2_obs_over_exp"].median(),
            "added_cpm_PYCARD-AS1": float(lw.loc[lw["gene"] == "PYCARD-AS1", "added_cpm"].sum()),
            "added_cpm_TRIM72": float(tr["added_cpm"].iloc[0]) if len(tr) else np.nan,
            "added_cpm_ITGAM": float(lw.loc[lw["gene"] == "ITGAM", "added_cpm"].sum()),
            "added_cpm_FUS": float(lw.loc[lw["gene"] == "FUS", "added_cpm"].sum())})
        low = df["pooled_cpm"].between(1, 10)
        summ.append({"well": lab, "sample": str(smp), "n_genes_E_ge_5": len(df),
                     "median_log2OE_all": med_all,
                     "median_log2OE_genes_1to10cpm": df.loc[low, "log2_obs_over_exp"].median(),
                     "median_log2OE_low_sense_exposed": df.loc[low & (df["DoG_class"] == "sense_exposed"),
                                                               "log2_obs_over_exp"].median(),
                     "median_log2OE_low_unexposed": df.loc[low & (df["DoG_class"] == "unexposed"),
                                                           "log2_obs_over_exp"].median(),
                     "median_log2OE_low_antisense_exposed": df.loc[low & (df["DoG_class"] == "antisense_exposed_only"),
                                                                   "log2_obs_over_exp"].median(),
                     "TRIM72_log2OE": float(lr[t_tok]), "TRIM72_rank_of_genes": int(df.loc[df["token"] == t_tok,
                                                                                          "rank_desc_all"].iloc[0]),
                     "TRIM72_pct_within_level_bin": float(df.loc[df["token"] == t_tok, "pct_within_level_bin"].iloc[0])})
        # per line: CPM gained in this well over the plate's quiet wells; which genes' gains track TRIM72's
        if lab.startswith(("Idarubicin 5", "Homoharringtonine 5")):
            cols = df["token"].to_numpy()
            gain = 1e6 * (cnt[okl][:, cols] / tw[okl][:, None] - base[okl][:, cols])      # lines x genes
            R = rankdata(gain, axis=0)
            R = R - R.mean(axis=0)
            sd = np.sqrt((R ** 2).sum(axis=0))
            rt_ = R[:, list(cols).index(t_tok)]
            rho = (rt_ @ R) / np.where(sd > 0, sd, np.nan) / np.sqrt((rt_ ** 2).sum())
            gain_cols[lab] = pd.Series(rho, index=cols)
            gain_cols[lab + " n_lines"] = int(okl.sum())
    lt = pd.DataFrame(rows)
    lt.to_csv(os.path.join(TAB, "c_locus_obs_over_exp_raiser_wells.csv"), index=False, float_format="%.4g")
    pd.DataFrame(summ).to_csv(os.path.join(TAB, "c_raiser_wells_genomewide_OE_summary.csv"), index=False,
                              float_format="%.4g")
    pd.DataFrame(strand_rows).to_csv(os.path.join(TAB, "c_locus_strand_summary_raiser_wells.csv"), index=False,
                                     float_format="%.4g")
    # per-line gain correlation with TRIM72, genome-wide
    wl = [k_ for k_ in gain_cols if not k_.endswith("n_lines")]
    G = pd.concat({k_: gain_cols[k_] for k_ in wl}, axis=1)
    G.columns = [f"rho_gain_vs_TRIM72_gain: {c_}" for c_ in G.columns]
    G.insert(0, "gene", sym.reindex(G.index).values)
    G.insert(1, "pooled_cpm", lvl[G.index.to_numpy()])
    G.insert(2, "DoG_class", pd.Series(G.index).map(cls).fillna("not in atlas").values)
    ida = [c_ for c_ in G.columns if "Idarubicin 5" in c_]
    G["rho_mean_idarubicin_5uM_wells"] = G[ida].mean(axis=1)
    G = G[G.index != t_tok].dropna(subset=["rho_mean_idarubicin_5uM_wells"])
    G["rank_idarubicin"] = G["rho_mean_idarubicin_5uM_wells"].rank(ascending=False).astype(int)
    G["pct_idarubicin_within_level_2x"] = np.nan
    lv = np.log2(G["pooled_cpm"].clip(1e-3).to_numpy())
    vals = G["rho_mean_idarubicin_5uM_wells"].to_numpy()
    for t_, nm in loc_tok.items():
        if t_ in G.index:
            i_ = G.index.get_loc(t_)
            m = np.abs(lv - lv[i_]) <= 1
            G.iloc[i_, G.columns.get_loc("pct_idarubicin_within_level_2x")] = 100 * float((vals[m] < vals[i_]).mean())
    G["in_TRIM72_locus_200kb"] = G.index.isin(list(loc_tok))
    G.sort_values("rho_mean_idarubicin_5uM_wells", ascending=False).to_csv(
        os.path.join(TAB, "c_per_line_gain_corr_with_TRIM72_genomewide.csv"), index_label="token", float_format="%.4g")
    log("  per-line gain partners of TRIM72 (idarubicin 5 uM):",
        ", ".join(G.nlargest(12, "rho_mean_idarubicin_5uM_wells")["gene"].astype(str)))
    log("(c) O/E done")


def step_c():
    step_c_dog()
    step_c_locus()
    step_c_genome_in_wells()


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--steps", default="fetch,prep,a,b,c")
    a = ap.parse_args()
    ensure_dir(TAB)
    for st in a.steps.split(","):
        globals()["step_" + st.strip()]()
