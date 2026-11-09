---
symbol: "MYO5C"
type: "gene"
col: 4924
ensembl_id: "ENSG00000128833"
name: "myosin VC"
location: "15q21.2"
module: 8
arm: "+"
pooled_cpm: 55.35
n_lines_expressing: 30
n_dd_up: 4
n_dd_down: 26
n_dd_up_clean: 1
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 9
direction_downstream: 11
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# MYO5C

*myosin VC* — 15q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.77× (z +13.9, q 6e-41, up in 18 of 28 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Clobetasol propionate (drug)]] 0.05 µM: 1.21× (z +4.7, q 4e-04, up in 6 of 28 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (A-427 3.16×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.403× (z -22.1, q 0e+00, down in 27 of 28 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SYK]] (+0.58, fdr 1e-05), [[ANXA3]] (+0.56, fdr 1e-05), [[DENND2D]] (+0.55, fdr 3e-05); moves opposite to [[LINC01615]] (-0.63, fdr 1e-05), [[ARMCX2]] (-0.58, fdr 2e-05), [[FBXL12]] (-0.58, fdr 1e-05).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[ANK3]] → it (grade B ⚠); 11 go from it, the strongest it → [[THBS2-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 4 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4924.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (A-427 3.16×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.77×** | +13.9 | 6e-41 | 18/28 (A-427, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.62×** | +11.2 | 1e-26 | 17/24 (NCI-H2347, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.26×** | +5.2 | 5e-05 | 9/25 (NCI-H2347, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.21×** | +4.7 | 4e-04 | 6/28 (SNU-1, SW 900, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~46% of this change | 1.17× | +3.5 | 0.047 | 3/28 (LoVo, COLO 205, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4924.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.403×** | -22.1 | 0e+00 | 27/28 (SW480, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.528×** | -21.9 | 0e+00 | 25/29 (NCI-H1573, KATO III, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.409×** | -21.7 | 0e+00 | 27/28 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.448×** | -19.5 | 0e+00 | 26/28 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.475×** | -18.0 | 0e+00 | 27/28 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.620×** | -16.4 | 0e+00 | 24/28 (NCI-H1573, SNU-1, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.512×** | -16.3 | 0e+00 | 26/28 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.624×** | -11.4 | 2e-28 | 23/28 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.650×** | -10.5 | 8e-24 | 21/28 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.452×** | -10.1 | 4e-22 | 24/29 (LoVo, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.466×** | -9.7 | 2e-20 | 24/27 (LS 180, COLO 205, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.684×** | -9.2 | 1e-18 | 22/28 (SNU-1, A-427, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.707×** | -8.1 | 2e-14 | 19/28 (NCI-H1573, SNU-1, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.722×** | -7.9 | 1e-13 | 18/28 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.723×** | -7.9 | 1e-13 | 21/28 (LoVo, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.806×** | -7.4 | 5e-12 | 16/28 (SNU-1, SW480, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.811×** | -7.2 | 2e-11 | 18/28 (BT-474, CFPAC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4924. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-1 (line)]] | wt | 430 | 0 | 20 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.134× (z -24.1) |
| [[LoVo (line)]] | wt | 132 | 0 | 12 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.393× (z -19.4) |
| [[SW480 (line)]] | alt | 85.4 | 0 | 11 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.190× (z -23.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.203× (z -22.7) |
| [[NCI-H1573 (line)]] | alt | 153 | 0 | 10 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.176× (z -26.8) |
| [[PANC-1 (line)]] | alt | 43.1 | 0 | 10 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.293× (z -19.8) |
| [[COLO 205 (line)]] | alt | 122 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -16.7) |
| [[HEC-1-A (line)]] | alt | 101 | 0 | 7 | — | [[Panobinostat (drug)]] 0.5 µM 0.302× (z -16.2) |
| [[HT-29 (line)]] | alt | 104 | 0 | 7 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.327× (z -18.9) |
| [[LS 180 (line)]] | wt | 115 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.324× (z -14.3) |
| [[Panc 03.27 (line)]] | alt | 91.5 | 0 | 6 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.370× (z -15.3) |
| [[SW1417 (line)]] | alt | 76.8 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.189× (z -17.9) |
| [[SW48 (line)]] | wt | 114 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.229× (z -13.0) |
| [[BT-474 (line)]] | alt | 101 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.277× (z -13.4) |
| [[KATO III (line)]] | alt | 132 | 0 | 5 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.312× (z -20.8) |
| [[NCI-H2030 (line)]] | alt | 72.8 | 0 | 5 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.344× (z -9.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.356× (z -9.1) |
| [[SHP-77 (line)]] | alt | 46.0 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.163× (z -13.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.181× (z -12.8) |
| [[SW 900 (line)]] | alt | 35.7 | 0 | 5 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.145× (z -14.5) |
| [[A-427 (line)]] | wt | 30.4 | 1 (1 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.16× (z +9.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.147× (z -15.9) |
| [[CFPAC-1 (line)]] | alt | 65.3 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.381× (z -15.2) |
| [[HCT15 (line)]] | alt | 99.9 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.307× (z -10.9) |
| [[Hs 766T (line)]] | wt | 36.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -11.3) |
| [[A549 (line)]] | wt | 33.5 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.247× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.454× (z -8.9) |
| [[NCI-H2347 (line)]] | alt | 74.6 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.415× (z -10.6) |
| [[NCI-H1792 (line)]] | alt | 21.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.331× (z -9.7) |
| [[RKO (line)]] | wt | 17.1 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.114× (z -10.8) ⚠ cell-cycle shift, explains ~29% of this change |
| [[A-172 (line)]] | wt | 6.52 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 4.36 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 11.5 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 6.77 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 7.75 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 10.7 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 7.67 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 9.77 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 42.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.93 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 9.81 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.09 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 8.03 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 9.14 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.06 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.34 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 47.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 54.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 11.2 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.49 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 12.3 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 11.6 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 11.5 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4924), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*39 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SYK]] | +0.58 | +0.62 / +0.51 | both halves | 1e-05 |  |
| [[ANXA3]] | +0.56 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[DENND2D]] | +0.55 | +0.60 / +0.44 | both halves | 3e-05 |  |
| [[ICA1]] | +0.53 | +0.60 / +0.38 | both halves | 7e-05 |  |
| [[IPO8]] | +0.52 | +0.43 / +0.52 | both halves | 3e-05 |  |
| [[DMTN]] | +0.51 | +0.51 / +0.46 | both halves | 2e-05 |  |
| [[PROM1]] | +0.50 | +0.45 / +0.40 | both halves | 4e-05 |  |
| [[INPP4B]] | +0.50 | +0.60 / +0.37 | both halves | 8e-05 |  |
| [[ANK3]] | +0.49 | +0.53 / +0.41 | both halves | 4e-05 |  |
| [[NUP210]] | +0.49 | +0.44 / +0.46 | both halves | 3e-05 |  |
| [[LRP5]] | +0.48 | +0.54 / +0.32 | both halves | 2e-04 |  |
| [[RPH3AL]] | +0.48 | +0.52 / +0.30 | both halves | 2e-04 |  |

## Genes that move opposite

*61 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01615]] | -0.63 | -0.66 / -0.52 | both halves | 1e-05 |  |
| [[ARMCX2]] | -0.58 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[FBXL12]] | -0.58 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[ZNF8-DT]] | -0.57 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[TSHZ3-AS1]] | -0.54 | -0.61 / -0.28 | both halves | 3e-04 |  |
| [[WIPF2]] | -0.53 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[TSHZ3]] | -0.53 | -0.45 / -0.34 | both halves | 1e-04 |  |
| [[PLIN3]] | -0.51 | -0.40 / -0.45 | both halves | 4e-05 |  |
| [[FAM228B]] | -0.51 | -0.63 / -0.38 | both halves | 7e-05 |  |
| [[HCFC1R1]] | -0.51 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[ZNF521]] | -0.50 | -0.49 / -0.34 | both halves | 1e-04 |  |
| [[SOX12]] | -0.49 | -0.50 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 3, C 6.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANK3]] | B | ANK3 activity raises MYO5C's level | lines that do not express ANK3 (23) vs lines expressing it (27) | 2.95× lower at baseline in the lines without ANK3 | 0.008 | ⚠ within organs, on part of the lines; also absent: ATP2C2, MACC1, GALNT3 |
| [[MEIS3]] | B | MEIS3 activity lowers MYO5C's level | lines that do not express MEIS3 (12) vs lines expressing it (38) | 4.11× higher at baseline in the lines without MEIS3 | 0.029 | ⚠ within organs, on part of the lines; also absent: PARVG, HECW2, RFLNB |
| [[SLC44A3]] | B | SLC44A3 activity raises MYO5C's level | lines that do not express SLC44A3 (13) vs lines expressing it (37) | 2.44× lower at baseline in the lines without SLC44A3 | 0.060 | ⚠ within organs, on part of the lines; also absent: SLC44A3-AS1, ENSG00000287306, SH2D3A; maybe low, not absent |
| [[MAL2]] | C | MAL2 activity raises MYO5C's level | lines that do not express MAL2 (31) vs lines expressing it (19) | 5.13× lower at baseline in the lines without MAL2 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: RAB25, TMEM125, CDH1; co-absent with the target |
| [[TMEM30B]] | C | TMEM30B activity raises MYO5C's level | lines that do not express TMEM30B (35) vs lines expressing it (15) | 5.37× lower at baseline in the lines without TMEM30B | 0.002 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, ANKRD22, RAB25; co-absent with the target |
| [[ANXA3]] | C | ANXA3 activity raises MYO5C's level | lines that do not express ANXA3 (24) vs lines expressing it (26) | 4.16× lower at baseline in the lines without ANXA3 | 0.004 | ⚠ within organs, on part of the lines; also absent: RNF223, P2RY2, C6orf132; co-absent with the target |
| [[FRAS1]] | C | FRAS1 activity raises MYO5C's level | lines that do not express FRAS1 (22) vs lines expressing it (28) | 3.19× lower at baseline in the lines without FRAS1 | 0.016 | ⚠ within organs, on part of the lines; also absent: ANO9, ELF3, FAAH2; co-absent with the target |
| [[ESRP2]] | C | ESRP2 activity raises MYO5C's level | lines that do not express ESRP2 (26) vs lines expressing it (24) | 4.26× lower at baseline in the lines without ESRP2 | 0.068 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: PRSS22, MARVELD3, CRB3; co-absent with the target |
| [[SORL1]] | C | SORL1 activity raises MYO5C's level | lines that do not express SORL1 (21) vs lines expressing it (29) | 3.29× lower at baseline in the lines without SORL1 | 0.076 | ⚠ within organs, on part of the lines; also absent: PRR15-DT, PLEKHG6, SLC52A3; co-absent with the target |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 6, C 5.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[THBS2-AS1]] | B | MYO5C activity lowers THBS2-AS1's level | lines that do not express MYO5C (20) vs lines expressing it (30) | 1.77× higher at baseline in the lines without MYO5C | 0.011 | ⚠ within organs, on part of the lines; also absent: ENSG00000288656, EVPL, NCMAP; maybe low, not absent |
| [[ANK3]] | B | MYO5C activity raises ANK3's level | lines that do not express MYO5C (20) vs lines expressing it (30) | 3.44× lower at baseline in the lines without MYO5C | 0.061 | ⚠ within organs, on part of the lines; also absent: ENSG00000288656, EVPL, NCMAP; maybe low, not absent |
| [[TSHZ3-AS1]] | B | MYO5C activity lowers TSHZ3-AS1's level | lines that do not express MYO5C (20) vs lines expressing it (30) | 2.92× higher at baseline in the lines without MYO5C | 0.068 | ⚠ within organs, on part of the lines; also absent: ENSG00000288656, EVPL, NCMAP; maybe low, not absent |
| [[LINC01615]] | B | MYO5C activity lowers LINC01615's level | lines that do not express MYO5C (20) vs lines expressing it (30) | 2.90× higher at baseline in the lines without MYO5C | 0.069 | ⚠ within organs, on part of the lines; also absent: ENSG00000288656, EVPL, NCMAP; maybe low, not absent |
| [[FBXL12]] | B | MYO5C activity lowers FBXL12's level | lines that do not express MYO5C (20) vs lines expressing it (30) | 1.30× higher at baseline in the lines without MYO5C | 0.075 | ⚠ within organs, on part of the lines; also absent: ENSG00000288656, EVPL, NCMAP; maybe low, not absent |
| [[PKD1L1-AS1]] | B | MYO5C activity lowers PKD1L1-AS1's level | lines that do not express MYO5C (20) vs lines expressing it (30) | 3.34× higher at baseline in the lines without MYO5C | 0.094 | ⚠ within organs, on part of the lines; also absent: ENSG00000288656, EVPL, NCMAP; maybe low, not absent |
| [[FRAS1]] | C | MYO5C activity raises FRAS1's level | lines that do not express MYO5C (20) vs lines expressing it (30) | 4.53× lower at baseline in the lines without MYO5C | 0.033 | ⚠ within organs, on part of the lines; also absent: ENSG00000288656, EVPL, NCMAP; maybe low, not absent; co-absent with the target |
| [[ESRP2]] | C | MYO5C activity raises ESRP2's level | lines that do not express MYO5C (20) vs lines expressing it (30) | 3.80× lower at baseline in the lines without MYO5C | 0.059 | ⚠ within organs, on part of the lines; also absent: ENSG00000288656, EVPL, NCMAP; maybe low, not absent; co-absent with the target |
| [[ANXA3]] | C | MYO5C activity raises ANXA3's level | lines that do not express MYO5C (20) vs lines expressing it (30) | 5.05× lower at baseline in the lines without MYO5C | 0.084 | ⚠ within organs, on part of the lines; also absent: ENSG00000288656, EVPL, NCMAP; maybe low, not absent; co-absent with the target |
| [[MAL2]] | C | MYO5C activity raises MAL2's level | lines that do not express MYO5C (20) vs lines expressing it (30) | 4.87× lower at baseline in the lines without MYO5C | 0.090 | ⚠ within organs, on part of the lines; also absent: ENSG00000288656, EVPL, NCMAP; maybe low, not absent; co-absent with the target |
| [[SORL1]] | C | MYO5C activity raises SORL1's level | lines that do not express MYO5C (20) vs lines expressing it (30) | 4.45× lower at baseline in the lines without MYO5C | 0.093 | ⚠ within organs, on part of the lines; also absent: ENSG00000288656, EVPL, NCMAP; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.379). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.9, 45.4); signed map (55.7, 5.2). **Vector** length 85.6, 22.9% of its response variance represented; |z| ≥ 3 in 846 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.2 | +13.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.8 | +11.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.6 | +5.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.7 | -16.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.5 | -4.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.6 | -0.7 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +1.5 | +0.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.3 | -0.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | +1.2 | +0.6 |
| fall | [[PH-797804 (drug)]] 5 µM |  | -1.9 | -9.7 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -1.7 | -7.9 |
|  | [[Selinexor (drug)]] 5 µM |  | -1.7 | -7.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -1.5 | -21.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -1.5 | -21.7 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -1.5 | -1.4 |
|  | [[Belzutifan (drug)]] 5 µM |  | -1.3 | -1.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.0 | +0.5 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -0.9 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | myosin VC |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q21.2 — chr15:52,192,322-52,295,804 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC74969 |
| Gene groups (HGNC) | Myosin heavy chains, class V; MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NQX4](https://www.uniprot.org/uniprotkb/Q9NQX4) (Unconventional myosin-Vc):

> May be involved in transferrin trafficking. Likely to power actin-based membrane trafficking in many physiologically crucial tissues.

**Summary**, from NCBI Gene [55930](https://www.ncbi.nlm.nih.gov/gene/55930):

> Predicted to enable actin filament binding activity and microfilament motor activity. Predicted to be involved in actin filament organization and endocytosis. Located in cytosol and nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:7604](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7604) · Entrez [55930](https://www.ncbi.nlm.nih.gov/gene/55930) · UniProt [Q9NQX4](https://www.uniprot.org/uniprotkb/Q9NQX4) · Ensembl [ENSG00000128833](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000128833)

## Data

Gene col 4924: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4924); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4924, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4924]; `tensor/DDL_lfc|DDL_z.npy` [4924]; `embed/gene_vectors.npy` [4924]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4924 or target_col == 4924). Every well: [[MYO5C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MYO5C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
