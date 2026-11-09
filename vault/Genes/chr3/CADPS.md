---
symbol: "CADPS"
type: "gene"
col: 8732
ensembl_id: "ENSG00000163618"
name: "calcium dependent secretion activator"
location: "3p14.2"
module: 55
arm: "+"
pooled_cpm: 25.33
n_lines_expressing: 11
n_dd_up: 7
n_dd_down: 2
n_dd_up_clean: 3
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 10
direction_downstream: 20
tags: ["gene", "module/055"]
generated_by: "tahoemap"
---

# CADPS

*calcium dependent secretion activator* — 3p14.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.50× (z +10.4, q 1e-22, up in 2 of 6 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.87× (z +7.6, q 5e-12, up in 3 of 9 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 0.593× (z -4.6, q 0.002, down in 8 of 8 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (SW1417 0.131×, LS 180 0.169×, HCT15 0.0655×, RPMI-7951 0.0487×, …; ⚠ cell-cycle shift, explains ~91% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 3 lines (HCT15 0.0547×, LS 180 0.220×, SW1417 0.195×); [[Panobinostat (drug)]] 0.5 µM in 2 lines (LS 180 0.0808×, SW1417 0.171×); [[Panobinostat (drug)]] 5 µM in 1 line (LS 180 0.0718×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC01819]] (+0.69, fdr 1e-05), [[TPRXL]] (+0.67, fdr 1e-05), [[TPTEP1-1]] (+0.66, fdr 1e-05).
> It is in [[Module 055]], a single-armed module (Regulation of FZD by ubiquitination).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[TNFRSF14-AS1]] → it (grade C ⚠); 20 go from it, the strongest it → [[TFF2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8732.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.50×** | +10.4 | 1e-22 | 2/6 (C32, LOX-IMVI) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.29×** | +10.3 | 2e-22 | 1/7 (LOX-IMVI) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.87×** | +7.6 | 5e-12 | 3/9 (LoVo, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.52×** | +7.4 | 2e-11 | 1/7 (C32) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.62×** | +4.0 | 0.007 | 0/8 | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.51×** | +3.5 | 0.038 | 0/8 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~2% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.47×** | +3.3 | 0.083 | 2/9 (LOX-IMVI, SK-MEL-2) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.43× | +3.1 | 0.15 | 5/8 (LOX-IMVI, HCT15, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8732.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (SW1417 0.131×, LS 180 0.169×, HCT15 0.0655×, RPMI-7951 0.0487×, …; ⚠ cell-cycle shift, explains ~91% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 3 lines (HCT15 0.0547×, LS 180 0.220×, SW1417 0.195×); [[Panobinostat (drug)]] 0.5 µM in 2 lines (LS 180 0.0808×, SW1417 0.171×); [[Panobinostat (drug)]] 5 µM in 1 line (LS 180 0.0718×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.593×** | -4.6 | 0.002 | 8/8 (LS 180, HCT15, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.634×** | -4.0 | 0.017 | 7/8 (HCT15, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | 0.689× | -3.0 | 0.44 | 0/8 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8732. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 633 | 0 | 11 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0718× (z -15.2) |
| [[HCT15 (line)]] | alt | 87.6 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0655× (z -11.9) ⚠ cell-cycle shift, explains ~91% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0547× (z -9.0) |
| [[SW1417 (line)]] | alt | 263 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.131× (z -15.2) ⚠ cell-cycle shift, explains ~91% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.171× (z -9.3) |
| [[SK-MEL-2 (line)]] | alt | 10.4 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -9.9) ⚠ cell-cycle shift, explains ~91% of this change |
| [[RPMI-7951 (line)]] | alt | 17.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0487× (z -11.0) ⚠ cell-cycle shift, explains ~91% of this change |
| [[A-172 (line)]] | wt | 2.75 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 2.32 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 2.20 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.34 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 4.63 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 3.24 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.78 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.80 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.03 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.23 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.70 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.01 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 3.01 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.14 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.84 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.38 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.66 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 3.14 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.71 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.50 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.81 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.07 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.11 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.43 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.57 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.46 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 3.07 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.55 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.34 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.48 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.07 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.80 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 3.39 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.77 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.84 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 6.97 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.11 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 3.07 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.09 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 6.05 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8732), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01819]] | +0.69 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[TPRXL]] | +0.67 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[TPTEP1-1]] | +0.66 | +0.65 / +0.52 | both halves | 1e-05 |  |
| [[GPX2]] | +0.65 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[NPSR1]] | +0.65 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[EDAR]] | +0.65 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[IGFL2]] | +0.64 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[HEPH]] | +0.64 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[FAM3D]] | +0.63 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[GPA33]] | +0.63 | +0.62 / +0.51 | both halves | 1e-05 |  |
| [[BMP4]] | +0.62 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[SLC5A1]] | +0.62 | +0.56 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 0, C 10.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TNFRSF14-AS1]] | C | TNFRSF14-AS1 activity raises CADPS's level | lines that do not express TNFRSF14-AS1 (23) vs lines expressing it (27) | 2.33× lower at baseline in the lines without TNFRSF14-AS1 | 0.009 | ⚠ within organs, on part of the lines; also absent: ACSL5, LINC01819, MAOB; co-absent with the target |
| [[MUC6]] | C | MUC6 activity raises CADPS's level | lines that do not express MUC6 (45) vs lines expressing it (5) | 4.10× lower at baseline in the lines without MUC6 | 0.023 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, ENSG00000230975, APOB; co-absent with the target |
| [[ARHGAP6]] | C | ARHGAP6 activity raises CADPS's level | lines that do not express ARHGAP6 (32) vs lines expressing it (18) | 1.21× lower at baseline in the lines without ARHGAP6 | 0.053 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PSG4, AMPH, SOX11; co-absent with the target |
| [[GPA33]] | C | GPA33 activity raises CADPS's level | lines that do not express GPA33 (41) vs lines expressing it (9) | 5.75× lower at baseline in the lines without GPA33 | 0.055 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PHGR1, NPSR1, CDH17; co-absent with the target |
| [[LGR6]] | C | LGR6 activity raises CADPS's level | lines that do not express LGR6 (35) vs lines expressing it (15) | 3.40× lower at baseline in the lines without LGR6 | 0.057 | ⚠ within organs, on part of the lines; also absent: SLC6A20, LINC01559, VWA2; co-absent with the target |
| [[ACSL5]] | C | ACSL5 activity raises CADPS's level | lines that do not express ACSL5 (24) vs lines expressing it (26) | 1.88× lower at baseline in the lines without ACSL5 | 0.060 | ⚠ within organs, on part of the lines; also absent: TNFRSF14-AS1, IL20RA, TINAGL1; co-absent with the target |
| [[VSNL1]] | C | VSNL1 activity raises CADPS's level | lines that do not express VSNL1 (34) vs lines expressing it (16) | 3.27× lower at baseline in the lines without VSNL1 | 0.069 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC02964, EDAR, VWA2; co-absent with the target |
| [[LINC02055]] | C | LINC02055 activity raises CADPS's level | lines that do not express LINC02055 (30) vs lines expressing it (20) | 2.22× lower at baseline in the lines without LINC02055 | 0.081 | ⚠ within organs, on part of the lines; also absent: BAGE2, LINC01446, ENSG00000234352; maybe low, not absent; co-absent with the target |
| [[ABO]] | C | ABO activity raises CADPS's level | lines that do not express ABO (32) vs lines expressing it (18) | 2.26× lower at baseline in the lines without ABO | 0.084 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: VWA2, PRSS3, SYK; co-absent with the target |
| [[NKD1]] | C | NKD1 activity raises CADPS's level | lines that do not express NKD1 (34) vs lines expressing it (16) | 3.21× lower at baseline in the lines without NKD1 | 0.093 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000265554, VSNL1, ENSG00000213981; co-absent with the target |

### Downstream of this gene

*20 arrows, 20 of them with an alert ⚠; grade A 0, B 0, C 20. Shown: the 12 strongest; 8 more arrows (8 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TFF2]] | C | CADPS activity raises TFF2's level | lines that do not express CADPS (39) vs lines expressing it (11) | 1.09× lower at baseline in the lines without CADPS | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SOX10, LINC01425, TYR; co-absent with the target |
| [[FAM83F]] | C | CADPS activity raises FAM83F's level | lines that do not express CADPS (39) vs lines expressing it (11) | 2.47× lower at baseline in the lines without CADPS | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SOX10, LINC01425, TYR; co-absent with the target |
| [[CDH17]] | C | CADPS activity raises CDH17's level | lines that do not express CADPS (39) vs lines expressing it (11) | 2.91× lower at baseline in the lines without CADPS | 0.030 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SOX10, LINC01425, TYR; co-absent with the target |
| [[SLC6A20]] | C | CADPS activity raises SLC6A20's level | lines that do not express CADPS (39) vs lines expressing it (11) | 2.82× lower at baseline in the lines without CADPS | 0.033 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SOX10, LINC01425, TYR; co-absent with the target |
| [[FGFR2]] | C | CADPS activity raises FGFR2's level | lines that do not express CADPS (39) vs lines expressing it (11) | 1.08× lower at baseline in the lines without CADPS | 0.035 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SOX10, LINC01425, TYR; co-absent with the target |
| [[VSNL1]] | C | CADPS activity raises VSNL1's level | lines that do not express CADPS (39) vs lines expressing it (11) | 4.13× lower at baseline in the lines without CADPS | 0.036 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SOX10, LINC01425, TYR; co-absent with the target |
| [[ABO]] | C | CADPS activity raises ABO's level | lines that do not express CADPS (39) vs lines expressing it (11) | 2.50× lower at baseline in the lines without CADPS | 0.041 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SOX10, LINC01425, TYR; co-absent with the target |
| [[TNFRSF14-AS1]] | C | CADPS activity raises TNFRSF14-AS1's level | lines that do not express CADPS (39) vs lines expressing it (11) | 1.92× lower at baseline in the lines without CADPS | 0.043 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SOX10, LINC01425, TYR; co-absent with the target |
| [[CALB1]] | C | CADPS activity raises CALB1's level | lines that do not express CADPS (39) vs lines expressing it (11) | 2.83× lower at baseline in the lines without CADPS | 0.043 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SOX10, LINC01425, TYR; co-absent with the target |
| [[HNF4A]] | C | CADPS activity raises HNF4A's level | lines that do not express CADPS (39) vs lines expressing it (11) | 2.54× lower at baseline in the lines without CADPS | 0.048 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SOX10, LINC01425, TYR; co-absent with the target |
| [[EPS8L3]] | C | CADPS activity raises EPS8L3's level | lines that do not express CADPS (39) vs lines expressing it (11) | 2.27× lower at baseline in the lines without CADPS | 0.056 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SOX10, LINC01425, TYR; co-absent with the target |
| [[MUC17]] | C | CADPS activity raises MUC17's level | lines that do not express CADPS (39) vs lines expressing it (11) | 1.76× lower at baseline in the lines without CADPS | 0.062 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SOX10, LINC01425, TYR; co-absent with the target |

## Where it sits

- **Module**: [[Module 055]] — Regulation of FZD by ubiquitination; 87 genes; every member is in the + arm (projection on the module's main direction 0.686). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (20.2, 49.6); signed map (64.6, 8.6). **Vector** length 32.9, 11.4% of its response variance represented; |z| ≥ 3 in 196 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.7 | +10.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.6 | +2.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +1.5 | +4.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.5 | +7.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.3 | +2.7 |
|  | [[venetoclax (drug)]] 5 µM |  | +0.8 | +1.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +0.8 | +0.6 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +0.7 | +1.9 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.9 | -2.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -0.7 | -2.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -0.6 | -0.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -0.6 | -1.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.6 | -2.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | -0.5 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | calcium dependent secretion activator |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p14.2 — chr3:62,398,346-62,875,416 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CAPS, KIAA1121, CAPS1, UNC-31, CADPS1 |
| Gene groups (HGNC) | Pleckstrin homology domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9ULU8](https://www.uniprot.org/uniprotkb/Q9ULU8) (Calcium-dependent secretion activator 1):

> Calcium-binding protein involved in exocytosis of vesicles filled with neurotransmitters and neuropeptides. Probably acts upstream of fusion in the biogenesis or maintenance of mature secretory vesicles. Regulates catecholamine loading of DCVs. May specifically mediate the Ca(2+)-dependent exocytosis of large dense-core vesicles (DCVs) and other dense-core vesicles by acting as a PtdIns(4,5)P2-binding protein that acts at prefusion step following ATP-dependent priming and participates in …

**Summary**, from NCBI Gene [8618](https://www.ncbi.nlm.nih.gov/gene/8618):

> This gene encodes a novel neural/endocrine-specific cytosolic and peripheral membrane protein required for the Ca2+-regulated exocytosis of secretory vesicles. The protein acts at a stage in exocytosis that follows ATP-dependent priming, which involves the essential synthesis of phosphatidylinositol 4,5-bisphosphate (PtdIns(4,5)P2). Alternative splicing has been observed at this locus and three variants, encoding distinct isoforms, are described. [provided by RefSeq, Aug 2008]

**Accessions** — [HGNC:1426](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1426) · Entrez [8618](https://www.ncbi.nlm.nih.gov/gene/8618) · UniProt [Q9ULU8](https://www.uniprot.org/uniprotkb/Q9ULU8) · Ensembl [ENSG00000163618](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163618)

## Data

Gene col 8732: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8732); `tables/drug_effects.parquet` (11 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8732, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8732]; `tensor/DDL_lfc|DDL_z.npy` [8732]; `embed/gene_vectors.npy` [8732]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8732 or target_col == 8732). Every well: [[CADPS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CADPS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
