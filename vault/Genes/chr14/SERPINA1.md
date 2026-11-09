---
symbol: "SERPINA1"
type: "gene"
col: 12368
ensembl_id: "ENSG00000197249"
name: "serpin family A member 1"
location: "14q32.13"
module: 155
arm: "+"
pooled_cpm: 84.23
n_lines_expressing: 16
n_dd_up: 6
n_dd_down: 11
n_dd_up_clean: 1
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 19
direction_downstream: 14
tags: ["gene", "module/155"]
generated_by: "tahoemap"
---

# SERPINA1

*serpin family A member 1* — 14q32.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.48× (z +11.9, q 1e-29, up in 9 of 15 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.67× (z +6.9, q 8e-10, up in 4 of 15 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Harringtonine (drug)]] 5 µM in 2 lines (Panc 03.27 4.55×, HOP62 5.11×; ⚠ cell-cycle shift, would explain all of this change); [[Canagliflozin (hemihydrate) (drug)]] 5 µM in 1 line (NCI-H596 18.4×); [[Homoharringtonine (drug)]] 5 µM in 1 line (Panc 03.27 3.25×; ⚠ cell-cycle shift, explains ~0% of this change); [[Fulvestrant (drug)]] 5 µM in 1 line (NCI-H596 14.4×).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.568× (z -5.4, q 4e-05, down in 10 of 14 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FGB]] (+0.66, fdr 1e-05), [[S100A9]] (+0.63, fdr 1e-05), [[GSDMC]] (+0.63, fdr 1e-05); moves opposite to [[ANKRD30A]] (-0.45, fdr 6e-05), [[ZNF552]] (-0.44, fdr 1e-04).
> It is in [[Module 155]], a single-armed module (MyD88 deficiency (TLR2/4)).
> Probable direction (from the cell lines, not proof of direct regulation): 19 arrows point to it, the strongest [[FRY]] → it (grade B ⚠); 14 go from it, the strongest it → [[SLC16A3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 5 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12368.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Harringtonine (drug)]] 5 µM in 2 lines (Panc 03.27 4.55×, HOP62 5.11×; ⚠ cell-cycle shift, would explain all of this change); [[Canagliflozin (hemihydrate) (drug)]] 5 µM in 1 line (NCI-H596 18.4×); [[Homoharringtonine (drug)]] 5 µM in 1 line (Panc 03.27 3.25×; ⚠ cell-cycle shift, explains ~0% of this change); [[Fulvestrant (drug)]] 5 µM in 1 line (NCI-H596 14.4×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.48×** | +11.9 | 1e-29 | 9/15 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.16×** | +10.5 | 2e-23 | 6/12 (H4, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.30×** | +7.3 | 5e-11 | 4/13 (SW480, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.67×** | +6.9 | 8e-10 | 4/15 (Panc 03.27, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **1.80×** | +5.6 | 3e-06 | 5/14 (SNU-423, SW480, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~43% of this change | **1.58×** | +4.3 | 0.001 | 4/14 (H4, SW48, …) | inconsistent across doses | low cells (technical?) |
| [[Arbutin (drug)]] 0.05 µM |  | 1.41× | +3.0 | 0.21 | 7/14 (Panc 03.27, SW48, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, none with an alert. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12368.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.568×** | -5.4 | 4e-05 | 10/14 (HT-29, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.639×** | -3.9 | 0.023 | 6/14 (HOP62, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **0.672×** | -3.8 | 0.029 | 2/14 (BT-474, SW480) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.678×** | -3.7 | 0.031 | 4/14 (HOP62, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.691×** | -3.5 | 0.039 | 8/14 (MIA PaCa-2, HepG2/C3A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.485×** | -3.5 | 0.039 | 7/15 (HT-29, CFPAC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **0.694×** | -3.5 | 0.039 | 11/14 (HT-29, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.759×** | -3.5 | 0.039 | 5/14 (HOP62, SW48, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM |  | **0.655×** | -3.4 | 0.043 | 6/16 (HOP62, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~17% here); noisy plate (z scaled) |
| [[Erlotinib (drug)]] 0.05 µM |  | **0.689×** | -3.3 | 0.059 | 1/14 (SW480) | inconsistent across doses | position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.708×** | -3.2 | 0.081 | 7/14 (SK-MEL-2, HOP62, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | 0.725× | -3.1 | 0.11 | 5/14 (HepG2/C3A, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~16% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12368. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 35.2 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0717× (z -11.1) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 362 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.225× (z -14.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.273× (z -8.9) |
| [[NCI-H596 (line)]] | alt | 86.6 | 2 | 1 | [[Canagliflozin (hemihydrate) (drug)]] 5 µM 18.4× (z +14.2) | [[Atazanavir (sulfate) (drug)]] 0.05 µM 0.166× (z -8.7) |
| [[HepG2_C3A (line)]] | wt | 4,284 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.288× (z -13.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.297× (z -9.3) |
| [[HOP62 (line)]] | alt | 124 | 1 (1 ⚠) | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 5.11× (z +9.8) ⚠ cell-cycle shift, would explain all of this change | [[Adagrasib (drug)]] 0.05 µM 0.627× (z -10.4) ⚠ position not correctable |
| [[MIA PaCa-2 (line)]] | alt | 44.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.131× (z -11.3) |
| [[Panc 03.27 (line)]] | alt | 100 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +13.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[CFPAC-1 (line)]] | alt | 342 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.395× (z -9.4) ⚠ cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 25.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.76× (z +11.0) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 9.33 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 6.26 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 10.9 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 8.15 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 15.4 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 7.95 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 8.69 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 6.43 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 10.9 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 7.80 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 24.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 13.0 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.20 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 7.13 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.2 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 6.09 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 14.2 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 6.94 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 8.23 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 11.2 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 10.9 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 5.65 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 8.17 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 86.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.35 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 39.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 6.39 n.m. | — | — | — | — |
| [[NCI-H661 (line)]] | alt | 12.2 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 5.84 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 15.4 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 6.13 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 19.9 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.92 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 51.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.5 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 19.5 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 17.0 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 19.2 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 22.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12368), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FGB]] | +0.66 | +0.57 / +0.64 | both halves | 1e-05 | pathway: Platelet activation, signaling and aggregation; STRING 810 |
| [[S100A9]] | +0.63 | +0.54 / +0.65 | both halves | 1e-05 | pathway: HALLMARK_COMPLEMENT; STRING 590 |
| [[GSDMC]] | +0.63 | +0.56 / +0.61 | both halves | 1e-05 | **novel candidate** |
| [[SLPI]] | +0.63 | +0.51 / +0.60 | both halves | 1e-05 | STRING 621 |
| [[ADGRE2]] | +0.63 | +0.52 / +0.65 | both halves | 1e-05 | **novel candidate** |
| [[PI3]] | +0.62 | +0.48 / +0.61 | both halves | 2e-05 | STRING 498 |
| [[CES1]] | +0.60 | +0.48 / +0.57 | both halves | 2e-05 | **novel candidate** |
| [[SERPINA3]] | +0.59 | +0.59 / +0.60 | both halves | 7e-06 | same gene group; pathway: HALLMARK_ESTROGEN_RESPONSE_LATE; STRING 680 |
| [[FGG]] | +0.58 | +0.46 / +0.58 | both halves | 3e-05 | pathway: HALLMARK_COAGULATION; STRING 886 |
| [[IL4R]] | +0.57 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[S100A8]] | +0.57 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[AQP3]] | +0.56 | +0.36 / +0.61 | both halves | 9e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKRD30A]] | -0.45 | -0.44 / -0.39 | both halves | 6e-05 |  |
| [[ZNF552]] | -0.44 | -0.34 / -0.49 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 1, C 18. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FRY]] | B | FRY activity raises SERPINA1's level | lines that do not express FRY (14) vs lines expressing it (36) | 1.75× lower at baseline in the lines without FRY | 0.058 | ⚠ within organs, on part of the lines; also absent: ADGRV1, DTNA, ZNF385B |
| [[SERPINA5]] | C | SERPINA5 activity raises SERPINA1's level | lines that do not express SERPINA5 (37) vs lines expressing it (13) | 6.96× lower at baseline in the lines without SERPINA5 | 4e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LINC02899, SERPINA1, ENSG00000286546; co-absent with the target |
| [[SLC6A14]] | C | SLC6A14 activity raises SERPINA1's level | lines that do not express SLC6A14 (39) vs lines expressing it (11) | 6.09× lower at baseline in the lines without SLC6A14 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DAPP1, MUC5AC, ST6GALNAC1; co-absent with the target |
| [[MUC5AC]] | C | MUC5AC activity raises SERPINA1's level | lines that do not express MUC5AC (39) vs lines expressing it (11) | 4.83× lower at baseline in the lines without MUC5AC | 0.025 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC6A14, GABRP, AGR3; co-absent with the target |
| [[MUC5B]] | C | MUC5B activity raises SERPINA1's level | lines that do not express MUC5B (37) vs lines expressing it (13) | 2.41× lower at baseline in the lines without MUC5B | 0.025 | ⚠ within organs, on part of the lines; also absent: DAPP1, AGR3, ENSG00000259925; co-absent with the target |
| [[LRG1]] | C | LRG1 activity raises SERPINA1's level | lines that do not express LRG1 (28) vs lines expressing it (22) | 3.49× lower at baseline in the lines without LRG1 | 0.030 | ⚠ within organs, on part of the lines; also absent: RORC, LAD1, EPCAM; co-absent with the target |
| [[SERPINA3]] | C | SERPINA3 activity raises SERPINA1's level | lines that do not express SERPINA3 (36) vs lines expressing it (14) | 3.41× lower at baseline in the lines without SERPINA3 | 0.032 | ⚠ within organs, on part of the lines; also absent: ENSG00000286546, LINC02099, SERPINA5; co-absent with the target |
| [[STEAP4]] | C | STEAP4 activity raises SERPINA1's level | lines that do not express STEAP4 (38) vs lines expressing it (12) | 2.45× lower at baseline in the lines without STEAP4 | 0.044 | ⚠ within organs, on part of the lines; also absent: ADGRF1, WFDC2, SLC5A1; co-absent with the target |
| [[FAM83A]] | C | FAM83A activity raises SERPINA1's level | lines that do not express FAM83A (37) vs lines expressing it (13) | 2.18× lower at baseline in the lines without FAM83A | 0.048 | ⚠ within organs, on part of the lines; also absent: GSDMC, DAPP1, S100A9; co-absent with the target |
| [[TNNT2]] | C | TNNT2 activity raises SERPINA1's level | lines that do not express TNNT2 (29) vs lines expressing it (21) | 2.92× lower at baseline in the lines without TNNT2 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, ATP2C2, ST14; co-absent with the target |
| [[LCN2]] | C | LCN2 activity raises SERPINA1's level | lines that do not express LCN2 (33) vs lines expressing it (17) | 3.33× lower at baseline in the lines without LCN2 | 0.061 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: PRSS8, RAB25, TMPRSS4; co-absent with the target |
| [[KRT23]] | C | KRT23 activity raises SERPINA1's level | lines that do not express KRT23 (40) vs lines expressing it (10) | 4.71× lower at baseline in the lines without KRT23 | 0.061 | ⚠ within organs, on part of the lines; also absent: PROM1, HSD17B2, GABRP; co-absent with the target |

### Downstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 4, C 10. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC16A3]] | B | SERPINA1 activity raises SLC16A3's level | lines that do not express SERPINA1 (34) vs lines expressing it (16) | 1.98× lower at baseline in the lines without SERPINA1 | 0.036 | ⚠ within organs, on part of the lines; also absent: SERPINA5, CST6, SERPINA3 |
| [[NIBAN2]] | B | SERPINA1 activity raises NIBAN2's level | lines that do not express SERPINA1 (34) vs lines expressing it (16) | 1.72× lower at baseline in the lines without SERPINA1 | 0.037 | ⚠ within organs, on part of the lines; also absent: SERPINA5, CST6, SERPINA3 |
| [[ZNF552]] | B | SERPINA1 activity raises ZNF552's level | lines that do not express SERPINA1 (34) vs lines expressing it (16) | 1.27× lower at baseline in the lines without SERPINA1 | 0.056 | ⚠ within organs, on part of the lines; also absent: SERPINA5, CST6, SERPINA3 |
| [[AQP3]] | B | SERPINA1 activity raises AQP3's level | lines that do not express SERPINA1 (34) vs lines expressing it (16) | 1.87× lower at baseline in the lines without SERPINA1 | 0.072 | ⚠ within organs, on part of the lines; also absent: SERPINA5, CST6, SERPINA3 |
| [[SERPINA5]] | C | SERPINA1 activity raises SERPINA5's level | lines that do not express SERPINA1 (34) vs lines expressing it (16) | 3.02× lower at baseline in the lines without SERPINA1 | 0.007 | ⚠ within organs, on part of the lines; also absent: SERPINA5, CST6, SERPINA3; co-absent with the target |
| [[SERPINA3]] | C | SERPINA1 activity raises SERPINA3's level | lines that do not express SERPINA1 (34) vs lines expressing it (16) | 5.51× lower at baseline in the lines without SERPINA1 | 0.007 | ⚠ within organs, on part of the lines; also absent: SERPINA5, CST6, SERPINA3; co-absent with the target |
| [[STEAP4]] | C | SERPINA1 activity raises STEAP4's level | lines that do not express SERPINA1 (34) vs lines expressing it (16) | 2.71× lower at baseline in the lines without SERPINA1 | 0.032 | ⚠ within organs, on part of the lines; also absent: SERPINA5, CST6, SERPINA3; co-absent with the target |
| [[TNNT2]] | C | SERPINA1 activity raises TNNT2's level | lines that do not express SERPINA1 (34) vs lines expressing it (16) | 2.32× lower at baseline in the lines without SERPINA1 | 0.049 | ⚠ within organs, on part of the lines; also absent: SERPINA5, CST6, SERPINA3; co-absent with the target |
| [[IL1RN]] | C | SERPINA1 activity raises IL1RN's level | lines that do not express SERPINA1 (34) vs lines expressing it (16) | 2.42× lower at baseline in the lines without SERPINA1 | 0.054 | ⚠ within organs, on part of the lines; also absent: SERPINA5, CST6, SERPINA3; co-absent with the target |
| [[SLC6A14]] | C | SERPINA1 activity raises SLC6A14's level | lines that do not express SERPINA1 (34) vs lines expressing it (16) | 3.15× lower at baseline in the lines without SERPINA1 | 0.058 | ⚠ within organs, on part of the lines; also absent: SERPINA5, CST6, SERPINA3; co-absent with the target |
| [[SCNN1A]] | C | SERPINA1 activity raises SCNN1A's level | lines that do not express SERPINA1 (34) vs lines expressing it (16) | 2.71× lower at baseline in the lines without SERPINA1 | 0.063 | ⚠ within organs, on part of the lines; also absent: SERPINA5, CST6, SERPINA3; co-absent with the target |
| [[SGPP2]] | C | SERPINA1 activity raises SGPP2's level | lines that do not express SERPINA1 (34) vs lines expressing it (16) | 2.83× lower at baseline in the lines without SERPINA1 | 0.071 | ⚠ within organs, on part of the lines; also absent: SERPINA5, CST6, SERPINA3; co-absent with the target |

## Where it sits

- **Module**: [[Module 155]] — MyD88 deficiency (TLR2/4); 29 genes; every member is in the + arm (projection on the module's main direction 0.681). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (36.7, 48.9); signed map (55.3, 24.1). **Vector** length 49.5, 15.2% of its response variance represented; |z| ≥ 3 in 397 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MyD88 deficiency (TLR2/4)* (reactome, mean cos +0.61 to 4); *IRAK4 deficiency (TLR2/4)* (reactome, mean cos +0.61 to 4); *Regulation of TLR by endogenous ligand* (reactome, mean cos +0.61 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.6 | +6.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.0 | +2.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.7 | +10.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +2.6 | -1.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.5 | +11.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.3 | +1.8 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +1.3 | +2.9 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +1.3 | +2.1 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.3 | +2.7 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -2.4 | -2.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.4 | -3.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.3 | -2.0 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.3 | -1.2 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.2 | +0.1 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.1 | -1.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.0 | -2.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.0 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | serpin family A member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q32.13 — chr14:94,376,747-94,390,693 (-) |
| Ensembl biotype | protein_coding |
| Also known as | AAT, A1A, PI1, alpha-1-antitrypsin, A1AT, alpha1AT; previously PI |
| Gene groups (HGNC) | Serpin peptidase inhibitors |
| Hallmark sets | COAGULATION, COMPLEMENT, ESTROGEN_RESPONSE_LATE |
| Reactome | 15 pathways, smallest: Cargo concentration in the ER; COPII-mediated vesicle transport; Post-translational protein phosphorylation |
| Matched by | ensembl_id |

**Function**, from UniProt [P01009](https://www.uniprot.org/uniprotkb/P01009) (Alpha-1-antitrypsin):

> Inhibitor of serine proteases. Its primary target is elastase, but it also has a moderate affinity for plasmin and thrombin. Irreversibly inhibits trypsin, chymotrypsin and plasminogen activator. The aberrant form inhibits insulin-induced NO synthesis in platelets, decreases coagulation time and has proteolytic activity against insulin and plasmin.; [Short peptide from AAT]: Reversible chymotrypsin inhibitor. It also inhibits elastase, but not trypsin. Its major physiological function is the …

**Summary**, from NCBI Gene [5265](https://www.ncbi.nlm.nih.gov/gene/5265):

> The protein encoded by this gene is a serine protease inhibitor belonging to the serpin superfamily whose targets include elastase, plasmin, thrombin, trypsin, chymotrypsin, and plasminogen activator. This protein is produced in the liver, the bone marrow, by lymphocytic and monocytic cells in lymphoid tissue, and by the Paneth cells of the gut. Defects in this gene are associated with chronic obstructive pulmonary disease, emphysema, and chronic liver disease. Several transcript variants …

**Accessions** — [HGNC:8941](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8941) · Entrez [5265](https://www.ncbi.nlm.nih.gov/gene/5265) · UniProt [P01009](https://www.uniprot.org/uniprotkb/P01009) · Ensembl [ENSG00000197249](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197249)

## Data

Gene col 12368: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12368); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12368, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12368]; `tensor/DDL_lfc|DDL_z.npy` [12368]; `embed/gene_vectors.npy` [12368]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12368 or target_col == 12368). Every well: [[SERPINA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SERPINA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
