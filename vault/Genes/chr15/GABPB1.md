---
symbol: "GABPB1"
type: "gene"
col: 2411
ensembl_id: "ENSG00000104064"
name: "GA binding protein transcription factor subunit beta 1"
location: "15q21.2"
module: 124
arm: "+"
pooled_cpm: 57.63
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 11
n_dd_up_clean: 20
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/124"]
generated_by: "tahoemap"
---

# GABPB1

*GA binding protein transcription factor subunit beta 1* — 15q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (6 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.63× (z +16.9, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.469× (z -13.2, q 3e-37, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[E2F3]] (+0.69, fdr 1e-05), [[POU6F1]] (+0.67, fdr 1e-04), [[KLHL42]] (+0.67, fdr 4e-05); moves opposite to [[RAB3A]] (-0.73, fdr 1e-05), [[PJA2]] (-0.65, fdr 6e-05), [[GNAI2]] (-0.65, fdr 5e-04).
> It sits in the **+** arm of [[Module 124]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MLF1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2411.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.63×** | +16.9 | 0e+00 | 47/48 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.52×** | +15.6 | 0e+00 | 45/48 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.87×** | +15.5 | 0e+00 | 43/48 (A549, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.32×** | +14.8 | 0e+00 | 44/47 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.24×** | +14.1 | 3e-43 | 45/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **2.14×** | +13.3 | 2e-38 | 47/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.96×** | +11.8 | 4e-30 | 47/48 (HT-29, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.52×** | +10.4 | 1e-23 | 36/49 (A-172, Hs 766T, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.00×** | +10.1 | 6e-22 | 40/49 (PANC-1, NCI-H2347, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.74×** | +9.1 | 4e-18 | 42/48 (LoVo, A498, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.63×** | +8.5 | 7e-16 | 39/48 (NCI-H460, LoVo, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.65×** | +8.5 | 1e-15 | 37/47 (LoVo, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.57×** | +7.9 | 1e-13 | 28/48 (A549, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.54×** | +7.5 | 2e-12 | 35/48 (A549, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.24×** | +7.4 | 5e-12 | 38/48 (NCI-H1573, NCI-H460, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.47×** | +6.7 | 6e-10 | 33/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.36×** | +5.4 | 2e-06 | 27/48 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2411.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.469×** | -13.2 | 3e-37 | 47/48 (SW480, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.478×** | -12.9 | 8e-36 | 45/48 (BT-474, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.494×** | -11.9 | 3e-30 | 39/42 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.534×** | -11.0 | 7e-26 | 40/48 (NCI-H2347, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.551×** | -10.4 | 2e-23 | 43/48 (SW480, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.792×** | -5.8 | 7e-07 | 27/48 (NCI-H2347, A498, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.721×** | -5.7 | 8e-07 | 34/48 (A498, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.776×** | -4.4 | 6e-04 | 24/49 (LS 180, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Entrectinib (drug)]] 5 µM |  | **0.796×** | -4.0 | 0.004 | 23/48 (NCI-H1792, LoVo, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.822×** | -3.4 | 0.034 | 14/49 (NCI-H2347, RKO, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.779×** | -3.1 | 0.094 | 17/48 (J82, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 0.835× | -3.0 | 0.11 | 17/47 (LoVo, C32, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.842× | -3.0 | 0.11 | 17/48 (SHP-77, RKO, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM |  | 0.720× | -3.0 | 0.11 | 18/47 (H4, SNU-1, …) | inconsistent across doses | cell-cycle shift (explains ~9% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2411. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 70.9 | 13 (2 ⚠) | 2 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 3.55× (z +14.6) | [[Dinaciclib (drug)]] 5 µM 0.264× (z -15.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.403× (z -10.9) |
| [[HOP62 (line)]] | alt | 48.0 | 7 (1 ⚠) | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.85× (z +11.0) | [[Dinaciclib (drug)]] 5 µM 0.334× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.367× (z -10.6) |
| [[LoVo (line)]] | wt | 46.6 | 9 (2 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 4.19× (z +15.7) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.67× (z +14.8) | — |
| [[PANC-1 (line)]] | alt | 70.8 | 7 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.72× (z +23.3) | [[Dinaciclib (drug)]] 5 µM 0.248× (z -14.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.382× (z -10.3) |
| [[SW480 (line)]] | alt | 56.6 | 5 (1 ⚠) | 4 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.70× (z +12.0) | [[Panobinostat (drug)]] 5 µM 0.326× (z -13.6) |
| [[NCI-H2347 (line)]] | alt | 61.5 | 4 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +15.7) | [[Dinaciclib (drug)]] 0.5 µM 0.306× (z -12.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.334× (z -11.4) |
| [[A498 (line)]] | wt | 57.4 | 6 | 1 | [[Harringtonine (drug)]] 5 µM 3.50× (z +11.6) | [[Panobinostat (drug)]] 0.5 µM 0.364× (z -9.8) |
| [[A549 (line)]] | wt | 82.1 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.11× (z +24.2) | — |
| [[LOX-IMVI (line)]] | wt | 62.0 | 4 | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.99× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.154× (z -15.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.366× (z -8.6) |
| [[LS 180 (line)]] | wt | 42.3 | 4 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.26× (z +10.9) | [[Dinaciclib (drug)]] 5 µM 0.273× (z -11.4) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 74.2 | 4 (1 ⚠) | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 4.58× (z +13.4) | [[Dinaciclib (drug)]] 5 µM 0.373× (z -8.7) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 61.8 | 3 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.78× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.209× (z -14.4) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 60.2 | 3 (1 ⚠) | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.76× (z +9.8) | [[Dinaciclib (drug)]] 0.5 µM 0.363× (z -9.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.374× (z -9.5) |
| [[A-172 (line)]] | wt | 30.0 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.60× (z +15.1) | — |
| [[H4 (line)]] | wt | 50.4 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +8.9) | — |
| [[Hs 766T (line)]] | wt | 40.0 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +11.4) | — |
| [[HT-29 (line)]] | alt | 50.6 | 3 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 3.82× (z +11.4) | [[Lonafarnib (drug)]] 5 µM 0.138× (z -8.8) ⚠ toxic |
| [[J82 (line)]] | alt | 65.1 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +11.8) | [[Dinaciclib (drug)]] 0.05 µM 0.288× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~1% of this change |
| [[NCI-H2030 (line)]] | alt | 76.9 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.31× (z +15.1) | — |
| [[RKO (line)]] | wt | 122 | 1 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.77× (z +8.5) | [[Panobinostat (drug)]] 5 µM 0.344× (z -11.3) |
| [[HEC-1-A (line)]] | alt | 58.8 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.49× (z +18.0) | [[Dinaciclib (drug)]] 5 µM 0.413× (z -8.7) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 39.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +8.9) | — |
| [[hTERT-HPNE (line)]] | wt | 38.5 | 3 | 0 | [[Harringtonine (drug)]] 5 µM 5.48× (z +9.8) | — |
| [[SNU-1 (line)]] | wt | 61.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.72× (z +13.0) | — |
| [[SW 900 (line)]] | alt | 44.9 | 3 | 0 | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 3.30× (z +9.2) | — |
| [[SW48 (line)]] | wt | 62.7 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +11.3) | [[Dinaciclib (drug)]] 5 µM 0.129× (z -12.8) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 43.7 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.312× (z -9.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.354× (z -8.9) |
| [[BT-474 (line)]] | alt | 72.6 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.183× (z -15.5) |
| [[CFPAC-1 (line)]] | alt | 43.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.26× (z +12.3) | — |
| [[KATO III (line)]] | alt | 53.9 | 1 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.71× (z +9.8) | [[Dinaciclib (drug)]] 0.5 µM 0.305× (z -11.6) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 67.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.270× (z -10.7) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 59.6 | 1 | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 4.16× (z +12.0) | [[Dinaciclib (drug)]] 5 µM 0.275× (z -10.8) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 58.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.303× (z -12.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.425× (z -8.6) |
| [[C-33 A (line)]] | alt | 61.0 | 1 | 0 | [[Digitoxin (drug)]] 0.5 µM 3.08× (z +8.9) | — |
| [[COLO 205 (line)]] | alt | 37.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.42× (z +8.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 51.9 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 3.31× (z +9.1) | — |
| [[Panc 03.27 (line)]] | alt | 60.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +9.3) | — |
| [[SK-MEL-2 (line)]] | alt | 63.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.179× (z -14.6) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 49.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 114 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 33.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 38.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 60.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 51.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 72.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 58.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 56.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 45.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2411), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 6 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[E2F3]] | +0.69 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[POU6F1]] | +0.67 | +0.54 / +0.34 | both halves | 1e-04 |  |
| [[KLHL42]] | +0.67 | +0.48 / +0.40 | both halves | 4e-05 |  |
| [[ITPA]] | +0.66 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[GCNT4]] | +0.66 | +0.48 / +0.32 | both halves | 2e-04 |  |
| [[EPM2A]] | +0.65 | +0.54 / +0.28 | both halves | 3e-04 |  |
| [[STARD7-AS1]] | +0.65 | +0.54 / +0.39 | both halves | 5e-05 |  |
| [[MTG2]] | +0.65 | +0.45 / +0.47 | both halves | 3e-05 |  |
| [[RCC1L]] | +0.64 | +0.53 / +0.39 | both halves | 5e-05 |  |
| [[SPRY3]] | +0.64 | +0.33 / +0.39 | both halves | 1e-04 |  |
| [[YARS2]] | +0.64 | +0.48 / +0.29 | both halves | 3e-04 |  |
| [[PBLD]] | +0.63 | +0.37 / +0.28 | both halves | 3e-04 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAB3A]] | -0.73 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[PJA2]] | -0.65 | -0.59 / -0.38 | both halves | 6e-05 |  |
| [[GNAI2]] | -0.65 | -0.49 / -0.23 | both halves | 5e-04 |  |
| [[TTC3]] | -0.64 | -0.53 / -0.54 | both halves | 1e-05 |  |
| [[DNAAF3]] | -0.63 | -0.42 / -0.40 | both halves | 4e-05 |  |
| [[USP48]] | -0.63 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[SPAG9]] | -0.62 | -0.45 / -0.35 | both halves | 1e-04 |  |
| [[CDON]] | -0.62 | -0.48 / -0.46 | both halves | 3e-05 |  |
| [[ALAD]] | -0.61 | -0.42 / -0.31 | both halves | 2e-04 |  |
| [[STARD5]] | -0.61 | -0.39 / -0.40 | both halves | 5e-05 |  |
| [[GDE1]] | -0.60 | -0.32 / -0.41 | both halves | 2e-04 |  |
| [[PAPSS1]] | -0.60 | -0.37 / -0.44 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MLF1]] | B | MLF1 activity lowers GABPB1's level | lines that do not express MLF1 (5) vs lines expressing it (45) | 1.45× higher at baseline in the lines without MLF1 | 0.060 | ⚠ within organs, on part of the lines; also absent: CCDC110, MLH1, ITGA3; its own permutation p |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises GABPB1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises GABPB1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 124]]; 39 genes; this gene is in the **+** arm (projection on the module's main direction 0.764). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (-5.0, 10.1); signed map (24.3, -26.5). **Vector** length 96.7, 29.5% of its response variance represented; |z| ≥ 3 in 1,528 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +11.8 | +10.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +8.4 | +6.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.7 | +3.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.3 | +15.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.3 | +1.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.6 | -2.8 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +3.3 | +0.4 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +3.3 | +0.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.2 | +4.6 |
|  | [[Benztropine (mesylate) (drug)]] 0.05 µM |  | +2.8 | +0.9 |
| fall | [[Panobinostat (drug)]] 5 µM |  | -6.6 | -13.2 |
|  | [[Belinostat (drug)]] 5 µM |  | -6.6 | -10.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -6.4 | -12.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -4.9 | -5.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.5 | -2.9 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -2.2 | -0.6 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -2.1 | +0.4 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.0 | +0.6 |
|  | [[Allopurinol (drug)]] 0.05 µM |  | -2.0 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | GA binding protein transcription factor subunit beta 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q21.2 — chr15:50,275,389-50,355,408 (-) |
| Ensembl biotype | protein_coding |
| Also known as | E4TF1-47, GABPB; previously GABPB2 |
| Gene groups (HGNC) | Ankyrin repeat domain containing; GA binding protein transcription factor subunits |
| Reactome | 3 pathways, smallest: Transcriptional activation of mitochondrial biogenesis; Mitochondrial biogenesis; Organelle biogenesis and maintenance |
| Matched by | ensembl_id |

**Function**, from UniProt [Q06547](https://www.uniprot.org/uniprotkb/Q06547) (GA-binding protein subunit beta-1):

> Transcription factor capable of interacting with purine rich repeats (GA repeats). Acts as a master regulator of nuclear-encoded mitochondrial genes (By similarity).; (Microbial infection) Necessary for the expression of the Adenovirus E4 gene.

**Summary**, from NCBI Gene [2553](https://www.ncbi.nlm.nih.gov/gene/2553):

> This gene encodes the GA-binding protein transcription factor, beta subunit. This protein forms a tetrameric complex with the alpha subunit, and stimulates transcription of target genes. The encoded protein may be involved in activation of cytochrome oxidase expression and nuclear control of mitochondrial function. The crystal structure of a similar protein in mouse has been resolved as a ternary protein complex. Multiple transcript variants encoding distinct isoforms have been identified for …

**Accessions** — [HGNC:4074](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4074) · Entrez [2553](https://www.ncbi.nlm.nih.gov/gene/2553) · UniProt [Q06547](https://www.uniprot.org/uniprotkb/Q06547) · Ensembl [ENSG00000104064](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104064)

## Data

Gene col 2411: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2411); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2411, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2411]; `tensor/DDL_lfc|DDL_z.npy` [2411]; `embed/gene_vectors.npy` [2411]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2411 or target_col == 2411). Every well: [[GABPB1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GABPB1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
