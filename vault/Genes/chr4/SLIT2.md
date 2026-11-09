---
symbol: "SLIT2"
type: "gene"
col: 6960
ensembl_id: "ENSG00000145147"
name: "slit guidance ligand 2"
location: "4p15.31"
module: 183
arm: "+"
pooled_cpm: 76.87
n_lines_expressing: 30
n_dd_up: 25
n_dd_down: 12
n_dd_up_clean: 21
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 14
direction_downstream: 9
tags: ["gene", "module/183"]
generated_by: "tahoemap"
---

# SLIT2

*slit guidance ligand 2* — 4p15.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 7.12× (z +35.9, q 0e+00, up in 25 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[Dexamethasone (drug)]] 5 µM: 0.661× (z -5.4, q 5e-05, down in 16 of 28 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ADAMTS1]] (+0.65, fdr 7e-06), [[PCDH17]] (+0.61, fdr 7e-06), [[PTHLH]] (+0.61, fdr 3e-05); moves opposite to [[FRG1DP]] (-0.60, fdr 2e-05), [[ARNT]] (-0.59, fdr 2e-05), [[COPS8]] (-0.58, fdr 1e-05).
> It is in [[Module 183]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 14 arrows point to it, the strongest [[IRAK3]] → it (grade B ⚠); 9 go from it, the strongest it → [[PMAIP1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 4 with an alert ⚠; shown: the 15 strongest. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6960.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **7.12×** | +35.9 | 0e+00 | 25/29 (NCI-H460, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **5.61×** | +31.5 | 0e+00 | 24/28 (C32, HOP62, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **5.00×** | +20.8 | 0e+00 | 23/28 (C32, NCI-H460, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **5.28×** | +20.7 | 0e+00 | 25/28 (HEC-1-A, A-172, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.57×** | +17.3 | 0e+00 | 24/28 (A-172, HOP62, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **3.96×** | +17.1 | 0e+00 | 26/30 (HEC-1-A, C32, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.20×** | +15.1 | 0e+00 | 24/28 (C32, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.18×** | +14.2 | 5e-44 | 22/28 (NCI-H460, SW1417, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **2.87×** | +13.6 | 1e-40 | 25/28 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.59×** | +12.3 | 6e-33 | 23/28 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.15×** | +9.9 | 3e-21 | 20/28 (A498, NCI-H460, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.10×** | +9.6 | 3e-20 | 22/28 (SNU-423, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.91×** | +8.4 | 3e-15 | 19/29 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.84×** | +7.9 | 1e-13 | 19/28 (C32, A-172, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.84×** | +7.6 | 2e-12 | 17/28 (C32, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 1 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6960.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dexamethasone (drug)]] 5 µM |  | **0.661×** | -5.4 | 5e-05 | 16/28 (A-172, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.671×** | -5.2 | 7e-05 | 14/28 (A-172, HS-578T, …) | all doses, stronger at high dose |  |
| [[Budesonide (drug)]] 5 µM |  | **0.739×** | -3.9 | 0.013 | 15/28 (A-172, H4, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.739×** | -3.9 | 0.013 | 14/28 (A-172, HOP62, …) | all doses, flat |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **0.761×** | -3.5 | 0.046 | 11/28 (A-172, HS-578T, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.777×** | -3.3 | 0.089 | 13/28 (A-172, hTERT-HPNE, …) | all doses, flat |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.624×** | -3.2 | 0.089 | 16/29 (RPMI-7951, CHP-212, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.783×** | -3.2 | 0.089 | 12/28 (A-172, H4, …) | two highest doses |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.784×** | -3.1 | 0.089 | 11/28 (A-172, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **0.785×** | -3.1 | 0.089 | 16/27 (HOP62, NCI-H1792, …) | all doses, flat |  |
| [[OTS514 (drug)]] 0.05 µM | ⚠ transcription drop | **0.774×** | -3.1 | 0.089 | 4/28 (LoVo, HOP62, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.787×** | -3.1 | 0.095 | 14/28 (A-172, Hs 766T, …) | all doses, flat |  |
| [[Carbamazepine (drug)]] 0.5 µM |  | 0.793× | -3.0 | 0.12 | 9/28 (SW 1271, HEC-1-A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.30 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6960. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 79.5 | 11 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.44× (z +24.3) | [[Clobetasol propionate (drug)]] 0.5 µM 0.254× (z -11.7) |
| [[C32 (line)]] | wt | 78.3 | 13 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 39.7× (z +27.4) | — |
| [[NCI-H460 (line)]] | wt | 23.4 | 13 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.6× (z +26.8) | — |
| [[CFPAC-1 (line)]] | alt | 42.8 | 11 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.8× (z +19.6) | — |
| [[BT-474 (line)]] | alt | 23.4 | 8 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 18.9× (z +20.1) | [[Harringtonine (drug)]] 0.05 µM 0.0652× (z -12.2) |
| [[LOX-IMVI (line)]] | wt | 36.0 | 9 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.1× (z +20.8) | — |
| [[A498 (line)]] | wt | 23.6 | 8 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.60× (z +19.1) | — |
| [[HOP62 (line)]] | alt | 199 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.62× (z +24.4) | — |
| [[SNU-423 (line)]] | alt | 60.3 | 8 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 12.9× (z +16.8) | — |
| [[C-33 A (line)]] | alt | 2,407 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0914× (z -22.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~82% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.381× (z -13.1) |
| [[H4 (line)]] | wt | 60.0 | 6 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.09× (z +12.1) | — |
| [[HS-578T (line)]] | alt | 48.1 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.51× (z +17.7) | — |
| [[LoVo (line)]] | wt | 25.9 | 5 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.96× (z +22.9) | [[Dinaciclib (drug)]] 5 µM 0.231× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~82% of this change |
| [[NCI-H2347 (line)]] | alt | 26.5 | 6 | 0 | [[Auranofin (drug)]] 5 µM 19.1× (z +14.8) | — |
| [[HEC-1-A (line)]] | alt | 59.4 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.11× (z +24.6) | — |
| [[Panc 03.27 (line)]] | alt | 36.2 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.54× (z +15.9) | — |
| [[SW 900 (line)]] | alt | 68.6 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.09× (z +12.2) | — |
| [[hTERT-HPNE (line)]] | wt | 304 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.51× (z +19.1) | — |
| [[SW1417 (line)]] | alt | 31.8 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.13× (z +13.7) | — |
| [[NCI-H1792 (line)]] | alt | 128 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.22× (z +23.0) | — |
| [[Hs 766T (line)]] | wt | 39.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.18× (z +11.3) | — |
| [[J82 (line)]] | alt | 341 | 1 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 4.10× (z +11.3) | — |
| [[RPMI-7951 (line)]] | alt | 296 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +9.0) | — |
| [[SHP-77 (line)]] | alt | 56.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.81× (z +11.1) | — |
| [[A-427 (line)]] | wt | 8.40 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 6.00 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 16.2 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 7.30 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 329 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.97 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 6.88 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 11.3 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 9.84 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 5.91 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 6.73 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.06 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 18.3 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 6.76 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.0 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 501 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.79 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 6.87 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.3 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 7.71 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 64.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.79 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 10.2 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6960), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*56 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADAMTS1]] | +0.65 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[PCDH17]] | +0.61 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[PTHLH]] | +0.61 | +0.44 / +0.61 | both halves | 3e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[LINC01828]] | +0.59 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[CUBN]] | +0.59 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[NEK10]] | +0.58 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[HBEGF]] | +0.57 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[ADAMTSL1]] | +0.57 | +0.54 / +0.57 | both halves | 1e-05 | same gene group |
| [[TBILA]] | +0.57 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[CLDN11]] | +0.57 | +0.52 / +0.45 | both halves | 3e-05 | same gene group; pathway: HALLMARK_APICAL_JUNCTION |
| [[RFX3]] | +0.56 | +0.61 / +0.45 | both halves | 3e-05 |  |
| [[CFAP299]] | +0.56 | +0.55 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*44 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FRG1DP]] | -0.60 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[ARNT]] | -0.59 | -0.61 / -0.48 | both halves | 2e-05 |  |
| [[COPS8]] | -0.58 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[GEMIN2]] | -0.58 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[VPS33B]] | -0.57 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[MINDY3]] | -0.55 | -0.60 / -0.33 | both halves | 1e-04 |  |
| [[SUGT1P4-STRA6LP]] | -0.55 | -0.53 / -0.33 | both halves | 1e-04 |  |
| [[ZNF230]] | -0.54 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[CCZ1]] | -0.54 | -0.58 / -0.46 | both halves | 3e-05 |  |
| [[EDEM2]] | -0.54 | -0.52 / -0.43 | both halves | 3e-05 |  |
| [[CDK5RAP1]] | -0.54 | -0.55 / -0.43 | both halves | 3e-05 |  |
| [[STRA6LP]] | -0.53 | -0.48 / -0.36 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 8, C 6. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IRAK3]] | B | IRAK3 activity raises SLIT2's level | lines that do not express IRAK3 (36) vs lines expressing it (14) | 2.44× lower at baseline in the lines without IRAK3 | 0.007 | ⚠ within organs, on part of the lines; also absent: IRAG2, TRBC2, CXCL5 |
| [[CXCL5]] | B | CXCL5 activity raises SLIT2's level | lines that do not express CXCL5 (35) vs lines expressing it (15) | 2.32× lower at baseline in the lines without CXCL5 | 0.019 | ⚠ within organs, on part of the lines; also absent: ANXA10, IRAK3, TRBC2 |
| [[TOP2A]] | B | TOP2A activity lowers SLIT2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MBP]] | B | MBP activity lowers SLIT2's level | lines that do not express MBP (9) vs lines expressing it (41) | 5.86× higher at baseline in the lines without MBP | 0.031 | ⚠ within organs, on part of the lines; co-occurs with PTEN; also absent: RHPN1, CHMP4C, EVPL |
| [[KCNIP4]] | B | KCNIP4 activity raises SLIT2's level | lines that do not express KCNIP4 (6) vs lines expressing it (44) | 4.24× lower at baseline in the lines without KCNIP4 | 0.040 | ⚠ within organs, on part of the lines; also absent: MLLT3, TEX9, MAMDC2-AS1; maybe low, not absent |
| [[OFCC1]] | B | OFCC1 activity raises SLIT2's level | lines that do not express OFCC1 (14) vs lines expressing it (36) | 2.93× lower at baseline in the lines without OFCC1 | 0.057 | ⚠ within organs, on part of the lines; also absent: PDLIM3, CAMK4, GLRB; maybe low, not absent |
| [[PCED1B]] | B | PCED1B activity raises SLIT2's level | lines that do not express PCED1B (11) vs lines expressing it (39) | 1.99× lower at baseline in the lines without PCED1B | 0.069 | ⚠ within organs, on part of the lines; also absent: AMIGO2, CXCL3, PRDM1 |
| [[SUSD1]] | B | SUSD1 activity raises SLIT2's level | lines that do not express SUSD1 (6) vs lines expressing it (44) | 1.33× lower at baseline in the lines without SUSD1 | 0.094 | ⚠ within organs, on part of the lines; also absent: ETS2, TCIRG1, SDC4; maybe low, not absent |
| [[PMAIP1]] | C | PMAIP1 activity strengthens SLIT2's drug response | lines that do not express PMAIP1 (3) vs lines expressing it (27) | the lines without PMAIP1 respond the other way (z diff +4.65); strongest at Idarubicin (hydrochloride) 5 µM: 0.98x vs 5.05x (z diff +8.3) | 0.025 | ⚠ few lines (4 vs 46); across organs; also absent: DOCK5, STAMBPL1, PERP; maybe low, not absent; target measured in part of the lines; the reference differs; artifact flags |
| [[CDH2]] | C | CDH2 activity raises SLIT2's level | lines that do not express CDH2 (22) vs lines expressing it (28) | 3.85× lower at baseline in the lines without CDH2 | 0.029 | ⚠ within organs, on part of the lines; also absent: ARMCX1, DKK3, RFTN1; co-absent with the target |
| [[HHIP]] | C | HHIP activity raises SLIT2's level | lines that do not express HHIP (33) vs lines expressing it (17) | 3.93× lower at baseline in the lines without HHIP | 0.051 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: COL5A1, PLPP4, LINC01411; maybe low, not absent; co-absent with the target |
| [[TOX]] | C | TOX activity raises SLIT2's level | lines that do not express TOX (30) vs lines expressing it (20) | 4.26× lower at baseline in the lines without TOX | 0.053 | ⚠ within organs, on part of the lines; also absent: CDH6, DKK3, MXRA5; co-absent with the target |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 4, C 5.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PMAIP1]] | B | SLIT2 activity raises PMAIP1's level | lines that do not express SLIT2 (20) vs lines expressing it (30) | 1.97× lower at baseline in the lines without SLIT2 | 7e-04 | ⚠ within organs, on part of the lines; also absent: CHSY3, MOXD1, IDO1 |
| [[NEGR1]] | B | SLIT2 activity strengthens NEGR1's drug response | lines that do not express SLIT2 (5) vs lines expressing it (19) | the lines without SLIT2 respond the other way (z diff +4.01); strongest at Epirubicin (hydrochloride) 5 µM: 0.50x vs 1.50x (z diff +5.8) | 0.051 | ⚠ within organs, on part of the lines; also absent: CHSY3, MOXD1, IDO1; target measured in part of the lines; artifact flags |
| [[PTHLH]] | B | SLIT2 activity raises PTHLH's level | lines that do not express SLIT2 (20) vs lines expressing it (30) | 2.15× lower at baseline in the lines without SLIT2 | 0.057 | ⚠ within organs, on part of the lines; also absent: CHSY3, MOXD1, IDO1 |
| [[LINC00536]] | B | SLIT2 activity raises LINC00536's level | lines that do not express SLIT2 (20) vs lines expressing it (30) | 2.47× lower at baseline in the lines without SLIT2 | 0.067 | ⚠ within organs, on part of the lines; also absent: CHSY3, MOXD1, IDO1 |
| [[RORB]] | C | SLIT2 activity raises RORB's level | lines that do not express SLIT2 (20) vs lines expressing it (30) | 2.66× lower at baseline in the lines without SLIT2 | 0.043 | ⚠ within organs, on part of the lines; also absent: CHSY3, MOXD1, IDO1; co-absent with the target |
| [[LBH]] | C | SLIT2 activity raises LBH's level | lines that do not express SLIT2 (20) vs lines expressing it (30) | 2.48× lower at baseline in the lines without SLIT2 | 0.063 | ⚠ within organs, on part of the lines; also absent: CHSY3, MOXD1, IDO1; co-absent with the target |
| [[HHIP]] | C | SLIT2 activity raises HHIP's level | lines that do not express SLIT2 (20) vs lines expressing it (30) | 2.30× lower at baseline in the lines without SLIT2 | 0.091 | ⚠ within organs, on part of the lines; also absent: CHSY3, MOXD1, IDO1; co-absent with the target |
| [[LYPD1]] | C | SLIT2 activity raises LYPD1's level | lines that do not express SLIT2 (20) vs lines expressing it (30) | 2.15× lower at baseline in the lines without SLIT2 | 0.093 | ⚠ within organs, on part of the lines; also absent: CHSY3, MOXD1, IDO1; co-absent with the target |
| [[CDH2]] | C | SLIT2 activity raises CDH2's level | lines that do not express SLIT2 (20) vs lines expressing it (30) | 4.79× lower at baseline in the lines without SLIT2 | 0.099 | ⚠ within organs, on part of the lines; also absent: CHSY3, MOXD1, IDO1; co-absent with the target |

## Where it sits

- **Module**: [[Module 183]]; 21 genes; every member is in the + arm (projection on the module's main direction -0.557). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.32; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (35.0, 29.1); signed map (37.5, 29.7). **Vector** length 100, 27.8% of its response variance represented; |z| ≥ 3 in 974 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.7 | +14.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.7 | +20.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +5.4 | +17.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.3 | +8.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.9 | +35.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.3 | +17.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.8 | +2.8 |
|  | [[Busulfan (drug)]] 0.05 µM |  | +1.7 | +2.3 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -4.0 | -5.2 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -3.7 | -2.0 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -3.7 | -5.4 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -3.6 | -3.2 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -3.4 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | slit guidance ligand 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p15.31 — chr4:20,251,905-20,620,561 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Slit-2; previously SLIL3 |
| Gene groups (HGNC) | MicroRNA protein coding host genes; Slit guidance ligands |
| Hallmark sets | APICAL_JUNCTION, EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 12 pathways, smallest: SLIT2:ROBO1 increases RHOA activity; Inactivation of CDC42 and RAC1; Role of ABL in ROBO-SLIT signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [O94813](https://www.uniprot.org/uniprotkb/O94813) (Slit homolog 2 protein):

> Thought to act as molecular guidance cue in cellular migration, and function appears to be mediated by interaction with roundabout homolog receptors. During neural development involved in axonal navigation at the ventral midline of the neural tube and projection of axons to different regions. SLIT1 and SLIT2 seem to be essential for midline guidance in the forebrain by acting as repulsive signal preventing inappropriate midline crossing by axons projecting from the olfactory bulb. In spinal …

**Summary**, from NCBI Gene [9353](https://www.ncbi.nlm.nih.gov/gene/9353):

> This gene encodes a member of the slit family of secreted glycoproteins, which are ligands for the Robo family of immunoglobulin receptors. Slit proteins play highly conserved roles in axon guidance and neuronal migration and may also have functions during other cell migration processes including leukocyte migration. Members of the slit family are characterized by an N-terminal signal peptide, four leucine-rich repeats, nine epidermal growth factor repeats, and a C-terminal cysteine knot. …

**Accessions** — [HGNC:11086](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11086) · Entrez [9353](https://www.ncbi.nlm.nih.gov/gene/9353) · UniProt [O94813](https://www.uniprot.org/uniprotkb/O94813) · Ensembl [ENSG00000145147](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000145147)

## Data

Gene col 6960: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6960); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6960, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6960]; `tensor/DDL_lfc|DDL_z.npy` [6960]; `embed/gene_vectors.npy` [6960]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6960 or target_col == 6960). Every well: [[SLIT2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLIT2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
