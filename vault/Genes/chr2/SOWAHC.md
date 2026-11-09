---
symbol: "SOWAHC"
type: "gene"
col: 12538
ensembl_id: "ENSG00000198142"
name: "sosondowah ankyrin repeat domain family member C"
location: "2q13"
module: 101
arm: "+"
pooled_cpm: 29.04
n_lines_expressing: 48
n_dd_up: 21
n_dd_down: 26
n_dd_up_clean: 14
n_dd_down_clean: 24
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/101"]
generated_by: "tahoemap"
---

# SOWAHC

*sosondowah ankyrin repeat domain family member C* — 2q13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (7 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 2.30× (z +11.9, q 5e-30, up in 33 of 46 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 1.91× (z +9.3, q 5e-18, up in 31 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.537× (z -8.9, q 2e-16, down in 28 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Cobimetinib (drug)]] 5 µM: 0.538× (z -8.6, q 3e-15, down in 28 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SEPTIN10]] (+0.68, fdr 7e-06, ⚠ same locus), [[FAM83G]] (+0.67, fdr 7e-06), [[EGR3]] (+0.66, fdr 7e-06), [[MCL1]] (+0.66, fdr 7e-06); moves opposite to [[TNRC6A]] (-0.58, fdr 1e-05), [[CNNM2]] (-0.58, fdr 1e-05), [[RCOR3]] (-0.57, fdr 1e-05).
> It is in [[Module 101]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[ABL1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 7 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12538.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **2.30×** | +11.9 | 5e-30 | 33/46 (NCI-H460, PANC-1, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.91×** | +9.3 | 5e-18 | 31/45 (NCI-H1573, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.70×** | +7.6 | 5e-12 | 30/45 (MIA PaCa-2, C32, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.63×** | +7.0 | 4e-10 | 27/46 (SW480, NCI-H460, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.58×** | +6.6 | 6e-09 | 26/46 (NCI-H1792, LOX-IMVI, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.37×** | +6.5 | 1e-08 | 23/45 (MIA PaCa-2, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Abemaciclib (drug)]] 5 µM |  | **2.13×** | +5.7 | 1e-06 | 23/46 (NCI-H460, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.44×** | +4.8 | 1e-04 | 25/44 (NCI-H460, A549, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.36×** | +4.4 | 5e-04 | 21/46 (SK-MEL-2, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.36×** | +4.4 | 6e-04 | 17/46 (SK-MEL-2, SW480, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.21×** | +3.9 | 0.004 | 17/46 (A-172, SK-MEL-2, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **1.31×** | +3.8 | 0.008 | 16/42 (NCI-H1573, NCI-H2030, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **1.29×** | +3.7 | 0.010 | 15/41 (NCI-H1792, SW480, …) | inconsistent across doses | composition shift; position effect removed |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.60×** | +3.5 | 0.017 | 12/45 (PANC-1, A498, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.26×** | +3.3 | 0.033 | 14/46 (SW480, SK-MEL-2, …) | rises with dose |  |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.05 µM |  | **1.26×** | +3.3 | 0.038 | 9/46 (NCI-H2030, NCI-H460, …) | all doses, flat | position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.25×** | +3.2 | 0.046 | 13/45 (LOX-IMVI, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[4EGI-1 (drug)]] 5 µM |  | **1.51×** | +3.1 | 0.059 | 7/43 (AsPC-1, SW480, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Naproxen (drug)]] 0.5 µM |  | **1.24×** | +3.1 | 0.059 | 8/46 (A-427, LOX-IMVI, …) | all doses, flat | position effect removed |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM |  | 1.16× | +3.1 | 0.059 | 7/46 (NCI-H460, LOX-IMVI, …) | all doses, flat | position effect removed |
| [[Naproxen (drug)]] 5 µM |  | **1.23×** | +2.9 | 0.099 | 12/45 (A-172, MIA PaCa-2, …) | all doses, flat | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12538.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.537×** | -8.9 | 2e-16 | 28/44 (H4, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.538×** | -8.6 | 3e-15 | 28/45 (NCI-H23, SNU-423, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM |  | **0.608×** | -8.2 | 6e-14 | 35/46 (NCI-H23, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.647×** | -7.7 | 2e-12 | 34/46 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.588×** | -7.6 | 3e-12 | 35/47 (NCI-H23, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.597×** | -7.4 | 1e-11 | 28/46 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.609×** | -6.9 | 6e-10 | 29/45 (HepG2/C3A, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.690×** | -6.7 | 1e-09 | 28/46 (SW480, CFPAC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **0.664×** | -6.5 | 6e-09 | 35/46 (NCI-H23, HepG2/C3A, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | **0.729×** | -6.4 | 8e-09 | 32/46 (AsPC-1, COLO 205, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM |  | **0.449×** | -6.0 | 9e-08 | 26/45 (RKO, AsPC-1, …) | top dose only | cell-cycle shift (explains ~6% here); noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.645×** | -5.9 | 1e-07 | 25/46 (A-427, SW480, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.674×** | -5.7 | 6e-07 | 27/45 (NCI-H23, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.658×** | -5.6 | 1e-06 | 25/46 (NCI-H23, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.776×** | -5.1 | 2e-05 | 21/46 (NCI-H23, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.779×** | -5.0 | 2e-05 | 25/46 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12538. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 39.1 | 0 | 8 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.492× (z -17.9) ⚠ position not correctable · without an alert: [[Cobimetinib (drug)]] 5 µM 0.188× (z -11.4) |
| [[LoVo (line)]] | wt | 66.8 | 0 | 6 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.175× (z -11.6) |
| [[NCI-H460 (line)]] | wt | 46.6 | 3 (1 ⚠) | 2 | [[c-Kit-IN-1 (drug)]] 0.05 µM 6.27× (z +16.4) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.47× (z +11.5) | [[Trametinib (drug)]] 0.5 µM 0.407× (z -10.1) |
| [[AsPC-1 (line)]] | alt | 84.4 | 1 (1 ⚠) | 3 | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.96× (z +9.8) ⚠ unreliable plate only | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM 0.259× (z -9.7) |
| [[NCI-H1573 (line)]] | alt | 44.8 | 4 (2 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 5.10× (z +10.3) | — |
| [[NCI-H1792 (line)]] | alt | 22.1 | 3 (1 ⚠) | 1 (1 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 6.33× (z +11.8) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.75× (z +9.1) | [[Adagrasib (drug)]] 0.05 µM 0.593× (z -11.1) ⚠ position not correctable |
| [[A-172 (line)]] | wt | 28.8 | 0 | 3 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.220× (z -11.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.452× (z -8.8) |
| [[CFPAC-1 (line)]] | alt | 55.6 | 3 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 4.34× (z +10.6) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.49× (z +9.2) | — |
| [[H4 (line)]] | wt | 23.2 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0524× (z -14.5) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 19.4 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.18× (z +14.6) | [[Adagrasib (drug)]] 0.05 µM 0.616× (z -10.4) ⚠ position not correctable |
| [[PANC-1 (line)]] | alt | 29.4 | 1 (1 ⚠) | 2 (1 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 4.54× (z +13.9) ⚠ unreliable plate only | [[Digitoxin (drug)]] 5 µM 0.324× (z -10.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.387× (z -8.8) |
| [[A549 (line)]] | wt | 23.3 | 1 (1 ⚠) | 1 | [[c-Kit-IN-1 (drug)]] 0.05 µM 4.85× (z +11.0) ⚠ unreliable plate only | [[Cobimetinib (drug)]] 5 µM 0.284× (z -8.5) |
| [[C32 (line)]] | wt | 11.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.09× (z +11.8) | — |
| [[LOX-IMVI (line)]] | wt | 39.6 | 1 (1 ⚠) | 1 | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.78× (z +10.5) ⚠ unreliable plate only | [[Cobimetinib (drug)]] 5 µM 0.287× (z -9.4) |
| [[NCI-H2030 (line)]] | alt | 37.8 | 0 | 2 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.483× (z -17.6) ⚠ position not correctable · without an alert: [[Cobimetinib (drug)]] 5 µM 0.280× (z -8.6) |
| [[A498 (line)]] | wt | 25.6 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 4.91× (z +13.6) ⚠ unreliable plate only | — |
| [[COLO 205 (line)]] | alt | 22.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0721× (z -12.2) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 38.0 | 0 | 1 | — | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.176× (z -9.4) |
| [[HOP62 (line)]] | alt | 28.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +11.1) | — |
| [[Hs 766T (line)]] | wt | 15.5 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 7.03× (z +9.2) ⚠ unreliable plate only | — |
| [[KATO III (line)]] | alt | 19.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0927× (z -14.2) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 24.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.180× (z -10.0) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 17.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.89× (z +9.7) | — |
| [[SK-MEL-2 (line)]] | alt | 27.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.73× (z +11.9) | — |
| [[SNU-423 (line)]] | alt | 13.0 | 0 | 1 | — | [[Cobimetinib (drug)]] 5 µM 0.132× (z -10.8) |
| [[SW480 (line)]] | alt | 22.5 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.92× (z +8.6) | — |
| [[A-427 (line)]] | wt | 24.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.59 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 24.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.27 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 17.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12538), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEPTIN10]] | +0.68 | +0.65 / +0.69 | both halves | 7e-06 | STRING 534; ⚠ same locus (0.2 kb: neighbours can correlate without regulation) |
| [[FAM83G]] | +0.67 | +0.67 / +0.67 | both halves | 7e-06 |  |
| [[EGR3]] | +0.66 | +0.70 / +0.59 | both halves | 7e-06 |  |
| [[MCL1]] | +0.66 | +0.72 / +0.62 | both halves | 7e-06 |  |
| [[SERPINB8]] | +0.65 | +0.73 / +0.66 | both halves | 7e-06 |  |
| [[ITGA2]] | +0.65 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[LINC00659]] | +0.64 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[LINC00941]] | +0.64 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[NOP14-AS1]] | +0.64 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[TTPAL]] | +0.64 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[SPRY4]] | +0.63 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[VASP]] | +0.63 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[PHLDA1]] | +0.63 | +0.67 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TNRC6A]] | -0.58 | -0.62 / -0.56 | both halves | 1e-05 |  |
| [[CNNM2]] | -0.58 | -0.54 / -0.59 | both halves | 1e-05 |  |
| [[RCOR3]] | -0.57 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[MBIP]] | -0.56 | -0.54 / -0.56 | both halves | 1e-05 |  |
| [[AMBRA1]] | -0.56 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[HOXA3]] | -0.56 | -0.57 / -0.47 | both halves | 2e-05 |  |
| [[ERP29]] | -0.55 | -0.52 / -0.57 | both halves | 1e-05 |  |
| [[ARL6IP5]] | -0.55 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[HSF2]] | -0.55 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[RSBN1L]] | -0.55 | -0.56 / -0.51 | both halves | 1e-05 |  |
| [[ATF6B]] | -0.54 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[ZFP14]] | -0.53 | -0.59 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 5, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ABL1]] | B | ABL1 activity raises SOWAHC's level | compounds that target ABL1: 4 of 6 lower it (Flumatinib, NG25, Ponatinib, Radotinib) | 67% of the class's compounds vs 4.2% of all compounds | 0.037 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[FAM110C]] | B | FAM110C activity raises SOWAHC's level | lines that do not express FAM110C (26) vs lines expressing it (24) | 1.60× lower at baseline in the lines without FAM110C | 0.039 | ⚠ within organs, on part of the lines; also absent: PRR15-DT, PRR15, PLEKHG6 |
| [[EPHA2]] | B | EPHA2 activity raises SOWAHC's level | lines that do not express EPHA2 (11) vs lines expressing it (39) | 1.61× lower at baseline in the lines without EPHA2 | 0.060 | ⚠ within organs, on part of the lines; also absent: RHOD, LINC00857, ABLIM2; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity raises SOWAHC's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.2% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ITGA2]] | B | ITGA2 activity raises SOWAHC's level | lines that do not express ITGA2 (11) vs lines expressing it (39) | 1.51× lower at baseline in the lines without ITGA2 | 0.098 | ⚠ within organs, on part of the lines; also absent: GPR39, ATXN1-AS1, MET |
| [[KDM7A-DT]] | C | KDM7A-DT activity raises SOWAHC's level | lines that do not express KDM7A-DT (4) vs lines expressing it (46) | 2.25× lower at baseline in the lines without KDM7A-DT | 0.055 | ⚠ few lines (4 vs 46); across organs; also absent: FBXO6, MCF2L2, KIAA1522; maybe low, not absent; co-absent with the target |
| [[NABP1]] | C | NABP1 activity raises SOWAHC's level | lines that do not express NABP1 (4) vs lines expressing it (46) | 2.44× lower at baseline in the lines without NABP1 | 0.066 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: PHF11, LACC1, NMI; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 101]]; 46 genes; every member is in the + arm (projection on the module's main direction 0.681). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (37.6, -2.4); signed map (4.7, 33.2). **Vector** length 130, 36.4% of its response variance represented; |z| ≥ 3 in 1,330 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.7 | +11.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.9 | +7.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.0 | +9.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +4.9 | +5.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.5 | +6.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.3 | +7.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.7 | +1.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.2 | +3.5 |
| fall | [[Cobimetinib (drug)]] 5 µM |  | -7.6 | -8.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -7.4 | -7.7 |
|  | [[Trametinib (drug)]] 5 µM |  | -7.1 | -8.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | -6.9 | -6.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -6.7 | -7.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -6.5 | -6.9 |

## What is on record

|  |  |
|---|---|
| Name | sosondowah ankyrin repeat domain family member C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q13 — chr2:109,614,364-109,618,990 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ21870; previously C2orf26, ANKRD57 |
| Gene groups (HGNC) | Ankyrin repeat domain containing |
| Hallmark sets | ADIPOGENESIS |
| Reactome | 6 pathways, smallest: RHOF GTPase cycle; RHOB GTPase cycle; RHOA GTPase cycle |
| Matched by | ensembl_id |

UniProt [Q53LP3](https://www.uniprot.org/uniprotkb/Q53LP3) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:26149](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26149) · Entrez [65124](https://www.ncbi.nlm.nih.gov/gene/65124) · UniProt [Q53LP3](https://www.uniprot.org/uniprotkb/Q53LP3) · Ensembl [ENSG00000198142](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198142)

## Data

Gene col 12538: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12538); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12538, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12538]; `tensor/DDL_lfc|DDL_z.npy` [12538]; `embed/gene_vectors.npy` [12538]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12538 or target_col == 12538). Every well: [[SOWAHC — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SOWAHC.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
