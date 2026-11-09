---
drug: "Trametinib"
type: "drug"
salt_base: "Trametinib"
targets: "MAP2K1, MAP2K2"
moa_fine: "MEK inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 1994
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Trametinib

*MEK inhibitor (inhibitor/antagonist) · targets: MAP2K1, MAP2K2 · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 1142 / 1803 / 1994; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.05 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.75 / 0.83.
> Flags by dose: - / noisy plate (z scaled) / cell-cycle shift; noisy plate (z scaled). ⚠ 5 µM: cell-cycle shift (artifact flags: its changes there are shown with an alert, not left out).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 01]]:C11, [[Plate 10]]:F9 | 647 / 495 | 0.841 | -0.39 | -3.6/-3.0/-2.5 | — |
| 0.5 µM | [[Plate 11]]:C11, [[Plate 02]]:F9 | 1,072 / 731 | 0.943 | -0.14 | -3.9/-1.7/-0.8 | noisy plate (z scaled) |
| 5 µM | [[Plate 12]]:C11, [[Plate 03]]:F9 | 964 / 1,030 | 0.916 | +0.95 | -4.5/-2.7/-2.7 | ⚠ cell-cycle shift · noisy plate (z scaled) |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (647 genes, none with an alert; 12 shown): [[GBP2]] 1.78× (z +11.2, 30/35 lines), [[CFB]] 1.98× (z +8.4, 21/28 lines), [[GBP1]] 1.73× (z +7.0, 26/32 lines), [[ENSG00000283782]] 1.24× (z +6.6, 30/48 lines), [[TLR3]] 1.77× (z +6.6, 22/36 lines), [[ARID5B]] 1.35× (z +6.5, 30/42 lines), [[TMEM140]] 1.65× (z +6.5, 23/38 lines), [[POT1-AS1]] 1.68× (z +6.4, 22/45 lines), [[TP53INP1]] 1.58× (z +6.4, 23/40 lines), [[TNS3]] 1.45× (z +6.4, 34/40 lines), [[LINC02100]] 1.44× (z +6.3, 20/39 lines), [[MAP2]] 1.55× (z +6.1, 20/33 lines)

**0.5 µM** (1072 genes, none with an alert; 12 shown): [[GBP2]] 2.37× (z +14.1, 33/35 lines), [[CFB]] 3.35× (z +13.2, 25/28 lines), [[PGM2L1]] 1.43× (z +9.5, 25/44 lines), [[GBP1]] 2.35× (z +9.5, 30/32 lines), [[ARID5B]] 1.54× (z +8.2, 32/42 lines), [[OLFML2A]] 1.84× (z +7.8, 13/27 lines), [[SELENOP]] 2.14× (z +7.8, 19/25 lines), [[PALLD]] 1.44× (z +7.7, 27/37 lines), [[POT1-AS1]] 1.83× (z +7.7, 28/44 lines), [[CLIP1]] 1.23× (z +7.6, 26/48 lines), [[LINC02057]] 1.95× (z +7.6, 19/23 lines), [[MVP-DT]] 1.80× (z +7.6, 30/46 lines)

**5 µM** (964 genes, 548 with an alert ⚠; the drug-dose carries ⚠ cell-cycle shift; 12 shown): [[GBP2]] 2.88× (z +15.1, 34/36 lines; cell-cycle shift (explains ~7% here)), [[CFB]] 3.71× (z +12.5, 26/28 lines; cell-cycle shift (explains ~6% here)), [[ARID5B]] 1.90× (z +10.3, 36/44 lines; cell-cycle shift (explains ~2% here)), [[GBP1]] 2.61× (z +9.8, 31/32 lines; cell-cycle shift (explains ~0% here)), [[CLIP1]] 1.40× (z +9.8, 36/50 lines; cell-cycle shift (explains ~15% here)), [[DUSP16]] 1.52× (z +9.1, 35/48 lines; cell-cycle shift (explains ~20% here)), [[POT1-AS1]] 2.23× (z +8.5, 31/47 lines; cell-cycle shift (explains ~11% here)), [[PHLDB2]] 1.69× (z +8.2, 27/39 lines; cell-cycle shift (explains ~20% here)), [[PALLD]] 1.57× (z +8.1, 29/39 lines; cell-cycle shift (explains ~0% here)), [[SORBS2]] 1.66× (z +7.8, 22/33 lines; cell-cycle shift (explains ~23% here)), [[PGM2L1]] 1.38× (z +7.8, 26/46 lines; cell-cycle shift (explains ~12% here)), [[MYOF]] 1.41× (z +7.6, 30/44 lines; cell-cycle shift (explains ~23% here))

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (495 genes, none with an alert; 12 shown): [[ETV5]] 0.409× (z -27.3, 46/48 lines), [[SPRY4]] 0.349× (z -19.2, 46/48 lines), [[EGR1]] 0.217× (z -16.5, 46/46 lines), [[DUSP6]] 0.286× (z -15.5, 43/44 lines), [[ETV4]] 0.488× (z -15.3, 41/46 lines), [[ZFPM2-AS1]] 0.620× (z -11.9, 28/32 lines), [[ETV1]] 0.509× (z -11.7, 33/37 lines), [[MYEOV]] 0.505× (z -10.9, 26/29 lines), [[FOSL1]] 0.471× (z -10.4, 41/43 lines), [[ELK3]] 0.642× (z -10.2, 35/44 lines), [[MCL1]] 0.651× (z -10.0, 44/48 lines), [[ITGA2]] 0.589× (z -9.8, 33/37 lines)

**0.5 µM** (731 genes, none with an alert; 12 shown): [[ETV5]] 0.223× (z -40.2, 48/48 lines), [[SPRY4]] 0.199× (z -26.2, 48/48 lines), [[ZFPM2-AS1]] 0.370× (z -22.6, 32/32 lines), [[ETV4]] 0.340× (z -20.2, 41/46 lines), [[SPRY4-AS1]] 0.242× (z -18.4, 45/45 lines), [[DUSP6]] 0.176× (z -18.4, 44/44 lines), [[EGR1]] 0.173× (z -16.9, 46/46 lines), [[SPRED2]] 0.422× (z -16.5, 48/48 lines), [[ETV1]] 0.344× (z -16.5, 36/37 lines), [[ITGA2]] 0.385× (z -16.0, 36/37 lines), [[NT5E]] 0.350× (z -15.9, 32/34 lines), [[MYEOV]] 0.326× (z -15.7, 27/29 lines)

**5 µM** (1030 genes, 313 with an alert ⚠; the drug-dose carries ⚠ cell-cycle shift; 12 shown): [[ETV5]] 0.107× (z -45.5, 49/50 lines; cell-cycle shift (explains ~3% here)), [[SPRY4]] 0.0967× (z -27.9, 48/49 lines; cell-cycle shift (explains ~2% here)), [[SPRY4-AS1]] 0.122× (z -23.0, 47/47 lines; cell-cycle shift (explains ~0% here)), [[ETV4]] 0.185× (z -22.5, 45/46 lines; cell-cycle shift (explains ~4% here)), [[ETV1]] 0.142× (z -22.3, 37/38 lines; cell-cycle shift (explains ~4% here)), [[ZFPM2-AS1]] 0.318× (z -22.2, 33/34 lines; cell-cycle shift (explains ~0% here)), [[DUSP6]] 0.0700× (z -21.6, 45/46 lines; cell-cycle shift (explains ~5% here)), [[EGR1]] 0.0643× (z -20.5, 48/48 lines; cell-cycle shift (explains ~7% here)), [[MYEOV]] 0.187× (z -20.0, 29/29 lines; cell-cycle shift (explains ~1% here)), [[ENSG00000260877]] 0.170× (z -18.7, 33/34 lines; cell-cycle shift (explains ~0% here)), [[DUSP4]] 0.301× (z -18.1, 33/35 lines; cell-cycle shift (explains ~0% here)), [[NT5E]] 0.233× (z -17.4, 34/36 lines; cell-cycle shift (explains ~0% here))

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | [[Module 146]] (+3.8), [[Module 046]] (+3.6), [[Module 230]] (+3.1) | [[Module 174]] (-6.0), [[Module 092]] (-4.2), [[Module 235]] (-3.8) |
| 0.5 µM | [[Module 059]] (+4.5), [[Module 182]] (+3.6), [[Module 070]] (+3.6) | [[Module 174]] (-9.1), [[Module 092]] (-7.0), [[Module 147]] (-5.6) |
| 5 µM | [[Module 046]] (+3.9), [[Module 135]] (+3.5), [[Module 171]] (+3.4) | [[Module 174]] (-9.8), [[Module 092]] (-8.0), [[Module 147]] (-6.0) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | [[NCI-H1792 (line)]] (-5.1) | [[NCI-H23 (line)]] (1.52), [[SW480 (line)]] (1.50), [[MIA PaCa-2 (line)]] (1.38), [[AsPC-1 (line)]] (1.35) · weakest: [[NCI-H661 (line)]] (0.422), [[hTERT-HPNE (line)]] (0.620), [[CHP-212 (line)]] (0.628) |
| 0.5 µM | [[NCI-H1792 (line)]] (-8.1), [[CHP-212 (line)]] (-6.0), [[SK-MEL-2 (line)]] (-5.1), [[COLO 205 (line)]] (-4.9), [[LoVo (line)]] (-4.5) | [[AsPC-1 (line)]] (1.54), [[NCI-H23 (line)]] (1.39), [[HOP62 (line)]] (1.35), [[MIA PaCa-2 (line)]] (1.32) · weakest: [[NCI-H661 (line)]] (0.433), [[AN3 CA (line)]] (0.691), [[SW 1271 (line)]] (0.717) |
| 5 µM | [[NCI-H1792 (line)]] (-12.6), [[CHP-212 (line)]] (-7.7), [[SK-MEL-2 (line)]] (-7.4), [[COLO 205 (line)]] (-5.0), [[LoVo (line)]] (-3.9) | [[AsPC-1 (line)]] (1.37), [[NCI-H23 (line)]] (1.36), [[MIA PaCa-2 (line)]] (1.36), [[NCI-H1573 (line)]] (1.35) · weakest: [[NCI-H596 (line)]] (0.489), [[NCI-H2122 (line)]] (0.513), [[NCI-H661 (line)]] (0.559) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

⚠ This drug's own vector: vector dose flagged: cell-cycle shift. Read its neighbours with that in mind.

*378 other drugs have a vector, 121 with an alert ⚠; shown: the 8 most similar.*

- [[Binimetinib (drug)]] (+0.92, MEK inhibitor); [[Trametinib (DMSO_TF solvate) (drug)]] (+0.91, MEK inhibitor); [[Elimusertib hydrochloride (drug)]] (+0.90, unclear); [[BI-3406 (drug)]] (+0.88, RAS inhibitor); [[Cobimetinib (drug)]] (+0.83, MEK inhibitor); [[Bimiralisib (drug)]] (+0.82, PI3K/AKT inhibitor); [[RMC-6236 (drug)]] (+0.82, RAS inhibitor); [[Perindopril (erbumine) (drug)]] (+0.73, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 10 arrows, 10 of them with an alert ⚠; grade A 0, B 2, C 8.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[AFAP1L2]] | 0.05 µM | B | AFAP1L2 activity lowers the cells' numbers under Trametinib 0.05 µM (makes them more sensitive) | lines that do not express AFAP1L2 (27) vs lines expressing it (21) | the lines without AFAP1L2: 1.11× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: LY75, ENSG00000235726, SHH |
| [[PDE3B]] | 0.5 µM | B | PDE3B activity lowers the cells' numbers under Trametinib 0.5 µM (makes them more sensitive) | lines that do not express PDE3B (20) vs lines expressing it (28) | the lines without PDE3B: 1.21× the cells of the other lines | 0.089 | ⚠ within organs, on part of the lines; also absent: ENSG00000250049, MIR4458HG, ASB4 |
| [[SDC3]] | 0.5 µM | C | SDC3 activity raises the cells' numbers under Trametinib 0.5 µM (protects the cells) | lines that do not express SDC3 (4) vs lines expressing it (44) | the lines without SDC3: 0.66× the cells of the other lines | 0.010 | ⚠ few lines (4 vs 46); across organs |
| [[SDC3]] | 5 µM | C | SDC3 activity raises the cells' numbers under Trametinib 5 µM (protects the cells) | lines that do not express SDC3 (4) vs lines expressing it (44) | the lines without SDC3: 0.64× the cells of the other lines | 0.028 | ⚠ few lines (4 vs 46); across organs |
| [[ENSG00000256029]] | 0.05 µM | C | ENSG00000256029 activity lowers the cells' numbers under Trametinib 0.05 µM (makes them more sensitive) | lines that do not express ENSG00000256029 (4) vs lines expressing it (44) | the lines without ENSG00000256029: 1.21× the cells of the other lines | 0.035 | ⚠ few lines (4 vs 46); across organs; also absent: ERRFI1, FXYD5, CAV2; maybe low, not absent |
| [[SKAP2]] | 5 µM | C | SKAP2 activity raises the cells' numbers under Trametinib 5 µM (protects the cells) | lines that do not express SKAP2 (3) vs lines expressing it (45) | the lines without SKAP2: 0.64× the cells of the other lines | 0.041 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: IGF2BP2, TCF7, TRIB3; maybe low, not absent |
| [[RILP]] | 5 µM | C | RILP activity raises the cells' numbers under Trametinib 5 µM (protects the cells) | lines that do not express RILP (3) vs lines expressing it (45) | the lines without RILP: 0.64× the cells of the other lines | 0.066 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: SAT1, KCP, RABGEF1P3; maybe low, not absent |
| [[LITAF]] | 5 µM | C | LITAF activity raises the cells' numbers under Trametinib 5 µM (protects the cells) | lines that do not express LITAF (3) vs lines expressing it (45) | the lines without LITAF: 0.64× the cells of the other lines | 0.075 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: SAT1, KIAA1522, SKAP2 |
| [[ERRFI1]] | 0.05 µM | C | ERRFI1 activity lowers the cells' numbers under Trametinib 0.05 µM (makes them more sensitive) | lines that do not express ERRFI1 (4) vs lines expressing it (44) | the lines without ERRFI1: 1.18× the cells of the other lines | 0.088 | ⚠ few lines (4 vs 46); across organs; also absent: ENSG00000256029; maybe low, not absent |
| [[STX1A]] | 0.5 µM | C | STX1A activity raises the cells' numbers under Trametinib 0.5 µM (protects the cells) | lines that do not express STX1A (3) vs lines expressing it (45) | the lines without STX1A: 0.72× the cells of the other lines | 0.090 | ⚠ few lines (3 vs 47); across organs; also absent: RABGEF1P3, SKAP2, PYGB; maybe low, not absent |

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

- `tables/drugs.parquet` — drug == "Trametinib"
- `tables/drugdoses.parquet` — dd in 1033, 1034, 1035
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
