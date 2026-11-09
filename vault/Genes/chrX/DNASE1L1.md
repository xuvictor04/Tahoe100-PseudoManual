---
symbol: "DNASE1L1"
type: "gene"
col: 277
ensembl_id: "ENSG00000013563"
name: "deoxyribonuclease 1 like 1"
location: "Xq28"
module: 192
arm: "+"
pooled_cpm: 23.8
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 17
n_dd_up_clean: 1
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/192"]
generated_by: "tahoemap"
---

# DNASE1L1

*deoxyribonuclease 1 like 1* — Xq28

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.95× (z +7.4, q 9e-11, up in 29 of 37 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.51× (z +4.6, q 9e-04, up in 22 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (LS 180 4.82×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.341× (z -16.7, q 0e+00, down in 45 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RRAS]] (+0.78, fdr 7e-06), [[IGSF8]] (+0.71, fdr 7e-06), [[PCMT1]] (+0.68, fdr 3e-05); moves opposite to [[FUBP1]] (-0.67, fdr 1e-05), [[BCLAF1]] (-0.63, fdr 1e-05), [[DCLRE1A]] (-0.63, fdr 1e-05).
> It is in [[Module 192]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → cells under [[ERK5-IN-2 (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 3 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 277.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (LS 180 4.82×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.95×** | +7.4 | 9e-11 | 29/37 (LS 180, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.76×** | +6.0 | 4e-07 | 24/30 (C32, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.51×** | +4.6 | 9e-04 | 22/47 (KATO III, LS 180, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.44×** | +3.8 | 0.024 | 18/36 (A-427, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, none with an alert; shown: the 15 strongest. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 277.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.341×** | -16.7 | 0e+00 | 45/46 (NCI-H460, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.407×** | -9.9 | 1e-20 | 40/46 (HS-578T, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.560×** | -6.1 | 2e-07 | 30/47 (A549, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.379×** | -5.6 | 3e-06 | 35/47 (MIA PaCa-2, A498, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.585×** | -5.5 | 3e-06 | 33/47 (RKO, C-33 A, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.624×** | -5.2 | 2e-05 | 29/48 (HOP62, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.422×** | -5.0 | 6e-05 | 28/45 (HEC-1-A, A498, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.677×** | -4.3 | 0.001 | 26/47 (HOP62, RKO, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.687×** | -4.1 | 0.002 | 22/47 (HS-578T, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.698×** | -3.9 | 0.005 | 25/48 (A498, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.722×** | -3.6 | 0.020 | 19/47 (MIA PaCa-2, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.714×** | -3.5 | 0.025 | 21/46 (RPMI-7951, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~20% here) |
| [[ERK5-IN-2 (drug)]] 5 µM |  | **0.552×** | -3.4 | 0.028 | 16/48 (HEC-1-A, RKO, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.734×** | -3.4 | 0.030 | 19/48 (NCI-H460, SW480, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.736×** | -3.3 | 0.031 | 13/47 (HOP62, A549, …) | rises with dose | cell-cycle shift (explains ~15% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 277. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 23.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -16.3) |
| [[A498 (line)]] | wt | 40.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.392× (z -10.8) |
| [[CFPAC-1 (line)]] | alt | 23.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -12.4) |
| [[HEC-1-A (line)]] | alt | 31.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -12.6) |
| [[HOP62 (line)]] | alt | 24.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.192× (z -16.1) |
| [[HS-578T (line)]] | alt | 27.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0972× (z -15.2) |
| [[MIA PaCa-2 (line)]] | alt | 26.3 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.205× (z -14.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.362× (z -9.4) |
| [[NCI-H1573 (line)]] | alt | 21.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.271× (z -10.7) |
| [[NCI-H460 (line)]] | wt | 25.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.197× (z -17.1) |
| [[RKO (line)]] | wt | 21.8 | 0 | 2 | — | [[TAK-901 (drug)]] 0.05 µM 0.108× (z -10.6) |
| [[A-172 (line)]] | wt | 42.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.430× (z -9.2) |
| [[A-427 (line)]] | wt | 34.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -10.9) |
| [[AsPC-1 (line)]] | alt | 44.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.180× (z -15.7) |
| [[BT-474 (line)]] | alt | 9.22 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.143× (z -11.3) |
| [[COLO 205 (line)]] | alt | 15.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -10.5) |
| [[H4 (line)]] | wt | 16.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -11.1) |
| [[HT-29 (line)]] | alt | 41.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.416× (z -9.2) |
| [[LS 180 (line)]] | wt | 16.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.82× (z +9.2) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 35.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -13.6) |
| [[NCI-H2347 (line)]] | alt | 13.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -12.8) |
| [[Panc 03.27 (line)]] | alt | 12.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -10.3) |
| [[PANC-1 (line)]] | alt | 38.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -11.7) |
| [[RPMI-7951 (line)]] | alt | 11.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.117× (z -8.5) |
| [[SK-MEL-2 (line)]] | alt | 30.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.332× (z -10.1) |
| [[SW 900 (line)]] | alt | 17.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -10.3) |
| [[AN3 CA (line)]] | alt | 6.95 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.36 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.42 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.84 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 60.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 27.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.23 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.83 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 11.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 277), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RRAS]] | +0.78 | +0.76 / +0.71 | both halves | 7e-06 |  |
| [[IGSF8]] | +0.71 | +0.69 / +0.58 | both halves | 7e-06 |  |
| [[PCMT1]] | +0.68 | +0.70 / +0.43 | both halves | 3e-05 |  |
| [[MYO9B]] | +0.68 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[YIF1B]] | +0.67 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[FAM89B]] | +0.65 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[SH3GL1]] | +0.65 | +0.65 / +0.50 | both halves | 1e-05 |  |
| [[PLD3]] | +0.65 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[RTN2]] | +0.65 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[TRPT1]] | +0.65 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[ARID3B]] | +0.65 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[B3GAT3]] | +0.64 | +0.57 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FUBP1]] | -0.67 | -0.52 / -0.61 | both halves | 1e-05 |  |
| [[BCLAF1]] | -0.63 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[DCLRE1A]] | -0.63 | -0.62 / -0.57 | both halves | 1e-05 |  |
| [[ZXDA]] | -0.62 | -0.58 / -0.43 | both halves | 3e-05 |  |
| [[ZXDB]] | -0.62 | -0.60 / -0.44 | both halves | 3e-05 |  |
| [[MCCC2]] | -0.61 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[HNRNPK]] | -0.60 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[ZNF507]] | -0.60 | -0.56 / -0.45 | both halves | 3e-05 |  |
| [[EWSR1]] | -0.60 | -0.51 / -0.57 | both halves | 1e-05 |  |
| [[POGLUT1]] | -0.60 | -0.58 / -0.41 | both halves | 4e-05 |  |
| [[HNRNPL]] | -0.60 | -0.43 / -0.56 | both halves | 3e-05 |  |
| [[UTP20]] | -0.58 | -0.53 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[ERK5-IN-2 (drug)]] 0.5 µM | C | DNASE1L1's natural level lowers the cells' numbers under ERK5-IN-2 0.5 µM (makes them more sensitive) | DNASE1L1's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.68 | 0.287 over the table, 0.034 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 192]]; 17 genes; every member is in the + arm (projection on the module's main direction 0.766). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.50; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (4.4, 0.3); signed map (-31.6, 15.0). **Vector** length 75.9, 17.3% of its response variance represented; |z| ≥ 3 in 737 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.5 | +2.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.4 | +1.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.0 | +4.6 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.9 | +2.8 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.8 | +1.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.2 | +0.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.0 | +1.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | +1.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.5 | +0.6 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.8 | -9.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.2 | -16.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.3 | -4.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.1 | -6.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.5 | -5.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.3 | -3.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.2 | -0.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.9 | -0.7 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -1.9 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | deoxyribonuclease 1 like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq28 — chrX:154,401,236-154,412,112 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DNAS1L1, XIB, DNASEX; previously DNL1L |
| Reactome | 2 pathways, smallest: Neutrophil degranulation; Innate Immune System |
| Matched by | ensembl_id |

UniProt [P49184](https://www.uniprot.org/uniprotkb/P49184) carries no function annotation.

**Summary**, from NCBI Gene [1774](https://www.ncbi.nlm.nih.gov/gene/1774):

> This gene encodes a deoxyribonuclease protein that shows high sequence similarity to DNase I. The encoded protein is localized to the endoplasmic reticulum and modified by N-linked glycosylation. Alternate transcriptional splice variants encoding the same protein have been observed. [provided by RefSeq, Jan 2015]

**Accessions** — [HGNC:2957](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2957) · Entrez [1774](https://www.ncbi.nlm.nih.gov/gene/1774) · UniProt [P49184](https://www.uniprot.org/uniprotkb/P49184) · Ensembl [ENSG00000013563](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000013563)

## Data

Gene col 277: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 277); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 277, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 277]; `tensor/DDL_lfc|DDL_z.npy` [277]; `embed/gene_vectors.npy` [277]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 277 or target_col == 277). Every well: [[DNASE1L1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DNASE1L1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
