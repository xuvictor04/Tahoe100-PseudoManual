---
symbol: "ARHGAP35"
type: "gene"
col: 8289
ensembl_id: "ENSG00000160007"
name: "Rho GTPase activating protein 35"
location: "19q13.32"
module: 45
arm: "+"
pooled_cpm: 184.37
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 15
n_dd_up_clean: 0
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/045"]
generated_by: "tahoemap"
---

# ARHGAP35

*Rho GTPase activating protein 35* — 19q13.32

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (HT-29 1.44×, HepG2/C3A 1.65×); [[Adagrasib (drug)]] 0.05 µM in 1 line (HOP62 1.40×; ⚠ position not correctable); [[TAK-901 (drug)]] 5 µM in 1 line (HT-29 3.72×; ⚠ cell-cycle shift, would explain all of this change).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.583× (z -22.3, q 0e+00, down in 41 of 49 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CAT]] (+0.57, fdr 7e-05), [[USP48]] (+0.54, fdr 5e-05), [[PCYOX1]] (+0.52, fdr 4e-05); moves opposite to [[GABPB1]] (-0.57, fdr 3e-05), [[MOSMO]] (-0.53, fdr 3e-05), [[E2F3]] (-0.52, fdr 1e-04).
> It sits in the **+** arm of [[Module 045]] (Iron uptake and transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8289.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (HT-29 1.44×, HepG2/C3A 1.65×); [[Adagrasib (drug)]] 0.05 µM in 1 line (HOP62 1.40×; ⚠ position not correctable); [[TAK-901 (drug)]] 5 µM in 1 line (HT-29 3.72×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | 1.13× | +3.4 | 0.14 | 12/50 (HOP62, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 1.14× | +3.4 | 0.14 | 14/48 (HOP62, AsPC-1, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.10× | +3.3 | 0.14 | 9/48 (LoVo, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | 1.08× | +3.3 | 0.14 | 4/48 (KATO III, HT-29, …) | rises with dose |  |
| [[Rifaximin (drug)]] 5 µM |  | 1.12× | +3.1 | 0.18 | 3/48 (NCI-H23, RPMI-7951, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.08× | +3.0 | 0.18 | 4/49 (LoVo, HOP62, …) | all doses, flat |  |
| [[NG25 (drug)]] 5 µM |  | 1.25× | +3.0 | 0.18 | 13/47 (AsPC-1, LoVo, …) | top dose only | cell-cycle shift (explains ~3% here); noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | 1.12× | +3.0 | 0.18 | 11/48 (HOP62, AsPC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 11 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8289.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.583×** | -22.3 | 0e+00 | 41/49 (SW 900, HS-578T, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.639×** | -12.5 | 1e-33 | 43/47 (SW 900, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.668×** | -11.8 | 1e-29 | 35/48 (HS-578T, hTERT-HPNE, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.687×** | -10.1 | 7e-22 | 29/45 (SW480, SNU-1, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.801×** | -9.2 | 6e-18 | 27/48 (A-172, hTERT-HPNE, …) | two highest doses | cell-cycle shift (explains ~6% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.739×** | -8.5 | 2e-15 | 31/50 (SW 900, RPMI-7951, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.746×** | -8.2 | 2e-14 | 30/48 (RPMI-7951, SW 900, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.785×** | -7.1 | 1e-10 | 30/48 (RPMI-7951, HOP62, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.783×** | -6.9 | 4e-10 | 32/48 (HS-578T, HOP62, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | **0.791×** | -6.8 | 5e-10 | 27/49 (NCI-H1792, SW480, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | **0.802×** | -6.2 | 3e-08 | 23/44 (LS 180, LoVo, …) | all doses, flat | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.817×** | -5.9 | 2e-07 | 25/48 (SW480, SW 900, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~9% of this change | **0.830×** | -5.4 | 3e-06 | 25/48 (A-172, H4, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | 0.863× | -4.3 | 7e-04 | 18/48 (SW 900, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.907× | -4.0 | 0.002 | 9/49 (H4, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Amsacrine (drug)]] 5 µM |  | 0.910× | -3.9 | 0.004 | 4/48 (SW 900, HOP62, …) | top dose only |  |
| [[Peretinoin (drug)]] 5 µM |  | 0.871× | -3.9 | 0.004 | 18/47 (AsPC-1, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | 0.870× | -3.7 | 0.006 | 19/47 (C32, A-427, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.881× | -3.7 | 0.006 | 13/47 (H4, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.881× | -3.7 | 0.007 | 13/48 (A-427, NCI-H460, …) | all doses, stronger at high dose |  |
| [[vincristine (drug)]] 0.5 µM |  | 0.842× | -3.3 | 0.027 | 17/48 (MIA PaCa-2, BT-474, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[vincristine (drug)]] 5 µM |  | **0.796×** | -3.1 | 0.047 | 16/46 (BT-474, SNU-423, …) | rises with dose | noisy plate (z scaled) |
| [[Retinoic acid (drug)]] 0.5 µM |  | 0.900× | -3.1 | 0.047 | 11/48 (NCI-H1792, RPMI-7951, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8289. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW 900 (line)]] | alt | 562 | 0 | 21 (15 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.244× (z -26.6) |
| [[RPMI-7951 (line)]] | alt | 449 | 0 | 15 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.288× (z -22.4) |
| [[H4 (line)]] | wt | 330 | 0 | 12 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.323× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.475× (z -12.9) |
| [[HOP62 (line)]] | alt | 251 | 0 | 12 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.392× (z -16.2) |
| [[hTERT-HPNE (line)]] | wt | 288 | 0 | 12 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -23.1) |
| [[C32 (line)]] | wt | 221 | 0 | 11 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -20.6) |
| [[A-172 (line)]] | wt | 134 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -25.7) |
| [[HS-578T (line)]] | alt | 356 | 0 | 9 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.348× (z -22.2) |
| [[NCI-H1792 (line)]] | alt | 279 | 0 | 8 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.396× (z -18.8) |
| [[LOX-IMVI (line)]] | wt | 176 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.496× (z -12.7) |
| [[CFPAC-1 (line)]] | alt | 107 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.406× (z -19.3) |
| [[HT-29 (line)]] | alt | 329 | 1 (1 ⚠) | 4 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 3.72× (z +10.7) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 5 µM 0.443× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change |
| [[LoVo (line)]] | wt | 176 | 1 (1 ⚠) | 4 (3 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 1.63× (z +8.8) ⚠ toxic; cell-cycle shift, explains ~0% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.488× (z -19.1) |
| [[MIA PaCa-2 (line)]] | alt | 169 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.350× (z -16.1) |
| [[SNU-423 (line)]] | alt | 173 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.412× (z -20.3) |
| [[A498 (line)]] | wt | 170 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.555× (z -14.3) |
| [[SW480 (line)]] | alt | 175 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.441× (z -16.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.557× (z -12.4) |
| [[HCT15 (line)]] | alt | 267 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.544× (z -12.2) |
| [[HEC-1-A (line)]] | alt | 257 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.558× (z -18.3) |
| [[J82 (line)]] | alt | 201 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.564× (z -12.7) |
| [[LS 180 (line)]] | wt | 179 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.283× (z -17.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.450× (z -16.2) |
| [[AsPC-1 (line)]] | alt | 156 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.419× (z -16.1) |
| [[KATO III (line)]] | alt | 202 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.464× (z -11.5) ⚠ toxic |
| [[NCI-H1573 (line)]] | alt | 64.3 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.14× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.483× (z -8.8) |
| [[NCI-H2030 (line)]] | alt | 140 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.534× (z -14.3) |
| [[NCI-H23 (line)]] | alt | 122 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.464× (z -11.5) |
| [[SW1417 (line)]] | alt | 301 | 1 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.76× (z +10.0) ⚠ cell-cycle shift, explains ~0% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.593× (z -13.2) |
| [[A-427 (line)]] | wt | 150 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.424× (z -13.3) |
| [[AN3 CA (line)]] | alt | 177 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.256× (z -12.3) |
| [[BT-474 (line)]] | alt | 202 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.483× (z -11.9) |
| [[C-33 A (line)]] | alt | 179 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.360× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change |
| [[COLO 205 (line)]] | alt | 116 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.455× (z -9.4) |
| [[HepG2_C3A (line)]] | wt | 157 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.65× (z +8.9) | — |
| [[NCI-H2347 (line)]] | alt | 78.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.666× (z -8.6) |
| [[NCI-H460 (line)]] | wt | 91.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.621× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change |
| [[PANC-1 (line)]] | alt | 166 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.593× (z -15.4) |
| [[SK-MEL-2 (line)]] | alt | 134 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.530× (z -8.7) ⚠ cell-cycle shift, explains ~23% of this change |
| [[SNU-1 (line)]] | wt | 129 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.253× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[SW 1088 (line)]] | alt | 289 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.310× (z -9.3) |
| [[SW 1271 (line)]] | alt | 177 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -9.1) |
| [[A549 (line)]] | wt | 171 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 117 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 93.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 174 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 178 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 99.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 151 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 137 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8289), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*53 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CAT]] | +0.57 | +0.59 / +0.37 | both halves | 7e-05 |  |
| [[USP48]] | +0.54 | +0.51 / +0.39 | both halves | 5e-05 |  |
| [[PCYOX1]] | +0.52 | +0.46 / +0.41 | both halves | 4e-05 |  |
| [[PLA2G12A]] | +0.52 | +0.53 / +0.31 | both halves | 2e-04 |  |
| [[PLEKHH3]] | +0.51 | +0.55 / +0.34 | both halves | 1e-04 |  |
| [[HDGFL2]] | +0.51 | +0.55 / +0.33 | both halves | 1e-04 |  |
| [[SOX12]] | +0.50 | +0.57 / +0.38 | both halves | 7e-05 |  |
| [[RAB3A]] | +0.50 | +0.41 / +0.36 | both halves | 9e-05 |  |
| [[PPP2R5D]] | +0.50 | +0.51 / +0.43 | both halves | 3e-05 |  |
| [[VDAC3]] | +0.49 | +0.49 / +0.40 | both halves | 5e-05 |  |
| [[HCFC1R1]] | +0.49 | +0.55 / +0.31 | both halves | 2e-04 |  |
| [[HNRNPUL2]] | +0.49 | +0.41 / +0.48 | both halves | 4e-05 |  |

## Genes that move opposite

*47 of its nearest partners move opposite, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GABPB1]] | -0.57 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[MOSMO]] | -0.53 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[E2F3]] | -0.52 | -0.47 / -0.36 | both halves | 1e-04 |  |
| [[GNG12-AS1]] | -0.50 | -0.49 / -0.34 | both halves | 1e-04 |  |
| [[SLC9B2]] | -0.50 | -0.36 / -0.42 | both halves | 9e-05 |  |
| [[ITGB1-DT]] | -0.49 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[NIPAL2]] | -0.49 | -0.44 / -0.30 | both halves | 2e-04 |  |
| [[GCNT4]] | -0.49 | -0.48 / -0.32 | both halves | 2e-04 |  |
| [[BMAL2]] | -0.49 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[FRMD6-AS2]] | -0.49 | -0.41 / -0.38 | both halves | 7e-05 |  |
| [[GSAP]] | -0.48 | -0.43 / -0.42 | both halves | 4e-05 |  |
| [[DUSP5-DT]] | -0.48 | -0.49 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises ARHGAP35's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 045]] — Iron uptake and transport; 102 genes; this gene is in the **+** arm (projection on the module's main direction 0.457). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (4.4, -8.6); signed map (-36.9, -11.4). **Vector** length 111, 32.4% of its response variance represented; |z| ≥ 3 in 1,290 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.1 | -2.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.9 | +0.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.6 | -3.1 |
|  | [[NG25 (drug)]] 5 µM |  | +3.0 | +3.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +3.0 | +3.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.9 | +2.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +2.7 | +2.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.7 | +2.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +2.7 | +2.4 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.0 | -22.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -7.4 | -12.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | -6.0 | -10.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | -5.5 | -7.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.0 | -11.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.0 | -2.6 |
|  | [[vincristine (drug)]] 0.5 µM |  | -2.6 | -3.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.6 | -3.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.6 | -1.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.5 | -4.0 |

## What is on record

|  |  |
|---|---|
| Name | Rho GTPase activating protein 35 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.32 — chr19:46,860,997-47,005,077 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GRF-1, p190ARhoGAP, P190A, KIAA1722, p190RhoGAP; previously GRLF1 |
| Gene groups (HGNC) | Rho GTPase activating proteins |
| Reactome | 25 pathways, smallest: Sema4D mediated inhibition of cell attachment and migration; PTK6 Regulates RHO GTPases, RAS GTPase and MAP kinases; Sema4D in semaphorin signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NRY4](https://www.uniprot.org/uniprotkb/Q9NRY4) (Rho GTPase-activating protein 35):

> Rho GTPase-activating protein (GAP). Binds several acidic phospholipids which inhibits the Rho GAP activity to promote the Rac GAP activity. This binding is inhibited by phosphorylation by PRKCA. Involved in cell differentiation as well as cell adhesion and migration, plays an important role in retinal tissue morphogenesis, neural tube fusion, midline fusion of the cerebral hemispheres and mammary gland branching morphogenesis (By similarity). Transduces signals from p21-ras to the nucleus, …

**Summary**, from NCBI Gene [2909](https://www.ncbi.nlm.nih.gov/gene/2909):

> The human glucocorticoid receptor DNA binding factor, which associates with the promoter region of the glucocorticoid receptor gene (hGR gene), is a repressor of glucocorticoid receptor transcription. The amino acid sequence deduced from the cDNA sequences show the presence of three sequence motifs characteristic of a zinc finger and one motif suggestive of a leucine zipper in which 1 cysteine is found instead of all leucines. The GRLF1 enhances the homologous down-regulation of wild-type hGR …

**Accessions** — [HGNC:4591](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4591) · Entrez [2909](https://www.ncbi.nlm.nih.gov/gene/2909) · UniProt [Q9NRY4](https://www.uniprot.org/uniprotkb/Q9NRY4) · Ensembl [ENSG00000160007](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000160007)

## Data

Gene col 8289: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8289); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8289, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8289]; `tensor/DDL_lfc|DDL_z.npy` [8289]; `embed/gene_vectors.npy` [8289]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8289 or target_col == 8289). Every well: [[ARHGAP35 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARHGAP35.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
