---
symbol: "CERCAM"
type: "gene"
col: 9423
ensembl_id: "ENSG00000167123"
name: "cerebral endothelial cell adhesion molecule"
location: "9q34.11"
module: 13
arm: "+"
pooled_cpm: 13.25
n_lines_expressing: 41
n_dd_up: 8
n_dd_down: 28
n_dd_up_clean: 3
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 12
direction_downstream: 20
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# CERCAM

*cerebral endothelial cell adhesion molecule* — 9q34.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.72× (z +9.7, q 2e-19, up in 15 of 26 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.37× (z +7.9, q 4e-13, up in 19 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.495× (z -17.8, q 0e+00, down in 27 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[L1CAM]] (+0.65, fdr 1e-05), [[MAN1B1]] (+0.62, fdr 1e-05), [[DKK3]] (+0.62, fdr 1e-05); moves opposite to [[ATXN7L1]] (-0.49, fdr 2e-05), [[ANK3]] (-0.48, fdr 9e-05), [[FOXP1]] (-0.47, fdr 4e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[BMP4]] → it (grade B ⚠); 20 go from it, the strongest it → [[NLGN2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9423.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.72×** | +9.7 | 2e-19 | 15/26 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.73×** | +8.6 | 1e-15 | 11/22 (NCI-H1792, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +7.9 | 4e-13 | 19/37 (A498, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.51×** | +6.8 | 2e-09 | 10/22 (A498, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 0.05 µM |  | **1.20×** | +4.5 | 7e-04 | 10/39 (hTERT-HPNE, HOP62, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.25×** | +3.9 | 0.008 | 9/39 (A-172, LOX-IMVI, …) | all doses, flat | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.27×** | +3.7 | 0.016 | 9/37 (PANC-1, H4, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.22×** | +3.5 | 0.033 | 10/38 (A-172, LOX-IMVI, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | 1.18× | +3.3 | 0.058 | 4/39 (NCI-H2030, LOX-IMVI, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9423.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.495×** | -17.8 | 0e+00 | 27/38 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.461×** | -13.8 | 4e-41 | 24/36 (A-172, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.482×** | -13.0 | 2e-36 | 23/37 (hTERT-HPNE, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.441×** | -12.9 | 7e-36 | 29/38 (MIA PaCa-2, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.527×** | -11.4 | 3e-28 | 27/39 (J82, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.518×** | -11.3 | 2e-27 | 27/39 (A-172, PANC-1, …) | two highest doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.561×** | -9.9 | 3e-21 | 25/39 (RKO, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.594×** | -9.3 | 1e-18 | 23/39 (H4, NCI-H1792, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.602×** | -9.1 | 8e-18 | 25/38 (A-172, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.592×** | -9.0 | 2e-17 | 27/39 (PANC-1, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.631×** | -8.2 | 9e-15 | 21/39 (A-172, LOX-IMVI, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.617×** | -8.1 | 2e-14 | 23/37 (SK-MEL-2, hTERT-HPNE, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.688×** | -6.7 | 1e-09 | 17/39 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.788×** | -6.0 | 7e-08 | 20/39 (HOP62, AN3 CA, …) | top dose only | position effect removed |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.716×** | -6.0 | 9e-08 | 18/38 (PANC-1, SNU-423, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.729×** | -5.7 | 5e-07 | 16/39 (LOX-IMVI, A-172, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.604×** | -4.7 | 8e-05 | 14/38 (A-427, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~21% here); composition shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.618×** | -4.5 | 2e-04 | 11/35 (SK-MEL-2, A498, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9423. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 63.2 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -21.1) |
| [[LOX-IMVI (line)]] | wt | 20.2 | 0 | 5 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.133× (z -11.4) ⚠ toxic; cell-cycle shift, explains ~18% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.223× (z -9.6) |
| [[A549 (line)]] | wt | 17.2 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -14.9) |
| [[J82 (line)]] | alt | 12.3 | 0 | 3 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0767× (z -13.5) ⚠ toxic; cell-cycle shift, explains ~48% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.198× (z -9.6) |
| [[A498 (line)]] | wt | 27.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -17.1) |
| [[BT-474 (line)]] | alt | 21.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -12.4) |
| [[H4 (line)]] | wt | 16.1 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0420× (z -14.3) |
| [[HEC-1-A (line)]] | alt | 25.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.408× (z -11.0) |
| [[MIA PaCa-2 (line)]] | alt | 16.3 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.0919× (z -12.5) |
| [[C32 (line)]] | wt | 15.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.126× (z -10.6) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 21.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.386× (z -9.5) |
| [[Hs 766T (line)]] | wt | 9.84 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.138× (z -8.7) |
| [[hTERT-HPNE (line)]] | wt | 33.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.162× (z -11.2) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 18.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -12.1) |
| [[NCI-H2347 (line)]] | alt | 9.88 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -10.4) |
| [[NCI-H460 (line)]] | wt | 7.90 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.152× (z -10.6) |
| [[Panc 03.27 (line)]] | alt | 9.35 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -12.1) |
| [[PANC-1 (line)]] | alt | 5.56 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.139× (z -12.4) |
| [[RKO (line)]] | wt | 33.2 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.264× (z -8.7) |
| [[RPMI-7951 (line)]] | alt | 41.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.270× (z -9.2) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 9.76 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.105× (z -9.5) |
| [[SW480 (line)]] | alt | 8.26 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.201× (z -10.6) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 9.05 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.55 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.10 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 7.05 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.11 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 4.81 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.83 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.41 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.55 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.811 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.99 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.16 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.10 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.60 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.21 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 37.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.33 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.03 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 12.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9423), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[L1CAM]] | +0.65 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[MAN1B1]] | +0.62 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[DKK3]] | +0.62 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[SCUBE3]] | +0.60 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[COL1A2]] | +0.59 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[RTL8C]] | +0.59 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[COL6A1]] | +0.58 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[CNPY4]] | +0.58 | +0.46 / +0.47 | both halves | 3e-05 |  |
| [[PRRT2]] | +0.56 | +0.40 / +0.56 | both halves | 5e-05 |  |
| [[COL5A1]] | +0.55 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[COLGALT1]] | +0.55 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[NRSN2]] | +0.55 | +0.51 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATXN7L1]] | -0.49 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[ANK3]] | -0.48 | -0.50 / -0.36 | both halves | 9e-05 |  |
| [[FOXP1]] | -0.47 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[NUDT4]] | -0.46 | -0.37 / -0.42 | both halves | 8e-05 |  |
| [[CASP4]] | -0.46 | -0.31 / -0.44 | both halves | 2e-04 |  |
| [[CRADD]] | -0.45 | -0.47 / -0.40 | both halves | 5e-05 |  |
| [[CHN2]] | -0.45 | -0.49 / -0.40 | both halves | 5e-05 |  |
| [[SPATA6L]] | -0.44 | -0.34 / -0.39 | both halves | 1e-04 |  |
| [[BMP4]] | -0.44 | -0.44 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 9, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BMP4]] | B | BMP4 activity lowers CERCAM's level | lines that do not express BMP4 (31) vs lines expressing it (19) | 3.81× higher at baseline in the lines without BMP4 | 0.004 | ⚠ within organs, on part of the lines; also absent: TRIM15, ENSG00000287426, TMEM45B |
| [[LOXL1]] | B | LOXL1 activity raises CERCAM's level | lines that do not express LOXL1 (18) vs lines expressing it (32) | 1.93× lower at baseline in the lines without LOXL1 | 0.017 | ⚠ within organs, on part of the lines; also absent: B3GALNT1, LOXL1-AS1, ENSG00000255330 |
| [[KATNAL1]] | B | KATNAL1 activity raises CERCAM's level | lines that do not express KATNAL1 (7) vs lines expressing it (43) | 3.53× lower at baseline in the lines without KATNAL1 | 0.021 | ⚠ within organs, on part of the lines; also absent: BOLA3-DT, STARD9, SPAG17 |
| [[SRPX]] | B | SRPX activity raises CERCAM's level | lines that do not express SRPX (22) vs lines expressing it (28) | 2.73× lower at baseline in the lines without SRPX | 0.032 | ⚠ within organs, on part of the lines; also absent: COL15A1, ARHGEF6, ENSG00000230647 |
| [[ARHGEF6]] | B | ARHGEF6 activity raises CERCAM's level | lines that do not express ARHGEF6 (20) vs lines expressing it (30) | 2.43× lower at baseline in the lines without ARHGEF6 | 0.038 | ⚠ within organs, on part of the lines; also absent: SRPX, MSRB3, ENSG00000230615; maybe low, not absent |
| [[CTSZ]] | B | CTSZ activity raises CERCAM's level | lines that do not express CTSZ (8) vs lines expressing it (42) | 1.60× lower at baseline in the lines without CTSZ | 0.040 | ⚠ within organs, on part of the lines; also absent: LRRK1, CAV2, PIWIL4; maybe low, not absent |
| [[ANK3]] | B | ANK3 activity lowers CERCAM's level | lines that do not express ANK3 (23) vs lines expressing it (27) | 1.56× higher at baseline in the lines without ANK3 | 0.051 | ⚠ within organs, on part of the lines; also absent: ATP2C2, MACC1, GALNT3 |
| [[APLP1]] | B | APLP1 activity raises CERCAM's level | lines that do not express APLP1 (12) vs lines expressing it (38) | 2.45× lower at baseline in the lines without APLP1 | 0.091 | ⚠ within organs, on part of the lines; also absent: ENSG00000291283, CTXN1, SUSD4; maybe low, not absent |
| [[DKK3]] | B | DKK3 activity raises CERCAM's level | lines that do not express DKK3 (29) vs lines expressing it (21) | 2.12× lower at baseline in the lines without DKK3 | 0.094 | ⚠ within organs, on part of the lines; also absent: COL5A1, ABI3BP, IDO1 |
| [[DZIP1L]] | C | DZIP1L activity raises CERCAM's level | lines that do not express DZIP1L (8) vs lines expressing it (42) | 3.72× lower at baseline in the lines without DZIP1L | 0.013 | ⚠ within organs, on part of the lines; also absent: STARD9, CYP46A1, RECK; maybe low, not absent; co-absent with the target |
| [[SEPTIN5]] | C | SEPTIN5 activity raises CERCAM's level | lines that do not express SEPTIN5 (12) vs lines expressing it (38) | 2.85× lower at baseline in the lines without SEPTIN5 | 0.046 | ⚠ within organs, on part of the lines; also absent: DCLK2, EBF4, TCF7L1; co-absent with the target |
| [[NLGN2]] | C | NLGN2 activity raises CERCAM's level | lines that do not express NLGN2 (4) vs lines expressing it (46) | 5.47× lower at baseline in the lines without NLGN2 | 0.057 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-occurs with CTNNB1; also absent: FSD1L, SLC29A4, DPF1 |

### Downstream of this gene

*20 arrows, 20 of them with an alert ⚠; grade A 0, B 18, C 2. Shown: the 12 strongest; 8 more arrows (8 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NLGN2]] | B | CERCAM activity raises NLGN2's level | lines that do not express CERCAM (9) vs lines expressing it (41) | 3.40× lower at baseline in the lines without CERCAM | 5e-04 | ⚠ within organs, on part of the lines; also absent: FGD1, EBF4, STARD9 |
| [[KATNAL1]] | B | CERCAM activity raises KATNAL1's level | lines that do not express CERCAM (9) vs lines expressing it (41) | 4.24× lower at baseline in the lines without CERCAM | 0.006 | ⚠ within organs, on part of the lines; also absent: FGD1, EBF4, STARD9 |
| [[SEC22C]] | B | CERCAM activity raises SEC22C's level | lines that do not express CERCAM (9) vs lines expressing it (41) | 2.14× lower at baseline in the lines without CERCAM | 0.006 | ⚠ within organs, on part of the lines; also absent: FGD1, EBF4, STARD9 |
| [[MXRA7]] | B | CERCAM activity raises MXRA7's level | lines that do not express CERCAM (9) vs lines expressing it (41) | 4.07× lower at baseline in the lines without CERCAM | 0.006 | ⚠ within organs, on part of the lines; also absent: FGD1, EBF4, STARD9 |
| [[LLGL1]] | B | CERCAM activity raises LLGL1's level | lines that do not express CERCAM (9) vs lines expressing it (41) | 1.69× lower at baseline in the lines without CERCAM | 0.008 | ⚠ within organs, on part of the lines; also absent: FGD1, EBF4, STARD9 |
| [[GLT8D1]] | B | CERCAM activity raises GLT8D1's level | lines that do not express CERCAM (9) vs lines expressing it (41) | 1.66× lower at baseline in the lines without CERCAM | 0.009 | ⚠ within organs, on part of the lines; also absent: FGD1, EBF4, STARD9 |
| [[BSG]] | B | CERCAM activity raises BSG's level | lines that do not express CERCAM (9) vs lines expressing it (41) | 1.53× lower at baseline in the lines without CERCAM | 0.031 | ⚠ within organs, on part of the lines; also absent: FGD1, EBF4, STARD9 |
| [[DDHD2]] | B | CERCAM activity raises DDHD2's level | lines that do not express CERCAM (9) vs lines expressing it (41) | 1.54× lower at baseline in the lines without CERCAM | 0.040 | ⚠ within organs, on part of the lines; also absent: FGD1, EBF4, STARD9 |
| [[MAP3K12]] | B | CERCAM activity raises MAP3K12's level | lines that do not express CERCAM (9) vs lines expressing it (41) | 1.44× lower at baseline in the lines without CERCAM | 0.048 | ⚠ within organs, on part of the lines; also absent: FGD1, EBF4, STARD9 |
| [[APLP1]] | B | CERCAM activity raises APLP1's level | lines that do not express CERCAM (9) vs lines expressing it (41) | 2.66× lower at baseline in the lines without CERCAM | 0.051 | ⚠ within organs, on part of the lines; also absent: FGD1, EBF4, STARD9 |
| [[SELENON]] | B | CERCAM activity raises SELENON's level | lines that do not express CERCAM (9) vs lines expressing it (41) | 1.85× lower at baseline in the lines without CERCAM | 0.054 | ⚠ within organs, on part of the lines; also absent: FGD1, EBF4, STARD9 |
| [[PRKACA]] | B | CERCAM activity raises PRKACA's level | lines that do not express CERCAM (9) vs lines expressing it (41) | 1.41× lower at baseline in the lines without CERCAM | 0.055 | ⚠ within organs, on part of the lines; also absent: FGD1, EBF4, STARD9 |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.368). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (56.8, 18.1); signed map (52.6, -17.0). **Vector** length 67.4, 12.4% of its response variance represented; |z| ≥ 3 in 913 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.7 | +8.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.0 | +6.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.9 | +7.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.9 | +9.7 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | +2.4 | +0.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.2 | +0.8 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +1.1 | +4.5 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +1.0 | +1.9 |
|  | [[Neratinib (drug)]] 5 µM |  | +1.0 | +1.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.0 | +2.3 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -3.5 | -9.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.7 | -12.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -2.3 | -8.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.3 | -13.8 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~24% of this change | -2.2 | -6.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.1 | -11.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.1 | -5.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.0 | -8.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.4 | -2.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.3 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | cerebral endothelial cell adhesion molecule |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.11 — chr9:128,411,751-128,437,351 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GLT25D3; previously CEECAM1 |
| Hallmark sets | APICAL_JUNCTION |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5T4B2](https://www.uniprot.org/uniprotkb/Q5T4B2) (Inactive glycosyltransferase 25 family member 3):

> Probable cell adhesion protein involved in leukocyte transmigration across the blood-brain barrier. Does not express any beta-galactosyltransferase activity in vitro.

**Summary**, from NCBI Gene [51148](https://www.ncbi.nlm.nih.gov/gene/51148):

> Enables identical protein binding activity. Acts upstream of or within cell adhesion. Predicted to be located in plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:23723](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23723) · Entrez [51148](https://www.ncbi.nlm.nih.gov/gene/51148) · UniProt [Q5T4B2](https://www.uniprot.org/uniprotkb/Q5T4B2) · Ensembl [ENSG00000167123](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167123)

## Data

Gene col 9423: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9423); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9423, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9423]; `tensor/DDL_lfc|DDL_z.npy` [9423]; `embed/gene_vectors.npy` [9423]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9423 or target_col == 9423). Every well: [[CERCAM — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CERCAM.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
