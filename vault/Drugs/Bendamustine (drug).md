---
drug: "Bendamustine"
type: "drug"
salt_base: "Bendamustine"
targets: ""
moa_fine: "DNA synthesis/repair inhibitor"
moa_broad: "unclear"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 257
tags: ["drug", "moa/unclear"]
generated_by: "tahoemap"
---

# Bendamustine

*DNA synthesis/repair inhibitor (unclear) · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 1 / 3 / 257; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.43 / -0.48.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 07]]:F11 | 0 / 1 | — | -0.07 | -1.1/-1.0/-0.9 | — |
| 0.5 µM | [[Plate 08]]:F11 | 3 / 0 | — | -0.23 | -1.5/-1.3/-1.5 | — |
| 5 µM | [[Plate 09]]:F11 | 229 / 28 | — | -0.57 | +1.6/+1.3/+2.2 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (3 genes, none with an alert): [[ENSG00000269968]] 1.78× (z +5.5, 33/47 lines), [[ENSG00000273149]] 1.63× (z +3.6, 12/45 lines), [[ENSG00000272335]] 1.27× (z +3.2, 1/47 lines)

**5 µM** (229 genes, none with an alert; 12 shown): [[PLPP2]] 1.43× (z +4.3, 8/37 lines), [[CLDN11]] 1.60× (z +4.3, 4/17 lines), [[BCAT1]] 1.25× (z +4.1, 1/23 lines), [[TMPRSS3]] 1.61× (z +4.1, 2/17 lines), [[LINC01618]] 1.56× (z +4.0, 7/30 lines), [[SLC5A1]] 1.65× (z +4.0, 0/11 lines), [[ENSG00000291100]] 1.41× (z +3.8, 16/33 lines), [[CLDN10]] 1.67× (z +3.8, 0/13 lines), [[C2orf74-DT]] 1.60× (z +3.8, 8/23 lines), [[MYOM3]] 1.56× (z +3.8, 0/14 lines), [[LINC01242]] 2.04× (z +3.8, 0/3 lines), [[GRHL2]] 1.30× (z +3.7, 0/14 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (1 gene, none with an alert): [[THNSL2]] 0.716× (z -2.9, 4/25 lines)

**5 µM** (28 genes, none with an alert; 12 shown): [[SEMA4F]] 0.742× (z -4.2, 12/40 lines), [[PRKAB1]] 0.767× (z -3.9, 14/43 lines), [[MFAP3]] 0.821× (z -3.7, 18/48 lines), [[NSF]] 0.833× (z -3.7, 16/47 lines), [[ENSG00000261386]] 0.726× (z -3.6, 9/40 lines), [[SLC35F5]] 0.806× (z -3.6, 23/48 lines), [[PIP4K2B]] 0.820× (z -3.6, 17/47 lines), [[INPP5B]] 0.817× (z -3.5, 14/47 lines), [[USP19]] 0.755× (z -3.4, 13/46 lines), [[ZNF587B]] 0.690× (z -3.3, 22/45 lines), [[PRDM16]] 0.793× (z -3.3, 14/28 lines), [[LRATD2]] 0.810× (z -3.3, 9/31 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | [[Module 060]] (+2.3), [[Module 064]] (+2.3), [[Module 131]] (+2.2) | [[Module 170]] (-2.1) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | [[HOP62 (line)]] (-3.7), [[A498 (line)]] (-3.1), [[A549 (line)]] (-3.1) | — |
| 5 µM | — | [[AN3 CA (line)]] (1.39), [[SW48 (line)]] (1.36), [[SW 1271 (line)]] (1.32), [[SW 1088 (line)]] (1.29) · weakest: [[CFPAC-1 (line)]] (0.506), [[SK-MEL-2 (line)]] (0.558), [[PANC-1 (line)]] (0.580) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 3 next most similar without an alert.*

- [[Bicalutamide (drug)]] (+0.87, Androgen receptor antagonist); [[Decitabine (drug)]] (+0.84, DNA methyltransferase inhibitor); [[Sivelestat (sodium tetrahydrate) (drug)]] (+0.81, unclear); [[Tranilast (drug)]] (+0.80, unclear, ⚠ only 6 significant genes); [[Darolutamide (drug)]] (+0.75, Androgen receptor antagonist, ⚠ only 5 significant genes); [[Imiquimod (hydrochloride) (drug)]] (+0.74, unclear, ⚠ vector dose flagged: toxic); [[Silodosin (drug)]] (+0.74, unclear); [[Arbutin (drug)]] (+0.72, unclear); [[Canagliflozin (hemihydrate) (drug)]] (+0.72, Glucose transporter inhibitor); [[Methylprednisolone succinate (drug)]] (+0.71, Glucocorticoid receptor agonist); [[Docetaxel (Trihydrate) (drug)]] (+0.71, Microtubule inhibitor)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 64 arrows, 64 of them with an alert ⚠; grade A 0, B 7, C 57. Shown: the 15 strongest; 49 more arrows (49 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[ENSG00000230615]] | 0.5 µM | B | ENSG00000230615 activity lowers the cells' numbers under Bendamustine 0.5 µM (makes them more sensitive) | lines that do not express ENSG00000230615 (25) vs lines expressing it (23) | the lines without ENSG00000230615: 1.29× the cells of the other lines | 0.047 | ⚠ within organs, on part of the lines; also absent: FRMD4A, ENSG00000253891, SRGN; maybe low, not absent |
| [[CGAS]] | 5 µM | B | CGAS activity raises the cells' numbers under Bendamustine 5 µM (protects the cells) | lines that do not express CGAS (17) vs lines expressing it (31) | the lines without CGAS: 0.82× the cells of the other lines | 0.052 | ⚠ within organs, on part of the lines; also absent: ENSG00000234902, C15orf48, TYMP |
| [[KLRC3]] | 5 µM | B | KLRC3 activity lowers the cells' numbers under Bendamustine 5 µM (makes them more sensitive) | lines that do not express KLRC3 (27) vs lines expressing it (21) | the lines without KLRC3: 1.16× the cells of the other lines | 0.069 | ⚠ within organs, on part of the lines; also absent: KLRK1, KLRC2, IGFL4 |
| [[KIRREL3]] | 0.5 µM | B | KIRREL3 activity lowers the cells' numbers under Bendamustine 0.5 µM (makes them more sensitive) | lines that do not express KIRREL3 (36) vs lines expressing it (12) | the lines without KIRREL3: 1.32× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FOXC2, LINC01411, SRGN |
| [[KLRC4-KLRK1]], [[KLRK1]] | 5 µM | B | KLRC4-KLRK1, KLRK1 activity lowers the cells' numbers under Bendamustine 5 µM (makes them more sensitive) | lines that do not express KLRC4-KLRK1, KLRK1 (29) vs lines expressing them (19) | the lines without KLRC4-KLRK1, KLRK1: 1.18× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: KLRC3, KLRC2, PIP5K1B; co-absent genes |
| [[MYH14]] | 0.5 µM | B | MYH14 activity raises the cells' numbers under Bendamustine 0.5 µM (protects the cells) | lines that do not express MYH14 (21) vs lines expressing it (27) | the lines without MYH14: 0.80× the cells of the other lines | 0.078 | ⚠ within organs, on part of the lines; also absent: ERBB3, EPCAM, FAAH2 |
| [[C12orf75-AS1]] | 0.5 µM | B | C12orf75-AS1 activity lowers the cells' numbers under Bendamustine 0.5 µM (makes them more sensitive) | lines that do not express C12orf75-AS1 (22) vs lines expressing it (26) | the lines without C12orf75-AS1: 1.24× the cells of the other lines | 0.0995 | ⚠ within organs, on part of the lines; also absent: ENSG00000230615, FOXC2, GLIPR1 |
| [[PICART1]] | 5 µM | C | PICART1 activity raises the cells' numbers under Bendamustine 5 µM (protects the cells) | lines that do not express PICART1 (4) vs lines expressing it (44) | the lines without PICART1: 0.74× the cells of the other lines | 0.014 | ⚠ few lines (4 vs 46); across organs; also absent: GULP1, RND3, MYO10; maybe low, not absent |
| [[RARG]] | 5 µM | C | RARG activity raises the cells' numbers under Bendamustine 5 µM (protects the cells) | lines that do not express RARG (3) vs lines expressing it (45) | the lines without RARG: 0.74× the cells of the other lines | 0.026 | ⚠ few lines (3 vs 47); across organs; also absent: ANXA2, SLC25A43, MYO10; maybe low, not absent |
| [[C2orf74]] | 0.5 µM | C | C2orf74 activity lowers the cells' numbers under Bendamustine 0.5 µM (makes them more sensitive) | lines that do not express C2orf74 (13) vs lines expressing it (35) | the lines without C2orf74: 1.21× the cells of the other lines | 0.033 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: C2orf74-DT, ENSG00000286964, NR3C1 |
| [[FIGN]] | 0.5 µM | C | FIGN activity lowers the cells' numbers under Bendamustine 0.5 µM (makes them more sensitive) | lines that do not express FIGN (16) vs lines expressing it (32) | the lines without FIGN: 1.19× the cells of the other lines | 0.034 | ⚠ tissue-confounded; across organs; also absent: SPART-AS1, CCDC169, SPART |
| [[NR3C1]] | 0.5 µM | C | NR3C1 activity lowers the cells' numbers under Bendamustine 0.5 µM (makes them more sensitive) | lines that do not express NR3C1 (13) vs lines expressing it (35) | the lines without NR3C1: 1.22× the cells of the other lines | 0.043 | ⚠ tissue-confounded; across organs; co-occurs with SETD1B, ZFHX3; also absent: C2orf74-DT, C2orf74, SPART-AS1 |
| [[FIGN]] | 5 µM | C | FIGN activity raises the cells' numbers under Bendamustine 5 µM (protects the cells) | lines that do not express FIGN (16) vs lines expressing it (32) | the lines without FIGN: 0.88× the cells of the other lines | 0.076 | ⚠ tissue-confounded; across organs; also absent: SPART-AS1, CCDC169, SPART |
| [[NR3C1]] | 5 µM | C | NR3C1 activity raises the cells' numbers under Bendamustine 5 µM (protects the cells) | lines that do not express NR3C1 (13) vs lines expressing it (35) | the lines without NR3C1: 0.85× the cells of the other lines | 0.082 | ⚠ tissue-confounded; across organs; co-occurs with SETD1B, ZFHX3; also absent: C2orf74-DT, C2orf74, SPART-AS1 |
| [[EID1]], [[TMEM17]] | 5 µM | C | EID1, TMEM17 activity raises the cells' numbers under Bendamustine 5 µM (protects the cells) | lines that do not express EID1, TMEM17 (3) vs lines expressing them (45) | the lines without EID1, TMEM17: 0.77× the cells of the other lines | 0.082 | ⚠ few lines (3 vs 47); across organs; also absent: MNS1, ENSG00000283491, AGK; co-absent genes |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Bendamustine"
- `tables/drugdoses.parquet` — dd in 155, 156, 157
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
