---
symbol: "CLMP"
type: "gene"
col: 9268
ensembl_id: "ENSG00000166250"
name: "CXADR like cell adhesion molecule"
location: "11q24.1"
module: 147
arm: "+"
pooled_cpm: 75.78
n_lines_expressing: 25
n_dd_up: 10
n_dd_down: 34
n_dd_up_clean: 8
n_dd_down_clean: 33
in_vector_space: true
direction_upstream: 17
direction_downstream: 19
tags: ["gene", "module/147"]
generated_by: "tahoemap"
---

# CLMP

*CXADR like cell adhesion molecule* — 11q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.05× (z +8.6, q 5e-15, up in 5 of 24 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Clobetasol propionate (drug)]] 0.05 µM: 1.53× (z +5.1, q 1e-04, up in 15 of 23 measured lines).
> Pooled over the cell lines (median), lowered significantly by 34 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.405× (z -15.2, q 0e+00, down in 23 of 23 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HMGA2]] (+0.72, fdr 7e-06), [[FOXL1]] (+0.68, fdr 7e-06), [[NLRP3]] (+0.67, fdr 7e-06); moves opposite to [[MBNL2]] (-0.58, fdr 1e-05), [[GPRC5B]] (-0.57, fdr 1e-05), [[PIK3C2B]] (-0.55, fdr 1e-05).
> It is in [[Module 147]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 17 arrows point to it, the strongest [[NPAS2]] → it (grade B ⚠); 19 go from it, the strongest it → [[ITGA5]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9268.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.05×** | +8.6 | 5e-15 | 5/24 (NCI-H2347, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.53×** | +5.1 | 1e-04 | 15/23 (Hs 766T, NCI-H2347, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 0.5 µM |  | **1.50×** | +4.9 | 2e-04 | 10/23 (Hs 766T, SNU-423, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.41×** | +4.1 | 0.005 | 12/23 (Hs 766T, NCI-H2347, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.40×** | +4.1 | 0.005 | 14/23 (Hs 766T, SNU-423, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.40×** | +4.0 | 0.005 | 7/23 (AsPC-1, NCI-H2347, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.35×** | +3.5 | 0.042 | 3/19 (NCI-H2347, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Budesonide (drug)]] 0.05 µM |  | **1.33×** | +3.4 | 0.046 | 6/23 (Hs 766T, SNU-423, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.53×** | +3.3 | 0.057 | 6/23 (NCI-H460, RPMI-7951, …) | two highest doses | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[Rapamycin (drug)]] 5 µM |  | **1.21×** | +3.2 | 0.082 | 10/23 (HS-578T, AsPC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 1 with an alert ⚠; shown: the 15 strongest. 34 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9268.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.405×** | -15.2 | 0e+00 | 23/23 (NCI-H460, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.355×** | -12.3 | 2e-32 | 22/23 (NCI-H460, HS-578T, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.446×** | -9.6 | 2e-19 | 23/23 (HS-578T, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.511×** | -8.0 | 2e-13 | 23/23 (HS-578T, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.510×** | -7.7 | 2e-12 | 21/23 (HS-578T, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.526×** | -7.6 | 2e-12 | 20/23 (HS-578T, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.539×** | -7.1 | 1e-10 | 17/22 (AsPC-1, HS-578T, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM |  | **0.557×** | -6.8 | 6e-10 | 20/25 (AsPC-1, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **0.572×** | -6.6 | 2e-09 | 23/23 (HS-578T, HOP62, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.680×** | -6.5 | 6e-09 | 19/23 (PANC-1, A-172, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~1% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.558×** | -6.4 | 8e-09 | 14/23 (AsPC-1, HS-578T, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.697×** | -5.9 | 2e-07 | 14/23 (AsPC-1, HS-578T, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.635×** | -5.4 | 3e-06 | 14/22 (AsPC-1, HOP62, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.373×** | -5.1 | 1e-05 | 19/24 (HS-578T, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.708×** | -5.0 | 2e-05 | 19/23 (AsPC-1, HS-578T, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9268. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 308 | 0 | 27 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0398× (z -36.9) |
| [[AsPC-1 (line)]] | alt | 396 | 1 | 23 (2 ⚠) | [[Auranofin (drug)]] 5 µM 3.76× (z +11.2) | [[Homoharringtonine (drug)]] 5 µM 0.0727× (z -31.0) |
| [[HOP62 (line)]] | alt | 440 | 0 | 24 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0269× (z -34.3) |
| [[Hs 766T (line)]] | wt | 54.6 | 7 | 6 | [[Clobetasol propionate (drug)]] 0.05 µM 4.37× (z +9.6) | [[Homoharringtonine (drug)]] 5 µM 0.141× (z -17.9) |
| [[NCI-H460 (line)]] | wt | 135 | 2 | 9 (2 ⚠) | [[Pitavastatin (Calcium) (drug)]] 5 µM 2.87× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.0414× (z -38.6) |
| [[A-172 (line)]] | wt | 64.5 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.121× (z -19.3) |
| [[A549 (line)]] | wt | 64.2 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0584× (z -22.3) |
| [[H4 (line)]] | wt | 216 | 1 | 6 (1 ⚠) | [[Pitavastatin (Calcium) (drug)]] 5 µM 3.70× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.133× (z -19.1) |
| [[hTERT-HPNE (line)]] | wt | 350 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0873× (z -18.8) |
| [[LOX-IMVI (line)]] | wt | 74.2 | 2 | 5 (1 ⚠) | [[Pitavastatin (Calcium) (drug)]] 5 µM 4.33× (z +10.8) | [[Homoharringtonine (drug)]] 5 µM 0.0583× (z -30.3) |
| [[NCI-H23 (line)]] | alt | 39.5 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.115× (z -18.9) |
| [[A498 (line)]] | wt | 170 | 1 | 5 (1 ⚠) | [[Clobetasol propionate (drug)]] 0.05 µM 2.96× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -16.9) |
| [[NCI-H1792 (line)]] | alt | 252 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.137× (z -18.4) |
| [[RPMI-7951 (line)]] | alt | 154 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.104× (z -24.1) |
| [[SNU-423 (line)]] | alt | 190 | 1 | 5 (1 ⚠) | [[Clobetasol propionate (drug)]] 0.5 µM 3.24× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.107× (z -23.9) |
| [[J82 (line)]] | alt | 47.9 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -17.0) |
| [[PANC-1 (line)]] | alt | 25.0 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -16.2) |
| [[AN3 CA (line)]] | alt | 96.9 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.0647× (z -14.2) |
| [[NCI-H1573 (line)]] | alt | 23.7 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.197× (z -11.5) |
| [[NCI-H2030 (line)]] | alt | 27.2 | 0 | 2 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.524× (z -12.0) ⚠ position not correctable · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.271× (z -9.6) |
| [[SW 1088 (line)]] | alt | 201 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.0230× (z -12.9) |
| [[NCI-H2347 (line)]] | alt | 19.0 | 1 | 0 | [[Clobetasol propionate (drug)]] 0.05 µM 4.59× (z +9.5) | — |
| [[A-427 (line)]] | wt | 4.85 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 6.82 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 7.72 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 6.49 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 8.91 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 23.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.22 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 7.80 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 6.82 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 7.02 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 7.70 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 6.18 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 9.65 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 5.67 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.04 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 87.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 76.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.9 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 6.35 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 6.58 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 5.41 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.74 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 6.77 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 8.39 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 16.0 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 6.15 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 8.49 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 5.94 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9268), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HMGA2]] | +0.72 | +0.68 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[FOXL1]] | +0.68 | +0.73 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[NLRP3]] | +0.67 | +0.73 / +0.65 | both halves | 7e-06 |  |
| [[AKAP12]] | +0.65 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[MAP4K4]] | +0.64 | +0.69 / +0.58 | both halves | 8e-06 |  |
| [[HMGA2-AS1]] | +0.64 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[LINC00941]] | +0.63 | +0.69 / +0.58 | both halves | 8e-06 |  |
| [[ANPEP]] | +0.63 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[CAPRIN2]] | +0.62 | +0.68 / +0.54 | both halves | 1e-05 |  |
| [[NT5E]] | +0.61 | +0.68 / +0.58 | both halves | 7e-06 |  |
| [[ARHGAP22]] | +0.60 | +0.65 / +0.53 | both halves | 1e-05 |  |
| [[KIAA1549L]] | +0.60 | +0.66 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MBNL2]] | -0.58 | -0.55 / -0.59 | both halves | 1e-05 |  |
| [[GPRC5B]] | -0.57 | -0.53 / -0.55 | both halves | 1e-05 |  |
| [[PIK3C2B]] | -0.55 | -0.51 / -0.60 | both halves | 1e-05 |  |
| [[MAP3K8]] | -0.53 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[AKR1B1]] | -0.53 | -0.53 / -0.46 | both halves | 3e-05 |  |
| [[EPB41]] | -0.52 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[FRK]] | -0.51 | -0.55 / -0.44 | both halves | 3e-05 |  |
| [[TMPRSS3]] | -0.50 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[MATCAP2]] | -0.48 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[DMRTA1]] | -0.48 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[EPB41L1]] | -0.48 | -0.40 / -0.44 | both halves | 5e-05 |  |
| [[ANKRD33B]] | -0.48 | -0.55 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 5, C 12. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NPAS2]] | B | NPAS2 activity raises CLMP's level | lines that do not express NPAS2 (7) vs lines expressing it (43) | 1.96× lower at baseline in the lines without NPAS2 | 0.054 | ⚠ within organs, on part of the lines |
| [[ABL1]] | B | ABL1 activity raises CLMP's level | compounds that target ABL1: 4 of 6 lower it (Flumatinib, NG25, Ponatinib, Radotinib) | 67% of the class's compounds vs 5.0% of all compounds | 0.054 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[BCAR3]] | B | BCAR3 activity raises CLMP's level | lines that do not express BCAR3 (9) vs lines expressing it (41) | 4.12× lower at baseline in the lines without BCAR3 | 0.080 | ⚠ within organs, on part of the lines; also absent: ENSG00000261273, CD59, C11orf91; maybe low, not absent |
| [[LINC02454]] | B | LINC02454 activity raises CLMP's level | lines that do not express LINC02454 (12) vs lines expressing it (38) | 4.31× lower at baseline in the lines without LINC02454 | 0.089 | ⚠ within organs, on part of the lines; also absent: PAPLN, LGALS1, SCHIP1; maybe low, not absent |
| [[HMGA2]] | B | HMGA2 activity raises CLMP's level | lines that do not express HMGA2 (9) vs lines expressing it (41) | 1.87× lower at baseline in the lines without HMGA2 | 0.089 | ⚠ within organs, on part of the lines; also absent: SEMA4G, LINC02454 |
| [[PAPPA]] | C | PAPPA activity raises CLMP's level | lines that do not express PAPPA (33) vs lines expressing it (17) | 8.51× lower at baseline in the lines without PAPPA | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HTRA3, MSC-AS1, PDGFRB; co-absent with the target |
| [[FOXL1]] | C | FOXL1 activity raises CLMP's level | lines that do not express FOXL1 (25) vs lines expressing it (25) | 6.21× lower at baseline in the lines without FOXL1 | 0.001 | ⚠ within organs, on part of the lines; also absent: SIRLNT, PTHLH, WNT5A; co-absent with the target |
| [[WNT5A]] | C | WNT5A activity raises CLMP's level | lines that do not express WNT5A (30) vs lines expressing it (20) | 6.31× lower at baseline in the lines without WNT5A | 0.003 | ⚠ within organs, on part of the lines; also absent: APCDD1L, ABCC9, CDH13; co-absent with the target |
| [[STC1]] | C | STC1 activity raises CLMP's level | lines that do not express STC1 (24) vs lines expressing it (26) | 7.81× lower at baseline in the lines without STC1 | 0.003 | ⚠ within organs, on part of the lines; also absent: ENSG00000253891, MSC-AS1, CLMP; co-absent with the target |
| [[RFX8]] | C | RFX8 activity raises CLMP's level | lines that do not express RFX8 (35) vs lines expressing it (15) | 5.17× lower at baseline in the lines without RFX8 | 0.006 | ⚠ within organs, on part of the lines; also absent: TMPRSS15, IRAG2, CARMN; co-absent with the target |
| [[NLRP3]] | C | NLRP3 activity raises CLMP's level | lines that do not express NLRP3 (28) vs lines expressing it (22) | 5.03× lower at baseline in the lines without NLRP3 | 0.022 | ⚠ within organs, on part of the lines; also absent: FLI1, APCDD1L, MME; co-absent with the target |
| [[MSRB3]] | C | MSRB3 activity raises CLMP's level | lines that do not express MSRB3 (20) vs lines expressing it (30) | 4.23× lower at baseline in the lines without MSRB3 | 0.040 | ⚠ within organs, on part of the lines; also absent: ARHGEF6, KCNG1, FHL1; co-absent with the target |

### Downstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 11, C 8. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ITGA5]] | B | CLMP activity raises ITGA5's level | lines that do not express CLMP (25) vs lines expressing it (25) | 3.76× lower at baseline in the lines without CLMP | 0.026 | ⚠ within organs, on part of the lines; also absent: KCNMA1, PAPPA, DOCK10 |
| [[MLKL]] | B | CLMP activity raises MLKL's level | lines that do not express CLMP (25) vs lines expressing it (25) | 2.05× lower at baseline in the lines without CLMP | 0.033 | ⚠ within organs, on part of the lines; also absent: KCNMA1, PAPPA, DOCK10 |
| [[ELL2]] | B | CLMP activity raises ELL2's level | lines that do not express CLMP (25) vs lines expressing it (25) | 2.91× lower at baseline in the lines without CLMP | 0.034 | ⚠ within organs, on part of the lines; also absent: KCNMA1, PAPPA, DOCK10 |
| [[ELK3]] | B | CLMP activity raises ELK3's level | lines that do not express CLMP (25) vs lines expressing it (25) | 1.99× lower at baseline in the lines without CLMP | 0.042 | ⚠ within organs, on part of the lines; also absent: KCNMA1, PAPPA, DOCK10 |
| [[OSBPL5]] | B | CLMP activity raises OSBPL5's level | lines that do not express CLMP (25) vs lines expressing it (25) | 1.52× lower at baseline in the lines without CLMP | 0.052 | ⚠ within organs, on part of the lines; also absent: KCNMA1, PAPPA, DOCK10 |
| [[KIAA1549L]] | B | CLMP activity raises KIAA1549L's level | lines that do not express CLMP (25) vs lines expressing it (25) | 2.57× lower at baseline in the lines without CLMP | 0.058 | ⚠ within organs, on part of the lines; also absent: KCNMA1, PAPPA, DOCK10 |
| [[MICAL2]] | B | CLMP activity raises MICAL2's level | lines that do not express CLMP (25) vs lines expressing it (25) | 1.84× lower at baseline in the lines without CLMP | 0.074 | ⚠ within organs, on part of the lines; also absent: KCNMA1, PAPPA, DOCK10 |
| [[STEAP3]] | B | CLMP activity raises STEAP3's level | lines that do not express CLMP (25) vs lines expressing it (25) | 2.27× lower at baseline in the lines without CLMP | 0.083 | ⚠ within organs, on part of the lines; also absent: KCNMA1, PAPPA, DOCK10 |
| [[STEAP3]] | B | CLMP activity strengthens STEAP3's drug response | lines that do not express CLMP (20) vs lines expressing it (22) | the lines without CLMP respond 0.71× as strongly (z diff +1.51); strongest at Digitoxin 5 µM: 0.46x vs 0.23x (z diff +2.9) | 0.089 | ⚠ within organs, on part of the lines; also absent: KCNMA1, PAPPA, DOCK10; target measured in part of the lines; artifact flags |
| [[RAI14]] | B | CLMP activity raises RAI14's level | lines that do not express CLMP (25) vs lines expressing it (25) | 3.32× lower at baseline in the lines without CLMP | 0.089 | ⚠ within organs, on part of the lines; also absent: KCNMA1, PAPPA, DOCK10 |
| cells under [[Pentoxifylline (drug)]] 0.05 µM | B | CLMP activity raises the cells' numbers under Pentoxifylline 0.05 µM (protects the cells) | lines that do not express CLMP (25) vs lines expressing it (23) | the lines without CLMP: 0.84× the cells of the other lines | 0.093 | ⚠ within organs, on part of the lines; also absent: KCNMA1, PAPPA, DOCK10 |
| [[STC1]] | C | CLMP activity raises STC1's level | lines that do not express CLMP (25) vs lines expressing it (25) | 8.03× lower at baseline in the lines without CLMP | 0.007 | ⚠ within organs, on part of the lines; also absent: KCNMA1, PAPPA, DOCK10; co-absent with the target |

## Where it sits

- **Module**: [[Module 147]]; 30 genes; every member is in the + arm (projection on the module's main direction 0.752). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.39; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (46.4, 8.6); signed map (11.7, 46.7). **Vector** length 132, 46.8% of its response variance represented; |z| ≥ 3 in 1,113 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.8 | +3.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.3 | +8.6 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +3.5 | +5.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.4 | -0.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.3 | +2.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.1 | +4.0 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +2.9 | +4.9 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +2.7 | +4.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.6 | +2.7 |
| fall | [[Trametinib (drug)]] 5 µM |  | -5.6 | -6.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -4.8 | -6.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -4.7 | -5.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.7 | -6.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -4.6 | -7.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.6 | -5.0 |

## What is on record

|  |  |
|---|---|
| Name | CXADR like cell adhesion molecule |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q24.1 — chr11:123,069,872-123,195,248 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ASAM, FLJ22415, ACAM |
| Gene groups (HGNC) | V-set domain containing; I-set domain containing; IgCAM CXADR-related subfamily |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H6B4](https://www.uniprot.org/uniprotkb/Q9H6B4) (CXADR-like membrane protein):

> May be involved in the cell-cell adhesion. May play a role in adipocyte differentiation and development of obesity. Is required for normal small intestine development.

**Summary**, from NCBI Gene [79827](https://www.ncbi.nlm.nih.gov/gene/79827):

> This gene encodes a type I transmembrane protein that is localized to junctional complexes between endothelial and epithelial cells and may have a role in cell-cell adhesion. Expression of this gene in white adipose tissue is implicated in adipocyte maturation and development of obesity. This gene is also essential for normal intestinal development and mutations in the gene are associated with congenital short bowel syndrome. [provided by RefSeq, Aug 2015]

**Accessions** — [HGNC:24039](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24039) · Entrez [79827](https://www.ncbi.nlm.nih.gov/gene/79827) · UniProt [Q9H6B4](https://www.uniprot.org/uniprotkb/Q9H6B4) · Ensembl [ENSG00000166250](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166250)

## Data

Gene col 9268: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9268); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9268, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9268]; `tensor/DDL_lfc|DDL_z.npy` [9268]; `embed/gene_vectors.npy` [9268]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9268 or target_col == 9268). Every well: [[CLMP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CLMP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
