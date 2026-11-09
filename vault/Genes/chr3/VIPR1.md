---
symbol: "VIPR1"
type: "gene"
col: 3592
ensembl_id: "ENSG00000114812"
name: "vasoactive intestinal peptide receptor 1"
location: "3p22.1"
module: 44
arm: "+"
pooled_cpm: 4.26
n_lines_expressing: 26
n_dd_up: 23
n_dd_down: 2
n_dd_up_clean: 15
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 24
direction_downstream: 52
tags: ["gene", "module/044"]
generated_by: "tahoemap"
---

# VIPR1

*vasoactive intestinal peptide receptor 1* — 3p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.72× (z +11.5, q 5e-28, up in 1 of 6 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 2.71× (z +9.2, q 7e-18, up in 15 of 22 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.581× (z -5.0, q 4e-04, down in 14 of 22 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Bortezomib (drug)]] 0.05 µM in 1 line (SNU-1 0.0305×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (LoVo 0.158×); [[Digitoxin (drug)]] 5 µM in 1 line (SNU-1 0.0423×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (SNU-1 0.109×); [[Selinexor (drug)]] 5 µM in 1 line (SNU-1 0.128×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PRR15L]] (+0.75, fdr 7e-06), [[FGFR2]] (+0.75, fdr 1e-05), [[TJP3]] (+0.72, fdr 7e-06); moves opposite to [[MAP3K20]] (-0.53, fdr 2e-05), [[ANKRD7]] (-0.50, fdr 8e-05), [[BVES-AS1]] (-0.49, fdr 5e-04).
> It is in [[Module 044]], a single-armed module (Defective GALNT12 causes CRCS1).
> Probable direction (from the cell lines, not proof of direct regulation): 24 arrows point to it, the strongest [[ATP8B1]] → it (grade B ⚠); 52 go from it, the strongest it → [[BICDL2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3592.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.72×** | +11.5 | 5e-28 | 1/6 (CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.91×** | +9.8 | 3e-20 | 5/14 (RPMI-7951, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.04×** | +9.4 | 7e-19 | 1/9 (SW1417) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.71×** | +9.2 | 7e-18 | 15/22 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.22×** | +7.3 | 3e-11 | 12/22 (SW1417, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.63×** | +6.3 | 2e-08 | 8/21 (SW480, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.84×** | +5.6 | 2e-06 | 7/22 (SW1417, LS 180, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.44×** | +4.7 | 2e-04 | 3/18 (RPMI-7951, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.62×** | +4.4 | 5e-04 | 2/20 (SW480, HOP62) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.41×** | +4.4 | 5e-04 | 3/22 (LS 180, HEC-1-A, …) | rises with dose |  |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.86×** | +4.1 | 0.002 | 1/18 (LoVo) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.53×** | +3.9 | 0.004 | 1/20 (HEC-1-A) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.47×** | +3.5 | 0.018 | 5/22 (LS 180, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.06×** | +3.5 | 0.021 | 0/9 | top dose only | noisy plate (z scaled) |
| [[18β-Glycyrrhetinic acid (drug)]] 5 µM |  | **1.31×** | +3.5 | 0.021 | 1/22 (SW480) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.30×** | +3.4 | 0.022 | 6/22 (KATO III, SW480, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~15% here) |
| [[5-Azacytidine (drug)]] 0.5 µM |  | **1.40×** | +3.1 | 0.063 | 0/21 | inconsistent across doses |  |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | **1.42×** | +3.0 | 0.082 | 0/16 | inconsistent across doses |  |
| [[Gemcitabine (drug)]] 0.5 µM |  | **1.37×** | +2.9 | 0.082 | 3/22 (LoVo, Panc 03.27, …) | all doses, flat | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.25×** | +2.9 | 0.082 | 0/22 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3592.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Bortezomib (drug)]] 0.05 µM in 1 line (SNU-1 0.0305×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (LoVo 0.158×); [[Digitoxin (drug)]] 5 µM in 1 line (SNU-1 0.0423×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (SNU-1 0.109×); [[Selinexor (drug)]] 5 µM in 1 line (SNU-1 0.128×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.581×** | -5.0 | 4e-04 | 14/22 (LoVo, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.639×** | -4.1 | 0.011 | 9/22 (HT-29, LoVo, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.687× | -3.5 | 0.10 | 10/22 (SNU-1, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | 0.702× | -3.2 | 0.13 | 11/21 (SW480, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.905× | -3.2 | 0.13 | 4/22 (HOP62, RPMI-7951, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | 0.709× | -3.2 | 0.13 | 4/22 (SNU-1, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.787× | -3.1 | 0.13 | 10/22 (HT-29, BT-474, …) | top dose only |  |
| [[Mebendazole (drug)]] 5 µM |  | 0.704× | -3.1 | 0.13 | 3/22 (NCI-H1573, LoVo, …) | top dose only | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | 0.716× | -3.1 | 0.13 | 11/21 (SNU-1, SW48, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3592. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-1 (line)]] | wt | 43.5 | 0 | 5 (3 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.0305× (z -10.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.109× (z -10.0) |
| [[KATO III (line)]] | alt | 5.22 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0853× (z -9.1) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 21.7 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.158× (z -10.3) |
| [[SW480 (line)]] | alt | 4.90 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.169× (z -8.5) |
| [[A-172 (line)]] | wt | 0.395 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.17 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.308 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.491 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.695 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.36 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.489 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.385 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.15 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.05 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.397 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 5.84 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.790 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.57 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.418 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.506 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.675 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.481 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.64 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.294 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.673 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.834 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 4.59 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.816 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 4.73 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.453 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.693 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 9.12 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.355 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.984 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 7.19 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.381 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.698 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.762 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.65 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3592), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRR15L]] | +0.75 | +0.63 / +0.80 | both halves | 7e-06 |  |
| [[FGFR2]] | +0.75 | +0.49 / +0.75 | both halves | 1e-05 | **novel candidate** |
| [[TJP3]] | +0.72 | +0.62 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[CYP4F12]] | +0.67 | +0.52 / +0.76 | both halves | 1e-05 |  |
| [[PRR15]] | +0.67 | +0.54 / +0.72 | both halves | 1e-05 |  |
| [[CFTR]] | +0.66 | +0.48 / +0.76 | both halves | 2e-05 |  |
| [[LINC01814]] | +0.65 | +0.57 / +0.62 | both halves | 8e-06 |  |
| [[LINC02331]] | +0.65 | +0.47 / +0.65 | both halves | 2e-05 |  |
| [[PRR15-DT]] | +0.64 | +0.57 / +0.64 | both halves | 8e-06 |  |
| [[CLDN3]] | +0.64 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[PLEKHG6]] | +0.64 | +0.42 / +0.72 | both halves | 4e-05 |  |
| [[LINC00299]] | +0.64 | +0.60 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAP3K20]] | -0.53 | -0.46 / -0.47 | both halves | 2e-05 |  |
| [[ANKRD7]] | -0.50 | -0.39 / -0.37 | both halves | 8e-05 |  |
| [[BVES-AS1]] | -0.49 | -0.46 / -0.24 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*24 arrows, 24 of them with an alert ⚠; grade A 0, B 2, C 22. Shown: the 12 strongest; 12 more arrows (12 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ATP8B1]] | B | ATP8B1 activity raises VIPR1's level | lines that do not express ATP8B1 (14) vs lines expressing it (36) | 2.15× lower at baseline in the lines without ATP8B1 | 0.011 | ⚠ within organs, on part of the lines; also absent: LGALS9, CDA, KRT86 |
| [[BICDL2]] | B | BICDL2 activity raises VIPR1's level | lines that do not express BICDL2 (22) vs lines expressing it (28) | 1.99× lower at baseline in the lines without BICDL2 | 0.067 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CRYBG2, MAL2, TNNT2; maybe low, not absent |
| [[CLIC5]] | C | CLIC5 activity raises VIPR1's level | lines that do not express CLIC5 (37) vs lines expressing it (13) | 3.19× lower at baseline in the lines without CLIC5 | 0.002 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, KLK11, CLRN3; co-absent with the target |
| [[PRKCH-AS1]] | C | PRKCH-AS1 activity raises VIPR1's level | lines that do not express PRKCH-AS1 (34) vs lines expressing it (16) | 3.04× lower at baseline in the lines without PRKCH-AS1 | 0.006 | ⚠ within organs, on part of the lines; also absent: SLC5A1, TMEM30B, TMPRSS2; maybe low, not absent; co-absent with the target |
| [[LINC02331]] | C | LINC02331 activity raises VIPR1's level | lines that do not express LINC02331 (30) vs lines expressing it (20) | 3.33× lower at baseline in the lines without LINC02331 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KDF1, EPS8L3, LCN2; co-absent with the target |
| [[ALOX5]] | C | ALOX5 activity raises VIPR1's level | lines that do not express ALOX5 (28) vs lines expressing it (22) | 2.50× lower at baseline in the lines without ALOX5 | 0.011 | ⚠ within organs, on part of the lines; also absent: PDZK1IP1, ADGRF1, RASSF6; co-absent with the target |
| [[TMPRSS2]] | C | TMPRSS2 activity raises VIPR1's level | lines that do not express TMPRSS2 (35) vs lines expressing it (15) | 3.40× lower at baseline in the lines without TMPRSS2 | 0.014 | ⚠ within organs, on part of the lines; also absent: SLC5A1, ARHGEF38, ITGB6; co-absent with the target |
| [[HSD17B2]] | C | HSD17B2 activity raises VIPR1's level | lines that do not express HSD17B2 (35) vs lines expressing it (15) | 2.78× lower at baseline in the lines without HSD17B2 | 0.016 | ⚠ within organs, on part of the lines; also absent: KRT23, S100P, TFF2; co-absent with the target |
| [[TMEM125]] | C | TMEM125 activity raises VIPR1's level | lines that do not express TMEM125 (33) vs lines expressing it (17) | 3.43× lower at baseline in the lines without TMEM125 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, ATP2C2, ST14; co-absent with the target |
| [[PLEKHG6]] | C | PLEKHG6 activity raises VIPR1's level | lines that do not express PLEKHG6 (26) vs lines expressing it (24) | 2.44× lower at baseline in the lines without PLEKHG6 | 0.026 | ⚠ within organs, on part of the lines; also absent: SCNN1A, KDF1, RNF39; maybe low, not absent; co-absent with the target |
| [[BMP4]] | C | BMP4 activity raises VIPR1's level | lines that do not express BMP4 (31) vs lines expressing it (19) | 2.90× lower at baseline in the lines without BMP4 | 0.028 | ⚠ within organs, on part of the lines; also absent: TRIM15, ENSG00000287426, TMEM45B; co-absent with the target |
| [[ARHGEF38]] | C | ARHGEF38 activity raises VIPR1's level | lines that do not express ARHGEF38 (36) vs lines expressing it (14) | 3.41× lower at baseline in the lines without ARHGEF38 | 0.030 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, TMEM125, SLC5A1; co-absent with the target |

### Downstream of this gene

*52 arrows, 52 of them with an alert ⚠; grade A 0, B 17, C 35. Shown: the 12 strongest; 40 more arrows (40 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BICDL2]] | B | VIPR1 activity raises BICDL2's level | lines that do not express VIPR1 (24) vs lines expressing it (26) | 3.29× lower at baseline in the lines without VIPR1 | 0.007 | ⚠ within organs, on part of the lines; also absent: ESRP1, IRF6, ENSG00000262302 |
| [[FUT2]] | B | VIPR1 activity raises FUT2's level | lines that do not express VIPR1 (24) vs lines expressing it (26) | 2.10× lower at baseline in the lines without VIPR1 | 0.008 | ⚠ within organs, on part of the lines; also absent: ESRP1, IRF6, ENSG00000262302 |
| [[ABHD11]] | B | VIPR1 activity raises ABHD11's level | lines that do not express VIPR1 (24) vs lines expressing it (26) | 2.28× lower at baseline in the lines without VIPR1 | 0.015 | ⚠ within organs, on part of the lines; also absent: ESRP1, IRF6, ENSG00000262302 |
| [[ATP8B1]] | B | VIPR1 activity raises ATP8B1's level | lines that do not express VIPR1 (24) vs lines expressing it (26) | 2.61× lower at baseline in the lines without VIPR1 | 0.027 | ⚠ within organs, on part of the lines; also absent: ESRP1, IRF6, ENSG00000262302 |
| [[DTX4]] | B | VIPR1 activity raises DTX4's level | lines that do not express VIPR1 (24) vs lines expressing it (26) | 1.88× lower at baseline in the lines without VIPR1 | 0.031 | ⚠ within organs, on part of the lines; also absent: ESRP1, IRF6, ENSG00000262302 |
| [[MROH7]] | B | VIPR1 activity raises MROH7's level | lines that do not express VIPR1 (24) vs lines expressing it (26) | 2.37× lower at baseline in the lines without VIPR1 | 0.036 | ⚠ within organs, on part of the lines; also absent: ESRP1, IRF6, ENSG00000262302 |
| [[MPP7]] | B | VIPR1 activity raises MPP7's level | lines that do not express VIPR1 (24) vs lines expressing it (26) | 2.49× lower at baseline in the lines without VIPR1 | 0.037 | ⚠ within organs, on part of the lines; also absent: ESRP1, IRF6, ENSG00000262302 |
| [[ELF3-AS1]] | B | VIPR1 activity raises ELF3-AS1's level | lines that do not express VIPR1 (24) vs lines expressing it (26) | 2.45× lower at baseline in the lines without VIPR1 | 0.052 | ⚠ within organs, on part of the lines; also absent: ESRP1, IRF6, ENSG00000262302 |
| cells under [[Afatinib (drug)]] 0.5 µM | B | VIPR1 activity lowers the cells' numbers under Afatinib 0.5 µM (makes them more sensitive) | lines that do not express VIPR1 (24) vs lines expressing it (24) | the lines without VIPR1: 1.14× the cells of the other lines | 0.058 | ⚠ within organs, on part of the lines; also absent: ESRP1, IRF6, ENSG00000262302 |
| cells under [[Omeprazole (drug)]] 5 µM | B | VIPR1 activity lowers the cells' numbers under Omeprazole 5 µM (makes them more sensitive) | lines that do not express VIPR1 (24) vs lines expressing it (24) | the lines without VIPR1: 1.17× the cells of the other lines | 0.069 | ⚠ within organs, on part of the lines; also absent: ESRP1, IRF6, ENSG00000262302 |
| cells under [[Docetaxel (Trihydrate) (drug)]] 5 µM | B | VIPR1 activity raises the cells' numbers under Docetaxel (Trihydrate) 5 µM (protects the cells) | lines that do not express VIPR1 (24) vs lines expressing it (24) | the lines without VIPR1: 0.80× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: ESRP1, IRF6, ENSG00000262302 |
| cells under [[Berbamine (dihydrochloride) (drug)]] 0.5 µM | B | VIPR1 activity lowers the cells' numbers under Berbamine (dihydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express VIPR1 (24) vs lines expressing it (24) | the lines without VIPR1: 1.17× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: ESRP1, IRF6, ENSG00000262302 |

## Where it sits

- **Module**: [[Module 044]] — Defective GALNT12 causes CRCS1; 102 genes; every member is in the + arm (projection on the module's main direction 0.707). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (22.8, 52.3); signed map (62.7, 5.5). **Vector** length 44.7, 9.03% of its response variance represented; |z| ≥ 3 in 552 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Defective GALNT12 causes CRCS1* (reactome, mean cos +0.52 to 5); *Defective GALNT3 causes HFTC* (reactome, mean cos +0.52 to 5); *Defective C1GALT1C1 causes TNPS* (reactome, mean cos +0.52 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +1.9 | +6.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | +0.9 | +9.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +0.9 | -0.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +0.8 | +9.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +0.7 | +11.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +0.6 | +4.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +0.6 | +1.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.6 | +1.3 |
|  | [[crizotinib (drug)]] 5 µM |  | +0.6 | +0.4 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +0.6 | +1.8 |
| fall | [[Auranofin (drug)]] 5 µM |  | -1.5 | -2.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.5 | -2.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.5 | -4.1 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | -1.3 | -1.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -1.2 | -5.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.1 | -1.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.1 | -2.0 |
|  | [[EX229 (drug)]] 5 µM |  | -1.0 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | vasoactive intestinal peptide receptor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p22.1 — chr3:42,489,299-42,537,573 (+) |
| Ensembl biotype | protein_coding |
| Also known as | VPAC1, RDC1, HVR1, VPAC1R |
| Gene groups (HGNC) | Vasoactive intestinal peptide family receptors |
| Hallmark sets | MYOGENESIS |
| Reactome | 6 pathways, smallest: Glucagon-type ligand receptors; Class B/2 (Secretin family receptors); G alpha (s) signalling events |
| Matched by | ensembl_id |

**Function**, from UniProt [P32241](https://www.uniprot.org/uniprotkb/P32241) (Vasoactive intestinal polypeptide receptor 1):

> G protein-coupled receptor activated by the neuropeptides vasoactive intestinal peptide (VIP) and pituitary adenylate cyclase-activating polypeptide (ADCYAP1/PACAP). Binds VIP and both PACAP27 and PACAP38 bioactive peptides with the following order of ligand affinity VIP = PACAP27 > PACAP38. Ligand binding causes a conformation change that triggers signaling via guanine nucleotide-binding proteins (G proteins) and modulates the activity of downstream effectors. Activates cAMP-dependent pathway.

**Summary**, from NCBI Gene [7433](https://www.ncbi.nlm.nih.gov/gene/7433):

> This gene encodes a receptor for vasoactive intestinal peptide, a small neuropeptide. Vasoactive intestinal peptide is involved in smooth muscle relaxation, exocrine and endocrine secretion, and water and ion flux in lung and intestinal epithelia. Its actions are effected through integral membrane receptors associated with a guanine nucleotide binding protein which activates adenylate cyclase. Several transcript variants encoding different isoforms have been found for this gene. [provided by …

**Accessions** — [HGNC:12694](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12694) · Entrez [7433](https://www.ncbi.nlm.nih.gov/gene/7433) · UniProt [P32241](https://www.uniprot.org/uniprotkb/P32241) · Ensembl [ENSG00000114812](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000114812)

## Data

Gene col 3592: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3592); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3592, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3592]; `tensor/DDL_lfc|DDL_z.npy` [3592]; `embed/gene_vectors.npy` [3592]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3592 or target_col == 3592). Every well: [[VIPR1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VIPR1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
