---
symbol: "RANGAP1"
type: "gene"
col: 1950
ensembl_id: "ENSG00000100401"
name: "Ran GTPase activating protein 1"
location: "22q13.2"
module: 22
arm: "+"
pooled_cpm: 39.58
n_lines_expressing: 50
n_dd_up: 43
n_dd_down: 14
n_dd_up_clean: 20
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# RANGAP1

*Ran GTPase activating protein 1* — 22q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 43 drug-doses (23 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.62× (z +27.3, q 0e+00, up in 43 of 47 measured lines) ⚠ cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 1.89× (z +12.8, q 3e-35, up in 35 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.702× (z -10.1, q 3e-21, down in 34 of 48 measured lines) ⚠ cell-cycle shift, explains ~59% of this change. The strongest without an alert is [[Trametinib (drug)]] 0.5 µM: 0.809× (z -5.0, q 1e-04, down in 24 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ANAPC7]] (+0.60, fdr 1e-05), [[CCDC9B]] (+0.58, fdr 3e-05), [[RNF123]] (+0.57, fdr 1e-05); moves opposite to [[RAB1A]] (-0.64, fdr 7e-06), [[DCAF5]] (-0.56, fdr 1e-05), [[SPCS2]] (-0.56, fdr 1e-05).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[PLEKHA6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 55 in all, 30 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 43 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 23 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1950.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **2.62×** | +27.3 | 0e+00 | 43/47 (HS-578T, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **2.74×** | +18.9 | 0e+00 | 44/48 (PANC-1, NCI-H460, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **2.14×** | +15.2 | 0e+00 | 37/45 (J82, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **2.00×** | +13.0 | 3e-36 | 32/40 (Hs 766T, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.89×** | +12.8 | 3e-35 | 35/47 (HS-578T, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.89×** | +12.7 | 4e-35 | 42/48 (HS-578T, Hs 766T, …) | all doses, stronger at high dose | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.96×** | +12.7 | 4e-35 | 41/48 (LoVo, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **1.84×** | +12.2 | 2e-32 | 36/47 (KATO III, LoVo, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.84×** | +12.2 | 3e-32 | 38/48 (KATO III, HOP62, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.80×** | +11.8 | 3e-30 | 39/47 (SW480, LS 180, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.74×** | +11.1 | 1e-26 | 35/47 (C32, BT-474, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.70×** | +10.6 | 2e-24 | 35/47 (KATO III, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **1.75×** | +10.4 | 1e-23 | 29/44 (KATO III, J82, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.63×** | +9.8 | 3e-21 | 30/48 (KATO III, LoVo, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.63×** | +9.7 | 7e-21 | 41/48 (SK-MEL-2, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.54×** | +8.6 | 3e-16 | 35/48 (NCI-H460, SNU-1, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.32×** | +7.8 | 1e-13 | 35/48 (NCI-H460, HT-29, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.46×** | +7.6 | 7e-13 | 34/47 (HS-578T, NCI-H460, …) | all doses, stronger at high dose | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.45×** | +7.4 | 2e-12 | 37/47 (HT-29, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.47×** | +7.2 | 1e-11 | 32/47 (LoVo, H4, …) | all doses, stronger at high dose | position effect removed |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.60×** | +6.7 | 3e-10 | 29/48 (LoVo, KATO III, …) | all doses, flat | noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **1.50×** | +5.8 | 1e-07 | 25/48 (SK-MEL-2, HT-29, …) | all doses, stronger at high dose | low cells (technical?); noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.05 µM |  | **1.33×** | +5.3 | 2e-06 | 24/47 (SK-MEL-2, NCI-H460, …) | all doses, stronger at high dose | position effect removed |
| [[vincristine (drug)]] 5 µM |  | **1.63×** | +5.1 | 5e-06 | 21/45 (SK-MEL-2, SNU-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | **1.27×** | +4.7 | 3e-05 | 21/48 (MIA PaCa-2, NCI-H1573, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1950.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.702×** | -10.1 | 3e-21 | 34/48 (LS 180, SK-MEL-2, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.667×** | -8.2 | 9e-14 | 34/48 (C-33 A, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.809×** | -5.0 | 1e-04 | 24/48 (SK-MEL-2, HEC-1-A, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.773×** | -4.9 | 2e-04 | 23/47 (SK-MEL-2, HCT15, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.817×** | -4.6 | 5e-04 | 21/48 (SK-MEL-2, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.815×** | -4.5 | 6e-04 | 18/48 (HEC-1-A, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.840× | -4.3 | 0.001 | 20/48 (SK-MEL-2, HEC-1-A, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.809×** | -4.3 | 0.001 | 17/47 (SK-MEL-2, AsPC-1, …) | two highest doses |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **0.809×** | -4.3 | 0.001 | 17/47 (C-33 A, SW48, …) | top dose only |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.804×** | -4.2 | 0.002 | 14/48 (HEC-1-A, SK-MEL-2, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~83% of this change | **0.832×** | -3.7 | 0.010 | 10/48 (SNU-1, LS 180, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.834× | -3.7 | 0.011 | 19/48 (SK-MEL-2, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Entrectinib (drug)]] 5 µM |  | 0.835× | -3.7 | 0.011 | 14/47 (PANC-1, A-172, …) | top dose only |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.883× | -3.5 | 0.016 | 12/48 (HEC-1-A, COLO 205, …) | all doses, flat | position effect removed |
| [[Cytarabine (drug)]] 0.05 µM |  | **0.830×** | -3.5 | 0.018 | 11/47 (hTERT-HPNE, HOP62, …) | inconsistent across doses |  |
| [[venetoclax (drug)]] 5 µM |  | **0.720×** | -3.5 | 0.018 | 12/47 (SK-MEL-2, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | 0.842× | -3.3 | 0.038 | 16/47 (SK-MEL-2, C-33 A, …) | two highest doses |  |
| [[EX229 (drug)]] 5 µM |  | **0.743×** | -3.1 | 0.051 | 10/47 (A498, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib (drug)]] 5 µM |  | **0.744×** | -3.1 | 0.051 | 10/47 (A-427, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, +0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1950. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 31.9 | 8 (5 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +13.6) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 3.21× (z +10.5) | [[Selinexor (drug)]] 5 µM 0.525× (z -8.8) ⚠ cell-cycle shift, explains ~59% of this change |
| [[KATO III (line)]] | alt | 27.8 | 7 (4 ⚠) | 0 | [[Bortezomib (drug)]] 0.05 µM 4.40× (z +10.2) | — |
| [[SNU-423 (line)]] | alt | 30.7 | 6 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.34× (z +19.7) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.57× (z +8.9) | — |
| [[J82 (line)]] | alt | 45.4 | 4 (4 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.11× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | [[Selinexor (drug)]] 5 µM 0.461× (z -10.8) ⚠ cell-cycle shift, explains ~59% of this change |
| [[NCI-H1573 (line)]] | alt | 39.1 | 5 (5 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.11× (z +13.3) ⚠ cell-cycle shift, explains ~15% of this change | — |
| [[NCI-H460 (line)]] | wt | 28.1 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +14.4) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 3.08× (z +10.5) | — |
| [[A498 (line)]] | wt | 35.3 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +16.9) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.05× (z +10.5) | — |
| [[CFPAC-1 (line)]] | alt | 27.2 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.74× (z +18.9) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[Hs 766T (line)]] | wt | 38.8 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.17× (z +14.9) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[HS-578T (line)]] | alt | 34.0 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.60× (z +21.6) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.05× (z +11.3) | — |
| [[SW480 (line)]] | alt | 37.9 | 4 (3 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.25× (z +9.0) | — |
| [[A-172 (line)]] | wt | 37.6 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +12.0) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.91× (z +8.5) | — |
| [[hTERT-HPNE (line)]] | wt | 21.7 | 2 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 5.48× (z +13.5) ⚠ cell-cycle shift, explains ~30% of this change | [[Thymol (drug)]] 0.5 µM 0.205× (z -9.0) |
| [[PANC-1 (line)]] | alt | 49.1 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +16.4) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.71× (z +10.5) | — |
| [[SNU-1 (line)]] | wt | 52.0 | 2 (1 ⚠) | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 4.62× (z +9.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 4.08× (z +9.3) | [[Selinexor (drug)]] 5 µM 0.353× (z -9.8) ⚠ cell-cycle shift, explains ~59% of this change |
| [[A549 (line)]] | wt | 28.1 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.80× (z +16.8) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.04× (z +10.6) | — |
| [[BT-474 (line)]] | alt | 48.6 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +9.4) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.22× (z +8.9) | — |
| [[C32 (line)]] | wt | 28.8 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.93× (z +12.6) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Auranofin (drug)]] 5 µM 4.32× (z +9.5) | — |
| [[HOP62 (line)]] | alt | 22.0 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.44× (z +15.9) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[NCI-H1792 (line)]] | alt | 13.4 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.92× (z +14.8) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[RKO (line)]] | wt | 70.1 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +12.6) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[AsPC-1 (line)]] | alt | 26.2 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.432× (z -9.3) ⚠ cell-cycle shift, explains ~59% of this change |
| [[COLO 205 (line)]] | alt | 16.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.25× (z +8.8) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[HCT15 (line)]] | alt | 38.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +8.5) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[HEC-1-A (line)]] | alt | 59.5 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0895× (z -13.2) ⚠ toxic |
| [[HepG2_C3A (line)]] | wt | 38.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +10.3) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[LOX-IMVI (line)]] | wt | 31.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +8.5) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[LS 180 (line)]] | wt | 26.9 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.255× (z -13.8) ⚠ cell-cycle shift, explains ~59% of this change |
| [[NCI-H2030 (line)]] | alt | 57.8 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.365× (z -9.8) ⚠ toxic; cell-cycle shift, explains ~15% of this change |
| [[NCI-H2347 (line)]] | alt | 29.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +13.2) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[Panc 03.27 (line)]] | alt | 38.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +12.6) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[RPMI-7951 (line)]] | alt | 26.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.02× (z +10.8) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 190 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.499× (z -12.6) ⚠ cell-cycle shift, explains ~59% of this change |
| [[SW 900 (line)]] | alt | 19.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.80× (z +11.5) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[A-427 (line)]] | wt | 40.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 41.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 26.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 28.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 56.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 56.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 47.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 68.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 64.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1950), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANAPC7]] | +0.60 | +0.63 / +0.56 | both halves | 1e-05 | pathway: Cell Cycle Checkpoints |
| [[CCDC9B]] | +0.58 | +0.44 / +0.56 | both halves | 3e-05 |  |
| [[RNF123]] | +0.57 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[SAE1]] | +0.56 | +0.61 / +0.51 | both halves | 1e-05 | pathway: SUMOylation; STRING 940 |
| [[BMAL2]] | +0.56 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[TCHP]] | +0.56 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[KIF14]] | +0.55 | +0.51 / +0.55 | both halves | 1e-05 | pathway: RHO GTPase Effectors |
| [[MDC1]] | +0.55 | +0.50 / +0.56 | both halves | 1e-05 | pathway: Cell Cycle Checkpoints |
| [[CTPS1]] | +0.55 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[PHF19]] | +0.54 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[BICD1]] | +0.54 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[AXL]] | +0.53 | +0.37 / +0.55 | both halves | 9e-05 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAB1A]] | -0.64 | -0.68 / -0.59 | both halves | 7e-06 |  |
| [[DCAF5]] | -0.56 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[SPCS2]] | -0.56 | -0.60 / -0.52 | both halves | 1e-05 |  |
| [[MED23]] | -0.55 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[CNOT8]] | -0.54 | -0.48 / -0.56 | both halves | 2e-05 |  |
| [[SPATA7]] | -0.53 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[DPM1]] | -0.53 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[TFG]] | -0.52 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[COPS4]] | -0.52 | -0.58 / -0.42 | both halves | 4e-05 |  |
| [[ODR4]] | -0.52 | -0.43 / -0.50 | both halves | 4e-05 |  |
| [[DNAJC4]] | -0.51 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[MED6]] | -0.51 | -0.63 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLEKHA6]] | B | PLEKHA6 activity lowers RANGAP1's level | lines that do not express PLEKHA6 (16) vs lines expressing it (34) | 1.40× higher at baseline in the lines without PLEKHA6 | 0.019 | ⚠ within organs, on part of the lines; also absent: KCNK1, ELF3, TNK1; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity raises RANGAP1's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.8% of all compounds | 0.053 | ⚠ off-target possible; 3 compounds |
| [[CCL28]] | B | CCL28 activity lowers RANGAP1's level | lines that do not express CCL28 (24) vs lines expressing it (26) | 1.19× higher at baseline in the lines without CCL28 | 0.055 | ⚠ within organs, on part of the lines; also absent: SHROOM4, LINC02432, CD74 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.418). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-1.3, -29.0); signed map (-5.3, 32.2). **Vector** length 108, 31.8% of its response variance represented; |z| ≥ 3 in 1,448 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | +8.0 | +13.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | +7.6 | +15.2 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +6.1 | +9.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | +5.5 | +10.4 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | +5.4 | +8.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | +5.0 | +7.2 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +4.7 | +7.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +4.5 | +7.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.4 | +7.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.1 | +11.1 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | -7.9 | -10.1 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~64% of this change | -5.9 | -8.2 |
|  | [[EX229 (drug)]] 5 µM |  | -4.0 | -3.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.6 | -1.0 |
|  | [[venetoclax (drug)]] 5 µM |  | -3.3 | -3.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.0 | -1.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.9 | -5.0 |

## What is on record

|  |  |
|---|---|
| Name | Ran GTPase activating protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.2 — chr22:41,244,779-41,286,187 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Fug1, KIAA1835; previously SD |
| Gene groups (HGNC) | MicroRNA protein coding host genes |
| Reactome | 30 pathways, smallest: SUMOylation of nuclear envelope proteins; Postmitotic nuclear pore complex (NPC) reformation; Rev-mediated nuclear export of HIV RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [P46060](https://www.uniprot.org/uniprotkb/P46060) (Ran GTPase-activating protein 1):

> GTPase activator for RAN. Converts cytoplasmic GTP-bound RAN to GDP-bound RAN, which is essential for RAN-mediated nuclear import and export. Mediates dissociation of cargo from nuclear export complexes containing XPO1, RAN and RANBP2 after nuclear export.

**Summary**, from NCBI Gene [5905](https://www.ncbi.nlm.nih.gov/gene/5905):

> This gene encodes a protein that associates with the nuclear pore complex and participates in the regulation of nuclear transport. The encoded protein interacts with Ras-related nuclear protein 1 (RAN) and regulates guanosine triphosphate (GTP)-binding and exchange. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jul 2013]

**Accessions** — [HGNC:9854](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9854) · Entrez [5905](https://www.ncbi.nlm.nih.gov/gene/5905) · UniProt [P46060](https://www.uniprot.org/uniprotkb/P46060) · Ensembl [ENSG00000100401](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100401)

## Data

Gene col 1950: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1950); `tables/drug_effects.parquet` (77 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1950, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1950]; `tensor/DDL_lfc|DDL_z.npy` [1950]; `embed/gene_vectors.npy` [1950]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1950 or target_col == 1950). Every well: [[RANGAP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RANGAP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
