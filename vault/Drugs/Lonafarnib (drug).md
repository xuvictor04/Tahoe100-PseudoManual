---
drug: "Lonafarnib"
type: "drug"
salt_base: "Lonafarnib"
targets: "HRAS, KRAS, NRAS"
moa_fine: "RAS inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 4176
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Lonafarnib

*RAS inhibitor (inhibitor/antagonist) · targets: HRAS, KRAS, NRAS · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 10 / 41 / 4176; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.05 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): -0.36 / 0.04.
> Flags by dose: - / noisy plate (z scaled) / toxic; noisy plate (z scaled). ⚠ 5 µM: toxic (artifact flags: its changes there are shown with an alert, not left out).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 01]]:B1 | 2 / 8 | — | +0.49 | +1.6/+0.6/+0.6 | — |
| 0.5 µM | [[Plate 02]]:B1 | 18 / 23 | — | +0.64 | -0.0/-0.3/-0.5 | noisy plate (z scaled) |
| 5 µM | [[Plate 03]]:B1 | 2,995 / 1,181 | — | -1.97 | +1.0/+0.2/+3.0 | ⚠ toxic · noisy plate (z scaled) |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (2 genes, none with an alert): [[OSGEP]] 1.20× (z +3.0, 3/48 lines), [[TM4SF1-AS1]] 1.37× (z +3.0, 3/33 lines)

**0.5 µM** (18 genes, none with an alert; 12 shown): [[ENSG00000232884]] 1.91× (z +4.7, 11/35 lines), [[SAMSN1]] 1.96× (z +4.2, 8/39 lines), [[LVRN]] 1.65× (z +3.6, 10/45 lines), [[ENSG00000235609]] 1.31× (z +3.6, 15/40 lines), [[ESYT2]] 1.33× (z +3.2, 27/48 lines), [[PDK1]] 1.50× (z +3.1, 29/48 lines), [[CHSY1]] 1.25× (z +3.1, 12/47 lines), [[ENSG00000229021]] 1.48× (z +3.1, 2/47 lines), [[ENSG00000274322]] 1.39× (z +3.1, 12/48 lines), [[MTFR2]] 1.39× (z +3.1, 3/48 lines), [[AGPAT5]] 1.24× (z +3.0, 10/48 lines), [[WDR49]] 1.61× (z +3.0, 8/45 lines)

**5 µM** (2995 genes, 2,995 with an alert ⚠; the drug-dose carries ⚠ toxic; 12 shown): [[LINC00536]] ⚠ 18.4× (z +14.7, 5/7 lines), [[ZC3H3]] ⚠ 4.52× (z +11.1, 29/31 lines), [[LINC01208]] ⚠ 5.44× (z +10.4, 10/14 lines), [[WDR43]] ⚠ 3.39× (z +10.2, 37/38 lines), [[ENSG00000232884]] ⚠ 6.51× (z +10.0, 7/7 lines), [[SAMSN1]] ⚠ 8.87× (z +10.0, 6/6 lines), [[ELAVL1]] ⚠ 2.03× (z +9.7, 29/36 lines), [[ENSG00000259805]] ⚠ 3.45× (z +9.5, 15/20 lines), [[NFKB1]] ⚠ 2.83× (z +9.3, 35/38 lines), [[SERPINB9]] ⚠ 3.22× (z +9.2, 13/19 lines), [[BHLHE40-AS1]] ⚠ 2.88× (z +9.0, 8/20 lines), [[SNX5]] ⚠ 2.03× (z +9.0, 32/37 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (8 genes, none with an alert): [[ENSG00000260342]] 0.505× (z -5.0, 15/44 lines), [[ENSG00000288000]] 0.611× (z -4.0, 34/48 lines), [[ENSG00000289405]] 0.703× (z -3.5, 15/47 lines), [[ENSG00000258864]] 0.680× (z -3.5, 2/44 lines), [[TLL2]] 0.693× (z -3.4, 6/44 lines), [[HCLS1]] 0.628× (z -3.4, 4/44 lines), [[SLC16A14]] 0.756× (z -3.1, 5/31 lines), [[MFSD2A]] 0.716× (z -3.0, 9/44 lines)

**0.5 µM** (23 genes, none with an alert; 12 shown): [[GRHL2]] 0.634× (z -3.8, 0/14 lines), [[GPRIN3]] 0.590× (z -3.5, 0/13 lines), [[EPS8L3]] 0.612× (z -3.4, 0/13 lines), [[TMEM45B]] 0.671× (z -3.2, 0/16 lines), [[ENSG00000287352]] 0.651× (z -3.2, 0/15 lines), [[ENSG00000257869]] 0.642× (z -3.1, 0/12 lines), [[USP9Y]] 0.766× (z -3.1, 0/18 lines), [[PRKY]] 0.735× (z -3.1, 0/18 lines), [[LINC02315]] 0.623× (z -3.0, 0/17 lines), [[TECPR1]] 0.759× (z -3.0, 1/48 lines), [[PTGES]] 0.664× (z -3.0, 3/31 lines), [[POF1B]] 0.691× (z -3.0, 0/14 lines)

**5 µM** (1181 genes, 1,181 with an alert ⚠; the drug-dose carries ⚠ toxic; 12 shown): [[ZC3H6]] ⚠ 0.422× (z -9.9, 26/36 lines), [[KAT6B]] ⚠ 0.473× (z -9.9, 34/38 lines), [[PPARA]] ⚠ 0.431× (z -9.7, 25/36 lines), [[MAGI3]] ⚠ 0.528× (z -9.3, 30/37 lines), [[TRIM38]] ⚠ 0.375× (z -9.3, 25/33 lines), [[NIHCOLE]] ⚠ 0.324× (z -9.1, 15/18 lines), [[NBEAL1]] ⚠ 0.511× (z -8.8, 33/38 lines), [[ZCCHC24]] ⚠ 0.420× (z -8.8, 20/29 lines), [[RSF1]] ⚠ 0.633× (z -8.7, 30/38 lines), [[NEAT1]] ⚠ 0.408× (z -8.6, 35/37 lines), [[PPP1R21]] ⚠ 0.523× (z -8.5, 28/38 lines), [[CFDP1]] ⚠ 0.617× (z -8.5, 33/38 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | [[Module 020]] (+2.0) | — |
| 5 µM | [[Module 168]] (+4.8), [[Module 182]] (+4.3), [[Module 083]] (+3.7) | [[Module 225]] (-4.2), [[Module 170]] (-4.0), [[Module 200]] (-3.1) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | [[HOP62 (line)]] (1.49), [[NCI-H1792 (line)]] (1.46), [[hTERT-HPNE (line)]] (1.41), [[SNU-423 (line)]] (1.41) · weakest: [[SW1417 (line)]] (0.546), [[A549 (line)]] (0.651), [[SHP-77 (line)]] (0.676) |
| 5 µM | [[SW480 (line)]] (-11.3), [[KATO III (line)]] (-10.1), [[RKO (line)]] (-9.6), [[HT-29 (line)]] (-8.9), [[Panc 03.27 (line)]] (-8.8) | [[Panc 03.27 (line)]] (1.96), [[BT-474 (line)]] (1.73), [[HT-29 (line)]] (1.50), [[AsPC-1 (line)]] (1.47) · weakest: [[SHP-77 (line)]] (0.241), [[CHP-212 (line)]] (0.454), [[NCI-H460 (line)]] (0.528) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

⚠ This drug's own vector: vector dose flagged: toxic. Read its neighbours with that in mind.

*378 other drugs have a vector, 121 with an alert ⚠; shown: the 8 most similar and the 3 next most similar without an alert.*

- [[Dinaciclib (drug)]] (+0.71, CDK inhibitor, ⚠ vector dose flagged: toxic; transcription drop; cell-cycle shift); [[Orlistat (drug)]] (+0.63, unclear); [[Imiquimod (maleate) (drug)]] (+0.56, unclear); [[Monocrotaline (drug)]] (+0.52, unclear); [[Pyridoxine (drug)]] (+0.51, unclear); [[Ataluren (drug)]] (+0.51, unclear, ⚠ only 7 significant genes); [[Oxaprozin (drug)]] (+0.50, Cyclooxygenase inhibitor); [[AZD2858 (drug)]] (+0.50, GSK3 inhibitor, ⚠ vector dose flagged: toxic); [[Valdecoxib (drug)]] (+0.49, Cyclooxygenase inhibitor); [[Drospirenone (drug)]] (+0.48, unclear); [[Isocorydine (drug)]] (+0.48, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 55 arrows, 55 of them with an alert ⚠; grade A 0, B 40, C 15. Shown: the 15 strongest; 40 more arrows (40 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[ATP1B1]] | 0.05 µM | B | ATP1B1 activity lowers the cells' numbers under Lonafarnib 0.05 µM (makes them more sensitive) | lines that do not express ATP1B1 (8) vs lines expressing it (40) | the lines without ATP1B1: 1.30× the cells of the other lines | 0.027 | ⚠ within organs, on part of the lines; also absent: PYROXD2, IL15, IER3; maybe low, not absent |
| [[AQP3]] | 0.05 µM | B | AQP3 activity lowers the cells' numbers under Lonafarnib 0.05 µM (makes them more sensitive) | lines that do not express AQP3 (19) vs lines expressing it (29) | the lines without AQP3: 1.26× the cells of the other lines | 0.036 | ⚠ within organs, on part of the lines; also absent: ABCC3, ELF3, CD24; maybe low, not absent |
| [[MSRB3-AS1]] | 0.05 µM | B | MSRB3-AS1 activity raises the cells' numbers under Lonafarnib 0.05 µM (protects the cells) | lines that do not express MSRB3-AS1 (42) vs lines expressing it (6) | the lines without MSRB3-AS1: 0.68× the cells of the other lines | 0.038 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: GCG, LINC01205, COX7B2 |
| [[FBXW10B]] | 0.05 µM | B | FBXW10B activity lowers the cells' numbers under Lonafarnib 0.05 µM (makes them more sensitive) | lines that do not express FBXW10B (11) vs lines expressing it (37) | the lines without FBXW10B: 1.27× the cells of the other lines | 0.048 | ⚠ within organs, on part of the lines; also absent: ENSG00000251537, NHS, BDKRB2; maybe low, not absent |
| [[ALDH3B1]] | 0.05 µM | B | ALDH3B1 activity lowers the cells' numbers under Lonafarnib 0.05 µM (makes them more sensitive) | lines that do not express ALDH3B1 (9) vs lines expressing it (39) | the lines without ALDH3B1: 1.27× the cells of the other lines | 0.056 | ⚠ within organs, on part of the lines; also absent: NIBAN2, IER3, FOSL1; maybe low, not absent |
| [[APOL3]] | 0.5 µM | B | APOL3 activity raises the cells' numbers under Lonafarnib 0.5 µM (protects the cells) | lines that do not express APOL3 (14) vs lines expressing it (34) | the lines without APOL3: 0.85× the cells of the other lines | 0.056 | ⚠ within organs, on part of the lines; also absent: SAMD9L, APOL1, GBP4 |
| [[SPTLC3]] | 0.05 µM | B | SPTLC3 activity lowers the cells' numbers under Lonafarnib 0.05 µM (makes them more sensitive) | lines that do not express SPTLC3 (16) vs lines expressing it (32) | the lines without SPTLC3: 1.20× the cells of the other lines | 0.058 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1, CXCL3, PTPRB; maybe low, not absent |
| [[ENSG00000258919]] | 0.5 µM | B | ENSG00000258919 activity raises the cells' numbers under Lonafarnib 0.5 µM (protects the cells) | lines that do not express ENSG00000258919 (23) vs lines expressing it (25) | the lines without ENSG00000258919: 0.85× the cells of the other lines | 0.062 | ⚠ within organs, on part of the lines; also absent: LINC02320, ENSG00000266088, DIO3OS |
| [[LGALS3BP]] | 0.05 µM | B | LGALS3BP activity lowers the cells' numbers under Lonafarnib 0.05 µM (makes them more sensitive) | lines that do not express LGALS3BP (7) vs lines expressing it (41) | the lines without LGALS3BP: 1.33× the cells of the other lines | 0.066 | ⚠ within organs, on part of the lines; also absent: LGALS3, KLF4, APOL6 |
| [[ANKS1B]] | 5 µM | B | ANKS1B activity raises the cells' numbers under Lonafarnib 5 µM (protects the cells) | lines that do not express ANKS1B (18) vs lines expressing it (30) | the lines without ANKS1B: 0.25× the cells of the other lines | 0.068 | ⚠ within organs, on part of the lines; also absent: LHX2, CECR2, HS6ST3 |
| [[SLC2A9]] | 0.05 µM | B | SLC2A9 activity lowers the cells' numbers under Lonafarnib 0.05 µM (makes them more sensitive) | lines that do not express SLC2A9 (6) vs lines expressing it (42) | the lines without SLC2A9: 1.41× the cells of the other lines | 0.068 | ⚠ within organs, on part of the lines; also absent: VDR, SEMA4G, TBC1D8B; maybe low, not absent |
| [[GABRE]] | 0.05 µM | B | GABRE activity lowers the cells' numbers under Lonafarnib 0.05 µM (makes them more sensitive) | lines that do not express GABRE (20) vs lines expressing it (28) | the lines without GABRE: 1.24× the cells of the other lines | 0.068 | ⚠ within organs, on part of the lines; also absent: IL2RG, ACSL5, PI3 |
| [[IL15]] | 0.05 µM | B | IL15 activity lowers the cells' numbers under Lonafarnib 0.05 µM (makes them more sensitive) | lines that do not express IL15 (10) vs lines expressing it (38) | the lines without IL15: 1.30× the cells of the other lines | 0.070 | ⚠ within organs, on part of the lines; also absent: TGFBR2, ITGA3, PSORS1C1; maybe low, not absent |
| [[PYROXD2]] | 0.05 µM | B | PYROXD2 activity lowers the cells' numbers under Lonafarnib 0.05 µM (makes them more sensitive) | lines that do not express PYROXD2 (7) vs lines expressing it (41) | the lines without PYROXD2: 1.28× the cells of the other lines | 0.071 | ⚠ within organs, on part of the lines; also absent: ATP1B1, SMARCA2, ZMIZ1; maybe low, not absent |
| [[ENSG00000251537]] | 0.05 µM | B | ENSG00000251537 activity lowers the cells' numbers under Lonafarnib 0.05 µM (makes them more sensitive) | lines that do not express ENSG00000251537 (9) vs lines expressing it (39) | the lines without ENSG00000251537: 1.28× the cells of the other lines | 0.071 | ⚠ within organs, on part of the lines; also absent: FBXW10B, PCED1B, NHS; maybe low, not absent |

### Its targets: what acting on them probably does

*Drug-target arrows of the compound classes it belongs to (compounds sharing a listed target and mechanism; one molecule counts once, under all its names): the target → a gene whose level those compounds move. A row that names several targets is one test: the compounds share them all, and any of them could be the cause. 1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Its target | Gene it moves | This drug | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|---|
| [[KRAS]] | [[MFSD2A]] | moves it that way too | B | KRAS activity raises MFSD2A's level | compounds that target KRAS: 3 of 4 lower it (BI-3406, Lonafarnib, RMC-6236) | 75% of the class's compounds vs 3.9% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds |

## Data

- `tables/drugs.parquet` — drug == "Lonafarnib"
- `tables/drugdoses.parquet` — dd in 627, 628, 629
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
