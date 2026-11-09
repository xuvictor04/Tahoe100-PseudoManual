---
drug: "Allantoin"
type: "drug"
salt_base: "Allantoin"
targets: ""
moa_fine: "unclear"
moa_broad: "unclear"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "0.5"
max_sig_genes: 24
tags: ["drug", "moa/unclear"]
generated_by: "tahoemap"
---

# Allantoin

*unclear (unclear) · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 20 / 24 / 20; best dose 0.5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.05 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.13 / 0.22.
> Flags by dose: transcription drop / - / -. ⚠ 0.05 µM: transcription drop (artifact flags: its changes there are shown with an alert, not left out).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 04]]:F5 | 18 / 2 | — | -0.36 | -0.3/-0.3/-0.8 | ⚠ transcription drop |
| 0.5 µM | [[Plate 05]]:F5 | 2 / 22 | — | -0.06 | -0.8/-0.5/+0.2 | — |
| 5 µM | [[Plate 14]]:F5 | 8 / 12 | 0.644 | +0.16 | +2.0/+1.8/+0.8 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (18 genes, 18 with an alert ⚠; the drug-dose carries ⚠ transcription drop; 12 shown): [[ATP8A2]] ⚠ 1.33× (z +3.6, 0/39 lines), [[ANKRD20A7P]] ⚠ 1.52× (z +3.5, 0/13 lines), [[DNAH3]] ⚠ 1.45× (z +3.5, 2/33 lines), [[ENSG00000259560]] ⚠ 1.35× (z +3.4, 2/11 lines), [[ENSG00000197670]] ⚠ 1.36× (z +3.3, 7/43 lines), [[SCARF1]] ⚠ 1.36× (z +3.2, 0/32 lines), [[POTEF]] ⚠ 1.30× (z +3.2, 1/19 lines), [[ENSG00000287176]] ⚠ 1.48× (z +3.1, 0/13 lines), [[ENSG00000266302]] ⚠ 1.27× (z +3.1, 0/16 lines), [[ENSG00000270055]] ⚠ 1.39× (z +3.1, 3/31 lines), [[ENSG00000266578]] ⚠ 1.45× (z +3.0, 2/17 lines), [[TTYH2]] ⚠ 1.24× (z +3.0, 1/32 lines)

**0.5 µM** (2 genes, none with an alert): [[SLIT1]] 1.24× (z +2.9, 0/34 lines), [[ALOX5]] 1.28× (z +2.8, 1/18 lines)

**5 µM** (8 genes, none with an alert): [[COCH]] 1.25× (z +3.9, 10/46 lines), [[MAP3K12]] 1.23× (z +3.9, 20/48 lines), [[ENSG00000259033]] 1.34× (z +3.7, 9/45 lines), [[CNTN5]] 1.26× (z +3.7, 10/46 lines), [[FKBP5]] 1.24× (z +3.7, 13/42 lines), [[ENSG00000260289]] 1.31× (z +3.4, 5/11 lines), [[HMGB3]] 1.24× (z +3.4, 14/47 lines), [[TP63]] 1.25× (z +3.0, 3/9 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (2 genes, 2 with an alert ⚠; the drug-dose carries ⚠ transcription drop): [[KLHDC3]] ⚠ 0.832× (z -3.6, 10/47 lines), [[DMTN]] ⚠ 0.764× (z -3.3, 6/31 lines)

**0.5 µM** (22 genes, none with an alert; 12 shown): [[MRPS17]] 0.630× (z -3.9, 10/36 lines), [[BMS1P23]] 0.694× (z -3.8, 14/36 lines), [[RNF187]] 0.767× (z -3.7, 24/48 lines), [[TPP1]] 0.790× (z -3.6, 18/46 lines), [[AGAP9]] 0.779× (z -3.6, 10/43 lines), [[HSPA8]] 0.711× (z -3.4, 38/48 lines), [[MORF4L1P1]] 0.714× (z -3.4, 6/42 lines), [[AGAP4]] 0.789× (z -3.4, 10/43 lines), [[INTS1]] 0.811× (z -3.4, 19/48 lines), [[ZNF284]] 0.722× (z -3.4, 8/34 lines), [[CCNG1]] 0.830× (z -3.3, 21/48 lines), [[PIAS3]] 0.818× (z -3.3, 12/48 lines)

**5 µM** (12 genes, none with an alert): [[MNT]] 0.789× (z -5.0, 32/48 lines), [[FBRS]] 0.796× (z -4.5, 26/48 lines), [[C3orf33]] 0.796× (z -3.9, 10/45 lines), [[SLC15A2]] 0.728× (z -3.7, 14/45 lines), [[PITPNM1]] 0.808× (z -3.7, 12/47 lines), [[PRSS8]] 0.738× (z -3.5, 0/15 lines), [[STK32A]] 0.798× (z -3.5, 5/25 lines), [[MORN4]] 0.789× (z -3.4, 9/46 lines), [[EAF2]] 0.798× (z -3.4, 11/48 lines), [[AMPD2]] 0.828× (z -3.3, 14/47 lines), [[NR1D1]] 0.764× (z -3.2, 18/46 lines), [[LINC01881]] 0.821× (z -3.2, 11/48 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | — | [[Module 179]] (-2.7), [[Module 207]] (-2.2) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | [[SW 1088 (line)]] (2.35), [[SNU-1 (line)]] (2.33), [[SW 1271 (line)]] (1.76), [[CHP-212 (line)]] (1.70) · weakest: [[A-427 (line)]] (-0.691), [[SK-MEL-2 (line)]] (-0.440), [[A549 (line)]] (-0.267) |
| 0.5 µM | [[Hs 766T (line)]] (-3.5) | [[SHP-77 (line)]] (1.59), [[hTERT-HPNE (line)]] (1.51), [[SW1417 (line)]] (1.46), [[Panc 03.27 (line)]] (1.46) · weakest: [[C-33 A (line)]] (0.441), [[BT-474 (line)]] (0.505), [[A549 (line)]] (0.514) |
| 5 µM | — | [[A549 (line)]] (1.89), [[SW 1088 (line)]] (1.70), [[hTERT-HPNE (line)]] (1.36), [[NCI-H2030 (line)]] (1.33) · weakest: [[COLO 205 (line)]] (0.122), [[AsPC-1 (line)]] (0.412), [[NCI-H2347 (line)]] (0.442) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 1 next most similar without an alert.*

- [[Elagolix sodium (drug)]] (+0.56, unclear); [[Bergenin (drug)]] (+0.55, unclear); [[Doxycycline (monohydrate) (drug)]] (+0.54, unclear); [[Sulfisoxazole (drug)]] (+0.53, unclear); [[Tolcapone (drug)]] (+0.47, unclear, ⚠ only 6 significant genes); [[Flutamide (drug)]] (+0.45, Androgen receptor antagonist); [[Sivelestat (sodium tetrahydrate) (drug)]] (+0.44, unclear); [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] (+0.44, Glucose transporter inhibitor); [[Verteporfin (drug)]] (+0.43, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 5 arrows, 5 of them with an alert ⚠; grade A 0, B 1, C 4.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[MTMR7]] | 0.5 µM | B | MTMR7 activity lowers the cells' numbers under Allantoin 0.5 µM (makes them more sensitive) | lines that do not express MTMR7 (16) vs lines expressing it (32) | the lines without MTMR7: 1.15× the cells of the other lines | 0.058 | ⚠ within organs, on part of the lines; also absent: GAP43, NRXN1, LOXL3; maybe low, not absent |
| [[ENSG00000285458]] | 0.5 µM | C | ENSG00000285458 activity raises the cells' numbers under Allantoin 0.5 µM (protects the cells) | lines that do not express ENSG00000285458 (5) vs lines expressing it (43) | the lines without ENSG00000285458: 0.82× the cells of the other lines | 0.038 | ⚠ tissue-confounded; across organs; also absent: TBILA, GCA, RILP; maybe low, not absent |
| [[PHF11]] | 0.5 µM | C | PHF11 activity raises the cells' numbers under Allantoin 0.5 µM (protects the cells) | lines that do not express PHF11 (3) vs lines expressing it (45) | the lines without PHF11: 0.79× the cells of the other lines | 0.082 | ⚠ few lines (3 vs 47); across organs; also absent: NABP1, ANXA2, SDC4 |
| [[FIGN]] | 0.5 µM | C | FIGN activity raises the cells' numbers under Allantoin 0.5 µM (protects the cells) | lines that do not express FIGN (16) vs lines expressing it (32) | the lines without FIGN: 0.89× the cells of the other lines | 0.090 | ⚠ tissue-confounded; across organs; also absent: SPART-AS1, CCDC169, SPART |
| [[PLEKHA5]] | 0.5 µM | C | PLEKHA5 activity raises the cells' numbers under Allantoin 0.5 µM (protects the cells) | lines that do not express PLEKHA5 (4) vs lines expressing it (44) | the lines without PLEKHA5: 0.82× the cells of the other lines | 0.097 | ⚠ few lines (4 vs 46); across organs; also absent: SVIP, LRRCC1, USP53 |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Allantoin"
- `tables/drugdoses.parquet` — dd in 69, 70, 71
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
