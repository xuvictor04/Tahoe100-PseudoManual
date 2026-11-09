---
symbol: "SSR1"
type: "gene"
col: 4568
ensembl_id: "ENSG00000124783"
name: "signal sequence receptor subunit 1"
location: "6p24.3"
module: 42
arm: "+"
pooled_cpm: 174.36
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 14
n_dd_up_clean: 4
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/042"]
generated_by: "tahoemap"
---

# SSR1

*signal sequence receptor subunit 1* — 6p24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.80× (z +16.3, q 0e+00, up in 43 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Abemaciclib (drug)]] 5 µM: 1.52× (z +6.0, q 2e-07, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.634× (z -17.0, q 0e+00, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SEC61A1]] (+0.78, fdr 7e-06), [[SSR3]] (+0.77, fdr 7e-06), [[SRPRA]] (+0.75, fdr 7e-06).
> It is in [[Module 042]], a single-armed module (UPR ER).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 5 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4568.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.80×** | +16.3 | 0e+00 | 43/49 (HOP62, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.83×** | +16.1 | 0e+00 | 39/44 (HOP62, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.55×** | +11.2 | 6e-27 | 34/45 (HOP62, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.30×** | +7.3 | 4e-11 | 33/48 (SW480, NCI-H2347, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.52×** | +6.0 | 2e-07 | 38/48 (SW480, NCI-H2347, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.48×** | +5.7 | 1e-06 | 32/48 (NCI-H2347, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.39×** | +4.8 | 2e-04 | 29/48 (SW480, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.23×** | +4.1 | 0.003 | 24/48 (CFPAC-1, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | 1.14× | +3.6 | 0.018 | 14/48 (SNU-423, HT-29, …) | top dose only |  |
| [[Fluvoxamine (maleate) (drug)]] 0.5 µM |  | 1.14× | +3.6 | 0.018 | 10/48 (NCI-H2347, LS 180, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~44% of this change | 1.14× | +3.6 | 0.018 | 17/48 (A-427, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Terfenadine (drug)]] 0.5 µM |  | 1.14× | +3.5 | 0.019 | 9/48 (PANC-1, LS 180, …) | two highest doses |  |
| [[EX229 (drug)]] 0.05 µM |  | 1.14× | +3.4 | 0.027 | 13/48 (LoVo, CFPAC-1, …) | all doses, flat |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | 1.18× | +3.3 | 0.035 | 18/48 (COLO 205, CFPAC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Cilostazol (drug)]] 0.05 µM |  | 1.13× | +3.2 | 0.051 | 13/48 (BT-474, CFPAC-1, …) | inconsistent across doses | position effect removed |
| [[EX229 (drug)]] 0.5 µM |  | 1.17× | +3.2 | 0.051 | 14/49 (COLO 205, CFPAC-1, …) | all doses, flat | plate-row cell shift; noisy plate (z scaled) |
| [[Tofacitinib (drug)]] 0.5 µM |  | 1.12× | +3.1 | 0.068 | 17/49 (KATO III, RPMI-7951, …) | inconsistent across doses |  |
| [[Lipoic acid (drug)]] 5 µM |  | 1.09× | +3.0 | 0.090 | 1/48 (SW480) | top dose only |  |
| [[Arbutin (drug)]] 5 µM |  | 1.12× | +3.0 | 0.090 | 4/48 (BT-474, HCT15, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4568.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.634×** | -17.0 | 0e+00 | 43/48 (J82, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.718×** | -9.1 | 2e-17 | 37/48 (LS 180, KATO III, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.803×** | -8.2 | 6e-14 | 26/49 (LoVo, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.748×** | -7.7 | 2e-12 | 27/48 (J82, A-172, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.754×** | -7.3 | 2e-11 | 38/48 (HT-29, LS 180, …) | all doses, flat | cell-cycle shift (explains ~17% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.835× | -7.0 | 3e-10 | 24/48 (J82, HEC-1-A, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | 0.840× | -6.4 | 1e-08 | 20/48 (RPMI-7951, J82, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.797×** | -6.2 | 3e-08 | 27/48 (KATO III, LS 180, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.812×** | -5.7 | 6e-07 | 25/48 (A-427, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Verteporfin (drug)]] 5 µM |  | **0.818×** | -5.3 | 6e-06 | 27/49 (NCI-H2030, HOP62, …) | top dose only |  |
| [[Cepharanthine (drug)]] 5 µM |  | 0.876× | -4.9 | 5e-05 | 12/48 (BT-474, A-427, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | 0.849× | -4.3 | 7e-04 | 21/47 (hTERT-HPNE, C32, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.859× | -4.2 | 0.001 | 17/48 (RPMI-7951, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.816×** | -4.0 | 0.003 | 20/49 (HOP62, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Rapamycin (drug)]] 5 µM |  | 0.899× | -3.8 | 0.005 | 4/48 (CFPAC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | 0.872× | -3.8 | 0.006 | 14/49 (H4, HCT15, …) | inconsistent across doses |  |
| [[Lidocaine (hydrochloride) (drug)]] 5 µM |  | 0.904× | -3.7 | 0.007 | 5/48 (HT-29, RKO, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4568. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 254 | 1 (1 ⚠) | 5 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 1.81× (z +9.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -31.1) |
| [[A-172 (line)]] | wt | 125 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 3.27× (z +16.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.466× (z -14.5) |
| [[HOP62 (line)]] | alt | 205 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.66× (z +18.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.644× (z -11.5) |
| [[NCI-H1573 (line)]] | alt | 140 | 3 (2 ⚠) | 2 | [[Homoharringtonine (drug)]] 0.5 µM 2.82× (z +13.1) | [[Ixazomib citrate (drug)]] 0.5 µM 0.485× (z -9.1) |
| [[RPMI-7951 (line)]] | alt | 169 | 2 (2 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.13× (z +9.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.377× (z -16.5) |
| [[SNU-423 (line)]] | alt | 176 | 4 (4 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.93× (z +17.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.468× (z -13.4) |
| [[A-427 (line)]] | wt | 164 | 1 (1 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 1.98× (z +11.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.451× (z -18.7) |
| [[A498 (line)]] | wt | 129 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 1.96× (z +10.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.403× (z -19.8) |
| [[HS-578T (line)]] | alt | 220 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.30× (z +17.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.493× (z -13.5) |
| [[LS 180 (line)]] | wt | 330 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.547× (z -13.5) |
| [[AN3 CA (line)]] | alt | 133 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.24× (z +8.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -11.5) |
| [[C32 (line)]] | wt | 135 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.36× (z +14.0) ⚠ toxic; transcription drop | [[Ixazomib citrate (drug)]] 5 µM 0.476× (z -8.9) |
| [[CFPAC-1 (line)]] | alt | 143 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.27× (z +12.9) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 169 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.26× (z +12.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.475× (z -14.8) |
| [[NCI-H2347 (line)]] | alt | 130 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 1.69× (z +8.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.473× (z -16.7) |
| [[SW 900 (line)]] | alt | 171 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 1.91× (z +9.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.521× (z -12.8) |
| [[A549 (line)]] | wt | 112 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.77× (z +14.9) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 96.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.59× (z +12.0) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 259 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.59× (z +12.4) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 176 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.07× (z +10.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.645× (z -8.5) |
| [[HT-29 (line)]] | alt | 210 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.501× (z -12.8) |
| [[hTERT-HPNE (line)]] | wt | 188 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 1.91× (z +8.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.450× (z -14.0) |
| [[KATO III (line)]] | alt | 300 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 5 µM 0.450× (z -10.7) |
| [[LOX-IMVI (line)]] | wt | 148 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.39× (z +12.0) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 159 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.18× (z +14.2) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 140 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 1.84× (z +8.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.539× (z -12.7) |
| [[PANC-1 (line)]] | alt | 154 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.16× (z +14.0) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 165 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.04× (z +10.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.515× (z -12.6) |
| [[SK-MEL-2 (line)]] | alt | 106 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.87× (z +13.7) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 220 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.447× (z -13.3) |
| [[SW1417 (line)]] | alt | 127 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 1.77× (z +8.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.634× (z -9.2) |
| [[SW480 (line)]] | alt | 177 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.581× (z -13.4) |
| [[COLO 205 (line)]] | alt | 201 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.49× (z +8.9) | — |
| [[H4 (line)]] | wt | 166 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.469× (z -8.8) |
| [[HEC-1-A (line)]] | alt | 184 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.614× (z -10.1) |
| [[LoVo (line)]] | wt | 268 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.423× (z -18.6) |
| [[MIA PaCa-2 (line)]] | alt | 172 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.39× (z +9.8) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 180 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.90× (z +9.5) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 138 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.39× (z +11.8) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 193 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.616× (z -8.7) |
| [[BT-474 (line)]] | alt | 126 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 169 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 139 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 278 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 132 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 164 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 213 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 196 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 192 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 190 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4568), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEC61A1]] | +0.78 | +0.75 / +0.74 | both halves | 7e-06 | pathway: Cotranslational targeting of proteins to the endoplasmic reticulum; STRING 987 |
| [[SSR3]] | +0.77 | +0.76 / +0.74 | both halves | 7e-06 | same gene group; pathway: Cotranslational targeting of proteins to the endoplasmic reticulum; STRING 999 |
| [[SRPRA]] | +0.75 | +0.79 / +0.67 | both halves | 7e-06 | pathway: HALLMARK_UNFOLDED_PROTEIN_RESPONSE; STRING 752 |
| [[TMED2]] | +0.74 | +0.77 / +0.71 | both halves | 7e-06 | STRING 536 |
| [[TMEM214]] | +0.74 | +0.73 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[COPG1]] | +0.72 | +0.66 / +0.72 | both halves | 7e-06 |  |
| [[STT3A]] | +0.72 | +0.71 / +0.66 | both halves | 7e-06 | pathway: Cotranslational targeting of proteins to the endoplasmic reticulum; STRING 940 |
| [[SEC63]] | +0.72 | +0.64 / +0.71 | both halves | 7e-06 | STRING 708 |
| [[PDIA4]] | +0.71 | +0.70 / +0.67 | both halves | 7e-06 |  |
| [[OSTC]] | +0.71 | +0.73 / +0.64 | both halves | 7e-06 | pathway: Cotranslational targeting of proteins to the endoplasmic reticulum; STRING 900 |
| [[TMED7]] | +0.71 | +0.70 / +0.63 | both halves | 7e-06 |  |
| [[CALU]] | +0.70 | +0.68 / +0.64 | both halves | 7e-06 | STRING 410 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 042]] — UPR ER; 103 genes; every member is in the + arm (projection on the module's main direction 0.789). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.1, -30.5); signed map (-55.5, 8.8). **Vector** length 132, 42.7% of its response variance represented; |z| ≥ 3 in 1,173 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *UPR ER* (control, mean cos +0.62 to 11); *Asparagine N-linked glycosylation* (reactome, mean cos +0.56 to 23); *Maturation of DENV proteins* (reactome, mean cos +0.61 to 11).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.3 | +7.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.7 | +16.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +4.5 | +6.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.3 | +16.3 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +4.3 | +4.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | +4.0 | +5.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.6 | +4.8 |
|  | [[EX229 (drug)]] 0.05 µM |  | +3.3 | +3.4 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -8.0 | -9.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -7.7 | -6.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -6.0 | -7.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.3 | -17.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.1 | -7.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.8 | -7.0 |
|  | [[Rapamycin (drug)]] 5 µM |  | -3.8 | -3.8 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -3.6 | -3.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -3.4 | -4.0 |

## What is on record

|  |  |
|---|---|
| Name | signal sequence receptor subunit 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p24.3 — chr6:7,268,306-7,347,446 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TRAPA |
| Gene groups (HGNC) | Minor histocompatibility antigens; Translocon associated protein complex subunits |
| Hallmark sets | UNFOLDED_PROTEIN_RESPONSE, MTORC1_SIGNALING |
| Reactome | 7 pathways, smallest: XBP1(S) activates chaperone genes; IRE1alpha activates chaperones; Unfolded Protein Response (UPR) |
| Matched by | ensembl_id |

**Function**, from UniProt [P43307](https://www.uniprot.org/uniprotkb/P43307) (Translocon-associated protein subunit alpha):

> TRAP proteins are part of a complex whose function is to bind calcium to the ER membrane and thereby regulate the retention of ER resident proteins. May be involved in the recycling of the translocation apparatus after completion of the translocation process or may function as a membrane-bound chaperone facilitating folding of translocated proteins.

**Summary**, from NCBI Gene [6745](https://www.ncbi.nlm.nih.gov/gene/6745):

> The signal sequence receptor (SSR) is a glycosylated endoplasmic reticulum (ER) membrane receptor associated with protein translocation across the ER membrane. The SSR consists of 2 subunits, a 34-kD glycoprotein encoded by this gene and a 22-kD glycoprotein. This gene generates several mRNA species as a result of complex alternative polyadenylation. This gene is unusual in that it utilizes arrays of polyA signal sequences that are mostly non-canonical. Multiple transcript variants encoding …

**Accessions** — [HGNC:11323](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11323) · Entrez [6745](https://www.ncbi.nlm.nih.gov/gene/6745) · UniProt [P43307](https://www.uniprot.org/uniprotkb/P43307) · Ensembl [ENSG00000124783](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000124783)

## Data

Gene col 4568: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4568); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4568, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4568]; `tensor/DDL_lfc|DDL_z.npy` [4568]; `embed/gene_vectors.npy` [4568]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4568 or target_col == 4568). Every well: [[SSR1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SSR1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
