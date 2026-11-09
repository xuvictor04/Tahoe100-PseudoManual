---
symbol: "PLAAT3"
type: "gene"
col: 10725
ensembl_id: "ENSG00000176485"
name: "phospholipase A and acyltransferase 3"
location: "11q12.3-q13.1"
module: 44
arm: "+"
pooled_cpm: 32.97
n_lines_expressing: 40
n_dd_up: 15
n_dd_down: 6
n_dd_up_clean: 10
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 11
direction_downstream: 2
tags: ["gene", "module/044"]
generated_by: "tahoemap"
---

# PLAAT3

*phospholipase A and acyltransferase 3* — 11q12.3-q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.15× (z +9.1, q 3e-17, up in 24 of 30 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.41× (z +5.8, q 7e-07, up in 23 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.569× (z -6.7, q 1e-08, down in 26 of 37 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.633× (z -5.4, q 2e-05, down in 25 of 37 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 7 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (COLO 205 0.0443×, KATO III 0.272×, HT-29 0.360×, LS 180 0.297×; ⚠ cell-cycle shift, explains ~0% of this change); [[Panobinostat (drug)]] 5 µM in 4 lines (HT-29 0.238×, KATO III 0.202×, A-172 0.322×, Hs 766T 0.273×; ⚠ cell-cycle shift, explains ~40% of this change); [[Panobinostat (drug)]] 0.5 µM in 3 lines (KATO III 0.244×, HT-29 0.296×, A-172 0.334×; ⚠ cell-cycle shift, explains ~38% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (KATO III 0.330×, Panc 03.27 0.362×); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (LS 180 0.263×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PLEKHG6]] (+0.73, fdr 7e-06), [[PIK3C2B]] (+0.67, fdr 1e-05), [[MAP3K8]] (+0.65, fdr 1e-05); moves opposite to [[WDR27]] (-0.56, fdr 1e-05), [[MSS51]] (-0.54, fdr 3e-05), [[HMGA2]] (-0.52, fdr 1e-05).
> It is in [[Module 044]], a single-armed module (Defective GALNT12 causes CRCS1).
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[CRACDL]] → it (grade B ⚠); 2 go from it, the strongest it → [[GALM]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 5 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10725.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.15×** | +9.1 | 3e-17 | 24/30 (C-33 A, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.11×** | +8.6 | 3e-15 | 18/24 (LoVo, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.70×** | +5.9 | 7e-07 | 15/25 (HEC-1-A, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.41×** | +5.8 | 7e-07 | 23/38 (HOP62, SW480, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.48×** | +4.7 | 3e-04 | 21/38 (A-172, J82, …) | all doses, stronger at high dose | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.46×** | +4.5 | 7e-04 | 11/37 (HS-578T, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.42×** | +4.2 | 0.002 | 17/37 (A-172, CFPAC-1, …) | top dose only | position effect removed |
| [[Radotinib (drug)]] 5 µM |  | **1.28×** | +4.1 | 0.002 | 18/38 (AsPC-1, A-427, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~28% of this change | **1.36×** | +3.7 | 0.016 | 18/33 (SW 900, NCI-H2347, …) | inconsistent across doses | low cells (technical?) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.37×** | +3.5 | 0.030 | 16/38 (BT-474, Hs 766T, …) | two highest doses | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.35×** | +3.4 | 0.030 | 17/37 (Hs 766T, AsPC-1, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.34×** | +3.3 | 0.038 | 14/37 (Hs 766T, AsPC-1, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.30×** | +3.2 | 0.066 | 13/38 (AsPC-1, BT-474, …) | all doses, flat | noisy plate (z scaled) |
| [[Entrectinib (drug)]] 5 µM |  | **1.30×** | +3.1 | 0.068 | 8/37 (CFPAC-1, RKO, …) | top dose only |  |
| [[Adagrasib (drug)]] 5 µM |  | **1.30×** | +3.0 | 0.097 | 10/38 (HOP62, NCI-H2030, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10725.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 7 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (COLO 205 0.0443×, KATO III 0.272×, HT-29 0.360×, LS 180 0.297×; ⚠ cell-cycle shift, explains ~0% of this change); [[Panobinostat (drug)]] 5 µM in 4 lines (HT-29 0.238×, KATO III 0.202×, A-172 0.322×, Hs 766T 0.273×; ⚠ cell-cycle shift, explains ~40% of this change); [[Panobinostat (drug)]] 0.5 µM in 3 lines (KATO III 0.244×, HT-29 0.296×, A-172 0.334×; ⚠ cell-cycle shift, explains ~38% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (KATO III 0.330×, Panc 03.27 0.362×); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (LS 180 0.263×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.569×** | -6.7 | 1e-08 | 26/37 (KATO III, Panc 03.27, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.633×** | -5.4 | 2e-05 | 25/37 (LS 180, SNU-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.697×** | -4.1 | 0.006 | 22/37 (RKO, A-427, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.708×** | -4.1 | 0.006 | 19/38 (HT-29, KATO III, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.732×** | -3.7 | 0.024 | 15/38 (KATO III, HT-29, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.819×** | -3.3 | 0.081 | 15/38 (Hs 766T, A-172, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 0.765× | -3.2 | 0.12 | 16/38 (LS 180, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | 0.774× | -3.0 | 0.16 | 17/38 (KATO III, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, +0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10725. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 135 | 0 | 6 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.360× (z -13.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 113 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -14.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.330× (z -9.0) |
| [[A-172 (line)]] | wt | 91.5 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.322× (z -10.3) ⚠ cell-cycle shift, explains ~40% of this change |
| [[Hs 766T (line)]] | wt | 71.6 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.273× (z -9.3) ⚠ cell-cycle shift, explains ~40% of this change |
| [[LoVo (line)]] | wt | 48.3 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.22× (z +9.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.417× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 32.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.297× (z -10.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.263× (z -8.5) |
| [[Panc 03.27 (line)]] | alt | 128 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.362× (z -8.6) |
| [[A-427 (line)]] | wt | 21.9 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.246× (z -8.6) ⚠ cell-cycle shift, explains ~30% of this change |
| [[C-33 A (line)]] | alt | 19.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.56× (z +9.3) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 30.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0443× (z -21.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 26.8 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.212× (z -9.1) ⚠ cell-cycle shift, explains ~30% of this change |
| [[A498 (line)]] | wt | 2.40 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 28.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.92 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.79 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 127 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.69 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 53.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.15 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.33 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.52 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.42 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 6.99 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 6.51 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 49.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.94 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.65 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 30.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.88 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 75.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 14.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10725), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLEKHG6]] | +0.73 | +0.73 / +0.60 | both halves | 7e-06 |  |
| [[PIK3C2B]] | +0.67 | +0.68 / +0.55 | both halves | 1e-05 | pathway: Phospholipid metabolism |
| [[MAP3K8]] | +0.65 | +0.67 / +0.54 | both halves | 1e-05 |  |
| [[PKDCC]] | +0.64 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[ATP8B1]] | +0.62 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[TJP3]] | +0.61 | +0.57 / +0.60 | both halves | 1e-05 | pathway: HALLMARK_ESTROGEN_RESPONSE_EARLY |
| [[ELF3]] | +0.61 | +0.61 / +0.57 | both halves | 9e-06 | pathway: HALLMARK_ESTROGEN_RESPONSE_EARLY |
| [[SLC40A1]] | +0.61 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[MUC12]] | +0.60 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[MUC3A]] | +0.60 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[PRR15]] | +0.59 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[GALM]] | +0.59 | +0.55 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDR27]] | -0.56 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[MSS51]] | -0.54 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[HMGA2]] | -0.52 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[KIAA1549L]] | -0.50 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[NEU3]] | -0.49 | -0.49 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 11, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CRACDL]] | B | CRACDL activity raises PLAAT3's level | lines that do not express CRACDL (25) vs lines expressing it (25) | 2.48× lower at baseline in the lines without CRACDL | 0.033 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CGN, MARVELD3, CASC19 |
| [[DAPK1]] | B | DAPK1 activity raises PLAAT3's level | lines that do not express DAPK1 (23) vs lines expressing it (27) | 1.70× lower at baseline in the lines without DAPK1 | 0.035 | ⚠ within organs, on part of the lines; also absent: HAVCR1, DCDC2, ENSG00000275649 |
| [[IGFL2-AS1]] | B | IGFL2-AS1 activity raises PLAAT3's level | lines that do not express IGFL2-AS1 (36) vs lines expressing it (14) | 2.35× lower at baseline in the lines without IGFL2-AS1 | 0.042 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALB1, CLRN3, LINC01559 |
| [[PTPRB]] | B | PTPRB activity raises PLAAT3's level | lines that do not express PTPRB (22) vs lines expressing it (28) | 2.15× lower at baseline in the lines without PTPRB | 0.057 | ⚠ within organs, on part of the lines; also absent: PLAAT4, PTPRR, ADGRF4 |
| [[MAP2K1]] | B | MAP2K1 activity lowers PLAAT3's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.1% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds |
| [[ATP8B1]] | B | ATP8B1 activity raises PLAAT3's level | lines that do not express ATP8B1 (14) vs lines expressing it (36) | 2.41× lower at baseline in the lines without ATP8B1 | 0.065 | ⚠ within organs, on part of the lines; also absent: LGALS9, CDA, KRT86 |
| [[FUT2]] | B | FUT2 activity raises PLAAT3's level | lines that do not express FUT2 (12) vs lines expressing it (38) | 1.83× lower at baseline in the lines without FUT2 | 0.065 | ⚠ within organs, on part of the lines; also absent: EFNB2, SH3TC1, PTPRE; maybe low, not absent |
| [[PDZK1IP1]] | B | PDZK1IP1 activity raises PLAAT3's level | lines that do not express PDZK1IP1 (32) vs lines expressing it (18) | 2.07× lower at baseline in the lines without PDZK1IP1 | 0.066 | ⚠ within organs, on part of the lines; also absent: MUC5B, UCA1, PRSS8 |
| [[GBP2]] | B | GBP2 activity raises PLAAT3's level | lines that do not express GBP2 (13) vs lines expressing it (37) | 1.46× lower at baseline in the lines without GBP2 | 0.068 | ⚠ within organs, on part of the lines; also absent: GBP1, ITGA3, SH3TC1 |
| [[TOP2B]] | B | TOP2B activity raises PLAAT3's level | compounds that target TOP2B: 2 of 2 lower it (Doxorubicin, Mitoxantrone) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[LINC02967]] | B | LINC02967 activity raises PLAAT3's level | lines that do not express LINC02967 (34) vs lines expressing it (16) | 2.56× lower at baseline in the lines without LINC02967 | 0.085 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with CDKN2A; also absent: TMEM30B, RAB25, TMPRSS4 |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GALM]] | B | PLAAT3 activity raises GALM's level | lines that do not express PLAAT3 (10) vs lines expressing it (40) | 1.83× lower at baseline in the lines without PLAAT3 | 0.071 | ⚠ within organs, on part of the lines; also absent: ME3, CTDSPL |
| [[HMGA2]] | B | PLAAT3 activity raises HMGA2's level | lines that do not express PLAAT3 (10) vs lines expressing it (40) | 1.88× lower at baseline in the lines without PLAAT3 | 0.089 | ⚠ within organs, on part of the lines; also absent: ME3, CTDSPL |

## Where it sits

- **Module**: [[Module 044]] — Defective GALNT12 causes CRCS1; 102 genes; every member is in the + arm (projection on the module's main direction 0.683). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (20.6, 52.9); signed map (50.3, 2.6). **Vector** length 85.4, 23.1% of its response variance represented; |z| ≥ 3 in 665 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Glucuronidation* (reactome, mean cos +0.54 to 4); *Aspirin ADME* (reactome, mean cos +0.54 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.6 | +5.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.2 | +9.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.1 | +4.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.8 | +8.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.5 | -0.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.9 | +3.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.8 | +4.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.4 | +4.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.4 | +3.5 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.2 | -6.7 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -3.0 | -1.1 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.6 | -5.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.1 | -1.2 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -2.0 | -2.7 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -1.9 | -3.0 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.8 | -0.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.8 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | phospholipase A and acyltransferase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q12.3-q13.1 — chr11:63,573,195-63,616,883 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HREV107, H-REV107-1, HREV107-3, MGC118754., AdPLA, PLAAT-3; previously HRASLS3, PLA2G16 |
| Gene groups (HGNC) | Phospholipases; Phospholipase A and acyltransferase family |
| Hallmark sets | ESTROGEN_RESPONSE_LATE, ESTROGEN_RESPONSE_EARLY |
| Reactome | 7 pathways, smallest: Acyl chain remodelling of PI; Acyl chain remodelling of PS; Acyl chain remodelling of PC |
| Matched by | ensembl_id |

**Function**, from UniProt [P53816](https://www.uniprot.org/uniprotkb/P53816) (Phospholipase A and acyltransferase 3):

> Exhibits both phospholipase A1/2 and acyltransferase activities. Shows phospholipase A1 (PLA1) and A2 (PLA2) activity, catalyzing the calcium-independent release of fatty acids from the sn-1 or sn-2 position of glycerophospholipids. For most substrates, PLA1 activity is much higher than PLA2 activity. Shows O-acyltransferase activity,catalyzing the transfer of a fatty acyl group from glycerophospholipid to the hydroxyl group of lysophospholipid. Shows N-acyltransferase activity, catalyzing the …

**Summary**, from NCBI Gene [11145](https://www.ncbi.nlm.nih.gov/gene/11145):

> Enables N-acyltransferase activity; glycerophospholipase activity; and lipid binding activity. Involved in N-acylphosphatidylethanolamine metabolic process. Located in cytosol. Biomarker of seminoma. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:17825](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17825) · Entrez [11145](https://www.ncbi.nlm.nih.gov/gene/11145) · UniProt [P53816](https://www.uniprot.org/uniprotkb/P53816) · Ensembl [ENSG00000176485](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000176485)

## Data

Gene col 10725: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10725); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10725, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10725]; `tensor/DDL_lfc|DDL_z.npy` [10725]; `embed/gene_vectors.npy` [10725]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10725 or target_col == 10725). Every well: [[PLAAT3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLAAT3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
