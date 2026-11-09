---
symbol: "PVT1"
type: "gene"
col: 14644
ensembl_id: "ENSG00000249859"
name: "Pvt1 oncogene"
location: "8q24.21"
module: 4
arm: "+"
pooled_cpm: 804.8
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 13
n_dd_up_clean: 7
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# PVT1

*Pvt1 oncogene* — 8q24.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.19× (z +14.9, q 0e+00, up in 44 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.434× (z -20.5, q 0e+00, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WDR43]] (+0.71, fdr 7e-06), [[ZP3]] (+0.68, fdr 7e-06), [[SP2-AS1]] (+0.64, fdr 1e-05); moves opposite to [[FAM161B]] (-0.52, fdr 2e-05), [[GOLGA2]] (-0.52, fdr 3e-05), [[MPC2]] (-0.51, fdr 3e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[PINCR]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14644.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.19×** | +14.9 | 0e+00 | 44/49 (SNU-1, LS 180, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.59×** | +12.2 | 8e-32 | 43/48 (LS 180, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.41×** | +8.4 | 1e-14 | 32/48 (Hs 766T, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.90×** | +8.2 | 3e-14 | 34/38 (A549, SNU-1, …) | rises with dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.37×** | +7.2 | 6e-11 | 25/45 (NCI-H460, H4, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.33×** | +7.1 | 2e-10 | 30/48 (Hs 766T, Panc 03.27, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.27×** | +5.9 | 2e-07 | 28/48 (HT-29, AsPC-1, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.26×** | +5.6 | 1e-06 | 25/48 (A-172, H4, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.19× | +5.4 | 4e-06 | 22/48 (LoVo, HepG2/C3A, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.23×** | +5.2 | 1e-05 | 24/48 (Hs 766T, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | 1.20× | +4.4 | 7e-04 | 23/48 (NCI-H1573, HT-29, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +4.1 | 0.002 | 23/48 (Hs 766T, HS-578T, …) | two highest doses | composition shift |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.22×** | +4.0 | 0.003 | 25/47 (SW48, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.35×** | +3.9 | 0.005 | 25/48 (AsPC-1, HS-578T, …) | top dose only | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~34% of this change | 1.16× | +3.6 | 0.010 | 18/49 (CHP-212, PANC-1, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 0.5 µM |  | 1.13× | +3.0 | 0.089 | 8/48 (HT-29, HEC-1-A, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 5 µM |  | 1.13× | +3.0 | 0.089 | 16/47 (NCI-H1573, SK-MEL-2, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 5 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14644.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.434×** | -20.5 | 0e+00 | 42/48 (HEC-1-A, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.456×** | -19.3 | 0e+00 | 42/48 (LoVo, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.514×** | -15.7 | 0e+00 | 36/44 (NCI-H23, A549, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.618×** | -15.6 | 0e+00 | 36/49 (HEC-1-A, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.588×** | -13.0 | 8e-37 | 34/48 (LoVo, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.599×** | -12.6 | 2e-34 | 36/49 (RKO, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.743×** | -9.7 | 2e-20 | 29/48 (NCI-H2030, SW1417, …) | top dose only | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~32% of this change | **0.771×** | -6.4 | 1e-08 | 28/48 (PANC-1, SW480, …) | inconsistent across doses | low cells (technical?) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.783×** | -5.8 | 5e-07 | 24/50 (NCI-H23, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.833×** | -4.5 | 4e-04 | 22/49 (SW1417, KATO III, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.743×** | -3.8 | 0.007 | 22/48 (RKO, SW1417, …) | rises with dose | noisy plate (z scaled) |
| [[Entrectinib (drug)]] 5 µM |  | 0.859× | -3.7 | 0.009 | 18/48 (KATO III, MIA PaCa-2, …) | top dose only |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.812×** | -3.5 | 0.020 | 20/48 (HEC-1-A, LS 180, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.875× | -3.2 | 0.065 | 20/48 (MIA PaCa-2, HEC-1-A, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.830×** | -3.1 | 0.067 | 18/47 (HepG2/C3A, SHP-77, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14644. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 1,064 | 6 (2 ⚠) | 11 (5 ⚠) | [[TAK-901 (drug)]] 5 µM 5.39× (z +13.3) | [[Panobinostat (drug)]] 5 µM 0.183× (z -25.7) |
| [[LoVo (line)]] | wt | 532 | 7 (2 ⚠) | 9 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 2.14× (z +11.7) ⚠ cell-cycle shift, explains ~51% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.00× (z +11.1) | [[Panobinostat (drug)]] 5 µM 0.180× (z -26.1) |
| [[SW1417 (line)]] | alt | 479 | 0 | 14 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -22.2) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.318× (z -22.0) |
| [[C32 (line)]] | wt | 796 | 4 (2 ⚠) | 9 (5 ⚠) | [[PH-797804 (drug)]] 5 µM 7.26× (z +13.0) | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -21.2) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.307× (z -14.8) |
| [[HEC-1-A (line)]] | alt | 695 | 0 | 12 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.263× (z -29.6) |
| [[PANC-1 (line)]] | alt | 830 | 1 | 11 (7 ⚠) | [[TAK-901 (drug)]] 5 µM 2.67× (z +8.9) | [[Panobinostat (drug)]] 5 µM 0.229× (z -25.7) |
| [[NCI-H23 (line)]] | alt | 2,709 | 1 (1 ⚠) | 10 (4 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.26× (z +10.9) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.140× (z -26.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.176× (z -23.2) |
| [[NCI-H460 (line)]] | wt | 1,208 | 6 (3 ⚠) | 5 (3 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 3.81× (z +15.1) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 5.89× (z +11.3) | [[Panobinostat (drug)]] 5 µM 0.352× (z -12.7) |
| [[SW480 (line)]] | alt | 612 | 1 | 10 (5 ⚠) | [[Digitoxin (drug)]] 0.5 µM 1.81× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -21.0) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.253× (z -20.5) |
| [[A-427 (line)]] | wt | 409 | 3 (1 ⚠) | 7 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.12× (z +12.0) | [[Panobinostat (drug)]] 5 µM 0.351× (z -17.0) |
| [[Hs 766T (line)]] | wt | 404 | 8 (4 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.10× (z +13.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.56× (z +11.5) | [[Dinaciclib (drug)]] 5 µM 0.404× (z -10.6) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 358 | 9 (6 ⚠) | 1 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.14× (z +11.4) ⚠ unreliable plate only · without an alert: [[TAK-901 (drug)]] 5 µM 3.81× (z +10.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.585× (z -10.6) |
| [[MIA PaCa-2 (line)]] | alt | 1,131 | 2 (1 ⚠) | 8 (5 ⚠) | [[TAK-901 (drug)]] 5 µM 3.66× (z +8.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.284× (z -21.7) |
| [[NCI-H2030 (line)]] | alt | 658 | 0 | 10 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -24.1) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.424× (z -17.5) |
| [[A-172 (line)]] | wt | 309 | 9 (6 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 11.3× (z +13.4) | — |
| [[A498 (line)]] | wt | 1,020 | 2 (1 ⚠) | 7 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 7.19× (z +13.6) | [[Panobinostat (drug)]] 5 µM 0.247× (z -18.4) |
| [[A549 (line)]] | wt | 1,042 | 3 (1 ⚠) | 6 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.60× (z +12.6) | [[Panobinostat (drug)]] 5 µM 0.246× (z -22.2) |
| [[H4 (line)]] | wt | 473 | 6 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.05 µM 3.58× (z +14.3) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 8.20× (z +13.3) | [[Panobinostat (drug)]] 0.5 µM 0.363× (z -12.2) |
| [[HepG2_C3A (line)]] | wt | 313 | 6 (3 ⚠) | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 3.11× (z +14.9) ⚠ cell-cycle shift, explains ~51% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 2.58× (z +11.9) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.475× (z -9.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.491× (z -9.3) |
| [[LS 180 (line)]] | wt | 465 | 3 (1 ⚠) | 6 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 6.23× (z +14.8) | [[Panobinostat (drug)]] 0.5 µM 0.269× (z -20.3) |
| [[RKO (line)]] | wt | 1,877 | 2 | 7 (3 ⚠) | [[PH-797804 (drug)]] 5 µM 4.82× (z +12.8) | [[Dinaciclib (drug)]] 0.5 µM 0.139× (z -30.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.256× (z -21.2) |
| [[SK-MEL-2 (line)]] | alt | 312 | 3 (3 ⚠) | 6 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.87× (z +8.9) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.368× (z -14.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.401× (z -13.0) |
| [[SW48 (line)]] | wt | 963 | 3 | 6 (2 ⚠) | [[TAK-901 (drug)]] 0.05 µM 4.64× (z +15.7) | [[Panobinostat (drug)]] 5 µM 0.196× (z -20.5) |
| [[Panc 03.27 (line)]] | alt | 366 | 6 (3 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.20× (z +11.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.11× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.486× (z -10.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.633× (z -8.7) |
| [[SNU-1 (line)]] | wt | 1,138 | 2 | 6 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 8.08× (z +15.7) | [[Dinaciclib (drug)]] 5 µM 0.238× (z -19.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.296× (z -17.3) |
| [[C-33 A (line)]] | alt | 849 | 0 | 7 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.337× (z -18.7) |
| [[J82 (line)]] | alt | 700 | 1 | 6 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 3.53× (z +9.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.314× (z -22.1) |
| [[KATO III (line)]] | alt | 346 | 1 (1 ⚠) | 6 (3 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 2.48× (z +10.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -16.9) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.387× (z -11.6) |
| [[BT-474 (line)]] | alt | 672 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -20.8) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.391× (z -16.5) |
| [[NCI-H1792 (line)]] | alt | 7,943 | 4 (3 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 3.16× (z +13.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.10× (z +9.7) | [[Homoharringtonine (drug)]] 5 µM 0.549× (z -10.3) ⚠ cell-cycle shift, explains ~42% of this change |
| [[AsPC-1 (line)]] | alt | 228 | 4 (2 ⚠) | 1 (1 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.28× (z +12.8) ⚠ unreliable plate only · without an alert: [[Auranofin (drug)]] 5 µM 2.56× (z +10.1) | [[Homoharringtonine (drug)]] 5 µM 0.435× (z -11.9) ⚠ cell-cycle shift, explains ~42% of this change |
| [[HOP62 (line)]] | alt | 358 | 3 (1 ⚠) | 2 | [[PH-797804 (drug)]] 5 µM 4.88× (z +12.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.615× (z -9.8) |
| [[NCI-H2347 (line)]] | alt | 331 | 4 (2 ⚠) | 1 | [[PH-797804 (drug)]] 5 µM 3.96× (z +11.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.550× (z -12.5) |
| [[CHP-212 (line)]] | wt | 594 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.158× (z -18.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.189× (z -17.1) |
| [[HT-29 (line)]] | alt | 468 | 4 (3 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.42× (z +14.9) ⚠ unreliable plate only · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 2.33× (z +10.2) | — |
| [[hTERT-HPNE (line)]] | wt | 290 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.54× (z +9.6) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 5.13× (z +9.5) | — |
| [[NCI-H1573 (line)]] | alt | 227 | 3 (2 ⚠) | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 3.98× (z +13.3) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Peretinoin (drug)]] 5 µM 2.61× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -13.4) ⚠ cell-cycle shift, explains ~42% of this change |
| [[RPMI-7951 (line)]] | alt | 291 | 3 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.07× (z +9.0) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[AN3 CA (line)]] | alt | 553 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.467× (z -10.7) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.411× (z -9.6) |
| [[CFPAC-1 (line)]] | alt | 315 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.64× (z +11.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.11× (z +8.6) | — |
| [[COLO 205 (line)]] | alt | 367 | 1 (1 ⚠) | 1 (1 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.35× (z +9.9) ⚠ unreliable plate only | [[Homoharringtonine (drug)]] 5 µM 0.377× (z -14.8) ⚠ cell-cycle shift, explains ~42% of this change |
| [[HCT15 (line)]] | alt | 289 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.05 µM 3.39× (z +12.8) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.520× (z -9.6) |
| [[SHP-77 (line)]] | alt | 395 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.557× (z -9.1) |
| [[SW 900 (line)]] | alt | 334 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.438× (z -10.1) |
| [[NCI-H2122 (line)]] | alt | 460 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 600 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 473 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 204 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 216 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 268 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14644), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDR43]] | +0.71 | +0.68 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[ZP3]] | +0.68 | +0.67 / +0.67 | both halves | 7e-06 |  |
| [[SP2-AS1]] | +0.64 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[METTL8]] | +0.62 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[UCK2]] | +0.62 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[POLR1A]] | +0.62 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[PRKX]] | +0.61 | +0.57 / +0.65 | both halves | 1e-05 |  |
| [[ZNF239]] | +0.61 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[NME1]] | +0.60 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[TWNK]] | +0.59 | +0.66 / +0.51 | both halves | 1e-05 |  |
| [[WDR4]] | +0.58 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[SNHG26]] | +0.58 | +0.49 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM161B]] | -0.52 | -0.56 / -0.47 | both halves | 2e-05 |  |
| [[GOLGA2]] | -0.52 | -0.57 / -0.45 | both halves | 3e-05 |  |
| [[MPC2]] | -0.51 | -0.43 / -0.52 | both halves | 3e-05 |  |
| [[SENP2]] | -0.51 | -0.55 / -0.39 | both halves | 6e-05 |  |
| [[SNAP29]] | -0.50 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[ANKMY2]] | -0.49 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[PJA2]] | -0.49 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[SYNJ1]] | -0.49 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[MINDY2]] | -0.49 | -0.46 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PINCR]] | B | PINCR activity strengthens PVT1's drug response | lines that do not express PINCR (29) vs lines expressing it (20) | the lines without PINCR respond 0.76× as strongly (z diff +1.67); rises at some drug-doses, falls at others (38% from rises): Belinostat 5 µM: 0.70x vs 0.46x (z diff +4.2); TAK-901 5 µM: 2.48x vs 4.65x (z diff +3.0); Panobinostat 5 µM: 0.53x vs 0.32x (z diff +2.9) | 0.021 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PTCHD4, ENSG00000269729, PCK1; target measured in part of the lines; rises at some drug-doses, falls at others; artifact flags |
| [[CELF2]] | B | CELF2 activity lowers PVT1's level | lines that do not express CELF2 (24) vs lines expressing it (26) | 1.48× higher at baseline in the lines without CELF2 | 0.025 | ⚠ within organs, on part of the lines; also absent: ENPP5, LMO3, GNAT3 |
| [[LAMC3]] | B | LAMC3 activity raises PVT1's level | lines that do not express LAMC3 (25) vs lines expressing it (25) | 1.76× lower at baseline in the lines without LAMC3 | 0.063 | ⚠ within organs, on part of the lines; also absent: DLL3, ADD2, CNKSR2 |
| [[TP53]] | B | TP53 activity strengthens PVT1's drug response | recorded loss-of-function mutation of TP53 in 32 lines vs 17 not recorded | the TP53-altered lines respond 0.74× as strongly (z diff +1.56); rises at some drug-doses, falls at others (52% from rises): Belinostat 5 µM: 0.69x vs 0.45x (z diff +4.1); TAK-901 5 µM: 2.40x vs 5.51x (z diff +4.0); PH-797804 5 µM: 2.23x vs 3.83x (z diff +2.9) | 0.065 | ⚠ within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines; target measured in part of the lines; rises at some drug-doses, falls at others; artifact flags |
| [[LAMC3]] | B | LAMC3 activity strengthens PVT1's drug response | lines that do not express LAMC3 (25) vs lines expressing it (24) | the lines without LAMC3 respond 0.76× as strongly (z diff +2.24); strongest at Belinostat 5 µM: 0.70x vs 0.50x (z diff +3.8) | 0.075 | ⚠ within organs, on part of the lines; also absent: DLL3, ADD2, CNKSR2; target measured in part of the lines; artifact flags |
| [[NCS1]] | B | NCS1 activity strengthens PVT1's drug response | lines that do not express NCS1 (6) vs lines expressing it (43) | the lines without NCS1 respond 0.49× as strongly (z diff +3.26); strongest at Belinostat 5 µM: 0.98x vs 0.55x (z diff +6.0) | 0.078 | ⚠ within organs, on part of the lines; also absent: SH3BP5, ZNF618, PBK; maybe low, not absent; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.507). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-12.9, -34.6); signed map (-2.3, -49.9). **Vector** length 159, 59.6% of its response variance represented; |z| ≥ 3 in 1,910 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[PH-797804 (drug)]] 5 µM |  | +8.8 | +12.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | +8.5 | +14.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +8.2 | +5.4 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | +6.8 | +8.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.7 | +5.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +5.8 | +4.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +5.6 | +2.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.5 | +1.1 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -6.3 | -20.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -6.2 | -2.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -5.2 | -2.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | -5.1 | -19.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -5.1 | -9.7 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -4.0 | -0.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -3.1 | -4.5 |
|  | [[Retinoic acid (drug)]] 5 µM |  | -3.0 | -2.1 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -2.9 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | Pvt1 oncogene |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 8q24.21 — chr8:127,794,526-128,187,101 (+) |
| Ensembl biotype | lncRNA |
| Also known as | FFX, HNB, NCRNA00079, LINC00079, onco-lncRNA-100, MIR1204HG, TP53LC09 |
| Gene groups (HGNC) | MicroRNA non-coding host genes; Long non-coding RNAs with non-systematic symbols |
| Hallmark sets | P53_PATHWAY |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [5820](https://www.ncbi.nlm.nih.gov/gene/5820):

> This gene represents a long non-coding RNA locus that has been identified as a candidate oncogene. Increased copy number and overexpression of this gene are associated with many types of cancers including breast and ovarian cancers, acute myeloid leukemia and Hodgkin lymphoma. Allelic variants of this gene are also associated with end-stage renal disease attributed to type 1 diabetes. Consistent with its association with various types of cancer, transcription of this gene is regulated by the …

**Accessions** — [HGNC:9709](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9709) · Entrez [5820](https://www.ncbi.nlm.nih.gov/gene/5820) · Ensembl [ENSG00000249859](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000249859)

## Data

Gene col 14644: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14644); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14644, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14644]; `tensor/DDL_lfc|DDL_z.npy` [14644]; `embed/gene_vectors.npy` [14644]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14644 or target_col == 14644). Every well: [[PVT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PVT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
