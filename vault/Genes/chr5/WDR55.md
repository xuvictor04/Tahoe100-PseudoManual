---
symbol: "WDR55"
type: "gene"
col: 4176
ensembl_id: "ENSG00000120314"
name: "WD repeat domain 55"
location: "5q31.3"
module: 2
arm: "+"
pooled_cpm: 18.49
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 3
n_dd_up_clean: 6
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# WDR55

*WD repeat domain 55* — 5q31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.12× (z +14.0, q 8e-42, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.780× (z -4.7, q 0.002, down in 19 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.805× (z -4.1, q 0.013, down in 12 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.281×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (LoVo 0.219×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H1573 0.175×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~93% of this change); [[Cobimetinib (drug)]] 5 µM in 1 line (C-33 A 0.193×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF275]] (+0.70, fdr 7e-06), [[MIER2]] (+0.66, fdr 1e-05), [[SLC35C1]] (+0.63, fdr 9e-06); moves opposite to [[ARID2]] (-0.58, fdr 3e-05), [[NUCKS1]] (-0.57, fdr 2e-04), [[NR1D2]] (-0.51, fdr 1e-04).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MAGEA4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4176.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.12×** | +14.0 | 8e-42 | 45/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.22×** | +12.6 | 4e-34 | 26/48 (SW480, LoVo, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.70×** | +9.9 | 1e-20 | 33/47 (HEC-1-A, SW480, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.61×** | +8.9 | 1e-16 | 34/48 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.46×** | +7.1 | 2e-10 | 24/47 (SW480, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **1.45×** | +6.6 | 3e-09 | 31/47 (HEC-1-A, PANC-1, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.24×** | +5.7 | 1e-06 | 18/48 (NCI-H2347, HEC-1-A, …) | rises with dose | low cells (technical?) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.34×** | +5.3 | 1e-05 | 14/48 (NCI-H460, AsPC-1, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.17× | +4.2 | 0.001 | 15/48 (NCI-H2347, MIA PaCa-2, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.51×** | +4.0 | 0.003 | 3/47 (NCI-H460, HEC-1-A, …) | rises with dose | noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **1.44×** | +3.6 | 0.018 | 5/43 (LOX-IMVI, A-427, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.23×** | +3.3 | 0.053 | 6/47 (LOX-IMVI, RKO, …) | two highest doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~22% of this change | **1.38×** | +3.1 | 0.072 | 4/39 (PANC-1, J82, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4176.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.281×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (LoVo 0.219×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H1573 0.175×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~93% of this change); [[Cobimetinib (drug)]] 5 µM in 1 line (C-33 A 0.193×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.780×** | -4.7 | 0.002 | 19/46 (LoVo, HOP62, …) | rises with dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.805×** | -4.1 | 0.013 | 12/47 (LoVo, H4, …) | rises with dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.807×** | -3.9 | 0.021 | 14/48 (H4, RPMI-7951, …) | top dose only | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | 0.848× | -3.1 | 0.24 | 16/47 (NCI-H2030, NCI-H1573, …) | all doses, flat |  |
| [[Palmatine (chloride) (drug)]] 0.5 µM |  | 0.846× | -3.1 | 0.24 | 13/45 (SW 900, RPMI-7951, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4176. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 19.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.219× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change |
| [[A-427 (line)]] | wt | 27.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -13.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 21.5 | 0 | 1 | — | [[Cobimetinib (drug)]] 5 µM 0.193× (z -8.5) |
| [[HEC-1-A (line)]] | alt | 23.5 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.36× (z +11.0) | — |
| [[NCI-H1573 (line)]] | alt | 13.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.175× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~93% of this change |
| [[NCI-H460 (line)]] | wt | 17.3 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.97× (z +9.5) | — |
| [[SW480 (line)]] | alt | 19.2 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.99× (z +10.4) | — |
| [[A-172 (line)]] | wt | 22.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 23.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 21.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.04 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4176), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF275]] | +0.70 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[MIER2]] | +0.66 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[SLC35C1]] | +0.63 | +0.57 / +0.60 | both halves | 9e-06 |  |
| [[TPD52L2]] | +0.63 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[E2F4]] | +0.62 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[RIC8A]] | +0.61 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[ARHGEF1]] | +0.61 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[B4GALT7]] | +0.61 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[RER1]] | +0.61 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[SOWAHC]] | +0.60 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[EIF1AD]] | +0.59 | +0.48 / +0.59 | both halves | 2e-05 | STRING 667 |
| [[GPSM1]] | +0.59 | +0.48 / +0.54 | both halves | 2e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARID2]] | -0.58 | -0.44 / -0.57 | both halves | 3e-05 |  |
| [[NUCKS1]] | -0.57 | -0.32 / -0.60 | both halves | 2e-04 |  |
| [[NR1D2]] | -0.51 | -0.34 / -0.51 | both halves | 1e-04 |  |
| [[FCHSD2]] | -0.51 | -0.46 / -0.50 | both halves | 3e-05 |  |
| [[REV3L]] | -0.50 | -0.35 / -0.50 | both halves | 1e-04 |  |
| [[TAPT1]] | -0.49 | -0.29 / -0.54 | both halves | 3e-04 |  |
| [[SMDT1]] | -0.49 | -0.31 / -0.41 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAGEA4]] | B | MAGEA4 activity raises WDR55's level | lines that do not express MAGEA4 (41) vs lines expressing it (9) | 1.12× lower at baseline in the lines without MAGEA4 | 0.075 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: CGA, CALCA, GCG |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.562). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-3.1, -25.6); signed map (-51.0, 0.8). **Vector** length 68.1, 10.7% of its response variance represented; |z| ≥ 3 in 846 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +5.8 | +9.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.9 | +5.3 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +3.5 | +2.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +3.0 | +5.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.3 | +14.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.1 | +4.0 |
|  | [[Belzutifan (drug)]] 5 µM |  | +1.5 | +3.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.5 | +2.0 |
|  | [[Budesonide (drug)]] 5 µM |  | +1.5 | +2.0 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -3.1 | -3.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.9 | -4.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.3 | -2.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | -2.3 | -3.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | -2.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.1 | -1.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.1 | -1.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.1 | -2.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.0 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | WD repeat domain 55 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q31.3 — chr5:140,664,868-140,674,124 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20195, FLJ21702 |
| Gene groups (HGNC) | WD repeat domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H6Y2](https://www.uniprot.org/uniprotkb/Q9H6Y2) (WD repeat-containing protein 55):

> Nucleolar protein that acts as a modulator of rRNA synthesis. Plays a central role during organogenesis (By similarity).

**Summary**, from NCBI Gene [54853](https://www.ncbi.nlm.nih.gov/gene/54853):

> Predicted to be involved in rRNA processing. Located in nucleolus and nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25971](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25971) · Entrez [54853](https://www.ncbi.nlm.nih.gov/gene/54853) · UniProt [Q9H6Y2](https://www.uniprot.org/uniprotkb/Q9H6Y2) · Ensembl [ENSG00000120314](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000120314)

## Data

Gene col 4176: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4176); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4176, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4176]; `tensor/DDL_lfc|DDL_z.npy` [4176]; `embed/gene_vectors.npy` [4176]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4176 or target_col == 4176). Every well: [[WDR55 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WDR55.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
