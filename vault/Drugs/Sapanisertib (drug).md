---
drug: "Sapanisertib"
type: "drug"
salt_base: "Sapanisertib"
targets: "MTOR"
moa_fine: "MTOR inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "no"
doses: ["0.05", "0.5", "5"]
best_dose: "0.5"
max_sig_genes: 842
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Sapanisertib

*MTOR inhibitor (inhibitor/antagonist) · targets: MTOR · approved: no*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 328 / 842 / 232; best dose 0.5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.05 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): -0.30 / -0.52.
> Flags by dose: cell-cycle shift / plate-row cell shift; noisy plate (z scaled) / plate-row cell shift; noisy plate (z scaled). ⚠ 0.05 µM: cell-cycle shift (artifact flags: its changes there are shown with an alert, not left out).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 01]]:D7 | 150 / 178 | — | +0.42 | -4.2/-3.4/-2.7 | ⚠ cell-cycle shift |
| 0.5 µM | [[Plate 02]]:D7 | 455 / 387 | — | -0.50 | -0.2/-0.7/+1.7 | plate-row cell shift; noisy plate (z scaled) |
| 5 µM | [[Plate 03]]:D7 | 119 / 113 | — | +1.55 | -2.2/-2.2/-2.5 | plate-row cell shift; noisy plate (z scaled) |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (150 genes, 104 with an alert ⚠; the drug-dose carries ⚠ cell-cycle shift; 23 shown): [[DHRSX]] ⚠ 1.24× (z +5.0, 27/47 lines; cell-cycle shift, explains ~46% of this change), [[TOP1MT]] 1.29× (z +4.7, 9/48 lines; cell-cycle shift (explains ~10% here)), [[MTA1]] ⚠ 1.24× (z +4.6, 15/48 lines; cell-cycle shift, explains ~19% of this change), [[SHC2]] ⚠ 1.56× (z +4.6, 12/40 lines; cell-cycle shift, explains ~51% of this change), [[SUPT3H]] ⚠ 1.31× (z +4.5, 33/47 lines; cell-cycle shift, explains ~58% of this change), [[MYO1D]] ⚠ 1.21× (z +4.5, 15/35 lines; cell-cycle shift, explains ~28% of this change), [[CSNK1D]] ⚠ 1.22× (z +4.4, 24/48 lines; cell-cycle shift, explains ~10% of this change), [[SLC25A53]] ⚠ 1.21× (z +4.4, 7/48 lines; cell-cycle shift, explains ~31% of this change), [[VAC14]] ⚠ 1.31× (z +4.3, 20/48 lines; cell-cycle shift, explains ~19% of this change), [[SCMH1]] ⚠ 1.26× (z +4.2, 30/48 lines; cell-cycle shift, explains ~38% of this change), [[PTPRE]] ⚠ 1.32× (z +4.2, 18/35 lines; cell-cycle shift, explains ~27% of this change), [[MLPH]] ⚠ 1.36× (z +4.2, 22/35 lines; cell-cycle shift, explains ~44% of this change), [[NAV2]] 1.34× (z +4.1, 19/31 lines; cell-cycle shift (explains ~12% here)), [[MSRA]] 1.34× (z +4.0, 16/46 lines; cell-cycle shift (explains ~4% here)), [[FLNA]] 1.44× (z +4.0, 36/47 lines; cell-cycle shift (explains ~0% here)), [[EPHB2]] 1.22× (z +4.0, 14/41 lines; cell-cycle shift (explains ~2% here)), [[NSMF]] 1.43× (z +3.9, 21/46 lines; cell-cycle shift (explains ~0% here)), [[ABTB1]] 1.52× (z +3.9, 8/46 lines; cell-cycle shift (explains ~23% here)), [[USP2-AS1]] 1.32× (z +3.8, 10/47 lines; cell-cycle shift (explains ~0% here)), [[RBM19]] 1.28× (z +3.8, 20/48 lines; cell-cycle shift (explains ~0% here)), [[MCTP1]] 1.35× (z +3.8, 16/35 lines; cell-cycle shift (explains ~0% here)), [[TPP1]] 1.30× (z +3.8, 17/47 lines; cell-cycle shift (explains ~12% here)), [[ABLIM2]] 1.36× (z +3.8, 13/34 lines; cell-cycle shift (explains ~18% here))

**0.5 µM** (455 genes, none with an alert; 12 shown): [[OSGIN1]] 2.18× (z +6.3, 22/43 lines), [[TRMT1]] 1.74× (z +6.0, 16/45 lines), [[KIF21A]] 1.42× (z +5.7, 33/46 lines), [[PDCD11]] 1.50× (z +5.5, 31/48 lines), [[SNHG17]] 1.75× (z +5.3, 31/48 lines), [[CLUH]] 1.66× (z +5.3, 23/47 lines), [[RABEPK]] 1.58× (z +5.3, 26/48 lines), [[FASTKD1]] 1.35× (z +5.2, 24/48 lines), [[TM9SF4]] 1.26× (z +5.0, 32/48 lines), [[CELF1]] 1.34× (z +4.9, 40/48 lines), [[YARS1]] 1.38× (z +4.9, 27/48 lines), [[SLC25A22]] 1.76× (z +4.9, 15/44 lines)

**5 µM** (119 genes, none with an alert; 12 shown): [[AKAP13]] 1.48× (z +5.1, 37/49 lines), [[NAV2]] 1.77× (z +5.0, 21/32 lines), [[FMNL2]] 1.50× (z +4.9, 29/47 lines), [[TBC1D15]] 1.52× (z +4.5, 34/49 lines), [[SOD2]] 1.85× (z +4.3, 28/46 lines), [[PELI2]] 1.64× (z +4.3, 16/33 lines), [[DHRSX]] 1.40× (z +4.3, 26/48 lines), [[KAT6B]] 1.37× (z +4.2, 28/49 lines), [[CEMIP]] 2.13× (z +4.1, 16/30 lines), [[JAK1]] 1.33× (z +4.1, 21/49 lines), [[KLHL24]] 1.63× (z +4.0, 27/49 lines), [[ARHGEF28]] 1.60× (z +3.9, 23/43 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (178 genes, 149 with an alert ⚠; the drug-dose carries ⚠ cell-cycle shift; 21 shown): [[DTL]] ⚠ 0.661× (z -5.6, 25/48 lines; cell-cycle shift, explains ~68% of this change), [[HELLS]] ⚠ 0.700× (z -5.3, 32/48 lines; cell-cycle shift, explains ~65% of this change), [[SSX2IP]] ⚠ 0.762× (z -5.2, 16/47 lines; cell-cycle shift, explains ~33% of this change), [[ATAD5]] ⚠ 0.747× (z -5.0, 25/48 lines; cell-cycle shift, explains ~56% of this change), [[WDHD1]] ⚠ 0.752× (z -4.9, 16/48 lines; cell-cycle shift, explains ~66% of this change), [[STARD4]] 0.643× (z -4.9, 31/44 lines; cell-cycle shift (explains ~0% here)), [[CDC7]] ⚠ 0.694× (z -4.7, 23/46 lines; cell-cycle shift, explains ~50% of this change), [[GPT2]] 0.732× (z -4.6, 21/46 lines; cell-cycle shift (explains ~0% here)), [[APOO]] ⚠ 0.793× (z -4.6, 11/47 lines; cell-cycle shift, explains ~19% of this change), [[PSAT1]] 0.686× (z -4.6, 18/40 lines; cell-cycle shift (explains ~7% here)), [[POLR3G]] ⚠ 0.751× (z -4.5, 17/45 lines; cell-cycle shift, explains ~41% of this change), [[MCM10]] ⚠ 0.658× (z -4.5, 19/44 lines; cell-cycle shift, explains ~83% of this change), [[FADS2]] 0.758× (z -4.4, 20/48 lines; cell-cycle shift (explains ~16% here)), [[TENT5A]] 0.767× (z -4.4, 19/37 lines; cell-cycle shift (explains ~0% here)), [[GPX8]] 0.691× (z -4.4, 18/40 lines; cell-cycle shift (explains ~4% here)), [[DIXDC1]] 0.793× (z -4.3, 13/48 lines; cell-cycle shift (explains ~1% here)), [[PPP1R3C]] 0.622× (z -4.2, 11/26 lines; cell-cycle shift (explains ~7% here)), [[GXYLT2]] 0.750× (z -4.0, 13/37 lines; cell-cycle shift (explains ~0% here)), [[EPHA3]] 0.679× (z -3.9, 4/22 lines; cell-cycle shift (explains ~4% here)), [[MSMO1]] 0.684× (z -3.9, 26/47 lines; cell-cycle shift (explains ~0% here)), [[PHGDH]] 0.719× (z -3.7, 21/43 lines; cell-cycle shift (explains ~9% here))

**0.5 µM** (387 genes, none with an alert; 12 shown): [[TNRC6B]] 0.705× (z -10.6, 43/48 lines), [[CCDC28A]] 0.491× (z -8.8, 40/48 lines), [[TFDP2]] 0.673× (z -8.8, 42/48 lines), [[PDCD4]] 0.574× (z -8.6, 43/48 lines), [[RB1CC1]] 0.658× (z -7.3, 46/48 lines), [[PHF3]] 0.669× (z -7.0, 46/48 lines), [[GARRE1]] 0.646× (z -6.8, 40/48 lines), [[RBL2]] 0.705× (z -6.3, 35/48 lines), [[TCP11L2]] 0.517× (z -6.2, 39/48 lines), [[CYBRD1]] 0.598× (z -6.0, 22/30 lines), [[CLNS1A]] 0.765× (z -6.0, 29/48 lines), [[PIK3CA]] 0.753× (z -6.0, 29/48 lines)

**5 µM** (113 genes, none with an alert; 12 shown): [[SEPHS1]] 0.703× (z -4.0, 3/48 lines), [[PSAT1]] 0.527× (z -3.9, 13/40 lines), [[ONECUT2]] 0.668× (z -3.8, 3/38 lines), [[EGFL7]] 0.380× (z -3.8, 12/39 lines), [[PRDX2]] 0.347× (z -3.8, 34/39 lines), [[FAM162A]] 0.454× (z -3.8, 42/48 lines), [[NUDT5]] 0.663× (z -3.7, 9/48 lines), [[GGH]] 0.541× (z -3.7, 20/43 lines), [[UBE2T]] 0.457× (z -3.6, 16/47 lines), [[CRABP2]] 0.491× (z -3.6, 11/24 lines), [[SLC16A14]] 0.555× (z -3.6, 4/32 lines), [[GRHL2]] 0.629× (z -3.6, 0/15 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | [[Module 193]] (+2.3), [[Module 230]] (+2.2) | [[Module 065]] (-2.4), [[Module 048]] (-2.3), [[Module 045]] (-2.3) |
| 0.5 µM | [[Module 229]] (+2.4), [[Module 054]] (+2.1), [[Module 125]] (+2.1) | [[Module 225]] (-3.3), [[Module 234]] (-2.9), [[Module 069]] (-2.9) |
| 5 µM | [[Module 225]] (+2.3), [[Module 234]] (+2.3), [[Module 185]] (+2.1) | [[Module 048]] (-2.7), [[Module 058]] (-2.1), [[Module 131]] (-2.0) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | [[Hs 766T (line)]] (1.56), [[MIA PaCa-2 (line)]] (1.54), [[COLO 205 (line)]] (1.38), [[HCT15 (line)]] (1.34) · weakest: [[SW1417 (line)]] (0.525), [[HepG2_C3A (line)]] (0.563), [[NCI-H1792 (line)]] (0.601) |
| 0.5 µM | [[Hs 766T (line)]] (-3.5), [[HCT15 (line)]] (-3.3) | [[NCI-H1792 (line)]] (1.35), [[NCI-H460 (line)]] (1.24), [[LOX-IMVI (line)]] (1.15), [[A498 (line)]] (1.13) · weakest: [[BT-474 (line)]] (0.632), [[LS 180 (line)]] (0.739), [[HS-578T (line)]] (0.740) |
| 5 µM | [[LOX-IMVI (line)]] (-4.3), [[Panc 03.27 (line)]] (-4.1), [[CFPAC-1 (line)]] (-3.2), [[COLO 205 (line)]] (-3.0) | [[Hs 766T (line)]] (1.39), [[H4 (line)]] (1.37), [[SW 1088 (line)]] (1.33), [[NCI-H1573 (line)]] (1.30) · weakest: [[NCI-H2122 (line)]] (0.607), [[SW1417 (line)]] (0.674), [[SW48 (line)]] (0.714) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar.*

- [[venetoclax (drug)]] (+0.68, unclear); [[EX229 (drug)]] (+0.67, unclear); [[Everolimus (drug)]] (+0.62, MTOR inhibitor); [[Ipatasertib (drug)]] (+0.62, PI3K/AKT inhibitor); [[c-Kit-IN-1 (drug)]] (+0.60, Multi-TK inhibitor); [[Methylprednisolone succinate (drug)]] (+0.58, Glucocorticoid receptor agonist); [[Abemaciclib (drug)]] (+0.57, CDK inhibitor); [[Erythromycin (drug)]] (+0.57, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[LINC01583]] | 5 µM | B | LINC01583 activity raises the cells' numbers under Sapanisertib 5 µM (protects the cells) | lines that do not express LINC01583 (28) vs lines expressing it (20) | the lines without LINC01583: 0.78× the cells of the other lines | 0.079 | ⚠ within organs, on part of the lines; also absent: INSYN2B, ADAM12, ZEB2 |
| [[HS3ST3B1]] | 0.5 µM | B | HS3ST3B1 activity lowers the cells' numbers under Sapanisertib 0.5 µM (makes them more sensitive) | lines that do not express HS3ST3B1 (18) vs lines expressing it (30) | the lines without HS3ST3B1: 1.12× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: ENSG00000230647, SRPX, APCDD1L-DT |
| [[PLXNA2]] | 0.5 µM | B | PLXNA2 activity lowers the cells' numbers under Sapanisertib 0.5 µM (makes them more sensitive) | lines that do not express PLXNA2 (15) vs lines expressing it (33) | the lines without PLXNA2: 1.21× the cells of the other lines | 0.089 | ⚠ within organs, on part of the lines; also absent: GATA6, HS3ST3B1, IFI16 |
| [[FAM3B]] | 0.5 µM | B | FAM3B activity lowers the cells' numbers under Sapanisertib 0.5 µM (makes them more sensitive) | lines that do not express FAM3B (12) vs lines expressing it (36) | the lines without FAM3B: 1.25× the cells of the other lines | 0.093 | ⚠ within organs, on part of the lines; also absent: TXNIP, CADPS2, PLAC4; maybe low, not absent |
| [[TREM1]] | 0.5 µM | B | TREM1 activity lowers the cells' numbers under Sapanisertib 0.5 µM (makes them more sensitive) | lines that do not express TREM1 (25) vs lines expressing it (23) | the lines without TREM1: 1.09× the cells of the other lines | 0.095 | ⚠ within organs, on part of the lines; also absent: EDIL3-DT, DTNA, MAF |
| [[CYB561]] | 5 µM | C | CYB561 activity lowers the cells' numbers under Sapanisertib 5 µM (makes them more sensitive) | lines that do not express CYB561 (3) vs lines expressing it (45) | the lines without CYB561: 1.65× the cells of the other lines | 0.094 | ⚠ few lines (3 vs 47); across organs; also absent: MATN1-AS1, E2F8, PBX4; maybe low, not absent |

### Its targets: what acting on them probably does

*Drug-target arrows of the compound classes it belongs to (compounds sharing a listed target and mechanism; one molecule counts once, under all its names): the target → a gene whose level those compounds move. A row that names several targets is one test: the compounds share them all, and any of them could be the cause. 93 arrows, 93 of them with an alert ⚠; grade A 0, B 93, C 0. Shown: the 15 strongest; 78 more arrows (78 of them with an alert ⚠) not shown.*

| Its target | Gene it moves | This drug | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|---|
| [[MTOR]] | [[INSR]] | moves it that way too | B | MTOR activity lowers INSR's level | compounds that target MTOR: 6 of 8 raise it (AZD-8055, Bimiralisib, GSK1059615, Rapamycin, Sapanisertib, Temsirolimus) | 75% of the class's compounds vs 3.4% of all compounds | 0.004 | ⚠ off-target possible; 6 compounds; artifact flags |
| [[MTOR]] | [[FKBP14]] | moves it that way too | B | MTOR activity raises FKBP14's level | compounds that target MTOR: 6 of 8 lower it (AZD-8055, Bimiralisib, GSK1059615, Rapamycin, Sapanisertib, Temsirolimus) | 75% of the class's compounds vs 4.2% of all compounds | 0.005 | ⚠ off-target possible; 6 compounds; artifact flags |
| [[MTOR]] | [[WASHC2C]] | moves it that way too | B | MTOR activity lowers WASHC2C's level | compounds that target MTOR: 6 of 8 raise it (AZD-8055, Bimiralisib, GSK1059615, Rapamycin, Sapanisertib, Temsirolimus) | 75% of the class's compounds vs 5.0% of all compounds | 0.005 | ⚠ off-target possible; 6 compounds; artifact flags |
| [[MTOR]] | [[TSPAN13]] | moves it that way too | B | MTOR activity raises TSPAN13's level | compounds that target MTOR: 5 of 8 lower it (AZD-8055, Bimiralisib, Rapamycin, Sapanisertib, Temsirolimus) | 62% of the class's compounds vs 2.8% of all compounds | 0.006 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[MTOR]] | [[MCM8]] | moves it that way too | B | MTOR activity raises MCM8's level | compounds that target MTOR: 6 of 8 lower it (AZD-8055, Bimiralisib, GSK1059615, Rapamycin, Sapanisertib, Temsirolimus) | 75% of the class's compounds vs 5.6% of all compounds | 0.007 | ⚠ off-target possible; 6 compounds; artifact flags |
| [[MTOR]] | [[WDR19]] | moves it that way too | B | MTOR activity lowers WDR19's level | compounds that target MTOR: 6 of 8 raise it (AZD-8055, Bimiralisib, GSK1059615, Rapamycin, Sapanisertib, Temsirolimus) | 75% of the class's compounds vs 5.6% of all compounds | 0.007 | ⚠ off-target possible; 6 compounds; artifact flags |
| [[MTOR]] | [[CENPN]] | moves it that way too | B | MTOR activity raises CENPN's level | compounds that target MTOR: 5 of 8 lower it (AZD-8055, Bimiralisib, Rapamycin, Sapanisertib, Temsirolimus) | 62% of the class's compounds vs 3.1% of all compounds | 0.007 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[MTOR]] | [[DTL]] | moves it that way too | B | MTOR activity raises DTL's level | compounds that target MTOR: 6 of 8 lower it (AZD-8055, Bimiralisib, GSK1059615, Rapamycin, Sapanisertib, Temsirolimus) | 75% of the class's compounds vs 6.2% of all compounds | 0.008 | ⚠ off-target possible; 6 compounds; artifact flags |
| [[MTOR]] | [[WDR62]] | moves it that way too | B | MTOR activity raises WDR62's level | compounds that target MTOR: 6 of 8 lower it (AZD-8055, Bimiralisib, GSK1059615, Rapamycin, Sapanisertib, Temsirolimus) | 75% of the class's compounds vs 6.2% of all compounds | 0.008 | ⚠ off-target possible; 6 compounds; artifact flags |
| [[MTOR]] | [[MARS1]] | moves it that way too | B | MTOR activity raises MARS1's level | compounds that target MTOR: 5 of 8 lower it (AZD-8055, Bimiralisib, Rapamycin, Sapanisertib, Temsirolimus) | 62% of the class's compounds vs 3.4% of all compounds | 0.008 | ⚠ off-target possible; 5 compounds |
| [[MTOR]] | [[SMAP2]] | moves it that way too | B | MTOR activity raises SMAP2's level | compounds that target MTOR: 5 of 8 lower it (Bimiralisib, GSK1059615, Rapamycin, Sapanisertib, Temsirolimus) | 62% of the class's compounds vs 3.4% of all compounds | 0.008 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[MTOR]] | [[ERICH1]] | moves it that way too | B | MTOR activity lowers ERICH1's level | compounds that target MTOR: 5 of 8 raise it (AZD-8055, Bimiralisib, Rapamycin, Sapanisertib, Temsirolimus) | 62% of the class's compounds vs 3.6% of all compounds | 0.010 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[MTOR]] | [[FBXO32]] | moves it that way too | B | MTOR activity lowers FBXO32's level | compounds that target MTOR: 6 of 8 raise it (AZD-8055, Bimiralisib, GSK1059615, Rapamycin, Sapanisertib, Temsirolimus) | 75% of the class's compounds vs 7.3% of all compounds | 0.013 | ⚠ off-target possible; 6 compounds |
| [[MTOR]] | [[PDIA3]] | moves it that way too | B | MTOR activity raises PDIA3's level | compounds that target MTOR: 5 of 8 lower it (Bimiralisib, GSK1059615, Rapamycin, Sapanisertib, Temsirolimus) | 62% of the class's compounds vs 3.9% of all compounds | 0.013 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[MTOR]] | [[YPEL1]] | moves it that way too | B | MTOR activity lowers YPEL1's level | compounds that target MTOR: 5 of 8 raise it (Bimiralisib, GSK1059615, Rapamycin, Sapanisertib, Temsirolimus) | 62% of the class's compounds vs 3.9% of all compounds | 0.013 | ⚠ off-target possible; 5 compounds; artifact flags |

## Data

- `tables/drugs.parquet` — drug == "Sapanisertib"
- `tables/drugdoses.parquet` — dd in 934, 935, 936
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
