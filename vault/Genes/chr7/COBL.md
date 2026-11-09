---
symbol: "COBL"
type: "gene"
col: 2719
ensembl_id: "ENSG00000106078"
name: "cordon-bleu WH2 repeat protein"
location: "7p12.1"
module: 197
arm: "+"
pooled_cpm: 96.41
n_lines_expressing: 27
n_dd_up: 13
n_dd_down: 14
n_dd_up_clean: 9
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 21
direction_downstream: 24
tags: ["gene", "module/197"]
generated_by: "tahoemap"
---

# COBL

*cordon-bleu WH2 repeat protein* — 7p12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.46× (z +12.0, q 2e-30, up in 17 of 25 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.637× (z -14.3, q 2e-43, down in 22 of 26 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRAK1]] (+0.65, fdr 1e-05), [[LINC02595]] (+0.63, fdr 7e-06), [[CARMIL1]] (+0.62, fdr 1e-05); moves opposite to [[PPIL3]] (-0.57, fdr 1e-05), [[ZNF490]] (-0.53, fdr 3e-05), [[IKZF4]] (-0.51, fdr 6e-05).
> It is in [[Module 197]], a single-armed module (Nervous system development).
> Probable direction (from the cell lines, not proof of direct regulation): 21 arrows point to it, the strongest [[RAPGEF5]] → it (grade B ⚠); 24 go from it, the strongest it → [[WWC1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2719.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.46×** | +12.0 | 2e-30 | 17/25 (CFPAC-1, NCI-H2030, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.49×** | +8.7 | 8e-16 | 14/25 (NCI-H2347, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.38×** | +7.4 | 4e-11 | 13/26 (MIA PaCa-2, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.26×** | +6.0 | 2e-07 | 12/25 (NCI-H460, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.27×** | +5.5 | 5e-06 | 13/25 (HCT15, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.19× | +5.4 | 5e-06 | 9/26 (CFPAC-1, HepG2/C3A, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.26×** | +5.2 | 2e-05 | 11/25 (AsPC-1, SW480, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.25×** | +5.1 | 2e-05 | 11/25 (NCI-H1573, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.23×** | +4.6 | 2e-04 | 10/25 (CFPAC-1, HepG2/C3A, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.23×** | +4.3 | 9e-04 | 7/24 (AsPC-1, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **1.21×** | +4.2 | 0.002 | 15/25 (NCI-H460, AsPC-1, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.20× | +4.1 | 0.002 | 13/25 (HT-29, A549, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.52×** | +4.1 | 0.002 | 11/26 (A-427, NCI-H2030, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.19× | +3.9 | 0.004 | 5/26 (AsPC-1, CFPAC-1, …) | all doses, flat | composition shift |
| [[Binimetinib (drug)]] 5 µM |  | 1.19× | +3.8 | 0.006 | 10/26 (NCI-H460, NCI-H2347, …) | rises with dose | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | 1.18× | +3.7 | 0.008 | 14/25 (CFPAC-1, A-427, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.15× | +3.7 | 0.008 | 10/25 (NCI-H460, NCI-H2347, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 1.16× | +3.3 | 0.027 | 8/25 (NCI-H460, AsPC-1, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.11× | +3.3 | 0.027 | 8/25 (BT-474, A-427, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 11 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2719.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.637×** | -14.3 | 2e-43 | 22/26 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.664×** | -9.2 | 9e-18 | 17/25 (SW480, LoVo, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.665×** | -9.2 | 9e-18 | 19/25 (SW48, SW480, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.751×** | -9.0 | 4e-17 | 19/25 (SW48, LoVo, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.682×** | -8.3 | 1e-14 | 20/25 (NCI-H1573, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.793×** | -7.3 | 3e-11 | 14/25 (Panc 03.27, SW480, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Artesunate (drug)]] 5 µM |  | **0.805×** | -6.8 | 9e-10 | 15/25 (KATO III, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.774×** | -5.8 | 6e-07 | 15/25 (SW480, MIA PaCa-2, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.798×** | -5.1 | 3e-05 | 13/25 (RKO, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.825×** | -4.2 | 0.002 | 11/25 (RKO, MIA PaCa-2, …) | rises with dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.826×** | -4.1 | 0.002 | 17/25 (SW480, SW48, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | 0.837× | -4.0 | 0.003 | 15/25 (SW1417, NCI-H2347, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.779×** | -4.0 | 0.003 | 11/25 (LoVo, SW1417, …) | two highest doses | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 5 µM |  | 0.883× | -3.9 | 0.004 | 6/25 (HEC-1-A, HT-29, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | 0.836× | -3.9 | 0.004 | 17/27 (SW480, KATO III, …) | top dose only |  |
| [[Dihydroartemisinin (drug)]] 0.5 µM |  | 0.854× | -3.5 | 0.012 | 3/25 (KATO III, BT-474, …) | two highest doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.696×** | -3.5 | 0.013 | 12/26 (HEC-1-A, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Artesunate (drug)]] 0.5 µM |  | 0.855× | -3.5 | 0.013 | 4/25 (HCT15, NCI-H460, …) | rises with dose |  |
| [[Triamcinolone (drug)]] 5 µM |  | 0.895× | -3.5 | 0.014 | 2/25 (AsPC-1, NCI-H1573) | top dose only |  |
| [[TAK-733 (drug)]] 0.05 µM |  | **0.827×** | -2.9 | 0.080 | 1/25 (LoVo) | inconsistent across doses | noisy plate (z scaled) |
| [[Retinoic acid (drug)]] 5 µM |  | 0.912× | -2.9 | 0.094 | 5/26 (KATO III, COLO 205, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2719. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW48 (line)]] | wt | 231 | 0 | 10 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -22.7) |
| [[SW480 (line)]] | alt | 363 | 0 | 9 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.261× (z -22.9) |
| [[HEC-1-A (line)]] | alt | 141 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.419× (z -16.5) |
| [[KATO III (line)]] | alt | 487 | 0 | 7 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.236× (z -20.1) |
| [[MIA PaCa-2 (line)]] | alt | 38.7 | 1 | 6 (5 ⚠) | [[Auranofin (drug)]] 5 µM 4.15× (z +11.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.306× (z -13.4) |
| [[LoVo (line)]] | wt | 305 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -21.2) |
| [[SW1417 (line)]] | alt | 306 | 0 | 6 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.258× (z -21.3) |
| [[HepG2_C3A (line)]] | wt | 120 | 4 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +10.2) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.232× (z -12.2) ⚠ toxic |
| [[NCI-H460 (line)]] | wt | 67.8 | 5 | 0 | [[Cobimetinib (drug)]] 5 µM 3.24× (z +10.0) | — |
| [[Panc 03.27 (line)]] | alt | 205 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.301× (z -16.4) |
| [[RKO (line)]] | wt | 81.3 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.344× (z -14.3) |
| [[AsPC-1 (line)]] | alt | 117 | 2 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.60× (z +11.3) ⚠ cell-cycle shift, explains ~0% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.222× (z -12.8) ⚠ toxic |
| [[BT-474 (line)]] | alt | 295 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.428× (z -13.3) |
| [[NCI-H1573 (line)]] | alt | 94.6 | 0 | 3 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.249× (z -13.2) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.328× (z -11.0) |
| [[LS 180 (line)]] | wt | 186 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.353× (z -14.6) |
| [[A-427 (line)]] | wt | 106 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.00× (z +8.6) | — |
| [[CFPAC-1 (line)]] | alt | 37.2 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.07× (z +8.7) | — |
| [[COLO 205 (line)]] | alt | 53.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.169× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 106 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.445× (z -8.8) |
| [[HT-29 (line)]] | alt | 71.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.392× (z -10.1) |
| [[NCI-H2030 (line)]] | alt | 43.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.467× (z -9.8) |
| [[NCI-H2347 (line)]] | alt | 90.5 | 1 (1 ⚠) | 0 | [[Trametinib (drug)]] 5 µM 2.39× (z +8.8) ⚠ cell-cycle shift, explains ~35% of this change | — |
| [[A-172 (line)]] | wt | 16.4 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 12.6 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 50.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 55.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 44.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.89 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 10.7 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 11.1 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 9.07 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 6.93 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 8.54 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.1 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 6.59 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 10.7 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 17.0 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 85.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 18.3 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.1 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 7.14 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 8.01 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 16.6 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.00 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 9.17 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 14.2 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 16.5 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 20.0 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 12.6 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2719), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRAK1]] | +0.65 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[LINC02595]] | +0.63 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[CARMIL1]] | +0.62 | +0.70 / +0.52 | both halves | 1e-05 |  |
| [[WWC1]] | +0.60 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[PLCE1]] | +0.59 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[ABLIM1]] | +0.57 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[CLIC5]] | +0.55 | +0.43 / +0.57 | both halves | 3e-05 |  |
| [[RAB15]] | +0.54 | +0.57 / +0.40 | both halves | 5e-05 |  |
| [[PLEKHA7]] | +0.54 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[SAMD12]] | +0.54 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[JPH1]] | +0.54 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[TBC1D1]] | +0.53 | +0.65 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPIL3]] | -0.57 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[ZNF490]] | -0.53 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[IKZF4]] | -0.51 | -0.51 / -0.38 | both halves | 6e-05 |  |
| [[ZSWIM3]] | -0.51 | -0.49 / -0.42 | both halves | 4e-05 |  |
| [[KRBOX4]] | -0.51 | -0.49 / -0.42 | both halves | 4e-05 |  |
| [[GLE1]] | -0.50 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[ARHGAP1]] | -0.49 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[CUL7]] | -0.49 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[EPOR]] | -0.48 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[TXNL4B]] | -0.47 | -0.35 / -0.41 | both halves | 1e-04 |  |
| [[YJU2B]] | -0.47 | -0.49 / -0.42 | both halves | 4e-05 |  |
| [[FBXL12]] | -0.47 | -0.35 / -0.50 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*21 arrows, 21 of them with an alert ⚠; grade A 0, B 7, C 14. Shown: the 12 strongest; 9 more arrows (9 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RAPGEF5]] | B | RAPGEF5 activity raises COBL's level | lines that do not express RAPGEF5 (17) vs lines expressing it (33) | 3.43× lower at baseline in the lines without RAPGEF5 | 0.015 | ⚠ within organs, on part of the lines; also absent: HSH2D, HOOK1, SAMD12; maybe low, not absent |
| [[WWC1]] | B | WWC1 activity raises COBL's level | lines that do not express WWC1 (13) vs lines expressing it (37) | 3.80× lower at baseline in the lines without WWC1 | 0.048 | ⚠ within organs, on part of the lines; also absent: SH2D3A, CHMP4C, LSR; maybe low, not absent |
| [[MTUS1]] | B | MTUS1 activity raises COBL's level | lines that do not express MTUS1 (17) vs lines expressing it (33) | 3.59× lower at baseline in the lines without MTUS1 | 0.052 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, SHROOM3, ELF3 |
| [[STON2]] | B | STON2 activity raises COBL's level | lines that do not express STON2 (19) vs lines expressing it (31) | 2.25× lower at baseline in the lines without STON2 | 0.072 | ⚠ within organs, on part of the lines; also absent: FRK, RASSF6, AQP3 |
| [[SAMD12]] | B | SAMD12 activity raises COBL's level | lines that do not express SAMD12 (20) vs lines expressing it (30) | 3.48× lower at baseline in the lines without SAMD12 | 0.082 | ⚠ within organs, on part of the lines; also absent: MST1R, STYK1, ENSG00000263325 |
| [[XK]] | B | XK activity raises COBL's level | lines that do not express XK (18) vs lines expressing it (32) | 2.53× lower at baseline in the lines without XK | 0.085 | ⚠ within organs, on part of the lines; also absent: SAMD12, MARVELD2, BTC; maybe low, not absent |
| [[DENND2D]] | B | DENND2D activity raises COBL's level | lines that do not express DENND2D (21) vs lines expressing it (29) | 2.87× lower at baseline in the lines without DENND2D | 0.097 | ⚠ within organs, on part of the lines; also absent: SAMD12, SLC52A3, AREG |
| [[ST14]] | C | ST14 activity raises COBL's level | lines that do not express ST14 (32) vs lines expressing it (18) | 7.54× lower at baseline in the lines without ST14 | 5e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, TMEM125, CDH1; co-absent with the target |
| [[MISP]] | C | MISP activity raises COBL's level | lines that do not express MISP (23) vs lines expressing it (27) | 6.20× lower at baseline in the lines without MISP | 0.001 | ⚠ within organs, on part of the lines; also absent: GRB7, KRT18, MYO5B; co-absent with the target |
| [[LINC02331]] | C | LINC02331 activity raises COBL's level | lines that do not express LINC02331 (30) vs lines expressing it (20) | 6.47× lower at baseline in the lines without LINC02331 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KDF1, EPS8L3, LCN2; co-absent with the target |
| [[TMPRSS2]] | C | TMPRSS2 activity raises COBL's level | lines that do not express TMPRSS2 (35) vs lines expressing it (15) | 6.26× lower at baseline in the lines without TMPRSS2 | 0.004 | ⚠ within organs, on part of the lines; also absent: SLC5A1, ARHGEF38, ITGB6; co-absent with the target |
| [[C6orf132]] | C | C6orf132 activity raises COBL's level | lines that do not express C6orf132 (27) vs lines expressing it (23) | 5.30× lower at baseline in the lines without C6orf132 | 0.005 | ⚠ within organs, on part of the lines; also absent: PCSK9, RNF223, CDH1; co-absent with the target |

### Downstream of this gene

*24 arrows, 24 of them with an alert ⚠; grade A 0, B 11, C 13. Shown: the 12 strongest; 12 more arrows (12 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[WWC1]] | B | COBL activity raises WWC1's level | lines that do not express COBL (23) vs lines expressing it (27) | 3.41× lower at baseline in the lines without COBL | 0.008 | ⚠ within organs, on part of the lines; also absent: MARVELD3, CRB3, GRB7 |
| [[PLEKHA7]] | B | COBL activity raises PLEKHA7's level | lines that do not express COBL (23) vs lines expressing it (27) | 3.37× lower at baseline in the lines without COBL | 0.024 | ⚠ within organs, on part of the lines; also absent: MARVELD3, CRB3, GRB7 |
| [[ANXA11]] | B | COBL activity raises ANXA11's level | lines that do not express COBL (23) vs lines expressing it (27) | 2.33× lower at baseline in the lines without COBL | 0.033 | ⚠ within organs, on part of the lines; also absent: MARVELD3, CRB3, GRB7 |
| [[MTUS1]] | B | COBL activity raises MTUS1's level | lines that do not express COBL (23) vs lines expressing it (27) | 3.50× lower at baseline in the lines without COBL | 0.034 | ⚠ within organs, on part of the lines; also absent: MARVELD3, CRB3, GRB7 |
| [[LYN]] | B | COBL activity raises LYN's level | lines that do not express COBL (23) vs lines expressing it (27) | 2.13× lower at baseline in the lines without COBL | 0.054 | ⚠ within organs, on part of the lines; also absent: MARVELD3, CRB3, GRB7 |
| [[ARAP2]] | B | COBL activity raises ARAP2's level | lines that do not express COBL (23) vs lines expressing it (27) | 3.11× lower at baseline in the lines without COBL | 0.071 | ⚠ within organs, on part of the lines; also absent: MARVELD3, CRB3, GRB7 |
| [[SPATA13]] | B | COBL activity raises SPATA13's level | lines that do not express COBL (23) vs lines expressing it (27) | 2.22× lower at baseline in the lines without COBL | 0.078 | ⚠ within organs, on part of the lines; also absent: MARVELD3, CRB3, GRB7 |
| [[GCLC]] | B | COBL activity raises GCLC's level | lines that do not express COBL (23) vs lines expressing it (27) | 2.50× lower at baseline in the lines without COBL | 0.086 | ⚠ within organs, on part of the lines; also absent: MARVELD3, CRB3, GRB7 |
| [[CARMIL1]] | B | COBL activity raises CARMIL1's level | lines that do not express COBL (23) vs lines expressing it (27) | 2.42× lower at baseline in the lines without COBL | 0.092 | ⚠ within organs, on part of the lines; also absent: MARVELD3, CRB3, GRB7 |
| [[PLPP2]] | B | COBL activity raises PLPP2's level | lines that do not express COBL (23) vs lines expressing it (27) | 1.79× lower at baseline in the lines without COBL | 0.094 | ⚠ within organs, on part of the lines; also absent: MARVELD3, CRB3, GRB7 |
| [[TXNRD1]] | B | COBL activity raises TXNRD1's level | lines that do not express COBL (23) vs lines expressing it (27) | 1.56× lower at baseline in the lines without COBL | 0.096 | ⚠ within organs, on part of the lines; also absent: MARVELD3, CRB3, GRB7 |
| [[MISP]] | C | COBL activity raises MISP's level | lines that do not express COBL (23) vs lines expressing it (27) | 5.95× lower at baseline in the lines without COBL | 4e-04 | ⚠ within organs, on part of the lines; also absent: MARVELD3, CRB3, GRB7; co-absent with the target |

## Where it sits

- **Module**: [[Module 197]] — Nervous system development; 16 genes; every member is in the + arm (projection on the module's main direction 0.589). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.45; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (11.3, 43.7); signed map (50.5, 16.3). **Vector** length 98.9, 30.7% of its response variance represented; |z| ≥ 3 in 809 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.4 | +12.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +4.8 | +8.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +4.7 | +3.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.7 | +7.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.4 | +2.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.2 | +4.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.1 | +6.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.7 | +3.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.5 | +4.2 |
| fall | [[Artesunate (drug)]] 5 µM |  | -3.4 | -6.8 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.5 | -1.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.3 | -3.5 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.2 | -4.0 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -2.2 | -2.9 |
|  | [[Belzutifan (drug)]] 5 µM |  | -1.7 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | cordon-bleu WH2 repeat protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p12.1 — chr7:51,016,212-51,316,818 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0633 |
| Matched by | ensembl_id |

**Function**, from UniProt [O75128](https://www.uniprot.org/uniprotkb/O75128) (Protein cordon-bleu):

> Plays an important role in the reorganization of the actin cytoskeleton. Regulates neuron morphogenesis and increases branching of axons and dendrites. Regulates dendrite branching in Purkinje cells (By similarity). Binds to and sequesters actin monomers (G actin). Nucleates actin polymerization by assembling three actin monomers in cross-filament orientation and thereby promotes growth of actin filaments at the barbed end. Can also mediate actin depolymerization at barbed ends and severing of …

**Summary**, from NCBI Gene [23242](https://www.ncbi.nlm.nih.gov/gene/23242):

> This gene encodes a protein that contains WH2 domains (WASP, Wiskott-Aldrich syndrome protein, homology domain-2) that interact with actin. The encoded actin regulator protein is required for growth and assembly of brush border microvilli that play a role in maintaining intestinal homeostasis. A similar protein in mouse functions in midbrain neural tube closure. A pseudogene of this gene is located on chromosome X. [provided by RefSeq, Oct 2016]

**Accessions** — [HGNC:22199](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:22199) · Entrez [23242](https://www.ncbi.nlm.nih.gov/gene/23242) · UniProt [O75128](https://www.uniprot.org/uniprotkb/O75128) · Ensembl [ENSG00000106078](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106078)

## Data

Gene col 2719: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2719); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2719, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2719]; `tensor/DDL_lfc|DDL_z.npy` [2719]; `embed/gene_vectors.npy` [2719]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2719 or target_col == 2719). Every well: [[COBL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COBL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
