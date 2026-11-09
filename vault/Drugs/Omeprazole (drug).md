---
drug: "Omeprazole"
type: "drug"
salt_base: "Omeprazole"
targets: ""
moa_fine: "unclear"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "0.05"
max_sig_genes: 112
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Omeprazole

*unclear (inhibitor/antagonist) · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 112 / 88 / 32; best dose 0.05 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.05 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.26 / 0.29.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 10]]:A7 | 93 / 19 | — | +0.85 | +1.8/+0.2/-0.5 | — |
| 0.5 µM | [[Plate 11]]:A7 | 84 / 4 | — | -0.82 | +1.1/+0.6/+0.9 | — |
| 5 µM | [[Plate 12]]:A7 | 26 / 6 | — | +0.70 | +1.7/+0.5/-0.8 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (93 genes, none with an alert; 12 shown): [[LAMB1]] 1.27× (z +4.3, 26/41 lines), [[SAMD9]] 1.68× (z +4.3, 28/37 lines), [[COL27A1]] 1.24× (z +4.1, 14/36 lines), [[LANCL2]] 1.31× (z +4.0, 23/48 lines), [[LINC01252]] 1.63× (z +3.9, 6/29 lines), [[IFIT1]] 1.69× (z +3.9, 28/44 lines), [[SLC16A3]] 1.29× (z +3.9, 27/41 lines), [[NLRC5]] 1.34× (z +3.9, 12/43 lines), [[TMEM45A]] 1.36× (z +3.8, 19/35 lines), [[MX1]] 1.43× (z +3.8, 22/29 lines), [[TET1]] 1.26× (z +3.8, 14/36 lines), [[IFIT5]] 1.43× (z +3.8, 13/48 lines)

**0.5 µM** (84 genes, none with an alert; 12 shown): [[LRRC34]] 1.66× (z +5.3, 5/20 lines), [[LINC02175]] 1.64× (z +4.4, 7/27 lines), [[LINC02331]] 1.59× (z +3.9, 3/18 lines), [[CCDC28B]] 1.54× (z +3.7, 4/35 lines), [[CAPN14]] 1.53× (z +3.7, 2/17 lines), [[LINC00299]] 1.47× (z +3.7, 3/18 lines), [[ENSG00000272305]] 1.28× (z +3.6, 10/44 lines), [[GSTK1]] 1.35× (z +3.6, 16/45 lines), [[SCUBE3]] 1.46× (z +3.5, 2/13 lines), [[ENSG00000287778]] 1.35× (z +3.5, 4/20 lines), [[ENSG00000270792]] 1.43× (z +3.5, 6/39 lines), [[KBTBD7]] 1.33× (z +3.5, 6/40 lines)

**5 µM** (26 genes, none with an alert; 12 shown): [[SUMF1]] 1.38× (z +3.7, 36/48 lines), [[PCDH7]] 1.39× (z +3.7, 15/30 lines), [[ENSG00000259336]] 1.53× (z +3.6, 6/45 lines), [[ENC1]] 1.45× (z +3.6, 16/43 lines), [[ENSG00000287249]] 1.37× (z +3.5, 0/45 lines), [[IRS1]] 1.32× (z +3.5, 7/42 lines), [[DPH6]] 1.35× (z +3.4, 21/48 lines), [[CFAP418-AS1]] 1.41× (z +3.4, 6/48 lines), [[CLYBL]] 1.26× (z +3.3, 8/46 lines), [[LANCL2]] 1.24× (z +3.3, 13/48 lines), [[NAALADL2]] 1.40× (z +3.2, 19/37 lines), [[DAB1]] 1.32× (z +3.2, 6/48 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (19 genes, none with an alert; 12 shown): [[ZNF670]] 0.786× (z -4.1, 17/48 lines), [[TIGAR]] 0.772× (z -3.9, 13/47 lines), [[PCGF6]] 0.785× (z -3.9, 7/48 lines), [[TRAF3IP2]] 0.810× (z -3.8, 7/45 lines), [[AMN1]] 0.787× (z -3.6, 17/46 lines), [[AUNIP]] 0.697× (z -3.6, 8/47 lines), [[ZBTB43]] 0.813× (z -3.5, 18/48 lines), [[C5orf34]] 0.817× (z -3.4, 4/48 lines), [[DRAM1]] 0.818× (z -3.4, 15/42 lines), [[FAM24B]] 0.794× (z -3.4, 7/40 lines), [[SNHG30]] 0.808× (z -3.3, 5/48 lines), [[ENSG00000266908]] 0.681× (z -3.3, 4/44 lines)

**0.5 µM** (4 genes, none with an alert): [[PLEKHB2]] 0.826× (z -3.6, 20/48 lines), [[KIAA0513]] 0.789× (z -3.2, 10/45 lines), [[ENSG00000291147]] 0.793× (z -3.0, 9/43 lines), [[PIF1]] 0.811× (z -2.6, 7/44 lines)

**5 µM** (6 genes, none with an alert): [[DRAM1]] 0.794× (z -3.9, 15/42 lines), [[NIBAN1]] 0.815× (z -3.4, 11/37 lines), [[SASS6]] 0.821× (z -3.1, 6/48 lines), [[GK]] 0.798× (z -3.1, 4/44 lines), [[ENSG00000284697]] 0.723× (z -3.0, 8/48 lines), [[CSF2]] 0.513× (z -3.0, 8/22 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | [[Module 010]] (+2.5), [[Module 016]] (+2.1) | [[Module 168]] (-2.1), [[Module 171]] (-2.1) |
| 0.5 µM | [[Module 024]] (+2.0) | — |
| 5 µM | [[Module 010]] (+2.0) | [[Module 207]] (-2.5), [[Module 171]] (-2.0) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | [[NCI-H1792 (line)]] (1.35), [[Panc 03.27 (line)]] (1.30), [[COLO 205 (line)]] (1.29), [[J82 (line)]] (1.28) · weakest: [[NCI-H661 (line)]] (0.0293), [[LS 180 (line)]] (0.364), [[AN3 CA (line)]] (0.421) |
| 0.5 µM | — | [[SW 1271 (line)]] (1.60), [[AN3 CA (line)]] (1.48), [[CHP-212 (line)]] (1.33), [[NCI-H661 (line)]] (1.33) · weakest: [[NCI-H23 (line)]] (0.232), [[SW480 (line)]] (0.307), [[NCI-H2347 (line)]] (0.453) |
| 5 µM | [[HEC-1-A (line)]] (-3.1) | [[RPMI-7951 (line)]] (1.54), [[SNU-1 (line)]] (1.37), [[LS 180 (line)]] (1.21), [[HOP62 (line)]] (1.21) · weakest: [[SW 1088 (line)]] (0.181), [[NCI-H661 (line)]] (0.368), [[A-427 (line)]] (0.473) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 1 next most similar without an alert.*

- [[Esmolol (hydrochloride) (drug)]] (+0.84, unclear); [[Demeclocycline (drug)]] (+0.77, unclear); [[Apalutamide (drug)]] (+0.76, Androgen receptor antagonist); [[Glasdegib (drug)]] (+0.76, Sonic inhibitor, ⚠ only 4 significant genes; no trustworthy dose (vector dose flagged: unreliable plate only)); [[Diphenhydramine (drug)]] (+0.71, unclear); [[Mifepristone (drug)]] (+0.70, unclear); [[Estrone sulfate (potassium) (drug)]] (+0.70, unclear); [[Filgotinib (drug)]] (+0.69, JAK/STAT inhibitor); [[Tirabrutinib (drug)]] (+0.68, Other TK inhibitor)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 101 arrows, 101 of them with an alert ⚠; grade A 0, B 97, C 4. Shown: the 15 strongest; 86 more arrows (86 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[RASEF]] | 0.05 µM | B | RASEF activity lowers the cells' numbers under Omeprazole 0.05 µM (makes them more sensitive) | lines that do not express RASEF (20) vs lines expressing it (28) | the lines without RASEF: 1.23× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: LIPH, ENSG00000263325, DENND2D |
| [[GJB3]] | 5 µM | B | GJB3 activity lowers the cells' numbers under Omeprazole 5 µM (makes them more sensitive) | lines that do not express GJB3 (31) vs lines expressing it (17) | the lines without GJB3: 1.20× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: IRF6, COL17A1, KLK10 |
| [[ENSG00000262302]] | 5 µM | B | ENSG00000262302 activity lowers the cells' numbers under Omeprazole 5 µM (makes them more sensitive) | lines that do not express ENSG00000262302 (29) vs lines expressing it (19) | the lines without ENSG00000262302: 1.20× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: CLDN7, ESRP1, ATP2C2; maybe low, not absent |
| [[ST14]] | 5 µM | B | ST14 activity lowers the cells' numbers under Omeprazole 5 µM (makes them more sensitive) | lines that do not express ST14 (32) vs lines expressing it (16) | the lines without ST14: 1.19× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, TMEM125, CDH1 |
| [[RNF39]] | 5 µM | B | RNF39 activity lowers the cells' numbers under Omeprazole 5 µM (makes them more sensitive) | lines that do not express RNF39 (30) vs lines expressing it (18) | the lines without RNF39: 1.16× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: CDH1, TNNT2, TRIM15; maybe low, not absent |
| [[TNNT2]] | 5 µM | B | TNNT2 activity lowers the cells' numbers under Omeprazole 5 µM (makes them more sensitive) | lines that do not express TNNT2 (29) vs lines expressing it (19) | the lines without TNNT2: 1.16× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, ATP2C2, ST14 |
| [[FGD4]] | 0.05 µM | B | FGD4 activity lowers the cells' numbers under Omeprazole 0.05 µM (makes them more sensitive) | lines that do not express FGD4 (10) vs lines expressing it (38) | the lines without FGD4: 1.25× the cells of the other lines | 0.027 | ⚠ within organs, on part of the lines; also absent: PARD6B, CARD10, VAMP8; maybe low, not absent |
| [[ATP2C2]] | 5 µM | B | ATP2C2 activity lowers the cells' numbers under Omeprazole 5 µM (makes them more sensitive) | lines that do not express ATP2C2 (32) vs lines expressing it (16) | the lines without ATP2C2: 1.20× the cells of the other lines | 0.033 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, GRHL2, ST14 |
| [[ESRP1]] | 5 µM | B | ESRP1 activity lowers the cells' numbers under Omeprazole 5 µM (makes them more sensitive) | lines that do not express ESRP1 (31) vs lines expressing it (17) | the lines without ESRP1: 1.18× the cells of the other lines | 0.036 | ⚠ within organs, on part of the lines; also absent: ST14, KDF1, CLDN7 |
| [[CLDN4]] | 5 µM | B | CLDN4 activity lowers the cells' numbers under Omeprazole 5 µM (makes them more sensitive) | lines that do not express CLDN4 (26) vs lines expressing it (22) | the lines without CLDN4: 1.16× the cells of the other lines | 0.036 | ⚠ within organs, on part of the lines; also absent: CDH1, SCNN1A, ITGB6 |
| [[KDF1]] | 5 µM | B | KDF1 activity lowers the cells' numbers under Omeprazole 5 µM (makes them more sensitive) | lines that do not express KDF1 (30) vs lines expressing it (18) | the lines without KDF1: 1.15× the cells of the other lines | 0.038 | ⚠ within organs, on part of the lines; also absent: CDH1, ESRP1, CRB3 |
| [[OVOL1]], [[TMPRSS4]] | 5 µM | B | OVOL1, TMPRSS4 activity lowers the cells' numbers under Omeprazole 5 µM (makes them more sensitive) | lines that do not express OVOL1, TMPRSS4 (33) vs lines expressing them (15) | the lines without OVOL1, TMPRSS4: 1.19× the cells of the other lines | 0.041 | ⚠ within organs, on part of the lines; also absent: GRHL2, ST14, TMEM30B; co-absent genes |
| [[CCL3]] | 0.05 µM | B | CCL3 activity raises the cells' numbers under Omeprazole 0.05 µM (protects the cells) | lines that do not express CCL3 (37) vs lines expressing it (11) | the lines without CCL3: 0.79× the cells of the other lines | 0.043 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TMPRSS15, ENSG00000224865, ESM1 |
| [[CLDN7]] | 5 µM | B | CLDN7 activity lowers the cells' numbers under Omeprazole 5 µM (makes them more sensitive) | lines that do not express CLDN7 (30) vs lines expressing it (18) | the lines without CLDN7: 1.18× the cells of the other lines | 0.044 | ⚠ within organs, on part of the lines; also absent: ESRP1, ENSG00000262302, ST14 |
| [[C1orf116]], [[IRF6]] | 5 µM | B | C1orf116, IRF6 activity lowers the cells' numbers under Omeprazole 5 µM (makes them more sensitive) | lines that do not express C1orf116, IRF6 (31) vs lines expressing them (17) | the lines without C1orf116, IRF6: 1.19× the cells of the other lines | 0.046 | ⚠ within organs, on part of the lines; also absent: ST14, TMPRSS4, TMEM125; co-absent genes |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Omeprazole"
- `tables/drugdoses.parquet` — dd in 738, 739, 740
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
