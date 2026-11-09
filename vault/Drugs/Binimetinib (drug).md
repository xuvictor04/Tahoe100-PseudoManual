---
drug: "Binimetinib"
type: "drug"
salt_base: "Binimetinib"
targets: "MAP2K1, MAP2K2"
moa_fine: "MEK inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "no"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 1486
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Binimetinib

*MEK inhibitor (inhibitor/antagonist) · targets: MAP2K1, MAP2K2 · approved: no*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 1014 / 1273 / 1486; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.05 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.85 / 0.91.
> Flags by dose: - / noisy plate (z scaled) / noisy plate (z scaled).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 01]]:B12, [[Plate 10]]:H5 | 724 / 290 | 0.936 | +0.34 | -1.8/-1.4/-1.7 | — |
| 0.5 µM | [[Plate 11]]:B12, [[Plate 02]]:H5 | 713 / 560 | 0.944 | +0.05 | -2.3/-0.7/-1.4 | noisy plate (z scaled) |
| 5 µM | [[Plate 12]]:B12, [[Plate 03]]:H5 | 930 / 556 | 0.946 | +0.14 | -2.8/-1.5/-1.1 | noisy plate (z scaled) |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (724 genes, none with an alert; 12 shown): [[GBP2]] 1.61× (z +8.8, 29/36 lines), [[CFB]] 1.84× (z +7.4, 24/28 lines), [[APOL6]] 1.33× (z +7.0, 31/42 lines), [[ARMH1]] 1.58× (z +6.5, 23/44 lines), [[JDP2]] 1.39× (z +6.5, 16/35 lines), [[GBP1]] 1.65× (z +6.3, 26/32 lines), [[MAP2]] 1.58× (z +6.2, 19/34 lines), [[ENSG00000234424]] 2.04× (z +6.2, 10/14 lines), [[PIR]] 1.33× (z +6.2, 16/38 lines), [[ZSCAN31]] 1.67× (z +6.2, 24/37 lines), [[MEF2C]] 1.31× (z +6.1, 17/34 lines), [[ANXA4]] 1.22× (z +6.1, 25/48 lines)

**0.5 µM** (713 genes, none with an alert; 12 shown): [[GBP2]] 2.02× (z +11.9, 31/35 lines), [[CFB]] 2.55× (z +10.2, 25/28 lines), [[GBP1]] 1.97× (z +7.7, 28/32 lines), [[APOL6]] 1.42× (z +7.4, 32/42 lines), [[PGM2L1]] 1.30× (z +7.1, 21/44 lines), [[PIR]] 1.45× (z +7.0, 22/38 lines), [[TRIM22]] 1.70× (z +6.8, 24/30 lines), [[TLR3]] 1.96× (z +6.7, 17/35 lines), [[ZNF608]] 1.49× (z +6.6, 22/36 lines), [[FRK]] 1.44× (z +6.5, 20/26 lines), [[ZSCAN31]] 1.79× (z +6.2, 22/36 lines), [[GXYLT2]] 1.42× (z +6.2, 18/37 lines)

**5 µM** (930 genes, 1 with an alert ⚠; 12 shown): [[GBP2]] 2.45× (z +12.9, 34/36 lines), [[CFB]] 3.28× (z +10.7, 26/28 lines), [[GBP1]] 2.68× (z +9.7, 30/32 lines), [[PGM2L1]] 1.43× (z +8.4, 25/45 lines), [[ARID5B]] 1.64× (z +8.0, 34/43 lines), [[PALLD]] 1.54× (z +7.9, 26/38 lines), [[ENSG00000234424]] 3.15× (z +7.7, 13/16 lines), [[APOL6]] 1.49× (z +7.2, 30/42 lines), [[GBP4]] 2.01× (z +7.0, 21/28 lines), [[APOL1]] 1.72× (z +7.0, 23/25 lines), [[DUSP16]] 1.35× (z +6.9, 35/47 lines), [[CLIP1]] 1.26× (z +6.9, 28/49 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (290 genes, 7 with an alert ⚠; 12 shown): [[SPRY4]] 0.485× (z -13.0, 44/48 lines), [[ETV4]] 0.570× (z -11.4, 38/46 lines), [[CDCP1]] 0.613× (z -11.3, 29/33 lines), [[ETV5]] 0.667× (z -11.2, 39/49 lines), [[ITGA2]] 0.567× (z -10.1, 34/38 lines), [[NT5E]] 0.549× (z -9.7, 25/35 lines), [[ELK3]] 0.660× (z -8.8, 35/45 lines), [[ITGB5]] 0.709× (z -8.3, 31/47 lines), [[DUSP6]] 0.509× (z -8.0, 42/45 lines), [[CORO2B]] 0.581× (z -7.8, 19/34 lines), [[BMP6]] 0.676× (z -7.7, 17/25 lines), [[PHLDA1]] 0.580× (z -7.6, 38/44 lines)

**0.5 µM** (560 genes, 9 with an alert ⚠; 14 shown): [[ETV5]] 0.399× (z -24.0, 45/48 lines), [[ETV4]] 0.383× (z -17.3, 43/46 lines), [[SPRY4]] 0.340× (z -17.0, 45/48 lines), [[ITGA2]] 0.406× (z -14.4, 34/37 lines), [[SPRY4-AS1]] ⚠ 0.317× (z -13.9, 41/45 lines; position correction uncertain), [[NT5E]] 0.384× (z -13.9, 31/34 lines), [[ITGB5]] 0.528× (z -13.4, 39/46 lines), [[ZFPM2-AS1]] 0.552× (z -13.4, 28/32 lines), [[ELK3]] 0.525× (z -13.1, 38/44 lines), [[DUSP6]] 0.286× (z -12.6, 44/44 lines), [[CDCP1]] 0.560× (z -12.0, 29/32 lines), [[ENSG00000285517]] ⚠ 0.379× (z -12.0, 30/33 lines; position correction uncertain), [[MCTP1]] 0.574× (z -11.0, 30/35 lines), [[ENSG00000260877]] 0.398× (z -11.0, 30/34 lines)

**5 µM** (556 genes, 10 with an alert ⚠; 13 shown): [[ETV5]] 0.226× (z -33.0, 47/49 lines), [[SPRY4]] 0.187× (z -20.8, 48/48 lines), [[ETV4]] 0.261× (z -19.1, 43/46 lines), [[SPRY4-AS1]] ⚠ 0.188× (z -18.3, 46/46 lines; position correction uncertain), [[ETV1]] 0.238× (z -17.6, 36/37 lines), [[ZFPM2-AS1]] 0.416× (z -16.5, 32/33 lines), [[DUSP6]] 0.161× (z -15.7, 44/45 lines), [[ITGA2]] 0.341× (z -14.4, 37/38 lines), [[ITGB5]] 0.454× (z -14.4, 42/47 lines), [[ENSG00000260877]] 0.274× (z -14.2, 32/34 lines), [[SPRED1]] 0.440× (z -14.0, 47/49 lines), [[MYEOV]] 0.334× (z -13.6, 29/29 lines), [[NT5E]] 0.334× (z -13.4, 33/35 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | [[Module 032]] (+2.8), [[Module 023]] (+2.7), [[Module 059]] (+2.7) | [[Module 174]] (-4.7), [[Module 147]] (-3.5), [[Module 193]] (-3.5) |
| 0.5 µM | [[Module 059]] (+3.4), [[Module 070]] (+3.2), [[Module 032]] (+3.1) | [[Module 174]] (-6.8), [[Module 092]] (-5.0), [[Module 193]] (-4.8) |
| 5 µM | [[Module 059]] (+3.6), [[Module 070]] (+3.5), [[Module 032]] (+3.2) | [[Module 174]] (-7.8), [[Module 092]] (-6.0), [[Module 147]] (-4.9) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | [[CHP-212 (line)]] (-6.2), [[LoVo (line)]] (-3.7), [[SK-MEL-2 (line)]] (-3.7), [[NCI-H1792 (line)]] (-3.5) | [[SW480 (line)]] (1.60), [[MIA PaCa-2 (line)]] (1.51), [[CFPAC-1 (line)]] (1.46), [[Hs 766T (line)]] (1.43) · weakest: [[AN3 CA (line)]] (0.479), [[NCI-H661 (line)]] (0.534), [[A-172 (line)]] (0.570) |
| 0.5 µM | [[CHP-212 (line)]] (-6.7), [[NCI-H1792 (line)]] (-6.1), [[SK-MEL-2 (line)]] (-4.7), [[NCI-H23 (line)]] (-3.4) | [[MIA PaCa-2 (line)]] (1.75), [[AsPC-1 (line)]] (1.67), [[SW480 (line)]] (1.65), [[C32 (line)]] (1.60) · weakest: [[NCI-H661 (line)]] (0.267), [[AN3 CA (line)]] (0.469), [[SW 1088 (line)]] (0.550) |
| 5 µM | [[SK-MEL-2 (line)]] (-7.0), [[NCI-H1792 (line)]] (-6.9), [[CHP-212 (line)]] (-6.1), [[COLO 205 (line)]] (-4.0), [[NCI-H23 (line)]] (-3.7) | [[MIA PaCa-2 (line)]] (1.57), [[AsPC-1 (line)]] (1.48), [[NCI-H23 (line)]] (1.42), [[C32 (line)]] (1.33) · weakest: [[NCI-H661 (line)]] (0.455), [[SW 1088 (line)]] (0.562), [[NCI-H2122 (line)]] (0.656) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 1 next most similar without an alert.*

- [[Elimusertib hydrochloride (drug)]] (+0.95, unclear); [[Trametinib (DMSO_TF solvate) (drug)]] (+0.94, MEK inhibitor); [[Trametinib (drug)]] (+0.92, MEK inhibitor, ⚠ vector dose flagged: cell-cycle shift); [[Cobimetinib (drug)]] (+0.91, MEK inhibitor); [[Capmatinib (drug)]] (+0.87, EGFR/ERBB inhibitor); [[BI-3406 (drug)]] (+0.80, RAS inhibitor); [[AZD-7648 (drug)]] (+0.75, DNA synthesis/repair inhibitor); [[Alpelisib (drug)]] (+0.75, PI3K/AKT inhibitor); [[RMC-6236 (drug)]] (+0.73, RAS inhibitor)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 19 arrows, 19 of them with an alert ⚠; grade A 0, B 5, C 14. Shown: the 15 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[KRT86]] | 5 µM | B | KRT86 activity raises the cells' numbers under Binimetinib 5 µM (protects the cells) | lines that do not express KRT86 (19) vs lines expressing it (29) | the lines without KRT86: 0.78× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: SPNS2, EDN2, SLPI |
| [[ADAMTS10]] | 0.05 µM | B | ADAMTS10 activity raises the cells' numbers under Binimetinib 0.05 µM (protects the cells) | lines that do not express ADAMTS10 (27) vs lines expressing it (21) | the lines without ADAMTS10: 0.89× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: TSHZ3, EPHA5-AS1, HECW2; maybe low, not absent |
| [[LINC02575]] | 0.5 µM | B | LINC02575 activity lowers the cells' numbers under Binimetinib 0.5 µM (makes them more sensitive) | lines that do not express LINC02575 (32) vs lines expressing it (16) | the lines without LINC02575: 1.17× the cells of the other lines | 0.090 | ⚠ within organs, on part of the lines; also absent: ENSG00000289309, LINC01205, MSRB3-AS1 |
| [[LINC02575]] | 5 µM | B | LINC02575 activity lowers the cells' numbers under Binimetinib 5 µM (makes them more sensitive) | lines that do not express LINC02575 (32) vs lines expressing it (16) | the lines without LINC02575: 1.21× the cells of the other lines | 0.090 | ⚠ within organs, on part of the lines; also absent: ENSG00000289309, LINC01205, MSRB3-AS1 |
| [[ENSG00000229618]] | 0.5 µM | B | ENSG00000229618 activity lowers the cells' numbers under Binimetinib 0.5 µM (makes them more sensitive) | lines that do not express ENSG00000229618 (32) vs lines expressing it (16) | the lines without ENSG00000229618: 1.08× the cells of the other lines | 0.095 | ⚠ within organs, on part of the lines; also absent: ANKRD20A21P, LINC01205, ENSG00000249776 |
| [[SDC3]] | 0.05 µM | C | SDC3 activity raises the cells' numbers under Binimetinib 0.05 µM (protects the cells) | lines that do not express SDC3 (4) vs lines expressing it (44) | the lines without SDC3: 0.72× the cells of the other lines | 0.021 | ⚠ few lines (4 vs 46); across organs |
| [[SDC3]] | 0.5 µM | C | SDC3 activity raises the cells' numbers under Binimetinib 0.5 µM (protects the cells) | lines that do not express SDC3 (4) vs lines expressing it (44) | the lines without SDC3: 0.72× the cells of the other lines | 0.023 | ⚠ few lines (4 vs 46); across organs |
| [[SDC3]] | 5 µM | C | SDC3 activity raises the cells' numbers under Binimetinib 5 µM (protects the cells) | lines that do not express SDC3 (4) vs lines expressing it (44) | the lines without SDC3: 0.68× the cells of the other lines | 0.029 | ⚠ few lines (4 vs 46); across organs |
| [[NPHS1]] | 0.05 µM | C | NPHS1 activity raises the cells' numbers under Binimetinib 0.05 µM (protects the cells) | lines that do not express NPHS1 (4) vs lines expressing it (44) | the lines without NPHS1: 0.75× the cells of the other lines | 0.061 | ⚠ few lines (4 vs 46); across organs; co-occurs with CTNNB1; also absent: FSD1L, MYO5A, DPF1; maybe low, not absent |
| [[TRIB3]] | 0.5 µM | C | TRIB3 activity raises the cells' numbers under Binimetinib 0.5 µM (protects the cells) | lines that do not express TRIB3 (3) vs lines expressing it (45) | the lines without TRIB3: 0.70× the cells of the other lines | 0.073 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: ARHGAP27, KIAA1522, ALOXE3; maybe low, not absent |
| [[RILP]] | 0.05 µM | C | RILP activity raises the cells' numbers under Binimetinib 0.05 µM (protects the cells) | lines that do not express RILP (3) vs lines expressing it (45) | the lines without RILP: 0.73× the cells of the other lines | 0.075 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: SAT1, KCP, RABGEF1P3; maybe low, not absent |
| [[STX1A]] | 5 µM | C | STX1A activity raises the cells' numbers under Binimetinib 5 µM (protects the cells) | lines that do not express STX1A (3) vs lines expressing it (45) | the lines without STX1A: 0.68× the cells of the other lines | 0.076 | ⚠ few lines (3 vs 47); across organs; also absent: RABGEF1P3, SKAP2, PYGB; maybe low, not absent |
| [[LINC02068]] | 0.05 µM | C | LINC02068 activity raises the cells' numbers under Binimetinib 0.05 µM (protects the cells) | lines that do not express LINC02068 (3) vs lines expressing it (45) | the lines without LINC02068: 0.73× the cells of the other lines | 0.082 | ⚠ few lines (3 vs 47); across organs; also absent: TRIB3; maybe low, not absent |
| [[RILP]] | 5 µM | C | RILP activity raises the cells' numbers under Binimetinib 5 µM (protects the cells) | lines that do not express RILP (3) vs lines expressing it (45) | the lines without RILP: 0.69× the cells of the other lines | 0.082 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: SAT1, KCP, RABGEF1P3; maybe low, not absent |
| [[RRM2]] | 0.05 µM | C | RRM2 activity raises the cells' numbers under Binimetinib 0.05 µM (protects the cells) | lines that do not express RRM2 (3) vs lines expressing it (45) | the lines without RRM2: 0.73× the cells of the other lines | 0.088 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: CLSPN, E2F8, TCF19; maybe low, not absent |

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

- `tables/drugs.parquet` — drug == "Binimetinib"
- `tables/drugdoses.parquet` — dd in 200, 201, 202
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
