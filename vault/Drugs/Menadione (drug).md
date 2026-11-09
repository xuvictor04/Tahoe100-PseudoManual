---
drug: "Menadione"
type: "drug"
salt_base: "Menadione"
targets: ""
moa_fine: "unclear"
moa_broad: "unclear"
approved: "no"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 32
tags: ["drug", "moa/unclear"]
generated_by: "tahoemap"
---

# Menadione

*unclear (unclear) · approved: no*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 18 / 5 / 32; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.13 / 0.27.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 07]]:G4 | 16 / 2 | — | -0.58 | +0.3/-0.0/+0.2 | — |
| 0.5 µM | [[Plate 08]]:G4 | 5 / 0 | — | -0.86 | -0.6/-1.0/-0.1 | — |
| 5 µM | [[Plate 09]]:G4 | 17 / 15 | — | -0.53 | -0.8/-0.1/+0.8 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (16 genes, none with an alert; 12 shown): [[WDR5B]] 1.42× (z +3.8, 6/30 lines), [[TLCD4-RWDD3]] 1.40× (z +3.3, 2/21 lines), [[ENSG00000262660]] 1.29× (z +3.2, 7/44 lines), [[ANK1]] 1.29× (z +3.2, 2/23 lines), [[LINC02646]] 1.55× (z +3.2, 7/39 lines), [[EFR3B]] 1.23× (z +3.1, 3/35 lines), [[FAM230C]] 1.28× (z +3.1, 0/16 lines), [[PPIA]] 1.22× (z +3.0, 17/48 lines), [[C1orf116]] 1.29× (z +3.0, 0/17 lines), [[ENSG00000239572]] 1.67× (z +3.0, 0/6 lines), [[PIK3CD]] 1.22× (z +3.0, 3/36 lines), [[PKHD1]] 1.41× (z +3.0, 0/12 lines)

**0.5 µM** (5 genes, none with an alert): [[ALDH1A3]] 1.28× (z +3.2, 7/27 lines), [[LINC01139]] 1.44× (z +3.1, 2/21 lines), [[ENSG00000261654]] 1.37× (z +3.0, 1/35 lines), [[LCA5L]] 1.29× (z +2.8, 3/42 lines), [[NUP210L]] 1.25× (z +2.8, 4/45 lines)

**5 µM** (17 genes, none with an alert; 12 shown): [[ALDH1A3]] 1.73× (z +6.8, 21/27 lines), [[MIR181A1HG]] 1.52× (z +6.1, 32/40 lines), [[CYP1B1]] 2.44× (z +5.9, 18/18 lines), [[RMDN2-AS1]] 2.18× (z +5.4, 18/24 lines), [[TIPARP]] 1.58× (z +5.4, 35/46 lines), [[AHRR]] 1.40× (z +5.2, 23/44 lines), [[TPRA1]] 1.33× (z +4.4, 22/47 lines), [[CYP1B1-AS1]] 1.62× (z +4.1, 14/29 lines), [[PIR]] 1.27× (z +3.7, 12/37 lines), [[ENSG00000285635]] 1.32× (z +3.6, 9/32 lines), [[VEGFD]] 1.47× (z +3.4, 6/31 lines), [[ENSG00000227400]] 1.48× (z +3.3, 11/16 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (2 genes, none with an alert): [[CABYR]] 0.781× (z -3.3, 8/35 lines), [[SMCO4]] 0.828× (z -2.9, 7/42 lines)

**5 µM** (15 genes, none with an alert; 12 shown): [[TNS1]] 0.737× (z -4.0, 8/24 lines), [[SMOC1]] 0.718× (z -3.4, 3/14 lines), [[ENSG00000255750]] 0.666× (z -3.3, 5/31 lines), [[HARBI1]] 0.737× (z -3.3, 10/34 lines), [[LINC03004]] 0.671× (z -3.3, 7/22 lines), [[ENSG00000285534]] 0.736× (z -3.2, 3/16 lines), [[LINC02454]] 0.701× (z -3.2, 6/27 lines), [[ENSG00000259560]] 0.750× (z -3.2, 2/11 lines), [[CPS1]] 0.719× (z -3.2, 4/11 lines), [[ENSG00000286329]] 0.687× (z -3.1, 2/11 lines), [[LINC02320]] 0.706× (z -3.0, 6/28 lines), [[SLCO4A1]] 0.781× (z -3.0, 9/38 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | — | — |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | — | [[H4 (line)]] (1.67), [[A498 (line)]] (1.58), [[NCI-H1792 (line)]] (1.54), [[NCI-H2030 (line)]] (1.30) · weakest: [[NCI-H661 (line)]] (-0.111), [[MIA PaCa-2 (line)]] (0.0440), [[A-172 (line)]] (0.167) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 4 next most similar without an alert.*

- [[Pasireotide (acetate) (drug)]] (+0.61, unclear); [[Futibatinib (drug)]] (+0.55, Other TK inhibitor); [[Ivabradine (hydrochloride) (drug)]] (+0.54, unclear, ⚠ no trustworthy dose (vector dose flagged: unreliable plate only)); [[Cysteamine (hydrochloride) (drug)]] (+0.48, unclear); [[Loperamide (hydrochloride) (drug)]] (+0.45, unclear); [[Fostamatinib (disodium hexahydrate) (drug)]] (+0.44, Other TK inhibitor, ⚠ only 3 significant genes; no trustworthy dose (vector dose flagged: unreliable plate only)); [[Lipoic acid (drug)]] (+0.43, unclear, ⚠ only 6 significant genes); [[Macitentan (drug)]] (+0.42, unclear, ⚠ only 5 significant genes); [[Gemcitabine (drug)]] (+0.41, DNA synthesis/repair inhibitor); [[Goserelin (acetate) (drug)]] (+0.36, unclear); [[Gallic acid (drug)]] (+0.36, Cyclooxygenase inhibitor); [[Bisoprolol (hemifumarate) (drug)]] (+0.35, Adrenoceptor agonist)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 34 arrows, 34 of them with an alert ⚠; grade A 0, B 13, C 21. Shown: the 15 strongest; 19 more arrows (19 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[MYH14]] | 0.5 µM | B | MYH14 activity raises the cells' numbers under Menadione 0.5 µM (protects the cells) | lines that do not express MYH14 (21) vs lines expressing it (27) | the lines without MYH14: 0.85× the cells of the other lines | 0.033 | ⚠ within organs, on part of the lines; also absent: ERBB3, EPCAM, FAAH2 |
| [[ERBB3]] | 0.5 µM | B | ERBB3 activity raises the cells' numbers under Menadione 0.5 µM (protects the cells) | lines that do not express ERBB3 (27) vs lines expressing it (21) | the lines without ERBB3: 0.86× the cells of the other lines | 0.046 | ⚠ within organs, on part of the lines; also absent: LAD1, KDF1, EPCAM |
| [[FAAH2]] | 0.5 µM | B | FAAH2 activity raises the cells' numbers under Menadione 0.5 µM (protects the cells) | lines that do not express FAAH2 (26) vs lines expressing it (22) | the lines without FAAH2: 0.84× the cells of the other lines | 0.071 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, TNNT2, ST14; maybe low, not absent |
| [[EPCAM]] | 0.5 µM | B | EPCAM activity raises the cells' numbers under Menadione 0.5 µM (protects the cells) | lines that do not express EPCAM (28) vs lines expressing it (20) | the lines without EPCAM: 0.87× the cells of the other lines | 0.071 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, KDF1, CLDN3 |
| [[PLCH1]] | 0.5 µM | B | PLCH1 activity raises the cells' numbers under Menadione 0.5 µM (protects the cells) | lines that do not express PLCH1 (12) vs lines expressing it (36) | the lines without PLCH1: 0.84× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[LAD1]] | 0.5 µM | B | LAD1 activity raises the cells' numbers under Menadione 0.5 µM (protects the cells) | lines that do not express LAD1 (30) vs lines expressing it (18) | the lines without LAD1: 0.86× the cells of the other lines | 0.075 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, ST14, KDF1 |
| [[CLDN4]] | 0.5 µM | B | CLDN4 activity raises the cells' numbers under Menadione 0.5 µM (protects the cells) | lines that do not express CLDN4 (26) vs lines expressing it (22) | the lines without CLDN4: 0.89× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: CDH1, SCNN1A, ITGB6 |
| [[FOXP2]] | 0.5 µM | B | FOXP2 activity raises the cells' numbers under Menadione 0.5 µM (protects the cells) | lines that do not express FOXP2 (26) vs lines expressing it (22) | the lines without FOXP2: 0.93× the cells of the other lines | 0.091 | ⚠ within organs, on part of the lines; also absent: BMP4, SPON1, ITGB6 |
| [[TMEM45B]] | 0.5 µM | B | TMEM45B activity raises the cells' numbers under Menadione 0.5 µM (protects the cells) | lines that do not express TMEM45B (32) vs lines expressing it (16) | the lines without TMEM45B: 0.86× the cells of the other lines | 0.093 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TRIM15, CDH1, ENSG00000267881 |
| [[BLACAT1]] | 0.5 µM | B | BLACAT1 activity raises the cells' numbers under Menadione 0.5 µM (protects the cells) | lines that do not express BLACAT1 (21) vs lines expressing it (27) | the lines without BLACAT1: 0.91× the cells of the other lines | 0.095 | ⚠ within organs, on part of the lines; also absent: LEMD1, MPZL3, SULT1C2 |
| [[ENSG00000230615]] | 0.5 µM | B | ENSG00000230615 activity lowers the cells' numbers under Menadione 0.5 µM (makes them more sensitive) | lines that do not express ENSG00000230615 (25) vs lines expressing it (23) | the lines without ENSG00000230615: 1.19× the cells of the other lines | 0.095 | ⚠ within organs, on part of the lines; also absent: FRMD4A, ENSG00000253891, SRGN; maybe low, not absent |
| [[NLGN4X]] | 0.5 µM | B | NLGN4X activity raises the cells' numbers under Menadione 0.5 µM (protects the cells) | lines that do not express NLGN4X (37) vs lines expressing it (11) | the lines without NLGN4X: 1.00× the cells of the other lines | 0.098 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01029, ENSG00000291025, ANKRD20A8P |
| [[RNF125]] | 0.5 µM | B | RNF125 activity raises the cells' numbers under Menadione 0.5 µM (protects the cells) | lines that do not express RNF125 (9) vs lines expressing it (39) | the lines without RNF125: 0.81× the cells of the other lines | 0.099 | ⚠ within organs, on part of the lines; also absent: SAMD10, TMTC2; maybe low, not absent |
| [[FIGN]] | 0.5 µM | C | FIGN activity lowers the cells' numbers under Menadione 0.5 µM (makes them more sensitive) | lines that do not express FIGN (16) vs lines expressing it (32) | the lines without FIGN: 1.16× the cells of the other lines | 0.008 | ⚠ tissue-confounded; across organs; also absent: SPART-AS1, CCDC169, SPART |
| [[SPART-AS1]] | 0.5 µM | C | SPART-AS1 activity lowers the cells' numbers under Menadione 0.5 µM (makes them more sensitive) | lines that do not express SPART-AS1 (16) vs lines expressing it (32) | the lines without SPART-AS1: 1.15× the cells of the other lines | 0.014 | ⚠ tissue-confounded; across organs; also absent: CCDC169, FIGN, SPART |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Menadione"
- `tables/drugdoses.parquet` — dd in 669, 670, 671
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
