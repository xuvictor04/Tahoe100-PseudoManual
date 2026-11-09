---
symbol: "HS2ST1"
type: "gene"
col: 7753
ensembl_id: "ENSG00000153936"
name: "heparan sulfate 2-O-sulfotransferase 1"
location: "1p22.3"
module: 16
arm: "-"
pooled_cpm: 162.28
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 28
n_dd_up_clean: 11
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# HS2ST1

*heparan sulfate 2-O-sulfotransferase 1* — 1p22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.05 µM: 1.57× (z +8.8, q 7e-16, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.417× (z -24.2, q 0e+00, down in 46 of 48 measured lines) ⚠ cell-cycle shift, explains ~36% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.443× (z -15.9, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ADAM10]] (+0.56, fdr 3e-05), [[FAM135A]] (+0.55, fdr 1e-05), [[RIC1]] (+0.52, fdr 1e-05); moves opposite to [[ZKSCAN3]] (-0.53, fdr 3e-05), [[CCDC102A]] (-0.50, fdr 3e-05), [[ZBED9]] (-0.50, fdr 6e-05).
> It sits in the **-** arm of [[Module 016]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 6 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7753.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.05 µM |  | **1.57×** | +8.8 | 7e-16 | 43/48 (J82, LoVo, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.55×** | +8.6 | 2e-15 | 42/48 (LoVo, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.43×** | +7.0 | 5e-10 | 37/48 (LoVo, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.25×** | +6.3 | 5e-08 | 27/48 (HT-29, LS 180, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.25×** | +6.2 | 7e-08 | 24/49 (HOP62, MIA PaCa-2, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.32×** | +5.4 | 7e-06 | 31/48 (A-172, BT-474, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **1.68×** | +5.3 | 8e-06 | 39/49 (LoVo, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.32×** | +5.2 | 1e-05 | 29/48 (HOP62, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.29×** | +5.0 | 3e-05 | 27/48 (LoVo, J82, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.29×** | +4.9 | 5e-05 | 29/49 (HT-29, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.22×** | +3.9 | 0.005 | 23/48 (hTERT-HPNE, RPMI-7951, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **1.21×** | +3.8 | 0.007 | 21/48 (hTERT-HPNE, RPMI-7951, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.21×** | +3.7 | 0.009 | 22/48 (J82, LoVo, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.21×** | +3.7 | 0.009 | 24/48 (hTERT-HPNE, SNU-423, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~88% of this change | **1.20×** | +3.6 | 0.011 | 21/48 (hTERT-HPNE, HOP62, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 5 µM |  | **1.20×** | +3.6 | 0.013 | 23/48 (hTERT-HPNE, SNU-423, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | 1.20× | +3.5 | 0.016 | 21/48 (SNU-423, RPMI-7951, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **1.22×** | +3.4 | 0.019 | 22/47 (SNU-423, RPMI-7951, …) | inconsistent across doses |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | 1.18× | +3.3 | 0.031 | 19/48 (SNU-423, RPMI-7951, …) | top dose only |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | 1.18× | +3.1 | 0.047 | 15/48 (hTERT-HPNE, SNU-423, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 13 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7753.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.417×** | -24.2 | 0e+00 | 46/48 (NCI-H1573, HepG2/C3A, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.443×** | -15.9 | 0e+00 | 47/48 (NCI-H1573, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.525×** | -12.1 | 1e-31 | 42/48 (NCI-H1573, COLO 205, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.567×** | -10.7 | 2e-24 | 41/47 (LoVo, COLO 205, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.640×** | -8.8 | 2e-16 | 42/48 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.652×** | -8.4 | 5e-15 | 43/48 (NCI-H460, SNU-1, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.674×** | -7.7 | 9e-13 | 38/48 (HT-29, C32, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.641×** | -7.7 | 9e-13 | 33/45 (A-427, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.700×** | -7.0 | 2e-10 | 39/48 (COLO 205, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.704×** | -6.9 | 3e-10 | 29/48 (NCI-H1573, KATO III, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.520×** | -6.7 | 1e-09 | 37/48 (Panc 03.27, NCI-H1573, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~58% of this change | **0.718×** | -6.5 | 4e-09 | 34/48 (KATO III, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.725×** | -6.3 | 1e-08 | 28/49 (NCI-H23, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~10% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.726×** | -6.3 | 1e-08 | 35/48 (LS 180, C32, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.543×** | -6.2 | 2e-08 | 39/49 (NCI-H1573, Panc 03.27, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.807×** | -5.9 | 1e-07 | 30/49 (CFPAC-1, LS 180, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.778×** | -4.4 | 4e-04 | 27/47 (RKO, LoVo, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.801×** | -4.3 | 4e-04 | 26/48 (CFPAC-1, SW 900, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.805×** | -4.3 | 5e-04 | 28/47 (SW 900, NCI-H460, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.795×** | -4.2 | 5e-04 | 27/48 (COLO 205, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Mebendazole (drug)]] 5 µM |  | **0.807×** | -4.0 | 0.001 | 25/48 (SW 900, Panc 03.27, …) | rises with dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.760×** | -3.8 | 0.003 | 28/48 (Panc 03.27, A-427, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, -0.51 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7753. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 165 | 0 | 15 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -38.2) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.138× (z -30.3) |
| [[COLO 205 (line)]] | alt | 329 | 0 | 14 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -26.6) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.140× (z -19.8) |
| [[NCI-H460 (line)]] | wt | 111 | 0 | 11 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.293× (z -24.9) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.324× (z -16.1) |
| [[HepG2_C3A (line)]] | wt | 397 | 0 | 9 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.182× (z -27.0) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.348× (z -11.8) |
| [[A-427 (line)]] | wt | 198 | 0 | 8 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.363× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.447× (z -11.6) |
| [[KATO III (line)]] | alt | 168 | 0 | 8 (7 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.304× (z -17.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.497× (z -10.2) |
| [[SW 900 (line)]] | alt | 248 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -18.5) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.257× (z -11.8) |
| [[C32 (line)]] | wt | 263 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -18.7) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.194× (z -15.4) |
| [[LoVo (line)]] | wt | 124 | 2 | 5 (4 ⚠) | [[Belinostat (drug)]] 5 µM 2.03× (z +10.6) | [[Homoharringtonine (drug)]] 5 µM 0.366× (z -21.2) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.363× (z -15.1) |
| [[LS 180 (line)]] | wt | 122 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.462× (z -12.7) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.345× (z -12.4) |
| [[SW480 (line)]] | alt | 183 | 1 (1 ⚠) | 6 (3 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 1.85× (z +9.9) ⚠ cell-cycle shift, explains ~39% of this change | [[Homoharringtonine (drug)]] 5 µM 0.502× (z -16.1) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.449× (z -13.2) |
| [[HT-29 (line)]] | alt | 236 | 2 | 4 (3 ⚠) | [[Tucidinostat (drug)]] 0.5 µM 2.07× (z +10.3) | [[Auranofin (drug)]] 5 µM 0.466× (z -10.9) |
| [[NCI-H23 (line)]] | alt | 172 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.258× (z -19.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.403× (z -13.3) |
| [[Panc 03.27 (line)]] | alt | 148 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -22.2) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.355× (z -11.9) |
| [[SW1417 (line)]] | alt | 192 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.399× (z -15.4) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.410× (z -10.6) |
| [[BT-474 (line)]] | alt | 58.2 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -16.2) ⚠ cell-cycle shift, explains ~36% of this change |
| [[CFPAC-1 (line)]] | alt | 183 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -14.3) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.250× (z -11.0) |
| [[hTERT-HPNE (line)]] | wt | 103 | 4 | 1 (1 ⚠) | [[Triamcinolone (drug)]] 5 µM 2.34× (z +11.4) | [[Homoharringtonine (drug)]] 5 µM 0.479× (z -9.9) ⚠ cell-cycle shift, explains ~36% of this change |
| [[MIA PaCa-2 (line)]] | alt | 187 | 1 (1 ⚠) | 4 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.88× (z +11.9) ⚠ cell-cycle shift, explains ~36% of this change | [[Homoharringtonine (drug)]] 0.05 µM 0.457× (z -10.4) |
| [[RKO (line)]] | wt | 211 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.336× (z -12.2) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.459× (z -9.9) |
| [[SNU-423 (line)]] | alt | 216 | 2 | 3 (2 ⚠) | [[Dexamethasone (drug)]] 0.5 µM 2.56× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.347× (z -13.9) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.385× (z -8.9) |
| [[HCT15 (line)]] | alt | 246 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -19.2) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.389× (z -11.0) |
| [[SW48 (line)]] | wt | 122 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -13.0) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.226× (z -12.3) |
| [[C-33 A (line)]] | alt | 328 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.434× (z -9.5) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 134 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.424× (z -17.8) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.419× (z -12.8) |
| [[HOP62 (line)]] | alt | 89.3 | 2 (2 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.99× (z +12.4) ⚠ cell-cycle shift, explains ~36% of this change | [[Homoharringtonine (drug)]] 5 µM 0.393× (z -16.8) ⚠ cell-cycle shift, explains ~36% of this change |
| [[Hs 766T (line)]] | wt | 161 | 2 (2 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.85× (z +11.0) ⚠ cell-cycle shift, explains ~36% of this change | [[Niclosamide (olamine) (drug)]] 5 µM 0.469× (z -9.2) ⚠ toxic |
| [[HS-578T (line)]] | alt | 152 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.412× (z -13.4) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.324× (z -12.0) |
| [[J82 (line)]] | alt | 127 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.05 µM 2.01× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.497× (z -12.5) ⚠ cell-cycle shift, explains ~36% of this change |
| [[LOX-IMVI (line)]] | wt | 174 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.483× (z -14.3) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.523× (z -9.0) |
| [[RPMI-7951 (line)]] | alt | 156 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.377× (z -14.1) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.363× (z -10.4) |
| [[A-172 (line)]] | wt | 79.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.478× (z -12.2) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.448× (z -9.4) |
| [[A498 (line)]] | wt | 116 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.552× (z -10.5) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.449× (z -10.0) |
| [[A549 (line)]] | wt | 110 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.438× (z -12.7) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.444× (z -8.8) |
| [[AN3 CA (line)]] | alt | 193 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -16.8) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.330× (z -8.9) |
| [[AsPC-1 (line)]] | alt | 87.3 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.395× (z -12.0) ⚠ cell-cycle shift, explains ~36% of this change |
| [[H4 (line)]] | wt | 98.7 | 1 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.03× (z +8.9) ⚠ cell-cycle shift, explains ~36% of this change | [[Homoharringtonine (drug)]] 5 µM 0.439× (z -10.4) ⚠ cell-cycle shift, explains ~36% of this change |
| [[NCI-H1792 (line)]] | alt | 264 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -18.5) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.206× (z -12.9) |
| [[PANC-1 (line)]] | alt | 276 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.523× (z -17.3) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.572× (z -10.5) |
| [[SK-MEL-2 (line)]] | alt | 144 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.586× (z -9.1) ⚠ cell-cycle shift, explains ~36% of this change |
| [[SNU-1 (line)]] | wt | 159 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.05 µM 0.342× (z -10.4) |
| [[CHP-212 (line)]] | wt | 135 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.247× (z -13.1) ⚠ cell-cycle shift, explains ~36% of this change |
| [[NCI-H2030 (line)]] | alt | 59.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.421× (z -10.2) ⚠ cell-cycle shift, explains ~36% of this change |
| [[NCI-H2122 (line)]] | alt | 131 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 47.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 158 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 178 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 183 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 151 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 116 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7753), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*49 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADAM10]] | +0.56 | +0.63 / +0.43 | both halves | 3e-05 |  |
| [[FAM135A]] | +0.55 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[RIC1]] | +0.52 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[UGP2]] | +0.51 | +0.47 / +0.54 | both halves | 2e-05 | pathway: HALLMARK_GLYCOLYSIS |
| [[BRWD3]] | +0.51 | +0.54 / +0.33 | both halves | 1e-04 |  |
| [[KIAA1958]] | +0.50 | +0.59 / +0.45 | both halves | 3e-05 |  |
| [[RALGAPA2]] | +0.50 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[ATP1A1]] | +0.50 | +0.53 / +0.39 | both halves | 5e-05 |  |
| [[TXNDC12]] | +0.50 | +0.51 / +0.44 | both halves | 3e-05 |  |
| [[PRDX4]] | +0.50 | +0.54 / +0.37 | both halves | 8e-05 |  |
| [[ATP1B3]] | +0.49 | +0.50 / +0.45 | both halves | 3e-05 |  |
| [[FBXW7]] | +0.48 | +0.54 / +0.39 | both halves | 6e-05 |  |

## Genes that move opposite

*51 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZKSCAN3]] | -0.53 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[CCDC102A]] | -0.50 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[ZBED9]] | -0.50 | -0.52 / -0.39 | both halves | 6e-05 |  |
| [[TCTN1]] | -0.50 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[TCEANC]] | -0.50 | -0.48 / -0.33 | both halves | 1e-04 |  |
| [[NEPRO-AS1]] | -0.48 | -0.48 / -0.39 | both halves | 5e-05 |  |
| [[ZSCAN26]] | -0.48 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[TTC8]] | -0.48 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[C2orf74]] | -0.48 | -0.53 / -0.30 | both halves | 2e-04 |  |
| [[ZMAT1]] | -0.47 | -0.44 / -0.37 | both halves | 8e-05 |  |
| [[ELAC1]] | -0.47 | -0.51 / -0.26 | both halves | 3e-04 |  |
| [[CCT6P3]] | -0.47 | -0.48 / -0.38 | both halves | 7e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **-** arm (projection on the module's main direction -0.405). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-13.8, 3.5); signed map (-39.7, 18.1). **Vector** length 113, 41.2% of its response variance represented; |z| ≥ 3 in 1,772 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +9.4 | +5.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | +7.4 | -5.7 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +7.2 | +8.6 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | +7.1 | -2.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.3 | -1.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +5.6 | +1.5 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +5.3 | +2.2 |
|  | [[EX229 (drug)]] 5 µM |  | +4.9 | +1.9 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +3.7 | +0.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.6 | +1.9 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -12.5 | -24.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -11.4 | -15.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -8.0 | -7.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -7.4 | -8.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.6 | -4.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.0 | -7.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | -5.6 | -0.7 |
|  | [[Radotinib (drug)]] 5 µM |  | -5.2 | -3.5 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | -3.7 | +0.7 |

## What is on record

|  |  |
|---|---|
| Name | heparan sulfate 2-O-sulfotransferase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p22.3 — chr1:86,914,635-87,109,982 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0448 |
| Gene groups (HGNC) | Sulfotransferases, membrane bound |
| Hallmark sets | GLYCOLYSIS |
| Reactome | 4 pathways, smallest: HS-GAG biosynthesis; Heparan sulfate/heparin (HS-GAG) metabolism; Glycosaminoglycan metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7LGA3](https://www.uniprot.org/uniprotkb/Q7LGA3) (Heparan sulfate 2-O-sulfotransferase 1):

> Catalyzes the transfer of a sulfo group from 3'-phospho-5'-adenylyl sulfate (PAPS) to the 2-OH position of iduronic acid (IdoA) or glucuronic acid (GlcA) within the heparan sulfate (HS) chain and participates in HS biosynthesis (By similarity). Required for metanephric development of kidney formation, suggesting that 2-O-sulfation within HS is essential for signaling between ureteric bud and metanephric mesenchyme (By similarity).

**Summary**, from NCBI Gene [9653](https://www.ncbi.nlm.nih.gov/gene/9653):

> Heparan sulfate biosynthetic enzymes are key components in generating a myriad of distinct heparan sulfate fine structures that carry out multiple biologic activities. This gene encodes a member of the heparan sulfate biosynthetic enzyme family that transfers sulfate to the 2 position of the iduronic acid residue of heparan sulfate. The disruption of this gene resulted in no kidney formation in knockout embryonic mice, indicating that the absence of this enzyme may interfere with the signaling …

**Accessions** — [HGNC:5193](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5193) · Entrez [9653](https://www.ncbi.nlm.nih.gov/gene/9653) · UniProt [Q7LGA3](https://www.uniprot.org/uniprotkb/Q7LGA3) · Ensembl [ENSG00000153936](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000153936)

## Data

Gene col 7753: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7753); `tables/drug_effects.parquet` (55 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7753, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7753]; `tensor/DDL_lfc|DDL_z.npy` [7753]; `embed/gene_vectors.npy` [7753]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7753 or target_col == 7753). Every well: [[HS2ST1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HS2ST1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
