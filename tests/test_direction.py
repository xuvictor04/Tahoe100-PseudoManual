#!/usr/bin/env python3
"""test_direction.py - the direction stage (tahoemap/direction.py) against planted answers, and at full scale.

    python tests/test_direction.py [--src OUT --data DATA] [--work DIR] [--no-fixture] [--no-scale]
                                   [--scale-genes 4000,8000] [--keep]

1. Synthetic run. Copies a finished synthetic output (default: run_tests.py's, /tmp/tahoemap_test/out_seed0 and
   data_seed0; made with run_tests.py when missing), runs `python -m tahoemap.direction` on the copy in its own
   process and checks the answers make_synthetic_tahoe.py planted (ground_truth.json next to the data): TP53 -> most
   P53_ACTIVITY genes with the right sign and a grade; TP53 -> cells under the DNA-damaging drugs; PSMD10's level ->
   Ixazomib and ACSL4's -> Artesunate; MTAP-null -> Pemetrexed; the drug-target classes (glucocorticoids, MTOR,
   statins); that random pseudo-groups give ~no edges; that no edge lacks p / q / grade, that the written-edge and
   grade rules hold and every alert starts with the warning sign; that the TP53-deleted lines are seen as not
   expressing TP53; that a small gene chunk gives identical edges.
2. Variants of the synthetic output: without metadata, relations, drug targets and cell numbers (the empty edges
   table keeps its column types), and with lines.csv lacking its Organ column (organs come from the metadata).
3. A 50-line fixture (3,000 genes x 300 drug-doses): (a) a genotype-dependent programme P that dominates the
   other responsive genes of its drug-doses, next to genes Q that respond the same in every line - P is found at
   grade A, Q never gets grade A and its edges say they rest on the global-sensitivity correction; (b) a
   line-wide damping (DAMP lines show 0.3x of every planted response, at narrow, near-threshold and broad
   drug-doses alike) - no gene-specific edges; (c) a random group - ~no edges.
4. Scale: generated outputs with the real numbers of drug-doses (1,132) and lines (50, 16 organs in realistic
   proportions), 4,000 / 8,000 genes (any list with --scale-genes, e.g. 16643), many drug-doses with line-to-line
   differences in cell numbers, tissue-specific absent genes, random small driver groups and hypermutated lines,
   40 compounds that move some genes in every line (as most drugs do), and planted answers: a genotype-dependent
   programme (found), a line-wide global resistance at broad drug-doses (not called gene-specific), TP53 / KEAP1
   effects, a natural knockout with partner effects (response and baseline), a lone natural-knockout effect on cell
   numbers (MTAP-null), a gene whose level modulates its partners' responses (level edges, direction clear) and one
   whose level sets a drug's effect (permuted levels give no more edges than the FDR allows); the pseudo-groups and the
   random driver groups give ~no edges and are rarely tissue-confounded; peak memory and minutes are measured and
   extrapolated to the real 16,643 genes (within ~3 GB and a few minutes). Each fixture's tensor is deleted after
   its run (DDL_lfc is a hard link of DDL_z where the file system allows: only the folds shown in readings use it).
Prints PASS / FAIL per check with its numbers; exit code 1 if anything fails.
"""

import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile
import time

import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
sys.path.insert(0, REPO)
DEFAULT_WORKDIR = "/tmp/tahoemap_test" if os.name != "nt" else os.path.join(tempfile.gettempdir(), "tahoemap_test")
RESULTS = []
FULL_GENES = 16643
MEM_LIMIT_GB = 3.0
MINUTES_LIMIT = 10.0
WARN = "⚠"


def check(name, fn):
    try:
        ok, detail = fn()
        status = "PASS" if ok else "FAIL"
    except Exception as e:  # noqa: BLE001
        import traceback
        status, detail = "FAIL", f"{type(e).__name__}: {e}\n{traceback.format_exc(limit=4)}"
    RESULTS.append((status, name, str(detail)))
    print(f"  [{status}] {name} -- {detail}", flush=True)


def run_stage(out, data, extra=()):
    cmd = [sys.executable, "-m", "tahoemap.direction", "--out", out, *(["--data", data] if data else []), *extra]
    t0 = time.time()
    r = subprocess.run(cmd, cwd=REPO, capture_output=True, text=True, encoding="utf-8", errors="replace")
    dt = time.time() - t0
    with open(os.path.join(out, "direction_console.log"), "w", encoding="utf-8") as fh:
        fh.write(r.stdout + "\n" + r.stderr)
    if r.returncode != 0:
        print(r.stdout[-3000:], r.stderr[-3000:])
    info = {}
    p = os.path.join(out, "direction", "info.json")
    if r.returncode == 0 and os.path.exists(p):
        with open(p, encoding="utf-8") as fh:
            info = json.load(fh)
    return r.returncode, dt, info, r.stdout


def copy_output(src, dst):
    if os.path.exists(dst):
        shutil.rmtree(dst)
    shutil.copytree(src, dst, symlinks=True, ignore=shutil.ignore_patterns("vault", "map", "review"))
    shutil.rmtree(os.path.join(dst, "direction"), ignore_errors=True)


def load(out):
    d = os.path.join(out, "direction")
    e = pd.read_parquet(os.path.join(d, "edges.parquet"))
    g = pd.read_parquet(os.path.join(d, "groups.parquet"))
    with open(os.path.join(d, "controls.json"), encoding="utf-8") as fh:
        ctl = json.load(fh)
    return e, g, ctl


def table_wide(e):
    """Edges significant over the whole table (grades A / B possible): q < 0.10 and, where present, q_group."""
    return (e["q"] < 0.10) & (e["q_group"].isna() | (e["q_group"] < 0.10))


def integrity(e):
    """Every edge has p, q and a grade; the written-edge rule, the grade rules and the alert format hold."""
    from tahoemap import direction as Dm
    bad = []
    if not e["p"].notna().all() or not np.isfinite(e["p"]).all():
        bad.append("p missing")
    grouped = e["kind"].str.startswith("genotype") | (e["kind"] == "level_sensitivity")
    written = np.where(grouped, e["q_group"] < 0.10, e["q"] < 0.10)
    if not written.all():
        bad.append(f"{int((~written).sum())} edges without q (q_group for grouped kinds) < 0.10")
    if not e["q"].notna().all():
        bad.append("q missing")
    if not e["grade"].isin(["A", "B", "C"]).all():
        bad.append("grade")
    if not e["kind"].isin(Dm.KINDS).all():
        bad.append("kind")
    if not e["sign"].isin([-1, 0, 1]).all():
        bad.append("sign")
    if ((e["source"] == "") | (e["target"] == "")).any():
        bad.append("empty source / target")
    if ((e["target_type"] == "gene") & (e["source_col"] == e["target_col"]) & (e["source_col"] >= 0)).any():
        bad.append("self edge")
    a = e[e["grade"] == "A"]
    rule = a["kind"].str.startswith("genotype") & (a["q"] < 0.05) & (a["q_group"] < 0.10) & \
        (a["n_altered"] >= 5) & (a["n_intact"] >= 5) & ~a["alerts"].str.contains(
            "tissue-confounded|co-occurs with|compared across organs|exists only relative|significant within this")
    if not rule.all():
        bad.append(f"{int((~rule).sum())} grade-A edges break the A rule")
    only_group = e["kind"].str.startswith("genotype") & ~table_wide(e)
    if not (e.loc[only_group, "grade"] == "C").all():
        bad.append("an edge significant only within its group is not grade C")
    al = e["alerts"].fillna("")
    if not ((al == "") | al.str.startswith(WARN + " ")).all():
        bad.append("an alert without the warning sign")
    n = al.map(lambda s: s.count("; ") + 1 if s else 0)
    if not (n == e["n_alerts"]).all():
        bad.append("n_alerts")
    return bad, len(a)


# ----------------------------------------------------------------------------- 1. the synthetic run
def synthetic_checks(out, data, info, console):
    dd_ = os.path.join(out, "direction")
    e, g, ctl = load(out)
    with open(os.path.join(data, "ground_truth.json"), encoding="utf-8") as fh:
        truth = json.load(fh)
    sys.path.insert(0, HERE)
    import make_synthetic_tahoe as MS
    genes = set(pd.read_csv(os.path.join(out, "atlas", "effects", "genes.csv"))["symbol"].astype(str))
    p53 = [x for x in MS.P53_ACTIVITY if x in genes]

    check("outputs written (edges, groups, controls, info, README)", lambda: (
        all(os.path.exists(os.path.join(dd_, f)) for f in ("edges.parquet", "groups.parquet", "controls.json",
                                                            "info.json", "README.md"))
        and os.path.exists(os.path.join(out, "stages", "direction.json")),
        f"{len(e)} edges, {len(g)} groups; by kind {info.get('edges_by_kind')}"))

    def integ():
        bad, na = integrity(e)
        return not bad, ("ok: every edge has p and q, passes its family's BH (q, or q_group for genotype and "
                         f"level_sensitivity), a grade, kind and sign; {na} grade-A edges, all within the rule; "
                         "group-only edges are grade C; alerts start with the warning sign" if not bad
                         else "; ".join(bad))
    check("no edge lacks p / q / grade; written-edge, grade and alert rules hold", integ)

    def tp53():
        r = e[(e["kind"] == "genotype_response") & (e["source"] == "TP53")]
        hit = r[r["target"].isin(p53)]
        right = hit[hit["sign"] == 1]
        prec = len(hit) / max(1, len(r))
        ctl_k = [v for k, v in ctl["positive"].items() if k.startswith("TP53") and "p53 targets" in k]
        ranks = sorted(x["rank"] for x in (ctl_k[0]["per_gene"] if ctl_k else []) if x["gene"] in p53)
        top = sum(x <= 0.05 * 1198 for x in ranks)
        tw = right[table_wide(right)]
        ok = len(right) >= 0.4 * len(p53) and prec >= 0.8 and (hit["sign"] == -1).sum() == 0 and \
            (tw["grade"] == "A").any() and top >= 0.5 * len(p53)
        return ok, (f"{len(right)} of {len(p53)} P53_ACTIVITY genes with an edge, sign +1 ({(hit['sign'] == -1).sum()}"
                    f" wrong sign); grades {right['grade'].value_counts().to_dict()} ({len(tw)} significant over the "
                    f"whole table, the rest within the TP53 group only: grade C); {len(hit)} of the {len(r)} TP53 "
                    f"response edges are P53_ACTIVITY genes ({prec:.0%}); {top} of {len(p53)} ranked in the top 5% of "
                    f"all genes (ranks {ranks[:12]}...)")
    check("TP53 -> most P53_ACTIVITY genes (sign +1, graded)", tp53)

    def tp53_sens():
        s = e[(e["kind"] == "genotype_sensitivity") & (e["source"] == "TP53")]
        st = s[table_wide(s)]
        want = ["Doxorubicin (hydrochloride) 5", "Topotecan (hydrochloride) 5", "5-Fluorouracil 5"]
        got = [w for w in want if ((st["target"] == f"cells under {w} µM") & (st["sign"] == -1)).any()]
        return len(got) >= 2 and (st["sign"] == 1).sum() == 0, (
            f"{len(got)} of 3 DNA-damaging drugs at 5 µM over the whole table ({', '.join(got)}), sign -1 (TP53 "
            f"activity sensitises), none of the table-wide ones with sign +1; all TP53 sensitivity edges: "
            f"{s[['target', 'grade', 'sign', 'q', 'q_group']].round(4).to_dict('records')}")
    check("TP53 -> cells under the DNA-damaging drugs (sign -1)", tp53_sens)

    def level(gene, drug):
        s = e[(e["kind"] == "level_sensitivity") & (e["source"] == gene) & e["target"].str.contains(drug, regex=False)]
        ok = len(s) >= 1 and (s["sign"] == -1).all() and (s["grade"] == "C").all()
        return ok, (f"{gene} -> {s['target'].tolist()} r {s['r'].round(2).tolist()} q {s['q'].round(4).tolist()} "
                    f"q within the drug-dose {s['q_group'].round(4).tolist()} grade {s['grade'].tolist()}")
    check("PSMD10 level -> cells under Ixazomib (sign -1)", lambda: level("PSMD10", "Ixazomib"))
    check("ACSL4 level -> cells under Artesunate (sign -1)", lambda: level("ACSL4", "Artesunate"))

    def mtap():
        s = e[(e["kind"] == "null_sensitivity") & (e["source"] == "MTAP") & e["target"].str.contains("Pemetrexed")]
        ok = len(s) >= 1 and (s["sign"] == 1).all()
        al = s["alerts"].iloc[0] if len(s) else ""
        return ok, (f"MTAP-null -> {s['target'].tolist()} (sign +1: MTAP protects), grade {s['grade'].tolist()}, "
                    f"q {s['q'].round(4).tolist()}; alerts: {al[:160]}")
    check("MTAP-null lines -> depleted by Pemetrexed (null_sensitivity)", mtap)

    def drug_targets():
        sets = truth["extra_not_in_panel_spec"]["synthetic gene sets"]
        d = e[e["kind"] == "drug_target"]
        out, ok = [], True
        for src, name, sign in (("NR3C1", "GLUCO", 1), ("MTOR", "RIBI", 1), ("HMGCR", "CHOL", -1)):
            members = set(sets[name])
            x = d[(d["source"] == src) & d["target"].isin(members)]
            wrong = int((x["sign"] != sign).sum())
            ok &= len(x) >= 0.4 * len(members) and wrong == 0
            out.append(f"{src} -> {name}: {len(x)} of {len(members)} (wrong sign {wrong})")
        return ok, "; ".join(out)
    check("drug_target: glucocorticoid / MTOR / statin classes, sign relative to the target's activity", drug_targets)

    def negatives():
        s = ctl["negative"]["summary"]
        pse = ctl["negative"]["pseudo"]
        ok = all(pse[k]["edges_mean_per_group"] <= 0.1 and (pse[k]["edges_per_tested"] or 0) <= 1e-4
                 for k in pse) and pse["response"]["groups"] >= 50
        return ok, "; ".join(f"{k}: pseudo {v['pseudo_edges_mean_per_group']} table-wide edges/group vs real "
                             f"{v['real_edges_mean_per_group']} (within the group only: pseudo "
                             f"{v['pseudo_within_group_edges_mean_per_group']} vs real "
                             f"{v['real_within_group_edges_mean_per_group']}; expected false edges "
                             f"{v['expected_false_edges']} table-wide, {v['expected_false_edges_within_group']} "
                             f"within groups)" for k, v in s.items()) + f"; {pse['response']['groups']} pseudo-groups"
    check("random pseudo-groups give ~no edges (empirical false-positive rate)", negatives)

    def deleted():
        r = g[(g["gene"] == "TP53") & (g["kind"] == "genotype")]
        n = int(r["x_not_expressed_in_altered"].max()) if len(r) else -1
        ok = n == len(truth["groups"]["tp53_deleted"])
        a = r["alerts"].iloc[0] if len(r) else ""
        return ok, f"TP53 not expressed in {n} of its altered lines (planted deletions: " \
                   f"{truth['groups']['tp53_deleted']}); alert: {'itself is not expressed' in a}"
    check("TP53-deleted lines seen as not expressing TP53", deleted)

    def readme():
        txt = open(os.path.join(dd_, "README.md"), encoding="utf-8").read()
        miss = [c for c in list(e.columns) + list(g.columns) if f"`{c}`" not in txt]
        return not miss and "columns without a description" not in console, f"undocumented: {miss}"
    check("README.md documents every column", readme)
    return e


def chunk_check(src_out, data, work, e_ref):
    out2 = os.path.join(work, "out_chunk")
    copy_output(src_out, out2)
    rc, dt, info, _ = run_stage(out2, data, ("--chunk", "97"))
    e2 = pd.read_parquet(os.path.join(out2, "direction", "edges.parquet")) if rc == 0 else None

    def same():
        if e2 is None:
            return False, f"exit code {rc}"
        cols = ["kind", "source", "target", "grade", "sign"]
        a = e_ref[cols].sort_values(cols).reset_index(drop=True)
        b = e2[cols].sort_values(cols).reset_index(drop=True)
        qd = float(np.max(np.abs(np.sort(e_ref["q"].to_numpy()) - np.sort(e2["q"].to_numpy())))) if len(a) == len(
            b) else np.inf
        return a.equals(b) and qd < 1e-9, f"{len(a)} vs {len(b)} edges, chunk {info.get('chunk')} genes, " \
                                          f"max q difference {qd:.1e}"
    check("identical edges with a small gene chunk (97 genes)", same)
    shutil.rmtree(out2, ignore_errors=True)


# ----------------------------------------------------------------------------- 2. variants
def variant_checks(src_out, data, work):
    import pyarrow.parquet as pq
    # (a) nothing optional: no metadata, no relations, no drug targets, no cell numbers
    out = os.path.join(work, "out_bare")
    copy_output(src_out, out)
    shutil.rmtree(os.path.join(out, "relations"), ignore_errors=True)
    fx = os.path.join(out, "atlas", "effects")
    for f in ("DD_A.npy", "DD_Az.npy", "file_index.json"):
        for p in (os.path.join(fx, f), os.path.join(out, "atlas", f)):
            if os.path.exists(p):
                os.remove(p)
    dd = pd.read_csv(os.path.join(fx, "drugdose.csv"))
    dd = dd.drop(columns=[c for c in ("targets", "moa-broad", "moa_broad") if c in dd])
    dd.to_csv(os.path.join(fx, "drugdose.csv"), index=False)
    lines = pd.read_csv(os.path.join(fx, "lines.csv"))
    lines.drop(columns=[c for c in ("drivers", "driver_changes") if c in lines]).to_csv(
        os.path.join(fx, "lines.csv"), index=False)
    shutil.rmtree(os.path.join(out, "tables"), ignore_errors=True)
    rc, _, info, _ = run_stage(out, None, ("--pseudo", "5"))

    def bare():
        if rc != 0:
            return False, f"exit code {rc}"
        sch = pq.read_schema(os.path.join(out, "direction", "edges.parquet"))
        nulls = [f.name for f in sch if str(f.type) == "null"]
        n = pq.read_metadata(os.path.join(out, "direction", "edges.parquet")).num_rows
        return not nulls, f"{n} edges; columns of Arrow type null: {nulls or 'none'} ({len(sch)} columns)"
    check("variant without metadata / relations / targets / cell numbers: runs, typed columns", bare)
    shutil.rmtree(out, ignore_errors=True)
    # (b) lines.csv without Organ: the metadata's Organ is used
    out = os.path.join(work, "out_noorgan")
    copy_output(src_out, out)
    fx = os.path.join(out, "atlas", "effects")
    lines = pd.read_csv(os.path.join(fx, "lines.csv"))
    lines.drop(columns=["Organ"]).to_csv(os.path.join(fx, "lines.csv"), index=False)
    rc, _, info, _ = run_stage(out, data, ("--pseudo", "5"))

    def noorgan():
        if rc != 0:
            return False, f"exit code {rc}"
        g = pd.read_parquet(os.path.join(out, "direction", "groups.parquet"))
        unk = g["organs_altered"].str.contains("unknown:").sum() + g["alerts"].str.contains("unknown:").sum()
        return unk == 0 and info.get("lines_with_organ") == len(lines), (
            f"organs from {info.get('organs_from')!r}, {info.get('lines_with_organ')} of {len(lines)} lines with an "
            f"organ; groups mentioning 'unknown:' organs {int(unk)}")
    check("variant with lines.csv lacking Organ: organs come from the metadata", noorgan)
    shutil.rmtree(out, ignore_errors=True)


# ----------------------------------------------------------------------------- 3. the 50-line fixture
def _write_common(out, data, gK, Dn, L, organ, rng, drugrows=None):
    fx = os.path.join(out, "atlas", "effects")
    for d in (fx, os.path.join(out, "tensor"), os.path.join(out, "relations"), os.path.join(data, "metadata")):
        os.makedirs(d, exist_ok=True)
    G = gK + 3
    sym = [f"FG{i:05d}" for i in range(gK)] + ["S_PHASE", "G2M_PHASE", "PROTEASOME"]
    pc = np.exp(rng.normal(5.0, 1.0, G))
    return fx, G, sym, pc


def _link_or_copy_lfc(tdir, fac):
    """DDL_lfc as a hard link of DDL_z (no extra disk; only the folds shown in readings read it), else a copy x fac."""
    z, lf = os.path.join(tdir, "DDL_z.npy"), os.path.join(tdir, "DDL_lfc.npy")
    if os.path.exists(lf):
        os.remove(lf)
    try:
        os.link(z, lf)
        return
    except OSError:
        pass
    from tahoemap.common import open_memmap
    a = np.load(z, mmap_mode="r")
    b = open_memmap(lf, a.shape, np.float32)
    for g0 in range(0, a.shape[0], 500):
        b[g0:g0 + 500] = a[g0:g0 + 500] * fac
    del a, b


def make_small_fixture(root, seed=7):
    """3,000 genes x 300 drug-doses x 50 lines (10 organs x 5). Planted (z units, per line): 16 narrow programmes
    (20 genes x 3 drug-doses, every line); broad genes B (400 x 4 drug-doses, every line; pooled z just below
    significance at 2 of the 4); programme P (300 genes) at 4 other drug-doses only where DOMG is intact (0.4x in the
    DOMG lines) and genes Q (100) responding there identically in every line; DAMP lines show 0.3x of every planted
    response. NULLG: 20 random lines (a control)."""
    from tahoemap.common import open_memmap
    gK, Dn, L = 3000, 300, 50
    rng = np.random.default_rng(seed)
    shutil.rmtree(root, ignore_errors=True)
    out, data = os.path.join(root, "out"), os.path.join(root, "data")
    organs = np.array([f"Organ{k}" for k in range(10)], dtype=object)[np.arange(L) % 10]
    fx, G, sym, pc = _write_common(out, data, gK, Dn, L, organs, rng)
    pd.DataFrame({"col": np.arange(G), "kind": ["gene"] * gK + ["module"] * 3, "token": np.arange(3, 3 + G),
                  "symbol": sym, "label": sym, "pooled_cpm": pc, "median_line_cpm": pc,
                  "n_lines_expressing": L}).to_csv(os.path.join(fx, "genes.csv"), index=False)
    pd.DataFrame([{"drug": f"Drug{i // 3:03d}", "dose": ["0.05", "0.5", "5"][i % 3], "conc": [0.05, 0.5, 5.0][i % 3],
                   "flags": "", "targets": "", "moa_broad": "inhibitor/antagonist", "plates": "p1", "wells": "A1"}
                  for i in range(Dn)]).to_csv(os.path.join(fx, "drugdose.csv"), index=False)
    pd.DataFrame({"cell_line_id": [f"CVCL_F{i:03d}" for i in range(L)], "cell_name": [f"Line{i:02d}" for i in range(L)],
                  "Organ": organs, "in_growth_analysis": True}).to_csv(os.path.join(fx, "lines.csv"), index=False)
    domg = np.zeros(L, bool)
    domg[[i for i in range(L) if (i // 10) % 2 == 0]] = True                # 25 lines, 2-3 per organ
    damp = np.zeros(L, bool)
    damp[[i for i in range(L) if i % 4 in (1, 2)]] = True                   # 25 lines, another pattern
    nullg = np.zeros(L, bool)
    nullg[rng.choice(L, 20, replace=False)] = True
    meta = []
    for i in range(L):
        for gene, on in (("DOMG", domg[i]), ("DAMP", damp[i]), ("NULLG", nullg[i]), ("ANCHOR", True)):
            if on:
                meta.append({"cell_name": f"Line{i:02d}", "Cell_ID_DepMap": f"ACH-{i:06d}",
                             "Cell_ID_Cellosaur": f"CVCL_F{i:03d}", "Organ": organs[i], "Driver_Gene_Symbol": gene,
                             "Driver_VarZyg": "Hom", "Driver_VarType": "Missense",
                             "Driver_ProtEffect_or_CdnaEffect": "p.X1Y",
                             "Driver_Mech_InferDM": None if gene == "ANCHOR" else "LoF",
                             "Driver_GeneType_DM": "Suppressor"})
    pd.DataFrame(meta).to_parquet(os.path.join(data, "metadata", "cell_line_metadata.parquet"), index=False)
    lc = pc[None, :] * np.exp(rng.normal(0, 0.4, (L, G)))
    np.save(os.path.join(fx, "line_cpm.npy"), lc.astype(np.float32))
    np.save(os.path.join(fx, "expr_mask.npy"), np.ones((L, G), bool))
    np.save(os.path.join(out, "tensor", "line_measured.npy"), np.ones((L, gK), bool))
    sig = np.zeros((Dn, gK), np.float32)                                     # in every line
    progs = []
    for p in range(16):
        gg, dd = np.arange(1000 + 20 * p, 1020 + 20 * p), np.arange(3 * p, 3 * p + 3)
        sig[np.ix_(dd, gg)] = 5.0
        progs.append(gg)
    B, dB = np.arange(100, 500), np.arange(200, 212, 3)
    sig[np.ix_(dB, B)] = 5.0
    P, Q, dP = np.arange(600, 900), np.arange(900, 1000), np.arange(250, 262, 3)
    sig[np.ix_(dP, Q)] = 5.0
    sigP = np.zeros((Dn, gK), np.float32)
    sigP[np.ix_(dP, P)] = 5.0                                                # only where DOMG is intact
    lf_damp = np.where(damp, 0.3, 1.0).astype(np.float32)
    lf_dom = np.where(domg, 0.4, 1.0).astype(np.float32)
    Zp = rng.standard_normal((Dn, G)).astype(np.float32) * 0.3
    Zp[:, :gK] += sig * float(lf_damp.mean())
    Zp[np.ix_(dP, P)] = 4.0                                                  # P: significant pooled (the median line)
    Zp[np.ix_(dB[[1, 3]], B)] = 2.5                                          # near the threshold: not significant
    q = np.where(np.abs(Zp) >= 3, 1e-5, 1.0).astype(np.float32)
    np.save(os.path.join(fx, "DD_z.npy"), Zp)
    np.save(os.path.join(fx, "DD_lfc.npy"), (Zp * 0.15).astype(np.float32))
    np.save(os.path.join(fx, "DD_qup.npy"), q)
    np.save(os.path.join(fx, "DD_qdn.npy"), np.ones((Dn, G), np.float32))
    A = rng.normal(0, 0.3, (Dn, L))
    np.save(os.path.join(fx, "DD_A.npy"), A.astype(np.float32))
    np.save(os.path.join(fx, "DD_Az.npy"), (A / 0.3).astype(np.float32))
    Zt = open_memmap(os.path.join(out, "tensor", "DDL_z.npy"), (gK, Dn, L), np.float32)
    for g0 in range(0, gK, 500):
        g1 = min(gK, g0 + 500)
        z = rng.standard_normal((g1 - g0, Dn, L), dtype=np.float32)
        z += sig[:, g0:g1].T[:, :, None] * lf_damp[None, None, :]
        z += sigP[:, g0:g1].T[:, :, None] * (lf_damp * lf_dom)[None, None, :]
        Zt[g0:g1] = z
    del Zt
    _link_or_copy_lfc(os.path.join(out, "tensor"), 0.15)
    a = np.repeat(np.arange(gK), 30)
    b = rng.integers(0, gK, a.size)
    ex = []
    for gg in progs + [P, Q]:
        pa, pb = np.meshgrid(gg, gg)
        k = pa.ravel() != pb.ravel()
        ex.append((pa.ravel()[k], pb.ravel()[k]))
    a = np.r_[a, np.concatenate([x[0] for x in ex])]
    b = np.r_[b, np.concatenate([x[1] for x in ex])]
    m = a != b
    pd.DataFrame({"col_a": a[m], "col_b": b[m], "cos": rng.uniform(0.3, 0.9, int(m.sum())).astype(np.float32)}) \
        .to_parquet(os.path.join(out, "relations", "gene_relations.parquet"), index=False)
    return out, data, {"P": P, "Q": Q, "B": B, "progs": np.concatenate(progs)}


def small_fixture_checks(work):
    root = os.path.join(work, "fixture50")
    out, data, plant = make_small_fixture(root)
    rc, dt, info, _ = run_stage(out, data, ("--pseudo", "20"))
    check("50-line fixture: stage finishes", lambda: (rc == 0, f"exit code {rc} in {dt:.0f} s; correction "
                                                              f"{info.get('global_sensitivity_correction')}"))
    if rc != 0:
        return
    e, _, _ = load(out)
    r = e[e["kind"] == "genotype_response"]

    def names(ix):
        return {f"FG{i:05d}" for i in ix}

    def dom():
        d = r[r["source"] == "DOMG"]
        p = d[d["target"].isin(names(plant["P"]))]
        q = d[d["target"].isin(names(plant["Q"]))]
        pa = int(((p["sign"] == 1) & (p["grade"] == "A")).sum())
        q_al = int(q["alerts"].str.contains("exists only relative").sum())
        q_c = int((~q["alerts"].str.contains("exists only relative") & (q["grade"] == "C")).sum())
        ok = pa >= 0.9 * len(plant["P"]) and (q["grade"] == "A").sum() == 0 and q_al + q_c == len(q) and \
            q_al >= 0.5 * len(plant["Q"])
        return ok, (f"DOMG -> P: {len(p)} of {len(plant['P'])} edges, {pa} grade A with sign +1; DOMG -> Q (same "
                    f"response in every line): {len(q)} edges, grades {q['grade'].value_counts().to_dict()}, "
                    f"{q_al} of them alerted as resting on the correction (raw_share median "
                    f"{q['raw_share'].median() if len(q) else float('nan'):.2f}), {q_c} other (grade C leads)")
    check("50-line fixture: a dominant genotype-dependent programme does not create grade-A edges elsewhere", dom)

    def damp():
        d = e[e["source"] == "DAMP"]
        planted = names(np.r_[plant["P"], plant["Q"], plant["B"], plant["progs"]])
        n = int(d["target"].isin(planted).sum())
        return n <= 0.02 * len(planted), (
            f"DAMP (0.3x of every planted response in its 25 lines, narrow, near-threshold and broad drug-doses) "
            f"-> {n} of the {len(planted)} planted responsive genes ({len(d)} DAMP edges in all, grades "
            f"{d['grade'].value_counts().to_dict()}); the line-wide responsiveness absorbs it")
    check("50-line fixture: a line-wide damping is not called gene-specific", damp)

    def nullg():
        d = e[e["source"] == "NULLG"]
        return len(d) <= 3, f"random group NULLG (20 lines): {len(d)} edges {d[['kind', 'grade']].values.tolist()}"
    check("50-line fixture: a random group gives ~no edges", nullg)
    shutil.rmtree(os.path.join(out, "tensor"), ignore_errors=True)


# ----------------------------------------------------------------------------- 4. scale fixture
ORGANS = [("Lung", 14), ("Pancreas", 6), ("Bowel", 6), ("Breast", 4), ("Skin", 3), ("Ovary", 3), ("Kidney", 2),
          ("Liver", 2), ("Stomach", 2), ("Esophagus", 2), ("Bladder", 1), ("Uterus", 1), ("Cervix", 1), ("CNS", 1),
          ("Bone", 1), ("HeadNeck", 1)]
NAMED = {"TP53": 50, "KRAS": 51, "CDKN2A": 52, "CDKN2B": 53, "KEAP1": 55, "MTAP": 64, "NQO1": 70, "HMOX1": 71,
         "AKR1C1": 72, "AKR1C2": 73, "TXNRD1": 74, "GCLM": 75, "SRXN1": 76, "NULLX": 700, "LEVX": 800}


def make_fixture(root, gK, Dn=1132, L=50, seed=1):
    """A tahoemap output with the real numbers of drug-doses and lines (see the module docstring, 4)."""
    from tahoemap.common import open_memmap
    rng = np.random.default_rng(seed)
    shutil.rmtree(root, ignore_errors=True)
    out, data = os.path.join(root, "out"), os.path.join(root, "data")
    organ = np.array(sum([[o] * n for o, n in ORGANS], []), dtype=object)[rng.permutation(L)]
    fx, G, sym, pc = _write_common(out, data, gK, Dn, L, organ, rng)
    for s, i in NAMED.items():
        sym[i] = s
    pd.DataFrame({"col": np.arange(G), "kind": ["gene"] * gK + ["module"] * 3, "token": np.arange(3, 3 + G),
                  "symbol": sym, "label": sym, "pooled_cpm": pc, "median_line_cpm": pc,
                  "n_lines_expressing": L}).to_csv(os.path.join(fx, "genes.csv"), index=False)
    rows = []
    for i in range(Dn):
        d = i // 3
        tg = f"TGT{d % 40}, TGT{d % 40 + 1}" if d % 3 == 0 else ""
        rows.append({"drug": f"Drug{d:03d}", "dose": ["0.05", "0.5", "5"][i % 3], "conc": [0.05, 0.5, 5.0][i % 3],
                     "flags": "", "targets": tg, "moa_broad": "inhibitor/antagonist", "plates": "p1", "wells": "A1"})
    pd.DataFrame(rows).to_csv(os.path.join(fx, "drugdose.csv"), index=False)
    pd.DataFrame({"cell_line_id": [f"CVCL_F{i:03d}" for i in range(L)], "cell_name": [f"Line{i:02d}" for i in range(L)],
                  "Organ": organ, "in_growth_analysis": True}).to_csv(os.path.join(fx, "lines.csv"), index=False)
    oi = {o: np.flatnonzero(organ == o) for o, _ in ORGANS}

    def within(frac, s):
        r = np.random.default_rng(s)
        m = np.zeros(L, bool)
        for idx in oi.values():
            k = int(round(frac * idx.size))
            if idx.size >= 2:
                k = min(max(k, 1), idx.size - 1)
            m[r.choice(idx, size=k, replace=False)] = True
        return m
    dep, res, tp53, cdkn2a = within(0.5, 11), within(0.5, 12), within(0.68, 13), within(0.45, 14)
    keap1 = np.zeros(L, bool)
    keap1[oi["Lung"][6:12]] = True
    hyper = np.zeros(L, bool)
    hyper[np.r_[oi["Bowel"][3:6], oi["Stomach"][:1], oi["Uterus"][:1], oi["Lung"][12:13]]] = True
    meta = []

    def add(i, gene, mech, vt="Missense"):
        meta.append({"cell_name": f"Line{i:02d}", "Cell_ID_DepMap": f"ACH-{i:06d}",
                     "Cell_ID_Cellosaur": f"CVCL_F{i:03d}", "Organ": organ[i], "Driver_Gene_Symbol": gene,
                     "Driver_VarZyg": "Hom", "Driver_VarType": vt,
                     "Driver_ProtEffect_or_CdnaEffect": "p.X1Y", "Driver_Mech_InferDM": mech,
                     "Driver_GeneType_DM": "Suppressor"})
    pool = [f"HYP{k:03d}" for k in range(150)]
    for i in range(L):
        add(i, "ANCHOR", None)
        if dep[i]:
            add(i, "FAKEDEP", "LoF")
        if res[i]:
            add(i, "FAKERES", "LoF")
        if tp53[i]:
            add(i, "TP53", "LoF" if rng.random() < 0.8 else None)
        if cdkn2a[i]:
            add(i, "CDKN2A", "LoF", "Deletion")
            if rng.random() < 0.7:
                add(i, "CDKN2B", "LoF", "Deletion")
        if keap1[i]:
            add(i, "KEAP1", "LoF")
        for k in range(60):                                               # random drivers: ~3-15 lines each
            if rng.random() < 0.03 + 0.15 * (k % 7) / 7:
                add(i, f"DRV{k:02d}", ["LoF", "GoF", None][k % 3])
        if hyper[i]:
            for gname in rng.choice(pool, size=30, replace=False):
                add(i, gname, [None, "LoF", "LoF", "GoF"][int(rng.integers(4))])
    pd.DataFrame(meta).to_parquet(os.path.join(data, "metadata", "cell_line_metadata.parquet"), index=False)
    # baseline: line-to-line variation; ~45% of genes absent from 1-4 organs (and a few flipped lines), 5% from a
    # few random lines
    lc = pc[None, :] * np.exp(rng.normal(0, 0.5, (L, G)))
    absent = np.zeros((L, G), bool)
    u = rng.random(gK)
    orgs = list(oi)
    for x in np.flatnonzero(u < 0.45):
        chosen = rng.choice(len(orgs), size=int(rng.integers(1, 5)), replace=False)
        absent[:, x] = np.isin(organ, [orgs[j] for j in chosen]) ^ (rng.random(L) < 0.08)
    for x in np.flatnonzero((u >= 0.45) & (u < 0.5)):
        absent[rng.choice(L, size=int(rng.integers(3, 8)), replace=False), x] = True
    nullx = within(0.2, 15)
    absent[:, 700] = nullx
    absent[:, 701:746] = False
    absent[:, 801:831] = False
    for name, x in NAMED.items():
        if name not in ("NULLX", "MTAP"):
            absent[:, x] = False
    absent[:, NAMED["MTAP"]] = cdkn2a                                       # MTAP lost with the CDKN2A deletion
    lc[absent] = pc[None, :].repeat(L, 0)[absent] * 0.05
    for s in ("NQO1", "HMOX1", "AKR1C1", "AKR1C2", "TXNRD1", "GCLM", "SRXN1"):
        lc[keap1, NAMED[s]] *= 5.0                                          # KEAP1 loss raises the NRF2 targets
    lc[np.ix_(nullx, np.arange(731, 746))] /= 4.0                          # NULLX absent: partners 4x lower
    levx = rng.normal(0, 1.0, L)
    lc[:, 800] = pc[800] * np.exp(levx)                                     # LEVX's level varies strongly
    np.save(os.path.join(fx, "line_cpm.npy"), lc.astype(np.float32))
    np.save(os.path.join(fx, "expr_mask.npy"), np.ones((L, G), bool))
    meas = ~absent[:, :gK]
    np.save(os.path.join(out, "tensor", "line_measured.npy"), meas)
    prog, d1 = np.arange(100, 140), np.arange(30, 36)
    broad, d2 = np.arange(200, 600), np.arange(60, 72, 3)
    nprog, dnull = np.arange(701, 731), np.arange(240, 246)
    lprog, dlev = np.arange(801, 831), np.arange(300, 306)
    # 40 compounds (2 doses each) that move 15 genes each in every line, as most drugs do: the lines' overall
    # responsiveness is read from such responses
    uni = [(np.arange(1000 + 15 * p, 1015 + 15 * p), 3 * (140 + p) + np.array([1, 2])) for p in range(40)]
    Zp = rng.standard_normal((Dn, G)).astype(np.float32)
    q = np.ones((Dn, G), np.float32)
    for P_, D_, zv, qv in [(prog, d1, 4.0, 1e-4), (broad, d2, 5.0, 1e-6), (nprog, dnull, 4.0, 1e-4),
                           (lprog, dlev, 4.0, 1e-4)] + [(u, d, 4.0, 1e-4) for u, d in uni]:
        Zp[np.ix_(D_, P_)] = zv
        q[np.ix_(D_, P_)] = qv
    np.save(os.path.join(fx, "DD_z.npy"), Zp)
    np.save(os.path.join(fx, "DD_lfc.npy"), (Zp * 0.15).astype(np.float32))
    np.save(os.path.join(fx, "DD_qup.npy"), q)
    np.save(os.path.join(fx, "DD_qdn.npy"), np.ones((Dn, G), np.float32))
    # cell numbers: line-specific drug effects (most drug-doses differ between lines) + planted effects
    A = rng.normal(0, 0.3, (Dn, L)) + rng.normal(0, 0.4, (Dn, 1)) * rng.normal(0, 1, (1, L))
    A[10] = rng.normal(0, 0.3, L)
    A[10, ~dep] -= 1.0                                                      # FAKEDEP-intact lines grow less
    lvl = np.log2(lc[:, 600] + 1)
    A[11] = rng.normal(0, 0.3, L) - 0.8 * (lvl - lvl.mean()) / lvl.std()    # FG00600's level -> sensitivity
    A[12] = rng.normal(0, 0.3, L)
    A[12, absent[:, NAMED["MTAP"]]] -= 1.2                                  # MTAP-null lines depleted
    A[13] = rng.normal(0, 0.3, L)
    A[13, tp53] += 0.9                                                      # TP53-altered lines resist
    np.save(os.path.join(fx, "DD_A.npy"), A.astype(np.float32))
    np.save(os.path.join(fx, "DD_Az.npy"), (A / 0.3).astype(np.float32))
    Zt = open_memmap(os.path.join(out, "tensor", "DDL_z.npy"), (gK, Dn, L), np.float32)
    levs = (levx - levx.mean()) / levx.std()
    for g0 in range(0, gK, 500):
        g1 = min(gK, g0 + 500)
        z = rng.standard_normal((g1 - g0, Dn, L), dtype=np.float32)
        for x in range(g0, g1):
            zz = z[x - g0]
            if 100 <= x < 140:
                zz[np.ix_(d1, np.flatnonzero(~dep))] += 6.0                 # only where FAKEDEP is intact
                zz[np.ix_(d1, np.flatnonzero(dep))] += 0.3
            if 200 <= x < 600:
                zz[np.ix_(d2, np.flatnonzero(~res))] += 5.0
                zz[np.ix_(d2, np.flatnonzero(res))] += 1.5                  # 0.3x: global resistance
            if 701 <= x < 731:
                zz[np.ix_(dnull, np.flatnonzero(~nullx))] += 6.0            # only where NULLX is expressed
                zz[np.ix_(dnull, np.flatnonzero(nullx))] += 0.5
            if 801 <= x < 831:
                zz[dlev] += (4.0 + 2.0 * levs)[None, :]                     # scales with LEVX's level
            if 1000 <= x < 1600:
                zz[uni[(x - 1000) // 15][1]] += 4.0                         # every line
        z[~meas[:, g0:g1].T[:, None, :].repeat(Dn, 1)] = np.nan
        Zt[g0:g1] = z
    del Zt
    _link_or_copy_lfc(os.path.join(out, "tensor"), 0.15)
    a = np.repeat(np.arange(gK), 100)
    b = rng.integers(0, gK, a.size)
    ex = []
    for P_ in [prog, np.r_[700, nprog, np.arange(731, 746)], np.r_[800, lprog]] + [u for u, _ in uni]:
        pa, pb = np.meshgrid(P_, P_)
        k = pa.ravel() != pb.ravel()
        ex.append((pa.ravel()[k], pb.ravel()[k]))
    a = np.r_[a, np.concatenate([x[0] for x in ex])]
    b = np.r_[b, np.concatenate([x[1] for x in ex])]
    m = a != b
    pd.DataFrame({"col_a": a[m], "col_b": b[m], "cos": rng.uniform(0.3, 0.9, int(m.sum())).astype(np.float32)}) \
        .to_parquet(os.path.join(out, "relations", "gene_relations.parquet"), index=False)
    return out, data, {"prog": prog, "broad": broad, "nprog": nprog, "nbase": np.arange(731, 746), "lprog": lprog}


def scale_checks(work, sizes):
    pts = []
    for gK in sizes:
        root = os.path.join(work, f"scale_{gK}")
        t0 = time.time()
        out, data, plant = make_fixture(root, gK)
        print(f"  fixture with {gK:,} genes x 1,132 drug-doses x 50 lines made in {(time.time() - t0) / 60:.1f} min",
              flush=True)
        rc, dt, info, _ = run_stage(out, data)
        shutil.rmtree(os.path.join(out, "tensor"), ignore_errors=True)       # free the disk for the next one
        pts.append((gK, rc, dt, info, out, plant))
        if rc != 0:
            break
    ok_runs = [p for p in pts if p[1] == 0]
    check("scale runs finish", lambda: (len(ok_runs) == len(sizes), "; ".join(
        f"{p[0]:,} genes: exit {p[1]}, {p[2] / 60:.2f} min, peak {p[3].get('peak_rss_mb')} MB" for p in pts)))
    if not ok_runs:
        return
    gK, _, _, info, out, plant = ok_runs[-1]
    e, g, ctl = load(out)
    tw = table_wide(e)

    def names(ix):
        return set(f"FG{i:05d}" for i in ix)

    def programme():
        r = e[(e["kind"] == "genotype_response") & (e["source"] == "FAKEDEP")]
        tg = names(plant["prog"])
        hit = r[r["target"].isin(tg) & (r["sign"] == 1)]
        prec = len(r[r["target"].isin(tg)]) / max(1, len(r))
        return len(hit) >= 0.8 * len(tg) and prec >= 0.8 and (hit["grade"] == "A").mean() >= 0.8, (
            f"FAKEDEP -> {len(hit)} of {len(tg)} programme genes (sign +1), {len(r)} FAKEDEP response edges "
            f"({prec:.0%} in the programme); grades {hit['grade'].value_counts().to_dict()}")
    check(f"scale ({gK:,} genes): a genotype-dependent programme is found (grade A)", programme)

    def global_res():
        r = e[(e["kind"] == "genotype_response") & (e["source"] == "FAKERES")]
        tg = names(plant["broad"])
        n = int(r["target"].isin(tg).sum())
        return n <= 0.05 * len(tg), (f"FAKERES (0.3x response in its lines at 4 broad drug-doses) -> {n} of the "
                                     f"{len(tg)} genes that respond there")
    check(f"scale ({gK:,} genes): a line-wide global resistance is not called gene-specific", global_res)

    def planted_cells():
        s = e[(e["kind"] == "genotype_sensitivity") & (e["source"] == "FAKEDEP") & (e["target_dd"] == 10) & tw]
        t = e[(e["kind"] == "genotype_sensitivity") & (e["source"] == "TP53") & (e["target_dd"] == 13) & tw]
        lv = e[(e["kind"] == "level_sensitivity") & (e["source"] == "FG00600") & (e["target_dd"] == 11) & tw]
        mt = e[(e["kind"] == "null_sensitivity") & (e["source"] == "MTAP") & (e["target_dd"] == 12)]
        ok = (len(s) == 1 and (s["sign"] == -1).all() and (t["sign"] == -1).any() and (t["sign"] != 1).all()
              and len(lv) == 1 and (lv["sign"] == -1).all() and len(mt) >= 1 and (mt["sign"] == 1).all())
        nt = info["tests"]["expression_null"]
        n_null = nt.get("sensitivity_within_organs", 0) + nt.get("sensitivity_across_organs", 0)
        return ok, (f"FAKEDEP -> cells (sign {s['sign'].tolist()}); TP53 -> cells (sign {t['sign'].tolist()}: -1 for "
                    "loss of function, 0 = not inferred for 'altered (any record)'; "
                    f"{t['group'].tolist()}); FG00600 level -> cells (sign {lv['sign'].tolist()}, q "
                    f"{lv['q'].round(6).tolist()}); MTAP-null -> cells, a lone effect among {n_null:,} tests (sign "
                    f"{mt['sign'].tolist()}, q {mt['q'].round(6).tolist()}, grade {mt['grade'].tolist()})")
    check(f"scale ({gK:,} genes): planted effects on cell numbers (genotype, level, lone natural knockout)",
          planted_cells)

    def keap1():
        b = e[(e["kind"] == "genotype_baseline") & (e["source"] == "KEAP1")]
        tg = {"NQO1", "HMOX1", "AKR1C1", "AKR1C2", "TXNRD1", "GCLM", "SRXN1"}
        h = b[b["target"].isin(tg)]
        return len(h) >= 3 and (h["sign"] == -1).all(), (
            f"KEAP1 (6 Lung lines; targets 5x) -> {len(h)} of 7 NRF2 targets at baseline, signs {h['sign'].tolist()}, "
            "grades "
            f"{h['grade'].value_counts().to_dict()}")
    check(f"scale ({gK:,} genes): KEAP1 -> NRF2 targets (baseline, sign -1)", keap1)

    def nullx():
        rr = e[(e["kind"] == "null_response") & (e["source"] == "NULLX") & e["target"].isin(names(plant["nprog"]))]
        bb = e[(e["kind"] == "null_baseline") & (e["source"] == "NULLX") & e["target"].isin(names(plant["nbase"]))]
        return len(rr) >= 0.6 * len(plant["nprog"]) and len(bb) >= 0.6 * len(plant["nbase"]) and \
            (rr["sign"] == 1).all() and (bb["sign"] == 1).all(), (
                f"NULLX-null (12 lines) -> {len(rr)} of {len(plant['nprog'])} partners' responses, {len(bb)} of "
                f"{len(plant['nbase'])} partners' baseline levels (4x lower; sign +1), grades "
                f"{pd.concat([rr, bb])['grade'].value_counts().to_dict()}")
    check(f"scale ({gK:,} genes): a natural knockout's partner effects (null_response, null_baseline)", nullx)

    def levx():
        lv = e[(e["kind"] == "level") & (e["source"] == "LEVX") & e["target"].isin(names(plant["lprog"]))]
        clear = int(lv["direction_clear"].fillna(False).astype(bool).sum())
        rev = e[(e["kind"] == "level") & (e["target"] == "LEVX") & (e["direction_clear"].fillna(False).astype(bool))]
        return len(lv) >= 0.6 * len(plant["lprog"]) and clear >= 0.5 * len(lv) and len(rev) == 0, (
            f"LEVX's level -> {len(lv)} of {len(plant['lprog'])} partners' responses (q max "
            f"{lv['q'].max() if len(lv) else float('nan'):.2g}), {clear} with the direction clear; reverse edges "
            f"called clear: {len(rev)}; among {info['tests']['level_pairs']:,} directed pairs")
    check(f"scale ({gK:,} genes): a level modulator -> its partners (level, direction clear)", levx)

    def negatives():
        s = ctl["negative"]["summary"]
        rnd = e[e["source"].str.match(r"^(DRV\d+|HYP\d+)$") & e["kind"].str.startswith("genotype")]
        rnd_tw = rnd[table_wide(rnd)]
        n_rnd = int(g[(g["kind"] == "genotype") & g["gene"].str.match(r"^(DRV\d+|HYP\d+)$")].shape[0])
        rate = sum((v["pseudo_edges_mean_per_group"] or 0) for v in s.values())
        ok = all((v["pseudo_edges_mean_per_group"] or 0) <= 0.2 for v in s.values()) and \
            len(rnd_tw) <= max(5.0, 2.0 * rate * n_rnd)
        return ok, ("; ".join(f"{k}: pseudo {v['pseudo_edges_mean_per_group']} vs real "
                              f"{v['real_edges_mean_per_group']} table-wide edges per group" for k, v in s.items())
                    + f"; random driver groups (DRV / HYP, {n_rnd} groups, no planted effect): {len(rnd_tw)} "
                      f"table-wide edges (the pseudo rate predicts {rate * n_rnd:.1f}), {len(rnd) - len(rnd_tw)} "
                      "within their group only (grade C)")
    check(f"scale ({gK:,} genes): pseudo-groups and random driver groups give ~no edges", negatives)

    def tissue():
        ps = g[g["kind"] == "pseudo"]
        rd = g[(g["kind"] == "genotype") & g["gene"].str.match(r"^(DRV\d+|HYP\d+)$")]
        a, b = float(ps["tissue_confounded"].mean()), float(rd["tissue_confounded"].mean())
        nul = info["groups_tested"]
        return a <= 0.2 and b <= 0.25 and nul["expression_null_line_sets_across_organs"] > 0, (
            f"tissue-confounded: {a:.0%} of {len(ps)} pseudo-groups, {b:.0%} of {len(rd)} random driver groups (16 "
            f"organs, Lung 14 of 50 lines); expression-null sets compared across organs (tested, separate BH "
            f"family): {nul['expression_null_line_sets_across_organs']:,} of {nul['expression_null_line_sets']:,}")
    check(f"scale ({gK:,} genes): the tissue alert fires only on organ-concentrated comparisons", tissue)

    def controls():
        ef = info["expected_false_edges"]
        lv = ctl["level_controls"]
        ok = all((ef[k]["expected_false"] or 0) <= 0.1 * ef[k]["edges"] + 3 for k in ("level", "level_sensitivity"))
        return ok, ("expected false edges: " + "; ".join(f"{k} {v['expected_false']} of {v['edges']}"
                                                           for k, v in ef.items())
                    + f"; level calibration {lv['level'].get('calibration')}; level_sensitivity calibration "
                      f"{lv['level_sensitivity'].get('calibration')}, {info['variable_drugdoses']} variable "
                      "drug-doses")
    check(f"scale ({gK:,} genes): permuted-level controls give no more level edges than the 10% FDR allows",
          controls)

    def extrapolate():
        if len(ok_runs) < 2:
            g_, _, dt, inf, _, _ = ok_runs[0]
            mem = inf["peak_rss_mb"] / 1024 * max(1.0, FULL_GENES / g_)
            mins = dt / 60 * max(1.0, FULL_GENES / g_)
        else:
            (g1, _, t1, i1, _, _), (g2, _, t2, i2, _, _) = ok_runs[-2], ok_runs[-1]
            m1, m2 = i1["peak_rss_mb"] / 1024, i2["peak_rss_mb"] / 1024
            mem = m2 + max(0.0, (m2 - m1) / (g2 - g1) * (FULL_GENES - g2))
            mins = t2 / 60 + max(0.0, (t2 - t1) / 60 / (g2 - g1) * (FULL_GENES - g2))
        inf = ok_runs[-1][3]
        return mem <= MEM_LIMIT_GB and mins <= MINUTES_LIMIT, (
            f"{'measured at' if ok_runs[-1][0] >= FULL_GENES else 'extrapolated to'} {FULL_GENES:,} genes: peak "
            f"{mem:.2f} GB (limit {MEM_LIMIT_GB}), {mins:.1f} min (limit {MINUTES_LIMIT}; this machine: "
            f"{os.cpu_count()} CPUs); largest run: {inf.get('groups_tested')}, {inf.get('variable_drugdoses')} "
            f"variable drug-doses, chunk {inf.get('chunk')} genes")
    check("scale: bounded memory and time", extrapolate)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", default=None, help="a finished synthetic output (default: run_tests.py's out_seed0)")
    ap.add_argument("--data", default=None, help="its data folder (with ground_truth.json)")
    ap.add_argument("--work", default=None, help="work folder (default: a temporary folder)")
    ap.add_argument("--no-fixture", action="store_true", help="skip the 50-line fixture")
    ap.add_argument("--no-scale", action="store_true", help="skip the full-dimension scale runs")
    ap.add_argument("--scale-genes", default="4000,8000", help="genes of the scale fixtures (e.g. 16643)")
    ap.add_argument("--keep", action="store_true", help="keep the work folder")
    a = ap.parse_args()
    src = a.src or os.path.join(DEFAULT_WORKDIR, "out_seed0")
    data = a.data or os.path.join(os.path.dirname(src), "data_seed0")
    if not os.path.exists(os.path.join(src, "stages", "relations.json")):
        print(f"{src} has no finished synthetic run: making one with run_tests.py ...", flush=True)
        subprocess.run([sys.executable, os.path.join(HERE, "run_tests.py"), "--workdir", os.path.dirname(src)],
                       cwd=REPO, check=False)
    work = a.work or tempfile.mkdtemp(prefix="tahoe_direction_")
    os.makedirs(work, exist_ok=True)
    print(f"Synthetic output {src}; work folder {work}", flush=True)
    out = os.path.join(work, "out")
    copy_output(src, out)
    rc, dt, info, console = run_stage(out, data)
    check("stage finishes on the synthetic output", lambda: (
        rc == 0, f"exit code {rc} in {dt:.0f} s, peak memory {info.get('peak_rss_mb')} MB, "
                 f"{info.get('edges')} edges"))
    if rc == 0:
        check("synthetic run within bounded memory (< 1.5 GB)", lambda: (
            (info.get("peak_rss_mb") or 0) < 1536, f"peak RSS {info.get('peak_rss_mb')} MB, chunk {info.get('chunk')}"))
        e = synthetic_checks(out, data, info, console)
        chunk_check(src, data, work, e)
        variant_checks(src, data, work)
    if not a.no_fixture:
        small_fixture_checks(work)
    if not a.no_scale:
        scale_checks(work, [int(x) for x in a.scale_genes.split(",") if x.strip()])
    n = {s: sum(r[0] == s for r in RESULTS) for s in ("PASS", "FAIL")}
    print(f"\n{n['PASS']} passed, {n['FAIL']} failed", flush=True)
    if not a.keep and not a.work:
        shutil.rmtree(work, ignore_errors=True)
    sys.exit(1 if n["FAIL"] else 0)


if __name__ == "__main__":
    main()
