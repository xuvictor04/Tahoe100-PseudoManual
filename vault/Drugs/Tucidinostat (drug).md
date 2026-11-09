---
drug: "Tucidinostat"
type: "drug"
salt_base: "Tucidinostat"
targets: "HDAC1, HDAC2, HDAC3, HDAC10, HDAC8, HDAC11"
moa_fine: "HDAC inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 6657
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Tucidinostat

*HDAC inhibitor (inhibitor/antagonist) · targets: HDAC1, HDAC2, HDAC3, HDAC10, HDAC8, HDAC11 · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 500 / 5512 / 6657; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.05 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.79 / 0.95.
> Flags by dose: - / cell-cycle shift / -. ⚠ 0.5 µM: cell-cycle shift (artifact flags: its changes there are shown with an alert, not left out).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 04]]:F3 | 465 / 35 | — | +0.22 | -1.7/-0.8/-1.7 | — |
| 0.5 µM | [[Plate 05]]:F3 | 4,178 / 1,334 | — | -0.04 | -4.3/-0.9/-3.4 | ⚠ cell-cycle shift |
| 5 µM | [[Plate 14]]:F3 | 5,068 / 1,589 | 0.913 | +0.05 | -3.4/+0.2/-3.6 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (465 genes, none with an alert; 12 shown): [[RGS9]] 1.94× (z +10.2, 24/42 lines), [[PLEKHH2]] 1.48× (z +8.0, 16/34 lines), [[L3MBTL3]] 1.68× (z +7.9, 29/45 lines), [[SEMA6B]] 1.81× (z +7.7, 20/33 lines), [[TOM1L1]] 1.24× (z +6.7, 29/48 lines), [[OLFM2]] 1.52× (z +6.6, 14/33 lines), [[KIAA0319]] 1.52× (z +6.6, 13/29 lines), [[NOVA2]] 2.01× (z +6.4, 14/24 lines), [[RAB6B]] 1.44× (z +6.3, 16/33 lines), [[GRAMD1C]] 1.46× (z +6.3, 26/44 lines), [[TLCD4]] 1.36× (z +6.2, 21/36 lines), [[CYFIP2]] 1.41× (z +6.2, 21/37 lines)

**0.5 µM** (4178 genes, 262 with an alert ⚠; the drug-dose carries ⚠ cell-cycle shift; 12 shown): [[B3GALT1]] 3.92× (z +24.5, 24/27 lines; cell-cycle shift (explains ~0% here)), [[RGS9]] 4.70× (z +23.7, 37/39 lines; cell-cycle shift (explains ~0% here)), [[MED12L]] 4.32× (z +22.0, 25/28 lines; cell-cycle shift (explains ~0% here)), [[PLEKHH2]] 2.92× (z +21.6, 33/34 lines; cell-cycle shift (explains ~0% here)), [[ENSG00000283674]] 3.31× (z +20.7, 31/31 lines; cell-cycle shift (explains ~0% here)), [[DOCK3]] 2.83× (z +19.7, 22/26 lines; cell-cycle shift (explains ~1% here)), [[CHRM3]] 2.93× (z +19.6, 23/26 lines; cell-cycle shift (explains ~0% here)), [[CACNA1C]] 3.07× (z +19.4, 30/33 lines; cell-cycle shift (explains ~0% here)), [[MTUS2]] 5.04× (z +19.3, 35/41 lines; cell-cycle shift (explains ~0% here)), [[CYFIP2]] 2.90× (z +19.3, 35/37 lines; cell-cycle shift (explains ~0% here)), [[SGSM1]] 3.72× (z +19.1, 35/39 lines; cell-cycle shift (explains ~2% here)), [[OTUD7A]] 2.82× (z +19.0, 38/40 lines; cell-cycle shift (explains ~0% here))

**5 µM** (5068 genes, none with an alert; 12 shown): [[B3GALT1]] 5.81× (z +43.3, 25/28 lines), [[OTUD7A]] 3.86× (z +35.1, 40/42 lines), [[NRXN3]] 4.31× (z +34.4, 25/25 lines), [[RGS9]] 4.84× (z +34.2, 39/42 lines), [[PARM1]] 5.28× (z +32.8, 17/20 lines), [[MTUS2]] 6.68× (z +32.1, 42/45 lines), [[SH3GL2]] 7.41× (z +31.9, 24/25 lines), [[RGS7]] 4.76× (z +31.7, 21/23 lines), [[ENSG00000283674]] 3.55× (z +31.0, 30/32 lines), [[SYT11]] 6.16× (z +30.6, 23/23 lines), [[WDR17]] 5.11× (z +30.6, 30/30 lines), [[SEMA6A]] 4.13× (z +30.0, 28/29 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (35 genes, none with an alert; 12 shown): [[EFCAB11]] 0.759× (z -5.1, 20/48 lines), [[TRAF3IP1]] 0.797× (z -5.0, 20/48 lines), [[MTOR]] 0.785× (z -4.8, 24/48 lines), [[ADI1]] 0.752× (z -4.8, 20/48 lines), [[LIN52]] 0.828× (z -4.3, 18/48 lines), [[ARID1B]] 0.822× (z -4.2, 25/47 lines), [[VPS18]] 0.752× (z -4.1, 6/46 lines), [[CRAMP1]] 0.812× (z -4.0, 19/48 lines), [[VAMP3]] 0.824× (z -4.0, 14/48 lines), [[UBR7]] 0.809× (z -3.9, 9/48 lines), [[CRPPA]] 0.731× (z -3.8, 14/42 lines), [[NRL]] 0.722× (z -3.8, 4/44 lines)

**0.5 µM** (1334 genes, 277 with an alert ⚠; the drug-dose carries ⚠ cell-cycle shift; 12 shown): [[WASHC2A]] 0.521× (z -13.7, 41/48 lines; cell-cycle shift (explains ~0% here)), [[TOPBP1]] 0.594× (z -13.2, 47/49 lines; cell-cycle shift (explains ~11% here)), [[EFCAB2]] 0.470× (z -12.6, 41/48 lines; cell-cycle shift (explains ~0% here)), [[TCTN2]] 0.490× (z -12.2, 36/46 lines; cell-cycle shift (explains ~0% here)), [[CSNK1G1]] 0.676× (z -11.8, 44/49 lines; cell-cycle shift (explains ~3% here)), [[ARID1B]] 0.580× (z -11.7, 48/48 lines; cell-cycle shift (explains ~0% here)), [[TRAF3IP1]] 0.591× (z -11.7, 43/48 lines; cell-cycle shift (explains ~6% here)), [[WASHC2C]] 0.558× (z -11.6, 39/47 lines; cell-cycle shift (explains ~0% here)), [[LRRC41]] 0.578× (z -11.2, 44/48 lines; cell-cycle shift (explains ~0% here)), [[CREBBP]] 0.693× (z -11.0, 43/49 lines; cell-cycle shift (explains ~0% here)), [[CRAMP1]] 0.569× (z -10.9, 42/49 lines; cell-cycle shift (explains ~3% here)), [[KAT6B]] 0.654× (z -10.7, 44/49 lines; cell-cycle shift (explains ~0% here))

**5 µM** (1589 genes, none with an alert; 12 shown): [[WASHC2C]] 0.531× (z -17.8, 45/47 lines), [[INO80D]] 0.602× (z -17.3, 45/48 lines), [[BBX]] 0.704× (z -17.2, 41/48 lines), [[EFCAB2]] 0.488× (z -16.9, 47/48 lines), [[CREBBP]] 0.674× (z -16.7, 47/48 lines), [[WASHC2A]] 0.574× (z -16.6, 45/48 lines), [[SENP6]] 0.674× (z -16.3, 44/48 lines), [[CSNK1G1]] 0.683× (z -16.2, 44/48 lines), [[ARID1B]] 0.590× (z -16.0, 47/47 lines), [[LRRC41]] 0.578× (z -15.8, 47/48 lines), [[KIAA0753]] 0.565× (z -15.6, 48/48 lines), [[CUL1]] 0.693× (z -14.8, 43/48 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | [[Module 208]] (+3.0), [[Module 115]] (+2.9), [[Module 100]] (+2.7) | [[Module 194]] (-3.2), [[Module 207]] (-2.8), [[Module 036]] (-2.7) |
| 0.5 µM | [[Module 115]] (+10.0), [[Module 082]] (+8.2), [[Module 102]] (+8.0) | [[Module 207]] (-11.4), [[Module 095]] (-9.0), [[Module 194]] (-8.7) |
| 5 µM | [[Module 115]] (+15.6), [[Module 061]] (+13.9), [[Module 191]] (+13.1) | [[Module 207]] (-15.7), [[Module 095]] (-14.8), [[Module 194]] (-13.0) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | [[BT-474 (line)]] (1.49), [[NCI-H2347 (line)]] (1.39), [[Panc 03.27 (line)]] (1.30), [[SW480 (line)]] (1.28) · weakest: [[AsPC-1 (line)]] (0.308), [[NCI-H661 (line)]] (0.475), [[NCI-H1792 (line)]] (0.509) |
| 0.5 µM | — | [[SW480 (line)]] (1.37), [[BT-474 (line)]] (1.36), [[NCI-H460 (line)]] (1.34), [[C32 (line)]] (1.31) · weakest: [[AsPC-1 (line)]] (0.430), [[SNU-1 (line)]] (0.588), [[NCI-H2122 (line)]] (0.595) |
| 5 µM | — | [[SW480 (line)]] (1.35), [[SW1417 (line)]] (1.34), [[NCI-H460 (line)]] (1.31), [[C32 (line)]] (1.31) · weakest: [[SNU-1 (line)]] (0.597), [[AsPC-1 (line)]] (0.641), [[AN3 CA (line)]] (0.673) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 2 next most similar without an alert.*

- [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] (+0.50, Glucose transporter inhibitor); [[Brivudine (drug)]] (+0.48, unclear); [[Simotinib (drug)]] (+0.45, EGFR/ERBB inhibitor, ⚠ vector dose flagged: toxic); [[Bicalutamide (drug)]] (+0.45, Androgen receptor antagonist); [[Omeprazole (sodium) (drug)]] (+0.45, unclear); [[AZD2858 (drug)]] (+0.44, GSK3 inhibitor, ⚠ vector dose flagged: toxic); [[Bendamustine (drug)]] (+0.42, DNA synthesis/repair inhibitor); [[Pimozide (drug)]] (+0.41, unclear); [[Saquinavir (drug)]] (+0.40, unclear); [[Flutamide (drug)]] (+0.39, Androgen receptor antagonist)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 11 arrows, 11 of them with an alert ⚠; grade A 0, B 4, C 7.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[GAP43]] | 5 µM | B | GAP43 activity lowers the cells' numbers under Tucidinostat 5 µM (makes them more sensitive) | lines that do not express GAP43 (22) vs lines expressing it (26) | the lines without GAP43: 1.11× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; also absent: ENSG00000287622, ENSG00000242880, ENSG00000286540; maybe low, not absent |
| [[XK]] | 5 µM | B | XK activity raises the cells' numbers under Tucidinostat 5 µM (protects the cells) | lines that do not express XK (18) vs lines expressing it (30) | the lines without XK: 0.90× the cells of the other lines | 0.077 | ⚠ within organs, on part of the lines; also absent: SAMD12, MARVELD2, BTC; maybe low, not absent |
| [[GREB1L]] | 5 µM | B | GREB1L activity raises the cells' numbers under Tucidinostat 5 µM (protects the cells) | lines that do not express GREB1L (19) vs lines expressing it (29) | the lines without GREB1L: 0.92× the cells of the other lines | 0.083 | ⚠ within organs, on part of the lines; also absent: ADAMTSL3, ZYG11A, CNNM1 |
| [[TDRD9]] | 5 µM | B | TDRD9 activity lowers the cells' numbers under Tucidinostat 5 µM (makes them more sensitive) | lines that do not express TDRD9 (37) vs lines expressing it (11) | the lines without TDRD9: 1.11× the cells of the other lines | 0.091 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GDNF, ITIH5, DCT |
| [[HPS1]] | 5 µM | C | HPS1 activity raises the cells' numbers under Tucidinostat 5 µM (protects the cells) | lines that do not express HPS1 (3) vs lines expressing it (45) | the lines without HPS1: 0.80× the cells of the other lines | 0.019 | ⚠ few lines (3 vs 47); across organs; also absent: SH3D19, PWWP2B, APOBEC3B; maybe low, not absent |
| [[TNFRSF10D]] | 5 µM | C | TNFRSF10D activity raises the cells' numbers under Tucidinostat 5 µM (protects the cells) | lines that do not express TNFRSF10D (11) vs lines expressing it (37) | the lines without TNFRSF10D: 0.89× the cells of the other lines | 0.041 | ⚠ tissue-confounded; across organs; also absent: OPLAH, LINC00857, LPIN3 |
| [[VRK2]] | 5 µM | C | VRK2 activity raises the cells' numbers under Tucidinostat 5 µM (protects the cells) | lines that do not express VRK2 (4) vs lines expressing it (44) | the lines without VRK2: 0.85× the cells of the other lines | 0.041 | ⚠ few lines (4 vs 46); tissue-confounded; across organs; also absent: PTER, ZC3HAV1L, OSR2 |
| [[SH3D19]] | 5 µM | C | SH3D19 activity raises the cells' numbers under Tucidinostat 5 µM (protects the cells) | lines that do not express SH3D19 (3) vs lines expressing it (45) | the lines without SH3D19: 0.84× the cells of the other lines | 0.042 | ⚠ few lines (3 vs 47); across organs; also absent: HPS1, APOBEC3B; maybe low, not absent |
| [[PTER]] | 5 µM | C | PTER activity raises the cells' numbers under Tucidinostat 5 µM (protects the cells) | lines that do not express PTER (6) vs lines expressing it (42) | the lines without PTER: 0.88× the cells of the other lines | 0.083 | ⚠ tissue-confounded; across organs; also absent: ENSG00000287925, VRK2, ZC3HAV1L |
| [[OSR2]] | 5 µM | C | OSR2 activity raises the cells' numbers under Tucidinostat 5 µM (protects the cells) | lines that do not express OSR2 (5) vs lines expressing it (43) | the lines without OSR2: 0.88× the cells of the other lines | 0.093 | ⚠ tissue-confounded; across organs; also absent: ZC3HAV1L, TACC2, VRK2; maybe low, not absent |
| [[APOBEC3B]] | 5 µM | C | APOBEC3B activity raises the cells' numbers under Tucidinostat 5 µM (protects the cells) | lines that do not express APOBEC3B (3) vs lines expressing it (45) | the lines without APOBEC3B: 0.84× the cells of the other lines | 0.097 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: HSD3B7, KDELR3, HPS1 |

### Its targets: what acting on them probably does

*Drug-target arrows of the compound classes it belongs to (compounds sharing a listed target and mechanism; one molecule counts once, under all its names): the target → a gene whose level those compounds move. A row that names several targets is one test: the compounds share them all, and any of them could be the cause. 599 arrows, 599 of them with an alert ⚠; grade A 0, B 599, C 0. Shown: the 15 strongest; 584 more arrows (584 of them with an alert ⚠) not shown.*

| Its target | Gene it moves | This drug | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | [[CDC23]] | moves it that way too | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises CDC23's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | [[CMIP]] | moves it that way too | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers CMIP's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | [[CROCCP3]] | moves it that way too | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers CROCCP3's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | [[CYB561]] | moves it that way too | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises CYB561's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | [[DNAJC2]] | moves it that way too | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises DNAJC2's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | [[ENSG00000288899]] | moves it that way too | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises ENSG00000288899's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | [[FAM78B]] | moves it that way too | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers FAM78B's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | [[FBXW9]] | moves it that way too | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises FBXW9's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | [[FMN1]] | moves it that way too | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers FMN1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | [[LRRC51]] | moves it that way too | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises LRRC51's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | [[MRPS7]] | moves it that way too | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises MRPS7's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | [[NCBP3]] | moves it that way too | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises NCBP3's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | [[RAPGEF5]] | moves it that way too | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers RAPGEF5's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | [[REXO1]] | moves it that way too | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises REXO1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | [[AMOTL1]] | moves it that way too | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers AMOTL1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |

## Data

- `tables/drugs.parquet` — drug == "Tucidinostat"
- `tables/drugdoses.parquet` — dd in 1060, 1061, 1062
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
