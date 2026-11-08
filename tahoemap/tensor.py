"""tensor - the per-cell-line layer the atlas collapsed: every gene's corrected effect in every well x cell line, and
every drug-dose x cell line fold change, stored gene-major so that one gene is one contiguous read.

The atlas (atlas_core.cmd_effects) computes, per plate, each profile's residual r1 = log2 CPM minus the line's median
over the plate's drug wells, minus the profile's composition shift; it then keeps only the median over cell lines (W1),
corrects that for the well position (W2 = W1 - eff) and pools wells into drug-doses (DD_lfc, DD_z). This stage
re-derives r1 per plate from the same build with the same ported functions, re-derives the position effect eff from
the saved W1 exactly as the atlas did (two passes, clean donors), and keeps the per-line values:

    R[g, w, l]       = r1[w, l, g] - eff[w, g]                         corrected log2 effect, well w, line l
    DDL_lfc[g, d, l] = mean of R[g, w, l] over drug-dose d's used wells  log2 fold change vs the line's own baseline
    DDL_z[g, d, l]   = Stouffer over those wells of (R - c[g,l]) / s[g,l] / plate factor[g, w]

where c, s are the robust centre and scale (median, 1.4826 MAD) of R over the reference wells (drug wells on reliable
plates) for that gene and line, and the plate factor is the atlas's own per-gene z divisor (plate_scale_gene.npy).

What is NaN (never 0), and why. Besides what the atlas leaves out (profiles with fewer than min_cells cells, and lines
outside the atlas's expr_mask, i.e. below 25% of the median line), two kinds of value are set to NaN here, because the
per-line values cannot be read there although the atlas's median over lines could:
  - ambient-only lines: line_measured[l, g] = expr_mask[l, g] AND line_cpm[l, g] >= AMB_FRAC x the gene's pooled CPM
    (genes.csv pooled_cpm). Every well holds ambient RNA, the average of all its cells, so a line that does not make
    the gene still reads about the ambient fraction (~0.1) of the pooled level. For a gene that fewer than half of the
    lines express, the median line is such a line and expr_mask lets the rest through; their "responses" are then
    the well's ambient RNA moving (other lines' responses, cell loss), not the line's own. Those (line, gene) pairs
    are NaN in R, DDL_lfc and DDL_z; line_measured.npy says which pairs are measured.
  - low-count profiles: a profile's value is NaN when its expected count line_cpm[l, g] x profile UMI / 1e6 < E_MIN.
    With ~0-1 expected counts the log2 CPM is the pseudocount and a single read; a line depleted by the drug (few
    cells, so few UMI) then shows large false rises of low-level genes, and the line's spread s (estimated from
    deeper wells) makes their z over-confident.
Both masks are applied after the W1 self-check below, so the check still compares like with like.

It checks itself as it goes: per plate, the median over lines of r1 must reproduce the saved W1, and the
re-derived eff must reproduce W1 - W2 wherever both are finite (both to float32 precision); the run stops otherwise.

Outputs in <out>/tensor/ (the row/column order of every index is that of <out>/atlas/effects/*.csv):
    R.npy            genes x wells x lines      (optional, --no-well-tensor drops it)
    DDL_lfc.npy      genes x drug-doses x lines (float16)
    DDL_z.npy        genes x drug-doses x lines (float16)
    line_measured.npy  lines x genes (bool): the line truly expresses the gene (see above); False -> NaN values
    line_center.npy, line_scale.npy  genes x lines: c and s above
    plate_base.npy   plates x lines x genes: each line's baseline (median log2 CPM over the plate's drug wells)
    well_counts.npy  wells x genes: raw UMI counts summed over the well's cell lines (the raw layer, per well)
    well_umi.npy, well_line_cells.npy, well_line_umi.npy   wells, wells x lines: totals and cells
    info.json        sizes, the self-check deviations, amb_frac, e_min and how many values each mask removed
"""

import json
import os
import time

import numpy as np

from . import atlas_core as A
from .common import log, open_memmap, read_effects_index, remove_file, replace_file, save_npy, stamp_stage

VERSION = 2

AMB_FRAC = 0.25      # a line truly expresses a gene at >= this fraction of the gene's pooled CPM (ambient reads ~0.1)
E_MIN = 2.0          # a profile's value needs >= this many expected counts (line_cpm x profile UMI / 1e6)


def measured_mask(expr_mask, line_cpm, pooled_cpm):
    """lines x genes (gene columns only): the line truly expresses the gene - the atlas's expr_mask AND a level of
    at least AMB_FRAC x the gene's pooled CPM (below it the line reads only the wells' ambient RNA)."""
    lc = np.asarray(line_cpm, dtype=np.float64)
    pc = np.asarray(pooled_cpm, dtype=np.float64)
    return np.asarray(expr_mask, dtype=bool) & (lc >= AMB_FRAC * pc[None, :])


def _position_effect(W1, wells, unreliable, gK):
    """eff exactly as atlas_core.cmd_effects computes it: leave-drug-out pass 1, then pass 2 with clean donors."""
    drug = ~wells["is_dmso"].to_numpy(dtype=bool)
    slot = wells["slot"].to_numpy(dtype=float)
    dname = wells["drug"].to_numpy(dtype=object)
    reliable = ~wells["plate"].isin(unreliable).to_numpy()
    ref = drug & reliable if (drug & reliable).any() else drug
    grp, _gtab, gkeys = A.plate_groups(wells, drug)
    rel_plates = set(wells["plate"]) - set(unreliable)
    gcols = np.arange(gK)

    def per_well(fac):
        return np.where(grp >= 0, fac[np.maximum(grp, 0)], 1.0).astype(np.float32)

    eff, n_total, _ = A.loo_effect(W1, slot, dname, drug)
    W2 = W1 - eff
    c, s = A.robust_cols(W2, ref)
    _raw1, fac1, _, _ = A.plate_factors(W2, c, drug, grp, gkeys, rel_plates, gcols)
    f1 = per_well(fac1)
    clean = np.abs((W2 - c) / (s * f1[:, None])) < A.POS_CLEAN_Z
    eff, _, n_clean = A.loo_effect(W1, slot, dname, drug, clean=clean)
    return eff, grp, ref, drug


def run(out, dtype="float32", keep_well=True, chunk=384, check=True):
    """out = the tahoemap output folder (atlas in out/atlas). Writes out/tensor/."""
    t0 = time.time()
    atl = os.path.join(out, "atlas")
    fxd = os.path.join(atl, "effects")
    td = os.path.join(out, "tensor")
    os.makedirs(td, exist_ok=True)
    ix = read_effects_index(fxd)
    genes, wells, dd, lines = ix["genes"], ix["wells"], ix["drugdose"], ix["lines"]
    info = ix["info"]
    gK = int((genes["kind"] == "gene").sum())
    N, Dn, L = len(wells), len(dd), len(lines)
    unreliable = list(info.get("unreliable_plates", []))
    A.MIN_CELLS = int(info.get("min_cells", A.MIN_CELLS))        # log_cpm reads the module global, as in effects
    log(f"Tensor: {gK:,} genes x {N:,} wells x {L} lines (drug-doses: {Dn:,}); min cells {A.MIN_CELLS}, "
        f"unreliable plates: {', '.join(unreliable) or 'none'}")

    W1 = np.load(os.path.join(fxd, "W1.npy"))
    W2 = np.load(os.path.join(fxd, "W2.npy"))
    expr_mask = np.load(os.path.join(fxd, "expr_mask.npy"))
    line_cpm = np.load(os.path.join(fxd, "line_cpm.npy"))
    FG = np.load(os.path.join(fxd, "plate_scale_gene.npy"))
    with open(os.path.join(fxd, "modules.json"), encoding="utf-8") as fh:
        modules = {k: np.asarray(v, dtype=np.int64) for k, v in json.load(fh).items()}
    keep = genes["token"].to_numpy()[:gK].astype(np.int64)
    comp_mask = expr_mask[:, :gK] & (line_cpm[:, :gK] >= A.COMP_MIN_CPM)
    measured = measured_mask(expr_mask[:, :gK], line_cpm[:, :gK], genes["pooled_cpm"].to_numpy()[:gK])
    n_amb = int((expr_mask[:, :gK] & ~measured).sum())
    lcpm = np.asarray(line_cpm[:, :gK], dtype=np.float32)
    log(f"  ambient-only (line, gene) pairs: {n_amb:,} of {int(expr_mask[:, :gK].sum()):,} the atlas counts as "
        f"expressed (line level < {AMB_FRAC:g} x the gene's pooled CPM) -> NaN; profiles with < {E_MIN:g} expected "
        "counts -> NaN")

    log("  position effect: re-deriving the atlas's two-pass leave-drug-out correction from W1 ...")
    eff, grp, ref, is_drug = _position_effect(W1, wells, unreliable, gK)
    fin = np.isfinite(W1) & np.isfinite(W2)
    dev = float(np.nanmax(np.abs((W1 - eff)[fin] - W2[fin]))) if fin.any() else 0.0
    log(f"    check: W1 - eff vs the saved W2: max |difference| {dev:.2e}")
    if check and dev > 1e-4:
        raise SystemExit(f"tensor: the re-derived position effect does not reproduce W2 (max diff {dev:.3g}); "
                         "the effects folder and this code disagree - rerun 'effects'")
    del W2

    prof = A.load_profiles(os.path.join(atl, "pseudobulk"))
    prof = prof[prof["sample"].isin(set(wells["sample"]))]
    prof = prof[prof["cell_line_id"].isin(set(lines["cell_line_id"]))].reset_index(drop=True)
    line_ids = list(lines["cell_line_id"])
    plates = list(ix["plates"]["plate"])

    R = open_memmap(os.path.join(td, "R.npy.tmp"), (gK, N, L), np.float16 if dtype == "float16" else np.float32)
    well_counts = np.zeros((N, gK), dtype=np.float32)
    well_umi = np.zeros(N)
    wl_cells = np.zeros((N, L), dtype=np.float32)
    wl_umi = np.zeros((N, L), dtype=np.float32)
    plate_base = np.full((len(plates), L, gK), np.nan, dtype=np.float32)
    worst = 0.0
    n_low = 0
    for pi, p in enumerate(plates):
        rows = np.flatnonzero(wells["plate"].to_numpy() == p)
        if not rows.size:
            continue
        smp_ = wells.iloc[rows].reset_index(drop=True)
        counts, tot, nc, _ng, r1, base = A.plate_residuals(prof, smp_, line_ids, keep, modules, expr_mask)
        shift = A.composition_shift(r1, comp_mask)
        r1 -= shift[:, :, None]
        if check:
            cnt = np.isfinite(r1).sum(axis=1)
            w1 = np.nanmedian(r1, axis=1)
            w1[cnt < A.MIN_LINES] = np.nan
            a, b = w1, W1[rows]
            both = np.isfinite(a) & np.isfinite(b)
            if (np.isfinite(a) != np.isfinite(b)).any():
                raise SystemExit(f"tensor: plate {p}: which values are measured differs from the saved W1")
            d = float(np.max(np.abs(a[both] - b[both]))) if both.any() else 0.0
            worst = max(worst, d)
            if d > 1e-4:
                raise SystemExit(f"tensor: plate {p}: the per-line residuals do not reproduce W1 (max diff {d:.3g})")
        r2 = r1[:, :, :gK] - eff[rows][:, None, :gK]
        # the per-line masks (module docstring), after the W1 check: ambient-only lines, then low expected counts
        r2[:, ~measured] = np.nan
        cpm_min = np.where(tot > 0, E_MIN * 1e6 / np.maximum(tot, 1.0), np.inf).astype(np.float32)   # lowest CPM kept
        low = (lcpm[None, :, :] < cpm_min[:, :, None]) & np.isfinite(r2)
        n_low += int(low.sum())
        r2[low] = np.nan
        del low
        if np.all(np.diff(rows) == 1):                     # a plate's wells are contiguous in the atlas order
            R[:, rows[0]:rows[-1] + 1, :] = r2.transpose(2, 0, 1).astype(R.dtype)
        else:
            for j, w in enumerate(rows):
                R[:, w, :] = r2[j].T.astype(R.dtype)
        well_counts[rows] = counts[:, :, :gK].sum(axis=1)
        well_umi[rows] = tot.sum(axis=1)
        wl_cells[rows] = nc
        wl_umi[rows] = tot
        plate_base[pi] = base[:, :gK]
        log(f"  {p}: {rows.size} wells written" + (f" (reproduces W1: max diff {d:.1e})" if check else ""))
        del counts, r1, r2
    R.flush()

    log("  per-line centre and scale, z, and drug-dose pooling (gene chunks) ...")
    import scipy.sparse as sp
    used = wells["used_in_drugdose"].to_numpy(dtype=bool)
    ddr = wells["drugdose_row"].to_numpy(dtype=int)
    m = used & (ddr >= 0)
    agg = sp.csr_matrix((np.ones(int(m.sum()), dtype=np.float32), (ddr[m], np.flatnonzero(m))), shape=(Dn, N))
    fw = np.ones((N, gK), dtype=np.float32)                    # each well's per-gene plate factor
    g_ok = grp >= 0
    fw[g_ok] = FG[grp[g_ok]][:, :gK]
    DDL_lfc = open_memmap(os.path.join(td, "DDL_lfc.npy.tmp"), (gK, Dn, L), np.float16)
    DDL_z = open_memmap(os.path.join(td, "DDL_z.npy.tmp"), (gK, Dn, L), np.float16)
    centre = np.full((gK, L), np.nan, dtype=np.float32)
    scale = np.full((gK, L), np.nan, dtype=np.float32)
    refw = np.flatnonzero(ref)
    for g0 in range(0, gK, chunk):
        g1 = min(gK, g0 + chunk)
        # a copy, not a view: no view of the R memmap may outlive the loop, or Windows refuses the rename / delete
        X = np.array(R[g0:g1], dtype=np.float32)                        # cg x N x L
        sub = X[:, refw, :]
        c = np.nanmedian(sub, axis=1)
        s = 1.4826 * np.nanmedian(np.abs(sub - c[:, None, :]), axis=1)
        sd = np.nanstd(sub, axis=1)
        s = np.where((s > 0) & np.isfinite(s), s, np.where(sd > 0, sd, np.nan))
        centre[g0:g1], scale[g0:g1] = c, s
        Z = (X - c[:, None, :]) / s[:, None, :] / fw[:, g0:g1].T[:, :, None]
        cg = g1 - g0
        Xf = np.nan_to_num(X).transpose(1, 0, 2).reshape(N, cg * L)
        Ff = np.isfinite(X).transpose(1, 0, 2).reshape(N, cg * L).astype(np.float32)
        Zf = np.nan_to_num(Z).transpose(1, 0, 2).reshape(N, cg * L)
        Fz = np.isfinite(Z).transpose(1, 0, 2).reshape(N, cg * L).astype(np.float32)
        n_x = agg @ Ff
        n_z = agg @ Fz
        with np.errstate(invalid="ignore", divide="ignore"):
            lfc = np.where(n_x > 0, (agg @ Xf) / np.maximum(n_x, 1), np.nan)
            zz = np.where(n_z > 0, (agg @ Zf) / np.sqrt(np.maximum(n_z, 1)), np.nan)
        DDL_lfc[g0:g1] = lfc.reshape(Dn, cg, L).transpose(1, 0, 2).astype(np.float16)
        DDL_z[g0:g1] = np.clip(zz, -6e4, 6e4).reshape(Dn, cg, L).transpose(1, 0, 2).astype(np.float16)
        if g0 // chunk % 10 == 0:
            log(f"    genes {g0:,}-{g1:,} of {gK:,} ({(time.time() - t0) / 60:.1f} min)")
    DDL_lfc.flush()
    DDL_z.flush()
    del R, DDL_lfc, DDL_z                       # close the memmaps before the files are renamed or removed
    for name in ("DDL_lfc", "DDL_z", "R"):
        tmp = os.path.join(td, f"{name}.npy.tmp")
        if name == "R" and not keep_well:
            os.remove(tmp)
            final = os.path.join(td, "R.npy")
            if os.path.exists(final):          # an earlier run's R.npy would not match this run's DDL_*
                remove_file(final)             # (Windows: a file in use cannot be removed - common.FileInUse)
            continue
        replace_file(tmp, os.path.join(td, f"{name}.npy"))
    for name, arr in [("line_measured", measured), ("line_center", centre), ("line_scale", scale),
                      ("plate_base", plate_base),
                      ("well_counts", well_counts), ("well_umi", well_umi.astype(np.float64)),
                      ("well_line_cells", wl_cells), ("well_line_umi", wl_umi)]:
        save_npy(os.path.join(td, f"{name}.npy"), arr)
    meta = {"version": VERSION, "genes": gK, "wells": N, "drugdoses": Dn, "lines": L, "plates": plates,
            "R_dtype": dtype if keep_well else None, "layout": "gene-major: R[g, w, l], DDL_*[g, d, l]",
            "min_cells": A.MIN_CELLS, "unreliable_plates": unreliable, "amb_frac": AMB_FRAC, "e_min": E_MIN,
            "n_measured_line_gene_pairs": int(measured.sum()), "n_ambient_line_gene_pairs": n_amb,
            "n_low_count_values": n_low, "check_W1_max_diff": worst, "check_W2_max_diff": dev,
            "minutes": round((time.time() - t0) / 60, 2)}
    with open(os.path.join(td, "info.json"), "w", encoding="utf-8") as fh:
        json.dump(meta, fh, indent=1)
    stamp_stage(out, "tensor", VERSION, meta)
    log(f"Tensor done: {gK:,} genes x {Dn:,} drug-doses x {L} lines -> {td} ({meta['minutes']} min)")
    return meta

