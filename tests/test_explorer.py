#!/usr/bin/env python3
"""test_explorer - checks of the explorer stage (OUT/explorer) on a finished synthetic run (design section 11.1,
items 1-7): exact values, flags, records, completeness, the planted answers, determinism and sizes.

    python tests/test_explorer.py --out OUT --data DATA [--work DIR] [--keep]

check(out, data, report=None, work=None) runs every check. report: run_tests.py's check(stage, name, fn) (each fn
returns (ok, detail)); without it each result is printed. Returns the list of (name, status, detail). The checks read
OUT/explorer when it exists (else they build it in a copy of OUT); the determinism, size-guard and option checks run
the stage in copies of OUT under --work (default: OUT/../explorer_test_work/run_*, removed at the end unless --keep).
"""

import argparse
import json
import os
import shutil
import sys
import tempfile
import traceback

import numpy as np
import pandas as pd

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if REPO not in sys.path:
    sys.path.insert(0, REPO)

# The real run's dimensions and row counts (the pushed results: stages/*.json and the published tables), for the
# size projection of item 7. Bytes per row of the record tables were measured on the published real tables
# (scratch measurement at the time this test was written: a floor for tables that are near-empty in synthetic data,
# e.g. annotations without network access).
REAL = {"genes": 16643, "columns": 16646, "drugdoses": 1132, "lines": 50, "wells": 1329, "plates": 14,
        "modules": 235, "drugs": 379, "dims": 64,
        "rows": {"tables/line_effects.parquet": 832150, "tables/drug_line_top.parquet": 367475,
                 "relations/gene_relations.parquet": 1507600, "direction/edges.parquet": 102590,
                 "direction/groups.parquet": 5915, "graph/nodes.parquet": 15076, "graph/edges.parquet": 179308,
                 "reference/annotations.parquet": 16643, "reference/gene_sets.parquet": 121626,
                 "reference/string_pairs.parquet": 626218, "tables/drug_effects.parquet": 539607,
                 "validation/novel_edges.csv": 2815, "validation/novel_members.csv": 10000,
                 "tables/genes.parquet": 16643, "embed/genes.parquet": 16643}}
REAL_BYTES_PER_ROW = {"reference/annotations.parquet": 700.0, "reference/gene_sets.parquet": 12.0,
                      "reference/string_pairs.parquet": 8.0, "validation/novel_edges.csv": 120.0,
                      "validation/novel_members.csv": 80.0}
WEB_PROJECTED_MAX = 0.85e9


def _ex():
    from tahoemap import explorer as E
    return E


class Ctx:
    """The explorer under test and its sources, decoded once."""

    def __init__(self, out, data, work):
        E = _ex()
        self.out, self.data, self.work = out, data, work
        self.E = E
        self.xo = out
        if not os.path.isdir(os.path.join(out, "explorer")):
            self.xo = os.path.join(work, "built")
            _copy_out(out, self.xo)
            E.run(self.xo)
        self.root = os.path.join(self.xo, "explorer")
        self.web, self.dvol = os.path.join(self.root, "web"), os.path.join(self.root, "data")
        self.S = E.Src(self.xo)
        self.stamp = json.load(open(os.path.join(self.xo, "stages", "explorer.json"), encoding="utf-8"))
        self.man = json.load(open(os.path.join(self.root, "manifest.json"), encoding="utf-8"))
        self.truth = json.load(open(os.path.join(data, "ground_truth.json"), encoding="utf-8")) if data else {}
        self._sh = {}
        fx = self.S.fx
        self.DD = {k: np.load(os.path.join(fx, f"DD_{k}.npy")) for k in ("lfc", "z", "qup", "qdn", "poseff")}
        self.gK, self.C, self.D, self.L = self.S.gK, self.S.C, self.S.D, self.S.L
        self.flags = self.shard("web", "d/flags.js")[2]["flags"]
        self.core = self.shard("web", "d/core.js")
        self.sym = {s: i for i, s in enumerate(self.S.ix["genes"]["symbol"].astype(str)) if i < self.gK}

    def files(self, vol, prefix=""):
        root = self.web if vol == "web" else (self.dvol if vol == "data" else os.path.join(self.root, vol))
        out = []
        for r, _d, fs in os.walk(root):
            for f in fs:
                rel = os.path.relpath(os.path.join(r, f), root).replace(os.sep, "/")
                if rel.startswith(prefix) and rel.endswith(".js") and rel not in ("d/hosts.js", "probe.js", "app.js"):
                    out.append(rel)
        return sorted(out)

    def shard(self, vol, rel, cache=True):
        key = (vol, rel)
        if key in self._sh:
            return self._sh[key]
        root = self.web if vol == "web" else (self.dvol if vol == "data" else os.path.join(self.root, vol))
        v = self.E.read_shard(os.path.join(root, *rel.split("/")))
        if cache:
            self._sh[key] = v
        return v

    def gene_shard(self, col):
        return self.shard("web", f"d/{self.E.g_id(col // self.E.BUCKET)}.js")


def _copy_out(src, dst, with_explorer=False):
    """A copy of an output folder for a stage run (the big inputs hard-linked when possible; never modified in place:
    the stage writes new files)."""
    if os.path.exists(dst):
        shutil.rmtree(dst)

    def ign(d, names):
        return [n for n in names if os.path.abspath(d) == os.path.abspath(src)
                and n in (("explorer.tmp", "explorer.old") if with_explorer else ("explorer", "explorer.tmp",
                                                                                   "explorer.old"))]

    def cp(s, d):
        try:
            os.link(s, d)
        except OSError:
            shutil.copy2(s, d)
    shutil.copytree(src, dst, ignore=ign, copy_function=cp)
    p = os.path.join(dst, "stages", "explorer.json")
    if not with_explorer and os.path.exists(p):
        os.remove(p)


def _bits(a):
    a = np.ascontiguousarray(a)
    return a.view(f"u{a.dtype.itemsize}") if a.dtype.kind == "f" else a


def _eq_bits(a, b):
    a, b = np.asarray(a), np.asarray(b)
    return a.dtype == b.dtype and a.shape == b.shape and np.array_equal(_bits(a), _bits(b))


# ----------------------------------------------------------------------------- 1. exactness
def t_exact_pooled(c):

    bad, n = [], 0
    G = {k: np.full((c.D, c.C), np.nan, np.float32) for k in ("lfc", "z", "q_up", "q_dn")}
    FLg = np.zeros((c.D, c.C), np.int64)
    for rel in c.files("web", "d/g/"):
        h, a, _t = c.shard("web", rel, cache=False)
        cols = a["cols"].astype(np.int64)
        for k, src in (("lfc", "lfc"), ("z", "z"), ("q_up", "qup"), ("q_dn", "qdn")):
            if not _eq_bits(a[k], np.ascontiguousarray(c.DD[src][:, cols].T)):
                bad.append(f"{rel} {k}")
            G[k][:, cols] = a[k].T
        FLg[:, cols] = a["flag"].T
        n += 1
    for k in G:
        if np.isnan(G[k]).all():
            bad.append(f"{k}: no values")
    P = {k: np.full((c.D, c.C), np.nan, np.float32) for k in G}
    FLp = np.zeros((c.D, c.C), np.int64)
    for rel in c.files("data", "p/"):
        h, a, _t = c.shard("data", rel, cache=False)
        dd = int(h["meta"]["dd"])
        for k, src in (("lfc", "lfc"), ("z", "z"), ("q_up", "qup"), ("q_dn", "qdn"), ("poseff", "poseff")):
            if not _eq_bits(a[k], c.DD[src][dd]):
                bad.append(f"{rel} {k}")
            if k in P:
                P[k][dd] = a[k]
        FLp[dd] = a["flag"]
        n += 1
    agree = all(_eq_bits(G[k], P[k]) for k in G) and np.array_equal(FLg, FLp)
    return (not bad and agree and n == len(c.files("web", "d/g/")) + c.D,
            f"{n} files: g/ and p/ equal DD_lfc / DD_z / DD_qup / DD_qdn (/ DD_poseff) through uint32 views (NaN "
            f"positions included); the two orientations agree: {agree}" + (f"; differing: {bad[:8]}" if bad else ""))


def t_exact_lines(c):
    S = c.S
    DL, DZ = S.npy("tensor/DDL_lfc.npy"), S.npy("tensor/DDL_z.npy")
    W = {k: np.load(os.path.join(S.fx, f"{k}.npy")) for k in ("W1", "W2", "Z")}
    cnt, pu = np.load(S.path("tensor/well_counts.npy")), np.load(os.path.join(S.fx, "posunc.npy"))
    pb = np.load(S.path("tensor/plate_base.npy"))
    small = {k: np.load(os.path.join(S.fx, f"{r}.npy")) for k, r in (("poff", "plate_offset"), ("slot", "slot_median"),
                                                                   ("psg", "plate_scale_gene"))}
    bad, n = [], 0
    for rel in c.files("data", "x/"):
        h, a, _t = c.shard("data", rel, cache=False)
        col = int(h["meta"]["col"])
        exp = {"w1": W["W1"][:, col], "w2": W["W2"][:, col], "wz": W["Z"][:, col], "wpu": pu[:, col].astype(np.uint8),
               "poseff": c.DD["poseff"][:, col], **{k: v[:, col] for k, v in small.items()}}
        if col < c.gK:
            exp.update(lfc=DL[col], z=DZ[col], counts=cnt[:, col], pbase=pb[:, :, col])
        for k, v in exp.items():
            if k not in a or not _eq_bits(a[k], np.ascontiguousarray(v)):
                bad.append(f"{rel} {k}")
        n += 1
    return (not bad and n == c.C, f"{n} x/ files ({c.C} columns): lfc / z equal DDL_*[col] through uint16 views; "
            "W1, W2, Z, counts, plate_base, plate_offset, slot_median, plate_scale_gene, posunc, poseff exact"
            + (f"; differing: {bad[:8]}" if bad else ""))


# ----------------------------------------------------------------------------- 2. flags
def t_flags(c):
    from tahoemap import tables as TB
    F = TB.gene_flag_inputs(c.xo)
    gK, D = c.gK, c.D
    d = np.repeat(np.arange(D), gK)
    g = np.tile(np.arange(gK), D)
    s, cl = TB.flag_strings(F["dd_flags"], d, F["posunc"][d, g], F["poseff"][d, g], F["pscale"][d, g],
                            TB.cc_pct(F["cc_share"][d, g], F["cc_cleared"][d, g]))
    codes = np.zeros((D, gK), np.int64)
    for rel in c.files("web", "d/g/"):
        if rel == "d/g/mod.js":
            continue
        _h, a, _t = c.shard("web", rel)
        codes[:, a["cols"]] = a["flag"].T
    dic = c.flags["s"].astype(object).to_numpy()
    dclean = c.flags["clean"].to_numpy(dtype=bool)
    got = dic[codes.ravel()]
    n_bad = int((got != s).sum())
    n_cbad = int((dclean[codes.ravel()] != cl).sum())
    return (n_bad == 0 and n_cbad == 0, f"{s.size:,} (drug-dose, gene) flag strings equal tables.flag_strings "
            f"recomputed ({n_bad} differ; clean differs at {n_cbad}); {len(dic)} distinct strings")


def t_drug_effects(c):
    from tahoemap import tables as TB
    de = pd.read_parquet(c.S.path("tables/drug_effects.parquet"))
    bad = {}
    col, dd = de["col"].to_numpy(np.int64), de["dd"].to_numpy(np.int64)
    rows = {}
    for b in np.unique(col // c.E.BUCKET):
        _h, a, _t = c.shard("web", f"d/{c.E.g_id(int(b))}.js")
        rows[int(b)] = a
    cc_dd = list(c.core[1]["cc_dd"])
    drug_of = c.core[1]["drug_of_dd"]
    dic = c.flags["s"].astype(object).to_numpy()
    dclean = c.flags["clean"].to_numpy(dtype=bool)
    pats = np.array(list(TB.PATTERNS), dtype=object)
    for i in range(len(de)):
        a = rows[int(col[i] // c.E.BUCKET)]
        j = int(col[i] - a["cols"][0])
        k = int(dd[i])
        r = de.iloc[i]
        chk = {"lfc": np.float32(a["lfc"][j, k]).view(np.uint32) == np.float32(r["lfc"]).view(np.uint32),
               "z": np.float32(a["z"][j, k]).view(np.uint32) == np.float32(r["z"]).view(np.uint32),
               "q_up": np.float32(a["q_up"][j, k]).view(np.uint32) == np.float32(r["q_up"]).view(np.uint32),
               "q_down": np.float32(a["q_dn"][j, k]).view(np.uint32) == np.float32(r["q_down"]).view(np.uint32),
               "flags": dic[a["flag"][j, k]] == (r["flags"] if isinstance(r["flags"], str) else ""),
               "clean": bool(dclean[a["flag"][j, k]]) == bool(r["clean"]),
               "n_lines_measured": int(a["nl"][j, k, 0]) == int(r["n_lines_measured"]),
               "n_lines_up": int(a["nl"][j, k, 1]) == int(r["n_lines_up"]),
               "n_lines_down": int(a["nl"][j, k, 2]) == int(r["n_lines_down"]),
               "pattern_up": pats[a["pat"][j, drug_of[k], 0]] == r["pattern_up"],
               "pattern_down": pats[a["pat"][j, drug_of[k], 1]] == r["pattern_down"]}
        ccv = np.float32(a["cc"][j, cc_dd.index(k)]) if k in cc_dd else np.float32(np.nan)
        chk["cc_share"] = ccv.view(np.uint32) == np.float32(r["cc_share"]).view(np.uint32)
        for kk, ok in chk.items():
            if not ok:
                bad[kk] = bad.get(kk, 0) + 1
    # the notable set: |z| >= KEEP_Z or q < Q_CUT, over every gene x drug-dose of the explorer
    keep = set()
    for b, a in ((b, c.gene_shard(b * c.E.BUCKET)[1]) for b in range((c.gK + 15) // 16)):
        jj, kk = np.nonzero((np.abs(a["z"]) >= TB.KEEP_Z) | (a["q_up"] < TB.Q_CUT) | (a["q_dn"] < TB.Q_CUT))
        keep |= set(zip((a["cols"][jj]).tolist(), kk.tolist()))
    same = keep == set(zip(col.tolist(), dd.tolist()))
    return (not bad and same, f"{len(de):,} drug_effects rows: flags, clean, cc_share, n_lines_*, pattern_*, lfc, z, "
            f"q equal the explorer's values (differing: {bad or 'none'}); notable set == drug_effects pairs: {same}")


def t_nl_counts(c):
    from tahoemap import tables as TB
    le = pd.read_parquet(c.S.path("tables/line_effects.parquet"))
    t = c.core[0]["meta"]["constants"]["line_z_threshold"]
    meas = np.load(c.S.path("tensor/line_measured.npy"))
    up = le.pivot(index="col", columns="line", values="n_dd_up_all").to_numpy()
    dn = le.pivot(index="col", columns="line", values="n_dd_down_all").to_numpy()
    bad_le, bad_nl = 0, 0
    for col in range(c.gK):
        _h, a, _t = c.shard("data", f"{c.E.x_id(col)}.js", cache=False)
        Z, X = a["z"].astype(np.float32)[None], a["lfc"].astype(np.float32)[None]
        m = TB.line_counts(Z, X, t, measured=meas[:, col:col + 1], masks=True)
        bad_le += int((m[3][0].sum(axis=0) != up[col]).sum() + (m[4][0].sum(axis=0) != dn[col]).sum())
        g = c.gene_shard(col)[1]
        j = col - int(g["cols"][0])
        cnt = np.stack([mm[0].sum(axis=1) for mm in m], axis=-1)
        bad_nl += int((cnt != g["nl"][j]).sum())
    return (bad_le == 0 and bad_nl == 0, f"per-line T-counts from the x/ files reproduce line_effects n_dd_up_all / "
            f"n_dd_down_all for all {c.gK} genes x {c.L} lines ({bad_le} differ); g/ nl equals them ({bad_nl} differ)")


# ----------------------------------------------------------------------------- 3. records
def t_records(c):
    E = c.E
    S = c.S
    held, probs, n_tab, srcs = {}, [], 0, {}
    for vol in ("web", "data"):
        for rel in c.files(vol):
            h, _a, tabs = c.shard(vol, rel, cache=False)
            for name, df in tabs.items():
                src = E.TABLE_SOURCES.get((h["kind"], name))
                if src is None or "_row" not in df:
                    continue
                if src not in srcs:
                    srcs[src] = S.df(src)
                d = E.table_diff(srcs[src], df, projection=(h["kind"], name) in E.PROJECTIONS)
                n_tab += 1
                if d:
                    probs.append(f"{rel} {name}: {d}")
                held.setdefault((h["kind"], name, src), []).append(df["_row"].to_numpy())
    cover = {}
    for (k, name, src), parts in held.items():
        rows = np.concatenate(parts) if parts else np.zeros(0)
        cover[f"{k}.{name}"] = (len(np.unique(rows)), len(srcs[src]), src)
    full = ("gene-bucket.le", "line.le", "gene-bucket.dlt", "gene-bucket.rel", "gene-bucket.relb", "dir-groups.edges",
            "dir-groups.groups", "groups.groups", "gene-bucket.ann", "gene-bucket.node", "module.members",
            "gene-bucket.gedge", "gene-bucket.nmem", "drug.de", "core.wells", "core.drugdoses", "val.novel_members")
    short = [f"{k} {v[0]}/{v[1]}" for k, v in cover.items() if k in full and v[0] != v[1]]
    # direction: every edge in every bucket it touches
    ed = S.df("direction/edges.parquet")
    miss = 0
    for rel in c.files("web", "d/g/"):
        if rel == "d/g/mod.js":
            continue
        h, a, t = c.shard("web", rel)
        c0, c1 = h["meta"]["cols"]
        want = set(np.flatnonzero(ed["source_col"].between(c0, c1 - 1) | ed["target_col"].between(c0, c1 - 1)))
        miss += len(want ^ set(t["dir"]["_row"].tolist()))
    return (not probs and not short and miss == 0,
            f"{n_tab} record tables decoded: each equals its source (values exact, text unclipped); complete views "
            f"hold every source row ({'all' if not short else short}); every direction edge is in every bucket it "
            f"touches ({miss} misplaced)" + (f"; differences: {probs[:5]}" if probs else ""))


# ----------------------------------------------------------------------------- 4. completeness
def t_complete(c):
    info = c.stamp["info"]
    bad = [f"{s} {v}: {g}/{w}" for s, r in info["complete"].items() for v, (g, w) in r["views"].items() if g != w]
    return (info.get("complete_ok") and not bad, f"stamp: {len(info['complete'])} source tables, every view holds "
            "the rows it must (" + ("all equal" if not bad else "; ".join(bad[:5])) + ")")


def t_inventory(c):
    E = c.E
    un = []
    n = 0
    for root, _d, fs in os.walk(c.xo):
        for f in fs:
            rel = os.path.relpath(os.path.join(root, f), c.xo).replace(os.sep, "/")
            n += 1
            if E.inventory_pattern(rel) is None:
                un.append(rel)
    return (not un, f"explorer.INVENTORY covers all {n:,} files of OUT" + (f"; not covered: {un[:10]}" if un else ""))


# ----------------------------------------------------------------------------- 5. planted answers
def _dd_index(c):
    dd = c.S.ix["drugdose"]
    return {(str(d), float(x)): i for i, (d, x) in enumerate(zip(dd["drug"].astype(str), dd["conc"]))}


def t_planted(c):
    T = c.truth
    out, ok = [], True
    ddi = _dd_index(c)
    names = list(c.S.ix["lines"]["cell_name"].astype(str))
    # CDKN1A: mean per-line z in the TP53-wt lines above the altered lines at the three DNA-damage drugs (5 uM)
    g = T.get("groups", {})
    wt = [names.index(x) for x in g.get("tp53_wt", []) if x in names]
    alt = [names.index(x) for x in g.get("tp53_altered", []) if x in names]
    _h, a, _t = c.shard("data", f"{c.E.x_id(c.sym['CDKN1A'])}.js")
    zz = a["z"].astype(np.float64)
    res = []
    for drug in ("Doxorubicin (hydrochloride)", "Topotecan (hydrochloride)", "5-Fluorouracil"):
        k = ddi[(drug, 5.0)]
        mw, ma = np.nanmean(zz[k, wt]), np.nanmean(zz[k, alt])
        res.append(mw > ma)
        out.append(f"CDKN1A {drug.split(' ')[0]} wt {mw:.1f} > altered {ma:.1f}")
    ok &= all(res) and len(wt) == 8 and len(alt) == 10
    # Doxorubicin 5 uM toxic, present for every gene; Bortezomib 5 uM toxic + transcription drop on every gene cell
    dic = c.flags["s"].astype(object).to_numpy()
    for drug, toks in (("Doxorubicin (hydrochloride)", ("toxic",)), ("Bortezomib", ("toxic", "transcription drop"))):
        k = ddi[(drug, 5.0)]
        h, a, _t = c.shard("data", f"{c.E.p_id(k)}.js")
        fl = dic[a["flag"][:c.gK]]
        good = all(all(tk in s.split("; ") for tk in toks) for s in fl) and len(a["lfc"]) == c.C
        ok &= good
        out.append(f"{drug.split(' ')[0]} 5 uM: {'; '.join(toks)} on all {len(fl)} genes: {good}")
    # NQO1: Dimethyl fumarate's top dose is the top raiser
    _h, a, _t = c.gene_shard(c.sym["NQO1"])
    j = c.sym["NQO1"] - int(a["cols"][0])
    top = int(np.nanargmax(a["z"][j]))
    want = max((x, i) for (d, x), i in ddi.items() if d == "Dimethyl fumarate")[1]
    ok &= top == want
    out.append(f"NQO1 top raiser dd {top} = Dimethyl fumarate top dose {want}: {top == want}")
    # MTAP: a position flag at the drug-doses of well H1, and a low baseline in the MTAP-null lines
    wells = c.core[2]["wells"]
    h1 = wells[(wells["well"] == "H1") & wells["used_in_drugdose"].astype(bool)]["drugdose_row"].astype(int)
    _h, a, _t = c.gene_shard(c.sym["MTAP"])
    j = c.sym["MTAP"] - int(a["cols"][0])
    pos = ("position effect removed", "position correction uncertain", "position not correctable")
    hit = [any(p in dic[a["flag"][j, k]] for p in pos) for k in h1]
    _h, la, _t = c.shard("web", "d/linecpm.js")
    cpm = la["line_cpm"][:, c.sym["MTAP"]]
    null = [names.index(x) for x in g.get("mtap_null", []) if x in names]
    rest = [i for i in range(c.L) if i not in null]
    low = float(np.mean(cpm[null])) < 0.3 * float(np.median(cpm[rest]))
    ok &= all(hit) and len(hit) > 0 and low
    out.append(f"MTAP position flag at {sum(hit)} of {len(hit)} H1 drug-doses; low baseline in {len(null)} null "
               f"lines: {low}")
    # Plate3: smp_1727 failed
    fw = c.core[2]["failed_wells"]
    f_ok = bool(((fw["sample"].astype(str) == "smp_1727") & (fw["plate"].astype(str) == "plate3")).any())
    ok &= f_ok
    out.append(f"plate3 smp_1727 failed: {f_ok}")
    # TRIM72 below detection
    b = c.shard("web", "d/below.js")[2]["b"]
    t_ok = "TRIM72" in set(b["symbol"].astype(str))
    ok &= t_ok
    out.append(f"TRIM72 in below.js: {t_ok}")
    # NFE2L2: its level arrows are in its bucket
    ed = c.S.df("direction/edges.parquet")
    lv = set(ed.index[(ed["source"] == "NFE2L2") & (ed["kind"] == "level")])
    _h, _a, t = c.gene_shard(c.sym["NFE2L2"])
    n_ok = len(lv) > 0 and lv <= set(t["dir"]["_row"].tolist())
    ok &= n_ok
    out.append(f"NFE2L2: its {len(lv)} level arrows in its bucket: {n_ok}")
    # MG53-like genes: the highest-z drug-dose carries an artifact flag -> it is row 0 of the default order
    art = ~c.flags["clean"].to_numpy(dtype=bool)
    n_mg, n_bad = 0, 0
    for b_ in range((c.gK + 15) // 16):
        _h, a, _t = c.gene_shard(b_ * 16)
        for j in range(len(a["cols"])):
            z = a["z"][j].astype(np.float64)
            if not np.isfinite(z).any():
                continue
            top = int(np.nanargmax(z))
            if art[a["flag"][j, top]]:
                n_mg += 1
                order = np.lexsort((np.arange(z.size), np.isnan(z), -np.nan_to_num(z, nan=-np.inf)))
                n_bad += int(order[0] != top)
    ok &= n_mg > 0 and n_bad == 0
    out.append(f"{n_mg} MG53-like genes (strongest raiser flagged): its row is first in the z order for all "
               f"({n_bad} not)")
    return ok, "; ".join(out)


# ----------------------------------------------------------------------------- 6-7. stage runs in a copy
def t_determinism(c):
    E = c.E
    d = os.path.join(c.work, "det")
    _copy_out(c.out, d)
    E.run(d)
    m1 = json.load(open(os.path.join(d, "explorer", "manifest.json"), encoding="utf-8"))["manifest_sha256"]
    E.run(d)
    m2 = json.load(open(os.path.join(d, "explorer", "manifest.json"), encoding="utf-8"))["manifest_sha256"]
    shutil.rmtree(d, ignore_errors=True)
    return m1 == m2, (f"two stage runs: MANIFEST.tsv sha256 identical for every volume ({m1})" if m1 == m2 else
                      f"two stage runs: MANIFEST.tsv sha256 differ: {m1} vs {m2}")


def t_sizes(c):
    """Files <= 10 MB on synthetic data, folders <= 1,000 entries, paths <= 80 characters; and the web volume
    projected to the real dimensions <= 0.85 GB."""
    big, crowded, long_ = [], [], []
    for vol in ("web", "data"):
        root = os.path.join(c.root, vol)
        for r, ds, fs in os.walk(root):
            if len(ds) + len(fs) > 1000:
                crowded.append(r)
            for f in fs:
                rel = os.path.relpath(os.path.join(r, f), root).replace(os.sep, "/")
                if os.path.getsize(os.path.join(r, f)) > 10e6:
                    big.append(rel)
                if len(rel) > 80:
                    long_.append(rel)
    proj, parts = project_web(c)
    ok = not big and not crowded and not long_ and proj <= WEB_PROJECTED_MAX
    return ok, (f"files <= 10 MB ({big or 'all'}), folders <= 1,000 entries ({crowded or 'all'}), paths <= 80 "
                f"characters ({long_ or 'all'}); web volume projected to the real dimensions: {proj / 1e9:.2f} GB "
                f"(limit {WEB_PROJECTED_MAX / 1e9:.2f}): "
                + ", ".join(f"{k} {v / 1e6:.0f} MB" for k, v in parts.items()))


def project_web(c):
    """The web volume at the real dimensions, from this run's bytes: each array of the gene, line and module files by
    bytes per element times its real number of elements; each record table by bytes per row (the per-file overhead
    apart; REAL_BYTES_PER_ROW as a floor where synthetic tables are near empty) times the real rows of its source
    (times how often a view repeats rows); the other files by their natural unit."""
    E = c.E
    S = c.S
    R = REAL
    Gs, Ds, Ls = c.gK, c.D, c.L
    Ms = max(len(S.df("graph/modules.parquet")), 1)
    DRs = len(S.df("tables/drugs.parquet"))
    Ks = int(np.load(S.path("embed/gene_vectors.npy"), mmap_mode="r").shape[1])
    ccs = max(len(c.core[1]["cc_dd"]), 1)
    Gr, Dr, Lr, Mr, DRr, Kr = R["genes"], R["drugdoses"], R["lines"], R["modules"], R["drugs"], R["dims"]
    gd = Gr * Dr / (Gs * Ds)
    arr_scale = {("g", "lfc"): gd, ("g", "z"): gd, ("g", "q_up"): gd, ("g", "q_dn"): gd, ("g", "flag"): gd,
                 ("g", "nl"): gd, ("g", "pat"): Gr * DRr / (Gs * DRs), ("g", "lcen"): Gr * Lr / (Gs * Ls),
                 ("g", "lsc"): Gr * Lr / (Gs * Ls), ("g", "gvec"): Gr * Kr / (Gs * Ks),
                 ("g", "cc"): Gr * 54 / (Gs * ccs), ("g", "cols"): Gr / Gs,
                 ("l", "ms"): Mr * Dr * Lr / (Ms * Ds * Ls), ("m", "ms"): Mr * Dr * Lr / (Ms * Ds * Ls),
                 ("m", "pz"): Mr * Dr / (Ms * Ds)}
    fam_files = {"g": [r for r in c.files("web", "d/g/") if r != "d/g/mod.js"], "l": c.files("web", "d/l/"),
                 "m": c.files("web", "d/m/"), "dg": c.files("web", "d/dg/"), "dr": c.files("web", "d/dr/")}
    kinds = {"g": "gene-bucket", "l": "line", "m": "module", "dg": "dir-groups", "dr": "drug"}
    real_files = {"g": Gr / 16, "l": Lr, "m": Mr, "dg": 250, "dr": DRr}
    srcs = {}
    parts = {}
    for fam, files in fam_files.items():
        ab, tb, rows, empty = {}, {}, {}, {}
        for rel in files:
            _h, a, t = c.shard("web", rel, cache=fam == "g")
            for k, v in a.items():
                ab[k] = ab.get(k, 0) + len(E.shard_text("x", E.encode("x", "r", "k", arrays={k: v})))
            for k, df in t.items():
                if k not in empty:
                    empty[k] = len(E.shard_text("x", E.encode("x", "r", "k", tables={k: df.iloc[:0]})))
                tb[k] = tb.get(k, 0) + len(E.shard_text("x", E.encode("x", "r", "k", tables={k: df}))) - empty[k]
                rows[k] = rows.get(k, 0) + len(df)
        tot = 0.0
        for k, b in ab.items():
            tot += b * arr_scale.get((fam, k), 1.0)
        for k, b in tb.items():
            src = E.TABLE_SOURCES.get((kinds[fam], k))
            if src and src not in srcs:
                srcs[src] = len(S.df(src))
            n_src = srcs.get(src, Gs) if src else Gs
            n_real = R["rows"].get(src, n_src * Gr / Gs) if src else Gr
            rep = rows[k] / max(n_src, 1)                          # how often the view holds each source row
            per = b / rows[k] if rows[k] >= 100 else 0.0
            per = max(per, REAL_BYTES_PER_ROW.get(src, 0.0) * 1.34)
            tot += per * n_real * rep + empty[k] * real_files[fam]
        parts[fam] = tot
    sizes = {}
    for r, _d, fs in os.walk(c.web):
        for f in fs:
            rel = os.path.relpath(os.path.join(r, f), c.web).replace(os.sep, "/")
            if rel.startswith(("d/g/", "d/l/", "d/m/", "d/dg/", "d/dr/")):
                continue
            sizes[rel] = os.path.getsize(os.path.join(r, f))
    scale = {"d/core.js": Dr / Ds * 2, "d/ddarr.js": Dr * Lr / (Ds * Ls), "map/gene_map.html": 25e6 / max(
        sizes.get("map/gene_map.html", 1), 1), "d/docs.js": 1.5, "d/flags.js": 30, "d/sets.js": 1.0,
        "d/groups.js": R["rows"]["direction/groups.parquet"] / max(len(S.df("direction/groups.parquet")), 1)}
    other = 0.0
    for rel, b in sizes.items():
        other += b * scale.get(rel, Gr / Gs)
    parts["other files"] = other + 2.0e6                              # + sets.js (gene sets: none offline)
    return sum(parts.values()), parts


def t_guard(c):
    """--pages-max-mb 1 applies every move, records them and loses nothing (the stage stops, its files are left in
    explorer.tmp, the previous explorer is untouched); a limit between the sizes makes exactly the first move and
    succeeds, with the move in the stamp and core.js."""
    E = c.E
    d = os.path.join(c.work, "guard")
    _copy_out(c.xo, d, with_explorer=True)
    before = json.load(open(os.path.join(d, "explorer", "manifest.json"), encoding="utf-8"))["manifest_sha256"]
    msg = ""
    try:
        E.run(d, pages_max_mb=1)
        stopped = False
    except SystemExit as e:
        stopped, msg = True, str(e)
    tmp = os.path.join(d, "explorer.tmp")
    man = json.load(open(os.path.join(tmp, "manifest.json"), encoding="utf-8"))
    parts = [m["part"] for m in man["moves"]]
    after = json.load(open(os.path.join(d, "explorer", "manifest.json"), encoding="utf-8"))["manifest_sha256"]
    # nothing lost: every moved part is in data w/, and every web and w/ file holds exactly its sources
    X = E.Expect(d)
    probs, n_w = [], 0
    for vol, pre in (("data", "w/"), ("web", "d/l/"), ("web", "d/g/"), ("web", "d/m/")):
        root = os.path.join(tmp, vol)
        for r, _ds, fs in os.walk(os.path.join(root, *pre.split("/"))):
            for f in fs:
                probs += X.check(os.path.join(r, f))
                n_w += vol == "data"
    lost = 0
    for r, _ds, fs in os.walk(os.path.join(tmp, "web", "d", "g")):
        for f in fs:
            h, _a, t = E.read_shard(os.path.join(r, f))
            if h["kind"] == "gene-bucket" and "rel" not in t and "rel" not in (h["meta"].get("moved") or {}):
                lost += 1
    ok1 = stopped and parts == ["l.ms", "g.rel", "m.ms"] and before == after and not probs and lost == 0 and n_w > 0
    # a limit that needs exactly the first move
    first = man["moves"][0]
    web0 = c.stamp["info"]["volumes"]["web"]["bytes"]
    lim = (web0 - first["bytes_freed"] / 2) / 2 ** 20
    _copy_out(c.out, d)
    info = E.run(d, pages_max_mb=lim)
    core = E.read_shard(os.path.join(d, "explorer", "web", "d", "core.js"))[0]["meta"]
    X = E.Expect(d)
    p2 = []
    for vol in ("web", "data"):
        for r, _ds, fs in os.walk(os.path.join(d, "explorer", vol)):
            for f in fs:
                if f.endswith(".js") and f not in ("hosts.js", "probe.js", "app.js"):
                    p2 += X.check(os.path.join(r, f))
    ok2 = [m["part"] for m in info["moves"]] == ["l.ms"] and core["where"] == {"l.ms": "data"} and not p2 \
        and info["volumes"]["web"]["bytes"] <= lim * 2 ** 20
    shutil.rmtree(d, ignore_errors=True)
    return ok1 and ok2, (f"--pages-max-mb 1: stopped {stopped}, moves {parts}, {n_w} data w/ files, previous "
                         f"explorer untouched {before == after}, nothing lost ({len(probs)} differences, {lost} "
                         f"buckets without rel); --pages-max-mb {lim:.2f}: moves {[m['part'] for m in info['moves']]}, "
                         f"core where {core['where']}, every file exact ({len(p2)} differences)"
                         + (f"; {probs[:3]} {p2[:3]}" if probs or p2 else "") + f"; message: {msg[:200]}...")


def t_options(c):
    """--with-line-dd writes data_dd y/ (exact per-line values per drug-dose); --with-pooled-r writes d/pooledr.js."""
    E = c.E
    d = os.path.join(c.work, "opts")
    _copy_out(c.out, d)
    info = E.run(d, line_dd=True, pooled_r=True, data_url="https://raw.githubusercontent.com/o/r-data/main/")
    X = E.Expect(d)
    probs, n = [], 0
    for r, _ds, fs in os.walk(os.path.join(d, "explorer", "data_dd", "y")):
        for f in fs:
            probs += X.check(os.path.join(r, f))
            n += 1
    _h, a, _t = E.read_shard(os.path.join(d, "explorer", "web", "d", "pooledr.js"))
    z = np.load(os.path.join(d, "atlas", "effects", "DD_z.npy"))[:, :c.gK].T
    zq = np.where(np.isfinite(z), np.clip(np.rint(z * 100.0), -32767, 32767), -32768).astype(np.int16)
    hosts = open(os.path.join(d, "explorer", "web", "d", "hosts.js"), encoding="ascii").read()
    ok = n == c.D and not probs and np.array_equal(a["zq"], zq) and "r-data-dd/main/" in hosts \
        and info["volumes"]["data_dd"]["files"] >= c.D
    shutil.rmtree(d, ignore_errors=True)
    return ok, (f"data_dd: {n} y/ files exact ({len(probs)} differences); pooledr.js equals round(100 z); hosts.js "
                f"names the data and data_dd hosts: {hosts.strip()[:160]}")


CHECKS = [("1 exact: pooled values in g/ and p/", t_exact_pooled), ("1 exact: per-line and per-well values in x/",
                                                                     t_exact_lines),
          ("2 flags: every (drug-dose, gene) string", t_flags), ("2 flags: every drug_effects row", t_drug_effects),
          ("2 flags: nl and line_effects counts", t_nl_counts), ("3 records equal their sources", t_records),
          ("4 completeness: stamp row counts", t_complete), ("4 completeness: INVENTORY covers OUT", t_inventory),
          ("5 planted answers", t_planted), ("6 determinism", t_determinism), ("7 sizes and limits", t_sizes),
          ("7 size guard moves and loses nothing", t_guard), ("options: data_dd and pooled r", t_options)]


def check(out, data, report=None, work=None, keep=False):
    """Run every check on OUT (DATA: the synthetic data folder with ground_truth.json). report: run_tests.py's
    check(stage, name, fn); else each result is printed. Returns [(name, PASS / FAIL, detail)]."""
    out = os.path.abspath(out)
    own = work is None
    if work is None:                    # next to OUT: the copies are hard links on the same disk
        os.makedirs(os.path.join(os.path.dirname(out), "explorer_test_work"), exist_ok=True)
        work = tempfile.mkdtemp(prefix="run_", dir=os.path.join(os.path.dirname(out), "explorer_test_work"))
    os.makedirs(work, exist_ok=True)
    results = []

    def run_one(name, fn):
        try:
            ok, detail = fn()
            st = "PASS" if ok else "FAIL"
        except BaseException as e:  # noqa: BLE001  (SystemExit included: a stage that stops is a failure here)
            ok, st, detail = False, "FAIL", f"{type(e).__name__}: {e}\n{traceback.format_exc(limit=4)}"
        results.append((name, st, detail))
        return ok, detail

    def emit(name, fn):
        if report is not None:
            report("explorer", name, lambda: run_one(name, fn))
        else:
            ok, detail = run_one(name, fn)
            print(f"  [{results[-1][1]}] explorer: {name} -- {detail}", flush=True)

    try:
        holder = {}

        def setup():
            holder["c"] = Ctx(out, data, work)
            return True, f"read {holder['c'].root}"
        emit("set-up: read the explorer (or build it in a copy)", setup)
        if "c" in holder:
            for name, fn in CHECKS:
                emit(name, lambda fn=fn: fn(holder["c"]))
    finally:
        if own and not keep:
            shutil.rmtree(work, ignore_errors=True)
            try:
                os.rmdir(os.path.dirname(work))
            except OSError:
                pass
    return results


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", required=True, help="a finished synthetic output folder")
    ap.add_argument("--data", required=True, help="its synthetic data folder (ground_truth.json)")
    ap.add_argument("--work", default=None, help="scratch folder for the stage runs (default: a temporary folder)")
    ap.add_argument("--keep", action="store_true", help="keep the scratch folder")
    a = ap.parse_args()
    res = check(a.out, a.data, work=a.work, keep=a.keep)
    n = {s: sum(r[1] == s for r in res) for s in ("PASS", "FAIL")}
    print(f"\nexplorer: {n['PASS']} passed, {n['FAIL']} failed")
    sys.exit(1 if n["FAIL"] else 0)


if __name__ == "__main__":
    main()
