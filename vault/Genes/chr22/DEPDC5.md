---
symbol: "DEPDC5"
type: "gene"
col: 1880
ensembl_id: "ENSG00000100150"
name: "DEP domain containing 5, GATOR1 subcomplex subunit"
location: "22q12.2-q12.3"
module: 142
arm: "+"
pooled_cpm: 36.71
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 18
n_dd_up_clean: 3
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/142"]
generated_by: "tahoemap"
---

# DEPDC5

*DEP domain containing 5, GATOR1 subcomplex subunit* — 22q12.2-q12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.81× (z +10.2, q 7e-22, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (12 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.354× (z -17.2, q 0e+00, down in 44 of 48 measured lines) ⚠ cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.556× (z -10.1, q 3e-22, down in 34 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SMYD4]] (+0.65, fdr 7e-06), [[IQCB1]] (+0.63, fdr 1e-05), [[NUP85]] (+0.60, fdr 1e-05); moves opposite to [[NR1D2]] (-0.59, fdr 4e-05), [[ATG2B]] (-0.57, fdr 5e-05), [[LGALSL]] (-0.56, fdr 6e-05).
> It is in [[Module 142]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1880.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.81×** | +10.2 | 7e-22 | 42/48 (A549, LoVo, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.70×** | +9.1 | 2e-17 | 41/48 (A549, J82, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.55×** | +7.6 | 6e-12 | 33/48 (LoVo, J82, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~79% of this change | **1.24×** | +3.7 | 0.031 | 17/48 (SW480, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 5 µM |  | 1.47× | +3.3 | 0.10 | 6/48 (HEC-1-A, SNU-423, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | 1.20× | +3.1 | 0.19 | 19/47 (LoVo, A498, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.19× | +3.0 | 0.19 | 14/48 (LoVo, SNU-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 12 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1880.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.354×** | -17.2 | 0e+00 | 44/48 (A-427, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.403×** | -15.7 | 0e+00 | 39/47 (A549, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **0.555×** | -14.4 | 2e-44 | 42/48 (A498, SNU-423, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.424×** | -14.2 | 7e-44 | 34/41 (SW480, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.461×** | -12.8 | 1e-35 | 41/47 (RPMI-7951, HOP62, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.468×** | -12.1 | 8e-32 | 31/44 (MIA PaCa-2, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.503×** | -11.9 | 2e-30 | 41/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.532×** | -10.9 | 1e-25 | 37/47 (NCI-H460, SW480, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.556×** | -10.1 | 3e-22 | 34/48 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.573×** | -9.6 | 4e-20 | 38/47 (LOX-IMVI, A549, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.614×** | -8.4 | 2e-15 | 36/48 (SNU-423, MIA PaCa-2, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.444×** | -7.0 | 9e-11 | 35/49 (KATO III, SNU-423, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~22% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.687×** | -6.5 | 4e-09 | 33/48 (H4, SW480, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.717×** | -5.7 | 4e-07 | 28/48 (SW480, NCI-H460, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.546×** | -5.3 | 6e-06 | 27/48 (Panc 03.27, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.792×** | -4.0 | 0.002 | 21/48 (Panc 03.27, A-172, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.757×** | -3.4 | 0.019 | 11/48 (A-427, CFPAC-1, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.840× | -3.0 | 0.077 | 10/47 (hTERT-HPNE, J82, …) | two highest doses |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | 0.836× | -3.0 | 0.080 | 8/48 (HT-29, PANC-1, …) | top dose only | plate-row cell shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, -0.62 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1880. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 31.2 | 0 | 13 (11 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.142× (z -19.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.231× (z -14.5) |
| [[SW480 (line)]] | alt | 55.5 | 0 | 10 (9 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.246× (z -17.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.403× (z -11.6) |
| [[SNU-423 (line)]] | alt | 40.0 | 0 | 8 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -17.1) ⚠ cell-cycle shift, explains ~67% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.204× (z -13.3) |
| [[KATO III (line)]] | alt | 45.4 | 0 | 7 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.371× (z -13.4) ⚠ cell-cycle shift, explains ~67% of this change |
| [[MIA PaCa-2 (line)]] | alt | 35.9 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.127× (z -16.6) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.170× (z -15.4) |
| [[A-427 (line)]] | wt | 38.3 | 0 | 6 (5 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.181× (z -15.1) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.356× (z -9.5) |
| [[A549 (line)]] | wt | 27.7 | 1 | 5 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 2.83× (z +8.7) | [[Dinaciclib (drug)]] 0.5 µM 0.0459× (z -25.8) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.189× (z -13.9) |
| [[PANC-1 (line)]] | alt | 41.3 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.274× (z -15.5) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 40.6 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -12.1) ⚠ cell-cycle shift, explains ~67% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.224× (z -10.1) |
| [[Panc 03.27 (line)]] | alt | 34.4 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.177× (z -14.6) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 50.0 | 0 | 5 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.178× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[A498 (line)]] | wt | 27.4 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -18.0) ⚠ cell-cycle shift, explains ~67% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.260× (z -11.1) |
| [[H4 (line)]] | wt | 25.1 | 0 | 4 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0344× (z -17.8) ⚠ cell-cycle shift, explains ~36% of this change |
| [[HEC-1-A (line)]] | alt | 45.9 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.334× (z -15.6) ⚠ cell-cycle shift, explains ~67% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.365× (z -10.1) |
| [[HS-578T (line)]] | alt | 41.7 | 0 | 4 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.221× (z -11.8) ⚠ cell-cycle shift, explains ~31% of this change |
| [[LoVo (line)]] | wt | 37.8 | 1 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.38× (z +8.5) | [[Digitoxin (drug)]] 5 µM 0.233× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[LS 180 (line)]] | wt | 38.4 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.227× (z -12.5) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 62.1 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.130× (z -17.1) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 30.6 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.127× (z -17.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[A-172 (line)]] | wt | 18.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.138× (z -13.4) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 25.3 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.290× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[C-33 A (line)]] | alt | 65.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0789× (z -20.0) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 37.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.307× (z -10.1) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 75.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.302× (z -9.1) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 36.5 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.345× (z -11.6) ⚠ cell-cycle shift, explains ~67% of this change |
| [[hTERT-HPNE (line)]] | wt | 29.2 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -10.5) ⚠ cell-cycle shift, explains ~67% of this change |
| [[J82 (line)]] | alt | 26.6 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.245× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[LOX-IMVI (line)]] | wt | 24.4 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.253× (z -10.8) ⚠ cell-cycle shift, explains ~40% of this change |
| [[NCI-H1573 (line)]] | alt | 41.4 | 0 | 2 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.147× (z -8.9) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.399× (z -8.5) |
| [[NCI-H1792 (line)]] | alt | 30.3 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.242× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[NCI-H2030 (line)]] | alt | 38.9 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.224× (z -12.6) ⚠ cell-cycle shift, explains ~31% of this change |
| [[NCI-H23 (line)]] | alt | 55.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.156× (z -18.2) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 33.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.103× (z -13.5) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 48.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.189× (z -14.1) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 43.5 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.213× (z -9.1) |
| [[AN3 CA (line)]] | alt | 43.8 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.117× (z -9.7) |
| [[HOP62 (line)]] | alt | 13.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.174× (z -11.6) ⚠ toxic |
| [[NCI-H2347 (line)]] | alt | 28.1 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.471× (z -8.6) ⚠ cell-cycle shift, explains ~90% of this change |
| [[SK-MEL-2 (line)]] | alt | 24.5 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.251× (z -9.1) |
| [[SNU-1 (line)]] | wt | 39.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.235× (z -9.6) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 33.9 | 0 | 1 | — | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM 0.0661× (z -8.5) |
| [[BT-474 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 41.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 29.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 43.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 39.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1880), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMYD4]] | +0.65 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[IQCB1]] | +0.63 | +0.51 / +0.66 | both halves | 1e-05 |  |
| [[NUP85]] | +0.60 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[NR2C2AP]] | +0.59 | +0.42 / +0.65 | both halves | 4e-05 |  |
| [[NUP214]] | +0.58 | +0.62 / +0.42 | both halves | 4e-05 |  |
| [[ARMH3]] | +0.58 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[GFOD2]] | +0.58 | +0.37 / +0.64 | both halves | 9e-05 |  |
| [[RNF121]] | +0.58 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[RABEPK]] | +0.58 | +0.44 / +0.63 | both halves | 3e-05 |  |
| [[TNPO3]] | +0.58 | +0.54 / +0.44 | both halves | 3e-05 |  |
| [[PIGU]] | +0.57 | +0.46 / +0.61 | both halves | 2e-05 |  |
| [[MRPS12]] | +0.57 | +0.42 / +0.55 | both halves | 4e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NR1D2]] | -0.59 | -0.40 / -0.61 | both halves | 4e-05 |  |
| [[ATG2B]] | -0.57 | -0.40 / -0.59 | both halves | 5e-05 |  |
| [[LGALSL]] | -0.56 | -0.58 / -0.39 | both halves | 6e-05 |  |
| [[CCDC50]] | -0.56 | -0.42 / -0.56 | both halves | 4e-05 |  |
| [[SGO1-AS1]] | -0.56 | -0.42 / -0.55 | both halves | 4e-05 |  |
| [[CFL2]] | -0.56 | -0.41 / -0.52 | both halves | 4e-05 |  |
| [[ZBTB10]] | -0.55 | -0.43 / -0.55 | both halves | 3e-05 |  |
| [[BMI1]] | -0.55 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[LEKR1]] | -0.54 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[CILK1]] | -0.54 | -0.43 / -0.58 | both halves | 3e-05 |  |
| [[TAF9B]] | -0.54 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[NOTCH2NLC]] | -0.54 | -0.40 / -0.51 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers DEPDC5's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 142]]; 33 genes; every member is in the + arm (projection on the module's main direction 0.608). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.40; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-8.4, -18.2); signed map (-42.9, -19.4). **Vector** length 76.9, 17.8% of its response variance represented; |z| ≥ 3 in 1,163 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.4 | +3.0 |
|  | [[EX229 (drug)]] 5 µM |  | +3.5 | +2.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.2 | +10.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.1 | +9.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~79% of this change | +3.0 | +3.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.7 | -0.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.6 | +0.9 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.6 | -0.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.3 | +1.3 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | -6.6 | -14.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -5.3 | -17.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | -5.2 | -9.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.0 | -12.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.3 | +0.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.8 | -8.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.2 | -1.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.9 | +1.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.6 | +1.9 |

## What is on record

|  |  |
|---|---|
| Name | DEP domain containing 5, GATOR1 subcomplex subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q12.2-q12.3 — chr22:31,753,867-31,908,033 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0645, DEP.5 |
| Gene groups (HGNC) | GATOR1 subcomplex; DEP domain containing |
| Reactome | 4 pathways, smallest: Amino acids regulate mTORC1; Cellular response to starvation; Cellular responses to stress |
| Matched by | ensembl_id |

**Function**, from UniProt [O75140](https://www.uniprot.org/uniprotkb/O75140) (GATOR1 complex protein DEPDC5):

> As a component of the GATOR1 complex functions as an inhibitor of the amino acid-sensing branch of the mTORC1 pathway. In response to amino acid depletion, the GATOR1 complex has GTPase activating protein (GAP) activity and strongly increases GTP hydrolysis by RagA/RRAGA (or RagB/RRAGB) within heterodimeric Rag complexes, thereby turning them into their inactive GDP-bound form, releasing mTORC1 from lysosomal surface and inhibiting mTORC1 signaling. In the presence of abundant amino acids, the …

**Summary**, from NCBI Gene [9681](https://www.ncbi.nlm.nih.gov/gene/9681):

> This gene encodes a member of the IML1 family of proteins involved in G-protein signaling pathways. The mechanistic target of rapamycin complex 1 (mTORC1) pathway regulates cell growth by sensing the availability of nutrients. The protein encoded by this gene is a component of the GATOR1 (GAP activity toward Rags) complex which inhibits the amino acid-sensing branch of the mTORC1 pathway. Mutations in this gene are associated with autosomal dominant familial focal epilepsy with variable foci. A …

**Accessions** — [HGNC:18423](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18423) · Entrez [9681](https://www.ncbi.nlm.nih.gov/gene/9681) · UniProt [O75140](https://www.uniprot.org/uniprotkb/O75140) · Ensembl [ENSG00000100150](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100150)

## Data

Gene col 1880: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1880); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1880, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1880]; `tensor/DDL_lfc|DDL_z.npy` [1880]; `embed/gene_vectors.npy` [1880]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1880 or target_col == 1880). Every well: [[DEPDC5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DEPDC5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
