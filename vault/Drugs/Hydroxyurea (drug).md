---
drug: "Hydroxyurea"
type: "drug"
salt_base: "Hydroxyurea"
targets: "RRM2, RRM1"
moa_fine: "DNA synthesis/repair inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "0.05"
max_sig_genes: 87
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Hydroxyurea

*DNA synthesis/repair inhibitor (inhibitor/antagonist) · targets: RRM2, RRM1 · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 87 / 43 / 21; best dose 0.05 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.05 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.05 / 0.36.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 07]]:D6 | 83 / 4 | — | -0.85 | -1.3/-1.3/+0.5 | — |
| 0.5 µM | [[Plate 08]]:D6 | 3 / 40 | — | -0.75 | -0.5/-0.9/+0.1 | — |
| 5 µM | [[Plate 09]]:D6 | 2 / 19 | — | +0.17 | -0.2/-0.3/-1.6 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (83 genes, none with an alert; 12 shown): [[LINC01611]] 1.77× (z +5.4, 1/11 lines), [[ENSG00000286263]] 1.57× (z +4.0, 4/15 lines), [[XKR8]] 1.48× (z +3.8, 3/23 lines), [[ACOT12]] 1.75× (z +3.7, 5/24 lines), [[MYO7A]] 1.57× (z +3.7, 5/25 lines), [[ENSG00000263655]] 1.76× (z +3.7, 0/5 lines), [[AZU1]] 1.80× (z +3.7, 2/14 lines), [[IPCEF1]] 1.43× (z +3.6, 2/24 lines), [[FSCN2]] 2.05× (z +3.6, 8/33 lines), [[CSMD2]] 1.43× (z +3.6, 2/12 lines), [[ENSG00000256915]] 1.50× (z +3.6, 0/15 lines), [[FBXW9]] 1.39× (z +3.6, 3/33 lines)

**0.5 µM** (3 genes, none with an alert): [[BEST1]] 1.39× (z +3.2, 12/45 lines), [[GALNT8]] 1.33× (z +2.9, 2/23 lines), [[EID3]] 1.35× (z +2.8, 5/41 lines)

**5 µM** (2 genes, none with an alert): [[GABBR1]] 1.20× (z +3.5, 11/41 lines), [[ENSG00000265784]] 1.45× (z +3.2, 3/43 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (4 genes, none with an alert): [[MRPS31P5-1]] 0.677× (z -3.5, 5/20 lines), [[ARMCX5]] 0.799× (z -3.3, 10/40 lines), [[ENSG00000173867]] 0.778× (z -3.2, 8/40 lines), [[TREX2]] 0.795× (z -3.1, 13/39 lines)

**0.5 µM** (40 genes, none with an alert; 12 shown): [[FGFRL1]] 0.533× (z -6.8, 36/46 lines), [[TP53I11]] 0.642× (z -5.6, 20/40 lines), [[MT-ND1]] 0.467× (z -5.0, 46/47 lines), [[MT-CO2]] 0.635× (z -4.9, 45/47 lines), [[MGRN1]] 0.801× (z -4.9, 29/47 lines), [[MT-ND4L]] 0.508× (z -4.6, 43/47 lines), [[SORBS3]] 0.748× (z -4.5, 18/45 lines), [[SDC3]] 0.727× (z -4.5, 15/43 lines), [[MT-ND5]] 0.647× (z -4.1, 47/47 lines), [[PLBD2]] 0.815× (z -4.0, 15/47 lines), [[GAS6]] 0.769× (z -3.9, 14/38 lines), [[CYP2S1]] 0.686× (z -3.9, 14/28 lines)

**5 µM** (19 genes, none with an alert; 12 shown): [[FGFRL1]] 0.650× (z -4.5, 18/45 lines), [[NDUFS2]] 0.766× (z -4.1, 17/47 lines), [[NTRK2]] 0.686× (z -4.0, 1/19 lines), [[GHDC]] 0.671× (z -3.8, 13/42 lines), [[PAXIP1-DT]] 0.680× (z -3.7, 10/42 lines), [[CASP6]] 0.721× (z -3.7, 14/46 lines), [[GNG10]] 0.809× (z -3.6, 12/47 lines), [[AKIP1]] 0.702× (z -3.5, 12/47 lines), [[NID2]] 0.706× (z -3.5, 0/15 lines), [[RNF7]] 0.673× (z -3.5, 35/48 lines), [[DHPS]] 0.768× (z -3.4, 14/47 lines), [[TSR3]] 0.660× (z -3.4, 13/46 lines)

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
| 0.05 µM | — | [[NCI-H661 (line)]] (2.36), [[SW 1271 (line)]] (1.90), [[SW48 (line)]] (1.51), [[HepG2_C3A (line)]] (1.38) · weakest: [[PANC-1 (line)]] (0.0295), [[KATO III (line)]] (0.122), [[LoVo (line)]] (0.200) |
| 0.5 µM | [[A549 (line)]] (-4.8), [[A498 (line)]] (-3.7), [[SNU-423 (line)]] (-3.7), [[HOP62 (line)]] (-3.4), [[HS-578T (line)]] (-3.4) | [[HT-29 (line)]] (1.22), [[C-33 A (line)]] (1.21), [[SK-MEL-2 (line)]] (1.21), [[BT-474 (line)]] (1.16) · weakest: [[Hs 766T (line)]] (0.732), [[LoVo (line)]] (0.779), [[LOX-IMVI (line)]] (0.813) |
| 5 µM | — | [[AN3 CA (line)]] (1.80), [[HT-29 (line)]] (1.53), [[SW48 (line)]] (1.47), [[HOP62 (line)]] (1.43) · weakest: [[SW 1088 (line)]] (0.0392), [[Panc 03.27 (line)]] (0.637), [[C32 (line)]] (0.699) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 3 next most similar without an alert.*

- [[Thymol (drug)]] (+0.85, unclear); [[Pyridoxine (drug)]] (+0.83, unclear); [[Nimesulide (drug)]] (+0.80, Cyclooxygenase inhibitor, ⚠ no trustworthy dose (vector dose flagged: toxic; unreliable plate only)); [[Canagliflozin (drug)]] (+0.78, Glucose transporter inhibitor); [[Ipatasertib (drug)]] (+0.75, PI3K/AKT inhibitor); [[LY-2584702 (tosylate salt) (drug)]] (+0.70, MTOR inhibitor, ⚠ vector dose flagged: toxic); [[Canagliflozin (hemihydrate) (drug)]] (+0.70, Glucose transporter inhibitor); [[Tubulin inhibitor 6 (drug)]] (+0.69, Microtubule inhibitor, ⚠ only 2 significant genes); [[Oxaprozin (drug)]] (+0.69, Cyclooxygenase inhibitor); [[Methylprednisolone succinate (drug)]] (+0.68, Glucocorticoid receptor agonist); [[9-ING-41 (drug)]] (+0.64, GSK3 inhibitor)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 28 arrows, 28 of them with an alert ⚠; grade A 0, B 12, C 16. Shown: the 15 strongest; 13 more arrows (13 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[ENSG00000230647]] | 0.5 µM | B | ENSG00000230647 activity lowers the cells' numbers under Hydroxyurea 0.5 µM (makes them more sensitive) | lines that do not express ENSG00000230647 (24) vs lines expressing it (24) | the lines without ENSG00000230647: 1.32× the cells of the other lines | 0.043 | ⚠ within organs, on part of the lines; also absent: ADAM12, ENSG00000253891, SPOCK1 |
| [[ENSG00000230615]] | 0.5 µM | B | ENSG00000230615 activity lowers the cells' numbers under Hydroxyurea 0.5 µM (makes them more sensitive) | lines that do not express ENSG00000230615 (25) vs lines expressing it (23) | the lines without ENSG00000230615: 1.35× the cells of the other lines | 0.052 | ⚠ within organs, on part of the lines; also absent: FRMD4A, ENSG00000253891, SRGN; maybe low, not absent |
| [[MYH14]] | 0.5 µM | B | MYH14 activity raises the cells' numbers under Hydroxyurea 0.5 µM (protects the cells) | lines that do not express MYH14 (21) vs lines expressing it (27) | the lines without MYH14: 0.74× the cells of the other lines | 0.056 | ⚠ within organs, on part of the lines; also absent: ERBB3, EPCAM, FAAH2 |
| [[PAPPA]] | 0.5 µM | B | PAPPA activity lowers the cells' numbers under Hydroxyurea 0.5 µM (makes them more sensitive) | lines that do not express PAPPA (33) vs lines expressing it (15) | the lines without PAPPA: 1.34× the cells of the other lines | 0.071 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HTRA3, MSC-AS1, PDGFRB |
| [[EPCAM]] | 0.5 µM | B | EPCAM activity raises the cells' numbers under Hydroxyurea 0.5 µM (protects the cells) | lines that do not express EPCAM (28) vs lines expressing it (20) | the lines without EPCAM: 0.79× the cells of the other lines | 0.073 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, KDF1, CLDN3 |
| [[KCNMA1]] | 0.5 µM | B | KCNMA1 activity lowers the cells' numbers under Hydroxyurea 0.5 µM (makes them more sensitive) | lines that do not express KCNMA1 (26) vs lines expressing it (22) | the lines without KCNMA1: 1.34× the cells of the other lines | 0.075 | ⚠ within organs, on part of the lines; also absent: F2RL2, SIRLNT, SRGN |
| [[SPOCK1]] | 0.5 µM | B | SPOCK1 activity lowers the cells' numbers under Hydroxyurea 0.5 µM (makes them more sensitive) | lines that do not express SPOCK1 (29) vs lines expressing it (19) | the lines without SPOCK1: 1.36× the cells of the other lines | 0.084 | ⚠ within organs, on part of the lines; also absent: SRGN, ENSG00000280241, TEX41 |
| [[SRGN]] | 0.5 µM | B | SRGN activity lowers the cells' numbers under Hydroxyurea 0.5 µM (makes them more sensitive) | lines that do not express SRGN (30) vs lines expressing it (18) | the lines without SRGN: 1.41× the cells of the other lines | 0.089 | ⚠ within organs, on part of the lines; also absent: SIRLNT, SPOCK1, KIRREL3 |
| [[KIRREL3]] | 0.5 µM | B | KIRREL3 activity lowers the cells' numbers under Hydroxyurea 0.5 µM (makes them more sensitive) | lines that do not express KIRREL3 (36) vs lines expressing it (12) | the lines without KIRREL3: 1.42× the cells of the other lines | 0.091 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FOXC2, LINC01411, SRGN |
| [[RNF125]] | 0.5 µM | B | RNF125 activity raises the cells' numbers under Hydroxyurea 0.5 µM (protects the cells) | lines that do not express RNF125 (9) vs lines expressing it (39) | the lines without RNF125: 0.73× the cells of the other lines | 0.093 | ⚠ within organs, on part of the lines; also absent: SAMD10, TMTC2; maybe low, not absent |
| [[SLFN5]] | 0.5 µM | B | SLFN5 activity lowers the cells' numbers under Hydroxyurea 0.5 µM (makes them more sensitive) | lines that do not express SLFN5 (11) vs lines expressing it (37) | the lines without SLFN5: 1.31× the cells of the other lines | 0.093 | ⚠ within organs, on part of the lines; also absent: ENSG00000261273, ETS1, SAMD9; maybe low, not absent |
| [[PLA2G4A]] | 0.5 µM | B | PLA2G4A activity lowers the cells' numbers under Hydroxyurea 0.5 µM (makes them more sensitive) | lines that do not express PLA2G4A (22) vs lines expressing it (26) | the lines without PLA2G4A: 1.17× the cells of the other lines | 0.095 | ⚠ within organs, on part of the lines; also absent: PTGS2, ITGA4, EPB41L3 |
| [[FIGN]] | 0.5 µM | C | FIGN activity lowers the cells' numbers under Hydroxyurea 0.5 µM (makes them more sensitive) | lines that do not express FIGN (16) vs lines expressing it (32) | the lines without FIGN: 1.26× the cells of the other lines | 0.025 | ⚠ tissue-confounded; across organs; also absent: SPART-AS1, CCDC169, SPART |
| [[SCAMP5]] | 0.5 µM | C | SCAMP5 activity raises the cells' numbers under Hydroxyurea 0.5 µM (protects the cells) | lines that do not express SCAMP5 (3) vs lines expressing it (45) | the lines without SCAMP5: 0.66× the cells of the other lines | 0.034 | ⚠ few lines (3 vs 47); across organs; also absent: ENSG00000262160, SLC4A11, CORO2A; maybe low, not absent |
| [[SPART-AS1]] | 0.5 µM | C | SPART-AS1 activity lowers the cells' numbers under Hydroxyurea 0.5 µM (makes them more sensitive) | lines that do not express SPART-AS1 (16) vs lines expressing it (32) | the lines without SPART-AS1: 1.24× the cells of the other lines | 0.037 | ⚠ tissue-confounded; across organs; also absent: CCDC169, FIGN, SPART |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Hydroxyurea"
- `tables/drugdoses.parquet` — dd in 534, 535, 536
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
