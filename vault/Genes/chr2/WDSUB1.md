---
symbol: "WDSUB1"
type: "gene"
col: 12140
ensembl_id: "ENSG00000196151"
name: "WD repeat, sterile alpha motif and U-box domain containing 1"
location: "2q24.2"
module: 45
arm: "+"
pooled_cpm: 27.66
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 16
n_dd_up_clean: 18
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/045"]
generated_by: "tahoemap"
---

# WDSUB1

*WD repeat, sterile alpha motif and U-box domain containing 1* — 2q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (6 with an alert ⚠); the strongest is [[Ponatinib (drug)]] 5 µM: 1.61× (z +9.0, q 1e-16, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.571× (z -10.6, q 2e-23, down in 25 of 44 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.594× (z -9.8, q 2e-20, down in 35 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SNX2]] (+0.70, fdr 7e-06), [[KIF13A]] (+0.66, fdr 7e-06), [[SPPL3]] (+0.65, fdr 7e-06); moves opposite to [[PDCD6]] (-0.61, fdr 1e-05), [[KPNA4]] (-0.58, fdr 1e-05), [[SETX]] (-0.57, fdr 1e-05).
> It sits in the **+** arm of [[Module 045]] (Iron uptake and transport).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[PKD1L2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12140.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **1.61×** | +9.0 | 1e-16 | 38/48 (NCI-H2030, HOP62, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.39×** | +8.7 | 1e-15 | 29/48 (NCI-H1792, LoVo, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.46×** | +7.1 | 2e-10 | 32/48 (CFPAC-1, A-172, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.30×** | +7.0 | 3e-10 | 27/48 (A-172, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Radotinib (drug)]] 5 µM |  | **1.28×** | +6.6 | 5e-09 | 30/48 (RKO, NCI-H23, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.37×** | +5.7 | 1e-06 | 24/47 (SW480, NCI-H2030, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.23×** | +5.5 | 2e-06 | 22/48 (BT-474, NCI-H1792, …) | rises with dose |  |
| [[Afatinib (drug)]] 5 µM |  | **1.36×** | +5.2 | 1e-05 | 21/48 (BT-474, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.31×** | +5.2 | 2e-05 | 18/48 (KATO III, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.28×** | +4.7 | 1e-04 | 18/48 (KATO III, LoVo, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.27×** | +4.5 | 4e-04 | 19/47 (BT-474, LS 180, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.25×** | +4.2 | 0.001 | 9/48 (NCI-H460, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Neratinib (drug)]] 5 µM |  | **1.23×** | +3.9 | 0.003 | 10/47 (BT-474, SW1417, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | 1.19× | +3.9 | 0.003 | 15/48 (SW480, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | **1.24×** | +3.9 | 0.003 | 10/47 (HEC-1-A, CFPAC-1, …) | top dose only |  |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | **1.22×** | +3.6 | 0.010 | 13/47 (A549, RKO, …) | top dose only |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.20×** | +3.5 | 0.015 | 7/47 (BT-474, A-172, …) | top dose only |  |
| [[AZD-8055 (drug)]] 5 µM |  | **1.39×** | +3.2 | 0.032 | 4/48 (SW480, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.20×** | +3.2 | 0.032 | 7/48 (SW480, RKO, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 15 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12140.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | **0.571×** | -10.6 | 2e-23 | 25/44 (Panc 03.27, SNU-1, …) | all doses, flat | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.594×** | -9.8 | 2e-20 | 35/47 (SW480, SNU-423, …) | top dose only | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.768×** | -7.1 | 3e-10 | 25/48 (MIA PaCa-2, NCI-H460, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change | **0.749×** | -5.1 | 6e-05 | 22/44 (C-33 A, SNU-1, …) | all doses, flat | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.775×** | -4.8 | 2e-04 | 22/48 (PANC-1, NCI-H2347, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.932× | -4.6 | 4e-04 | 2/48 (hTERT-HPNE, SW 1271) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.779×** | -4.5 | 5e-04 | 19/47 (MIA PaCa-2, SNU-423, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **0.785×** | -4.4 | 7e-04 | 18/35 (A-427, SW1417, …) | all doses, flat | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.848× | -4.4 | 7e-04 | 21/48 (MIA PaCa-2, NCI-H2347, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.802×** | -4.2 | 0.002 | 20/48 (SW480, SNU-1, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **0.809×** | -3.9 | 0.006 | 19/48 (RKO, NCI-H460, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.816×** | -3.8 | 0.006 | 18/48 (NCI-H460, PANC-1, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.818×** | -3.8 | 0.006 | 19/47 (SW480, SNU-1, …) | two highest doses |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.682×** | -3.8 | 0.006 | 17/48 (MIA PaCa-2, NCI-H460, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.692×** | -3.6 | 0.010 | 15/47 (LS 180, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.826×** | -3.6 | 0.011 | 17/48 (SW 1271, PANC-1, …) | inconsistent across doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.728×** | -3.1 | 0.052 | 13/47 (CFPAC-1, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **0.800×** | -3.0 | 0.070 | 11/48 (H4, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[(S)-Crizotinib (drug)]] 0.5 µM |  | 0.857× | -2.9 | 0.088 | 11/47 (NCI-H1792, A-172, …) | two highest doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.38 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12140. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 46.0 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.181× (z -13.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.332× (z -8.8) |
| [[SW480 (line)]] | alt | 27.2 | 0 | 5 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.155× (z -17.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.316× (z -11.0) |
| [[SNU-1 (line)]] | wt | 50.0 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.182× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change · without an alert: [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.233× (z -9.3) |
| [[A-172 (line)]] | wt | 34.3 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +12.9) | [[Dinaciclib (drug)]] 0.5 µM 0.336× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change |
| [[NCI-H460 (line)]] | wt | 37.1 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.439× (z -8.9) ⚠ cell-cycle shift, explains ~25% of this change |
| [[SNU-423 (line)]] | alt | 38.6 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.289× (z -9.5) |
| [[A-427 (line)]] | wt | 36.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.254× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[AN3 CA (line)]] | alt | 52.1 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.138× (z -8.5) ⚠ cell-cycle shift, explains ~60% of this change |
| [[BT-474 (line)]] | alt | 20.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.74× (z +11.2) | — |
| [[C-33 A (line)]] | alt | 38.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.228× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change |
| [[CHP-212 (line)]] | wt | 38.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.120× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change |
| [[J82 (line)]] | alt | 23.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +10.7) | — |
| [[KATO III (line)]] | alt | 20.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.63× (z +12.2) | — |
| [[LoVo (line)]] | wt | 22.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.338× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H1792 (line)]] | alt | 17.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.313× (z -10.6) |
| [[NCI-H2347 (line)]] | alt | 22.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +9.1) | — |
| [[Panc 03.27 (line)]] | alt | 37.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0559× (z -24.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change |
| [[RKO (line)]] | wt | 31.4 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.280× (z -9.0) ⚠ cell-cycle shift, explains ~68% of this change |
| [[SW1417 (line)]] | alt | 46.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.346× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 37.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 27.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.31 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 37.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 29.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 24.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 30.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 51.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 42.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 24.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12140), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNX2]] | +0.70 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[KIF13A]] | +0.66 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[SPPL3]] | +0.65 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[TRPM7]] | +0.64 | +0.69 / +0.64 | both halves | 7e-06 |  |
| [[RRAGD]] | +0.63 | +0.58 / +0.62 | both halves | 8e-06 |  |
| [[MLLT10]] | +0.63 | +0.50 / +0.63 | both halves | 1e-05 |  |
| [[KBTBD3]] | +0.62 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[ESD]] | +0.60 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[RCHY1]] | +0.60 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[AQP11]] | +0.60 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[RCOR3]] | +0.60 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[MORN4]] | +0.60 | +0.54 / +0.64 | both halves | 1e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDCD6]] | -0.61 | -0.62 / -0.55 | both halves | 1e-05 |  |
| [[KPNA4]] | -0.58 | -0.51 / -0.60 | both halves | 1e-05 |  |
| [[SETX]] | -0.57 | -0.54 / -0.59 | both halves | 1e-05 |  |
| [[DDX5]] | -0.57 | -0.46 / -0.57 | both halves | 3e-05 |  |
| [[UCKL1-AS1]] | -0.57 | -0.54 / -0.56 | both halves | 1e-05 |  |
| [[SEC16A]] | -0.57 | -0.53 / -0.60 | both halves | 1e-05 |  |
| [[GATAD2A]] | -0.56 | -0.47 / -0.58 | both halves | 2e-05 |  |
| [[LARP4B]] | -0.56 | -0.52 / -0.56 | both halves | 1e-05 |  |
| [[HCG18]] | -0.56 | -0.52 / -0.59 | both halves | 1e-05 |  |
| [[EP400P1]] | -0.56 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[LRRC59]] | -0.55 | -0.49 / -0.59 | both halves | 1e-05 |  |
| [[SLC25A44]] | -0.55 | -0.47 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PKD1L2]] | B | PKD1L2 activity raises WDSUB1's level | lines that do not express PKD1L2 (13) vs lines expressing it (37) | 1.40× lower at baseline in the lines without PKD1L2 | 0.007 | ⚠ within organs, on part of the lines; also absent: SPDYE10; maybe low, not absent |
| [[HRK]] | B | HRK activity raises WDSUB1's level | lines that do not express HRK (13) vs lines expressing it (37) | 1.52× lower at baseline in the lines without HRK | 0.019 | ⚠ within organs, on part of the lines; also absent: AP3B2, BSN, ZNF71 |
| [[ASPH]] | B | ASPH activity lowers WDSUB1's level | lines that do not express ASPH (5) vs lines expressing it (45) | 1.74× higher at baseline in the lines without ASPH | 0.021 | ⚠ within organs, on part of the lines; also absent: HIPK2, EPS8, SCML1; maybe low, not absent |
| [[ABL1]] | B | ABL1 activity lowers WDSUB1's level | compounds that target ABL1: 4 of 6 raise it (Flumatinib, NG25, Ponatinib, Radotinib) | 67% of the class's compounds vs 5.0% of all compounds | 0.054 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[GKAP1]] | C | GKAP1 activity raises WDSUB1's level | lines that do not express GKAP1 (3) vs lines expressing it (47) | 2.08× lower at baseline in the lines without GKAP1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SEMA3F, TMEM132A, SPDL1; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 045]] — Iron uptake and transport; 102 genes; this gene is in the **+** arm (projection on the module's main direction 0.605). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (8.7, -9.8); signed map (-25.0, -8.1). **Vector** length 112, 28.2% of its response variance represented; |z| ≥ 3 in 998 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ponatinib (drug)]] 5 µM |  | +7.3 | +9.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +7.0 | +6.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +6.4 | +8.7 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +5.8 | +7.1 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +4.1 | +4.7 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +3.4 | +5.5 |
|  | [[Afatinib (drug)]] 5 µM |  | +3.4 | +5.2 |
| fall | [[Auranofin (drug)]] 5 µM |  | -6.0 | -9.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.8 | -4.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -5.0 | -7.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | -5.0 | -3.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | -4.7 | -4.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -3.0 | -3.1 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -2.5 | -1.9 |
|  | [[Diphenhydramine (drug)]] 0.5 µM |  | -2.1 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | WD repeat, sterile alpha motif and U-box domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q24.2 — chr2:159,235,798-159,286,703 (-) |
| Ensembl biotype | protein_coding |
| Also known as | UBOX6, FLJ36175; previously WDSAM1 |
| Gene groups (HGNC) | WD repeat domain containing; U-box domain containing; Sterile alpha motif domain containing |
| Matched by | ensembl_id |

UniProt [Q8N9V3](https://www.uniprot.org/uniprotkb/Q8N9V3) carries no function annotation.

**Summary**, from NCBI Gene [151525](https://www.ncbi.nlm.nih.gov/gene/151525):

> Predicted to enable ubiquitin-protein transferase activity. Predicted to be involved in protein ubiquitination. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26697](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26697) · Entrez [151525](https://www.ncbi.nlm.nih.gov/gene/151525) · UniProt [Q8N9V3](https://www.uniprot.org/uniprotkb/Q8N9V3) · Ensembl [ENSG00000196151](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196151)

## Data

Gene col 12140: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12140); `tables/drug_effects.parquet` (59 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12140, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12140]; `tensor/DDL_lfc|DDL_z.npy` [12140]; `embed/gene_vectors.npy` [12140]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12140 or target_col == 12140). Every well: [[WDSUB1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WDSUB1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
