---
drug: "Ixazomib citrate"
type: "drug"
salt_base: "Ixazomib citrate"
targets: "PSMB1, PSMB2, PSMB5"
moa_fine: "Proteasome inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 7136
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Ixazomib citrate

*Proteasome inhibitor (inhibitor/antagonist) · targets: PSMB1, PSMB2, PSMB5 · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 11 / 5967 / 7136; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.05 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.31 / 0.94.
> Flags by dose: - / - / cell-cycle shift. ⚠ 5 µM: cell-cycle shift (artifact flags: its changes there are shown with an alert, not left out).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 10]]:G8 | 11 / 0 | — | -0.10 | -0.7/-0.1/+1.9 | — |
| 0.5 µM | [[Plate 11]]:G8 | 2,689 / 3,278 | — | -0.32 | +3.7/-1.8/+19.2 | — |
| 5 µM | [[Plate 12]]:G8 | 3,303 / 3,833 | — | -0.67 | +3.0/-5.2/+20.1 | ⚠ cell-cycle shift |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (11 genes, none with an alert): [[DYNC1I1]] 1.55× (z +5.5, 17/34 lines), [[DGKG]] 1.30× (z +4.6, 13/34 lines), [[PIR]] 1.34× (z +4.6, 13/37 lines), [[MLLT11]] 1.54× (z +4.2, 14/26 lines), [[DAP3]] 1.23× (z +3.9, 24/48 lines), [[PSMD13]] 1.22× (z +3.8, 17/48 lines), [[TMEM161A]] 1.20× (z +3.5, 7/46 lines), [[NMRAL2P]] 1.43× (z +3.3, 10/29 lines), [[PSMD3]] 1.23× (z +3.2, 21/48 lines), [[EGF]] 1.34× (z +3.1, 9/24 lines), [[ENSG00000232053]] 1.24× (z +2.9, 5/16 lines)

**0.5 µM** (2689 genes, none with an alert; 12 shown): [[DNAJB1]] 12.9× (z +34.3, 48/48 lines), [[HSPA1B]] 35.9× (z +31.9, 48/48 lines), [[PSMD1]] 4.24× (z +30.1, 48/48 lines), [[BAG3]] 6.72× (z +29.8, 48/48 lines), [[UFD1]] 4.29× (z +28.5, 48/48 lines), [[DNAJA4]] 7.17× (z +28.3, 25/25 lines), [[CAMK2G]] 2.98× (z +27.9, 48/48 lines), [[PSMD11]] 3.82× (z +27.1, 48/48 lines), [[HSPA1A]] 53.5× (z +26.5, 34/34 lines), [[PSMD12]] 2.86× (z +26.4, 48/48 lines), [[NAA25]] 3.16× (z +26.2, 48/48 lines), [[HSPH1]] 15.4× (z +25.7, 48/48 lines)

**5 µM** (3303 genes, 612 with an alert ⚠; the drug-dose carries ⚠ cell-cycle shift; 12 shown): [[BAG3]] 8.62× (z +38.4, 48/48 lines; cell-cycle shift (explains ~0% here)), [[DNAJB1]] 17.0× (z +38.1, 48/48 lines; cell-cycle shift (explains ~0% here)), [[HSPA1B]] 49.5× (z +34.8, 47/47 lines; cell-cycle shift (explains ~0% here)), [[CAMK2G]] 3.68× (z +33.2, 48/48 lines; cell-cycle shift (explains ~0% here)), [[PSMD1]] 4.57× (z +31.7, 48/48 lines; cell-cycle shift (explains ~3% here)), [[HSPH1]] 21.1× (z +31.6, 48/48 lines; cell-cycle shift (explains ~0% here)), [[DNAJA4]] 8.94× (z +31.5, 25/25 lines; cell-cycle shift (explains ~0% here)), [[UFD1]] 4.96× (z +31.3, 48/48 lines; cell-cycle shift (explains ~3% here)), [[PSMD12]] 3.29× (z +30.0, 48/48 lines; cell-cycle shift (explains ~0% here)), [[PCYT1A]] 2.49× (z +29.3, 46/48 lines; cell-cycle shift (explains ~6% here)), [[HSPA1A]] 76.3× (z +28.9, 34/34 lines; cell-cycle shift (explains ~0% here)), [[PSMD11]] 3.84× (z +28.5, 48/48 lines; cell-cycle shift (explains ~0% here))

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (3278 genes, none with an alert; 12 shown): [[TPCN1]] 0.477× (z -16.8, 45/48 lines), [[TMTC2]] 0.446× (z -16.2, 40/42 lines), [[ZC3H6]] 0.495× (z -15.5, 43/48 lines), [[SLC1A1]] 0.429× (z -14.2, 36/37 lines), [[NR2F2-AS1]] 0.311× (z -14.1, 37/40 lines), [[ZNF33A]] 0.615× (z -14.0, 44/48 lines), [[LINC01876]] 0.369× (z -13.6, 24/24 lines), [[TRERF1]] 0.481× (z -13.3, 40/42 lines), [[ZSWIM5]] 0.512× (z -13.3, 40/43 lines), [[SCLT1]] 0.519× (z -13.1, 45/48 lines), [[SLC2A10]] 0.311× (z -12.9, 25/29 lines), [[H6PD]] 0.460× (z -12.8, 43/48 lines)

**5 µM** (3833 genes, 486 with an alert ⚠; the drug-dose carries ⚠ cell-cycle shift; 12 shown): [[ZC3H6]] 0.394× (z -20.6, 48/48 lines; cell-cycle shift (explains ~11% here)), [[TPCN1]] 0.415× (z -20.0, 44/48 lines; cell-cycle shift (explains ~0% here)), [[ZSWIM5]] 0.406× (z -17.9, 41/43 lines; cell-cycle shift (explains ~0% here)), [[SCLT1]] 0.410× (z -17.8, 46/48 lines; cell-cycle shift (explains ~10% here)), [[TXNIP]] 0.265× (z -17.3, 35/37 lines; cell-cycle shift (explains ~22% here)), [[CCDC18-AS1]] 0.349× (z -16.9, 48/48 lines; cell-cycle shift (explains ~0% here)), [[PLD1]] 0.322× (z -16.5, 35/41 lines; cell-cycle shift (explains ~2% here)), [[RIN2]] 0.336× (z -16.4, 35/39 lines; cell-cycle shift (explains ~0% here)), [[NR2F2-AS1]] 0.259× (z -16.3, 40/40 lines; cell-cycle shift (explains ~5% here)), [[CCDC7]] 0.320× (z -16.2, 44/46 lines; cell-cycle shift (explains ~0% here)), [[RNF170]] 0.284× (z -16.1, 43/47 lines; cell-cycle shift (explains ~0% here)), [[POLI]] 0.358× (z -16.0, 46/47 lines; cell-cycle shift (explains ~0% here))

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | [[Module 060]] (+18.5), [[Module 072]] (+11.9), [[Module 064]] (+10.3) | [[Module 170]] (-8.4), [[Module 234]] (-5.0), [[Module 200]] (-4.7) |
| 5 µM | [[Module 060]] (+20.4), [[Module 072]] (+12.7), [[Module 135]] (+11.0) | [[Module 170]] (-8.0), [[Module 200]] (-6.1), [[Module 148]] (-5.7) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | [[SK-MEL-2 (line)]] (-6.9), [[RPMI-7951 (line)]] (-5.4), [[C32 (line)]] (-4.7), [[J82 (line)]] (-3.2) | [[HT-29 (line)]] (1.41), [[COLO 205 (line)]] (1.33), [[HOP62 (line)]] (1.33), [[H4 (line)]] (1.33) · weakest: [[SHP-77 (line)]] (0.609), [[NCI-H2347 (line)]] (0.660), [[CHP-212 (line)]] (0.673) |
| 5 µM | [[RPMI-7951 (line)]] (-10.9), [[H4 (line)]] (-7.4), [[HS-578T (line)]] (-6.0), [[J82 (line)]] (-5.5), [[SW 900 (line)]] (-4.1) | [[H4 (line)]] (1.36), [[PANC-1 (line)]] (1.27), [[HT-29 (line)]] (1.26), [[MIA PaCa-2 (line)]] (1.25) · weakest: [[SHP-77 (line)]] (0.596), [[SW 1088 (line)]] (0.630), [[NCI-H2347 (line)]] (0.643) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

⚠ This drug's own vector: vector dose flagged: cell-cycle shift. Read its neighbours with that in mind.

*378 other drugs have a vector, 121 with an alert ⚠; shown: the 8 most similar and the 1 next most similar without an alert.*

- [[Bortezomib (drug)]] (+0.95, Proteasome inhibitor, ⚠ vector dose flagged: cell-cycle shift); [[Infigratinib (drug)]] (+0.30, Other TK inhibitor); [[EX229 (drug)]] (+0.27, unclear); [[Hydroxyfasudil (drug)]] (+0.26, unclear); [[Auranofin (drug)]] (+0.26, unclear); [[venetoclax (drug)]] (+0.24, unclear); [[c-Kit-IN-1 (drug)]] (+0.24, Multi-TK inhibitor); [[Neratinib (drug)]] (+0.23, EGFR/ERBB inhibitor); [[Clotrimazole (drug)]] (+0.23, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 16 arrows, 16 of them with an alert ⚠; grade A 0, B 7, C 9. Shown: the 15 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[PLEKHG3]] | 5 µM | B | PLEKHG3 activity raises the cells' numbers under Ixazomib citrate 5 µM (protects the cells) | lines that do not express PLEKHG3 (5) vs lines expressing it (43) | the lines without PLEKHG3: 0.57× the cells of the other lines | 0.028 | ⚠ across organs; also absent: ATP11A, SHC2, PPP1R26; maybe low, not absent |
| [[PDZRN3]] | 5 µM | B | PDZRN3 activity lowers the cells' numbers under Ixazomib citrate 5 µM (makes them more sensitive) | lines that do not express PDZRN3 (30) vs lines expressing it (18) | the lines without PDZRN3: 1.32× the cells of the other lines | 0.084 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000237268, ENSG00000253642, ENSG00000288098 |
| [[ENSG00000232884]] | 0.5 µM | B | ENSG00000232884 activity raises the cells' numbers under Ixazomib citrate 0.5 µM (protects the cells) | lines that do not express ENSG00000232884 (12) vs lines expressing it (36) | the lines without ENSG00000232884: 0.75× the cells of the other lines | 0.089 | ⚠ within organs, on part of the lines; also absent: ENSG00000235609, NRIP1, ATXN1; maybe low, not absent |
| [[ZNF185]] | 5 µM | B | ZNF185 activity raises the cells' numbers under Ixazomib citrate 5 µM (protects the cells) | lines that do not express ZNF185 (15) vs lines expressing it (33) | the lines without ZNF185: 0.66× the cells of the other lines | 0.092 | ⚠ within organs, on part of the lines; also absent: HTR1D, KLF5, IL18 |
| [[TCF4]] | 5 µM | B | TCF4 activity lowers the cells' numbers under Ixazomib citrate 5 µM (makes them more sensitive) | lines that do not express TCF4 (25) vs lines expressing it (23) | the lines without TCF4: 1.55× the cells of the other lines | 0.098 | ⚠ within organs, on part of the lines; also absent: KCNT2, APCDD1L, MSC-AS1 |
| [[TOR4A]] | 0.5 µM | B | TOR4A activity raises the cells' numbers under Ixazomib citrate 0.5 µM (protects the cells) | lines that do not express TOR4A (14) vs lines expressing it (34) | the lines without TOR4A: 0.71× the cells of the other lines | 0.098 | ⚠ within organs, on part of the lines; also absent: PLEKHA6, CDCP1, C19orf33 |
| [[HGF]] | 5 µM | B | HGF activity lowers the cells' numbers under Ixazomib citrate 5 µM (makes them more sensitive) | lines that do not express HGF (38) vs lines expressing it (10) | the lines without HGF: 1.55× the cells of the other lines | 0.0995 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: SYT4, RIT2, CALCA |
| [[ATAD1]], [[PTEN]] | 5 µM | C | ATAD1, PTEN activity raises the cells' numbers under Ixazomib citrate 5 µM (protects the cells) | lines that do not express ATAD1, PTEN (4) vs lines expressing them (44) | the lines without ATAD1, PTEN: 0.54× the cells of the other lines | 0.014 | ⚠ few lines (4 vs 46); tissue-confounded; across organs; also absent: CFL1P1-1, ZC3HAV1L, OSR2; co-absent genes |
| [[TNFRSF25]] | 0.5 µM | C | TNFRSF25 activity raises the cells' numbers under Ixazomib citrate 0.5 µM (protects the cells) | lines that do not express TNFRSF25 (4) vs lines expressing it (44) | the lines without TNFRSF25: 0.63× the cells of the other lines | 0.024 | ⚠ few lines (4 vs 46); tissue-confounded; across organs; also absent: PLEKHG5, ENSG00000284716 |
| [[OPLAH]] | 5 µM | C | OPLAH activity raises the cells' numbers under Ixazomib citrate 5 µM (protects the cells) | lines that do not express OPLAH (10) vs lines expressing it (38) | the lines without OPLAH: 0.66× the cells of the other lines | 0.028 | ⚠ tissue-confounded; across organs; co-occurs with TERT; also absent: TNFRSF10D, PATJ, EPHX2 |
| [[ENSG00000286964]] | 5 µM | C | ENSG00000286964 activity lowers the cells' numbers under Ixazomib citrate 5 µM (makes them more sensitive) | lines that do not express ENSG00000286964 (10) vs lines expressing it (38) | the lines without ENSG00000286964: 1.47× the cells of the other lines | 0.042 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: SIX1, C2orf74, SYDE1 |
| [[SPART-AS1]] | 5 µM | C | SPART-AS1 activity lowers the cells' numbers under Ixazomib citrate 5 µM (makes them more sensitive) | lines that do not express SPART-AS1 (16) vs lines expressing it (32) | the lines without SPART-AS1: 1.40× the cells of the other lines | 0.053 | ⚠ tissue-confounded; across organs; also absent: CCDC169, FIGN, SPART |
| [[ENSG00000214265]], [[SNHG14]], [[SNRPN]] | 5 µM | C | ENSG00000214265, SNHG14, SNRPN activity lowers the cells' numbers under Ixazomib citrate 5 µM (makes them more sensitive) | lines that do not express ENSG00000214265, SNHG14, SNRPN (14) vs lines expressing them (34) | the lines without ENSG00000214265, SNHG14, SNRPN: 1.40× the cells of the other lines | 0.054 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: RNF150, CHST10, ENSG00000268163; co-absent genes |
| [[ENSG00000284716]] | 0.5 µM | C | ENSG00000284716 activity raises the cells' numbers under Ixazomib citrate 0.5 µM (protects the cells) | lines that do not express ENSG00000284716 (5) vs lines expressing it (43) | the lines without ENSG00000284716: 0.70× the cells of the other lines | 0.055 | ⚠ tissue-confounded; across organs; also absent: FTH1, TMEM184A, ZFP36; maybe low, not absent |
| [[TNFRSF10D]] | 0.5 µM | C | TNFRSF10D activity raises the cells' numbers under Ixazomib citrate 0.5 µM (protects the cells) | lines that do not express TNFRSF10D (11) vs lines expressing it (37) | the lines without TNFRSF10D: 0.78× the cells of the other lines | 0.055 | ⚠ tissue-confounded; across organs; also absent: OPLAH, LINC00857, LPIN3 |

### Its targets: what acting on them probably does

*Drug-target arrows of the compound classes it belongs to (compounds sharing a listed target and mechanism; one molecule counts once, under all its names): the target → a gene whose level those compounds move. A row that names several targets is one test: the compounds share them all, and any of them could be the cause. 493 arrows, 493 of them with an alert ⚠; grade A 0, B 493, C 0. Shown: the 15 strongest; 478 more arrows (478 of them with an alert ⚠) not shown.*

| Its target | Gene it moves | This drug | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|---|
| [[PSMB5]] | [[BTG2]] | moves it that way too | B | PSMB5 activity raises BTG2's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PSMB5]] | [[EMSY-DT]] | moves it that way too | B | PSMB5 activity raises EMSY-DT's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PSMB5]] | [[FAM200B]] | moves it that way too | B | PSMB5 activity raises FAM200B's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PSMB5]] | [[GNAQ]] | moves it that way too | B | PSMB5 activity lowers GNAQ's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PSMB5]] | [[GPR37]] | moves it that way too | B | PSMB5 activity raises GPR37's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PSMB5]] | [[ISYNA1]] | moves it that way too | B | PSMB5 activity raises ISYNA1's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PSMB5]] | [[MYRIP]] | moves it that way too | B | PSMB5 activity raises MYRIP's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PSMB5]] | [[NPTXR]] | moves it that way too | B | PSMB5 activity raises NPTXR's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PSMB5]] | [[NT5C2]] | moves it that way too | B | PSMB5 activity lowers NT5C2's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PSMB5]] | [[PPIL2]] | moves it that way too | B | PSMB5 activity lowers PPIL2's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PSMB5]] | [[RFLNA]] | moves it that way too | B | PSMB5 activity raises RFLNA's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PSMB5]] | [[RUFY2]] | moves it that way too | B | PSMB5 activity lowers RUFY2's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PSMB5]] | [[TRMT2B]] | moves it that way too | B | PSMB5 activity lowers TRMT2B's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PSMB5]] | [[VARS2]] | moves it that way too | B | PSMB5 activity raises VARS2's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PSMB5]] | [[WWP1]] | moves it that way too | B | PSMB5 activity lowers WWP1's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |

## Data

- `tables/drugs.parquet` — drug == "Ixazomib citrate"
- `tables/drugdoses.parquet` — dd in 579, 580, 581
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
