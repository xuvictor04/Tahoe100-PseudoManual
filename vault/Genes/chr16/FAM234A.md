---
symbol: "FAM234A"
type: "gene"
col: 9560
ensembl_id: "ENSG00000167930"
name: "family with sequence similarity 234 member A"
location: "16p13.3"
module: 50
arm: "+"
pooled_cpm: 30.1
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 27
n_dd_up_clean: 8
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/050"]
generated_by: "tahoemap"
---

# FAM234A

*family with sequence similarity 234 member A* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.11× (z +11.6, q 2e-28, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (5 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.417× (z -13.6, q 3e-39, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DAG1]] (+0.68, fdr 1e-05), [[BSG]] (+0.68, fdr 7e-06), [[AGPAT1]] (+0.67, fdr 7e-06); moves opposite to [[TYW3]] (-0.60, fdr 4e-05), [[GPRASP3]] (-0.56, fdr 2e-04), [[CDKL1]] (-0.56, fdr 4e-05).
> It is in [[Module 050]], a single-armed module (Extracellular matrix organization).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 6 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9560.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.11×** | +11.6 | 2e-28 | 45/48 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.97×** | +10.6 | 1e-23 | 42/48 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.84×** | +9.5 | 3e-19 | 29/44 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.80×** | +8.8 | 2e-16 | 29/35 (J82, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.65×** | +7.8 | 7e-13 | 36/48 (A498, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +7.2 | 5e-11 | 34/48 (HS-578T, SNU-423, …) | rises with dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.53×** | +6.1 | 8e-08 | 25/41 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.46×** | +5.9 | 3e-07 | 36/48 (LS 180, SW480, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.22×** | +4.4 | 6e-04 | 21/48 (HS-578T, HOP62, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.63×** | +4.0 | 0.004 | 20/48 (A498, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~15% of this change | **1.28×** | +3.8 | 0.006 | 20/48 (hTERT-HPNE, A498, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.18× | +3.6 | 0.014 | 17/48 (SHP-77, LOX-IMVI, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.53×** | +3.5 | 0.022 | 16/47 (SW480, HCT15, …) | top dose only | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **1.24×** | +3.3 | 0.036 | 16/48 (BT-474, SW1417, …) | rises with dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.23×** | +3.3 | 0.036 | 16/48 (SW480, A498, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9560.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.417×** | -13.6 | 3e-39 | 48/48 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.418×** | -13.5 | 3e-39 | 46/47 (LOX-IMVI, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.444×** | -12.6 | 4e-34 | 46/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.489×** | -11.1 | 2e-26 | 45/48 (LS 180, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.512×** | -10.4 | 4e-23 | 42/48 (J82, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.516×** | -9.9 | 5e-21 | 44/48 (A-427, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.640×** | -9.8 | 1e-20 | 39/47 (HS-578T, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.564×** | -8.9 | 5e-17 | 37/47 (HS-578T, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.565×** | -8.3 | 4e-15 | 41/48 (PANC-1, KATO III, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.626×** | -7.3 | 2e-11 | 36/48 (SW 1088, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.630×** | -7.1 | 5e-11 | 36/48 (HT-29, LoVo, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.631×** | -7.1 | 5e-11 | 31/48 (KATO III, J82, …) | rises with dose | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.446×** | -6.5 | 3e-09 | 35/48 (A-427, NCI-H460, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.448×** | -6.5 | 3e-09 | 30/42 (A-427, A549, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.457×** | -6.3 | 8e-09 | 32/48 (A-427, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | **0.727×** | -4.8 | 6e-05 | 30/48 (J82, AN3 CA, …) | top dose only | position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.740×** | -4.6 | 1e-04 | 23/47 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9560. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 26.0 | 0 | 6 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.305× (z -10.8) |
| [[PANC-1 (line)]] | alt | 45.6 | 3 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.52× (z +11.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 2.22× (z +9.5) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.405× (z -10.8) |
| [[J82 (line)]] | alt | 31.3 | 1 (1 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.13× (z +9.3) ⚠ toxic; transcription drop | [[Ixazomib citrate (drug)]] 5 µM 0.175× (z -14.1) |
| [[LS 180 (line)]] | wt | 27.8 | 0 | 5 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.124× (z -16.3) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.205× (z -12.4) |
| [[SW480 (line)]] | alt | 30.2 | 0 | 5 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.320× (z -13.1) |
| [[A-427 (line)]] | wt | 33.7 | 0 | 4 (1 ⚠) | — | [[PH-797804 (drug)]] 5 µM 0.0622× (z -13.1) |
| [[SW1417 (line)]] | alt | 27.5 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.247× (z -11.4) |
| [[A498 (line)]] | wt | 37.4 | 3 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.60× (z +9.5) | — |
| [[BT-474 (line)]] | alt | 32.2 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.123× (z -16.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.284× (z -9.7) |
| [[HT-29 (line)]] | alt | 27.2 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.392× (z -10.3) |
| [[NCI-H1792 (line)]] | alt | 26.3 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.85× (z +9.7) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.293× (z -8.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.303× (z -8.5) |
| [[SNU-423 (line)]] | alt | 32.5 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.66× (z +9.8) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.287× (z -9.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.304× (z -8.9) |
| [[C32 (line)]] | wt | 35.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.261× (z -10.0) |
| [[Hs 766T (line)]] | wt | 27.5 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.261× (z -9.2) |
| [[HS-578T (line)]] | alt | 36.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.341× (z -11.7) |
| [[KATO III (line)]] | alt | 41.1 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.249× (z -12.4) |
| [[NCI-H460 (line)]] | wt | 23.0 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 5 µM 0.298× (z -10.5) |
| [[SW48 (line)]] | wt | 24.9 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.124× (z -9.5) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.155× (z -8.5) |
| [[A-172 (line)]] | wt | 56.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.358× (z -9.9) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 33.3 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0739× (z -11.1) ⚠ toxic |
| [[CHP-212 (line)]] | wt | 33.4 | 0 | 1 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.109× (z -8.9) ⚠ cell-cycle shift, explains ~36% of this change |
| [[COLO 205 (line)]] | alt | 37.1 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.229× (z -10.2) |
| [[H4 (line)]] | wt | 37.7 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.238× (z -8.6) |
| [[HOP62 (line)]] | alt | 26.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.242× (z -10.5) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 13.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0472× (z -18.5) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 14.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.88× (z +10.4) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 16.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.234× (z -8.7) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 13.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.303× (z -8.6) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 17.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.230× (z -8.9) |
| [[SNU-1 (line)]] | wt | 25.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.0530× (z -14.5) |
| [[AN3 CA (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 24.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 34.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 23.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9560), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DAG1]] | +0.68 | +0.55 / +0.66 | both halves | 1e-05 |  |
| [[BSG]] | +0.68 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[AGPAT1]] | +0.67 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[CHPF]] | +0.65 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[NOMO1]] | +0.62 | +0.43 / +0.54 | both halves | 3e-05 |  |
| [[PRKACA]] | +0.62 | +0.45 / +0.63 | both halves | 3e-05 |  |
| [[TAF6]] | +0.62 | +0.58 / +0.47 | both halves | 2e-05 |  |
| [[SLC25A39]] | +0.62 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[MAN1B1]] | +0.62 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[NAGA]] | +0.60 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[PRPF8]] | +0.59 | +0.62 / +0.45 | both halves | 3e-05 |  |
| [[FUCA1]] | +0.59 | +0.49 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TYW3]] | -0.60 | -0.41 / -0.56 | both halves | 4e-05 |  |
| [[GPRASP3]] | -0.56 | -0.30 / -0.50 | both halves | 2e-04 |  |
| [[CDKL1]] | -0.56 | -0.49 / -0.42 | both halves | 4e-05 |  |
| [[DNAJC2]] | -0.55 | -0.42 / -0.54 | both halves | 4e-05 |  |
| [[KCNMB3]] | -0.55 | -0.33 / -0.48 | both halves | 1e-04 |  |
| [[MRPL45P2]] | -0.55 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[FBXO10]] | -0.55 | -0.33 / -0.46 | both halves | 1e-04 |  |
| [[YIPF7]] | -0.54 | -0.37 / -0.46 | both halves | 8e-05 |  |
| [[GRK7]] | -0.54 | -0.36 / -0.44 | both halves | 9e-05 |  |
| [[BTN2A3P-1]] | -0.54 | -0.38 / -0.38 | both halves | 6e-05 |  |
| [[MAFG]] | -0.52 | -0.48 / -0.35 | both halves | 1e-04 |  |
| [[TBCA]] | -0.51 | -0.51 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 050]] — Extracellular matrix organization; 92 genes; every member is in the + arm (projection on the module's main direction 0.694). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-20.9, -22.2); signed map (-28.1, -39.1). **Vector** length 71.0, 15.7% of its response variance represented; |z| ≥ 3 in 1,263 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +3.8 | +11.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.3 | +10.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.0 | +9.5 |
|  | [[Belinostat (drug)]] 5 µM |  | +2.9 | +7.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.6 | +8.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | +1.4 | +1.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.3 | +4.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | +1.3 | -0.4 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | +1.3 | -1.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.2 | +3.5 |
| fall | [[Auranofin (drug)]] 5 µM |  | -6.8 | -7.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.6 | -8.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.3 | -7.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -4.3 | -10.4 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -4.2 | -8.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.5 | -7.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.1 | -2.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.7 | -4.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.0 | -4.4 |

## What is on record

|  |  |
|---|---|
| Name | family with sequence similarity 234 member A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:234,521-272,183 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP761D0211, FLJ32603; previously C16orf9, ITFG3 |
| Matched by | ensembl_id |

UniProt [Q9H0X4](https://www.uniprot.org/uniprotkb/Q9H0X4) carries no function annotation.

**Summary**, from NCBI Gene [83986](https://www.ncbi.nlm.nih.gov/gene/83986):

> Located in cell surface. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:14163](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14163) · Entrez [83986](https://www.ncbi.nlm.nih.gov/gene/83986) · UniProt [Q9H0X4](https://www.uniprot.org/uniprotkb/Q9H0X4) · Ensembl [ENSG00000167930](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167930)

## Data

Gene col 9560: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9560); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9560, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9560]; `tensor/DDL_lfc|DDL_z.npy` [9560]; `embed/gene_vectors.npy` [9560]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9560 or target_col == 9560). Every well: [[FAM234A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM234A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
