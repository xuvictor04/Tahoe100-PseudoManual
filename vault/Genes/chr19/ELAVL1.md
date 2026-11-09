---
symbol: "ELAVL1"
type: "gene"
col: 816
ensembl_id: "ENSG00000066044"
name: "ELAV like RNA binding protein 1"
location: "19p13.2"
module: 20
arm: "+"
pooled_cpm: 56.7
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 2
n_dd_up_clean: 7
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# ELAVL1

*ELAV like RNA binding protein 1* — 19p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (16 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 4.02× (z +19.1, q 0e+00, up in 47 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 0.5 µM: 0.841× (z -4.6, q 0.002, down in 21 of 48 measured lines) ⚠ cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.901× (z -3.9, q 0.015, down in 15 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 2 lines (SK-MEL-2 0.552×, A-427 0.583×; ⚠ cell-cycle shift, would explain all of this change); [[Citalopram (hydrobromide) (drug)]] 0.05 µM in 1 line (NCI-H596 0.427×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (C-33 A 0.346×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change); [[Dorzolamide (hydrochloride) (drug)]] 0.05 µM in 1 line (SW 1271 0.0694×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM248]] (+0.70, fdr 7e-06), [[SMPD4]] (+0.69, fdr 7e-06), [[CHID1]] (+0.68, fdr 7e-06); moves opposite to [[ATF4]] (-0.67, fdr 7e-06), [[TMEM265]] (-0.66, fdr 1e-05), [[BRD2]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 020]] (Cap-dependent Translation Initiation).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[PIK3CA]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 24 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 816.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **4.02×** | +19.1 | 0e+00 | 47/49 (SW480, HEC-1-A, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.76×** | +13.9 | 1e-41 | 41/48 (SW480, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.65×** | +13.1 | 9e-37 | 42/48 (SW480, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **1.66×** | +12.8 | 4e-35 | 34/43 (LoVo, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **1.59×** | +12.2 | 4e-32 | 43/47 (SW480, HOP62, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.36×** | +11.5 | 2e-28 | 36/48 (A549, PANC-1, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **1.52×** | +10.1 | 5e-22 | 32/45 (A-427, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.46×** | +9.8 | 6e-21 | 39/48 (SW480, HOP62, …) | all doses, stronger at high dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.03×** | +9.7 | 2e-20 | 29/36 (NCI-H2030, HOP62, …) | rises with dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change | **1.44×** | +9.5 | 1e-19 | 33/49 (NCI-H1792, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.44×** | +9.4 | 2e-19 | 37/48 (SW480, HOP62, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.42×** | +9.2 | 1e-18 | 33/48 (MIA PaCa-2, SHP-77, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.37×** | +8.3 | 4e-15 | 32/48 (AsPC-1, CFPAC-1, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~42% of this change | **1.35×** | +7.5 | 2e-12 | 30/47 (A-172, SW480, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.31×** | +7.1 | 4e-11 | 32/48 (PANC-1, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.21×** | +5.0 | 2e-05 | 21/48 (CFPAC-1, HCT15, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | 1.13× | +3.2 | 0.031 | 8/48 (NCI-H2030, AsPC-1, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.5 µM |  | 1.18× | +3.1 | 0.031 | 7/48 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.26×** | +3.1 | 0.031 | 8/48 (MIA PaCa-2, NCI-H2030, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Phenytoin (sodium) (drug)]] 0.05 µM |  | 1.14× | +3.1 | 0.034 | 5/47 (NCI-H2347, SW480, …) | inconsistent across doses | position effect removed |
| [[NG25 (drug)]] 0.05 µM |  | 1.13× | +3.1 | 0.038 | 10/48 (HCT15, NCI-H23, …) | inconsistent across doses | position effect removed |
| [[vincristine (drug)]] 0.05 µM |  | 1.13× | +3.0 | 0.051 | 9/48 (AsPC-1, MIA PaCa-2, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 816.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 2 lines (SK-MEL-2 0.552×, A-427 0.583×; ⚠ cell-cycle shift, would explain all of this change); [[Citalopram (hydrobromide) (drug)]] 0.05 µM in 1 line (NCI-H596 0.427×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (C-33 A 0.346×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change); [[Dorzolamide (hydrochloride) (drug)]] 0.05 µM in 1 line (SW 1271 0.0694×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | 0.841× | -4.6 | 0.002 | 21/48 (COLO 205, SW480, …) | two highest doses | position effect removed |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~61% of this change | 0.857× | -4.1 | 0.011 | 12/48 (CHP-212, CFPAC-1, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.901× | -3.9 | 0.015 | 15/48 (KATO III, SW 1271, …) | two highest doses | position effect removed |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.907× | -3.6 | 0.046 | 4/48 (SW 1271, HT-29, …) | all doses, flat |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | 0.878× | -3.5 | 0.046 | 6/48 (NCI-H1573, NCI-H460, …) | two highest doses |  |
| [[Alpelisib (drug)]] 5 µM |  | **0.779×** | -3.4 | 0.046 | 14/47 (KATO III, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **0.779×** | -3.4 | 0.046 | 7/49 (H4, HEC-1-A, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 0.900× | -3.2 | 0.092 | 7/48 (NCI-H23, A-427, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~82% of this change | 0.902× | -3.1 | 0.11 | 9/49 (SW480, HEC-1-A, …) | rises with dose | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | 0.886× | -3.1 | 0.11 | 8/47 (A-427, SNU-423, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.892× | -3.0 | 0.11 | 13/48 (NCI-H460, A-172, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.913× | -3.0 | 0.11 | 3/48 (MIA PaCa-2, HOP62, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 816. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 50.1 | 6 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.79× (z +12.0) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.21× (z +8.8) | — |
| [[LoVo (line)]] | wt | 51.5 | 6 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.03× (z +13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 6.85× (z +12.3) | — |
| [[PANC-1 (line)]] | alt | 49.4 | 6 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.34× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.48× (z +10.6) | — |
| [[SW480 (line)]] | alt | 77.0 | 6 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.63× (z +16.1) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.56× (z +13.3) | — |
| [[LS 180 (line)]] | wt | 60.1 | 4 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.58× (z +10.9) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 6.05× (z +10.8) | — |
| [[HEC-1-A (line)]] | alt | 89.6 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 5.13× (z +12.7) | — |
| [[A-427 (line)]] | wt | 69.2 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.418× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 58.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.12× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 81.1 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 5.82× (z +10.7) | — |
| [[NCI-H1792 (line)]] | alt | 39.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.10× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change | — |
| [[RKO (line)]] | wt | 78.1 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 5.41× (z +9.8) | — |
| [[A-172 (line)]] | wt | 66.6 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.42× (z +9.7) | — |
| [[A549 (line)]] | wt | 44.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.27× (z +11.1) | — |
| [[C-33 A (line)]] | alt | 97.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.346× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change |
| [[Hs 766T (line)]] | wt | 37.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.41× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[HT-29 (line)]] | alt | 38.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.84× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[LOX-IMVI (line)]] | wt | 37.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.92× (z +8.5) | — |
| [[NCI-H1573 (line)]] | alt | 30.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.75× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[NCI-H460 (line)]] | wt | 46.8 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 3.71× (z +8.8) | — |
| [[NCI-H596 (line)]] | alt | 54.5 | 0 | 1 | — | [[Citalopram (hydrobromide) (drug)]] 0.05 µM 0.427× (z -12.6) |
| [[Panc 03.27 (line)]] | alt | 54.4 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.06× (z +10.1) | — |
| [[SK-MEL-2 (line)]] | alt | 73.3 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.552× (z -9.6) ⚠ cell-cycle shift, would explain all of this change |
| [[SNU-423 (line)]] | alt | 51.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +10.8) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SW 1271 (line)]] | alt | 73.3 | 0 | 1 | — | [[Dorzolamide (hydrochloride) (drug)]] 0.05 µM 0.0694× (z -10.9) |
| [[SW48 (line)]] | wt | 78.6 | 1 | 0 | [[TAK-901 (drug)]] 0.05 µM 3.29× (z +9.2) | — |
| [[AN3 CA (line)]] | alt | 82.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 55.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 61.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 73.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 60.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 82.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 52.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 65.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 47.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 59.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 61.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 49.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 65.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 53.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 61.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 42.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 84.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 67.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 46.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 65.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 816), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM248]] | +0.70 | +0.69 / +0.65 | both halves | 7e-06 |  |
| [[SMPD4]] | +0.69 | +0.65 / +0.71 | both halves | 7e-06 |  |
| [[CHID1]] | +0.68 | +0.59 / +0.68 | both halves | 7e-06 |  |
| [[SENP3]] | +0.67 | +0.66 / +0.71 | both halves | 7e-06 |  |
| [[HACD3]] | +0.66 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[GMPS]] | +0.64 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[BPNT2]] | +0.63 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[RNF4]] | +0.63 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[TOMM40]] | +0.63 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[XPO7]] | +0.63 | +0.69 / +0.62 | both halves | 7e-06 |  |
| [[RPA1]] | +0.62 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[DNAAF5]] | +0.62 | +0.58 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATF4]] | -0.67 | -0.68 / -0.65 | both halves | 7e-06 |  |
| [[TMEM265]] | -0.66 | -0.53 / -0.67 | both halves | 1e-05 |  |
| [[BRD2]] | -0.61 | -0.55 / -0.60 | both halves | 1e-05 |  |
| [[TUBB2A]] | -0.61 | -0.53 / -0.65 | both halves | 1e-05 |  |
| [[COMMD3]] | -0.61 | -0.47 / -0.67 | both halves | 2e-05 |  |
| [[CHMP2B]] | -0.60 | -0.54 / -0.60 | both halves | 1e-05 |  |
| [[H3-3B]] | -0.60 | -0.60 / -0.56 | both halves | 1e-05 | STRING 403 |
| [[JUND]] | -0.59 | -0.63 / -0.62 | both halves | 7e-06 |  |
| [[OFD1]] | -0.59 | -0.61 / -0.56 | both halves | 1e-05 |  |
| [[BTG1]] | -0.59 | -0.47 / -0.64 | both halves | 2e-05 |  |
| [[ZNF674]] | -0.58 | -0.63 / -0.53 | both halves | 1e-05 |  |
| [[USP53]] | -0.57 | -0.54 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PIK3CA]] | B | PIK3CA activity raises ELAVL1's level | compounds that target PIK3CA: 2 of 4 lower it (Alpelisib, Bimiralisib) | 50% of the class's compounds vs 0.6% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds |
| [[RNF223]] | B | RNF223 activity lowers ELAVL1's level | lines that do not express RNF223 (28) vs lines expressing it (22) | 1.19× higher at baseline in the lines without RNF223 | 0.062 | ⚠ within organs, on part of the lines; also absent: CDH1, IRF6, MPZL2 |
| [[WNK2]] | B | WNK2 activity raises ELAVL1's level | lines that do not express WNK2 (16) vs lines expressing it (34) | 1.23× lower at baseline in the lines without WNK2 | 0.075 | ⚠ within organs, on part of the lines; also absent: NUP210, SLC27A2, CHDH |
| [[MXRA7]] | B | MXRA7 activity raises ELAVL1's level | lines that do not express MXRA7 (6) vs lines expressing it (44) | 1.13× lower at baseline in the lines without MXRA7 | 0.089 | ⚠ within organs, on part of the lines; also absent: FKBP7, KIF3C, SNTA1; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **+** arm (projection on the module's main direction 0.601). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-18.6, -29.3); signed map (-24.8, -45.5). **Vector** length 87.3, 20.8% of its response variance represented; |z| ≥ 3 in 1,109 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +6.8 | +19.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | +6.6 | +12.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change | +6.2 | +9.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +6.1 | +13.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | +5.6 | +10.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.2 | +9.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.1 | +2.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.0 | +2.5 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.9 | +2.5 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.8 | -2.7 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.1 | -0.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.5 | -0.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -3.7 | +2.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.5 | -0.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.4 | -3.9 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -1.9 | -2.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.8 | -1.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.6 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | ELAV like RNA binding protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.2 — chr19:7,958,573-8,005,659 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HuR, Hua, MelG; previously HUR |
| Gene groups (HGNC) | RNA binding motif containing; ELAV like RNA binding protein family |
| Reactome | 6 pathways, smallest: HuR (ELAVL1) binds and stabilizes mRNA; Regulation of mRNA stability by proteins that bind AU-rich elements; Dengue Virus-Host Interactions |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15717](https://www.uniprot.org/uniprotkb/Q15717) (ELAV-like protein 1):

> RNA-binding protein that binds to the 3'-UTR region of mRNAs and increases their stability. Involved in embryonic stem cell (ESC) differentiation: preferentially binds mRNAs that are not methylated by N6-methyladenosine (m6A), stabilizing them, promoting ESC differentiation (By similarity). Has also been shown to be capable of binding to m6A-containing mRNAs and contributes to MYC stability by binding to m6A-containing MYC mRNAs. Binds to poly-U elements and AU-rich elements (AREs) in the …

**Summary**, from NCBI Gene [1994](https://www.ncbi.nlm.nih.gov/gene/1994):

> The protein encoded by this gene is a member of the ELAVL family of RNA-binding proteins that contain several RNA recognition motifs, and selectively bind AU-rich elements (AREs) found in the 3' untranslated regions of mRNAs. AREs signal degradation of mRNAs as a means to regulate gene expression, thus by binding AREs, the ELAVL family of proteins play a role in stabilizing ARE-containing mRNAs. This gene has been implicated in a variety of biological processes and has been linked to a number …

**Accessions** — [HGNC:3312](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3312) · Entrez [1994](https://www.ncbi.nlm.nih.gov/gene/1994) · UniProt [Q15717](https://www.uniprot.org/uniprotkb/Q15717) · Ensembl [ENSG00000066044](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000066044)

## Data

Gene col 816: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 816); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 816, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 816]; `tensor/DDL_lfc|DDL_z.npy` [816]; `embed/gene_vectors.npy` [816]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 816 or target_col == 816). Every well: [[ELAVL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ELAVL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
