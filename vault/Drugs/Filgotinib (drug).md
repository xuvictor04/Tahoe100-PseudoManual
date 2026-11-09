---
drug: "Filgotinib"
type: "drug"
salt_base: "Filgotinib"
targets: "JAK1, JAK2, TYK2, JAK3"
moa_fine: "JAK/STAT inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 1393
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Filgotinib

*JAK/STAT inhibitor (inhibitor/antagonist) · targets: JAK1, JAK2, TYK2, JAK3 · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 101 / 36 / 1393; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.05 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.44 / 0.40.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 10]]:A5 | 29 / 72 | — | +0.07 | +0.6/+0.8/-0.6 | — |
| 0.5 µM | [[Plate 11]]:A5 | 31 / 5 | — | -0.27 | +0.7/+0.6/+1.3 | — |
| 5 µM | [[Plate 12]]:A5 | 1,112 / 281 | — | +0.85 | +1.4/+1.4/-1.3 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (29 genes, none with an alert; 12 shown): [[TSPAN31]] 1.27× (z +3.9, 6/46 lines), [[TXNIP]] 1.33× (z +3.8, 21/37 lines), [[TUBA1A]] 1.43× (z +3.8, 13/38 lines), [[THUMPD3-AS1]] 1.25× (z +3.5, 28/48 lines), [[MX1]] 1.39× (z +3.5, 14/29 lines), [[SLC25A45]] 1.43× (z +3.4, 5/44 lines), [[MIR4435-2HG]] 1.22× (z +3.4, 20/45 lines), [[C19orf38]] 1.52× (z +3.4, 6/45 lines), [[DMBX1]] 1.39× (z +3.4, 0/35 lines), [[TMEM45A]] 1.31× (z +3.4, 11/35 lines), [[C9]] 1.59× (z +3.3, 3/24 lines), [[NT5E]] 1.30× (z +3.3, 18/34 lines)

**0.5 µM** (31 genes, none with an alert; 12 shown): [[LINC02580]] 1.36× (z +4.0, 5/43 lines), [[ETV4]] 1.27× (z +3.7, 9/45 lines), [[TMEM14C]] 1.40× (z +3.6, 25/48 lines), [[TMEM187]] 1.38× (z +3.4, 1/40 lines), [[KCNN3]] 1.38× (z +3.4, 2/31 lines), [[NEK5]] 1.32× (z +3.4, 2/41 lines), [[ITPRIPL2]] 1.32× (z +3.4, 16/46 lines), [[B4GAT1]] 1.45× (z +3.3, 7/45 lines), [[PSMD14-DT]] 1.35× (z +3.3, 9/42 lines), [[MIR1915HG]] 1.46× (z +3.3, 2/29 lines), [[SMNDC1]] 1.25× (z +3.2, 22/48 lines), [[LINC02882]] 1.26× (z +3.2, 2/20 lines)

**5 µM** (1112 genes, none with an alert; 12 shown): [[MSH4]] 2.71× (z +9.8, 31/46 lines), [[STPG4]] 2.29× (z +8.9, 41/46 lines), [[ENSG00000260392]] 3.22× (z +8.9, 40/48 lines), [[ENSG00000285190]] 3.61× (z +8.8, 37/45 lines), [[LINC01191]] 2.30× (z +8.8, 38/46 lines), [[C21orf91-OT1]] 2.87× (z +8.7, 38/43 lines), [[LINC01030]] 2.61× (z +8.7, 27/45 lines), [[ENSG00000278819]] 2.36× (z +8.7, 27/47 lines), [[SLC22A14]] 2.61× (z +8.6, 38/47 lines), [[HCLS1]] 2.69× (z +8.5, 35/46 lines), [[ENSG00000282440]] 3.00× (z +8.4, 23/30 lines), [[PLAC8L1]] 2.57× (z +8.0, 36/47 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (72 genes, none with an alert; 12 shown): [[HBS1L]] 0.786× (z -4.6, 27/48 lines), [[LRRFIP2]] 0.800× (z -4.3, 28/48 lines), [[PPTC7]] 0.751× (z -4.3, 29/48 lines), [[HSF2]] 0.728× (z -4.3, 16/47 lines), [[PHAF1]] 0.786× (z -4.2, 19/48 lines), [[SPATA5L1]] 0.763× (z -4.1, 17/48 lines), [[NAA16]] 0.769× (z -4.1, 24/48 lines), [[SNRNP40]] 0.757× (z -4.0, 23/48 lines), [[RPS10-NUDT3]] 0.618× (z -4.0, 8/46 lines), [[SMPD4BP]] 0.785× (z -4.0, 18/48 lines), [[OTUD6B]] 0.772× (z -3.9, 15/48 lines), [[KPNA1]] 0.808× (z -3.8, 22/48 lines)

**0.5 µM** (5 genes, none with an alert): [[TRIM25]] 0.826× (z -3.7, 20/48 lines), [[HECA]] 0.813× (z -3.1, 18/48 lines), [[PARP12]] 0.804× (z -3.1, 18/46 lines), [[RBM44]] 0.767× (z -2.9, 8/42 lines), [[SH3D21]] 0.799× (z -2.9, 12/44 lines)

**5 µM** (281 genes, none with an alert; 12 shown): [[ENSG00000253100]] 0.456× (z -7.4, 22/37 lines), [[TAP1]] 0.616× (z -7.1, 32/48 lines), [[TBK1]] 0.763× (z -6.7, 36/48 lines), [[TRIM22]] 0.527× (z -6.5, 25/30 lines), [[PRKRA]] 0.742× (z -6.4, 38/48 lines), [[RNF149]] 0.749× (z -6.2, 38/47 lines), [[GBP4]] 0.527× (z -6.0, 21/28 lines), [[GK]] 0.670× (z -5.5, 23/44 lines), [[TUBE1]] 0.573× (z -5.5, 36/48 lines), [[MPZL1]] 0.824× (z -5.4, 23/48 lines), [[CFB]] 0.553× (z -5.3, 19/28 lines), [[PARP12]] 0.688× (z -5.2, 26/46 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | [[Module 184]] (+2.2) | [[Module 168]] (-2.3), [[Module 182]] (-2.3), [[Module 171]] (-2.3) |
| 0.5 µM | — | — |
| 5 µM | [[Module 039]] (+4.5), [[Module 010]] (+3.8), [[Module 223]] (+3.3) | [[Module 030]] (-3.0), [[Module 048]] (-2.5), [[Module 168]] (-2.4) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | [[HEC-1-A (line)]] (-4.4) | [[AsPC-1 (line)]] (1.53), [[NCI-H1792 (line)]] (1.37), [[SW 900 (line)]] (1.31), [[CHP-212 (line)]] (1.30) · weakest: [[AN3 CA (line)]] (0.175), [[BT-474 (line)]] (0.192), [[SNU-1 (line)]] (0.499) |
| 0.5 µM | — | [[SW 1088 (line)]] (1.61), [[BT-474 (line)]] (1.35), [[NCI-H661 (line)]] (1.33), [[AsPC-1 (line)]] (1.20) · weakest: [[SNU-1 (line)]] (0.324), [[AN3 CA (line)]] (0.439), [[LS 180 (line)]] (0.442) |
| 5 µM | — | [[A498 (line)]] (1.32), [[LoVo (line)]] (1.29), [[SW48 (line)]] (1.27), [[A549 (line)]] (1.26) · weakest: [[SW 1088 (line)]] (0.386), [[NCI-H661 (line)]] (0.401), [[AN3 CA (line)]] (0.510) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 2 next most similar without an alert.*

- [[Nafamostat (mesylate) (drug)]] (+0.70, unclear, ⚠ only 3 significant genes); [[Apalutamide (drug)]] (+0.70, Androgen receptor antagonist); [[Omeprazole (drug)]] (+0.69, unclear); [[Demeclocycline (drug)]] (+0.69, unclear); [[Esmolol (hydrochloride) (drug)]] (+0.68, unclear); [[Mifepristone (drug)]] (+0.62, unclear); [[Glasdegib (drug)]] (+0.62, Sonic inhibitor, ⚠ only 4 significant genes; no trustworthy dose (vector dose flagged: unreliable plate only)); [[Proglumide (drug)]] (+0.61, unclear); [[Tirabrutinib (drug)]] (+0.61, Other TK inhibitor); [[(R)-Verapamil (hydrochloride) (drug)]] (+0.60, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 39 arrows, 39 of them with an alert ⚠; grade A 0, B 31, C 8. Shown: the 15 strongest; 24 more arrows (24 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[COL17A1]] | 0.05 µM | B | COL17A1 activity lowers the cells' numbers under Filgotinib 0.05 µM (makes them more sensitive) | lines that do not express COL17A1 (34) vs lines expressing it (14) | the lines without COL17A1: 1.27× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: SERPINB5, GJB3, FGFBP1 |
| [[TMEM30B]] | 0.05 µM | B | TMEM30B activity lowers the cells' numbers under Filgotinib 0.05 µM (makes them more sensitive) | lines that do not express TMEM30B (35) vs lines expressing it (13) | the lines without TMEM30B: 1.24× the cells of the other lines | 0.033 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, ANKRD22, RAB25 |
| [[RASEF]] | 0.05 µM | B | RASEF activity lowers the cells' numbers under Filgotinib 0.05 µM (makes them more sensitive) | lines that do not express RASEF (20) vs lines expressing it (28) | the lines without RASEF: 1.23× the cells of the other lines | 0.037 | ⚠ within organs, on part of the lines; also absent: LIPH, ENSG00000263325, DENND2D |
| [[BARX2]] | 0.05 µM | B | BARX2 activity lowers the cells' numbers under Filgotinib 0.05 µM (makes them more sensitive) | lines that do not express BARX2 (29) vs lines expressing it (19) | the lines without BARX2: 1.21× the cells of the other lines | 0.043 | ⚠ within organs, on part of the lines; also absent: COL17A1, FXYD3, CEACAM6 |
| [[SERPINB5]] | 0.05 µM | B | SERPINB5 activity lowers the cells' numbers under Filgotinib 0.05 µM (makes them more sensitive) | lines that do not express SERPINB5 (34) vs lines expressing it (14) | the lines without SERPINB5: 1.26× the cells of the other lines | 0.047 | ⚠ within organs, on part of the lines; also absent: COL17A1, FGFBP1, TSPAN8 |
| [[OVOL1]], [[TMPRSS4]] | 0.05 µM | B | OVOL1, TMPRSS4 activity lowers the cells' numbers under Filgotinib 0.05 µM (makes them more sensitive) | lines that do not express OVOL1, TMPRSS4 (33) vs lines expressing them (15) | the lines without OVOL1, TMPRSS4: 1.29× the cells of the other lines | 0.068 | ⚠ within organs, on part of the lines; also absent: GRHL2, ST14, TMEM30B; co-absent genes |
| [[ANKRD22]] | 0.05 µM | B | ANKRD22 activity lowers the cells' numbers under Filgotinib 0.05 µM (makes them more sensitive) | lines that do not express ANKRD22 (34) vs lines expressing it (14) | the lines without ANKRD22: 1.24× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: TMEM30B, GRHL2, RAB25 |
| [[SEPTIN9-DT]] | 0.05 µM | B | SEPTIN9-DT activity lowers the cells' numbers under Filgotinib 0.05 µM (makes them more sensitive) | lines that do not express SEPTIN9-DT (13) vs lines expressing it (35) | the lines without SEPTIN9-DT: 1.16× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: MALL, CDCP1, EPHA2; maybe low, not absent |
| [[C19orf33]] | 0.05 µM | B | C19orf33 activity lowers the cells' numbers under Filgotinib 0.05 µM (makes them more sensitive) | lines that do not express C19orf33 (19) vs lines expressing it (29) | the lines without C19orf33: 1.27× the cells of the other lines | 0.075 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: KRT80, MISP, AREG |
| [[EHF]] | 0.05 µM | B | EHF activity lowers the cells' numbers under Filgotinib 0.05 µM (makes them more sensitive) | lines that do not express EHF (27) vs lines expressing it (21) | the lines without EHF: 1.24× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; also absent: TMPRSS4, IRF6, GJB3 |
| [[C1orf116]], [[IRF6]] | 0.05 µM | B | C1orf116, IRF6 activity lowers the cells' numbers under Filgotinib 0.05 µM (makes them more sensitive) | lines that do not express C1orf116, IRF6 (31) vs lines expressing them (17) | the lines without C1orf116, IRF6: 1.28× the cells of the other lines | 0.077 | ⚠ within organs, on part of the lines; also absent: ST14, TMPRSS4, TMEM125; co-absent genes |
| [[GRHL2]], [[LINC02967]] | 0.05 µM | B | GRHL2, LINC02967 activity lowers the cells' numbers under Filgotinib 0.05 µM (makes them more sensitive) | lines that do not express GRHL2, LINC02967 (34) vs lines expressing them (14) | the lines without GRHL2, LINC02967: 1.28× the cells of the other lines | 0.078 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM30B, RAB25, TMPRSS4; co-absent genes |
| [[TMPRSS2]] | 0.05 µM | B | TMPRSS2 activity lowers the cells' numbers under Filgotinib 0.05 µM (makes them more sensitive) | lines that do not express TMPRSS2 (35) vs lines expressing it (13) | the lines without TMPRSS2: 1.24× the cells of the other lines | 0.078 | ⚠ within organs, on part of the lines; also absent: SLC5A1, ARHGEF38, ITGB6 |
| [[GJB3]] | 0.05 µM | B | GJB3 activity lowers the cells' numbers under Filgotinib 0.05 µM (makes them more sensitive) | lines that do not express GJB3 (31) vs lines expressing it (17) | the lines without GJB3: 1.30× the cells of the other lines | 0.079 | ⚠ within organs, on part of the lines; also absent: IRF6, COL17A1, KLK10 |
| [[GXYLT2]] | 0.05 µM | B | GXYLT2 activity raises the cells' numbers under Filgotinib 0.05 µM (protects the cells) | lines that do not express GXYLT2 (11) vs lines expressing it (37) | the lines without GXYLT2: 0.83× the cells of the other lines | 0.079 | ⚠ within organs, on part of the lines; also absent: TMEM145, SLC17A7, FAM171B |

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
| [[JAK2]] | [[ZSCAN5A]] | moves it that way too | B | JAK2 activity lowers ZSCAN5A's level | compounds that target JAK2: 2 of 3 raise it (Fedratinib, Filgotinib) | 67% of the class's compounds vs 0.6% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds |
| [[JAK2]] | [[IL15]] | moves it that way too | B | JAK2 activity raises IL15's level | compounds that target JAK2: 3 of 3 lower it (Fedratinib, Filgotinib, Tofacitinib) | 100% of the class's compounds vs 3.9% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds |
| [[JAK2]] | [[PATL1]] | moves it that way too | B | JAK2 activity raises PATL1's level | compounds that target JAK2: 3 of 3 lower it (Fedratinib, Filgotinib, Tofacitinib) | 100% of the class's compounds vs 3.9% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds |
| [[JAK2]] | [[TRAF3IP2]] | moves it that way too | B | JAK2 activity raises TRAF3IP2's level | compounds that target JAK2: 3 of 3 lower it (Fedratinib, Filgotinib, Tofacitinib) | 100% of the class's compounds vs 3.9% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds |
| [[JAK2]] | [[IL15RA]] | moves it that way too | B | JAK2 activity raises IL15RA's level | compounds that target JAK2: 3 of 3 lower it (Fedratinib, Filgotinib, Tofacitinib) | 100% of the class's compounds vs 4.2% of all compounds | 0.053 | ⚠ off-target possible; 3 compounds |
| [[JAK2]] | [[PLEKHA4]] | moves it that way too | B | JAK2 activity raises PLEKHA4's level | compounds that target JAK2: 3 of 3 lower it (Fedratinib, Filgotinib, Tofacitinib) | 100% of the class's compounds vs 4.8% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds |
| [[JAK1]], [[JAK3]] | [[CTDSPL]] | moves it that way too | B | JAK1, JAK3 activity lowers CTDSPL's level | compounds that target JAK1, JAK3: 2 of 2 raise it (Filgotinib, Tofacitinib) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; shared targets |
| [[JAK2]] | [[ENSG00000291144]] | moves it that way too | B | JAK2 activity raises ENSG00000291144's level | compounds that target JAK2: 3 of 3 lower it (Fedratinib, Filgotinib, Tofacitinib) | 100% of the class's compounds vs 5.3% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds |
| [[JAK2]] | [[BIRC3]] | moves it that way too | B | JAK2 activity raises BIRC3's level | compounds that target JAK2: 3 of 3 lower it (Fedratinib, Filgotinib, Tofacitinib) | 100% of the class's compounds vs 5.6% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds |

## Data

- `tables/drugs.parquet` — drug == "Filgotinib"
- `tables/drugdoses.parquet` — dd in 447, 448, 449
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
