---
symbol: "GTPBP4"
type: "gene"
col: 2899
ensembl_id: "ENSG00000107937"
name: "GTP binding protein 4"
location: "10p15.3"
module: 5
arm: "+"
pooled_cpm: 116.74
n_lines_expressing: 50
n_dd_up: 40
n_dd_down: 15
n_dd_up_clean: 23
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# GTPBP4

*GTP binding protein 4* — 10p15.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 40 drug-doses (17 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 2.54× (z +16.9, q 0e+00, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (2 with an alert ⚠); the strongest is [[Ponatinib (drug)]] 5 µM: 0.719× (z -6.0, q 1e-06, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PNO1]] (+0.78, fdr 7e-06), [[MRTO4]] (+0.77, fdr 7e-06), [[PUS1]] (+0.77, fdr 7e-06); moves opposite to [[TXNDC16]] (-0.67, fdr 2e-05), [[ELF2]] (-0.62, fdr 7e-06), [[PPDPF]] (-0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 46 in all, 20 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 40 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2899.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.54×** | +16.9 | 0e+00 | 44/48 (NCI-H1792, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.86×** | +16.0 | 0e+00 | 41/48 (NCI-H1792, A498, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **4.71×** | +14.7 | 0e+00 | 46/49 (LoVo, HOP62, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **2.09×** | +13.4 | 9e-39 | 46/48 (SW480, A-172, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **4.10×** | +13.4 | 9e-39 | 46/48 (RKO, SK-MEL-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.82×** | +10.9 | 9e-26 | 41/48 (NCI-H1573, SW480, …) | all doses, stronger at high dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.82×** | +10.9 | 9e-26 | 44/48 (NCI-H1792, HT-29, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.78×** | +10.4 | 1e-23 | 45/48 (HT-29, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.61×** | +8.4 | 4e-15 | 37/47 (CFPAC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~85% of this change | **1.57×** | +8.2 | 1e-14 | 40/49 (HT-29, NCI-H1792, …) | all doses, flat | composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.30×** | +7.9 | 1e-13 | 35/38 (NCI-H1573, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | **1.54×** | +7.9 | 1e-13 | 35/48 (NCI-H1573, LS 180, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | **1.56×** | +7.5 | 3e-12 | 33/45 (NCI-H1573, NCI-H1792, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.51×** | +7.5 | 3e-12 | 39/48 (NCI-H1573, SW480, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.54×** | +7.5 | 4e-12 | 39/48 (HOP62, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.48×** | +7.1 | 4e-11 | 39/48 (HT-29, HOP62, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.41×** | +6.3 | 9e-09 | 37/48 (LOX-IMVI, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[EX229 (drug)]] 5 µM |  | **1.90×** | +6.1 | 3e-08 | 39/48 (MIA PaCa-2, NCI-H1792, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.86×** | +5.9 | 8e-08 | 39/48 (NCI-H1792, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.80×** | +5.6 | 6e-07 | 41/48 (MIA PaCa-2, HT-29, …) | rises with dose | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.66×** | +4.8 | 3e-05 | 33/48 (NCI-H1792, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.29×** | +4.6 | 8e-05 | 27/48 (MIA PaCa-2, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[EX229 (drug)]] 0.5 µM |  | **1.55×** | +4.5 | 1e-04 | 31/49 (NCI-H1792, MIA PaCa-2, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.57×** | +4.3 | 3e-04 | 32/48 (NCI-H1792, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2899.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **0.719×** | -6.0 | 1e-06 | 38/48 (LoVo, RKO, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.907× | -5.9 | 1e-06 | 5/50 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.755×** | -4.7 | 5e-04 | 30/50 (LoVo, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.775×** | -4.4 | 0.001 | 33/47 (LOX-IMVI, LoVo, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.797×** | -4.3 | 0.002 | 24/48 (MIA PaCa-2, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 0.843× | -4.3 | 0.002 | 24/48 (LoVo, SW 1088, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.786×** | -4.0 | 0.005 | 26/48 (LoVo, SW480, …) | all doses, flat |  |
| [[Bimiralisib (drug)]] 5 µM |  | **0.662×** | -3.9 | 0.006 | 27/50 (LoVo, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Afatinib (drug)]] 5 µM |  | **0.768×** | -3.9 | 0.007 | 25/49 (BT-474, C-33 A, …) | rises with dose | noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **0.819×** | -3.6 | 0.017 | 23/48 (KATO III, J82, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.871× | -3.5 | 0.022 | 16/48 (LoVo, RKO, …) | inconsistent across doses | low cells (technical?) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.820×** | -3.4 | 0.027 | 20/48 (LoVo, NCI-H23, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.829×** | -3.4 | 0.028 | 24/47 (MIA PaCa-2, LoVo, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.823×** | -3.4 | 0.028 | 19/47 (LOX-IMVI, LoVo, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.822×** | -3.3 | 0.031 | 20/49 (LoVo, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.838× | -3.2 | 0.048 | 19/47 (LoVo, NCI-H2030, …) | rises with dose | low cells (technical?) |
| [[Verteporfin (drug)]] 5 µM |  | **0.833×** | -3.2 | 0.049 | 22/49 (A498, J82, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.887× | -3.1 | 0.065 | 8/48 (AsPC-1, A498, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.845× | -3.0 | 0.065 | 19/49 (LoVo, MIA PaCa-2, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.32 per unit of S-phase module lfc, +0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2899. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 63.7 | 15 (12 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +15.3) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.74× (z +13.1) | — |
| [[NCI-H1792 (line)]] | alt | 98.4 | 11 (9 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.07× (z +19.5) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 6.97× (z +19.0) | — |
| [[HOP62 (line)]] | alt | 63.8 | 10 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.89× (z +16.0) | — |
| [[HT-29 (line)]] | alt | 105 | 9 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.16× (z +13.9) | — |
| [[A-172 (line)]] | wt | 78.3 | 7 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.63× (z +13.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 135 | 6 (2 ⚠) | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.84× (z +12.9) | [[Adagrasib (drug)]] 0.05 µM 0.606× (z -16.3) ⚠ position not correctable |
| [[PANC-1 (line)]] | alt | 125 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +14.7) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.01× (z +13.6) | — |
| [[SK-MEL-2 (line)]] | alt | 155 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +12.9) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.71× (z +12.3) | — |
| [[SNU-423 (line)]] | alt | 58.8 | 7 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.27× (z +17.8) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.86× (z +11.7) | — |
| [[CFPAC-1 (line)]] | alt | 95.8 | 6 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.85× (z +16.2) | — |
| [[COLO 205 (line)]] | alt | 69.6 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +11.4) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 15.1× (z +11.2) | — |
| [[LoVo (line)]] | wt | 140 | 4 (1 ⚠) | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 7.17× (z +13.1) | [[Ponatinib (drug)]] 5 µM 0.482× (z -9.4) |
| [[SW480 (line)]] | alt | 99.1 | 6 (4 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.14× (z +16.2) | — |
| [[AsPC-1 (line)]] | alt | 154 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +11.9) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.96× (z +11.0) | — |
| [[RPMI-7951 (line)]] | alt | 169 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.15× (z +14.4) | — |
| [[HEC-1-A (line)]] | alt | 109 | 4 | 0 | [[Auranofin (drug)]] 5 µM 2.82× (z +12.8) | — |
| [[HS-578T (line)]] | alt | 69.2 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +13.9) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.24× (z +10.9) | — |
| [[hTERT-HPNE (line)]] | wt | 87.7 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.65× (z +11.2) | — |
| [[LOX-IMVI (line)]] | wt | 157 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.28× (z +11.0) | — |
| [[LS 180 (line)]] | wt | 98.6 | 4 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.66× (z +10.3) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 6.32× (z +10.2) | — |
| [[NCI-H460 (line)]] | wt | 86.1 | 4 (3 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.65× (z +9.9) ⚠ unreliable plate only · without an alert: [[Auranofin (drug)]] 5 µM 2.59× (z +9.7) | — |
| [[RKO (line)]] | wt | 289 | 2 | 2 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 5.53× (z +12.3) | [[Harringtonine (drug)]] 5 µM 0.523× (z -8.6) ⚠ cell-cycle shift, explains ~67% of this change · without an alert: [[Ponatinib (drug)]] 5 µM 0.538× (z -8.6) |
| [[A498 (line)]] | wt | 158 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +19.0) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.38× (z +17.2) | — |
| [[A549 (line)]] | wt | 120 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +15.6) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.11× (z +11.4) | — |
| [[Hs 766T (line)]] | wt | 68.9 | 3 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 9.07× (z +9.5) | — |
| [[KATO III (line)]] | alt | 87.4 | 3 | 0 | [[PH-797804 (drug)]] 5 µM 6.39× (z +10.9) | — |
| [[NCI-H2030 (line)]] | alt | 218 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +9.8) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.33× (z +9.6) | — |
| [[NCI-H2347 (line)]] | alt | 74.0 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.64× (z +10.0) | — |
| [[Panc 03.27 (line)]] | alt | 75.8 | 3 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.58× (z +12.6) | — |
| [[SW 900 (line)]] | alt | 89.9 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +13.8) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.80× (z +12.6) | — |
| [[H4 (line)]] | wt | 65.7 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +10.1) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.41× (z +8.8) | — |
| [[HepG2_C3A (line)]] | wt | 119 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +11.2) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.91× (z +11.0) | — |
| [[AN3 CA (line)]] | alt | 113 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.04× (z +10.3) | — |
| [[BT-474 (line)]] | alt | 122 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.21× (z +12.0) | — |
| [[C-33 A (line)]] | alt | 154 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.89× (z +10.1) | — |
| [[HCT15 (line)]] | alt | 93.7 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.41× (z +9.5) | — |
| [[J82 (line)]] | alt | 161 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.21× (z +9.6) | — |
| [[NCI-H23 (line)]] | alt | 208 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.82× (z +11.4) | — |
| [[SHP-77 (line)]] | alt | 122 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.35× (z +9.4) | — |
| [[SNU-1 (line)]] | wt | 135 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 7.31× (z +9.7) | — |
| [[A-427 (line)]] | wt | 161 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 45.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 106 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 92.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 57.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 79.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 143 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 173 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2899), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PNO1]] | +0.78 | +0.79 / +0.75 | both halves | 7e-06 | STRING 772 |
| [[MRTO4]] | +0.77 | +0.80 / +0.72 | both halves | 7e-06 | STRING 999 |
| [[PUS1]] | +0.77 | +0.74 / +0.78 | both halves | 7e-06 | STRING 403 |
| [[NOP2]] | +0.77 | +0.78 / +0.75 | both halves | 7e-06 | STRING 993 |
| [[DDX21]] | +0.77 | +0.76 / +0.76 | both halves | 7e-06 | STRING 813 |
| [[WDR4]] | +0.77 | +0.73 / +0.79 | both halves | 7e-06 | STRING 425 |
| [[TSR1]] | +0.76 | +0.71 / +0.74 | both halves | 7e-06 | STRING 923 |
| [[NOM1]] | +0.75 | +0.79 / +0.75 | both halves | 7e-06 | STRING 433 |
| [[NOP16]] | +0.75 | +0.79 / +0.71 | both halves | 7e-06 |  |
| [[TWNK]] | +0.74 | +0.79 / +0.71 | both halves | 7e-06 |  |
| [[DDX31]] | +0.74 | +0.75 / +0.71 | both halves | 7e-06 | STRING 882 |
| [[SDAD1]] | +0.74 | +0.75 / +0.66 | both halves | 7e-06 | STRING 997 |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TXNDC16]] | -0.67 | -0.48 / -0.62 | both halves | 2e-05 |  |
| [[ELF2]] | -0.62 | -0.63 / -0.61 | both halves | 7e-06 |  |
| [[PPDPF]] | -0.62 | -0.52 / -0.62 | both halves | 1e-05 |  |
| [[PLAG1]] | -0.61 | -0.61 / -0.56 | both halves | 1e-05 |  |
| [[USP33]] | -0.60 | -0.60 / -0.52 | both halves | 1e-05 |  |
| [[RCOR3]] | -0.60 | -0.60 / -0.60 | both halves | 7e-06 |  |
| [[CAT]] | -0.60 | -0.62 / -0.53 | both halves | 1e-05 |  |
| [[KBTBD3]] | -0.59 | -0.54 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises GTPBP4's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.1% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.814). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-14.7, -36.2); signed map (-1.5, -46.9). **Vector** length 99.2, 39.6% of its response variance represented; |z| ≥ 3 in 1,670 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MYC targets v2* (hallmark, mean cos +0.66 to 13); *rRNA processing* (reactome, mean cos +0.60 to 20); *rRNA processing in the nucleus and cytosol* (reactome, mean cos +0.60 to 19).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.8 | +10.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.2 | +13.4 |
|  | [[EX229 (drug)]] 5 µM |  | +5.4 | +6.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.5 | +13.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +4.4 | +5.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | +4.0 | +4.3 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | -4.5 | +7.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | -4.5 | +10.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | -4.1 | +6.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.9 | -6.0 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | -3.0 | +6.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.8 | -3.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.7 | -4.0 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.6 | -2.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.3 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | GTP binding protein 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p15.3 — chr10:988,434-1,019,932 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CRFG, NGB, FLJ10690, FLJ10686, NOG1 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BZE4](https://www.uniprot.org/uniprotkb/Q9BZE4) (GTP-binding protein 4):

> Involved in the biogenesis of the 60S ribosomal subunit. Acts as a TP53 repressor, preventing TP53 stabilization and cell cycle arrest.

**Summary**, from NCBI Gene [23560](https://www.ncbi.nlm.nih.gov/gene/23560):

> GTP-binding proteins are GTPases and function as molecular switches that can flip between two states: active, when GTP is bound, and inactive, when GDP is bound. 'Active' in this context usually means that the molecule acts as a signal to trigger other events in the cell. When an extracellular ligand binds to a G-protein-linked receptor, the receptor changes its conformation and switches on the trimeric G proteins that associate with it by causing them to eject their GDP and replace it with …

**Accessions** — [HGNC:21535](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21535) · Entrez [23560](https://www.ncbi.nlm.nih.gov/gene/23560) · UniProt [Q9BZE4](https://www.uniprot.org/uniprotkb/Q9BZE4) · Ensembl [ENSG00000107937](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000107937)

## Data

Gene col 2899: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2899); `tables/drug_effects.parquet` (70 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2899, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2899]; `tensor/DDL_lfc|DDL_z.npy` [2899]; `embed/gene_vectors.npy` [2899]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2899 or target_col == 2899). Every well: [[GTPBP4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GTPBP4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
