---
drug: "Sivelestat (sodium tetrahydrate)"
type: "drug"
salt_base: "Sivelestat"
targets: "ELANE"
moa_fine: "unclear"
moa_broad: "inhibitor/antagonist"
approved: "no"
doses: ["0.05", "0.5", "5"]
best_dose: "0.5"
max_sig_genes: 70
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Sivelestat (sodium tetrahydrate)

*unclear (inhibitor/antagonist) · targets: ELANE · approved: no*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 13 / 70 / 51; best dose 0.5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.05 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.35 / -0.33.
> Flags by dose: - / - / plate-row cell shift.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 07]]:A1 | 2 / 11 | — | +0.52 | +1.3/+0.6/+0.7 | — |
| 0.5 µM | [[Plate 08]]:A1 | 58 / 12 | — | -0.33 | -0.2/+1.0/+1.0 | — |
| 5 µM | [[Plate 09]]:A1 | 23 / 28 | — | +1.20 | -0.5/-1.8/-2.3 | plate-row cell shift |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (2 genes, none with an alert): [[CFAP210]] 1.89× (z +3.2, 20/45 lines), [[OSR2]] 1.64× (z +3.0, 7/38 lines)

**0.5 µM** (58 genes, none with an alert; 12 shown): [[ENSG00000256625]] 1.58× (z +4.4, 8/37 lines), [[GRHL2]] 1.33× (z +4.2, 0/14 lines), [[ESRP1]] 1.37× (z +4.1, 0/17 lines), [[LINC01019]] 1.35× (z +4.1, 7/45 lines), [[MAL2]] 1.24× (z +3.9, 0/17 lines), [[PDE4A]] 1.27× (z +3.8, 7/41 lines), [[TWIST1]] 1.48× (z +3.7, 4/22 lines), [[SLC6A15]] 1.36× (z +3.7, 0/15 lines), [[ENSG00000242828]] 1.61× (z +3.6, 0/9 lines), [[SLCO1B3]] 1.21× (z +3.6, 0/20 lines), [[TOMM20L-DT]] 1.44× (z +3.6, 3/42 lines), [[SKAP1]] 1.27× (z +3.5, 0/14 lines)

**5 µM** (23 genes, none with an alert; 12 shown): [[ARHGEF10]] 1.24× (z +4.1, 21/41 lines), [[FBXO16]] 1.33× (z +3.6, 10/39 lines), [[DTX2P1]] 1.58× (z +3.6, 15/46 lines), [[GALNS]] 1.25× (z +3.5, 10/48 lines), [[ASMTL]] 1.21× (z +3.5, 8/48 lines), [[NPIPB14P]] 1.27× (z +3.5, 12/48 lines), [[PLCG2]] 1.24× (z +3.5, 5/38 lines), [[NR2F2-AS1]] 1.34× (z +3.4, 20/41 lines), [[MEPCE]] 1.34× (z +3.4, 15/48 lines), [[BTN3A1]] 1.25× (z +3.3, 6/47 lines), [[LINGO2]] 1.22× (z +3.3, 6/22 lines), [[TMEM45A]] 1.32× (z +3.3, 9/35 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (11 genes, none with an alert): [[ZNF212]] 0.757× (z -4.1, 21/48 lines), [[ZNF2]] 0.771× (z -4.0, 3/46 lines), [[CDC42EP2]] 0.564× (z -3.8, 8/37 lines), [[ENSG00000270019]] 0.633× (z -3.7, 13/41 lines), [[ENSG00000280878]] 0.707× (z -3.6, 7/43 lines), [[RN7SL76P]] 0.629× (z -3.5, 7/40 lines), [[BMS1P23]] 0.702× (z -3.4, 7/40 lines), [[SLC45A3]] 0.671× (z -3.3, 6/39 lines), [[ENSG00000230021]] 0.778× (z -3.0, 14/48 lines), [[ENSG00000225313]] 0.785× (z -3.0, 3/43 lines), [[JAKMIP3]] 0.795× (z -2.8, 3/35 lines)

**0.5 µM** (12 genes, none with an alert): [[SLC4A3]] 0.699× (z -3.8, 8/36 lines), [[SHC1]] 0.737× (z -3.7, 28/47 lines), [[IGSF9B]] 0.764× (z -3.5, 9/30 lines), [[BRD9]] 0.830× (z -3.4, 18/48 lines), [[IDUA]] 0.713× (z -3.3, 11/42 lines), [[H2BC8]] 0.531× (z -3.3, 12/31 lines), [[POMK]] 0.798× (z -3.3, 14/46 lines), [[MYEOV]] 0.754× (z -3.2, 14/29 lines), [[NUP210]] 0.821× (z -3.1, 13/35 lines), [[ZNF320]] 0.830× (z -3.1, 5/36 lines), [[FAT1]] 0.823× (z -3.0, 21/45 lines), [[ZNF469]] 0.746× (z -3.0, 8/27 lines)

**5 µM** (28 genes, none with an alert; 12 shown): [[LRRFIP2]] 0.792× (z -4.4, 29/49 lines), [[DYNC1LI1]] 0.790× (z -4.4, 24/49 lines), [[RAD21]] 0.795× (z -4.1, 31/49 lines), [[IDH3A]] 0.800× (z -4.1, 12/47 lines), [[VPS26A]] 0.822× (z -4.1, 23/49 lines), [[EIF4E]] 0.760× (z -4.0, 25/49 lines), [[CMTM6]] 0.791× (z -3.9, 23/48 lines), [[SNRPG]] 0.772× (z -3.9, 14/47 lines), [[ATG3]] 0.772× (z -3.9, 25/49 lines), [[FDX1]] 0.787× (z -3.9, 14/47 lines), [[PLEKHF2]] 0.796× (z -3.7, 12/49 lines), [[FGFR1OP2]] 0.823× (z -3.7, 19/49 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | [[Module 054]] (+2.8), [[Module 043]] (+2.6), [[Module 048]] (+2.4) | [[Module 020]] (-2.4), [[Module 025]] (-2.4) |
| 5 µM | [[Module 170]] (+2.7) | [[Module 182]] (-3.2) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | [[AN3 CA (line)]] (1.87), [[C-33 A (line)]] (1.51), [[SNU-1 (line)]] (1.45), [[SW48 (line)]] (1.44) · weakest: [[SK-MEL-2 (line)]] (0.309), [[J82 (line)]] (0.418), [[NCI-H1573 (line)]] (0.487) |
| 5 µM | — | [[NCI-H2122 (line)]] (1.93), [[CHP-212 (line)]] (1.63), [[AsPC-1 (line)]] (1.62), [[NCI-H1792 (line)]] (1.58) · weakest: [[KATO III (line)]] (0.537), [[BT-474 (line)]] (0.546), [[HCT15 (line)]] (0.561) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 3 next most similar without an alert.*

- [[Tranilast (drug)]] (+0.86, unclear, ⚠ only 6 significant genes); [[Decitabine (drug)]] (+0.83, DNA methyltransferase inhibitor); [[Bendamustine (drug)]] (+0.81, DNA synthesis/repair inhibitor); [[Docetaxel (Trihydrate) (drug)]] (+0.79, Microtubule inhibitor); [[Azithromycin (hydrate) (drug)]] (+0.77, unclear); [[Darolutamide (drug)]] (+0.75, Androgen receptor antagonist, ⚠ only 5 significant genes); [[Tetracycline (hydrochloride) (drug)]] (+0.75, unclear, ⚠ only 6 significant genes); [[Silodosin (drug)]] (+0.74, unclear); [[Methylprednisolone succinate (drug)]] (+0.73, Glucocorticoid receptor agonist); [[Bicalutamide (drug)]] (+0.73, Androgen receptor antagonist); [[18β-Glycyrrhetinic acid (drug)]] (+0.72, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 81 arrows, 81 of them with an alert ⚠; grade A 0, B 65, C 16. Shown: the 15 strongest; 66 more arrows (66 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[DAPP1]] | 5 µM | B | DAPP1 activity lowers the cells' numbers under Sivelestat (sodium tetrahydrate) 5 µM (makes them more sensitive) | lines that do not express DAPP1 (39) vs lines expressing it (9) | the lines without DAPP1: 1.28× the cells of the other lines | 0.036 | ⚠ within organs, on part of the lines; also absent: SLC6A14, CEACAM6, MUC5B |
| [[ATP2C2]] | 5 µM | B | ATP2C2 activity lowers the cells' numbers under Sivelestat (sodium tetrahydrate) 5 µM (makes them more sensitive) | lines that do not express ATP2C2 (32) vs lines expressing it (16) | the lines without ATP2C2: 1.23× the cells of the other lines | 0.036 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, GRHL2, ST14 |
| [[GRHL2]], [[LINC02967]] | 5 µM | B | GRHL2, LINC02967 activity lowers the cells' numbers under Sivelestat (sodium tetrahydrate) 5 µM (makes them more sensitive) | lines that do not express GRHL2, LINC02967 (34) vs lines expressing them (14) | the lines without GRHL2, LINC02967: 1.23× the cells of the other lines | 0.037 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM30B, RAB25, TMPRSS4; co-absent genes |
| [[TMEM30B]] | 5 µM | B | TMEM30B activity lowers the cells' numbers under Sivelestat (sodium tetrahydrate) 5 µM (makes them more sensitive) | lines that do not express TMEM30B (35) vs lines expressing it (13) | the lines without TMEM30B: 1.24× the cells of the other lines | 0.038 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, ANKRD22, RAB25 |
| [[TMEM125]] | 5 µM | B | TMEM125 activity lowers the cells' numbers under Sivelestat (sodium tetrahydrate) 5 µM (makes them more sensitive) | lines that do not express TMEM125 (33) vs lines expressing it (15) | the lines without TMEM125: 1.22× the cells of the other lines | 0.041 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, ATP2C2, ST14 |
| [[OVOL1]], [[TMPRSS4]] | 5 µM | B | OVOL1, TMPRSS4 activity lowers the cells' numbers under Sivelestat (sodium tetrahydrate) 5 µM (makes them more sensitive) | lines that do not express OVOL1, TMPRSS4 (33) vs lines expressing them (15) | the lines without OVOL1, TMPRSS4: 1.23× the cells of the other lines | 0.047 | ⚠ within organs, on part of the lines; also absent: GRHL2, ST14, TMEM30B; co-absent genes |
| [[MAL2]] | 5 µM | B | MAL2 activity lowers the cells' numbers under Sivelestat (sodium tetrahydrate) 5 µM (makes them more sensitive) | lines that do not express MAL2 (31) vs lines expressing it (17) | the lines without MAL2: 1.19× the cells of the other lines | 0.047 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: RAB25, TMEM125, CDH1 |
| [[SLC5A1]] | 5 µM | B | SLC5A1 activity lowers the cells' numbers under Sivelestat (sodium tetrahydrate) 5 µM (makes them more sensitive) | lines that do not express SLC5A1 (36) vs lines expressing it (12) | the lines without SLC5A1: 1.26× the cells of the other lines | 0.050 | ⚠ within organs, on part of the lines; also absent: TMEM30B, TMPRSS2, TMEM125 |
| [[FMNL1-DT]] | 0.5 µM | B | FMNL1-DT activity raises the cells' numbers under Sivelestat (sodium tetrahydrate) 0.5 µM (protects the cells) | lines that do not express FMNL1-DT (23) vs lines expressing it (25) | the lines without FMNL1-DT: 0.83× the cells of the other lines | 0.050 | ⚠ within organs, on part of the lines; also absent: CACNG6, FMNL1, SLFN11; maybe low, not absent |
| [[SPOCK1]] | 0.05 µM | B | SPOCK1 activity raises the cells' numbers under Sivelestat (sodium tetrahydrate) 0.05 µM (protects the cells) | lines that do not express SPOCK1 (29) vs lines expressing it (19) | the lines without SPOCK1: 0.84× the cells of the other lines | 0.050 | ⚠ within organs, on part of the lines; also absent: SRGN, ENSG00000280241, TEX41 |
| [[SLC6A14]] | 5 µM | B | SLC6A14 activity lowers the cells' numbers under Sivelestat (sodium tetrahydrate) 5 µM (makes them more sensitive) | lines that do not express SLC6A14 (39) vs lines expressing it (9) | the lines without SLC6A14: 1.23× the cells of the other lines | 0.052 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DAPP1, MUC5AC, ST6GALNAC1 |
| [[TMPRSS2]] | 5 µM | B | TMPRSS2 activity lowers the cells' numbers under Sivelestat (sodium tetrahydrate) 5 µM (makes them more sensitive) | lines that do not express TMPRSS2 (35) vs lines expressing it (13) | the lines without TMPRSS2: 1.26× the cells of the other lines | 0.056 | ⚠ within organs, on part of the lines; also absent: SLC5A1, ARHGEF38, ITGB6 |
| [[ANKRD22]] | 5 µM | B | ANKRD22 activity lowers the cells' numbers under Sivelestat (sodium tetrahydrate) 5 µM (makes them more sensitive) | lines that do not express ANKRD22 (34) vs lines expressing it (14) | the lines without ANKRD22: 1.24× the cells of the other lines | 0.056 | ⚠ within organs, on part of the lines; also absent: TMEM30B, GRHL2, RAB25 |
| [[COL17A1]] | 5 µM | B | COL17A1 activity lowers the cells' numbers under Sivelestat (sodium tetrahydrate) 5 µM (makes them more sensitive) | lines that do not express COL17A1 (34) vs lines expressing it (14) | the lines without COL17A1: 1.24× the cells of the other lines | 0.056 | ⚠ within organs, on part of the lines; also absent: SERPINB5, GJB3, FGFBP1 |
| [[DCLK2]] | 5 µM | B | DCLK2 activity raises the cells' numbers under Sivelestat (sodium tetrahydrate) 5 µM (protects the cells) | lines that do not express DCLK2 (17) vs lines expressing it (31) | the lines without DCLK2: 0.87× the cells of the other lines | 0.056 | ⚠ within organs, on part of the lines; also absent: LINC03041, HECW2, AFF3 |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Sivelestat (sodium tetrahydrate)"
- `tables/drugdoses.parquet` — dd in 955, 956, 957
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
