---
symbol: "GNA12"
type: "gene"
col: 7102
ensembl_id: "ENSG00000146535"
name: "G protein subunit alpha 12"
location: "7p22.3-p22.2"
module: 77
arm: "+"
pooled_cpm: 94.55
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 15
n_dd_up_clean: 10
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/077"]
generated_by: "tahoemap"
---

# GNA12

*G protein subunit alpha 12* — 7p22.3-p22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 1.67× (z +10.3, q 4e-22, up in 35 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.514× (z -13.0, q 9e-36, down in 42 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.692× (z -10.5, q 7e-24, down in 33 of 49 measured lines).
> Its strongest partners by |cos| (89 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 11 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LIMK1]] (+0.72, fdr 7e-06), [[PACC1]] (+0.71, fdr 7e-06), [[TPST2]] (+0.71, fdr 1e-05); moves opposite to [[TMEM202-AS1]] (-0.73, fdr 6e-05), [[KRCC1]] (-0.71, fdr 4e-05), [[METTL6]] (-0.70, fdr 1e-04).
> It sits in the **+** arm of [[Module 077]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[ROR1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 6 with an alert ⚠; shown: the 15 strongest. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7102.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **1.67×** | +10.3 | 4e-22 | 35/48 (AsPC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.61×** | +9.7 | 1e-19 | 35/48 (AsPC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.59×** | +9.3 | 2e-18 | 39/48 (AsPC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.28×** | +5.0 | 7e-05 | 28/48 (AsPC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.28×** | +4.7 | 3e-04 | 24/47 (HOP62, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.53×** | +4.5 | 6e-04 | 27/49 (BT-474, Panc 03.27, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.24×** | +4.4 | 8e-04 | 24/48 (SW480, HT-29, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.51×** | +4.4 | 9e-04 | 24/45 (KATO III, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~24% here); noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.49×** | +4.2 | 0.002 | 23/49 (AsPC-1, H4, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.22×** | +4.1 | 0.003 | 23/48 (SW1417, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.22×** | +4.1 | 0.003 | 22/48 (SW480, AsPC-1, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.22×** | +4.0 | 0.003 | 21/47 (A-427, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.21×** | +3.8 | 0.007 | 23/48 (SNU-423, A-427, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Verteporfin (drug)]] 5 µM |  | **1.21×** | +3.7 | 0.010 | 21/49 (HepG2/C3A, A-172, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.20×** | +3.5 | 0.015 | 19/48 (SW480, KATO III, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7102.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.514×** | -13.0 | 9e-36 | 42/44 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.541×** | -12.5 | 4e-33 | 40/49 (HCT15, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.674×** | -11.3 | 2e-27 | 33/48 (A498, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.692×** | -10.5 | 7e-24 | 33/49 (HS-578T, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.627×** | -8.7 | 2e-16 | 34/45 (HT-29, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.648×** | -8.5 | 3e-15 | 38/48 (A498, A549, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.664×** | -8.3 | 9e-15 | 38/48 (A498, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.694×** | -7.4 | 8e-12 | 30/48 (A-427, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.770×** | -5.1 | 2e-05 | 24/48 (HOP62, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.790×** | -4.6 | 2e-04 | 26/50 (HOP62, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.809×** | -4.3 | 8e-04 | 23/48 (NCI-H2347, A498, …) | all doses, stronger at high dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.949× | -3.8 | 0.006 | 1/50 (MIA PaCa-2) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.832×** | -3.7 | 0.008 | 22/48 (A-427, HOP62, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~54% of this change | **0.833×** | -3.7 | 0.008 | 23/48 (HOP62, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.829×** | -3.7 | 0.009 | 22/47 (A498, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | 0.862× | -3.3 | 0.038 | 15/48 (HOP62, COLO 205, …) | two highest doses | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 0.855× | -3.1 | 0.065 | 13/48 (HOP62, NCI-H2347, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | 0.881× | -3.0 | 0.082 | 14/49 (HOP62, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7102. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 333 | 0 | 10 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.372× (z -17.7) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.516× (z -11.9) |
| [[PANC-1 (line)]] | alt | 164 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.405× (z -16.8) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.540× (z -11.5) |
| [[HOP62 (line)]] | alt | 110 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.542× (z -11.2) |
| [[NCI-H460 (line)]] | wt | 111 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.198× (z -17.7) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 82.9 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.117× (z -17.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.266× (z -10.8) |
| [[SW480 (line)]] | alt | 74.4 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.11× (z +11.2) | [[Dinaciclib (drug)]] 0.5 µM 0.462× (z -11.6) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 72.1 | 0 | 4 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.328× (z -11.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.431× (z -9.1) |
| [[NCI-H2030 (line)]] | alt | 59.1 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.467× (z -11.2) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.549× (z -8.8) |
| [[NCI-H596 (line)]] | alt | 75.5 | 2 | 2 | [[Oxaprozin (drug)]] 5 µM 2.05× (z +15.1) | [[Canagliflozin (hemihydrate) (drug)]] 5 µM 0.464× (z -16.5) |
| [[A-172 (line)]] | wt | 101 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.259× (z -15.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.484× (z -8.6) |
| [[AsPC-1 (line)]] | alt | 50.0 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.30× (z +12.0) | — |
| [[J82 (line)]] | alt | 114 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.493× (z -12.4) |
| [[KATO III (line)]] | alt | 95.6 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.337× (z -12.0) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 65.7 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.300× (z -11.2) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 46.3 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.369× (z -14.1) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.332× (z -11.0) |
| [[NCI-H2347 (line)]] | alt | 67.0 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.483× (z -12.1) |
| [[SW1417 (line)]] | alt | 79.9 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.475× (z -11.8) |
| [[BT-474 (line)]] | alt | 112 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +14.6) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.80× (z +9.1) | — |
| [[H4 (line)]] | wt | 106 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.195× (z -13.1) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 106 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.401× (z -15.5) |
| [[HT-29 (line)]] | alt | 69.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.144× (z -18.1) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 87.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.389× (z -9.4) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 29.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.239× (z -12.3) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 238 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.482× (z -11.7) ⚠ cell-cycle shift, explains ~39% of this change |
| [[NCI-H23 (line)]] | alt | 63.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.190× (z -15.6) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 82.8 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.530× (z -9.5) |
| [[SHP-77 (line)]] | alt | 135 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.305× (z -11.7) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 66.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.341× (z -9.6) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 71.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.215× (z -11.4) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 46.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.324× (z -11.5) |
| [[HCT15 (line)]] | alt | 57.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0780× (z -19.3) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 59.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.193× (z -14.3) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 99.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 56.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 43.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 59.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 48.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 89.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 80.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 75.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 48.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 75.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 82.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 92.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 83.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 143 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 151 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 93.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7102), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*46 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LIMK1]] | +0.72 | +0.70 / +0.62 | both halves | 7e-06 |  |
| [[PACC1]] | +0.71 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[TPST2]] | +0.71 | +0.73 / +0.54 | both halves | 1e-05 |  |
| [[AP3M2]] | +0.71 | +0.69 / +0.56 | both halves | 1e-05 |  |
| [[ANKRD27]] | +0.69 | +0.66 / +0.41 | both halves | 4e-05 |  |
| [[LPCAT4]] | +0.68 | +0.69 / +0.46 | both halves | 3e-05 |  |
| [[MPZL1]] | +0.68 | +0.67 / +0.52 | both halves | 1e-05 |  |
| [[PBX4]] | +0.67 | +0.61 / +0.42 | both halves | 4e-05 |  |
| [[YIF1B]] | +0.66 | +0.63 / +0.27 | both halves | 3e-04 |  |
| [[PIP4K2A]] | +0.66 | +0.68 / +0.47 | both halves | 2e-05 |  |
| [[TMEM120B]] | +0.66 | +0.60 / +0.46 | both halves | 2e-05 |  |
| [[ST6GALNAC4]] | +0.66 | +0.60 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*54 of its nearest partners move opposite, 11 of them with an alert (⚠; 11 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM202-AS1]] | -0.73 | -0.74 / -0.39 | both halves | 6e-05 |  |
| [[KRCC1]] | -0.71 | -0.75 / -0.41 | both halves | 4e-05 |  |
| [[METTL6]] | -0.70 | -0.75 / -0.34 | both halves | 1e-04 |  |
| [[PCNX4-DT]] | -0.70 | -0.73 / -0.37 | both halves | 8e-05 |  |
| [[THAP2]] | -0.70 | -0.71 / -0.37 | both halves | 8e-05 |  |
| [[SEPTIN7-DT]] | -0.69 | -0.71 / -0.32 | both halves | 2e-04 |  |
| [[AK9]] | -0.69 | -0.73 / -0.33 | both halves | 1e-04 |  |
| [[PATL2]] | -0.69 | -0.70 / -0.39 | both halves | 6e-05 |  |
| [[N4BP2L1]] | -0.68 | -0.71 / -0.38 | both halves | 7e-05 |  |
| [[TAPBPL]] | -0.68 | -0.66 / -0.47 | both halves | 2e-05 |  |
| [[GABPB2]] | -0.68 | -0.69 / -0.36 | both halves | 1e-04 |  |
| [[AEBP2]] | -0.68 | -0.58 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ROR1]] | B | ROR1 activity raises GNA12's level | lines that do not express ROR1 (14) vs lines expressing it (36) | 1.41× lower at baseline in the lines without ROR1 | 0.040 | ⚠ within organs, on part of the lines |
| [[TOP2A]] | B | TOP2A activity raises GNA12's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[DNMT3B]] | C | DNMT3B activity raises GNA12's level | lines that do not express DNMT3B (4) vs lines expressing it (46) | 1.91× lower at baseline in the lines without DNMT3B | 0.058 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CCDC113, SLC29A4, MYBL2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 077]]; 59 genes; this gene is in the **+** arm (projection on the module's main direction 0.781). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.44).
- **Nodal map** (x, y) = (3.3, 4.5); signed map (-42.0, -6.0). **Vector** length 113, 32.6% of its response variance represented; |z| ≥ 3 in 1,115 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +7.3 | +9.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +7.0 | +10.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | +6.5 | +9.7 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +5.0 | +5.0 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +4.8 | +4.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.8 | +4.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.5 | +2.5 |
|  | [[Gemcitabine (drug)]] 0.05 µM |  | +1.4 | +1.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.4 | -0.3 |
|  | [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.05 µM |  | +1.4 | +1.7 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -10.7 | -11.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -9.1 | -7.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -7.0 | -8.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -6.0 | -8.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.4 | -10.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.7 | -4.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.4 | -2.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.9 | -3.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.3 | -3.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.2 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | G protein subunit alpha 12 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p22.3-p22.2 — chr7:2,721,822-2,870,786 (-) |
| Ensembl biotype | protein_coding |
| Also known as | gep |
| Gene groups (HGNC) | G protein subunits alpha, group 12/13 |
| Reactome | 6 pathways, smallest: Thrombin signalling through proteinase activated receptors (PARs); G alpha (12/13) signalling events; Platelet activation, signaling and aggregation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q03113](https://www.uniprot.org/uniprotkb/Q03113) (Guanine nucleotide-binding protein subunit alpha-12):

> Guanine nucleotide-binding proteins (G proteins) are involved as modulators or transducers in various transmembrane signaling systems. Activates effector molecule RhoA by binding and activating RhoGEFs (ARHGEF12/LARG). GNA12-dependent Rho signaling subsequently regulates transcription factor AP-1 (activating protein-1) (By similarity). GNA12-dependent Rho signaling also regulates protein phosphatese 2A activation causing dephosphorylation of its target proteins. Promotes tumor cell invasion and …

**Summary**, from NCBI Gene [2768](https://www.ncbi.nlm.nih.gov/gene/2768):

> Enables G protein activity; protein phosphatase 2A binding activity; and protein phosphatase activator activity. Involved in Rho-activating G protein-coupled receptor signaling pathway; regulation of TOR signaling; and regulation of proteasomal ubiquitin-dependent protein catabolic process. Located in several cellular components, including cytosol; lateral plasma membrane; and neuronal cell body. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:4380](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4380) · Entrez [2768](https://www.ncbi.nlm.nih.gov/gene/2768) · UniProt [Q03113](https://www.uniprot.org/uniprotkb/Q03113) · Ensembl [ENSG00000146535](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000146535)

## Data

Gene col 7102: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7102); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7102, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7102]; `tensor/DDL_lfc|DDL_z.npy` [7102]; `embed/gene_vectors.npy` [7102]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7102 or target_col == 7102). Every well: [[GNA12 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GNA12.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
