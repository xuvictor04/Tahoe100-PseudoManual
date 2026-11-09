---
symbol: "ZSCAN18"
type: "gene"
col: 4273
ensembl_id: "ENSG00000121413"
name: "zinc finger and SCAN domain containing 18"
location: "19q13.43"
module: 16
arm: "+"
pooled_cpm: 7.34
n_lines_expressing: 29
n_dd_up: 8
n_dd_down: 15
n_dd_up_clean: 6
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 2
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# ZSCAN18

*zinc finger and SCAN domain containing 18* — 19q13.43

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.42× (z +6.1, q 6e-07, up in 13 of 25 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.538× (z -10.7, q 5e-24, down in 19 of 26 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CROCCP2-1]] (+0.64, fdr 7e-06), [[SLC31A2]] (+0.62, fdr 2e-05), [[LIPT1]] (+0.62, fdr 1e-05); moves opposite to [[TXNDC5]] (-0.65, fdr 7e-06), [[STT3B]] (-0.60, fdr 1e-05), [[SMG1P6]] (-0.58, fdr 3e-05).
> It sits in the **+** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 2 go from it, the strongest it → [[ZNF254]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4273.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.42×** | +6.1 | 6e-07 | 13/25 (A-427, J82, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.66×** | +6.0 | 8e-07 | 12/26 (A-427, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.01×** | +4.5 | 0.001 | 10/15 (NCI-H460, C-33 A, …) | rises with dose | noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.10× | +4.2 | 0.004 | 4/27 (HOP62, NCI-H23, …) | inconsistent across doses |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.37×** | +3.9 | 0.011 | 10/26 (C-33 A, H4, …) | rises with dose |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.55×** | +3.8 | 0.013 | 10/25 (SK-MEL-2, CFPAC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.54×** | +3.8 | 0.013 | 10/20 (MIA PaCa-2, CFPAC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.48×** | +3.4 | 0.041 | 8/23 (SK-MEL-2, BT-474, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **1.22×** | +3.4 | 0.044 | 8/27 (MIA PaCa-2, H4, …) | all doses, flat | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 9 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4273.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.538×** | -10.7 | 5e-24 | 19/26 (NCI-H460, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.648×** | -5.1 | 1e-04 | 12/22 (NCI-H460, HOP62, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.635×** | -4.7 | 4e-04 | 9/15 (SNU-423, SK-MEL-2, …) | inconsistent across doses | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.492×** | -4.5 | 8e-04 | 12/24 (Panc 03.27, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.714×** | -4.1 | 0.004 | 12/26 (NCI-H23, C-33 A, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.527×** | -4.1 | 0.004 | 11/23 (SK-MEL-2, J82, …) | top dose only | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.713×** | -4.0 | 0.006 | 13/25 (RPMI-7951, A-427, …) | top dose only | position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.552×** | -3.8 | 0.010 | 7/13 (NCI-H2347, NCI-H23, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.569×** | -3.6 | 0.020 | 10/26 (Panc 03.27, H4, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.747×** | -3.6 | 0.021 | 10/26 (Panc 03.27, NCI-H460, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.576×** | -3.5 | 0.021 | 7/26 (CFPAC-1, A-427, …) | rises with dose | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.750×** | -3.5 | 0.021 | 6/26 (NCI-H1792, NCI-H2030, …) | two highest doses | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.744×** | -3.5 | 0.023 | 9/26 (NCI-H23, C-33 A, …) | top dose only |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.698×** | -3.1 | 0.068 | 4/27 (NCI-H460, NCI-H2347, …) | rises with dose | noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **0.782×** | -3.0 | 0.098 | 10/26 (A-427, NCI-H460, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.32 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4273. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Panc 03.27 (line)]] | alt | 16.5 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.192× (z -13.4) |
| [[SW 900 (line)]] | alt | 28.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.149× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 14.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.402× (z -9.0) |
| [[Hs 766T (line)]] | wt | 7.36 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.190× (z -9.3) |
| [[MIA PaCa-2 (line)]] | alt | 18.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.373× (z -9.0) |
| [[NCI-H23 (line)]] | alt | 22.2 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.253× (z -9.5) ⚠ cell-cycle shift, explains ~37% of this change |
| [[NCI-H460 (line)]] | wt | 8.68 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.185× (z -15.2) |
| [[SK-MEL-2 (line)]] | alt | 21.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.183× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[SNU-423 (line)]] | alt | 18.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.190× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[A-172 (line)]] | wt | 0.928 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.855 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.41 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.648 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.808 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.669 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.734 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.808 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.705 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.44 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.789 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.76 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.647 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.583 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.798 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.673 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.614 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 6.06 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.90 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.84 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.15 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.760 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.13 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 6.55 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.844 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 8.27 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.702 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.817 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.612 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4273), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CROCCP2-1]] | +0.64 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[SLC31A2]] | +0.62 | +0.48 / +0.68 | both halves | 2e-05 |  |
| [[LIPT1]] | +0.62 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[MAPK1IP1L]] | +0.60 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[CERS4]] | +0.60 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[DCTN6]] | +0.60 | +0.45 / +0.64 | both halves | 3e-05 |  |
| [[MRFAP1L1]] | +0.60 | +0.50 / +0.62 | both halves | 1e-05 |  |
| [[BTN2A2]] | +0.59 | +0.46 / +0.63 | both halves | 2e-05 |  |
| [[JUND]] | +0.59 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[NT5C]] | +0.59 | +0.37 / +0.60 | both halves | 9e-05 |  |
| [[ZBTB4]] | +0.58 | +0.51 / +0.56 | both halves | 1e-05 | same gene group |
| [[DUSP15]] | +0.58 | +0.48 / +0.62 | both halves | 2e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TXNDC5]] | -0.65 | -0.61 / -0.65 | both halves | 7e-06 |  |
| [[STT3B]] | -0.60 | -0.54 / -0.62 | both halves | 1e-05 |  |
| [[SMG1P6]] | -0.58 | -0.44 / -0.58 | both halves | 3e-05 |  |
| [[PTDSS1]] | -0.57 | -0.39 / -0.57 | both halves | 6e-05 |  |
| [[GDI2]] | -0.57 | -0.57 / -0.50 | both halves | 1e-05 |  |
| [[RNPS1]] | -0.57 | -0.42 / -0.57 | both halves | 4e-05 |  |
| [[RPN1]] | -0.56 | -0.52 / -0.59 | both halves | 1e-05 |  |
| [[DPAGT1]] | -0.56 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[ERMP1]] | -0.55 | -0.54 / -0.57 | both halves | 1e-05 |  |
| [[NSUN2]] | -0.55 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[TPM3]] | -0.55 | -0.49 / -0.56 | both halves | 1e-05 |  |
| [[TM9SF3]] | -0.55 | -0.47 / -0.59 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF254]] | B | ZSCAN18 activity raises ZNF254's level | lines that do not express ZSCAN18 (21) vs lines expressing it (29) | 1.92× lower at baseline in the lines without ZSCAN18 | 0.094 | ⚠ within organs, on part of the lines; also absent: ZNF829, ZNF568, ZNF471 |
| [[YJU2B]] | B | ZSCAN18 activity raises YJU2B's level | lines that do not express ZSCAN18 (21) vs lines expressing it (29) | 1.12× lower at baseline in the lines without ZSCAN18 | 0.098 | ⚠ within organs, on part of the lines; also absent: ZNF829, ZNF568, ZNF471 |

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.411). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-41.4, 25.9); signed map (-1.0, -12.9). **Vector** length 42.2, 7.33% of its response variance represented; |z| ≥ 3 in 459 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +3.0 | +6.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.0 | +6.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | +1.8 | +3.4 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.6 | +1.9 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.5 | +2.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | +3.4 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.0 | +3.8 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.0 | +3.8 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +0.9 | +2.4 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +0.9 | +2.7 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -2.6 | -10.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -2.3 | -3.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -2.1 | -4.0 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | -1.4 | -3.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.3 | -3.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.2 | -1.9 |
|  | [[EX229 (drug)]] 5 µM |  | -1.2 | -4.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.0 | -3.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.0 | -2.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.0 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger and SCAN domain containing 18 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.43 — chr19:58,083,838-58,118,427 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ12895; previously ZNF447 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; SCAN domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TBC5](https://www.uniprot.org/uniprotkb/Q8TBC5) (Zinc finger and SCAN domain-containing protein 18):

> May be involved in transcriptional regulation.

**Summary**, from NCBI Gene [65982](https://www.ncbi.nlm.nih.gov/gene/65982):

> Predicted to enable DNA-binding transcription factor activity, RNA polymerase II-specific and RNA polymerase II cis-regulatory region sequence-specific DNA binding activity. Predicted to be involved in regulation of transcription by RNA polymerase II. Predicted to be located in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:21037](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21037) · Entrez [65982](https://www.ncbi.nlm.nih.gov/gene/65982) · UniProt [Q8TBC5](https://www.uniprot.org/uniprotkb/Q8TBC5) · Ensembl [ENSG00000121413](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000121413)

## Data

Gene col 4273: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4273); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4273, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4273]; `tensor/DDL_lfc|DDL_z.npy` [4273]; `embed/gene_vectors.npy` [4273]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4273 or target_col == 4273). Every well: [[ZSCAN18 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZSCAN18.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
