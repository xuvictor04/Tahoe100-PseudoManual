"""Per-stage checks of a finished synthetic run against the generator's planted truth (used by run_tests.py)."""

import json
import os
import re
import subprocess
import sys

import numpy as np
import pandas as pd

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OPPOSITE = [("HDAC_UP", "HDAC_DOWN"), ("COLOC_UP", "COLOC_DOWN"), ("COLOC2_UP", "COLOC2_DOWN")]


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
        json.load(open(os.path.join(fx, "complete.json")))["version"] == 3, "complete.json version 3"))
    check("effects", "plate13 unreliable, failed well removed", lambda: (
        "plate13" in json.load(open(os.path.join(fx, "info.json"))).get("unreliable_plates", []) and
        len(pd.read_csv(os.path.join(fx, "failed_wells.csv"))) >= 1,
        f"failed wells: {len(pd.read_csv(os.path.join(fx, 'failed_wells.csv')))}"))

    # ---------------------------------------------------------------- tensor
    def tensor_exact():
        info = json.load(open(os.path.join(out, "tensor", "info.json")))
        return (info["check_W1_max_diff"] <= 1e-5 and info["check_W2_max_diff"] <= 1e-5,
                f"reproduces the atlas: W1 {info['check_W1_max_diff']:.1e}, W2 {info['check_W2_max_diff']:.1e}")
    check("tensor", "per-line residuals reproduce the atlas exactly", tensor_exact)

    td = os.path.join(out, "tensor")
    DDL = np.load(os.path.join(td, "DDL_lfc.npy"), mmap_mode="r")
    DDZ = np.load(os.path.join(td, "DDL_z.npy"), mmap_mode="r")
    DD = np.load(os.path.join(fx, "DD_lfc.npy"))
    tinfo = json.load(open(os.path.join(td, "info.json")))
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
        check("tables", "CDKN1A best clean raiser is a DNA-damage drug",
              lambda: best("CDKN1A", ["Doxorubicin", "Topotecan", "5-Fluorouracil", "Fluorouracil"]))
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

        tinfo_t = json.load(open(os.path.join(tb, "info.json")))
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
            fl = [set(str(f).split("; ")) for f in dd["flags"].fillna("")]
            from tahoemap.atlas_core import ARTIFACT_FLAGS
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
                        f"included), {int(exp_cln[meas].sum())} clean")
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
        res = {k: round(mean_cos(v, v), 2) for k, v in sets.items() if len(v) >= 8 and k != "COMPOSITION"}
        weak = {k: v for k, v in res.items() if not v >= 0.35}
        return not weak, f"within-module mean cosine {res}"
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
        nrf2 = set(truth["gene_sets"].get("NRF2_CORE", [])) if isinstance(truth.get("gene_sets"), dict) else set()
        top = rel[(rel["symbol_a"] == "HMOX1") & (rel["cos"] > 0)].nsmallest(10, "rank")["symbol_b"].tolist()
        hit = [s for s in top if s in nrf2]
        return len(hit) >= 5, f"HMOX1's top 10 positive partners: {top}; NRF2 core among them: {len(hit)}"
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
        res, ok = {}, True
        sx = np.linalg.norm(nodes[["x", "y"]].std().to_numpy())
        ss = np.linalg.norm(nodes[["xs", "ys"]].std().to_numpy())
        for a, b in OPPOSITE:
            A, B = nodes[nodes["symbol"].isin(sets[a])], nodes[nodes["symbol"].isin(sets[b])]
            dn = np.linalg.norm(A[["x", "y"]].mean().to_numpy() - B[["x", "y"]].mean().to_numpy()) / sx
            ds = np.linalg.norm(A[["xs", "ys"]].mean().to_numpy() - B[["xs", "ys"]].mean().to_numpy()) / ss
            res[f"{a}/{b}"] = f"nodal {dn:.2f}, signed {ds:.2f}"
            ok &= dn < 0.3 and ds > 0.7
        return ok, f"centroid distance / map spread: {res}"
    check("graph", "opposite genes: together on the nodal map, apart on the signed map", maps_differ)

    # ---------------------------------------------------------------- validate
    vd = os.path.join(out, "validation")
    if os.path.exists(os.path.join(vd, "metrics.json")):
        check("validate", "report written", lambda: (
            os.path.getsize(os.path.join(vd, "report.md")) > 1000, f"{os.path.getsize(os.path.join(vd, 'report.md'))} bytes"))

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

    # ---------------------------------------------------------------- map
    html = os.path.join(out, "map", "gene_map.html")
    if os.path.exists(html):
        check("map", "self-contained HTML map", lambda: (
            os.path.getsize(html) > 10_000 and "http" not in re.sub(r"https?://[^\s\"']*(uniprot|ncbi|ensembl|"
                                                                       r"genenames)[^\s\"']*", "",
                                                                       open(html, encoding="utf-8").read()[:2000]),
            f"{os.path.getsize(html) / 1e6:.1f} MB"))

    # ---------------------------------------------------------------- look-ups
    def lookup_gene():
        r = subprocess.run([sys.executable, "-m", "tahoemap", "gene", "HMOX1", "--data", data, "--out", out],
                           cwd=REPO, capture_output=True, text=True)
        txt = r.stdout
        return (r.returncode == 0 and ("Dimethyl fumarate" in txt or "Auranofin" in txt) and "NQO1" in txt,
                f"exit {r.returncode}; {len(txt.splitlines())} lines")
    if os.path.exists(os.path.join(REPO, "tahoemap", "query.py")):
        check("query", "tahoe gene HMOX1 answers the question", lookup_gene)
