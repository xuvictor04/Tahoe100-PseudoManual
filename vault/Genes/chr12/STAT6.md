---
symbol: "STAT6"
type: "gene"
col: 9379
ensembl_id: "ENSG00000166888"
name: "signal transducer and activator of transcription 6"
location: "12q13.3"
module: 68
arm: "+"
pooled_cpm: 49.89
n_lines_expressing: 48
n_dd_up: 8
n_dd_down: 31
n_dd_up_clean: 5
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/068"]
generated_by: "tahoemap"
---

# STAT6

*signal transducer and activator of transcription 6* — 12q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.68× (z +8.7, q 1e-15, up in 25 of 38 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ipatasertib (drug)]] 0.5 µM: 1.39× (z +4.2, q 0.006, up in 21 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 31 drug-doses (13 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.196× (z -28.4, q 0e+00, down in 44 of 46 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MVP-DT]] (+0.60, fdr 1e-05), [[FMO4]] (+0.60, fdr 3e-05), [[SLC9A8]] (+0.59, fdr 2e-05); moves opposite to [[POGLUT2]] (-0.58, fdr 1e-05), [[VLDLR]] (-0.57, fdr 8e-05), [[TAF5L]] (-0.57, fdr 6e-05).
> It sits in the **+** arm of [[Module 068]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[KMO]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9379.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.68×** | +8.7 | 1e-15 | 25/38 (HepG2/C3A, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.43×** | +6.3 | 1e-07 | 29/45 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.39×** | +4.2 | 0.006 | 21/44 (A-427, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.37×** | +4.0 | 0.011 | 15/43 (NCI-H460, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.22×** | +3.4 | 0.056 | 19/44 (A549, AsPC-1, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | 1.15× | +3.4 | 0.056 | 13/46 (SW480, SW1417, …) | all doses, flat | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.21×** | +3.3 | 0.068 | 12/45 (LoVo, LS 180, …) | two highest doses | low cells (technical?) |
| [[Belumosudil (drug)]] 5 µM |  | **1.21×** | +3.3 | 0.077 | 15/46 (NCI-H2347, J82, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.22×** | +3.2 | 0.089 | 19/41 (J82, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 15 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 31 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9379.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.196×** | -28.4 | 0e+00 | 44/46 (NCI-H460, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.225×** | -26.0 | 0e+00 | 43/46 (HT-29, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.268×** | -23.0 | 0e+00 | 44/46 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.496×** | -11.5 | 2e-28 | 41/46 (SW1417, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.684×** | -9.3 | 1e-18 | 29/45 (CFPAC-1, COLO 205, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.602×** | -8.8 | 1e-16 | 36/46 (COLO 205, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.344×** | -8.3 | 6e-15 | 35/47 (Panc 03.27, CFPAC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.624×** | -8.2 | 2e-14 | 36/45 (SK-MEL-2, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.627×** | -8.1 | 3e-14 | 38/46 (LoVo, PANC-1, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.382×** | -7.5 | 3e-12 | 38/47 (HT-29, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.651×** | -7.5 | 4e-12 | 29/45 (NCI-H1573, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~41% of this change | **0.646×** | -7.3 | 1e-11 | 29/43 (H4, Panc 03.27, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.668×** | -7.0 | 1e-10 | 32/46 (A-427, LoVo, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.439×** | -6.4 | 5e-09 | 32/44 (Panc 03.27, COLO 205, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.698×** | -6.3 | 2e-08 | 33/46 (NCI-H460, SW 1088, …) | all doses, flat |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.737×** | -5.3 | 4e-06 | 26/45 (HT-29, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[EX229 (drug)]] 5 µM |  | **0.550×** | -4.7 | 7e-05 | 20/46 (NCI-H460, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.785×** | -4.2 | 7e-04 | 20/46 (NCI-H460, MIA PaCa-2, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.776×** | -4.2 | 7e-04 | 22/45 (NCI-H1573, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[TAK-733 (drug)]] 5 µM |  | **0.622×** | -3.7 | 0.004 | 17/45 (PANC-1, Hs 766T, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.57 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9379. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 82.5 | 0 | 10 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.135× (z -22.9) |
| [[Panc 03.27 (line)]] | alt | 93.6 | 0 | 9 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.172× (z -20.2) |
| [[COLO 205 (line)]] | alt | 93.8 | 0 | 8 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0791× (z -20.6) |
| [[LOX-IMVI (line)]] | wt | 74.7 | 0 | 8 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.188× (z -15.9) |
| [[SW1417 (line)]] | alt | 73.2 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.264× (z -13.9) |
| [[SW480 (line)]] | alt | 22.7 | 2 (2 ⚠) | 5 | [[Dinaciclib (drug)]] 0.5 µM 3.13× (z +11.2) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.223× (z -14.6) |
| [[A-427 (line)]] | wt | 58.9 | 1 (1 ⚠) | 5 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.45× (z +8.5) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.175× (z -17.2) |
| [[CFPAC-1 (line)]] | alt | 80.1 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -17.8) |
| [[HT-29 (line)]] | alt | 88.9 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.108× (z -22.2) |
| [[NCI-H23 (line)]] | alt | 56.1 | 0 | 6 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.139× (z -16.8) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.170× (z -16.3) |
| [[SK-MEL-2 (line)]] | alt | 48.1 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.123× (z -18.1) |
| [[HEC-1-A (line)]] | alt | 74.4 | 0 | 5 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.204× (z -18.0) |
| [[KATO III (line)]] | alt | 50.4 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.103× (z -20.5) |
| [[LS 180 (line)]] | wt | 104 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.106× (z -23.1) |
| [[NCI-H1573 (line)]] | alt | 80.1 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.192× (z -17.4) |
| [[NCI-H460 (line)]] | wt | 50.0 | 1 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.63× (z +8.8) | [[Panobinostat (drug)]] 5 µM 0.137× (z -25.2) |
| [[RKO (line)]] | wt | 60.4 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.169× (z -15.4) |
| [[HS-578T (line)]] | alt | 32.1 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.114× (z -16.7) |
| [[MIA PaCa-2 (line)]] | alt | 32.9 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.198× (z -12.2) |
| [[NCI-H1792 (line)]] | alt | 36.6 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.133× (z -16.3) |
| [[SNU-423 (line)]] | alt | 49.7 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.0965× (z -18.9) |
| [[A-172 (line)]] | wt | 25.4 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.257× (z -10.2) |
| [[A498 (line)]] | wt | 39.8 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.325× (z -9.9) |
| [[A549 (line)]] | wt | 42.1 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.244× (z -11.0) |
| [[AsPC-1 (line)]] | alt | 97.0 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.192× (z -16.5) |
| [[C32 (line)]] | wt | 32.5 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.147× (z -14.1) |
| [[HOP62 (line)]] | alt | 28.5 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.166× (z -15.1) |
| [[Hs 766T (line)]] | wt | 32.7 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.117× (z -14.9) |
| [[hTERT-HPNE (line)]] | wt | 60.7 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.150× (z -13.7) |
| [[J82 (line)]] | alt | 61.1 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.221× (z -15.1) |
| [[NCI-H2347 (line)]] | alt | 59.2 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.285× (z -13.8) |
| [[PANC-1 (line)]] | alt | 22.5 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.331× (z -10.1) |
| [[RPMI-7951 (line)]] | alt | 49.7 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.121× (z -17.2) |
| [[H4 (line)]] | wt | 25.5 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0846× (z -11.9) ⚠ toxic; cell-cycle shift, explains ~41% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.147× (z -9.6) |
| [[HCT15 (line)]] | alt | 46.2 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.219× (z -10.0) |
| [[NCI-H2030 (line)]] | alt | 35.4 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.249× (z -10.8) |
| [[SNU-1 (line)]] | wt | 29.4 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.123× (z -15.9) ⚠ cell-cycle shift, explains ~54% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.145× (z -10.3) |
| [[SW 1088 (line)]] | alt | 47.3 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.0491× (z -9.0) |
| [[HepG2_C3A (line)]] | wt | 35.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.23× (z +12.0) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 36.6 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.246× (z -9.7) |
| [[SW48 (line)]] | wt | 24.3 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.154× (z -9.2) |
| [[AN3 CA (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.36 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 62.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 49.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.98 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 15.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9379), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MVP-DT]] | +0.60 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[FMO4]] | +0.60 | +0.44 / +0.45 | both halves | 3e-05 |  |
| [[SLC9A8]] | +0.59 | +0.53 / +0.46 | both halves | 2e-05 |  |
| [[TAPBPL]] | +0.58 | +0.48 / +0.42 | both halves | 4e-05 |  |
| [[SLC43A2]] | +0.58 | +0.39 / +0.49 | both halves | 5e-05 |  |
| [[STX4]] | +0.57 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[SLC12A7]] | +0.56 | +0.47 / +0.46 | both halves | 3e-05 |  |
| [[CFLAR]] | +0.56 | +0.42 / +0.48 | both halves | 4e-05 |  |
| [[CHMP4B]] | +0.55 | +0.41 / +0.54 | both halves | 4e-05 |  |
| [[SPTY2D1OS]] | +0.55 | +0.37 / +0.32 | both halves | 1e-04 |  |
| [[C7orf31]] | +0.54 | +0.46 / +0.39 | both halves | 5e-05 |  |
| [[LINC01725]] | +0.54 | +0.46 / +0.32 | both halves | 2e-04 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POGLUT2]] | -0.58 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[VLDLR]] | -0.57 | -0.40 / -0.37 | both halves | 8e-05 |  |
| [[TAF5L]] | -0.57 | -0.38 / -0.50 | both halves | 6e-05 |  |
| [[PLEKHA8]] | -0.55 | -0.47 / -0.46 | both halves | 2e-05 |  |
| [[TTC13]] | -0.55 | -0.50 / -0.59 | both halves | 1e-05 |  |
| [[ATRN]] | -0.53 | -0.34 / -0.47 | both halves | 1e-04 |  |
| [[WASF3]] | -0.53 | -0.39 / -0.43 | both halves | 6e-05 |  |
| [[NME2]] | -0.53 | -0.39 / -0.39 | both halves | 6e-05 |  |
| [[SOCS7]] | -0.52 | -0.45 / -0.40 | both halves | 5e-05 | same gene group |
| [[EEF1AKMT4]] | -0.52 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[L2HGDH]] | -0.52 | -0.30 / -0.54 | both halves | 2e-04 |  |
| [[MTERF3]] | -0.52 | -0.43 / -0.47 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KMO]] | B | KMO activity raises STAT6's level | lines that do not express KMO (18) vs lines expressing it (32) | 1.51× lower at baseline in the lines without KMO | 0.013 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: SRPX2, IL1R1, TRIM6; maybe low, not absent |
| [[SLC2A6]] | B | SLC2A6 activity lowers STAT6's level | lines that do not express SLC2A6 (6) vs lines expressing it (44) | 1.86× higher at baseline in the lines without SLC2A6 | 0.096 | ⚠ within organs, on part of the lines; also absent: GFOD1, SOAT1, RGS9; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 068]]; 73 genes; this gene is in the **+** arm (projection on the module's main direction 0.525). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (11.5, 7.2); signed map (15.3, -20.4). **Vector** length 81.0, 20.7% of its response variance represented; |z| ≥ 3 in 1,163 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.3 | +8.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.2 | +6.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.4 | -9.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.2 | +3.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +4.7 | -2.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.5 | -0.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.3 | +4.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | -0.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.3 | +0.0 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.1 | +2.7 |
| fall | [[Panobinostat (drug)]] 0.05 µM |  | -3.1 | -11.5 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -3.1 | -8.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.0 | -6.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.4 | -7.5 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.3 | -23.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.0 | -3.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.8 | -3.7 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.7 | -2.7 |
|  | [[EX229 (drug)]] 5 µM |  | -1.7 | -4.7 |

## What is on record

|  |  |
|---|---|
| Name | signal transducer and activator of transcription 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.3 — chr12:57,095,408-57,132,139 (-) |
| Ensembl biotype | protein_coding |
| Also known as | D12S1644, IL-4-STAT |
| Gene groups (HGNC) | SH2 domain containing; Signal transducer and activator of transcription family |
| Reactome | 16 pathways, smallest: STAT6-mediated induction of chemokines; STING mediated induction of host immune responses; Downstream signal transduction |
| Matched by | ensembl_id |

**Function**, from UniProt [P42226](https://www.uniprot.org/uniprotkb/P42226) (Signal transducer and activator of transcription 6):

> Carries out a dual function: signal transduction and activation of transcription. Involved in IL4/interleukin-4- and IL3/interleukin-3-mediated signaling.

**Summary**, from NCBI Gene [6778](https://www.ncbi.nlm.nih.gov/gene/6778):

> The protein encoded by this gene is a member of the STAT family of transcription factors. In response to cytokines and growth factors, STAT family members are phosphorylated by the receptor associated kinases, and then form homo- or heterodimers that translocate to the cell nucleus where they act as transcription activators. This protein plays a central role in exerting IL4 mediated biological responses. It is found to induce the expression of BCL2L1/BCL-X(L), which is responsible for the …

**Accessions** — [HGNC:11368](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11368) · Entrez [6778](https://www.ncbi.nlm.nih.gov/gene/6778) · UniProt [P42226](https://www.uniprot.org/uniprotkb/P42226) · Ensembl [ENSG00000166888](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166888)

## Data

Gene col 9379: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9379); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9379, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9379]; `tensor/DDL_lfc|DDL_z.npy` [9379]; `embed/gene_vectors.npy` [9379]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9379 or target_col == 9379). Every well: [[STAT6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STAT6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
