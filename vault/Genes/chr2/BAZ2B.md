---
symbol: "BAZ2B"
type: "gene"
col: 4452
ensembl_id: "ENSG00000123636"
name: "bromodomain adjacent to zinc finger domain 2B"
location: "2q24.2"
module: 77
arm: "-"
pooled_cpm: 191.08
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 35
n_dd_up_clean: 10
n_dd_down_clean: 26
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/077"]
generated_by: "tahoemap"
---

# BAZ2B

*bromodomain adjacent to zinc finger domain 2B* — 2q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.95× (z +18.3, q 0e+00, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 35 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.313× (z -22.4, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C11orf58]] (+0.80, fdr 7e-06), [[CREBBP]] (+0.76, fdr 7e-06), [[TIA1]] (+0.75, fdr 7e-06); moves opposite to [[IMPDH1]] (-0.78, fdr 7e-06), [[TAF5L]] (-0.77, fdr 1e-05), [[LPCAT1]] (-0.77, fdr 1e-05).
> It sits in the **-** arm of [[Module 077]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[RB1]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4452.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.95×** | +18.3 | 0e+00 | 44/48 (A-172, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.62×** | +9.0 | 6e-17 | 38/48 (A-172, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.48×** | +7.6 | 8e-12 | 29/48 (A-172, A498, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.43×** | +6.7 | 2e-09 | 39/47 (HEC-1-A, Hs 766T, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.41×** | +6.7 | 2e-09 | 34/48 (HT-29, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.30×** | +4.8 | 2e-04 | 34/50 (MIA PaCa-2, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.26×** | +4.6 | 4e-04 | 24/48 (HOP62, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bimiralisib (drug)]] 5 µM |  | **1.54×** | +4.4 | 8e-04 | 32/50 (HEC-1-A, AsPC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.27×** | +4.4 | 8e-04 | 32/47 (MIA PaCa-2, HOP62, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.24×** | +4.1 | 0.003 | 26/47 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | 1.17× | +3.6 | 0.016 | 20/48 (AsPC-1, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.15× | +3.6 | 0.016 | 11/48 (MIA PaCa-2, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.22×** | +3.6 | 0.017 | 24/48 (NCI-H23, MIA PaCa-2, …) | inconsistent across doses |  |
| [[RMC-6236 (drug)]] 5 µM |  | **1.40×** | +3.4 | 0.026 | 26/48 (AsPC-1, MIA PaCa-2, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | 1.13× | +3.3 | 0.035 | 16/48 (A498, HT-29, …) | top dose only | low cells (technical?) |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.13× | +3.3 | 0.037 | 8/49 (AsPC-1, MIA PaCa-2, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 1.19× | +3.2 | 0.037 | 22/48 (MIA PaCa-2, AsPC-1, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 5 µM |  | 1.18× | +3.2 | 0.046 | 23/49 (MIA PaCa-2, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 46 in all, 11 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 35 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4452.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.313×** | -22.4 | 0e+00 | 47/48 (HT-29, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.326×** | -21.7 | 0e+00 | 47/48 (SW480, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.343×** | -20.7 | 0e+00 | 46/48 (SW480, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.596×** | -10.0 | 2e-21 | 41/48 (HepG2/C3A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.603×** | -9.8 | 2e-20 | 42/48 (HepG2/C3A, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.614×** | -9.4 | 4e-19 | 40/48 (NCI-H1792, RKO, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **0.601×** | -9.1 | 9e-18 | 34/45 (SNU-1, HT-29, …) | all doses, flat | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **0.644×** | -8.2 | 2e-14 | 34/47 (RKO, NCI-H1573, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.677×** | -7.5 | 4e-12 | 35/48 (NCI-H23, MIA PaCa-2, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.688×** | -7.2 | 3e-11 | 33/48 (SW480, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change | **0.676×** | -7.0 | 1e-10 | 34/49 (A-427, COLO 205, …) | all doses, flat | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~36% of this change | **0.694×** | -6.8 | 6e-10 | 36/47 (NCI-H1792, NCI-H1573, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~80% of this change | **0.695×** | -6.8 | 6e-10 | 29/44 (NCI-H1573, KATO III, …) | all doses, flat | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.518×** | -6.6 | 1e-09 | 32/49 (PANC-1, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.573×** | -5.6 | 7e-07 | 41/48 (RKO, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **0.591×** | -5.3 | 4e-06 | 33/49 (HepG2/C3A, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.780×** | -4.8 | 6e-05 | 28/48 (SW480, C-33 A, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.642×** | -4.5 | 2e-04 | 27/48 (RKO, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.853× | -4.3 | 4e-04 | 24/49 (C32, NCI-H23, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.654×** | -4.3 | 5e-04 | 31/48 (NCI-H460, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.795×** | -4.2 | 8e-04 | 25/48 (CFPAC-1, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.42 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4452. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 289 | 5 (2 ⚠) | 9 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +16.4) | [[Panobinostat (drug)]] 0.5 µM 0.206× (z -22.8) |
| [[SW480 (line)]] | alt | 197 | 1 | 12 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +12.8) | [[Panobinostat (drug)]] 5 µM 0.157× (z -25.3) |
| [[HepG2_C3A (line)]] | wt | 298 | 2 | 10 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +13.8) | [[Panobinostat (drug)]] 5 µM 0.169× (z -24.2) |
| [[HOP62 (line)]] | alt | 149 | 8 (3 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +20.8) | [[Panobinostat (drug)]] 0.5 µM 0.286× (z -16.8) |
| [[AsPC-1 (line)]] | alt | 231 | 2 | 7 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +15.1) | [[Panobinostat (drug)]] 0.5 µM 0.177× (z -20.4) |
| [[LS 180 (line)]] | wt | 482 | 1 | 8 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.59× (z +8.9) | [[Panobinostat (drug)]] 0.5 µM 0.191× (z -22.8) |
| [[MIA PaCa-2 (line)]] | alt | 180 | 4 (1 ⚠) | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +18.4) | [[Belinostat (drug)]] 5 µM 0.312× (z -13.9) |
| [[NCI-H1792 (line)]] | alt | 171 | 0 | 9 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.179× (z -18.9) |
| [[NCI-H1573 (line)]] | alt | 217 | 0 | 8 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.188× (z -23.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~80% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.279× (z -18.8) |
| [[Panc 03.27 (line)]] | alt | 249 | 2 | 6 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +10.7) | [[Panobinostat (drug)]] 0.5 µM 0.195× (z -20.9) |
| [[RKO (line)]] | wt | 199 | 3 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +17.9) | [[Panobinostat (drug)]] 5 µM 0.193× (z -19.9) |
| [[SW1417 (line)]] | alt | 251 | 2 | 6 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +12.6) | [[Panobinostat (drug)]] 0.5 µM 0.253× (z -18.9) |
| [[COLO 205 (line)]] | alt | 294 | 1 | 6 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.75× (z +10.2) | [[Panobinostat (drug)]] 0.5 µM 0.175× (z -22.5) |
| [[PANC-1 (line)]] | alt | 218 | 1 | 6 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.77× (z +11.5) | [[Panobinostat (drug)]] 0.5 µM 0.350× (z -14.9) |
| [[SNU-423 (line)]] | alt | 162 | 1 | 6 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +10.1) | [[Belinostat (drug)]] 5 µM 0.238× (z -16.7) |
| [[A-427 (line)]] | wt | 135 | 2 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +20.1) | [[Dinaciclib (drug)]] 0.5 µM 0.0413× (z -37.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.359× (z -13.0) |
| [[A498 (line)]] | wt | 137 | 5 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +19.8) | [[Panobinostat (drug)]] 0.5 µM 0.500× (z -8.8) |
| [[BT-474 (line)]] | alt | 224 | 2 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +18.3) | [[Panobinostat (drug)]] 0.5 µM 0.313× (z -13.6) |
| [[hTERT-HPNE (line)]] | wt | 115 | 3 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +16.7) | [[Panobinostat (drug)]] 5 µM 0.373× (z -10.0) |
| [[NCI-H23 (line)]] | alt | 197 | 1 | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +18.6) | [[Auranofin (drug)]] 5 µM 0.394× (z -12.8) |
| [[NCI-H2347 (line)]] | alt | 164 | 3 | 3 | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +18.2) | [[Panobinostat (drug)]] 0.5 µM 0.278× (z -15.0) |
| [[SW 900 (line)]] | alt | 265 | 2 | 4 | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +10.4) | [[Panobinostat (drug)]] 5 µM 0.223× (z -17.5) |
| [[A-172 (line)]] | wt | 137 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.06× (z +27.2) | — |
| [[CFPAC-1 (line)]] | alt | 163 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.263× (z -15.9) |
| [[Hs 766T (line)]] | wt | 92.4 | 1 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +10.4) | [[Belinostat (drug)]] 5 µM 0.351× (z -10.2) |
| [[J82 (line)]] | alt | 85.0 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.31× (z +27.0) | — |
| [[KATO III (line)]] | alt | 130 | 1 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +11.6) | [[Panobinostat (drug)]] 5 µM 0.326× (z -13.9) |
| [[NCI-H460 (line)]] | wt | 241 | 1 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +12.1) | [[Panobinostat (drug)]] 5 µM 0.255× (z -16.6) |
| [[SK-MEL-2 (line)]] | alt | 134 | 1 | 4 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +12.6) | [[Panobinostat (drug)]] 0.5 µM 0.258× (z -15.7) |
| [[SNU-1 (line)]] | wt | 148 | 1 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +9.9) | [[Dinaciclib (drug)]] 0.05 µM 0.237× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.324× (z -10.3) |
| [[A549 (line)]] | wt | 194 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.288× (z -12.9) |
| [[C-33 A (line)]] | alt | 261 | 1 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.75× (z +9.1) | [[Dinaciclib (drug)]] 0.5 µM 0.407× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.466× (z -8.6) |
| [[C32 (line)]] | wt | 182 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.322× (z -11.1) |
| [[CHP-212 (line)]] | wt | 338 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.108× (z -18.6) |
| [[HCT15 (line)]] | alt | 231 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +14.0) | [[Panobinostat (drug)]] 5 µM 0.246× (z -15.2) |
| [[NCI-H2030 (line)]] | alt | 287 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.264× (z -12.2) |
| [[RPMI-7951 (line)]] | alt | 178 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +14.6) | [[Panobinostat (drug)]] 0.5 µM 0.376× (z -10.8) |
| [[SW48 (line)]] | wt | 163 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.35× (z +14.3) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.336× (z -9.3) ⚠ unreliable plate only · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.338× (z -9.2) |
| [[AN3 CA (line)]] | alt | 281 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.224× (z -11.4) |
| [[HEC-1-A (line)]] | alt | 162 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 1.71× (z +10.0) | [[Panobinostat (drug)]] 0.5 µM 0.455× (z -10.4) |
| [[LoVo (line)]] | wt | 127 | 1 | 2 | [[Harringtonine (drug)]] 5 µM 2.79× (z +14.5) | [[Panobinostat (drug)]] 5 µM 0.512× (z -9.9) |
| [[LOX-IMVI (line)]] | wt | 160 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.284× (z -16.1) |
| [[SHP-77 (line)]] | alt | 97.5 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.323× (z -13.2) |
| [[HS-578T (line)]] | alt | 76.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +15.9) | — |
| [[H4 (line)]] | wt | 145 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 230 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 202 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 220 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 219 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4452), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*56 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C11orf58]] | +0.80 | +0.80 / +0.60 | both halves | 7e-06 |  |
| [[CREBBP]] | +0.76 | +0.70 / +0.61 | both halves | 7e-06 | same gene group; STRING 473 |
| [[TIA1]] | +0.75 | +0.75 / +0.59 | both halves | 7e-06 |  |
| [[MED13]] | +0.73 | +0.58 / +0.69 | both halves | 8e-06 |  |
| [[WAC-AS1]] | +0.72 | +0.69 / +0.47 | both halves | 2e-05 |  |
| [[PATL2]] | +0.71 | +0.70 / +0.38 | both halves | 6e-05 |  |
| [[GGPS1]] | +0.71 | +0.65 / +0.52 | both halves | 1e-05 |  |
| [[TAPBPL]] | +0.70 | +0.65 / +0.46 | both halves | 2e-05 |  |
| [[RIPK2-DT]] | +0.70 | +0.67 / +0.49 | both halves | 1e-05 |  |
| [[EP300]] | +0.69 | +0.44 / +0.63 | both halves | 3e-05 | same gene group |
| [[ZBED5]] | +0.69 | +0.66 / +0.42 | both halves | 4e-05 |  |
| [[ATRX]] | +0.69 | +0.72 / +0.59 | both halves | 7e-06 | STRING 629 |

## Genes that move opposite

*44 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IMPDH1]] | -0.78 | -0.80 / -0.60 | both halves | 7e-06 |  |
| [[TAF5L]] | -0.77 | -0.78 / -0.57 | both halves | 1e-05 |  |
| [[LPCAT1]] | -0.77 | -0.73 / -0.57 | both halves | 1e-05 |  |
| [[RNF216P1]] | -0.76 | -0.74 / -0.54 | both halves | 1e-05 |  |
| [[WASF3]] | -0.75 | -0.68 / -0.54 | both halves | 1e-05 |  |
| [[TMEM120B]] | -0.75 | -0.67 / -0.62 | both halves | 7e-06 |  |
| [[ANKRD27]] | -0.74 | -0.72 / -0.52 | both halves | 1e-05 |  |
| [[ST6GALNAC6]] | -0.71 | -0.68 / -0.48 | both halves | 2e-05 |  |
| [[EIF4EBP1]] | -0.70 | -0.71 / -0.44 | both halves | 3e-05 |  |
| [[RBAK-RBAKDN]] | -0.69 | -0.72 / -0.50 | both halves | 1e-05 |  |
| [[GTPBP3]] | -0.69 | -0.67 / -0.38 | both halves | 6e-05 |  |
| [[ST6GALNAC4]] | -0.69 | -0.60 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RB1]] | C | the direction of RB1's effect on BAZ2B's drug response is not inferred (the mechanism is not recorded) | recorded alteration (mechanism not recorded) of RB1 in 3 lines vs 45 not recorded | the RB1-altered lines respond 0.52× as strongly (z diff +3.33); strongest at Panobinostat 0.05 µM: 1.04x vs 0.59x (z diff +6.5) | 0.040 | ⚠ few lines (4 vs 46); tissue-confounded; across organs; mechanism partly not recorded; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 077]]; 59 genes; this gene is in the **-** arm (projection on the module's main direction -0.840). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.44).
- **Nodal map** (x, y) = (-1.4, 0.7); signed map (21.5, -17.3). **Vector** length 148, 58.2% of its response variance represented; |z| ≥ 3 in 1,807 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +14.4 | +18.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | +13.9 | +9.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +10.2 | +7.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +9.0 | +6.7 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +7.5 | +1.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.7 | +3.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +5.9 | +6.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.9 | +0.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +4.4 | +3.6 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +4.2 | +4.4 |
| fall | [[Belinostat (drug)]] 5 µM |  | -10.0 | -20.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | -9.2 | -21.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -9.0 | -22.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.8 | -9.4 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -6.6 | -9.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -5.3 | -4.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.9 | -4.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -4.4 | -4.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -4.2 | -5.6 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -4.1 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | bromodomain adjacent to zinc finger domain 2B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q24.2 — chr2:159,318,979-159,616,569 (-) |
| Ensembl biotype | protein_coding |
| Also known as | WALp4 |
| Gene groups (HGNC) | PHD finger proteins; Methyl-CpG binding domain containing; Bromodomain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UIF8](https://www.uniprot.org/uniprotkb/Q9UIF8) (Bromodomain adjacent to zinc finger domain protein 2B):

> Regulatory subunit of the ATP-dependent BRF-1 and BRF-5 ISWI chromatin remodeling complexes, which form ordered nucleosome arrays on chromatin and facilitate access to DNA during DNA-templated processes such as DNA replication, transcription, and repair. Both complexes regulate the spacing of nucleosomes along the chromatin and have the ability to slide mononucleosomes to the center of a DNA template. The BRF-1 ISWI chromatin remodeling complex has a lower ATP hydrolysis rate than the BRF-5 …

**Summary**, from NCBI Gene [29994](https://www.ncbi.nlm.nih.gov/gene/29994):

> This gene belongs to the bromodomain gene family. Members of this gene family encode proteins that are integral components of chromatin remodeling complexes. The encoded protein showed strong preference for the activating H3K14Ac mark in a histone peptide screen, suggesting a potential role in transcriptional activation. This gene may be associated with susceptibility to sudden cardiac death (SCD). [provided by RefSeq, Aug 2016]

**Accessions** — [HGNC:963](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:963) · Entrez [29994](https://www.ncbi.nlm.nih.gov/gene/29994) · UniProt [Q9UIF8](https://www.uniprot.org/uniprotkb/Q9UIF8) · Ensembl [ENSG00000123636](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000123636)

## Data

Gene col 4452: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4452); `tables/drug_effects.parquet` (67 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4452, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4452]; `tensor/DDL_lfc|DDL_z.npy` [4452]; `embed/gene_vectors.npy` [4452]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4452 or target_col == 4452). Every well: [[BAZ2B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BAZ2B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
