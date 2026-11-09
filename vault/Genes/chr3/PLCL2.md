---
symbol: "PLCL2"
type: "gene"
col: 7843
ensembl_id: "ENSG00000154822"
name: "phospholipase C like 2"
location: "3p24.3"
module: 62
arm: "+"
pooled_cpm: 21.2
n_lines_expressing: 38
n_dd_up: 33
n_dd_down: 24
n_dd_up_clean: 22
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 5
direction_downstream: 5
tags: ["gene", "module/062"]
generated_by: "tahoemap"
---

# PLCL2

*phospholipase C like 2* — 3p24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 33 drug-doses (11 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.73× (z +11.7, q 8e-29, up in 27 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.468× (z -11.5, q 7e-28, down in 27 of 36 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAS]] (+0.72, fdr 1e-05), [[ACTA2]] (+0.68, fdr 3e-05), [[SPATA18]] (+0.65, fdr 6e-05); moves opposite to [[LINC02935]] (-0.55, fdr 4e-05), [[SAMD4B]] (-0.53, fdr 4e-05), [[NBEAL1]] (-0.53, fdr 6e-05).
> It is in [[Module 062]], a single-armed module (p53 targets up).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 5 go from it, the strongest it → [[FAS]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 33 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7843.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.73×** | +11.7 | 8e-29 | 27/36 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.87×** | +9.5 | 7e-19 | 25/35 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.46×** | +8.0 | 2e-13 | 22/36 (A549, LOX-IMVI, …) | rises with dose | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.58×** | +6.9 | 7e-10 | 22/36 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.54×** | +6.3 | 4e-08 | 19/34 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.34×** | +6.2 | 7e-08 | 17/36 (A498, A549, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.45×** | +5.6 | 2e-06 | 21/36 (C32, AsPC-1, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.40×** | +5.1 | 2e-05 | 17/35 (NCI-H2347, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Amsacrine (drug)]] 5 µM |  | **1.27×** | +5.0 | 3e-05 | 15/36 (A549, A-172, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.26×** | +5.0 | 3e-05 | 18/36 (NCI-H2347, SNU-423, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.32×** | +3.9 | 0.005 | 9/36 (SW48, PANC-1, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.29×** | +3.9 | 0.005 | 11/35 (A549, A-172, …) | all doses, stronger at high dose |  |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.30×** | +3.8 | 0.005 | 11/35 (A-427, A498, …) | rises with dose |  |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.30×** | +3.8 | 0.005 | 12/35 (NCI-H460, A-427, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 1.20× | +3.8 | 0.005 | 13/36 (AsPC-1, LoVo, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.30×** | +3.6 | 0.010 | 9/35 (AsPC-1, NCI-H2347, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **1.56×** | +3.5 | 0.015 | 7/36 (HOP62, LoVo, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | **1.26×** | +3.4 | 0.019 | 8/35 (A-427, NCI-H460, …) | rises with dose | plate-row cell shift |
| [[Cobimetinib (drug)]] 5 µM |  | **1.26×** | +3.4 | 0.020 | 9/35 (NCI-H2347, AsPC-1, …) | all doses, flat |  |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.24×** | +3.3 | 0.025 | 8/35 (A549, NCI-H460, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7843.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.468×** | -11.5 | 7e-28 | 27/36 (HT-29, AsPC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.495×** | -10.7 | 4e-24 | 21/35 (HT-29, LoVo, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.553×** | -9.0 | 6e-17 | 25/36 (HT-29, AsPC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.556×** | -8.9 | 9e-17 | 23/33 (A-427, LoVo, …) | two highest doses | cell-cycle shift (explains ~13% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.627×** | -7.1 | 2e-10 | 25/35 (HT-29, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.628×** | -7.0 | 2e-10 | 23/35 (HT-29, C32, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.638×** | -6.4 | 1e-08 | 19/36 (HT-29, SW48, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.457×** | -6.2 | 4e-08 | 21/34 (Panc 03.27, SK-MEL-2, …) | rises with dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.674×** | -5.7 | 6e-07 | 17/26 (LOX-IMVI, AsPC-1, …) | two highest doses | cell-cycle shift (explains ~13% here); composition shift |
| [[Abemaciclib (drug)]] 5 µM |  | **0.557×** | -4.6 | 2e-04 | 17/36 (AsPC-1, SK-MEL-2, …) | rises with dose | noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **0.579×** | -4.3 | 7e-04 | 13/33 (HS-578T, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~51% of this change | **0.753×** | -4.3 | 7e-04 | 16/34 (HT-29, RKO, …) | inconsistent across doses | low cells (technical?) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.757×** | -4.2 | 0.001 | 14/35 (NCI-H2347, SK-MEL-2, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.590×** | -4.2 | 0.001 | 14/35 (HT-29, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM |  | **0.824×** | -4.2 | 0.001 | 12/36 (HCT15, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-733 (drug)]] 5 µM |  | **0.611×** | -3.9 | 0.003 | 13/34 (HS-578T, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.843× | -3.7 | 0.008 | 15/36 (HT-29, C32, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.795×** | -3.5 | 0.014 | 14/35 (C32, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, -0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7843. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 39.5 | 0 | 10 (3 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.126× (z -15.6) |
| [[C32 (line)]] | wt | 81.7 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -15.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.187× (z -12.3) |
| [[A498 (line)]] | wt | 17.0 | 5 (3 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.36× (z +13.5) | [[Bortezomib (drug)]] 5 µM 0.0769× (z -10.6) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[SNU-1 (line)]] | wt | 111 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.138× (z -14.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.309× (z -8.9) |
| [[A549 (line)]] | wt | 36.7 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.56× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 2.37× (z +9.1) | — |
| [[LoVo (line)]] | wt | 53.7 | 2 | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.29× (z +16.0) | [[Dinaciclib (drug)]] 5 µM 0.181× (z -15.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.275× (z -12.4) |
| [[LS 180 (line)]] | wt | 54.2 | 2 (1 ⚠) | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.39× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.229× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.289× (z -9.6) |
| [[AsPC-1 (line)]] | alt | 39.6 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0573× (z -18.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.200× (z -11.0) |
| [[HEC-1-A (line)]] | alt | 28.4 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.112× (z -17.2) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.314× (z -9.5) |
| [[RKO (line)]] | wt | 47.4 | 0 | 4 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.214× (z -10.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.300× (z -8.5) |
| [[A-172 (line)]] | wt | 13.5 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.66× (z +11.2) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SW48 (line)]] | wt | 47.6 | 0 | 3 | — | [[Auranofin (drug)]] 5 µM 0.156× (z -11.0) |
| [[LOX-IMVI (line)]] | wt | 36.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0507× (z -24.2) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 7.35 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.92× (z +14.8) | — |
| [[Panc 03.27 (line)]] | alt | 28.8 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.261× (z -8.9) |
| [[SHP-77 (line)]] | alt | 22.2 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.139× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.191× (z -9.6) |
| [[A-427 (line)]] | wt | 37.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.149× (z -14.9) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 24.0 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.165× (z -8.8) |
| [[NCI-H2347 (line)]] | alt | 22.8 | 1 | 0 | [[Tucidinostat (drug)]] 0.5 µM 3.19× (z +8.6) | — |
| [[SK-MEL-2 (line)]] | alt | 36.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -16.8) ⚠ cell-cycle shift, would explain all of this change |
| [[AN3 CA (line)]] | alt | 3.45 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.46 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.60 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 37.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.75 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 8.67 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.88 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.84 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.73 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.45 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 52.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.07 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.23 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.48 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.24 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 9.51 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.26 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.20 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7843), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAS]] | +0.72 | +0.52 / +0.70 | both halves | 1e-05 |  |
| [[ACTA2]] | +0.68 | +0.45 / +0.62 | both halves | 3e-05 |  |
| [[SPATA18]] | +0.65 | +0.39 / +0.63 | both halves | 6e-05 |  |
| [[ZMAT3]] | +0.63 | +0.48 / +0.67 | both halves | 2e-05 |  |
| [[ZNF423]] | +0.63 | +0.45 / +0.59 | both halves | 3e-05 |  |
| [[DRAM1]] | +0.62 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[DSC3]] | +0.61 | +0.39 / +0.44 | both halves | 6e-05 |  |
| [[PINCR]] | +0.60 | +0.37 / +0.61 | both halves | 8e-05 |  |
| [[PPM1D]] | +0.59 | +0.46 / +0.64 | both halves | 3e-05 |  |
| [[PTCHD4]] | +0.59 | +0.31 / +0.62 | both halves | 2e-04 |  |
| [[PURPL]] | +0.58 | +0.44 / +0.54 | both halves | 3e-05 |  |
| [[REV3L]] | +0.57 | +0.51 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02935]] | -0.55 | -0.40 / -0.49 | both halves | 4e-05 |  |
| [[SAMD4B]] | -0.53 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[NBEAL1]] | -0.53 | -0.40 / -0.38 | both halves | 6e-05 |  |
| [[NUMBL]] | -0.52 | -0.44 / -0.37 | both halves | 8e-05 |  |
| [[ACOX3]] | -0.49 | -0.45 / -0.43 | both halves | 3e-05 |  |
| [[PC]] | -0.48 | -0.36 / -0.34 | both halves | 1e-04 | same gene group |
| [[LRRFIP1]] | -0.48 | -0.40 / -0.35 | both halves | 1e-04 |  |
| [[CLTCL1]] | -0.47 | -0.41 / -0.22 | both halves | 6e-04 |  |
| [[ASL]] | -0.47 | -0.41 / -0.23 | both halves | 6e-04 |  |
| [[KCTD21]] | -0.47 | -0.40 / -0.25 | both halves | 4e-04 |  |
| [[SWI5]] | -0.46 | -0.46 / -0.34 | both halves | 1e-04 |  |
| [[GCDH]] | -0.46 | -0.26 / -0.30 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 3, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PLCL2's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 5.9% of all compounds | 0.007 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[TOP1]] | B | TOP1 activity lowers PLCL2's level | compounds that target TOP1: 3 of 3 raise it (Doxorubicin, Irinotecan, Topotecan) | 100% of the class's compounds vs 5.9% of all compounds | 0.079 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[PINCR]] | B | PINCR activity strengthens PLCL2's drug response | lines that do not express PINCR (19) vs lines expressing it (17) | the lines without PINCR respond 0.55× as strongly (z diff +2.13); rises at some drug-doses, falls at others (75% from rises): Idarubicin (hydrochloride) 5 µM: 1.47x vs 2.10x (z diff +3.1); Selinexor 5 µM: 1.28x vs 1.67x (z diff +2.9); Auranofin 5 µM: 0.60x vs 0.45x (z diff +2.3) | 0.081 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PTCHD4, ENSG00000269729, PCK1; target measured in part of the lines; rises at some drug-doses, falls at others; artifact flags |
| [[GALNT7]] | C | GALNT7 activity raises PLCL2's level | lines that do not express GALNT7 (3) vs lines expressing it (47) | 5.70× lower at baseline in the lines without GALNT7 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: RND3, SCML1, TTC39C; its own permutation p |
| [[TP53]] | C | TP53 activity strengthens PLCL2's drug response | recorded loss-of-function mutation of TP53 in 20 lines vs 16 not recorded | the TP53-altered lines respond 0.52× as strongly (z diff +2.33); strongest at Idarubicin (hydrochloride) 5 µM: 1.46x vs 2.16x (z diff +3.4) | 0.463 over the table, 0.021 within its group | ⚠ within its group only (a lead); within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines; target measured in part of the lines; lower baseline (lost expression?); artifact flags |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAS]] | B | PLCL2 activity strengthens FAS's drug response | lines that do not express PLCL2 (9) vs lines expressing it (31) | the lines without PLCL2 respond 0.65× as strongly (z diff +2.07); rises at some drug-doses, falls at others (28% from rises): Homoharringtonine 5 µM: 1.43x vs 2.31x (z diff +3.4); Belinostat 5 µM: 0.38x vs 0.21x (z diff +3.1); Panobinostat 0.05 µM: 0.69x vs 0.46x (z diff +2.7) | 0.026 | ⚠ within organs, on part of the lines; target measured in part of the lines; rises at some drug-doses, falls at others; artifact flags |
| [[KITLG]] | B | PLCL2 activity raises KITLG's level | lines that do not express PLCL2 (12) vs lines expressing it (38) | 2.06× lower at baseline in the lines without PLCL2 | 0.051 | ⚠ within organs, on part of the lines |
| [[KCTD1]] | B | PLCL2 activity raises KCTD1's level | lines that do not express PLCL2 (12) vs lines expressing it (38) | 1.53× lower at baseline in the lines without PLCL2 | 0.056 | ⚠ within organs, on part of the lines |
| [[FAS]] | B | PLCL2 activity raises FAS's level | lines that do not express PLCL2 (12) vs lines expressing it (38) | 1.75× lower at baseline in the lines without PLCL2 | 0.089 | ⚠ within organs, on part of the lines |
| [[GPX1]] | B | PLCL2 activity raises GPX1's level | lines that do not express PLCL2 (12) vs lines expressing it (38) | 1.67× lower at baseline in the lines without PLCL2 | 0.096 | ⚠ within organs, on part of the lines |

## Where it sits

- **Module**: [[Module 062]] — p53 targets up; 78 genes; every member is in the + arm (projection on the module's main direction 0.680). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-13.9, 36.1); signed map (42.2, -22.8). **Vector** length 113, 29.7% of its response variance represented; |z| ≥ 3 in 1,097 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.6 | +11.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | +6.1 | +6.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +6.1 | +9.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +6.0 | +6.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +5.2 | +8.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.3 | +5.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.2 | +5.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.2 | +6.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.4 | +3.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.2 | +1.9 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -5.8 | -11.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | -5.6 | -9.0 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.2 | -7.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.8 | -10.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.0 | -7.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.6 | -4.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.6 | -1.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.8 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | phospholipase C like 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p24.3 — chr3:16,802,651-17,090,604 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1092; previously PLCE2 |
| Gene groups (HGNC) | C2 domain containing phospholipases; MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UPR0](https://www.uniprot.org/uniprotkb/Q9UPR0) (Inactive phospholipase C-like protein 2):

> May play an role in the regulation of Ins(1,4,5)P3 around the endoplasmic reticulum.

**Summary**, from NCBI Gene [23228](https://www.ncbi.nlm.nih.gov/gene/23228):

> Enables GABA receptor binding activity. Predicted to be involved in several processes, including gamma-aminobutyric acid signaling pathway; negative regulation of cold-induced thermogenesis; and phosphatidylinositol-mediated signaling. Predicted to act upstream of or within B cell proliferation involved in immune response; B-1a B cell differentiation; and negative regulation of B cell receptor signaling pathway. Predicted to be located in cytoplasm. [provided by Alliance of Genome Resources, …

**Accessions** — [HGNC:9064](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9064) · Entrez [23228](https://www.ncbi.nlm.nih.gov/gene/23228) · UniProt [Q9UPR0](https://www.uniprot.org/uniprotkb/Q9UPR0) · Ensembl [ENSG00000154822](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000154822)

## Data

Gene col 7843: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7843); `tables/drug_effects.parquet` (60 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7843, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7843]; `tensor/DDL_lfc|DDL_z.npy` [7843]; `embed/gene_vectors.npy` [7843]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7843 or target_col == 7843). Every well: [[PLCL2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLCL2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
