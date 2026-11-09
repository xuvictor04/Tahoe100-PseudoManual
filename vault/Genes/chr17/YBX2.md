---
symbol: "YBX2"
type: "gene"
col: 101
ensembl_id: "ENSG00000006047"
name: "Y-box binding protein 2"
location: "17p13.1"
module: 44
arm: "+"
pooled_cpm: 2.76
n_lines_expressing: 22
n_dd_up: 25
n_dd_down: 1
n_dd_up_clean: 15
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 5
direction_downstream: 21
tags: ["gene", "module/044"]
generated_by: "tahoemap"
---

# YBX2

*Y-box binding protein 2* — 17p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 6.46× (z +12.6, q 1e-33, up in 3 of 4 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 3.31× (z +8.4, q 6e-15, up in 15 of 19 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.573× (z -4.0, q 0.042, down in 10 of 17 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Ixazomib citrate (drug)]] 5 µM in 1 line (LS 180 0.0447×); [[Selinexor (drug)]] 5 µM in 1 line (LS 180 0.116×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GLB1L2]] (+0.64, fdr 1e-05), [[VIL1]] (+0.62, fdr 1e-05), [[MYB]] (+0.62, fdr 1e-05); moves opposite to [[ATG12]] (-0.50, fdr 1e-04), [[TEFM]] (-0.50, fdr 3e-05), [[COA6]] (-0.46, fdr 1e-04).
> It is in [[Module 044]], a single-armed module (Defective GALNT12 causes CRCS1).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[CKMT1A]] → it (grade C ⚠); 21 go from it, the strongest it → [[ARHGAP4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 10 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 101.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **6.46×** | +12.6 | 1e-33 | 3/4 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.45×** | +11.9 | 3e-30 | 6/6 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.79×** | +8.7 | 9e-16 | 3/5 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **3.31×** | +8.4 | 6e-15 | 15/19 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **2.82×** | +7.3 | 4e-11 | 9/17 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.92×** | +6.4 | 1e-08 | 4/14 (A-427, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.39×** | +6.1 | 9e-08 | 4/10 (NCI-H2347, LS 180, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.27×** | +5.8 | 6e-07 | 8/16 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.91×** | +5.3 | 6e-06 | 1/10 (NCI-H2030) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.16×** | +5.2 | 1e-05 | 3/13 (NCI-H1573, COLO 205, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **4.02×** | +5.1 | 2e-05 | 0/4 | top dose only | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.93×** | +4.6 | 2e-04 | 8/19 (SW480, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.54×** | +4.3 | 9e-04 | 1/16 (LoVo) | rises with dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.87×** | +4.2 | 0.001 | 1/9 (SW1417) | inconsistent across doses | cell-cycle shift (explains ~14% here); position effect removed |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.26×** | +4.1 | 0.002 | 0/10 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Thymol (drug)]] 0.5 µM |  | **1.75×** | +3.9 | 0.003 | 1/11 (KATO III) | inconsistent across doses | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.18×** | +3.9 | 0.003 | 0/11 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.72×** | +3.8 | 0.005 | 2/12 (SW480, NCI-H2347) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.66×** | +3.5 | 0.012 | 2/15 (LoVo, BT-474) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Pyridoxine (drug)]] 0.5 µM |  | **1.65×** | +3.5 | 0.012 | 0/11 | inconsistent across doses | low cells (technical?); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.68×** | +3.5 | 0.012 | 3/13 (NCI-H2347, KATO III, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **1.64×** | +3.3 | 0.020 | 3/10 (LS 180, A-427, …) | top dose only | position effect removed |
| [[Oxaprozin (drug)]] 0.5 µM |  | **1.59×** | +3.2 | 0.027 | 0/13 | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 101.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Ixazomib citrate (drug)]] 5 µM in 1 line (LS 180 0.0447×); [[Selinexor (drug)]] 5 µM in 1 line (LS 180 0.116×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.573×** | -4.0 | 0.042 | 10/17 (LS 180, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | 0.630× | -3.3 | 0.29 | 7/15 (LS 180, A-427, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.33 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 101. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 8.87 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0447× (z -12.6) |
| [[A-172 (line)]] | wt | 0.389 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.583 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.467 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.660 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.236 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.283 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.373 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.227 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 8.81 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.183 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.675 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.212 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.616 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.186 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.201 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.221 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.205 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 7.52 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.712 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.214 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.165 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.04 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.148 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 0.974 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.44 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.234 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.75 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.280 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.177 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.398 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.372 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.782 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.205 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.208 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.580 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.839 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.241 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 8.43 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.47 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.24 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 101), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GLB1L2]] | +0.64 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[VIL1]] | +0.62 | +0.63 / +0.50 | both halves | 1e-05 |  |
| [[MYB]] | +0.62 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[MUC6]] | +0.58 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[LRRC45]] | +0.57 | +0.55 / +0.45 | both halves | 3e-05 |  |
| [[CHTF18]] | +0.57 | +0.45 / +0.58 | both halves | 3e-05 |  |
| [[PCK1]] | +0.55 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[SAPCD1]] | +0.54 | +0.49 / +0.46 | both halves | 3e-05 |  |
| [[MSH5]] | +0.54 | +0.48 / +0.46 | both halves | 2e-05 | pathway: HALLMARK_KRAS_SIGNALING_DN |
| [[ENTPD2]] | +0.54 | +0.49 / +0.39 | both halves | 6e-05 |  |
| [[ARHGAP33]] | +0.53 | +0.44 / +0.53 | both halves | 3e-05 |  |
| [[PPP1R1B]] | +0.53 | +0.44 / +0.51 | both halves | 3e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATG12]] | -0.50 | -0.56 / -0.34 | both halves | 1e-04 |  |
| [[TEFM]] | -0.50 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[COA6]] | -0.46 | -0.35 / -0.39 | both halves | 1e-04 |  |
| [[ZNF431]] | -0.45 | -0.37 / -0.41 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 0, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CKMT1A]] | C | CKMT1A activity raises YBX2's level | lines that do not express CKMT1A (28) vs lines expressing it (22) | 2.80× lower at baseline in the lines without CKMT1A | 0.004 | ⚠ within organs, on part of the lines; also absent: CKMT1B, CLDN7, EPCAM; co-absent with the target |
| [[ESRP2]] | C | ESRP2 activity raises YBX2's level | lines that do not express ESRP2 (26) vs lines expressing it (24) | 2.50× lower at baseline in the lines without ESRP2 | 0.021 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: PRSS22, MARVELD3, CRB3; co-absent with the target |
| [[TJP3]] | C | TJP3 activity raises YBX2's level | lines that do not express TJP3 (29) vs lines expressing it (21) | 2.25× lower at baseline in the lines without TJP3 | 0.052 | ⚠ within organs, on part of the lines; also absent: KDF1, EPCAM, CDH1; co-absent with the target |
| [[CHDH]] | C | CHDH activity raises YBX2's level | lines that do not express CHDH (22) vs lines expressing it (28) | 2.27× lower at baseline in the lines without CHDH | 0.064 | ⚠ within organs, on part of the lines; also absent: IL17RB, ESRP2, PRSS22; co-absent with the target |
| [[ENTPD2]] | C | ENTPD2 activity raises YBX2's level | lines that do not express ENTPD2 (22) vs lines expressing it (28) | 2.44× lower at baseline in the lines without ENTPD2 | 0.070 | ⚠ within organs, on part of the lines; also absent: LSR, OCLN, ESRP2; co-absent with the target |

### Downstream of this gene

*21 arrows, 21 of them with an alert ⚠; grade A 0, B 13, C 8. Shown: the 12 strongest; 9 more arrows (9 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARHGAP4]] | B | YBX2 activity raises ARHGAP4's level | lines that do not express YBX2 (28) vs lines expressing it (22) | 1.77× lower at baseline in the lines without YBX2 | 0.003 | ⚠ within organs, on part of the lines; also absent: CKMT1A, PRR15L, FGF9 |
| [[MLXIPL]] | B | YBX2 activity raises MLXIPL's level | lines that do not express YBX2 (28) vs lines expressing it (22) | 2.80× lower at baseline in the lines without YBX2 | 0.006 | ⚠ within organs, on part of the lines; also absent: CKMT1A, PRR15L, FGF9 |
| [[CRACR2B]] | B | YBX2 activity raises CRACR2B's level | lines that do not express YBX2 (28) vs lines expressing it (22) | 2.24× lower at baseline in the lines without YBX2 | 0.012 | ⚠ within organs, on part of the lines; also absent: CKMT1A, PRR15L, FGF9 |
| [[FGFR4]] | B | YBX2 activity raises FGFR4's level | lines that do not express YBX2 (28) vs lines expressing it (22) | 1.83× lower at baseline in the lines without YBX2 | 0.013 | ⚠ within organs, on part of the lines; also absent: CKMT1A, PRR15L, FGF9 |
| [[ASRGL1]] | B | YBX2 activity raises ASRGL1's level | lines that do not express YBX2 (28) vs lines expressing it (22) | 2.06× lower at baseline in the lines without YBX2 | 0.018 | ⚠ within organs, on part of the lines; also absent: CKMT1A, PRR15L, FGF9 |
| [[BRME1]] | B | YBX2 activity raises BRME1's level | lines that do not express YBX2 (28) vs lines expressing it (22) | 1.40× lower at baseline in the lines without YBX2 | 0.026 | ⚠ within organs, on part of the lines; also absent: CKMT1A, PRR15L, FGF9 |
| [[GLB1L2]] | B | YBX2 activity raises GLB1L2's level | lines that do not express YBX2 (28) vs lines expressing it (22) | 2.70× lower at baseline in the lines without YBX2 | 0.034 | ⚠ within organs, on part of the lines; also absent: CKMT1A, PRR15L, FGF9 |
| [[SLC37A4]] | B | YBX2 activity raises SLC37A4's level | lines that do not express YBX2 (28) vs lines expressing it (22) | 1.42× lower at baseline in the lines without YBX2 | 0.038 | ⚠ within organs, on part of the lines; also absent: CKMT1A, PRR15L, FGF9 |
| [[CENPM]] | B | YBX2 activity raises CENPM's level | lines that do not express YBX2 (28) vs lines expressing it (22) | 1.48× lower at baseline in the lines without YBX2 | 0.044 | ⚠ within organs, on part of the lines; also absent: CKMT1A, PRR15L, FGF9 |
| [[PCYT2]] | B | YBX2 activity raises PCYT2's level | lines that do not express YBX2 (28) vs lines expressing it (22) | 1.26× lower at baseline in the lines without YBX2 | 0.051 | ⚠ within organs, on part of the lines; also absent: CKMT1A, PRR15L, FGF9 |
| [[TEDC1]] | B | YBX2 activity raises TEDC1's level | lines that do not express YBX2 (28) vs lines expressing it (22) | 1.37× lower at baseline in the lines without YBX2 | 0.052 | ⚠ within organs, on part of the lines; also absent: CKMT1A, PRR15L, FGF9 |
| [[ARHGEF39]] | B | YBX2 activity raises ARHGEF39's level | lines that do not express YBX2 (28) vs lines expressing it (22) | 1.50× lower at baseline in the lines without YBX2 | 0.055 | ⚠ within organs, on part of the lines; also absent: CKMT1A, PRR15L, FGF9 |

## Where it sits

- **Module**: [[Module 044]] — Defective GALNT12 causes CRCS1; 102 genes; every member is in the + arm (projection on the module's main direction 0.478). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (23.5, 47.0); signed map (63.3, 12.7). **Vector** length 38.2, 8.83% of its response variance represented; |z| ≥ 3 in 437 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.6 | +12.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.1 | +11.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.5 | +8.7 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +2.5 | +6.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.4 | +6.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.1 | +4.3 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.3 | +5.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | +3.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.0 | +2.6 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +0.8 | +2.1 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -1.6 | -4.0 |
|  | [[Selinexor (drug)]] 5 µM |  | -1.4 | +1.8 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -1.4 | -3.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.3 | -1.6 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.3 | -0.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.1 | -2.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.0 | -0.7 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -0.8 | -2.7 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.8 | -2.2 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -0.8 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | Y-box binding protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.1 — chr17:7,288,263-7,294,639 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MSY2, CSDA3, Contrin |
| Gene groups (HGNC) | Y-box binding proteins; Cold shock domain containing |
| Hallmark sets | SPERMATOGENESIS, KRAS_SIGNALING_DN |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y2T7](https://www.uniprot.org/uniprotkb/Q9Y2T7) (Y-box-binding protein 2):

> Major constituent of messenger ribonucleoprotein particles (mRNPs). Involved in the regulation of the stability and/or translation of germ cell mRNAs. Binds to Y-box consensus promoter element. Binds to full-length mRNA with high affinity in a sequence-independent manner. Binds to short RNA sequences containing the consensus site 5'-UCCAUCA-3' with low affinity and limited sequence specificity. Its binding with maternal mRNAs is necessary for its cytoplasmic retention. May mark specific mRNAs …

**Summary**, from NCBI Gene [51087](https://www.ncbi.nlm.nih.gov/gene/51087):

> This gene encodes a nucleic acid binding protein which is highly expressed in germ cells. The encoded protein binds to a Y-box element in the promoters of certain genes but also binds to mRNA transcribed from these genes. Pseudogenes for this gene are located on chromosome 10 and 15. [provided by RefSeq, Feb 2012]

**Accessions** — [HGNC:17948](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17948) · Entrez [51087](https://www.ncbi.nlm.nih.gov/gene/51087) · UniProt [Q9Y2T7](https://www.uniprot.org/uniprotkb/Q9Y2T7) · Ensembl [ENSG00000006047](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000006047)

## Data

Gene col 101: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 101); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 101, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 101]; `tensor/DDL_lfc|DDL_z.npy` [101]; `embed/gene_vectors.npy` [101]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 101 or target_col == 101). Every well: [[YBX2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/YBX2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
