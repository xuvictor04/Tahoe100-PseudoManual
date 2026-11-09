---
symbol: "ATP9B"
type: "gene"
col: 9293
ensembl_id: "ENSG00000166377"
name: "ATPase phospholipid transporting 9B"
location: "18q23"
module: 5
arm: "+"
pooled_cpm: 125.44
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 12
n_dd_up_clean: 2
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# ATP9B

*ATPase phospholipid transporting 9B* — 18q23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.32× (z +6.4, q 1e-07, up in 25 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 11 lines (NCI-H2347 4.56×, PANC-1 3.19×, A-172 3.47×, COLO 205 3.21×, …); [[Pitavastatin (Calcium) (drug)]] 5 µM in 2 lines (C32 4.17×, NCI-H460 2.96×; ⚠ cell-cycle shift, explains ~20% of this change); [[Harringtonine (drug)]] 5 µM in 1 line (PANC-1 2.08×; ⚠ cell-cycle shift, explains ~0% of this change); [[Pitavastatin (Calcium) (drug)]] 0.5 µM in 1 line (NCI-H460 2.75×).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.592× (z -12.2, q 3e-31, down in 46 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COMMD10]] (+0.60, fdr 1e-05), [[OSBP2]] (+0.59, fdr 2e-05), [[HLCS]] (+0.59, fdr 2e-05); moves opposite to [[EED]] (-0.59, fdr 1e-05), [[FUCA1]] (-0.58, fdr 2e-05), [[SRP54-AS1]] (-0.58, fdr 1e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[NCF2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9293.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 11 lines (NCI-H2347 4.56×, PANC-1 3.19×, A-172 3.47×, COLO 205 3.21×, …); [[Pitavastatin (Calcium) (drug)]] 5 µM in 2 lines (C32 4.17×, NCI-H460 2.96×; ⚠ cell-cycle shift, explains ~20% of this change); [[Harringtonine (drug)]] 5 µM in 1 line (PANC-1 2.08×; ⚠ cell-cycle shift, explains ~0% of this change); [[Pitavastatin (Calcium) (drug)]] 0.5 µM in 1 line (NCI-H460 2.75×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.32×** | +6.4 | 1e-07 | 25/48 (NCI-H2347, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.34×** | +4.6 | 0.001 | 36/47 (C32, NCI-H460, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.30×** | +3.8 | 0.030 | 26/47 (NCI-H460, C32, …) | rises with dose | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 9 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9293.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.592×** | -12.2 | 3e-31 | 46/49 (NCI-H460, SNU-1, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.514×** | -10.5 | 3e-23 | 39/44 (NCI-H23, C-33 A, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.502×** | -9.9 | 7e-21 | 44/49 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.605×** | -7.2 | 1e-10 | 37/45 (C-33 A, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.654×** | -6.7 | 3e-09 | 34/50 (NCI-H23, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | **0.656×** | -6.6 | 3e-09 | 31/47 (NCI-H23, MIA PaCa-2, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.696×** | -5.7 | 9e-07 | 34/48 (NCI-H23, A-172, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.697×** | -5.7 | 9e-07 | 33/47 (MIA PaCa-2, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | **0.722×** | -5.3 | 6e-06 | 29/48 (PANC-1, SW48, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~55% of this change | **0.761×** | -4.5 | 4e-04 | 33/48 (PANC-1, BT-474, …) | inconsistent across doses | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~90% of this change | **0.802×** | -3.6 | 0.016 | 23/48 (PANC-1, LS 180, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **0.808×** | -3.5 | 0.023 | 25/48 (LOX-IMVI, MIA PaCa-2, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9293. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 306 | 2 (1 ⚠) | 6 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.19× (z +22.3) | [[Dinaciclib (drug)]] 5 µM 0.332× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[C32 (line)]] | wt | 133 | 1 (1 ⚠) | 6 (4 ⚠) | [[Pitavastatin (Calcium) (drug)]] 5 µM 4.17× (z +14.2) ⚠ cell-cycle shift, explains ~20% of this change | [[Homoharringtonine (drug)]] 5 µM 0.467× (z -11.2) |
| [[MIA PaCa-2 (line)]] | alt | 158 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.154× (z -20.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.406× (z -10.0) |
| [[NCI-H23 (line)]] | alt | 195 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0757× (z -31.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.235× (z -17.6) |
| [[A-172 (line)]] | wt | 113 | 1 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +19.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.383× (z -14.9) |
| [[NCI-H460 (line)]] | wt | 191 | 2 (1 ⚠) | 3 (2 ⚠) | [[Pitavastatin (Calcium) (drug)]] 5 µM 2.96× (z +11.1) ⚠ cell-cycle shift, explains ~20% of this change · without an alert: [[Pitavastatin (Calcium) (drug)]] 0.5 µM 2.75× (z +9.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.325× (z -17.0) |
| [[A-427 (line)]] | wt | 190 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.312× (z -13.4) ⚠ cell-cycle shift, would explain all of this change |
| [[C-33 A (line)]] | alt | 219 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0618× (z -30.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.561× (z -9.2) |
| [[LS 180 (line)]] | wt | 174 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.222× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[NCI-H1792 (line)]] | alt | 202 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.334× (z -16.3) |
| [[SNU-1 (line)]] | wt | 324 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0570× (z -25.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.283× (z -16.7) |
| [[SW480 (line)]] | alt | 92.3 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.491× (z -13.8) |
| [[A498 (line)]] | wt | 84.5 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +11.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.512× (z -11.6) |
| [[A549 (line)]] | wt | 123 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +11.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.332× (z -16.3) |
| [[AsPC-1 (line)]] | alt | 103 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.342× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.523× (z -8.9) |
| [[H4 (line)]] | wt | 130 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +13.0) | [[Dinaciclib (drug)]] 5 µM 0.280× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[J82 (line)]] | alt | 86.9 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +13.9) | [[Dinaciclib (drug)]] 0.05 µM 0.270× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[LoVo (line)]] | wt | 127 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.351× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[RPMI-7951 (line)]] | alt | 88.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +10.5) | [[Dinaciclib (drug)]] 0.05 µM 0.281× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[SK-MEL-2 (line)]] | alt | 140 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.250× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[SW48 (line)]] | wt | 116 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +10.1) | [[Digitoxin (drug)]] 5 µM 0.275× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change |
| [[BT-474 (line)]] | alt | 120 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.83× (z +16.1) | — |
| [[CFPAC-1 (line)]] | alt | 60.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.557× (z -8.5) |
| [[COLO 205 (line)]] | alt | 96.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +16.2) | — |
| [[HEC-1-A (line)]] | alt | 122 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.353× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[LOX-IMVI (line)]] | wt | 112 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.495× (z -11.0) |
| [[NCI-H1573 (line)]] | alt | 105 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.505× (z -10.5) |
| [[NCI-H2347 (line)]] | alt | 64.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.56× (z +24.7) | — |
| [[Panc 03.27 (line)]] | alt | 90.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.475× (z -11.0) |
| [[RKO (line)]] | wt | 156 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.561× (z -8.9) |
| [[SHP-77 (line)]] | alt | 130 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.196× (z -18.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[SNU-423 (line)]] | alt | 74.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.265× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[SW 900 (line)]] | alt | 75.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.349× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[SW1417 (line)]] | alt | 105 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.540× (z -9.3) |
| [[AN3 CA (line)]] | alt | 111 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 122 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 147 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 90.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 47.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 71.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 63.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 80.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 87.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 90.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 67.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 99.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 84.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 158 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9293), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COMMD10]] | +0.60 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[OSBP2]] | +0.59 | +0.61 / +0.48 | both halves | 2e-05 |  |
| [[HLCS]] | +0.59 | +0.47 / +0.60 | both halves | 2e-05 |  |
| [[CDC42BPA]] | +0.59 | +0.44 / +0.68 | both halves | 3e-05 |  |
| [[RABGAP1L]] | +0.57 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[JPX]] | +0.57 | +0.47 / +0.63 | both halves | 2e-05 |  |
| [[RALGAPA1]] | +0.56 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[RAD23A]] | +0.55 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[FKTN]] | +0.55 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[NUTM2B-AS1]] | +0.54 | +0.46 / +0.65 | both halves | 2e-05 |  |
| [[ZMYM4]] | +0.54 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[BCL7B]] | +0.54 | +0.37 / +0.54 | both halves | 7e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EED]] | -0.59 | -0.52 / -0.57 | both halves | 1e-05 |  |
| [[FUCA1]] | -0.58 | -0.47 / -0.62 | both halves | 2e-05 |  |
| [[SRP54-AS1]] | -0.58 | -0.52 / -0.59 | both halves | 1e-05 |  |
| [[SAP30-DT]] | -0.55 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[CRLS1]] | -0.54 | -0.46 / -0.56 | both halves | 3e-05 |  |
| [[NARF]] | -0.54 | -0.42 / -0.53 | both halves | 4e-05 |  |
| [[PAIP2B]] | -0.53 | -0.38 / -0.49 | both halves | 6e-05 |  |
| [[ANKZF1]] | -0.53 | -0.49 / -0.52 | both halves | 2e-05 |  |
| [[TPCN1]] | -0.53 | -0.46 / -0.56 | both halves | 3e-05 | pathway: Ion channel transport |
| [[APAF1]] | -0.52 | -0.47 / -0.58 | both halves | 2e-05 |  |
| [[SPICE1]] | -0.52 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[KDM3A]] | -0.51 | -0.49 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NCF2]] | B | NCF2 activity lowers ATP9B's level | lines that do not express NCF2 (9) vs lines expressing it (41) | 1.71× higher at baseline in the lines without NCF2 | 0.007 | ⚠ within organs, on part of the lines; also absent: MAML2; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity raises ATP9B's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.292). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (5.3, -21.8); signed map (5.8, -49.6). **Vector** length 82.9, 22.3% of its response variance represented; |z| ≥ 3 in 925 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.4 | +6.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.9 | +0.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.0 | -0.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +3.6 | -0.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.6 | -1.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.5 | -1.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.5 | +2.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.8 | +3.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.5 | -0.1 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.6 | -12.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.6 | -6.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.5 | -5.7 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.8 | -2.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.2 | -2.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.1 | -1.2 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | -2.0 | -1.7 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -1.6 | -0.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.6 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | ATPase phospholipid transporting 9B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q23 — chr18:79,069,285-79,378,287 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ATPIIB |
| Gene groups (HGNC) | ATPase phospholipid transporting |
| Reactome | 3 pathways, smallest: Ion transport by P-type ATPases; Ion channel transport; Transport of small molecules |
| Matched by | ensembl_id |

UniProt [O43861](https://www.uniprot.org/uniprotkb/O43861) carries no function annotation.

**Summary**, from NCBI Gene [374868](https://www.ncbi.nlm.nih.gov/gene/374868):

> Predicted to enable ATPase-coupled intramembrane lipid carrier activity. Predicted to be involved in endocytosis; phospholipid translocation; and retrograde vesicle-mediated transport, Golgi to endoplasmic reticulum. Located in perinuclear region of cytoplasm and trans-Golgi network. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:13541](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13541) · Entrez [374868](https://www.ncbi.nlm.nih.gov/gene/374868) · UniProt [O43861](https://www.uniprot.org/uniprotkb/O43861) · Ensembl [ENSG00000166377](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166377)

## Data

Gene col 9293: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9293); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9293, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9293]; `tensor/DDL_lfc|DDL_z.npy` [9293]; `embed/gene_vectors.npy` [9293]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9293 or target_col == 9293). Every well: [[ATP9B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATP9B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
