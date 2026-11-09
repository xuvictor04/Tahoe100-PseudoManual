---
symbol: "NAA11"
type: "gene"
col: 7966
ensembl_id: "ENSG00000156269"
name: "N-alpha-acetyltransferase 11, NatA catalytic subunit"
location: "4q21.21"
module: 9
arm: "+"
pooled_cpm: 4.67
n_lines_expressing: 11
n_dd_up: 19
n_dd_down: 2
n_dd_up_clean: 9
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 18
direction_downstream: 39
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# NAA11

*N-alpha-acetyltransferase 11, NatA catalytic subunit* — 4q21.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.96× (z +11.9, q 6e-30, up in 0 of 4 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.53× (z +10.1, q 1e-21, up in 2 of 7 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Methyl aminolevulinate (hydrochloride) (drug)]] 0.5 µM: 0.627× (z -3.7, q 0.091, down in 0 of 7 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (SK-MEL-2 0.319×, NCI-H1573 0.333×; ⚠ cell-cycle shift, explains ~34% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H1573 0.207×, SK-MEL-2 0.301×; ⚠ toxic; transcription drop); [[Decitabine (drug)]] 0.5 µM in 1 line (LS 180 0.0527×).
> Its strongest partners by |cos| (61 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 39 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RNF17]] (+0.59, fdr 1e-04), [[FAM230C]] (+0.56, fdr 2e-04), [[ASXL3]] (+0.56, fdr 2e-04).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 18 arrows point to it, the strongest [[GTSF1]] → it (grade C ⚠); 39 go from it, the strongest it → [[FRG1FP]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 10 with an alert ⚠. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7966.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.96×** | +11.9 | 6e-30 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.53×** | +10.1 | 1e-21 | 2/7 (LS 180, NCI-H1573) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.47×** | +9.6 | 1e-19 | 0/7 | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.36×** | +6.1 | 1e-07 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.94×** | +5.1 | 4e-05 | 3/7 (NCI-H1573, SHP-77, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.85×** | +4.7 | 2e-04 | 0/4 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~7% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.84×** | +4.5 | 5e-04 | 1/7 (NCI-H1573) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.76×** | +4.1 | 0.003 | 1/3 (NCI-H1573) | top dose only | noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.66×** | +3.9 | 0.006 | 0/7 | inconsistent across doses | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.63×** | +3.8 | 0.010 | 1/7 (SHP-77) | top dose only |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.92×** | +3.6 | 0.017 | 0/5 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.61×** | +3.5 | 0.021 | 0/6 | top dose only | cell-cycle shift (explains ~8% here) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.38×** | +3.5 | 0.021 | 0/3 | top dose only | noisy plate (z scaled) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.53×** | +3.2 | 0.048 | 0/7 | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.52×** | +3.2 | 0.051 | 1/7 (LS 180) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[BAY1125976 (drug)]] 0.5 µM |  | **1.76×** | +3.1 | 0.063 | 0/7 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.52×** | +3.1 | 0.063 | 0/7 | top dose only | cell-cycle shift (explains ~3% here) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.72×** | +3.0 | 0.088 | 0/7 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.47×** | +3.0 | 0.088 | 1/7 (H4) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7966.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (SK-MEL-2 0.319×, NCI-H1573 0.333×; ⚠ cell-cycle shift, explains ~34% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H1573 0.207×, SK-MEL-2 0.301×; ⚠ toxic; transcription drop); [[Decitabine (drug)]] 0.5 µM in 1 line (LS 180 0.0527×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Methyl aminolevulinate (hydrochloride) (drug)]] 0.5 µM |  | **0.627×** | -3.7 | 0.091 | 0/7 | inconsistent across doses |  |
| [[Erlotinib (drug)]] 0.05 µM |  | **0.608×** | -3.6 | 0.091 | 1/7 (HS-578T) | inconsistent across doses |  |
| [[Doxycycline (monohydrate) (drug)]] 5 µM |  | 0.657× | -3.2 | 0.30 | 1/7 (HS-578T) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7966. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 37.8 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.333× (z -10.5) ⚠ cell-cycle shift, explains ~34% of this change |
| [[SK-MEL-2 (line)]] | alt | 100 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -12.1) ⚠ cell-cycle shift, explains ~34% of this change |
| [[LS 180 (line)]] | wt | 4.16 | 0 | 1 | — | [[Decitabine (drug)]] 0.5 µM 0.0527× (z -9.5) |
| [[A-172 (line)]] | wt | 0.695 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.539 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.581 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.590 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.929 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.594 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.804 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.740 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.06 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.723 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.777 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.750 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.718 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.765 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.654 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.61 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.888 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.01 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.594 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.775 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.755 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.841 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.584 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.594 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.637 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 5.23 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.647 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.589 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.703 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 8.19 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.893 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.590 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.589 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.722 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.733 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 64.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.801 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.777 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.847 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.858 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.630 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.832 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.660 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7966), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 39 of them with an alert (⚠; 39 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF17]] | +0.59 | +0.35 / +0.63 | both halves | 1e-04 | **novel candidate** |
| [[FAM230C]] | +0.56 | +0.29 / +0.57 | both halves | 2e-04 |  |
| [[ASXL3]] | +0.56 | +0.29 / +0.61 | both halves | 2e-04 |  |
| [[KHDRBS2]] | +0.55 | +0.24 / +0.72 | both halves | 5e-04 |  |
| [[ZNF208]] | +0.54 | +0.27 / +0.60 | both halves | 3e-04 |  |
| [[GTSF1]] | +0.52 | +0.29 / +0.46 | both halves | 2e-04 |  |
| [[GABRA2]] | +0.51 | +0.33 / +0.43 | both halves | 1e-04 |  |
| [[LINGO2]] | +0.51 | +0.31 / +0.47 | both halves | 2e-04 |  |
| [[CKMT1A]] | +0.51 | +0.50 / +0.28 | both halves | 3e-04 |  |
| [[NELL1]] | +0.50 | +0.17 / +0.60 | ⚠ one half (not replicated) | 0.001 |  |
| [[SLC6A15]] | +0.50 | +0.28 / +0.48 | both halves | 3e-04 |  |
| [[PARM1]] | +0.50 | +0.40 / +0.46 | both halves | 5e-05 |  |
| [[KCNH7]] | +0.49 | +0.34 / +0.55 | both halves | 1e-04 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 0, C 18. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GTSF1]] | C | GTSF1 activity raises NAA11's level | lines that do not express GTSF1 (40) vs lines expressing it (10) | 3.79× lower at baseline in the lines without GTSF1 | 0.007 | ⚠ within organs, on part of the lines; also absent: CGA, CALCA, LINC02566; co-absent with the target |
| [[F11-AS1]] | C | F11-AS1 activity raises NAA11's level | lines that do not express F11-AS1 (34) vs lines expressing it (16) | 2.72× lower at baseline in the lines without F11-AS1 | 0.013 | ⚠ within organs, on part of the lines; also absent: ENSG00000272297, SRRM4, LINC02566; maybe low, not absent; co-absent with the target |
| [[LINC01518]] | C | LINC01518 activity raises NAA11's level | lines that do not express LINC01518 (36) vs lines expressing it (14) | 2.49× lower at baseline in the lines without LINC01518 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000285822, CCDC144NL-AS1, PHF2P2; co-absent with the target |
| [[CHMP1B2P]] | C | CHMP1B2P activity raises NAA11's level | lines that do not express CHMP1B2P (31) vs lines expressing it (19) | 2.31× lower at baseline in the lines without CHMP1B2P | 0.021 | ⚠ within organs, on part of the lines; also absent: LINC01242, LINC00648, BHMT2; co-absent with the target |
| [[CGA]] | C | CGA activity raises NAA11's level | lines that do not express CGA (44) vs lines expressing it (6) | 4.54× lower at baseline in the lines without CGA | 0.029 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, SYT4, RIT2; co-absent with the target |
| [[RNF17]] | C | RNF17 activity raises NAA11's level | lines that do not express RNF17 (42) vs lines expressing it (8) | 3.93× lower at baseline in the lines without RNF17 | 0.030 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SSX1, LINC00879, APOD; co-absent with the target |
| [[NLGN4X]] | C | NLGN4X activity raises NAA11's level | lines that do not express NLGN4X (37) vs lines expressing it (13) | 3.48× lower at baseline in the lines without NLGN4X | 0.030 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01029, ENSG00000291025, ANKRD20A8P; co-absent with the target |
| [[LINC01446]] | C | LINC01446 activity raises NAA11's level | lines that do not express LINC01446 (34) vs lines expressing it (16) | 2.88× lower at baseline in the lines without LINC01446 | 0.031 | ⚠ within organs, on part of the lines; also absent: GABRG2, BAGE2, ENSG00000253363; co-absent with the target |
| [[MARCHF1]] | C | MARCHF1 activity raises NAA11's level | lines that do not express MARCHF1 (33) vs lines expressing it (17) | 2.74× lower at baseline in the lines without MARCHF1 | 0.040 | ⚠ within organs, on part of the lines; also absent: UNC5D, DSCAM, LINC01266; maybe low, not absent; co-absent with the target |
| [[RIT2]] | C | RIT2 activity raises NAA11's level | lines that do not express RIT2 (44) vs lines expressing it (6) | 3.79× lower at baseline in the lines without RIT2 | 0.044 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, KCNB2, SYT4; co-absent with the target |
| [[SRRM4]] | C | SRRM4 activity raises NAA11's level | lines that do not express SRRM4 (41) vs lines expressing it (9) | 3.94× lower at baseline in the lines without SRRM4 | 0.045 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: KCNB2, RIT2, CALCA; maybe low, not absent; co-absent with the target |
| [[LINC03046]] | C | LINC03046 activity raises NAA11's level | lines that do not express LINC03046 (38) vs lines expressing it (12) | 2.96× lower at baseline in the lines without LINC03046 | 0.049 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MAGEB2, LINC00824, LINC01205; co-absent with the target |

### Downstream of this gene

*39 arrows, 39 of them with an alert ⚠; grade A 0, B 3, C 36. Shown: the 12 strongest; 27 more arrows (27 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FRG1FP]] | B | NAA11 activity raises FRG1FP's level | lines that do not express NAA11 (39) vs lines expressing it (11) | 3.08× lower at baseline in the lines without NAA11 | 0.014 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CGA, RIT2, ADGRG7; maybe low, not absent |
| [[MYT1L]] | B | NAA11 activity raises MYT1L's level | lines that do not express NAA11 (39) vs lines expressing it (11) | 2.00× lower at baseline in the lines without NAA11 | 0.046 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CGA, RIT2, ADGRG7; maybe low, not absent |
| [[FKBP9P1]] | B | NAA11 activity raises FKBP9P1's level | lines that do not express NAA11 (39) vs lines expressing it (11) | 2.05× lower at baseline in the lines without NAA11 | 0.082 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CGA, RIT2, ADGRG7; maybe low, not absent |
| [[ST6GALNAC1]] | C | NAA11 activity raises ST6GALNAC1's level | lines that do not express NAA11 (39) vs lines expressing it (11) | 1.61× lower at baseline in the lines without NAA11 | 6e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CGA, RIT2, ADGRG7; maybe low, not absent; co-absent with the target |
| [[F11-AS1]] | C | NAA11 activity raises F11-AS1's level | lines that do not express NAA11 (39) vs lines expressing it (11) | 4.67× lower at baseline in the lines without NAA11 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CGA, RIT2, ADGRG7; maybe low, not absent; co-absent with the target |
| [[RNF17]] | C | NAA11 activity raises RNF17's level | lines that do not express NAA11 (39) vs lines expressing it (11) | 2.69× lower at baseline in the lines without NAA11 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CGA, RIT2, ADGRG7; maybe low, not absent; co-absent with the target |
| [[NRG3]] | C | NAA11 activity raises NRG3's level | lines that do not express NAA11 (39) vs lines expressing it (11) | 4.60× lower at baseline in the lines without NAA11 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CGA, RIT2, ADGRG7; maybe low, not absent; co-absent with the target |
| [[GTSF1]] | C | NAA11 activity raises GTSF1's level | lines that do not express NAA11 (39) vs lines expressing it (11) | 2.85× lower at baseline in the lines without NAA11 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CGA, RIT2, ADGRG7; maybe low, not absent; co-absent with the target |
| [[SNTG1]] | C | NAA11 activity raises SNTG1's level | lines that do not express NAA11 (39) vs lines expressing it (11) | 2.88× lower at baseline in the lines without NAA11 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CGA, RIT2, ADGRG7; maybe low, not absent; co-absent with the target |
| [[PIGR]] | C | NAA11 activity raises PIGR's level | lines that do not express NAA11 (39) vs lines expressing it (11) | 2.35× lower at baseline in the lines without NAA11 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CGA, RIT2, ADGRG7; maybe low, not absent; co-absent with the target |
| [[LINGO2]] | C | NAA11 activity raises LINGO2's level | lines that do not express NAA11 (39) vs lines expressing it (11) | 4.94× lower at baseline in the lines without NAA11 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CGA, RIT2, ADGRG7; maybe low, not absent; co-absent with the target |
| [[LINC02055]] | C | NAA11 activity raises LINC02055's level | lines that do not express NAA11 (39) vs lines expressing it (11) | 4.66× lower at baseline in the lines without NAA11 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CGA, RIT2, ADGRG7; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.471). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (36.8, 36.5); signed map (43.6, 35.9). **Vector** length 16.3, 3.87% of its response variance represented; |z| ≥ 3 in 133 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.0 | +11.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.0 | +9.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.6 | +6.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.3 | +10.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.9 | +2.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.6 | +3.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.0 | +0.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.9 | +2.5 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +0.9 | +3.9 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.0 | -2.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.8 | -2.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.7 | -2.6 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -0.7 | -2.9 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -0.6 | -2.8 |
|  | [[Diphenhydramine (drug)]] 0.05 µM |  | -0.6 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | N-alpha-acetyltransferase 11, NatA catalytic subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q21.21 — chr4:79,225,694-79,326,061 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ARD2, hARD2; previously ARD1B |
| Gene groups (HGNC) | N-alpha-acetyltransferase subunits; GCN5 related N-acetyltransferases |
| Hallmark sets | SPERMATOGENESIS |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BSU3](https://www.uniprot.org/uniprotkb/Q9BSU3) (N-alpha-acetyltransferase 11):

> Displays alpha (N-terminal) acetyltransferase activity. Proposed alternative catalytic subunit of the N-terminal acetyltransferase A (NatA) complex.

**Summary**, from NCBI Gene [84779](https://www.ncbi.nlm.nih.gov/gene/84779):

> Enables protein-N-terminal amino-acid acetyltransferase activity. Involved in N-terminal protein amino acid acetylation. Located in cytosol and nucleoplasm. Part of NatA complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28125](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28125) · Entrez [84779](https://www.ncbi.nlm.nih.gov/gene/84779) · UniProt [Q9BSU3](https://www.uniprot.org/uniprotkb/Q9BSU3) · Ensembl [ENSG00000156269](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000156269)

## Data

Gene col 7966: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7966); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7966, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7966]; `tensor/DDL_lfc|DDL_z.npy` [7966]; `embed/gene_vectors.npy` [7966]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7966 or target_col == 7966). Every well: [[NAA11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NAA11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
