"""Per-stage checks of a finished synthetic run against the generator's planted truth (used by run_tests.py).

run_all also calls the checks of the newer packages on the same output (design I5): tests/test_direction.py check(out)
(the reasons in tiers and the edge rules), tests/test_surfaces.py check(out, data) (links, map, vault and look-ups
that point into the explorer, and their second-wave texts) and tests/test_explorer.py check(out, data) (the explorer
stage: exact values, flags, records, completeness, planted answers, determinism, sizes).

wave2_checks follows every rule the second wave added to its planted answer (ground_truth.json): only atlas_core.py,
common.py and tests/test_port.py use atlas_core's flag list (a syntax-tree scan); clean = not common.has_artifact on
every table; the neighbouring-well tiers and their per-gene reading (W2 (a)-(f)), with the validation section, the
module drug lists and the direction drug-dose lists; the translation-inhibitor caveat (g), with the drug note's class
line and the validation words; the DMSO sign check (h), drug_line_response and selectivity (i), TP53 'not recorded'
(j), dose = plate (k), the annotations and classes (l), the tables README (m), the drug's annotation columns on
drugdoses.parquet and the validation README's word for the top-dose tier (n); the direction VERSION 5 rules D1-D17
(tests/test_direction.py v5_checks), the drug-target classes and the stage order; lineage pairs, counts in two units,
drug-dose similarity, covariates, partner preservation; the module labels and the report's new sections. A planted
effect the synthetic data make too small for its rule is a WARN that names it (a request to make the plant
stronger), never a silent pass."""

import json
import os
import pathlib
import re
import subprocess
import sys

import numpy as np
import pandas as pd

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OPPOSITE = [("HDAC_UP", "HDAC_DOWN"), ("COLOC_UP", "COLOC_DOWN"), ("COLOC2_UP", "COLOC2_DOWN")]
# planted sets that move under one drug-dose only (tests/make_synthetic_tahoe.py ONE_DOSE: Bergenin 5 uM in the
# TP53-wild-type lines): their vectors share little beyond that one context, so the tightness check reports them only
SINGLE_CONTEXT_SETS = ("ONE_DOSE",)


def _sets(truth):
    return truth["extra_not_in_panel_spec"]["synthetic gene sets"]


def run_all(out, data, truth, check):
    fx = os.path.join(out, "atlas", "effects")
    from tahoemap.common import read_effects_index
    ix = read_effects_index(fx)
    genes, dd, lines = ix["genes"], ix["drugdose"], ix["lines"]
    gK = int((genes["kind"] == "gene").sum())
    col = {s: int(c) for s, c in zip(genes["symbol"][:gK], genes["col"][:gK])}
    wt = {ln["cell_name"] for ln in truth["lines"] if str(ln.get("tp53", "")).lower() in ("wt", "wild type")}

    # ---------------------------------------------------------------- effects (the verbatim port)
    check("effects", "method v3 complete", lambda: (
        json.load(open(os.path.join(fx, "complete.json"), encoding="utf-8"))["version"] == 3,
        "complete.json version 3"))
    check("effects", "plate13 unreliable, failed well removed", lambda: (
        "plate13" in json.load(open(os.path.join(fx, "info.json"), encoding="utf-8")).get("unreliable_plates", []) and
        len(pd.read_csv(os.path.join(fx, "failed_wells.csv"))) >= 1,
        f"failed wells: {len(pd.read_csv(os.path.join(fx, 'failed_wells.csv')))}"))

    # ---------------------------------------------------------------- tensor
    def tensor_exact():
        info = json.load(open(os.path.join(out, "tensor", "info.json"), encoding="utf-8"))
        return (info["check_W1_max_diff"] <= 1e-5 and info["check_W2_max_diff"] <= 1e-5,
                f"reproduces the atlas: W1 {info['check_W1_max_diff']:.1e}, W2 {info['check_W2_max_diff']:.1e}")
    check("tensor", "per-line residuals reproduce the atlas exactly", tensor_exact)

    td = os.path.join(out, "tensor")
    DDL = np.load(os.path.join(td, "DDL_lfc.npy"), mmap_mode="r")
    DDZ = np.load(os.path.join(td, "DDL_z.npy"), mmap_mode="r")
    DD = np.load(os.path.join(fx, "DD_lfc.npy"))
    tinfo = json.load(open(os.path.join(td, "info.json"), encoding="utf-8"))
    LM = np.load(os.path.join(td, "line_measured.npy"))                     # lines x genes
    EM = np.load(os.path.join(fx, "expr_mask.npy"))[:, :gK]
    LCPM = np.load(os.path.join(fx, "line_cpm.npy"))[:, :gK]

    def median_matches():
        """Where the tensor masked nothing (no ambient-only line, every profile >= e_min expected counts), the median
        over lines of the per-line values is the atlas's pooled value."""
        one = np.flatnonzero(dd["n_wells"].to_numpy() == 1)
        wl = pd.read_csv(os.path.join(fx, "wells.csv"))
        w_of = {int(r): i for i, (r, u) in enumerate(zip(wl["drugdose_row"], wl["used_in_drugdose"]))
                if str(u).lower() in ("true", "1") and int(r) >= 0}
        w1 = np.array([w_of[d] for d in one])
        umi = np.load(os.path.join(td, "well_line_umi.npy"))[w1]                 # n1 x lines
        cells = np.load(os.path.join(td, "well_line_cells.npy"))[w1]
        prof = (cells >= tinfo["min_cells"])[:, :, None] & EM[None]           # profiles the atlas measured
        masked = (prof & (~LM[None] | (LCPM[None] * umi[:, :, None] / 1e6 < tinfo["e_min"]))).any(axis=1)
        with np.errstate(all="ignore"):
            import warnings
            warnings.simplefilter("ignore")
            med = np.nanmedian(np.asarray(DDL[:, one, :], dtype=np.float32), axis=2).T
        ref = DD[one][:, :gK]
        ok = np.isfinite(med) & np.isfinite(ref) & ~masked
        d = float(np.max(np.abs(med[ok] - ref[ok])))
        return d < 0.01 and ok.sum() > 0.3 * ok.size, (
            f"median over lines vs DD_lfc (single-well drug-doses, {int(ok.sum()):,} of {ok.size:,} values where "
            f"the tensor masked no line): max |diff| {d:.4f} (float16)")
    check("tensor", "per-line fold changes collapse to the atlas's", median_matches)

    def masks_applied():
        fin = np.isfinite(np.asarray(DDL, dtype=np.float32)).any(axis=1).T          # lines x genes: any value
        leak = int((fin & ~LM).sum())
        sub = bool((LM <= EM).all())
        rule = bool((LM == (EM & (LCPM >= tinfo["amb_frac"] * genes["pooled_cpm"].to_numpy()[:gK][None]))).all())
        return (leak == 0 and sub and rule and tinfo["n_ambient_line_gene_pairs"] > 0
                and tinfo["n_low_count_values"] >= 0,
                f"ambient-only (line, gene) pairs {tinfo['n_ambient_line_gene_pairs']:,}, low-count values masked "
                f"{tinfo['n_low_count_values']:,}; values where line_measured is False: {leak}; "
                f"line_measured within expr_mask {sub}, follows the rule {rule}")
    check("tensor", "ambient-only lines and low-count profiles are NaN", masks_applied)

    def il1b_ambient():
        grp = set(truth["groups"].get("il1b_expressing", []))
        names = lines["cell_name"].to_numpy()
        c = col["IL1B"]
        meas = {n for n, v in zip(names, LM[:, c]) if v}
        atlas = {n for n, v in zip(names, EM[:, c]) if v}
        return (meas == grp, f"IL1B (made only by {sorted(grp)}): measured in {sorted(meas)}; the atlas's "
                             f"expr_mask also lets through {sorted(atlas - grp)}")
    if "IL1B" in col:
        check("tensor", "a gene made by few lines is measured only in those (ambient rule)", il1b_ambient)

    def p53_lines():
        c = col["CDKN1A"]
        rows = dd.index[dd["drug"].str.startswith("Doxorubicin") & (dd["dose"] == "5")]
        d = int(rows[0])
        z = np.asarray(DDZ[c, d, :], dtype=float)
        names = lines["cell_name"].to_numpy()
        up = {n for n, v in zip(names, z) if np.isfinite(v) and v >= 2}
        bad = up - wt
        return (len(up) >= 2 and not bad,
                f"CDKN1A up (z>=2) under doxorubicin 5 uM in {sorted(up)}; not TP53-WT among them: {sorted(bad)}")
    check("tensor", "p53 targets rise only in TP53-wild-type lines", p53_lines)

    # ---------------------------------------------------------------- tables
    tb = os.path.join(out, "tables")
    if os.path.exists(os.path.join(tb, "genes.parquet")):
        g = pd.read_parquet(os.path.join(tb, "genes.parquet"))
        de = pd.read_parquet(os.path.join(tb, "drug_effects.parquet"))

        def best(sym, prefix_list, direction="up"):
            r = g[g["symbol"] == sym].iloc[0]
            drug = str(r[f"best_clean_{direction}_drug"])
            return any(drug.lower().startswith(p.lower()) for p in prefix_list), \
                f"{sym}: best clean {direction} = {drug} {r[f'best_clean_{direction}_dose']}"
        # the TOP2-poison plant (W1) raises the p53 genes under Amsacrine, Epirubicin, Idarubicin and Mitoxantrone
        # too: on another seed one of them can be CDKN1A's best clean raiser
        check("tables", "CDKN1A best clean raiser is a DNA-damage drug",
              lambda: best("CDKN1A", ["Doxorubicin", "Topotecan", "5-Fluorouracil", "Fluorouracil", "Amsacrine",
                                      "Epirubicin", "Idarubicin", "Mitoxantrone"]))
        check("tables", "HMOX1 best clean raiser is an NRF2 / proteotoxic drug",
              lambda: best("HMOX1", ["Dimethyl fumarate", "Auranofin", "Bortezomib"]))

        def ftl_down():
            rows = de[(de["symbol"].isin(["FTH1", "FTL"])) & (de["clean"]) & (de["lfc"] < 0)]
            top = rows.sort_values("z").groupby("symbol").head(3)
            hit = top["drug"].str.startswith("Ciclopirox").groupby(top["symbol"]).any()
            return bool(hit.all()) and len(hit) == 2, f"Ciclopirox among the top-3 clean lowerers: {hit.to_dict()}"
        check("tables", "FTH1 / FTL lowered by ciclopirox", ftl_down)
        check("tables", "line_effects has every gene x line", lambda: (
            len(pd.read_parquet(os.path.join(tb, "line_effects.parquet"), columns=["col"])) == gK * len(lines),
            f"{gK} genes x {len(lines)} lines"))

        tinfo_t = json.load(open(os.path.join(tb, "info.json"), encoding="utf-8"))
        le = pd.read_parquet(os.path.join(tb, "line_effects.parquet"))
        dlt = pd.read_parquet(os.path.join(tb, "drug_line_top.parquet"))
        t = float(tinfo_t["line_z_threshold"])

        def line_cut_used():
            e = tinfo_t["line_z_expected_chance"]
            up, dn = le[le["best_up_dd"] >= 0], le[le["best_down_dd"] >= 0]
            ok = (t >= 4 and e is not None and e <= 0.05 and abs(tinfo_t["line_fold_min"] - np.log2(1.5)) < 1e-9
                  and bool((up["best_up_z"] >= t).all()) and bool((dn["best_down_z"] <= -t).all())
                  and bool((up["best_up_lfc"] >= np.log2(1.5) - 1e-6).all())
                  and bool(((le["n_dd_up"] > 0) == (le["best_up_dd"] >= 0)).all())
                  and bool(((le["n_dd_down"] > 0) == (le["best_down_dd"] >= 0)).all())
                  and bool((dlt["z"].abs() >= t).all()))
            return ok, (f"line_z_threshold {t:g} (expected chance per gene x line {e:.3g}; null P(|z|>=3) "
                        f"{tinfo_t['line_z_null_tail'].get('3')}, >=4 {tinfo_t['line_z_null_tail'].get('4')}); "
                        f"best_* and drug_line_top all beyond it; {len(dlt):,} drug_line_top rows")
        check("tables", "per-line |z| cut is calibrated and used", line_cut_used)

        def null_genes_line_calls():
            moved = set()
            for v in _sets(truth).values():
                moved |= set(v)
            nullc = [col[s] for s in col if s.startswith("SYNTH") and s not in moved]
            sub = le[le["col"].isin(nullc) & le["expressed"]]
            rate = float((sub["n_dd_up"] + sub["n_dd_down"]).mean()) if len(sub) else float("nan")
            return (True if rate <= 0.1 else "warn"), (
                f"un-planted genes: {rate:.3f} per-line calls per (gene, line) over the clean drug-doses "
                f"(calibrated expectation {tinfo_t['line_z_expected_chance']:.3f}; {len(sub):,} gene x line rows)")
        check("tables", "un-planted genes rarely pass the per-line cut", null_genes_line_calls)

        def p53_line_top():
            c = col["CDKN1A"]
            r = dlt[(dlt["col"] == c) & (dlt["direction"] == "up") & dlt["drug"].str.startswith(
                ("Doxorubicin", "Topotecan", "5-Fluorouracil"))]
            bad = sorted(set(r["cell_name"]) - wt)
            return (len(r) >= 1 and not bad,
                    f"CDKN1A up in drug_line_top under DNA-damage drugs: {len(r)} cells in "
                    f"{sorted(set(r['cell_name']))}; not TP53-WT: {bad}")
        check("tables", "per-line p53 response is in drug_line_top, TP53-WT lines only", p53_line_top)

        def expressed_is_measured():
            M = LM.T.ravel()                                      # gene-major, as line_effects
            return (bool((le.sort_values(["col", "line"])["expressed"].to_numpy() == M).all())
                    and bool((g["n_lines_expressing"].to_numpy() == LM.sum(axis=0)).all()),
                    f"line_effects expressed == tensor line_measured ({int(M.sum()):,} of {M.size:,}); "
                    "genes.n_lines_expressing counts it")
        check("tables", "'expressed' is the tensor's line_measured", expressed_is_measured)

        def depleted_counts():
            lt = pd.read_parquet(os.path.join(tb, "lines.parquet"))
            ga = lt["in_growth_analysis"].astype(str).str.lower().isin(["true", "1"]).to_numpy()
            Az = np.load(os.path.join(fx, "DD_Az.npy"))
            from tahoemap.common import ARTIFACT_FLAGS
            from tahoemap.tables import dd_flags_of_record
            fl = [set(str(f).split("; ")) for f in dd_flags_of_record(out)]      # the flags of record
            untrusted = np.array([bool(f & {"unreliable plate only", "position not correctable", "wells disagree"})
                                  for f in fl])
            art = np.array([bool(f & set(ARTIFACT_FLAGS)) for f in fl])
            meas = ga & np.isfinite(Az).any(axis=0)
            exp_all = np.where(meas, ((Az <= -3) & ~untrusted[:, None]).sum(axis=0), -1)
            exp_cln = np.where(meas, ((Az <= -3) & ~art[:, None]).sum(axis=0), -1)
            ok = (bool((lt["n_dd_depleted"].to_numpy() == exp_all).all())
                  and bool((lt["n_dd_depleted_clean"].to_numpy() == exp_cln).all())
                  and bool((lt["n_dd_depleted"] >= lt["n_dd_depleted_clean"]).all()))
            return ok, (f"lines not in the growth analysis (-> -1): {int((~ga).sum())}; depleting drug-doses summed "
                        f"over lines: {int(exp_all[meas].sum())} (artifact-flagged ones but untrusted counts "
                        f"included), {int(exp_cln[meas].sum())} clean (flags of record, common.ARTIFACT_FLAGS: "
                        f"{int(art.sum())} artifact drug-doses)")
        check("tables", "lines.n_dd_depleted: abundance-trusted drug-doses, -1 = not measured", depleted_counts)

    # ---------------------------------------------------------------- embed
    ed = os.path.join(out, "embed")
    U = np.load(os.path.join(ed, "gene_unit.npy"))
    sets = _sets(truth)

    def mean_cos(a, b):
        A = U[[col[s] for s in a if s in col]]
        B = U[[col[s] for s in b if s in col]]
        A, B = A[np.isfinite(A).all(1)], B[np.isfinite(B).all(1)]
        C = A @ B.T
        if a is b:
            C = C[~np.eye(len(A), dtype=bool)]
        return float(np.mean(C)) if C.size else float("nan")

    def modules_cohere():
        """Each planted set of >= 8 genes is tight (mean within-set cosine >= 0.35), except COMPOSITION and the sets
        planted at one drug-dose only (SINGLE_CONTEXT_SETS: ONE_DOSE moves under Bergenin 5 uM in 8 lines, so its
        vectors share little beyond that one context; W1 measured 0.33): those are reported, not judged."""
        res = {k: round(mean_cos(v, v), 2) for k, v in sets.items() if len(v) >= 8 and k != "COMPOSITION"}
        weak = {k: v for k, v in res.items() if not v >= 0.35 and k not in SINGLE_CONTEXT_SETS}
        one = {k: v for k, v in res.items() if k in SINGLE_CONTEXT_SETS}
        return not weak, (f"within-module mean cosine {({k: v for k, v in res.items() if k not in one})}; planted at "
                          f"one drug-dose only (not judged): {one}")
    check("embed", "planted modules are tight in the vector space", modules_cohere)

    def random_flat():
        inc = np.flatnonzero(np.isfinite(U).all(1))
        rng = np.random.default_rng(0)
        a, b = rng.choice(inc, 3000), rng.choice(inc, 3000)
        m = float(np.mean(np.einsum("ij,ij->i", U[a], U[b])))
        return abs(m) < 0.05, f"random pairs mean cosine {m:+.3f}"
    check("embed", "random gene pairs are unrelated", random_flat)

    def opposite_vectors():
        res = {f"{a}/{b}": round(mean_cos(sets[a], sets[b]), 2) for a, b in OPPOSITE}
        return all(v <= -0.4 for v in res.values()), f"cross-module cosine {res}"
    check("embed", "opposite modules point opposite ways", opposite_vectors)

    # ---------------------------------------------------------------- relations
    rel = pd.read_parquet(os.path.join(out, "relations", "gene_relations.parquet"))

    def nrf2_partners():
        """the planted NRF2 programme: NRF2_CORE and, since the direction plants, the SYNTH NRF2 targets NRF2_EXT
        (they respond to the same activators as the core by construction, so they are HMOX1's partners too)"""
        nrf2 = set(truth["gene_sets"].get("NRF2_CORE", [])) if isinstance(truth.get("gene_sets"), dict) else set()
        ext = set(sets.get("NRF2_EXT", []))
        top = rel[(rel["symbol_a"] == "HMOX1") & (rel["cos"] > 0)].nsmallest(10, "rank")["symbol_b"].tolist()
        hit = [s for s in top if s in nrf2 | ext]
        return len(hit) >= 5, (f"HMOX1's top 10 positive partners: {top}; planted NRF2 targets among them: "
                               f"{len(hit)} ({sum(s in nrf2 for s in hit)} of NRF2_CORE, "
                               f"{sum(s in ext for s in hit)} of NRF2_EXT)")
    check("relations", "HMOX1 moves with the NRF2 core", nrf2_partners)

    def fdr_monotone():
        c = pd.read_csv(os.path.join(out, "relations", "fdr_curve.csv"))
        mono = bool(np.all(np.diff(c["fdr"].to_numpy()) <= 1e-12))
        at5 = c.loc[(c["t"] - 0.5).abs().idxmin(), "fdr"]
        return mono and at5 < 0.1, f"monotone {mono}; FDR at half-cos 0.5 = {at5:.3f}"
    check("relations", "sign-concordance FDR is calibrated and monotone", fdr_monotone)

    def null_genes_quiet():
        moved = set()
        for v in sets.values():
            moved |= set(v)
        nullg = [s for s in col if s.startswith("SYNTH") and s not in moved]
        r = rel[(rel["col_a"] < rel["col_b"]) & (rel["fdr"] <= 0.05) & (rel["abs_cos"] >= 0.5)]
        both_null = r["symbol_a"].isin(nullg) & r["symbol_b"].isin(nullg)
        frac = float(both_null.mean()) if len(r) else 0.0
        return ("warn" if frac > 0.1 else True), \
            f"strong reproducible pairs: {len(r)}; between two un-planted genes: {int(both_null.sum())} ({frac:.1%})"
    check("relations", "un-planted genes rarely form strong relations", null_genes_quiet)

    # ---------------------------------------------------------------- graph (the user's two maps)
    nodes = pd.read_parquet(os.path.join(out, "graph", "nodes.parquet"))
    mod = dict(zip(nodes["symbol"], nodes["module"]))
    arm = dict(zip(nodes["symbol"], nodes["arm"]))

    def same_module_opposite_arms():
        out_ = {}
        ok = True
        for a, b in OPPOSITE:
            ma = pd.Series([mod.get(s) for s in sets[a]]).mode()[0]
            mb = pd.Series([mod.get(s) for s in sets[b]]).mode()[0]
            aa = pd.Series([arm.get(s) for s in sets[a]]).mode()[0]
            ab = pd.Series([arm.get(s) for s in sets[b]]).mode()[0]
            out_[f"{a}/{b}"] = f"modules {ma}/{mb} arms {aa}/{ab}"
            ok &= (ma == mb) and (aa != ab) and ma != 0
        return ok, out_
    check("graph", "opposite modules share a module, on opposite arms", same_module_opposite_arms)

    def maps_differ():
        """t-SNE keeps neighbourhoods, not long distances: how far apart two separate islands of the signed map land
        varies from machine to machine (tiny floating-point differences: the COLOC pair's centroid distance ranges
        0.4-2.0 map spreads under 1e-6 perturbations of the input). What is stable, and what the maps promise, is the
        mixing: on the nodal map the two sets share neighbourhoods; on the signed map no gene of one set has a gene
        of the other among its nearest map neighbours (validate.map_mixing; 1 = as mixed as chance, 0 = apart)."""
        from tahoemap.validate import map_mixing
        res, ok = {}, True
        sx = np.linalg.norm(nodes[["x", "y"]].std().to_numpy())
        ss = np.linalg.norm(nodes[["xs", "ys"]].std().to_numpy())
        xy, xys = nodes[["x", "y"]].to_numpy(float), nodes[["xs", "ys"]].to_numpy(float)
        for a, b in OPPOSITE:
            ia = np.flatnonzero(nodes["symbol"].isin(sets[a]).to_numpy())
            ib = np.flatnonzero(nodes["symbol"].isin(sets[b]).to_numpy())
            dn = np.linalg.norm(xy[ia].mean(0) - xy[ib].mean(0)) / sx
            ds = np.linalg.norm(xys[ia].mean(0) - xys[ib].mean(0)) / ss
            mn, ms = map_mixing(xy, ia, ib), map_mixing(xys, ia, ib)
            res[f"{a}/{b}"] = f"nodal: centroid {dn:.2f}, mixing {mn:.2f}; signed: centroid {ds:.2f}, mixing {ms:.2f}"
            ok &= dn < 0.3 and mn >= 0.5 and ms <= 0.1
        return ok, f"centroid distance / map spread, and neighbourhood mixing: {res}"
    check("graph", "opposite genes: together on the nodal map, apart on the signed map", maps_differ)

    # ---------------------------------------------------------------- direction
    direction_checks(out, truth, check, col)

    # ---------------------------------------------------------------- validate
    vd = os.path.join(out, "validation")
    if os.path.exists(os.path.join(vd, "metrics.json")):
        check("validate", "report written", lambda: (
            os.path.getsize(os.path.join(vd, "report.md")) > 1000,
            f"{os.path.getsize(os.path.join(vd, 'report.md'))} bytes"))

    # ---------------------------------------------------------------- vault
    vt = os.path.join(out, "vault")
    if os.path.isdir(vt):
        def vault_links():
            names, links = {}, []
            for root, _d, files in os.walk(vt):
                if ".obsidian" in root:
                    continue
                for f in files:
                    if f.endswith((".md", ".canvas")):
                        names[os.path.splitext(f)[0].lower()] = os.path.join(root, f)
            for p in names.values():
                if p.endswith(".md"):
                    links += [(p, m) for m in re.findall(r"\[\[([^\]|#]+)", open(p, encoding="utf-8").read())]
            def target(m):
                m = m.strip()
                return os.path.splitext(m)[0] if m.lower().endswith((".md", ".canvas")) else m
            bad = [(os.path.basename(p), m) for p, m in links if target(m).lower() not in names]
            n_gene = sum(1 for p in names.values() if f"{os.sep}Genes{os.sep}" in p and "plates" not in p)
            return (not bad and n_gene >= gK,
                    f"{len(names)} notes ({n_gene} gene notes), {len(links)} links, unresolved: {bad[:5]}")
        check("vault", "a note per gene and no unresolved links", vault_links)
        check("vault", "direction sections: gene, drug and line notes, the concept note, an output without the stage",
              lambda: vault_direction(out, col, gK, _planted_null(data)))

    # ---------------------------------------------------------------- map
    html = os.path.join(out, "map", "gene_map.html")
    if os.path.exists(html):
        check("map", "self-contained HTML map", lambda: (
            os.path.getsize(html) > 10_000 and "http" not in re.sub(r"https?://[^\s\"']*(uniprot|ncbi|ensembl|"
                                                                       r"genenames)[^\s\"']*", "",
                                                                       open(html, encoding="utf-8").read()[:2000]),
            f"{os.path.getsize(html) / 1e6:.1f} MB"))

        def map_data():
            txt = open(html, encoding="utf-8").read()
            m = re.search(r'<script id="tm-data" type="application/json">(.*?)</script>', txt, re.S)
            return txt, json.loads(m.group(1))

        def map_tabs_and_edges():
            """the seven tabs exist; the embedded graph edges are graph/edges.parquet between two map genes"""
            import base64
            txt, D = map_data()
            tabs = re.findall(r'data-tab="(\w+)"', txt)
            e, n = D["edges"], D["n"]
            dt = "<u2" if e["bytes"] == 2 else "<u4"
            a, b = (np.frombuffer(base64.b64decode(e[k]), dtype=dt).astype(np.int64) for k in ("a", "b"))
            c = np.frombuffer(base64.b64decode(e["cos"]), dtype=np.int8) / 100
            ev = np.frombuffer(base64.b64decode(e["ev"]), dtype=np.uint8)
            ge = pd.read_parquet(os.path.join(out, "graph", "edges.parquet"))
            ent = {cc: i for i, cc in enumerate(D["col"][:n])}
            want = {}
            for ca, cb, cc in zip(ge["col_a"], ge["col_b"], ge["cos"]):
                if ca in ent and cb in ent and ent[ca] != ent[cb]:
                    k = (min(ent[ca], ent[cb]), max(ent[ca], ent[cb]))
                    if k not in want or abs(cc) > abs(want[k]):
                        want[k] = float(cc)
            got = {(int(x), int(y)): float(z) for x, y, z in zip(a, b, c)}
            err = max((abs(got[k] - v) for k, v in want.items() if k in got), default=1.0)
            ok = (tabs == ["nodal", "signed", "tour", "nbr", "mod", "all", "help"] and e["m"] == len(a) == len(want)
                  and set(got) == set(want) and err <= 0.0051 and bool((a < b).all()) and int(b.max()) < n
                  and set(np.unique(ev).tolist()) <= {0, 1, 2})
            return ok, (f"tabs {tabs}; {e['m']:,} edges embedded ({len(want):,} in graph/edges.parquet between map "
                        f"genes), max |cos error| {err:.4f}, evidence codes {sorted(np.unique(ev).tolist())}, "
                        f"{sum(len(e[k]) for k in ('a', 'b', 'cos', 'ev')) / 1e3:.0f} kB")
        check("map", "tabs, and the graph edges for the physics tabs", map_tabs_and_edges)

        def map_physics():
            """in a headless browser (when Playwright and its Chromium are installed): no script errors on any tab;
            the module tab holds the planted HDAC module; flipping 'opposite genes repel' parts its two arms"""
            try:
                from playwright.sync_api import sync_playwright
            except ImportError:
                return "warn", ("Playwright not installed: browser check skipped (optional: pip install playwright, "
                                "then python -m playwright install chromium)")
            up, dn = set(sets["HDAC_UP"]), set(sets["HDAC_DOWN"])

            def split(s, sym):
                P = np.array([(x, y) for i, x, y in zip(s["ids"], s["x"], s["y"]) if sym[i] in up])
                M = np.array([(x, y) for i, x, y in zip(s["ids"], s["x"], s["y"]) if sym[i] in dn])
                spread = (np.sqrt(((P - P.mean(0)) ** 2).sum(1).mean())
                          + np.sqrt(((M - M.mean(0)) ** 2).sum(1).mean())) / 2
                return float(np.linalg.norm(P.mean(0) - M.mean(0)) / spread), len(P), len(M)
            try:
                with sync_playwright() as p:
                    b = p.chromium.launch()
                    try:
                        pg = b.new_page(viewport={"width": 1300, "height": 800})
                        errs = []
                        pg.on("pageerror", lambda e: errs.append(str(e)))
                        pg.on("console", lambda m: errs.append(m.text) if m.type == "error" else None)
                        pg.goto(pathlib.Path(html).resolve().as_uri())     # file:///C:/... on Windows
                        pg.wait_for_function("() => !!window.TAHOE_MAP")
                        sym = pg.evaluate("TAHOE_MAP.data.sym")
                        g = next(s for s in sets["HDAC_UP"] if s in sym[:pg.evaluate("TAHOE_MAP.data.n")])
                        pg.evaluate(f"TAHOE_MAP.select({sym.index(g)})")
                        settled = "() => { const s = TAHOE_MAP.sim('{t}'); return s && s.n > 0 && !s.moving; }"
                        for t in ("signed", "nbr", "all", "help", "mod"):
                            pg.click(f"#tabs [data-tab='{t}']")
                            if t in ("nbr", "all", "mod"):
                                pg.wait_for_function(settled.replace("{t}", t), timeout=60000)
                        r0 = split(pg.evaluate("TAHOE_MAP.sim('mod')"), sym)
                        pg.click("#pane-mod [data-k='opp1']")
                        pg.wait_for_timeout(300)
                        pg.wait_for_function(settled.replace("{t}", "mod"), timeout=60000)
                        r1 = split(pg.evaluate("TAHOE_MAP.sim('mod')"), sym)
                    finally:
                        b.close()
            except Exception as e:  # noqa: BLE001  (no browser binary, sandbox, ...)
                if "Executable doesn't exist" in str(e) or "playwright install" in str(e):
                    return "warn", ("Playwright's Chromium is not installed: browser check skipped (optional: "
                                    "python -m playwright install chromium)")
                raise
            return (not errs and r1[0] > 2 * r0[0] and r1[0] > 1.5,
                    f"HDAC module {r0[1]} + / {r0[2]} - genes: arm centroid distance / arm spread {r0[0]:.2f} when "
                    f"opposite genes attract, {r1[0]:.2f} when they repel; script errors: {errs[:3]}")
        check("map", "physics tabs run; the sign switch parts the planted HDAC arms", map_physics)

        def knn_mixing(xy, group, k=5):
            """share of the k nearest grouped genes of every grouped gene that belong to another group"""
            from scipy.spatial import cKDTree
            g = group >= 0
            _, j = cKDTree(xy[g]).query(xy[g], k=k + 1)
            return float((group[g][j[:, 1:]] != group[g][:, None]).mean())

        def map_spread_layouts():
            """graph/nodes.parquet's spread layouts move the modules apart: on the nodal map (groups = modules) and
            the signed map (groups = module arms) far fewer of a module gene's nearest module genes are in another
            group than on the t-SNE layouts, and the spread layouts are deterministic numbers (finite)"""
            res, ok = {}, True
            if not {"xm", "ym", "xsm", "ysm"} <= set(nodes.columns):
                return False, "graph/nodes.parquet has no xm, ym, xsm, ysm"
            m = nodes["module"].to_numpy()
            two = nodes["module"].map(nodes.groupby("module")["arm"].agg(lambda a: (a == "-").any())).to_numpy()
            gs = np.where(m > 0, 2 * m + ((nodes["arm"] == "-").to_numpy() & two), -1)
            for name, a, b, grp in (("nodal", ("x", "y"), ("xm", "ym"), np.where(m > 0, m, -1)),
                                    ("signed", ("xs", "ys"), ("xsm", "ysm"), gs)):
                t, sp = (nodes[list(c)].to_numpy(float) for c in (a, b))
                m0, m1 = knn_mixing(t, grp), knn_mixing(sp, grp)
                res[name] = f"{m0:.3f} on the t-SNE layout -> {m1:.3f} spread"
                ok &= bool(np.isfinite(sp).all()) and m1 < 0.5 * m0 and m1 <= 0.03
            return ok, f"a module gene's 5 nearest module genes in another group: {res}"
        check("map", "the spread layouts move the modules apart", map_spread_layouts)

        def map_alerts_not_removed():
            """the side panel's drug-dose lists hold every row of tables/drug_effects.parquet in its ranked place,
            flagged ones too, cut at n_drugs plus any unflagged ones of the first n_drugs beyond them; a row with an
            artifact flag carries an alert naming its flags; the planted toxic drug-doses show up with '⚠ toxic'"""
            _, D = map_data()
            de = pd.read_parquet(os.path.join(out, "tables", "drug_effects.parquet"))
            ent = {c: i for i, c in enumerate(D["col"])}
            fl, nd = D["fl"], D["n_drugs"]
            bad, n_alert, seen_toxic = [], 0, set()
            tox = {(t["drug"], float(t["conc"])) for t in truth.get("toxic_drug_doses", [])}
            dlab = {r["dd"]: (r["drug"], float(r["conc"])) for r in de[["dd", "drug", "conc"]].drop_duplicates("dd")
                    .to_dict("records")}
            for sign, key in ((1, "up"), (-1, "dn")):
                sub = de[np.sign(de["z"]) == sign].copy()
                sub["ent"] = sub["col"].map(ent)
                sub["zz"] = sign * sub["z"]
                for e, g in sub.dropna(subset=["ent"]).sort_values(["ent", "zz"], ascending=[True, False],
                                                                    kind="mergesort").groupby("ent"):
                    clean = g["clean"].to_numpy(bool)
                    keep = np.zeros(len(g), dtype=bool)
                    keep[:nd] = True
                    keep[np.flatnonzero(clean)[:nd]] = True
                    want = g["dd"].to_numpy()[keep].tolist()
                    a = D[key][int(e)]
                    got = a[0::5]
                    if got != want:
                        bad.append((D["sym"][int(e)], key, got[:4], want[:4]))
                        continue
                    ccs = g["cc_share"].to_numpy(float)[keep] if "cc_share" in g else np.full(keep.sum(), np.nan)
                    for dd_, code, cl, f, cc in zip(got, a[4::5], clean[keep], g["flags"].to_numpy()[keep], ccs):
                        alert = code > 0 and fl[code - 1][1] == 1
                        # the cell-cycle share shown is this row's own (100 x cc_share, rounded; cc_share is stored
                        # as float32, so allow the last digit)
                        pct = re.search(r"explains ~(\d+)%", fl[code - 1][0]) if code > 0 else None
                        cc_ok = not (np.isfinite(cc) and "cell-cycle shift" in str(f)) or (
                            pct is not None and abs(int(pct.group(1)) - 100 * cc) <= 0.51)
                        if alert != (not cl) or not cc_ok or (alert and not fl[code - 1][0].split(";")[0]
                                                              .split(",")[0] in str(f)):
                            bad.append((D["sym"][int(e)], key, dd_, code, cl, f))
                        n_alert += alert
                        if alert and "toxic" in fl[code - 1][0] and dlab.get(dd_) in tox:
                            seen_toxic.add(dlab[dd_])
            return (not bad and n_alert > 0 and seen_toxic == tox,
                    f"{n_alert} listed rows with an alert; planted toxic drug-doses shown with '⚠ toxic': "
                    f"{sorted(seen_toxic)} of {sorted(tox)}; mismatches: {bad[:3]}")
        check("map", "flagged drug-doses stay in the side panel's lists, with an alert", map_alerts_not_removed)

        # the line rows (the strongest drug-dose up and down, and each way the strongest without an alert) are
        # checked by tests/test_surfaces.py (map_line_checks), run below with the other surface checks

        def map_views():
            """in a headless browser: the Spread slider moves the genes and parts the modules on the page; the tour
            tab draws and turns; axis mode shows two axes exactly (x = axis i, y = axis j of each gene's vector);
            depth 3 holds more genes than depth 2; the side panel lists an alerted drug-dose with its alert"""
            try:
                from playwright.sync_api import sync_playwright
            except ImportError:
                return "warn", "Playwright not installed: browser check skipped"
            res = {}
            try:
                with sync_playwright() as p:
                    b = p.chromium.launch()
                    try:
                        pg = b.new_page(viewport={"width": 1300, "height": 800})
                        errs = []
                        pg.on("pageerror", lambda e: errs.append(str(e)))
                        pg.on("console", lambda m: errs.append(m.text) if m.type == "error" else None)
                        pg.goto(pathlib.Path(html).resolve().as_uri())
                        pg.wait_for_function("() => !!window.TAHOE_MAP")
                        D = pg.evaluate("TAHOE_MAP.data")
                        n = D["n"]
                        mod = np.array(D["mod"][:n])
                        grp = np.where(mod > 0, mod, -1)
                        # spread: the page opens at Spread 1 when the graph stage made the spread layouts (html_map
                        # VERSION 9); the check moves it to 0 (the t-SNE layout) first, then back to 1
                        res["default"] = (pg.evaluate("TAHOE_MAP.hasSpread()"), pg.evaluate("TAHOE_MAP.spread()"))
                        pg.evaluate("TAHOE_MAP.spread(0)")
                        pg.wait_for_function("() => !TAHOE_MAP.positions().animating", timeout=10000)
                        p0 = pg.evaluate("TAHOE_MAP.positions()")
                        pg.evaluate("TAHOE_MAP.spread(1)")
                        pg.wait_for_function("() => !TAHOE_MAP.positions().animating", timeout=10000)
                        p1 = pg.evaluate("TAHOE_MAP.positions()")
                        xy0, xy1 = (np.column_stack([q["x"], q["y"]]) for q in (p0, p1))
                        res["spread"] = (knn_mixing(xy0, grp), knn_mixing(xy1, grp),
                                         float(np.hypot(*(xy1 - xy0).T).mean()))
                        pg.evaluate("TAHOE_MAP.spread(0)")
                        # tour
                        pg.click("#tabs [data-tab='tour']")
                        pg.wait_for_timeout(700)
                        s1 = pg.evaluate("TAHOE_MAP.tour()")
                        pg.wait_for_timeout(500)
                        s2 = pg.evaluate("TAHOE_MAP.tour()")
                        drawn = pg.evaluate("""() => { const c = document.querySelector('#pane-tour canvas');
                            const d = c.getContext('2d').getImageData(0, 0, c.width, c.height).data; let k = 0;
                            for (let i = 0; i < d.length; i += 4) if (d[i] < 240 || d[i + 2] < 240) k++; return k; }""")
                        res["tour"] = (s1["k"], s1["n"], float(np.abs(np.subtract(s1["frame"], s2["frame"])).max()),
                                       drawn, round(pg.evaluate("TAHOE_MAP.tourBench(30)"), 2))
                        # axis mode: axis 1 against axis 3
                        pg.evaluate("TAHOE_MAP.tourAxes(0, 2)")
                        pg.wait_for_function("() => !TAHOE_MAP.tour().moving", timeout=30000)
                        pos = pg.evaluate("TAHOE_MAP.tourPositions()")
                        err = max(max(abs(pos["x"][i] - v[0]), abs(pos["y"][i] - v[2]))
                                  for i in range(0, n, max(1, n // 25))
                                  for v in [pg.evaluate(f"TAHOE_MAP.tourVector({i})")])
                        res["axes"] = (pg.evaluate("TAHOE_MAP.tour().mode"), err)
                        # neighbourhood depth
                        g = next(s for s in sets["HDAC_UP"] if s in D["sym"][:n])
                        pg.evaluate(f"TAHOE_MAP.select({D['sym'].index(g)})")
                        pg.click("#tabs [data-tab='nbr']")
                        pg.wait_for_function("() => { const s = TAHOE_MAP.sim('nbr'); return s && s.n > 0; }")
                        d2 = pg.evaluate("TAHOE_MAP.sim('nbr')")
                        pg.click("#pane-nbr [data-k='dep2']")
                        pg.wait_for_timeout(200)
                        d3 = pg.evaluate("TAHOE_MAP.sim('nbr')")
                        res["depth"] = (d2["depth"], d2["n"], d3["depth"], d3["n"])
                        # side panel: an alerted drug-dose of a map gene
                        fl = D["fl"]
                        pick = next(((i, key) for i in range(n) for key in ("up", "dn")
                                     if any(c > 0 and fl[c - 1][1] == 1 for c in D[key][i][4::5])), None)
                        if pick:
                            i, key = pick
                            a = D[key][i]
                            t = next(t for t in range(0, len(a), 5) if a[t + 4] > 0 and fl[a[t + 4] - 1][1] == 1)
                            pg.evaluate(f"TAHOE_MAP.select({i})")
                            txt = pg.evaluate("TAHOE_MAP.panel()")
                            res["panel"] = (D["sym"][i], D["dd"][a[t]], "⚠ " + fl[a[t + 4] - 1][0] in txt,
                                            D["dd"][a[t]] in txt)
                    finally:
                        b.close()
            except Exception as e:  # noqa: BLE001
                if "Executable doesn't exist" in str(e) or "playwright install" in str(e):
                    return "warn", "Playwright's Chromium is not installed: browser check skipped"
                raise
            sp, tr, ax, dp = res["spread"], res["tour"], res["axes"], res["depth"]
            dflt = res.get("default") or (None, None)
            ok = (not errs and (dflt[1] == 1 if dflt[0] else True) and sp[1] < 0.5 * sp[0] and sp[2] > 0
                  and tr[2] > 1e-3 and tr[3] > tr[1]
                  and ax[0] == "axes" and ax[1] < 1e-4 and dp[0] == 2 and dp[2] == 3 and dp[3] > dp[1]
                  and bool(res.get("panel")) and all(res["panel"][2:]))
            return ok, (f"opens at Spread {dflt[1]} (spread layouts: {dflt[0]}); Spread 0 -> 1: module mixing "
                        f"{sp[0]:.3f} -> {sp[1]:.3f}, mean move {sp[2]:.3f}; tour: {tr[0]}-D, "
                        f"{tr[1]} genes, frame change {tr[2]:.3f} in 0.5 s, {tr[3]} pixels drawn, {tr[4]} ms per "
                        f"frame; axis mode max |error| {ax[1]:.1e}; neighbourhood depth 2: {dp[1]} genes, depth 3: "
                        f"{dp[3]}; side panel {res.get('panel')}; script errors: {errs[:3]}")
        check("map", "opens at Spread 1; spread slider, tour, axis mode, neighbourhood depth, alerts in the side "
                     "panel", map_views)
        check("map", "probable direction: side-panel lists = direction_view, arrows and their toggles, an older output",
              lambda: map_direction(out, html))

    # ---------------------------------------------------------------- look-ups
    def lookup_gene():
        """`tahoe gene HMOX1` names the NRF2 activators among the drugs that raise it, and NRF2 targets among the
        genes that move with it: NRF2_CORE, or (since the direction plants) the SYNTH NRF2 targets NRF2_EXT, which
        respond to the same activators by construction and can fill its partner list (on seed 1 they push NQO1 out
        of the 15 shown)"""
        r = subprocess.run([sys.executable, "-m", "tahoemap", "gene", "HMOX1", "--data", data, "--out", out],
                           cwd=REPO, capture_output=True, text=True, encoding="utf-8")
        txt = r.stdout
        nrf2 = set(truth["gene_sets"].get("NRF2_CORE", [])) if isinstance(truth.get("gene_sets"), dict) else set()
        nrf2 |= set(sets.get("NRF2_EXT", []))
        sec = txt.split("\nMOVES WITH", 1)[1].split("\n\n", 1)[0] if "\nMOVES WITH" in txt else ""
        named = sorted(x for x in nrf2 - {"HMOX1"} if re.search(rf"^ +{re.escape(x)} ", sec, re.M))
        return (r.returncode == 0 and ("Dimethyl fumarate" in txt or "Auranofin" in txt) and len(named) >= 3,
                f"exit {r.returncode}; {len(txt.splitlines())} lines; planted NRF2 targets among the genes that move "
                f"with it: {len(named)} ({', '.join(named[:6])}{', ...' if len(named) > 6 else ''})")
    if os.path.exists(os.path.join(REPO, "tahoemap", "query.py")):
        check("query", "tahoe gene HMOX1 answers the question", lookup_gene)
        check("query", "probable direction in gene / drug / line / pair: direction_view's rows, order, cap rule and "
                       "words; a cp1252 console; an output without the stage", lambda: lookup_direction(out, data))

    check("run", "--redo removes the finished plates before the build (a run without it resumes from them)",
          redo_removes_plates)

    # ---------------------------------------------------------------- the second wave's rules (W1-W7)
    wave2_checks(out, data, truth, check, col, gK)

    # ---------------------------------------------------------------- the newer packages' checks (design I5)
    package_checks(out, data, check)

    # ---------------------------------------------------------------- the rules changed after the reviews of the
    # published results (tests/test_fix_back.py: toy inputs, then this output)
    fix_back_checks(out, check)


def fix_back_checks(out, check):
    """tests/test_fix_back.py: its unit checks (toy inputs) and its checks of this output, each a 'fix-back' check:
    caveats next to named values, per-line signs, the line cards' selective drug-doses, the report's wording, the
    direction notes of changed rules, Tahoe's annotation without the metadata file, the ChEMBL / Compara progress and
    the PubChem retry."""
    sys.path.insert(0, os.path.join(REPO, "tests"))
    try:
        import test_fix_back as FB
    except ImportError as e:
        check("fix-back", "tests/test_fix_back.py", lambda e=e: (False, f"not importable: {e}"))
        return
    for name, fn in FB.UNIT + FB.output_checks(out):
        check("fix-back", name, fn)


def _report(check, stage, results):
    """Each (name, ok, detail) of a package's check(...) as one run_tests check (ok True, False or 'warn')."""
    for name, ok, detail in results:
        check(stage, name, lambda ok=ok, detail=detail: ("warn" if ok == "warn" else ok is True, detail))


def package_checks(out, data, check):
    """tests/test_direction.py, tests/test_surfaces.py and tests/test_explorer.py on this output."""
    sys.path.insert(0, os.path.join(REPO, "tests"))
    if os.path.exists(os.path.join(out, "direction", "edges.parquet")):
        try:
            import test_direction as TD
            _report(check, "direction", TD.check(out, data))
        except Exception as e:  # noqa: BLE001
            check("direction", "tests/test_direction.py check(out)", lambda e=e: (False, f"{type(e).__name__}: {e}"))
    if os.path.exists(os.path.join(out, "map", "gene_map.html")):
        try:
            import test_surfaces as TS
            _report(check, "surfaces", TS.check(out, data))
        except Exception as e:  # noqa: BLE001
            check("surfaces", "tests/test_surfaces.py check(out, data)",
                  lambda e=e: (False, f"{type(e).__name__}: {e}"))
    if os.path.exists(os.path.join(out, "stages", "explorer.json")):
        import test_explorer as TX
        TX.check(out, data, report=check)
        check("explorer", "registered after map: when only its page files (tahoemap/explorer_app) change, run copies "
              "only them (the data files are not touched); status shows its volumes, row counts and checks",
              lambda: explorer_pipeline(out))
    else:
        check("explorer", "the explorer stage ran (stages/explorer.json)", lambda: (False, f"{out} has no explorer"))


# ---------------------------------------------------------------- look-ups: probable direction (tahoemap/query.py)
def _planted_null(data):
    """The planted natural knockout's gene (ground_truth.json 'direction' 'gluco_coactivator_null'; the first GLUCO
    gene, which differs between seeds: SYNTH0881 on seed 0)."""
    try:
        with open(os.path.join(data, "ground_truth.json"), encoding="utf-8") as fh:
            return json.load(fh)["direction"]["gluco_coactivator_null"]["source"]
    except (OSError, ValueError, KeyError, TypeError):
        return "SYNTH0881"


def _tp53_cells_drug(dv):
    """The first DNA-damaging drug (Doxorubicin, Topotecan, 5-Fluorouracil) with a TP53 -> cells row at any dose, as
    named in drugdose.csv ('' when none): the surfaces' checks follow the planted TP53 effect where it passed."""
    ce = dv.cells("TP53")
    for pre in ("Doxorubicin", "Topotecan", "5-Fluorouracil"):
        hit = [str(d) for d in ce["target_drug"] if str(d).startswith(pre)] if len(ce) else []
        if hit:
            return hit[0]
    return ""


def lookup_direction(out, data):
    """the look-ups' probable direction (direction stage) on the synthetic run: `gene` lists upstream, downstream and
    cells rows as direction_view orders, caps (the cap rule) and words them (edge line, counts, more text), with the
    legend and the caveat; `drug` the genes that set how the cells fare under it and its drug-target arrows; `line` the
    TP53 loss-of-function group and the planted natural knockout (SYNTH0881 on seed 0) with their arrows; `pair` the
    arrow either way with every alert in full and a shared upstream gene (its arrows marked when they carry an alert);
    `gene` of a drug target that is no measured gene lists that target's arrows (all of them with a large --top, which
    its capped list names), and `pair` of it with a measured gene gives the arrows with every alert in full; a cp1252
    console (a Windows redirect) gets '->' and '!' with every line <= 120 characters; an output without the stage
    gets one sentence and no traceback"""
    from tahoemap import direction_view as DV
    from tahoemap import query as Q
    from tahoemap.common import cap_keep
    dv = DV.load(out, cache=False)
    if dv is None:
        return False, "no direction stage in this output (direction/edges.parquet)"

    def run(*args, enc="utf-8"):
        env = dict(os.environ, PYTHONIOENCODING=enc, COLUMNS="120")
        r = subprocess.run([sys.executable, "-m", "tahoemap", *args, "--data", data, "--out", out], cwd=REPO,
                           capture_output=True, env=env)
        return r.returncode, r.stdout.decode(enc, errors="replace"), r.stderr.decode(enc, errors="replace")

    def norm(t):
        return " ".join(t.split())

    def section(t, head, stop="\nFULL TABLES"):
        return t.split(head, 1)[1].split(stop, 1)[0] if head in t else ""

    def blocks(t):
        """{rank: the row's text, whitespace-normalised} of a probable-direction list."""
        out_, cur = {}, None
        for ln in t.splitlines():
            m = re.match(r"^  ( {0,2}\d{1,3})  (\S.*)$", ln)
            if m:
                cur = int(m.group(1))
                out_[cur] = m.group(2)
            elif cur is not None and ln.startswith(" " * 7):
                out_[cur] += " " + ln.strip()
            else:
                cur = None
        return {k: norm(v) for k, v in out_.items()}

    def list_ok(text, title, rows, n):
        """the list under `title`: its counts, the cap rule's rows (rank and edge line) and the more text"""
        part = text.split("\n  " + title, 1)[1] if "\n  " + title in text else ""
        part = re.split(r"\n  (?:upstream|downstream|cells under drugs|how to read|genes that set|its targets|"
                        r"recorded alterations|genes it does not|the strongest arrows)", part, maxsplit=1)[0]
        if norm(DV.counts_text(rows, "arrows")) not in norm(part):
            return False
        if not len(rows):
            return True
        al = rows["has_alert"].to_numpy(dtype=bool)
        keep = cap_keep(al, n)
        b = blocks(part)
        rest = np.setdiff1d(np.arange(len(rows)), keep)
        more = DV.more_text(int(rest.size), int(al[rest].sum()), "arrows")
        return (sorted(b) == [int(k) + 1 for k in keep]
                and all(b[int(k) + 1].startswith(norm(DV.edge_line(rows.iloc[int(k)], alerts="none", max_names=4)))
                        and norm(DV.alert_short(rows.iloc[int(k)])) in b[int(k) + 1] for k in keep)
                and (not more or norm(more) in norm(part)))
    bad, wide = [], []
    # gene: TP53 (downstream and cells, capped at 3), CDKN1A (upstream)
    code, txt, err = run("gene", "TP53", "--top", "3")
    sec = section(txt, "PROBABLE DIRECTION")
    wide += [ln for ln in txt.splitlines() if len(ln) > 120]
    if not (code == 0 and list_ok(sec, "downstream - genes TP53", dv.downstream("TP53"), 3)
            and list_ok(sec, "cells under drugs - how TP53", dv.cells("TP53"), 3)
            and list_ok(sec, "upstream - what probably acts on TP53", dv.upstream("TP53"), 3)
            and norm(DV.CAVEAT) in norm(sec) and "grades: A: strong" in sec and DV.ORDER in norm(sec)):
        bad.append(f"gene TP53 (exit {code}; {err[-200:]})")
    code, txt, _e = run("gene", "CDKN1A")
    sec = section(txt, "PROBABLE DIRECTION")
    tr = dv.upstream("CDKN1A")
    tr = tr[tr["source"] == "TP53"]
    if not (code == 0 and len(tr) and list_ok(sec, "upstream - what probably acts on CDKN1A", dv.upstream("CDKN1A"), 10)
            and norm(DV.edge_line(tr.iloc[0], alerts="none")) in norm(sec)
            and "TP53 activity strengthens CDKN1A's drug response" in sec and norm(DV.SIGN_RESPONSE_NOTE) in norm(sec)):
        bad.append("gene CDKN1A")
    # a drug target that is no measured gene of the run: `gene` lists its arrows (all of them with a large --top, and
    # the hint for that when capped); `pair` with a measured target gives the arrows with every alert in full
    um = dv.rows[(dv.rows["source_col"] < 0) & (dv.rows["target_type"].astype(str) == "gene")]
    src = str(um.iloc[0]["sources"][0]) if len(um) else ""
    if src:
        code, txt, _e = run("gene", src.lower())
        if not (code == 0 and "not a measured gene of this run" in txt
                and list_ok(section(txt, "PROBABLE DIRECTION"), f"downstream - genes {src} probably",
                            dv.downstream(src), 10)):
            bad.append(f"gene {src} (a drug target that is no measured gene)")
        tgt = str(um.iloc[0]["target"])
        code, txt, err = run("pair", src, tgt)
        row = dv.downstream(src)
        row = row[row["target"] == tgt]
        if not (code == 0 and "not a measured gene of this run" in txt and len(row)
                and norm(DV.alert_long(row.iloc[0])) in norm(txt) and f"{tgt} → {src}: none can exist" in txt):
            bad.append(f"pair {src} {tgt} (the arrows of a source that is no measured gene, every alert in full)")
    big = max(set(str(x) for ss in um["sources"] for x in ss), key=lambda x: len(dv.downstream(x)), default="")
    if big and len(dv.downstream(big)) > 10:
        n_big = len(dv.downstream(big))
        code, txt, _e = run("gene", big)
        hint = f"(`--top {n_big}` lists them all)"
        code2, txt2, _e = run("gene", big, "--top", str(n_big + 5))
        if not (code == 0 and hint in txt and code2 == 0 and list_ok(section(txt2, "PROBABLE DIRECTION"),
                                                                      f"downstream - genes {big} probably",
                                                                      dv.downstream(big), n_big + 5)
                and "more arrows" not in section(txt2, "PROBABLE DIRECTION")):
            bad.append(f"gene {big}: --top lists all {n_big} arrows, and the capped list says so")
    # drug: the cells under a DNA-damaging drug with a TP53 -> cells row (Doxorubicin on seed 0; on another seed the
    # planted TP53 effect may pass at another of them only), and Dexamethasone's NR3C1 arrows
    drug = _tp53_cells_drug(dv)
    code, txt, _e = run("drug", drug.split(" (")[0])
    dd = pd.read_csv(os.path.join(out, "atlas", "effects", "drugdose.csv"))
    dds = [i for i, d in enumerate(dd["drug"].astype(str)) if d == drug]
    pos = np.unique(np.concatenate([np.zeros(0, np.int64)] + [dv.for_drugdose(i)["order"].to_numpy() for i in dds]))
    sec = section(txt, "PROBABLE DIRECTION")
    if not (code == 0 and len(pos) and list_ok(sec, "genes that set how the cells fare under it", dv.rows.iloc[pos], 10)
            and f"TP53 → cells under {drug}" in sec):
        bad.append(f"drug {drug or '(no DNA-damaging drug with a TP53 -> cells row)'}")
    code, txt, _e = run("drug", "Dexamethasone")
    sec = section(txt, "PROBABLE DIRECTION")
    tg = dv.drug_targets("Dexamethasone")
    if not (code == 0 and len(tg) and list_ok(sec, "its targets: what acting on them", tg, 10)
            and "NR3C1 → " in sec and "this drug moves it that way too" in norm(sec)):
        bad.append("drug Dexamethasone")
    # line: a TP53 loss-of-function line that lacks the planted natural knockout (SYNTH0881 on seed 0)
    null_src = _planted_null(data)
    g = dv.groups
    desc = {k: str(g.loc[g["group_id"] == k, "description"].iloc[0]) for k in ("genotype:TP53:LoF", f"null:{null_src}")
            if (g["group_id"] == k).any()}
    lines = [set(str(g.loc[g["group_id"] == k, "altered_lines"].iloc[0]).split(", ")) for k in desc]
    both = sorted(set.intersection(*lines)) if len(lines) == 2 else []
    if both:
        code, txt, _e = run("line", both[0])
        sec = norm(section(txt, "PROBABLE DIRECTION"))
        r = dv.rows
        ok = code == 0 and "the strongest arrows of these groups" in sec
        for k, d in desc.items():
            sub = r[r["group"].astype(str) == d]
            pre = "genotype" if k.startswith("genotype") else "null"
            by = ", ".join(f"{w} {int((sub['kind'] == f'{pre}_{x}').sum())}" for x, w in (
                ("response", "response"), ("baseline", "level"), ("sensitivity", "cells"),
                ("selectivity", "selectivity")))
            ok = ok and f"{d}: {len(sub)} arrows ({by};" in sec
        if not ok:
            bad.append(f"line {both[0]}")
    else:
        bad.append(f"no line both TP53-LoF and without {null_src}")
    # pair: the arrow with every alert in full; none the other way; a shared upstream gene
    code, txt, _e = run("pair", "TP53", "CDKN1A")
    sec = section(txt, "PROBABLE DIRECTION BETWEEN THEM", "\nGENOME AND KNOWN LINKS")
    row = dv.downstream("TP53")
    row = row[row["target"] == "CDKN1A"]
    if not (code == 0 and len(row) and norm(DV.alert_long(row.iloc[0])) in norm(sec)
            and "CDKN1A → TP53: none" in sec):
        bad.append("pair TP53 CDKN1A")
    code, txt, _e = run("pair", "CDKN1A", "BAX")
    shared = norm(txt.split("shared upstream - genes with an arrow to both", 1)[1])[:400] if \
        "shared upstream - genes with an arrow to both" in txt else ""
    ua = dv.upstream("CDKN1A")
    ua = ua[ua["source"] == "TP53"]
    if not (code == 0 and shared and "TP53 (→ CDKN1A [" in shared
            and (f"[{ua['grade'].iloc[0]}] {DV.sign_word(ua['sign'].iloc[0], ua['kind'].iloc[0])} ⚠" in shared
                 if len(ua) and bool(ua["has_alert"].iloc[0]) else True)):
        bad.append("pair CDKN1A BAX (shared upstream, with the arrows' alert marks)")
    # a cp1252 console (a Windows redirect): ASCII signs, nothing wider than 120 characters
    code, txt, _e = run("gene", "TP53", enc="cp1252")
    sec = section(txt, "PROBABLE DIRECTION")
    wide += [ln for ln in txt.splitlines() if len(ln) > 120]
    # TP53's first downstream row in direction_view's order (CDKN1A on some seeds; on others a planted gene of the
    # TP53-wild-type lines ranks first and CDKN1A is beyond the cap)
    td = dv.downstream("TP53").head(1)
    # since direction VERSION 3 'within organs' (when most lines are compared) is a note: edge_line prints it as
    # '- notes: within organs, ...' in ASCII, wrapped across lines
    if not (code == 0 and len(td) and f"TP53 -> {td['target'].iloc[0]}  [{td['grade'].iloc[0]}]" in sec
            and "- notes: within organs" in " ".join(sec.split())
            and "→" not in txt and "⚠" not in txt and "SOURCE -> TARGET" in sec):
        bad.append("cp1252 console")
    # an output without the stage (Out.ran patched in memory: the run's files are not touched)
    o = Q.Out(out)
    ran = o.ran
    o.ran = lambda s: False if s == "direction" else ran(s)
    try:
        texts = ["\n".join(Q.cmd_gene(o, ["TP53"], 5)), "\n".join(Q.cmd_drug(o, ["Doxorubicin"], 5)),
                 "\n".join(Q.cmd_line(o, [both[0] if both else "PANC-1"], 5)),
                 "\n".join(Q.cmd_pair(o, ["TP53", "CDKN1A"], 5))]
        older = all("[probable direction: the direction stage has not run here" in norm(t) for t in texts)
    except Exception as e:  # noqa: BLE001
        older, texts = False, [f"{type(e).__name__}: {e}"]
    if not older:
        bad.append(f"an output without the stage ({texts[-1][-200:]})")
    if wide:
        bad.append(f"{len(wide)} lines wider than 120 characters")
    return not bad, (f"TP53: {len(dv.downstream('TP53'))} downstream, {len(dv.cells('TP53'))} cells rows; "
                     f"unmeasured source {src or '-'}; line {both[0] if both else '-'}; problems: {bad or 'none'}")


# ---------------------------------------------------------------- map: probable direction (tahoemap/html_map.py)
def map_direction(out, html):
    """the map's probable direction (direction stage): the page holds every display row of direction_view that touches
    one of its genes (the others are counted); in a headless browser every gene's upstream, downstream and cells lists
    are direction_view's rows in its order and words (edge_line), cut by its cap rule with its counts, and 'show all'
    lists them all; a gene link in a row selects that gene; the neighbourhood draws one arrow per ordered pair of genes
    shown (its strongest row), '+ its genes' adds a gene's up- and downstream genes and 'off' removes the arrows; a
    page without the stage says so; no script errors"""
    from tahoemap import direction_view as DV
    from tahoemap import html_map as HM
    dv = DV.load(out, cache=False)
    if dv is None:
        return False, "no direction/edges.parquet"
    txt = open(html, encoding="utf-8").read()
    D = json.loads(re.search(r'<script id="tm-data" type="application/json">(.*?)</script>', txt, re.S).group(1))
    dr = D.get("dir") or {}
    ent = {int(c): i for i, c in enumerate(D["col"])}
    touch = sum(1 for r in dv.rows.itertuples(index=False) if any(int(c) in ent for c in r.source_cols)
                or (r.target_type != "cells" and int(r.target_col) in ent))
    block = (bool(dr.get("ok")) and dr.get("n_rows") == touch and dr.get("n_rows_stage") == len(dv.rows)
             and dr.get("n_rows") + dr.get("n_rows_out", -1) == len(dv.rows))
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        return "warn", "Playwright not installed: browser check skipped"
    cap, res, errs = int(dr.get("cap") or 8), {}, []
    want = {}                                    # entry -> {list: [edge_line], ...} from direction_view
    for e, c in enumerate(D["col"]):
        lists = {w: list(f(int(c)).itertuples(index=False)) for w, f in
                 (("up", dv.upstream), ("dn", dv.downstream), ("ce", dv.cells))}
        if any(lists.values()):
            want[e] = lists
    old = os.path.join(os.path.dirname(html), "_test_no_direction.html")
    try:
        with sync_playwright() as p:
            b = p.chromium.launch()
            try:
                pg = b.new_page(viewport={"width": 1300, "height": 800})
                pg.on("pageerror", lambda e: errs.append(str(e)))
                pg.on("console", lambda m: errs.append(m.text) if m.type == "error" else None)
                pg.goto(pathlib.Path(html).resolve().as_uri())
                pg.wait_for_function("() => !!window.TAHOE_MAP")
                sym = D["sym"]
                got = pg.evaluate("ks => ks.map(i => TAHOE_MAP.direction(i))", list(want))
                bad = []
                for (e, lists), g in zip(want.items(), got):
                    for w, rows in lists.items():
                        df = pd.DataFrame(rows)
                        shown, n_more, n_al = DV.cap(df, cap) if len(df) else (df, 0, 0)
                        pos = [list(df["order"]).index(o) for o in shown["order"]] if len(df) else []
                        if (g[w] != [DV.edge_line(r) for r in rows] or g[w + "_shown"] != pos
                                or g[w + "_more"] != [n_more, n_al]
                                or g[w + "_counts"] != DV.counts_text(df if len(df) else None)):
                            bad.append((sym[e], w))
                empty = pg.evaluate("n => { const o = []; for (let i = 0; i < n; i += 7) { "
                                    "const d = TAHOE_MAP.direction(i); "
                                    "if (d.up.length + d.dn.length + d.ce.length) o.push(i); } return o; }", len(sym))
                bad += [(sym[e], "rows on the page, none in direction_view") for e in empty if e not in want]
                res["lists"] = (len(want), sum(len(v) for x in want.values() for v in x.values()), bad[:4])
                # a target's panel: TP53 -> CDKN1A, and the TP53 link selects TP53
                i, t = sym.index("CDKN1A"), sym.index("TP53")
                pg.evaluate(f"TAHOE_MAP.select({i})")
                panel = pg.evaluate("TAHOE_MAP.panel()")
                pg.click(f"#dlw-up [data-g='{t}']")
                res["panel"] = ("TP53 → CDKN1A" in panel and "Upstream (probable)" in panel,
                                pg.evaluate("TAHOE_MAP.state().sel") == t)
                # show all (a list longer than the cap)
                long_ = next(((e, w) for e, x in want.items() for w, r in x.items()
                              if len(r) > len(DV.cap(pd.DataFrame(r), cap)[0])), None)
                if long_:
                    e, w = long_
                    pg.evaluate(f"TAHOE_MAP.select({e})")
                    n0 = pg.evaluate(f"document.querySelectorAll('#dl-{w} .dr').length")
                    pg.click(f"[data-dall='{w}']")
                    n1 = pg.evaluate(f"document.querySelectorAll('#dl-{w} .dr').length")
                    res["all"] = (sym[e], w, n0, n1, len(want[e][w]))
                # the neighbourhood: TP53 (not on the map) with its downstream genes and arrows
                settled = "() => { const s = TAHOE_MAP.sim('nbr'); return s && s.n > 0 && !s.moving; }"
                pg.evaluate(f"TAHOE_MAP.select({t})")
                pg.click("#tabs [data-tab='nbr']")
                pg.wait_for_function(settled, timeout=60000)

                def expected(ids):
                    idx = {e: u for u, e in enumerate(ids)}
                    exp = {}
                    for e in ids:
                        for r in dv.downstream(int(D["col"][e])).itertuples(index=False):
                            v = ent.get(int(r.target_col), -1)
                            if v in idx and v != e and (e, v) not in exp:
                                exp[(e, v)] = DV.edge_line(r)
                    return exp
                a = pg.evaluate("TAHOE_MAP.dirArrows('nbr')")
                got_a = {(x["s"], x["t"]): x["line"] for x in a["arrows"]}
                res["tp53"] = (a["mode"], a["added"], len(got_a), got_a == expected(a["ids"]))
                # NFE2L2 (on the map): arrows to its NRF2 targets among its partners; 'off' removes them from the canvas
                count = """() => { const c = document.querySelector('#pane-nbr canvas');
                    const d = c.getContext('2d').getImageData(0, 0, c.width, c.height).data; let k = 0;
                    for (let i = 0; i < d.length; i += 4) if (d[i + 2] > d[i] + 40 && d[i + 2] > d[i + 1] + 50
                        && d[i] >= d[i + 1] - 5) k++; return k; }"""
                pg.evaluate(f"TAHOE_MAP.select({sym.index('NFE2L2')})")
                pg.wait_for_function(settled, timeout=60000)
                pg.click("#pane-nbr [data-k='dir1']")
                pg.wait_for_timeout(250)
                a1 = pg.evaluate("TAHOE_MAP.dirArrows('nbr')")
                px1 = pg.evaluate(count)
                pg.click("#pane-nbr [data-k='dir0']")
                pg.wait_for_timeout(250)
                a0 = pg.evaluate("TAHOE_MAP.dirArrows('nbr')")
                px0 = pg.evaluate(count)
                got1 = {(x["s"], x["t"]): x["line"] for x in a1["arrows"]}
                res["nfe2l2"] = (a1["mode"], len(got1), got1 == expected(a1["ids"]), a0["mode"], len(a0["arrows"]),
                                 px1, px0)
                for tab in ("nodal", "signed", "tour", "mod", "all", "help"):
                    pg.click(f"#tabs [data-tab='{tab}']")
                    pg.wait_for_timeout(150)
                # an older output: the same page without the direction stage
                d2 = dict(D)
                d2["dir"] = HM.dir_missing("no direction stage in this output (direction/edges.parquet is missing)")
                with open(old, "w", encoding="utf-8") as fh:
                    fh.write(HM.render(d2))
                pg.goto(pathlib.Path(old).resolve().as_uri())
                pg.wait_for_function("() => !!window.TAHOE_MAP")
                pg.evaluate(f"TAHOE_MAP.select({i})")
                p2 = pg.evaluate("TAHOE_MAP.panel()")
                pg.click("#tabs [data-tab='nbr']")
                pg.wait_for_timeout(300)
                res["old"] = ("No probable directions here" in p2,
                              pg.evaluate("document.querySelector(\"#pane-nbr [data-k='dir2']\").disabled"),
                              pg.evaluate("TAHOE_MAP.direction(0).ok"))
            finally:
                b.close()
    except Exception as e:  # noqa: BLE001
        if "Executable doesn't exist" in str(e) or "playwright install" in str(e):
            return "warn", "Playwright's Chromium is not installed: browser check skipped"
        raise
    finally:
        if os.path.exists(old):
            os.remove(old)
    li, pa, tp, nf, od = res["lists"], res["panel"], res["tp53"], res["nfe2l2"], res["old"]
    al = res.get("all")
    ok = (block and not errs and li[0] > 0 and not li[2] and all(pa) and (al is None or al[3] == al[4] > al[2])
          and tp[0] == 2 and tp[1] > 0 and tp[2] > 0 and tp[3] and nf[0] == 1 and nf[1] > 0 and nf[2]
          and nf[3] == 0 and nf[4] == 0 and nf[5] > nf[6] + 50 and od[0] and od[1] and od[2] is False)
    return ok, (f"page rows {dr.get('n_rows')} of the stage's {dr.get('n_rows_stage')} ({dr.get('n_rows_out')} touch "
                f"no page gene; expected {touch} that do); {li[0]} genes' lists ({li[1]} rows) = direction_view "
                f"(rows, order, words, cap, counts); mismatches {li[2]}; CDKN1A panel names TP53 → CDKN1A and its "
                f"TP53 link selects TP53: {pa}; show all {al}; neighbourhood of TP53 (mode, genes added, arrows, = "
                f"expected): {tp}; NFE2L2 arrows (mode, n, = expected, then off: mode, n; violet pixels on / off): "
                f"{nf}; page without the stage (panel says so, toggle disabled, ok): {od}; script errors {errs[:3]}")


# ---------------------------------------------------------------- direction (tahoemap/direction.py, direction_view.py)
DNA_DAMAGE_5UM = ("Doxorubicin (hydrochloride) 5", "Topotecan (hydrochloride) 5", "5-Fluorouracil 5")


def _table_wide(e):
    """Edges significant over the whole table of their kind (q < 0.10 and, where present, q_group < 0.10)."""
    return (e["q"] < 0.10) & (e["q_group"].isna() | (e["q_group"] < 0.10))


def direction_checks(out, truth, check, col):
    """The direction stage on the synthetic run: its stamp and outputs, the format of every edge, the planted answers
    (TP53 -> p53 targets and -> cells under DNA-damaging drugs; NFE2L2's level -> the NRF2 targets; a natural knockout
    of the glucocorticoid co-activator -> its partners), the negative controls, direction_view's rows and wording, its
    place among the stages, and its section of the validation report."""
    from tahoemap import direction as Dm
    from tahoemap import direction_view as DV
    dr = os.path.join(out, "direction")
    files = ("edges.parquet", "groups.parquet", "controls.json", "info.json", "README.md")

    def outputs():
        st = json.load(open(os.path.join(out, "stages", "direction.json"), encoding="utf-8"))
        miss = [f for f in files if not os.path.exists(os.path.join(dr, f))]
        e = pd.read_parquet(os.path.join(dr, "edges.parquet"))
        g = pd.read_parquet(os.path.join(dr, "groups.parquet"))
        txt = open(os.path.join(dr, "README.md"), encoding="utf-8").read()
        undoc = [c for c in list(e.columns) + list(g.columns) if f"`{c}`" not in txt]
        return (st["version"] == Dm.VERSION and not miss and st["info"]["edges"] == len(e) and not undoc
                and {"compounds", "compounds_supporting", "drug_effect"} <= set(e.columns),
                f"stamp version {st['version']}, {len(e):,} edges (stamp {st['info']['edges']:,}), {len(g)} groups; "
                f"missing files {miss}; columns without a README description {undoc}")
    check("direction", "stage stamp and outputs (edges, groups, controls, info, README with every column)", outputs)
    if not os.path.exists(os.path.join(dr, "edges.parquet")):
        return
    e = pd.read_parquet(os.path.join(dr, "edges.parquet"))
    ctl = json.load(open(os.path.join(dr, "controls.json"), encoding="utf-8"))
    sets = truth.get("gene_sets") or {}
    planted = truth.get("direction") or {}

    def edge_format():
        bad = []
        p, q = e["p"].to_numpy(float), e["q"].to_numpy(float)
        if not (np.isfinite(p).all() and (p > 0).all() and (p <= 1).all()):
            bad.append("p")
        if not (np.isfinite(q).all() and (q >= 0).all() and (q <= 1).all()):
            bad.append("q")
        grouped = e["kind"].str.startswith("genotype") | (e["kind"] == "level_sensitivity")
        if not np.where(grouped, e["q_group"] < 0.10, e["q"] < 0.10).all():
            bad.append("an edge without q (q_group for genotype and level_sensitivity) < 0.10")
        for c_, ok in (("grade", e["grade"].isin(list("ABC"))), ("kind", e["kind"].isin(Dm.KINDS)),
                       ("sign", e["sign"].isin([-1, 0, 1]))):
            if not ok.all():
                bad.append(c_)
        al = e["alerts"].fillna("")
        if not ((al == "") | al.str.startswith("⚠ ")).all():
            bad.append("an alert text without '⚠ '")
        if not (al.map(lambda s: s.count("; ") + 1 if s else 0) == e["n_alerts"]).all():
            bad.append("n_alerts")
        cells = e["target_type"] == "cells"
        resp = e["target_type"] == "response"                   # the selectivity kinds (direction VERSION 5)
        if not (((cells | resp) == (e["target_dd"] >= 0)) & (~cells | e["target"].str.startswith("cells under "))
                & (~resp | e["target"].str.startswith("response to "))).all():
            bad.append("cells / response targets and target_dd")
        if not (cells == e["kind"].isin(list(DV.SENSITIVITY))).all():
            bad.append("cells targets are not the sensitivity kinds")
        if not (resp == e["kind"].isin(list(DV.SELECTIVITY))).all():
            bad.append("response targets are not the selectivity kinds")
        a = e[e["grade"] == "A"]
        if not (a["kind"].str.startswith("genotype") & (a["q"] < 0.05) & (a["n_altered"] >= 5) & (a["n_intact"] >= 5)
                & ~a["alerts"].str.contains("tissue-confounded|co-occurs with|compared across organs|exists only "
                                            "relative|significant within this|sit on the other side")).all():
            bad.append("a grade-A edge breaks the A rule")
        if not (e.loc[e["kind"].str.startswith("genotype") & e["alerts"].str.contains("tissue-confounded"),
                      "grade"] == "C").all():
            bad.append("a tissue-confounded genotype edge is not grade C")
        if not (e.loc[e["kind"].str.startswith("genotype") & ~_table_wide(e), "grade"] == "C").all():
            bad.append("an edge significant only within its group is not grade C")
        dt = e[e["kind"] == "drug_target"]
        sup_ok = all(set(s_.split("; ")) <= set(c_.split("; ")) for s_, c_ in zip(dt["compounds_supporting"],
                                                                                 dt["compounds"]))
        if not (len(dt) == 0 or ((dt["compounds"] != "").all() and sup_ok
                                 and dt["drug_effect"].isin(["raises", "lowers"]).all())):
            bad.append("drug_target compounds / compounds_supporting / drug_effect")
        if (e.loc[e["kind"] != "drug_target", ["compounds", "compounds_supporting", "drug_effect"]] != "").any().any():
            bad.append("compounds columns filled for another kind")
        return not bad, (f"{len(e):,} edges, by kind {e['kind'].value_counts().to_dict()}, by grade "
                         f"{e['grade'].value_counts().to_dict()}; problems: {bad or 'none'}")
    check("direction", "every edge has p, q, grade, kind, sign and alerts in the right format (and the grade rules)",
          edge_format)

    def rise_fall():
        """rise_share on the response kinds only; the 'rises at some ... falls at others' alert exactly where each
        direction carries >= MIXED of the evidence; a one-way target's reading leads with a drug-dose of its main
        direction (pooled z of that drug-dose, atlas/effects), never with a minority one going the other way."""
        bad = []
        resp = e["kind"].isin(DV.RESPONSE)
        rs = e["rise_share"].to_numpy(float)
        if not (np.isfinite(rs[resp.to_numpy()]).all() and ((rs[resp.to_numpy()] >= 0) & (rs[resp.to_numpy()] <= 1))
                .all() and np.isnan(rs[~resp.to_numpy()]).all()):
            bad.append("rise_share not in [0, 1] on the response kinds, or set on another kind")
        mixed = resp & (e["rise_share"] >= Dm.MIXED) & (e["rise_share"] <= 1 - Dm.MIXED)
        has = e["alerts"].str.contains(" falls at others", regex=False)
        if not (mixed == has).all():
            bad.append(f"mixed alert on {int((has & ~mixed).sum())} edges that are not mixed, missing on "
                       f"{int((mixed & ~has).sum())} that are")
        dd = pd.read_csv(os.path.join(out, "atlas", "effects", "drugdose.csv"), dtype={"drug": str, "dose": str})
        Z = np.load(os.path.join(out, "atlas", "effects", "DD_z.npy"), mmap_mode="r")
        lab = {Dm._dd_label(a, b): i for i, (a, b) in enumerate(zip(dd["drug"].astype(str), dd["dose"].astype(str)))}
        one = e[e["kind"].isin(["genotype_response", "null_response"]) & ~mixed & (e["top_drugdoses"] != "")]
        wrong, n = [], 0
        for r in one.itertuples(index=False):
            first = str(r.top_drugdoses).split("; ")[0].rsplit(": ", 1)[0]
            d = lab.get(first)
            if d is None:
                wrong.append(f"{r.source}->{r.target}: '{first}' not a drug-dose label")
                continue
            n += 1
            up = float(Z[d, int(r.target_col)]) > 0
            if up != (float(r.rise_share) > 0.5) or f"at {first}" not in str(r.reading):
                wrong.append(f"{r.source}->{r.target} ({r.rise_share:.2f} from rises) leads with {first}")
        if wrong:
            bad.append("; ".join(wrong[:4]))
        x = e[(e["source"] == "TP53") & (e["target"] == "RPS27L") & (e["kind"] == "genotype_response")]
        rp = (f"TP53 -> RPS27L: {float(x['rise_share'].iloc[0]):.0%} from rises, reading "
              f"'{str(x['reading'].iloc[0]).split(': ', 1)[-1][:70]}'") if len(x) else "no TP53 -> RPS27L edge"
        return not bad, (f"{int(resp.sum())} response edges, {int(mixed.sum())} mixed (alerted), {n} one-way ones "
                         f"checked for their headline drug-dose; {rp}; problems: {bad or 'none'}")
    check("direction", "rise or fall: rise_share, the mixed alert, a one-way target's headline drug-dose in its main "
                       "direction", rise_fall)

    def tp53_targets():
        p53 = set(sets.get("P53_ACTIVITY") or [])
        r = e[(e["kind"] == "genotype_response") & (e["source"] == "TP53") & e["target"].isin(p53)]
        ab = r[(r["sign"] == 1) & r["grade"].isin(["A", "B"])]
        return (len(ab) >= 2 and "CDKN1A" in set(ab["target"]) and (r["sign"] == -1).sum() == 0,
                f"TP53 -> {len(r)} of the {len(p53)} planted p53 targets; sign +1 at grade A / B: "
                f"{ab[['target', 'grade']].values.tolist()}; with sign -1: {int((r['sign'] == -1).sum())}")
    check("direction", "TP53 -> CDKN1A and other p53 targets (sign +1, grade A or B)", tp53_targets)

    def tp53_cells():
        s = e[(e["kind"] == "genotype_sensitivity") & (e["source"] == "TP53")]
        st = s[_table_wide(s)]
        got = [w for w in DNA_DAMAGE_5UM if ((st["target"] == f"cells under {w} µM") & (st["sign"] == -1)).any()]
        return (len(got) >= 2 and (st["sign"] == 1).sum() == 0,
                f"{len(got)} of the 3 DNA-damaging drugs at 5 µM over the whole table with sign -1 (TP53 activity "
                f"makes the cells more sensitive): {got}; table-wide with sign +1: {int((st['sign'] == 1).sum())}")
    check("direction", "TP53 -> cells under the DNA-damaging drugs (sign -1)", tp53_cells)

    def nfe2l2_level():
        p = planted.get("nfe2l2_level")
        if not p:
            return False, "ground_truth.json has no direction.nfe2l2_level (old synthetic data: run with --regen)"
        tg = set(p["targets"])
        lv = e[(e["kind"] == "level") & (e["source"] == p["source"]) & e["target"].isin(tg)]
        right = lv[lv["sign"] == 1]
        clr = e["direction_clear"].fillna(False).astype(bool)
        clear = int(right["direction_clear"].fillna(False).astype(bool).sum())
        rev = e[(e["kind"] == "level") & (e["target"] == p["source"]) & e["source"].isin(tg) & clr]
        # an unplanted level edge (the shuffled-level control expects a few false ones) called 'direction clear':
        # the direction test allows for an edge having been selected because it is strong, so none should be
        other = e[(e["kind"] == "level") & ~((e["source"] == p["source"]) & e["target"].isin(tg)) & clr]
        unclear_ok = bool(lv.loc[~lv["direction_clear"].fillna(False).astype(bool),
                                 "alerts_all" if "alerts_all" in lv else "alerts"].fillna("").str.contains(
            "allowed for that this arrow was written because it is strong|could not be tested").all())
        # the precision reason is a kind caveat since direction VERSION 3 (caveats; alerts_all keeps every reason)
        reasons = lv["alerts_all"] if "alerts_all" in lv else lv["alerts"]
        alert_ok = bool(reasons.fillna("").str.contains("a stronger correlation one way").all()) and \
            bool((lv["grade"] == "C").all()) and unclear_ok
        return (len(right) >= NFE2L2_MIN and len(right) == len(lv) and len(rev) == 0 and len(other) == 0
                and alert_ok,
                f"level edges {p['source']} -> {len(right)} of the {len(tg)} NRF2 targets with sign +1 "
                f"({len(lv) - len(right)} other sign), {clear} with the direction clear (with 18 lines, few pass "
                f"once the selection is allowed for), r {right['r'].round(2).tolist()}, q max "
                f"{right['q'].max() if len(right) else float('nan'):.3g}; reverse edges (a target's level -> "
                f"{p['source']}) called clear: {len(rev)}; unplanted level edges called clear: {len(other)}; grade C "
                f"with the precision alert and, where unclear, the selection reason: {alert_ok}")
    check("direction", "a gene's natural level -> its partners' response (NFE2L2 -> NRF2 targets; no reverse or "
          "unplanted edge called 'direction clear')", nfe2l2_level)

    def null_partners():
        p = planted.get("gluco_coactivator_null")
        if not p:
            return False, "ground_truth.json has no direction.gluco_coactivator_null (run with --regen)"
        tg = set(p["partners"])
        r = e[(e["kind"] == "null_response") & (e["source"] == p["source"]) & e["target"].isin(tg)]
        right = r[(r["sign"] == 1) & (r["grade"] == "B")]
        g = pd.read_parquet(os.path.join(dr, "groups.parquet"))
        g = g[(g["kind"] == "null") & (g["gene"] == p["source"])]
        lines_ok = len(g) == 1 and set(g["altered_lines"].iloc[0].split(", ")) == set(p["lines"]) and \
            bool(g["stratified"].iloc[0]) and not bool(g["tissue_confounded"].iloc[0])
        return (len(right) >= 0.6 * len(tg) and (r["sign"] == -1).sum() == 0 and lines_ok,
                f"{p['source']} not expressed in {len(p['lines'])} lines -> {len(right)} of its {len(tg)} planted "
                f"partners as null_response with sign +1 at grade B (q max "
                f"{right['q'].max() if len(right) else float('nan'):.2g}); sign -1: {int((r['sign'] == -1).sum())}; "
                f"its line set found and compared within organs, not tissue-confounded: {lines_ok}")
    check("direction", "a natural knockout -> its partners respond less (null_response, sign +1, grade B)",
          null_partners)

    def controls():
        s = ctl["negative"]["pseudo"]
        ef = ctl["expected_false_edges"]
        tw = {k: v["edges_mean_per_group"] for k, v in s.items()}
        wg = {k: v["within_group_edges_mean_per_group"] for k, v in s.items()}
        lv_ok = all((ef[k]["expected_false"] or 0) <= 0.1 * ef[k]["edges"] + 3 for k in ("level", "level_sensitivity"))
        ok = (all((v or 0) <= 0.1 for v in tw.values()) and all((v or 0) <= 0.25 for v in wg.values()) and lv_ok
              and s["response"]["groups"] >= 50)
        return ok, (f"random pseudo-groups ({s['response']['groups']}): edges per group over the whole table {tw}, "
                    f"within their group only {wg}; permuted levels: level {ef['level']['expected_false']} expected "
                    f"false of {ef['level']['edges']}, level_sensitivity {ef['level_sensitivity']['expected_false']} "
                    f"of {ef['level_sensitivity']['edges']}")
    check("direction", "negative controls (random pseudo-groups, permuted levels) are not above what is expected",
          controls)

    def view():
        dv = DV.load(out, cache=False)
        rows = dv.rows
        mem = sorted(i for m in rows["members"] for i in m)
        part = mem == list(range(len(e)))
        multi = rows[rows["n_sources"] > 1]
        same_test = all(len(set(dv.edges.set_index("edge_id").loc[list(m), "p"])) == 1 for m in multi["members"])
        gi = {"A": 0, "B": 1, "C": 2}
        o = rows["grade"].map(gi).to_numpy()
        ordered = bool((np.diff(o) >= 0).all()) and all(
            (np.diff(rows.loc[rows["grade"] == g_, "q"].to_numpy(float)) >= -1e-15).all() for g_ in gi)
        tp = dv.downstream("TP53")
        up = dv.upstream(col["CDKN1A"]) if "CDKN1A" in col else dv.upstream("CDKN1A")
        ce = dv.cells("TP53")
        cons = (len(tp) == int(((e["source"] == "TP53") & (e["target_type"] == "gene")).sum())
                and (up["target"] == "CDKN1A").all() and ce["target_type"].isin(DV.DRUGDOSE_TARGETS).all()
                and "TP53" in set(up["source"]))
        dt = dv.for_drug("Dexamethasone")["targets"]
        shown, n_more, n_alert = DV.cap(rows, 5)
        cap_ok = len(shown) >= min(5, len(rows)) and len(shown) + n_more == len(rows)
        line = DV.edge_line(tp.iloc[0]) if len(tp) else ""
        asc = DV.ascii_signs(line)
        sw = DV.sign_word(tp["sign"].iloc[0], tp["kind"].iloc[0]) if len(tp) else "?"
        txt_ok = ("TP53 → " in line and "TP53 -> " in asc and "→" not in asc and "⚠" not in asc
                  and f"activity {sw} " in line and f"[{tp['grade'].iloc[0]}]" in line
                  and (sw in ("strengthens", "weakens")) == (tp["kind"].iloc[0] in DV.RESPONSE))
        return (part and same_test and ordered and cons and len(dt) > 0 and cap_ok and txt_ok,
                f"{len(e):,} edges in {len(rows):,} display rows (every edge in exactly one: {part}; {len(multi)} rows "
                f"name several sources, each one test: {same_test}); in ORDER {ordered}; TP53 downstream "
                f"{len(tp)}, CDKN1A upstream {len(up)}, TP53 -> cells {len(ce)}: consistent {cons}; Dexamethasone's "
                f"drug_target rows {len(dt)}; cap(5) shows {len(shown)}, {n_more} more ({n_alert} with an alert); "
                f"'{DV.ascii_signs(line)[:90]}'")
    check("direction", "direction_view: every edge in one display row, in order, look-ups, cap rule, wording", view)

    def registered():
        import shutil
        import tempfile
        tmp = tempfile.mkdtemp(prefix="tahoe_dir_status_")
        try:
            os.makedirs(os.path.join(tmp, "stages"))
            for f in os.listdir(os.path.join(out, "stages")):
                if f.endswith(".json") and f != "direction.json":
                    shutil.copy2(os.path.join(out, "stages", f), os.path.join(tmp, "stages", f))
            r = subprocess.run([sys.executable, "-m", "tahoemap", "status", "--out", tmp, "--offline"], cwd=REPO,
                               capture_output=True, text=True, encoding="utf-8", errors="replace")
        finally:
            shutil.rmtree(tmp, ignore_errors=True)
        nxt = [ln for ln in r.stdout.splitlines() if ln.startswith("next:")]
        return (r.returncode == 0 and bool(nxt)
                and nxt[0].startswith("next: direction -> validate -> vault -> map -> explorer "),
                f"an output whose stages are all done but direction: {nxt[0] if nxt else r.stdout[-300:]}")
    check("direction", "registered after graph: a finished older output runs direction, validate, vault, map, "
          "explorer",
          registered)

    def report():
        rp = os.path.join(out, "validation", "report.md")
        txt = open(rp, encoding="utf-8").read() if os.path.exists(rp) else ""
        m = json.load(open(os.path.join(out, "validation", "metrics.json"), encoding="utf-8")) \
            if os.path.exists(os.path.join(out, "validation", "metrics.json")) else {}
        d = m.get("direction") or {}
        ok = ("## 10. Direction" in txt and "Positive controls" in txt and "expected false" in txt
              and d.get("edges") == len(e) and bool(d.get("positive")) and bool(d.get("synthetic")))
        return ok, (f"report section 10: {'## 10. Direction' in txt}; metrics.json direction: edges {d.get('edges')}, "
                    f"positive controls {list((d.get('positive') or {}))[:2]}, planted answers "
                    f"{d.get('synthetic')}")
    check("direction", "validation report: the Direction section (controls, expected false edges, planted answers)",
          report)


NFE2L2_MIN = 6              # level edges NFE2L2 -> NRF2 targets the synthetic run must give (18 lines: a weak test)


# ---------------------------------------------------------------- the vault's direction sections (tahoemap/vault.py)
def vault_direction(out, col, gK, null_src="SYNTH0881"):
    """The vault's direction sections on the synthetic run: the concept note (generated, linked from Home, with the
    controls of direction/controls.json); every gene note has 'Direction (probable)', its arrows are those of
    direction_view (vault.direction_positions == upstream / downstream / cells for every gene; the frontmatter
    counts); CDKN1A's upstream table has TP53 at its grade with its sign words (and At a glance says so); TP53's
    downstream list follows the cap rule and names the cells under a drug-dose; a drug note lists the genes that set
    how its cells fare and its drug-target arrows; a line note lists its genotype groups and natural knockouts with
    their arrows; an output without the stage reads 'has not run' in each section, without a crash."""
    import contextlib
    import io
    from tahoemap import direction_view as DV
    from tahoemap import vault as V
    vt = os.path.join(out, "vault")
    dv = DV.load(out, cache=False)
    if dv is None:
        return False, "no direction stage in this output (direction/edges.parquet)"
    notes = {}
    for root, _d, files in os.walk(vt):
        for f in files:
            if f.endswith(".md"):
                notes[f[:-3]] = os.path.join(root, f)

    def text(name):
        return open(notes[name], encoding="utf-8").read() if name in notes else ""

    def part(t, head, stop="\n## "):
        return t.split(head, 1)[1].split(stop, 1)[0] if head in t else ""
    bad = []
    cn = text(V.DIR_NOTE)
    if not (cn.startswith("---") and 'generated_by: "tahoemap"' in cn and "**Positive controls**" in cn
            and "| Expected false |" in cn and "[[CDKN1A]] (rank" in cn and f"[[{V.DIR_NOTE}]]" in text("Home")):
        bad.append("concept note / Home")
    genes = [p for p in notes.values() if f"{os.sep}Genes{os.sep}" in p and not p.endswith(" — plates.md")]
    miss = [os.path.basename(p) for p in genes if "\n## Direction (probable)\n" not in open(p, encoding="utf-8").read()]
    if miss or len(genes) < gK:
        bad.append(f"gene notes without the section: {miss[:3]}")
    pos = V.direction_positions(dv)
    empty = np.zeros(0, dtype=np.int64)
    off = [c for c in range(gK) for role, fn in (("up", dv.upstream), ("down", dv.downstream), ("cells", dv.cells))
           if not np.array_equal(fn(c)["order"].to_numpy(dtype=np.int64), pos[role].get(c, empty))]
    if off:
        bad.append(f"direction_positions differ from the look-ups for cols {off[:5]}")
    t = text("CDKN1A")
    up = part(t, "### Upstream of this gene", "\n### ")
    tr = dv.upstream("CDKN1A")
    tr = tr[tr["source"] == "TP53"]
    g0 = str(tr["grade"].iloc[0]) if len(tr) else "?"
    # direction VERSION 5 group words (D15): 'TP53 change recorded as loss of function in 10 lines (8 missense, 2
    # truncating, splice or deletion) vs 8 not recorded' (was 'recorded loss-of-function mutation of TP53 in ...')
    if not (len(tr) and re.search(rf"^\| \[\[TP53\]\] \| {g0} \| TP53 activity strengthens CDKN1A's drug response \| "
                                  r"TP53 change recorded as loss of function in \d+ lines \([^|]*\) vs \d+ not "
                                  r"recorded \|", up, re.M)
            and f"[[TP53]] → it (grade {g0}" in part(t, "> [!summary] In this data", "\n\n")
            and f"direction_upstream: {len(pos['up'].get(col['CDKN1A'], empty))}" in t):
        bad.append(f"CDKN1A: TP53 upstream at grade {g0} (table, At a glance, frontmatter)")
    t = text("TP53")
    dn = np.union1d(pos["down"].get(col["TP53"], empty), pos["cells"].get(col["TP53"], empty))
    sec = part(t, "### Downstream of this gene")
    rows = [x for x in sec.splitlines() if x.startswith("| ") and not x.startswith("| Target |")]
    al = dv.rows["has_alert"].to_numpy(dtype=bool)[dn]
    keep = V.cap_keep(al, V.N_DIRECTION)
    more = DV.more_text(len(dn) - len(keep), int(al.sum() - al[keep].sum()), "arrows")
    # the first row shown is direction_view's first (BAX on seed 0 since the TOP2-poison plant; CDKN1A before), and a
    # 'cells under' row is expected only when the cap keeps one
    first = dv.rows.iloc[int(dn[keep[0]])] if len(keep) else None
    kept_types = set(dv.rows["target_type"].astype(str).to_numpy()[dn][keep]) if len(keep) else set()
    first_cell = (f"| [[{first['target']}]] | {first['grade']} |" if first is not None
                  and str(first["target_type"]) == "gene" else "| cells under [[")
    if not (f"*{len(dn):,} arrows" in sec and len(rows) == len(keep) and (more in sec if more else True)
            and ("| cells under [[" in sec if "cells" in kept_types else True) and rows
            and rows[0].startswith(first_cell) and f"direction_downstream: {len(dn)}" in t):
        bad.append(f"TP53 downstream: {len(dn)} arrows, {len(rows)} rows shown, cap keeps {len(keep)}; '{more}'")
    drug = _tp53_cells_drug(dv)            # Doxorubicin on seed 0 (the drug of a TP53 -> cells row)
    ce = dv.cells("TP53")
    ce = ce[ce["target_drug"].astype(str) == drug] if drug else ce.iloc[:0]
    dox = text(f"{drug} (drug)") if drug else ""
    dex = text("Dexamethasone (drug)")
    n_dex = len(dv.drug_targets("Dexamethasone"))
    if not (len(ce) and re.search(rf"^\| \[\[TP53\]\] \| {re.escape(str(ce['target_dose'].iloc[0]))} µM \| "
                                  rf"{ce['grade'].iloc[0]} \| TP53 activity lowers the cells' numbers",
                                  part(dox, "### Genes that set how the cells fare under it", "\n### "), re.M)
            and "*Drug-target arrows" in dex and f" {n_dex:,} arrow" in part(dex, "### Its targets")
            and "| NR3C1 | [[" in part(dex, "### Its targets")):
        bad.append(f"drug notes ({drug or 'no DNA-damaging drug'}: TP53 -> cells; Dexamethasone: {n_dex} "
                   "drug-target arrows)")
    g = dv.groups
    tp = g[g["group_id"] == "genotype:TP53:LoF"]
    nl = g[g["group_id"] == f"null:{null_src}"]
    lines_ok = len(tp) == 1 and len(nl) == 1
    if lines_ok:
        lt = text(f"{tp['altered_lines'].iloc[0].split(', ')[0]} (line)")
        n_by = [int(((dv.rows["group"] == nl["description"].iloc[0]) & (dv.rows["kind"] == f"null_{k}")).sum())
                for k in ("response", "baseline", "sensitivity", "selectivity")]
        ln = text(f"{nl['altered_lines'].iloc[0].split(', ')[0]} (line)")
        # four arrow counts since direction VERSION 5 (response / level / cells / selectivity); the group words
        # 'TP53 recorded as loss of function (...)' (D15)
        lines_ok = ("| [[TP53]] | TP53 recorded as loss of function (" in part(lt, "### Its recorded alterations",
                                                                             "\n### ")
                    and re.search(rf"^\| \[\[{null_src}\]\] \| \d+ vs \d+ \| {n_by[0]} / {n_by[1]} / {n_by[2]} / "
                                  rf"{n_by[3]} \|", part(ln, "### Genes it does not express"), re.M) is not None)
    if not lines_ok:
        bad.append(f"line notes (TP53 loss-of-function group; {null_src} natural knockout with its arrows)")
    # an output without the stage: the sections say so (rendered in memory; the run's vault is not touched)
    load = DV.load
    try:
        DV.load = lambda *_a, **_k: None
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            v = V.Vault(out)
            v.R.load_gene_tables()
            v.load_fragments()
            v.assign_names()
            v.load_literature()
            v.load_direction()
            written = {}
            v.W = type("W", (), {"write": lambda self, rel, txt: written.__setitem__(rel, txt)})()
            v.direction_note()
            v.home()
            d0 = str(v.R.dd_drug[0])
            old = [v.gene_note(col["TP53"]), "\n".join(v.sec_direction_drug(d0, [0])),
                   "\n".join(v.sec_direction_line(0)), written.get(f"Concepts/{V.DIR_NOTE}.md", "")]
    finally:
        DV.load = load
    if not (all(V.DIR_NOT_RUN in x for x in old) and "direction_upstream: null" in old[0]
            and "not computed: the direction stage has not run" in written.get("Home.md", "")):
        bad.append("an output without the direction stage")
    return not bad, (f"{len(genes):,} gene notes with the section; {len(dv.rows):,} arrows; TP53 downstream "
                     f"{len(dn)} ({len(rows)} shown); Dexamethasone drug-target arrows {n_dex}; problems: "
                     f"{bad or 'none'}")


# ---------------------------------------------------------------- the second wave: every new rule on planted data
# Files that may use atlas_core's own flag list (it cannot change: a verbatim port); every other module reads
# common.ARTIFACT_FLAGS / common.has_artifact (the seven + 'like a neighbouring well').
ATLAS_FLAG_FILES = ("tahoemap/atlas_core.py", "tahoemap/common.py", "tests/test_port.py")


def atlas_flag_users(root=REPO):
    """[(file, line, what)]: every use of atlas_core's has_artifact or ARTIFACT_FLAGS in a Python file of tahoemap/,
    tests/ or tools/ other than ATLAS_FLAG_FILES, read as a syntax tree: an import of the two names from atlas_core
    (or *), or an attribute has_artifact / ARTIFACT_FLAGS of a name bound to the atlas_core module."""
    import ast
    names, hits = {"has_artifact", "ARTIFACT_FLAGS"}, []
    for top in ("tahoemap", "tests", "tools"):
        for dp, dirs, files in os.walk(os.path.join(root, top)):
            dirs[:] = sorted(d for d in dirs if d != "__pycache__")
            for f in sorted(files):
                if not f.endswith(".py"):
                    continue
                path = os.path.join(dp, f)
                rel = os.path.relpath(path, root).replace(os.sep, "/")
                if rel in ATLAS_FLAG_FILES:
                    continue
                try:
                    with open(path, encoding="utf-8") as fh:
                        tree = ast.parse(fh.read(), filename=rel)
                except (SyntaxError, UnicodeDecodeError) as e:
                    hits.append((rel, getattr(e, "lineno", 0) or 0, f"cannot be read: {e}"))
                    continue
                mods = set()                                    # names bound to the atlas_core module
                for n in ast.walk(tree):
                    if isinstance(n, ast.Import):
                        mods |= {a.asname or a.name for a in n.names if a.name.split(".")[-1] == "atlas_core"}
                    elif isinstance(n, ast.ImportFrom):
                        if (n.module or "").split(".")[-1] == "atlas_core":
                            hits += [(rel, n.lineno, f"from {n.module} import {a.name}") for a in n.names
                                     if a.name in names or a.name == "*"]
                        else:
                            mods |= {a.asname or a.name for a in n.names if a.name == "atlas_core"}
                for n in ast.walk(tree):
                    if isinstance(n, ast.Attribute) and n.attr in names:
                        base = ast.unparse(n.value)
                        if base in mods or base.split(".")[-1] == "atlas_core":
                            hits.append((rel, n.lineno, f"{base}.{n.attr}"))
    return hits


def _tokens(flags):
    return [t for t in str(flags or "").split("; ") if t]


def wave2_checks(out, data, truth, check, col, gK):
    """The rules the second wave added (packages W1-W7), on the planted answers of ground_truth.json: the shared
    artifact-flag list; clean = not common.has_artifact on every table; the neighbouring-well rule (tiers, tokens,
    the per-gene reading, the validation section, the module and direction drug lists); the translation-inhibitor
    caveat; dose and plate; the rough DMSO-referenced fold change; drug_line_response (growth, response strength,
    selectivity); TP53 'not recorded'; Tahoe and ChEMBL annotations and mechanism classes; the tables README; the
    direction VERSION 5 rules (test_direction.v5_checks, D1-D17), the drug-target classes and the stage order; the
    relations, embed and graph rules (lineage pairs, read-sharing copies, counts in two units, drug-dose similarity,
    covariates, partner preservation, modules.gmt); and the validation report's new sections and labels. A planted
    effect that the synthetic data make too small to detect is a WARN with the reason (named in the detail)."""
    from tahoemap import common as CM
    from tahoemap import tables as TB
    tb = os.path.join(out, "tables")
    fx = os.path.join(out, "atlas", "effects")

    def code_flags():
        h = atlas_flag_users()
        n = len(CM.ARTIFACT_FLAGS)
        return (not h and n == 8 and CM.ARTIFACT_FLAGS[-1] == CM.NB_FLAG and not set(CM.CAVEAT_FLAGS) &
                set(CM.ARTIFACT_FLAGS),
                f"uses outside {', '.join(ATLAS_FLAG_FILES)}: {h[:5] or 'none'}; common.ARTIFACT_FLAGS holds {n} "
                f"tokens (the atlas's 7 + '{CM.ARTIFACT_FLAGS[-1]}'); caveat tokens never artifacts: "
                f"{list(CM.CAVEAT_FLAGS)}")
    check("code", "only atlas_core.py, common.py and tests/test_port.py use atlas_core's has_artifact / "
                  "ARTIFACT_FLAGS (every other module reads common's list of 8)", code_flags)

    if not os.path.exists(os.path.join(tb, "drug_line_response.parquet")):
        check("tables", "second-wave tables (tables VERSION 5)",
              lambda: (False, "no tables/drug_line_response.parquet: an older tables stage"))
        return
    dd = pd.read_parquet(os.path.join(tb, "drugdoses.parquet"))
    de = pd.read_parquet(os.path.join(tb, "drug_effects.parquet"))
    genes = pd.read_parquet(os.path.join(tb, "genes.parquet"))
    drugs = pd.read_parquet(os.path.join(tb, "drugs.parquet"))
    lines_t = pd.read_parquet(os.path.join(tb, "lines.parquet"))
    dlr = pd.read_parquet(os.path.join(tb, "drug_line_response.parquet"))
    dlt = pd.read_parquet(os.path.join(tb, "drug_line_top.parquet"))
    le = pd.read_parquet(os.path.join(tb, "line_effects.parquet"))
    info = json.load(open(os.path.join(tb, "info.json"), encoding="utf-8"))
    sets = _sets(truth)

    def ddrow(drug, dose):
        """The drugdoses.parquet row of a planted drug (its name with or without the salt in brackets) at a dose."""
        m = ((dd["drug"].str.replace(r" \(.*\)$", "", regex=True) == drug) | (dd["drug"] == drug)) & \
            (dd["conc"].astype(float) == float(dose))
        if int(m.sum()) != 1:
            raise ValueError(f"{drug} {dose}: {int(m.sum())} drug-doses")
        return dd[m].iloc[0]

    # ------------------------------------------------ clean = not common.has_artifact, on every table
    def clean_rule():
        n, bad = 0, {}
        for name, df in (("drug_effects", de), ("drug_line_top", dlt)):
            want = np.array([not CM.has_artifact(f) for f in df["flags"]], dtype=bool)
            bad[name] = int((df["clean"].to_numpy(dtype=bool) != want).sum())
            n += len(df)
        for p in ("best_up", "best_down"):
            sub = le[le[f"{p}_dd_all"] >= 0]
            want = np.array([not CM.has_artifact(f) for f in sub[f"{p}_flags_all"]], dtype=bool)
            bad[f"line_effects {p}_clean_all"] = int((sub[f"{p}_clean_all"].to_numpy(dtype=bool) != want).sum())
            n += len(sub)
        n_nb = sum(CM.NB_FLAG in _tokens(f) for f in de["flags"])
        return not any(bad.values()), (f"{n:,} rows (drug_effects, drug_line_top, line_effects *_all): clean == not "
                                       f"common.has_artifact(flags); rows that differ {bad}; drug_effects rows with "
                                       f"'{CM.NB_FLAG}' (artifact): {n_nb}")
    check("tables", "clean == not common.has_artifact(flags) on every drug_effects, drug_line_top and line_effects "
                    "*_all row", clean_rule)

    # ------------------------------------------------ neighbouring wells (ground_truth.json neighbour_copy)
    nb = truth.get("neighbour_copy")
    if nb:
        src, dst, top = nb["src"], nb["dst"], nb["top_dst"]
        src_genes = set(nb["genes_up"]) | set(nb["genes_down"])

        def nb_a():
            r, s_ = ddrow(dst, nb["dose_dst"]), ddrow(src, nb["dose_dst"])
            want = [f"{w['plate']} {w['well']} next to {w['next_to'][0]}" for w in nb["wells"] if w["drug"] == dst]
            ok = (r["nb_tier"] == "artifact" and r["nb_partner"] == f"{s_['drug']} {s_['dose']} µM"
                  and int(r["nb_partner_dd"]) == int(s_["dd"]) and all(w in r["nb_where"] for w in want)
                  and CM.NB_FLAG in _tokens(r["flags"]) and CM.NB_FLAG not in _tokens(r["atlas_flags"])
                  and str(r["nb_alert"]).strip() != "")
            return ok, (f"{dst} {r['dose']} µM: tier '{r['nb_tier']}', partner '{r['nb_partner']}', where "
                        f"'{r['nb_where']}' (planted {want}); flags of record '{r['flags']}', atlas flags "
                        f"'{r['atlas_flags']}'; alert: {str(r['nb_alert'])[:160]}")
        check("tables", "(a) neighbouring wells: the planted copy is tier 'artifact' with its partner, wells and token "
                        "(flags of record, not the atlas flags)", nb_a)

        def nb_b():
            r = ddrow(dst, nb["dose_dst"])
            d_ = de[de["dd"] == r["dd"]]
            at = d_[d_["symbol"].isin(src_genes) & (d_["z"].abs() >= 3)]
            other = d_[~d_.index.isin(at.index)]
            ok_at = len(at) > 0 and all(CM.NB_FLAG in _tokens(f) for f in at["flags"]) and not at["clean"].any()
            toks = [_tokens(f) for f in other["flags"]]
            wo = [not CM.has_artifact("; ".join(x for x in t if x not in (CM.NB_FLAG, CM.NB_CLEARED))) for t in toks]
            n_cl = sum(CM.NB_CLEARED in t for t in toks)
            ok_o = (all(CM.NB_FLAG not in t for t in toks) and list(other["clean"]) == wo and n_cl == len(other))
            # every gene at that drug-dose (drug_effects holds only the moved ones): the flag strings the tables
            # stage's own inputs give (tables.gene_flag_inputs, flag_strings): the token on the neighbour's genes,
            # '(not this gene)' on every other gene
            F = TB.gene_flag_inputs(out)
            d = int(r["dd"])
            k, dk = np.arange(gK), np.full(gK, d)
            fs, _cl = TB.flag_strings(F["dd_flags"], dk, F["posunc"][dk, k], F["poseff"][dk, k], F["pscale"][dk, k],
                                      TB.cc_pct(F["cc_share"][dk, k], F["cc_cleared"][dk, k]), F["nb"][dk, k],
                                      F["rise"][dk, k])
            on = np.array([CM.NB_FLAG in _tokens(f) for f in fs])
            off = np.array([CM.NB_CLEARED in _tokens(f) for f in fs])
            sym_of = dict(zip(genes["col"].astype(int), genes["symbol"].astype(str)))
            planted = np.array([sym_of.get(k, "") in src_genes for k in range(gK)])
            ok_all = bool((on == F["nb"][d, :gK]).all() and (on ^ off).all())
            n_pl = int((on & planted).sum())
            return ok_at and ok_o and ok_all and n_pl >= len(at), (
                f"{len(at)} drug_effects rows at the planted genes hold '{CM.NB_FLAG}' and are not clean: {ok_at}; the "
                f"other {len(other)} rows read '{CM.NB_CLEARED}' ({n_cl}) and keep their clean: {ok_o}; over all "
                f"{gK:,} genes at {r['drug']} {r['dose']} µM: {int(on.sum())} carry the token (the genes the "
                f"neighbour moves the same way, {n_pl} of them planted), {int(off.sum())} read '{CM.NB_CLEARED}': "
                f"{ok_all}")
        check("tables", "(b) the per-gene reading: the artifact token only on the genes the neighbour moves the same "
                        "way; the other genes read '(not this gene)' and keep their clean", nb_b)

        def nb_c():
            rt = ddrow(top, nb["dose_top"])
            x = de[(de["dd"] == rt["dd"]) & de["symbol"].isin(src_genes) & (de["z"].abs() >= 3)]
            ok = (rt["nb_tier"] == "top dose" and len(x) > 0 and all(CM.NB_TOP in _tokens(f) for f in x["flags"])
                  and bool(x["clean"].all()) and not CM.has_artifact(CM.NB_TOP))
            return ok, (f"{top} {rt['dose']} µM: tier '{rt['nb_tier']}', partner '{rt['nb_partner']}'; {len(x)} rows "
                        f"at the planted genes hold '{CM.NB_TOP}' and stay clean (a caveat): {bool(x['clean'].all())}")
        check("tables", "(c) a copy at the drug's top dose is tier 'top dose': a caveat token, the rows stay clean",
              nb_c)

        def nb_d():
            s_ = dd[dd["drug"] == ddrow(src, nb["dose_dst"])["drug"]]
            r = ddrow(dst, nb["dose_dst"])
            o = dd[(dd["drug"] == r["drug"]) & (dd["conc"].astype(float) != float(nb["dose_dst"]))]
            tiers = dd[dd["nb_tier"] != ""][["drug", "dose", "nb_tier"]].values.tolist()
            ok = (s_["nb_tier"] == "").all() and (o["nb_tier"] == "").all() and int((dd["nb_tier"] == "artifact")
                                                                                       .sum()) == 1
            return ok, (f"source {src}: tiers {list(s_['nb_tier'])}; {dst}'s other doses {list(o['nb_tier'])}; every "
                        f"drug-dose with a tier: {tiers}")
        check("tables", "(d) the source well and the copy's other doses have no tier; no other artifact tier", nb_d)

        def nb_e():
            r = ddrow(dst, nb["dose_dst"])
            g_ = genes[genes["symbol"].isin(set(nb["genes_up"]))]
            n = int((g_["best_clean_up_dd"] == r["dd"]).sum())
            return n == 0, (f"{len(g_)} planted up genes: best clean raiser is {dst} {r['dose']} µM for {n} (it is "
                            "flagged on them, so never their best clean raiser)")
        check("tables", "(e) the flagged copy is never a planted gene's best clean raiser", nb_e)

        def nb_f():
            nr = info.get("neighbour_rule") or {}
            tier = dd[dd["nb_tier"] != ""]
            rec = {(int(x["dd"]), x["tier"], x["partner"], x["where"]) for x in nr.get("tier_drugdoses", [])}
            got = {(int(a), b, c_, w) for a, b, c_, w in zip(tier["dd"], tier["nb_tier"], tier["nb_partner"],
                                                             tier["nb_where"])}
            cnt = tier["nb_tier"].value_counts().to_dict()
            ok = (info.get("version") == TB.VERSION and rec == got
                  and all(int(nr.get("drugdoses", {}).get(k, 0)) == int(cnt.get(k, 0)) for k in TB.NB_TIERS)
                  and nr.get("constants", {}).get("NB_SHARE") == TB.NB_SHARE)
            return ok, (f"tables version {info.get('version')}; info.json neighbour_rule: pairs judged "
                        f"{nr.get('pairs_judged')}, passing {nr.get('pairs_passing')}, drug-doses "
                        f"{nr.get('drugdoses')}, expected by chance {nr.get('expected_passes')}; = "
                        f"drugdoses.parquet's tiers {cnt}: "
                        f"{rec == got}")
        check("tables", "(f) tables VERSION 5: info.json neighbour_rule names the same tiers, partners and wells as "
                        "drugdoses.parquet", nb_f)

        def nb_validation():
            rp = os.path.join(out, "validation", "report.md")
            rep = open(rp, encoding="utf-8").read() if os.path.exists(rp) else ""
            if "## 4. " not in rep:
                return False, "validation/report.md has no section 4"
            s4 = rep.split("## 4. ", 1)[1].split("\n## 5. ", 1)[0]
            r, rt = ddrow(dst, nb["dose_dst"]), ddrow(top, nb["dose_top"])
            nbinfo = info["neighbour_rule"]
            t3 = [ln for ln in s4.split("\n") if ln.startswith("| ") and "explorer" in ln and "](" in ln]
            okr = (any(f"{r['drug']} {r['dose']} µM" in x and "| artifact |" in x for x in t3)
                   and any(f"{rt['drug']} {rt['dose']} µM" in x and "| top dose |" in x for x in t3)
                   and len(t3) == int((dd["nb_tier"] != "").sum()))
            okc = (all(f"| {o['orientation']} | {o['judged']:,} | {o['resembling']:,} |" in s4
                       for o in nbinfo["orientation"])
                   and all(f"| {t} | {nbinfo['pairs_passing'][t]} |" in s4 for t in nbinfo["pairs_passing"]))
            return okr and okc, (f"section 4 table: {len(t3)} rows = drug-doses with a tier "
                                 f"{int((dd['nb_tier'] != '').sum())}; {dst} {r['dose']} 'artifact' and {top} "
                                 f"{rt['dose']} 'top dose' listed: {okr}; orientation and passing counts = "
                                 f"tables/info.json neighbour_rule {nbinfo['pairs_passing']}: {okc}")
        check("validate", "section 4 (neighbouring wells): the planted artifact and top-dose tiers, one row per "
                          "drug-dose with a tier, the counts of tables/info.json", nb_validation)

        def nb_modules():
            mods = pd.read_parquet(os.path.join(out, "graph", "modules.parquet"))
            r = ddrow(dst, nb["dose_dst"])
            labs = (f"{r['drug']} {r['dose']} µM", f"{r['drug']} {r['dose']} uM")
            items = [it for c_ in ("drugs_up", "drugs_down") for x in mods[c_].fillna("") for it in str(x).split("; ")
                     if it.startswith(labs)]
            ok = len(items) > 0 and all("⚠" in it and CM.NB_FLAG in it for it in items)
            return ok, f"{len(items)} module drug-list items name {labs[0]}, each with its alert: {items[:2]}"
        check("graph", "the module drug lists mark the neighbouring-well copy with '⚠ ... like a neighbouring well'",
              nb_modules)

        def nb_direction():
            from types import SimpleNamespace
            from tahoemap import direction as Dm
            ep = os.path.join(out, "direction", "edges.parquet")
            if not os.path.exists(ep):
                return False, "no direction/edges.parquet"
            e = pd.read_parquet(ep, columns=["source", "target", "top_drugdoses", "drugdoses_all"])
            r = ddrow(dst, nb["dose_dst"])
            fl = TB.dd_flags_of_record(out)
            ns = SimpleNamespace(dd_flags=np.asarray(fl, dtype=object),
                                 dd_art=np.array([CM.has_artifact(f) for f in fl], dtype=bool))
            txt = Dm._flags_text(ns, int(r["dd"]))
            lab = Dm._dd_label(r["drug"], r["dose"])
            segs = [m.group(0) for v in e["drugdoses_all"].fillna("")
                    for m in re.finditer(re.escape(lab) + r":[^;]*", str(v))]
            ok = (txt.startswith(" [artifact flags: ") and CM.NB_FLAG in txt
                  and all("[artifact flags: " in s_ and CM.NB_FLAG in s_ for s_ in segs))
            return ok, (f"the stage's drug-dose list item for {lab} ends '{txt}'; it appears in {len(segs)} edges' "
                        f"drug-dose lists (seed 0: none of the planted genes is a direction target), each with the "
                        f"token: {all(CM.NB_FLAG in s_ for s_ in segs)}")
        check("direction", "the direction drug-dose lists name 'like a neighbouring well' (artifact flags) for the "
                           "copy", nb_direction)
    else:
        check("tables", "neighbouring wells: planted answers", lambda: (
            False, "ground_truth.json has no neighbour_copy (older synthetic data: run with --regen)"))

    # ------------------------------------------------ translation inhibitor (ground_truth.json translation_inhibitor)
    ti = truth.get("translation_inhibitor")
    if ti:
        tl = ti["drug"]

        def tl_flags():
            tld = dd[dd["drug"] == tl]
            h = de[de["drug"] == tl]
            pos, neg = h[h["lfc"] > 0], h[h["lfc"] <= 0]
            ok_dd = len(tld) == 3 and all(CM.TL_DD in _tokens(f) for f in tld["flags"])
            ok_rows = (all(CM.TL_RISE in _tokens(f) for f in pos["flags"])
                       and not any(CM.TL_RISE in _tokens(f) or CM.TL_DD in _tokens(f) for f in neg["flags"]))
            up = set(ti["genes_up"])
            clean_rise = bool((h["symbol"].isin(up) & h["clean"] & h["flags"].map(lambda f: CM.TL_RISE in _tokens(f)))
                              .any())
            tinf = info.get("translation_inhibitors") or {}
            notm = sorted((tinf.get("not_members") or {}).get("TRANSLATION_ELONGATION", {}))
            ok_info = (tinf.get("drug_effects_rows_rise") == len(pos) and tl in (tinf.get("members") or {})
                       and "TOMIVOSERTIB" in notm)
            return ok_dd and ok_rows and clean_rise and ok_info, (
                f"{tl}: {len(tld)} drug-doses with '{CM.TL_DD}': {ok_dd}; {len(pos)} rising rows read '{CM.TL_RISE}', "
                f"{len(neg)} falling rows carry neither token: {ok_rows}; a planted rise stays clean (a caveat): "
                f"{clean_rise}; info.json translation_inhibitors {tinf.get('drugdoses')} drug-doses, "
                f"{tinf.get('drug_effects_rows_rise')} rise rows, documented as not members (Tahoe's 'Protein "
                f"synthesis inhibitor' label): {notm}")
        check("tables", "(g) translation inhibitor: the drug-dose token, 'rise under a translation inhibitor' on its "
                        "rising rows only, caveats never change clean", tl_flags)

        def tl_vault():
            p = os.path.join(out, "vault", "Drugs", f"{tl} (drug).md")
            t = open(p, encoding="utf-8").read() if os.path.exists(p) else ""
            ln = [x for x in t.splitlines() if x.startswith("- Class: ")]
            ok = bool(ln) and "translation inhibitor (blocks the ribosome)" in ln[0] and "code constant (" in ln[0] \
                and "- Tahoe: " in t and re.search(r"- ChEMBL \d+: ", t) is not None
            return ok, f"{os.path.basename(p)}: {ln[0][:200] if ln else 'no class line'}"
        if os.path.isdir(os.path.join(out, "vault")):
            check("vault", "the translation inhibitor's drug note shows its class line with the source, and both "
                           "annotations", tl_vault)

        def tl_validation():
            rp = os.path.join(out, "validation", "report.md")
            rep = open(rp, encoding="utf-8").read() if os.path.exists(rp) else ""
            if "## 1. " not in rep or "## 9. " not in rep:
                return False, "validation/report.md lacks section 1 or 9"
            s1 = rep.split("## 1. ")[1].split("## 2. ")[0] + rep.split("## 9. ")[1].split("## 10. ")[0]
            rows = [ln for ln in s1.split("\n") if ln.startswith("| ") and tl in ln]
            judged = [x for x in rows if len(x.split("|")) > 8 and any(
                tl in y for y in x.split("|")[8].split("<br>")[0].split("; ")[:5])]
            from tahoemap import validate as VA
            ok = bool(rows) and all(VA.TL_WORDS in x and "without translation inhibitors:" in x for x in judged)
            return ok, (f"{len(rows)} rows of sections 1 and 9 name {tl}; {len(judged)} with it among the 5 strongest "
                        f"raisers, each with '{VA.TL_WORDS}' and the 'without translation inhibitors' list")
        check("validate", "sections 1 and 9: the translation-inhibitor caveat words and the raisers without "
                          "translation inhibitors", tl_validation)

    # ------------------------------------------------ dose = plate, DMSO sign check, growth, selectivity, TP53, ...
    def dmso():
        ix = CM.read_effects_index(fx)
        PO = np.load(os.path.join(fx, "plate_offset.npy"))
        pn = ix["plates"]["plate"].astype(str).tolist()
        w = ix["wells"]
        u = w[w["used_in_drugdose"] & (w["drugdose_row"] >= 0)]
        offd = {int(d): [pn.index(p) for p in grp["plate"]] for d, grp in u.groupby("drugdose_row")}
        diff = de["lfc_vs_dmso"].to_numpy(np.float64) - de["lfc"].to_numpy(np.float64)
        exp = np.array([PO[offd[int(d)], int(c)].mean() for d, c in zip(de["dd"], de["col"])])
        fin = np.isfinite(exp)
        ok = np.allclose(diff[fin], exp[fin], atol=1e-5) and bool((np.isnan(diff) == np.isnan(exp)).all())
        cd = int(ix["genes"].index[ix["genes"]["symbol"] == "CDKN1A"][0])
        v = PO[pn.index("plate2"), cd] - np.median(np.delete(PO[:, cd], pn.index("plate2")))
        ds = info.get("dmso_sign_changes") or {}
        return ok and abs(v - 0.62) <= 0.25 and bool(ds.get("plates")), (
            f"{len(de):,} rows: lfc_vs_dmso - lfc = the mean DMSO offset of the used wells' plates (max |diff| "
            f"{np.nanmax(np.abs(diff[fin] - exp[fin])) if fin.any() else float('nan'):.1e}); CDKN1A's planted plate2 "
            f"DMSO offset {v:+.2f} (planted +0.62); info.json dmso_sign_changes over {len(ds.get('plates') or {})} "
            f"plates: {ds.get('sign_changes')} sign changes")
    check("tables", "(h) the rough DMSO-referenced fold change: lfc_vs_dmso = lfc + the plates' DMSO offset",
          dmso)

    def growth():
        Dn, L = len(dd), len(lines_t)
        res, ok = [], len(dlr) == Dn * L
        for c_, f in (("log2_rel_abundance", "DD_A"), ("abundance_z", "DD_Az"), ("response_strength", "DD_beta"),
                      ("response_r", "DD_rcor")):
            a = dlr[c_].to_numpy(np.float32).reshape(Dn, L)
            b = np.load(os.path.join(fx, f + ".npy")).astype(np.float32)
            fin = np.isfinite(b)                 # the finite values bit for bit; NaN exactly where the atlas has NaN
            same = bool((np.isfinite(a) == fin).all() and np.array_equal(a[fin].view(np.uint32),
                                                                         b[fin].view(np.uint32)))
            ok &= same
            res.append(f"{c_} = {f}: {same}")
        lt = lines_t.set_index("line")
        cnt = (dlr["depleted"] & dlr["abundance_trusted"] & dlr["in_growth_analysis"]).groupby(dlr["line"]).sum()
        cnt2 = (dlr["depleted"] & dlr["abundance_trusted"] & dlr["in_growth_analysis"] & dlr["clean"]) \
            .groupby(dlr["line"]).sum()
        okd = all((lt["n_dd_depleted"][x] == cnt.get(x, 0)) or (lt["n_dd_depleted"][x] == -1 and cnt.get(x, 0) == 0)
                  for x in lt.index) and \
            all((lt["n_dd_depleted_clean"][x] == cnt2.get(x, 0)) or
                (lt["n_dd_depleted_clean"][x] == -1 and cnt2.get(x, 0) == 0) for x in lt.index)
        rule = TB.selective_mask(dlr["sel_z"].to_numpy(), dlr["n_genes"].to_numpy())
        ok_sel = bool((dlr["selective"].to_numpy(dtype=bool) == rule).all())
        listed = all(all(n_ in str(r_["selective_lines"]) for n_ in dlr.loc[(dlr["dd"] == r_["dd"]) &
                                                                             dlr["selective"], "cell_name"])
                     and int(r_["n_selective_lines"]) == int(((dlr["dd"] == r_["dd"]) & dlr["selective"]).sum())
                     for _, r_ in dd.iterrows())
        return ok and okd and ok_sel and listed, (
            f"{len(dlr):,} rows = {Dn} drug-doses x {L} lines; {'; '.join(res)} (bit for bit); n_dd_depleted(_clean) "
            f"= its rows: {okd}; selective = sel_z >= {TB.SEL_Z:g} and >= {TB.SEL_MIN_GENES} genes beyond the per-line "
            f"cut on every row: {ok_sel} ({int(dlr['selective'].sum())} selective rows); drugdoses selective_lines / "
            f"n_selective_lines list them: {listed}")
    check("tables", "(i) drug_line_response: growth and response strength bit for bit, the depleted counts, the "
                    "selectivity rule", growth)

    kr = (truth.get("direction") or {}).get("kras_g12_selectivity")
    if kr:
        def kras():
            klines = set(kr["lines"])
            out_, planted_ok, lead_ok = [], True, True
            for dose in kr["doses"]:
                rr = ddrow(kr["drug"], dose)
                s_ = dlr[dlr["dd"] == rr["dd"]]
                sel = s_[s_["selective"]]
                nk, no = int(sel["cell_name"].isin(klines).sum()), int((~sel["cell_name"].isin(klines)).sum())
                planted_ok &= nk >= 4 and no <= 1
                meas = s_[s_["measured"]]
                topk = meas.sort_values("sel_z", ascending=False).head(len(klines))
                n_top = int(topk["cell_name"].isin(klines).sum())
                ng = meas[meas["cell_name"].isin(klines)]["n_genes"].tolist()
                if float(dose) == float(kr["doses"][0]):
                    lead_ok = n_top == len(klines)
                out_.append(f"{rr['drug']} {rr['dose']} µM: {len(meas)} lines measured; the {len(klines)} KRAS "
                            f"codon-12 lines: {n_top} of the top {len(klines)} by sel_z, genes beyond the cut {ng}; "
                            f"selective {nk} KRAS, {no} other")
            if planted_ok:
                return True, "; ".join(out_)
            return ("warn" if lead_ok else False), (
                "; ".join(out_) + f". The KRAS lines lead sel_z at {kr['doses'][0]:g} µM, but selective needs "
                f">= {TB.SEL_MIN_GENES} genes beyond the per-line cut and the plant moves {len(kr['genes'])} genes "
                f"x {kr.get('fold')}: the planted effect is below what the rule can call here (tests/"
                "make_synthetic_tahoe.py KRAS_N, KRAS_FOLD, KRAS_DOSES)")
        check("tables", "(i) KRAS codon-12 selectivity: the planted MEK inhibitor is selective in the KRAS codon-12 "
                        "lines", kras)

    def tp53():
        wtl = {x["cell_name"] for x in truth["lines"] if str(x.get("tp53", "")).lower() in ("wt", "wild type")}
        vals = set(lines_t["tp53_status"])
        ok = vals <= {"altered", "not recorded", "unknown"} and \
            bool((lines_t[lines_t["cell_name"].isin(wtl)]["tp53_status"] == "not recorded").all())
        return ok, (f"tp53_status values {sorted(vals)} (never 'wild type': not recorded is not confirmed); the "
                    f"{len(wtl)} planted TP53-wild-type lines read 'not recorded': "
                    f"{bool((lines_t[lines_t['cell_name'].isin(wtl)]['tp53_status'] == 'not recorded').all())}; "
                    f"info.json tp53_counts {info.get('tp53_counts')}")
    check("tables", "(j) TP53 'not recorded' (never 'wild type')", tp53)

    def dose_plates():
        bad = []
        for _, r_ in drugs.iterrows():
            for part in str(r_["dose_plates"]).split(" / "):
                dz, ws = part.split(": ", 1)
                x = dd[(dd["drug"] == r_["drug"]) & (dd["dose"] == dz)].iloc[0]
                pw = [t.split(" ") for t in ws.split(", ")]
                if set(p for p, _ in pw) != set(str(x["plates"]).split(",")) or \
                        set(w_ for _, w_ in pw) != set(str(x["wells"]).split(",")):
                    bad.append(f"{r_['drug']} {part}")
        m = de.groupby("dd")["n_wells"].first()
        okw = bool((m == dd.set_index("dd")["n_wells"].reindex(m.index)).all())
        share = int(drugs["doses_share_a_plate"].astype(bool).sum())
        dp = info.get("dose_and_plate") or {}
        return not bad and okw and share == dp.get("drugs_with_doses_sharing_a_plate"), (
            f"{len(drugs)} drugs: dose_plates parses back to drugdoses' plates and wells (bad: {bad[:3]}); "
            f"drug_effects n_wells = drugdoses n_wells: {okw}; drugs whose doses share a plate {share} (info.json "
            f"{dp.get('drugs_with_doses_sharing_a_plate')}); wells per drug-dose {dp.get('n_wells')}; e.g. "
            f"'{drugs['dose_plates'].iloc[0]}'")
    check("tables", "(k) dose = plate: dose_plates, doses_share_a_plate, n_wells", dose_plates)

    def annotations():
        mc = drugs.set_index("drug")["mechanism_classes"]
        tl_ = (truth.get("translation_inhibitor") or {}).get("drug", "Harringtonine")
        n_ch = int((drugs["chembl_id"] != "").sum())
        alerts = drugs[drugs["annotation_alert"] != ""]
        ok = ("translation inhibitor" in str(mc.get(tl_, "")) and "TOP2 poison" in str(mc.get("Amsacrine", ""))
              and n_ch == 93 and len(drugs) == 94 and "Carbamazepine" in set(alerts["drug"])
              and {"targets", "moa_fine", "moa_broad", "chembl_mechanisms", "chembl_targets", "annotation_status",
                   "annotation_note"} <= set(drugs.columns))
        return ok, (f"{tl_}: '{mc.get(tl_)}'; Amsacrine: '{mc.get('Amsacrine')}'; ChEMBL ids for {n_ch} of "
                    f"{len(drugs)} drugs (the fixture has no record of HI-TOPK-032); {len(alerts)} with an annotation "
                    f"alert: {alerts[['drug', 'annotation_alert']].values.tolist()[:2]}; Tahoe's targets / moa kept "
                    f"next to ChEMBL's; info.json annotations {info.get('annotations', {}).get('status')}")
    check("tables", "(l) Tahoe and ChEMBL annotations side by side, mechanism classes (offline fixture: 93 of 94 "
                    "drugs matched)", annotations)

    def readme():
        txt = open(os.path.join(tb, "README.md"), encoding="utf-8").read()
        need = ("drug_line_response.parquet", "drugdose_signatures.gmt", "Neighbouring wells", CM.NB_FLAG, CM.TL_RISE,
                "lfc_vs_dmso", "dose_plates")
        miss = [w for w in need if w not in txt]
        gmt = os.path.join(tb, "drugdose_signatures.gmt")
        n_sets = sum(1 for _ in open(gmt, encoding="utf-8")) if os.path.exists(gmt) else -1
        return not info.get("undocumented_columns") and not miss and n_sets == (info.get("gmt") or {}).get("written"), (
            f"undocumented columns: {info.get('undocumented_columns') or 'none'}; words missing from tables/README.md: "
            f"{miss or 'none'}; drugdose_signatures.gmt {n_sets} sets (info.json {info.get('gmt')})")
    check("tables", "(m) tables/README.md documents every column and the new rules; the GMT of call sets", readme)

    def dd_annotations():
        """tables VERSION 7: drugdoses.parquet carries the drug's chembl_mechanisms and annotation_alert, equal to
        drugs.parquet by drug on every row (the same for each dose), documented in the drugdoses section of the README;
        the validation README calls the top-dose tier 'an alert, not an artifact flag' and 'translation inhibitor' a
        caveat (validate VERSION 9)."""
        st = json.load(open(os.path.join(out, "stages", "tables.json"), encoding="utf-8"))
        cols = [c for c in TB.DD_FROM_DRUGS if c in dd]
        ref = drugs.set_index("drug")
        diff = {c: int((dd[c].fillna("").astype(str).to_numpy()
                        != ref.loc[dd["drug"], c].fillna("").astype(str).to_numpy()).sum()) for c in cols}
        txt = open(os.path.join(tb, "README.md"), encoding="utf-8").read()
        sec = txt.split("## drugdoses.parquet", 1)[-1].split("## drugs.parquet", 1)[0]
        doc = all(f"| `{c}` | " in sec and "copied from drugs.parquet" in sec for c in TB.DD_FROM_DRUGS)
        vr = os.path.join(out, "validation", "README.md")
        vtxt = " ".join(open(vr, encoding="utf-8").read().split()) if os.path.exists(vr) else ""
        vok = ("'like a neighbouring well (top dose)', is an alert, not an artifact flag" in vtxt
               and "'translation inhibitor' is a caveat" in vtxt)
        ok = (int(st.get("version", 0)) >= 7 and cols == list(TB.DD_FROM_DRUGS) and not any(diff.values()) and doc
              and vok)
        n_al = int((dd["annotation_alert"].fillna("") != "").sum()) if "annotation_alert" in dd else 0
        return ok, (f"tables version {st.get('version')}; drugdoses columns {cols}; rows that differ from "
                    f"drugs.parquet {diff} (of {len(dd)}; {n_al} drug-doses with an annotation alert); documented in "
                    f"the drugdoses section: {doc}; validation README: top-dose tier an alert, not an artifact flag, "
                    f"'translation inhibitor' a caveat: {vok}")
    check("tables", "(n) drugdoses carries the drug's chembl_mechanisms and annotation_alert (= tables/drugs by "
                    "drug), documented; the validation README's words for the top-dose tier", dd_annotations)

    # ------------------------------------------------ direction VERSION 5 (D1-D17 of tests/test_direction.py)
    dr = os.path.join(out, "direction")
    if os.path.exists(os.path.join(dr, "edges.parquet")):
        e = pd.read_parquet(os.path.join(dr, "edges.parquet"))
        g = pd.read_parquet(os.path.join(dr, "groups.parquet"))
        ctl = json.load(open(os.path.join(dr, "controls.json"), encoding="utf-8"))
        dinfo = json.load(open(os.path.join(dr, "info.json"), encoding="utf-8"))
        try:
            sys.path.insert(0, os.path.join(REPO, "tests"))
            import test_direction as TD
            for name, fn in TD.v5_checks(out, data, e, g, ctl, dinfo, truth):
                check("direction", name, fn)
        except Exception as ex:  # noqa: BLE001
            check("direction", "the VERSION 5 rules (tests/test_direction.py v5_checks)",
                  lambda ex=ex: (False, f"{type(ex).__name__}: {ex}"))

        def dt_classes():
            d = e[e["kind"] == "drug_target"]
            res, ok = [], True
            # MTOR -> RIBI: at least 7 (the 7 genes moved by 3 of the 6 MTOR inhibitors; W1's measure after the plants
            # widened the drug-target test family); the other two classes at least 40% of their set
            for s_, name, sign, need in (("NR3C1", "GLUCO", 1, 0.4), ("MTOR", "RIBI", 1, 7),
                                         ("HMGCR", "CHOL", -1, 0.4)):
                mem = set(sets.get(name, []))
                x = d[(d["source"] == s_) & d["target"].isin(mem)]
                wrong = int((x["sign"] != sign).sum())
                k = need if need >= 1 else need * len(mem)
                ok &= len(x) >= k - 1e-9 and wrong == 0
                res.append(f"{s_} -> {name}: {len(x)} of {len(mem)} (needs {k:g}; wrong sign {wrong})")
            no_inh = not d["reading"].str.contains("inhibiting ", regex=False).any()
            return ok and no_inh, "; ".join(res) + f"; no reading says 'inhibiting': {no_inh}"
        check("direction", "drug-target classes: NR3C1 -> GLUCO and HMGCR -> CHOL >= 40%, MTOR -> RIBI >= 7; readings "
                           "say 'compounds annotated to ...'", dt_classes)

    def stage_order():
        import shutil
        import tempfile
        want = ["build", "effects", "tensor", "reference", "tables", "embed", "relations", "graph", "direction",
                "validate", "vault", "map", "explorer"]
        tmp = tempfile.mkdtemp(prefix="tahoe_stage_order_")
        try:
            os.makedirs(os.path.join(tmp, "stages"))
            for f in os.listdir(os.path.join(out, "stages")):
                if f.endswith(".json") and f != "reference.json":
                    shutil.copy2(os.path.join(out, "stages", f), os.path.join(tmp, "stages", f))
            r = subprocess.run([sys.executable, "-m", "tahoemap", "status", "--out", tmp, "--offline"], cwd=REPO,
                               capture_output=True, text=True, encoding="utf-8", errors="replace")
        finally:
            shutil.rmtree(tmp, ignore_errors=True)
        nxt = [ln for ln in r.stdout.splitlines() if ln.startswith("next:")]
        exp = "next: " + " -> ".join(want[3:]) + " "
        return (list(CM.STAGES) == want and r.returncode == 0 and bool(nxt) and nxt[0].startswith(exp),
                f"common.STAGES {' -> '.join(CM.STAGES)}; an output whose stages are all done but reference: "
                f"{nxt[0] if nxt else r.stdout[-300:]}")
    check("run", "stage order: reference right after tensor; without it every later stage runs again (tables reads "
                 "its drug annotations)", stage_order)

    # ------------------------------------------------ relations, embed, graph (W4)
    rel_p = os.path.join(out, "relations", "gene_relations.parquet")
    if os.path.exists(rel_p) and truth.get("lineage_plant"):
        rel = pd.read_parquet(rel_p)
        rinfo = json.load(open(os.path.join(out, "relations", "info.json"), encoding="utf-8"))
        lin, twin = set(truth["lineage_plant"]["genes"]), set(truth["broad_twin"]["genes"])

        def lineage():
            ll = rel[rel["symbol_a"].isin(lin) & rel["symbol_b"].isin(lin)]
            tw = rel[rel["symbol_a"].isin(twin) | rel["symbol_b"].isin(twin)]
            n_l = len(truth["lineage_plant"]["lines"])
            ok_l = (len(ll) > 0 and (ll["n_lines_a"] == n_l).all() and (ll["n_lines_b"] == n_l).all()
                    and (ll["lines_jaccard"] == 1.0).all() and ll["lineage_pair"].all()
                    and np.isfinite(ll["lineage_p"]).all()
                    and ll["alert"].str.contains("lineage: both genes are expressed in few lines", regex=False).all())
            ok_t = (len(tw) > 0 and (~tw["lineage_pair"]).all() and tw["lineage_p"].isna().all()
                    and (~tw["alert"].str.contains("lineage", regex=False)).all())
            ok_i = rinfo["lineage"]["rows"] == int(rel["lineage_pair"].sum())
            return ok_l and ok_t and ok_i, (
                f"lineage plant: {len(ll)} rows, lines {n_l} / {n_l}, J 1, lineage pair with a lineage_p "
                f"{sorted(set(ll['lineage_p'].round(4)))[:4]} and the alert: {ok_l}; its broad twin (every line): "
                f"{len(tw)} rows, no lineage pair: {ok_t}; info.json lineage rows {rinfo['lineage']['rows']} = "
                f"{int(rel['lineage_pair'].sum())}")
        check("relations", "lineage pairs: the planted lineage-restricted genes are marked, their broad twin is not",
              lineage)

        def units():
            keys = ["units", "rows_total", "pairs_total", "rows_both_halves", "pairs_both_halves",
                    "share_rows_both_halves", "rows_one_half", "pairs_one_half", "rows_not_reproduced",
                    "pairs_not_reproduced", "rows_fdr_le_0.05", "pairs_fdr_le_0.05", "rows_known", "pairs_known",
                    "rows_locus", "pairs_locus", "rows_readthrough_risk", "pairs_readthrough_risk", "rows_with_alert",
                    "pairs_with_alert", "rows_novel_candidate", "pairs_novel_candidate", "rows_lineage",
                    "pairs_lineage", "rows_read_sharing", "pairs_read_sharing", "novel_assessed", "novel_blocked_by"]
            miss = [k for k in keys if k not in rinfo]
            old = [k for k in ("pairs", "reproducible_pairs", "one_half_pairs", "known_pairs", "novel_candidate_pairs")
                   if k in rinfo]
            rs = (rel["read_sharing"] == "").all() and not rel["read_sharing_risk"].any() and \
                str(rinfo.get("read_sharing_source", "")).startswith("not assessed")
            return not miss and not old and rinfo["rows_total"] == len(rel) and rs, (
                f"missing keys {miss}; old keys {old}; rows_total {rinfo['rows_total']} = {len(rel):,} rows, "
                f"pairs_total {rinfo.get('pairs_total')}; read-sharing copies: "
                f"'{rinfo.get('read_sharing_source')}' (the offline fixture has no HGNC or Compara file), none "
                f"marked: {rs}; words: '{rinfo.get('evidence_both_halves', '')[:80]}'")
        check("relations", "counts in two units (rows and pairs); read-sharing copies not assessed without HGNC and "
                           "Compara", units)

    ed = os.path.join(out, "embed")
    if os.path.exists(os.path.join(ed, "drug_similarity.parquet")):
        def similarity():
            sim = pd.read_parquet(os.path.join(ed, "drug_similarity.parquet"))
            edd = pd.read_parquet(os.path.join(ed, "drugdoses.parquet"))
            per = sim.groupby("dd").size()
            mono = sim.groupby("dd")["cos_pooled"].apply(
                lambda v: bool((np.diff(np.nan_to_num(v.to_numpy(), nan=-9)) <= 1e-7).all()))
            fr = TB.dd_flags_of_record(out)
            edr = pd.read_parquet(os.path.join(ed, "drugs.parquet"))
            bc = pd.read_csv(os.path.join(ed, "broad_components.csv"), keep_default_na=False)
            # a resemblance note is expected only where the planted labels lie: a drug-dose whose wells are all on
            # the unreliable plate (its labels shuffled against the biology), and then it names the drug whose
            # biology the well carries (seed 0: Bestatin 5 µM carries Idarubicin's)
            up = (truth.get("method_v3") or {}).get("unreliable_plate") or {}
            only = {(str(x["drug"]), float(x["conc"])) for x in up.get("only_there", [])}
            bio = {(str(r["drug"]), float(r["conc"])): str(r.get("biology") or "") for r in truth.get("layout", [])
                   if r.get("plate") == up.get("plate") and r.get("biology")}
            notes = edd[edd["resembles_note"] != ""]
            bad_notes = [(str(d), str(x)) for d, x, rd in zip(notes["drug"], notes["dose"],
                                                               notes["resembles_drugdoses"])
                         if (str(d), float(x)) not in only or not bio.get((str(d), float(x)))
                         or bio[(str(d), float(x))] not in str(rd)]
            ok = ((per == 50).all() and mono.all() and per.index.tolist() == list(range(len(edd)))
                  and not bad_notes and list(edd["flags"]) == list(fr)
                  and "salt_form_alert" in edr
                  and {"top_pos_drugdoses", "top_neg_drugdoses"} <= set(bc.columns)
                  and (bc["top_pos_drugdoses"].str.count("; ") == 4).all())
            return ok, (f"{len(sim):,} rows: 50 per drug-dose for all {len(edd)}, cos_pooled non-increasing: "
                        f"{bool(mono.all())}; resembles notes {int((edd['resembles_note'] != '').sum())} "
                        f"{[(d, x) for d, x in zip(notes['drug'], notes['dose'])]} (expected only on the drug-doses "
                        f"of the unreliable plate's shuffled labels, naming the drug of the well's biology; not so: "
                        f"{bad_notes}); embed flags = the flags of record: "
                        f"{list(edd['flags']) == list(fr)}; "
                        f"salt-form alerts {int((edr['salt_form_alert'] != '').sum())}; broad components name 5 "
                        "drug-doses each way")
        check("embed", "drug-dose similarity (50 per drug-dose), flags of record, salt-form and resemblance notes, "
                       "broad components named", similarity)

    gr = os.path.join(out, "graph")
    if os.path.exists(os.path.join(gr, "modules.parquet")):
        def graph_new():
            from tahoemap import embed as EM, graph as GR, relations as RL   # the versions this code writes
            mods = pd.read_parquet(os.path.join(gr, "modules.parquet"))
            gi = json.load(open(os.path.join(gr, "info.json"), encoding="utf-8"))
            ei = json.load(open(os.path.join(ed, "info.json"), encoding="utf-8"))
            ri = json.load(open(os.path.join(out, "relations", "info.json"), encoding="utf-8"))
            covc = [f"cov_{k}_{t}" for k in ("umi_per_cell", "genes_per_cell", "cells", "composition", "S_phase",
                                             "G2M_phase") for t in ("r", "rho")]
            pp = gi.get("partner_preservation", {})
            ok = (all(c_ in mods for c_ in covc + ["covariate_kinds", "covariate_tag"])
                  and len(pp.get("layouts", {})) == 4 and all(0 <= v <= 1 for v in pp["layouts"].values())
                  and os.path.exists(os.path.join(gr, "modules.gmt"))
                  and (ei["version"], ri["version"], gi["version"]) == (EM.VERSION, RL.VERSION, GR.VERSION)
                  and (ei["version"], ri["version"], gi["version"]) >= (5, 5, 6))
            return ok, (f"modules covariate columns and tags ({int((mods['covariate_tag'] != '').sum())} tagged); "
                        f"partner preservation {pp.get('layouts')} (chance {pp.get('chance')}); modules.gmt "
                        f"{gi.get('gmt')}; versions embed {ei['version']}, relations {ri['version']}, graph "
                        f"{gi['version']}")
        check("graph", "module covariates, partner preservation of the four layouts, modules.gmt", graph_new)

    # ------------------------------------------------ validation (validate VERSION 7)
    vd = os.path.join(out, "validation")
    if os.path.exists(os.path.join(vd, "module_labels.csv")):
        _validation_checks(out, vd, truth, check)


def _validation_checks(out, vd, truth, check):
    """validate VERSION 7 on the planted modules: the label rule (gene sets, the drug class that drives a module,
    lineage), the report's sections, section 8's line controls, section 10's p53 counting, novel_edges.csv."""
    syn = _sets(truth)
    lab = pd.read_csv(os.path.join(vd, "module_labels.csv")).fillna("")
    nodes = pd.read_parquet(os.path.join(out, "graph", "nodes.parquet"))
    rep = open(os.path.join(vd, "report.md"), encoding="utf-8").read()
    met = json.load(open(os.path.join(vd, "metrics.json"), encoding="utf-8"))
    L = lab.set_index("module")
    s2m = dict(zip(nodes["symbol"], nodes["module"]))

    def module_of(setname, k):
        ms = pd.Series([s2m.get(x, -1) for x in syn.get(setname, [])]).value_counts()
        if not len(ms):
            return None
        m = int(ms.index[0])
        return m if ms.iloc[0] >= k and m > 0 and m in L.index else None

    def lab_hdac():
        m = module_of("HDAC_UP", 5)
        r = L.loc[m]
        ok = (r["label_source"] == "drug class" and "histone deacetylase inhibitor" in r["label"]
              and all(x in r["drivers_up_drugs"] for x in ("Belinostat", "Panobinostat", "Tucidinostat"))
              and "Carbamazepine" not in r["drivers_up_drugs"])
        return ok, f"module {m}: '{r['label']}' ({r['label_source']}); driven by {r['drivers_up_drugs']}"
    check("validate", "(a) the HDAC module is named by its driving class (HDAC inhibitors), not by Carbamazepine "
                      "(Tahoe calls it an HDAC inhibitor; ChEMBL does not)", lab_hdac)

    def lab_gluco():
        m = module_of("GLUCO", 5)
        r = L.loc[m]
        gcs = ["Dexamethasone", "Budesonide", "Triamcinolone", "Betamethasone dipropionate"]
        ok = (r["label"].startswith("raised by") and "glucocorticoid receptor agonist" in r["label"].lower()
              and sum(x in r["drivers_up_drugs"] for x in gcs) >= 3)
        return ok, f"module {m}: '{r['label']}'; {r['drivers_up_drugs']}"
    check("validate", "(b) the glucocorticoid module: 'raised by glucocorticoid receptor agonist' (>= 3 of the 4)",
          lab_gluco)

    def lab_ribi():
        m = module_of("RIBI", 5)
        r = L.loc[m]
        mt = ["Everolimus", "Temsirolimus", "Rapamycin", "Sapanisertib", "AZD-8055"]
        ok = (r["label"].startswith("lowered by") and "mtor" in (r["label"] + r["drivers_down_class"]).lower()
              and sum(x in r["drivers_down_drugs"] for x in mt) >= 3)
        if ok:
            return True, f"module {m}: '{r['label']}'; {r['drivers_down_drugs']}"
        z = np.load(os.path.join(out, "graph", "module_pooled_z.npy"))
        mods = pd.read_parquet(os.path.join(out, "graph", "modules.parquet"))
        row = int(np.flatnonzero(mods["module"].to_numpy() == m)[0]) if m in set(mods["module"]) else -1
        dd = pd.read_csv(os.path.join(out, "atlas", "effects", "drugdose.csv"), dtype={"dose": str})
        idx = [i for i, (dr_, ds) in enumerate(zip(dd["drug"].astype(str), dd["dose"])) if ds == "5"
               and any(dr_.startswith(x) for x in mt)]
        zz = sorted(round(float(z[row, i]), 2) for i in idx) if row >= 0 else []
        from tahoemap import validate as VA
        return "warn", (f"module {m}: '{r['label']}'; the mTOR inhibitors at 5 µM give module pooled z {zz}, below "
                        f"DRIVER_MIN_Z {VA.DRIVER_MIN_Z:g}: the planted fall (ln -0.5) is too small for the label "
                        "rule. A stronger fall does not help on this design: with a further ln -0.2 or -0.3 (tried) "
                        "the RIBI genes join the proteasome genes' module (the mTOR inhibitors lower both), and the "
                        "curated proteasome set then names that module, as the label rule intends")
    check("validate", "(c) the ribosome-biogenesis module: 'lowered by' an mTOR class (>= 3 of the 5)", lab_ribi)

    def lab_controls():
        m = module_of("NRF2_EXT", 5)
        ctl = lab[lab["label_source"] == "control"]["label"].tolist()
        ok = (L.loc[m, "label"] == "NRF2" and L.loc[m, "label_source"] == "control"
              and all(any(x in c_ for c_ in ctl) for x in ("DREAM", "E2F", "proteasome")))
        return ok, f"NRF2 module {m}: '{L.loc[m, 'label']}'; control labels {ctl}"
    check("validate", "(d) curated control sets keep their labels (NRF2, DREAM, E2F, proteasome)", lab_controls)

    def lab_cols():
        cols = {"label_weak", "label_drugs", "label_display", "label_alert"}
        bad = lab[(lab["label"].str.startswith("genes:")) & (lab["label_drugs"] != "")]
        src = lab["label_source"].value_counts().to_dict()
        return cols <= set(lab.columns) and not len(bad), (f"label sources {src}; 'genes:' labels with label_drugs: "
                                                           f"{bad['module'].tolist()}")
    check("validate", "(e) every label row has label_weak, label_drugs, label_display, label_alert", lab_cols)

    def lab_lineage():
        """The module of the planted lineage genes (expressed in 3 lines) is lineage-restricted: its median member is
        expressed in fewer than LINEAGE_MAX_SHARE of the lines. Its broad twin (the same drugs, every line) can join
        the module: on seed 0 the median is 3, on seed 1 (6 + 6 genes) 10.5 of 18, still under 0.6 x 18."""
        from tahoemap import validate as VA
        m = module_of("LINEAGE", 4)
        r = L.loc[m]
        others = [module_of(x, 5) for x in ("HDAC_UP", "GLUCO", "NRF2_EXT")]
        n_lines = len(truth.get("lines", [])) or 18
        cut = VA.LINEAGE_MAX_SHARE * n_lines
        ok = (float(r["median_lines_expressing"]) < cut and "lineage-restricted" in r["label_alert"]
              and "⚠ lineage-restricted" in r["label_display"]
              and not any("lineage-restricted" in L.loc[o, "label_alert"] for o in others if o is not None)
              and (lab["chrY_genes"] == "").all())
        return ok, (f"module {m} ({int(r['n_genes'])} genes): '{r['label_display']}', median lines expressing "
                    f"{r['median_lines_expressing']} (< {cut:g}: {VA.LINEAGE_MAX_SHARE:g} x {n_lines} lines); the "
                    "HDAC, glucocorticoid and NRF2 modules carry no lineage alert")
    check("validate", "(f) the lineage-restricted module carries its alert and tag; the others do not", lab_lineage)

    def report_order():
        heads = re.findall(r"^## (\d+)\. ", rep, flags=re.M)
        order = re.findall(r"^## (.+)$", rep, flags=re.M)
        s3 = rep.split("## 3. ")[1].split("## 4. ")[0] if "## 3. " in rep else ""
        ok3 = ("Tahoe / ChEMBL" in s3 and "| Tahoe class |" in s3 and "Annotation agreement" in s3
               and "| drug | Tahoe | ChEMBL | alert |" in s3 and "Carbamazepine" in s3)
        return heads == [str(i) for i in range(1, 11)] and order[-2:] == ["Caveats", "Files"] and ok3, (
            f"sections {heads}, ending {order[-2:]}; section 3 checks drugs by Tahoe's and ChEMBL's classes with the "
            f"annotation agreement table: {ok3}")
    check("validate", "report: sections 1-10 then Caveats and Files; section 3 by Tahoe and by ChEMBL classes",
          report_order)

    def line_controls():
        """The planted KRAS lines rank first by sel_z; the planted TP53-wild-type response ranks first by one of the
        two measures: response strength (NaN with fewer than 20 significant genes: Topotecan 5 µM on seed 0, both
        drugs on seed 1) or sel_z (the lines move 0-2 genes past the per-line cut: 0.52 / 0.71 on seed 0)."""
        lc = pd.read_csv(os.path.join(vd, "line_controls.csv"))
        tr = lc[lc["control"].str.contains("Trametinib")]
        tp = lc[lc["control"].str.contains("tp53_wt")]
        best = np.nanmax(np.r_[tp["auroc"].to_numpy(float), tp["auroc_response_strength"].to_numpy(float), -1.0])
        ok = (tr["auroc"] >= 0.9).any() and best >= 0.8
        return ok, (f"planted Trametinib rows (AUROC of sel_z) {tr[['dose', 'auroc']].values.tolist()}; TP53 rows: "
                    f"AUROC of response strength {tp[['drug', 'auroc_response_strength']].values.tolist()}, of sel_z "
                    f"{tp['auroc'].round(2).tolist()}: the best {best:.2f}")
    check("validate", "section 8: line-selective positive controls (KRAS plant by sel_z, TP53 by response strength "
                      "or sel_z)", line_controls)

    def p53_counting():
        s10 = rep.split("## 10. ")[1] if "## 10. " in rep else ""
        tg = (truth.get("direction") or {}).get("p53_fall_target", {}).get("gene", "TIGAR")
        ok = ("Not counted" in s10 and f"{tg} (rank" in s10 and "evidence from falls" in s10
              and "random-gene rate per test" in s10
              and f"p53_fall_target: {tg} in the p53 control: not counted" in s10)
        return ok, f"section 10 names the p53 targets not counted with why ({tg}: evidence from falls): {ok}"
    check("validate", "section 10: the p53 control counts rises only (the planted falling target is not counted); "
                      "the natural knockouts' random-gene rates", p53_counting)

    def novel_cols():
        ne = pd.read_csv(os.path.join(vd, "novel_edges.csv"))
        need = ["n_lines_a", "n_lines_b", "lines_shared", "lines_jaccard", "lineage_pair", "lineage_p",
                "read_sharing"]
        ok = all(c_ in ne.columns for c_ in need) and all(k in met.get("novel", {}) for k in (
            "edges_lineage", "edges_lineage_p_ge_0.01", "edges_read_sharing")) and "drug_class" in met["module_labels"]
        return ok, (f"novel_edges.csv columns {[c_ for c_ in need if c_ in ne.columns]}; metrics novel "
                    f"{ {k: met.get('novel', {}).get(k) for k in ('edges_lineage', 'edges_read_sharing')} }; module "
                    f"label sources {met['module_labels'].get('drug_class')} by drug class")
    check("validate", "novel_edges.csv has the lineage and read-sharing columns; metrics.json counts them",
          novel_cols)


def explorer_pipeline(out):
    """cli on a copy of OUT (the data volume hard-linked, the pages copied: the page files are rewritten in place):
    the plan with a changed explorer_app (a stand-in folder) is 'explorer' alone, for that reason; running it copies
    the page files only (app.js = the scripts joined in name order; data files keep their inode and bytes); the plan
    is then empty; status prints the explorer's lines."""
    import shutil
    import tempfile
    from tahoemap import cli
    from tahoemap import explorer as XP
    work = tempfile.mkdtemp(prefix="tahoe_explorer_assets_", dir=os.path.dirname(os.path.abspath(out)))
    try:
        xo = os.path.join(work, "out")

        def ign(d, names):
            return [n for n in names if os.path.abspath(d) == os.path.abspath(out) and n in ("explorer.tmp",
                                                                                               "explorer.old")]

        def cp(s_, d_):
            if f"{os.sep}explorer{os.sep}data{os.sep}" in s_ or f"{os.sep}tensor{os.sep}" in s_ \
                    or f"{os.sep}atlas{os.sep}" in s_:
                try:
                    return os.link(s_, d_)
                except OSError:
                    pass
            return shutil.copy2(s_, d_)
        shutil.copytree(out, xo, ignore=ign, copy_function=cp)
        app = os.path.join(work, "app")
        os.makedirs(os.path.join(app, "js"))
        for rel, text in (("index.html", "<!DOCTYPE html><title>stand-in page</title>\n"), ("app.css", "b{}\n"),
                          ("js/10_b.js", "var B = 2;\n"), ("js/00_a.js", "var A = 1;\n")):
            with open(os.path.join(app, *rel.split("/")), "w", encoding="utf-8", newline="\n") as fh:
                fh.write(text)
        orig_sha, orig_dir = XP.assets_sha, XP.APP_DIR
        XP.APP_DIR = app
        XP.assets_sha = lambda app_dir=app: orig_sha(app_dir)
        try:
            ap = cli.make_parser()
            a = ap.parse_args(["run", "--out", xo, "--offline"])
            a.defaults = {k: ap.get_default(k) for k in cli.REMEMBERED}
            a.data_in = a.data = xo
            cli.remember_options(a, set(), save=False)
            todo, why = cli.plan(a)
            data = os.path.join(xo, "explorer", "data")
            probe = sorted(os.listdir(os.path.join(data, "x", "00")))[:3]
            before = {f: os.stat(os.path.join(data, "x", "00", f)).st_ino for f in probe}
            cli._run_stage("explorer", a)
            after = {f: os.stat(os.path.join(data, "x", "00", f)).st_ino for f in probe}
            web = os.path.join(xo, "explorer", "web")
            appjs = open(os.path.join(web, "app.js"), encoding="utf-8").read()
            idx = open(os.path.join(web, "index.html"), encoding="utf-8").read()
            st = json.load(open(os.path.join(xo, "stages", "explorer.json"), encoding="utf-8"))
            todo2, _w = cli.plan(a)
            lines = cli.explorer_status(xo)
        finally:
            XP.assets_sha, XP.APP_DIR = orig_sha, orig_dir
        joined = appjs == "// ---- 00_a.js\nvar A = 1;\n// ---- 10_b.js\nvar B = 2;\n"
        ok = (todo == ["explorer"] and why == f"explorer: {cli.EXPLORER_ASSETS}" and before == after and joined
              and "stand-in page" in idx and st["info"]["assets_sha"] == orig_sha(app) and todo2 == []
              and len(lines) >= 5 and "rows:" in lines[1] and "every row" in lines[1])
        return ok, (f"plan {todo} ({why}); data files untouched {before == after}; app.js joined in name order "
                    f"{joined}; stamp assets_sha updated {st['info']['assets_sha'] == orig_sha(app)}; then plan "
                    f"{todo2}; status: {' | '.join(lines[:3])}")
    finally:
        shutil.rmtree(work, ignore_errors=True)


def redo_removes_plates():
    """cli._run_stage('build') on a folder with two finished plates (stand-in files; the build itself replaced by a
    recorder): without --redo the build finds them (that is how a stopped build resumes), with --redo it finds none."""
    import shutil
    import tempfile
    import types
    from tahoemap import cli, stream
    tmp = tempfile.mkdtemp(prefix="tahoe_redo_")
    seen = []
    orig = stream.build_local
    try:
        pb = os.path.join(tmp, "atlas", "pseudobulk")
        os.makedirs(pb)
        for g in ("group000", "group001"):
            for suf in (".npy", "_profiles.csv", "_barcodes.csv", "_samples.csv", "_files.txt"):
                with open(os.path.join(pb, g + suf), "w") as fh:
                    fh.write("x")
        stream.build_local = lambda args: seen.append(sorted(os.listdir(pb)))
        a = types.SimpleNamespace(out=tmp, redo=False, stream=False, data_in=tmp, reindex=False, limit_files=0,
                                  workers=0, batch_size=1, layout=None, unreliable_plates=None, min_cells=10,
                                  allow_partial=False, start=None)
        cli._run_stage("build", a)
        a.redo = True
        cli._run_stage("build", a)
    finally:
        stream.build_local = orig
        shutil.rmtree(tmp, ignore_errors=True)
    return (len(seen) == 2 and len(seen[0]) == 10 and seen[1] == [],
            f"files the build found: without --redo {len(seen[0]) if seen else '?'}, with --redo "
            f"{len(seen[1]) if len(seen) > 1 else '?'}")
