---
symbol: "CSTB"
type: "gene"
col: 8321
ensembl_id: "ENSG00000160213"
name: "cystatin B"
location: "21q22.3"
module: 3
arm: "+"
pooled_cpm: 154.1
n_lines_expressing: 42
n_dd_up: 2
n_dd_down: 0
n_dd_up_clean: 0
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 13
direction_downstream: 6
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# CSTB

*cystatin B* — 21q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.61× (z +6.5, q 4e-08, up in 31 of 41 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 3 lines (SW480 4.39×, NCI-H460 4.59×, A-427 4.89×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SW480 4.74×, NCI-H460 4.70×; ⚠ toxic; transcription drop).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 7 lines (NCI-H2347 0.0730×, CFPAC-1 0.236×, NCI-H1573 0.260×, LOX-IMVI 0.239×, …); [[Belinostat (drug)]] 5 µM in 6 lines (CFPAC-1 0.222×, HepG2/C3A 0.191×, AsPC-1 0.230×, A-172 0.233×, …); [[Panobinostat (drug)]] 5 µM in 4 lines (A-172 0.171×, AsPC-1 0.189×, CFPAC-1 0.194×, NCI-H2347 0.215×; ⚠ cell-cycle shift, explains ~18% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H2347 0.136×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZBTB43]] (+0.64, fdr 7e-06), [[RALA]] (+0.61, fdr 1e-05), [[MXD1]] (+0.61, fdr 1e-05); moves opposite to [[HNRNPR]] (-0.57, fdr 4e-05), [[ILF3]] (-0.57, fdr 2e-05), [[CAPRIN1]] (-0.56, fdr 2e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 13 arrows point to it, the strongest [[NECTIN4]] → it (grade B ⚠); 6 go from it, the strongest it → [[RPL35A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 3 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8321.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 3 lines (SW480 4.39×, NCI-H460 4.59×, A-427 4.89×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SW480 4.74×, NCI-H460 4.70×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.61×** | +6.5 | 4e-08 | 31/41 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.16×** | +5.6 | 8e-06 | 24/37 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~41% of this change | 1.55× | +3.3 | 0.19 | 27/40 (hTERT-HPNE, KATO III, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8321.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 7 lines (NCI-H2347 0.0730×, CFPAC-1 0.236×, NCI-H1573 0.260×, LOX-IMVI 0.239×, …); [[Belinostat (drug)]] 5 µM in 6 lines (CFPAC-1 0.222×, HepG2/C3A 0.191×, AsPC-1 0.230×, A-172 0.233×, …); [[Panobinostat (drug)]] 5 µM in 4 lines (A-172 0.171×, AsPC-1 0.189×, CFPAC-1 0.194×, NCI-H2347 0.215×; ⚠ cell-cycle shift, explains ~18% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H2347 0.136×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | 0.728× | -3.4 | 0.25 | 26/40 (NCI-H2347, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Budesonide (drug)]] 5 µM |  | 0.641× | -3.3 | 0.25 | 32/40 (NCI-H2347, SW 1088, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, +0.44 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8321. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 793 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0730× (z -24.3) |
| [[CFPAC-1 (line)]] | alt | 824 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -13.3) |
| [[NCI-H1573 (line)]] | alt | 228 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.260× (z -11.6) |
| [[A-172 (line)]] | wt | 837 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.171× (z -11.4) ⚠ cell-cycle shift, explains ~18% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.233× (z -9.4) |
| [[AsPC-1 (line)]] | alt | 204 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.189× (z -10.7) ⚠ cell-cycle shift, explains ~18% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.230× (z -9.4) |
| [[HepG2_C3A (line)]] | wt | 95.2 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -10.3) |
| [[A-427 (line)]] | wt | 48.7 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.89× (z +8.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.282× (z -10.4) |
| [[NCI-H460 (line)]] | wt | 41.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.59× (z +9.0) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 38.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.39× (z +9.0) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 290 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -11.3) |
| [[Panc 03.27 (line)]] | alt | 156 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.325× (z -9.8) |
| [[A498 (line)]] | wt | 172 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 76.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 53.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 38.3 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 29.6 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 24.9 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 34.2 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 217 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 103 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 53.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 71.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 67.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 219 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 62.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 83.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 58.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 68.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 98.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 85.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 145 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 57.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 57.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 185 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 22.2 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 63.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 88.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 43.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 48.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 24.0 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 38.0 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 73.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 33.6 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 63.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 76.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 60.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8321), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZBTB43]] | +0.64 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[RALA]] | +0.61 | +0.57 / +0.64 | both halves | 1e-05 |  |
| [[MXD1]] | +0.61 | +0.66 / +0.49 | both halves | 1e-05 |  |
| [[LDAF1]] | +0.60 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[COMMD6]] | +0.59 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[HEBP2]] | +0.59 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[FA2H]] | +0.59 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[CAMLG]] | +0.58 | +0.43 / +0.53 | both halves | 3e-05 |  |
| [[TNFRSF11A]] | +0.57 | +0.57 / +0.45 | both halves | 3e-05 |  |
| [[CIAO2B]] | +0.57 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[PPP1R21]] | +0.57 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[FBXL2]] | +0.56 | +0.49 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HNRNPR]] | -0.57 | -0.42 / -0.63 | both halves | 4e-05 |  |
| [[ILF3]] | -0.57 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[CAPRIN1]] | -0.56 | -0.47 / -0.55 | both halves | 2e-05 |  |
| [[SRSF1]] | -0.56 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[HNRNPL]] | -0.55 | -0.46 / -0.52 | both halves | 3e-05 |  |
| [[ERH]] | -0.55 | -0.42 / -0.57 | both halves | 4e-05 |  |
| [[LMNB2]] | -0.54 | -0.46 / -0.60 | both halves | 3e-05 |  |
| [[POGLUT3]] | -0.54 | -0.43 / -0.47 | both halves | 3e-05 |  |
| [[ATP13A1]] | -0.53 | -0.41 / -0.54 | both halves | 4e-05 |  |
| [[EWSR1]] | -0.53 | -0.36 / -0.54 | both halves | 1e-04 |  |
| [[HNRNPD]] | -0.53 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[ABCE1]] | -0.52 | -0.44 / -0.49 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 13, C 0. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NECTIN4]] | B | NECTIN4 activity raises CSTB's level | lines that do not express NECTIN4 (33) vs lines expressing it (17) | 2.38× lower at baseline in the lines without NECTIN4 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TMEM30B, PRSS8, RAB25 |
| [[S100A14]] | B | S100A14 activity raises CSTB's level | lines that do not express S100A14 (33) vs lines expressing it (17) | 1.89× lower at baseline in the lines without S100A14 | 0.010 | ⚠ within organs, on part of the lines; also absent: PRSS8, RAB25, TMPRSS4 |
| [[ANTXR1]] | B | ANTXR1 activity lowers CSTB's level | lines that do not express ANTXR1 (17) vs lines expressing it (33) | 1.80× higher at baseline in the lines without ANTXR1 | 0.011 | ⚠ within organs, on part of the lines; also absent: VASH1, RFLNB, ENSG00000285804 |
| [[CLDN4]] | B | CLDN4 activity raises CSTB's level | lines that do not express CLDN4 (26) vs lines expressing it (24) | 1.85× lower at baseline in the lines without CLDN4 | 0.019 | ⚠ within organs, on part of the lines; also absent: CDH1, SCNN1A, ITGB6 |
| [[FA2H]] | B | FA2H activity raises CSTB's level | lines that do not express FA2H (27) vs lines expressing it (23) | 1.72× lower at baseline in the lines without FA2H | 0.020 | ⚠ within organs, on part of the lines; also absent: IRF6, ST14, SGPP2 |
| [[BARX2]] | B | BARX2 activity raises CSTB's level | lines that do not express BARX2 (29) vs lines expressing it (21) | 1.94× lower at baseline in the lines without BARX2 | 0.025 | ⚠ within organs, on part of the lines; also absent: COL17A1, FXYD3, CEACAM6 |
| [[NECTIN4]] | B | NECTIN4 activity strengthens CSTB's drug response | lines that do not express NECTIN4 (26) vs lines expressing it (15) | the lines without NECTIN4 respond 1.24× as strongly (z diff -0.26); rises at some drug-doses, falls at others (29% from rises): Homoharringtonine 5 µM: 0.69x vs 0.45x (z diff +2.5); Clobetasol propionate 5 µM: 0.67x vs 0.62x (z diff +1.1); Entrectinib 5 µM: 1.39x vs 1.50x (z diff +0.7) | 0.033 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TMEM30B, PRSS8, RAB25; target measured in part of the lines; both ways; rises at some drug-doses, falls at others; artifact flags |
| [[PTAFR]] | B | PTAFR activity raises CSTB's level | lines that do not express PTAFR (29) vs lines expressing it (21) | 1.55× lower at baseline in the lines without PTAFR | 0.038 | ⚠ within organs, on part of the lines; also absent: TJP3, BSPRY, KDF1; maybe low, not absent |
| [[DZIP1L]] | B | DZIP1L activity lowers CSTB's level | lines that do not express DZIP1L (8) vs lines expressing it (42) | 1.86× higher at baseline in the lines without DZIP1L | 0.043 | ⚠ within organs, on part of the lines; also absent: STARD9, CYP46A1, RECK; maybe low, not absent |
| [[TMCC3]] | B | TMCC3 activity raises CSTB's level | lines that do not express TMCC3 (19) vs lines expressing it (31) | 1.84× lower at baseline in the lines without TMCC3 | 0.074 | ⚠ within organs, on part of the lines; also absent: PTPRB, KRT7, ADGRF4 |
| [[BARX2]] | B | BARX2 activity strengthens CSTB's drug response | lines that do not express BARX2 (24) vs lines expressing it (17) | the lines without BARX2 respond 1.02× as strongly (z diff +0.06); strongest at Homoharringtonine 5 µM: 0.71x vs 0.46x (z diff +2.8) | 0.076 | ⚠ within organs, on part of the lines; also absent: COL17A1, FXYD3, CEACAM6; target measured in part of the lines; both ways; artifact flags |
| [[TTC9]] | B | TTC9 activity raises CSTB's level | lines that do not express TTC9 (23) vs lines expressing it (27) | 1.49× lower at baseline in the lines without TTC9 | 0.089 | ⚠ within organs, on part of the lines; also absent: ITGB4, AREG, SPNS2 |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RPL35A]] | B | CSTB activity raises RPL35A's level | lines that do not express CSTB (8) vs lines expressing it (42) | 1.43× lower at baseline in the lines without CSTB | 0.047 | ⚠ within organs, on part of the lines; also absent: PLAUR, PLS3, ADGRE5; maybe low, not absent |
| [[MICU1]] | B | CSTB activity raises MICU1's level | lines that do not express CSTB (8) vs lines expressing it (42) | 1.44× lower at baseline in the lines without CSTB | 0.050 | ⚠ within organs, on part of the lines; also absent: PLAUR, PLS3, ADGRE5; maybe low, not absent |
| [[BLVRB]] | B | CSTB activity raises BLVRB's level | lines that do not express CSTB (8) vs lines expressing it (42) | 1.66× lower at baseline in the lines without CSTB | 0.051 | ⚠ within organs, on part of the lines; also absent: PLAUR, PLS3, ADGRE5; maybe low, not absent |
| [[RPL28]] | B | CSTB activity raises RPL28's level | lines that do not express CSTB (8) vs lines expressing it (42) | 1.39× lower at baseline in the lines without CSTB | 0.057 | ⚠ within organs, on part of the lines; also absent: PLAUR, PLS3, ADGRE5; maybe low, not absent |
| [[UBE2B]] | B | CSTB activity raises UBE2B's level | lines that do not express CSTB (8) vs lines expressing it (42) | 1.42× lower at baseline in the lines without CSTB | 0.097 | ⚠ within organs, on part of the lines; also absent: PLAUR, PLS3, ADGRE5; maybe low, not absent |
| cells under [[Anethole trithione (drug)]] 0.5 µM | C | CSTB's natural level lowers the cells' numbers under Anethole trithione 0.5 µM (makes them more sensitive) | CSTB's natural level across 40 lines (lineage-adjusted; a glimpse) | r -0.65 | 0.491 over the table, 0.098 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.564). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-40.3, -26.5); signed map (-23.5, 13.0). **Vector** length 86.3, 31.9% of its response variance represented; |z| ≥ 3 in 599 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | +4.0 | -2.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~74% of this change | +3.6 | -0.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.4 | -1.1 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.1 | -2.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.0 | -0.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.9 | +0.1 |
|  | [[Adagrasib (drug)]] 5 µM |  | +2.5 | +2.8 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.4 | +2.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.4 | +0.8 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.1 | +2.1 |
| fall | [[Budesonide (drug)]] 5 µM |  | -2.9 | -3.3 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.7 | -2.8 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.2 | -1.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.1 | -1.4 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | -1.9 | -2.1 |
|  | [[Larotrectinib (drug)]] 5 µM |  | -1.8 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | cystatin B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q22.3 — chr21:43,772,511-43,776,330 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CST6, PME; previously EPM1, STFB |
| Gene groups (HGNC) | Cystatins, type 1 |
| Reactome | 2 pathways, smallest: Neutrophil degranulation; Innate Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [P04080](https://www.uniprot.org/uniprotkb/P04080) (Cystatin-B):

> This is an intracellular thiol proteinase inhibitor. Tightly binding reversible inhibitor of cathepsins L, H and B.

**Summary**, from NCBI Gene [1476](https://www.ncbi.nlm.nih.gov/gene/1476):

> The cystatin superfamily encompasses proteins that contain multiple cystatin-like sequences. Some of the members are active cysteine protease inhibitors, while others have lost or perhaps never acquired this inhibitory activity. There are three inhibitory families in the superfamily, including the type 1 cystatins (stefins), type 2 cystatins and kininogens. This gene encodes a stefin that functions as an intracellular thiol protease inhibitor. The protein is able to form a dimer stabilized by …

**Accessions** — [HGNC:2482](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2482) · Entrez [1476](https://www.ncbi.nlm.nih.gov/gene/1476) · UniProt [P04080](https://www.uniprot.org/uniprotkb/P04080) · Ensembl [ENSG00000160213](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000160213)

## Data

Gene col 8321: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8321); `tables/drug_effects.parquet` (5 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8321, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8321]; `tensor/DDL_lfc|DDL_z.npy` [8321]; `embed/gene_vectors.npy` [8321]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8321 or target_col == 8321). Every well: [[CSTB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CSTB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
