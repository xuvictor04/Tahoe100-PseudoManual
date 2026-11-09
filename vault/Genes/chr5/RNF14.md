---
symbol: "RNF14"
type: "gene"
col: 276
ensembl_id: "ENSG00000013561"
name: "ring finger protein 14"
location: "5q31.3"
module: 160
arm: "-"
pooled_cpm: 38.26
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 0
n_dd_up_clean: 7
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/160"]
generated_by: "tahoemap"
---

# RNF14

*ring finger protein 14* — 5q31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 0.5 µM: 1.36× (z +6.7, q 1e-08, up in 30 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 4 lines (NCI-H1573 0.253×, A-427 0.282×, NCI-H460 0.378×, AN3 CA 0.165×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (hTERT-HPNE 0.119×, SW1417 0.381×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H1573 0.203×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Saquinavir (drug)]] 0.5 µM in 1 line (NCI-H661 0.0647×); [[Arbutin (drug)]] 5 µM in 1 line (SW 1271 0.0789×); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (SK-MEL-2 0.363×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CLCC1]] (+0.60, fdr 3e-05), [[SVIL-AS1-1]] (+0.57, fdr 1e-05), [[PTPN9]] (+0.56, fdr 3e-05); moves opposite to [[MAGI1]] (-0.57, fdr 1e-05), [[DPY19L2P1]] (-0.53, fdr 2e-05), [[NR4A1]] (-0.52, fdr 4e-05).
> It sits in the **-** arm of [[Module 160]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 12 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 276.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.36×** | +6.7 | 1e-08 | 30/48 (PANC-1, NCI-H460, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.32×** | +6.0 | 4e-07 | 25/48 (PANC-1, NCI-H2030, …) | two highest doses | cell-cycle shift (explains ~17% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.22×** | +6.0 | 4e-07 | 23/48 (SW1417, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.64×** | +5.6 | 3e-06 | 22/48 (LoVo, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | 1.18× | +5.2 | 3e-05 | 16/48 (NCI-H2030, PANC-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **1.27×** | +4.9 | 9e-05 | 22/47 (LoVo, A498, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.24×** | +4.6 | 3e-04 | 15/48 (A498, LS 180, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.22×** | +4.3 | 0.001 | 15/48 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.21×** | +4.1 | 0.002 | 17/48 (KATO III, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.21×** | +4.1 | 0.002 | 18/48 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | 1.14× | +4.1 | 0.002 | 9/48 (PANC-1, A-427, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.21×** | +4.1 | 0.002 | 14/48 (NCI-H2030, A-172, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.22×** | +4.0 | 0.002 | 17/48 (PANC-1, NCI-H2030, …) | inconsistent across doses |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 1.19× | +3.7 | 0.009 | 8/47 (NCI-H460, A-172, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.4 | 0.021 | 16/48 (SW480, A-427, …) | all doses, flat |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.12× | +3.4 | 0.025 | 10/48 (A-172, NCI-H1792, …) | two highest doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 1.18× | +3.2 | 0.039 | 11/47 (C-33 A, hTERT-HPNE, …) | all doses, flat | low cells (technical?) |
| [[Neratinib (drug)]] 5 µM |  | 1.15× | +3.1 | 0.056 | 9/48 (A498, A-172, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 1.16× | +3.0 | 0.075 | 8/48 (SW480, C32, …) | inconsistent across doses |  |
| [[Erlotinib (drug)]] 0.05 µM |  | 1.16× | +2.9 | 0.084 | 5/48 (AN3 CA, NCI-H23, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 276.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 4 lines (NCI-H1573 0.253×, A-427 0.282×, NCI-H460 0.378×, AN3 CA 0.165×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (hTERT-HPNE 0.119×, SW1417 0.381×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H1573 0.203×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Saquinavir (drug)]] 0.5 µM in 1 line (NCI-H661 0.0647×); [[Arbutin (drug)]] 5 µM in 1 line (SW 1271 0.0789×); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (SK-MEL-2 0.363×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bergenin (drug)]] 0.5 µM |  | 0.859× | -3.3 | 0.28 | 12/48 (KATO III, J82, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | 0.852× | -3.2 | 0.28 | 20/43 (hTERT-HPNE, SW1417, …) | inconsistent across doses | composition shift; position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.863× | -3.2 | 0.28 | 11/48 (NCI-H2347, LOX-IMVI, …) | two highest doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 276. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 37.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.203× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 38.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.282× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[AN3 CA (line)]] | alt | 65.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.165× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[hTERT-HPNE (line)]] | wt | 30.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.119× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change |
| [[NCI-H460 (line)]] | wt | 35.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.378× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H661 (line)]] | alt | 39.4 | 0 | 1 | — | [[Saquinavir (drug)]] 0.5 µM 0.0647× (z -9.9) |
| [[SK-MEL-2 (line)]] | alt | 39.4 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.363× (z -8.6) |
| [[SW 1271 (line)]] | alt | 54.3 | 0 | 1 | — | [[Arbutin (drug)]] 5 µM 0.0789× (z -9.5) |
| [[SW1417 (line)]] | alt | 51.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.381× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change |
| [[SW480 (line)]] | alt | 35.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.71× (z +9.2) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[A-172 (line)]] | wt | 58.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 41.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 40.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 40.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 32.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 35.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 47.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 26.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 56.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 48.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 36.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 37.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 24.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 52.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 42.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 41.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 42.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 34.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 46.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 49.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 30.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 276), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CLCC1]] | +0.60 | +0.62 / +0.46 | both halves | 3e-05 |  |
| [[SVIL-AS1-1]] | +0.57 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[PTPN9]] | +0.56 | +0.49 / +0.46 | both halves | 3e-05 |  |
| [[ZFR]] | +0.54 | +0.50 / +0.46 | both halves | 2e-05 |  |
| [[HMGN4]] | +0.54 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[VPS26A]] | +0.53 | +0.46 / +0.54 | both halves | 3e-05 |  |
| [[MID2]] | +0.53 | +0.57 / +0.36 | both halves | 1e-04 | same gene group |
| [[PIGC]] | +0.53 | +0.44 / +0.42 | both halves | 4e-05 |  |
| [[DCTN2]] | +0.53 | +0.54 / +0.46 | both halves | 2e-05 |  |
| [[ZNF343]] | +0.52 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[DDX59]] | +0.52 | +0.47 / +0.46 | both halves | 2e-05 |  |
| [[DNAJC13]] | +0.52 | +0.52 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAGI1]] | -0.57 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[DPY19L2P1]] | -0.53 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[NR4A1]] | -0.52 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[HES1]] | -0.51 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[NR4A3]] | -0.50 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[NXN]] | -0.49 | -0.48 / -0.39 | both halves | 5e-05 |  |
| [[TSPAN5]] | -0.49 | -0.33 / -0.47 | both halves | 1e-04 |  |
| [[CA8]] | -0.48 | -0.35 / -0.41 | both halves | 1e-04 |  |
| [[SNAP25]] | -0.48 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[NCEH1]] | -0.47 | -0.46 / -0.39 | both halves | 5e-05 |  |
| [[VWA1]] | -0.46 | -0.41 / -0.32 | both halves | 2e-04 |  |
| [[ZNF331]] | -0.46 | -0.24 / -0.46 | both halves | 5e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 160]]; 27 genes; this gene is in the **-** arm (projection on the module's main direction -0.321). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-12.1, 17.6); signed map (-33.8, -22.3). **Vector** length 81.3, 15.1% of its response variance represented; |z| ≥ 3 in 838 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | +5.6 | +5.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.8 | +6.7 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~61% of this change | +3.7 | +4.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +3.7 | +6.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +3.5 | +3.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.0 | +4.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.0 | +2.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.6 | +2.8 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.4 | -0.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.0 | -2.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | -2.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.3 | +0.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.2 | -2.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.5 | -1.1 |
|  | [[Vilanterol (drug)]] 0.5 µM |  | -1.5 | -2.5 |
|  | [[Arbutin (drug)]] 5 µM |  | -1.4 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | ring finger protein 14 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q31.3 — chr5:141,958,328-141,990,292 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ARA54, HFB30, TRIAD2 |
| Gene groups (HGNC) | Ring finger proteins; RBR E3 ubiquitin ligases; RWD domain containing |
| Reactome | 3 pathways, smallest: Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation; Adaptive Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UBS8](https://www.uniprot.org/uniprotkb/Q9UBS8) (E3 ubiquitin-protein ligase RNF14):

> E3 ubiquitin-protein ligase that plays a key role in the RNF14-RNF25 translation quality control pathway, a pathway that takes place when a ribosome has stalled during translation, and which promotes ubiquitination and degradation of translation factors on stalled ribosomes. Recruited to stalled ribosomes by the ribosome collision sensor GCN1 and mediates 'Lys-6'-linked ubiquitination of target proteins, leading to their degradation. Mediates ubiquitination of EEF1A1/eEF1A and ETF1/eRF1 …

**Summary**, from NCBI Gene [9604](https://www.ncbi.nlm.nih.gov/gene/9604):

> The protein encoded by this gene contains a RING zinc finger, a motif known to be involved in protein-protein interactions. This protein interacts with androgen receptor (AR) and may function as a coactivator that induces AR target gene expression in prostate. A dominant negative mutant of this gene has been demonstrated to inhibit the AR-mediated growth of prostate cancer. This protein also interacts with class III ubiquitin-conjugating enzymes (E2s) and may act as a ubiquitin-ligase (E3) in …

**Accessions** — [HGNC:10058](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10058) · Entrez [9604](https://www.ncbi.nlm.nih.gov/gene/9604) · UniProt [Q9UBS8](https://www.uniprot.org/uniprotkb/Q9UBS8) · Ensembl [ENSG00000013561](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000013561)

## Data

Gene col 276: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 276); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 276, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 276]; `tensor/DDL_lfc|DDL_z.npy` [276]; `embed/gene_vectors.npy` [276]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 276 or target_col == 276). Every well: [[RNF14 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RNF14.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
