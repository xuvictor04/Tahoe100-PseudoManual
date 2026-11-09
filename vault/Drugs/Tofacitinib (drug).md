---
drug: "Tofacitinib"
type: "drug"
salt_base: "Tofacitinib"
targets: "JAK1, JAK2, JAK3"
moa_fine: "JAK/STAT inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 291
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Tofacitinib

*JAK/STAT inhibitor (inhibitor/antagonist) · targets: JAK1, JAK2, JAK3 · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 24 / 253 / 291; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.05 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.35 / 0.63.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 04]]:C3 | 8 / 16 | — | -0.28 | +0.6/+1.5/-0.6 | — |
| 0.5 µM | [[Plate 05]]:C3 | 19 / 234 | — | +0.05 | +1.5/+1.5/+0.1 | — |
| 5 µM | [[Plate 14]]:C3 | 34 / 257 | 0.928 | -0.07 | +0.2/+1.2/-1.5 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (8 genes, none with an alert): [[CFAP210]] 1.92× (z +3.6, 17/42 lines), [[CDHR2]] 1.38× (z +3.3, 3/15 lines), [[MOK]] 1.25× (z +3.3, 12/48 lines), [[HNF1B]] 1.29× (z +3.3, 2/17 lines), [[ARHGEF6]] 1.28× (z +3.3, 0/25 lines), [[NUP62CL]] 1.38× (z +3.1, 5/28 lines), [[PER2]] 1.25× (z +3.0, 17/48 lines), [[CFAP69]] 1.25× (z +3.0, 13/47 lines)

**0.5 µM** (19 genes, none with an alert; 12 shown): [[ABHD2]] 1.23× (z +4.2, 24/48 lines), [[SEC24D]] 1.34× (z +3.9, 34/49 lines), [[GFPT1]] 1.22× (z +3.8, 23/49 lines), [[PTGER4]] 1.35× (z +3.7, 10/35 lines), [[SDC1]] 1.35× (z +3.7, 12/38 lines), [[GSN]] 1.22× (z +3.6, 13/46 lines), [[PLCD3]] 1.22× (z +3.6, 6/47 lines), [[SORL1]] 1.26× (z +3.6, 7/28 lines), [[EIF2AK3]] 1.30× (z +3.5, 23/49 lines), [[REEP4]] 1.37× (z +3.5, 9/44 lines), [[WFS1]] 1.26× (z +3.4, 6/43 lines), [[ALDH6A1]] 1.23× (z +3.2, 8/48 lines)

**5 µM** (34 genes, none with an alert; 12 shown): [[SORL1]] 1.36× (z +6.8, 12/27 lines), [[ABHD2]] 1.22× (z +5.6, 22/48 lines), [[ZNF704]] 1.24× (z +5.2, 12/32 lines), [[SORBS2]] 1.28× (z +5.2, 12/32 lines), [[OLFML2A]] 1.37× (z +4.8, 12/28 lines), [[SLIT3]] 1.27× (z +4.8, 8/17 lines), [[BMP7]] 1.27× (z +4.7, 6/25 lines), [[CACNG4]] 1.32× (z +4.3, 7/25 lines), [[CABLES1]] 1.23× (z +4.3, 19/41 lines), [[ROR1]] 1.23× (z +4.2, 18/34 lines), [[GNG2]] 1.21× (z +3.9, 7/26 lines), [[SFXN2]] 1.23× (z +3.9, 9/47 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (16 genes, none with an alert; 12 shown): [[TMEM201]] 0.737× (z -4.1, 8/44 lines), [[TRIM22]] 0.688× (z -3.8, 17/30 lines), [[CMTR1]] 0.833× (z -3.7, 18/48 lines), [[CFB]] 0.684× (z -3.4, 15/28 lines), [[PML]] 0.828× (z -3.4, 16/46 lines), [[NRIR]] 0.636× (z -3.3, 5/27 lines), [[PNPT1]] 0.815× (z -3.2, 21/47 lines), [[GBP4]] 0.716× (z -3.1, 10/28 lines), [[TREX2]] 0.812× (z -3.1, 6/45 lines), [[TMEM104]] 0.811× (z -3.0, 6/47 lines), [[ENSG00000271204]] 0.830× (z -3.0, 8/43 lines), [[OAS3]] 0.754× (z -3.0, 21/43 lines)

**0.5 µM** (234 genes, none with an alert; 12 shown): [[EIF2AK2]] 0.455× (z -14.1, 35/48 lines), [[IFI44L]] 0.217× (z -13.5, 24/26 lines), [[MX1]] 0.282× (z -13.3, 27/30 lines), [[PARP9]] 0.344× (z -12.9, 38/42 lines), [[STAT1]] 0.420× (z -12.7, 37/49 lines), [[TRIM22]] 0.296× (z -12.4, 26/30 lines), [[SP100]] 0.556× (z -12.3, 32/46 lines), [[OAS3]] 0.317× (z -12.2, 35/44 lines), [[OAS2]] 0.198× (z -12.1, 29/34 lines), [[HERC5]] 0.396× (z -11.6, 20/33 lines), [[IFI44]] 0.392× (z -11.5, 27/37 lines), [[PNPT1]] 0.476× (z -11.5, 36/48 lines)

**5 µM** (257 genes, none with an alert; 12 shown): [[PARP9]] 0.247× (z -24.0, 37/42 lines), [[MX1]] 0.222× (z -22.4, 29/30 lines), [[EIF2AK2]] 0.418× (z -22.2, 33/48 lines), [[OAS3]] 0.241× (z -21.5, 34/44 lines), [[STAT1]] 0.361× (z -21.2, 38/49 lines), [[IFI44]] 0.317× (z -20.0, 28/37 lines), [[SP100]] 0.512× (z -19.9, 32/46 lines), [[IRF9]] 0.465× (z -19.5, 39/48 lines), [[PLSCR1]] 0.356× (z -19.1, 37/41 lines), [[OAS2]] 0.179× (z -18.1, 30/34 lines), [[IFI44L]] 0.242× (z -17.7, 24/26 lines), [[ADAR]] 0.612× (z -16.4, 34/49 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | [[Module 205]] (+2.3) | — |
| 0.5 µM | — | [[Module 032]] (-5.8), [[Module 070]] (-3.1), [[Module 139]] (-2.8) |
| 5 µM | — | [[Module 032]] (-8.8), [[Module 070]] (-4.3), [[Module 139]] (-3.8) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | [[A-427 (line)]] (-3.5), [[NCI-H661 (line)]] (-3.5) | [[BT-474 (line)]] (1.78), [[SNU-1 (line)]] (1.74), [[NCI-H1573 (line)]] (1.42), [[COLO 205 (line)]] (1.42) · weakest: [[SW 1088 (line)]] (-0.300), [[NCI-H460 (line)]] (0.286), [[HEC-1-A (line)]] (0.384) |
| 0.5 µM | — | [[BT-474 (line)]] (2.02), [[MIA PaCa-2 (line)]] (1.65), [[NCI-H1792 (line)]] (1.54), [[A549 (line)]] (1.53) · weakest: [[NCI-H661 (line)]] (0.125), [[NCI-H460 (line)]] (0.131), [[HEC-1-A (line)]] (0.142) |
| 5 µM | — | [[MIA PaCa-2 (line)]] (1.79), [[COLO 205 (line)]] (1.75), [[BT-474 (line)]] (1.74), [[CFPAC-1 (line)]] (1.66) · weakest: [[HEC-1-A (line)]] (0.0819), [[SW 1271 (line)]] (0.125), [[NCI-H460 (line)]] (0.143) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar.*

- [[Tofacitinib (citrate) (drug)]] (+0.82, JAK/STAT inhibitor); [[Ixazomib (drug)]] (+0.57, Proteasome inhibitor); [[Fedratinib (hydrochloride hydrate) (drug)]] (+0.47, JAK/STAT inhibitor); [[Filgotinib (drug)]] (+0.36, JAK/STAT inhibitor); [[Crizotinib (hydrochloride) (drug)]] (+0.34, Multi-TK inhibitor); [[Ralimetinib dimesylate (drug)]] (+0.34, Other MAPK inhibitor); [[Ciclopirox (drug)]] (+0.30, unclear); [[Trimetrexate (drug)]] (+0.30, DNA synthesis/repair inhibitor)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 16 arrows, 16 of them with an alert ⚠; grade A 0, B 15, C 1. Shown: the 15 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[SLC2A9]] | 0.05 µM | B | SLC2A9 activity raises the cells' numbers under Tofacitinib 0.05 µM (protects the cells) | lines that do not express SLC2A9 (6) vs lines expressing it (42) | the lines without SLC2A9: 0.70× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: VDR, SEMA4G, TBC1D8B; maybe low, not absent |
| [[AHR]] | 0.05 µM | B | AHR activity raises the cells' numbers under Tofacitinib 0.05 µM (protects the cells) | lines that do not express AHR (7) vs lines expressing it (41) | the lines without AHR: 0.77× the cells of the other lines | 0.037 | ⚠ within organs, on part of the lines; also absent: ENSG00000283321, VDR, GPR39 |
| [[ATP1B1]] | 0.05 µM | B | ATP1B1 activity raises the cells' numbers under Tofacitinib 0.05 µM (protects the cells) | lines that do not express ATP1B1 (8) vs lines expressing it (40) | the lines without ATP1B1: 0.75× the cells of the other lines | 0.047 | ⚠ within organs, on part of the lines; also absent: PYROXD2, IL15, IER3; maybe low, not absent |
| [[PLSCR2]] | 0.05 µM | B | PLSCR2 activity raises the cells' numbers under Tofacitinib 0.05 µM (protects the cells) | lines that do not express PLSCR2 (6) vs lines expressing it (42) | the lines without PLSCR2: 0.75× the cells of the other lines | 0.052 | ⚠ within organs, on part of the lines; also absent: TRIB1, SLC2A1, CEMIP2; maybe low, not absent |
| [[TRIB1]] | 0.05 µM | B | TRIB1 activity raises the cells' numbers under Tofacitinib 0.05 µM (protects the cells) | lines that do not express TRIB1 (6) vs lines expressing it (42) | the lines without TRIB1: 0.70× the cells of the other lines | 0.071 | ⚠ within organs, on part of the lines; also absent: TGFBR2, VDR, PLSCR2; maybe low, not absent |
| [[HPCAL1]] | 0.05 µM | B | HPCAL1 activity raises the cells' numbers under Tofacitinib 0.05 µM (protects the cells) | lines that do not express HPCAL1 (6) vs lines expressing it (42) | the lines without HPCAL1: 0.86× the cells of the other lines | 0.073 | ⚠ within organs, on part of the lines; also absent: SHB, ARMCX3, ECE1; maybe low, not absent |
| [[DNAJC12]] | 0.05 µM | B | DNAJC12 activity raises the cells' numbers under Tofacitinib 0.05 µM (protects the cells) | lines that do not express DNAJC12 (25) vs lines expressing it (23) | the lines without DNAJC12: 0.79× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; also absent: TSHZ2, ENSG00000232053, PROX1 |
| [[HIPK2]] | 0.05 µM | B | HIPK2 activity raises the cells' numbers under Tofacitinib 0.05 µM (protects the cells) | lines that do not express HIPK2 (5) vs lines expressing it (43) | the lines without HIPK2: 0.68× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: MARCHF3, ASPH, ENSG00000286533; maybe low, not absent |
| [[ENSG00000283321]] | 0.05 µM | B | ENSG00000283321 activity raises the cells' numbers under Tofacitinib 0.05 µM (protects the cells) | lines that do not express ENSG00000283321 (7) vs lines expressing it (41) | the lines without ENSG00000283321: 0.82× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; co-occurs with WNK2; also absent: AHR, PSMB8, CXCL2 |
| [[MSRB3-AS1]] | 0.05 µM | B | MSRB3-AS1 activity lowers the cells' numbers under Tofacitinib 0.05 µM (makes them more sensitive) | lines that do not express MSRB3-AS1 (42) vs lines expressing it (6) | the lines without MSRB3-AS1: 1.39× the cells of the other lines | 0.084 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: GCG, LINC01205, COX7B2 |
| [[MET]] | 0.05 µM | B | MET activity raises the cells' numbers under Tofacitinib 0.05 µM (protects the cells) | lines that do not express MET (9) vs lines expressing it (39) | the lines without MET: 0.81× the cells of the other lines | 0.089 | ⚠ within organs, on part of the lines; also absent: TGFBR2, PHLDA2, VDR |
| [[VDR]] | 0.05 µM | B | VDR activity raises the cells' numbers under Tofacitinib 0.05 µM (protects the cells) | lines that do not express VDR (8) vs lines expressing it (40) | the lines without VDR: 0.74× the cells of the other lines | 0.091 | ⚠ within organs, on part of the lines; also absent: TGFBR2, TRIB1, MET |
| [[LGALS3BP]] | 0.05 µM | B | LGALS3BP activity raises the cells' numbers under Tofacitinib 0.05 µM (protects the cells) | lines that do not express LGALS3BP (7) vs lines expressing it (41) | the lines without LGALS3BP: 0.74× the cells of the other lines | 0.095 | ⚠ within organs, on part of the lines; also absent: LGALS3, KLF4, APOL6 |
| [[ZFPM2-AS1]] | 0.05 µM | B | ZFPM2-AS1 activity raises the cells' numbers under Tofacitinib 0.05 µM (protects the cells) | lines that do not express ZFPM2-AS1 (16) vs lines expressing it (32) | the lines without ZFPM2-AS1: 0.83× the cells of the other lines | 0.099 | ⚠ within organs, on part of the lines; co-occurs with WNK2; also absent: MIR3142HG, FRMD4A, TLR6 |
| [[CCL20]] | 0.05 µM | B | CCL20 activity raises the cells' numbers under Tofacitinib 0.05 µM (protects the cells) | lines that do not express CCL20 (16) vs lines expressing it (32) | the lines without CCL20: 0.89× the cells of the other lines | 0.0995 | ⚠ within organs, on part of the lines; also absent: TGM2, CLDN16, GPR39 |

### Its targets: what acting on them probably does

*Drug-target arrows of the compound classes it belongs to (compounds sharing a listed target and mechanism; one molecule counts once, under all its names): the target → a gene whose level those compounds move. A row that names several targets is one test: the compounds share them all, and any of them could be the cause. 38 arrows, 38 of them with an alert ⚠; grade A 0, B 38, C 0. Shown: the 15 strongest; 23 more arrows (23 of them with an alert ⚠) not shown.*

| Its target | Gene it moves | This drug | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|---|
| [[JAK2]] | [[TAP2]] | moves it that way too | B | JAK2 activity raises TAP2's level | compounds that target JAK2: 3 of 3 lower it (Fedratinib, Filgotinib, Tofacitinib) | 100% of the class's compounds vs 2.5% of all compounds | 0.026 | ⚠ off-target possible; 3 compounds |
| [[JAK2]] | [[OGFR]] | moves it that way too | B | JAK2 activity raises OGFR's level | compounds that target JAK2: 3 of 3 lower it (Fedratinib, Filgotinib, Tofacitinib) | 100% of the class's compounds vs 3.1% of all compounds | 0.032 | ⚠ off-target possible; 3 compounds |
| [[JAK2]] | [[TRIM25]] | moves it that way too | B | JAK2 activity raises TRIM25's level | compounds that target JAK2: 3 of 3 lower it (Fedratinib, Filgotinib, Tofacitinib) | 100% of the class's compounds vs 3.1% of all compounds | 0.032 | ⚠ off-target possible; 3 compounds |
| [[JAK2]] | [[ADAR]] | moves it that way too | B | JAK2 activity raises ADAR's level | compounds that target JAK2: 3 of 3 lower it (Fedratinib, Filgotinib, Tofacitinib) | 100% of the class's compounds vs 3.4% of all compounds | 0.037 | ⚠ off-target possible; 3 compounds |
| [[JAK2]] | [[STRIP2]] | moves it that way too | B | JAK2 activity raises STRIP2's level | compounds that target JAK2: 3 of 3 lower it (Fedratinib, Filgotinib, Tofacitinib) | 100% of the class's compounds vs 3.4% of all compounds | 0.037 | ⚠ off-target possible; 3 compounds |
| [[JAK2]] | [[NAMPT]] | moves it that way too | B | JAK2 activity raises NAMPT's level | compounds that target JAK2: 3 of 3 lower it (Fedratinib, Filgotinib, Tofacitinib) | 100% of the class's compounds vs 3.6% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds |
| [[JAK2]] | [[ZSCAN5A]] | does not move it that way (the class's other compounds do) | B | JAK2 activity lowers ZSCAN5A's level | compounds that target JAK2: 2 of 3 raise it (Fedratinib, Filgotinib) | 67% of the class's compounds vs 0.6% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds |
| [[JAK2]] | [[IL15]] | moves it that way too | B | JAK2 activity raises IL15's level | compounds that target JAK2: 3 of 3 lower it (Fedratinib, Filgotinib, Tofacitinib) | 100% of the class's compounds vs 3.9% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds |
| [[JAK2]] | [[PATL1]] | moves it that way too | B | JAK2 activity raises PATL1's level | compounds that target JAK2: 3 of 3 lower it (Fedratinib, Filgotinib, Tofacitinib) | 100% of the class's compounds vs 3.9% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds |
| [[JAK2]] | [[TRAF3IP2]] | moves it that way too | B | JAK2 activity raises TRAF3IP2's level | compounds that target JAK2: 3 of 3 lower it (Fedratinib, Filgotinib, Tofacitinib) | 100% of the class's compounds vs 3.9% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds |
| [[JAK2]] | [[IL15RA]] | moves it that way too | B | JAK2 activity raises IL15RA's level | compounds that target JAK2: 3 of 3 lower it (Fedratinib, Filgotinib, Tofacitinib) | 100% of the class's compounds vs 4.2% of all compounds | 0.053 | ⚠ off-target possible; 3 compounds |
| [[JAK2]] | [[PLEKHA4]] | moves it that way too | B | JAK2 activity raises PLEKHA4's level | compounds that target JAK2: 3 of 3 lower it (Fedratinib, Filgotinib, Tofacitinib) | 100% of the class's compounds vs 4.8% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds |
| [[JAK1]], [[JAK3]] | [[CTDSPL]] | moves it that way too | B | JAK1, JAK3 activity lowers CTDSPL's level | compounds that target JAK1, JAK3: 2 of 2 raise it (Filgotinib, Tofacitinib) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; shared targets |
| [[JAK2]] | [[ENSG00000291144]] | moves it that way too | B | JAK2 activity raises ENSG00000291144's level | compounds that target JAK2: 3 of 3 lower it (Fedratinib, Filgotinib, Tofacitinib) | 100% of the class's compounds vs 5.3% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds |
| [[JAK2]] | [[BIRC3]] | moves it that way too | B | JAK2 activity raises BIRC3's level | compounds that target JAK2: 3 of 3 lower it (Fedratinib, Filgotinib, Tofacitinib) | 100% of the class's compounds vs 5.6% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds |

## Data

- `tables/drugs.parquet` — drug == "Tofacitinib"
- `tables/drugdoses.parquet` — dd in 1012, 1013, 1014
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
