---
symbol: "KIFBP"
type: "gene"
col: 12755
ensembl_id: "ENSG00000198954"
name: "kinesin family binding protein"
location: "10q22.1"
module: 11
arm: "+"
pooled_cpm: 32.67
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 9
n_dd_up_clean: 10
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# KIFBP

*kinesin family binding protein* — 10q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (7 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 1.70× (z +11.0, q 2e-25, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.657× (z -8.7, q 2e-15, down in 27 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.699× (z -7.4, q 3e-11, down in 25 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRM2]] (+0.66, fdr 7e-06), [[CCDC137]] (+0.64, fdr 7e-06), [[NME6]] (+0.64, fdr 7e-06); moves opposite to [[CTSD]] (-0.53, fdr 2e-05), [[GAA]] (-0.50, fdr 3e-05), [[ANKRD10]] (-0.49, fdr 1e-05).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CTSD]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 11 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12755.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **1.70×** | +11.0 | 2e-25 | 39/48 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.38×** | +9.4 | 1e-18 | 32/47 (AsPC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.56×** | +9.3 | 4e-18 | 33/48 (CFPAC-1, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.52×** | +8.3 | 1e-14 | 33/45 (SW480, HT-29, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.39×** | +6.9 | 8e-10 | 29/48 (HEC-1-A, PANC-1, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.37×** | +6.3 | 2e-08 | 24/48 (CFPAC-1, A498, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.27×** | +5.0 | 4e-05 | 23/48 (SW480, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +4.8 | 9e-05 | 20/48 (J82, HEC-1-A, …) | top dose only | low cells (technical?) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | 1.18× | +4.8 | 1e-04 | 22/48 (SW480, CFPAC-1, …) | all doses, flat | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.25×** | +4.6 | 2e-04 | 19/48 (MIA PaCa-2, AsPC-1, …) | rises with dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | 1.16× | +4.4 | 6e-04 | 11/48 (PANC-1, LS 180, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.23×** | +4.3 | 9e-04 | 15/48 (SW480, AsPC-1, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.48×** | +4.2 | 9e-04 | 15/48 (SW480, BT-474, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.22×** | +4.2 | 0.001 | 19/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.24×** | +4.1 | 0.001 | 17/47 (C-33 A, MIA PaCa-2, …) | all doses, stronger at high dose | low cells (technical?) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.21×** | +3.6 | 0.011 | 17/47 (NCI-H2347, LoVo, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 5 µM |  | 1.19× | +3.4 | 0.020 | 15/47 (SW480, SW1417, …) | all doses, stronger at high dose |  |
| [[Filgotinib (drug)]] 5 µM |  | 1.17× | +3.3 | 0.024 | 8/48 (LoVo, SW480, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 1.17× | +3.3 | 0.028 | 10/47 (SW48, H4, …) | all doses, stronger at high dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.35×** | +3.2 | 0.029 | 10/48 (RKO, NCI-H2030, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[vincristine (drug)]] 0.5 µM |  | **1.23×** | +3.0 | 0.055 | 8/48 (HT-29, HEC-1-A, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | 1.16× | +3.0 | 0.055 | 20/48 (MIA PaCa-2, SK-MEL-2, …) | top dose only |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.15× | +3.0 | 0.064 | 7/48 (HEC-1-A, CFPAC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 7 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12755.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.657×** | -8.7 | 2e-15 | 27/47 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.699×** | -7.4 | 3e-11 | 25/48 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.747×** | -6.0 | 3e-07 | 23/42 (C32, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.765×** | -5.6 | 4e-06 | 22/48 (MIA PaCa-2, PANC-1, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.820×** | -3.9 | 0.009 | 16/37 (A549, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.828×** | -3.9 | 0.009 | 19/48 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.829×** | -3.7 | 0.015 | 18/47 (SW48, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.837× | -3.7 | 0.015 | 18/48 (NCI-H460, NCI-H1573, …) | rises with dose |  |
| [[Thymol (drug)]] 0.5 µM |  | 0.837× | -3.7 | 0.015 | 17/46 (MIA PaCa-2, SW480, …) | inconsistent across doses |  |
| [[Almonertinib (mesylate) (drug)]] 0.5 µM |  | 0.842× | -3.6 | 0.019 | 7/48 (NCI-H2347, SNU-423, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.831×** | -3.6 | 0.019 | 18/41 (NCI-H2030, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.799×** | -3.3 | 0.043 | 11/46 (BT-474, HOP62, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.848× | -3.3 | 0.044 | 17/48 (SW 1088, AN3 CA, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.896× | -3.2 | 0.053 | 10/48 (HOP62, A-172, …) | rises with dose |  |
| [[Fusidic acid (drug)]] 5 µM |  | 0.901× | -3.1 | 0.083 | 4/48 (Hs 766T, SW 1088, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12755. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 26.2 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.166× (z -18.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.281× (z -12.8) |
| [[A-172 (line)]] | wt | 75.0 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.409× (z -16.4) ⚠ cell-cycle shift, explains ~61% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.560× (z -10.6) |
| [[HOP62 (line)]] | alt | 60.9 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.344× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.474× (z -8.7) |
| [[SW480 (line)]] | alt | 29.6 | 3 (3 ⚠) | 1 (1 ⚠) | [[Topotecan (hydrochloride) (drug)]] 5 µM 2.57× (z +10.7) ⚠ toxic | [[Dinaciclib (drug)]] 0.05 µM 0.430× (z -9.2) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 23.7 | 3 (2 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 3.61× (z +9.5) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.35× (z +9.3) | — |
| [[A498 (line)]] | wt | 46.5 | 2 (1 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 2.41× (z +10.1) | — |
| [[HEC-1-A (line)]] | alt | 45.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.308× (z -12.4) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 24.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.304× (z -9.5) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 45.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.150× (z -15.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.383× (z -8.5) |
| [[A-427 (line)]] | wt | 37.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.284× (z -11.1) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 37.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.123× (z -18.0) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 60.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.169× (z -8.9) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 17.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.71× (z +11.8) | — |
| [[C-33 A (line)]] | alt | 38.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.246× (z -9.3) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 29.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0669× (z -19.8) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 21.9 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.111× (z -10.6) |
| [[HepG2_C3A (line)]] | wt | 28.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.142× (z -10.7) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 24.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.206× (z -12.7) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 34.2 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.94× (z +9.2) | — |
| [[NCI-H23 (line)]] | alt | 26.9 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.290× (z -9.1) |
| [[SW48 (line)]] | wt | 42.6 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.167× (z -10.8) |
| [[BT-474 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 26.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 31.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 27.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 25.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 24.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 43.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 29.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12755), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRM2]] | +0.66 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[CCDC137]] | +0.64 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[NME6]] | +0.64 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[RBAK]] | +0.63 | +0.67 / +0.54 | both halves | 1e-05 |  |
| [[PHAX]] | +0.63 | +0.67 / +0.55 | both halves | 1e-05 |  |
| [[THUMPD1]] | +0.61 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[TACO1]] | +0.61 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[FBXO45]] | +0.60 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[AGGF1]] | +0.60 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[ZBTB6]] | +0.59 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[C10orf88]] | +0.59 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[UBL4A]] | +0.59 | +0.50 / +0.63 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CTSD]] | -0.53 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[GAA]] | -0.50 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[ANKRD10]] | -0.49 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[PSAP]] | -0.49 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[EIF2S3]] | -0.49 | -0.40 / -0.59 | both halves | 5e-05 |  |
| [[LAPTM4B]] | -0.49 | -0.46 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CTSD]] | C | CTSD activity raises KIFBP's level | lines that do not express CTSD (4) vs lines expressing it (46) | 1.29× lower at baseline in the lines without CTSD | 0.079 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: IFITM10, SQOR, ST6GALNAC2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.596). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-39.7, 2.3); signed map (-0.9, -21.7). **Vector** length 100, 22.2% of its response variance represented; |z| ≥ 3 in 899 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +6.4 | +11.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +6.2 | +8.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.7 | +6.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.5 | +9.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +4.3 | +5.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.0 | +4.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.6 | +3.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.2 | +3.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.1 | +4.1 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.0 | -8.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -5.3 | -6.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -4.9 | -7.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.3 | -3.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.1 | -3.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.0 | -3.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.3 | -3.3 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.6 | -2.4 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -1.6 | -1.9 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | -1.5 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | kinesin family binding protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q22.1 — chr10:68,988,803-69,043,544 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP586B0923, TTC20, KBP; previously KIAA1279, KIF1BP |
| Gene groups (HGNC) | Tetratricopeptide repeat domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96EK5](https://www.uniprot.org/uniprotkb/Q96EK5) (KIF-binding protein):

> Activator of KIF1B plus-end-directed microtubule motor activity. Required for organization of axonal microtubules, and axonal outgrowth and maintenance during peripheral and central nervous system development.

**Summary**, from NCBI Gene [26128](https://www.ncbi.nlm.nih.gov/gene/26128):

> This gene encodes a kinesin family member 1 binding protein that is characterized by two tetratrico peptide repeats. The encoded protein localizes to the mitochondria and may be involved in regulating transport of the mitochondria. Mutations in this gene are associated with Goldberg-Shprintzen megacolon syndrome. [provided by RefSeq, Mar 2010]

**Accessions** — [HGNC:23419](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23419) · Entrez [26128](https://www.ncbi.nlm.nih.gov/gene/26128) · UniProt [Q96EK5](https://www.uniprot.org/uniprotkb/Q96EK5) · Ensembl [ENSG00000198954](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198954)

## Data

Gene col 12755: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12755); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12755, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12755]; `tensor/DDL_lfc|DDL_z.npy` [12755]; `embed/gene_vectors.npy` [12755]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12755 or target_col == 12755). Every well: [[KIFBP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KIFBP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
