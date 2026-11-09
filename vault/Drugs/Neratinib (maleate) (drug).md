---
drug: "Neratinib (maleate)"
type: "drug"
salt_base: "Neratinib"
targets: "EGFR, ERBB2"
moa_fine: "EGFR/ERBB inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "0.5"
max_sig_genes: 513
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Neratinib (maleate)

*EGFR/ERBB inhibitor (inhibitor/antagonist) · targets: EGFR, ERBB2 · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 4 / 513 / 503; best dose 0.5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.46 / 0.57.
> Flags by dose: - / cell-cycle shift / -. ⚠ 0.5 µM: cell-cycle shift (artifact flags: its changes there are shown with an alert, not left out).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 04]]:G6 | 4 / 0 | — | +0.34 | +0.2/+0.3/+0.0 | — |
| 0.5 µM | [[Plate 05]]:G6 | 308 / 205 | — | -0.33 | -4.8/-3.6/+0.2 | ⚠ cell-cycle shift |
| 5 µM | [[Plate 14]]:G6 | 197 / 306 | 0.860 | +0.22 | -5.6/-4.3/-0.8 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (4 genes, none with an alert): [[PSAT1]] 1.27× (z +3.1, 13/40 lines), [[ALKBH2]] 1.27× (z +3.0, 3/46 lines), [[PHGDH]] 1.26× (z +2.8, 11/43 lines), [[BEND6]] 1.33× (z +2.8, 0/32 lines)

**0.5 µM** (308 genes, 99 with an alert ⚠; the drug-dose carries ⚠ cell-cycle shift; 12 shown): [[PSAT1]] 2.73× (z +12.9, 38/40 lines; cell-cycle shift (explains ~0% here)), [[ASNS]] 2.70× (z +12.8, 44/44 lines; cell-cycle shift (explains ~1% here)), [[YARS1]] 1.76× (z +12.2, 44/48 lines; cell-cycle shift (explains ~0% here)), [[TRIB3]] 2.38× (z +12.2, 42/44 lines; cell-cycle shift (explains ~16% here)), [[XPOT]] 1.76× (z +11.7, 46/48 lines; cell-cycle shift (explains ~10% here)), [[CARS1]] 1.76× (z +11.6, 43/48 lines; cell-cycle shift (explains ~6% here)), [[PCK2]] 2.27× (z +11.4, 35/44 lines; cell-cycle shift (explains ~10% here)), [[NIBAN1]] 2.00× (z +11.3, 32/37 lines; cell-cycle shift (explains ~7% here)), [[PHGDH]] 2.55× (z +11.3, 41/43 lines; cell-cycle shift (explains ~0% here)), [[SLC7A1]] 1.58× (z +11.2, 40/47 lines; cell-cycle shift (explains ~6% here)), [[MARS1]] 1.88× (z +10.7, 47/48 lines; cell-cycle shift (explains ~0% here)), [[JDP2]] 2.01× (z +9.9, 24/34 lines; cell-cycle shift (explains ~20% here))

**5 µM** (197 genes, none with an alert; 12 shown): [[ASNS]] 1.96× (z +12.3, 40/44 lines), [[PSAT1]] 1.95× (z +12.1, 37/40 lines), [[NIBAN1]] 1.67× (z +11.4, 32/37 lines), [[YARS1]] 1.41× (z +10.5, 36/48 lines), [[CARS1]] 1.44× (z +10.4, 39/48 lines), [[XPOT]] 1.42× (z +10.3, 43/48 lines), [[SLC1A4]] 1.53× (z +9.8, 30/44 lines), [[CEBPG]] 1.56× (z +9.4, 43/48 lines), [[SLC25A53]] 1.31× (z +9.3, 33/48 lines), [[TOM1L1]] 1.24× (z +9.3, 28/48 lines), [[PCK2]] 1.59× (z +9.1, 31/47 lines), [[ANK2]] 1.60× (z +8.9, 28/32 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (205 genes, 161 with an alert ⚠; the drug-dose carries ⚠ cell-cycle shift; 22 shown): [[DEPDC1B]] ⚠ 0.708× (z -6.7, 24/48 lines; cell-cycle shift, explains ~44% of this change), [[ESPL1]] ⚠ 0.662× (z -6.4, 25/45 lines; cell-cycle shift, explains ~27% of this change), [[ATAD5]] ⚠ 0.708× (z -6.2, 33/48 lines; cell-cycle shift, explains ~51% of this change), [[PHTF2]] ⚠ 0.822× (z -6.0, 22/48 lines; cell-cycle shift, explains ~20% of this change), [[WDR62]] ⚠ 0.669× (z -5.9, 28/44 lines; cell-cycle shift, explains ~59% of this change), [[RRM2]] ⚠ 0.615× (z -5.8, 39/45 lines; cell-cycle shift, explains ~64% of this change), [[BCKDHA]] 0.721× (z -5.8, 24/47 lines; cell-cycle shift (explains ~0% here)), [[MPHOSPH9]] ⚠ 0.804× (z -5.7, 21/48 lines; cell-cycle shift, explains ~25% of this change), [[PLA2G4A]] 0.721× (z -5.7, 14/26 lines; cell-cycle shift (explains ~3% here)), [[ZGRF1]] ⚠ 0.764× (z -5.4, 21/48 lines; cell-cycle shift, explains ~57% of this change), [[RAD51AP1]] ⚠ 0.668× (z -5.4, 26/45 lines; cell-cycle shift, explains ~63% of this change), [[MASTL]] ⚠ 0.747× (z -5.3, 29/48 lines; cell-cycle shift, explains ~41% of this change), [[WDPCP]] 0.818× (z -4.6, 25/47 lines; cell-cycle shift (explains ~0% here)), [[TUBGCP3]] 0.753× (z -4.6, 28/48 lines; cell-cycle shift (explains ~2% here)), [[ENSG00000285897]] 0.676× (z -4.3, 12/21 lines; cell-cycle shift (explains ~1% here)), [[SFMBT2]] 0.792× (z -4.3, 11/27 lines; cell-cycle shift (explains ~0% here)), [[SLC39A8]] 0.809× (z -4.2, 14/36 lines; cell-cycle shift (explains ~4% here)), [[PHF10]] 0.827× (z -4.2, 21/48 lines; cell-cycle shift (explains ~0% here)), [[MAN2C1]] 0.764× (z -4.1, 17/47 lines; cell-cycle shift (explains ~0% here)), [[LINC00511]] 0.761× (z -4.1, 24/36 lines; cell-cycle shift (explains ~0% here)), [[IL4I1]] 0.803× (z -4.1, 13/46 lines; cell-cycle shift (explains ~0% here)), [[TGFB2]] 0.801× (z -4.0, 16/32 lines; cell-cycle shift (explains ~0% here))

**5 µM** (306 genes, none with an alert; 12 shown): [[PLA2G4A]] 0.742× (z -7.4, 14/26 lines), [[RRM2]] 0.658× (z -6.9, 36/45 lines), [[ATAD2]] 0.788× (z -6.4, 30/47 lines), [[KIF15]] 0.780× (z -6.4, 24/47 lines), [[SPC25]] 0.746× (z -6.1, 30/47 lines), [[NCAPH]] 0.758× (z -6.1, 31/47 lines), [[TGFB2]] 0.791× (z -6.0, 20/33 lines), [[TCF4]] 0.763× (z -6.0, 14/23 lines), [[EXO1]] 0.721× (z -6.0, 25/46 lines), [[EHF]] 0.788× (z -5.9, 14/21 lines), [[TESC]] 0.702× (z -5.9, 11/25 lines), [[HCP5]] 0.694× (z -5.9, 17/24 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | [[Module 179]] (-2.1) |
| 0.5 µM | [[Module 063]] (+5.4), [[Module 133]] (+5.4), [[Module 211]] (+2.1) | [[Module 006]] (-3.1), [[Module 179]] (-2.6), [[Module 067]] (-2.5) |
| 5 µM | [[Module 133]] (+4.7), [[Module 063]] (+4.7), [[Module 170]] (+2.8) | [[Module 235]] (-3.4), [[Module 006]] (-3.0), [[Module 067]] (-2.5) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | [[Hs 766T (line)]] (1.40), [[NCI-H2030 (line)]] (1.37), [[SNU-1 (line)]] (1.36), [[NCI-H460 (line)]] (1.35) · weakest: [[PANC-1 (line)]] (0.461), [[NCI-H661 (line)]] (0.564), [[AsPC-1 (line)]] (0.632) |
| 5 µM | [[BT-474 (line)]] (-4.0), [[SK-MEL-2 (line)]] (-3.5) | [[Hs 766T (line)]] (1.44), [[HCT15 (line)]] (1.39), [[H4 (line)]] (1.36), [[A-172 (line)]] (1.32) · weakest: [[PANC-1 (line)]] (0.618), [[CHP-212 (line)]] (0.672), [[HepG2_C3A (line)]] (0.721) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

⚠ This drug's own vector: vector dose flagged: cell-cycle shift. Read its neighbours with that in mind.

*378 other drugs have a vector, 121 with an alert ⚠; shown: the 8 most similar and the 2 next most similar without an alert.*

- [[Neratinib (drug)]] (+0.80, EGFR/ERBB inhibitor); [[Belumosudil (mesylate) (drug)]] (+0.65, unclear); [[Chlorhexidine (diacetate) (drug)]] (+0.57, unclear); [[5-Azacytidine (drug)]] (+0.55, DNA methyltransferase inhibitor); [[Artesunate (drug)]] (+0.53, JAK/STAT inhibitor, ⚠ vector dose flagged: cell-cycle shift); [[Vinblastine (sulfate) (drug)]] (+0.52, Microtubule inhibitor); [[Adagrasib (drug)]] (+0.49, RAS inhibitor); [[Pitavastatin (Calcium) (drug)]] (+0.46, unclear, ⚠ vector dose flagged: cell-cycle shift); [[Temsirolimus (drug)]] (+0.44, MTOR inhibitor); [[Dihydroartemisinin (drug)]] (+0.44, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 16 arrows, 16 of them with an alert ⚠; grade A 0, B 11, C 5. Shown: the 15 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[MGAM2]] | 0.5 µM | B | MGAM2 activity lowers the cells' numbers under Neratinib (maleate) 0.5 µM (makes them more sensitive) | lines that do not express MGAM2 (33) vs lines expressing it (15) | the lines without MGAM2: 1.19× the cells of the other lines | 0.036 | ⚠ within organs, on part of the lines; also absent: ENSG00000254261, CDH17, LYZ |
| [[FXYD3]] | 0.05 µM | B | FXYD3 activity lowers the cells' numbers under Neratinib (maleate) 0.05 µM (makes them more sensitive) | lines that do not express FXYD3 (34) vs lines expressing it (14) | the lines without FXYD3: 1.19× the cells of the other lines | 0.068 | ⚠ within organs, on part of the lines; also absent: CEACAM6, TMEM30B, TMPRSS2 |
| [[MPZL2]] | 0.05 µM | B | MPZL2 activity lowers the cells' numbers under Neratinib (maleate) 0.05 µM (makes them more sensitive) | lines that do not express MPZL2 (29) vs lines expressing it (19) | the lines without MPZL2: 1.18× the cells of the other lines | 0.069 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, IRF6, ST14 |
| [[KCNH8]] | 0.05 µM | B | KCNH8 activity lowers the cells' numbers under Neratinib (maleate) 0.05 µM (makes them more sensitive) | lines that do not express KCNH8 (32) vs lines expressing it (16) | the lines without KCNH8: 1.19× the cells of the other lines | 0.073 | ⚠ within organs, on part of the lines; also absent: SLC5A1, VWA2, ANKRD22 |
| [[PAX2]] | 0.05 µM | B | PAX2 activity raises the cells' numbers under Neratinib (maleate) 0.05 µM (protects the cells) | lines that do not express PAX2 (33) vs lines expressing it (15) | the lines without PAX2: 0.86× the cells of the other lines | 0.078 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PREX2, LINC02643, ADD2 |
| [[LINC02306]] | 0.5 µM | B | LINC02306 activity lowers the cells' numbers under Neratinib (maleate) 0.5 µM (makes them more sensitive) | lines that do not express LINC02306 (13) vs lines expressing it (35) | the lines without LINC02306: 1.18× the cells of the other lines | 0.091 | ⚠ within organs, on part of the lines; also absent: KCNMB2, COP1-DT, LINC02398; maybe low, not absent |
| [[MGC32805]] | 0.5 µM | B | MGC32805 activity lowers the cells' numbers under Neratinib (maleate) 0.5 µM (makes them more sensitive) | lines that do not express MGC32805 (32) vs lines expressing it (16) | the lines without MGC32805: 1.21× the cells of the other lines | 0.091 | ⚠ within organs, on part of the lines; also absent: CEACAM5, ST18, PRR15L; maybe low, not absent |
| [[VIL1]] | 0.05 µM | B | VIL1 activity lowers the cells' numbers under Neratinib (maleate) 0.05 µM (makes them more sensitive) | lines that do not express VIL1 (34) vs lines expressing it (14) | the lines without VIL1: 1.16× the cells of the other lines | 0.093 | ⚠ within organs, on part of the lines; also absent: LINC02964, NPSR1-AS1, MOGAT3; maybe low, not absent |
| [[TRIM29]] | 0.05 µM | B | TRIM29 activity lowers the cells' numbers under Neratinib (maleate) 0.05 µM (makes them more sensitive) | lines that do not express TRIM29 (28) vs lines expressing it (20) | the lines without TRIM29: 1.16× the cells of the other lines | 0.095 | ⚠ within organs, on part of the lines; also absent: CDH1, IRF6, TNNT2 |
| [[ENSG00000287292]] | 0.05 µM | B | ENSG00000287292 activity lowers the cells' numbers under Neratinib (maleate) 0.05 µM (makes them more sensitive) | lines that do not express ENSG00000287292 (13) vs lines expressing it (35) | the lines without ENSG00000287292: 1.10× the cells of the other lines | 0.095 | ⚠ within organs, on part of the lines; also absent: NR3C2, ENSG00000249631, SATB1; maybe low, not absent |
| [[MOGAT3]] | 0.05 µM | B | MOGAT3 activity lowers the cells' numbers under Neratinib (maleate) 0.05 µM (makes them more sensitive) | lines that do not express MOGAT3 (30) vs lines expressing it (18) | the lines without MOGAT3: 1.15× the cells of the other lines | 0.097 | ⚠ within organs, on part of the lines; also absent: VIL1, LINC02964, LINC01819 |
| [[IFT74]] | 5 µM | C | IFT74 activity raises the cells' numbers under Neratinib (maleate) 5 µM (protects the cells) | lines that do not express IFT74 (3) vs lines expressing it (45) | the lines without IFT74: 0.81× the cells of the other lines | 0.017 | ⚠ few lines (3 vs 47); across organs; also absent: LCA5, P3H4, TOMM40L; maybe low, not absent |
| [[OPLAH]] | 5 µM | C | OPLAH activity raises the cells' numbers under Neratinib (maleate) 5 µM (protects the cells) | lines that do not express OPLAH (10) vs lines expressing it (38) | the lines without OPLAH: 0.89× the cells of the other lines | 0.028 | ⚠ tissue-confounded; across organs; co-occurs with TERT; also absent: TNFRSF10D, PATJ, EPHX2 |
| [[ITPK1]] | 0.05 µM | C | ITPK1 activity lowers the cells' numbers under Neratinib (maleate) 0.05 µM (makes them more sensitive) | lines that do not express ITPK1 (4) vs lines expressing it (44) | the lines without ITPK1: 1.26× the cells of the other lines | 0.055 | ⚠ few lines (4 vs 46); across organs; also absent: ENSG00000253796; maybe low, not absent |
| [[SVIL]] | 5 µM | C | SVIL activity raises the cells' numbers under Neratinib (maleate) 5 µM (protects the cells) | lines that do not express SVIL (3) vs lines expressing it (45) | the lines without SVIL: 0.83× the cells of the other lines | 0.067 | ⚠ few lines (3 vs 47); across organs; also absent: DBN1, LAMC1, PLEC; maybe low, not absent |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Neratinib (maleate)"
- `tables/drugdoses.parquet` — dd in 714, 715, 716
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
