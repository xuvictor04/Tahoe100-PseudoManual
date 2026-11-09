---
symbol: "TM4SF1"
type: "gene"
col: 9872
ensembl_id: "ENSG00000169908"
name: "transmembrane 4 L six family member 1"
location: "3q25.1"
module: 81
arm: "+"
pooled_cpm: 381.38
n_lines_expressing: 38
n_dd_up: 10
n_dd_down: 63
n_dd_up_clean: 8
n_dd_down_clean: 49
in_vector_space: true
direction_upstream: 4
direction_downstream: 4
tags: ["gene", "module/081"]
generated_by: "tahoemap"
---

# TM4SF1

*transmembrane 4 L six family member 1* — 3q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 1.15× (z +5.9, q 3e-06, up in 12 of 38 measured lines) ⚠ position not correctable. The strongest without an alert is [[vincristine (drug)]] 0.5 µM: 1.73× (z +4.9, q 3e-04, up in 31 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 63 drug-doses (14 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.212× (z -27.1, q 0e+00, down in 34 of 36 measured lines) ⚠ position correction uncertain. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 0.222× (z -18.6, q 0e+00, down in 36 of 36 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC4A7]] (+0.66, fdr 7e-06), [[LRRC8C]] (+0.65, fdr 1e-05), [[BCL2A1]] (+0.64, fdr 8e-06); moves opposite to [[UBE2E1]] (-0.50, fdr 1e-04), [[ALG12]] (-0.48, fdr 3e-05).
> It is in [[Module 081]], a single-armed module (KRAS signaling up).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[BCL2A1]] → it (grade B ⚠); 4 go from it, the strongest it → [[UBASH3B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9872.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.15× | +5.9 | 3e-06 | 12/38 (SW 900, CFPAC-1, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.73×** | +4.9 | 3e-04 | 31/36 (A-427, NCI-H2030, …) | all doses, flat | low cells (technical?); noisy plate (z scaled) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.46×** | +4.7 | 5e-04 | 24/36 (AsPC-1, A-427, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.43×** | +4.5 | 0.001 | 21/36 (A549, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~24% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.41×** | +4.2 | 0.003 | 21/36 (A549, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~22% here); position effect removed |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only; position correction uncertain | **1.40×** | +4.1 | 0.003 | 27/35 (A-427, SW 900, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.39×** | +3.9 | 0.008 | 22/35 (SW 900, LoVo, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.33×** | +3.5 | 0.032 | 21/35 (A-427, AsPC-1, …) | all doses, stronger at high dose |  |
| [[vincristine (drug)]] 5 µM |  | **1.96×** | +3.3 | 0.060 | 23/34 (A-427, NCI-H2030, …) | all doses, flat | noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.43×** | +3.2 | 0.087 | 20/36 (NCI-H1792, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[vincristine (drug)]] 0.05 µM |  | **1.30×** | +3.1 | 0.093 | 20/36 (A-427, SK-MEL-2, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 64 in all, 14 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 63 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9872.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ position correction uncertain | **0.212×** | -27.1 | 0e+00 | 34/36 (HepG2/C3A, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.222×** | -18.6 | 0e+00 | 36/36 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.239×** | -17.7 | 0e+00 | 36/36 (Panc 03.27, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.438×** | -14.4 | 6e-45 | 33/37 (A549, NCI-H460, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.338×** | -13.4 | 1e-38 | 35/36 (HepG2/C3A, COLO 205, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ position correction uncertain | **0.434×** | -10.3 | 7e-23 | 30/36 (RKO, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.426×** | -10.1 | 4e-22 | 31/36 (HepG2/C3A, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **0.496×** | -8.6 | 4e-16 | 34/36 (NCI-H23, PANC-1, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.526×** | -7.6 | 2e-12 | 32/36 (MIA PaCa-2, C32, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.576×** | -6.8 | 6e-10 | 28/36 (NCI-H2347, NCI-H460, …) | all doses, flat |  |
| [[Auranofin (drug)]] 5 µM |  | **0.588×** | -6.5 | 3e-09 | 25/36 (HS-578T, NCI-H23, …) | top dose only |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.604×** | -6.2 | 3e-08 | 28/35 (MIA PaCa-2, RKO, …) | all doses, stronger at high dose |  |
| [[Budesonide (drug)]] 5 µM |  | **0.615×** | -6.0 | 9e-08 | 28/36 (HS-578T, HOP62, …) | all doses, stronger at high dose | position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **0.606×** | -5.9 | 1e-07 | 26/35 (SK-MEL-2, RKO, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.598×** | -5.9 | 2e-07 | 28/36 (MIA PaCa-2, NCI-H23, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.637×** | -5.6 | 9e-07 | 24/37 (MIA PaCa-2, NCI-H23, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.725×** | -5.5 | 1e-06 | 26/36 (MIA PaCa-2, SK-MEL-2, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.724×** | -5.4 | 1e-06 | 27/37 (MIA PaCa-2, C32, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.635×** | -5.4 | 2e-06 | 22/36 (MIA PaCa-2, C32, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.51 per unit of S-phase module lfc, +0.68 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9872. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 1,049 | 1 (1 ⚠) | 25 (8 ⚠) | [[Digitoxin (drug)]] 5 µM 2.44× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | [[Homoharringtonine (drug)]] 5 µM 0.117× (z -29.1) ⚠ position correction uncertain · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.198× (z -22.0) |
| [[C32 (line)]] | wt | 326 | 0 | 22 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -20.2) ⚠ position correction uncertain · without an alert: [[Panobinostat (drug)]] 5 µM 0.155× (z -16.5) |
| [[NCI-H23 (line)]] | alt | 443 | 0 | 22 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0937× (z -26.2) ⚠ position correction uncertain · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.181× (z -18.8) |
| [[HS-578T (line)]] | alt | 613 | 0 | 19 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.154× (z -18.8) ⚠ position correction uncertain · without an alert: [[Panobinostat (drug)]] 5 µM 0.133× (z -14.3) |
| [[RKO (line)]] | wt | 278 | 0 | 19 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.175× (z -18.8) ⚠ position correction uncertain · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.303× (z -12.9) |
| [[NCI-H460 (line)]] | wt | 762 | 6 (4 ⚠) | 11 (7 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.35× (z +12.7) ⚠ cell-cycle shift, explains ~86% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 2.67× (z +10.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.189× (z -24.6) |
| [[SK-MEL-2 (line)]] | alt | 417 | 0 | 13 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.127× (z -27.8) ⚠ position correction uncertain · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.197× (z -15.4) |
| [[A549 (line)]] | wt | 721 | 5 (3 ⚠) | 5 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 3.60× (z +13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 3.28× (z +12.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.181× (z -25.6) |
| [[HOP62 (line)]] | alt | 509 | 0 | 10 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.108× (z -23.5) ⚠ position correction uncertain · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.342× (z -11.3) |
| [[PANC-1 (line)]] | alt | 721 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.129× (z -24.3) ⚠ position correction uncertain · without an alert: [[Panobinostat (drug)]] 5 µM 0.0599× (z -23.5) |
| [[HepG2_C3A (line)]] | wt | 594 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0520× (z -37.7) ⚠ position correction uncertain · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.0649× (z -24.7) |
| [[AsPC-1 (line)]] | alt | 518 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.154× (z -23.0) ⚠ position correction uncertain · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.135× (z -17.4) |
| [[LOX-IMVI (line)]] | wt | 378 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -22.2) ⚠ position correction uncertain · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.174× (z -16.3) |
| [[NCI-H2347 (line)]] | alt | 598 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -27.0) ⚠ position correction uncertain · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.174× (z -17.5) |
| [[SW 900 (line)]] | alt | 233 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -24.0) ⚠ position correction uncertain · without an alert: [[Panobinostat (drug)]] 5 µM 0.201× (z -14.3) |
| [[SW480 (line)]] | alt | 157 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.282× (z -19.7) ⚠ position correction uncertain · without an alert: [[Belinostat (drug)]] 5 µM 0.210× (z -17.2) |
| [[hTERT-HPNE (line)]] | wt | 715 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.160× (z -17.6) ⚠ position correction uncertain · without an alert: [[Panobinostat (drug)]] 5 µM 0.122× (z -14.3) |
| [[KATO III (line)]] | alt | 408 | 1 | 5 (2 ⚠) | [[Digitoxin (drug)]] 0.5 µM 2.66× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.129× (z -25.5) ⚠ position correction uncertain · without an alert: [[Panobinostat (drug)]] 5 µM 0.0907× (z -21.1) |
| [[A498 (line)]] | wt | 182 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -14.0) ⚠ position correction uncertain · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.403× (z -10.7) |
| [[CFPAC-1 (line)]] | alt | 584 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -19.2) ⚠ position correction uncertain · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.144× (z -18.3) |
| [[COLO 205 (line)]] | alt | 318 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.136× (z -22.1) ⚠ position correction uncertain · without an alert: [[Belinostat (drug)]] 5 µM 0.0809× (z -19.7) |
| [[NCI-H1792 (line)]] | alt | 306 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.227× (z -14.4) |
| [[A-172 (line)]] | wt | 257 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -13.7) ⚠ position correction uncertain · without an alert: [[Panobinostat (drug)]] 5 µM 0.249× (z -10.0) |
| [[Hs 766T (line)]] | wt | 274 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.163× (z -17.8) |
| [[HT-29 (line)]] | alt | 253 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.198× (z -14.3) |
| [[Panc 03.27 (line)]] | alt | 533 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0864× (z -25.4) |
| [[LS 180 (line)]] | wt | 110 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.222× (z -9.9) |
| [[NCI-H2030 (line)]] | alt | 1,060 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0826× (z -29.1) ⚠ position correction uncertain · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.273× (z -15.2) |
| [[SNU-1 (line)]] | wt | 327 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.329× (z -11.8) ⚠ position correction uncertain · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.401× (z -9.7) |
| [[SW1417 (line)]] | alt | 139 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.319× (z -11.0) |
| [[LoVo (line)]] | wt | 139 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.280× (z -10.7) |
| [[SNU-423 (line)]] | alt | 149 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.214× (z -16.6) ⚠ position correction uncertain · without an alert: [[Panobinostat (drug)]] 5 µM 0.319× (z -8.7) |
| [[SW 1088 (line)]] | alt | 327 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -12.0) ⚠ position correction uncertain |
| [[SW 1271 (line)]] | alt | 387 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.118× (z -14.8) ⚠ position correction uncertain · without an alert: [[Panobinostat (drug)]] 5 µM 0.121× (z -10.3) |
| [[A-427 (line)]] | wt | 268 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.461× (z -8.9) ⚠ position correction uncertain |
| [[H4 (line)]] | wt | 151 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -11.3) ⚠ position correction uncertain |
| [[NCI-H2122 (line)]] | alt | 484 | 0 | 1 | — | [[Betamethasone dipropionate (drug)]] 5 µM 0.0454× (z -8.9) |
| [[AN3 CA (line)]] | alt | 61.9 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 88.7 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 39.3 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 56.9 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 50.2 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 88.4 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 59.8 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 94.6 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 302 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 45.5 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 51.2 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 66.0 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 64.4 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9872), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC4A7]] | +0.66 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[LRRC8C]] | +0.65 | +0.56 / +0.68 | both halves | 1e-05 |  |
| [[BCL2A1]] | +0.64 | +0.58 / +0.66 | both halves | 8e-06 |  |
| [[TMEM158]] | +0.64 | +0.68 / +0.60 | both halves | 7e-06 |  |
| [[MMP1]] | +0.64 | +0.68 / +0.58 | both halves | 7e-06 |  |
| [[STC1]] | +0.64 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[TFPI2]] | +0.63 | +0.58 / +0.57 | both halves | 9e-06 |  |
| [[EXT1]] | +0.62 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[CORO2B]] | +0.61 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[ITGA2]] | +0.61 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[FAM107B]] | +0.60 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[AADACP1]] | +0.60 | +0.58 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBE2E1]] | -0.50 | -0.36 / -0.41 | both halves | 1e-04 |  |
| [[ALG12]] | -0.48 | -0.44 / -0.48 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BCL2A1]] | B | BCL2A1 activity raises TM4SF1's level | lines that do not express BCL2A1 (26) vs lines expressing it (24) | 2.36× lower at baseline in the lines without BCL2A1 | 0.035 | ⚠ within organs, on part of the lines; also absent: BASP1-AS1, TMEM156, CSGALNACT1 |
| [[CD44]] | B | CD44 activity raises TM4SF1's level | lines that do not express CD44 (15) vs lines expressing it (35) | 2.40× lower at baseline in the lines without CD44 | 0.041 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: GBP3, CLEC2B, ADAMTS16 |
| [[MAP2K1]] | B | MAP2K1 activity raises TM4SF1's level | compounds that target MAP2K1: 4 of 4 lower it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 10.6% of all compounds | 0.066 | ⚠ off-target possible; 4 compounds |
| [[TM4SF1-AS1]] | C | TM4SF1-AS1 activity raises TM4SF1's level | lines that do not express TM4SF1-AS1 (14) vs lines expressing it (36) | 3.43× lower at baseline in the lines without TM4SF1-AS1 | 0.024 | ⚠ within organs, on part of the lines; also absent: CXCL1, MBP, TM4SF1; co-absent with the target |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[UBASH3B]] | B | TM4SF1 activity raises UBASH3B's level | lines that do not express TM4SF1 (12) vs lines expressing it (38) | 2.49× lower at baseline in the lines without TM4SF1 | 0.038 | ⚠ within organs, on part of the lines; also absent: TM4SF1-AS1; maybe low, not absent |
| [[ADAM19]] | B | TM4SF1 activity raises ADAM19's level | lines that do not express TM4SF1 (12) vs lines expressing it (38) | 2.83× lower at baseline in the lines without TM4SF1 | 0.048 | ⚠ within organs, on part of the lines; also absent: TM4SF1-AS1; maybe low, not absent |
| [[WWTR1]] | B | TM4SF1 activity raises WWTR1's level | lines that do not express TM4SF1 (12) vs lines expressing it (38) | 1.79× lower at baseline in the lines without TM4SF1 | 0.083 | ⚠ within organs, on part of the lines; also absent: TM4SF1-AS1; maybe low, not absent |
| [[STX1A]] | B | TM4SF1 activity raises STX1A's level | lines that do not express TM4SF1 (12) vs lines expressing it (38) | 2.08× lower at baseline in the lines without TM4SF1 | 0.096 | ⚠ within organs, on part of the lines; also absent: TM4SF1-AS1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 081]] — KRAS signaling up; 55 genes; every member is in the + arm (projection on the module's main direction 0.708). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (47.2, 3.8); signed map (3.6, 47.5). **Vector** length 130, 47.0% of its response variance represented; |z| ≥ 3 in 1,795 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.8 | +1.6 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +5.8 | +4.7 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only; position correction uncertain | +5.5 | +4.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | +5.1 | +3.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.9 | -1.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.2 | +2.2 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +4.0 | +3.5 |
| fall | [[venetoclax (drug)]] 5 µM |  | -5.8 | -4.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | -5.6 | -8.6 |
|  | [[Budesonide (drug)]] 5 µM |  | -5.2 | -6.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -5.0 | -4.3 |
|  | [[Clobetasol propionate (drug)]] 5 µM | ⚠ position correction uncertain | -4.9 | -5.4 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane 4 L six family member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q25.1 — chr3:149,369,022-149,377,692 (-) |
| Ensembl biotype | protein_coding |
| Also known as | L6; previously M3S1 |
| Gene groups (HGNC) | Transmembrane 4 L six family |
| Hallmark sets | P53_PATHWAY |
| Matched by | ensembl_id |

UniProt [P30408](https://www.uniprot.org/uniprotkb/P30408) carries no function annotation.

**Summary**, from NCBI Gene [4071](https://www.ncbi.nlm.nih.gov/gene/4071):

> The protein encoded by this gene is a member of the transmembrane 4 superfamily, also known as the tetraspanin family. Most of these members are cell-surface proteins that are characterized by the presence of four hydrophobic domains. The proteins mediate signal transduction events that play a role in the regulation of cell development, activation, growth and motility. This encoded protein is a cell surface antigen and is highly expressed in different carcinomas. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:11853](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11853) · Entrez [4071](https://www.ncbi.nlm.nih.gov/gene/4071) · UniProt [P30408](https://www.uniprot.org/uniprotkb/P30408) · Ensembl [ENSG00000169908](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169908)

## Data

Gene col 9872: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9872); `tables/drug_effects.parquet` (75 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9872, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9872]; `tensor/DDL_lfc|DDL_z.npy` [9872]; `embed/gene_vectors.npy` [9872]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9872 or target_col == 9872). Every well: [[TM4SF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TM4SF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
