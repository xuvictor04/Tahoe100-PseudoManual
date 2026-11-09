---
symbol: "PRKD3"
type: "gene"
col: 3723
ensembl_id: "ENSG00000115825"
name: "protein kinase D3"
location: "2p22.2"
module: 79
arm: "+"
pooled_cpm: 123.35
n_lines_expressing: 49
n_dd_up: 5
n_dd_down: 12
n_dd_up_clean: 3
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/079"]
generated_by: "tahoemap"
---

# PRKD3

*protein kinase D3* — 2p22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.25× (z +5.5, q 2e-05, up in 25 of 47 measured lines) ⚠ cell-cycle shift, explains ~9% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 0.5 µM: 1.21× (z +4.9, q 2e-04, up in 20 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.596× (z -12.0, q 1e-30, down in 34 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.768× (z -9.4, q 8e-19, down in 29 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PPP4R4]] (+0.62, fdr 3e-05), [[RNF24]] (+0.57, fdr 2e-05), [[IGFBP2]] (+0.56, fdr 3e-05); moves opposite to [[PCBD2]] (-0.53, fdr 4e-05), [[ARMCX4]] (-0.52, fdr 9e-05), [[LTO1]] (-0.51, fdr 2e-04).
> It is in [[Module 079]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PIP4P2]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3723.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | **1.25×** | +5.5 | 2e-05 | 25/47 (SW480, HOP62, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~11% of this change | **1.23×** | +5.1 | 8e-05 | 21/47 (SW480, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.21×** | +4.9 | 2e-04 | 20/48 (NCI-H2347, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.45×** | +4.8 | 2e-04 | 25/48 (HS-578T, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.23×** | +3.7 | 0.029 | 15/47 (A498, SW1417, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.10× | +3.3 | 0.086 | 16/47 (NCI-H2347, CFPAC-1, …) | all doses, flat |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | 1.14× | +3.1 | 0.15 | 5/48 (PANC-1, NCI-H1573, …) | top dose only | plate-row cell shift |
| [[Tucidinostat (drug)]] 0.05 µM |  | 1.13× | +3.0 | 0.15 | 6/47 (NCI-H2030, NCI-H2347, …) | all doses, flat |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.13× | +3.0 | 0.15 | 15/47 (C32, SHP-77, …) | inconsistent across doses |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | 1.13× | +3.0 | 0.15 | 6/48 (LoVo, LOX-IMVI, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 12 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3723.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.596×** | -12.0 | 1e-30 | 34/44 (LoVo, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.666×** | -10.2 | 4e-22 | 38/48 (NCI-H1792, hTERT-HPNE, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.768×** | -9.4 | 8e-19 | 29/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.702×** | -8.6 | 1e-15 | 30/42 (HepG2/C3A, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.734×** | -7.8 | 7e-13 | 28/47 (SW480, A-172, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.776×** | -6.4 | 1e-08 | 27/46 (NCI-H1573, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | 0.846× | -6.0 | 2e-07 | 20/47 (SW480, NCI-H1792, …) | inconsistent across doses | low cells (technical?) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.786×** | -5.8 | 4e-07 | 25/47 (LS 180, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.810×** | -5.1 | 2e-05 | 25/46 (HepG2/C3A, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.817×** | -5.1 | 2e-05 | 25/47 (NCI-H460, SW480, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.811×** | -5.1 | 2e-05 | 28/47 (NCI-H23, NCI-H1573, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.821×** | -5.0 | 3e-05 | 23/47 (SW480, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.823×** | -4.9 | 4e-05 | 26/47 (NCI-H460, hTERT-HPNE, …) | all doses, flat |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.949× | -4.9 | 4e-05 | 1/49 (MIA PaCa-2) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.834× | -4.4 | 4e-04 | 21/49 (LS 180, SW480, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.891× | -4.1 | 0.001 | 16/47 (A-172, NCI-H460, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | 0.881× | -3.2 | 0.035 | 17/47 (SNU-423, NCI-H460, …) | top dose only |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | 0.838× | -3.2 | 0.035 | 15/47 (Hs 766T, RPMI-7951, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.884× | -3.1 | 0.043 | 13/47 (LS 180, NCI-H1573, …) | two highest doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.909× | -2.9 | 0.089 | 7/47 (LS 180, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3723. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 161 | 2 (2 ⚠) | 4 | [[Digitoxin (drug)]] 5 µM 1.73× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~11% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.586× (z -14.3) |
| [[NCI-H1792 (line)]] | alt | 166 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.451× (z -14.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.495× (z -8.9) |
| [[NCI-H460 (line)]] | wt | 374 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.252× (z -17.5) |
| [[SNU-423 (line)]] | alt | 147 | 0 | 5 (3 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.439× (z -9.7) |
| [[LOX-IMVI (line)]] | wt | 169 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.383× (z -13.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.591× (z -11.1) |
| [[LS 180 (line)]] | wt | 91.2 | 0 | 4 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.372× (z -12.0) |
| [[A-172 (line)]] | wt | 197 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.506× (z -9.4) |
| [[HepG2_C3A (line)]] | wt | 95.5 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +13.7) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.136× (z -18.8) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 145 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.490× (z -10.7) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 124 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.457× (z -9.5) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 103 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.77× (z +9.9) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.361× (z -12.1) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 108 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.388× (z -8.9) |
| [[HEC-1-A (line)]] | alt | 85.5 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.533× (z -12.4) |
| [[hTERT-HPNE (line)]] | wt | 159 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.227× (z -14.9) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 84.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.303× (z -17.2) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 88.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.333× (z -17.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.337× (z -12.4) |
| [[NCI-H23 (line)]] | alt | 116 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.288× (z -23.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.540× (z -11.5) |
| [[A-427 (line)]] | wt | 128 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.301× (z -16.4) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 152 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.245× (z -16.4) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 112 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.514× (z -11.0) |
| [[CFPAC-1 (line)]] | alt | 103 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.416× (z -10.9) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 105 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.510× (z -10.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 145 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.528× (z -8.8) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 120 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.19× (z +10.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 102 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.387× (z -14.0) |
| [[NCI-H2347 (line)]] | alt | 83.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.402× (z -11.9) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 103 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.381× (z -11.6) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 100 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.632× (z -9.7) |
| [[SW 900 (line)]] | alt | 132 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.336× (z -10.7) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 43.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 75.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 97.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 84.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 95.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 10.3 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 71.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 62.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 70.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 161 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 92.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 54.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 168 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 96.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 77.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 56.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3723), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP4R4]] | +0.62 | +0.45 / +0.59 | both halves | 3e-05 |  |
| [[RNF24]] | +0.57 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[IGFBP2]] | +0.56 | +0.49 / +0.46 | both halves | 3e-05 |  |
| [[SFXN1]] | +0.55 | +0.58 / +0.47 | both halves | 2e-05 |  |
| [[RADX]] | +0.55 | +0.53 / +0.43 | both halves | 3e-05 |  |
| [[RFX2]] | +0.55 | +0.57 / +0.42 | both halves | 4e-05 |  |
| [[PDK3]] | +0.54 | +0.59 / +0.41 | both halves | 4e-05 |  |
| [[CHEK2]] | +0.53 | +0.39 / +0.54 | both halves | 5e-05 |  |
| [[IFNAR2]] | +0.53 | +0.42 / +0.51 | both halves | 4e-05 |  |
| [[TNFRSF1B]] | +0.52 | +0.29 / +0.52 | both halves | 2e-04 |  |
| [[ASRGL1]] | +0.52 | +0.25 / +0.43 | both halves | 4e-04 |  |
| [[PIP4P2]] | +0.52 | +0.41 / +0.45 | both halves | 4e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PCBD2]] | -0.53 | -0.49 / -0.42 | both halves | 4e-05 |  |
| [[ARMCX4]] | -0.52 | -0.50 / -0.36 | both halves | 9e-05 |  |
| [[LTO1]] | -0.51 | -0.57 / -0.30 | both halves | 2e-04 |  |
| [[PPP3CB-AS1]] | -0.51 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[DNAJB12]] | -0.51 | -0.59 / -0.36 | both halves | 1e-04 |  |
| [[CHMP3]] | -0.50 | -0.49 / -0.37 | both halves | 8e-05 |  |
| [[SNAPC5]] | -0.50 | -0.58 / -0.25 | both halves | 4e-04 |  |
| [[ACYP2]] | -0.50 | -0.53 / -0.37 | both halves | 8e-05 |  |
| [[LINC00571]] | -0.50 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[SMIM15-AS1]] | -0.50 | -0.55 / -0.29 | both halves | 2e-04 |  |
| [[WDR74]] | -0.49 | -0.49 / -0.32 | both halves | 2e-04 |  |
| [[EIF5]] | -0.49 | -0.54 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PIP4P2]] | C | PIP4P2 activity raises PRKD3's level | lines that do not express PIP4P2 (4) vs lines expressing it (46) | 2.15× lower at baseline in the lines without PIP4P2 | 0.052 | ⚠ few lines (4 vs 46); across organs; also absent: THEM4, MRPS30-DT; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 079]] — hypoxia; 57 genes; every member is in the + arm (projection on the module's main direction 0.463). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.3, -10.5); signed map (-33.6, 20.9). **Vector** length 101, 24.6% of its response variance represented; |z| ≥ 3 in 1,061 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.7 | +3.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.2 | +4.9 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +6.4 | +1.2 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.8 | +1.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.5 | +2.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +3.0 | +3.0 |
|  | [[Brivudine (drug)]] 0.5 µM |  | +2.1 | +1.2 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | +1.8 | +1.7 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.0 | -6.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.7 | -4.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.0 | -5.1 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.2 | -2.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -3.2 | -12.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.1 | -5.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.9 | -3.1 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.7 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | protein kinase D3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p22.2 — chr2:37,250,502-37,324,833 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PKD3, EPK2; previously PRKCN |
| Gene groups (HGNC) | Pleckstrin homology domain containing; Protein kinase D family |
| Reactome | 3 pathways, smallest: Sphingolipid de novo biosynthesis; Sphingolipid metabolism; Metabolism of lipids |
| Matched by | ensembl_id |

**Function**, from UniProt [O94806](https://www.uniprot.org/uniprotkb/O94806) (Serine/threonine-protein kinase D3):

> Converts transient diacylglycerol (DAG) signals into prolonged physiological effects, downstream of PKC. Involved in resistance to oxidative stress (By similarity).

**Summary**, from NCBI Gene [23683](https://www.ncbi.nlm.nih.gov/gene/23683):

> This gene belongs to the multigene protein kinase D family of serine/threonine kinases, which bind diacylglycerol and phorbol esters. Members of this family are characterized by an N-terminal regulatory domain comprised of a tandem repeat of cysteine-rich zinc-finger motifs and a pleckstrin domain. The C-terminal region contains the catalytic domain and is distantly related to calcium-regulated kinases. Catalytic activity of this enzyme promotes its nuclear localization. This protein has been …

**Accessions** — [HGNC:9408](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9408) · Entrez [23683](https://www.ncbi.nlm.nih.gov/gene/23683) · UniProt [O94806](https://www.uniprot.org/uniprotkb/O94806) · Ensembl [ENSG00000115825](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115825)

## Data

Gene col 3723: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3723); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3723, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3723]; `tensor/DDL_lfc|DDL_z.npy` [3723]; `embed/gene_vectors.npy` [3723]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3723 or target_col == 3723). Every well: [[PRKD3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRKD3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
