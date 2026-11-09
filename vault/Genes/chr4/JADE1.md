---
symbol: "JADE1"
type: "gene"
col: 1195
ensembl_id: "ENSG00000077684"
name: "jade family PHD finger 1"
location: "4q28.2"
module: 217
arm: "+"
pooled_cpm: 43.12
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 17
n_dd_up_clean: 14
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/217"]
generated_by: "tahoemap"
---

# JADE1

*jade family PHD finger 1* — 4q28.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.36× (z +8.3, q 7e-14, up in 29 of 48 measured lines) ⚠ cell-cycle shift, explains ~84% of this change. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 1.42× (z +6.6, q 9e-09, up in 32 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.540× (z -11.8, q 3e-29, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF608]] (+0.62, fdr 1e-05), [[SETD2]] (+0.62, fdr 1e-05), [[BAZ1B]] (+0.62, fdr 7e-06); moves opposite to [[ARPC1A]] (-0.56, fdr 1e-05), [[UBA6]] (-0.54, fdr 1e-05), [[ARPC2]] (-0.53, fdr 1e-05).
> It is in [[Module 217]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1195.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~84% of this change | **1.36×** | +8.3 | 7e-14 | 29/48 (LS 180, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.42×** | +6.6 | 9e-09 | 32/48 (NCI-H2347, A549, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.31×** | +5.2 | 3e-05 | 27/48 (A549, SW 900, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.29×** | +4.9 | 2e-04 | 21/48 (LS 180, hTERT-HPNE, …) | all doses, flat |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.61×** | +4.8 | 2e-04 | 22/47 (A549, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.28×** | +4.7 | 3e-04 | 21/48 (HOP62, NCI-H1792, …) | all doses, flat |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | 1.18× | +4.4 | 7e-04 | 15/48 (A-427, NCI-H2347, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **1.25×** | +4.3 | 0.001 | 19/48 (LS 180, C32, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~85% of this change | **1.25×** | +4.1 | 0.002 | 24/48 (LS 180, KATO III, …) | all doses, flat | composition shift |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.17× | +4.0 | 0.003 | 9/48 (HEC-1-A, NCI-H460, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.21×** | +4.0 | 0.004 | 14/48 (HEC-1-A, NCI-H460, …) | two highest doses | noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.23×** | +3.9 | 0.004 | 16/47 (A498, BT-474, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.16× | +3.9 | 0.004 | 21/48 (NCI-H2347, LoVo, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.37×** | +3.8 | 0.007 | 16/48 (HEC-1-A, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.21×** | +3.7 | 0.008 | 20/48 (HOP62, A549, …) | all doses, flat |  |
| [[L-Eflornithine (monohydrochloride) (drug)]] 5 µM |  | **1.21×** | +3.7 | 0.008 | 11/48 (PANC-1, NCI-H460, …) | rises with dose | position effect removed |
| [[Budesonide (drug)]] 0.5 µM |  | **1.21×** | +3.6 | 0.009 | 15/48 (HS-578T, NCI-H1792, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.20×** | +3.6 | 0.010 | 13/48 (HEC-1-A, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Triamcinolone (drug)]] 0.5 µM |  | **1.21×** | +3.6 | 0.010 | 13/48 (A549, A498, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.22×** | +3.5 | 0.011 | 17/47 (C32, SW48, …) | all doses, flat | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.20×** | +3.5 | 0.011 | 14/48 (HOP62, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 13 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1195.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.540×** | -11.8 | 3e-29 | 37/48 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.586×** | -10.2 | 5e-22 | 37/48 (HEC-1-A, SW480, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.645×** | -8.4 | 1e-14 | 36/48 (SW480, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.750×** | -5.3 | 2e-05 | 21/40 (SHP-77, C-33 A, …) | top dose only | cell-cycle shift (explains ~13% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.760×** | -5.2 | 2e-05 | 25/48 (A-427, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.749×** | -5.2 | 2e-05 | 23/48 (NCI-H460, SW1417, …) | all doses, flat |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **0.827×** | -5.1 | 3e-05 | 24/48 (LOX-IMVI, A-427, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.769×** | -5.0 | 4e-05 | 23/48 (PANC-1, HT-29, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.776×** | -4.7 | 2e-04 | 22/47 (A-427, NCI-H460, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | 0.842× | -4.6 | 2e-04 | 21/48 (NCI-H460, SHP-77, …) | rises with dose | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.636×** | -4.5 | 3e-04 | 23/48 (NCI-H460, A498, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.792×** | -4.5 | 4e-04 | 22/48 (SHP-77, SNU-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.796×** | -4.3 | 6e-04 | 20/47 (SHP-77, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~37% of this change | **0.649×** | -4.3 | 6e-04 | 19/43 (PANC-1, HEC-1-A, …) | all doses, flat | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 0.05 µM |  | **0.829×** | -3.4 | 0.025 | 9/48 (H4, COLO 205, …) | inconsistent across doses |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 0.841× | -3.3 | 0.031 | 8/47 (SNU-423, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Ivermectin (drug)]] 5 µM |  | 0.854× | -3.0 | 0.072 | 4/48 (SK-MEL-2, RKO, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.781×** | -3.0 | 0.075 | 10/48 (HOP62, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.743×** | -3.0 | 0.075 | 5/48 (HOP62, SW1417, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, +0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1195. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 80.0 | 0 | 7 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.108× (z -17.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.232× (z -11.9) |
| [[A-427 (line)]] | wt | 92.5 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.307× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.371× (z -10.6) |
| [[HEC-1-A (line)]] | alt | 90.5 | 2 (1 ⚠) | 3 | [[Trametinib (drug)]] 5 µM 1.85× (z +8.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Binimetinib (drug)]] 5 µM 1.83× (z +8.7) | [[Panobinostat (drug)]] 5 µM 0.378× (z -12.9) |
| [[C-33 A (line)]] | alt | 77.8 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.202× (z -15.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.279× (z -12.6) |
| [[NCI-H460 (line)]] | wt | 71.6 | 0 | 4 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.353× (z -14.0) ⚠ cell-cycle shift, explains ~46% of this change |
| [[PANC-1 (line)]] | alt | 49.7 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.399× (z -11.2) |
| [[RKO (line)]] | wt | 53.1 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.225× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 32.2 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.227× (z -15.8) |
| [[A498 (line)]] | wt | 66.2 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.482× (z -10.4) ⚠ cell-cycle shift, explains ~46% of this change |
| [[LS 180 (line)]] | wt | 31.0 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +11.9) ⚠ cell-cycle shift, explains ~84% of this change | — |
| [[CFPAC-1 (line)]] | alt | 21.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +9.1) ⚠ cell-cycle shift, explains ~84% of this change | — |
| [[COLO 205 (line)]] | alt | 13.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.86× (z +9.0) ⚠ cell-cycle shift, explains ~84% of this change | — |
| [[HepG2_C3A (line)]] | wt | 27.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.114× (z -12.9) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 31.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +9.3) ⚠ cell-cycle shift, explains ~84% of this change | — |
| [[KATO III (line)]] | alt | 16.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.44× (z +10.6) ⚠ cell-cycle shift, explains ~84% of this change | — |
| [[LoVo (line)]] | wt | 22.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +8.5) ⚠ cell-cycle shift, explains ~84% of this change | — |
| [[LOX-IMVI (line)]] | wt | 35.0 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.478× (z -9.0) ⚠ cell-cycle shift, explains ~73% of this change |
| [[NCI-H1573 (line)]] | alt | 23.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +9.4) ⚠ cell-cycle shift, explains ~84% of this change | — |
| [[NCI-H2030 (line)]] | alt | 52.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +8.6) ⚠ cell-cycle shift, explains ~84% of this change | — |
| [[Panc 03.27 (line)]] | alt | 28.3 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.235× (z -10.4) |
| [[SK-MEL-2 (line)]] | alt | 66.2 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.485× (z -9.0) ⚠ cell-cycle shift, explains ~46% of this change |
| [[SNU-1 (line)]] | wt | 67.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.149× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[A-172 (line)]] | wt | 44.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 45.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 64.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 24.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 25.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 47.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 50.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 24.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 26.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 52.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 40.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 52.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 50.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 60.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 50.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 33.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1195), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF608]] | +0.62 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[SETD2]] | +0.62 | +0.55 / +0.55 | both halves | 1e-05 | pathway: Chromatin modifying enzymes |
| [[BAZ1B]] | +0.62 | +0.58 / +0.59 | both halves | 7e-06 | same gene group |
| [[ZFHX3]] | +0.61 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[NFIB]] | +0.60 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[RNF115]] | +0.59 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[DNAH5]] | +0.59 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[ARL4A]] | +0.58 | +0.60 / +0.66 | both halves | 7e-06 |  |
| [[USP13]] | +0.57 | +0.62 / +0.44 | both halves | 3e-05 |  |
| [[DEPDC1]] | +0.56 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[DIS3L]] | +0.56 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[CNTRL]] | +0.56 | +0.59 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARPC1A]] | -0.56 | -0.63 / -0.50 | both halves | 1e-05 |  |
| [[UBA6]] | -0.54 | -0.62 / -0.50 | both halves | 1e-05 |  |
| [[ARPC2]] | -0.53 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[QSOX1]] | -0.53 | -0.59 / -0.45 | both halves | 3e-05 |  |
| [[F11R]] | -0.51 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[BCAP31]] | -0.51 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[TPMT]] | -0.51 | -0.45 / -0.39 | both halves | 5e-05 |  |
| [[MYO9B]] | -0.51 | -0.61 / -0.37 | both halves | 7e-05 |  |
| [[SNAP23]] | -0.51 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[ZFC3H1]] | -0.50 | -0.56 / -0.49 | both halves | 1e-05 |  |
| [[MLF2]] | -0.50 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[TPD52L2]] | -0.49 | -0.48 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 217]]; 12 genes; every member is in the + arm (projection on the module's main direction 0.691). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-23.9, 5.8); signed map (15.8, 25.6). **Vector** length 119, 32.1% of its response variance represented; |z| ≥ 3 in 1,216 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~70% of this change | +7.6 | +4.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~84% of this change | +7.2 | +8.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~85% of this change | +5.4 | +4.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +5.2 | +6.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | +4.3 | +4.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.1 | +3.9 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +3.8 | +5.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.7 | +4.0 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +3.5 | +4.7 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -5.4 | -10.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | -5.3 | -11.8 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.3 | -8.4 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | -3.8 | -5.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~40% of this change | -3.0 | -5.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.4 | -4.5 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.4 | -3.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.3 | -3.0 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -2.1 | -3.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.9 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | jade family PHD finger 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q28.2 — chr4:128,809,700-128,875,224 (+) |
| Ensembl biotype | protein_coding |
| Also known as | JADE-1; previously PHF17 |
| Gene groups (HGNC) | PHD finger proteins; Jade family PHD fingers |
| Reactome | 3 pathways, smallest: HATs acetylate histones; Chromatin modifying enzymes; Chromatin organization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6IE81](https://www.uniprot.org/uniprotkb/Q6IE81) (Protein Jade-1):

> Scaffold subunit of some HBO1 complexes, which have a histone H4 acetyltransferase activity. Plays a key role in HBO1 complex by directing KAT7/HBO1 specificity towards histone H4 acetylation (H4K5ac, H4K8ac and H4K12ac), regulating DNA replication initiation, regulating DNA replication initiation. May also promote acetylation of nucleosomal histone H4 by KAT5. Promotes apoptosis. May act as a renal tumor suppressor. Negatively regulates canonical Wnt signaling; at least in part, cooperates …

**Summary**, from NCBI Gene [79960](https://www.ncbi.nlm.nih.gov/gene/79960):

> Enables transcription coactivator activity. Contributes to histone acetyltransferase activity. Involved in several processes, including negative regulation of canonical Wnt signaling pathway; regulation of DNA metabolic process; and regulation of cell growth. Acts upstream of or within negative regulation of G1/S transition of mitotic cell cycle. Located in several cellular components, including ciliary basal body; cytosol; and nuclear speck. Part of histone acetyltransferase complex. [provided …

**Accessions** — [HGNC:30027](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30027) · Entrez [79960](https://www.ncbi.nlm.nih.gov/gene/79960) · UniProt [Q6IE81](https://www.uniprot.org/uniprotkb/Q6IE81) · Ensembl [ENSG00000077684](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000077684)

## Data

Gene col 1195: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1195); `tables/drug_effects.parquet` (56 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1195, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1195]; `tensor/DDL_lfc|DDL_z.npy` [1195]; `embed/gene_vectors.npy` [1195]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1195 or target_col == 1195). Every well: [[JADE1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/JADE1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
