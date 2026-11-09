---
symbol: "DGKG"
type: "gene"
col: 669
ensembl_id: "ENSG00000058866"
name: "diacylglycerol kinase gamma"
location: "3q27.2-q27.3"
module: 72
arm: "+"
pooled_cpm: 32.03
n_lines_expressing: 36
n_dd_up: 14
n_dd_down: 35
n_dd_up_clean: 11
n_dd_down_clean: 29
in_vector_space: true
direction_upstream: 4
direction_downstream: 8
tags: ["gene", "module/072"]
generated_by: "tahoemap"
---

# DGKG

*diacylglycerol kinase gamma* — 3q27.2-q27.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 2.73× (z +16.6, q 0e+00, up in 26 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 35 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.362× (z -24.9, q 0e+00, down in 27 of 33 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HSP90AA2P]] (+0.64, fdr 7e-06), [[DYNC1I1]] (+0.62, fdr 1e-05), [[TMEM161A]] (+0.61, fdr 1e-05); moves opposite to [[ZBTB10]] (-0.54, fdr 1e-05), [[CHD2]] (-0.52, fdr 2e-05), [[RNF103]] (-0.52, fdr 3e-05).
> It is in [[Module 072]], a single-armed module (Degradation of DVL).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[LINC02985]] → it (grade B ⚠); 8 go from it, the strongest it → [[SLC10A7]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 4 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 669.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **2.73×** | +16.6 | 0e+00 | 26/34 (SW480, LoVo, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.37×** | +15.2 | 0e+00 | 30/34 (SW480, KATO III, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.18×** | +13.7 | 1e-40 | 28/34 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.99×** | +12.1 | 1e-31 | 25/34 (CFPAC-1, LoVo, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.44×** | +9.0 | 4e-17 | 17/34 (SW1417, LS 180, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.52×** | +8.5 | 2e-15 | 21/32 (SW480, KATO III, …) | all doses, flat | cell-cycle shift (explains ~16% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.67×** | +6.5 | 8e-09 | 19/34 (KATO III, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.05 µM |  | **1.30×** | +4.6 | 2e-04 | 13/34 (KATO III, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **1.25×** | +3.9 | 0.006 | 9/34 (NCI-H1573, SHP-77, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.24×** | +3.6 | 0.016 | 12/34 (CFPAC-1, RKO, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 0.5 µM |  | **1.23×** | +3.6 | 0.016 | 12/34 (SW480, LoVo, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.22×** | +3.5 | 0.018 | 8/33 (LoVo, SK-MEL-2, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.21×** | +3.4 | 0.032 | 10/33 (SW1417, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Infigratinib (drug)]] 5 µM |  | **1.40×** | +3.1 | 0.072 | 8/33 (KATO III, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.13× | +3.0 | 0.092 | 5/34 (BT-474, CFPAC-1, …) | top dose only |  |
| [[Meloxicam (drug)]] 0.05 µM |  | 1.19× | +3.0 | 0.096 | 2/34 (SNU-423, CHP-212) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 35 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 669.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.362×** | -24.9 | 0e+00 | 27/33 (NCI-H1792, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.455×** | -13.8 | 5e-41 | 24/33 (A-172, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.475×** | -13.1 | 7e-37 | 29/34 (A-172, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.529×** | -11.2 | 7e-27 | 24/34 (A-172, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.520×** | -11.1 | 2e-26 | 24/34 (A-172, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.570×** | -9.9 | 5e-21 | 25/34 (A-172, HS-578T, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.669×** | -8.6 | 5e-16 | 24/34 (SW480, A-172, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.630×** | -8.1 | 3e-14 | 23/34 (SW480, A-172, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.634×** | -7.7 | 8e-13 | 20/34 (SW480, C32, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM |  | **0.670×** | -7.6 | 1e-12 | 20/34 (A-172, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.758×** | -6.8 | 7e-10 | 25/33 (A-172, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.480×** | -6.7 | 8e-10 | 19/34 (A-172, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.695×** | -6.2 | 3e-08 | 12/32 (SW480, NCI-H2347, …) | all doses, stronger at high dose | position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | **0.734×** | -6.1 | 4e-08 | 19/34 (SW480, C32, …) | rises with dose | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.713×** | -5.7 | 4e-07 | 19/31 (SNU-423, A-172, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.713×** | -5.7 | 4e-07 | 20/34 (A-172, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.726×** | -5.6 | 6e-07 | 20/34 (A-172, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.33 per unit of S-phase module lfc, -0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 669. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 244 | 0 | 24 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0808× (z -25.2) |
| [[HS-578T (line)]] | alt | 102 | 0 | 13 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.208× (z -15.6) |
| [[SW480 (line)]] | alt | 40.9 | 3 | 9 | [[Ixazomib citrate (drug)]] 0.5 µM 4.36× (z +15.7) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.273× (z -13.8) |
| [[KATO III (line)]] | alt | 28.2 | 5 | 4 (2 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 8.20× (z +15.6) | [[Homoharringtonine (drug)]] 5 µM 0.313× (z -11.9) |
| [[NCI-H460 (line)]] | wt | 44.7 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -22.9) |
| [[H4 (line)]] | wt | 137 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -21.5) |
| [[LoVo (line)]] | wt | 38.5 | 4 | 4 (2 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 4.72× (z +14.9) | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -21.8) |
| [[NCI-H1792 (line)]] | alt | 71.5 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0581× (z -31.2) |
| [[HOP62 (line)]] | alt | 42.5 | 3 | 4 | [[Ixazomib citrate (drug)]] 0.5 µM 4.65× (z +13.3) | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -16.1) |
| [[RKO (line)]] | wt | 53.0 | 1 | 6 (2 ⚠) | [[Bortezomib (drug)]] 0.05 µM 3.86× (z +10.5) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.192× (z -13.7) |
| [[SNU-423 (line)]] | alt | 31.9 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0931× (z -18.9) |
| [[A549 (line)]] | wt | 48.4 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.157× (z -23.3) |
| [[COLO 205 (line)]] | alt | 16.3 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 18.6× (z +12.3) | — |
| [[HepG2_C3A (line)]] | wt | 21.5 | 2 | 2 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 7.43× (z +10.1) | [[Niclosamide (olamine) (drug)]] 5 µM 0.109× (z -10.7) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.261× (z -9.5) |
| [[SHP-77 (line)]] | alt | 31.6 | 3 | 1 | [[Ixazomib citrate (drug)]] 0.5 µM 4.77× (z +10.3) | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -10.5) |
| [[SK-MEL-2 (line)]] | alt | 60.8 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.118× (z -24.7) |
| [[CFPAC-1 (line)]] | alt | 20.6 | 3 | 0 | [[Auranofin (drug)]] 5 µM 4.72× (z +10.5) | — |
| [[LS 180 (line)]] | wt | 12.2 | 3 | 0 | [[Bortezomib (drug)]] 0.05 µM 8.09× (z +10.9) | — |
| [[NCI-H1573 (line)]] | alt | 19.5 | 2 | 1 | [[Ixazomib citrate (drug)]] 5 µM 7.98× (z +11.4) | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -9.2) |
| [[NCI-H2347 (line)]] | alt | 11.4 | 3 | 0 | [[Bortezomib (drug)]] 0.05 µM 5.47× (z +10.1) | — |
| [[RPMI-7951 (line)]] | alt | 46.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -15.1) |
| [[C32 (line)]] | wt | 29.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -12.0) |
| [[HCT15 (line)]] | alt | 12.8 | 0 | 2 | — | [[Gemfibrozil (drug)]] 0.5 µM 0.0724× (z -10.8) |
| [[J82 (line)]] | alt | 31.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.387× (z -10.4) |
| [[NCI-H2030 (line)]] | alt | 28.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -10.4) |
| [[A498 (line)]] | wt | 29.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -14.2) |
| [[SW1417 (line)]] | alt | 8.38 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 6.55× (z +11.9) | — |
| [[A-427 (line)]] | wt | 6.97 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.03 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 8.96 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.11 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.43 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 4.74 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 5.04 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.72 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.71 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.15 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.58 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 9.69 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.35 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 6.63 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 86.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.26 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.50 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 669), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HSP90AA2P]] | +0.64 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[DYNC1I1]] | +0.62 | +0.57 / +0.60 | both halves | 1e-05 |  |
| [[TMEM161A]] | +0.61 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[PSMD14]] | +0.61 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[CHRNA5]] | +0.60 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[ANKRD39]] | +0.60 | +0.65 / +0.47 | both halves | 2e-05 |  |
| [[PLAA]] | +0.59 | +0.65 / +0.44 | both halves | 3e-05 |  |
| [[POMP]] | +0.59 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[MINDY4]] | +0.58 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[AP4B1]] | +0.57 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[GCKR]] | +0.57 | +0.60 / +0.40 | both halves | 5e-05 |  |
| [[ULBP3]] | +0.57 | +0.42 / +0.58 | both halves | 4e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZBTB10]] | -0.54 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[CHD2]] | -0.52 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[RNF103]] | -0.52 | -0.53 / -0.46 | both halves | 3e-05 |  |
| [[GABARAP]] ⚠ | -0.51 | -0.51 / -0.49 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[CREBRF]] | -0.51 | -0.62 / -0.42 | both halves | 4e-05 |  |
| [[REL]] | -0.49 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[TXNDC16]] | -0.49 | -0.51 / -0.41 | both halves | 4e-05 |  |
| [[TMEM14C]] | -0.48 | -0.54 / -0.43 | both halves | 3e-05 |  |
| [[TAPT1]] | -0.48 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[CDK19]] | -0.48 | -0.48 / -0.40 | both halves | 5e-05 |  |
| [[NEU1]] | -0.48 | -0.53 / -0.39 | both halves | 5e-05 |  |
| [[CPEB2]] | -0.47 | -0.50 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02985]] | B | LINC02985 activity raises DGKG's level | lines that do not express LINC02985 (15) vs lines expressing it (35) | 2.60× lower at baseline in the lines without LINC02985 | 0.016 | ⚠ within organs, on part of the lines; also absent: GXYLT2 |
| [[GCKR]] | B | GCKR activity raises DGKG's level | lines that do not express GCKR (24) vs lines expressing it (26) | 1.79× lower at baseline in the lines without GCKR | 0.058 | ⚠ within organs, on part of the lines; also absent: G0S2, IGFBP1, AADAC; maybe low, not absent |
| [[TM4SF19]] | B | TM4SF19 activity raises DGKG's level | lines that do not express TM4SF19 (20) vs lines expressing it (30) | 2.53× lower at baseline in the lines without TM4SF19 | 0.067 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ADAMTS9, KYNU, PAK3 |
| [[RABGEF1P3]] | B | RABGEF1P3 activity raises DGKG's level | lines that do not express RABGEF1P3 (5) vs lines expressing it (45) | 2.90× lower at baseline in the lines without RABGEF1P3 | 0.089 | ⚠ within organs, on part of the lines; also absent: SLC2A1, PHLDA2, SHB; maybe low, not absent; its own permutation p |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC10A7]] | B | DGKG activity raises SLC10A7's level | lines that do not express DGKG (14) vs lines expressing it (36) | 1.70× lower at baseline in the lines without DGKG | 0.012 | ⚠ within organs, on part of the lines; also absent: CADPS2, RBPMS, SHC4; maybe low, not absent |
| [[TAPT1]] | B | DGKG activity raises TAPT1's level | lines that do not express DGKG (14) vs lines expressing it (36) | 1.35× lower at baseline in the lines without DGKG | 0.018 | ⚠ within organs, on part of the lines; also absent: CADPS2, RBPMS, SHC4; maybe low, not absent |
| [[STIP1]] | B | DGKG activity lowers STIP1's level | lines that do not express DGKG (14) vs lines expressing it (36) | 1.28× higher at baseline in the lines without DGKG | 0.046 | ⚠ within organs, on part of the lines; also absent: CADPS2, RBPMS, SHC4; maybe low, not absent |
| [[CCT4]] | B | DGKG activity lowers CCT4's level | lines that do not express DGKG (14) vs lines expressing it (36) | 1.34× higher at baseline in the lines without DGKG | 0.060 | ⚠ within organs, on part of the lines; also absent: CADPS2, RBPMS, SHC4; maybe low, not absent |
| [[SLC10A7]] | B | DGKG activity strengthens SLC10A7's drug response | lines that do not express DGKG (13) vs lines expressing it (35) | the lines without DGKG respond 0.76× as strongly (z diff +1.13); strongest at Dinaciclib 0.5 µM: 0.68x vs 0.40x (z diff +3.2) | 0.069 | ⚠ within organs, on part of the lines; also absent: CADPS2, RBPMS, SHC4; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[CHORDC1]] | B | DGKG activity lowers CHORDC1's level | lines that do not express DGKG (14) vs lines expressing it (36) | 1.38× higher at baseline in the lines without DGKG | 0.081 | ⚠ within organs, on part of the lines; also absent: CADPS2, RBPMS, SHC4; maybe low, not absent |
| [[CACYBP]] | B | DGKG activity lowers CACYBP's level | lines that do not express DGKG (14) vs lines expressing it (36) | 1.33× higher at baseline in the lines without DGKG | 0.087 | ⚠ within organs, on part of the lines; also absent: CADPS2, RBPMS, SHC4; maybe low, not absent |
| [[DYNC1I1]] | B | DGKG activity raises DYNC1I1's level | lines that do not express DGKG (14) vs lines expressing it (36) | 1.88× lower at baseline in the lines without DGKG | 0.098 | ⚠ within organs, on part of the lines; also absent: CADPS2, RBPMS, SHC4; maybe low, not absent |

## Where it sits

- **Module**: [[Module 072]] — Degradation of DVL; 69 genes; every member is in the + arm (projection on the module's main direction 0.625). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-17.2, -8.6); signed map (-28.4, -26.8). **Vector** length 114, 29.8% of its response variance represented; |z| ≥ 3 in 1,199 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +10.7 | +16.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +10.6 | +13.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +9.7 | +15.2 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +7.6 | +8.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.0 | +12.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.7 | +9.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +5.3 | +6.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | -2.4 |
| fall | [[Trametinib (drug)]] 5 µM |  | -4.8 | -7.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.1 | -8.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.9 | -13.1 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.8 | -5.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.7 | -5.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.6 | -8.1 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -3.4 | -5.1 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -3.3 | -5.2 |

## What is on record

|  |  |
|---|---|
| Name | diacylglycerol kinase gamma |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q27.2-q27.3 — chr3:186,105,668-186,362,234 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously DAGK3 |
| Gene groups (HGNC) | EF-hand domain containing; Diacylglycerol kinase family |
| Hallmark sets | COMPLEMENT |
| Reactome | 6 pathways, smallest: Effects of PIP2 hydrolysis; G alpha (q) signalling events; Platelet activation, signaling and aggregation |
| Matched by | ensembl_id |

**Function**, from UniProt [P49619](https://www.uniprot.org/uniprotkb/P49619) (Diacylglycerol kinase gamma):

> Diacylglycerol kinase that converts diacylglycerol/DAG into phosphatidic acid/phosphatidate/PA and regulates the respective levels of these two bioactive lipids. Thereby, acts as a central switch between the signaling pathways activated by these second messengers with different cellular targets and opposite effects in numerous biological processes (By similarity). Has no apparent specificity with regard to the acyl compositions of diacylglycerol. Specifically expressed in the cerebellum where …

**Summary**, from NCBI Gene [1608](https://www.ncbi.nlm.nih.gov/gene/1608):

> This gene encodes an enzyme that is a member of the type I subfamily of diacylglycerol kinases, which are involved in lipid metabolism. These enzymes generate phosphatidic acid by catalyzing the phosphorylation of diacylglycerol, a fundamental lipid second messenger that activates numerous proteins, including protein kinase C isoforms, Ras guanyl nucleotide-releasing proteins and some transient receptor potential channels. Diacylglycerol kinase gamma has been implicated in cell cycle regulation …

**Accessions** — [HGNC:2853](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2853) · Entrez [1608](https://www.ncbi.nlm.nih.gov/gene/1608) · UniProt [P49619](https://www.uniprot.org/uniprotkb/P49619) · Ensembl [ENSG00000058866](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000058866)

## Data

Gene col 669: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 669); `tables/drug_effects.parquet` (58 rows, flagged included); `relations/gene_relations.parquet` (col_a == 669, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 669]; `tensor/DDL_lfc|DDL_z.npy` [669]; `embed/gene_vectors.npy` [669]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 669 or target_col == 669). Every well: [[DGKG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DGKG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
