#!/usr/bin/env python3
"""Plot TRIM72 (MG53) fold change at 5 uM idarubicin, per cell line and plate, from TRIM72_idarubicin.csv.

    python3 plot_fold_change.py        # writes TRIM72_idarubicin_5uM_fold_change.png next to this script
"""
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
INK, MUTED, GRID, SURFACE = "#0b0b0b", "#52514e", "#e4e3df", "#fcfcfb"
PLATES = {6: ("#2a78d6", "o", -0.17), 14: ("#eb6834", "D", 0.17)}   # colour, marker, row offset

d = pd.read_csv(os.path.join(HERE, "TRIM72_idarubicin.csv"))
d = d[(d.concentration == 5) & d.log2FoldChange.notna()].copy()
d["sig"] = d.padj < 0.05
order = d.groupby("Cell_Name_Vevo").log2FoldChange.mean().sort_values().index
y = {line: i for i, line in enumerate(order)}

plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 9, "text.color": INK,
                     "axes.labelcolor": INK, "xtick.color": MUTED, "ytick.color": INK})
fig, ax = plt.subplots(figsize=(8.5, 13), facecolor=SURFACE)
ax.set_facecolor(SURFACE)

for plate, (col, mk, off) in PLATES.items():
    p = d[d.plate == plate]
    yy = p.Cell_Name_Vevo.map(y) + off
    ax.errorbar(p.log2FoldChange, yy, xerr=1.96 * p.lfcSE, fmt="none", ecolor=col, elinewidth=1.2, alpha=0.45,
                zorder=2)
    for sig, face in ((True, col), (False, SURFACE)):
        q = p[p.sig == sig]
        ax.scatter(q.log2FoldChange, q.Cell_Name_Vevo.map(y) + off, s=42, marker=mk, facecolor=face,
                   edgecolor=col, linewidth=1.5, zorder=3)

# right-hand column: fold change per plate, in text ink
xr = 10.6
ax.text(xr, len(order) - 0.1, "plate 6   plate 14", ha="left", va="bottom", color=MUTED, fontsize=8)
for line, i in y.items():
    fc = {pl: d[(d.Cell_Name_Vevo == line) & (d.plate == pl)].log2FoldChange for pl in PLATES}
    txt = ["{:>6}".format(f"{2 ** s.iloc[0]:.1f}×" if len(s) else "–") for s in fc.values()]
    ax.text(xr, i, "   ".join(txt), ha="left", va="center", family="DejaVu Sans Mono", fontsize=8, color=INK)

ax.axvline(0, color=MUTED, linewidth=1, zorder=1)
ticks = [-4, -2, 0, 2, 4, 6, 8, 10]
ax.set_xticks(ticks, [f"{2 ** t:g}×" if t >= 0 else f"1/{2 ** -t:g}×" for t in ticks])
ax.set_xlim(-4.5, 10.4)
ax.set_yticks(range(len(order)), order)
ax.set_ylim(-0.8, len(order) - 0.2)
ax.grid(axis="x", color=GRID, linewidth=0.8, zorder=0)
for s in ("top", "right", "left"):
    ax.spines[s].set_visible(False)
ax.spines["bottom"].set_color(GRID)
ax.tick_params(axis="y", length=0)
ax.set_xlabel("TRIM72 (MG53) fold change vs. plate DMSO, log2 scale (bars: 95% CI)")

h = [plt.Line2D([], [], marker=mk, color=col, markerfacecolor=col, linestyle="", markersize=7,
                label=f"plate {pl}") for pl, (col, mk, _) in PLATES.items()]
h.append(plt.Line2D([], [], marker="o", color=MUTED, markerfacecolor=SURFACE, linestyle="", markersize=7,
                    label="hollow: not significant (padj ≥ 0.05)"))
fig.legend(handles=h, loc="upper left", bbox_to_anchor=(0.02, 0.928), ncol=3, frameon=False, fontsize=8.5)

n_up = d[d.sig & (d.log2FoldChange > 0)].Cell_Name_Vevo.nunique()
fig.suptitle("TRIM72 (MG53) mRNA rises with 5 µM idarubicin in most cancer cell lines", x=0.02, ha="left",
             fontsize=12.5, fontweight="bold")
fig.text(0.02, 0.962, f"Tahoe-100M published pseudobulk DESeq2, uncorrected. Significantly up on at least\none plate in "
         f"{n_up} of {d.Cell_Name_Vevo.nunique()} lines. Plate 6 runs consistently higher than plate 14 "
         f"(median {2 ** d[d.plate == 6].log2FoldChange.median():.1f}× vs "
         f"{2 ** d[d.plate == 14].log2FoldChange.median():.1f}×),\nso read the size of the effect as a range.",
         ha="left", va="top", color=MUTED, fontsize=8.5)
fig.subplots_adjust(left=0.14, right=0.78, top=0.895, bottom=0.05)
out = os.path.join(HERE, "TRIM72_idarubicin_5uM_fold_change.png")
fig.savefig(out, dpi=160, facecolor=SURFACE)
print("wrote", out)
