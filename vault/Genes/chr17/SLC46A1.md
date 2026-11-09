---
symbol: "SLC46A1"
type: "gene"
col: 1150
ensembl_id: "ENSG00000076351"
name: "solute carrier family 46 member 1"
location: "17q11.2"
module: 33
arm: "+"
pooled_cpm: 4.43
n_lines_expressing: 48
n_dd_up: 12
n_dd_down: 21
n_dd_up_clean: 8
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# SLC46A1

*solute carrier family 46 member 1* — 17q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.84× (z +6.5, q 3e-08, up in 2 of 6 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 1.68× (z +5.8, q 2e-06, up in 20 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.498× (z -10.9, q 4e-25, down in 26 of 35 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ASB13]] (+0.67, fdr 1e-05), [[RSAD1]] (+0.63, fdr 2e-05), [[NLE1]] (+0.63, fdr 1e-05); moves opposite to [[FANK1]] (-0.51, fdr 5e-05), [[AP4S1]] (-0.50, fdr 2e-04), [[IPO9-AS1]] (-0.48, fdr 2e-04).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[RASGEF1A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1150.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.84×** | +6.5 | 3e-08 | 2/6 (J82, CFPAC-1) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.68×** | +5.8 | 2e-06 | 20/43 (CFPAC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.67×** | +5.7 | 2e-06 | 24/45 (HepG2/C3A, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.39×** | +5.2 | 3e-05 | 17/44 (HepG2/C3A, A498, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.47×** | +4.3 | 0.002 | 13/45 (HepG2/C3A, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.31×** | +4.2 | 0.002 | 7/44 (RKO, A498, …) | top dose only | low cells (technical?) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.44×** | +4.0 | 0.005 | 6/24 (NCI-H23, A498, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.43×** | +3.8 | 0.009 | 6/21 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.37×** | +3.5 | 0.024 | 9/39 (HepG2/C3A, SW1417, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.41×** | +3.5 | 0.024 | 7/31 (LoVo, SW480, …) | inconsistent across doses | low cells (technical?) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.37×** | +3.5 | 0.024 | 6/42 (C32, HT-29, …) | rises with dose | position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **1.32×** | +3.1 | 0.093 | 5/44 (PANC-1, SW480, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1150.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.498×** | -10.9 | 4e-25 | 26/35 (BT-474, PANC-1, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.432×** | -9.3 | 4e-18 | 24/42 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.437×** | -9.2 | 7e-18 | 28/45 (SNU-1, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.472×** | -8.3 | 1e-14 | 21/31 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.482×** | -8.1 | 7e-14 | 22/44 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.503×** | -7.6 | 2e-12 | 23/42 (PANC-1, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.517×** | -7.3 | 2e-11 | 25/42 (LoVo, A498, …) | rises with dose | position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.512×** | -7.2 | 6e-11 | 18/43 (MIA PaCa-2, RKO, …) | top dose only | cell-cycle shift (explains ~20% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.346×** | -6.2 | 4e-08 | 18/40 (PANC-1, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.710×** | -5.4 | 5e-06 | 16/36 (SW1417, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.872× | -5.3 | 6e-06 | 20/46 (HEC-1-A, SW 900, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.631×** | -5.1 | 2e-05 | 15/45 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.650×** | -4.8 | 8e-05 | 16/37 (PANC-1, RKO, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.691×** | -3.9 | 0.003 | 7/33 (COLO 205, J82, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.695×** | -3.9 | 0.004 | 14/31 (A498, SNU-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.515×** | -3.8 | 0.004 | 14/33 (HEC-1-A, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.696×** | -3.8 | 0.005 | 8/38 (PANC-1, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1150. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 4.12 | 0 | 4 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.104× (z -11.4) |
| [[NCI-H2030 (line)]] | alt | 5.34 | 0 | 3 (2 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.0973× (z -9.5) ⚠ transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.220× (z -8.7) |
| [[A549 (line)]] | wt | 6.74 | 0 | 2 | — | [[Menadione (drug)]] 0.05 µM 0.0777× (z -10.1) |
| [[MIA PaCa-2 (line)]] | alt | 5.66 | 0 | 2 | — | [[Ipatasertib (drug)]] 0.05 µM 0.0776× (z -9.4) |
| [[SHP-77 (line)]] | alt | 4.39 | 0 | 2 | — | [[Bimatoprost (drug)]] 0.05 µM 0.0793× (z -8.6) |
| [[SW480 (line)]] | alt | 5.32 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0523× (z -16.3) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 13.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.274× (z -8.6) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 5.09 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0853× (z -11.2) |
| [[J82 (line)]] | alt | 5.22 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.0964× (z -9.5) |
| [[LoVo (line)]] | wt | 4.53 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0589× (z -12.0) |
| [[NCI-H23 (line)]] | alt | 6.43 | 0 | 1 (1 ⚠) | — | [[Sunitinib (drug)]] 5 µM 0.0919× (z -10.1) ⚠ toxic |
| [[RKO (line)]] | wt | 5.04 | 0 | 1 | — | [[Rosiglitazone (drug)]] 0.05 µM 0.0757× (z -8.7) |
| [[SNU-1 (line)]] | wt | 8.55 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0391× (z -10.0) |
| [[A-172 (line)]] | wt | 1.87 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 7.16 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.02 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.56 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.70 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.72 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.08 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.95 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.09 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.82 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.24 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.37 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.438 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.467 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.73 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.68 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.98 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.75 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.88 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.83 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.77 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.07 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1150), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ASB13]] | +0.67 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[RSAD1]] | +0.63 | +0.47 / +0.62 | both halves | 2e-05 |  |
| [[NLE1]] | +0.63 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[ZNF692]] | +0.62 | +0.42 / +0.61 | both halves | 4e-05 |  |
| [[TMCO6]] | +0.61 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[CGREF1]] | +0.60 | +0.62 / +0.47 | both halves | 2e-05 |  |
| [[TMEM177]] | +0.60 | +0.37 / +0.62 | both halves | 9e-05 |  |
| [[GTPBP3]] | +0.59 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[ACTR5]] | +0.58 | +0.46 / +0.49 | both halves | 2e-05 |  |
| [[CHST10]] | +0.58 | +0.44 / +0.60 | both halves | 3e-05 |  |
| [[MCOLN2]] | +0.58 | +0.42 / +0.53 | both halves | 4e-05 |  |
| [[FXN]] | +0.57 | +0.47 / +0.52 | both halves | 2e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FANK1]] | -0.51 | -0.40 / -0.48 | both halves | 5e-05 |  |
| [[AP4S1]] | -0.50 | -0.30 / -0.43 | both halves | 2e-04 |  |
| [[IPO9-AS1]] | -0.48 | -0.32 / -0.36 | both halves | 2e-04 |  |
| [[SNHG31]] | -0.48 | -0.28 / -0.36 | both halves | 3e-04 |  |
| [[FBXL13]] | -0.47 | -0.29 / -0.40 | both halves | 3e-04 |  |
| [[RNASEK]] | -0.47 | -0.33 / -0.38 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RASGEF1A]] | B | RASGEF1A activity raises SLC46A1's level | lines that do not express RASGEF1A (25) vs lines expressing it (25) | 1.57× lower at baseline in the lines without RASGEF1A | 0.004 | ⚠ within organs, on part of the lines; also absent: ITGB2, ANKRD20A21P, CHGB |
| [[LHX6]] | B | LHX6 activity raises SLC46A1's level | lines that do not express LHX6 (16) vs lines expressing it (34) | 1.47× lower at baseline in the lines without LHX6 | 0.045 | ⚠ within organs, on part of the lines; also absent: ENSG00000224905, RADIL, OLFM1; maybe low, not absent |
| [[RAB6B]] | B | RAB6B activity raises SLC46A1's level | lines that do not express RAB6B (14) vs lines expressing it (36) | 1.72× lower at baseline in the lines without RAB6B | 0.052 | ⚠ within organs, on part of the lines; also absent: FAM124A, WNT9A, MRAS |
| [[BRSK2]] | B | BRSK2 activity strengthens SLC46A1's drug response | lines that do not express BRSK2 (13) vs lines expressing it (32) | the lines without BRSK2 respond 0.56× as strongly (z diff +1.43); strongest at Digitoxin 5 µM: 0.53x vs 0.31x (z diff +2.4) | 0.086 | ⚠ within organs, on part of the lines; also absent: KIF26A, APLP1, E2F2; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[MCOLN2]] | B | MCOLN2 activity raises SLC46A1's level | lines that do not express MCOLN2 (18) vs lines expressing it (32) | 1.34× lower at baseline in the lines without MCOLN2 | 0.089 | ⚠ within organs, on part of the lines; also absent: DCLK2, MSI1, PARVG |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.611). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-11.9, -41.5); signed map (-8.3, -53.2). **Vector** length 53.2, 6.94% of its response variance represented; |z| ≥ 3 in 1,035 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +2.8 | +5.2 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +2.5 | +4.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.2 | +5.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.1 | +2.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +2.1 | +4.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.8 | +1.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.4 | +2.3 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.3 | +0.4 |
|  | [[Budesonide (drug)]] 5 µM |  | +1.2 | +1.6 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -3.2 | -10.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.2 | -5.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.7 | -7.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.6 | -9.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -2.6 | -3.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.2 | -2.7 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.7 | -3.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.2 | -3.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.2 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 46 member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q11.2 — chr17:28,394,642-28,407,197 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HCP1, MGC9564, PCFT, HsPCFT, hPCFT |
| Gene groups (HGNC) | Solute carrier family 46 |
| Reactome | 8 pathways, smallest: Metabolism of folate and pterines; Heme signaling; Iron uptake and transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96NT5](https://www.uniprot.org/uniprotkb/Q96NT5) (Proton-coupled folate transporter):

> Proton-coupled folate symporter that mediates folate absorption using an H(+) gradient as a driving force. Involved in the intestinal absorption of folates at the brush-border membrane of the proximal jejunum, and the transport from blood to cerebrospinal fluid across the choroid plexus. Functions at acidic pH via alternate outward- and inward-open conformation states. Protonation of residues in the outward open state primes the protein for transport. Binding of folate promotes breaking of salt …

**Summary**, from NCBI Gene [113235](https://www.ncbi.nlm.nih.gov/gene/113235):

> This gene encodes a transmembrane proton-coupled folate transporter protein that facilitates the movement of folate and antifolate substrates across cell membranes, optimally in acidic pH environments. This protein is also expressed in the brain and choroid plexus where it transports folates into the central nervous system. This protein further functions as a heme transporter in duodenal enterocytes, and potentially in other tissues like liver and kidney. Its localization to the apical membrane …

**Accessions** — [HGNC:30521](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30521) · Entrez [113235](https://www.ncbi.nlm.nih.gov/gene/113235) · UniProt [Q96NT5](https://www.uniprot.org/uniprotkb/Q96NT5) · Ensembl [ENSG00000076351](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000076351)

## Data

Gene col 1150: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1150); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1150, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1150]; `tensor/DDL_lfc|DDL_z.npy` [1150]; `embed/gene_vectors.npy` [1150]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1150 or target_col == 1150). Every well: [[SLC46A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC46A1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
