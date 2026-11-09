---
symbol: "CKMT1A"
type: "gene"
col: 13349
ensembl_id: "ENSG00000223572"
name: "creatine kinase, mitochondrial 1A"
location: "15q15.3"
module: 44
arm: "+"
pooled_cpm: 2.2
n_lines_expressing: 22
n_dd_up: 17
n_dd_down: 0
n_dd_up_clean: 3
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 12
direction_downstream: 31
tags: ["gene", "module/044"]
generated_by: "tahoemap"
---

# CKMT1A

*creatine kinase, mitochondrial 1A* — 15q15.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (14 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 5.52× (z +9.0, q 6e-17, up in 1 of 1 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 2.17× (z +6.3, q 5e-08, up in 7 of 19 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (LoVo 0.0362×, KATO III 0.0699×, COLO 205 0.0874×, LS 180 0.165×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (KATO III 0.0264×, LS 180 0.0612×; ⚠ cell-cycle shift, explains ~17% of this change); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (A-427 0.119×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CKMT1B]] (+0.96, fdr 7e-06), [[PPP1R1B]] (+0.72, fdr 7e-06), [[RAB25]] (+0.70, fdr 1e-05); moves opposite to [[MCPH1-AS1]] (-0.50, fdr 1e-04), [[PPP1R3F]] (-0.50, fdr 7e-05), [[BRD1]] (-0.49, fdr 1e-04).
> It is in [[Module 044]], a single-armed module (Defective GALNT12 causes CRCS1).
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[CKMT1B]] → it (grade C ⚠); 31 go from it, the strongest it → [[PLS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 14 with an alert ⚠; shown: the 15 strongest. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13349.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.52×** | +9.0 | 6e-17 | 1/1 (LoVo) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.80×** | +9.0 | 6e-17 | 6/8 (LS 180, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.11×** | +7.5 | 1e-11 | 2/2 (LS 180, LoVo) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **2.17×** | +6.3 | 5e-08 | 7/19 (NCI-H23, SW48, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **2.53×** | +5.3 | 1e-05 | 8/19 (PANC-1, SW480, …) | rises with dose | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.51×** | +5.3 | 1e-05 | 7/10 (KATO III, LS 180, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~8% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.51×** | +4.8 | 1e-04 | 3/9 (SHP-77, NCI-H23, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.24×** | +4.3 | 0.001 | 2/13 (A-427, NCI-H1573) | top dose only | cell-cycle shift (explains ~18% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.64×** | +4.0 | 0.004 | 1/16 (NCI-H23) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **2.01×** | +4.0 | 0.004 | 7/19 (PANC-1, NCI-H1573, …) | rises with dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.94×** | +3.8 | 0.008 | 8/19 (PANC-1, NCI-H1573, …) | rises with dose |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **3.91×** | +3.7 | 0.011 | 0/6 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.90×** | +3.7 | 0.011 | 2/16 (A-427, Panc 03.27) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.81×** | +3.4 | 0.028 | 6/14 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **1.79×** | +3.2 | 0.046 | 4/15 (KATO III, NCI-H23, …) | top dose only |  |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (LoVo 0.0362×, KATO III 0.0699×, COLO 205 0.0874×, LS 180 0.165×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (KATO III 0.0264×, LS 180 0.0612×; ⚠ cell-cycle shift, explains ~17% of this change); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (A-427 0.119×; ⚠ cell-cycle shift, would explain all of this change).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.48 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13349. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 10.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0699× (z -15.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 8.04 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0612× (z -10.0) ⚠ cell-cycle shift, explains ~17% of this change |
| [[A-427 (line)]] | wt | 6.32 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.119× (z -8.6) ⚠ cell-cycle shift, would explain all of this change |
| [[COLO 205 (line)]] | alt | 9.10 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0874× (z -11.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 16.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0362× (z -23.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 0.144 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.123 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.375 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.309 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.249 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.142 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.250 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.200 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.164 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.178 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.190 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.191 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.154 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.149 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.194 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.134 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.212 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.199 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.138 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.70 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.501 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.565 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.165 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.180 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 9.96 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.353 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.149 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.195 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.385 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.171 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.187 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.92 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.10 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13349), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CKMT1B]] | +0.96 | +0.93 / +0.93 | both halves | 7e-06 | same gene group; STRING 999 |
| [[PPP1R1B]] | +0.72 | +0.73 / +0.63 | both halves | 7e-06 |  |
| [[RAB25]] | +0.70 | +0.72 / +0.55 | both halves | 1e-05 |  |
| [[MUC3A]] | +0.68 | +0.73 / +0.56 | both halves | 1e-05 |  |
| [[ST6GALNAC1]] | +0.66 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[CLDN3]] | +0.66 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[FGFR4]] | +0.64 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[GPX2]] | +0.63 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[KLK7]] | +0.63 | +0.61 / +0.57 | both halves | 1e-05 |  |
| [[CYP4F12]] | +0.62 | +0.62 / +0.48 | both halves | 2e-05 |  |
| [[SLC27A2]] | +0.62 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[PCK1]] | +0.62 | +0.60 / +0.39 | both halves | 5e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MCPH1-AS1]] | -0.50 | -0.42 / -0.36 | both halves | 1e-04 |  |
| [[PPP1R3F]] | -0.50 | -0.37 / -0.40 | both halves | 7e-05 |  |
| [[BRD1]] | -0.49 | -0.35 / -0.41 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 0, C 12.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CKMT1B]] | C | CKMT1B activity raises CKMT1A's level | lines that do not express CKMT1B (28) vs lines expressing it (22) | 3.28× lower at baseline in the lines without CKMT1B | 5e-04 | ⚠ within organs, on part of the lines; also absent: CKMT1A, SYK, PPP1R1B; co-absent with the target |
| [[BSPRY]] | C | BSPRY activity raises CKMT1A's level | lines that do not express BSPRY (29) vs lines expressing it (21) | 3.07× lower at baseline in the lines without BSPRY | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KDF1, EPCAM, RAB25; co-absent with the target |
| [[EPCAM]] | C | EPCAM activity raises CKMT1A's level | lines that do not express EPCAM (28) vs lines expressing it (22) | 2.86× lower at baseline in the lines without EPCAM | 0.004 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, KDF1, CLDN3; co-absent with the target |
| [[SMPDL3B]] | C | SMPDL3B activity raises CKMT1A's level | lines that do not express SMPDL3B (23) vs lines expressing it (27) | 2.46× lower at baseline in the lines without SMPDL3B | 0.008 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: HOOK1, BSPRY, SPINT1-AS1; co-absent with the target |
| [[CLDN3]] | C | CLDN3 activity raises CKMT1A's level | lines that do not express CLDN3 (28) vs lines expressing it (22) | 2.85× lower at baseline in the lines without CLDN3 | 0.015 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, EPCAM, ESRP1; co-absent with the target |
| [[TJP3]] | C | TJP3 activity raises CKMT1A's level | lines that do not express TJP3 (29) vs lines expressing it (21) | 2.52× lower at baseline in the lines without TJP3 | 0.028 | ⚠ within organs, on part of the lines; also absent: KDF1, EPCAM, CDH1; co-absent with the target |
| [[PPP1R1B]] | C | PPP1R1B activity raises CKMT1A's level | lines that do not express PPP1R1B (37) vs lines expressing it (13) | 2.91× lower at baseline in the lines without PPP1R1B | 0.034 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CEACAM5, NPSR1, CDH17; co-absent with the target |
| [[EPHA1]] | C | EPHA1 activity raises CKMT1A's level | lines that do not express EPHA1 (23) vs lines expressing it (27) | 2.01× lower at baseline in the lines without EPHA1 | 0.060 | ⚠ within organs, on part of the lines; also absent: TNNT2, KDF1, PLEKHG6; maybe low, not absent; co-absent with the target |
| [[CBLC]] | C | CBLC activity raises CKMT1A's level | lines that do not express CBLC (31) vs lines expressing it (19) | 2.28× lower at baseline in the lines without CBLC | 0.061 | ⚠ within organs, on part of the lines; also absent: KDF1, CLDN7, PRSS8; co-absent with the target |
| [[MUC3A]] | C | MUC3A activity raises CKMT1A's level | lines that do not express MUC3A (25) vs lines expressing it (25) | 2.24× lower at baseline in the lines without MUC3A | 0.064 | ⚠ within organs, on part of the lines; also absent: HSH2D, ADGRF1, CKMT1B; co-absent with the target |
| [[PIK3AP1]] | C | PIK3AP1 activity raises CKMT1A's level | lines that do not express PIK3AP1 (28) vs lines expressing it (22) | 2.16× lower at baseline in the lines without PIK3AP1 | 0.068 | ⚠ within organs, on part of the lines; also absent: HNF4A, EPS8L3, TMEM139; co-absent with the target |
| [[PLEKHG6]] | C | PLEKHG6 activity raises CKMT1A's level | lines that do not express PLEKHG6 (26) vs lines expressing it (24) | 2.30× lower at baseline in the lines without PLEKHG6 | 0.077 | ⚠ within organs, on part of the lines; also absent: SCNN1A, KDF1, RNF39; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*31 arrows, 31 of them with an alert ⚠; grade A 0, B 5, C 26. Shown: the 12 strongest; 19 more arrows (19 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLS1]] | B | CKMT1A activity raises PLS1's level | lines that do not express CKMT1A (28) vs lines expressing it (22) | 3.71× lower at baseline in the lines without CKMT1A | 0.010 | ⚠ within organs, on part of the lines; also absent: CKMT1B, CLDN7, EPCAM |
| [[FGFR4]] | B | CKMT1A activity raises FGFR4's level | lines that do not express CKMT1A (28) vs lines expressing it (22) | 1.69× lower at baseline in the lines without CKMT1A | 0.013 | ⚠ within organs, on part of the lines; also absent: CKMT1B, CLDN7, EPCAM |
| [[CDC42EP5]] | B | CKMT1A activity raises CDC42EP5's level | lines that do not express CKMT1A (28) vs lines expressing it (22) | 1.53× lower at baseline in the lines without CKMT1A | 0.091 | ⚠ within organs, on part of the lines; also absent: CKMT1B, CLDN7, EPCAM |
| [[GLB1L2]] | B | CKMT1A activity raises GLB1L2's level | lines that do not express CKMT1A (28) vs lines expressing it (22) | 2.46× lower at baseline in the lines without CKMT1A | 0.095 | ⚠ within organs, on part of the lines; also absent: CKMT1B, CLDN7, EPCAM |
| [[PODXL2]] | B | CKMT1A activity raises PODXL2's level | lines that do not express CKMT1A (28) vs lines expressing it (22) | 1.93× lower at baseline in the lines without CKMT1A | 0.095 | ⚠ within organs, on part of the lines; also absent: CKMT1B, CLDN7, EPCAM |
| [[CKMT1B]] | C | CKMT1A activity raises CKMT1B's level | lines that do not express CKMT1A (28) vs lines expressing it (22) | 3.38× lower at baseline in the lines without CKMT1A | 4e-04 | ⚠ within organs, on part of the lines; also absent: CKMT1B, CLDN7, EPCAM; co-absent with the target |
| [[TJP3]] | C | CKMT1A activity raises TJP3's level | lines that do not express CKMT1A (28) vs lines expressing it (22) | 5.12× lower at baseline in the lines without CKMT1A | 0.002 | ⚠ within organs, on part of the lines; also absent: CKMT1B, CLDN7, EPCAM; co-absent with the target |
| [[EPCAM]] | C | CKMT1A activity raises EPCAM's level | lines that do not express CKMT1A (28) vs lines expressing it (22) | 7.48× lower at baseline in the lines without CKMT1A | 0.002 | ⚠ within organs, on part of the lines; also absent: CKMT1B, CLDN7, EPCAM; co-absent with the target |
| [[YBX2]] | C | CKMT1A activity raises YBX2's level | lines that do not express CKMT1A (28) vs lines expressing it (22) | 2.80× lower at baseline in the lines without CKMT1A | 0.004 | ⚠ within organs, on part of the lines; also absent: CKMT1B, CLDN7, EPCAM; co-absent with the target |
| [[BSPRY]] | C | CKMT1A activity raises BSPRY's level | lines that do not express CKMT1A (28) vs lines expressing it (22) | 4.57× lower at baseline in the lines without CKMT1A | 0.005 | ⚠ within organs, on part of the lines; also absent: CKMT1B, CLDN7, EPCAM; co-absent with the target |
| [[CLDN3]] | C | CKMT1A activity raises CLDN3's level | lines that do not express CKMT1A (28) vs lines expressing it (22) | 5.02× lower at baseline in the lines without CKMT1A | 0.007 | ⚠ within organs, on part of the lines; also absent: CKMT1B, CLDN7, EPCAM; co-absent with the target |
| [[PLEKHG6]] | C | CKMT1A activity raises PLEKHG6's level | lines that do not express CKMT1A (28) vs lines expressing it (22) | 3.66× lower at baseline in the lines without CKMT1A | 0.007 | ⚠ within organs, on part of the lines; also absent: CKMT1B, CLDN7, EPCAM; co-absent with the target |

## Where it sits

- **Module**: [[Module 044]] — Defective GALNT12 causes CRCS1; 102 genes; every member is in the + arm (projection on the module's main direction 0.668). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (21.4, 52.6); signed map (63.3, 6.3). **Vector** length 36.5, 7.99% of its response variance represented; |z| ≥ 3 in 373 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.1 | +9.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.9 | +1.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.9 | +9.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.3 | +1.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.2 | +7.5 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.0 | +1.2 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.0 | +1.1 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +0.9 | +1.6 |
|  | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | +0.9 | +2.9 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | -1.6 | -0.8 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.1 | -1.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.0 | -2.3 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -0.9 | -2.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.9 | -1.8 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -0.9 | -2.5 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -0.9 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | creatine kinase, mitochondrial 1A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q15.3 — chr15:43,692,886-43,699,222 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously CKMT1 |
| Gene groups (HGNC) | Proteins encoded by multiple genes; Creatine kinase family |
| Reactome | 2 pathways, smallest: Creatine metabolism; Metabolism of amino acids and derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [P12532](https://www.uniprot.org/uniprotkb/P12532) (Creatine kinase U-type, mitochondrial):

> Reversibly catalyzes the transfer of phosphate between ATP and various phosphogens (e.g. creatine phosphate). Creatine kinase isoenzymes play a central role in energy transduction in tissues with large, fluctuating energy demands, such as skeletal muscle, heart, brain and spermatozoa.

**Summary**, from NCBI Gene [548596](https://www.ncbi.nlm.nih.gov/gene/548596):

> Mitochondrial creatine (MtCK) kinase is responsible for the transfer of high energy phosphate from mitochondria to the cytosolic carrier, creatine. It belongs to the creatine kinase isoenzyme family. It exists as two isoenzymes, sarcomeric MtCK and ubiquitous MtCK, encoded by separate genes. Mitochondrial creatine kinase occurs in two different oligomeric forms: dimers and octamers, in contrast to the exclusively dimeric cytosolic creatine kinase isoenzymes. Many malignant cancers with poor …

**Accessions** — [HGNC:31736](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:31736) · Entrez [548596](https://www.ncbi.nlm.nih.gov/gene/548596) · UniProt [P12532](https://www.uniprot.org/uniprotkb/P12532) · Ensembl [ENSG00000223572](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000223572)

## Data

Gene col 13349: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13349); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13349, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13349]; `tensor/DDL_lfc|DDL_z.npy` [13349]; `embed/gene_vectors.npy` [13349]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13349 or target_col == 13349). Every well: [[CKMT1A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CKMT1A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
