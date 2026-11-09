---
symbol: "SNX5"
type: "gene"
col: 1558
ensembl_id: "ENSG00000089006"
name: "sorting nexin 5"
location: "20p11.23"
module: 1
arm: "+"
pooled_cpm: 81.11
n_lines_expressing: 50
n_dd_up: 30
n_dd_down: 8
n_dd_up_clean: 17
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# SNX5

*sorting nexin 5* — 20p11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (13 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.86× (z +21.4, q 0e+00, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.571× (z -13.7, q 4e-40, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF124]] (+0.69, fdr 3e-05), [[SLC5A6]] (+0.68, fdr 1e-05), [[MCCC2]] (+0.68, fdr 9e-06); moves opposite to [[TECPR1]] (-0.75, fdr 1e-05), [[FAM89B]] (-0.69, fdr 1e-05), [[PIGH]] (-0.66, fdr 5e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 41 in all, 16 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1558.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.86×** | +21.4 | 0e+00 | 41/48 (AsPC-1, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.91×** | +15.7 | 0e+00 | 45/48 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.80×** | +14.3 | 3e-44 | 41/48 (LOX-IMVI, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.70×** | +12.9 | 1e-35 | 42/48 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.65×** | +12.2 | 3e-32 | 45/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **1.65×** | +12.2 | 3e-32 | 33/49 (A-427, A549, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **1.66×** | +11.9 | 9e-31 | 33/42 (A549, HepG2/C3A, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.66×** | +11.9 | 1e-30 | 39/47 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **1.58×** | +11.1 | 6e-27 | 37/48 (LoVo, NCI-H460, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.57×** | +11.0 | 4e-26 | 41/48 (AsPC-1, CFPAC-1, …) | all doses, flat |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +10.8 | 2e-25 | 31/49 (NCI-H2347, HT-29, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **1.52×** | +9.5 | 1e-19 | 31/45 (A549, C32, …) | all doses, stronger at high dose | composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.03×** | +9.0 | 8e-18 | 32/37 (HEC-1-A, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +8.8 | 4e-17 | 40/50 (MIA PaCa-2, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.27×** | +8.3 | 4e-15 | 31/48 (A-172, Panc 03.27, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **1.60×** | +6.0 | 6e-08 | 34/48 (AsPC-1, A549, …) | inconsistent across doses | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.58×** | +5.8 | 2e-07 | 33/48 (NCI-H460, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.53×** | +5.4 | 2e-06 | 29/48 (AsPC-1, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.51×** | +5.3 | 4e-06 | 24/48 (CFPAC-1, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.29×** | +4.4 | 2e-04 | 19/48 (NCI-H460, SW 900, …) | rises with dose | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.40×** | +4.3 | 4e-04 | 19/48 (NCI-H460, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | 1.19× | +4.0 | 0.001 | 17/48 (NCI-H460, SHP-77, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 2 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1558.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.571×** | -13.7 | 4e-40 | 41/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.579×** | -13.4 | 2e-38 | 36/48 (PANC-1, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.591×** | -12.9 | 1e-35 | 38/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.741×** | -7.4 | 3e-11 | 28/48 (PANC-1, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.754×** | -6.9 | 4e-10 | 27/48 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.825×** | -4.7 | 2e-04 | 24/47 (SK-MEL-2, HCT15, …) | two highest doses | low cells (technical?) |
| [[Brivudine (drug)]] 5 µM |  | **0.707×** | -4.5 | 7e-04 | 20/49 (PANC-1, LOX-IMVI, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | 0.837× | -4.2 | 0.002 | 18/47 (NCI-H2030, SW480, …) | two highest doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.898× | -3.8 | 0.010 | 11/48 (LS 180, KATO III, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | 0.859× | -3.6 | 0.018 | 12/47 (C-33 A, HOP62, …) | rises with dose |  |
| [[Cepharanthine (drug)]] 5 µM |  | 0.905× | -3.5 | 0.024 | 9/48 (NCI-H2030, LS 180, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 0.865× | -3.4 | 0.027 | 17/48 (HepG2/C3A, SNU-423, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.825×** | -3.4 | 0.031 | 16/48 (PANC-1, KATO III, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | 0.880× | -3.2 | 0.066 | 15/49 (PANC-1, HOP62, …) | rises with dose |  |
| [[Rapamycin (drug)]] 5 µM |  | 0.916× | -3.1 | 0.074 | 8/48 (HOP62, SW 900, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1558. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 88.3 | 8 (4 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +14.4) | [[Panobinostat (drug)]] 5 µM 0.443× (z -10.8) |
| [[LOX-IMVI (line)]] | wt | 102 | 6 (2 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +13.1) | [[Panobinostat (drug)]] 5 µM 0.471× (z -9.1) |
| [[LoVo (line)]] | wt | 98.4 | 7 (3 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.58× (z +16.5) | [[Belinostat (drug)]] 5 µM 0.515× (z -8.7) |
| [[PANC-1 (line)]] | alt | 97.5 | 3 (1 ⚠) | 5 | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +16.6) | [[Panobinostat (drug)]] 0.5 µM 0.415× (z -14.5) |
| [[A549 (line)]] | wt | 99.9 | 7 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.97× (z +12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.83× (z +10.0) | — |
| [[SW480 (line)]] | alt | 82.0 | 3 | 3 | [[Digitoxin (drug)]] 0.5 µM 2.06× (z +10.6) | [[Panobinostat (drug)]] 5 µM 0.399× (z -13.5) |
| [[CFPAC-1 (line)]] | alt | 54.8 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +14.1) | — |
| [[HEC-1-A (line)]] | alt | 80.3 | 2 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.15× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.55× (z +8.9) | [[Panobinostat (drug)]] 0.5 µM 0.529× (z -9.3) |
| [[A498 (line)]] | wt | 115 | 3 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +18.2) | [[Panobinostat (drug)]] 0.5 µM 0.571× (z -8.7) |
| [[C32 (line)]] | wt | 45.5 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.76× (z +18.3) | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.0866× (z -10.7) ⚠ toxic |
| [[COLO 205 (line)]] | alt | 80.3 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.17× (z +17.5) | — |
| [[AsPC-1 (line)]] | alt | 67.1 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.70× (z +19.7) | — |
| [[HOP62 (line)]] | alt | 83.0 | 3 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.60× (z +11.5) | — |
| [[HT-29 (line)]] | alt | 73.8 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.21× (z +12.1) | — |
| [[J82 (line)]] | alt | 72.4 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +13.2) | [[Belinostat (drug)]] 5 µM 0.426× (z -9.0) |
| [[KATO III (line)]] | alt | 118 | 2 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.25× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.66× (z +9.0) | [[Panobinostat (drug)]] 5 µM 0.510× (z -8.5) |
| [[LS 180 (line)]] | wt | 91.3 | 1 | 2 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.20× (z +9.2) | [[Panobinostat (drug)]] 0.5 µM 0.454× (z -9.2) |
| [[MIA PaCa-2 (line)]] | alt | 96.3 | 3 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.47× (z +9.9) | — |
| [[RKO (line)]] | wt | 124 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.05 µM 2.14× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | [[Panobinostat (drug)]] 5 µM 0.384× (z -11.5) |
| [[SNU-423 (line)]] | alt | 66.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +15.8) | — |
| [[SW48 (line)]] | wt | 136 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.268× (z -13.3) |
| [[A-172 (line)]] | wt | 52.8 | 2 (1 ⚠) | 0 | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 1.79× (z +8.9) | — |
| [[A-427 (line)]] | wt | 53.1 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.00× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | [[Belinostat (drug)]] 5 µM 0.419× (z -9.2) |
| [[C-33 A (line)]] | alt | 130 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.387× (z -9.1) |
| [[HepG2_C3A (line)]] | wt | 134 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.97× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[Hs 766T (line)]] | wt | 58.9 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.88× (z +9.8) | — |
| [[HS-578T (line)]] | alt | 66.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +15.3) | — |
| [[NCI-H2030 (line)]] | alt | 48.7 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.395× (z -9.6) |
| [[NCI-H2347 (line)]] | alt | 91.5 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.35× (z +13.3) | — |
| [[Panc 03.27 (line)]] | alt | 55.8 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.12× (z +10.4) | — |
| [[SK-MEL-2 (line)]] | alt | 63.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.17× (z +15.5) | — |
| [[SW 900 (line)]] | alt | 71.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +11.2) | — |
| [[hTERT-HPNE (line)]] | wt | 54.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +13.3) | — |
| [[NCI-H1573 (line)]] | alt | 23.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.82× (z +14.3) | — |
| [[NCI-H1792 (line)]] | alt | 24.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.97× (z +15.6) | — |
| [[NCI-H661 (line)]] | alt | 75.0 | 0 | 1 | — | [[Adenosine (drug)]] 5 µM 0.258× (z -9.0) |
| [[RPMI-7951 (line)]] | alt | 106 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.47× (z +9.1) | — |
| [[SNU-1 (line)]] | wt | 91.7 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.328× (z -9.0) |
| [[SW 1088 (line)]] | alt | 86.2 | 0 | 1 | — | [[Fenofibrate (drug)]] 5 µM 0.1000× (z -8.7) |
| [[AN3 CA (line)]] | alt | 103 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 75.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 99.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 90.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 64.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 54.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 77.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 144 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 88.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 57.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1558), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*55 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF124]] | +0.69 | +0.67 / +0.44 | both halves | 3e-05 |  |
| [[SLC5A6]] | +0.68 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[MCCC2]] | +0.68 | +0.63 / +0.57 | both halves | 9e-06 |  |
| [[ILF3]] | +0.68 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[OXCT1]] | +0.68 | +0.61 / +0.57 | both halves | 9e-06 |  |
| [[UTP20]] | +0.67 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[SRSF1]] | +0.67 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[EPM2A]] | +0.67 | +0.66 / +0.27 | both halves | 3e-04 |  |
| [[QTRT1]] | +0.67 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[USP13]] | +0.66 | +0.63 / +0.44 | both halves | 3e-05 |  |
| [[ANAPC1]] | +0.66 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[ANKRD18A]] | +0.66 | +0.59 / +0.35 | both halves | 1e-04 |  |

## Genes that move opposite

*45 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TECPR1]] | -0.75 | -0.62 / -0.52 | both halves | 1e-05 |  |
| [[FAM89B]] | -0.69 | -0.52 / -0.60 | both halves | 1e-05 |  |
| [[PIGH]] | -0.66 | -0.61 / -0.40 | both halves | 5e-05 |  |
| [[PLIN3]] | -0.66 | -0.59 / -0.62 | both halves | 7e-06 |  |
| [[RRAS]] | -0.66 | -0.59 / -0.46 | both halves | 2e-05 |  |
| [[YIF1B]] | -0.65 | -0.53 / -0.37 | both halves | 8e-05 |  |
| [[TNNT1]] | -0.65 | -0.59 / -0.55 | both halves | 1e-05 |  |
| [[EDF1]] | -0.65 | -0.52 / -0.46 | both halves | 2e-05 |  |
| [[PLCD1]] | -0.64 | -0.56 / -0.44 | both halves | 3e-05 |  |
| [[POLD4]] | -0.64 | -0.55 / -0.63 | both halves | 1e-05 |  |
| [[SLC27A1]] | -0.64 | -0.57 / -0.33 | both halves | 1e-04 |  |
| [[CARHSP1]] | -0.64 | -0.51 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SNX5's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.6% of all compounds | 0.041 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[STOX1]] | B | STOX1 activity raises SNX5's level | lines that do not express STOX1 (9) vs lines expressing it (41) | 1.35× lower at baseline in the lines without STOX1 | 0.053 | ⚠ within organs, on part of the lines; also absent: CACNA2D2, RIMS3, VASH2; maybe low, not absent |
| [[TMEM92]] | B | TMEM92 activity lowers SNX5's level | lines that do not express TMEM92 (22) vs lines expressing it (28) | 1.31× higher at baseline in the lines without TMEM92 | 0.057 | ⚠ within organs, on part of the lines; also absent: ARL14, LINC01589, TNFSF10 |
| [[HDAC6]] | B | HDAC6 activity raises SNX5's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.468). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-3.3, 5.7); signed map (21.6, -33.1). **Vector** length 117, 36.4% of its response variance represented; |z| ≥ 3 in 1,339 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +8.1 | +7.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +8.0 | +8.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +7.6 | +11.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.0 | +10.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | +6.4 | +11.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.4 | +8.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | +4.1 | +5.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +4.0 | +5.8 |
|  | [[EX229 (drug)]] 5 µM |  | +3.9 | +6.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.1 | +5.4 |
| fall | [[Belinostat (drug)]] 5 µM |  | -8.1 | -13.4 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -7.6 | -6.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -7.6 | -13.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | -6.5 | -12.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -5.8 | -7.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.4 | -4.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.0 | +2.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.9 | -4.7 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -2.8 | -2.3 |
|  | [[Retinoic acid (drug)]] 5 µM |  | -2.3 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | sorting nexin 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20p11.23 — chr20:17,941,597-17,968,980 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Sorting nexins; PX-BAR domain containing; Small nucleolar RNA protein coding host genes |
| Reactome | 4 pathways, smallest: Golgi Associated Vesicle Biogenesis; trans-Golgi Network Vesicle Budding; Membrane Trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y5X3](https://www.uniprot.org/uniprotkb/Q9Y5X3) (Sorting nexin-5):

> Involved in several stages of intracellular trafficking. Interacts with membranes containing phosphatidylinositol 3-phosphate (PtdIns(3P)) or phosphatidylinositol 3,4-bisphosphate (PtdIns(3,4)P2). Acts in part as component of the retromer membrane-deforming SNX-BAR subcomplex. The SNX-BAR retromer mediates retrograde transport of cargo proteins from endosomes to the trans-Golgi network (TGN) and is involved in endosome-to-plasma membrane transport for cargo protein recycling. The SNX-BAR …

**Summary**, from NCBI Gene [27131](https://www.ncbi.nlm.nih.gov/gene/27131):

> This gene encodes a member of the sorting nexin family. Members of this family contain a phox (PX) domain, which is a phosphoinositide binding domain, and are involved in intracellular trafficking. This protein functions in endosomal sorting, the phosphoinositide-signaling pathway, and macropinocytosis. This gene may play a role in the tumorigenesis of papillary thyroid carcinoma. Alternative splicing results in multiple transcript variants encoding different isoforms. [provided by RefSeq, Sep …

**Accessions** — [HGNC:14969](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14969) · Entrez [27131](https://www.ncbi.nlm.nih.gov/gene/27131) · UniProt [Q9Y5X3](https://www.uniprot.org/uniprotkb/Q9Y5X3) · Ensembl [ENSG00000089006](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000089006)

## Data

Gene col 1558: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1558); `tables/drug_effects.parquet` (56 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1558, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1558]; `tensor/DDL_lfc|DDL_z.npy` [1558]; `embed/gene_vectors.npy` [1558]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1558 or target_col == 1558). Every well: [[SNX5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SNX5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
