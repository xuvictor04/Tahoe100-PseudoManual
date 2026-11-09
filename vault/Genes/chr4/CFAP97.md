---
symbol: "CFAP97"
type: "gene"
col: 8928
ensembl_id: "ENSG00000164323"
name: "cilia and flagella associated protein 97"
location: "4q35.1"
module: 1
arm: "+"
pooled_cpm: 56.1
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 11
n_dd_up_clean: 6
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# CFAP97

*cilia and flagella associated protein 97* — 4q35.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.12× (z +11.5, q 5e-28, up in 42 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 1.78× (z +8.8, q 3e-16, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.582× (z -8.2, q 1e-13, down in 40 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.656× (z -6.4, q 5e-08, down in 35 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PEX1]] (+0.66, fdr 1e-05), [[LARS1]] (+0.65, fdr 1e-05), [[ATIC]] (+0.63, fdr 1e-05); moves opposite to [[COX6C]] (-0.59, fdr 1e-05), [[UBL5]] (-0.57, fdr 4e-05), [[NDUFA11]] (-0.57, fdr 6e-05, ⚠ NDUFA11 in the vector space only through flagged drug-doses), [[NDUFA4]] (-0.56, fdr 2e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 7 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8928.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.12×** | +11.5 | 5e-28 | 42/48 (A498, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.18×** | +11.5 | 5e-28 | 39/43 (A-427, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.78×** | +8.8 | 3e-16 | 39/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.61×** | +6.7 | 3e-09 | 29/45 (KATO III, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.29×** | +5.6 | 3e-06 | 25/48 (HOP62, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.42×** | +5.3 | 9e-06 | 35/48 (LOX-IMVI, A549, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.39×** | +4.9 | 8e-05 | 26/48 (HOP62, HCT15, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.36×** | +4.7 | 2e-04 | 28/48 (NCI-H1792, CFPAC-1, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.32×** | +4.1 | 0.002 | 24/48 (NCI-H1792, C32, …) | top dose only |  |
| [[Pralsetinib (drug)]] 5 µM |  | **1.59×** | +3.7 | 0.013 | 26/48 (NCI-H2030, HS-578T, …) | top dose only | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~54% of this change | **1.24×** | +3.3 | 0.044 | 23/48 (PANC-1, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | 1.16× | +3.1 | 0.076 | 10/48 (NCI-H460, SK-MEL-2, …) | top dose only |  |
| [[Sulfatinib (drug)]] 5 µM |  | **1.24×** | +3.1 | 0.076 | 18/48 (LoVo, A-427, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8928.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.582×** | -8.2 | 1e-13 | 40/47 (SW48, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.656×** | -6.4 | 5e-08 | 35/48 (LS 180, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.681×** | -5.8 | 1e-06 | 31/48 (PANC-1, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.717×** | -5.0 | 7e-05 | 30/48 (J82, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.731×** | -4.8 | 2e-04 | 29/48 (LS 180, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.550×** | -4.7 | 2e-04 | 33/49 (AN3 CA, NCI-H23, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **0.746×** | -4.4 | 7e-04 | 26/48 (RKO, A-427, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.607×** | -4.0 | 0.005 | 25/48 (A-427, NCI-H2030, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.775×** | -3.9 | 0.007 | 23/48 (LS 180, HCT15, …) | rises with dose |  |
| [[Resveratrol (drug)]] 0.5 µM |  | **0.779×** | -3.8 | 0.009 | 23/48 (SW 1088, SW480, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.780×** | -3.8 | 0.009 | 24/48 (NCI-H23, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.936× | -3.2 | 0.073 | 0/49 | inconsistent across doses |  |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | 0.812× | -3.0 | 0.11 | 15/48 (RKO, NCI-H460, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8928. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 31.6 | 5 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.52× (z +11.5) | — |
| [[PANC-1 (line)]] | alt | 87.1 | 2 (2 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.34× (z +10.9) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.487× (z -9.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.498× (z -9.2) |
| [[SW480 (line)]] | alt | 66.6 | 3 (2 ⚠) | 2 (1 ⚠) | [[Harringtonine (drug)]] 0.5 µM 2.59× (z +10.5) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.391× (z -10.3) |
| [[LS 180 (line)]] | wt | 61.8 | 0 | 4 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.299× (z -10.4) |
| [[HS-578T (line)]] | alt | 47.5 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.03× (z +9.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.08× (z +9.4) | — |
| [[J82 (line)]] | alt | 57.5 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.57× (z +9.0) ⚠ toxic; transcription drop | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.371× (z -9.3) |
| [[NCI-H1792 (line)]] | alt | 39.7 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.75× (z +10.6) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[NCI-H23 (line)]] | alt | 59.5 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.77× (z +9.2) ⚠ toxic; transcription drop | [[Dinaciclib (drug)]] 0.05 µM 0.321× (z -9.8) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 102 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.358× (z -9.0) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 66.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.88× (z +11.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.553× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 65.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.81× (z +12.2) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 80.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.44× (z +9.4) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 47.6 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.22× (z +8.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.573× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 42.1 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.239× (z -8.9) |
| [[SW48 (line)]] | wt | 75.3 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.202× (z -10.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.251× (z -9.2) |
| [[A549 (line)]] | wt | 42.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.32× (z +10.9) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 98.4 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.0805× (z -8.5) |
| [[C-33 A (line)]] | alt | 136 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.386× (z -8.7) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 39.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.51× (z +8.8) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[HEC-1-A (line)]] | alt | 70.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.30× (z +8.9) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 38.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.12× (z +8.8) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 51.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.33× (z +11.0) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 38.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.80× (z +8.6) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 32.7 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.303× (z -8.5) |
| [[SNU-423 (line)]] | alt | 31.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.82× (z +10.0) ⚠ toxic; transcription drop | — |
| [[SW 1271 (line)]] | alt | 61.6 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.120× (z -8.5) |
| [[SW1417 (line)]] | alt | 42.9 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.343× (z -9.0) |
| [[A-172 (line)]] | wt | 61.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 67.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 47.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 70.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 50.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 89.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 25.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 46.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 58.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 46.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 62.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 59.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 43.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 51.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 63.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 64.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 47.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 31.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8928), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PEX1]] | +0.66 | +0.67 / +0.55 | both halves | 1e-05 |  |
| [[LARS1]] | +0.65 | +0.68 / +0.57 | both halves | 1e-05 |  |
| [[ATIC]] | +0.63 | +0.70 / +0.52 | both halves | 1e-05 |  |
| [[AKAP11]] | +0.63 | +0.68 / +0.62 | both halves | 7e-06 |  |
| [[IMPACT]] | +0.62 | +0.64 / +0.51 | both halves | 1e-05 |  |
| [[THNSL1]] | +0.62 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[RIMOC1]] | +0.61 | +0.59 / +0.58 | both halves | 8e-06 |  |
| [[DCAF17]] | +0.60 | +0.67 / +0.40 | both halves | 5e-05 |  |
| [[MRPL30]] | +0.60 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[KARS1]] | +0.60 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[GUF1]] | +0.60 | +0.68 / +0.44 | both halves | 3e-05 |  |
| [[GTF3A]] ⚠ | +0.60 | +0.59 / +0.58 | both halves | 8e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[TMA16]] | +0.59 | +0.67 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COX6C]] | -0.59 | -0.58 / -0.49 | both halves | 1e-05 |  |
| [[UBL5]] | -0.57 | -0.60 / -0.41 | both halves | 4e-05 |  |
| [[NDUFA11]] ⚠ | -0.57 | -0.56 / -0.38 | both halves | 6e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[NDUFA4]] | -0.56 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[UQCRQ]] ⚠ | -0.56 | -0.50 / -0.46 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[MED31]] | -0.55 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[NEDD8]] | -0.55 | -0.57 / -0.37 | both halves | 7e-05 |  |
| [[COX6A1]] | -0.54 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[SEMA6C]] | -0.54 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[NDUFB11]] ⚠ | -0.53 | -0.55 / -0.37 | both halves | 8e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[MTCH1]] | -0.53 | -0.57 / -0.47 | both halves | 2e-05 |  |
| [[POLR2J3-1]] | -0.53 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[EGFL8]] | -0.52 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[SDHAP2]] | -0.51 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[ANKRD9]] | -0.51 | -0.42 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.513). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-31.1, -16.0); signed map (-0.6, -37.4). **Vector** length 112, 32.1% of its response variance represented; |z| ≥ 3 in 973 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +8.6 | +8.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +7.5 | +4.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +7.0 | +5.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.8 | +2.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | +3.8 | +4.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +3.5 | +2.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.7 | +2.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.4 | +2.1 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.3 | -8.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -4.0 | -5.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.9 | -2.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.7 | -6.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | -3.5 | -4.7 |
|  | [[PH-797804 (drug)]] 0.5 µM |  | -3.3 | -2.5 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | -2.7 | -1.8 |
|  | [[Bergenin (drug)]] 0.5 µM |  | -2.6 | -1.9 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | -2.4 | +0.5 |

## What is on record

|  |  |
|---|---|
| Name | cilia and flagella associated protein 97 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q35.1 — chr4:185,159,665-185,209,504 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp434F1728, hmw; previously KIAA1430 |
| Gene groups (HGNC) | Cilia and flagella associated |
| Matched by | ensembl_id |

UniProt [Q9P2B7](https://www.uniprot.org/uniprotkb/Q9P2B7) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:29276](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29276) · Entrez [57587](https://www.ncbi.nlm.nih.gov/gene/57587) · UniProt [Q9P2B7](https://www.uniprot.org/uniprotkb/Q9P2B7) · Ensembl [ENSG00000164323](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164323)

## Data

Gene col 8928: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8928); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8928, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8928]; `tensor/DDL_lfc|DDL_z.npy` [8928]; `embed/gene_vectors.npy` [8928]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8928 or target_col == 8928). Every well: [[CFAP97 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CFAP97.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
