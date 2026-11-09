---
symbol: "WDR27"
type: "gene"
col: 11540
ensembl_id: "ENSG00000184465"
name: "WD repeat domain 27"
location: "6q27"
module: 5
arm: "+"
pooled_cpm: 87.74
n_lines_expressing: 49
n_dd_up: 5
n_dd_down: 19
n_dd_up_clean: 3
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# WDR27

*WD repeat domain 27* — 6q27

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 1.43× (z +5.6, q 1e-05, up in 42 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (14 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.411× (z -9.8, q 5e-20, down in 41 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.523× (z -7.2, q 1e-10, down in 41 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IPO4]] (+0.64, fdr 9e-06), [[SPRY4-AS1]] (+0.62, fdr 1e-05), [[BRD9]] (+0.61, fdr 8e-06); moves opposite to [[GALM]] (-0.59, fdr 1e-05), [[KBTBD3]] (-0.58, fdr 1e-05), [[CCDC88B]] (-0.58, fdr 1e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[NCMAP]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11540.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.43×** | +5.6 | 1e-05 | 42/47 (NCI-H2030, CFPAC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.64×** | +5.5 | 1e-05 | 34/47 (AsPC-1, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.53×** | +4.5 | 0.001 | 34/47 (HT-29, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.27×** | +3.8 | 0.023 | 27/48 (HT-29, NCI-H1573, …) | rises with dose |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.38×** | +3.4 | 0.082 | 28/47 (MIA PaCa-2, SW480, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 14 with an alert ⚠; shown: the 15 strongest. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11540.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.411×** | -9.8 | 5e-20 | 41/47 (PANC-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.511×** | -7.4 | 3e-11 | 40/47 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.523×** | -7.2 | 1e-10 | 41/47 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.316×** | -6.7 | 3e-09 | 42/48 (SW 900, LOX-IMVI, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.549×** | -6.6 | 3e-09 | 36/47 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.691×** | -5.8 | 6e-07 | 26/47 (HEC-1-A, A549, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.589×** | -5.6 | 1e-06 | 33/46 (hTERT-HPNE, H4, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.608×** | -5.5 | 3e-06 | 37/47 (LOX-IMVI, PANC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **0.601×** | -5.4 | 4e-06 | 29/47 (SK-MEL-2, HEC-1-A, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.520×** | -5.3 | 6e-06 | 32/48 (NCI-H23, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~22% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.615×** | -5.1 | 2e-05 | 38/47 (J82, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.642×** | -4.5 | 3e-04 | 24/44 (NCI-H23, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~12% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.671×** | -4.4 | 4e-04 | 31/47 (PANC-1, NCI-H23, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.512×** | -3.9 | 0.004 | 28/47 (A-427, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.696×** | -3.9 | 0.004 | 23/42 (SK-MEL-2, C-33 A, …) | all doses, flat | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, -0.65 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11540. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 166 | 0 | 7 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.214× (z -14.6) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.397× (z -8.8) |
| [[A-427 (line)]] | wt | 103 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.376× (z -12.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.114× (z -10.3) |
| [[NCI-H23 (line)]] | alt | 135 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0791× (z -16.5) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 75.0 | 0 | 4 (4 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0656× (z -16.4) ⚠ toxic |
| [[J82 (line)]] | alt | 94.8 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.388× (z -10.7) ⚠ cell-cycle shift, would explain all of this change |
| [[SK-MEL-2 (line)]] | alt | 149 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.110× (z -18.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[SW480 (line)]] | alt | 105 | 0 | 4 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.265× (z -11.8) ⚠ cell-cycle shift, explains ~36% of this change |
| [[H4 (line)]] | wt | 70.0 | 0 | 3 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0714× (z -14.6) ⚠ toxic |
| [[HEC-1-A (line)]] | alt | 103 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -13.6) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 83.2 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -11.9) ⚠ cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 38.7 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.397× (z -9.5) ⚠ cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 77.4 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.320× (z -13.2) ⚠ cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 119 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.315× (z -9.5) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 113 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.401× (z -9.0) ⚠ cell-cycle shift, would explain all of this change |
| [[KATO III (line)]] | alt | 107 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.269× (z -11.2) ⚠ cell-cycle shift, explains ~36% of this change |
| [[LoVo (line)]] | wt | 96.9 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.292× (z -11.8) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.405× (z -8.7) |
| [[LOX-IMVI (line)]] | wt | 82.4 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.212× (z -12.3) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 107 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.244× (z -11.4) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 64.8 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.304× (z -10.2) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 175 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.263× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[AsPC-1 (line)]] | alt | 40.1 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.26× (z +8.6) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[C-33 A (line)]] | alt | 128 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.141× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[HT-29 (line)]] | alt | 62.8 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.49× (z +10.6) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 195 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.221× (z -10.2) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 28.6 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.40× (z +8.7) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[NCI-H2030 (line)]] | alt | 36.3 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.203× (z -11.3) ⚠ toxic |
| [[SNU-1 (line)]] | wt | 80.6 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.167× (z -11.1) ⚠ toxic |
| [[SW 900 (line)]] | alt | 92.8 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.104× (z -8.6) |
| [[AN3 CA (line)]] | alt | 111 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 35.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 45.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 78.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 46.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 89.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 50.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 69.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 64.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 21.5 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 74.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 54.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 101 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 70.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 80.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 74.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 68.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 36.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11540), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IPO4]] | +0.64 | +0.63 / +0.57 | both halves | 9e-06 |  |
| [[SPRY4-AS1]] | +0.62 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[BRD9]] | +0.61 | +0.57 / +0.60 | both halves | 8e-06 |  |
| [[DOCK1]] | +0.60 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[ANKMY1]] | +0.60 | +0.68 / +0.48 | both halves | 2e-05 |  |
| [[IPO7]] | +0.58 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[HDAC4]] | +0.58 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[ZRANB3]] | +0.57 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[HMGA2]] | +0.56 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[NOLC1]] | +0.56 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[WDR4]] | +0.56 | +0.54 / +0.55 | both halves | 1e-05 | same gene group |
| [[GRWD1]] | +0.56 | +0.52 / +0.53 | both halves | 1e-05 | same gene group |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GALM]] | -0.59 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[KBTBD3]] | -0.58 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[CCDC88B]] | -0.58 | -0.57 / -0.51 | both halves | 1e-05 |  |
| [[ABHD8]] | -0.56 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[PLAAT3]] | -0.56 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[GDPD1]] | -0.54 | -0.43 / -0.46 | both halves | 4e-05 |  |
| [[IFNLR1]] | -0.54 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[KIAA1522]] | -0.53 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[USP30]] | -0.53 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[NRG4]] | -0.53 | -0.44 / -0.57 | both halves | 3e-05 |  |
| [[DBP]] | -0.52 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[AKAP1-DT]] | -0.51 | -0.44 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NCMAP]] | B | NCMAP activity lowers WDR27's level | lines that do not express NCMAP (26) vs lines expressing it (24) | 1.48× higher at baseline in the lines without NCMAP | 0.016 | ⚠ within organs, on part of the lines; also absent: TC2N, CRB3, SPINT1-AS1; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers WDR27's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 1.4% of all compounds | 0.026 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[LINC00482]] | B | LINC00482 activity weakens WDR27's drug response | lines that do not express LINC00482 (8) vs lines expressing it (40) | the lines without LINC00482 respond 1.46× as strongly (z diff -1.59); strongest at Homoharringtonine 5 µM: 0.44x vs 0.76x (z diff -5.3) | 0.057 | ⚠ within organs, on part of the lines; also absent: SOX13, SEPTIN9-DT; target measured in part of the lines; artifact flags |
| [[TOP2B]] | B | TOP2B activity lowers WDR27's level | compounds that target TOP2B: 2 of 2 raise it (Doxorubicin, Mitoxantrone) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[SLC2A12]] | B | SLC2A12 activity raises WDR27's level | lines that do not express SLC2A12 (10) vs lines expressing it (40) | 1.32× lower at baseline in the lines without SLC2A12 | 0.078 | ⚠ within organs, on part of the lines; also absent: IRAK2, IL22RA1, PLEKHG4; maybe low, not absent |
| [[GNG12-AS1]] | C | GNG12-AS1 activity raises WDR27's level | lines that do not express GNG12-AS1 (3) vs lines expressing it (47) | 2.06× lower at baseline in the lines without GNG12-AS1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: GALNT7, PARP11, DPP7; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.604). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (17.4, -0.3); signed map (2.2, -49.5). **Vector** length 85.8, 25.8% of its response variance represented; |z| ≥ 3 in 995 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.4 | +5.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.1 | +4.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.8 | +1.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.4 | +2.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.2 | +1.1 |
|  | [[BAY1125976 (drug)]] 5 µM |  | +2.0 | +2.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.9 | +1.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | +1.9 | +1.2 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.2 | +1.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -4.1 | +0.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.0 | +0.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -3.9 | -3.8 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -3.6 | -5.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.5 | +0.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.5 | -0.5 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.2 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | WD repeat domain 27 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q27 — chr6:169,457,212-169,702,067 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC43690 |
| Gene groups (HGNC) | WD repeat domain containing |
| Matched by | ensembl_id |

UniProt [A2RRH5](https://www.uniprot.org/uniprotkb/A2RRH5) carries no function annotation.

**Summary**, from NCBI Gene [253769](https://www.ncbi.nlm.nih.gov/gene/253769):

> This gene encodes a protein with multiple WD repeats. Proteins with these repeats may form scaffolds for protein-protein interaction and play key roles in cell signalling. Alternative splicing results in multiple transcript variants, but the full-length structure of some of these variants cannot be determined. [provided by RefSeq, Nov 2015]

**Accessions** — [HGNC:21248](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21248) · Entrez [253769](https://www.ncbi.nlm.nih.gov/gene/253769) · UniProt [A2RRH5](https://www.uniprot.org/uniprotkb/A2RRH5) · Ensembl [ENSG00000184465](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184465)

## Data

Gene col 11540: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11540); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11540, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11540]; `tensor/DDL_lfc|DDL_z.npy` [11540]; `embed/gene_vectors.npy` [11540]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11540 or target_col == 11540). Every well: [[WDR27 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WDR27.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
