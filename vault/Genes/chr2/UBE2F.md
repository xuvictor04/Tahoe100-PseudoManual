---
symbol: "UBE2F"
type: "gene"
col: 11499
ensembl_id: "ENSG00000184182"
name: "ubiquitin conjugating enzyme E2 F (putative)"
location: "2q37.3"
module: 2
arm: "+"
pooled_cpm: 27.77
n_lines_expressing: 50
n_dd_up: 29
n_dd_down: 1
n_dd_up_clean: 23
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# UBE2F

*ubiquitin conjugating enzyme E2 F (putative)* — 2q37.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 1.90× (z +14.0, q 2e-41, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 0.5 µM: 0.787× (z -5.2, q 1e-04, down in 20 of 48 measured lines) ⚠ cell-cycle shift, explains ~12% of this change.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Bendamustine (drug)]] 5 µM in 1 line (CHP-212 0.0665×); [[Dinaciclib (drug)]] 5 µM in 1 line (SHP-77 0.389×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TEX2]] (+0.65, fdr 1e-05), [[TSPAN17]] (+0.65, fdr 1e-05), [[CSK]] (+0.63, fdr 1e-05); moves opposite to [[ANKRD26]] (-0.53, fdr 3e-05), [[MORF4L2]] (-0.53, fdr 3e-05), [[RBM39]] (-0.52, fdr 8e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MFAP3L]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 44 in all, 14 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11499.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **1.90×** | +14.0 | 2e-41 | 46/48 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.90×** | +13.9 | 2e-41 | 45/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.90×** | +13.9 | 2e-41 | 41/47 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +10.1 | 8e-22 | 32/48 (NCI-H460, H4, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.47×** | +8.4 | 6e-15 | 29/48 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.46×** | +8.2 | 3e-14 | 32/48 (SW480, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.49×** | +8.1 | 3e-14 | 31/48 (KATO III, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.44×** | +8.0 | 1e-13 | 31/47 (LS 180, KATO III, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.41×** | +7.5 | 5e-12 | 24/47 (HOP62, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.41×** | +7.5 | 5e-12 | 30/48 (HOP62, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.78×** | +6.5 | 4e-09 | 25/48 (MIA PaCa-2, KATO III, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.77×** | +6.4 | 6e-09 | 22/47 (MIA PaCa-2, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.74×** | +6.2 | 2e-08 | 14/29 (NCI-H1573, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.33×** | +6.2 | 2e-08 | 26/47 (SW480, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.30×** | +5.7 | 4e-07 | 19/47 (SW480, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.31×** | +5.5 | 1e-06 | 23/48 (SW480, H4, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.20× | +5.5 | 1e-06 | 17/48 (A498, LoVo, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.28×** | +5.4 | 2e-06 | 24/48 (LS 180, KATO III, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11499.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Bendamustine (drug)]] 5 µM in 1 line (CHP-212 0.0665×); [[Dinaciclib (drug)]] 5 µM in 1 line (SHP-77 0.389×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **0.787×** | -5.2 | 1e-04 | 20/48 (LoVo, CFPAC-1, …) | all doses, flat |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.939× | -4.8 | 4e-04 | 3/48 (HOP62, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Raltitrexed (drug)]] 0.5 µM |  | 0.847× | -3.7 | 0.049 | 10/47 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 0.05 µM |  | 0.863× | -3.2 | 0.18 | 10/48 (HEC-1-A, AsPC-1, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 5 µM |  | 0.875× | -3.2 | 0.18 | 5/48 (MIA PaCa-2, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | 0.869× | -3.1 | 0.20 | 3/48 (Panc 03.27, AsPC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11499. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 23.6 | 6 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.60× (z +10.5) | — |
| [[HOP62 (line)]] | alt | 23.1 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.44× (z +10.1) | — |
| [[PANC-1 (line)]] | alt | 23.7 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.23× (z +8.9) | — |
| [[CHP-212 (line)]] | wt | 27.5 | 0 | 1 | — | [[Bendamustine (drug)]] 5 µM 0.0665× (z -8.7) |
| [[H4 (line)]] | wt | 19.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.07× (z +8.6) | — |
| [[NCI-H460 (line)]] | wt | 28.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.46× (z +13.6) | — |
| [[SHP-77 (line)]] | alt | 63.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.389× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 27.7 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 26.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 28.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 28.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 43.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 45.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 23.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 33.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 28.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 51.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 37.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 27.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 46.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 19.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11499), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TEX2]] | +0.65 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[TSPAN17]] | +0.65 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[CSK]] | +0.63 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[STIMATE]] | +0.62 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[ABCC10]] | +0.60 | +0.63 / +0.47 | both halves | 2e-05 |  |
| [[ATP13A2]] | +0.59 | +0.57 / +0.49 | both halves | 1e-05 |  |
| [[ZNF767P-1]] | +0.59 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[LIMK1]] | +0.59 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[CSNK2A2]] | +0.59 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[TRAPPC10]] | +0.58 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[CDC42BPB]] | +0.58 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[SGPP1]] | +0.58 | +0.59 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKRD26]] | -0.53 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[MORF4L2]] | -0.53 | -0.45 / -0.60 | both halves | 3e-05 |  |
| [[RBM39]] | -0.52 | -0.37 / -0.43 | both halves | 8e-05 |  |
| [[BTN3A1]] | -0.52 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[TRA2A]] | -0.51 | -0.40 / -0.49 | both halves | 5e-05 |  |
| [[RSRC2]] | -0.50 | -0.36 / -0.52 | both halves | 9e-05 |  |
| [[AHI1]] | -0.49 | -0.39 / -0.45 | both halves | 5e-05 |  |
| [[NUCKS1]] | -0.49 | -0.45 / -0.30 | both halves | 2e-04 |  |
| [[METTL25B]] | -0.48 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[SF3B1]] | -0.48 | -0.55 / -0.33 | both halves | 1e-04 |  |
| [[ZNF608]] | -0.48 | -0.43 / -0.37 | both halves | 8e-05 |  |
| [[APOLD1]] | -0.48 | -0.41 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MFAP3L]] | B | MFAP3L activity weakens UBE2F's drug response | lines that do not express MFAP3L (9) vs lines expressing it (39) | the lines without MFAP3L respond 1.43× as strongly (z diff -1.03); strongest at Panobinostat 0.5 µM: 2.61x vs 1.87x (z diff -2.1) | 0.035 | ⚠ within organs, on part of the lines; also absent: CRACD, FILIP1, TSPAN33; maybe low, not absent; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.526). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-7.2, -26.3); signed map (-45.3, -13.7). **Vector** length 74.0, 13.6% of its response variance represented; |z| ≥ 3 in 978 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +3.7 | +0.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change | +3.7 | +3.1 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.4 | +7.5 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.0 | +13.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.8 | +8.4 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.7 | +3.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.5 | +5.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.2 | +4.1 |
|  | [[EX229 (drug)]] 5 µM |  | +1.8 | +2.8 |
|  | [[Neratinib (drug)]] 5 µM |  | +1.7 | +1.4 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.0 | +4.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | -2.7 | -5.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.6 | -2.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.0 | +4.0 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.8 | -4.8 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.7 | -2.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.6 | -2.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.6 | -3.2 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.5 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin conjugating enzyme E2 F (putative) |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q37.3 — chr2:237,966,827-238,042,782 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NCE2 |
| Gene groups (HGNC) | Ubiquitin conjugating enzymes E2 |
| Reactome | 4 pathways, smallest: Neddylation; Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q969M7](https://www.uniprot.org/uniprotkb/Q969M7) (NEDD8-conjugating enzyme UBE2F):

> Accepts the ubiquitin-like protein NEDD8 from the UBA3-NAE1 E1 complex and catalyzes its covalent attachment to other proteins. Together with the E3 ubiquitin ligase RNF7/RBX2, specifically neddylates cullin-5 (CUL5). Does not neddylate CUL1, CUL2, CUL3, CUL4A or CUL4B. Mediates neddylation of the CUL9-RBX1 complex.; (Microbial infection) Following infection by HIV-1 virus, participates to HIV-1 Vif protein-mediated ubiquitination and degradation of APOBEC3G by mediating neddylation of cullin-5 …

**Summary**, from NCBI Gene [140739](https://www.ncbi.nlm.nih.gov/gene/140739):

> Enables NEDD8 conjugating enzyme activity. Involved in protein neddylation. Predicted to be active in cytosol and nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:12480](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12480) · Entrez [140739](https://www.ncbi.nlm.nih.gov/gene/140739) · UniProt [Q969M7](https://www.uniprot.org/uniprotkb/Q969M7) · Ensembl [ENSG00000184182](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184182)

## Data

Gene col 11499: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11499); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11499, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11499]; `tensor/DDL_lfc|DDL_z.npy` [11499]; `embed/gene_vectors.npy` [11499]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11499 or target_col == 11499). Every well: [[UBE2F — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UBE2F.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
