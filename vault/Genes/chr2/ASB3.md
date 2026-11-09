---
symbol: "ASB3"
type: "gene"
col: 3640
ensembl_id: "ENSG00000115239"
name: "ankyrin repeat and SOCS box containing 3"
location: "2p16.2"
module: 38
arm: "+"
pooled_cpm: 118.52
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 16
n_dd_up_clean: 11
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/038"]
generated_by: "tahoemap"
---

# ASB3

*ankyrin repeat and SOCS box containing 3* — 2p16.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.58× (z +18.1, q 0e+00, up in 34 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (6 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.648× (z -12.2, q 1e-31, down in 43 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.735× (z -8.7, q 7e-16, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ISY1-RAB43]] (+0.68, fdr 7e-06), [[ING4]] (+0.66, fdr 1e-05), [[SEM1]] (+0.64, fdr 7e-06); moves opposite to [[LRRC8B]] (-0.50, fdr 5e-05), [[IDH3A]] (-0.49, fdr 8e-05), [[CEP83]] (-0.49, fdr 3e-04).
> It is in [[Module 038]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3640.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.58×** | +18.1 | 0e+00 | 34/48 (LoVo, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.11×** | +10.5 | 2e-23 | 43/49 (MIA PaCa-2, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.30×** | +10.4 | 3e-23 | 33/49 (HS-578T, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.92×** | +9.1 | 1e-17 | 43/48 (SW480, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.34×** | +8.2 | 4e-14 | 28/48 (C32, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.43×** | +7.5 | 8e-12 | 37/48 (HepG2/C3A, HT-29, …) | all doses, flat | cell-cycle shift (explains ~14% here); noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.27×** | +6.7 | 2e-09 | 31/48 (A-172, HS-578T, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.24×** | +6.1 | 6e-08 | 27/48 (LoVo, HepG2/C3A, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | 1.17× | +6.1 | 6e-08 | 16/48 (PANC-1, HS-578T, …) | rises with dose | low cells (technical?) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.27×** | +5.0 | 3e-05 | 23/47 (A-172, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +5.0 | 3e-05 | 22/48 (SW480, SHP-77, …) | rises with dose | composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.37×** | +4.4 | 5e-04 | 24/45 (HepG2/C3A, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~18% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.16× | +4.2 | 1e-03 | 17/48 (LoVo, HepG2/C3A, …) | rises with dose |  |
| [[ERK5-IN-2 (drug)]] 5 µM |  | **1.31×** | +3.7 | 0.007 | 12/49 (NCI-H2347, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.30×** | +3.7 | 0.008 | 14/49 (A498, NCI-H2030, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 1.12× | +3.3 | 0.038 | 9/48 (SNU-423, A498, …) | inconsistent across doses | low cells (technical?) |
| [[Docetaxel (Trihydrate) (drug)]] 5 µM |  | 1.12× | +3.1 | 0.067 | 4/48 (HepG2/C3A, KATO III, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.24×** | +3.0 | 0.081 | 11/49 (A-172, NCI-H1573, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3640.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.648×** | -12.2 | 1e-31 | 43/48 (CFPAC-1, AsPC-1, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.680×** | -10.4 | 4e-23 | 31/44 (SK-MEL-2, A-427, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.717×** | -9.4 | 1e-18 | 31/49 (NCI-H1573, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.735×** | -8.7 | 7e-16 | 37/48 (A498, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.774×** | -6.9 | 5e-10 | 26/48 (A498, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[TAK-733 (drug)]] 5 µM |  | **0.657×** | -5.9 | 4e-07 | 33/48 (AsPC-1, A498, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.669×** | -5.6 | 1e-06 | 30/48 (AsPC-1, A498, …) | rises with dose | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.812×** | -5.6 | 1e-06 | 25/48 (J82, NCI-H1573, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.682×** | -5.4 | 5e-06 | 29/48 (AsPC-1, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~33% of this change | **0.830×** | -5.2 | 8e-06 | 23/48 (HepG2/C3A, SW480, …) | inconsistent across doses | low cells (technical?) |
| [[venetoclax (drug)]] 5 µM |  | **0.689×** | -5.2 | 8e-06 | 28/48 (CFPAC-1, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~20% of this change | **0.825×** | -5.2 | 8e-06 | 22/47 (SHP-77, NCI-H1573, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.821×** | -5.1 | 1e-05 | 24/47 (MIA PaCa-2, BT-474, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.843× | -4.8 | 6e-05 | 19/48 (AsPC-1, Panc 03.27, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **0.731×** | -4.4 | 4e-04 | 21/48 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Pralsetinib (drug)]] 5 µM |  | **0.740×** | -4.2 | 8e-04 | 20/49 (SW 900, H4, …) | top dose only | noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **0.753×** | -4.0 | 0.002 | 19/47 (SW 1088, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Carbamazepine (drug)]] 5 µM |  | 0.880× | -3.6 | 0.010 | 6/47 (LS 180, RKO, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3640. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 131 | 0 | 4 (3 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.431× (z -14.0) |
| [[AsPC-1 (line)]] | alt | 135 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.332× (z -14.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.605× (z -9.5) |
| [[CFPAC-1 (line)]] | alt | 122 | 0 | 4 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.420× (z -12.2) ⚠ unreliable plate only · without an alert: [[venetoclax (drug)]] 5 µM 0.278× (z -9.0) |
| [[HS-578T (line)]] | alt | 91.8 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.12× (z +28.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 128 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +19.7) | — |
| [[SW480 (line)]] | alt | 144 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.65× (z +12.5) | [[Dinaciclib (drug)]] 5 µM 0.589× (z -9.0) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 107 | 2 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 1.91× (z +10.0) | [[Dinaciclib (drug)]] 5 µM 0.526× (z -9.5) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 119 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.36× (z +13.4) | [[Dinaciclib (drug)]] 5 µM 0.391× (z -10.0) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 130 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.09× (z +21.1) | [[Dinaciclib (drug)]] 5 µM 0.431× (z -8.6) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 131 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.64× (z +10.1) | [[Dinaciclib (drug)]] 0.5 µM 0.302× (z -17.3) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 127 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +23.2) | — |
| [[PANC-1 (line)]] | alt | 83.6 | 1 (1 ⚠) | 2 (1 ⚠) | [[Selinexor (drug)]] 5 µM 1.59× (z +11.5) ⚠ cell-cycle shift, explains ~39% of this change | [[Harringtonine (drug)]] 5 µM 0.572× (z -9.4) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.598× (z -9.0) |
| [[A549 (line)]] | wt | 124 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.01× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 3.29× (z +8.9) | — |
| [[C32 (line)]] | wt | 101 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.89× (z +29.8) | — |
| [[HEC-1-A (line)]] | alt | 144 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.513× (z -10.1) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 133 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +18.7) | — |
| [[Hs 766T (line)]] | wt | 87.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +14.9) | — |
| [[HT-29 (line)]] | alt | 124 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.355× (z -10.6) ⚠ unreliable plate only |
| [[LoVo (line)]] | wt | 102 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.10× (z +32.0) | — |
| [[LOX-IMVI (line)]] | wt | 124 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +21.4) | — |
| [[NCI-H2030 (line)]] | alt | 95.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.71× (z +10.2) | [[Dinaciclib (drug)]] 0.05 µM 0.395× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 100 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.420× (z -13.3) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 167 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.60× (z +22.0) | — |
| [[SK-MEL-2 (line)]] | alt | 109 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.39× (z +22.4) | [[Dinaciclib (drug)]] 5 µM 0.110× (z -27.5) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 94.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +11.0) | — |
| [[SW 900 (line)]] | alt | 182 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.299× (z -15.5) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 137 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.207× (z -21.5) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 134 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.422× (z -11.0) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 142 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +13.5) | — |
| [[NCI-H1792 (line)]] | alt | 64.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.46× (z +30.7) | — |
| [[NCI-H23 (line)]] | alt | 159 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +14.2) | — |
| [[SHP-77 (line)]] | alt | 226 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 3.02× (z +8.5) | — |
| [[SNU-1 (line)]] | wt | 108 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.73× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[SW 1088 (line)]] | alt | 141 | 0 | 1 | — | [[Decitabine (drug)]] 0.5 µM 0.116× (z -9.9) |
| [[AN3 CA (line)]] | alt | 117 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 72.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 140 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 153 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 74.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 105 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 99.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 114 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 139 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 89.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3640), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ISY1-RAB43]] | +0.68 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[ING4]] | +0.66 | +0.49 / +0.69 | both halves | 1e-05 |  |
| [[SEM1]] | +0.64 | +0.66 / +0.59 | both halves | 7e-06 | pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[LINC02245]] | +0.62 | +0.50 / +0.62 | both halves | 1e-05 |  |
| [[FAM209A]] | +0.62 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[LINC00672]] | +0.62 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[METTL21EP-1]] | +0.61 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[FAM184B]] | +0.61 | +0.44 / +0.63 | both halves | 3e-05 |  |
| [[ISY1]] | +0.61 | +0.57 / +0.60 | both halves | 1e-05 |  |
| [[SLC5A11]] | +0.59 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[ZNF394]] | +0.58 | +0.38 / +0.64 | both halves | 7e-05 |  |
| [[NOXRED1]] | +0.58 | +0.62 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRRC8B]] | -0.50 | -0.40 / -0.49 | both halves | 5e-05 |  |
| [[IDH3A]] | -0.49 | -0.46 / -0.37 | both halves | 8e-05 |  |
| [[CEP83]] | -0.49 | -0.28 / -0.53 | both halves | 3e-04 |  |
| [[SMC6]] | -0.49 | -0.33 / -0.55 | both halves | 1e-04 |  |
| [[MIOS]] | -0.48 | -0.27 / -0.62 | both halves | 3e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 038]]; 122 genes; every member is in the + arm (projection on the module's main direction 0.544). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (30.6, -18.8); signed map (5.5, 5.7). **Vector** length 107, 29.8% of its response variance represented; |z| ≥ 3 in 1,015 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +7.0 | +6.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.2 | +10.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +5.0 | +6.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +4.2 | +7.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.0 | +10.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.6 | +9.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.5 | +2.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.5 | +5.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.9 | +4.2 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -8.9 | -12.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -7.1 | -8.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -6.6 | -6.9 |
|  | [[venetoclax (drug)]] 5 µM |  | -5.6 | -5.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | -5.2 | -5.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -4.9 | -5.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -4.7 | -5.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.7 | -5.6 |

## What is on record

|  |  |
|---|---|
| Name | ankyrin repeat and SOCS box containing 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p16.2 — chr2:53,532,672-53,860,160 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ASB-3 |
| Gene groups (HGNC) | Ankyrin repeat domain containing |
| Reactome | 4 pathways, smallest: Neddylation; Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y575](https://www.uniprot.org/uniprotkb/Q9Y575) (Ankyrin repeat and SOCS box protein 3):

> Probable substrate-recognition component of a SCF-like ECS (Elongin-Cullin-SOCS-box protein) E3 ubiquitin-protein ligase complex which mediates the ubiquitination and subsequent proteasomal degradation of target proteins. Recognizes TNFRSF1B. Plays a role in the down-regulation of antiviral innate immunity by targeting MAVS for ubiquitin-proteasomal degradation. Also destabilizes TRAF6 by enhancing its 'Lys-48'-linked polyubiquitination.

**Summary**, from NCBI Gene [51130](https://www.ncbi.nlm.nih.gov/gene/51130):

> The protein encoded by this gene is a member of the ankyrin repeat and SOCS box-containing (ASB) family of proteins. They contain ankyrin repeat sequence and SOCS box domain. The SOCS box serves to couple suppressor of cytokine signalling (SOCS) proteins and their binding partners with the elongin B and C complex, possibly targeting them for degradation. Alternatively spliced transcript variants have been described for this gene. [provided by RefSeq, Jan 2011]

**Accessions** — [HGNC:16013](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16013) · Entrez [51130](https://www.ncbi.nlm.nih.gov/gene/51130) · UniProt [Q9Y575](https://www.uniprot.org/uniprotkb/Q9Y575) · Ensembl [ENSG00000115239](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115239)

## Data

Gene col 3640: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3640); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3640, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3640]; `tensor/DDL_lfc|DDL_z.npy` [3640]; `embed/gene_vectors.npy` [3640]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3640 or target_col == 3640). Every well: [[ASB3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ASB3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
