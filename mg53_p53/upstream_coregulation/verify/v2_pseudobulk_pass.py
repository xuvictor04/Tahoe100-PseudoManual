#!/usr/bin/env python3
"""Independent read of the atlas pseudobulk (read-only) for the adversarial check of the baseline (b) and locus (c)
claims. Does NOT use the analysis's cache/.

    python3 mg53_p53/upstream_coregulation/verify/v2_pseudobulk_pass.py      (~10-20 min, < 3 GB RAM)

Writes out/v2_cache/:
  plate_line_sums.npz   per plate x line summed counts of every gene and summed total counts over
                        (all) every non-failed well with >= 30 cells of the line (no activity filter),
                        (dmso) DMSO wells only
  plate_line_quiet.npz  as (all) but drug wells of drug-doses with n_sig_genes >= 1000 left out (= the analysis's rule)
  wells_p6_p14.npz      plates 6 and 14: per line the MEDIAN CPM over the plate's non-failed drug wells (>= 30 cells;
                        the atlas's baseline definition), and full count profiles of the idarubicin / homoharringtonine
                        5 uM wells
"""
import glob
import json
import os
import time

import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out", "v2_cache")
os.makedirs(OUT, exist_ok=True)
DATA = "/home/user/tahoe_data"
PB = os.path.join(DATA, "atlas", "pseudobulk")
FXD = os.path.join(DATA, "atlas", "effects")
TARGET = {"smp_2010": "Idarubicin 5 (plate6)", "smp_2778": "Idarubicin 5 (plate14)",
          "smp_2047": "Homoharringtonine 5 (plate6)", "smp_2815": "Homoharringtonine 5 (plate14)"}


def log(*a):
    print(time.strftime("%H:%M:%S"), *a, flush=True)


def main():
    lines = pd.read_csv(os.path.join(FXD, "lines.csv"), dtype={"id": str})
    lid = lines["id"].astype(str).tolist() if "id" in lines else lines["cell_line_id"].astype(str).tolist()
    sm = pd.read_csv(os.path.join(DATA, "atlas", "sample_map.csv"), dtype={"sample": str})
    plates = sorted(sm["plate"].unique(), key=lambda p: int(p.replace("plate", "")))
    failed = set(pd.read_csv(os.path.join(FXD, "failed_wells.csv"), dtype={"sample": str})["sample"])
    wells = pd.read_csv(os.path.join(FXD, "wells.csv"), dtype={"sample": str})
    dd = pd.read_csv(os.path.join(FXD, "drugdose.csv"))
    nsig = wells["drugdose_row"].map(lambda r: dd["n_sig_genes"].iloc[int(r)] if r >= 0 else np.nan)
    active = set(wells.loc[(~wells["is_dmso"].astype(bool)) & (nsig >= 1000), "sample"])
    plate_of = dict(zip(sm["sample"], sm["plate"]))
    dmso = set(sm.loc[sm["is_dmso"].astype(bool), "sample"])
    parts = []
    for m in sorted(glob.glob(os.path.join(PB, "group*_profiles.csv"))):
        t = pd.read_csv(m, dtype={"sample": str, "cell_line_id": str})
        t["file"] = m.replace("_profiles.csv", ".npy")
        parts.append(t)
    prof = pd.concat(parts, ignore_index=True)
    prof = prof[prof["cell_line_id"].isin(lid)].copy()
    prof["plate"] = prof["sample"].map(plate_of)
    print("profiles without plate:", prof["plate"].isna().sum())
    pi = {p: i for i, p in enumerate(plates)}
    li = {l: i for i, l in enumerate(lid)}
    prof["pi"] = prof["plate"].map(pi)
    prof["li"] = prof["cell_line_id"].map(li)
    # n_cells per (sample, line) after summing split rows: the >= 30 cell rule applies to the summed profile
    ncs = prof.groupby(["sample", "cell_line_id"])["n_cells"].sum()
    prof["n_cells_sum"] = [ncs[(s, l)] for s, l in zip(prof["sample"], prof["cell_line_id"])]
    prof["ok30"] = prof["n_cells_sum"] >= 30
    prof["is_failed"] = prof["sample"].isin(failed)
    prof["is_dmso"] = prof["sample"].isin(dmso)
    prof["is_active"] = prof["sample"].isin(active)
    G = int(np.load(prof["file"].iloc[0], mmap_mode="r").shape[1])
    P, L = len(plates), len(lid)
    acc = {k: np.zeros((P * L, G)) for k in ("all", "dmso", "quiet")}
    tot = {k: np.zeros(P * L) for k in ("all", "dmso", "quiet")}
    for f, g in prof.groupby("file"):
        g = g.sort_values("row")
        arr = np.load(f, mmap_mode="r")
        log("reading", os.path.basename(f), len(g))
        for s0 in range(0, len(g), 400):
            gg = g.iloc[s0:s0 + 400]
            sub = np.asarray(arr[gg["row"].to_numpy()], dtype=np.float64)
            k = (gg["pi"].to_numpy() * L + gg["li"].to_numpy())
            base = (~gg["is_failed"] & gg["ok30"]).to_numpy()
            masks = {"all": base, "dmso": base & gg["is_dmso"].to_numpy(),
                     "quiet": base & ~gg["is_active"].to_numpy()}
            for nm, m in masks.items():
                if not m.any():
                    continue
                kk = k[m]
                o = np.argsort(kk, kind="stable")
                ks = kk[o]
                st = np.flatnonzero(np.r_[True, ks[1:] != ks[:-1]])
                acc[nm][ks[st]] += np.add.reduceat(sub[m][o], st, axis=0)
                tot[nm][ks[st]] += np.add.reduceat(gg["total_counts"].to_numpy()[m][o], st)
            del sub
    for nm in acc:
        fn = "plate_line_quiet.npz" if nm == "quiet" else f"plate_line_sums_{nm}.npz"
        np.savez(os.path.join(OUT, fn), counts=acc[nm].reshape(P, L, G).astype(np.float32),
                 total=tot[nm].reshape(P, L), plates=np.array(plates), lines=np.array(lid))
    del acc
    log("sums written")
    # plates 6 and 14: per-line median CPM over the plate's non-failed drug wells (>= 30 cells), target profiles
    med = np.full((2, L, G), np.nan, dtype=np.float32)
    nmed = np.zeros((2, L), dtype=int)
    tg = list(TARGET)
    tcounts = np.zeros((len(tg), L, G), dtype=np.float32)
    ttot = np.zeros((len(tg), L))
    tcells = np.zeros((len(tg), L))
    for a, p in enumerate(("plate6", "plate14")):
        gp = prof[prof["plate"] == p]
        for l_ in range(L):
            gl = gp[gp["li"] == l_]
            rows = {}
            for f, h in gl.groupby("file"):
                arr = np.load(f, mmap_mode="r")
                hh = h.sort_values("row")
                x = np.asarray(arr[hh["row"].to_numpy()], dtype=np.float64)
                for s, v, tc, nc in zip(hh["sample"], x, hh["total_counts"], hh["n_cells"]):
                    if s in rows:
                        rows[s] = (rows[s][0] + v, rows[s][1] + tc, rows[s][2] + nc)
                    else:
                        rows[s] = (v, tc, nc)
            use = [s for s, (v, tc, nc) in rows.items() if s not in failed and s not in dmso and nc >= 30
                   and s not in TARGET]
            if use:
                C = np.stack([rows[s][0] / rows[s][1] * 1e6 for s in use])
                med[a, l_] = np.median(C, axis=0)
                nmed[a, l_] = len(use)
            for j, s in enumerate(tg):
                if s in rows:
                    tcounts[j, l_] = rows[s][0]
                    ttot[j, l_] = rows[s][1]
                    tcells[j, l_] = rows[s][2]
        log("median baseline done", p)
    np.savez(os.path.join(OUT, "wells_p6_p14.npz"), median_cpm=med, n_wells_median=nmed, target_counts=tcounts,
             target_total=ttot, target_cells=tcells, targets=np.array(tg), plates=np.array(["plate6", "plate14"]),
             lines=np.array(lid))
    with open(os.path.join(OUT, "done.json"), "w") as fh:
        json.dump({"plates": plates, "n_active_wells_left_out_of_quiet": len(active), "targets": TARGET}, fh)
    log("done")


if __name__ == "__main__":
    main()
