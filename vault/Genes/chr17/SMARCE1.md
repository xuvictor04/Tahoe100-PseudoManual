---
symbol: "SMARCE1"
type: "gene"
col: 1053
ensembl_id: "ENSG00000073584"
name: "SWI/SNF related BAF chromatin remodeling complex subunit E1"
location: "17q21.2"
module: 28
arm: "+"
pooled_cpm: 95.13
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 16
n_dd_up_clean: 3
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# SMARCE1

*SWI/SNF related BAF chromatin remodeling complex subunit E1* — 17q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.31× (z +15.1, q 0e+00, up in 44 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 1.48× (z +7.4, q 2e-11, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.747× (z -7.2, q 3e-10, down in 34 of 49 measured lines) ⚠ cell-cycle shift, explains ~20% of this change. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 0.691× (z -6.9, q 2e-09, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RNF214]] (+0.80, fdr 7e-06), [[CCDC25]] (+0.80, fdr 7e-06), [[COPS5]] (+0.74, fdr 7e-06); moves opposite to [[TOR1B]] (-0.64, fdr 1e-05), [[MBOAT7]] (-0.61, fdr 7e-06), [[RABGEF1P1]] (-0.60, fdr 7e-06).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CFL2]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 8 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1053.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.31×** | +15.1 | 0e+00 | 44/44 (MIA PaCa-2, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.22×** | +15.0 | 0e+00 | 46/49 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.71×** | +9.3 | 4e-18 | 38/45 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.48×** | +7.4 | 2e-11 | 39/48 (PANC-1, A498, …) | two highest doses | cell-cycle shift (explains ~16% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.45×** | +6.7 | 2e-09 | 35/48 (LoVo, A498, …) | two highest doses | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.40×** | +6.3 | 3e-08 | 36/48 (A498, PANC-1, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.31×** | +5.2 | 2e-05 | 32/48 (LOX-IMVI, PANC-1, …) | all doses, flat |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~54% of this change | **1.31×** | +5.1 | 3e-05 | 32/48 (SW 900, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.21×** | +5.0 | 4e-05 | 24/48 (A498, PANC-1, …) | all doses, flat | composition shift |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.52×** | +4.1 | 0.002 | 31/47 (PANC-1, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.39×** | +3.2 | 0.063 | 22/47 (A-172, LS 180, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1053.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.747×** | -7.2 | 3e-10 | 34/49 (NCI-H460, Hs 766T, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.691×** | -6.9 | 2e-09 | 41/48 (NCI-H460, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.698×** | -6.7 | 5e-09 | 37/48 (NCI-H460, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.722×** | -6.0 | 2e-07 | 43/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.726×** | -5.9 | 3e-07 | 30/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.747×** | -5.2 | 2e-05 | 31/48 (NCI-H460, LS 180, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.767×** | -4.9 | 8e-05 | 27/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.782×** | -4.6 | 4e-04 | 25/48 (NCI-H460, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.787×** | -4.4 | 6e-04 | 29/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.795×** | -4.2 | 0.001 | 25/48 (SW480, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.809×** | -3.9 | 0.004 | 25/48 (NCI-H2347, SNU-423, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.857× | -3.8 | 0.008 | 20/48 (NCI-H460, A-172, …) | rises with dose |  |
| [[Cepharanthine (drug)]] 5 µM |  | 0.866× | -3.6 | 0.014 | 10/48 (SNU-1, NCI-H460, …) | top dose only | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.824×** | -3.6 | 0.015 | 23/48 (A-172, BT-474, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~5% of this change | **0.828×** | -3.5 | 0.019 | 21/48 (AN3 CA, SW1417, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.832×** | -3.4 | 0.024 | 18/49 (CHP-212, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.724×** | -3.1 | 0.055 | 22/49 (NCI-H460, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.730×** | -3.1 | 0.067 | 19/48 (MIA PaCa-2, Hs 766T, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, +0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1053. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 101 | 2 (2 ⚠) | 7 (3 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.63× (z +13.9) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.515× (z -12.9) ⚠ cell-cycle shift, explains ~20% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.493× (z -10.1) |
| [[SW480 (line)]] | alt | 118 | 3 (3 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.07× (z +16.4) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.389× (z -13.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.491× (z -10.4) |
| [[A498 (line)]] | wt | 125 | 6 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.20× (z +15.8) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 1.88× (z +8.6) | — |
| [[PANC-1 (line)]] | alt | 104 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.70× (z +15.2) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 1.88× (z +9.6) | — |
| [[J82 (line)]] | alt | 78.6 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.48× (z +10.4) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.443× (z -9.3) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 108 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.96× (z +13.6) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 113 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.05× (z +9.8) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 77.3 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.95× (z +10.3) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.385× (z -12.4) ⚠ cell-cycle shift, explains ~20% of this change |
| [[MIA PaCa-2 (line)]] | alt | 73.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.51× (z +15.9) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 94.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.25× (z +13.5) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 105 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.24× (z +9.2) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 121 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.13× (z +11.3) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 125 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.35× (z +11.0) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 88.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.61× (z +11.0) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 80.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.68× (z +11.0) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 65.2 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.402× (z -9.4) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.404× (z -9.3) |
| [[LoVo (line)]] | wt | 80.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.47× (z +10.1) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 101 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.17× (z +8.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 2.13× (z +8.6) | — |
| [[NCI-H1792 (line)]] | alt | 66.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.69× (z +12.9) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 107 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.485× (z -9.4) |
| [[SW 1088 (line)]] | alt | 75.5 | 0 | 2 | — | [[Radotinib (drug)]] 0.5 µM 0.0808× (z -9.2) |
| [[BT-474 (line)]] | alt | 67.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.51× (z +8.5) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 117 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.01× (z +8.7) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 115 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.78× (z +10.0) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 121 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.08× (z +9.9) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 85.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.45× (z +9.6) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 118 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +10.0) ⚠ cell-cycle shift, would explain all of this change | — |
| [[RKO (line)]] | wt | 98.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.39× (z +9.6) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 90.5 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.489× (z -9.2) |
| [[SW48 (line)]] | wt | 108 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.03× (z +9.2) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 128 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 49.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 75.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 219 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 70.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 82.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 67.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 73.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 68.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 88.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 78.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 86.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 65.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 88.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 66.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 94.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 99.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 62.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1053), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF214]] | +0.80 | +0.78 / +0.78 | both halves | 7e-06 |  |
| [[CCDC25]] | +0.80 | +0.79 / +0.66 | both halves | 7e-06 |  |
| [[COPS5]] | +0.74 | +0.77 / +0.67 | both halves | 7e-06 |  |
| [[PEX1]] | +0.73 | +0.74 / +0.59 | both halves | 7e-06 |  |
| [[AASDHPPT]] | +0.73 | +0.75 / +0.66 | both halves | 7e-06 |  |
| [[TRUB1]] | +0.71 | +0.76 / +0.65 | both halves | 7e-06 |  |
| [[FUNDC1]] | +0.71 | +0.77 / +0.61 | both halves | 7e-06 |  |
| [[DDX1]] | +0.71 | +0.74 / +0.64 | both halves | 7e-06 |  |
| [[NDUFA5]] | +0.70 | +0.69 / +0.67 | both halves | 7e-06 |  |
| [[TMEM128]] | +0.69 | +0.74 / +0.58 | both halves | 7e-06 |  |
| [[VPS72]] | +0.67 | +0.66 / +0.63 | both halves | 7e-06 | pathway: Chromatin modifying enzymes |
| [[YTHDC2]] | +0.67 | +0.66 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TOR1B]] | -0.64 | -0.56 / -0.65 | both halves | 1e-05 |  |
| [[MBOAT7]] | -0.61 | -0.59 / -0.61 | both halves | 7e-06 |  |
| [[RABGEF1P1]] | -0.60 | -0.61 / -0.58 | both halves | 7e-06 |  |
| [[CD81]] | -0.59 | -0.61 / -0.56 | both halves | 1e-05 |  |
| [[PDXK]] | -0.59 | -0.62 / -0.58 | both halves | 7e-06 |  |
| [[CSNK1G2]] | -0.59 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[POM121]] | -0.59 | -0.61 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CFL2]] | C | CFL2 activity raises SMARCE1's level | lines that do not express CFL2 (4) vs lines expressing it (45) | 1.40× lower at baseline in the lines without CFL2 | 0.060 | ⚠ few lines (4 vs 45); within organs, on part of the lines; also absent: TPST1, SLC35F1, ITGA2B; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.830). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-25.1, 3.8); signed map (7.0, -26.3). **Vector** length 113, 35.3% of its response variance represented; |z| ≥ 3 in 883 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +9.5 | +5.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | +8.8 | +6.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | +7.3 | +6.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.9 | +7.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.8 | +5.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.6 | +2.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.0 | +1.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +2.7 | +0.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.6 | +2.5 |
| fall | [[Auranofin (drug)]] 5 µM |  | -6.7 | -3.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.4 | -5.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | -5.7 | -7.2 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -4.7 | -4.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -4.6 | -5.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.3 | -1.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.0 | -2.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.8 | -3.8 |
|  | [[Thymol (drug)]] 0.5 µM |  | -2.6 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | SWI/SNF related BAF chromatin remodeling complex subunit E1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.2 — chr17:40,624,962-40,648,654 (-) |
| Ensembl biotype | protein_coding |
| Also known as | BAF57 |
| Gene groups (HGNC) | BAF complex subunits; PBAF complex subunits |
| Reactome | 21 pathways, smallest: Formation of the canonical BAF (cBAF) complex; Formation of the polybromo-BAF (pBAF) complex; Formation of the embryonic stem cell BAF (esBAF) complex |
| Matched by | ensembl_id |

**Function**, from UniProt [Q969G3](https://www.uniprot.org/uniprotkb/Q969G3) (SWI/SNF-related matrix-associated actin-dependent regulator of chromatin subfamily E member 1):

> Involved in transcriptional activation and repression of select genes by chromatin remodeling (alteration of DNA-nucleosome topology). Component of SWI/SNF chromatin remodeling complexes that carry out key enzymatic activities, changing chromatin structure by altering DNA-histone contacts within a nucleosome in an ATP-dependent manner. Belongs to the neural progenitors-specific chromatin remodeling complex (npBAF complex) and the neuron-specific chromatin remodeling complex (nBAF complex). …

**Summary**, from NCBI Gene [6605](https://www.ncbi.nlm.nih.gov/gene/6605):

> The protein encoded by this gene is part of the large ATP-dependent chromatin remodeling complex SWI/SNF, which is required for transcriptional activation of genes normally repressed by chromatin. The encoded protein, either alone or when in the SWI/SNF complex, can bind to 4-way junction DNA, which is thought to mimic the topology of DNA as it enters or exits the nucleosome. The protein contains a DNA-binding HMG domain, but disruption of this domain does not abolish the DNA-binding or …

**Accessions** — [HGNC:11109](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11109) · Entrez [6605](https://www.ncbi.nlm.nih.gov/gene/6605) · UniProt [Q969G3](https://www.uniprot.org/uniprotkb/Q969G3) · Ensembl [ENSG00000073584](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000073584)

## Data

Gene col 1053: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1053); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1053, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1053]; `tensor/DDL_lfc|DDL_z.npy` [1053]; `embed/gene_vectors.npy` [1053]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1053 or target_col == 1053). Every well: [[SMARCE1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SMARCE1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
