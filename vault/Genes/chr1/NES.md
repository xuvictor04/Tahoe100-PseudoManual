---
symbol: "NES"
type: "gene"
col: 5360
ensembl_id: "ENSG00000132688"
name: "nestin"
location: "1q23.1"
module: 78
arm: "+"
pooled_cpm: 17.23
n_lines_expressing: 24
n_dd_up: 19
n_dd_down: 9
n_dd_up_clean: 7
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 3
direction_downstream: 10
tags: ["gene", "module/078"]
generated_by: "tahoemap"
---

# NES

*nestin* — 1q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 5.68× (z +16.4, q 0e+00, up in 17 of 19 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 2.10× (z +9.9, q 9e-21, up in 15 of 21 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM: 0.559× (z -5.1, q 2e-04, down in 10 of 21 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NMNAT2]] (+0.69, fdr 7e-06), [[MSN]] (+0.66, fdr 1e-05), [[F2R]] (+0.66, fdr 7e-06); moves opposite to [[TOM1]] (-0.55, fdr 1e-05), [[MAP2K5]] (-0.52, fdr 2e-05), [[ANAPC16]] (-0.51, fdr 2e-05).
> It is in [[Module 078]], a single-armed module (apical junction).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); 10 go from it, the strongest it → [[DCBLD2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 12 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5360.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **5.68×** | +16.4 | 0e+00 | 17/19 (NCI-H1792, C32, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **4.41×** | +13.4 | 1e-38 | 14/15 (NCI-H1792, C32, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **3.44×** | +10.8 | 1e-24 | 15/16 (NCI-H1792, C32, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **2.10×** | +9.9 | 9e-21 | 15/21 (HEC-1-A, NCI-H460, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.07×** | +9.7 | 3e-20 | 8/22 (NCI-H1792, SW480, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.56×** | +8.9 | 7e-17 | 18/21 (SW480, C32, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.94×** | +6.2 | 4e-08 | 13/21 (NCI-H2347, NCI-H1792, …) | all doses, flat | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.89×** | +6.0 | 1e-07 | 12/21 (HEC-1-A, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **1.84×** | +5.5 | 2e-06 | 8/19 (SW480, NCI-H2347, …) | top dose only | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **1.69×** | +4.9 | 5e-05 | 13/21 (NCI-H2347, NCI-H1792, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~95% of this change | **1.59×** | +4.4 | 6e-04 | 11/21 (NCI-H2347, SK-MEL-2, …) | all doses, flat | position effect removed |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.58×** | +4.3 | 8e-04 | 12/19 (PANC-1, NCI-H2347, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.52×** | +4.0 | 0.003 | 14/21 (NCI-H1792, SHP-77, …) | all doses, flat | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.53×** | +3.9 | 0.004 | 6/21 (SK-MEL-2, C32, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.49×** | +3.6 | 0.011 | 6/21 (NCI-H1792, C32, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.29×** | +3.3 | 0.030 | 6/22 (NCI-H2347, SW480, …) | top dose only |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.57×** | +3.0 | 0.077 | 7/20 (NCI-H2347, Panc 03.27, …) | two highest doses | low cells (technical?); noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5360.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.559×** | -5.1 | 2e-04 | 10/21 (SW480, NCI-H460, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.708×** | -4.6 | 0.001 | 6/21 (PANC-1, SW480, …) | rises with dose | position effect removed |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.630×** | -4.5 | 0.002 | 14/21 (A-172, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Artesunate (drug)]] 0.5 µM |  | **0.678×** | -3.7 | 0.033 | 3/21 (PANC-1, AN3 CA, …) | rises with dose | position effect removed |
| [[Trametinib (drug)]] 0.05 µM |  | **0.765×** | -3.5 | 0.040 | 5/21 (SW480, HepG2/C3A, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.681×** | -3.5 | 0.040 | 11/21 (Panc 03.27, C32, …) | top dose only | position effect removed |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.730×** | -3.5 | 0.040 | 10/21 (SW480, C32, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.700×** | -3.4 | 0.049 | 10/21 (SW480, Hs 766T, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.701×** | -3.4 | 0.049 | 9/21 (HOP62, RPMI-7951, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.62 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5360. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 130 | 7 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.86× (z +12.4) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.91× (z +8.8) | — |
| [[NCI-H1792 (line)]] | alt | 13.6 | 7 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.7× (z +11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.95× (z +9.8) | — |
| [[SW480 (line)]] | alt | 46.3 | 3 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.71× (z +9.4) | — |
| [[A-172 (line)]] | wt | 111 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.30× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.221× (z -10.8) ⚠ cell-cycle shift, explains ~6% of this change |
| [[Hs 766T (line)]] | wt | 20.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.197× (z -10.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.157× (z -8.5) |
| [[NCI-H460 (line)]] | wt | 8.93 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.94× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[CHP-212 (line)]] | wt | 160 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -10.0) ⚠ cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 5.66 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 4.68× (z +8.8) | — |
| [[PANC-1 (line)]] | alt | 53.1 | 0 | 1 | — | [[Chlorhexidine (diacetate) (drug)]] 5 µM 0.394× (z -8.8) |
| [[SHP-77 (line)]] | alt | 5.06 | 0 | 1 | — | [[Phenylephrine (hydrochloride) (drug)]] 0.05 µM 0.0468× (z -9.0) |
| [[SK-MEL-2 (line)]] | alt | 27.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.30× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[A-427 (line)]] | wt | 1.27 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.32 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.65 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.63 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.46 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.71 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 9.96 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.96 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.56 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 3.58 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 27.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.50 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.07 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 41.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.14 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.61 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.96 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.99 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.53 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.58 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.34 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.82 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.72 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.88 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.76 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.55 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.05 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.81 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.82 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.96 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 8.49 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.13 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5360), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NMNAT2]] | +0.69 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[MSN]] | +0.66 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[F2R]] | +0.66 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[ACTN1]] | +0.65 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[CDC42EP2]] | +0.64 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[C13orf46]] | +0.64 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[AMOTL1]] | +0.63 | +0.57 / +0.59 | both halves | 9e-06 |  |
| [[CSMD2]] | +0.63 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[PODXL]] | +0.63 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[TPM3]] | +0.62 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[HHIP]] | +0.62 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[CD44]] | +0.62 | +0.53 / +0.64 | both halves | 1e-05 | STRING 888 |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TOM1]] | -0.55 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[MAP2K5]] | -0.52 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[ANAPC16]] | -0.51 | -0.51 / -0.46 | both halves | 2e-05 |  |
| [[TRPM7]] | -0.51 | -0.50 / -0.40 | both halves | 5e-05 |  |
| [[SAT2]] | -0.50 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[FBXO9]] | -0.50 | -0.41 / -0.47 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises NES's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 1.4% of all compounds | 0.017 | ⚠ off-target possible; 3 compounds |
| [[MAP2K2]] | B | MAP2K2 activity raises NES's level | compounds that target MAP2K2: 2 of 2 lower it (Binimetinib, Trametinib) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; shared targets |
| [[LAMA4]] | C | LAMA4 activity raises NES's level | lines that do not express LAMA4 (27) vs lines expressing it (23) | 2.76× lower at baseline in the lines without LAMA4 | 0.042 | ⚠ within organs, on part of the lines; also absent: SLFN12, ARMCX1, BAALC; co-absent with the target |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 3, C 7.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DCBLD2]] | B | NES activity raises DCBLD2's level | lines that do not express NES (26) vs lines expressing it (24) | 2.07× lower at baseline in the lines without NES | 0.041 | ⚠ within organs, on part of the lines; also absent: LAPTM5, CSPG4, ENSG00000230490 |
| [[ADAM19]] | B | NES activity raises ADAM19's level | lines that do not express NES (26) vs lines expressing it (24) | 2.13× lower at baseline in the lines without NES | 0.051 | ⚠ within organs, on part of the lines; also absent: LAPTM5, CSPG4, ENSG00000230490 |
| [[SCUBE3]] | B | NES activity raises SCUBE3's level | lines that do not express NES (26) vs lines expressing it (24) | 1.89× lower at baseline in the lines without NES | 0.085 | ⚠ within organs, on part of the lines; also absent: LAPTM5, CSPG4, ENSG00000230490 |
| [[PTGS1]] | C | NES activity raises PTGS1's level | lines that do not express NES (26) vs lines expressing it (24) | 2.65× lower at baseline in the lines without NES | 0.030 | ⚠ within organs, on part of the lines; also absent: LAPTM5, CSPG4, ENSG00000230490; co-absent with the target |
| [[LAMA4]] | C | NES activity raises LAMA4's level | lines that do not express NES (26) vs lines expressing it (24) | 3.89× lower at baseline in the lines without NES | 0.041 | ⚠ within organs, on part of the lines; also absent: LAPTM5, CSPG4, ENSG00000230490; co-absent with the target |
| [[LAPTM5]] | C | NES activity raises LAPTM5's level | lines that do not express NES (26) vs lines expressing it (24) | 2.07× lower at baseline in the lines without NES | 0.051 | ⚠ within organs, on part of the lines; also absent: LAPTM5, CSPG4, ENSG00000230490; co-absent with the target |
| [[TRPV2]] | C | NES activity raises TRPV2's level | lines that do not express NES (26) vs lines expressing it (24) | 2.42× lower at baseline in the lines without NES | 0.056 | ⚠ within organs, on part of the lines; also absent: LAPTM5, CSPG4, ENSG00000230490; co-absent with the target |
| [[PLAT]] | C | NES activity raises PLAT's level | lines that do not express NES (26) vs lines expressing it (24) | 4.31× lower at baseline in the lines without NES | 0.065 | ⚠ within organs, on part of the lines; also absent: LAPTM5, CSPG4, ENSG00000230490; co-absent with the target |
| [[WNT7A]] | C | NES activity raises WNT7A's level | lines that do not express NES (26) vs lines expressing it (24) | 1.97× lower at baseline in the lines without NES | 0.067 | ⚠ within organs, on part of the lines; also absent: LAPTM5, CSPG4, ENSG00000230490; co-absent with the target |
| [[PAEP]] | C | NES activity raises PAEP's level | lines that do not express NES (26) vs lines expressing it (24) | 2.48× lower at baseline in the lines without NES | 0.073 | ⚠ within organs, on part of the lines; also absent: LAPTM5, CSPG4, ENSG00000230490; co-absent with the target |

## Where it sits

- **Module**: [[Module 078]] — apical junction; 58 genes; every member is in the + arm (projection on the module's main direction 0.781). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (49.2, 10.7); signed map (6.7, 45.8). **Vector** length 60.6, 16.1% of its response variance represented; |z| ≥ 3 in 597 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *apical junction* (hallmark, mean cos +0.54 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.0 | +9.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | +4.8 | +13.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | +4.6 | +10.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | +4.5 | +16.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.8 | +6.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.7 | +8.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.1 | +1.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.4 | +1.8 |
|  | [[Apalutamide (drug)]] 0.5 µM |  | +1.2 | +1.6 |
| fall | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -2.8 | -4.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.4 | -3.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.2 | -5.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.1 | -2.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -1.8 | -0.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.8 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | nestin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q23.1 — chr1:156,668,763-156,677,407 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ21841 |
| Gene groups (HGNC) | Intermediate filaments Type IV |
| Matched by | ensembl_id |

**Function**, from UniProt [P48681](https://www.uniprot.org/uniprotkb/P48681) (Nestin):

> Required for brain and eye development. Promotes the disassembly of phosphorylated vimentin intermediate filaments (IF) during mitosis and may play a role in the trafficking and distribution of IF proteins and other cellular factors to daughter cells during progenitor cell division. Required for survival, renewal and mitogen-stimulated proliferation of neural progenitor cells (By similarity).

**Summary**, from NCBI Gene [10763](https://www.ncbi.nlm.nih.gov/gene/10763):

> This gene encodes a member of the intermediate filament protein family and is expressed primarily in nerve cells. [provided by RefSeq, Sep 2011]

**Accessions** — [HGNC:7756](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7756) · Entrez [10763](https://www.ncbi.nlm.nih.gov/gene/10763) · UniProt [P48681](https://www.uniprot.org/uniprotkb/P48681) · Ensembl [ENSG00000132688](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132688)

## Data

Gene col 5360: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5360); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5360, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5360]; `tensor/DDL_lfc|DDL_z.npy` [5360]; `embed/gene_vectors.npy` [5360]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5360 or target_col == 5360). Every well: [[NES — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NES.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
