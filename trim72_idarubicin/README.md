# TRIM72 under idarubicin (Tahoe-100M)

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

## Corrected results (method v3), 5 µM

The numbers below use the repo's own corrections, the same code as `tahoe_gene_panel.py analyze`:
- the baseline is the median of the plate's drug wells for the same cell line;
- a composition shift per well and line is taken from the computed atlas;
- a two-pass leave-drug-out correction removes well-position effects;
- failed wells and unreliable plates are left out;
- lines that do not express the gene are left out.

The full dataset was streamed from Hugging Face through the repo's atlas build and gene-panel extract, then
`tahoe_atlas.py effects` and `tahoe_gene_panel.py extract` ran on it (95,624,334 cells, 1,344 wells, 50 lines, the same as
the authors' full run). Files are in `corrected/`:

| File | What it holds |
|---|---|
| `TRIM72_idarubicin_5uM_per_line_corrected.csv` | One row per cell line: corrected log2 fold change (mean of the two 5 µM wells), each plate alone, per-line z, up/down calls, untreated level. |
| `TRIM72_idarubicin_5uM_per_well_line.csv` | Each correction step per well and line: log2 CPM, plate baseline residual, composition shift, position effect, result. |
| `TRIM72_idarubicin_by_dose_corrected.csv` | All three doses pooled over lines: the row `tahoe_gene_panel.py analyze` writes for TRIM72 (fold change, z, FDR, flags). |
| `run_notes.txt` | Expressed threshold, ambient RNA, plate factors, wells used. |
| `mg53_p53/setup/stream_build.py` (moved there) | Streams the dataset through the repo's build and extract a few files at a time (`plates`, `stream`, `finish`). |
| `trim72_ida_per_line.py` | Runs the panel's setup and `expression_effects` for TRIM72 and writes the three tables. |

Checks: four independent checks agreed with these tables.
- A from-scratch recomputation matched to about 1e-15.
- A method audit found the per-line values equal the method's internal per-line table.
- Cell numbers matched Tahoe's published counts in 100 of 100 rows.
- A skeptic review (its findings are in the caveats below).

The atlas look-up (`tahoe_atlas.py lookup gene TRIM72`) gives the same 12.2x and ranks it the strongest TRIM72 increase
of all 1,132 drug-doses.

**Pooled over lines** (the panel's TRIM72 row):

| Dose | Fold change | z | FDR | Lines up |
|---|---|---|---|---|
| 0.05 µM (1 well) | 1.9× | 2.9 | 0.09 | 9 of 47 |
| 0.5 µM (1 well) | 2.2× | 3.4 | 0.02 | 13 of 47 |
| 5 µM (2 wells) | 12.2× | 15.9 | 4e-54 | 47 of 48 |

**Per cell line at 5 µM.** "Fold change, corrected" is the geometric mean of the two replicate wells (plates 6 and 14,
both at C12). "Up" means per-line z > 2 and fold change > 1.2x.

| Cell line | Tissue | Untreated TRIM72 (CPM, DMSO) | Fold change, corrected | Plate 6 | Plate 14 | Up on both plates | Note |
|---|---|---|---|---|---|---|---|
| MIA PaCa-2 | Pancreas | 3.8 | 43.4× | 151.0× | 12.5× | yes |  |
| A549 | Lung | 2.0 | 29.0× | 48.7× | 17.3× | yes |  |
| A-172 | CNS/Brain | 4.3 | 25.5× | 88.1× | 7.4× | yes |  |
| AsPC-1 | Pancreas | 4.2 | 25.4× | 58.0× | 11.1× | yes |  |
| NCI-H460 | Lung | 1.9 | 24.8× | 39.7× | 15.6× | yes |  |
| NCI-H2347 | Lung | 1.1 | 24.5× | 54.8× | 10.9× | yes |  |
| Panc 03.27 | Pancreas | 1.9 | 21.6× | 35.9× | 13.0× | yes |  |
| Hs 766T | Pancreas | 2.2 | 21.3× | 43.3× | 10.5× | yes |  |
| SW1417 | Bowel | 1.3 | 20.3× | 31.4× | 13.1× | yes |  |
| SNU-1 | Esophagus/Stomach | 2.9 | 20.0× | 59.2× | 6.8× | yes |  |
| C32 | Skin | 5.6 | 19.2× | 58.1× | 6.4× | yes |  |
| HS-578T | Breast | 2.2 | 19.0× | 34.0× | 10.6× | yes |  |
| CFPAC-1 | Pancreas | 2.5 | 18.7× | 40.9× | 8.6× | yes |  |
| SNU-423 | Liver | 2.8 | 17.8× | 39.9× | 8.0× | yes |  |
| PANC-1 | Pancreas | 1.4 | 17.5× | 28.9× | 10.6× | yes |  |
| KATO III | Esophagus/Stomach | 2.4 | 16.8× | 26.5× | 10.7× | yes |  |
| HOP62 | Lung | 6.5 | 16.2× | 38.0× | 6.9× | yes |  |
| NCI-H1792 | Lung | 1.8 | 15.3× | 33.2× | 7.1× | yes |  |
| CHP-212 | Peripheral Nervous System | 2.7 | 14.6× | 47.0× | 4.5× | yes |  |
| COLO 205 | Bowel | 5.0 | 14.4× | 32.4× | 6.4× | yes |  |
| SW 1271 | Lung | 7.1 | 13.7× | 23.6× | 8.0× | yes |  |
| SW480 | Bowel | 2.3 | 13.7× | 17.3× | 10.9× | yes |  |
| LS 180 | Bowel | 1.3 | 12.3× | 18.7× | 8.1× | yes |  |
| HT-29 | Bowel | 3.6 | 12.1× | 13.9× | 10.6× | yes |  |
| J82 | Bladder/Urinary Tract | 6.2 | 12.1× | 42.2× | 3.5× | yes |  |
| hTERT-HPNE | Pancreas | 10.8 | 12.0× | 28.5× | 5.0× | yes |  |
| RKO | Bowel | 10.6 | 11.6× | 29.6× | 4.5× | yes |  |
| SK-MEL-2 | Skin | 2.8 | 10.5× | 14.9× | 7.4× | yes |  |
| SW48 | Bowel | 14.4 | 10.1× | 23.7× | 4.3× | yes |  |
| RPMI-7951 | Skin | 5.5 | 9.7× | 17.7× | 5.3× | yes |  |
| LOX-IMVI | Skin | 8.7 | 9.5× | 24.0× | 3.8× | yes |  |
| SW 900 | Lung | 15.9 | 9.4× | 22.3× | 4.0× | yes |  |
| BT-474 | Breast | 14.2 | 9.2× | 16.7× | 5.1× | yes |  |
| HepG2/C3A | Liver | 13.2 | 9.2× | 25.0× | 3.4× | yes |  |
| NCI-H23 | Lung | 6.5 | 8.6× | 18.6× | 4.0× | yes |  |
| LoVo | Bowel | 12.3 | 7.6× | 15.9× | 3.6× | yes |  |
| SW 1088 | CNS/Brain | 10.2 | 6.9× | 12.8× | 3.7× | yes |  |
| A498 | Kidney | 9.4 | 6.8× | 20.3× | 2.3× | no | up on plate 14 too, but below the line z cutoff |
| HCT15 | Bowel | 19.3 | 6.2× | 14.7× | 2.6× | yes |  |
| HEC-1-A | Uterus | 21.5 | 6.0× | 12.7× | 2.9× | yes |  |
| AN3 CA | Uterus | 9.6 | 4.8× | 10.1× | 2.3× | no | up on plate 14 too, but below the line z cutoff |
| H4 | CNS/Brain | 21.0 | 4.8× | 11.7× | 2.0× | no | up on plate 14 too, but below the line z cutoff |
| NCI-H1573 | Lung | 23.5 | 4.1× | 7.5× | 2.3× | no | up on plate 14 too, but below the line z cutoff |
| NCI-H2030 | Lung | 17.1 | 3.7× | 6.0× | 2.3× | yes |  |
| C-33 A | Cervix | 23.5 | 3.7× | 6.7× | 2.0× | no | up on plate 14 too, but below the line z cutoff |
| SHP-77 | Lung | 7.6 | 3.3× | 4.5× | 2.5× | yes |  |
| NCI-H2122 | Lung | 13.9 | 2.1× | – | 2.1× | – | plate 14 only; 2 reads in 31 cells: weak |
| A-427 | Lung | 6.9 | 0.2× | – | 0.2× | – | plate 14 only (0 reads in 54 cells); its plate-6 well (29 cells, < 30) points up: not credible |
| NCI-H596 | Lung | 12.1 | – | – | – | – | < 30 cells in both 5 µM wells: no estimate |
| NCI-H661 | Lung | 0.9 | – | – | – | – | not expressed (0.94 CPM, below 1.0): left out by the method |

**How to read it**
- **Direction: TRIM72 rises.** 46 of 46 lines are up on plate 6, 42 of 48 on plate 14, and 41 of the 46 lines measured on both plates are
  up on both. The 5 lines up on plate 6 only are still 2.0-2.3x up on plate 14, but below the per-line z cutoff. This holds with
  a DMSO baseline instead (8.2x pooled, uncorrected), with no pseudocount, and after removing the extra ambient RNA of the dying 5 µM wells.
- **Size: a range, not one number.** TRIM72's untreated level is about 10x lower on plates 4-13 (median line 0.5-1.5 CPM)
  than on plates 1-3 and 14 (about 10-12 CPM), the largest plate-6 vs plate-14 baseline gap of any expressed gene. The idarubicin
  wells read about 40-55 CPM on both plates. So the fold change is about 26x against plate 6's baseline and about 6x against
  plate 14's (per-line medians). The 12x is their geometric mean, so expect roughly 5x to 25x. No v3 flag or plate factor
  covers this batch effect.
- **Weak calls.** A-427 'down' rests on one well with 0 reads in 54 cells (its sub-threshold plate-6 well points up).
  NCI-H2122 'up' rests on 2 reads in 31 cells. Read both as no estimate.
- **Not specific.** 5 µM idarubicin is cytotoxic (cells about 0.8 log2 lower than the plate's typical well; cell-cycle shift) and changes
  about 11,000 genes. TRIM72 ranks about 40th by fold change. Other drugs at 5 µM raise TRIM72 too: homoharringtonine 10.3x, auranofin 6.6x,
  dinaciclib 5.6x, and the anthracyclines epirubicin 4.5x and doxorubicin 3.0x; mitoxantrone 2.0x and topotecan 2.6x. At 0.05 and 0.5 µM
  the effect is about 2x, from single wells.
- **Scope.** mRNA, 24 h, cancer cell lines in which TRIM72 is low. This says nothing about MG53 protein or about muscle/heart cells.
