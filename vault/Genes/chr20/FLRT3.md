---
symbol: "FLRT3"
type: "gene"
col: 4678
ensembl_id: "ENSG00000125848"
name: "fibronectin leucine rich transmembrane protein 3"
location: "20p12.1"
module: 155
arm: "+"
pooled_cpm: 4.82
n_lines_expressing: 29
n_dd_up: 15
n_dd_down: 4
n_dd_up_clean: 12
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 23
direction_downstream: 33
tags: ["gene", "module/155"]
generated_by: "tahoemap"
---

# FLRT3

*fibronectin leucine rich transmembrane protein 3* — 20p12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.32× (z +7.2, q 3e-10, up in 2 of 9 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.58× (z +5.8, q 2e-06, up in 6 of 25 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.658× (z -5.3, q 7e-05, down in 16 of 21 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SERPINB4]] (+0.69, fdr 7e-06), [[SERPINB3]] (+0.69, fdr 7e-06), [[TMC5]] (+0.68, fdr 7e-06).
> It is in [[Module 155]], a single-armed module (MyD88 deficiency (TLR2/4)).
> Probable direction (from the cell lines, not proof of direct regulation): 23 arrows point to it, the strongest [[LGALS9]] → it (grade B ⚠); 33 go from it, the strongest it → [[ELF3-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 3 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4678.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.32×** | +7.2 | 3e-10 | 2/9 (HS-578T, NCI-H2347) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.58×** | +5.8 | 2e-06 | 6/25 (HEC-1-A, C32, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.57×** | +5.7 | 2e-06 | 9/27 (SK-MEL-2, LS 180, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.54×** | +5.5 | 7e-06 | 9/27 (hTERT-HPNE, LS 180, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.59×** | +5.1 | 4e-05 | 14/27 (HEC-1-A, NCI-H2030, …) | all doses, flat | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.76×** | +4.7 | 3e-04 | 0/12 | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **1.59×** | +4.0 | 0.005 | 7/24 (C32, CFPAC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.56×** | +4.0 | 0.005 | 4/24 (LS 180, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.51×** | +3.7 | 0.016 | 7/26 (HEC-1-A, NCI-H2030, …) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.47×** | +3.4 | 0.033 | 5/27 (NCI-H2030, HEC-1-A, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.49×** | +3.4 | 0.033 | 5/16 (HEC-1-A, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.45×** | +3.4 | 0.037 | 7/27 (CFPAC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.49×** | +3.3 | 0.045 | 4/22 (NCI-H460, AsPC-1, …) | inconsistent across doses | low cells (technical?) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.62×** | +3.1 | 0.088 | 1/16 (HEC-1-A) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.28×** | +3.0 | 0.093 | 9/27 (HEC-1-A, NCI-H460, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4678.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.658×** | -5.3 | 7e-05 | 16/21 (AsPC-1, BT-474, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.659×** | -3.5 | 0.085 | 11/24 (COLO 205, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.678×** | -3.5 | 0.085 | 15/27 (BT-474, COLO 205, …) | top dose only | cell-cycle shift (explains ~2% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.670×** | -3.4 | 0.085 | 15/23 (BT-474, C32, …) | top dose only | cell-cycle shift (explains ~11% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4678. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 26.6 | 0 | 22 (3 ⚠) | — | [[Neratinib (drug)]] 0.05 µM 0.0219× (z -12.4) |
| [[AsPC-1 (line)]] | alt | 44.0 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.106× (z -16.1) |
| [[HT-29 (line)]] | alt | 21.1 | 0 | 3 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0436× (z -13.2) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.114× (z -9.5) |
| [[CFPAC-1 (line)]] | alt | 10.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0992× (z -9.0) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 9.10 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0506× (z -13.5) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 12.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.116× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 4.70 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.157× (z -8.7) |
| [[A-172 (line)]] | wt | 2.19 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.505 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.680 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 6.71 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.831 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.610 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 6.21 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.46 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.90 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.625 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 4.84 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.601 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.821 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.73 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.88 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.887 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 5.96 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.490 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.267 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 6.96 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 3.97 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.35 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.660 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.419 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.478 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.577 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.598 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.896 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.594 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.07 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.541 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4678), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SERPINB4]] | +0.69 | +0.68 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[SERPINB3]] | +0.69 | +0.67 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[TMC5]] | +0.68 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[FGB]] | +0.67 | +0.67 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[S100A9]] | +0.66 | +0.61 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[TMEM45B]] | +0.66 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[TCIM]] | +0.65 | +0.62 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[S100A8]] | +0.64 | +0.57 / +0.67 | both halves | 1e-05 |  |
| [[ITGB6]] | +0.63 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[RGS6]] | +0.63 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[CEACAM5]] | +0.63 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[IL1RN]] | +0.62 | +0.64 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*23 arrows, 23 of them with an alert ⚠; grade A 0, B 5, C 18. Shown: the 12 strongest; 11 more arrows (11 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LGALS9]] | B | LGALS9 activity raises FLRT3's level | lines that do not express LGALS9 (13) vs lines expressing it (37) | 2.05× lower at baseline in the lines without LGALS9 | 0.050 | ⚠ within organs, on part of the lines; also absent: NMRAL2P-1, ATP8B1, CTSS; maybe low, not absent |
| [[PDZK1IP1]] | B | PDZK1IP1 activity raises FLRT3's level | lines that do not express PDZK1IP1 (32) vs lines expressing it (18) | 2.18× lower at baseline in the lines without PDZK1IP1 | 0.079 | ⚠ within organs, on part of the lines; also absent: MUC5B, UCA1, PRSS8 |
| [[LINC01559]] | B | LINC01559 activity raises FLRT3's level | lines that do not express LINC01559 (38) vs lines expressing it (12) | 2.24× lower at baseline in the lines without LINC01559 | 0.079 | ⚠ within organs, on part of the lines; also absent: CLRN3, NPSR1, CDH17 |
| [[NTN4]] | B | NTN4 activity raises FLRT3's level | lines that do not express NTN4 (18) vs lines expressing it (32) | 1.70× lower at baseline in the lines without NTN4 | 0.083 | ⚠ within organs, on part of the lines; also absent: TNFAIP2, LINC02057, BMP2 |
| [[KLF5]] | B | KLF5 activity raises FLRT3's level | lines that do not express KLF5 (18) vs lines expressing it (32) | 1.93× lower at baseline in the lines without KLF5 | 0.098 | ⚠ within organs, on part of the lines; also absent: LAMA3, IFNLR1, NCMAP; maybe low, not absent |
| [[MUC13]] | C | MUC13 activity raises FLRT3's level | lines that do not express MUC13 (40) vs lines expressing it (10) | 3.48× lower at baseline in the lines without MUC13 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, NPSR1, CDH17; co-absent with the target |
| [[GCNT3]] | C | GCNT3 activity raises FLRT3's level | lines that do not express GCNT3 (38) vs lines expressing it (12) | 3.04× lower at baseline in the lines without GCNT3 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, LYZ, MUC13; co-absent with the target |
| [[ARHGAP30]] | C | ARHGAP30 activity raises FLRT3's level | lines that do not express ARHGAP30 (22) vs lines expressing it (28) | 2.34× lower at baseline in the lines without ARHGAP30 | 0.014 | ⚠ within organs, on part of the lines; also absent: CEACAM1, IL1RN, NECTIN4; maybe low, not absent; co-absent with the target |
| [[LCN2]] | C | LCN2 activity raises FLRT3's level | lines that do not express LCN2 (33) vs lines expressing it (17) | 2.64× lower at baseline in the lines without LCN2 | 0.020 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: PRSS8, RAB25, TMPRSS4; co-absent with the target |
| [[MUC5B]] | C | MUC5B activity raises FLRT3's level | lines that do not express MUC5B (37) vs lines expressing it (13) | 3.34× lower at baseline in the lines without MUC5B | 0.020 | ⚠ within organs, on part of the lines; also absent: DAPP1, AGR3, ENSG00000259925; co-absent with the target |
| [[CEACAM6]] | C | CEACAM6 activity raises FLRT3's level | lines that do not express CEACAM6 (37) vs lines expressing it (13) | 3.16× lower at baseline in the lines without CEACAM6 | 0.022 | ⚠ within organs, on part of the lines; also absent: DAPP1, TMPRSS2, CDH17; co-absent with the target |
| [[CEACAM5]] | C | CEACAM5 activity raises FLRT3's level | lines that do not express CEACAM5 (39) vs lines expressing it (11) | 3.26× lower at baseline in the lines without CEACAM5 | 0.026 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, ENSG00000267881; co-absent with the target |

### Downstream of this gene

*33 arrows, 33 of them with an alert ⚠; grade A 0, B 15, C 18. Shown: the 12 strongest; 21 more arrows (21 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ELF3-AS1]] | B | FLRT3 activity raises ELF3-AS1's level | lines that do not express FLRT3 (21) vs lines expressing it (29) | 2.19× lower at baseline in the lines without FLRT3 | 0.008 | ⚠ within organs, on part of the lines; also absent: ARHGAP30, TMC5, ENSG00000259925 |
| [[TARID]] | B | FLRT3 activity raises TARID's level | lines that do not express FLRT3 (21) vs lines expressing it (29) | 2.70× lower at baseline in the lines without FLRT3 | 0.015 | ⚠ within organs, on part of the lines; also absent: ARHGAP30, TMC5, ENSG00000259925 |
| [[KLF5]] | B | FLRT3 activity raises KLF5's level | lines that do not express FLRT3 (21) vs lines expressing it (29) | 2.75× lower at baseline in the lines without FLRT3 | 0.022 | ⚠ within organs, on part of the lines; also absent: ARHGAP30, TMC5, ENSG00000259925 |
| [[STS]] | B | FLRT3 activity raises STS's level | lines that do not express FLRT3 (21) vs lines expressing it (29) | 2.38× lower at baseline in the lines without FLRT3 | 0.028 | ⚠ within organs, on part of the lines; also absent: ARHGAP30, TMC5, ENSG00000259925 |
| [[TNFRSF21]] | B | FLRT3 activity raises TNFRSF21's level | lines that do not express FLRT3 (21) vs lines expressing it (29) | 2.59× lower at baseline in the lines without FLRT3 | 0.032 | ⚠ within organs, on part of the lines; also absent: ARHGAP30, TMC5, ENSG00000259925 |
| [[PLD1]] | B | FLRT3 activity raises PLD1's level | lines that do not express FLRT3 (21) vs lines expressing it (29) | 1.73× lower at baseline in the lines without FLRT3 | 0.036 | ⚠ within organs, on part of the lines; also absent: ARHGAP30, TMC5, ENSG00000259925 |
| [[RBM47]] | B | FLRT3 activity raises RBM47's level | lines that do not express FLRT3 (21) vs lines expressing it (29) | 2.77× lower at baseline in the lines without FLRT3 | 0.043 | ⚠ within organs, on part of the lines; also absent: ARHGAP30, TMC5, ENSG00000259925 |
| [[PDZK1IP1]] | B | FLRT3 activity raises PDZK1IP1's level | lines that do not express FLRT3 (21) vs lines expressing it (29) | 1.96× lower at baseline in the lines without FLRT3 | 0.055 | ⚠ within organs, on part of the lines; also absent: ARHGAP30, TMC5, ENSG00000259925 |
| [[MISP]] | B | FLRT3 activity raises MISP's level | lines that do not express FLRT3 (21) vs lines expressing it (29) | 2.50× lower at baseline in the lines without FLRT3 | 0.061 | ⚠ within organs, on part of the lines; also absent: ARHGAP30, TMC5, ENSG00000259925 |
| [[LRG1]] | B | FLRT3 activity raises LRG1's level | lines that do not express FLRT3 (21) vs lines expressing it (29) | 1.71× lower at baseline in the lines without FLRT3 | 0.064 | ⚠ within organs, on part of the lines; also absent: ARHGAP30, TMC5, ENSG00000259925 |
| [[EPHA1]] | B | FLRT3 activity raises EPHA1's level | lines that do not express FLRT3 (21) vs lines expressing it (29) | 1.83× lower at baseline in the lines without FLRT3 | 0.065 | ⚠ within organs, on part of the lines; also absent: ARHGAP30, TMC5, ENSG00000259925 |
| [[TNFRSF21]] | B | FLRT3 activity strengthens TNFRSF21's drug response | lines that do not express FLRT3 (13) vs lines expressing it (21) | the lines without FLRT3 respond 0.73× as strongly (z diff +0.77); strongest at Digitoxin 5 µM: 0.81x vs 0.44x (z diff +4.3) | 0.068 | ⚠ within organs, on part of the lines; also absent: ARHGAP30, TMC5, ENSG00000259925; target measured in part of the lines; both ways; artifact flags |

## Where it sits

- **Module**: [[Module 155]] — MyD88 deficiency (TLR2/4); 29 genes; every member is in the + arm (projection on the module's main direction 0.772). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (35.7, 48.6); signed map (54.5, 23.2). **Vector** length 73.3, 17.4% of its response variance represented; |z| ≥ 3 in 805 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MyD88 deficiency (TLR2/4)* (reactome, mean cos +0.63 to 4); *IRAK4 deficiency (TLR2/4)* (reactome, mean cos +0.63 to 4); *Regulation of TLR by endogenous ligand* (reactome, mean cos +0.63 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.1 | +7.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +3.9 | +1.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.9 | +3.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.8 | +5.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.8 | +5.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.6 | +5.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.7 | +5.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.6 | +3.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.5 | +2.6 |
| fall | [[Tomivosertib (drug)]] 5 µM |  | -1.4 | -2.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.3 | -2.7 |
|  | [[Fluvoxamine (drug)]] 0.5 µM |  | -1.2 | -0.1 |
|  | [[Encorafenib (drug)]] 5 µM |  | -1.2 | -0.6 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -1.2 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | fibronectin leucine rich transmembrane protein 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20p12.1 — chr20:14,322,985-14,337,614 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Fibronectin type III domain containing |
| Reactome | 7 pathways, smallest: Downstream signaling of activated FGFR1; Signaling by FGFR1; Signaling by FGFR |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NZU0](https://www.uniprot.org/uniprotkb/Q9NZU0) (Leucine-rich repeat transmembrane protein FLRT3):

> Functions in cell-cell adhesion, cell migration and axon guidance, exerting an attractive or repulsive role depending on its interaction partners. Plays a role in the spatial organization of brain neurons. Plays a role in vascular development in the retina (By similarity). Plays a role in cell-cell adhesion via its interaction with ADGRL3 and probably also other latrophilins that are expressed at the surface of adjacent cells. Interaction with the intracellular domain of ROBO1 mediates axon …

**Summary**, from NCBI Gene [23767](https://www.ncbi.nlm.nih.gov/gene/23767):

> This gene encodes a member of the fibronectin leucine rich transmembrane protein (FLRT) family. FLRTs may function in cell adhesion and/or receptor signalling. Their protein structures resemble small leucine-rich proteoglycans found in the extracellular matrix. This gene is expressed in many tissues. Two alternatively spliced transcript variants encoding the same protein have been described for this gene. [provided by RefSeq, Jul 2010]

**Accessions** — [HGNC:3762](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3762) · Entrez [23767](https://www.ncbi.nlm.nih.gov/gene/23767) · UniProt [Q9NZU0](https://www.uniprot.org/uniprotkb/Q9NZU0) · Ensembl [ENSG00000125848](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125848)

## Data

Gene col 4678: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4678); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4678, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4678]; `tensor/DDL_lfc|DDL_z.npy` [4678]; `embed/gene_vectors.npy` [4678]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4678 or target_col == 4678). Every well: [[FLRT3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FLRT3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
