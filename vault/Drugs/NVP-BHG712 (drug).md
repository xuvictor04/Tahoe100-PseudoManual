---
drug: "NVP-BHG712"
type: "drug"
salt_base: "NVP-BHG712"
targets: "EPHB4"
moa_fine: "unclear"
moa_broad: "inhibitor/antagonist"
approved: "no"
doses: ["0.05", "0.5", "5"]
best_dose: "0.05"
max_sig_genes: 28
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# NVP-BHG712

*unclear (inhibitor/antagonist) · targets: EPHB4 · approved: no*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 28 / 12 / 8; best dose 0.05 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): low dose only (noise?).
> Signature similarity between consecutive doses (low–mid / mid–high): -0.49 / 0.02.
> Flags by dose: - / plate-row cell shift; noisy plate (z scaled) / plate-row cell shift; noisy plate (z scaled).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 01]]:D1 | 14 / 14 | — | +0.33 | -0.8/-1.8/-1.0 | — |
| 0.5 µM | [[Plate 02]]:D1 | 6 / 6 | — | -0.96 | +1.1/+1.0/+1.3 | plate-row cell shift; noisy plate (z scaled) |
| 5 µM | [[Plate 03]]:D1 | 8 / 0 | — | +0.09 | +1.5/+0.8/-0.7 | plate-row cell shift; noisy plate (z scaled) |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (14 genes, none with an alert; 12 shown): [[ACVR2A]] 1.22× (z +3.8, 17/48 lines), [[LINC02458]] 1.46× (z +3.5, 4/46 lines), [[GNA13]] 1.27× (z +3.4, 22/48 lines), [[TEX10]] 1.28× (z +3.3, 21/48 lines), [[FOXO3]] 1.21× (z +3.3, 19/48 lines), [[SEC23B]] 1.24× (z +3.3, 15/48 lines), [[UBOX5]] 1.25× (z +3.3, 12/48 lines), [[MED23]] 1.21× (z +3.1, 14/48 lines), [[CHIC2]] 1.25× (z +3.1, 19/48 lines), [[ZNF410]] 1.28× (z +3.1, 17/48 lines), [[ILKAP]] 1.27× (z +3.1, 17/48 lines), [[CD200R1]] 1.59× (z +3.0, 3/45 lines)

**0.5 µM** (6 genes, none with an alert): [[NEFM]] 2.35× (z +3.8, 0/10 lines), [[IL18R1]] 1.41× (z +3.0, 0/28 lines), [[GABPA]] 1.21× (z +3.0, 7/48 lines), [[COQ10A]] 1.38× (z +2.9, 2/39 lines), [[HNRNPH1]] 1.37× (z +2.8, 32/48 lines), [[AGTR1]] 1.74× (z +2.8, 0/10 lines)

**5 µM** (8 genes, none with an alert): [[MAP2K6]] 1.93× (z +3.1, 2/24 lines), [[CREB5]] 1.39× (z +3.0, 5/33 lines), [[CAT]] 1.41× (z +2.8, 1/46 lines), [[NRG2]] 1.42× (z +2.8, 1/33 lines), [[PIK3R1]] 1.27× (z +2.8, 7/46 lines), [[DIXDC1]] 1.30× (z +2.7, 7/48 lines), [[TM7SF3]] 1.25× (z +2.7, 6/48 lines), [[ALDH7A1]] 1.25× (z +2.7, 1/46 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (14 genes, none with an alert; 12 shown): [[CDIPT]] 0.708× (z -3.9, 16/48 lines), [[SANBR]] 0.798× (z -3.8, 11/48 lines), [[STPG4]] 0.656× (z -3.7, 3/46 lines), [[PDE4C]] 0.642× (z -3.6, 7/43 lines), [[DNAJC22]] 0.744× (z -3.4, 4/38 lines), [[MYD88]] 0.649× (z -3.4, 11/42 lines), [[EBPL]] 0.809× (z -3.3, 8/48 lines), [[CFAP210]] 0.537× (z -3.3, 15/46 lines), [[TRMT1L]] 0.806× (z -3.2, 12/48 lines), [[ANKRD26]] 0.830× (z -3.1, 12/48 lines), [[GALM]] 0.767× (z -3.0, 4/37 lines), [[ENDOD1]] 0.799× (z -2.9, 9/46 lines)

**0.5 µM** (6 genes, none with an alert): [[PPP1R8]] 0.793× (z -3.5, 9/48 lines), [[GFOD2]] 0.806× (z -3.4, 5/48 lines), [[RAB35]] 0.830× (z -3.2, 9/48 lines), [[TPST2]] 0.820× (z -3.2, 7/48 lines), [[PPP6R2]] 0.825× (z -3.1, 6/47 lines), [[TBC1D25]] 0.813× (z -2.8, 10/47 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | [[Module 179]] (+2.9) | [[Module 060]] (-2.2) |
| 0.5 µM | — | — |
| 5 µM | — | — |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | [[SW 1088 (line)]] (2.02), [[H4 (line)]] (1.32), [[Hs 766T (line)]] (1.32), [[NCI-H2030 (line)]] (1.31) · weakest: [[SW48 (line)]] (0.573), [[HT-29 (line)]] (0.584), [[LoVo (line)]] (0.628) |
| 0.5 µM | — | — |
| 5 µM | [[NCI-H661 (line)]] (-3.2) | — |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 4 next most similar without an alert.*

- [[Capivasertib (drug)]] (+0.83, PI3K/AKT inhibitor, ⚠ only 5 significant genes); [[Acetazolamide (drug)]] (+0.67, unclear, ⚠ only 3 significant genes); [[Gallic acid (drug)]] (+0.67, Cyclooxygenase inhibitor); [[Goserelin (acetate) (drug)]] (+0.62, unclear); [[Asciminib (drug)]] (+0.59, Other TK inhibitor); [[Baicalin (drug)]] (+0.57, unclear); [[Indacaterol (maleate) (drug)]] (+0.55, Adrenoceptor agonist, ⚠ only 3 significant genes); [[Delamanid (drug)]] (+0.52, unclear, ⚠ only 6 significant genes); [[Tomivosertib (drug)]] (+0.51, Protein synthesis inhibitor); [[Hexylresorcinol (drug)]] (+0.46, unclear); [[Captopril (drug)]] (+0.46, unclear); [[Pravastatin (sodium) (drug)]] (+0.44, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 53 arrows, 53 of them with an alert ⚠; grade A 0, B 47, C 6. Shown: the 15 strongest; 38 more arrows (38 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[AHR]] | 5 µM | B | AHR activity raises the cells' numbers under NVP-BHG712 5 µM (protects the cells) | lines that do not express AHR (7) vs lines expressing it (41) | the lines without AHR: 0.81× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: ENSG00000283321, VDR, GPR39 |
| [[ENSG00000232884]] | 0.05 µM | B | ENSG00000232884 activity lowers the cells' numbers under NVP-BHG712 0.05 µM (makes them more sensitive) | lines that do not express ENSG00000232884 (12) vs lines expressing it (36) | the lines without ENSG00000232884: 1.24× the cells of the other lines | 0.047 | ⚠ within organs, on part of the lines; also absent: ENSG00000235609, NRIP1, ATXN1; maybe low, not absent |
| [[STON2]] | 0.05 µM | B | STON2 activity lowers the cells' numbers under NVP-BHG712 0.05 µM (makes them more sensitive) | lines that do not express STON2 (19) vs lines expressing it (29) | the lines without STON2: 1.15× the cells of the other lines | 0.050 | ⚠ within organs, on part of the lines; also absent: FRK, RASSF6, AQP3 |
| [[SLC27A2]] | 5 µM | B | SLC27A2 activity raises the cells' numbers under NVP-BHG712 5 µM (protects the cells) | lines that do not express SLC27A2 (19) vs lines expressing it (29) | the lines without SLC27A2: 0.95× the cells of the other lines | 0.056 | ⚠ within organs, on part of the lines; also absent: ICA1, BTC, ENSG00000288656 |
| [[ASPH]] | 5 µM | B | ASPH activity raises the cells' numbers under NVP-BHG712 5 µM (protects the cells) | lines that do not express ASPH (5) vs lines expressing it (43) | the lines without ASPH: 0.74× the cells of the other lines | 0.065 | ⚠ within organs, on part of the lines; also absent: HIPK2, EPS8, SCML1; maybe low, not absent |
| [[ENSG00000246225]] | 5 µM | B | ENSG00000246225 activity raises the cells' numbers under NVP-BHG712 5 µM (protects the cells) | lines that do not express ENSG00000246225 (7) vs lines expressing it (41) | the lines without ENSG00000246225: 0.82× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: PTPRK, SVIP, MAST4; maybe low, not absent |
| [[MYO1B]] | 5 µM | B | MYO1B activity raises the cells' numbers under NVP-BHG712 5 µM (protects the cells) | lines that do not express MYO1B (7) vs lines expressing it (41) | the lines without MYO1B: 0.88× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: TBC1D8B, AHR, FAM241A |
| [[PSD3]] | 5 µM | B | PSD3 activity raises the cells' numbers under NVP-BHG712 5 µM (protects the cells) | lines that do not express PSD3 (13) vs lines expressing it (35) | the lines without PSD3: 0.83× the cells of the other lines | 0.075 | ⚠ within organs, on part of the lines; also absent: ENSG00000253557, LINC00511, ZFPM2-AS1; maybe low, not absent |
| [[PTGFRN]] | 5 µM | B | PTGFRN activity raises the cells' numbers under NVP-BHG712 5 µM (protects the cells) | lines that do not express PTGFRN (8) vs lines expressing it (40) | the lines without PTGFRN: 0.84× the cells of the other lines | 0.075 | ⚠ within organs, on part of the lines; also absent: MLLT3, FHIT |
| [[SLC2A9]] | 5 µM | B | SLC2A9 activity raises the cells' numbers under NVP-BHG712 5 µM (protects the cells) | lines that do not express SLC2A9 (6) vs lines expressing it (42) | the lines without SLC2A9: 0.82× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; also absent: VDR, SEMA4G, TBC1D8B; maybe low, not absent |
| [[ENSG00000283321]] | 5 µM | B | ENSG00000283321 activity raises the cells' numbers under NVP-BHG712 5 µM (protects the cells) | lines that do not express ENSG00000283321 (7) vs lines expressing it (41) | the lines without ENSG00000283321: 0.86× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; co-occurs with WNK2; also absent: AHR, PSMB8, CXCL2 |
| [[GPR39]] | 0.05 µM | B | GPR39 activity lowers the cells' numbers under NVP-BHG712 0.05 µM (makes them more sensitive) | lines that do not express GPR39 (11) vs lines expressing it (37) | the lines without GPR39: 1.17× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; also absent: MET, AHR, ABCC3 |
| [[ENSG00000283240]] | 0.05 µM | B | ENSG00000283240 activity lowers the cells' numbers under NVP-BHG712 0.05 µM (makes them more sensitive) | lines that do not express ENSG00000283240 (19) vs lines expressing it (29) | the lines without ENSG00000283240: 1.17× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; also absent: MGST1, IL1R2, STON2 |
| [[TNFRSF11A]] | 5 µM | B | TNFRSF11A activity raises the cells' numbers under NVP-BHG712 5 µM (protects the cells) | lines that do not express TNFRSF11A (9) vs lines expressing it (39) | the lines without TNFRSF11A: 0.90× the cells of the other lines | 0.078 | ⚠ within organs, on part of the lines; also absent: PTGER4; maybe low, not absent |
| [[MPZL3]] | 0.05 µM | B | MPZL3 activity lowers the cells' numbers under NVP-BHG712 0.05 µM (makes them more sensitive) | lines that do not express MPZL3 (25) vs lines expressing it (23) | the lines without MPZL3: 1.19× the cells of the other lines | 0.079 | ⚠ within organs, on part of the lines; also absent: RNF39, MYO5B, CDH1 |

### Its targets: what acting on them probably does

*Drug-target arrows of the compound classes it belongs to (compounds sharing a listed target and mechanism; one molecule counts once, under all its names): the target → a gene whose level those compounds move. A row that names several targets is one test: the compounds share them all, and any of them could be the cause. 1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Its target | Gene it moves | This drug | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|---|
| [[EPHB4]] | [[RAB35]] | moves it that way too | B | EPHB4 activity raises RAB35's level | compounds that target EPHB4: 2 of 3 lower it (NG25, NVP-BHG712) | 67% of the class's compounds vs 1.1% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

## Data

- `tables/drugs.parquet` — drug == "NVP-BHG712"
- `tables/drugdoses.parquet` — dd in 702, 703, 704
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
