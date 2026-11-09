---
symbol: "SPECC1L"
type: "gene"
col: 1843
ensembl_id: "ENSG00000100014"
name: "sperm antigen with calponin homology and coiled-coil domains 1 like"
location: "22q11.23"
module: 18
arm: "+"
pooled_cpm: 106.29
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 8
n_dd_up_clean: 3
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# SPECC1L

*sperm antigen with calponin homology and coiled-coil domains 1 like* — 22q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 1.22× (z +6.1, q 6e-07, up in 24 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 1.20× (z +5.4, q 1e-05, up in 21 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.534× (z -26.7, q 0e+00, down in 39 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRTFB]] (+0.67, fdr 7e-06), [[PDS5A]] (+0.63, fdr 4e-05), [[INPP4A]] (+0.63, fdr 7e-06); moves opposite to [[ZNF490]] (-0.58, fdr 3e-05), [[KLC4]] (-0.54, fdr 1e-05), [[FAM117A]] (-0.52, fdr 6e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 8 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1843.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.22×** | +6.1 | 6e-07 | 24/48 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **1.21×** | +5.8 | 2e-06 | 24/48 (COLO 205, NCI-H2347, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.20×** | +5.4 | 1e-05 | 21/48 (NCI-H23, NCI-H2347, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +5.3 | 2e-05 | 22/48 (SW480, PANC-1, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.18× | +4.9 | 1e-04 | 19/48 (MIA PaCa-2, Panc 03.27, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | 1.18× | +4.8 | 1e-04 | 20/48 (LS 180, NCI-H460, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~65% of this change | 1.17× | +4.7 | 2e-04 | 20/48 (CFPAC-1, HS-578T, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | 1.15× | +4.3 | 0.001 | 12/48 (MIA PaCa-2, A-427, …) | two highest doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | 1.14× | +3.9 | 0.005 | 11/48 (MIA PaCa-2, SK-MEL-2, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~82% of this change | 1.13× | +3.7 | 0.010 | 16/48 (HEC-1-A, HCT15, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.13× | +3.7 | 0.012 | 15/48 (SNU-423, HS-578T, …) | inconsistent across doses |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.25×** | +3.5 | 0.021 | 16/48 (NCI-H2347, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | 1.12× | +3.3 | 0.041 | 10/48 (MIA PaCa-2, NCI-H23, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **1.23×** | +3.3 | 0.041 | 10/48 (C32, HepG2/C3A, …) | top dose only | noisy plate (z scaled) |
| [[Trifluridine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | 1.11× | +3.2 | 0.053 | 5/48 (KATO III, HCT15, …) | inconsistent across doses |  |
| [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | 1.11× | +3.1 | 0.080 | 8/50 (HS-578T, SNU-423, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 7 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1843.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.534×** | -26.7 | 0e+00 | 39/48 (NCI-H460, A-427, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.638×** | -13.5 | 5e-39 | 41/48 (SW480, C-33 A, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.428×** | -13.4 | 2e-38 | 43/49 (LoVo, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.695×** | -10.9 | 1e-25 | 29/48 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.716×** | -9.3 | 2e-18 | 27/45 (SW480, SW48, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.657×** | -6.6 | 4e-09 | 29/48 (RKO, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.842× | -5.2 | 2e-05 | 21/49 (RKO, NCI-H460, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~3% of this change | 0.843× | -5.1 | 2e-05 | 22/48 (SW 1271, NCI-H460, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 0.843× | -4.9 | 5e-05 | 22/47 (NCI-H2030, HepG2/C3A, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.772×** | -4.1 | 0.003 | 15/38 (NCI-H1792, A549, …) | top dose only | noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **0.799×** | -3.5 | 0.023 | 10/47 (A498, KATO III, …) | top dose only | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.891× | -3.3 | 0.038 | 18/44 (C-33 A, A549, …) | all doses, flat | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1843. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 83.5 | 0 | 12 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.341× (z -25.3) |
| [[A-427 (line)]] | wt | 109 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.383× (z -20.6) |
| [[C-33 A (line)]] | alt | 221 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.335× (z -16.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.378× (z -15.1) |
| [[SW480 (line)]] | alt | 138 | 2 (2 ⚠) | 3 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 1.58× (z +9.7) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 0.05 µM 0.395× (z -18.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.437× (z -18.2) |
| [[A549 (line)]] | wt | 91.2 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.432× (z -16.2) |
| [[HEC-1-A (line)]] | alt | 129 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.571× (z -13.7) |
| [[HS-578T (line)]] | alt | 154 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.458× (z -17.1) |
| [[RKO (line)]] | wt | 126 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.282× (z -16.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.222× (z -10.4) |
| [[SNU-1 (line)]] | wt | 129 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.353× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~3% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.488× (z -10.4) |
| [[SW1417 (line)]] | alt | 146 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.467× (z -18.4) |
| [[SW48 (line)]] | wt | 121 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.195× (z -16.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.386× (z -14.8) |
| [[A498 (line)]] | wt | 144 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.324× (z -15.0) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 92.4 | 3 (3 ⚠) | 0 | [[Epirubicin (hydrochloride) (drug)]] 5 µM 2.13× (z +9.8) ⚠ cell-cycle shift, explains ~74% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 119 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.528× (z -13.6) |
| [[NCI-H1573 (line)]] | alt | 117 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.417× (z -17.0) |
| [[NCI-H2030 (line)]] | alt | 145 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.469× (z -16.3) |
| [[SK-MEL-2 (line)]] | alt | 121 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.417× (z -16.2) |
| [[SW 1271 (line)]] | alt | 103 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0768× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~3% of this change |
| [[SW 900 (line)]] | alt | 98.5 | 0 | 3 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.438× (z -9.8) |
| [[A-172 (line)]] | wt | 67.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.406× (z -16.0) |
| [[C32 (line)]] | wt | 131 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.340× (z -17.7) |
| [[HepG2_C3A (line)]] | wt | 107 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.307× (z -12.4) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 115 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.509× (z -16.7) |
| [[NCI-H1792 (line)]] | alt | 88.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.333× (z -19.8) |
| [[NCI-H23 (line)]] | alt | 140 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.514× (z -13.8) |
| [[Panc 03.27 (line)]] | alt | 202 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.519× (z -10.8) |
| [[PANC-1 (line)]] | alt | 90.4 | 1 (1 ⚠) | 1 | [[Harringtonine (drug)]] 0.5 µM 1.59× (z +8.9) ⚠ cell-cycle shift, explains ~0% of this change | [[TAK-901 (drug)]] 5 µM 0.359× (z -10.2) |
| [[RPMI-7951 (line)]] | alt | 57.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.352× (z -13.0) |
| [[AN3 CA (line)]] | alt | 149 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -11.7) |
| [[HOP62 (line)]] | alt | 73.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.388× (z -17.2) |
| [[Hs 766T (line)]] | wt | 108 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.500× (z -11.7) |
| [[HT-29 (line)]] | alt | 65.1 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.495× (z -8.8) |
| [[J82 (line)]] | alt | 112 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.514× (z -14.0) |
| [[LOX-IMVI (line)]] | wt | 65.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.457× (z -12.1) |
| [[SNU-423 (line)]] | alt | 104 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.349× (z -17.3) |
| [[AsPC-1 (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 52.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 108 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 54.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 52.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 91.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 115 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 83.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 55.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 98.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 127 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 97.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1843), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRTFB]] | +0.67 | +0.68 / +0.62 | both halves | 7e-06 |  |
| [[PDS5A]] | +0.63 | +0.70 / +0.41 | both halves | 4e-05 |  |
| [[INPP4A]] | +0.63 | +0.72 / +0.59 | both halves | 7e-06 |  |
| [[ARHGEF11]] | +0.62 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[RANBP17]] | +0.62 | +0.66 / +0.54 | both halves | 1e-05 |  |
| [[EHMT1]] | +0.61 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[EXOC2]] | +0.61 | +0.65 / +0.57 | both halves | 1e-05 |  |
| [[CLASP2]] | +0.61 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[FANCC]] | +0.59 | +0.67 / +0.46 | both halves | 3e-05 |  |
| [[KPNA3]] | +0.58 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[R3HDM1]] | +0.58 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[ATR]] | +0.57 | +0.61 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF490]] | -0.58 | -0.58 / -0.45 | both halves | 3e-05 |  |
| [[KLC4]] | -0.54 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[FAM117A]] | -0.52 | -0.39 / -0.55 | both halves | 6e-05 |  |
| [[IQUB]] | -0.51 | -0.43 / -0.43 | both halves | 3e-05 |  |
| [[GNL1]] | -0.51 | -0.58 / -0.36 | both halves | 1e-04 |  |
| [[PLCH2]] | -0.50 | -0.49 / -0.46 | both halves | 3e-05 |  |
| [[CDKL3]] | -0.49 | -0.36 / -0.56 | both halves | 9e-05 |  |
| [[ZNF547]] | -0.48 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[HOOK2]] | -0.48 | -0.49 / -0.37 | both halves | 7e-05 |  |
| [[SRRM5]] | -0.47 | -0.52 / -0.32 | both halves | 2e-04 |  |
| [[KLHL28]] | -0.47 | -0.55 / -0.39 | both halves | 5e-05 |  |
| [[LAMTOR3]] | -0.47 | -0.49 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.561). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-6.5, -33.3); signed map (-17.8, -52.0). **Vector** length 114, 30.5% of its response variance represented; |z| ≥ 3 in 1,067 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +7.5 | +6.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +5.4 | +5.4 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.2 | +1.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +4.9 | +4.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.4 | +1.9 |
|  | [[venetoclax (drug)]] 5 µM |  | +3.1 | +2.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.0 | +2.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.7 | +0.8 |
| fall | [[Auranofin (drug)]] 5 µM |  | -10.1 | -13.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -9.7 | -26.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -8.7 | -9.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | -6.2 | -13.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.9 | -10.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.3 | -6.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.3 | -1.8 |
|  | [[Entrectinib (drug)]] 5 µM |  | -2.3 | -0.9 |
|  | [[Glycyrrhizic acid (drug)]] 0.05 µM |  | -2.1 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | sperm antigen with calponin homology and coiled-coil domains 1 like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q11.23 — chr22:24,270,817-24,417,739 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0376; previously CYTSA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q69YQ0](https://www.uniprot.org/uniprotkb/Q69YQ0) (Cytospin-A):

> Involved in cytokinesis and spindle organization. May play a role in actin cytoskeleton organization and microtubule stabilization and hence required for proper cell adhesion and migration.

**Summary**, from NCBI Gene [23384](https://www.ncbi.nlm.nih.gov/gene/23384):

> This gene encodes a coiled-coil domain containing protein. The encoded protein may play a critical role in actin-cytoskeletal reorganization during facial morphogenesis. Mutations in this gene are a cause of oblique facial clefting-1. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene. A read-through transcript composed of SPECC1L (sperm antigen with calponin homology and coiled-coil domains 1-like) and the downstream ADORA2A (adenosine A2a …

**Accessions** — [HGNC:29022](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29022) · Entrez [23384](https://www.ncbi.nlm.nih.gov/gene/23384) · UniProt [Q69YQ0](https://www.uniprot.org/uniprotkb/Q69YQ0) · Ensembl [ENSG00000100014](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100014)

## Data

Gene col 1843: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1843); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1843, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1843]; `tensor/DDL_lfc|DDL_z.npy` [1843]; `embed/gene_vectors.npy` [1843]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1843 or target_col == 1843). Every well: [[SPECC1L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPECC1L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
