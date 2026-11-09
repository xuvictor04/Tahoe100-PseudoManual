---
symbol: "CERK"
type: "gene"
col: 1958
ensembl_id: "ENSG00000100422"
name: "ceramide kinase"
location: "22q13.31"
module: 34
arm: "+"
pooled_cpm: 36.25
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 21
n_dd_up_clean: 3
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# CERK

*ceramide kinase* — 22q13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 1.52× (z +8.1, q 4e-13, up in 31 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.440× (z -22.0, q 0e+00, down in 41 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARAP1]] (+0.56, fdr 1e-05), [[LINC02210-CRHR1]] (+0.54, fdr 1e-05), [[CELSR1]] (+0.53, fdr 1e-05); moves opposite to [[PTPN2]] (-0.60, fdr 1e-05), [[ZNF644]] (-0.54, fdr 1e-05), [[TIGD2]] (-0.52, fdr 1e-05).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1958.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.52×** | +8.1 | 4e-13 | 31/48 (LoVo, SW480, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.46×** | +7.3 | 9e-11 | 22/43 (LOX-IMVI, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.39×** | +4.6 | 9e-04 | 20/47 (COLO 205, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.37×** | +4.4 | 0.002 | 19/47 (A549, C32, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.25×** | +4.3 | 0.002 | 22/45 (HOP62, KATO III, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~5% here) |
| [[Radotinib (drug)]] 5 µM |  | 1.15× | +3.9 | 0.011 | 15/48 (NCI-H23, NCI-H460, …) | top dose only |  |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.19× | +3.4 | 0.048 | 8/47 (HepG2/C3A, A-172, …) | top dose only |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.40×** | +3.4 | 0.048 | 8/41 (HOP62, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.19× | +3.2 | 0.091 | 16/42 (LOX-IMVI, A-172, …) | inconsistent across doses | composition shift |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | 1.12× | +3.1 | 0.12 | 13/48 (C32, MIA PaCa-2, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1958.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.440×** | -22.0 | 0e+00 | 41/47 (C32, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.378×** | -18.1 | 0e+00 | 37/48 (SNU-1, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.427×** | -16.4 | 0e+00 | 43/48 (SW480, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.448×** | -15.5 | 0e+00 | 43/48 (SW480, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.375×** | -13.5 | 1e-39 | 39/47 (A549, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.531×** | -12.2 | 3e-32 | 40/48 (PANC-1, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.554×** | -11.4 | 4e-28 | 32/48 (C32, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.599×** | -9.9 | 3e-21 | 31/47 (NCI-H23, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.643×** | -8.2 | 2e-14 | 32/47 (SNU-1, CHP-212, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.740×** | -8.0 | 7e-14 | 28/48 (MIA PaCa-2, PANC-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.675×** | -7.6 | 2e-12 | 29/48 (SW480, A549, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.686×** | -7.3 | 2e-11 | 33/48 (NCI-H460, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.704×** | -6.8 | 6e-10 | 27/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.777×** | -6.6 | 1e-09 | 29/48 (A549, HepG2/C3A, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.712×** | -6.3 | 1e-08 | 26/48 (C32, CHP-212, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.591×** | -5.3 | 4e-06 | 26/49 (SNU-1, HT-29, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.782×** | -4.7 | 8e-05 | 21/48 (A549, NCI-H460, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.676×** | -3.9 | 0.002 | 18/47 (RKO, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.843× | -3.0 | 0.059 | 12/48 (CFPAC-1, NCI-H1792, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 0.851× | -3.0 | 0.071 | 15/47 (AsPC-1, RPMI-7951, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.30 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1958. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 24.8 | 1 (1 ⚠) | 11 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.94× (z +9.3) ⚠ cell-cycle shift, explains ~24% of this change | [[Homoharringtonine (drug)]] 5 µM 0.336× (z -15.2) |
| [[PANC-1 (line)]] | alt | 32.8 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -21.9) |
| [[A549 (line)]] | wt | 51.5 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -20.4) |
| [[SNU-1 (line)]] | wt | 64.4 | 0 | 8 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0225× (z -25.8) |
| [[SW480 (line)]] | alt | 48.8 | 0 | 8 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.237× (z -17.6) |
| [[C32 (line)]] | wt | 69.1 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.143× (z -22.1) |
| [[CHP-212 (line)]] | wt | 159 | 0 | 7 (6 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.113× (z -13.5) ⚠ toxic; cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.233× (z -9.4) |
| [[A-427 (line)]] | wt | 23.8 | 0 | 4 | — | [[Harringtonine (drug)]] 5 µM 0.192× (z -10.8) |
| [[AsPC-1 (line)]] | alt | 36.6 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -21.9) |
| [[HOP62 (line)]] | alt | 47.3 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.466× (z -12.3) |
| [[Hs 766T (line)]] | wt | 46.2 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.286× (z -14.9) |
| [[MIA PaCa-2 (line)]] | alt | 30.9 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.194× (z -12.6) |
| [[SNU-423 (line)]] | alt | 52.6 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -13.4) |
| [[A-172 (line)]] | wt | 33.0 | 0 | 3 | — | [[Harringtonine (drug)]] 5 µM 0.165× (z -14.1) |
| [[J82 (line)]] | alt | 30.3 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.409× (z -10.1) |
| [[NCI-H2030 (line)]] | alt | 30.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -15.2) |
| [[CFPAC-1 (line)]] | alt | 25.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -13.9) |
| [[HCT15 (line)]] | alt | 71.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -12.5) |
| [[HEC-1-A (line)]] | alt | 32.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.438× (z -10.5) |
| [[hTERT-HPNE (line)]] | wt | 52.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.338× (z -12.2) |
| [[NCI-H1573 (line)]] | alt | 61.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.334× (z -13.0) |
| [[NCI-H2347 (line)]] | alt | 19.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.298× (z -13.3) |
| [[Panc 03.27 (line)]] | alt | 18.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.329× (z -9.7) |
| [[SW 900 (line)]] | alt | 62.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.439× (z -10.4) |
| [[C-33 A (line)]] | alt | 38.3 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.276× (z -8.9) |
| [[COLO 205 (line)]] | alt | 41.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.370× (z -9.4) |
| [[HT-29 (line)]] | alt | 27.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -11.4) |
| [[KATO III (line)]] | alt | 34.2 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.309× (z -10.2) |
| [[LoVo (line)]] | wt | 29.8 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.377× (z -9.1) |
| [[LOX-IMVI (line)]] | wt | 24.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.55× (z +8.9) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 29.3 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.289× (z -10.5) |
| [[NCI-H23 (line)]] | alt | 18.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.134× (z -12.2) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 32.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -13.6) |
| [[RPMI-7951 (line)]] | alt | 27.6 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.196× (z -10.2) |
| [[SHP-77 (line)]] | alt | 52.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.272× (z -10.6) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 16.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.175× (z -12.9) |
| [[A498 (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 35.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 85.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 45.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 43.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 51.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 39.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1958), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARAP1]] | +0.56 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[LINC02210-CRHR1]] | +0.54 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[CELSR1]] | +0.53 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[NOL4L]] | +0.52 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[BACE2]] | +0.51 | +0.61 / +0.42 | both halves | 4e-05 |  |
| [[MBOAT7]] | +0.51 | +0.43 / +0.64 | both halves | 3e-05 |  |
| [[DNAJC5]] | +0.51 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[CASTOR2]] | +0.51 | +0.37 / +0.51 | both halves | 8e-05 |  |
| [[DPP9]] | +0.51 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[LTBP4]] | +0.51 | +0.56 / +0.45 | both halves | 3e-05 |  |
| [[LAT]] | +0.50 | +0.45 / +0.56 | both halves | 3e-05 |  |
| [[TMEM255B]] | +0.50 | +0.56 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTPN2]] | -0.60 | -0.51 / -0.56 | both halves | 1e-05 |  |
| [[ZNF644]] | -0.54 | -0.52 / -0.58 | both halves | 1e-05 |  |
| [[TIGD2]] | -0.52 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[GBP1]] | -0.51 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[EPSTI1]] | -0.50 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[TLR3]] | -0.50 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[PSMB8]] | -0.50 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[FNDC3A]] | -0.48 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[DTX3L]] | -0.48 | -0.52 / -0.43 | both halves | 3e-05 |  |
| [[DNAH5]] | -0.48 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[HERC6]] | -0.48 | -0.49 / -0.42 | both halves | 4e-05 |  |
| [[PUDP]] | -0.48 | -0.48 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises CERK's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CACNB4]] | B | CACNB4 activity raises CERK's level | lines that do not express CACNB4 (8) vs lines expressing it (42) | 1.27× lower at baseline in the lines without CACNB4 | 0.045 | ⚠ within organs, on part of the lines; also absent: HECTD2, RHBDL3, CERCAM; maybe low, not absent |
| [[CIB2]] | B | CIB2 activity lowers CERK's level | lines that do not express CIB2 (15) vs lines expressing it (35) | 1.12× higher at baseline in the lines without CIB2 | 0.070 | ⚠ within organs, on part of the lines; also absent: HID1, ENSG00000266869, FAM169A; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.374). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (48.7, -1.2); signed map (-26.1, 26.9). **Vector** length 89.5, 21.4% of its response variance represented; |z| ≥ 3 in 1,162 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +8.1 | +8.1 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.7 | -0.1 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.6 | -2.5 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.9 | +0.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +2.6 | -1.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.3 | -0.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.3 | +4.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.3 | +0.7 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | +2.1 | +3.1 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -6.2 | -11.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.3 | -18.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.3 | -6.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -3.1 | -8.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.0 | -2.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.9 | -2.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.7 | -4.7 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.7 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | ceramide kinase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.31 — chr22:46,684,410-46,738,252 (-) |
| Ensembl biotype | protein_coding |
| Also known as | hCERK, FLJ23239, dA59H18.3, DKFZp434E0211, FLJ21430, KIAA1646, LK4, dA59H18.2 |
| Gene groups (HGNC) | SPHK, AGK, CERK lipid kinase family |
| Reactome | 4 pathways, smallest: Glycosphingolipid biosynthesis; Glycosphingolipid metabolism; Sphingolipid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TCT0](https://www.uniprot.org/uniprotkb/Q8TCT0) (Ceramide kinase):

> Catalyzes specifically the phosphorylation of ceramide to form ceramide 1-phosphate. Acts efficiently on natural and analog ceramides (C6, C8, C16 ceramides, and C8-dihydroceramide), to a lesser extent on C2-ceramide and C6-dihydroceramide, but not on other lipids, such as various sphingosines. Shows a greater preference for D-erythro isomer of ceramides. Binds phosphoinositides.

**Summary**, from NCBI Gene [64781](https://www.ncbi.nlm.nih.gov/gene/64781):

> CERK converts ceramide to ceramide 1-phosphate (C1P), a sphingolipid metabolite. Both CERK and C1P have been implicated in various cellular processes, including proliferation, apoptosis, phagocytosis, and inflammation (Kim et al., 2006 [PubMed 16488390]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:19256](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19256) · Entrez [64781](https://www.ncbi.nlm.nih.gov/gene/64781) · UniProt [Q8TCT0](https://www.uniprot.org/uniprotkb/Q8TCT0) · Ensembl [ENSG00000100422](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100422)

## Data

Gene col 1958: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1958); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1958, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1958]; `tensor/DDL_lfc|DDL_z.npy` [1958]; `embed/gene_vectors.npy` [1958]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1958 or target_col == 1958). Every well: [[CERK — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CERK.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
