---
symbol: "FARSB"
type: "gene"
col: 3761
ensembl_id: "ENSG00000116120"
name: "phenylalanyl-tRNA synthetase subunit beta"
location: "2q36.1"
module: 4
arm: "+"
pooled_cpm: 34.0
n_lines_expressing: 50
n_dd_up: 41
n_dd_down: 1
n_dd_up_clean: 29
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# FARSB

*phenylalanyl-tRNA synthetase subunit beta* — 2q36.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 41 drug-doses (12 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.55× (z +18.1, q 0e+00, up in 47 of 48 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 2.13× (z +10.8, q 3e-25, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.774× (z -5.2, q 1e-04, down in 25 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 4 lines (SW480 0.333×, SW48 0.180×, RKO 0.249×, PANC-1 0.457×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (SW480 0.427×, HEC-1-A 0.478×, RKO 0.408×); [[Auranofin (drug)]] 5 µM in 1 line (RKO 0.244×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATIC]] (+0.85, fdr 7e-06), [[RUVBL1]] (+0.84, fdr 7e-06), [[PFAS]] (+0.82, fdr 7e-06); moves opposite to [[TSC22D4]] (-0.73, fdr 7e-06), [[TESK2]] (-0.72, fdr 7e-06), [[RSRP1]] (-0.71, fdr 1e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HLA-F-AS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 43 in all, 13 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 41 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3761.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **3.55×** | +18.1 | 0e+00 | 47/48 (NCI-H1573, A-172, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **3.18×** | +16.5 | 0e+00 | 48/48 (A-172, HOP62, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **3.08×** | +16.1 | 0e+00 | 48/48 (A-172, HOP62, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **2.84×** | +14.3 | 4e-44 | 35/39 (NCI-H460, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **2.28×** | +11.7 | 1e-29 | 40/46 (NCI-H460, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **2.18×** | +11.1 | 9e-27 | 45/48 (MIA PaCa-2, NCI-H460, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **2.30×** | +11.0 | 4e-26 | 38/43 (SNU-423, A549, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.13×** | +10.8 | 3e-25 | 44/48 (CFPAC-1, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.70×** | +10.7 | 8e-25 | 40/48 (NCI-H2030, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.10×** | +10.6 | 2e-24 | 44/48 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.16×** | +10.5 | 3e-24 | 42/48 (NCI-H1573, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **3.21×** | +8.7 | 2e-16 | 36/48 (HOP62, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.86×** | +7.8 | 2e-13 | 35/48 (HOP62, Hs 766T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.76×** | +7.8 | 3e-13 | 41/48 (NCI-H1792, NCI-H1573, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.68×** | +7.4 | 7e-12 | 39/48 (LOX-IMVI, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.54×** | +6.1 | 3e-08 | 29/48 (A-172, HS-578T, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.53×** | +6.1 | 4e-08 | 35/48 (LOX-IMVI, PANC-1, …) | all doses, stronger at high dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.84×** | +4.6 | 2e-04 | 25/48 (MIA PaCa-2, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.83×** | +4.5 | 2e-04 | 24/48 (SW 900, A498, …) | all doses, flat | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.79×** | +4.4 | 4e-04 | 21/48 (A549, C32, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.71×** | +4.0 | 0.002 | 20/48 (MIA PaCa-2, Hs 766T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.70×** | +4.0 | 0.002 | 22/48 (MIA PaCa-2, C32, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3761.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 4 lines (SW480 0.333×, SW48 0.180×, RKO 0.249×, PANC-1 0.457×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (SW480 0.427×, HEC-1-A 0.478×, RKO 0.408×); [[Auranofin (drug)]] 5 µM in 1 line (RKO 0.244×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.774×** | -5.2 | 1e-04 | 25/48 (SW480, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | 0.798× | -3.3 | 0.22 | 22/47 (SW480, SW48, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 0.801× | -3.2 | 0.22 | 15/48 (SW48, LoVo, …) | inconsistent across doses | position effect removed |
| [[PF-06260933 (drug)]] 5 µM |  | 0.656× | -3.2 | 0.22 | 17/47 (SHP-77, NCI-H2030, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.63 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3761. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 21.9 | 8 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 7.23× (z +11.6) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 6.34× (z +10.8) | — |
| [[A549 (line)]] | wt | 30.5 | 6 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.22× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.66× (z +10.4) | — |
| [[HT-29 (line)]] | alt | 16.3 | 6 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.82× (z +9.6) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.27× (z +9.1) | — |
| [[NCI-H460 (line)]] | wt | 37.6 | 6 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.91× (z +12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[SNU-423 (line)]] | alt | 20.1 | 6 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.51× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[SW480 (line)]] | alt | 50.1 | 3 (2 ⚠) | 3 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.79× (z +9.7) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.45× (z +8.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.427× (z -11.4) |
| [[Hs 766T (line)]] | wt | 24.9 | 5 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.12× (z +10.2) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.86× (z +8.5) | — |
| [[HS-578T (line)]] | alt | 27.6 | 5 (5 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.00× (z +9.2) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[AsPC-1 (line)]] | alt | 15.7 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 7.15× (z +10.3) | — |
| [[HOP62 (line)]] | alt | 28.2 | 4 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.14× (z +10.7) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[LoVo (line)]] | wt | 24.2 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.09× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[SW 900 (line)]] | alt | 19.1 | 4 (4 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 5.16× (z +9.7) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[A-172 (line)]] | wt | 26.4 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 5.00× (z +11.3) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[C32 (line)]] | wt | 32.8 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.33× (z +8.8) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[CFPAC-1 (line)]] | alt | 17.4 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 8.21× (z +12.4) | — |
| [[NCI-H1792 (line)]] | alt | 18.7 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 6.04× (z +10.3) | — |
| [[NCI-H2030 (line)]] | alt | 34.4 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +11.7) | — |
| [[RKO (line)]] | wt | 60.4 | 0 | 3 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.244× (z -9.6) |
| [[SHP-77 (line)]] | alt | 83.2 | 3 (3 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 2.97× (z +9.9) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[A498 (line)]] | wt | 34.6 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.83× (z +9.1) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[H4 (line)]] | wt | 33.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.10× (z +8.7) | — |
| [[HepG2_C3A (line)]] | wt | 20.9 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 6.12× (z +8.9) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 52.1 | 2 (2 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.68× (z +10.2) ⚠ unreliable plate only | — |
| [[NCI-H23 (line)]] | alt | 48.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.00× (z +9.1) | [[Bortezomib (drug)]] 5 µM 0.130× (z -8.9) ⚠ toxic |
| [[NCI-H2347 (line)]] | alt | 15.6 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.26× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.17× (z +8.9) | — |
| [[Panc 03.27 (line)]] | alt | 25.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.89× (z +9.8) | — |
| [[RPMI-7951 (line)]] | alt | 32.5 | 2 (2 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 4.48× (z +8.9) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[COLO 205 (line)]] | alt | 14.3 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 9.77× (z +9.0) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[HEC-1-A (line)]] | alt | 41.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.478× (z -9.7) |
| [[KATO III (line)]] | alt | 33.7 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.94× (z +9.3) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[LOX-IMVI (line)]] | wt | 27.7 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.48× (z +9.2) | — |
| [[PANC-1 (line)]] | alt | 57.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.457× (z -9.0) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 30.6 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.46× (z +8.6) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[SW48 (line)]] | wt | 44.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.180× (z -9.8) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 40.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 51.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 49.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 36.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 38.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 32.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 38.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3761), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATIC]] | +0.85 | +0.83 / +0.89 | both halves | 7e-06 |  |
| [[RUVBL1]] | +0.84 | +0.82 / +0.83 | both halves | 7e-06 |  |
| [[PFAS]] | +0.82 | +0.79 / +0.81 | both halves | 7e-06 |  |
| [[AGK]] | +0.78 | +0.70 / +0.77 | both halves | 7e-06 |  |
| [[PPIL1]] | +0.78 | +0.84 / +0.74 | both halves | 7e-06 |  |
| [[NAA15]] | +0.78 | +0.74 / +0.82 | both halves | 7e-06 |  |
| [[MYBBP1A]] | +0.78 | +0.68 / +0.79 | both halves | 7e-06 |  |
| [[LAS1L]] | +0.78 | +0.75 / +0.74 | both halves | 7e-06 |  |
| [[EIF2S1]] | +0.78 | +0.74 / +0.81 | both halves | 7e-06 | STRING 711 |
| [[EFTUD2]] | +0.76 | +0.55 / +0.80 | both halves | 1e-05 |  |
| [[DDX10]] | +0.75 | +0.78 / +0.76 | both halves | 7e-06 |  |
| [[POLR1A]] | +0.75 | +0.71 / +0.78 | both halves | 7e-06 | STRING 525 |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TSC22D4]] | -0.73 | -0.65 / -0.75 | both halves | 7e-06 |  |
| [[TESK2]] | -0.72 | -0.62 / -0.69 | both halves | 7e-06 |  |
| [[RSRP1]] | -0.71 | -0.55 / -0.71 | both halves | 1e-05 |  |
| [[ZMAT5]] | -0.68 | -0.51 / -0.67 | both halves | 1e-05 |  |
| [[AAMDC]] | -0.67 | -0.65 / -0.65 | both halves | 7e-06 |  |
| [[ARID4B]] | -0.66 | -0.43 / -0.72 | both halves | 3e-05 |  |
| [[BSDC1]] | -0.65 | -0.54 / -0.70 | both halves | 1e-05 |  |
| [[NARF]] | -0.65 | -0.67 / -0.68 | both halves | 7e-06 |  |
| [[GNAS]] | -0.64 | -0.67 / -0.63 | both halves | 7e-06 |  |
| [[GABARAPL2]] | -0.64 | -0.58 / -0.72 | both halves | 7e-06 |  |
| [[KLHL24]] | -0.64 | -0.65 / -0.57 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HLA-F-AS1]] | B | HLA-F-AS1 activity lowers FARSB's level | lines that do not express HLA-F-AS1 (6) vs lines expressing it (44) | 1.77× higher at baseline in the lines without HLA-F-AS1 | 0.006 | ⚠ within organs, on part of the lines; also absent: LRP1, STRIP2, SH2D4B; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.825). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-19.7, -34.8); signed map (-7.0, -46.2). **Vector** length 132, 44.5% of its response variance represented; |z| ≥ 3 in 1,391 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MYC targets v1* (hallmark, mean cos +0.56 to 21); *tRNA processing in the nucleus* (reactome, mean cos +0.53 to 8); *Processing of Capped Intron-Containing Pre-mRNA* (reactome, mean cos +0.53 to 15).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +8.0 | +11.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | +7.8 | +11.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | +7.7 | +14.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +7.4 | +7.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +7.3 | +10.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.5 | +7.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.0 | +6.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +4.4 | +4.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | +4.3 | +4.6 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -10.6 | -5.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.4 | -1.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.9 | -3.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.6 | +0.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -3.9 | -0.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.8 | -2.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.4 | -2.4 |
|  | [[Entrectinib (drug)]] 5 µM |  | -3.1 | -2.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.1 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | phenylalanyl-tRNA synthetase subunit beta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q36.1 — chr2:222,566,899-222,656,092 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PheHB, FRSB; previously FARSLB |
| Gene groups (HGNC) | Aminoacyl tRNA synthetases, Class II |
| Reactome | 3 pathways, smallest: Cytosolic tRNA aminoacylation; tRNA Aminoacylation; Translation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NSD9](https://www.uniprot.org/uniprotkb/Q9NSD9) (Phenylalanine--tRNA ligase beta subunit):

> Beta subunit of cytoplasmic phenylalanyl-tRNA synthetase, an enzyme that catalyzes the esterification of phenylalanine to its cognate tRNA with the concomitant hydrolysis of ATP. The activated amino acid is transferred to the 2-OH group of a phenylalanine-accepting tRNA.

**Summary**, from NCBI Gene [10056](https://www.ncbi.nlm.nih.gov/gene/10056):

> This gene encodes a highly conserved enzyme that belongs to the aminoacyl-tRNA synthetase class IIc subfamily. This enzyme comprises the regulatory beta subunits that form a tetramer with two catalytic alpha subunits. In the presence of ATP, this tetramer is responsible for attaching L-phenylalanine to the terminal adenosine of the appropriate tRNA. A pseudogene located on chromosome 10 has been identified. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jan …

**Accessions** — [HGNC:17800](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17800) · Entrez [10056](https://www.ncbi.nlm.nih.gov/gene/10056) · UniProt [Q9NSD9](https://www.uniprot.org/uniprotkb/Q9NSD9) · Ensembl [ENSG00000116120](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116120)

## Data

Gene col 3761: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3761); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3761, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3761]; `tensor/DDL_lfc|DDL_z.npy` [3761]; `embed/gene_vectors.npy` [3761]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3761 or target_col == 3761). Every well: [[FARSB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FARSB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
