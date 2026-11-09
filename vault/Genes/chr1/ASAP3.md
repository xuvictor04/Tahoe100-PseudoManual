---
symbol: "ASAP3"
type: "gene"
col: 1525
ensembl_id: "ENSG00000088280"
name: "ArfGAP with SH3 domain, ankyrin repeat and PH domain 3"
location: "1p36.12"
module: 30
arm: "+"
pooled_cpm: 7.27
n_lines_expressing: 45
n_dd_up: 35
n_dd_down: 19
n_dd_up_clean: 29
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 3
direction_downstream: 10
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# ASAP3

*ArfGAP with SH3 domain, ankyrin repeat and PH domain 3* — 1p36.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 35 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 4.32× (z +17.3, q 0e+00, up in 40 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (11 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.524× (z -7.6, q 1e-11, down in 26 of 42 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RIMS3]] (+0.69, fdr 1e-05), [[IQSEC2]] (+0.66, fdr 1e-05), [[USP35]] (+0.66, fdr 1e-05); moves opposite to [[FJX1]] (-0.59, fdr 2e-05), [[NSUN6]] (-0.58, fdr 4e-05), [[ERCC6L2]] (-0.56, fdr 1e-04).
> It sits in the **+** arm of [[Module 030]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TSPAN33]] → it (grade B ⚠); 10 go from it, the strongest it → [[NEPRO-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 35 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1525.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **4.32×** | +17.3 | 0e+00 | 40/43 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **4.17×** | +16.9 | 0e+00 | 41/43 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.96×** | +16.3 | 0e+00 | 39/42 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.98×** | +12.9 | 6e-36 | 37/43 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.08×** | +12.2 | 3e-32 | 36/43 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **2.13×** | +9.0 | 3e-17 | 27/39 (HepG2/C3A, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **3.95×** | +8.5 | 2e-15 | 33/41 (PANC-1, NCI-H460, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.95×** | +7.9 | 2e-13 | 30/41 (NCI-H2347, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.60×** | +5.2 | 1e-05 | 15/41 (HepG2/C3A, HOP62, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.53×** | +5.0 | 3e-05 | 18/42 (HOP62, J82, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.40×** | +4.7 | 1e-04 | 12/42 (HepG2/C3A, BT-474, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **1.51×** | +4.5 | 3e-04 | 13/43 (BT-474, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~19% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~39% of this change | **2.01×** | +4.3 | 7e-04 | 4/22 (HOP62, SNU-423, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.28×** | +4.1 | 0.002 | 10/42 (HS-578T, NCI-H23, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.40×** | +4.0 | 0.002 | 9/42 (HT-29, SW1417, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.37×** | +3.8 | 0.006 | 6/43 (HCT15, PANC-1, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.38×** | +3.7 | 0.007 | 7/40 (HCT15, C32, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.37×** | +3.7 | 0.007 | 8/41 (HOP62, BT-474, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 11 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1525.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.524×** | -7.6 | 1e-11 | 26/42 (HS-578T, AN3 CA, …) | two highest doses | cell-cycle shift (explains ~20% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.577×** | -6.5 | 2e-08 | 19/43 (HT-29, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **0.569×** | -6.4 | 3e-08 | 18/36 (A-427, SNU-423, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **0.573×** | -6.3 | 4e-08 | 22/43 (HS-578T, NCI-H23, …) | two highest doses | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.385×** | -5.9 | 4e-07 | 21/41 (A-427, SK-MEL-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~22% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.639×** | -5.3 | 1e-05 | 19/38 (HT-29, A-172, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.650×** | -5.1 | 3e-05 | 17/42 (HT-29, PANC-1, …) | two highest doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.441×** | -5.1 | 3e-05 | 17/36 (SW 900, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.643×** | -4.8 | 9e-05 | 8/18 (A-172, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~21% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.690×** | -4.4 | 7e-04 | 16/41 (A-172, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | **0.692×** | -4.3 | 7e-04 | 18/38 (NCI-H460, A549, …) | two highest doses |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.700×** | -4.1 | 0.002 | 8/43 (A-427, HS-578T, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.726×** | -3.8 | 0.007 | 17/41 (A498, PANC-1, …) | all doses, flat |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.726×** | -3.8 | 0.007 | 12/42 (HT-29, Panc 03.27, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.548×** | -3.7 | 0.008 | 10/39 (A498, HT-29, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.554×** | -3.7 | 0.009 | 13/41 (HT-29, PANC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.608×** | -3.1 | 0.064 | 8/37 (HT-29, HepG2/C3A, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, -0.64 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1525. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 15.7 | 0 | 6 (6 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0946× (z -12.1) ⚠ cell-cycle shift, explains ~49% of this change |
| [[PANC-1 (line)]] | alt | 10.3 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 5.27× (z +11.7) | [[Homoharringtonine (drug)]] 0.5 µM 0.298× (z -8.6) ⚠ cell-cycle shift, explains ~49% of this change |
| [[A-172 (line)]] | wt | 14.5 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.129× (z -12.1) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 5.05 | 1 | 2 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 5.37× (z +8.5) | [[Digitoxin (drug)]] 5 µM 0.127× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change |
| [[A-427 (line)]] | wt | 13.8 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0835× (z -13.0) ⚠ toxic; cell-cycle shift, explains ~26% of this change |
| [[A549 (line)]] | wt | 5.61 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0711× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change |
| [[AN3 CA (line)]] | alt | 29.3 | 0 | 1 | — | [[Ponatinib (drug)]] 5 µM 0.0706× (z -9.2) |
| [[HS-578T (line)]] | alt | 14.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.190× (z -8.7) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 5.85 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0811× (z -9.9) ⚠ toxic; cell-cycle shift, explains ~26% of this change |
| [[SNU-423 (line)]] | alt | 10.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.101× (z -10.0) ⚠ toxic; cell-cycle shift, explains ~26% of this change |
| [[SW480 (line)]] | alt | 2.77 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 9.14× (z +8.5) | — |
| [[A498 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.58 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.61 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.44 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 4.54 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.59 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.10 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.27 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.59 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.46 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.950 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 7.84 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.34 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.48 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.22 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.76 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.59 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.96 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.70 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.01 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.14 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.02 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.22 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.44 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1525), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RIMS3]] | +0.69 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[IQSEC2]] | +0.66 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[USP35]] | +0.66 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[AP2A2]] | +0.65 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[NXPE3]] | +0.64 | +0.50 / +0.70 | both halves | 1e-05 |  |
| [[TSPAN33]] | +0.64 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[PEDS1]] | +0.63 | +0.47 / +0.59 | both halves | 2e-05 |  |
| [[SLC29A4]] | +0.62 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[MAST3]] | +0.61 | +0.46 / +0.61 | both halves | 3e-05 |  |
| [[SNTA1]] | +0.61 | +0.52 / +0.46 | both halves | 3e-05 |  |
| [[CAMK2G]] | +0.61 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[RECK]] | +0.60 | +0.47 / +0.62 | both halves | 2e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FJX1]] | -0.59 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[NSUN6]] | -0.58 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[ERCC6L2]] | -0.56 | -0.33 / -0.50 | both halves | 1e-04 |  |
| [[INO80D]] | -0.55 | -0.28 / -0.56 | both halves | 3e-04 |  |
| [[RBM26-AS1]] | -0.55 | -0.39 / -0.24 | both halves | 5e-04 |  |
| [[NFKB1]] | -0.55 | -0.38 / -0.53 | both halves | 6e-05 | same gene group |
| [[NEPRO-AS1]] | -0.55 | -0.41 / -0.39 | both halves | 6e-05 |  |
| [[ST7L]] | -0.55 | -0.30 / -0.41 | both halves | 2e-04 |  |
| [[CDK6-AS1]] | -0.54 | -0.40 / -0.37 | both halves | 8e-05 |  |
| [[LINS1]] | -0.54 | -0.36 / -0.39 | both halves | 9e-05 |  |
| [[HELQ]] | -0.54 | -0.42 / -0.25 | both halves | 4e-04 |  |
| [[LINC01145-1]] | -0.53 | -0.29 / -0.50 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TSPAN33]] | B | TSPAN33 activity raises ASAP3's level | lines that do not express TSPAN33 (12) vs lines expressing it (38) | 1.70× lower at baseline in the lines without TSPAN33 | 0.049 | ⚠ within organs, on part of the lines; also absent: SRCIN1, CRACD, GNAZ; maybe low, not absent |
| [[ATP8B2]] | B | ATP8B2 activity raises ASAP3's level | lines that do not express ATP8B2 (10) vs lines expressing it (40) | 2.12× lower at baseline in the lines without ATP8B2 | 0.096 | ⚠ within organs, on part of the lines; co-occurs with APC; also absent: CRIP2, NRSN2, TTC28 |
| [[SLC29A4]] | C | SLC29A4 activity raises ASAP3's level | lines that do not express SLC29A4 (6) vs lines expressing it (44) | 2.86× lower at baseline in the lines without SLC29A4 | 0.034 | ⚠ within organs, on part of the lines; also absent: DPF1, DNMT3B, CNTNAP1; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 7, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NEPRO-AS1]] | B | ASAP3 activity raises NEPRO-AS1's level | lines that do not express ASAP3 (5) vs lines expressing it (45) | 2.53× lower at baseline in the lines without ASAP3 | 0.027 | ⚠ within organs, on part of the lines; also absent: DPF1, SCML2, CCDC102A; maybe low, not absent |
| [[ANKRD27]] | B | ASAP3 activity raises ANKRD27's level | lines that do not express ASAP3 (5) vs lines expressing it (45) | 1.39× lower at baseline in the lines without ASAP3 | 0.046 | ⚠ within organs, on part of the lines; also absent: DPF1, SCML2, CCDC102A; maybe low, not absent |
| [[FADS3]] | B | ASAP3 activity raises FADS3's level | lines that do not express ASAP3 (5) vs lines expressing it (45) | 2.02× lower at baseline in the lines without ASAP3 | 0.049 | ⚠ within organs, on part of the lines; also absent: DPF1, SCML2, CCDC102A; maybe low, not absent |
| [[NXPE3]] | B | ASAP3 activity raises NXPE3's level | lines that do not express ASAP3 (5) vs lines expressing it (45) | 3.73× lower at baseline in the lines without ASAP3 | 0.057 | ⚠ within organs, on part of the lines; also absent: DPF1, SCML2, CCDC102A; maybe low, not absent |
| [[GNB5]] | B | ASAP3 activity raises GNB5's level | lines that do not express ASAP3 (5) vs lines expressing it (45) | 1.86× lower at baseline in the lines without ASAP3 | 0.071 | ⚠ within organs, on part of the lines; also absent: DPF1, SCML2, CCDC102A; maybe low, not absent |
| [[CYREN]] | B | ASAP3 activity raises CYREN's level | lines that do not express ASAP3 (5) vs lines expressing it (45) | 1.43× lower at baseline in the lines without ASAP3 | 0.080 | ⚠ within organs, on part of the lines; also absent: DPF1, SCML2, CCDC102A; maybe low, not absent |
| [[PCID2]] | B | ASAP3 activity raises PCID2's level | lines that do not express ASAP3 (5) vs lines expressing it (45) | 1.57× lower at baseline in the lines without ASAP3 | 0.090 | ⚠ within organs, on part of the lines; also absent: DPF1, SCML2, CCDC102A; maybe low, not absent |
| [[RHOQ]] | C | ASAP3 activity raises RHOQ's level | lines that do not express ASAP3 (5) vs lines expressing it (45) | 4.53× lower at baseline in the lines without ASAP3 | 0.020 | ⚠ within organs, on part of the lines; also absent: DPF1, SCML2, CCDC102A; maybe low, not absent; co-absent with the target |
| [[SLC29A4]] | C | ASAP3 activity raises SLC29A4's level | lines that do not express ASAP3 (5) vs lines expressing it (45) | 3.15× lower at baseline in the lines without ASAP3 | 0.036 | ⚠ within organs, on part of the lines; also absent: DPF1, SCML2, CCDC102A; maybe low, not absent; co-absent with the target |
| [[TPST1]] | C | ASAP3 activity raises TPST1's level | lines that do not express ASAP3 (5) vs lines expressing it (45) | 5.60× lower at baseline in the lines without ASAP3 | 0.043 | ⚠ within organs, on part of the lines; also absent: DPF1, SCML2, CCDC102A; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.585). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (1.3, 0.3); signed map (-38.0, -5.7). **Vector** length 70.0, 12.2% of its response variance represented; |z| ≥ 3 in 1,141 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.3 | +12.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.6 | +7.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | +4.6 | +5.0 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~49% of this change | +3.9 | +5.2 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.6 | +12.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.5 | +1.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.9 | +8.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.1 | +1.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.9 | +3.3 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | -4.6 | -5.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | -4.1 | -6.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.1 | -7.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -3.2 | -3.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | -0.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.6 | -3.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.5 | +0.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.0 | -3.7 |
|  | [[Belzutifan (drug)]] 5 µM |  | -2.0 | -2.5 |
|  | [[EX229 (drug)]] 5 µM |  | -1.9 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | ArfGAP with SH3 domain, ankyrin repeat and PH domain 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.12 — chr1:23,428,563-23,484,637 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20199, UPLC1, CENTB6; previously DDEFL1 |
| Gene groups (HGNC) | ArfGAPs; Ankyrin repeat domain containing; BAR-PH domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TDY4](https://www.uniprot.org/uniprotkb/Q8TDY4) (Arf-GAP with SH3 domain, ANK repeat and PH domain-containing protein 3):

> Promotes cell proliferation.

**Summary**, from NCBI Gene [55616](https://www.ncbi.nlm.nih.gov/gene/55616):

> This gene encodes a member of a subfamily of ADP-ribosylation factor(Arf) GTPase-activating proteins that contain additional ankyrin repeat and pleckstrin homology domains. The Arf GAP domain of this protein catalyzes the hydrolysis of GTP bound to Arf proteins. The encoded protein promotes cell differentiation and migration and has been implicated in cancer cell invasion. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jan 2009]

**Accessions** — [HGNC:14987](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14987) · Entrez [55616](https://www.ncbi.nlm.nih.gov/gene/55616) · UniProt [Q8TDY4](https://www.uniprot.org/uniprotkb/Q8TDY4) · Ensembl [ENSG00000088280](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000088280)

## Data

Gene col 1525: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1525); `tables/drug_effects.parquet` (54 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1525, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1525]; `tensor/DDL_lfc|DDL_z.npy` [1525]; `embed/gene_vectors.npy` [1525]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1525 or target_col == 1525). Every well: [[ASAP3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ASAP3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
