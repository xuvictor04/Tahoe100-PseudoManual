---
symbol: "SYCP2"
type: "gene"
col: 12125
ensembl_id: "ENSG00000196074"
name: "synaptonemal complex protein 2"
location: "20q13.33"
module: 10
arm: "+"
pooled_cpm: 24.39
n_lines_expressing: 35
n_dd_up: 15
n_dd_down: 19
n_dd_up_clean: 12
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 1
direction_downstream: 5
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# SYCP2

*synaptonemal complex protein 2* — 20q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.01× (z +16.4, q 0e+00, up in 16 of 25 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.85× (z +12.9, q 9e-36, up in 18 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (7 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.538× (z -9.2, q 2e-17, down in 27 of 32 measured lines).
> Its strongest partners by |cos| (82 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 19 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDH26]] (+0.56, fdr 3e-05, ⚠ same locus), [[LINC00466]] (+0.55, fdr 4e-05), [[FAM184A]] (+0.54, fdr 2e-05), [[ABCA17P]] (+0.52, fdr 1e-04); moves opposite to [[TRAPPC1]] (-0.47, fdr 1e-04), [[HTRA2]] (-0.46, fdr 3e-04), [[VPS33B]] (-0.43, fdr 1e-04).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ANKRD20A21P]] → it (grade B ⚠); 5 go from it, the strongest it → [[ANKRD20A11P]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 3 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12125.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.01×** | +16.4 | 0e+00 | 16/25 (NCI-H2347, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.85×** | +12.9 | 9e-36 | 18/32 (HT-29, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.38×** | +12.4 | 3e-33 | 12/16 (NCI-H2347, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.17×** | +10.7 | 2e-24 | 11/20 (NCI-H2347, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.42×** | +7.4 | 1e-11 | 15/33 (NCI-H1573, C-33 A, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.49×** | +5.8 | 8e-07 | 14/31 (LoVo, NCI-H23, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.38×** | +4.8 | 2e-04 | 12/32 (A498, Panc 03.27, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.37×** | +4.7 | 2e-04 | 14/32 (LoVo, A498, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.33×** | +4.2 | 0.002 | 8/30 (LoVo, KATO III, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.30×** | +3.9 | 0.006 | 16/31 (Panc 03.27, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Isocorydine (drug)]] 0.5 µM |  | **1.28×** | +3.7 | 0.011 | 5/31 (C32, AN3 CA, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.18× | +3.5 | 0.022 | 9/32 (LoVo, HT-29, …) | all doses, flat |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.26×** | +3.5 | 0.022 | 5/32 (A498, SW1417, …) | rises with dose |  |
| [[Vitamin K4 (drug)]] 0.05 µM |  | **1.26×** | +3.5 | 0.022 | 2/32 (A498, HCT15) | inconsistent across doses |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **1.24×** | +3.2 | 0.049 | 4/31 (BT-474, RPMI-7951, …) | inconsistent across doses |  |
| [[Lactate (calcium) (drug)]] 0.05 µM |  | **1.23×** | +3.1 | 0.069 | 3/32 (A498, NCI-H2030, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | 1.18× | +3.1 | 0.076 | 4/33 (LoVo, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12125.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.538×** | -9.2 | 2e-17 | 27/32 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.552×** | -8.8 | 3e-16 | 23/31 (PANC-1, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.567×** | -8.5 | 5e-15 | 23/32 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.608×** | -7.4 | 2e-11 | 19/32 (NCI-H23, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.398×** | -7.2 | 8e-11 | 20/30 (A-427, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.642×** | -6.6 | 4e-09 | 19/30 (C-33 A, NCI-H23, …) | two highest doses | cell-cycle shift (explains ~6% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.439×** | -6.4 | 1e-08 | 20/31 (A-427, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.712×** | -5.0 | 3e-05 | 15/32 (NCI-H2030, NCI-H23, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.744×** | -4.4 | 7e-04 | 14/32 (COLO 205, NCI-H23, …) | two highest doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.754×** | -4.2 | 0.002 | 13/31 (PANC-1, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.749×** | -4.1 | 0.002 | 11/31 (NCI-H23, NCI-H2030, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.779×** | -3.7 | 0.010 | 9/32 (NCI-H23, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.792×** | -3.5 | 0.023 | 10/32 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.795×** | -3.4 | 0.026 | 15/32 (NCI-H2030, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Fluvoxamine (maleate) (drug)]] 0.5 µM |  | **0.801×** | -3.3 | 0.036 | 10/31 (NCI-H460, RPMI-7951, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.744×** | -3.1 | 0.056 | 0/33 | rises with dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.818×** | -3.0 | 0.087 | 10/31 (HT-29, BT-474, …) | rises with dose |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **0.812×** | -3.0 | 0.087 | 7/32 (COLO 205, H4, …) | top dose only | plate-row cell shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12125. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 27.2 | 0 | 7 (3 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.183× (z -10.8) |
| [[PANC-1 (line)]] | alt | 178 | 0 | 7 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.336× (z -20.2) |
| [[A-427 (line)]] | wt | 77.1 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -17.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.266× (z -13.2) |
| [[HT-29 (line)]] | alt | 21.4 | 1 | 4 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.26× (z +8.8) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.163× (z -9.5) |
| [[NCI-H2030 (line)]] | alt | 22.4 | 0 | 4 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.219× (z -10.4) |
| [[NCI-H2347 (line)]] | alt | 82.6 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.75× (z +12.3) ⚠ toxic; transcription drop | [[Selinexor (drug)]] 5 µM 0.570× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 21.5 | 0 | 3 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.192× (z -8.8) |
| [[C32 (line)]] | wt | 16.0 | 0 | 2 (1 ⚠) | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0939× (z -10.5) |
| [[LoVo (line)]] | wt | 12.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.202× (z -8.9) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 7.00 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.14× (z +8.5) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 24.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.213× (z -9.3) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 3.35 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 9.49 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.07 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.25 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.87 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 48.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.67 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.56 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.29 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.35 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.54 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 4.24 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 5.16 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.52 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.06 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.53 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.16 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.61 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.07 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 5.68 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 225 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.06 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.28 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.15 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 6.49 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.16 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 271 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.19 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.56 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.08 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 4.76 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12125), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 18 of them with an alert (⚠; 17 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDH26]] | +0.56 | +0.46 / +0.43 | both halves | 3e-05 | ⚠ same locus (24.8 kb: neighbours can correlate without regulation) |
| [[LINC00466]] | +0.55 | +0.49 / +0.41 | both halves | 4e-05 |  |
| [[FAM184A]] | +0.54 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[ABCA17P]] | +0.52 | +0.43 / +0.35 | both halves | 1e-04 |  |
| [[EFHD1]] | +0.51 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[LRIG3-DT]] | +0.50 | +0.50 / +0.39 | both halves | 5e-05 |  |
| [[DHRS4L2]] | +0.49 | +0.44 / +0.35 | both halves | 1e-04 |  |
| [[ANKRD20A21P]] | +0.49 | +0.44 / +0.33 | both halves | 1e-04 |  |
| [[BCLAF1]] | +0.49 | +0.50 / +0.16 | ⚠ one half (not replicated) | 0.001 |  |
| [[ZCWPW1]] | +0.49 | +0.53 / +0.23 | both halves | 5e-04 |  |
| [[GPLD1]] | +0.49 | +0.36 / +0.45 | both halves | 1e-04 |  |
| [[KATNAL2]] | +0.48 | +0.58 / +0.33 | both halves | 1e-04 |  |
| [[GALC]] | +0.48 | +0.45 / +0.34 | both halves | 1e-04 |  |
| [[BEND6]] | +0.48 | +0.48 / +0.35 | both halves | 1e-04 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRAPPC1]] | -0.47 | -0.43 / -0.33 | both halves | 1e-04 |  |
| [[HTRA2]] | -0.46 | -0.28 / -0.34 | both halves | 3e-04 |  |
| [[VPS33B]] | -0.43 | -0.36 / -0.33 | both halves | 1e-04 |  |
| [[KCTD10]] | -0.41 | -0.34 / -0.40 | both halves | 1e-04 |  |
| [[CD68]] | -0.41 | -0.39 / -0.33 | both halves | 1e-04 |  |
| [[TNFAIP1]] | -0.40 | -0.30 / -0.42 | both halves | 2e-04 |  |
| [[EMC4]] | -0.40 | -0.28 / -0.37 | both halves | 3e-04 |  |
| [[CIAO2B]] | -0.40 | -0.29 / -0.23 | both halves | 5e-04 |  |
| [[TUSC2]] | -0.40 | -0.30 / -0.24 | both halves | 5e-04 |  |
| [[TMEM92]] | -0.40 | -0.34 / -0.32 | both halves | 2e-04 |  |
| [[DYNLT1]] | -0.40 | -0.37 / -0.25 | both halves | 4e-04 |  |
| [[PRRG1]] | -0.40 | -0.42 / -0.18 | ⚠ not reproduced | 9e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANKRD20A21P]] | B | ANKRD20A21P activity raises SYCP2's level | lines that do not express ANKRD20A21P (30) vs lines expressing it (20) | 2.46× lower at baseline in the lines without ANKRD20A21P | 0.079 | ⚠ within organs, on part of the lines; also absent: ENSG00000229618, PAX2, ANKRD20A11P |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANKRD20A11P]] | B | SYCP2 activity raises ANKRD20A11P's level | lines that do not express SYCP2 (15) vs lines expressing it (35) | 1.97× lower at baseline in the lines without SYCP2 | 0.049 | ⚠ within organs, on part of the lines; also absent: AMOT, LINC00937, DMBX1; maybe low, not absent |
| [[CABLES1]] | B | SYCP2 activity raises CABLES1's level | lines that do not express SYCP2 (15) vs lines expressing it (35) | 1.98× lower at baseline in the lines without SYCP2 | 0.054 | ⚠ within organs, on part of the lines; also absent: AMOT, LINC00937, DMBX1; maybe low, not absent |
| [[CREB3L4]] | B | SYCP2 activity raises CREB3L4's level | lines that do not express SYCP2 (15) vs lines expressing it (35) | 1.42× lower at baseline in the lines without SYCP2 | 0.092 | ⚠ within organs, on part of the lines; also absent: AMOT, LINC00937, DMBX1; maybe low, not absent |
| [[EMC4]] | B | SYCP2 activity raises EMC4's level | lines that do not express SYCP2 (15) vs lines expressing it (35) | 1.22× lower at baseline in the lines without SYCP2 | 0.096 | ⚠ within organs, on part of the lines; also absent: AMOT, LINC00937, DMBX1; maybe low, not absent |
| [[SYT9-AS1]] | B | SYCP2 activity raises SYT9-AS1's level | lines that do not express SYCP2 (15) vs lines expressing it (35) | 1.68× lower at baseline in the lines without SYCP2 | 0.096 | ⚠ within organs, on part of the lines; also absent: AMOT, LINC00937, DMBX1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.374). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (7.4, 31.8); signed map (37.0, -10.9). **Vector** length 59.2, 10.7% of its response variance represented; |z| ≥ 3 in 782 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.0 | +16.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.9 | +12.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.4 | +10.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.6 | +7.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.1 | -0.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.8 | +4.7 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.1 | +4.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.4 | +5.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.3 | +3.5 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -2.8 | -6.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.0 | -5.0 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.8 | -0.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | -1.6 | -4.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -1.6 | -4.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.5 | -2.8 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.4 | -3.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.3 | -2.5 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.1 | -1.8 |
|  | [[Belzutifan (drug)]] 5 µM |  | -1.1 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | synaptonemal complex protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.33 — chr20:59,863,564-59,933,655 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SCP2 |
| Reactome | 4 pathways, smallest: Meiotic synapsis; Meiosis; Reproduction |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BX26](https://www.uniprot.org/uniprotkb/Q9BX26) (Synaptonemal complex protein 2):

> Major component of the axial/lateral elements of synaptonemal complexes (SCS) during meiotic prophase. Plays a role in the assembly of synaptonemal complexes. Required for normal meiotic chromosome synapsis during oocyte and spermatocyte development and for normal male and female fertility. Required for insertion of SYCP3 into synaptonemal complexes. May be involved in the organization of chromatin by temporarily binding to DNA scaffold attachment regions. Requires SYCP3, but not SYCP1, in …

**Summary**, from NCBI Gene [10388](https://www.ncbi.nlm.nih.gov/gene/10388):

> The synaptonemal complex is a proteinaceous structure that links homologous chromosomes during the prophase of meiosis. The protein encoded by this gene is a major component of the synaptonemal complex and may bind DNA at scaffold attachment regions. The encoded protein requires synaptonemal complex protein 3, but not 1, for inclusion in the synaptonemal complex. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:11490](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11490) · Entrez [10388](https://www.ncbi.nlm.nih.gov/gene/10388) · UniProt [Q9BX26](https://www.uniprot.org/uniprotkb/Q9BX26) · Ensembl [ENSG00000196074](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196074)

## Data

Gene col 12125: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12125); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12125, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12125]; `tensor/DDL_lfc|DDL_z.npy` [12125]; `embed/gene_vectors.npy` [12125]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12125 or target_col == 12125). Every well: [[SYCP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SYCP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
