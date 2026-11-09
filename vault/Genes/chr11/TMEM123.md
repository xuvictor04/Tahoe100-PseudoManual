---
symbol: "TMEM123"
type: "gene"
col: 7642
ensembl_id: "ENSG00000152558"
name: "transmembrane protein 123"
location: "11q22.2"
module: 29
arm: "+"
pooled_cpm: 251.11
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 27
n_dd_up_clean: 4
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# TMEM123

*transmembrane protein 123* — 11q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.96× (z +12.6, q 2e-33, up in 46 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 1.26× (z +4.3, q 0.002, up in 25 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.505× (z -18.1, q 0e+00, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SCARB2]] (+0.74, fdr 7e-06), [[ERMP1]] (+0.71, fdr 7e-06), [[STT3B]] (+0.69, fdr 7e-06); moves opposite to [[ZNF611]] (-0.69, fdr 7e-06), [[ZNF593]] (-0.67, fdr 7e-06), [[PLEKHN1]] (-0.63, fdr 1e-05).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[LUM]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7642.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.96×** | +12.6 | 2e-33 | 46/49 (NCI-H1573, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.97×** | +12.2 | 7e-32 | 43/44 (A549, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.74×** | +9.6 | 2e-19 | 39/45 (HS-578T, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.28×** | +4.6 | 5e-04 | 25/48 (HS-578T, NCI-H1792, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.26×** | +4.3 | 0.002 | 25/48 (H4, HOP62, …) | two highest doses | cell-cycle shift (explains ~10% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.51×** | +4.0 | 0.005 | 27/49 (BT-474, C32, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | **1.21×** | +3.6 | 0.028 | 26/49 (A498, A549, …) | all doses, flat |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | **1.20×** | +3.4 | 0.043 | 21/48 (A549, A-172, …) | all doses, flat |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~42% of this change | 1.20× | +3.4 | 0.047 | 21/48 (hTERT-HPNE, NCI-H1573, …) | inconsistent across doses | low cells (technical?) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.40×** | +3.3 | 0.056 | 20/38 (HS-578T, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[Lopinavir (drug)]] 5 µM |  | 1.18× | +3.1 | 0.086 | 15/47 (A-427, C-33 A, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7642.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.505×** | -18.1 | 0e+00 | 38/48 (COLO 205, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.517×** | -12.4 | 1e-32 | 44/48 (SW480, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.527×** | -12.0 | 7e-31 | 42/48 (SW480, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.583×** | -10.1 | 7e-22 | 36/48 (A-427, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.611×** | -9.2 | 3e-18 | 40/48 (SW480, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.646×** | -7.9 | 3e-13 | 34/48 (AsPC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.679×** | -7.0 | 3e-10 | 36/47 (C32, SW480, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.713×** | -6.0 | 2e-07 | 33/48 (COLO 205, SW480, …) | all doses, flat | cell-cycle shift (explains ~17% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.740×** | -5.6 | 1e-06 | 32/49 (NCI-H2347, MIA PaCa-2, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.772×** | -4.8 | 7e-05 | 27/48 (HepG2/C3A, COLO 205, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | 0.834× | -4.8 | 7e-05 | 23/49 (HT-29, SW480, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.798×** | -4.2 | 0.001 | 29/48 (AsPC-1, SW480, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.804×** | -4.1 | 0.002 | 25/48 (NCI-H2030, SW480, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.737×** | -4.1 | 0.002 | 35/48 (MIA PaCa-2, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.805×** | -4.1 | 0.002 | 28/48 (SW480, NCI-H1573, …) | top dose only |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.741×** | -4.0 | 0.002 | 26/48 (KATO III, HepG2/C3A, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.810×** | -4.0 | 0.002 | 25/48 (COLO 205, LS 180, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.815×** | -3.8 | 0.004 | 25/48 (SW480, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[PH-797804 (drug)]] 0.5 µM |  | **0.767×** | -3.5 | 0.011 | 28/49 (SHP-77, NCI-H460, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7642. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 248 | 1 (1 ⚠) | 10 (3 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.08× (z +9.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.374× (z -17.9) |
| [[SW480 (line)]] | alt | 402 | 0 | 11 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -20.3) |
| [[HepG2_C3A (line)]] | wt | 581 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -19.7) |
| [[PANC-1 (line)]] | alt | 451 | 3 (3 ⚠) | 6 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.10× (z +10.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.440× (z -16.1) |
| [[COLO 205 (line)]] | alt | 255 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.133× (z -26.6) |
| [[HT-29 (line)]] | alt | 478 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -18.9) |
| [[KATO III (line)]] | alt | 553 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.374× (z -17.0) |
| [[AsPC-1 (line)]] | alt | 157 | 2 (1 ⚠) | 5 | [[Dinaciclib (drug)]] 0.5 µM 2.27× (z +9.1) ⚠ toxic; transcription drop · without an alert: [[Radotinib (drug)]] 5 µM 1.73× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.336× (z -17.1) |
| [[LoVo (line)]] | wt | 170 | 2 (2 ⚠) | 5 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.58× (z +12.2) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.415× (z -11.3) |
| [[NCI-H460 (line)]] | wt | 140 | 3 (3 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 2.49× (z +12.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.379× (z -18.9) |
| [[C-33 A (line)]] | alt | 174 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 2.99× (z +13.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.377× (z -17.4) |
| [[C32 (line)]] | wt | 374 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.266× (z -15.0) |
| [[NCI-H1573 (line)]] | alt | 74.4 | 1 (1 ⚠) | 5 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.72× (z +14.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.363× (z -15.4) |
| [[A-427 (line)]] | wt | 399 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.386× (z -17.0) |
| [[A549 (line)]] | wt | 153 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 4.04× (z +15.4) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.438× (z -9.5) |
| [[BT-474 (line)]] | alt | 550 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -17.3) |
| [[HEC-1-A (line)]] | alt | 132 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.22× (z +11.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.535× (z -12.4) |
| [[MIA PaCa-2 (line)]] | alt | 379 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.345× (z -17.2) |
| [[SHP-77 (line)]] | alt | 145 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 2.38× (z +9.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.415× (z -14.2) |
| [[SW1417 (line)]] | alt | 451 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.341× (z -14.1) |
| [[SW48 (line)]] | wt | 276 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.368× (z -12.4) |
| [[LOX-IMVI (line)]] | wt | 228 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.35× (z +10.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.531× (z -10.9) |
| [[NCI-H23 (line)]] | alt | 153 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -20.6) |
| [[SK-MEL-2 (line)]] | alt | 94.4 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.07× (z +12.0) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.346× (z -11.3) |
| [[SNU-1 (line)]] | wt | 142 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.84× (z +10.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.495× (z -9.4) |
| [[HOP62 (line)]] | alt | 121 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.73× (z +12.1) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 160 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.25× (z +11.3) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 123 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.08× (z +12.0) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 116 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.74× (z +12.2) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 185 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.88× (z +11.3) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 361 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.466× (z -12.5) |
| [[RKO (line)]] | wt | 190 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.35× (z +10.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.370× (z -17.6) |
| [[A498 (line)]] | wt | 153 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.02× (z +9.3) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 186 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.96× (z +10.3) ⚠ toxic; transcription drop | [[Bortezomib (drug)]] 5 µM 0.0904× (z -12.5) ⚠ toxic |
| [[HCT15 (line)]] | alt | 183 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -18.8) |
| [[NCI-H2030 (line)]] | alt | 204 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.340× (z -17.8) |
| [[NCI-H2347 (line)]] | alt | 314 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.442× (z -15.2) |
| [[A-172 (line)]] | wt | 117 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.448× (z -9.5) |
| [[AN3 CA (line)]] | alt | 192 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.22× (z +9.6) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 292 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.556× (z -9.3) |
| [[Hs 766T (line)]] | wt | 204 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.498× (z -10.7) |
| [[CHP-212 (line)]] | wt | 198 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 187 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 234 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 204 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 153 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 232 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 229 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 345 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 160 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7642), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*59 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SCARB2]] | +0.74 | +0.69 / +0.76 | both halves | 7e-06 |  |
| [[ERMP1]] | +0.71 | +0.65 / +0.69 | both halves | 7e-06 |  |
| [[STT3B]] | +0.69 | +0.72 / +0.66 | both halves | 7e-06 |  |
| [[PON2]] | +0.68 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[FKBP9]] | +0.68 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[LAMP2]] | +0.66 | +0.58 / +0.70 | both halves | 7e-06 |  |
| [[TMX1]] | +0.66 | +0.63 / +0.67 | both halves | 7e-06 |  |
| [[CRTAP]] | +0.66 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[ITM2B]] | +0.65 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[MBNL3]] | +0.65 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[ATP5F1B]] | +0.64 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[PPT1]] | +0.64 | +0.63 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*41 of its nearest partners move opposite, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF611]] | -0.69 | -0.60 / -0.74 | both halves | 7e-06 |  |
| [[ZNF593]] | -0.67 | -0.59 / -0.69 | both halves | 7e-06 |  |
| [[PLEKHN1]] | -0.63 | -0.56 / -0.58 | both halves | 1e-05 |  |
| [[C19orf25]] | -0.61 | -0.49 / -0.66 | both halves | 1e-05 |  |
| [[NDUFB9]] | -0.61 | -0.63 / -0.59 | both halves | 7e-06 |  |
| [[USE1]] | -0.61 | -0.59 / -0.57 | both halves | 1e-05 |  |
| [[PEX16]] | -0.60 | -0.54 / -0.61 | both halves | 1e-05 |  |
| [[SAP30BP]] | -0.60 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[UBE2CP5]] | -0.60 | -0.61 / -0.61 | both halves | 7e-06 |  |
| [[METRNL]] | -0.59 | -0.53 / -0.58 | both halves | 1e-05 |  |
| [[ADRM1]] | -0.59 | -0.53 / -0.60 | both halves | 1e-05 |  |
| [[SMIM26]] ⚠ | -0.59 | -0.52 / -0.62 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[JOSD2]] | -0.58 | -0.39 / -0.62 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LUM]] | B | LUM activity weakens TMEM123's drug response | lines that do not express LUM (34) vs lines expressing it (15) | the lines without LUM respond 1.59× as strongly (z diff -1.86); strongest at Homoharringtonine 5 µM: 0.43x vs 0.76x (z diff -5.6) | 0.066 | ⚠ within organs, on part of the lines; also absent: ITGA11, DCN, IRAG2; target measured in part of the lines; artifact flags |
| [[ALDH1A1]] | B | ALDH1A1 activity raises TMEM123's level | lines that do not express ALDH1A1 (36) vs lines expressing it (14) | 1.43× lower at baseline in the lines without ALDH1A1 | 0.085 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AKR1B10, FGA, GCG |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.814). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-25.9, -20.9); signed map (-22.2, -39.4). **Vector** length 151, 55.5% of its response variance represented; |z| ≥ 3 in 1,407 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +8.1 | +9.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.4 | +12.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.4 | +12.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +5.6 | +2.7 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +4.2 | +1.6 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +4.1 | +1.9 |
|  | [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | +4.0 | +2.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +3.7 | +3.4 |
| fall | [[Bortezomib (drug)]] 0.05 µM |  | -7.4 | -6.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -7.1 | -4.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -6.1 | -7.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.8 | -4.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.7 | -7.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -5.1 | -4.1 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -5.0 | -4.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.9 | -2.6 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | -4.7 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 123 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q22.2 — chr11:102,396,332-102,470,384 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PORIMIN, KCT3 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N131](https://www.uniprot.org/uniprotkb/Q8N131) (Porimin):

> Implicated in oncotic cell death, characterized by cell swelling, organelle swelling, vacuolization and increased membrane permeability.

**Summary**, from NCBI Gene [114908](https://www.ncbi.nlm.nih.gov/gene/114908):

> This gene encodes a highly glycosylated transmembrane protein with a high content of threonine and serine residues in its extracellular domain, similar to a broadly defined category of proteins termed mucins. Exposure of some cell types to anti-PORIMIN (pro-oncosis receptor inducing membrane injury) antibody, crosslinks this protein on the cell surface and induces a type of cell death termed oncosis. Oncosis is distinct from apoptosis and is characterized by a loss of cell membrane integrity …

**Accessions** — [HGNC:30138](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30138) · Entrez [114908](https://www.ncbi.nlm.nih.gov/gene/114908) · UniProt [Q8N131](https://www.uniprot.org/uniprotkb/Q8N131) · Ensembl [ENSG00000152558](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000152558)

## Data

Gene col 7642: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7642); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7642, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7642]; `tensor/DDL_lfc|DDL_z.npy` [7642]; `embed/gene_vectors.npy` [7642]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7642 or target_col == 7642). Every well: [[TMEM123 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM123.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
