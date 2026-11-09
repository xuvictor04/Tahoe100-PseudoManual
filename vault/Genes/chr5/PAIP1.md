---
symbol: "PAIP1"
type: "gene"
col: 10227
ensembl_id: "ENSG00000172239"
name: "poly(A) binding protein interacting protein 1"
location: "5p12"
module: 28
arm: "+"
pooled_cpm: 69.08
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 6
n_dd_up_clean: 1
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# PAIP1

*poly(A) binding protein interacting protein 1* — 5p12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.80× (z +12.2, q 2e-31, up in 36 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 0.05 µM: 1.20× (z +3.8, q 0.010, up in 20 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (NCI-H1792 3.58×, HOP62 2.68×, PANC-1 2.26×, A549 2.53×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (A549 3.23×, J82 2.42×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (SK-MEL-2 3.67×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.558× (z -12.1, q 8e-31, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZFR]] (+0.66, fdr 1e-05), [[SETD2]] (+0.66, fdr 1e-05), [[FBXO9]] (+0.65, fdr 2e-05); moves opposite to [[TRIOBP]] (-0.62, fdr 1e-05), [[PDE2A]] (-0.61, fdr 1e-05), [[ADGRL1-AS1]] (-0.60, fdr 7e-06).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[F3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 9 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10227.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (NCI-H1792 3.58×, HOP62 2.68×, PANC-1 2.26×, A549 2.53×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (A549 3.23×, J82 2.42×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (SK-MEL-2 3.67×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.80×** | +12.2 | 2e-31 | 36/49 (NCI-H1792, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.65×** | +9.9 | 7e-21 | 33/43 (A549, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.32×** | +5.5 | 7e-06 | 29/47 (LoVo, COLO 205, …) | top dose only | cell-cycle shift (explains ~3% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~31% of this change | **1.28×** | +5.1 | 5e-05 | 29/48 (NCI-H23, C32, …) | all doses, flat | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.23×** | +4.1 | 0.006 | 23/45 (SK-MEL-2, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +4.0 | 0.006 | 13/48 (SNU-423, SK-MEL-2, …) | rises with dose | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.20×** | +3.8 | 0.010 | 20/48 (A549, LS 180, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | 1.19× | +3.5 | 0.028 | 19/48 (A549, NCI-H2030, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.18× | +3.4 | 0.042 | 16/48 (HepG2/C3A, C32, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 1.19× | +3.3 | 0.048 | 17/47 (A549, HEC-1-A, …) | inconsistent across doses | low cells (technical?) |
| [[Radotinib (drug)]] 5 µM |  | 1.12× | +3.2 | 0.063 | 8/48 (AsPC-1, C32, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.2 | 0.066 | 14/48 (A-172, A549, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.33×** | +3.1 | 0.091 | 14/47 (C32, PANC-1, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10227.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.558×** | -12.1 | 8e-31 | 43/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.578×** | -11.4 | 2e-27 | 45/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.856× | -11.0 | 8e-26 | 12/49 (NCI-H460, PANC-1, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM |  | **0.671×** | -8.3 | 2e-14 | 41/48 (SW480, C-33 A, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.701×** | -7.3 | 2e-11 | 34/48 (NCI-H23, SW 900, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.758×** | -5.7 | 9e-07 | 31/48 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | 0.834× | -5.3 | 1e-05 | 26/48 (SW480, BT-474, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.853× | -4.6 | 2e-04 | 22/48 (AN3 CA, NCI-H23, …) | top dose only | composition shift |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.843× | -3.5 | 0.026 | 18/48 (BT-474, SW480, …) | rises with dose |  |
| [[Tetracycline (hydrochloride) (drug)]] 5 µM |  | 0.841× | -3.4 | 0.033 | 15/49 (CFPAC-1, NCI-H2122, …) | top dose only | plate-row cell shift; position effect removed |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | 0.850× | -3.4 | 0.039 | 15/48 (C-33 A, HepG2/C3A, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.738×** | -3.3 | 0.047 | 15/48 (SK-MEL-2, SW480, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, +0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10227. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 71.4 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.287× (z -11.6) |
| [[SW480 (line)]] | alt | 84.8 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.347× (z -16.2) |
| [[MIA PaCa-2 (line)]] | alt | 82.3 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.403× (z -10.8) |
| [[NCI-H460 (line)]] | wt | 61.1 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.407× (z -12.0) |
| [[SW1417 (line)]] | alt | 91.1 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 1.97× (z +9.0) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.462× (z -10.2) |
| [[A549 (line)]] | wt | 62.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.23× (z +12.0) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 62.2 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.26× (z +10.1) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.489× (z -8.9) |
| [[A-427 (line)]] | wt | 97.4 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.492× (z -9.3) |
| [[AN3 CA (line)]] | alt | 125 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.329× (z -10.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 85.8 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.147× (z -9.9) ⚠ toxic |
| [[CHP-212 (line)]] | wt | 70.3 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.0819× (z -13.0) ⚠ cell-cycle shift, explains ~49% of this change |
| [[HepG2_C3A (line)]] | wt | 63.2 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.334× (z -9.0) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 46.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.68× (z +10.4) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 71.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.59× (z +9.4) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 80.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.42× (z +9.5) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 51.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.58× (z +11.0) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 99.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.540× (z -10.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 108 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.510× (z -9.5) |
| [[SK-MEL-2 (line)]] | alt | 25.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.67× (z +8.5) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 70.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.225× (z -11.9) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 65.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.57× (z +9.3) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 70.8 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.364× (z -8.5) |
| [[A-172 (line)]] | wt | 74.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 80.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 46.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 45.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 53.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 48.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 60.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 54.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 60.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 62.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 60.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 39.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 51.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 74.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 50.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 62.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 50.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 96.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 58.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 61.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 151 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 87.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 63.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 43.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 83.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 58.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 70.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 68.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10227), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZFR]] | +0.66 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[SETD2]] | +0.66 | +0.57 / +0.64 | both halves | 1e-05 |  |
| [[FBXO9]] | +0.65 | +0.71 / +0.48 | both halves | 2e-05 |  |
| [[TLK1]] | +0.65 | +0.48 / +0.68 | both halves | 2e-05 |  |
| [[TRUB1]] | +0.64 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[USP24]] | +0.64 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[CLPX]] | +0.64 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[SMARCE1]] | +0.63 | +0.54 / +0.70 | both halves | 1e-05 |  |
| [[FAM204A]] | +0.62 | +0.46 / +0.66 | both halves | 2e-05 |  |
| [[PYURF]] | +0.62 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[AASDHPPT]] | +0.62 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[ZNF428]] | +0.62 | +0.56 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRIOBP]] | -0.62 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[PDE2A]] | -0.61 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[ADGRL1-AS1]] | -0.60 | -0.58 / -0.59 | both halves | 7e-06 |  |
| [[LRRC8A]] | -0.60 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[KCNQ1OT1]] | -0.59 | -0.53 / -0.58 | both halves | 1e-05 |  |
| [[TTLL3]] | -0.59 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[DUSP5]] | -0.58 | -0.46 / -0.54 | both halves | 2e-05 |  |
| [[MYO9B]] | -0.58 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[ERCC1]] | -0.57 | -0.66 / -0.48 | both halves | 2e-05 |  |
| [[SEC16A]] | -0.57 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[MFSD2A]] | -0.56 | -0.47 / -0.57 | both halves | 2e-05 |  |
| [[TPT1-AS1]] | -0.56 | -0.55 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[F3]] | B | F3 activity lowers PAIP1's level | lines that do not express F3 (24) vs lines expressing it (26) | 1.19× higher at baseline in the lines without F3 | 0.049 | ⚠ within organs, on part of the lines; also absent: TLR2, KRT7, EDNRA |
| [[ST3GAL1]] | B | ST3GAL1 activity lowers PAIP1's level | lines that do not express ST3GAL1 (11) vs lines expressing it (39) | 1.31× higher at baseline in the lines without ST3GAL1 | 0.051 | ⚠ within organs, on part of the lines; also absent: IL1RAP, FBXO32, PLSCR2 |
| [[HDAC6]] | B | HDAC6 activity raises PAIP1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[LUCAT1]] | B | LUCAT1 activity lowers PAIP1's level | lines that do not express LUCAT1 (8) vs lines expressing it (42) | 1.28× higher at baseline in the lines without LUCAT1 | 0.063 | ⚠ within organs, on part of the lines; also absent: TBILA, C3orf52, SPAG16 |
| [[HRH1]] | B | HRH1 activity lowers PAIP1's level | lines that do not express HRH1 (10) vs lines expressing it (40) | 1.34× higher at baseline in the lines without HRH1 | 0.094 | ⚠ within organs, on part of the lines; also absent: PHLDA2, PLAUR, LRRK1; maybe low, not absent |
| [[ZBED3]] | C | ZBED3 activity raises PAIP1's level | lines that do not express ZBED3 (3) vs lines expressing it (47) | 1.53× lower at baseline in the lines without ZBED3 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: GPD1L, DBNDD1, CDON; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.545). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-20.6, 4.0); signed map (11.1, -34.7). **Vector** length 99.9, 25.8% of its response variance represented; |z| ≥ 3 in 779 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +7.5 | +4.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +5.1 | +3.4 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.6 | +3.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +3.4 | +1.0 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | +3.3 | +3.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.1 | +3.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.0 | +2.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.0 | +1.8 |
| fall | [[Auranofin (drug)]] 5 µM |  | -7.5 | -7.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.2 | -5.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -3.1 | -3.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | -3.0 | -12.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.8 | -11.4 |
|  | [[Thymol (drug)]] 0.5 µM |  | -2.1 | -1.4 |
|  | [[Vilanterol (drug)]] 0.5 µM |  | -2.0 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | poly(A) binding protein interacting protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5p12 — chr5:43,526,267-43,557,758 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | MIF4G domain containing proteins |
| Hallmark sets | UNFOLDED_PROTEIN_RESPONSE |
| Reactome | 6 pathways, smallest: Z-decay: degradation of maternal mRNAs by zygotically expressed factors; Deadenylation of mRNA; M-decay: degradation of maternal mRNAs by maternally stored factors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H074](https://www.uniprot.org/uniprotkb/Q9H074) (Polyadenylate-binding protein-interacting protein 1):

> Acts as a coactivator in the regulation of translation initiation of poly(A)-containing mRNAs. Its stimulatory activity on translation is mediated via its action on PABPC1. Competes with PAIP2 for binding to PABPC1. Its association with EIF4A and PABPC1 may potentiate contacts between mRNA termini. May also be involved in translationally coupled mRNA turnover. Implicated with other RNA-binding proteins in the cytoplasmic deadenylation/translational and decay interplay of the FOS mRNA mediated …

**Summary**, from NCBI Gene [10605](https://www.ncbi.nlm.nih.gov/gene/10605):

> The protein encoded by this gene interacts with poly(A)-binding protein and with the cap-binding complex eIF4A. It is involved in translational initiation and protein biosynthesis. Overexpression of this gene in COS7 cells stimulates translation. Alternative splicing occurs at this locus and three transcript variants encoding three distinct isoforms have been identified. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:16945](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16945) · Entrez [10605](https://www.ncbi.nlm.nih.gov/gene/10605) · UniProt [Q9H074](https://www.uniprot.org/uniprotkb/Q9H074) · Ensembl [ENSG00000172239](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172239)

## Data

Gene col 10227: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10227); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10227, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10227]; `tensor/DDL_lfc|DDL_z.npy` [10227]; `embed/gene_vectors.npy` [10227]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10227 or target_col == 10227). Every well: [[PAIP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PAIP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
