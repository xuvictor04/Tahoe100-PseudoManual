---
symbol: "DIP2A"
type: "gene"
col: 8337
ensembl_id: "ENSG00000160305"
name: "DIP2 acetate--CoA ligase A"
location: "21q22.3"
module: 2
arm: "+"
pooled_cpm: 97.22
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 20
n_dd_up_clean: 2
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# DIP2A

*DIP2 acetate--CoA ligase A* — 21q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Pitavastatin (Calcium) (drug)]] 5 µM: 1.23× (z +4.4, q 0.006, up in 26 of 47 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Pitavastatin (Calcium) (drug)]] 0.5 µM: 1.20× (z +4.1, q 0.011, up in 22 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.368× (z -31.5, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RGS12]] (+0.65, fdr 7e-06), [[BICD2]] (+0.65, fdr 3e-05), [[MYO9B]] (+0.64, fdr 1e-05); moves opposite to [[BHLHE41]] (-0.70, fdr 7e-06), [[ZNF462]] (-0.66, fdr 3e-05), [[HMG20A]] (-0.65, fdr 1e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[LRMDA]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8337.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.23×** | +4.4 | 0.006 | 26/47 (COLO 205, C32, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.20×** | +4.1 | 0.011 | 22/47 (SK-MEL-2, J82, …) | rises with dose | low cells (technical?) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.40×** | +3.9 | 0.018 | 23/49 (LoVo, RKO, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~53% of this change | 1.16× | +3.1 | 0.26 | 13/48 (HOP62, HEC-1-A, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 14 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8337.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.368×** | -31.5 | 0e+00 | 47/48 (HS-578T, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.361×** | -21.8 | 0e+00 | 46/48 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.391×** | -20.9 | 0e+00 | 46/48 (HEC-1-A, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.571×** | -17.6 | 0e+00 | 48/49 (HEC-1-A, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **0.586×** | -11.9 | 2e-30 | 37/49 (SNU-1, AsPC-1, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.614×** | -10.8 | 2e-25 | 42/48 (A-172, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **0.624×** | -10.1 | 6e-22 | 32/44 (A-172, A549, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.641×** | -9.1 | 4e-18 | 33/45 (A-427, C-33 A, …) | all doses, flat | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.555×** | -6.8 | 5e-10 | 34/49 (HS-578T, A-172, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~21% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.760×** | -5.8 | 3e-07 | 31/47 (MIA PaCa-2, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.836× | -5.6 | 1e-06 | 21/48 (NCI-H2347, LoVo, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.790×** | -5.2 | 8e-06 | 32/48 (A-172, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.784×** | -5.2 | 9e-06 | 28/50 (HEC-1-A, A-172, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.809×** | -4.5 | 2e-04 | 24/48 (BT-474, J82, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.817×** | -4.5 | 3e-04 | 23/48 (HEC-1-A, A-172, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.841× | -3.6 | 0.011 | 21/47 (NCI-H460, SW48, …) | all doses, stronger at high dose | low cells (technical?) |
| [[PH-797804 (drug)]] 5 µM |  | **0.747×** | -3.4 | 0.016 | 23/48 (LOX-IMVI, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Sulfatinib (drug)]] 5 µM |  | 0.854× | -3.4 | 0.017 | 19/49 (HOP62, A498, …) | top dose only |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.750×** | -3.3 | 0.018 | 18/49 (NCI-H23, NCI-H2347, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8337. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 195 | 0 | 14 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.250× (z -33.1) |
| [[LOX-IMVI (line)]] | wt | 151 | 0 | 12 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -29.8) |
| [[A-172 (line)]] | wt | 110 | 0 | 11 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.116× (z -35.1) |
| [[HOP62 (line)]] | alt | 134 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.172× (z -33.9) |
| [[MIA PaCa-2 (line)]] | alt | 165 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -27.2) |
| [[AsPC-1 (line)]] | alt | 156 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.141× (z -32.4) |
| [[NCI-H1573 (line)]] | alt | 91.0 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -26.6) |
| [[HS-578T (line)]] | alt | 116 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.138× (z -35.2) |
| [[NCI-H460 (line)]] | wt | 65.5 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.404× (z -17.3) |
| [[A498 (line)]] | wt | 98.7 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -22.8) |
| [[A549 (line)]] | wt | 77.9 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -24.5) |
| [[H4 (line)]] | wt | 107 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -14.5) |
| [[hTERT-HPNE (line)]] | wt | 120 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -22.3) |
| [[NCI-H2347 (line)]] | alt | 99.4 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.363× (z -18.9) |
| [[BT-474 (line)]] | alt | 83.4 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.347× (z -16.4) |
| [[CFPAC-1 (line)]] | alt | 119 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -25.6) |
| [[NCI-H2030 (line)]] | alt | 78.6 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.359× (z -18.7) |
| [[NCI-H23 (line)]] | alt | 83.4 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.356× (z -18.1) |
| [[RPMI-7951 (line)]] | alt | 114 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -19.6) |
| [[SW 900 (line)]] | alt | 78.1 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.332× (z -16.2) |
| [[A-427 (line)]] | wt | 95.4 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.266× (z -16.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.513× (z -13.0) |
| [[LoVo (line)]] | wt | 94.5 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.381× (z -21.1) |
| [[LS 180 (line)]] | wt | 92.8 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.422× (z -14.1) |
| [[NCI-H1792 (line)]] | alt | 89.7 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.438× (z -14.1) |
| [[Panc 03.27 (line)]] | alt | 83.8 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.362× (z -17.1) |
| [[HCT15 (line)]] | alt | 134 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.315× (z -16.9) |
| [[Hs 766T (line)]] | wt | 90.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.387× (z -14.5) |
| [[J82 (line)]] | alt | 70.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.333× (z -20.1) |
| [[KATO III (line)]] | alt | 45.9 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.376× (z -10.2) |
| [[PANC-1 (line)]] | alt | 62.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -25.4) |
| [[SK-MEL-2 (line)]] | alt | 73.2 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.258× (z -13.0) |
| [[SNU-423 (line)]] | alt | 82.0 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.160× (z -28.0) |
| [[SW48 (line)]] | wt | 76.5 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.176× (z -14.6) |
| [[C-33 A (line)]] | alt | 107 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.264× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.529× (z -9.2) |
| [[C32 (line)]] | wt | 72.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.373× (z -13.6) |
| [[SNU-1 (line)]] | wt | 124 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.213× (z -16.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change |
| [[SW 1088 (line)]] | alt | 115 | 0 | 2 | — | [[Mifepristone (drug)]] 5 µM 0.0726× (z -10.1) |
| [[SW1417 (line)]] | alt | 81.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.535× (z -11.6) |
| [[SW480 (line)]] | alt | 106 | 0 | 2 | — | [[Harringtonine (drug)]] 0.5 µM 0.571× (z -9.0) |
| [[AN3 CA (line)]] | alt | 102 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.133× (z -13.5) |
| [[COLO 205 (line)]] | alt | 70.9 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.357× (z -8.8) |
| [[RKO (line)]] | wt | 87.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.532× (z -9.9) |
| [[CHP-212 (line)]] | wt | 74.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 69.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 64.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 96.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 81.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 75.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 86.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8337), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*59 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RGS12]] | +0.65 | +0.71 / +0.61 | both halves | 7e-06 |  |
| [[BICD2]] | +0.65 | +0.66 / +0.44 | both halves | 3e-05 |  |
| [[MYO9B]] | +0.64 | +0.70 / +0.53 | both halves | 1e-05 |  |
| [[BCL7C]] | +0.63 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[NAP1L4]] | +0.63 | +0.75 / +0.52 | both halves | 1e-05 |  |
| [[AP2A2]] | +0.63 | +0.74 / +0.42 | both halves | 4e-05 |  |
| [[ASB16-AS1]] | +0.63 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[TPST2]] | +0.62 | +0.69 / +0.46 | both halves | 3e-05 |  |
| [[PBX4]] | +0.62 | +0.68 / +0.39 | both halves | 5e-05 |  |
| [[CCM2]] | +0.62 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[TCF3]] | +0.62 | +0.71 / +0.48 | both halves | 2e-05 |  |
| [[STX2]] | +0.61 | +0.70 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*41 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BHLHE41]] | -0.70 | -0.63 / -0.70 | both halves | 7e-06 |  |
| [[ZNF462]] | -0.66 | -0.72 / -0.43 | both halves | 3e-05 |  |
| [[HMG20A]] | -0.65 | -0.64 / -0.55 | both halves | 1e-05 |  |
| [[ZNF608]] | -0.64 | -0.63 / -0.64 | both halves | 7e-06 |  |
| [[ZNF827]] | -0.63 | -0.54 / -0.44 | both halves | 3e-05 |  |
| [[TIGD2]] | -0.63 | -0.77 / -0.56 | both halves | 1e-05 |  |
| [[TAPBPL]] | -0.62 | -0.68 / -0.42 | both halves | 4e-05 |  |
| [[ZNF620]] | -0.61 | -0.71 / -0.48 | both halves | 2e-05 |  |
| [[LEKR1]] | -0.61 | -0.70 / -0.41 | both halves | 4e-05 |  |
| [[CILK1]] | -0.60 | -0.69 / -0.42 | both halves | 4e-05 |  |
| [[KLF10]] | -0.60 | -0.54 / -0.56 | both halves | 1e-05 |  |
| [[CFH]] | -0.60 | -0.55 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LRMDA]] | B | LRMDA activity lowers DIP2A's level | lines that do not express LRMDA (21) vs lines expressing it (29) | 1.27× higher at baseline in the lines without LRMDA | 0.076 | ⚠ within organs, on part of the lines; also absent: ENSG00000289911, CCL28, SMIM10 |
| [[CLTCL1]] | C | CLTCL1 activity raises DIP2A's level | lines that do not express CLTCL1 (3) vs lines expressing it (47) | 1.61× lower at baseline in the lines without CLTCL1 | 0.081 | ⚠ few lines (3 vs 47); across organs; also absent: NKAIN1, WHRN, SUGCT |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.602). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (18.3, 5.5); signed map (-42.9, -4.7). **Vector** length 101, 29.6% of its response variance represented; |z| ≥ 3 in 1,196 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +5.1 | -3.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~77% of this change | +5.1 | -4.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +4.9 | +1.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~86% of this change | +4.5 | -3.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.3 | +2.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.9 | +0.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.8 | +0.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.3 | +1.6 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +2.8 | -0.1 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -7.6 | -21.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -7.0 | -31.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -6.9 | -10.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.7 | -20.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | -6.5 | -6.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.7 | -5.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.9 | -3.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.7 | -5.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.7 | -0.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.6 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | DIP2 acetate--CoA ligase A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q22.3 — chr21:46,458,891-46,570,015 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Dip2, KIAA0184; previously C21orf106 |
| Gene groups (HGNC) | DIP2 family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14689](https://www.uniprot.org/uniprotkb/Q14689) (Disco-interacting protein 2 homolog A):

> Catalyzes the de novo synthesis of acetyl-CoA in vitro (By similarity). Promotes acetylation of CTTN, possibly by providing the acetyl donor, ensuring correct dendritic spine morphology and synaptic transmission (By similarity). Binds to follistatin-related protein FSTL1 and may act as a cell surface receptor for FSTL1, contributing to AKT activation and subsequent FSTL1-induced survival and function of endothelial cells and cardiac myocytes.

**Summary**, from NCBI Gene [23181](https://www.ncbi.nlm.nih.gov/gene/23181):

> The protein encoded by this gene may be involved in axon patterning in the central nervous system. This gene is not highly expressed. Several transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Mar 2009]

**Accessions** — [HGNC:17217](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17217) · Entrez [23181](https://www.ncbi.nlm.nih.gov/gene/23181) · UniProt [Q14689](https://www.uniprot.org/uniprotkb/Q14689) · Ensembl [ENSG00000160305](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000160305)

## Data

Gene col 8337: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8337); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8337, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8337]; `tensor/DDL_lfc|DDL_z.npy` [8337]; `embed/gene_vectors.npy` [8337]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8337 or target_col == 8337). Every well: [[DIP2A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DIP2A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
