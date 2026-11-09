---
symbol: "PROS1"
type: "gene"
col: 11546
ensembl_id: "ENSG00000184500"
name: "protein S"
location: "3q11.1"
module: 139
arm: "+"
pooled_cpm: 43.38
n_lines_expressing: 44
n_dd_up: 15
n_dd_down: 43
n_dd_up_clean: 14
n_dd_down_clean: 27
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/139"]
generated_by: "tahoemap"
---

# PROS1

*protein S* — 3q11.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.40× (z +6.8, q 5e-09, up in 32 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 43 drug-doses (16 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.454× (z -15.7, q 0e+00, down in 31 of 42 measured lines) ⚠ cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.433× (z -11.8, q 1e-29, down in 30 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ABCB7]] (+0.58, fdr 1e-05), [[STOM]] (+0.55, fdr 3e-05), [[RHOBTB3]] (+0.53, fdr 1e-05); moves opposite to [[SMIM12]] (-0.52, fdr 9e-05), [[LINC00310]] (-0.51, fdr 2e-05), [[CCM2]] (-0.47, fdr 3e-05).
> It is in [[Module 139]], a single-armed module (Interleukin-4 and Interleukin-13 signaling).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MAP2K1]] → it (grade B ⚠); 1 goes from it, the strongest it → [[SLC5A4-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11546.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.40×** | +6.8 | 5e-09 | 32/42 (A498, LoVo, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.50×** | +5.8 | 2e-06 | 32/42 (LS 180, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.46×** | +5.4 | 1e-05 | 26/41 (PANC-1, A549, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.39×** | +4.5 | 8e-04 | 24/41 (A-427, HEC-1-A, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.33×** | +4.1 | 0.006 | 21/41 (PANC-1, A549, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.30×** | +3.6 | 0.029 | 19/41 (A498, SW 900, …) | inconsistent across doses |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **1.28×** | +3.5 | 0.036 | 12/42 (A549, A498, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.20×** | +3.4 | 0.050 | 14/42 (LS 180, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.26×** | +3.3 | 0.050 | 19/41 (HEC-1-A, MIA PaCa-2, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.18× | +3.3 | 0.050 | 17/42 (NCI-H2030, SHP-77, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 5 µM |  | **1.26×** | +3.3 | 0.050 | 16/42 (A498, PANC-1, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.26×** | +3.3 | 0.050 | 15/42 (NCI-H2347, LS 180, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.26×** | +3.2 | 0.052 | 15/42 (HEC-1-A, A-172, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 1.20× | +3.2 | 0.063 | 14/42 (LS 180, HEC-1-A, …) | all doses, flat | noisy plate (z scaled) |
| [[Dexamethasone (drug)]] 0.05 µM |  | **1.24×** | +3.1 | 0.078 | 15/42 (PANC-1, A549, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **1.24×** | +3.1 | 0.078 | 13/42 (A549, PANC-1, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 44 in all, 17 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 43 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11546.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.454×** | -15.7 | 0e+00 | 31/42 (SHP-77, HepG2/C3A, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.433×** | -11.8 | 1e-29 | 30/42 (COLO 205, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.452×** | -10.8 | 7e-25 | 33/42 (COLO 205, A549, …) | rises with dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.505×** | -9.6 | 7e-20 | 34/42 (SW480, HT-29, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.552×** | -8.4 | 6e-15 | 31/42 (COLO 205, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **0.557×** | -7.9 | 2e-13 | 30/40 (A549, SW480, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **0.580×** | -7.7 | 1e-12 | 30/41 (SW480, COLO 205, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.682×** | -7.6 | 2e-12 | 27/42 (HT-29, NCI-H23, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.610×** | -7.0 | 2e-10 | 25/41 (SW480, A-427, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.630×** | -6.5 | 4e-09 | 29/42 (H4, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.645×** | -6.2 | 4e-08 | 28/42 (SW480, COLO 205, …) | all doses, stronger at high dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.656×** | -5.9 | 1e-07 | 26/42 (HT-29, C-33 A, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.661×** | -5.8 | 3e-07 | 25/42 (SW480, COLO 205, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.657×** | -5.7 | 6e-07 | 28/41 (SK-MEL-2, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.672×** | -5.6 | 9e-07 | 25/42 (SW480, COLO 205, …) | rises with dose |  |
| [[Tofacitinib (drug)]] 5 µM |  | **0.756×** | -5.5 | 1e-06 | 27/42 (SHP-77, SK-MEL-2, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.669×** | -5.4 | 2e-06 | 26/42 (NCI-H23, A-427, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.682×** | -5.4 | 2e-06 | 24/41 (SW480, CFPAC-1, …) | two highest doses |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.770×** | -5.2 | 6e-06 | 27/42 (SHP-77, SK-MEL-2, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.503×** | -5.1 | 1e-05 | 27/43 (RKO, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~25% here); composition shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.704×** | -4.9 | 2e-05 | 24/41 (NCI-H23, HT-29, …) | all doses, flat |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.785×** | -4.8 | 4e-05 | 24/42 (SHP-77, CFPAC-1, …) | two highest doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.571×** | -4.1 | 8e-04 | 22/42 (COLO 205, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.746×** | -4.1 | 9e-04 | 22/42 (SK-MEL-2, J82, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.738×** | -4.1 | 9e-04 | 21/42 (MIA PaCa-2, NCI-H23, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, -0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11546. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 47.5 | 0 | 15 (12 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.188× (z -14.7) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.214× (z -13.5) |
| [[COLO 205 (line)]] | alt | 108 | 0 | 11 (9 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.133× (z -16.8) |
| [[SHP-77 (line)]] | alt | 86.5 | 0 | 8 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.142× (z -27.0) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.282× (z -12.4) |
| [[HT-29 (line)]] | alt | 85.2 | 0 | 6 (4 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.205× (z -13.5) |
| [[LOX-IMVI (line)]] | wt | 39.7 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -15.6) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.283× (z -8.8) |
| [[NCI-H460 (line)]] | wt | 34.6 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -16.5) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.268× (z -10.9) |
| [[A-427 (line)]] | wt | 71.9 | 2 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +10.4) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.79× (z +9.8) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.293× (z -11.3) |
| [[A549 (line)]] | wt | 36.0 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -14.2) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.153× (z -12.6) |
| [[HCT15 (line)]] | alt | 81.2 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.229× (z -15.8) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.214× (z -11.7) |
| [[NCI-H1573 (line)]] | alt | 43.0 | 0 | 4 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.237× (z -9.9) ⚠ cell-cycle shift, explains ~32% of this change |
| [[NCI-H23 (line)]] | alt | 70.6 | 0 | 4 (2 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.230× (z -11.5) |
| [[RKO (line)]] | wt | 114 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.114× (z -18.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.310× (z -10.5) |
| [[SNU-1 (line)]] | wt | 71.6 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.121× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.305× (z -11.7) |
| [[AN3 CA (line)]] | alt | 79.6 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.150× (z -14.0) ⚠ cell-cycle shift, explains ~33% of this change |
| [[LoVo (line)]] | wt | 24.1 | 1 | 2 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.51× (z +9.4) | [[Homoharringtonine (drug)]] 5 µM 0.430× (z -8.6) ⚠ cell-cycle shift, explains ~33% of this change |
| [[CFPAC-1 (line)]] | alt | 46.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -15.4) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.134× (z -13.9) |
| [[CHP-212 (line)]] | wt | 50.6 | 0 | 2 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.0628× (z -10.5) |
| [[J82 (line)]] | alt | 72.6 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.495× (z -8.8) |
| [[NCI-H2030 (line)]] | alt | 40.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -15.4) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.234× (z -10.1) |
| [[Panc 03.27 (line)]] | alt | 20.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.106× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[PANC-1 (line)]] | alt | 24.4 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.99× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.288× (z -15.1) ⚠ cell-cycle shift, explains ~33% of this change |
| [[SK-MEL-2 (line)]] | alt | 120 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.353× (z -13.5) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.362× (z -9.0) |
| [[A498 (line)]] | wt | 29.6 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.41× (z +10.1) | — |
| [[C-33 A (line)]] | alt | 74.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.474× (z -8.5) ⚠ cell-cycle shift, explains ~33% of this change |
| [[C32 (line)]] | wt | 41.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.374× (z -9.3) ⚠ cell-cycle shift, explains ~33% of this change |
| [[H4 (line)]] | wt | 13.3 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.0478× (z -11.3) |
| [[HEC-1-A (line)]] | alt | 111 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.554× (z -9.6) ⚠ cell-cycle shift, explains ~33% of this change |
| [[HepG2_C3A (line)]] | wt | 70.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.197× (z -16.6) ⚠ cell-cycle shift, explains ~33% of this change |
| [[LS 180 (line)]] | wt | 35.9 | 1 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 2.29× (z +9.3) ⚠ cell-cycle shift, would explain all of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 19.1 | 0 | 1 | — | [[Belumosudil (drug)]] 5 µM 0.101× (z -11.4) |
| [[NCI-H1792 (line)]] | alt | 11.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.161× (z -9.0) |
| [[RPMI-7951 (line)]] | alt | 22.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.204× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[SW 900 (line)]] | alt | 48.6 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.330× (z -8.5) ⚠ cell-cycle shift, explains ~32% of this change |
| [[A-172 (line)]] | wt | 49.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.8 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.73 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 6.83 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 24.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.29 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.63 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 54.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 46.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 283 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 60.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.67 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11546), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABCB7]] | +0.58 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[STOM]] | +0.55 | +0.43 / +0.58 | both halves | 3e-05 |  |
| [[RHOBTB3]] | +0.53 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[SLC5A4-AS1]] | +0.52 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[CSRNP3]] | +0.52 | +0.41 / +0.47 | both halves | 4e-05 |  |
| [[SOAT1]] | +0.52 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[ALDH5A1]] | +0.52 | +0.42 / +0.49 | both halves | 4e-05 |  |
| [[CERS6]] | +0.50 | +0.43 / +0.51 | both halves | 3e-05 |  |
| [[SAA2]] | +0.50 | +0.46 / +0.51 | both halves | 3e-05 |  |
| [[QPRT]] | +0.50 | +0.53 / +0.43 | both halves | 3e-05 |  |
| [[WDR17]] | +0.49 | +0.35 / +0.52 | both halves | 1e-04 |  |
| [[FIGN]] | +0.49 | +0.57 / +0.36 | both halves | 1e-04 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMIM12]] | -0.52 | -0.36 / -0.46 | both halves | 9e-05 |  |
| [[LINC00310]] | -0.51 | -0.48 / -0.57 | both halves | 2e-05 |  |
| [[CCM2]] | -0.47 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[ANKMY1]] | -0.46 | -0.36 / -0.52 | both halves | 1e-04 |  |
| [[DPP9]] | -0.45 | -0.49 / -0.42 | both halves | 4e-05 |  |
| [[TMCO3]] | -0.45 | -0.35 / -0.47 | both halves | 1e-04 |  |
| [[CRYGS]] | -0.43 | -0.37 / -0.29 | both halves | 2e-04 |  |
| [[FAM131A]] | -0.43 | -0.39 / -0.28 | both halves | 3e-04 |  |
| [[GOLGA3]] | -0.42 | -0.48 / -0.36 | both halves | 9e-05 |  |
| [[MRPS6]] | -0.42 | -0.34 / -0.53 | both halves | 1e-04 |  |
| [[PRPSAP1]] | -0.42 | -0.30 / -0.40 | both halves | 2e-04 |  |
| [[ZNF778]] | -0.42 | -0.31 / -0.29 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers PROS1's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.2% of all compounds | 0.037 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC5A4-AS1]] | B | PROS1 activity raises SLC5A4-AS1's level | lines that do not express PROS1 (6) vs lines expressing it (44) | 2.52× lower at baseline in the lines without PROS1 | 0.042 | ⚠ within organs, on part of the lines; also absent: WDR35, AGK, ERO1B |

## Where it sits

- **Module**: [[Module 139]] — Interleukin-4 and Interleukin-13 signaling; 34 genes; every member is in the + arm (projection on the module's main direction 0.500). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (22.5, 16.9); signed map (43.1, -9.3). **Vector** length 97.9, 26.7% of its response variance represented; |z| ≥ 3 in 1,295 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.1 | +6.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.1 | +5.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +4.5 | -2.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.1 | -0.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.9 | +4.5 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +3.4 | +4.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.8 | +3.3 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +2.8 | +5.4 |
| fall | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | -3.8 | -2.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.7 | -3.4 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -3.4 | -5.9 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.9 | -2.7 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | -2.8 | -3.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.8 | -4.8 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -2.6 | -5.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.4 | -5.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.4 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | protein S |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q11.1 — chr3:93,873,051-93,980,003 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously PROS |
| Gene groups (HGNC) | Gla domain containing |
| Hallmark sets | COAGULATION, XENOBIOTIC_METABOLISM |
| Reactome | 22 pathways, smallest: Transport of gamma-carboxylated protein precursors from the endoplasmic reticulum to the Golgi apparatus; Gamma-carboxylation of protein precursors; Removal of aminoterminal propeptides from gamma-carboxylated proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [P07225](https://www.uniprot.org/uniprotkb/P07225) (Vitamin K-dependent protein S):

> Anticoagulant plasma protein which directly binds coagulation factors Va (F5) and Xa (F10) and inhibits their activity. Acts independently of activated protein C. Also acts as a ligand for tyrosine-protein kinase receptors AXL and TYRO3, whose signaling is implicated in cell growth and survival, cell adhesion and cell migration.

**Summary**, from NCBI Gene [5627](https://www.ncbi.nlm.nih.gov/gene/5627):

> This gene encodes a vitamin K-dependent plasma protein that functions as a cofactor for the anticoagulant protease, activated protein C (APC) to inhibit blood coagulation. It is found in plasma in both a free, functionally active form and also in an inactive form complexed with C4b-binding protein. Mutations in this gene result in autosomal dominant hereditary thrombophilia. An inactive pseudogene of this locus is located at an adjacent region on chromosome 3. Alternative splicing results in …

**Accessions** — [HGNC:9456](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9456) · Entrez [5627](https://www.ncbi.nlm.nih.gov/gene/5627) · UniProt [P07225](https://www.uniprot.org/uniprotkb/P07225) · Ensembl [ENSG00000184500](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184500)

## Data

Gene col 11546: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11546); `tables/drug_effects.parquet` (61 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11546, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11546]; `tensor/DDL_lfc|DDL_z.npy` [11546]; `embed/gene_vectors.npy` [11546]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11546 or target_col == 11546). Every well: [[PROS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PROS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
