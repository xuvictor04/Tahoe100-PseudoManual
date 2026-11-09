---
symbol: "FRG1FP"
type: "gene"
col: 16003
ensembl_id: "ENSG00000283047"
name: "FSHD region gene 1 family member F, pseudogene"
location: "22p11.2"
module: 9
arm: "+"
pooled_cpm: 2.13
n_lines_expressing: 28
n_dd_up: 11
n_dd_down: 0
n_dd_up_clean: 3
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 9
direction_downstream: 10
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# FRG1FP

*FSHD region gene 1 family member F, pseudogene* — 22p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.43× (z +9.4, q 3e-18, up in 0 of 2 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.80× (z +6.6, q 6e-09, up in 4 of 20 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SK-MEL-2 0.293×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FRG1GP]] (+0.65, fdr 1e-04), [[GRIA2]] (+0.64, fdr 1e-05), [[FRG1DP]] (+0.61, fdr 1e-05); moves opposite to [[XXYLT1]] (-0.45, fdr 1e-04), [[CFL1]] (-0.43, fdr 3e-04), [[SNTB2]] (-0.43, fdr 1e-04).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[NAA11]] → it (grade B ⚠); 10 go from it, the strongest it → [[DACH1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 8 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 16003.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.43×** | +9.4 | 3e-18 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.13×** | +8.4 | 2e-14 | 3/5 (SK-MEL-2, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.80×** | +6.6 | 6e-09 | 4/20 (A-172, SK-MEL-2, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.26×** | +6.5 | 1e-08 | 3/7 (NCI-H1573, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.01×** | +5.3 | 1e-05 | 2/6 (NCI-H1573, HS-578T) | top dose only | cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.52×** | +5.2 | 1e-05 | 0/6 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.67×** | +4.1 | 0.004 | 1/4 (HS-578T) | top dose only | noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.55×** | +3.9 | 0.007 | 0/2 | top dose only | noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.59×** | +3.7 | 0.014 | 1/8 (H4) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +3.6 | 0.021 | 0/12 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.51×** | +3.3 | 0.056 | 2/6 (H4, A-172) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~4% here) |
| [[Bendamustine (drug)]] 5 µM |  | 1.49× | +3.0 | 0.11 | 2/11 (SK-MEL-2, PANC-1) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 16003.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SK-MEL-2 0.293×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ciclopirox (drug)]] 0.5 µM |  | 0.637× | -3.6 | 0.22 | 1/16 (KATO III) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.668× | -3.2 | 0.42 | 7/19 (C32, KATO III, …) | inconsistent across doses |  |
| [[Berberine (chloride hydrate) (drug)]] 0.5 µM |  | 0.680× | -3.0 | 0.44 | 3/15 (SHP-77, SK-MEL-2, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 16003. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SK-MEL-2 (line)]] | alt | 17.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.293× (z -9.6) |
| [[A-172 (line)]] | wt | 4.89 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.56 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.632 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.525 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.623 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.445 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.258 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.357 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.19 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.461 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.43 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.347 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.445 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.425 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.656 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.360 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.873 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.407 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.453 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.302 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.04 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.317 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.55 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.358 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.302 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.669 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.460 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.441 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.340 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.435 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.594 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.339 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.629 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.542 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.453 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.668 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.687 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.552 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.649 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.389 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.536 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 16003), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FRG1GP]] | +0.65 | +0.33 / +0.69 | both halves | 1e-04 |  |
| [[GRIA2]] | +0.64 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[FRG1DP]] | +0.61 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[ASXL3]] | +0.60 | +0.61 / +0.44 | both halves | 3e-05 |  |
| [[LINC02197]] | +0.58 | +0.59 / +0.40 | both halves | 4e-05 |  |
| [[KHDRBS2]] | +0.58 | +0.46 / +0.45 | both halves | 3e-05 |  |
| [[NELL1]] | +0.58 | +0.63 / +0.32 | both halves | 1e-04 |  |
| [[ZNF727]] | +0.58 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[RUNX1T1]] | +0.55 | +0.57 / +0.37 | both halves | 9e-05 |  |
| [[GTSF1]] | +0.55 | +0.53 / +0.43 | both halves | 3e-05 |  |
| [[SYT4]] | +0.54 | +0.50 / +0.39 | both halves | 5e-05 |  |
| [[STK32A]] | +0.54 | +0.51 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[XXYLT1]] | -0.45 | -0.34 / -0.42 | both halves | 1e-04 |  |
| [[CFL1]] | -0.43 | -0.28 / -0.47 | both halves | 3e-04 |  |
| [[SNTB2]] | -0.43 | -0.36 / -0.43 | both halves | 1e-04 |  |
| [[PTRH1]] | -0.43 | -0.29 / -0.44 | both halves | 2e-04 |  |
| [[PLXNA1]] | -0.43 | -0.35 / -0.40 | both halves | 1e-04 |  |
| [[EP400P1]] | -0.43 | -0.46 / -0.26 | both halves | 3e-04 |  |
| [[SLFNL1-AS1]] | -0.43 | -0.30 / -0.36 | both halves | 2e-04 |  |
| [[MAD1L1]] | -0.43 | -0.40 / -0.37 | both halves | 7e-05 |  |
| [[ANKMY1]] | -0.42 | -0.41 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 3, C 6.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NAA11]] | B | NAA11 activity raises FRG1FP's level | lines that do not express NAA11 (39) vs lines expressing it (11) | 3.08× lower at baseline in the lines without NAA11 | 0.014 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CGA, RIT2, ADGRG7; maybe low, not absent |
| [[LINC01518]] | B | LINC01518 activity raises FRG1FP's level | lines that do not express LINC01518 (36) vs lines expressing it (14) | 2.37× lower at baseline in the lines without LINC01518 | 0.026 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000285822, CCDC144NL-AS1, PHF2P2 |
| [[GTSF1]] | B | GTSF1 activity raises FRG1FP's level | lines that do not express GTSF1 (40) vs lines expressing it (10) | 1.99× lower at baseline in the lines without GTSF1 | 0.076 | ⚠ within organs, on part of the lines; also absent: CGA, CALCA, LINC02566 |
| [[FRG1GP]] | C | FRG1GP activity raises FRG1FP's level | lines that do not express FRG1GP (28) vs lines expressing it (22) | 2.62× lower at baseline in the lines without FRG1GP | 0.007 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: BAGE2, TPTE, CCDC144NL-AS1; maybe low, not absent; co-absent with the target |
| [[GABRG2]] | C | GABRG2 activity raises FRG1FP's level | lines that do not express GABRG2 (36) vs lines expressing it (14) | 2.53× lower at baseline in the lines without GABRG2 | 0.028 | ⚠ within organs, on part of the lines; also absent: ENSG00000287211, PCSK1, BAGE2; maybe low, not absent; co-absent with the target |
| [[ZNF208]] | C | ZNF208 activity raises FRG1FP's level | lines that do not express ZNF208 (41) vs lines expressing it (9) | 3.87× lower at baseline in the lines without ZNF208 | 0.034 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000234426, LINC01029, ENSG00000287598; co-absent with the target |
| [[FAM230C]] | C | FAM230C activity raises FRG1FP's level | lines that do not express FAM230C (28) vs lines expressing it (22) | 2.38× lower at baseline in the lines without FAM230C | 0.062 | ⚠ within organs, on part of the lines; also absent: ENSG00000277693, LINC01446, LINC01266; co-absent with the target |
| [[FRG1JP]] | C | FRG1JP activity raises FRG1FP's level | lines that do not express FRG1JP (23) vs lines expressing it (27) | 2.21× lower at baseline in the lines without FRG1JP | 0.073 | ⚠ within organs, on part of the lines; also absent: LSAMP, TRPV2, MSC; maybe low, not absent; co-absent with the target |
| [[STK32A]] | C | STK32A activity raises FRG1FP's level | lines that do not express STK32A (23) vs lines expressing it (27) | 1.92× lower at baseline in the lines without STK32A | 0.088 | ⚠ within organs, on part of the lines; also absent: CHSY3, FRMPD4, SAA1; co-absent with the target |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 3, C 7.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DACH1]] | B | FRG1FP activity raises DACH1's level | lines that do not express FRG1FP (22) vs lines expressing it (28) | 2.47× lower at baseline in the lines without FRG1FP | 0.018 | ⚠ within organs, on part of the lines; also absent: FRG1GP, LINC01446, ENSG00000248973; maybe low, not absent |
| [[TATDN3]] | B | FRG1FP activity raises TATDN3's level | lines that do not express FRG1FP (22) vs lines expressing it (28) | 1.35× lower at baseline in the lines without FRG1FP | 0.025 | ⚠ within organs, on part of the lines; also absent: FRG1GP, LINC01446, ENSG00000248973; maybe low, not absent |
| [[FAM229B]] | B | FRG1FP activity raises FAM229B's level | lines that do not express FRG1FP (22) vs lines expressing it (28) | 1.81× lower at baseline in the lines without FRG1FP | 0.079 | ⚠ within organs, on part of the lines; also absent: FRG1GP, LINC01446, ENSG00000248973; maybe low, not absent |
| [[KC6]] | C | FRG1FP activity raises KC6's level | lines that do not express FRG1FP (22) vs lines expressing it (28) | 3.61× lower at baseline in the lines without FRG1FP | 0.034 | ⚠ within organs, on part of the lines; also absent: FRG1GP, LINC01446, ENSG00000248973; maybe low, not absent; co-absent with the target |
| [[GABRG2]] | C | FRG1FP activity raises GABRG2's level | lines that do not express FRG1FP (22) vs lines expressing it (28) | 2.37× lower at baseline in the lines without FRG1FP | 0.039 | ⚠ within organs, on part of the lines; also absent: FRG1GP, LINC01446, ENSG00000248973; maybe low, not absent; co-absent with the target |
| [[AK4P3]] | C | FRG1FP activity raises AK4P3's level | lines that do not express FRG1FP (22) vs lines expressing it (28) | 2.75× lower at baseline in the lines without FRG1FP | 0.059 | ⚠ within organs, on part of the lines; also absent: FRG1GP, LINC01446, ENSG00000248973; maybe low, not absent; co-absent with the target |
| [[RBM20]] | C | FRG1FP activity raises RBM20's level | lines that do not express FRG1FP (22) vs lines expressing it (28) | 3.29× lower at baseline in the lines without FRG1FP | 0.067 | ⚠ within organs, on part of the lines; also absent: FRG1GP, LINC01446, ENSG00000248973; maybe low, not absent; co-absent with the target |
| [[NRXN1]] | C | FRG1FP activity raises NRXN1's level | lines that do not express FRG1FP (22) vs lines expressing it (28) | 2.15× lower at baseline in the lines without FRG1FP | 0.070 | ⚠ within organs, on part of the lines; also absent: FRG1GP, LINC01446, ENSG00000248973; maybe low, not absent; co-absent with the target |
| [[FRG1DP]] | C | FRG1FP activity raises FRG1DP's level | lines that do not express FRG1FP (22) vs lines expressing it (28) | 2.35× lower at baseline in the lines without FRG1FP | 0.091 | ⚠ within organs, on part of the lines; also absent: FRG1GP, LINC01446, ENSG00000248973; maybe low, not absent; co-absent with the target |
| [[FRG1GP]] | C | FRG1FP activity raises FRG1GP's level | lines that do not express FRG1FP (22) vs lines expressing it (28) | 2.44× lower at baseline in the lines without FRG1FP | 0.096 | ⚠ within organs, on part of the lines; also absent: FRG1GP, LINC01446, ENSG00000248973; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.505). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (36.0, 36.5); signed map (43.9, 35.5). **Vector** length 15.3, 1.46% of its response variance represented; |z| ≥ 3 in 390 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.8 | +6.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.7 | +9.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.5 | +8.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.2 | +1.4 |
|  | [[Selinexor (drug)]] 5 µM |  | +1.1 | +6.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | +0.7 | +1.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.7 | +1.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +0.6 | +1.8 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +0.5 | +2.1 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.8 | -2.8 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -0.6 | -2.2 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -0.6 | -2.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift | -0.5 | -0.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -0.5 | -3.2 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.5 | -0.4 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.5 | -2.5 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -0.5 | -0.5 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -0.4 | -1.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -0.4 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | FSHD region gene 1 family member F, pseudogene |
| Locus type | pseudogene |
| Location | 22p11.2 — chr22:10,939,388-10,961,338 (-) |
| Ensembl biotype | unprocessed_pseudogene |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:51765](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:51765) · Entrez [102723780](https://www.ncbi.nlm.nih.gov/gene/102723780) · Ensembl [ENSG00000283047](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000283047)

## Data

Gene col 16003: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 16003); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 16003, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 16003]; `tensor/DDL_lfc|DDL_z.npy` [16003]; `embed/gene_vectors.npy` [16003]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 16003 or target_col == 16003). Every well: [[FRG1FP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FRG1FP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
