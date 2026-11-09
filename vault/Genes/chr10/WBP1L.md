---
symbol: "WBP1L"
type: "gene"
col: 9275
ensembl_id: "ENSG00000166272"
name: "WW domain binding protein 1 like"
location: "10q24.32"
module: 118
arm: "+"
pooled_cpm: 47.66
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 22
n_dd_up_clean: 1
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/118"]
generated_by: "tahoemap"
---

# WBP1L

*WW domain binding protein 1 like* — 10q24.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 1.64× (z +4.5, q 0.003, up in 24 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Trametinib (drug)]] 5 µM in 1 line (SW480 2.11×; ⚠ cell-cycle shift, explains ~44% of this change).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (15 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.391× (z -16.3, q 0e+00, down in 46 of 48 measured lines) ⚠ cell-cycle shift, explains ~25% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.568× (z -9.8, q 5e-21, down in 39 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZSWIM8]] (+0.67, fdr 8e-06), [[TMUB2]] (+0.64, fdr 7e-06), [[ZKSCAN5]] (+0.62, fdr 1e-05); moves opposite to [[LRRC8B]] (-0.56, fdr 1e-05), [[EFR3A]] (-0.56, fdr 1e-05), [[TNPO1]] (-0.54, fdr 3e-05).
> It sits in the **+** arm of [[Module 118]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9275.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Trametinib (drug)]] 5 µM in 1 line (SW480 2.11×; ⚠ cell-cycle shift, explains ~44% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **1.64×** | +4.5 | 0.003 | 24/49 (COLO 205, NCI-H23, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | 1.23× | +3.4 | 0.20 | 13/49 (SW480, SNU-423, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | 1.43× | +3.2 | 0.23 | 9/49 (SW480, Hs 766T, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.13× | +3.1 | 0.27 | 11/48 (RKO, A-427, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | 1.19× | +3.0 | 0.27 | 11/48 (SK-MEL-2, A-172, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 15 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9275.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.391×** | -16.3 | 0e+00 | 46/48 (SW480, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.402×** | -15.8 | 0e+00 | 45/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.547×** | -14.8 | 0e+00 | 38/48 (CFPAC-1, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.441×** | -14.2 | 9e-44 | 42/48 (AsPC-1, SK-MEL-2, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.449×** | -12.9 | 9e-36 | 37/43 (KATO III, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~21% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.401×** | -12.8 | 2e-35 | 42/48 (COLO 205, HEC-1-A, …) | rises with dose | composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.559×** | -10.1 | 5e-22 | 42/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.488×** | -10.0 | 7e-22 | 30/39 (A-172, SW 900, …) | all doses, flat | composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.490×** | -10.0 | 1e-21 | 34/47 (Panc 03.27, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~21% here); noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.568×** | -9.8 | 5e-21 | 39/48 (CFPAC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.613×** | -8.5 | 1e-15 | 42/48 (CFPAC-1, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.619×** | -8.3 | 4e-15 | 41/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.655×** | -7.3 | 1e-11 | 33/48 (PANC-1, CFPAC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.674×** | -6.9 | 3e-10 | 29/48 (NCI-H460, AN3 CA, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.714×** | -5.8 | 2e-07 | 27/48 (PANC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | 0.838× | -4.3 | 5e-04 | 23/48 (PANC-1, SNU-1, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.632×** | -4.2 | 1e-03 | 24/48 (PANC-1, CFPAC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.802×** | -3.8 | 0.003 | 23/48 (C-33 A, SNU-423, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.720×** | -3.0 | 0.070 | 16/48 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9275. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 60.3 | 0 | 10 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.282× (z -16.8) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.272× (z -12.2) |
| [[NCI-H460 (line)]] | wt | 45.7 | 0 | 10 (8 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.129× (z -22.0) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.302× (z -12.9) |
| [[PANC-1 (line)]] | alt | 98.3 | 0 | 10 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.258× (z -15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.396× (z -10.8) |
| [[NCI-H1573 (line)]] | alt | 70.4 | 0 | 8 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.247× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[SW480 (line)]] | alt | 48.3 | 1 (1 ⚠) | 7 (7 ⚠) | [[Trametinib (drug)]] 5 µM 2.11× (z +8.7) ⚠ cell-cycle shift, explains ~44% of this change | [[Digitoxin (drug)]] 5 µM 0.177× (z -19.7) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 62.1 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.136× (z -18.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.382× (z -8.7) |
| [[A549 (line)]] | wt | 60.1 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.333× (z -13.1) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.364× (z -8.6) |
| [[BT-474 (line)]] | alt | 43.3 | 0 | 5 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.164× (z -14.6) ⚠ cell-cycle shift, explains ~25% of this change |
| [[COLO 205 (line)]] | alt | 63.4 | 0 | 5 (5 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.149× (z -13.0) ⚠ cell-cycle shift, explains ~27% of this change |
| [[SNU-423 (line)]] | alt | 71.4 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.223× (z -15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[A-172 (line)]] | wt | 54.2 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0785× (z -19.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[HEC-1-A (line)]] | alt | 38.3 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -16.6) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.361× (z -10.3) |
| [[C32 (line)]] | wt | 37.6 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.283× (z -9.6) ⚠ toxic; transcription drop · without an alert: [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.313× (z -8.8) |
| [[HepG2_C3A (line)]] | wt | 54.6 | 0 | 3 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.105× (z -13.4) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 58.2 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.221× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[HT-29 (line)]] | alt | 41.0 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.220× (z -12.5) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 41.7 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0916× (z -20.2) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 32.1 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.297× (z -12.1) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 41.9 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.225× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.343× (z -8.6) |
| [[LS 180 (line)]] | wt | 33.3 | 0 | 3 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.188× (z -14.1) ⚠ cell-cycle shift, explains ~25% of this change |
| [[MIA PaCa-2 (line)]] | alt | 38.2 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -14.1) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.339× (z -9.2) |
| [[Panc 03.27 (line)]] | alt | 57.7 | 0 | 3 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.166× (z -13.6) ⚠ toxic |
| [[RPMI-7951 (line)]] | alt | 44.1 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0904× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[SW 900 (line)]] | alt | 48.6 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0936× (z -16.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[SW1417 (line)]] | alt | 36.0 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -12.7) ⚠ cell-cycle shift, explains ~48% of this change |
| [[A-427 (line)]] | wt | 35.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.198× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[A498 (line)]] | wt | 37.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.301× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[H4 (line)]] | wt | 49.3 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.175× (z -10.9) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 54.6 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.236× (z -10.2) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 31.5 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.261× (z -11.1) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 42.2 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.111× (z -14.7) ⚠ toxic |
| [[RKO (line)]] | wt | 39.6 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.194× (z -10.3) ⚠ toxic |
| [[SHP-77 (line)]] | alt | 32.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.144× (z -13.8) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 26.1 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.106× (z -10.9) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 55.8 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.0856× (z -12.8) |
| [[C-33 A (line)]] | alt | 32.1 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.195× (z -9.9) |
| [[HS-578T (line)]] | alt | 34.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.286× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[hTERT-HPNE (line)]] | wt | 53.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.198× (z -11.2) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 28.4 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.343× (z -9.0) ⚠ cell-cycle shift, explains ~25% of this change |
| [[NCI-H1792 (line)]] | alt | 44.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.117× (z -16.3) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 40.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.316× (z -10.4) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 45.9 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.374× (z -11.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 45.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.125× (z -17.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[SNU-1 (line)]] | wt | 31.9 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.200× (z -9.1) ⚠ cell-cycle shift, explains ~25% of this change |
| [[CHP-212 (line)]] | wt | 42.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 49.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 43.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 55.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 41.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9275), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZSWIM8]] | +0.67 | +0.58 / +0.70 | both halves | 8e-06 |  |
| [[TMUB2]] | +0.64 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[ZKSCAN5]] | +0.62 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[SUPT4H1]] | +0.62 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[ZNF350]] | +0.60 | +0.61 / +0.47 | both halves | 2e-05 |  |
| [[RETREG3]] | +0.59 | +0.45 / +0.59 | both halves | 3e-05 |  |
| [[PRPF18]] | +0.59 | +0.62 / +0.38 | both halves | 6e-05 |  |
| [[SYNRG]] | +0.59 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[ZNF394]] | +0.58 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[IGBP1]] | +0.58 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[PIN4]] | +0.58 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[TFIP11]] | +0.57 | +0.56 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRRC8B]] | -0.56 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[EFR3A]] | -0.56 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[TNPO1]] | -0.54 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[SSX2IP]] | -0.54 | -0.52 / -0.57 | both halves | 1e-05 |  |
| [[HOOK1]] | -0.52 | -0.45 / -0.43 | both halves | 3e-05 |  |
| [[PTAR1]] | -0.51 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[IDH3A]] | -0.50 | -0.53 / -0.46 | both halves | 3e-05 |  |
| [[AADAT]] | -0.50 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[BLMH]] | -0.50 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[RFK]] | -0.48 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[ISOC1]] | -0.48 | -0.50 / -0.40 | both halves | 5e-05 |  |
| [[GPR63]] | -0.48 | -0.44 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 118]]; 41 genes; this gene is in the **+** arm (projection on the module's main direction 0.720). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-28.2, -10.0); signed map (-3.9, -4.7). **Vector** length 79.6, 19.9% of its response variance represented; |z| ≥ 3 in 1,215 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +8.3 | +4.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +6.4 | +2.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +3.9 | +2.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.4 | +3.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.6 | +1.4 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.0 | +1.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.9 | +2.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +0.5 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.7 | -12.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | -5.6 | -14.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | -5.1 | -10.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.8 | -2.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | -4.2 | -14.8 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.5 | -4.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.0 | -1.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.6 | +0.9 |
|  | [[Radotinib (drug)]] 0.5 µM |  | -1.6 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | WW domain binding protein 1 like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q24.32 — chr10:102,743,948-102,834,516 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20154, OPAL1; previously C10orf26 |
| Gene groups (HGNC) | WBP1/VOPP1 family |
| Matched by | ensembl_id |

UniProt [Q9NX94](https://www.uniprot.org/uniprotkb/Q9NX94) carries no function annotation.

**Summary**, from NCBI Gene [54838](https://www.ncbi.nlm.nih.gov/gene/54838):

> Predicted to enable ubiquitin protein ligase binding activity. Predicted to be involved in CXCL12-activated CXCR4 signaling pathway. Predicted to act upstream of or within hemopoiesis and positive regulation of protein ubiquitination. Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:23510](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23510) · Entrez [54838](https://www.ncbi.nlm.nih.gov/gene/54838) · UniProt [Q9NX94](https://www.uniprot.org/uniprotkb/Q9NX94) · Ensembl [ENSG00000166272](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166272)

## Data

Gene col 9275: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9275); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9275, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9275]; `tensor/DDL_lfc|DDL_z.npy` [9275]; `embed/gene_vectors.npy` [9275]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9275 or target_col == 9275). Every well: [[WBP1L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WBP1L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
