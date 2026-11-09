---
drug: "EX229"
type: "drug"
salt_base: "EX229"
targets: "PRKAA1"
moa_fine: "unclear"
moa_broad: "activator/agonist"
approved: "no"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 2133
tags: ["drug", "moa/activator_agonist"]
generated_by: "tahoemap"
---

# EX229

*unclear (activator/agonist) · targets: PRKAA1 · approved: no*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 543 / 605 / 2133; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.05 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.67 / 0.74.
> Flags by dose: - / plate-row cell shift; noisy plate (z scaled) / noisy plate (z scaled).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 01]]:E7 | 172 / 371 | — | -0.35 | +1.3/+0.1/+1.0 | — |
| 0.5 µM | [[Plate 02]]:E7 | 246 / 359 | — | -0.16 | +0.5/-0.5/+1.6 | plate-row cell shift; noisy plate (z scaled) |
| 5 µM | [[Plate 03]]:E7 | 1,011 / 1,122 | — | -0.03 | -0.7/-3.1/+0.8 | noisy plate (z scaled) |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (172 genes, none with an alert; 12 shown): [[CLCN5]] 1.33× (z +5.6, 16/47 lines), [[TM4SF19]] 1.50× (z +5.2, 15/28 lines), [[POLR3G]] 1.38× (z +5.1, 23/45 lines), [[CRYM]] 1.72× (z +5.0, 21/35 lines), [[KIF21A]] 1.25× (z +4.8, 27/46 lines), [[ZPR1]] 1.38× (z +4.7, 19/48 lines), [[NOP2]] 1.38× (z +4.6, 20/48 lines), [[LRRC59]] 1.39× (z +4.6, 37/48 lines), [[FASTKD1]] 1.22× (z +4.5, 17/48 lines), [[NOC3L]] 1.29× (z +4.3, 26/48 lines), [[AGPAT5]] 1.27× (z +4.3, 23/48 lines), [[OSGIN1]] 1.49× (z +4.3, 12/44 lines)

**0.5 µM** (246 genes, none with an alert; 12 shown): [[KIF21A]] 1.44× (z +6.1, 33/47 lines), [[NOC3L]] 1.57× (z +5.9, 38/48 lines), [[YARS1]] 1.43× (z +5.5, 32/49 lines), [[POLR3G]] 1.57× (z +5.4, 24/45 lines), [[PDCD11]] 1.47× (z +5.3, 33/48 lines), [[GPAT3]] 1.61× (z +5.1, 24/42 lines), [[RABEPK]] 1.55× (z +5.0, 21/48 lines), [[FRMD5]] 1.45× (z +4.9, 20/39 lines), [[WDR3]] 1.44× (z +4.8, 21/48 lines), [[EARS2]] 1.37× (z +4.8, 10/48 lines), [[DHX37]] 1.45× (z +4.8, 16/47 lines), [[PNO1]] 1.57× (z +4.7, 22/48 lines)

**5 µM** (1011 genes, none with an alert; 12 shown): [[FRMD5]] 2.63× (z +9.4, 30/38 lines), [[PDCD11]] 2.53× (z +9.4, 45/48 lines), [[DHX37]] 2.66× (z +9.3, 41/47 lines), [[MRPS25]] 2.05× (z +8.4, 38/48 lines), [[POLR1B]] 2.36× (z +8.1, 33/47 lines), [[NOC3L]] 2.32× (z +8.0, 39/48 lines), [[GEMIN5]] 1.92× (z +7.9, 33/48 lines), [[WDR3]] 2.07× (z +7.8, 38/48 lines), [[NOL10]] 1.68× (z +7.8, 41/48 lines), [[GPHN]] 1.74× (z +7.6, 42/47 lines), [[KIF21A]] 1.87× (z +7.6, 37/46 lines), [[MDN1]] 1.96× (z +7.5, 40/48 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (371 genes, none with an alert; 12 shown): [[TFDP2]] 0.586× (z -15.6, 47/48 lines), [[CCDC28A]] 0.405× (z -14.8, 44/48 lines), [[PDCD4]] 0.550× (z -12.3, 44/48 lines), [[KLHL24]] 0.471× (z -11.4, 45/48 lines), [[FBXL20]] 0.637× (z -9.8, 41/48 lines), [[FBXO25]] 0.622× (z -9.8, 32/43 lines), [[BCAS3]] 0.573× (z -9.5, 48/48 lines), [[JMY]] 0.551× (z -9.1, 44/47 lines), [[REPS2]] 0.529× (z -9.0, 30/36 lines), [[TNRC6B]] 0.723× (z -8.8, 36/48 lines), [[CREBRF]] 0.552× (z -8.7, 45/48 lines), [[TCP11L2]] 0.508× (z -8.4, 44/47 lines)

**0.5 µM** (359 genes, none with an alert; 12 shown): [[TNRC6B]] 0.658× (z -12.7, 47/49 lines), [[TFDP2]] 0.645× (z -9.7, 44/49 lines), [[PDCD4]] 0.572× (z -8.7, 45/49 lines), [[CCDC28A]] 0.505× (z -8.5, 38/48 lines), [[RB1CC1]] 0.643× (z -7.7, 46/49 lines), [[GARRE1]] 0.613× (z -7.7, 43/49 lines), [[PLEKHM3]] 0.579× (z -7.6, 37/48 lines), [[WIPI2]] 0.627× (z -7.3, 39/49 lines), [[TCP11L2]] 0.476× (z -7.0, 42/49 lines), [[MOB2]] 0.589× (z -6.8, 31/48 lines), [[KLHL24]] 0.526× (z -6.7, 45/49 lines), [[ACVR2B]] 0.671× (z -6.7, 24/48 lines)

**5 µM** (1122 genes, none with an alert; 12 shown): [[PDCD4]] 0.198× (z -18.5, 46/48 lines), [[KLHL24]] 0.136× (z -16.1, 48/48 lines), [[TFDP2]] 0.384× (z -15.4, 44/48 lines), [[CCDC28A]] 0.186× (z -15.2, 44/47 lines), [[FBXL20]] 0.224× (z -15.1, 47/48 lines), [[CREBRF]] 0.169× (z -14.5, 47/48 lines), [[RB1CC1]] 0.324× (z -14.4, 48/48 lines), [[GARRE1]] 0.286× (z -14.4, 45/48 lines), [[FBXO25]] 0.294× (z -14.0, 39/43 lines), [[YPEL2]] 0.227× (z -13.2, 42/44 lines), [[CRIPT]] 0.276× (z -13.0, 42/48 lines), [[JMY]] 0.220× (z -12.8, 46/47 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | [[Module 145]] (-3.8), [[Module 225]] (-3.7), [[Module 076]] (-3.7) |
| 0.5 µM | [[Module 033]] (+2.1) | [[Module 225]] (-4.3), [[Module 069]] (-3.4), [[Module 145]] (-3.2) |
| 5 µM | [[Module 033]] (+4.5), [[Module 005]] (+4.1), [[Module 001]] (+3.9) | [[Module 069]] (-6.5), [[Module 145]] (-6.0), [[Module 187]] (-5.7) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | [[J82 (line)]] (-3.6) | [[SW48 (line)]] (1.84), [[LoVo (line)]] (1.68), [[Hs 766T (line)]] (1.47), [[RKO (line)]] (1.46) · weakest: [[A-172 (line)]] (0.579), [[HS-578T (line)]] (0.660), [[BT-474 (line)]] (0.700) |
| 0.5 µM | [[SW 1088 (line)]] (-3.3) | [[NCI-H1792 (line)]] (1.48), [[NCI-H460 (line)]] (1.38), [[MIA PaCa-2 (line)]] (1.38), [[LOX-IMVI (line)]] (1.23) · weakest: [[BT-474 (line)]] (0.559), [[LS 180 (line)]] (0.638), [[A-172 (line)]] (0.716) |
| 5 µM | [[RPMI-7951 (line)]] (-7.8), [[Hs 766T (line)]] (-6.3), [[SK-MEL-2 (line)]] (-5.3), [[Panc 03.27 (line)]] (-4.6), [[BT-474 (line)]] (-4.2) | [[MIA PaCa-2 (line)]] (1.37), [[NCI-H1792 (line)]] (1.29), [[NCI-H460 (line)]] (1.28), [[AsPC-1 (line)]] (1.27) · weakest: [[LS 180 (line)]] (0.640), [[CHP-212 (line)]] (0.717), [[NCI-H661 (line)]] (0.725) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar.*

- [[c-Kit-IN-1 (drug)]] (+0.94, Multi-TK inhibitor); [[TAK-733 (drug)]] (+0.90, MEK inhibitor); [[Abemaciclib (drug)]] (+0.87, CDK inhibitor); [[venetoclax (drug)]] (+0.82, unclear); [[Sapanisertib (drug)]] (+0.67, MTOR inhibitor); [[Belzutifan (drug)]] (+0.62, unclear); [[Everolimus (drug)]] (+0.61, MTOR inhibitor); [[Volasertib (drug)]] (+0.56, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 51 arrows, 51 of them with an alert ⚠; grade A 0, B 38, C 13. Shown: the 15 strongest; 36 more arrows (36 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[RNF39]] | 0.05 µM | B | RNF39 activity raises the cells' numbers under EX229 0.05 µM (protects the cells) | lines that do not express RNF39 (30) vs lines expressing it (18) | the lines without RNF39: 0.83× the cells of the other lines | 0.036 | ⚠ within organs, on part of the lines; also absent: CDH1, TNNT2, TRIM15; maybe low, not absent |
| [[KRT16]] | 0.05 µM | B | KRT16 activity raises the cells' numbers under EX229 0.05 µM (protects the cells) | lines that do not express KRT16 (27) vs lines expressing it (21) | the lines without KRT16: 0.85× the cells of the other lines | 0.052 | ⚠ within organs, on part of the lines; also absent: TRIM29, LGR6, IRF6 |
| [[FOXQ1]] | 0.05 µM | B | FOXQ1 activity raises the cells' numbers under EX229 0.05 µM (protects the cells) | lines that do not express FOXQ1 (30) vs lines expressing it (18) | the lines without FOXQ1: 0.84× the cells of the other lines | 0.058 | ⚠ within organs, on part of the lines; also absent: SERPINB5, TTC22, COL17A1 |
| [[CATSPERB]] | 0.05 µM | B | CATSPERB activity raises the cells' numbers under EX229 0.05 µM (protects the cells) | lines that do not express CATSPERB (30) vs lines expressing it (18) | the lines without CATSPERB: 0.85× the cells of the other lines | 0.058 | ⚠ within organs, on part of the lines; also absent: SGPP2, TC2N, ST14 |
| [[INAVA]], [[MROH3P]] | 0.05 µM | B | INAVA, MROH3P activity raises the cells' numbers under EX229 0.05 µM (protects the cells) | lines that do not express INAVA, MROH3P (29) vs lines expressing them (19) | the lines without INAVA, MROH3P: 0.84× the cells of the other lines | 0.060 | ⚠ within organs, on part of the lines; also absent: CDH1, MAL2, B3GNT3; co-absent genes |
| [[RNF165]] | 5 µM | B | RNF165 activity lowers the cells' numbers under EX229 5 µM (makes them more sensitive) | lines that do not express RNF165 (21) vs lines expressing it (27) | the lines without RNF165: 1.26× the cells of the other lines | 0.065 | ⚠ within organs, on part of the lines; also absent: TDRP, ZSCAN18, SH3GL3 |
| [[GJB3]] | 0.05 µM | B | GJB3 activity raises the cells' numbers under EX229 0.05 µM (protects the cells) | lines that do not express GJB3 (31) vs lines expressing it (17) | the lines without GJB3: 0.83× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: IRF6, COL17A1, KLK10 |
| [[ST14]] | 0.05 µM | B | ST14 activity raises the cells' numbers under EX229 0.05 µM (protects the cells) | lines that do not express ST14 (32) vs lines expressing it (16) | the lines without ST14: 0.83× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, TMEM125, CDH1 |
| [[FGFBP1]] | 0.05 µM | B | FGFBP1 activity raises the cells' numbers under EX229 0.05 µM (protects the cells) | lines that do not express FGFBP1 (36) vs lines expressing it (12) | the lines without FGFBP1: 0.83× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: COL17A1, KLK10, SERPINB5 |
| [[S100A14]] | 0.05 µM | B | S100A14 activity raises the cells' numbers under EX229 0.05 µM (protects the cells) | lines that do not express S100A14 (33) vs lines expressing it (15) | the lines without S100A14: 0.84× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: PRSS8, RAB25, TMPRSS4 |
| [[ENSG00000204876]] | 0.05 µM | B | ENSG00000204876 activity raises the cells' numbers under EX229 0.05 µM (protects the cells) | lines that do not express ENSG00000204876 (27) vs lines expressing it (21) | the lines without ENSG00000204876: 0.87× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: EPS8L3, AREG, ENSG00000225680 |
| [[ENSG00000225680]] | 0.05 µM | B | ENSG00000225680 activity raises the cells' numbers under EX229 0.05 µM (protects the cells) | lines that do not express ENSG00000225680 (33) vs lines expressing it (15) | the lines without ENSG00000225680: 0.83× the cells of the other lines | 0.073 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TRIM15, EPS8L3, LINC02964 |
| [[MPZL3]] | 0.05 µM | B | MPZL3 activity raises the cells' numbers under EX229 0.05 µM (protects the cells) | lines that do not express MPZL3 (25) vs lines expressing it (23) | the lines without MPZL3: 0.85× the cells of the other lines | 0.073 | ⚠ within organs, on part of the lines; also absent: RNF39, MYO5B, CDH1 |
| [[TNNT2]] | 0.05 µM | B | TNNT2 activity raises the cells' numbers under EX229 0.05 µM (protects the cells) | lines that do not express TNNT2 (29) vs lines expressing it (19) | the lines without TNNT2: 0.83× the cells of the other lines | 0.073 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, ATP2C2, ST14 |
| [[OVOL1]], [[TMPRSS4]] | 0.05 µM | B | OVOL1, TMPRSS4 activity raises the cells' numbers under EX229 0.05 µM (protects the cells) | lines that do not express OVOL1, TMPRSS4 (33) vs lines expressing them (15) | the lines without OVOL1, TMPRSS4: 0.83× the cells of the other lines | 0.075 | ⚠ within organs, on part of the lines; also absent: GRHL2, ST14, TMEM30B; co-absent genes |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "EX229"
- `tables/drugdoses.parquet` — dd in 392, 393, 394
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
