---
symbol: "OSBPL10"
type: "gene"
col: 6907
ensembl_id: "ENSG00000144645"
name: "oxysterol binding protein like 10"
location: "3p23"
module: 195
arm: "+"
pooled_cpm: 168.77
n_lines_expressing: 45
n_dd_up: 2
n_dd_down: 29
n_dd_up_clean: 2
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 14
direction_downstream: 7
tags: ["gene", "module/195"]
generated_by: "tahoemap"
---

# OSBPL10

*oxysterol binding protein like 10* — 3p23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.30× (z +7.4, q 6e-11, up in 24 of 43 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (BT-474 1.84×; ⚠ cell-cycle shift, explains ~36% of this change); [[Tucidinostat (drug)]] 5 µM in 1 line (RKO 2.32×).
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.713× (z -9.5, q 2e-18, down in 31 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF704]] (+0.63, fdr 7e-06), [[ITGA6]] (+0.63, fdr 7e-06), [[ETV4]] (+0.63, fdr 7e-06); moves opposite to [[BBOF1]] (-0.56, fdr 1e-05), [[LRRC27]] (-0.53, fdr 1e-05), [[TMUB2]] (-0.53, fdr 3e-05).
> It is in [[Module 195]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 14 arrows point to it, the strongest [[ZNF860]] → it (grade B ⚠); 7 go from it, the strongest it → [[ZNF860]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6907.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (BT-474 1.84×; ⚠ cell-cycle shift, explains ~36% of this change); [[Tucidinostat (drug)]] 5 µM in 1 line (RKO 2.32×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.30×** | +7.4 | 6e-11 | 24/43 (RKO, NCI-H2347, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.30×** | +5.3 | 4e-05 | 24/44 (RKO, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~2% of this change | 1.19× | +3.5 | 0.079 | 15/43 (NCI-H2347, NCI-H23, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.05× | +3.2 | 0.17 | 0/45 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6907.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.713×** | -9.5 | 2e-18 | 31/44 (SW1417, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.755×** | -6.3 | 1e-07 | 24/45 (NCI-H460, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.736×** | -6.1 | 2e-07 | 25/43 (C32, HEC-1-A, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **0.816×** | -5.7 | 2e-06 | 22/43 (SW48, Panc 03.27, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.821×** | -5.5 | 4e-06 | 23/43 (PANC-1, HepG2/C3A, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.753×** | -5.4 | 6e-06 | 24/43 (PANC-1, HepG2/C3A, …) | rises with dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~17% of this change | **0.762×** | -5.4 | 6e-06 | 26/43 (SW480, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.746×** | -5.4 | 6e-06 | 23/41 (AN3 CA, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.759×** | -5.2 | 1e-05 | 22/40 (C-33 A, SW48, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.769×** | -5.2 | 1e-05 | 28/43 (PANC-1, SW48, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.770×** | -5.2 | 1e-05 | 23/43 (C-33 A, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.771×** | -5.2 | 1e-05 | 25/43 (C-33 A, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.797×** | -5.1 | 2e-05 | 24/43 (C32, NCI-H1573, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **0.792×** | -4.6 | 2e-04 | 24/43 (C-33 A, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[venetoclax (drug)]] 5 µM |  | **0.642×** | -4.6 | 2e-04 | 24/43 (C32, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.758×** | -4.5 | 3e-04 | 23/44 (C32, NCI-H1573, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **0.833×** | -4.1 | 0.001 | 18/44 (C32, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.814×** | -4.1 | 0.002 | 22/43 (Panc 03.27, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.815×** | -3.9 | 0.003 | 21/43 (NCI-H1573, C32, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.825×** | -3.6 | 0.007 | 18/42 (C32, SK-MEL-2, …) | all doses, flat |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.720×** | -3.4 | 0.017 | 16/43 (C32, NCI-H1792, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6907. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 324 | 0 | 16 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.285× (z -16.9) |
| [[C-33 A (line)]] | alt | 550 | 0 | 9 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.155× (z -16.4) |
| [[HEC-1-A (line)]] | alt | 648 | 0 | 8 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.355× (z -18.9) |
| [[SW48 (line)]] | wt | 500 | 0 | 8 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.272× (z -17.9) |
| [[SK-MEL-2 (line)]] | alt | 285 | 0 | 6 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.343× (z -13.3) |
| [[SW480 (line)]] | alt | 268 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.331× (z -16.0) |
| [[HepG2_C3A (line)]] | wt | 364 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.275× (z -15.1) |
| [[KATO III (line)]] | alt | 289 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.314× (z -14.3) |
| [[HT-29 (line)]] | alt | 295 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.334× (z -14.4) |
| [[PANC-1 (line)]] | alt | 164 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.388× (z -16.4) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.446× (z -14.0) |
| [[SW1417 (line)]] | alt | 556 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.297× (z -20.9) |
| [[A-427 (line)]] | wt | 79.4 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.466× (z -10.7) ⚠ cell-cycle shift, explains ~36% of this change |
| [[BT-474 (line)]] | alt | 137 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +9.5) ⚠ cell-cycle shift, explains ~36% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.576× (z -8.7) |
| [[HCT15 (line)]] | alt | 187 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.358× (z -10.4) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 297 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.481× (z -9.0) |
| [[LOX-IMVI (line)]] | wt | 105 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.417× (z -12.5) ⚠ cell-cycle shift, explains ~36% of this change |
| [[Panc 03.27 (line)]] | alt | 198 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.577× (z -9.1) |
| [[A549 (line)]] | wt | 92.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.462× (z -10.1) ⚠ cell-cycle shift, explains ~36% of this change |
| [[AN3 CA (line)]] | alt | 240 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.143× (z -13.3) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 129 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.514× (z -11.2) |
| [[CHP-212 (line)]] | wt | 84.3 | 0 | 1 | — | [[Decitabine (drug)]] 0.05 µM 0.154× (z -8.9) |
| [[J82 (line)]] | alt | 95.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.355× (z -10.7) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 62.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.520× (z -9.0) ⚠ cell-cycle shift, explains ~36% of this change |
| [[NCI-H460 (line)]] | wt | 66.8 | 0 | 1 | — | [[Trametinib (drug)]] 5 µM 0.446× (z -9.4) |
| [[RKO (line)]] | wt | 49.8 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.32× (z +9.5) | — |
| [[SHP-77 (line)]] | alt | 88.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.263× (z -12.7) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 105 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 104 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 78.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 136 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 47.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 96.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 45.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 40.5 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 32.7 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 274 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 22.9 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 55.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 207 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 66.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 168 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 322 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 56.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 17.2 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 81.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 78.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.9 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 53.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6907), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF704]] | +0.63 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[ITGA6]] | +0.63 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[ETV4]] | +0.63 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[UBASH3B]] | +0.62 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[ZNF860]] | +0.60 | +0.53 / +0.64 | both halves | 1e-05 | STRING 543; ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[ASAP2]] | +0.59 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[RAPGEF5]] | +0.59 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[MYEOV]] | +0.59 | +0.50 / +0.64 | both halves | 1e-05 |  |
| [[STK39]] | +0.58 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[B4GALT6]] | +0.57 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[CTDSPL]] | +0.57 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[SH3TC2-DT]] | +0.57 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[PKP4]] | +0.57 | +0.52 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BBOF1]] | -0.56 | -0.60 / -0.52 | both halves | 1e-05 |  |
| [[LRRC27]] | -0.53 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[TMUB2]] | -0.53 | -0.46 / -0.47 | both halves | 3e-05 |  |
| [[OSCP1]] | -0.49 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[YJU2B]] | -0.48 | -0.53 / -0.35 | both halves | 1e-04 |  |
| [[TP53BP1]] | -0.48 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[SECISBP2L]] | -0.48 | -0.49 / -0.46 | both halves | 3e-05 |  |
| [[MMUT]] | -0.47 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[ZBTB3]] | -0.47 | -0.41 / -0.36 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 14, C 0. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF860]] | B | ZNF860 activity raises OSBPL10's level | lines that do not express ZNF860 (16) vs lines expressing it (34) | 3.21× lower at baseline in the lines without ZNF860 | 4e-04 | ⚠ within organs, on part of the lines; also absent: CRYBG2, IL18, TMC4 |
| [[PRAG1]] | B | PRAG1 activity raises OSBPL10's level | lines that do not express PRAG1 (16) vs lines expressing it (34) | 1.71× lower at baseline in the lines without PRAG1 | 0.007 | ⚠ within organs, on part of the lines; also absent: ANO9, EPS8L2, PDGFB; maybe low, not absent |
| [[ONECUT3]] | B | ONECUT3 activity raises OSBPL10's level | lines that do not express ONECUT3 (37) vs lines expressing it (13) | 2.10× lower at baseline in the lines without ONECUT3 | 0.015 | ⚠ within organs, on part of the lines; also absent: KLK7, KLK11, SLC6A20 |
| [[ARHGAP8]] | B | ARHGAP8 activity raises OSBPL10's level | lines that do not express ARHGAP8 (22) vs lines expressing it (28) | 1.86× lower at baseline in the lines without ARHGAP8 | 0.017 | ⚠ within organs, on part of the lines; also absent: AP1M2, SPINT2, FUT3 |
| [[ZNF860]] | B | ZNF860 activity strengthens OSBPL10's drug response | lines that do not express ZNF860 (11) vs lines expressing it (34) | the lines without ZNF860 respond 0.58× as strongly (z diff +1.61); strongest at Idarubicin (hydrochloride) 5 µM: 0.90x vs 0.56x (z diff +5.7) | 0.020 | ⚠ within organs, on part of the lines; also absent: CRYBG2, IL18, TMC4; target measured in part of the lines; artifact flags |
| [[MAP2K1]] | B | MAP2K1 activity raises OSBPL10's level | compounds that target MAP2K1: 4 of 4 lower it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 5.6% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CEACAM1]] | B | CEACAM1 activity raises OSBPL10's level | lines that do not express CEACAM1 (27) vs lines expressing it (23) | 1.88× lower at baseline in the lines without CEACAM1 | 0.021 | ⚠ within organs, on part of the lines; also absent: TOX3, FOXQ1, TRIM29 |
| [[RBP1]] | B | RBP1 activity raises OSBPL10's level | lines that do not express RBP1 (37) vs lines expressing it (13) | 1.95× lower at baseline in the lines without RBP1 | 0.034 | ⚠ within organs, on part of the lines; also absent: ENSG00000232252, ENSG00000260573, LGR5 |
| [[KIAA0040]] | B | KIAA0040 activity raises OSBPL10's level | lines that do not express KIAA0040 (24) vs lines expressing it (26) | 2.01× lower at baseline in the lines without KIAA0040 | 0.036 | ⚠ within organs, on part of the lines; also absent: ENSG00000226281, CLDN3, ESRP1 |
| [[LAMA3]] | B | LAMA3 activity raises OSBPL10's level | lines that do not express LAMA3 (22) vs lines expressing it (28) | 1.98× lower at baseline in the lines without LAMA3 | 0.038 | ⚠ within organs, on part of the lines; also absent: P2RY2, ELF3, MYO5B |
| [[B3GNT3]] | B | B3GNT3 activity raises OSBPL10's level | lines that do not express B3GNT3 (31) vs lines expressing it (19) | 2.27× lower at baseline in the lines without B3GNT3 | 0.048 | ⚠ within organs, on part of the lines; also absent: CDH1, INAVA, SLC5A1 |
| [[SCEL]] | B | SCEL activity raises OSBPL10's level | lines that do not express SCEL (35) vs lines expressing it (15) | 1.86× lower at baseline in the lines without SCEL | 0.050 | ⚠ within organs, on part of the lines; also absent: FGFBP1, MUC4, DAPP1 |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 6, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF860]] | B | OSBPL10 activity raises ZNF860's level | lines that do not express OSBPL10 (5) vs lines expressing it (45) | 2.96× lower at baseline in the lines without OSBPL10 | 0.052 | ⚠ within organs, on part of the lines; also absent: MORC4, USP53, CTNNA3; maybe low, not absent |
| [[LINC01844]] | B | OSBPL10 activity lowers LINC01844's level | lines that do not express OSBPL10 (5) vs lines expressing it (45) | 2.93× higher at baseline in the lines without OSBPL10 | 0.072 | ⚠ within organs, on part of the lines; also absent: MORC4, USP53, CTNNA3; maybe low, not absent |
| [[SPRY4]] | B | OSBPL10 activity lowers SPRY4's level | lines that do not express OSBPL10 (5) vs lines expressing it (45) | 2.62× higher at baseline in the lines without OSBPL10 | 0.073 | ⚠ within organs, on part of the lines; also absent: MORC4, USP53, CTNNA3; maybe low, not absent |
| [[KIAA0040]] | B | OSBPL10 activity raises KIAA0040's level | lines that do not express OSBPL10 (5) vs lines expressing it (45) | 3.93× lower at baseline in the lines without OSBPL10 | 0.089 | ⚠ within organs, on part of the lines; also absent: MORC4, USP53, CTNNA3; maybe low, not absent |
| [[PLEKHA6]] | B | OSBPL10 activity raises PLEKHA6's level | lines that do not express OSBPL10 (5) vs lines expressing it (45) | 3.70× lower at baseline in the lines without OSBPL10 | 0.089 | ⚠ within organs, on part of the lines; also absent: MORC4, USP53, CTNNA3; maybe low, not absent |
| cells under [[Capivasertib (drug)]] 5 µM | B | OSBPL10 activity raises the cells' numbers under Capivasertib 5 µM (protects the cells) | lines that do not express OSBPL10 (5) vs lines expressing it (43) | the lines without OSBPL10: 0.78× the cells of the other lines | 0.090 | ⚠ within organs, on part of the lines; also absent: MORC4, USP53, CTNNA3; maybe low, not absent |
| cells under [[Ouabain (Octahydrate) (drug)]] 5 µM | C | OSBPL10's natural level raises the cells' numbers under Ouabain (Octahydrate) 5 µM (protects the cells) | OSBPL10's natural level across 43 lines (lineage-adjusted; a glimpse) | r +0.74 | 0.268 over the table, 0.021 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 195]]; 17 genes; every member is in the + arm (projection on the module's main direction 0.577). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (42.2, 4.7); signed map (4.0, 41.8). **Vector** length 115, 32.0% of its response variance represented; |z| ≥ 3 in 1,209 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.7 | +7.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.6 | +5.3 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~2% of this change | +4.5 | +3.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.2 | -3.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | +1.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.7 | +1.8 |
|  | [[Ipatasertib (drug)]] 5 µM |  | +2.3 | +2.8 |
|  | [[Bentamapimod (drug)]] 5 µM |  | +2.2 | +2.6 |
| fall | [[Trametinib (drug)]] 5 µM |  | -6.3 | -6.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -5.3 | -5.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -5.1 | -4.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -4.9 | -3.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | -4.7 | -4.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -4.5 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | oxysterol binding protein like 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p23 — chr3:31,657,912-32,077,580 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Oxysterol binding proteins; Pleckstrin homology domain containing |
| Reactome | 4 pathways, smallest: Acyl chain remodelling of PS; Glycerophospholipid biosynthesis; Phospholipid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BXB5](https://www.uniprot.org/uniprotkb/Q9BXB5) (Oxysterol-binding protein-related protein 10):

> Lipid transporter involved in lipid countertransport between the endoplasmic reticulum and the plasma membrane. Its ability to bind phosphatidylserine, suggests that it specifically exchanges phosphatidylserine with phosphatidylinositol 4-phosphate (PI4P), delivering phosphatidylserine to the plasma membrane in exchange for PI4P (Probable). Plays a role in negative regulation of lipid biosynthesis. Interacts with OSBPL9 to function as lipid transfer proteins. Together they form a heterodimer …

**Summary**, from NCBI Gene [114884](https://www.ncbi.nlm.nih.gov/gene/114884):

> This gene encodes a member of the oxysterol-binding protein (OSBP) family, a group of intracellular lipid receptors. Like most members, the encoded protein contains an N-terminal pleckstrin homology domain and a highly conserved C-terminal OSBP-like sterol-binding domain. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Mar 2010]

**Accessions** — [HGNC:16395](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16395) · Entrez [114884](https://www.ncbi.nlm.nih.gov/gene/114884) · UniProt [Q9BXB5](https://www.uniprot.org/uniprotkb/Q9BXB5) · Ensembl [ENSG00000144645](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000144645)

## Data

Gene col 6907: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6907); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6907, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6907]; `tensor/DDL_lfc|DDL_z.npy` [6907]; `embed/gene_vectors.npy` [6907]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6907 or target_col == 6907). Every well: [[OSBPL10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/OSBPL10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
