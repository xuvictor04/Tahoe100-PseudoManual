# TRIM72 under idarubicin (Tahoe-100M published pseudobulk DE)

Tahoe-100M is single-cell RNA-seq: it has no qPCR Ct values. These files hold Tahoe's own published pseudobulk
DESeq2 tests (idarubicin vs. plate DMSO) for TRIM72, plus a derived **pseudo-ΔΔCt = −log2FoldChange** (qPCR reports
fold change as 2^−ΔΔCt). A negative pseudo-ΔΔCt means TRIM72 is higher under idarubicin. It is computed, not measured.

| File | What it holds |
|---|---|
| `fetch_trim72_idarubicin.py` | Reads `metadata/pseudobulk_differential_expression` remotely from Hugging Face (parquet footers plus the row groups whose `drug` statistics match), keeps TRIM72 × Idarubicin (hydrochloride). No full download needed. |
| `trim72_idarubicin_raw.csv` | All 200 rows as published (50 cell lines; 0.05 and 0.5 µM on one plate each, 5 µM on plates 6 and 14). |
| `TRIM72_idarubicin.csv` | The same rows, trimmed to the useful columns, with `pseudo_ddCt`. |
| `plot_fold_change.py` | Draws `TRIM72_idarubicin_5uM_fold_change.png` from `TRIM72_idarubicin.csv`. |
| `TRIM72_idarubicin_5uM_fold_change.png` | Fold change at 5 µM per cell line and plate, with 95% CI (uncorrected, as published). |

    pip install fsspec aiohttp pyarrow pandas
    python3 fetch_trim72_idarubicin.py trim72_idarubicin_raw.csv    # ~10 min, 1,026 files

## Results

| Dose | Median log2FC | Median pseudo-ΔΔCt | Median baseMean |
|---|---|---|---|
| 0.05 µM | +0.44 | −0.44 | ~4 (barely detected) |
| 0.5 µM | +0.11 | −0.11 | ~5 (barely detected) |
| 5 µM | +2.95 (~7.7×) | −2.95 | ~26 |

- At 5 µM, 46 of 50 lines have TRIM72 significantly up (padj < 0.05) on at least one plate.
- The two 5 µM plates disagree: median log2FC 4.27 on plate 6 vs. 1.47 on plate 14. These numbers are
  **uncorrected** (plate-DMSO and well-position artifacts remain); the direction is consistent, the size is not.
  `tahoe_gene_panel.py` gives corrected effects for TRIM72 on the full download.
- At 0.05 and 0.5 µM TRIM72 is near the detection limit and the tests are mostly noise.
