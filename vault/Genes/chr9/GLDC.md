---
symbol: "GLDC"
type: "gene"
col: 10929
ensembl_id: "ENSG00000178445"
name: "glycine decarboxylase"
location: "9p24.1"
module: 87
arm: "+"
pooled_cpm: 6.58
n_lines_expressing: 28
n_dd_up: 24
n_dd_down: 11
n_dd_up_clean: 10
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 8
direction_downstream: 1
tags: ["gene", "module/087"]
generated_by: "tahoemap"
---

# GLDC

*glycine decarboxylase* — 9p24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (14 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.63× (z +24.4, q 0e+00, up in 17 of 24 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Trametinib (drug)]] 5 µM: 0.612× (z -6.1, q 6e-07, down in 10 of 26 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM: 0.652× (z -5.7, q 3e-06, down in 12 of 26 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PTPRZ1]] (+0.63, fdr 7e-06), [[LINC01812]] (+0.63, fdr 1e-05), [[MIR3681HG]] (+0.62, fdr 7e-06); moves opposite to [[ENTPD3-AS1]] (-0.50, fdr 1e-04), [[LRRC27]] (-0.49, fdr 3e-05), [[C15orf40]] (-0.46, fdr 2e-04).
> It is in [[Module 087]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[ST6GAL1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 14 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10929.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.63×** | +24.4 | 0e+00 | 17/24 (A549, C-33 A, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **3.73×** | +17.6 | 0e+00 | 21/25 (A549, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **3.71×** | +17.5 | 0e+00 | 22/26 (A549, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **2.67×** | +13.1 | 4e-37 | 23/26 (A549, J82, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.62×** | +9.2 | 5e-18 | 10/24 (J82, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.94×** | +8.9 | 7e-17 | 19/26 (J82, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.95×** | +8.6 | 6e-16 | 12/25 (C-33 A, NCI-H460, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.92×** | +8.4 | 3e-15 | 10/21 (C-33 A, NCI-H460, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | **1.92×** | +8.1 | 4e-14 | 3/13 (A549, HepG2/C3A, …) | all doses, flat | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.52×** | +7.9 | 2e-13 | 15/25 (NCI-H460, J82, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change | **1.83×** | +7.8 | 3e-13 | 3/10 (A549, HepG2/C3A, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~85% of this change | **1.75×** | +7.5 | 3e-12 | 5/17 (A549, HepG2/C3A, …) | all doses, flat | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.48×** | +7.4 | 6e-12 | 10/26 (A-427, HEC-1-A, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.58×** | +6.1 | 5e-08 | 14/25 (A549, PANC-1, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.49×** | +5.4 | 3e-06 | 14/26 (A549, J82, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **2.14×** | +5.3 | 4e-06 | 7/21 (A549, SK-MEL-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.46×** | +5.1 | 1e-05 | 8/25 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.37×** | +4.2 | 7e-04 | 5/25 (NCI-H460, SNU-423, …) | top dose only |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.54×** | +4.1 | 1e-03 | 1/25 (PANC-1) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.63×** | +3.4 | 0.017 | 1/20 (A549) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 1 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10929.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.612×** | -6.1 | 6e-07 | 10/26 (C32, SK-MEL-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.652×** | -5.7 | 3e-06 | 12/26 (C32, SK-MEL-2, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.681×** | -4.8 | 4e-04 | 8/26 (C32, A-427, …) | all doses, flat |  |
| [[Bimiralisib (drug)]] 5 µM |  | **0.510×** | -4.7 | 4e-04 | 4/25 (MIA PaCa-2, A-427, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.701×** | -4.6 | 5e-04 | 11/25 (A-427, C32, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.803×** | -4.1 | 0.004 | 11/25 (C32, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.778×** | -4.0 | 0.006 | 10/25 (A-427, C32, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.744×** | -3.7 | 0.013 | 8/24 (A-427, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.792×** | -3.6 | 0.017 | 8/25 (C32, A-427, …) | all doses, flat | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **0.769×** | -3.5 | 0.024 | 4/26 (A-427, AN3 CA, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | 0.844× | -3.2 | 0.065 | 5/25 (C32, A-427, …) | top dose only |  |
| [[RMC-6236 (drug)]] 5 µM |  | **0.635×** | -3.2 | 0.076 | 3/25 (A-427, C32, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | 0.799× | -3.0 | 0.11 | 6/25 (A-427, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.78 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10929. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 22.0 | 0 | 5 (1 ⚠) | — | [[Vinblastine (sulfate) (drug)]] 5 µM 0.200× (z -10.8) |
| [[NCI-H460 (line)]] | wt | 3.08 | 5 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 25.6× (z +12.2) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 6.08× (z +9.6) | — |
| [[A549 (line)]] | wt | 27.8 | 4 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 9.16× (z +14.6) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.04× (z +10.4) | — |
| [[J82 (line)]] | alt | 8.42 | 4 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 9.66× (z +10.7) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 3.66× (z +8.7) | — |
| [[NCI-H2030 (line)]] | alt | 14.8 | 3 (3 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 9.07× (z +12.6) ⚠ cell-cycle shift, explains ~31% of this change | [[Dinaciclib (drug)]] 5 µM 0.146× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change |
| [[C-33 A (line)]] | alt | 44.4 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.56× (z +9.9) | [[Dinaciclib (drug)]] 0.05 µM 0.190× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change |
| [[HEC-1-A (line)]] | alt | 8.32 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.43× (z +9.7) | — |
| [[A-427 (line)]] | wt | 48.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.210× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change |
| [[CFPAC-1 (line)]] | alt | 5.04 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 12.0× (z +9.4) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[HepG2_C3A (line)]] | wt | 34.9 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 6.93× (z +10.4) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[NCI-H23 (line)]] | alt | 10.6 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.111× (z -9.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.238× (z -9.0) |
| [[PANC-1 (line)]] | alt | 9.50 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.24× (z +11.1) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[A-172 (line)]] | wt | 2.96 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.3× (z +9.3) | — |
| [[AN3 CA (line)]] | alt | 84.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -10.2) |
| [[MIA PaCa-2 (line)]] | alt | 7.49 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.238× (z -17.8) ⚠ position not correctable |
| [[A498 (line)]] | wt | 1.03 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.812 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.894 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.766 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.33 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.19 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.35 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.38 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.63 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.890 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.24 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.745 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.906 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.28 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.99 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.08 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.20 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.875 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.31 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.37 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.36 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.64 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.44 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.846 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.42 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 4.91 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.793 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.60 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.861 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10929), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTPRZ1]] | +0.63 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[LINC01812]] | +0.63 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[MIR3681HG]] | +0.62 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[MED12L]] | +0.60 | +0.57 / +0.60 | both halves | 9e-06 |  |
| [[TRIM9]] | +0.60 | +0.51 / +0.64 | both halves | 1e-05 |  |
| [[GALNT18]] | +0.59 | +0.44 / +0.59 | both halves | 3e-05 |  |
| [[EFR3B]] | +0.59 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[SPRY4]] | +0.58 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[GNAO1]] | +0.58 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[LEF1-AS1]] | +0.57 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[TEX15]] | +0.57 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[LEF1]] | +0.56 | +0.49 / +0.63 | both halves | 1e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ENTPD3-AS1]] | -0.50 | -0.32 / -0.47 | both halves | 1e-04 |  |
| [[LRRC27]] | -0.49 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[C15orf40]] | -0.46 | -0.31 / -0.36 | both halves | 2e-04 |  |
| [[COPS5]] | -0.46 | -0.32 / -0.46 | both halves | 2e-04 |  |
| [[GABARAPL1]] | -0.46 | -0.36 / -0.44 | both halves | 1e-04 |  |
| [[XPA]] | -0.45 | -0.32 / -0.35 | both halves | 2e-04 |  |
| [[RNF115]] | -0.45 | -0.28 / -0.39 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 6, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers GLDC's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[STAMBPL1]] | B | STAMBPL1 activity lowers GLDC's level | lines that do not express STAMBPL1 (6) vs lines expressing it (44) | 6.52× higher at baseline in the lines without STAMBPL1 | 0.057 | ⚠ within organs, on part of the lines; also absent: CFAP45, PMAIP1, OCIAD2 |
| [[PLCXD1]] | B | PLCXD1 activity raises GLDC's level | lines that do not express PLCXD1 (11) vs lines expressing it (39) | 2.15× lower at baseline in the lines without PLCXD1 | 0.063 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[MAP2K2]] | B | MAP2K2 activity raises GLDC's level | compounds that target MAP2K2: 2 of 2 lower it (Binimetinib, Trametinib) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[ST6GAL1]] | B | ST6GAL1 activity raises GLDC's level | lines that do not express ST6GAL1 (14) vs lines expressing it (36) | 1.90× lower at baseline in the lines without ST6GAL1 | 0.088 | ⚠ within organs, on part of the lines; also absent: B4GALNT4, MYT1, ENSG00000290588; maybe low, not absent |
| [[PHF21B]] | B | PHF21B activity raises GLDC's level | lines that do not express PHF21B (21) vs lines expressing it (29) | 2.04× lower at baseline in the lines without PHF21B | 0.094 | ⚠ within organs, on part of the lines; also absent: JAM3, ADAM23, ADD2 |
| [[CACNA1H]] | C | CACNA1H activity raises GLDC's level | lines that do not express CACNA1H (23) vs lines expressing it (27) | 2.41× lower at baseline in the lines without CACNA1H | 0.044 | ⚠ within organs, on part of the lines; also absent: LHX2, LMX1B, JPH3; co-absent with the target |
| [[WT1]] | C | WT1 activity raises GLDC's level | lines that do not express WT1 (29) vs lines expressing it (21) | 1.89× lower at baseline in the lines without WT1 | 0.055 | ⚠ within organs, on part of the lines; also absent: WT1-AS, INA, ZNF677; co-absent with the target |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ST6GAL1]] | B | GLDC activity raises ST6GAL1's level | lines that do not express GLDC (22) vs lines expressing it (28) | 1.77× lower at baseline in the lines without GLDC | 0.090 | ⚠ within organs, on part of the lines; also absent: PRAME, LRRC63, ZFP82; maybe low, not absent |

## Where it sits

- **Module**: [[Module 087]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.561). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (54.2, 28.5); signed map (14.6, 48.4). **Vector** length 61.5, 13.3% of its response variance represented; |z| ≥ 3 in 710 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change | +3.9 | +7.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~85% of this change | +3.7 | +7.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.3 | +24.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | +3.2 | +8.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.0 | +7.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +7.4 |
|  | [[EX229 (drug)]] 5 µM |  | +1.5 | +5.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.3 | +2.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.2 | +2.8 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.9 | -4.8 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -2.9 | -6.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.5 | -5.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.3 | -4.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -2.2 | -4.6 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -2.1 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | glycine decarboxylase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p24.1 — chr9:6,532,467-6,645,729 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GCSP, NKH |
| Gene groups (HGNC) | Oxidoreductases |
| Hallmark sets | CHOLESTEROL_HOMEOSTASIS |
| Reactome | 3 pathways, smallest: Glycine degradation; Glyoxylate metabolism and glycine degradation; Metabolism of amino acids and derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [P23378](https://www.uniprot.org/uniprotkb/P23378) (Glycine dehydrogenase):

> The glycine cleavage system catalyzes the degradation of glycine. The P protein (GLDC) binds the alpha-amino group of glycine through its pyridoxal phosphate cofactor; CO(2) is released and the remaining methylamine moiety is then transferred to the lipoamide cofactor of the H protein (GCSH).

**Summary**, from NCBI Gene [2731](https://www.ncbi.nlm.nih.gov/gene/2731):

> Degradation of glycine is brought about by the glycine cleavage system, which is composed of four mitochondrial protein components: P protein (a pyridoxal phosphate-dependent glycine decarboxylase), H protein (a lipoic acid-containing protein), T protein (a tetrahydrofolate-requiring enzyme), and L protein (a lipoamide dehydrogenase). The protein encoded by this gene is the P protein, which binds to glycine and enables the methylamine group from glycine to be transferred to the T protein. …

**Accessions** — [HGNC:4313](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4313) · Entrez [2731](https://www.ncbi.nlm.nih.gov/gene/2731) · UniProt [P23378](https://www.uniprot.org/uniprotkb/P23378) · Ensembl [ENSG00000178445](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000178445)

## Data

Gene col 10929: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10929); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10929, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10929]; `tensor/DDL_lfc|DDL_z.npy` [10929]; `embed/gene_vectors.npy` [10929]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10929 or target_col == 10929). Every well: [[GLDC — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GLDC.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
