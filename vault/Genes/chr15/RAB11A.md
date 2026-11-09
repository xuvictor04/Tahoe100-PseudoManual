---
symbol: "RAB11A"
type: "gene"
col: 2395
ensembl_id: "ENSG00000103769"
name: "RAB11A, member RAS oncogene family"
location: "15q22.31"
module: 5
arm: "-"
pooled_cpm: 79.74
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 0
n_dd_up_clean: 6
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# RAB11A

*RAB11A, member RAS oncogene family* — 15q22.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.84× (z +17.0, q 0e+00, up in 38 of 48 measured lines) ⚠ cell-cycle shift, explains ~34% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.34× (z +8.2, q 2e-14, up in 28 of 49 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Trametinib (drug)]] 5 µM in 1 line (NCI-H596 0.359×; ⚠ cell-cycle shift, explains ~45% of this change); [[Cabozantinib (S-malate) (drug)]] 0.05 µM in 1 line (SW 1088 0.0725×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPINT2]] (+0.59, fdr 3e-05), [[MAPK3]] (+0.56, fdr 2e-05), [[MMUT]] (+0.55, fdr 2e-05); moves opposite to [[MTHFD1L]] (-0.56, fdr 1e-05), [[ZBTB40]] (-0.56, fdr 2e-05), [[TANGO6]] (-0.56, fdr 3e-05).
> It sits in the **-** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ATP8B1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 12 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2395.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.84×** | +17.0 | 0e+00 | 38/48 (NCI-H460, NCI-H1573, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **1.83×** | +9.5 | 7e-19 | 39/49 (LoVo, SW480, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **1.60×** | +8.9 | 1e-16 | 35/44 (SW480, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +8.2 | 2e-14 | 28/49 (CFPAC-1, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.15×** | +7.9 | 3e-13 | 42/49 (PANC-1, NCI-H1573, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **1.44×** | +7.1 | 9e-11 | 37/48 (SNU-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.42×** | +6.9 | 3e-10 | 33/48 (SHP-77, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.11× | +6.5 | 4e-09 | 0/50 | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.35×** | +6.0 | 1e-07 | 29/48 (J82, A549, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **1.37×** | +5.7 | 6e-07 | 27/45 (PANC-1, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | **1.35×** | +5.7 | 8e-07 | 32/47 (PANC-1, NCI-H1573, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.33×** | +5.5 | 1e-06 | 34/48 (SK-MEL-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~58% of this change | **1.28×** | +4.8 | 7e-05 | 30/48 (NCI-H23, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **1.29×** | +4.8 | 8e-05 | 24/48 (PANC-1, NCI-H1573, …) | rises with dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.27×** | +4.5 | 2e-04 | 24/50 (NCI-H23, MIA PaCa-2, …) | top dose only |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.25×** | +3.1 | 0.063 | 15/48 (Panc 03.27, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2395.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Trametinib (drug)]] 5 µM in 1 line (NCI-H596 0.359×; ⚠ cell-cycle shift, explains ~45% of this change); [[Cabozantinib (S-malate) (drug)]] 0.05 µM in 1 line (SW 1088 0.0725×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Lidocaine (hydrochloride) (drug)]] 5 µM |  | 0.885× | -3.4 | 0.34 | 9/48 (NCI-H1792, SW480, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, +0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2395. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 70.4 | 8 (7 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.15× (z +26.8) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.92× (z +12.4) | — |
| [[NCI-H460 (line)]] | wt | 51.2 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.77× (z +29.1) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[HEC-1-A (line)]] | alt | 72.8 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +19.0) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[NCI-H23 (line)]] | alt | 60.9 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +11.4) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[A-172 (line)]] | wt | 74.8 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.94× (z +23.0) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[CFPAC-1 (line)]] | alt | 114 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +13.8) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.92× (z +12.0) | — |
| [[H4 (line)]] | wt | 62.2 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +10.5) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 54.7 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +12.3) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.10× (z +9.5) | — |
| [[NCI-H1573 (line)]] | alt | 70.9 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.36× (z +28.2) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[NCI-H1792 (line)]] | alt | 68.8 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +12.2) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.91× (z +9.6) | — |
| [[SW480 (line)]] | alt | 72.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.27× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[A498 (line)]] | wt | 90.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +13.4) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[A549 (line)]] | wt | 91.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +11.7) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[AsPC-1 (line)]] | alt | 80.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.80× (z +9.5) | — |
| [[BT-474 (line)]] | alt | 86.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +9.7) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[HOP62 (line)]] | alt | 56.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +14.8) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[HS-578T (line)]] | alt | 56.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +11.8) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 72.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +10.6) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[J82 (line)]] | alt | 57.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +12.3) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[LoVo (line)]] | wt | 95.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.31× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[LOX-IMVI (line)]] | wt | 61.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.92× (z +9.3) | — |
| [[NCI-H2030 (line)]] | alt | 135 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +17.0) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[NCI-H596 (line)]] | alt | 81.9 | 0 | 1 (1 ⚠) | — | [[Trametinib (drug)]] 5 µM 0.359× (z -10.6) ⚠ cell-cycle shift, explains ~45% of this change |
| [[Panc 03.27 (line)]] | alt | 77.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.71× (z +8.5) | — |
| [[SK-MEL-2 (line)]] | alt | 72.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +11.8) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[SNU-423 (line)]] | alt | 50.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +15.4) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[SW 1088 (line)]] | alt | 71.3 | 0 | 1 | — | [[Cabozantinib (S-malate) (drug)]] 0.05 µM 0.0725× (z -9.1) |
| [[SW48 (line)]] | wt | 66.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.68× (z +14.3) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[A-427 (line)]] | wt | 51.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 75.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 75.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 54.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 59.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 73.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 65.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 77.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 139 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 105 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 96.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 81.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 120 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 70.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 80.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 102 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 68.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 101 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2395), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*52 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPINT2]] | +0.59 | +0.44 / +0.53 | both halves | 3e-05 |  |
| [[MAPK3]] | +0.56 | +0.46 / +0.50 | both halves | 2e-05 | STRING 437 |
| [[MMUT]] | +0.55 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[GRB7]] | +0.54 | +0.37 / +0.59 | both halves | 9e-05 |  |
| [[ORC4]] | +0.54 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[ABI1]] | +0.54 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[SLC25A23]] | +0.53 | +0.38 / +0.51 | both halves | 6e-05 |  |
| [[TMEM219]] | +0.53 | +0.35 / +0.55 | both halves | 1e-04 |  |
| [[KLHL28]] | +0.53 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[FRG1DP]] | +0.52 | +0.52 / +0.38 | both halves | 7e-05 |  |
| [[JUP]] | +0.52 | +0.41 / +0.53 | both halves | 4e-05 |  |
| [[LMBRD1]] | +0.51 | +0.41 / +0.46 | both halves | 4e-05 |  |

## Genes that move opposite

*48 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTHFD1L]] | -0.56 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[ZBTB40]] | -0.56 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[TANGO6]] | -0.56 | -0.60 / -0.45 | both halves | 3e-05 |  |
| [[LARS2]] | -0.55 | -0.62 / -0.43 | both halves | 3e-05 |  |
| [[MLH3]] | -0.54 | -0.48 / -0.54 | both halves | 2e-05 |  |
| [[NOP56]] | -0.54 | -0.45 / -0.40 | both halves | 5e-05 |  |
| [[SCMH1]] | -0.53 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[MZF1]] | -0.53 | -0.55 / -0.39 | both halves | 5e-05 |  |
| [[PUS7]] | -0.53 | -0.63 / -0.43 | both halves | 3e-05 |  |
| [[ZNF8]] | -0.52 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[TAS2R14]] | -0.52 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[ATR]] | -0.52 | -0.51 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ATP8B1]] | B | ATP8B1 activity raises RAB11A's level | lines that do not express ATP8B1 (14) vs lines expressing it (36) | 1.26× lower at baseline in the lines without ATP8B1 | 0.034 | ⚠ within organs, on part of the lines; also absent: LGALS9, CDA, KRT86 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **-** arm (projection on the module's main direction -0.552). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-4.2, -32.8); signed map (-29.7, -3.8). **Vector** length 85.6, 20.3% of its response variance represented; |z| ≥ 3 in 778 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +5.8 | +17.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.3 | +7.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | +3.4 | +5.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.3 | +8.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | +3.2 | +9.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | +2.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.0 | +1.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.8 | +1.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.7 | -0.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.7 | +2.7 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.9 | -2.9 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.6 | -1.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.3 | -2.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.8 | -0.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | +0.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.1 | +0.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.8 | -1.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.6 | +0.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.4 | -1.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.3 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | RAB11A, member RAS oncogene family |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q22.31 — chr15:65,726,054-65,891,989 (+) |
| Ensembl biotype | protein_coding |
| Also known as | YL8 |
| Gene groups (HGNC) | RAB, member RAS oncogene GTPases |
| Reactome | 15 pathways, smallest: VxPx cargo-targeting to cilium; Vasopressin regulates renal water homeostasis via Aquaporins; Aquaporin-mediated transport |
| Matched by | ensembl_id |

**Function**, from UniProt [P62491](https://www.uniprot.org/uniprotkb/P62491) (Ras-related protein Rab-11A):

> The small GTPases Rab are key regulators of intracellular membrane trafficking, from the formation of transport vesicles to their fusion with membranes. Rabs cycle between an inactive GDP-bound form and an active GTP-bound form that is able to recruit to membranes different set of downstream effectors directly responsible for vesicle formation, movement, tethering and fusion. RAB11A regulates endocytic recycling. Forms a functional Rab11/RAB11FIP3/dynein complex that regulates the movement of …

**Summary**, from NCBI Gene [8766](https://www.ncbi.nlm.nih.gov/gene/8766):

> The protein encoded by this gene belongs to the Rab family of the small GTPase superfamily. It is associated with both constitutive and regulated secretory pathways, and may be involved in protein transport. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, May 2011]

**Accessions** — [HGNC:9760](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9760) · Entrez [8766](https://www.ncbi.nlm.nih.gov/gene/8766) · UniProt [P62491](https://www.uniprot.org/uniprotkb/P62491) · Ensembl [ENSG00000103769](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000103769)

## Data

Gene col 2395: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2395); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2395, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2395]; `tensor/DDL_lfc|DDL_z.npy` [2395]; `embed/gene_vectors.npy` [2395]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2395 or target_col == 2395). Every well: [[RAB11A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RAB11A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
