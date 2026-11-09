---
symbol: "TGFBR3"
type: "gene"
col: 925
ensembl_id: "ENSG00000069702"
name: "transforming growth factor beta receptor 3"
location: "1p22.1"
module: 106
arm: "+"
pooled_cpm: 35.01
n_lines_expressing: 44
n_dd_up: 25
n_dd_down: 30
n_dd_up_clean: 22
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 5
direction_downstream: 2
tags: ["gene", "module/106"]
generated_by: "tahoemap"
---

# TGFBR3

*transforming growth factor beta receptor 3* — 1p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (3 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.12× (z +18.6, q 0e+00, up in 37 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (9 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.611× (z -8.6, q 4e-15, down in 27 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SORL1]] (+0.61, fdr 1e-05), [[EPS8]] (+0.60, fdr 1e-05), [[PRKAR2B]] (+0.58, fdr 1e-05); moves opposite to [[GPATCH2L]] (-0.53, fdr 3e-05), [[ZNF621]] (-0.52, fdr 4e-05), [[LCA5L]] (-0.51, fdr 6e-05).
> It is in [[Module 106]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[VSNL1]] → it (grade B ⚠); 2 go from it, the strongest it → [[OPHN1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 4 with an alert ⚠; shown: the 15 strongest. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 925.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.12×** | +18.6 | 0e+00 | 37/42 (J82, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.02×** | +12.3 | 3e-32 | 29/42 (NCI-H2347, RKO, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.90×** | +11.2 | 8e-27 | 30/42 (NCI-H2347, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.79×** | +10.2 | 4e-22 | 22/42 (A498, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.77×** | +10.0 | 2e-21 | 25/41 (A498, J82, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.55×** | +8.6 | 1e-15 | 24/42 (LoVo, NCI-H2030, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.52×** | +7.3 | 3e-11 | 20/42 (NCI-H2030, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~13% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.48×** | +6.8 | 7e-10 | 22/42 (C32, SW48, …) | all doses, stronger at high dose |  |
| [[Radotinib (drug)]] 5 µM |  | **1.24×** | +5.2 | 1e-05 | 14/42 (A-172, SK-MEL-2, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.33×** | +5.0 | 3e-05 | 18/41 (HS-578T, LOX-IMVI, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.31×** | +4.7 | 1e-04 | 15/41 (HS-578T, hTERT-HPNE, …) | all doses, flat |  |
| [[Budesonide (drug)]] 0.5 µM |  | **1.29×** | +4.4 | 5e-04 | 14/42 (HS-578T, LOX-IMVI, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.28×** | +4.4 | 6e-04 | 12/42 (NCI-H1792, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Arbutin (drug)]] 0.05 µM |  | **1.30×** | +4.2 | 0.001 | 9/41 (HEC-1-A, SW480, …) | all doses, flat | position effect removed |
| [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | **1.27×** | +4.2 | 0.001 | 12/42 (HS-578T, A498, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 925.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.611×** | -8.6 | 4e-15 | 27/41 (SW480, SNU-1, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.641×** | -7.5 | 2e-11 | 22/42 (COLO 205, HepG2/C3A, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.653×** | -7.5 | 2e-11 | 22/42 (SW480, SW48, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.662×** | -7.2 | 8e-11 | 21/41 (COLO 205, LS 180, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **0.762×** | -6.7 | 2e-09 | 24/42 (SNU-1, HepG2/C3A, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.683×** | -6.7 | 2e-09 | 18/40 (SW480, HCT15, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.790×** | -5.8 | 5e-07 | 19/42 (LS 180, COLO 205, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.728×** | -5.3 | 7e-06 | 15/41 (CFPAC-1, C32, …) | all doses, stronger at high dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.738×** | -5.3 | 7e-06 | 17/41 (KATO III, SW480, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.752×** | -5.0 | 3e-05 | 19/42 (COLO 205, SW480, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.747×** | -4.9 | 5e-05 | 20/42 (SNU-1, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.756×** | -4.9 | 5e-05 | 16/41 (COLO 205, LS 180, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.760×** | -4.8 | 7e-05 | 19/42 (SW480, Hs 766T, …) | rises with dose | composition shift |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.761×** | -4.8 | 8e-05 | 15/41 (C32, COLO 205, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.766×** | -4.7 | 1e-04 | 16/41 (COLO 205, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.645×** | -4.0 | 0.002 | 16/42 (SNU-1, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.648×** | -4.0 | 0.002 | 15/42 (HCT15, SW480, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.789×** | -3.9 | 0.003 | 16/42 (LS 180, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Mebendazole (drug)]] 5 µM |  | **0.796×** | -3.8 | 0.004 | 11/42 (KATO III, SW480, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.808×** | -3.6 | 0.008 | 18/41 (SW480, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, -0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 925. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 37.2 | 19 | 0 | [[Dexamethasone (drug)]] 0.5 µM 8.03× (z +15.7) | — |
| [[SNU-1 (line)]] | wt | 551 | 0 | 16 (11 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0274× (z -38.0) ⚠ toxic; transcription drop; cell-cycle shift, explains <1% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.224× (z -15.8) |
| [[SW480 (line)]] | alt | 73.5 | 0 | 14 (7 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.210× (z -13.8) |
| [[COLO 205 (line)]] | alt | 129 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.162× (z -16.9) ⚠ cell-cycle shift, explains ~72% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.229× (z -9.7) |
| [[LS 180 (line)]] | wt | 181 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.146× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.183× (z -11.9) |
| [[KATO III (line)]] | alt | 47.6 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.168× (z -15.0) ⚠ cell-cycle shift, explains ~72% of this change |
| [[SW48 (line)]] | wt | 32.7 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.234× (z -11.8) ⚠ cell-cycle shift, explains ~72% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.216× (z -8.8) |
| [[HepG2_C3A (line)]] | wt | 111 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0816× (z -19.8) ⚠ cell-cycle shift, explains ~72% of this change |
| [[hTERT-HPNE (line)]] | wt | 24.9 | 3 | 0 | [[Clobetasol propionate (drug)]] 5 µM 5.80× (z +8.6) | — |
| [[LOX-IMVI (line)]] | wt | 14.2 | 3 | 0 | [[Tucidinostat (drug)]] 5 µM 3.31× (z +9.4) | — |
| [[Hs 766T (line)]] | wt | 73.5 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -14.1) ⚠ cell-cycle shift, explains ~72% of this change |
| [[LoVo (line)]] | wt | 41.9 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.11× (z +9.9) | [[Dinaciclib (drug)]] 0.05 µM 0.347× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~8% of this change |
| [[A-427 (line)]] | wt | 19.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.284× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 14.8 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.45× (z +8.8) | — |
| [[C32 (line)]] | wt | 26.4 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.223× (z -8.8) |
| [[HCT15 (line)]] | alt | 51.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.183× (z -9.5) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 27.6 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.95× (z +11.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 40.2 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.72× (z +11.2) ⚠ position not correctable | — |
| [[NCI-H2347 (line)]] | alt | 23.0 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.76× (z +10.9) | — |
| [[RKO (line)]] | wt | 13.1 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.90× (z +8.9) | — |
| [[SK-MEL-2 (line)]] | alt | 15.5 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.131× (z -10.4) |
| [[A-172 (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 47.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.65 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.81 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.32 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 9.71 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.82 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 8.44 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.75 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.15 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 35.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 925), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SORL1]] | +0.61 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[EPS8]] | +0.60 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[PRKAR2B]] | +0.58 | +0.53 / +0.59 | both halves | 1e-05 | pathway: HALLMARK_UV_RESPONSE_DN |
| [[TMEM131L]] | +0.58 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[FOXO1]] | +0.57 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[TRAK1]] | +0.56 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[SHROOM2]] | +0.56 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[RAPGEF5]] | +0.56 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[EMP2]] | +0.56 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[AXIN2]] | +0.55 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[TANC1]] | +0.55 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[VSNL1]] | +0.55 | +0.59 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPATCH2L]] | -0.53 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[ZNF621]] | -0.52 | -0.46 / -0.41 | both halves | 4e-05 |  |
| [[LCA5L]] | -0.51 | -0.45 / -0.38 | both halves | 6e-05 |  |
| [[ADGRL1-AS1]] | -0.51 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[LUCAT1]] | -0.50 | -0.52 / -0.43 | both halves | 3e-05 |  |
| [[ZNF432]] | -0.50 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[C9orf24]] | -0.49 | -0.50 / -0.39 | both halves | 6e-05 |  |
| [[NIT1]] | -0.49 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[TRPC1]] | -0.48 | -0.43 / -0.38 | both halves | 6e-05 |  |
| [[CLDN14-AS1]] | -0.47 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[CCDC149]] | -0.47 | -0.51 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[VSNL1]] | B | VSNL1 activity raises TGFBR3's level | lines that do not express VSNL1 (34) vs lines expressing it (16) | 2.85× lower at baseline in the lines without VSNL1 | 0.056 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC02964, EDAR, VWA2 |
| [[NKD1]] | B | NKD1 activity raises TGFBR3's level | lines that do not express NKD1 (34) vs lines expressing it (16) | 2.25× lower at baseline in the lines without NKD1 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000265554, VSNL1, ENSG00000213981 |
| [[IGFL4]] | B | IGFL4 activity strengthens TGFBR3's drug response | lines that do not express IGFL4 (22) vs lines expressing it (20) | the lines without IGFL4 respond 1.10× as strongly (z diff -0.12); strongest at Harringtonine 0.5 µM: 0.86x vs 0.54x (z diff +3.4) | 0.076 | ⚠ within organs, on part of the lines; also absent: YBX2, FGF9, KLRK1; maybe low, not absent; target measured in part of the lines; both ways; artifact flags |
| [[CTDSPL]] | B | CTDSPL activity raises TGFBR3's level | lines that do not express CTDSPL (5) vs lines expressing it (45) | 2.76× lower at baseline in the lines without CTDSPL | 0.086 | ⚠ within organs, on part of the lines; also absent: ITGA9-AS1, SLC43A2, PLAAT3; maybe low, not absent |
| [[CAVIN2]] | B | CAVIN2 activity raises TGFBR3's level | lines that do not express CAVIN2 (32) vs lines expressing it (18) | 1.58× lower at baseline in the lines without CAVIN2 | 0.086 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CAVIN2-AS1, NLGN4Y, PSG9 |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OPHN1]] | B | TGFBR3 activity strengthens OPHN1's drug response | lines that do not express TGFBR3 (5) vs lines expressing it (43) | the lines without TGFBR3 respond 0.71× as strongly (z diff +2.65); strongest at Homoharringtonine 5 µM: 0.93x vs 0.55x (z diff +4.6) | 0.068 | ⚠ within organs, on part of the lines; also absent: LRP1, AMN; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[CTDSPL]] | B | TGFBR3 activity raises CTDSPL's level | lines that do not express TGFBR3 (6) vs lines expressing it (44) | 2.72× lower at baseline in the lines without TGFBR3 | 0.098 | ⚠ within organs, on part of the lines; also absent: LRP1, AMN; maybe low, not absent |

## Where it sits

- **Module**: [[Module 106]]; 44 genes; every member is in the + arm (projection on the module's main direction 0.642). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (15.3, 43.7); signed map (19.7, 27.1). **Vector** length 105, 25.6% of its response variance represented; |z| ≥ 3 in 1,308 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.5 | +18.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.8 | +11.2 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.6 | +12.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.4 | +8.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.2 | -2.7 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +3.1 | +2.3 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +3.0 | +2.7 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +2.8 | +1.9 |
| fall | [[5-Azacytidine (drug)]] 5 µM |  | -4.1 | -5.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.9 | -8.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -2.8 | -3.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.6 | -3.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.5 | -5.8 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.9 | -4.9 |

## What is on record

|  |  |
|---|---|
| Name | transforming growth factor beta receptor 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p22.1 — chr1:91,680,343-91,906,335 (-) |
| Ensembl biotype | protein_coding |
| Also known as | betaglycan, BGCAN |
| Gene groups (HGNC) | Proteoglycans |
| Hallmark sets | UV_RESPONSE_DN, APOPTOSIS, EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 17 pathways, smallest: TGFBR3 regulates FGF2 signaling; TGFBR3 regulates activin signaling; FGFR1b ligand binding and activation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q03167](https://www.uniprot.org/uniprotkb/Q03167) (Transforming growth factor beta receptor type 3):

> Cell surface receptor that regulates diverse cellular processes including cell proliferation, differentiation, migration, and apoptosis. Initiates BMP, inhibin, and TGF-beta signaling pathways by interacting with different ligands including TGFB1, BMP2, BMP5, BMP7 or GDF5. Alternatively, acts as a cell surface coreceptor for BMP ligands, serving to enhance ligand binding by differentially regulating BMPR1A/ALK3 and BMPR1B/ALK6 receptor trafficking. Promotes epithelial cell adhesion, focal …

**Summary**, from NCBI Gene [7049](https://www.ncbi.nlm.nih.gov/gene/7049):

> This locus encodes the transforming growth factor (TGF)-beta type III receptor. The encoded receptor is a membrane proteoglycan that often functions as a co-receptor with other TGF-beta receptor superfamily members. Ectodomain shedding produces soluble TGFBR3, which may inhibit TGFB signaling. Decreased expression of this receptor has been observed in various cancers. Alternatively spliced transcript variants encoding different isoforms have been identified for this gene.[provided by RefSeq, …

**Accessions** — [HGNC:11774](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11774) · Entrez [7049](https://www.ncbi.nlm.nih.gov/gene/7049) · UniProt [Q03167](https://www.uniprot.org/uniprotkb/Q03167) · Ensembl [ENSG00000069702](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000069702)

## Data

Gene col 925: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 925); `tables/drug_effects.parquet` (62 rows, flagged included); `relations/gene_relations.parquet` (col_a == 925, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 925]; `tensor/DDL_lfc|DDL_z.npy` [925]; `embed/gene_vectors.npy` [925]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 925 or target_col == 925). Every well: [[TGFBR3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TGFBR3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
