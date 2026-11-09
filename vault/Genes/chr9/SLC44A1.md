---
symbol: "SLC44A1"
type: "gene"
col: 943
ensembl_id: "ENSG00000070214"
name: "solute carrier family 44 member 1"
location: "9q31.1-q31.2"
module: 106
arm: "+"
pooled_cpm: 168.53
n_lines_expressing: 45
n_dd_up: 4
n_dd_down: 39
n_dd_up_clean: 2
n_dd_down_clean: 30
in_vector_space: true
direction_upstream: 3
direction_downstream: 5
tags: ["gene", "module/106"]
generated_by: "tahoemap"
---

# SLC44A1

*solute carrier family 44 member 1* — 9q31.1-q31.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.39× (z +13.5, q 1e-38, up in 34 of 43 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 13 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Clobetasol propionate (drug)]] 0.05 µM in 2 lines (hTERT-HPNE 3.00×, A549 2.67×); [[Triamcinolone (drug)]] 5 µM in 2 lines (hTERT-HPNE 2.14×, NCI-H1792 1.86×); [[Triamcinolone (drug)]] 0.5 µM in 2 lines (hTERT-HPNE 2.76×, NCI-H1792 2.46×).
> Pooled over the cell lines (median), lowered significantly by 39 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.478× (z -29.7, q 0e+00, down in 41 of 43 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SORT1]] (+0.63, fdr 1e-05), [[ADD3]] (+0.62, fdr 1e-05), [[LIFR]] (+0.59, fdr 1e-05); moves opposite to [[PLEKHN1]] (-0.64, fdr 1e-05), [[CLCF1]] (-0.57, fdr 3e-05), [[GPATCH2L]] (-0.55, fdr 3e-05).
> It is in [[Module 106]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 5 go from it, the strongest it → [[SPAG7]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 943.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 13 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Clobetasol propionate (drug)]] 0.05 µM in 2 lines (hTERT-HPNE 3.00×, A549 2.67×); [[Triamcinolone (drug)]] 5 µM in 2 lines (hTERT-HPNE 2.14×, NCI-H1792 1.86×); [[Triamcinolone (drug)]] 0.5 µM in 2 lines (hTERT-HPNE 2.76×, NCI-H1792 2.46×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.39×** | +13.5 | 1e-38 | 34/43 (SW480, SW1417, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.47×** | +10.7 | 3e-24 | 20/38 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.42×** | +10.0 | 2e-21 | 34/44 (SW480, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.39×** | +9.4 | 7e-19 | 26/44 (NCI-H1573, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.09× | +3.2 | 0.18 | 6/43 (AsPC-1, CFPAC-1, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 58 in all, 18 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 39 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 943.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.478×** | -29.7 | 0e+00 | 41/43 (NCI-H23, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.511×** | -27.0 | 0e+00 | 39/44 (NCI-H460, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.410×** | -25.3 | 0e+00 | 42/43 (A498, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.401×** | -25.0 | 0e+00 | 40/43 (A498, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.581×** | -15.4 | 0e+00 | 40/43 (SW 900, LoVo, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.579×** | -14.9 | 0e+00 | 37/42 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.593×** | -14.9 | 0e+00 | 36/43 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.606×** | -14.2 | 6e-44 | 39/43 (SW 900, A498, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.612×** | -13.9 | 3e-42 | 34/43 (RKO, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.619×** | -13.6 | 2e-40 | 36/43 (SW 900, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.650×** | -12.2 | 1e-32 | 34/43 (NCI-H1792, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.656×** | -11.9 | 4e-31 | 38/43 (A498, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.660×** | -11.8 | 2e-30 | 33/43 (NCI-H1792, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.453×** | -11.8 | 2e-30 | 37/44 (LoVo, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.664×** | -11.0 | 2e-26 | 36/43 (HEC-1-A, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.698×** | -10.2 | 8e-23 | 29/43 (SW480, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.709×** | -9.7 | 7e-21 | 31/43 (HepG2/C3A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 943. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[hTERT-HPNE (line)]] | wt | 182 | 16 | 10 (2 ⚠) | [[Clobetasol propionate (drug)]] 5 µM 3.21× (z +14.0) | [[Digitoxin (drug)]] 5 µM 0.346× (z -12.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.480× (z -12.4) |
| [[SW 900 (line)]] | alt | 215 | 6 | 18 (7 ⚠) | [[Clobetasol propionate (drug)]] 0.05 µM 2.48× (z +10.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.218× (z -23.8) |
| [[NCI-H1792 (line)]] | alt | 273 | 11 | 12 (3 ⚠) | [[Triamcinolone (drug)]] 0.5 µM 2.46× (z +11.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.258× (z -24.7) |
| [[NCI-H460 (line)]] | wt | 763 | 0 | 18 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.185× (z -33.8) |
| [[SW480 (line)]] | alt | 111 | 3 (1 ⚠) | 14 (3 ⚠) | [[Dinaciclib (drug)]] 5 µM 1.99× (z +11.6) ⚠ toxic; transcription drop · without an alert: [[Tucidinostat (drug)]] 5 µM 1.59× (z +11.4) | [[Auranofin (drug)]] 5 µM 0.402× (z -15.9) |
| [[A498 (line)]] | wt | 239 | 0 | 14 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.300× (z -26.9) |
| [[HS-578T (line)]] | alt | 136 | 0 | 14 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.225× (z -28.1) |
| [[LoVo (line)]] | wt | 211 | 0 | 14 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.417× (z -22.8) |
| [[RKO (line)]] | wt | 136 | 1 (1 ⚠) | 13 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.49× (z +9.7) ⚠ toxic; transcription drop | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.246× (z -14.9) |
| [[A549 (line)]] | wt | 115 | 5 | 8 (1 ⚠) | [[Clobetasol propionate (drug)]] 0.05 µM 2.67× (z +11.5) | [[Homoharringtonine (drug)]] 0.5 µM 0.185× (z -19.6) |
| [[HEC-1-A (line)]] | alt | 219 | 0 | 13 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.464× (z -21.2) |
| [[HepG2_C3A (line)]] | wt | 218 | 0 | 12 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.276× (z -21.0) |
| [[A-172 (line)]] | wt | 219 | 1 | 10 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.55× (z +10.5) | [[Homoharringtonine (drug)]] 5 µM 0.278× (z -30.1) |
| [[H4 (line)]] | wt | 200 | 0 | 9 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.186× (z -18.0) ⚠ cell-cycle shift, explains ~24% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.276× (z -13.8) |
| [[HT-29 (line)]] | alt | 186 | 0 | 9 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.412× (z -18.1) |
| [[LS 180 (line)]] | wt | 214 | 0 | 9 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.439× (z -16.1) |
| [[SNU-423 (line)]] | alt | 176 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -24.5) |
| [[HOP62 (line)]] | alt | 96.0 | 2 (2 ⚠) | 6 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.91× (z +8.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.314× (z -15.3) |
| [[J82 (line)]] | alt | 201 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.332× (z -26.2) |
| [[RPMI-7951 (line)]] | alt | 178 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.431× (z -15.8) |
| [[COLO 205 (line)]] | alt | 286 | 0 | 6 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.360× (z -17.0) |
| [[NCI-H1573 (line)]] | alt | 78.8 | 2 (2 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 2.54× (z +10.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.292× (z -14.0) |
| [[Panc 03.27 (line)]] | alt | 136 | 0 | 6 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.494× (z -13.4) |
| [[Hs 766T (line)]] | wt | 68.3 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.293× (z -17.5) |
| [[LOX-IMVI (line)]] | wt | 94.3 | 0 | 5 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.169× (z -22.6) |
| [[NCI-H23 (line)]] | alt | 63.4 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.135× (z -31.9) |
| [[NCI-H2347 (line)]] | alt | 141 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.390× (z -18.8) |
| [[SK-MEL-2 (line)]] | alt | 166 | 0 | 5 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.438× (z -14.3) |
| [[BT-474 (line)]] | alt | 95.4 | 0 | 4 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.362× (z -11.0) |
| [[HCT15 (line)]] | alt | 128 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.302× (z -12.3) |
| [[AsPC-1 (line)]] | alt | 108 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.418× (z -14.8) |
| [[CFPAC-1 (line)]] | alt | 93.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.448× (z -14.5) |
| [[CHP-212 (line)]] | wt | 192 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.197× (z -17.3) |
| [[KATO III (line)]] | alt | 136 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 1.81× (z +8.7) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.517× (z -13.6) |
| [[SW1417 (line)]] | alt | 204 | 1 | 2 | [[Tucidinostat (drug)]] 5 µM 1.61× (z +11.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.506× (z -15.8) |
| [[C32 (line)]] | wt | 170 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.276× (z -20.9) |
| [[SNU-1 (line)]] | wt | 63.1 | 1 | 1 | [[Retinoic acid (drug)]] 5 µM 2.62× (z +9.4) | [[Homoharringtonine (drug)]] 0.5 µM 0.175× (z -12.0) |
| [[SW48 (line)]] | wt | 121 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.433× (z -8.8) |
| [[A-427 (line)]] | wt | 36.9 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 35.5 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 107 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 40.4 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 35.1 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 150 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 190 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 96.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 35.8 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 79.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 161 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 77.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 943), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*54 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SORT1]] | +0.63 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[ADD3]] | +0.62 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[LIFR]] | +0.59 | +0.49 / +0.55 | both halves | 1e-05 | same gene group |
| [[HLTF]] | +0.58 | +0.44 / +0.57 | both halves | 3e-05 |  |
| [[PLSCR4]] | +0.58 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[MBNL1]] | +0.56 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[B4GALT1]] | +0.56 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[CPD]] | +0.55 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[ACSL1]] | +0.55 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[TMEM245]] | +0.54 | +0.46 / +0.48 | both halves | 3e-05 |  |
| [[PRKAR2B]] | +0.54 | +0.42 / +0.50 | both halves | 4e-05 |  |
| [[ALDH7A1]] | +0.54 | +0.46 / +0.48 | both halves | 2e-05 | pathway: Choline catabolism |

## Genes that move opposite

*46 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLEKHN1]] | -0.64 | -0.53 / -0.64 | both halves | 1e-05 |  |
| [[CLCF1]] | -0.57 | -0.44 / -0.58 | both halves | 3e-05 |  |
| [[GPATCH2L]] | -0.55 | -0.54 / -0.44 | both halves | 3e-05 |  |
| [[LTO1]] | -0.52 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[ZDHHC1]] | -0.52 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[IGHMBP2]] | -0.52 | -0.38 / -0.49 | both halves | 7e-05 |  |
| [[ZNF778]] | -0.52 | -0.35 / -0.45 | both halves | 1e-04 |  |
| [[USP36]] | -0.52 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[ZNF621]] | -0.52 | -0.53 / -0.42 | both halves | 4e-05 |  |
| [[SPAG7]] | -0.51 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[C10orf88]] | -0.51 | -0.39 / -0.48 | both halves | 5e-05 |  |
| [[COMMD5]] | -0.51 | -0.31 / -0.44 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises SLC44A1's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.6% of all compounds | 0.071 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SLC39A8]] | B | SLC39A8 activity raises SLC44A1's level | lines that do not express SLC39A8 (12) vs lines expressing it (38) | 1.84× lower at baseline in the lines without SLC39A8 | 0.073 | ⚠ within organs, on part of the lines; also absent: PLCB4, PAG1, RGS17 |
| [[ADD3]] | B | ADD3 activity raises SLC44A1's level | lines that do not express ADD3 (5) vs lines expressing it (45) | 2.11× lower at baseline in the lines without ADD3 | 0.094 | ⚠ within organs, on part of the lines; also absent: LINC02842, ADD3-AS1, WWC3 |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SPAG7]] | B | SLC44A1 activity lowers SPAG7's level | lines that do not express SLC44A1 (5) vs lines expressing it (45) | 1.44× higher at baseline in the lines without SLC44A1 | 0.041 | ⚠ within organs, on part of the lines; also absent: RALGPS2, PELI1, LINC00298; maybe low, not absent |
| [[B4GALT1]] | B | SLC44A1 activity raises B4GALT1's level | lines that do not express SLC44A1 (5) vs lines expressing it (45) | 2.28× lower at baseline in the lines without SLC44A1 | 0.060 | ⚠ within organs, on part of the lines; also absent: RALGPS2, PELI1, LINC00298; maybe low, not absent |
| [[ERLIN1]] | B | SLC44A1 activity lowers ERLIN1's level | lines that do not express SLC44A1 (5) vs lines expressing it (45) | 1.69× higher at baseline in the lines without SLC44A1 | 0.069 | ⚠ within organs, on part of the lines; also absent: RALGPS2, PELI1, LINC00298; maybe low, not absent |
| [[PAQR7]] | B | SLC44A1 activity lowers PAQR7's level | lines that do not express SLC44A1 (5) vs lines expressing it (45) | 2.24× higher at baseline in the lines without SLC44A1 | 0.092 | ⚠ within organs, on part of the lines; also absent: RALGPS2, PELI1, LINC00298; maybe low, not absent |
| [[CEP164]] | B | SLC44A1 activity lowers CEP164's level | lines that do not express SLC44A1 (5) vs lines expressing it (45) | 1.58× higher at baseline in the lines without SLC44A1 | 0.095 | ⚠ within organs, on part of the lines; also absent: RALGPS2, PELI1, LINC00298; maybe low, not absent |

## Where it sits

- **Module**: [[Module 106]]; 44 genes; every member is in the + arm (projection on the module's main direction 0.655). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.7, 5.9); signed map (-4.6, 19.3). **Vector** length 103, 31.2% of its response variance represented; |z| ≥ 3 in 1,775 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +10.3 | +13.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.9 | +10.0 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +5.2 | +2.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.7 | -1.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.7 | +1.9 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +3.7 | +0.8 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +3.3 | +0.9 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +2.9 | +1.4 |
| fall | [[Auranofin (drug)]] 5 µM |  | -6.7 | -15.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.7 | -9.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -5.7 | -14.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.5 | -27.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.9 | -14.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.7 | -5.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -4.1 | -3.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.3 | -4.8 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 44 member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q31.1-q31.2 — chr9:105,244,622-105,439,171 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CTL1, CHTL1, CD92; previously CDW92 |
| Gene groups (HGNC) | CD molecules; Solute carrier family 44 |
| Reactome | 10 pathways, smallest: SLC-mediated bile acid transport; Choline catabolism; SLC-mediated transport of organic anions |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WWI5](https://www.uniprot.org/uniprotkb/Q8WWI5) (Choline transporter-like protein 1):

> Choline/H+ antiporter. Also acts as a high-affinity ethanolamine/H+ antiporter, regulating the supply of extracellular ethanolamine (Etn) for the CDP-Etn pathway, redistribute intracellular Etn and balance the CDP-Cho and CDP-Etn arms of the Kennedy pathway. Involved in membrane synthesis and myelin production.

**Summary**, from NCBI Gene [23446](https://www.ncbi.nlm.nih.gov/gene/23446):

> Enables choline transmembrane transporter activity and ethanolamine transmembrane transporter activity. Involved in choline transport; ethanolamine transport; and transmembrane transport. Located in cytosol; mitochondrial outer membrane; and plasma membrane. Implicated in high grade glioma. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:18798](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18798) · Entrez [23446](https://www.ncbi.nlm.nih.gov/gene/23446) · UniProt [Q8WWI5](https://www.uniprot.org/uniprotkb/Q8WWI5) · Ensembl [ENSG00000070214](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000070214)

## Data

Gene col 943: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 943); `tables/drug_effects.parquet` (63 rows, flagged included); `relations/gene_relations.parquet` (col_a == 943, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 943]; `tensor/DDL_lfc|DDL_z.npy` [943]; `embed/gene_vectors.npy` [943]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 943 or target_col == 943). Every well: [[SLC44A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC44A1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
