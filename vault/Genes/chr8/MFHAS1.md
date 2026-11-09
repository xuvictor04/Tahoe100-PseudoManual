---
symbol: "MFHAS1"
type: "gene"
col: 7172
ensembl_id: "ENSG00000147324"
name: "multifunctional ROCO family signaling regulator 1"
location: "8p23.1"
module: 18
arm: "+"
pooled_cpm: 72.4
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 12
n_dd_up_clean: 6
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# MFHAS1

*multifunctional ROCO family signaling regulator 1* — 8p23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 2.58× (z +13.8, q 1e-40, up in 40 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.569× (z -24.0, q 0e+00, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[USP31]] (+0.55, fdr 2e-05), [[CDYL]] (+0.55, fdr 3e-05), [[DOCK9]] (+0.55, fdr 1e-05); moves opposite to [[SF3B1]] (-0.55, fdr 2e-05), [[RAB3GAP2]] (-0.52, fdr 1e-05), [[TMEM167B]] (-0.48, fdr 3e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PHF21B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 11 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7172.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.58×** | +13.8 | 1e-40 | 40/49 (A549, LoVo, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.26×** | +7.1 | 5e-10 | 25/48 (COLO 205, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.50×** | +6.0 | 5e-07 | 23/48 (SW48, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | **1.22×** | +5.7 | 2e-06 | 19/47 (CFPAC-1, NCI-H2347, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.18× | +5.1 | 4e-05 | 18/48 (Hs 766T, Panc 03.27, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains <1% of this change | 1.17× | +4.8 | 2e-04 | 16/48 (LOX-IMVI, Hs 766T, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.12× | +4.7 | 2e-04 | 13/49 (MIA PaCa-2, CFPAC-1, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 1.17× | +4.7 | 2e-04 | 19/47 (CFPAC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 1.17× | +4.7 | 2e-04 | 15/48 (CFPAC-1, NCI-H2347, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~3% of this change | 1.17× | +4.7 | 2e-04 | 18/48 (NCI-H23, SW480, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | 1.17× | +4.5 | 4e-04 | 14/48 (LoVo, PANC-1, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.10× | +4.2 | 0.001 | 10/48 (AsPC-1, A549, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 1.14× | +4.0 | 0.002 | 15/47 (MIA PaCa-2, CFPAC-1, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 1.10× | +3.9 | 0.003 | 11/48 (A498, HOP62, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~6% of this change | 1.14× | +3.9 | 0.003 | 16/48 (HS-578T, H4, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **1.31×** | +3.9 | 0.003 | 9/49 (A498, A-427, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Rapamycin (drug)]] 5 µM |  | 1.09× | +3.8 | 0.004 | 6/48 (H4, AsPC-1, …) | rises with dose |  |
| [[Amsacrine (drug)]] 5 µM |  | 1.09× | +3.7 | 0.007 | 5/48 (SW480, H4, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.13× | +3.6 | 0.009 | 13/48 (CFPAC-1, MIA PaCa-2, …) | rises with dose |  |
| [[vincristine (drug)]] 0.5 µM |  | 1.18× | +3.5 | 0.013 | 9/48 (MIA PaCa-2, LoVo, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.08× | +3.4 | 0.018 | 10/48 (A498, LoVo, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7172.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.569×** | -24.0 | 0e+00 | 40/48 (NCI-H23, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.653×** | -12.4 | 1e-32 | 29/48 (SNU-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.692×** | -11.1 | 3e-26 | 26/48 (A-172, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.698×** | -10.4 | 3e-23 | 27/42 (A-172, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.726×** | -9.7 | 5e-20 | 28/48 (A-172, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.727×** | -9.6 | 7e-20 | 25/48 (A-172, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.770×** | -7.9 | 3e-13 | 23/48 (SHP-77, SK-MEL-2, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.778×** | -7.0 | 2e-10 | 24/44 (SW480, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~2% of this change | 0.863× | -6.3 | 2e-08 | 17/48 (NCI-H2347, Panc 03.27, …) | rises with dose | low cells (technical?) |
| [[NG25 (drug)]] 5 µM |  | **0.679×** | -5.6 | 1e-06 | 20/47 (A-172, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.826×** | -5.5 | 2e-06 | 20/47 (HEC-1-A, RKO, …) | all doses, stronger at high dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.957× | -4.4 | 5e-04 | 0/50 | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.870× | -4.2 | 0.001 | 18/48 (SW48, RKO, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.876× | -4.0 | 0.003 | 16/48 (C32, NCI-H460, …) | rises with dose |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | 0.872× | -3.9 | 0.004 | 14/48 (SW48, HEC-1-A, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.891× | -3.5 | 0.019 | 12/49 (HEC-1-A, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[ERK5-IN-2 (drug)]] 5 µM |  | **0.794×** | -3.4 | 0.025 | 4/49 (A-172, SW48, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.807×** | -3.1 | 0.052 | 6/48 (A498, Panc 03.27, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7172. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 216 | 1 | 10 (6 ⚠) | [[TAK-901 (drug)]] 5 µM 3.57× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.248× (z -21.1) ⚠ toxic; transcription drop · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.451× (z -17.7) |
| [[SW48 (line)]] | wt | 171 | 2 | 7 (4 ⚠) | [[PH-797804 (drug)]] 5 µM 7.04× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.147× (z -26.3) |
| [[SW480 (line)]] | alt | 84.6 | 1 | 7 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 3.95× (z +10.4) | [[Homoharringtonine (drug)]] 5 µM 0.493× (z -15.7) |
| [[NCI-H460 (line)]] | wt | 39.9 | 1 (1 ⚠) | 5 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.19× (z +11.8) ⚠ cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 5 µM 0.383× (z -14.4) |
| [[SHP-77 (line)]] | alt | 153 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.357× (z -12.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.396× (z -11.5) |
| [[A498 (line)]] | wt | 99.2 | 3 (2 ⚠) | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.95× (z +10.6) | [[Dinaciclib (drug)]] 5 µM 0.439× (z -10.8) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 139 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.375× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.494× (z -10.0) |
| [[RKO (line)]] | wt | 96.5 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.356× (z -16.4) |
| [[SK-MEL-2 (line)]] | alt | 72.8 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.256× (z -20.4) |
| [[C32 (line)]] | wt | 37.4 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -16.8) |
| [[HepG2_C3A (line)]] | wt | 192 | 1 | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.27× (z +9.4) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.373× (z -11.1) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.479× (z -8.6) |
| [[LS 180 (line)]] | wt | 87.6 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.370× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.511× (z -10.7) |
| [[A-427 (line)]] | wt | 82.2 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.496× (z -13.0) |
| [[NCI-H596 (line)]] | alt | 69.8 | 1 (1 ⚠) | 2 | [[Trametinib (drug)]] 5 µM 3.68× (z +11.5) ⚠ cell-cycle shift, explains ~25% of this change | [[Citalopram (hydrobromide) (drug)]] 0.05 µM 0.0939× (z -20.6) |
| [[PANC-1 (line)]] | alt | 35.8 | 1 | 2 | [[TAK-901 (drug)]] 5 µM 4.73× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.376× (z -16.4) |
| [[SNU-1 (line)]] | wt | 69.2 | 0 | 3 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.162× (z -14.1) |
| [[A549 (line)]] | wt | 109 | 2 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 10.0× (z +14.1) | — |
| [[C-33 A (line)]] | alt | 82.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.161× (z -17.2) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 76.2 | 1 (1 ⚠) | 1 | [[Selinexor (drug)]] 5 µM 2.31× (z +9.6) ⚠ cell-cycle shift, explains ~2% of this change | [[Homoharringtonine (drug)]] 5 µM 0.428× (z -9.7) |
| [[LoVo (line)]] | wt | 105 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 4.94× (z +10.8) | [[Homoharringtonine (drug)]] 5 µM 0.403× (z -17.9) |
| [[MIA PaCa-2 (line)]] | alt | 52.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -23.4) |
| [[NCI-H1573 (line)]] | alt | 35.4 | 2 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 28.6× (z +9.5) | — |
| [[NCI-H1792 (line)]] | alt | 85.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.354× (z -13.5) |
| [[NCI-H2030 (line)]] | alt | 59.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -20.5) |
| [[NCI-H2347 (line)]] | alt | 88.6 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.393× (z -15.8) ⚠ cell-cycle shift, explains ~2% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.541× (z -10.4) |
| [[HCT15 (line)]] | alt | 94.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.399× (z -11.7) |
| [[HEC-1-A (line)]] | alt | 113 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.455× (z -11.0) |
| [[Hs 766T (line)]] | wt | 42.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.486× (z -9.0) |
| [[LOX-IMVI (line)]] | wt | 35.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.381× (z -11.8) |
| [[NCI-H23 (line)]] | alt | 42.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0718× (z -29.5) |
| [[Panc 03.27 (line)]] | alt | 46.7 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.443× (z -10.8) ⚠ cell-cycle shift, explains ~2% of this change |
| [[SW1417 (line)]] | alt | 32.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.480× (z -9.2) |
| [[AN3 CA (line)]] | alt | 58.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 48.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 46.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 29.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 53.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 48.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 44.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 97.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 63.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 54.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 37.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7172), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USP31]] | +0.55 | +0.61 / +0.47 | both halves | 2e-05 |  |
| [[CDYL]] | +0.55 | +0.59 / +0.43 | both halves | 3e-05 |  |
| [[DOCK9]] | +0.55 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[ZDHHC14]] | +0.55 | +0.40 / +0.55 | both halves | 5e-05 |  |
| [[UBTD2]] | +0.54 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[SMIM13]] | +0.52 | +0.58 / +0.40 | both halves | 5e-05 |  |
| [[BCL7A]] | +0.52 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[ABCA3]] | +0.52 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[ABHD15]] | +0.51 | +0.30 / +0.57 | both halves | 2e-04 |  |
| [[PAQR4]] | +0.51 | +0.44 / +0.55 | both halves | 3e-05 |  |
| [[LIMD1]] | +0.50 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[UCK2]] | +0.50 | +0.47 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SF3B1]] | -0.55 | -0.47 / -0.57 | both halves | 2e-05 |  |
| [[RAB3GAP2]] | -0.52 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[TMEM167B]] | -0.48 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[PRPF38A]] | -0.47 | -0.39 / -0.45 | both halves | 5e-05 |  |
| [[HDLBP]] | -0.47 | -0.38 / -0.45 | both halves | 7e-05 |  |
| [[CUL4B]] | -0.46 | -0.31 / -0.49 | both halves | 2e-04 |  |
| [[SEC23B]] | -0.46 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[RAB1B]] | -0.46 | -0.29 / -0.47 | both halves | 2e-04 |  |
| [[PAN2]] | -0.46 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[COPG1]] | -0.45 | -0.32 / -0.49 | both halves | 2e-04 |  |
| [[TP53BP1]] | -0.44 | -0.34 / -0.49 | both halves | 1e-04 |  |
| [[YIPF6]] | -0.44 | -0.37 / -0.46 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PHF21B]] | B | PHF21B activity lowers MFHAS1's level | lines that do not express PHF21B (21) vs lines expressing it (29) | 1.20× higher at baseline in the lines without PHF21B | 0.097 | ⚠ within organs, on part of the lines; also absent: JAM3, ADAM23, ADD2 |
| [[TRIM35]] | C | TRIM35's natural level strengthens MFHAS1's drug response | TRIM35's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.64, reverse +0.07; direction not clear | 0.056 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.368). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-7.2, -2.8); signed map (-13.0, 46.0). **Vector** length 116, 29.5% of its response variance represented; |z| ≥ 3 in 1,228 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +7.6 | +13.8 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~3% of this change | +6.8 | +4.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +6.0 | +6.0 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~5% of this change | +5.4 | +3.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | +4.5 | +5.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.3 | +4.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.3 | +3.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.7 | +4.2 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -5.0 | -24.0 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -4.4 | -4.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.6 | -12.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~2% of this change | -2.8 | -6.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.8 | -4.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.5 | -7.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.4 | -2.0 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.2 | -3.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.2 | -2.3 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -2.0 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | multifunctional ROCO family signaling regulator 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p23.1 — chr8:8,783,354-8,893,630 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MASL1, LRRC65 |
| Gene groups (HGNC) | ROCO family |
| Hallmark sets | HEME_METABOLISM |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y4C4](https://www.uniprot.org/uniprotkb/Q9Y4C4) (Malignant fibrous histiocytoma-amplified sequence 1):

> Probable GTP-binding protein. Functions in innate immunity and more specifically the inflammatory response as a regulator of the Toll-like receptor TLR2 and TLR4 signaling pathways. Negatively regulates the part of the TLR4 signaling pathway that leads to the activation of the transcription factor AP-1. By retaining the phosphatase complex PP2A into the cytoplasm, prevents the dephosphorylation of the AP-1 subunit JUN which is required for proper activation of the transcription factor. Both …

**Summary**, from NCBI Gene [9258](https://www.ncbi.nlm.nih.gov/gene/9258):

> Identified in a human 8p amplicon, this gene is a potential oncogene whose expression is enhanced in some malignant fibrous histiocytomas (MFH). The primary structure of its product includes an ATP/GTP-binding site, three leucine zipper domains, and a leucine-rich tandem repeat, which are structural or functional elements for interactions among proteins related to the cell cycle, and which suggest that overexpression might be oncogenic with respect to MFH. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:16982](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16982) · Entrez [9258](https://www.ncbi.nlm.nih.gov/gene/9258) · UniProt [Q9Y4C4](https://www.uniprot.org/uniprotkb/Q9Y4C4) · Ensembl [ENSG00000147324](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000147324)

## Data

Gene col 7172: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7172); `tables/drug_effects.parquet` (54 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7172, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7172]; `tensor/DDL_lfc|DDL_z.npy` [7172]; `embed/gene_vectors.npy` [7172]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7172 or target_col == 7172). Every well: [[MFHAS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MFHAS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
