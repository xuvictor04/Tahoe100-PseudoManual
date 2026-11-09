---
symbol: "PACSIN3"
type: "gene"
col: 9204
ensembl_id: "ENSG00000165912"
name: "protein kinase C and casein kinase substrate in neurons 3"
location: "11p11.2"
module: 2
arm: "+"
pooled_cpm: 7.37
n_lines_expressing: 48
n_dd_up: 4
n_dd_down: 10
n_dd_up_clean: 0
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# PACSIN3

*protein kinase C and casein kinase substrate in neurons 3* — 11p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.90× (z +10.4, q 2e-22, up in 22 of 27 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (A498 3.58×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.354× (z -14.4, q 3e-44, down in 35 of 40 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GRHPR]] (+0.65, fdr 1e-05), [[TSPAN17]] (+0.61, fdr 1e-05), [[MIIP]] (+0.59, fdr 1e-05); moves opposite to [[THAP9]] (-0.52, fdr 6e-05), [[ALG13]] (-0.51, fdr 5e-05), [[ARMH4]] (-0.50, fdr 3e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[HES2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 7 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9204.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (A498 3.58×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.90×** | +10.4 | 2e-22 | 22/27 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.36×** | +8.0 | 3e-13 | 15/15 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.18×** | +7.0 | 5e-10 | 13/20 (A498, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.76×** | +5.5 | 7e-06 | 17/32 (AsPC-1, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~4% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.15× | +4.5 | 9e-04 | 4/46 (NCI-H23, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | 1.68× | +3.2 | 0.12 | 9/37 (RKO, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | 1.92× | +3.1 | 0.12 | 2/20 (BT-474, NCI-H23) | top dose only | noisy plate (z scaled) |
| [[Celecoxib (drug)]] 0.5 µM |  | 1.64× | +3.1 | 0.12 | 5/42 (Panc 03.27, KATO III, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Bimiralisib (drug)]] 0.5 µM |  | 1.63× | +3.0 | 0.12 | 4/41 (LS 180, NCI-H2030, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | 1.25× | +3.0 | 0.12 | 6/45 (J82, SW480, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | 1.63× | +3.0 | 0.12 | 9/34 (Hs 766T, RKO, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[vincristine (drug)]] 0.5 µM |  | 1.63× | +3.0 | 0.12 | 4/39 (SW480, NCI-H460, …) | two highest doses | low cells (technical?); noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9204.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.354×** | -14.4 | 3e-44 | 35/40 (J82, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.307×** | -11.6 | 1e-28 | 33/37 (LOX-IMVI, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.445×** | -8.0 | 3e-13 | 34/45 (SW480, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.496×** | -6.9 | 7e-10 | 30/44 (LOX-IMVI, RKO, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.541×** | -6.1 | 2e-07 | 24/43 (NCI-H2030, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.590×** | -5.0 | 5e-05 | 22/42 (AsPC-1, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.404×** | -4.4 | 1e-03 | 18/42 (Panc 03.27, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.656×** | -4.2 | 0.002 | 19/40 (AsPC-1, SW48, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.431×** | -4.1 | 0.003 | 17/37 (SW480, NCI-H2030, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.724×** | -3.2 | 0.076 | 14/43 (hTERT-HPNE, SNU-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 0.735× | -3.1 | 0.11 | 6/43 (LS 180, LoVo, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9204. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 9.65 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -12.4) |
| [[Panc 03.27 (line)]] | alt | 11.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.166× (z -12.4) |
| [[LOX-IMVI (line)]] | wt | 7.42 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0463× (z -13.2) |
| [[PANC-1 (line)]] | alt | 5.88 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -9.2) |
| [[A-172 (line)]] | wt | 8.54 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.135× (z -9.0) |
| [[A498 (line)]] | wt | 15.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.58× (z +9.1) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 9.21 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.106× (z -13.9) |
| [[BT-474 (line)]] | alt | 8.51 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0993× (z -13.1) |
| [[Hs 766T (line)]] | wt | 11.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -10.2) |
| [[HS-578T (line)]] | alt | 4.63 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0685× (z -9.2) |
| [[J82 (line)]] | alt | 15.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.107× (z -18.8) |
| [[LS 180 (line)]] | wt | 9.37 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -10.9) |
| [[NCI-H1573 (line)]] | alt | 5.17 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.126× (z -10.1) |
| [[NCI-H2347 (line)]] | alt | 5.06 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -10.0) |
| [[NCI-H460 (line)]] | wt | 4.76 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -9.2) |
| [[SK-MEL-2 (line)]] | alt | 7.60 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.195× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 6.59 | 0 | 1 (1 ⚠) | — | [[Nimesulide (drug)]] 5 µM 0.0760× (z -9.9) ⚠ toxic; unreliable plate only |
| [[SW1417 (line)]] | alt | 14.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.166× (z -13.7) |
| [[SW480 (line)]] | alt | 7.96 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -12.1) |
| [[A-427 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.35 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.45 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.92 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.06 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.74 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.35 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.15 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.76 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.03 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.47 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.82 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.40 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.42 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.40 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.52 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.15 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9204), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GRHPR]] | +0.65 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[TSPAN17]] | +0.61 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[MIIP]] | +0.59 | +0.54 / +0.53 | both halves | 1e-05 | same gene group |
| [[NCK2]] | +0.59 | +0.60 / +0.39 | both halves | 5e-05 | same gene group |
| [[ZDHHC8]] | +0.59 | +0.60 / +0.43 | both halves | 3e-05 |  |
| [[PARD6G]] | +0.58 | +0.50 / +0.46 | both halves | 2e-05 |  |
| [[STK25]] | +0.58 | +0.56 / +0.44 | both halves | 3e-05 |  |
| [[TRABD]] | +0.57 | +0.54 / +0.46 | both halves | 3e-05 |  |
| [[USP35]] | +0.57 | +0.61 / +0.29 | both halves | 2e-04 |  |
| [[TBC1D24]] | +0.57 | +0.59 / +0.35 | both halves | 1e-04 |  |
| [[INPP4A]] | +0.56 | +0.50 / +0.36 | both halves | 1e-04 |  |
| [[SRPK2]] | +0.56 | +0.55 / +0.34 | both halves | 1e-04 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[THAP9]] | -0.52 | -0.55 / -0.38 | both halves | 6e-05 |  |
| [[ALG13]] | -0.51 | -0.40 / -0.43 | both halves | 5e-05 |  |
| [[ARMH4]] | -0.50 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[HELQ]] | -0.50 | -0.55 / -0.21 | both halves | 7e-04 |  |
| [[THAP6]] | -0.49 | -0.58 / -0.20 | both halves | 7e-04 |  |
| [[PFN1]] | -0.48 | -0.44 / -0.36 | both halves | 9e-05 |  |
| [[ZNF585A]] | -0.47 | -0.50 / -0.23 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HES2]] | B | HES2 activity raises PACSIN3's level | lines that do not express HES2 (20) vs lines expressing it (30) | 1.37× lower at baseline in the lines without HES2 | 0.024 | ⚠ within organs, on part of the lines; also absent: FBXO2, PADI2, YBX2 |
| [[BTBD6]] | B | BTBD6 activity lowers PACSIN3's level | lines that do not express BTBD6 (8) vs lines expressing it (42) | 1.40× higher at baseline in the lines without BTBD6 | 0.077 | ⚠ within organs, on part of the lines; also absent: ENSG00000225647, ENSG00000254394, RPL23AP49 |
| [[SNTA1]] | B | SNTA1 activity raises PACSIN3's level | lines that do not express SNTA1 (5) vs lines expressing it (45) | 1.82× lower at baseline in the lines without SNTA1 | 0.087 | ⚠ within organs, on part of the lines; also absent: SACS, CLTCL1, MXRA7; maybe low, not absent |
| [[NCS1]] | B | NCS1 activity raises PACSIN3's level | lines that do not express NCS1 (6) vs lines expressing it (44) | 1.56× lower at baseline in the lines without NCS1 | 0.096 | ⚠ within organs, on part of the lines; also absent: SH3BP5, ZNF618, PBK; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.561). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-5.3, -21.4); signed map (-45.2, -7.2). **Vector** length 55.7, 8.64% of its response variance represented; |z| ≥ 3 in 803 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +3.8 | +2.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.3 | +2.2 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.1 | +2.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.8 | +2.8 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.8 | +1.1 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +1.7 | +2.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.7 | +1.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +3.2 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.6 | +3.0 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -4.0 | -14.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.0 | -11.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | -1.8 | -5.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | -1.3 | -4.4 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.2 | -6.9 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.1 | -2.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.1 | -2.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.1 | -1.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.1 | -1.5 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -1.0 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | protein kinase C and casein kinase substrate in neurons 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p11.2 — chr11:47,177,522-47,186,443 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SDPIII |
| Gene groups (HGNC) | F-BAR domain containing; MicroRNA protein coding host genes; SH3 domain containing |
| Reactome | 3 pathways, smallest: Clathrin-mediated endocytosis; Membrane Trafficking; Vesicle-mediated transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UKS6](https://www.uniprot.org/uniprotkb/Q9UKS6) (Protein kinase C and casein kinase substrate in neurons protein 3):

> Plays a role in endocytosis and regulates internalization of plasma membrane proteins. Overexpression impairs internalization of SLC2A1/GLUT1 and TRPV4 and increases the levels of SLC2A1/GLUT1 and TRPV4 at the cell membrane. Inhibits the TRPV4 calcium channel activity (By similarity).

**Summary**, from NCBI Gene [29763](https://www.ncbi.nlm.nih.gov/gene/29763):

> This gene is a member of the protein kinase C and casein kinase substrate in neurons family. The encoded protein is involved in linking the actin cytoskeleton with vesicle formation. Alternative splicing results in multiple transcript variants. [provided by RefSeq, May 2010]

**Accessions** — [HGNC:8572](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8572) · Entrez [29763](https://www.ncbi.nlm.nih.gov/gene/29763) · UniProt [Q9UKS6](https://www.uniprot.org/uniprotkb/Q9UKS6) · Ensembl [ENSG00000165912](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165912)

## Data

Gene col 9204: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9204); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9204, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9204]; `tensor/DDL_lfc|DDL_z.npy` [9204]; `embed/gene_vectors.npy` [9204]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9204 or target_col == 9204). Every well: [[PACSIN3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PACSIN3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
