---
symbol: "HACD2"
type: "gene"
col: 13045
ensembl_id: "ENSG00000206527"
name: "3-hydroxyacyl-CoA dehydratase 2"
location: "3q21.1"
module: 25
arm: "+"
pooled_cpm: 88.18
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 0
n_dd_up_clean: 14
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# HACD2

*3-hydroxyacyl-CoA dehydratase 2* — 3q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.18× (z +23.6, q 0e+00, up in 45 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (NCI-H661 0.0721×); [[Allantoin (drug)]] 0.05 µM in 1 line (Hs 766T 0.258×; ⚠ transcription drop); [[Clobetasol propionate (drug)]] 0.5 µM in 1 line (NCI-H1573 0.418×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GPD2]] (+0.66, fdr 1e-05), [[CFL2]] (+0.62, fdr 1e-05), [[LPGAT1]] (+0.62, fdr 2e-05); moves opposite to [[ATG101]] (-0.67, fdr 1e-05), [[ELL]] (-0.64, fdr 1e-05), [[EXOSC4]] (-0.61, fdr 5e-05).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ITPRIP]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 16 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13045.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.18×** | +23.6 | 0e+00 | 45/48 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.20×** | +17.0 | 0e+00 | 47/48 (SW480, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.01×** | +14.4 | 7e-45 | 44/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.94×** | +13.7 | 1e-40 | 35/44 (MIA PaCa-2, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.80×** | +12.6 | 4e-34 | 39/49 (MIA PaCa-2, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.78×** | +12.4 | 4e-33 | 43/48 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.76×** | +12.1 | 6e-32 | 41/48 (SW480, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.41×** | +10.5 | 7e-24 | 40/48 (PANC-1, CFPAC-1, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.58×** | +9.9 | 3e-21 | 37/48 (BT-474, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.57×** | +9.7 | 1e-20 | 39/48 (BT-474, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.48×** | +8.4 | 2e-15 | 38/48 (LoVo, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.44×** | +7.6 | 2e-12 | 31/47 (LoVo, COLO 205, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.37×** | +6.8 | 6e-10 | 31/48 (A498, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **1.41×** | +6.8 | 6e-10 | 31/45 (A-172, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Selinexor (drug)]] 0.5 µM |  | **1.34×** | +6.2 | 2e-08 | 36/48 (PANC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.05 µM |  | **1.33×** | +6.1 | 4e-08 | 30/49 (NCI-H2347, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[venetoclax (drug)]] 5 µM |  | **1.57×** | +5.1 | 1e-05 | 27/48 (PANC-1, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.25×** | +4.9 | 3e-05 | 26/48 (LoVo, KATO III, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.34×** | +4.5 | 1e-04 | 26/48 (NCI-H460, NCI-H23, …) | two highest doses | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 1.19× | +3.6 | 0.006 | 18/49 (NCI-H1573, PANC-1, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 1.20× | +3.6 | 0.007 | 18/48 (NCI-H1573, PANC-1, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13045.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (NCI-H661 0.0721×); [[Allantoin (drug)]] 0.05 µM in 1 line (Hs 766T 0.258×; ⚠ transcription drop); [[Clobetasol propionate (drug)]] 0.5 µM in 1 line (NCI-H1573 0.418×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Lactate (calcium) (drug)]] 0.5 µM |  | 0.842× | -3.7 | 0.10 | 21/48 (RPMI-7951, NCI-H1573, …) | two highest doses |  |
| [[Clotrimazole (drug)]] 0.5 µM |  | 0.857× | -3.4 | 0.15 | 13/48 (NCI-H661, KATO III, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | 0.806× | -3.3 | 0.15 | 17/48 (SHP-77, HepG2/C3A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Pimozide (drug)]] 0.5 µM | ⚠ transcription drop | 0.870× | -3.0 | 0.26 | 13/47 (SK-MEL-2, SHP-77, …) | inconsistent across doses |  |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | 0.871× | -3.0 | 0.26 | 7/48 (Panc 03.27, AsPC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13045. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 134 | 9 (2 ⚠) | 1 | [[Digitoxin (drug)]] 5 µM 2.99× (z +10.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.88× (z +10.2) | [[Clobetasol propionate (drug)]] 0.5 µM 0.418× (z -8.5) |
| [[HOP62 (line)]] | alt | 47.1 | 9 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +14.7) | — |
| [[SW480 (line)]] | alt | 96.4 | 9 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +23.1) | — |
| [[BT-474 (line)]] | alt | 113 | 7 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.03× (z +17.3) | — |
| [[HEC-1-A (line)]] | alt | 103 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +15.3) | — |
| [[J82 (line)]] | alt | 128 | 7 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +15.5) | — |
| [[PANC-1 (line)]] | alt | 92.7 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +18.8) | — |
| [[COLO 205 (line)]] | alt | 59.5 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.36× (z +17.0) | — |
| [[SW1417 (line)]] | alt | 188 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.83× (z +19.8) | — |
| [[A549 (line)]] | wt | 77.2 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.10× (z +19.5) | — |
| [[HT-29 (line)]] | alt | 102 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.54× (z +21.9) | — |
| [[LoVo (line)]] | wt | 98.3 | 5 (3 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.83× (z +13.7) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.50× (z +12.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 91.2 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.53× (z +14.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.07× (z +11.8) | — |
| [[A-172 (line)]] | wt | 43.3 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.35× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.89× (z +8.9) | — |
| [[KATO III (line)]] | alt | 94.1 | 4 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.52× (z +16.9) | — |
| [[SNU-423 (line)]] | alt | 61.9 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.51× (z +16.0) | — |
| [[A498 (line)]] | wt | 51.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.97× (z +21.5) | — |
| [[CFPAC-1 (line)]] | alt | 87.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.16× (z +18.2) | — |
| [[HepG2_C3A (line)]] | wt | 136 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +16.3) | — |
| [[HS-578T (line)]] | alt | 73.1 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +16.2) | — |
| [[NCI-H1792 (line)]] | alt | 45.6 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.65× (z +11.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.64× (z +8.5) | — |
| [[NCI-H460 (line)]] | wt | 48.1 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.73× (z +12.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.70× (z +9.3) | — |
| [[Panc 03.27 (line)]] | alt | 167 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +14.1) | — |
| [[SK-MEL-2 (line)]] | alt | 64.1 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +14.0) | — |
| [[C32 (line)]] | wt | 53.6 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.02× (z +9.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.91× (z +9.1) | — |
| [[Hs 766T (line)]] | wt | 35.4 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.49× (z +9.8) ⚠ toxic; transcription drop | [[Allantoin (drug)]] 0.05 µM 0.258× (z -10.7) ⚠ transcription drop |
| [[RKO (line)]] | wt | 74.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +11.5) | — |
| [[A-427 (line)]] | wt | 124 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +10.4) | — |
| [[AsPC-1 (line)]] | alt | 63.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +13.7) | — |
| [[HCT15 (line)]] | alt | 125 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.56× (z +9.2) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 41.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.85× (z +12.4) | — |
| [[LOX-IMVI (line)]] | wt | 48.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.43× (z +9.2) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 70.4 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.52× (z +9.5) | — |
| [[NCI-H2347 (line)]] | alt | 151 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +14.0) | — |
| [[NCI-H661 (line)]] | alt | 85.3 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.0721× (z -13.5) |
| [[RPMI-7951 (line)]] | alt | 62.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +9.3) | — |
| [[SNU-1 (line)]] | wt | 75.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +10.1) | — |
| [[SW 900 (line)]] | alt | 48.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +10.3) | — |
| [[AN3 CA (line)]] | alt | 62.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 104 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 52.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 78.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 155 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 79.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 87.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 78.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 50.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 84.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 116 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13045), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*43 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPD2]] | +0.66 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[CFL2]] | +0.62 | +0.49 / +0.63 | both halves | 1e-05 |  |
| [[LPGAT1]] | +0.62 | +0.46 / +0.59 | both halves | 2e-05 |  |
| [[TMEM237]] | +0.61 | +0.47 / +0.67 | both halves | 2e-05 |  |
| [[TMEM106B]] | +0.59 | +0.44 / +0.59 | both halves | 3e-05 |  |
| [[PON2]] | +0.57 | +0.34 / +0.52 | both halves | 1e-04 | pathway: Fatty acid metabolism |
| [[VRK2]] | +0.57 | +0.45 / +0.54 | both halves | 3e-05 |  |
| [[RAB11FIP2]] | +0.55 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[GALNT7]] | +0.55 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[OGFRL1]] | +0.54 | +0.37 / +0.56 | both halves | 8e-05 |  |
| [[DPY19L4]] | +0.54 | +0.24 / +0.59 | both halves | 4e-04 |  |
| [[ERAP1]] | +0.54 | +0.46 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*57 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATG101]] | -0.67 | -0.54 / -0.68 | both halves | 1e-05 |  |
| [[ELL]] | -0.64 | -0.53 / -0.67 | both halves | 1e-05 |  |
| [[EXOSC4]] | -0.61 | -0.39 / -0.63 | both halves | 5e-05 |  |
| [[RABGEF1P1]] | -0.60 | -0.47 / -0.64 | both halves | 2e-05 |  |
| [[ZNRD2]] | -0.59 | -0.45 / -0.56 | both halves | 3e-05 |  |
| [[YRDC]] | -0.57 | -0.54 / -0.57 | both halves | 1e-05 |  |
| [[RBAK-RBAKDN]] | -0.57 | -0.56 / -0.46 | both halves | 2e-05 |  |
| [[ZKSCAN5]] | -0.56 | -0.44 / -0.52 | both halves | 3e-05 |  |
| [[MYO9B]] | -0.55 | -0.45 / -0.57 | both halves | 3e-05 |  |
| [[NUDT22]] | -0.55 | -0.34 / -0.57 | both halves | 1e-04 |  |
| [[FBXL18]] | -0.55 | -0.29 / -0.59 | both halves | 3e-04 |  |
| [[MAP2K1]] | -0.53 | -0.52 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ITPRIP]] | B | ITPRIP activity lowers HACD2's level | lines that do not express ITPRIP (10) vs lines expressing it (40) | 1.55× higher at baseline in the lines without ITPRIP | 0.026 | ⚠ within organs, on part of the lines; also absent: C13orf46; maybe low, not absent |
| [[LONRF2]] | B | LONRF2 activity lowers HACD2's level | lines that do not express LONRF2 (21) vs lines expressing it (29) | 1.02× higher at baseline in the lines without LONRF2 | 0.077 | ⚠ within organs, on part of the lines; also absent: ANKRD6, PPM1E, ADCY1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.525). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-29.0, -17.6); signed map (-17.5, -39.3). **Vector** length 107, 30.7% of its response variance represented; |z| ≥ 3 in 1,299 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +9.3 | +10.5 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +5.7 | +6.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +4.9 | +17.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +4.7 | +3.6 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.7 | +3.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.3 | +1.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +3.7 | +3.6 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +3.6 | +2.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.3 | +2.7 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -7.4 | -1.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -5.9 | -0.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.2 | +0.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.2 | -1.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.8 | +2.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.5 | -3.3 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -2.4 | -0.9 |
|  | [[TAK-901 (drug)]] 0.5 µM |  | -2.3 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | 3-hydroxyacyl-CoA dehydratase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q21.1 — chr3:123,490,820-123,585,053 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously PTPLB |
| Gene groups (HGNC) | 3-hydroxyacyl-CoA dehydratase family |
| Reactome | 4 pathways, smallest: Synthesis of very long-chain fatty acyl-CoAs; Fatty acyl-CoA biosynthesis; Fatty acid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6Y1H2](https://www.uniprot.org/uniprotkb/Q6Y1H2) (Very-long-chain):

> Catalyzes the third of the very long-chain fatty acids (VLCFA) elongation four-step cycle (condensation, reduction, dehydration, and reduction). This endoplasmic reticulum-elongation process is characterized by the addition of two carbons to the lipid chain through each cycle. This enzyme catalyzes the dehydration of the 3-hydroxyacyl-CoA intermediate into trans-2,3-enoyl-CoA, within each cycle of elongation. Therefore, it participates in the production of various VLCFAs involved in multiple …

**Summary**, from NCBI Gene [201562](https://www.ncbi.nlm.nih.gov/gene/201562):

> The protein encoded by this gene can catalyze the third step (dehydration) in the conversion of long chain fatty acids to very long chain fatty acids. The encoded protein localizes to the endoplasmic reticulum membrane. [provided by RefSeq, Jul 2016]

**Accessions** — [HGNC:9640](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9640) · Entrez [201562](https://www.ncbi.nlm.nih.gov/gene/201562) · UniProt [Q6Y1H2](https://www.uniprot.org/uniprotkb/Q6Y1H2) · Ensembl [ENSG00000206527](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000206527)

## Data

Gene col 13045: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13045); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13045, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13045]; `tensor/DDL_lfc|DDL_z.npy` [13045]; `embed/gene_vectors.npy` [13045]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13045 or target_col == 13045). Every well: [[HACD2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HACD2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
