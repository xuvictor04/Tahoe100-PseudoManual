---
symbol: "EXOSC9"
type: "gene"
col: 4457
ensembl_id: "ENSG00000123737"
name: "exosome component 9"
location: "4q27"
module: 17
arm: "+"
pooled_cpm: 26.53
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 1
n_dd_up_clean: 11
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# EXOSC9

*exosome component 9* — 4q27

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (17 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 2.35× (z +12.3, q 8e-32, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.795× (z -4.7, q 0.001, down in 25 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (SHP-77 0.158×, C-33 A 0.243×, AsPC-1 0.144×, HEC-1-A 0.361×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (A-427 0.271×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SW48 0.285×).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GEMIN2]] (+0.71, fdr 7e-06), [[SAAL1]] (+0.68, fdr 7e-06), [[FAM133B]] (+0.65, fdr 9e-06); moves opposite to [[TMBIM6]] (-0.56, fdr 4e-05), [[SLC25A53]] (-0.56, fdr 1e-04), [[SWT1]] (-0.56, fdr 1e-05).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 18 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4457.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **2.35×** | +12.3 | 8e-32 | 44/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **2.31×** | +11.6 | 1e-28 | 43/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.05×** | +10.3 | 2e-22 | 43/47 (NCI-H2347, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.64×** | +10.1 | 1e-21 | 35/48 (A549, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | **1.70×** | +7.6 | 2e-12 | 30/46 (PANC-1, LoVo, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.69×** | +7.5 | 7e-12 | 39/48 (LoVo, CFPAC-1, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.69×** | +7.4 | 9e-12 | 36/48 (RPMI-7951, PANC-1, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~23% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **1.61×** | +6.8 | 9e-10 | 29/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.56×** | +6.4 | 9e-09 | 34/48 (PANC-1, C32, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **1.55×** | +6.2 | 2e-08 | 36/48 (LoVo, RKO, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | **1.53×** | +6.1 | 7e-08 | 37/48 (LoVo, NCI-H1573, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~61% of this change | **1.47×** | +5.3 | 6e-06 | 23/47 (NCI-H23, LoVo, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **1.41×** | +4.7 | 1e-04 | 21/45 (PANC-1, HOP62, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.42×** | +4.6 | 2e-04 | 25/47 (NCI-H460, A-427, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.33×** | +4.1 | 0.002 | 24/48 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.57×** | +3.4 | 0.018 | 18/48 (RPMI-7951, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.25×** | +3.2 | 0.034 | 20/48 (HCT15, SW480, …) | rises with dose |  |
| [[Sonidegib (drug)]] 0.5 µM |  | **1.35×** | +3.0 | 0.056 | 10/48 (HCT15, SNU-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.24×** | +2.9 | 0.078 | 14/48 (NCI-H1792, LoVo, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.32×** | +2.8 | 0.086 | 15/46 (SNU-1, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4457.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (SHP-77 0.158×, C-33 A 0.243×, AsPC-1 0.144×, HEC-1-A 0.361×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (A-427 0.271×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SW48 0.285×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.795×** | -4.7 | 0.001 | 25/48 (SW48, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.801× | -3.2 | 0.33 | 13/47 (H4, LS 180, …) | inconsistent across doses | low cells (technical?) |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~70% of this change | 0.803× | -3.0 | 0.33 | 14/48 (SW480, A498, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.46 per unit of S-phase module lfc, +0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4457. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 19.4 | 5 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.85× (z +9.9) ⚠ cell-cycle shift, explains ~69% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.61× (z +9.1) | — |
| [[NCI-H1573 (line)]] | alt | 21.7 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +9.8) ⚠ cell-cycle shift, explains ~59% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 3.71× (z +8.8) | — |
| [[A-427 (line)]] | wt | 40.8 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.271× (z -13.1) |
| [[A549 (line)]] | wt | 19.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +10.0) ⚠ cell-cycle shift, explains ~59% of this change | — |
| [[AsPC-1 (line)]] | alt | 15.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.144× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 56.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.243× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 41.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.361× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 39.3 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.90× (z +9.6) | — |
| [[NCI-H460 (line)]] | wt | 23.7 | 1 | 0 | [[Harringtonine (drug)]] 0.5 µM 3.07× (z +8.7) | — |
| [[SHP-77 (line)]] | alt | 54.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.158× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 23.4 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.104× (z -9.8) ⚠ toxic |
| [[SW1417 (line)]] | alt | 21.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.237× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW48 (line)]] | wt | 45.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.285× (z -11.0) |
| [[SW480 (line)]] | alt | 23.7 | 1 | 0 | [[Harringtonine (drug)]] 0.5 µM 2.58× (z +9.0) | — |
| [[A-172 (line)]] | wt | 26.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 35.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 47.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 24.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 29.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 21.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 43.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 76.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 45.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 38.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 24.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4457), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GEMIN2]] | +0.71 | +0.64 / +0.71 | both halves | 7e-06 |  |
| [[SAAL1]] | +0.68 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[FAM133B]] | +0.65 | +0.57 / +0.61 | both halves | 9e-06 |  |
| [[OBI1]] | +0.64 | +0.61 / +0.76 | both halves | 7e-06 |  |
| [[KBTBD6]] | +0.63 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[HPF1]] | +0.63 | +0.47 / +0.65 | both halves | 2e-05 |  |
| [[YEATS4]] | +0.63 | +0.55 / +0.68 | both halves | 1e-05 |  |
| [[PARP2]] | +0.62 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[MDM1]] | +0.62 | +0.50 / +0.66 | both halves | 1e-05 |  |
| [[BRIX1]] | +0.62 | +0.59 / +0.66 | both halves | 7e-06 | STRING 571 |
| [[KAT14]] | +0.62 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[RBL1]] | +0.61 | +0.40 / +0.70 | both halves | 5e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMBIM6]] | -0.56 | -0.41 / -0.68 | both halves | 4e-05 |  |
| [[SLC25A53]] | -0.56 | -0.34 / -0.61 | both halves | 1e-04 |  |
| [[SWT1]] | -0.56 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[RAB22A]] | -0.54 | -0.48 / -0.54 | both halves | 2e-05 |  |
| [[SMG1P6]] | -0.53 | -0.29 / -0.56 | both halves | 2e-04 |  |
| [[YPEL5]] | -0.52 | -0.46 / -0.47 | both halves | 2e-05 |  |
| [[APLP2]] | -0.52 | -0.50 / -0.57 | both halves | 1e-05 |  |
| [[ADGRE3]] | -0.52 | -0.33 / -0.45 | both halves | 1e-04 |  |
| [[ZFC3H1]] | -0.52 | -0.37 / -0.61 | both halves | 7e-05 | pathway: Nuclear RNA decay; STRING 948 |
| [[LINC02245]] | -0.51 | -0.10 / -0.53 | ⚠ one half (not replicated) | 0.003 |  |
| [[SNHG29]] | -0.51 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[LASP1]] | -0.51 | -0.36 / -0.53 | both halves | 9e-05 |  |
| [[GNAS]] | -0.51 | -0.41 / -0.48 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.600). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-25.8, -1.7); signed map (-22.7, -16.2). **Vector** length 81.8, 19.0% of its response variance represented; |z| ≥ 3 in 862 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +5.2 | +12.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.4 | +6.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +3.6 | +11.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.3 | +10.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.1 | +4.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.0 | +2.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.8 | +0.3 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.8 | -0.3 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.7 | -2.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.4 | -4.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.7 | +0.1 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -2.6 | +3.0 |
|  | [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.4 | -2.9 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.9 | -2.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.6 | -1.4 |
|  | [[AZD-8055 (drug)]] 0.5 µM |  | -1.6 | -1.9 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.6 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | exosome component 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q27 — chr4:121,801,318-121,817,021 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PM/Scl-75, Rrp45p, RRP45, p5, p6; previously PMSCL1 |
| Gene groups (HGNC) | Exosome complex |
| Hallmark sets | UNFOLDED_PROTEIN_RESPONSE |
| Reactome | 20 pathways, smallest: mRNA decay by 3' to 5' exoribonuclease; Butyrate Response Factor 1 (BRF1) binds and destabilizes mRNA; KSRP (KHSRP) binds and destabilizes mRNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q06265](https://www.uniprot.org/uniprotkb/Q06265) (Exosome complex component RRP45):

> Non-catalytic component of the RNA exosome complex which has 3'->5' exoribonuclease activity and participates in a multitude of cellular RNA processing and degradation events. In the nucleus, the RNA exosome complex is involved in proper maturation of stable RNA species such as rRNA, snRNA and snoRNA, in the elimination of RNA processing by-products and non-coding 'pervasive' transcripts, such as antisense RNA species and promoter-upstream transcripts (PROMPTs), and of mRNAs with processing …

**Summary**, from NCBI Gene [5393](https://www.ncbi.nlm.nih.gov/gene/5393):

> This gene encodes a component of the human exosome, a exoribonuclease complex which processes and degrades RNA in the nucleus and cytoplasm. This component may play a role in mRNA degradation and the polymyositis/scleroderma autoantigen complex. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Aug 2011]

**Accessions** — [HGNC:9137](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9137) · Entrez [5393](https://www.ncbi.nlm.nih.gov/gene/5393) · UniProt [Q06265](https://www.uniprot.org/uniprotkb/Q06265) · Ensembl [ENSG00000123737](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000123737)

## Data

Gene col 4457: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4457); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4457, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4457]; `tensor/DDL_lfc|DDL_z.npy` [4457]; `embed/gene_vectors.npy` [4457]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4457 or target_col == 4457). Every well: [[EXOSC9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EXOSC9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
