---
symbol: "HLA-K"
type: "gene"
col: 13769
ensembl_id: "ENSG00000230795"
name: "major histocompatibility complex, class I, K (pseudogene)"
location: "6p22.1"
module: 169
arm: "+"
pooled_cpm: 4.46
n_lines_expressing: 28
n_dd_up: 8
n_dd_down: 5
n_dd_up_clean: 5
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 10
tags: ["gene", "module/169"]
generated_by: "tahoemap"
---

# HLA-K

*major histocompatibility complex, class I, K (pseudogene)* — 6p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 1.28× (z +6.1, q 7e-07, up in 19 of 26 measured lines) ⚠ position not correctable. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.74× (z +5.6, q 6e-06, up in 14 of 23 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.398× (z -6.6, q 2e-08, down in 20 of 26 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM: 0.535× (z -4.5, q 1e-03, down in 15 of 26 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 1 line (Panc 03.27 0.0161×; ⚠ cell-cycle shift, explains ~30% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (KATO III 0.0849×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MIR30DHG]] (+0.61, fdr 1e-05), [[SLC45A3]] (+0.59, fdr 1e-05), [[HLA-V-1]] (+0.54, fdr 3e-05); moves opposite to [[PPP2R5E]] (-0.54, fdr 2e-05), [[SEC24B]] (-0.51, fdr 7e-05), [[CCZ1]] (-0.50, fdr 4e-05).
> It is in [[Module 169]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MET]] → it (grade B ⚠); 10 go from it, the strongest it → [[KIF3A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13769.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.28×** | +6.1 | 7e-07 | 19/26 (CFPAC-1, NCI-H1792, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.74×** | +5.6 | 6e-06 | 14/23 (AsPC-1, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.86×** | +4.2 | 0.004 | 0/4 | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.79×** | +4.1 | 0.005 | 9/26 (NCI-H2347, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.75×** | +4.0 | 0.007 | 11/26 (SW 900, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.65×** | +3.5 | 0.038 | 6/25 (COLO 205, SW480, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.62×** | +3.3 | 0.079 | 12/24 (NCI-H2347, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.57×** | +3.2 | 0.096 | 4/20 (J82, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | 1.60× | +3.1 | 0.12 | 0/7 | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13769.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 1 line (Panc 03.27 0.0161×; ⚠ cell-cycle shift, explains ~30% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (KATO III 0.0849×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.398×** | -6.6 | 2e-08 | 20/26 (CFPAC-1, COLO 205, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.445×** | -5.8 | 1e-06 | 17/26 (Panc 03.27, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.446×** | -5.8 | 1e-06 | 17/26 (CFPAC-1, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.535×** | -4.5 | 1e-03 | 15/26 (KATO III, RPMI-7951, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.607×** | -3.6 | 0.036 | 13/23 (NCI-H1792, RKO, …) | rises with dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | 0.648× | -3.1 | 0.17 | 8/26 (Panc 03.27, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.632× | -3.1 | 0.18 | 4/26 (SW480, KATO III, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.45 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13769. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 3.44 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.8× (z +9.0) | — |
| [[KATO III (line)]] | alt | 17.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0849× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 10.4 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0161× (z -14.8) ⚠ cell-cycle shift, explains ~30% of this change |
| [[A-172 (line)]] | wt | 0.383 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.323 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.971 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.873 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.562 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.288 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.358 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.862 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.592 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 9.01 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.90 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.68 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.724 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.83 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.595 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.628 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.41 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.05 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.59 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.628 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.533 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 5.41 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.58 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.00 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.29 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.939 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.439 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.70 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.645 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.733 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.538 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.874 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.688 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 3.54 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13769), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 6 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MIR30DHG]] | +0.61 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[SLC45A3]] | +0.59 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[HLA-V-1]] | +0.54 | +0.49 / +0.46 | both halves | 3e-05 |  |
| [[FAM83G]] | +0.52 | +0.45 / +0.49 | both halves | 3e-05 |  |
| [[RELT]] | +0.52 | +0.46 / +0.55 | both halves | 2e-05 |  |
| [[HAS3]] | +0.52 | +0.44 / +0.51 | both halves | 3e-05 |  |
| [[KHNYN]] | +0.51 | +0.48 / +0.37 | both halves | 8e-05 |  |
| [[GPR35]] | +0.50 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[ZNF443]] | +0.50 | +0.41 / +0.52 | both halves | 4e-05 |  |
| [[SERPINB8]] | +0.49 | +0.35 / +0.48 | both halves | 1e-04 |  |
| [[NPR2]] | +0.49 | +0.27 / +0.44 | both halves | 3e-04 |  |
| [[LINC00460]] | +0.49 | +0.41 / +0.47 | both halves | 4e-05 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP2R5E]] | -0.54 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[SEC24B]] | -0.51 | -0.38 / -0.52 | both halves | 7e-05 |  |
| [[CCZ1]] | -0.50 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[RHOT1]] | -0.50 | -0.38 / -0.40 | both halves | 7e-05 |  |
| [[NLK]] | -0.48 | -0.37 / -0.41 | both halves | 8e-05 |  |
| [[TYW1]] | -0.48 | -0.38 / -0.42 | both halves | 6e-05 |  |
| [[USP42]] | -0.47 | -0.37 / -0.38 | both halves | 9e-05 |  |
| [[CCZ1B]] | -0.47 | -0.35 / -0.43 | both halves | 1e-04 |  |
| [[LAMTOR2]] | -0.46 | -0.36 / -0.43 | both halves | 1e-04 |  |
| [[KLHDC10]] | -0.46 | -0.27 / -0.48 | both halves | 3e-04 |  |
| [[SRPK2]] | -0.46 | -0.36 / -0.39 | both halves | 1e-04 |  |
| [[TSTD1]] | -0.46 | -0.29 / -0.39 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MET]] | B | MET activity raises HLA-K's level | lines that do not express MET (9) vs lines expressing it (41) | 2.68× lower at baseline in the lines without MET | 0.043 | ⚠ within organs, on part of the lines; also absent: TGFBR2, PHLDA2, VDR |
| [[HDAC6]] | B | HDAC6 activity raises HLA-K's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 9, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KIF3A]] | B | HLA-K activity lowers KIF3A's level | lines that do not express HLA-K (22) vs lines expressing it (28) | 1.50× higher at baseline in the lines without HLA-K | 0.019 | ⚠ within organs, on part of the lines; also absent: ACSL5, ICAM2, ENSG00000263325 |
| [[RHOT1]] | B | HLA-K activity lowers RHOT1's level | lines that do not express HLA-K (22) vs lines expressing it (28) | 1.30× higher at baseline in the lines without HLA-K | 0.030 | ⚠ within organs, on part of the lines; also absent: ACSL5, ICAM2, ENSG00000263325 |
| [[TLDC2]] | B | HLA-K activity raises TLDC2's level | lines that do not express HLA-K (22) vs lines expressing it (28) | 1.93× lower at baseline in the lines without HLA-K | 0.037 | ⚠ within organs, on part of the lines; also absent: ACSL5, ICAM2, ENSG00000263325 |
| [[MOB3C]] | B | HLA-K activity raises MOB3C's level | lines that do not express HLA-K (22) vs lines expressing it (28) | 1.32× lower at baseline in the lines without HLA-K | 0.057 | ⚠ within organs, on part of the lines; also absent: ACSL5, ICAM2, ENSG00000263325 |
| [[VSIG1]] | B | HLA-K activity raises VSIG1's level | lines that do not express HLA-K (22) vs lines expressing it (28) | 1.69× lower at baseline in the lines without HLA-K | 0.059 | ⚠ within organs, on part of the lines; also absent: ACSL5, ICAM2, ENSG00000263325 |
| [[MICE]] | B | HLA-K activity raises MICE's level | lines that do not express HLA-K (22) vs lines expressing it (28) | 1.98× lower at baseline in the lines without HLA-K | 0.070 | ⚠ within organs, on part of the lines; also absent: ACSL5, ICAM2, ENSG00000263325 |
| [[MET]] | B | HLA-K activity raises MET's level | lines that do not express HLA-K (22) vs lines expressing it (28) | 2.72× lower at baseline in the lines without HLA-K | 0.070 | ⚠ within organs, on part of the lines; also absent: ACSL5, ICAM2, ENSG00000263325 |
| [[HLA-H]] | B | HLA-K activity raises HLA-H's level | lines that do not express HLA-K (22) vs lines expressing it (28) | 1.93× lower at baseline in the lines without HLA-K | 0.075 | ⚠ within organs, on part of the lines; also absent: ACSL5, ICAM2, ENSG00000263325 |
| [[ANTKMT]] | B | HLA-K activity lowers ANTKMT's level | lines that do not express HLA-K (22) vs lines expressing it (28) | 1.28× higher at baseline in the lines without HLA-K | 0.098 | ⚠ within organs, on part of the lines; also absent: ACSL5, ICAM2, ENSG00000263325 |
| [[ICAM2]] | C | HLA-K activity raises ICAM2's level | lines that do not express HLA-K (22) vs lines expressing it (28) | 2.09× lower at baseline in the lines without HLA-K | 0.023 | ⚠ within organs, on part of the lines; also absent: ACSL5, ICAM2, ENSG00000263325; co-absent with the target |

## Where it sits

- **Module**: [[Module 169]]; 25 genes; every member is in the + arm (projection on the module's main direction -0.443). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (39.2, 1.3); signed map (7.9, 38.7). **Vector** length 45.0, 8.22% of its response variance represented; |z| ≥ 3 in 639 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.7 | +4.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.6 | +3.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.2 | +3.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.2 | +2.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.1 | +5.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.5 | +2.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +0.8 | +2.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +0.8 | +0.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +0.8 | +0.4 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | -1.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.5 | -0.4 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -1.4 | -3.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -1.1 | -1.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -1.1 | -6.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.1 | -2.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.1 | -2.9 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -1.0 | -2.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.0 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | major histocompatibility complex, class I, K (pseudogene) |
| Locus type | pseudogene |
| Location | 6p22.1 — chr6:29,926,459-29,929,232 (+) |
| Ensembl biotype | unprocessed_pseudogene |
| Also known as | HLA-70; previously HLAK, HLA70 |
| Gene groups (HGNC) | Histocompatibility complex |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:4969](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4969) · Entrez [3138](https://www.ncbi.nlm.nih.gov/gene/3138) · Ensembl [ENSG00000230795](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000230795)

## Data

Gene col 13769: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13769); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13769, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13769]; `tensor/DDL_lfc|DDL_z.npy` [13769]; `embed/gene_vectors.npy` [13769]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13769 or target_col == 13769). Every well: [[HLA-K — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HLA-K.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
