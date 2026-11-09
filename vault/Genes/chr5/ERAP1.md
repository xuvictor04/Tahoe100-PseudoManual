---
symbol: "ERAP1"
type: "gene"
col: 8925
ensembl_id: "ENSG00000164307"
name: "endoplasmic reticulum aminopeptidase 1"
location: "5q15"
module: 25
arm: "+"
pooled_cpm: 48.85
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 15
n_dd_up_clean: 3
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# ERAP1

*endoplasmic reticulum aminopeptidase 1* — 5q15

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.00× (z +14.3, q 2e-43, up in 32 of 36 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Cobimetinib (drug)]] 0.5 µM: 1.25× (z +4.8, q 2e-04, up in 22 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (1 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.448× (z -17.2, q 0e+00, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PDIA3P1]] (+0.76, fdr 7e-06), [[CTSO]] (+0.74, fdr 1e-05), [[RCN1]] (+0.72, fdr 1e-05); moves opposite to [[SLC66A2]] (-0.58, fdr 8e-05), [[POLR2I]] (-0.57, fdr 2e-04), [[TMEM191A-1]] (-0.57, fdr 6e-04).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[CTSS]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 6 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8925.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.00×** | +14.3 | 2e-43 | 32/36 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.79×** | +12.4 | 4e-33 | 37/47 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.50×** | +8.1 | 1e-13 | 26/41 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.25×** | +4.8 | 2e-04 | 22/47 (NCI-H23, AsPC-1, …) | two highest doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +4.4 | 0.001 | 19/48 (AsPC-1, HOP62, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.23×** | +4.2 | 0.002 | 19/47 (NCI-H23, AsPC-1, …) | two highest doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **1.21×** | +4.1 | 0.003 | 15/48 (AsPC-1, NCI-H23, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.14× | +3.9 | 0.006 | 17/48 (A-427, HOP62, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.21×** | +3.7 | 0.011 | 12/48 (AsPC-1, NCI-H23, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.16× | +3.7 | 0.014 | 11/48 (AsPC-1, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 1.19× | +3.6 | 0.017 | 10/48 (AsPC-1, NCI-H23, …) | all doses, flat |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~0% of this change | 1.18× | +3.6 | 0.018 | 17/46 (SW 900, NCI-H1792, …) | inconsistent across doses | low cells (technical?) |
| [[Rifaximin (drug)]] 0.05 µM |  | 1.19× | +3.5 | 0.019 | 11/48 (RPMI-7951, LS 180, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.12× | +3.5 | 0.020 | 12/48 (AsPC-1, NCI-H23, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 5 µM |  | 1.15× | +3.3 | 0.033 | 9/48 (NCI-H23, Hs 766T, …) | all doses, flat | noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | 1.18× | +3.3 | 0.033 | 7/48 (NCI-H23, NCI-H2030, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 1.15× | +3.1 | 0.068 | 8/49 (AsPC-1, NCI-H23, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8925.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.448×** | -17.2 | 0e+00 | 46/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.463×** | -16.5 | 0e+00 | 46/48 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.481×** | -15.7 | 0e+00 | 44/48 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.637×** | -13.7 | 2e-40 | 36/48 (HS-578T, A-427, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **0.579×** | -11.7 | 1e-29 | 45/48 (HS-578T, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.599×** | -11.0 | 4e-26 | 45/48 (SW480, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.722×** | -7.0 | 3e-10 | 32/48 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.744×** | -6.3 | 2e-08 | 26/48 (HT-29, PANC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.759×** | -5.7 | 9e-07 | 24/48 (NCI-H1573, HS-578T, …) | inconsistent across doses | composition shift |
| [[Belinostat (drug)]] 0.05 µM |  | **0.773×** | -5.5 | 2e-06 | 28/48 (HEC-1-A, SW1417, …) | all doses, stronger at high dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.777×** | -5.4 | 3e-06 | 26/48 (MIA PaCa-2, A549, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.788×** | -4.8 | 7e-05 | 24/48 (PANC-1, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.684×** | -4.3 | 9e-04 | 17/48 (SHP-77, LoVo, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.815×** | -4.0 | 0.002 | 14/47 (HT-29, SW 1271, …) | inconsistent across doses | low cells (technical?) |
| [[vincristine (drug)]] 5 µM |  | **0.751×** | -3.2 | 0.052 | 10/44 (SNU-1, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 0.862× | -3.2 | 0.053 | 15/48 (NCI-H460, SNU-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8925. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 35.1 | 3 (3 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 2.30× (z +10.3) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.253× (z -17.0) |
| [[NCI-H460 (line)]] | wt | 44.8 | 2 (2 ⚠) | 4 | [[Dinaciclib (drug)]] 5 µM 2.82× (z +12.6) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.403× (z -11.6) |
| [[NCI-H1573 (line)]] | alt | 71.5 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.371× (z -14.4) |
| [[A-172 (line)]] | wt | 57.3 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.326× (z -11.1) |
| [[A498 (line)]] | wt | 77.7 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 2.26× (z +9.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.443× (z -14.1) |
| [[A549 (line)]] | wt | 50.4 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.253× (z -12.7) |
| [[HS-578T (line)]] | alt | 103 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.360× (z -16.6) |
| [[HOP62 (line)]] | alt | 30.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.04× (z +10.6) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 77.1 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.355× (z -9.6) |
| [[LoVo (line)]] | wt | 61.2 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.293× (z -12.9) |
| [[A-427 (line)]] | wt | 39.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.338× (z -14.6) |
| [[AN3 CA (line)]] | alt | 46.0 | 0 | 2 | — | [[Thymol (drug)]] 0.5 µM 0.0579× (z -13.1) |
| [[COLO 205 (line)]] | alt | 105 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.272× (z -12.1) |
| [[LS 180 (line)]] | wt | 40.2 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.346× (z -9.0) |
| [[MIA PaCa-2 (line)]] | alt | 42.9 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.277× (z -11.1) |
| [[NCI-H1792 (line)]] | alt | 44.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.37× (z +11.1) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 42.2 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.70× (z +9.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.510× (z -9.0) |
| [[PANC-1 (line)]] | alt | 52.6 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.484× (z -8.7) |
| [[SW1417 (line)]] | alt | 29.1 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.299× (z -9.8) |
| [[AsPC-1 (line)]] | alt | 46.0 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.346× (z -9.2) |
| [[C-33 A (line)]] | alt | 20.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.77× (z +8.6) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 31.8 | 0 | 1 | — | [[Alpelisib (drug)]] 0.05 µM 0.0819× (z -9.5) |
| [[H4 (line)]] | wt | 81.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.363× (z -11.2) |
| [[HEC-1-A (line)]] | alt | 22.8 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.293× (z -10.2) |
| [[KATO III (line)]] | alt | 47.9 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.331× (z -9.2) |
| [[LOX-IMVI (line)]] | wt | 23.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.35× (z +9.1) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 36.1 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.324× (z -8.5) |
| [[NCI-H2347 (line)]] | alt | 74.7 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.464× (z -8.5) |
| [[SW 900 (line)]] | alt | 40.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.465× (z -9.1) |
| [[BT-474 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 30.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 74.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 36.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 50.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 52.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 41.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 54.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 34.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 43.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 76.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 34.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 52.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 131 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 55.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 26.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8925), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDIA3P1]] | +0.76 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[CTSO]] | +0.74 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[RCN1]] | +0.72 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[C5orf15]] | +0.72 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[TAPBP]] | +0.69 | +0.60 / +0.63 | both halves | 7e-06 | pathway: Antigen Presentation: Folding, assembly and peptide loading of class I MHC; STRING 827 |
| [[HLA-H]] | +0.68 | +0.50 / +0.64 | both halves | 1e-05 | pathway: Antigen Presentation: Folding, assembly and peptide loading of class I MHC |
| [[MOB1A]] | +0.67 | +0.54 / +0.65 | both halves | 1e-05 |  |
| [[HLA-C]] | +0.65 | +0.55 / +0.62 | both halves | 1e-05 | pathway: Antigen Presentation: Folding, assembly and peptide loading of class I MHC; STRING 887 |
| [[ERAP2]] | +0.65 | +0.55 / +0.52 | both halves | 1e-05 | same gene group; pathway: Antigen Presentation: Folding, assembly and peptide loading of class I MHC; STRING 607 |
| [[ITM2B]] | +0.64 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[STRADB]] | +0.63 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[MOV10]] | +0.63 | +0.53 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 4 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC66A2]] | -0.58 | -0.37 / -0.47 | both halves | 8e-05 |  |
| [[POLR2I]] | -0.57 | -0.31 / -0.45 | both halves | 2e-04 |  |
| [[TMEM191A-1]] | -0.57 | -0.21 / -0.55 | both halves | 6e-04 |  |
| [[CARMIL2]] | -0.57 | -0.30 / -0.48 | both halves | 2e-04 |  |
| [[SPATA2L]] | -0.55 | -0.34 / -0.45 | both halves | 1e-04 |  |
| [[RBAK-RBAKDN]] | -0.55 | -0.39 / -0.41 | both halves | 5e-05 |  |
| [[MT1X]] | -0.55 | -0.36 / -0.46 | both halves | 1e-04 |  |
| [[ASL]] | -0.55 | -0.36 / -0.41 | both halves | 1e-04 |  |
| [[RPP21]] | -0.55 | -0.31 / -0.51 | both halves | 2e-04 |  |
| [[TECPR1]] | -0.55 | -0.29 / -0.41 | both halves | 3e-04 |  |
| [[ATP5F1D]] ⚠ | -0.55 | -0.28 / -0.46 | both halves | 3e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[SPATC1L]] | -0.54 | -0.31 / -0.41 | both halves | 2e-04 |  |
| [[DUSP23]] | -0.54 | -0.24 / -0.54 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CTSS]] | B | CTSS activity raises ERAP1's level | lines that do not express CTSS (15) vs lines expressing it (35) | 1.63× lower at baseline in the lines without CTSS | 0.032 | ⚠ within organs, on part of the lines; also absent: LINC02257, NMRAL2P-1, CSF2; maybe low, not absent |
| [[APOL6]] | B | APOL6 activity raises ERAP1's level | lines that do not express APOL6 (6) vs lines expressing it (44) | 1.70× lower at baseline in the lines without APOL6 | 0.077 | ⚠ within organs, on part of the lines; also absent: KLF4, S100A13, LGALS3BP; maybe low, not absent |
| [[HLA-H]] | B | HLA-H activity raises ERAP1's level | lines that do not express HLA-H (8) vs lines expressing it (42) | 1.67× lower at baseline in the lines without HLA-H | 0.084 | ⚠ within organs, on part of the lines; also absent: GPAT3, S100A6, ENSG00000290574; maybe low, not absent |
| [[DUSP23]] | B | DUSP23 activity raises ERAP1's level | lines that do not express DUSP23 (14) vs lines expressing it (36) | 1.55× lower at baseline in the lines without DUSP23 | 0.088 | ⚠ within organs, on part of the lines; also absent: HLA-F, SH2D4A, RARRES1 |
| [[MAP2K1]] | B | MAP2K1 activity lowers ERAP1's level | compounds that target MAP2K1: 2 of 4 raise it (Cobimetinib, Trametinib) | 50% of the class's compounds vs 0.8% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[GALNT7]] | C | GALNT7 activity raises ERAP1's level | lines that do not express GALNT7 (3) vs lines expressing it (47) | 1.42× lower at baseline in the lines without GALNT7 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: RND3, SCML1, TTC39C; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.517). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (18.6, 3.7); signed map (24.8, -20.4). **Vector** length 114, 30.0% of its response variance represented; |z| ≥ 3 in 1,067 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.0 | +14.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +8.0 | +4.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.3 | +12.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.1 | +8.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +6.7 | +2.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.2 | +3.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +4.4 | +3.7 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +4.0 | +3.7 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +3.9 | +4.8 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +3.9 | +3.5 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -7.4 | -11.7 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.7 | -17.2 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.6 | -11.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.3 | -6.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.2 | -7.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.0 | -3.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.0 | -2.4 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -2.9 | -2.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.9 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | endoplasmic reticulum aminopeptidase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q15 — chr5:96,760,810-96,808,100 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ARTS-1, A-LAP, PILS-AP, KIAA0525, ERAAP1 |
| Gene groups (HGNC) | Aminopeptidases; Minor histocompatibility antigens; M1 metallopeptidases |
| Reactome | 3 pathways, smallest: Antigen Presentation: Folding, assembly and peptide loading of class I MHC; Class I MHC mediated antigen processing & presentation; Adaptive Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NZ08](https://www.uniprot.org/uniprotkb/Q9NZ08) (Endoplasmic reticulum aminopeptidase 1):

> Aminopeptidase that plays a central role in peptide trimming, a step required for the generation of most HLA class I-binding peptides. Peptide trimming is essential to customize longer precursor peptides to fit them to the correct length required for presentation on MHC class I molecules. Strongly prefers substrates 9-16 residues long. Rapidly degrades 13-mer to a 9-mer and then stops. Preferentially hydrolyzes the residue Leu and peptides with a hydrophobic C-terminus, while it has weak …

**Summary**, from NCBI Gene [51752](https://www.ncbi.nlm.nih.gov/gene/51752):

> The protein encoded by this gene is an aminopeptidase involved in trimming HLA class I-binding precursors so that they can be presented on MHC class I molecules. The encoded protein acts as a monomer or as a heterodimer with ERAP2. This protein may also be involved in blood pressure regulation by inactivation of angiotensin II. Three transcript variants encoding two different isoforms have been found for this gene.[provided by RefSeq, Oct 2010]

**Accessions** — [HGNC:18173](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18173) · Entrez [51752](https://www.ncbi.nlm.nih.gov/gene/51752) · UniProt [Q9NZ08](https://www.uniprot.org/uniprotkb/Q9NZ08) · Ensembl [ENSG00000164307](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164307)

## Data

Gene col 8925: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8925); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8925, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8925]; `tensor/DDL_lfc|DDL_z.npy` [8925]; `embed/gene_vectors.npy` [8925]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8925 or target_col == 8925). Every well: [[ERAP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ERAP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
