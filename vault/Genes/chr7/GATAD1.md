---
symbol: "GATAD1"
type: "gene"
col: 8057
ensembl_id: "ENSG00000157259"
name: "GATA zinc finger domain containing 1"
location: "7q21.2"
module: 20
arm: "-"
pooled_cpm: 63.23
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 12
n_dd_up_clean: 0
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# GATAD1

*GATA zinc finger domain containing 1* — 7q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.63× (z +6.7, q 1e-08, up in 38 of 49 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 2 lines (LS 180 3.56×, HEC-1-A 2.50×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (A-427 3.32×, NCI-H23 2.69×; ⚠ cell-cycle shift, explains ~29% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (PANC-1 1.85×, A-427 2.31×; ⚠ cell-cycle shift, would explain all of this change).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[PH-797804 (drug)]] 5 µM: 0.295× (z -8.6, q 3e-15, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZC3H6]] (+0.73, fdr 7e-06), [[NKAP]] (+0.70, fdr 7e-06), [[TRIP11]] (+0.69, fdr 7e-06); moves opposite to [[ATP5F1B]] (-0.66, fdr 1e-05), [[ADAM15]] (-0.66, fdr 7e-06), [[GLB1L2]] (-0.65, fdr 1e-05).
> It sits in the **-** arm of [[Module 020]] (Cap-dependent Translation Initiation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 4 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8057.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 2 lines (LS 180 3.56×, HEC-1-A 2.50×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (A-427 3.32×, NCI-H23 2.69×; ⚠ cell-cycle shift, explains ~29% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (PANC-1 1.85×, A-427 2.31×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.63×** | +6.7 | 1e-08 | 38/49 (HEC-1-A, RKO, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.60×** | +6.2 | 2e-07 | 30/43 (LS 180, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.39×** | +4.5 | 0.001 | 29/48 (A-427, NCI-H23, …) | two highest doses |  |
| [[Entrectinib (drug)]] 5 µM |  | 1.27× | +3.3 | 0.15 | 23/48 (LoVo, NCI-H1792, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | 1.26× | +3.1 | 0.23 | 23/48 (PANC-1, A-427, …) | rises with dose | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8057.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **0.295×** | -8.6 | 3e-15 | 47/48 (MIA PaCa-2, RKO, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.343×** | -7.6 | 1e-11 | 44/49 (SW480, HT-29, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.630×** | -6.2 | 9e-08 | 36/48 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.640×** | -6.0 | 3e-07 | 39/48 (NCI-H1573, SW480, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.644×** | -5.9 | 3e-07 | 32/48 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.649×** | -5.8 | 6e-07 | 35/48 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.667×** | -5.4 | 4e-06 | 36/48 (SW480, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.677×** | -5.3 | 1e-05 | 34/48 (NCI-H460, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.560×** | -4.1 | 0.003 | 20/36 (NCI-H1573, SNU-1, …) | rises with dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.742×** | -4.0 | 0.004 | 26/48 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.753×** | -3.8 | 0.007 | 24/48 (NCI-H1573, NCI-H460, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.754×** | -3.6 | 0.016 | 25/47 (SW48, SW1417, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.929× | -3.0 | 0.11 | 0/49 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8057. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 92.5 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.287× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.320× (z -12.3) |
| [[A-427 (line)]] | wt | 50.8 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.32× (z +9.9) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[HEC-1-A (line)]] | alt | 72.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.73× (z +9.7) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 74.9 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.340× (z -9.7) |
| [[LOX-IMVI (line)]] | wt | 29.2 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0811× (z -8.7) |
| [[LS 180 (line)]] | wt | 49.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.56× (z +10.0) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 81.2 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.110× (z -10.1) |
| [[NCI-H1573 (line)]] | alt | 89.4 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.405× (z -8.7) |
| [[NCI-H23 (line)]] | alt | 61.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.69× (z +8.7) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[Panc 03.27 (line)]] | alt | 55.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.128× (z -15.8) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 61.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +9.8) ⚠ cell-cycle shift, would explain all of this change | — |
| [[RKO (line)]] | wt | 81.8 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.148× (z -8.8) |
| [[SW 1271 (line)]] | alt | 85.8 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.127× (z -9.1) ⚠ transcription drop; cell-cycle shift, explains ~43% of this change |
| [[SW48 (line)]] | wt | 76.4 | 0 | 1 | — | [[TAK-901 (drug)]] 0.05 µM 0.262× (z -8.6) |
| [[A-172 (line)]] | wt | 51.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 119 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 62.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 65.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 43.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 65.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 58.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 49.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 54.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 53.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 66.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 79.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 49.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 45.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 58.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 53.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 56.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 49.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 78.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 95.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 57.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 72.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 42.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 62.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 62.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 56.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 55.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 69.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 62.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 58.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 61.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 71.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8057), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZC3H6]] | +0.73 | +0.74 / +0.66 | both halves | 7e-06 |  |
| [[NKAP]] | +0.70 | +0.75 / +0.74 | both halves | 7e-06 |  |
| [[TRIP11]] | +0.69 | +0.76 / +0.58 | both halves | 7e-06 |  |
| [[SNHG32]] | +0.69 | +0.69 / +0.70 | both halves | 7e-06 |  |
| [[WASHC1]] | +0.69 | +0.69 / +0.65 | both halves | 7e-06 |  |
| [[WHAMM]] | +0.68 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[FAM98C]] | +0.67 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[TIPRL]] | +0.66 | +0.72 / +0.68 | both halves | 7e-06 |  |
| [[NFKBIB]] | +0.66 | +0.68 / +0.60 | both halves | 7e-06 |  |
| [[CCDC174]] | +0.66 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[MITD1]] | +0.65 | +0.69 / +0.62 | both halves | 7e-06 |  |
| [[UPF3B]] | +0.64 | +0.66 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP5F1B]] | -0.66 | -0.59 / -0.55 | both halves | 1e-05 |  |
| [[ADAM15]] | -0.66 | -0.68 / -0.59 | both halves | 7e-06 |  |
| [[GLB1L2]] | -0.65 | -0.59 / -0.54 | both halves | 1e-05 |  |
| [[CHID1]] | -0.64 | -0.66 / -0.53 | both halves | 1e-05 |  |
| [[COLGALT1]] | -0.63 | -0.65 / -0.56 | both halves | 1e-05 |  |
| [[CASP2]] | -0.63 | -0.66 / -0.50 | both halves | 1e-05 |  |
| [[YWHAQ]] | -0.63 | -0.65 / -0.65 | both halves | 7e-06 |  |
| [[TUBB]] | -0.62 | -0.62 / -0.59 | both halves | 7e-06 |  |
| [[CALM3]] | -0.62 | -0.62 / -0.49 | both halves | 1e-05 |  |
| [[EIF5A]] | -0.62 | -0.52 / -0.62 | both halves | 1e-05 |  |
| [[PGAM1]] | -0.62 | -0.63 / -0.68 | both halves | 7e-06 |  |
| [[PODXL2]] | -0.61 | -0.64 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **-** arm (projection on the module's main direction -0.635). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-36.1, -15.7); signed map (3.1, -12.8). **Vector** length 97.7, 28.5% of its response variance represented; |z| ≥ 3 in 730 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +7.0 | +2.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +6.7 | +4.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | +6.3 | +3.1 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.0 | +2.1 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | +2.8 | +1.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.6 | +1.5 |
|  | [[Adagrasib (drug)]] 5 µM |  | +2.1 | +2.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.0 | +1.3 |
|  | [[Temsirolimus (drug)]] 5 µM |  | +1.9 | +0.8 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.9 | +1.1 |
| fall | [[PH-797804 (drug)]] 5 µM |  | -5.5 | -8.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.9 | -6.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | -4.7 | -7.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -4.6 | -3.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -4.1 | -3.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.0 | +0.6 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -2.0 | -2.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -2.0 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | GATA zinc finger domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q21.2 — chr7:92,447,482-92,460,075 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ODAG, RG083M05.2, FLJ22489 |
| Gene groups (HGNC) | GATA zinc finger domain containing; EMSY complex |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WUU5](https://www.uniprot.org/uniprotkb/Q8WUU5) (GATA zinc finger domain-containing protein 1):

> Component of some chromatin complex recruited to chromatin sites methylated 'Lys-4' of histone H3 (H3K4me), with a preference for trimethylated form (H3K4me3).

**Summary**, from NCBI Gene [57798](https://www.ncbi.nlm.nih.gov/gene/57798):

> The protein encoded by this gene contains a zinc finger at the N-terminus, and is thought to bind to a histone modification site that regulates gene expression. Mutations in this gene have been associated with autosomal recessive dilated cardiomyopathy. Alternatively spliced transcript variants have been found for this gene. [provided by RefSeq, Jun 2012]

**Accessions** — [HGNC:29941](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29941) · Entrez [57798](https://www.ncbi.nlm.nih.gov/gene/57798) · UniProt [Q8WUU5](https://www.uniprot.org/uniprotkb/Q8WUU5) · Ensembl [ENSG00000157259](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000157259)

## Data

Gene col 8057: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8057); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8057, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8057]; `tensor/DDL_lfc|DDL_z.npy` [8057]; `embed/gene_vectors.npy` [8057]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8057 or target_col == 8057). Every well: [[GATAD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GATAD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
