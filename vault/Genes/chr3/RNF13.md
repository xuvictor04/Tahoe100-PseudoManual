---
symbol: "RNF13"
type: "gene"
col: 1358
ensembl_id: "ENSG00000082996"
name: "ring finger protein 13"
location: "3q25.1"
module: 169
arm: "+"
pooled_cpm: 137.01
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 19
n_dd_up_clean: 7
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/169"]
generated_by: "tahoemap"
---

# RNF13

*ring finger protein 13* — 3q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 1.55× (z +10.8, q 1e-24, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.515× (z -22.4, q 0e+00, down in 43 of 48 measured lines) ⚠ cell-cycle shift, explains ~36% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.610× (z -12.2, q 4e-32, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SEC24B]] (+0.64, fdr 1e-05), [[NDUFAF7]] (+0.62, fdr 1e-05), [[RTCA]] (+0.62, fdr 2e-05); moves opposite to [[THOC6]] (-0.62, fdr 1e-05), [[PER2]] (-0.58, fdr 1e-05), [[PHF19]] (-0.57, fdr 2e-05).
> It is in [[Module 169]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 5 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1358.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.55×** | +10.8 | 1e-24 | 39/48 (HT-29, COLO 205, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.55×** | +10.1 | 1e-21 | 42/48 (HT-29, LS 180, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.31×** | +9.1 | 3e-17 | 33/48 (J82, BT-474, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.30×** | +8.9 | 6e-17 | 35/48 (J82, HT-29, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.38×** | +8.0 | 1e-13 | 33/48 (HT-29, COLO 205, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.37×** | +7.7 | 2e-12 | 34/49 (NCI-H2347, BT-474, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~78% of this change | **1.27×** | +5.9 | 2e-07 | 27/48 (KATO III, HT-29, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.23×** | +5.2 | 2e-05 | 24/48 (NCI-H2347, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.48×** | +5.0 | 3e-05 | 33/49 (J82, HEC-1-A, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.15× | +4.5 | 3e-04 | 15/48 (MIA PaCa-2, RKO, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.11× | +3.6 | 0.018 | 5/48 (BT-474, A-427, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +3.5 | 0.026 | 18/48 (A-172, J82, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.29×** | +3.3 | 0.041 | 22/48 (LS 180, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~60% of this change | **1.28×** | +3.1 | 0.068 | 20/45 (HT-29, LS 180, …) | all doses, flat | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 5 µM |  | 1.13× | +3.1 | 0.078 | 11/48 (NCI-H1573, AsPC-1, …) | all doses, flat |  |
| [[Budesonide (drug)]] 5 µM |  | 1.13× | +3.0 | 0.091 | 12/48 (NCI-H1573, Panc 03.27, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 5 µM |  | 1.09× | +3.0 | 0.091 | 6/48 (NCI-H1573, Hs 766T, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 13 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1358.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.515×** | -22.4 | 0e+00 | 43/48 (NCI-H460, A498, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.541×** | -14.5 | 3e-45 | 43/48 (A498, PANC-1, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.556×** | -13.9 | 1e-41 | 36/44 (A549, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.594×** | -12.8 | 2e-35 | 32/48 (NCI-H460, KATO III, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.609×** | -12.2 | 3e-32 | 37/49 (A-427, SHP-77, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.610×** | -12.2 | 4e-32 | 38/48 (SW480, A-427, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.639×** | -11.0 | 2e-26 | 43/48 (SW1417, NCI-H460, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.621×** | -10.9 | 1e-25 | 37/45 (A-427, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.656×** | -10.4 | 2e-23 | 35/48 (NCI-H460, KATO III, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.766×** | -6.6 | 3e-09 | 31/48 (NCI-H460, A549, …) | rises with dose |  |
| [[venetoclax (drug)]] 5 µM |  | **0.610×** | -6.4 | 1e-08 | 36/48 (A498, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~63% of this change | **0.773×** | -6.3 | 1e-08 | 34/48 (NCI-H2347, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.788×** | -5.9 | 2e-07 | 35/48 (NCI-H460, A498, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.663×** | -5.3 | 5e-06 | 34/48 (NCI-H460, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.719×** | -4.3 | 8e-04 | 21/48 (CFPAC-1, SW1417, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.724×** | -4.2 | 0.001 | 25/48 (HEC-1-A, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.791×** | -4.1 | 0.001 | 26/48 (NCI-H460, LOX-IMVI, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.829×** | -3.3 | 0.028 | 17/48 (LoVo, SW48, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **0.830×** | -3.3 | 0.029 | 18/49 (SW48, SW 1088, …) | all doses, flat | plate-row cell shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | 0.883× | -2.9 | 0.086 | 17/48 (HS-578T, NCI-H1792, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1358. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 107 | 4 (2 ⚠) | 11 (11 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.20× (z +11.0) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 1.89× (z +9.4) | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -25.7) ⚠ cell-cycle shift, explains ~36% of this change |
| [[A549 (line)]] | wt | 161 | 0 | 9 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.323× (z -22.2) ⚠ cell-cycle shift, explains ~36% of this change |
| [[HT-29 (line)]] | alt | 120 | 4 (2 ⚠) | 4 (3 ⚠) | [[Bortezomib (drug)]] 0.05 µM 3.31× (z +16.2) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.68× (z +14.1) | [[Digitoxin (drug)]] 5 µM 0.418× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.473× (z -10.7) |
| [[LS 180 (line)]] | wt | 157 | 3 (1 ⚠) | 5 (5 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.57× (z +12.4) | [[Dinaciclib (drug)]] 5 µM 0.385× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[PANC-1 (line)]] | alt | 180 | 0 | 8 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.394× (z -21.8) ⚠ cell-cycle shift, explains ~36% of this change |
| [[SW480 (line)]] | alt | 169 | 2 (1 ⚠) | 6 (5 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 1.62× (z +8.7) | [[Auranofin (drug)]] 5 µM 0.443× (z -14.7) |
| [[A498 (line)]] | wt | 142 | 0 | 7 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -24.4) ⚠ cell-cycle shift, explains ~36% of this change |
| [[C32 (line)]] | wt | 112 | 4 (2 ⚠) | 3 (3 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.63× (z +10.6) | [[Homoharringtonine (drug)]] 5 µM 0.396× (z -14.0) ⚠ cell-cycle shift, explains ~36% of this change |
| [[HOP62 (line)]] | alt | 108 | 2 | 5 (5 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.06× (z +9.5) | [[Homoharringtonine (drug)]] 5 µM 0.488× (z -12.9) ⚠ cell-cycle shift, explains ~36% of this change |
| [[NCI-H2347 (line)]] | alt | 139 | 2 (1 ⚠) | 4 (4 ⚠) | [[Selinexor (drug)]] 5 µM 1.57× (z +9.2) ⚠ cell-cycle shift, explains ~60% of this change · without an alert: [[Tucidinostat (drug)]] 0.5 µM 1.80× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.494× (z -14.5) ⚠ cell-cycle shift, explains ~36% of this change |
| [[SK-MEL-2 (line)]] | alt | 173 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.297× (z -21.0) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.398× (z -11.7) |
| [[SW1417 (line)]] | alt | 166 | 0 | 6 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.503× (z -14.7) ⚠ cell-cycle shift, explains ~36% of this change |
| [[A-427 (line)]] | wt | 280 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.238× (z -18.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.402× (z -12.9) |
| [[HS-578T (line)]] | alt | 187 | 0 | 5 (5 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.237× (z -18.3) ⚠ cell-cycle shift, explains ~33% of this change |
| [[J82 (line)]] | alt | 130 | 2 (1 ⚠) | 3 (3 ⚠) | [[Selinexor (drug)]] 5 µM 1.63× (z +9.8) ⚠ cell-cycle shift, explains ~60% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 1.59× (z +9.2) | [[Harringtonine (drug)]] 5 µM 0.469× (z -10.8) ⚠ cell-cycle shift, explains ~33% of this change |
| [[KATO III (line)]] | alt | 158 | 3 (1 ⚠) | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.04× (z +10.6) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.364× (z -15.0) ⚠ cell-cycle shift, explains ~34% of this change |
| [[NCI-H1573 (line)]] | alt | 165 | 3 (1 ⚠) | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.33× (z +11.5) | [[Homoharringtonine (drug)]] 5 µM 0.295× (z -22.7) ⚠ cell-cycle shift, explains ~36% of this change |
| [[AsPC-1 (line)]] | alt | 104 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.298× (z -19.0) ⚠ cell-cycle shift, explains ~36% of this change |
| [[COLO 205 (line)]] | alt | 134 | 3 (1 ⚠) | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 3.12× (z +12.4) | [[Homoharringtonine (drug)]] 5 µM 0.334× (z -16.5) ⚠ cell-cycle shift, explains ~36% of this change |
| [[HEC-1-A (line)]] | alt | 111 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.426× (z -12.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.505× (z -10.6) |
| [[hTERT-HPNE (line)]] | wt | 120 | 0 | 4 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.194× (z -16.5) ⚠ cell-cycle shift, explains ~33% of this change |
| [[LoVo (line)]] | wt | 124 | 1 | 3 (2 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 1.78× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -22.1) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.501× (z -10.3) |
| [[NCI-H1792 (line)]] | alt | 111 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -20.1) ⚠ cell-cycle shift, explains ~36% of this change |
| [[SNU-423 (line)]] | alt | 102 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -23.0) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.481× (z -9.3) |
| [[A-172 (line)]] | wt | 98.8 | 0 | 3 (2 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.484× (z -9.4) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.500× (z -9.0) |
| [[BT-474 (line)]] | alt | 101 | 2 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.31× (z +9.4) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.433× (z -9.4) ⚠ cell-cycle shift, explains ~34% of this change |
| [[H4 (line)]] | wt | 170 | 0 | 3 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.334× (z -11.7) ⚠ cell-cycle shift, explains ~34% of this change |
| [[MIA PaCa-2 (line)]] | alt | 157 | 1 | 2 (1 ⚠) | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 1.70× (z +8.8) | [[Auranofin (drug)]] 5 µM 0.383× (z -12.0) |
| [[NCI-H2030 (line)]] | alt | 130 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.355× (z -12.4) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 160 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.444× (z -15.1) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.468× (z -10.3) |
| [[Panc 03.27 (line)]] | alt | 195 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.464× (z -16.9) ⚠ cell-cycle shift, explains ~36% of this change |
| [[RPMI-7951 (line)]] | alt | 143 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.498× (z -11.4) ⚠ cell-cycle shift, explains ~36% of this change |
| [[SHP-77 (line)]] | alt | 178 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.320× (z -16.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[SW 900 (line)]] | alt | 97.0 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.209× (z -14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[CFPAC-1 (line)]] | alt | 113 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.493× (z -13.4) ⚠ cell-cycle shift, explains ~36% of this change |
| [[HepG2_C3A (line)]] | wt | 90.6 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.404× (z -11.6) ⚠ cell-cycle shift, explains ~36% of this change |
| [[LOX-IMVI (line)]] | wt | 110 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.512× (z -12.6) ⚠ cell-cycle shift, explains ~36% of this change |
| [[RKO (line)]] | wt | 79.8 | 1 (1 ⚠) | 1 (1 ⚠) | [[Selinexor (drug)]] 5 µM 1.82× (z +8.6) ⚠ cell-cycle shift, explains ~60% of this change | [[Homoharringtonine (drug)]] 5 µM 0.555× (z -8.7) ⚠ cell-cycle shift, explains ~36% of this change |
| [[SNU-1 (line)]] | wt | 116 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.439× (z -10.5) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.379× (z -9.1) |
| [[SW48 (line)]] | wt | 128 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.289× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[AN3 CA (line)]] | alt | 88.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.320× (z -9.8) ⚠ cell-cycle shift, explains ~36% of this change |
| [[NCI-H596 (line)]] | alt | 134 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 5 µM 0.0641× (z -9.0) |
| [[SW 1088 (line)]] | alt | 104 | 0 | 1 | — | [[Ferulic acid (drug)]] 0.05 µM 0.0838× (z -9.6) |
| [[C-33 A (line)]] | alt | 73.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 92.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 67.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 184 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 129 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1358), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEC24B]] | +0.64 | +0.67 / +0.49 | both halves | 1e-05 |  |
| [[NDUFAF7]] | +0.62 | +0.63 / +0.57 | both halves | 1e-05 |  |
| [[RTCA]] | +0.62 | +0.71 / +0.47 | both halves | 2e-05 |  |
| [[EVI5]] | +0.59 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[REXO2]] | +0.58 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[PPHLN1]] | +0.57 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[JKAMP]] | +0.56 | +0.61 / +0.46 | both halves | 3e-05 |  |
| [[SLC38A9]] | +0.56 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[PSMA6]] | +0.56 | +0.63 / +0.41 | both halves | 4e-05 |  |
| [[ATG5]] | +0.56 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[SNX4]] | +0.55 | +0.60 / +0.45 | both halves | 3e-05 |  |
| [[PSMA2]] | +0.55 | +0.57 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[THOC6]] | -0.62 | -0.61 / -0.55 | both halves | 1e-05 |  |
| [[PER2]] | -0.58 | -0.64 / -0.49 | both halves | 1e-05 |  |
| [[PHF19]] | -0.57 | -0.63 / -0.47 | both halves | 2e-05 |  |
| [[AGRN]] | -0.54 | -0.58 / -0.45 | both halves | 3e-05 |  |
| [[CELSR3]] | -0.54 | -0.57 / -0.40 | both halves | 5e-05 |  |
| [[KDM6B]] | -0.53 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[VEZF1]] | -0.51 | -0.57 / -0.41 | both halves | 4e-05 |  |
| [[DPY19L2P2]] | -0.51 | -0.50 / -0.42 | both halves | 4e-05 |  |
| [[CDC42EP1]] | -0.51 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[RELB]] | -0.51 | -0.63 / -0.42 | both halves | 4e-05 |  |
| [[BAHCC1]] | -0.51 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[ZBTB1]] | -0.50 | -0.56 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers RNF13's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[PSMB5]] | B | PSMB5 activity lowers RNF13's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 169]]; 25 genes; every member is in the + arm (projection on the module's main direction 0.631). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-2.3, -13.9); signed map (-35.7, -8.3). **Vector** length 126, 40.9% of its response variance represented; |z| ≥ 3 in 1,414 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~32% of this change | +11.3 | +10.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +10.9 | +10.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +10.8 | +8.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | +8.8 | +8.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.0 | +9.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.1 | +2.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.6 | +2.3 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +3.4 | +1.7 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -12.6 | -22.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -9.3 | -14.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -7.1 | -12.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | -6.3 | -13.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | -5.7 | -6.6 |
|  | [[venetoclax (drug)]] 5 µM |  | -4.1 | -6.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.6 | -4.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.0 | -5.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.9 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | ring finger protein 13 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q25.1 — chr3:149,812,770-149,962,139 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RZF |
| Gene groups (HGNC) | Ring finger proteins; RING finger E3 ubiquitin protein ligases |
| Matched by | ensembl_id |

**Function**, from UniProt [O43567](https://www.uniprot.org/uniprotkb/O43567) (E3 ubiquitin-protein ligase RNF13):

> E3 ubiquitin-protein ligase that regulates cell proliferation. Involved in apoptosis regulation. Mediates ER stress-induced activation of JNK signaling pathway and apoptosis by promoting ERN1 activation and splicing of XBP1 mRNA. Also involved in protein trafficking and localization.

**Summary**, from NCBI Gene [11342](https://www.ncbi.nlm.nih.gov/gene/11342):

> The protein encoded by this gene contains a RING zinc finger, a motif known to be involved in protein-protein interactions. The specific function of this gene has not yet been determined. Alternatively spliced transcript variants that encode the same protein have been reported. A pseudogene, which is also located on chromosome 3, has been defined for this gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:10057](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10057) · Entrez [11342](https://www.ncbi.nlm.nih.gov/gene/11342) · UniProt [O43567](https://www.uniprot.org/uniprotkb/O43567) · Ensembl [ENSG00000082996](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000082996)

## Data

Gene col 1358: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1358); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1358, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1358]; `tensor/DDL_lfc|DDL_z.npy` [1358]; `embed/gene_vectors.npy` [1358]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1358 or target_col == 1358). Every well: [[RNF13 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RNF13.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
