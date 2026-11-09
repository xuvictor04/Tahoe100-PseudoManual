---
symbol: "HECTD4"
type: "gene"
col: 10334
ensembl_id: "ENSG00000173064"
name: "HECT domain E3 ubiquitin protein ligase 4"
location: "12q24.13"
module: 54
arm: "+"
pooled_cpm: 176.6
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 9
n_dd_up_clean: 6
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/054"]
generated_by: "tahoemap"
---

# HECTD4

*HECT domain E3 ubiquitin protein ligase 4* — 12q24.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.34× (z +12.1, q 5e-31, up in 32 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.498× (z -20.2, q 0e+00, down in 45 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.600× (z -14.8, q 0e+00, down in 45 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Auranofin (drug)]] 5 µM in 15 lines (MIA PaCa-2 0.321×, HOP62 0.416×, LOX-IMVI 0.463×, A-172 0.477×, …); [[Dinaciclib (drug)]] 5 µM in 6 lines (C-33 A 0.0558×, A-427 0.208×, Panc 03.27 0.270×, LoVo 0.321×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 4 lines (MIA PaCa-2 0.229×, NCI-H460 0.358×, NCI-H1792 0.325×, A549 0.351×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RTF1]] (+0.66, fdr 1e-05), [[PTPRA]] (+0.64, fdr 2e-05), [[KIF1B]] (+0.62, fdr 1e-05); moves opposite to [[LINC03009]] (-0.57, fdr 2e-05), [[MAT2A]] (-0.55, fdr 4e-05), [[SRSF1]] (-0.53, fdr 4e-05).
> It sits in the **+** arm of [[Module 054]] (Mitochondrial ribosome-associated quality control).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10334.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.34×** | +12.1 | 5e-31 | 32/48 (SW480, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.33×** | +8.3 | 2e-14 | 35/48 (PANC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.29×** | +7.3 | 5e-11 | 31/48 (A-427, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.27×** | +6.9 | 9e-10 | 27/48 (A-427, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **1.21×** | +5.4 | 8e-06 | 27/47 (NCI-H460, SW480, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~40% of this change | 1.18× | +4.2 | 0.003 | 19/48 (C32, PANC-1, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | 1.17× | +4.0 | 0.004 | 18/50 (SW480, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.13× | +3.5 | 0.028 | 13/47 (SW480, H4, …) | rises with dose | low cells (technical?) |
| [[Brivudine (drug)]] 5 µM |  | **1.30×** | +3.5 | 0.032 | 19/49 (AsPC-1, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 1.14× | +3.4 | 0.034 | 6/48 (SW480, LS 180, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.09× | +3.3 | 0.045 | 2/48 (SW480, H4) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.12× | +3.3 | 0.053 | 20/48 (PANC-1, SW480, …) | top dose only | composition shift |
| [[RMC-6236 (drug)]] 5 µM |  | **1.27×** | +3.1 | 0.069 | 8/48 (SW480, hTERT-HPNE, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.08× | +3.1 | 0.069 | 2/48 (SW48, H4) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 10 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10334.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Auranofin (drug)]] 5 µM in 15 lines (MIA PaCa-2 0.321×, HOP62 0.416×, LOX-IMVI 0.463×, A-172 0.477×, …); [[Dinaciclib (drug)]] 5 µM in 6 lines (C-33 A 0.0558×, A-427 0.208×, Panc 03.27 0.270×, LoVo 0.321×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 4 lines (MIA PaCa-2 0.229×, NCI-H460 0.358×, NCI-H1792 0.325×, A549 0.351×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.498×** | -20.2 | 0e+00 | 45/49 (NCI-H460, SW 1271, …) | all doses, flat | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.517×** | -17.7 | 0e+00 | 41/45 (MIA PaCa-2, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.543×** | -17.0 | 0e+00 | 42/44 (C-33 A, A-427, …) | all doses, flat | cell-cycle shift (explains ~17% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.600×** | -14.8 | 0e+00 | 45/48 (MIA PaCa-2, HOP62, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.646×** | -12.2 | 5e-32 | 39/47 (NCI-H2030, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~23% of this change | **0.759×** | -7.7 | 1e-12 | 32/47 (LOX-IMVI, NCI-H460, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~39% of this change | **0.818×** | -5.8 | 4e-07 | 25/48 (Panc 03.27, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.826×** | -5.5 | 2e-06 | 24/48 (NCI-H1792, Panc 03.27, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.888× | -4.9 | 7e-05 | 13/48 (LoVo, NCI-H1792, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.848× | -4.8 | 1e-04 | 19/48 (MIA PaCa-2, J82, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.867× | -4.1 | 0.002 | 14/49 (LoVo, NCI-H1573, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.766×** | -3.6 | 0.018 | 22/48 (NCI-H1573, RKO, …) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | 0.896× | -3.2 | 0.063 | 16/48 (A549, A-172, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10334. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 190 | 2 (1 ⚠) | 10 (9 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.51× (z +12.1) | [[Dinaciclib (drug)]] 0.05 µM 0.358× (z -19.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.580× (z -11.4) |
| [[A-172 (line)]] | wt | 199 | 0 | 8 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.334× (z -18.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.477× (z -12.4) |
| [[AsPC-1 (line)]] | alt | 180 | 0 | 8 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.322× (z -17.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.528× (z -9.8) |
| [[PANC-1 (line)]] | alt | 177 | 3 (1 ⚠) | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.56× (z +13.3) | [[Dinaciclib (drug)]] 0.05 µM 0.508× (z -13.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.639× (z -9.5) |
| [[SW480 (line)]] | alt | 156 | 4 (3 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +23.0) | [[Dinaciclib (drug)]] 0.5 µM 0.487× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.577× (z -10.3) |
| [[LOX-IMVI (line)]] | wt | 172 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.354× (z -15.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.463× (z -12.6) |
| [[MIA PaCa-2 (line)]] | alt | 223 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.229× (z -20.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.321× (z -17.4) |
| [[SW 900 (line)]] | alt | 164 | 1 | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.62× (z +10.4) | [[Dinaciclib (drug)]] 0.05 µM 0.383× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.477× (z -11.2) |
| [[A498 (line)]] | wt | 147 | 2 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.57× (z +11.0) | [[Dinaciclib (drug)]] 0.05 µM 0.361× (z -16.4) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 204 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.351× (z -17.6) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 163 | 1 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +13.6) | [[Dinaciclib (drug)]] 5 µM 0.354× (z -13.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.494× (z -9.6) |
| [[HS-578T (line)]] | alt | 147 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.336× (z -16.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.529× (z -9.6) |
| [[NCI-H1792 (line)]] | alt | 202 | 1 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.54× (z +11.0) | [[Dinaciclib (drug)]] 0.05 µM 0.325× (z -18.9) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 137 | 3 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 1.86× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.208× (z -22.1) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 157 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.507× (z -11.6) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 236 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.498× (z -13.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.567× (z -10.9) |
| [[LoVo (line)]] | wt | 206 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.75× (z +13.4) | [[Dinaciclib (drug)]] 5 µM 0.321× (z -18.4) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 205 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.388× (z -14.6) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 147 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.270× (z -20.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.588× (z -8.8) |
| [[C-33 A (line)]] | alt | 223 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0558× (z -37.6) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 153 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.411× (z -13.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.416× (z -13.7) |
| [[HT-29 (line)]] | alt | 155 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +14.9) | [[Dinaciclib (drug)]] 5 µM 0.328× (z -16.1) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 155 | 0 | 3 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.458× (z -11.7) ⚠ toxic |
| [[LS 180 (line)]] | wt | 166 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.58× (z +10.4) | [[Dinaciclib (drug)]] 0.05 µM 0.340× (z -16.3) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 183 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.488× (z -12.4) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 191 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.324× (z -16.9) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 137 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +12.5) | [[Dinaciclib (drug)]] 0.5 µM 0.247× (z -17.1) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 164 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.311× (z -15.8) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 158 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.464× (z -11.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.468× (z -11.6) |
| [[SW1417 (line)]] | alt | 211 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.483× (z -11.5) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 250 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.260× (z -17.8) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 168 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.383× (z -12.0) ⚠ toxic |
| [[KATO III (line)]] | alt | 136 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.52× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.464× (z -11.9) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 187 | 1 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.73× (z +11.3) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.503× (z -9.6) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 144 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.62× (z +9.0) | [[Auranofin (drug)]] 5 µM 0.521× (z -8.6) |
| [[SHP-77 (line)]] | alt | 255 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.445× (z -15.0) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 153 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.275× (z -13.0) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 277 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.353× (z -9.5) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 268 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.563× (z -9.1) |
| [[CHP-212 (line)]] | wt | 177 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.293× (z -9.6) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 126 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.77× (z +9.8) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[Hs 766T (line)]] | wt | 111 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.529× (z -8.6) |
| [[hTERT-HPNE (line)]] | wt | 146 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.481× (z -8.5) |
| [[NCI-H661 (line)]] | alt | 204 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.149× (z -13.3) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 199 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0688× (z -18.4) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 113 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 193 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 176 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 137 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 157 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10334), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 6 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RTF1]] | +0.66 | +0.51 / +0.65 | both halves | 1e-05 | **novel candidate** |
| [[PTPRA]] | +0.64 | +0.49 / +0.70 | both halves | 2e-05 |  |
| [[KIF1B]] | +0.62 | +0.49 / +0.66 | both halves | 1e-05 | same gene group |
| [[HRAS]] | +0.59 | +0.43 / +0.57 | both halves | 4e-05 |  |
| [[MTM1]] | +0.58 | +0.36 / +0.65 | both halves | 9e-05 |  |
| [[NCOA1]] | +0.58 | +0.65 / +0.65 | both halves | 7e-06 |  |
| [[DCTN3]] | +0.58 | +0.42 / +0.58 | both halves | 4e-05 |  |
| [[FAM193A]] | +0.58 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[RANBP10]] | +0.57 | +0.42 / +0.56 | both halves | 4e-05 |  |
| [[ZYG11B]] | +0.55 | +0.40 / +0.55 | both halves | 5e-05 |  |
| [[MORN2]] | +0.55 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[FNBP1]] | +0.55 | +0.45 / +0.51 | both halves | 3e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC03009]] | -0.57 | -0.47 / -0.57 | both halves | 2e-05 |  |
| [[MAT2A]] | -0.55 | -0.42 / -0.60 | both halves | 4e-05 |  |
| [[SRSF1]] | -0.53 | -0.41 / -0.57 | both halves | 4e-05 |  |
| [[NCR3LG1]] | -0.53 | -0.30 / -0.56 | both halves | 2e-04 |  |
| [[ZNF121]] | -0.52 | -0.32 / -0.57 | both halves | 2e-04 |  |
| [[TIGD1]] | -0.50 | -0.41 / -0.46 | both halves | 4e-05 | same gene group |
| [[ZFP69B]] | -0.50 | -0.39 / -0.54 | both halves | 5e-05 |  |
| [[RRN3P1]] | -0.49 | -0.28 / -0.48 | both halves | 3e-04 |  |
| [[ARL5B]] | -0.48 | -0.40 / -0.49 | both halves | 5e-05 |  |
| [[RAB4A-AS1]] | -0.48 | -0.40 / -0.48 | both halves | 5e-05 |  |
| [[TMSB15B]] | -0.48 | -0.29 / -0.49 | both halves | 2e-04 |  |
| [[CYP27B1]] | -0.47 | -0.42 / -0.46 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers HECTD4's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 054]] — Mitochondrial ribosome-associated quality control; 88 genes; this gene is in the **+** arm (projection on the module's main direction 0.306). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-1.2, -21.1); signed map (-24.5, 5.4). **Vector** length 104, 31.6% of its response variance represented; |z| ≥ 3 in 1,133 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +4.2 | +12.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | +3.7 | +5.4 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~40% of this change | +3.0 | +4.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +3.0 | +2.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +2.7 | +2.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.6 | +1.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.5 | +2.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.5 | +3.5 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.2 | +3.1 |
| fall | [[Auranofin (drug)]] 5 µM |  | -9.9 | -14.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -9.6 | -4.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -8.8 | -17.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -8.0 | -4.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -7.1 | -12.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -3.1 | -0.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.7 | -2.2 |
|  | [[Cepharanthine (drug)]] 5 µM |  | -1.7 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | HECT domain E3 ubiquitin protein ligase 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.13 — chr12:112,160,188-112,382,439 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ34154, KIAA0614; previously C12orf51 |
| Gene groups (HGNC) | MicroRNA protein coding host genes; HECT domain E3 ubiquitin protein ligases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y4D8](https://www.uniprot.org/uniprotkb/Q9Y4D8) (Probable E3 ubiquitin-protein ligase HECTD4):

> E3 ubiquitin-protein ligase which accepts ubiquitin from an E2 ubiquitin-conjugating enzyme in the form of a thioester and then directly transfers the ubiquitin to targeted substrates.

**Summary**, from NCBI Gene [283450](https://www.ncbi.nlm.nih.gov/gene/283450):

> Predicted to enable ubiquitin protein ligase activity. Involved in glucose homeostasis and glucose metabolic process. Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26611](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26611) · Entrez [283450](https://www.ncbi.nlm.nih.gov/gene/283450) · UniProt [Q9Y4D8](https://www.uniprot.org/uniprotkb/Q9Y4D8) · Ensembl [ENSG00000173064](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173064)

## Data

Gene col 10334: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10334); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10334, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10334]; `tensor/DDL_lfc|DDL_z.npy` [10334]; `embed/gene_vectors.npy` [10334]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10334 or target_col == 10334). Every well: [[HECTD4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HECTD4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
