---
symbol: "DDX18"
type: "gene"
col: 1522
ensembl_id: "ENSG00000088205"
name: "DEAD-box helicase 18"
location: "2q14.1"
module: 1
arm: "+"
pooled_cpm: 129.74
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 0
n_dd_up_clean: 4
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# DDX18

*DEAD-box helicase 18* — 2q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.41× (z +10.0, q 9e-21, up in 48 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 1.68× (z +6.9, q 1e-09, up in 40 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Adagrasib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.738×; ⚠ position not correctable).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPF2]] (+0.70, fdr 7e-06), [[UTP14A]] (+0.69, fdr 7e-06), [[ZNF146]] (+0.66, fdr 7e-06); moves opposite to [[SEC61A2]] (-0.59, fdr 1e-05), [[RNF38]] (-0.58, fdr 3e-05), [[STRN]] (-0.57, fdr 7e-06).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 11 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1522.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **2.41×** | +10.0 | 9e-21 | 48/49 (NCI-H1792, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **2.11×** | +8.9 | 1e-16 | 43/44 (A-427, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **1.77×** | +6.9 | 7e-10 | 37/45 (HT-29, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.68×** | +6.9 | 1e-09 | 40/48 (NCI-H1573, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~22% here) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.45×** | +4.3 | 0.002 | 34/48 (NCI-H1573, LOX-IMVI, …) | two highest doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~66% of this change | **1.37×** | +4.1 | 0.003 | 36/48 (HOP62, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.72×** | +3.7 | 0.015 | 35/49 (NCI-H1573, A549, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.36×** | +3.6 | 0.020 | 31/47 (A-172, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.28×** | +3.3 | 0.061 | 32/48 (NCI-H23, C-33 A, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.28×** | +3.3 | 0.061 | 32/48 (NCI-H1792, MIA PaCa-2, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.59×** | +3.2 | 0.074 | 25/48 (KATO III, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.27×** | +3.2 | 0.074 | 28/48 (LOX-IMVI, A549, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.30×** | +3.1 | 0.082 | 23/48 (NCI-H1792, HOP62, …) | two highest doses | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.18× | +3.1 | 0.082 | 22/48 (NCI-H1573, NCI-H1792, …) | all doses, flat | composition shift |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | 1.17× | +3.0 | 0.10 | 17/48 (SK-MEL-2, KATO III, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1522.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Adagrasib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.738×; ⚠ position not correctable).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 0.05 µM |  | 0.825× | -3.5 | 0.28 | 27/48 (SW480, A-427, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, +0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1522. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 86.1 | 8 (7 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.21× (z +13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.11× (z +10.8) | — |
| [[NCI-H1573 (line)]] | alt | 136 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.55× (z +14.4) | — |
| [[A549 (line)]] | wt | 119 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.90× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.36× (z +8.5) | — |
| [[HT-29 (line)]] | alt | 104 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.33× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.41× (z +8.7) | — |
| [[SNU-423 (line)]] | alt | 87.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.11× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[A498 (line)]] | wt | 199 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.82× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[HOP62 (line)]] | alt | 94.4 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.07× (z +10.5) | — |
| [[Hs 766T (line)]] | wt | 85.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.67× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[LOX-IMVI (line)]] | wt | 116 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.80× (z +8.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 130 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.72× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[NCI-H2030 (line)]] | alt | 170 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.85× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[NCI-H460 (line)]] | wt | 113 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.26× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[SW480 (line)]] | alt | 160 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.60× (z +11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[A-172 (line)]] | wt | 81.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +10.1) ⚠ cell-cycle shift, would explain all of this change | — |
| [[A-427 (line)]] | wt | 126 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.96× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[CFPAC-1 (line)]] | alt | 111 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.54× (z +9.6) | — |
| [[COLO 205 (line)]] | alt | 83.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.20× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 94.4 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.96× (z +8.6) | — |
| [[KATO III (line)]] | alt | 108 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.76× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[NCI-H23 (line)]] | alt | 176 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.10× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[Panc 03.27 (line)]] | alt | 105 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.45× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[AN3 CA (line)]] | alt | 119 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 91.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 142 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 78.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 158 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 164 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 180 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 170 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 118 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 85.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 162 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 120 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 129 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 98.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 69.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 120 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 152 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 169 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 145 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 174 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 166 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 148 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 144 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 144 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 165 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 131 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1522), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPF2]] | +0.70 | +0.75 / +0.60 | both halves | 7e-06 | STRING 992 |
| [[UTP14A]] | +0.69 | +0.72 / +0.63 | both halves | 7e-06 | same gene group; STRING 923 |
| [[ZNF146]] | +0.66 | +0.75 / +0.60 | both halves | 7e-06 |  |
| [[GAR1]] | +0.65 | +0.66 / +0.61 | both halves | 7e-06 | STRING 626 |
| [[SDAD1]] | +0.65 | +0.67 / +0.64 | both halves | 7e-06 | STRING 854 |
| [[NCBP2]] | +0.65 | +0.69 / +0.55 | both halves | 1e-05 | pathway: HALLMARK_MYC_TARGETS_V1 |
| [[PNO1]] | +0.64 | +0.68 / +0.59 | both halves | 7e-06 | STRING 496 |
| [[GNL2]] | +0.64 | +0.60 / +0.67 | both halves | 7e-06 | STRING 975 |
| [[GTPBP4]] | +0.64 | +0.68 / +0.57 | both halves | 1e-05 | STRING 997 |
| [[CEBPZ]] | +0.63 | +0.78 / +0.55 | both halves | 1e-05 | STRING 958 |
| [[SCFD2]] | +0.62 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[PES1]] | +0.61 | +0.65 / +0.52 | both halves | 1e-05 | pathway: HALLMARK_MYC_TARGETS_V2; STRING 997 |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEC61A2]] | -0.59 | -0.60 / -0.53 | both halves | 1e-05 |  |
| [[RNF38]] | -0.58 | -0.68 / -0.43 | both halves | 3e-05 |  |
| [[STRN]] | -0.57 | -0.63 / -0.59 | both halves | 7e-06 |  |
| [[TWSG1]] | -0.55 | -0.60 / -0.58 | both halves | 8e-06 |  |
| [[ELMO2]] | -0.55 | -0.59 / -0.43 | both halves | 3e-05 |  |
| [[TRAF6]] | -0.54 | -0.56 / -0.49 | both halves | 1e-05 |  |
| [[HSF2]] | -0.53 | -0.46 / -0.50 | both halves | 2e-05 |  |
| [[MICA]] | -0.53 | -0.54 / -0.45 | both halves | 3e-05 |  |
| [[RUSC1]] | -0.53 | -0.62 / -0.40 | both halves | 4e-05 |  |
| [[ELL3]] | -0.53 | -0.55 / -0.44 | both halves | 3e-05 |  |
| [[HSPA1B]] | -0.53 | -0.55 / -0.43 | both halves | 3e-05 |  |
| [[LINC00847]] | -0.52 | -0.49 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.495). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-21.4, -41.0); signed map (0.7, -45.0). **Vector** length 89.1, 31.6% of its response variance represented; |z| ≥ 3 in 746 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.8 | +6.9 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | +5.0 | +3.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.4 | +3.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.8 | +3.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.8 | +3.2 |
|  | [[EX229 (drug)]] 5 µM |  | +2.3 | +2.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.7 | +2.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.6 | +2.8 |
| fall | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.2 | -0.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -4.0 | -0.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -3.4 | -1.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.1 | +1.8 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.0 | -1.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.2 | -1.6 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -2.2 | -3.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.1 | -2.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -2.1 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | DEAD-box helicase 18 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q14.1 — chr2:117,814,691-117,832,377 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MrDb, Has1 |
| Gene groups (HGNC) | DEAD-box helicases; SSU processome |
| Hallmark sets | MYC_TARGETS_V2, MYC_TARGETS_V1 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NVP1](https://www.uniprot.org/uniprotkb/Q9NVP1) (ATP-dependent RNA helicase DDX18):

> ATP-dependent RNA helicase that plays a role in the regulation of R-loop homeostasis in both endogenous R-loop-prone regions and at sites of DNA damage. At endogenous loci such as actively transcribed genes, may act as a helicase to resolve the formation of R-loop during transcription and prevent the interference of R-loop with DNA-replication machinery. Also participates in the removal of DNA-lesion-associated R-loop. Plays an essential role for establishing pluripotency during embryogenesis …

**Summary**, from NCBI Gene [8886](https://www.ncbi.nlm.nih.gov/gene/8886):

> DEAD box proteins, characterized by the conserved motif Asp-Glu-Ala-Asp (DEAD), are putative RNA helicases. They are implicated in a number of cellular processes involving alteration of RNA secondary structure such as translation initiation, nuclear and mitochondrial splicing, and ribosome and spliceosome assembly. Based on their distribution patterns, some members of this family are believed to be involved in embryogenesis, spermatogenesis, and cellular growth and division. This gene encodes a …

**Accessions** — [HGNC:2741](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2741) · Entrez [8886](https://www.ncbi.nlm.nih.gov/gene/8886) · UniProt [Q9NVP1](https://www.uniprot.org/uniprotkb/Q9NVP1) · Ensembl [ENSG00000088205](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000088205)

## Data

Gene col 1522: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1522); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1522, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1522]; `tensor/DDL_lfc|DDL_z.npy` [1522]; `embed/gene_vectors.npy` [1522]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1522 or target_col == 1522). Every well: [[DDX18 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DDX18.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
