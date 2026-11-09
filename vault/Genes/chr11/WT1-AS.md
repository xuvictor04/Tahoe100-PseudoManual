---
symbol: "WT1-AS"
type: "gene"
col: 11383
ensembl_id: "ENSG00000183242"
name: "WT1 antisense RNA"
location: "11p13"
module: 110
arm: "+"
pooled_cpm: 4.41
n_lines_expressing: 14
n_dd_up: 16
n_dd_down: 2
n_dd_up_clean: 5
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 4
direction_downstream: 21
tags: ["gene", "module/110"]
generated_by: "tahoemap"
---

# WT1-AS

*WT1 antisense RNA* — 11p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (11 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.81× (z +15.1, q 0e+00, up in 8 of 9 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM: 0.615× (z -3.6, q 0.088, down in 2 of 12 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 19 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Adagrasib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.229×; ⚠ position not correctable); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (MIA PaCa-2 0.0620×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (MIA PaCa-2 0.0217×); [[Binimetinib (drug)]] 5 µM in 1 line (MIA PaCa-2 0.0321×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WT1]] (+0.74, fdr 7e-06, ⚠ same locus), [[LINC01629]] (+0.64, fdr 1e-05), [[C12orf56]] (+0.56, fdr 1e-05), [[FIBCD1]] (+0.56, fdr 2e-05); moves opposite to [[TOM1]] (-0.39, fdr 4e-04).
> It is in [[Module 110]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[BEGAIN]] → it (grade B ⚠); 21 go from it, the strongest it → [[PLXNA1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 11 with an alert ⚠; shown: the 15 strongest. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11383.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.81×** | +15.1 | 0e+00 | 8/9 (SW480, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.57×** | +12.2 | 1e-31 | 1/4 (PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.16×** | +11.0 | 1e-25 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.61×** | +7.1 | 2e-10 | 1/4 (PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.29×** | +4.7 | 2e-04 | 0/6 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.80×** | +4.7 | 2e-04 | 0/9 | top dose only | cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.18×** | +4.5 | 7e-04 | 0/5 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Fingolimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.72×** | +4.3 | 0.001 | 0/10 | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.71×** | +4.1 | 0.002 | 0/6 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.68×** | +4.0 | 0.004 | 0/8 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.56×** | +3.9 | 0.004 | 0/4 | top dose only | noisy plate (z scaled) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.48×** | +3.8 | 0.007 | 0/5 | rises with dose | noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 0.05 µM |  | **1.53×** | +3.4 | 0.031 | 0/10 | inconsistent across doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.11×** | +3.1 | 0.073 | 1/5 (SW480) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | **1.50×** | +3.1 | 0.079 | 0/9 | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11383.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 19 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Adagrasib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.229×; ⚠ position not correctable); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (MIA PaCa-2 0.0620×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (MIA PaCa-2 0.0217×); [[Binimetinib (drug)]] 5 µM in 1 line (MIA PaCa-2 0.0321×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.615×** | -3.6 | 0.088 | 2/12 (MIA PaCa-2, CHP-212) | inconsistent across doses |  |
| [[Darinaparsin (drug)]] 0.05 µM |  | **0.641×** | -3.6 | 0.088 | 2/11 (SW480, HepG2/C3A) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.899× | -3.3 | 0.20 | 3/12 (MIA PaCa-2, HepG2/C3A, …) | inconsistent across doses |  |
| [[Relugolix (drug)]] 5 µM |  | 0.761× | -3.2 | 0.23 | 1/12 (RPMI-7951) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11383. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 94.5 | 0 | 28 (8 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.229× (z -29.3) ⚠ position not correctable · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0620× (z -22.2) |
| [[HOP62 (line)]] | alt | 11.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0747× (z -11.1) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 7.87 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.122× (z -8.6) |
| [[SW480 (line)]] | alt | 2.09 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.51× (z +8.5) | [[Bendamustine (drug)]] 5 µM 0.0817× (z -8.5) |
| [[PANC-1 (line)]] | alt | 11.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.156× (z -10.7) |
| [[A-172 (line)]] | wt | 1.01 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 2.19 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.484 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.01 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.647 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.491 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.599 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.579 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.537 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.553 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.483 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.630 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.555 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.572 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.14 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.533 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.821 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.526 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.572 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 4.70 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.461 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.489 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.521 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.464 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.504 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.580 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.909 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.473 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.647 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.487 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.506 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.542 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.570 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.632 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.607 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.776 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.526 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.584 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.517 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11383), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WT1]] | +0.74 | +0.76 / +0.66 | both halves | 7e-06 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[LINC01629]] | +0.64 | +0.65 / +0.54 | both halves | 1e-05 | **novel candidate** |
| [[C12orf56]] | +0.56 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[FIBCD1]] | +0.56 | +0.47 / +0.60 | both halves | 2e-05 |  |
| [[ACP7]] | +0.55 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[EDARADD]] | +0.54 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[CYS1]] | +0.54 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[ADAMTS4]] | +0.53 | +0.40 / +0.61 | both halves | 5e-05 |  |
| [[GBX1]] | +0.53 | +0.42 / +0.54 | both halves | 4e-05 |  |
| [[LAMC3]] | +0.53 | +0.55 / +0.37 | both halves | 8e-05 |  |
| [[CORO2B]] | +0.51 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[KCNC4]] | +0.51 | +0.42 / +0.57 | both halves | 4e-05 |  |
| [[TEX10]] | +0.50 | +0.46 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TOM1]] | -0.39 | -0.35 / -0.26 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 1, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BEGAIN]] | B | BEGAIN activity raises WT1-AS's level | lines that do not express BEGAIN (23) vs lines expressing it (27) | 1.56× lower at baseline in the lines without BEGAIN | 0.098 | ⚠ within organs, on part of the lines; also absent: ROR2, CBFA2T3, FXYD6; maybe low, not absent |
| [[WT1]] | C | WT1 activity raises WT1-AS's level | lines that do not express WT1 (29) vs lines expressing it (21) | 2.60× lower at baseline in the lines without WT1 | 0.005 | ⚠ within organs, on part of the lines; also absent: WT1-AS, INA, ZNF677; co-absent with the target |
| [[ELFN1]] | C | ELFN1 activity raises WT1-AS's level | lines that do not express ELFN1 (24) vs lines expressing it (26) | 1.82× lower at baseline in the lines without ELFN1 | 0.009 | ⚠ within organs, on part of the lines; also absent: SORCS2, JAM3, ENSG00000269547; co-absent with the target |
| [[PDZD4]] | C | PDZD4 activity raises WT1-AS's level | lines that do not express PDZD4 (22) vs lines expressing it (28) | 1.85× lower at baseline in the lines without PDZD4 | 0.034 | ⚠ within organs, on part of the lines; also absent: CECR2, CPEB1, COLEC12; co-absent with the target |

### Downstream of this gene

*21 arrows, 21 of them with an alert ⚠; grade A 0, B 10, C 11. Shown: the 12 strongest; 9 more arrows (9 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLXNA1]] | B | WT1-AS activity raises PLXNA1's level | lines that do not express WT1-AS (36) vs lines expressing it (14) | 1.37× lower at baseline in the lines without WT1-AS | 0.017 | ⚠ within organs, on part of the lines; also absent: WT1, ZNF677, GCG |
| [[ZFP69]] | B | WT1-AS activity raises ZFP69's level | lines that do not express WT1-AS (36) vs lines expressing it (14) | 1.61× lower at baseline in the lines without WT1-AS | 0.048 | ⚠ within organs, on part of the lines; also absent: WT1, ZNF677, GCG |
| [[SLC45A1]] | B | WT1-AS activity raises SLC45A1's level | lines that do not express WT1-AS (36) vs lines expressing it (14) | 1.89× lower at baseline in the lines without WT1-AS | 0.060 | ⚠ within organs, on part of the lines; also absent: WT1, ZNF677, GCG |
| [[NKAIN1]] | B | WT1-AS activity raises NKAIN1's level | lines that do not express WT1-AS (36) vs lines expressing it (14) | 1.32× lower at baseline in the lines without WT1-AS | 0.064 | ⚠ within organs, on part of the lines; also absent: WT1, ZNF677, GCG |
| [[LINC01237]] | B | WT1-AS activity raises LINC01237's level | lines that do not express WT1-AS (36) vs lines expressing it (14) | 1.51× lower at baseline in the lines without WT1-AS | 0.067 | ⚠ within organs, on part of the lines; also absent: WT1, ZNF677, GCG |
| [[PRRT3-AS1]] | B | WT1-AS activity strengthens PRRT3-AS1's drug response | lines that do not express WT1-AS (35) vs lines expressing it (12) | the lines without WT1-AS respond 0.70× as strongly (z diff +0.73); strongest at Harringtonine 5 µM: 0.60x vs 0.27x (z diff +3.3) | 0.069 | ⚠ within organs, on part of the lines; also absent: WT1, ZNF677, GCG; target measured in part of the lines; artifact flags |
| [[LINC01237]] | B | WT1-AS activity strengthens LINC01237's drug response | lines that do not express WT1-AS (30) vs lines expressing it (10) | the lines without WT1-AS respond 0.63× as strongly (z diff +1.92); strongest at Homoharringtonine 5 µM: 0.50x vs 0.18x (z diff +4.9) | 0.070 | ⚠ within organs, on part of the lines; also absent: WT1, ZNF677, GCG; target measured in part of the lines; artifact flags |
| [[BOLA3-DT]] | B | WT1-AS activity raises BOLA3-DT's level | lines that do not express WT1-AS (36) vs lines expressing it (14) | 1.62× lower at baseline in the lines without WT1-AS | 0.071 | ⚠ within organs, on part of the lines; also absent: WT1, ZNF677, GCG |
| [[USP2-AS1]] | B | WT1-AS activity raises USP2-AS1's level | lines that do not express WT1-AS (36) vs lines expressing it (14) | 1.50× lower at baseline in the lines without WT1-AS | 0.074 | ⚠ within organs, on part of the lines; also absent: WT1, ZNF677, GCG |
| [[VASH1]] | B | WT1-AS activity raises VASH1's level | lines that do not express WT1-AS (36) vs lines expressing it (14) | 1.84× lower at baseline in the lines without WT1-AS | 0.081 | ⚠ within organs, on part of the lines; also absent: WT1, ZNF677, GCG |
| [[WT1]] | C | WT1-AS activity raises WT1's level | lines that do not express WT1-AS (36) vs lines expressing it (14) | 6.02× lower at baseline in the lines without WT1-AS | 5e-05 | ⚠ within organs, on part of the lines; also absent: WT1, ZNF677, GCG; co-absent with the target |
| [[CYS1]] | C | WT1-AS activity raises CYS1's level | lines that do not express WT1-AS (36) vs lines expressing it (14) | 1.91× lower at baseline in the lines without WT1-AS | 0.006 | ⚠ within organs, on part of the lines; also absent: WT1, ZNF677, GCG; co-absent with the target |

## Where it sits

- **Module**: [[Module 110]]; 43 genes; every member is in the + arm (projection on the module's main direction 0.615). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (52.6, 4.2); signed map (7.3, 55.2). **Vector** length 37.5, 10.5% of its response variance represented; |z| ≥ 3 in 351 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.9 | +15.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.6 | +7.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.4 | +11.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.8 | +12.2 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | +1.5 | +3.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.5 | +2.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +0.8 | +2.2 |
|  | [[vincristine (drug)]] 0.5 µM |  | +0.7 | +2.4 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +0.7 | +1.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +0.7 | +0.5 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | -1.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -1.4 | -2.3 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.2 | -1.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.2 | -1.6 |
|  | [[Trametinib (drug)]] 5 µM |  | -1.1 | -2.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.0 | -1.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.0 | -3.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | -0.9 | +0.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -0.9 | -1.6 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -0.9 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | WT1 antisense RNA |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 11p13 — chr11:32,435,518-32,500,632 (+) |
| Ensembl biotype | lncRNA |
| Also known as | WIT-1, WT1AS, WT1-AS1; previously WIT1 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

UniProt [Q06250](https://www.uniprot.org/uniprotkb/Q06250) carries no function annotation.

**Summary**, from NCBI Gene [51352](https://www.ncbi.nlm.nih.gov/gene/51352):

> This gene is located upstream of the Wilms tumor 1 (WT1) gene; these two genes are bi-directionally transcribed from the same promoter region. This gene is imprinted in kidney, with preferential expression from the paternal allele. Imprinting defects at chromosome 11p13 may contribute to tumorigenesis. [provided by RefSeq, May 2014]

**Accessions** — [HGNC:18135](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18135) · Entrez [51352](https://www.ncbi.nlm.nih.gov/gene/51352) · UniProt [Q06250](https://www.uniprot.org/uniprotkb/Q06250) · Ensembl [ENSG00000183242](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183242)

## Data

Gene col 11383: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11383); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11383, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11383]; `tensor/DDL_lfc|DDL_z.npy` [11383]; `embed/gene_vectors.npy` [11383]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11383 or target_col == 11383). Every well: [[WT1-AS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WT1-AS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
