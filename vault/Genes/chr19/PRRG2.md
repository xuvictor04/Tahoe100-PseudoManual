---
symbol: "PRRG2"
type: "gene"
col: 4738
ensembl_id: "ENSG00000126460"
name: "proline rich and Gla domain 2"
location: "19q13.33"
module: 8
arm: "+"
pooled_cpm: 3.53
n_lines_expressing: 44
n_dd_up: 10
n_dd_down: 4
n_dd_up_clean: 5
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 26
direction_downstream: 3
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# PRRG2

*proline rich and Gla domain 2* — 19q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.61× (z +16.8, q 0e+00, up in 17 of 22 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.819× (z -6.5, q 5e-08, down in 20 of 39 measured lines) ⚠ position not correctable. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.585× (z -5.0, q 1e-04, down in 20 of 40 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (HT-29 0.0505×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~80% of this change); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (HEC-1-A 0.186×); [[Saquinavir (drug)]] 0.5 µM in 1 line (HCT15 0.122×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATXN7L3-AS1]] (+0.66, fdr 7e-06), [[HNF1A-AS1]] (+0.64, fdr 1e-05), [[TMC4]] (+0.63, fdr 1e-05); moves opposite to [[LRRC8B]] (-0.50, fdr 2e-04), [[PCNX2]] (-0.50, fdr 2e-04), [[SSX2IP]] (-0.49, fdr 3e-04).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 26 arrows point to it, the strongest [[ESRP1]] → it (grade B ⚠); 3 go from it, the strongest it → [[FCGRT]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4738.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.61×** | +16.8 | 0e+00 | 17/22 (SW480, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.38×** | +7.7 | 4e-12 | 3/5 (SW1417, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.66×** | +6.6 | 8e-09 | 5/37 (SW1417, BT-474, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.03×** | +6.1 | 2e-07 | 3/8 (HEC-1-A, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.79×** | +5.2 | 3e-05 | 4/14 (LS 180, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.73×** | +5.1 | 3e-05 | 7/30 (NCI-H2030, SHP-77, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.71×** | +5.0 | 6e-05 | 3/13 (NCI-H2347, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.71×** | +4.8 | 1e-04 | 6/25 (SW480, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.32×** | +3.6 | 0.017 | 4/36 (LS 180, J82, …) | rises with dose | low cells (technical?) |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.72×** | +3.6 | 0.020 | 4/25 (LS 180, SW480, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4738.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (HT-29 0.0505×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~80% of this change); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (HEC-1-A 0.186×); [[Saquinavir (drug)]] 0.5 µM in 1 line (HCT15 0.122×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **0.819×** | -6.5 | 5e-08 | 20/39 (A-172, A549, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.560×** | -5.4 | 2e-05 | 17/37 (KATO III, SW1417, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.585×** | -5.0 | 1e-04 | 20/40 (KATO III, A-172, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.623×** | -4.2 | 0.003 | 15/32 (SW1417, LoVo, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4738. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HCT15 (line)]] | alt | 16.2 | 0 | 1 | — | [[Saquinavir (drug)]] 0.5 µM 0.122× (z -8.8) |
| [[HEC-1-A (line)]] | alt | 9.99 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.186× (z -8.9) |
| [[HT-29 (line)]] | alt | 10.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0505× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~80% of this change |
| [[A-172 (line)]] | wt | 1.88 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.64 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.975 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.14 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.976 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.21 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.08 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.937 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.78 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.28 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.65 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.666 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.761 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.885 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.04 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.30 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.884 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.36 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.95 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.51 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.679 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.10 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.777 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.907 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.930 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.04 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.879 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.04 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.763 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.989 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.76 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.43 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4738), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATXN7L3-AS1]] | +0.66 | +0.65 / +0.58 | both halves | 7e-06 |  |
| [[HNF1A-AS1]] | +0.64 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[TMC4]] | +0.63 | +0.68 / +0.55 | both halves | 1e-05 |  |
| [[SLC3A1]] | +0.62 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[CCNO-DT]] | +0.61 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[C11orf52]] | +0.61 | +0.66 / +0.49 | both halves | 1e-05 |  |
| [[ADCY4]] | +0.59 | +0.71 / +0.47 | both halves | 2e-05 |  |
| [[DNASE1]] | +0.58 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[FAM177B]] | +0.57 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[KLHL2P1]] | +0.57 | +0.66 / +0.33 | both halves | 1e-04 |  |
| [[MUC20]] | +0.56 | +0.65 / +0.40 | both halves | 4e-05 |  |
| [[SGK2]] | +0.55 | +0.42 / +0.50 | both halves | 4e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRRC8B]] | -0.50 | -0.30 / -0.58 | both halves | 2e-04 |  |
| [[PCNX2]] | -0.50 | -0.30 / -0.51 | both halves | 2e-04 |  |
| [[SSX2IP]] | -0.49 | -0.28 / -0.53 | both halves | 3e-04 |  |
| [[UXS1]] | -0.48 | -0.40 / -0.36 | both halves | 1e-04 |  |
| [[EEFSEC]] | -0.48 | -0.43 / -0.35 | both halves | 1e-04 |  |
| [[CEP83]] | -0.48 | -0.23 / -0.51 | both halves | 5e-04 |  |
| [[IMPDH2]] | -0.48 | -0.42 / -0.35 | both halves | 1e-04 |  |
| [[ARHGDIA]] | -0.48 | -0.33 / -0.51 | both halves | 1e-04 |  |
| [[EIF2B3]] | -0.47 | -0.34 / -0.40 | both halves | 1e-04 |  |
| [[ZMIZ2]] | -0.47 | -0.32 / -0.47 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*26 arrows, 26 of them with an alert ⚠; grade A 0, B 26, C 0. Shown: the 12 strongest; 14 more arrows (14 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ESRP1]] | B | ESRP1 activity raises PRRG2's level | lines that do not express ESRP1 (31) vs lines expressing it (19) | 3.41× lower at baseline in the lines without ESRP1 | 3e-05 | ⚠ within organs, on part of the lines; also absent: ST14, KDF1, CLDN7 |
| [[ERBB3]] | B | ERBB3 activity raises PRRG2's level | lines that do not express ERBB3 (27) vs lines expressing it (23) | 3.01× lower at baseline in the lines without ERBB3 | 9e-05 | ⚠ within organs, on part of the lines; also absent: LAD1, KDF1, EPCAM |
| [[SPINT1-AS1]] | B | SPINT1-AS1 activity raises PRRG2's level | lines that do not express SPINT1-AS1 (27) vs lines expressing it (23) | 2.96× lower at baseline in the lines without SPINT1-AS1 | 3e-04 | ⚠ within organs, on part of the lines; also absent: EPCAM, CLDN3, CRB3 |
| [[FAAH2]] | B | FAAH2 activity raises PRRG2's level | lines that do not express FAAH2 (26) vs lines expressing it (24) | 2.53× lower at baseline in the lines without FAAH2 | 6e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, TNNT2, ST14; maybe low, not absent |
| [[FUT3]] | B | FUT3 activity raises PRRG2's level | lines that do not express FUT3 (29) vs lines expressing it (21) | 2.53× lower at baseline in the lines without FUT3 | 7e-04 | ⚠ within organs, on part of the lines; also absent: ATP2C2, TMEM125, ENSG00000243004 |
| [[TMC4]] | B | TMC4 activity raises PRRG2's level | lines that do not express TMC4 (26) vs lines expressing it (24) | 2.50× lower at baseline in the lines without TMC4 | 0.001 | ⚠ within organs, on part of the lines; also absent: CBLC, TNNT2, CRB3; maybe low, not absent |
| [[RORC]] | B | RORC activity raises PRRG2's level | lines that do not express RORC (30) vs lines expressing it (20) | 2.35× lower at baseline in the lines without RORC | 0.002 | ⚠ within organs, on part of the lines; also absent: LRG1, LINC03040, ATP2C2 |
| [[PRR15-DT]] | B | PRR15-DT activity raises PRRG2's level | lines that do not express PRR15-DT (25) vs lines expressing it (25) | 2.34× lower at baseline in the lines without PRR15-DT | 0.009 | ⚠ within organs, on part of the lines; also absent: PRR15, FAM110C, PLEKHG6; maybe low, not absent |
| [[ACTR3C]] | B | ACTR3C activity raises PRRG2's level | lines that do not express ACTR3C (15) vs lines expressing it (35) | 2.05× lower at baseline in the lines without ACTR3C | 0.015 | ⚠ within organs, on part of the lines; also absent: LRRC61, ENPP4, ENSG00000263325 |
| [[C11orf52]] | B | C11orf52 activity raises PRRG2's level | lines that do not express C11orf52 (23) vs lines expressing it (27) | 2.06× lower at baseline in the lines without C11orf52 | 0.018 | ⚠ within organs, on part of the lines; also absent: TNNT2, MPZL3, RNF39 |
| [[ADCY4]] | B | ADCY4 activity raises PRRG2's level | lines that do not express ADCY4 (33) vs lines expressing it (17) | 2.26× lower at baseline in the lines without ADCY4 | 0.018 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, SLC5A1, CLIC5 |
| [[RNF183]] | B | RNF183 activity raises PRRG2's level | lines that do not express RNF183 (36) vs lines expressing it (14) | 2.56× lower at baseline in the lines without RNF183 | 0.019 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: EPS8L3, LINC02964, VIL1 |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FCGRT]] | B | PRRG2 activity raises FCGRT's level | lines that do not express PRRG2 (6) vs lines expressing it (44) | 1.95× lower at baseline in the lines without PRRG2 | 0.042 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[SPATA6L]] | B | PRRG2 activity raises SPATA6L's level | lines that do not express PRRG2 (6) vs lines expressing it (44) | 2.76× lower at baseline in the lines without PRRG2 | 0.046 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[ERBB3]] | B | PRRG2 activity raises ERBB3's level | lines that do not express PRRG2 (6) vs lines expressing it (44) | 4.18× lower at baseline in the lines without PRRG2 | 0.097 | ⚠ within organs, on part of the lines; maybe low, not absent |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.470). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (28.5, 49.9); signed map (55.8, 1.7). **Vector** length 39.6, 5.30% of its response variance represented; |z| ≥ 3 in 720 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.2 | +16.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.5 | +5.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | +6.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.8 | +6.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.7 | +5.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.1 | +2.6 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.0 | +1.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.0 | +1.3 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.7 | -5.4 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | -2.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | -1.5 | -4.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.3 | -1.6 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -0.9 | -6.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -0.9 | -1.8 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.8 | -2.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.5 µM |  | -0.8 | -1.7 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | -0.8 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | proline rich and Gla domain 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.33 — chr19:49,580,646-49,591,004 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PRGP2 |
| Gene groups (HGNC) | Proline rich and Gla domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [O14669](https://www.uniprot.org/uniprotkb/O14669) (Transmembrane gamma-carboxyglutamic acid protein 2):

> Vitamin K-dependent protein that is essential for calcium homeostasis and haemostasis.

**Summary**, from NCBI Gene [5639](https://www.ncbi.nlm.nih.gov/gene/5639):

> The protein encoded by this gene is a single-pass transmembrane protein containing an N-terminal gamma-carboxyglutamic acid (Gla) domain and tandem Pro/Leu-Pro-Xaa-Tyr (PY) motifs at its C-terminal end. The Gla domain is exposed on the cell surface while the PY motifs are cytoplasmic. The PY motifs of the encoded protein have been shown to interact with YAP1, a WW domain-containing protein. Therefore, it is thought that the encoded protein may be part of a signal transduction pathway. Two …

**Accessions** — [HGNC:9470](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9470) · Entrez [5639](https://www.ncbi.nlm.nih.gov/gene/5639) · UniProt [O14669](https://www.uniprot.org/uniprotkb/O14669) · Ensembl [ENSG00000126460](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000126460)

## Data

Gene col 4738: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4738); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4738, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4738]; `tensor/DDL_lfc|DDL_z.npy` [4738]; `embed/gene_vectors.npy` [4738]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4738 or target_col == 4738). Every well: [[PRRG2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRRG2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
