---
symbol: "OTUD6B-AS1"
type: "gene"
col: 14838
ensembl_id: "ENSG00000253738"
name: "OTUD6B antisense RNA 1"
location: "8q21.3"
module: 51
arm: "+"
pooled_cpm: 31.14
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 1
n_dd_up_clean: 7
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/051"]
generated_by: "tahoemap"
---

# OTUD6B-AS1

*OTUD6B antisense RNA 1* — 8q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (9 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.83× (z +10.9, q 4e-25, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.895× (z -4.7, q 0.001, down in 3 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.581× (z -3.7, q 0.061, down in 24 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H1573 0.436×; ⚠ cell-cycle shift, explains ~0% of this change); [[TAK-901 (drug)]] 5 µM in 1 line (A-427 0.0647×); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.185×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EPC1]] (+0.65, fdr 7e-06), [[MAPK1IP1L]] (+0.65, fdr 1e-05), [[LARP7]] (+0.65, fdr 1e-05); moves opposite to [[LPCAT1]] (-0.63, fdr 2e-05), [[GNB1L]] (-0.60, fdr 1e-05), [[COLGALT1]] (-0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 051]] (Chromatin modifying enzymes).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 9 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14838.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **1.83×** | +10.9 | 4e-25 | 45/48 (NCI-H2347, J82, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.13×** | +9.8 | 3e-20 | 29/36 (SW480, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.09×** | +9.6 | 2e-19 | 41/47 (NCI-H2347, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.94×** | +9.0 | 4e-17 | 35/44 (SW480, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.95×** | +8.3 | 1e-14 | 31/38 (LS 180, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.89×** | +8.3 | 1e-14 | 40/47 (AsPC-1, A498, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.45×** | +6.9 | 4e-10 | 34/47 (AsPC-1, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.57×** | +6.1 | 8e-08 | 34/48 (HEC-1-A, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.55×** | +5.9 | 2e-07 | 28/47 (RKO, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.49×** | +5.4 | 4e-06 | 36/48 (NCI-H2347, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.48×** | +5.4 | 4e-06 | 31/48 (RKO, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~42% of this change | **1.44×** | +4.9 | 4e-05 | 27/46 (HEC-1-A, MIA PaCa-2, …) | all doses, flat | low cells (technical?) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.36×** | +3.9 | 0.005 | 21/47 (HEC-1-A, LoVo, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.20×** | +3.4 | 0.027 | 19/48 (A-427, SW 900, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | **1.27×** | +3.2 | 0.048 | 18/47 (HEC-1-A, BT-474, …) | top dose only |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.25×** | +3.1 | 0.080 | 11/48 (HOP62, RKO, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14838.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H1573 0.436×; ⚠ cell-cycle shift, explains ~0% of this change); [[TAK-901 (drug)]] 5 µM in 1 line (A-427 0.0647×); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.185×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.895× | -4.7 | 0.001 | 3/48 (HCT15, SNU-1, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.581×** | -3.7 | 0.061 | 24/48 (A-427, RPMI-7951, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Budesonide (drug)]] 5 µM |  | 0.796× | -3.0 | 0.38 | 12/48 (SW 900, Panc 03.27, …) | top dose only | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | 0.643× | -3.0 | 0.38 | 18/47 (NCI-H1573, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, +0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14838. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 37.1 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.60× (z +15.6) ⚠ cell-cycle shift, explains ~60% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.28× (z +9.0) | — |
| [[A498 (line)]] | wt | 31.1 | 2 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 2.20× (z +9.0) | — |
| [[HS-578T (line)]] | alt | 44.0 | 2 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 2.35× (z +9.6) | — |
| [[NCI-H2347 (line)]] | alt | 32.7 | 2 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 2.63× (z +10.1) | — |
| [[RKO (line)]] | wt | 58.5 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.27× (z +9.0) | — |
| [[SW480 (line)]] | alt | 36.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.96× (z +13.0) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 23.5 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.0647× (z -9.1) |
| [[CFPAC-1 (line)]] | alt | 17.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +9.6) ⚠ cell-cycle shift, explains ~60% of this change | — |
| [[HEC-1-A (line)]] | alt | 38.1 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 2.89× (z +8.9) ⚠ toxic | — |
| [[HepG2_C3A (line)]] | wt | 22.3 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.185× (z -8.9) |
| [[HT-29 (line)]] | alt | 29.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.04× (z +10.7) ⚠ cell-cycle shift, explains ~60% of this change | — |
| [[J82 (line)]] | alt | 30.4 | 1 | 0 | [[Selinexor (drug)]] 5 µM 2.53× (z +9.7) | — |
| [[KATO III (line)]] | alt | 46.0 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 2.84× (z +8.8) ⚠ toxic | — |
| [[LS 180 (line)]] | wt | 30.3 | 1 | 0 | [[Selinexor (drug)]] 5 µM 2.50× (z +8.5) | — |
| [[NCI-H1573 (line)]] | alt | 56.3 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.436× (z -10.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 18.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.64× (z +8.9) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 20.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.76× (z +8.5) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 26.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.68× (z +8.6) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 32.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 42.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 27.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 39.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 33.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 36.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 57.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 57.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 44.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 42.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 39.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 19.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14838), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPC1]] | +0.65 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[MAPK1IP1L]] | +0.65 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[LARP7]] | +0.65 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[ZC3HC1]] | +0.63 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[BAZ2B]] | +0.63 | +0.74 / +0.44 | both halves | 3e-05 |  |
| [[ZNF518A]] | +0.63 | +0.73 / +0.45 | both halves | 3e-05 |  |
| [[ZNF441]] | +0.62 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[FUNDC1]] | +0.62 | +0.53 / +0.69 | both halves | 1e-05 |  |
| [[DIAPH2-AS1]] | +0.62 | +0.53 / +0.64 | both halves | 1e-05 | same gene group |
| [[ARMCX5-GPRASP2]] | +0.62 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[DHFR2]] | +0.61 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[CASC9]] | +0.61 | +0.59 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LPCAT1]] | -0.63 | -0.63 / -0.47 | both halves | 2e-05 |  |
| [[GNB1L]] | -0.60 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[COLGALT1]] | -0.59 | -0.69 / -0.51 | both halves | 1e-05 |  |
| [[ZDHHC8]] | -0.58 | -0.67 / -0.42 | both halves | 4e-05 |  |
| [[NUP93]] | -0.58 | -0.57 / -0.49 | both halves | 1e-05 |  |
| [[RNF126]] | -0.58 | -0.60 / -0.50 | both halves | 1e-05 |  |
| [[RNF4]] | -0.58 | -0.68 / -0.46 | both halves | 2e-05 |  |
| [[TBC1D24]] | -0.58 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[TBCD]] | -0.57 | -0.58 / -0.48 | both halves | 2e-05 |  |
| [[LRRC20]] | -0.57 | -0.51 / -0.40 | both halves | 5e-05 |  |
| [[SETD3]] | -0.57 | -0.54 / -0.55 | both halves | 1e-05 |  |
| [[INTS11]] | -0.57 | -0.66 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 051]] — Chromatin modifying enzymes; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.621). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-26.6, 10.5); signed map (12.5, -16.1). **Vector** length 87.6, 21.7% of its response variance represented; |z| ≥ 3 in 703 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +11.1 | +10.9 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +6.7 | +5.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +5.6 | +8.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.5 | +9.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | +4.3 | +6.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.9 | +5.4 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.8 | +2.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.7 | +3.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.2 | +0.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.1 | +1.7 |
| fall | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | -0.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | -0.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.0 | +0.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.0 | -3.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.4 | -1.1 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -1.4 | -1.1 |
|  | [[Fusidic acid (drug)]] 5 µM |  | -1.4 | -1.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.3 | -1.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.3 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | OTUD6B antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 8q21.3 — chr8:91,059,318-91,070,583 (-) |
| Ensembl biotype | lncRNA |
| Also known as | GS1-251I9.4 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:50466](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:50466) · Entrez [100506365](https://www.ncbi.nlm.nih.gov/gene/100506365) · Ensembl [ENSG00000253738](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000253738)

## Data

Gene col 14838: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14838); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14838, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14838]; `tensor/DDL_lfc|DDL_z.npy` [14838]; `embed/gene_vectors.npy` [14838]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14838 or target_col == 14838). Every well: [[OTUD6B-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/OTUD6B-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
