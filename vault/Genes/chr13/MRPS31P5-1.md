---
symbol: "MRPS31P5-1"
type: "gene"
col: 16543
ensembl_id: "ENSG00000291010"
name: ""
location: ""
module: 17
arm: "+"
pooled_cpm: 2.27
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 13
n_dd_up_clean: 8
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# MRPS31P5-1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.94× (z +6.4, q 9e-08, up in 16 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.510× (z -6.5, q 5e-08, down in 16 of 37 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRPS31P4]] (+0.78, fdr 7e-06), [[MED23]] (+0.68, fdr 7e-06), [[MINDY3]] (+0.68, fdr 9e-06); moves opposite to [[GPR137]] (-0.68, fdr 1e-05), [[AKT1S1]] (-0.66, fdr 1e-05), [[LINC00393]] (-0.65, fdr 2e-05).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PLEKHA6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 16543.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.94×** | +6.4 | 9e-08 | 16/46 (NCI-H1573, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.86×** | +6.0 | 4e-07 | 16/44 (NCI-H1573, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.55×** | +6.0 | 4e-07 | 9/45 (HEC-1-A, SNU-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~25% here); position effect removed |
| [[Radotinib (drug)]] 5 µM |  | **1.45×** | +5.1 | 4e-05 | 10/45 (AsPC-1, PANC-1, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.68×** | +4.8 | 1e-04 | 3/12 (HEC-1-A, Hs 766T, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.53×** | +4.1 | 0.003 | 4/44 (LoVo, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.55×** | +4.1 | 0.004 | 0/1 | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Triamcinolone (drug)]] 5 µM |  | **1.30×** | +3.6 | 0.020 | 2/45 (LOX-IMVI, PANC-1) | top dose only | position effect removed |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.43×** | +3.5 | 0.035 | 6/40 (A549, Hs 766T, …) | rises with dose | position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.96×** | +3.4 | 0.036 | 0/3 | top dose only | noisy plate (z scaled) |
| [[Ferulic acid (drug)]] 0.5 µM |  | **1.40×** | +3.3 | 0.055 | 3/38 (C32, CHP-212, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.26×** | +3.2 | 0.062 | 4/46 (C32, SHP-77, …) | top dose only | position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **1.37×** | +3.1 | 0.094 | 0/46 | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 16543.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.510×** | -6.5 | 5e-08 | 16/37 (SW480, A-427, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.675×** | -5.3 | 2e-05 | 21/31 (SW1417, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.750×** | -3.9 | 0.017 | 16/33 (COLO 205, A498, …) | inconsistent across doses | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.672×** | -3.8 | 0.019 | 7/46 (SW480, Hs 766T, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.683×** | -3.5 | 0.048 | 14/41 (AsPC-1, BT-474, …) | rises with dose | composition shift; position effect removed |
| [[Hydroxyurea (drug)]] 0.05 µM |  | **0.677×** | -3.5 | 0.048 | 5/20 (NCI-H2347, LOX-IMVI, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.701×** | -3.4 | 0.049 | 9/40 (HOP62, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.703×** | -3.4 | 0.049 | 12/43 (NCI-H460, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~23% here); position effect removed |
| [[5-Fluorouracil (drug)]] 0.5 µM |  | **0.715×** | -3.2 | 0.080 | 8/42 (HOP62, NCI-H2347, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.718×** | -3.2 | 0.083 | 9/44 (HepG2/C3A, KATO III, …) | rises with dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.722×** | -3.1 | 0.091 | 11/40 (Panc 03.27, SW480, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~36% of this change | **0.725×** | -3.1 | 0.091 | 8/12 (SW480, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.717×** | -3.1 | 0.091 | 12/32 (NCI-H460, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~6% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 16543. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 6.08 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.204× (z -9.5) |
| [[A498 (line)]] | wt | 2.64 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0886× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~98% of this change |
| [[A-172 (line)]] | wt | 1.66 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.09 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.72 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.829 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.16 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.04 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.33 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.80 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.05 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.97 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.37 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.51 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.55 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.19 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.869 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.67 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.35 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.56 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.51 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.02 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 16543), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPS31P4]] | +0.78 | +0.61 / +0.78 | both halves | 7e-06 |  |
| [[MED23]] | +0.68 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[MINDY3]] | +0.68 | +0.57 / +0.64 | both halves | 9e-06 |  |
| [[BRAT1]] | +0.67 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[LRIG2]] | +0.67 | +0.68 / +0.58 | both halves | 7e-06 |  |
| [[HEATR6]] | +0.67 | +0.69 / +0.50 | both halves | 1e-05 |  |
| [[ANAPC5]] | +0.67 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[UBXN2B]] | +0.67 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[PEX2]] | +0.65 | +0.64 / +0.57 | both halves | 1e-05 |  |
| [[TMEM185A]] | +0.65 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[CDADC1]] | +0.64 | +0.58 / +0.65 | both halves | 8e-06 |  |
| [[SDHB]] | +0.64 | +0.60 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPR137]] | -0.68 | -0.56 / -0.60 | both halves | 1e-05 |  |
| [[AKT1S1]] | -0.66 | -0.59 / -0.53 | both halves | 1e-05 |  |
| [[LINC00393]] | -0.65 | -0.56 / -0.47 | both halves | 2e-05 |  |
| [[MPDU1]] | -0.62 | -0.56 / -0.47 | both halves | 2e-05 |  |
| [[SLC6A13]] | -0.62 | -0.60 / -0.49 | both halves | 1e-05 |  |
| [[BOLA1]] | -0.62 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[GARIN1A]] | -0.62 | -0.61 / -0.48 | both halves | 2e-05 |  |
| [[MZF1-AS1]] | -0.62 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[TRIM69]] | -0.61 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[MEPCE]] | -0.61 | -0.59 / -0.45 | both halves | 3e-05 |  |
| [[PARD6G-AS1]] | -0.61 | -0.65 / -0.34 | both halves | 1e-04 |  |
| [[CCDC90B-AS1]] | -0.61 | -0.49 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLEKHA6]] | B | PLEKHA6 activity lowers MRPS31P5-1's level | lines that do not express PLEKHA6 (16) vs lines expressing it (34) | 1.09× higher at baseline in the lines without PLEKHA6 | 0.075 | ⚠ within organs, on part of the lines; also absent: KCNK1, ELF3, TNK1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.684). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-3.6, -10.6); signed map (-30.6, -11.9). **Vector** length 41.6, 4.28% of its response variance represented; |z| ≥ 3 in 1,060 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +1.6 | +6.0 |
|  | [[Belinostat (drug)]] 5 µM |  | +1.5 | +4.1 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | +1.5 | +3.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +1.5 | +6.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.2 | +5.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.1 | +3.1 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +0.9 | +1.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +0.9 | +1.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +0.8 | +1.7 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.4 | -5.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.2 | -6.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | -2.9 | -3.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.2 | -0.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | -1.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.2 | -1.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.1 | -2.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.0 | -3.1 |

## What is on record

> [!warning] No registry record
> MRPS31P5-1 has no HGNC entry matched to it: no approved name, no gene group, no cross-references. The quantification assigned reads to this identifier and that is what is known; nothing more is claimed.

## Data

Gene col 16543: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 16543); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 16543, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 16543]; `tensor/DDL_lfc|DDL_z.npy` [16543]; `embed/gene_vectors.npy` [16543]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 16543 or target_col == 16543). Every well: [[MRPS31P5-1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MRPS31P5-1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
