---
symbol: "MRPS18A"
type: "gene"
col: 1762
ensembl_id: "ENSG00000096080"
name: "mitochondrial ribosomal protein S18A"
location: "6p21.1"
module: 16
arm: "+"
pooled_cpm: 11.3
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 5
n_dd_up_clean: 14
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# MRPS18A

*mitochondrial ribosomal protein S18A* — 6p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 1.76× (z +10.9, q 1e-24, up in 27 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.770× (z -7.1, q 5e-10, down in 25 of 44 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 2 lines (LoVo 0.128×, HT-29 0.106×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (CFPAC-1 0.165×, LoVo 0.262×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (LoVo 0.386×); [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM in 1 line (C-33 A 0.106×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CSTF2T]] (+0.79, fdr 7e-06), [[ZNF317]] (+0.71, fdr 7e-06), [[SRRD]] (+0.70, fdr 7e-06); moves opposite to [[KDELR1]] (-0.60, fdr 3e-05), [[SRD5A1]] (-0.59, fdr 1e-05), [[CRNDE]] (-0.57, fdr 1e-05).
> It sits in the **+** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CRNDE]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1762.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.76×** | +10.9 | 1e-24 | 27/43 (PANC-1, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.77×** | +10.3 | 2e-22 | 36/47 (HOP62, HT-29, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.69×** | +10.2 | 5e-22 | 40/46 (PANC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.72×** | +9.6 | 1e-19 | 33/46 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.36×** | +8.4 | 4e-15 | 22/46 (PANC-1, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~17% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.50×** | +7.8 | 4e-13 | 22/47 (PANC-1, NCI-H460, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.41×** | +6.7 | 2e-09 | 19/47 (SW480, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.42×** | +6.3 | 3e-08 | 21/43 (HEC-1-A, A-172, …) | all doses, stronger at high dose | low cells (technical?) |
| [[PH-797804 (drug)]] 5 µM |  | **1.68×** | +5.2 | 1e-05 | 12/43 (HEC-1-A, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.29×** | +4.9 | 5e-05 | 15/47 (HOP62, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.29×** | +4.5 | 3e-04 | 9/41 (CFPAC-1, SW48, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~22% of this change | **1.25×** | +4.3 | 9e-04 | 17/41 (HS-578T, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.26×** | +4.3 | 9e-04 | 14/45 (CFPAC-1, HCT15, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Pralsetinib (drug)]] 5 µM |  | **1.46×** | +3.8 | 0.005 | 6/44 (SW480, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.29×** | +3.6 | 0.014 | 9/44 (NCI-H460, Panc 03.27, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.20× | +3.4 | 0.020 | 8/47 (HEC-1-A, HOP62, …) | rises with dose |  |
| [[BI-78D3 (drug)]] 0.5 µM |  | **1.28×** | +3.4 | 0.023 | 3/45 (C32, J82, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1762.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 2 lines (LoVo 0.128×, HT-29 0.106×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (CFPAC-1 0.165×, LoVo 0.262×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (LoVo 0.386×); [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM in 1 line (C-33 A 0.106×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.770×** | -7.1 | 5e-10 | 25/44 (LoVo, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.793×** | -4.5 | 0.002 | 18/35 (NCI-H460, SNU-423, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.810×** | -3.8 | 0.032 | 12/41 (NCI-H1792, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.823×** | -3.5 | 0.060 | 11/24 (CFPAC-1, LoVo, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Allantoin (drug)]] 0.5 µM |  | 0.836× | -3.5 | 0.060 | 11/45 (PANC-1, COLO 205, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.828×** | -3.4 | 0.068 | 14/46 (NCI-H23, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Verteporfin (drug)]] 0.5 µM |  | 0.854× | -3.1 | 0.18 | 4/47 (Panc 03.27, A549, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1762. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 16.8 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.128× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.386× (z -10.0) |
| [[C-33 A (line)]] | alt | 10.6 | 0 | 1 | — | [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM 0.106× (z -8.6) |
| [[CFPAC-1 (line)]] | alt | 13.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.165× (z -13.0) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 13.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.106× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 9.12 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.268× (z -9.9) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 9.43 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.96 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.81 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.38 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.11 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.15 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.10 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.61 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.94 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.42 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.20 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.72 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.57 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.80 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.59 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.79 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.69 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.93 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.16 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 12.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1762), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CSTF2T]] | +0.79 | +0.76 / +0.76 | both halves | 7e-06 |  |
| [[ZNF317]] | +0.71 | +0.67 / +0.67 | both halves | 7e-06 | STRING 536 |
| [[SRRD]] | +0.70 | +0.66 / +0.75 | both halves | 7e-06 |  |
| [[ZSWIM1]] | +0.70 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[KLHL9]] | +0.70 | +0.65 / +0.68 | both halves | 7e-06 |  |
| [[ABT1]] | +0.69 | +0.69 / +0.67 | both halves | 7e-06 |  |
| [[POP4]] | +0.68 | +0.72 / +0.59 | both halves | 7e-06 |  |
| [[ZNF502]] | +0.68 | +0.59 / +0.68 | both halves | 7e-06 |  |
| [[PABIR1]] | +0.68 | +0.58 / +0.71 | both halves | 7e-06 |  |
| [[RTL6]] | +0.67 | +0.57 / +0.69 | both halves | 9e-06 |  |
| [[GPKOW]] | +0.67 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[ZSCAN26]] | +0.66 | +0.60 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KDELR1]] | -0.60 | -0.46 / -0.62 | both halves | 3e-05 |  |
| [[SRD5A1]] | -0.59 | -0.55 / -0.59 | both halves | 1e-05 |  |
| [[CRNDE]] | -0.57 | -0.51 / -0.64 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CRNDE]] | C | CRNDE activity lowers MRPS18A's level | lines that do not express CRNDE (3) vs lines expressing it (47) | 1.52× higher at baseline in the lines without CRNDE | 0.096 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: HSD17B14, DMXL2, CRB1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.758). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-34.8, 10.1); signed map (-0.0, -26.2). **Vector** length 61.2, 8.57% of its response variance represented; |z| ≥ 3 in 818 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +5.4 | +10.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.7 | +7.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.6 | +9.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.1 | +10.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.1 | +10.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.3 | +6.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.1 | +5.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.8 | +1.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.7 | +1.7 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -3.7 | -3.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.1 | -7.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -2.5 | -3.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | -2.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.7 | -0.8 |
|  | [[Entecavir (monohydrate) (drug)]] 0.5 µM |  | -1.2 | -1.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.2 | -0.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.2 | -3.0 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.0 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial ribosomal protein S18A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.1 — chr6:43,671,202-43,687,791 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10548, MRPS18-3, mL66 |
| Gene groups (HGNC) | Mitochondrial ribosomal proteins; Large subunit mitochondrial ribosomal proteins |
| Reactome | 6 pathways, smallest: Mitochondrial ribosome-associated quality control; Mitochondrial translation elongation; Mitochondrial translation initiation |
| Matched by | ensembl_id |

UniProt [Q9NVS2](https://www.uniprot.org/uniprotkb/Q9NVS2) carries no function annotation.

**Summary**, from NCBI Gene [55168](https://www.ncbi.nlm.nih.gov/gene/55168):

> Mammalian mitochondrial ribosomal proteins are encoded by nuclear genes and help in protein synthesis within the mitochondrion. Mitochondrial ribosomes (mitoribosomes) consist of a small 28S subunit and a large 39S subunit. They have an estimated 75% protein to rRNA composition compared to prokaryotic ribosomes, where this ratio is reversed. Another difference between mammalian mitoribosomes and prokaryotic ribosomes is that the latter contain a 5S rRNA. Among different species, the proteins …

**Accessions** — [HGNC:14515](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14515) · Entrez [55168](https://www.ncbi.nlm.nih.gov/gene/55168) · UniProt [Q9NVS2](https://www.uniprot.org/uniprotkb/Q9NVS2) · Ensembl [ENSG00000096080](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000096080)

## Data

Gene col 1762: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1762); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1762, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1762]; `tensor/DDL_lfc|DDL_z.npy` [1762]; `embed/gene_vectors.npy` [1762]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1762 or target_col == 1762). Every well: [[MRPS18A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MRPS18A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
