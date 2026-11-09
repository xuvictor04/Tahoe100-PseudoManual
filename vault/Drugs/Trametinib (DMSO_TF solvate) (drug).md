---
drug: "Trametinib (DMSO_TF solvate)"
type: "drug"
salt_base: "Trametinib"
targets: "MAP2K1, MAP2K2"
moa_fine: "MEK inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 1909
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Trametinib (DMSO_TF solvate)

*MEK inhibitor (inhibitor/antagonist) · targets: MAP2K1, MAP2K2 · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 1546 / 1357 / 1909; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.05 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.71 / 0.87.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 07]]:C2 | 466 / 1,080 | — | +0.90 | -1.8/-0.9/-1.5 | — |
| 0.5 µM | [[Plate 08]]:C2 | 587 / 770 | — | +0.42 | -2.2/-0.5/+0.1 | — |
| 5 µM | [[Plate 09]]:C2 | 1,168 / 741 | — | -0.09 | -3.1/-1.3/-0.4 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (466 genes, none with an alert; 12 shown): [[GBP2]] 1.84× (z +8.5, 28/35 lines), [[CFB]] 2.41× (z +7.2, 21/28 lines), [[TTBK2]] 1.31× (z +6.1, 32/48 lines), [[TMEM140]] 1.95× (z +5.8, 25/38 lines), [[IL15]] 1.45× (z +5.8, 23/38 lines), [[STK38]] 1.21× (z +5.5, 19/48 lines), [[PPM1H]] 1.40× (z +5.5, 17/36 lines), [[TLR3]] 2.02× (z +5.5, 15/35 lines), [[POT1-AS1]] 1.74× (z +5.4, 22/45 lines), [[TMEM106B]] 1.32× (z +5.4, 31/48 lines), [[ARMH1]] 1.74× (z +5.4, 18/44 lines), [[FRK]] 1.48× (z +5.3, 17/26 lines)

**0.5 µM** (587 genes, none with an alert; 12 shown): [[GBP2]] 2.23× (z +12.1, 31/36 lines), [[CFB]] 3.11× (z +10.1, 26/28 lines), [[GBP1]] 2.38× (z +8.0, 29/32 lines), [[PGM2L1]] 1.36× (z +7.0, 24/45 lines), [[PIR]] 1.53× (z +6.7, 19/38 lines), [[POT1-AS1]] 1.86× (z +6.6, 30/46 lines), [[PALLD]] 1.45× (z +6.5, 25/38 lines), [[IL15]] 1.47× (z +6.5, 24/39 lines), [[ZSCAN31]] 2.06× (z +6.3, 23/37 lines), [[APOL6]] 1.43× (z +6.3, 29/43 lines), [[ARID5B]] 1.49× (z +6.2, 29/43 lines), [[TMEM140]] 1.95× (z +6.2, 27/38 lines)

**5 µM** (1168 genes, none with an alert; 12 shown): [[GBP2]] 2.76× (z +14.7, 33/35 lines), [[CFB]] 4.16× (z +12.2, 24/27 lines), [[GBP1]] 2.86× (z +9.3, 29/32 lines), [[ARID5B]] 1.71× (z +8.1, 32/42 lines), [[ZSCAN31]] 2.62× (z +8.1, 26/34 lines), [[POT1-AS1]] 2.18× (z +8.0, 29/43 lines), [[CLIP1]] 1.29× (z +7.8, 32/48 lines), [[TRIM22]] 2.19× (z +7.7, 26/29 lines), [[IL15]] 1.59× (z +7.4, 25/38 lines), [[TLR3]] 2.50× (z +7.4, 26/32 lines), [[CD24]] 1.85× (z +7.4, 15/23 lines), [[JDP2]] 1.69× (z +7.2, 19/34 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (1080 genes, none with an alert; 12 shown): [[ETV5]] 0.278× (z -26.5, 46/48 lines), [[SPRY4]] 0.211× (z -18.7, 47/48 lines), [[EGR1]] 0.0979× (z -16.5, 46/46 lines), [[DUSP6]] 0.141× (z -16.1, 44/44 lines), [[ETV4]] 0.342× (z -15.4, 40/45 lines), [[ZFPM2-AS1]] 0.453× (z -13.5, 31/32 lines), [[SPRY4-AS1]] 0.266× (z -12.7, 43/45 lines), [[ITGB5]] 0.475× (z -12.1, 40/46 lines), [[ITGA2]] 0.385× (z -11.8, 36/37 lines), [[MYEOV]] 0.354× (z -11.0, 26/29 lines), [[ETV1]] 0.386× (z -10.9, 31/37 lines), [[DUSP5]] 0.397× (z -10.8, 39/41 lines)

**0.5 µM** (770 genes, none with an alert; 12 shown): [[ETV5]] 0.152× (z -42.1, 48/49 lines), [[SPRY4]] 0.149× (z -24.8, 47/49 lines), [[ZFPM2-AS1]] 0.310× (z -20.1, 33/33 lines), [[ETV4]] 0.276× (z -20.0, 43/45 lines), [[DUSP6]] 0.109× (z -19.7, 44/45 lines), [[SPRY4-AS1]] 0.173× (z -18.1, 46/46 lines), [[EGR1]] 0.106× (z -17.2, 47/47 lines), [[ETV1]] 0.267× (z -16.5, 35/38 lines), [[ITGB5]] 0.395× (z -16.3, 42/47 lines), [[SPRED1]] 0.362× (z -16.0, 47/49 lines), [[ITGA2]] 0.320× (z -15.3, 36/38 lines), [[SPRED2]] 0.393× (z -14.8, 48/49 lines)

**5 µM** (741 genes, none with an alert; 12 shown): [[ETV5]] 0.132× (z -43.7, 48/48 lines), [[SPRY4]] 0.163× (z -22.7, 46/47 lines), [[ETV4]] 0.251× (z -20.6, 44/45 lines), [[ZFPM2-AS1]] 0.330× (z -19.7, 32/32 lines), [[DUSP6]] 0.113× (z -18.6, 44/44 lines), [[ETV1]] 0.218× (z -18.3, 35/37 lines), [[EGR1]] 0.103× (z -16.8, 46/46 lines), [[SPRED1]] 0.351× (z -15.8, 47/48 lines), [[ITGB5]] 0.397× (z -15.6, 43/46 lines), [[SPRY4-AS1]] 0.210× (z -15.5, 44/45 lines), [[SPRED2]] 0.371× (z -15.1, 48/48 lines), [[ITGA2]] 0.315× (z -14.9, 36/37 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | [[Module 171]] (+3.8), [[Module 135]] (+3.4), [[Module 194]] (+3.3) | [[Module 174]] (-6.5), [[Module 235]] (-5.1), [[Module 092]] (-4.9) |
| 0.5 µM | [[Module 059]] (+4.0), [[Module 182]] (+3.8), [[Module 135]] (+3.3) | [[Module 174]] (-9.0), [[Module 092]] (-6.6), [[Module 147]] (-4.9) |
| 5 µM | [[Module 135]] (+4.1), [[Module 070]] (+3.5), [[Module 059]] (+3.5) | [[Module 174]] (-8.5), [[Module 092]] (-6.3), [[Module 235]] (-4.4) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | [[NCI-H1792 (line)]] (-5.6), [[NCI-H23 (line)]] (-3.9), [[A549 (line)]] (-3.5) | [[C32 (line)]] (1.42), [[SW480 (line)]] (1.40), [[MIA PaCa-2 (line)]] (1.38), [[SW48 (line)]] (1.35) · weakest: [[RPMI-7951 (line)]] (0.767), [[A-172 (line)]] (0.770), [[SW 1088 (line)]] (0.782) |
| 0.5 µM | [[NCI-H1792 (line)]] (-6.6), [[SK-MEL-2 (line)]] (-4.6), [[CHP-212 (line)]] (-4.1), [[NCI-H23 (line)]] (-3.6) | [[MIA PaCa-2 (line)]] (1.49), [[NCI-H1573 (line)]] (1.47), [[NCI-H23 (line)]] (1.43), [[AsPC-1 (line)]] (1.42) · weakest: [[NCI-H661 (line)]] (0.255), [[AN3 CA (line)]] (0.578), [[CHP-212 (line)]] (0.626) |
| 5 µM | [[NCI-H1792 (line)]] (-4.8), [[NCI-H23 (line)]] (-3.8), [[SK-MEL-2 (line)]] (-3.2) | [[HOP62 (line)]] (1.39), [[NCI-H23 (line)]] (1.36), [[AsPC-1 (line)]] (1.34), [[NCI-H1573 (line)]] (1.33) · weakest: [[NCI-H661 (line)]] (0.176), [[AN3 CA (line)]] (0.523), [[CHP-212 (line)]] (0.557) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 1 next most similar without an alert.*

- [[Elimusertib hydrochloride (drug)]] (+0.95, unclear); [[Binimetinib (drug)]] (+0.94, MEK inhibitor); [[Cobimetinib (drug)]] (+0.92, MEK inhibitor); [[Trametinib (drug)]] (+0.91, MEK inhibitor, ⚠ vector dose flagged: cell-cycle shift); [[Capmatinib (drug)]] (+0.82, EGFR/ERBB inhibitor); [[BI-3406 (drug)]] (+0.77, RAS inhibitor); [[AZD-7648 (drug)]] (+0.77, DNA synthesis/repair inhibitor); [[Perindopril (erbumine) (drug)]] (+0.76, unclear); [[Alpelisib (drug)]] (+0.76, PI3K/AKT inhibitor)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 15 arrows, 15 of them with an alert ⚠; grade A 0, B 3, C 12.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[GLIS3]] | 0.05 µM | B | GLIS3 activity lowers the cells' numbers under Trametinib (DMSO_TF solvate) 0.05 µM (makes them more sensitive) | lines that do not express GLIS3 (21) vs lines expressing it (27) | the lines without GLIS3: 1.22× the cells of the other lines | 0.050 | ⚠ within organs, on part of the lines; also absent: ENSG00000232949, STEAP1B-AS1, SYNPO |
| [[BNC2]] | 0.05 µM | B | BNC2 activity lowers the cells' numbers under Trametinib (DMSO_TF solvate) 0.05 µM (makes them more sensitive) | lines that do not express BNC2 (21) vs lines expressing it (27) | the lines without BNC2: 1.28× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: LINC03041, DPY19L2, RNF182 |
| [[ZNF469]] | 0.05 µM | B | ZNF469 activity lowers the cells' numbers under Trametinib (DMSO_TF solvate) 0.05 µM (makes them more sensitive) | lines that do not express ZNF469 (20) vs lines expressing it (28) | the lines without ZNF469: 1.25× the cells of the other lines | 0.092 | ⚠ within organs, on part of the lines; also absent: LINC02057, IL6, TMEM158 |
| [[SPART-AS1]] | 0.05 µM | C | SPART-AS1 activity lowers the cells' numbers under Trametinib (DMSO_TF solvate) 0.05 µM (makes them more sensitive) | lines that do not express SPART-AS1 (16) vs lines expressing it (32) | the lines without SPART-AS1: 1.24× the cells of the other lines | 0.008 | ⚠ tissue-confounded; across organs; also absent: CCDC169, FIGN, SPART |
| [[NR3C1]] | 0.05 µM | C | NR3C1 activity lowers the cells' numbers under Trametinib (DMSO_TF solvate) 0.05 µM (makes them more sensitive) | lines that do not express NR3C1 (13) vs lines expressing it (35) | the lines without NR3C1: 1.28× the cells of the other lines | 0.015 | ⚠ tissue-confounded; across organs; co-occurs with SETD1B, ZFHX3; also absent: C2orf74-DT, C2orf74, SPART-AS1 |
| [[C2orf74]] | 0.05 µM | C | C2orf74 activity lowers the cells' numbers under Trametinib (DMSO_TF solvate) 0.05 µM (makes them more sensitive) | lines that do not express C2orf74 (13) vs lines expressing it (35) | the lines without C2orf74: 1.26× the cells of the other lines | 0.018 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: C2orf74-DT, ENSG00000286964, NR3C1 |
| [[FIGN]] | 0.05 µM | C | FIGN activity lowers the cells' numbers under Trametinib (DMSO_TF solvate) 0.05 µM (makes them more sensitive) | lines that do not express FIGN (16) vs lines expressing it (32) | the lines without FIGN: 1.25× the cells of the other lines | 0.021 | ⚠ tissue-confounded; across organs; also absent: SPART-AS1, CCDC169, SPART |
| [[RILP]] | 0.5 µM | C | RILP activity raises the cells' numbers under Trametinib (DMSO_TF solvate) 0.5 µM (protects the cells) | lines that do not express RILP (3) vs lines expressing it (45) | the lines without RILP: 0.71× the cells of the other lines | 0.034 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: SAT1, KCP, RABGEF1P3; maybe low, not absent |
| [[STX1A]] | 0.5 µM | C | STX1A activity raises the cells' numbers under Trametinib (DMSO_TF solvate) 0.5 µM (protects the cells) | lines that do not express STX1A (3) vs lines expressing it (45) | the lines without STX1A: 0.70× the cells of the other lines | 0.040 | ⚠ few lines (3 vs 47); across organs; also absent: RABGEF1P3, SKAP2, PYGB; maybe low, not absent |
| [[PSMB8]] | 5 µM | C | PSMB8 activity lowers the cells' numbers under Trametinib (DMSO_TF solvate) 5 µM (makes them more sensitive) | lines that do not express PSMB8 (4) vs lines expressing it (44) | the lines without PSMB8: 1.30× the cells of the other lines | 0.044 | ⚠ few lines (4 vs 46); across organs; co-occurs with WNK2; also absent: TBILA, GCA, C3orf52 |
| [[ENSG00000286964]] | 0.05 µM | C | ENSG00000286964 activity lowers the cells' numbers under Trametinib (DMSO_TF solvate) 0.05 µM (makes them more sensitive) | lines that do not express ENSG00000286964 (10) vs lines expressing it (38) | the lines without ENSG00000286964: 1.22× the cells of the other lines | 0.062 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: SIX1, C2orf74, SYDE1 |
| [[VRK2]] | 5 µM | C | VRK2 activity raises the cells' numbers under Trametinib (DMSO_TF solvate) 5 µM (protects the cells) | lines that do not express VRK2 (4) vs lines expressing it (44) | the lines without VRK2: 0.77× the cells of the other lines | 0.063 | ⚠ few lines (4 vs 46); tissue-confounded; across organs; also absent: PTER, ZC3HAV1L, OSR2 |
| [[SKAP2]] | 0.5 µM | C | SKAP2 activity raises the cells' numbers under Trametinib (DMSO_TF solvate) 0.5 µM (protects the cells) | lines that do not express SKAP2 (3) vs lines expressing it (45) | the lines without SKAP2: 0.74× the cells of the other lines | 0.079 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: IGF2BP2, TCF7, TRIB3; maybe low, not absent |
| [[ENSG00000214265]], [[SNHG14]], [[SNRPN]] | 0.05 µM | C | ENSG00000214265, SNHG14, SNRPN activity lowers the cells' numbers under Trametinib (DMSO_TF solvate) 0.05 µM (makes them more sensitive) | lines that do not express ENSG00000214265, SNHG14, SNRPN (14) vs lines expressing them (34) | the lines without ENSG00000214265, SNHG14, SNRPN: 1.19× the cells of the other lines | 0.084 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: RNF150, CHST10, ENSG00000268163; co-absent genes |
| [[RNF150]] | 0.05 µM | C | RNF150 activity lowers the cells' numbers under Trametinib (DMSO_TF solvate) 0.05 µM (makes them more sensitive) | lines that do not express RNF150 (16) vs lines expressing it (32) | the lines without RNF150: 1.19× the cells of the other lines | 0.093 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: SNRPN, BVES, MPDZ |

### Its targets: what acting on them probably does

*Drug-target arrows of the compound classes it belongs to (compounds sharing a listed target and mechanism; one molecule counts once, under all its names): the target → a gene whose level those compounds move. A row that names several targets is one test: the compounds share them all, and any of them could be the cause. 1,113 arrows, 1,113 of them with an alert ⚠; grade A 0, B 1,113, C 0. Shown: the 15 strongest; 1,098 more arrows (1,098 of them with an alert ⚠) not shown.*

| Its target | Gene it moves | This drug | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|---|
| [[MAP2K1]] | [[ST3GAL6]] | moves it that way too | B | MAP2K1 activity raises ST3GAL6's level | compounds that target MAP2K1: 4 of 4 lower it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 2.8% of all compounds | 0.006 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MAP2K1]] | [[PIH1D1]] | moves it that way too | B | MAP2K1 activity raises PIH1D1's level | compounds that target MAP2K1: 4 of 4 lower it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 3.1% of all compounds | 0.007 | ⚠ off-target possible; 4 compounds |
| [[MAP2K1]] | [[CCT2]] | moves it that way too | B | MAP2K1 activity raises CCT2's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 0.8% of all compounds | 0.007 | ⚠ off-target possible; 3 compounds |
| [[MAP2K1]] | [[EPHA2-AS1]] | moves it that way too | B | MAP2K1 activity raises EPHA2-AS1's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 0.8% of all compounds | 0.007 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[MAP2K1]] | [[LINC00963]] | moves it that way too | B | MAP2K1 activity lowers LINC00963's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 0.8% of all compounds | 0.007 | ⚠ off-target possible; 3 compounds |
| [[MAP2K1]] | [[LRFN5]] | moves it that way too | B | MAP2K1 activity raises LRFN5's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 0.8% of all compounds | 0.007 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[MAP2K1]] | [[PFDN2]] | moves it that way too | B | MAP2K1 activity raises PFDN2's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 0.8% of all compounds | 0.007 | ⚠ off-target possible; 3 compounds |
| [[MAP2K1]] | [[PRKG2-AS1]] | moves it that way too | B | MAP2K1 activity raises PRKG2-AS1's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 0.8% of all compounds | 0.007 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[MAP2K1]] | [[RRP9]] | moves it that way too | B | MAP2K1 activity raises RRP9's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 0.8% of all compounds | 0.007 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[MAP2K1]] | [[TBC1D32]] | moves it that way too | B | MAP2K1 activity lowers TBC1D32's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 0.8% of all compounds | 0.007 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[MAP2K1]] | [[ZNF630]] | moves it that way too | B | MAP2K1 activity lowers ZNF630's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 0.8% of all compounds | 0.007 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[MAP2K1]] | [[FOXL1]] | moves it that way too | B | MAP2K1 activity raises FOXL1's level | compounds that target MAP2K1: 4 of 4 lower it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 3.4% of all compounds | 0.008 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MAP2K1]] | [[DOCK4]] | moves it that way too | B | MAP2K1 activity raises DOCK4's level | compounds that target MAP2K1: 4 of 4 lower it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 3.6% of all compounds | 0.009 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MAP2K1]] | [[KDSR]] | moves it that way too | B | MAP2K1 activity raises KDSR's level | compounds that target MAP2K1: 4 of 4 lower it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 3.6% of all compounds | 0.009 | ⚠ off-target possible; 4 compounds |
| [[MAP2K1]] | [[CDYL2]] | moves it that way too | B | MAP2K1 activity raises CDYL2's level | compounds that target MAP2K1: 4 of 4 lower it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 3.9% of all compounds | 0.010 | ⚠ off-target possible; 4 compounds |

## Data

- `tables/drugs.parquet` — drug == "Trametinib (DMSO_TF solvate)"
- `tables/drugdoses.parquet` — dd in 1036, 1037, 1038
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
