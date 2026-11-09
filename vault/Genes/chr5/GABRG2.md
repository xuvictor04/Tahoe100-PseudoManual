---
symbol: "GABRG2"
type: "gene"
col: 3450
ensembl_id: "ENSG00000113327"
name: "gamma-aminobutyric acid type A receptor subunit gamma2"
location: "5q34"
module: 27
arm: "+"
pooled_cpm: 3.77
n_lines_expressing: 14
n_dd_up: 20
n_dd_down: 3
n_dd_up_clean: 8
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 32
direction_downstream: 52
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# GABRG2

*gamma-aminobutyric acid type A receptor subunit gamma2* — 5q34

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 5.89× (z +13.2, q 4e-37, up in 0 of 7 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.91× (z +6.8, q 1e-09, up in 0 of 8 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 0.445× (z -6.1, q 8e-07, down in 8 of 10 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC00491]] (+0.72, fdr 7e-06), [[ARHGAP25]] (+0.70, fdr 7e-06), [[LINC02315]] (+0.70, fdr 7e-06).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 32 arrows point to it, the strongest [[LINC02050]] → it (grade C ⚠); 52 go from it, the strongest it → [[SLCO6A1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 12 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3450.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.89×** | +13.2 | 4e-37 | 0/7 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.00×** | +11.5 | 3e-28 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.73×** | +9.1 | 2e-17 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.85×** | +7.5 | 1e-11 | 3/7 (A-172, A-427, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.91×** | +6.8 | 1e-09 | 0/8 | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.64×** | +5.2 | 2e-05 | 5/10 (A-427, SW480, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.01×** | +5.2 | 2e-05 | 0/9 | top dose only | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.62×** | +5.1 | 2e-05 | 1/7 (SHP-77) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.88×** | +4.7 | 2e-04 | 0/7 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~8% here) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.84×** | +4.5 | 3e-04 | 2/8 (SW480, SK-MEL-2) | top dose only |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.21×** | +4.2 | 0.001 | 0/7 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.45×** | +3.9 | 0.005 | 0/8 | top dose only | cell-cycle shift (explains ~22% here); composition shift |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.66×** | +3.8 | 0.007 | 0/8 | inconsistent across doses | low cells (technical?) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.62×** | +3.6 | 0.013 | 1/9 (A-172) | top dose only |  |
| [[Fingolimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.62×** | +3.6 | 0.013 | 0/9 | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.40×** | +3.6 | 0.013 | 3/10 (SW480, NCI-H1573, …) | rises with dose |  |
| [[BAY1125976 (drug)]] 0.5 µM |  | **1.88×** | +3.3 | 0.027 | 0/8 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bestatin (hydrochloride) (drug)]] 0.05 µM |  | **1.52×** | +3.1 | 0.055 | 1/10 (SW480) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3450.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.445×** | -6.1 | 8e-07 | 8/10 (SHP-77, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Mebendazole (drug)]] 5 µM |  | **0.585×** | -3.9 | 0.033 | 1/10 (H4) | top dose only |  |
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | **0.589×** | -3.7 | 0.047 | 0/10 | inconsistent across doses |  |
| [[Artesunate (drug)]] 0.5 µM |  | 0.651× | -3.2 | 0.18 | 0/10 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.31 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3450. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SK-MEL-2 (line)]] | alt | 25.0 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0389× (z -18.2) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0734× (z -14.1) |
| [[SHP-77 (line)]] | alt | 68.1 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.123× (z -15.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.245× (z -15.2) |
| [[NCI-H1573 (line)]] | alt | 24.7 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -11.8) |
| [[A-172 (line)]] | wt | 8.19 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.101× (z -10.0) ⚠ cell-cycle shift, explains ~55% of this change |
| [[H4 (line)]] | wt | 17.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.140× (z -10.5) |
| [[SW480 (line)]] | alt | 7.76 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0303× (z -17.3) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 8.27 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.456 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.725 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.764 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.621 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.642 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.669 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.507 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.731 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.621 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.588 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.603 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.670 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.683 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.627 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.846 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.721 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.721 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.487 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.525 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.606 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.722 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.533 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.468 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.483 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.524 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 5.82 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.576 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.444 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.590 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.70 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.458 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.476 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.585 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.598 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.618 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.695 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.843 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.724 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3450), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00491]] | +0.72 | +0.70 / +0.64 | both halves | 7e-06 |  |
| [[ARHGAP25]] | +0.70 | +0.62 / +0.72 | both halves | 7e-06 |  |
| [[LINC02315]] | +0.70 | +0.71 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[LINC01980]] | +0.69 | +0.60 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[MIR2052HG]] | +0.68 | +0.69 / +0.63 | both halves | 7e-06 |  |
| [[SLCO6A1]] | +0.66 | +0.63 / +0.57 | both halves | 1e-05 |  |
| [[LINC01905]] | +0.66 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[LINC00648]] | +0.65 | +0.65 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[RUNX1T1]] | +0.65 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[CSMD3]] | +0.64 | +0.60 / +0.56 | both halves | 1e-05 | **novel candidate** |
| [[RMST]] | +0.64 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[LINC02492]] | +0.63 | +0.60 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*32 arrows, 32 of them with an alert ⚠; grade A 0, B 0, C 32. Shown: the 12 strongest; 20 more arrows (20 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02050]] | C | LINC02050 activity raises GABRG2's level | lines that do not express LINC02050 (37) vs lines expressing it (13) | 3.43× lower at baseline in the lines without LINC02050 | 7e-04 | ⚠ within organs, on part of the lines; also absent: ENSG00000286329, ENSG00000242828, PASD1; co-absent with the target |
| [[NLGN4X]] | C | NLGN4X activity raises GABRG2's level | lines that do not express NLGN4X (37) vs lines expressing it (13) | 4.49× lower at baseline in the lines without NLGN4X | 7e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01029, ENSG00000291025, ANKRD20A8P; co-absent with the target |
| [[LINC01446]] | C | LINC01446 activity raises GABRG2's level | lines that do not express LINC01446 (34) vs lines expressing it (16) | 3.62× lower at baseline in the lines without LINC01446 | 0.004 | ⚠ within organs, on part of the lines; also absent: GABRG2, BAGE2, ENSG00000253363; co-absent with the target |
| [[LINC02315]] | C | LINC02315 activity raises GABRG2's level | lines that do not express LINC02315 (31) vs lines expressing it (19) | 2.76× lower at baseline in the lines without LINC02315 | 0.006 | ⚠ within organs, on part of the lines; also absent: GABRG2, COX7B2, SLC25A24P1; co-absent with the target |
| [[LINC00648]] | C | LINC00648 activity raises GABRG2's level | lines that do not express LINC00648 (35) vs lines expressing it (15) | 3.56× lower at baseline in the lines without LINC00648 | 0.007 | ⚠ within organs, on part of the lines; also absent: LINC00470, ANKRD20A8P, ZIC1; co-absent with the target |
| [[JAKMIP2]] | C | JAKMIP2 activity raises GABRG2's level | lines that do not express JAKMIP2 (29) vs lines expressing it (21) | 2.87× lower at baseline in the lines without JAKMIP2 | 0.007 | ⚠ within organs, on part of the lines; also absent: MARCHF1, KCNH5, ENSG00000289309; maybe low, not absent; co-absent with the target |
| [[SPINK5]] | C | SPINK5 activity raises GABRG2's level | lines that do not express SPINK5 (35) vs lines expressing it (15) | 2.22× lower at baseline in the lines without SPINK5 | 0.012 | ⚠ within organs, on part of the lines; also absent: TFF2, ST6GALNAC1, ENSG00000248588; co-absent with the target |
| [[LRRTM4]] | C | LRRTM4 activity raises GABRG2's level | lines that do not express LRRTM4 (33) vs lines expressing it (17) | 2.89× lower at baseline in the lines without LRRTM4 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000227088, ENSG00000249174, ENSG00000248973; co-absent with the target |
| [[KCNH5]] | C | KCNH5 activity raises GABRG2's level | lines that do not express KCNH5 (36) vs lines expressing it (14) | 3.54× lower at baseline in the lines without KCNH5 | 0.019 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ASCL1, ENSG00000260958, UNC5D; co-absent with the target |
| [[LINC02438]] | C | LINC02438 activity raises GABRG2's level | lines that do not express LINC02438 (36) vs lines expressing it (14) | 3.13× lower at baseline in the lines without LINC02438 | 0.024 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000248515, MSR1, FSTL5; co-absent with the target |
| [[FUT9]] | C | FUT9 activity raises GABRG2's level | lines that do not express FUT9 (40) vs lines expressing it (10) | 3.06× lower at baseline in the lines without FUT9 | 0.031 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000232252, KCNH7, GCG; co-absent with the target |
| [[FAM95A]] | C | FAM95A activity raises GABRG2's level | lines that do not express FAM95A (38) vs lines expressing it (12) | 3.58× lower at baseline in the lines without FAM95A | 0.035 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: ENSG00000291025, ENSG00000249174, TPTE; co-absent with the target |

### Downstream of this gene

*52 arrows, 52 of them with an alert ⚠; grade A 0, B 4, C 48. Shown: the 12 strongest; 40 more arrows (40 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLCO6A1]] | B | GABRG2 activity raises SLCO6A1's level | lines that do not express GABRG2 (36) vs lines expressing it (14) | 1.94× lower at baseline in the lines without GABRG2 | 0.022 | ⚠ within organs, on part of the lines; also absent: ENSG00000287211, PCSK1, BAGE2; maybe low, not absent |
| [[LINC01980]] | B | GABRG2 activity raises LINC01980's level | lines that do not express GABRG2 (36) vs lines expressing it (14) | 2.02× lower at baseline in the lines without GABRG2 | 0.049 | ⚠ within organs, on part of the lines; also absent: ENSG00000287211, PCSK1, BAGE2; maybe low, not absent |
| cells under [[Adagrasib (drug)]] 0.5 µM | B | GABRG2 activity raises the cells' numbers under Adagrasib 0.5 µM (protects the cells) | lines that do not express GABRG2 (36) vs lines expressing it (12) | the lines without GABRG2: 0.88× the cells of the other lines | 0.092 | ⚠ within organs, on part of the lines; also absent: ENSG00000287211, PCSK1, BAGE2; maybe low, not absent |
| cells under [[Flumatinib (mesylate) (drug)]] 0.5 µM | B | GABRG2 activity lowers the cells' numbers under Flumatinib (mesylate) 0.5 µM (makes them more sensitive) | lines that do not express GABRG2 (36) vs lines expressing it (12) | the lines without GABRG2: 1.16× the cells of the other lines | 0.095 | ⚠ within organs, on part of the lines; also absent: ENSG00000287211, PCSK1, BAGE2; maybe low, not absent |
| [[LINC02315]] | C | GABRG2 activity raises LINC02315's level | lines that do not express GABRG2 (36) vs lines expressing it (14) | 5.56× lower at baseline in the lines without GABRG2 | 7e-04 | ⚠ within organs, on part of the lines; also absent: ENSG00000287211, PCSK1, BAGE2; maybe low, not absent; co-absent with the target |
| [[LINC01446]] | C | GABRG2 activity raises LINC01446's level | lines that do not express GABRG2 (36) vs lines expressing it (14) | 5.99× lower at baseline in the lines without GABRG2 | 0.005 | ⚠ within organs, on part of the lines; also absent: ENSG00000287211, PCSK1, BAGE2; maybe low, not absent; co-absent with the target |
| [[DACH1]] | C | GABRG2 activity raises DACH1's level | lines that do not express GABRG2 (36) vs lines expressing it (14) | 3.73× lower at baseline in the lines without GABRG2 | 0.006 | ⚠ within organs, on part of the lines; also absent: ENSG00000287211, PCSK1, BAGE2; maybe low, not absent; co-absent with the target |
| [[LINC02616]] | C | GABRG2 activity raises LINC02616's level | lines that do not express GABRG2 (36) vs lines expressing it (14) | 4.09× lower at baseline in the lines without GABRG2 | 0.008 | ⚠ within organs, on part of the lines; also absent: ENSG00000287211, PCSK1, BAGE2; maybe low, not absent; co-absent with the target |
| [[OR3A2]] | C | GABRG2 activity raises OR3A2's level | lines that do not express GABRG2 (36) vs lines expressing it (14) | 2.36× lower at baseline in the lines without GABRG2 | 0.012 | ⚠ within organs, on part of the lines; also absent: ENSG00000287211, PCSK1, BAGE2; maybe low, not absent; co-absent with the target |
| [[LNCAROD]] | C | GABRG2 activity raises LNCAROD's level | lines that do not express GABRG2 (36) vs lines expressing it (14) | 3.82× lower at baseline in the lines without GABRG2 | 0.013 | ⚠ within organs, on part of the lines; also absent: ENSG00000287211, PCSK1, BAGE2; maybe low, not absent; co-absent with the target |
| [[LINC02438]] | C | GABRG2 activity raises LINC02438's level | lines that do not express GABRG2 (36) vs lines expressing it (14) | 4.83× lower at baseline in the lines without GABRG2 | 0.017 | ⚠ within organs, on part of the lines; also absent: ENSG00000287211, PCSK1, BAGE2; maybe low, not absent; co-absent with the target |
| [[LINC00491]] | C | GABRG2 activity raises LINC00491's level | lines that do not express GABRG2 (36) vs lines expressing it (14) | 2.49× lower at baseline in the lines without GABRG2 | 0.018 | ⚠ within organs, on part of the lines; also absent: ENSG00000287211, PCSK1, BAGE2; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.531). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (30.3, 40.5); signed map (48.1, 34.7). **Vector** length 35.3, 11.8% of its response variance represented; |z| ≥ 3 in 226 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.5 | +11.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.3 | +13.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.5 | +9.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.7 | +6.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.3 | +3.6 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.6 | +1.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +2.8 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.3 | +2.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.3 | +2.1 |
| fall | [[Lucanthone (drug)]] 0.05 µM |  | -1.4 | -2.8 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.2 | +0.3 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.1 | -3.7 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.1 | -1.0 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.1 | -1.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.1 | -3.2 |
|  | [[Irinotecan (hydrochloride) (drug)]] 0.5 µM |  | -1.1 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | gamma-aminobutyric acid type A receptor subunit gamma2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q34 — chr5:162,000,057-162,162,977 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Gamma-aminobutyric acid type A receptor subunits |
| Reactome | 6 pathways, smallest: GABA receptor activation; Signaling by ERBB4; Neurotransmitter receptors and postsynaptic signal transmission |
| Matched by | ensembl_id |

**Function**, from UniProt [P18507](https://www.uniprot.org/uniprotkb/P18507) (Gamma-aminobutyric acid receptor subunit gamma-2):

> Gamma subunit of the heteropentameric ligand-gated chloride channel gated by gamma-aminobutyric acid (GABA), a major inhibitory neurotransmitter in the brain. GABA-gated chloride channels, also named GABA(A) receptors (GABAAR), consist of five subunits arranged around a central pore and contain GABA active binding site(s) located at the alpha and beta subunit interface(s). When activated by GABA, GABAARs selectively allow the flow of chloride anions across the cell membrane down their …

**Summary**, from NCBI Gene [2566](https://www.ncbi.nlm.nih.gov/gene/2566):

> This gene encodes a gamma-aminobutyric acid (GABA) receptor. GABA is the major inhibitory neurotransmitter in the mammlian brain, where it acts at GABA-A receptors, which are ligand-gated chloride channels. GABA-A receptors are pentameric, consisting of proteins from several subunit classes: alpha, beta, gamma, delta and rho. Mutations in this gene have been associated with epilepsy and febrile seizures. Multiple transcript variants encoding different isoforms have been identified for this …

**Accessions** — [HGNC:4087](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4087) · Entrez [2566](https://www.ncbi.nlm.nih.gov/gene/2566) · UniProt [P18507](https://www.uniprot.org/uniprotkb/P18507) · Ensembl [ENSG00000113327](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000113327)

## Data

Gene col 3450: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3450); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3450, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3450]; `tensor/DDL_lfc|DDL_z.npy` [3450]; `embed/gene_vectors.npy` [3450]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3450 or target_col == 3450). Every well: [[GABRG2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GABRG2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
