---
symbol: "POU6F1"
type: "gene"
col: 11512
ensembl_id: "ENSG00000184271"
name: "POU class 6 homeobox 1"
location: "12q13.13"
module: 124
arm: "+"
pooled_cpm: 6.55
n_lines_expressing: 48
n_dd_up: 6
n_dd_down: 20
n_dd_up_clean: 2
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/124"]
generated_by: "tahoemap"
---

# POU6F1

*POU class 6 homeobox 1* — 12q13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.51× (z +7.1, q 5e-10, up in 23 of 40 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SW480 2.46×).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.193× (z -20.1, q 0e+00, down in 42 of 45 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WNT3]] (+0.70, fdr 2e-05), [[EPM2A]] (+0.69, fdr 5e-05), [[PYGO1]] (+0.67, fdr 3e-05); moves opposite to [[RAB3A]] (-0.69, fdr 9e-05), [[SLC25A11]] (-0.67, fdr 2e-05), [[ALAD]] (-0.67, fdr 3e-05).
> It sits in the **+** arm of [[Module 124]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[WNT5B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11512.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SW480 2.46×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.51×** | +7.1 | 5e-10 | 23/40 (SW480, A549, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.71×** | +6.3 | 9e-08 | 8/12 (J82, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.54×** | +5.3 | 2e-05 | 13/29 (AsPC-1, SW 900, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.60×** | +5.3 | 2e-05 | 9/16 (NCI-H2347, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.41×** | +4.2 | 0.003 | 9/45 (C32, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.36×** | +3.7 | 0.024 | 13/34 (SK-MEL-2, LoVo, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.05 µM |  | 1.21× | +3.2 | 0.12 | 7/44 (PANC-1, Hs 766T, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11512.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.193×** | -20.1 | 0e+00 | 42/45 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.251×** | -16.9 | 0e+00 | 41/45 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.266×** | -15.5 | 0e+00 | 40/45 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.554×** | -10.2 | 3e-22 | 30/42 (RKO, hTERT-HPNE, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.444×** | -9.9 | 4e-21 | 31/45 (SW480, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.496×** | -8.2 | 2e-14 | 27/44 (RKO, LOX-IMVI, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.548×** | -7.3 | 2e-11 | 23/38 (LOX-IMVI, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.340×** | -6.9 | 4e-10 | 23/43 (LoVo, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~19% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **0.569×** | -6.9 | 4e-10 | 22/40 (NCI-H1573, SW480, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.629×** | -5.7 | 9e-07 | 21/44 (SNU-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.652×** | -5.0 | 3e-05 | 17/41 (HEC-1-A, J82, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **0.666×** | -5.0 | 3e-05 | 20/45 (H4, PANC-1, …) | inconsistent across doses | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.463×** | -4.9 | 4e-05 | 19/40 (HEC-1-A, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **0.477×** | -4.7 | 9e-05 | 16/46 (RKO, NCI-H460, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.786×** | -4.1 | 0.001 | 12/44 (LOX-IMVI, C32, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.557×** | -3.7 | 0.007 | 12/37 (J82, A498, …) | rises with dose | noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM |  | **0.826×** | -3.3 | 0.030 | 9/45 (SNU-1, AN3 CA, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.36 per unit of S-phase module lfc, -0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11512. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 9.22 | 1 | 5 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.46× (z +8.9) | [[Panobinostat (drug)]] 5 µM 0.0961× (z -16.2) |
| [[NCI-H460 (line)]] | wt | 8.41 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.153× (z -11.3) |
| [[LOX-IMVI (line)]] | wt | 10.0 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.143× (z -10.3) |
| [[RKO (line)]] | wt | 17.0 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.188× (z -13.7) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.140× (z -11.0) |
| [[HEC-1-A (line)]] | alt | 7.42 | 0 | 3 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0696× (z -13.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.103× (z -11.7) |
| [[LoVo (line)]] | wt | 18.2 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.0960× (z -18.2) |
| [[H4 (line)]] | wt | 13.8 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.0804× (z -9.9) |
| [[hTERT-HPNE (line)]] | wt | 7.65 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.113× (z -10.6) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Vismodegib (drug)]] 0.5 µM 0.0546× (z -9.5) |
| [[MIA PaCa-2 (line)]] | alt | 6.52 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.0599× (z -12.5) |
| [[NCI-H2030 (line)]] | alt | 6.38 | 0 | 2 (1 ⚠) | — | [[Silodosin (drug)]] 5 µM 0.0748× (z -10.9) |
| [[SW48 (line)]] | wt | 8.34 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.0654× (z -8.8) |
| [[A498 (line)]] | wt | 9.53 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.200× (z -9.6) |
| [[C-33 A (line)]] | alt | 7.91 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0550× (z -9.6) |
| [[C32 (line)]] | wt | 6.90 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.119× (z -8.8) |
| [[HS-578T (line)]] | alt | 4.96 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.0243× (z -12.8) |
| [[HT-29 (line)]] | alt | 3.42 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.0257× (z -11.8) |
| [[J82 (line)]] | alt | 8.63 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.181× (z -8.6) |
| [[NCI-H1792 (line)]] | alt | 5.89 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0827× (z -9.5) |
| [[NCI-H23 (line)]] | alt | 4.81 | 0 | 1 | — | [[Dorzolamide (hydrochloride) (drug)]] 0.05 µM 0.0658× (z -9.1) |
| [[Panc 03.27 (line)]] | alt | 5.41 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.174× (z -8.8) ⚠ cell-cycle shift, explains ~46% of this change |
| [[A-172 (line)]] | wt | 5.48 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 8.80 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.78 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.42 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.89 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.29 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.71 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.45 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.06 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.54 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 4.33 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.70 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.11 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.41 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.20 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.56 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.28 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.98 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.18 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.29 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.56 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.88 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11512), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WNT3]] | +0.70 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[EPM2A]] | +0.69 | +0.50 / +0.39 | both halves | 5e-05 |  |
| [[PYGO1]] | +0.67 | +0.55 / +0.45 | both halves | 3e-05 |  |
| [[GABPB1]] | +0.67 | +0.54 / +0.34 | both halves | 1e-04 |  |
| [[RCC1L]] | +0.66 | +0.51 / +0.40 | both halves | 4e-05 |  |
| [[PRDM11]] | +0.65 | +0.42 / +0.42 | both halves | 4e-05 |  |
| [[AVEN]] | +0.65 | +0.49 / +0.40 | both halves | 4e-05 |  |
| [[C2orf88]] | +0.64 | +0.40 / +0.21 | both halves | 6e-04 |  |
| [[GTF3C2-AS2]] | +0.64 | +0.36 / +0.43 | both halves | 9e-05 |  |
| [[GCNT4]] | +0.64 | +0.40 / +0.32 | both halves | 2e-04 |  |
| [[ANKAR]] | +0.63 | +0.42 / +0.50 | both halves | 4e-05 |  |
| [[ACYP2]] | +0.63 | +0.38 / +0.46 | both halves | 6e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAB3A]] | -0.69 | -0.56 / -0.36 | both halves | 9e-05 |  |
| [[SLC25A11]] | -0.67 | -0.46 / -0.49 | both halves | 2e-05 |  |
| [[ALAD]] | -0.67 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[HPS3]] | -0.63 | -0.44 / -0.37 | both halves | 8e-05 |  |
| [[ZNF184]] | -0.63 | -0.49 / -0.59 | both halves | 1e-05 |  |
| [[ORC4]] | -0.62 | -0.46 / -0.48 | both halves | 3e-05 |  |
| [[INIP]] | -0.60 | -0.44 / -0.41 | both halves | 4e-05 |  |
| [[MRPL17]] | -0.60 | -0.41 / -0.37 | both halves | 7e-05 |  |
| [[DNAAF3]] | -0.59 | -0.38 / -0.21 | both halves | 7e-04 |  |
| [[GDE1]] | -0.59 | -0.39 / -0.38 | both halves | 7e-05 |  |
| [[PJA2]] | -0.58 | -0.44 / -0.33 | both halves | 1e-04 |  |
| [[TXNDC17]] | -0.58 | -0.40 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[WNT5B]] | B | WNT5B activity raises POU6F1's level | lines that do not express WNT5B (22) vs lines expressing it (28) | 1.42× lower at baseline in the lines without WNT5B | 0.020 | ⚠ within organs, on part of the lines; also absent: DPY19L2, TRIML2, VASH1 |
| [[HECTD2]] | B | HECTD2 activity raises POU6F1's level | lines that do not express HECTD2 (5) vs lines expressing it (45) | 1.96× lower at baseline in the lines without HECTD2 | 0.073 | ⚠ within organs, on part of the lines; also absent: IMPG2, PHC1, TPST1; maybe low, not absent |
| [[MIATNB]] | C | MIATNB activity raises POU6F1's level | lines that do not express MIATNB (3) vs lines expressing it (47) | 2.19× lower at baseline in the lines without MIATNB | 0.039 | ⚠ few lines (3 vs 47); across organs; also absent: MIAT, LRP1, KLF2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 124]]; 39 genes; this gene is in the **+** arm (projection on the module's main direction 0.759). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (-5.0, 10.6); signed map (24.1, -26.4). **Vector** length 70.3, 11.7% of its response variance represented; |z| ≥ 3 in 1,035 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.7 | +7.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.8 | +6.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.3 | +3.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.3 | +5.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.5 | +5.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.8 | +0.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +1.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.0 | -1.4 |
|  | [[Rapamycin (drug)]] 5 µM |  | +1.8 | +2.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.7 | +1.8 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -4.5 | -15.5 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.4 | -16.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | -3.9 | -20.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.7 | -6.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -2.4 | -9.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.8 | -2.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.7 | -4.7 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.6 | -2.8 |
|  | [[Relugolix (drug)]] 0.5 µM |  | -1.5 | -2.1 |
|  | [[Hesperidin (drug)]] 0.05 µM |  | -1.5 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | POU class 6 homeobox 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.13 — chr12:51,186,936-51,218,062 (-) |
| Ensembl biotype | protein_coding |
| Also known as | BRN5, MPOU, TCFB1 |
| Gene groups (HGNC) | POU class homeoboxes and pseudogenes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14863](https://www.uniprot.org/uniprotkb/Q14863) (POU domain, class 6, transcription factor 1):

> Transcription factor that binds preferentially to a variant of the octamer motif (5'-ATGATAAT-3').

**Summary**, from NCBI Gene [5463](https://www.ncbi.nlm.nih.gov/gene/5463):

> Enables DNA-binding transcription repressor activity, RNA polymerase II-specific and sequence-specific double-stranded DNA binding activity. Involved in negative regulation of transcription by RNA polymerase II. Located in nuclear body. Biomarker of lung adenocarcinoma. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:9224](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9224) · Entrez [5463](https://www.ncbi.nlm.nih.gov/gene/5463) · UniProt [Q14863](https://www.uniprot.org/uniprotkb/Q14863) · Ensembl [ENSG00000184271](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184271)

## Data

Gene col 11512: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11512); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11512, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11512]; `tensor/DDL_lfc|DDL_z.npy` [11512]; `embed/gene_vectors.npy` [11512]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11512 or target_col == 11512). Every well: [[POU6F1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/POU6F1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
