---
symbol: "SPNS2"
type: "gene"
col: 11357
ensembl_id: "ENSG00000183018"
name: "SPNS lysolipid transporter 2, sphingosine-1-phosphate"
location: "17p13.2"
module: 161
arm: "+"
pooled_cpm: 22.58
n_lines_expressing: 24
n_dd_up: 11
n_dd_down: 13
n_dd_up_clean: 10
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 25
direction_downstream: 39
tags: ["gene", "module/161"]
generated_by: "tahoemap"
---

# SPNS2

*SPNS lysolipid transporter 2, sphingosine-1-phosphate* — 17p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 5.02× (z +16.2, q 0e+00, up in 14 of 22 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (2 with an alert ⚠); the strongest is [[Betamethasone dipropionate (drug)]] 0.05 µM: 0.530× (z -5.9, q 2e-06, down in 12 of 22 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC2A1]] (+0.65, fdr 1e-05), [[TNFRSF11A]] (+0.62, fdr 1e-05), [[BAIAP3]] (+0.61, fdr 4e-05); moves opposite to [[ANGEL2]] (-0.53, fdr 9e-05), [[N4BP2]] (-0.51, fdr 3e-04), [[SPRY3]] (-0.50, fdr 3e-04).
> It is in [[Module 161]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 25 arrows point to it, the strongest [[PDGFB]] → it (grade B ⚠); 39 go from it, the strongest it → [[RDH13]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 1 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11357.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **5.02×** | +16.2 | 0e+00 | 14/22 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.54×** | +12.7 | 2e-34 | 14/22 (LoVo, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.47×** | +12.5 | 1e-33 | 13/22 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.88×** | +8.9 | 6e-17 | 11/22 (COLO 205, A498, …) | rises with dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.60×** | +6.6 | 4e-09 | 10/22 (NCI-H460, A549, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.81×** | +4.2 | 0.002 | 3/22 (HCT15, NCI-H1573, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.52×** | +4.2 | 0.002 | 7/22 (KATO III, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.18×** | +4.1 | 0.003 | 14/23 (A498, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Fumaric acid (drug)]] 5 µM |  | **1.41×** | +3.3 | 0.052 | 11/23 (HEC-1-A, SHP-77, …) | top dose only | plate-row cell shift |
| [[Vilanterol (drug)]] 0.05 µM |  | **1.38×** | +3.2 | 0.073 | 5/22 (CFPAC-1, HT-29, …) | all doses, flat | position effect removed |
| [[Vilanterol (drug)]] 5 µM |  | **1.25×** | +3.1 | 0.084 | 8/23 (A498, A-172, …) | all doses, flat | position effect removed |
| [[Dimethyl fumarate (drug)]] 5 µM |  | 1.37× | +3.0 | 0.11 | 9/23 (KATO III, HEC-1-A, …) | top dose only | plate-row cell shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11357.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **0.530×** | -5.9 | 2e-06 | 12/22 (Panc 03.27, NCI-H2347, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.571×** | -5.6 | 5e-06 | 15/22 (SW480, SW1417, …) | two highest doses | cell-cycle shift (explains ~16% here) |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.670×** | -4.0 | 0.011 | 11/22 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.685×** | -3.8 | 0.018 | 10/22 (NCI-H2347, Panc 03.27, …) | all doses, flat |  |
| [[Budesonide (drug)]] 0.5 µM |  | **0.687×** | -3.8 | 0.018 | 10/22 (NCI-H2347, NCI-H1573, …) | all doses, stronger at high dose | position effect removed |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.696×** | -3.6 | 0.023 | 9/22 (NCI-H2347, Panc 03.27, …) | all doses, flat |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.698×** | -3.6 | 0.023 | 12/22 (SW480, HT-29, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.690×** | -3.5 | 0.035 | 4/22 (SW480, SHP-77, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 5 µM |  | **0.710×** | -3.5 | 0.035 | 11/22 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **0.705×** | -3.4 | 0.041 | 15/22 (NCI-H2347, KATO III, …) | two highest doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.722×** | -3.3 | 0.054 | 7/22 (A-172, CFPAC-1, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.728×** | -3.2 | 0.067 | 13/22 (HT-29, LS 180, …) | top dose only |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.557×** | -3.1 | 0.092 | 11/23 (HEC-1-A, BT-474, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, +0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11357. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 16.1 | 0 | 8 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0881× (z -12.9) ⚠ toxic; cell-cycle shift, explains ~27% of this change · without an alert: [[Clobetasol propionate (drug)]] 5 µM 0.132× (z -11.2) |
| [[SW480 (line)]] | alt | 106 | 0 | 8 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.308× (z -12.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.272× (z -9.3) |
| [[HT-29 (line)]] | alt | 96.4 | 0 | 6 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.180× (z -16.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 5.80 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.05 µM 9.63× (z +9.3) | — |
| [[A-172 (line)]] | wt | 58.9 | 0 | 3 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0610× (z -11.6) ⚠ toxic; cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.0768× (z -11.1) |
| [[COLO 205 (line)]] | alt | 50.4 | 2 (2 ⚠) | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 20.5× (z +11.5) ⚠ cell-cycle shift, would explain all of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.215× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 87.4 | 0 | 3 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.324× (z -12.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 6.31 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 7.75× (z +8.6) | — |
| [[NCI-H1573 (line)]] | alt | 20.0 | 2 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 11.2× (z +9.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SHP-77 (line)]] | alt | 27.1 | 1 (1 ⚠) | 1 | [[Niclosamide (olamine) (drug)]] 5 µM 7.87× (z +8.7) ⚠ toxic; cell-cycle shift, would explain all of this change | [[Binimetinib (drug)]] 0.05 µM 0.232× (z -8.8) |
| [[A498 (line)]] | wt | 6.94 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.18× (z +9.7) ⚠ cell-cycle shift, explains ~41% of this change | — |
| [[HEC-1-A (line)]] | alt | 29.4 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.354× (z -8.9) ⚠ cell-cycle shift, explains ~86% of this change |
| [[LS 180 (line)]] | wt | 36.6 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.159× (z -10.3) ⚠ cell-cycle shift, would explain all of this change |
| [[SW1417 (line)]] | alt | 90.6 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.433× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 2.17 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.35 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 5.24 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.74 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.43 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 56.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.27 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.91 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.62 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.19 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 8.03 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.41 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.84 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.33 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.41 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.32 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.37 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 4.59 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.35 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.04 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.90 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.40 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.99 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.61 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.65 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 4.36 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 5.43 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 2.77 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 7.83 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.06 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11357), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC2A1]] | +0.65 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[TNFRSF11A]] | +0.62 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[BAIAP3]] | +0.61 | +0.54 / +0.42 | both halves | 4e-05 |  |
| [[NKD2]] | +0.60 | +0.61 / +0.42 | both halves | 4e-05 |  |
| [[CDK18]] | +0.59 | +0.56 / +0.43 | both halves | 3e-05 |  |
| [[PDGFB]] | +0.58 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[CARD10]] | +0.57 | +0.42 / +0.59 | both halves | 4e-05 |  |
| [[TMC6]] | +0.57 | +0.45 / +0.60 | both halves | 3e-05 |  |
| [[PRAG1]] | +0.56 | +0.46 / +0.55 | both halves | 3e-05 |  |
| [[RHPN2]] | +0.56 | +0.42 / +0.47 | both halves | 4e-05 |  |
| [[FCHO1]] | +0.56 | +0.56 / +0.28 | both halves | 3e-04 |  |
| [[SUN1]] | +0.56 | +0.49 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANGEL2]] | -0.53 | -0.39 / -0.37 | both halves | 9e-05 |  |
| [[N4BP2]] | -0.51 | -0.44 / -0.29 | both halves | 3e-04 |  |
| [[SPRY3]] | -0.50 | -0.45 / -0.28 | both halves | 3e-04 |  |
| [[MTHFD2L]] | -0.50 | -0.51 / -0.34 | both halves | 1e-04 |  |
| [[COBLL1]] | -0.48 | -0.53 / -0.30 | both halves | 2e-04 |  |
| [[HORMAD1]] | -0.48 | -0.50 / -0.20 | both halves | 7e-04 |  |
| [[STXBP5]] | -0.48 | -0.49 / -0.37 | both halves | 8e-05 |  |
| [[FAIM]] | -0.47 | -0.40 / -0.23 | both halves | 5e-04 |  |
| [[METTL4]] | -0.47 | -0.40 / -0.21 | both halves | 6e-04 |  |
| [[CARD8]] | -0.47 | -0.39 / -0.27 | both halves | 3e-04 |  |
| [[AP5M1]] | -0.47 | -0.42 / -0.16 | ⚠ not reproduced | 0.001 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*25 arrows, 25 of them with an alert ⚠; grade A 0, B 7, C 18. Shown: the 12 strongest; 13 more arrows (13 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PDGFB]] | B | PDGFB activity raises SPNS2's level | lines that do not express PDGFB (16) vs lines expressing it (34) | 2.51× lower at baseline in the lines without PDGFB | 0.022 | ⚠ within organs, on part of the lines; also absent: PRAG1, LGALS3, ADAM8 |
| [[NR3C1]] | B | NR3C1 activity lowers SPNS2's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 3.1% of all compounds | 0.032 | ⚠ off-target possible; 3 compounds |
| [[MFNG]] | B | MFNG activity raises SPNS2's level | lines that do not express MFNG (12) vs lines expressing it (38) | 3.40× lower at baseline in the lines without MFNG | 0.046 | ⚠ within organs, on part of the lines; also absent: CARD10, EPS8L2, KRT8 |
| [[KRT15]] | B | KRT15 activity raises SPNS2's level | lines that do not express KRT15 (15) vs lines expressing it (35) | 2.98× lower at baseline in the lines without KRT15 | 0.067 | ⚠ within organs, on part of the lines; also absent: MISP, PSORS1C1, ENSG00000266088 |
| [[SEMA3B]] | B | SEMA3B activity raises SPNS2's level | lines that do not express SEMA3B (19) vs lines expressing it (31) | 1.92× lower at baseline in the lines without SEMA3B | 0.078 | ⚠ within organs, on part of the lines; also absent: SERPINA1, CSF1R, TNNT2; maybe low, not absent |
| [[EPHB3]] | B | EPHB3 activity raises SPNS2's level | lines that do not express EPHB3 (15) vs lines expressing it (35) | 2.90× lower at baseline in the lines without EPHB3 | 0.091 | ⚠ within organs, on part of the lines; also absent: SLC7A8, MCF2L, ENPP5; maybe low, not absent |
| [[ATG9B]] | B | ATG9B activity raises SPNS2's level | lines that do not express ATG9B (20) vs lines expressing it (30) | 2.24× lower at baseline in the lines without ATG9B | 0.096 | ⚠ within organs, on part of the lines; also absent: AFAP1L2, GJB3, EREG |
| [[IRF6]] | C | IRF6 activity raises SPNS2's level | lines that do not express IRF6 (31) vs lines expressing it (19) | 5.83× lower at baseline in the lines without IRF6 | 3e-04 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ST14, TMPRSS4, TMEM125; co-absent with the target |
| [[SLC5A1]] | C | SLC5A1 activity raises SPNS2's level | lines that do not express SLC5A1 (36) vs lines expressing it (14) | 6.86× lower at baseline in the lines without SLC5A1 | 7e-04 | ⚠ within organs, on part of the lines; also absent: TMEM30B, TMPRSS2, TMEM125; co-absent with the target |
| [[PTAFR]] | C | PTAFR activity raises SPNS2's level | lines that do not express PTAFR (29) vs lines expressing it (21) | 4.35× lower at baseline in the lines without PTAFR | 0.001 | ⚠ within organs, on part of the lines; also absent: TJP3, BSPRY, KDF1; maybe low, not absent; co-absent with the target |
| [[TINAGL1]] | C | TINAGL1 activity raises SPNS2's level | lines that do not express TINAGL1 (26) vs lines expressing it (24) | 3.65× lower at baseline in the lines without TINAGL1 | 0.001 | ⚠ within organs, on part of the lines; also absent: IL20RA, MSLN, KRT19; co-absent with the target |
| [[SKAP1]] | C | SKAP1 activity raises SPNS2's level | lines that do not express SKAP1 (34) vs lines expressing it (16) | 5.68× lower at baseline in the lines without SKAP1 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KCNE3, TMEM125, SLC5A1; co-absent with the target |

### Downstream of this gene

*39 arrows, 39 of them with an alert ⚠; grade A 0, B 22, C 17. Shown: the 12 strongest; 27 more arrows (27 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RDH13]] | B | SPNS2 activity raises RDH13's level | lines that do not express SPNS2 (26) vs lines expressing it (24) | 2.24× lower at baseline in the lines without SPNS2 | 0.005 | ⚠ within organs, on part of the lines; also absent: MACC1, CATSPERB, TC2N |
| [[FAM102A]] | B | SPNS2 activity raises FAM102A's level | lines that do not express SPNS2 (26) vs lines expressing it (24) | 2.18× lower at baseline in the lines without SPNS2 | 0.005 | ⚠ within organs, on part of the lines; also absent: MACC1, CATSPERB, TC2N |
| [[BIK]] | B | SPNS2 activity raises BIK's level | lines that do not express SPNS2 (26) vs lines expressing it (24) | 2.82× lower at baseline in the lines without SPNS2 | 0.005 | ⚠ within organs, on part of the lines; also absent: MACC1, CATSPERB, TC2N |
| [[SLC25A25]] | B | SPNS2 activity raises SLC25A25's level | lines that do not express SPNS2 (26) vs lines expressing it (24) | 1.96× lower at baseline in the lines without SPNS2 | 0.017 | ⚠ within organs, on part of the lines; also absent: MACC1, CATSPERB, TC2N |
| [[EPHB3]] | B | SPNS2 activity raises EPHB3's level | lines that do not express SPNS2 (26) vs lines expressing it (24) | 2.47× lower at baseline in the lines without SPNS2 | 0.020 | ⚠ within organs, on part of the lines; also absent: MACC1, CATSPERB, TC2N |
| [[CDK18]] | B | SPNS2 activity raises CDK18's level | lines that do not express SPNS2 (26) vs lines expressing it (24) | 2.02× lower at baseline in the lines without SPNS2 | 0.022 | ⚠ within organs, on part of the lines; also absent: MACC1, CATSPERB, TC2N |
| [[TMC6]] | B | SPNS2 activity raises TMC6's level | lines that do not express SPNS2 (26) vs lines expressing it (24) | 3.05× lower at baseline in the lines without SPNS2 | 0.024 | ⚠ within organs, on part of the lines; also absent: MACC1, CATSPERB, TC2N |
| [[GOLGA7B]] | B | SPNS2 activity raises GOLGA7B's level | lines that do not express SPNS2 (26) vs lines expressing it (24) | 1.78× lower at baseline in the lines without SPNS2 | 0.030 | ⚠ within organs, on part of the lines; also absent: MACC1, CATSPERB, TC2N |
| [[NGEF]] | B | SPNS2 activity raises NGEF's level | lines that do not express SPNS2 (26) vs lines expressing it (24) | 2.33× lower at baseline in the lines without SPNS2 | 0.036 | ⚠ within organs, on part of the lines; also absent: MACC1, CATSPERB, TC2N |
| [[SLC2A1]] | B | SPNS2 activity raises SLC2A1's level | lines that do not express SPNS2 (26) vs lines expressing it (24) | 2.13× lower at baseline in the lines without SPNS2 | 0.046 | ⚠ within organs, on part of the lines; also absent: MACC1, CATSPERB, TC2N |
| [[RARA]] | B | SPNS2 activity raises RARA's level | lines that do not express SPNS2 (26) vs lines expressing it (24) | 1.14× lower at baseline in the lines without SPNS2 | 0.048 | ⚠ within organs, on part of the lines; also absent: MACC1, CATSPERB, TC2N |
| [[KRT15]] | B | SPNS2 activity raises KRT15's level | lines that do not express SPNS2 (26) vs lines expressing it (24) | 2.51× lower at baseline in the lines without SPNS2 | 0.050 | ⚠ within organs, on part of the lines; also absent: MACC1, CATSPERB, TC2N |

## Where it sits

- **Module**: [[Module 161]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.664). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (35.3, -4.0); signed map (-2.2, 41.8). **Vector** length 86.3, 27.2% of its response variance represented; |z| ≥ 3 in 683 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +4.8 | +16.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.6 | +12.5 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.3 | +12.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | +6.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.1 | +4.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.2 | +4.2 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | +1.7 | +2.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.6 | +2.4 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.5 | +1.6 |
| fall | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.3 | +0.3 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, would explain all of this change | -3.2 | -0.9 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.2 | -2.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -3.1 | -3.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.0 | -0.4 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.2 | -4.0 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.2 | -3.1 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -2.2 | -2.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.2 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | SPNS lysolipid transporter 2, sphingosine-1-phosphate |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.2 — chr17:4,498,881-4,539,035 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SLC63A2 |
| Gene groups (HGNC) | Solute carrier family 63, sphingosine phosphate transporters |
| Reactome | 3 pathways, smallest: Sphingolipid de novo biosynthesis; Sphingolipid metabolism; Metabolism of lipids |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IVW8](https://www.uniprot.org/uniprotkb/Q8IVW8) (Sphingosine-1-phosphate transporter SPNS2):

> Lipid transporter that specifically mediates export of sphingosine-1-phosphate (sphing-4-enine 1-phosphate, S1P) and sphinganine-1-phosphate in the lymph, thereby playing a role in lymphocyte trafficking. S1P is a bioactive signaling molecule that regulates many physiological processes important for the development and for the immune system. Regulates levels of S1P and the S1P gradient that exists between the high circulating concentrations of S1P and low tissue levels that control lymphocyte …

**Summary**, from NCBI Gene [124976](https://www.ncbi.nlm.nih.gov/gene/124976):

> The protein encoded by this gene is a transporter of sphingosine 1-phosphate, a secreted lipid that is important in cardiovascular, immunological, and neural development. Defects in this gene are a cause of early onset progressive hearing loss. [provided by RefSeq, Jul 2016]

**Accessions** — [HGNC:26992](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26992) · Entrez [124976](https://www.ncbi.nlm.nih.gov/gene/124976) · UniProt [Q8IVW8](https://www.uniprot.org/uniprotkb/Q8IVW8) · Ensembl [ENSG00000183018](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183018)

## Data

Gene col 11357: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11357); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11357, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11357]; `tensor/DDL_lfc|DDL_z.npy` [11357]; `embed/gene_vectors.npy` [11357]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11357 or target_col == 11357). Every well: [[SPNS2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPNS2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
