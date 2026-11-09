---
symbol: "CTNNA2"
type: "gene"
col: 815
ensembl_id: "ENSG00000066032"
name: "catenin alpha 2"
location: "2p12"
module: 9
arm: "+"
pooled_cpm: 41.13
n_lines_expressing: 17
n_dd_up: 25
n_dd_down: 2
n_dd_up_clean: 20
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 23
direction_downstream: 26
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# CTNNA2

*catenin alpha 2* — 2p12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (5 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 3.36× (z +20.4, q 0e+00, up in 11 of 15 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Topotecan (hydrochloride) (drug)]] 0.5 µM: 0.682× (z -4.6, q 0.003, down in 9 of 14 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (C-33 A 0.151×, SW1417 0.206×, NCI-H661 0.139×, SHP-77 0.419×); [[Homoharringtonine (drug)]] 5 µM in 3 lines (NCI-H23 0.0982×, SW1417 0.138×, PANC-1 0.212×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (SW1417 0.104×, PANC-1 0.169×); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H23 0.0510×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDH10]] (+0.68, fdr 1e-05), [[TMEM108]] (+0.67, fdr 7e-06), [[NCAM2]] (+0.67, fdr 7e-06).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 23 arrows point to it, the strongest [[KCNH7]] → it (grade C ⚠); 26 go from it, the strongest it → [[HOXC4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 815.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **3.36×** | +20.4 | 0e+00 | 11/15 (NCI-H1573, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.27×** | +13.8 | 4e-41 | 2/15 (SW48, AN3 CA) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **3.12×** | +13.6 | 1e-39 | 11/14 (NCI-H1573, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.96×** | +12.9 | 4e-36 | 1/12 (SW48) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.48×** | +10.4 | 2e-23 | 0/9 | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.90×** | +7.7 | 2e-12 | 9/14 (NCI-H1573, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.92×** | +7.2 | 4e-11 | 1/11 (SK-MEL-2) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.80×** | +7.0 | 1e-10 | 1/15 (SW48) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.77×** | +6.8 | 7e-10 | 12/14 (NCI-H1573, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.65×** | +6.0 | 1e-07 | 9/14 (NCI-H1573, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.68×** | +6.0 | 1e-07 | 1/14 (SK-MEL-2) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.48×** | +4.7 | 1e-04 | 9/14 (NCI-H23, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.71×** | +4.3 | 6e-04 | 0/12 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.39×** | +3.7 | 0.007 | 8/14 (SHP-77, C-33 A, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.35×** | +3.6 | 0.012 | 0/13 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.34×** | +3.5 | 0.019 | 2/14 (SW48, SK-MEL-2) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.33×** | +3.4 | 0.021 | 8/13 (SHP-77, C32, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.32×** | +3.3 | 0.027 | 2/14 (SHP-77, PANC-1) | inconsistent across doses |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.31×** | +3.3 | 0.032 | 0/14 | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 815.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (C-33 A 0.151×, SW1417 0.206×, NCI-H661 0.139×, SHP-77 0.419×); [[Homoharringtonine (drug)]] 5 µM in 3 lines (NCI-H23 0.0982×, SW1417 0.138×, PANC-1 0.212×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (SW1417 0.104×, PANC-1 0.169×); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H23 0.0510×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.682×** | -4.6 | 0.003 | 9/14 (C-33 A, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.735×** | -3.7 | 0.073 | 8/14 (NCI-H23, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Lucanthone (drug)]] 0.05 µM |  | 0.759× | -3.0 | 0.43 | 0/15 | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 815. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 50.3 | 4 | 7 (5 ⚠) | [[Tucidinostat (drug)]] 5 µM 4.66× (z +12.7) | [[Homoharringtonine (drug)]] 5 µM 0.0982× (z -19.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0510× (z -16.6) |
| [[C-33 A (line)]] | alt | 1,584 | 0 | 7 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.151× (z -20.3) |
| [[NCI-H1573 (line)]] | alt | 28.8 | 5 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 7.71× (z +14.1) | [[Homoharringtonine (drug)]] 5 µM 0.278× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 234 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.138× (z -15.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.104× (z -12.9) |
| [[A-427 (line)]] | wt | 46.6 | 1 | 2 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.88× (z +9.0) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.190× (z -9.7) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 134 | 2 | 1 | [[Tucidinostat (drug)]] 5 µM 2.60× (z +10.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.419× (z -9.6) |
| [[SK-MEL-2 (line)]] | alt | 150 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.94× (z +12.3) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[C32 (line)]] | wt | 42.4 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 5.14× (z +10.5) | — |
| [[PANC-1 (line)]] | alt | 43.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.212× (z -11.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.169× (z -9.0) |
| [[NCI-H661 (line)]] | alt | 1,095 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.139× (z -12.7) |
| [[SW48 (line)]] | wt | 16.4 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 13.6× (z +11.7) | — |
| [[A-172 (line)]] | wt | 10.0 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 5.24 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 7.54 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.84 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 8.05 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 5.33 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 8.68 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 7.27 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 29.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.86 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 6.14 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 6.70 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 6.20 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 5.08 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 5.59 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 6.79 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.98 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 4.87 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 5.22 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 7.59 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 8.14 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 5.47 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.46 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 4.78 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 6.98 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 39.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.45 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 5.42 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 49.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.56 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 6.04 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 5.31 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 6.08 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 7.15 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.22 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 5.68 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 815), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDH10]] | +0.68 | +0.53 / +0.68 | both halves | 1e-05 | STRING 666 |
| [[TMEM108]] | +0.67 | +0.61 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[NCAM2]] | +0.67 | +0.58 / +0.68 | both halves | 7e-06 |  |
| [[ERBB4]] | +0.66 | +0.54 / +0.77 | both halves | 1e-05 | **novel candidate** |
| [[CARD18]] | +0.66 | +0.53 / +0.71 | both halves | 1e-05 | **novel candidate** |
| [[EPHA5]] | +0.65 | +0.49 / +0.68 | both halves | 1e-05 |  |
| [[LINC01194]] | +0.63 | +0.47 / +0.70 | both halves | 2e-05 | **novel candidate** |
| [[FSTL5]] | +0.62 | +0.53 / +0.65 | both halves | 1e-05 | **novel candidate** |
| [[CDH18]] | +0.62 | +0.53 / +0.72 | both halves | 1e-05 | STRING 728 |
| [[KCNH7]] | +0.62 | +0.51 / +0.74 | both halves | 1e-05 |  |
| [[GPC3]] | +0.61 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[MMRN1]] | +0.61 | +0.42 / +0.69 | both halves | 4e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*23 arrows, 23 of them with an alert ⚠; grade A 0, B 0, C 23. Shown: the 12 strongest; 11 more arrows (11 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KCNH7]] | C | KCNH7 activity raises CTNNA2's level | lines that do not express KCNH7 (35) vs lines expressing it (15) | 6.18× lower at baseline in the lines without KCNH7 | 0.001 | ⚠ within organs, on part of the lines; also absent: FUT9, ENSG00000289309, PI15; maybe low, not absent; co-absent with the target |
| [[FAR2P1]] | C | FAR2P1 activity raises CTNNA2's level | lines that do not express FAR2P1 (29) vs lines expressing it (21) | 3.45× lower at baseline in the lines without FAR2P1 | 0.001 | ⚠ within organs, on part of the lines; co-absent genes; also absent: POTEE, ENSG00000264660, ENSG00000286329; co-absent with the target |
| [[LINC02327]] | C | LINC02327 activity raises CTNNA2's level | lines that do not express LINC02327 (41) vs lines expressing it (9) | 4.31× lower at baseline in the lines without LINC02327 | 0.006 | ⚠ within organs, on part of the lines; also absent: ENSG00000258028, LINC02566, ENSG00000289605; co-absent with the target |
| [[DISC1FP1]] | C | DISC1FP1 activity raises CTNNA2's level | lines that do not express DISC1FP1 (29) vs lines expressing it (21) | 3.35× lower at baseline in the lines without DISC1FP1 | 0.008 | ⚠ within organs, on part of the lines; also absent: FSTL5, ENSG00000250954, ENSG00000251574; co-absent with the target |
| [[CSMD3]] | C | CSMD3 activity raises CTNNA2's level | lines that do not express CSMD3 (36) vs lines expressing it (14) | 3.67× lower at baseline in the lines without CSMD3 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, LINC01205, ENSG00000243486; co-absent with the target |
| [[BMP5]] | C | BMP5 activity raises CTNNA2's level | lines that do not express BMP5 (38) vs lines expressing it (12) | 6.31× lower at baseline in the lines without BMP5 | 0.014 | ⚠ within organs, on part of the lines; also absent: LINC01035, CPLX2, SCG3; co-absent with the target |
| [[JPH3]] | C | JPH3 activity raises CTNNA2's level | lines that do not express JPH3 (29) vs lines expressing it (21) | 3.79× lower at baseline in the lines without JPH3 | 0.020 | ⚠ within organs, on part of the lines; also absent: OLFM1, JAKMIP1, GABBR2; maybe low, not absent; co-absent with the target |
| [[NELL2]] | C | NELL2 activity raises CTNNA2's level | lines that do not express NELL2 (28) vs lines expressing it (22) | 3.40× lower at baseline in the lines without NELL2 | 0.031 | ⚠ within organs, on part of the lines; also absent: SOX2, FREM2, PTH2R; maybe low, not absent; co-absent with the target |
| [[FUT9]] | C | FUT9 activity raises CTNNA2's level | lines that do not express FUT9 (40) vs lines expressing it (10) | 2.87× lower at baseline in the lines without FUT9 | 0.031 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000232252, KCNH7, GCG; co-absent with the target |
| [[NFASC]] | C | NFASC activity raises CTNNA2's level | lines that do not express NFASC (27) vs lines expressing it (23) | 3.36× lower at baseline in the lines without NFASC | 0.039 | ⚠ within organs, on part of the lines; also absent: DPYSL5, JPH3, KIF1A; co-absent with the target |
| [[SLC6A17]] | C | SLC6A17 activity raises CTNNA2's level | lines that do not express SLC6A17 (28) vs lines expressing it (22) | 3.85× lower at baseline in the lines without SLC6A17 | 0.039 | ⚠ within organs, on part of the lines; also absent: TWIST1, LINC00470, MAGEA3-DT; co-absent with the target |
| [[FREM2]] | C | FREM2 activity raises CTNNA2's level | lines that do not express FREM2 (26) vs lines expressing it (24) | 2.44× lower at baseline in the lines without FREM2 | 0.040 | ⚠ within organs, on part of the lines; also absent: NELL2, ANKRD20A11P, KCNH7; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*26 arrows, 26 of them with an alert ⚠; grade A 0, B 8, C 18. Shown: the 12 strongest; 14 more arrows (14 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HOXC4]] | B | CTNNA2 activity raises HOXC4's level | lines that do not express CTNNA2 (33) vs lines expressing it (17) | 2.67× lower at baseline in the lines without CTNNA2 | 0.010 | ⚠ within organs, on part of the lines; also absent: SRRM4, MAGEA4, KCNH7 |
| [[PRKD1]] | B | CTNNA2 activity raises PRKD1's level | lines that do not express CTNNA2 (33) vs lines expressing it (17) | 2.65× lower at baseline in the lines without CTNNA2 | 0.040 | ⚠ within organs, on part of the lines; also absent: SRRM4, MAGEA4, KCNH7 |
| [[SOBP]] | B | CTNNA2 activity raises SOBP's level | lines that do not express CTNNA2 (33) vs lines expressing it (17) | 3.32× lower at baseline in the lines without CTNNA2 | 0.067 | ⚠ within organs, on part of the lines; also absent: SRRM4, MAGEA4, KCNH7 |
| [[ROBO1]] | B | CTNNA2 activity raises ROBO1's level | lines that do not express CTNNA2 (33) vs lines expressing it (17) | 2.82× lower at baseline in the lines without CTNNA2 | 0.070 | ⚠ within organs, on part of the lines; also absent: SRRM4, MAGEA4, KCNH7 |
| [[ANKS1B]] | B | CTNNA2 activity raises ANKS1B's level | lines that do not express CTNNA2 (33) vs lines expressing it (17) | 2.20× lower at baseline in the lines without CTNNA2 | 0.074 | ⚠ within organs, on part of the lines; also absent: SRRM4, MAGEA4, KCNH7 |
| [[SNTG2]] | B | CTNNA2 activity raises SNTG2's level | lines that do not express CTNNA2 (33) vs lines expressing it (17) | 1.83× lower at baseline in the lines without CTNNA2 | 0.081 | ⚠ within organs, on part of the lines; also absent: SRRM4, MAGEA4, KCNH7 |
| [[SEPTIN3]] | B | CTNNA2 activity raises SEPTIN3's level | lines that do not express CTNNA2 (33) vs lines expressing it (17) | 2.37× lower at baseline in the lines without CTNNA2 | 0.089 | ⚠ within organs, on part of the lines; also absent: SRRM4, MAGEA4, KCNH7 |
| [[FAM184A]] | B | CTNNA2 activity raises FAM184A's level | lines that do not express CTNNA2 (33) vs lines expressing it (17) | 2.07× lower at baseline in the lines without CTNNA2 | 0.095 | ⚠ within organs, on part of the lines; also absent: SRRM4, MAGEA4, KCNH7 |
| [[FAR2P1]] | C | CTNNA2 activity raises FAR2P1's level | lines that do not express CTNNA2 (33) vs lines expressing it (17) | 2.92× lower at baseline in the lines without CTNNA2 | 0.001 | ⚠ within organs, on part of the lines; also absent: SRRM4, MAGEA4, KCNH7; co-absent with the target |
| [[CARD18]] | C | CTNNA2 activity raises CARD18's level | lines that do not express CTNNA2 (33) vs lines expressing it (17) | 2.79× lower at baseline in the lines without CTNNA2 | 0.006 | ⚠ within organs, on part of the lines; also absent: SRRM4, MAGEA4, KCNH7; co-absent with the target |
| [[GNAO1]] | C | CTNNA2 activity raises GNAO1's level | lines that do not express CTNNA2 (33) vs lines expressing it (17) | 2.60× lower at baseline in the lines without CTNNA2 | 0.011 | ⚠ within organs, on part of the lines; also absent: SRRM4, MAGEA4, KCNH7; co-absent with the target |
| [[SYN2]] | C | CTNNA2 activity raises SYN2's level | lines that do not express CTNNA2 (33) vs lines expressing it (17) | 2.67× lower at baseline in the lines without CTNNA2 | 0.030 | ⚠ within organs, on part of the lines; also absent: SRRM4, MAGEA4, KCNH7; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.682). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (38.4, 34.0); signed map (39.8, 35.4). **Vector** length 54.6, 17.0% of its response variance represented; |z| ≥ 3 in 456 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.9 | +20.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.4 | +12.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.8 | +10.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.7 | +13.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.7 | +7.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.5 | +1.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | +3.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.8 | +2.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.3 | +3.0 |
| fall | [[Digitoxin (drug)]] 0.05 µM |  | -2.1 | -3.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -2.1 | -4.6 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.3 | -2.5 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.2 | -2.8 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.2 | -3.0 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -1.2 | -1.5 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.1 | -2.1 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.1 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | catenin alpha 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p12 — chr2:79,185,231-80,648,861 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CAP-R, CT114 |
| Gene groups (HGNC) | Alpha catenins |
| Reactome | 1 pathways, smallest: Myogenesis |
| Matched by | ensembl_id |

**Function**, from UniProt [P26232](https://www.uniprot.org/uniprotkb/P26232) (Catenin alpha-2):

> May function as a linker between cadherin adhesion receptors and the cytoskeleton to regulate cell-cell adhesion and differentiation in the nervous system (By similarity). Required for proper regulation of cortical neuronal migration and neurite growth. It acts as a negative regulator of Arp2/3 complex activity and Arp2/3-mediated actin polymerization. It thereby suppresses excessive actin branching which would impair neurite growth and stability. Regulates morphological plasticity of synapses …

**Summary**, from NCBI Gene [1496](https://www.ncbi.nlm.nih.gov/gene/1496):

> Enables actin filament binding activity. Involved in negative regulation of Arp2/3 complex-mediated actin nucleation; regulation of neuron migration; and regulation of neuron projection development. Located in cytoplasm. Implicated in complex cortical dysplasia with other brain malformations 9. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:2510](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2510) · Entrez [1496](https://www.ncbi.nlm.nih.gov/gene/1496) · UniProt [P26232](https://www.uniprot.org/uniprotkb/P26232) · Ensembl [ENSG00000066032](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000066032)

## Data

Gene col 815: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 815); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 815, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 815]; `tensor/DDL_lfc|DDL_z.npy` [815]; `embed/gene_vectors.npy` [815]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 815 or target_col == 815). Every well: [[CTNNA2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CTNNA2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
