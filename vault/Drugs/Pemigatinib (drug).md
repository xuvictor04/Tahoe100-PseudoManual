---
drug: "Pemigatinib"
type: "drug"
salt_base: "Pemigatinib"
targets: "FGFR1, FGFR2, FGFR3, FGFR4"
moa_fine: "Other TK inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "5"]
best_dose: "0.05"
max_sig_genes: 17
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Pemigatinib

*Other TK inhibitor (inhibitor/antagonist) · targets: FGFR1, FGFR2, FGFR3, FGFR4 · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 5 µM): 17 / 0; best dose 0.05 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): low dose only (noise?).
> Signature similarity between consecutive doses (low–mid / mid–high): 0.11.
> Flags by dose: - / noisy plate (z scaled).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 01]]:A4 | 15 / 2 | — | -0.30 | +1.0/+1.2/+1.4 | — |
| 5 µM | [[Plate 03]]:A4 | 0 / 0 | — | +0.10 | -1.0/-0.6/-0.6 | noisy plate (z scaled) |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (15 genes, none with an alert; 12 shown): [[MAGI2-AS3]] 1.32× (z +3.4, 2/16 lines), [[DXO]] 1.40× (z +3.3, 7/42 lines), [[NSMF]] 1.34× (z +3.3, 15/46 lines), [[ABT1]] 1.31× (z +3.2, 4/46 lines), [[NBEAP1]] 1.41× (z +3.1, 0/17 lines), [[ZC3H12A]] 1.32× (z +3.1, 4/41 lines), [[EIF2B2]] 1.21× (z +3.0, 7/48 lines), [[PASD1]] 1.84× (z +3.0, 1/2 lines), [[FLT3LG]] 1.41× (z +3.0, 3/37 lines), [[FRG1GP]] 1.48× (z +2.9, 3/12 lines), [[PAF1]] 1.24× (z +2.9, 9/48 lines), [[ZFP36]] 1.40× (z +2.9, 18/45 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (2 genes, none with an alert): [[DYNC1I1]] 0.742× (z -3.6, 2/31 lines), [[ENSG00000291283]] 0.747× (z -3.2, 10/35 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 5 µM | — | — |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 5 µM | [[H4 (line)]] (-3.6) | — |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 5 next most similar without an alert.*

- [[Erdafitinib (drug)]] (+0.74, Other TK inhibitor, ⚠ only 6 significant genes); [[Eplerenone (drug)]] (+0.69, unclear, ⚠ only 4 significant genes); [[Aprepitant (drug)]] (+0.68, unclear); [[Minodronic acid (drug)]] (+0.67, unclear); [[Zileuton (drug)]] (+0.66, unclear, ⚠ only 4 significant genes); [[LY-2584702 (tosylate salt) (drug)]] (+0.64, MTOR inhibitor, ⚠ vector dose flagged: toxic); [[Erythromycin (drug)]] (+0.62, unclear); [[Docetaxel (drug)]] (+0.61, Microtubule inhibitor, ⚠ vector dose flagged: transcription drop; cell-cycle shift); [[XRK3F2 (drug)]] (+0.61, unclear); [[Fumaric acid (drug)]] (+0.59, unclear); [[9-ING-41 (drug)]] (+0.59, GSK3 inhibitor); [[Mozavaptan (drug)]] (+0.56, unclear); [[Silodosin (drug)]] (+0.56, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 8 arrows, 8 of them with an alert ⚠; grade A 0, B 3, C 5.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[LINC02306]] | 5 µM | B | LINC02306 activity lowers the cells' numbers under Pemigatinib 5 µM (makes them more sensitive) | lines that do not express LINC02306 (13) vs lines expressing it (35) | the lines without LINC02306: 1.22× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: KCNMB2, COP1-DT, LINC02398; maybe low, not absent |
| [[ENSG00000251294]] | 5 µM | B | ENSG00000251294 activity lowers the cells' numbers under Pemigatinib 5 µM (makes them more sensitive) | lines that do not express ENSG00000251294 (23) vs lines expressing it (25) | the lines without ENSG00000251294: 1.19× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; also absent: VIPR2, OR3A2, RALYL; maybe low, not absent |
| [[GRIA1]] | 5 µM | B | GRIA1 activity lowers the cells' numbers under Pemigatinib 5 µM (makes them more sensitive) | lines that do not express GRIA1 (17) vs lines expressing it (31) | the lines without GRIA1: 1.17× the cells of the other lines | 0.096 | ⚠ within organs, on part of the lines; also absent: RAMP1, ENSG00000263745, ENSG00000285534; maybe low, not absent |
| [[PMAIP1]] | 5 µM | C | PMAIP1 activity raises the cells' numbers under Pemigatinib 5 µM (protects the cells) | lines that do not express PMAIP1 (4) vs lines expressing it (44) | the lines without PMAIP1: 0.72× the cells of the other lines | 0.033 | ⚠ few lines (4 vs 46); across organs; also absent: DOCK5, STAMBPL1, PERP; maybe low, not absent |
| [[DOCK5]] | 5 µM | C | DOCK5 activity raises the cells' numbers under Pemigatinib 5 µM (protects the cells) | lines that do not express DOCK5 (3) vs lines expressing it (45) | the lines without DOCK5: 0.71× the cells of the other lines | 0.082 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: PMAIP1, FZD6, GCA; maybe low, not absent |
| [[MAP3K5]] | 5 µM | C | MAP3K5 activity raises the cells' numbers under Pemigatinib 5 µM (protects the cells) | lines that do not express MAP3K5 (3) vs lines expressing it (45) | the lines without MAP3K5: 0.70× the cells of the other lines | 0.091 | ⚠ few lines (3 vs 47); across organs; also absent: PFKP, GALNT7, C3orf52 |
| [[HMGA1P4]] | 5 µM | C | HMGA1P4 activity raises the cells' numbers under Pemigatinib 5 µM (protects the cells) | lines that do not express HMGA1P4 (3) vs lines expressing it (45) | the lines without HMGA1P4: 0.73× the cells of the other lines | 0.093 | ⚠ few lines (3 vs 47); across organs; co-occurs with WNK2; also absent: MYD88, CASP8, SP100 |
| [[METTL2A]] | 5 µM | C | METTL2A's natural level raises the cells' numbers under Pemigatinib 5 µM (protects the cells) | METTL2A's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.73 | 0.178 over the table, 0.005 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Pemigatinib"
- `tables/drugdoses.parquet` — dd in 783, 784
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
