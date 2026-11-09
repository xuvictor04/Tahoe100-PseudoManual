---
symbol: "BRD9"
type: "gene"
col: 385
ensembl_id: "ENSG00000028310"
name: "bromodomain containing 9"
location: "5p15.33"
module: 5
arm: "+"
pooled_cpm: 57.62
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 9
n_dd_up_clean: 9
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# BRD9

*bromodomain containing 9* — 5p15.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 1.45× (z +6.7, q 1e-08, up in 28 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 0.5 µM: 0.688× (z -6.8, q 5e-09, down in 39 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[REXO1]] (+0.68, fdr 7e-06), [[NOM1]] (+0.67, fdr 7e-06), [[IPO4]] (+0.67, fdr 9e-06); moves opposite to [[KBTBD3]] (-0.63, fdr 1e-05), [[C16orf87]] (-0.59, fdr 6e-05), [[LAMTOR2]] (-0.58, fdr 3e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 385.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.45×** | +6.7 | 1e-08 | 28/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.28×** | +6.4 | 6e-08 | 27/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.44×** | +5.8 | 1e-06 | 30/48 (Hs 766T, HT-29, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.36×** | +5.1 | 4e-05 | 26/45 (LS 180, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~6% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.32×** | +5.1 | 4e-05 | 26/48 (AsPC-1, SW480, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.32×** | +5.0 | 4e-05 | 27/49 (KATO III, LoVo, …) | all doses, flat | cell-cycle shift (explains ~5% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.32×** | +5.0 | 4e-05 | 28/48 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.31×** | +4.8 | 9e-05 | 27/48 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.58×** | +4.3 | 1e-03 | 26/49 (A498, BT-474, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.26×** | +4.2 | 0.002 | 24/48 (NCI-H460, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.55×** | +4.1 | 0.002 | 25/49 (NCI-H460, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.06× | +3.7 | 0.008 | 0/49 | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.46×** | +3.6 | 0.014 | 21/48 (PANC-1, Hs 766T, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 1.20× | +3.3 | 0.044 | 13/48 (C32, NCI-H1792, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.19× | +3.1 | 0.069 | 15/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 385.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.688×** | -6.8 | 5e-09 | 39/49 (NCI-H2347, A498, …) | two highest doses | cell-cycle shift (explains ~3% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.813×** | -5.4 | 2e-05 | 26/48 (A-172, CFPAC-1, …) | two highest doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.788×** | -4.4 | 0.002 | 24/49 (AsPC-1, MIA PaCa-2, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.801×** | -3.9 | 0.013 | 20/47 (AsPC-1, LoVo, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.819×** | -3.7 | 0.027 | 23/48 (J82, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Trametinib (drug)]] 0.05 µM |  | 0.874× | -3.5 | 0.039 | 12/48 (PANC-1, LoVo, …) | inconsistent across doses | position effect removed |
| [[Arbutin (drug)]] 5 µM |  | **0.821×** | -3.5 | 0.039 | 19/48 (KATO III, A-172, …) | top dose only | position effect removed |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | **0.830×** | -3.4 | 0.042 | 18/48 (PANC-1, SW1417, …) | inconsistent across doses | position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | 0.865× | -3.3 | 0.050 | 12/48 (AsPC-1, A-427, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Ixazomib (drug)]] 0.05 µM |  | **0.826×** | -3.3 | 0.050 | 17/47 (NCI-H2030, PANC-1, …) | inconsistent across doses | position effect removed |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.819×** | -3.2 | 0.061 | 13/49 (A-172, BT-474, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.889× | -3.1 | 0.093 | 12/48 (J82, A-427, …) | rises with dose | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 385. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 61.7 | 14 (7 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.78× (z +23.2) | — |
| [[NCI-H1573 (line)]] | alt | 45.4 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.80× (z +19.4) | — |
| [[PANC-1 (line)]] | alt | 60.4 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +10.4) | — |
| [[AsPC-1 (line)]] | alt | 58.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +8.5) | [[Lonafarnib (drug)]] 5 µM 0.0873× (z -12.4) ⚠ toxic |
| [[RKO (line)]] | wt | 64.7 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.347× (z -9.7) ⚠ toxic; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.513× (z -9.0) |
| [[LS 180 (line)]] | wt | 40.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.62× (z +8.5) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 59.4 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.55× (z +8.7) | — |
| [[NCI-H2030 (line)]] | alt | 69.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +8.6) | — |
| [[NCI-H23 (line)]] | alt | 31.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.235× (z -10.8) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 48.9 | 0 | 1 (1 ⚠) | — | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.135× (z -8.5) ⚠ toxic |
| [[SHP-77 (line)]] | alt | 88.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +9.6) | — |
| [[SW 900 (line)]] | alt | 71.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +13.1) | — |
| [[SW480 (line)]] | alt | 84.9 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.18× (z +9.3) ⚠ cell-cycle shift, explains ~24% of this change | — |
| [[A-172 (line)]] | wt | 46.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 84.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 52.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 63.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 53.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 70.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 55.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 27.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 54.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 53.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 77.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 78.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 87.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 48.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 33.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 57.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 76.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 51.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 72.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 34.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 73.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 52.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 52.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 60.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 79.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 44.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 55.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 69.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 50.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 58.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 59.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 57.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 49.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 64.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 385), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[REXO1]] | +0.68 | +0.59 / +0.66 | both halves | 7e-06 |  |
| [[NOM1]] | +0.67 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[IPO4]] | +0.67 | +0.57 / +0.66 | both halves | 9e-06 |  |
| [[ARMC6]] | +0.67 | +0.50 / +0.71 | both halves | 1e-05 |  |
| [[DHX34]] | +0.66 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[GRWD1]] | +0.65 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[CEP170B]] | +0.65 | +0.57 / +0.66 | both halves | 1e-05 |  |
| [[PUS1]] | +0.65 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[RBM19]] | +0.65 | +0.50 / +0.69 | both halves | 1e-05 |  |
| [[MTA1]] | +0.65 | +0.48 / +0.72 | both halves | 2e-05 | pathway: ATP-dependent chromatin remodelers |
| [[GNL3L]] | +0.64 | +0.49 / +0.68 | both halves | 1e-05 |  |
| [[DMWD]] | +0.63 | +0.52 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KBTBD3]] | -0.63 | -0.51 / -0.64 | both halves | 1e-05 |  |
| [[C16orf87]] | -0.59 | -0.38 / -0.68 | both halves | 6e-05 |  |
| [[LAMTOR2]] | -0.58 | -0.45 / -0.62 | both halves | 3e-05 |  |
| [[HOXA5]] | -0.58 | -0.50 / -0.60 | both halves | 1e-05 |  |
| [[AKAP1-DT]] | -0.57 | -0.34 / -0.65 | both halves | 1e-04 |  |
| [[PGAP1]] | -0.56 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[LGR4]] | -0.56 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[DENND4C]] | -0.56 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[DPM3]] | -0.56 | -0.41 / -0.58 | both halves | 4e-05 |  |
| [[TRIM52-AS1]] | -0.55 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[ATP5IF1]] | -0.55 | -0.40 / -0.54 | both halves | 5e-05 |  |
| [[COX7C]] | -0.55 | -0.42 / -0.55 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.615). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-14.6, -31.9); signed map (0.2, -47.8). **Vector** length 104, 24.5% of its response variance represented; |z| ≥ 3 in 840 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +7.7 | +2.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.5 | +5.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.3 | +5.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.6 | +5.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.0 | +5.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.9 | +1.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.2 | +0.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.7 | +0.3 |
|  | [[EX229 (drug)]] 5 µM |  | +2.4 | +1.8 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.8 | -5.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -4.6 | -6.8 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.4 | -3.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.2 | -4.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.9 | -2.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.9 | -2.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.8 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | bromodomain containing 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5p15.33 — chr5:850,291-892,801 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ13441, SMARCI2 |
| Gene groups (HGNC) | Bromodomain containing; BAF complex subunits; GBAF complex subunits |
| Reactome | 4 pathways, smallest: Formation of the non-canonical BAF (ncBAF) complex; SWI/SNF chromatin remodelers; ATP-dependent chromatin remodelers |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H8M2](https://www.uniprot.org/uniprotkb/Q9H8M2) (Bromodomain-containing protein 9):

> Plays a role in chromatin remodeling and regulation of transcription. Acts as a chromatin reader that recognizes and binds acylated histones: binds histones that are acetylated and/or butyrylated. Component of SWI/SNF chromatin remodeling subcomplex GBAF that carries out key enzymatic activities, changing chromatin structure by altering DNA-histone contacts within a nucleosome in an ATP-dependent manner. Also orchestrates the RAD51-RAD54 complex formation and thereby plays a role in homologous …

**Summary**, from NCBI Gene [65980](https://www.ncbi.nlm.nih.gov/gene/65980):

> Enables histone reader activity. Involved in double-strand break repair via homologous recombination. Located in nucleoplasm. Part of SWI/SNF complex. Is active in site of double-strand break. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25818](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25818) · Entrez [65980](https://www.ncbi.nlm.nih.gov/gene/65980) · UniProt [Q9H8M2](https://www.uniprot.org/uniprotkb/Q9H8M2) · Ensembl [ENSG00000028310](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000028310)

## Data

Gene col 385: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 385); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 385, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 385]; `tensor/DDL_lfc|DDL_z.npy` [385]; `embed/gene_vectors.npy` [385]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 385 or target_col == 385). Every well: [[BRD9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BRD9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
