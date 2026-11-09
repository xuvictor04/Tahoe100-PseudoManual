---
symbol: "LRRC58"
type: "gene"
col: 8688
ensembl_id: "ENSG00000163428"
name: "leucine rich repeat containing 58"
location: "3q13.33"
module: 25
arm: "+"
pooled_cpm: 119.04
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 0
n_dd_up_clean: 10
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# LRRC58

*leucine rich repeat containing 58* — 3q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (15 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.60× (z +14.6, q 3e-45, up in 43 of 48 measured lines) ⚠ cell-cycle shift, explains ~40% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 1.64× (z +10.9, q 2e-25, up in 44 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM64]] (+0.65, fdr 7e-06), [[MANEA]] (+0.62, fdr 1e-05), [[BMI1]] (+0.62, fdr 1e-05); moves opposite to [[FRMD8]] (-0.56, fdr 1e-05), [[VRK3]] (-0.54, fdr 2e-05), [[MYO9B]] (-0.54, fdr 3e-05).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CFL2]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 21 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8688.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.60×** | +14.6 | 3e-45 | 43/48 (HOP62, J82, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **1.68×** | +11.4 | 7e-28 | 43/49 (SW480, LOX-IMVI, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.64×** | +10.9 | 2e-25 | 44/48 (HOP62, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.70×** | +10.8 | 5e-25 | 41/45 (SW480, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~23% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.54×** | +9.5 | 2e-19 | 37/48 (LS 180, SW48, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **1.47×** | +8.1 | 4e-14 | 33/44 (SW480, KATO III, …) | all doses, flat | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.30×** | +8.0 | 8e-14 | 30/49 (HS-578T, SNU-423, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.41×** | +7.5 | 3e-12 | 42/48 (A-427, CFPAC-1, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **1.38×** | +7.0 | 1e-10 | 34/48 (NCI-H460, LS 180, …) | all doses, stronger at high dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.38×** | +6.8 | 5e-10 | 34/47 (Panc 03.27, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.36×** | +6.8 | 5e-10 | 33/48 (LOX-IMVI, PANC-1, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.35×** | +6.7 | 1e-09 | 35/48 (SW480, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | **1.36×** | +6.5 | 4e-09 | 30/47 (NCI-H1573, LOX-IMVI, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.32×** | +6.1 | 5e-08 | 34/48 (NCI-H460, H4, …) | all doses, stronger at high dose | position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.31×** | +5.7 | 4e-07 | 30/48 (HS-578T, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.26×** | +5.1 | 9e-06 | 32/48 (CFPAC-1, Panc 03.27, …) | two highest doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.49×** | +4.6 | 1e-04 | 33/48 (PANC-1, HT-29, …) | rises with dose | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.22×** | +4.3 | 4e-04 | 24/48 (C-33 A, SW48, …) | top dose only |  |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | 1.20× | +3.8 | 0.004 | 18/48 (SK-MEL-2, NCI-H2030, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.20×** | +3.7 | 0.005 | 20/47 (MIA PaCa-2, SW48, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | 1.18× | +3.6 | 0.008 | 17/48 (NCI-H2030, AsPC-1, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.35×** | +3.5 | 0.011 | 19/48 (CFPAC-1, A-427, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.35×** | +3.5 | 0.011 | 22/48 (CFPAC-1, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.34×** | +3.4 | 0.016 | 17/48 (SK-MEL-2, CFPAC-1, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8688.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.922× | -6.1 | 6e-07 | 0/50 | inconsistent across doses |  |
| [[Bergenin (drug)]] 0.5 µM |  | 0.859× | -3.4 | 0.19 | 17/48 (J82, C32, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | 0.817× | -3.2 | 0.25 | 24/48 (RKO, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8688. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 131 | 9 (8 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 0.05 µM 2.36× (z +13.1) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Gefitinib (drug)]] 5 µM 1.75× (z +8.5) | — |
| [[H4 (line)]] | wt | 127 | 5 (5 ⚠) | 0 | [[Digitoxin (drug)]] 0.5 µM 2.84× (z +10.1) ⚠ cell-cycle shift, explains ~41% of this change | — |
| [[LOX-IMVI (line)]] | wt | 97.9 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.65× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.20× (z +9.0) | — |
| [[HS-578T (line)]] | alt | 131 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +11.9) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.81× (z +9.7) | — |
| [[hTERT-HPNE (line)]] | wt | 96.9 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +15.3) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.26× (z +10.5) | — |
| [[LS 180 (line)]] | wt | 104 | 4 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.87× (z +13.1) ⚠ cell-cycle shift, explains ~37% of this change | — |
| [[SNU-423 (line)]] | alt | 125 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +12.4) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.80× (z +8.9) | — |
| [[SW480 (line)]] | alt | 135 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.40× (z +13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[J82 (line)]] | alt | 209 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +18.5) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.10× (z +10.8) | — |
| [[KATO III (line)]] | alt | 115 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +15.7) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.01× (z +9.7) | — |
| [[NCI-H1573 (line)]] | alt | 93.7 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +16.6) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[NCI-H1792 (line)]] | alt | 70.2 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +10.8) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[A-427 (line)]] | wt | 175 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.03× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[A498 (line)]] | wt | 89.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +14.2) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 1.94× (z +8.7) | — |
| [[C32 (line)]] | wt | 121 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +10.8) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[CFPAC-1 (line)]] | alt | 85.0 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.31× (z +10.6) | — |
| [[COLO 205 (line)]] | alt | 104 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +13.6) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[HOP62 (line)]] | alt | 103 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.04× (z +18.7) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.62× (z +11.4) | — |
| [[HT-29 (line)]] | alt | 123 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +12.2) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 1.97× (z +9.1) | — |
| [[SW48 (line)]] | wt | 156 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.84× (z +11.3) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[TAK-901 (drug)]] 0.05 µM 2.76× (z +10.4) | — |
| [[A549 (line)]] | wt | 94.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +11.1) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[AsPC-1 (line)]] | alt | 48.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +10.4) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[LoVo (line)]] | wt | 128 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.13× (z +9.3) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 112 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +11.1) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[NCI-H23 (line)]] | alt | 139 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.01× (z +9.3) | — |
| [[NCI-H2347 (line)]] | alt | 97.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +12.2) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[Panc 03.27 (line)]] | alt | 132 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.16× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[PANC-1 (line)]] | alt | 108 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 1.76× (z +8.8) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 140 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.26× (z +9.3) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 109 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.25× (z +8.5) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 116 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.51× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[A-172 (line)]] | wt | 157 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 154 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 98.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 161 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 150 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 144 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 187 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 64.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 98.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 81.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 138 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 150 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 148 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 81.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 142 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 98.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 137 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8688), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*55 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM64]] | +0.65 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[MANEA]] | +0.62 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[BMI1]] | +0.62 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[ZC3HAV1L]] | +0.61 | +0.38 / +0.57 | both halves | 6e-05 |  |
| [[MBTPS2]] | +0.59 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[TMEM126B]] | +0.57 | +0.62 / +0.40 | both halves | 5e-05 |  |
| [[DIS3L]] | +0.56 | +0.61 / +0.44 | both halves | 3e-05 |  |
| [[MBNL3]] | +0.55 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[CHRAC1]] | +0.55 | +0.35 / +0.49 | both halves | 1e-04 |  |
| [[CFAP97]] | +0.55 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[COX11]] | +0.54 | +0.63 / +0.50 | both halves | 1e-05 |  |
| [[HINT3]] | +0.53 | +0.46 / +0.49 | both halves | 3e-05 |  |

## Genes that move opposite

*45 of its nearest partners move opposite, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FRMD8]] | -0.56 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[VRK3]] | -0.54 | -0.53 / -0.46 | both halves | 2e-05 |  |
| [[MYO9B]] | -0.54 | -0.56 / -0.46 | both halves | 3e-05 |  |
| [[NDUFA11]] ⚠ | -0.53 | -0.44 / -0.50 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[FAAP20]] | -0.53 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[C19orf25]] | -0.53 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[WNT2B]] | -0.52 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[PSEN1]] | -0.52 | -0.56 / -0.47 | both halves | 2e-05 |  |
| [[POLR2J3-1]] | -0.51 | -0.40 / -0.46 | both halves | 5e-05 |  |
| [[UBL5]] | -0.51 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[GON4L]] | -0.51 | -0.55 / -0.46 | both halves | 3e-05 |  |
| [[POLR2J4]] | -0.51 | -0.40 / -0.48 | both halves | 5e-05 |  |
| [[EDF1]] | -0.51 | -0.49 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CFL2]] | C | CFL2 activity raises LRRC58's level | lines that do not express CFL2 (4) vs lines expressing it (45) | 1.32× lower at baseline in the lines without CFL2 | 0.060 | ⚠ few lines (4 vs 45); within organs, on part of the lines; also absent: TPST1, SLC35F1, ITGA2B; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.499). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-15.9, -5.4); signed map (-14.4, -40.6). **Vector** length 96.0, 27.1% of its response variance represented; |z| ≥ 3 in 1,051 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ponatinib (drug)]] 5 µM |  | +5.2 | +3.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.0 | +10.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.8 | +10.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.7 | +2.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.7 | +6.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.3 | +4.6 |
|  | [[Ipatasertib (drug)]] 5 µM |  | +2.8 | +2.1 |
| fall | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.3 | +1.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.1 | +0.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.5 | -3.2 |
|  | [[PH-797804 (drug)]] 0.5 µM |  | -2.9 | -2.4 |
|  | [[Thymol (drug)]] 0.5 µM |  | -2.6 | -2.7 |
|  | [[Bergenin (drug)]] 0.5 µM |  | -2.2 | -3.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.1 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | leucine rich repeat containing 58 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q13.33 — chr3:120,324,509-120,349,354 (-) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96CX6](https://www.uniprot.org/uniprotkb/Q96CX6) (Leucine-rich repeat-containing protein 58):

> Substrate-recognition component of a cullin-5-RING E3 ubiquitin-protein ligase complex (ECS complex, also named CRL5 complex), which mediates the ubiquitination and subsequent proteasomal degradation of target proteins, such as CDO1. The ECS(LRRC58) complex acts as a regulator of cysteine catabolism by mediating ubiquitination and degradation of CDO1, the rate-limiting enzyme of the cysteine catabolic process to taurine. L-cysteine abundance regulates ECS(LRRC58)-mediated ubiquitination of …

**Summary**, from NCBI Gene [116064](https://www.ncbi.nlm.nih.gov/gene/116064):

> Enables ubiquitin-like ligase-substrate adaptor activity. Involved in proteasome-mediated ubiquitin-dependent protein catabolic process and regulation of taurine biosynthetic process. Part of Cul5-RING ubiquitin ligase complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26968](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26968) · Entrez [116064](https://www.ncbi.nlm.nih.gov/gene/116064) · UniProt [Q96CX6](https://www.uniprot.org/uniprotkb/Q96CX6) · Ensembl [ENSG00000163428](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163428)

## Data

Gene col 8688: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8688); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8688, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8688]; `tensor/DDL_lfc|DDL_z.npy` [8688]; `embed/gene_vectors.npy` [8688]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8688 or target_col == 8688). Every well: [[LRRC58 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LRRC58.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
