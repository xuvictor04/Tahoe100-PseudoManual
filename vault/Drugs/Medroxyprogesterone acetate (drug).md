---
drug: "Medroxyprogesterone acetate"
type: "drug"
salt_base: "Medroxyprogesterone acetate"
targets: "PGR"
moa_fine: "unclear"
moa_broad: "unclear"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "0.5"
max_sig_genes: 465
tags: ["drug", "moa/unclear"]
generated_by: "tahoemap"
---

# Medroxyprogesterone acetate

*unclear (unclear) · targets: PGR · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 108 / 465 / 115; best dose 0.5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.05 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.07 / 0.13.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 04]]:G5 | 26 / 82 | — | -0.05 | +1.3/-0.2/-0.4 | — |
| 0.5 µM | [[Plate 05]]:G5 | 286 / 179 | — | -0.56 | +0.5/-0.2/+1.6 | — |
| 5 µM | [[Plate 14]]:G5 | 46 / 69 | 0.645 | -0.07 | +1.0/-0.3/-0.1 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (26 genes, none with an alert; 12 shown): [[FKBP5]] 1.79× (z +8.8, 24/41 lines), [[KLF9]] 1.42× (z +5.9, 24/43 lines), [[B3GNT5]] 1.39× (z +5.5, 20/41 lines), [[CCND3]] 1.46× (z +5.2, 23/47 lines), [[PID1]] 1.44× (z +5.1, 13/26 lines), [[NNMT]] 1.63× (z +4.5, 13/24 lines), [[TAF8]] 1.20× (z +4.0, 11/47 lines), [[ENSG00000289418]] 2.03× (z +3.8, 9/9 lines), [[MAOA]] 1.28× (z +3.4, 10/32 lines), [[ADPRHL1]] 1.32× (z +3.3, 15/45 lines), [[TANC2]] 1.21× (z +3.2, 17/41 lines), [[GREB1]] 1.29× (z +3.2, 3/35 lines)

**0.5 µM** (286 genes, none with an alert; 12 shown): [[FKBP5]] 1.78× (z +8.7, 28/40 lines), [[JPH2]] 1.94× (z +7.7, 16/26 lines), [[IRAK3]] 2.01× (z +7.6, 10/12 lines), [[DNER]] 1.79× (z +7.5, 11/16 lines), [[ADPRHL1]] 1.87× (z +7.5, 23/37 lines), [[HS3ST3B1]] 1.75× (z +7.2, 14/26 lines), [[PID1]] 1.65× (z +7.1, 13/26 lines), [[CCND3]] 1.66× (z +6.9, 25/46 lines), [[NNMT]] 2.09× (z +6.7, 17/22 lines), [[ENSG00000289418]] 3.39× (z +6.5, 8/8 lines), [[ITGA10]] 1.98× (z +6.3, 20/28 lines), [[TMTC1]] 1.49× (z +6.2, 9/21 lines)

**5 µM** (46 genes, none with an alert; 12 shown): [[FKBP5]] 1.91× (z +12.9, 28/42 lines), [[KLF9]] 1.40× (z +8.1, 28/43 lines), [[PID1]] 1.43× (z +6.9, 15/26 lines), [[MAOA]] 1.42× (z +6.1, 11/33 lines), [[CCND3]] 1.36× (z +5.9, 23/47 lines), [[B3GNT5]] 1.28× (z +5.7, 22/41 lines), [[NNMT]] 1.52× (z +5.4, 14/24 lines), [[IRAK3]] 1.41× (z +5.3, 9/12 lines), [[ENSG00000289418]] 2.03× (z +5.3, 9/10 lines), [[DNER]] 1.32× (z +5.1, 11/16 lines), [[CCBE1]] 1.23× (z +5.0, 12/20 lines), [[ADPRHL1]] 1.32× (z +4.7, 17/47 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (82 genes, none with an alert; 12 shown): [[PTGS2]] 0.654× (z -5.0, 7/21 lines), [[GJA1]] 0.688× (z -4.9, 10/22 lines), [[INHBA]] 0.576× (z -4.8, 6/16 lines), [[RIMS1]] 0.628× (z -4.7, 8/24 lines), [[IL1B]] 0.498× (z -4.5, 10/18 lines), [[PKIA]] 0.772× (z -4.5, 11/25 lines), [[IL6]] 0.518× (z -4.4, 11/16 lines), [[VSIG1]] 0.528× (z -4.4, 4/14 lines), [[NCKAP5]] 0.743× (z -4.3, 13/26 lines), [[CYP2S1]] 0.666× (z -4.2, 8/28 lines), [[CD274]] 0.747× (z -4.2, 9/29 lines), [[KIF5C]] 0.774× (z -4.1, 15/48 lines)

**0.5 µM** (179 genes, none with an alert; 12 shown): [[RBAK]] 0.691× (z -7.8, 35/48 lines), [[ENSG00000273149]] 0.405× (z -6.6, 23/29 lines), [[DSE]] 0.766× (z -6.5, 22/39 lines), [[ENSG00000278384]] 0.599× (z -6.0, 11/26 lines), [[MIA3]] 0.804× (z -5.9, 27/48 lines), [[ATP1B1]] 0.702× (z -5.5, 33/40 lines), [[TMF1]] 0.747× (z -5.4, 39/48 lines), [[MALAT1]] 0.743× (z -5.4, 46/48 lines), [[RASSF8]] 0.813× (z -5.3, 17/33 lines), [[ARHGAP29]] 0.786× (z -5.3, 19/38 lines), [[NPIPB14P]] 0.711× (z -5.1, 25/45 lines), [[E2F7]] 0.762× (z -5.0, 20/43 lines)

**5 µM** (69 genes, none with an alert; 12 shown): [[WNT7B]] 0.757× (z -5.1, 14/28 lines), [[PKIA]] 0.820× (z -4.8, 13/25 lines), [[FGF11]] 0.789× (z -4.7, 10/37 lines), [[PHLDA1]] 0.742× (z -4.7, 37/43 lines), [[CFAP46]] 0.662× (z -4.6, 5/21 lines), [[CD68]] 0.764× (z -4.5, 24/42 lines), [[MIAT]] 0.700× (z -4.5, 17/38 lines), [[CNOT3]] 0.822× (z -4.3, 22/48 lines), [[LIF]] 0.773× (z -4.2, 20/38 lines), [[RAPGEF3]] 0.746× (z -4.1, 10/40 lines), [[IL6]] 0.653× (z -4.1, 13/16 lines), [[RASGRP3]] 0.790× (z -4.0, 10/31 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | [[Module 194]] (+2.2) | — |
| 0.5 µM | [[Module 098]] (+3.2), [[Module 104]] (+2.3), [[Module 118]] (+2.1) | — |
| 5 µM | [[Module 194]] (+2.6), [[Module 098]] (+2.5) | — |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | [[NCI-H1573 (line)]] (2.12), [[A549 (line)]] (1.85), [[NCI-H1792 (line)]] (1.77), [[H4 (line)]] (1.65) · weakest: [[NCI-H661 (line)]] (0.168), [[A-427 (line)]] (0.596), [[KATO III (line)]] (0.610) |
| 0.5 µM | [[HCT15 (line)]] (-4.0), [[SW480 (line)]] (-3.7), [[NCI-H460 (line)]] (-3.6), [[C32 (line)]] (-3.2) | [[NCI-H1573 (line)]] (1.75), [[A549 (line)]] (1.42), [[NCI-H1792 (line)]] (1.40), [[H4 (line)]] (1.37) · weakest: [[SW480 (line)]] (0.431), [[SW1417 (line)]] (0.519), [[A-427 (line)]] (0.523) |
| 5 µM | — | [[NCI-H1573 (line)]] (2.21), [[A549 (line)]] (2.09), [[NCI-H1792 (line)]] (1.92), [[Hs 766T (line)]] (1.79) · weakest: [[SW48 (line)]] (0.380), [[NCI-H661 (line)]] (0.508), [[LS 180 (line)]] (0.527) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 1 next most similar without an alert.*

- [[Triamcinolone (drug)]] (+0.64, Glucocorticoid receptor agonist); [[Thymol (drug)]] (+0.59, unclear); [[Ipatasertib (drug)]] (+0.57, PI3K/AKT inhibitor); [[Lenalidomide (hemihydrate) (drug)]] (+0.57, unclear); [[Betamethasone dipropionate (drug)]] (+0.56, Glucocorticoid receptor agonist); [[Hydroxyurea (drug)]] (+0.55, DNA synthesis/repair inhibitor); [[Canagliflozin (drug)]] (+0.52, Glucose transporter inhibitor); [[Tubulin inhibitor 6 (drug)]] (+0.47, Microtubule inhibitor, ⚠ only 2 significant genes); [[Clobetasol propionate (drug)]] (+0.47, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[MTMR7]] | 0.5 µM | B | MTMR7 activity lowers the cells' numbers under Medroxyprogesterone acetate 0.5 µM (makes them more sensitive) | lines that do not express MTMR7 (16) vs lines expressing it (32) | the lines without MTMR7: 1.28× the cells of the other lines | 0.075 | ⚠ within organs, on part of the lines; also absent: GAP43, NRXN1, LOXL3; maybe low, not absent |
| [[INPP4B]] | 0.5 µM | B | INPP4B activity raises the cells' numbers under Medroxyprogesterone acetate 0.5 µM (protects the cells) | lines that do not express INPP4B (10) vs lines expressing it (38) | the lines without INPP4B: 0.76× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: RAB32, CD82, IFIT2 |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Medroxyprogesterone acetate"
- `tables/drugdoses.parquet` — dd in 660, 661, 662
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
