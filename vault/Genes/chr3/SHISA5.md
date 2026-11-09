---
symbol: "SHISA5"
type: "gene"
col: 8848
ensembl_id: "ENSG00000164054"
name: "shisa family member 5"
location: "3p21.31"
module: 32
arm: "+"
pooled_cpm: 56.52
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 37
n_dd_up_clean: 0
n_dd_down_clean: 32
in_vector_space: true
direction_upstream: 18
direction_downstream: 0
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# SHISA5

*shisa family member 5* — 3p21.31

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (HS-578T 2.78×, HOP62 2.80×); [[Dinaciclib (drug)]] 0.05 µM in 1 line (A-427 3.23×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (SW480 3.69×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 37 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.525× (z -11.9, q 1e-29, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FBXO39]] (+0.75, fdr 7e-06), [[IRF9]] (+0.74, fdr 7e-06), [[HELZ2]] (+0.73, fdr 7e-06).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 18 arrows point to it, the strongest [[SRMS]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

No drug-dose raises it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (HS-578T 2.78×, HOP62 2.80×); [[Dinaciclib (drug)]] 0.05 µM in 1 line (A-427 3.23×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (SW480 3.69×; ⚠ toxic; transcription drop).

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 5 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 37 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8848.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.525×** | -11.9 | 1e-29 | 40/48 (BT-474, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.447×** | -10.5 | 3e-23 | 44/48 (LoVo, RKO, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.457×** | -10.2 | 5e-22 | 45/48 (NCI-H23, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.470×** | -9.8 | 1e-20 | 43/48 (NCI-H23, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.618×** | -8.9 | 1e-16 | 38/48 (RPMI-7951, HS-578T, …) | top dose only | cell-cycle shift (explains ~4% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.514×** | -8.6 | 5e-16 | 43/48 (RPMI-7951, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.544×** | -7.5 | 6e-12 | 43/48 (MIA PaCa-2, AN3 CA, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.568×** | -7.1 | 1e-10 | 37/47 (H4, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.370×** | -6.8 | 8e-10 | 38/49 (KATO III, BT-474, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.597×** | -6.7 | 1e-09 | 39/48 (MIA PaCa-2, Panc 03.27, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.705×** | -6.4 | 7e-09 | 33/48 (COLO 205, RPMI-7951, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.616×** | -6.3 | 1e-08 | 35/48 (NCI-H1573, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.431×** | -5.7 | 4e-07 | 34/48 (A-427, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.654×** | -5.5 | 1e-06 | 35/48 (RKO, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Tofacitinib (drug)]] 5 µM |  | **0.742×** | -5.5 | 2e-06 | 33/48 (NCI-H2347, MIA PaCa-2, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.682×** | -5.0 | 2e-05 | 37/48 (SNU-423, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~2% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8848. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 64.2 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -16.2) |
| [[RKO (line)]] | wt | 68.6 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -13.7) |
| [[BT-474 (line)]] | alt | 65.3 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.138× (z -20.7) |
| [[A-427 (line)]] | wt | 47.5 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.05 µM 3.23× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | [[PH-797804 (drug)]] 5 µM 0.131× (z -10.4) |
| [[RPMI-7951 (line)]] | alt | 177 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.306× (z -13.9) |
| [[SNU-423 (line)]] | alt | 80.3 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.416× (z -10.4) |
| [[H4 (line)]] | wt | 57.8 | 0 | 3 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0977× (z -11.9) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.147× (z -10.1) |
| [[KATO III (line)]] | alt | 65.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.308× (z -12.8) |
| [[LoVo (line)]] | wt | 50.7 | 0 | 3 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.237× (z -12.2) |
| [[LOX-IMVI (line)]] | wt | 45.4 | 0 | 3 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.246× (z -11.6) |
| [[NCI-H23 (line)]] | alt | 53.3 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.224× (z -12.2) |
| [[C-33 A (line)]] | alt | 70.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.325× (z -10.8) |
| [[CHP-212 (line)]] | wt | 71.6 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.222× (z -10.4) |
| [[COLO 205 (line)]] | alt | 41.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -9.6) |
| [[HEC-1-A (line)]] | alt | 99.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.293× (z -16.1) |
| [[HS-578T (line)]] | alt | 84.7 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +12.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.404× (z -10.8) |
| [[HT-29 (line)]] | alt | 31.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -13.2) |
| [[NCI-H1573 (line)]] | alt | 42.8 | 0 | 2 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0322× (z -13.0) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.339× (z -11.0) |
| [[NCI-H1792 (line)]] | alt | 67.7 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.403× (z -9.2) |
| [[SW480 (line)]] | alt | 26.3 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.69× (z +9.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.382× (z -10.3) |
| [[A-172 (line)]] | wt | 55.1 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.413× (z -8.7) |
| [[A498 (line)]] | wt | 38.5 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.366× (z -9.5) |
| [[A549 (line)]] | wt | 45.2 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.346× (z -8.5) |
| [[HepG2_C3A (line)]] | wt | 65.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.160× (z -9.8) ⚠ toxic |
| [[HOP62 (line)]] | alt | 63.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +9.1) | — |
| [[Hs 766T (line)]] | wt | 81.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.436× (z -10.1) |
| [[J82 (line)]] | alt | 61.4 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.142× (z -8.8) ⚠ toxic |
| [[NCI-H2030 (line)]] | alt | 47.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.421× (z -10.8) |
| [[NCI-H2347 (line)]] | alt | 86.1 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.310× (z -10.0) |
| [[NCI-H661 (line)]] | alt | 42.2 | 0 | 1 | — | [[Citalopram (hydrobromide) (drug)]] 0.5 µM 0.0918× (z -8.6) |
| [[Panc 03.27 (line)]] | alt | 66.0 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.316× (z -8.9) |
| [[PANC-1 (line)]] | alt | 34.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.554× (z -8.5) |
| [[SW 900 (line)]] | alt | 42.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.366× (z -9.0) |
| [[SW1417 (line)]] | alt | 67.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.421× (z -10.0) |
| [[AN3 CA (line)]] | alt | 54.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 42.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 87.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 60.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 70.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 59.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 34.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 44.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 32.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 51.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 83.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 54.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 91.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 34.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8848), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBXO39]] | +0.75 | +0.60 / +0.78 | both halves | 7e-06 |  |
| [[IRF9]] | +0.74 | +0.65 / +0.76 | both halves | 7e-06 |  |
| [[HELZ2]] | +0.73 | +0.69 / +0.73 | both halves | 7e-06 |  |
| [[SP100]] | +0.73 | +0.60 / +0.75 | both halves | 7e-06 |  |
| [[STAT1]] | +0.72 | +0.64 / +0.71 | both halves | 7e-06 |  |
| [[RIGI]] | +0.72 | +0.61 / +0.74 | both halves | 7e-06 |  |
| [[OAS3]] | +0.72 | +0.66 / +0.72 | both halves | 7e-06 |  |
| [[OAS2]] | +0.71 | +0.60 / +0.75 | both halves | 7e-06 |  |
| [[MX2]] | +0.70 | +0.58 / +0.75 | both halves | 7e-06 |  |
| [[PLSCR1]] | +0.70 | +0.59 / +0.71 | both halves | 7e-06 |  |
| [[MX1]] | +0.70 | +0.58 / +0.73 | both halves | 8e-06 |  |
| [[SP110]] | +0.69 | +0.56 / +0.73 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 10, C 8. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SRMS]] | B | SRMS activity strengthens SHISA5's drug response | lines that do not express SRMS (14) vs lines expressing it (35) | the lines without SRMS respond 0.64× as strongly (z diff +1.65); strongest at Homoharringtonine 5 µM: 0.67x vs 0.49x (z diff +2.7) | 0.033 | ⚠ within organs, on part of the lines; also absent: MX1, OAS2, RSAD2; target measured in part of the lines; artifact flags |
| [[IFITM1]] | B | IFITM1 activity raises SHISA5's level | lines that do not express IFITM1 (19) vs lines expressing it (31) | 1.30× lower at baseline in the lines without IFITM1 | 0.041 | ⚠ within organs, on part of the lines; also absent: TRIM22, IFI6, SLC15A3 |
| [[MX1]] | B | MX1 activity raises SHISA5's level | lines that do not express MX1 (19) vs lines expressing it (31) | 1.29× lower at baseline in the lines without MX1 | 0.046 | ⚠ within organs, on part of the lines; also absent: OAS2, SRMS, EPSTI1 |
| [[IFI44L]] | B | IFI44L activity raises SHISA5's level | lines that do not express IFI44L (22) vs lines expressing it (28) | 1.33× lower at baseline in the lines without IFI44L | 0.048 | ⚠ within organs, on part of the lines; also absent: GBP1, EPSTI1, GBP4 |
| [[IFI6]] | B | IFI6 activity raises SHISA5's level | lines that do not express IFI6 (13) vs lines expressing it (37) | 1.38× lower at baseline in the lines without IFI6 | 0.055 | ⚠ within organs, on part of the lines; also absent: RASGRP3, MX1, IFITM1; maybe low, not absent |
| [[TRIM22]] | B | TRIM22 activity raises SHISA5's level | lines that do not express TRIM22 (18) vs lines expressing it (32) | 1.32× lower at baseline in the lines without TRIM22 | 0.055 | ⚠ within organs, on part of the lines; also absent: CD5L, XAF1, IFITM1 |
| [[PARP9]] | B | PARP9 activity strengthens SHISA5's drug response | lines that do not express PARP9 (7) vs lines expressing it (42) | the lines without PARP9 respond 0.64× as strongly (z diff +1.67); strongest at Panobinostat 5 µM: 0.67x vs 0.43x (z diff +3.5) | 0.065 | ⚠ within organs, on part of the lines; also absent: PLSCR1, OAS3, SRMS; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[IFI6]] | B | IFI6 activity strengthens SHISA5's drug response | lines that do not express IFI6 (13) vs lines expressing it (36) | the lines without IFI6 respond 0.67× as strongly (z diff +1.56); strongest at Panobinostat 5 µM: 0.63x vs 0.41x (z diff +3.2) | 0.081 | ⚠ within organs, on part of the lines; also absent: RASGRP3, MX1, IFITM1; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[SP110]] | B | SP110 activity strengthens SHISA5's drug response | lines that do not express SP110 (5) vs lines expressing it (44) | the lines without SP110 respond 0.52× as strongly (z diff +2.32); strongest at Panobinostat 5 µM: 0.75x vs 0.44x (z diff +4.4) | 0.092 | ⚠ within organs, on part of the lines; also absent: IFIT1; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[SLC15A3]] | B | SLC15A3 activity raises SHISA5's level | lines that do not express SLC15A3 (16) vs lines expressing it (34) | 1.35× lower at baseline in the lines without SLC15A3 | 0.094 | ⚠ within organs, on part of the lines; also absent: XAF1, MX2, GBP4 |
| [[HELZ2]] | C | HELZ2's natural level strengthens SHISA5's drug response | HELZ2's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.74, reverse +0.33; direction not clear | 0.002 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[REC8]] | C | REC8's natural level strengthens SHISA5's drug response | REC8's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.73, reverse +0.36; direction not clear | 0.004 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.700). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (49.6, 53.2); signed map (65.9, 30.8). **Vector** length 101, 29.9% of its response variance represented; |z| ≥ 3 in 1,173 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon alpha response* (hallmark, mean cos +0.58 to 56); *interferon gamma response* (hallmark, mean cos +0.59 to 60); *interferon* (control, mean cos +0.67 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.4 | +2.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.3 | -2.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +4.9 | -2.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.7 | -11.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.4 | +1.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.4 | +0.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.3 | +1.0 |
|  | [[Omeprazole (drug)]] 0.05 µM |  | +2.3 | +2.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +1.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.2 | -0.4 |
| fall | [[Ponatinib (drug)]] 5 µM |  | -5.5 | -4.9 |
|  | [[Selinexor (drug)]] 5 µM |  | -5.3 | -6.4 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -5.3 | -5.5 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -4.5 | -3.5 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -4.4 | -7.5 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -4.0 | -3.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.8 | -4.0 |

## What is on record

|  |  |
|---|---|
| Name | shisa family member 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.31 — chr3:48,467,798-48,504,826 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SCOTIN, hShisa5 |
| Gene groups (HGNC) | Shisa family members |
| Reactome | 2 pathways, smallest: Post-translational protein phosphorylation; Regulation of Insulin-like Growth Factor (IGF) transport and uptake by Insulin-like Growth Factor Binding Proteins (IGFBPs) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N114](https://www.uniprot.org/uniprotkb/Q8N114) (Protein shisa-5):

> Can induce apoptosis in a caspase-dependent manner and plays a role in p53/TP53-dependent apoptosis.

**Summary**, from NCBI Gene [51246](https://www.ncbi.nlm.nih.gov/gene/51246):

> This gene encodes a member of the shisa family. The encoded protein is localized to the endoplasmic reticulum, and together with p53 induces apoptosis in a caspase-dependent manner. Alternative splicing results in multiple transcript variants. Related pseudogenes of this gene are found on chromosome X. [provided by RefSeq, Apr 2016]

**Accessions** — [HGNC:30376](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30376) · Entrez [51246](https://www.ncbi.nlm.nih.gov/gene/51246) · UniProt [Q8N114](https://www.uniprot.org/uniprotkb/Q8N114) · Ensembl [ENSG00000164054](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164054)

## Data

Gene col 8848: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8848); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8848, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8848]; `tensor/DDL_lfc|DDL_z.npy` [8848]; `embed/gene_vectors.npy` [8848]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8848 or target_col == 8848). Every well: [[SHISA5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SHISA5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
