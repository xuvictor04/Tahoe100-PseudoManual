---
symbol: "A1CF"
type: "gene"
col: 7297
ensembl_id: "ENSG00000148584"
name: "APOBEC1 complementation factor"
location: "10q11.23"
module: 27
arm: "+"
pooled_cpm: 4.37
n_lines_expressing: 15
n_dd_up: 17
n_dd_down: 0
n_dd_up_clean: 10
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 29
direction_downstream: 42
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# A1CF

*APOBEC1 complementation factor* — 10q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 5.34× (z +12.4, q 2e-32, up in 3 of 6 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.55× (z +9.5, q 4e-19, up in 3 of 11 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 6 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 4 lines (SW480 0.0513×, COLO 205 0.107×, AsPC-1 0.107×, HepG2/C3A 0.203×; ⚠ cell-cycle shift, explains ~65% of this change); [[Panobinostat (drug)]] 5 µM in 2 lines (COLO 205 0.0620×, SW480 0.0656×; ⚠ cell-cycle shift, explains ~85% of this change); [[Belinostat (drug)]] 5 µM in 2 lines (SW480 0.0404×, COLO 205 0.143×; ⚠ cell-cycle shift, explains ~57% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (COLO 205 0.275×, HepG2/C3A 0.354×); [[Homoharringtonine (drug)]] 5 µM in 1 line (COLO 205 0.289×); [[venetoclax (drug)]] 5 µM in 1 line (COLO 205 0.0403×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC02058]] (+0.78, fdr 7e-06), [[RASSF6]] (+0.78, fdr 7e-06), [[B3GAT1-DT]] (+0.74, fdr 7e-06).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 29 arrows point to it, the strongest [[TFF3]] → it (grade C ⚠); 42 go from it, the strongest it → [[HGD]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 7 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7297.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.34×** | +12.4 | 2e-32 | 3/6 (AsPC-1, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.69×** | +11.0 | 2e-25 | 3/4 (AsPC-1, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.55×** | +9.5 | 4e-19 | 3/11 (HEC-1-A, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.05×** | +7.6 | 4e-12 | 2/4 (A498, AsPC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.89×** | +4.7 | 3e-04 | 2/11 (LoVo, HEC-1-A) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.55×** | +4.4 | 0.001 | 1/11 (AsPC-1) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.73×** | +4.0 | 0.004 | 0/7 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.59×** | +4.0 | 0.005 | 7/11 (HepG2/C3A, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.75×** | +3.9 | 0.005 | 0/8 | top dose only | cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.10×** | +3.9 | 0.006 | 0/5 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.56×** | +3.6 | 0.014 | 0/3 | top dose only | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.42×** | +3.6 | 0.014 | 5/11 (AsPC-1, SW480, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~2% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.63×** | +3.5 | 0.022 | 0/10 | top dose only | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.85×** | +3.2 | 0.051 | 0/7 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Saquinavir (drug)]] 5 µM |  | **1.38×** | +3.2 | 0.051 | 0/11 | rises with dose | position effect removed |
| [[Entrectinib (drug)]] 5 µM |  | **1.51×** | +3.0 | 0.083 | 0/11 | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.52×** | +3.0 | 0.098 | 6/11 (HepG2/C3A, SW480, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7297.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 6 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 4 lines (SW480 0.0513×, COLO 205 0.107×, AsPC-1 0.107×, HepG2/C3A 0.203×; ⚠ cell-cycle shift, explains ~65% of this change); [[Panobinostat (drug)]] 5 µM in 2 lines (COLO 205 0.0620×, SW480 0.0656×; ⚠ cell-cycle shift, explains ~85% of this change); [[Belinostat (drug)]] 5 µM in 2 lines (SW480 0.0404×, COLO 205 0.143×; ⚠ cell-cycle shift, explains ~57% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (COLO 205 0.275×, HepG2/C3A 0.354×); [[Homoharringtonine (drug)]] 5 µM in 1 line (COLO 205 0.289×); [[venetoclax (drug)]] 5 µM in 1 line (COLO 205 0.0403×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | 0.625× | -3.2 | 0.31 | 0/11 | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.655× | -3.2 | 0.31 | 8/11 (SW480, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~14% here) |
| [[BAY1125976 (drug)]] 5 µM |  | 0.445× | -3.1 | 0.31 | 2/11 (AsPC-1, SW480) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Lucanthone (drug)]] 0.05 µM |  | 0.643× | -3.0 | 0.34 | 0/11 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.34 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7297. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 116 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0620× (z -17.3) ⚠ cell-cycle shift, explains ~85% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.275× (z -11.1) |
| [[SW480 (line)]] | alt | 9.53 | 0 | 6 (6 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0404× (z -15.5) ⚠ cell-cycle shift, explains ~57% of this change |
| [[HepG2_C3A (line)]] | wt | 117 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.203× (z -9.4) ⚠ cell-cycle shift, explains ~65% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.354× (z -8.5) |
| [[AsPC-1 (line)]] | alt | 14.5 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.107× (z -9.6) ⚠ cell-cycle shift, explains ~65% of this change |
| [[LS 180 (line)]] | wt | 6.48 | 0 | 1 | — | [[Tofacitinib (citrate) (drug)]] 0.5 µM 0.0553× (z -9.7) |
| [[A-172 (line)]] | wt | 0.620 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.444 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 2.12 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.54 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.640 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.718 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.582 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.709 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.890 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.765 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.673 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.626 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.512 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.555 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.918 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.523 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.557 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.66 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.781 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.476 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.975 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.539 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.543 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.532 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.534 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.623 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.70 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.794 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.518 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.466 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.658 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.581 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.715 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.552 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.722 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.618 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.730 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.784 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.788 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7297), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02058]] | +0.78 | +0.78 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[RASSF6]] | +0.78 | +0.73 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[B3GAT1-DT]] | +0.74 | +0.67 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[HNF1A-AS1]] | +0.73 | +0.74 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[CDX2]] | +0.70 | +0.61 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[TOX3]] | +0.69 | +0.61 / +0.69 | both halves | 7e-06 |  |
| [[C11orf52]] | +0.69 | +0.75 / +0.56 | both halves | 1e-05 |  |
| [[LIPC]] | +0.68 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[AXIN2]] | +0.67 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[PKHD1]] | +0.67 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[MGAM2]] | +0.66 | +0.51 / +0.64 | both halves | 1e-05 |  |
| [[HGD]] | +0.66 | +0.68 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*29 arrows, 29 of them with an alert ⚠; grade A 0, B 0, C 29. Shown: the 12 strongest; 17 more arrows (17 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TFF3]] | C | TFF3 activity raises A1CF's level | lines that do not express TFF3 (38) vs lines expressing it (12) | 4.07× lower at baseline in the lines without TFF3 | 0.004 | ⚠ within organs, on part of the lines; also absent: CEACAM5, MUC17, AGR3; co-absent with the target |
| [[CLRN3]] | C | CLRN3 activity raises A1CF's level | lines that do not express CLRN3 (40) vs lines expressing it (10) | 3.53× lower at baseline in the lines without CLRN3 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, MUC13; co-absent with the target |
| [[VIL1]] | C | VIL1 activity raises A1CF's level | lines that do not express VIL1 (34) vs lines expressing it (16) | 3.28× lower at baseline in the lines without VIL1 | 0.018 | ⚠ within organs, on part of the lines; also absent: LINC02964, NPSR1-AS1, MOGAT3; maybe low, not absent; co-absent with the target |
| [[NPSR1-AS1]] | C | NPSR1-AS1 activity raises A1CF's level | lines that do not express NPSR1-AS1 (34) vs lines expressing it (16) | 3.23× lower at baseline in the lines without NPSR1-AS1 | 0.020 | ⚠ within organs, on part of the lines; also absent: VIL1, A1CF, EPS8L3; maybe low, not absent; co-absent with the target |
| [[TOX3]] | C | TOX3 activity raises A1CF's level | lines that do not express TOX3 (31) vs lines expressing it (19) | 2.62× lower at baseline in the lines without TOX3 | 0.022 | ⚠ within organs, on part of the lines; also absent: GPX2, ENSG00000287426, TMEM45B; co-absent with the target |
| [[MUC13]] | C | MUC13 activity raises A1CF's level | lines that do not express MUC13 (40) vs lines expressing it (10) | 2.95× lower at baseline in the lines without MUC13 | 0.036 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, NPSR1, CDH17; co-absent with the target |
| [[PLA2G2A]] | C | PLA2G2A activity raises A1CF's level | lines that do not express PLA2G2A (41) vs lines expressing it (9) | 3.88× lower at baseline in the lines without PLA2G2A | 0.041 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, ENSG00000248588, CALB1; co-absent with the target |
| [[LYZ]] | C | LYZ activity raises A1CF's level | lines that do not express LYZ (40) vs lines expressing it (10) | 4.33× lower at baseline in the lines without LYZ | 0.044 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCNT3, TRIM31, MUC17; co-absent with the target |
| [[USH1C]] | C | USH1C activity raises A1CF's level | lines that do not express USH1C (34) vs lines expressing it (16) | 2.27× lower at baseline in the lines without USH1C | 0.044 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC13, CLRN3, HHLA2; co-absent with the target |
| [[SULT1C2]] | C | SULT1C2 activity raises A1CF's level | lines that do not express SULT1C2 (30) vs lines expressing it (20) | 2.42× lower at baseline in the lines without SULT1C2 | 0.045 | ⚠ within organs, on part of the lines; also absent: LINC03040, EPS8L3, TMEM139; co-absent with the target |
| [[HNF1A-AS1]] | C | HNF1A-AS1 activity raises A1CF's level | lines that do not express HNF1A-AS1 (31) vs lines expressing it (19) | 2.77× lower at baseline in the lines without HNF1A-AS1 | 0.045 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: HNF1A, EPS8L3, GCNT3; maybe low, not absent; co-absent with the target |
| [[PEG3]] | C | PEG3 activity raises A1CF's level | lines that do not express PEG3 (41) vs lines expressing it (9) | 1.72× lower at baseline in the lines without PEG3 | 0.046 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: APOB, AFP, APOA1; co-absent with the target |

### Downstream of this gene

*42 arrows, 42 of them with an alert ⚠; grade A 0, B 5, C 37. Shown: the 12 strongest; 30 more arrows (30 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HGD]] | B | A1CF activity raises HGD's level | lines that do not express A1CF (35) vs lines expressing it (15) | 4.17× lower at baseline in the lines without A1CF | 0.010 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: VIL1, NPSR1-AS1, MUC13 |
| [[ELF3-AS1]] | B | A1CF activity raises ELF3-AS1's level | lines that do not express A1CF (35) vs lines expressing it (15) | 2.77× lower at baseline in the lines without A1CF | 0.025 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: VIL1, NPSR1-AS1, MUC13 |
| [[RSPH1]] | B | A1CF activity raises RSPH1's level | lines that do not express A1CF (35) vs lines expressing it (15) | 2.02× lower at baseline in the lines without A1CF | 0.045 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: VIL1, NPSR1-AS1, MUC13 |
| [[SLC37A1]] | B | A1CF activity raises SLC37A1's level | lines that do not express A1CF (35) vs lines expressing it (15) | 2.77× lower at baseline in the lines without A1CF | 0.050 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: VIL1, NPSR1-AS1, MUC13 |
| [[BCL2L15]] | B | A1CF activity raises BCL2L15's level | lines that do not express A1CF (35) vs lines expressing it (15) | 2.25× lower at baseline in the lines without A1CF | 0.097 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: VIL1, NPSR1-AS1, MUC13 |
| [[EPS8L3]] | C | A1CF activity raises EPS8L3's level | lines that do not express A1CF (35) vs lines expressing it (15) | 5.95× lower at baseline in the lines without A1CF | 6e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: VIL1, NPSR1-AS1, MUC13; co-absent with the target |
| [[USH1C]] | C | A1CF activity raises USH1C's level | lines that do not express A1CF (35) vs lines expressing it (15) | 7.30× lower at baseline in the lines without A1CF | 1e-03 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: VIL1, NPSR1-AS1, MUC13; co-absent with the target |
| [[MUC13]] | C | A1CF activity raises MUC13's level | lines that do not express A1CF (35) vs lines expressing it (15) | 7.00× lower at baseline in the lines without A1CF | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: VIL1, NPSR1-AS1, MUC13; co-absent with the target |
| [[RASSF6]] | C | A1CF activity raises RASSF6's level | lines that do not express A1CF (35) vs lines expressing it (15) | 5.50× lower at baseline in the lines without A1CF | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: VIL1, NPSR1-AS1, MUC13; co-absent with the target |
| [[HNF1A]] | C | A1CF activity raises HNF1A's level | lines that do not express A1CF (35) vs lines expressing it (15) | 3.06× lower at baseline in the lines without A1CF | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: VIL1, NPSR1-AS1, MUC13; co-absent with the target |
| [[POF1B]] | C | A1CF activity raises POF1B's level | lines that do not express A1CF (35) vs lines expressing it (15) | 4.84× lower at baseline in the lines without A1CF | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: VIL1, NPSR1-AS1, MUC13; co-absent with the target |
| [[VIL1]] | C | A1CF activity raises VIL1's level | lines that do not express A1CF (35) vs lines expressing it (15) | 4.73× lower at baseline in the lines without A1CF | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: VIL1, NPSR1-AS1, MUC13; co-absent with the target |

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.719). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (27.4, 48.7); signed map (57.2, 3.0). **Vector** length 46.8, 17.0% of its response variance represented; |z| ≥ 3 in 345 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.3 | +11.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.5 | +12.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.2 | +7.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.7 | +9.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.6 | +4.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.9 | +2.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +2.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.6 | +4.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.6 | +1.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.6 | +1.5 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -1.5 | -3.2 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.2 | -3.1 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -1.1 | -1.4 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.1 | -1.9 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~18% of this change | -1.0 | -1.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.0 | -1.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.9 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | APOBEC1 complementation factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q11.23 — chr10:50,799,409-50,885,675 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ACF, ASP, ACF64, ACF65, APOBEC1CF |
| Gene groups (HGNC) | RNA binding motif containing |
| Reactome | 4 pathways, smallest: Formation of the Editosome; mRNA Editing: C to U Conversion; mRNA Editing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NQ94](https://www.uniprot.org/uniprotkb/Q9NQ94) (APOBEC1 complementation factor):

> Essential component of the apolipoprotein B mRNA editing enzyme complex which is responsible for the postranscriptional editing of a CAA codon for Gln to a UAA codon for stop in APOB mRNA. Binds to APOB mRNA and is probably responsible for docking the catalytic subunit, APOBEC1, to the mRNA to allow it to deaminate its target cytosine. The complex also protects the edited APOB mRNA from nonsense-mediated decay.

**Summary**, from NCBI Gene [29974](https://www.ncbi.nlm.nih.gov/gene/29974):

> Mammalian apolipoprotein B mRNA undergoes site-specific C to U deamination, which is mediated by a multi-component enzyme complex containing a minimal core composed of APOBEC-1 and a complementation factor encoded by this gene. The gene product has three non-identical RNA recognition motifs and belongs to the hnRNP R family of RNA-binding proteins. It has been proposed that this complementation factor functions as an RNA-binding subunit and docks APOBEC-1 to deaminate the upstream cytidine. …

**Accessions** — [HGNC:24086](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24086) · Entrez [29974](https://www.ncbi.nlm.nih.gov/gene/29974) · UniProt [Q9NQ94](https://www.uniprot.org/uniprotkb/Q9NQ94) · Ensembl [ENSG00000148584](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000148584)

## Data

Gene col 7297: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7297); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7297, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7297]; `tensor/DDL_lfc|DDL_z.npy` [7297]; `embed/gene_vectors.npy` [7297]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7297 or target_col == 7297). Every well: [[A1CF — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/A1CF.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
