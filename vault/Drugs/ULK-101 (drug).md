---
drug: "ULK-101"
type: "drug"
salt_base: "ULK-101"
targets: "ULK1, ULK2"
moa_fine: "unclear"
moa_broad: "inhibitor/antagonist"
approved: "no"
doses: ["0.05", "0.5", "5"]
best_dose: "0.05"
max_sig_genes: 123
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# ULK-101

*unclear (inhibitor/antagonist) · targets: ULK1, ULK2 · approved: no*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 123 / 8 / 2; best dose 0.05 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): low dose only (noise?).
> Signature similarity between consecutive doses (low–mid / mid–high): -0.08 / 0.17.
> Flags by dose: - / plate-row cell shift; noisy plate (z scaled) / noisy plate (z scaled).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 01]]:E10 | 64 / 59 | — | -0.18 | -3.4/-3.2/-1.9 | — |
| 0.5 µM | [[Plate 02]]:E10 | 7 / 1 | — | -0.89 | -0.3/+0.4/+0.5 | plate-row cell shift; noisy plate (z scaled) |
| 5 µM | [[Plate 03]]:E10 | 2 / 0 | — | -0.56 | -0.7/-0.6/-1.1 | noisy plate (z scaled) |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (64 genes, none with an alert; 12 shown): [[ENSG00000290890]] 1.39× (z +4.8, 21/48 lines), [[ING4]] 1.31× (z +4.7, 16/47 lines), [[GAB2]] 1.30× (z +4.7, 23/47 lines), [[KLHL24]] 1.34× (z +4.4, 32/49 lines), [[ZSWIM4]] 1.29× (z +4.3, 19/49 lines), [[RRAGC-DT]] 1.43× (z +4.1, 25/48 lines), [[ZNF83]] 1.21× (z +4.1, 16/39 lines), [[WASHC2A]] 1.23× (z +4.1, 12/48 lines), [[CREBRF]] 1.31× (z +4.1, 30/49 lines), [[OSBP2]] 1.22× (z +3.9, 15/47 lines), [[SNX8]] 1.34× (z +3.9, 18/48 lines), [[PLEKHM1]] 1.25× (z +3.9, 16/49 lines)

**0.5 µM** (7 genes, none with an alert): [[RIC8A]] 1.29× (z +3.3, 7/47 lines), [[GYG1]] 1.35× (z +3.3, 3/46 lines), [[TCIRG1]] 1.45× (z +3.3, 8/41 lines), [[PPT2]] 1.32× (z +3.0, 2/42 lines), [[SDR16C5]] 1.54× (z +3.0, 1/20 lines), [[E2F7]] 1.24× (z +2.8, 4/43 lines), [[FAM219B]] 1.30× (z +2.8, 1/47 lines)

**5 µM** (2 genes, none with an alert): [[NATD1]] 1.79× (z +2.9, 0/17 lines), [[KLHL24]] 1.39× (z +2.7, 14/48 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (59 genes, none with an alert; 12 shown): [[DLAT]] 0.788× (z -4.4, 18/48 lines), [[MCM4]] 0.694× (z -4.3, 23/46 lines), [[ANGPT1]] 0.704× (z -4.1, 9/23 lines), [[PNPO]] 0.682× (z -4.1, 14/43 lines), [[ACLY]] 0.788× (z -4.0, 24/48 lines), [[SERPINH1]] 0.732× (z -4.0, 22/45 lines), [[ATP5F1B]] 0.743× (z -3.9, 36/49 lines), [[TMPO]] 0.779× (z -3.9, 18/48 lines), [[RBBP9]] 0.740× (z -3.8, 14/46 lines), [[DHCR7]] 0.682× (z -3.8, 18/43 lines), [[DEPDC1]] 0.725× (z -3.8, 17/46 lines), [[ANLN]] 0.743× (z -3.6, 26/47 lines)

**0.5 µM** (1 gene, none with an alert): [[TMEM268]] 0.754× (z -3.4, 7/43 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | [[Module 170]] (+2.4) | [[Module 006]] (-2.4), [[Module 025]] (-2.1), [[Module 060]] (-2.1) |
| 0.5 µM | — | — |
| 5 µM | — | — |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | [[HOP62 (line)]] (1.43), [[Hs 766T (line)]] (1.41), [[LOX-IMVI (line)]] (1.30), [[NCI-H460 (line)]] (1.29) · weakest: [[NCI-H2122 (line)]] (0.113), [[SW1417 (line)]] (0.568), [[C-33 A (line)]] (0.597) |
| 0.5 µM | [[HCT15 (line)]] (-3.5) | — |
| 5 µM | [[RKO (line)]] (-3.6), [[SW480 (line)]] (-3.3) | — |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 1 next most similar without an alert.*

- [[AZD1390 (drug)]] (+0.73, unclear); [[Resveratrol (drug)]] (+0.71, unclear); [[Rapamycin (drug)]] (+0.66, MTOR inhibitor); [[Temsirolimus (drug)]] (+0.65, MTOR inhibitor); [[Lactate (calcium) (drug)]] (+0.65, unclear); [[MK-3903 (drug)]] (+0.63, unclear); [[Bergenin (drug)]] (+0.59, unclear); [[4EGI-1 (drug)]] (+0.58, Protein synthesis inhibitor, ⚠ vector dose flagged: cell-cycle shift); [[Hydroxyurea (drug)]] (+0.51, DNA synthesis/repair inhibitor)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 10 arrows, 10 of them with an alert ⚠; grade A 0, B 5, C 5.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[EEPD1]] | 5 µM | B | EEPD1 activity raises the cells' numbers under ULK-101 5 µM (protects the cells) | lines that do not express EEPD1 (14) vs lines expressing it (34) | the lines without EEPD1: 0.86× the cells of the other lines | 0.033 | ⚠ within organs, on part of the lines; also absent: KCNK5, RHOD, LAMP3; maybe low, not absent |
| [[PAPPA2]] | 5 µM | B | PAPPA2 activity lowers the cells' numbers under ULK-101 5 µM (makes them more sensitive) | lines that do not express PAPPA2 (28) vs lines expressing it (20) | the lines without PAPPA2: 1.20× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: COL19A1, KCNH5, KCNK2; maybe low, not absent |
| [[GLRX]] | 5 µM | B | GLRX activity lowers the cells' numbers under ULK-101 5 µM (makes them more sensitive) | lines that do not express GLRX (10) vs lines expressing it (38) | the lines without GLRX: 1.17× the cells of the other lines | 0.092 | ⚠ within organs, on part of the lines; also absent: DUSP10, FES, DGKG; maybe low, not absent |
| [[LINC02306]] | 5 µM | B | LINC02306 activity lowers the cells' numbers under ULK-101 5 µM (makes them more sensitive) | lines that do not express LINC02306 (13) vs lines expressing it (35) | the lines without LINC02306: 1.20× the cells of the other lines | 0.094 | ⚠ within organs, on part of the lines; also absent: KCNMB2, COP1-DT, LINC02398; maybe low, not absent |
| [[PLXNA2]] | 5 µM | B | PLXNA2 activity lowers the cells' numbers under ULK-101 5 µM (makes them more sensitive) | lines that do not express PLXNA2 (15) vs lines expressing it (33) | the lines without PLXNA2: 1.11× the cells of the other lines | 0.096 | ⚠ within organs, on part of the lines; also absent: GATA6, HS3ST3B1, IFI16 |
| [[SEMA4G]] | 5 µM | C | SEMA4G activity lowers the cells' numbers under ULK-101 5 µM (makes them more sensitive) | lines that do not express SEMA4G (6) vs lines expressing it (42) | the lines without SEMA4G: 1.28× the cells of the other lines | 0.050 | ⚠ tissue-confounded; across organs; also absent: SLC2A9, HMGA2; maybe low, not absent |
| [[PPP2R1B]] | 5 µM | C | PPP2R1B's natural level lowers the cells' numbers under ULK-101 5 µM (makes them more sensitive) | PPP2R1B's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.70 | 0.268 over the table, 0.033 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| [[ENSG00000274322]] | 5 µM | C | ENSG00000274322's natural level lowers the cells' numbers under ULK-101 5 µM (makes them more sensitive) | ENSG00000274322's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.66 | 0.339 over the table, 0.064 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| [[MTA3]] | 5 µM | C | MTA3's natural level raises the cells' numbers under ULK-101 5 µM (protects the cells) | MTA3's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.66 | 0.352 over the table, 0.064 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| [[C1QTNF6]] | 5 µM | C | C1QTNF6's natural level raises the cells' numbers under ULK-101 5 µM (protects the cells) | C1QTNF6's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.65 | 0.361 over the table, 0.064 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "ULK-101"
- `tables/drugdoses.parquet` — dd in 1063, 1064, 1065
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
