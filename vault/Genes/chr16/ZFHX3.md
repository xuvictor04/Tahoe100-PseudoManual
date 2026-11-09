---
symbol: "ZFHX3"
type: "gene"
col: 6454
ensembl_id: "ENSG00000140836"
name: "zinc finger homeobox 3"
location: "16q22.2-q22.3"
module: 217
arm: "+"
pooled_cpm: 218.49
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 25
n_dd_up_clean: 2
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/217"]
generated_by: "tahoemap"
---

# ZFHX3

*zinc finger homeobox 3* — 16q22.2-q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Harringtonine (drug)]] 5 µM: 1.41× (z +9.1, q 6e-17, up in 27 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 13 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Harringtonine (drug)]] 5 µM in 4 lines (PANC-1 3.42×, A-172 4.07×, J82 3.26×, A498 2.78×); [[Homoharringtonine (drug)]] 5 µM in 3 lines (J82 3.12×, A-172 3.09×, PANC-1 2.12×; ⚠ cell-cycle shift, explains ~21% of this change); [[Budesonide (drug)]] 0.5 µM in 1 line (Hs 766T 3.88×); [[Budesonide (drug)]] 5 µM in 1 line (Hs 766T 3.75×).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (12 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.317× (z -31.7, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RNF115]] (+0.67, fdr 7e-06), [[ZFP36L1]] (+0.63, fdr 7e-06), [[JADE1]] (+0.61, fdr 1e-05); moves opposite to [[UBA6]] (-0.59, fdr 1e-05), [[ENTPD4]] (-0.56, fdr 5e-05), [[LMAN1]] (-0.55, fdr 5e-05).
> It is in [[Module 217]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 3 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6454.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 13 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Harringtonine (drug)]] 5 µM in 4 lines (PANC-1 3.42×, A-172 4.07×, J82 3.26×, A498 2.78×); [[Homoharringtonine (drug)]] 5 µM in 3 lines (J82 3.12×, A-172 3.09×, PANC-1 2.12×; ⚠ cell-cycle shift, explains ~21% of this change); [[Budesonide (drug)]] 0.5 µM in 1 line (Hs 766T 3.88×); [[Budesonide (drug)]] 5 µM in 1 line (Hs 766T 3.75×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **1.41×** | +9.1 | 6e-17 | 27/48 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | 1.15× | +5.7 | 4e-06 | 23/48 (J82, A-172, …) | top dose only | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.20×** | +5.1 | 5e-05 | 24/48 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.18× | +4.7 | 4e-04 | 16/47 (SHP-77, HEC-1-A, …) | two highest doses | low cells (technical?) |
| [[Binimetinib (drug)]] 5 µM |  | 1.17× | +4.1 | 0.004 | 19/49 (NCI-H460, NCI-H1573, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 1.13× | +4.0 | 0.006 | 13/48 (NCI-H460, NCI-H1573, …) | all doses, flat | noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | 1.15× | +3.9 | 0.006 | 14/48 (NCI-H2030, NCI-H1573, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.15× | +3.9 | 0.006 | 18/48 (Hs 766T, HS-578T, …) | inconsistent across doses |  |
| [[Pentamidine (isethionate) (drug)]] 5 µM |  | 1.10× | +3.9 | 0.007 | 5/48 (HS-578T, NCI-H2030, …) | top dose only |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | 1.15× | +3.8 | 0.008 | 15/50 (NCI-H460, NCI-H1573, …) | all doses, flat | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | 1.15× | +3.7 | 0.009 | 14/47 (NCI-H460, SHP-77, …) | two highest doses |  |
| [[Omeprazole (drug)]] 0.05 µM |  | 1.14× | +3.7 | 0.010 | 12/48 (LOX-IMVI, SK-MEL-2, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.14× | +3.6 | 0.016 | 14/48 (A-427, C32, …) | two highest doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 1.14× | +3.5 | 0.016 | 18/48 (NCI-H460, NCI-H1573, …) | rises with dose |  |
| [[Entrectinib (drug)]] 5 µM |  | 1.13× | +3.5 | 0.021 | 9/48 (NCI-H1573, NCI-H1792, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.09× | +3.4 | 0.021 | 10/49 (NCI-H460, LoVo, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.10× | +3.4 | 0.026 | 7/48 (NCI-H460, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 0.05 µM |  | 1.12× | +3.2 | 0.040 | 8/49 (HepG2/C3A, NCI-H2347, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 44 in all, 20 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6454.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.317×** | -31.7 | 0e+00 | 47/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.317×** | -31.7 | 0e+00 | 47/48 (KATO III, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.393×** | -25.8 | 0e+00 | 45/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **0.597×** | -13.7 | 2e-40 | 35/47 (KATO III, HT-29, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.665×** | -11.2 | 3e-27 | 42/48 (NCI-H460, SNU-423, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.723×** | -8.9 | 4e-17 | 35/48 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.725×** | -8.9 | 6e-17 | 32/48 (NCI-H1573, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | **0.735×** | -7.8 | 3e-13 | 29/45 (NCI-H460, HOP62, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~89% of this change | **0.766×** | -7.1 | 1e-10 | 26/44 (HT-29, NCI-H460, …) | all doses, flat | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.766×** | -7.0 | 1e-10 | 30/48 (NCI-H23, C32, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.769×** | -7.0 | 2e-10 | 29/50 (KATO III, NCI-H460, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **0.777×** | -6.9 | 2e-10 | 28/48 (NCI-H1573, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.628×** | -6.7 | 9e-10 | 38/48 (SW480, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **0.793×** | -6.4 | 8e-09 | 29/49 (NCI-H460, HOP62, …) | all doses, flat | composition shift |
| [[Brivudine (drug)]] 5 µM |  | **0.660×** | -6.0 | 8e-08 | 31/49 (HEC-1-A, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.746×** | -5.8 | 3e-07 | 36/48 (NCI-H460, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.702×** | -5.1 | 1e-05 | 34/48 (NCI-H460, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.712×** | -4.9 | 3e-05 | 30/48 (HOP62, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.885× | -4.7 | 5e-05 | 12/48 (AN3 CA, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.726×** | -4.6 | 1e-04 | 29/48 (SW480, SNU-423, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | 0.844× | -4.4 | 2e-04 | 21/48 (SW480, MIA PaCa-2, …) | all doses, flat |  |
| [[EX229 (drug)]] 5 µM |  | **0.747×** | -4.2 | 6e-04 | 22/48 (SW480, C32, …) | all doses, flat | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 0.05 µM |  | 0.855× | -4.1 | 9e-04 | 13/48 (SNU-1, NCI-H2347, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.902× | -4.0 | 0.001 | 13/48 (HEC-1-A, NCI-H460, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.43 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6454. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 305 | 15 (2 ⚠) | 12 (9 ⚠) | [[Trametinib (drug)]] 0.05 µM 1.67× (z +12.7) | [[Panobinostat (drug)]] 5 µM 0.153× (z -33.5) |
| [[Hs 766T (line)]] | wt | 152 | 18 | 4 (1 ⚠) | [[Budesonide (drug)]] 0.5 µM 3.88× (z +16.5) | [[Panobinostat (drug)]] 5 µM 0.269× (z -16.0) |
| [[HS-578T (line)]] | alt | 167 | 12 | 3 | [[Clobetasol propionate (drug)]] 0.05 µM 3.06× (z +11.8) | [[Panobinostat (drug)]] 0.5 µM 0.223× (z -15.9) |
| [[hTERT-HPNE (line)]] | wt | 225 | 8 | 4 (1 ⚠) | [[Clobetasol propionate (drug)]] 0.5 µM 2.37× (z +10.1) | [[Panobinostat (drug)]] 0.5 µM 0.173× (z -20.5) |
| [[HEC-1-A (line)]] | alt | 420 | 2 (1 ⚠) | 9 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.62× (z +13.1) ⚠ cell-cycle shift, explains ~21% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 1.89× (z +11.7) | [[Panobinostat (drug)]] 0.5 µM 0.203× (z -30.6) |
| [[NCI-H1792 (line)]] | alt | 251 | 6 | 5 (2 ⚠) | [[Budesonide (drug)]] 0.5 µM 2.06× (z +9.6) | [[Panobinostat (drug)]] 5 µM 0.336× (z -14.5) |
| [[HOP62 (line)]] | alt | 323 | 1 (1 ⚠) | 9 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.58× (z +10.2) ⚠ cell-cycle shift, explains ~21% of this change | [[Panobinostat (drug)]] 5 µM 0.171× (z -28.2) |
| [[LOX-IMVI (line)]] | wt | 166 | 4 | 6 (3 ⚠) | [[Budesonide (drug)]] 0.5 µM 2.14× (z +9.9) | [[Panobinostat (drug)]] 5 µM 0.251× (z -17.9) |
| [[AN3 CA (line)]] | alt | 593 | 0 | 9 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.207× (z -16.1) |
| [[HT-29 (line)]] | alt | 231 | 0 | 9 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.232× (z -26.2) |
| [[NCI-H1573 (line)]] | alt | 156 | 0 | 9 (6 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.356× (z -14.5) ⚠ cell-cycle shift, explains ~23% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.372× (z -13.9) |
| [[NCI-H2030 (line)]] | alt | 424 | 0 | 9 (6 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.305× (z -14.5) |
| [[A-172 (line)]] | wt | 149 | 5 (2 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +20.2) ⚠ cell-cycle shift, explains ~21% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 4.07× (z +17.1) | [[Panobinostat (drug)]] 0.5 µM 0.371× (z -12.5) |
| [[COLO 205 (line)]] | alt | 169 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -24.1) ⚠ cell-cycle shift, explains ~21% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.297× (z -15.7) |
| [[KATO III (line)]] | alt | 320 | 1 | 7 (4 ⚠) | [[Harringtonine (drug)]] 5 µM 1.71× (z +9.8) | [[Panobinostat (drug)]] 0.5 µM 0.175× (z -32.8) |
| [[LS 180 (line)]] | wt | 218 | 2 | 6 (3 ⚠) | [[Harringtonine (drug)]] 5 µM 1.96× (z +11.1) | [[Panobinostat (drug)]] 5 µM 0.371× (z -17.1) |
| [[A498 (line)]] | wt | 174 | 4 (2 ⚠) | 3 | [[Harringtonine (drug)]] 5 µM 2.78× (z +15.7) | [[Panobinostat (drug)]] 0.5 µM 0.298× (z -19.2) |
| [[MIA PaCa-2 (line)]] | alt | 145 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.286× (z -15.9) |
| [[NCI-H23 (line)]] | alt | 139 | 0 | 6 (3 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.354× (z -12.7) ⚠ cell-cycle shift, explains ~64% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.412× (z -11.2) |
| [[SHP-77 (line)]] | alt | 339 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.213× (z -21.8) |
| [[C32 (line)]] | wt | 219 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.383× (z -17.0) ⚠ cell-cycle shift, explains ~21% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.398× (z -11.6) |
| [[H4 (line)]] | wt | 134 | 3 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +9.2) ⚠ cell-cycle shift, explains ~21% of this change · without an alert: [[Betamethasone dipropionate (drug)]] 0.5 µM 2.73× (z +8.8) | [[Panobinostat (drug)]] 0.5 µM 0.321× (z -9.9) |
| [[J82 (line)]] | alt | 174 | 2 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +23.6) ⚠ cell-cycle shift, explains ~21% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.26× (z +16.7) | [[Panobinostat (drug)]] 0.5 µM 0.387× (z -14.0) |
| [[LoVo (line)]] | wt | 167 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 2.08× (z +12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~89% of this change | [[Panobinostat (drug)]] 5 µM 0.323× (z -20.3) |
| [[NCI-H2347 (line)]] | alt | 114 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.380× (z -13.1) |
| [[SW1417 (line)]] | alt | 245 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.294× (z -22.2) |
| [[SW480 (line)]] | alt | 282 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.215× (z -33.3) |
| [[A-427 (line)]] | wt | 134 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.381× (z -14.3) |
| [[A549 (line)]] | wt | 315 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.148× (z -23.2) |
| [[AsPC-1 (line)]] | alt | 175 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.181× (z -22.5) |
| [[CFPAC-1 (line)]] | alt | 137 | 1 (1 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +13.2) ⚠ cell-cycle shift, explains ~21% of this change | [[Panobinostat (drug)]] 0.5 µM 0.482× (z -11.0) |
| [[HCT15 (line)]] | alt | 296 | 1 | 3 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 2.13× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.377× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.421× (z -10.9) |
| [[HepG2_C3A (line)]] | wt | 399 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.228× (z -17.7) |
| [[Panc 03.27 (line)]] | alt | 192 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.269× (z -23.1) |
| [[RKO (line)]] | wt | 167 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.314× (z -14.3) |
| [[SNU-423 (line)]] | alt | 211 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.237× (z -19.5) |
| [[SW 900 (line)]] | alt | 259 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.250× (z -18.8) |
| [[BT-474 (line)]] | alt | 264 | 2 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +10.3) ⚠ cell-cycle shift, explains ~21% of this change · without an alert: [[TAK-901 (drug)]] 0.05 µM 2.29× (z +9.2) | [[Panobinostat (drug)]] 0.5 µM 0.322× (z -13.1) |
| [[C-33 A (line)]] | alt | 255 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.297× (z -17.6) |
| [[CHP-212 (line)]] | wt | 243 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.229× (z -13.0) |
| [[PANC-1 (line)]] | alt | 98.3 | 2 (1 ⚠) | 1 | [[Harringtonine (drug)]] 5 µM 3.42× (z +17.6) | [[Panobinostat (drug)]] 5 µM 0.541× (z -9.1) |
| [[RPMI-7951 (line)]] | alt | 141 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.347× (z -12.3) |
| [[SK-MEL-2 (line)]] | alt | 125 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.388× (z -10.9) |
| [[SNU-1 (line)]] | wt | 91.6 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.241× (z -11.9) ⚠ cell-cycle shift, explains ~45% of this change |
| [[SW 1088 (line)]] | alt | 131 | 0 | 2 | — | [[Idoxuridine (drug)]] 0.5 µM 0.0481× (z -12.4) |
| [[SW48 (line)]] | wt | 166 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.65× (z +8.6) ⚠ cell-cycle shift, explains ~21% of this change | — |
| [[NCI-H2122 (line)]] | alt | 224 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 243 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 127 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 176 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6454), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF115]] | +0.67 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[ZFP36L1]] | +0.63 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[JADE1]] | +0.61 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[CUX1]] | +0.61 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[ZBTB4]] | +0.61 | +0.58 / +0.55 | both halves | 1e-05 | same gene group |
| [[KLF9]] | +0.61 | +0.53 / +0.64 | both halves | 1e-05 | same gene group |
| [[CEBPD]] | +0.60 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[BCL9L]] | +0.60 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[ZFAND5]] | +0.59 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[ZFP36L2]] | +0.59 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[ZBTB2]] | +0.58 | +0.60 / +0.56 | both halves | 1e-05 | same gene group |
| [[ZFX]] | +0.58 | +0.54 / +0.57 | both halves | 1e-05 | same gene group |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBA6]] | -0.59 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[ENTPD4]] | -0.56 | -0.56 / -0.40 | both halves | 5e-05 |  |
| [[LMAN1]] | -0.55 | -0.55 / -0.40 | both halves | 5e-05 |  |
| [[DCAF13]] | -0.55 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[PMPCA]] | -0.55 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[NOMO2]] | -0.55 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[COG5]] | -0.54 | -0.52 / -0.46 | both halves | 2e-05 |  |
| [[CA5B]] | -0.54 | -0.50 / -0.40 | both halves | 5e-05 |  |
| [[P3H1]] | -0.53 | -0.49 / -0.46 | both halves | 3e-05 |  |
| [[DNAJC24]] | -0.53 | -0.42 / -0.52 | both halves | 4e-05 |  |
| [[SAR1A]] | -0.53 | -0.52 / -0.40 | both halves | 5e-05 |  |
| [[KHDC4]] | -0.51 | -0.50 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 217]]; 12 genes; every member is in the + arm (projection on the module's main direction 0.678). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (26.2, 13.6); signed map (15.5, 26.4). **Vector** length 120, 37.5% of its response variance represented; |z| ≥ 3 in 1,857 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +13.1 | +9.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | +10.0 | +5.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +8.9 | +5.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +8.4 | +0.9 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +5.3 | +3.9 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +4.6 | +2.1 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +4.4 | +2.7 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +4.3 | +1.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.3 | -0.9 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.1 | -11.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | -5.0 | -13.7 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -4.3 | -5.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -4.3 | -5.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.2 | -5.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -4.2 | -6.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.1 | -4.6 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -3.2 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger homeobox 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q22.2-q22.3 — chr16:72,782,885-73,891,871 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ZNF927, FLJ26184; previously ATBF1, C16orf47 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; Zinc fingers matrin-type; ZF class homeoboxes and pseudogenes |
| Reactome | 2 pathways, smallest: RUNX3 regulates CDKN1A transcription; Transcriptional regulation by RUNX3 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15911](https://www.uniprot.org/uniprotkb/Q15911) (Zinc finger homeobox protein 3):

> Transcriptional regulator which can act as an activator or a repressor. Inhibits the enhancer element of the AFP gene by binding to its AT-rich core sequence. In concert with SMAD-dependent TGF-beta signaling can repress the transcription of AFP via its interaction with SMAD2/3. Regulates the circadian locomotor rhythms via transcriptional activation of neuropeptidergic genes which are essential for intercellular synchrony and rhythm amplitude in the suprachiasmatic nucleus (SCN) of the brain …

**Summary**, from NCBI Gene [463](https://www.ncbi.nlm.nih.gov/gene/463):

> This gene encodes a transcription factor with multiple homeodomains and zinc finger motifs, and regulates myogenic and neuronal differentiation. The encoded protein suppresses expression of the alpha-fetoprotein gene by binding to an AT-rich enhancer motif. The protein has also been shown to negatively regulate c-Myb, and transactivate the cell cycle inhibitor cyclin-dependent kinase inhibitor 1A (also known as p21CIP1). This gene is reported to function as a tumor suppressor in several …

**Accessions** — [HGNC:777](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:777) · Entrez [463](https://www.ncbi.nlm.nih.gov/gene/463) · UniProt [Q15911](https://www.uniprot.org/uniprotkb/Q15911) · Ensembl [ENSG00000140836](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000140836)

## Data

Gene col 6454: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6454); `tables/drug_effects.parquet` (66 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6454, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6454]; `tensor/DDL_lfc|DDL_z.npy` [6454]; `embed/gene_vectors.npy` [6454]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6454 or target_col == 6454). Every well: [[ZFHX3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZFHX3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
