---
symbol: "DPYSL3"
type: "gene"
col: 3490
ensembl_id: "ENSG00000113657"
name: "dihydropyrimidinase like 3"
location: "5q32"
module: 66
arm: "+"
pooled_cpm: 67.55
n_lines_expressing: 30
n_dd_up: 12
n_dd_down: 27
n_dd_up_clean: 7
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 14
direction_downstream: 10
tags: ["gene", "module/066"]
generated_by: "tahoemap"
---

# DPYSL3

*dihydropyrimidinase like 3* — 5q32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.28× (z +12.5, q 2e-33, up in 21 of 25 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Binimetinib (drug)]] 5 µM: 1.31× (z +4.2, q 0.003, up in 12 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.375× (z -21.0, q 0e+00, down in 23 of 28 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MOXD1]] (+0.64, fdr 1e-05), [[GXYLT2]] (+0.60, fdr 1e-05), [[TIMP3]] (+0.60, fdr 1e-05); moves opposite to [[ZBTB7A]] (-0.46, fdr 2e-04), [[SELENOH]] (-0.45, fdr 4e-04), [[PRRG2]] (-0.45, fdr 4e-05).
> It is in [[Module 066]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 14 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); 10 go from it, the strongest it → [[GGH]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3490.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.28×** | +12.5 | 2e-33 | 21/25 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.15×** | +12.1 | 2e-31 | 20/28 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.82×** | +8.8 | 3e-16 | 19/25 (A-172, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.34×** | +4.6 | 6e-04 | 14/28 (A-172, NCI-H460, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.31×** | +4.2 | 0.003 | 12/28 (A-172, Hs 766T, …) | rises with dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.26×** | +4.1 | 0.003 | 12/28 (Hs 766T, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | **1.26×** | +3.7 | 0.016 | 10/28 (A498, SW480, …) | all doses, flat |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~5% of this change | 1.19× | +3.7 | 0.017 | 10/28 (SW 900, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **1.22×** | +3.6 | 0.019 | 13/29 (A-172, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.20×** | +3.5 | 0.023 | 11/28 (HOP62, A-172, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.23×** | +3.3 | 0.047 | 10/27 (Hs 766T, HS-578T, …) | two highest doses |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | **1.23×** | +3.3 | 0.053 | 5/29 (SW480, RPMI-7951, …) | all doses, flat |  |
| [[Folic acid (drug)]] 5 µM |  | 1.15× | +3.1 | 0.093 | 8/28 (SW1417, CFPAC-1, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.21×** | +3.0 | 0.093 | 8/28 (HOP62, A-172, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3490.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.375×** | -21.0 | 0e+00 | 23/28 (NCI-H1792, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.529×** | -13.7 | 4e-40 | 25/28 (NCI-H1792, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.433×** | -13.2 | 9e-38 | 22/28 (C32, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.535×** | -9.5 | 3e-19 | 21/28 (SK-MEL-2, C32, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.574×** | -8.8 | 2e-16 | 22/28 (J82, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.599×** | -8.1 | 5e-14 | 22/28 (J82, A549, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.599×** | -7.8 | 6e-13 | 20/28 (SK-MEL-2, C32, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.617×** | -7.6 | 2e-12 | 19/28 (C32, SK-MEL-2, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.622×** | -7.5 | 4e-12 | 22/28 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.661×** | -6.5 | 3e-09 | 17/28 (A549, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.756×** | -6.0 | 1e-07 | 16/28 (A-172, NCI-H1792, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.749×** | -5.9 | 1e-07 | 20/28 (A-427, NCI-H460, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.703×** | -5.4 | 4e-06 | 16/29 (SK-MEL-2, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.710×** | -5.2 | 8e-06 | 14/27 (HS-578T, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.800×** | -4.7 | 9e-05 | 16/29 (SHP-77, Hs 766T, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.721×** | -4.6 | 1e-04 | 16/28 (A498, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.764×** | -4.2 | 8e-04 | 14/28 (C32, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~6% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3490. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 96.6 | 0 | 10 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0965× (z -27.7) |
| [[A-172 (line)]] | wt | 237 | 6 (4 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.63× (z +13.5) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 2.60× (z +9.7) | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.351× (z -11.0) |
| [[NCI-H1792 (line)]] | alt | 311 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0610× (z -31.9) |
| [[A498 (line)]] | wt | 247 | 3 (3 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.52× (z +12.6) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.420× (z -11.9) |
| [[HOP62 (line)]] | alt | 103 | 4 (4 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.42× (z +12.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -20.8) |
| [[HS-578T (line)]] | alt | 442 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -15.8) |
| [[SK-MEL-2 (line)]] | alt | 102 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.229× (z -18.5) |
| [[A549 (line)]] | wt | 61.6 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -14.7) |
| [[SHP-77 (line)]] | alt | 257 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -15.5) |
| [[A-427 (line)]] | wt | 35.1 | 1 (1 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.75× (z +9.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.260× (z -16.7) |
| [[SNU-423 (line)]] | alt | 109 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.51× (z +10.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.365× (z -11.8) |
| [[Hs 766T (line)]] | wt | 75.5 | 2 (1 ⚠) | 1 | [[Darinaparsin (drug)]] 5 µM 2.75× (z +8.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Binimetinib (drug)]] 0.5 µM 3.01× (z +8.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.331× (z -9.6) |
| [[J82 (line)]] | alt | 41.6 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.206× (z -15.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.325× (z -14.7) |
| [[NCI-H2030 (line)]] | alt | 44.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.134× (z -25.9) |
| [[NCI-H460 (line)]] | wt | 33.7 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.70× (z +9.1) ⚠ toxic; transcription drop | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.459× (z -9.7) |
| [[NCI-H23 (line)]] | alt | 24.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -11.2) |
| [[RPMI-7951 (line)]] | alt | 181 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -16.6) |
| [[SW 1271 (line)]] | alt | 65.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.102× (z -12.1) |
| [[CFPAC-1 (line)]] | alt | 76.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -19.1) |
| [[H4 (line)]] | wt | 95.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.186× (z -10.9) |
| [[hTERT-HPNE (line)]] | wt | 17.9 | 0 | 1 | — | [[Monocrotaline (drug)]] 0.05 µM 0.0774× (z -10.1) |
| [[LOX-IMVI (line)]] | wt | 43.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.451× (z -9.0) |
| [[Panc 03.27 (line)]] | alt | 19.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.72× (z +9.0) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 45.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +9.8) | — |
| [[SW480 (line)]] | alt | 48.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.451× (z -9.2) |
| [[AN3 CA (line)]] | alt | 8.35 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 4.67 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 10.4 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.78 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 50.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.21 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 10.4 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 4.19 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 4.71 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 6.43 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.99 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 5.98 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 4.02 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.69 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 12.5 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 48.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.50 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 50.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.94 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 4.34 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 4.32 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 4.92 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.97 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3490), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MOXD1]] | +0.64 | +0.49 / +0.65 | both halves | 1e-05 |  |
| [[GXYLT2]] | +0.60 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[TIMP3]] | +0.60 | +0.53 / +0.58 | both halves | 1e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[IGFBP5]] | +0.58 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[FBN1]] | +0.55 | +0.47 / +0.57 | both halves | 2e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[EDIL3]] | +0.54 | +0.53 / +0.54 | both halves | 1e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[SULF1]] | +0.54 | +0.47 / +0.47 | both halves | 2e-05 |  |
| [[RARB]] | +0.51 | +0.59 / +0.36 | both halves | 1e-04 |  |
| [[L1CAM]] | +0.51 | +0.48 / +0.46 | both halves | 3e-05 |  |
| [[NREP]] | +0.50 | +0.43 / +0.54 | both halves | 3e-05 |  |
| [[YWHAQ]] | +0.50 | +0.42 / +0.51 | both halves | 4e-05 |  |
| [[CDH6]] | +0.49 | +0.44 / +0.48 | both halves | 3e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |

## Genes that move opposite

*22 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZBTB7A]] | -0.46 | -0.32 / -0.51 | both halves | 2e-04 |  |
| [[SELENOH]] | -0.45 | -0.25 / -0.51 | both halves | 4e-04 |  |
| [[PRRG2]] | -0.45 | -0.44 / -0.41 | both halves | 4e-05 |  |
| [[SNX8]] | -0.44 | -0.41 / -0.40 | both halves | 5e-05 |  |
| [[ZNF791]] | -0.44 | -0.29 / -0.47 | both halves | 2e-04 |  |
| [[FAM98C]] | -0.44 | -0.35 / -0.43 | both halves | 1e-04 |  |
| [[TMEM101]] | -0.44 | -0.19 / -0.48 | ⚠ not reproduced | 8e-04 |  |
| [[EXD3]] | -0.44 | -0.42 / -0.36 | both halves | 1e-04 |  |
| [[FOXC2]] | -0.44 | -0.26 / -0.49 | both halves | 4e-04 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[FHL3]] | -0.44 | -0.39 / -0.46 | both halves | 5e-05 |  |
| [[MOSMO]] | -0.43 | -0.31 / -0.39 | both halves | 2e-04 |  |
| [[MRPL32]] | -0.43 | -0.26 / -0.46 | both halves | 4e-04 |  |
| [[HMGA1P4]] | -0.43 | -0.42 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 8, C 6. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers DPYSL3's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.0% of all compounds | 0.029 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[SESN3]] | B | SESN3 activity raises DPYSL3's level | lines that do not express SESN3 (20) vs lines expressing it (30) | 3.03× lower at baseline in the lines without SESN3 | 0.032 | ⚠ within organs, on part of the lines; also absent: EPHA4, GNG2, ST6GALNAC5; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity raises DPYSL3's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.6% of all compounds | 0.041 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[FZD1]] | B | FZD1 activity raises DPYSL3's level | lines that do not express FZD1 (6) vs lines expressing it (44) | 6.36× lower at baseline in the lines without FZD1 | 0.049 | ⚠ within organs, on part of the lines; also absent: TMOD2, SNPH, DNAI1; maybe low, not absent |
| [[HLTF]] | B | HLTF activity raises DPYSL3's level | lines that do not express HLTF (8) vs lines expressing it (42) | 6.67× lower at baseline in the lines without HLTF | 0.058 | ⚠ within organs, on part of the lines; also absent: HDGFL3, ZNF512B, FERMT2 |
| [[ANXA8]] | B | ANXA8 activity raises DPYSL3's level | lines that do not express ANXA8 (38) vs lines expressing it (12) | 2.85× lower at baseline in the lines without ANXA8 | 0.063 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PSG9, PSG1, KRT5 |
| [[MSX1]] | B | MSX1 activity raises DPYSL3's level | lines that do not express MSX1 (6) vs lines expressing it (44) | 3.41× lower at baseline in the lines without MSX1 | 0.079 | ⚠ within organs, on part of the lines; also absent: ANAPC1P4, WDR35, TMCC2; maybe low, not absent |
| [[MAP2K2]] | B | MAP2K2 activity lowers DPYSL3's level | compounds that target MAP2K2: 2 of 2 raise it (Binimetinib, Trametinib) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[ZMAT4]] | C | ZMAT4 activity raises DPYSL3's level | lines that do not express ZMAT4 (31) vs lines expressing it (19) | 4.96× lower at baseline in the lines without ZMAT4 | 0.033 | ⚠ within organs, on part of the lines; also absent: UBE2QL1, SHISAL1, SOX11; co-absent with the target |
| [[PCDHGC3]] | C | PCDHGC3 activity raises DPYSL3's level | lines that do not express PCDHGC3 (18) vs lines expressing it (32) | 5.54× lower at baseline in the lines without PCDHGC3 | 0.040 | ⚠ within organs, on part of the lines; also absent: ENSG00000259753, ITGB3, EGFEM1P; co-absent with the target |
| [[FOXC2]] | C | FOXC2 activity raises DPYSL3's level | lines that do not express FOXC2 (33) vs lines expressing it (17) | 4.03× lower at baseline in the lines without FOXC2 | 0.057 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KIRREL3, LINC01411, SIRLNT; co-absent with the target |
| [[NRP2]] | C | NRP2 activity raises DPYSL3's level | lines that do not express NRP2 (24) vs lines expressing it (26) | 3.24× lower at baseline in the lines without NRP2 | 0.068 | ⚠ within organs, on part of the lines; also absent: NLRP1, RFX8, TNFAIP6; co-absent with the target |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 6, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GGH]] | B | DPYSL3 activity raises GGH's level | lines that do not express DPYSL3 (20) vs lines expressing it (30) | 2.18× lower at baseline in the lines without DPYSL3 | 0.019 | ⚠ within organs, on part of the lines; also absent: SNAP25, SNAI2, ADAM7-AS1 |
| [[FZD1]] | B | DPYSL3 activity raises FZD1's level | lines that do not express DPYSL3 (20) vs lines expressing it (30) | 1.70× lower at baseline in the lines without DPYSL3 | 0.022 | ⚠ within organs, on part of the lines; also absent: SNAP25, SNAI2, ADAM7-AS1 |
| [[SESN3]] | B | DPYSL3 activity raises SESN3's level | lines that do not express DPYSL3 (20) vs lines expressing it (30) | 2.46× lower at baseline in the lines without DPYSL3 | 0.024 | ⚠ within organs, on part of the lines; also absent: SNAP25, SNAI2, ADAM7-AS1 |
| [[MSX1]] | B | DPYSL3 activity raises MSX1's level | lines that do not express DPYSL3 (20) vs lines expressing it (30) | 1.32× lower at baseline in the lines without DPYSL3 | 0.058 | ⚠ within organs, on part of the lines; also absent: SNAP25, SNAI2, ADAM7-AS1 |
| [[NREP]] | B | DPYSL3 activity raises NREP's level | lines that do not express DPYSL3 (20) vs lines expressing it (30) | 3.39× lower at baseline in the lines without DPYSL3 | 0.090 | ⚠ within organs, on part of the lines; also absent: SNAP25, SNAI2, ADAM7-AS1 |
| [[TTLL7]] | B | DPYSL3 activity raises TTLL7's level | lines that do not express DPYSL3 (20) vs lines expressing it (30) | 3.11× lower at baseline in the lines without DPYSL3 | 0.098 | ⚠ within organs, on part of the lines; also absent: SNAP25, SNAI2, ADAM7-AS1 |
| [[RARB]] | C | DPYSL3 activity raises RARB's level | lines that do not express DPYSL3 (20) vs lines expressing it (30) | 3.89× lower at baseline in the lines without DPYSL3 | 0.032 | ⚠ within organs, on part of the lines; also absent: SNAP25, SNAI2, ADAM7-AS1; co-absent with the target |
| [[PCDHGC3]] | C | DPYSL3 activity raises PCDHGC3's level | lines that do not express DPYSL3 (20) vs lines expressing it (30) | 3.05× lower at baseline in the lines without DPYSL3 | 0.050 | ⚠ within organs, on part of the lines; also absent: SNAP25, SNAI2, ADAM7-AS1; co-absent with the target |
| [[NRP2]] | C | DPYSL3 activity raises NRP2's level | lines that do not express DPYSL3 (20) vs lines expressing it (30) | 3.21× lower at baseline in the lines without DPYSL3 | 0.055 | ⚠ within organs, on part of the lines; also absent: SNAP25, SNAI2, ADAM7-AS1; co-absent with the target |
| [[CCDC80]] | C | DPYSL3 activity raises CCDC80's level | lines that do not express DPYSL3 (20) vs lines expressing it (30) | 4.13× lower at baseline in the lines without DPYSL3 | 0.067 | ⚠ within organs, on part of the lines; also absent: SNAP25, SNAI2, ADAM7-AS1; co-absent with the target |

## Where it sits

- **Module**: [[Module 066]] — epithelial mesenchymal transition; 74 genes; every member is in the + arm (projection on the module's main direction 0.546). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (51.0, 25.6); signed map (29.3, 42.7). **Vector** length 106, 29.3% of its response variance represented; |z| ≥ 3 in 1,078 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +9.3 | +12.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +8.6 | +8.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.6 | +12.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.0 | +2.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.9 | +2.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.6 | +3.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.5 | +4.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.1 | +2.9 |
| fall | [[Triamcinolone (drug)]] 5 µM |  | -2.8 | -3.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.7 | -7.6 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.4 | -2.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.3 | -3.1 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | -1.2 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -2.2 | -3.2 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -2.0 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | dihydropyrimidinase like 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q32 — chr5:147,390,808-147,510,068 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DRP-3, ULIP, CRMP4 |
| Gene groups (HGNC) | M38 metallopeptidases |
| Hallmark sets | EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 4 pathways, smallest: CRMPs in Sema3A signaling; Semaphorin interactions; Axon guidance |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14195](https://www.uniprot.org/uniprotkb/Q14195) (Dihydropyrimidinase-related protein 3):

> Necessary for signaling by class 3 semaphorins and subsequent remodeling of the cytoskeleton. Plays a role in axon guidance, neuronal growth cone collapse and cell migration (By similarity).

**Summary**, from NCBI Gene [1809](https://www.ncbi.nlm.nih.gov/gene/1809):

> Enables filamin binding activity. Predicted to be involved in several processes, including actin filament organization; regulation of plasma membrane bounded cell projection organization; and response to axon injury. Predicted to act upstream of or within nervous system development. Predicted to be located in several cellular components, including exocytic vesicle; lamellipodium; and obsolete extracellular space. Predicted to be part of filamentous actin. Predicted to be active in cytosol. …

**Accessions** — [HGNC:3015](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3015) · Entrez [1809](https://www.ncbi.nlm.nih.gov/gene/1809) · UniProt [Q14195](https://www.uniprot.org/uniprotkb/Q14195) · Ensembl [ENSG00000113657](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000113657)

## Data

Gene col 3490: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3490); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3490, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3490]; `tensor/DDL_lfc|DDL_z.npy` [3490]; `embed/gene_vectors.npy` [3490]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3490 or target_col == 3490). Every well: [[DPYSL3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DPYSL3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
