---
symbol: "MDGA2"
type: "gene"
col: 6354
ensembl_id: "ENSG00000139915"
name: "MAM domain containing glycosylphosphatidylinositol anchor 2"
location: "14q21.3"
module: 87
arm: "+"
pooled_cpm: 66.34
n_lines_expressing: 18
n_dd_up: 11
n_dd_down: 9
n_dd_up_clean: 7
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 4
direction_downstream: 11
tags: ["gene", "module/087"]
generated_by: "tahoemap"
---

# MDGA2

*MAM domain containing glycosylphosphatidylinositol anchor 2* — 14q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.14× (z +12.7, q 5e-34, up in 1 of 17 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.578× (z -6.4, q 7e-08, down in 12 of 16 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SETBP1]] (+0.70, fdr 7e-06), [[NLGN4X]] (+0.70, fdr 7e-06), [[SOX10]] (+0.68, fdr 7e-06).
> It is in [[Module 087]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[F11-AS1]] → it (grade C ⚠); 11 go from it, the strongest it → [[LINC02226]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6354.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.14×** | +12.7 | 5e-34 | 1/17 (RPMI-7951) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.35×** | +10.1 | 2e-21 | 1/17 (NCI-H1573) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.17×** | +8.8 | 3e-16 | 0/14 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.72×** | +4.6 | 7e-04 | 0/16 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.41×** | +3.7 | 0.021 | 1/15 (A-427) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bimatoprost (drug)]] 0.5 µM |  | **1.34×** | +3.5 | 0.040 | 1/17 (NCI-H661) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.34×** | +3.4 | 0.040 | 5/16 (SNU-423, SHP-77, …) | top dose only |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.34×** | +3.4 | 0.040 | 0/16 | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.23×** | +3.4 | 0.040 | 3/16 (NCI-H1573, BT-474, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +3.4 | 0.044 | 0/18 | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.31×** | +3.2 | 0.062 | 0/15 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~10% here) |
| [[Cobimetinib (drug)]] 5 µM |  | 1.30× | +3.0 | 0.12 | 10/16 (HOP62, SW 1271, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6354.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.578×** | -6.4 | 7e-08 | 12/16 (C32, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.613×** | -5.7 | 3e-06 | 11/16 (SK-MEL-2, A-172, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.669×** | -4.7 | 5e-04 | 10/16 (SK-MEL-2, C32, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.731×** | -3.7 | 0.035 | 8/16 (HS-578T, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.744×** | -3.5 | 0.051 | 12/16 (SW 1271, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.569×** | -3.5 | 0.051 | 6/16 (A-172, C32, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~8% of this change | **0.813×** | -3.4 | 0.051 | 8/16 (C32, HOP62, …) | rises with dose | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.749×** | -3.4 | 0.051 | 12/16 (C32, HOP62, …) | two highest doses |  |
| [[MK-8353 (drug)]] 0.5 µM |  | **0.675×** | -3.3 | 0.063 | 0/16 | inconsistent across doses | noisy plate (z scaled) |
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | 0.755× | -3.0 | 0.13 | 0/16 | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | 0.773× | -3.0 | 0.13 | 11/16 (SK-MEL-2, C32, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6354. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 1,626 | 0 | 19 (14 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -20.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.108× (z -17.8) |
| [[NCI-H23 (line)]] | alt | 435 | 0 | 12 (10 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0385× (z -24.0) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.248× (z -10.3) |
| [[SK-MEL-2 (line)]] | alt | 435 | 0 | 12 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.166× (z -21.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.207× (z -13.3) |
| [[HOP62 (line)]] | alt | 91.9 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -10.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.202× (z -10.0) |
| [[A-172 (line)]] | wt | 31.3 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.137× (z -12.1) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.211× (z -9.4) |
| [[SW 1271 (line)]] | alt | 169 | 0 | 4 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0902× (z -10.1) ⚠ cell-cycle shift, explains ~12% of this change |
| [[A-427 (line)]] | wt | 32.8 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.63× (z +9.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.96× (z +9.1) | [[Dinaciclib (drug)]] 0.5 µM 0.168× (z -9.0) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 496 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.300× (z -10.2) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 32.8 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.96× (z +9.6) | [[Ixazomib citrate (drug)]] 5 µM 0.242× (z -8.9) ⚠ cell-cycle shift, explains ~46% of this change |
| [[SNU-423 (line)]] | alt | 64.8 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.229× (z -8.9) ⚠ cell-cycle shift, explains ~43% of this change |
| [[A498 (line)]] | wt | 5.34 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 7.84 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 15.8 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 6.61 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.18 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 5.60 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 192 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.06 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 58.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.66 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 6.55 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 6.71 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 5.30 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.16 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.05 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 5.25 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 5.83 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 6.11 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 15.7 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 6.28 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.06 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 7.71 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 6.54 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.67 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 6.52 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.91 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 4.85 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 6.56 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.07 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 16.1 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 8.89 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 5.86 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 8.11 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 5.65 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6354), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SETBP1]] | +0.70 | +0.67 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[NLGN4X]] | +0.70 | +0.68 / +0.73 | both halves | 7e-06 | STRING 626 |
| [[SOX10]] | +0.68 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[PI15]] | +0.65 | +0.55 / +0.71 | both halves | 1e-05 | **novel candidate** |
| [[COL19A1]] | +0.65 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[IGFBP5]] | +0.64 | +0.72 / +0.55 | both halves | 1e-05 | **novel candidate** |
| [[MIR3681HG]] | +0.64 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[PTPRD]] | +0.63 | +0.55 / +0.64 | both halves | 1e-05 | same gene group |
| [[KC6]] | +0.63 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[DIRC3]] | +0.63 | +0.60 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[LOXL3]] | +0.63 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[AEBP1]] | +0.62 | +0.64 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 0, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[F11-AS1]] | C | F11-AS1 activity raises MDGA2's level | lines that do not express F11-AS1 (34) vs lines expressing it (16) | 3.41× lower at baseline in the lines without F11-AS1 | 0.015 | ⚠ within organs, on part of the lines; also absent: ENSG00000272297, SRRM4, LINC02566; maybe low, not absent; co-absent with the target |
| [[WNK3]] | C | WNK3 activity raises MDGA2's level | lines that do not express WNK3 (28) vs lines expressing it (22) | 6.15× lower at baseline in the lines without WNK3 | 0.072 | ⚠ within organs, on part of the lines; also absent: PCDH17, ZNF667, PTPRN; maybe low, not absent; co-absent with the target |
| [[ST8SIA6-AS1]] | C | ST8SIA6-AS1 activity raises MDGA2's level | lines that do not express ST8SIA6-AS1 (40) vs lines expressing it (10) | 4.90× lower at baseline in the lines without ST8SIA6-AS1 | 0.079 | ⚠ within organs, on part of the lines; also absent: CALCA, MUC6, LINC02267; co-absent with the target |
| [[NLGN4X]] | C | NLGN4X activity raises MDGA2's level | lines that do not express NLGN4X (37) vs lines expressing it (13) | 5.82× lower at baseline in the lines without NLGN4X | 0.094 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01029, ENSG00000291025, ANKRD20A8P; co-absent with the target |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 1, C 10.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02226]] | B | MDGA2 activity raises LINC02226's level | lines that do not express MDGA2 (32) vs lines expressing it (18) | 2.11× lower at baseline in the lines without MDGA2 | 0.073 | ⚠ within organs, on part of the lines; also absent: ZIC1, NLGN4X, TWIST1 |
| [[LINC02438]] | C | MDGA2 activity raises LINC02438's level | lines that do not express MDGA2 (32) vs lines expressing it (18) | 5.51× lower at baseline in the lines without MDGA2 | 0.027 | ⚠ within organs, on part of the lines; also absent: ZIC1, NLGN4X, TWIST1; co-absent with the target |
| [[LINC01446]] | C | MDGA2 activity raises LINC01446's level | lines that do not express MDGA2 (32) vs lines expressing it (18) | 5.28× lower at baseline in the lines without MDGA2 | 0.029 | ⚠ within organs, on part of the lines; also absent: ZIC1, NLGN4X, TWIST1; co-absent with the target |
| [[MAGEA3-DT]] | C | MDGA2 activity raises MAGEA3-DT's level | lines that do not express MDGA2 (32) vs lines expressing it (18) | 4.93× lower at baseline in the lines without MDGA2 | 0.044 | ⚠ within organs, on part of the lines; also absent: ZIC1, NLGN4X, TWIST1; co-absent with the target |
| [[CAMK4]] | C | MDGA2 activity raises CAMK4's level | lines that do not express MDGA2 (32) vs lines expressing it (18) | 4.81× lower at baseline in the lines without MDGA2 | 0.047 | ⚠ within organs, on part of the lines; also absent: ZIC1, NLGN4X, TWIST1; co-absent with the target |
| [[WNK3]] | C | MDGA2 activity raises WNK3's level | lines that do not express MDGA2 (32) vs lines expressing it (18) | 3.77× lower at baseline in the lines without MDGA2 | 0.047 | ⚠ within organs, on part of the lines; also absent: ZIC1, NLGN4X, TWIST1; co-absent with the target |
| [[NLGN4X]] | C | MDGA2 activity raises NLGN4X's level | lines that do not express MDGA2 (32) vs lines expressing it (18) | 4.58× lower at baseline in the lines without MDGA2 | 0.049 | ⚠ within organs, on part of the lines; also absent: ZIC1, NLGN4X, TWIST1; co-absent with the target |
| [[LINC02055]] | C | MDGA2 activity raises LINC02055's level | lines that do not express MDGA2 (32) vs lines expressing it (18) | 3.94× lower at baseline in the lines without MDGA2 | 0.051 | ⚠ within organs, on part of the lines; also absent: ZIC1, NLGN4X, TWIST1; co-absent with the target |
| [[GABRA3]] | C | MDGA2 activity raises GABRA3's level | lines that do not express MDGA2 (32) vs lines expressing it (18) | 3.41× lower at baseline in the lines without MDGA2 | 0.070 | ⚠ within organs, on part of the lines; also absent: ZIC1, NLGN4X, TWIST1; co-absent with the target |
| [[LINC02575]] | C | MDGA2 activity raises LINC02575's level | lines that do not express MDGA2 (32) vs lines expressing it (18) | 2.63× lower at baseline in the lines without MDGA2 | 0.095 | ⚠ within organs, on part of the lines; also absent: ZIC1, NLGN4X, TWIST1; co-absent with the target |
| [[CHRM3]] | C | MDGA2 activity raises CHRM3's level | lines that do not express MDGA2 (32) vs lines expressing it (18) | 3.04× lower at baseline in the lines without MDGA2 | 0.0997 | ⚠ within organs, on part of the lines; also absent: ZIC1, NLGN4X, TWIST1; co-absent with the target |

## Where it sits

- **Module**: [[Module 087]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.732). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (50.9, 27.8); signed map (30.4, 41.0). **Vector** length 66.0, 21.4% of its response variance represented; |z| ≥ 3 in 519 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.0 | +10.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.1 | +8.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.0 | +3.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.8 | +12.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.6 | +3.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.3 | +3.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +1.8 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.9 | +3.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | +4.6 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -2.4 | -3.4 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.3 | -2.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.2 | -2.5 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -2.1 | -3.7 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -2.0 | -2.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.9 | -1.5 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.9 | -3.0 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.7 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | MAM domain containing glycosylphosphatidylinositol anchor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q21.3 — chr14:46,840,092-47,675,605 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously MAMDC1 |
| Gene groups (HGNC) | I-set domain containing |
| Reactome | 1 pathways, smallest: Post-translational modification: synthesis of GPI-anchored proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z553](https://www.uniprot.org/uniprotkb/Q7Z553) (MAM domain-containing glycosylphosphatidylinositol anchor protein 2):

> Key regulator of excitatory-inhibitory synaptic balance, acting through the negative modulation of excitatory glutamatergic synapse formation and synaptic transmission.

**Summary**, from NCBI Gene [161357](https://www.ncbi.nlm.nih.gov/gene/161357):

> Predicted to be involved in regulation of synapse organization and spinal cord motor neuron differentiation. Predicted to act upstream of or within several processes, including motor behavior; negative regulation of neuron apoptotic process; and neuron migration. Predicted to be located in extracellular region and plasma membrane. Predicted to be active in GABA-ergic synapse; glutamatergic synapse; and postsynaptic density membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:19835](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19835) · Entrez [161357](https://www.ncbi.nlm.nih.gov/gene/161357) · UniProt [Q7Z553](https://www.uniprot.org/uniprotkb/Q7Z553) · Ensembl [ENSG00000139915](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000139915)

## Data

Gene col 6354: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6354); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6354, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6354]; `tensor/DDL_lfc|DDL_z.npy` [6354]; `embed/gene_vectors.npy` [6354]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6354 or target_col == 6354). Every well: [[MDGA2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MDGA2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
