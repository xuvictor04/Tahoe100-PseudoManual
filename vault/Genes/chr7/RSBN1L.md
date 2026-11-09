---
symbol: "RSBN1L"
type: "gene"
col: 11906
ensembl_id: "ENSG00000187257"
name: "round spermatid basic protein 1 like"
location: "7q11.23"
module: 145
arm: "+"
pooled_cpm: 102.75
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 15
n_dd_up_clean: 8
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/145"]
generated_by: "tahoemap"
---

# RSBN1L

*round spermatid basic protein 1 like* — 7q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.72× (z +15.0, q 0e+00, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.510× (z -18.1, q 0e+00, down in 38 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-733 (drug)]] 5 µM: 0.545× (z -8.8, q 1e-16, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TNRC6B]] (+0.63, fdr 1e-05), [[PDS5B]] (+0.63, fdr 1e-05), [[CNOT6L]] (+0.61, fdr 1e-05); moves opposite to [[CDC37]] (-0.56, fdr 1e-05), [[EIF3I]] (-0.55, fdr 2e-05), [[SOWAHC]] (-0.55, fdr 1e-05).
> It is in [[Module 145]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HOXA5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11906.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.72×** | +15.0 | 0e+00 | 41/48 (LS 180, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.71×** | +15.0 | 0e+00 | 41/48 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.24×** | +11.7 | 2e-29 | 33/49 (SW480, KATO III, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.20×** | +11.5 | 2e-28 | 44/48 (SW480, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.47×** | +10.3 | 1e-22 | 32/47 (SK-MEL-2, COLO 205, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.40×** | +9.3 | 2e-18 | 35/48 (SW480, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.39×** | +9.1 | 6e-18 | 36/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.30×** | +7.0 | 1e-10 | 28/48 (SW480, HEC-1-A, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.29×** | +6.7 | 1e-09 | 27/47 (BT-474, SW48, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.22×** | +5.5 | 3e-06 | 25/48 (A498, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | **1.21×** | +5.2 | 1e-05 | 24/48 (A-427, MIA PaCa-2, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 1.13× | +4.8 | 7e-05 | 11/48 (LoVo, SK-MEL-2, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | 1.17× | +4.3 | 6e-04 | 21/48 (HEC-1-A, SNU-1, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.16× | +4.1 | 0.002 | 17/48 (A498, RKO, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.22×** | +3.9 | 0.004 | 18/49 (RKO, A498, …) | all doses, flat | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | 1.15× | +3.8 | 0.006 | 14/48 (NCI-H2347, NCI-H2030, …) | rises with dose |  |
| [[Verteporfin (drug)]] 5 µM |  | 1.12× | +3.1 | 0.061 | 7/49 (A-427, HepG2/C3A, …) | top dose only |  |
| [[crizotinib (drug)]] 5 µM |  | 1.12× | +2.9 | 0.096 | 7/48 (C32, COLO 205, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11906.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.510×** | -18.1 | 0e+00 | 38/44 (A498, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.567×** | -15.8 | 0e+00 | 39/49 (A498, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.672×** | -10.3 | 2e-22 | 34/45 (A498, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.665×** | -9.3 | 2e-18 | 44/48 (KATO III, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.545×** | -8.8 | 1e-16 | 44/48 (KATO III, COLO 205, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.612×** | -7.2 | 8e-11 | 35/48 (A498, PANC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.620×** | -7.0 | 3e-10 | 34/48 (KATO III, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.635×** | -6.6 | 3e-09 | 29/48 (SW 1271, KATO III, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **0.639×** | -6.5 | 4e-09 | 34/47 (AsPC-1, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | 0.859× | -6.0 | 1e-07 | 16/48 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **0.833×** | -5.1 | 2e-05 | 22/48 (KATO III, HT-29, …) | top dose only |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.792×** | -4.7 | 1e-04 | 21/48 (KATO III, Hs 766T, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **0.805×** | -4.3 | 6e-04 | 20/49 (NCI-H1792, COLO 205, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.817×** | -4.0 | 0.002 | 14/48 (KATO III, HT-29, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.869× | -3.9 | 0.003 | 16/47 (RKO, SK-MEL-2, …) | inconsistent across doses | low cells (technical?) |
| [[venetoclax (drug)]] 5 µM |  | **0.779×** | -3.6 | 0.009 | 21/48 (PANC-1, SW48, …) | top dose only | noisy plate (z scaled) |
| [[Pexidartinib (hydrochloride) (drug)]] 5 µM |  | 0.887× | -3.2 | 0.036 | 8/48 (A-427, SNU-423, …) | rises with dose |  |
| [[EX229 (drug)]] 0.05 µM |  | 0.890× | -3.1 | 0.056 | 14/48 (NCI-H661, RKO, …) | all doses, stronger at high dose |  |
| [[Infigratinib (drug)]] 0.05 µM |  | 0.891× | -3.1 | 0.058 | 5/48 (SW1417, LoVo, …) | inconsistent across doses |  |
| [[Olanzapine (drug)]] 5 µM |  | 0.927× | -3.0 | 0.062 | 0/48 | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11906. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 177 | 6 (2 ⚠) | 6 (4 ⚠) | [[Digitoxin (drug)]] 5 µM 2.58× (z +15.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.49× (z +14.4) | [[Dinaciclib (drug)]] 5 µM 0.296× (z -18.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.494× (z -11.2) |
| [[SW480 (line)]] | alt | 113 | 7 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.26× (z +15.2) | [[Dinaciclib (drug)]] 5 µM 0.512× (z -11.9) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 126 | 5 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.10× (z +16.5) | [[Dinaciclib (drug)]] 5 µM 0.360× (z -11.6) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 134 | 3 (1 ⚠) | 3 (3 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 1.99× (z +11.5) | [[Dinaciclib (drug)]] 0.5 µM 0.260× (z -22.6) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 172 | 1 | 5 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 4.50× (z +10.8) | [[Dinaciclib (drug)]] 0.05 µM 0.301× (z -15.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.530× (z -8.6) |
| [[PANC-1 (line)]] | alt | 81.3 | 5 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.41× (z +15.9) | [[Dinaciclib (drug)]] 0.5 µM 0.478× (z -13.2) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 74.8 | 5 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.44× (z +12.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.34× (z +12.3) | — |
| [[HEC-1-A (line)]] | alt | 158 | 4 (4 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +16.0) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 5 µM 0.516× (z -8.8) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 117 | 3 (2 ⚠) | 2 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 2.02× (z +11.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.93× (z +10.3) | [[Selinexor (drug)]] 5 µM 0.628× (z -10.3) ⚠ cell-cycle shift, explains ~27% of this change |
| [[NCI-H1573 (line)]] | alt | 119 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.310× (z -16.2) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 114 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.303× (z -16.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.540× (z -8.5) |
| [[SK-MEL-2 (line)]] | alt | 106 | 3 (1 ⚠) | 2 (2 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.43× (z +11.6) ⚠ toxic · without an alert: [[PH-797804 (drug)]] 5 µM 3.89× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.240× (z -19.3) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 163 | 1 | 4 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.95× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.344× (z -14.9) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 93.8 | 3 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.15× (z +10.7) | [[Dinaciclib (drug)]] 0.5 µM 0.471× (z -10.6) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 104 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +9.4) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.23× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.372× (z -10.2) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 107 | 1 | 2 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 8.07× (z +11.0) | [[Dinaciclib (drug)]] 0.5 µM 0.314× (z -11.7) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 95.3 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.268× (z -15.4) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 99.9 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.35× (z +10.1) | [[Dinaciclib (drug)]] 0.5 µM 0.462× (z -9.1) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 146 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.68× (z +10.3) | [[Dinaciclib (drug)]] 5 µM 0.406× (z -9.6) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 83.2 | 2 (1 ⚠) | 0 | [[PH-797804 (drug)]] 5 µM 3.68× (z +9.0) | — |
| [[AsPC-1 (line)]] | alt | 126 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.263× (z -15.3) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 84.7 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.91× (z +10.9) | [[Niclosamide (olamine) (drug)]] 5 µM 0.384× (z -10.0) ⚠ toxic |
| [[COLO 205 (line)]] | alt | 118 | 2 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.83× (z +11.1) ⚠ toxic · without an alert: [[TAK-901 (drug)]] 5 µM 5.08× (z +9.4) | — |
| [[HepG2_C3A (line)]] | wt | 110 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.305× (z -11.2) ⚠ toxic; cell-cycle shift, explains ~1% of this change |
| [[HOP62 (line)]] | alt | 56.0 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.36× (z +9.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.15× (z +8.6) | — |
| [[NCI-H661 (line)]] | alt | 134 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.119× (z -11.4) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 108 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.484× (z -9.6) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 101 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.463× (z -10.1) ⚠ cell-cycle shift, explains ~17% of this change |
| [[A-172 (line)]] | wt | 92.6 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.08× (z +9.6) ⚠ toxic | — |
| [[A549 (line)]] | wt | 68.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.375× (z -10.7) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 78.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.188× (z -17.9) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 79.8 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.17× (z +8.7) | — |
| [[LOX-IMVI (line)]] | wt | 93.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.346× (z -11.7) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 122 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.413× (z -10.7) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 98.8 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.46× (z +9.9) ⚠ toxic | — |
| [[NCI-H23 (line)]] | alt | 87.7 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.18× (z +9.1) | — |
| [[NCI-H460 (line)]] | wt | 77.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.626× (z -10.4) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H596 (line)]] | alt | 106 | 1 | 0 | [[Oxaprozin (drug)]] 5 µM 3.51× (z +9.8) | — |
| [[RPMI-7951 (line)]] | alt | 77.3 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.52× (z +9.0) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 177 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 50.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 104 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 85.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 59.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 75.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 120 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 65.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 77.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 90.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11906), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TNRC6B]] | +0.63 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[PDS5B]] | +0.63 | +0.64 / +0.57 | both halves | 1e-05 |  |
| [[CNOT6L]] | +0.61 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[ZNRF2]] | +0.60 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[PHIP]] | +0.60 | +0.47 / +0.66 | both halves | 2e-05 |  |
| [[AMBRA1]] | +0.60 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[HOXB5]] | +0.59 | +0.68 / +0.47 | both halves | 2e-05 |  |
| [[HOXB6]] | +0.58 | +0.68 / +0.47 | both halves | 2e-05 |  |
| [[TNRC6A]] | +0.58 | +0.66 / +0.51 | both halves | 1e-05 |  |
| [[FBXO9]] | +0.58 | +0.62 / +0.51 | both halves | 1e-05 |  |
| [[PAPOLG]] | +0.58 | +0.46 / +0.63 | both halves | 3e-05 |  |
| [[PPM1B]] | +0.57 | +0.54 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDC37]] | -0.56 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[EIF3I]] | -0.55 | -0.48 / -0.58 | both halves | 2e-05 |  |
| [[SOWAHC]] | -0.55 | -0.56 / -0.51 | both halves | 1e-05 |  |
| [[FAM83G]] | -0.54 | -0.63 / -0.47 | both halves | 2e-05 |  |
| [[PITRM1]] | -0.53 | -0.54 / -0.45 | both halves | 3e-05 |  |
| [[HUS1]] | -0.51 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[NOP14-AS1]] | -0.49 | -0.57 / -0.43 | both halves | 3e-05 |  |
| [[SEPTIN10]] | -0.49 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[TTPAL]] | -0.48 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[ARPC4]] | -0.48 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[BCAN-AS2]] | -0.48 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[MFSD10]] | -0.48 | -0.50 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HOXA5]] | B | HOXA5 activity lowers RSBN1L's level | lines that do not express HOXA5 (9) vs lines expressing it (41) | 1.06× higher at baseline in the lines without HOXA5 | 0.043 | ⚠ within organs, on part of the lines; also absent: HOXA3, HOXA6, HOTAIRM1 |
| [[PKDCC]] | B | PKDCC activity raises RSBN1L's level | lines that do not express PKDCC (20) vs lines expressing it (30) | 1.19× lower at baseline in the lines without PKDCC | 0.096 | ⚠ within organs, on part of the lines; also absent: CHD5, CCDC144NL-AS1, LINC02864 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 145]]; 31 genes; every member is in the + arm (projection on the module's main direction 0.509). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.21; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-8.4, -7.1); signed map (-18.5, 15.7). **Vector** length 125, 38.7% of its response variance represented; |z| ≥ 3 in 1,303 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ponatinib (drug)]] 5 µM |  | +5.6 | +3.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +4.9 | +4.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +4.7 | +10.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | +3.7 | +5.2 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +3.7 | +2.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.5 | +2.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.2 | +1.8 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -11.4 | -9.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -7.5 | -7.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | -6.5 | -8.8 |
|  | [[EX229 (drug)]] 5 µM |  | -6.4 | -7.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -6.3 | +2.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -6.2 | -6.6 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -5.5 | -4.7 |

## What is on record

|  |  |
|---|---|
| Name | round spermatid basic protein 1 like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q11.23 — chr7:77,696,459-77,783,022 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ42526, FLJ45813, MGC71764 |
| Gene groups (HGNC) | Round spermatid basic protein 1 family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6PCB5](https://www.uniprot.org/uniprotkb/Q6PCB5) (Lysine-specific demethylase RSBN1L):

> Lysine-specific demethylase that specifically demethylates methylated lysine residues of proteins.

**Summary**, from NCBI Gene [222194](https://www.ncbi.nlm.nih.gov/gene/222194):

> Predicted to enable protein demethylase activity. Located in nuclear speck. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:24765](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24765) · Entrez [222194](https://www.ncbi.nlm.nih.gov/gene/222194) · UniProt [Q6PCB5](https://www.uniprot.org/uniprotkb/Q6PCB5) · Ensembl [ENSG00000187257](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000187257)

## Data

Gene col 11906: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11906); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11906, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11906]; `tensor/DDL_lfc|DDL_z.npy` [11906]; `embed/gene_vectors.npy` [11906]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11906 or target_col == 11906). Every well: [[RSBN1L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RSBN1L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
