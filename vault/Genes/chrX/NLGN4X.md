---
symbol: "NLGN4X"
type: "gene"
col: 7134
ensembl_id: "ENSG00000146938"
name: "neuroligin 4 X-linked"
location: "Xp22.32-p22.31"
module: 87
arm: "+"
pooled_cpm: 12.05
n_lines_expressing: 13
n_dd_up: 11
n_dd_down: 5
n_dd_up_clean: 6
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 14
direction_downstream: 37
tags: ["gene", "module/087"]
generated_by: "tahoemap"
---

# NLGN4X

*neuroligin 4 X-linked* — Xp22.32-p22.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.19× (z +12.7, q 6e-34, up in 0 of 9 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.74× (z +8.5, q 2e-15, up in 0 of 10 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.584× (z -5.9, q 2e-06, down in 9 of 10 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MDGA2]] (+0.70, fdr 7e-06), [[LINC01205]] (+0.67, fdr 2e-05), [[PI15]] (+0.64, fdr 1e-05); moves opposite to [[CSAG1]] (-0.43, fdr 3e-04), [[LINC02086]] (-0.41, fdr 7e-04), [[ALDH3B1]] (-0.39, fdr 1e-04).
> It is in [[Module 087]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 14 arrows point to it, the strongest [[CTXN1]] → it (grade B ⚠); 37 go from it, the strongest it → cells under [[Fenofibrate (drug)]] 0.05 µM (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7134.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.19×** | +12.7 | 6e-34 | 0/9 | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.65×** | +10.2 | 4e-22 | 0/8 | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.74×** | +8.5 | 2e-15 | 0/10 | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.57×** | +6.9 | 7e-10 | 7/10 (SHP-77, A-172, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.76×** | +5.7 | 1e-06 | 0/9 | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Idoxuridine (drug)]] 0.05 µM |  | **1.45×** | +4.0 | 0.005 | 0/10 | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.42×** | +3.8 | 0.011 | 5/10 (SHP-77, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.39×** | +3.6 | 0.021 | 0/10 | top dose only | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.72×** | +3.6 | 0.021 | 0/9 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.61×** | +3.1 | 0.093 | 0/10 | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~19% of this change | **1.33×** | +3.1 | 0.093 | 0/9 | inconsistent across doses | low cells (technical?) |
| [[Bicalutamide (drug)]] 0.5 µM |  | 1.32× | +3.0 | 0.12 | 0/10 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7134.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.584×** | -5.9 | 2e-06 | 9/10 (NCI-H1573, C32, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.717×** | -5.2 | 6e-05 | 9/10 (NCI-H1573, SK-MEL-2, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.636×** | -5.0 | 1e-04 | 3/10 (SHP-77, BT-474, …) | top dose only | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.640×** | -4.5 | 8e-04 | 1/11 (C32) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.915× | -3.7 | 0.028 | 0/11 | inconsistent across doses |  |
| [[Medroxyprogesterone acetate (drug)]] 0.05 µM |  | **0.733×** | -3.4 | 0.061 | 1/10 (BT-474) | inconsistent across doses |  |
| [[Lucanthone (drug)]] 0.05 µM |  | 0.731× | -3.2 | 0.11 | 0/11 | inconsistent across doses | position effect removed |
| [[Clobetasol propionate (drug)]] 5 µM |  | 0.751× | -3.1 | 0.12 | 0/10 | top dose only |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.822× | -3.1 | 0.14 | 1/11 (BT-474) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7134. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 63.2 | 0 | 10 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.123× (z -15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.133× (z -15.3) |
| [[NCI-H1573 (line)]] | alt | 177 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0610× (z -30.5) |
| [[BT-474 (line)]] | alt | 35.9 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0512× (z -12.3) |
| [[HS-578T (line)]] | alt | 87.3 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -12.6) |
| [[SK-MEL-2 (line)]] | alt | 70.6 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0570× (z -18.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.160× (z -17.0) |
| [[C32 (line)]] | wt | 33.1 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.113× (z -14.8) |
| [[A-172 (line)]] | wt | 11.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.172× (z -11.6) |
| [[A498 (line)]] | wt | 1.38 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.76 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.82 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.93 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.61 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.98 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.43 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.49 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.55 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.53 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.68 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.86 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.84 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.86 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.54 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.84 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.17 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.52 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.24 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.60 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.45 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.75 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.44 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.57 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.61 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.51 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.84 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.67 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 6.08 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.47 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.47 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.67 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 2.03 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.86 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 2.78 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.75 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.34 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7134), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MDGA2]] | +0.70 | +0.68 / +0.73 | both halves | 7e-06 | STRING 626 |
| [[LINC01205]] | +0.67 | +0.48 / +0.70 | both halves | 2e-05 | **novel candidate** |
| [[PI15]] | +0.64 | +0.49 / +0.70 | both halves | 1e-05 | **novel candidate** |
| [[SOX10]] | +0.63 | +0.55 / +0.66 | both halves | 1e-05 |  |
| [[SAMMSON]] | +0.60 | +0.45 / +0.68 | both halves | 3e-05 |  |
| [[LEF1-AS1]] | +0.60 | +0.48 / +0.68 | both halves | 2e-05 |  |
| [[LEF1]] | +0.58 | +0.49 / +0.66 | both halves | 1e-05 |  |
| [[COL19A1]] | +0.57 | +0.48 / +0.67 | both halves | 2e-05 |  |
| [[LINC00879]] | +0.56 | +0.46 / +0.65 | both halves | 3e-05 |  |
| [[LINGO2]] | +0.56 | +0.43 / +0.61 | both halves | 3e-05 |  |
| [[LINC02566]] | +0.55 | +0.38 / +0.58 | both halves | 6e-05 |  |
| [[PTPRD]] | +0.55 | +0.43 / +0.58 | both halves | 3e-05 | pathway: Neuronal System |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CSAG1]] | -0.43 | -0.47 / -0.28 | both halves | 3e-04 |  |
| [[LINC02086]] | -0.41 | -0.43 / -0.20 | both halves | 7e-04 |  |
| [[ALDH3B1]] | -0.39 | -0.36 / -0.37 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 1, C 13. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CTXN1]] | B | CTXN1 activity raises NLGN4X's level | lines that do not express CTXN1 (8) vs lines expressing it (42) | 1.03× lower at baseline in the lines without CTXN1 | 0.093 | ⚠ within organs, on part of the lines; also absent: PARD6G, SLC29A4, CBX2; maybe low, not absent |
| [[ANKRD20A8P]], [[FAM95A]] | C | ANKRD20A8P, FAM95A activity raises NLGN4X's level | lines that do not express ANKRD20A8P, FAM95A (38) vs lines expressing them (12) | 5.16× lower at baseline in the lines without ANKRD20A8P, FAM95A | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000291025, ENSG00000249174, TPTE; co-absent with the target; co-absent genes |
| [[LINC00648]] | C | LINC00648 activity raises NLGN4X's level | lines that do not express LINC00648 (35) vs lines expressing it (15) | 3.77× lower at baseline in the lines without LINC00648 | 0.018 | ⚠ within organs, on part of the lines; also absent: LINC00470, ANKRD20A8P, ZIC1; co-absent with the target |
| [[LINC02616]] | C | LINC02616 activity raises NLGN4X's level | lines that do not express LINC02616 (37) vs lines expressing it (13) | 4.37× lower at baseline in the lines without LINC02616 | 0.023 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ADGRG7, ENSG00000287474, FCRLA; co-absent with the target |
| [[JAKMIP2]] | C | JAKMIP2 activity raises NLGN4X's level | lines that do not express JAKMIP2 (29) vs lines expressing it (21) | 3.06× lower at baseline in the lines without JAKMIP2 | 0.029 | ⚠ within organs, on part of the lines; also absent: MARCHF1, KCNH5, ENSG00000289309; maybe low, not absent; co-absent with the target |
| [[NRG3]] | C | NRG3 activity raises NLGN4X's level | lines that do not express NRG3 (41) vs lines expressing it (9) | 4.98× lower at baseline in the lines without NRG3 | 0.033 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, LINC00879, GPR141; co-absent with the target |
| [[CSAG1]] | C | CSAG1 activity raises NLGN4X's level | lines that do not express CSAG1 (30) vs lines expressing it (20) | 2.93× lower at baseline in the lines without CSAG1 | 0.034 | ⚠ within organs, on part of the lines; also absent: ENSG00000253363, ENSG00000226043, LINC02616; co-absent with the target |
| [[LINC02438]] | C | LINC02438 activity raises NLGN4X's level | lines that do not express LINC02438 (36) vs lines expressing it (14) | 3.09× lower at baseline in the lines without LINC02438 | 0.039 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000248515, MSR1, FSTL5; co-absent with the target |
| [[GABRG2]] | C | GABRG2 activity raises NLGN4X's level | lines that do not express GABRG2 (36) vs lines expressing it (14) | 3.24× lower at baseline in the lines without GABRG2 | 0.045 | ⚠ within organs, on part of the lines; also absent: ENSG00000287211, PCSK1, BAGE2; maybe low, not absent; co-absent with the target |
| [[MDGA2]] | C | MDGA2 activity raises NLGN4X's level | lines that do not express MDGA2 (32) vs lines expressing it (18) | 4.58× lower at baseline in the lines without MDGA2 | 0.049 | ⚠ within organs, on part of the lines; also absent: ZIC1, NLGN4X, TWIST1; co-absent with the target |
| [[CHMP1B2P]] | C | CHMP1B2P activity raises NLGN4X's level | lines that do not express CHMP1B2P (31) vs lines expressing it (19) | 2.26× lower at baseline in the lines without CHMP1B2P | 0.061 | ⚠ within organs, on part of the lines; also absent: LINC01242, LINC00648, BHMT2; co-absent with the target |
| [[GABRA3]] | C | GABRA3 activity raises NLGN4X's level | lines that do not express GABRA3 (26) vs lines expressing it (24) | 2.55× lower at baseline in the lines without GABRA3 | 0.076 | ⚠ within organs, on part of the lines; also absent: MAGEA3-DT, MKRN3, LRRTM4; co-absent with the target |

### Downstream of this gene

*37 arrows, 37 of them with an alert ⚠; grade A 0, B 14, C 23. Shown: the 12 strongest; 25 more arrows (25 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Fenofibrate (drug)]] 0.05 µM | B | NLGN4X activity raises the cells' numbers under Fenofibrate 0.05 µM (protects the cells) | lines that do not express NLGN4X (37) vs lines expressing it (11) | the lines without NLGN4X: 0.94× the cells of the other lines | 0.052 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01029, ENSG00000291025, ANKRD20A8P |
| cells under [[Sulfatinib (drug)]] 0.5 µM | B | NLGN4X activity raises the cells' numbers under Sulfatinib 0.5 µM (protects the cells) | lines that do not express NLGN4X (37) vs lines expressing it (11) | the lines without NLGN4X: 0.96× the cells of the other lines | 0.071 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01029, ENSG00000291025, ANKRD20A8P |
| cells under [[Sulfatinib (drug)]] 5 µM | B | NLGN4X activity lowers the cells' numbers under Sulfatinib 5 µM (makes them more sensitive) | lines that do not express NLGN4X (37) vs lines expressing it (11) | the lines without NLGN4X: 1.12× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01029, ENSG00000291025, ANKRD20A8P |
| cells under [[Vortioxetine (drug)]] 0.5 µM | B | NLGN4X activity raises the cells' numbers under Vortioxetine 0.5 µM (protects the cells) | lines that do not express NLGN4X (37) vs lines expressing it (11) | the lines without NLGN4X: 0.90× the cells of the other lines | 0.073 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01029, ENSG00000291025, ANKRD20A8P |
| cells under [[Betamethasone dipropionate (drug)]] 5 µM | B | NLGN4X activity lowers the cells' numbers under Betamethasone dipropionate 5 µM (makes them more sensitive) | lines that do not express NLGN4X (37) vs lines expressing it (11) | the lines without NLGN4X: 1.06× the cells of the other lines | 0.075 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01029, ENSG00000291025, ANKRD20A8P |
| cells under [[Imiquimod (hydrochloride) (drug)]] 0.05 µM | B | NLGN4X activity raises the cells' numbers under Imiquimod (hydrochloride) 0.05 µM (protects the cells) | lines that do not express NLGN4X (37) vs lines expressing it (11) | the lines without NLGN4X: 0.95× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01029, ENSG00000291025, ANKRD20A8P |
| cells under [[Tetracycline (hydrochloride) (drug)]] 0.5 µM | B | NLGN4X activity lowers the cells' numbers under Tetracycline (hydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express NLGN4X (37) vs lines expressing it (11) | the lines without NLGN4X: 1.06× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01029, ENSG00000291025, ANKRD20A8P |
| cells under [[Glasdegib (drug)]] 5 µM | B | NLGN4X activity raises the cells' numbers under Glasdegib 5 µM (protects the cells) | lines that do not express NLGN4X (37) vs lines expressing it (11) | the lines without NLGN4X: 0.96× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01029, ENSG00000291025, ANKRD20A8P; cell counts less trustworthy |
| cells under [[Digitoxin (drug)]] 0.05 µM | B | NLGN4X activity raises the cells' numbers under Digitoxin 0.05 µM (protects the cells) | lines that do not express NLGN4X (37) vs lines expressing it (11) | the lines without NLGN4X: 0.82× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01029, ENSG00000291025, ANKRD20A8P |
| cells under [[Vismodegib (drug)]] 5 µM | B | NLGN4X activity raises the cells' numbers under Vismodegib 5 µM (protects the cells) | lines that do not express NLGN4X (37) vs lines expressing it (11) | the lines without NLGN4X: 0.93× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01029, ENSG00000291025, ANKRD20A8P |
| [[EFR3B]] | B | NLGN4X activity raises EFR3B's level | lines that do not express NLGN4X (37) vs lines expressing it (13) | 2.36× lower at baseline in the lines without NLGN4X | 0.081 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01029, ENSG00000291025, ANKRD20A8P |
| cells under [[Loperamide (hydrochloride) (drug)]] 0.5 µM | B | NLGN4X activity raises the cells' numbers under Loperamide (hydrochloride) 0.5 µM (protects the cells) | lines that do not express NLGN4X (37) vs lines expressing it (11) | the lines without NLGN4X: 0.92× the cells of the other lines | 0.088 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01029, ENSG00000291025, ANKRD20A8P |

## Where it sits

- **Module**: [[Module 087]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.665). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (51.1, 28.3); signed map (30.9, 39.6). **Vector** length 50.6, 20.5% of its response variance represented; |z| ≥ 3 in 286 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.1 | +12.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.7 | +10.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.6 | +5.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.1 | +8.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.0 | +6.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.5 | +1.2 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.4 | +2.6 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.1 | +1.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.1 | +1.2 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.4 | -4.5 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.2 | -3.2 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.2 | -2.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.1 | -1.4 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -1.1 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | neuroligin 4 X-linked |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp22.32-p22.31 — chrX:5,840,637-6,228,867 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1260, NLGN, HLNX; previously NLGN4 |
| Gene groups (HGNC) | Neuroligins |
| Reactome | 3 pathways, smallest: Neurexins and neuroligins; Protein-protein interactions at synapses; Neuronal System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N0W4](https://www.uniprot.org/uniprotkb/Q8N0W4) (Neuroligin-4, X-linked):

> Cell surface protein involved in cell-cell-interactions via its interactions with neurexin family members.

**Summary**, from NCBI Gene [57502](https://www.ncbi.nlm.nih.gov/gene/57502):

> This gene encodes a member of the type-B carboxylesterase/lipase protein family. The encoded protein belongs to a family of neuronal cell surface proteins. Members of this family may act as splice site-specific ligands for beta-neurexins and may be involved in the formation and remodeling of central nervous system synapses. The encoded protein interacts with discs large homolog 4 (DLG4). Mutations in this gene have been associated with autism and Asperger syndrome. Alternative splicing results …

**Accessions** — [HGNC:14287](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14287) · Entrez [57502](https://www.ncbi.nlm.nih.gov/gene/57502) · UniProt [Q8N0W4](https://www.uniprot.org/uniprotkb/Q8N0W4) · Ensembl [ENSG00000146938](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000146938)

## Data

Gene col 7134: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7134); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7134, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7134]; `tensor/DDL_lfc|DDL_z.npy` [7134]; `embed/gene_vectors.npy` [7134]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7134 or target_col == 7134). Every well: [[NLGN4X — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NLGN4X.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
