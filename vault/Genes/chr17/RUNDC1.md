---
symbol: "RUNDC1"
type: "gene"
col: 12714
ensembl_id: "ENSG00000198863"
name: "RUN domain containing 1"
location: "17q21.31"
module: 144
arm: "+"
pooled_cpm: 29.78
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 5
n_dd_up_clean: 13
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/144"]
generated_by: "tahoemap"
---

# RUNDC1

*RUN domain containing 1* — 17q21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.40× (z +10.8, q 1e-24, up in 32 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.697× (z -7.8, q 3e-12, down in 20 of 38 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 0.5 µM: 0.775× (z -5.3, q 2e-05, down in 22 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (A549 0.107×, HCT15 0.152×, J82 0.276×, CHP-212 0.154×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (HepG2/C3A 0.134×, SW48 0.115×, A-172 0.323×, NCI-H1792 0.263×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (HEC-1-A 0.416×, BT-474 0.221×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAML1]] (+0.57, fdr 2e-05), [[RBM15]] (+0.52, fdr 1e-04), [[AP4E1]] (+0.52, fdr 6e-05); moves opposite to [[SMC5]] (-0.44, fdr 1e-04), [[RTN3]] (-0.42, fdr 8e-05), [[MALAT1]] (-0.42, fdr 7e-04, ⚠ one half only (not replicated)), [[MBOAT2]] (-0.41, fdr 1e-04).
> It is in [[Module 144]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12714.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.40×** | +10.8 | 1e-24 | 32/48 (NCI-H1792, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.52×** | +9.5 | 8e-19 | 31/47 (COLO 205, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.21×** | +9.4 | 1e-18 | 31/48 (SW480, RKO, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.56×** | +9.3 | 1e-18 | 29/47 (A549, LS 180, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.50×** | +9.1 | 7e-18 | 29/48 (HOP62, LS 180, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.49×** | +9.0 | 1e-17 | 32/48 (A549, HEC-1-A, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.46×** | +8.6 | 7e-16 | 31/48 (A549, HOP62, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.44×** | +8.3 | 1e-14 | 29/47 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.40×** | +7.7 | 1e-12 | 29/47 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.23×** | +6.7 | 1e-09 | 26/47 (KATO III, LS 180, …) | all doses, flat | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.35×** | +6.5 | 5e-09 | 25/46 (COLO 205, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.65×** | +5.9 | 1e-07 | 24/46 (SW480, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.20× | +5.7 | 4e-07 | 20/48 (HEC-1-A, HOP62, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.26×** | +5.2 | 6e-06 | 22/47 (A-427, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.22×** | +4.2 | 9e-04 | 16/48 (LOX-IMVI, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.21×** | +4.0 | 0.003 | 15/47 (A549, NCI-H460, …) | all doses, flat | low cells (technical?) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.37×** | +3.7 | 0.006 | 14/47 (NCI-H2030, SHP-77, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Gefitinib (drug)]] 5 µM |  | 1.17× | +3.5 | 0.014 | 6/48 (NCI-H460, C-33 A, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12714.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (A549 0.107×, HCT15 0.152×, J82 0.276×, CHP-212 0.154×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (HepG2/C3A 0.134×, SW48 0.115×, A-172 0.323×, NCI-H1792 0.263×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (HEC-1-A 0.416×, BT-474 0.221×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.697×** | -7.8 | 3e-12 | 20/38 (A549, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.792×** | -7.4 | 3e-11 | 27/48 (J82, NCI-H1792, …) | rises with dose | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.752×** | -6.4 | 3e-08 | 24/44 (HepG2/C3A, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.775×** | -5.3 | 2e-05 | 22/47 (SW 1271, SHP-77, …) | two highest doses | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.865× | -4.6 | 5e-04 | 15/48 (SW480, NCI-H661, …) | two highest doses |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.819×** | -4.2 | 0.003 | 17/48 (HEC-1-A, NCI-H1792, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | 0.847× | -3.6 | 0.027 | 8/47 (HOP62, A-172, …) | top dose only |  |
| [[Resveratrol (drug)]] 5 µM |  | 0.903× | -3.2 | 0.084 | 8/48 (SW48, SW 900, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12714. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 34.3 | 2 | 1 (1 ⚠) | [[Harringtonine (drug)]] 0.5 µM 2.91× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.107× (z -17.7) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 31.9 | 3 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.14× (z +10.0) | — |
| [[SW480 (line)]] | alt | 33.7 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.08× (z +9.3) | — |
| [[HepG2_C3A (line)]] | wt | 38.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.134× (z -13.4) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 27.9 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.62× (z +10.3) | [[Dinaciclib (drug)]] 0.5 µM 0.263× (z -10.2) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 32.9 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.451× (z -8.8) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 30.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.323× (z -10.2) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 30.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +9.2) ⚠ cell-cycle shift, explains ~35% of this change | — |
| [[BT-474 (line)]] | alt | 25.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.221× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[CHP-212 (line)]] | wt | 65.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.154× (z -9.6) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 30.0 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.63× (z +8.8) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 44.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.152× (z -13.4) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 42.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.416× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[J82 (line)]] | alt | 32.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.276× (z -11.9) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 34.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +11.1) ⚠ cell-cycle shift, explains ~35% of this change | — |
| [[LoVo (line)]] | wt | 33.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.99× (z +9.3) | — |
| [[LS 180 (line)]] | wt | 26.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +10.7) ⚠ cell-cycle shift, explains ~35% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 28.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +9.8) ⚠ cell-cycle shift, explains ~35% of this change | — |
| [[NCI-H23 (line)]] | alt | 41.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.18× (z +9.9) | — |
| [[SK-MEL-2 (line)]] | alt | 40.5 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.350× (z -8.7) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[SW48 (line)]] | wt | 29.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.115× (z -12.4) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 24.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 36.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 22.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 30.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 40.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 31.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 62.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 23.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 25.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12714), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAML1]] | +0.57 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[RBM15]] | +0.52 | +0.34 / +0.54 | both halves | 1e-04 |  |
| [[AP4E1]] | +0.52 | +0.55 / +0.38 | both halves | 6e-05 |  |
| [[PDE12]] | +0.50 | +0.42 / +0.48 | both halves | 4e-05 |  |
| [[RSBN1]] | +0.50 | +0.47 / +0.48 | both halves | 2e-05 |  |
| [[INAFM2]] | +0.50 | +0.37 / +0.50 | both halves | 7e-05 |  |
| [[HOXA11]] | +0.49 | +0.48 / +0.42 | both halves | 4e-05 |  |
| [[FBXL14]] | +0.48 | +0.47 / +0.44 | both halves | 3e-05 |  |
| [[AKAP8L]] | +0.47 | +0.42 / +0.41 | both halves | 4e-05 |  |
| [[LIMD1]] | +0.47 | +0.39 / +0.39 | both halves | 6e-05 |  |
| [[CSTF1]] | +0.46 | +0.44 / +0.42 | both halves | 4e-05 |  |
| [[SPRY1]] | +0.46 | +0.53 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMC5]] | -0.44 | -0.36 / -0.41 | both halves | 1e-04 |  |
| [[RTN3]] | -0.42 | -0.37 / -0.43 | both halves | 8e-05 |  |
| [[MALAT1]] | -0.42 | -0.20 / -0.50 | ⚠ one half (not replicated) | 7e-04 |  |
| [[MBOAT2]] | -0.41 | -0.34 / -0.39 | both halves | 1e-04 |  |
| [[FAM161A]] | -0.41 | -0.29 / -0.40 | both halves | 3e-04 |  |
| [[EIF2S3]] | -0.40 | -0.33 / -0.40 | both halves | 1e-04 |  |
| [[TALAM1]] | -0.40 | -0.25 / -0.46 | both halves | 4e-04 |  |
| [[VAMP7]] | -0.40 | -0.32 / -0.40 | both halves | 2e-04 |  |
| [[DYNC1I2]] | -0.40 | -0.35 / -0.33 | both halves | 1e-04 |  |
| [[CAPG]] | -0.39 | -0.29 / -0.35 | both halves | 2e-04 |  |
| [[RABGAP1L]] | -0.39 | -0.27 / -0.35 | both halves | 3e-04 |  |
| [[STARD3NL]] | -0.39 | -0.27 / -0.42 | both halves | 3e-04 |  |
| [[RSRC1]] | -0.38 | -0.31 / -0.34 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 144]]; 32 genes; every member is in the + arm (projection on the module's main direction 0.551). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-56.9, -5.3); signed map (-3.7, 6.6). **Vector** length 88.3, 17.7% of its response variance represented; |z| ≥ 3 in 931 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.4 | +9.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.1 | +8.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.0 | +10.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.3 | +6.5 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.6 | +5.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.5 | +5.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.2 | +4.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.5 | +2.2 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.3 | -0.4 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | -5.2 | -7.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.0 | -4.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | -3.9 | -2.9 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -3.7 | -4.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -3.3 | -5.3 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.8 | -0.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.7 | -2.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.5 | -1.7 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -1.2 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | RUN domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.31 — chr17:42,980,565-42,995,142 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp761H0421 |
| Gene groups (HGNC) | RUN domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96C34](https://www.uniprot.org/uniprotkb/Q96C34) (RUN domain-containing protein 1):

> May play a role as p53/TP53 inhibitor and thus may have oncogenic activity.

**Summary**, from NCBI Gene [146923](https://www.ncbi.nlm.nih.gov/gene/146923):

> This gene encodes a protein that contains a RUN (RPIP8, UNC-14 and NESCA) domain and a coiled coil domain. The encoded protein may negatively regulate p53 transcriptional activity. This gene is a potential candidate gene for predisposition to glioma in humans. [provided by RefSeq, May 2017]

**Accessions** — [HGNC:25418](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25418) · Entrez [146923](https://www.ncbi.nlm.nih.gov/gene/146923) · UniProt [Q96C34](https://www.uniprot.org/uniprotkb/Q96C34) · Ensembl [ENSG00000198863](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198863)

## Data

Gene col 12714: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12714); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12714, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12714]; `tensor/DDL_lfc|DDL_z.npy` [12714]; `embed/gene_vectors.npy` [12714]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12714 or target_col == 12714). Every well: [[RUNDC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RUNDC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
