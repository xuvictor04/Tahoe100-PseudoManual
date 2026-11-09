---
symbol: "TXNDC9"
type: "gene"
col: 3686
ensembl_id: "ENSG00000115514"
name: "thioredoxin domain containing 9"
location: "2q11.2"
module: 64
arm: "+"
pooled_cpm: 23.49
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 3
n_dd_up_clean: 14
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/064"]
generated_by: "tahoemap"
---

# TXNDC9

*thioredoxin domain containing 9* — 2q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.48× (z +12.1, q 7e-31, up in 35 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.661× (z -9.0, q 1e-16, down in 27 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 4 lines (RKO 0.216×, SW1417 0.348×, SW480 0.461×, SW 900 0.288×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (LS 180 0.217×, NCI-H1573 0.262×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (SW1417 0.358×, NCI-H460 0.424×); [[Hesperidin (drug)]] 5 µM in 1 line (C-33 A 0.195×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRPS11]] (+0.66, fdr 3e-05), [[RRP36]] (+0.63, fdr 1e-05), [[OGFOD1]] (+0.60, fdr 1e-05); moves opposite to [[PTMA]] (-0.53, fdr 2e-05), [[NEU1]] (-0.50, fdr 5e-05), [[TXNDC16]] (-0.49, fdr 3e-04).
> It sits in the **+** arm of [[Module 064]] (proteasome).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 8 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3686.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.48×** | +12.1 | 7e-31 | 35/47 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.73×** | +11.2 | 1e-26 | 37/48 (PANC-1, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.67×** | +11.1 | 2e-26 | 38/48 (SW480, A-172, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.67×** | +11.1 | 3e-26 | 35/47 (LS 180, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.53×** | +9.2 | 3e-18 | 34/47 (SW480, A-427, …) | two highest doses | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **1.51×** | +8.6 | 5e-16 | 20/34 (A498, C32, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.38×** | +6.9 | 3e-10 | 25/48 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.39×** | +6.9 | 4e-10 | 24/47 (SW480, NCI-H2030, …) | two highest doses | cell-cycle shift (explains ~19% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.36×** | +6.7 | 2e-09 | 24/48 (COLO 205, SW480, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.34×** | +6.4 | 1e-08 | 23/47 (CFPAC-1, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.31×** | +5.8 | 3e-07 | 19/47 (AsPC-1, CFPAC-1, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.64×** | +5.6 | 9e-07 | 19/41 (SW 900, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change | **1.28×** | +5.3 | 4e-06 | 18/43 (A-172, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.25×** | +4.9 | 5e-05 | 17/47 (SW480, MIA PaCa-2, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.26×** | +4.6 | 1e-04 | 15/48 (PANC-1, A549, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.51×** | +4.6 | 1e-04 | 19/48 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.22×** | +4.3 | 5e-04 | 16/47 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.15× | +4.2 | 1e-03 | 10/48 (A-427, HOP62, …) | rises with dose |  |
| [[Pralsetinib (drug)]] 5 µM |  | **1.32×** | +3.1 | 0.050 | 12/48 (RPMI-7951, C32, …) | top dose only | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.31×** | +3.1 | 0.055 | 9/46 (LS 180, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 1.15× | +3.0 | 0.058 | 5/46 (HCT15, NCI-H1573, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3686.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 4 lines (RKO 0.216×, SW1417 0.348×, SW480 0.461×, SW 900 0.288×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (LS 180 0.217×, NCI-H1573 0.262×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (SW1417 0.358×, NCI-H460 0.424×); [[Hesperidin (drug)]] 5 µM in 1 line (C-33 A 0.195×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.661×** | -9.0 | 1e-16 | 27/48 (SW1417, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.779×** | -5.4 | 1e-05 | 20/48 (BT-474, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.793×** | -5.1 | 8e-05 | 20/47 (RKO, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.848× | -3.6 | 0.041 | 14/47 (NCI-H460, SW1417, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | 0.842× | -3.5 | 0.055 | 5/48 (HEC-1-A, LoVo, …) | inconsistent across doses |  |
| [[Pentamidine (isethionate) (drug)]] 5 µM |  | 0.900× | -3.3 | 0.10 | 7/48 (A-427, RPMI-7951, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3686. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 29.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.262× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[NCI-H460 (line)]] | wt | 23.9 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.424× (z -9.4) |
| [[SW1417 (line)]] | alt | 27.7 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.348× (z -9.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.358× (z -9.6) |
| [[AsPC-1 (line)]] | alt | 23.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.397× (z -8.8) ⚠ cell-cycle shift, would explain all of this change |
| [[C-33 A (line)]] | alt | 20.1 | 0 | 1 | — | [[Hesperidin (drug)]] 5 µM 0.195× (z -8.5) |
| [[HEC-1-A (line)]] | alt | 32.0 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.164× (z -9.1) ⚠ toxic |
| [[LS 180 (line)]] | wt | 20.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.217× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[NCI-H2030 (line)]] | alt | 27.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.495× (z -8.8) ⚠ cell-cycle shift, would explain all of this change |
| [[RKO (line)]] | wt | 20.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.216× (z -10.1) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 30.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.288× (z -8.9) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 26.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.461× (z -9.1) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 36.6 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 25.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 38.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 25.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 25.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 19.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3686), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPS11]] | +0.66 | +0.71 / +0.45 | both halves | 3e-05 |  |
| [[RRP36]] | +0.63 | +0.68 / +0.55 | both halves | 1e-05 |  |
| [[OGFOD1]] | +0.60 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[EIF2B2]] | +0.58 | +0.60 / +0.49 | both halves | 1e-05 |  |
| [[TRIM27]] | +0.57 | +0.62 / +0.42 | both halves | 4e-05 |  |
| [[CCT6A]] | +0.57 | +0.61 / +0.42 | both halves | 4e-05 | STRING 670 |
| [[PSMA5]] | +0.57 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[PSMC5]] | +0.56 | +0.60 / +0.43 | both halves | 3e-05 |  |
| [[PSMD6]] | +0.56 | +0.60 / +0.45 | both halves | 3e-05 |  |
| [[RPL26L1]] | +0.55 | +0.60 / +0.39 | both halves | 6e-05 |  |
| [[NUDT5]] | +0.55 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[PSMD12]] | +0.55 | +0.65 / +0.41 | both halves | 4e-05 | STRING 409 |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTMA]] | -0.53 | -0.56 / -0.47 | both halves | 2e-05 |  |
| [[NEU1]] | -0.50 | -0.50 / -0.40 | both halves | 5e-05 |  |
| [[TXNDC16]] | -0.49 | -0.53 / -0.29 | both halves | 3e-04 | same gene group |
| [[REL]] | -0.49 | -0.45 / -0.43 | both halves | 3e-05 |  |
| [[H3-3A]] | -0.49 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[LUC7L3]] | -0.48 | -0.35 / -0.46 | both halves | 1e-04 |  |
| [[PEAK1]] | -0.48 | -0.62 / -0.27 | both halves | 3e-04 |  |
| [[SPPL3]] | -0.48 | -0.53 / -0.34 | both halves | 1e-04 |  |
| [[PABPN1]] | -0.47 | -0.46 / -0.39 | both halves | 6e-05 |  |
| [[MIR23AHG]] | -0.47 | -0.43 / -0.43 | both halves | 3e-05 |  |
| [[VAMP2]] | -0.46 | -0.37 / -0.41 | both halves | 8e-05 |  |
| [[RNF103]] | -0.46 | -0.53 / -0.36 | both halves | 9e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 064]] — proteasome; 77 genes; this gene is in the **+** arm (projection on the module's main direction 0.419). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-47.9, 2.9); signed map (-8.7, -26.3). **Vector** length 86.8, 16.9% of its response variance represented; |z| ≥ 3 in 923 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +7.4 | +11.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +6.3 | +11.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.1 | +11.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.9 | +9.2 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +3.6 | +5.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.3 | +4.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.0 | +3.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.1 | +2.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.1 | +2.0 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.0 | -5.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -4.6 | -9.0 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.7 | -5.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.6 | -3.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -2.6 | +0.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.7 | -2.5 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -1.6 | -0.4 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -1.5 | -1.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.5 | -2.3 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -1.4 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | thioredoxin domain containing 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q11.2 — chr2:99,318,982-99,340,702 (-) |
| Ensembl biotype | protein_coding |
| Also known as | APACD |
| Gene groups (HGNC) | Thioredoxin domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [O14530](https://www.uniprot.org/uniprotkb/O14530) (Thioredoxin domain-containing protein 9):

> Significantly diminishes the chaperonin TCP1 complex ATPase activity, thus negatively impacts protein folding, including that of actin or tubulin.

**Summary**, from NCBI Gene [10190](https://www.ncbi.nlm.nih.gov/gene/10190):

> The protein encoded by this gene is a member of the thioredoxin family. The exact function of this protein is not known but it is associated with cell differentiation. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:24110](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24110) · Entrez [10190](https://www.ncbi.nlm.nih.gov/gene/10190) · UniProt [O14530](https://www.uniprot.org/uniprotkb/O14530) · Ensembl [ENSG00000115514](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115514)

## Data

Gene col 3686: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3686); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3686, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3686]; `tensor/DDL_lfc|DDL_z.npy` [3686]; `embed/gene_vectors.npy` [3686]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3686 or target_col == 3686). Every well: [[TXNDC9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TXNDC9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
