---
symbol: "SORBS2"
type: "gene"
col: 7816
ensembl_id: "ENSG00000154556"
name: "sorbin and SH3 domain containing 2"
location: "4q35.1"
module: 34
arm: "+"
pooled_cpm: 63.1
n_lines_expressing: 33
n_dd_up: 36
n_dd_down: 37
n_dd_up_clean: 35
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 8
direction_downstream: 13
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# SORBS2

*sorbin and SH3 domain containing 2* — 4q35.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 36 drug-doses (1 with an alert ⚠); the strongest is [[Trametinib (drug)]] 5 µM: 1.66× (z +7.8, q 3e-12, up in 22 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 37 drug-doses (21 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.370× (z -15.0, q 0e+00, down in 27 of 31 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.416× (z -13.2, q 2e-37, down in 19 of 31 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMTC1]] (+0.57, fdr 1e-05), [[ZNF608]] (+0.55, fdr 1e-05), [[TNS3]] (+0.55, fdr 2e-05); moves opposite to [[CELSR1]] (-0.57, fdr 1e-05), [[GDPGP1]] (-0.55, fdr 1e-05), [[CSNK1E]] (-0.54, fdr 1e-05).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[PRUNE2]] → it (grade B ⚠); 13 go from it, the strongest it → [[MIR4713HG]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 1 with an alert ⚠; shown: the 15 strongest. 36 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7816.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM |  | **1.66×** | +7.8 | 3e-12 | 22/33 (C32, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.51×** | +7.4 | 6e-11 | 24/31 (C32, HEC-1-A, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.62×** | +7.3 | 8e-11 | 21/30 (NCI-H1792, SNU-423, …) | all doses, flat |  |
| [[Budesonide (drug)]] 0.5 µM |  | **1.57×** | +6.8 | 1e-09 | 16/31 (NCI-H1792, HOP62, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.59×** | +6.7 | 2e-09 | 19/30 (C32, H4, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.81×** | +6.7 | 2e-09 | 22/30 (NCI-H1792, SNU-423, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.52×** | +6.4 | 1e-08 | 20/32 (C32, HEC-1-A, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.54×** | +6.3 | 2e-08 | 20/30 (C32, SW480, …) | all doses, stronger at high dose |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **1.49×** | +5.6 | 1e-06 | 16/30 (NCI-H1792, HOP62, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.44×** | +5.5 | 3e-06 | 18/31 (KATO III, CFPAC-1, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.43×** | +5.4 | 4e-06 | 20/30 (C32, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.42×** | +5.3 | 5e-06 | 14/30 (NCI-H1792, HOP62, …) | all doses, flat |  |
| [[Tofacitinib (drug)]] 5 µM |  | **1.28×** | +5.2 | 1e-05 | 12/32 (CFPAC-1, Panc 03.27, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.40×** | +5.1 | 1e-05 | 20/32 (C32, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.38×** | +4.9 | 4e-05 | 11/30 (NCI-H1792, Hs 766T, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 21 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 37 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 21 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7816.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.370×** | -15.0 | 0e+00 | 27/31 (SW480, LS 180, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.384×** | -14.4 | 1e-44 | 25/31 (SW480, A-172, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.416×** | -13.2 | 2e-37 | 19/31 (NCI-H460, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.549×** | -12.8 | 3e-35 | 23/32 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.484×** | -10.9 | 9e-26 | 25/31 (SW480, A-172, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.541×** | -9.2 | 2e-18 | 19/31 (SW480, KATO III, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **0.579×** | -8.2 | 2e-14 | 22/30 (SW480, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.611×** | -7.4 | 9e-12 | 21/31 (SW480, HCT15, …) | two highest doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.608×** | -7.2 | 4e-11 | 20/30 (SW480, SNU-423, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.628×** | -7.0 | 1e-10 | 18/31 (SW480, KATO III, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.723×** | -6.9 | 2e-10 | 19/31 (NCI-H460, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.417×** | -6.9 | 3e-10 | 18/32 (NCI-H460, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.637×** | -6.8 | 5e-10 | 21/31 (SW480, Panc 03.27, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.695×** | -5.5 | 2e-06 | 18/31 (SW480, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.516×** | -5.2 | 7e-06 | 17/31 (A-172, LS 180, …) | rises with dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.702×** | -5.0 | 2e-05 | 18/31 (SW480, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.539×** | -4.9 | 4e-05 | 13/31 (KATO III, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.812×** | -4.4 | 2e-04 | 14/31 (COLO 205, HepG2/C3A, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.752×** | -4.3 | 5e-04 | 17/31 (SW480, SNU-423, …) | two highest doses | cell-cycle shift (explains ~18% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.783×** | -3.7 | 0.005 | 11/30 (SW480, HEC-1-A, …) | top dose only |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.782×** | -3.6 | 0.008 | 11/30 (SHP-77, Panc 03.27, …) | top dose only |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.791×** | -3.4 | 0.013 | 10/31 (SHP-77, Hs 766T, …) | rises with dose |  |
| [[Auranofin (drug)]] 0.5 µM |  | **0.801×** | -3.4 | 0.015 | 13/31 (SW 1088, HT-29, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.673×** | -3.1 | 0.030 | 9/31 (NCI-H460, SW480, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.52 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7816. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 62.9 | 18 | 3 (2 ⚠) | [[Clobetasol propionate (drug)]] 0.5 µM 8.90× (z +13.8) | [[Harringtonine (drug)]] 5 µM 0.105× (z -13.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.360× (z -9.1) |
| [[SW480 (line)]] | alt | 156 | 0 | 21 (14 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.239× (z -21.3) |
| [[C32 (line)]] | wt | 89.3 | 12 (2 ⚠) | 3 (3 ⚠) | [[Harringtonine (drug)]] 0.5 µM 4.89× (z +11.9) ⚠ cell-cycle shift, explains ~20% of this change · without an alert: [[Binimetinib (drug)]] 5 µM 3.94× (z +10.9) | [[Panobinostat (drug)]] 5 µM 0.218× (z -11.5) ⚠ cell-cycle shift, explains ~35% of this change |
| [[SNU-423 (line)]] | alt | 74.3 | 9 | 6 (5 ⚠) | [[Clobetasol propionate (drug)]] 0.5 µM 3.91× (z +10.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.274× (z -14.6) |
| [[KATO III (line)]] | alt | 75.5 | 2 | 12 (9 ⚠) | [[Ponatinib (drug)]] 5 µM 3.42× (z +11.4) | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -17.4) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.341× (z -14.2) |
| [[Panc 03.27 (line)]] | alt | 146 | 0 | 12 (9 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.199× (z -18.4) |
| [[NCI-H460 (line)]] | wt | 259 | 0 | 11 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.108× (z -21.5) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.143× (z -18.7) |
| [[A-172 (line)]] | wt | 185 | 2 (1 ⚠) | 8 (7 ⚠) | [[Pitavastatin (Calcium) (drug)]] 5 µM 5.79× (z +10.9) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Pitavastatin (Calcium) (drug)]] 0.5 µM 4.82× (z +10.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.137× (z -18.0) |
| [[HOP62 (line)]] | alt | 19.7 | 10 | 0 | [[Budesonide (drug)]] 5 µM 9.68× (z +11.0) | — |
| [[HS-578T (line)]] | alt | 133 | 4 | 4 (3 ⚠) | [[Budesonide (drug)]] 0.5 µM 6.38× (z +9.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.217× (z -11.5) |
| [[LS 180 (line)]] | wt | 166 | 0 | 7 (7 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.279× (z -14.2) ⚠ cell-cycle shift, explains ~29% of this change |
| [[MIA PaCa-2 (line)]] | alt | 40.5 | 6 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 17.6× (z +22.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 27.1× (z +18.6) | — |
| [[CFPAC-1 (line)]] | alt | 78.6 | 1 | 3 (1 ⚠) | [[Ponatinib (drug)]] 5 µM 3.16× (z +9.0) | [[Homoharringtonine (drug)]] 5 µM 0.322× (z -12.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.239× (z -11.4) |
| [[COLO 205 (line)]] | alt | 109 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.346× (z -12.6) |
| [[HepG2_C3A (line)]] | wt | 58.0 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -14.5) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.139× (z -12.1) |
| [[SHP-77 (line)]] | alt | 64.0 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.294× (z -10.4) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.343× (z -9.1) |
| [[SW1417 (line)]] | alt | 66.6 | 0 | 4 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.260× (z -10.1) ⚠ cell-cycle shift, explains ~54% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.433× (z -8.9) |
| [[H4 (line)]] | wt | 28.7 | 2 (1 ⚠) | 1 (1 ⚠) | [[Pitavastatin (Calcium) (drug)]] 5 µM 31.6× (z +11.9) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Pitavastatin (Calcium) (drug)]] 0.5 µM 20.9× (z +10.8) | [[Homoharringtonine (drug)]] 5 µM 0.0942× (z -12.0) ⚠ cell-cycle shift, explains ~28% of this change |
| [[HCT15 (line)]] | alt | 31.1 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.142× (z -8.9) |
| [[HEC-1-A (line)]] | alt | 123 | 0 | 3 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.328× (z -11.3) |
| [[SNU-1 (line)]] | wt | 75.2 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.137× (z -9.9) ⚠ cell-cycle shift, explains ~35% of this change |
| [[Hs 766T (line)]] | wt | 37.7 | 2 | 0 | [[Triamcinolone (drug)]] 5 µM 3.23× (z +9.6) | — |
| [[hTERT-HPNE (line)]] | wt | 120 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -11.9) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.189× (z -10.9) |
| [[LoVo (line)]] | wt | 21.3 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.65× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | [[Digitoxin (drug)]] 0.5 µM 0.308× (z -8.9) ⚠ cell-cycle shift, explains ~26% of this change |
| [[HT-29 (line)]] | alt | 24.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.196× (z -10.0) ⚠ cell-cycle shift, explains ~26% of this change |
| [[NCI-H661 (line)]] | alt | 287 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.283× (z -8.9) |
| [[A-427 (line)]] | wt | 5.10 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 6.35 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 5.44 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 12.9 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 7.50 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.90 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 12.1 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 8.06 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 9.54 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 7.19 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 6.25 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 73.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.53 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 7.17 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 81.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.80 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 6.85 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 14.8 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.05 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 42.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 19.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7816), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*53 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMTC1]] | +0.57 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[ZNF608]] | +0.55 | +0.54 / +0.49 | both halves | 1e-05 | same gene group |
| [[TNS3]] | +0.55 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[ATOH8]] | +0.54 | +0.36 / +0.51 | both halves | 1e-04 |  |
| [[PKHD1]] | +0.51 | +0.53 / +0.43 | both halves | 3e-05 |  |
| [[LINC01170]] | +0.51 | +0.52 / +0.42 | both halves | 4e-05 |  |
| [[PHYHIPL]] | +0.51 | +0.44 / +0.43 | both halves | 3e-05 |  |
| [[LINC00299]] | +0.51 | +0.56 / +0.40 | both halves | 5e-05 |  |
| [[LINC01814]] | +0.49 | +0.54 / +0.40 | both halves | 4e-05 |  |
| [[ARID5B]] | +0.49 | +0.52 / +0.39 | both halves | 5e-05 |  |
| [[RDX]] | +0.49 | +0.49 / +0.46 | both halves | 2e-05 |  |
| [[EPS8]] | +0.48 | +0.47 / +0.43 | both halves | 3e-05 | same gene group |

## Genes that move opposite

*47 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CELSR1]] | -0.57 | -0.58 / -0.54 | both halves | 1e-05 |  |
| [[GDPGP1]] | -0.55 | -0.49 / -0.59 | both halves | 1e-05 |  |
| [[CSNK1E]] | -0.54 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[KCNC4]] | -0.52 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[WNT7B]] | -0.51 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[LUCAT1]] | -0.51 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[CIB1]] | -0.51 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[UBA6]] | -0.50 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[COL13A1]] | -0.50 | -0.46 / -0.49 | both halves | 2e-05 |  |
| [[ITGA3]] | -0.50 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[EHD4]] | -0.49 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[LOXL2]] | -0.49 | -0.46 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 7, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRUNE2]] | B | PRUNE2 activity raises SORBS2's level | lines that do not express PRUNE2 (30) vs lines expressing it (20) | 2.03× lower at baseline in the lines without PRUNE2 | 0.025 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGF13, SSX1, UTY |
| [[LRRTM4]] | B | LRRTM4 activity raises SORBS2's level | lines that do not express LRRTM4 (33) vs lines expressing it (17) | 2.69× lower at baseline in the lines without LRRTM4 | 0.034 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000227088, ENSG00000249174, ENSG00000248973 |
| [[MIR4713HG]] | B | MIR4713HG activity raises SORBS2's level | lines that do not express MIR4713HG (30) vs lines expressing it (20) | 2.24× lower at baseline in the lines without MIR4713HG | 0.062 | ⚠ within organs, on part of the lines; also absent: GLDN, C4BPB, IL20RA |
| [[NR3C1]] | B | NR3C1 activity raises SORBS2's level | compounds that target NR3C1: 3 of 3 raise it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 5.0% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds |
| [[TOP2A]] | B | TOP2A activity raises SORBS2's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.3% of all compounds | 0.065 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ZNF608]] | B | ZNF608 activity raises SORBS2's level | lines that do not express ZNF608 (12) vs lines expressing it (38) | 2.96× lower at baseline in the lines without ZNF608 | 0.069 | ⚠ within organs, on part of the lines; also absent: LINC01170, GDF15 |
| [[TMEM255B]] | B | TMEM255B activity raises SORBS2's level | lines that do not express TMEM255B (19) vs lines expressing it (31) | 1.64× lower at baseline in the lines without TMEM255B | 0.077 | ⚠ within organs, on part of the lines; also absent: DOCK10, ENSG00000289600, OR4F15; maybe low, not absent |
| [[LINC00299]] | C | LINC00299 activity raises SORBS2's level | lines that do not express LINC00299 (27) vs lines expressing it (23) | 3.07× lower at baseline in the lines without LINC00299 | 0.092 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LINC01814, TNNT2, ATP2C2; co-absent with the target |

### Downstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 10, C 3. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MIR4713HG]] | B | SORBS2 activity raises MIR4713HG's level | lines that do not express SORBS2 (17) vs lines expressing it (33) | 3.93× lower at baseline in the lines without SORBS2 | 0.013 | ⚠ within organs, on part of the lines; also absent: LINC00299, ENSG00000228033, HR |
| [[ZNF608]] | B | SORBS2 activity raises ZNF608's level | lines that do not express SORBS2 (17) vs lines expressing it (33) | 2.12× lower at baseline in the lines without SORBS2 | 0.021 | ⚠ within organs, on part of the lines; also absent: LINC00299, ENSG00000228033, HR |
| [[TMTC1]] | B | SORBS2 activity raises TMTC1's level | lines that do not express SORBS2 (17) vs lines expressing it (33) | 1.60× lower at baseline in the lines without SORBS2 | 0.022 | ⚠ within organs, on part of the lines; also absent: LINC00299, ENSG00000228033, HR |
| [[LINC01170]] | B | SORBS2 activity raises LINC01170's level | lines that do not express SORBS2 (17) vs lines expressing it (33) | 1.75× lower at baseline in the lines without SORBS2 | 0.025 | ⚠ within organs, on part of the lines; also absent: LINC00299, ENSG00000228033, HR |
| [[MAP2K6]] | B | SORBS2 activity raises MAP2K6's level | lines that do not express SORBS2 (17) vs lines expressing it (33) | 1.75× lower at baseline in the lines without SORBS2 | 0.029 | ⚠ within organs, on part of the lines; also absent: LINC00299, ENSG00000228033, HR |
| [[TRIM9]] | B | SORBS2 activity weakens TRIM9's drug response | lines that do not express SORBS2 (14) vs lines expressing it (18) | the lines without SORBS2 respond 1.26× as strongly (z diff -1.63); strongest at Digitoxin 5 µM: 0.26x vs 0.41x (z diff -3.6) | 0.045 | ⚠ within organs, on part of the lines; also absent: LINC00299, ENSG00000228033, HR; target measured in part of the lines; artifact flags |
| [[PRUNE2]] | B | SORBS2 activity raises PRUNE2's level | lines that do not express SORBS2 (17) vs lines expressing it (33) | 1.53× lower at baseline in the lines without SORBS2 | 0.052 | ⚠ within organs, on part of the lines; also absent: LINC00299, ENSG00000228033, HR |
| [[PLXDC2]] | B | SORBS2 activity raises PLXDC2's level | lines that do not express SORBS2 (17) vs lines expressing it (33) | 1.45× lower at baseline in the lines without SORBS2 | 0.052 | ⚠ within organs, on part of the lines; also absent: LINC00299, ENSG00000228033, HR |
| [[LNX1]] | B | SORBS2 activity raises LNX1's level | lines that do not express SORBS2 (17) vs lines expressing it (33) | 3.12× lower at baseline in the lines without SORBS2 | 0.054 | ⚠ within organs, on part of the lines; also absent: LINC00299, ENSG00000228033, HR |
| [[MYRIP]] | B | SORBS2 activity raises MYRIP's level | lines that do not express SORBS2 (17) vs lines expressing it (33) | 1.65× lower at baseline in the lines without SORBS2 | 0.081 | ⚠ within organs, on part of the lines; also absent: LINC00299, ENSG00000228033, HR |
| [[GLDN]] | C | SORBS2 activity raises GLDN's level | lines that do not express SORBS2 (17) vs lines expressing it (33) | 2.84× lower at baseline in the lines without SORBS2 | 0.009 | ⚠ within organs, on part of the lines; also absent: LINC00299, ENSG00000228033, HR; co-absent with the target |
| [[LINC01814]] | C | SORBS2 activity raises LINC01814's level | lines that do not express SORBS2 (17) vs lines expressing it (33) | 2.90× lower at baseline in the lines without SORBS2 | 0.082 | ⚠ within organs, on part of the lines; also absent: LINC00299, ENSG00000228033, HR; co-absent with the target |

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction -0.381). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (45.1, -1.5); signed map (50.2, 13.5). **Vector** length 109, 29.8% of its response variance represented; |z| ≥ 3 in 1,344 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.9 | +0.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +5.6 | -6.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~61% of this change | +5.1 | -4.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.9 | -0.3 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +4.9 | +6.7 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +4.5 | +3.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +4.2 | +7.4 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +3.8 | +5.3 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +3.7 | +6.8 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -2.5 | -15.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | -2.3 | -10.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.2 | -3.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -1.9 | -14.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | -1.4 |
|  | [[Ivermectin (drug)]] 5 µM |  | -1.7 | -1.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.7 | -2.2 |
|  | [[Hexylresorcinol (drug)]] 5 µM |  | -1.7 | -1.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.6 | -0.0 |

## What is on record

|  |  |
|---|---|
| Name | sorbin and SH3 domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q35.1 — chr4:185,585,444-185,956,652 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ARGBP2, KIAA0777 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; SH3 domain containing |
| Hallmark sets | MITOTIC_SPINDLE |
| Matched by | ensembl_id |

**Function**, from UniProt [O94875](https://www.uniprot.org/uniprotkb/O94875) (Sorbin and SH3 domain-containing protein 2):

> Adapter protein that plays a role in the assembling of signaling complexes, being a link between ABL kinases and actin cytoskeleton. Can form complex with ABL1 and CBL, thus promoting ubiquitination and degradation of ABL1. May play a role in the regulation of pancreatic cell adhesion, possibly by acting on WASF1 phosphorylation, enhancing phosphorylation by ABL1, as well as dephosphorylation by PTPN12. Isoform 6 increases water and sodium absorption in the intestine and gall-bladder.

**Summary**, from NCBI Gene [8470](https://www.ncbi.nlm.nih.gov/gene/8470):

> Arg and c-Abl represent the mammalian members of the Abelson family of non-receptor protein-tyrosine kinases. They interact with the Arg/Abl binding proteins via the SH3 domains present in the carboxy end of the latter group of proteins. This gene encodes the sorbin and SH3 domain containing 2 protein. It has three C-terminal SH3 domains and an N-terminal sorbin homology (SoHo) domain that interacts with lipid raft proteins. The subcellular localization of this protein in epithelial and cardiac …

**Accessions** — [HGNC:24098](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24098) · Entrez [8470](https://www.ncbi.nlm.nih.gov/gene/8470) · UniProt [O94875](https://www.uniprot.org/uniprotkb/O94875) · Ensembl [ENSG00000154556](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000154556)

## Data

Gene col 7816: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7816); `tables/drug_effects.parquet` (76 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7816, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7816]; `tensor/DDL_lfc|DDL_z.npy` [7816]; `embed/gene_vectors.npy` [7816]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7816 or target_col == 7816). Every well: [[SORBS2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SORBS2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
