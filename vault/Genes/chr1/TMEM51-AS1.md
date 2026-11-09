---
symbol: "TMEM51-AS1"
type: "gene"
col: 10568
ensembl_id: "ENSG00000175147"
name: "TMEM51 antisense RNA 1"
location: "1p36.21"
module: 8
arm: "+"
pooled_cpm: 7.45
n_lines_expressing: 37
n_dd_up: 4
n_dd_down: 23
n_dd_up_clean: 4
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 44
direction_downstream: 22
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# TMEM51-AS1

*TMEM51 antisense RNA 1* — 1p36.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.92× (z +10.0, q 1e-20, up in 17 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.372× (z -15.1, q 0e+00, down in 26 of 30 measured lines) ⚠ cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.394× (z -10.0, q 2e-21, down in 24 of 29 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SMIM2-AS1]] (+0.65, fdr 7e-06), [[TMEM51]] (+0.62, fdr 1e-05, ⚠ same locus), [[LASTR]] (+0.59, fdr 1e-05), [[ERBB3]] (+0.58, fdr 2e-05); moves opposite to [[DCLK2]] (-0.52, fdr 1e-05).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 44 arrows point to it, the strongest [[ERBB3]] → it (grade B ⚠); 22 go from it, the strongest it → [[TMEM51]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10568.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.92×** | +10.0 | 1e-20 | 17/30 (SW480, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.43×** | +3.8 | 0.043 | 8/31 (CFPAC-1, KATO III, …) | inconsistent across doses | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.26×** | +3.6 | 0.063 | 9/32 (SW480, A-172, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.38×** | +3.5 | 0.063 | 7/31 (SW480, HepG2/C3A, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | 1.36× | +3.2 | 0.14 | 0/11 | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | 1.34× | +3.2 | 0.14 | 11/32 (PANC-1, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Tirabrutinib (drug)]] 0.5 µM |  | 1.33× | +3.1 | 0.16 | 2/33 (Panc 03.27, CFPAC-1) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~64% of this change | 1.32× | +3.0 | 0.18 | 5/33 (A-427, HT-29, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 9 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10568.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.372×** | -15.1 | 0e+00 | 26/30 (SK-MEL-2, CFPAC-1, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.377×** | -10.5 | 2e-23 | 25/33 (COLO 205, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.394×** | -10.0 | 2e-21 | 24/29 (LoVo, COLO 205, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.391×** | -9.7 | 3e-20 | 26/31 (SK-MEL-2, CFPAC-1, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.404×** | -9.6 | 1e-19 | 25/31 (COLO 205, C32, …) | two highest doses | cell-cycle shift (explains ~24% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.416×** | -9.3 | 2e-18 | 23/31 (LoVo, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.424×** | -9.2 | 2e-18 | 21/31 (SK-MEL-2, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.508×** | -7.3 | 2e-11 | 19/34 (Panc 03.27, SK-MEL-2, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **0.511×** | -7.2 | 3e-11 | 23/29 (HepG2/C3A, HEC-1-A, …) | two highest doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | **0.518×** | -6.8 | 6e-10 | 18/26 (Panc 03.27, CFPAC-1, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.329×** | -6.3 | 2e-08 | 20/30 (LoVo, SK-MEL-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.572×** | -5.9 | 2e-07 | 20/32 (Panc 03.27, SK-MEL-2, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.579×** | -5.9 | 2e-07 | 15/32 (C32, A549, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.574×** | -5.9 | 2e-07 | 18/31 (SK-MEL-2, A-427, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.643×** | -4.7 | 7e-05 | 12/33 (HOP62, A-427, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.627×** | -4.7 | 7e-05 | 17/31 (HOP62, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.685×** | -4.1 | 0.002 | 9/32 (Panc 03.27, HEC-1-A, …) | top dose only |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.694×** | -3.8 | 0.005 | 7/32 (Panc 03.27, CFPAC-1, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.814×** | -3.1 | 0.053 | 8/32 (CFPAC-1, SK-MEL-2, …) | top dose only |  |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM |  | **0.747×** | -3.0 | 0.072 | 12/31 (H4, C32, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.749×** | -3.0 | 0.074 | 7/31 (NCI-H23, NCI-H2030, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.592×** | -3.0 | 0.078 | 9/30 (A549, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.30 per unit of S-phase module lfc, -0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10568. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Panc 03.27 (line)]] | alt | 41.6 | 0 | 12 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -17.5) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.305× (z -11.5) |
| [[CFPAC-1 (line)]] | alt | 42.5 | 0 | 11 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0769× (z -23.0) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.167× (z -11.3) |
| [[SK-MEL-2 (line)]] | alt | 45.4 | 0 | 10 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0764× (z -24.2) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.178× (z -11.2) |
| [[COLO 205 (line)]] | alt | 28.7 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0828× (z -17.5) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0628× (z -13.7) |
| [[C32 (line)]] | wt | 9.39 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.178× (z -9.0) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0923× (z -8.8) |
| [[HEC-1-A (line)]] | alt | 13.8 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -11.2) ⚠ cell-cycle shift, explains ~33% of this change |
| [[LoVo (line)]] | wt | 7.13 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0443× (z -15.7) |
| [[A-427 (line)]] | wt | 11.2 | 0 | 2 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0902× (z -11.1) |
| [[HepG2_C3A (line)]] | wt | 23.1 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0361× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[HOP62 (line)]] | alt | 8.77 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.119× (z -13.7) ⚠ cell-cycle shift, explains ~33% of this change |
| [[HT-29 (line)]] | alt | 5.12 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0638× (z -9.5) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0660× (z -9.2) |
| [[HCT15 (line)]] | alt | 21.1 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.148× (z -8.6) ⚠ cell-cycle shift, explains ~31% of this change |
| [[KATO III (line)]] | alt | 8.51 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -9.2) ⚠ cell-cycle shift, explains ~33% of this change |
| [[LS 180 (line)]] | wt | 7.44 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -11.1) ⚠ cell-cycle shift, explains ~33% of this change |
| [[NCI-H1573 (line)]] | alt | 4.01 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0617× (z -9.9) |
| [[NCI-H2030 (line)]] | alt | 2.66 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0670× (z -8.7) ⚠ cell-cycle shift, explains ~31% of this change |
| [[NCI-H23 (line)]] | alt | 3.59 | 0 | 1 | — | [[Auranofin (drug)]] 0.5 µM 0.0630× (z -8.5) |
| [[NCI-H2347 (line)]] | alt | 6.95 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.214× (z -10.3) ⚠ cell-cycle shift, explains ~33% of this change |
| [[SW1417 (line)]] | alt | 7.88 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 0.05 µM 0.0801× (z -9.6) |
| [[A-172 (line)]] | wt | 3.41 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.21 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.95 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.28 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.85 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.54 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.81 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.15 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.02 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 4.24 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.60 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.77 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.65 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.35 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 6.04 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.73 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.20 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.899 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 6.67 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.57 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.11 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 4.00 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.52 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.64 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 5.86 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.33 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10568), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMIM2-AS1]] | +0.65 | +0.62 / +0.60 | both halves | 7e-06 | same gene group |
| [[TMEM51]] | +0.62 | +0.57 / +0.66 | both halves | 1e-05 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[LASTR]] | +0.59 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[ERBB3]] | +0.58 | +0.63 / +0.47 | both halves | 2e-05 |  |
| [[ADCY4]] | +0.58 | +0.53 / +0.46 | both halves | 2e-05 |  |
| [[SLC44A4]] | +0.57 | +0.61 / +0.46 | both halves | 3e-05 |  |
| [[TMC4]] | +0.56 | +0.59 / +0.41 | both halves | 4e-05 |  |
| [[ST14]] | +0.55 | +0.58 / +0.45 | both halves | 3e-05 |  |
| [[SLC44A3-AS1]] | +0.54 | +0.59 / +0.38 | both halves | 7e-05 | same gene group |
| [[SHROOM4]] | +0.54 | +0.53 / +0.48 | both halves | 2e-05 | **novel candidate** |
| [[ADGRF1]] | +0.54 | +0.59 / +0.46 | both halves | 3e-05 |  |
| [[TACSTD2]] | +0.53 | +0.44 / +0.35 | both halves | 1e-04 |  |
| [[KLHL2P1]] | +0.53 | +0.51 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DCLK2]] | -0.52 | -0.50 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*44 arrows, 44 of them with an alert ⚠; grade A 0, B 44, C 0. Shown: the 12 strongest; 32 more arrows (32 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ERBB3]] | B | ERBB3 activity raises TMEM51-AS1's level | lines that do not express ERBB3 (27) vs lines expressing it (23) | 2.73× lower at baseline in the lines without ERBB3 | 0.003 | ⚠ within organs, on part of the lines; also absent: LAD1, KDF1, EPCAM |
| [[HNF1B]] | B | HNF1B activity raises TMEM51-AS1's level | lines that do not express HNF1B (31) vs lines expressing it (19) | 2.23× lower at baseline in the lines without HNF1B | 0.006 | ⚠ within organs, on part of the lines; also absent: ENSG00000254261, PDZK1IP1, ADGRF1 |
| [[MAL2]] | B | MAL2 activity raises TMEM51-AS1's level | lines that do not express MAL2 (31) vs lines expressing it (19) | 2.62× lower at baseline in the lines without MAL2 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: RAB25, TMEM125, CDH1 |
| [[HSH2D]] | B | HSH2D activity raises TMEM51-AS1's level | lines that do not express HSH2D (27) vs lines expressing it (23) | 2.46× lower at baseline in the lines without HSH2D | 0.007 | ⚠ within organs, on part of the lines; also absent: LAD1, KDF1, EPCAM; maybe low, not absent |
| [[ESRP1]] | B | ESRP1 activity raises TMEM51-AS1's level | lines that do not express ESRP1 (31) vs lines expressing it (19) | 2.23× lower at baseline in the lines without ESRP1 | 0.008 | ⚠ within organs, on part of the lines; also absent: ST14, KDF1, CLDN7 |
| [[TC2N]] | B | TC2N activity raises TMEM51-AS1's level | lines that do not express TC2N (28) vs lines expressing it (22) | 1.87× lower at baseline in the lines without TC2N | 0.009 | ⚠ within organs, on part of the lines; also absent: CATSPERB, ESRP1, ST14 |
| [[SLC44A4]] | B | SLC44A4 activity raises TMEM51-AS1's level | lines that do not express SLC44A4 (37) vs lines expressing it (13) | 2.64× lower at baseline in the lines without SLC44A4 | 0.009 | ⚠ within organs, on part of the lines; also absent: ST6GALNAC1, LCN2, NPSR1 |
| [[TMPRSS4]] | B | TMPRSS4 activity raises TMEM51-AS1's level | lines that do not express TMPRSS4 (33) vs lines expressing it (17) | 2.29× lower at baseline in the lines without TMPRSS4 | 0.010 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B |
| [[CDH1]] | B | CDH1 activity raises TMEM51-AS1's level | lines that do not express CDH1 (31) vs lines expressing it (19) | 2.36× lower at baseline in the lines without CDH1 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ST14, LAD1, KDF1 |
| [[PROM1]] | B | PROM1 activity raises TMEM51-AS1's level | lines that do not express PROM1 (37) vs lines expressing it (13) | 2.94× lower at baseline in the lines without PROM1 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: AZGP1, KRT23, GJB1 |
| [[B3GNT7]] | B | B3GNT7 activity raises TMEM51-AS1's level | lines that do not express B3GNT7 (31) vs lines expressing it (19) | 2.45× lower at baseline in the lines without B3GNT7 | 0.013 | ⚠ within organs, on part of the lines; also absent: KRT23, PROM1, HSD17B2 |
| [[FUT3]] | B | FUT3 activity raises TMEM51-AS1's level | lines that do not express FUT3 (29) vs lines expressing it (21) | 1.83× lower at baseline in the lines without FUT3 | 0.013 | ⚠ within organs, on part of the lines; also absent: ATP2C2, TMEM125, ENSG00000243004 |

### Downstream of this gene

*22 arrows, 22 of them with an alert ⚠; grade A 0, B 22, C 0. Shown: the 12 strongest; 10 more arrows (10 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMEM51]] | B | TMEM51-AS1 activity raises TMEM51's level | lines that do not express TMEM51-AS1 (13) vs lines expressing it (37) | 2.68× lower at baseline in the lines without TMEM51-AS1 | 0.001 | ⚠ within organs, on part of the lines; also absent: RAB17, PLEKHG1, EPHA1; maybe low, not absent |
| [[TMC4]] | B | TMEM51-AS1 activity raises TMC4's level | lines that do not express TMEM51-AS1 (13) vs lines expressing it (37) | 3.15× lower at baseline in the lines without TMEM51-AS1 | 0.010 | ⚠ within organs, on part of the lines; also absent: RAB17, PLEKHG1, EPHA1; maybe low, not absent |
| [[PRRG2]] | B | TMEM51-AS1 activity raises PRRG2's level | lines that do not express TMEM51-AS1 (13) vs lines expressing it (37) | 1.98× lower at baseline in the lines without TMEM51-AS1 | 0.021 | ⚠ within organs, on part of the lines; also absent: RAB17, PLEKHG1, EPHA1; maybe low, not absent |
| [[EPCAM-DT]] | B | TMEM51-AS1 activity raises EPCAM-DT's level | lines that do not express TMEM51-AS1 (13) vs lines expressing it (37) | 2.63× lower at baseline in the lines without TMEM51-AS1 | 0.024 | ⚠ within organs, on part of the lines; also absent: RAB17, PLEKHG1, EPHA1; maybe low, not absent |
| [[ESRP1]] | B | TMEM51-AS1 activity raises ESRP1's level | lines that do not express TMEM51-AS1 (13) vs lines expressing it (37) | 4.32× lower at baseline in the lines without TMEM51-AS1 | 0.045 | ⚠ within organs, on part of the lines; also absent: RAB17, PLEKHG1, EPHA1; maybe low, not absent |
| [[SLC44A3]] | B | TMEM51-AS1 activity raises SLC44A3's level | lines that do not express TMEM51-AS1 (13) vs lines expressing it (37) | 2.13× lower at baseline in the lines without TMEM51-AS1 | 0.049 | ⚠ within organs, on part of the lines; also absent: RAB17, PLEKHG1, EPHA1; maybe low, not absent |
| [[CLDN7]] | B | TMEM51-AS1 activity raises CLDN7's level | lines that do not express TMEM51-AS1 (13) vs lines expressing it (37) | 3.14× lower at baseline in the lines without TMEM51-AS1 | 0.054 | ⚠ within organs, on part of the lines; also absent: RAB17, PLEKHG1, EPHA1; maybe low, not absent |
| [[BCL2L15]] | B | TMEM51-AS1 activity raises BCL2L15's level | lines that do not express TMEM51-AS1 (13) vs lines expressing it (37) | 1.81× lower at baseline in the lines without TMEM51-AS1 | 0.057 | ⚠ within organs, on part of the lines; also absent: RAB17, PLEKHG1, EPHA1; maybe low, not absent |
| [[CDH1]] | B | TMEM51-AS1 activity raises CDH1's level | lines that do not express TMEM51-AS1 (13) vs lines expressing it (37) | 4.44× lower at baseline in the lines without TMEM51-AS1 | 0.059 | ⚠ within organs, on part of the lines; also absent: RAB17, PLEKHG1, EPHA1; maybe low, not absent |
| [[TNFRSF14-AS1]] | B | TMEM51-AS1 activity raises TNFRSF14-AS1's level | lines that do not express TMEM51-AS1 (13) vs lines expressing it (37) | 1.70× lower at baseline in the lines without TMEM51-AS1 | 0.062 | ⚠ within organs, on part of the lines; also absent: RAB17, PLEKHG1, EPHA1; maybe low, not absent |
| [[B3GNT7]] | B | TMEM51-AS1 activity raises B3GNT7's level | lines that do not express TMEM51-AS1 (13) vs lines expressing it (37) | 1.62× lower at baseline in the lines without TMEM51-AS1 | 0.069 | ⚠ within organs, on part of the lines; also absent: RAB17, PLEKHG1, EPHA1; maybe low, not absent |
| [[MROH7]] | B | TMEM51-AS1 activity raises MROH7's level | lines that do not express TMEM51-AS1 (13) vs lines expressing it (37) | 2.00× lower at baseline in the lines without TMEM51-AS1 | 0.070 | ⚠ within organs, on part of the lines; also absent: RAB17, PLEKHG1, EPHA1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.589). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (23.8, 57.0); signed map (58.4, 5.3). **Vector** length 68.1, 14.1% of its response variance represented; |z| ≥ 3 in 877 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.4 | +10.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +3.8 | +0.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +3.6 | -2.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.4 | +3.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.2 | +3.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.4 | +1.4 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.2 | +0.5 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.2 | +1.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.1 | +1.0 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.9 | -10.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -2.3 | -9.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | -2.8 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.6 | -1.0 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.5 | +0.1 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.3 | -0.6 |
|  | [[Gemcitabine (drug)]] 0.05 µM |  | -1.2 | -2.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.2 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | TMEM51 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 1p36.21 — chr1:15,111,815-15,153,618 (-) |
| Ensembl biotype | lncRNA |
| Also known as | FLJ23703; previously C1orf126 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:26301](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26301) · Entrez [200197](https://www.ncbi.nlm.nih.gov/gene/200197) · Ensembl [ENSG00000175147](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175147)

## Data

Gene col 10568: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10568); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10568, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10568]; `tensor/DDL_lfc|DDL_z.npy` [10568]; `embed/gene_vectors.npy` [10568]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10568 or target_col == 10568). Every well: [[TMEM51-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM51-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
