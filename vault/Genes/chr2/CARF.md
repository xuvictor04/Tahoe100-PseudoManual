---
symbol: "CARF"
type: "gene"
col: 6163
ensembl_id: "ENSG00000138380"
name: "calcium responsive transcription factor"
location: "2q33.2"
module: 10
arm: "+"
pooled_cpm: 15.45
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 36
n_dd_up_clean: 2
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# CARF

*calcium responsive transcription factor* — 2q33.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Ponatinib (drug)]] 5 µM: 1.53× (z +3.9, q 0.046, up in 27 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H460 3.50×; ⚠ cell-cycle shift, would explain all of this change).
> Pooled over the cell lines (median), lowered significantly by 36 drug-doses (17 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.211× (z -14.3, q 7e-44, down in 45 of 48 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.296× (z -11.2, q 9e-27, down in 41 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM174A-DT]] (+0.69, fdr 7e-06), [[BDNF-AS]] (+0.69, fdr 7e-06), [[LINC00412]] (+0.68, fdr 7e-06); moves opposite to [[BACE2]] (-0.54, fdr 8e-05), [[ZCCHC17]] (-0.54, fdr 3e-04), [[TMEM184B]] (-0.53, fdr 1e-04).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[FBXO15]] → it (grade B ⚠); 1 goes from it, the strongest it → [[PPP1CB-DT]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6163.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H460 3.50×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **1.53×** | +3.9 | 0.046 | 27/48 (KATO III, LS 180, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.48×** | +3.6 | 0.083 | 22/46 (KATO III, A-427, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.47× | +3.4 | 0.13 | 17/46 (HS-578T, NCI-H460, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.42× | +3.3 | 0.16 | 16/46 (SW480, C32, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 1.40× | +3.1 | 0.17 | 17/46 (A549, HS-578T, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.29× | +3.1 | 0.17 | 16/48 (SW480, NCI-H23, …) | all doses, flat |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 1.39× | +3.1 | 0.17 | 15/47 (KATO III, J82, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 17 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 36 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6163.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.211×** | -14.3 | 7e-44 | 45/48 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.296×** | -11.2 | 9e-27 | 41/46 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.308×** | -10.9 | 3e-25 | 40/44 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.321×** | -10.5 | 1e-23 | 41/46 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.348×** | -9.7 | 2e-20 | 39/47 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.433×** | -7.7 | 1e-12 | 35/46 (PANC-1, SW480, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.428×** | -7.5 | 5e-12 | 35/47 (PANC-1, A549, …) | rises with dose | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.448×** | -7.0 | 2e-10 | 34/47 (PANC-1, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~36% of this change | **0.469×** | -6.7 | 1e-09 | 30/42 (NCI-H23, SK-MEL-2, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.617×** | -6.3 | 2e-08 | 29/46 (PANC-1, A549, …) | rises with dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.520×** | -6.0 | 9e-08 | 30/47 (PANC-1, SW480, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.518×** | -5.7 | 5e-07 | 26/48 (SW480, PANC-1, …) | all doses, stronger at high dose | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.375×** | -4.7 | 1e-04 | 27/43 (C32, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.604×** | -4.6 | 1e-04 | 24/47 (PANC-1, A549, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.392×** | -4.5 | 2e-04 | 28/48 (PANC-1, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.405×** | -4.4 | 5e-04 | 26/47 (HT-29, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.625×** | -4.3 | 5e-04 | 26/45 (SNU-1, HT-29, …) | two highest doses |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.642×** | -4.1 | 0.001 | 22/48 (SW48, LOX-IMVI, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.644×** | -4.1 | 0.001 | 25/46 (PANC-1, SW480, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.745×** | -3.8 | 0.003 | 25/47 (NCI-H1573, MIA PaCa-2, …) | two highest doses |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.604×** | -3.3 | 0.020 | 14/48 (NCI-H23, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.610×** | -3.3 | 0.024 | 14/47 (PANC-1, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.703×** | -3.2 | 0.024 | 17/47 (NCI-H23, LOX-IMVI, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.696×** | -3.2 | 0.026 | 18/46 (NCI-H23, RKO, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.30 per unit of S-phase module lfc, -0.60 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6163. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 34.3 | 0 | 14 (8 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0620× (z -21.8) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.123× (z -16.4) |
| [[SW480 (line)]] | alt | 18.4 | 0 | 9 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0817× (z -18.2) |
| [[A-427 (line)]] | wt | 17.5 | 0 | 6 (3 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.108× (z -12.0) ⚠ cell-cycle shift, explains ~77% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.121× (z -11.9) |
| [[A549 (line)]] | wt | 18.2 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.138× (z -13.8) ⚠ cell-cycle shift, would explain all of this change |
| [[H4 (line)]] | wt | 15.8 | 0 | 5 (4 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0501× (z -11.3) |
| [[LOX-IMVI (line)]] | wt | 16.3 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0352× (z -17.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.112× (z -11.7) |
| [[HEC-1-A (line)]] | alt | 22.5 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -11.3) ⚠ cell-cycle shift, would explain all of this change |
| [[J82 (line)]] | alt | 11.4 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0536× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.148× (z -8.6) |
| [[KATO III (line)]] | alt | 16.5 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0990× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.139× (z -10.6) |
| [[NCI-H23 (line)]] | alt | 19.7 | 0 | 3 (2 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0923× (z -13.4) ⚠ cell-cycle shift, explains ~77% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.188× (z -9.8) |
| [[NCI-H460 (line)]] | wt | 19.0 | 1 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.50× (z +10.5) ⚠ cell-cycle shift, would explain all of this change | [[Digitoxin (drug)]] 5 µM 0.106× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.235× (z -8.6) |
| [[SW1417 (line)]] | alt | 15.7 | 0 | 3 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0970× (z -12.8) ⚠ cell-cycle shift, explains ~26% of this change |
| [[A-172 (line)]] | wt | 24.2 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.209× (z -9.2) |
| [[COLO 205 (line)]] | alt | 19.5 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -12.7) ⚠ cell-cycle shift, would explain all of this change |
| [[HT-29 (line)]] | alt | 11.3 | 0 | 2 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.120× (z -10.5) |
| [[MIA PaCa-2 (line)]] | alt | 14.2 | 0 | 2 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.0952× (z -11.1) |
| [[NCI-H1573 (line)]] | alt | 22.7 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.125× (z -12.6) ⚠ cell-cycle shift, explains ~26% of this change |
| [[SK-MEL-2 (line)]] | alt | 15.9 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0828× (z -12.2) ⚠ toxic; cell-cycle shift, explains ~36% of this change |
| [[A498 (line)]] | wt | 14.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -10.0) ⚠ cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 16.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.315× (z -8.6) ⚠ cell-cycle shift, would explain all of this change |
| [[hTERT-HPNE (line)]] | wt | 14.1 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0838× (z -9.4) ⚠ cell-cycle shift, explains ~26% of this change |
| [[LoVo (line)]] | wt | 9.97 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.210× (z -8.8) |
| [[Panc 03.27 (line)]] | alt | 11.3 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.148× (z -8.6) ⚠ cell-cycle shift, explains ~26% of this change |
| [[SHP-77 (line)]] | alt | 14.3 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.129× (z -9.0) ⚠ cell-cycle shift, explains ~26% of this change |
| [[SNU-423 (line)]] | alt | 10.9 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0978× (z -9.5) ⚠ cell-cycle shift, explains ~26% of this change |
| [[SW 900 (line)]] | alt | 12.2 | 0 | 1 | — | [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.5 µM 0.0997× (z -10.3) |
| [[AN3 CA (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.90 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.40 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.91 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.46 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.66 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.24 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.43 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.83 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6163), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM174A-DT]] | +0.69 | +0.69 / +0.63 | both halves | 7e-06 |  |
| [[BDNF-AS]] | +0.69 | +0.74 / +0.61 | both halves | 7e-06 |  |
| [[LINC00412]] | +0.68 | +0.72 / +0.61 | both halves | 7e-06 |  |
| [[TMEM9B-AS1]] | +0.67 | +0.70 / +0.51 | both halves | 1e-05 |  |
| [[LINC02482]] | +0.66 | +0.69 / +0.51 | both halves | 1e-05 |  |
| [[KLHDC1]] | +0.64 | +0.74 / +0.46 | both halves | 3e-05 |  |
| [[SLC24A1]] | +0.64 | +0.65 / +0.53 | both halves | 1e-05 |  |
| [[FAM227B]] | +0.64 | +0.70 / +0.45 | both halves | 3e-05 |  |
| [[BICRAL]] | +0.63 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[CCDC191]] | +0.63 | +0.73 / +0.54 | both halves | 1e-05 |  |
| [[MAD2L1-DT]] | +0.63 | +0.72 / +0.46 | both halves | 2e-05 |  |
| [[LINC00886]] | +0.63 | +0.66 / +0.37 | both halves | 8e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BACE2]] | -0.54 | -0.59 / -0.37 | both halves | 8e-05 |  |
| [[ZCCHC17]] | -0.54 | -0.57 / -0.28 | both halves | 3e-04 |  |
| [[TMEM184B]] | -0.53 | -0.55 / -0.34 | both halves | 1e-04 |  |
| [[CPOX]] | -0.52 | -0.54 / -0.41 | both halves | 4e-05 |  |
| [[NGLY1]] | -0.52 | -0.53 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FBXO15]] | B | FBXO15 activity raises CARF's level | lines that do not express FBXO15 (6) vs lines expressing it (44) | 1.63× lower at baseline in the lines without FBXO15 | 0.098 | ⚠ within organs, on part of the lines; also absent: DNAI1, EFCAB6, KCNK15-AS1 |
| [[CCDC171]], [[RFX3-DT]] | C | CCDC171, RFX3-DT activity raises CARF's level | lines that do not express CCDC171, RFX3-DT (3) vs lines expressing them (47) | 2.33× lower at baseline in the lines without CCDC171, RFX3-DT | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: POGLUT2, ANAPC1P4, WDR35; maybe low, not absent; its own permutation p; co-absent genes |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PPP1CB-DT]] | C | CARF's natural level strengthens PPP1CB-DT's drug response | CARF's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.62, reverse +0.53; direction not clear | 0.095 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.690). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (5.4, 17.9); signed map (30.9, -11.6). **Vector** length 63.5, 13.2% of its response variance represented; |z| ≥ 3 in 1,167 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.9 | +0.8 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +2.5 | -4.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.1 | +3.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.0 | -0.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.9 | +2.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.8 | +1.5 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.7 | +3.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.6 | -4.7 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -3.6 | -9.7 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -3.3 | -7.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.8 | -0.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.8 | -6.0 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | -2.6 | -4.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.4 | -7.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.1 | -3.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.9 | -3.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.9 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | calcium responsive transcription factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q33.2 — chr2:202,912,214-202,988,263 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ21579, NYD-SP24; previously ALS2CR8 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N187](https://www.uniprot.org/uniprotkb/Q8N187) (Calcium-responsive transcription factor):

> Acts as a transcriptional activator that mediates the calcium- and neuron-selective induction of BDNF exon III transcription. Binds to the consensus calcium-response element CaRE1 5'-CTATTTCGAG-3' sequence.

**Summary**, from NCBI Gene [79800](https://www.ncbi.nlm.nih.gov/gene/79800):

> Enables DNA binding activity and DNA-binding transcription activator activity, RNA polymerase II-specific. Involved in cellular response to calcium ion. Predicted to be located in granular component. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:14435](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14435) · Entrez [79800](https://www.ncbi.nlm.nih.gov/gene/79800) · UniProt [Q8N187](https://www.uniprot.org/uniprotkb/Q8N187) · Ensembl [ENSG00000138380](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138380)

## Data

Gene col 6163: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6163); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6163, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6163]; `tensor/DDL_lfc|DDL_z.npy` [6163]; `embed/gene_vectors.npy` [6163]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6163 or target_col == 6163). Every well: [[CARF — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CARF.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
