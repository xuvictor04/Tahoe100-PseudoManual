---
drug: "5-Azacytidine"
type: "drug"
salt_base: "5-Azacytidine"
targets: "DNMT1"
moa_fine: "DNA methyltransferase inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 1424
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# 5-Azacytidine

*DNA methyltransferase inhibitor (inhibitor/antagonist) · targets: DNMT1 · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 0 / 8 / 1424; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.23 / 0.23.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 10]]:G9 | 0 / 0 | — | +0.02 | +0.0/+0.6/+0.3 | — |
| 0.5 µM | [[Plate 11]]:G9 | 4 / 4 | — | -0.41 | -0.1/+1.2/+0.1 | — |
| 5 µM | [[Plate 12]]:G9 | 632 / 792 | — | -0.52 | -1.3/+1.0/+0.2 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (4 genes, none with an alert): [[EPHA1]] 1.34× (z +3.2, 3/19 lines), [[VIPR1]] 1.40× (z +3.1, 0/21 lines), [[DSC3]] 1.32× (z +3.0, 3/16 lines), [[ENSG00000239462]] 1.25× (z +2.8, 6/28 lines)

**5 µM** (632 genes, none with an alert; 12 shown): [[NIBAN1]] 2.55× (z +15.3, 32/37 lines), [[TRIB3]] 2.33× (z +11.9, 39/44 lines), [[WARS1]] 2.02× (z +11.3, 41/47 lines), [[CREB5]] 1.90× (z +11.2, 25/33 lines), [[AARS1]] 2.00× (z +11.2, 47/48 lines), [[PCK2]] 2.13× (z +10.5, 38/46 lines), [[MOCOS]] 1.97× (z +10.2, 33/41 lines), [[CLIP1]] 1.35× (z +9.6, 37/48 lines), [[ARHGEF2]] 1.81× (z +9.6, 41/47 lines), [[XPOT]] 1.54× (z +8.9, 41/48 lines), [[ASNS]] 1.99× (z +8.9, 36/44 lines), [[SLC22A15]] 1.95× (z +8.8, 23/35 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (4 genes, none with an alert): [[CHST14]] 0.612× (z -3.9, 9/31 lines), [[POLR3H]] 0.783× (z -3.5, 11/45 lines), [[PDE1C]] 0.799× (z -3.3, 5/19 lines), [[HMGCR]] 0.813× (z -3.0, 16/47 lines)

**5 µM** (792 genes, none with an alert; 12 shown): [[SORL1]] 0.563× (z -9.1, 25/26 lines), [[SLC16A7]] 0.539× (z -8.3, 19/24 lines), [[ARRB1]] 0.639× (z -8.2, 29/46 lines), [[PAPSS2]] 0.676× (z -8.0, 23/33 lines), [[MEF2C]] 0.619× (z -7.9, 24/33 lines), [[GXYLT2]] 0.593× (z -7.7, 25/37 lines), [[SLC39A8]] 0.689× (z -7.5, 22/35 lines), [[PAG1]] 0.702× (z -7.5, 23/33 lines), [[LGR4]] 0.689× (z -7.4, 28/41 lines), [[ARHGAP18]] 0.693× (z -7.4, 26/42 lines), [[ARID5B]] 0.626× (z -7.4, 31/42 lines), [[CD82]] 0.653× (z -7.3, 26/37 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | [[Module 133]] (+5.3), [[Module 063]] (+4.7), [[Module 135]] (+4.4) | [[Module 045]] (-4.6), [[Module 065]] (-3.6), [[Module 057]] (-3.3) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | [[NCI-H1792 (line)]] (-5.1), [[SK-MEL-2 (line)]] (-4.1), [[H4 (line)]] (-3.8) | [[H4 (line)]] (1.44), [[LOX-IMVI (line)]] (1.39), [[Panc 03.27 (line)]] (1.31), [[NCI-H460 (line)]] (1.31) · weakest: [[NCI-H661 (line)]] (0.460), [[SW1417 (line)]] (0.588), [[SW 1088 (line)]] (0.612) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 2 next most similar without an alert.*

- [[Peretinoin (drug)]] (+0.59, Retinoic receptor agonist); [[Neratinib (maleate) (drug)]] (+0.55, EGFR/ERBB inhibitor, ⚠ vector dose flagged: cell-cycle shift); [[Belumosudil (mesylate) (drug)]] (+0.53, unclear); [[Dihydroartemisinin (drug)]] (+0.50, unclear); [[Daptomycin (drug)]] (+0.49, unclear, ⚠ no trustworthy dose (vector dose flagged: unreliable plate only)); [[Neratinib (drug)]] (+0.47, EGFR/ERBB inhibitor); [[Dabrafenib (drug)]] (+0.46, RAF inhibitor); [[Dapagliflozin (drug)]] (+0.45, Glucose transporter inhibitor); [[Vinblastine (sulfate) (drug)]] (+0.44, Microtubule inhibitor); [[Ivermectin (drug)]] (+0.40, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 51 arrows, 51 of them with an alert ⚠; grade A 0, B 43, C 8. Shown: the 15 strongest; 36 more arrows (36 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[EPCAM]] | 5 µM | B | EPCAM activity raises the cells' numbers under 5-Azacytidine 5 µM (protects the cells) | lines that do not express EPCAM (28) vs lines expressing it (20) | the lines without EPCAM: 0.76× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, KDF1, CLDN3 |
| [[BNC2]] | 5 µM | B | BNC2 activity lowers the cells' numbers under 5-Azacytidine 5 µM (makes them more sensitive) | lines that do not express BNC2 (21) vs lines expressing it (27) | the lines without BNC2: 1.30× the cells of the other lines | 0.036 | ⚠ within organs, on part of the lines; also absent: LINC03041, DPY19L2, RNF182 |
| [[CDH1]] | 5 µM | B | CDH1 activity raises the cells' numbers under 5-Azacytidine 5 µM (protects the cells) | lines that do not express CDH1 (31) vs lines expressing it (17) | the lines without CDH1: 0.75× the cells of the other lines | 0.050 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ST14, LAD1, KDF1 |
| [[CGN]] | 5 µM | B | CGN activity raises the cells' numbers under 5-Azacytidine 5 µM (protects the cells) | lines that do not express CGN (21) vs lines expressing it (27) | the lines without CGN: 0.76× the cells of the other lines | 0.056 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, CRACDL, CAMSAP3 |
| [[KDF1]] | 5 µM | B | KDF1 activity raises the cells' numbers under 5-Azacytidine 5 µM (protects the cells) | lines that do not express KDF1 (30) vs lines expressing it (18) | the lines without KDF1: 0.76× the cells of the other lines | 0.058 | ⚠ within organs, on part of the lines; also absent: CDH1, ESRP1, CRB3 |
| [[C1orf116]], [[IRF6]] | 5 µM | B | C1orf116, IRF6 activity raises the cells' numbers under 5-Azacytidine 5 µM (protects the cells) | lines that do not express C1orf116, IRF6 (31) vs lines expressing them (17) | the lines without C1orf116, IRF6: 0.77× the cells of the other lines | 0.058 | ⚠ within organs, on part of the lines; also absent: ST14, TMPRSS4, TMEM125; co-absent genes |
| [[DCLK2]] | 5 µM | B | DCLK2 activity lowers the cells' numbers under 5-Azacytidine 5 µM (makes them more sensitive) | lines that do not express DCLK2 (17) vs lines expressing it (31) | the lines without DCLK2: 1.24× the cells of the other lines | 0.068 | ⚠ within organs, on part of the lines; also absent: LINC03041, HECW2, AFF3 |
| [[NPNT]] | 5 µM | B | NPNT activity raises the cells' numbers under 5-Azacytidine 5 µM (protects the cells) | lines that do not express NPNT (33) vs lines expressing it (15) | the lines without NPNT: 0.76× the cells of the other lines | 0.071 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: PRSS8, RAB25, TMPRSS4 |
| [[ST14]] | 5 µM | B | ST14 activity raises the cells' numbers under 5-Azacytidine 5 µM (protects the cells) | lines that do not express ST14 (32) vs lines expressing it (16) | the lines without ST14: 0.77× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, TMEM125, CDH1 |
| [[TRIM29]] | 5 µM | B | TRIM29 activity raises the cells' numbers under 5-Azacytidine 5 µM (protects the cells) | lines that do not express TRIM29 (28) vs lines expressing it (20) | the lines without TRIM29: 0.79× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: CDH1, IRF6, TNNT2 |
| [[CDS1]] | 5 µM | B | CDS1 activity raises the cells' numbers under 5-Azacytidine 5 µM (protects the cells) | lines that do not express CDS1 (19) vs lines expressing it (29) | the lines without CDS1: 0.80× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: ANO9, EPS8L2, C6orf132; maybe low, not absent |
| [[ANXA3]] | 5 µM | B | ANXA3 activity raises the cells' numbers under 5-Azacytidine 5 µM (protects the cells) | lines that do not express ANXA3 (24) vs lines expressing it (24) | the lines without ANXA3: 0.82× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: RNF223, P2RY2, C6orf132 |
| [[MPZL2]] | 5 µM | B | MPZL2 activity raises the cells' numbers under 5-Azacytidine 5 µM (protects the cells) | lines that do not express MPZL2 (29) vs lines expressing it (19) | the lines without MPZL2: 0.76× the cells of the other lines | 0.074 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, IRF6, ST14 |
| [[HS3ST1]] | 5 µM | B | HS3ST1 activity raises the cells' numbers under 5-Azacytidine 5 µM (protects the cells) | lines that do not express HS3ST1 (31) vs lines expressing it (17) | the lines without HS3ST1: 0.79× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; also absent: KLK10, ADGRF1, TMPRSS4 |
| [[TNFSF15]] | 5 µM | B | TNFSF15 activity raises the cells' numbers under 5-Azacytidine 5 µM (protects the cells) | lines that do not express TNFSF15 (31) vs lines expressing it (17) | the lines without TNFSF15: 0.77× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, GRHL2, ST14 |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "5-Azacytidine"
- `tables/drugdoses.parquet` — dd in 12, 13, 14
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
