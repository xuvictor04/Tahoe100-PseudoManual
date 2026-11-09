---
symbol: "MSRB3"
type: "gene"
col: 10459
ensembl_id: "ENSG00000174099"
name: "methionine sulfoxide reductase B3"
location: "12q14.3"
module: 13
arm: "+"
pooled_cpm: 89.88
n_lines_expressing: 30
n_dd_up: 5
n_dd_down: 13
n_dd_up_clean: 5
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 11
direction_downstream: 50
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# MSRB3

*methionine sulfoxide reductase B3* — 12q14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 0.5 µM: 1.89× (z +9.1, q 4e-17, up in 17 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (6 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.602× (z -7.3, q 1e-10, down in 22 of 28 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GLIS3]] (+0.54, fdr 2e-05), [[WNT5B]] (+0.53, fdr 3e-05), [[MIR100HG]] (+0.53, fdr 3e-05); moves opposite to [[EMC2]] (-0.50, fdr 5e-05), [[GOLPH3L]] (-0.48, fdr 4e-05), [[PLEKHA2]] (-0.47, fdr 5e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[RAB20]] → it (grade B ⚠); 50 go from it, the strongest it → [[HMGA2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10459.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.89×** | +9.1 | 4e-17 | 17/28 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.37×** | +6.4 | 6e-08 | 14/28 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.30×** | +3.7 | 0.042 | 11/28 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.28×** | +3.5 | 0.067 | 16/28 (C32, HOP62, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **1.27×** | +3.4 | 0.070 | 13/28 (Hs 766T, RPMI-7951, …) | all doses, flat |  |
| [[Megestrol (drug)]] 0.05 µM |  | 1.25× | +3.2 | 0.11 | 12/28 (HOP62, hTERT-HPNE, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 1.25× | +3.2 | 0.12 | 11/27 (NCI-H1792, HS-578T, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 7 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10459.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.602×** | -7.3 | 1e-10 | 22/28 (PANC-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.665×** | -5.9 | 1e-06 | 24/28 (PANC-1, LOX-IMVI, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.673×** | -5.7 | 2e-06 | 20/28 (NCI-H1792, A-427, …) | two highest doses | cell-cycle shift (explains ~13% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.683×** | -5.5 | 6e-06 | 23/28 (RPMI-7951, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.737×** | -4.4 | 0.001 | 19/28 (A-427, NCI-H1792, …) | two highest doses | cell-cycle shift (explains ~17% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.730×** | -4.4 | 0.001 | 17/28 (H4, HOP62, …) | rises with dose | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.732×** | -4.3 | 0.002 | 20/28 (PANC-1, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.744×** | -4.1 | 0.003 | 18/27 (RKO, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~24% of this change | **0.755×** | -3.9 | 0.006 | 17/27 (NCI-H460, A498, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.772×** | -3.7 | 0.010 | 19/28 (NCI-H1792, C32, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.773×** | -3.7 | 0.010 | 16/28 (A-427, NCI-H1792, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.780×** | -3.6 | 0.015 | 14/28 (LOX-IMVI, NCI-H460, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.653×** | -3.2 | 0.056 | 13/28 (LOX-IMVI, AN3 CA, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.864× | -3.0 | 0.11 | 7/28 (AN3 CA, SNU-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10459. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 487 | 0 | 12 (6 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.530× (z -18.9) ⚠ position not correctable · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.253× (z -11.6) |
| [[SNU-1 (line)]] | wt | 193 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.101× (z -21.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.326× (z -10.9) |
| [[LOX-IMVI (line)]] | wt | 217 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.430× (z -9.3) |
| [[NCI-H460 (line)]] | wt | 61.5 | 4 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 2.73× (z +15.2) | — |
| [[A-427 (line)]] | wt | 408 | 0 | 3 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.390× (z -11.7) ⚠ cell-cycle shift, explains ~23% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.406× (z -11.2) |
| [[AN3 CA (line)]] | alt | 418 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.229× (z -12.9) ⚠ cell-cycle shift, would explain all of this change |
| [[PANC-1 (line)]] | alt | 232 | 0 | 2 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.386× (z -10.3) |
| [[RKO (line)]] | wt | 44.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.40× (z +10.7) ⚠ toxic; transcription drop | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.178× (z -12.0) ⚠ toxic |
| [[SW480 (line)]] | alt | 65.8 | 2 | 0 | [[Tucidinostat (drug)]] 0.5 µM 2.16× (z +8.7) | — |
| [[C-33 A (line)]] | alt | 192 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.370× (z -9.2) |
| [[H4 (line)]] | wt | 96.0 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.198× (z -12.1) ⚠ cell-cycle shift, explains ~30% of this change |
| [[hTERT-HPNE (line)]] | wt | 201 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.340× (z -12.8) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H2030 (line)]] | alt | 220 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.380× (z -9.0) |
| [[NCI-H23 (line)]] | alt | 183 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.446× (z -8.9) |
| [[RPMI-7951 (line)]] | alt | 128 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.371× (z -8.5) ⚠ transcription drop |
| [[SW 1088 (line)]] | alt | 80.5 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.0660× (z -8.5) ⚠ cell-cycle shift, explains ~21% of this change |
| [[A-172 (line)]] | wt | 22.1 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 96.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 122 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 22.4 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 15.9 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 87.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.81 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 42.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.36 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 7.62 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 7.59 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 9.94 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 46.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 173 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.42 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 64.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.55 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 9.29 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 6.00 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.1 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 12.5 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 52.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.61 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 72.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 164 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.53 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 5.71 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 16.9 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 56.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 98.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 55.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 19.9 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 9.03 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10459), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GLIS3]] | +0.54 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[WNT5B]] | +0.53 | +0.55 / +0.45 | both halves | 3e-05 |  |
| [[MIR100HG]] | +0.53 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[DDAH1]] | +0.52 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[MPDZ]] | +0.51 | +0.46 / +0.52 | both halves | 2e-05 |  |
| [[MIR137HG]] | +0.51 | +0.50 / +0.46 | both halves | 3e-05 |  |
| [[KPNA4]] | +0.51 | +0.45 / +0.52 | both halves | 3e-05 |  |
| [[REEP3]] | +0.51 | +0.46 / +0.45 | both halves | 3e-05 |  |
| [[CLCN4]] | +0.50 | +0.37 / +0.48 | both halves | 8e-05 |  |
| [[EVC2]] | +0.50 | +0.51 / +0.44 | both halves | 3e-05 |  |
| [[SATB2]] | +0.49 | +0.48 / +0.37 | both halves | 9e-05 |  |
| [[MAP4K4]] | +0.49 | +0.37 / +0.48 | both halves | 7e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EMC2]] | -0.50 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[GOLPH3L]] | -0.48 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[PLEKHA2]] | -0.47 | -0.45 / -0.40 | both halves | 5e-05 |  |
| [[CFAP36]] | -0.45 | -0.32 / -0.44 | both halves | 2e-04 |  |
| [[DOK4]] | -0.45 | -0.41 / -0.33 | both halves | 1e-04 |  |
| [[ABCD4]] | -0.45 | -0.41 / -0.40 | both halves | 5e-05 |  |
| [[SLC25A14]] | -0.45 | -0.26 / -0.49 | both halves | 4e-04 |  |
| [[FIG4]] | -0.45 | -0.43 / -0.36 | both halves | 9e-05 |  |
| [[PIK3C2B]] | -0.45 | -0.46 / -0.41 | both halves | 4e-05 |  |
| [[LINC00674]] | -0.45 | -0.48 / -0.36 | both halves | 9e-05 |  |
| [[RAB20]] | -0.44 | -0.34 / -0.43 | both halves | 1e-04 |  |
| [[RASSF7]] | -0.44 | -0.41 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 2, C 9.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RAB20]] | B | RAB20 activity lowers MSRB3's level | lines that do not express RAB20 (8) vs lines expressing it (42) | 5.49× higher at baseline in the lines without RAB20 | 0.022 | ⚠ within organs, on part of the lines; also absent: RPS6KA2, PRDX2, YPEL3; maybe low, not absent |
| [[HEG1]] | B | HEG1 activity raises MSRB3's level | lines that do not express HEG1 (11) vs lines expressing it (39) | 5.24× lower at baseline in the lines without HEG1 | 0.029 | ⚠ within organs, on part of the lines; also absent: CCDC88A, STARD9, RECK |
| [[BNC2]] | C | BNC2 activity raises MSRB3's level | lines that do not express BNC2 (21) vs lines expressing it (29) | 4.76× lower at baseline in the lines without BNC2 | 7e-04 | ⚠ within organs, on part of the lines; also absent: LINC03041, DPY19L2, RNF182; co-absent with the target |
| [[TSHZ3-AS1]] | C | TSHZ3-AS1 activity raises MSRB3's level | lines that do not express TSHZ3-AS1 (25) vs lines expressing it (25) | 4.54× lower at baseline in the lines without TSHZ3-AS1 | 0.004 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ADAMTS18, TWIST2, INSYN2B; co-absent with the target |
| [[WNT5B]] | C | WNT5B activity raises MSRB3's level | lines that do not express WNT5B (22) vs lines expressing it (28) | 4.66× lower at baseline in the lines without WNT5B | 0.004 | ⚠ within organs, on part of the lines; also absent: DPY19L2, TRIML2, VASH1; co-absent with the target |
| [[LINC03041]] | C | LINC03041 activity raises MSRB3's level | lines that do not express LINC03041 (18) vs lines expressing it (32) | 4.81× lower at baseline in the lines without LINC03041 | 0.013 | ⚠ within organs, on part of the lines; also absent: BNC2, HECW2, ACTN2; maybe low, not absent; co-absent with the target |
| [[FAT4]] | C | FAT4 activity raises MSRB3's level | lines that do not express FAT4 (20) vs lines expressing it (30) | 4.00× lower at baseline in the lines without FAT4 | 0.020 | ⚠ within organs, on part of the lines; also absent: RFTN1, GPR176, GNG11; co-absent with the target |
| [[LINC00702]] | C | LINC00702 activity raises MSRB3's level | lines that do not express LINC00702 (25) vs lines expressing it (25) | 3.64× lower at baseline in the lines without LINC00702 | 0.020 | ⚠ within organs, on part of the lines; also absent: FGF5, ENSG00000253553, LNCOG; co-absent with the target |
| [[EVC2]] | C | EVC2 activity raises MSRB3's level | lines that do not express EVC2 (34) vs lines expressing it (16) | 4.54× lower at baseline in the lines without EVC2 | 0.024 | ⚠ within organs, on part of the lines; also absent: ENSG00000226043, LINC01242, ADGRG7; co-absent with the target |
| [[ANTXR1]] | C | ANTXR1 activity raises MSRB3's level | lines that do not express ANTXR1 (17) vs lines expressing it (33) | 5.52× lower at baseline in the lines without ANTXR1 | 0.028 | ⚠ within organs, on part of the lines; also absent: VASH1, RFLNB, ENSG00000285804; co-absent with the target |
| [[PAPPA]] | C | PAPPA activity raises MSRB3's level | lines that do not express PAPPA (33) vs lines expressing it (17) | 3.97× lower at baseline in the lines without PAPPA | 0.050 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HTRA3, MSC-AS1, PDGFRB; co-absent with the target |

### Downstream of this gene

*50 arrows, 50 of them with an alert ⚠; grade A 0, B 37, C 13. Shown: the 12 strongest; 38 more arrows (38 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HMGA2]] | B | MSRB3 activity raises HMGA2's level | lines that do not express MSRB3 (20) vs lines expressing it (30) | 3.03× lower at baseline in the lines without MSRB3 | 0.006 | ⚠ within organs, on part of the lines; also absent: ARHGEF6, KCNG1, FHL1 |
| [[HEG1]] | B | MSRB3 activity raises HEG1's level | lines that do not express MSRB3 (20) vs lines expressing it (30) | 3.18× lower at baseline in the lines without MSRB3 | 0.011 | ⚠ within organs, on part of the lines; also absent: ARHGEF6, KCNG1, FHL1 |
| [[HMGA2-AS1]] | B | MSRB3 activity raises HMGA2-AS1's level | lines that do not express MSRB3 (20) vs lines expressing it (30) | 1.51× lower at baseline in the lines without MSRB3 | 0.013 | ⚠ within organs, on part of the lines; also absent: ARHGEF6, KCNG1, FHL1 |
| [[TTC22]] | B | MSRB3 activity lowers TTC22's level | lines that do not express MSRB3 (20) vs lines expressing it (30) | 2.84× higher at baseline in the lines without MSRB3 | 0.015 | ⚠ within organs, on part of the lines; also absent: ARHGEF6, KCNG1, FHL1 |
| [[RASSF7]] | B | MSRB3 activity lowers RASSF7's level | lines that do not express MSRB3 (20) vs lines expressing it (30) | 2.27× higher at baseline in the lines without MSRB3 | 0.016 | ⚠ within organs, on part of the lines; also absent: ARHGEF6, KCNG1, FHL1 |
| cells under [[Vinblastine (sulfate) (drug)]] 0.5 µM | B | MSRB3 activity lowers the cells' numbers under Vinblastine (sulfate) 0.5 µM (makes them more sensitive) | lines that do not express MSRB3 (20) vs lines expressing it (28) | the lines without MSRB3: 1.29× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: ARHGEF6, KCNG1, FHL1 |
| cells under [[Vinblastine (sulfate) (drug)]] 5 µM | B | MSRB3 activity lowers the cells' numbers under Vinblastine (sulfate) 5 µM (makes them more sensitive) | lines that do not express MSRB3 (20) vs lines expressing it (28) | the lines without MSRB3: 1.21× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: ARHGEF6, KCNG1, FHL1 |
| cells under [[Berbamine (dihydrochloride) (drug)]] 0.5 µM | B | MSRB3 activity raises the cells' numbers under Berbamine (dihydrochloride) 0.5 µM (protects the cells) | lines that do not express MSRB3 (20) vs lines expressing it (28) | the lines without MSRB3: 0.85× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: ARHGEF6, KCNG1, FHL1 |
| [[PTPN14]] | B | MSRB3 activity raises PTPN14's level | lines that do not express MSRB3 (20) vs lines expressing it (30) | 1.59× lower at baseline in the lines without MSRB3 | 0.029 | ⚠ within organs, on part of the lines; also absent: ARHGEF6, KCNG1, FHL1 |
| [[KLHL5]] | B | MSRB3 activity raises KLHL5's level | lines that do not express MSRB3 (20) vs lines expressing it (30) | 2.58× lower at baseline in the lines without MSRB3 | 0.031 | ⚠ within organs, on part of the lines; also absent: ARHGEF6, KCNG1, FHL1 |
| cells under [[Peretinoin (drug)]] 0.5 µM | B | MSRB3 activity lowers the cells' numbers under Peretinoin 0.5 µM (makes them more sensitive) | lines that do not express MSRB3 (20) vs lines expressing it (28) | the lines without MSRB3: 1.42× the cells of the other lines | 0.033 | ⚠ within organs, on part of the lines; also absent: ARHGEF6, KCNG1, FHL1 |
| [[CDK18]] | B | MSRB3 activity lowers CDK18's level | lines that do not express MSRB3 (20) vs lines expressing it (30) | 2.01× higher at baseline in the lines without MSRB3 | 0.034 | ⚠ within organs, on part of the lines; also absent: ARHGEF6, KCNG1, FHL1 |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.330). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (55.4, 14.3); signed map (18.1, 42.1). **Vector** length 93.9, 29.6% of its response variance represented; |z| ≥ 3 in 721 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.2 | +6.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.2 | +9.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.9 | +0.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +4.8 | +0.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.7 | +1.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.2 | +2.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.5 | +1.4 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.2 | +3.5 |
| fall | [[Radotinib (drug)]] 5 µM |  | -2.8 | -2.5 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -2.2 | -4.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.2 | -3.7 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | -1.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.1 | -7.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.0 | -5.9 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.9 | -2.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.8 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | methionine sulfoxide reductase B3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q14.3 — chr12:65,278,643-65,491,430 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ36866, DKFZp686C1178; previously DFNB74 |
| Gene groups (HGNC) | Methionine sulfoxide reductases |
| Reactome | 1 pathways, smallest: Protein repair |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IXL7](https://www.uniprot.org/uniprotkb/Q8IXL7) (Methionine-R-sulfoxide reductase B3):

> Catalyzes the reduction of free and protein-bound methionine sulfoxide to methionine. Isoform 2 is essential for hearing.

**Summary**, from NCBI Gene [253827](https://www.ncbi.nlm.nih.gov/gene/253827):

> The protein encoded by this gene catalyzes the reduction of methionine sulfoxide to methionine. This enzyme acts as a monomer and requires zinc as a cofactor. Several transcript variants encoding two different isoforms have been found for this gene. One of the isoforms localizes to mitochondria while the other localizes to endoplasmic reticula. [provided by RefSeq, Jul 2010]

**Accessions** — [HGNC:27375](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27375) · Entrez [253827](https://www.ncbi.nlm.nih.gov/gene/253827) · UniProt [Q8IXL7](https://www.uniprot.org/uniprotkb/Q8IXL7) · Ensembl [ENSG00000174099](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000174099)

## Data

Gene col 10459: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10459); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10459, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10459]; `tensor/DDL_lfc|DDL_z.npy` [10459]; `embed/gene_vectors.npy` [10459]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10459 or target_col == 10459). Every well: [[MSRB3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MSRB3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
