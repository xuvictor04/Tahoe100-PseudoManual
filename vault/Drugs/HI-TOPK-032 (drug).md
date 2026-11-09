---
drug: "HI-TOPK-032"
type: "drug"
salt_base: "HI-TOPK-032"
targets: "PBK"
moa_fine: "unclear"
moa_broad: "inhibitor/antagonist"
approved: "no"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 1347
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# HI-TOPK-032

*unclear (inhibitor/antagonist) · targets: PBK · approved: no*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 174 / 42 / 1347; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.05 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): -0.01 / 0.51.
> Flags by dose: low cells (technical?) / noisy plate (z scaled) / noisy plate (z scaled).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 01]]:H1 | 45 / 129 | — | -1.23 | +0.2/+1.5/-0.1 | low cells (technical?) |
| 0.5 µM | [[Plate 02]]:H1 | 21 / 21 | — | +0.00 | +0.4/+2.1/+1.2 | noisy plate (z scaled) |
| 5 µM | [[Plate 03]]:H1 | 652 / 695 | — | -0.38 | +0.9/+2.1/-0.0 | noisy plate (z scaled) |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (45 genes, none with an alert; 12 shown): [[CEP170P1]] 1.67× (z +5.0, 4/30 lines), [[TFB1M]] 1.22× (z +4.2, 12/46 lines), [[WT1]] 1.50× (z +4.1, 4/17 lines), [[PXN-AS1]] 1.48× (z +4.0, 3/42 lines), [[TRMU]] 1.27× (z +3.8, 14/47 lines), [[OIP5]] 1.35× (z +3.8, 12/43 lines), [[ENSG00000258101]] 1.41× (z +3.7, 5/39 lines), [[TMEM87B]] 1.21× (z +3.7, 15/47 lines), [[ARL6]] 1.30× (z +3.7, 10/44 lines), [[AK4]] 1.22× (z +3.6, 20/47 lines), [[HERC2P10]] 1.41× (z +3.6, 0/20 lines), [[WNK3]] 1.28× (z +3.5, 0/17 lines)

**0.5 µM** (21 genes, none with an alert; 12 shown): [[HMMR]] 1.70× (z +4.0, 22/48 lines), [[SGO2]] 1.40× (z +3.8, 21/48 lines), [[SMC4]] 1.30× (z +3.5, 21/48 lines), [[BCHE]] 1.54× (z +3.4, 0/13 lines), [[CDC25C]] 1.39× (z +3.4, 12/48 lines), [[DBF4]] 1.41× (z +3.4, 21/49 lines), [[ZCCHC24]] 1.27× (z +3.3, 1/43 lines), [[CDC20]] 1.62× (z +3.3, 20/45 lines), [[KNL1]] 1.30× (z +3.2, 14/47 lines), [[SUN2]] 1.24× (z +3.2, 6/48 lines), [[EFR3B]] 1.31× (z +3.1, 1/38 lines), [[CENPE]] 1.29× (z +3.1, 11/49 lines)

**5 µM** (652 genes, none with an alert; 12 shown): [[EFR3B]] 3.94× (z +11.8, 24/33 lines), [[PEG10]] 3.96× (z +10.0, 28/31 lines), [[STIM2]] 2.08× (z +9.5, 37/47 lines), [[B3GALT1]] 2.75× (z +9.5, 18/26 lines), [[MPHOSPH9]] 1.82× (z +8.2, 36/48 lines), [[SORBS1]] 2.21× (z +7.9, 27/40 lines), [[ZCCHC24]] 2.14× (z +7.6, 26/41 lines), [[SESN3]] 2.27× (z +7.5, 19/28 lines), [[NMT2]] 1.78× (z +7.3, 33/47 lines), [[ATP8A1]] 2.13× (z +7.2, 16/34 lines), [[DPF3]] 2.85× (z +7.1, 14/25 lines), [[GLCE]] 1.80× (z +7.0, 29/47 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (129 genes, none with an alert; 12 shown): [[MYOCOS]] 0.487× (z -5.1, 22/44 lines), [[ENSG00000272772]] 0.670× (z -5.1, 21/45 lines), [[TINCR]] 0.588× (z -5.1, 21/44 lines), [[ENSG00000259316]] 0.638× (z -4.9, 9/44 lines), [[WTIP]] 0.729× (z -4.9, 13/40 lines), [[ENSG00000236255]] 0.668× (z -4.9, 23/46 lines), [[LINC02803]] 0.526× (z -4.8, 25/44 lines), [[VWCE]] 0.539× (z -4.8, 22/45 lines), [[LINC01031]] 0.649× (z -4.8, 16/44 lines), [[SLC22A14]] 0.575× (z -4.7, 19/44 lines), [[ENSG00000284952]] 0.520× (z -4.7, 16/41 lines), [[LINC00654]] 0.546× (z -4.6, 11/36 lines)

**0.5 µM** (21 genes, none with an alert; 12 shown): [[ZNF618]] 0.654× (z -4.0, 14/39 lines), [[TGFBRAP1]] 0.744× (z -3.9, 12/48 lines), [[DENND1B]] 0.742× (z -3.8, 25/48 lines), [[PRSS12]] 0.736× (z -3.8, 3/28 lines), [[ALKBH8]] 0.738× (z -3.6, 6/48 lines), [[LRIG3]] 0.692× (z -3.6, 10/42 lines), [[RBMS3]] 0.760× (z -3.4, 16/30 lines), [[HERC2P10]] 0.652× (z -3.3, 5/31 lines), [[TDRD3]] 0.820× (z -3.3, 16/49 lines), [[WASHC5]] 0.812× (z -3.1, 9/49 lines), [[PTGFRN]] 0.744× (z -3.1, 5/40 lines), [[ZNF827]] 0.821× (z -3.1, 11/45 lines)

**5 µM** (695 genes, none with an alert; 12 shown): [[TDRD3]] 0.486× (z -8.8, 40/48 lines), [[GALC]] 0.417× (z -8.3, 16/29 lines), [[BNC2]] 0.369× (z -8.2, 22/27 lines), [[ZNF827]] 0.498× (z -8.1, 39/44 lines), [[ZHX2]] 0.423× (z -8.0, 36/41 lines), [[CTPS2]] 0.477× (z -7.8, 34/47 lines), [[HIPK2]] 0.574× (z -7.7, 37/43 lines), [[TMCO4]] 0.374× (z -7.5, 33/44 lines), [[RBMS3]] 0.446× (z -7.3, 25/29 lines), [[XRCC4]] 0.610× (z -7.3, 30/48 lines), [[ZNF618]] 0.351× (z -7.2, 31/37 lines), [[ZMYND8]] 0.495× (z -7.2, 41/47 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | [[Module 039]] (-2.6), [[Module 038]] (-2.2) |
| 0.5 µM | — | — |
| 5 µM | [[Module 002]] (+2.6), [[Module 093]] (+2.5), [[Module 085]] (+2.5) | [[Module 095]] (-3.6), [[Module 088]] (-3.3), [[Module 137]] (-2.9) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | [[PANC-1 (line)]] (-6.0), [[A-172 (line)]] (-4.5), [[A498 (line)]] (-3.9), [[SNU-423 (line)]] (-3.7), [[J82 (line)]] (-3.1) | [[MIA PaCa-2 (line)]] (1.60), [[NCI-H1573 (line)]] (1.40), [[C32 (line)]] (1.39), [[NCI-H23 (line)]] (1.35) · weakest: [[SHP-77 (line)]] (0.402), [[NCI-H2347 (line)]] (0.468), [[SW1417 (line)]] (0.473) |
| 0.5 µM | — | [[NCI-H23 (line)]] (1.51), [[HOP62 (line)]] (1.49), [[A549 (line)]] (1.40), [[NCI-H2030 (line)]] (1.29) · weakest: [[NCI-H2122 (line)]] (-0.0444), [[HepG2_C3A (line)]] (0.467), [[COLO 205 (line)]] (0.492) |
| 5 µM | [[SNU-1 (line)]] (-3.5), [[LOX-IMVI (line)]] (-3.4) | [[MIA PaCa-2 (line)]] (1.35), [[HOP62 (line)]] (1.25), [[Panc 03.27 (line)]] (1.23), [[CFPAC-1 (line)]] (1.16) · weakest: [[AN3 CA (line)]] (0.652), [[C-33 A (line)]] (0.697), [[NCI-H661 (line)]] (0.702) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 4 next most similar without an alert.*

- [[Fedratinib (hydrochloride hydrate) (drug)]] (+0.55, JAK/STAT inhibitor); [[Fumaric acid (drug)]] (+0.52, unclear); [[Pravastatin (sodium) (drug)]] (+0.52, unclear); [[Belinostat (drug)]] (+0.51, HDAC inhibitor, ⚠ vector dose flagged: cell-cycle shift); [[AT7519 (drug)]] (+0.51, CDK inhibitor, ⚠ only 6 significant genes); [[Daidzin (drug)]] (+0.50, unclear, ⚠ only 3 significant genes); [[Ranolazine (drug)]] (+0.49, unclear); [[Panobinostat (drug)]] (+0.49, HDAC inhibitor, ⚠ vector dose flagged: cell-cycle shift); [[Piroxicam (drug)]] (+0.45, Cyclooxygenase inhibitor); [[Sinomenine (drug)]] (+0.43, unclear); [[Tomivosertib (drug)]] (+0.43, Protein synthesis inhibitor); [[Quinidine (15% dihydroquinidine) (drug)]] (+0.42, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 29 arrows, 29 of them with an alert ⚠; grade A 0, B 22, C 7. Shown: the 15 strongest; 14 more arrows (14 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[RAB20]] | 0.05 µM | B | RAB20 activity raises the cells' numbers under HI-TOPK-032 0.05 µM (protects the cells) | lines that do not express RAB20 (8) vs lines expressing it (40) | the lines without RAB20: 0.73× the cells of the other lines | 0.067 | ⚠ within organs, on part of the lines; also absent: RPS6KA2, PRDX2, YPEL3; maybe low, not absent |
| [[NOD2]] | 5 µM | B | NOD2 activity raises the cells' numbers under HI-TOPK-032 5 µM (protects the cells) | lines that do not express NOD2 (17) vs lines expressing it (31) | the lines without NOD2: 0.84× the cells of the other lines | 0.071 | ⚠ within organs, on part of the lines; also absent: STAT5A, TLR2, BDKRB2 |
| [[LINC00589]] | 0.05 µM | B | LINC00589 activity raises the cells' numbers under HI-TOPK-032 0.05 µM (protects the cells) | lines that do not express LINC00589 (28) vs lines expressing it (20) | the lines without LINC00589: 0.80× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00520, ENSG00000267881, TSPAN8 |
| [[ENSG00000264825]] | 0.05 µM | B | ENSG00000264825 activity raises the cells' numbers under HI-TOPK-032 0.05 µM (protects the cells) | lines that do not express ENSG00000264825 (24) vs lines expressing it (24) | the lines without ENSG00000264825: 0.81× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: GATA6, TFF1, AGR2; maybe low, not absent |
| [[TRANK1]] | 5 µM | B | TRANK1 activity raises the cells' numbers under HI-TOPK-032 5 µM (protects the cells) | lines that do not express TRANK1 (7) vs lines expressing it (41) | the lines without TRANK1: 0.91× the cells of the other lines | 0.073 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[MGC32805]] | 0.05 µM | B | MGC32805 activity raises the cells' numbers under HI-TOPK-032 0.05 µM (protects the cells) | lines that do not express MGC32805 (32) vs lines expressing it (16) | the lines without MGC32805: 0.78× the cells of the other lines | 0.074 | ⚠ within organs, on part of the lines; also absent: CEACAM5, ST18, PRR15L; maybe low, not absent |
| [[LGALS3BP]] | 0.05 µM | B | LGALS3BP activity raises the cells' numbers under HI-TOPK-032 0.05 µM (protects the cells) | lines that do not express LGALS3BP (7) vs lines expressing it (41) | the lines without LGALS3BP: 0.83× the cells of the other lines | 0.078 | ⚠ within organs, on part of the lines; also absent: LGALS3, KLF4, APOL6 |
| [[SAMD9L]] | 5 µM | B | SAMD9L activity raises the cells' numbers under HI-TOPK-032 5 µM (protects the cells) | lines that do not express SAMD9L (18) vs lines expressing it (30) | the lines without SAMD9L: 0.85× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: GBP4, CD5L, TRIM22 |
| [[TFF1]] | 0.05 µM | B | TFF1 activity raises the cells' numbers under HI-TOPK-032 0.05 µM (protects the cells) | lines that do not express TFF1 (31) vs lines expressing it (17) | the lines without TFF1: 0.78× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; also absent: TOX3, CEACAM5, MUC5AC |
| [[FBXO39]] | 5 µM | B | FBXO39 activity raises the cells' numbers under HI-TOPK-032 5 µM (protects the cells) | lines that do not express FBXO39 (16) vs lines expressing it (32) | the lines without FBXO39: 0.89× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; also absent: XAF1, TRIM22, SLC15A3 |
| [[NPNT]] | 0.05 µM | B | NPNT activity raises the cells' numbers under HI-TOPK-032 0.05 µM (protects the cells) | lines that do not express NPNT (33) vs lines expressing it (15) | the lines without NPNT: 0.72× the cells of the other lines | 0.085 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: PRSS8, RAB25, TMPRSS4 |
| [[HS3ST1]] | 0.05 µM | B | HS3ST1 activity raises the cells' numbers under HI-TOPK-032 0.05 µM (protects the cells) | lines that do not express HS3ST1 (31) vs lines expressing it (17) | the lines without HS3ST1: 0.76× the cells of the other lines | 0.089 | ⚠ within organs, on part of the lines; also absent: KLK10, ADGRF1, TMPRSS4 |
| [[ENSG00000287292]] | 0.05 µM | B | ENSG00000287292 activity raises the cells' numbers under HI-TOPK-032 0.05 µM (protects the cells) | lines that do not express ENSG00000287292 (13) vs lines expressing it (35) | the lines without ENSG00000287292: 0.85× the cells of the other lines | 0.091 | ⚠ within organs, on part of the lines; also absent: NR3C2, ENSG00000249631, SATB1; maybe low, not absent |
| [[TGFA]] | 0.05 µM | B | TGFA activity raises the cells' numbers under HI-TOPK-032 0.05 µM (protects the cells) | lines that do not express TGFA (17) vs lines expressing it (31) | the lines without TGFA: 0.77× the cells of the other lines | 0.091 | ⚠ within organs, on part of the lines; also absent: AQP3, ELF3, VIPR1 |
| [[ADAMTS10]] | 0.05 µM | B | ADAMTS10 activity lowers the cells' numbers under HI-TOPK-032 0.05 µM (makes them more sensitive) | lines that do not express ADAMTS10 (27) vs lines expressing it (21) | the lines without ADAMTS10: 1.41× the cells of the other lines | 0.093 | ⚠ within organs, on part of the lines; also absent: TSHZ3, EPHA5-AS1, HECW2; maybe low, not absent |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "HI-TOPK-032"
- `tables/drugdoses.parquet` — dd in 516, 517, 518
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
