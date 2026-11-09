---
drug: "Pitavastatin (Calcium)"
type: "drug"
salt_base: "Pitavastatin"
targets: "HMGCR"
moa_fine: "unclear"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 1158
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Pitavastatin (Calcium)

*unclear (inhibitor/antagonist) · targets: HMGCR · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 35 / 864 / 1158; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.05 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.52 / 0.83.
> Flags by dose: - / low cells (technical?) / cell-cycle shift. ⚠ 5 µM: cell-cycle shift (artifact flags: its changes there are shown with an alert, not left out).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 07]]:D8 | 25 / 10 | — | -0.44 | -0.7/-0.5/-0.1 | — |
| 0.5 µM | [[Plate 08]]:D8 | 602 / 262 | — | -1.29 | -4.1/-2.2/-1.9 | low cells (technical?) |
| 5 µM | [[Plate 09]]:D8 | 716 / 442 | — | -0.83 | -4.3/-1.7/-1.3 | ⚠ cell-cycle shift |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (25 genes, none with an alert; 12 shown): [[RHOB]] 1.98× (z +7.0, 36/46 lines), [[KRAS]] 1.29× (z +5.5, 28/47 lines), [[KLF2]] 2.18× (z +4.9, 28/41 lines), [[RHOA]] 1.23× (z +4.7, 24/47 lines), [[TSC22D3]] 1.75× (z +4.3, 15/35 lines), [[LINC01611]] 1.55× (z +4.2, 1/12 lines), [[YWHAH]] 1.40× (z +4.1, 28/47 lines), [[ENSG00000225339]] 1.45× (z +4.1, 14/46 lines), [[ARHGEF4]] 1.31× (z +3.9, 12/33 lines), [[RDH13]] 1.21× (z +3.9, 11/46 lines), [[TMOD1]] 1.29× (z +3.6, 5/32 lines), [[RAPGEFL1]] 1.30× (z +3.5, 10/45 lines)

**0.5 µM** (602 genes, none with an alert; 12 shown): [[RHOB]] 3.92× (z +15.2, 44/46 lines), [[RHOA]] 1.80× (z +14.1, 45/47 lines), [[DUSP16]] 1.68× (z +11.5, 40/45 lines), [[YWHAH]] 2.29× (z +10.9, 42/47 lines), [[KRAS]] 1.54× (z +10.2, 40/47 lines), [[CREB5]] 1.76× (z +9.9, 26/32 lines), [[ATP2B4]] 1.55× (z +9.4, 29/39 lines), [[KRTAP5-AS1]] 2.61× (z +9.4, 21/32 lines), [[TSC22D3]] 3.03× (z +9.3, 32/35 lines), [[KLF3]] 1.58× (z +9.3, 37/47 lines), [[KLF2]] 4.17× (z +9.2, 38/43 lines), [[TCTA]] 1.97× (z +9.1, 35/45 lines)

**5 µM** (716 genes, 310 with an alert ⚠; the drug-dose carries ⚠ cell-cycle shift; 13 shown): [[RHOB]] 4.99× (z +17.2, 46/46 lines; cell-cycle shift (explains ~1% here)), [[RHOA]] 1.89× (z +14.8, 47/47 lines; cell-cycle shift (explains ~0% here)), [[CREB5]] 2.23× (z +13.5, 27/32 lines; cell-cycle shift (explains ~0% here)), [[KRAS]] 1.73× (z +12.5, 42/47 lines; cell-cycle shift (explains ~5% here)), [[DUSP16]] 1.78× (z +12.2, 42/45 lines; cell-cycle shift (explains ~13% here)), [[KRTAP5-AS1]] 3.23× (z +11.0, 23/30 lines; cell-cycle shift (explains ~5% here)), [[ATP2B4]] 1.71× (z +11.0, 32/39 lines; cell-cycle shift (explains ~2% here)), [[YWHAH]] 2.36× (z +10.9, 44/47 lines; cell-cycle shift (explains ~0% here)), [[KLF2]] 5.19× (z +10.9, 40/40 lines; cell-cycle shift (explains ~4% here)), [[DLGAP4]] 1.55× (z +9.8, 33/47 lines; cell-cycle shift (explains ~12% here)), [[ENSG00000225339]] 2.32× (z +9.6, 35/45 lines; cell-cycle shift (explains ~0% here)), [[MAP4]] ⚠ 1.31× (z +9.5, 34/46 lines; cell-cycle shift, explains ~17% of this change), [[TSC22D3]] 3.17× (z +9.3, 34/35 lines; cell-cycle shift (explains ~10% here))

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (10 genes, none with an alert): [[CCN1]] 0.593× (z -5.4, 28/40 lines), [[CCN2]] 0.567× (z -4.8, 16/30 lines), [[TGFB2]] 0.770× (z -4.4, 10/32 lines), [[AMOTL2]] 0.733× (z -4.3, 19/43 lines), [[LATS2]] 0.799× (z -3.8, 19/46 lines), [[ENSG00000283674]] 0.808× (z -3.4, 9/31 lines), [[GPR176]] 0.803× (z -3.2, 9/29 lines), [[PNMA2]] 0.799× (z -3.1, 4/29 lines), [[ENSG00000264808]] 0.739× (z -2.9, 6/39 lines), [[MMP17]] 0.762× (z -2.9, 5/24 lines)

**0.5 µM** (262 genes, none with an alert; 12 shown): [[DLC1]] 0.627× (z -10.9, 27/33 lines), [[AMOTL2]] 0.543× (z -9.2, 34/43 lines), [[CCN2]] 0.313× (z -9.2, 23/30 lines), [[CCN1]] 0.443× (z -9.0, 36/40 lines), [[BDNF]] 0.616× (z -7.4, 20/28 lines), [[AJUBA]] 0.582× (z -6.9, 25/45 lines), [[WWC1]] 0.771× (z -6.9, 20/35 lines), [[LATS2]] 0.700× (z -6.5, 30/46 lines), [[ARHGAP18]] 0.733× (z -6.3, 24/41 lines), [[ZNHIT6]] 0.785× (z -6.0, 28/46 lines), [[GPR176]] 0.686× (z -6.0, 16/29 lines), [[TGFB2]] 0.717× (z -6.0, 17/32 lines)

**5 µM** (442 genes, 215 with an alert ⚠; the drug-dose carries ⚠ cell-cycle shift; 12 shown): [[CCN2]] 0.244× (z -12.4, 25/29 lines; cell-cycle shift (explains ~7% here)), [[DLC1]] 0.587× (z -11.9, 31/33 lines; cell-cycle shift (explains ~4% here)), [[AMOTL2]] 0.473× (z -10.9, 36/43 lines; cell-cycle shift (explains ~0% here)), [[CCN1]] 0.408× (z -9.5, 36/40 lines; cell-cycle shift (explains ~5% here)), [[SLFN12]] 0.509× (z -7.7, 14/23 lines; cell-cycle shift (explains ~11% here)), [[BDNF]] 0.594× (z -7.6, 20/28 lines; cell-cycle shift (explains ~2% here)), [[AJUBA]] 0.544× (z -7.5, 33/44 lines; cell-cycle shift (explains ~0% here)), [[WWC1]] 0.751× (z -7.3, 23/35 lines; cell-cycle shift (explains ~6% here)), [[LATS2]] 0.676× (z -6.9, 32/46 lines; cell-cycle shift (explains ~0% here)), [[ETV1]] 0.562× (z -6.9, 29/36 lines; cell-cycle shift (explains ~12% here)), [[THBS1]] 0.515× (z -6.7, 20/33 lines; cell-cycle shift (explains ~13% here)), [[ARHGAP18]] 0.710× (z -6.7, 27/41 lines; cell-cycle shift (explains ~21% here))

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | [[Module 208]] (+4.5), [[Module 136]] (+2.9), [[Module 227]] (+2.8) | [[Module 006]] (-3.7), [[Module 001]] (-2.5), [[Module 005]] (-2.4) |
| 5 µM | [[Module 208]] (+4.3), [[Module 227]] (+3.5), [[Module 234]] (+3.3) | [[Module 006]] (-3.6), [[Module 001]] (-2.7), [[Module 005]] (-2.6) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | [[C-33 A (line)]] (1.91), [[A-172 (line)]] (1.79), [[MIA PaCa-2 (line)]] (1.71), [[SK-MEL-2 (line)]] (1.70) · weakest: [[BT-474 (line)]] (-0.0202), [[KATO III (line)]] (0.133), [[NCI-H661 (line)]] (0.300) |
| 0.5 µM | [[HOP62 (line)]] (-5.8), [[SNU-423 (line)]] (-5.7), [[A498 (line)]] (-4.2), [[HS-578T (line)]] (-3.5), [[SW 900 (line)]] (-3.0) | [[H4 (line)]] (1.98), [[SK-MEL-2 (line)]] (1.64), [[SW48 (line)]] (1.55), [[NCI-H2030 (line)]] (1.49) · weakest: [[BT-474 (line)]] (0.414), [[HepG2_C3A (line)]] (0.489), [[NCI-H661 (line)]] (0.538) |
| 5 µM | [[HOP62 (line)]] (-3.4), [[NCI-H1792 (line)]] (-3.2) | [[H4 (line)]] (1.99), [[NCI-H460 (line)]] (1.58), [[SK-MEL-2 (line)]] (1.43), [[HOP62 (line)]] (1.37) · weakest: [[NCI-H2347 (line)]] (0.404), [[BT-474 (line)]] (0.420), [[CHP-212 (line)]] (0.595) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

⚠ This drug's own vector: vector dose flagged: cell-cycle shift. Read its neighbours with that in mind.

*378 other drugs have a vector, 121 with an alert ⚠; shown: the 8 most similar and the 2 next most similar without an alert.*

- [[Neratinib (drug)]] (+0.49, EGFR/ERBB inhibitor); [[Cyclosporin A (drug)]] (+0.48, unclear); [[Neratinib (maleate) (drug)]] (+0.46, EGFR/ERBB inhibitor, ⚠ vector dose flagged: cell-cycle shift); [[RMC-6236 (drug)]] (+0.44, RAS inhibitor); [[Daptomycin (drug)]] (+0.41, unclear, ⚠ no trustworthy dose (vector dose flagged: unreliable plate only)); [[Vinblastine (sulfate) (drug)]] (+0.39, Microtubule inhibitor); [[BI-3406 (drug)]] (+0.39, RAS inhibitor); [[Entrectinib (drug)]] (+0.37, Other TK inhibitor); [[Crizotinib (hydrochloride) (drug)]] (+0.37, Multi-TK inhibitor); [[GSK1059615 (drug)]] (+0.35, PI3K/AKT inhibitor)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 21 arrows, 21 of them with an alert ⚠; grade A 0, B 11, C 10. Shown: the 15 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[CYP1B1-AS1]] | 5 µM | B | CYP1B1-AS1 activity lowers the cells' numbers under Pitavastatin (Calcium) 5 µM (makes them more sensitive) | lines that do not express CYP1B1-AS1 (14) vs lines expressing it (34) | the lines without CYP1B1-AS1: 1.21× the cells of the other lines | 0.037 | ⚠ within organs, on part of the lines; also absent: KCNMA1, ENOX1, PDGFC; maybe low, not absent |
| [[KCNMA1]] | 5 µM | B | KCNMA1 activity lowers the cells' numbers under Pitavastatin (Calcium) 5 µM (makes them more sensitive) | lines that do not express KCNMA1 (26) vs lines expressing it (22) | the lines without KCNMA1: 1.30× the cells of the other lines | 0.046 | ⚠ within organs, on part of the lines; also absent: F2RL2, SIRLNT, SRGN |
| [[EPPK1]] | 5 µM | B | EPPK1 activity raises the cells' numbers under Pitavastatin (Calcium) 5 µM (protects the cells) | lines that do not express EPPK1 (25) vs lines expressing it (23) | the lines without EPPK1: 0.80× the cells of the other lines | 0.068 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, EPCAM, CLDN3 |
| [[CLDN3]] | 5 µM | B | CLDN3 activity raises the cells' numbers under Pitavastatin (Calcium) 5 µM (protects the cells) | lines that do not express CLDN3 (28) vs lines expressing it (20) | the lines without CLDN3: 0.79× the cells of the other lines | 0.075 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, EPCAM, ESRP1 |
| [[EPCAM]] | 5 µM | B | EPCAM activity raises the cells' numbers under Pitavastatin (Calcium) 5 µM (protects the cells) | lines that do not express EPCAM (28) vs lines expressing it (20) | the lines without EPCAM: 0.77× the cells of the other lines | 0.077 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, KDF1, CLDN3 |
| [[CGN]] | 5 µM | B | CGN activity raises the cells' numbers under Pitavastatin (Calcium) 5 µM (protects the cells) | lines that do not express CGN (21) vs lines expressing it (27) | the lines without CGN: 0.76× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, CRACDL, CAMSAP3 |
| [[HTR1F]] | 5 µM | B | HTR1F activity lowers the cells' numbers under Pitavastatin (Calcium) 5 µM (makes them more sensitive) | lines that do not express HTR1F (34) vs lines expressing it (14) | the lines without HTR1F: 1.26× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MGP, TIMP3, AEBP1; maybe low, not absent |
| [[RASSF8]] | 5 µM | B | RASSF8 activity lowers the cells' numbers under Pitavastatin (Calcium) 5 µM (makes them more sensitive) | lines that do not express RASSF8 (15) vs lines expressing it (33) | the lines without RASSF8: 1.30× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; also absent: RASSF8-AS1, KCNG1, B4GALNT1 |
| [[RASSF8-AS1]] | 5 µM | B | RASSF8-AS1 activity lowers the cells' numbers under Pitavastatin (Calcium) 5 µM (makes them more sensitive) | lines that do not express RASSF8-AS1 (14) vs lines expressing it (34) | the lines without RASSF8-AS1: 1.28× the cells of the other lines | 0.089 | ⚠ within organs, on part of the lines; also absent: RASSF8, B4GALNT1, ENSG00000285804 |
| [[SPINT1-AS1]] | 5 µM | B | SPINT1-AS1 activity raises the cells' numbers under Pitavastatin (Calcium) 5 µM (protects the cells) | lines that do not express SPINT1-AS1 (27) vs lines expressing it (21) | the lines without SPINT1-AS1: 0.77× the cells of the other lines | 0.096 | ⚠ within organs, on part of the lines; also absent: EPCAM, CLDN3, CRB3 |
| [[JUP]] | 5 µM | B | JUP activity raises the cells' numbers under Pitavastatin (Calcium) 5 µM (protects the cells) | lines that do not express JUP (16) vs lines expressing it (32) | the lines without JUP: 0.82× the cells of the other lines | 0.098 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: ELF3, SHROOM3, ENSG00000253671 |
| [[SCAMP5]] | 5 µM | C | SCAMP5 activity raises the cells' numbers under Pitavastatin (Calcium) 5 µM (protects the cells) | lines that do not express SCAMP5 (3) vs lines expressing it (45) | the lines without SCAMP5: 0.70× the cells of the other lines | 0.026 | ⚠ few lines (3 vs 47); across organs; also absent: ENSG00000262160, SLC4A11, CORO2A; maybe low, not absent |
| [[ITPK1]] | 0.5 µM | C | ITPK1 activity raises the cells' numbers under Pitavastatin (Calcium) 0.5 µM (protects the cells) | lines that do not express ITPK1 (4) vs lines expressing it (44) | the lines without ITPK1: 0.65× the cells of the other lines | 0.028 | ⚠ few lines (4 vs 46); across organs; also absent: ENSG00000253796; maybe low, not absent |
| [[ENSG00000286964]] | 5 µM | C | ENSG00000286964 activity lowers the cells' numbers under Pitavastatin (Calcium) 5 µM (makes them more sensitive) | lines that do not express ENSG00000286964 (10) vs lines expressing it (38) | the lines without ENSG00000286964: 1.23× the cells of the other lines | 0.059 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: SIX1, C2orf74, SYDE1 |
| [[SCAMP5]] | 0.5 µM | C | SCAMP5 activity raises the cells' numbers under Pitavastatin (Calcium) 0.5 µM (protects the cells) | lines that do not express SCAMP5 (3) vs lines expressing it (45) | the lines without SCAMP5: 0.61× the cells of the other lines | 0.068 | ⚠ few lines (3 vs 47); across organs; also absent: ENSG00000262160, SLC4A11, CORO2A; maybe low, not absent |

### Its targets: what acting on them probably does

*Drug-target arrows of the compound classes it belongs to (compounds sharing a listed target and mechanism; one molecule counts once, under all its names): the target → a gene whose level those compounds move. A row that names several targets is one test: the compounds share them all, and any of them could be the cause. 4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Its target | Gene it moves | This drug | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|---|
| [[HMGCR]] | [[PMP22]] | moves it that way too | B | HMGCR activity lowers PMP22's level | compounds that target HMGCR: 2 of 2 raise it (Pitavastatin, Pravastatin) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds |
| [[HMGCR]] | [[IQCD]] | moves it that way too | B | HMGCR activity raises IQCD's level | compounds that target HMGCR: 2 of 2 lower it (Pitavastatin, Pravastatin) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[HMGCR]] | [[NDRG1]] | moves it that way too | B | HMGCR activity lowers NDRG1's level | compounds that target HMGCR: 2 of 2 raise it (Pitavastatin, Pravastatin) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds |
| [[HMGCR]] | [[SLC35G1]] | moves it that way too | B | HMGCR activity raises SLC35G1's level | compounds that target HMGCR: 2 of 2 lower it (Pitavastatin, Pravastatin) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

## Data

- `tables/drugs.parquet` — drug == "Pitavastatin (Calcium)"
- `tables/drugdoses.parquet` — dd in 824, 825, 826
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
