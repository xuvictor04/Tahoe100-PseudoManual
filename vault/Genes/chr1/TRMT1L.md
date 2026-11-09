---
symbol: "TRMT1L"
type: "gene"
col: 4278
ensembl_id: "ENSG00000121486"
name: "tRNA methyltransferase 1L"
location: "1q25.3"
module: 28
arm: "+"
pooled_cpm: 31.02
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 24
n_dd_up_clean: 13
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# TRMT1L

*tRNA methyltransferase 1L* — 1q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (1 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 1.89× (z +10.2, q 1e-21, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.458× (z -11.5, q 5e-28, down in 30 of 40 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.510× (z -10.8, q 1e-24, down in 35 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PPCS]] (+0.73, fdr 7e-06), [[C1orf131]] (+0.72, fdr 7e-06), [[REST]] (+0.71, fdr 7e-06); moves opposite to [[TCF3]] (-0.70, fdr 7e-06), [[FAM20B]] (-0.68, fdr 7e-06), [[RBM14-RBM4]] (-0.68, fdr 7e-06).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 2 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4278.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **1.89×** | +10.2 | 1e-21 | 42/48 (NCI-H2347, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.86×** | +9.6 | 3e-19 | 37/47 (A-427, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.64×** | +8.0 | 3e-13 | 38/48 (A-427, NCI-H2347, …) | all doses, flat |  |
| [[Selinexor (drug)]] 5 µM |  | **1.42×** | +7.9 | 4e-13 | 37/48 (SNU-423, C32, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.59×** | +7.5 | 1e-11 | 34/47 (RKO, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.34×** | +6.5 | 6e-09 | 28/47 (A-427, C32, …) | all doses, flat | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.20×** | +4.2 | 0.003 | 18/48 (RKO, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.29×** | +4.0 | 0.005 | 18/47 (C32, KATO III, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.27×** | +3.8 | 0.010 | 18/48 (KATO III, A-172, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.27×** | +3.8 | 0.010 | 18/48 (KATO III, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 5 µM |  | **1.25×** | +3.7 | 0.012 | 12/48 (C32, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.22×** | +3.7 | 0.012 | 21/48 (SW480, C32, …) | two highest doses | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.28×** | +3.6 | 0.012 | 18/47 (A549, SW480, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.23×** | +3.3 | 0.038 | 14/48 (SW480, NCI-H2347, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +3.2 | 0.060 | 18/48 (C32, SW480, …) | two highest doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 9 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4278.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.458×** | -11.5 | 5e-28 | 30/40 (Hs 766T, hTERT-HPNE, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.510×** | -10.8 | 1e-24 | 35/47 (MIA PaCa-2, SW480, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.418×** | -7.3 | 6e-11 | 33/49 (Hs 766T, A-427, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.636×** | -7.2 | 6e-11 | 34/48 (COLO 205, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.442×** | -6.8 | 1e-09 | 31/47 (C32, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.655×** | -6.8 | 1e-09 | 30/47 (AsPC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.468×** | -6.4 | 2e-08 | 20/33 (C-33 A, NCI-H1573, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.694×** | -5.8 | 4e-07 | 27/48 (KATO III, SW480, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.691×** | -5.7 | 8e-07 | 26/45 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.704×** | -5.6 | 1e-06 | 27/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.697×** | -5.4 | 3e-06 | 29/48 (AN3 CA, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.719×** | -5.3 | 7e-06 | 31/47 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.757×** | -4.5 | 4e-04 | 24/48 (Hs 766T, NCI-H460, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.767×** | -4.1 | 0.002 | 20/35 (C32, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~4% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.767×** | -4.1 | 0.002 | 20/46 (NCI-H23, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.642×** | -3.7 | 0.007 | 19/46 (Hs 766T, RKO, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.736×** | -3.4 | 0.020 | 14/48 (MIA PaCa-2, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[NVP-BHG712 (drug)]] 0.05 µM |  | **0.806×** | -3.2 | 0.033 | 12/48 (A498, SHP-77, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **0.700×** | -3.0 | 0.077 | 16/47 (SW 900, C-33 A, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.706×** | -2.9 | 0.090 | 9/48 (SW480, A498, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.769×** | -2.9 | 0.090 | 8/48 (NCI-H460, LS 180, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 0.05 µM |  | **0.827×** | -2.9 | 0.097 | 5/48 (LoVo, Hs 766T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4278. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 32.4 | 1 | 7 (3 ⚠) | [[Harringtonine (drug)]] 5 µM 2.34× (z +8.8) | [[Digitoxin (drug)]] 5 µM 0.317× (z -12.3) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.394× (z -10.0) |
| [[NCI-H460 (line)]] | wt | 41.1 | 0 | 6 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.373× (z -11.1) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.385× (z -10.7) |
| [[COLO 205 (line)]] | alt | 34.3 | 0 | 5 (4 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.163× (z -11.6) |
| [[KATO III (line)]] | alt | 31.4 | 0 | 4 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.206× (z -12.9) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.271× (z -11.1) |
| [[A-427 (line)]] | wt | 45.7 | 2 (1 ⚠) | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 3.31× (z +11.3) | [[Dinaciclib (drug)]] 5 µM 0.229× (z -14.0) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 56.8 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +9.5) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.57× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.0648× (z -19.4) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 47.1 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0952× (z -19.7) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.390× (z -8.5) |
| [[MIA PaCa-2 (line)]] | alt | 39.7 | 0 | 2 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.270× (z -10.7) |
| [[NCI-H23 (line)]] | alt | 32.3 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0700× (z -20.9) ⚠ toxic |
| [[Panc 03.27 (line)]] | alt | 34.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.181× (z -14.6) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 27.2 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.388× (z -9.0) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.418× (z -9.0) |
| [[A-172 (line)]] | wt | 41.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.370× (z -9.0) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 39.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.408× (z -8.6) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 25.2 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.0778× (z -8.8) |
| [[AsPC-1 (line)]] | alt | 21.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.112× (z -13.2) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 29.2 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0498× (z -9.2) ⚠ toxic |
| [[H4 (line)]] | wt | 30.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.148× (z -9.3) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 25.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.255× (z -9.7) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 33.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.333× (z -9.8) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 15.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.106× (z -12.8) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 27.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.102× (z -13.7) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 28.9 | 1 | 0 | [[Harringtonine (drug)]] 0.5 µM 2.52× (z +8.5) | — |
| [[LS 180 (line)]] | wt | 22.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.209× (z -10.4) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 35.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.304× (z -9.2) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 28.6 | 0 | 1 (1 ⚠) | — | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.0985× (z -9.1) ⚠ toxic |
| [[NCI-H2030 (line)]] | alt | 24.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +8.7) ⚠ cell-cycle shift, explains ~39% of this change | — |
| [[NCI-H2347 (line)]] | alt | 32.8 | 1 | 0 | [[Harringtonine (drug)]] 0.5 µM 2.55× (z +9.4) | — |
| [[SW 900 (line)]] | alt | 34.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.294× (z -8.6) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 29.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.52 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 33.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 52.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 28.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 27.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 43.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 24.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4278), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPCS]] | +0.73 | +0.73 / +0.71 | both halves | 7e-06 |  |
| [[C1orf131]] | +0.72 | +0.71 / +0.72 | both halves | 7e-06 |  |
| [[REST]] | +0.71 | +0.68 / +0.70 | both halves | 7e-06 | same gene group |
| [[TRIP11]] | +0.71 | +0.77 / +0.67 | both halves | 7e-06 |  |
| [[ZC3H6]] | +0.70 | +0.73 / +0.68 | both halves | 7e-06 |  |
| [[MRPS31]] | +0.70 | +0.68 / +0.75 | both halves | 7e-06 |  |
| [[SCAF11]] | +0.70 | +0.62 / +0.70 | both halves | 7e-06 |  |
| [[ANKRD26]] | +0.70 | +0.74 / +0.65 | both halves | 7e-06 |  |
| [[CEP350]] | +0.69 | +0.61 / +0.71 | both halves | 7e-06 |  |
| [[RSF1]] | +0.68 | +0.59 / +0.70 | both halves | 7e-06 |  |
| [[PEX12]] | +0.68 | +0.63 / +0.71 | both halves | 7e-06 |  |
| [[NFYB]] | +0.68 | +0.73 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TCF3]] | -0.70 | -0.70 / -0.70 | both halves | 7e-06 |  |
| [[FAM20B]] | -0.68 | -0.65 / -0.67 | both halves | 7e-06 |  |
| [[RBM14-RBM4]] | -0.68 | -0.65 / -0.66 | both halves | 7e-06 |  |
| [[TPST2]] | -0.65 | -0.73 / -0.61 | both halves | 7e-06 |  |
| [[SNRPA]] | -0.61 | -0.58 / -0.52 | both halves | 1e-05 |  |
| [[PRR5-ARHGAP8]] | -0.61 | -0.57 / -0.57 | both halves | 1e-05 |  |
| [[CPSF4]] | -0.61 | -0.65 / -0.52 | both halves | 1e-05 |  |
| [[FBRSL1]] | -0.61 | -0.56 / -0.57 | both halves | 1e-05 |  |
| [[HSF1]] | -0.61 | -0.71 / -0.51 | both halves | 1e-05 |  |
| [[NTAQ1]] | -0.60 | -0.58 / -0.57 | both halves | 1e-05 |  |
| [[AHCY]] | -0.60 | -0.52 / -0.57 | both halves | 1e-05 |  |
| [[CHID1]] | -0.59 | -0.52 / -0.61 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers TRMT1L's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.2% of all compounds | 0.037 | ⚠ off-target possible; 3 compounds |
| [[IFT74]] | C | IFT74 activity raises TRMT1L's level | lines that do not express IFT74 (3) vs lines expressing it (47) | 1.73× lower at baseline in the lines without IFT74 | 0.080 | ⚠ few lines (3 vs 47); across organs; also absent: LCA5, P3H4, TOMM40L; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.709). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-25.9, 6.7); signed map (5.2, -16.3). **Vector** length 109, 28.4% of its response variance represented; |z| ≥ 3 in 1,115 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +11.4 | +10.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | +9.9 | +9.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.6 | +7.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +7.3 | +8.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +5.9 | +6.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +4.0 | +3.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.7 | +4.0 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +2.3 | +3.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +2.3 | +3.3 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.4 | -11.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -5.3 | -10.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.3 | -1.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.2 | -4.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -5.0 | -4.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -3.0 | -3.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.7 | -2.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.3 | -0.7 |
|  | [[EX229 (drug)]] 5 µM |  | -2.3 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | tRNA methyltransferase 1L |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q25.3 — chr1:185,118,101-185,157,072 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously C1orf25 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; 7BS DNA/RNA methyltransferases; DNA/RNA methyltransferases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z2T5](https://www.uniprot.org/uniprotkb/Q7Z2T5) (tRNA):

> Specifically dimethylates a single guanine residue at position 27 of tRNA(Tyr) using S-adenosyl-L-methionine as donor of the methyl groups. Dimethylation at position 27 of tRNA(Tyr) is required for efficient translation of tyrosine codons. Also required to maintain 3-(3-amino-3-carboxypropyl)uridine (acp3U) in the D-loop of several cytoplasmic tRNAs.

**Summary**, from NCBI Gene [81627](https://www.ncbi.nlm.nih.gov/gene/81627):

> This gene encodes a protein that has some similarity to N2,N2-dimethylguanosine tRNA methyltransferase from other organisms. Studies of the mouse ortholog have shown that this protein plays a role in motor coordination and exploratory behavior, and it may also be involved in modulating postnatal neuronal functions. Alternatively spliced transcripts have been identified for this gene. [provided by RefSeq, Jan 2011]

**Accessions** — [HGNC:16782](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16782) · Entrez [81627](https://www.ncbi.nlm.nih.gov/gene/81627) · UniProt [Q7Z2T5](https://www.uniprot.org/uniprotkb/Q7Z2T5) · Ensembl [ENSG00000121486](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000121486)

## Data

Gene col 4278: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4278); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4278, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4278]; `tensor/DDL_lfc|DDL_z.npy` [4278]; `embed/gene_vectors.npy` [4278]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4278 or target_col == 4278). Every well: [[TRMT1L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRMT1L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
