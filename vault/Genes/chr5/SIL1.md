---
symbol: "SIL1"
type: "gene"
col: 4214
ensembl_id: "ENSG00000120725"
name: "SIL1 nucleotide exchange factor"
location: "5q31.2"
module: 49
arm: "+"
pooled_cpm: 106.93
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 12
n_dd_up_clean: 1
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/049"]
generated_by: "tahoemap"
---

# SIL1

*SIL1 nucleotide exchange factor* — 5q31.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.26× (z +5.5, q 2e-05, up in 24 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (10 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.649× (z -10.1, q 2e-21, down in 39 of 48 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.727× (z -7.5, q 1e-11, down in 34 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 7 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (A498 0.327×, SNU-423 0.471×, SW1417 0.494×, J82 0.505×; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (SNU-1 0.107×, MIA PaCa-2 0.293×, SK-MEL-2 0.306×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Auranofin (drug)]] 5 µM in 2 lines (LoVo 0.393×, MIA PaCa-2 0.528×); [[Ixazomib citrate (drug)]] 5 µM in 1 line (LoVo 0.467×); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (LoVo 0.503×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SRPRB]] (+0.55, fdr 2e-05), [[SLC35B1]] (+0.54, fdr 1e-05), [[USO1]] (+0.48, fdr 2e-05); moves opposite to [[RP2]] (-0.44, fdr 4e-05), [[GPR137B]] (-0.42, fdr 8e-05), [[MEX3B]] (-0.42, fdr 1e-04).
> It is in [[Module 049]], a single-armed module (XBP1(S) activates chaperone genes).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 4 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4214.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.26×** | +5.5 | 2e-05 | 24/48 (HepG2/C3A, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.16× | +4.7 | 6e-04 | 15/49 (SW480, A498, …) | all doses, flat |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.22×** | +4.7 | 6e-04 | 24/48 (SK-MEL-2, LoVo, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.23×** | +4.5 | 0.001 | 27/50 (A-427, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.05× | +4.2 | 0.003 | 0/50 | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.15× | +4.1 | 0.004 | 12/48 (MIA PaCa-2, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | 1.15× | +3.8 | 0.011 | 12/49 (NCI-H460, A-427, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 1.13× | +3.8 | 0.011 | 6/48 (MIA PaCa-2, HOP62, …) | all doses, flat |  |
| [[Belumosudil (drug)]] 5 µM |  | 1.18× | +3.7 | 0.015 | 21/48 (SW480, SW1417, …) | top dose only |  |
| [[Dihydroartemisinin (drug)]] 0.05 µM |  | 1.17× | +3.6 | 0.016 | 14/48 (NCI-H460, A498, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.17× | +3.6 | 0.018 | 15/48 (HS-578T, HOP62, …) | all doses, flat |  |
| [[Budesonide (drug)]] 5 µM |  | 1.16× | +3.5 | 0.022 | 15/48 (NCI-H1573, CFPAC-1, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | 1.16× | +3.4 | 0.026 | 11/48 (HS-578T, A-172, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +3.3 | 0.036 | 21/48 (MIA PaCa-2, HepG2/C3A, …) | rises with dose |  |
| [[Rifaximin (drug)]] 5 µM |  | 1.16× | +3.3 | 0.038 | 14/48 (NCI-H2030, NCI-H460, …) | inconsistent across doses |  |
| [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | 1.15× | +3.2 | 0.043 | 11/50 (NCI-H1573, A-172, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.15× | +3.2 | 0.053 | 15/47 (NCI-H2347, BT-474, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | 1.11× | +3.0 | 0.090 | 8/48 (A-427, BT-474, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 1.15× | +2.9 | 0.099 | 16/48 (A-427, MIA PaCa-2, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 13 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4214.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 7 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (A498 0.327×, SNU-423 0.471×, SW1417 0.494×, J82 0.505×; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (SNU-1 0.107×, MIA PaCa-2 0.293×, SK-MEL-2 0.306×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Auranofin (drug)]] 5 µM in 2 lines (LoVo 0.393×, MIA PaCa-2 0.528×); [[Ixazomib citrate (drug)]] 5 µM in 1 line (LoVo 0.467×); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (LoVo 0.503×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.649×** | -10.1 | 2e-21 | 39/48 (LoVo, SW1417, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.676×** | -9.2 | 2e-17 | 33/48 (LoVo, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.667×** | -9.1 | 2e-17 | 36/47 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **0.712×** | -7.7 | 3e-12 | 32/48 (A498, LOX-IMVI, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.727×** | -7.5 | 1e-11 | 34/48 (LoVo, MIA PaCa-2, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.807×** | -7.1 | 1e-10 | 25/48 (A498, SNU-423, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.741×** | -7.0 | 2e-10 | 35/48 (LS 180, KATO III, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.747×** | -6.8 | 6e-10 | 35/48 (KATO III, LS 180, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.610×** | -6.1 | 9e-08 | 31/49 (PANC-1, NCI-H1573, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.777×** | -5.7 | 7e-07 | 28/47 (NCI-H2030, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change | **0.814×** | -4.8 | 7e-05 | 25/49 (COLO 205, NCI-H23, …) | inconsistent across doses | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.817×** | -4.7 | 1e-04 | 24/48 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | 0.845× | -3.7 | 0.011 | 20/45 (SW1417, MIA PaCa-2, …) | inconsistent across doses | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.870× | -3.3 | 0.043 | 19/48 (LoVo, LS 180, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | 0.868× | -3.2 | 0.051 | 14/47 (CFPAC-1, LoVo, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.870× | -3.0 | 0.080 | 17/47 (A549, SNU-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Mebendazole (drug)]] 5 µM |  | 0.877× | -3.0 | 0.089 | 11/48 (CFPAC-1, NCI-H2030, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4214. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 179 | 0 | 7 (4 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.364× (z -14.5) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.393× (z -13.9) |
| [[LS 180 (line)]] | wt | 128 | 0 | 6 (6 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.370× (z -10.8) ⚠ cell-cycle shift, explains ~44% of this change |
| [[SW1417 (line)]] | alt | 139 | 0 | 6 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.494× (z -13.0) ⚠ cell-cycle shift, would explain all of this change |
| [[MIA PaCa-2 (line)]] | alt | 143 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.293× (z -16.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.528× (z -8.9) |
| [[NCI-H460 (line)]] | wt | 118 | 0 | 5 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.469× (z -11.8) ⚠ cell-cycle shift, explains ~44% of this change |
| [[C32 (line)]] | wt | 91.3 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.521× (z -10.4) ⚠ cell-cycle shift, would explain all of this change |
| [[H4 (line)]] | wt | 112 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.425× (z -11.2) ⚠ cell-cycle shift, would explain all of this change |
| [[KATO III (line)]] | alt | 134 | 0 | 4 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.376× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[HOP62 (line)]] | alt | 94.1 | 0 | 3 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.420× (z -9.7) ⚠ toxic |
| [[HS-578T (line)]] | alt | 121 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.559× (z -10.8) ⚠ cell-cycle shift, would explain all of this change |
| [[J82 (line)]] | alt | 73.6 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.505× (z -11.8) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H23 (line)]] | alt | 96.3 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.422× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change |
| [[A498 (line)]] | wt | 94.1 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -21.8) ⚠ cell-cycle shift, would explain all of this change |
| [[PANC-1 (line)]] | alt | 107 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.524× (z -10.2) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 111 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.306× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 97.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.591× (z -9.2) ⚠ cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 77.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.503× (z -11.1) ⚠ cell-cycle shift, would explain all of this change |
| [[COLO 205 (line)]] | alt | 157 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.233× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change |
| [[HEC-1-A (line)]] | alt | 112 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.601× (z -8.8) ⚠ cell-cycle shift, would explain all of this change |
| [[HT-29 (line)]] | alt | 103 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.348× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change |
| [[LOX-IMVI (line)]] | wt | 70.3 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.365× (z -11.6) ⚠ cell-cycle shift, explains ~63% of this change |
| [[NCI-H1573 (line)]] | alt | 120 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.374× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H2030 (line)]] | alt | 132 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.495× (z -9.4) ⚠ toxic |
| [[SNU-1 (line)]] | wt | 137 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.107× (z -20.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SNU-423 (line)]] | alt | 91.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.471× (z -13.3) ⚠ cell-cycle shift, would explain all of this change |
| [[SW48 (line)]] | wt | 116 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.381× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 99.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.478× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 126 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 195 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 57.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 88.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 88.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 88.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 67.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 77.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 118 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 69.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 87.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 91.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 91.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 97.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 120 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 76.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 179 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 59.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4214), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRPRB]] | +0.55 | +0.47 / +0.61 | both halves | 2e-05 |  |
| [[SLC35B1]] | +0.54 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[USO1]] | +0.48 | +0.47 / +0.49 | both halves | 2e-05 | same gene group |
| [[FBXW8]] | +0.48 | +0.44 / +0.53 | both halves | 3e-05 |  |
| [[OSTC]] | +0.48 | +0.40 / +0.49 | both halves | 5e-05 |  |
| [[SRBD1]] | +0.47 | +0.49 / +0.46 | both halves | 3e-05 |  |
| [[RUSF1]] | +0.47 | +0.40 / +0.50 | both halves | 5e-05 |  |
| [[GMDS-DT]] | +0.47 | +0.46 / +0.51 | both halves | 2e-05 |  |
| [[WDR25]] | +0.47 | +0.54 / +0.38 | both halves | 7e-05 |  |
| [[SSR3]] | +0.47 | +0.41 / +0.53 | both halves | 4e-05 |  |
| [[SLC38A10]] | +0.47 | +0.52 / +0.41 | both halves | 4e-05 |  |
| [[NDUFV3]] | +0.46 | +0.55 / +0.32 | both halves | 2e-04 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RP2]] | -0.44 | -0.46 / -0.41 | both halves | 4e-05 |  |
| [[GPR137B]] | -0.42 | -0.37 / -0.40 | both halves | 8e-05 |  |
| [[MEX3B]] | -0.42 | -0.39 / -0.33 | both halves | 1e-04 |  |
| [[CDC42EP4]] | -0.41 | -0.31 / -0.46 | both halves | 2e-04 |  |
| [[RPS6KA3]] | -0.39 | -0.45 / -0.34 | both halves | 1e-04 |  |
| [[RGS17]] | -0.39 | -0.39 / -0.33 | both halves | 1e-04 |  |
| [[TLE3]] | -0.38 | -0.38 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 049]] — XBP1(S) activates chaperone genes; 93 genes; every member is in the + arm (projection on the module's main direction 0.458). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.12; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (15.4, -39.4); signed map (-56.8, 12.8). **Vector** length 103, 29.0% of its response variance represented; |z| ≥ 3 in 1,111 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belumosudil (drug)]] 5 µM |  | +4.9 | +3.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.1 | +1.9 |
|  | [[venetoclax (drug)]] 5 µM |  | +3.3 | +1.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.9 | +1.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.6 | +0.8 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +2.6 | +4.7 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.4 | -1.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.6 | -2.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.9 | -7.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.4 | -2.6 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.3 | -1.7 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | -2.4 | -1.5 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.2 | -1.7 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -2.1 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | SIL1 nucleotide exchange factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q31.2 — chr5:138,946,724-139,293,557 (-) |
| Ensembl biotype | protein_coding |
| Also known as | BAP, ULG5; previously MSS |
| Gene groups (HGNC) | Armadillo like helical domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H173](https://www.uniprot.org/uniprotkb/Q9H173) (Nucleotide exchange factor SIL1):

> Required for protein translocation and folding in the endoplasmic reticulum (ER). Functions as a nucleotide exchange factor for the ER lumenal chaperone HSPA5.

**Summary**, from NCBI Gene [64374](https://www.ncbi.nlm.nih.gov/gene/64374):

> This gene encodes a resident endoplasmic reticulum (ER), N-linked glycoprotein with an N-terminal ER targeting sequence, 2 putative N-glycosylation sites, and a C-terminal ER retention signal. This protein functions as a nucleotide exchange factor for another unfolded protein response protein. Mutations in this gene have been associated with Marinesco-Sjogren syndrome. Alternate transcriptional splice variants have been characterized. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:24624](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24624) · Entrez [64374](https://www.ncbi.nlm.nih.gov/gene/64374) · UniProt [Q9H173](https://www.uniprot.org/uniprotkb/Q9H173) · Ensembl [ENSG00000120725](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000120725)

## Data

Gene col 4214: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4214); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4214, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4214]; `tensor/DDL_lfc|DDL_z.npy` [4214]; `embed/gene_vectors.npy` [4214]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4214 or target_col == 4214). Every well: [[SIL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SIL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
