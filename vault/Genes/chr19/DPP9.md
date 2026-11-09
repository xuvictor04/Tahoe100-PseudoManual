---
symbol: "DPP9"
type: "gene"
col: 6590
ensembl_id: "ENSG00000142002"
name: "dipeptidyl peptidase 9"
location: "19p13.3"
module: 52
arm: "+"
pooled_cpm: 57.16
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 15
n_dd_up_clean: 5
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/052"]
generated_by: "tahoemap"
---

# DPP9

*dipeptidyl peptidase 9* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.57× (z +10.1, q 2e-21, up in 38 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.31× (z +6.0, q 5e-07, up in 26 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.664× (z -12.9, q 3e-35, down in 38 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[YKT6]] (+0.74, fdr 7e-06), [[GOLGA3]] (+0.72, fdr 7e-06), [[TPD52L2]] (+0.70, fdr 7e-06); moves opposite to [[PUM1]] (-0.64, fdr 4e-05), [[CEBPD]] (-0.64, fdr 1e-05), [[ZNF608]] (-0.62, fdr 7e-06).
> It sits in the **+** arm of [[Module 052]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CXCL3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 8 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6590.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.57×** | +10.1 | 2e-21 | 38/47 (RPMI-7951, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.44×** | +7.9 | 8e-13 | 25/40 (A549, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.31×** | +6.0 | 5e-07 | 26/48 (SW480, A-172, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.18× | +5.3 | 1e-05 | 20/48 (HT-29, SW480, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.27×** | +5.3 | 1e-05 | 24/47 (HT-29, SW 900, …) | all doses, stronger at high dose | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.25×** | +5.0 | 4e-05 | 24/48 (HT-29, NCI-H460, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.23×** | +4.3 | 0.001 | 18/42 (KATO III, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.20×** | +4.1 | 0.002 | 16/47 (HT-29, SW 900, …) | all doses, stronger at high dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.20×** | +4.1 | 0.002 | 23/48 (HT-29, SW480, …) | all doses, stronger at high dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.28×** | +4.0 | 0.004 | 20/48 (HT-29, SW 900, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | 1.20× | +3.9 | 0.005 | 15/47 (HT-29, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~36% of this change | 1.17× | +3.6 | 0.017 | 17/48 (SHP-77, NCI-H2347, …) | inconsistent across doses | low cells (technical?) |
| [[TAK-901 (drug)]] 5 µM |  | **1.31×** | +3.2 | 0.062 | 19/49 (H4, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.15× | +3.0 | 0.092 | 12/48 (NCI-H2030, HT-29, …) | inconsistent across doses | position effect removed |
| [[Raltitrexed (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.10× | +3.0 | 0.092 | 1/49 (SHP-77) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 14 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6590.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.664×** | -12.9 | 3e-35 | 38/47 (J82, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.556×** | -12.6 | 7e-34 | 38/48 (J82, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.699×** | -11.3 | 3e-27 | 41/48 (NCI-H2347, A-172, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.740×** | -9.5 | 3e-19 | 35/48 (HS-578T, J82, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~17% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.673×** | -8.8 | 1e-16 | 39/48 (CFPAC-1, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.749×** | -6.4 | 1e-08 | 28/48 (HEC-1-A, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.937× | -5.0 | 5e-05 | 5/49 (MIA PaCa-2, NCI-H2030, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.794×** | -4.9 | 6e-05 | 22/47 (AsPC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.804×** | -4.9 | 7e-05 | 24/48 (HS-578T, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.810×** | -4.7 | 2e-04 | 23/48 (MIA PaCa-2, HOP62, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~20% of this change | **0.804×** | -4.7 | 2e-04 | 23/47 (H4, HT-29, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.854× | -4.2 | 0.001 | 17/48 (MIA PaCa-2, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.831×** | -4.1 | 0.002 | 18/48 (Panc 03.27, J82, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.831×** | -4.1 | 0.002 | 19/48 (HOP62, PANC-1, …) | inconsistent across doses | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.836× | -4.0 | 0.003 | 22/48 (HOP62, AsPC-1, …) | top dose only | composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **0.832×** | -3.9 | 0.003 | 20/48 (J82, MIA PaCa-2, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | 0.855× | -3.5 | 0.013 | 16/48 (NCI-H2347, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 0.850× | -3.5 | 0.014 | 15/48 (MIA PaCa-2, NCI-H23, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.847× | -3.4 | 0.015 | 16/48 (MIA PaCa-2, AsPC-1, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.858× | -3.4 | 0.015 | 15/49 (MIA PaCa-2, AsPC-1, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.884× | -3.3 | 0.020 | 14/48 (MIA PaCa-2, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6590. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 117 | 0 | 8 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.459× (z -12.3) ⚠ cell-cycle shift, explains ~20% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.460× (z -12.2) |
| [[MIA PaCa-2 (line)]] | alt | 134 | 0 | 8 (4 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.607× (z -17.3) ⚠ position not correctable · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.467× (z -10.5) |
| [[A-172 (line)]] | wt | 82.4 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.461× (z -13.3) |
| [[J82 (line)]] | alt | 80.6 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.260× (z -22.5) |
| [[HEC-1-A (line)]] | alt | 45.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.381× (z -13.2) |
| [[HOP62 (line)]] | alt | 72.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.449× (z -12.0) |
| [[A498 (line)]] | wt | 63.2 | 0 | 2 | — | [[Selinexor (drug)]] 5 µM 0.576× (z -10.4) |
| [[A549 (line)]] | wt | 48.3 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.74× (z +8.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.503× (z -8.7) |
| [[HS-578T (line)]] | alt | 91.9 | 0 | 2 | — | [[Selinexor (drug)]] 5 µM 0.483× (z -11.6) |
| [[NCI-H2030 (line)]] | alt | 59.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.486× (z -12.4) |
| [[NCI-H460 (line)]] | wt | 33.6 | 0 | 2 | — | [[Harringtonine (drug)]] 0.5 µM 0.425× (z -9.0) |
| [[PANC-1 (line)]] | alt | 87.6 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.416× (z -10.1) ⚠ cell-cycle shift, explains ~16% of this change |
| [[SHP-77 (line)]] | alt | 35.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.92× (z +8.5) ⚠ toxic; transcription drop | [[Dinaciclib (drug)]] 5 µM 0.270× (z -10.1) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 50.3 | 0 | 2 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.365× (z -8.8) |
| [[A-427 (line)]] | wt | 43.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.251× (z -13.4) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 36.8 | 0 | 1 | — | [[Tucidinostat (drug)]] 0.5 µM 0.364× (z -8.7) |
| [[HCT15 (line)]] | alt | 57.6 | 0 | 1 | — | [[GSK1059615 (drug)]] 0.5 µM 0.173× (z -9.1) |
| [[Hs 766T (line)]] | wt | 87.4 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.573× (z -8.5) |
| [[hTERT-HPNE (line)]] | wt | 54.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.455× (z -9.6) |
| [[KATO III (line)]] | alt | 35.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.55× (z +8.5) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 46.0 | 0 | 1 | — | [[Tucidinostat (drug)]] 5 µM 0.577× (z -8.5) |
| [[LOX-IMVI (line)]] | wt | 55.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.22× (z +8.6) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 36.5 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.275× (z -11.1) |
| [[NCI-H1792 (line)]] | alt | 74.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.411× (z -11.0) |
| [[NCI-H2347 (line)]] | alt | 45.7 | 0 | 1 | — | [[Tucidinostat (drug)]] 5 µM 0.512× (z -10.8) |
| [[RPMI-7951 (line)]] | alt | 66.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.60× (z +9.6) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 40.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.69× (z +9.5) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 37.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.548× (z -8.7) |
| [[SW480 (line)]] | alt | 51.1 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.10× (z +9.2) | — |
| [[AN3 CA (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 28.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 33.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 59.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 31.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 45.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 92.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 58.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 43.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 31.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 50.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 72.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 43.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6590), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YKT6]] | +0.74 | +0.70 / +0.65 | both halves | 7e-06 |  |
| [[GOLGA3]] | +0.72 | +0.69 / +0.77 | both halves | 7e-06 |  |
| [[TPD52L2]] | +0.70 | +0.62 / +0.71 | both halves | 7e-06 |  |
| [[EPN1]] | +0.68 | +0.61 / +0.68 | both halves | 7e-06 |  |
| [[AP1M1]] | +0.68 | +0.72 / +0.57 | both halves | 9e-06 |  |
| [[EHBP1L1]] | +0.66 | +0.67 / +0.58 | both halves | 7e-06 |  |
| [[TMEM104]] | +0.66 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[RER1]] | +0.65 | +0.63 / +0.58 | both halves | 8e-06 |  |
| [[VPS53]] | +0.64 | +0.50 / +0.71 | both halves | 1e-05 |  |
| [[PDCD6]] | +0.63 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[ARHGEF1]] | +0.63 | +0.59 / +0.66 | both halves | 7e-06 |  |
| [[MYO9B]] | +0.62 | +0.65 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PUM1]] | -0.64 | -0.42 / -0.60 | both halves | 4e-05 |  |
| [[CEBPD]] | -0.64 | -0.62 / -0.55 | both halves | 1e-05 |  |
| [[ZNF608]] | -0.62 | -0.61 / -0.63 | both halves | 7e-06 |  |
| [[VAPA]] | -0.62 | -0.46 / -0.56 | both halves | 2e-05 |  |
| [[EPS8]] | -0.61 | -0.58 / -0.64 | both halves | 8e-06 |  |
| [[WAC]] | -0.61 | -0.34 / -0.46 | both halves | 1e-04 |  |
| [[CHIC1]] | -0.61 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[DHFR2]] | -0.59 | -0.54 / -0.64 | both halves | 1e-05 |  |
| [[ABCB7]] | -0.59 | -0.45 / -0.63 | both halves | 3e-05 |  |
| [[SCAMP1-AS1]] | -0.58 | -0.55 / -0.46 | both halves | 3e-05 |  |
| [[WTAP]] | -0.57 | -0.36 / -0.50 | both halves | 1e-04 |  |
| [[PLEKHF2]] | -0.57 | -0.39 / -0.53 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CXCL3]] | B | CXCL3 activity strengthens DPP9's drug response | lines that do not express CXCL3 (14) vs lines expressing it (34) | the lines without CXCL3 respond 0.51× as strongly (z diff +1.45); rises at some drug-doses, falls at others (33% from rises): Dinaciclib 5 µM: 0.97x vs 1.52x (z diff +4.7); Homoharringtonine 5 µM: 0.81x vs 0.60x (z diff +3.3); Harringtonine 5 µM: 0.69x vs 0.51x (z diff +2.1) | 0.068 | ⚠ within organs, on part of the lines; also absent: MGLL, SPTLC3, PCED1B; target measured in part of the lines; rises at some drug-doses, falls at others; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 052]]; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.768). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (9.9, -26.7); signed map (-50.2, 2.3). **Vector** length 115, 30.8% of its response variance represented; |z| ≥ 3 in 1,223 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.8 | +6.0 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +5.2 | +4.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.9 | +5.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +4.8 | +5.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.8 | -0.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.9 | +3.9 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +3.5 | +4.1 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -7.9 | -11.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -7.4 | -8.8 |
|  | [[Selinexor (drug)]] 5 µM |  | -7.0 | -9.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | -6.7 | -12.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.4 | -6.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.1 | -4.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -3.4 | -3.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.4 | -4.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -3.3 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | dipeptidyl peptidase 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:4,674,341-4,724,673 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | DASH family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86TI2](https://www.uniprot.org/uniprotkb/Q86TI2) (Dipeptidyl peptidase 9):

> Dipeptidyl peptidase that cleaves off N-terminal dipeptides from proteins having a Pro or Ala residue at position 2. Acts as a key inhibitor of caspase-1-dependent monocyte and macrophage pyroptosis in resting cells by preventing activation of NLRP1 and CARD8. Sequesters the cleaved C-terminal part of NLRP1 and CARD8, which respectively constitute the active part of the NLRP1 and CARD8 inflammasomes, in a ternary complex, thereby preventing their oligomerization and activation. The dipeptidyl …

**Summary**, from NCBI Gene [91039](https://www.ncbi.nlm.nih.gov/gene/91039):

> This gene encodes a protein that is a member of the S9B family in clan SC of the serine proteases. The protein has been shown to have post-proline dipeptidyl aminopeptidase activity, cleaving Xaa-Pro dipeptides from the N-termini of proteins. Although the activity of this protein is similar to that of dipeptidyl peptidase 4 (DPP4), it does not appear to be membrane bound. In general, dipeptidyl peptidases appear to be involved in the regulation of the activity of their substrates and have been …

**Accessions** — [HGNC:18648](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18648) · Entrez [91039](https://www.ncbi.nlm.nih.gov/gene/91039) · UniProt [Q86TI2](https://www.uniprot.org/uniprotkb/Q86TI2) · Ensembl [ENSG00000142002](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000142002)

## Data

Gene col 6590: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6590); `tables/drug_effects.parquet` (53 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6590, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6590]; `tensor/DDL_lfc|DDL_z.npy` [6590]; `embed/gene_vectors.npy` [6590]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6590 or target_col == 6590). Every well: [[DPP9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DPP9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
