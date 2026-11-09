---
symbol: "ZSWIM6"
type: "gene"
col: 5067
ensembl_id: "ENSG00000130449"
name: "zinc finger SWIM-type containing 6"
location: "5q12.1"
module: 171
arm: "-"
pooled_cpm: 485.29
n_lines_expressing: 49
n_dd_up: 23
n_dd_down: 11
n_dd_up_clean: 19
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/171"]
generated_by: "tahoemap"
---

# ZSWIM6

*zinc finger SWIM-type containing 6* — 5q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.98× (z +18.5, q 0e+00, up in 47 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.488× (z -12.1, q 3e-31, down in 45 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 0.705× (z -5.9, q 4e-07, down in 42 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (HCT15 0.134×, LS 180 0.271×, LOX-IMVI 0.347×, J82 0.346×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (NCI-H23 0.181×, J82 0.326×, LOX-IMVI 0.348×, A498 0.326×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 4 lines (KATO III 0.291×, HS-578T 0.337×, SNU-423 0.297×, J82 0.353×; ⚠ toxic; transcription drop); [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM in 1 line (NCI-H23 0.488×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (NCI-H1573 0.444×); [[Radotinib (drug)]] 5 µM in 1 line (AsPC-1 0.618×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARIH1]] (+0.64, fdr 7e-06), [[MYO1E]] (+0.61, fdr 1e-05), [[CSNK1A1]] (+0.60, fdr 9e-06); moves opposite to [[CDC23]] (-0.66, fdr 7e-06), [[PMS2P1]] (-0.62, fdr 1e-05), [[MORN4]] (-0.62, fdr 7e-06).
> It sits in the **-** arm of [[Module 171]] (Sealing of the nuclear envelope (NE) by ESCRT-III).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[FER1L4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5067.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.98×** | +18.5 | 0e+00 | 47/47 (SW480, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.36×** | +14.6 | 1e-45 | 47/47 (SW480, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.77×** | +13.8 | 7e-41 | 44/47 (C32, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **2.25×** | +13.7 | 8e-41 | 47/47 (SW480, A-172, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.47×** | +9.2 | 3e-18 | 46/47 (C-33 A, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.60×** | +8.0 | 1e-13 | 45/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.57×** | +7.4 | 1e-11 | 39/47 (MIA PaCa-2, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +5.7 | 9e-07 | 37/47 (MIA PaCa-2, C32, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.39×** | +5.6 | 1e-06 | 28/47 (C32, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.25×** | +5.4 | 4e-06 | 27/48 (MIA PaCa-2, LoVo, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.37×** | +5.4 | 4e-06 | 33/47 (SW480, SNU-1, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.36×** | +5.2 | 8e-06 | 33/47 (A-172, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.35×** | +5.1 | 2e-05 | 31/47 (A-172, KATO III, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.34×** | +5.0 | 2e-05 | 36/48 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.32×** | +4.8 | 7e-05 | 33/47 (HepG2/C3A, SW480, …) | two highest doses | cell-cycle shift (explains ~16% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.62×** | +4.3 | 6e-04 | 37/47 (SW480, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 9 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5067.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (HCT15 0.134×, LS 180 0.271×, LOX-IMVI 0.347×, J82 0.346×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (NCI-H23 0.181×, J82 0.326×, LOX-IMVI 0.348×, A498 0.326×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 4 lines (KATO III 0.291×, HS-578T 0.337×, SNU-423 0.297×, J82 0.353×; ⚠ toxic; transcription drop); [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM in 1 line (NCI-H23 0.488×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (NCI-H1573 0.444×); [[Radotinib (drug)]] 5 µM in 1 line (AsPC-1 0.618×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.488×** | -12.1 | 3e-31 | 45/48 (NCI-H23, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.539×** | -10.1 | 2e-21 | 38/43 (HCT15, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.535×** | -9.8 | 3e-20 | 37/44 (KATO III, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.595×** | -8.8 | 2e-16 | 44/47 (HT-29, KATO III, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.705×** | -5.9 | 4e-07 | 42/47 (KATO III, SNU-423, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | **0.807×** | -5.1 | 3e-05 | 27/47 (AsPC-1, RKO, …) | rises with dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **0.785×** | -4.1 | 0.003 | 27/47 (NCI-H1573, RKO, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.794×** | -3.7 | 0.013 | 28/46 (HepG2/C3A, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **0.804×** | -3.7 | 0.014 | 29/47 (AsPC-1, PANC-1, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 0.858× | -3.6 | 0.015 | 17/47 (AsPC-1, LoVo, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.827×** | -3.2 | 0.071 | 23/47 (RKO, C-33 A, …) | inconsistent across doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.699×** | -3.2 | 0.073 | 20/38 (Panc 03.27, NCI-H2347, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5067. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 370 | 10 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 4.17× (z +21.2) | [[Dinaciclib (drug)]] 0.5 µM 0.477× (z -11.0) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 255 | 12 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.61× (z +22.6) | — |
| [[KATO III (line)]] | alt | 444 | 6 | 4 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 3.04× (z +14.8) | [[Dinaciclib (drug)]] 0.05 µM 0.291× (z -15.3) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 373 | 6 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +18.6) | [[Dinaciclib (drug)]] 0.05 µM 0.389× (z -12.3) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 358 | 9 | 0 | [[Panobinostat (drug)]] 5 µM 4.12× (z +21.0) | — |
| [[LoVo (line)]] | wt | 644 | 6 (1 ⚠) | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 3.55× (z +18.6) | [[Dinaciclib (drug)]] 5 µM 0.416× (z -12.4) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 628 | 6 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +15.6) | [[Dinaciclib (drug)]] 0.5 µM 0.348× (z -15.6) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 469 | 5 (1 ⚠) | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +12.2) | [[Dinaciclib (drug)]] 5 µM 0.271× (z -15.3) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 364 | 6 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 4.01× (z +20.2) | [[Dinaciclib (drug)]] 0.5 µM 0.471× (z -10.9) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 591 | 5 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.49× (z +12.5) | [[Dinaciclib (drug)]] 0.5 µM 0.381× (z -13.2) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 474 | 5 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.10× (z +20.0) | [[Dinaciclib (drug)]] 0.5 µM 0.326× (z -13.9) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 449 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.31× (z +25.4) | — |
| [[hTERT-HPNE (line)]] | wt | 612 | 4 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +14.9) | [[Dinaciclib (drug)]] 0.5 µM 0.434× (z -9.7) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 399 | 6 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +14.0) | [[Dinaciclib (drug)]] 5 µM 0.393× (z -13.4) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 543 | 5 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 4.27× (z +20.7) | [[Dinaciclib (drug)]] 0.05 µM 0.337× (z -14.3) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 733 | 3 | 4 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 2.42× (z +10.8) | [[Docetaxel (drug)]] 0.05 µM 0.273× (z -16.0) ⚠ transcription drop |
| [[J82 (line)]] | alt | 549 | 3 | 4 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 2.62× (z +13.4) | [[Dinaciclib (drug)]] 0.5 µM 0.326× (z -15.7) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 177 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +13.7) | — |
| [[H4 (line)]] | wt | 508 | 5 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.10× (z +16.3) | [[Dinaciclib (drug)]] 0.5 µM 0.342× (z -12.3) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 421 | 4 (1 ⚠) | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.38× (z +14.8) | [[Dinaciclib (drug)]] 5 µM 0.134× (z -23.4) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 321 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +13.3) | — |
| [[NCI-H2030 (line)]] | alt | 408 | 5 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.50× (z +19.9) | [[Dinaciclib (drug)]] 0.05 µM 0.501× (z -8.5) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 560 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 3.44× (z +16.9) | — |
| [[Panc 03.27 (line)]] | alt | 730 | 2 | 4 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 2.59× (z +10.8) | [[Dinaciclib (drug)]] 0.05 µM 0.316× (z -12.1) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 568 | 4 (2 ⚠) | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.21× (z +10.7) | [[Selinexor (drug)]] 5 µM 0.623× (z -9.0) ⚠ cell-cycle shift, explains ~10% of this change |
| [[SNU-423 (line)]] | alt | 695 | 3 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.69× (z +11.9) | [[Dinaciclib (drug)]] 0.05 µM 0.297× (z -13.6) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 725 | 4 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.28× (z +13.4) | [[Docetaxel (drug)]] 0.05 µM 0.397× (z -10.4) ⚠ transcription drop |
| [[SW48 (line)]] | wt | 487 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 4.38× (z +16.0) | — |
| [[C-33 A (line)]] | alt | 314 | 5 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.99× (z +16.8) | — |
| [[Hs 766T (line)]] | wt | 325 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 3.32× (z +13.5) | — |
| [[NCI-H1792 (line)]] | alt | 525 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +16.2) | — |
| [[NCI-H23 (line)]] | alt | 418 | 3 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.22× (z +10.5) | [[Dinaciclib (drug)]] 0.5 µM 0.181× (z -22.7) ⚠ toxic; transcription drop · without an alert: [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM 0.488× (z -9.6) |
| [[RPMI-7951 (line)]] | alt | 426 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +14.9) | [[Dinaciclib (drug)]] 0.5 µM 0.467× (z -9.1) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 968 | 2 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.46× (z +11.3) | [[Selinexor (drug)]] 5 µM 0.585× (z -9.5) ⚠ cell-cycle shift, explains ~10% of this change · without an alert: [[Radotinib (drug)]] 5 µM 0.618× (z -8.5) |
| [[HOP62 (line)]] | alt | 275 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.53× (z +18.0) | — |
| [[NCI-H1573 (line)]] | alt | 322 | 2 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.45× (z +10.0) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.444× (z -9.2) |
| [[NCI-H2347 (line)]] | alt | 734 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.06× (z +9.4) | [[Dinaciclib (drug)]] 0.5 µM 0.445× (z -10.5) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 318 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.29× (z +14.5) | — |
| [[SW 1088 (line)]] | alt | 680 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +10.7) | [[Dinaciclib (drug)]] 0.5 µM 0.221× (z -10.5) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 636 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.29× (z +11.7) | — |
| [[HepG2_C3A (line)]] | wt | 286 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.98× (z +13.9) | — |
| [[BT-474 (line)]] | alt | 426 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.33× (z +10.0) | — |
| [[CFPAC-1 (line)]] | alt | 577 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +11.2) | — |
| [[CHP-212 (line)]] | wt | 638 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.97× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.392× (z -8.5) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 509 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.44× (z +14.5) | — |
| [[AN3 CA (line)]] | alt | 96.4 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 563 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 504 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 274 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 653 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5067), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*48 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARIH1]] | +0.64 | +0.63 / +0.59 | both halves | 7e-06 | STRING 401 |
| [[MYO1E]] | +0.61 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[CSNK1A1]] | +0.60 | +0.59 / +0.57 | both halves | 9e-06 |  |
| [[RCOR1]] | +0.60 | +0.45 / +0.59 | both halves | 3e-05 |  |
| [[SYAP1]] | +0.60 | +0.57 / +0.63 | both halves | 9e-06 |  |
| [[RAPGEF2]] | +0.60 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[TLE4]] | +0.59 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[DUSP5]] | +0.59 | +0.39 / +0.63 | both halves | 6e-05 |  |
| [[WNT2B]] | +0.58 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[MAPKAPK2]] | +0.58 | +0.45 / +0.58 | both halves | 3e-05 |  |
| [[SLC16A3]] | +0.57 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[PRKCA]] | +0.57 | +0.51 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*52 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDC23]] | -0.66 | -0.63 / -0.65 | both halves | 7e-06 |  |
| [[PMS2P1]] | -0.62 | -0.57 / -0.61 | both halves | 1e-05 |  |
| [[MORN4]] | -0.62 | -0.58 / -0.58 | both halves | 7e-06 |  |
| [[NDUFAF5]] | -0.61 | -0.54 / -0.62 | both halves | 1e-05 |  |
| [[RWDD4]] | -0.60 | -0.57 / -0.53 | both halves | 1e-05 |  |
| [[TMEM209]] | -0.59 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[COPS7B]] | -0.58 | -0.54 / -0.56 | both halves | 1e-05 |  |
| [[TIGD1]] | -0.58 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[RWDD3]] | -0.58 | -0.58 / -0.56 | both halves | 1e-05 |  |
| [[CIPC]] | -0.58 | -0.43 / -0.62 | both halves | 3e-05 |  |
| [[OTUD6B]] | -0.57 | -0.51 / -0.59 | both halves | 1e-05 |  |
| [[MED24]] | -0.57 | -0.48 / -0.62 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FER1L4]] | B | FER1L4 activity raises ZSWIM6's level | lines that do not express FER1L4 (7) vs lines expressing it (43) | 1.41× lower at baseline in the lines without FER1L4 | 0.050 | ⚠ within organs, on part of the lines; also absent: TNFRSF10A, STEAP2, OSR2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 171]] — Sealing of the nuclear envelope (NE) by ESCRT-III; 24 genes; this gene is in the **-** arm (projection on the module's main direction -0.574). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.41).
- **Nodal map** (x, y) = (-15.2, 27.8); signed map (2.3, 25.8). **Vector** length 132, 54.2% of its response variance represented; |z| ≥ 3 in 1,573 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.6 | +9.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.5 | +5.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.4 | +5.0 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +4.1 | +4.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +4.0 | +2.6 |
|  | [[(S)-Crizotinib (drug)]] 0.5 µM |  | +3.3 | +0.9 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | -11.1 | -5.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -10.2 | -3.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | -9.3 | -5.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -7.7 | -9.8 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | -7.6 | -4.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -6.2 | -3.6 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -5.9 | -3.7 |
|  | [[venetoclax (drug)]] 5 µM |  | -5.3 | -2.9 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | -4.6 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger SWIM-type containing 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q12.1 — chr5:61,332,258-61,546,172 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1577 |
| Gene groups (HGNC) | Zinc fingers SWIM-type |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HCJ5](https://www.uniprot.org/uniprotkb/Q9HCJ5) (Zinc finger SWIM domain-containing protein 6):

> involved in nervous system development, important for striatal morphology and motor regulation.

**Summary**, from NCBI Gene [57688](https://www.ncbi.nlm.nih.gov/gene/57688):

> The protein encoded by this gene contains a zinc finger SWI2/SNF2 and MuDR (SWIM) domain. Proteins with SWIM domains have been found in a diverse number of species and are predicted to interact with DNA or proteins. Mutations in this gene result in acromelic frontonasal dysostosis. [provided by RefSeq, Apr 2017]

**Accessions** — [HGNC:29316](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29316) · Entrez [57688](https://www.ncbi.nlm.nih.gov/gene/57688) · UniProt [Q9HCJ5](https://www.uniprot.org/uniprotkb/Q9HCJ5) · Ensembl [ENSG00000130449](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130449)

## Data

Gene col 5067: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5067); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5067, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5067]; `tensor/DDL_lfc|DDL_z.npy` [5067]; `embed/gene_vectors.npy` [5067]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5067 or target_col == 5067). Every well: [[ZSWIM6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZSWIM6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
