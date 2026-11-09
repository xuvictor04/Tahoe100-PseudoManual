"""Per-stage checks of a finished synthetic run against the generator's planted truth (used by run_tests.py).

run_all also calls the checks of the newer packages on the same output (design I5): tests/test_direction.py check(out)
(the reasons in tiers and the edge rules), tests/test_surfaces.py check(out, data) (links, map, vault and look-ups
that point into the explorer) and tests/test_explorer.py check(out, data) (the explorer stage: exact values, flags,
records, completeness, planted answers, determinism, sizes)."""

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
                        # spread
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
            ok = (not errs and sp[1] < 0.5 * sp[0] and sp[2] > 0 and tr[2] > 1e-3 and tr[3] > tr[1]
                  and ax[0] == "axes" and ax[1] < 1e-4 and dp[0] == 2 and dp[2] == 3 and dp[3] > dp[1]
                  and bool(res.get("panel")) and all(res["panel"][2:]))
            return ok, (f"spread: module mixing {sp[0]:.3f} -> {sp[1]:.3f}, mean move {sp[2]:.3f}; tour: {tr[0]}-D, "
                        f"{tr[1]} genes, frame change {tr[2]:.3f} in 0.5 s, {tr[3]} pixels drawn, {tr[4]} ms per "
                        f"frame; axis mode max |error| {ax[1]:.1e}; neighbourhood depth 2: {dp[1]} genes, depth 3: "
                        f"{dp[3]}; side panel {res.get('panel')}; script errors: {errs[:3]}")
        check("map", "spread slider, tour, axis mode, neighbourhood depth, alerts in the side panel", map_views)
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

    # ---------------------------------------------------------------- the newer packages' checks (design I5)
    package_checks(out, data, check)


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
            and "NR3C1 → " in sec and "this drug moves it that way too" in sec):
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
                ("response", "response"), ("baseline", "level"), ("sensitivity", "cells")))
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
    td = dv.downstream("TP53")
    td = td[td["target"] == "CDKN1A"]
    # since direction VERSION 3 'within organs' (when most lines are compared) is a note: edge_line prints it as
    # '- notes: within organs, ...' in ASCII, wrapped across lines
    if not (code == 0 and len(td) and f"TP53 -> CDKN1A  [{td['grade'].iloc[0]}]" in sec
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
        if not ((cells == (e["target_dd"] >= 0)) & (~cells | e["target"].str.startswith("cells under "))).all():
            bad.append("cells targets / target_dd")
        if not (cells == e["kind"].isin(["genotype_sensitivity", "null_sensitivity", "level_sensitivity"])).all():
            bad.append("cells targets are not the sensitivity kinds")
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
                and (up["target"] == "CDKN1A").all() and (ce["target_type"] == "cells").all()
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
        ok = ("## 8. Direction" in txt and "Positive controls" in txt and "expected false" in txt
              and d.get("edges") == len(e) and bool(d.get("positive")) and bool(d.get("synthetic")))
        return ok, (f"report section 8: {'## 8. Direction' in txt}; metrics.json direction: edges {d.get('edges')}, "
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
    if not (len(tr) and re.search(rf"^\| \[\[TP53\]\] \| {g0} \| TP53 activity strengthens CDKN1A's drug response \| "
                                  r"recorded loss-of-function mutation of TP53 in \d+ lines vs \d+ not recorded \|", up,
                                  re.M)
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
    if not (f"*{len(dn):,} arrows" in sec and len(rows) == len(keep) and (more in sec if more else True)
            and "| cells under [[" in sec and rows and rows[0].startswith(
                f"| [[CDKN1A]] | {dv.rows['grade'].to_numpy()[dn][keep[0]]} |")
            and f"direction_downstream: {len(dn)}" in t):
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
                for k in ("response", "baseline", "sensitivity")]
        ln = text(f"{nl['altered_lines'].iloc[0].split(', ')[0]} (line)")
        lines_ok = ("| [[TP53]] | TP53 loss of function (" in part(lt, "### Its recorded alterations", "\n### ")
                    and re.search(rf"^\| \[\[{null_src}\]\] \| \d+ vs \d+ \| {n_by[0]} / {n_by[1]} / {n_by[2]} \|",
                                  part(ln, "### Genes it does not express"), re.M) is not None)
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
