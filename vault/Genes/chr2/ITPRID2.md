---
symbol: "ITPRID2"
type: "gene"
col: 6175
ensembl_id: "ENSG00000138434"
name: "ITPR interacting domain containing 2"
location: "2q31.3"
module: 34
arm: "+"
pooled_cpm: 255.57
n_lines_expressing: 49
n_dd_up: 5
n_dd_down: 24
n_dd_up_clean: 2
n_dd_down_clean: 23
in_vector_space: true
direction_upstream: 22
direction_downstream: 0
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# ITPRID2

*ITPR interacting domain containing 2* — 2q31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.33× (z +6.5, q 4e-08, up in 28 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 1.31× (z +6.1, q 2e-07, up in 26 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 4 lines (A-427 2.52×, Panc 03.27 2.26×, SW1417 1.99×, MIA PaCa-2 2.24×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (Panc 03.27 2.61×, A-172 2.68×, SW1417 1.79×; ⚠ toxic; transcription drop); [[Pitavastatin (Calcium) (drug)]] 0.5 µM in 2 lines (hTERT-HPNE 2.51×, NCI-H460 1.93×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (MIA PaCa-2 1.66×).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.707× (z -11.2, q 2e-26, down in 29 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ITGA6]] (+0.76, fdr 7e-06), [[SEPTIN10]] (+0.66, fdr 7e-06), [[PSD3]] (+0.65, fdr 9e-06); moves opposite to [[RAF1]] (-0.54, fdr 8e-05), [[TRPM7]] (-0.50, fdr 3e-05), [[ZCCHC8]] (-0.50, fdr 4e-05).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 22 arrows point to it, the strongest [[CD59]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6175.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 4 lines (A-427 2.52×, Panc 03.27 2.26×, SW1417 1.99×, MIA PaCa-2 2.24×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (Panc 03.27 2.61×, A-172 2.68×, SW1417 1.79×; ⚠ toxic; transcription drop); [[Pitavastatin (Calcium) (drug)]] 0.5 µM in 2 lines (hTERT-HPNE 2.51×, NCI-H460 1.93×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (MIA PaCa-2 1.66×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.33×** | +6.5 | 4e-08 | 28/48 (Panc 03.27, A-172, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.31×** | +6.1 | 2e-07 | 26/47 (HepG2/C3A, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.27×** | +5.1 | 5e-05 | 26/47 (LOX-IMVI, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.25×** | +4.9 | 1e-04 | 25/46 (LOX-IMVI, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.24×** | +4.7 | 3e-04 | 22/43 (A-427, Panc 03.27, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~6% of this change | 1.19× | +4.0 | 0.005 | 21/47 (HepG2/C3A, SW480, …) | all doses, stronger at high dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.16× | +3.4 | 0.061 | 16/46 (hTERT-HPNE, NCI-H460, …) | inconsistent across doses | low cells (technical?); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 7 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6175.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.707×** | -11.2 | 2e-26 | 29/48 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.600×** | -11.2 | 2e-26 | 39/47 (AsPC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.733×** | -10.0 | 3e-21 | 28/47 (NCI-H460, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.695×** | -8.3 | 1e-14 | 30/47 (AsPC-1, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.708×** | -7.6 | 5e-12 | 32/47 (AsPC-1, LoVo, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.777×** | -6.9 | 4e-10 | 26/47 (SW480, SW48, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.791×** | -6.7 | 2e-09 | 28/47 (NCI-H23, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.810×** | -6.6 | 3e-09 | 28/48 (SW480, SW48, …) | all doses, flat |  |
| [[Radotinib (drug)]] 5 µM |  | **0.816×** | -6.6 | 3e-09 | 23/47 (LoVo, AsPC-1, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.765×** | -5.9 | 2e-07 | 27/47 (AsPC-1, SW48, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.765×** | -5.9 | 2e-07 | 29/47 (NCI-H460, SW48, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.837× | -5.7 | 5e-07 | 23/47 (SW480, AsPC-1, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.781×** | -5.7 | 7e-07 | 25/48 (NCI-H23, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **0.798×** | -5.6 | 8e-07 | 28/49 (NCI-H23, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.793×** | -5.3 | 4e-06 | 26/48 (AsPC-1, SW48, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.627×** | -5.2 | 7e-06 | 30/48 (A498, Panc 03.27, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6175. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 447 | 2 (1 ⚠) | 20 (5 ⚠) | [[Pitavastatin (Calcium) (drug)]] 5 µM 2.20× (z +10.4) ⚠ cell-cycle shift, explains ~16% of this change · without an alert: [[Pitavastatin (Calcium) (drug)]] 0.5 µM 1.93× (z +9.0) | [[Homoharringtonine (drug)]] 5 µM 0.265× (z -25.8) |
| [[SW48 (line)]] | wt | 614 | 0 | 18 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.143× (z -22.0) |
| [[AsPC-1 (line)]] | alt | 1,294 | 0 | 15 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.320× (z -18.6) |
| [[LoVo (line)]] | wt | 750 | 0 | 7 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.237× (z -24.6) |
| [[Panc 03.27 (line)]] | alt | 308 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.61× (z +13.1) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.526× (z -12.4) |
| [[SW480 (line)]] | alt | 394 | 0 | 5 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.388× (z -14.2) |
| [[hTERT-HPNE (line)]] | wt | 242 | 2 (1 ⚠) | 2 | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 2.51× (z +10.4) | [[Homoharringtonine (drug)]] 5 µM 0.458× (z -12.4) |
| [[LS 180 (line)]] | wt | 437 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.304× (z -17.3) |
| [[NCI-H23 (line)]] | alt | 152 | 0 | 4 | — | [[Trametinib (drug)]] 0.5 µM 0.516× (z -11.1) |
| [[A-427 (line)]] | wt | 102 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.52× (z +11.5) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 402 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.388× (z -13.9) |
| [[A-172 (line)]] | wt | 253 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.68× (z +9.3) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.521× (z -8.7) |
| [[CHP-212 (line)]] | wt | 610 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.220× (z -17.4) |
| [[HOP62 (line)]] | alt | 197 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.506× (z -12.8) |
| [[Hs 766T (line)]] | wt | 269 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.432× (z -12.4) |
| [[HT-29 (line)]] | alt | 322 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.327× (z -15.4) |
| [[MIA PaCa-2 (line)]] | alt | 79.7 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.24× (z +9.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.66× (z +8.5) | — |
| [[NCI-H1573 (line)]] | alt | 221 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.590× (z -9.9) |
| [[NCI-H1792 (line)]] | alt | 178 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.503× (z -10.2) |
| [[PANC-1 (line)]] | alt | 249 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.587× (z -10.1) |
| [[SW1417 (line)]] | alt | 218 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 1.99× (z +10.1) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 231 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.377× (z -11.1) |
| [[HCT15 (line)]] | alt | 236 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.550× (z -8.9) |
| [[LOX-IMVI (line)]] | wt | 178 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.654× (z -8.7) |
| [[NCI-H2030 (line)]] | alt | 142 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.576× (z -10.5) |
| [[SK-MEL-2 (line)]] | alt | 115 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.577× (z -9.9) |
| [[A498 (line)]] | wt | 128 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 85.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 69.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 40.3 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 160 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 145 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 122 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 122 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 120 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 93.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 189 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 318 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 263 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 98.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 143 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 141 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 89.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 157 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 175 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 230 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 140 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6175), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ITGA6]] | +0.76 | +0.76 / +0.73 | both halves | 7e-06 |  |
| [[SEPTIN10]] | +0.66 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[PSD3]] | +0.65 | +0.76 / +0.57 | both halves | 9e-06 |  |
| [[ITGA2]] | +0.65 | +0.71 / +0.60 | both halves | 7e-06 |  |
| [[TMC7]] | +0.63 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[ITGB1]] | +0.61 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[LAMC2]] | +0.61 | +0.66 / +0.57 | both halves | 1e-05 |  |
| [[F2RL1]] | +0.61 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[DCBLD2]] | +0.61 | +0.63 / +0.57 | both halves | 1e-05 |  |
| [[KIAA0040]] | +0.60 | +0.57 / +0.60 | both halves | 9e-06 |  |
| [[FERMT1]] | +0.59 | +0.61 / +0.57 | both halves | 8e-06 |  |
| [[ITGB5]] | +0.58 | +0.63 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAF1]] | -0.54 | -0.51 / -0.37 | both halves | 8e-05 |  |
| [[TRPM7]] | -0.50 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[ZCCHC8]] | -0.50 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[EDN2]] | -0.50 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[SUPV3L1]] | -0.49 | -0.42 / -0.38 | both halves | 7e-05 |  |
| [[PSMA6]] | -0.49 | -0.33 / -0.45 | both halves | 1e-04 |  |
| [[SART3]] | -0.49 | -0.49 / -0.37 | both halves | 8e-05 |  |
| [[MRPL44]] | -0.48 | -0.40 / -0.47 | both halves | 5e-05 |  |
| [[HEIH]] | -0.48 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[NGDN]] | -0.48 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[FLVCR2]] | -0.47 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[CEBPD]] | -0.47 | -0.52 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*22 arrows, 22 of them with an alert ⚠; grade A 0, B 22, C 0. Shown: the 12 strongest; 10 more arrows (10 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CD59]] | B | CD59 activity raises ITPRID2's level | lines that do not express CD59 (7) vs lines expressing it (43) | 1.73× lower at baseline in the lines without CD59 | 0.012 | ⚠ within organs, on part of the lines; also absent: C11orf91, ENSG00000284969, MET; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity raises ITPRID2's level | compounds that target MAP2K1: 4 of 4 lower it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 4.2% of all compounds | 0.013 | ⚠ off-target possible; 4 compounds |
| [[SERPINE2]] | B | SERPINE2 activity raises ITPRID2's level | lines that do not express SERPINE2 (21) vs lines expressing it (29) | 1.59× lower at baseline in the lines without SERPINE2 | 0.017 | ⚠ within organs, on part of the lines; also absent: NMRAL2P-1, ZNF365, ADAM12 |
| [[ADAM19]] | B | ADAM19 activity raises ITPRID2's level | lines that do not express ADAM19 (13) vs lines expressing it (37) | 1.76× lower at baseline in the lines without ADAM19 | 0.022 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: ITGA1, ABLIM3, LBH |
| [[NT5E]] | B | NT5E activity raises ITPRID2's level | lines that do not express NT5E (14) vs lines expressing it (36) | 1.66× lower at baseline in the lines without NT5E | 0.022 | ⚠ within organs, on part of the lines; also absent: MDFIC, PAPSS2, ENSG00000289526 |
| [[PRKCA]] | B | PRKCA activity raises ITPRID2's level | lines that do not express PRKCA (5) vs lines expressing it (45) | 1.89× lower at baseline in the lines without PRKCA | 0.025 | ⚠ within organs, on part of the lines; also absent: TMEM51, ITGA2-AS1; maybe low, not absent |
| [[ITGA6]] | B | ITGA6 activity raises ITPRID2's level | lines that do not express ITGA6 (9) vs lines expressing it (41) | 1.48× lower at baseline in the lines without ITGA6 | 0.026 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[ITGA2]] | B | ITGA2 activity raises ITPRID2's level | lines that do not express ITGA2 (11) vs lines expressing it (39) | 1.83× lower at baseline in the lines without ITGA2 | 0.034 | ⚠ within organs, on part of the lines; also absent: GPR39, ATXN1-AS1, MET |
| [[MIR31HG]] | B | MIR31HG activity raises ITPRID2's level | lines that do not express MIR31HG (16) vs lines expressing it (34) | 1.54× lower at baseline in the lines without MIR31HG | 0.040 | ⚠ within organs, on part of the lines; also absent: SMCO2, POU5F1, PLA2R1 |
| [[CA2]] | B | CA2 activity raises ITPRID2's level | lines that do not express CA2 (27) vs lines expressing it (23) | 1.80× lower at baseline in the lines without CA2 | 0.040 | ⚠ within organs, on part of the lines; also absent: CCDC68, SCEL, MUC4 |
| [[CEMIP]] | B | CEMIP activity raises ITPRID2's level | lines that do not express CEMIP (19) vs lines expressing it (31) | 1.72× lower at baseline in the lines without CEMIP | 0.052 | ⚠ within organs, on part of the lines; also absent: PPARGC1A, DUSP4, SHC4 |
| [[ITGA2]] | B | ITGA2 activity strengthens ITPRID2's drug response | lines that do not express ITGA2 (10) vs lines expressing it (38) | the lines without ITGA2 respond 0.49× as strongly (z diff +1.74); strongest at Homoharringtonine 5 µM: 1.11x vs 0.64x (z diff +6.3) | 0.054 | ⚠ within organs, on part of the lines; also absent: GPR39, ATXN1-AS1, MET; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.628). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (40.9, 4.2); signed map (4.4, 42.9). **Vector** length 127, 40.5% of its response variance represented; |z| ≥ 3 in 1,521 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.9 | +6.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.5 | +4.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +7.4 | +1.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.7 | -0.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +4.3 | +4.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.2 | +1.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.1 | +3.4 |
|  | [[Tofacitinib (drug)]] 5 µM |  | +3.1 | +1.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.9 | +0.2 |
| fall | [[Trametinib (drug)]] 5 µM |  | -6.7 | -5.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -6.1 | -5.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -5.9 | -6.7 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -5.8 | -5.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -5.7 | -5.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | -5.6 | -5.7 |

## What is on record

|  |  |
|---|---|
| Name | ITPR interacting domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q31.3 — chr2:181,891,730-181,930,738 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CS-1, SPAG13, KRAP, KIAA1927; previously SSFA2 |
| Matched by | ensembl_id |

UniProt [P28290](https://www.uniprot.org/uniprotkb/P28290) carries no function annotation.

**Summary**, from NCBI Gene [6744](https://www.ncbi.nlm.nih.gov/gene/6744):

> Enables actin filament binding activity. Located in cytosol. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:11319](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11319) · Entrez [6744](https://www.ncbi.nlm.nih.gov/gene/6744) · UniProt [P28290](https://www.uniprot.org/uniprotkb/P28290) · Ensembl [ENSG00000138434](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138434)

## Data

Gene col 6175: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6175); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6175, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6175]; `tensor/DDL_lfc|DDL_z.npy` [6175]; `embed/gene_vectors.npy` [6175]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6175 or target_col == 6175). Every well: [[ITPRID2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ITPRID2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
