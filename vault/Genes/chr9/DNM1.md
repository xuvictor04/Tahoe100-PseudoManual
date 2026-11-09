---
symbol: "DNM1"
type: "gene"
col: 2816
ensembl_id: "ENSG00000106976"
name: "dynamin 1"
location: "9q34.11"
module: 57
arm: "+"
pooled_cpm: 32.97
n_lines_expressing: 45
n_dd_up: 17
n_dd_down: 19
n_dd_up_clean: 12
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 0
direction_downstream: 3
tags: ["gene", "module/057"]
generated_by: "tahoemap"
---

# DNM1

*dynamin 1* — 9q34.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.99× (z +13.1, q 1e-36, up in 32 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.673× (z -10.7, q 8e-24, down in 29 of 42 measured lines) ⚠ cell-cycle shift, explains ~69% of this change. The strongest without an alert is [[PH-797804 (drug)]] 5 µM: 0.482× (z -7.1, q 2e-10, down in 24 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAPRE3]] (+0.63, fdr 1e-05), [[SUDS3]] (+0.60, fdr 3e-05), [[PLXND1]] (+0.58, fdr 1e-05); moves opposite to [[PDCD7]] (-0.57, fdr 2e-05), [[LATS1]] (-0.56, fdr 3e-05), [[PPP1R8]] (-0.54, fdr 7e-05).
> It sits in the **+** arm of [[Module 057]] (Peroxisomal protein import).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 3 go from it, the strongest it → [[ZNF330]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 6 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2816.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.99×** | +13.1 | 1e-36 | 32/42 (RKO, KATO III, …) | all doses, flat | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.92×** | +12.4 | 6e-33 | 30/42 (J82, SW480, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.88×** | +12.1 | 2e-31 | 23/36 (NCI-H1792, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.55×** | +11.9 | 2e-30 | 30/43 (RKO, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.85×** | +11.8 | 5e-30 | 27/42 (RKO, KATO III, …) | all doses, flat | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.74×** | +10.2 | 2e-22 | 20/28 (A-172, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~1% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.70×** | +10.2 | 3e-22 | 27/42 (LOX-IMVI, PANC-1, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.66×** | +9.7 | 3e-20 | 26/42 (SW480, A-172, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.72×** | +9.6 | 7e-20 | 16/31 (A-172, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~4% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.58×** | +8.7 | 2e-16 | 25/42 (SW480, A-172, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.54×** | +7.8 | 3e-13 | 24/41 (SW480, J82, …) | all doses, flat |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.47×** | +7.3 | 1e-11 | 24/41 (A-172, J82, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.46×** | +7.2 | 3e-11 | 23/42 (J82, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.76×** | +5.5 | 1e-06 | 17/43 (LOX-IMVI, HOP62, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.26×** | +4.4 | 3e-04 | 20/42 (A-172, HOP62, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.16× | +3.8 | 0.006 | 9/43 (HEC-1-A, MIA PaCa-2, …) | all doses, flat |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.31×** | +3.7 | 0.008 | 12/43 (SW480, A-172, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.19× | +3.4 | 0.022 | 6/42 (HEC-1-A, A549, …) | two highest doses |  |
| [[Brivudine (drug)]] 0.5 µM |  | **1.28×** | +3.4 | 0.022 | 9/43 (J82, NCI-H23, …) | rises with dose | noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 1.12× | +3.2 | 0.041 | 5/43 (NCI-H23, LOX-IMVI, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 12 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2816.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **0.673×** | -10.7 | 8e-24 | 29/42 (HEC-1-A, COLO 205, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.597×** | -9.8 | 2e-20 | 30/39 (COLO 205, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.664×** | -7.8 | 1e-12 | 25/42 (LoVo, COLO 205, …) | all doses, stronger at high dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.482×** | -7.1 | 2e-10 | 24/38 (HEC-1-A, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.496×** | -6.8 | 1e-09 | 23/42 (LoVo, COLO 205, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.696×** | -6.6 | 3e-09 | 26/41 (COLO 205, LoVo, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.708×** | -6.6 | 4e-09 | 26/41 (LoVo, SW1417, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.717×** | -6.3 | 2e-08 | 23/42 (RKO, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.724×** | -6.1 | 5e-08 | 20/42 (LoVo, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.804×** | -5.9 | 2e-07 | 21/43 (A498, SW480, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.745×** | -5.6 | 1e-06 | 21/41 (AsPC-1, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.751×** | -5.1 | 1e-05 | 18/42 (HEC-1-A, SW48, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.931× | -4.8 | 8e-05 | 5/43 (LOX-IMVI, C-33 A, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.838× | -4.8 | 8e-05 | 18/43 (AsPC-1, A498, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~70% of this change | **0.789×** | -4.5 | 2e-04 | 22/40 (HOP62, AsPC-1, …) | inconsistent across doses | low cells (technical?) |
| [[EX229 (drug)]] 5 µM |  | **0.642×** | -4.3 | 5e-04 | 17/40 (LoVo, LS 180, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.820×** | -3.8 | 0.005 | 13/42 (MIA PaCa-2, A498, …) | all doses, stronger at high dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.804×** | -3.0 | 0.084 | 8/40 (HCT15, HEC-1-A, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, -0.44 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2816. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 32.1 | 6 (5 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 5.07× (z +13.4) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 4.06× (z +11.6) | — |
| [[HEC-1-A (line)]] | alt | 100 | 3 (2 ⚠) | 3 (3 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.60× (z +11.8) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 2.25× (z +10.0) | [[Homoharringtonine (drug)]] 5 µM 0.406× (z -15.8) ⚠ cell-cycle shift, explains ~69% of this change |
| [[COLO 205 (line)]] | alt | 55.3 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -15.0) ⚠ cell-cycle shift, explains ~69% of this change |
| [[LoVo (line)]] | wt | 31.5 | 0 | 5 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.268× (z -12.2) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.156× (z -8.8) |
| [[SW480 (line)]] | alt | 45.0 | 3 (2 ⚠) | 1 | [[Ixazomib citrate (drug)]] 5 µM 4.32× (z +16.8) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 3.73× (z +15.1) | [[Selinexor (drug)]] 5 µM 0.585× (z -8.8) |
| [[A498 (line)]] | wt | 93.8 | 0 | 3 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.585× (z -9.3) |
| [[CFPAC-1 (line)]] | alt | 34.8 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.222× (z -11.7) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.463× (z -8.5) |
| [[HOP62 (line)]] | alt | 38.9 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.95× (z +10.7) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 2.56× (z +9.2) | [[Homoharringtonine (drug)]] 0.5 µM 0.358× (z -10.1) ⚠ cell-cycle shift, explains ~31% of this change |
| [[HT-29 (line)]] | alt | 151 | 0 | 3 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.423× (z -12.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[J82 (line)]] | alt | 41.2 | 2 (2 ⚠) | 1 | [[Ixazomib citrate (drug)]] 5 µM 3.43× (z +11.5) ⚠ cell-cycle shift, explains ~34% of this change | [[Selinexor (drug)]] 5 µM 0.517× (z -8.7) |
| [[AsPC-1 (line)]] | alt | 64.6 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.363× (z -13.4) ⚠ cell-cycle shift, explains ~69% of this change |
| [[RPMI-7951 (line)]] | alt | 50.2 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.427× (z -9.0) ⚠ cell-cycle shift, explains ~69% of this change |
| [[A549 (line)]] | wt | 69.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.51× (z +8.6) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 27.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.185× (z -8.5) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 11.4 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.273× (z -8.7) |
| [[KATO III (line)]] | alt | 9.03 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 8.68× (z +9.4) | — |
| [[LOX-IMVI (line)]] | wt | 19.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.195× (z -10.2) ⚠ cell-cycle shift, explains ~31% of this change |
| [[LS 180 (line)]] | wt | 27.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.251× (z -9.7) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 13.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.58× (z +10.8) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 16.2 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.90× (z +8.5) | — |
| [[RKO (line)]] | wt | 13.5 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 7.20× (z +9.5) | — |
| [[SHP-77 (line)]] | alt | 90.5 | 1 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.39× (z +8.6) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[A-427 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.19 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 29.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 21.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.38 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.37 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 8.40 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.74 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.19 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 9.13 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.50 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 26.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2816), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*55 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAPRE3]] | +0.63 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[SUDS3]] | +0.60 | +0.63 / +0.46 | both halves | 3e-05 |  |
| [[PLXND1]] | +0.58 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[CAMK2G]] | +0.58 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[CYP4F3]] | +0.58 | +0.65 / +0.53 | both halves | 1e-05 |  |
| [[MAPK9]] | +0.58 | +0.51 / +0.53 | both halves | 1e-05 | pathway: Toll Like Receptor 4 (TLR4) Cascade |
| [[MYH14]] | +0.57 | +0.52 / +0.44 | both halves | 3e-05 | pathway: EPH-Ephrin signaling |
| [[NXPE3]] | +0.57 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[NDRG3]] | +0.56 | +0.45 / +0.47 | both halves | 3e-05 |  |
| [[TALDO1]] | +0.55 | +0.52 / +0.41 | both halves | 4e-05 |  |
| [[ASAP3]] | +0.55 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[GSR]] | +0.55 | +0.50 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*45 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDCD7]] | -0.57 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[LATS1]] | -0.56 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[PPP1R8]] | -0.54 | -0.37 / -0.59 | both halves | 7e-05 |  |
| [[UTP23]] | -0.53 | -0.50 / -0.40 | both halves | 5e-05 |  |
| [[TMEM187]] | -0.53 | -0.38 / -0.53 | both halves | 6e-05 |  |
| [[RPP25L]] | -0.52 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[CPT2]] | -0.52 | -0.31 / -0.56 | both halves | 2e-04 |  |
| [[HELQ]] | -0.52 | -0.45 / -0.36 | both halves | 9e-05 |  |
| [[ERCC6L2-AS1]] | -0.51 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[SMIM19]] | -0.51 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[TPRN]] | -0.51 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[RBM8A]] | -0.51 | -0.46 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF330]] | B | DNM1 activity weakens ZNF330's drug response | lines that do not express DNM1 (5) vs lines expressing it (43) | the lines without DNM1 respond 1.48× as strongly (z diff -1.66); strongest at Homoharringtonine 5 µM: 3.86x vs 2.15x (z diff -2.7) | 0.045 | ⚠ within organs, on part of the lines; also absent: PKN3, STARD10; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[NDRG3]] | B | DNM1 activity raises NDRG3's level | lines that do not express DNM1 (5) vs lines expressing it (45) | 1.70× lower at baseline in the lines without DNM1 | 0.057 | ⚠ within organs, on part of the lines; also absent: PKN3, STARD10; maybe low, not absent |
| [[SLC45A4]] | B | DNM1 activity raises SLC45A4's level | lines that do not express DNM1 (5) vs lines expressing it (45) | 1.98× lower at baseline in the lines without DNM1 | 0.093 | ⚠ within organs, on part of the lines; also absent: PKN3, STARD10; maybe low, not absent |

## Where it sits

- **Module**: [[Module 057]] — Peroxisomal protein import; 86 genes; this gene is in the **+** arm (projection on the module's main direction 0.394). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-21.3, -8.1); signed map (-30.1, -27.8). **Vector** length 93.7, 20.4% of its response variance represented; |z| ≥ 3 in 1,080 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 0.5 µM |  | +8.2 | +9.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +8.0 | +8.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | +6.8 | +7.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.3 | +12.1 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.2 | +12.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.7 | +3.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.5 | +4.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.3 | +5.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.2 | +11.9 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | -7.0 | -10.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -6.8 | -9.8 |
|  | [[Selinexor (drug)]] 5 µM |  | -5.8 | -5.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.0 | -1.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | -3.4 | -6.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.9 | -7.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.5 | -5.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.4 | -3.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.2 | -1.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.7 | +2.7 |

## What is on record

|  |  |
|---|---|
| Name | dynamin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.11 — chr9:128,191,655-128,255,248 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously DNM |
| Gene groups (HGNC) | Pleckstrin homology domain containing; Dynamins |
| Reactome | 22 pathways, smallest: Formation of annular gap junctions; Gap junction degradation; Retrograde neurotrophin signalling |
| Matched by | ensembl_id |

**Function**, from UniProt [Q05193](https://www.uniprot.org/uniprotkb/Q05193) (Dynamin-1):

> Catalyzes the hydrolysis of GTP and utilizes this energy to mediate vesicle scission and participates in many forms of endocytosis, such as clathrin-mediated endocytosis or synaptic vesicle endocytosis as well as rapid endocytosis (RE). Associates to the membrane, through lipid binding, and self-assembles into rings and stacks of interconnected rings through oligomerization to form a helical polymer around the vesicle membrane leading to constriction of invaginated coated pits around their …

**Summary**, from NCBI Gene [1759](https://www.ncbi.nlm.nih.gov/gene/1759):

> This gene encodes a member of the dynamin subfamily of GTP-binding proteins. The encoded protein possesses unique mechanochemical properties used to tubulate and sever membranes, and is involved in clathrin-mediated endocytosis and other vesicular trafficking processes. Actin and other cytoskeletal proteins act as binding partners for the encoded protein, which can also self-assemble leading to stimulation of GTPase activity. More than sixty highly conserved copies of the 3' region of this gene …

**Accessions** — [HGNC:2972](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2972) · Entrez [1759](https://www.ncbi.nlm.nih.gov/gene/1759) · UniProt [Q05193](https://www.uniprot.org/uniprotkb/Q05193) · Ensembl [ENSG00000106976](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106976)

## Data

Gene col 2816: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2816); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2816, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2816]; `tensor/DDL_lfc|DDL_z.npy` [2816]; `embed/gene_vectors.npy` [2816]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2816 or target_col == 2816). Every well: [[DNM1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DNM1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
