---
symbol: "DENND2A"
type: "gene"
col: 7137
ensembl_id: "ENSG00000146966"
name: "DENN domain containing 2A"
location: "7q34"
module: 13
arm: "+"
pooled_cpm: 11.53
n_lines_expressing: 27
n_dd_up: 15
n_dd_down: 17
n_dd_up_clean: 11
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 29
direction_downstream: 37
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# DENND2A

*DENN domain containing 2A* — 7q34

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.01× (z +22.2, q 0e+00, up in 10 of 23 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (8 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.542× (z -8.7, q 2e-15, down in 19 of 25 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COL5A1]] (+0.76, fdr 7e-06), [[LINC01615]] (+0.75, fdr 7e-06), [[APCDD1L]] (+0.73, fdr 7e-06); moves opposite to [[SSTR2]] (-0.53, fdr 4e-05), [[INPP4B]] (-0.47, fdr 1e-04), [[RPSAP58]] (-0.47, fdr 5e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 29 arrows point to it, the strongest [[SSTR2]] → it (grade B ⚠); 37 go from it, the strongest it → [[SSC5D]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 5 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7137.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.01×** | +22.2 | 0e+00 | 10/23 (A498, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.40×** | +20.3 | 0e+00 | 1/9 (A498) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.35×** | +17.2 | 0e+00 | 6/17 (HEC-1-A, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.63×** | +12.7 | 9e-35 | 2/12 (HEC-1-A, A498) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.87×** | +8.9 | 7e-17 | 5/25 (BT-474, LoVo, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.54×** | +5.9 | 4e-07 | 4/22 (HEC-1-A, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +5.6 | 2e-06 | 3/22 (HEC-1-A, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.27×** | +4.9 | 8e-05 | 9/23 (LoVo, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Verteporfin (drug)]] 5 µM |  | **1.35×** | +4.1 | 0.002 | 2/24 (A498, NCI-H23) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.20× | +3.6 | 0.017 | 4/25 (A498, HEC-1-A, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.28×** | +3.5 | 0.023 | 5/25 (SNU-423, J82, …) | all doses, flat |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.41×** | +3.5 | 0.025 | 6/22 (A-172, RPMI-7951, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | 1.19× | +3.4 | 0.026 | 2/24 (LoVo, C-33 A) | top dose only | low cells (technical?) |
| [[Bimatoprost (drug)]] 0.5 µM |  | **1.26×** | +3.3 | 0.038 | 0/23 | inconsistent across doses |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.26×** | +3.1 | 0.074 | 4/23 (A498, HOP62, …) | inconsistent across doses |  |
| [[Larotrectinib (drug)]] 0.5 µM |  | **1.23×** | +3.0 | 0.092 | 0/24 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 8 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7137.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.542×** | -8.7 | 2e-15 | 19/25 (hTERT-HPNE, HOP62, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.591×** | -7.5 | 2e-11 | 17/25 (SNU-423, SK-MEL-2, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.603×** | -7.2 | 1e-10 | 17/25 (SNU-423, A-172, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.633×** | -6.5 | 1e-08 | 18/25 (SNU-423, RPMI-7951, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.664×** | -5.8 | 6e-07 | 14/25 (SNU-423, A-172, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.675×** | -5.4 | 7e-06 | 13/23 (SNU-423, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.704×** | -5.0 | 5e-05 | 12/24 (hTERT-HPNE, HS-578T, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.711×** | -4.8 | 9e-05 | 12/25 (RPMI-7951, PANC-1, …) | inconsistent across doses | composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **0.703×** | -4.8 | 9e-05 | 14/25 (HOP62, SNU-423, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.741×** | -4.3 | 0.001 | 8/24 (HOP62, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.758×** | -3.9 | 0.004 | 10/20 (SNU-423, J82, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.594×** | -3.9 | 0.005 | 11/23 (hTERT-HPNE, HOP62, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.785×** | -3.4 | 0.025 | 11/25 (SNU-423, HS-578T, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **0.791×** | -3.3 | 0.036 | 14/21 (hTERT-HPNE, RPMI-7951, …) | all doses, flat |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.655×** | -3.1 | 0.063 | 6/22 (HS-578T, SNU-423, …) | rises with dose | noisy plate (z scaled) |
| [[(S)-Crizotinib (drug)]] 0.05 µM |  | **0.791×** | -3.1 | 0.068 | 4/25 (LoVo, A498, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7137. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-423 (line)]] | alt | 91.3 | 0 | 17 (11 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0485× (z -24.3) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.120× (z -24.0) |
| [[RPMI-7951 (line)]] | alt | 112 | 0 | 15 (8 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0941× (z -17.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.238× (z -15.1) |
| [[hTERT-HPNE (line)]] | wt | 36.8 | 0 | 12 (8 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0257× (z -16.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0628× (z -12.2) |
| [[HOP62 (line)]] | alt | 31.2 | 0 | 11 (7 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.112× (z -13.7) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.122× (z -12.6) |
| [[PANC-1 (line)]] | alt | 12.1 | 0 | 11 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -14.1) |
| [[HS-578T (line)]] | alt | 47.2 | 0 | 10 (6 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.117× (z -13.0) |
| [[SK-MEL-2 (line)]] | alt | 27.7 | 0 | 10 (7 ⚠) | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0693× (z -13.6) |
| [[J82 (line)]] | alt | 34.0 | 0 | 9 (6 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.155× (z -13.5) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.313× (z -12.3) |
| [[A-172 (line)]] | wt | 41.1 | 0 | 8 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0750× (z -19.6) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.181× (z -18.3) |
| [[A498 (line)]] | wt | 3.70 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.94× (z +10.6) | — |
| [[HEC-1-A (line)]] | alt | 6.68 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0649× (z -12.4) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 1.90 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.80 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.66 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.09 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.14 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 5.97 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.58 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 8.30 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.31 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.27 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.13 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.21 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.40 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 4.17 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.34 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.82 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.79 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.81 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.55 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.74 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 9.88 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.23 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.01 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.94 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.81 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.19 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.48 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 43.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.81 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.40 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 2.32 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.48 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.19 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7137), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COL5A1]] | +0.76 | +0.74 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[LINC01615]] | +0.75 | +0.77 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[APCDD1L]] | +0.73 | +0.77 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[COL6A3]] | +0.71 | +0.68 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[NAV1]] | +0.70 | +0.68 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[GPR173]] | +0.69 | +0.58 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[IPO9-AS1]] | +0.66 | +0.63 / +0.70 | both halves | 7e-06 |  |
| [[SARDH]] | +0.66 | +0.64 / +0.59 | both halves | 7e-06 | **novel candidate** |
| [[ADAMTS2]] | +0.66 | +0.69 / +0.54 | both halves | 1e-05 | **novel candidate** |
| [[FAM20C]] | +0.64 | +0.58 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[CSPG4]] | +0.64 | +0.67 / +0.55 | both halves | 1e-05 |  |
| [[WNT5B]] | +0.62 | +0.52 / +0.65 | both halves | 1e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SSTR2]] | -0.53 | -0.59 / -0.42 | both halves | 4e-05 |  |
| [[INPP4B]] | -0.47 | -0.59 / -0.33 | both halves | 1e-04 |  |
| [[RPSAP58]] | -0.47 | -0.43 / -0.39 | both halves | 5e-05 |  |
| [[ICA1]] | -0.46 | -0.57 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*29 arrows, 29 of them with an alert ⚠; grade A 0, B 7, C 22. Shown: the 12 strongest; 17 more arrows (17 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SSTR2]] | B | SSTR2 activity raises DENND2A's level | lines that do not express SSTR2 (25) vs lines expressing it (25) | 3.12× lower at baseline in the lines without SSTR2 | 0.013 | ⚠ within organs, on part of the lines; also absent: PPP2R2B, DKK3, ENSG00000260517 |
| [[ZNF439]] | B | ZNF439 activity raises DENND2A's level | lines that do not express ZNF439 (21) vs lines expressing it (29) | 2.60× lower at baseline in the lines without ZNF439 | 0.022 | ⚠ within organs, on part of the lines; also absent: ENSG00000267383, PPP2R2B, CSF1R |
| [[DKK3]] | B | DKK3 activity raises DENND2A's level | lines that do not express DKK3 (29) vs lines expressing it (21) | 2.41× lower at baseline in the lines without DKK3 | 0.060 | ⚠ within organs, on part of the lines; also absent: COL5A1, ABI3BP, IDO1 |
| [[GPR173]] | B | GPR173 activity raises DENND2A's level | lines that do not express GPR173 (30) vs lines expressing it (20) | 2.35× lower at baseline in the lines without GPR173 | 0.062 | ⚠ within organs, on part of the lines; also absent: ITGA11, LUM, IRAG2 |
| [[SSC5D]] | B | SSC5D activity raises DENND2A's level | lines that do not express SSC5D (11) vs lines expressing it (39) | 2.71× lower at baseline in the lines without SSC5D | 0.062 | ⚠ within organs, on part of the lines; also absent: GXYLT2, SLC17A7, GNAZ; maybe low, not absent |
| [[DIRAS3]] | B | DIRAS3 activity raises DENND2A's level | lines that do not express DIRAS3 (44) vs lines expressing it (6) | 2.78× lower at baseline in the lines without DIRAS3 | 0.066 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000230258, MTND1P23, APOB |
| [[CYGB]] | B | CYGB activity raises DENND2A's level | lines that do not express CYGB (20) vs lines expressing it (30) | 2.15× lower at baseline in the lines without CYGB | 0.083 | ⚠ within organs, on part of the lines; also absent: ENSG00000269547, RNF175, FBXO17; maybe low, not absent |
| [[CSPG4]] | C | CSPG4 activity raises DENND2A's level | lines that do not express CSPG4 (31) vs lines expressing it (19) | 3.14× lower at baseline in the lines without CSPG4 | 0.002 | ⚠ within organs, on part of the lines; also absent: MMP2, PCDH18, AEBP1; co-absent with the target |
| [[PDGFRB]] | C | PDGFRB activity raises DENND2A's level | lines that do not express PDGFRB (36) vs lines expressing it (14) | 5.04× lower at baseline in the lines without PDGFRB | 0.003 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: COL3A1, ALPK2, GREM2; co-absent with the target |
| [[MIR493HG]] | C | MIR493HG activity raises DENND2A's level | lines that do not express MIR493HG (36) vs lines expressing it (14) | 2.89× lower at baseline in the lines without MIR493HG | 0.007 | ⚠ within organs, on part of the lines; also absent: MEG3, MEG8, ENSG00000232252; co-absent with the target |
| [[LAMA4]] | C | LAMA4 activity raises DENND2A's level | lines that do not express LAMA4 (27) vs lines expressing it (23) | 2.81× lower at baseline in the lines without LAMA4 | 0.007 | ⚠ within organs, on part of the lines; also absent: SLFN12, ARMCX1, BAALC; co-absent with the target |
| [[ADAMTS2]] | C | ADAMTS2 activity raises DENND2A's level | lines that do not express ADAMTS2 (29) vs lines expressing it (21) | 3.59× lower at baseline in the lines without ADAMTS2 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ZNF667, ZNF667-AS1, COL3A1; co-absent with the target |

### Downstream of this gene

*37 arrows, 37 of them with an alert ⚠; grade A 0, B 16, C 21. Shown: the 12 strongest; 25 more arrows (25 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SSC5D]] | B | DENND2A activity raises SSC5D's level | lines that do not express DENND2A (23) vs lines expressing it (27) | 2.41× lower at baseline in the lines without DENND2A | 0.002 | ⚠ within organs, on part of the lines; also absent: PTPRN, SPARC, BAALC; maybe low, not absent |
| [[TRPC1]] | B | DENND2A activity raises TRPC1's level | lines that do not express DENND2A (23) vs lines expressing it (27) | 2.04× lower at baseline in the lines without DENND2A | 0.021 | ⚠ within organs, on part of the lines; also absent: PTPRN, SPARC, BAALC; maybe low, not absent |
| [[PLEKHG4B]] | B | DENND2A activity raises PLEKHG4B's level | lines that do not express DENND2A (23) vs lines expressing it (27) | 2.51× lower at baseline in the lines without DENND2A | 0.035 | ⚠ within organs, on part of the lines; also absent: PTPRN, SPARC, BAALC; maybe low, not absent |
| [[CYGB]] | B | DENND2A activity raises CYGB's level | lines that do not express DENND2A (23) vs lines expressing it (27) | 1.85× lower at baseline in the lines without DENND2A | 0.053 | ⚠ within organs, on part of the lines; also absent: PTPRN, SPARC, BAALC; maybe low, not absent |
| [[IPO9-AS1]] | B | DENND2A activity raises IPO9-AS1's level | lines that do not express DENND2A (23) vs lines expressing it (27) | 1.61× lower at baseline in the lines without DENND2A | 0.053 | ⚠ within organs, on part of the lines; also absent: PTPRN, SPARC, BAALC; maybe low, not absent |
| [[COL23A1]] | B | DENND2A activity raises COL23A1's level | lines that do not express DENND2A (23) vs lines expressing it (27) | 1.79× lower at baseline in the lines without DENND2A | 0.055 | ⚠ within organs, on part of the lines; also absent: PTPRN, SPARC, BAALC; maybe low, not absent |
| [[C2orf92]] | B | DENND2A activity raises C2orf92's level | lines that do not express DENND2A (23) vs lines expressing it (27) | 1.90× lower at baseline in the lines without DENND2A | 0.067 | ⚠ within organs, on part of the lines; also absent: PTPRN, SPARC, BAALC; maybe low, not absent |
| [[THBS2-AS1]] | B | DENND2A activity raises THBS2-AS1's level | lines that do not express DENND2A (23) vs lines expressing it (27) | 1.53× lower at baseline in the lines without DENND2A | 0.072 | ⚠ within organs, on part of the lines; also absent: PTPRN, SPARC, BAALC; maybe low, not absent |
| cells under [[Peretinoin (drug)]] 5 µM | B | DENND2A activity lowers the cells' numbers under Peretinoin 5 µM (makes them more sensitive) | lines that do not express DENND2A (23) vs lines expressing it (25) | the lines without DENND2A: 1.17× the cells of the other lines | 0.084 | ⚠ within organs, on part of the lines; also absent: PTPRN, SPARC, BAALC; maybe low, not absent |
| [[TMEM45A]] | B | DENND2A activity raises TMEM45A's level | lines that do not express DENND2A (23) vs lines expressing it (27) | 3.27× lower at baseline in the lines without DENND2A | 0.085 | ⚠ within organs, on part of the lines; also absent: PTPRN, SPARC, BAALC; maybe low, not absent |
| [[NAV1]] | B | DENND2A activity raises NAV1's level | lines that do not express DENND2A (23) vs lines expressing it (27) | 3.39× lower at baseline in the lines without DENND2A | 0.085 | ⚠ within organs, on part of the lines; also absent: PTPRN, SPARC, BAALC; maybe low, not absent |
| [[ARMCX2]] | B | DENND2A activity raises ARMCX2's level | lines that do not express DENND2A (23) vs lines expressing it (27) | 1.99× lower at baseline in the lines without DENND2A | 0.089 | ⚠ within organs, on part of the lines; also absent: PTPRN, SPARC, BAALC; maybe low, not absent |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.717). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (53.2, 17.8); signed map (25.3, 46.8). **Vector** length 78.4, 20.2% of its response variance represented; |z| ≥ 3 in 831 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Signaling by PDGF* (reactome, mean cos +0.55 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.6 | +20.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.6 | +12.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.4 | +17.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.3 | +8.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.1 | +22.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +3.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.4 | +4.1 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.3 | +3.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.2 | +3.5 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.2 | -8.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.9 | -7.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -1.8 | -5.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | -2.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | -1.5 | -4.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.5 | -3.1 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.3 | -1.5 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.2 | -2.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.2 | -0.8 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.1 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | DENN domain containing 2A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q34 — chr7:140,518,420-140,673,993 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FAM31D; previously KIAA1277 |
| Gene groups (HGNC) | DENN domain containing |
| Reactome | 4 pathways, smallest: RAB GEFs exchange GTP for GDP on RABs; Rab regulation of trafficking; Membrane Trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9ULE3](https://www.uniprot.org/uniprotkb/Q9ULE3) (DENN domain-containing protein 2A):

> Guanine nucleotide exchange factor (GEF) which may activate RAB9A and RAB9B. Promotes the exchange of GDP to GTP, converting inactive GDP-bound Rab proteins into their active GTP-bound form. May play a role in late endosomes back to trans-Golgi network/TGN transport.

**Summary**, from NCBI Gene [27147](https://www.ncbi.nlm.nih.gov/gene/27147):

> Enables guanyl-nucleotide exchange factor activity. Involved in retrograde transport, endosome to Golgi. Located in actin cytoskeleton. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:22212](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:22212) · Entrez [27147](https://www.ncbi.nlm.nih.gov/gene/27147) · UniProt [Q9ULE3](https://www.uniprot.org/uniprotkb/Q9ULE3) · Ensembl [ENSG00000146966](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000146966)

## Data

Gene col 7137: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7137); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7137, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7137]; `tensor/DDL_lfc|DDL_z.npy` [7137]; `embed/gene_vectors.npy` [7137]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7137 or target_col == 7137). Every well: [[DENND2A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DENND2A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
