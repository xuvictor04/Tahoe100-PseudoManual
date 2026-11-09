---
symbol: "MED14"
type: "gene"
col: 11084
ensembl_id: "ENSG00000180182"
name: "mediator complex subunit 14"
location: "Xp11.4"
module: 12
arm: "-"
pooled_cpm: 97.41
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 7
n_dd_up_clean: 6
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# MED14

*mediator complex subunit 14* — Xp11.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.23× (z +8.3, q 5e-14, up in 40 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.626× (z -9.3, q 1e-17, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AGPAT1]] (+0.60, fdr 1e-05), [[FAM234A]] (+0.59, fdr 3e-05), [[CDKN2AIPNL]] (+0.59, fdr 4e-05); moves opposite to [[DNAJC2]] (-0.67, fdr 1e-05), [[NOXRED1]] (-0.66, fdr 7e-06), [[CCDC59]] (-0.65, fdr 7e-06).
> It sits in the **-** arm of [[Module 012]] (mRNA Splicing - Major Pathway).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11084.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.23×** | +8.3 | 5e-14 | 40/49 (BT-474, Panc 03.27, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.43×** | +7.0 | 5e-10 | 36/48 (BT-474, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.38×** | +6.4 | 3e-08 | 34/48 (PANC-1, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.38×** | +6.3 | 4e-08 | 32/48 (BT-474, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.28×** | +4.9 | 1e-04 | 26/48 (BT-474, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.27×** | +4.5 | 6e-04 | 22/48 (RPMI-7951, J82, …) | top dose only | cell-cycle shift (explains ~6% here); composition shift |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~7% of this change | **1.23×** | +4.1 | 0.003 | 26/47 (NCI-H460, BT-474, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.45×** | +3.9 | 0.008 | 23/48 (BT-474, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~9% of this change | 1.18× | +3.3 | 0.055 | 17/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~15% of this change | 1.19× | +3.3 | 0.055 | 23/47 (J82, NCI-H460, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11084.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.626×** | -9.3 | 1e-17 | 43/48 (SW480, SK-MEL-2, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.739×** | -8.5 | 7e-15 | 34/49 (A549, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.773×** | -4.8 | 3e-04 | 31/48 (NCI-H2347, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.795×** | -4.5 | 8e-04 | 25/48 (CFPAC-1, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.810×** | -4.2 | 0.004 | 26/48 (NCI-H2347, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.820×** | -3.9 | 0.008 | 19/49 (AN3 CA, A-427, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.945× | -3.9 | 0.009 | 1/50 (NCI-H23) | inconsistent across doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.872× | -3.8 | 0.009 | 5/48 (Hs 766T, LOX-IMVI, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.822×** | -3.7 | 0.012 | 21/48 (C32, A-427, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.881× | -3.5 | 0.023 | 24/48 (AN3 CA, A-427, …) | all doses, flat | composition shift |
| [[Trametinib (drug)]] 0.5 µM |  | 0.866× | -3.2 | 0.063 | 16/48 (A-427, C32, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.05 µM |  | 0.842× | -3.2 | 0.075 | 15/48 (BT-474, A-172, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11084. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 71.3 | 9 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +15.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 3.43× (z +12.1) | — |
| [[J82 (line)]] | alt | 137 | 5 (2 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 2.62× (z +11.5) | — |
| [[NCI-H460 (line)]] | wt | 95.7 | 5 (3 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.15× (z +10.8) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 2.09× (z +10.5) | — |
| [[Panc 03.27 (line)]] | alt | 97.5 | 3 (1 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.30× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.443× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 123 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.527× (z -11.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 109 | 2 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +8.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.22× (z +8.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.496× (z -11.3) |
| [[RPMI-7951 (line)]] | alt | 141 | 1 | 2 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 3.20× (z +12.5) | [[Dinaciclib (drug)]] 5 µM 0.422× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.459× (z -8.7) |
| [[A-172 (line)]] | wt | 99.5 | 2 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 2.61× (z +9.9) | — |
| [[AN3 CA (line)]] | alt | 197 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.156× (z -14.8) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 72.4 | 0 | 2 | — | [[Sonidegib (drug)]] 5 µM 0.0934× (z -11.2) |
| [[NCI-H2347 (line)]] | alt | 114 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.587× (z -11.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.518× (z -9.6) |
| [[PANC-1 (line)]] | alt | 72.2 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.49× (z +11.8) | — |
| [[SNU-423 (line)]] | alt | 140 | 1 | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.25× (z +8.6) | [[Auranofin (drug)]] 5 µM 0.449× (z -8.5) |
| [[A498 (line)]] | wt | 84.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +10.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[C-33 A (line)]] | alt | 191 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.468× (z -8.7) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 96.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.532× (z -9.4) |
| [[CFPAC-1 (line)]] | alt | 76.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +11.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[Hs 766T (line)]] | wt | 116 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +11.1) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[LoVo (line)]] | wt | 77.7 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.84× (z +10.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 90.2 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 2.59× (z +9.9) | — |
| [[NCI-H1573 (line)]] | alt | 120 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.76× (z +10.0) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 83.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.423× (z -9.4) |
| [[RKO (line)]] | wt | 107 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.529× (z -10.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 73.8 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.384× (z -10.3) |
| [[SW 1088 (line)]] | alt | 108 | 0 | 1 (1 ⚠) | — | [[Fingolimod (hydrochloride) (drug)]] 5 µM 0.0777× (z -10.3) ⚠ toxic |
| [[SW480 (line)]] | alt | 156 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.489× (z -10.8) |
| [[AsPC-1 (line)]] | alt | 92.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 63.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 71.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 85.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 133 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 56.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 58.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 67.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 82.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 108 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 106 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 56.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 96.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 61.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 44.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 90.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 93.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 86.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 68.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 61.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 55.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 181 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11084), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*42 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AGPAT1]] | +0.60 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[FAM234A]] | +0.59 | +0.45 / +0.46 | both halves | 3e-05 |  |
| [[CDKN2AIPNL]] | +0.59 | +0.47 / +0.41 | both halves | 4e-05 |  |
| [[GGH]] | +0.58 | +0.56 / +0.46 | both halves | 3e-05 |  |
| [[FKBP1A]] | +0.57 | +0.66 / +0.46 | both halves | 3e-05 |  |
| [[TMEM106C]] | +0.57 | +0.53 / +0.47 | both halves | 2e-05 |  |
| [[RBBP7]] | +0.57 | +0.54 / +0.56 | both halves | 1e-05 | pathway: Adipogenesis |
| [[APEH]] | +0.57 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[CDK2]] | +0.56 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[EML4]] | +0.55 | +0.58 / +0.46 | both halves | 3e-05 |  |
| [[ATP13A3]] | +0.55 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[EPB41L2]] | +0.55 | +0.48 / +0.56 | both halves | 2e-05 |  |

## Genes that move opposite

*58 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAJC2]] | -0.67 | -0.66 / -0.54 | both halves | 1e-05 |  |
| [[NOXRED1]] | -0.66 | -0.59 / -0.66 | both halves | 7e-06 |  |
| [[CCDC59]] | -0.65 | -0.65 / -0.63 | both halves | 7e-06 |  |
| [[LRSAM1]] | -0.64 | -0.59 / -0.62 | both halves | 7e-06 |  |
| [[SLC4A1AP]] | -0.61 | -0.64 / -0.50 | both halves | 1e-05 |  |
| [[FNBP4]] | -0.61 | -0.57 / -0.46 | both halves | 2e-05 |  |
| [[UBXN4]] | -0.58 | -0.64 / -0.42 | both halves | 4e-05 |  |
| [[MRPL45P2]] | -0.58 | -0.62 / -0.50 | both halves | 1e-05 |  |
| [[LRIF1]] | -0.58 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[ATF4]] | -0.57 | -0.67 / -0.52 | both halves | 1e-05 |  |
| [[ZNF546]] | -0.57 | -0.59 / -0.47 | both halves | 2e-05 |  |
| [[SPAG7]] | -0.56 | -0.48 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **-** arm (projection on the module's main direction -0.429). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-47.7, -4.0); signed map (-29.5, -39.4). **Vector** length 98.4, 24.8% of its response variance represented; |z| ≥ 3 in 959 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.9 | +2.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~15% of this change | +3.9 | +3.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.3 | +1.1 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.2 | +0.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.0 | +0.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.8 | +1.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.6 | +1.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | +2.1 | +1.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +1.8 | +1.5 |
|  | [[Berbamine (drug)]] 0.05 µM |  | +1.5 | -0.1 |
| fall | [[Auranofin (drug)]] 5 µM |  | -8.3 | -9.3 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -6.9 | -4.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -6.0 | -3.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.7 | -4.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.0 | -1.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.7 | -2.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.6 | -2.7 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -3.3 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | mediator complex subunit 14 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp11.4 — chrX:40,648,305-40,735,858 (-) |
| Ensembl biotype | protein_coding |
| Also known as | EXLM1, CRSP150, TRAP170, RGR1, CSRP; previously CXorf4, CRSP2 |
| Gene groups (HGNC) | Mediator complex |
| Reactome | 13 pathways, smallest: Transcriptional regulation of white adipocyte differentiation; RSV-host interactions; Epigenetic regulation of adipogenesis genes by MLL3 and MLL4 complexes |
| Matched by | ensembl_id |

**Function**, from UniProt [O60244](https://www.uniprot.org/uniprotkb/O60244) (Mediator of RNA polymerase II transcription subunit 14):

> Component of the Mediator complex, a coactivator involved in the regulated transcription of nearly all RNA polymerase II-dependent genes. Mediator functions as a bridge to convey information from gene-specific regulatory proteins to the basal RNA polymerase II transcription machinery. Mediator is recruited to promoters by direct interactions with regulatory proteins and serves as a scaffold for the assembly of a functional pre-initiation complex with RNA polymerase II and the general …

**Summary**, from NCBI Gene [9282](https://www.ncbi.nlm.nih.gov/gene/9282):

> The activation of gene transcription is a multistep process that is triggered by factors that recognize transcriptional enhancer sites in DNA. These factors work with co-activators to direct transcriptional initiation by the RNA polymerase II apparatus. The protein encoded by this gene is a subunit of the CRSP (cofactor required for SP1 activation) complex, which, along with TFIID, is required for efficient activation by SP1. This protein is also a component of other multisubunit complexes e.g. …

**Accessions** — [HGNC:2370](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2370) · Entrez [9282](https://www.ncbi.nlm.nih.gov/gene/9282) · UniProt [O60244](https://www.uniprot.org/uniprotkb/O60244) · Ensembl [ENSG00000180182](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000180182)

## Data

Gene col 11084: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11084); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11084, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11084]; `tensor/DDL_lfc|DDL_z.npy` [11084]; `embed/gene_vectors.npy` [11084]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11084 or target_col == 11084). Every well: [[MED14 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MED14.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
