---
symbol: "POLR1C"
type: "gene"
col: 10111
ensembl_id: "ENSG00000171453"
name: "RNA polymerase I and III subunit C"
location: "6p21.1"
module: 5
arm: "+"
pooled_cpm: 42.4
n_lines_expressing: 50
n_dd_up: 30
n_dd_down: 17
n_dd_up_clean: 18
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# POLR1C

*RNA polymerase I and III subunit C* — 6p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (12 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.89× (z +27.0, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (3 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 5 µM: 0.655× (z -7.4, q 6e-11, down in 40 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MIRLET7A1HG]] (+0.72, fdr 7e-06), [[ZNF26]] (+0.67, fdr 7e-06), [[KCNJ14]] (+0.66, fdr 7e-06); moves opposite to [[EXOC5]] (-0.71, fdr 7e-06), [[TTBK2]] (-0.57, fdr 2e-05), [[HSD17B4]] (-0.51, fdr 4e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 14 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10111.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.89×** | +27.0 | 0e+00 | 48/48 (A-172, HOP62, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.63×** | +12.4 | 1e-32 | 37/48 (LOX-IMVI, HS-578T, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.77×** | +10.4 | 3e-23 | 39/48 (NCI-H2347, A-172, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.75×** | +10.2 | 2e-22 | 36/48 (HOP62, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.69×** | +9.6 | 1e-19 | 44/48 (HT-29, NCI-H1792, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.65×** | +8.7 | 2e-16 | 34/46 (CFPAC-1, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.57×** | +8.2 | 2e-14 | 38/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.53×** | +7.8 | 5e-13 | 32/48 (LS 180, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **1.53×** | +7.7 | 8e-13 | 36/47 (NCI-H460, LS 180, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.35×** | +7.6 | 2e-12 | 29/48 (A-172, HOP62, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.22×** | +7.6 | 2e-12 | 39/49 (A-172, LS 180, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.45×** | +6.8 | 6e-10 | 35/48 (SNU-423, A-172, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.41×** | +6.3 | 2e-08 | 28/48 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **1.40×** | +5.7 | 5e-07 | 25/45 (NCI-H460, A-172, …) | inconsistent across doses | composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.25×** | +5.6 | 8e-07 | 26/48 (NCI-H2347, NCI-H460, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.78×** | +5.5 | 1e-06 | 29/48 (A-172, RKO, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.51×** | +3.9 | 0.002 | 19/48 (HS-578T, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.51×** | +3.9 | 0.003 | 19/48 (MIA PaCa-2, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.33×** | +3.7 | 0.006 | 11/48 (KATO III, NCI-H460, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **1.22×** | +3.4 | 0.015 | 13/48 (NCI-H2030, A-427, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.30×** | +3.4 | 0.015 | 13/47 (LoVo, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **1.43×** | +3.4 | 0.016 | 10/48 (HS-578T, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10111.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **0.655×** | -7.4 | 6e-11 | 40/47 (A-427, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.690×** | -6.5 | 2e-08 | 25/41 (SHP-77, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.745×** | -5.4 | 1e-05 | 23/47 (C32, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.753×** | -5.2 | 3e-05 | 28/47 (A-172, AsPC-1, …) | rises with dose | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.746×** | -5.2 | 3e-05 | 24/47 (LoVo, HOP62, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.755×** | -5.0 | 7e-05 | 25/48 (LoVo, C-33 A, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.788×** | -4.2 | 0.002 | 19/47 (A-427, LoVo, …) | all doses, flat |  |
| [[Cepharanthine (drug)]] 5 µM |  | 0.849× | -4.2 | 0.002 | 20/48 (Panc 03.27, CFPAC-1, …) | top dose only |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.840× | -4.2 | 0.002 | 15/48 (LoVo, SW480, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.819×** | -4.1 | 0.002 | 19/48 (SW480, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.825×** | -4.1 | 0.002 | 17/48 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **0.800×** | -4.1 | 0.002 | 23/48 (LoVo, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.05 µM |  | **0.807×** | -3.6 | 0.012 | 13/47 (AsPC-1, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.821×** | -3.6 | 0.012 | 17/49 (AsPC-1, LoVo, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.825×** | -3.5 | 0.016 | 18/48 (LoVo, LOX-IMVI, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.814×** | -3.5 | 0.017 | 17/48 (LoVo, MIA PaCa-2, …) | all doses, flat |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.829×** | -3.3 | 0.030 | 15/47 (NCI-H23, SNU-423, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | **0.806×** | -3.3 | 0.033 | 14/47 (NCI-H1792, SHP-77, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.37 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10111. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 29.0 | 6 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.63× (z +15.0) | — |
| [[HOP62 (line)]] | alt | 38.7 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.26× (z +19.2) | — |
| [[HS-578T (line)]] | alt | 38.4 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.21× (z +18.8) | — |
| [[LOX-IMVI (line)]] | wt | 54.6 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +13.2) | — |
| [[A-172 (line)]] | wt | 31.3 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.60× (z +20.0) | — |
| [[HT-29 (line)]] | alt | 35.6 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.12× (z +17.0) | — |
| [[KATO III (line)]] | alt | 47.4 | 2 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.66× (z +13.0) | [[Dinaciclib (drug)]] 5 µM 0.277× (z -11.7) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 34.5 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.39× (z +10.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 46.1 | 2 (1 ⚠) | 1 (1 ⚠) | [[Topotecan (hydrochloride) (drug)]] 5 µM 4.03× (z +11.6) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.25× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.261× (z -11.1) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 36.1 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.98× (z +11.8) | [[Dinaciclib (drug)]] 0.5 µM 0.141× (z -15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 41.6 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.43× (z +18.0) | [[Dinaciclib (drug)]] 5 µM 0.343× (z -8.9) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 66.4 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.149× (z -10.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.185× (z -9.4) |
| [[C-33 A (line)]] | alt | 65.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0705× (z -19.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 41.4 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.75× (z +15.7) | — |
| [[HCT15 (line)]] | alt | 61.8 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.63× (z +10.4) | — |
| [[HepG2_C3A (line)]] | wt | 36.4 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.09× (z +10.5) | — |
| [[hTERT-HPNE (line)]] | wt | 38.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +9.2) | — |
| [[J82 (line)]] | alt | 37.8 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.06× (z +13.4) | [[Dinaciclib (drug)]] 5 µM 0.221× (z -12.5) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 26.6 | 2 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 4.09× (z +10.6) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.51× (z +10.0) | — |
| [[NCI-H1792 (line)]] | alt | 29.7 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.25× (z +14.4) | — |
| [[NCI-H2347 (line)]] | alt | 37.3 | 2 | 0 | [[Selinexor (drug)]] 5 µM 3.12× (z +12.7) | — |
| [[Panc 03.27 (line)]] | alt | 61.6 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.63× (z +16.6) | [[Dinaciclib (drug)]] 5 µM 0.301× (z -10.6) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 55.0 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.28× (z +13.2) | — |
| [[SHP-77 (line)]] | alt | 45.4 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.78× (z +11.6) | [[Dinaciclib (drug)]] 5 µM 0.198× (z -12.6) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 51.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.20× (z +12.8) | — |
| [[A-427 (line)]] | wt | 39.3 | 0 | 1 | — | [[Cobimetinib (drug)]] 5 µM 0.340× (z -8.9) |
| [[A498 (line)]] | wt | 30.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.82× (z +13.2) | — |
| [[A549 (line)]] | wt | 27.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.00× (z +14.3) | — |
| [[AsPC-1 (line)]] | alt | 31.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.65× (z +12.9) | — |
| [[BT-474 (line)]] | alt | 47.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.38× (z +16.1) | — |
| [[C32 (line)]] | wt | 23.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.01× (z +11.8) | — |
| [[HEC-1-A (line)]] | alt | 54.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.79× (z +14.2) | — |
| [[Hs 766T (line)]] | wt | 26.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.12× (z +11.5) | — |
| [[PANC-1 (line)]] | alt | 47.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.85× (z +15.4) | — |
| [[SNU-1 (line)]] | wt | 51.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +8.5) | — |
| [[SW 900 (line)]] | alt | 27.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.82× (z +14.2) | — |
| [[SW1417 (line)]] | alt | 44.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.73× (z +12.2) | — |
| [[SW48 (line)]] | wt | 73.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.38× (z +8.5) | — |
| [[CHP-212 (line)]] | wt | 47.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 65.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 50.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 52.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 65.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 44.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 53.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 68.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10111), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MIRLET7A1HG]] | +0.72 | +0.65 / +0.71 | both halves | 7e-06 |  |
| [[ZNF26]] | +0.67 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[KCNJ14]] | +0.66 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[NOP16]] | +0.66 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[IDI2-AS1]] | +0.64 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[NOP2]] | +0.64 | +0.67 / +0.59 | both halves | 7e-06 | STRING 745 |
| [[FBXW9]] | +0.63 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[HCG18]] | +0.63 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[KANSL1L-AS1]] | +0.63 | +0.61 / +0.57 | both halves | 1e-05 |  |
| [[MIR17HG]] | +0.62 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[TRMT1]] | +0.61 | +0.54 / +0.59 | both halves | 1e-05 | STRING 412 |
| [[GTPBP4]] | +0.61 | +0.66 / +0.55 | both halves | 1e-05 | STRING 643 |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EXOC5]] | -0.71 | -0.63 / -0.75 | both halves | 7e-06 |  |
| [[TTBK2]] | -0.57 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[HSD17B4]] | -0.51 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[DLD]] | -0.51 | -0.34 / -0.52 | both halves | 1e-04 |  |
| [[CALCOCO2]] | -0.50 | -0.49 / -0.46 | both halves | 2e-05 |  |
| [[CAT]] | -0.50 | -0.54 / -0.36 | both halves | 1e-04 |  |
| [[GRHL1]] | -0.50 | -0.38 / -0.45 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises POLR1C's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.5% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[MEX3A]] | B | MEX3A activity raises POLR1C's level | lines that do not express MEX3A (6) vs lines expressing it (44) | 1.23× lower at baseline in the lines without MEX3A | 0.048 | ⚠ within organs, on part of the lines; also absent: SNTA1, POGLUT3, FMNL3; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers POLR1C's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.0% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.567). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-10.2, -29.2); signed map (14.8, 1.1). **Vector** length 103, 27.7% of its response variance represented; |z| ≥ 3 in 1,070 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.4 | +27.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +6.1 | +8.7 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.1 | +5.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.6 | +7.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.4 | +1.3 |
|  | [[EX229 (drug)]] 5 µM |  | +3.4 | +3.9 |
|  | [[Belzutifan (drug)]] 5 µM |  | +2.7 | +2.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.5 | +3.9 |
| fall | [[Cobimetinib (drug)]] 5 µM |  | -4.6 | -7.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -4.1 | +3.9 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -3.9 | -5.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | -3.8 | -3.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.8 | -3.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.7 | -3.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.6 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | RNA polymerase I and III subunit C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.1 — chr6:43,509,702-43,562,419 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RPA40, RPA39, RPA5, RPAC1, AC40, RPC40 |
| Gene groups (HGNC) | RNA polymerase subunits |
| Hallmark sets | DNA_REPAIR |
| Reactome | 19 pathways, smallest: RNA Polymerase III Chain Elongation; RNA Polymerase III Transcription Termination; RNA Polymerase III Transcription Initiation From Type 2 Promoter |
| Matched by | ensembl_id |

**Function**, from UniProt [O15160](https://www.uniprot.org/uniprotkb/O15160) (DNA-directed RNA polymerases I and III subunit RPAC1):

> DNA-dependent RNA polymerase catalyzes the transcription of DNA into RNA using the four ribonucleoside triphosphates as substrates. Common component of RNA polymerases I and III which synthesize ribosomal RNA precursors and short non-coding RNAs including 5S rRNA, snRNAs, tRNAs and miRNAs, respectively. POLR1C/RPAC1 is part of the polymerase core and may function as a clamp element that moves to open and close the cleft.

**Summary**, from NCBI Gene [9533](https://www.ncbi.nlm.nih.gov/gene/9533):

> The protein encoded by this gene is a subunit of both RNA polymerase I and RNA polymerase III complexes. The encoded protein is part of the Pol core element. Mutations in this gene have been associated with Treacher Collins syndrome (TCS) and hypomyelinating leukodystrophy 11. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jan 2016]

**Accessions** — [HGNC:20194](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20194) · Entrez [9533](https://www.ncbi.nlm.nih.gov/gene/9533) · UniProt [O15160](https://www.uniprot.org/uniprotkb/O15160) · Ensembl [ENSG00000171453](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171453)

## Data

Gene col 10111: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10111); `tables/drug_effects.parquet` (57 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10111, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10111]; `tensor/DDL_lfc|DDL_z.npy` [10111]; `embed/gene_vectors.npy` [10111]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10111 or target_col == 10111). Every well: [[POLR1C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/POLR1C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
