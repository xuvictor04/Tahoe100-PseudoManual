---
symbol: "AGR3"
type: "gene"
col: 10390
ensembl_id: "ENSG00000173467"
name: "anterior gradient 3, protein disulphide isomerase family member"
location: "7p21.1"
module: 44
arm: "+"
pooled_cpm: 6.83
n_lines_expressing: 8
n_dd_up: 7
n_dd_down: 1
n_dd_up_clean: 3
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 45
direction_downstream: 91
tags: ["gene", "module/044"]
generated_by: "tahoemap"
---

# AGR3

*anterior gradient 3, protein disulphide isomerase family member* — 7p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 5.73× (z +9.2, q 2e-17, up in 1 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.83× (z +4.3, q 0.002, up in 0 of 6 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Docetaxel (drug)]] 0.5 µM: 0.488× (z -3.8, q 0.093, down in 6 of 6 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (LS 180 0.0565×, KATO III 0.185×, HT-29 0.140×; ⚠ cell-cycle shift, explains ~81% of this change); [[Panobinostat (drug)]] 0.5 µM in 1 line (KATO III 0.113×; ⚠ cell-cycle shift, explains ~0% of this change); [[Panobinostat (drug)]] 5 µM in 1 line (KATO III 0.122×; ⚠ cell-cycle shift, explains ~0% of this change); [[Docetaxel (drug)]] 5 µM in 1 line (HT-29 0.158×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HNF1A-AS1]] (+0.77, fdr 7e-06), [[PRR15L]] (+0.74, fdr 7e-06), [[LGALS4]] (+0.73, fdr 7e-06).
> It is in [[Module 044]], a single-armed module (Defective GALNT12 causes CRCS1).
> Probable direction (from the cell lines, not proof of direct regulation): 45 arrows point to it, the strongest [[TM4SF4]] → it (grade C ⚠); 91 go from it, the strongest it → [[LNX1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10390.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.73×** | +9.2 | 2e-17 | 1/5 (KATO III) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.27×** | +8.4 | 9e-15 | 1/5 (KATO III) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.60×** | +6.3 | 7e-08 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.83×** | +4.3 | 0.002 | 0/6 | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.95×** | +3.4 | 0.074 | 0/5 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.55×** | +3.3 | 0.091 | 2/6 (LS 180, COLO 205) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Entrectinib (drug)]] 5 µM |  | **1.85×** | +3.3 | 0.091 | 1/6 (BT-474) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | 1.82× | +3.2 | 0.10 | 0/5 | top dose only | cell-cycle shift (explains ~14% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10390.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (LS 180 0.0565×, KATO III 0.185×, HT-29 0.140×; ⚠ cell-cycle shift, explains ~81% of this change); [[Panobinostat (drug)]] 0.5 µM in 1 line (KATO III 0.113×; ⚠ cell-cycle shift, explains ~0% of this change); [[Panobinostat (drug)]] 5 µM in 1 line (KATO III 0.122×; ⚠ cell-cycle shift, explains ~0% of this change); [[Docetaxel (drug)]] 5 µM in 1 line (HT-29 0.158×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Docetaxel (drug)]] 0.5 µM |  | **0.488×** | -3.8 | 0.093 | 6/6 (KATO III, HT-29, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | 0.506× | -3.3 | 0.26 | 0/6 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, +0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10390. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 223 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -10.1) ⚠ cell-cycle shift, explains ~81% of this change |
| [[HT-29 (line)]] | alt | 22.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -9.2) ⚠ cell-cycle shift, explains ~81% of this change · without an alert: [[Docetaxel (drug)]] 5 µM 0.158× (z -8.6) |
| [[LS 180 (line)]] | wt | 15.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0565× (z -12.6) ⚠ cell-cycle shift, explains ~81% of this change |
| [[A-172 (line)]] | wt | 0.577 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.530 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.525 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.513 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.948 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.18 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 9.93 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.639 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.587 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 4.33 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.712 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 3.89 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.604 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.643 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.735 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.656 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.636 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.618 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.599 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.788 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.532 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.56 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.642 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.515 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.735 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.500 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.570 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 5.23 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.592 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.609 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.589 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.639 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.522 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.504 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.635 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.583 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.570 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.531 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.946 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.13 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.12 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.684 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.694 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.604 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.694 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.679 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10390), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HNF1A-AS1]] | +0.77 | +0.66 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[PRR15L]] | +0.74 | +0.67 / +0.69 | both halves | 7e-06 |  |
| [[LGALS4]] | +0.73 | +0.74 / +0.70 | both halves | 7e-06 |  |
| [[PLEKHG6]] | +0.72 | +0.61 / +0.70 | both halves | 7e-06 |  |
| [[TSPAN8]] | +0.70 | +0.68 / +0.67 | both halves | 7e-06 |  |
| [[C9orf152]] | +0.68 | +0.62 / +0.68 | both halves | 7e-06 |  |
| [[ST6GALNAC1]] | +0.68 | +0.72 / +0.57 | both halves | 1e-05 |  |
| [[BCAS1]] | +0.68 | +0.60 / +0.66 | both halves | 7e-06 |  |
| [[POF1B]] | +0.68 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[UGT1A1]] | +0.67 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[PCK1]] | +0.67 | +0.52 / +0.70 | both halves | 1e-05 |  |
| [[SLC40A1]] | +0.66 | +0.56 / +0.65 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*45 arrows, 45 of them with an alert ⚠; grade A 0, B 0, C 45. Shown: the 12 strongest; 33 more arrows (33 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TM4SF4]] | C | TM4SF4 activity raises AGR3's level | lines that do not express TM4SF4 (42) vs lines expressing it (8) | 2.47× lower at baseline in the lines without TM4SF4 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PIGR, MUC17, HHLA2; co-absent with the target |
| [[PIGR]] | C | PIGR activity raises AGR3's level | lines that do not express PIGR (45) vs lines expressing it (5) | 2.57× lower at baseline in the lines without PIGR | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, TM4SF4, APOB; co-absent with the target |
| [[FGFR2]] | C | FGFR2 activity raises AGR3's level | lines that do not express FGFR2 (44) vs lines expressing it (6) | 7.21× lower at baseline in the lines without FGFR2 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC17, REG4, APOA2; co-absent with the target |
| [[MUC5B]] | C | MUC5B activity raises AGR3's level | lines that do not express MUC5B (37) vs lines expressing it (13) | 3.49× lower at baseline in the lines without MUC5B | 0.010 | ⚠ within organs, on part of the lines; also absent: DAPP1, AGR3, ENSG00000259925; co-absent with the target |
| [[MUC17]] | C | MUC17 activity raises AGR3's level | lines that do not express MUC17 (44) vs lines expressing it (6) | 7.37× lower at baseline in the lines without MUC17 | 0.014 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, FGFR2, NPSR1; co-absent with the target |
| [[LYZ]] | C | LYZ activity raises AGR3's level | lines that do not express LYZ (40) vs lines expressing it (10) | 4.16× lower at baseline in the lines without LYZ | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCNT3, TRIM31, MUC17; co-absent with the target |
| [[FAM3D]] | C | FAM3D activity raises AGR3's level | lines that do not express FAM3D (43) vs lines expressing it (7) | 2.99× lower at baseline in the lines without FAM3D | 0.019 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PHGR1, ENSG00000230975, NPSR1; maybe low, not absent; co-absent with the target |
| [[SLC44A4]] | C | SLC44A4 activity raises AGR3's level | lines that do not express SLC44A4 (37) vs lines expressing it (13) | 3.05× lower at baseline in the lines without SLC44A4 | 0.019 | ⚠ within organs, on part of the lines; also absent: ST6GALNAC1, LCN2, NPSR1; co-absent with the target |
| [[NPSR1]] | C | NPSR1 activity raises AGR3's level | lines that do not express NPSR1 (42) vs lines expressing it (8) | 5.44× lower at baseline in the lines without NPSR1 | 0.020 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, MUC17, CDH17; co-absent with the target |
| [[PHGR1]] | C | PHGR1 activity raises AGR3's level | lines that do not express PHGR1 (43) vs lines expressing it (7) | 2.95× lower at baseline in the lines without PHGR1 | 0.022 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FAM3D, GPA33, KRT20; co-absent with the target |
| [[RNF183]] | C | RNF183 activity raises AGR3's level | lines that do not express RNF183 (36) vs lines expressing it (14) | 2.84× lower at baseline in the lines without RNF183 | 0.024 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: EPS8L3, LINC02964, VIL1; co-absent with the target |
| [[ST6GALNAC1]] | C | ST6GALNAC1 activity raises AGR3's level | lines that do not express ST6GALNAC1 (37) vs lines expressing it (13) | 2.98× lower at baseline in the lines without ST6GALNAC1 | 0.026 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC6A14, SLC44A4, STEAP4; co-absent with the target |

### Downstream of this gene

*91 arrows, 91 of them with an alert ⚠; grade A 0, B 18, C 73. Shown: the 12 strongest; 79 more arrows (79 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LNX1]] | B | AGR3 activity raises LNX1's level | lines that do not express AGR3 (42) vs lines expressing it (8) | 9.45× lower at baseline in the lines without AGR3 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGFR2, GABRP, MUC17 |
| [[ATP1B1]] | B | AGR3 activity raises ATP1B1's level | lines that do not express AGR3 (42) vs lines expressing it (8) | 4.09× lower at baseline in the lines without AGR3 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGFR2, GABRP, MUC17 |
| [[HNMT]] | B | AGR3 activity raises HNMT's level | lines that do not express AGR3 (42) vs lines expressing it (8) | 2.63× lower at baseline in the lines without AGR3 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGFR2, GABRP, MUC17 |
| [[GNA14]] | B | AGR3 activity raises GNA14's level | lines that do not express AGR3 (42) vs lines expressing it (8) | 2.85× lower at baseline in the lines without AGR3 | 0.021 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGFR2, GABRP, MUC17 |
| [[RSPH1]] | B | AGR3 activity raises RSPH1's level | lines that do not express AGR3 (42) vs lines expressing it (8) | 2.59× lower at baseline in the lines without AGR3 | 0.022 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGFR2, GABRP, MUC17 |
| [[PLCH1]] | B | AGR3 activity raises PLCH1's level | lines that do not express AGR3 (42) vs lines expressing it (8) | 4.48× lower at baseline in the lines without AGR3 | 0.023 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGFR2, GABRP, MUC17 |
| [[BCL2L15]] | B | AGR3 activity raises BCL2L15's level | lines that do not express AGR3 (42) vs lines expressing it (8) | 3.77× lower at baseline in the lines without AGR3 | 0.027 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGFR2, GABRP, MUC17 |
| [[PTPN22]] | B | AGR3 activity raises PTPN22's level | lines that do not express AGR3 (42) vs lines expressing it (8) | 2.61× lower at baseline in the lines without AGR3 | 0.033 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGFR2, GABRP, MUC17 |
| [[MANSC1]] | B | AGR3 activity raises MANSC1's level | lines that do not express AGR3 (42) vs lines expressing it (8) | 3.18× lower at baseline in the lines without AGR3 | 0.039 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGFR2, GABRP, MUC17 |
| [[FUT2]] | B | AGR3 activity raises FUT2's level | lines that do not express AGR3 (42) vs lines expressing it (8) | 3.17× lower at baseline in the lines without AGR3 | 0.040 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGFR2, GABRP, MUC17 |
| [[FRMD4B]] | B | AGR3 activity raises FRMD4B's level | lines that do not express AGR3 (42) vs lines expressing it (8) | 3.50× lower at baseline in the lines without AGR3 | 0.057 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGFR2, GABRP, MUC17 |
| [[FMO5]] | B | AGR3 activity raises FMO5's level | lines that do not express AGR3 (42) vs lines expressing it (8) | 1.74× lower at baseline in the lines without AGR3 | 0.059 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGFR2, GABRP, MUC17 |

## Where it sits

- **Module**: [[Module 044]] — Defective GALNT12 causes CRCS1; 102 genes; every member is in the + arm (projection on the module's main direction 0.795). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (22.7, 51.4); signed map (63.3, 5.0). **Vector** length 29.0, 13.9% of its response variance represented; |z| ≥ 3 in 125 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Defective GALNT12 causes CRCS1* (reactome, mean cos +0.56 to 5); *Defective GALNT3 causes HFTC* (reactome, mean cos +0.56 to 5); *Defective C1GALT1C1 causes TNPS* (reactome, mean cos +0.56 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.6 | +6.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.5 | +1.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.4 | +9.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.4 | +2.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.4 | +8.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | +0.9 | +1.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | +0.7 | +0.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +0.7 | +1.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +0.7 | -0.0 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -0.9 | -2.5 |
|  | [[4EGI-1 (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.7 | -2.8 |
|  | [[Docetaxel (drug)]] 5 µM |  | -0.6 | -2.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | -0.6 | -1.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -0.6 | -1.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | -0.6 | -0.8 |
|  | [[Phenylephrine (hydrochloride) (drug)]] 0.5 µM |  | -0.5 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | anterior gradient 3, protein disulphide isomerase family member |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p21.1 — chr7:16,859,412-16,881,987 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HAG3, hAG-3, BCMP11, PDIA18 |
| Gene groups (HGNC) | Protein disulfide isomerases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TD06](https://www.uniprot.org/uniprotkb/Q8TD06) (Anterior gradient protein 3):

> Required for calcium-mediated regulation of ciliary beat frequency and mucociliary clearance in the airway. Might be involved in the regulation of intracellular calcium in tracheal epithelial cells.

**Summary**, from NCBI Gene [155465](https://www.ncbi.nlm.nih.gov/gene/155465):

> This gene encodes a member of the disulfide isomerase (PDI) family of endoplasmic reticulum (ER) proteins that catalyze protein folding and thiol-disulfide interchange reactions. The encoded protein has an N-terminal ER-signal sequence, a catalytically active thioredoxin domain, and a C-terminal ER-retention sequence. This gene is expressed in ciliated airway epithelial cells and, in mouse, plays a role in ciliary beat frequency in multiciliated cells. This gene is also over-expressed in …

**Accessions** — [HGNC:24167](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24167) · Entrez [155465](https://www.ncbi.nlm.nih.gov/gene/155465) · UniProt [Q8TD06](https://www.uniprot.org/uniprotkb/Q8TD06) · Ensembl [ENSG00000173467](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173467)

## Data

Gene col 10390: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10390); `tables/drug_effects.parquet` (10 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10390, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10390]; `tensor/DDL_lfc|DDL_z.npy` [10390]; `embed/gene_vectors.npy` [10390]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10390 or target_col == 10390). Every well: [[AGR3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AGR3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
