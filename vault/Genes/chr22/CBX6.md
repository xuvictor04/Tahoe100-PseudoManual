---
symbol: "CBX6"
type: "gene"
col: 11446
ensembl_id: "ENSG00000183741"
name: "chromobox 6"
location: "22q13.1"
module: 207
arm: "-"
pooled_cpm: 28.92
n_lines_expressing: 49
n_dd_up: 24
n_dd_down: 1
n_dd_up_clean: 11
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/207"]
generated_by: "tahoemap"
---

# CBX6

*chromobox 6* — 22q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.13× (z +13.0, q 8e-36, up in 39 of 43 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.97× (z +7.7, q 2e-12, up in 38 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.666× (z -6.6, q 2e-08, down in 31 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 7 lines (MIA PaCa-2 0.229×, SW480 0.402×, NCI-H23 0.364×, SW1417 0.376×, …); [[Homoharringtonine (drug)]] 5 µM in 2 lines (C32 0.198×, SK-MEL-2 0.327×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (C32 0.114×; ⚠ cell-cycle shift, explains ~23% of this change); [[Clotrimazole (drug)]] 5 µM in 1 line (NCI-H661 0.135×).
> Its strongest partners by |cos| (92 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NAA40]] (+0.57, fdr 7e-05), [[CENPB]] (+0.54, fdr 4e-05), [[KIAA0930]] (+0.52, fdr 3e-05); moves opposite to [[IKZF4]] (-0.55, fdr 1e-04), [[SUOX]] (-0.52, fdr 1e-04), [[RECQL5]] (-0.51, fdr 2e-04).
> It sits in the **-** arm of [[Module 207]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TMOD2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 13 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11446.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **3.13×** | +13.0 | 8e-36 | 39/43 (A498, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.03×** | +12.1 | 2e-31 | 32/35 (NCI-H1792, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **2.10×** | +7.8 | 1e-12 | 31/40 (SNU-423, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.97×** | +7.7 | 2e-12 | 38/47 (SW480, A-427, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.61×** | +7.7 | 2e-12 | 38/47 (A498, HT-29, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.93×** | +7.5 | 6e-12 | 40/47 (HS-578T, HOP62, …) | all doses, flat | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.81×** | +6.7 | 1e-09 | 35/47 (HS-578T, HOP62, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.76×** | +6.2 | 4e-08 | 35/44 (SNU-423, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.70×** | +6.0 | 1e-07 | 34/47 (HS-578T, HOP62, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.70×** | +6.0 | 1e-07 | 36/46 (HEC-1-A, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **1.68×** | +5.9 | 2e-07 | 32/45 (HEC-1-A, NCI-H1573, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~30% of this change | **1.67×** | +5.8 | 3e-07 | 34/45 (HOP62, HS-578T, …) | inconsistent across doses | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.65×** | +5.7 | 6e-07 | 32/47 (HEC-1-A, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.58×** | +5.2 | 8e-06 | 32/47 (HS-578T, HOP62, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.53×** | +4.8 | 6e-05 | 27/47 (HS-578T, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~19% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.42×** | +4.0 | 0.002 | 26/47 (A498, HS-578T, …) | inconsistent across doses | position effect removed |
| [[vincristine (drug)]] 0.5 µM |  | **1.53×** | +3.4 | 0.017 | 17/46 (SK-MEL-2, CFPAC-1, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.39×** | +3.4 | 0.017 | 22/46 (A498, NCI-H2030, …) | all doses, flat | low cells (technical?); position effect removed |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.34×** | +3.4 | 0.022 | 22/47 (CFPAC-1, BT-474, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.33×** | +3.2 | 0.034 | 16/46 (CFPAC-1, NCI-H460, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11446.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 7 lines (MIA PaCa-2 0.229×, SW480 0.402×, NCI-H23 0.364×, SW1417 0.376×, …); [[Homoharringtonine (drug)]] 5 µM in 2 lines (C32 0.198×, SK-MEL-2 0.327×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (C32 0.114×; ⚠ cell-cycle shift, explains ~23% of this change); [[Clotrimazole (drug)]] 5 µM in 1 line (NCI-H661 0.135×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.666×** | -6.6 | 2e-08 | 31/47 (MIA PaCa-2, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.27 per unit of S-phase module lfc, +0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11446. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 22.1 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.29× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[Hs 766T (line)]] | wt | 23.7 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 6.35× (z +10.6) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.302× (z -10.1) |
| [[MIA PaCa-2 (line)]] | alt | 38.7 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.71× (z +12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.229× (z -14.7) |
| [[SNU-423 (line)]] | alt | 13.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 11.3× (z +11.4) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 42.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.22× (z +12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[C32 (line)]] | wt | 33.1 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -14.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 29.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.73× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[HOP62 (line)]] | alt | 17.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.59× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[NCI-H1792 (line)]] | alt | 17.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 12.5× (z +12.8) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 33.8 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.364× (z -10.7) |
| [[PANC-1 (line)]] | alt | 28.8 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.98× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.458× (z -8.5) |
| [[RPMI-7951 (line)]] | alt | 22.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.43× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[A-172 (line)]] | wt | 9.38 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.5× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[HepG2_C3A (line)]] | wt | 18.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.97× (z +10.9) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[KATO III (line)]] | alt | 45.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.03× (z +8.5) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 31.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.374× (z -10.1) |
| [[LOX-IMVI (line)]] | wt | 24.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.85× (z +9.3) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 68.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.74× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[NCI-H460 (line)]] | wt | 13.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.56× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[NCI-H661 (line)]] | alt | 34.2 | 0 | 1 | — | [[Clotrimazole (drug)]] 5 µM 0.135× (z -9.0) |
| [[SHP-77 (line)]] | alt | 31.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.54× (z +10.1) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 49.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -11.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 39.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.376× (z -10.4) |
| [[SW480 (line)]] | alt | 37.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.402× (z -11.7) |
| [[A-427 (line)]] | wt | 25.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 22.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.73 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 27.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 22.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.86 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 36.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 57.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 63.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11446), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NAA40]] | +0.57 | +0.37 / +0.59 | both halves | 7e-05 |  |
| [[CENPB]] | +0.54 | +0.64 / +0.42 | both halves | 4e-05 |  |
| [[KIAA0930]] | +0.52 | +0.45 / +0.50 | both halves | 3e-05 |  |
| [[ATP6V0A1]] | +0.51 | +0.34 / +0.57 | both halves | 1e-04 |  |
| [[NBEA]] | +0.51 | +0.54 / +0.39 | both halves | 6e-05 | pathway: Intracellular signaling by second messengers |
| [[MRTFB]] | +0.50 | +0.50 / +0.46 | both halves | 3e-05 |  |
| [[SLC23A2]] | +0.50 | +0.35 / +0.43 | both halves | 1e-04 |  |
| [[COBL]] | +0.50 | +0.44 / +0.41 | both halves | 4e-05 |  |
| [[DTNB]] | +0.49 | +0.46 / +0.49 | both halves | 2e-05 |  |
| [[DVL1]] | +0.49 | +0.27 / +0.40 | both halves | 3e-04 |  |
| [[DNAH14]] | +0.49 | +0.44 / +0.58 | both halves | 3e-05 |  |
| [[CELF1]] | +0.48 | +0.38 / +0.41 | both halves | 7e-05 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IKZF4]] | -0.55 | -0.35 / -0.49 | both halves | 1e-04 |  |
| [[SUOX]] | -0.52 | -0.34 / -0.40 | both halves | 1e-04 |  |
| [[RECQL5]] | -0.51 | -0.32 / -0.48 | both halves | 2e-04 |  |
| [[PMS2P4-1]] | -0.51 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[RAB27A]] | -0.51 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[GLE1]] | -0.50 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[ZNF451]] | -0.50 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[CRLS1]] | -0.49 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[ICAM3]] | -0.49 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[SPAG4]] | -0.49 | -0.29 / -0.47 | both halves | 3e-04 |  |
| [[DYRK4]] | -0.49 | -0.34 / -0.43 | both halves | 1e-04 |  |
| [[YME1L1]] | -0.48 | -0.42 / -0.45 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMOD2]] | B | TMOD2 activity raises CBX6's level | lines that do not express TMOD2 (6) vs lines expressing it (44) | 1.70× lower at baseline in the lines without TMOD2 | 0.087 | ⚠ within organs, on part of the lines; also absent: CCDC102A, CYP46A1, FZD1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 207]]; 15 genes; this gene is in the **-** arm (projection on the module's main direction -0.629). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.36).
- **Nodal map** (x, y) = (-20.5, 28.5); signed map (9.6, -48.6). **Vector** length 88.4, 22.3% of its response variance represented; |z| ≥ 3 in 992 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.1 | +7.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.1 | +5.7 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.7 | +7.5 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.6 | +6.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.4 | +2.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.6 | +7.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.1 | +2.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.1 | +1.6 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -12.1 | -6.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.5 | +0.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.8 | -0.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.6 | -0.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | -0.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.6 | +0.1 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -1.9 | +0.1 |
|  | [[Budesonide (drug)]] 0.5 µM |  | -1.3 | -1.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.3 | +0.8 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.3 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | chromobox 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.1 — chr22:38,861,422-38,872,249 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Chromobox family |
| Reactome | 12 pathways, smallest: RUNX1 interacts with co-factors whose precise effect on RUNX1 targets is not known; Regulation of PTEN gene transcription; Differentiation of naive CD4+ T cells to T helper 2 cells (Th2 cells) |
| Matched by | ensembl_id |

**Function**, from UniProt [O95503](https://www.uniprot.org/uniprotkb/O95503) (Chromobox protein homolog 6):

> Component of a Polycomb group (PcG) multiprotein PRC1-like complex, a complex class required to maintain the transcriptionally repressive state of many genes, including Hox genes, throughout development. PcG PRC1 complex acts via chromatin remodeling and modification of histones; it mediates monoubiquitination of histone H2A 'Lys-119', rendering chromatin heritably changed in its expressibility. Possibly contributes to the target selectivity of the PRC1 complex by binding specific regions of …

**Summary**, from NCBI Gene [23466](https://www.ncbi.nlm.nih.gov/gene/23466):

> Predicted to enable chromatin binding activity. Involved in negative regulation of transcription by RNA polymerase II. Located in nuclear body. Part of PcG protein complex. Biomarker of glioblastoma. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:1556](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1556) · Entrez [23466](https://www.ncbi.nlm.nih.gov/gene/23466) · UniProt [O95503](https://www.uniprot.org/uniprotkb/O95503) · Ensembl [ENSG00000183741](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183741)

## Data

Gene col 11446: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11446); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11446, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11446]; `tensor/DDL_lfc|DDL_z.npy` [11446]; `embed/gene_vectors.npy` [11446]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11446 or target_col == 11446). Every well: [[CBX6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CBX6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
