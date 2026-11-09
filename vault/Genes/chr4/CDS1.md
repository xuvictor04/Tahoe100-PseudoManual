---
symbol: "CDS1"
type: "gene"
col: 8733
ensembl_id: "ENSG00000163624"
name: "CDP-diacylglycerol synthase 1"
location: "4q21.23"
module: 99
arm: "+"
pooled_cpm: 26.14
n_lines_expressing: 31
n_dd_up: 18
n_dd_down: 9
n_dd_up_clean: 15
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 17
direction_downstream: 36
tags: ["gene", "module/099"]
generated_by: "tahoemap"
---

# CDS1

*CDP-diacylglycerol synthase 1* — 4q21.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (3 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.37× (z +19.0, q 0e+00, up in 19 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (none with an alert); the strongest is [[Harringtonine (drug)]] 5 µM: 0.564× (z -8.6, q 5e-15, down in 19 of 29 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MGAT4A]] (+0.67, fdr 7e-06), [[TPD52]] (+0.66, fdr 1e-05), [[TMEM65]] (+0.65, fdr 7e-06); moves opposite to [[ST7L]] (-0.62, fdr 1e-05), [[NEPRO-AS1]] (-0.61, fdr 3e-05), [[TASOR]] (-0.59, fdr 2e-05).
> It is in [[Module 099]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 17 arrows point to it, the strongest [[GALNT3]] → it (grade B ⚠); 36 go from it, the strongest it → [[OCLN]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8733.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.37×** | +19.0 | 0e+00 | 19/29 (PANC-1, A-172, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **3.37×** | +18.9 | 0e+00 | 23/29 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **3.18×** | +18.0 | 0e+00 | 25/29 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.84×** | +16.2 | 0e+00 | 23/29 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.62×** | +15.0 | 0e+00 | 26/29 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.02×** | +11.0 | 5e-26 | 13/28 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **3.26×** | +9.6 | 7e-20 | 22/29 (PANC-1, A498, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.51×** | +9.1 | 6e-18 | 12/28 (SW480, SHP-77, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.59×** | +7.2 | 3e-11 | 19/28 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Radotinib (drug)]] 5 µM |  | **1.30×** | +5.8 | 3e-07 | 16/29 (AsPC-1, SW1417, …) | top dose only |  |
| [[Brivudine (drug)]] 0.5 µM |  | **1.49×** | +4.4 | 6e-04 | 2/30 (A-427, PANC-1) | rises with dose | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.30×** | +4.1 | 0.002 | 9/29 (A-427, NCI-H1573, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.19× | +3.8 | 0.006 | 12/29 (NCI-H2347, BT-474, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.27×** | +3.8 | 0.007 | 16/29 (HT-29, A498, …) | inconsistent across doses |  |
| [[venetoclax (drug)]] 5 µM |  | **1.52×** | +3.4 | 0.024 | 5/26 (AsPC-1, COLO 205, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.16× | +3.3 | 0.037 | 9/30 (COLO 205, LS 180, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8733.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.564×** | -8.6 | 5e-15 | 19/29 (NCI-H2347, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.639×** | -7.0 | 9e-10 | 18/29 (NCI-H1573, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.696×** | -5.7 | 3e-06 | 19/29 (NCI-H2347, KATO III, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.821×** | -4.4 | 0.002 | 13/29 (NCI-H2347, BT-474, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.760×** | -4.3 | 0.002 | 15/29 (A498, NCI-H1573, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.774×** | -3.7 | 0.021 | 10/27 (LoVo, H4, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.938× | -3.6 | 0.027 | 2/30 (J82, C-33 A) | inconsistent across doses |  |
| [[Megestrol (drug)]] 0.05 µM |  | **0.799×** | -3.5 | 0.031 | 6/29 (LS 180, A498, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.793×** | -3.5 | 0.031 | 10/29 (LoVo, LS 180, …) | top dose only |  |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | **0.813×** | -3.2 | 0.068 | 2/29 (Hs 766T, SHP-77) | inconsistent across doses |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | 0.823× | -3.0 | 0.12 | 4/30 (A498, LS 180, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8733. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 74.8 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.464× (z -12.9) ⚠ cell-cycle shift, explains ~51% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.324× (z -12.8) |
| [[KATO III (line)]] | alt | 66.4 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.309× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.356× (z -11.1) |
| [[NCI-H1573 (line)]] | alt | 65.0 | 0 | 5 (2 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.307× (z -10.9) |
| [[LoVo (line)]] | wt | 45.4 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -14.6) ⚠ cell-cycle shift, explains ~51% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.343× (z -10.2) |
| [[PANC-1 (line)]] | alt | 9.32 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 5.73× (z +10.7) | [[Futibatinib (drug)]] 5 µM 0.0482× (z -9.7) |
| [[A498 (line)]] | wt | 15.2 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.18× (z +9.6) | — |
| [[HT-29 (line)]] | alt | 73.0 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.229× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.406× (z -9.4) |
| [[LS 180 (line)]] | wt | 91.6 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.247× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~11% of this change |
| [[SW48 (line)]] | wt | 109 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0662× (z -19.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~11% of this change |
| [[BT-474 (line)]] | alt | 46.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.265× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.344× (z -9.1) |
| [[HEC-1-A (line)]] | alt | 95.3 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.291× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~11% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.440× (z -8.6) |
| [[Panc 03.27 (line)]] | alt | 50.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.327× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 8.73 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.127× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 22.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.269× (z -8.6) |
| [[HCT15 (line)]] | alt | 67.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.348× (z -11.6) ⚠ cell-cycle shift, explains ~51% of this change |
| [[SHP-77 (line)]] | alt | 28.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.116× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 58.5 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.352× (z -10.7) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 6.15 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 4.65 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.27 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.64 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.85 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 7.27 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.47 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.39 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 6.68 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.12 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.84 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 4.19 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 4.48 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 46.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.87 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 4.42 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.68 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 4.96 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.49 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.65 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.62 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 7.95 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.87 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.27 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 14.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8733), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MGAT4A]] | +0.67 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[TPD52]] | +0.66 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[TMEM65]] | +0.65 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[PLEKHH3]] | +0.64 | +0.63 / +0.50 | both halves | 1e-05 |  |
| [[RALGPS1]] | +0.62 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[IGSF3]] | +0.61 | +0.48 / +0.64 | both halves | 2e-05 |  |
| [[FHIP1A]] | +0.61 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[SLC25A23]] | +0.61 | +0.59 / +0.48 | both halves | 2e-05 |  |
| [[HEBP1]] | +0.60 | +0.54 / +0.46 | both halves | 3e-05 |  |
| [[GPR160]] | +0.60 | +0.57 / +0.49 | both halves | 1e-05 |  |
| [[TRIM62]] | +0.60 | +0.59 / +0.47 | both halves | 2e-05 |  |
| [[ARL3]] | +0.59 | +0.50 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ST7L]] | -0.62 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[NEPRO-AS1]] | -0.61 | -0.57 / -0.46 | both halves | 3e-05 |  |
| [[TASOR]] | -0.59 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[CLHC1]] | -0.58 | -0.54 / -0.41 | both halves | 4e-05 |  |
| [[AVEN]] | -0.58 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[EMG1]] | -0.58 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[MCPH1]] | -0.58 | -0.55 / -0.43 | both halves | 3e-05 |  |
| [[PRORP]] | -0.58 | -0.59 / -0.41 | both halves | 4e-05 |  |
| [[MAD2L1-DT]] | -0.57 | -0.52 / -0.36 | both halves | 9e-05 |  |
| [[KRR1]] | -0.57 | -0.56 / -0.41 | both halves | 4e-05 |  |
| [[ERCC6]] | -0.57 | -0.59 / -0.39 | both halves | 6e-05 |  |
| [[ZNF655]] | -0.57 | -0.52 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 10, C 7. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GALNT3]] | B | GALNT3 activity raises CDS1's level | lines that do not express GALNT3 (30) vs lines expressing it (20) | 4.83× lower at baseline in the lines without GALNT3 | 0.001 | ⚠ within organs, on part of the lines; also absent: TMEM125, GRHL2, SKAP1 |
| [[PLEKHG1]] | B | PLEKHG1 activity raises CDS1's level | lines that do not express PLEKHG1 (17) vs lines expressing it (33) | 2.76× lower at baseline in the lines without PLEKHG1 | 0.019 | ⚠ within organs, on part of the lines; also absent: HLA-V-1, LSR, ARHGAP8 |
| [[CXADR]] | B | CXADR activity raises CDS1's level | lines that do not express CXADR (16) vs lines expressing it (34) | 3.09× lower at baseline in the lines without CXADR | 0.021 | ⚠ within organs, on part of the lines; also absent: LSR, ENTPD2, LMTK3 |
| [[ATP8B1]] | B | ATP8B1 activity raises CDS1's level | lines that do not express ATP8B1 (14) vs lines expressing it (36) | 3.09× lower at baseline in the lines without ATP8B1 | 0.022 | ⚠ within organs, on part of the lines; also absent: LGALS9, CDA, KRT86 |
| [[MGAT4A]] | B | MGAT4A activity raises CDS1's level | lines that do not express MGAT4A (11) vs lines expressing it (39) | 3.07× lower at baseline in the lines without MGAT4A | 0.025 | ⚠ within organs, on part of the lines; also absent: CAMSAP3, ZNF860, EPHA2 |
| [[NCMAP]] | B | NCMAP activity raises CDS1's level | lines that do not express NCMAP (26) vs lines expressing it (24) | 3.59× lower at baseline in the lines without NCMAP | 0.027 | ⚠ within organs, on part of the lines; also absent: TC2N, CRB3, SPINT1-AS1; maybe low, not absent |
| [[MCTP2]] | B | MCTP2 activity raises CDS1's level | lines that do not express MCTP2 (20) vs lines expressing it (30) | 2.82× lower at baseline in the lines without MCTP2 | 0.052 | ⚠ within organs, on part of the lines; also absent: ENSG00000227486, ENSG00000284644, MPZL3 |
| [[OCLN]] | B | OCLN activity raises CDS1's level | lines that do not express OCLN (19) vs lines expressing it (31) | 3.38× lower at baseline in the lines without OCLN | 0.061 | ⚠ within organs, on part of the lines; also absent: ENTPD2, LSR, EPHA10 |
| [[HHLA2]] | B | HHLA2 activity raises CDS1's level | lines that do not express HHLA2 (38) vs lines expressing it (12) | 3.44× lower at baseline in the lines without HHLA2 | 0.099 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, TM4SF4, MUC13 |
| [[FHIP1A]] | B | FHIP1A activity raises CDS1's level | lines that do not express FHIP1A (7) vs lines expressing it (43) | 2.77× lower at baseline in the lines without FHIP1A | 0.0995 | ⚠ within organs, on part of the lines; also absent: SLC18B1, NIPAL1, TXNIP; maybe low, not absent |
| [[ESRP1]] | C | ESRP1 activity raises CDS1's level | lines that do not express ESRP1 (31) vs lines expressing it (19) | 6.53× lower at baseline in the lines without ESRP1 | 2e-05 | ⚠ within organs, on part of the lines; also absent: ST14, KDF1, CLDN7; co-absent with the target |
| [[CDH1]] | C | CDH1 activity raises CDS1's level | lines that do not express CDH1 (31) vs lines expressing it (19) | 6.40× lower at baseline in the lines without CDH1 | 3e-05 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ST14, LAD1, KDF1; co-absent with the target |

### Downstream of this gene

*36 arrows, 36 of them with an alert ⚠; grade A 0, B 30, C 6. Shown: the 12 strongest; 24 more arrows (24 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OCLN]] | B | CDS1 activity raises OCLN's level | lines that do not express CDS1 (19) vs lines expressing it (31) | 4.43× lower at baseline in the lines without CDS1 | 0.003 | ⚠ within organs, on part of the lines; also absent: ANO9, EPS8L2, C6orf132; maybe low, not absent |
| [[FAM102A]] | B | CDS1 activity raises FAM102A's level | lines that do not express CDS1 (19) vs lines expressing it (31) | 2.17× lower at baseline in the lines without CDS1 | 0.016 | ⚠ within organs, on part of the lines; also absent: ANO9, EPS8L2, C6orf132; maybe low, not absent |
| [[ATP8B1]] | B | CDS1 activity raises ATP8B1's level | lines that do not express CDS1 (19) vs lines expressing it (31) | 3.24× lower at baseline in the lines without CDS1 | 0.020 | ⚠ within organs, on part of the lines; also absent: ANO9, EPS8L2, C6orf132; maybe low, not absent |
| [[PPP2R5A]] | B | CDS1 activity raises PPP2R5A's level | lines that do not express CDS1 (19) vs lines expressing it (31) | 1.24× lower at baseline in the lines without CDS1 | 0.028 | ⚠ within organs, on part of the lines; also absent: ANO9, EPS8L2, C6orf132; maybe low, not absent |
| [[RAB6A]] | B | CDS1 activity raises RAB6A's level | lines that do not express CDS1 (19) vs lines expressing it (31) | 1.17× lower at baseline in the lines without CDS1 | 0.032 | ⚠ within organs, on part of the lines; also absent: ANO9, EPS8L2, C6orf132; maybe low, not absent |
| [[CNGA1]] | B | CDS1 activity raises CNGA1's level | lines that do not express CDS1 (19) vs lines expressing it (31) | 1.57× lower at baseline in the lines without CDS1 | 0.039 | ⚠ within organs, on part of the lines; also absent: ANO9, EPS8L2, C6orf132; maybe low, not absent |
| [[RCBTB2]] | B | CDS1 activity lowers RCBTB2's level | lines that do not express CDS1 (19) vs lines expressing it (31) | 1.44× higher at baseline in the lines without CDS1 | 0.039 | ⚠ within organs, on part of the lines; also absent: ANO9, EPS8L2, C6orf132; maybe low, not absent |
| [[RTN3]] | B | CDS1 activity raises RTN3's level | lines that do not express CDS1 (19) vs lines expressing it (31) | 1.42× lower at baseline in the lines without CDS1 | 0.039 | ⚠ within organs, on part of the lines; also absent: ANO9, EPS8L2, C6orf132; maybe low, not absent |
| [[ERCC6]] | B | CDS1 activity strengthens ERCC6's drug response | lines that do not express CDS1 (19) vs lines expressing it (30) | the lines without CDS1 respond 0.77× as strongly (z diff +0.82); strongest at Homoharringtonine 5 µM: 1.17x vs 1.55x (z diff +3.4) | 0.041 | ⚠ within organs, on part of the lines; also absent: ANO9, EPS8L2, C6orf132; maybe low, not absent; target measured in part of the lines; both ways; artifact flags |
| [[GALNT3]] | B | CDS1 activity raises GALNT3's level | lines that do not express CDS1 (19) vs lines expressing it (31) | 3.02× lower at baseline in the lines without CDS1 | 0.049 | ⚠ within organs, on part of the lines; also absent: ANO9, EPS8L2, C6orf132; maybe low, not absent |
| [[MGAT4A]] | B | CDS1 activity raises MGAT4A's level | lines that do not express CDS1 (19) vs lines expressing it (31) | 2.46× lower at baseline in the lines without CDS1 | 0.052 | ⚠ within organs, on part of the lines; also absent: ANO9, EPS8L2, C6orf132; maybe low, not absent |
| [[RAB11FIP1]] | B | CDS1 activity raises RAB11FIP1's level | lines that do not express CDS1 (19) vs lines expressing it (31) | 1.91× lower at baseline in the lines without CDS1 | 0.053 | ⚠ within organs, on part of the lines; also absent: ANO9, EPS8L2, C6orf132; maybe low, not absent |

## Where it sits

- **Module**: [[Module 099]] — hypoxia; 48 genes; every member is in the + arm (projection on the module's main direction 0.592). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-0.8, 4.6); signed map (-32.8, 19.6). **Vector** length 88.5, 24.4% of its response variance represented; |z| ≥ 3 in 732 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.4 | +19.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.4 | +15.0 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.7 | +18.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.7 | +11.0 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.6 | +7.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.2 | +9.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.1 | +5.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.3 | +4.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.3 | +3.3 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.5 | -5.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.9 | -8.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | -4.2 | -2.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.9 | -7.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.5 | -3.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.9 | -4.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.9 | -4.4 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.9 | -2.2 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.8 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | CDP-diacylglycerol synthase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q21.23 — chr4:84,583,127-84,651,334 (+) |
| Ensembl biotype | protein_coding |
| Reactome | 4 pathways, smallest: Synthesis of PI; Glycerophospholipid biosynthesis; Phospholipid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92903](https://www.uniprot.org/uniprotkb/Q92903) (Phosphatidate cytidylyltransferase 1):

> Catalyzes the conversion of phosphatidic acid (PA) to CDP-diacylglycerol (CDP-DAG), an essential intermediate in the synthesis of phosphatidylglycerol, cardiolipin and phosphatidylinositol. Exhibits almost no acyl chain preference for PA, showing no discrimination for the sn-1/sn-2 acyl chain composition of PAs. Plays an important role in regulating the growth of lipid droplets which are storage organelles at the center of lipid and energy homeostasis. Positively regulates the differentiation …

**Summary**, from NCBI Gene [1040](https://www.ncbi.nlm.nih.gov/gene/1040):

> Breakdown products of phosphoinositides are ubiquitous second messengers that function downstream of many G protein-coupled receptors and tyrosine kinases regulating cell growth, calcium metabolism, and protein kinase C activity. This gene encodes an enzyme which regulates the amount of phosphatidylinositol available for signaling by catalyzing the conversion of phosphatidic acid to CDP-diacylglycerol. This enzyme is an integral membrane protein localized to two subcellular domains, the matrix …

**Accessions** — [HGNC:1800](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1800) · Entrez [1040](https://www.ncbi.nlm.nih.gov/gene/1040) · UniProt [Q92903](https://www.uniprot.org/uniprotkb/Q92903) · Ensembl [ENSG00000163624](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163624)

## Data

Gene col 8733: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8733); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8733, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8733]; `tensor/DDL_lfc|DDL_z.npy` [8733]; `embed/gene_vectors.npy` [8733]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8733 or target_col == 8733). Every well: [[CDS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
