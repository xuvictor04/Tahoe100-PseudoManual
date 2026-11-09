"""Per-stage checks of a finished synthetic run against the generator's planted truth (used by run_tests.py)."""

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
        json.load(open(os.path.join(fx, "complete.json"), encoding="utf-8"))["version"] == 3, "complete.json version 3"))
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
                spread = (np.sqrt(((P - P.mean(0)) ** 2).sum(1).mean()) + np.sqrt(((M - M.mean(0)) ** 2).sum(1).mean())) / 2
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

        def map_line_rows():
            """the side panel's cell-line rows: when a line's strongest drug-dose carries an alert, the row also names
            the line's strongest drug-dose without one (tables/line_effects best_* clean columns, the stronger of up
            and down), when that one reaches the per-line cut; no row names one otherwise"""
            _, D = map_data()
            W = int(D.get("lnw") or 9)
            if W < 12 or not D.get("ln_all"):
                return False, f"the page has no clean drug-dose per line row (lnw {W}, ln_all {D.get('ln_all')})"
            le = pd.read_parquet(os.path.join(out, "tables", "line_effects.parquet"),
                                 columns=["col", "line", "best_up_dd", "best_up_z", "best_down_dd", "best_down_z"])
            by = {(int(c), int(ln_)): r for c, ln_, r in zip(le["col"], le["line"], le.to_dict("records"))}
            fl, lz = D["fl"], float(D["line_z"])
            n_rows = n_flag = n_named = 0
            bad = []
            for e, a in enumerate(D["ln"]):
                for t in range(0, len(a) - W + 1, W):
                    n_rows += 1
                    r = by[(int(D["col"][e]), int(a[t]))]
                    alert = a[t + 5] >= 0 and a[t + 8] > 0 and fl[a[t + 8] - 1][1] == 1
                    u = r["best_up_z"] if np.isfinite(r["best_up_z"]) else -np.inf
                    d = r["best_down_z"] if np.isfinite(r["best_down_z"]) else np.inf
                    dd_, z_ = (r["best_up_dd"], u) if u >= -d else (r["best_down_dd"], d)
                    want = int(dd_) if alert and np.isfinite(z_) and abs(z_) >= lz and np.isfinite(dd_) else -1
                    n_flag += alert
                    n_named += a[t + 9] >= 0
                    if a[t + 9] != want or (want >= 0 and abs(a[t + 11] / 10 - z_) > 0.051):
                        bad.append((D["sym"][e], int(a[t]), a[t + 9], want))
            return (not bad and n_named > 0,
                    f"{n_rows:,} line rows, {n_flag:,} with a strongest drug-dose that carries an alert, "
                    f"{n_named:,} of these also name the strongest without one; mismatches: {bad[:3]}")
        check("map", "a line row whose strongest drug-dose is flagged also names the strongest without an alert",
              map_line_rows)

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

    # ---------------------------------------------------------------- look-ups
    def lookup_gene():
        r = subprocess.run([sys.executable, "-m", "tahoemap", "gene", "HMOX1", "--data", data, "--out", out],
                           cwd=REPO, capture_output=True, text=True)
        txt = r.stdout
        return (r.returncode == 0 and ("Dimethyl fumarate" in txt or "Auranofin" in txt) and "NQO1" in txt,
                f"exit {r.returncode}; {len(txt.splitlines())} lines")
    if os.path.exists(os.path.join(REPO, "tahoemap", "query.py")):
        check("query", "tahoe gene HMOX1 answers the question", lookup_gene)
