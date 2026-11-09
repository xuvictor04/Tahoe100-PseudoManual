---
symbol: "SLC27A5"
type: "gene"
col: 1380
ensembl_id: "ENSG00000083807"
name: "solute carrier family 27 member 5"
location: "19q13.43"
module: 36
arm: "+"
pooled_cpm: 5.78
n_lines_expressing: 48
n_dd_up: 11
n_dd_down: 10
n_dd_up_clean: 3
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# SLC27A5

*solute carrier family 27 member 5* — 19q13.43

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.53× (z +10.5, q 4e-23, up in 5 of 7 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belinostat (drug)]] 0.5 µM: 1.53× (z +5.0, q 6e-05, up in 13 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.443× (z -9.7, q 2e-19, down in 29 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM53A]] (+0.66, fdr 7e-06), [[RRP7BP]] (+0.66, fdr 1e-05), [[ST6GALNAC6-1]] (+0.65, fdr 1e-05); moves opposite to [[IFNAR1]] (-0.56, fdr 7e-05), [[STXBP3]] (-0.55, fdr 3e-05), [[RO60]] (-0.52, fdr 6e-05).
> It sits in the **+** arm of [[Module 036]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ABCA3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 9 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1380.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.53×** | +10.5 | 4e-23 | 5/7 (A498, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.89×** | +7.5 | 2e-11 | 13/20 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.76×** | +6.1 | 2e-07 | 8/13 (NCI-H1792, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.66×** | +5.9 | 5e-07 | 22/43 (NCI-H1792, A549, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.63×** | +5.5 | 4e-06 | 10/26 (LoVo, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.54×** | +5.0 | 4e-05 | 17/43 (SW480, NCI-H1792, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.53×** | +5.0 | 6e-05 | 13/37 (A-172, HT-29, …) | two highest doses | cell-cycle shift (explains ~8% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.30×** | +4.3 | 0.001 | 13/36 (A498, C32, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.39×** | +3.9 | 0.007 | 4/26 (SK-MEL-2, NCI-H23, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.09× | +3.4 | 0.037 | 2/45 (SK-MEL-2, RPMI-7951) | inconsistent across doses |  |
| [[Ritonavir (drug)]] 5 µM |  | **1.23×** | +3.4 | 0.037 | 6/42 (SW 900, NCI-H1792, …) | top dose only |  |
| [[Cabozantinib (S-malate) (drug)]] 0.05 µM |  | **1.31×** | +3.1 | 0.080 | 3/42 (SW480, C-33 A, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 0.5 µM |  | 1.29× | +3.0 | 0.11 | 7/32 (NCI-H2030, SW480, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1380.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.443×** | -9.7 | 2e-19 | 29/43 (PANC-1, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.517×** | -7.5 | 1e-11 | 23/41 (A549, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.642×** | -5.3 | 2e-05 | 14/43 (BT-474, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.654×** | -5.1 | 6e-05 | 17/35 (RKO, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~18% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.720×** | -3.9 | 0.009 | 16/42 (A-427, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.722×** | -3.9 | 0.009 | 14/33 (NCI-H23, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.798×** | -3.8 | 0.010 | 17/38 (SW48, BT-474, …) | two highest doses | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.759×** | -3.3 | 0.069 | 11/43 (PANC-1, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.762×** | -3.3 | 0.069 | 7/43 (hTERT-HPNE, SW 900, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM |  | **0.832×** | -3.1 | 0.096 | 14/42 (LS 180, A-427, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | 0.775× | -3.1 | 0.12 | 11/42 (RKO, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1380. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 7.33 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0939× (z -10.7) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.136× (z -8.7) |
| [[RKO (line)]] | wt | 15.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0541× (z -14.1) |
| [[A-427 (line)]] | wt | 12.7 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.210× (z -8.7) |
| [[A549 (line)]] | wt | 6.29 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.114× (z -9.1) |
| [[PANC-1 (line)]] | alt | 7.42 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.130× (z -12.5) |
| [[SW48 (line)]] | wt | 18.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -9.0) ⚠ cell-cycle shift, explains ~41% of this change |
| [[A-172 (line)]] | wt | 2.41 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.68 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.33 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.41 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.27 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.64 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.16 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.48 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.62 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.28 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.72 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.45 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.23 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.70 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.66 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.46 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.79 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.94 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.70 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.71 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.61 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 8.21 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.81 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.97 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.52 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.99 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.23 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.40 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1380), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM53A]] | +0.66 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[RRP7BP]] | +0.66 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[ST6GALNAC6-1]] | +0.65 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[SLC25A10]] | +0.65 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[IL9RP3]] | +0.64 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[POLR3H]] | +0.61 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[GNB1L]] | +0.61 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[NOP2]] | +0.60 | +0.57 / +0.64 | both halves | 1e-05 |  |
| [[EIF3B]] | +0.60 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[TMEM201]] | +0.60 | +0.42 / +0.54 | both halves | 4e-05 |  |
| [[ZNF787]] | +0.59 | +0.47 / +0.57 | both halves | 2e-05 |  |
| [[TOMM40]] | +0.58 | +0.52 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IFNAR1]] | -0.56 | -0.38 / -0.52 | both halves | 7e-05 |  |
| [[STXBP3]] | -0.55 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[RO60]] | -0.52 | -0.39 / -0.50 | both halves | 6e-05 |  |
| [[ARMT1]] | -0.52 | -0.31 / -0.50 | both halves | 2e-04 |  |
| [[PHC3]] | -0.50 | -0.44 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ABCA3]] | B | ABCA3 activity raises SLC27A5's level | lines that do not express ABCA3 (9) vs lines expressing it (41) | 1.57× lower at baseline in the lines without ABCA3 | 0.096 | ⚠ within organs, on part of the lines; also absent: SLC37A1, CCDC88C, GRTP1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **+** arm (projection on the module's main direction 0.510). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (37.8, -21.9); signed map (-12.7, -55.0). **Vector** length 52.6, 6.85% of its response variance represented; |z| ≥ 3 in 928 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.9 | +10.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.7 | +6.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.1 | +7.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +3.1 | +5.9 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | +2.4 | +0.6 |
|  | [[EX229 (drug)]] 5 µM |  | +1.8 | +1.9 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +1.6 | +2.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +2.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.4 | +2.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.4 | +1.8 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -3.4 | -7.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.2 | -9.7 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.2 | -2.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | -2.0 | -3.1 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | -1.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.6 | -2.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.5 | -1.9 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.4 | -1.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.4 | -1.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.3 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 27 member 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.43 — chr19:58,479,512-58,512,413 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FATP5, VLACSR, VLCS-H2, VLCSH2, FACVL3, FLJ22987, ACSVL6, ACSB |
| Gene groups (HGNC) | Acyl-CoA synthetase family; Solute carrier family 27 |
| Hallmark sets | BILE_ACID_METABOLISM |
| Reactome | 7 pathways, smallest: Synthesis of bile acids and bile salts via 24-hydroxycholesterol; Recycling of bile acids and salts; Synthesis of bile acids and bile salts via 7alpha-hydroxycholesterol |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y2P5](https://www.uniprot.org/uniprotkb/Q9Y2P5) (Long-chain fatty acid transport protein 5):

> May mediate the import of long-chain fatty acids (LCFA) by facilitating their transport across cell membranes. Also catalyzes the ATP-dependent formation of fatty acyl-CoA using LCFA and very-long-chain fatty acids (VLCFA) as substrates. Mainly functions as a bile acyl-CoA synthetase catalyzing the activation of bile acids via ATP-dependent formation of bile acid CoA thioesters which is necessary for their subsequent conjugation with glycine or taurine. Both primary bile acids (cholic acid and …

**Summary**, from NCBI Gene [10998](https://www.ncbi.nlm.nih.gov/gene/10998):

> The protein encoded by this gene is an isozyme of very long-chain acyl-CoA synthetase (VLCS). It is capable of activating very long-chain fatty-acids containing 24- and 26-carbons. It is expressed in liver and associated with endoplasmic reticulum but not with peroxisomes. Its primary role is in fatty acid elongation or complex lipid synthesis rather than in degradation. This gene has a mouse ortholog. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:10999](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10999) · Entrez [10998](https://www.ncbi.nlm.nih.gov/gene/10998) · UniProt [Q9Y2P5](https://www.uniprot.org/uniprotkb/Q9Y2P5) · Ensembl [ENSG00000083807](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000083807)

## Data

Gene col 1380: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1380); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1380, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1380]; `tensor/DDL_lfc|DDL_z.npy` [1380]; `embed/gene_vectors.npy` [1380]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1380 or target_col == 1380). Every well: [[SLC27A5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC27A5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
