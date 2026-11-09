---
symbol: "ATP2B1"
type: "gene"
col: 972
ensembl_id: "ENSG00000070961"
name: "ATPase plasma membrane Ca2+ transporting 1"
location: "12q21.33"
module: 81
arm: "+"
pooled_cpm: 299.32
n_lines_expressing: 49
n_dd_up: 12
n_dd_down: 12
n_dd_up_clean: 9
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 23
direction_downstream: 0
tags: ["gene", "module/081"]
generated_by: "tahoemap"
---

# ATP2B1

*ATPase plasma membrane Ca2+ transporting 1* — 12q21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.43× (z +16.0, q 0e+00, up in 36 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (6 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 0.630× (z -14.0, q 1e-41, down in 36 of 46 measured lines) ⚠ toxic. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.819× (z -8.9, q 2e-16, down in 25 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SERPINE2]] (+0.59, fdr 1e-05), [[SMOX]] (+0.56, fdr 1e-05), [[TCIM]] (+0.55, fdr 2e-05); moves opposite to [[CDC23]] (-0.54, fdr 3e-05), [[ZCCHC4]] (-0.49, fdr 1e-04), [[PHC3]] (-0.45, fdr 5e-05).
> It is in [[Module 081]], a single-armed module (KRAS signaling up).
> Probable direction (from the cell lines, not proof of direct regulation): 23 arrows point to it, the strongest [[SERPINE2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 9 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 972.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.43×** | +16.0 | 0e+00 | 36/47 (SW1417, NCI-H2347, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.71×** | +16.0 | 0e+00 | 34/48 (RPMI-7951, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.62×** | +15.1 | 0e+00 | 43/47 (SW1417, Hs 766T, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.33×** | +9.0 | 4e-17 | 28/48 (NCI-H2347, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.20×** | +8.2 | 2e-14 | 23/47 (hTERT-HPNE, A498, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.26×** | +7.4 | 2e-11 | 23/47 (RKO, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.58×** | +7.3 | 2e-11 | 27/47 (SW1417, A498, …) | rises with dose | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~14% of this change | **1.24×** | +6.5 | 5e-09 | 25/46 (LoVo, HS-578T, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~18% of this change | 1.18× | +5.3 | 8e-06 | 20/47 (LOX-IMVI, HOP62, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | 1.18× | +5.1 | 2e-05 | 23/47 (J82, HS-578T, …) | top dose only | composition shift |
| [[EX229 (drug)]] 5 µM |  | **1.34×** | +4.7 | 1e-04 | 20/47 (SW1417, A498, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.23×** | +4.6 | 2e-04 | 17/47 (SW1417, Hs 766T, …) | rises with dose | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 1.16× | +4.6 | 2e-04 | 16/47 (Hs 766T, NCI-H2030, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.32×** | +4.5 | 3e-04 | 19/47 (SW1417, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +4.4 | 4e-04 | 19/46 (NCI-H460, HOP62, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.15× | +4.3 | 6e-04 | 18/48 (LoVo, SW1417, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.14× | +4.1 | 0.002 | 16/46 (NCI-H460, NCI-H23, …) | rises with dose | low cells (technical?) |
| [[EX229 (drug)]] 0.5 µM |  | 1.18× | +3.7 | 0.005 | 10/48 (KATO III, CFPAC-1, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 0.5 µM |  | 1.11× | +3.3 | 0.024 | 7/47 (BT-474, COLO 205, …) | inconsistent across doses |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.21×** | +3.1 | 0.045 | 17/47 (LoVo, J82, …) | rises with dose | noisy plate (z scaled) |
| [[Piroxicam (drug)]] 0.05 µM |  | 1.10× | +3.1 | 0.045 | 3/47 (LOX-IMVI, LS 180, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 12 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 972.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.630×** | -14.0 | 1e-41 | 36/46 (C32, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.819×** | -8.9 | 2e-16 | 25/48 (NCI-H460, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.767×** | -8.0 | 2e-13 | 24/43 (C32, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.786×** | -7.6 | 5e-12 | 26/47 (C32, HOP62, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~15% of this change | **0.775×** | -7.5 | 5e-12 | 26/47 (C32, HOP62, …) | all doses, flat |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~10% of this change | **0.817×** | -6.3 | 2e-08 | 27/47 (BT-474, A549, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.827×** | -6.0 | 2e-07 | 22/47 (NCI-H1573, NCI-H460, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.828×** | -5.9 | 2e-07 | 22/47 (HOP62, C32, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.858× | -5.8 | 3e-07 | 20/47 (C32, BT-474, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.825×** | -5.8 | 3e-07 | 21/46 (BT-474, C32, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 0.883× | -5.5 | 2e-06 | 16/47 (AsPC-1, BT-474, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.844× | -5.3 | 5e-06 | 22/47 (NCI-H460, NCI-H1573, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.852× | -5.0 | 2e-05 | 20/48 (BT-474, C32, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~5% of this change | 0.856× | -4.9 | 4e-05 | 21/47 (C32, A498, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.863× | -4.6 | 1e-04 | 18/47 (SNU-423, SW 900, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.854× | -4.6 | 2e-04 | 19/46 (J82, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Trametinib (drug)]] 0.05 µM |  | 0.905× | -4.4 | 4e-04 | 13/47 (C32, AsPC-1, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 0.870× | -4.2 | 8e-04 | 20/47 (BT-474, C32, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.869× | -4.1 | 0.001 | 17/47 (C32, BT-474, …) | all doses, flat |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | 0.873× | -4.0 | 0.001 | 12/47 (AsPC-1, C32, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 972. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 606 | 1 | 31 (7 ⚠) | [[TAK-901 (drug)]] 5 µM 8.38× (z +12.5) | [[Vinblastine (sulfate) (drug)]] 5 µM 0.367× (z -16.5) |
| [[C32 (line)]] | wt | 492 | 1 | 15 (8 ⚠) | [[TAK-901 (drug)]] 5 µM 6.57× (z +13.3) | [[Dinaciclib (drug)]] 5 µM 0.310× (z -15.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.474× (z -14.6) |
| [[hTERT-HPNE (line)]] | wt | 576 | 4 (2 ⚠) | 11 (8 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.18× (z +25.1) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 8.16× (z +13.3) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.330× (z -13.2) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.511× (z -11.8) |
| [[NCI-H460 (line)]] | wt | 901 | 2 (1 ⚠) | 10 (8 ⚠) | [[Pitavastatin (Calcium) (drug)]] 5 µM 2.46× (z +11.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Pitavastatin (Calcium) (drug)]] 0.5 µM 2.10× (z +10.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.305× (z -22.8) |
| [[HS-578T (line)]] | alt | 256 | 8 (5 ⚠) | 1 | [[Homoharringtonine (drug)]] 0.5 µM 4.03× (z +20.8) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 8.46× (z +16.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.552× (z -12.5) |
| [[AsPC-1 (line)]] | alt | 603 | 3 (2 ⚠) | 5 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 7.51× (z +15.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.521× (z -13.6) |
| [[BT-474 (line)]] | alt | 283 | 2 (1 ⚠) | 6 (3 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.47× (z +9.1) ⚠ unreliable plate only · without an alert: [[TAK-901 (drug)]] 5 µM 5.77× (z +9.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.438× (z -12.0) |
| [[A498 (line)]] | wt | 266 | 5 (5 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.64× (z +24.8) ⚠ cell-cycle shift, explains ~33% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.451× (z -10.4) ⚠ toxic |
| [[HOP62 (line)]] | alt | 486 | 2 (1 ⚠) | 5 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 12.9× (z +17.6) | [[Ixazomib citrate (drug)]] 5 µM 0.359× (z -13.7) |
| [[RPMI-7951 (line)]] | alt | 501 | 3 (2 ⚠) | 3 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 13.1× (z +18.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.534× (z -12.7) |
| [[SW 900 (line)]] | alt | 784 | 1 | 5 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 5.44× (z +9.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.317× (z -17.8) |
| [[A-172 (line)]] | wt | 102 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.33× (z +9.9) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 1.75× (z +9.3) | — |
| [[J82 (line)]] | alt | 241 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +24.2) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 7.30× (z +15.0) | — |
| [[NCI-H2347 (line)]] | alt | 203 | 4 (1 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 9.76× (z +14.8) | [[Dinaciclib (drug)]] 0.5 µM 0.511× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 148 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +15.0) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 1.88× (z +13.6) | — |
| [[LoVo (line)]] | wt | 387 | 3 (2 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 8.83× (z +17.7) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.504× (z -10.5) ⚠ toxic |
| [[RKO (line)]] | wt | 85.7 | 4 (2 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 2.28× (z +11.2) | — |
| [[SHP-77 (line)]] | alt | 339 | 0 | 4 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.468× (z -11.1) ⚠ cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 115 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.65× (z +11.6) | — |
| [[Panc 03.27 (line)]] | alt | 134 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +16.7) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 12.0× (z +16.1) | — |
| [[SNU-423 (line)]] | alt | 454 | 1 | 2 | [[TAK-901 (drug)]] 5 µM 8.82× (z +12.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.462× (z -12.2) |
| [[A549 (line)]] | wt | 447 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.281× (z -18.0) |
| [[CFPAC-1 (line)]] | alt | 172 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +20.3) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 6.98× (z +12.0) | — |
| [[Hs 766T (line)]] | wt | 185 | 2 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.87× (z +12.9) ⚠ unreliable plate only · without an alert: [[TAK-901 (drug)]] 5 µM 5.22× (z +10.3) | — |
| [[LOX-IMVI (line)]] | wt | 242 | 2 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 1.63× (z +9.4) | — |
| [[NCI-H1792 (line)]] | alt | 309 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 6.87× (z +10.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.253× (z -21.1) |
| [[NCI-H2030 (line)]] | alt | 269 | 2 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 4.46× (z +12.0) | — |
| [[A-427 (line)]] | wt | 105 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 1.68× (z +10.0) | — |
| [[COLO 205 (line)]] | alt | 84.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.31× (z +11.8) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[H4 (line)]] | wt | 171 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.58× (z +9.4) ⚠ unreliable plate only | — |
| [[HT-29 (line)]] | alt | 305 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.491× (z -9.5) ⚠ toxic |
| [[KATO III (line)]] | alt | 212 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.19× (z +12.5) ⚠ unreliable plate only | — |
| [[NCI-H23 (line)]] | alt | 251 | 1 | 0 | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 2.63× (z +9.6) | — |
| [[SK-MEL-2 (line)]] | alt | 196 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.389× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW48 (line)]] | wt | 294 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.59× (z +9.7) ⚠ unreliable plate only | — |
| [[SW480 (line)]] | alt | 97.3 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 1.63× (z +9.6) | — |
| [[AN3 CA (line)]] | alt | 88.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 221 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 302 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 148 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 234 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 445 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 62.1 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 312 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 384 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 193 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 133 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 345 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 360 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 972), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SERPINE2]] | +0.59 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[SMOX]] | +0.56 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[TCIM]] | +0.55 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[RASD1]] | +0.53 | +0.46 / +0.56 | both halves | 3e-05 |  |
| [[ELL2]] | +0.51 | +0.46 / +0.50 | both halves | 3e-05 |  |
| [[EPAS1]] | +0.51 | +0.47 / +0.49 | both halves | 2e-05 |  |
| [[FNDC3B]] | +0.51 | +0.50 / +0.42 | both halves | 4e-05 |  |
| [[MAP3K5]] | +0.50 | +0.54 / +0.45 | both halves | 3e-05 |  |
| [[PTGS2]] | +0.50 | +0.54 / +0.43 | both halves | 3e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[HEY1]] | +0.50 | +0.49 / +0.44 | both halves | 3e-05 |  |
| [[AHR]] | +0.49 | +0.43 / +0.49 | both halves | 3e-05 | pathway: HALLMARK_INFLAMMATORY_RESPONSE |
| [[GRB10]] | +0.48 | +0.43 / +0.48 | both halves | 3e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDC23]] | -0.54 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[ZCCHC4]] | -0.49 | -0.55 / -0.33 | both halves | 1e-04 |  |
| [[PHC3]] | -0.45 | -0.40 / -0.42 | both halves | 5e-05 |  |
| [[TRMT2B]] | -0.43 | -0.41 / -0.35 | both halves | 1e-04 |  |
| [[QRSL1]] | -0.43 | -0.46 / -0.33 | both halves | 1e-04 |  |
| [[ERBB2]] | -0.41 | -0.35 / -0.37 | both halves | 1e-04 | pathway: HALLMARK_UV_RESPONSE_DN |
| [[RCC1L]] | -0.41 | -0.47 / -0.31 | both halves | 2e-04 |  |
| [[SMYD5]] | -0.41 | -0.40 / -0.36 | both halves | 1e-04 |  |
| [[UNKL]] | -0.40 | -0.35 / -0.35 | both halves | 1e-04 |  |
| [[TMCO4]] | -0.40 | -0.35 / -0.34 | both halves | 1e-04 |  |
| [[MED24]] | -0.40 | -0.42 / -0.28 | both halves | 3e-04 |  |
| [[MVB12B]] | -0.39 | -0.29 / -0.41 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*23 arrows, 23 of them with an alert ⚠; grade A 0, B 23, C 0. Shown: the 12 strongest; 11 more arrows (11 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SERPINE2]] | B | SERPINE2 activity raises ATP2B1's level | lines that do not express SERPINE2 (21) vs lines expressing it (29) | 2.03× lower at baseline in the lines without SERPINE2 | 0.002 | ⚠ within organs, on part of the lines; also absent: NMRAL2P-1, ZNF365, ADAM12 |
| [[PAG1]] | B | PAG1 activity raises ATP2B1's level | lines that do not express PAG1 (15) vs lines expressing it (35) | 2.09× lower at baseline in the lines without PAG1 | 0.009 | ⚠ within organs, on part of the lines; also absent: LINC02257, PALLD, TSC22D3 |
| [[RHCG]] | B | RHCG activity raises ATP2B1's level | lines that do not express RHCG (33) vs lines expressing it (17) | 2.21× lower at baseline in the lines without RHCG | 0.009 | ⚠ within organs, on part of the lines; also absent: RSPO3, CRLF2, ANXA10 |
| [[CEMIP]] | B | CEMIP activity raises ATP2B1's level | lines that do not express CEMIP (19) vs lines expressing it (31) | 1.87× lower at baseline in the lines without CEMIP | 0.012 | ⚠ within organs, on part of the lines; also absent: PPARGC1A, DUSP4, SHC4 |
| [[DUSP4]] | B | DUSP4 activity raises ATP2B1's level | lines that do not express DUSP4 (15) vs lines expressing it (35) | 1.77× lower at baseline in the lines without DUSP4 | 0.014 | ⚠ within organs, on part of the lines; also absent: IGSF9, CEMIP, SYTL5 |
| [[PTGER4]] | B | PTGER4 activity raises ATP2B1's level | lines that do not express PTGER4 (12) vs lines expressing it (38) | 2.02× lower at baseline in the lines without PTGER4 | 0.018 | ⚠ within organs, on part of the lines; also absent: CFAP20DC, AMOTL1, GOLGA7B; maybe low, not absent |
| [[TRIB1]] | B | TRIB1 activity raises ATP2B1's level | lines that do not express TRIB1 (6) vs lines expressing it (44) | 2.19× lower at baseline in the lines without TRIB1 | 0.024 | ⚠ within organs, on part of the lines; also absent: TGFBR2, VDR, PLSCR2; maybe low, not absent |
| [[AHR]] | B | AHR activity raises ATP2B1's level | lines that do not express AHR (7) vs lines expressing it (43) | 2.37× lower at baseline in the lines without AHR | 0.028 | ⚠ within organs, on part of the lines; also absent: ENSG00000283321, VDR, GPR39 |
| [[LTBP1]] | B | LTBP1 activity raises ATP2B1's level | lines that do not express LTBP1 (15) vs lines expressing it (35) | 1.92× lower at baseline in the lines without LTBP1 | 0.029 | ⚠ within organs, on part of the lines |
| [[CD55]] | B | CD55 activity raises ATP2B1's level | lines that do not express CD55 (16) vs lines expressing it (34) | 1.47× lower at baseline in the lines without CD55 | 0.035 | ⚠ within organs, on part of the lines; also absent: IL32, IL2RG, ENSG00000271933; maybe low, not absent |
| [[DUSP4]] | B | DUSP4 activity strengthens ATP2B1's drug response | lines that do not express DUSP4 (14) vs lines expressing it (34) | the lines without DUSP4 respond 0.65× as strongly (z diff +1.22); strongest at Dinaciclib 5 µM: 1.12x vs 0.70x (z diff +5.1) | 0.047 | ⚠ within organs, on part of the lines; also absent: IGSF9, CEMIP, SYTL5; target measured in part of the lines; artifact flags |
| [[GRB10]] | B | GRB10 activity raises ATP2B1's level | lines that do not express GRB10 (11) vs lines expressing it (39) | 1.56× lower at baseline in the lines without GRB10 | 0.049 | ⚠ within organs, on part of the lines; also absent: FAM107B, DGKG, GEM |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 081]] — KRAS signaling up; 55 genes; every member is in the + arm (projection on the module's main direction 0.369). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (35.8, 9.3); signed map (8.1, 51.8). **Vector** length 142, 44.4% of its response variance represented; |z| ≥ 3 in 1,658 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +10.3 | +16.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.8 | +9.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +7.3 | +15.1 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +6.1 | +7.4 |
|  | [[EX229 (drug)]] 5 µM |  | +4.5 | +4.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +4.4 | +7.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.9 | +1.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +3.2 | +4.3 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~15% of this change | -7.3 | -7.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -6.4 | -7.6 |
|  | [[Radotinib (drug)]] 5 µM |  | -5.1 | -5.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.7 | -5.9 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -4.5 | -6.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -4.4 | -5.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -4.4 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | ATPase plasma membrane Ca2+ transporting 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q21.33 — chr12:89,588,049-89,709,366 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PMCA1 |
| Gene groups (HGNC) | ATPases Ca2+ transporting |
| Hallmark sets | INFLAMMATORY_RESPONSE, UV_RESPONSE_DN, TNFA_SIGNALING_VIA_NFKB |
| Reactome | 13 pathways, smallest: Reduction of cytosolic Ca++ levels; Platelet calcium homeostasis; Ion homeostasis |
| Matched by | ensembl_id |

**Function**, from UniProt [P20020](https://www.uniprot.org/uniprotkb/P20020) (Plasma membrane calcium-transporting ATPase 1):

> Catalyzes the hydrolysis of ATP coupled with the transport of calcium from the cytoplasm to the extracellular space thereby maintaining intracellular calcium homeostasis. Plays a role in blood pressure regulation through regulation of intracellular calcium concentration and nitric oxide production leading to regulation of vascular smooth muscle cells vasoconstriction. Positively regulates bone mineralization through absorption of calcium from the intestine. Plays dual roles in osteoclast …

**Summary**, from NCBI Gene [490](https://www.ncbi.nlm.nih.gov/gene/490):

> The protein encoded by this gene belongs to the family of P-type primary ion transport ATPases characterized by the formation of an aspartyl phosphate intermediate during the reaction cycle. These enzymes remove bivalent calcium ions from eukaryotic cells against very large concentration gradients and play a critical role in intracellular calcium homeostasis. The mammalian plasma membrane calcium ATPase isoforms are encoded by at least four separate genes and the diversity of these enzymes is …

**Accessions** — [HGNC:814](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:814) · Entrez [490](https://www.ncbi.nlm.nih.gov/gene/490) · UniProt [P20020](https://www.uniprot.org/uniprotkb/P20020) · Ensembl [ENSG00000070961](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000070961)

## Data

Gene col 972: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 972); `tables/drug_effects.parquet` (66 rows, flagged included); `relations/gene_relations.parquet` (col_a == 972, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 972]; `tensor/DDL_lfc|DDL_z.npy` [972]; `embed/gene_vectors.npy` [972]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 972 or target_col == 972). Every well: [[ATP2B1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATP2B1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
