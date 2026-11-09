---
symbol: "PLCH1"
type: "gene"
col: 3591
ensembl_id: "ENSG00000114805"
name: "phospholipase C eta 1"
location: "3q25.31"
module: 8
arm: "+"
pooled_cpm: 21.54
n_lines_expressing: 38
n_dd_up: 31
n_dd_down: 21
n_dd_up_clean: 25
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 42
direction_downstream: 22
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# PLCH1

*phospholipase C eta 1* — 3q25.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.48× (z +7.1, q 8e-10, up in 14 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (6 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.401× (z -11.8, q 3e-29, down in 27 of 36 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC02331]] (+0.79, fdr 7e-06), [[BCL2L15]] (+0.77, fdr 7e-06), [[ARHGEF38]] (+0.72, fdr 7e-06); moves opposite to [[DNAAF9]] (-0.63, fdr 1e-05), [[PDLIM7]] (-0.62, fdr 1e-05), [[CROCCP3]] (-0.59, fdr 3e-05).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 42 arrows point to it, the strongest [[CATSPERB]] → it (grade B ⚠); 22 go from it, the strongest it → [[RBM47]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3591.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.48×** | +7.1 | 8e-10 | 14/34 (NCI-H2347, A-172, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.45×** | +6.8 | 3e-09 | 19/36 (NCI-H2347, KATO III, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.44×** | +6.6 | 7e-09 | 17/34 (A-172, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.61×** | +5.8 | 1e-06 | 21/36 (AsPC-1, HEC-1-A, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.58×** | +5.7 | 1e-06 | 20/36 (AsPC-1, HEC-1-A, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.47×** | +5.0 | 7e-05 | 23/36 (AsPC-1, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.38×** | +4.9 | 9e-05 | 19/36 (AsPC-1, HEC-1-A, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.47×** | +4.8 | 1e-04 | 21/36 (AsPC-1, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.34×** | +4.6 | 3e-04 | 20/36 (AsPC-1, HEC-1-A, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.05 µM |  | **1.42×** | +4.5 | 4e-04 | 17/36 (HT-29, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.43×** | +4.4 | 6e-04 | 17/36 (AsPC-1, NCI-H23, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.30×** | +4.4 | 6e-04 | 16/36 (AsPC-1, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.29×** | +4.3 | 9e-04 | 17/36 (AsPC-1, A549, …) | all doses, flat |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.39×** | +4.2 | 1e-03 | 14/36 (HT-29, SW1417, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.38×** | +4.2 | 0.001 | 16/36 (HEC-1-A, AsPC-1, …) | two highest doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.33×** | +3.6 | 0.009 | 8/36 (SW1417, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.32×** | +3.4 | 0.020 | 10/36 (A-172, C-33 A, …) | top dose only | cell-cycle shift (explains ~13% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3591.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.401×** | -11.8 | 3e-29 | 27/36 (COLO 205, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.458×** | -10.0 | 3e-21 | 29/36 (COLO 205, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.486×** | -9.3 | 3e-18 | 28/35 (COLO 205, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.607×** | -6.4 | 2e-08 | 21/36 (COLO 205, LoVo, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.612×** | -6.3 | 3e-08 | 25/36 (SW480, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.721×** | -5.9 | 3e-07 | 21/36 (KATO III, HT-29, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.665×** | -5.2 | 1e-05 | 16/36 (KATO III, HT-29, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.673×** | -5.1 | 2e-05 | 17/36 (NCI-H661, CHP-212, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.694×** | -4.5 | 4e-04 | 18/33 (LoVo, COLO 205, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.725×** | -4.1 | 0.002 | 14/36 (HT-29, LS 180, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.728×** | -4.1 | 0.002 | 18/36 (A549, HepG2/C3A, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.742×** | -3.8 | 0.006 | 19/36 (COLO 205, LoVo, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 5 µM |  | **0.736×** | -3.8 | 0.007 | 14/36 (Panc 03.27, HT-29, …) | all doses, stronger at high dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.744×** | -3.7 | 0.010 | 11/36 (SW480, A549, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.605×** | -3.4 | 0.027 | 15/35 (KATO III, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 5 µM |  | **0.629×** | -3.1 | 0.057 | 6/36 (SW480, BT-474, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **0.719×** | -3.0 | 0.067 | 12/36 (HT-29, SK-MEL-2, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.638×** | -3.0 | 0.067 | 12/35 (A498, SW48, …) | rises with dose | noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3591. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 207 | 0 | 16 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0568× (z -35.3) |
| [[KATO III (line)]] | alt | 115 | 0 | 14 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.110× (z -16.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.131× (z -16.0) |
| [[LoVo (line)]] | wt | 44.2 | 0 | 8 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.117× (z -17.6) |
| [[LS 180 (line)]] | wt | 87.9 | 0 | 7 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.187× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.206× (z -12.3) |
| [[SW480 (line)]] | alt | 31.1 | 0 | 6 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.120× (z -15.4) |
| [[HT-29 (line)]] | alt | 46.8 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.101× (z -16.1) ⚠ toxic; transcription drop · without an alert: [[Vinblastine (sulfate) (drug)]] 5 µM 0.395× (z -9.2) |
| [[A498 (line)]] | wt | 18.0 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0704× (z -13.0) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.186× (z -12.1) |
| [[SW48 (line)]] | wt | 54.9 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.154× (z -9.8) ⚠ toxic; transcription drop · without an alert: [[Ponatinib (drug)]] 5 µM 0.179× (z -9.0) |
| [[A-172 (line)]] | wt | 8.86 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.65× (z +10.2) | — |
| [[A549 (line)]] | wt | 45.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -12.2) |
| [[HEC-1-A (line)]] | alt | 32.0 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.264× (z -9.6) |
| [[J82 (line)]] | alt | 6.12 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.13× (z +8.9) | — |
| [[NCI-H1792 (line)]] | alt | 13.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0377× (z -15.3) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 15.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.35× (z +11.8) | — |
| [[NCI-H460 (line)]] | wt | 7.88 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.181× (z -9.4) |
| [[RKO (line)]] | wt | 16.3 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.104× (z -11.4) |
| [[SK-MEL-2 (line)]] | alt | 6.33 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.89× (z +9.8) | — |
| [[A-427 (line)]] | wt | 4.13 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.59 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.54 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.73 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.93 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 3.25 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.83 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.03 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.63 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.92 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.20 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.67 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 45.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.83 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 5.73 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.52 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 5.44 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.05 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.78 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 3.46 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3591), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02331]] | +0.79 | +0.77 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[BCL2L15]] | +0.77 | +0.75 / +0.68 | both halves | 7e-06 |  |
| [[ARHGEF38]] | +0.72 | +0.69 / +0.70 | both halves | 7e-06 |  |
| [[HNF4G]] | +0.72 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[NPNT]] | +0.72 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[MGAM2]] | +0.71 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[PROM1]] | +0.71 | +0.67 / +0.70 | both halves | 7e-06 |  |
| [[ANK3]] | +0.71 | +0.71 / +0.67 | both halves | 7e-06 |  |
| [[SIDT1]] | +0.70 | +0.70 / +0.72 | both halves | 7e-06 |  |
| [[CCSER1]] | +0.70 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[SAMD12-AS1]] | +0.70 | +0.70 / +0.59 | both halves | 7e-06 |  |
| [[POF1B]] | +0.70 | +0.68 / +0.68 | both halves | 7e-06 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAAF9]] | -0.63 | -0.64 / -0.53 | both halves | 1e-05 |  |
| [[PDLIM7]] | -0.62 | -0.61 / -0.53 | both halves | 1e-05 |  |
| [[CROCCP3]] | -0.59 | -0.59 / -0.46 | both halves | 3e-05 |  |
| [[CROCCP3-1]] | -0.57 | -0.56 / -0.55 | both halves | 1e-05 |  |
| [[ARID3B]] | -0.56 | -0.58 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*42 arrows, 42 of them with an alert ⚠; grade A 0, B 42, C 0. Shown: the 12 strongest; 30 more arrows (30 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CATSPERB]] | B | CATSPERB activity raises PLCH1's level | lines that do not express CATSPERB (30) vs lines expressing it (20) | 3.61× lower at baseline in the lines without CATSPERB | 0.006 | ⚠ within organs, on part of the lines; also absent: SGPP2, TC2N, ST14 |
| [[CYP4F3]] | B | CYP4F3 activity raises PLCH1's level | lines that do not express CYP4F3 (29) vs lines expressing it (21) | 2.83× lower at baseline in the lines without CYP4F3 | 0.006 | ⚠ within organs, on part of the lines; also absent: P2RY2, CYP3A5, ITGB6 |
| [[SIDT1]] | B | SIDT1 activity raises PLCH1's level | lines that do not express SIDT1 (32) vs lines expressing it (18) | 2.89× lower at baseline in the lines without SIDT1 | 0.006 | ⚠ within organs, on part of the lines; also absent: TMEM30B, STEAP4, GRHL2 |
| [[LINC01876]] | B | LINC01876 activity raises PLCH1's level | lines that do not express LINC01876 (24) vs lines expressing it (26) | 2.20× lower at baseline in the lines without LINC01876 | 0.007 | ⚠ within organs, on part of the lines; also absent: TOX3, TFF1, TMEM45B |
| [[TLR3]] | B | TLR3 activity raises PLCH1's level | lines that do not express TLR3 (12) vs lines expressing it (38) | 2.27× lower at baseline in the lines without TLR3 | 0.008 | ⚠ within organs, on part of the lines; also absent: LGALS3, GBP4, RAB27B; maybe low, not absent |
| [[RASSF6]] | B | RASSF6 activity raises PLCH1's level | lines that do not express RASSF6 (28) vs lines expressing it (22) | 2.88× lower at baseline in the lines without RASSF6 | 0.011 | ⚠ within organs, on part of the lines; also absent: TOX3, ELF3, ITGB6 |
| [[GCNT3]] | B | GCNT3 activity raises PLCH1's level | lines that do not express GCNT3 (38) vs lines expressing it (12) | 3.45× lower at baseline in the lines without GCNT3 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, LYZ, MUC13 |
| [[RBM47]] | B | RBM47 activity raises PLCH1's level | lines that do not express RBM47 (20) vs lines expressing it (30) | 2.95× lower at baseline in the lines without RBM47 | 0.013 | ⚠ within organs, on part of the lines; also absent: FA2H, MISP, ELF3 |
| [[SLC40A1]] | B | SLC40A1 activity raises PLCH1's level | lines that do not express SLC40A1 (28) vs lines expressing it (22) | 2.60× lower at baseline in the lines without SLC40A1 | 0.013 | ⚠ within organs, on part of the lines; also absent: RASSF6, WFDC2, TOX3 |
| [[SMIM2-AS1]] | B | SMIM2-AS1 activity raises PLCH1's level | lines that do not express SMIM2-AS1 (37) vs lines expressing it (13) | 2.70× lower at baseline in the lines without SMIM2-AS1 | 0.014 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ATP10B, CFTR, TRIM31; maybe low, not absent |
| [[HNF1A-AS1]] | B | HNF1A-AS1 activity raises PLCH1's level | lines that do not express HNF1A-AS1 (31) vs lines expressing it (19) | 3.21× lower at baseline in the lines without HNF1A-AS1 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: HNF1A, EPS8L3, GCNT3; maybe low, not absent |
| [[POF1B]] | B | POF1B activity raises PLCH1's level | lines that do not express POF1B (34) vs lines expressing it (16) | 3.49× lower at baseline in the lines without POF1B | 0.020 | ⚠ within organs, on part of the lines; also absent: S100P, ENSG00000287426, TRIM31 |

### Downstream of this gene

*22 arrows, 22 of them with an alert ⚠; grade A 0, B 22, C 0. Shown: the 12 strongest; 10 more arrows (10 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RBM47]] | B | PLCH1 activity raises RBM47's level | lines that do not express PLCH1 (12) vs lines expressing it (38) | 4.18× lower at baseline in the lines without PLCH1 | 0.005 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[TLR3]] | B | PLCH1 activity raises TLR3's level | lines that do not express PLCH1 (12) vs lines expressing it (38) | 2.10× lower at baseline in the lines without PLCH1 | 0.017 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[PDZK1IP1]] | B | PLCH1 activity raises PDZK1IP1's level | lines that do not express PLCH1 (12) vs lines expressing it (38) | 2.40× lower at baseline in the lines without PLCH1 | 0.027 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[FRK]] | B | PLCH1 activity raises FRK's level | lines that do not express PLCH1 (12) vs lines expressing it (38) | 3.12× lower at baseline in the lines without PLCH1 | 0.031 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[STS]] | B | PLCH1 activity raises STS's level | lines that do not express PLCH1 (12) vs lines expressing it (38) | 1.93× lower at baseline in the lines without PLCH1 | 0.033 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[SLC40A1]] | B | PLCH1 activity raises SLC40A1's level | lines that do not express PLCH1 (12) vs lines expressing it (38) | 2.31× lower at baseline in the lines without PLCH1 | 0.035 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[DNAJC15]] | B | PLCH1 activity strengthens DNAJC15's drug response | lines that do not express PLCH1 (10) vs lines expressing it (28) | the lines without PLCH1 respond 0.78× as strongly (z diff +0.77); strongest at Idarubicin (hydrochloride) 5 µM: 0.95x vs 0.65x (z diff +3.3) | 0.036 | ⚠ within organs, on part of the lines; maybe low, not absent; target measured in part of the lines; both ways; artifact flags |
| [[ITGB1BP1]] | B | PLCH1 activity lowers ITGB1BP1's level | lines that do not express PLCH1 (12) vs lines expressing it (38) | 1.47× higher at baseline in the lines without PLCH1 | 0.037 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[UCA1]] | B | PLCH1 activity raises UCA1's level | lines that do not express PLCH1 (12) vs lines expressing it (38) | 2.63× lower at baseline in the lines without PLCH1 | 0.039 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[DCDC2]] | B | PLCH1 activity raises DCDC2's level | lines that do not express PLCH1 (12) vs lines expressing it (38) | 2.52× lower at baseline in the lines without PLCH1 | 0.042 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[ELF3-AS1]] | B | PLCH1 activity raises ELF3-AS1's level | lines that do not express PLCH1 (12) vs lines expressing it (38) | 2.16× lower at baseline in the lines without PLCH1 | 0.065 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[CARD14]] | B | PLCH1 activity raises CARD14's level | lines that do not express PLCH1 (12) vs lines expressing it (38) | 1.61× lower at baseline in the lines without PLCH1 | 0.067 | ⚠ within organs, on part of the lines; maybe low, not absent |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.758). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (26.6, 51.3); signed map (58.4, 1.5). **Vector** length 106, 29.3% of its response variance represented; |z| ≥ 3 in 1,014 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +4.9 | +7.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.1 | +4.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +3.9 | +6.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.7 | +3.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.3 | +6.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.1 | +5.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.8 | +3.4 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +2.7 | +4.6 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -4.7 | -6.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.2 | -3.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.0 | -2.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.7 | -5.9 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -2.5 | -5.2 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -2.1 | -3.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.1 | -1.6 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.1 | -3.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.0 | -5.1 |

## What is on record

|  |  |
|---|---|
| Name | phospholipase C eta 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q25.31 — chr3:155,375,580-155,745,071 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1069, MGC117152, DKFZp434C1372, PLCeta1; previously PLCL3 |
| Gene groups (HGNC) | Phospholipases; C2 domain containing phospholipases; EF-hand domain containing |
| Reactome | 2 pathways, smallest: Synthesis of IP3 and IP4 in the cytosol; Inositol phosphate metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q4KWH8](https://www.uniprot.org/uniprotkb/Q4KWH8) (1-phosphatidylinositol 4,5-bisphosphate phosphodiesterase eta-1):

> The production of the second messenger molecules diacylglycerol (DAG) and inositol 1,4,5-trisphosphate (IP3) is mediated by calcium-activated phosphatidylinositol-specific phospholipase C enzymes.

**Summary**, from NCBI Gene [23007](https://www.ncbi.nlm.nih.gov/gene/23007):

> PLCH1 is a member of the PLC-eta family of the phosphoinositide-specific phospholipase C (PLC) superfamily of enzymes that cleave phosphatidylinositol 4,5-bisphosphate (PtdIns(4,5)P2) to generate second messengers inositol 1,4,5-trisphosphate (IP3) and diacylglycerol (DAG) (Hwang et al., 2005 [PubMed 15702972]).[supplied by OMIM, Jun 2009]

**Accessions** — [HGNC:29185](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29185) · Entrez [23007](https://www.ncbi.nlm.nih.gov/gene/23007) · UniProt [Q4KWH8](https://www.uniprot.org/uniprotkb/Q4KWH8) · Ensembl [ENSG00000114805](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000114805)

## Data

Gene col 3591: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3591); `tables/drug_effects.parquet` (55 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3591, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3591]; `tensor/DDL_lfc|DDL_z.npy` [3591]; `embed/gene_vectors.npy` [3591]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3591 or target_col == 3591). Every well: [[PLCH1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLCH1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
