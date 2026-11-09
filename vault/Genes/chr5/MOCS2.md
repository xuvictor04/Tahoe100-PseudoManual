---
symbol: "MOCS2"
type: "gene"
col: 8892
ensembl_id: "ENSG00000164172"
name: "molybdenum cofactor synthesis 2"
location: "5q11.2"
module: 57
arm: "+"
pooled_cpm: 22.16
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 9
n_dd_up_clean: 11
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/057"]
generated_by: "tahoemap"
---

# MOCS2

*molybdenum cofactor synthesis 2* — 5q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.09× (z +19.3, q 0e+00, up in 41 of 41 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.39× (z +6.4, q 1e-08, up in 32 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.497× (z -9.6, q 6e-19, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPAP3]] (+0.76, fdr 7e-06), [[PHF6]] (+0.65, fdr 1e-05), [[TMTC3]] (+0.65, fdr 2e-05); moves opposite to [[TMEM187]] (-0.64, fdr 3e-05), [[SETD1B]] (-0.60, fdr 2e-04), [[LEMD3]] (-0.57, fdr 1e-04).
> It sits in the **+** arm of [[Module 057]] (Peroxisomal protein import).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8892.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.09×** | +19.3 | 0e+00 | 41/41 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.08×** | +18.6 | 0e+00 | 33/34 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.43×** | +11.3 | 3e-27 | 29/36 (NCI-H2347, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.76×** | +7.7 | 1e-12 | 38/48 (PANC-1, HepG2/C3A, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.69×** | +7.2 | 6e-11 | 36/48 (J82, A498, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.67×** | +7.1 | 1e-10 | 38/48 (J82, PANC-1, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.39×** | +6.4 | 1e-08 | 32/48 (A498, NCI-H2347, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.57×** | +6.2 | 5e-08 | 31/48 (RKO, C32, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.51×** | +5.7 | 1e-06 | 28/48 (A498, NCI-H2347, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.45×** | +5.1 | 2e-05 | 25/48 (KATO III, A498, …) | two highest doses | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.43×** | +4.9 | 4e-05 | 30/48 (HS-578T, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.28×** | +4.8 | 7e-05 | 26/48 (SNU-1, LS 180, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **1.42×** | +4.6 | 2e-04 | 23/44 (MIA PaCa-2, A-427, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~29% of this change | **1.38×** | +4.4 | 4e-04 | 24/44 (CFPAC-1, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.35×** | +3.9 | 0.004 | 18/48 (A498, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.32×** | +3.8 | 0.005 | 18/48 (Panc 03.27, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.31×** | +3.7 | 0.007 | 17/48 (A549, RKO, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.30×** | +3.6 | 0.009 | 18/48 (NCI-H2347, NCI-H1792, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.25×** | +3.0 | 0.076 | 12/48 (C32, SW 900, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8892.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.497×** | -9.6 | 6e-19 | 40/48 (SW480, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.533×** | -8.6 | 2e-15 | 34/47 (NCI-H23, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.646×** | -8.5 | 5e-15 | 35/46 (PANC-1, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.548×** | -8.2 | 3e-14 | 40/48 (SW480, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.560×** | -7.9 | 2e-13 | 35/48 (J82, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.689×** | -5.1 | 3e-05 | 24/47 (NCI-H23, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.493×** | -5.1 | 3e-05 | 30/46 (A-427, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.752×** | -3.9 | 0.007 | 20/48 (A-172, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.630×** | -3.3 | 0.059 | 14/48 (SNU-1, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.35 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8892. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 23.5 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 4.07× (z +12.0) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 0.5 µM 0.329× (z -9.8) |
| [[A498 (line)]] | wt | 18.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.15× (z +15.8) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 26.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.42× (z +13.7) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 20.8 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.06× (z +10.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.400× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 44.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.36× (z +11.7) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 27.7 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.19× (z +12.6) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.486× (z -9.0) |
| [[SNU-423 (line)]] | alt | 25.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.54× (z +14.0) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 23.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 8.67× (z +14.2) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 17.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 11.1× (z +12.3) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 24.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.66× (z +12.2) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 24.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.87× (z +11.6) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 10.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.84× (z +9.9) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 23.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.27× (z +10.6) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 21.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.17× (z +9.4) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 21.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.20× (z +9.2) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 23.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.84× (z +12.8) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 21.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.94× (z +11.7) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 13.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.95× (z +9.9) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 22.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.85× (z +9.9) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 19.3 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.119× (z -13.3) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 21.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.06× (z +14.3) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 43.9 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.363× (z -8.5) |
| [[A549 (line)]] | wt | 22.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.74× (z +9.5) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 21.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.84× (z +9.3) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 21.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.82× (z +8.5) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 23.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.12× (z +10.6) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 12.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.83× (z +8.7) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 24.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.27× (z +10.8) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 21.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 17.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8892), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPAP3]] | +0.76 | +0.61 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[PHF6]] | +0.65 | +0.50 / +0.63 | both halves | 1e-05 |  |
| [[TMTC3]] | +0.65 | +0.46 / +0.70 | both halves | 2e-05 |  |
| [[ZDHHC21]] | +0.65 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[ALAS1]] | +0.64 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[CCNC]] | +0.64 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[GNPDA2]] | +0.63 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[TTC1]] | +0.63 | +0.50 / +0.63 | both halves | 1e-05 |  |
| [[COMMD8]] | +0.63 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[KIFAP3]] | +0.61 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[DLD]] | +0.61 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[ADH5]] | +0.61 | +0.46 / +0.51 | both halves | 2e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM187]] | -0.64 | -0.43 / -0.60 | both halves | 3e-05 |  |
| [[SETD1B]] | -0.60 | -0.30 / -0.64 | both halves | 2e-04 |  |
| [[LEMD3]] | -0.57 | -0.35 / -0.47 | both halves | 1e-04 |  |
| [[CA5BP1]] | -0.56 | -0.42 / -0.60 | both halves | 4e-05 |  |
| [[MSL1]] | -0.55 | -0.43 / -0.54 | both halves | 3e-05 |  |
| [[SLC12A9]] | -0.55 | -0.38 / -0.51 | both halves | 6e-05 |  |
| [[KIAA2026]] | -0.53 | -0.34 / -0.51 | both halves | 1e-04 |  |
| [[GSK3A]] | -0.53 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[TNRC18]] | -0.53 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[CRAMP1]] | -0.53 | -0.52 / -0.56 | both halves | 1e-05 |  |
| [[ARID1A]] | -0.52 | -0.32 / -0.49 | both halves | 2e-04 |  |
| [[ENDOG]] | -0.52 | -0.19 / -0.52 | ⚠ one half (not replicated) | 8e-04 |  |
| [[PRDM15]] | -0.51 | -0.38 / -0.43 | both halves | 6e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 057]] — Peroxisomal protein import; 86 genes; this gene is in the **+** arm (projection on the module's main direction 0.439). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-20.9, -0.5); signed map (-23.3, -20.2). **Vector** length 81.2, 17.9% of its response variance represented; |z| ≥ 3 in 953 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.8 | +5.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.1 | +6.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +4.0 | +5.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +3.7 | +3.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.5 | +3.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.4 | +6.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.2 | +2.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.0 | +3.6 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -11.0 | -8.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.7 | -8.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.6 | -1.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -4.4 | -8.2 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.9 | -9.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.9 | -0.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.8 | +0.2 |
|  | [[Thymol (drug)]] 0.5 µM |  | -1.6 | -1.7 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.5 | +0.3 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | -1.5 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | molybdenum cofactor synthesis 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q11.2 — chr5:53,095,679-53,110,063 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MOCO1, MOCS2A, MOCS2B |
| Gene groups (HGNC) | Molybdenum cofactor synthesis proteins |
| Hallmark sets | ESTROGEN_RESPONSE_LATE |
| Reactome | 3 pathways, smallest: Molybdenum cofactor biosynthesis; Metabolism of water-soluble vitamins and cofactors; Metabolism of vitamins and cofactors |
| Matched by | ensembl_id |

**Function**, from UniProt [O96007](https://www.uniprot.org/uniprotkb/O96007) (Molybdopterin synthase catalytic subunit):

> Catalytic subunit of the molybdopterin synthase complex, a complex that catalyzes the conversion of precursor Z into molybdopterin. Acts by mediating the incorporation of 2 sulfur atoms from thiocarboxylated MOCS2A into precursor Z to generate a dithiolene group (By similarity). Together with MBIP, inhibits the activity of stress kinase EIF2AK2/PKR; this may suppress JNK activation and subsequent stress-responsive transcription, or suppress eIF2a phosphorylation to favor translation.

**Summary**, from NCBI Gene [4338](https://www.ncbi.nlm.nih.gov/gene/4338):

> Eukaryotic molybdoenzymes use a unique molybdenum cofactor (MoCo) consisting of a pterin, termed molybdopterin, and the catalytically active metal molybdenum. MoCo is synthesized from precursor Z by the heterodimeric enzyme molybdopterin synthase. The large and small subunits of molybdopterin synthase are both encoded from this gene by overlapping open reading frames. The proteins were initially thought to be encoded from a bicistronic transcript. They are now thought to be encoded from …

**Accessions** — [HGNC:7193](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7193) · Entrez [4338](https://www.ncbi.nlm.nih.gov/gene/4338) · UniProt [O96007](https://www.uniprot.org/uniprotkb/O96007) · Ensembl [ENSG00000164172](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164172)

## Data

Gene col 8892: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8892); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8892, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8892]; `tensor/DDL_lfc|DDL_z.npy` [8892]; `embed/gene_vectors.npy` [8892]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8892 or target_col == 8892). Every well: [[MOCS2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MOCS2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
