---
symbol: "TMEFF1"
type: "gene"
col: 14284
ensembl_id: "ENSG00000241697"
name: "transmembrane protein with EGF like and two follistatin like domains 1"
location: "9q31.1"
module: 181
arm: "+"
pooled_cpm: 31.06
n_lines_expressing: 45
n_dd_up: 18
n_dd_down: 22
n_dd_up_clean: 13
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 6
direction_downstream: 2
tags: ["gene", "module/181"]
generated_by: "tahoemap"
---

# TMEFF1

*transmembrane protein with EGF like and two follistatin like domains 1* — 9q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.84× (z +24.3, q 0e+00, up in 38 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.456× (z -13.3, q 2e-37, down in 34 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CAVIN4]] (+0.86, fdr 7e-06, ⚠ same locus), [[MSANTD3-TMEFF1]] (+0.80, fdr 7e-06, ⚠ same locus), [[MSANTD3]] (+0.67, fdr 1e-05, ⚠ same locus), [[AMPD3]] (+0.64, fdr 7e-06), [[GRK4]] (+0.60, fdr 1e-05), [[PIK3IP1-DT]] (+0.59, fdr 1e-05); moves opposite to [[MPPE1]] (-0.50, fdr 5e-05), [[C1GALT1C1]] (-0.50, fdr 6e-04), [[CDC42SE2]] (-0.50, fdr 3e-05).
> It is in [[Module 181]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[AFF3]] → it (grade B ⚠); 2 go from it, the strongest it → [[GPR156]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14284.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.84×** | +24.3 | 0e+00 | 38/42 (LOX-IMVI, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **9.68×** | +20.1 | 0e+00 | 41/43 (NCI-H460, A-172, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **2.01×** | +11.8 | 7e-30 | 31/43 (RKO, SW480, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.82×** | +10.1 | 8e-22 | 30/42 (NCI-H460, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.70×** | +8.8 | 2e-16 | 33/43 (A-172, HS-578T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.70×** | +8.6 | 8e-16 | 30/43 (Hs 766T, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.34×** | +7.5 | 5e-12 | 18/30 (A-172, HOP62, …) | rises with dose | noisy plate (z scaled) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.40×** | +5.7 | 6e-07 | 22/43 (A498, BT-474, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.33×** | +4.6 | 2e-04 | 17/42 (NCI-H2347, Panc 03.27, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.22×** | +4.6 | 3e-04 | 21/43 (MIA PaCa-2, NCI-H1573, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.30×** | +4.5 | 4e-04 | 19/43 (RKO, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | 1.20× | +4.2 | 0.001 | 11/43 (J82, PANC-1, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.26×** | +4.0 | 0.003 | 12/43 (SW480, NCI-H460, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.26×** | +3.9 | 0.003 | 11/43 (C-33 A, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.26×** | +3.9 | 0.004 | 15/42 (Panc 03.27, NCI-H2030, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.52×** | +3.7 | 0.008 | 12/43 (NCI-H460, RKO, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.24×** | +3.7 | 0.008 | 12/43 (COLO 205, CFPAC-1, …) | rises with dose |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **1.22×** | +3.3 | 0.029 | 12/42 (Hs 766T, PANC-1, …) | rises with dose |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 1.20× | +3.0 | 0.064 | 10/43 (NCI-H460, LOX-IMVI, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 7 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14284.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.456×** | -13.3 | 2e-37 | 34/43 (HEC-1-A, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.508×** | -11.5 | 6e-28 | 34/43 (HEC-1-A, HS-578T, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.572×** | -9.5 | 6e-19 | 30/43 (HEC-1-A, HS-578T, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **0.630×** | -7.5 | 9e-12 | 22/30 (HEC-1-A, SHP-77, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | **0.679×** | -6.5 | 7e-09 | 23/39 (C32, HEC-1-A, …) | rises with dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.682×** | -6.5 | 9e-09 | 24/43 (HCT15, HS-578T, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | **0.689×** | -6.1 | 1e-07 | 24/41 (HCT15, AN3 CA, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM |  | **0.508×** | -6.0 | 1e-07 | 24/41 (A549, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **0.756×** | -4.7 | 1e-04 | 17/43 (C32, HEC-1-A, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.762×** | -4.6 | 3e-04 | 21/43 (A498, NCI-H460, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.778×** | -4.2 | 0.001 | 16/43 (A498, NCI-H1573, …) | all doses, flat |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.792×** | -3.9 | 0.004 | 17/43 (HEC-1-A, PANC-1, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.833×** | -3.5 | 0.019 | 16/43 (NCI-H23, Panc 03.27, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Berbamine (drug)]] 0.05 µM |  | **0.816×** | -3.4 | 0.023 | 8/43 (NCI-H460, A-172, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.818×** | -3.4 | 0.025 | 17/43 (NCI-H2347, A549, …) | all doses, flat |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.747×** | -3.4 | 0.025 | 10/41 (SNU-423, NCI-H1792, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[AZD-7648 (drug)]] 5 µM |  | **0.683×** | -3.4 | 0.025 | 10/40 (HEC-1-A, A549, …) | rises with dose | noisy plate (z scaled) |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **0.824×** | -3.3 | 0.031 | 12/43 (A498, SW 1088, …) | inconsistent across doses |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **0.831×** | -3.1 | 0.048 | 13/43 (NCI-H460, SHP-77, …) | two highest doses |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.764×** | -3.1 | 0.049 | 12/43 (HOP62, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.829×** | -3.0 | 0.070 | 10/43 (NCI-H661, Hs 766T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.37 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14284. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 101 | 4 (1 ⚠) | 5 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 25.7× (z +16.0) | [[Panobinostat (drug)]] 5 µM 0.201× (z -15.1) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.284× (z -11.8) |
| [[HEC-1-A (line)]] | alt | 65.8 | 1 | 6 (5 ⚠) | [[TAK-901 (drug)]] 5 µM 10.2× (z +11.0) | [[Dinaciclib (drug)]] 0.5 µM 0.152× (z -17.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.160× (z -16.7) |
| [[RPMI-7951 (line)]] | alt | 74.9 | 3 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.25× (z +15.8) | [[Dinaciclib (drug)]] 0.05 µM 0.156× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.322× (z -9.0) |
| [[HS-578T (line)]] | alt | 62.8 | 2 | 4 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 16.5× (z +12.5) | [[Panobinostat (drug)]] 5 µM 0.156× (z -15.8) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.195× (z -13.9) |
| [[Hs 766T (line)]] | wt | 35.0 | 3 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.71× (z +15.9) | [[Panobinostat (drug)]] 0.5 µM 0.304× (z -8.9) |
| [[hTERT-HPNE (line)]] | wt | 59.3 | 1 | 4 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 20.2× (z +10.6) | [[Panobinostat (drug)]] 0.5 µM 0.253× (z -9.3) |
| [[A498 (line)]] | wt | 17.3 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +10.0) | — |
| [[NCI-H460 (line)]] | wt | 35.0 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.42× (z +19.2) | — |
| [[RKO (line)]] | wt | 23.5 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.05× (z +15.0) | — |
| [[SNU-423 (line)]] | alt | 56.6 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.16× (z +20.2) | [[Panobinostat (drug)]] 5 µM 0.341× (z -9.5) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.348× (z -9.4) |
| [[A549 (line)]] | wt | 41.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.48× (z +15.2) | — |
| [[J82 (line)]] | alt | 55.3 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.06× (z +16.1) | [[Dinaciclib (drug)]] 0.5 µM 0.263× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change |
| [[LOX-IMVI (line)]] | wt | 25.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.0× (z +22.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 59.0 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.214× (z -11.1) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.237× (z -10.4) |
| [[AN3 CA (line)]] | alt | 39.6 | 0 | 2 (1 ⚠) | — | [[Hesperidin (drug)]] 5 µM 0.0907× (z -9.0) |
| [[H4 (line)]] | wt | 73.6 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 15.2× (z +9.2) | [[Belinostat (drug)]] 5 µM 0.202× (z -10.3) ⚠ cell-cycle shift, explains ~34% of this change |
| [[HCT15 (line)]] | alt | 23.4 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.150× (z -8.9) ⚠ toxic; cell-cycle shift, explains ~34% of this change |
| [[HOP62 (line)]] | alt | 51.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.51× (z +13.7) | — |
| [[LoVo (line)]] | wt | 8.92 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.39× (z +14.8) | — |
| [[NCI-H1792 (line)]] | alt | 50.4 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 8.14× (z +9.7) | [[Panobinostat (drug)]] 0.5 µM 0.372× (z -8.8) |
| [[NCI-H2030 (line)]] | alt | 17.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.20× (z +15.0) | — |
| [[NCI-H23 (line)]] | alt | 32.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.81× (z +13.3) | — |
| [[PANC-1 (line)]] | alt | 26.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +13.3) | — |
| [[SHP-77 (line)]] | alt | 43.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.178× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[SK-MEL-2 (line)]] | alt | 29.9 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.35× (z +13.2) | [[Dinaciclib (drug)]] 0.5 µM 0.175× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change |
| [[A-427 (line)]] | wt | 20.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.234× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change |
| [[BT-474 (line)]] | alt | 9.12 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.24× (z +8.9) | — |
| [[C-33 A (line)]] | alt | 44.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.179× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 36.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0510× (z -18.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change |
| [[COLO 205 (line)]] | alt | 10.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 27.1× (z +17.0) | — |
| [[HepG2_C3A (line)]] | wt | 27.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.74× (z +10.2) | — |
| [[NCI-H1573 (line)]] | alt | 13.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +8.9) | — |
| [[NCI-H2347 (line)]] | alt | 18.5 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 9.68× (z +8.8) | — |
| [[SW 900 (line)]] | alt | 23.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +9.5) | — |
| [[SW48 (line)]] | wt | 9.47 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.2× (z +10.2) | — |
| [[SW480 (line)]] | alt | 15.5 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 8.42× (z +9.0) | — |
| [[AsPC-1 (line)]] | alt | 7.71 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 48.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.53 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.41 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 6.66 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.38 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 59.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.28 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14284), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CAVIN4]] | +0.86 | +0.82 / +0.84 | both halves | 7e-06 | ⚠ same locus (0.4 kb, same strand: neighbours can correlate without regulation) |
| [[MSANTD3-TMEFF1]] | +0.80 | +0.83 / +0.73 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[MSANTD3]] | +0.67 | +0.72 / +0.52 | both halves | 1e-05 | STRING 693; ⚠ same locus (21.4 kb, same strand: neighbours can correlate without regulation) |
| [[AMPD3]] | +0.64 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[GRK4]] | +0.60 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[PIK3IP1-DT]] | +0.59 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[ZNF382]] | +0.59 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[ZNF267]] | +0.59 | +0.56 / +0.46 | both halves | 2e-05 |  |
| [[SLC4A10]] | +0.59 | +0.63 / +0.31 | both halves | 2e-04 |  |
| [[SYT16]] | +0.58 | +0.47 / +0.48 | both halves | 2e-05 |  |
| [[ALOXE3]] | +0.58 | +0.54 / +0.40 | both halves | 4e-05 |  |
| [[IL34]] | +0.57 | +0.51 / +0.40 | both halves | 5e-05 |  |
| [[SLC22A1]] | +0.57 | +0.49 / +0.43 | both halves | 3e-05 |  |
| [[NUP210L]] | +0.57 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[AFF3]] | +0.57 | +0.55 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MPPE1]] | -0.50 | -0.40 / -0.46 | both halves | 5e-05 |  |
| [[C1GALT1C1]] | -0.50 | -0.59 / -0.22 | both halves | 6e-04 |  |
| [[CDC42SE2]] | -0.50 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[SMARCD2]] | -0.49 | -0.48 / -0.29 | both halves | 3e-04 |  |
| [[EEF1AKMT2]] | -0.49 | -0.43 / -0.37 | both halves | 9e-05 |  |
| [[SPIDR]] | -0.49 | -0.41 / -0.39 | both halves | 5e-05 |  |
| [[TMEM242]] | -0.49 | -0.48 / -0.29 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AFF3]] | B | AFF3 activity raises TMEFF1's level | lines that do not express AFF3 (22) vs lines expressing it (28) | 2.53× lower at baseline in the lines without AFF3 | 0.007 | ⚠ within organs, on part of the lines; also absent: PTX3, DCLK2, SRPX |
| [[TRAF1]] | B | TRAF1 activity raises TMEFF1's level | lines that do not express TRAF1 (12) vs lines expressing it (38) | 2.45× lower at baseline in the lines without TRAF1 | 0.015 | ⚠ within organs, on part of the lines; also absent: MT2A, TUBA1A, ENSG00000230479; maybe low, not absent |
| [[KCNMA1]] | B | KCNMA1 activity raises TMEFF1's level | lines that do not express KCNMA1 (26) vs lines expressing it (24) | 2.24× lower at baseline in the lines without KCNMA1 | 0.028 | ⚠ within organs, on part of the lines; also absent: F2RL2, SIRLNT, SRGN |
| [[ZNF382]] | B | ZNF382 activity raises TMEFF1's level | lines that do not express ZNF382 (18) vs lines expressing it (32) | 2.45× lower at baseline in the lines without ZNF382 | 0.065 | ⚠ within organs, on part of the lines; also absent: AFF3, DZIP1, MMP16 |
| [[KCNMA1]] | B | KCNMA1 activity strengthens TMEFF1's drug response | lines that do not express KCNMA1 (21) vs lines expressing it (22) | the lines without KCNMA1 respond 0.69× as strongly (z diff +1.49); strongest at TAK-901 5 µM: 6.63x vs 13x (z diff +3.0) | 0.076 | ⚠ within organs, on part of the lines; also absent: F2RL2, SIRLNT, SRGN; target measured in part of the lines; artifact flags |
| [[FMNL3]] | B | FMNL3 activity raises TMEFF1's level | lines that do not express FMNL3 (8) vs lines expressing it (42) | 2.63× lower at baseline in the lines without FMNL3 | 0.095 | ⚠ within organs, on part of the lines; also absent: STARD9, CERCAM, ASAP3 |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GPR156]] | B | TMEFF1 activity raises GPR156's level | lines that do not express TMEFF1 (5) vs lines expressing it (45) | 2.46× lower at baseline in the lines without TMEFF1 | 0.093 | ⚠ within organs, on part of the lines; also absent: DNAJC18, HECTD2, TBKBP1; maybe low, not absent |
| [[CAVIN4]] | C | TMEFF1 activity raises CAVIN4's level | lines that do not express TMEFF1 (5) vs lines expressing it (45) | 3.04× lower at baseline in the lines without TMEFF1 | 0.069 | ⚠ within organs, on part of the lines; also absent: DNAJC18, HECTD2, TBKBP1; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 181]]; 22 genes; every member is in the + arm (projection on the module's main direction 0.588). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (30.9, -4.0); signed map (24.8, 8.2). **Vector** length 108, 27.5% of its response variance represented; |z| ≥ 3 in 1,039 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +10.0 | +11.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +9.5 | +24.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +6.5 | +3.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | +6.2 | +20.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.9 | +10.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.8 | +0.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.0 | +1.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.6 | +8.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.5 | +4.6 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.7 | -1.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.2 | -2.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.1 | -0.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.0 | -2.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.9 | -13.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.3 | -3.9 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.2 | -1.9 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.2 | -3.4 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -2.0 | -1.8 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.9 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein with EGF like and two follistatin like domains 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q31.1 — chr9:100,473,149-100,577,636 (+) |
| Ensembl biotype | protein_coding |
| Also known as | H7365, CT120.1; previously C9orf2 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IYR6](https://www.uniprot.org/uniprotkb/Q8IYR6) (Tomoregulin-1):

> Neuron-specific restriction factor that prevents herpes simplex virus 1 (HHV-1) infection in the brain by blocking viral entry. Also able to restrict herpes simplex virus 2 (HHV-2) infection, although to a lesser extent. Acts by preventing the association between the viral glycoprotein D (gD) and its cell surface receptor NECTIN1, thereby inhibiting fusion of the virus and the cell membrane. Also able to prevent the association between the viral glycoprotein B (gB) and MYH9/NMMHC-IIA and …

**Summary**, from NCBI Gene [8577](https://www.ncbi.nlm.nih.gov/gene/8577):

> Enables receptor ligand inhibitor activity. Involved in host-mediated suppression of symbiont invasion. Is active in plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:11866](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11866) · Entrez [8577](https://www.ncbi.nlm.nih.gov/gene/8577) · UniProt [Q8IYR6](https://www.uniprot.org/uniprotkb/Q8IYR6) · Ensembl [ENSG00000241697](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000241697)

## Data

Gene col 14284: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14284); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14284, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14284]; `tensor/DDL_lfc|DDL_z.npy` [14284]; `embed/gene_vectors.npy` [14284]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14284 or target_col == 14284). Every well: [[TMEFF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEFF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
