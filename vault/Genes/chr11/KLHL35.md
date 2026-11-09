---
symbol: "KLHL35"
type: "gene"
col: 7353
ensembl_id: "ENSG00000149243"
name: "kelch like family member 35"
location: "11q13.4"
module: 12
arm: "+"
pooled_cpm: 2.86
n_lines_expressing: 40
n_dd_up: 4
n_dd_down: 20
n_dd_up_clean: 1
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# KLHL35

*kelch like family member 35* — 11q13.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.47× (z +6.8, q 6e-09, up in 1 of 2 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM: 1.50× (z +3.4, q 0.091, up in 5 of 20 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (6 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.292× (z -10.3, q 4e-22, down in 25 of 31 measured lines).
> Its strongest partners by |cos| (82 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 18 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MIF4GD]] (+0.50, fdr 3e-05), [[MFSD3]] (+0.50, fdr 4e-05), [[NUDT7]] (+0.48, fdr 1e-04); moves opposite to [[M6PR]] (-0.47, fdr 2e-04), [[PTMS]] (-0.41, fdr 2e-04), [[BST2]] (-0.41, fdr 0.001, ⚠ one half only (not replicated)), [[HLA-C]] (-0.41, fdr 1e-04).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 4 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7353.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.47×** | +6.8 | 6e-09 | 1/2 (NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.01×** | +5.4 | 2e-05 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.60×** | +3.9 | 0.015 | 2/12 (NCI-H2347, NCI-H460) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.50×** | +3.4 | 0.091 | 5/20 (NCI-H23, SNU-1, …) | inconsistent across doses | low cells (technical?) |
| [[XRK3F2 (drug)]] 0.5 µM |  | 1.69× | +3.1 | 0.19 | 2/14 (NCI-H460, J82) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | 1.45× | +3.1 | 0.19 | 4/16 (SW1417, Hs 766T, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7353.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.292×** | -10.3 | 4e-22 | 25/31 (PANC-1, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~8% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.300×** | -10.1 | 2e-21 | 23/33 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.516×** | -7.8 | 8e-13 | 21/25 (NCI-H23, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.398×** | -7.7 | 2e-12 | 20/29 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.518×** | -5.5 | 4e-06 | 20/31 (NCI-H23, SW1417, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.532×** | -5.3 | 1e-05 | 18/32 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.536×** | -4.7 | 2e-04 | 12/29 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.573×** | -4.7 | 2e-04 | 17/22 (PANC-1, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~24% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.573×** | -4.7 | 2e-04 | 18/32 (NCI-H23, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.592×** | -4.4 | 6e-04 | 11/33 (NCI-H2030, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.603×** | -4.2 | 0.001 | 12/21 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.609×** | -4.2 | 0.002 | 18/32 (NCI-H23, PANC-1, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.621×** | -4.0 | 0.003 | 14/30 (PANC-1, HT-29, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.414×** | -3.9 | 0.004 | 10/30 (NCI-H23, HOP62, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.635×** | -3.8 | 0.005 | 11/28 (HOP62, BT-474, …) | all doses, flat | cell-cycle shift (explains ~11% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.428×** | -3.7 | 0.007 | 11/22 (Hs 766T, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Erlotinib (drug)]] 0.05 µM |  | **0.657×** | -3.3 | 0.035 | 4/33 (A-172, COLO 205, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.695×** | -3.0 | 0.068 | 9/28 (HT-29, NCI-H23, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.38 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7353. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 13.0 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.124× (z -14.0) |
| [[PANC-1 (line)]] | alt | 6.43 | 0 | 5 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0806× (z -13.5) |
| [[J82 (line)]] | alt | 4.08 | 0 | 4 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0276× (z -12.9) |
| [[AsPC-1 (line)]] | alt | 3.06 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0914× (z -9.7) |
| [[HOP62 (line)]] | alt | 2.02 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0364× (z -10.1) |
| [[LS 180 (line)]] | wt | 3.18 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0416× (z -9.5) |
| [[NCI-H460 (line)]] | wt | 2.47 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.105× (z -8.7) |
| [[SW1417 (line)]] | alt | 3.26 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0594× (z -9.0) |
| [[SW480 (line)]] | alt | 1.60 | 0 | 1 | — | [[Benproperine (phosphate) (drug)]] 5 µM 0.0612× (z -8.8) |
| [[A-172 (line)]] | wt | 2.09 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.39 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.447 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.16 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.931 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.363 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.869 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.05 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.87 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.523 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 6.25 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.561 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.405 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.702 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.85 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.392 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.366 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.79 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.712 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 9.90 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.411 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.44 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.74 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7353), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 11 of them with an alert (⚠; 11 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MIF4GD]] | +0.50 | +0.46 / +0.43 | both halves | 3e-05 |  |
| [[MFSD3]] | +0.50 | +0.42 / +0.42 | both halves | 4e-05 |  |
| [[NUDT7]] | +0.48 | +0.41 / +0.35 | both halves | 1e-04 |  |
| [[SLC46A1]] | +0.48 | +0.38 / +0.45 | both halves | 6e-05 |  |
| [[HDDC3]] | +0.46 | +0.32 / +0.48 | both halves | 2e-04 |  |
| [[TMEM216]] | +0.43 | +0.33 / +0.46 | both halves | 1e-04 |  |
| [[RASGEF1A]] | +0.43 | +0.39 / +0.43 | both halves | 5e-05 |  |
| [[ABCA3]] | +0.43 | +0.45 / +0.36 | both halves | 1e-04 |  |
| [[CCDC51]] | +0.42 | +0.40 / +0.44 | both halves | 5e-05 |  |
| [[YDJC]] | +0.42 | +0.31 / +0.46 | both halves | 2e-04 |  |
| [[ZNF32]] | +0.42 | +0.39 / +0.41 | both halves | 6e-05 |  |
| [[FANCF]] | +0.42 | +0.33 / +0.36 | both halves | 1e-04 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest and the 5 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[M6PR]] | -0.47 | -0.30 / -0.42 | both halves | 2e-04 |  |
| [[PTMS]] | -0.41 | -0.39 / -0.31 | both halves | 2e-04 |  |
| [[BST2]] | -0.41 | -0.54 / -0.17 | ⚠ one half (not replicated) | 0.001 |  |
| [[HLA-C]] | -0.41 | -0.34 / -0.34 | both halves | 1e-04 |  |
| [[HLA-H]] | -0.41 | -0.24 / -0.55 | both halves | 5e-04 |  |
| [[CFI]] | -0.40 | -0.46 / -0.17 | ⚠ not reproduced | 0.001 |  |
| [[PPP2R1B]] | -0.39 | -0.32 / -0.43 | both halves | 2e-04 |  |
| [[ITM2B]] | -0.39 | -0.31 / -0.36 | both halves | 2e-04 |  |
| [[UMAD1]] | -0.39 | -0.43 / -0.15 | ⚠ not reproduced | 0.001 |  |
| [[GLA]] | -0.38 | -0.38 / -0.21 | both halves | 7e-04 |  |
| [[SPARC]] | -0.38 | -0.39 / -0.19 | ⚠ not reproduced | 8e-04 |  |
| [[APOL1]] | -0.38 | -0.47 / -0.13 | ⚠ not reproduced | 0.002 |  |
| [[RNF213]] | -0.38 | -0.35 / -0.34 | both halves | 1e-04 |  |
| [[RNF144A]] | -0.37 | -0.40 / -0.25 | both halves | 4e-04 |  |
| [[BCL2L2]] | -0.37 | -0.23 / -0.33 | both halves | 5e-04 |  |
| [[PI4K2B]] | -0.37 | -0.33 / -0.23 | both halves | 6e-04 |  |
| [[DNAJC13]] | -0.37 | -0.20 / -0.53 | both halves | 7e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.339). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-48.4, -13.0); signed map (-21.3, -5.2). **Vector** length 37.1, 4.78% of its response variance represented; |z| ≥ 3 in 770 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +1.5 | +1.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +1.2 | +2.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.1 | +2.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.1 | +0.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.1 | +0.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +0.7 | +3.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +0.7 | -3.7 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.7 | -10.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.4 | -4.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.1 | -7.7 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.9 | -10.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.7 | -4.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.4 | -2.5 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -0.6 | +0.5 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -0.6 | -1.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -0.6 | +0.3 |

## What is on record

|  |  |
|---|---|
| Name | kelch like family member 35 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.4 — chr11:75,422,394-75,433,203 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ33790 |
| Gene groups (HGNC) | Kelch like; BTB domain containing |
| Matched by | ensembl_id |

UniProt [Q6PF15](https://www.uniprot.org/uniprotkb/Q6PF15) carries no function annotation.

**Summary**, from NCBI Gene [283212](https://www.ncbi.nlm.nih.gov/gene/283212):

> Predicted to enable ubiquitin-like ligase-substrate adaptor activity. Predicted to be involved in proteasome-mediated ubiquitin-dependent protein catabolic process. Predicted to be part of Cul3-RING ubiquitin ligase complex. Predicted to be active in cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26597](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26597) · Entrez [283212](https://www.ncbi.nlm.nih.gov/gene/283212) · UniProt [Q6PF15](https://www.uniprot.org/uniprotkb/Q6PF15) · Ensembl [ENSG00000149243](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000149243)

## Data

Gene col 7353: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7353); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7353, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7353]; `tensor/DDL_lfc|DDL_z.npy` [7353]; `embed/gene_vectors.npy` [7353]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7353 or target_col == 7353). Every well: [[KLHL35 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KLHL35.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
