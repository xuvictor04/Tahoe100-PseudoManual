---
symbol: "MBP"
type: "gene"
col: 12502
ensembl_id: "ENSG00000197971"
name: "myelin basic protein"
location: "18q23"
module: 92
arm: "+"
pooled_cpm: 127.51
n_lines_expressing: 41
n_dd_up: 3
n_dd_down: 32
n_dd_up_clean: 3
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 3
direction_downstream: 4
tags: ["gene", "module/092"]
generated_by: "tahoemap"
---

# MBP

*myelin basic protein* — 18q23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[Auranofin (drug)]] 5 µM: 1.75× (z +12.6, q 8e-34, up in 30 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 32 drug-doses (15 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.342× (z -24.1, q 0e+00, down in 37 of 39 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AGO2]] (+0.59, fdr 1e-05), [[ADGRL4]] (+0.58, fdr 1e-05), [[PCED1B]] (+0.58, fdr 2e-05); moves opposite to [[POT1]] (-0.50, fdr 3e-05), [[ELP1]] (-0.50, fdr 2e-05), [[SRPX]] (-0.50, fdr 4e-05).
> It is in [[Module 092]], a single-armed module (MAPK output).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[PMEPA1]] → it (grade B ⚠); 4 go from it, the strongest it → [[SLIT2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12502.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.75×** | +12.6 | 8e-34 | 30/39 (SW480, HEC-1-A, …) | top dose only |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | 1.19× | +3.9 | 0.024 | 9/39 (SNU-1, NCI-H1573, …) | inconsistent across doses |  |
| [[4EGI-1 (drug)]] 5 µM |  | **1.37×** | +3.7 | 0.041 | 13/39 (J82, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 5 µM |  | **1.35×** | +3.6 | 0.051 | 11/39 (SHP-77, Hs 766T, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 5 µM |  | 1.32× | +3.3 | 0.13 | 11/40 (PANC-1, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Bestatin (hydrochloride) (drug)]] 0.5 µM |  | 1.15× | +3.2 | 0.13 | 8/39 (HOP62, PANC-1, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | 1.14× | +3.1 | 0.18 | 13/39 (NCI-H1792, MIA PaCa-2, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 54 in all, 20 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 32 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12502.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.342×** | -24.1 | 0e+00 | 37/39 (NCI-H460, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.379×** | -21.8 | 0e+00 | 36/39 (NCI-H460, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.446×** | -18.1 | 0e+00 | 37/39 (NCI-H460, A549, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.284×** | -14.8 | 0e+00 | 35/40 (PANC-1, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **0.528×** | -13.8 | 3e-41 | 26/36 (NCI-H460, HCT15, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.650×** | -13.6 | 3e-40 | 24/39 (NCI-H460, SNU-1, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | **0.601×** | -11.4 | 3e-28 | 29/40 (NCI-H460, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.393×** | -10.9 | 5e-26 | 29/39 (RKO, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.614×** | -10.5 | 5e-24 | 32/39 (COLO 205, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.637×** | -10.1 | 3e-22 | 26/39 (NCI-H23, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **0.634×** | -9.4 | 2e-19 | 27/37 (KATO III, RKO, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.663×** | -9.2 | 1e-18 | 27/39 (PANC-1, NCI-H460, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.674×** | -8.5 | 9e-16 | 23/39 (MIA PaCa-2, RKO, …) | top dose only | cell-cycle shift (explains ~20% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **0.696×** | -8.1 | 2e-14 | 27/39 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.729×** | -7.1 | 5e-11 | 23/39 (PANC-1, NCI-H23, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.726×** | -6.8 | 5e-10 | 23/39 (PANC-1, A549, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[EX229 (drug)]] 5 µM |  | **0.645×** | -5.1 | 8e-06 | 22/39 (NCI-H460, CFPAC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.651×** | -5.0 | 1e-05 | 22/39 (NCI-H460, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Budesonide (drug)]] 0.05 µM |  | **0.818×** | -4.5 | 2e-04 | 20/39 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.770×** | -4.2 | 6e-04 | 19/39 (NCI-H460, A549, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.834× | -4.0 | 0.001 | 15/40 (NCI-H460, NCI-H1792, …) | all doses, flat |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.718×** | -3.9 | 0.002 | 18/39 (NCI-H460, A549, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.39 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12502. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 317 | 0 | 43 (15 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.161× (z -28.2) |
| [[MIA PaCa-2 (line)]] | alt | 263 | 0 | 20 (12 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.163× (z -28.2) ⚠ cell-cycle shift, explains ~64% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.193× (z -18.1) |
| [[NCI-H1792 (line)]] | alt | 288 | 0 | 15 (7 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.584× (z -17.7) ⚠ position not correctable · without an alert: [[Panobinostat (drug)]] 5 µM 0.193× (z -15.4) |
| [[NCI-H23 (line)]] | alt | 83.4 | 1 | 11 (5 ⚠) | [[Auranofin (drug)]] 5 µM 2.67× (z +9.7) | [[Niclosamide (olamine) (drug)]] 5 µM 0.147× (z -18.2) ⚠ toxic; cell-cycle shift, explains ~60% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.335× (z -15.2) |
| [[PANC-1 (line)]] | alt | 213 | 0 | 12 (6 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.261× (z -17.7) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.288× (z -16.4) |
| [[SNU-1 (line)]] | wt | 273 | 0 | 10 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -24.0) |
| [[LOX-IMVI (line)]] | wt | 91.3 | 0 | 9 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.122× (z -20.5) |
| [[RKO (line)]] | wt | 58.6 | 0 | 9 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.196× (z -16.6) |
| [[HEC-1-A (line)]] | alt | 144 | 1 | 7 (1 ⚠) | [[Auranofin (drug)]] 5 µM 4.05× (z +20.7) | [[Panobinostat (drug)]] 5 µM 0.416× (z -13.0) |
| [[HT-29 (line)]] | alt | 176 | 1 | 7 (4 ⚠) | [[Auranofin (drug)]] 5 µM 3.85× (z +17.1) | [[Dinaciclib (drug)]] 5 µM 0.347× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.379× (z -12.2) |
| [[KATO III (line)]] | alt | 162 | 1 | 7 (4 ⚠) | [[Auranofin (drug)]] 5 µM 3.16× (z +15.9) | [[Dinaciclib (drug)]] 0.5 µM 0.326× (z -15.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.438× (z -11.4) |
| [[LoVo (line)]] | wt | 165 | 1 | 7 (4 ⚠) | [[Auranofin (drug)]] 5 µM 2.56× (z +13.9) | [[Panobinostat (drug)]] 5 µM 0.346× (z -15.6) |
| [[NCI-H1573 (line)]] | alt | 123 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -14.1) |
| [[A549 (line)]] | wt | 184 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0980× (z -24.2) |
| [[CFPAC-1 (line)]] | alt | 194 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.342× (z -14.2) |
| [[Hs 766T (line)]] | wt | 99.7 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.224× (z -13.8) |
| [[LS 180 (line)]] | wt | 256 | 0 | 7 (3 ⚠) | — | [[TAK-901 (drug)]] 5 µM 0.128× (z -11.9) |
| [[SW 900 (line)]] | alt | 135 | 0 | 7 (3 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.144× (z -14.8) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.149× (z -14.6) |
| [[SW48 (line)]] | wt | 110 | 1 | 6 (4 ⚠) | [[Auranofin (drug)]] 5 µM 2.58× (z +9.0) | [[Digitoxin (drug)]] 5 µM 0.222× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.296× (z -11.5) |
| [[SW480 (line)]] | alt | 59.9 | 1 | 6 (3 ⚠) | [[Auranofin (drug)]] 5 µM 4.51× (z +23.3) | [[Panobinostat (drug)]] 5 µM 0.339× (z -16.7) |
| [[COLO 205 (line)]] | alt | 218 | 3 (2 ⚠) | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.70× (z +12.4) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.05× (z +8.6) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.250× (z -16.6) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 5 µM 0.492× (z -8.8) |
| [[HOP62 (line)]] | alt | 65.2 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.224× (z -13.7) |
| [[NCI-H2030 (line)]] | alt | 128 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -17.0) |
| [[AsPC-1 (line)]] | alt | 91.5 | 0 | 5 | — | [[Harringtonine (drug)]] 5 µM 0.301× (z -11.8) |
| [[J82 (line)]] | alt | 60.5 | 4 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +14.4) | [[Panobinostat (drug)]] 5 µM 0.386× (z -9.7) |
| [[Panc 03.27 (line)]] | alt | 202 | 0 | 5 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.344× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.457× (z -9.6) |
| [[SHP-77 (line)]] | alt | 152 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.481× (z -10.2) |
| [[SNU-423 (line)]] | alt | 56.8 | 1 | 2 | [[Auranofin (drug)]] 5 µM 3.73× (z +11.7) | [[Panobinostat (drug)]] 5 µM 0.309× (z -10.3) |
| [[HCT15 (line)]] | alt | 155 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.181× (z -19.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.389× (z -11.0) |
| [[SK-MEL-2 (line)]] | alt | 67.1 | 1 | 1 | [[Auranofin (drug)]] 5 µM 2.84× (z +9.0) | [[Homoharringtonine (drug)]] 5 µM 0.404× (z -11.0) |
| [[SW 1271 (line)]] | alt | 210 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.144× (z -9.5) |
| [[SW1417 (line)]] | alt | 115 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.91× (z +16.1) | [[Dinaciclib (drug)]] 0.05 µM 0.416× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change |
| [[A-427 (line)]] | wt | 58.9 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.02× (z +13.8) | — |
| [[A498 (line)]] | wt | 46.4 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.31× (z +8.7) | — |
| [[BT-474 (line)]] | alt | 69.2 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.61× (z +11.5) | — |
| [[HepG2_C3A (line)]] | wt | 101 | 0 | 1 | — | [[Ponatinib (drug)]] 5 µM 0.383× (z -9.1) |
| [[NCI-H2347 (line)]] | alt | 84.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +9.6) | — |
| [[A-172 (line)]] | wt | 9.25 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 19.3 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 10.5 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 33.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 39.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.2 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 9.75 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 24.6 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 120 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.3 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 31.8 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 28.5 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12502), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AGO2]] | +0.59 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[ADGRL4]] | +0.58 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[PCED1B]] | +0.58 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[KIFC3]] | +0.56 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[DUSP4]] | +0.55 | +0.47 / +0.59 | both halves | 2e-05 |  |
| [[ACVR1C]] | +0.55 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[LINC01033]] | +0.54 | +0.36 / +0.53 | both halves | 9e-05 |  |
| [[LINC00472]] | +0.54 | +0.55 / +0.42 | both halves | 4e-05 |  |
| [[RESF1]] | +0.54 | +0.54 / +0.46 | both halves | 3e-05 |  |
| [[PMEPA1]] | +0.53 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[ANTXR2]] | +0.53 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[FST]] | +0.53 | +0.42 / +0.53 | both halves | 4e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POT1]] | -0.50 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[ELP1]] | -0.50 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[SRPX]] | -0.50 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[ANAPC5]] | -0.49 | -0.37 / -0.51 | both halves | 8e-05 |  |
| [[NDUFV1]] | -0.49 | -0.40 / -0.44 | both halves | 5e-05 |  |
| [[COPS8]] | -0.48 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[STRA6LP]] | -0.48 | -0.38 / -0.49 | both halves | 6e-05 |  |
| [[COPS4]] | -0.48 | -0.51 / -0.40 | both halves | 5e-05 |  |
| [[EEF1AKMT2]] | -0.48 | -0.30 / -0.49 | both halves | 2e-04 |  |
| [[SKIC3]] | -0.47 | -0.46 / -0.48 | both halves | 3e-05 |  |
| [[ALG9]] | -0.47 | -0.44 / -0.39 | both halves | 6e-05 |  |
| [[FAR1]] | -0.47 | -0.31 / -0.54 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PMEPA1]] | B | PMEPA1 activity raises MBP's level | lines that do not express PMEPA1 (6) vs lines expressing it (44) | 1.26× lower at baseline in the lines without PMEPA1 | 0.030 | ⚠ within organs, on part of the lines; also absent: SOX4, SLC2A1-DT, ENSG00000285253 |
| [[CDH4]] | B | CDH4 activity lowers MBP's level | lines that do not express CDH4 (32) vs lines expressing it (18) | 1.58× higher at baseline in the lines without CDH4 | 0.079 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KIRREL3, UCHL1, SIRLNT |
| [[KIFC3]] | C | KIFC3 activity raises MBP's level | lines that do not express KIFC3 (3) vs lines expressing it (47) | 4.21× lower at baseline in the lines without KIFC3 | 0.088 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; co-occurs with WNK2; also absent: SLC2A1, CEMIP2, S100A13; maybe low, not absent; its own permutation p |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLIT2]] | B | MBP activity lowers SLIT2's level | lines that do not express MBP (9) vs lines expressing it (41) | 5.86× higher at baseline in the lines without MBP | 0.031 | ⚠ within organs, on part of the lines; co-occurs with PTEN; also absent: RHPN1, CHMP4C, EVPL |
| [[AGO2]] | B | MBP activity raises AGO2's level | lines that do not express MBP (9) vs lines expressing it (41) | 1.54× lower at baseline in the lines without MBP | 0.056 | ⚠ within organs, on part of the lines; co-occurs with PTEN; also absent: RHPN1, CHMP4C, EVPL |
| [[MRPS31P4]] | B | MBP activity lowers MRPS31P4's level | lines that do not express MBP (9) vs lines expressing it (41) | 1.17× higher at baseline in the lines without MBP | 0.060 | ⚠ within organs, on part of the lines; co-occurs with PTEN; also absent: RHPN1, CHMP4C, EVPL |
| [[ADGRL4]] | B | MBP activity lowers ADGRL4's level | lines that do not express MBP (9) vs lines expressing it (41) | 1.53× higher at baseline in the lines without MBP | 0.078 | ⚠ within organs, on part of the lines; co-occurs with PTEN; also absent: RHPN1, CHMP4C, EVPL |

## Where it sits

- **Module**: [[Module 092]] — MAPK output; 49 genes; every member is in the + arm (projection on the module's main direction 0.496). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (42.0, 10.9); signed map (12.0, 43.3). **Vector** length 112, 33.2% of its response variance represented; |z| ≥ 3 in 1,516 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +12.5 | +12.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +6.0 | -3.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.7 | -13.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.4 | -8.5 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.7 | -0.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.6 | -2.0 |
|  | [[Rapamycin (drug)]] 5 µM |  | +3.0 | +1.7 |
|  | [[4EGI-1 (drug)]] 5 µM |  | +2.9 | +3.7 |
|  | [[BAY1125976 (drug)]] 5 µM |  | +2.7 | +3.6 |
| fall | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.6 | -3.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | -4.3 | -14.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.3 | -3.0 |
|  | [[venetoclax (drug)]] 5 µM |  | -4.2 | -3.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -3.9 | -3.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.7 | -2.2 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -3.6 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | myelin basic protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q23 — chr18:76,978,827-77,133,683 (-) |
| Ensembl biotype | protein_coding |
| Hallmark sets | REACTIVE_OXYGEN_SPECIES_PATHWAY |
| Reactome | 2 pathways, smallest: EGR2 and SOX10-mediated initiation of Schwann cell myelination; Nervous system development |
| Matched by | ensembl_id |

**Function**, from UniProt [P02686](https://www.uniprot.org/uniprotkb/P02686) (Myelin basic protein):

> The classic group of MBP isoforms (isoform 4-isoform 14) are with PLP the most abundant protein components of the myelin membrane in the CNS. They have a role in both its formation and stabilization. The smaller isoforms might have an important role in remyelination of denuded axons in multiple sclerosis. The non-classic group of MBP isoforms (isoform 1-isoform 3/Golli-MBPs) may preferentially have a role in the early developing brain long before myelination, maybe as components of …

**Summary**, from NCBI Gene [4155](https://www.ncbi.nlm.nih.gov/gene/4155):

> The protein encoded by the classic MBP gene is a major constituent of the myelin sheath of oligodendrocytes and Schwann cells in the nervous system. However, MBP-related transcripts are also present in the bone marrow and the immune system. These mRNAs arise from the long MBP gene (otherwise called "Golli-MBP") that contains 3 additional exons located upstream of the classic MBP exons. Alternative splicing from the Golli and the MBP transcription start sites gives rise to 2 sets of MBP-related …

**Accessions** — [HGNC:6925](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6925) · Entrez [4155](https://www.ncbi.nlm.nih.gov/gene/4155) · UniProt [P02686](https://www.uniprot.org/uniprotkb/P02686) · Ensembl [ENSG00000197971](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197971)

## Data

Gene col 12502: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12502); `tables/drug_effects.parquet` (61 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12502, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12502]; `tensor/DDL_lfc|DDL_z.npy` [12502]; `embed/gene_vectors.npy` [12502]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12502 or target_col == 12502). Every well: [[MBP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MBP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
