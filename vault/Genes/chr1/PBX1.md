---
symbol: "PBX1"
type: "gene"
col: 11706
ensembl_id: "ENSG00000185630"
name: "PBX homeobox 1"
location: "1q23.3"
module: 8
arm: "+"
pooled_cpm: 67.18
n_lines_expressing: 30
n_dd_up: 40
n_dd_down: 32
n_dd_up_clean: 35
n_dd_down_clean: 25
in_vector_space: true
direction_upstream: 14
direction_downstream: 12
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# PBX1

*PBX homeobox 1* — 1q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 40 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.67× (z +9.0, q 2e-16, up in 19 of 27 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 2.39× (z +8.1, q 2e-13, up in 23 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 32 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.275× (z -12.0, q 3e-30, down in 25 of 28 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MID1]] (+0.64, fdr 7e-06), [[SPTLC3]] (+0.61, fdr 1e-05), [[ESRRG]] (+0.60, fdr 1e-05); moves opposite to [[PLEKHN1]] (-0.50, fdr 6e-05), [[SMIM29]] (-0.49, fdr 4e-05), [[PARVB]] (-0.47, fdr 3e-05).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 14 arrows point to it, the strongest [[TCN1]] → it (grade B ⚠); 12 go from it, the strongest it → [[MTUS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 40 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11706.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.67×** | +9.0 | 2e-16 | 19/27 (A-172, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **2.39×** | +8.1 | 2e-13 | 23/28 (A-172, CFPAC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.47×** | +8.1 | 2e-13 | 13/23 (A-172, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.12×** | +7.0 | 4e-10 | 14/28 (A-172, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.90×** | +5.9 | 4e-07 | 23/27 (NCI-H23, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.88×** | +5.8 | 4e-07 | 21/28 (A-172, NCI-H23, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.93×** | +5.8 | 4e-07 | 22/27 (NCI-H23, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.88×** | +5.8 | 4e-07 | 13/28 (A-172, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.87×** | +5.8 | 4e-07 | 14/28 (A-172, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.57×** | +5.4 | 5e-06 | 20/28 (NCI-H23, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.15×** | +5.3 | 7e-06 | 17/28 (A-172, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.70×** | +5.0 | 2e-05 | 22/29 (NCI-H23, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.46×** | +5.0 | 3e-05 | 13/28 (A-172, COLO 205, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM |  | **1.67×** | +4.9 | 4e-05 | 21/30 (NCI-H23, BT-474, …) | all doses, flat | cell-cycle shift (explains ~10% here); noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.54×** | +4.8 | 5e-05 | 21/28 (NCI-H23, BT-474, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.72×** | +4.8 | 5e-05 | 20/27 (NCI-H23, LoVo, …) | all doses, flat |  |
| [[Brivudine (drug)]] 5 µM |  | **2.82×** | +4.8 | 5e-05 | 15/29 (A-172, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 32 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11706.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.275×** | -12.0 | 3e-30 | 25/28 (HT-29, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.414×** | -11.6 | 2e-28 | 23/28 (HT-29, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.323×** | -10.5 | 2e-23 | 27/28 (HT-29, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.329×** | -10.3 | 1e-22 | 27/28 (LS 180, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.339×** | -9.7 | 5e-20 | 25/28 (HEC-1-A, LS 180, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.348×** | -9.6 | 6e-20 | 25/28 (NCI-H460, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.372×** | -9.2 | 4e-18 | 26/27 (NCI-H23, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.375×** | -9.1 | 7e-18 | 24/27 (HT-29, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.583×** | -7.1 | 1e-10 | 26/29 (HT-29, CFPAC-1, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.484×** | -6.7 | 1e-09 | 22/27 (HT-29, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.508×** | -6.3 | 2e-08 | 23/27 (HT-29, NCI-H23, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.525×** | -6.0 | 1e-07 | 22/27 (NCI-H1573, Panc 03.27, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.532×** | -5.9 | 2e-07 | 26/28 (HT-29, A-427, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.540×** | -5.7 | 5e-07 | 21/28 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.528×** | -5.7 | 5e-07 | 23/27 (HT-29, NCI-H23, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.549×** | -5.6 | 9e-07 | 19/27 (CFPAC-1, HT-29, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.539×** | -4.9 | 3e-05 | 24/28 (AN3 CA, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.596×** | -4.8 | 5e-05 | 21/28 (HT-29, A498, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.592×** | -4.8 | 5e-05 | 18/27 (HT-29, AN3 CA, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, -0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11706. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 77.5 | 0 | 13 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.141× (z -17.6) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0784× (z -16.1) |
| [[LS 180 (line)]] | wt | 90.0 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -14.0) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.135× (z -12.4) |
| [[NCI-H23 (line)]] | alt | 31.1 | 1 (1 ⚠) | 6 (2 ⚠) | [[Adagrasib (drug)]] 0.05 µM 2.50× (z +15.4) ⚠ position not correctable | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0803× (z -12.8) |
| [[NCI-H460 (line)]] | wt | 325 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.192× (z -14.0) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.144× (z -11.4) |
| [[HEC-1-A (line)]] | alt | 51.0 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -17.1) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.172× (z -12.9) |
| [[LoVo (line)]] | wt | 27.4 | 0 | 6 (2 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.192× (z -10.3) |
| [[SHP-77 (line)]] | alt | 77.8 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.104× (z -13.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.213× (z -9.8) |
| [[NCI-H1573 (line)]] | alt | 86.8 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0683× (z -13.7) |
| [[NCI-H1792 (line)]] | alt | 50.1 | 1 (1 ⚠) | 3 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.74× (z +9.4) ⚠ position not correctable | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.119× (z -10.6) |
| [[A-172 (line)]] | wt | 38.8 | 3 (1 ⚠) | 0 | [[Ponatinib (drug)]] 5 µM 4.46× (z +9.9) | — |
| [[A-427 (line)]] | wt | 40.1 | 0 | 3 | — | [[Harringtonine (drug)]] 5 µM 0.145× (z -10.3) |
| [[A498 (line)]] | wt | 416 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.196× (z -13.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.125× (z -11.9) |
| [[CFPAC-1 (line)]] | alt | 39.9 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -10.1) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.153× (z -9.4) |
| [[Panc 03.27 (line)]] | alt | 65.5 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0994× (z -10.8) |
| [[A549 (line)]] | wt | 128 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.147× (z -12.2) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.132× (z -9.1) |
| [[SW1417 (line)]] | alt | 31.7 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.251× (z -11.0) ⚠ cell-cycle shift, explains ~29% of this change |
| [[AN3 CA (line)]] | alt | 69.8 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.101× (z -8.7) |
| [[AsPC-1 (line)]] | alt | 32.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -10.4) ⚠ cell-cycle shift, explains ~29% of this change |
| [[COLO 205 (line)]] | alt | 23.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.146× (z -8.8) |
| [[SW 900 (line)]] | alt | 55.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.271× (z -9.2) ⚠ cell-cycle shift, explains ~29% of this change |
| [[SW48 (line)]] | wt | 20.2 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.0806× (z -8.8) |
| [[BT-474 (line)]] | alt | 343 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.84 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 5.78 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 253 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 39.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.89 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 14.2 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 6.10 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 58.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.7 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 15.5 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 11.0 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 12.9 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.50 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 8.92 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 62.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.62 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 71.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.9 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 6.68 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 7.84 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 10.0 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.31 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 7.77 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.2 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 6.40 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11706), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MID1]] | +0.64 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[SPTLC3]] | +0.61 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[ESRRG]] | +0.60 | +0.55 / +0.52 | both halves | 1e-05 | STRING 428 |
| [[CXXC4]] | +0.60 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[MAP2K6]] | +0.58 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[HAVCR1]] | +0.58 | +0.46 / +0.44 | both halves | 3e-05 |  |
| [[GPRIN3]] | +0.58 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[CPS1]] | +0.58 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[SLC4A4]] | +0.57 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[MPP7]] | +0.57 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[BCAS1]] | +0.57 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[MTUS1]] | +0.55 | +0.52 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLEKHN1]] | -0.50 | -0.38 / -0.58 | both halves | 6e-05 |  |
| [[SMIM29]] | -0.49 | -0.41 / -0.53 | both halves | 4e-05 |  |
| [[PARVB]] | -0.47 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[PPP1R21]] | -0.46 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[KIF5A]] | -0.46 | -0.48 / -0.31 | both halves | 2e-04 |  |
| [[TNFRSF10A]] | -0.46 | -0.40 / -0.50 | both halves | 5e-05 |  |
| [[FAM83G]] | -0.46 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[IL17RA]] | -0.46 | -0.38 / -0.47 | both halves | 7e-05 |  |
| [[STK10]] | -0.46 | -0.38 / -0.49 | both halves | 6e-05 |  |
| [[MEIS3]] | -0.45 | -0.44 / -0.45 | both halves | 3e-05 | same gene group; STRING 634 |
| [[ZNF600]] | -0.45 | -0.36 / -0.42 | both halves | 1e-04 |  |
| [[SFN]] | -0.45 | -0.32 / -0.51 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 11, C 3. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TCN1]] | B | TCN1 activity raises PBX1's level | lines that do not express TCN1 (37) vs lines expressing it (13) | 1.86× lower at baseline in the lines without TCN1 | 0.019 | ⚠ within organs, on part of the lines; also absent: AGR3, MUC5AC, MUC5B |
| [[GPRIN3]] | B | GPRIN3 activity raises PBX1's level | lines that do not express GPRIN3 (35) vs lines expressing it (15) | 2.82× lower at baseline in the lines without GPRIN3 | 0.037 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AKR1B10, ENSG00000230975, ENSG00000237031 |
| [[POF1B]] | B | POF1B activity raises PBX1's level | lines that do not express POF1B (34) vs lines expressing it (16) | 2.21× lower at baseline in the lines without POF1B | 0.037 | ⚠ within organs, on part of the lines; also absent: S100P, ENSG00000287426, TRIM31 |
| [[LIMCH1]] | B | LIMCH1 activity raises PBX1's level | lines that do not express LIMCH1 (16) vs lines expressing it (34) | 2.35× lower at baseline in the lines without LIMCH1 | 0.053 | ⚠ within organs, on part of the lines; also absent: SNCAIP, TTC6, DIO2 |
| [[SIDT1]] | B | SIDT1 activity raises PBX1's level | lines that do not express SIDT1 (32) vs lines expressing it (18) | 2.36× lower at baseline in the lines without SIDT1 | 0.060 | ⚠ within organs, on part of the lines; also absent: TMEM30B, STEAP4, GRHL2 |
| [[ESRRG]] | B | ESRRG activity raises PBX1's level | lines that do not express ESRRG (26) vs lines expressing it (24) | 2.67× lower at baseline in the lines without ESRRG | 0.074 | ⚠ within organs, on part of the lines; also absent: HS3ST5, RUNX1T1, SNTG1; maybe low, not absent |
| [[FOXP2]] | B | FOXP2 activity raises PBX1's level | lines that do not express FOXP2 (26) vs lines expressing it (24) | 1.87× lower at baseline in the lines without FOXP2 | 0.076 | ⚠ within organs, on part of the lines; also absent: BMP4, SPON1, ITGB6 |
| [[CYP4F12]] | B | CYP4F12 activity raises PBX1's level | lines that do not express CYP4F12 (32) vs lines expressing it (18) | 2.16× lower at baseline in the lines without CYP4F12 | 0.079 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FXYD3, CDH17, MUC13 |
| [[TM4SF4]] | B | TM4SF4 activity raises PBX1's level | lines that do not express TM4SF4 (42) vs lines expressing it (8) | 2.60× lower at baseline in the lines without TM4SF4 | 0.085 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PIGR, MUC17, HHLA2 |
| [[CXXC4]] | B | CXXC4 activity raises PBX1's level | lines that do not express CXXC4 (25) vs lines expressing it (25) | 2.31× lower at baseline in the lines without CXXC4 | 0.091 | ⚠ within organs, on part of the lines; also absent: VIPR2, DOK6, CCSER1 |
| [[MAP2K6]] | B | MAP2K6 activity raises PBX1's level | lines that do not express MAP2K6 (21) vs lines expressing it (29) | 1.83× lower at baseline in the lines without MAP2K6 | 0.095 | ⚠ within organs, on part of the lines; also absent: AGMO, MTMR8, ENSG00000286133; maybe low, not absent |
| [[PDK4]] | C | PDK4 activity raises PBX1's level | lines that do not express PDK4 (25) vs lines expressing it (25) | 2.71× lower at baseline in the lines without PDK4 | 0.024 | ⚠ within organs, on part of the lines; also absent: TNS4, HPGD, IL20RA; co-absent with the target |

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 9, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MTUS1]] | B | PBX1 activity raises MTUS1's level | lines that do not express PBX1 (20) vs lines expressing it (30) | 2.97× lower at baseline in the lines without PBX1 | 0.012 | ⚠ within organs, on part of the lines; also absent: LIPG, ENSG00000287003, GALNT9 |
| [[RBM47]] | B | PBX1 activity raises RBM47's level | lines that do not express PBX1 (20) vs lines expressing it (30) | 2.93× lower at baseline in the lines without PBX1 | 0.044 | ⚠ within organs, on part of the lines; also absent: LIPG, ENSG00000287003, GALNT9 |
| [[BAG1]] | B | PBX1 activity raises BAG1's level | lines that do not express PBX1 (20) vs lines expressing it (30) | 1.47× lower at baseline in the lines without PBX1 | 0.051 | ⚠ within organs, on part of the lines; also absent: LIPG, ENSG00000287003, GALNT9 |
| [[DLK2]] | B | PBX1 activity lowers DLK2's level | lines that do not express PBX1 (20) vs lines expressing it (30) | 1.50× higher at baseline in the lines without PBX1 | 0.060 | ⚠ within organs, on part of the lines; also absent: LIPG, ENSG00000287003, GALNT9 |
| [[ADD3]] | B | PBX1 activity raises ADD3's level | lines that do not express PBX1 (20) vs lines expressing it (30) | 1.87× lower at baseline in the lines without PBX1 | 0.066 | ⚠ within organs, on part of the lines; also absent: LIPG, ENSG00000287003, GALNT9 |
| [[TJP3]] | B | PBX1 activity raises TJP3's level | lines that do not express PBX1 (20) vs lines expressing it (30) | 2.25× lower at baseline in the lines without PBX1 | 0.074 | ⚠ within organs, on part of the lines; also absent: LIPG, ENSG00000287003, GALNT9 |
| [[SIDT1]] | B | PBX1 activity raises SIDT1's level | lines that do not express PBX1 (20) vs lines expressing it (30) | 2.18× lower at baseline in the lines without PBX1 | 0.082 | ⚠ within organs, on part of the lines; also absent: LIPG, ENSG00000287003, GALNT9 |
| [[ATP8B1]] | B | PBX1 activity raises ATP8B1's level | lines that do not express PBX1 (20) vs lines expressing it (30) | 2.18× lower at baseline in the lines without PBX1 | 0.083 | ⚠ within organs, on part of the lines; also absent: LIPG, ENSG00000287003, GALNT9 |
| [[LIMCH1]] | B | PBX1 activity raises LIMCH1's level | lines that do not express PBX1 (20) vs lines expressing it (30) | 2.51× lower at baseline in the lines without PBX1 | 0.093 | ⚠ within organs, on part of the lines; also absent: LIPG, ENSG00000287003, GALNT9 |
| [[TC2N]] | C | PBX1 activity raises TC2N's level | lines that do not express PBX1 (20) vs lines expressing it (30) | 3.72× lower at baseline in the lines without PBX1 | 0.009 | ⚠ within organs, on part of the lines; also absent: LIPG, ENSG00000287003, GALNT9; co-absent with the target |
| [[PDK4]] | C | PBX1 activity raises PDK4's level | lines that do not express PBX1 (20) vs lines expressing it (30) | 2.88× lower at baseline in the lines without PBX1 | 0.020 | ⚠ within organs, on part of the lines; also absent: LIPG, ENSG00000287003, GALNT9; co-absent with the target |
| [[TSPAN8]] | C | PBX1 activity raises TSPAN8's level | lines that do not express PBX1 (20) vs lines expressing it (30) | 1.90× lower at baseline in the lines without PBX1 | 0.086 | ⚠ within organs, on part of the lines; also absent: LIPG, ENSG00000287003, GALNT9; co-absent with the target |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.463). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (35.9, 43.0); signed map (51.1, 18.2). **Vector** length 95.6, 30.2% of its response variance represented; |z| ≥ 3 in 1,095 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.1 | +9.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.6 | +4.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.6 | +8.1 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.3 | +2.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.3 | -1.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +5.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.9 | +4.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.6 | +5.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.5 | +4.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.4 | +5.0 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -4.0 | -9.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.9 | -6.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.3 | -5.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.2 | -1.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.2 | -7.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.1 | -5.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.7 | -5.7 |

## What is on record

|  |  |
|---|---|
| Name | PBX homeobox 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q23.3 — chr1:164,555,584-164,899,296 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | TALE class homeoboxes and pseudogenes |
| Reactome | 6 pathways, smallest: Transcriptional regulation of pluripotent stem cells; NOTCH3 Intracellular Domain Regulates Transcription; Signaling by NOTCH3 |
| Matched by | ensembl_id |

**Function**, from UniProt [P40424](https://www.uniprot.org/uniprotkb/P40424) (Pre-B-cell leukemia transcription factor 1):

> Transcription factor which binds the DNA sequence 5'-TGATTGAT-3' as part of a heterodimer with HOX proteins such as HOXA1, HOXA5, HOXB7 and HOXB8. Binds to the DNA sequence 5'-TGATTGAC-3' in complex with a nuclear factor which is not a class I HOX protein. Has also been shown to bind the DNA sequence 5'-ATCAATCAA-3' cooperatively with HOXA5, HOXB7, HOXB8, HOXC8 and HOXD4. Acts as a transcriptional activator of PF4 in complex with MEIS1. Also activates transcription of SOX3 in complex with MEIS1 …

**Summary**, from NCBI Gene [5087](https://www.ncbi.nlm.nih.gov/gene/5087):

> This gene encodes a nuclear protein that belongs to the PBX homeobox family of transcriptional factors. Studies in mice suggest that this gene may be involved in the regulation of osteogenesis and required for skeletal patterning and programming. A chromosomal translocation, t(1;19) involving this gene and TCF3/E2A gene, is associated with pre-B-cell acute lymphoblastic leukemia. The resulting fusion protein, in which the DNA binding domain of E2A is replaced by the DNA binding domain of this …

**Accessions** — [HGNC:8632](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8632) · Entrez [5087](https://www.ncbi.nlm.nih.gov/gene/5087) · UniProt [P40424](https://www.uniprot.org/uniprotkb/P40424) · Ensembl [ENSG00000185630](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185630)

## Data

Gene col 11706: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11706); `tables/drug_effects.parquet` (72 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11706, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11706]; `tensor/DDL_lfc|DDL_z.npy` [11706]; `embed/gene_vectors.npy` [11706]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11706 or target_col == 11706). Every well: [[PBX1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PBX1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
