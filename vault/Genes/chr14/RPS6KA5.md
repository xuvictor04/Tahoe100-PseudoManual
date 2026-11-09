---
symbol: "RPS6KA5"
type: "gene"
col: 2021
ensembl_id: "ENSG00000100784"
name: "ribosomal protein S6 kinase A5"
location: "14q32.11"
module: 76
arm: "+"
pooled_cpm: 140.57
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 28
n_dd_up_clean: 12
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/076"]
generated_by: "tahoemap"
---

# RPS6KA5

*ribosomal protein S6 kinase A5* — 14q32.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.71× (z +12.5, q 6e-33, up in 36 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (7 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.397× (z -21.3, q 0e+00, down in 45 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.505× (z -15.8, q 0e+00, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAP3K3]] (+0.68, fdr 1e-05), [[SPSB3]] (+0.65, fdr 2e-05), [[FBXO33]] (+0.62, fdr 3e-05); moves opposite to [[MTHFSD]] (-0.67, fdr 1e-05), [[TACO1]] (-0.65, fdr 1e-05), [[GSS]] (-0.65, fdr 1e-05).
> It is in [[Module 076]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MTOR]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 2 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2021.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.71×** | +12.5 | 6e-33 | 36/48 (NCI-H2347, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.65×** | +11.6 | 2e-28 | 38/48 (NCI-H2347, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.63×** | +11.4 | 9e-28 | 37/48 (NCI-H2347, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.56×** | +10.3 | 8e-23 | 36/48 (NCI-H2347, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.47×** | +8.6 | 1e-15 | 35/47 (HOP62, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.40×** | +7.9 | 3e-13 | 31/48 (NCI-H2347, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.71×** | +6.1 | 7e-08 | 27/49 (NCI-H2347, Panc 03.27, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.20× | +6.0 | 2e-07 | 22/48 (NCI-H2347, Panc 03.27, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.21×** | +4.5 | 5e-04 | 19/48 (SW480, C-33 A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.9 | 0.007 | 21/48 (C32, CFPAC-1, …) | inconsistent across doses | composition shift |
| [[GSK1059615 (drug)]] 5 µM |  | **1.34×** | +3.4 | 0.040 | 11/49 (NCI-H460, SW48, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.33×** | +3.3 | 0.045 | 15/48 (A498, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **1.32×** | +3.2 | 0.061 | 13/50 (NCI-H460, LS 180, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 5 µM |  | **1.31×** | +3.1 | 0.084 | 8/49 (CFPAC-1, J82, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.14× | +3.1 | 0.084 | 13/49 (KATO III, C32, …) | top dose only |  |
| [[AZD-8055 (drug)]] 0.5 µM |  | **1.20×** | +3.0 | 0.084 | 7/48 (LoVo, J82, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 11 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2021.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.397×** | -21.3 | 0e+00 | 45/48 (HEC-1-A, NCI-H2030, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.505×** | -15.8 | 0e+00 | 44/48 (PANC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.505×** | -15.8 | 0e+00 | 35/48 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.518×** | -14.6 | 0e+00 | 39/48 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.651×** | -14.0 | 2e-42 | 30/48 (A-427, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[TAK-733 (drug)]] 5 µM |  | **0.307×** | -13.5 | 2e-39 | 42/48 (HEC-1-A, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.594×** | -12.0 | 2e-31 | 38/48 (LoVo, HEC-1-A, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.382×** | -11.0 | 3e-26 | 38/48 (HEC-1-A, A-427, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.408×** | -10.2 | 8e-23 | 36/48 (HEC-1-A, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **0.424×** | -9.8 | 7e-21 | 40/47 (NCI-H23, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.433×** | -9.6 | 7e-20 | 36/49 (A-427, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.653×** | -9.5 | 1e-19 | 31/44 (SHP-77, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.568×** | -9.3 | 5e-19 | 37/48 (SW480, NCI-H23, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.445×** | -9.2 | 9e-19 | 36/48 (HEC-1-A, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.673×** | -9.2 | 2e-18 | 36/48 (MIA PaCa-2, A-427, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.771×** | -8.5 | 9e-16 | 27/48 (MIA PaCa-2, A498, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[venetoclax (drug)]] 5 µM |  | **0.510×** | -7.7 | 5e-13 | 34/48 (SK-MEL-2, SW480, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2021. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 141 | 5 (1 ⚠) | 13 (1 ⚠) | [[Panobinostat (drug)]] 0.05 µM 1.83× (z +10.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.385× (z -16.7) ⚠ unreliable plate only · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.418× (z -15.2) |
| [[HOP62 (line)]] | alt | 171 | 1 (1 ⚠) | 15 (5 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.74× (z +12.0) ⚠ toxic | [[Harringtonine (drug)]] 5 µM 0.212× (z -18.5) |
| [[HEC-1-A (line)]] | alt | 157 | 0 | 15 (4 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.237× (z -21.8) ⚠ unreliable plate only · without an alert: [[Auranofin (drug)]] 5 µM 0.360× (z -15.5) |
| [[A-427 (line)]] | wt | 171 | 0 | 12 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -29.4) |
| [[LoVo (line)]] | wt | 688 | 0 | 12 (8 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.213× (z -25.0) |
| [[A498 (line)]] | wt | 96.1 | 0 | 9 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.282× (z -15.1) ⚠ unreliable plate only · without an alert: [[Selinexor (drug)]] 5 µM 0.511× (z -11.3) |
| [[NCI-H23 (line)]] | alt | 78.9 | 0 | 9 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.251× (z -15.7) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.381× (z -15.5) |
| [[NCI-H2347 (line)]] | alt | 70.6 | 7 (1 ⚠) | 2 (1 ⚠) | [[Belinostat (drug)]] 5 µM 3.09× (z +14.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.280× (z -16.2) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.246× (z -8.9) |
| [[SK-MEL-2 (line)]] | alt | 226 | 0 | 8 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.350× (z -14.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.423× (z -12.1) |
| [[A549 (line)]] | wt | 137 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.446× (z -15.2) |
| [[CFPAC-1 (line)]] | alt | 302 | 2 (2 ⚠) | 5 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.13× (z +9.7) ⚠ cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 5 µM 0.408× (z -16.2) |
| [[HS-578T (line)]] | alt | 118 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.349× (z -15.1) |
| [[MIA PaCa-2 (line)]] | alt | 119 | 0 | 7 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.236× (z -16.2) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.301× (z -13.4) |
| [[NCI-H1573 (line)]] | alt | 72.1 | 3 | 4 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.75× (z +10.6) | [[Harringtonine (drug)]] 0.5 µM 0.260× (z -14.0) |
| [[NCI-H2030 (line)]] | alt | 157 | 0 | 7 (4 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.139× (z -19.0) ⚠ unreliable plate only · without an alert: [[Belzutifan (drug)]] 5 µM 0.155× (z -8.9) |
| [[PANC-1 (line)]] | alt | 65.6 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -21.2) |
| [[KATO III (line)]] | alt | 116 | 0 | 6 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.274× (z -13.6) ⚠ unreliable plate only · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.370× (z -10.5) |
| [[SW48 (line)]] | wt | 291 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -18.7) |
| [[A-172 (line)]] | wt | 86.3 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.453× (z -13.4) |
| [[AsPC-1 (line)]] | alt | 100 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -17.1) |
| [[Hs 766T (line)]] | wt | 133 | 1 | 4 (1 ⚠) | [[Dexamethasone (drug)]] 0.05 µM 2.47× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.278× (z -17.1) |
| [[SW1417 (line)]] | alt | 109 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.57× (z +11.2) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.381× (z -11.5) ⚠ unreliable plate only |
| [[HCT15 (line)]] | alt | 195 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.386× (z -14.1) |
| [[LS 180 (line)]] | wt | 293 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.201× (z -14.6) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.323× (z -10.7) |
| [[Panc 03.27 (line)]] | alt | 90.7 | 4 | 0 | [[Belinostat (drug)]] 5 µM 3.18× (z +12.3) | — |
| [[C32 (line)]] | wt | 129 | 3 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.24× (z +10.9) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[J82 (line)]] | alt | 131 | 3 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.76× (z +10.2) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 5 µM 2.39× (z +9.1) | — |
| [[SHP-77 (line)]] | alt | 130 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0645× (z -29.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.420× (z -9.6) |
| [[C-33 A (line)]] | alt | 60.3 | 1 (1 ⚠) | 1 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 3.15× (z +8.5) ⚠ toxic | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.251× (z -10.6) ⚠ unreliable plate only |
| [[HT-29 (line)]] | alt | 102 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.401× (z -9.8) |
| [[LOX-IMVI (line)]] | wt | 81.2 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.230× (z -16.2) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.398× (z -10.1) |
| [[NCI-H1792 (line)]] | alt | 112 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.363× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.542× (z -9.4) |
| [[NCI-H460 (line)]] | wt | 61.8 | 2 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.54× (z +10.3) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 2.18× (z +9.0) | — |
| [[SNU-1 (line)]] | wt | 115 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.132× (z -16.1) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 89.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.405× (z -14.4) |
| [[AN3 CA (line)]] | alt | 117 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.246× (z -9.1) ⚠ unreliable plate only |
| [[COLO 205 (line)]] | alt | 42.7 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.99× (z +8.5) ⚠ toxic | — |
| [[hTERT-HPNE (line)]] | wt | 77.2 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.383× (z -10.2) |
| [[NCI-H596 (line)]] | alt | 136 | 0 | 1 | — | [[Atazanavir (sulfate) (drug)]] 5 µM 0.119× (z -12.0) |
| [[RKO (line)]] | wt | 46.9 | 1 | 0 | [[Panobinostat (drug)]] 0.05 µM 2.83× (z +9.1) | — |
| [[RPMI-7951 (line)]] | alt | 65.0 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.244× (z -11.5) ⚠ unreliable plate only |
| [[BT-474 (line)]] | alt | 230 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 104 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 72.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 35.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 69.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 52.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 129 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2021), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*39 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAP3K3]] | +0.68 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[SPSB3]] | +0.65 | +0.48 / +0.64 | both halves | 2e-05 |  |
| [[FBXO33]] | +0.62 | +0.44 / +0.66 | both halves | 3e-05 |  |
| [[PHF1]] | +0.61 | +0.61 / +0.46 | both halves | 2e-05 |  |
| [[LINC01881]] | +0.60 | +0.43 / +0.62 | both halves | 3e-05 |  |
| [[STRN]] | +0.60 | +0.60 / +0.44 | both halves | 3e-05 |  |
| [[MIS18BP1]] | +0.58 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[KMT5C]] | +0.58 | +0.43 / +0.60 | both halves | 3e-05 |  |
| [[DHTKD1]] | +0.58 | +0.45 / +0.50 | both halves | 3e-05 |  |
| [[CBFA2T2]] | +0.57 | +0.58 / +0.39 | both halves | 5e-05 |  |
| [[CMC2]] | +0.57 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[MPST]] | +0.56 | +0.46 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*61 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTHFSD]] | -0.67 | -0.62 / -0.52 | both halves | 1e-05 |  |
| [[TACO1]] | -0.65 | -0.68 / -0.49 | both halves | 1e-05 |  |
| [[GSS]] | -0.65 | -0.66 / -0.56 | both halves | 1e-05 |  |
| [[PYM1]] | -0.60 | -0.57 / -0.47 | both halves | 2e-05 |  |
| [[KICS2]] | -0.60 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[DNAJC11]] | -0.59 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[POLR2M]] | -0.59 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[GUF1]] | -0.59 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[ZBTB6]] | -0.58 | -0.64 / -0.38 | both halves | 7e-05 |  |
| [[FUNDC1]] | -0.58 | -0.64 / -0.42 | both halves | 4e-05 |  |
| [[GTF2H3]] | -0.58 | -0.61 / -0.55 | both halves | 1e-05 |  |
| [[TMEM128]] | -0.58 | -0.62 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MTOR]] | B | MTOR activity lowers RPS6KA5's level | compounds that target MTOR: 4 of 8 raise it (AZD-8055, Bimiralisib, GSK1059615, Sapanisertib) | 50% of the class's compounds vs 2.8% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds |
| [[MYADM]] | C | MYADM activity lowers RPS6KA5's level | lines that do not express MYADM (3) vs lines expressing it (47) | 3.74× higher at baseline in the lines without MYADM | 0.004 | ⚠ few lines (3 vs 47); across organs; also absent: SRGAP2C, HSD17B14, DNAJB5 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 076]]; 59 genes; every member is in the + arm (projection on the module's main direction 0.586). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-17.9, 6.9); signed map (-20.9, 11.3). **Vector** length 144, 46.3% of its response variance represented; |z| ≥ 3 in 1,920 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +7.0 | +8.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +6.8 | +11.6 |
|  | [[Belinostat (drug)]] 5 µM |  | +6.8 | +11.4 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.5 | +1.8 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +5.3 | +7.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.6 | +6.1 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +3.9 | +3.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +3.0 | +3.3 |
|  | [[BAY1125976 (drug)]] 5 µM |  | +2.9 | +2.6 |
|  | [[Sapanisertib (drug)]] 5 µM |  | +2.6 | +3.1 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -12.2 | -21.3 |
|  | [[Selinexor (drug)]] 5 µM |  | -11.5 | -8.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -11.4 | -15.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -10.7 | -15.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -10.4 | -14.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | -10.0 | -13.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -9.7 | -9.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -9.4 | -12.0 |
|  | [[venetoclax (drug)]] 5 µM |  | -8.7 | -7.7 |
|  | [[EX229 (drug)]] 5 µM |  | -8.6 | -9.2 |

## What is on record

|  |  |
|---|---|
| Name | ribosomal protein S6 kinase A5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q32.11 — chr14:90,847,861-91,060,641 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MSK1, RLPK |
| Gene groups (HGNC) | MAPK activated protein kinases; Ribosomal protein S6 kinase family |
| Hallmark sets | G2M_CHECKPOINT |
| Reactome | 35 pathways, smallest: CREB phosphorylation; CD209 (DC-SIGN) signaling; ERK/MAPK targets |
| Matched by | ensembl_id |

**Function**, from UniProt [O75582](https://www.uniprot.org/uniprotkb/O75582) (Ribosomal protein S6 kinase alpha-5):

> Serine/threonine-protein kinase that is required for the mitogen or stress-induced phosphorylation of the transcription factors CREB1 and ATF1 and for the regulation of the transcription factors RELA, STAT3 and ETV1/ER81, and that contributes to gene activation by histone phosphorylation and functions in the regulation of inflammatory genes. Phosphorylates CREB1 and ATF1 in response to mitogenic or stress stimuli such as UV-C irradiation, epidermal growth factor (EGF) and anisomycin. Plays an …

**Summary**, from NCBI Gene [9252](https://www.ncbi.nlm.nih.gov/gene/9252):

> Enables ATP binding activity and protein kinase activity. Involved in several processes, including interleukin-1-mediated signaling pathway; protein phosphorylation; and regulation of DNA-templated transcription. Located in cytoplasm and nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:10434](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10434) · Entrez [9252](https://www.ncbi.nlm.nih.gov/gene/9252) · UniProt [O75582](https://www.uniprot.org/uniprotkb/O75582) · Ensembl [ENSG00000100784](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100784)

## Data

Gene col 2021: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2021); `tables/drug_effects.parquet` (53 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2021, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2021]; `tensor/DDL_lfc|DDL_z.npy` [2021]; `embed/gene_vectors.npy` [2021]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2021 or target_col == 2021). Every well: [[RPS6KA5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPS6KA5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
