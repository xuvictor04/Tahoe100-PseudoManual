---
drug: "Lactate (calcium)"
type: "drug"
salt_base: "Lactate"
targets: ""
moa_fine: "unclear"
moa_broad: "unclear"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "0.5"
max_sig_genes: 178
tags: ["drug", "moa/unclear"]
generated_by: "tahoemap"
---

# Lactate (calcium)

*unclear (unclear) · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 131 / 178 / 90; best dose 0.5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.05 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.29 / 0.37.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 10]]:H1 | 107 / 24 | — | +0.25 | +0.1/-1.8/-0.2 | — |
| 0.5 µM | [[Plate 11]]:H1 | 109 / 69 | — | -0.37 | -2.8/-3.7/-1.7 | — |
| 5 µM | [[Plate 12]]:H1 | 58 / 32 | — | -0.17 | -0.2/-2.1/+0.8 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (107 genes, none with an alert; 12 shown): [[FKBP5]] 1.82× (z +9.0, 26/42 lines), [[CCND3]] 1.86× (z +8.5, 31/47 lines), [[KLF9]] 1.50× (z +6.8, 26/43 lines), [[NNMT]] 1.95× (z +6.1, 18/24 lines), [[HIPK2]] 1.23× (z +5.3, 23/43 lines), [[SAA2-SAA4]] 2.33× (z +5.1, 14/24 lines), [[SAA2]] 2.31× (z +4.8, 13/26 lines), [[TPCN1]] 1.23× (z +4.6, 17/48 lines), [[PID1]] 1.38× (z +4.5, 12/26 lines), [[VWA8]] 1.38× (z +4.5, 33/48 lines), [[SLC7A11]] 1.43× (z +4.4, 21/42 lines), [[MIPOL1]] 1.30× (z +4.3, 26/40 lines)

**0.5 µM** (109 genes, none with an alert; 12 shown): [[FAM114A1]] 1.27× (z +5.1, 27/46 lines), [[TTLL3]] 1.27× (z +4.4, 20/48 lines), [[LINC02649]] 1.37× (z +4.4, 31/45 lines), [[PMS2P4-1]] 1.23× (z +4.2, 19/48 lines), [[CCDC18-AS1]] 1.29× (z +4.2, 28/48 lines), [[NLRP1]] 1.28× (z +4.2, 10/27 lines), [[COL4A3]] 1.43× (z +4.1, 6/18 lines), [[ENSG00000272305]] 1.33× (z +4.1, 6/46 lines), [[CDKL1]] 1.22× (z +4.0, 14/48 lines), [[EPS15-AS1]] 1.51× (z +4.0, 8/32 lines), [[MATN1-AS1]] 1.43× (z +3.9, 6/40 lines), [[PATJ]] 1.20× (z +3.9, 18/39 lines)

**5 µM** (58 genes, none with an alert; 12 shown): [[UTY]] 1.27× (z +4.1, 0/17 lines), [[ZEB2]] 1.25× (z +3.9, 0/21 lines), [[TOX3]] 1.36× (z +3.8, 0/17 lines), [[MACC1]] 1.37× (z +3.7, 0/16 lines), [[SLC8A2]] 1.57× (z +3.7, 4/44 lines), [[ENSG00000243389]] 1.34× (z +3.6, 1/45 lines), [[HAP1]] 1.53× (z +3.6, 10/34 lines), [[ENSG00000268279]] 1.47× (z +3.5, 3/43 lines), [[ENSG00000243276]] 1.33× (z +3.5, 0/17 lines), [[FES]] 1.65× (z +3.5, 2/33 lines), [[IDI2-AS1]] 1.45× (z +3.4, 10/47 lines), [[GARIN1B]] 2.09× (z +3.4, 7/39 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (24 genes, none with an alert; 12 shown): [[PKIA]] 0.789× (z -4.1, 13/26 lines), [[TUBB6]] 0.796× (z -4.0, 16/37 lines), [[HIF1A-AS3]] 0.780× (z -3.8, 18/35 lines), [[LBH]] 0.735× (z -3.7, 9/26 lines), [[ENSG00000100101]] 0.779× (z -3.7, 10/48 lines), [[ENSG00000273269]] 0.633× (z -3.6, 13/45 lines), [[RIMKLA]] 0.815× (z -3.6, 9/40 lines), [[ENSG00000288894]] 0.707× (z -3.4, 4/44 lines), [[DTNA]] 0.784× (z -3.4, 11/26 lines), [[CEP55]] 0.803× (z -3.4, 14/46 lines), [[ENSG00000272772]] 0.786× (z -3.3, 11/48 lines), [[SMTN]] 0.796× (z -3.2, 14/48 lines)

**0.5 µM** (69 genes, none with an alert; 12 shown): [[CCNB1]] 0.692× (z -4.6, 25/47 lines), [[FAM83D]] 0.729× (z -4.5, 17/47 lines), [[SHCBP1]] 0.733× (z -4.4, 24/47 lines), [[KNSTRN]] 0.761× (z -4.4, 13/47 lines), [[ARHGAP11A]] 0.763× (z -4.4, 24/47 lines), [[CEP55]] 0.751× (z -4.4, 24/46 lines), [[NUF2]] 0.740× (z -4.2, 24/47 lines), [[DEPDC1]] 0.713× (z -4.2, 20/46 lines), [[AURKA]] 0.739× (z -4.1, 22/48 lines), [[KIF23]] 0.773× (z -4.1, 17/47 lines), [[ANLN]] 0.750× (z -4.0, 35/46 lines), [[H2AC6]] 0.711× (z -3.9, 21/48 lines)

**5 µM** (32 genes, none with an alert; 12 shown): [[KNSTRN]] 0.704× (z -5.7, 23/47 lines), [[CEP85]] 0.786× (z -4.6, 12/48 lines), [[ARHGAP11A]] 0.779× (z -4.1, 17/47 lines), [[MYEF2]] 0.825× (z -3.9, 12/31 lines), [[TACC3]] 0.805× (z -3.8, 9/48 lines), [[CEP55]] 0.782× (z -3.8, 17/46 lines), [[NUP93]] 0.801× (z -3.6, 18/48 lines), [[CIT]] 0.806× (z -3.6, 14/47 lines), [[ZNF563]] 0.719× (z -3.6, 5/38 lines), [[PANK3]] 0.813× (z -3.5, 25/48 lines), [[FAR1]] 0.813× (z -3.4, 23/47 lines), [[GAS2L3]] 0.825× (z -3.4, 11/48 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | [[Module 230]] (+2.1), [[Module 137]] (+2.0) | [[Module 179]] (-2.3), [[Module 207]] (-2.0) |
| 0.5 µM | [[Module 170]] (+2.7) | [[Module 182]] (-3.3), [[Module 025]] (-2.0) |
| 5 µM | — | [[Module 025]] (-2.4), [[Module 171]] (-2.3) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | [[HEC-1-A (line)]] (-3.3) | [[A549 (line)]] (1.89), [[NCI-H1573 (line)]] (1.81), [[HOP62 (line)]] (1.62), [[NCI-H1792 (line)]] (1.62) · weakest: [[KATO III (line)]] (0.381), [[AN3 CA (line)]] (0.424), [[NCI-H661 (line)]] (0.483) |
| 0.5 µM | — | [[SW 1088 (line)]] (1.34), [[Hs 766T (line)]] (1.25), [[SNU-423 (line)]] (1.23), [[HS-578T (line)]] (1.22) · weakest: [[AN3 CA (line)]] (0.140), [[NCI-H661 (line)]] (0.454), [[BT-474 (line)]] (0.517) |
| 5 µM | [[HEC-1-A (line)]] (-3.3) | [[AN3 CA (line)]] (1.26), [[RKO (line)]] (1.25), [[CHP-212 (line)]] (1.24), [[C32 (line)]] (1.20) · weakest: [[LS 180 (line)]] (0.447), [[NCI-H661 (line)]] (0.450), [[SW 1088 (line)]] (0.457) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 2 next most similar without an alert.*

- [[Idoxuridine (drug)]] (+0.69, DNA synthesis/repair inhibitor, ⚠ only 4 significant genes); [[Bimatoprost (drug)]] (+0.66, unclear); [[ULK-101 (drug)]] (+0.65, unclear); [[Drospirenone (drug)]] (+0.61, unclear); [[AZD1390 (drug)]] (+0.60, unclear); [[Bestatin (hydrochloride) (drug)]] (+0.59, unclear); [[Canagliflozin (hemihydrate) (drug)]] (+0.58, Glucose transporter inhibitor); [[Levobupivacaine (hydrochloride) (drug)]] (+0.58, unclear, ⚠ only 9 significant genes); [[Rapamycin (drug)]] (+0.58, MTOR inhibitor); [[Pimozide (drug)]] (+0.57, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 35 arrows, 35 of them with an alert ⚠; grade A 0, B 30, C 5. Shown: the 15 strongest; 20 more arrows (20 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[SPOCK1]] | 0.05 µM | B | SPOCK1 activity raises the cells' numbers under Lactate (calcium) 0.05 µM (protects the cells) | lines that do not express SPOCK1 (29) vs lines expressing it (19) | the lines without SPOCK1: 0.79× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: SRGN, ENSG00000280241, TEX41 |
| [[ENSG00000230647]] | 0.05 µM | B | ENSG00000230647 activity raises the cells' numbers under Lactate (calcium) 0.05 µM (protects the cells) | lines that do not express ENSG00000230647 (24) vs lines expressing it (24) | the lines without ENSG00000230647: 0.80× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: ADAM12, ENSG00000253891, SPOCK1 |
| [[EPCAM]] | 0.05 µM | B | EPCAM activity lowers the cells' numbers under Lactate (calcium) 0.05 µM (makes them more sensitive) | lines that do not express EPCAM (28) vs lines expressing it (20) | the lines without EPCAM: 1.20× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, KDF1, CLDN3 |
| [[MYH14]] | 0.05 µM | B | MYH14 activity lowers the cells' numbers under Lactate (calcium) 0.05 µM (makes them more sensitive) | lines that do not express MYH14 (21) vs lines expressing it (27) | the lines without MYH14: 1.24× the cells of the other lines | 0.036 | ⚠ within organs, on part of the lines; also absent: ERBB3, EPCAM, FAAH2 |
| [[SRGN]] | 0.05 µM | B | SRGN activity raises the cells' numbers under Lactate (calcium) 0.05 µM (protects the cells) | lines that do not express SRGN (30) vs lines expressing it (18) | the lines without SRGN: 0.78× the cells of the other lines | 0.037 | ⚠ within organs, on part of the lines; also absent: SIRLNT, SPOCK1, KIRREL3 |
| [[DCDC2]] | 0.05 µM | B | DCDC2 activity lowers the cells' numbers under Lactate (calcium) 0.05 µM (makes them more sensitive) | lines that do not express DCDC2 (25) vs lines expressing it (23) | the lines without DCDC2: 1.13× the cells of the other lines | 0.043 | ⚠ within organs, on part of the lines; also absent: FXYD2, PGBD5, HAVCR1 |
| [[SIRLNT]] | 0.05 µM | B | SIRLNT activity raises the cells' numbers under Lactate (calcium) 0.05 µM (protects the cells) | lines that do not express SIRLNT (32) vs lines expressing it (16) | the lines without SIRLNT: 0.78× the cells of the other lines | 0.046 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SRGN, LINC01411, KCNMA1 |
| [[KCNMA1]] | 0.05 µM | B | KCNMA1 activity raises the cells' numbers under Lactate (calcium) 0.05 µM (protects the cells) | lines that do not express KCNMA1 (26) vs lines expressing it (22) | the lines without KCNMA1: 0.80× the cells of the other lines | 0.048 | ⚠ within organs, on part of the lines; also absent: F2RL2, SIRLNT, SRGN |
| [[ERBB3]] | 0.05 µM | B | ERBB3 activity lowers the cells' numbers under Lactate (calcium) 0.05 µM (makes them more sensitive) | lines that do not express ERBB3 (27) vs lines expressing it (21) | the lines without ERBB3: 1.19× the cells of the other lines | 0.056 | ⚠ within organs, on part of the lines; also absent: LAD1, KDF1, EPCAM |
| [[ADAM12]] | 0.05 µM | B | ADAM12 activity raises the cells' numbers under Lactate (calcium) 0.05 µM (protects the cells) | lines that do not express ADAM12 (27) vs lines expressing it (21) | the lines without ADAM12: 0.80× the cells of the other lines | 0.066 | ⚠ within organs, on part of the lines; also absent: ZEB2, MSC-AS1, CNRIP1 |
| [[PAPPA]] | 0.05 µM | B | PAPPA activity raises the cells' numbers under Lactate (calcium) 0.05 µM (protects the cells) | lines that do not express PAPPA (33) vs lines expressing it (15) | the lines without PAPPA: 0.81× the cells of the other lines | 0.071 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HTRA3, MSC-AS1, PDGFRB |
| [[ENSG00000230615]] | 0.05 µM | B | ENSG00000230615 activity raises the cells' numbers under Lactate (calcium) 0.05 µM (protects the cells) | lines that do not express ENSG00000230615 (25) vs lines expressing it (23) | the lines without ENSG00000230615: 0.81× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: FRMD4A, ENSG00000253891, SRGN; maybe low, not absent |
| [[RNF125]] | 0.05 µM | B | RNF125 activity lowers the cells' numbers under Lactate (calcium) 0.05 µM (makes them more sensitive) | lines that do not express RNF125 (9) vs lines expressing it (39) | the lines without RNF125: 1.26× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; also absent: SAMD10, TMTC2; maybe low, not absent |
| [[FGD4]] | 0.05 µM | B | FGD4 activity lowers the cells' numbers under Lactate (calcium) 0.05 µM (makes them more sensitive) | lines that do not express FGD4 (10) vs lines expressing it (38) | the lines without FGD4: 1.16× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; also absent: PARD6B, CARD10, VAMP8; maybe low, not absent |
| [[SMPDL3B]] | 0.05 µM | B | SMPDL3B activity lowers the cells' numbers under Lactate (calcium) 0.05 µM (makes them more sensitive) | lines that do not express SMPDL3B (23) vs lines expressing it (25) | the lines without SMPDL3B: 1.18× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: HOOK1, BSPRY, SPINT1-AS1 |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Lactate (calcium)"
- `tables/drugdoses.parquet` — dd in 600, 601, 602
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
