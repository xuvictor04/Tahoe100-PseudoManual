---
symbol: "TBL3"
type: "gene"
col: 11448
ensembl_id: "ENSG00000183751"
name: "transducin beta like 3"
location: "16p13.3"
module: 1
arm: "+"
pooled_cpm: 7.49
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 0
n_dd_up_clean: 12
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# TBL3

*transducin beta like 3* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (11 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.77× (z +11.3, q 9e-27, up in 34 of 43 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM in 1 line (MIA PaCa-2 0.0800×); [[Topotecan (hydrochloride) (drug)]] 0.05 µM in 1 line (HOP62 0.109×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WDR46]] (+0.77, fdr 7e-06), [[IPO4]] (+0.72, fdr 7e-06), [[NOP9]] (+0.72, fdr 7e-06); moves opposite to [[UQCRB]] (-0.62, fdr 7e-06, ⚠ UQCRB in the vector space only through flagged drug-doses), [[GABARAPL2]] (-0.61, fdr 7e-06), [[EIF1B]] (-0.60, fdr 1e-05), [[COX17]] (-0.57, fdr 1e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 11 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11448.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.77×** | +11.3 | 9e-27 | 34/43 (A549, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.86×** | +8.7 | 8e-16 | 37/47 (SW480, LS 180, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **1.84×** | +8.6 | 2e-15 | 17/30 (LoVo, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.79×** | +8.2 | 5e-14 | 32/46 (SW480, LOX-IMVI, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.74×** | +7.7 | 1e-12 | 29/47 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **1.75×** | +7.6 | 4e-12 | 12/13 (LOX-IMVI, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.70×** | +7.5 | 7e-12 | 26/47 (SW480, HEC-1-A, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **1.69×** | +7.1 | 9e-11 | 19/35 (NCI-H460, NCI-H1573, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **1.53×** | +5.5 | 3e-06 | 11/21 (NCI-H460, A498, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.46×** | +5.3 | 7e-06 | 13/36 (CFPAC-1, J82, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~9% here); position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.47×** | +5.1 | 1e-05 | 17/45 (RKO, NCI-H1792, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.42×** | +4.9 | 6e-05 | 16/43 (A-172, C-33 A, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.41×** | +4.8 | 7e-05 | 15/46 (SNU-423, HCT15, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.92×** | +4.8 | 7e-05 | 11/43 (MIA PaCa-2, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **1.84×** | +4.5 | 3e-04 | 15/46 (SW480, LS 180, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.32×** | +3.9 | 0.003 | 10/41 (NCI-H1792, SK-MEL-2, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.33×** | +3.7 | 0.006 | 9/44 (A498, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Imiquimod (hydrochloride) (drug)]] 0.05 µM |  | **1.30×** | +3.7 | 0.007 | 6/46 (J82, SNU-1, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.30×** | +3.6 | 0.010 | 12/45 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift; position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.20× | +3.5 | 0.011 | 12/48 (HOP62, PANC-1, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.55×** | +3.2 | 0.033 | 4/44 (PANC-1, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[venetoclax (drug)]] 5 µM |  | **1.53×** | +3.1 | 0.041 | 4/39 (NCI-H460, CFPAC-1, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11448.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM in 1 line (MIA PaCa-2 0.0800×); [[Topotecan (hydrochloride) (drug)]] 0.05 µM in 1 line (HOP62 0.109×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | 0.781× | -3.5 | 0.17 | 12/45 (H4, SW48, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.844× | -3.4 | 0.17 | 13/48 (A498, SW48, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | 0.786× | -3.3 | 0.19 | 12/45 (HS-578T, LoVo, …) | top dose only |  |
| [[18β-Glycyrrhetinic acid (drug)]] 5 µM |  | 0.861× | -3.0 | 0.31 | 11/46 (SNU-1, NCI-H1792, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.42 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11448. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 3.85 | 0 | 1 | — | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.109× (z -8.5) |
| [[MIA PaCa-2 (line)]] | alt | 6.28 | 0 | 1 | — | [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM 0.0800× (z -10.5) |
| [[A-172 (line)]] | wt | 7.49 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.23 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.89 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.79 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.44 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.60 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.23 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.07 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.71 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.66 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.90 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.61 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.49 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.72 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.03 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.00 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.76 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.55 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.07 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.76 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.10 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.29 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.96 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.59 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.08 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.24 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.27 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.92 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.83 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.91 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.68 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.19 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.83 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.27 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.68 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.32 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.59 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.80 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 8.28 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11448), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDR46]] | +0.77 | +0.71 / +0.76 | both halves | 7e-06 | same gene group; pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 999 |
| [[IPO4]] | +0.72 | +0.71 / +0.72 | both halves | 7e-06 | STRING 657 |
| [[NOP9]] | +0.72 | +0.69 / +0.71 | both halves | 7e-06 | STRING 861 |
| [[NOL6]] | +0.71 | +0.70 / +0.69 | both halves | 7e-06 | pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 999 |
| [[E2F4]] | +0.70 | +0.70 / +0.72 | both halves | 7e-06 |  |
| [[TOMM40]] | +0.70 | +0.65 / +0.70 | both halves | 7e-06 |  |
| [[ABCF2]] | +0.70 | +0.66 / +0.70 | both halves | 7e-06 | STRING 516 |
| [[DPH2]] | +0.69 | +0.70 / +0.64 | both halves | 7e-06 |  |
| [[PCNX3]] | +0.69 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[NOC2L]] | +0.68 | +0.69 / +0.67 | both halves | 7e-06 | STRING 985 |
| [[MFN2]] | +0.68 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[ATAD3A]] | +0.68 | +0.63 / +0.72 | both halves | 7e-06 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 4 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UQCRB]] ⚠ | -0.62 | -0.60 / -0.62 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[GABARAPL2]] | -0.61 | -0.60 / -0.62 | both halves | 7e-06 |  |
| [[EIF1B]] | -0.60 | -0.56 / -0.55 | both halves | 1e-05 |  |
| [[COX17]] | -0.57 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[RPL37A]] ⚠ | -0.57 | -0.58 / -0.54 | both halves | 1e-05 | pathway: Major pathway of rRNA processing in the nucleolus and cytosol; ⚠ in the vector space only through flagged drug-doses |
| [[RPS27A]] ⚠ | -0.56 | -0.53 / -0.56 | both halves | 1e-05 | pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 896; ⚠ in the vector space only through flagged drug-doses |
| [[ZCRB1]] | -0.56 | -0.46 / -0.64 | both halves | 2e-05 |  |
| [[UBE2B]] | -0.56 | -0.49 / -0.61 | both halves | 1e-05 |  |
| [[COX4I1]] ⚠ | -0.56 | -0.51 / -0.53 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.381). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-17.1, -32.6); signed map (-4.7, -44.4). **Vector** length 57.8, 7.71% of its response variance represented; |z| ≥ 3 in 906 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | +5.1 | +7.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | +4.9 | +8.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | +4.5 | +5.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.9 | +11.3 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +3.1 | +5.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.3 | +3.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.7 | +4.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.6 | +5.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.5 | +1.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.5 | +1.6 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.0 | -3.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -2.6 | -3.5 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -0.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | -0.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -1.6 | +0.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.6 | -1.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.4 | -0.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.4 | -2.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.4 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | transducin beta like 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:1,972,053-1,982,929 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SAZD, UTP13 |
| Gene groups (HGNC) | WD repeat domain containing; UTPb subcomplex |
| Reactome | 5 pathways, smallest: rRNA modification in the nucleus and cytosol; Major pathway of rRNA processing in the nucleolus and cytosol; rRNA processing in the nucleus and cytosol |
| Matched by | ensembl_id |

**Function**, from UniProt [Q12788](https://www.uniprot.org/uniprotkb/Q12788) (Transducin beta-like protein 3):

> Part of the small subunit (SSU) processome, first precursor of the small eukaryotic ribosomal subunit. During the assembly of the SSU processome in the nucleolus, many ribosome biogenesis factors, an RNA chaperone and ribosomal proteins associate with the nascent pre-rRNA and work in concert to generate RNA folding, modifications, rearrangements and cleavage as well as targeted degradation of pre-ribosomal RNA by the RNA exosome.

**Summary**, from NCBI Gene [10607](https://www.ncbi.nlm.nih.gov/gene/10607):

> The protein encoded by this gene has sequence similarity with members of the WD40 repeat-containing protein family. The WD40 group is a large family of proteins, which appear to have a regulatory function. It is believed that the WD40 repeats mediate protein-protein interactions and members of the family are involved in signal transduction, RNA processing, gene regulation, vesicular trafficking, cytoskeletal assembly and may play a role in the control of cytotypic differentiation. This gene has …

**Accessions** — [HGNC:11587](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11587) · Entrez [10607](https://www.ncbi.nlm.nih.gov/gene/10607) · UniProt [Q12788](https://www.uniprot.org/uniprotkb/Q12788) · Ensembl [ENSG00000183751](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183751)

## Data

Gene col 11448: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11448); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11448, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11448]; `tensor/DDL_lfc|DDL_z.npy` [11448]; `embed/gene_vectors.npy` [11448]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11448 or target_col == 11448). Every well: [[TBL3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TBL3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
