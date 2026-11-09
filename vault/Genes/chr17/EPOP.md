---
symbol: "EPOP"
type: "gene"
col: 15791
ensembl_id: "ENSG00000273604"
name: "elongin BC and polycomb repressive complex 2 associated protein"
location: "17q12"
module: 57
arm: "-"
pooled_cpm: 5.24
n_lines_expressing: 47
n_dd_up: 24
n_dd_down: 1
n_dd_up_clean: 16
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/057"]
generated_by: "tahoemap"
---

# EPOP

*elongin BC and polycomb repressive complex 2 associated protein* — 17q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.43× (z +13.7, q 9e-40, up in 28 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Verteporfin (drug)]] 5 µM: 0.678× (z -4.1, q 0.023, down in 15 of 37 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (A498 0.0978×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Neratinib (maleate) (drug)]] 0.5 µM in 1 line (BT-474 0.211×; ⚠ cell-cycle shift, would explain all of this change); [[Afatinib (drug)]] 5 µM in 1 line (BT-474 0.265×); [[Neratinib (drug)]] 5 µM in 1 line (SW48 0.0503×); [[Pexidartinib (hydrochloride) (drug)]] 5 µM in 1 line (SW1417 0.0552×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TLNRD1]] (+0.62, fdr 1e-05), [[ZNF347]] (+0.61, fdr 3e-05), [[PRR7]] (+0.58, fdr 1e-05); moves opposite to [[SCP2]] (-0.63, fdr 1e-05), [[ATP5F1C]] (-0.60, fdr 2e-05), [[LINC03006-1]] (-0.57, fdr 3e-05).
> It sits in the **-** arm of [[Module 057]] (Peroxisomal protein import).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[SRCIN1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15791.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.43×** | +13.7 | 9e-40 | 28/39 (CFPAC-1, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.31×** | +12.9 | 2e-35 | 26/35 (A549, BT-474, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **2.18×** | +8.5 | 4e-15 | 22/42 (HT-29, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **2.07×** | +7.6 | 5e-12 | 23/41 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.00×** | +7.5 | 6e-12 | 25/42 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.99×** | +7.5 | 6e-12 | 18/35 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.88×** | +6.9 | 6e-10 | 23/44 (HT-29, A-172, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.85×** | +6.4 | 9e-09 | 10/22 (MIA PaCa-2, BT-474, …) | rises with dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.67×** | +5.6 | 2e-06 | 14/26 (NCI-H2030, A498, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~23% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.52×** | +4.5 | 3e-04 | 15/44 (HT-29, CFPAC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.52×** | +4.2 | 0.001 | 9/32 (A549, MIA PaCa-2, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.30×** | +4.0 | 0.003 | 13/42 (HT-29, SK-MEL-2, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.44×** | +3.9 | 0.004 | 8/44 (HT-29, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[vincristine (drug)]] 0.5 µM |  | **1.61×** | +3.7 | 0.010 | 2/36 (MIA PaCa-2, Panc 03.27) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.39×** | +3.6 | 0.012 | 10/37 (J82, HT-29, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.26×** | +3.5 | 0.018 | 11/43 (MIA PaCa-2, NCI-H2347, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.36×** | +3.3 | 0.027 | 9/39 (MIA PaCa-2, A549, …) | all doses, stronger at high dose | position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.37×** | +3.3 | 0.032 | 8/42 (NCI-H2030, SNU-423, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.35×** | +3.2 | 0.039 | 11/40 (NCI-H460, MIA PaCa-2, …) | top dose only |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.67×** | +2.9 | 0.096 | 2/31 (CFPAC-1, NCI-H2030) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15791.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (A498 0.0978×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Neratinib (maleate) (drug)]] 0.5 µM in 1 line (BT-474 0.211×; ⚠ cell-cycle shift, would explain all of this change); [[Afatinib (drug)]] 5 µM in 1 line (BT-474 0.265×); [[Neratinib (drug)]] 5 µM in 1 line (SW48 0.0503×); [[Pexidartinib (hydrochloride) (drug)]] 5 µM in 1 line (SW1417 0.0552×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Verteporfin (drug)]] 5 µM |  | **0.678×** | -4.1 | 0.023 | 15/37 (BT-474, HepG2/C3A, …) | rises with dose | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.724× | -3.5 | 0.11 | 15/42 (SW480, SK-MEL-2, …) | two highest doses |  |
| [[TAK-901 (drug)]] 5 µM |  | 0.554× | -3.4 | 0.12 | 9/39 (A-427, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Pentagastrin (drug)]] 5 µM |  | 0.808× | -3.3 | 0.12 | 7/44 (SW 1271, MIA PaCa-2, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | 0.814× | -3.2 | 0.15 | 9/41 (MIA PaCa-2, A-427, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | 0.582× | -3.1 | 0.17 | 4/40 (BT-474, SK-MEL-2, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~36% of this change | 0.743× | -3.1 | 0.17 | 12/38 (PANC-1, BT-474, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.37 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15791. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 44.7 | 1 | 5 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.96× (z +10.0) | [[Neratinib (maleate) (drug)]] 0.5 µM 0.211× (z -10.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Afatinib (drug)]] 5 µM 0.265× (z -9.9) |
| [[PANC-1 (line)]] | alt | 5.41 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.25× (z +10.9) | [[Bortezomib (drug)]] 0.05 µM 0.170× (z -9.0) ⚠ cell-cycle shift, explains ~36% of this change |
| [[NCI-H1573 (line)]] | alt | 3.13 | 3 | 0 | [[Harringtonine (drug)]] 5 µM 27.1× (z +10.5) | — |
| [[A498 (line)]] | wt | 4.28 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0978× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.150× (z -8.5) |
| [[A549 (line)]] | wt | 5.31 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.34× (z +10.9) | — |
| [[CFPAC-1 (line)]] | alt | 3.54 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.2× (z +11.6) | — |
| [[A-172 (line)]] | wt | 2.52 | 0 | 1 | — | [[Brimonidine (drug)]] 0.05 µM 0.0640× (z -8.5) |
| [[HepG2_C3A (line)]] | wt | 9.57 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.89× (z +9.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 8.90 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 7.09× (z +8.6) | — |
| [[NCI-H460 (line)]] | wt | 3.83 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.79× (z +8.6) | — |
| [[SW1417 (line)]] | alt | 3.72 | 0 | 1 | — | [[Pexidartinib (hydrochloride) (drug)]] 5 µM 0.0552× (z -9.2) |
| [[SW48 (line)]] | wt | 9.36 | 0 | 1 | — | [[Neratinib (drug)]] 5 µM 0.0503× (z -9.3) |
| [[A-427 (line)]] | wt | 9.27 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.48 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.93 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.90 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.42 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.79 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.42 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.714 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 5.88 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.431 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 7.38 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.03 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.59 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.34 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.47 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.30 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.66 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.09 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.27 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.22 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15791), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*51 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TLNRD1]] | +0.62 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[ZNF347]] | +0.61 | +0.60 / +0.46 | both halves | 3e-05 |  |
| [[PRR7]] | +0.58 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[NTMT1]] | +0.58 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[CCDC71L]] | +0.57 | +0.47 / +0.61 | both halves | 2e-05 |  |
| [[S1PR2]] | +0.56 | +0.58 / +0.44 | both halves | 3e-05 |  |
| [[KHNYN]] | +0.56 | +0.55 / +0.43 | both halves | 3e-05 |  |
| [[INTS5]] | +0.55 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[PPRC1]] | +0.55 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[TP53RK]] | +0.55 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[FBXL6]] | +0.54 | +0.59 / +0.46 | both halves | 2e-05 |  |
| [[GEMIN4]] | +0.54 | +0.42 / +0.56 | both halves | 4e-05 |  |

## Genes that move opposite

*49 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SCP2]] | -0.63 | -0.56 / -0.61 | both halves | 1e-05 |  |
| [[ATP5F1C]] | -0.60 | -0.63 / -0.46 | both halves | 2e-05 |  |
| [[LINC03006-1]] | -0.57 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[ARL6IP5]] | -0.57 | -0.56 / -0.49 | both halves | 1e-05 |  |
| [[CROT]] | -0.57 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[ASAH1]] | -0.56 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[ATF6B]] | -0.55 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[TENT2]] | -0.54 | -0.60 / -0.51 | both halves | 1e-05 |  |
| [[PECR]] | -0.54 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[ATP6V1A]] | -0.54 | -0.35 / -0.51 | both halves | 1e-04 |  |
| [[ERGIC3]] | -0.54 | -0.51 / -0.46 | both halves | 3e-05 |  |
| [[UBE4B]] | -0.53 | -0.58 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SRCIN1]] | B | SRCIN1 activity raises EPOP's level | lines that do not express SRCIN1 (9) vs lines expressing it (41) | 1.98× lower at baseline in the lines without SRCIN1 | 0.038 | ⚠ within organs, on part of the lines; also absent: TSPAN33, PRKN |
| [[GABBR1]] | B | GABBR1 activity raises EPOP's level | lines that do not express GABBR1 (7) vs lines expressing it (43) | 1.81× lower at baseline in the lines without GABBR1 | 0.060 | ⚠ within organs, on part of the lines; also absent: BLVRA, TUBA1A, CABYR |
| [[IKZF3]] | B | IKZF3 activity raises EPOP's level | lines that do not express IKZF3 (31) vs lines expressing it (19) | 1.43× lower at baseline in the lines without IKZF3 | 0.079 | ⚠ within organs, on part of the lines; also absent: SLC34A2, ENSG00000244468, ENSG00000255026; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 057]] — Peroxisomal protein import; 86 genes; this gene is in the **-** arm (projection on the module's main direction -0.583). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-3.3, -6.9); signed map (9.3, 23.1). **Vector** length 60.5, 8.89% of its response variance represented; |z| ≥ 3 in 978 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +4.6 | +13.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.6 | +7.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.6 | +7.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +3.1 | +7.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.8 | +12.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.8 | +4.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.6 | +3.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.3 | +2.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.2 | +2.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.1 | +4.2 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | -2.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.7 | -3.5 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~36% of this change | -2.6 | -3.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.6 | -2.0 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | -2.7 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.2 | -3.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.3 | -0.8 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | -1.3 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | elongin BC and polycomb repressive complex 2 associated protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q12 — chr17:38,671,703-38,674,957 (-) |
| Ensembl biotype | protein_coding |
| Also known as | LOC100170841, PRR28; previously C17orf96 |
| Reactome | 2 pathways, smallest: PRC2 methylates histones and DNA; Epigenetic regulation of gene expression |
| Matched by | ensembl_id |

**Function**, from UniProt [A6NHQ4](https://www.uniprot.org/uniprotkb/A6NHQ4) (Elongin BC and Polycomb repressive complex 2-associated protein):

> Scaffold protein that serves as a bridging partner between the PRC2/EZH2 complex and the elongin BC complex: required to fine-tune the transcriptional status of Polycomb group (PcG) target genes in embryonic stem cells (ESCs). Plays a key role in genomic regions that display both active and repressive chromatin properties in pluripotent stem cells by sustaining low level expression at PcG target genes: acts by recruiting the elongin BC complex, thereby restricting excessive activity of the …

**Summary**, from NCBI Gene [100170841](https://www.ncbi.nlm.nih.gov/gene/100170841):

> Predicted to enable chromatin binding activity. Predicted to be involved in neuron fate commitment; regulation of transcription by RNA polymerase II; and stem cell differentiation. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:34493](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:34493) · Entrez [100170841](https://www.ncbi.nlm.nih.gov/gene/100170841) · UniProt [A6NHQ4](https://www.uniprot.org/uniprotkb/A6NHQ4) · Ensembl [ENSG00000273604](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000273604)

## Data

Gene col 15791: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15791); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15791, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15791]; `tensor/DDL_lfc|DDL_z.npy` [15791]; `embed/gene_vectors.npy` [15791]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15791 or target_col == 15791). Every well: [[EPOP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EPOP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
