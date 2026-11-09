---
symbol: "PLPP1"
type: "gene"
col: 850
ensembl_id: "ENSG00000067113"
name: "phospholipid phosphatase 1"
location: "5q11.2"
module: 59
arm: "+"
pooled_cpm: 63.91
n_lines_expressing: 49
n_dd_up: 19
n_dd_down: 11
n_dd_up_clean: 18
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 3
direction_downstream: 1
tags: ["gene", "module/059"]
generated_by: "tahoemap"
---

# PLPP1

*phospholipid phosphatase 1* — 5q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.37× (z +10.2, q 2e-21, up in 28 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.437× (z -18.3, q 0e+00, down in 33 of 41 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.469× (z -17.4, q 0e+00, down in 43 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCDC24]] (+0.58, fdr 1e-05), [[LACTB]] (+0.55, fdr 1e-05), [[TRIM36]] (+0.55, fdr 1e-05); moves opposite to [[TTN-AS1]] (-0.53, fdr 2e-04), [[DNAH1]] (-0.51, fdr 4e-05), [[EBNA1BP2]] (-0.51, fdr 6e-05).
> It sits in the **+** arm of [[Module 059]] (Amino acids regulate mTORC1).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[RNF220]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[Everolimus (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 7 with an alert ⚠; shown: the 15 strongest. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 850.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.37×** | +10.2 | 2e-21 | 28/47 (CFPAC-1, J82, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.31×** | +8.8 | 5e-16 | 31/47 (LoVo, HEC-1-A, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.28×** | +6.9 | 1e-09 | 30/47 (NCI-H460, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.32×** | +6.4 | 2e-08 | 29/47 (LoVo, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.33×** | +6.3 | 3e-08 | 26/46 (NCI-H460, LoVo, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.31×** | +6.2 | 4e-08 | 30/47 (SW480, LoVo, …) | all doses, flat | cell-cycle shift (explains ~8% here) |
| [[Trametinib (drug)]] 5 µM |  | **1.31×** | +6.1 | 8e-08 | 28/49 (NCI-H460, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~8% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.32×** | +6.0 | 1e-07 | 23/47 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.31×** | +5.9 | 2e-07 | 27/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.62×** | +5.5 | 2e-06 | 25/48 (LoVo, NCI-H2347, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 1.18× | +5.1 | 2e-05 | 18/47 (NCI-H460, AsPC-1, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.20× | +4.8 | 9e-05 | 18/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.25×** | +4.7 | 9e-05 | 20/47 (NCI-H460, SW480, …) | all doses, flat |  |
| [[RMC-6236 (drug)]] 5 µM |  | **1.50×** | +4.6 | 2e-04 | 17/47 (NCI-H460, SW480, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.22×** | +4.5 | 2e-04 | 21/48 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 7 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 850.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.437×** | -18.3 | 0e+00 | 33/41 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.469×** | -17.4 | 0e+00 | 43/47 (MIA PaCa-2, Hs 766T, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.476×** | -17.1 | 0e+00 | 39/48 (A-427, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.490×** | -15.2 | 0e+00 | 35/45 (NCI-H2030, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.706×** | -8.0 | 1e-13 | 36/47 (PANC-1, H4, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~19% here) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | 0.860× | -5.0 | 7e-05 | 15/47 (RPMI-7951, PANC-1, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.672×** | -4.6 | 4e-04 | 23/48 (NCI-H1792, A549, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.675×** | -4.5 | 5e-04 | 21/47 (SNU-1, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.828×** | -4.4 | 8e-04 | 19/47 (CFPAC-1, J82, …) | two highest doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~21% of this change | **0.827×** | -4.2 | 0.001 | 16/46 (HepG2/C3A, C32, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.835× | -4.0 | 0.003 | 18/47 (SNU-423, J82, …) | top dose only |  |
| [[Sulfatinib (drug)]] 5 µM |  | 0.856× | -3.5 | 0.025 | 14/47 (NCI-H2347, A549, …) | top dose only |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.819×** | -3.3 | 0.048 | 16/47 (SW48, SHP-77, …) | two highest doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.759×** | -3.2 | 0.063 | 10/36 (SW480, A-172, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 850. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 91.1 | 12 (1 ⚠) | 1 (1 ⚠) | [[Binimetinib (drug)]] 5 µM 3.11× (z +14.3) | [[Dinaciclib (drug)]] 0.5 µM 0.430× (z -10.6) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 42.9 | 7 | 0 | [[Trametinib (drug)]] 0.5 µM 2.37× (z +11.8) | — |
| [[AsPC-1 (line)]] | alt | 67.5 | 4 | 2 (2 ⚠) | [[Trametinib (drug)]] 5 µM 3.19× (z +11.4) | [[Dinaciclib (drug)]] 0.5 µM 0.336× (z -10.6) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 50.6 | 2 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +10.3) | [[Dinaciclib (drug)]] 5 µM 0.182× (z -19.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.364× (z -11.9) |
| [[PANC-1 (line)]] | alt | 83.0 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.274× (z -20.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.469× (z -11.9) |
| [[Hs 766T (line)]] | wt | 161 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.217× (z -13.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.237× (z -12.5) |
| [[HT-29 (line)]] | alt | 49.9 | 1 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.197× (z -14.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.323× (z -10.2) |
| [[NCI-H2347 (line)]] | alt | 66.3 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +11.2) | [[Dinaciclib (drug)]] 0.05 µM 0.335× (z -11.4) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 82.8 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.141× (z -19.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.401× (z -10.0) |
| [[A-427 (line)]] | wt | 118 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.127× (z -24.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.404× (z -10.6) |
| [[J82 (line)]] | alt | 44.1 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +14.5) | [[Dinaciclib (drug)]] 5 µM 0.371× (z -9.5) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 114 | 1 (1 ⚠) | 3 (2 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.63× (z +19.0) ⚠ position not correctable | [[Auranofin (drug)]] 5 µM 0.268× (z -14.5) |
| [[NCI-H661 (line)]] | alt | 682 | 0 | 4 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.228× (z -11.4) ⚠ cell-cycle shift, explains ~17% of this change |
| [[C32 (line)]] | wt | 82.3 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.199× (z -16.4) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 46.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +10.5) | — |
| [[NCI-H2030 (line)]] | alt | 66.5 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.151× (z -20.0) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 66.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +12.2) | [[Dinaciclib (drug)]] 5 µM 0.409× (z -9.7) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 94.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.293× (z -16.3) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 74.3 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.296× (z -10.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.377× (z -8.6) |
| [[CFPAC-1 (line)]] | alt | 52.1 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +15.4) | [[Dinaciclib (drug)]] 0.5 µM 0.394× (z -9.3) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 360 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.118× (z -9.4) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 53.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.257× (z -9.1) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 83.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.243× (z -14.3) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 52.5 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.158× (z -19.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.322× (z -12.1) |
| [[SHP-77 (line)]] | alt | 67.0 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.329× (z -10.3) |
| [[SNU-1 (line)]] | wt | 53.1 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.211× (z -10.3) ⚠ toxic; transcription drop · without an alert: [[PH-797804 (drug)]] 5 µM 0.0768× (z -9.1) |
| [[SNU-423 (line)]] | alt | 58.6 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.335× (z -10.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.371× (z -10.3) |
| [[SW 1271 (line)]] | alt | 93.2 | 0 | 2 (2 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.134× (z -9.3) ⚠ transcription drop |
| [[AN3 CA (line)]] | alt | 106 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.255× (z -8.6) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 46.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +11.0) | — |
| [[H4 (line)]] | wt | 49.7 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.235× (z -9.5) ⚠ transcription drop |
| [[HepG2_C3A (line)]] | wt | 40.3 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.250× (z -9.2) ⚠ toxic; cell-cycle shift, explains ~21% of this change |
| [[HOP62 (line)]] | alt | 28.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +10.6) | — |
| [[HS-578T (line)]] | alt | 66.8 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.532× (z -8.9) ⚠ cell-cycle shift, explains ~17% of this change |
| [[hTERT-HPNE (line)]] | wt | 48.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.83× (z +10.5) | — |
| [[KATO III (line)]] | alt | 24.4 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.24× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~77% of this change | — |
| [[Panc 03.27 (line)]] | alt | 45.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +11.2) | — |
| [[RPMI-7951 (line)]] | alt | 49.2 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.293× (z -11.3) |
| [[SW 900 (line)]] | alt | 48.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +14.1) | — |
| [[SW1417 (line)]] | alt | 18.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +9.9) | — |
| [[SW48 (line)]] | wt | 42.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.187× (z -10.0) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 8.88 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 44.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 51.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 62.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 49.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 68.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 67.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 850), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC24]] | +0.58 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[LACTB]] | +0.55 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[TRIM36]] | +0.55 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[RAB30]] | +0.54 | +0.46 / +0.56 | both halves | 2e-05 |  |
| [[KIF13A]] | +0.54 | +0.44 / +0.45 | both halves | 3e-05 |  |
| [[CNTNAP1]] | +0.54 | +0.55 / +0.45 | both halves | 3e-05 |  |
| [[NCOA1]] | +0.53 | +0.59 / +0.46 | both halves | 3e-05 |  |
| [[PGM2L1]] | +0.53 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[LCA5]] | +0.53 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[DIPK1A]] | +0.52 | +0.42 / +0.60 | both halves | 4e-05 |  |
| [[DENND5A]] | +0.52 | +0.37 / +0.46 | both halves | 8e-05 | pathway: HALLMARK_IL2_STAT5_SIGNALING |
| [[MRTFA]] | +0.51 | +0.43 / +0.57 | both halves | 3e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TTN-AS1]] | -0.53 | -0.32 / -0.50 | both halves | 2e-04 |  |
| [[DNAH1]] | -0.51 | -0.42 / -0.55 | both halves | 4e-05 |  |
| [[EBNA1BP2]] | -0.51 | -0.44 / -0.38 | both halves | 6e-05 | same gene group |
| [[SMG1P6]] | -0.51 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[EIPR1]] | -0.50 | -0.53 / -0.46 | both halves | 3e-05 |  |
| [[PSMD12]] | -0.50 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[LINC02320]] | -0.48 | -0.49 / -0.46 | both halves | 3e-05 |  |
| [[MINAR1]] | -0.48 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[COG8]] | -0.48 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[ATG16L1]] | -0.48 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[RAPGEF3]] | -0.47 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[LINC02458]] | -0.47 | -0.47 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RNF220]] | B | RNF220 activity raises PLPP1's level | lines that do not express RNF220 (9) vs lines expressing it (41) | 1.31× lower at baseline in the lines without RNF220 | 0.063 | ⚠ within organs, on part of the lines; also absent: GNAZ, ENSG00000287400, CTXN1; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity lowers PLPP1's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.4% of all compounds | 0.067 | ⚠ off-target possible; 3 compounds |
| [[CNTNAP1]] | C | CNTNAP1 activity raises PLPP1's level | lines that do not express CNTNAP1 (4) vs lines expressing it (46) | 2.70× lower at baseline in the lines without CNTNAP1 | 0.071 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZCCHC24, KIF17, SLC29A4 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Everolimus (drug)]] 5 µM | C | PLPP1's natural level raises the cells' numbers under Everolimus 5 µM (protects the cells) | PLPP1's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.70 | 0.268 over the table, 0.049 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 059]] — Amino acids regulate mTORC1; 80 genes; this gene is in the **+** arm (projection on the module's main direction 0.498). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (19.8, -8.4); signed map (-8.4, 14.1). **Vector** length 109, 29.1% of its response variance represented; |z| ≥ 3 in 1,351 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.8 | +8.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.5 | +6.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +6.4 | +6.9 |
|  | [[Trametinib (drug)]] 5 µM |  | +5.9 | +6.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | +5.6 | +5.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +5.4 | +4.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +5.3 | +6.0 |
| fall | [[Auranofin (drug)]] 5 µM |  | -9.8 | -17.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | -5.3 | -4.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -5.0 | -4.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.0 | -15.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.5 | -18.3 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -2.3 | -0.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.3 | -4.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.2 | -4.0 |

## What is on record

|  |  |
|---|---|
| Name | phospholipid phosphatase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q11.2 — chr5:55,424,854-55,534,969 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PAP-2a, LPP1; previously PPAP2A |
| Gene groups (HGNC) | Phospholipid phosphatases; MicroRNA protein coding host genes |
| Hallmark sets | ANDROGEN_RESPONSE, IL2_STAT5_SIGNALING |
| Reactome | 3 pathways, smallest: Sphingolipid catabolism; Sphingolipid metabolism; Metabolism of lipids |
| Matched by | ensembl_id |

**Function**, from UniProt [O14494](https://www.uniprot.org/uniprotkb/O14494) (Phospholipid phosphatase 1):

> Magnesium-independent phospholipid phosphatase of the plasma membrane that catalyzes the dephosphorylation of a variety of glycerolipid and sphingolipid phosphate esters including phosphatidate/PA, lysophosphatidate/LPA, diacylglycerol pyrophosphate/DGPP, sphingosine 1-phosphate/S1P and ceramide 1-phosphate/C1P. Also acts on N-oleoyl ethanolamine phosphate/N-(9Z-octadecenoyl)-ethanolamine phosphate, a potential physiological compound. Through its extracellular phosphatase activity allows both …

**Summary**, from NCBI Gene [8611](https://www.ncbi.nlm.nih.gov/gene/8611):

> The protein encoded by this gene is a member of the phosphatidic acid phosphatase (PAP) family. PAPs convert phosphatidic acid to diacylglycerol, and function in synthesis of glycerolipids and in phospholipase D-mediated signal transduction. This enzyme is an integral membrane glycoprotein that plays a role in the hydrolysis and uptake of lipids from extracellular space. Alternate splicing results in multiple transcript variants of this gene. [provided by RefSeq, May 2013]

**Accessions** — [HGNC:9228](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9228) · Entrez [8611](https://www.ncbi.nlm.nih.gov/gene/8611) · UniProt [O14494](https://www.uniprot.org/uniprotkb/O14494) · Ensembl [ENSG00000067113](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000067113)

## Data

Gene col 850: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 850); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 850, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 850]; `tensor/DDL_lfc|DDL_z.npy` [850]; `embed/gene_vectors.npy` [850]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 850 or target_col == 850). Every well: [[PLPP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLPP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
