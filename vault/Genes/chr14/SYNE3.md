---
symbol: "SYNE3"
type: "gene"
col: 10719
ensembl_id: "ENSG00000176438"
name: "spectrin repeat containing nuclear envelope family member 3"
location: "14q32.13"
module: 31
arm: "+"
pooled_cpm: 27.09
n_lines_expressing: 39
n_dd_up: 12
n_dd_down: 41
n_dd_up_clean: 11
n_dd_down_clean: 34
in_vector_space: true
direction_upstream: 3
direction_downstream: 9
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# SYNE3

*spectrin repeat containing nuclear envelope family member 3* — 14q32.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.50× (z +8.4, q 2e-14, up in 16 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 41 drug-doses (7 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.441× (z -12.0, q 2e-30, down in 24 of 37 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[VASP]] (+0.63, fdr 1e-05), [[PTPRN2]] (+0.57, fdr 1e-05), [[LINC02320]] (+0.55, fdr 1e-05); moves opposite to [[ZNF148]] (-0.44, fdr 1e-04), [[MTUS1-DT]] (-0.41, fdr 5e-05), [[LXN]] (-0.41, fdr 1e-04).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[PIWIL1]] → it (grade B ⚠); 9 go from it, the strongest it → [[PPARG]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 2 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10719.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.50×** | +8.4 | 2e-14 | 16/35 (J82, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +7.5 | 2e-11 | 16/36 (BT-474, A549, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.39×** | +4.8 | 3e-04 | 14/37 (NCI-H460, BT-474, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.26×** | +4.8 | 3e-04 | 17/37 (NCI-H460, BT-474, …) | rises with dose |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | 1.19× | +3.7 | 0.026 | 17/37 (BT-474, KATO III, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.28×** | +3.6 | 0.029 | 13/36 (Hs 766T, AsPC-1, …) | all doses, flat |  |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM |  | 1.18× | +3.5 | 0.037 | 5/37 (LoVo, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.05 µM |  | **1.26×** | +3.4 | 0.051 | 4/37 (PANC-1, A-427, …) | inconsistent across doses | position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.26×** | +3.4 | 0.051 | 8/36 (NCI-H460, RPMI-7951, …) | inconsistent across doses | low cells (technical?) |
| [[Clobetasol propionate (drug)]] 5 µM |  | **1.25×** | +3.3 | 0.057 | 10/37 (Hs 766T, AsPC-1, …) | all doses, flat |  |
| [[Budesonide (drug)]] 5 µM |  | **1.23×** | +3.1 | 0.096 | 10/37 (Hs 766T, AsPC-1, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **1.23×** | +3.1 | 0.096 | 8/37 (KATO III, SW480, …) | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.23×** | +3.0 | 0.099 | 13/36 (LOX-IMVI, HCT15, …) | inconsistent across doses |  |
| [[Naproxen (drug)]] 0.05 µM |  | **1.25×** | +3.0 | 0.099 | 7/36 (LOX-IMVI, SW 1271, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 45 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 41 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10719.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.441×** | -12.0 | 2e-30 | 24/37 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.590×** | -10.9 | 2e-25 | 31/37 (SW1417, SW480, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.515×** | -9.7 | 5e-20 | 28/35 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.522×** | -9.5 | 2e-19 | 26/36 (LS 180, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.530×** | -9.3 | 1e-18 | 23/36 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.547×** | -8.8 | 9e-17 | 26/37 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.554×** | -8.6 | 4e-16 | 25/37 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.632×** | -6.7 | 1e-09 | 23/37 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.637×** | -6.6 | 3e-09 | 23/37 (MIA PaCa-2, LS 180, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.644×** | -6.5 | 6e-09 | 21/36 (LoVo, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~14% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.453×** | -6.1 | 7e-08 | 22/37 (LS 180, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.651×** | -5.9 | 1e-07 | 25/37 (SW480, AN3 CA, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.673×** | -5.8 | 3e-07 | 21/37 (SW480, LoVo, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.726×** | -5.8 | 3e-07 | 21/37 (LoVo, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.675×** | -5.8 | 3e-07 | 19/37 (HepG2/C3A, SW480, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.670×** | -5.5 | 1e-06 | 20/36 (LoVo, SW480, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.697×** | -5.3 | 4e-06 | 20/37 (LoVo, SW480, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10719. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 70.3 | 0 | 19 (6 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.131× (z -18.7) |
| [[SW480 (line)]] | alt | 153 | 0 | 19 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.121× (z -20.3) |
| [[LS 180 (line)]] | wt | 102 | 0 | 15 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -15.8) |
| [[KATO III (line)]] | alt | 38.8 | 0 | 8 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.155× (z -11.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.174× (z -10.8) |
| [[HepG2_C3A (line)]] | wt | 42.5 | 0 | 7 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.106× (z -12.8) ⚠ toxic; cell-cycle shift, explains ~8% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.207× (z -9.6) |
| [[PANC-1 (line)]] | alt | 20.1 | 1 | 6 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +9.9) | [[Digitoxin (drug)]] 5 µM 0.273× (z -11.3) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.274× (z -11.2) |
| [[MIA PaCa-2 (line)]] | alt | 18.3 | 0 | 4 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.132× (z -11.0) |
| [[C32 (line)]] | wt | 41.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0826× (z -16.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.426× (z -8.6) |
| [[H4 (line)]] | wt | 51.5 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.117× (z -10.8) |
| [[Hs 766T (line)]] | wt | 31.7 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0996× (z -12.6) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.306× (z -9.2) |
| [[NCI-H1792 (line)]] | alt | 23.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +9.4) | [[Adagrasib (drug)]] 0.05 µM 0.557× (z -11.9) ⚠ position not correctable |
| [[NCI-H2030 (line)]] | alt | 29.5 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.285× (z -10.3) |
| [[NCI-H460 (line)]] | wt | 20.0 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.186× (z -12.5) ⚠ cell-cycle shift, explains ~57% of this change |
| [[Panc 03.27 (line)]] | alt | 30.1 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.181× (z -10.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.261× (z -8.6) |
| [[A549 (line)]] | wt | 8.35 | 0 | 1 | — | [[Naproxen (drug)]] 0.05 µM 0.0880× (z -9.8) |
| [[AsPC-1 (line)]] | alt | 16.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -10.5) |
| [[BT-474 (line)]] | alt | 9.98 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.36× (z +11.4) | — |
| [[COLO 205 (line)]] | alt | 11.5 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.0936× (z -9.4) |
| [[HS-578T (line)]] | alt | 19.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0584× (z -15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[J82 (line)]] | alt | 9.04 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.96× (z +9.9) | — |
| [[LOX-IMVI (line)]] | wt | 15.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.142× (z -11.1) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 18.8 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.304× (z -11.0) |
| [[SW48 (line)]] | wt | 12.8 | 0 | 1 | — | [[Fulvestrant (drug)]] 0.5 µM 0.0777× (z -9.5) |
| [[A-172 (line)]] | wt | 6.95 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 8.45 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.83 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.16 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.76 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.43 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.69 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 35.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.22 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.27 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.25 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.33 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.04 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.47 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 6.05 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 17.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10719), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VASP]] | +0.63 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[PTPRN2]] | +0.57 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[LINC02320]] | +0.55 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[ANO1]] | +0.55 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[MYEOV]] | +0.54 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[ITGB4]] | +0.54 | +0.53 / +0.53 | both halves | 1e-05 | STRING 685 |
| [[PPARG]] | +0.53 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[ONECUT3]] | +0.53 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[TNS4]] | +0.53 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[TRABD2A]] | +0.53 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[CACNA2D4]] | +0.52 | +0.49 / +0.51 | both halves | 2e-05 |  |
| [[RAPH1]] | +0.52 | +0.55 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF148]] | -0.44 | -0.36 / -0.43 | both halves | 1e-04 |  |
| [[MTUS1-DT]] | -0.41 | -0.40 / -0.43 | both halves | 5e-05 |  |
| [[LXN]] | -0.41 | -0.34 / -0.39 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PIWIL1]] | B | PIWIL1 activity raises SYNE3's level | lines that do not express PIWIL1 (38) vs lines expressing it (12) | 2.21× lower at baseline in the lines without PIWIL1 | 0.065 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TFF2, CALB1, CLRN3 |
| [[PPARG]] | B | PPARG activity raises SYNE3's level | lines that do not express PPARG (20) vs lines expressing it (30) | 1.67× lower at baseline in the lines without PPARG | 0.068 | ⚠ within organs, on part of the lines; also absent: ENSG00000271933, LINC01589, NUP62CL |
| [[NPAS2]] | B | NPAS2 activity raises SYNE3's level | lines that do not express NPAS2 (7) vs lines expressing it (43) | 2.40× lower at baseline in the lines without NPAS2 | 0.080 | ⚠ within organs, on part of the lines |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 9, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PPARG]] | B | SYNE3 activity raises PPARG's level | lines that do not express SYNE3 (11) vs lines expressing it (39) | 2.51× lower at baseline in the lines without SYNE3 | 0.018 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[BTBD19]] | B | SYNE3 activity raises BTBD19's level | lines that do not express SYNE3 (11) vs lines expressing it (39) | 1.68× lower at baseline in the lines without SYNE3 | 0.026 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[EXTL2]] | B | SYNE3 activity lowers EXTL2's level | lines that do not express SYNE3 (11) vs lines expressing it (39) | 1.55× higher at baseline in the lines without SYNE3 | 0.055 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[ITGA6]] | B | SYNE3 activity raises ITGA6's level | lines that do not express SYNE3 (11) vs lines expressing it (39) | 2.21× lower at baseline in the lines without SYNE3 | 0.062 | ⚠ within organs, on part of the lines; maybe low, not absent |
| cells under [[Dinaciclib (drug)]] 5 µM | B | SYNE3 activity raises the cells' numbers under Dinaciclib 5 µM (protects the cells) | lines that do not express SYNE3 (11) vs lines expressing it (37) | the lines without SYNE3: 0.44× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[ANO1]] | B | SYNE3 activity raises ANO1's level | lines that do not express SYNE3 (11) vs lines expressing it (39) | 2.66× lower at baseline in the lines without SYNE3 | 0.074 | ⚠ within organs, on part of the lines; maybe low, not absent |
| cells under [[Dinaciclib (drug)]] 0.5 µM | B | SYNE3 activity raises the cells' numbers under Dinaciclib 0.5 µM (protects the cells) | lines that do not express SYNE3 (11) vs lines expressing it (37) | the lines without SYNE3: 0.42× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; maybe low, not absent |
| cells under [[Dinaciclib (drug)]] 0.05 µM | B | SYNE3 activity raises the cells' numbers under Dinaciclib 0.05 µM (protects the cells) | lines that do not express SYNE3 (11) vs lines expressing it (37) | the lines without SYNE3: 0.52× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[ITGB4]] | B | SYNE3 activity raises ITGB4's level | lines that do not express SYNE3 (11) vs lines expressing it (39) | 3.81× lower at baseline in the lines without SYNE3 | 0.086 | ⚠ within organs, on part of the lines; maybe low, not absent |

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.429). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.4, 50.0); signed map (6.9, 36.1). **Vector** length 108, 27.1% of its response variance represented; |z| ≥ 3 in 1,248 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +5.6 | +8.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.5 | +7.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.3 | +4.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.0 | +4.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +3.4 | +0.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.5 | -1.5 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +2.1 | +2.0 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | +2.0 | +2.5 |
|  | [[Betamethasone dipropionate (drug)]] 0.05 µM |  | +2.0 | +2.6 |
| fall | [[Selinexor (drug)]] 5 µM |  | -6.4 | -10.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -5.0 | -4.4 |
|  | [[Trametinib (drug)]] 5 µM |  | -4.7 | -4.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.3 | -5.8 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -4.2 | -5.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | -4.1 | -4.9 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -3.8 | -4.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.7 | -5.3 |

## What is on record

|  |  |
|---|---|
| Name | spectrin repeat containing nuclear envelope family member 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q32.13 — chr14:95,407,266-95,516,650 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ25605, NET53, Nesprin-3, Nesp3; previously C14orf49, LINC00341, C14orf139, NCRNA00341 |
| Gene groups (HGNC) | Spectrin repeat containing nuclear envelope family; KASH domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6ZMZ3](https://www.uniprot.org/uniprotkb/Q6ZMZ3) (Nesprin-3):

> As a component of the LINC (LInker of Nucleoskeleton and Cytoskeleton) complex involved in the connection between the nuclear lamina and the cytoskeleton. The nucleocytoplasmic interactions established by the LINC complex play an important role in the transmission of mechanical forces across the nuclear envelope and in nuclear movement and positioning. Probable anchoring protein which tethers the nucleus to the cytoskeleton by binding PLEC which can associate with the intermediate filament …

**Summary**, from NCBI Gene [161176](https://www.ncbi.nlm.nih.gov/gene/161176):

> Enables actin filament binding activity and cytoskeleton-nuclear membrane anchor activity. Involved in cytoskeleton organization; establishment of protein localization to membrane; and regulation of cell shape. Located in nuclear membrane. Part of meiotic nuclear membrane microtubule tethering complex. Biomarker of Huntington's disease. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:19861](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19861) · Entrez [161176](https://www.ncbi.nlm.nih.gov/gene/161176) · UniProt [Q6ZMZ3](https://www.uniprot.org/uniprotkb/Q6ZMZ3) · Ensembl [ENSG00000176438](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000176438)

## Data

Gene col 10719: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10719); `tables/drug_effects.parquet` (59 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10719, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10719]; `tensor/DDL_lfc|DDL_z.npy` [10719]; `embed/gene_vectors.npy` [10719]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10719 or target_col == 10719). Every well: [[SYNE3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SYNE3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
