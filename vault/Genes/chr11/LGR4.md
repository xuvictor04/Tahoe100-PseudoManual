---
symbol: "LGR4"
type: "gene"
col: 12958
ensembl_id: "ENSG00000205213"
name: "leucine rich repeat containing G protein-coupled receptor 4"
location: "11p14.1"
module: 45
arm: "+"
pooled_cpm: 104.18
n_lines_expressing: 43
n_dd_up: 22
n_dd_down: 17
n_dd_up_clean: 20
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 2
direction_downstream: 5
tags: ["gene", "module/045"]
generated_by: "tahoemap"
---

# LGR4

*leucine rich repeat containing G protein-coupled receptor 4* — 11p14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (2 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.53× (z +12.0, q 1e-30, up in 29 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.454× (z -15.2, q 0e+00, down in 33 of 36 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.671× (z -7.9, q 3e-13, down in 28 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATP8A1]] (+0.60, fdr 7e-06), [[NOS1AP]] (+0.60, fdr 1e-05), [[RNF145]] (+0.57, fdr 2e-05); moves opposite to [[BRD9]] (-0.56, fdr 2e-05), [[FAM83G]] (-0.55, fdr 1e-05), [[ZNF621]] (-0.52, fdr 3e-05).
> It sits in the **+** arm of [[Module 045]] (Iron uptake and transport).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[IL1RL1]] → it (grade B ⚠); 5 go from it, the strongest it → [[ZNF621]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12958.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.53×** | +12.0 | 1e-30 | 29/41 (HS-578T, SW480, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.62×** | +9.3 | 4e-18 | 27/40 (LoVo, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.57×** | +9.0 | 3e-17 | 27/41 (SW1417, SW480, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.50×** | +8.2 | 5e-14 | 21/41 (SW1417, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.49×** | +8.0 | 1e-13 | 24/41 (SW1417, SW480, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.41×** | +6.9 | 5e-10 | 24/42 (NCI-H2347, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.39×** | +6.6 | 3e-09 | 22/41 (HepG2/C3A, C32, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.83×** | +6.3 | 2e-08 | 24/42 (SW1417, COLO 205, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | **1.21×** | +5.5 | 2e-06 | 20/41 (PANC-1, AsPC-1, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.33×** | +5.5 | 2e-06 | 22/40 (NCI-H460, AsPC-1, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.31×** | +5.4 | 4e-06 | 21/41 (SW1417, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[NG25 (drug)]] 5 µM |  | **1.60×** | +4.9 | 5e-05 | 21/41 (HepG2/C3A, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.28×** | +4.7 | 1e-04 | 19/41 (NCI-H2347, LS 180, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.25×** | +4.5 | 2e-04 | 16/40 (LS 180, LoVo, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.25×** | +4.4 | 4e-04 | 16/41 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.24×** | +4.3 | 6e-04 | 10/41 (PANC-1, NCI-H2030, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.49×** | +4.2 | 0.001 | 20/41 (C32, SW48, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 11 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12958.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.454×** | -15.2 | 0e+00 | 33/36 (LS 180, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.469×** | -15.1 | 0e+00 | 32/41 (LS 180, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.624×** | -8.7 | 7e-16 | 29/37 (C32, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.671×** | -7.9 | 3e-13 | 28/41 (PANC-1, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.689×** | -7.4 | 1e-11 | 28/41 (A498, NCI-H460, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.698×** | -7.2 | 7e-11 | 24/41 (NCI-H1573, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.724×** | -6.4 | 1e-08 | 26/41 (LS 180, HT-29, …) | all doses, flat | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.750×** | -5.5 | 2e-06 | 24/40 (NCI-H2347, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.774×** | -5.1 | 2e-05 | 21/41 (SW 900, NCI-H460, …) | top dose only |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.627×** | -4.9 | 6e-05 | 20/41 (NCI-H2347, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.812×** | -4.1 | 0.002 | 21/41 (NCI-H460, Panc 03.27, …) | all doses, flat |  |
| [[Docetaxel (drug)]] 5 µM |  | 0.865× | -4.1 | 0.002 | 14/41 (NCI-H2347, NCI-H1792, …) | all doses, flat |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.821×** | -3.9 | 0.004 | 15/40 (HT-29, NCI-H460, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.870× | -3.9 | 0.004 | 19/41 (Hs 766T, NCI-H1573, …) | all doses, flat | composition shift |
| [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | 0.848× | -3.3 | 0.038 | 16/42 (HT-29, KATO III, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **0.738×** | -3.2 | 0.051 | 16/41 (LoVo, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.842× | -3.2 | 0.051 | 9/40 (A498, NCI-H460, …) | all doses, flat | low cells (technical?) |
| [[vincristine (drug)]] 0.5 µM |  | **0.802×** | -3.1 | 0.052 | 14/41 (HT-29, SW 900, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.742×** | -3.1 | 0.054 | 15/41 (PANC-1, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 0.05 µM |  | 0.850× | -3.0 | 0.070 | 14/41 (HT-29, A549, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.754×** | -2.9 | 0.077 | 17/41 (SW 900, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | 0.859× | -2.9 | 0.082 | 13/41 (A498, SW 900, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12958. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 415 | 4 (4 ⚠) | 4 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.94× (z +16.0) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.194× (z -18.3) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 68.5 | 6 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.81× (z +17.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 3.12× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.278× (z -11.1) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 230 | 0 | 7 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.345× (z -12.7) ⚠ cell-cycle shift, explains ~14% of this change |
| [[NCI-H460 (line)]] | wt | 132 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.234× (z -14.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.296× (z -12.0) |
| [[AsPC-1 (line)]] | alt | 83.9 | 5 (2 ⚠) | 1 | [[Triamcinolone (drug)]] 0.5 µM 4.63× (z +12.0) | [[Harringtonine (drug)]] 0.5 µM 0.334× (z -8.6) |
| [[HEC-1-A (line)]] | alt | 138 | 4 (3 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +17.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.03× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.373× (z -11.7) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 128 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -17.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.237× (z -13.4) |
| [[SW480 (line)]] | alt | 34.7 | 6 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.58× (z +17.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 2.09× (z +10.1) | — |
| [[A498 (line)]] | wt | 136 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.295× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.402× (z -9.7) |
| [[C32 (line)]] | wt | 83.7 | 2 (1 ⚠) | 3 (3 ⚠) | [[PH-797804 (drug)]] 5 µM 7.27× (z +9.0) | [[Dinaciclib (drug)]] 0.05 µM 0.158× (z -14.8) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 263 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.227× (z -16.0) ⚠ toxic; transcription drop · without an alert: [[Vinblastine (sulfate) (drug)]] 5 µM 0.540× (z -9.8) |
| [[PANC-1 (line)]] | alt | 75.9 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.416× (z -14.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.409× (z -10.5) |
| [[SW 900 (line)]] | alt | 109 | 0 | 5 (3 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.248× (z -12.8) |
| [[Hs 766T (line)]] | wt | 257 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.247× (z -18.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.299× (z -11.0) |
| [[NCI-H2030 (line)]] | alt | 169 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.329× (z -14.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.296× (z -10.9) |
| [[NCI-H2347 (line)]] | alt | 154 | 1 | 3 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.79× (z +9.7) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.363× (z -11.5) ⚠ toxic |
| [[KATO III (line)]] | alt | 162 | 0 | 3 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.440× (z -11.7) ⚠ cell-cycle shift, explains ~14% of this change |
| [[LoVo (line)]] | wt | 174 | 2 (2 ⚠) | 1 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 3.20× (z +11.6) ⚠ toxic | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.431× (z -8.7) ⚠ unreliable plate only |
| [[BT-474 (line)]] | alt | 74.1 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +9.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 1.99× (z +8.8) | — |
| [[COLO 205 (line)]] | alt | 70.4 | 2 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 2.38× (z +9.4) | — |
| [[HS-578T (line)]] | alt | 63.6 | 1 | 1 | [[Tucidinostat (drug)]] 5 µM 2.53× (z +11.1) | [[Harringtonine (drug)]] 0.5 µM 0.362× (z -8.6) |
| [[J82 (line)]] | alt | 96.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.257× (z -11.6) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 103 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +13.4) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.362× (z -9.0) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 31.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.260× (z -9.3) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 35.8 | 0 | 1 | — | [[Naproxen (drug)]] 0.05 µM 0.154× (z -9.0) |
| [[MIA PaCa-2 (line)]] | alt | 28.3 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.63× (z +9.6) ⚠ cell-cycle shift, explains ~14% of this change | — |
| [[NCI-H1792 (line)]] | alt | 50.1 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.36× (z +9.3) | — |
| [[SHP-77 (line)]] | alt | 60.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.115× (z -15.6) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 94.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.279× (z -8.9) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 17.9 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 79.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 139 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.7 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 92.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 133 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 17.4 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 31.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 36.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 82.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 19.9 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 23.1 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 18.3 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 62.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 92.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 43.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.7 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12958), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP8A1]] | +0.60 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[NOS1AP]] | +0.60 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[RNF145]] | +0.57 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[HMGN3]] | +0.56 | +0.60 / +0.49 | both halves | 1e-05 |  |
| [[RSBN1L]] | +0.56 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[LRRC1]] | +0.56 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[TLE1]] | +0.55 | +0.49 / +0.56 | both halves | 1e-05 | pathway: Signaling by WNT |
| [[CDC42SE2]] | +0.55 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[SYBU]] | +0.54 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[LRIG3]] | +0.54 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[ACSL3]] | +0.54 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[HSF2]] | +0.54 | +0.44 / +0.49 | both halves | 3e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BRD9]] | -0.56 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[FAM83G]] | -0.55 | -0.58 / -0.50 | both halves | 1e-05 |  |
| [[ZNF621]] | -0.52 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[MYSM1]] | -0.50 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[MSS51]] | -0.49 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[DESI1]] | -0.48 | -0.39 / -0.42 | both halves | 6e-05 |  |
| [[ALG13]] | -0.48 | -0.37 / -0.48 | both halves | 8e-05 |  |
| [[GPATCH2L]] | -0.48 | -0.52 / -0.40 | both halves | 5e-05 |  |
| [[BCL2L13]] | -0.48 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[TRPV3]] | -0.47 | -0.42 / -0.36 | both halves | 9e-05 |  |
| [[KHNYN]] | -0.47 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[ZNF655]] | -0.47 | -0.40 / -0.43 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IL1RL1]] | B | IL1RL1 activity raises LGR4's level | lines that do not express IL1RL1 (32) vs lines expressing it (18) | 1.82× lower at baseline in the lines without IL1RL1 | 0.015 | ⚠ within organs, on part of the lines; also absent: FAM83A, GSDMC, IGFBP1 |
| [[ABL1]] | B | ABL1 activity lowers LGR4's level | compounds that target ABL1: 4 of 6 raise it (Flumatinib, NG25, Ponatinib, Radotinib) | 67% of the class's compounds vs 5.0% of all compounds | 0.054 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF621]] | B | LGR4 activity lowers ZNF621's level | lines that do not express LGR4 (7) vs lines expressing it (43) | 1.67× higher at baseline in the lines without LGR4 | 0.068 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[ACAD9]] | B | LGR4 activity lowers ACAD9's level | lines that do not express LGR4 (7) vs lines expressing it (43) | 1.16× higher at baseline in the lines without LGR4 | 0.077 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[STK10]] | B | LGR4 activity lowers STK10's level | lines that do not express LGR4 (7) vs lines expressing it (43) | 1.54× higher at baseline in the lines without LGR4 | 0.080 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[PTPRJ]] | B | LGR4 activity raises PTPRJ's level | lines that do not express LGR4 (7) vs lines expressing it (43) | 1.79× lower at baseline in the lines without LGR4 | 0.081 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[EPB41L4B]] | B | LGR4 activity raises EPB41L4B's level | lines that do not express LGR4 (7) vs lines expressing it (43) | 2.70× lower at baseline in the lines without LGR4 | 0.089 | ⚠ within organs, on part of the lines; maybe low, not absent |

## Where it sits

- **Module**: [[Module 045]] — Iron uptake and transport; 102 genes; this gene is in the **+** arm (projection on the module's main direction 0.579). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (8.5, 5.4); signed map (-20.5, 20.0). **Vector** length 126, 35.5% of its response variance represented; |z| ≥ 3 in 1,544 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.8 | +12.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +4.8 | +5.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.6 | +6.9 |
|  | [[NG25 (drug)]] 5 µM |  | +4.3 | +4.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.1 | +5.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.9 | +4.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.7 | +3.3 |
| fall | [[5-Azacytidine (drug)]] 5 µM |  | -7.5 | -7.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.7 | -15.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.5 | -7.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.5 | -2.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.9 | -8.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.8 | -5.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.4 | -2.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.4 | -2.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.1 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | leucine rich repeat containing G protein-coupled receptor 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p14.1 — chr11:27,365,961-27,472,790 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously GPR48 |
| Gene groups (HGNC) | G protein-coupled receptors, Class A orphans |
| Reactome | 3 pathways, smallest: Regulation of FZD by ubiquitination; TCF dependent signaling in response to WNT; Signaling by WNT |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BXB1](https://www.uniprot.org/uniprotkb/Q9BXB1) (Leucine-rich repeat-containing G protein-coupled receptor 4):

> Receptor for R-spondins that potentiates the canonical Wnt signaling pathway and is involved in the formation of various organs. Upon binding to R-spondins (RSPO1, RSPO2, RSPO3 or RSPO4), associates with phosphorylated LRP6 and frizzled receptors that are activated by extracellular Wnt receptors, triggering the canonical Wnt signaling pathway to increase expression of target genes. In contrast to classical G protein-coupled receptors, does not activate heterotrimeric G proteins to transduce the …

**Summary**, from NCBI Gene [55366](https://www.ncbi.nlm.nih.gov/gene/55366):

> The protein encoded by this gene is a G-protein coupled receptor that binds R-spondins and activates the Wnt signaling pathway. This Wnt signaling pathway activation is necessary for proper development of many organs of the body. [provided by RefSeq, Oct 2016]

**Accessions** — [HGNC:13299](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13299) · Entrez [55366](https://www.ncbi.nlm.nih.gov/gene/55366) · UniProt [Q9BXB1](https://www.uniprot.org/uniprotkb/Q9BXB1) · Ensembl [ENSG00000205213](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000205213)

## Data

Gene col 12958: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12958); `tables/drug_effects.parquet` (64 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12958, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12958]; `tensor/DDL_lfc|DDL_z.npy` [12958]; `embed/gene_vectors.npy` [12958]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12958 or target_col == 12958). Every well: [[LGR4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LGR4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
