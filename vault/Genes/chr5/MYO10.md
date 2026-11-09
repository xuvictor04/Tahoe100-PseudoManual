---
symbol: "MYO10"
type: "gene"
col: 7004
ensembl_id: "ENSG00000145555"
name: "myosin X"
location: "5p15.1"
module: 13
arm: "+"
pooled_cpm: 335.28
n_lines_expressing: 45
n_dd_up: 17
n_dd_down: 20
n_dd_up_clean: 12
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 16
direction_downstream: 2
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# MYO10

*myosin X* — 5p15.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (5 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.59× (z +11.6, q 2e-28, up in 35 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (3 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 0.562× (z -12.9, q 2e-35, down in 38 of 42 measured lines) ⚠ toxic. The strongest without an alert is [[Triamcinolone (drug)]] 5 µM: 0.767× (z -8.7, q 5e-16, down in 23 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CD44]] (+0.70, fdr 7e-06), [[PPFIBP1]] (+0.65, fdr 7e-06), [[SH2B3]] (+0.65, fdr 7e-06).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 16 arrows point to it, the strongest [[PRSS23]] → it (grade B ⚠); 2 go from it, the strongest it → [[ACTN1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7004.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.59×** | +11.6 | 2e-28 | 35/44 (BT-474, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.39×** | +10.9 | 2e-25 | 34/43 (A-427, SW480, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.39×** | +7.7 | 3e-12 | 30/43 (LoVo, Panc 03.27, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.38×** | +7.5 | 1e-11 | 28/43 (A-427, NCI-H2030, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.71×** | +6.6 | 6e-09 | 30/40 (Panc 03.27, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.31×** | +6.2 | 4e-08 | 26/43 (LoVo, KATO III, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.30×** | +6.1 | 8e-08 | 24/44 (A-427, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.28×** | +5.8 | 4e-07 | 25/43 (A-427, NCI-H2030, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~16% of this change | **1.28×** | +5.5 | 3e-06 | 25/42 (NCI-H460, LoVo, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.25×** | +5.3 | 7e-06 | 21/43 (NCI-H460, HT-29, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.48×** | +4.8 | 9e-05 | 24/43 (BT-474, SW1417, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.24×** | +4.7 | 1e-04 | 24/43 (LoVo, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.21×** | +4.6 | 2e-04 | 21/43 (A498, LoVo, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.22×** | +4.5 | 2e-04 | 21/43 (A498, HS-578T, …) | top dose only | cell-cycle shift (explains ~3% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.14× | +4.3 | 6e-04 | 20/43 (A498, BT-474, …) | top dose only | composition shift |
| [[PF-06260933 (drug)]] 5 µM |  | **1.39×** | +4.0 | 0.002 | 18/43 (NCI-H460, RPMI-7951, …) | top dose only | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | 1.16× | +3.3 | 0.031 | 18/43 (C32, NCI-H1792, …) | top dose only |  |
| [[BAY1125976 (drug)]] 5 µM |  | **1.30×** | +3.2 | 0.042 | 15/43 (Panc 03.27, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.21×** | +3.1 | 0.047 | 16/44 (A498, LoVo, …) | all doses, stronger at high dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 49 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7004.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.562×** | -12.9 | 2e-35 | 38/42 (COLO 205, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.647×** | -9.7 | 5e-20 | 25/39 (A549, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Triamcinolone (drug)]] 5 µM |  | **0.767×** | -8.7 | 5e-16 | 23/43 (A549, H4, …) | all doses, stronger at high dose |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.717×** | -7.7 | 2e-12 | 24/43 (A549, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.721×** | -7.6 | 3e-12 | 28/44 (LS 180, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.751×** | -6.7 | 3e-09 | 28/43 (C32, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.776×** | -5.9 | 3e-07 | 22/43 (HS-578T, A549, …) | all doses, flat |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **0.808×** | -5.0 | 5e-05 | 22/43 (A549, NCI-H460, …) | two highest doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.810×** | -4.9 | 7e-05 | 20/43 (J82, HOP62, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.836× | -4.8 | 8e-05 | 20/43 (C32, Hs 766T, …) | all doses, flat | noisy plate (z scaled) |
| [[Budesonide (drug)]] 0.05 µM |  | **0.816×** | -4.7 | 1e-04 | 23/43 (A549, HS-578T, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **0.803×** | -4.7 | 1e-04 | 22/42 (A549, HS-578T, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.863× | -4.7 | 1e-04 | 18/44 (Hs 766T, RKO, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.824×** | -4.5 | 2e-04 | 20/44 (C32, Hs 766T, …) | all doses, flat | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.823×** | -4.5 | 2e-04 | 21/43 (A549, HS-578T, …) | all doses, flat |  |
| [[Budesonide (drug)]] 0.5 µM |  | **0.824×** | -4.5 | 2e-04 | 22/43 (HS-578T, A549, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.856× | -4.4 | 4e-04 | 19/43 (C32, Hs 766T, …) | two highest doses | noisy plate (z scaled) |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **0.830×** | -4.3 | 5e-04 | 22/43 (A549, HS-578T, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7004. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 470 | 2 | 18 (5 ⚠) | [[Tofacitinib (drug)]] 5 µM 1.99× (z +12.5) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.322× (z -14.0) ⚠ toxic · without an alert: [[Vinblastine (sulfate) (drug)]] 5 µM 0.480× (z -13.3) |
| [[A549 (line)]] | wt | 545 | 1 | 11 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 7.87× (z +15.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.314× (z -23.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Triamcinolone (drug)]] 5 µM 0.604× (z -10.2) |
| [[BT-474 (line)]] | alt | 414 | 11 (7 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +21.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 18.8× (z +19.9) | [[Dinaciclib (drug)]] 5 µM 0.505× (z -8.5) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 880 | 0 | 10 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.335× (z -15.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ponatinib (drug)]] 5 µM 0.413× (z -9.1) |
| [[LOX-IMVI (line)]] | wt | 881 | 0 | 10 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -19.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.448× (z -8.6) |
| [[NCI-H460 (line)]] | wt | 358 | 6 (3 ⚠) | 4 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 9.87× (z +18.0) | [[Dinaciclib (drug)]] 5 µM 0.512× (z -9.7) ⚠ toxic; transcription drop · without an alert: [[Triamcinolone (drug)]] 5 µM 0.661× (z -8.8) |
| [[A498 (line)]] | wt | 373 | 9 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.86× (z +29.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.84× (z +15.3) | — |
| [[LoVo (line)]] | wt | 259 | 6 (2 ⚠) | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.48× (z +25.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 1.96× (z +13.3) | [[Dinaciclib (drug)]] 5 µM 0.625× (z -9.0) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 414 | 4 (1 ⚠) | 4 (4 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.60× (z +11.1) | [[Dinaciclib (drug)]] 0.5 µM 0.456× (z -12.9) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 253 | 1 | 7 (5 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.62× (z +8.6) | [[Selinexor (drug)]] 5 µM 0.515× (z -12.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Radotinib (drug)]] 5 µM 0.602× (z -9.2) |
| [[A-172 (line)]] | wt | 138 | 3 | 4 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.99× (z +10.6) | [[Trametinib (drug)]] 5 µM 0.436× (z -9.2) ⚠ cell-cycle shift, explains ~19% of this change · without an alert: [[Cobimetinib (drug)]] 5 µM 0.428× (z -8.8) |
| [[A-427 (line)]] | wt | 125 | 7 (4 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 3.18× (z +16.3) | — |
| [[HS-578T (line)]] | alt | 528 | 4 (2 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.73× (z +20.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.91× (z +14.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.444× (z -12.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Clobetasol propionate (drug)]] 0.5 µM 0.447× (z -8.8) |
| [[SW1417 (line)]] | alt | 449 | 6 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 1.81× (z +10.2) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 3.04× (z +10.0) | — |
| [[hTERT-HPNE (line)]] | wt | 1,742 | 0 | 5 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.231× (z -15.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 303 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +19.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.30× (z +11.5) | — |
| [[COLO 205 (line)]] | alt | 557 | 2 (1 ⚠) | 2 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 2.11× (z +10.5) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.326× (z -15.7) ⚠ toxic |
| [[H4 (line)]] | wt | 445 | 0 | 4 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.333× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ponatinib (drug)]] 5 µM 0.345× (z -9.0) |
| [[LS 180 (line)]] | wt | 300 | 1 (1 ⚠) | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.57× (z +10.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.375× (z -16.1) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 260 | 4 (2 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 10.8× (z +17.1) | — |
| [[SNU-423 (line)]] | alt | 331 | 3 (2 ⚠) | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.72× (z +11.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.544× (z -12.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 326 | 2 (1 ⚠) | 1 (1 ⚠) | [[Tofacitinib (drug)]] 5 µM 1.73× (z +9.5) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.406× (z -10.6) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 564 | 0 | 3 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.356× (z -10.0) ⚠ toxic · without an alert: [[Trametinib (drug)]] 0.5 µM 0.458× (z -9.4) |
| [[NCI-H1573 (line)]] | alt | 134 | 3 (2 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 14.9× (z +18.4) | — |
| [[NCI-H2030 (line)]] | alt | 95.7 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.97× (z +12.1) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[NCI-H23 (line)]] | alt | 126 | 0 | 3 (2 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.497× (z -19.8) ⚠ position not correctable · without an alert: [[Radotinib (drug)]] 5 µM 0.426× (z -9.8) |
| [[SW480 (line)]] | alt | 283 | 2 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.56× (z +12.9) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.544× (z -12.0) ⚠ toxic |
| [[HEC-1-A (line)]] | alt | 108 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 1.68× (z +9.9) | — |
| [[KATO III (line)]] | alt | 186 | 1 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 1.76× (z +9.9) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.562× (z -9.8) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 426 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.69× (z +8.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.561× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 387 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 7.41× (z +11.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.410× (z -14.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 184 | 1 (1 ⚠) | 1 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.42× (z +9.8) ⚠ toxic; cell-cycle shift, explains ~16% of this change | [[Homoharringtonine (drug)]] 5 µM 0.568× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW 900 (line)]] | alt | 246 | 0 | 2 (1 ⚠) | — | [[Trametinib (drug)]] 5 µM 0.359× (z -10.9) ⚠ cell-cycle shift, explains ~19% of this change · without an alert: [[Trametinib (drug)]] 0.5 µM 0.465× (z -9.1) |
| [[SW48 (line)]] | wt | 169 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 6.37× (z +9.6) | — |
| [[J82 (line)]] | alt | 169 | 0 | 1 | — | [[Ponatinib (drug)]] 5 µM 0.338× (z -10.2) |
| [[RPMI-7951 (line)]] | alt | 207 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.570× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 108 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 67.4 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 38.7 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 93.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 239 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 58.7 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 320 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 381 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 389 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 428 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 25.2 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 45.9 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 473 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 161 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7004), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CD44]] | +0.70 | +0.68 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[PPFIBP1]] | +0.65 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[SH2B3]] | +0.65 | +0.60 / +0.65 | both halves | 7e-06 | same gene group |
| [[MACF1]] | +0.63 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[NMNAT2]] | +0.63 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[SHANK1]] | +0.61 | +0.60 / +0.57 | both halves | 9e-06 |  |
| [[CSMD2]] | +0.61 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[HBEGF]] | +0.60 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[BCL2A1]] | +0.59 | +0.66 / +0.50 | both halves | 1e-05 |  |
| [[NES]] | +0.59 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[MEG8]] | +0.59 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[SYNJ2]] | +0.59 | +0.50 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 15, C 1. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRSS23]] | B | PRSS23 activity raises MYO10's level | lines that do not express PRSS23 (13) vs lines expressing it (37) | 2.42× lower at baseline in the lines without PRSS23 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with SETD1B; also absent: ETS1, TMSB4X, ZNF469; maybe low, not absent |
| [[WWTR1]] | B | WWTR1 activity raises MYO10's level | lines that do not express WWTR1 (7) vs lines expressing it (43) | 2.71× lower at baseline in the lines without WWTR1 | 0.014 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: ZNF585A, LGALS1, EBI3 |
| [[ADAMTS16]] | B | ADAMTS16 activity raises MYO10's level | lines that do not express ADAMTS16 (25) vs lines expressing it (25) | 2.12× lower at baseline in the lines without ADAMTS16 | 0.022 | ⚠ within organs, on part of the lines; also absent: PLAU, ADAMTS12, GBP5 |
| [[COL15A1]] | B | COL15A1 activity raises MYO10's level | lines that do not express COL15A1 (28) vs lines expressing it (22) | 1.97× lower at baseline in the lines without COL15A1 | 0.033 | ⚠ within organs, on part of the lines; also absent: LINC01583, PHACTR1, GYPC |
| [[ADAMTS12]] | B | ADAMTS12 activity raises MYO10's level | lines that do not express ADAMTS12 (33) vs lines expressing it (17) | 2.26× lower at baseline in the lines without ADAMTS12 | 0.033 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LINC01411, APBB1IP, VCAM1 |
| [[GFPT2]] | B | GFPT2 activity raises MYO10's level | lines that do not express GFPT2 (23) vs lines expressing it (27) | 1.80× lower at baseline in the lines without GFPT2 | 0.035 | ⚠ within organs, on part of the lines; also absent: PDCD1LG2, MIR100HG, AK5 |
| [[COL5A3]] | B | COL5A3 activity raises MYO10's level | lines that do not express COL5A3 (24) vs lines expressing it (26) | 1.96× lower at baseline in the lines without COL5A3 | 0.040 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ZEB2, OR4F15, HS3ST3A1 |
| [[INSYN2B]] | B | INSYN2B activity raises MYO10's level | lines that do not express INSYN2B (31) vs lines expressing it (19) | 1.94× lower at baseline in the lines without INSYN2B | 0.053 | ⚠ within organs, on part of the lines; also absent: MMP2, ITGA11, FGF5 |
| [[CD44]] | B | CD44 activity raises MYO10's level | lines that do not express CD44 (15) vs lines expressing it (35) | 2.54× lower at baseline in the lines without CD44 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: GBP3, CLEC2B, ADAMTS16 |
| [[SPOCD1]] | B | SPOCD1 activity raises MYO10's level | lines that do not express SPOCD1 (25) vs lines expressing it (25) | 2.26× lower at baseline in the lines without SPOCD1 | 0.066 | ⚠ within organs, on part of the lines; also absent: IL7R, ARMCX1, IDO1 |
| [[FRMD4A]] | B | FRMD4A activity raises MYO10's level | lines that do not express FRMD4A (24) vs lines expressing it (26) | 1.95× lower at baseline in the lines without FRMD4A | 0.070 | ⚠ within organs, on part of the lines; also absent: ENSG00000230615, PTGFR, TNFAIP6 |
| [[KCNN4]] | B | KCNN4 activity raises MYO10's level | lines that do not express KCNN4 (12) vs lines expressing it (38) | 2.41× lower at baseline in the lines without KCNN4 | 0.072 | ⚠ within organs, on part of the lines; also absent: RP1, GSPT2, GALC |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ACTN1]] | B | MYO10 activity raises ACTN1's level | lines that do not express MYO10 (5) vs lines expressing it (45) | 1.86× lower at baseline in the lines without MYO10 | 0.060 | ⚠ within organs, on part of the lines; also absent: FAM111A, RARG, DPH6-DT; its own permutation p |
| [[SLC9A7]] | B | MYO10 activity raises SLC9A7's level | lines that do not express MYO10 (5) vs lines expressing it (45) | 2.17× lower at baseline in the lines without MYO10 | 0.089 | ⚠ within organs, on part of the lines; also absent: FAM111A, RARG, DPH6-DT; its own permutation p |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.619). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (47.7, 6.4); signed map (6.0, 49.4). **Vector** length 137, 42.9% of its response variance represented; |z| ≥ 3 in 1,936 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +9.7 | +10.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +7.4 | +7.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.3 | +6.1 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +4.9 | +6.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +4.8 | +7.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.3 | +3.3 |
|  | [[Busulfan (drug)]] 0.05 µM |  | +2.8 | +2.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.6 | +4.6 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -8.5 | -12.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -6.6 | -6.7 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -6.0 | -8.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | -5.2 | -4.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.0 | -3.2 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -5.0 | -7.7 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -4.6 | -5.9 |
|  | [[Budesonide (drug)]] 5 µM |  | -4.3 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | myosin X |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5p15.1 — chr5:16,661,907-16,936,288 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0799, MyoX |
| Gene groups (HGNC) | Pleckstrin homology domain containing; Myosin heavy chains, class X; FERM domain containing |
| Reactome | 11 pathways, smallest: Netrin-1 signaling; FCGR3A-mediated phagocytosis; Leishmania phagocytosis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HD67](https://www.uniprot.org/uniprotkb/Q9HD67) (Unconventional myosin-X):

> Myosins are actin-based motor molecules with ATPase activity. Unconventional myosins serve in intracellular movements. MYO10 binds to actin filaments and actin bundles and functions as a plus end-directed motor. Moves with higher velocity and takes larger steps on actin bundles than on single actin filaments. The tail domain binds to membranous compartments containing phosphatidylinositol 3,4,5-trisphosphate or integrins, and mediates cargo transport along actin filaments. Regulates cell shape, …

**Summary**, from NCBI Gene [4651](https://www.ncbi.nlm.nih.gov/gene/4651):

> This gene encodes a member of the myosin superfamily. The protein represents an unconventional myosin; it should not be confused with the conventional non-muscle myosin-10 (MYH10). Unconventional myosins contain the basic domains of conventional myosins and are further distinguished from class members by their tail domains. This gene functions as an actin-based molecular motor and plays a role in integration of F-actin and microtubule cytoskeletons during meiosis. [provided by RefSeq, Dec 2011]

**Accessions** — [HGNC:7593](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7593) · Entrez [4651](https://www.ncbi.nlm.nih.gov/gene/4651) · UniProt [Q9HD67](https://www.uniprot.org/uniprotkb/Q9HD67) · Ensembl [ENSG00000145555](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000145555)

## Data

Gene col 7004: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7004); `tables/drug_effects.parquet` (69 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7004, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7004]; `tensor/DDL_lfc|DDL_z.npy` [7004]; `embed/gene_vectors.npy` [7004]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7004 or target_col == 7004). Every well: [[MYO10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MYO10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
