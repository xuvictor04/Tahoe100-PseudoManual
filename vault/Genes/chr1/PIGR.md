---
symbol: "PIGR"
type: "gene"
col: 8595
ensembl_id: "ENSG00000162896"
name: "polymeric immunoglobulin receptor"
location: "1q32.1"
module: 44
arm: "+"
pooled_cpm: 12.67
n_lines_expressing: 5
n_dd_up: 16
n_dd_down: 0
n_dd_up_clean: 6
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 17
direction_downstream: 44
tags: ["gene", "module/044"]
generated_by: "tahoemap"
---

# PIGR

*polymeric immunoglobulin receptor* — 1q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 6.44× (z +12.2, q 2e-31, up in 3 of 3 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.99× (z +6.4, q 3e-08, up in 1 of 3 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (LS 180 0.0637×, CFPAC-1 0.0572×, HEC-1-A 0.309×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (LS 180 0.0469×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LYZ]] (+0.71, fdr 7e-06), [[TSPAN8]] (+0.66, fdr 7e-06), [[PPP1R1B]] (+0.65, fdr 1e-05); moves opposite to [[PRKG2-AS1]] (-0.46, fdr 2e-04).
> It is in [[Module 044]], a single-armed module (Defective GALNT12 causes CRCS1).
> Probable direction (from the cell lines, not proof of direct regulation): 17 arrows point to it, the strongest [[TM4SF4]] → it (grade C ⚠); 44 go from it, the strongest it → [[PROM2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 10 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8595.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **6.44×** | +12.2 | 2e-31 | 3/3 (HEC-1-A, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **6.45×** | +11.7 | 3e-29 | 3/3 (HEC-1-A, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.58×** | +9.2 | 7e-18 | 3/3 (HEC-1-A, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.99×** | +6.4 | 3e-08 | 1/3 (HEC-1-A) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.37×** | +5.6 | 2e-06 | 0/3 | top dose only | cell-cycle shift (explains ~10% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.70×** | +4.9 | 9e-05 | 2/3 (HEC-1-A, CFPAC-1) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **4.14×** | +4.9 | 1e-04 | 0/2 | top dose only | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.05×** | +4.7 | 2e-04 | 1/2 (HEC-1-A) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~18% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.95×** | +4.2 | 0.002 | 1/3 (HEC-1-A) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.86×** | +3.9 | 0.006 | 2/3 (CFPAC-1, HEC-1-A) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.85×** | +3.9 | 0.006 | 0/3 | top dose only | cell-cycle shift (explains ~8% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.21×** | +3.5 | 0.026 | 0/2 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.19×** | +3.4 | 0.026 | 1/3 (CFPAC-1) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.69×** | +3.4 | 0.026 | 2/3 (HEC-1-A, CFPAC-1) | rises with dose |  |
| [[Bendamustine (drug)]] 5 µM |  | **1.67×** | +3.2 | 0.046 | 0/3 | top dose only |  |
| [[Omeprazole (drug)]] 0.5 µM |  | **1.62×** | +3.2 | 0.056 | 0/3 | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8595.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (LS 180 0.0637×, CFPAC-1 0.0572×, HEC-1-A 0.309×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (LS 180 0.0469×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dexamethasone (drug)]] 0.5 µM |  | 0.613× | -3.2 | 0.73 | 0/3 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, +0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8595. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 15.1 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 6.42× (z +9.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -8.5) ⚠ cell-cycle shift, would explain all of this change |
| [[LS 180 (line)]] | wt | 480 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0637× (z -22.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0469× (z -18.0) |
| [[CFPAC-1 (line)]] | alt | 4.48 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0572× (z -13.5) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 0.826 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.684 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.13 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.744 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.46 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.11 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.820 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.882 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.782 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.00 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.858 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.869 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.936 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.870 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.852 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.839 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.02 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.15 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.697 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.73 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.18 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.972 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.662 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.731 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.747 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.713 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 2.74 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.795 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.968 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.49 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.627 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.837 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.818 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.754 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.813 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.924 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.867 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.78 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.907 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.896 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.849 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.02 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.763 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8595), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LYZ]] | +0.71 | +0.63 / +0.66 | both halves | 7e-06 | STRING 639 |
| [[TSPAN8]] | +0.66 | +0.65 / +0.58 | both halves | 7e-06 |  |
| [[PPP1R1B]] | +0.65 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[ST6GALNAC1]] | +0.64 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[MSLN]] | +0.63 | +0.69 / +0.51 | both halves | 1e-05 |  |
| [[HNF1A-AS1]] | +0.62 | +0.49 / +0.46 | both halves | 3e-05 |  |
| [[PCK1]] | +0.61 | +0.58 / +0.45 | both halves | 3e-05 |  |
| [[GPA33]] | +0.61 | +0.55 / +0.46 | both halves | 2e-05 | same gene group |
| [[FXYD3]] | +0.61 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[SLC40A1]] | +0.60 | +0.46 / +0.53 | both halves | 3e-05 |  |
| [[UGT1A1]] | +0.60 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[VIL1]] | +0.59 | +0.37 / +0.65 | both halves | 8e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRKG2-AS1]] | -0.46 | -0.48 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 0, C 17. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TM4SF4]] | C | TM4SF4 activity raises PIGR's level | lines that do not express TM4SF4 (42) vs lines expressing it (8) | 4.62× lower at baseline in the lines without TM4SF4 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PIGR, MUC17, HHLA2; co-absent with the target |
| [[NAA11]] | C | NAA11 activity raises PIGR's level | lines that do not express NAA11 (39) vs lines expressing it (11) | 2.35× lower at baseline in the lines without NAA11 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CGA, RIT2, ADGRG7; maybe low, not absent; co-absent with the target |
| [[TCN1]] | C | TCN1 activity raises PIGR's level | lines that do not express TCN1 (37) vs lines expressing it (13) | 2.20× lower at baseline in the lines without TCN1 | 0.034 | ⚠ within organs, on part of the lines; also absent: AGR3, MUC5AC, MUC5B; co-absent with the target |
| [[MUC5B]] | C | MUC5B activity raises PIGR's level | lines that do not express MUC5B (37) vs lines expressing it (13) | 2.39× lower at baseline in the lines without MUC5B | 0.034 | ⚠ within organs, on part of the lines; also absent: DAPP1, AGR3, ENSG00000259925; co-absent with the target |
| [[AGR3]] | C | AGR3 activity raises PIGR's level | lines that do not express AGR3 (42) vs lines expressing it (8) | 3.55× lower at baseline in the lines without AGR3 | 0.034 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGFR2, GABRP, MUC17; co-absent with the target |
| [[PLA2G2A]] | C | PLA2G2A activity raises PIGR's level | lines that do not express PLA2G2A (41) vs lines expressing it (9) | 2.53× lower at baseline in the lines without PLA2G2A | 0.053 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, ENSG00000248588, CALB1; co-absent with the target |
| [[ST6GALNAC1]] | C | ST6GALNAC1 activity raises PIGR's level | lines that do not express ST6GALNAC1 (37) vs lines expressing it (13) | 2.45× lower at baseline in the lines without ST6GALNAC1 | 0.054 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC6A14, SLC44A4, STEAP4; co-absent with the target |
| [[LCN2]] | C | LCN2 activity raises PIGR's level | lines that do not express LCN2 (33) vs lines expressing it (17) | 2.37× lower at baseline in the lines without LCN2 | 0.059 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: PRSS8, RAB25, TMPRSS4; co-absent with the target |
| [[SLC44A4]] | C | SLC44A4 activity raises PIGR's level | lines that do not express SLC44A4 (37) vs lines expressing it (13) | 2.47× lower at baseline in the lines without SLC44A4 | 0.059 | ⚠ within organs, on part of the lines; also absent: ST6GALNAC1, LCN2, NPSR1; co-absent with the target |
| [[RAB25]] | C | RAB25 activity raises PIGR's level | lines that do not express RAB25 (33) vs lines expressing it (17) | 2.36× lower at baseline in the lines without RAB25 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, TMEM30B, PRSS8; co-absent with the target |
| [[REG4]] | C | REG4 activity raises PIGR's level | lines that do not express REG4 (43) vs lines expressing it (7) | 3.74× lower at baseline in the lines without REG4 | 0.072 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC17, NPSR1, ENSG00000230975; co-absent with the target |
| [[SOD3]] | C | SOD3 activity raises PIGR's level | lines that do not express SOD3 (34) vs lines expressing it (16) | 2.32× lower at baseline in the lines without SOD3 | 0.072 | ⚠ within organs, on part of the lines; also absent: PIGR, PHGR1, KRT20; co-absent with the target |

### Downstream of this gene

*44 arrows, 44 of them with an alert ⚠; grade A 0, B 1, C 43. Shown: the 12 strongest; 32 more arrows (32 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PROM2]] | B | PIGR activity raises PROM2's level | lines that do not express PIGR (45) vs lines expressing it (5) | 3.13× lower at baseline in the lines without PIGR | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, TM4SF4, APOB |
| [[MUC5B]] | C | PIGR activity raises MUC5B's level | lines that do not express PIGR (45) vs lines expressing it (5) | 5.74× lower at baseline in the lines without PIGR | 6e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, TM4SF4, APOB; co-absent with the target |
| [[ST6GALNAC1]] | C | PIGR activity raises ST6GALNAC1's level | lines that do not express PIGR (45) vs lines expressing it (5) | 3.44× lower at baseline in the lines without PIGR | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, TM4SF4, APOB; co-absent with the target |
| [[AGR3]] | C | PIGR activity raises AGR3's level | lines that do not express PIGR (45) vs lines expressing it (5) | 2.57× lower at baseline in the lines without PIGR | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, TM4SF4, APOB; co-absent with the target |
| [[TCN1]] | C | PIGR activity raises TCN1's level | lines that do not express PIGR (45) vs lines expressing it (5) | 3.58× lower at baseline in the lines without PIGR | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, TM4SF4, APOB; co-absent with the target |
| [[AMBP]] | C | PIGR activity raises AMBP's level | lines that do not express PIGR (45) vs lines expressing it (5) | 1.94× lower at baseline in the lines without PIGR | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, TM4SF4, APOB; co-absent with the target |
| [[HNF1A-AS1]] | C | PIGR activity raises HNF1A-AS1's level | lines that do not express PIGR (45) vs lines expressing it (5) | 5.41× lower at baseline in the lines without PIGR | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, TM4SF4, APOB; co-absent with the target |
| [[GPA33]] | C | PIGR activity raises GPA33's level | lines that do not express PIGR (45) vs lines expressing it (5) | 3.37× lower at baseline in the lines without PIGR | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, TM4SF4, APOB; co-absent with the target |
| [[RORC]] | C | PIGR activity raises RORC's level | lines that do not express PIGR (45) vs lines expressing it (5) | 3.42× lower at baseline in the lines without PIGR | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, TM4SF4, APOB; co-absent with the target |
| [[SLC44A4]] | C | PIGR activity raises SLC44A4's level | lines that do not express PIGR (45) vs lines expressing it (5) | 4.34× lower at baseline in the lines without PIGR | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, TM4SF4, APOB; co-absent with the target |
| [[MSLN]] | C | PIGR activity raises MSLN's level | lines that do not express PIGR (45) vs lines expressing it (5) | 3.85× lower at baseline in the lines without PIGR | 0.019 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, TM4SF4, APOB; co-absent with the target |
| [[PHGR1]] | C | PIGR activity raises PHGR1's level | lines that do not express PIGR (45) vs lines expressing it (5) | 3.10× lower at baseline in the lines without PIGR | 0.020 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, TM4SF4, APOB; co-absent with the target |

## Where it sits

- **Module**: [[Module 044]] — Defective GALNT12 causes CRCS1; 102 genes; every member is in the + arm (projection on the module's main direction 0.704). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (22.3, 51.0); signed map (65.5, 5.0). **Vector** length 13.9, 6.23% of its response variance represented; |z| ≥ 3 in 59 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Defective GALNT12 causes CRCS1* (reactome, mean cos +0.50 to 5); *Defective GALNT3 causes HFTC* (reactome, mean cos +0.50 to 5); *Defective C1GALT1C1 causes TNPS* (reactome, mean cos +0.50 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.9 | +11.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.8 | +12.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.6 | +9.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.2 | +6.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.0 | +2.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.0 | +4.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +0.7 | +2.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +0.5 | +1.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +0.5 | +3.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +0.5 | +1.4 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.6 | -1.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -0.6 | -1.9 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.5 | -1.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -0.4 | -1.8 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -0.4 | -1.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -0.3 | -1.5 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.3 | -3.2 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -0.3 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | polymeric immunoglobulin receptor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q32.1 — chr1:206,928,522-206,946,466 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | V-set domain containing |
| Hallmark sets | KRAS_SIGNALING_UP |
| Reactome | 2 pathways, smallest: Neutrophil degranulation; Innate Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [P01833](https://www.uniprot.org/uniprotkb/P01833) (Polymeric immunoglobulin receptor):

> [Polymeric immunoglobulin receptor]: Mediates selective transcytosis of polymeric IgA and IgM across mucosal epithelial cells. Binds polymeric IgA and IgM at the basolateral surface of epithelial cells. The complex is then transported across the cell to be secreted at the apical surface. During this process, a cleavage occurs that separates the extracellular (known as the secretory component) from the transmembrane segment.; [Secretory component]: Through its N-linked glycans ensures anchoring …

**Summary**, from NCBI Gene [5284](https://www.ncbi.nlm.nih.gov/gene/5284):

> This gene is a member of the immunoglobulin superfamily. The encoded poly-Ig receptor binds polymeric immunoglobulin molecules at the basolateral surface of epithelial cells; the complex is then transported across the cell to be secreted at the apical surface. A significant association was found between immunoglobulin A nephropathy and several SNPs in this gene.[provided by RefSeq, Sep 2009]

**Accessions** — [HGNC:8968](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8968) · Entrez [5284](https://www.ncbi.nlm.nih.gov/gene/5284) · UniProt [P01833](https://www.uniprot.org/uniprotkb/P01833) · Ensembl [ENSG00000162896](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162896)

## Data

Gene col 8595: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8595); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8595, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8595]; `tensor/DDL_lfc|DDL_z.npy` [8595]; `embed/gene_vectors.npy` [8595]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8595 or target_col == 8595). Every well: [[PIGR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PIGR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
