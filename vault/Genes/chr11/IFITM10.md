---
symbol: "IFITM10"
type: "gene"
col: 14397
ensembl_id: "ENSG00000244242"
name: "interferon induced transmembrane protein 10"
location: "11p15.5"
module: 96
arm: "+"
pooled_cpm: 7.53
n_lines_expressing: 46
n_dd_up: 12
n_dd_down: 17
n_dd_up_clean: 8
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 5
direction_downstream: 4
tags: ["gene", "module/096"]
generated_by: "tahoemap"
---

# IFITM10

*interferon induced transmembrane protein 10* — 11p15.5

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.95× (z +6.3, q 1e-07, up in 19 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (9 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.411× (z -8.3, q 7e-14, down in 31 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CTSD]] (+0.55, fdr 2e-05, ⚠ read-through risk), [[PIP5KL1]] (+0.52, fdr 1e-05), [[AMDHD2]] (+0.52, fdr 2e-05), [[ZFAND5]] (+0.52, fdr 2e-05); moves opposite to [[TEX30]] (-0.49, fdr 5e-05), [[GSTCD]] (-0.47, fdr 9e-05), [[LRRC8C]] (-0.46, fdr 4e-05).
> It is in [[Module 096]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[EPS8L2]] → it (grade B ⚠); 4 go from it, the strongest it → [[CTSD]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14397.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.95×** | +6.3 | 1e-07 | 19/41 (SW480, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | **2.00×** | +6.2 | 2e-07 | 19/40 (SW480, LS 180, …) | inconsistent across doses | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.74×** | +5.2 | 3e-05 | 21/40 (HT-29, HEC-1-A, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.75×** | +5.1 | 4e-05 | 6/13 (C32, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.71×** | +5.1 | 5e-05 | 18/40 (LoVo, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.72×** | +4.7 | 2e-04 | 4/14 (NCI-H2347, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.63×** | +4.6 | 3e-04 | 15/40 (A549, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.60×** | +4.5 | 6e-04 | 16/41 (A549, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.48×** | +3.7 | 0.014 | 5/22 (HEC-1-A, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.47×** | +3.6 | 0.015 | 10/40 (A498, H4, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.44×** | +3.4 | 0.030 | 15/40 (HEC-1-A, LoVo, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.32×** | +3.1 | 0.088 | 4/41 (SK-MEL-2, CFPAC-1, …) | all doses, flat | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 9 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14397.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.411×** | -8.3 | 7e-14 | 31/40 (PANC-1, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.467×** | -7.2 | 2e-10 | 25/42 (HepG2/C3A, SK-MEL-2, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.506×** | -6.2 | 1e-07 | 22/40 (PANC-1, SW1417, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.566×** | -5.3 | 1e-05 | 21/40 (RPMI-7951, SK-MEL-2, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.583×** | -5.1 | 5e-05 | 21/39 (PANC-1, A549, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.594×** | -4.7 | 2e-04 | 18/40 (SW 900, SNU-423, …) | rises with dose | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.711×** | -4.5 | 5e-04 | 20/37 (PANC-1, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.640×** | -4.2 | 0.002 | 18/41 (PANC-1, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.645×** | -4.1 | 0.002 | 15/40 (LS 180, PANC-1, …) | all doses, flat |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.763×** | -3.6 | 0.018 | 16/41 (SK-MEL-2, SW 900, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change | **0.683×** | -3.6 | 0.018 | 19/35 (HT-29, LoVo, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.699×** | -3.4 | 0.035 | 16/41 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.690×** | -3.4 | 0.035 | 11/41 (MIA PaCa-2, CFPAC-1, …) | top dose only | position effect removed |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.701×** | -3.3 | 0.035 | 14/41 (RPMI-7951, PANC-1, …) | all doses, flat | position effect removed |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **0.694×** | -3.3 | 0.036 | 4/40 (LS 180, HEC-1-A, …) | top dose only | plate-row cell shift |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.704×** | -3.0 | 0.076 | 12/35 (J82, A549, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, -0.47 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14397. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 23.2 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0809× (z -21.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.276× (z -10.8) |
| [[HT-29 (line)]] | alt | 17.3 | 0 | 3 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0846× (z -13.0) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[RPMI-7951 (line)]] | alt | 13.1 | 0 | 3 (3 ⚠) | — | [[Daptomycin (drug)]] 0.5 µM 0.0375× (z -11.9) ⚠ unreliable plate only |
| [[LoVo (line)]] | wt | 4.23 | 0 | 2 | — | [[Cobimetinib (drug)]] 5 µM 0.0889× (z -9.0) |
| [[SW1417 (line)]] | alt | 10.7 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.126× (z -9.0) ⚠ cell-cycle shift, explains ~44% of this change |
| [[A498 (line)]] | wt | 23.6 | 1 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 5.67× (z +11.0) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[C32 (line)]] | wt | 10.5 | 0 | 1 | — | [[Bendamustine (drug)]] 5 µM 0.123× (z -8.8) |
| [[COLO 205 (line)]] | alt | 28.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -9.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HepG2_C3A (line)]] | wt | 4.63 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0390× (z -8.7) ⚠ cell-cycle shift, explains ~37% of this change |
| [[J82 (line)]] | alt | 7.53 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.08× (z +9.2) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[KATO III (line)]] | alt | 6.02 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0682× (z -10.3) ⚠ cell-cycle shift, explains ~49% of this change |
| [[NCI-H460 (line)]] | wt | 3.49 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.05× (z +12.3) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[Panc 03.27 (line)]] | alt | 4.68 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0556× (z -8.6) ⚠ cell-cycle shift, explains ~44% of this change |
| [[SK-MEL-2 (line)]] | alt | 16.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.173× (z -10.3) |
| [[SNU-423 (line)]] | alt | 11.3 | 0 | 1 | — | [[Orlistat (drug)]] 0.05 µM 0.0842× (z -9.2) |
| [[A-172 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.36 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.78 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.57 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 5.34 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.78 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 20.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.00 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.12 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.94 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.46 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.36 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.61 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.22 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.05 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.49 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.77 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.73 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.30 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 4.31 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.07 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.19 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.63 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14397), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CTSD]] | +0.55 | +0.48 / +0.60 | both halves | 2e-05 | STRING 404; ⚠ **readthrough risk**: this gene lies 2.2 kb 3′ of CTSD on the same strand (can correlate by spillover, not regulation) |
| [[PIP5KL1]] | +0.52 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[AMDHD2]] | +0.52 | +0.46 / +0.55 | both halves | 2e-05 |  |
| [[ZFAND5]] | +0.52 | +0.53 / +0.47 | both halves | 2e-05 |  |
| [[PBXIP1]] | +0.51 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[ZNF628]] | +0.49 | +0.47 / +0.38 | both halves | 6e-05 |  |
| [[NR1H2]] | +0.48 | +0.49 / +0.38 | both halves | 6e-05 |  |
| [[CYP4F3]] | +0.48 | +0.44 / +0.46 | both halves | 3e-05 |  |
| [[EPS8L2]] | +0.47 | +0.37 / +0.38 | both halves | 8e-05 |  |
| [[CACFD1]] | +0.47 | +0.39 / +0.41 | both halves | 5e-05 |  |
| [[AP5Z1]] | +0.47 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[DNM1]] | +0.47 | +0.40 / +0.46 | both halves | 5e-05 |  |
| [[SSH3]] | +0.47 | +0.41 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TEX30]] | -0.49 | -0.40 / -0.41 | both halves | 5e-05 |  |
| [[GSTCD]] | -0.47 | -0.37 / -0.46 | both halves | 9e-05 |  |
| [[LRRC8C]] | -0.46 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[TUBGCP5]] | -0.45 | -0.39 / -0.45 | both halves | 6e-05 |  |
| [[TMEM158]] | -0.45 | -0.41 / -0.44 | both halves | 4e-05 |  |
| [[FBXO45]] | -0.45 | -0.34 / -0.43 | both halves | 1e-04 |  |
| [[NEDD1]] | -0.44 | -0.38 / -0.48 | both halves | 6e-05 |  |
| [[BIVM]] | -0.44 | -0.43 / -0.36 | both halves | 9e-05 |  |
| [[ARMC1]] | -0.44 | -0.41 / -0.44 | both halves | 4e-05 |  |
| [[ACTL6A]] | -0.43 | -0.49 / -0.40 | both halves | 4e-05 |  |
| [[KATNBL1]] | -0.43 | -0.50 / -0.38 | both halves | 6e-05 |  |
| [[ADAMTS6]] | -0.43 | -0.47 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPS8L2]] | B | EPS8L2 activity raises IFITM10's level | lines that do not express EPS8L2 (19) vs lines expressing it (31) | 1.37× lower at baseline in the lines without EPS8L2 | 0.059 | ⚠ within organs, on part of the lines; also absent: KRT80, ITGB4, C19orf33; maybe low, not absent |
| [[SH3BP2]] | B | SH3BP2 activity raises IFITM10's level | lines that do not express SH3BP2 (8) vs lines expressing it (42) | 2.11× lower at baseline in the lines without SH3BP2 | 0.090 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[SERPINA5]] | B | SERPINA5 activity raises IFITM10's level | lines that do not express SERPINA5 (37) vs lines expressing it (13) | 1.35× lower at baseline in the lines without SERPINA5 | 0.094 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LINC02899, SERPINA1, ENSG00000286546 |
| [[PSMB5]] | B | PSMB5 activity lowers IFITM10's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[CTSD]] | C | CTSD activity raises IFITM10's level | lines that do not express CTSD (4) vs lines expressing it (46) | 2.61× lower at baseline in the lines without CTSD | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: IFITM10, SQOR, ST6GALNAC2; maybe low, not absent; co-absent with the target; its own permutation p |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 0, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CTSD]] | C | IFITM10 activity raises CTSD's level | lines that do not express IFITM10 (4) vs lines expressing it (46) | 3.11× lower at baseline in the lines without IFITM10 | 0.010 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CTSD, FLVCR2; maybe low, not absent; co-absent with the target |
| [[FADS3]] | C | IFITM10 activity raises FADS3's level | lines that do not express IFITM10 (4) vs lines expressing it (46) | 2.22× lower at baseline in the lines without IFITM10 | 0.027 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CTSD, FLVCR2; maybe low, not absent |
| [[WBP2]] | C | IFITM10 activity raises WBP2's level | lines that do not express IFITM10 (4) vs lines expressing it (46) | 1.61× lower at baseline in the lines without IFITM10 | 0.055 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CTSD, FLVCR2; maybe low, not absent |
| [[TUBA8]] | C | IFITM10's natural level weakens TUBA8's drug response | IFITM10's natural level across 42 lines (lineage-adjusted; a glimpse) | r -0.66, reverse -0.04; direction not clear | 0.097 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

## Where it sits

- **Module**: [[Module 096]]; 48 genes; every member is in the + arm (projection on the module's main direction 0.306). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (41.0, -21.2); signed map (-5.3, 21.5). **Vector** length 82.1, 16.0% of its response variance represented; |z| ≥ 3 in 1,053 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +4.0 | +5.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +3.3 | +5.1 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | +3.3 | +6.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.2 | +3.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.0 | +4.7 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +2.3 | +2.7 |
|  | [[crizotinib (drug)]] 5 µM |  | +1.9 | +2.7 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.9 | +1.8 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -4.5 | -8.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -3.7 | -1.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.4 | -5.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | -3.3 | -1.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -2.8 | -4.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.2 | -0.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.0 | -3.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.9 | -3.0 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.5 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | interferon induced transmembrane protein 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.5 — chr11:1,732,406-1,750,595 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DSPA3 |
| Gene groups (HGNC) | Interferon induced transmembrane protein family; Dispanins |
| Matched by | ensembl_id |

UniProt [A6NMD0](https://www.uniprot.org/uniprotkb/A6NMD0) carries no function annotation.

**Summary**, from NCBI Gene [402778](https://www.ncbi.nlm.nih.gov/gene/402778):

> Predicted to be located in membrane. Predicted to be active in plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:40022](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:40022) · Entrez [402778](https://www.ncbi.nlm.nih.gov/gene/402778) · UniProt [A6NMD0](https://www.uniprot.org/uniprotkb/A6NMD0) · Ensembl [ENSG00000244242](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000244242)

## Data

Gene col 14397: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14397); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14397, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14397]; `tensor/DDL_lfc|DDL_z.npy` [14397]; `embed/gene_vectors.npy` [14397]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14397 or target_col == 14397). Every well: [[IFITM10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IFITM10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
