---
symbol: "BARX2"
type: "gene"
col: 492
ensembl_id: "ENSG00000043039"
name: "BARX homeobox 2"
location: "11q24.3"
module: 8
arm: "+"
pooled_cpm: 27.96
n_lines_expressing: 21
n_dd_up: 15
n_dd_down: 16
n_dd_up_clean: 11
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 32
direction_downstream: 49
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# BARX2

*BARX homeobox 2* — 11q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.05× (z +10.8, q 3e-24, up in 1 of 18 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.41× (z +7.2, q 9e-11, up in 3 of 19 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.647× (z -6.5, q 3e-08, down in 13 of 19 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PRSS51]] (+0.55, fdr 1e-05), [[NECTIN4]] (+0.52, fdr 1e-05), [[HS3ST1]] (+0.49, fdr 1e-05); moves opposite to [[TMEM168]] (-0.40, fdr 1e-04), [[EHMT1]] (-0.38, fdr 2e-04), [[KIAA0232]] (-0.36, fdr 4e-04).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 32 arrows point to it, the strongest [[FRMD4B]] → it (grade B ⚠); 49 go from it, the strongest it → [[KPNA7]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 5 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 492.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.05×** | +10.8 | 3e-24 | 1/18 (NCI-H1573) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.68×** | +7.5 | 2e-11 | 0/15 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.41×** | +7.2 | 9e-11 | 3/19 (LS 180, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.65×** | +6.9 | 6e-10 | 1/15 (SW1417) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.28×** | +5.3 | 1e-05 | 7/19 (SW1417, PANC-1, …) | top dose only |  |
| [[Vitamin K4 (drug)]] 0.05 µM |  | **1.31×** | +4.1 | 0.004 | 0/19 | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.67×** | +4.0 | 0.004 | 11/19 (LoVo, A498, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.66×** | +4.0 | 0.005 | 2/13 (A498, HCT15) | top dose only | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.30×** | +3.8 | 0.008 | 2/18 (PANC-1, LoVo) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.30×** | +3.8 | 0.008 | 0/19 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Verteporfin (drug)]] 5 µM |  | **1.28×** | +3.5 | 0.022 | 0/19 | top dose only |  |
| [[Bimatoprost (drug)]] 0.5 µM |  | **1.24×** | +3.3 | 0.050 | 0/19 | inconsistent across doses |  |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | **1.23×** | +3.1 | 0.074 | 0/19 | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.1 | 0.086 | 9/19 (COLO 205, BT-474, …) | top dose only | low cells (technical?) |
| [[Pexidartinib (hydrochloride) (drug)]] 5 µM |  | **1.23×** | +3.0 | 0.096 | 5/19 (NCI-H1573, MIA PaCa-2, …) | top dose only |  |
| [[Loperamide (hydrochloride) (drug)]] 0.05 µM |  | **1.22×** | +3.0 | 0.096 | 0/19 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 492.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.647×** | -6.5 | 3e-08 | 13/19 (CFPAC-1, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~12% here) |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.714×** | -5.1 | 9e-05 | 7/19 (A498, CFPAC-1, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM |  | **0.718×** | -5.0 | 9e-05 | 13/19 (CFPAC-1, Hs 766T, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.718×** | -5.0 | 9e-05 | 13/19 (MIA PaCa-2, A498, …) | top dose only |  |
| [[Artesunate (drug)]] 0.5 µM |  | **0.760×** | -4.1 | 0.004 | 2/19 (HCT15, COLO 205) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 0.05 µM |  | **0.771×** | -3.9 | 0.008 | 5/19 (A498, NCI-H2347, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.756×** | -3.9 | 0.008 | 4/19 (MIA PaCa-2, AsPC-1, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 5 µM |  | 0.836× | -3.8 | 0.010 | 6/19 (A498, NCI-H2347, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 5 µM |  | 0.837× | -3.8 | 0.010 | 7/19 (CFPAC-1, A498, …) | rises with dose |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.784×** | -3.7 | 0.014 | 6/19 (A498, NCI-H2347, …) | inconsistent across doses |  |
| [[Canagliflozin (drug)]] 5 µM |  | **0.787×** | -3.5 | 0.028 | 3/19 (AsPC-1, PANC-1, …) | top dose only |  |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | 0.852× | -3.4 | 0.031 | 6/19 (MIA PaCa-2, A498, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.799×** | -3.4 | 0.031 | 7/19 (CFPAC-1, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~8% here) |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **0.788×** | -3.3 | 0.035 | 8/19 (A498, CFPAC-1, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.944× | -3.3 | 0.035 | 0/19 | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.803×** | -3.3 | 0.035 | 6/19 (MIA PaCa-2, NCI-H2347, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 492. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 42.2 | 1 | 16 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 3.72× (z +8.9) | [[Panobinostat (drug)]] 5 µM 0.147× (z -13.5) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.189× (z -11.7) |
| [[CFPAC-1 (line)]] | alt | 205 | 0 | 15 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.116× (z -24.8) |
| [[NCI-H2347 (line)]] | alt | 69.1 | 0 | 15 (9 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.161× (z -17.5) |
| [[MIA PaCa-2 (line)]] | alt | 156 | 0 | 12 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.108× (z -17.8) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.212× (z -17.5) |
| [[Hs 766T (line)]] | wt | 179 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -20.1) ⚠ cell-cycle shift, explains ~85% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.122× (z -16.0) |
| [[Panc 03.27 (line)]] | alt | 37.3 | 0 | 7 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.148× (z -10.9) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.218× (z -9.0) |
| [[NCI-H1573 (line)]] | alt | 47.7 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0996× (z -16.2) ⚠ cell-cycle shift, explains ~85% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.194× (z -11.5) |
| [[LoVo (line)]] | wt | 45.5 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 10.6× (z +9.1) | [[Dinaciclib (drug)]] 0.5 µM 0.242× (z -10.4) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 60.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0694× (z -16.7) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 8.81 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0828× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Peretinoin (drug)]] 5 µM 0.110× (z -8.5) |
| [[AsPC-1 (line)]] | alt | 28.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.217× (z -10.4) |
| [[BT-474 (line)]] | alt | 31.9 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.131× (z -9.8) |
| [[COLO 205 (line)]] | alt | 40.1 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.108× (z -9.1) |
| [[HT-29 (line)]] | alt | 32.7 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.225× (z -8.9) |
| [[KATO III (line)]] | alt | 9.86 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.171× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 14.0 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.318× (z -8.6) |
| [[A-172 (line)]] | wt | 1.87 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.82 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.12 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.54 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.90 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.54 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.35 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.95 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.12 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.24 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.89 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.48 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.70 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.43 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.61 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.24 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.47 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.44 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.96 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.89 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.06 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.83 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.17 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.17 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.43 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 3.17 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 3.77 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.06 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 6.65 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 492), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRSS51]] | +0.55 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[NECTIN4]] | +0.52 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[HS3ST1]] | +0.49 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[GPR87]] | +0.48 | +0.43 / +0.47 | both halves | 3e-05 |  |
| [[WNT7A]] | +0.48 | +0.44 / +0.55 | both halves | 3e-05 |  |
| [[FAM107B]] | +0.48 | +0.47 / +0.44 | both halves | 3e-05 |  |
| [[ADGRF4]] | +0.47 | +0.47 / +0.36 | both halves | 1e-04 |  |
| [[NET1]] | +0.47 | +0.44 / +0.47 | both halves | 3e-05 |  |
| [[INPP4B]] | +0.47 | +0.46 / +0.47 | both halves | 3e-05 |  |
| [[TTC9]] | +0.46 | +0.39 / +0.46 | both halves | 5e-05 |  |
| [[CAMK1D]] | +0.46 | +0.44 / +0.42 | both halves | 4e-05 |  |
| [[PGBD5]] | +0.46 | +0.43 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM168]] | -0.40 | -0.39 / -0.35 | both halves | 1e-04 |  |
| [[EHMT1]] | -0.38 | -0.31 / -0.37 | both halves | 2e-04 |  |
| [[KIAA0232]] | -0.36 | -0.24 / -0.37 | both halves | 4e-04 |  |
| [[KAT8]] | -0.35 | -0.26 / -0.36 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*32 arrows, 32 of them with an alert ⚠; grade A 0, B 10, C 22. Shown: the 12 strongest; 20 more arrows (20 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FRMD4B]] | B | FRMD4B activity raises BARX2's level | lines that do not express FRMD4B (20) vs lines expressing it (30) | 2.70× lower at baseline in the lines without FRMD4B | 0.021 | ⚠ within organs, on part of the lines; also absent: LINC01589, ENSG00000290729, FRK; maybe low, not absent |
| [[KPNA7]] | B | KPNA7 activity raises BARX2's level | lines that do not express KPNA7 (10) vs lines expressing it (40) | 3.98× lower at baseline in the lines without KPNA7 | 0.025 | ⚠ within organs, on part of the lines; also absent: STS, LGALS3, ENSG00000248993; maybe low, not absent |
| [[FGD6]] | B | FGD6 activity raises BARX2's level | lines that do not express FGD6 (12) vs lines expressing it (38) | 4.05× lower at baseline in the lines without FGD6 | 0.037 | ⚠ within organs, on part of the lines; also absent: ENSG00000290957, PKP2, EPHA2-AS1; maybe low, not absent |
| [[ATG9B]] | B | ATG9B activity raises BARX2's level | lines that do not express ATG9B (20) vs lines expressing it (30) | 2.62× lower at baseline in the lines without ATG9B | 0.048 | ⚠ within organs, on part of the lines; also absent: AFAP1L2, GJB3, EREG |
| [[RAB27B]] | B | RAB27B activity raises BARX2's level | lines that do not express RAB27B (15) vs lines expressing it (35) | 2.68× lower at baseline in the lines without RAB27B | 0.079 | ⚠ within organs, on part of the lines; also absent: CXCL3, PLAAT4, F3 |
| [[KLHL32]] | B | KLHL32 activity raises BARX2's level | lines that do not express KLHL32 (13) vs lines expressing it (37) | 1.68× lower at baseline in the lines without KLHL32 | 0.091 | ⚠ within organs, on part of the lines; also absent: ATP8A1, ENSG00000270265, CHN2; maybe low, not absent |
| [[GRHL3]] | B | GRHL3 activity raises BARX2's level | lines that do not express GRHL3 (16) vs lines expressing it (34) | 2.27× lower at baseline in the lines without GRHL3 | 0.093 | ⚠ within organs, on part of the lines; also absent: SPINT2, FA2H, CDC42BPG; maybe low, not absent |
| [[TTC9]] | B | TTC9 activity raises BARX2's level | lines that do not express TTC9 (23) vs lines expressing it (27) | 2.42× lower at baseline in the lines without TTC9 | 0.093 | ⚠ within organs, on part of the lines; also absent: ITGB4, AREG, SPNS2 |
| [[INPP4B]] | B | INPP4B activity raises BARX2's level | lines that do not express INPP4B (10) vs lines expressing it (40) | 1.34× lower at baseline in the lines without INPP4B | 0.098 | ⚠ within organs, on part of the lines; also absent: RAB32, CD82, IFIT2 |
| [[TNFRSF21]] | B | TNFRSF21 activity raises BARX2's level | lines that do not express TNFRSF21 (15) vs lines expressing it (35) | 2.12× lower at baseline in the lines without TNFRSF21 | 0.099 | ⚠ within organs, on part of the lines; also absent: ENSG00000256982, SORL1, THRB; maybe low, not absent |
| [[EHF]] | C | EHF activity raises BARX2's level | lines that do not express EHF (27) vs lines expressing it (23) | 5.04× lower at baseline in the lines without EHF | 7e-04 | ⚠ within organs, on part of the lines; also absent: TMPRSS4, IRF6, GJB3; co-absent with the target |
| [[LPAR5]] | C | LPAR5 activity raises BARX2's level | lines that do not express LPAR5 (20) vs lines expressing it (30) | 3.69× lower at baseline in the lines without LPAR5 | 0.006 | ⚠ within organs, on part of the lines; also absent: PTAFR, SCNN1A, ITGB4; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*49 arrows, 49 of them with an alert ⚠; grade A 0, B 22, C 27. Shown: the 12 strongest; 37 more arrows (37 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KPNA7]] | B | BARX2 activity raises KPNA7's level | lines that do not express BARX2 (29) vs lines expressing it (21) | 2.65× lower at baseline in the lines without BARX2 | 0.004 | ⚠ within organs, on part of the lines; also absent: COL17A1, FXYD3, CEACAM6 |
| [[TNFRSF21]] | B | BARX2 activity raises TNFRSF21's level | lines that do not express BARX2 (29) vs lines expressing it (21) | 3.11× lower at baseline in the lines without BARX2 | 0.010 | ⚠ within organs, on part of the lines; also absent: COL17A1, FXYD3, CEACAM6 |
| [[ATG9B]] | B | BARX2 activity raises ATG9B's level | lines that do not express BARX2 (29) vs lines expressing it (21) | 2.13× lower at baseline in the lines without BARX2 | 0.010 | ⚠ within organs, on part of the lines; also absent: COL17A1, FXYD3, CEACAM6 |
| [[FRMD4B]] | B | BARX2 activity raises FRMD4B's level | lines that do not express BARX2 (29) vs lines expressing it (21) | 3.16× lower at baseline in the lines without BARX2 | 0.014 | ⚠ within organs, on part of the lines; also absent: COL17A1, FXYD3, CEACAM6 |
| [[RAB11FIP1]] | B | BARX2 activity raises RAB11FIP1's level | lines that do not express BARX2 (29) vs lines expressing it (21) | 2.35× lower at baseline in the lines without BARX2 | 0.015 | ⚠ within organs, on part of the lines; also absent: COL17A1, FXYD3, CEACAM6 |
| [[JUP]] | B | BARX2 activity raises JUP's level | lines that do not express BARX2 (29) vs lines expressing it (21) | 3.44× lower at baseline in the lines without BARX2 | 0.016 | ⚠ within organs, on part of the lines; also absent: COL17A1, FXYD3, CEACAM6 |
| [[FGD6]] | B | BARX2 activity raises FGD6's level | lines that do not express BARX2 (29) vs lines expressing it (21) | 2.39× lower at baseline in the lines without BARX2 | 0.022 | ⚠ within organs, on part of the lines; also absent: COL17A1, FXYD3, CEACAM6 |
| [[ATP1B1]] | B | BARX2 activity raises ATP1B1's level | lines that do not express BARX2 (29) vs lines expressing it (21) | 2.40× lower at baseline in the lines without BARX2 | 0.024 | ⚠ within organs, on part of the lines; also absent: COL17A1, FXYD3, CEACAM6 |
| [[CSTB]] | B | BARX2 activity raises CSTB's level | lines that do not express BARX2 (29) vs lines expressing it (21) | 1.94× lower at baseline in the lines without BARX2 | 0.025 | ⚠ within organs, on part of the lines; also absent: COL17A1, FXYD3, CEACAM6 |
| [[MXD1]] | B | BARX2 activity raises MXD1's level | lines that do not express BARX2 (29) vs lines expressing it (21) | 1.69× lower at baseline in the lines without BARX2 | 0.027 | ⚠ within organs, on part of the lines; also absent: COL17A1, FXYD3, CEACAM6 |
| [[PLEKHG3]] | B | BARX2 activity raises PLEKHG3's level | lines that do not express BARX2 (29) vs lines expressing it (21) | 2.04× lower at baseline in the lines without BARX2 | 0.041 | ⚠ within organs, on part of the lines; also absent: COL17A1, FXYD3, CEACAM6 |
| [[FRMPD3]] | B | BARX2 activity raises FRMPD3's level | lines that do not express BARX2 (29) vs lines expressing it (21) | 1.76× lower at baseline in the lines without BARX2 | 0.043 | ⚠ within organs, on part of the lines; also absent: COL17A1, FXYD3, CEACAM6 |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.332). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (17.2, 58.6); signed map (55.0, 7.7). **Vector** length 78.4, 23.3% of its response variance represented; |z| ≥ 3 in 682 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +2.9 | +4.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | +2.4 | -3.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.3 | +1.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~85% of this change | +2.2 | +0.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +2.2 | +3.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.6 | +0.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.5 | +0.7 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.3 | +2.4 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.2 | +0.3 |
| fall | [[5-Azacytidine (drug)]] 5 µM |  | -1.9 | -2.0 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.7 | -5.1 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.7 | -1.3 |
|  | [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | -1.5 | -3.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.5 | -5.0 |

## What is on record

|  |  |
|---|---|
| Name | BARX homeobox 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q24.3 — chr11:129,375,848-129,452,279 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | NKL subclass homeoboxes and pseudogenes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UMQ3](https://www.uniprot.org/uniprotkb/Q9UMQ3) (Homeobox protein BarH-like 2):

> Transcription factor. Binds optimally to the DNA consensus sequence 5'-YYTAATGRTTTTY-3'. May control the expression of neural adhesion molecules such as L1 or Ng-CAM during embryonic development of both the central and peripherical nervous system. May be involved in controlling adhesive processes in keratinizing epithelia (By similarity).

**Summary**, from NCBI Gene [8538](https://www.ncbi.nlm.nih.gov/gene/8538):

> This gene encodes a member of the homeobox transcription factor family. A highly related protein in mouse has been shown to influence cellular processes that control cell adhesion and remodeling of the actin cytoskeleton in myoblast fusion and chondrogenesis. The encoded protein may also play a role in cancer progression. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:956](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:956) · Entrez [8538](https://www.ncbi.nlm.nih.gov/gene/8538) · UniProt [Q9UMQ3](https://www.uniprot.org/uniprotkb/Q9UMQ3) · Ensembl [ENSG00000043039](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000043039)

## Data

Gene col 492: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 492); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 492, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 492]; `tensor/DDL_lfc|DDL_z.npy` [492]; `embed/gene_vectors.npy` [492]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 492 or target_col == 492). Every well: [[BARX2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BARX2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
