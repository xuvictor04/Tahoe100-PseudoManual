---
drug: "Pyridoxine (hydrochloride)"
type: "drug"
salt_base: "Pyridoxine"
targets: ""
moa_fine: "unclear"
moa_broad: "unclear"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "0.05"
max_sig_genes: 152
tags: ["drug", "moa/unclear"]
generated_by: "tahoemap"
---

# Pyridoxine (hydrochloride)

*unclear (unclear) · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 152 / 32 / 118; best dose 0.05 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.05 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.62 / 0.63.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 04]]:H1 | 52 / 100 | — | +0.16 | +2.4/-0.5/-0.7 | — |
| 0.5 µM | [[Plate 05]]:H1 | 2 / 30 | — | +0.92 | +0.8/-0.8/+0.0 | — |
| 5 µM | [[Plate 14]]:H1 | 24 / 94 | 0.871 | -0.14 | +0.2/-2.5/-0.4 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (52 genes, none with an alert; 12 shown): [[MCM6]] 1.34× (z +4.3, 17/46 lines), [[ALG10B]] 1.45× (z +4.3, 6/45 lines), [[CAPN1]] 1.23× (z +4.0, 14/48 lines), [[WDR76]] 1.31× (z +4.0, 10/46 lines), [[SCARB2]] 1.21× (z +3.8, 23/48 lines), [[PRKDC]] 1.25× (z +3.8, 27/48 lines), [[TUBGCP3]] 1.26× (z +3.8, 20/48 lines), [[DPYSL3]] 1.26× (z +3.7, 10/28 lines), [[CARMIL1]] 1.23× (z +3.7, 18/40 lines), [[DAG1]] 1.24× (z +3.7, 18/48 lines), [[FAT1]] 1.30× (z +3.7, 28/45 lines), [[RIPK4]] 1.40× (z +3.7, 14/35 lines)

**0.5 µM** (2 genes, none with an alert): [[TMEM123]] 1.21× (z +3.6, 26/49 lines), [[DPYSL3]] 1.23× (z +3.3, 5/29 lines)

**5 µM** (24 genes, none with an alert; 12 shown): [[MCM6]] 1.24× (z +4.4, 20/46 lines), [[MINDY1]] 1.28× (z +4.2, 8/45 lines), [[ZMYM3]] 1.31× (z +4.1, 18/48 lines), [[RIPK4]] 1.29× (z +3.9, 18/35 lines), [[ANKRD30BL]] 1.61× (z +3.9, 17/46 lines), [[WDR76]] 1.20× (z +3.8, 12/46 lines), [[ENSG00000266953]] 1.40× (z +3.8, 16/47 lines), [[LOXL1-AS1]] 1.22× (z +3.5, 3/31 lines), [[MICU3]] 1.22× (z +3.5, 8/29 lines), [[RAB3D]] 1.20× (z +3.5, 13/46 lines), [[STAMBPL1]] 1.21× (z +3.4, 10/42 lines), [[ALG10B]] 1.24× (z +3.4, 5/46 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (100 genes, none with an alert; 12 shown): [[SNX31]] 0.505× (z -4.9, 15/46 lines), [[GPC5]] 0.573× (z -4.7, 26/40 lines), [[SLC15A2]] 0.628× (z -4.5, 17/46 lines), [[ECT2L]] 0.649× (z -4.5, 11/46 lines), [[HM13]] 0.796× (z -4.2, 31/48 lines), [[ENSG00000255139]] 0.745× (z -4.2, 15/48 lines), [[WDR49]] 0.633× (z -4.2, 20/45 lines), [[MOGAT3]] 0.506× (z -4.1, 6/16 lines), [[GOLPH3L]] 0.790× (z -4.1, 26/47 lines), [[RUBCNL]] 0.632× (z -4.1, 2/17 lines), [[MTRFR]] 0.790× (z -4.1, 15/48 lines), [[ACBD3]] 0.783× (z -4.0, 26/48 lines)

**0.5 µM** (30 genes, none with an alert; 12 shown): [[ENSG00000225647]] 0.465× (z -4.1, 11/34 lines), [[GPC5]] 0.615× (z -4.1, 17/41 lines), [[DYSF]] 0.746× (z -4.0, 4/36 lines), [[MSH4]] 0.671× (z -4.0, 12/47 lines), [[ENSG00000258101]] 0.710× (z -3.8, 3/46 lines), [[GBX1]] 0.653× (z -3.6, 8/26 lines), [[KNSTRN]] 0.801× (z -3.6, 5/48 lines), [[MYRFL]] 0.703× (z -3.6, 7/34 lines), [[CTU1]] 0.738× (z -3.5, 1/45 lines), [[HSDL2-AS1]] 0.793× (z -3.5, 7/48 lines), [[ENSG00000273763]] 0.672× (z -3.4, 9/48 lines), [[ENSG00000240553]] 0.803× (z -3.4, 8/48 lines)

**5 µM** (94 genes, none with an alert; 12 shown): [[UNC119B]] 0.751× (z -6.0, 25/48 lines), [[GPC5]] 0.642× (z -5.3, 28/40 lines), [[ECT2L]] 0.709× (z -5.0, 17/47 lines), [[LNP1]] 0.753× (z -4.8, 8/47 lines), [[ENSG00000236255]] 0.780× (z -4.5, 21/48 lines), [[WDR49]] 0.707× (z -4.5, 24/45 lines), [[ENSG00000259316]] 0.763× (z -4.4, 10/47 lines), [[POLN]] 0.782× (z -4.4, 23/48 lines), [[HVCN1]] 0.712× (z -4.3, 6/46 lines), [[OSER1-DT]] 0.788× (z -4.3, 9/48 lines), [[ENSG00000240553]] 0.822× (z -4.3, 15/48 lines), [[DMGDH]] 0.707× (z -4.2, 14/40 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | [[Module 006]] (+3.2), [[Module 025]] (+2.8), [[Module 029]] (+2.5) | [[Module 041]] (-3.1), [[Module 043]] (-2.9), [[Module 024]] (-2.7) |
| 0.5 µM | [[Module 029]] (+2.2), [[Module 025]] (+2.1) | [[Module 002]] (-2.1) |
| 5 µM | [[Module 006]] (+2.5), [[Module 029]] (+2.2), [[Module 025]] (+2.1) | [[Module 041]] (-2.6) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | [[HEC-1-A (line)]] (-3.3) | [[NCI-H1573 (line)]] (1.47), [[SW 1088 (line)]] (1.42), [[H4 (line)]] (1.41), [[COLO 205 (line)]] (1.32) · weakest: [[NCI-H2347 (line)]] (0.458), [[AsPC-1 (line)]] (0.655), [[BT-474 (line)]] (0.671) |
| 0.5 µM | — | [[SW 1271 (line)]] (1.90), [[AN3 CA (line)]] (1.73), [[Hs 766T (line)]] (1.67), [[SW 1088 (line)]] (1.55) · weakest: [[NCI-H2122 (line)]] (0.475), [[NCI-H2347 (line)]] (0.544), [[SW 900 (line)]] (0.549) |
| 5 µM | [[PANC-1 (line)]] (-3.3) | [[SW 1088 (line)]] (1.54), [[NCI-H1573 (line)]] (1.44), [[COLO 205 (line)]] (1.36), [[H4 (line)]] (1.32) · weakest: [[NCI-H661 (line)]] (0.633), [[NCI-H2347 (line)]] (0.642), [[A498 (line)]] (0.716) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 3 next most similar without an alert.*

- [[Trifluridine (drug)]] (+0.80, DNA synthesis/repair inhibitor, ⚠ vector dose flagged: cell-cycle shift); [[Adenine (drug)]] (+0.78, unclear); [[Balsalazide (sodium hydrate) (drug)]] (+0.76, JAK/STAT inhibitor, ⚠ only 9 significant genes); [[Folic acid (drug)]] (+0.75, unclear); [[Retinoic acid (drug)]] (+0.75, Retinoic receptor agonist); [[Megestrol (drug)]] (+0.72, unclear, ⚠ vector dose flagged: cell-cycle shift); [[Busulfan (drug)]] (+0.72, DNA synthesis/repair inhibitor); [[MK-8353 (drug)]] (+0.72, Other MAPK inhibitor); [[Palmatine (chloride) (drug)]] (+0.71, unclear); [[Rutin (trihydrate) (drug)]] (+0.68, unclear); [[Larotrectinib (drug)]] (+0.68, Other TK inhibitor)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 19 arrows, 19 of them with an alert ⚠; grade A 0, B 15, C 4. Shown: the 15 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[MTMR7]] | 0.5 µM | B | MTMR7 activity raises the cells' numbers under Pyridoxine (hydrochloride) 0.5 µM (protects the cells) | lines that do not express MTMR7 (16) vs lines expressing it (32) | the lines without MTMR7: 0.86× the cells of the other lines | 0.041 | ⚠ within organs, on part of the lines; also absent: GAP43, NRXN1, LOXL3; maybe low, not absent |
| [[MTMR7]] | 5 µM | B | MTMR7 activity raises the cells' numbers under Pyridoxine (hydrochloride) 5 µM (protects the cells) | lines that do not express MTMR7 (16) vs lines expressing it (32) | the lines without MTMR7: 0.87× the cells of the other lines | 0.047 | ⚠ within organs, on part of the lines; also absent: GAP43, NRXN1, LOXL3; maybe low, not absent |
| [[GBP2]] | 5 µM | B | GBP2 activity lowers the cells' numbers under Pyridoxine (hydrochloride) 5 µM (makes them more sensitive) | lines that do not express GBP2 (13) vs lines expressing it (35) | the lines without GBP2: 1.18× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; also absent: GBP1, ITGA3, SH3TC1 |
| [[AKR1E2]] | 0.5 µM | B | AKR1E2 activity lowers the cells' numbers under Pyridoxine (hydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express AKR1E2 (19) vs lines expressing it (29) | the lines without AKR1E2: 1.13× the cells of the other lines | 0.084 | ⚠ within organs, on part of the lines; also absent: FLNC, AFAP1L1, CACNA2D1 |
| [[LEF1-AS1]] | 5 µM | B | LEF1-AS1 activity raises the cells' numbers under Pyridoxine (hydrochloride) 5 µM (protects the cells) | lines that do not express LEF1-AS1 (33) vs lines expressing it (15) | the lines without LEF1-AS1: 0.89× the cells of the other lines | 0.086 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: COL19A1, ENSG00000226043, DCT; maybe low, not absent |
| [[AFAP1L2]] | 0.5 µM | B | AFAP1L2 activity lowers the cells' numbers under Pyridoxine (hydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express AFAP1L2 (27) vs lines expressing it (21) | the lines without AFAP1L2: 1.10× the cells of the other lines | 0.086 | ⚠ within organs, on part of the lines; also absent: LY75, ENSG00000235726, SHH |
| [[ENSG00000251294]] | 0.5 µM | B | ENSG00000251294 activity raises the cells' numbers under Pyridoxine (hydrochloride) 0.5 µM (protects the cells) | lines that do not express ENSG00000251294 (23) vs lines expressing it (25) | the lines without ENSG00000251294: 0.90× the cells of the other lines | 0.087 | ⚠ within organs, on part of the lines; also absent: VIPR2, OR3A2, RALYL; maybe low, not absent |
| [[IFIT2]] | 5 µM | B | IFIT2 activity lowers the cells' numbers under Pyridoxine (hydrochloride) 5 µM (makes them more sensitive) | lines that do not express IFIT2 (8) vs lines expressing it (40) | the lines without IFIT2: 1.17× the cells of the other lines | 0.093 | ⚠ within organs, on part of the lines; also absent: IFIT3, ENSG00000235609, TRIM38 |
| [[FGD4]] | 0.05 µM | B | FGD4 activity lowers the cells' numbers under Pyridoxine (hydrochloride) 0.05 µM (makes them more sensitive) | lines that do not express FGD4 (10) vs lines expressing it (38) | the lines without FGD4: 1.09× the cells of the other lines | 0.093 | ⚠ within organs, on part of the lines; also absent: PARD6B, CARD10, VAMP8; maybe low, not absent |
| [[CRYBG1]] | 5 µM | B | CRYBG1 activity lowers the cells' numbers under Pyridoxine (hydrochloride) 5 µM (makes them more sensitive) | lines that do not express CRYBG1 (18) vs lines expressing it (30) | the lines without CRYBG1: 1.13× the cells of the other lines | 0.094 | ⚠ within organs, on part of the lines; also absent: TSPOAP1, MPZL3, LNX1 |
| [[NXPH4]] | 0.5 µM | B | NXPH4 activity raises the cells' numbers under Pyridoxine (hydrochloride) 0.5 µM (protects the cells) | lines that do not express NXPH4 (13) vs lines expressing it (35) | the lines without NXPH4: 0.86× the cells of the other lines | 0.097 | ⚠ within organs, on part of the lines; also absent: LINC01234; maybe low, not absent |
| [[FGD4]] | 0.5 µM | B | FGD4 activity lowers the cells' numbers under Pyridoxine (hydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express FGD4 (10) vs lines expressing it (38) | the lines without FGD4: 1.12× the cells of the other lines | 0.098 | ⚠ within organs, on part of the lines; also absent: PARD6B, CARD10, VAMP8; maybe low, not absent |
| [[TNFSF10]] | 0.5 µM | B | TNFSF10 activity lowers the cells' numbers under Pyridoxine (hydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express TNFSF10 (24) vs lines expressing it (24) | the lines without TNFSF10: 1.11× the cells of the other lines | 0.098 | ⚠ within organs, on part of the lines; also absent: PLAAT4, TMEM92, LY75 |
| [[CDKN1C]] | 0.05 µM | B | CDKN1C activity lowers the cells' numbers under Pyridoxine (hydrochloride) 0.05 µM (makes them more sensitive) | lines that do not express CDKN1C (8) vs lines expressing it (40) | the lines without CDKN1C: 1.15× the cells of the other lines | 0.099 | ⚠ within organs, on part of the lines; also absent: MAP3K9, CARD10, TESMIN; maybe low, not absent |
| [[CDKN1C]] | 0.5 µM | B | CDKN1C activity lowers the cells' numbers under Pyridoxine (hydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express CDKN1C (8) vs lines expressing it (40) | the lines without CDKN1C: 1.12× the cells of the other lines | 0.0995 | ⚠ within organs, on part of the lines; also absent: MAP3K9, CARD10, TESMIN; maybe low, not absent |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Pyridoxine (hydrochloride)"
- `tables/drugdoses.parquet` — dd in 851, 852, 853
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
