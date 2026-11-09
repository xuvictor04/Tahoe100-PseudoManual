---
symbol: "TMEM145"
type: "gene"
col: 9502
ensembl_id: "ENSG00000167619"
name: "transmembrane protein 145"
location: "19q13.2"
module: 103
arm: "+"
pooled_cpm: 2.58
n_lines_expressing: 39
n_dd_up: 15
n_dd_down: 1
n_dd_up_clean: 10
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 5
direction_downstream: 12
tags: ["gene", "module/103"]
generated_by: "tahoemap"
---

# TMEM145

*transmembrane protein 145* — 19q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.34× (z +7.6, q 1e-11, up in 0 of 1 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.61× (z +6.3, q 4e-08, up in 11 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.616× (z -4.5, q 0.003, down in 13 of 23 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (HOP62 0.0801×; ⚠ toxic; cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (HOP62 0.195×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (RKO 0.1000×); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (HOP62 0.126×); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (HOP62 0.292×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ABCB9]] (+0.62, fdr 9e-06), [[MPP2]] (+0.60, fdr 1e-05), [[FOXO6]] (+0.59, fdr 2e-05); moves opposite to [[SH3D19]] (-0.48, fdr 3e-05), [[ENOX2]] (-0.48, fdr 4e-05), [[ARHGEF28]] (-0.45, fdr 5e-05).
> It is in [[Module 103]], a single-armed module (glycolysis).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[BCL11B]] → it (grade B ⚠); 12 go from it, the strongest it → [[DLG4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 5 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9502.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.34×** | +7.6 | 1e-11 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.14×** | +6.8 | 3e-09 | 1/8 (SW480) | inconsistent across doses | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.10×** | +6.4 | 2e-08 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.98×** | +6.4 | 2e-08 | 4/12 (NCI-H2030, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.61×** | +6.3 | 4e-08 | 11/33 (NCI-H460, HEC-1-A, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.88×** | +5.9 | 3e-07 | 8/32 (HEC-1-A, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.65×** | +4.7 | 3e-04 | 5/27 (LoVo, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.52×** | +3.9 | 0.006 | 4/30 (HEC-1-A, NCI-H460, …) | all doses, stronger at high dose | position effect removed |
| [[Thymol (drug)]] 0.5 µM |  | **1.48×** | +3.7 | 0.016 | 1/16 (SW480) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.05 µM |  | **1.49×** | +3.5 | 0.023 | 1/28 (SHP-77) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.45×** | +3.5 | 0.026 | 4/30 (A-427, HOP62, …) | inconsistent across doses |  |
| [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.5 µM |  | **1.43×** | +3.3 | 0.041 | 1/23 (NCI-H2030) | inconsistent across doses |  |
| [[Cepharanthine (drug)]] 5 µM |  | **1.27×** | +3.1 | 0.078 | 2/30 (C32, HOP62) | top dose only | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.39×** | +3.1 | 0.082 | 1/25 (SHP-77) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.58×** | +3.0 | 0.088 | 0/15 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9502.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (HOP62 0.0801×; ⚠ toxic; cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (HOP62 0.195×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (RKO 0.1000×); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (HOP62 0.126×); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (HOP62 0.292×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.616×** | -4.5 | 0.003 | 13/23 (RKO, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 5 µM |  | 0.686× | -3.4 | 0.19 | 10/27 (NCI-H1792, C32, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9502. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 13.7 | 0 | 4 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0801× (z -12.8) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.126× (z -10.5) |
| [[RKO (line)]] | wt | 14.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.1000× (z -11.6) |
| [[A-172 (line)]] | wt | 0.734 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.90 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.325 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.49 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.263 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.598 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 6.34 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.20 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.75 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.298 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.09 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.857 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.48 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.473 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.625 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.584 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.53 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.339 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.70 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.88 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.477 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.688 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.08 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.379 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.764 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.315 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.51 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.832 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.06 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.02 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.914 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.94 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9502), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABCB9]] | +0.62 | +0.57 / +0.61 | both halves | 9e-06 |  |
| [[MPP2]] | +0.60 | +0.63 / +0.57 | both halves | 1e-05 |  |
| [[FOXO6]] | +0.59 | +0.46 / +0.52 | both halves | 2e-05 |  |
| [[GNA15]] | +0.59 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[COL6A2]] | +0.56 | +0.51 / +0.45 | both halves | 3e-05 |  |
| [[PFKFB4]] | +0.55 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[SLC26A6]] | +0.55 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[TMEM39B]] | +0.54 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[SLC29A4]] | +0.54 | +0.44 / +0.55 | both halves | 3e-05 |  |
| [[SMARCD3]] | +0.54 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[NDNF]] | +0.53 | +0.41 / +0.56 | both halves | 4e-05 |  |
| [[JAG2]] | +0.53 | +0.48 / +0.50 | both halves | 2e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SH3D19]] | -0.48 | -0.45 / -0.43 | both halves | 3e-05 |  |
| [[ENOX2]] | -0.48 | -0.44 / -0.41 | both halves | 4e-05 |  |
| [[ARHGEF28]] | -0.45 | -0.44 / -0.39 | both halves | 5e-05 |  |
| [[TRAPPC8]] | -0.44 | -0.25 / -0.52 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 3, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BCL11B]] | B | BCL11B activity lowers TMEM145's level | lines that do not express BCL11B (18) vs lines expressing it (32) | 1.35× higher at baseline in the lines without BCL11B | 0.022 | ⚠ within organs, on part of the lines; also absent: ENSG00000249111, HLA-V-1, ENSG00000272297; maybe low, not absent |
| [[PLEKHG4B]] | B | PLEKHG4B activity raises TMEM145's level | lines that do not express PLEKHG4B (27) vs lines expressing it (23) | 1.71× lower at baseline in the lines without PLEKHG4B | 0.079 | ⚠ within organs, on part of the lines; also absent: CHST8, SNAP91, JAKMIP1 |
| [[ITGA11]] | B | ITGA11 activity raises TMEM145's level | lines that do not express ITGA11 (34) vs lines expressing it (16) | 1.48× lower at baseline in the lines without ITGA11 | 0.088 | ⚠ within organs, on part of the lines; also absent: GYPC, INSYN2B, LINC01411 |
| [[SLC17A7]] | C | SLC17A7 activity raises TMEM145's level | lines that do not express SLC17A7 (9) vs lines expressing it (41) | 2.00× lower at baseline in the lines without SLC17A7 | 0.066 | ⚠ within organs, on part of the lines; also absent: GXYLT2, ITGA10, NT5M; maybe low, not absent; co-absent with the target |
| [[SH3D19]] | C | SH3D19 activity lowers TMEM145's level | lines that do not express SH3D19 (3) vs lines expressing it (47) | 3.06× higher at baseline in the lines without SH3D19 | 0.067 | ⚠ few lines (3 vs 47); across organs; also absent: HPS1, APOBEC3B; maybe low, not absent |

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 12, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DLG4]] | B | TMEM145 activity raises DLG4's level | lines that do not express TMEM145 (11) vs lines expressing it (39) | 2.42× lower at baseline in the lines without TMEM145 | 0.024 | ⚠ within organs, on part of the lines; also absent: GXYLT2, KCNK13, DLX1 |
| [[MPP2]] | B | TMEM145 activity raises MPP2's level | lines that do not express TMEM145 (11) vs lines expressing it (39) | 3.06× lower at baseline in the lines without TMEM145 | 0.028 | ⚠ within organs, on part of the lines; also absent: GXYLT2, KCNK13, DLX1 |
| [[DHRS13]] | B | TMEM145 activity raises DHRS13's level | lines that do not express TMEM145 (11) vs lines expressing it (39) | 1.61× lower at baseline in the lines without TMEM145 | 0.034 | ⚠ within organs, on part of the lines; also absent: GXYLT2, KCNK13, DLX1 |
| [[CHSY1]] | B | TMEM145 activity raises CHSY1's level | lines that do not express TMEM145 (11) vs lines expressing it (39) | 1.99× lower at baseline in the lines without TMEM145 | 0.046 | ⚠ within organs, on part of the lines; also absent: GXYLT2, KCNK13, DLX1 |
| [[FAM234B]] | B | TMEM145 activity raises FAM234B's level | lines that do not express TMEM145 (11) vs lines expressing it (39) | 2.13× lower at baseline in the lines without TMEM145 | 0.048 | ⚠ within organs, on part of the lines; also absent: GXYLT2, KCNK13, DLX1 |
| [[UPK1A-AS1]] | B | TMEM145 activity raises UPK1A-AS1's level | lines that do not express TMEM145 (11) vs lines expressing it (39) | 2.48× lower at baseline in the lines without TMEM145 | 0.061 | ⚠ within organs, on part of the lines; also absent: GXYLT2, KCNK13, DLX1 |
| [[ZNRF1]] | B | TMEM145 activity raises ZNRF1's level | lines that do not express TMEM145 (11) vs lines expressing it (39) | 1.57× lower at baseline in the lines without TMEM145 | 0.062 | ⚠ within organs, on part of the lines; also absent: GXYLT2, KCNK13, DLX1 |
| [[CELF5]] | B | TMEM145 activity raises CELF5's level | lines that do not express TMEM145 (11) vs lines expressing it (39) | 1.52× lower at baseline in the lines without TMEM145 | 0.069 | ⚠ within organs, on part of the lines; also absent: GXYLT2, KCNK13, DLX1 |
| [[SMARCD3]] | B | TMEM145 activity raises SMARCD3's level | lines that do not express TMEM145 (11) vs lines expressing it (39) | 2.10× lower at baseline in the lines without TMEM145 | 0.071 | ⚠ within organs, on part of the lines; also absent: GXYLT2, KCNK13, DLX1 |
| [[TRIM9]] | B | TMEM145 activity raises TRIM9's level | lines that do not express TMEM145 (11) vs lines expressing it (39) | 3.71× lower at baseline in the lines without TMEM145 | 0.074 | ⚠ within organs, on part of the lines; also absent: GXYLT2, KCNK13, DLX1 |
| [[POM121C]] | B | TMEM145 activity raises POM121C's level | lines that do not express TMEM145 (11) vs lines expressing it (39) | 1.33× lower at baseline in the lines without TMEM145 | 0.083 | ⚠ within organs, on part of the lines; also absent: GXYLT2, KCNK13, DLX1 |
| [[AHDC1]] | B | TMEM145 activity lowers AHDC1's level | lines that do not express TMEM145 (11) vs lines expressing it (39) | 1.40× higher at baseline in the lines without TMEM145 | 0.099 | ⚠ within organs, on part of the lines; also absent: GXYLT2, KCNK13, DLX1 |

## Where it sits

- **Module**: [[Module 103]] — glycolysis; 45 genes; every member is in the + arm (projection on the module's main direction 0.580). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (9.3, -3.3); signed map (-6.8, 48.0). **Vector** length 42.6, 6.14% of its response variance represented; |z| ≥ 3 in 736 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | +6.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.0 | +4.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | +1.9 | +5.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +1.9 | +3.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.8 | +7.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.7 | +3.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.4 | +1.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.8 | +3.0 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +0.8 | +2.4 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -1.4 | -3.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | -1.3 | -1.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -1.2 | -4.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.2 | -1.3 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | -1.1 | -0.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.1 | -1.5 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -1.1 | -1.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.0 | -2.0 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.0 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 145 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.2 — chr19:42,313,309-42,325,064 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ90805 |
| Matched by | ensembl_id |

UniProt [Q8NBT3](https://www.uniprot.org/uniprotkb/Q8NBT3) carries no function annotation.

**Summary**, from NCBI Gene [284339](https://www.ncbi.nlm.nih.gov/gene/284339):

> Predicted to be involved in G protein-coupled receptor signaling pathway and response to pheromone. Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26912](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26912) · Entrez [284339](https://www.ncbi.nlm.nih.gov/gene/284339) · UniProt [Q8NBT3](https://www.uniprot.org/uniprotkb/Q8NBT3) · Ensembl [ENSG00000167619](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167619)

## Data

Gene col 9502: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9502); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9502, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9502]; `tensor/DDL_lfc|DDL_z.npy` [9502]; `embed/gene_vectors.npy` [9502]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9502 or target_col == 9502). Every well: [[TMEM145 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM145.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
