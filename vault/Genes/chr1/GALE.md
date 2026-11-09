---
symbol: "GALE"
type: "gene"
col: 3894
ensembl_id: "ENSG00000117308"
name: "UDP-galactose-4-epimerase"
location: "1p36.11"
module: 141
arm: "+"
pooled_cpm: 17.67
n_lines_expressing: 49
n_dd_up: 4
n_dd_down: 20
n_dd_up_clean: 1
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 14
direction_downstream: 0
tags: ["gene", "module/141"]
generated_by: "tahoemap"
---

# GALE

*UDP-galactose-4-epimerase* — 1p36.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.71× (z +6.2, q 3e-07, up in 27 of 37 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 1.49× (z +4.6, q 0.001, up in 22 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (AsPC-1 3.52×, A-172 2.81×; ⚠ cell-cycle shift, would explain all of this change).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (3 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.531× (z -7.3, q 1e-10, down in 33 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EPHA2]] (+0.67, fdr 7e-06), [[RIN1]] (+0.66, fdr 1e-05), [[EHD1]] (+0.65, fdr 8e-06); moves opposite to [[FHIP2A]] (-0.60, fdr 7e-06), [[CHPT1]] (-0.56, fdr 1e-05), [[ANP32B]] (-0.55, fdr 3e-05).
> It is in [[Module 141]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 14 arrows point to it, the strongest [[ZNF618]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 4 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3894.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (AsPC-1 3.52×, A-172 2.81×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **1.71×** | +6.2 | 3e-07 | 27/37 (NCI-H460, PANC-1, …) | two highest doses | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.49×** | +4.6 | 0.001 | 22/46 (KATO III, SW1417, …) | two highest doses | cell-cycle shift (explains ~19% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~44% of this change | **1.41×** | +4.0 | 0.012 | 19/43 (AsPC-1, LOX-IMVI, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.34×** | +3.4 | 0.096 | 20/47 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | 1.31× | +3.2 | 0.17 | 16/47 (LOX-IMVI, PANC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3894.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.531×** | -7.3 | 1e-10 | 33/46 (CFPAC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.523×** | -7.1 | 5e-10 | 36/45 (HT-29, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~20% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.571×** | -6.5 | 2e-08 | 31/46 (LS 180, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.585×** | -6.2 | 9e-08 | 31/47 (NCI-H2030, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.608×** | -5.7 | 1e-06 | 28/46 (LS 180, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.376×** | -4.9 | 9e-05 | 27/47 (CFPAC-1, HOP62, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.411×** | -4.5 | 6e-04 | 22/42 (LoVo, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.680×** | -4.4 | 6e-04 | 23/45 (LS 180, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.644×** | -4.3 | 0.001 | 22/47 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.706×** | -4.0 | 0.003 | 16/47 (HOP62, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.723×** | -3.7 | 0.009 | 21/45 (HT-29, LS 180, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.708×** | -3.7 | 0.011 | 14/46 (SW480, SK-MEL-2, …) | all doses, flat |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.482×** | -3.7 | 0.011 | 19/37 (PANC-1, HepG2/C3A, …) | inconsistent across doses | cell-cycle shift (explains ~17% here); noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.720×** | -3.6 | 0.014 | 23/46 (BT-474, HEC-1-A, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.507×** | -3.4 | 0.025 | 13/46 (NCI-H23, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **0.758×** | -3.2 | 0.048 | 13/46 (HT-29, SW480, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.758×** | -3.2 | 0.048 | 19/45 (NCI-H1573, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3894. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 59.9 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.156× (z -18.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.268× (z -9.4) |
| [[KATO III (line)]] | alt | 27.8 | 0 | 3 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.262× (z -9.0) |
| [[LS 180 (line)]] | wt | 25.5 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.119× (z -14.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.218× (z -10.0) |
| [[A-172 (line)]] | wt | 15.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +8.6) ⚠ cell-cycle shift, would explain all of this change | — |
| [[AsPC-1 (line)]] | alt | 20.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.52× (z +10.3) ⚠ cell-cycle shift, would explain all of this change | — |
| [[C32 (line)]] | wt | 11.5 | 0 | 1 | — | [[Cobimetinib (drug)]] 5 µM 0.0533× (z -12.3) |
| [[CFPAC-1 (line)]] | alt | 44.1 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.282× (z -9.2) |
| [[COLO 205 (line)]] | alt | 33.0 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.312× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 24.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.155× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[Hs 766T (line)]] | wt | 20.3 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.334× (z -9.3) ⚠ cell-cycle shift, would explain all of this change |
| [[LoVo (line)]] | wt | 18.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.111× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[PANC-1 (line)]] | alt | 16.9 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0387× (z -10.4) ⚠ toxic |
| [[A-427 (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.89 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.05 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 29.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.15 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.95 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.14 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.83 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.66 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 6.79 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.88 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.03 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 15.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3894), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPHA2]] | +0.67 | +0.62 / +0.69 | both halves | 7e-06 |  |
| [[RIN1]] | +0.66 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[EHD1]] | +0.65 | +0.64 / +0.58 | both halves | 8e-06 |  |
| [[PLK3]] | +0.65 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[EGR2]] | +0.64 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[NFKBIE]] | +0.64 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[EGR3]] | +0.62 | +0.66 / +0.51 | both halves | 1e-05 | pathway: HALLMARK_ESTROGEN_RESPONSE_LATE |
| [[KCTD11]] | +0.62 | +0.55 / +0.70 | both halves | 1e-05 |  |
| [[METTL23]] | +0.62 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[DUSP6]] | +0.61 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[EGR1]] | +0.61 | +0.66 / +0.50 | both halves | 1e-05 |  |
| [[BCL10]] | +0.61 | +0.66 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FHIP2A]] | -0.60 | -0.61 / -0.58 | both halves | 7e-06 |  |
| [[CHPT1]] | -0.56 | -0.56 / -0.51 | both halves | 1e-05 | pathway: HALLMARK_ESTROGEN_RESPONSE_LATE |
| [[ANP32B]] | -0.55 | -0.60 / -0.45 | both halves | 3e-05 |  |
| [[LAMTOR5-AS1]] | -0.54 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[USP46]] | -0.54 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[C8orf44-SGK3]] | -0.54 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[EIF3F]] | -0.53 | -0.38 / -0.57 | both halves | 6e-05 |  |
| [[CSDE1]] | -0.53 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[SLC16A4-AS1]] | -0.53 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[NAAA]] | -0.52 | -0.40 / -0.39 | both halves | 6e-05 |  |
| [[SEPHS1]] | -0.52 | -0.50 / -0.42 | both halves | 4e-05 |  |
| [[DRAM2]] | -0.51 | -0.50 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 13, C 1. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF618]] | B | ZNF618 activity lowers GALE's level | lines that do not express ZNF618 (9) vs lines expressing it (41) | 1.98× higher at baseline in the lines without ZNF618 | 0.009 | ⚠ within organs, on part of the lines; also absent: NCS1, MRAS, GPR63 |
| [[TGFA]] | B | TGFA activity raises GALE's level | lines that do not express TGFA (17) vs lines expressing it (33) | 1.59× lower at baseline in the lines without TGFA | 0.016 | ⚠ within organs, on part of the lines; also absent: AQP3, ELF3, VIPR1 |
| [[LSR]] | B | LSR activity raises GALE's level | lines that do not express LSR (19) vs lines expressing it (31) | 1.63× lower at baseline in the lines without LSR | 0.019 | ⚠ within organs, on part of the lines; also absent: ENTPD2, EPHA10, OCLN |
| [[SH2D3A]] | B | SH2D3A activity raises GALE's level | lines that do not express SH2D3A (24) vs lines expressing it (26) | 1.63× lower at baseline in the lines without SH2D3A | 0.022 | ⚠ within organs, on part of the lines; also absent: GRB7, MYO5B, CRB3 |
| [[AREG]] | B | AREG activity raises GALE's level | lines that do not express AREG (26) vs lines expressing it (24) | 1.56× lower at baseline in the lines without AREG | 0.027 | ⚠ within organs, on part of the lines; also absent: TC2N, ESRP1, CRB3 |
| [[LAMA3]] | B | LAMA3 activity raises GALE's level | lines that do not express LAMA3 (22) vs lines expressing it (28) | 1.61× lower at baseline in the lines without LAMA3 | 0.029 | ⚠ within organs, on part of the lines; also absent: P2RY2, ELF3, MYO5B |
| [[GOLT1A]] | B | GOLT1A activity raises GALE's level | lines that do not express GOLT1A (24) vs lines expressing it (26) | 1.57× lower at baseline in the lines without GOLT1A | 0.041 | ⚠ within organs, on part of the lines; also absent: GRB7, RHOV, ELF3; maybe low, not absent |
| [[PRKG2-AS1]] | B | PRKG2-AS1 activity raises GALE's level | lines that do not express PRKG2-AS1 (23) vs lines expressing it (27) | 1.57× lower at baseline in the lines without PRKG2-AS1 | 0.062 | ⚠ within organs, on part of the lines; also absent: CBLC, B3GNT3, ESRP2; maybe low, not absent |
| [[TRIM15]] | B | TRIM15 activity raises GALE's level | lines that do not express TRIM15 (34) vs lines expressing it (16) | 1.71× lower at baseline in the lines without TRIM15 | 0.065 | ⚠ within organs, on part of the lines; also absent: TMEM45B, EPS8L3, ENSG00000225680 |
| [[ZNF618]] | B | ZNF618 activity weakens GALE's drug response | lines that do not express ZNF618 (9) vs lines expressing it (38) | the lines without ZNF618 respond 1.31× as strongly (z diff -0.49); strongest at Ixazomib citrate 5 µM: 0.35x vs 0.56x (z diff -3.3) | 0.070 | ⚠ within organs, on part of the lines; also absent: NCS1, MRAS, GPR63; target measured in part of the lines; artifact flags |
| [[FAM110C]] | B | FAM110C activity raises GALE's level | lines that do not express FAM110C (26) vs lines expressing it (24) | 1.58× lower at baseline in the lines without FAM110C | 0.082 | ⚠ within organs, on part of the lines; also absent: PRR15-DT, PRR15, PLEKHG6 |
| [[LINC00659]] | B | LINC00659 activity raises GALE's level | lines that do not express LINC00659 (26) vs lines expressing it (24) | 1.54× lower at baseline in the lines without LINC00659 | 0.083 | ⚠ within organs, on part of the lines; also absent: KLK6, TRIM15, ENSG00000225680 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 141]] — TNF-alpha signaling via NF-kB; 33 genes; every member is in the + arm (projection on the module's main direction 0.751). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (38.8, -1.0); signed map (6.4, 31.4). **Vector** length 89.3, 21.3% of its response variance represented; |z| ≥ 3 in 819 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *TNF-alpha signaling via NF-kB* (hallmark, mean cos +0.53 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +5.8 | +2.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.4 | +4.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.3 | +2.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.7 | +2.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | +2.7 | +3.2 |
|  | [[Entrectinib (drug)]] 5 µM |  | +2.2 | +2.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.0 | +0.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.9 | +2.3 |
|  | [[Belzutifan (drug)]] 5 µM |  | +1.9 | +2.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.8 | +1.4 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -4.7 | -7.3 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -3.9 | -7.1 |
|  | [[Trametinib (drug)]] 5 µM |  | -3.6 | -4.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.4 | -3.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.3 | -3.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.2 | -2.9 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -3.1 | -2.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -2.8 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | UDP-galactose-4-epimerase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.11 — chr1:23,795,599-23,800,781 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SDR1E1 |
| Gene groups (HGNC) | Short chain dehydrogenase/reductase superfamily |
| Hallmark sets | ESTROGEN_RESPONSE_LATE, GLYCOLYSIS |
| Reactome | 5 pathways, smallest: Galactose catabolism; Diseases associated with glycosylation precursor biosynthesis; Diseases of glycosylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14376](https://www.uniprot.org/uniprotkb/Q14376) (UDP-glucose 4-epimerase):

> Catalyzes two distinct but analogous reactions: the reversible epimerization of UDP-glucose to UDP-galactose and the reversible epimerization of UDP-N-acetylglucosamine to UDP-N-acetylgalactosamine. The reaction with UDP-Gal plays a critical role in the Leloir pathway of galactose catabolism in which galactose is converted to the glycolytic intermediate glucose 6-phosphate. It contributes to the catabolism of dietary galactose and enables the endogenous biosynthesis of both UDP-Gal and …

**Summary**, from NCBI Gene [2582](https://www.ncbi.nlm.nih.gov/gene/2582):

> This gene encodes UDP-galactose-4-epimerase which catalyzes two distinct but analogous reactions: the epimerization of UDP-glucose to UDP-galactose, and the epimerization of UDP-N-acetylglucosamine to UDP-N-acetylgalactosamine. The bifunctional nature of the enzyme has the important metabolic consequence that mutant cells (or individuals) are dependent not only on exogenous galactose, but also on exogenous N-acetylgalactosamine as a necessary precursor for the synthesis of glycoproteins and …

**Accessions** — [HGNC:4116](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4116) · Entrez [2582](https://www.ncbi.nlm.nih.gov/gene/2582) · UniProt [Q14376](https://www.uniprot.org/uniprotkb/Q14376) · Ensembl [ENSG00000117308](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000117308)

## Data

Gene col 3894: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3894); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3894, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3894]; `tensor/DDL_lfc|DDL_z.npy` [3894]; `embed/gene_vectors.npy` [3894]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3894 or target_col == 3894). Every well: [[GALE — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GALE.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
