---
symbol: "MYL12A"
type: "gene"
col: 2158
ensembl_id: "ENSG00000101608"
name: "myosin light chain 12A"
location: "18p11.31"
module: 174
arm: "+"
pooled_cpm: 181.97
n_lines_expressing: 49
n_dd_up: 13
n_dd_down: 6
n_dd_up_clean: 5
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/174"]
generated_by: "tahoemap"
---

# MYL12A

*myosin light chain 12A* — 18p11.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.68× (z +12.1, q 6e-31, up in 47 of 48 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.54× (z +4.0, q 0.007, up in 34 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Trametinib (drug)]] 5 µM: 0.551× (z -4.8, q 0.001, down in 45 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MYL12B]] (+0.69, fdr 7e-06, ⚠ same locus), [[PFN1]] (+0.66, fdr 1e-05), [[MCL1]] (+0.62, fdr 7e-06), [[TNFRSF12A]] (+0.62, fdr 1e-05); moves opposite to [[FBXO7]] (-0.56, fdr 3e-05), [[TMEM94]] (-0.56, fdr 1e-05), [[SUPV3L1]] (-0.54, fdr 1e-05).
> It is in [[Module 174]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[EPHA2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 8 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2158.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **3.68×** | +12.1 | 6e-31 | 47/48 (NCI-H1792, J82, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **3.10×** | +10.1 | 2e-21 | 41/43 (A498, SNU-423, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **2.10×** | +6.4 | 4e-08 | 40/44 (J82, hTERT-HPNE, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | **1.76×** | +5.3 | 2e-05 | 40/47 (Hs 766T, HCT15, …) | rises with dose | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.54×** | +4.0 | 0.007 | 34/47 (MIA PaCa-2, SW480, …) | top dose only |  |
| [[vincristine (drug)]] 0.5 µM |  | **2.29×** | +3.7 | 0.018 | 44/47 (HT-29, A-172, …) | all doses, stronger at high dose | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~87% of this change | **1.48×** | +3.7 | 0.020 | 36/47 (HOP62, CFPAC-1, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Mebendazole (drug)]] 5 µM |  | **1.46×** | +3.4 | 0.055 | 36/47 (HT-29, NCI-H1792, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.43×** | +3.3 | 0.055 | 32/47 (A549, NCI-H1792, …) | two highest doses |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.40×** | +3.1 | 0.092 | 31/47 (COLO 205, LOX-IMVI, …) | top dose only |  |
| [[vincristine (drug)]] 5 µM |  | **2.08×** | +3.1 | 0.092 | 35/45 (A-172, HT-29, …) | all doses, stronger at high dose | noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **1.40×** | +3.1 | 0.092 | 26/47 (LOX-IMVI, C32, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.41×** | +3.1 | 0.098 | 30/46 (A-172, HT-29, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2158.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM |  | **0.551×** | -4.8 | 0.001 | 45/49 (MIA PaCa-2, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~22% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.597×** | -4.4 | 0.003 | 37/47 (MIA PaCa-2, C32, …) | all doses, flat | position effect removed |
| [[Trametinib (drug)]] 0.05 µM |  | **0.725×** | -4.1 | 0.006 | 37/47 (MIA PaCa-2, C32, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.652×** | -3.8 | 0.018 | 33/46 (NCI-H23, SW480, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~73% of this change | **0.667×** | -3.6 | 0.042 | 39/47 (LOX-IMVI, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.695×** | -3.4 | 0.067 | 34/47 (C32, HOP62, …) | rises with dose |  |
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.715× | -3.1 | 0.14 | 39/47 (C32, H4, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | 0.486× | -3.1 | 0.14 | 36/49 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.720× | -3.1 | 0.14 | 28/46 (C32, MIA PaCa-2, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, +0.71 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2158. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 169 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.27× (z +13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[A-172 (line)]] | wt | 242 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.75× (z +13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[A498 (line)]] | wt | 140 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.22× (z +12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[A549 (line)]] | wt | 144 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.93× (z +12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[AsPC-1 (line)]] | alt | 215 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.32× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[C32 (line)]] | wt | 108 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.72× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[CFPAC-1 (line)]] | alt | 63.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.43× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[HOP62 (line)]] | alt | 359 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.99× (z +12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[Hs 766T (line)]] | wt | 185 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.20× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[HT-29 (line)]] | alt | 235 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.35× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 113 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.37× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[KATO III (line)]] | alt | 207 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.72× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 221 | 0 | 2 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.628× (z -12.5) ⚠ position not correctable · without an alert: [[Trametinib (drug)]] 5 µM 0.279× (z -9.2) |
| [[NCI-H1792 (line)]] | alt | 73.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.45× (z +13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[NCI-H2030 (line)]] | alt | 206 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.68× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[NCI-H460 (line)]] | wt | 108 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.15× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[PANC-1 (line)]] | alt | 235 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.68× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[SNU-423 (line)]] | alt | 81.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.00× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[SW 900 (line)]] | alt | 116 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.72× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[AN3 CA (line)]] | alt | 71.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 9.88× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[CHP-212 (line)]] | wt | 90.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.19× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[COLO 205 (line)]] | alt | 82.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.54× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[H4 (line)]] | wt | 111 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.22× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[HEC-1-A (line)]] | alt | 237 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.75× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[HepG2_C3A (line)]] | wt | 190 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.449× (z -8.5) ⚠ cell-cycle shift, would explain all of this change |
| [[HS-578T (line)]] | alt | 155 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.91× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[LoVo (line)]] | wt | 103 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.27× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[LOX-IMVI (line)]] | wt | 107 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.32× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[NCI-H23 (line)]] | alt | 294 | 0 | 1 | — | [[Trametinib (drug)]] 5 µM 0.339× (z -8.7) |
| [[NCI-H2347 (line)]] | alt | 212 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.73× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[Panc 03.27 (line)]] | alt | 186 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.81× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[RPMI-7951 (line)]] | alt | 128 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.79× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[SNU-1 (line)]] | wt | 131 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.93× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[SW1417 (line)]] | alt | 115 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.27× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[SW48 (line)]] | wt | 85.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.56× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[SW480 (line)]] | alt | 172 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.33× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[A-427 (line)]] | wt | 483 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 232 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 193 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 156 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 173 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 345 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 148 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 272 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 43.7 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 142 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 121 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2158), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYL12B]] | +0.69 | +0.65 / +0.72 | both halves | 7e-06 | same gene group; pathway: EPH-Ephrin signaling; STRING 945; ⚠ same locus (5.2 kb, same strand: neighbours can correlate without regulation) |
| [[PFN1]] | +0.66 | +0.71 / +0.57 | both halves | 1e-05 | STRING 402 |
| [[MCL1]] | +0.62 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[TNFRSF12A]] | +0.62 | +0.69 / +0.56 | both halves | 1e-05 |  |
| [[S100A11]] | +0.62 | +0.54 / +0.68 | both halves | 1e-05 |  |
| [[SEPTIN10]] | +0.61 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[GOLT1A]] | +0.61 | +0.65 / +0.48 | both halves | 2e-05 |  |
| [[AGO2]] | +0.61 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[DUSP6]] | +0.61 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[DOCK5]] | +0.59 | +0.49 / +0.62 | both halves | 1e-05 |  |
| [[SPRY4-AS1]] | +0.59 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[CD59]] | +0.58 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[ITGB5]] | +0.58 | +0.51 / +0.59 | both halves | 1e-05 | pathway: Muscle contraction; STRING 575 |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBXO7]] | -0.56 | -0.56 / -0.46 | both halves | 3e-05 |  |
| [[TMEM94]] | -0.56 | -0.57 / -0.50 | both halves | 1e-05 |  |
| [[SUPV3L1]] | -0.54 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[HSF2]] | -0.54 | -0.63 / -0.47 | both halves | 2e-05 |  |
| [[PSMA3]] | -0.54 | -0.54 / -0.44 | both halves | 3e-05 |  |
| [[PSMC6]] | -0.53 | -0.56 / -0.45 | both halves | 3e-05 |  |
| [[RAVER2]] | -0.53 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[EFCAB7]] | -0.53 | -0.58 / -0.49 | both halves | 1e-05 |  |
| [[TXNL1]] | -0.52 | -0.58 / -0.44 | both halves | 3e-05 |  |
| [[TMEM143]] | -0.52 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[GNPDA2]] | -0.51 | -0.61 / -0.43 | both halves | 3e-05 |  |
| [[COPS2]] | -0.51 | -0.55 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPHA2]] | B | EPHA2 activity raises MYL12A's level | lines that do not express EPHA2 (11) vs lines expressing it (39) | 1.59× lower at baseline in the lines without EPHA2 | 0.026 | ⚠ within organs, on part of the lines; also absent: RHOD, LINC00857, ABLIM2; maybe low, not absent |
| [[CCND1]] | B | CCND1 activity raises MYL12A's level | lines that do not express CCND1 (7) vs lines expressing it (43) | 1.62× lower at baseline in the lines without CCND1 | 0.036 | ⚠ within organs, on part of the lines; also absent: FSTL3, ADAMTSL5; maybe low, not absent |
| [[PSMB5]] | B | PSMB5 activity raises MYL12A's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[LINC01844]] | B | LINC01844 activity raises MYL12A's level | lines that do not express LINC01844 (11) vs lines expressing it (39) | 1.48× lower at baseline in the lines without LINC01844 | 0.086 | ⚠ within organs, on part of the lines; also absent: ENSG00000287712, ADGRG2, ENSG00000291283; maybe low, not absent |
| [[VGF]] | B | VGF activity strengthens MYL12A's drug response | lines that do not express VGF (32) vs lines expressing it (17) | the lines without VGF respond 1.01× as strongly (z diff +0.59); strongest at Cobimetinib 5 µM: 0.67x vs 0.56x (z diff +1.5) | 0.097 | ⚠ within organs, on part of the lines; also absent: RAB3C, KCNH5, CSMD3; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 174]]; 23 genes; every member is in the + arm (projection on the module's main direction 0.576). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (38.8, 3.8); signed map (9.3, 41.4). **Vector** length 101, 43.9% of its response variance represented; |z| ≥ 3 in 1,017 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.0 | +2.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.2 | +2.9 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.8 | +1.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~71% of this change | +3.5 | +3.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.4 | +1.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.9 | +2.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.8 | +3.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.4 | +2.9 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.9 | +2.6 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | -7.1 | -3.4 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~73% of this change | -5.7 | -3.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.6 | -1.8 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.4 | -2.3 |
|  | [[Trametinib (drug)]] 5 µM |  | -4.3 | -4.8 |
|  | [[venetoclax (drug)]] 5 µM |  | -4.1 | -1.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.0 | -2.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -3.7 | -2.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.6 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | myosin light chain 12A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18p11.31 — chr18:3,247,481-3,256,236 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MLCB, MYL2B, MRLC3, MRCL3 |
| Gene groups (HGNC) | Myosin light chains, class 2 |
| Hallmark sets | ANDROGEN_RESPONSE |
| Reactome | 6 pathways, smallest: Ephrin signaling; Smooth Muscle Contraction; EPH-Ephrin signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [P19105](https://www.uniprot.org/uniprotkb/P19105) (Myosin regulatory light chain 12A):

> Myosin regulatory subunit that plays an important role in regulation of both smooth muscle and nonmuscle cell contractile activity via its phosphorylation. Implicated in cytokinesis, receptor capping, and cell locomotion (By similarity).

**Summary**, from NCBI Gene [10627](https://www.ncbi.nlm.nih.gov/gene/10627):

> This gene encodes a nonsarcomeric myosin regulatory light chain. This protein is activated by phosphorylation and regulates smooth muscle and non-muscle cell contraction. This protein may also be involved in DNA damage repair by sequestering the transcriptional regulator apoptosis-antagonizing transcription factor (AATF)/Che-1 which functions as a repressor of p53-driven apoptosis. Alternate splicing results in multiple transcript variants. A pseudogene of this gene is found on chromosome …

**Accessions** — [HGNC:16701](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16701) · Entrez [10627](https://www.ncbi.nlm.nih.gov/gene/10627) · UniProt [P19105](https://www.uniprot.org/uniprotkb/P19105) · Ensembl [ENSG00000101608](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101608)

## Data

Gene col 2158: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2158); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2158, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2158]; `tensor/DDL_lfc|DDL_z.npy` [2158]; `embed/gene_vectors.npy` [2158]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2158 or target_col == 2158). Every well: [[MYL12A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MYL12A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
