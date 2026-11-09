---
symbol: "HAVCR1"
type: "gene"
col: 3440
ensembl_id: "ENSG00000113249"
name: "hepatitis A virus cellular receptor 1"
location: "5q33.3"
module: 8
arm: "+"
pooled_cpm: 6.16
n_lines_expressing: 11
n_dd_up: 35
n_dd_down: 0
n_dd_up_clean: 23
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 12
direction_downstream: 19
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# HAVCR1

*hepatitis A virus cellular receptor 1* — 5q33.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 35 drug-doses (12 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.52× (z +16.8, q 0e+00, up in 4 of 9 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Proglumide (drug)]] 0.05 µM in 1 line (NCI-H2347 0.0495×); [[Selinexor (drug)]] 5 µM in 1 line (A498 0.316×; ⚠ cell-cycle shift, explains ~0% of this change); [[Bortezomib (drug)]] 0.05 µM in 1 line (A549 0.143×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (CFPAC-1 0.263×); [[Posaconazole (drug)]] 0.5 µM in 1 line (LoVo 0.0507×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TIMD4]] (+0.80, fdr 7e-06), [[POU5F1]] (+0.72, fdr 1e-05), [[FGA]] (+0.70, fdr 7e-06); moves opposite to [[MPG]] (-0.50, fdr 4e-05), [[PBX4]] (-0.47, fdr 1e-04), [[SPRY4]] (-0.46, fdr 3e-05).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 19 go from it, the strongest it → [[EFNA1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 12 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 35 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3440.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.52×** | +16.8 | 0e+00 | 4/9 (A498, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.93×** | +14.0 | 4e-42 | 6/6 (A498, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.92×** | +13.5 | 5e-39 | 5/6 (A498, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.92×** | +11.9 | 2e-30 | 3/9 (LoVo, HCT15, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.69×** | +11.2 | 3e-27 | 5/6 (A498, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **3.16×** | +9.0 | 1e-17 | 1/9 (HCT15) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **2.00×** | +7.7 | 1e-12 | 2/9 (NCI-H2347, HepG2/C3A) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.78×** | +6.4 | 1e-08 | 3/9 (NCI-H2347, A498, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.02×** | +5.5 | 2e-06 | 0/8 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.00×** | +5.4 | 3e-06 | 1/8 (LoVo) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.99×** | +5.2 | 1e-05 | 1/9 (CFPAC-1) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.33×** | +4.9 | 4e-05 | 5/9 (A498, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.91×** | +4.9 | 5e-05 | 1/7 (NCI-H2347) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.20×** | +4.8 | 7e-05 | 1/5 (HEC-1-A) | top dose only | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.68×** | +4.7 | 1e-04 | 6/9 (HEC-1-A, A549, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.75×** | +4.2 | 8e-04 | 1/9 (NCI-H2347) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.64×** | +3.9 | 0.003 | 3/9 (NCI-H2347, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.44×** | +3.9 | 0.003 | 5/9 (HEC-1-A, CFPAC-1, …) | all doses, flat |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.45×** | +3.7 | 0.006 | 0/8 | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.52×** | +3.1 | 0.037 | 7/9 (HEC-1-A, A549, …) | rises with dose | position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.75×** | +3.1 | 0.039 | 0/7 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3440.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Proglumide (drug)]] 0.05 µM in 1 line (NCI-H2347 0.0495×); [[Selinexor (drug)]] 5 µM in 1 line (A498 0.316×; ⚠ cell-cycle shift, explains ~0% of this change); [[Bortezomib (drug)]] 0.05 µM in 1 line (A549 0.143×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (CFPAC-1 0.263×); [[Posaconazole (drug)]] 0.5 µM in 1 line (LoVo 0.0507×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 0.5 µM |  | 0.642× | -3.5 | 0.23 | 1/9 (NCI-H2347) | all doses, flat |  |
| [[PH-797804 (drug)]] 0.05 µM |  | 0.664× | -3.1 | 0.59 | 0/9 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, +0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3440. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 59.0 | 4 (1 ⚠) | 0 | [[Binimetinib (drug)]] 5 µM 4.03× (z +9.5) | — |
| [[A498 (line)]] | wt | 25.9 | 1 (1 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.68× (z +9.2) ⚠ toxic; transcription drop | [[Selinexor (drug)]] 5 µM 0.316× (z -10.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 70.3 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.143× (z -10.2) ⚠ cell-cycle shift, would explain all of this change |
| [[CFPAC-1 (line)]] | alt | 12.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -8.9) |
| [[LoVo (line)]] | wt | 2.52 | 0 | 1 | — | [[Posaconazole (drug)]] 0.5 µM 0.0507× (z -8.8) |
| [[NCI-H2347 (line)]] | alt | 3.07 | 0 | 1 | — | [[Proglumide (drug)]] 0.05 µM 0.0495× (z -10.4) |
| [[A-172 (line)]] | wt | 0.546 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.402 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.746 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.484 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.699 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.460 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.549 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.694 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.621 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.15 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.604 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.477 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.534 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.718 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.788 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.421 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.552 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.600 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.487 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.398 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.824 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.720 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.472 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.470 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.495 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.434 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.476 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.526 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.553 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.542 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.611 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.598 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.881 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.654 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.581 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.536 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.571 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.517 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3440), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TIMD4]] | +0.80 | +0.88 / +0.65 | both halves | 7e-06 | same gene group; pathway: Dengue Virus Attachment and Entry; STRING 857 |
| [[POU5F1]] | +0.72 | +0.69 / +0.56 | both halves | 1e-05 | **novel candidate** |
| [[FGA]] | +0.70 | +0.76 / +0.60 | both halves | 7e-06 |  |
| [[SLC4A4]] | +0.66 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[RHEX]] | +0.64 | +0.70 / +0.50 | both halves | 1e-05 |  |
| [[CP]] | +0.62 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[PON3]] | +0.61 | +0.57 / +0.43 | both halves | 4e-05 |  |
| [[CFH]] | +0.59 | +0.49 / +0.45 | both halves | 3e-05 |  |
| [[PBX1]] | +0.58 | +0.46 / +0.44 | both halves | 3e-05 |  |
| [[SLC34A2]] | +0.57 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[DCDC2]] | +0.57 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[GUCY1B2]] | +0.57 | +0.51 / +0.40 | both halves | 4e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MPG]] | -0.50 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[PBX4]] | -0.47 | -0.34 / -0.43 | both halves | 1e-04 |  |
| [[SPRY4]] | -0.46 | -0.43 / -0.43 | both halves | 3e-05 |  |
| [[PLEK2]] | -0.45 | -0.35 / -0.39 | both halves | 1e-04 |  |
| [[TOR4A]] | -0.44 | -0.33 / -0.40 | both halves | 1e-04 |  |
| [[HMOX2]] | -0.44 | -0.32 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 1, C 11.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers HAVCR1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.6% of all compounds | 0.071 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TIMD4]] | C | TIMD4 activity raises HAVCR1's level | lines that do not express TIMD4 (40) vs lines expressing it (10) | 6.84× lower at baseline in the lines without TIMD4 | 4e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HAVCR1, RHEX, FGA; co-absent with the target |
| [[FGA]] | C | FGA activity raises HAVCR1's level | lines that do not express FGA (43) vs lines expressing it (7) | 4.12× lower at baseline in the lines without FGA | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGB, ITIH2, FGG; co-absent with the target |
| [[LINC00278]] | C | LINC00278 activity raises HAVCR1's level | lines that do not express LINC00278 (32) vs lines expressing it (18) | 1.67× lower at baseline in the lines without LINC00278 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZFY, PRKY, RPS4Y1; co-absent with the target |
| [[FGG]] | C | FGG activity raises HAVCR1's level | lines that do not express FGG (42) vs lines expressing it (8) | 3.33× lower at baseline in the lines without FGG | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGB, FGA, APOB; co-absent with the target |
| [[FXYD2]] | C | FXYD2 activity raises HAVCR1's level | lines that do not express FXYD2 (38) vs lines expressing it (12) | 2.50× lower at baseline in the lines without FXYD2 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DSCAML1, ITIH2, FGA; co-absent with the target |
| [[CYP24A1]] | C | CYP24A1 activity raises HAVCR1's level | lines that do not express CYP24A1 (39) vs lines expressing it (11) | 2.44× lower at baseline in the lines without CYP24A1 | 0.041 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGA, S100A9, FGG; co-absent with the target |
| [[IGFBP1]] | C | IGFBP1 activity raises HAVCR1's level | lines that do not express IGFBP1 (39) vs lines expressing it (11) | 2.28× lower at baseline in the lines without IGFBP1 | 0.053 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGA, FGB, ITIH2; co-absent with the target |
| [[SLCO1B1]] | C | SLCO1B1 activity raises HAVCR1's level | lines that do not express SLCO1B1 (28) vs lines expressing it (22) | 1.65× lower at baseline in the lines without SLCO1B1 | 0.057 | ⚠ within organs, on part of the lines; also absent: ENSG00000257062, SLCO1B3, SLCO1B3-SLCO1B7; co-absent with the target |
| [[POU5F1]] | C | POU5F1 activity raises HAVCR1's level | lines that do not express POU5F1 (27) vs lines expressing it (23) | 2.26× lower at baseline in the lines without POU5F1 | 0.060 | ⚠ within organs, on part of the lines; also absent: P2RY2, C4BPB, UGT1A6; co-absent with the target |
| [[TM4SF4]] | C | TM4SF4 activity raises HAVCR1's level | lines that do not express TM4SF4 (42) vs lines expressing it (8) | 3.21× lower at baseline in the lines without TM4SF4 | 0.076 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PIGR, MUC17, HHLA2; co-absent with the target |
| [[DSCAML1]] | C | DSCAML1 activity raises HAVCR1's level | lines that do not express DSCAML1 (37) vs lines expressing it (13) | 2.84× lower at baseline in the lines without DSCAML1 | 0.097 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FXYD2, ITIH2, FGG; co-absent with the target |

### Downstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 4, C 15. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EFNA1]] | B | HAVCR1 activity raises EFNA1's level | lines that do not express HAVCR1 (39) vs lines expressing it (11) | 2.57× lower at baseline in the lines without HAVCR1 | 0.038 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TIMD4, RHEX, FGA |
| [[RBPMS]] | B | HAVCR1 activity raises RBPMS's level | lines that do not express HAVCR1 (39) vs lines expressing it (11) | 2.93× lower at baseline in the lines without HAVCR1 | 0.045 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TIMD4, RHEX, FGA |
| [[MTUS1-DT]] | B | HAVCR1 activity raises MTUS1-DT's level | lines that do not express HAVCR1 (39) vs lines expressing it (11) | 2.17× lower at baseline in the lines without HAVCR1 | 0.069 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TIMD4, RHEX, FGA |
| [[SLC44A3-AS1]] | B | HAVCR1 activity raises SLC44A3-AS1's level | lines that do not express HAVCR1 (39) vs lines expressing it (11) | 2.49× lower at baseline in the lines without HAVCR1 | 0.078 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TIMD4, RHEX, FGA |
| [[LINC00278]] | C | HAVCR1 activity raises LINC00278's level | lines that do not express HAVCR1 (39) vs lines expressing it (11) | 3.12× lower at baseline in the lines without HAVCR1 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TIMD4, RHEX, FGA; co-absent with the target |
| [[POU5F1]] | C | HAVCR1 activity raises POU5F1's level | lines that do not express HAVCR1 (39) vs lines expressing it (11) | 5.92× lower at baseline in the lines without HAVCR1 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TIMD4, RHEX, FGA; co-absent with the target |
| [[TIMD4]] | C | HAVCR1 activity raises TIMD4's level | lines that do not express HAVCR1 (39) vs lines expressing it (11) | 3.26× lower at baseline in the lines without HAVCR1 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TIMD4, RHEX, FGA; co-absent with the target |
| [[SLCO1B1]] | C | HAVCR1 activity raises SLCO1B1's level | lines that do not express HAVCR1 (39) vs lines expressing it (11) | 2.11× lower at baseline in the lines without HAVCR1 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TIMD4, RHEX, FGA; co-absent with the target |
| [[ARSL]] | C | HAVCR1 activity raises ARSL's level | lines that do not express HAVCR1 (39) vs lines expressing it (11) | 3.58× lower at baseline in the lines without HAVCR1 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TIMD4, RHEX, FGA; co-absent with the target |
| [[DCDC2]] | C | HAVCR1 activity raises DCDC2's level | lines that do not express HAVCR1 (39) vs lines expressing it (11) | 4.53× lower at baseline in the lines without HAVCR1 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TIMD4, RHEX, FGA; co-absent with the target |
| [[IGFBP1]] | C | HAVCR1 activity raises IGFBP1's level | lines that do not express HAVCR1 (39) vs lines expressing it (11) | 4.18× lower at baseline in the lines without HAVCR1 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TIMD4, RHEX, FGA; co-absent with the target |
| [[RHEX]] | C | HAVCR1 activity raises RHEX's level | lines that do not express HAVCR1 (39) vs lines expressing it (11) | 4.87× lower at baseline in the lines without HAVCR1 | 0.024 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TIMD4, RHEX, FGA; co-absent with the target |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.484). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (37.6, 44.2); signed map (51.8, 26.8). **Vector** length 34.4, 11.2% of its response variance represented; |z| ≥ 3 in 273 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.4 | +13.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.1 | +14.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.9 | +11.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.3 | +7.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +1.8 | +3.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.7 | +2.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.6 | +4.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.6 | +2.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.5 | +3.1 |
| fall | [[5-Azacytidine (drug)]] 5 µM |  | -1.4 | -1.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.0 | -1.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.0 | +0.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.0 | -1.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -0.9 | -1.3 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -0.8 | -2.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.8 | -2.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.7 | -3.5 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.7 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | hepatitis A virus cellular receptor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q33.3 — chr5:157,026,742-157,069,396 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HAVCR-1, TIM-1, TIM1, HAVCR, TIMD1, CD365, KIM1 |
| Gene groups (HGNC) | CD molecules; V-set domain containing |
| Reactome | 7 pathways, smallest: Attachment and Entry_9694614; Early SARS-CoV-2 Infection Events; Dengue Virus Attachment and Entry |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96D42](https://www.uniprot.org/uniprotkb/Q96D42) (Hepatitis A virus cellular receptor 1):

> Phosphatidylserine receptor that plays an important functional role in regulatory B-cell homeostasis including generation, expansion and suppressor functions. Involved in efferocytosis, the process by which apoptotic cells are removed, by binding to phosphatidylserine present on apoptotic cells and promoting their engulfment. Confers phagocytic ability on injured kidney epithelial cells, allowing them to bind to and internalize apoptotic bodies and necrotic debris following kidney injury. The …

**Summary**, from NCBI Gene [26762](https://www.ncbi.nlm.nih.gov/gene/26762):

> The protein encoded by this gene is a membrane receptor for both human hepatitis A virus (HHAV) and TIMD4. The encoded protein may be involved in the moderation of asthma and allergic diseases. The reference genome represents an allele that retains a MTTVP amino acid segment that confers protection against atopy in HHAV seropositive individuals. The protein is a receptor for multiple other viruses, including Ebola virus, Marburg virus, Dengue virus, and Zika virus and is a possible entry factor …

**Accessions** — [HGNC:17866](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17866) · Entrez [26762](https://www.ncbi.nlm.nih.gov/gene/26762) · UniProt [Q96D42](https://www.uniprot.org/uniprotkb/Q96D42) · Ensembl [ENSG00000113249](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000113249)

## Data

Gene col 3440: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3440); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3440, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3440]; `tensor/DDL_lfc|DDL_z.npy` [3440]; `embed/gene_vectors.npy` [3440]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3440 or target_col == 3440). Every well: [[HAVCR1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HAVCR1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
