---
symbol: "TCEA3"
type: "gene"
col: 12831
ensembl_id: "ENSG00000204219"
name: "transcription elongation factor A3"
location: "1p36.12"
module: 44
arm: "+"
pooled_cpm: 11.87
n_lines_expressing: 36
n_dd_up: 17
n_dd_down: 24
n_dd_up_clean: 13
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 4
direction_downstream: 7
tags: ["gene", "module/044"]
generated_by: "tahoemap"
---

# TCEA3

*transcription elongation factor A3* — 1p36.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.45× (z +11.0, q 1e-25, up in 12 of 22 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 2.17× (z +9.5, q 3e-19, up in 10 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (5 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.394× (z -11.4, q 2e-27, down in 23 of 32 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SYTL1]] (+0.65, fdr 7e-06), [[GALM]] (+0.62, fdr 1e-05), [[CCDC88B]] (+0.60, fdr 1e-05); moves opposite to [[NIP7]] (-0.49, fdr 1e-04), [[ZBED4]] (-0.45, fdr 8e-05), [[TRMT5]] (-0.45, fdr 4e-04).
> It is in [[Module 044]], a single-armed module (Defective GALNT12 causes CRCS1).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[NSUN7]] → it (grade B ⚠); 7 go from it, the strongest it → [[CDKL2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 4 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12831.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.45×** | +11.0 | 1e-25 | 12/22 (HepG2/C3A, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.51×** | +10.9 | 4e-25 | 9/18 (SW480, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.17×** | +9.5 | 3e-19 | 10/33 (A498, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.51×** | +7.2 | 1e-10 | 14/33 (SHP-77, KATO III, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.76×** | +6.4 | 1e-08 | 5/17 (HepG2/C3A, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.54×** | +5.1 | 3e-05 | 12/32 (KATO III, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Radotinib (drug)]] 5 µM |  | **1.34×** | +5.1 | 3e-05 | 18/33 (NCI-H23, KATO III, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.49×** | +4.9 | 5e-05 | 18/33 (KATO III, SW480, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.43×** | +4.4 | 8e-04 | 13/32 (KATO III, PANC-1, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.33×** | +4.1 | 0.002 | 7/33 (SW480, NCI-H23, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.28×** | +4.1 | 0.002 | 9/34 (SW480, HepG2/C3A, …) | all doses, flat |  |
| [[Belinostat (drug)]] 5 µM |  | **1.35×** | +3.7 | 0.009 | 8/32 (A-172, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.25×** | +3.5 | 0.019 | 8/33 (SW480, HepG2/C3A, …) | all doses, flat | noisy plate (z scaled) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.31×** | +3.3 | 0.037 | 7/31 (LS 180, SNU-423, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.30×** | +3.3 | 0.038 | 6/32 (SK-MEL-2, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Binimetinib (drug)]] 5 µM |  | **1.28×** | +3.3 | 0.038 | 6/34 (SW480, HepG2/C3A, …) | all doses, flat | noisy plate (z scaled) |
| [[Entrectinib (drug)]] 5 µM |  | **1.30×** | +3.3 | 0.038 | 8/32 (KATO III, A-427, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12831.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.394×** | -11.4 | 2e-27 | 23/32 (HT-29, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.405×** | -11.1 | 4e-26 | 24/32 (PANC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.448×** | -9.8 | 1e-20 | 25/32 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.505×** | -8.4 | 7e-15 | 22/31 (SW 900, SW480, …) | two highest doses | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.510×** | -8.3 | 2e-14 | 19/30 (HT-29, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.518×** | -7.8 | 8e-13 | 21/30 (NCI-H1792, LS 180, …) | two highest doses | cell-cycle shift (explains ~15% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.555×** | -7.2 | 4e-11 | 19/32 (HT-29, Hs 766T, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.355×** | -6.7 | 2e-09 | 22/31 (A-427, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.698×** | -6.2 | 3e-08 | 21/30 (HT-29, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.611×** | -5.8 | 4e-07 | 18/30 (Hs 766T, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.659×** | -5.1 | 2e-05 | 15/32 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.452×** | -5.1 | 2e-05 | 18/31 (SW480, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.776×** | -4.4 | 5e-04 | 15/33 (HT-29, H4, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.550×** | -3.8 | 0.005 | 9/31 (NCI-H1792, HT-29, …) | rises with dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.734×** | -3.8 | 0.006 | 13/32 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[EX229 (drug)]] 0.05 µM |  | **0.734×** | -3.6 | 0.011 | 11/33 (SHP-77, HT-29, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.664×** | -3.6 | 0.011 | 11/34 (HT-29, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.579×** | -3.5 | 0.014 | 10/29 (HT-29, Hs 766T, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12831. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 33.0 | 0 | 13 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0734× (z -23.6) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0829× (z -15.9) |
| [[SW 900 (line)]] | alt | 46.0 | 0 | 9 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.218× (z -15.8) ⚠ cell-cycle shift, explains ~14% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.145× (z -14.1) |
| [[LS 180 (line)]] | wt | 61.7 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -20.2) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.158× (z -15.2) |
| [[Hs 766T (line)]] | wt | 18.9 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0150× (z -22.1) |
| [[PANC-1 (line)]] | alt | 20.3 | 0 | 7 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.134× (z -16.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.172× (z -14.1) |
| [[SW480 (line)]] | alt | 17.8 | 1 (1 ⚠) | 6 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.37× (z +9.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.214× (z -14.9) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.136× (z -13.6) |
| [[NCI-H23 (line)]] | alt | 25.1 | 1 (1 ⚠) | 5 (2 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.64× (z +9.6) ⚠ position not correctable | [[Homoharringtonine (drug)]] 5 µM 0.164× (z -14.5) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.119× (z -12.1) |
| [[J82 (line)]] | alt | 10.6 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0789× (z -12.5) |
| [[NCI-H2347 (line)]] | alt | 45.9 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -18.4) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.155× (z -14.4) |
| [[NCI-H1792 (line)]] | alt | 13.0 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.0447× (z -15.1) |
| [[NCI-H2030 (line)]] | alt | 12.1 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.162× (z -8.8) |
| [[A-427 (line)]] | wt | 13.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.160× (z -9.7) ⚠ cell-cycle shift, explains ~34% of this change |
| [[HCT15 (line)]] | alt | 13.7 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.113× (z -8.6) |
| [[HepG2_C3A (line)]] | wt | 28.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.19× (z +9.0) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 5.52 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.62 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.66 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.66 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 9.31 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.14 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.06 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 8.90 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.69 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 4.99 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.49 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.17 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 8.76 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.41 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.12 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.05 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.60 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.80 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.66 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.00 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 6.43 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.63 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 42.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.86 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 5.79 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.61 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.29 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.41 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.98 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12831), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SYTL1]] | +0.65 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[GALM]] | +0.62 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[CCDC88B]] | +0.60 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[EPS8L2]] | +0.58 | +0.59 / +0.44 | both halves | 3e-05 |  |
| [[CAPN12]] | +0.57 | +0.42 / +0.48 | both halves | 4e-05 |  |
| [[PROM2]] | +0.55 | +0.41 / +0.51 | both halves | 4e-05 |  |
| [[REEP2]] | +0.54 | +0.37 / +0.51 | both halves | 8e-05 |  |
| [[CMBL]] | +0.54 | +0.45 / +0.56 | both halves | 3e-05 |  |
| [[PRXL2A]] | +0.53 | +0.44 / +0.51 | both halves | 3e-05 |  |
| [[FCGRT]] | +0.52 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[ASS1]] | +0.52 | +0.36 / +0.51 | both halves | 9e-05 |  |
| [[GABRP]] | +0.51 | +0.35 / +0.43 | both halves | 1e-04 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NIP7]] | -0.49 | -0.36 / -0.45 | both halves | 1e-04 |  |
| [[ZBED4]] | -0.45 | -0.37 / -0.52 | both halves | 8e-05 |  |
| [[TRMT5]] | -0.45 | -0.26 / -0.43 | both halves | 4e-04 |  |
| [[WDR27]] | -0.44 | -0.26 / -0.40 | both halves | 4e-04 |  |
| [[PTPRG]] | -0.43 | -0.35 / -0.30 | both halves | 2e-04 |  |
| [[DIMT1]] | -0.43 | -0.27 / -0.43 | both halves | 3e-04 |  |
| [[FAM86DP-1]] | -0.42 | -0.35 / -0.38 | both halves | 1e-04 |  |
| [[RNF144A]] | -0.42 | -0.42 / -0.36 | both halves | 1e-04 |  |
| [[C1orf109]] | -0.42 | -0.32 / -0.28 | both halves | 3e-04 |  |
| [[CCNJ]] | -0.42 | -0.29 / -0.37 | both halves | 3e-04 |  |
| [[GLI3]] | -0.41 | -0.38 / -0.43 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NSUN7]] | B | NSUN7 activity raises TCEA3's level | lines that do not express NSUN7 (22) vs lines expressing it (28) | 2.33× lower at baseline in the lines without NSUN7 | 0.030 | ⚠ within organs, on part of the lines; also absent: NEBL, KIF1A, FRMPD3; maybe low, not absent |
| [[ATAD3C]] | B | ATAD3C activity raises TCEA3's level | lines that do not express ATAD3C (17) vs lines expressing it (33) | 2.03× lower at baseline in the lines without ATAD3C | 0.033 | ⚠ within organs, on part of the lines; also absent: SLC52A3, MYH14, SORL1 |
| [[CRACR2B]] | B | CRACR2B activity raises TCEA3's level | lines that do not express CRACR2B (11) vs lines expressing it (39) | 2.09× lower at baseline in the lines without CRACR2B | 0.052 | ⚠ within organs, on part of the lines; also absent: PNPLA4, ENSG00000285679, DAPK2 |
| [[ATP2A3]] | B | ATP2A3 activity raises TCEA3's level | lines that do not express ATP2A3 (16) vs lines expressing it (34) | 1.99× lower at baseline in the lines without ATP2A3 | 0.079 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: WBP2NL, BEX4, NSUN7; maybe low, not absent |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDKL2]] | B | TCEA3 activity raises CDKL2's level | lines that do not express TCEA3 (14) vs lines expressing it (36) | 1.59× lower at baseline in the lines without TCEA3 | 0.047 | ⚠ within organs, on part of the lines; also absent: ZNF43, ENSG00000267383, ZNF681; maybe low, not absent |
| [[CXXC5]] | B | TCEA3 activity raises CXXC5's level | lines that do not express TCEA3 (14) vs lines expressing it (36) | 2.04× lower at baseline in the lines without TCEA3 | 0.056 | ⚠ within organs, on part of the lines; also absent: ZNF43, ENSG00000267383, ZNF681; maybe low, not absent |
| [[NSUN7]] | B | TCEA3 activity raises NSUN7's level | lines that do not express TCEA3 (14) vs lines expressing it (36) | 2.16× lower at baseline in the lines without TCEA3 | 0.058 | ⚠ within organs, on part of the lines; also absent: ZNF43, ENSG00000267383, ZNF681; maybe low, not absent |
| [[KBTBD3]] | B | TCEA3 activity raises KBTBD3's level | lines that do not express TCEA3 (14) vs lines expressing it (36) | 1.20× lower at baseline in the lines without TCEA3 | 0.064 | ⚠ within organs, on part of the lines; also absent: ZNF43, ENSG00000267383, ZNF681; maybe low, not absent |
| [[RORC]] | B | TCEA3 activity raises RORC's level | lines that do not express TCEA3 (14) vs lines expressing it (36) | 1.79× lower at baseline in the lines without TCEA3 | 0.078 | ⚠ within organs, on part of the lines; also absent: ZNF43, ENSG00000267383, ZNF681; maybe low, not absent |
| [[CLIP3]] | B | TCEA3 activity raises CLIP3's level | lines that do not express TCEA3 (14) vs lines expressing it (36) | 1.49× lower at baseline in the lines without TCEA3 | 0.082 | ⚠ within organs, on part of the lines; also absent: ZNF43, ENSG00000267383, ZNF681; maybe low, not absent |
| [[RCN3]] | B | TCEA3 activity raises RCN3's level | lines that do not express TCEA3 (14) vs lines expressing it (36) | 2.01× lower at baseline in the lines without TCEA3 | 0.091 | ⚠ within organs, on part of the lines; also absent: ZNF43, ENSG00000267383, ZNF681; maybe low, not absent |

## Where it sits

- **Module**: [[Module 044]] — Defective GALNT12 causes CRCS1; 102 genes; every member is in the + arm (projection on the module's main direction 0.426). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (2.1, 34.6); signed map (-6.2, 16.8). **Vector** length 67.9, 13.3% of its response variance represented; |z| ≥ 3 in 888 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.3 | +10.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.2 | +7.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.8 | +11.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.6 | +5.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.5 | +6.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.7 | +4.9 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.3 | +4.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.9 | +5.1 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | +1.5 | +0.6 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -4.1 | -8.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.3 | -7.2 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.0 | -11.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.4 | -5.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.4 | -7.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.0 | -3.8 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.8 | -3.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.8 | -3.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.6 | -2.1 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.5 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | transcription elongation factor A3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.12 — chr1:23,380,909-23,424,748 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TFIIS.H |
| Matched by | ensembl_id |

**Function**, from UniProt [O75764](https://www.uniprot.org/uniprotkb/O75764) (Transcription elongation factor A protein 3):

> Necessary for efficient RNA polymerase II transcription elongation past template-encoded arresting sites. The arresting sites in DNA have the property of trapping a certain fraction of elongating RNA polymerases that pass through, resulting in locked ternary complexes. Cleavage of the nascent transcript by S-II allows the resumption of elongation from the new 3'-terminus.

**Summary**, from NCBI Gene [6920](https://www.ncbi.nlm.nih.gov/gene/6920):

> Predicted to enable transcription elongation factor activity. Predicted to be involved in transcription elongation by RNA polymerase II. Predicted to act upstream of or within gene expression. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:11615](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11615) · Entrez [6920](https://www.ncbi.nlm.nih.gov/gene/6920) · UniProt [O75764](https://www.uniprot.org/uniprotkb/O75764) · Ensembl [ENSG00000204219](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204219)

## Data

Gene col 12831: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12831); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12831, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12831]; `tensor/DDL_lfc|DDL_z.npy` [12831]; `embed/gene_vectors.npy` [12831]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12831 or target_col == 12831). Every well: [[TCEA3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TCEA3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
