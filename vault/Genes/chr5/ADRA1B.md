---
symbol: "ADRA1B"
type: "gene"
col: 9915
ensembl_id: "ENSG00000170214"
name: "adrenoceptor alpha 1B"
location: "5q33.3"
module: 97
arm: "+"
pooled_cpm: 6.32
n_lines_expressing: 26
n_dd_up: 30
n_dd_down: 2
n_dd_up_clean: 21
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 6
direction_downstream: 7
tags: ["gene", "module/097"]
generated_by: "tahoemap"
---

# ADRA1B

*adrenoceptor alpha 1B* — 5q33.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (9 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.31× (z +13.4, q 2e-38, up in 20 of 22 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.910× (z -3.9, q 0.037, down in 6 of 24 measured lines) ⚠ position not correctable. The strongest without an alert is [[Trametinib (drug)]] 0.05 µM: 0.784× (z -3.8, q 0.037, down in 5 of 22 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (A-172 0.172×, NCI-H23 0.109×, HEC-1-A 0.365×; ⚠ cell-cycle shift, explains ~47% of this change); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 2 lines (HEC-1-A 0.0719×, A-172 0.179×); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (NCI-H2030 0.172×, A-172 0.294×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 2 lines (HEC-1-A 0.238×, SW480 0.272×); [[Homoharringtonine (drug)]] 5 µM in 1 line (SK-MEL-2 0.112×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRNP1]] (+0.59, fdr 2e-05), [[RHOBTB2]] (+0.58, fdr 3e-05), [[CAMK4]] (+0.55, fdr 3e-05); moves opposite to [[NCOA2]] (-0.53, fdr 6e-05), [[PCMTD1]] (-0.52, fdr 4e-05), [[PXDNL]] (-0.49, fdr 9e-05).
> It is in [[Module 097]], a single-armed module (estrogen response early).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[KCNMB4]] → it (grade B ⚠); 7 go from it, the strongest it → cells under [[Cobimetinib (drug)]] 5 µM (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9915.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.31×** | +13.4 | 2e-38 | 20/22 (NCI-H2347, NCI-H460, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.94×** | +10.6 | 1e-23 | 12/21 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.31×** | +9.5 | 5e-19 | 17/22 (NCI-H2347, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **2.32×** | +9.2 | 6e-18 | 0/12 | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM |  | **2.13×** | +8.5 | 2e-15 | 18/22 (PANC-1, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.94×** | +7.5 | 5e-12 | 14/22 (NCI-H2347, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.94×** | +7.5 | 5e-12 | 14/22 (NCI-H2347, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~25% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.92×** | +7.4 | 1e-11 | 15/22 (NCI-H2030, SW480, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **1.87×** | +7.1 | 9e-11 | 7/21 (NCI-H1573, HOP62, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.79×** | +6.3 | 1e-08 | 15/22 (A-172, A498, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.67×** | +5.8 | 3e-07 | 11/21 (A-172, A498, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.54×** | +5.5 | 2e-06 | 13/22 (PANC-1, SNU-423, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Budesonide (drug)]] 0.5 µM |  | **1.62×** | +5.5 | 2e-06 | 7/22 (NCI-H2347, PANC-1, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **1.68×** | +5.4 | 3e-06 | 1/14 (NCI-H2347) | all doses, stronger at high dose | composition shift |
| [[Brivudine (drug)]] 5 µM |  | **2.47×** | +5.4 | 3e-06 | 10/23 (NCI-H2347, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Budesonide (drug)]] 0.05 µM |  | **1.56×** | +5.1 | 2e-05 | 8/22 (NCI-H2347, A549, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.38×** | +3.7 | 0.007 | 9/22 (NCI-H2347, A549, …) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **1.35×** | +3.4 | 0.017 | 7/22 (NCI-H2347, A549, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **1.36×** | +3.3 | 0.022 | 6/22 (NCI-H2347, PANC-1, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9915.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (A-172 0.172×, NCI-H23 0.109×, HEC-1-A 0.365×; ⚠ cell-cycle shift, explains ~47% of this change); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 2 lines (HEC-1-A 0.0719×, A-172 0.179×); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (NCI-H2030 0.172×, A-172 0.294×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 2 lines (HEC-1-A 0.238×, SW480 0.272×); [[Homoharringtonine (drug)]] 5 µM in 1 line (SK-MEL-2 0.112×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.910× | -3.9 | 0.037 | 6/24 (SNU-423, NCI-H1792, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.784×** | -3.8 | 0.037 | 5/22 (CFPAC-1, NCI-H460, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.794×** | -3.7 | 0.039 | 15/22 (A498, SK-MEL-2, …) | top dose only | low cells (technical?) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 0.737× | -3.3 | 0.12 | 9/22 (NCI-H1792, SK-MEL-2, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | 0.745× | -3.2 | 0.15 | 14/22 (HEC-1-A, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.743× | -3.1 | 0.17 | 3/22 (SK-MEL-2, Panc 03.27, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9915. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 40.7 | 2 (1 ⚠) | 5 (3 ⚠) | [[Harringtonine (drug)]] 5 µM 5.77× (z +12.6) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.59× (z +10.1) | [[Dinaciclib (drug)]] 0.05 µM 0.0501× (z -20.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.179× (z -12.4) |
| [[HEC-1-A (line)]] | alt | 22.9 | 0 | 3 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0719× (z -17.0) |
| [[A498 (line)]] | wt | 6.89 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.72× (z +13.5) | — |
| [[NCI-H2030 (line)]] | alt | 12.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.172× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change |
| [[NCI-H23 (line)]] | alt | 7.58 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.109× (z -12.2) ⚠ cell-cycle shift, explains ~47% of this change |
| [[NCI-H2347 (line)]] | alt | 4.22 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 6.22× (z +9.3) | — |
| [[SK-MEL-2 (line)]] | alt | 10.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.112× (z -12.6) |
| [[SNU-423 (line)]] | alt | 10.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.86× (z +8.6) | — |
| [[SW480 (line)]] | alt | 13.5 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.272× (z -8.8) |
| [[A-427 (line)]] | wt | 1.03 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.958 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.710 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.18 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.26 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.43 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.651 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.10 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.599 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.673 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.32 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.510 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.578 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.28 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.63 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.581 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.533 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 6.28 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.798 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 6.19 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.590 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.844 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.612 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.683 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.72 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.47 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.83 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.46 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.694 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9915), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRNP1]] | +0.59 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[RHOBTB2]] | +0.58 | +0.46 / +0.47 | both halves | 3e-05 |  |
| [[CAMK4]] | +0.55 | +0.44 / +0.52 | both halves | 3e-05 |  |
| [[PPP1R14C]] | +0.55 | +0.43 / +0.53 | both halves | 3e-05 |  |
| [[HIVEP3]] | +0.54 | +0.44 / +0.42 | both halves | 4e-05 |  |
| [[ERGIC1]] | +0.52 | +0.45 / +0.36 | both halves | 1e-04 |  |
| [[TGFBR2]] | +0.51 | +0.44 / +0.47 | both halves | 3e-05 |  |
| [[BIRC3]] | +0.51 | +0.40 / +0.46 | both halves | 5e-05 |  |
| [[ANKRD20A7P]] | +0.50 | +0.40 / +0.40 | both halves | 5e-05 |  |
| [[UBE2E2]] | +0.50 | +0.43 / +0.45 | both halves | 3e-05 |  |
| [[ZHX3]] | +0.50 | +0.44 / +0.39 | both halves | 5e-05 |  |
| [[MT2A]] | +0.50 | +0.44 / +0.38 | both halves | 7e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NCOA2]] | -0.53 | -0.42 / -0.39 | both halves | 6e-05 |  |
| [[PCMTD1]] | -0.52 | -0.43 / -0.43 | both halves | 4e-05 |  |
| [[PXDNL]] | -0.49 | -0.37 / -0.37 | both halves | 9e-05 |  |
| [[ZNF213-AS1]] | -0.48 | -0.31 / -0.37 | both halves | 2e-04 |  |
| [[CSDE1]] | -0.47 | -0.36 / -0.41 | both halves | 1e-04 |  |
| [[SOS1]] | -0.47 | -0.39 / -0.35 | both halves | 1e-04 | pathway: G alpha (12/13) signalling events |
| [[CDIPT]] | -0.46 | -0.38 / -0.41 | both halves | 6e-05 |  |
| [[VPS39]] | -0.46 | -0.38 / -0.38 | both halves | 7e-05 |  |
| [[PRR13]] | -0.46 | -0.44 / -0.38 | both halves | 7e-05 |  |
| [[UROD]] | -0.46 | -0.25 / -0.38 | both halves | 4e-04 |  |
| [[NXF1]] | -0.46 | -0.41 / -0.25 | both halves | 4e-04 |  |
| [[PTPN23-DT]] | -0.46 | -0.32 / -0.38 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KCNMB4]] | B | KCNMB4 activity lowers ADRA1B's level | lines that do not express KCNMB4 (5) vs lines expressing it (45) | 1.82× higher at baseline in the lines without KCNMB4 | 0.029 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[TGFBR2]] | B | TGFBR2 activity raises ADRA1B's level | lines that do not express TGFBR2 (7) vs lines expressing it (43) | 2.41× lower at baseline in the lines without TGFBR2 | 0.050 | ⚠ within organs, on part of the lines; also absent: VDR, TRIB1, MET |
| [[NR3C1]] | B | NR3C1 activity raises ADRA1B's level | compounds that target NR3C1: 3 of 3 raise it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 5.9% of all compounds | 0.079 | ⚠ off-target possible; 3 compounds |
| [[TRNP1]] | B | TRNP1 activity raises ADRA1B's level | lines that do not express TRNP1 (10) vs lines expressing it (40) | 2.09× lower at baseline in the lines without TRNP1 | 0.088 | ⚠ within organs, on part of the lines; also absent: USP43, STEAP2 |
| [[UBE2E2]] | B | UBE2E2 activity raises ADRA1B's level | lines that do not express UBE2E2 (11) vs lines expressing it (39) | 2.45× lower at baseline in the lines without UBE2E2 | 0.099 | ⚠ within organs, on part of the lines; also absent: PRDM5, AMOTL1, RAB31 |
| [[DPY19L2P1]] | C | DPY19L2P1 activity raises ADRA1B's level | lines that do not express DPY19L2P1 (26) vs lines expressing it (24) | 2.13× lower at baseline in the lines without DPY19L2P1 | 0.070 | ⚠ within organs, on part of the lines; also absent: STAC, RNF180, SRGN; co-absent with the target |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 6, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Cobimetinib (drug)]] 5 µM | B | ADRA1B activity lowers the cells' numbers under Cobimetinib 5 µM (makes them more sensitive) | lines that do not express ADRA1B (24) vs lines expressing it (24) | the lines without ADRA1B: 1.16× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: IL31RA, IGFBP3, STAC |
| [[TGFBR2]] | B | ADRA1B activity raises TGFBR2's level | lines that do not express ADRA1B (24) vs lines expressing it (26) | 1.88× lower at baseline in the lines without ADRA1B | 0.038 | ⚠ within organs, on part of the lines; also absent: IL31RA, IGFBP3, STAC |
| [[NEK11]] | B | ADRA1B activity raises NEK11's level | lines that do not express ADRA1B (24) vs lines expressing it (26) | 1.49× lower at baseline in the lines without ADRA1B | 0.063 | ⚠ within organs, on part of the lines; also absent: IL31RA, IGFBP3, STAC |
| [[UBE2E2]] | B | ADRA1B activity raises UBE2E2's level | lines that do not express ADRA1B (24) vs lines expressing it (26) | 2.49× lower at baseline in the lines without ADRA1B | 0.080 | ⚠ within organs, on part of the lines; also absent: IL31RA, IGFBP3, STAC |
| [[YPEL5]] | B | ADRA1B activity raises YPEL5's level | lines that do not express ADRA1B (24) vs lines expressing it (26) | 1.42× lower at baseline in the lines without ADRA1B | 0.099 | ⚠ within organs, on part of the lines; also absent: IL31RA, IGFBP3, STAC |
| [[DPF1]] | B | ADRA1B activity lowers DPF1's level | lines that do not express ADRA1B (24) vs lines expressing it (26) | 1.21× higher at baseline in the lines without ADRA1B | 0.099 | ⚠ within organs, on part of the lines; also absent: IL31RA, IGFBP3, STAC |
| [[NCOA2]] | C | ADRA1B activity weakens NCOA2's drug response | lines that do not express ADRA1B (24) vs lines expressing it (25) | the lines without ADRA1B respond 0.97× as strongly (z diff -0.46); strongest at Panobinostat 0.5 µM: 0.20x vs 0.20x (z diff -1.1) | 0.090 | ⚠ within organs, on part of the lines; also absent: IL31RA, IGFBP3, STAC; target measured in part of the lines; rests on the correction; artifact flags |

## Where it sits

- **Module**: [[Module 097]] — estrogen response early; 48 genes; every member is in the + arm (projection on the module's main direction 0.552). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (30.0, 12.2); signed map (14.0, 33.4). **Vector** length 61.4, 15.2% of its response variance represented; |z| ≥ 3 in 596 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.0 | +13.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.7 | +7.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.7 | +10.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.2 | +7.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +2.9 | +6.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.1 | +5.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.6 | +0.5 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +1.4 | +5.5 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.2 | +0.5 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | -2.7 | -3.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -2.6 | -2.1 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -1.4 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.8 | -3.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -1.8 | -3.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.7 | +0.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.4 | -3.1 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.4 | -0.9 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -1.4 | -2.0 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.3 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | adrenoceptor alpha 1B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q33.3 — chr5:159,865,080-159,973,012 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Adrenoceptors |
| Hallmark sets | APICAL_JUNCTION |
| Reactome | 8 pathways, smallest: Adrenoceptors; Amine ligand-binding receptors; G alpha (12/13) signalling events |
| Matched by | ensembl_id |

**Function**, from UniProt [P35368](https://www.uniprot.org/uniprotkb/P35368) (Alpha-1B adrenergic receptor):

> Alpha-1 adrenergic receptors are G protein-coupled receptors for catecholamines that signal through the G(q) family of G proteins, including G(q) and G(11). Upon activation, they stimulate the phosphatidylinositol-calcium second messenger pathway, leading to calcium release from intracellular stores and activation of protein kinase C (By similarity). ADRA1B binds the catecholamine ligands norepinephrine and epinephrine. Can also couple to G(14) and G(16) proteins (By similarity). Nuclear ADRA1B …

**Summary**, from NCBI Gene [147](https://www.ncbi.nlm.nih.gov/gene/147):

> Alpha-1-adrenergic receptors (alpha-1-ARs) are members of the G protein-coupled receptor superfamily. They activate mitogenic responses and regulate growth and proliferation of many cells. There are 3 alpha-1-AR subtypes: alpha-1A, -1B and -1D, all of which signal through the Gq/11 family of G-proteins and different subtypes show different patterns of activation. This gene encodes alpha-1B-adrenergic receptor, which induces neoplastic transformation when transfected into NIH 3T3 fibroblasts and …

**Accessions** — [HGNC:278](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:278) · Entrez [147](https://www.ncbi.nlm.nih.gov/gene/147) · UniProt [P35368](https://www.uniprot.org/uniprotkb/P35368) · Ensembl [ENSG00000170214](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170214)

## Data

Gene col 9915: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9915); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9915, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9915]; `tensor/DDL_lfc|DDL_z.npy` [9915]; `embed/gene_vectors.npy` [9915]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9915 or target_col == 9915). Every well: [[ADRA1B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADRA1B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
