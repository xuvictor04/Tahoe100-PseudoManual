---
drug: "Belinostat"
type: "drug"
salt_base: "Belinostat"
targets: "HDAC6"
moa_fine: "HDAC inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 9818
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Belinostat

*HDAC inhibitor (inhibitor/antagonist) · targets: HDAC6 · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 178 / 5244 / 9818; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.05 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.73 / 0.82.
> Flags by dose: - / cell-cycle shift / cell-cycle shift. ⚠ 0.5 µM: cell-cycle shift; 5 µM: cell-cycle shift (artifact flags: its changes there are shown with an alert, not left out).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 10]]:A10 | 61 / 117 | — | -0.02 | +0.8/+0.3/+1.0 | — |
| 0.5 µM | [[Plate 11]]:A10 | 2,973 / 2,271 | — | -0.92 | +4.3/+1.3/+1.7 | ⚠ cell-cycle shift |
| 5 µM | [[Plate 12]]:A10 | 5,322 / 4,496 | — | -0.13 | +14.4/+3.2/+1.7 | ⚠ cell-cycle shift |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (61 genes, none with an alert; 12 shown): [[CCDC126]] 1.39× (z +6.1, 19/48 lines), [[MEGF9]] 1.23× (z +5.2, 15/48 lines), [[TPST2]] 1.22× (z +4.6, 11/48 lines), [[MITF]] 1.28× (z +4.4, 7/39 lines), [[GFOD2]] 1.22× (z +4.4, 15/48 lines), [[ADGRL1]] 1.21× (z +4.2, 9/41 lines), [[LIN52]] 1.20× (z +4.2, 12/48 lines), [[CASTOR2]] 1.29× (z +4.1, 9/47 lines), [[PINX1]] 1.25× (z +4.1, 5/47 lines), [[PACC1]] 1.24× (z +3.8, 5/47 lines), [[PLCXD2]] 1.33× (z +3.7, 5/41 lines), [[ASMTL]] 1.21× (z +3.7, 11/48 lines)

**0.5 µM** (2973 genes, 685 with an alert ⚠; the drug-dose carries ⚠ cell-cycle shift; 12 shown): [[MEGF9]] 2.30× (z +21.3, 46/47 lines; cell-cycle shift (explains ~4% here)), [[B3GALT1]] 2.99× (z +19.6, 25/27 lines; cell-cycle shift (explains ~7% here)), [[CASTOR2]] 3.08× (z +18.3, 44/47 lines; cell-cycle shift (explains ~0% here)), [[MITF]] 2.74× (z +18.1, 34/39 lines; cell-cycle shift (explains ~5% here)), [[ADGRL1]] 2.21× (z +17.0, 39/41 lines; cell-cycle shift (explains ~7% here)), [[DPF3]] 3.63× (z +16.7, 26/27 lines; cell-cycle shift (explains ~9% here)), [[EDA]] 2.76× (z +16.0, 34/34 lines; cell-cycle shift (explains ~1% here)), [[CCDC126]] 2.32× (z +15.8, 42/47 lines; cell-cycle shift (explains ~2% here)), [[ZNF277]] 1.79× (z +15.6, 46/48 lines; cell-cycle shift (explains ~4% here)), [[STRBP]] 1.59× (z +15.2, 41/47 lines; cell-cycle shift (explains ~10% here)), [[DOCK4]] 1.96× (z +14.5, 24/34 lines; cell-cycle shift (explains ~7% here)), [[OSBPL6]] 2.04× (z +14.5, 33/35 lines; cell-cycle shift (explains ~10% here))

**5 µM** (5322 genes, 2,005 with an alert ⚠; the drug-dose carries ⚠ cell-cycle shift; 12 shown): [[RGL1]] 10.5× (z +45.5, 42/44 lines; cell-cycle shift (explains ~8% here)), [[DPF3]] 31.9× (z +45.0, 34/34 lines; cell-cycle shift (explains ~11% here)), [[B3GALT1]] 12.2× (z +44.9, 26/27 lines; cell-cycle shift (explains ~10% here)), [[SORBS1]] 7.30× (z +37.8, 40/41 lines; cell-cycle shift (explains ~6% here)), [[OTUD7A]] 7.60× (z +37.2, 41/41 lines; cell-cycle shift (explains ~3% here)), [[TYW1B]] 7.10× (z +34.6, 48/48 lines; cell-cycle shift (explains ~12% here)), [[MEGF9]] 3.85× (z +34.5, 48/48 lines; cell-cycle shift (explains ~8% here)), [[AGFG2]] 9.09× (z +33.9, 46/47 lines; cell-cycle shift (explains ~4% here)), [[STK4]] 2.45× (z +33.7, 48/48 lines; cell-cycle shift (explains ~12% here)), [[ATP8A1]] 6.15× (z +33.3, 34/35 lines; cell-cycle shift (explains ~0% here)), [[PTPN1]] 3.63× (z +33.1, 48/48 lines; cell-cycle shift (explains ~16% here)), [[EFR3B]] 7.31× (z +32.7, 35/37 lines; cell-cycle shift (explains ~18% here))

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (117 genes, none with an alert; 12 shown): [[EFCAB2]] 0.605× (z -8.4, 37/48 lines), [[PMF1]] 0.713× (z -7.7, 29/47 lines), [[KAT6B]] 0.765× (z -6.7, 42/48 lines), [[ENSG00000232884]] 0.532× (z -6.5, 14/32 lines), [[DHRSX]] 0.776× (z -6.2, 35/47 lines), [[EPC1]] 0.816× (z -6.0, 27/48 lines), [[ERAP1]] 0.773× (z -5.5, 28/48 lines), [[LANCL2]] 0.710× (z -5.1, 34/48 lines), [[ARSD]] 0.671× (z -5.0, 24/42 lines), [[PARVA]] 0.760× (z -4.8, 29/42 lines), [[RCBTB2]] 0.619× (z -4.8, 19/44 lines), [[FAR2]] 0.750× (z -4.7, 10/29 lines)

**0.5 µM** (2271 genes, 575 with an alert ⚠; the drug-dose carries ⚠ cell-cycle shift; 12 shown): [[KAT6B]] 0.349× (z -26.5, 48/48 lines; cell-cycle shift (explains ~6% here)), [[DHRSX]] 0.358× (z -25.1, 47/47 lines; cell-cycle shift (explains ~11% here)), [[PMF1]] 0.370× (z -22.5, 44/46 lines; cell-cycle shift (explains ~3% here)), [[EFCAB2]] 0.302× (z -20.0, 46/47 lines; cell-cycle shift (explains ~3% here)), [[KMT5B]] 0.548× (z -18.8, 48/48 lines; cell-cycle shift (explains ~12% here)), [[SENP6]] 0.532× (z -18.4, 48/48 lines; cell-cycle shift (explains ~9% here)), [[FBXW4]] 0.383× (z -17.8, 46/48 lines; cell-cycle shift (explains ~9% here)), [[PBRM1]] 0.564× (z -17.8, 48/48 lines; cell-cycle shift (explains ~3% here)), [[CREBBP]] 0.558× (z -17.5, 47/48 lines; cell-cycle shift (explains ~6% here)), [[PHF11]] 0.367× (z -17.0, 41/43 lines; cell-cycle shift (explains ~7% here)), [[ZFX]] 0.457× (z -16.8, 47/48 lines; cell-cycle shift (explains ~5% here)), [[ZNF33A]] 0.570× (z -16.2, 47/48 lines; cell-cycle shift (explains ~16% here))

**5 µM** (4496 genes, 1,870 with an alert ⚠; the drug-dose carries ⚠ cell-cycle shift; 13 shown): [[DHRSX]] 0.143× (z -47.4, 47/47 lines; cell-cycle shift (explains ~19% here)), [[CUL1]] 0.200× (z -45.9, 48/48 lines; cell-cycle shift (explains ~7% here)), [[SENP6]] 0.209× (z -45.7, 48/48 lines; cell-cycle shift (explains ~11% here)), [[ZFX]] 0.157× (z -39.6, 48/48 lines; cell-cycle shift (explains ~7% here)), [[MAP3K20]] 0.337× (z -39.3, 47/47 lines; cell-cycle shift (explains ~11% here)), [[TLK1]] 0.323× (z -36.1, 48/48 lines; cell-cycle shift (explains ~12% here)), [[KAT6B]] 0.242× (z -35.8, 48/48 lines; cell-cycle shift (explains ~15% here)), [[ZNF827]] 0.200× (z -35.8, 44/44 lines; cell-cycle shift (explains ~6% here)), [[ARID1B]] 0.193× (z -35.5, 47/47 lines; cell-cycle shift (explains ~13% here)), [[STAG2]] 0.288× (z -34.4, 48/48 lines; cell-cycle shift (explains ~17% here)), [[ZNF33A]] ⚠ 0.310× (z -34.0, 47/48 lines; cell-cycle shift, explains ~25% of this change), [[SPATS2L]] 0.317× (z -34.0, 47/47 lines; cell-cycle shift (explains ~7% here)), [[KMT5B]] 0.344× (z -33.3, 48/48 lines; cell-cycle shift (explains ~24% here))

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | [[Module 168]] (+2.3) | [[Module 137]] (-2.9), [[Module 095]] (-2.8), [[Module 051]] (-2.8) |
| 0.5 µM | [[Module 077]] (+9.2), [[Module 184]] (+7.7), [[Module 168]] (+7.0) | [[Module 095]] (-12.7), [[Module 137]] (-10.7), [[Module 088]] (-9.9) |
| 5 µM | [[Module 184]] (+17.4), [[Module 085]] (+17.2), [[Module 002]] (+16.7) | [[Module 095]] (-27.7), [[Module 088]] (-20.0), [[Module 137]] (-19.5) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | [[J82 (line)]] (1.38), [[SNU-423 (line)]] (1.32), [[A549 (line)]] (1.25), [[HOP62 (line)]] (1.24) · weakest: [[SK-MEL-2 (line)]] (0.728), [[AN3 CA (line)]] (0.734), [[NCI-H661 (line)]] (0.782) |
| 0.5 µM | — | [[H4 (line)]] (1.20), [[SNU-423 (line)]] (1.20), [[HOP62 (line)]] (1.19), [[A549 (line)]] (1.14) · weakest: [[AN3 CA (line)]] (0.680), [[SNU-1 (line)]] (0.710), [[SHP-77 (line)]] (0.764) |
| 5 µM | [[H4 (line)]] (-6.8), [[A-172 (line)]] (-6.7), [[NCI-H1792 (line)]] (-5.0), [[LOX-IMVI (line)]] (-3.7), [[NCI-H23 (line)]] (-3.5) | [[A549 (line)]] (1.23), [[H4 (line)]] (1.18), [[SW480 (line)]] (1.17), [[HOP62 (line)]] (1.16) · weakest: [[NCI-H661 (line)]] (0.709), [[AN3 CA (line)]] (0.768), [[SW 1088 (line)]] (0.772) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

⚠ This drug's own vector: vector dose flagged: cell-cycle shift. Read its neighbours with that in mind.

*378 other drugs have a vector, 121 with an alert ⚠; shown: the 8 most similar and the 1 next most similar without an alert.*

- [[Panobinostat (drug)]] (+0.94, HDAC inhibitor, ⚠ vector dose flagged: cell-cycle shift); [[Brivudine (drug)]] (+0.74, unclear); [[Fumaric acid (drug)]] (+0.58, unclear); [[L-Thyroxine (sodium salt pentahydrate) (drug)]] (+0.56, unclear); [[HI-TOPK-032 (drug)]] (+0.51, unclear); [[Quinidine (15% dihydroquinidine) (drug)]] (+0.51, unclear); [[Aprepitant (drug)]] (+0.51, unclear); [[Dimethyl fumarate (drug)]] (+0.49, unclear); [[Pimitespib (drug)]] (+0.48, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 8 arrows, 8 of them with an alert ⚠; grade A 0, B 1, C 7.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[ENSG00000229618]] | 5 µM | B | ENSG00000229618 activity lowers the cells' numbers under Belinostat 5 µM (makes them more sensitive) | lines that do not express ENSG00000229618 (32) vs lines expressing it (16) | the lines without ENSG00000229618: 1.20× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; also absent: ANKRD20A21P, LINC01205, ENSG00000249776 |
| [[TACC2]] | 5 µM | C | TACC2 activity raises the cells' numbers under Belinostat 5 µM (protects the cells) | lines that do not express TACC2 (3) vs lines expressing it (45) | the lines without TACC2: 0.59× the cells of the other lines | 0.008 | ⚠ few lines (3 vs 47); across organs; also absent: NME3, OSR2, H1-0; maybe low, not absent |
| [[OSR2]] | 5 µM | C | OSR2 activity raises the cells' numbers under Belinostat 5 µM (protects the cells) | lines that do not express OSR2 (5) vs lines expressing it (43) | the lines without OSR2: 0.69× the cells of the other lines | 0.022 | ⚠ tissue-confounded; across organs; also absent: ZC3HAV1L, TACC2, VRK2; maybe low, not absent |
| [[ZC3HAV1L]] | 5 µM | C | ZC3HAV1L activity raises the cells' numbers under Belinostat 5 µM (protects the cells) | lines that do not express ZC3HAV1L (5) vs lines expressing it (43) | the lines without ZC3HAV1L: 0.70× the cells of the other lines | 0.032 | ⚠ tissue-confounded; across organs; also absent: OSR2, PTER, VRK2 |
| [[TMEM216]] | 5 µM | C | TMEM216 activity raises the cells' numbers under Belinostat 5 µM (protects the cells) | lines that do not express TMEM216 (6) vs lines expressing it (42) | the lines without TMEM216: 0.74× the cells of the other lines | 0.036 | ⚠ tissue-confounded; across organs; also absent: H1-0, LPIN3, TACC2 |
| [[ENSG00000291055]], [[PDCD6P1]] | 5 µM | C | ENSG00000291055, PDCD6P1 activity raises the cells' numbers under Belinostat 5 µM (protects the cells) | lines that do not express ENSG00000291055, PDCD6P1 (4) vs lines expressing them (44) | the lines without ENSG00000291055, PDCD6P1: 0.69× the cells of the other lines | 0.058 | ⚠ few lines (4 vs 46); across organs; also absent: NSUN5, KIAA1671, ENSG00000291079; maybe low, not absent; co-absent genes |
| [[SCAMP5]] | 5 µM | C | SCAMP5 activity raises the cells' numbers under Belinostat 5 µM (protects the cells) | lines that do not express SCAMP5 (3) vs lines expressing it (45) | the lines without SCAMP5: 0.70× the cells of the other lines | 0.080 | ⚠ few lines (3 vs 47); across organs; also absent: ENSG00000262160, SLC4A11, CORO2A; maybe low, not absent |
| [[DHCR7]], [[ENSG00000254682]] | 5 µM | C | DHCR7, ENSG00000254682 activity raises the cells' numbers under Belinostat 5 µM (protects the cells) | lines that do not express DHCR7, ENSG00000254682 (3) vs lines expressing them (45) | the lines without DHCR7, ENSG00000254682: 0.65× the cells of the other lines | 0.097 | ⚠ few lines (3 vs 47); across organs; also absent: LPIN3, TACC2, INSR; co-absent genes |

### Its targets: what acting on them probably does

*Drug-target arrows of the compound classes it belongs to (compounds sharing a listed target and mechanism; one molecule counts once, under all its names): the target → a gene whose level those compounds move. A row that names several targets is one test: the compounds share them all, and any of them could be the cause. 1,739 arrows, 1,739 of them with an alert ⚠; grade A 0, B 1,739, C 0. Shown: the 15 strongest; 1,724 more arrows (1,724 of them with an alert ⚠) not shown.*

| Its target | Gene it moves | This drug | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|---|
| [[HDAC6]] | [[ABRACL]] | moves it that way too | B | HDAC6 activity raises ABRACL's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[HDAC6]] | [[ACTR5]] | moves it that way too | B | HDAC6 activity lowers ACTR5's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[HDAC6]] | [[ANKRD10]] | moves it that way too | B | HDAC6 activity raises ANKRD10's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[HDAC6]] | [[ANKS3]] | moves it that way too | B | HDAC6 activity lowers ANKS3's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[HDAC6]] | [[ARAP2]] | moves it that way too | B | HDAC6 activity raises ARAP2's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[HDAC6]] | [[ARF1]] | moves it that way too | B | HDAC6 activity raises ARF1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[HDAC6]] | [[ARPP19]] | moves it that way too | B | HDAC6 activity raises ARPP19's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[HDAC6]] | [[BAIAP2L2]] | moves it that way too | B | HDAC6 activity raises BAIAP2L2's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[HDAC6]] | [[BTG3]] | moves it that way too | B | HDAC6 activity raises BTG3's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[HDAC6]] | [[CABIN1]] | moves it that way too | B | HDAC6 activity lowers CABIN1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[HDAC6]] | [[CARD19]] | moves it that way too | B | HDAC6 activity lowers CARD19's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[HDAC6]] | [[CD63]] | moves it that way too | B | HDAC6 activity raises CD63's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[HDAC6]] | [[CLDN18]] | moves it that way too | B | HDAC6 activity raises CLDN18's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[HDAC6]] | [[COA6]] | moves it that way too | B | HDAC6 activity raises COA6's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[HDAC6]] | [[COCH]] | moves it that way too | B | HDAC6 activity raises COCH's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |

## Data

- `tables/drugs.parquet` — drug == "Belinostat"
- `tables/drugdoses.parquet` — dd in 144, 145, 146
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
