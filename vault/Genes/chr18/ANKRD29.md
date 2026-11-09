---
symbol: "ANKRD29"
type: "gene"
col: 7765
ensembl_id: "ENSG00000154065"
name: "ankyrin repeat domain 29"
location: "18q11.2"
module: 196
arm: "+"
pooled_cpm: 6.54
n_lines_expressing: 31
n_dd_up: 16
n_dd_down: 3
n_dd_up_clean: 10
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 3
direction_downstream: 4
tags: ["gene", "module/196"]
generated_by: "tahoemap"
---

# ANKRD29

*ankyrin repeat domain 29* — 18q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (6 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.86× (z +15.8, q 0e+00, up in 24 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.616× (z -7.2, q 3e-10, down in 20 of 27 measured lines) ⚠ cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.584× (z -5.7, q 4e-06, down in 17 of 28 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 18 here, 7 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 6 lines (NCI-H460 0.149×, C32 0.139×, A549 0.172×, SW 900 0.162×, …; ⚠ cell-cycle shift, explains ~33% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (HT-29 0.219×, SW 900 0.201×; ⚠ cell-cycle shift, explains ~37% of this change); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 2 lines (A-427 0.181×, LoVo 0.126×); [[Binimetinib (drug)]] 0.5 µM in 1 line (C32 0.0895×); [[Binimetinib (drug)]] 5 µM in 1 line (C32 0.169×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CNTNAP3B]] (+0.54, fdr 1e-05), [[TDRD9]] (+0.51, fdr 6e-05), [[CSF2RA]] (+0.51, fdr 1e-04); moves opposite to [[TTC28-AS1]] (-0.42, fdr 2e-04), [[EFCAB11]] (-0.41, fdr 1e-04), [[MTMR4]] (-0.41, fdr 3e-05).
> It is in [[Module 196]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[LAMA3]] → it (grade B ⚠); 4 go from it, the strongest it → [[LAMA3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 6 with an alert ⚠; shown: the 15 strongest. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7765.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.86×** | +15.8 | 0e+00 | 24/28 (SW480, A-172, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.26×** | +12.1 | 5e-31 | 5/11 (NCI-H1792, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.75×** | +10.8 | 1e-24 | 22/27 (SW480, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.34×** | +9.0 | 2e-17 | 14/28 (NCI-H1573, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.27×** | +8.0 | 1e-13 | 3/13 (HOP62, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.05×** | +7.2 | 7e-11 | 20/28 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.91×** | +6.9 | 6e-10 | 10/20 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.80×** | +6.2 | 3e-08 | 11/28 (J82, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.67×** | +5.4 | 3e-06 | 15/28 (NCI-H1573, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.56×** | +4.5 | 3e-04 | 6/20 (AsPC-1, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~21% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.41×** | +3.6 | 0.014 | 4/27 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **1.91×** | +3.6 | 0.016 | 1/28 (NCI-H1573) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 5 µM |  | **1.36×** | +3.2 | 0.059 | 5/28 (A-427, A498, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.23×** | +3.2 | 0.059 | 2/29 (A498, NCI-H2347) | rises with dose |  |
| [[Simotinib (drug)]] 5 µM | ⚠ toxic | **1.35×** | +3.1 | 0.078 | 4/22 (A498, SW 900, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7765.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 18 here, 7 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 6 lines (NCI-H460 0.149×, C32 0.139×, A549 0.172×, SW 900 0.162×, …; ⚠ cell-cycle shift, explains ~33% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (HT-29 0.219×, SW 900 0.201×; ⚠ cell-cycle shift, explains ~37% of this change); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 2 lines (A-427 0.181×, LoVo 0.126×); [[Binimetinib (drug)]] 0.5 µM in 1 line (C32 0.0895×); [[Binimetinib (drug)]] 5 µM in 1 line (C32 0.169×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.616×** | -7.2 | 3e-10 | 20/27 (NCI-H460, C32, …) | top dose only | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.584×** | -5.7 | 4e-06 | 17/28 (NCI-H2030, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.613×** | -5.2 | 4e-05 | 12/28 (A-427, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | 0.727× | -3.4 | 0.11 | 11/28 (A-427, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | 0.576× | -3.1 | 0.26 | 11/26 (A-427, SW 900, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7765. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 25.3 | 0 | 9 (3 ⚠) | — | [[Binimetinib (drug)]] 0.5 µM 0.0895× (z -13.3) |
| [[NCI-H460 (line)]] | wt | 10.2 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -14.7) ⚠ cell-cycle shift, explains ~33% of this change |
| [[SW 900 (line)]] | alt | 23.0 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.162× (z -12.3) ⚠ cell-cycle shift, explains ~33% of this change |
| [[SW48 (line)]] | wt | 19.2 | 0 | 3 (1 ⚠) | — | [[Bendamustine (drug)]] 5 µM 0.106× (z -9.4) |
| [[A-427 (line)]] | wt | 24.5 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.181× (z -11.5) |
| [[A549 (line)]] | wt | 19.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.172× (z -12.8) ⚠ cell-cycle shift, explains ~33% of this change |
| [[LoVo (line)]] | wt | 4.39 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.111× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.126× (z -8.9) |
| [[A498 (line)]] | wt | 8.90 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.208× (z -11.6) ⚠ cell-cycle shift, explains ~33% of this change |
| [[HT-29 (line)]] | alt | 15.3 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.219× (z -11.8) ⚠ cell-cycle shift, explains ~37% of this change |
| [[NCI-H1792 (line)]] | alt | 44.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -9.8) ⚠ cell-cycle shift, explains ~33% of this change |
| [[NCI-H2030 (line)]] | alt | 12.7 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.150× (z -9.2) |
| [[SW480 (line)]] | alt | 3.46 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 4.33× (z +9.1) | — |
| [[A-172 (line)]] | wt | 2.00 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.40 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.870 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.801 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.13 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.60 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.895 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.962 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.04 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.17 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.768 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.883 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 4.07 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.02 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.15 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.913 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.797 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 6.27 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.688 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.848 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.879 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.51 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7765), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CNTNAP3B]] | +0.54 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[TDRD9]] | +0.51 | +0.39 / +0.49 | both halves | 6e-05 |  |
| [[CSF2RA]] | +0.51 | +0.33 / +0.51 | both halves | 1e-04 |  |
| [[ANKRD6]] | +0.51 | +0.52 / +0.43 | both halves | 3e-05 | same gene group |
| [[ACOXL]] | +0.51 | +0.44 / +0.47 | both halves | 3e-05 |  |
| [[RAB27B]] | +0.51 | +0.50 / +0.40 | both halves | 5e-05 |  |
| [[MCTP1]] | +0.51 | +0.37 / +0.54 | both halves | 8e-05 |  |
| [[ARHGEF4]] | +0.50 | +0.44 / +0.47 | both halves | 3e-05 |  |
| [[FAM124A]] | +0.50 | +0.43 / +0.47 | both halves | 3e-05 | STRING 454 |
| [[CHMP1B2P]] | +0.49 | +0.38 / +0.50 | both halves | 6e-05 |  |
| [[CNTNAP3]] | +0.49 | +0.47 / +0.48 | both halves | 2e-05 |  |
| [[AMOTL1]] | +0.49 | +0.44 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TTC28-AS1]] | -0.42 | -0.44 / -0.32 | both halves | 2e-04 |  |
| [[EFCAB11]] | -0.41 | -0.33 / -0.51 | both halves | 1e-04 |  |
| [[MTMR4]] | -0.41 | -0.43 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LAMA3]] | B | LAMA3 activity raises ANKRD29's level | lines that do not express LAMA3 (22) vs lines expressing it (28) | 2.43× lower at baseline in the lines without LAMA3 | 0.001 | ⚠ within organs, on part of the lines; also absent: P2RY2, ELF3, MYO5B |
| [[GOLGA7B-DT]] | B | GOLGA7B-DT activity raises ANKRD29's level | lines that do not express GOLGA7B-DT (12) vs lines expressing it (38) | 2.59× lower at baseline in the lines without GOLGA7B-DT | 0.031 | ⚠ within organs, on part of the lines; also absent: GOLGA7B, BCL11B, GJB2; maybe low, not absent |
| [[PTGS2]] | B | PTGS2 activity raises ANKRD29's level | lines that do not express PTGS2 (27) vs lines expressing it (23) | 2.11× lower at baseline in the lines without PTGS2 | 0.075 | ⚠ within organs, on part of the lines; also absent: ADAMTS9-AS2, CFH, ITGA4 |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LAMA3]] | B | ANKRD29 activity raises LAMA3's level | lines that do not express ANKRD29 (19) vs lines expressing it (31) | 2.55× lower at baseline in the lines without ANKRD29 | 0.020 | ⚠ within organs, on part of the lines; also absent: NHS, PI3, GPR37 |
| [[CNTNAP3]] | B | ANKRD29 activity raises CNTNAP3's level | lines that do not express ANKRD29 (19) vs lines expressing it (31) | 2.13× lower at baseline in the lines without ANKRD29 | 0.060 | ⚠ within organs, on part of the lines; also absent: NHS, PI3, GPR37 |
| [[MCTP1]] | B | ANKRD29 activity lowers MCTP1's level | lines that do not express ANKRD29 (19) vs lines expressing it (31) | 1.16× higher at baseline in the lines without ANKRD29 | 0.064 | ⚠ within organs, on part of the lines; also absent: NHS, PI3, GPR37 |
| [[PTGS2]] | B | ANKRD29 activity raises PTGS2's level | lines that do not express ANKRD29 (19) vs lines expressing it (31) | 3.76× lower at baseline in the lines without ANKRD29 | 0.099 | ⚠ within organs, on part of the lines; also absent: NHS, PI3, GPR37 |

## Where it sits

- **Module**: [[Module 196]]; 17 genes; every member is in the + arm (projection on the module's main direction 0.551). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (30.9, 27.6); signed map (17.6, 56.3). **Vector** length 63.4, 13.9% of its response variance represented; |z| ≥ 3 in 690 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.7 | +15.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.9 | +12.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.3 | +6.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.9 | +10.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.2 | +8.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.0 | +1.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | +3.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.9 | +0.8 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.8 | +2.2 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.4 | -1.5 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.3 | -2.0 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | -1.9 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.8 | -0.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.7 | +0.7 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.6 | -1.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.6 | -2.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.4 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | ankyrin repeat domain 29 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q11.2 — chr18:23,598,926-23,662,911 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ25053 |
| Gene groups (HGNC) | Ankyrin repeat domain containing |
| Matched by | ensembl_id |

UniProt [Q8N6D5](https://www.uniprot.org/uniprotkb/Q8N6D5) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:27110](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27110) · Entrez [147463](https://www.ncbi.nlm.nih.gov/gene/147463) · UniProt [Q8N6D5](https://www.uniprot.org/uniprotkb/Q8N6D5) · Ensembl [ENSG00000154065](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000154065)

## Data

Gene col 7765: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7765); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7765, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7765]; `tensor/DDL_lfc|DDL_z.npy` [7765]; `embed/gene_vectors.npy` [7765]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7765 or target_col == 7765). Every well: [[ANKRD29 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANKRD29.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
