---
symbol: "DDX27"
type: "gene"
col: 4509
ensembl_id: "ENSG00000124228"
name: "DEAD-box helicase 27"
location: "20q13.13"
module: 11
arm: "+"
pooled_cpm: 99.74
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 2
n_dd_up_clean: 8
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# DDX27

*DEAD-box helicase 27* — 20q13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 2.01× (z +9.0, q 1e-16, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Folic acid (drug)]] 5 µM: 0.820× (z -3.6, q 0.089, down in 22 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NSRP1]] (+0.68, fdr 7e-06), [[DNTTIP2]] (+0.67, fdr 7e-06), [[BOD1L1]] (+0.67, fdr 7e-06); moves opposite to [[C4orf46]] (-0.61, fdr 1e-05), [[TWSG1]] (-0.60, fdr 7e-06), [[LSM4]] (-0.58, fdr 1e-05).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 12 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4509.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.01×** | +9.0 | 1e-16 | 46/48 (HT-29, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | **1.92×** | +8.4 | 1e-14 | 44/49 (NCI-H23, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.83×** | +7.8 | 9e-13 | 46/48 (HT-29, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **1.51×** | +7.5 | 1e-11 | 34/48 (LS 180, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.82×** | +7.4 | 1e-11 | 45/48 (NCI-H1573, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.77×** | +7.4 | 1e-11 | 44/48 (NCI-H1573, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.72×** | +7.0 | 2e-10 | 46/48 (BT-474, HEC-1-A, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.72×** | +7.0 | 2e-10 | 46/48 (HT-29, HEC-1-A, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | **1.75×** | +7.0 | 2e-10 | 36/44 (A498, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.62×** | +6.2 | 3e-08 | 43/48 (RKO, J82, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.58×** | +5.9 | 2e-07 | 41/48 (J82, SNU-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.59×** | +5.7 | 7e-07 | 40/48 (PANC-1, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.57×** | +5.6 | 1e-06 | 37/47 (J82, HT-29, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **1.47×** | +5.0 | 2e-05 | 37/48 (AsPC-1, BT-474, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.45×** | +4.8 | 5e-05 | 37/48 (LOX-IMVI, PANC-1, …) | all doses, stronger at high dose |  |
| [[Bendamustine (drug)]] 5 µM |  | **1.28×** | +3.1 | 0.060 | 26/48 (BT-474, MIA PaCa-2, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4509.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Folic acid (drug)]] 5 µM |  | **0.820×** | -3.6 | 0.089 | 22/48 (Hs 766T, MIA PaCa-2, …) | top dose only |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.816×** | -3.6 | 0.089 | 28/48 (A-427, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.760× | -3.3 | 0.21 | 26/48 (MIA PaCa-2, C-33 A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, +0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4509. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 51.9 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +13.2) ⚠ cell-cycle shift, explains ~65% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.96× (z +9.7) | — |
| [[NCI-H1573 (line)]] | alt | 80.6 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +11.2) ⚠ cell-cycle shift, explains ~65% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.80× (z +10.7) | — |
| [[BT-474 (line)]] | alt | 167 | 3 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.16× (z +12.0) | — |
| [[LOX-IMVI (line)]] | wt | 82.7 | 3 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.21× (z +11.0) | — |
| [[A498 (line)]] | wt | 80.8 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.63× (z +10.4) | — |
| [[HT-29 (line)]] | alt | 96.7 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.51× (z +12.1) | — |
| [[SNU-1 (line)]] | wt | 71.2 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +9.5) ⚠ cell-cycle shift, explains ~65% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.47× (z +9.0) | — |
| [[SW480 (line)]] | alt | 126 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.52× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.31× (z +8.9) | — |
| [[A-172 (line)]] | wt | 56.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.22× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | — |
| [[AsPC-1 (line)]] | alt | 145 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.06× (z +11.0) ⚠ cell-cycle shift, explains ~65% of this change | — |
| [[COLO 205 (line)]] | alt | 86.2 | 1 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 7.68× (z +8.8) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[H4 (line)]] | wt | 53.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.82× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | — |
| [[HCT15 (line)]] | alt | 85.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.28× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | — |
| [[HEC-1-A (line)]] | alt | 70.1 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.44× (z +9.0) | — |
| [[HOP62 (line)]] | alt | 69.4 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.89× (z +10.6) | — |
| [[Hs 766T (line)]] | wt | 128 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.89× (z +9.9) | — |
| [[J82 (line)]] | alt | 190 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.44× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | — |
| [[LoVo (line)]] | wt | 49.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +9.8) ⚠ cell-cycle shift, explains ~65% of this change | — |
| [[NCI-H1792 (line)]] | alt | 56.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.16× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | — |
| [[NCI-H23 (line)]] | alt | 224 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.21× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | — |
| [[SNU-423 (line)]] | alt | 85.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.89× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | — |
| [[SW 900 (line)]] | alt | 68.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +9.9) ⚠ cell-cycle shift, explains ~65% of this change | — |
| [[A-427 (line)]] | wt | 140 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 76.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 65.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 104 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 72.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 77.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 84.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 107 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 69.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 55.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 155 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 97.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 84.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 82.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 72.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 92.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 151 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 94.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 76.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 126 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 81.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 217 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 103 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4509), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NSRP1]] | +0.68 | +0.70 / +0.68 | both halves | 7e-06 |  |
| [[DNTTIP2]] | +0.67 | +0.71 / +0.64 | both halves | 7e-06 | STRING 444 |
| [[BOD1L1]] | +0.67 | +0.73 / +0.63 | both halves | 7e-06 |  |
| [[DNAJC2]] | +0.65 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[SNW1]] | +0.65 | +0.74 / +0.56 | both halves | 1e-05 |  |
| [[NOL8]] | +0.65 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[FAM32A]] | +0.64 | +0.75 / +0.54 | both halves | 1e-05 |  |
| [[RBM25]] | +0.64 | +0.63 / +0.59 | both halves | 7e-06 | STRING 458 |
| [[CEBPZ]] | +0.63 | +0.68 / +0.63 | both halves | 7e-06 | STRING 910 |
| [[ESF1]] | +0.63 | +0.69 / +0.59 | both halves | 7e-06 | STRING 818 |
| [[CWC22]] | +0.62 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[BDP1]] | +0.62 | +0.69 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C4orf46]] | -0.61 | -0.56 / -0.57 | both halves | 1e-05 |  |
| [[TWSG1]] | -0.60 | -0.61 / -0.61 | both halves | 7e-06 |  |
| [[LSM4]] | -0.58 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[C12orf75]] | -0.57 | -0.67 / -0.51 | both halves | 1e-05 |  |
| [[SLC25A40]] | -0.56 | -0.58 / -0.48 | both halves | 2e-05 |  |
| [[CALM3]] | -0.56 | -0.58 / -0.62 | both halves | 7e-06 |  |
| [[EZH2]] | -0.54 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[STT3B]] | -0.54 | -0.56 / -0.49 | both halves | 1e-05 |  |
| [[TENT4A]] | -0.53 | -0.58 / -0.56 | both halves | 1e-05 |  |
| [[TMEM106C]] | -0.53 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[SEC61A2]] | -0.53 | -0.47 / -0.56 | both halves | 2e-05 |  |
| [[GGH]] | -0.53 | -0.52 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.516). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-39.8, 0.1); signed map (-2.0, -17.4). **Vector** length 87.0, 29.6% of its response variance represented; |z| ≥ 3 in 971 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.9 | +4.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +4.6 | +7.8 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +4.5 | +5.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.5 | +7.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.4 | +2.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.3 | +7.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.6 | +1.3 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.0 | +2.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | +0.9 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.4 | +1.9 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.3 | +0.3 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.3 | -1.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.2 | -3.3 |
|  | [[Clonidine (hydrochloride) (drug)]] 5 µM |  | -1.9 | -1.7 |
|  | [[Lopinavir (drug)]] 5 µM |  | -1.9 | -2.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.9 | -1.0 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -1.8 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | DEAD-box helicase 27 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.13 — chr20:49,219,347-49,244,077 (+) |
| Ensembl biotype | protein_coding |
| Also known as | dJ686N3.1, DRS1 |
| Gene groups (HGNC) | DEAD-box helicases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96GQ7](https://www.uniprot.org/uniprotkb/Q96GQ7) (Probable ATP-dependent RNA helicase DDX27):

> Probable ATP-dependent RNA helicase. Component of the nucleolar ribosomal RNA (rRNA) processing machinery that regulates 3' end formation of ribosomal 47S rRNA.

**Summary**, from NCBI Gene [55661](https://www.ncbi.nlm.nih.gov/gene/55661):

> DEAD box proteins, characterized by the conserved motif Asp-Glu-Ala-Asp (DEAD), are putative RNA helicases. They are implicated in a number of cellular processes involving alteration of RNA secondary structure such as translation initiation, nuclear and mitochondrial splicing, and ribosome and spliceosome assembly. Based on their distribution patterns, some members of this family are believed to be involved in embryogenesis, spermatogenesis, and cellular growth and division. This gene encodes a …

**Accessions** — [HGNC:15837](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15837) · Entrez [55661](https://www.ncbi.nlm.nih.gov/gene/55661) · UniProt [Q96GQ7](https://www.uniprot.org/uniprotkb/Q96GQ7) · Ensembl [ENSG00000124228](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000124228)

## Data

Gene col 4509: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4509); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4509, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4509]; `tensor/DDL_lfc|DDL_z.npy` [4509]; `embed/gene_vectors.npy` [4509]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4509 or target_col == 4509). Every well: [[DDX27 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DDX27.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
