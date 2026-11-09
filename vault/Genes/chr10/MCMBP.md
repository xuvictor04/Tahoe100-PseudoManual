---
symbol: "MCMBP"
type: "gene"
col: 12459
ensembl_id: "ENSG00000197771"
name: "minichromosome maintenance complex binding protein"
location: "10q26.11"
module: 6
arm: "+"
pooled_cpm: 59.33
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 5
n_dd_up_clean: 2
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# MCMBP

*minichromosome maintenance complex binding protein* — 10q26.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[PH-797804 (drug)]] 5 µM: 2.68× (z +10.8, q 3e-24, up in 39 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[TAK-901 (drug)]] 5 µM in 4 lines (LoVo 5.51×, SW480 3.94×, C32 6.72×, LS 180 5.82×); [[Niclosamide (olamine) (drug)]] 5 µM in 3 lines (LoVo 2.97×, PANC-1 2.16×, NCI-H1792 2.74×; ⚠ toxic); [[PH-797804 (drug)]] 5 µM in 3 lines (C32 7.91×, PANC-1 3.21×, LS 180 6.14×); [[TAK-901 (drug)]] 0.05 µM in 2 lines (SW48 4.66×, LOX-IMVI 2.77×).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.707× (z -7.3, q 2e-10, down in 30 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AUNIP]] (+0.72, fdr 7e-06), [[AHCTF1]] (+0.69, fdr 7e-06), [[GMPS]] (+0.69, fdr 7e-06); moves opposite to [[SQSTM1]] (-0.58, fdr 1e-05), [[ATP6V0C]] (-0.58, fdr 2e-05), [[BBIP1]] (-0.54, fdr 1e-05).
> It sits in the **+** arm of [[Module 006]] (E2F targets).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12459.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[TAK-901 (drug)]] 5 µM in 4 lines (LoVo 5.51×, SW480 3.94×, C32 6.72×, LS 180 5.82×); [[Niclosamide (olamine) (drug)]] 5 µM in 3 lines (LoVo 2.97×, PANC-1 2.16×, NCI-H1792 2.74×; ⚠ toxic); [[PH-797804 (drug)]] 5 µM in 3 lines (C32 7.91×, PANC-1 3.21×, LS 180 6.14×); [[TAK-901 (drug)]] 0.05 µM in 2 lines (SW48 4.66×, LOX-IMVI 2.77×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **2.68×** | +10.8 | 3e-24 | 39/48 (C32, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.68×** | +10.5 | 3e-23 | 38/47 (LoVo, PANC-1, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.36×** | +9.4 | 2e-18 | 41/49 (LoVo, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | 1.19× | +3.5 | 0.060 | 14/48 (NCI-H460, A549, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12459.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.707×** | -7.3 | 2e-10 | 30/48 (SW480, SHP-77, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.936× | -5.1 | 9e-05 | 3/49 (NCI-H23, NCI-H2122, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.797×** | -4.8 | 4e-04 | 23/48 (J82, SHP-77, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.801×** | -4.4 | 0.001 | 22/48 (A-427, A-172, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.824×** | -4.1 | 0.005 | 21/48 (A-427, LoVo, …) | all doses, flat |  |
| [[Auranofin (drug)]] 5 µM |  | **0.827×** | -4.0 | 0.006 | 20/48 (C32, A-427, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | 0.833× | -3.7 | 0.018 | 17/47 (HEC-1-A, A-427, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~41% of this change | 0.854× | -3.3 | 0.056 | 11/49 (LoVo, Hs 766T, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | 0.858× | -3.3 | 0.056 | 13/49 (C32, HEC-1-A, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.855× | -3.3 | 0.056 | 15/47 (C32, A-427, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | 0.897× | -3.2 | 0.063 | 16/48 (A-427, LS 180, …) | all doses, flat | low cells (technical?) |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.891× | -3.2 | 0.074 | 13/48 (C32, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | 0.818× | -3.0 | 0.11 | 12/48 (SK-MEL-2, PANC-1, …) | two highest doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.901× | -3.0 | 0.11 | 12/48 (COLO 205, HEC-1-A, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12459. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 55.0 | 4 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.71× (z +9.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 6.14× (z +9.0) | — |
| [[A-172 (line)]] | wt | 71.8 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.549× (z -9.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 49.4 | 3 (2 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.97× (z +11.7) ⚠ toxic · without an alert: [[TAK-901 (drug)]] 5 µM 5.51× (z +10.0) | — |
| [[A-427 (line)]] | wt | 79.6 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.382× (z -16.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 57.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.237× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 123 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.217× (z -14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 62.0 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 7.91× (z +9.6) | — |
| [[PANC-1 (line)]] | alt | 74.4 | 2 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.16× (z +11.2) ⚠ toxic · without an alert: [[PH-797804 (drug)]] 5 µM 3.21× (z +9.3) | — |
| [[SW48 (line)]] | wt | 78.4 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 0.05 µM 4.66× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.293× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 97.2 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.187× (z -10.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 36.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.251× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 75.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.473× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 48.3 | 1 | 0 | [[TAK-901 (drug)]] 0.05 µM 2.77× (z +9.2) | — |
| [[NCI-H1792 (line)]] | alt | 49.6 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.74× (z +9.1) ⚠ toxic | — |
| [[NCI-H460 (line)]] | wt | 56.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +11.8) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[Panc 03.27 (line)]] | alt | 60.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.266× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 76.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.432× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 71.1 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.178× (z -8.6) ⚠ toxic; cell-cycle shift, explains ~44% of this change |
| [[SW480 (line)]] | alt | 62.6 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 3.94× (z +9.0) | — |
| [[A498 (line)]] | wt | 55.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 63.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 61.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 55.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 46.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 62.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 57.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 49.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 51.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 40.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 37.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 73.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 53.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 56.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 67.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 53.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 52.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 66.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 55.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 70.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 63.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 45.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 66.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 58.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 48.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 47.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 83.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 63.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12459), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AUNIP]] | +0.72 | +0.72 / +0.70 | both halves | 7e-06 |  |
| [[AHCTF1]] | +0.69 | +0.73 / +0.58 | both halves | 7e-06 |  |
| [[GMPS]] | +0.69 | +0.68 / +0.70 | both halves | 7e-06 | STRING 531 |
| [[DUT]] | +0.63 | +0.57 / +0.63 | both halves | 9e-06 |  |
| [[DSCC1]] | +0.63 | +0.58 / +0.66 | both halves | 8e-06 |  |
| [[TUBGCP3]] | +0.62 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[NCAPD3]] | +0.62 | +0.57 / +0.68 | both halves | 1e-05 |  |
| [[SKP2]] | +0.62 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[CSE1L]] | +0.62 | +0.59 / +0.66 | both halves | 7e-06 |  |
| [[RANBP1]] | +0.62 | +0.54 / +0.66 | both halves | 1e-05 |  |
| [[ERLIN1]] | +0.61 | +0.67 / +0.57 | both halves | 1e-05 |  |
| [[MMS22L]] | +0.61 | +0.53 / +0.68 | both halves | 1e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SQSTM1]] | -0.58 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[ATP6V0C]] | -0.58 | -0.62 / -0.49 | both halves | 2e-05 |  |
| [[BBIP1]] | -0.54 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[SWT1]] | -0.54 | -0.60 / -0.47 | both halves | 2e-05 |  |
| [[ATP6V1G1]] | -0.53 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[OSGIN1]] | -0.52 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[WDR26]] | -0.52 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[WBP2]] | -0.51 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[ALS2]] | -0.51 | -0.53 / -0.42 | both halves | 4e-05 |  |
| [[MICU1]] | -0.51 | -0.62 / -0.39 | both halves | 5e-05 |  |
| [[EIF1]] | -0.51 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[IER5]] | -0.51 | -0.55 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.575). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-30.8, -41.3); signed map (-32.7, -43.8). **Vector** length 114, 30.9% of its response variance represented; |z| ≥ 3 in 895 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[PH-797804 (drug)]] 5 µM |  | +4.9 | +10.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +4.2 | +10.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.2 | +9.4 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.9 | +2.5 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +2.6 | +2.1 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +2.5 | +1.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.3 | -0.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.2 | +2.1 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~34% of this change | -5.7 | -4.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.4 | -0.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.6 | +0.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -4.3 | +2.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -3.7 | -1.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.7 | +0.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.6 | -4.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.3 | -1.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.3 | -3.3 |
|  | [[Posaconazole (drug)]] 5 µM |  | -2.0 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | minichromosome maintenance complex binding protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q26.11 — chr10:119,829,404-119,892,556 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ13081, MCM-BP; previously C10orf119 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BTE3](https://www.uniprot.org/uniprotkb/Q9BTE3) (Mini-chromosome maintenance complex-binding protein):

> Associated component of the MCM complex that acts as a regulator of DNA replication. Binds to the MCM complex during late S phase and promotes the disassembly of the MCM complex from chromatin, thereby acting as a key regulator of pre-replication complex (pre-RC) unloading from replicated DNA. Can dissociate the MCM complex without addition of ATP; probably acts by destabilizing interactions of each individual subunits of the MCM complex. Required for sister chromatid cohesion.

**Summary**, from NCBI Gene [79892](https://www.ncbi.nlm.nih.gov/gene/79892):

> This gene encodes a protein which is a component of the hexameric minichromosome maintenance (MCM) complex which regulates initiation and elongation of DNA. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jan 2012]

**Accessions** — [HGNC:25782](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25782) · Entrez [79892](https://www.ncbi.nlm.nih.gov/gene/79892) · UniProt [Q9BTE3](https://www.uniprot.org/uniprotkb/Q9BTE3) · Ensembl [ENSG00000197771](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197771)

## Data

Gene col 12459: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12459); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12459, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12459]; `tensor/DDL_lfc|DDL_z.npy` [12459]; `embed/gene_vectors.npy` [12459]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12459 or target_col == 12459). Every well: [[MCMBP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MCMBP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
