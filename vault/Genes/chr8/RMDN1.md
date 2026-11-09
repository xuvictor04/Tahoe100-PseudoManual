---
symbol: "RMDN1"
type: "gene"
col: 10736
ensembl_id: "ENSG00000176623"
name: "regulator of microtubule dynamics 1"
location: "8q21.3"
module: 28
arm: "+"
pooled_cpm: 45.03
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 21
n_dd_up_clean: 5
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# RMDN1

*regulator of microtubule dynamics 1* — 8q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.67× (z +10.3, q 2e-22, up in 40 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Doxorubicin (hydrochloride) (drug)]] 5 µM: 1.69× (z +10.1, q 2e-21, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (8 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.488× (z -14.3, q 2e-43, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM149B1]] (+0.68, fdr 7e-06), [[TRAPPC6B]] (+0.58, fdr 1e-05), [[DMTF1]] (+0.58, fdr 1e-05); moves opposite to [[GNB1L]] (-0.51, fdr 4e-05), [[POLR3H]] (-0.49, fdr 3e-05), [[LRP8]] (-0.48, fdr 4e-05).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10736.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.67×** | +10.3 | 2e-22 | 40/48 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.69×** | +10.1 | 2e-21 | 38/48 (A498, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.36×** | +8.7 | 5e-16 | 30/48 (A498, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.56×** | +8.6 | 1e-15 | 30/38 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +7.2 | 7e-11 | 33/48 (HT-29, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.26×** | +6.7 | 2e-09 | 24/48 (RKO, J82, …) | rises with dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.22×** | +4.0 | 0.005 | 18/48 (AsPC-1, C-33 A, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.21×** | +3.8 | 0.008 | 18/48 (A-427, PANC-1, …) | all doses, stronger at high dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.31×** | +3.8 | 0.008 | 17/47 (HCT15, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 1.18× | +3.4 | 0.038 | 12/48 (CFPAC-1, HS-578T, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.18× | +3.4 | 0.038 | 14/48 (KATO III, J82, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 12 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10736.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.488×** | -14.3 | 2e-43 | 46/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.498×** | -13.8 | 4e-41 | 42/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.513×** | -13.3 | 7e-38 | 46/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.571×** | -11.1 | 1e-26 | 41/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.577×** | -10.9 | 1e-25 | 39/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.679×** | -10.8 | 2e-25 | 35/47 (LOX-IMVI, A549, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.391×** | -9.5 | 1e-19 | 39/49 (HCT15, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.394×** | -9.5 | 2e-19 | 39/47 (PANC-1, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.692×** | -7.3 | 2e-11 | 34/48 (Hs 766T, NCI-H460, …) | all doses, flat |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.694×** | -6.8 | 5e-10 | 34/48 (PANC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.722×** | -6.1 | 7e-08 | 29/47 (LOX-IMVI, C32, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.741×** | -5.9 | 2e-07 | 24/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.737×** | -5.8 | 3e-07 | 26/47 (PANC-1, H4, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.752×** | -5.6 | 8e-07 | 30/48 (SW480, PANC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.613×** | -5.0 | 3e-05 | 23/43 (SNU-1, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.841× | -3.4 | 0.020 | 16/48 (NCI-H661, Panc 03.27, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.786×** | -3.3 | 0.025 | 12/48 (PANC-1, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[crizotinib (drug)]] 5 µM |  | 0.857× | -2.9 | 0.084 | 10/48 (SW480, SNU-423, …) | top dose only |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.813×** | -2.8 | 0.097 | 5/48 (NCI-H460, NCI-H2030, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10736. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 65.3 | 0 | 9 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.311× (z -17.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.340× (z -16.3) |
| [[SW480 (line)]] | alt | 51.8 | 0 | 7 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.188× (z -20.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.209× (z -19.5) |
| [[H4 (line)]] | wt | 51.7 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.207× (z -11.2) |
| [[HOP62 (line)]] | alt | 51.4 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -14.5) |
| [[LOX-IMVI (line)]] | wt | 83.1 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.340× (z -17.3) |
| [[A498 (line)]] | wt | 50.3 | 4 (2 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.93× (z +11.2) | — |
| [[A549 (line)]] | wt | 49.7 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.313× (z -17.0) |
| [[NCI-H460 (line)]] | wt | 31.8 | 2 (2 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.87× (z +10.4) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.302× (z -12.0) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 58.8 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.211× (z -12.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.334× (z -8.9) |
| [[HS-578T (line)]] | alt | 62.2 | 1 | 2 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.90× (z +9.5) | [[Digitoxin (drug)]] 5 µM 0.339× (z -10.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.342× (z -9.9) |
| [[MIA PaCa-2 (line)]] | alt | 35.0 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.441× (z -9.7) |
| [[NCI-H1573 (line)]] | alt | 83.7 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.397× (z -14.5) |
| [[COLO 205 (line)]] | alt | 39.0 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.105× (z -16.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.388× (z -9.7) |
| [[J82 (line)]] | alt | 33.5 | 1 (1 ⚠) | 1 | [[Selinexor (drug)]] 5 µM 1.98× (z +8.7) ⚠ cell-cycle shift, explains ~22% of this change | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.359× (z -9.1) |
| [[RKO (line)]] | wt | 68.4 | 1 (1 ⚠) | 1 (1 ⚠) | [[Selinexor (drug)]] 5 µM 2.14× (z +9.6) ⚠ cell-cycle shift, explains ~22% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.161× (z -14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 42.2 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.89× (z +8.8) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.357× (z -8.5) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 40.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -15.5) |
| [[SW1417 (line)]] | alt | 27.4 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.31× (z +9.3) | [[Digitoxin (drug)]] 5 µM 0.298× (z -9.4) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 43.6 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.403× (z -8.5) |
| [[AsPC-1 (line)]] | alt | 33.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.42× (z +9.8) | — |
| [[C-33 A (line)]] | alt | 47.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.185× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 40.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.26× (z +8.5) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 58.9 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.341× (z -9.2) |
| [[HT-29 (line)]] | alt | 23.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.25× (z +8.7) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 43.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.280× (z -8.8) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 47.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.376× (z -9.8) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 30.6 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.320× (z -8.5) |
| [[Panc 03.27 (line)]] | alt | 28.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.420× (z -9.2) |
| [[RPMI-7951 (line)]] | alt | 53.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -12.7) |
| [[A-427 (line)]] | wt | 64.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 43.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 42.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 40.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 30.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 48.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 47.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 44.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 39.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 50.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 63.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 26.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10736), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM149B1]] | +0.68 | +0.72 / +0.62 | both halves | 7e-06 |  |
| [[TRAPPC6B]] | +0.58 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[DMTF1]] | +0.58 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[POLR1HASP]] | +0.58 | +0.57 / +0.49 | both halves | 1e-05 |  |
| [[PPP2R3C]] | +0.57 | +0.58 / +0.45 | both halves | 3e-05 |  |
| [[ERMARD]] | +0.56 | +0.57 / +0.46 | both halves | 3e-05 |  |
| [[RNF170]] | +0.55 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[LRRC40]] | +0.55 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[ACAD11]] | +0.55 | +0.57 / +0.47 | both halves | 2e-05 |  |
| [[COG4]] | +0.55 | +0.64 / +0.34 | both halves | 1e-04 |  |
| [[SLC30A9]] | +0.54 | +0.61 / +0.42 | both halves | 4e-05 |  |
| [[CBR4]] | +0.54 | +0.46 / +0.53 | both halves | 3e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNB1L]] | -0.51 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[POLR3H]] | -0.49 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[LRP8]] | -0.48 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[ARHGAP8]] | -0.48 | -0.50 / -0.33 | both halves | 1e-04 |  |
| [[ST3GAL4]] | -0.47 | -0.45 / -0.31 | both halves | 2e-04 |  |
| [[CMTM8]] | -0.47 | -0.51 / -0.23 | both halves | 5e-04 |  |
| [[SETD1A]] | -0.47 | -0.46 / -0.47 | both halves | 2e-05 |  |
| [[PIP5KL1]] | -0.46 | -0.47 / -0.36 | both halves | 1e-04 |  |
| [[TMEM201]] | -0.46 | -0.35 / -0.36 | both halves | 1e-04 |  |
| [[DCAF1]] | -0.45 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[ERCC2]] | -0.45 | -0.48 / -0.31 | both halves | 2e-04 |  |
| [[MRPL14]] | -0.45 | -0.43 / -0.29 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers RMDN1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.0% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[KCTD18]] | C | KCTD18's natural level strengthens RMDN1's drug response | KCTD18's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.64, reverse +0.22; direction not clear | 0.051 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.417). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-21.4, 20.3); signed map (19.0, -17.4). **Vector** length 82.1, 20.2% of its response variance represented; |z| ≥ 3 in 1,070 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +5.5 | +7.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.4 | +10.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | +5.0 | +6.7 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +3.3 | +4.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.7 | +2.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.2 | +1.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.9 | +1.3 |
|  | [[Bexarotene (drug)]] 5 µM |  | +1.9 | +1.0 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | +1.5 | +0.7 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~3% of this change | -3.3 | -3.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.3 | -10.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.0 | -6.1 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.8 | -0.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -2.3 | -6.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.3 | -2.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.8 | +2.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.7 | -9.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.7 | +0.4 |

## What is on record

|  |  |
|---|---|
| Name | regulator of microtubule dynamics 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q21.3 — chr8:86,468,257-86,514,357 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CGI-90, FLJ20665, RMD1; previously FAM82B |
| Matched by | ensembl_id |

UniProt [Q96DB5](https://www.uniprot.org/uniprotkb/Q96DB5) carries no function annotation.

**Summary**, from NCBI Gene [51115](https://www.ncbi.nlm.nih.gov/gene/51115):

> Enables microtubule binding activity. Predicted to be involved in attachment of mitotic spindle microtubules to kinetochore and mitotic spindle organization. Located in centrosome; mitotic spindle pole; and spindle microtubule. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:24285](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24285) · Entrez [51115](https://www.ncbi.nlm.nih.gov/gene/51115) · UniProt [Q96DB5](https://www.uniprot.org/uniprotkb/Q96DB5) · Ensembl [ENSG00000176623](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000176623)

## Data

Gene col 10736: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10736); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10736, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10736]; `tensor/DDL_lfc|DDL_z.npy` [10736]; `embed/gene_vectors.npy` [10736]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10736 or target_col == 10736). Every well: [[RMDN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RMDN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
