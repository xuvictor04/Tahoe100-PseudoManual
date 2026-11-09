---
symbol: "MLLT10"
type: "gene"
col: 1223
ensembl_id: "ENSG00000078403"
name: "MLLT10 histone lysine methyltransferase DOT1L cofactor"
location: "10p12.31"
module: 146
arm: "+"
pooled_cpm: 219.49
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 22
n_dd_up_clean: 2
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/146"]
generated_by: "tahoemap"
---

# MLLT10

*MLLT10 histone lysine methyltransferase DOT1L cofactor* — 10p12.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[PH-797804 (drug)]] 5 µM: 1.87× (z +6.8, q 8e-09, up in 34 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (PANC-1 1.52×, A549 1.63×); [[Harringtonine (drug)]] 5 µM in 1 line (PANC-1 2.37×; ⚠ cell-cycle shift, explains ~38% of this change); [[TAK-901 (drug)]] 5 µM in 1 line (HT-29 3.72×); [[TAK-901 (drug)]] 0.05 µM in 1 line (LOX-IMVI 2.01×).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.348× (z -20.9, q 0e+00, down in 42 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.498× (z -20.3, q 0e+00, down in 47 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C6orf136]] (+0.68, fdr 1e-05), [[HSF2]] (+0.67, fdr 7e-06), [[TADA1]] (+0.67, fdr 7e-06); moves opposite to [[TUT7]] (-0.64, fdr 7e-06), [[DDX5]] (-0.59, fdr 2e-05), [[BACH1]] (-0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 146]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1223.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (PANC-1 1.52×, A549 1.63×); [[Harringtonine (drug)]] 5 µM in 1 line (PANC-1 2.37×; ⚠ cell-cycle shift, explains ~38% of this change); [[TAK-901 (drug)]] 5 µM in 1 line (HT-29 3.72×); [[TAK-901 (drug)]] 0.05 µM in 1 line (LOX-IMVI 2.01×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **1.87×** | +6.8 | 8e-09 | 34/48 (RKO, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.68×** | +5.6 | 5e-06 | 30/49 (HT-29, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.28×** | +4.9 | 2e-04 | 26/47 (J82, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | 1.13× | +3.5 | 0.061 | 2/48 (SHP-77, SW 1088) | rises with dose |  |
| [[Verteporfin (drug)]] 5 µM |  | 1.19× | +3.5 | 0.061 | 21/49 (SHP-77, A-427, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | 1.12× | +3.3 | 0.090 | 7/48 (AsPC-1, RKO, …) | top dose only |  |
| [[Sildenafil (drug)]] 0.5 µM |  | 1.17× | +3.3 | 0.090 | 10/48 (LoVo, J82, …) | two highest doses |  |
| [[Tomivosertib (drug)]] 5 µM |  | 1.34× | +3.1 | 0.12 | 23/48 (MIA PaCa-2, Hs 766T, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 14 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1223.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.348×** | -20.9 | 0e+00 | 42/44 (SNU-1, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.363×** | -20.9 | 0e+00 | 48/49 (SW48, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.498×** | -20.3 | 0e+00 | 47/49 (C-33 A, A549, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.396×** | -17.7 | 0e+00 | 42/45 (SNU-423, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.461×** | -16.0 | 0e+00 | 48/48 (SW480, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.470×** | -15.6 | 0e+00 | 48/48 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.536×** | -12.9 | 6e-36 | 47/48 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.565×** | -11.3 | 7e-28 | 46/47 (MIA PaCa-2, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.569×** | -11.2 | 3e-27 | 43/50 (MIA PaCa-2, LS 180, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.701×** | -10.4 | 2e-23 | 30/48 (LOX-IMVI, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.598×** | -10.2 | 1e-22 | 43/48 (MIA PaCa-2, LS 180, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.611×** | -10.2 | 1e-22 | 43/48 (SW480, HCT15, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.694×** | -7.5 | 2e-12 | 32/48 (NCI-H1573, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.719×** | -6.8 | 4e-10 | 35/48 (MIA PaCa-2, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.728×** | -6.6 | 2e-09 | 40/48 (BT-474, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.831×** | -5.4 | 2e-06 | 23/48 (HOP62, A-172, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.832×** | -3.8 | 0.004 | 23/49 (NCI-H2347, AsPC-1, …) | top dose only |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.776×** | -3.2 | 0.029 | 24/48 (SW48, NCI-H23, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | 0.848× | -3.1 | 0.039 | 15/47 (NCI-H661, LS 180, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.870× | -2.9 | 0.090 | 13/47 (AsPC-1, NCI-H23, …) | all doses, flat |  |
| [[Amsacrine (drug)]] 5 µM |  | 0.906× | -2.9 | 0.090 | 8/48 (C-33 A, A549, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.38 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1223. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 426 | 0 | 14 (9 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.164× (z -22.4) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.384× (z -17.5) |
| [[HOP62 (line)]] | alt | 168 | 0 | 13 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.371× (z -18.7) |
| [[A-172 (line)]] | wt | 267 | 0 | 12 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.201× (z -18.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.406× (z -15.6) |
| [[AsPC-1 (line)]] | alt | 161 | 0 | 11 (8 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.202× (z -19.6) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.367× (z -17.4) |
| [[LOX-IMVI (line)]] | wt | 241 | 1 | 10 (6 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.01× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -25.4) |
| [[NCI-H2030 (line)]] | alt | 474 | 0 | 11 (8 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.209× (z -16.6) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.438× (z -12.9) |
| [[HEC-1-A (line)]] | alt | 234 | 0 | 10 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.329× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.516× (z -13.0) |
| [[NCI-H2347 (line)]] | alt | 214 | 0 | 10 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.251× (z -18.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.442× (z -16.1) |
| [[SW1417 (line)]] | alt | 224 | 0 | 10 (8 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.386× (z -14.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.542× (z -14.0) |
| [[SW480 (line)]] | alt | 214 | 0 | 10 (6 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.295× (z -21.4) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.335× (z -19.2) |
| [[J82 (line)]] | alt | 207 | 1 (1 ⚠) | 8 (7 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 1.92× (z +9.1) ⚠ toxic | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.411× (z -18.3) |
| [[NCI-H1573 (line)]] | alt | 82.8 | 0 | 9 (7 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.180× (z -21.0) |
| [[RPMI-7951 (line)]] | alt | 282 | 0 | 9 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.201× (z -18.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.504× (z -11.4) |
| [[SK-MEL-2 (line)]] | alt | 186 | 0 | 9 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.168× (z -22.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.335× (z -14.3) |
| [[SNU-423 (line)]] | alt | 239 | 0 | 9 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.187× (z -18.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.426× (z -14.2) |
| [[A498 (line)]] | wt | 191 | 0 | 8 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.270× (z -17.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.442× (z -15.1) |
| [[A549 (line)]] | wt | 237 | 1 | 7 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.63× (z +8.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.322× (z -19.9) |
| [[C-33 A (line)]] | alt | 541 | 0 | 8 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0723× (z -32.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.296× (z -21.9) |
| [[CFPAC-1 (line)]] | alt | 217 | 0 | 8 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.284× (z -18.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.453× (z -16.0) |
| [[HS-578T (line)]] | alt | 193 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.409× (z -13.9) |
| [[NCI-H1792 (line)]] | alt | 279 | 0 | 8 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.245× (z -20.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.413× (z -17.9) |
| [[SW48 (line)]] | wt | 330 | 0 | 8 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.111× (z -25.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.474× (z -12.3) |
| [[A-427 (line)]] | wt | 287 | 0 | 7 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.307× (z -15.9) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 127 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.247× (z -22.9) |
| [[HT-29 (line)]] | alt | 158 | 1 | 6 (5 ⚠) | [[TAK-901 (drug)]] 5 µM 3.72× (z +9.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.430× (z -11.6) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.507× (z -9.7) |
| [[KATO III (line)]] | alt | 117 | 0 | 7 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.543× (z -11.9) |
| [[NCI-H23 (line)]] | alt | 253 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.254× (z -20.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.643× (z -9.8) |
| [[NCI-H460 (line)]] | wt | 161 | 0 | 7 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.381× (z -14.1) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.517× (z -13.7) |
| [[SNU-1 (line)]] | wt | 364 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0368× (z -38.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.536× (z -10.8) |
| [[HepG2_C3A (line)]] | wt | 411 | 0 | 6 (6 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.189× (z -21.6) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 169 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.375× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[hTERT-HPNE (line)]] | wt | 157 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -21.0) |
| [[LoVo (line)]] | wt | 166 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.451× (z -17.7) |
| [[LS 180 (line)]] | wt | 204 | 0 | 6 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.476× (z -14.3) |
| [[PANC-1 (line)]] | alt | 192 | 2 (1 ⚠) | 4 (3 ⚠) | [[Harringtonine (drug)]] 5 µM 2.37× (z +12.4) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.52× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.324× (z -16.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.601× (z -10.7) |
| [[AN3 CA (line)]] | alt | 344 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.180× (z -13.7) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.291× (z -9.9) |
| [[HCT15 (line)]] | alt | 332 | 0 | 4 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.309× (z -17.0) |
| [[SW 900 (line)]] | alt | 162 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.409× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.441× (z -9.0) |
| [[Panc 03.27 (line)]] | alt | 136 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.212× (z -17.2) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 209 | 0 | 3 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.356× (z -13.0) ⚠ toxic |
| [[BT-474 (line)]] | alt | 157 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.416× (z -11.0) ⚠ cell-cycle shift, explains ~27% of this change |
| [[COLO 205 (line)]] | alt | 98.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.343× (z -16.0) |
| [[H4 (line)]] | wt | 134 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.379× (z -9.3) ⚠ cell-cycle shift, explains ~34% of this change |
| [[CHP-212 (line)]] | wt | 272 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 201 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 220 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 300 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 186 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 150 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1223), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C6orf136]] | +0.68 | +0.67 / +0.52 | both halves | 1e-05 |  |
| [[HSF2]] | +0.67 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[TADA1]] | +0.67 | +0.71 / +0.58 | both halves | 7e-06 |  |
| [[EHMT2]] | +0.64 | +0.65 / +0.65 | both halves | 7e-06 |  |
| [[RHOT1]] | +0.64 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[WDSUB1]] | +0.63 | +0.50 / +0.63 | both halves | 1e-05 |  |
| [[RCOR3]] | +0.63 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[KIF13A]] | +0.61 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[ORC4]] | +0.61 | +0.66 / +0.53 | both halves | 1e-05 |  |
| [[KCTD3]] | +0.60 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[NDUFB10]] | +0.60 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[REV1]] | +0.60 | +0.61 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TUT7]] | -0.64 | -0.68 / -0.58 | both halves | 7e-06 |  |
| [[DDX5]] | -0.59 | -0.59 / -0.47 | both halves | 2e-05 |  |
| [[BACH1]] | -0.59 | -0.58 / -0.52 | both halves | 1e-05 |  |
| [[GPATCH2L]] | -0.58 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[NABP1]] | -0.57 | -0.60 / -0.57 | both halves | 1e-05 |  |
| [[SERPINB8]] | -0.57 | -0.50 / -0.58 | both halves | 1e-05 |  |
| [[SETX]] | -0.57 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[NIPAL1]] | -0.56 | -0.56 / -0.57 | both halves | 1e-05 |  |
| [[DUSP5-DT]] | -0.56 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[TBILA]] | -0.56 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[NOP14-AS1]] | -0.55 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[KHNYN]] | -0.55 | -0.57 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises MLLT10's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LRP3]] | B | LRP3 activity raises MLLT10's level | lines that do not express LRP3 (7) vs lines expressing it (43) | 1.54× lower at baseline in the lines without LRP3 | 0.041 | ⚠ within organs, on part of the lines; also absent: ACBD7, SNTA1, TMCC2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 146]]; 31 genes; this gene is in the **+** arm (projection on the module's main direction 0.769). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-6.7, -8.1); signed map (-27.9, -11.8). **Vector** length 109, 43.2% of its response variance represented; |z| ≥ 3 in 1,351 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +7.3 | +4.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +6.7 | +2.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +6.4 | +3.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | +3.6 | +3.5 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +3.4 | +2.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.4 | +6.8 |
| fall | [[Auranofin (drug)]] 5 µM |  | -4.0 | -10.2 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.9 | -0.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -3.0 | -5.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.7 | +0.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.6 | -0.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.6 | -0.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.4 | -2.5 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -2.1 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | MLLT10 histone lysine methyltransferase DOT1L cofactor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p12.31 — chr10:21,524,646-21,743,630 (+) |
| Ensembl biotype | protein_coding |
| Also known as | AF10 |
| Gene groups (HGNC) | PHD finger proteins |
| Hallmark sets | SPERMATOGENESIS |
| Matched by | ensembl_id |

**Function**, from UniProt [P55197](https://www.uniprot.org/uniprotkb/P55197) (Protein AF-10):

> Probably involved in transcriptional regulation. In vitro or as fusion protein with KMT2A/MLL1 has transactivation activity. Binds to cruciform DNA. In cells, binding to unmodified histone H3 regulates DOT1L functions including histone H3 'Lys-79' dimethylation (H3K79me2) and gene activation.

**Summary**, from NCBI Gene [8028](https://www.ncbi.nlm.nih.gov/gene/8028):

> This gene encodes a transcription factor and has been identified as a partner gene involved in several chromosomal rearrangements resulting in various leukemias. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Sep 2010]

**Accessions** — [HGNC:16063](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16063) · Entrez [8028](https://www.ncbi.nlm.nih.gov/gene/8028) · UniProt [P55197](https://www.uniprot.org/uniprotkb/P55197) · Ensembl [ENSG00000078403](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000078403)

## Data

Gene col 1223: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1223); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1223, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1223]; `tensor/DDL_lfc|DDL_z.npy` [1223]; `embed/gene_vectors.npy` [1223]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1223 or target_col == 1223). Every well: [[MLLT10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MLLT10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
