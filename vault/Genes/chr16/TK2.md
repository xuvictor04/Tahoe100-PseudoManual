---
symbol: "TK2"
type: "gene"
col: 9329
ensembl_id: "ENSG00000166548"
name: "thymidine kinase 2"
location: "16q21"
module: 95
arm: "+"
pooled_cpm: 22.96
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 33
n_dd_up_clean: 3
n_dd_down_clean: 24
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/095"]
generated_by: "tahoemap"
---

# TK2

*thymidine kinase 2* — 16q21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[Clobetasol propionate (drug)]] 0.05 µM: 1.32× (z +3.9, q 0.051, up in 17 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 33 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.277× (z -17.7, q 0e+00, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC00623]] (+0.59, fdr 1e-05), [[SOCS6]] (+0.54, fdr 4e-05), [[DCPS]] (+0.54, fdr 6e-05); moves opposite to [[PRDX1]] (-0.54, fdr 7e-05), [[NUCB1]] (-0.49, fdr 3e-05), [[ERP44]] (-0.48, fdr 8e-05).
> It sits in the **+** arm of [[Module 095]] (Chromatin organization).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[IRX3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9329.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.32×** | +3.9 | 0.051 | 17/47 (HOP62, CFPAC-1, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.44×** | +3.6 | 0.087 | 23/47 (HEC-1-A, A-172, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.28×** | +3.5 | 0.094 | 15/48 (HOP62, CFPAC-1, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.25× | +3.1 | 0.22 | 12/48 (LOX-IMVI, LS 180, …) | rises with dose |  |
| [[Celecoxib (drug)]] 0.5 µM |  | 1.37× | +3.1 | 0.22 | 7/47 (Hs 766T, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | 1.36× | +3.0 | 0.22 | 13/43 (RPMI-7951, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 9 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 33 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9329.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.277×** | -17.7 | 0e+00 | 46/48 (SW480, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.297×** | -16.7 | 0e+00 | 45/47 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.315×** | -15.9 | 0e+00 | 48/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.319×** | -15.7 | 0e+00 | 46/48 (SW480, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.398×** | -12.7 | 9e-35 | 45/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.425×** | -11.8 | 4e-30 | 44/47 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.436×** | -11.4 | 3e-28 | 40/47 (SW480, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.466×** | -10.5 | 5e-24 | 40/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.476×** | -10.2 | 9e-23 | 39/48 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.483×** | -10.0 | 7e-22 | 39/47 (MIA PaCa-2, SW480, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.603×** | -9.8 | 4e-21 | 33/47 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.499×** | -9.6 | 5e-20 | 42/48 (SW480, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.277×** | -9.2 | 1e-18 | 42/48 (NCI-H2030, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.520×** | -8.5 | 7e-16 | 32/47 (NCI-H460, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.371×** | -7.1 | 4e-11 | 37/45 (LS 180, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **0.597×** | -6.8 | 3e-10 | 28/47 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9329. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 33.9 | 0 | 19 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0629× (z -27.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0937× (z -23.5) |
| [[NCI-H460 (line)]] | wt | 22.0 | 0 | 16 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -15.8) |
| [[PANC-1 (line)]] | alt | 17.9 | 0 | 9 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.148× (z -16.1) |
| [[LoVo (line)]] | wt | 21.4 | 0 | 6 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.190× (z -13.8) |
| [[MIA PaCa-2 (line)]] | alt | 47.2 | 0 | 6 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.204× (z -12.5) |
| [[NCI-H2030 (line)]] | alt | 83.2 | 0 | 6 | — | [[Panobinostat (drug)]] 5 µM 0.255× (z -13.3) |
| [[A549 (line)]] | wt | 20.1 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.297× (z -11.8) |
| [[A-427 (line)]] | wt | 28.0 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.162× (z -14.2) |
| [[HEC-1-A (line)]] | alt | 43.5 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.337× (z -10.0) |
| [[LS 180 (line)]] | wt | 18.3 | 0 | 4 (1 ⚠) | — | [[PH-797804 (drug)]] 5 µM 0.0225× (z -13.8) |
| [[NCI-H23 (line)]] | alt | 19.6 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.165× (z -11.7) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.215× (z -10.0) |
| [[SW1417 (line)]] | alt | 18.8 | 0 | 4 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.211× (z -10.1) |
| [[HS-578T (line)]] | alt | 19.4 | 0 | 3 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.194× (z -9.9) |
| [[KATO III (line)]] | alt | 20.1 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.136× (z -13.5) |
| [[NCI-H1573 (line)]] | alt | 14.5 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -12.9) |
| [[NCI-H1792 (line)]] | alt | 41.9 | 0 | 3 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.287× (z -9.3) |
| [[SW 900 (line)]] | alt | 24.8 | 0 | 3 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.158× (z -10.3) |
| [[C-33 A (line)]] | alt | 25.0 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.195× (z -9.2) |
| [[COLO 205 (line)]] | alt | 17.1 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.0734× (z -12.2) |
| [[Hs 766T (line)]] | wt | 40.7 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.217× (z -16.3) ⚠ cell-cycle shift, explains ~24% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.293× (z -9.2) |
| [[HT-29 (line)]] | alt | 9.57 | 0 | 2 | — | [[Belinostat (drug)]] 0.5 µM 0.117× (z -9.9) |
| [[LOX-IMVI (line)]] | wt | 12.6 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.125× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.264× (z -10.4) |
| [[SNU-1 (line)]] | wt | 38.0 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.192× (z -9.8) |
| [[A-172 (line)]] | wt | 22.0 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.295× (z -8.6) |
| [[C32 (line)]] | wt | 24.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -11.8) |
| [[CFPAC-1 (line)]] | alt | 20.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.390× (z -8.9) |
| [[CHP-212 (line)]] | wt | 17.3 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0219× (z -12.4) |
| [[HepG2_C3A (line)]] | wt | 29.4 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.188× (z -9.9) |
| [[HOP62 (line)]] | alt | 12.5 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.185× (z -9.2) |
| [[RKO (line)]] | wt | 15.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0536× (z -15.0) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 28.3 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.210× (z -8.8) |
| [[SK-MEL-2 (line)]] | alt | 13.9 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.131× (z -10.0) |
| [[SNU-423 (line)]] | alt | 22.4 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.223× (z -9.4) |
| [[SW 1271 (line)]] | alt | 36.4 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0443× (z -10.1) |
| [[SW48 (line)]] | wt | 24.4 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.140× (z -9.0) |
| [[A498 (line)]] | wt | 6.96 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.04 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.43 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.06 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.97 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 21.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9329), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00623]] | +0.59 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[SOCS6]] | +0.54 | +0.48 / +0.41 | both halves | 4e-05 |  |
| [[DCPS]] | +0.54 | +0.48 / +0.38 | both halves | 6e-05 |  |
| [[PYM1]] | +0.54 | +0.54 / +0.38 | both halves | 7e-05 |  |
| [[CLK4]] | +0.54 | +0.50 / +0.38 | both halves | 7e-05 |  |
| [[SREK1]] | +0.53 | +0.47 / +0.33 | both halves | 1e-04 |  |
| [[CHAMP1]] | +0.53 | +0.57 / +0.39 | both halves | 5e-05 |  |
| [[ZC3H7B]] | +0.53 | +0.59 / +0.31 | both halves | 2e-04 |  |
| [[UPF3A]] | +0.52 | +0.58 / +0.33 | both halves | 1e-04 |  |
| [[SMIM19]] | +0.52 | +0.48 / +0.44 | both halves | 3e-05 |  |
| [[SEMA4C]] | +0.52 | +0.43 / +0.52 | both halves | 3e-05 |  |
| [[LIPT1]] | +0.52 | +0.45 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRDX1]] | -0.54 | -0.53 / -0.38 | both halves | 7e-05 |  |
| [[NUCB1]] | -0.49 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[ERP44]] | -0.48 | -0.47 / -0.37 | both halves | 8e-05 |  |
| [[TPST2]] | -0.48 | -0.41 / -0.33 | both halves | 1e-04 |  |
| [[LMAN1]] | -0.47 | -0.43 / -0.37 | both halves | 8e-05 |  |
| [[GNB2]] | -0.47 | -0.52 / -0.15 | ⚠ one half (not replicated) | 0.001 |  |
| [[PPP2R3A]] | -0.47 | -0.47 / -0.37 | both halves | 9e-05 |  |
| [[NBEAL1]] | -0.47 | -0.39 / -0.37 | both halves | 7e-05 |  |
| [[RHOA]] | -0.47 | -0.40 / -0.41 | both halves | 4e-05 |  |
| [[IDS]] | -0.46 | -0.39 / -0.43 | both halves | 5e-05 |  |
| [[CLTC]] | -0.46 | -0.54 / -0.40 | both halves | 5e-05 |  |
| [[TKT]] | -0.46 | -0.41 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IRX3]] | B | IRX3 activity raises TK2's level | lines that do not express IRX3 (9) vs lines expressing it (41) | 1.40× lower at baseline in the lines without IRX3 | 0.036 | ⚠ within organs, on part of the lines; also absent: DYSF, DRAM1, LINC02609 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 095]] — Chromatin organization; 48 genes; this gene is in the **+** arm (projection on the module's main direction 0.449). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.36).
- **Nodal map** (x, y) = (-31.7, 18.5); signed map (10.2, -38.0). **Vector** length 65.1, 13.7% of its response variance represented; |z| ≥ 3 in 1,236 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.7 | -4.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.5 | -9.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.9 | +1.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.8 | -2.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.8 | +0.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.2 | +3.5 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.7 | +3.9 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +1.6 | +1.4 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.6 | +2.7 |
| fall | [[Auranofin (drug)]] 5 µM |  | -3.8 | -10.0 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -2.9 | -8.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.8 | -11.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.8 | -10.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.6 | -2.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.5 | -0.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.5 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | thymidine kinase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q21 — chr16:66,508,003-66,552,544 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SCA31 |
| Gene groups (HGNC) | Deoxyribonucleoside kinases |
| Hallmark sets | DNA_REPAIR |
| Reactome | 3 pathways, smallest: Pyrimidine salvage; Nucleotide salvage; Metabolism of nucleotides |
| Matched by | ensembl_id |

**Function**, from UniProt [O00142](https://www.uniprot.org/uniprotkb/O00142) (Thymidine kinase 2, mitochondrial):

> Phosphorylates thymidine, deoxycytidine, and deoxyuridine in the mitochondrial matrix. In non-replicating cells, where cytosolic dNTP synthesis is down-regulated, mtDNA synthesis depends solely on TK2 and DGUOK. Widely used as target of antiviral and chemotherapeutic agents.

**Summary**, from NCBI Gene [7084](https://www.ncbi.nlm.nih.gov/gene/7084):

> This gene encodes a deoxyribonucleoside kinase that specifically phosphorylates thymidine, deoxycytidine, and deoxyuridine. The encoded enzyme localizes to the mitochondria and is required for mitochondrial DNA synthesis. Mutations in this gene are associated with a myopathic form of mitochondrial DNA depletion syndrome. Alternate splicing results in multiple transcript variants encoding distinct isoforms, some of which lack transit peptide, so are not localized to mitochondria. [provided by …

**Accessions** — [HGNC:11831](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11831) · Entrez [7084](https://www.ncbi.nlm.nih.gov/gene/7084) · UniProt [O00142](https://www.uniprot.org/uniprotkb/O00142) · Ensembl [ENSG00000166548](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166548)

## Data

Gene col 9329: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9329); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9329, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9329]; `tensor/DDL_lfc|DDL_z.npy` [9329]; `embed/gene_vectors.npy` [9329]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9329 or target_col == 9329). Every well: [[TK2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TK2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
