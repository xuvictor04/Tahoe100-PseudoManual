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

    DDL = np.load(os.path.join(out, "tensor", "DDL_lfc.npy"), mmap_mode="r")
    DDZ = np.load(os.path.join(out, "tensor", "DDL_z.npy"), mmap_mode="r")
    DD = np.load(os.path.join(fx, "DD_lfc.npy"))

    def median_matches():
        one = np.flatnonzero(dd["n_wells"].to_numpy() == 1)
        med = np.nanmedian(np.asarray(DDL[:, one, :], dtype=np.float32), axis=2).T
        ref = DD[one][:, :gK]
        ok = np.isfinite(med) & np.isfinite(ref)
        d = float(np.max(np.abs(med[ok] - ref[ok])))
        return d < 0.01, f"median over lines vs DD_lfc (single-well drug-doses): max |diff| {d:.4f} (float16)"
    check("tensor", "per-line fold changes collapse to the atlas's", median_matches)

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
            bad = [(os.path.basename(p), m) for p, m in links if m.strip().lower() not in names]
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
