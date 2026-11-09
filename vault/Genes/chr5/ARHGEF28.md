---
symbol: "ARHGEF28"
type: "gene"
col: 13233
ensembl_id: "ENSG00000214944"
name: "Rho guanine nucleotide exchange factor 28"
location: "5q13.2"
module: 120
arm: "+"
pooled_cpm: 114.0
n_lines_expressing: 44
n_dd_up: 23
n_dd_down: 21
n_dd_up_clean: 16
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 5
direction_downstream: 2
tags: ["gene", "module/120"]
generated_by: "tahoemap"
---

# ARHGEF28

*Rho guanine nucleotide exchange factor 28* — 5q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.58× (z +10.4, q 2e-22, up in 24 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.594× (z -8.0, q 1e-12, down in 26 of 43 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 0.628× (z -7.4, q 3e-11, down in 34 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CRIM1]] (+0.63, fdr 1e-05), [[KIFC3]] (+0.58, fdr 1e-05), [[SRGAP1]] (+0.58, fdr 1e-05); moves opposite to [[NRSN2]] (-0.51, fdr 2e-05), [[TMEM145]] (-0.45, fdr 5e-05), [[RAB2B]] (-0.44, fdr 9e-05).
> It is in [[Module 120]], a single-armed module (RHOA GTPase cycle).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[DAPK1]] → it (grade B ⚠); 2 go from it, the strongest it → [[PARD3B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13233.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.58×** | +10.4 | 2e-22 | 24/42 (Hs 766T, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.33×** | +6.5 | 3e-08 | 23/42 (LS 180, SW480, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.38×** | +5.2 | 5e-05 | 26/43 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[BAY1125976 (drug)]] 5 µM |  | **1.74×** | +4.6 | 5e-04 | 26/42 (HEC-1-A, J82, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.32×** | +4.4 | 0.001 | 22/42 (MIA PaCa-2, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Rapamycin (drug)]] 5 µM |  | **1.21×** | +4.3 | 0.002 | 22/42 (Hs 766T, A-172, …) | all doses, stronger at high dose |  |
| [[Larotrectinib sulfate (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.30×** | +4.2 | 0.002 | 22/42 (Hs 766T, PANC-1, …) | two highest doses |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.30×** | +3.9 | 0.006 | 22/42 (PANC-1, Hs 766T, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 5 µM |  | **1.60×** | +3.9 | 0.006 | 23/43 (HEC-1-A, Hs 766T, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Hydroxyfasudil (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.26×** | +3.7 | 0.012 | 20/42 (Hs 766T, Panc 03.27, …) | inconsistent across doses |  |
| [[MK-3903 (drug)]] 5 µM |  | **1.54×** | +3.6 | 0.016 | 18/42 (HEC-1-A, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.25×** | +3.5 | 0.020 | 20/42 (NCI-H1573, A-172, …) | rises with dose |  |
| [[Tofacitinib (drug)]] 5 µM |  | 1.17× | +3.5 | 0.020 | 18/43 (A549, COLO 205, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.23×** | +3.4 | 0.027 | 17/42 (HOP62, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.49×** | +3.4 | 0.027 | 18/43 (NCI-H2347, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **1.46×** | +3.2 | 0.044 | 15/44 (NCI-H1573, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Rapamycin (drug)]] 0.5 µM |  | **1.22×** | +3.2 | 0.044 | 15/42 (Hs 766T, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Demeclocycline (drug)]] 5 µM |  | 1.14× | +3.0 | 0.065 | 10/42 (NCI-H2030, CFPAC-1, …) | top dose only |  |
| [[AZD-8055 (drug)]] 0.5 µM |  | **1.30×** | +3.0 | 0.065 | 13/42 (PANC-1, Hs 766T, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13233.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **0.594×** | -8.0 | 1e-12 | 26/43 (RKO, A-427, …) | all doses, flat | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.628×** | -7.4 | 3e-11 | 34/42 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.646×** | -7.0 | 5e-10 | 34/42 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.699×** | -5.4 | 9e-06 | 27/42 (HT-29, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **0.696×** | -5.4 | 9e-06 | 24/39 (HEC-1-A, Panc 03.27, …) | all doses, flat | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.747×** | -4.7 | 3e-04 | 24/42 (HEC-1-A, RKO, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **0.758×** | -4.4 | 8e-04 | 24/42 (NCI-H460, NCI-H1573, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.775×** | -4.1 | 0.003 | 22/42 (RKO, HEC-1-A, …) | two highest doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.626×** | -3.9 | 0.006 | 23/40 (RKO, SW48, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~82% of this change | **0.792×** | -3.6 | 0.019 | 21/37 (A-427, Panc 03.27, …) | all doses, flat | composition shift |
| [[Abemaciclib (drug)]] 5 µM |  | **0.665×** | -3.4 | 0.030 | 15/42 (HEC-1-A, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.800×** | -3.4 | 0.030 | 19/42 (NCI-H460, HEC-1-A, …) | two highest doses |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.860× | -3.4 | 0.030 | 10/42 (SW480, SHP-77, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.818×** | -3.2 | 0.053 | 21/42 (HT-29, COLO 205, …) | rises with dose |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.756×** | -3.2 | 0.053 | 16/42 (HEC-1-A, COLO 205, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.758×** | -3.2 | 0.055 | 19/43 (PANC-1, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.690×** | -3.1 | 0.059 | 17/42 (A498, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.763×** | -3.1 | 0.059 | 12/42 (CFPAC-1, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.703×** | -3.0 | 0.085 | 20/42 (SK-MEL-2, RKO, …) | top dose only | noisy plate (z scaled) |
| [[Pimitespib (drug)]] 0.05 µM |  | **0.825×** | -2.9 | 0.094 | 13/42 (NCI-H1573, Hs 766T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13233. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 139 | 1 (1 ⚠) | 13 (11 ⚠) | [[TAK-901 (drug)]] 5 µM 5.27× (z +8.8) ⚠ cell-cycle shift, explains ~0% of this change | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.160× (z -18.8) ⚠ cell-cycle shift, explains ~64% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.244× (z -14.5) |
| [[RKO (line)]] | wt | 413 | 0 | 12 (9 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0998× (z -20.0) ⚠ toxic; cell-cycle shift, explains ~34% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.357× (z -9.3) |
| [[HT-29 (line)]] | alt | 378 | 0 | 8 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.145× (z -17.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~82% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.268× (z -12.7) |
| [[NCI-H2030 (line)]] | alt | 296 | 0 | 8 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.359× (z -13.9) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.359× (z -9.3) |
| [[HEC-1-A (line)]] | alt | 176 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.281× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.572× (z -9.1) |
| [[Panc 03.27 (line)]] | alt | 614 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.126× (z -20.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~82% of this change |
| [[PANC-1 (line)]] | alt | 197 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.289× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.316× (z -11.4) |
| [[Hs 766T (line)]] | wt | 113 | 4 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.82× (z +19.2) | [[Dinaciclib (drug)]] 5 µM 0.261× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~82% of this change |
| [[J82 (line)]] | alt | 172 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.304× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[NCI-H1573 (line)]] | alt | 38.6 | 3 (2 ⚠) | 1 (1 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 2.91× (z +10.1) | [[Digitoxin (drug)]] 5 µM 0.179× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change |
| [[A-427 (line)]] | wt | 99.0 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.110× (z -21.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~82% of this change |
| [[MIA PaCa-2 (line)]] | alt | 63.2 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.76× (z +16.0) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.289× (z -10.3) ⚠ toxic; cell-cycle shift, explains ~34% of this change |
| [[A498 (line)]] | wt | 89.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.400× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[A549 (line)]] | wt | 181 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.326× (z -14.3) ⚠ cell-cycle shift, explains ~42% of this change |
| [[CFPAC-1 (line)]] | alt | 160 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.33× (z +8.5) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.355× (z -10.0) ⚠ toxic; cell-cycle shift, explains ~34% of this change |
| [[COLO 205 (line)]] | alt | 118 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.280× (z -11.0) |
| [[HOP62 (line)]] | alt | 32.6 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.39× (z +14.8) | — |
| [[LoVo (line)]] | wt | 63.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.355× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[LS 180 (line)]] | wt | 76.2 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.325× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change |
| [[SK-MEL-2 (line)]] | alt | 53.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +10.9) | [[Dinaciclib (drug)]] 5 µM 0.250× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~82% of this change |
| [[A-172 (line)]] | wt | 65.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +10.9) | — |
| [[AsPC-1 (line)]] | alt | 90.8 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.264× (z -9.4) ⚠ cell-cycle shift, explains ~64% of this change |
| [[HS-578T (line)]] | alt | 42.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.24× (z +11.3) | — |
| [[hTERT-HPNE (line)]] | wt | 39.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +8.6) | — |
| [[LOX-IMVI (line)]] | wt | 37.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +8.9) | — |
| [[NCI-H1792 (line)]] | alt | 58.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.66× (z +14.4) | — |
| [[NCI-H23 (line)]] | alt | 41.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.01× (z +14.6) | — |
| [[RPMI-7951 (line)]] | alt | 40.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.64× (z +12.4) | — |
| [[SNU-423 (line)]] | alt | 102 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +13.9) | — |
| [[SW1417 (line)]] | alt | 78.9 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.321× (z -10.7) ⚠ toxic; cell-cycle shift, explains ~34% of this change |
| [[SW48 (line)]] | wt | 44.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.198× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change |
| [[SW480 (line)]] | alt | 41.9 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.432× (z -8.5) ⚠ cell-cycle shift, explains ~64% of this change |
| [[AN3 CA (line)]] | alt | 58.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 17.6 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 20.0 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 22.5 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 34.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 26.2 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 171 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 57.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 88.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 63.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 79.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.9 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 23.5 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 67.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 329 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 59.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13233), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CRIM1]] | +0.63 | +0.59 / +0.55 | both halves | 1e-05 | **novel candidate** |
| [[KIFC3]] | +0.58 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[SRGAP1]] | +0.58 | +0.52 / +0.54 | both halves | 1e-05 | pathway: RHOA GTPase cycle |
| [[DDAH1]] | +0.58 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[MGLL]] | +0.57 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[LINC00472]] | +0.55 | +0.60 / +0.47 | both halves | 2e-05 |  |
| [[ERBIN]] | +0.54 | +0.51 / +0.48 | both halves | 2e-05 | pathway: RHOA GTPase cycle |
| [[SLC35F3]] | +0.53 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[PGM5P2-1]] | +0.53 | +0.47 / +0.45 | both halves | 3e-05 |  |
| [[ST6GALNAC5]] | +0.53 | +0.45 / +0.45 | both halves | 3e-05 |  |
| [[CCN1]] | +0.52 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[MARCHF4]] | +0.51 | +0.45 / +0.53 | both halves | 3e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NRSN2]] | -0.51 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[TMEM145]] | -0.45 | -0.44 / -0.39 | both halves | 5e-05 |  |
| [[RAB2B]] | -0.44 | -0.52 / -0.36 | both halves | 9e-05 |  |
| [[PLEKHG4B]] | -0.43 | -0.39 / -0.44 | both halves | 5e-05 | same gene group |
| [[LINC03047]] | -0.43 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[PLXNB3]] | -0.42 | -0.49 / -0.39 | both halves | 5e-05 |  |
| [[DDX41]] | -0.42 | -0.44 / -0.38 | both halves | 6e-05 |  |
| [[ABCB6]] | -0.42 | -0.44 / -0.33 | both halves | 1e-04 |  |
| [[APOBEC3G]] | -0.41 | -0.45 / -0.33 | both halves | 1e-04 |  |
| [[SH3D21]] | -0.41 | -0.45 / -0.31 | both halves | 2e-04 |  |
| [[ARHGEF6]] | -0.41 | -0.40 / -0.43 | both halves | 5e-05 | same gene group |
| [[AIM2]] | -0.41 | -0.40 / -0.43 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DAPK1]] | B | DAPK1 activity raises ARHGEF28's level | lines that do not express DAPK1 (23) vs lines expressing it (27) | 2.12× lower at baseline in the lines without DAPK1 | 0.016 | ⚠ within organs, on part of the lines; also absent: HAVCR1, DCDC2, ENSG00000275649 |
| [[AIM2]] | B | AIM2 activity weakens ARHGEF28's drug response | lines that do not express AIM2 (22) vs lines expressing it (21) | the lines without AIM2 respond 1.52× as strongly (z diff -1.17); strongest at Dinaciclib 0.5 µM: 0.41x vs 0.81x (z diff -4.7) | 0.060 | ⚠ within organs, on part of the lines; also absent: PEX5L, PHACTR1, ARMCX2; target measured in part of the lines; artifact flags |
| [[MGLL]] | B | MGLL activity raises ARHGEF28's level | lines that do not express MGLL (14) vs lines expressing it (36) | 2.03× lower at baseline in the lines without MGLL | 0.073 | ⚠ within organs, on part of the lines; also absent: CXCL3, MET, PSORS1C1; maybe low, not absent |
| [[MTOR]] | B | MTOR activity lowers ARHGEF28's level | compounds that target MTOR: 4 of 8 raise it (AZD-8055, Bimiralisib, Rapamycin, Sapanisertib) | 50% of the class's compounds vs 4.5% of all compounds | 0.077 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SHANK2]] | B | SHANK2 activity raises ARHGEF28's level | lines that do not express SHANK2 (15) vs lines expressing it (35) | 2.64× lower at baseline in the lines without SHANK2 | 0.079 | ⚠ within organs, on part of the lines; also absent: CDCP1, CHMP4C, EPS8L2 |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PARD3B]] | B | ARHGEF28 activity lowers PARD3B's level | lines that do not express ARHGEF28 (6) vs lines expressing it (44) | 3.28× higher at baseline in the lines without ARHGEF28 | 0.039 | ⚠ within organs, on part of the lines; also absent: SHB, RABGEF1P3, TBILA; maybe low, not absent |
| [[MGLL]] | B | ARHGEF28 activity raises MGLL's level | lines that do not express ARHGEF28 (6) vs lines expressing it (44) | 3.35× lower at baseline in the lines without ARHGEF28 | 0.076 | ⚠ within organs, on part of the lines; also absent: SHB, RABGEF1P3, TBILA; maybe low, not absent |

## Where it sits

- **Module**: [[Module 120]] — RHOA GTPase cycle; 41 genes; every member is in the + arm (projection on the module's main direction 0.678). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (40.6, 11.5); signed map (13.1, 42.4). **Vector** length 123, 37.0% of its response variance represented; |z| ≥ 3 in 1,357 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +5.8 | +3.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +5.8 | +2.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.8 | +10.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | +5.6 | +2.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.5 | +4.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +5.1 | +1.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.9 | +6.5 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +4.4 | +2.1 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -6.6 | -7.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -6.2 | -7.4 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -4.8 | -5.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.1 | -4.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.9 | -3.4 |
|  | [[venetoclax (drug)]] 5 µM |  | -3.8 | -3.0 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -3.6 | -3.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.1 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | Rho guanine nucleotide exchange factor 28 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q13.2 — chr5:73,626,158-73,941,993 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RGNEF, p190RhoGEF, RIP2 |
| Gene groups (HGNC) | Dbl family Rho GEFs |
| Reactome | 10 pathways, smallest: EPHB-mediated forward signaling; RHOB GTPase cycle; RHOC GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N1W1](https://www.uniprot.org/uniprotkb/Q8N1W1) (Rho guanine nucleotide exchange factor 28):

> Functions as a RHOA-specific guanine nucleotide exchange factor regulating signaling pathways downstream of integrins and growth factor receptors. Functions in axonal branching, synapse formation and dendritic morphogenesis. Also functions in focal adhesion formation, cell motility and B-lymphocytes activation. May regulate NEFL expression and aggregation and play a role in apoptosis (By similarity).

**Summary**, from NCBI Gene [64283](https://www.ncbi.nlm.nih.gov/gene/64283):

> This gene encodes a member of the Rho guanine nucleotide exchange factor family. The encoded protein interacts with low molecular weight neurofilament mRNA and may be involved in the formation of amyotrophic lateral sclerosis neurofilament aggregates. Alternate splicing results in multiple transcript variants.[provided by RefSeq, Apr 2010]

**Accessions** — [HGNC:30322](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30322) · Entrez [64283](https://www.ncbi.nlm.nih.gov/gene/64283) · UniProt [Q8N1W1](https://www.uniprot.org/uniprotkb/Q8N1W1) · Ensembl [ENSG00000214944](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000214944)

## Data

Gene col 13233: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13233); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13233, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13233]; `tensor/DDL_lfc|DDL_z.npy` [13233]; `embed/gene_vectors.npy` [13233]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13233 or target_col == 13233). Every well: [[ARHGEF28 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARHGEF28.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
