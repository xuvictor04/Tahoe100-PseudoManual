---
symbol: "MPHOSPH9"
type: "gene"
col: 582
ensembl_id: "ENSG00000051825"
name: "M-phase phosphoprotein 9"
location: "12q24.31"
module: 67
arm: "+"
pooled_cpm: 68.36
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 17
n_dd_up_clean: 8
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/067"]
generated_by: "tahoemap"
---

# MPHOSPH9

*M-phase phosphoprotein 9* — 12q24.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.08× (z +19.3, q 0e+00, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (3 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.572× (z -14.7, q 0e+00, down in 34 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CIT]] (+0.82, fdr 7e-06), [[PARPBP]] (+0.81, fdr 7e-06), [[PBK]] (+0.81, fdr 7e-06).
> It is in [[Module 067]], a single-armed module (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[LINC02257]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 582.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.08×** | +19.3 | 0e+00 | 38/48 (SW480, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.90×** | +17.0 | 0e+00 | 39/48 (SW480, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.75×** | +14.7 | 0e+00 | 37/48 (SW480, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **1.46×** | +9.6 | 1e-19 | 25/43 (LoVo, A-172, …) | rises with dose | composition shift |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.82×** | +8.2 | 2e-14 | 36/48 (A498, SNU-423, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.34×** | +7.6 | 2e-12 | 30/48 (HOP62, HEC-1-A, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~87% of this change | **1.24×** | +5.8 | 6e-07 | 24/49 (NCI-H1573, LS 180, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.22×** | +5.3 | 1e-05 | 23/48 (SW1417, LoVo, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | 1.14× | +4.8 | 1e-04 | 20/48 (LoVo, hTERT-HPNE, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.37×** | +4.4 | 7e-04 | 20/48 (AsPC-1, NCI-H2347, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~35% of this change | 1.17× | +4.1 | 0.002 | 21/47 (A549, NCI-H23, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM |  | **1.33×** | +3.9 | 0.004 | 13/47 (NCI-H2347, J82, …) | top dose only | cell-cycle shift (explains ~10% here); noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | 1.18× | +3.8 | 0.008 | 12/47 (SW 900, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.29×** | +3.5 | 0.017 | 12/48 (NCI-H23, NCI-H1573, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | 1.14× | +3.3 | 0.039 | 11/48 (HepG2/C3A, A549, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 1.14× | +3.2 | 0.044 | 11/48 (AsPC-1, LoVo, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | 1.09× | +3.2 | 0.045 | 6/48 (hTERT-HPNE, AsPC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 45 in all, 13 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 582.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.572×** | -14.7 | 0e+00 | 34/48 (SW480, SHP-77, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.729×** | -11.8 | 1e-29 | 32/48 (A498, A-427, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.669×** | -10.6 | 6e-24 | 39/48 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.677×** | -10.3 | 1e-22 | 30/48 (MIA PaCa-2, SNU-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.682×** | -9.7 | 4e-20 | 29/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.783×** | -9.1 | 9e-18 | 30/48 (A-427, PANC-1, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.737×** | -8.1 | 7e-14 | 34/48 (A498, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.749×** | -7.6 | 2e-12 | 28/48 (A498, NCI-H460, …) | all doses, flat |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.761×** | -7.2 | 4e-11 | 27/48 (A-427, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.832×** | -6.8 | 5e-10 | 23/48 (NCI-H460, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.849× | -6.1 | 6e-08 | 21/49 (A498, PANC-1, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.646×** | -6.0 | 8e-08 | 27/48 (AN3 CA, SNU-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.804×** | -5.7 | 4e-07 | 21/48 (HT-29, H4, …) | two highest doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.664×** | -5.6 | 7e-07 | 26/49 (PANC-1, NCI-H2030, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.875× | -5.0 | 3e-05 | 17/48 (MIA PaCa-2, SW480, …) | two highest doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.855× | -4.1 | 0.001 | 18/48 (LS 180, A-427, …) | rises with dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.811×** | -3.9 | 0.003 | 18/48 (LoVo, PANC-1, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Bestatin (hydrochloride) (drug)]] 0.05 µM |  | 0.868× | -3.7 | 0.006 | 9/48 (SNU-423, PANC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 582. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 88.8 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.282× (z -16.3) |
| [[PANC-1 (line)]] | alt | 149 | 0 | 6 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.629× (z -10.8) ⚠ cell-cycle shift, explains ~22% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.529× (z -10.5) |
| [[SW480 (line)]] | alt | 90.4 | 3 | 3 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.43× (z +14.0) | [[Auranofin (drug)]] 5 µM 0.406× (z -14.3) |
| [[MIA PaCa-2 (line)]] | alt | 95.2 | 0 | 5 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.171× (z -19.7) |
| [[A-427 (line)]] | wt | 96.9 | 0 | 4 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.447× (z -14.6) |
| [[HT-29 (line)]] | alt | 57.4 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.90× (z +10.7) | [[Selinexor (drug)]] 5 µM 0.543× (z -8.7) ⚠ cell-cycle shift, explains ~22% of this change |
| [[LoVo (line)]] | wt | 46.9 | 4 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.57× (z +21.2) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.53× (z +10.9) | — |
| [[NCI-H460 (line)]] | wt | 74.3 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.399× (z -15.7) |
| [[AsPC-1 (line)]] | alt | 31.5 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.27× (z +13.8) | — |
| [[HOP62 (line)]] | alt | 70.4 | 2 | 1 | [[Panobinostat (drug)]] 0.5 µM 2.12× (z +8.8) | [[Homoharringtonine (drug)]] 0.5 µM 0.436× (z -9.8) |
| [[SNU-1 (line)]] | wt | 107 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.126× (z -17.6) |
| [[SW1417 (line)]] | alt | 71.2 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.62× (z +10.7) | — |
| [[HEC-1-A (line)]] | alt | 54.1 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.13× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | [[Auranofin (drug)]] 5 µM 0.476× (z -8.9) |
| [[Hs 766T (line)]] | wt | 58.4 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.01× (z +9.5) | — |
| [[KATO III (line)]] | alt | 36.6 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.85× (z +9.8) | — |
| [[LOX-IMVI (line)]] | wt | 68.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.487× (z -10.7) |
| [[LS 180 (line)]] | wt | 34.1 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.23× (z +9.7) | [[Selinexor (drug)]] 5 µM 0.445× (z -9.6) ⚠ cell-cycle shift, explains ~22% of this change |
| [[NCI-H2347 (line)]] | alt | 47.1 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.40× (z +9.0) | — |
| [[SNU-423 (line)]] | alt | 56.8 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.54× (z +9.0) | — |
| [[A-172 (line)]] | wt | 43.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.85× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[A549 (line)]] | wt | 62.6 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.26× (z +8.5) | — |
| [[AN3 CA (line)]] | alt | 82.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -11.5) |
| [[C-33 A (line)]] | alt | 107 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.385× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change |
| [[CFPAC-1 (line)]] | alt | 27.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.03× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[CHP-212 (line)]] | wt | 66.8 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.121× (z -11.1) |
| [[COLO 205 (line)]] | alt | 42.4 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.35× (z +8.7) | — |
| [[H4 (line)]] | wt | 66.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.260× (z -13.1) |
| [[NCI-H1573 (line)]] | alt | 24.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.78× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~87% of this change | — |
| [[RKO (line)]] | wt | 46.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +9.3) | — |
| [[SHP-77 (line)]] | alt | 133 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.426× (z -10.0) |
| [[SW 1271 (line)]] | alt | 103 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.106× (z -9.7) |
| [[SW 900 (line)]] | alt | 64.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.402× (z -8.6) |
| [[BT-474 (line)]] | alt | 63.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 66.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 78.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 48.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 47.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 38.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 87.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 44.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 65.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 46.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 52.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 71.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 60.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 52.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 49.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 46.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 582), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CIT]] | +0.82 | +0.81 / +0.71 | both halves | 7e-06 |  |
| [[PARPBP]] | +0.81 | +0.80 / +0.76 | both halves | 7e-06 |  |
| [[PBK]] | +0.81 | +0.80 / +0.73 | both halves | 7e-06 |  |
| [[NEIL3]] | +0.79 | +0.82 / +0.69 | both halves | 7e-06 |  |
| [[CENPI]] | +0.77 | +0.76 / +0.69 | both halves | 7e-06 |  |
| [[BUB1B]] | +0.77 | +0.79 / +0.68 | both halves | 7e-06 |  |
| [[CDCA3]] | +0.76 | +0.79 / +0.67 | both halves | 7e-06 |  |
| [[CEP85]] | +0.75 | +0.75 / +0.69 | both halves | 7e-06 |  |
| [[NUF2]] | +0.75 | +0.77 / +0.65 | both halves | 7e-06 |  |
| [[SPAG5]] | +0.75 | +0.78 / +0.67 | both halves | 7e-06 |  |
| [[NCAPD3]] | +0.74 | +0.71 / +0.68 | both halves | 7e-06 |  |
| [[INCENP]] | +0.74 | +0.73 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02257]] | B | LINC02257 activity lowers MPHOSPH9's level | lines that do not express LINC02257 (15) vs lines expressing it (35) | 1.58× higher at baseline in the lines without LINC02257 | 0.004 | ⚠ within organs, on part of the lines; also absent: CTSS, PAG1, ZNF365; maybe low, not absent |
| [[LINC02257]] | B | LINC02257 activity strengthens MPHOSPH9's drug response | lines that do not express LINC02257 (15) vs lines expressing it (33) | the lines without LINC02257 respond 0.96× as strongly (z diff +0.22); strongest at Dinaciclib 5 µM: 0.94x vs 1.69x (z diff +5.1) | 0.071 | ⚠ within organs, on part of the lines; also absent: CTSS, PAG1, ZNF365; maybe low, not absent; target measured in part of the lines; both ways; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 067]] — E2F targets; 73 genes; every member is in the + arm (projection on the module's main direction 0.835). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-33.7, -53.7); signed map (-46.3, -40.2). **Vector** length 131, 39.1% of its response variance represented; |z| ≥ 3 in 1,232 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.70 to 12); *G2/M checkpoint* (hallmark, mean cos +0.70 to 9); *Mitotic Prometaphase* (reactome, mean cos +0.69 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~35% of this change | +4.8 | +4.1 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.6 | +14.7 |
|  | [[NG25 (drug)]] 5 µM |  | +4.5 | +3.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.5 | +17.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.4 | +19.3 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +3.6 | +8.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.5 | +4.4 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.3 | +2.5 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.3 | +3.2 |
|  | [[Ipatasertib (drug)]] 5 µM |  | +2.2 | +1.7 |
| fall | [[Auranofin (drug)]] 5 µM |  | -10.4 | -14.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | -10.2 | -11.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -8.4 | -9.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.7 | -10.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -6.9 | -10.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.1 | -7.6 |
|  | [[Amsacrine (drug)]] 5 µM |  | -3.9 | -2.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.5 | -6.1 |

## What is on record

|  |  |
|---|---|
| Name | M-phase phosphoprotein 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.31 — chr12:123,152,320-123,244,014 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MPP9 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99550](https://www.uniprot.org/uniprotkb/Q99550) (M-phase phosphoprotein 9):

> Negatively regulates cilia formation by recruiting the CP110-CEP97 complex (a negative regulator of ciliogenesis) at the distal end of the mother centriole in ciliary cells. At the beginning of cilia formation, MPHOSPH9 undergoes TTBK2-mediated phosphorylation and degradation via the ubiquitin-proteasome system and removes itself and the CP110-CEP97 complex from the distal end of the mother centriole, which subsequently promotes cilia formation.

**Summary**, from NCBI Gene [10198](https://www.ncbi.nlm.nih.gov/gene/10198):

> Involved in negative regulation of cilium assembly. Located in Golgi apparatus and microtubule organizing center. Implicated in multiple sclerosis. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:7215](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7215) · Entrez [10198](https://www.ncbi.nlm.nih.gov/gene/10198) · UniProt [Q99550](https://www.uniprot.org/uniprotkb/Q99550) · Ensembl [ENSG00000051825](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000051825)

## Data

Gene col 582: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 582); `tables/drug_effects.parquet` (64 rows, flagged included); `relations/gene_relations.parquet` (col_a == 582, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 582]; `tensor/DDL_lfc|DDL_z.npy` [582]; `embed/gene_vectors.npy` [582]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 582 or target_col == 582). Every well: [[MPHOSPH9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MPHOSPH9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
