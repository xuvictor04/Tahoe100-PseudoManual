---
symbol: "HEATR6"
type: "gene"
col: 881
ensembl_id: "ENSG00000068097"
name: "HEAT repeat containing 6"
location: "17q23.1"
module: 17
arm: "+"
pooled_cpm: 27.45
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 23
n_dd_up_clean: 5
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# HEATR6

*HEAT repeat containing 6* — 17q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (none with an alert); the strongest is [[Ponatinib (drug)]] 5 µM: 1.42× (z +7.3, q 1e-10, up in 34 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.476× (z -21.9, q 0e+00, down in 43 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATG4C]] (+0.78, fdr 7e-06), [[JKAMP]] (+0.75, fdr 7e-06), [[ANAPC4]] (+0.75, fdr 7e-06); moves opposite to [[HIVEP2-DT]] (-0.68, fdr 7e-06), [[PSMD6-AS1]] (-0.66, fdr 1e-05), [[DDX5]] (-0.66, fdr 7e-06).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[C2orf27A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 881.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **1.42×** | +7.3 | 1e-10 | 34/48 (HOP62, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Radotinib (drug)]] 5 µM |  | **1.28×** | +7.2 | 1e-10 | 28/48 (PANC-1, SK-MEL-2, …) | rises with dose |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.24×** | +4.6 | 0.001 | 15/48 (HOP62, LOX-IMVI, …) | rises with dose |  |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | **1.23×** | +4.1 | 0.005 | 16/47 (Panc 03.27, LOX-IMVI, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.6 | 0.041 | 14/48 (RKO, BT-474, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | 1.18× | +3.4 | 0.060 | 15/48 (HOP62, RKO, …) | inconsistent across doses |  |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.18× | +3.4 | 0.060 | 9/48 (NCI-H2347, AsPC-1, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.34×** | +3.2 | 0.092 | 5/48 (C-33 A, BT-474, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | 1.16× | +3.1 | 0.12 | 13/48 (A-172, BT-474, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 881.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.476×** | -21.9 | 0e+00 | 43/47 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.406×** | -18.8 | 0e+00 | 44/48 (BT-474, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.400×** | -18.5 | 0e+00 | 42/48 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.494×** | -14.7 | 0e+00 | 36/47 (BT-474, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.624×** | -13.9 | 4e-42 | 46/48 (A549, A498, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.515×** | -13.3 | 1e-38 | 31/39 (A-172, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.548×** | -12.1 | 9e-32 | 39/48 (SNU-423, NCI-H460, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.568×** | -11.8 | 2e-30 | 35/44 (C-33 A, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.569×** | -10.9 | 6e-26 | 33/42 (SK-MEL-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.612×** | -10.3 | 5e-23 | 35/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.606×** | -10.1 | 3e-22 | 34/47 (NCI-H460, J82, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.634×** | -9.5 | 8e-20 | 35/47 (BT-474, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.653×** | -8.6 | 4e-16 | 33/47 (NCI-H460, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.689×** | -7.8 | 3e-13 | 30/48 (SW480, BT-474, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.768×** | -5.5 | 1e-06 | 23/48 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.858× | -4.5 | 2e-04 | 15/48 (SNU-1, A-172, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.815×** | -4.3 | 6e-04 | 20/47 (KATO III, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.828×** | -3.7 | 0.005 | 15/48 (CFPAC-1, NCI-H661, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[vincristine (drug)]] 0.5 µM |  | **0.802×** | -3.3 | 0.025 | 11/48 (HCT15, SW 1271, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[Gefitinib (drug)]] 5 µM |  | 0.855× | -3.3 | 0.026 | 7/48 (NCI-H460, HOP62, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 881. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 23.6 | 0 | 12 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.152× (z -17.3) |
| [[PANC-1 (line)]] | alt | 26.5 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -20.7) |
| [[A-172 (line)]] | wt | 27.1 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.103× (z -18.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.249× (z -17.0) |
| [[A498 (line)]] | wt | 26.3 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -18.0) |
| [[A549 (line)]] | wt | 44.1 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -19.4) |
| [[HOP62 (line)]] | alt | 28.6 | 0 | 6 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.139× (z -18.1) |
| [[KATO III (line)]] | alt | 20.5 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.189× (z -11.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.226× (z -11.1) |
| [[SNU-423 (line)]] | alt | 25.1 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.256× (z -14.1) |
| [[SW480 (line)]] | alt | 26.0 | 0 | 5 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.251× (z -15.4) |
| [[BT-474 (line)]] | alt | 76.5 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0889× (z -24.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.146× (z -19.1) |
| [[CFPAC-1 (line)]] | alt | 28.0 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.229× (z -12.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.401× (z -11.0) |
| [[HS-578T (line)]] | alt | 29.3 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -13.9) |
| [[C32 (line)]] | wt | 19.8 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.147× (z -15.8) |
| [[H4 (line)]] | wt | 43.6 | 0 | 3 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.172× (z -10.8) |
| [[HepG2_C3A (line)]] | wt | 20.4 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0737× (z -14.0) |
| [[Hs 766T (line)]] | wt | 15.4 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.152× (z -10.7) |
| [[NCI-H1792 (line)]] | alt | 30.6 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -15.6) |
| [[NCI-H2347 (line)]] | alt | 32.8 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.342× (z -10.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.412× (z -9.0) |
| [[SK-MEL-2 (line)]] | alt | 35.2 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -15.7) |
| [[SW 900 (line)]] | alt | 23.9 | 0 | 3 | — | [[Harringtonine (drug)]] 5 µM 0.143× (z -11.5) |
| [[SW48 (line)]] | wt | 36.0 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.174× (z -9.7) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.220× (z -8.7) |
| [[A-427 (line)]] | wt | 44.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.205× (z -14.6) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 54.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0848× (z -21.2) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 34.2 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.119× (z -12.5) ⚠ toxic; transcription drop · without an alert: [[Thymol (drug)]] 0.5 µM 0.222× (z -9.6) |
| [[hTERT-HPNE (line)]] | wt | 26.6 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0980× (z -13.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.352× (z -9.0) |
| [[J82 (line)]] | alt | 19.5 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.265× (z -9.7) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.411× (z -9.5) |
| [[MIA PaCa-2 (line)]] | alt | 20.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.156× (z -12.8) ⚠ cell-cycle shift, explains ~13% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.323× (z -11.0) |
| [[NCI-H2030 (line)]] | alt | 29.2 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.162× (z -13.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.341× (z -12.1) |
| [[NCI-H23 (line)]] | alt | 39.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.204× (z -13.8) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.357× (z -8.6) |
| [[RKO (line)]] | wt | 20.0 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.202× (z -9.2) |
| [[SHP-77 (line)]] | alt | 36.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0832× (z -18.6) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 19.6 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.285× (z -8.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.299× (z -8.6) |
| [[AN3 CA (line)]] | alt | 27.5 | 0 | 1 | — | [[Drospirenone (drug)]] 0.5 µM 0.0926× (z -9.3) |
| [[AsPC-1 (line)]] | alt | 10.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.228× (z -11.1) |
| [[COLO 205 (line)]] | alt | 19.0 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0709× (z -13.1) |
| [[HEC-1-A (line)]] | alt | 32.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.331× (z -10.6) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 12.1 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.190× (z -10.3) |
| [[LoVo (line)]] | wt | 16.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.222× (z -10.9) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 17.9 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.174× (z -11.3) |
| [[NCI-H661 (line)]] | alt | 46.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.201× (z -8.6) |
| [[Panc 03.27 (line)]] | alt | 30.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.298× (z -9.3) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 29.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -8.9) |
| [[CHP-212 (line)]] | wt | 75.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 30.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 39.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 881), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATG4C]] | +0.78 | +0.70 / +0.69 | both halves | 7e-06 |  |
| [[JKAMP]] | +0.75 | +0.77 / +0.73 | both halves | 7e-06 |  |
| [[ANAPC4]] | +0.75 | +0.72 / +0.66 | both halves | 7e-06 |  |
| [[TADA1]] | +0.73 | +0.72 / +0.69 | both halves | 7e-06 |  |
| [[POT1]] | +0.73 | +0.74 / +0.57 | both halves | 9e-06 |  |
| [[MRPS31P4]] | +0.72 | +0.70 / +0.59 | both halves | 7e-06 |  |
| [[EXD2]] | +0.72 | +0.75 / +0.62 | both halves | 7e-06 |  |
| [[METTL14]] | +0.71 | +0.68 / +0.67 | both halves | 7e-06 |  |
| [[ABHD10]] | +0.71 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[NCK1]] | +0.70 | +0.66 / +0.57 | both halves | 1e-05 |  |
| [[RAD17]] | +0.70 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[DDX55]] | +0.70 | +0.63 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HIVEP2-DT]] | -0.68 | -0.61 / -0.66 | both halves | 7e-06 |  |
| [[PSMD6-AS1]] | -0.66 | -0.57 / -0.60 | both halves | 1e-05 |  |
| [[DDX5]] | -0.66 | -0.58 / -0.65 | both halves | 7e-06 | same gene group |
| [[CDKN2B-AS1]] | -0.65 | -0.57 / -0.55 | both halves | 1e-05 |  |
| [[NLGN3]] | -0.63 | -0.58 / -0.55 | both halves | 1e-05 |  |
| [[PHF8]] | -0.62 | -0.55 / -0.42 | both halves | 4e-05 |  |
| [[SPON1-AS1]] | -0.61 | -0.60 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C2orf27A]] | B | C2orf27A activity raises HEATR6's level | lines that do not express C2orf27A (5) vs lines expressing it (45) | 1.92× lower at baseline in the lines without C2orf27A | 0.014 | ⚠ within organs, on part of the lines; also absent: NBEAP2, UBA6-DT, ENSG00000287621; maybe low, not absent |
| [[ABL1]] | B | ABL1 activity lowers HEATR6's level | compounds that target ABL1: 3 of 6 raise it (Flumatinib, Ponatinib, Radotinib) | 50% of the class's compounds vs 1.4% of all compounds | 0.036 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.755). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-4.0, -10.2); signed map (-29.9, -12.2). **Vector** length 101, 25.0% of its response variance represented; |z| ≥ 3 in 1,089 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.3 | +3.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +4.8 | +7.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.7 | +7.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.5 | -1.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.1 | +0.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.6 | +1.9 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +2.6 | +1.5 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.4 | +4.6 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -5.9 | -21.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.5 | -8.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.4 | -13.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.3 | -18.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.0 | -13.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.6 | -7.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.4 | -4.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.5 | -2.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.3 | -1.3 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -2.1 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | HEAT repeat containing 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q23.1 — chr17:60,041,008-60,078,922 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ABC1, FLJ22087 |
| Gene groups (HGNC) | Armadillo like helical domain containing; MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6AI08](https://www.uniprot.org/uniprotkb/Q6AI08) (HEAT repeat-containing protein 6):

> Amplification-dependent oncogene.

**Summary**, from NCBI Gene [63897](https://www.ncbi.nlm.nih.gov/gene/63897):

> Enables RNA binding activity. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24076](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24076) · Entrez [63897](https://www.ncbi.nlm.nih.gov/gene/63897) · UniProt [Q6AI08](https://www.uniprot.org/uniprotkb/Q6AI08) · Ensembl [ENSG00000068097](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000068097)

## Data

Gene col 881: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 881); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 881, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 881]; `tensor/DDL_lfc|DDL_z.npy` [881]; `embed/gene_vectors.npy` [881]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 881 or target_col == 881). Every well: [[HEATR6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HEATR6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
