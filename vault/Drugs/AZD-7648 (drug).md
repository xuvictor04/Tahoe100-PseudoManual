---
drug: "AZD-7648"
type: "drug"
salt_base: "AZD-7648"
targets: "PRKDC"
moa_fine: "DNA synthesis/repair inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "no"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 196
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# AZD-7648

*DNA synthesis/repair inhibitor (inhibitor/antagonist) · targets: PRKDC · approved: no*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 0 / 72 / 196; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): -0.25 / 0.77.
> Flags by dose: - / low cells (technical?); noisy plate (z scaled) / noisy plate (z scaled).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 01]]:G8 | 0 / 0 | — | +0.26 | +0.5/-0.0/-1.0 | — |
| 0.5 µM | [[Plate 02]]:G8 | 62 / 10 | — | -1.25 | +1.1/+1.7/+1.4 | low cells (technical?); noisy plate (z scaled) |
| 5 µM | [[Plate 03]]:G8 | 93 / 103 | — | -0.44 | +0.8/+0.9/+0.8 | noisy plate (z scaled) |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (62 genes, none with an alert; 12 shown): [[EIF2AK1]] 1.53× (z +4.3, 39/48 lines), [[CYP1B1-AS1]] 2.01× (z +4.0, 9/31 lines), [[FGF9]] 1.94× (z +3.9, 7/14 lines), [[TMEM44-AS1]] 1.64× (z +3.6, 2/34 lines), [[MAPK4]] 1.97× (z +3.6, 0/10 lines), [[RMDN2-AS1]] 2.64× (z +3.6, 9/22 lines), [[ENSG00000227400]] 1.78× (z +3.6, 4/17 lines), [[CYP1B1]] 2.96× (z +3.5, 11/19 lines), [[E2F7]] 1.31× (z +3.5, 16/43 lines), [[YEATS4]] 1.33× (z +3.5, 10/48 lines), [[PDAP1]] 1.35× (z +3.5, 25/48 lines), [[HNRNPH1]] 1.47× (z +3.5, 40/48 lines)

**5 µM** (93 genes, none with an alert; 12 shown): [[CYP1B1]] 6.48× (z +6.4, 17/18 lines), [[EIF2AK1]] 1.78× (z +5.4, 43/48 lines), [[NFE2L2]] 1.43× (z +5.1, 30/48 lines), [[CYP1B1-AS1]] 2.98× (z +5.1, 16/23 lines), [[AKR1C1]] 2.61× (z +5.0, 12/21 lines), [[RMDN2-AS1]] 3.36× (z +4.6, 13/16 lines), [[PIR]] 1.86× (z +4.5, 16/36 lines), [[NQO1]] 2.38× (z +4.5, 33/42 lines), [[UGT1A6]] 2.17× (z +4.3, 7/12 lines), [[MIR181A1HG]] 1.73× (z +4.3, 23/41 lines), [[TRIM16L-1]] 2.18× (z +4.3, 12/35 lines), [[AJUBA]] 1.90× (z +4.3, 9/41 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (10 genes, none with an alert): [[ARFGEF3]] 0.786× (z -3.3, 20/42 lines), [[PLBD2]] 0.790× (z -3.3, 12/48 lines), [[ENSG00000285589]] 0.643× (z -3.2, 9/43 lines), [[EFTUD2]] 0.818× (z -3.1, 12/48 lines), [[ENSG00000267698]] 0.739× (z -3.0, 12/44 lines), [[TOR1AIP1]] 0.790× (z -3.0, 10/48 lines), [[C3orf52]] 0.696× (z -2.9, 11/42 lines), [[STAM2]] 0.788× (z -2.9, 7/48 lines), [[FGD6]] 0.812× (z -2.8, 10/36 lines), [[TVP23C-CDRT4]] 0.801× (z -2.7, 3/46 lines)

**5 µM** (103 genes, none with an alert; 12 shown): [[NAV2]] 0.610× (z -4.3, 18/31 lines), [[MYEOV]] 0.483× (z -4.3, 12/28 lines), [[CBFB]] 0.727× (z -4.3, 21/48 lines), [[FMNL2]] 0.715× (z -4.1, 24/46 lines), [[MCTP1]] 0.574× (z -4.0, 21/35 lines), [[SPRY4]] 0.401× (z -3.8, 22/47 lines), [[ARID3B]] 0.607× (z -3.8, 21/47 lines), [[RGS17]] 0.562× (z -3.8, 16/32 lines), [[PPARD]] 0.639× (z -3.8, 25/46 lines), [[CLN8]] 0.672× (z -3.7, 13/44 lines), [[SPRY4-AS1]] 0.503× (z -3.7, 25/44 lines), [[BACE2]] 0.708× (z -3.7, 20/38 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | — | [[Module 077]] (-2.0), [[Module 174]] (-2.0) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | [[NCI-H661 (line)]] (1.50), [[HT-29 (line)]] (1.24), [[NCI-H23 (line)]] (1.21), [[HOP62 (line)]] (1.20) · weakest: [[AN3 CA (line)]] (0.344), [[SK-MEL-2 (line)]] (0.623), [[hTERT-HPNE (line)]] (0.728) |
| 5 µM | [[C32 (line)]] (-6.1), [[SK-MEL-2 (line)]] (-4.2), [[CHP-212 (line)]] (-3.8), [[COLO 205 (line)]] (-3.5) | [[AsPC-1 (line)]] (1.54), [[HOP62 (line)]] (1.32), [[NCI-H1573 (line)]] (1.29), [[SW 1271 (line)]] (1.25) · weakest: [[NCI-H661 (line)]] (0.500), [[AN3 CA (line)]] (0.568), [[A-172 (line)]] (0.571) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar.*

- [[Capmatinib (drug)]] (+0.86, EGFR/ERBB inhibitor); [[Elimusertib hydrochloride (drug)]] (+0.79, unclear); [[Trametinib (DMSO_TF solvate) (drug)]] (+0.77, MEK inhibitor); [[Alpelisib (drug)]] (+0.75, PI3K/AKT inhibitor); [[Binimetinib (drug)]] (+0.75, MEK inhibitor); [[Cobimetinib (drug)]] (+0.74, MEK inhibitor); [[DT-061 (drug)]] (+0.73, unclear); [[LJI308 (drug)]] (+0.71, Other MAPK inhibitor)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 5 arrows, 5 of them with an alert ⚠; grade A 0, B 0, C 5.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[SDC3]] | 5 µM | C | SDC3 activity raises the cells' numbers under AZD-7648 5 µM (protects the cells) | lines that do not express SDC3 (4) vs lines expressing it (44) | the lines without SDC3: 0.66× the cells of the other lines | 0.028 | ⚠ few lines (4 vs 46); across organs |
| [[LINC02068]] | 5 µM | C | LINC02068 activity raises the cells' numbers under AZD-7648 5 µM (protects the cells) | lines that do not express LINC02068 (3) vs lines expressing it (45) | the lines without LINC02068: 0.62× the cells of the other lines | 0.028 | ⚠ few lines (3 vs 47); across organs; also absent: TRIB3; maybe low, not absent |
| [[CDR2L]] | 5 µM | C | CDR2L activity raises the cells' numbers under AZD-7648 5 µM (protects the cells) | lines that do not express CDR2L (4) vs lines expressing it (44) | the lines without CDR2L: 0.68× the cells of the other lines | 0.039 | ⚠ few lines (4 vs 46); tissue-confounded; across organs; also absent: MTARC2, LRP5, HACD1; maybe low, not absent |
| [[NPHS1]] | 5 µM | C | NPHS1 activity raises the cells' numbers under AZD-7648 5 µM (protects the cells) | lines that do not express NPHS1 (4) vs lines expressing it (44) | the lines without NPHS1: 0.68× the cells of the other lines | 0.068 | ⚠ few lines (4 vs 46); across organs; co-occurs with CTNNB1; also absent: FSD1L, MYO5A, DPF1; maybe low, not absent |
| [[TRIB3]] | 5 µM | C | TRIB3 activity raises the cells' numbers under AZD-7648 5 µM (protects the cells) | lines that do not express TRIB3 (3) vs lines expressing it (45) | the lines without TRIB3: 0.62× the cells of the other lines | 0.073 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: ARHGAP27, KIAA1522, ALOXE3; maybe low, not absent |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "AZD-7648"
- `tables/drugdoses.parquet` — dd in 30, 31, 32
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
