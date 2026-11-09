---
symbol: "UQCC2"
type: "gene"
col: 5998
ensembl_id: "ENSG00000137288"
name: "ubiquinol-cytochrome c reductase complex assembly factor 2"
location: "6p21.31"
module: 4
arm: "+"
pooled_cpm: 13.2
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 4
n_dd_up_clean: 4
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# UQCC2

*ubiquinol-cytochrome c reductase complex assembly factor 2* — 6p21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.78× (z +11.7, q 5e-29, up in 33 of 37 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 1.54× (z +4.9, q 1e-04, up in 26 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.586× (z -8.8, q 1e-15, down in 32 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 6 lines (NCI-H2030 0.262×, RKO 0.312×, SHP-77 0.350×, HS-578T 0.301×, …); [[Selinexor (drug)]] 5 µM in 1 line (HEC-1-A 0.252×; ⚠ cell-cycle shift, explains ~90% of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (SNU-1 0.0785×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ANAPC7]] (+0.69, fdr 7e-06), [[PPIL1]] (+0.67, fdr 7e-06), [[COQ2]] (+0.62, fdr 2e-05); moves opposite to [[KDELR1]] (-0.61, fdr 7e-06), [[TSC22D4]] (-0.61, fdr 8e-06), [[MKRN1]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[PTP4A3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 9 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5998.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **2.78×** | +11.7 | 5e-29 | 33/37 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **2.52×** | +10.2 | 5e-22 | 18/20 (SW480, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **2.63×** | +8.5 | 3e-15 | 25/32 (SNU-423, HOP62, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.54×** | +4.9 | 1e-04 | 26/46 (NCI-H1573, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.52×** | +4.6 | 5e-04 | 21/46 (SNU-423, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~55% of this change | **1.42×** | +4.0 | 0.006 | 15/40 (SW 900, SNU-423, …) | inconsistent across doses | low cells (technical?) |
| [[Belumosudil (drug)]] 5 µM |  | **1.42×** | +3.9 | 0.008 | 16/47 (LoVo, NCI-H23, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.39×** | +3.8 | 0.011 | 14/47 (LOX-IMVI, LoVo, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.40×** | +3.7 | 0.014 | 16/40 (CFPAC-1, PANC-1, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.38×** | +3.7 | 0.014 | 12/47 (NCI-H1792, Panc 03.27, …) | inconsistent across doses |  |
| [[Pralsetinib (drug)]] 5 µM |  | **1.86×** | +3.3 | 0.054 | 9/43 (NCI-H460, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.31× | +3.1 | 0.11 | 16/45 (NCI-H2030, CFPAC-1, …) | top dose only |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~53% of this change | 1.30× | +3.0 | 0.11 | 6/48 (HOP62, NCI-H2030, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5998.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 6 lines (NCI-H2030 0.262×, RKO 0.312×, SHP-77 0.350×, HS-578T 0.301×, …); [[Selinexor (drug)]] 5 µM in 1 line (HEC-1-A 0.252×; ⚠ cell-cycle shift, explains ~90% of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (SNU-1 0.0785×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.586×** | -8.8 | 1e-15 | 32/47 (NCI-H2030, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.464×** | -4.1 | 0.013 | 20/46 (SK-MEL-2, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~90% of this change | **0.801×** | -3.6 | 0.049 | 22/48 (HEC-1-A, NCI-H2030, …) | all doses, flat | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~84% of this change | **0.737×** | -3.5 | 0.056 | 15/46 (H4, SW 1271, …) | all doses, flat |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~54% of this change | 0.757× | -3.2 | 0.14 | 11/48 (PANC-1, KATO III, …) | all doses, flat |  |
| [[ULK-101 (drug)]] 0.05 µM |  | 0.754× | -3.1 | 0.18 | 12/47 (NCI-H460, RPMI-7951, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.34 per unit of S-phase module lfc, +0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5998. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 23.9 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.96× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.480× (z -8.8) |
| [[NCI-H2030 (line)]] | alt | 22.7 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.262× (z -12.4) |
| [[BT-474 (line)]] | alt | 17.3 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.164× (z -8.8) ⚠ toxic; cell-cycle shift, explains ~75% of this change |
| [[C-33 A (line)]] | alt | 23.5 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.198× (z -8.7) ⚠ cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 13.2 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.252× (z -12.5) ⚠ cell-cycle shift, explains ~90% of this change |
| [[HOP62 (line)]] | alt | 12.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.88× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[HS-578T (line)]] | alt | 12.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.301× (z -9.1) |
| [[LOX-IMVI (line)]] | wt | 10.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.12× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[LS 180 (line)]] | wt | 13.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.263× (z -9.0) |
| [[NCI-H1792 (line)]] | alt | 7.14 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.74× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[NCI-H460 (line)]] | wt | 11.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.91× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[RKO (line)]] | wt | 17.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.312× (z -9.7) |
| [[SHP-77 (line)]] | alt | 21.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.350× (z -9.3) |
| [[SNU-1 (line)]] | wt | 21.7 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0785× (z -11.4) |
| [[SW480 (line)]] | alt | 12.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.51× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[A-172 (line)]] | wt | 9.99 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 23.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 8.02 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.53 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.42 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.12 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.21 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.83 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.22 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.51 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.54 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.68 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.71 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.17 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.13 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 13.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5998), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANAPC7]] | +0.69 | +0.74 / +0.71 | both halves | 7e-06 |  |
| [[PPIL1]] | +0.67 | +0.74 / +0.66 | both halves | 7e-06 |  |
| [[COQ2]] | +0.62 | +0.48 / +0.68 | both halves | 2e-05 |  |
| [[MRPL12]] | +0.62 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[CTPS1]] | +0.61 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[FARSB]] | +0.61 | +0.67 / +0.57 | both halves | 9e-06 |  |
| [[CEP83]] | +0.60 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[MRPL24]] | +0.60 | +0.64 / +0.51 | both halves | 1e-05 |  |
| [[NAA15]] | +0.60 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[YTHDC2]] | +0.60 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[MPHOSPH6]] | +0.60 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[PFAS]] | +0.59 | +0.65 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KDELR1]] | -0.61 | -0.60 / -0.65 | both halves | 7e-06 |  |
| [[TSC22D4]] | -0.61 | -0.61 / -0.58 | both halves | 8e-06 |  |
| [[MKRN1]] | -0.60 | -0.63 / -0.55 | both halves | 1e-05 |  |
| [[GNAS]] | -0.57 | -0.53 / -0.64 | both halves | 1e-05 |  |
| [[AAMDC]] | -0.57 | -0.59 / -0.46 | both halves | 3e-05 |  |
| [[GET1-SH3BGR]] | -0.57 | -0.53 / -0.54 | both halves | 1e-05 |  |
| [[TMEM59]] | -0.56 | -0.65 / -0.50 | both halves | 1e-05 |  |
| [[RSRP1]] | -0.54 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[SPACDR]] | -0.54 | -0.55 / -0.43 | both halves | 3e-05 |  |
| [[SERINC1]] | -0.53 | -0.62 / -0.49 | both halves | 1e-05 |  |
| [[PNPLA7]] | -0.53 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[STX5-DT]] | -0.53 | -0.48 / -0.52 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PTP4A3]] | B | PTP4A3 activity raises UQCC2's level | lines that do not express PTP4A3 (7) vs lines expressing it (43) | 1.48× lower at baseline in the lines without PTP4A3 | 0.035 | ⚠ within organs, on part of the lines; also absent: RHOF, RHPN1, JAG2; maybe low, not absent |
| [[BSN]] | B | BSN activity raises UQCC2's level | lines that do not express BSN (17) vs lines expressing it (33) | 1.37× lower at baseline in the lines without BSN | 0.074 | ⚠ within organs, on part of the lines; also absent: HRK, SPTB, CACNA2D2; maybe low, not absent |
| [[RNFT2]] | C | RNFT2 activity raises UQCC2's level | lines that do not express RNFT2 (3) vs lines expressing it (47) | 1.81× lower at baseline in the lines without RNFT2 | 0.098 | ⚠ few lines (3 vs 47); across organs; also absent: ARHGEF37, CSRP1-AS1, DBNDD1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.554). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-17.9, -45.9); signed map (0.6, -42.7). **Vector** length 71.3, 14.3% of its response variance represented; |z| ≥ 3 in 644 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | +4.4 | +11.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | +4.3 | +4.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | +3.7 | +10.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +3.7 | +4.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.2 | +2.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.9 | +3.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.3 | +3.8 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +1.9 | +3.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.8 | +2.4 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.5 | -8.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~90% of this change | -2.9 | -3.6 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~84% of this change | -2.8 | -3.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -2.4 | -2.6 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~54% of this change | -2.3 | -3.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.7 | -4.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.6 | -2.8 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -1.3 | -1.8 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.2 | -2.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.2 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | ubiquinol-cytochrome c reductase complex assembly factor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.31 — chr6:33,694,293-33,711,727 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC14833, bA6B20.2, M19, Cbp6; previously C6orf125, MNF1 |
| Gene groups (HGNC) | Mitochondrial respiratory chain complex assembly factors; Mitochondrial nucleoid associated proteins |
| Reactome | 3 pathways, smallest: Complex III assembly; Respiratory electron transport; Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BRT2](https://www.uniprot.org/uniprotkb/Q9BRT2) (Ubiquinol-cytochrome c reductase complex assembly factor 2):

> Required for the assembly of the ubiquinol-cytochrome c reductase complex (mitochondrial respiratory chain complex III or cytochrome b-c1 complex). Plays a role in the modulation of respiratory chain activities such as oxygen consumption and ATP production and via its modulation of the respiratory chain activity can regulate skeletal muscle differentiation and insulin secretion by pancreatic beta-cells. Involved in cytochrome b translation and/or stability.

**Summary**, from NCBI Gene [84300](https://www.ncbi.nlm.nih.gov/gene/84300):

> This gene encodes a nucleoid protein localized to the mitochondria inner membrane. The encoded protein affects regulation of insulin secretion, mitochondrial ATP production, and myogenesis through modulation of mitochondrial respiratory chain activity. [provided by RefSeq, Oct 2012]

**Accessions** — [HGNC:21237](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21237) · Entrez [84300](https://www.ncbi.nlm.nih.gov/gene/84300) · UniProt [Q9BRT2](https://www.uniprot.org/uniprotkb/Q9BRT2) · Ensembl [ENSG00000137288](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137288)

## Data

Gene col 5998: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5998); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5998, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5998]; `tensor/DDL_lfc|DDL_z.npy` [5998]; `embed/gene_vectors.npy` [5998]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5998 or target_col == 5998). Every well: [[UQCC2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UQCC2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
