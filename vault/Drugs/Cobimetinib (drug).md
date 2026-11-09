---
drug: "Cobimetinib"
type: "drug"
salt_base: "Cobimetinib"
targets: "MAP2K1"
moa_fine: "MEK inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 2969
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Cobimetinib

*MEK inhibitor (inhibitor/antagonist) · targets: MAP2K1 · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 308 / 1728 / 2969; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.05 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.62 / 0.87.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 07]]:D9 | 156 / 152 | — | -0.56 | -0.7/-0.2/-0.1 | — |
| 0.5 µM | [[Plate 08]]:D9 | 1,201 / 527 | — | -0.82 | -1.8/-1.7/-1.4 | — |
| 5 µM | [[Plate 09]]:D9 | 2,043 / 926 | — | -0.60 | -3.1/-1.2/-1.9 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (156 genes, none with an alert; 12 shown): [[ST3GAL4]] 1.28× (z +5.0, 17/47 lines), [[MPP7]] 1.32× (z +4.7, 6/28 lines), [[STK32A]] 1.57× (z +4.4, 7/22 lines), [[KIAA0319]] 1.36× (z +4.4, 11/28 lines), [[IL22RA1]] 1.42× (z +4.4, 5/28 lines), [[COL28A1]] 1.60× (z +4.2, 1/26 lines), [[TEF]] 1.39× (z +4.2, 10/41 lines), [[CDON]] 1.36× (z +4.2, 13/43 lines), [[SNCAIP]] 1.56× (z +4.1, 2/17 lines), [[EFNA1]] 1.50× (z +4.1, 19/32 lines), [[PARP10]] 1.50× (z +4.1, 12/43 lines), [[MKX]] 1.65× (z +4.1, 7/15 lines)

**0.5 µM** (1201 genes, none with an alert; 12 shown): [[GBP2]] 1.99× (z +10.3, 27/34 lines), [[CFB]] 2.60× (z +8.5, 24/27 lines), [[POT1-AS1]] 1.98× (z +7.3, 25/44 lines), [[TRIM22]] 2.03× (z +7.2, 24/29 lines), [[SGO1-AS1]] 1.74× (z +7.1, 27/46 lines), [[GBP1]] 2.14× (z +7.0, 28/31 lines), [[ENSG00000249413]] 1.83× (z +6.9, 26/28 lines), [[MAPK10]] 1.95× (z +6.9, 27/35 lines), [[DIO2]] 2.03× (z +6.8, 18/33 lines), [[ENSG00000197585]] 1.87× (z +6.8, 22/46 lines), [[PGM2L1]] 1.35× (z +6.8, 22/43 lines), [[MATN2]] 1.59× (z +6.7, 19/40 lines)

**5 µM** (2043 genes, none with an alert; 12 shown): [[GBP2]] 3.02× (z +16.0, 33/34 lines), [[CFB]] 4.28× (z +12.5, 25/26 lines), [[GBP1]] 3.35× (z +10.8, 30/31 lines), [[PPM1H]] 1.82× (z +10.3, 29/36 lines), [[TRIM22]] 2.77× (z +10.0, 26/29 lines), [[STK38]] 1.38× (z +9.7, 33/47 lines), [[NREP]] 2.58× (z +9.7, 32/34 lines), [[POT1-AS1]] 2.54× (z +9.5, 31/43 lines), [[SAMD12]] 1.71× (z +9.3, 25/28 lines), [[TMEM140]] 2.77× (z +9.2, 32/35 lines), [[GXYLT2]] 1.85× (z +8.7, 23/36 lines), [[ENSG00000286540]] 2.02× (z +8.7, 22/24 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (152 genes, 4 with an alert ⚠; 15 shown): [[SPRY4]] 0.478× (z -8.9, 38/47 lines), [[ETV5]] 0.698× (z -7.4, 31/47 lines), [[ELK3]] 0.645× (z -6.8, 32/43 lines), [[DUSP6]] 0.448× (z -6.6, 38/43 lines), [[MCL1]] 0.678× (z -6.0, 38/47 lines), [[MCTP1]] 0.679× (z -5.9, 22/34 lines), [[ITGA2]] 0.619× (z -5.9, 28/36 lines), [[FAM107B]] ⚠ 0.742× (z -5.9, 24/36 lines; position correction uncertain), [[SEPTIN10]] 0.764× (z -5.8, 31/47 lines), [[CEMIP]] ⚠ 0.554× (z -5.7, 19/28 lines; position correction uncertain), [[LIF]] ⚠ 0.600× (z -5.5, 24/37 lines; position correction uncertain), [[SRPK1]] 0.798× (z -5.5, 25/47 lines), [[CDCP1]] 0.706× (z -5.4, 24/32 lines), [[ITGB5]] 0.723× (z -5.2, 27/45 lines), [[THSD4]] 0.648× (z -5.1, 23/30 lines)

**0.5 µM** (527 genes, 4 with an alert ⚠; 12 shown): [[ETV5]] 0.253× (z -30.8, 47/47 lines), [[SPRY4]] 0.223× (z -19.5, 46/47 lines), [[ETV4]] 0.327× (z -17.3, 39/45 lines), [[DUSP6]] 0.167× (z -15.9, 42/43 lines), [[EGR1]] 0.179× (z -13.2, 44/45 lines), [[SPRY4-AS1]] 0.281× (z -13.1, 41/44 lines), [[ITGB5]] 0.512× (z -11.7, 39/45 lines), [[MCTP1]] 0.509× (z -11.2, 28/34 lines), [[ITGA2]] 0.438× (z -11.0, 33/36 lines), [[CDCP1]] 0.543× (z -10.3, 29/32 lines), [[NT5E]] 0.436× (z -10.1, 27/33 lines), [[MYEOV]] 0.414× (z -10.0, 22/29 lines)

**5 µM** (926 genes, 4 with an alert ⚠; 12 shown): [[ETV5]] 0.0966× (z -50.3, 46/47 lines), [[SPRY4]] 0.114× (z -27.2, 47/47 lines), [[ETV4]] 0.181× (z -25.5, 42/44 lines), [[DUSP6]] 0.0864× (z -21.0, 42/43 lines), [[ETV1]] 0.198× (z -19.4, 35/36 lines), [[EGR1]] 0.0754× (z -19.1, 45/45 lines), [[SPRY4-AS1]] 0.153× (z -18.7, 44/44 lines), [[ZFPM2-AS1]] 0.361× (z -18.1, 29/31 lines), [[ITGB5]] 0.366× (z -16.9, 41/45 lines), [[MYEOV]] 0.219× (z -16.7, 28/29 lines), [[SPRED2]] 0.359× (z -15.6, 46/47 lines), [[CCND1]] 0.322× (z -15.4, 38/40 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | [[Module 059]] (+3.3) | [[Module 174]] (-3.2), [[Module 147]] (-2.7), [[Module 193]] (-2.3) |
| 0.5 µM | [[Module 032]] (+3.1), [[Module 194]] (+3.0), [[Module 010]] (+2.8) | [[Module 174]] (-6.5), [[Module 092]] (-4.1), [[Module 147]] (-3.7) |
| 5 µM | [[Module 032]] (+4.5), [[Module 070]] (+4.1), [[Module 230]] (+3.9) | [[Module 174]] (-8.6), [[Module 092]] (-6.1), [[Module 147]] (-4.8) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | [[C32 (line)]] (-4.3) | [[C32 (line)]] (1.83), [[AsPC-1 (line)]] (1.65), [[SW48 (line)]] (1.29), [[SW 1271 (line)]] (1.18) · weakest: [[A-172 (line)]] (0.472), [[J82 (line)]] (0.499), [[SHP-77 (line)]] (0.545) |
| 0.5 µM | [[NCI-H1792 (line)]] (-4.3), [[A549 (line)]] (-3.9), [[CHP-212 (line)]] (-3.3), [[NCI-H23 (line)]] (-3.1) | [[C32 (line)]] (1.55), [[MIA PaCa-2 (line)]] (1.49), [[NCI-H23 (line)]] (1.46), [[SW480 (line)]] (1.43) · weakest: [[AN3 CA (line)]] (0.300), [[NCI-H661 (line)]] (0.389), [[SNU-1 (line)]] (0.578) |
| 5 µM | [[NCI-H1792 (line)]] (-5.9), [[CHP-212 (line)]] (-3.7), [[NCI-H23 (line)]] (-3.2) | [[NCI-H23 (line)]] (1.35), [[HOP62 (line)]] (1.31), [[SW480 (line)]] (1.26), [[AsPC-1 (line)]] (1.25) · weakest: [[NCI-H661 (line)]] (0.251), [[AN3 CA (line)]] (0.485), [[SNU-1 (line)]] (0.577) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 1 next most similar without an alert.*

- [[Trametinib (DMSO_TF solvate) (drug)]] (+0.92, MEK inhibitor); [[Elimusertib hydrochloride (drug)]] (+0.92, unclear); [[Binimetinib (drug)]] (+0.91, MEK inhibitor); [[Trametinib (drug)]] (+0.83, MEK inhibitor, ⚠ vector dose flagged: cell-cycle shift); [[Capmatinib (drug)]] (+0.80, EGFR/ERBB inhibitor); [[AZD-7648 (drug)]] (+0.74, DNA synthesis/repair inhibitor); [[BI-3406 (drug)]] (+0.70, RAS inhibitor); [[Perindopril (erbumine) (drug)]] (+0.67, unclear); [[RMC-6236 (drug)]] (+0.67, RAS inhibitor)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 33 arrows, 33 of them with an alert ⚠; grade A 0, B 24, C 9. Shown: the 15 strongest; 18 more arrows (18 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[ADRA1B]] | 5 µM | B | ADRA1B activity lowers the cells' numbers under Cobimetinib 5 µM (makes them more sensitive) | lines that do not express ADRA1B (24) vs lines expressing it (24) | the lines without ADRA1B: 1.16× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: IL31RA, IGFBP3, STAC |
| [[C15orf48]] | 5 µM | B | C15orf48 activity lowers the cells' numbers under Cobimetinib 5 µM (makes them more sensitive) | lines that do not express C15orf48 (25) vs lines expressing it (23) | the lines without C15orf48: 1.15× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: ZNF229, HMGN2P46, RHCG |
| [[TLR1]] | 5 µM | B | TLR1 activity lowers the cells' numbers under Cobimetinib 5 µM (makes them more sensitive) | lines that do not express TLR1 (15) vs lines expressing it (33) | the lines without TLR1: 1.23× the cells of the other lines | 0.024 | ⚠ within organs, on part of the lines; also absent: TLR6, ENSG00000289526, TMEM158 |
| [[STAC]] | 5 µM | B | STAC activity lowers the cells' numbers under Cobimetinib 5 µM (makes them more sensitive) | lines that do not express STAC (25) vs lines expressing it (23) | the lines without STAC: 1.21× the cells of the other lines | 0.056 | ⚠ within organs, on part of the lines; also absent: GUCY1B1, ZNF229, DNAH11 |
| [[TLR6]] | 5 µM | B | TLR6 activity lowers the cells' numbers under Cobimetinib 5 µM (makes them more sensitive) | lines that do not express TLR6 (16) vs lines expressing it (32) | the lines without TLR6: 1.23× the cells of the other lines | 0.062 | ⚠ within organs, on part of the lines; also absent: TLR1, ENSG00000289526, CYP27C1; maybe low, not absent |
| [[TLR1]] | 0.5 µM | B | TLR1 activity lowers the cells' numbers under Cobimetinib 0.5 µM (makes them more sensitive) | lines that do not express TLR1 (15) vs lines expressing it (33) | the lines without TLR1: 1.27× the cells of the other lines | 0.069 | ⚠ within organs, on part of the lines; also absent: TLR6, ENSG00000289526, TMEM158 |
| [[FHOD3]] | 5 µM | B | FHOD3 activity lowers the cells' numbers under Cobimetinib 5 µM (makes them more sensitive) | lines that do not express FHOD3 (14) vs lines expressing it (34) | the lines without FHOD3: 1.19× the cells of the other lines | 0.071 | ⚠ within organs, on part of the lines; also absent: GJC1, ENSG00000267405, MAMLD1 |
| [[STAC]] | 0.5 µM | B | STAC activity lowers the cells' numbers under Cobimetinib 0.5 µM (makes them more sensitive) | lines that do not express STAC (25) vs lines expressing it (23) | the lines without STAC: 1.27× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: GUCY1B1, ZNF229, DNAH11 |
| [[JCAD]] | 5 µM | B | JCAD activity lowers the cells' numbers under Cobimetinib 5 µM (makes them more sensitive) | lines that do not express JCAD (20) vs lines expressing it (28) | the lines without JCAD: 1.14× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: ANKRD33B, FAT4, EFEMP1 |
| [[SLFN5]] | 0.5 µM | B | SLFN5 activity lowers the cells' numbers under Cobimetinib 0.5 µM (makes them more sensitive) | lines that do not express SLFN5 (11) vs lines expressing it (37) | the lines without SLFN5: 1.32× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; also absent: ENSG00000261273, ETS1, SAMD9; maybe low, not absent |
| [[C15orf48]] | 0.5 µM | B | C15orf48 activity lowers the cells' numbers under Cobimetinib 0.5 µM (makes them more sensitive) | lines that do not express C15orf48 (25) vs lines expressing it (23) | the lines without C15orf48: 1.24× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; also absent: ZNF229, HMGN2P46, RHCG |
| [[ENSG00000232386]] | 5 µM | B | ENSG00000232386 activity lowers the cells' numbers under Cobimetinib 5 µM (makes them more sensitive) | lines that do not express ENSG00000232386 (17) vs lines expressing it (31) | the lines without ENSG00000232386: 1.18× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; also absent: GCAWKR, BEX2, BEX4 |
| [[TSPAN2]] | 5 µM | B | TSPAN2 activity lowers the cells' numbers under Cobimetinib 5 µM (makes them more sensitive) | lines that do not express TSPAN2 (19) vs lines expressing it (29) | the lines without TSPAN2: 1.21× the cells of the other lines | 0.077 | ⚠ within organs, on part of the lines; also absent: SAA1, STK32A, IFI44L |
| [[ENSG00000259354]], [[HMGN2P46]] | 0.5 µM | B | ENSG00000259354, HMGN2P46 activity lowers the cells' numbers under Cobimetinib 0.5 µM (makes them more sensitive) | lines that do not express ENSG00000259354, HMGN2P46 (18) vs lines expressing them (30) | the lines without ENSG00000259354, HMGN2P46: 1.22× the cells of the other lines | 0.078 | ⚠ within organs, on part of the lines; also absent: C15orf48, IL1R1, STAC; co-absent genes |
| [[ENSG00000259354]], [[HMGN2P46]] | 5 µM | B | ENSG00000259354, HMGN2P46 activity lowers the cells' numbers under Cobimetinib 5 µM (makes them more sensitive) | lines that do not express ENSG00000259354, HMGN2P46 (18) vs lines expressing them (30) | the lines without ENSG00000259354, HMGN2P46: 1.11× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: C15orf48, IL1R1, STAC; co-absent genes |

### Its targets: what acting on them probably does

*Drug-target arrows of the compound classes it belongs to (compounds sharing a listed target and mechanism; one molecule counts once, under all its names): the target → a gene whose level those compounds move. A row that names several targets is one test: the compounds share them all, and any of them could be the cause. 963 arrows, 963 of them with an alert ⚠; grade A 0, B 963, C 0. Shown: the 15 strongest; 948 more arrows (948 of them with an alert ⚠) not shown.*

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

- `tables/drugs.parquet` — drug == "Cobimetinib"
- `tables/drugdoses.parquet` — dd in 290, 291, 292
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
