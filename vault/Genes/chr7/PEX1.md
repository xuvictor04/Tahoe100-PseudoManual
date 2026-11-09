---
symbol: "PEX1"
type: "gene"
col: 4851
ensembl_id: "ENSG00000127980"
name: "peroxisomal biogenesis factor 1"
location: "7q21.2"
module: 28
arm: "+"
pooled_cpm: 23.17
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 12
n_dd_up_clean: 16
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# PEX1

*peroxisomal biogenesis factor 1* — 7q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.82× (z +13.0, q 5e-36, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.375× (z -15.1, q 0e+00, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AASDHPPT]] (+0.81, fdr 7e-06), [[CCDC113]] (+0.74, fdr 7e-06), [[ZNF510]] (+0.73, fdr 7e-06); moves opposite to [[CD81]] (-0.67, fdr 7e-06), [[NEDD8]] (-0.67, fdr 1e-05), [[UBL5]] (-0.63, fdr 2e-05).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CCDC113]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4851.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.82×** | +13.0 | 5e-36 | 39/48 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.96×** | +10.3 | 1e-22 | 41/48 (A498, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.91×** | +10.0 | 5e-21 | 41/48 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.93×** | +9.7 | 4e-20 | 34/48 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.87×** | +9.6 | 7e-20 | 41/48 (A498, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.69×** | +8.1 | 6e-14 | 41/48 (A498, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.63×** | +7.5 | 5e-12 | 37/48 (A498, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.42×** | +5.4 | 6e-06 | 25/48 (LoVo, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.88×** | +5.1 | 2e-05 | 30/48 (A498, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.39×** | +4.9 | 5e-05 | 22/44 (NCI-H1573, COLO 205, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.34×** | +4.5 | 4e-04 | 19/42 (HCT15, NCI-H2347, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.32×** | +4.2 | 0.001 | 15/47 (CFPAC-1, A-172, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.31×** | +4.1 | 0.002 | 22/47 (SW48, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.31×** | +4.1 | 0.002 | 22/48 (CFPAC-1, BT-474, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.21×** | +4.1 | 0.002 | 15/48 (A498, NCI-H2347, …) | rises with dose | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.29×** | +3.9 | 0.003 | 15/48 (HEC-1-A, LoVo, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.28×** | +3.6 | 0.011 | 10/47 (C32, NCI-H23, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.25×** | +3.4 | 0.024 | 13/48 (A498, Hs 766T, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.24×** | +3.3 | 0.024 | 4/48 (Panc 03.27, HEC-1-A, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4851.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.375×** | -15.1 | 0e+00 | 44/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.385×** | -14.7 | 0e+00 | 42/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.422×** | -13.3 | 4e-38 | 44/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.502×** | -10.6 | 3e-24 | 40/47 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.638×** | -6.9 | 5e-10 | 29/47 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.490×** | -5.7 | 9e-07 | 23/48 (SW480, Panc 03.27, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.555×** | -4.7 | 2e-04 | 23/48 (A-427, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.737×** | -4.7 | 2e-04 | 21/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.694×** | -4.0 | 0.004 | 17/48 (C-33 A, RKO, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **0.773×** | -3.8 | 0.007 | 12/48 (PANC-1, C-33 A, …) | top dose only | plate-row cell shift; position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.842× | -3.8 | 0.009 | 15/48 (MIA PaCa-2, Panc 03.27, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.808×** | -3.3 | 0.044 | 16/48 (HT-29, NCI-H460, …) | rises with dose |  |
| [[Allopurinol (drug)]] 0.05 µM |  | **0.808×** | -3.3 | 0.044 | 7/48 (A-172, NCI-H661, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4851. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 42.2 | 2 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +14.6) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.204× (z -17.9) |
| [[A-427 (line)]] | wt | 25.7 | 1 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.74× (z +10.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.131× (z -15.5) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.0825× (z -9.9) |
| [[NCI-H460 (line)]] | wt | 24.1 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.259× (z -11.5) |
| [[PANC-1 (line)]] | alt | 26.3 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.178× (z -17.0) |
| [[LoVo (line)]] | wt | 39.2 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +16.0) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.417× (z -9.3) |
| [[HEC-1-A (line)]] | alt | 17.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +10.8) | — |
| [[HT-29 (line)]] | alt | 24.1 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.155× (z -13.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.247× (z -10.0) |
| [[LS 180 (line)]] | wt | 22.8 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.237× (z -9.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.277× (z -8.6) |
| [[NCI-H1573 (line)]] | alt | 23.2 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.141× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.293× (z -9.3) |
| [[NCI-H23 (line)]] | alt | 28.8 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.216× (z -11.7) |
| [[SNU-1 (line)]] | wt | 18.4 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.103× (z -10.2) |
| [[SW48 (line)]] | wt | 28.3 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0879× (z -12.1) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 0.05 µM 0.130× (z -9.6) |
| [[A498 (line)]] | wt | 15.9 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.81× (z +9.1) | — |
| [[AN3 CA (line)]] | alt | 59.3 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.144× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 20.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.167× (z -9.4) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 27.0 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.213× (z -9.4) |
| [[HCT15 (line)]] | alt | 21.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.134× (z -10.3) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 24.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.219× (z -9.8) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 11.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +9.8) | — |
| [[RKO (line)]] | wt | 32.7 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.305× (z -8.5) |
| [[RPMI-7951 (line)]] | alt | 15.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.188× (z -8.8) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 16.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.142× (z -10.3) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 32.3 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.282× (z -10.7) |
| [[A-172 (line)]] | wt | 22.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.32 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 31.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 23.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 34.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4851), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AASDHPPT]] | +0.81 | +0.89 / +0.75 | both halves | 7e-06 |  |
| [[CCDC113]] | +0.74 | +0.76 / +0.75 | both halves | 7e-06 |  |
| [[ZNF510]] | +0.73 | +0.77 / +0.67 | both halves | 7e-06 |  |
| [[SMARCE1]] | +0.73 | +0.74 / +0.59 | both halves | 7e-06 |  |
| [[IMPACT]] | +0.70 | +0.71 / +0.62 | both halves | 7e-06 |  |
| [[ZNF252P-1]] | +0.69 | +0.79 / +0.60 | both halves | 7e-06 |  |
| [[CCDC25]] | +0.69 | +0.81 / +0.52 | both halves | 1e-05 |  |
| [[CFAP97]] | +0.66 | +0.67 / +0.55 | both halves | 1e-05 |  |
| [[DIS3L]] | +0.66 | +0.77 / +0.65 | both halves | 7e-06 |  |
| [[CCT6P3]] | +0.66 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[C12orf29]] | +0.66 | +0.75 / +0.64 | both halves | 7e-06 |  |
| [[THAP5]] | +0.65 | +0.74 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CD81]] | -0.67 | -0.73 / -0.60 | both halves | 7e-06 |  |
| [[NEDD8]] | -0.67 | -0.68 / -0.49 | both halves | 1e-05 |  |
| [[UBL5]] | -0.63 | -0.67 / -0.47 | both halves | 2e-05 |  |
| [[MBOAT7]] | -0.63 | -0.71 / -0.57 | both halves | 1e-05 |  |
| [[UQCRH]] | -0.60 | -0.75 / -0.45 | both halves | 3e-05 |  |
| [[SNHG30]] | -0.60 | -0.65 / -0.49 | both halves | 1e-05 |  |
| [[COX6C]] | -0.57 | -0.62 / -0.40 | both halves | 5e-05 |  |
| [[SAR1A]] | -0.57 | -0.63 / -0.57 | both halves | 8e-06 |  |
| [[FKBP11]] | -0.57 | -0.45 / -0.57 | both halves | 3e-05 |  |
| [[TNPO3]] | -0.57 | -0.69 / -0.51 | both halves | 1e-05 |  |
| [[QSOX1]] | -0.57 | -0.67 / -0.62 | both halves | 7e-06 |  |
| [[MTCH1]] | -0.56 | -0.49 / -0.57 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCDC113]] | C | CCDC113 activity raises PEX1's level | lines that do not express CCDC113 (3) vs lines expressing it (47) | 1.63× lower at baseline in the lines without CCDC113 | 0.084 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: DNMT3B, DBNDD1, SPDL1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.743). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-26.3, 3.3); signed map (6.4, -27.3). **Vector** length 79.8, 17.3% of its response variance represented; |z| ≥ 3 in 1,079 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.1 | +10.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.7 | +9.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.4 | +13.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +6.0 | +5.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.3 | +3.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.8 | +3.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.4 | +0.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.3 | +1.3 |
|  | [[Erlotinib (drug)]] 5 µM |  | +1.3 | +1.1 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -5.3 | +1.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.2 | -14.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -4.3 | -15.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.7 | +0.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.6 | -10.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.5 | +0.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.4 | -1.6 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -2.2 | -4.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.2 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | peroxisomal biogenesis factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q21.2 — chr7:92,487,020-92,528,520 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously ZWS1, ZWS |
| Gene groups (HGNC) | AAA ATPases; Peroxins |
| Hallmark sets | BILE_ACID_METABOLISM |
| Reactome | 2 pathways, smallest: Peroxisomal protein import; Protein localization |
| Matched by | ensembl_id |

**Function**, from UniProt [O43933](https://www.uniprot.org/uniprotkb/O43933) (Peroxisomal ATPase PEX1):

> Component of the PEX1-PEX6 AAA ATPase complex, a protein dislocase complex that mediates the ATP-dependent extraction of the PEX5 receptor from peroxisomal membranes, an essential step for PEX5 recycling. Specifically recognizes PEX5 monoubiquitinated at 'Cys-11', and pulls it out of the peroxisome lumen through the PEX2-PEX10-PEX12 retrotranslocation channel. Extraction by the PEX1-PEX6 AAA ATPase complex is accompanied by unfolding of the TPR repeats and release of bound cargo from PEX5.

**Summary**, from NCBI Gene [5189](https://www.ncbi.nlm.nih.gov/gene/5189):

> This gene encodes a member of the AAA ATPase family, a large group of ATPases associated with diverse cellular activities. This protein is cytoplasmic but is often anchored to a peroxisomal membrane where it forms a heteromeric complex and plays a role in the import of proteins into peroxisomes and peroxisome biogenesis. Mutations in this gene have been associated with complementation group 1 peroxisomal disorders such as neonatal adrenoleukodystrophy, infantile Refsum disease, and Zellweger …

**Accessions** — [HGNC:8850](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8850) · Entrez [5189](https://www.ncbi.nlm.nih.gov/gene/5189) · UniProt [O43933](https://www.uniprot.org/uniprotkb/O43933) · Ensembl [ENSG00000127980](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000127980)

## Data

Gene col 4851: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4851); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4851, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4851]; `tensor/DDL_lfc|DDL_z.npy` [4851]; `embed/gene_vectors.npy` [4851]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4851 or target_col == 4851). Every well: [[PEX1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PEX1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
