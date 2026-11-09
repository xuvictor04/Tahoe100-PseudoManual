---
drug: "Doxorubicin (hydrochloride)"
type: "drug"
salt_base: "Doxorubicin"
targets: "TOP2A, TOP2B, TOP1"
moa_fine: "DNA synthesis/repair inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 7317
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Doxorubicin (hydrochloride)

*DNA synthesis/repair inhibitor (inhibitor/antagonist) · targets: TOP2A, TOP2B, TOP1 · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 11 / 213 / 7317; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.05 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.04 / 0.31.
> Flags by dose: - / - / cell-cycle shift. ⚠ 5 µM: cell-cycle shift (artifact flags: its changes there are shown with an alert, not left out).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 07]]:G3 | 9 / 2 | — | +0.15 | +0.9/+1.1/+1.0 | — |
| 0.5 µM | [[Plate 08]]:G3 | 131 / 82 | — | -0.74 | +2.4/-1.0/-0.5 | — |
| 5 µM | [[Plate 09]]:G3 | 4,738 / 2,579 | — | -0.65 | +9.4/+0.0/+1.8 | ⚠ cell-cycle shift |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (9 genes, none with an alert): [[RING1]] 1.39× (z +5.2, 22/47 lines), [[SUPT7L]] 1.25× (z +4.2, 17/47 lines), [[ZNF875]] 1.31× (z +3.8, 21/46 lines), [[COL4A2]] 1.21× (z +3.4, 6/23 lines), [[SUPT5H]] 1.27× (z +3.1, 29/48 lines), [[ARHGAP4]] 1.25× (z +3.1, 10/46 lines), [[MPND]] 1.31× (z +3.1, 2/42 lines), [[WNK3]] 1.24× (z +3.1, 0/18 lines), [[DDX39A]] 1.25× (z +2.8, 5/47 lines)

**0.5 µM** (131 genes, none with an alert; 12 shown): [[ZFPM1]] 1.60× (z +6.2, 27/48 lines), [[CASD1]] 1.46× (z +5.7, 35/47 lines), [[TAF3]] 1.23× (z +5.6, 25/48 lines), [[TMEM132B]] 1.60× (z +5.3, 19/39 lines), [[FAM118B]] 1.35× (z +5.2, 18/47 lines), [[GINS4]] 1.46× (z +5.1, 17/47 lines), [[NTN1]] 1.32× (z +5.0, 13/30 lines), [[LIG1]] 1.33× (z +5.0, 20/48 lines), [[FBF1]] 1.41× (z +4.9, 14/46 lines), [[DNA2]] 1.31× (z +4.9, 19/48 lines), [[CSRNP2]] 1.40× (z +4.7, 24/48 lines), [[DDB2]] 1.30× (z +4.5, 25/46 lines)

**5 µM** (4738 genes, 1,345 with an alert ⚠; the drug-dose carries ⚠ cell-cycle shift; 13 shown): [[EPHA4]] 7.16× (z +27.6, 26/29 lines; cell-cycle shift (explains ~12% here)), [[ENSG00000287292]] 16.2× (z +26.4, 29/30 lines; cell-cycle shift (explains ~0% here)), [[C2]] 11.4× (z +25.5, 42/43 lines; cell-cycle shift (explains ~6% here)), [[LINC01829]] 9.41× (z +25.2, 37/37 lines; cell-cycle shift (explains ~0% here)), [[SIAH2-AS1]] 18.6× (z +24.9, 26/26 lines; cell-cycle shift (explains ~0% here)), [[ENSG00000289156]] 9.83× (z +24.9, 31/32 lines; cell-cycle shift (explains ~0% here)), [[ENSG00000286533]] 8.80× (z +24.9, 42/43 lines; cell-cycle shift (explains ~0% here)), [[IGSF11]] 10.2× (z +24.4, 25/28 lines; cell-cycle shift (explains ~1% here)), [[ADAMTS17]] 5.61× (z +24.3, 28/29 lines; cell-cycle shift (explains ~10% here)), [[GSTCD]] ⚠ 3.33× (z +23.9, 44/47 lines; cell-cycle shift, explains ~25% of this change), [[DYRK4]] 3.66× (z +23.2, 38/44 lines; cell-cycle shift (explains ~12% here)), [[MAP7D2]] 6.88× (z +22.4, 35/40 lines; cell-cycle shift (explains ~6% here)), [[SERINC5]] 2.14× (z +22.0, 41/47 lines; cell-cycle shift (explains ~0% here))

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (2 genes, none with an alert): [[RIMOC1]] 0.793× (z -3.4, 11/48 lines), [[IGIP]] 0.760× (z -3.0, 14/46 lines)

**0.5 µM** (82 genes, none with an alert; 12 shown): [[STAC]] 0.713× (z -6.3, 10/23 lines), [[ENSG00000235609]] 0.720× (z -6.1, 23/40 lines), [[NRF1]] 0.737× (z -5.8, 29/48 lines), [[CTDSPL]] 0.744× (z -5.7, 23/43 lines), [[C1QTNF7-AS1]] 0.762× (z -5.2, 19/45 lines), [[NEK3]] 0.788× (z -4.6, 12/44 lines), [[NEURL1]] 0.601× (z -4.4, 13/39 lines), [[NBN]] 0.824× (z -4.3, 19/48 lines), [[SLC9A2]] 0.721× (z -4.3, 8/27 lines), [[CCNF]] 0.770× (z -4.3, 18/47 lines), [[SLC5A11]] 0.586× (z -4.1, 12/44 lines), [[PLK1]] 0.731× (z -4.1, 19/47 lines)

**5 µM** (2579 genes, 1,066 with an alert ⚠; the drug-dose carries ⚠ cell-cycle shift; 12 shown): [[GTF2IRD1]] 0.347× (z -23.7, 44/48 lines; cell-cycle shift (explains ~13% here)), [[CSTPP1]] 0.455× (z -19.7, 41/48 lines; cell-cycle shift (explains ~0% here)), [[SLC25A43]] 0.380× (z -19.5, 38/43 lines; cell-cycle shift (explains ~18% here)), [[DCTN4]] 0.472× (z -19.5, 47/48 lines; cell-cycle shift (explains ~10% here)), [[SPOP]] 0.468× (z -18.9, 43/48 lines; cell-cycle shift (explains ~18% here)), [[SH3PXD2B]] 0.403× (z -18.2, 39/46 lines; cell-cycle shift (explains ~0% here)), [[NBDY]] 0.433× (z -18.2, 40/47 lines; cell-cycle shift (explains ~13% here)), [[MPP3]] 0.338× (z -18.0, 41/47 lines; cell-cycle shift (explains ~7% here)), [[CLPB]] 0.410× (z -17.9, 39/47 lines; cell-cycle shift (explains ~0% here)), [[SLC27A1]] 0.349× (z -17.8, 42/47 lines; cell-cycle shift (explains ~7% here)), [[CRTC1]] 0.435× (z -17.5, 43/48 lines; cell-cycle shift (explains ~7% here)), [[SMIM7]] 0.484× (z -17.4, 40/48 lines; cell-cycle shift (explains ~9% here))

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | [[Module 194]] (+2.3), [[Module 170]] (+2.2) | — |
| 5 µM | [[Module 026]] (+12.1), [[Module 137]] (+11.8), [[Module 194]] (+9.9) | [[Module 085]] (-10.9), [[Module 017]] (-9.1), [[Module 051]] (-8.2) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | [[SNU-423 (line)]] (1.46), [[BT-474 (line)]] (1.44), [[MIA PaCa-2 (line)]] (1.44), [[H4 (line)]] (1.33) · weakest: [[NCI-H1573 (line)]] (0.423), [[SHP-77 (line)]] (0.436), [[AsPC-1 (line)]] (0.477) |
| 5 µM | [[NCI-H23 (line)]] (-10.3), [[SK-MEL-2 (line)]] (-9.7), [[RKO (line)]] (-9.6), [[A-172 (line)]] (-6.7), [[H4 (line)]] (-6.0) | [[HOP62 (line)]] (1.68), [[HS-578T (line)]] (1.58), [[H4 (line)]] (1.54), [[MIA PaCa-2 (line)]] (1.50) · weakest: [[NCI-H1573 (line)]] (0.194), [[SHP-77 (line)]] (0.310), [[HepG2_C3A (line)]] (0.515) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

⚠ This drug's own vector: vector dose flagged: cell-cycle shift. Read its neighbours with that in mind.

*378 other drugs have a vector, 121 with an alert ⚠; shown: the 8 most similar and the 4 next most similar without an alert.*

- [[Epirubicin (hydrochloride) (drug)]] (+0.96, DNA synthesis/repair inhibitor, ⚠ vector dose flagged: cell-cycle shift); [[Idarubicin (hydrochloride) (drug)]] (+0.82, DNA synthesis/repair inhibitor, ⚠ vector dose flagged: cell-cycle shift); [[Mitoxantrone (dihydrochloride) (drug)]] (+0.71, DNA synthesis/repair inhibitor); [[Orlistat (drug)]] (+0.34, unclear); [[Vemurafenib (drug)]] (+0.34, RAF inhibitor, ⚠ only 1 significant gene); [[Pimozide (drug)]] (+0.33, unclear); [[Valdecoxib (drug)]] (+0.31, Cyclooxygenase inhibitor); [[Nafamostat (mesylate) (drug)]] (+0.29, unclear, ⚠ only 3 significant genes); [[Amsacrine (drug)]] (+0.29, DNA synthesis/repair inhibitor); [[Meloxicam (drug)]] (+0.28, Cyclooxygenase inhibitor); [[Demeclocycline (drug)]] (+0.28, unclear); [[Drospirenone (drug)]] (+0.27, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 35 arrows, 35 of them with an alert ⚠; grade A 0, B 30, C 5. Shown: the 15 strongest; 20 more arrows (20 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[JUP]] | 5 µM | B | JUP activity raises the cells' numbers under Doxorubicin (hydrochloride) 5 µM (protects the cells) | lines that do not express JUP (16) vs lines expressing it (32) | the lines without JUP: 0.55× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: ELF3, SHROOM3, ENSG00000253671 |
| [[LAMA1]] | 5 µM | B | LAMA1 activity lowers the cells' numbers under Doxorubicin (hydrochloride) 5 µM (makes them more sensitive) | lines that do not express LAMA1 (31) vs lines expressing it (17) | the lines without LAMA1: 1.80× the cells of the other lines | 0.036 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LNCOG, CCL3, PHACTR1 |
| [[ELF3]] | 5 µM | B | ELF3 activity raises the cells' numbers under Doxorubicin (hydrochloride) 5 µM (protects the cells) | lines that do not express ELF3 (23) vs lines expressing it (25) | the lines without ELF3: 0.58× the cells of the other lines | 0.037 | ⚠ within organs, on part of the lines; also absent: RASSF6, GOLT1A, LAMA3 |
| [[AFF3]] | 5 µM | B | AFF3 activity lowers the cells' numbers under Doxorubicin (hydrochloride) 5 µM (makes them more sensitive) | lines that do not express AFF3 (22) vs lines expressing it (26) | the lines without AFF3: 1.61× the cells of the other lines | 0.050 | ⚠ within organs, on part of the lines; also absent: PTX3, DCLK2, SRPX |
| [[SHROOM3]] | 5 µM | B | SHROOM3 activity raises the cells' numbers under Doxorubicin (hydrochloride) 5 µM (protects the cells) | lines that do not express SHROOM3 (19) vs lines expressing it (29) | the lines without SHROOM3: 0.59× the cells of the other lines | 0.052 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: RHOV, ELF3, PLUT |
| [[LINC01226]] | 5 µM | B | LINC01226 activity raises the cells' numbers under Doxorubicin (hydrochloride) 5 µM (protects the cells) | lines that do not express LINC01226 (16) vs lines expressing it (32) | the lines without LINC01226: 0.59× the cells of the other lines | 0.052 | ⚠ within organs, on part of the lines; also absent: LASTR, TRIM29, ENSG00000287003; maybe low, not absent |
| [[TSPAN13]] | 5 µM | B | TSPAN13 activity raises the cells' numbers under Doxorubicin (hydrochloride) 5 µM (protects the cells) | lines that do not express TSPAN13 (13) vs lines expressing it (35) | the lines without TSPAN13: 0.59× the cells of the other lines | 0.052 | ⚠ within organs, on part of the lines; also absent: JUP, MPZL3, MYO5C |
| [[C11orf52]] | 5 µM | B | C11orf52 activity raises the cells' numbers under Doxorubicin (hydrochloride) 5 µM (protects the cells) | lines that do not express C11orf52 (23) vs lines expressing it (25) | the lines without C11orf52: 0.59× the cells of the other lines | 0.056 | ⚠ within organs, on part of the lines; also absent: TNNT2, MPZL3, RNF39 |
| [[PDLIM1]] | 5 µM | B | PDLIM1 activity raises the cells' numbers under Doxorubicin (hydrochloride) 5 µM (protects the cells) | lines that do not express PDLIM1 (11) vs lines expressing it (37) | the lines without PDLIM1: 0.59× the cells of the other lines | 0.069 | ⚠ within organs, on part of the lines; also absent: PCED1B, GPR39, ATP8B1 |
| [[TMEM45B]] | 5 µM | B | TMEM45B activity raises the cells' numbers under Doxorubicin (hydrochloride) 5 µM (protects the cells) | lines that do not express TMEM45B (32) vs lines expressing it (16) | the lines without TMEM45B: 0.58× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TRIM15, CDH1, ENSG00000267881 |
| [[BNC2]] | 5 µM | B | BNC2 activity lowers the cells' numbers under Doxorubicin (hydrochloride) 5 µM (makes them more sensitive) | lines that do not express BNC2 (21) vs lines expressing it (27) | the lines without BNC2: 1.58× the cells of the other lines | 0.073 | ⚠ within organs, on part of the lines; also absent: LINC03041, DPY19L2, RNF182 |
| [[TNNT2]] | 5 µM | B | TNNT2 activity raises the cells' numbers under Doxorubicin (hydrochloride) 5 µM (protects the cells) | lines that do not express TNNT2 (29) vs lines expressing it (19) | the lines without TNNT2: 0.61× the cells of the other lines | 0.075 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, ATP2C2, ST14 |
| [[ENSG00000287003]] | 5 µM | B | ENSG00000287003 activity raises the cells' numbers under Doxorubicin (hydrochloride) 5 µM (protects the cells) | lines that do not express ENSG00000287003 (20) vs lines expressing it (28) | the lines without ENSG00000287003: 0.64× the cells of the other lines | 0.075 | ⚠ within organs, on part of the lines; also absent: TMEM154, ALOX5, RASSF6 |
| [[ENSG00000251584]] | 5 µM | B | ENSG00000251584 activity raises the cells' numbers under Doxorubicin (hydrochloride) 5 µM (protects the cells) | lines that do not express ENSG00000251584 (28) vs lines expressing it (20) | the lines without ENSG00000251584: 0.62× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; also absent: HPGD, HNF1A-AS1, ENSG00000267881 |
| [[RNF39]] | 5 µM | B | RNF39 activity raises the cells' numbers under Doxorubicin (hydrochloride) 5 µM (protects the cells) | lines that do not express RNF39 (30) vs lines expressing it (18) | the lines without RNF39: 0.60× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: CDH1, TNNT2, TRIM15; maybe low, not absent |

### Its targets: what acting on them probably does

*Drug-target arrows of the compound classes it belongs to (compounds sharing a listed target and mechanism; one molecule counts once, under all its names): the target → a gene whose level those compounds move. A row that names several targets is one test: the compounds share them all, and any of them could be the cause. 4,393 arrows, 4,393 of them with an alert ⚠; grade A 0, B 4,393, C 0. Shown: the 15 strongest; 4,378 more arrows (4,378 of them with an alert ⚠) not shown.*

| Its target | Gene it moves | This drug | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|---|
| [[TOP2A]] | [[G2E3]] | moves it that way too | B | TOP2A activity raises G2E3's level | compounds that target TOP2A: 5 of 5 lower it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 2.5% of all compounds | 0.004 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[TOP2A]] | [[RABL2B]] | moves it that way too | B | TOP2A activity lowers RABL2B's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 2.8% of all compounds | 0.004 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[TOP2A]] | [[RASSF8-AS1]] | moves it that way too | B | TOP2A activity lowers RASSF8-AS1's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 2.8% of all compounds | 0.004 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[TOP2A]] | [[ENSG00000285667]] | moves it that way too | B | TOP2A activity lowers ENSG00000285667's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 3.1% of all compounds | 0.004 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[TOP2A]] | [[LRRIQ3]] | moves it that way too | B | TOP2A activity lowers LRRIQ3's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 3.1% of all compounds | 0.004 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[TOP2A]] | [[BAX]] | moves it that way too | B | TOP2A activity lowers BAX's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 3.4% of all compounds | 0.004 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[TOP2A]] | [[CIBAR1-DT]] | moves it that way too | B | TOP2A activity lowers CIBAR1-DT's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 3.4% of all compounds | 0.004 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[TOP2A]] | [[ENSG00000287400]] | moves it that way too | B | TOP2A activity lowers ENSG00000287400's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 3.4% of all compounds | 0.004 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[TOP2A]] | [[MIDEAS]] | moves it that way too | B | TOP2A activity raises MIDEAS's level | compounds that target TOP2A: 5 of 5 lower it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 3.4% of all compounds | 0.004 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[TOP2A]] | [[TARID]] | moves it that way too | B | TOP2A activity lowers TARID's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 3.4% of all compounds | 0.004 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[TOP2A]] | [[ZNF665]] | moves it that way too | B | TOP2A activity lowers ZNF665's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 3.4% of all compounds | 0.004 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[TOP2A]] | [[AK1]] | moves it that way too | B | TOP2A activity lowers AK1's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 3.6% of all compounds | 0.004 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[TOP2A]] | [[CAMKK1]] | moves it that way too | B | TOP2A activity raises CAMKK1's level | compounds that target TOP2A: 5 of 5 lower it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 3.6% of all compounds | 0.004 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[TOP2A]] | [[ENSG00000228566]] | moves it that way too | B | TOP2A activity lowers ENSG00000228566's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 3.6% of all compounds | 0.004 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[TOP2A]] | [[FCGBP]] | moves it that way too | B | TOP2A activity lowers FCGBP's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 3.6% of all compounds | 0.004 | ⚠ off-target possible; 5 compounds; artifact flags |

## Data

- `tables/drugs.parquet` — drug == "Doxorubicin (hydrochloride)"
- `tables/drugdoses.parquet` — dd in 377, 378, 379
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
