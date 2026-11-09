---
symbol: "DHX35"
type: "gene"
col: 2141
ensembl_id: "ENSG00000101452"
name: "DEAH-box helicase 35"
location: "20q11.23-q12"
module: 15
arm: "+"
pooled_cpm: 32.56
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 10
n_dd_up_clean: 16
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# DHX35

*DEAH-box helicase 35* — 20q11.23-q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.53× (z +10.7, q 4e-24, up in 37 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.569× (z -10.0, q 1e-20, down in 34 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.731× (z -7.9, q 7e-13, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRAPPC13]] (+0.74, fdr 7e-06), [[STARD7-AS1]] (+0.69, fdr 1e-05), [[QRSL1]] (+0.68, fdr 1e-05); moves opposite to [[SPAG9]] (-0.59, fdr 4e-05), [[IER2]] (-0.57, fdr 1e-05), [[JUNB]] (-0.56, fdr 1e-05).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2141.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.53×** | +10.7 | 4e-24 | 37/47 (SW1417, A498, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.77×** | +10.2 | 9e-22 | 40/48 (NCI-H1573, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.74×** | +9.8 | 3e-20 | 39/47 (NCI-H23, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.72×** | +9.6 | 1e-19 | 40/47 (NCI-H23, HOP62, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.60×** | +8.3 | 1e-14 | 36/47 (KATO III, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.57×** | +8.0 | 1e-13 | 37/48 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.53×** | +7.3 | 3e-11 | 29/47 (HEC-1-A, HOP62, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.54×** | +7.2 | 3e-11 | 36/48 (LOX-IMVI, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~8% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.50×** | +7.2 | 4e-11 | 33/48 (PANC-1, NCI-H460, …) | all doses, flat |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.48×** | +6.7 | 1e-09 | 24/48 (HEC-1-A, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.84×** | +5.7 | 7e-07 | 19/32 (NCI-H1573, HEC-1-A, …) | rises with dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.33×** | +5.0 | 2e-05 | 23/48 (HOP62, NCI-H23, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.32×** | +5.0 | 3e-05 | 24/47 (NCI-H2030, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~18% of this change | **1.29×** | +4.4 | 4e-04 | 20/46 (SW480, COLO 205, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.19× | +4.3 | 7e-04 | 18/48 (SW1417, A-172, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.26×** | +4.1 | 0.002 | 17/48 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.25×** | +4.0 | 0.002 | 20/47 (CFPAC-1, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.23×** | +3.7 | 0.006 | 20/48 (HT-29, SW480, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.23×** | +3.6 | 0.010 | 16/48 (NCI-H23, NCI-H460, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2141.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.569×** | -10.0 | 1e-20 | 34/46 (Panc 03.27, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.616×** | -8.3 | 4e-14 | 25/38 (LoVo, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.731×** | -7.9 | 7e-13 | 36/48 (NCI-H2347, NCI-H460, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.665×** | -6.7 | 3e-09 | 24/44 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.699×** | -6.4 | 2e-08 | 31/48 (SW480, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.764×** | -4.8 | 2e-04 | 23/48 (NCI-H460, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.774×** | -4.5 | 5e-04 | 24/48 (NCI-H2030, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.715×** | -4.2 | 0.002 | 15/48 (NCI-H1792, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **0.811×** | -3.7 | 0.013 | 20/48 (NCI-H460, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.817×** | -3.6 | 0.020 | 18/47 (SW48, CHP-212, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Entrectinib (drug)]] 5 µM |  | 0.839× | -3.1 | 0.094 | 11/47 (KATO III, SW48, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2141. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 61.0 | 4 (2 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.50× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.202× (z -15.8) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 67.7 | 2 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.67× (z +14.3) | [[Dinaciclib (drug)]] 0.5 µM 0.313× (z -12.0) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 28.6 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.73× (z +12.8) | — |
| [[J82 (line)]] | alt | 51.9 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.205× (z -15.1) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 31.1 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.72× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.184× (z -11.8) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 28.2 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.34× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.0627× (z -20.5) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 46.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Talc (drug)]] 0.5 µM 0.150× (z -8.6) |
| [[HOP62 (line)]] | alt | 19.3 | 1 | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.17× (z +8.6) | [[Dinaciclib (drug)]] 0.05 µM 0.262× (z -9.5) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 28.3 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 3.34× (z +9.1) | — |
| [[NCI-H2030 (line)]] | alt | 40.5 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +9.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.73× (z +9.2) | — |
| [[PANC-1 (line)]] | alt | 34.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.342× (z -11.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 29.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.285× (z -10.4) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 22.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.86× (z +13.2) | — |
| [[AsPC-1 (line)]] | alt | 17.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.01× (z +11.4) | — |
| [[C-33 A (line)]] | alt | 38.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.231× (z -9.2) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 42.5 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.31× (z +8.7) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 27.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.265× (z -9.8) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 21.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.146× (z -16.5) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 36.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.252× (z -12.3) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 34.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.398× (z -10.2) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 45.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.199× (z -12.9) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 44.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.174× (z -13.3) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 32.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.143× (z -13.6) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 26.6 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.153× (z -10.4) |
| [[SW480 (line)]] | alt | 49.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.465× (z -9.4) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 42.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 25.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 21.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 22.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 37.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 33.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 57.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 41.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 66.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 16.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2141), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRAPPC13]] | +0.74 | +0.67 / +0.65 | both halves | 7e-06 |  |
| [[STARD7-AS1]] | +0.69 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[QRSL1]] | +0.68 | +0.65 / +0.51 | both halves | 1e-05 |  |
| [[ANGEL2]] | +0.62 | +0.58 / +0.46 | both halves | 3e-05 |  |
| [[TMEM11-DT]] | +0.62 | +0.55 / +0.43 | both halves | 3e-05 |  |
| [[C2orf42]] | +0.62 | +0.52 / +0.46 | both halves | 3e-05 |  |
| [[RCC1L]] | +0.62 | +0.56 / +0.38 | both halves | 7e-05 |  |
| [[EPM2A]] | +0.59 | +0.48 / +0.34 | both halves | 1e-04 |  |
| [[C8orf76]] | +0.59 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[FAHD2A]] | +0.59 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[TMEM267]] | +0.59 | +0.49 / +0.45 | both halves | 3e-05 |  |
| [[ASH2L]] | +0.58 | +0.59 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPAG9]] | -0.59 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[IER2]] | -0.57 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[JUNB]] | -0.56 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[SYAP1]] | -0.56 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[STARD5]] | -0.54 | -0.38 / -0.34 | both halves | 1e-04 |  |
| [[SYT5]] | -0.54 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[EZR]] | -0.53 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[BCL10]] | -0.53 | -0.62 / -0.45 | both halves | 3e-05 |  |
| [[IER3]] | -0.53 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[PJA2]] | -0.53 | -0.39 / -0.39 | both halves | 6e-05 |  |
| [[NBEAL1]] | -0.53 | -0.44 / -0.33 | both halves | 1e-04 |  |
| [[NR4A1]] | -0.53 | -0.48 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises DHX35's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises DHX35's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TOP2A]] | B | TOP2A activity lowers DHX35's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.592). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-9.4, 16.4); signed map (23.9, -23.7). **Vector** length 102, 25.2% of its response variance represented; |z| ≥ 3 in 1,079 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.4 | +10.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +7.1 | +7.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +5.5 | +6.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.7 | +4.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~18% of this change | +4.7 | +4.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.2 | +1.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.0 | +2.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.8 | +2.6 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.7 | +2.7 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -6.4 | -7.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -6.2 | -6.4 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -5.3 | -1.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -5.0 | -4.8 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.9 | -4.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -3.2 | -2.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.2 | -1.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.7 | +0.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.2 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | DEAH-box helicase 35 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q11.23-q12 — chr20:38,962,299-39,039,723 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ22759, KAIA0875; previously C20orf15, DDX35 |
| Gene groups (HGNC) | DEAH-box helicases; Spliceosomal C complex |
| Reactome | 4 pathways, smallest: mRNA Splicing - Major Pathway; mRNA Splicing; Processing of Capped Intron-Containing Pre-mRNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H5Z1](https://www.uniprot.org/uniprotkb/Q9H5Z1) (Probable ATP-dependent RNA helicase DHX35):

> Acts as a co-sensor in RIGI-mediated antiviral innate immunity. Enhances RIGI recognition of viral nucleic acids and interacts with RIGI and MAVS to form a signaling complex which triggers downstream signaling cascades that lead to the induction of type I interferons and pro-inflammatory cytokines during the antiviral innate immune response.

**Summary**, from NCBI Gene [60625](https://www.ncbi.nlm.nih.gov/gene/60625):

> DEAD box proteins characterized by the conserved motif Asp-Glu-Ala-Asp (DEAD), are putative RNA helicases. They are implicated in a number of cellular processes involving alteration of RNA secondary structure such as translation initiation, nuclear and mitochondrial splicing, and ribosome and spliceosome assembly. Based on their distribution patterns, some members of the DEAD box protein family are believed to be involved in embryogenesis, spermatogenesis, and cellular growth and division. The …

**Accessions** — [HGNC:15861](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15861) · Entrez [60625](https://www.ncbi.nlm.nih.gov/gene/60625) · UniProt [Q9H5Z1](https://www.uniprot.org/uniprotkb/Q9H5Z1) · Ensembl [ENSG00000101452](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101452)

## Data

Gene col 2141: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2141); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2141, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2141]; `tensor/DDL_lfc|DDL_z.npy` [2141]; `embed/gene_vectors.npy` [2141]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2141 or target_col == 2141). Every well: [[DHX35 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DHX35.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
