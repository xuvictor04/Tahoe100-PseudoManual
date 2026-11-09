---
symbol: "FUBP3"
type: "gene"
col: 2830
ensembl_id: "ENSG00000107164"
name: "far upstream element binding protein 3"
location: "9q34.11-q34.12"
module: 52
arm: "+"
pooled_cpm: 139.12
n_lines_expressing: 49
n_dd_up: 23
n_dd_down: 1
n_dd_up_clean: 17
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/052"]
generated_by: "tahoemap"
---

# FUBP3

*far upstream element binding protein 3* — 9q34.11-q34.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (6 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.86× (z +13.2, q 4e-37, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Ponatinib (drug)]] 5 µM: 0.834× (z -4.4, q 0.005, down in 21 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (RKO 0.423×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.460×; ⚠ toxic; cell-cycle shift, would explain all of this change); [[Pentoxifylline (drug)]] 0.05 µM in 1 line (NCI-H596 0.277×; ⚠ transcription drop).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NDUFA10]] (+0.67, fdr 7e-06), [[GAK]] (+0.67, fdr 7e-06), [[RER1]] (+0.67, fdr 1e-05); moves opposite to [[ZBTB10]] (-0.60, fdr 1e-05), [[BTN2A2]] (-0.58, fdr 1e-05), [[TRMT1L]] (-0.57, fdr 1e-05).
> It sits in the **+** arm of [[Module 052]].
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[NUP214]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 14 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2830.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.86×** | +13.2 | 4e-37 | 44/48 (Hs 766T, COLO 205, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.57×** | +11.9 | 3e-30 | 42/47 (PANC-1, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.61×** | +11.4 | 5e-28 | 44/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.49×** | +9.6 | 1e-19 | 41/47 (MIA PaCa-2, SW480, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.43×** | +8.5 | 2e-15 | 43/47 (PANC-1, Hs 766T, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.39×** | +8.0 | 2e-13 | 36/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.86×** | +7.8 | 4e-13 | 29/37 (NCI-H1573, HS-578T, …) | rises with dose | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.38×** | +7.8 | 5e-13 | 32/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.36×** | +7.4 | 1e-11 | 38/47 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.36×** | +7.3 | 2e-11 | 38/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.34×** | +6.6 | 2e-09 | 38/47 (SW480, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.66×** | +6.3 | 1e-08 | 38/44 (HCT15, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~3% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.27×** | +5.6 | 7e-07 | 28/47 (SW480, SNU-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.26×** | +5.5 | 2e-06 | 28/47 (SW480, HEC-1-A, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +5.0 | 2e-05 | 16/47 (NCI-H460, PANC-1, …) | rises with dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.49×** | +5.0 | 2e-05 | 29/47 (Hs 766T, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.33×** | +4.9 | 3e-05 | 31/48 (PANC-1, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.26×** | +3.9 | 0.002 | 25/47 (NCI-H460, PANC-1, …) | two highest doses | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.22×** | +3.4 | 0.014 | 19/47 (NCI-H460, Hs 766T, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 1.15× | +3.4 | 0.015 | 6/46 (NCI-H2030, LoVo, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **1.31×** | +3.3 | 0.018 | 17/47 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.30×** | +3.3 | 0.018 | 18/47 (NCI-H460, Hs 766T, …) | two highest doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2830.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (RKO 0.423×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.460×; ⚠ toxic; cell-cycle shift, would explain all of this change); [[Pentoxifylline (drug)]] 0.05 µM in 1 line (NCI-H596 0.277×; ⚠ transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | 0.834× | -4.4 | 0.005 | 21/47 (J82, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~1% of this change | 0.862× | -3.6 | 0.059 | 17/47 (SW1417, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.814×** | -3.6 | 0.059 | 24/47 (A498, HT-29, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 0.879× | -3.5 | 0.059 | 10/47 (AsPC-1, RKO, …) | two highest doses | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | 0.862× | -3.5 | 0.059 | 15/48 (SW 1271, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 0.866× | -3.4 | 0.059 | 15/47 (LOX-IMVI, HOP62, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.871× | -3.4 | 0.059 | 11/47 (NCI-H1792, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | 0.868× | -3.3 | 0.066 | 13/46 (AN3 CA, AsPC-1, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.879× | -3.2 | 0.098 | 9/46 (A549, SNU-423, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2830. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 89.9 | 9 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.44× (z +15.5) | — |
| [[SW480 (line)]] | alt | 169 | 9 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.47× (z +15.9) | — |
| [[NCI-H460 (line)]] | wt | 155 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +12.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.11× (z +11.0) | — |
| [[Hs 766T (line)]] | wt | 141 | 5 (2 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 6.09× (z +11.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 171 | 5 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 2.29× (z +11.1) | — |
| [[NCI-H1573 (line)]] | alt | 101 | 4 (2 ⚠) | 0 | [[Lonafarnib (drug)]] 5 µM 6.02× (z +11.1) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.30× (z +9.9) | — |
| [[HEC-1-A (line)]] | alt | 165 | 3 | 0 | [[TAK-901 (drug)]] 0.05 µM 2.05× (z +10.6) | — |
| [[HS-578T (line)]] | alt | 96.0 | 3 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 4.25× (z +9.7) | — |
| [[NCI-H23 (line)]] | alt | 131 | 3 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 3.25× (z +8.8) | — |
| [[BT-474 (line)]] | alt | 189 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 3.16× (z +8.7) | — |
| [[LOX-IMVI (line)]] | wt | 162 | 2 | 0 | [[TAK-901 (drug)]] 0.05 µM 2.47× (z +12.4) | — |
| [[RKO (line)]] | wt | 380 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.423× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 179 | 1 | 0 | [[Auranofin (drug)]] 5 µM 1.78× (z +8.7) | — |
| [[AN3 CA (line)]] | alt | 135 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.63× (z +10.0) | — |
| [[C-33 A (line)]] | alt | 140 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.436× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 67.4 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.390× (z -8.5) ⚠ toxic |
| [[COLO 205 (line)]] | alt | 157 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 7.80× (z +11.5) | — |
| [[LoVo (line)]] | wt | 163 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 3.44× (z +9.2) | — |
| [[LS 180 (line)]] | wt | 137 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 3.80× (z +8.6) | — |
| [[NCI-H1792 (line)]] | alt | 111 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.91× (z +8.6) | — |
| [[NCI-H596 (line)]] | alt | 140 | 0 | 1 (1 ⚠) | — | [[Pentoxifylline (drug)]] 0.05 µM 0.277× (z -10.6) ⚠ transcription drop |
| [[Panc 03.27 (line)]] | alt | 136 | 1 | 0 | [[Auranofin (drug)]] 5 µM 1.90× (z +8.8) | — |
| [[SHP-77 (line)]] | alt | 196 | 1 | 0 | [[Auranofin (drug)]] 5 µM 1.92× (z +9.6) | — |
| [[A-172 (line)]] | wt | 10.3 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 81.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 145 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 132 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 122 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 161 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 159 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 165 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 89.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 131 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 137 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 144 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 208 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 143 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 87.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 154 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 133 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 148 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 174 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 149 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 156 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2830), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDUFA10]] | +0.67 | +0.58 / +0.70 | both halves | 7e-06 |  |
| [[GAK]] | +0.67 | +0.69 / +0.68 | both halves | 7e-06 |  |
| [[RER1]] | +0.67 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[STX16-NPEPL1]] | +0.67 | +0.56 / +0.69 | both halves | 1e-05 |  |
| [[EARS2]] | +0.66 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[PMM2]] | +0.65 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[PIGG]] | +0.65 | +0.69 / +0.62 | both halves | 7e-06 |  |
| [[VPS53]] | +0.63 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[RAB5C]] | +0.63 | +0.52 / +0.70 | both halves | 1e-05 |  |
| [[NIPA2]] | +0.63 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[MAGOH]] | +0.62 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[SENP5]] | +0.62 | +0.67 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZBTB10]] | -0.60 | -0.56 / -0.60 | both halves | 1e-05 |  |
| [[BTN2A2]] | -0.58 | -0.55 / -0.59 | both halves | 1e-05 |  |
| [[TRMT1L]] | -0.57 | -0.55 / -0.61 | both halves | 1e-05 |  |
| [[LCA5]] | -0.57 | -0.53 / -0.58 | both halves | 1e-05 |  |
| [[MIER1]] | -0.56 | -0.40 / -0.56 | both halves | 5e-05 |  |
| [[PNRC1]] | -0.55 | -0.44 / -0.60 | both halves | 3e-05 |  |
| [[PIM3]] | -0.55 | -0.42 / -0.62 | both halves | 4e-05 | same gene group |
| [[MARCKS]] | -0.55 | -0.42 / -0.54 | both halves | 4e-05 |  |
| [[KMT2A]] | -0.55 | -0.39 / -0.60 | both halves | 6e-05 |  |
| [[ARL4A]] | -0.55 | -0.49 / -0.58 | both halves | 1e-05 |  |
| [[FBXL3]] | -0.55 | -0.28 / -0.64 | both halves | 3e-04 |  |
| [[OSR2]] | -0.54 | -0.52 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NUP214]] | C | FUBP3's natural level strengthens NUP214's drug response | FUBP3's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.66, reverse +0.20; direction not clear | 0.038 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 052]]; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.709). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (10.0, -27.4); signed map (-48.6, 1.9). **Vector** length 95.4, 27.8% of its response variance represented; |z| ≥ 3 in 1,071 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +8.9 | +2.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +8.8 | -0.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +8.4 | +9.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | +6.6 | +3.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.0 | +8.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.8 | +11.9 |
|  | [[EX229 (drug)]] 5 µM |  | +3.7 | +3.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.3 | +5.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.0 | +3.0 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -7.3 | +1.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.6 | +5.0 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.2 | -1.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.6 | +3.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.9 | -0.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.3 | -2.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.3 | -3.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.2 | -3.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.1 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | far upstream element binding protein 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.11-q34.12 — chr9:130,578,965-130,638,352 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously FBP3 |
| Gene groups (HGNC) | MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96I24](https://www.uniprot.org/uniprotkb/Q96I24) (Far upstream element-binding protein 3):

> May interact with single-stranded DNA from the far-upstream element (FUSE). May activate gene expression.

**Summary**, from NCBI Gene [8939](https://www.ncbi.nlm.nih.gov/gene/8939):

> Enables single-stranded DNA binding activity. Involved in DNA-templated transcription; positive regulation of DNA-templated transcription; and positive regulation of gene expression. Acts upstream of or within positive regulation of transcription by RNA polymerase II. Located in cytoplasm and nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:4005](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4005) · Entrez [8939](https://www.ncbi.nlm.nih.gov/gene/8939) · UniProt [Q96I24](https://www.uniprot.org/uniprotkb/Q96I24) · Ensembl [ENSG00000107164](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000107164)

## Data

Gene col 2830: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2830); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2830, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2830]; `tensor/DDL_lfc|DDL_z.npy` [2830]; `embed/gene_vectors.npy` [2830]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2830 or target_col == 2830). Every well: [[FUBP3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FUBP3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
