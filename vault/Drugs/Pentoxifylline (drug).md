---
drug: "Pentoxifylline"
type: "drug"
salt_base: "Pentoxifylline"
targets: ""
moa_fine: "unclear"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "0.5"
max_sig_genes: 24
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Pentoxifylline

*unclear (inhibitor/antagonist) · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 13 / 24 / 5; best dose 0.5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): low dose only (noise?).
> Signature similarity between consecutive doses (low–mid / mid–high): -0.04 / 0.42.
> Flags by dose: transcription drop / - / -. ⚠ 0.05 µM: transcription drop (artifact flags: its changes there are shown with an alert, not left out).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 10]]:F5 | 8 / 5 | — | +0.09 | +0.4/+1.2/+1.1 | ⚠ transcription drop |
| 0.5 µM | [[Plate 11]]:F5 | 20 / 4 | — | -0.15 | +0.7/+1.1/-0.3 | — |
| 5 µM | [[Plate 12]]:F5 | 4 / 1 | — | +0.43 | +0.1/+1.2/-0.2 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (8 genes, 8 with an alert ⚠; the drug-dose carries ⚠ transcription drop): [[PI4KAP1-1]] ⚠ 1.47× (z +4.1, 0/20 lines), [[MT-TV]] ⚠ 1.76× (z +3.7, 11/42 lines), [[MT-TL1]] ⚠ 1.64× (z +3.2, 11/44 lines), [[AKR1B10]] ⚠ 1.61× (z +3.1, 1/7 lines), [[LINC00654]] ⚠ 1.46× (z +3.0, 3/39 lines), [[SV2A]] ⚠ 1.30× (z +2.9, 1/28 lines), [[KRT6A]] ⚠ 1.78× (z +2.8, 0/7 lines), [[RASGEF1B]] ⚠ 1.26× (z +2.8, 1/34 lines)

**0.5 µM** (20 genes, none with an alert; 12 shown): [[EPN1]] 1.20× (z +4.2, 20/48 lines), [[PLBD2]] 1.24× (z +4.1, 15/48 lines), [[AGBL5]] 1.25× (z +3.8, 14/48 lines), [[SCAF1]] 1.22× (z +3.7, 11/48 lines), [[ATN1]] 1.23× (z +3.6, 23/48 lines), [[CDC25B]] 1.29× (z +3.6, 13/48 lines), [[RIPOR1]] 1.27× (z +3.6, 15/47 lines), [[BAG6]] 1.23× (z +3.3, 17/48 lines), [[RBM22]] 1.20× (z +3.3, 9/48 lines), [[HCFC1]] 1.27× (z +3.3, 23/48 lines), [[WIZ]] 1.27× (z +3.2, 5/46 lines), [[ELK4]] 1.26× (z +3.2, 22/48 lines)

**5 µM** (4 genes, none with an alert): [[ENSG00000262831]] 1.65× (z +4.3, 10/44 lines), [[SCAF1]] 1.22× (z +3.6, 9/48 lines), [[CDC25B]] 1.28× (z +3.5, 11/48 lines), [[PI4KAP1-1]] 1.37× (z +3.4, 0/21 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (5 genes, 5 with an alert ⚠; the drug-dose carries ⚠ transcription drop): [[ZNF18]] ⚠ 0.742× (z -3.9, 7/43 lines), [[LRFN3]] ⚠ 0.764× (z -3.4, 2/43 lines), [[ENSG00000289293]] ⚠ 0.706× (z -3.2, 11/44 lines), [[ENSG00000285043]] ⚠ 0.735× (z -3.1, 6/41 lines), [[RTKN]] ⚠ 0.827× (z -2.9, 8/41 lines)

**0.5 µM** (4 genes, none with an alert): [[CRMP1]] 0.765× (z -3.9, 3/26 lines), [[LINC00482]] 0.666× (z -3.3, 11/28 lines), [[ZNF461]] 0.833× (z -3.3, 10/40 lines), [[ENSG00000285572]] 0.688× (z -3.2, 8/31 lines)

**5 µM** (1 gene, none with an alert): [[ENSG00000249631]] 0.741× (z -3.2, 2/26 lines)

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
| 0.5 µM | [[Hs 766T (line)]] (-6.5) | [[HT-29 (line)]] (1.65), [[LS 180 (line)]] (1.52), [[A549 (line)]] (1.50), [[C32 (line)]] (1.44) · weakest: [[CHP-212 (line)]] (0.175), [[SW 1271 (line)]] (0.281), [[SW 1088 (line)]] (0.307) |
| 5 µM | — | — |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 4 next most similar without an alert.*

- [[Uridine (drug)]] (+0.69, unclear, ⚠ only 6 significant genes); [[Methylthiouracil (drug)]] (+0.67, unclear, ⚠ only 9 significant genes); [[Folic acid (drug)]] (+0.58, unclear); [[Malotilate (drug)]] (+0.56, unclear); [[Phenytoin (sodium) (drug)]] (+0.54, unclear, ⚠ only 7 significant genes); [[Ivermectin (drug)]] (+0.52, unclear); [[Docetaxel (drug)]] (+0.52, Microtubule inhibitor, ⚠ vector dose flagged: transcription drop; cell-cycle shift); [[8-Hydroxyquinoline (drug)]] (+0.52, unclear); [[Omeprazole (drug)]] (+0.46, unclear); [[Fluvoxamine (drug)]] (+0.43, unclear); [[Roxadustat (drug)]] (+0.43, unclear); [[Bentamapimod (drug)]] (+0.42, Other MAPK inhibitor)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 30 arrows, 30 of them with an alert ⚠; grade A 0, B 14, C 16. Shown: the 15 strongest; 15 more arrows (15 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[ALDH3B1]] | 0.5 µM | B | ALDH3B1 activity raises the cells' numbers under Pentoxifylline 0.5 µM (protects the cells) | lines that do not express ALDH3B1 (9) vs lines expressing it (39) | the lines without ALDH3B1: 0.78× the cells of the other lines | 0.052 | ⚠ within organs, on part of the lines; also absent: NIBAN2, IER3, FOSL1; maybe low, not absent |
| [[PRSS23]] | 0.05 µM | B | PRSS23 activity raises the cells' numbers under Pentoxifylline 0.05 µM (protects the cells) | lines that do not express PRSS23 (13) vs lines expressing it (35) | the lines without PRSS23: 0.82× the cells of the other lines | 0.058 | ⚠ within organs, on part of the lines; co-occurs with SETD1B; also absent: ETS1, TMSB4X, ZNF469; maybe low, not absent |
| [[MYH14]] | 0.05 µM | B | MYH14 activity lowers the cells' numbers under Pentoxifylline 0.05 µM (makes them more sensitive) | lines that do not express MYH14 (21) vs lines expressing it (27) | the lines without MYH14: 1.19× the cells of the other lines | 0.058 | ⚠ within organs, on part of the lines; also absent: ERBB3, EPCAM, FAAH2 |
| [[KCNMA1]] | 0.05 µM | B | KCNMA1 activity raises the cells' numbers under Pentoxifylline 0.05 µM (protects the cells) | lines that do not express KCNMA1 (26) vs lines expressing it (22) | the lines without KCNMA1: 0.83× the cells of the other lines | 0.071 | ⚠ within organs, on part of the lines; also absent: F2RL2, SIRLNT, SRGN |
| [[PAPPA]] | 0.05 µM | B | PAPPA activity raises the cells' numbers under Pentoxifylline 0.05 µM (protects the cells) | lines that do not express PAPPA (33) vs lines expressing it (15) | the lines without PAPPA: 0.84× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HTRA3, MSC-AS1, PDGFRB |
| [[SIRLNT]] | 0.05 µM | B | SIRLNT activity raises the cells' numbers under Pentoxifylline 0.05 µM (protects the cells) | lines that do not express SIRLNT (32) vs lines expressing it (16) | the lines without SIRLNT: 0.82× the cells of the other lines | 0.078 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SRGN, LINC01411, KCNMA1 |
| [[SLFN5]] | 0.05 µM | B | SLFN5 activity raises the cells' numbers under Pentoxifylline 0.05 µM (protects the cells) | lines that do not express SLFN5 (11) vs lines expressing it (37) | the lines without SLFN5: 0.84× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: ENSG00000261273, ETS1, SAMD9; maybe low, not absent |
| [[ZNF469]] | 0.05 µM | B | ZNF469 activity raises the cells' numbers under Pentoxifylline 0.05 µM (protects the cells) | lines that do not express ZNF469 (20) vs lines expressing it (28) | the lines without ZNF469: 0.83× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; also absent: LINC02057, IL6, TMEM158 |
| [[ENSG00000259200]] | 0.5 µM | B | ENSG00000259200 activity raises the cells' numbers under Pentoxifylline 0.5 µM (protects the cells) | lines that do not express ENSG00000259200 (18) vs lines expressing it (30) | the lines without ENSG00000259200: 0.85× the cells of the other lines | 0.089 | ⚠ within organs, on part of the lines; also absent: ENSG00000203635, CSGALNACT1, ENSG00000232692; maybe low, not absent |
| [[ENSG00000228933]] | 0.5 µM | B | ENSG00000228933 activity lowers the cells' numbers under Pentoxifylline 0.5 µM (makes them more sensitive) | lines that do not express ENSG00000228933 (26) vs lines expressing it (22) | the lines without ENSG00000228933: 1.15× the cells of the other lines | 0.091 | ⚠ within organs, on part of the lines; also absent: ENSG00000242021, ENSG00000259639, CCDC144NL-AS1 |
| [[BHLHE41]] | 0.5 µM | B | BHLHE41 activity raises the cells' numbers under Pentoxifylline 0.5 µM (protects the cells) | lines that do not express BHLHE41 (19) vs lines expressing it (29) | the lines without BHLHE41: 0.83× the cells of the other lines | 0.093 | ⚠ within organs, on part of the lines; also absent: RAC2, JHY, ENSG00000289600 |
| [[CLMP]] | 0.05 µM | B | CLMP activity raises the cells' numbers under Pentoxifylline 0.05 µM (protects the cells) | lines that do not express CLMP (25) vs lines expressing it (23) | the lines without CLMP: 0.84× the cells of the other lines | 0.093 | ⚠ within organs, on part of the lines; also absent: KCNMA1, PAPPA, DOCK10 |
| [[MCF2L]] | 0.05 µM | B | MCF2L activity lowers the cells' numbers under Pentoxifylline 0.05 µM (makes them more sensitive) | lines that do not express MCF2L (14) vs lines expressing it (34) | the lines without MCF2L: 1.19× the cells of the other lines | 0.095 | ⚠ within organs, on part of the lines; also absent: B4GALNT3, CGN, HSD11B2 |
| [[HTRA3]] | 0.05 µM | B | HTRA3 activity raises the cells' numbers under Pentoxifylline 0.05 µM (protects the cells) | lines that do not express HTRA3 (31) vs lines expressing it (17) | the lines without HTRA3: 0.84× the cells of the other lines | 0.095 | ⚠ within organs, on part of the lines; also absent: PAPPA, LUM, LAYN |
| [[PSMB8]] | 0.5 µM | C | PSMB8 activity raises the cells' numbers under Pentoxifylline 0.5 µM (protects the cells) | lines that do not express PSMB8 (4) vs lines expressing it (44) | the lines without PSMB8: 0.73× the cells of the other lines | 0.013 | ⚠ few lines (4 vs 46); across organs; co-occurs with WNK2; also absent: TBILA, GCA, C3orf52 |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Pentoxifylline"
- `tables/drugdoses.parquet` — dd in 794, 795, 796
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
