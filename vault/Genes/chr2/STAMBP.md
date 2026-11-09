---
symbol: "STAMBP"
type: "gene"
col: 4521
ensembl_id: "ENSG00000124356"
name: "STAM binding protein"
location: "2p13.1"
module: 28
arm: "+"
pooled_cpm: 70.22
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 13
n_dd_up_clean: 4
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# STAMBP

*STAM binding protein* — 2p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.41× (z +10.0, q 6e-21, up in 31 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.25× (z +9.1, q 4e-17, up in 26 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.554× (z -17.3, q 0e+00, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[METTL6]] (+0.68, fdr 1e-05), [[FBXO38]] (+0.67, fdr 1e-05), [[ZNF585A]] (+0.65, fdr 2e-04); moves opposite to [[UBE2G1]] (-0.60, fdr 3e-05), [[NME2]] (-0.58, fdr 8e-05), [[FAM118A]] (-0.58, fdr 2e-04).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4521.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.41×** | +10.0 | 6e-21 | 31/49 (NCI-H460, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.25×** | +9.1 | 4e-17 | 26/48 (NCI-H1573, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.30×** | +7.7 | 2e-12 | 29/48 (NCI-H1573, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.31×** | +7.6 | 4e-12 | 23/43 (Panc 03.27, SHP-77, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.18× | +7.0 | 4e-10 | 21/48 (SW480, NCI-H2030, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | 1.16× | +6.0 | 2e-07 | 17/48 (Panc 03.27, SW1417, …) | rises with dose | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~4% of this change | **1.21×** | +5.5 | 3e-06 | 21/48 (A498, A-427, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.21×** | +5.5 | 3e-06 | 23/48 (NCI-H1573, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.13× | +3.6 | 0.018 | 14/48 (RKO, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.13× | +3.6 | 0.019 | 9/48 (NCI-H460, A498, …) | two highest doses |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.13× | +3.5 | 0.024 | 10/48 (NCI-H1573, NCI-H2030, …) | rises with dose |  |
| [[Belzutifan (drug)]] 5 µM |  | **1.25×** | +3.4 | 0.035 | 13/47 (SW 900, H4, …) | top dose only | noisy plate (z scaled) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | 1.12× | +3.2 | 0.062 | 7/47 (C32, HS-578T, …) | inconsistent across doses | low cells (technical?) |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | 1.12× | +3.2 | 0.062 | 9/47 (A498, LoVo, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 5 with an alert ⚠; shown: the 15 strongest. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4521.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.554×** | -17.3 | 0e+00 | 37/48 (PANC-1, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.566×** | -16.7 | 0e+00 | 43/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.607×** | -13.8 | 5e-41 | 40/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.668×** | -11.1 | 1e-26 | 37/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.761×** | -7.6 | 5e-12 | 27/48 (HOP62, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.778×** | -7.4 | 1e-11 | 28/48 (HOP62, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.770×** | -7.4 | 1e-11 | 28/47 (LOX-IMVI, HOP62, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.783×** | -7.2 | 6e-11 | 23/48 (HOP62, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.789×** | -6.9 | 3e-10 | 25/48 (LOX-IMVI, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.859× | -6.3 | 1e-08 | 19/48 (HOP62, SW480, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.803×** | -6.1 | 6e-08 | 21/48 (SW1417, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~10% of this change | **0.818×** | -5.9 | 2e-07 | 21/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.754×** | -4.3 | 7e-04 | 19/49 (PANC-1, SHP-77, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.858× | -4.3 | 9e-04 | 13/48 (HOP62, LOX-IMVI, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~9% of this change | 0.874× | -4.0 | 0.003 | 15/48 (HOP62, SW480, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4521. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 111 | 0 | 11 (4 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.325× (z -13.9) ⚠ toxic · without an alert: [[TAK-901 (drug)]] 0.05 µM 0.374× (z -11.9) |
| [[HOP62 (line)]] | alt | 143 | 0 | 10 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.313× (z -13.7) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.378× (z -12.0) |
| [[NCI-H460 (line)]] | wt | 68.2 | 2 (1 ⚠) | 7 (4 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.75× (z +9.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 1.72× (z +8.8) | [[Digitoxin (drug)]] 5 µM 0.405× (z -14.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.425× (z -13.7) |
| [[NCI-H1792 (line)]] | alt | 109 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.522× (z -12.1) |
| [[PANC-1 (line)]] | alt | 73.7 | 1 | 6 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.52× (z +10.9) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.297× (z -22.2) |
| [[NCI-H1573 (line)]] | alt | 73.6 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +16.5) | — |
| [[SW480 (line)]] | alt | 81.2 | 1 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 1.60× (z +8.5) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.467× (z -13.7) |
| [[A-427 (line)]] | wt | 89.8 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.64× (z +9.8) | [[Dinaciclib (drug)]] 0.05 µM 0.332× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 84.0 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.223× (z -12.7) |
| [[HS-578T (line)]] | alt | 40.5 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.314× (z -10.8) |
| [[LS 180 (line)]] | wt | 65.0 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.298× (z -15.9) |
| [[SHP-77 (line)]] | alt | 68.2 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.427× (z -10.1) |
| [[AsPC-1 (line)]] | alt | 55.3 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.398× (z -9.9) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 89.5 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.394× (z -12.0) |
| [[NCI-H2030 (line)]] | alt | 87.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +15.9) | — |
| [[NCI-H23 (line)]] | alt | 110 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +12.0) | — |
| [[SNU-423 (line)]] | alt | 56.1 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.428× (z -9.7) |
| [[C32 (line)]] | wt | 45.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.371× (z -8.5) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 80.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.523× (z -9.2) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 53.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.04× (z +9.0) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 55.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.189× (z -12.9) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 40.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.368× (z -9.0) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 58.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.70× (z +10.5) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 83.6 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.406× (z -8.7) ⚠ toxic |
| [[RPMI-7951 (line)]] | alt | 75.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.331× (z -10.5) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 93.4 | 0 | 1 | — | [[Naproxen (drug)]] 5 µM 0.103× (z -8.6) |
| [[SW 900 (line)]] | alt | 73.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.381× (z -9.3) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 59.1 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.422× (z -10.2) |
| [[A-172 (line)]] | wt | 23.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 82.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 70.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 50.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 58.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 55.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 76.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 97.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 58.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 51.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 53.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 57.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 70.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 50.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 68.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 60.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 78.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 55.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 64.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 65.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4521), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[METTL6]] | +0.68 | +0.73 / +0.54 | both halves | 1e-05 |  |
| [[FBXO38]] | +0.67 | +0.72 / +0.56 | both halves | 1e-05 |  |
| [[ZNF585A]] | +0.65 | +0.78 / +0.32 | both halves | 2e-04 |  |
| [[AIMP1]] | +0.65 | +0.71 / +0.47 | both halves | 2e-05 |  |
| [[CCDC90B]] | +0.64 | +0.75 / +0.46 | both halves | 2e-05 |  |
| [[FUNDC1]] | +0.64 | +0.71 / +0.49 | both halves | 1e-05 |  |
| [[FAM200A]] | +0.64 | +0.75 / +0.34 | both halves | 1e-04 |  |
| [[SLC25A46]] | +0.63 | +0.68 / +0.51 | both halves | 1e-05 |  |
| [[FCF1]] | +0.63 | +0.75 / +0.42 | both halves | 4e-05 |  |
| [[ZNF181]] | +0.62 | +0.70 / +0.41 | both halves | 4e-05 |  |
| [[TMEM260]] | +0.62 | +0.66 / +0.40 | both halves | 5e-05 |  |
| [[CHM]] | +0.61 | +0.62 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBE2G1]] | -0.60 | -0.67 / -0.45 | both halves | 3e-05 |  |
| [[NME2]] | -0.58 | -0.66 / -0.37 | both halves | 8e-05 |  |
| [[FAM118A]] | -0.58 | -0.69 / -0.31 | both halves | 2e-04 |  |
| [[METAP1]] | -0.58 | -0.66 / -0.41 | both halves | 4e-05 |  |
| [[CMTM8]] | -0.58 | -0.61 / -0.40 | both halves | 4e-05 |  |
| [[LRP5L]] | -0.58 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[ATP8A1]] | -0.57 | -0.56 / -0.46 | both halves | 2e-05 |  |
| [[CBX2]] | -0.57 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[ADA]] | -0.56 | -0.54 / -0.54 | both halves | 1e-05 |  |
| [[LRRC20]] | -0.56 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[STK32C]] | -0.56 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[ABHD6]] | -0.56 | -0.55 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.647). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-30.0, 8.2); signed map (8.8, -23.0). **Vector** length 105, 25.8% of its response variance represented; |z| ≥ 3 in 1,090 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +10.3 | +7.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +9.2 | +9.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | +7.8 | +5.5 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +6.5 | +3.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.6 | +3.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.0 | +7.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.5 | +1.9 |
|  | [[Amsacrine (drug)]] 5 µM |  | +2.4 | +2.3 |
|  | [[Belzutifan (drug)]] 5 µM |  | +2.3 | +3.4 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -6.2 | -6.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -5.6 | -7.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.0 | -16.7 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~9% of this change | -4.8 | -4.0 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -4.7 | -13.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.8 | -1.5 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.0 | -0.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.8 | -2.2 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | -1.2 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | STAM binding protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p13.1 — chr2:73,828,916-73,873,659 (+) |
| Ensembl biotype | protein_coding |
| Also known as | AMSH |
| Gene groups (HGNC) | JAMM/MPN+ metallopeptidase family |
| Reactome | 2 pathways, smallest: Metalloprotease DUBs; Deubiquitination |
| Matched by | ensembl_id |

**Function**, from UniProt [O95630](https://www.uniprot.org/uniprotkb/O95630) (STAM-binding protein):

> Zinc metalloprotease that specifically cleaves 'Lys-63'-linked polyubiquitin chains. Does not cleave 'Lys-48'-linked polyubiquitin chains. Plays a role in signal transduction for cell growth and MYC induction mediated by IL-2 and GM-CSF. Potentiates BMP (bone morphogenetic protein) signaling by antagonizing the inhibitory action of SMAD6 and SMAD7. Has a key role in regulation of cell surface receptor-mediated endocytosis and ubiquitin-dependent sorting of receptors to lysosomes. Endosomal …

**Summary**, from NCBI Gene [10617](https://www.ncbi.nlm.nih.gov/gene/10617):

> Cytokine-mediated signal transduction in the JAK-STAT cascade requires the involvement of adaptor molecules. One such signal-transducing adaptor molecule contains an SH3 domain that is required for induction of MYC and cell growth. The protein encoded by this gene binds to the SH3 domain of the signal-transducing adaptor molecule, and plays a critical role in cytokine-mediated signaling for MYC induction and cell cycle progression. Multiple alternatively spliced transcript variants encoding the …

**Accessions** — [HGNC:16950](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16950) · Entrez [10617](https://www.ncbi.nlm.nih.gov/gene/10617) · UniProt [O95630](https://www.uniprot.org/uniprotkb/O95630) · Ensembl [ENSG00000124356](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000124356)

## Data

Gene col 4521: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4521); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4521, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4521]; `tensor/DDL_lfc|DDL_z.npy` [4521]; `embed/gene_vectors.npy` [4521]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4521 or target_col == 4521). Every well: [[STAMBP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STAMBP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
