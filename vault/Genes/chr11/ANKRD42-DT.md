---
symbol: "ANKRD42-DT"
type: "gene"
col: 14484
ensembl_id: "ENSG00000247137"
name: "ANKRD42 divergent transcript"
location: "11q14.1"
module: 15
arm: "+"
pooled_cpm: 19.76
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 12
n_dd_up_clean: 9
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# ANKRD42-DT

*ANKRD42 divergent transcript* — 11q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 2.32× (z +15.0, q 0e+00, up in 27 of 37 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.64× (z +13.5, q 6e-39, up in 33 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.615× (z -13.2, q 8e-37, down in 35 of 47 measured lines) ⚠ cell-cycle shift, explains ~36% of this change. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.516× (z -12.2, q 8e-32, down in 33 of 47 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PCF11-AS1]] (+0.82, fdr 7e-06, ⚠ read-through risk), [[TAF11]] (+0.73, fdr 7e-06), [[URM1]] (+0.69, fdr 1e-05), [[RSL1D1-DT]] (+0.69, fdr 3e-05); moves opposite to [[NIN]] (-0.53, fdr 5e-05), [[SSX2IP]] (-0.52, fdr 3e-05), [[ALAS1]] (-0.52, fdr 3e-05).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 7 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14484.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.32×** | +15.0 | 0e+00 | 27/37 (NCI-H460, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.64×** | +13.5 | 6e-39 | 33/47 (HS-578T, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.59×** | +12.7 | 1e-34 | 43/48 (PANC-1, A-427, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.86×** | +11.5 | 2e-28 | 34/44 (KATO III, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.54×** | +8.3 | 9e-15 | 28/47 (SHP-77, RKO, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.51×** | +8.0 | 1e-13 | 31/48 (PANC-1, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.26×** | +6.4 | 1e-08 | 20/48 (HS-578T, SW1417, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.31×** | +5.1 | 3e-05 | 18/47 (HS-578T, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.29×** | +5.0 | 4e-05 | 17/42 (NCI-H460, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.21×** | +3.7 | 0.011 | 6/48 (KATO III, PANC-1, …) | all doses, stronger at high dose |  |
| [[Bimatoprost (drug)]] 0.5 µM |  | **1.21×** | +3.7 | 0.011 | 11/47 (SHP-77, PANC-1, …) | inconsistent across doses |  |
| [[Amsacrine (drug)]] 5 µM |  | 1.14× | +3.6 | 0.014 | 11/48 (NCI-H460, HS-578T, …) | rises with dose |  |
| [[Rapamycin (drug)]] 0.5 µM |  | 1.20× | +3.5 | 0.023 | 8/47 (CFPAC-1, H4, …) | two highest doses |  |
| [[MK-3903 (drug)]] 5 µM |  | **1.40×** | +3.4 | 0.028 | 4/46 (RPMI-7951, SNU-1, …) | top dose only | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | 1.19× | +3.4 | 0.030 | 3/47 (RKO, A-427, …) | rises with dose | position effect removed |
| [[Temsirolimus (drug)]] 0.5 µM |  | 1.18× | +3.1 | 0.060 | 14/47 (SW48, NCI-H460, …) | all doses, flat |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.25×** | +3.1 | 0.063 | 2/47 (C32, Hs 766T) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.25×** | +3.1 | 0.063 | 6/48 (NCI-H460, Hs 766T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 5 µM |  | 1.11× | +3.0 | 0.089 | 4/48 (H4, SHP-77, …) | all doses, flat |  |
| [[Pralsetinib (drug)]] 5 µM |  | **1.34×** | +3.0 | 0.089 | 11/46 (NCI-H2030, J82, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14484.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.615×** | -13.2 | 8e-37 | 35/47 (MIA PaCa-2, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.516×** | -12.2 | 8e-32 | 33/47 (MIA PaCa-2, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.573×** | -10.3 | 2e-22 | 36/46 (PANC-1, J82, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.863× | -9.6 | 1e-19 | 13/48 (A-427, HS-578T, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.637×** | -8.6 | 8e-16 | 30/47 (H4, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.660×** | -8.0 | 2e-13 | 34/48 (LOX-IMVI, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.739×** | -5.8 | 6e-07 | 19/48 (J82, PANC-1, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.784×** | -4.6 | 2e-04 | 15/47 (NCI-H460, A-427, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.846× | -4.5 | 5e-04 | 18/48 (PANC-1, LoVo, …) | top dose only |  |
| [[Gefitinib (drug)]] 5 µM |  | **0.798×** | -4.3 | 1e-03 | 8/48 (SW480, NCI-H1573, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.802×** | -4.2 | 0.001 | 18/47 (J82, PANC-1, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~83% of this change | **0.817×** | -3.7 | 0.010 | 15/34 (A549, LS 180, …) | top dose only | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.830×** | -3.5 | 0.017 | 13/48 (PANC-1, SW 1271, …) | all doses, stronger at high dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.833×** | -3.5 | 0.021 | 12/47 (H4, NCI-H460, …) | two highest doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.848× | -3.1 | 0.065 | 9/47 (PANC-1, HCT15, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.850× | -3.1 | 0.069 | 11/48 (A-172, PANC-1, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.840× | -3.1 | 0.071 | 10/46 (A-172, NCI-H460, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Mebendazole (drug)]] 5 µM |  | 0.847× | -3.0 | 0.076 | 6/48 (SK-MEL-2, NCI-H460, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14484. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 33.1 | 1 (1 ⚠) | 3 (2 ⚠) | [[Selinexor (drug)]] 5 µM 2.01× (z +8.7) ⚠ cell-cycle shift, explains ~27% of this change | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.129× (z -17.0) |
| [[PANC-1 (line)]] | alt | 29.7 | 2 (2 ⚠) | 2 (2 ⚠) | [[Selinexor (drug)]] 5 µM 1.99× (z +11.0) ⚠ cell-cycle shift, explains ~27% of this change | [[Niclosamide (olamine) (drug)]] 5 µM 0.294× (z -13.1) ⚠ toxic |
| [[NCI-H2347 (line)]] | alt | 19.3 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.276× (z -10.0) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 22.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.162× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~83% of this change |
| [[HS-578T (line)]] | alt | 20.9 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.84× (z +10.7) | — |
| [[LOX-IMVI (line)]] | wt | 20.1 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 4.04× (z +8.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.378× (z -9.1) ⚠ cell-cycle shift, explains ~36% of this change |
| [[MIA PaCa-2 (line)]] | alt | 21.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -13.7) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.195× (z -10.7) |
| [[NCI-H460 (line)]] | wt | 15.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.59× (z +11.5) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 30.0 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.97× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.283× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~83% of this change |
| [[SNU-423 (line)]] | alt | 24.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.308× (z -11.9) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.285× (z -8.6) |
| [[SW1417 (line)]] | alt | 27.8 | 1 (1 ⚠) | 1 (1 ⚠) | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.45× (z +9.9) ⚠ toxic | [[Dinaciclib (drug)]] 0.05 µM 0.291× (z -9.5) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 18.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.101× (z -9.8) |
| [[HEC-1-A (line)]] | alt | 17.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.23× (z +8.6) | — |
| [[HepG2_C3A (line)]] | wt | 13.6 | 0 | 1 | — | [[Betamethasone dipropionate (drug)]] 0.05 µM 0.0706× (z -10.7) |
| [[J82 (line)]] | alt | 25.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.247× (z -10.9) ⚠ toxic |
| [[KATO III (line)]] | alt | 22.6 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 4.28× (z +10.7) ⚠ toxic | — |
| [[LoVo (line)]] | wt | 13.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.308× (z -11.4) ⚠ cell-cycle shift, explains ~36% of this change |
| [[LS 180 (line)]] | wt | 19.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.220× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~83% of this change |
| [[NCI-H1573 (line)]] | alt | 20.0 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.73× (z +9.0) ⚠ toxic | — |
| [[NCI-H1792 (line)]] | alt | 15.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.357× (z -9.2) ⚠ cell-cycle shift, explains ~36% of this change |
| [[Panc 03.27 (line)]] | alt | 24.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.230× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~83% of this change |
| [[SW480 (line)]] | alt | 21.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.92× (z +8.8) | — |
| [[A-172 (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 9.88 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 29.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 48.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14484), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PCF11-AS1]] | +0.82 | +0.76 / +0.72 | both halves | 7e-06 | ⚠ **readthrough risk**: PCF11-AS1 lies 0.0 kb 3′ of this gene on the same strand (can correlate by spillover, not regulation) |
| [[TAF11]] | +0.73 | +0.64 / +0.72 | both halves | 7e-06 |  |
| [[URM1]] | +0.69 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[RSL1D1-DT]] | +0.69 | +0.43 / +0.66 | both halves | 3e-05 | same gene group |
| [[NUDT2]] | +0.68 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[ZBTB26]] | +0.68 | +0.53 / +0.66 | both halves | 1e-05 |  |
| [[GLUD1P3]] | +0.67 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[LINC00115]] | +0.67 | +0.50 / +0.63 | both halves | 1e-05 |  |
| [[CAPN10-DT]] | +0.67 | +0.51 / +0.62 | both halves | 1e-05 | same gene group |
| [[DYNLT2]] | +0.66 | +0.43 / +0.60 | both halves | 3e-05 |  |
| [[ZBTB8OS]] | +0.65 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[SLC25A53]] | +0.64 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[ZNF460-AS1]] | +0.62 | +0.47 / +0.55 | both halves | 2e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NIN]] | -0.53 | -0.40 / -0.51 | both halves | 5e-05 |  |
| [[SSX2IP]] | -0.52 | -0.48 / -0.46 | both halves | 3e-05 |  |
| [[ALAS1]] | -0.52 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[ROCK2]] | -0.51 | -0.49 / -0.54 | both halves | 1e-05 |  |
| [[ABCD3]] | -0.51 | -0.32 / -0.49 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ANKRD42-DT's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.680). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-11.2, 23.8); signed map (0.1, -1.5). **Vector** length 97.6, 20.8% of its response variance represented; |z| ≥ 3 in 928 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +8.4 | +12.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.2 | +13.5 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +5.8 | +8.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.8 | +11.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.0 | +8.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | +6.4 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.0 | +2.4 |
|  | [[Bimiralisib (drug)]] 0.05 µM |  | +1.7 | +2.8 |
|  | [[Temsirolimus (drug)]] 5 µM |  | +1.5 | +3.0 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -5.9 | -10.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.7 | -12.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -5.0 | -13.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.0 | -4.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.3 | -8.0 |
|  | [[Gefitinib (drug)]] 5 µM |  | -2.1 | -4.3 |
|  | [[Cepharanthine (drug)]] 5 µM |  | -1.9 | -2.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.9 | -0.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.7 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | ANKRD42 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 11q14.1 — chr11:83,184,491-83,193,794 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55590](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55590) · Entrez [100506282](https://www.ncbi.nlm.nih.gov/gene/100506282) · Ensembl [ENSG00000247137](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000247137)

## Data

Gene col 14484: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14484); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14484, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14484]; `tensor/DDL_lfc|DDL_z.npy` [14484]; `embed/gene_vectors.npy` [14484]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14484 or target_col == 14484). Every well: [[ANKRD42-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANKRD42-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
