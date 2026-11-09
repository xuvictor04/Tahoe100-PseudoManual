---
drug: "Ixazomib"
type: "drug"
salt_base: "Ixazomib"
targets: "PSMB5"
moa_fine: "Proteasome inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 255
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Ixazomib

*Proteasome inhibitor (inhibitor/antagonist) · targets: PSMB5 · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 131 / 0 / 255; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): -0.23 / 0.12.
> Flags by dose: - / noisy plate (z scaled) / noisy plate (z scaled).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 01]]:G3 | 65 / 66 | — | -0.77 | +0.3/+1.2/+1.2 | — |
| 0.5 µM | [[Plate 02]]:G3 | 0 / 0 | — | +0.43 | -0.3/+0.0/-0.8 | noisy plate (z scaled) |
| 5 µM | [[Plate 03]]:G3 | 79 / 176 | — | -0.44 | -1.7/-0.0/-0.2 | noisy plate (z scaled) |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (65 genes, none with an alert; 12 shown): [[ENSG00000237550]] 1.80× (z +4.4, 21/44 lines), [[CACNB2]] 1.45× (z +4.3, 1/14 lines), [[CMAHP]] 1.34× (z +4.2, 8/45 lines), [[TMEM30B]] 1.55× (z +4.2, 0/13 lines), [[SORT1]] 1.24× (z +3.7, 8/40 lines), [[CD302]] 1.33× (z +3.7, 7/43 lines), [[VSNL1]] 1.44× (z +3.7, 0/13 lines), [[ENSG00000235979]] 1.88× (z +3.7, 13/44 lines), [[RING1]] 1.26× (z +3.7, 5/47 lines), [[ENSG00000269755]] 1.39× (z +3.7, 2/34 lines), [[ENSG00000253363]] 1.57× (z +3.6, 2/9 lines), [[KLF11]] 1.26× (z +3.6, 8/42 lines)

**5 µM** (79 genes, none with an alert; 12 shown): [[RING1]] 1.80× (z +5.2, 23/45 lines), [[SORT1]] 1.71× (z +5.1, 18/39 lines), [[ADD3]] 1.52× (z +4.6, 22/43 lines), [[SESN3]] 1.64× (z +4.5, 8/28 lines), [[GSN]] 1.61× (z +4.5, 19/44 lines), [[CAT]] 1.69× (z +4.3, 17/45 lines), [[APOLD1]] 1.36× (z +4.2, 16/48 lines), [[OLFML2A]] 2.03× (z +4.0, 7/24 lines), [[PEG10]] 1.73× (z +4.0, 15/31 lines), [[HSD17B11]] 1.47× (z +3.9, 14/44 lines), [[PCBP2]] 1.42× (z +3.8, 37/48 lines), [[HNMT]] 1.75× (z +3.8, 6/28 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (66 genes, none with an alert; 12 shown): [[PARP12]] 0.689× (z -4.9, 28/45 lines), [[AKT2]] 0.821× (z -4.4, 16/47 lines), [[NLRC5]] 0.702× (z -4.4, 22/42 lines), [[PML]] 0.776× (z -4.3, 24/46 lines), [[RIGI]] 0.669× (z -4.3, 26/44 lines), [[ENSG00000111788]] 0.650× (z -4.1, 13/40 lines), [[STAT2]] 0.750× (z -4.0, 27/47 lines), [[REC8]] 0.628× (z -3.9, 18/44 lines), [[DHX58]] 0.713× (z -3.9, 8/40 lines), [[PAN2]] 0.733× (z -3.9, 16/47 lines), [[PLSCR1]] 0.730× (z -3.9, 24/40 lines), [[OSMR-DT]] 0.741× (z -3.8, 18/33 lines)

**5 µM** (176 genes, none with an alert; 12 shown): [[PARP9]] 0.226× (z -9.4, 32/40 lines), [[EIF2AK2]] 0.374× (z -9.3, 33/47 lines), [[MX1]] 0.193× (z -9.1, 26/29 lines), [[OAS3]] 0.221× (z -8.4, 31/42 lines), [[STAT1]] 0.343× (z -8.2, 35/48 lines), [[PARP12]] 0.355× (z -7.6, 32/45 lines), [[PLSCR1]] 0.328× (z -7.6, 32/40 lines), [[IFI44]] 0.323× (z -7.3, 26/36 lines), [[TRIM25]] 0.489× (z -7.2, 33/48 lines), [[OAS2]] 0.159× (z -7.2, 26/32 lines), [[USP18]] 0.249× (z -7.0, 28/40 lines), [[SP100]] 0.528× (z -7.0, 31/45 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | [[Module 045]] (+2.1) | — |
| 0.5 µM | — | — |
| 5 µM | [[Module 059]] (+2.1) | [[Module 032]] (-3.2) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | [[A-172 (line)]] (-4.2), [[J82 (line)]] (-4.1), [[A498 (line)]] (-3.8) | [[CHP-212 (line)]] (1.37), [[NCI-H1792 (line)]] (1.26), [[SW 1088 (line)]] (1.16), [[BT-474 (line)]] (1.14) · weakest: [[SW480 (line)]] (0.556), [[NCI-H2030 (line)]] (0.634), [[NCI-H460 (line)]] (0.650) |
| 0.5 µM | — | — |
| 5 µM | [[H4 (line)]] (-3.9), [[NCI-H1792 (line)]] (-3.2), [[A-172 (line)]] (-3.2), [[A-427 (line)]] (-3.1) | [[BT-474 (line)]] (1.54), [[MIA PaCa-2 (line)]] (1.54), [[COLO 205 (line)]] (1.54), [[LoVo (line)]] (1.44) · weakest: [[NCI-H661 (line)]] (0.205), [[LS 180 (line)]] (0.225), [[HEC-1-A (line)]] (0.278) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 2 next most similar without an alert.*

- [[Entrectinib (drug)]] (+0.59, Other TK inhibitor); [[Tofacitinib (drug)]] (+0.57, JAK/STAT inhibitor); [[Ponatinib (drug)]] (+0.54, Multi-TK inhibitor); [[NG25 (drug)]] (+0.53, Other MAPK inhibitor, ⚠ vector dose flagged: cell-cycle shift); [[Tofacitinib (citrate) (drug)]] (+0.52, JAK/STAT inhibitor); [[Alpelisib (drug)]] (+0.48, PI3K/AKT inhibitor); [[Fedratinib (hydrochloride hydrate) (drug)]] (+0.48, JAK/STAT inhibitor); [[Selinexor (drug)]] (+0.45, unclear, ⚠ vector dose flagged: cell-cycle shift); [[IQ 1 (drug)]] (+0.41, unclear); [[Cabozantinib (S-malate) (drug)]] (+0.40, Multi-TK inhibitor)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 56 arrows, 56 of them with an alert ⚠; grade A 0, B 42, C 14. Shown: the 15 strongest; 41 more arrows (41 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[FAAH2]] | 0.05 µM | B | FAAH2 activity raises the cells' numbers under Ixazomib 0.05 µM (protects the cells) | lines that do not express FAAH2 (26) vs lines expressing it (22) | the lines without FAAH2: 0.77× the cells of the other lines | 0.036 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, TNNT2, ST14; maybe low, not absent |
| [[EID2B]] | 0.05 µM | B | EID2B activity lowers the cells' numbers under Ixazomib 0.05 µM (makes them more sensitive) | lines that do not express EID2B (13) vs lines expressing it (35) | the lines without EID2B: 1.27× the cells of the other lines | 0.036 | ⚠ within organs, on part of the lines; also absent: ANTXR1, SIRPA, MSRB3; maybe low, not absent |
| [[SGPP2]] | 0.05 µM | B | SGPP2 activity raises the cells' numbers under Ixazomib 0.05 µM (protects the cells) | lines that do not express SGPP2 (32) vs lines expressing it (16) | the lines without SGPP2: 0.78× the cells of the other lines | 0.037 | ⚠ within organs, on part of the lines; also absent: ST14, CATSPERB, TMPRSS4 |
| [[DUOX2]] | 0.05 µM | B | DUOX2 activity raises the cells' numbers under Ixazomib 0.05 µM (protects the cells) | lines that do not express DUOX2 (32) vs lines expressing it (16) | the lines without DUOX2: 0.85× the cells of the other lines | 0.043 | ⚠ within organs, on part of the lines; also absent: MMP7, SLC44A4, MAOB |
| [[NPAS1]] | 5 µM | B | NPAS1 activity lowers the cells' numbers under Ixazomib 5 µM (makes them more sensitive) | lines that do not express NPAS1 (9) vs lines expressing it (39) | the lines without NPAS1: 1.28× the cells of the other lines | 0.050 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[PCSK9]] | 0.05 µM | B | PCSK9 activity raises the cells' numbers under Ixazomib 0.05 µM (protects the cells) | lines that do not express PCSK9 (28) vs lines expressing it (20) | the lines without PCSK9: 0.81× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: C6orf132, RNF223, CDH1 |
| [[C1orf116]], [[IRF6]] | 0.05 µM | B | C1orf116, IRF6 activity raises the cells' numbers under Ixazomib 0.05 µM (protects the cells) | lines that do not express C1orf116, IRF6 (31) vs lines expressing them (17) | the lines without C1orf116, IRF6: 0.77× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: ST14, TMPRSS4, TMEM125; co-absent genes |
| [[TGFA]] | 0.05 µM | B | TGFA activity raises the cells' numbers under Ixazomib 0.05 µM (protects the cells) | lines that do not express TGFA (17) vs lines expressing it (31) | the lines without TGFA: 0.85× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: AQP3, ELF3, VIPR1 |
| [[GABBR2]] | 0.05 µM | B | GABBR2 activity lowers the cells' numbers under Ixazomib 0.05 µM (makes them more sensitive) | lines that do not express GABBR2 (25) vs lines expressing it (23) | the lines without GABBR2: 1.15× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: JPH3, JAKMIP1, LMX1B; maybe low, not absent |
| [[ENSG00000259925]] | 0.05 µM | B | ENSG00000259925 activity raises the cells' numbers under Ixazomib 0.05 µM (protects the cells) | lines that do not express ENSG00000259925 (32) vs lines expressing it (16) | the lines without ENSG00000259925: 0.79× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; also absent: SGPP2, MUC5B, TMPRSS4 |
| [[AGR2]] | 0.05 µM | B | AGR2 activity raises the cells' numbers under Ixazomib 0.05 µM (protects the cells) | lines that do not express AGR2 (32) vs lines expressing it (16) | the lines without AGR2: 0.80× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; also absent: FXYD3, SERPINB5, PRKCH-AS1 |
| [[MAP1A]] | 0.05 µM | B | MAP1A activity lowers the cells' numbers under Ixazomib 0.05 µM (makes them more sensitive) | lines that do not express MAP1A (17) vs lines expressing it (31) | the lines without MAP1A: 1.19× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; also absent: HMCN1, HOXB-AS1, LINC02269; maybe low, not absent |
| [[TSPAN1]] | 0.05 µM | B | TSPAN1 activity raises the cells' numbers under Ixazomib 0.05 µM (protects the cells) | lines that do not express TSPAN1 (26) vs lines expressing it (22) | the lines without TSPAN1: 0.81× the cells of the other lines | 0.078 | ⚠ within organs, on part of the lines; also absent: TRIM29, CDH1, IRF6 |
| [[CACNG7]] | 0.05 µM | B | CACNG7 activity lowers the cells' numbers under Ixazomib 0.05 µM (makes them more sensitive) | lines that do not express CACNG7 (21) vs lines expressing it (27) | the lines without CACNG7: 1.24× the cells of the other lines | 0.079 | ⚠ within organs, on part of the lines; also absent: WNT5B, P3H2, EID2B |
| [[DCLK2]] | 0.05 µM | B | DCLK2 activity lowers the cells' numbers under Ixazomib 0.05 µM (makes them more sensitive) | lines that do not express DCLK2 (17) vs lines expressing it (31) | the lines without DCLK2: 1.24× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: LINC03041, HECW2, AFF3 |

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

- `tables/drugs.parquet` — drug == "Ixazomib"
- `tables/drugdoses.parquet` — dd in 576, 577, 578
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
