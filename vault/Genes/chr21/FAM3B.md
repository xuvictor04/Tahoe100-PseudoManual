---
symbol: "FAM3B"
type: "gene"
col: 11464
ensembl_id: "ENSG00000183844"
name: "FAM3 metabolism regulating signaling molecule B"
location: "21q22.3"
module: 47
arm: "+"
pooled_cpm: 2.66
n_lines_expressing: 38
n_dd_up: 6
n_dd_down: 12
n_dd_up_clean: 1
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 24
direction_downstream: 7
tags: ["gene", "module/047"]
generated_by: "tahoemap"
---

# FAM3B

*FAM3 metabolism regulating signaling molecule B* — 21q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.14× (z +12.2, q 2e-31, up in 0 of 1 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 2.40× (z +7.8, q 2e-12, up in 11 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.475× (z -6.7, q 1e-08, down in 17 of 25 measured lines).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PLEKHS1]] (+0.62, fdr 1e-05), [[PTPN22]] (+0.59, fdr 3e-05), [[BCAR3-AS1]] (+0.58, fdr 3e-05); moves opposite to [[WASHC4]] (-0.49, fdr 4e-05), [[FBXL5]] (-0.47, fdr 2e-04), [[DMTF1]] (-0.46, fdr 4e-05).
> It is in [[Module 047]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 24 arrows point to it, the strongest [[PLA2G2A]] → it (grade B ⚠); 7 go from it, the strongest it → [[EPHA1-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 5 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11464.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.14×** | +12.2 | 2e-31 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.40×** | +7.8 | 2e-12 | 11/29 (C32, SK-MEL-2, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.16×** | +6.9 | 1e-09 | 0/6 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.69×** | +6.2 | 8e-08 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.46×** | +4.2 | 0.003 | 0/0 | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.49×** | +3.4 | 0.058 | 0/7 | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 1.41× | +3.0 | 0.20 | 3/28 (SW480, A-172, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11464.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.475×** | -6.7 | 1e-08 | 17/25 (COLO 205, KATO III, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.600×** | -6.5 | 2e-08 | 21/26 (COLO 205, KATO III, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.540×** | -5.5 | 6e-06 | 18/34 (LoVo, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.537×** | -5.4 | 1e-05 | 13/29 (COLO 205, BT-474, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.556×** | -5.3 | 2e-05 | 14/33 (COLO 205, KATO III, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.582×** | -4.9 | 1e-04 | 13/32 (LOX-IMVI, COLO 205, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.600×** | -4.5 | 5e-04 | 9/33 (COLO 205, BT-474, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.608×** | -4.5 | 5e-04 | 13/34 (COLO 205, KATO III, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.616×** | -4.4 | 8e-04 | 9/34 (SW48, C32, …) | top dose only |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **0.632×** | -4.0 | 0.004 | 5/34 (RKO, BT-474, …) | top dose only | plate-row cell shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.644×** | -3.9 | 0.005 | 12/29 (KATO III, NCI-H1573, …) | two highest doses |  |
| [[Resveratrol (drug)]] 5 µM |  | **0.776×** | -3.2 | 0.056 | 3/32 (C32, Panc 03.27, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.27 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11464. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 63.6 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.112× (z -22.3) |
| [[BT-474 (line)]] | alt | 26.0 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.147× (z -10.6) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.299× (z -9.6) |
| [[KATO III (line)]] | alt | 9.05 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.129× (z -13.4) |
| [[LS 180 (line)]] | wt | 1.62 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0641× (z -8.9) |
| [[NCI-H1573 (line)]] | alt | 2.45 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0806× (z -8.6) |
| [[A-172 (line)]] | wt | 1.80 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.480 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.872 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.662 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.545 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.337 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.75 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.818 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.405 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 4.52 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.702 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.304 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 5.19 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.871 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.19 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.839 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.37 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.44 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.06 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.370 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.695 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.402 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 5.96 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.479 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.283 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.04 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.398 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.391 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.11 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.02 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.665 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.36 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.87 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11464), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLEKHS1]] | +0.62 | +0.64 / +0.52 | both halves | 1e-05 | **novel candidate** |
| [[PTPN22]] | +0.59 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[BCAR3-AS1]] | +0.58 | +0.45 / +0.60 | both halves | 3e-05 |  |
| [[MUC20]] | +0.55 | +0.38 / +0.61 | both halves | 6e-05 |  |
| [[ZNF503-AS1]] | +0.54 | +0.50 / +0.45 | both halves | 3e-05 |  |
| [[MINAR1]] | +0.52 | +0.37 / +0.59 | both halves | 7e-05 |  |
| [[MYO18B]] | +0.51 | +0.37 / +0.52 | both halves | 8e-05 |  |
| [[CATSPERB]] | +0.51 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[HSD17B2-AS1]] | +0.50 | +0.32 / +0.56 | both halves | 2e-04 |  |
| [[TUBA8]] | +0.50 | +0.38 / +0.53 | both halves | 6e-05 |  |
| [[SPON2]] | +0.49 | +0.44 / +0.44 | both halves | 3e-05 |  |
| [[MYO7A]] | +0.49 | +0.35 / +0.50 | both halves | 1e-04 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WASHC4]] | -0.49 | -0.46 / -0.41 | both halves | 4e-05 |  |
| [[FBXL5]] | -0.47 | -0.30 / -0.49 | both halves | 2e-04 |  |
| [[DMTF1]] | -0.46 | -0.44 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*24 arrows, 24 of them with an alert ⚠; grade A 0, B 24, C 0. Shown: the 12 strongest; 12 more arrows (12 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLA2G2A]] | B | PLA2G2A activity raises FAM3B's level | lines that do not express PLA2G2A (41) vs lines expressing it (9) | 3.34× lower at baseline in the lines without PLA2G2A | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, ENSG00000248588, CALB1 |
| [[TOX3]] | B | TOX3 activity raises FAM3B's level | lines that do not express TOX3 (31) vs lines expressing it (19) | 2.08× lower at baseline in the lines without TOX3 | 0.019 | ⚠ within organs, on part of the lines; also absent: GPX2, ENSG00000287426, TMEM45B |
| [[PRR15]] | B | PRR15 activity raises FAM3B's level | lines that do not express PRR15 (28) vs lines expressing it (22) | 1.66× lower at baseline in the lines without PRR15 | 0.025 | ⚠ within organs, on part of the lines; also absent: PRR15-DT, RNF223, FAM110C |
| [[CYP4F3]] | B | CYP4F3 activity raises FAM3B's level | lines that do not express CYP4F3 (29) vs lines expressing it (21) | 1.82× lower at baseline in the lines without CYP4F3 | 0.047 | ⚠ within organs, on part of the lines; also absent: P2RY2, CYP3A5, ITGB6 |
| [[PROM1]] | B | PROM1 activity raises FAM3B's level | lines that do not express PROM1 (37) vs lines expressing it (13) | 2.04× lower at baseline in the lines without PROM1 | 0.048 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: AZGP1, KRT23, GJB1 |
| [[LINC00299]] | B | LINC00299 activity raises FAM3B's level | lines that do not express LINC00299 (27) vs lines expressing it (23) | 1.85× lower at baseline in the lines without LINC00299 | 0.055 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LINC01814, TNNT2, ATP2C2 |
| [[AGR3]] | B | AGR3 activity raises FAM3B's level | lines that do not express AGR3 (42) vs lines expressing it (8) | 3.02× lower at baseline in the lines without AGR3 | 0.059 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGFR2, GABRP, MUC17 |
| [[LINC01819]] | B | LINC01819 activity raises FAM3B's level | lines that do not express LINC01819 (29) vs lines expressing it (21) | 1.66× lower at baseline in the lines without LINC01819 | 0.061 | ⚠ within organs, on part of the lines; also absent: MOGAT3, LGR6, A1CF; maybe low, not absent |
| [[ST6GALNAC1]] | B | ST6GALNAC1 activity raises FAM3B's level | lines that do not express ST6GALNAC1 (37) vs lines expressing it (13) | 1.79× lower at baseline in the lines without ST6GALNAC1 | 0.063 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC6A14, SLC44A4, STEAP4 |
| [[LINC02331]] | B | LINC02331 activity raises FAM3B's level | lines that do not express LINC02331 (30) vs lines expressing it (20) | 1.62× lower at baseline in the lines without LINC02331 | 0.069 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KDF1, EPS8L3, LCN2 |
| [[CYP4F12]] | B | CYP4F12 activity raises FAM3B's level | lines that do not express CYP4F12 (32) vs lines expressing it (18) | 1.89× lower at baseline in the lines without CYP4F12 | 0.070 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FXYD3, CDH17, MUC13 |
| [[PRR15L]] | B | PRR15L activity raises FAM3B's level | lines that do not express PRR15L (38) vs lines expressing it (12) | 2.34× lower at baseline in the lines without PRR15L | 0.071 | ⚠ within organs, on part of the lines; co-occurs with TP53, CDKN2A; also absent: TMEM30B, CDH17, ENSG00000267881 |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPHA1-AS1]] | B | FAM3B activity raises EPHA1-AS1's level | lines that do not express FAM3B (12) vs lines expressing it (38) | 1.58× lower at baseline in the lines without FAM3B | 0.032 | ⚠ within organs, on part of the lines; also absent: TXNIP, CADPS2, PLAC4; maybe low, not absent |
| [[PRR15]] | B | FAM3B activity raises PRR15's level | lines that do not express FAM3B (12) vs lines expressing it (38) | 1.94× lower at baseline in the lines without FAM3B | 0.050 | ⚠ within organs, on part of the lines; also absent: TXNIP, CADPS2, PLAC4; maybe low, not absent |
| [[GABRR2]] | B | FAM3B activity raises GABRR2's level | lines that do not express FAM3B (12) vs lines expressing it (38) | 1.43× lower at baseline in the lines without FAM3B | 0.056 | ⚠ within organs, on part of the lines; also absent: TXNIP, CADPS2, PLAC4; maybe low, not absent |
| [[IMPA1P1]] | B | FAM3B activity raises IMPA1P1's level | lines that do not express FAM3B (12) vs lines expressing it (38) | 1.26× lower at baseline in the lines without FAM3B | 0.087 | ⚠ within organs, on part of the lines; also absent: TXNIP, CADPS2, PLAC4; maybe low, not absent |
| [[GNA14]] | B | FAM3B activity raises GNA14's level | lines that do not express FAM3B (12) vs lines expressing it (38) | 1.40× lower at baseline in the lines without FAM3B | 0.088 | ⚠ within organs, on part of the lines; also absent: TXNIP, CADPS2, PLAC4; maybe low, not absent |
| [[UCKL1-AS1]] | B | FAM3B activity raises UCKL1-AS1's level | lines that do not express FAM3B (12) vs lines expressing it (38) | 1.51× lower at baseline in the lines without FAM3B | 0.090 | ⚠ within organs, on part of the lines; also absent: TXNIP, CADPS2, PLAC4; maybe low, not absent |
| cells under [[Sapanisertib (drug)]] 0.5 µM | B | FAM3B activity lowers the cells' numbers under Sapanisertib 0.5 µM (makes them more sensitive) | lines that do not express FAM3B (12) vs lines expressing it (36) | the lines without FAM3B: 1.25× the cells of the other lines | 0.093 | ⚠ within organs, on part of the lines; also absent: TXNIP, CADPS2, PLAC4; maybe low, not absent |

## Where it sits

- **Module**: [[Module 047]]; 95 genes; every member is in the + arm (projection on the module's main direction 0.438). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (29.0, 56.8); signed map (66.6, 1.2). **Vector** length 38.5, 5.04% of its response variance represented; |z| ≥ 3 in 791 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.6 | +6.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.6 | +7.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.5 | +12.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.1 | +6.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.8 | +2.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.0 | +0.1 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.0 | +3.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +0.9 | +0.7 |
| fall | [[Radotinib (drug)]] 5 µM |  | -1.4 | -1.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -1.3 | -6.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.3 | -4.4 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -1.2 | -3.9 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.2 | -2.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.1 | -2.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.1 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | FAM3 metabolism regulating signaling molecule B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q22.3 — chr21:41,304,212-41,357,727 (+) |
| Ensembl biotype | protein_coding |
| Also known as | D21M16SJHU19e, PRED44, 2-21, ORF9, C21orf76, PANDER; previously C21orf11 |
| Matched by | ensembl_id |

**Function**, from UniProt [P58499](https://www.uniprot.org/uniprotkb/P58499) (Protein FAM3B):

> Induces apoptosis of alpha and beta cells in a dose- and time-dependent manner.

**Summary**, from NCBI Gene [54097](https://www.ncbi.nlm.nih.gov/gene/54097):

> Predicted to enable cytokine activity. Involved in insulin secretion. Located in extracellular exosome. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:1253](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1253) · Entrez [54097](https://www.ncbi.nlm.nih.gov/gene/54097) · UniProt [P58499](https://www.uniprot.org/uniprotkb/P58499) · Ensembl [ENSG00000183844](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183844)

## Data

Gene col 11464: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11464); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11464, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11464]; `tensor/DDL_lfc|DDL_z.npy` [11464]; `embed/gene_vectors.npy` [11464]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11464 or target_col == 11464). Every well: [[FAM3B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM3B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
