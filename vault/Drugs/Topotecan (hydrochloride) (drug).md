---
drug: "Topotecan (hydrochloride)"
type: "drug"
salt_base: "Topotecan"
targets: "TOP1"
moa_fine: "DNA synthesis/repair inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 8958
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Topotecan (hydrochloride)

*DNA synthesis/repair inhibitor (inhibitor/antagonist) · targets: TOP1 · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 490 / 3368 / 8958; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.05 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.51 / 0.65.
> Flags by dose: - / cell-cycle shift / toxic; cell-cycle shift. ⚠ 0.5 µM: cell-cycle shift; 5 µM: toxic; cell-cycle shift (artifact flags: its changes there are shown with an alert, not left out).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 07]]:B11 | 355 / 135 | — | -0.96 | +2.5/-2.2/+0.8 | — |
| 0.5 µM | [[Plate 08]]:B11 | 2,057 / 1,311 | — | +0.11 | +7.2/-2.9/+0.3 | ⚠ cell-cycle shift |
| 5 µM | [[Plate 09]]:B11 | 6,202 / 2,756 | — | -1.25 | +6.9/-2.7/+4.8 | ⚠ toxic; cell-cycle shift |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (355 genes, none with an alert; 12 shown): [[NTN1]] 1.50× (z +6.7, 17/29 lines), [[FDXR]] 1.80× (z +5.4, 22/36 lines), [[ENSG00000283674]] 1.38× (z +5.2, 10/30 lines), [[VARS2]] 1.57× (z +5.1, 16/44 lines), [[PGBD1]] 1.34× (z +5.0, 13/44 lines), [[GRIN2C]] 1.93× (z +4.9, 12/20 lines), [[E2F7]] 1.33× (z +4.8, 18/41 lines), [[LGI4]] 1.84× (z +4.8, 6/15 lines), [[GINS4]] 1.45× (z +4.7, 17/43 lines), [[PIDD1]] 1.85× (z +4.5, 6/28 lines), [[ZMAT3]] 1.33× (z +4.5, 19/42 lines), [[GLS2]] 1.65× (z +4.4, 6/16 lines)

**0.5 µM** (2057 genes, 1,248 with an alert ⚠; the drug-dose carries ⚠ cell-cycle shift; 21 shown): [[NETO2]] ⚠ 1.92× (z +12.7, 33/36 lines; cell-cycle shift, explains ~26% of this change), [[CCNE2]] ⚠ 2.46× (z +11.3, 32/46 lines; cell-cycle shift, explains ~58% of this change), [[DNA2]] ⚠ 1.83× (z +11.2, 36/47 lines; cell-cycle shift, explains ~58% of this change), [[NPL]] ⚠ 2.40× (z +11.1, 29/39 lines; cell-cycle shift, explains ~32% of this change), [[NTN1]] ⚠ 1.82× (z +10.6, 26/30 lines; cell-cycle shift, explains ~29% of this change), [[SLC25A19]] ⚠ 2.07× (z +10.3, 32/47 lines; cell-cycle shift, explains ~39% of this change), [[RETSAT]] 1.59× (z +9.9, 29/47 lines; cell-cycle shift (explains ~12% here)), [[FAM111B]] ⚠ 3.13× (z +9.9, 33/37 lines; cell-cycle shift, explains ~63% of this change), [[ENSG00000283674]] ⚠ 1.76× (z +9.8, 25/31 lines; cell-cycle shift, explains ~44% of this change), [[CCDC138]] ⚠ 1.63× (z +9.7, 44/48 lines; cell-cycle shift, explains ~33% of this change), [[GLMN]] 1.49× (z +9.7, 41/48 lines; cell-cycle shift (explains ~17% here)), [[PLCL2]] 1.87× (z +9.5, 25/35 lines; cell-cycle shift (explains ~14% here)), [[NCR3LG1]] 2.15× (z +9.3, 32/41 lines; cell-cycle shift (explains ~12% here)), [[FAM111A]] 2.03× (z +9.2, 35/44 lines; cell-cycle shift (explains ~20% here)), [[HDX]] 2.00× (z +9.1, 25/31 lines; cell-cycle shift (explains ~7% here)), [[EXOG]] 1.60× (z +9.0, 37/47 lines; cell-cycle shift (explains ~20% here)), [[MARCHF3]] 1.68× (z +8.9, 31/42 lines; cell-cycle shift (explains ~25% here)), [[AK3]] 1.35× (z +8.6, 27/47 lines; cell-cycle shift (explains ~6% here)), [[HSPBAP1]] 1.73× (z +8.6, 32/47 lines; cell-cycle shift (explains ~13% here)), [[TAP2]] 1.64× (z +8.5, 39/47 lines; cell-cycle shift (explains ~15% here)), [[PHTF1]] 1.48× (z +8.4, 36/47 lines; cell-cycle shift (explains ~24% here))

**5 µM** (6202 genes, 6,202 with an alert ⚠; the drug-dose carries ⚠ toxic; cell-cycle shift; 12 shown): [[MSH4]] ⚠ 9.24× (z +21.0, 26/27 lines; toxic; cell-cycle shift (explains ~9% here)), [[SOCS4]] ⚠ 2.62× (z +20.2, 43/47 lines; toxic; cell-cycle shift (explains ~18% here)), [[MED21]] ⚠ 2.27× (z +19.3, 45/47 lines; toxic; cell-cycle shift (explains ~5% here)), [[SLC13A3]] ⚠ 3.77× (z +17.7, 20/28 lines; toxic; cell-cycle shift (explains ~7% here)), [[SLC35G1]] ⚠ 3.03× (z +16.9, 37/40 lines; toxic; cell-cycle shift (explains ~17% here)), [[PPP1R42]] ⚠ 6.71× (z +16.8, 8/9 lines; toxic; cell-cycle shift (explains ~5% here)), [[THEM4]] ⚠ 2.38× (z +16.5, 37/39 lines; toxic; cell-cycle shift (explains ~7% here)), [[NETO2]] ⚠ 2.38× (z +16.3, 33/36 lines; toxic; cell-cycle shift (explains ~20% here)), [[ENSG00000222017]] ⚠ 3.73× (z +16.1, 24/32 lines; toxic; cell-cycle shift (explains ~17% here)), [[RNASEH1]] ⚠ 2.19× (z +15.9, 43/47 lines; toxic; cell-cycle shift (explains ~12% here)), [[TERB1]] ⚠ 6.30× (z +15.7, 7/8 lines; toxic; cell-cycle shift (explains ~3% here)), [[FBXO22]] ⚠ 2.11× (z +15.6, 43/47 lines; toxic; cell-cycle shift (explains ~16% here))

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (135 genes, none with an alert; 12 shown): [[C1QTNF7-AS1]] 0.665× (z -7.3, 29/44 lines), [[NAV2]] 0.648× (z -6.7, 25/30 lines), [[ENSG00000223727]] 0.500× (z -6.4, 23/38 lines), [[ENSG00000226965]] 0.629× (z -6.3, 20/36 lines), [[DIAPH2]] 0.719× (z -6.0, 35/40 lines), [[FHIT]] 0.596× (z -6.0, 39/41 lines), [[SBF2]] 0.780× (z -5.7, 35/47 lines), [[GBE1]] 0.713× (z -5.2, 38/45 lines), [[CCSER1]] 0.710× (z -5.1, 18/28 lines), [[WWOX]] 0.675× (z -4.7, 30/42 lines), [[LPP]] 0.748× (z -4.6, 39/47 lines), [[FNDC3B]] 0.765× (z -4.6, 40/47 lines)

**0.5 µM** (1311 genes, 591 with an alert ⚠; the drug-dose carries ⚠ cell-cycle shift; 13 shown): [[C1QTNF7-AS1]] 0.277× (z -24.7, 45/45 lines; cell-cycle shift (explains ~16% here)), [[ENSG00000289986]] 0.208× (z -19.9, 38/43 lines; cell-cycle shift (explains ~7% here)), [[ENSG00000285713]] 0.298× (z -19.3, 44/47 lines; cell-cycle shift (explains ~0% here)), [[LINC02935]] 0.199× (z -19.3, 40/43 lines; cell-cycle shift (explains ~0% here)), [[NAV2]] 0.337× (z -18.3, 30/31 lines; cell-cycle shift (explains ~21% here)), [[SBF2]] 0.478× (z -18.3, 48/48 lines; cell-cycle shift (explains ~6% here)), [[ENSG00000251379]] 0.204× (z -17.8, 43/43 lines; cell-cycle shift (explains ~12% here)), [[ENSG00000223727]] 0.179× (z -17.3, 39/40 lines; cell-cycle shift (explains ~10% here)), [[MAP4]] 0.630× (z -17.1, 47/47 lines; cell-cycle shift (explains ~12% here)), [[ENSG00000235609]] ⚠ 0.410× (z -16.6, 33/39 lines; cell-cycle shift, explains ~39% of this change), [[ENSG00000227240]] 0.325× (z -16.3, 31/35 lines; cell-cycle shift (explains ~9% here)), [[LINC01505]] 0.343× (z -16.1, 39/42 lines; cell-cycle shift (explains ~0% here)), [[LINC00598]] 0.391× (z -15.5, 40/43 lines; cell-cycle shift (explains ~9% here))

**5 µM** (2756 genes, 2,756 with an alert ⚠; the drug-dose carries ⚠ toxic; cell-cycle shift; 12 shown): [[ENSG00000235609]] ⚠ 0.205× (z -28.4, 35/38 lines; toxic; cell-cycle shift (explains ~22% here)), [[BBX]] ⚠ 0.485× (z -24.2, 47/47 lines; toxic; cell-cycle shift (explains ~13% here)), [[SBF2]] ⚠ 0.363× (z -24.1, 47/47 lines; toxic; cell-cycle shift (explains ~5% here)), [[LINC00598]] ⚠ 0.227× (z -23.5, 40/42 lines; toxic; cell-cycle shift (explains ~6% here)), [[FNDC3B]] ⚠ 0.269× (z -23.3, 46/47 lines; toxic; cell-cycle shift (explains ~12% here)), [[NCOR1]] ⚠ 0.560× (z -22.7, 47/47 lines; toxic; cell-cycle shift (explains ~11% here)), [[NAV2]] ⚠ 0.250× (z -22.4, 30/30 lines; toxic; cell-cycle shift (explains ~17% here)), [[CFDP1]] ⚠ 0.507× (z -22.0, 45/47 lines; toxic; cell-cycle shift (explains ~7% here)), [[DIAPH2]] ⚠ 0.315× (z -21.9, 40/40 lines; toxic; cell-cycle shift (explains ~8% here)), [[MAP4]] ⚠ 0.545× (z -21.6, 44/46 lines; toxic; cell-cycle shift (explains ~10% here)), [[KAZN]] ⚠ 0.380× (z -21.6, 37/42 lines; toxic; cell-cycle shift (explains ~1% here)), [[FHIT]] ⚠ 0.170× (z -21.4, 41/41 lines; toxic; cell-cycle shift (explains ~5% here))

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | [[Module 062]] (+2.3) | [[Module 200]] (-3.0) |
| 0.5 µM | [[Module 137]] (+7.5), [[Module 006]] (+4.5), [[Module 005]] (+4.3) | [[Module 200]] (-6.4), [[Module 026]] (-4.1), [[Module 099]] (-3.9) |
| 5 µM | [[Module 168]] (+8.7), [[Module 118]] (+8.4), [[Module 068]] (+7.9) | [[Module 200]] (-13.9), [[Module 231]] (-8.9), [[Module 211]] (-8.8) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | [[NCI-H661 (line)]] (1.43), [[C32 (line)]] (1.35), [[SW 1271 (line)]] (1.24), [[HepG2_C3A (line)]] (1.20) · weakest: [[SK-MEL-2 (line)]] (0.540), [[PANC-1 (line)]] (0.620), [[NCI-H23 (line)]] (0.641) |
| 0.5 µM | [[H4 (line)]] (-5.8), [[LOX-IMVI (line)]] (-4.3) | [[CFPAC-1 (line)]] (1.45), [[MIA PaCa-2 (line)]] (1.40), [[HOP62 (line)]] (1.36), [[C32 (line)]] (1.33) · weakest: [[BT-474 (line)]] (0.696), [[NCI-H661 (line)]] (0.699), [[NCI-H23 (line)]] (0.704) |
| 5 µM | [[RKO (line)]] (-12.6), [[MIA PaCa-2 (line)]] (-9.1), [[SW1417 (line)]] (-6.2), [[HepG2_C3A (line)]] (-5.4), [[C32 (line)]] (-5.2) | [[RKO (line)]] (1.56), [[HepG2_C3A (line)]] (1.43), [[MIA PaCa-2 (line)]] (1.42), [[SNU-1 (line)]] (1.27) · weakest: [[BT-474 (line)]] (0.576), [[SHP-77 (line)]] (0.684), [[A549 (line)]] (0.686) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

⚠ This drug's own vector: vector dose flagged: toxic; cell-cycle shift. Read its neighbours with that in mind.

*378 other drugs have a vector, 121 with an alert ⚠; shown: the 8 most similar and the 2 next most similar without an alert.*

- [[Amsacrine (drug)]] (+0.61, DNA synthesis/repair inhibitor); [[Monocrotaline (drug)]] (+0.56, unclear); [[Oxaprozin (drug)]] (+0.51, Cyclooxygenase inhibitor); [[Irinotecan (drug)]] (+0.50, DNA synthesis/repair inhibitor); [[Hydroxyurea (drug)]] (+0.49, DNA synthesis/repair inhibitor); [[Pyridoxine (drug)]] (+0.48, unclear); [[Macitentan (drug)]] (+0.48, unclear, ⚠ only 5 significant genes); [[Imiquimod (hydrochloride) (drug)]] (+0.44, unclear, ⚠ vector dose flagged: toxic); [[Cysteamine (hydrochloride) (drug)]] (+0.44, unclear); [[Drospirenone (drug)]] (+0.41, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 27 arrows, 27 of them with an alert ⚠; grade A 0, B 11, C 16. Shown: the 15 strongest; 12 more arrows (12 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[PCED1B]] | 5 µM | B | PCED1B activity raises the cells' numbers under Topotecan (hydrochloride) 5 µM (protects the cells) | lines that do not express PCED1B (11) vs lines expressing it (37) | the lines without PCED1B: 0.51× the cells of the other lines | 0.050 | ⚠ within organs, on part of the lines; also absent: AMIGO2, CXCL3, PRDM1 |
| [[ATXN1]] | 5 µM | B | ATXN1 activity raises the cells' numbers under Topotecan (hydrochloride) 5 µM (protects the cells) | lines that do not express ATXN1 (6) vs lines expressing it (42) | the lines without ATXN1: 0.55× the cells of the other lines | 0.050 | ⚠ within organs, on part of the lines; also absent: ATXN1-AS1, LAMB1, SYTL2 |
| [[ARHGAP26]] | 5 µM | B | ARHGAP26 activity raises the cells' numbers under Topotecan (hydrochloride) 5 µM (protects the cells) | lines that do not express ARHGAP26 (6) vs lines expressing it (42) | the lines without ARHGAP26: 0.47× the cells of the other lines | 0.056 | ⚠ within organs, on part of the lines; also absent: SSUH2, ADM2, TBC1D8; maybe low, not absent |
| [[NNT]], [[NNT-AS1]] | 5 µM | B | NNT, NNT-AS1 activity raises the cells' numbers under Topotecan (hydrochloride) 5 µM (protects the cells) | lines that do not express NNT, NNT-AS1 (6) vs lines expressing them (42) | the lines without NNT, NNT-AS1: 0.65× the cells of the other lines | 0.079 | ⚠ within organs, on part of the lines; co-absent genes |
| [[ENSG00000251537]] | 5 µM | B | ENSG00000251537 activity raises the cells' numbers under Topotecan (hydrochloride) 5 µM (protects the cells) | lines that do not express ENSG00000251537 (9) vs lines expressing it (39) | the lines without ENSG00000251537: 0.52× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: FBXW10B, PCED1B, NHS; maybe low, not absent |
| [[HR]] | 0.5 µM | B | HR activity lowers the cells' numbers under Topotecan (hydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express HR (23) vs lines expressing it (25) | the lines without HR: 1.01× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; also absent: SULF2, CEACAM1, HNF1A-AS1 |
| [[PDLIM1]] | 5 µM | B | PDLIM1 activity raises the cells' numbers under Topotecan (hydrochloride) 5 µM (protects the cells) | lines that do not express PDLIM1 (11) vs lines expressing it (37) | the lines without PDLIM1: 0.62× the cells of the other lines | 0.087 | ⚠ within organs, on part of the lines; also absent: PCED1B, GPR39, ATP8B1 |
| [[SYT12]] | 0.5 µM | B | SYT12 activity raises the cells' numbers under Topotecan (hydrochloride) 0.5 µM (protects the cells) | lines that do not express SYT12 (9) vs lines expressing it (39) | the lines without SYT12: 0.89× the cells of the other lines | 0.095 | ⚠ within organs, on part of the lines; also absent: EMSLR; maybe low, not absent |
| [[ATP1B1]] | 5 µM | B | ATP1B1 activity raises the cells' numbers under Topotecan (hydrochloride) 5 µM (protects the cells) | lines that do not express ATP1B1 (8) vs lines expressing it (40) | the lines without ATP1B1: 0.63× the cells of the other lines | 0.096 | ⚠ within organs, on part of the lines; also absent: PYROXD2, IL15, IER3; maybe low, not absent |
| [[TBC1D8]] | 0.5 µM | B | TBC1D8 activity raises the cells' numbers under Topotecan (hydrochloride) 0.5 µM (protects the cells) | lines that do not express TBC1D8 (6) vs lines expressing it (42) | the lines without TBC1D8: 0.87× the cells of the other lines | 0.098 | ⚠ within organs, on part of the lines; also absent: SSUH2, ARHGAP26, ENSG00000251537; maybe low, not absent |
| [[SEC16B]] | 5 µM | B | SEC16B activity raises the cells' numbers under Topotecan (hydrochloride) 5 µM (protects the cells) | lines that do not express SEC16B (13) vs lines expressing it (35) | the lines without SEC16B: 0.65× the cells of the other lines | 0.0995 | ⚠ within organs, on part of the lines; also absent: CRYZL2P, CYP2S1, GRHL3 |
| [[VRK2]] | 0.5 µM | C | VRK2 activity raises the cells' numbers under Topotecan (hydrochloride) 0.5 µM (protects the cells) | lines that do not express VRK2 (4) vs lines expressing it (44) | the lines without VRK2: 0.67× the cells of the other lines | 0.002 | ⚠ few lines (4 vs 46); tissue-confounded; across organs; also absent: PTER, ZC3HAV1L, OSR2 |
| [[KLHL9]] | 0.5 µM | C | KLHL9 activity raises the cells' numbers under Topotecan (hydrochloride) 0.5 µM (protects the cells) | lines that do not express KLHL9 (3) vs lines expressing it (45) | the lines without KLHL9: 0.63× the cells of the other lines | 0.008 | ⚠ few lines (3 vs 47); across organs; also absent: MTAP, TMEM117, CFL1P1-1 |
| [[DDR1]] | 5 µM | C | DDR1 activity raises the cells' numbers under Topotecan (hydrochloride) 5 µM (protects the cells) | lines that do not express DDR1 (3) vs lines expressing it (45) | the lines without DDR1: 0.38× the cells of the other lines | 0.009 | ⚠ few lines (3 vs 47); across organs; co-occurs with SMAD3; also absent: FTH1, LINC00847, IER3; maybe low, not absent |
| [[ATAD1]], [[PTEN]] | 0.5 µM | C | ATAD1, PTEN activity raises the cells' numbers under Topotecan (hydrochloride) 0.5 µM (protects the cells) | lines that do not express ATAD1, PTEN (4) vs lines expressing them (44) | the lines without ATAD1, PTEN: 0.68× the cells of the other lines | 0.012 | ⚠ few lines (4 vs 46); tissue-confounded; across organs; also absent: CFL1P1-1, ZC3HAV1L, OSR2; co-absent genes |

### Its targets: what acting on them probably does

*Drug-target arrows of the compound classes it belongs to (compounds sharing a listed target and mechanism; one molecule counts once, under all its names): the target → a gene whose level those compounds move. A row that names several targets is one test: the compounds share them all, and any of them could be the cause. 98 arrows, 98 of them with an alert ⚠; grade A 0, B 98, C 0. Shown: the 15 strongest; 83 more arrows (83 of them with an alert ⚠) not shown.*

| Its target | Gene it moves | This drug | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|---|
| [[TOP1]] | [[SRBD1]] | moves it that way too | B | TOP1 activity lowers SRBD1's level | compounds that target TOP1: 3 of 3 raise it (Doxorubicin, Irinotecan, Topotecan) | 100% of the class's compounds vs 1.4% of all compounds | 0.010 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[TOP1]] | [[ENSG00000227240]] | moves it that way too | B | TOP1 activity raises ENSG00000227240's level | compounds that target TOP1: 3 of 3 lower it (Doxorubicin, Irinotecan, Topotecan) | 100% of the class's compounds vs 2.0% of all compounds | 0.017 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[TOP1]] | [[ENSG00000229618]] | moves it that way too | B | TOP1 activity raises ENSG00000229618's level | compounds that target TOP1: 3 of 3 lower it (Doxorubicin, Irinotecan, Topotecan) | 100% of the class's compounds vs 2.5% of all compounds | 0.026 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[TOP1]] | [[ENSG00000267053]] | moves it that way too | B | TOP1 activity lowers ENSG00000267053's level | compounds that target TOP1: 3 of 3 raise it (Doxorubicin, Irinotecan, Topotecan) | 100% of the class's compounds vs 2.8% of all compounds | 0.028 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[TOP1]] | [[MND1]] | moves it that way too | B | TOP1 activity lowers MND1's level | compounds that target TOP1: 3 of 3 raise it (Doxorubicin, Irinotecan, Topotecan) | 100% of the class's compounds vs 3.1% of all compounds | 0.032 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[TOP1]] | [[LINC03041]] | moves it that way too | B | TOP1 activity raises LINC03041's level | compounds that target TOP1: 3 of 3 lower it (Doxorubicin, Irinotecan, Topotecan) | 100% of the class's compounds vs 3.4% of all compounds | 0.037 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[TOP1]] | [[TAF4]] | moves it that way too | B | TOP1 activity lowers TAF4's level | compounds that target TOP1: 3 of 3 raise it (Doxorubicin, Irinotecan, Topotecan) | 100% of the class's compounds vs 3.4% of all compounds | 0.037 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[TOP1]] | [[CENPO]] | moves it that way too | B | TOP1 activity lowers CENPO's level | compounds that target TOP1: 3 of 3 raise it (Doxorubicin, Irinotecan, Topotecan) | 100% of the class's compounds vs 3.6% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[TOP1]] | [[MELK]] | moves it that way too | B | TOP1 activity lowers MELK's level | compounds that target TOP1: 3 of 3 raise it (Doxorubicin, Irinotecan, Topotecan) | 100% of the class's compounds vs 3.6% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[TOP1]] | [[POLQ]] | moves it that way too | B | TOP1 activity lowers POLQ's level | compounds that target TOP1: 3 of 3 raise it (Doxorubicin, Irinotecan, Topotecan) | 100% of the class's compounds vs 3.6% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[TOP1]] | [[RFC3]] | moves it that way too | B | TOP1 activity lowers RFC3's level | compounds that target TOP1: 3 of 3 raise it (Doxorubicin, Irinotecan, Topotecan) | 100% of the class's compounds vs 3.6% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[TOP1]] | [[TBC1D31]] | moves it that way too | B | TOP1 activity lowers TBC1D31's level | compounds that target TOP1: 3 of 3 raise it (Doxorubicin, Irinotecan, Topotecan) | 100% of the class's compounds vs 3.6% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[TOP1]] | [[SEMA6A-AS1]] | moves it that way too | B | TOP1 activity raises SEMA6A-AS1's level | compounds that target TOP1: 2 of 3 lower it (Irinotecan, Topotecan) | 67% of the class's compounds vs 0.6% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TOP1]] | [[DNA2]] | moves it that way too | B | TOP1 activity lowers DNA2's level | compounds that target TOP1: 3 of 3 raise it (Doxorubicin, Irinotecan, Topotecan) | 100% of the class's compounds vs 3.9% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[TOP1]] | [[FANCI]] | moves it that way too | B | TOP1 activity lowers FANCI's level | compounds that target TOP1: 3 of 3 raise it (Doxorubicin, Irinotecan, Topotecan) | 100% of the class's compounds vs 3.9% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |

## Data

- `tables/drugs.parquet` — drug == "Topotecan (hydrochloride)"
- `tables/drugdoses.parquet` — dd in 1027, 1028, 1029
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
