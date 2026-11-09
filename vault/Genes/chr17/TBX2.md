---
symbol: "TBX2"
type: "gene"
col: 4252
ensembl_id: "ENSG00000121068"
name: "T-box transcription factor 2"
location: "17q23.2"
module: 19
arm: "+"
pooled_cpm: 9.22
n_lines_expressing: 31
n_dd_up: 19
n_dd_down: 3
n_dd_up_clean: 10
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# TBX2

*T-box transcription factor 2* — 17q23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.62× (z +11.5, q 7e-28, up in 19 of 25 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.635× (z -3.9, q 0.051, down in 14 of 27 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 4 lines (NCI-H460 0.0911×, CHP-212 0.121×, hTERT-HPNE 0.138×, AN3 CA 0.202×); [[Panobinostat (drug)]] 5 µM in 4 lines (NCI-H460 0.104×, CHP-212 0.133×, hTERT-HPNE 0.0780×, AN3 CA 0.165×; ⚠ cell-cycle shift, explains ~6% of this change); [[Belinostat (drug)]] 5 µM in 3 lines (NCI-H460 0.0898×, CHP-212 0.251×, hTERT-HPNE 0.163×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (CHP-212 0.298×, AN3 CA 0.270×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SEMA4C]] (+0.63, fdr 9e-06), [[HOXB2]] (+0.60, fdr 1e-05), [[HOXC9]] (+0.58, fdr 3e-05); moves opposite to [[JPT2]] (-0.49, fdr 1e-04), [[ANXA2]] (-0.47, fdr 6e-05), [[RHOA]] (-0.47, fdr 1e-04).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[GREM2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 9 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4252.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.62×** | +11.5 | 7e-28 | 19/25 (PANC-1, A549, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.43×** | +7.2 | 2e-10 | 13/23 (PANC-1, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.72×** | +6.4 | 2e-08 | 21/28 (PANC-1, RPMI-7951, …) | all doses, flat | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.05 µM |  | **2.05×** | +6.0 | 2e-07 | 19/28 (PANC-1, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **2.06×** | +5.9 | 5e-07 | 17/27 (RPMI-7951, C32, …) | top dose only | composition shift |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.96×** | +5.7 | 1e-06 | 18/27 (PANC-1, SW480, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.61×** | +5.7 | 1e-06 | 14/26 (NCI-H2347, Panc 03.27, …) | top dose only | composition shift; position effect removed |
| [[Selinexor (drug)]] 0.5 µM |  | **1.78×** | +4.9 | 8e-05 | 15/26 (PANC-1, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.78×** | +4.7 | 2e-04 | 13/24 (PANC-1, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **1.65×** | +4.2 | 0.001 | 10/25 (NCI-H2030, C-33 A, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~31% of this change | **1.65×** | +4.2 | 0.001 | 10/22 (PANC-1, SNU-423, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.61×** | +3.8 | 0.006 | 2/15 (PANC-1, NCI-H1792) | all doses, flat | cell-cycle shift (explains ~15% here); composition shift |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.53×** | +3.6 | 0.015 | 3/27 (A-172, C32, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.94×** | +3.5 | 0.015 | 1/25 (Panc 03.27) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **1.52×** | +3.5 | 0.015 | 11/27 (PANC-1, RPMI-7951, …) | top dose only |  |
| [[Palmatine (chloride) (drug)]] 0.5 µM |  | **1.43×** | +3.0 | 0.083 | 8/26 (HS-578T, CHP-212, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4252.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 4 lines (NCI-H460 0.0911×, CHP-212 0.121×, hTERT-HPNE 0.138×, AN3 CA 0.202×); [[Panobinostat (drug)]] 5 µM in 4 lines (NCI-H460 0.104×, CHP-212 0.133×, hTERT-HPNE 0.0780×, AN3 CA 0.165×; ⚠ cell-cycle shift, explains ~6% of this change); [[Belinostat (drug)]] 5 µM in 3 lines (NCI-H460 0.0898×, CHP-212 0.251×, hTERT-HPNE 0.163×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (CHP-212 0.298×, AN3 CA 0.270×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.635×** | -3.9 | 0.051 | 14/27 (NCI-H460, CHP-212, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.627×** | -3.7 | 0.051 | 9/28 (NCI-H460, HS-578T, …) | inconsistent across doses |  |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.652×** | -3.6 | 0.051 | 5/28 (SW 900, C-33 A, …) | inconsistent across doses |  |
| [[Fenofibrate (drug)]] 0.05 µM |  | 0.652× | -3.4 | 0.11 | 2/27 (NCI-H460, AN3 CA) | inconsistent across doses |  |
| [[Benproperine (phosphate) (drug)]] 0.05 µM |  | 0.658× | -3.3 | 0.11 | 7/27 (NCI-H460, A-427, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, +0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4252. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 27.3 | 0 | 8 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -16.4) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.0898× (z -15.2) |
| [[AN3 CA (line)]] | alt | 130 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0907× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.270× (z -10.3) |
| [[CHP-212 (line)]] | wt | 309 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.121× (z -14.0) |
| [[hTERT-HPNE (line)]] | wt | 118 | 0 | 6 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0780× (z -12.5) ⚠ cell-cycle shift, explains ~6% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.138× (z -9.7) |
| [[A549 (line)]] | wt | 3.69 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.48× (z +10.4) | [[Phenytoin (sodium) (drug)]] 5 µM 0.0565× (z -8.9) |
| [[PANC-1 (line)]] | alt | 3.20 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.54× (z +10.8) | — |
| [[NCI-H2030 (line)]] | alt | 4.82 | 0 | 1 | — | [[Pemetrexed (drug)]] 0.5 µM 0.0739× (z -9.6) |
| [[NCI-H2347 (line)]] | alt | 4.38 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.01× (z +8.6) ⚠ cell-cycle shift, explains ~49% of this change | — |
| [[RPMI-7951 (line)]] | alt | 11.7 | 1 | 0 | [[Selinexor (drug)]] 5 µM 4.64× (z +8.5) | — |
| [[SW480 (line)]] | alt | 13.7 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.188× (z -9.7) ⚠ cell-cycle shift, explains ~6% of this change |
| [[A-172 (line)]] | wt | 8.51 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.26 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.27 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 35.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.977 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.29 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.19 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.41 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.59 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 4.52 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.97 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.24 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 9.69 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.45 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 7.17 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.13 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.25 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.31 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.734 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.33 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 7.79 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.87 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.86 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.07 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.19 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.91 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.75 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.38 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.59 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.84 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4252), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEMA4C]] | +0.63 | +0.57 / +0.61 | both halves | 9e-06 |  |
| [[HOXB2]] | +0.60 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[HOXC9]] | +0.58 | +0.43 / +0.52 | both halves | 3e-05 |  |
| [[HOXC8]] | +0.57 | +0.39 / +0.55 | both halves | 6e-05 |  |
| [[PART1]] | +0.56 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[KCNK2]] | +0.55 | +0.67 / +0.41 | both halves | 4e-05 |  |
| [[ZNF433]] | +0.55 | +0.46 / +0.48 | both halves | 2e-05 |  |
| [[SLCO1C1]] | +0.54 | +0.54 / +0.44 | both halves | 3e-05 |  |
| [[FOXC1]] | +0.53 | +0.46 / +0.47 | both halves | 3e-05 |  |
| [[ZNF563]] | +0.53 | +0.41 / +0.48 | both halves | 4e-05 |  |
| [[LINC01257]] | +0.52 | +0.55 / +0.42 | both halves | 4e-05 |  |
| [[ZNF101]] | +0.51 | +0.44 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[JPT2]] | -0.49 | -0.35 / -0.52 | both halves | 1e-04 |  |
| [[ANXA2]] | -0.47 | -0.47 / -0.39 | both halves | 6e-05 |  |
| [[RHOA]] | -0.47 | -0.42 / -0.36 | both halves | 1e-04 |  |
| [[OPA1]] | -0.46 | -0.37 / -0.40 | both halves | 8e-05 |  |
| [[NUTF2]] | -0.46 | -0.37 / -0.41 | both halves | 9e-05 |  |
| [[FAM91A1]] | -0.45 | -0.36 / -0.45 | both halves | 9e-05 |  |
| [[LHPP]] | -0.44 | -0.22 / -0.38 | both halves | 6e-04 |  |
| [[CS]] | -0.43 | -0.24 / -0.42 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GREM2]] | B | GREM2 activity raises TBX2's level | lines that do not express GREM2 (40) vs lines expressing it (10) | 4.91× lower at baseline in the lines without GREM2 | 0.014 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC03000, GSG1L2, ENSG00000238054 |
| [[NLGN4Y]] | B | NLGN4Y activity raises TBX2's level | lines that do not express NLGN4Y (37) vs lines expressing it (13) | 2.39× lower at baseline in the lines without NLGN4Y | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GREM2, PDGFRB, PSG9 |
| [[PAMR1]] | C | PAMR1 activity raises TBX2's level | lines that do not express PAMR1 (28) vs lines expressing it (22) | 2.85× lower at baseline in the lines without PAMR1 | 0.075 | ⚠ within organs, on part of the lines; also absent: MARCHF4, FLRT2, ESM1; maybe low, not absent; co-absent with the target |
| [[GNG11]] | C | GNG11 activity raises TBX2's level | lines that do not express GNG11 (21) vs lines expressing it (29) | 2.81× lower at baseline in the lines without GNG11 | 0.087 | ⚠ within organs, on part of the lines; also absent: LOXL2, SLC8A1, NALCN; co-absent with the target |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.430). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-0.0, 24.9); signed map (19.5, -12.0). **Vector** length 69.8, 17.4% of its response variance represented; |z| ≥ 3 in 590 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.9 | +11.5 |
|  | [[Selinexor (drug)]] 5 µM |  | +5.6 | +6.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | +3.9 | +5.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +3.8 | +5.9 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +3.4 | +4.9 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.5 | +5.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.3 | +3.5 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.2 | +3.6 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | +1.9 | +2.1 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +1.8 | +2.7 |
| fall | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | -2.5 | -1.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.5 | -3.9 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.1 | -1.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.1 | -3.7 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.8 | -2.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.8 | -1.7 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.7 | -1.6 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.7 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | T-box transcription factor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q23.2 — chr17:61,399,843-61,409,466 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | T-box transcription factors |
| Reactome | 3 pathways, smallest: Regulation of MITF-M-dependent genes involved in cell cycle and proliferation; MITF-M-dependent gene expression; MITF-M-regulated melanocyte development |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13207](https://www.uniprot.org/uniprotkb/Q13207) (T-box transcription factor TBX2):

> Transcription factor which acts as a transcriptional repressor. May also function as a transcriptional activator (By similarity). Binds to the palindromic T site 5'-TTCACACCTAGGTGTGAA-3' DNA sequence, or a half-site, which are present in the regulatory region of several genes. Required for cardiac atrioventricular canal formation. May cooperate with NKX2.5 to negatively modulate expression of NPPA/ANF in the atrioventricular canal (By similarity). May play a role as a positive regulator of …

**Summary**, from NCBI Gene [6909](https://www.ncbi.nlm.nih.gov/gene/6909):

> This gene is a member of a phylogenetically conserved family of genes that share a common DNA-binding domain, the T-box. T-box genes encode transcription factors involved in the regulation of developmental processes. This gene product is the human homolog of mouse Tbx2, and shares strong sequence similarity with Drosophila omb protein. Expression studies indicate that this gene may have a potential role in tumorigenesis as an immortalizing agent. Transcript heterogeneity due to alternative …

**Accessions** — [HGNC:11597](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11597) · Entrez [6909](https://www.ncbi.nlm.nih.gov/gene/6909) · UniProt [Q13207](https://www.uniprot.org/uniprotkb/Q13207) · Ensembl [ENSG00000121068](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000121068)

## Data

Gene col 4252: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4252); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4252, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4252]; `tensor/DDL_lfc|DDL_z.npy` [4252]; `embed/gene_vectors.npy` [4252]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4252 or target_col == 4252). Every well: [[TBX2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TBX2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
