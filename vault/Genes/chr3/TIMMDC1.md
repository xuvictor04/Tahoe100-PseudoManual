---
symbol: "TIMMDC1"
type: "gene"
col: 3508
ensembl_id: "ENSG00000113845"
name: "translocase of inner mitochondrial membrane domain containing 1"
location: "3q13.33"
module: 148
arm: "+"
pooled_cpm: 45.59
n_lines_expressing: 50
n_dd_up: 27
n_dd_down: 10
n_dd_up_clean: 16
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/148"]
generated_by: "tahoemap"
---

# TIMMDC1

*translocase of inner mitochondrial membrane domain containing 1* — 3q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.63× (z +14.1, q 4e-42, up in 38 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.69× (z +11.2, q 1e-26, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.490× (z -10.8, q 2e-24, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (91 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BCDIN3D]] (+0.75, fdr 7e-06), [[KRCC1]] (+0.71, fdr 1e-05), [[THOC7]] (+0.69, fdr 7e-06); moves opposite to [[CABLES2]] (-0.64, fdr 7e-05), [[IGSF8]] (-0.63, fdr 1e-04), [[EFNA4]] (-0.62, fdr 2e-04).
> It sits in the **+** arm of [[Module 148]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 12 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3508.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.63×** | +14.1 | 4e-42 | 38/42 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.53×** | +14.0 | 4e-42 | 45/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.69×** | +11.2 | 1e-26 | 41/48 (MIA PaCa-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.84×** | +8.5 | 2e-15 | 33/43 (SW480, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.73×** | +7.9 | 2e-13 | 36/48 (PANC-1, SW480, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.37×** | +6.7 | 2e-09 | 34/48 (A-172, SW1417, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.52×** | +6.1 | 9e-08 | 32/48 (SW480, COLO 205, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.50×** | +5.9 | 3e-07 | 30/48 (Hs 766T, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.44×** | +5.5 | 3e-06 | 26/47 (A-172, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.42×** | +5.3 | 8e-06 | 31/48 (A-172, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.42×** | +5.2 | 8e-06 | 30/48 (A549, A498, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.27×** | +5.1 | 2e-05 | 27/48 (RKO, NCI-H1573, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.26×** | +5.0 | 3e-05 | 23/47 (Hs 766T, A-172, …) | all doses, flat | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.39×** | +5.0 | 3e-05 | 28/47 (HT-29, LS 180, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~13% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.39×** | +4.6 | 2e-04 | 28/47 (HS-578T, PANC-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.30×** | +4.0 | 0.002 | 26/48 (PANC-1, CFPAC-1, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.26×** | +3.5 | 0.015 | 19/48 (SHP-77, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.24×** | +3.3 | 0.027 | 15/48 (PANC-1, NCI-H1792, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.41×** | +3.2 | 0.030 | 13/47 (NCI-H1792, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Vitamin K4 (drug)]] 0.05 µM |  | **1.24×** | +3.2 | 0.034 | 11/48 (SNU-423, LOX-IMVI, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.40×** | +3.1 | 0.036 | 16/48 (RPMI-7951, HEC-1-A, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3508.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.490×** | -10.8 | 2e-24 | 42/48 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.509×** | -10.2 | 4e-22 | 45/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.515×** | -10.0 | 2e-21 | 37/47 (PANC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.556×** | -8.9 | 7e-17 | 35/48 (MIA PaCa-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.602×** | -7.7 | 2e-12 | 37/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.408×** | -6.5 | 8e-09 | 36/48 (SW480, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.557×** | -4.2 | 0.002 | 24/49 (NCI-H23, A-427, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.772×** | -3.9 | 0.006 | 24/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.800×** | -3.4 | 0.044 | 19/48 (PANC-1, LoVo, …) | rises with dose |  |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 0.857× | -3.3 | 0.049 | 11/48 (Hs 766T, A-427, …) | all doses, stronger at high dose | position effect removed |
| [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | **0.811×** | -3.2 | 0.072 | 13/48 (LoVo, COLO 205, …) | all doses, stronger at high dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3508. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 75.5 | 3 (2 ⚠) | 5 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.53× (z +10.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.90× (z +10.6) | [[Digitoxin (drug)]] 0.5 µM 0.306× (z -14.0) |
| [[SW480 (line)]] | alt | 41.3 | 4 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.48× (z +12.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.95× (z +9.6) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.314× (z -11.8) |
| [[NCI-H23 (line)]] | alt | 74.6 | 2 (1 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.35× (z +11.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.93× (z +9.1) | [[Digitoxin (drug)]] 0.5 µM 0.308× (z -11.6) |
| [[NCI-H460 (line)]] | wt | 32.1 | 2 (2 ⚠) | 4 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.24× (z +12.9) ⚠ toxic; transcription drop | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.309× (z -10.9) |
| [[A-427 (line)]] | wt | 97.5 | 1 (1 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.14× (z +8.5) ⚠ toxic; transcription drop | [[Dinaciclib (drug)]] 0.05 µM 0.0873× (z -25.3) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 49.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.91× (z +12.0) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 27.5 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.82× (z +10.5) | — |
| [[HT-29 (line)]] | alt | 42.8 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.309× (z -9.4) |
| [[J82 (line)]] | alt | 46.3 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.03× (z +9.4) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 0.5 µM 0.285× (z -10.7) |
| [[LoVo (line)]] | wt | 46.7 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.45× (z +9.1) ⚠ toxic; transcription drop | [[Niclosamide (olamine) (drug)]] 5 µM 0.322× (z -11.5) ⚠ toxic; cell-cycle shift, would explain all of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.434× (z -8.8) |
| [[LOX-IMVI (line)]] | wt | 37.2 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.60× (z +10.1) ⚠ toxic; transcription drop | [[TAK-901 (drug)]] 0.05 µM 0.285× (z -9.3) |
| [[HCT15 (line)]] | alt | 38.4 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.65× (z +8.7) | [[Digitoxin (drug)]] 5 µM 0.241× (z -9.0) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 39.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.01× (z +11.8) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 37.7 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.63× (z +10.0) | — |
| [[HS-578T (line)]] | alt | 51.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.19× (z +11.1) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 57.2 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.57× (z +12.1) | [[Ixazomib citrate (drug)]] 5 µM 0.297× (z -11.0) |
| [[NCI-H1573 (line)]] | alt | 53.9 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.11× (z +9.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.10× (z +9.2) | — |
| [[NCI-H1792 (line)]] | alt | 31.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.15× (z +12.4) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 26.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.91× (z +9.5) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 35.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.74× (z +10.2) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 66.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.74× (z +8.5) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 53.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.00× (z +9.9) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 30.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.76× (z +9.1) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 18.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.80× (z +8.7) | — |
| [[HEC-1-A (line)]] | alt | 60.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.03× (z +10.4) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 36.1 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.303× (z -9.1) |
| [[Panc 03.27 (line)]] | alt | 41.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.20× (z +9.6) | — |
| [[RKO (line)]] | wt | 43.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.310× (z -9.4) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 33.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.02× (z +8.5) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 43.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.04× (z +8.7) | — |
| [[AN3 CA (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 50.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 29.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 43.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 37.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 44.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 27.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 35.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 62.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 51.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 86.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 31.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 47.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 57.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 26.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3508), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 9 of them with an alert (⚠; 9 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BCDIN3D]] | +0.75 | +0.78 / +0.59 | both halves | 7e-06 |  |
| [[KRCC1]] | +0.71 | +0.81 / +0.50 | both halves | 1e-05 |  |
| [[THOC7]] | +0.69 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[COQ5]] | +0.69 | +0.75 / +0.47 | both halves | 2e-05 |  |
| [[CCAR1]] | +0.69 | +0.71 / +0.63 | both halves | 7e-06 |  |
| [[MCTS1]] | +0.67 | +0.74 / +0.30 | both halves | 2e-04 |  |
| [[SMIM19]] | +0.66 | +0.75 / +0.44 | both halves | 3e-05 |  |
| [[TRMT13]] | +0.66 | +0.73 / +0.44 | both halves | 3e-05 |  |
| [[LINC00174]] | +0.66 | +0.78 / +0.40 | both halves | 5e-05 |  |
| [[RAB30-DT]] | +0.65 | +0.76 / +0.39 | both halves | 6e-05 |  |
| [[MZF1-AS1]] | +0.64 | +0.82 / +0.25 | both halves | 4e-04 |  |
| [[RAD50]] | +0.64 | +0.79 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CABLES2]] | -0.64 | -0.58 / -0.38 | both halves | 7e-05 |  |
| [[IGSF8]] | -0.63 | -0.67 / -0.33 | both halves | 1e-04 |  |
| [[EFNA4]] | -0.62 | -0.57 / -0.31 | both halves | 2e-04 |  |
| [[SLC27A1]] | -0.60 | -0.69 / -0.27 | both halves | 3e-04 |  |
| [[AZIN2]] | -0.60 | -0.53 / -0.33 | both halves | 1e-04 |  |
| [[GNB2]] | -0.60 | -0.65 / -0.30 | both halves | 2e-04 |  |
| [[EFNA3]] | -0.59 | -0.60 / -0.33 | both halves | 1e-04 |  |
| [[MAST3]] | -0.59 | -0.66 / -0.21 | both halves | 7e-04 |  |
| [[PEDS1]] | -0.58 | -0.63 / -0.26 | both halves | 4e-04 |  |
| [[SAP130]] | -0.58 | -0.70 / -0.40 | both halves | 4e-05 |  |
| [[L2HGDH]] | -0.58 | -0.60 / -0.26 | both halves | 3e-04 | pathway: Aerobic respiration and respiratory electron transport |
| [[SNN]] | -0.57 | -0.52 / -0.22 | both halves | 6e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TIMMDC1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 148]]; 30 genes; this gene is in the **+** arm (projection on the module's main direction 0.683). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-21.7, 7.9); signed map (13.3, -26.3). **Vector** length 72.7, 18.3% of its response variance represented; |z| ≥ 3 in 1,033 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +6.3 | +5.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.6 | +5.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.5 | +5.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.9 | +4.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | +3.8 | +5.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.0 | +0.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.9 | +4.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.6 | +0.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.6 | +0.1 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | -4.9 | +4.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | -4.7 | +4.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -4.2 | -8.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.7 | +1.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -3.5 | +5.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.9 | -3.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.9 | +1.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.9 | -1.7 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.3 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | translocase of inner mitochondrial membrane domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q13.33 — chr3:119,498,547-119,525,090 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ22597; previously C3orf1 |
| Gene groups (HGNC) | Mitochondrial respiratory chain complex assembly factors; Tim17 family |
| Reactome | 3 pathways, smallest: Complex I biogenesis; Respiratory electron transport; Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NPL8](https://www.uniprot.org/uniprotkb/Q9NPL8) (Complex I assembly factor TIMMDC1, mitochondrial):

> Chaperone protein involved in the assembly of the mitochondrial NADH:ubiquinone oxidoreductase complex (complex I). Participates in constructing the membrane arm of complex I.

**Summary**, from NCBI Gene [51300](https://www.ncbi.nlm.nih.gov/gene/51300):

> Predicted to be involved in mitochondrial respiratory chain complex I assembly. Located in mitochondrion and nucleoplasm. Implicated in nuclear type mitochondrial complex I deficiency 31. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:1321](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1321) · Entrez [51300](https://www.ncbi.nlm.nih.gov/gene/51300) · UniProt [Q9NPL8](https://www.uniprot.org/uniprotkb/Q9NPL8) · Ensembl [ENSG00000113845](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000113845)

## Data

Gene col 3508: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3508); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3508, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3508]; `tensor/DDL_lfc|DDL_z.npy` [3508]; `embed/gene_vectors.npy` [3508]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3508 or target_col == 3508). Every well: [[TIMMDC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TIMMDC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
