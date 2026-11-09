---
symbol: "PITPNM2"
type: "gene"
col: 1646
ensembl_id: "ENSG00000090975"
name: "phosphatidylinositol transfer protein membrane associated 2"
location: "12q24.31"
module: 172
arm: "+"
pooled_cpm: 50.12
n_lines_expressing: 48
n_dd_up: 3
n_dd_down: 30
n_dd_up_clean: 2
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/172"]
generated_by: "tahoemap"
---

# PITPNM2

*phosphatidylinositol transfer protein membrane associated 2* — 12q24.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Neratinib (maleate) (drug)]] 5 µM: 1.17× (z +5.0, q 3e-04, up in 12 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Adagrasib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 1.52×; ⚠ position not correctable); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (SW480 2.09×; ⚠ cell-cycle shift, explains ~68% of this change); [[Digitoxin (drug)]] 5 µM in 1 line (SW480 2.05×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.276× (z -41.1, q 0e+00, down in 45 of 46 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DHX35]] (+0.52, fdr 2e-05), [[IGHMBP2]] (+0.50, fdr 1e-04), [[NCOA6]] (+0.49, fdr 2e-05); moves opposite to [[ARL5B]] (-0.46, fdr 9e-05), [[VWA5A]] (-0.46, fdr 6e-05), [[PRSS16]] (-0.45, fdr 7e-05).
> It is in [[Module 172]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1646.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Adagrasib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 1.52×; ⚠ position not correctable); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (SW480 2.09×; ⚠ cell-cycle shift, explains ~68% of this change); [[Digitoxin (drug)]] 5 µM in 1 line (SW480 2.05×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.17× | +5.0 | 3e-04 | 12/46 (SK-MEL-2, NCI-H460, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.23×** | +4.8 | 4e-04 | 19/45 (NCI-H2030, SW480, …) | two highest doses | low cells (technical?) |
| [[Rapamycin (drug)]] 5 µM |  | 1.16× | +4.7 | 4e-04 | 3/46 (SK-MEL-2, NCI-H460, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.21×** | +4.2 | 0.004 | 18/45 (NCI-H460, SW480, …) | two highest doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.21×** | +4.2 | 0.004 | 19/45 (MIA PaCa-2, SW480, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | 1.15× | +3.7 | 0.018 | 11/46 (SW480, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 1.12× | +3.5 | 0.034 | 14/46 (SW480, MIA PaCa-2, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.16× | +3.3 | 0.059 | 11/45 (C32, MIA PaCa-2, …) | rises with dose |  |
| [[Neratinib (drug)]] 5 µM |  | 1.15× | +3.3 | 0.060 | 8/45 (NCI-H460, SW 900, …) | rises with dose |  |
| [[Tirabrutinib (drug)]] 0.5 µM |  | 1.15× | +3.1 | 0.100 | 8/46 (RPMI-7951, NCI-H1792, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 15 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1646.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.276×** | -41.1 | 0e+00 | 45/46 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.202×** | -36.2 | 0e+00 | 45/46 (PANC-1, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.207×** | -35.7 | 0e+00 | 46/46 (PANC-1, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.246×** | -31.7 | 0e+00 | 44/46 (AsPC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.332×** | -24.0 | 0e+00 | 39/46 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **0.485×** | -16.3 | 0e+00 | 34/44 (PANC-1, NCI-H1792, …) | all doses, flat | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.253×** | -16.2 | 0e+00 | 44/47 (PANC-1, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.489×** | -16.1 | 0e+00 | 38/46 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.629×** | -14.8 | 0e+00 | 27/46 (SHP-77, AsPC-1, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.539×** | -12.9 | 2e-36 | 26/38 (SW480, NCI-H2030, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | **0.555×** | -12.8 | 1e-35 | 30/34 (NCI-H2030, PANC-1, …) | all doses, flat | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.678×** | -12.4 | 1e-33 | 35/46 (PANC-1, SNU-423, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.615×** | -11.0 | 2e-26 | 31/45 (PANC-1, SHP-77, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | **0.620×** | -10.4 | 2e-23 | 33/45 (PANC-1, AsPC-1, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **0.729×** | -10.1 | 3e-22 | 30/46 (SNU-423, NCI-H2347, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.654×** | -9.6 | 4e-20 | 31/45 (SW48, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.702×** | -8.0 | 5e-14 | 30/47 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.518×** | -7.8 | 2e-13 | 27/47 (SHP-77, PANC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.741×** | -6.7 | 4e-10 | 23/46 (SHP-77, A-172, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.36 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1646. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 330 | 0 | 22 (7 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0505× (z -22.5) |
| [[PANC-1 (line)]] | alt | 77.7 | 0 | 17 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.136× (z -38.4) |
| [[A-172 (line)]] | wt | 35.2 | 0 | 12 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0553× (z -34.6) |
| [[MIA PaCa-2 (line)]] | alt | 69.2 | 1 (1 ⚠) | 11 (5 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.52× (z +13.8) ⚠ position not correctable | [[Panobinostat (drug)]] 5 µM 0.0797× (z -23.7) |
| [[A549 (line)]] | wt | 61.8 | 0 | 11 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0714× (z -36.3) |
| [[NCI-H1792 (line)]] | alt | 75.0 | 0 | 11 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.125× (z -27.9) |
| [[RPMI-7951 (line)]] | alt | 59.3 | 0 | 11 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -16.0) |
| [[NCI-H2030 (line)]] | alt | 77.5 | 0 | 10 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.154× (z -20.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.300× (z -19.8) |
| [[NCI-H460 (line)]] | wt | 51.2 | 0 | 10 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -26.5) |
| [[SW1417 (line)]] | alt | 54.1 | 0 | 10 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.221× (z -16.5) |
| [[AsPC-1 (line)]] | alt | 99.6 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -26.3) |
| [[Hs 766T (line)]] | wt | 61.3 | 0 | 9 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.121× (z -19.2) |
| [[LoVo (line)]] | wt | 55.0 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -22.5) |
| [[SNU-423 (line)]] | alt | 40.6 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -21.1) |
| [[SW480 (line)]] | alt | 45.8 | 2 (2 ⚠) | 7 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.09× (z +9.3) ⚠ cell-cycle shift, explains ~68% of this change | [[Panobinostat (drug)]] 0.5 µM 0.177× (z -21.6) |
| [[A498 (line)]] | wt | 56.6 | 0 | 8 | — | [[Homoharringtonine (drug)]] 5 µM 0.148× (z -30.4) |
| [[HS-578T (line)]] | alt | 28.7 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -17.3) |
| [[NCI-H2347 (line)]] | alt | 37.8 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.348× (z -13.1) |
| [[J82 (line)]] | alt | 40.4 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.208× (z -19.4) |
| [[LS 180 (line)]] | wt | 38.3 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.184× (z -16.5) |
| [[SK-MEL-2 (line)]] | alt | 31.8 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -12.9) |
| [[C32 (line)]] | wt | 32.8 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.257× (z -13.9) |
| [[HOP62 (line)]] | alt | 30.2 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -20.6) |
| [[LOX-IMVI (line)]] | wt | 32.8 | 0 | 6 | — | [[Panobinostat (drug)]] 0.5 µM 0.114× (z -17.7) |
| [[NCI-H1573 (line)]] | alt | 25.5 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -21.3) |
| [[RKO (line)]] | wt | 44.1 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -14.6) |
| [[SW48 (line)]] | wt | 47.4 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.136× (z -18.9) |
| [[COLO 205 (line)]] | alt | 59.3 | 0 | 5 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.134× (z -16.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.202× (z -12.8) |
| [[HEC-1-A (line)]] | alt | 22.6 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -15.1) |
| [[SNU-1 (line)]] | wt | 37.3 | 0 | 5 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.105× (z -13.5) ⚠ toxic; cell-cycle shift, explains ~34% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.158× (z -11.5) |
| [[A-427 (line)]] | wt | 26.5 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.201× (z -12.8) |
| [[C-33 A (line)]] | alt | 43.1 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.104× (z -17.8) |
| [[HepG2_C3A (line)]] | wt | 101 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.188× (z -15.8) |
| [[NCI-H23 (line)]] | alt | 21.9 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.184× (z -12.0) |
| [[Panc 03.27 (line)]] | alt | 30.9 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.182× (z -12.0) |
| [[SW 900 (line)]] | alt | 31.7 | 0 | 4 | — | [[Harringtonine (drug)]] 5 µM 0.107× (z -15.3) |
| [[hTERT-HPNE (line)]] | wt | 31.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -11.8) |
| [[CFPAC-1 (line)]] | alt | 23.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.399× (z -10.3) |
| [[BT-474 (line)]] | alt | 32.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.234× (z -14.2) |
| [[AN3 CA (line)]] | alt | 47.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.7 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 9.23 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 73.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 50.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 37.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1646), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DHX35]] | +0.52 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[IGHMBP2]] | +0.50 | +0.33 / +0.53 | both halves | 1e-04 |  |
| [[NCOA6]] | +0.49 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[RILPL1]] | +0.49 | +0.52 / +0.46 | both halves | 2e-05 |  |
| [[HIRA]] | +0.48 | +0.47 / +0.57 | both halves | 2e-05 |  |
| [[CRTC3]] | +0.47 | +0.57 / +0.41 | both halves | 4e-05 |  |
| [[PTPN9]] | +0.46 | +0.59 / +0.44 | both halves | 3e-05 |  |
| [[RUFY3]] | +0.45 | +0.43 / +0.42 | both halves | 4e-05 |  |
| [[PRELID3A]] | +0.45 | +0.44 / +0.33 | both halves | 1e-04 |  |
| [[LRFN4]] | +0.45 | +0.35 / +0.45 | both halves | 1e-04 |  |
| [[ZNF746]] | +0.45 | +0.26 / +0.51 | both halves | 4e-04 |  |
| [[MAST2]] | +0.45 | +0.54 / +0.38 | both halves | 7e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARL5B]] | -0.46 | -0.45 / -0.37 | both halves | 9e-05 |  |
| [[VWA5A]] | -0.46 | -0.39 / -0.48 | both halves | 6e-05 |  |
| [[PRSS16]] | -0.45 | -0.41 / -0.38 | both halves | 7e-05 |  |
| [[CUL4B]] | -0.42 | -0.36 / -0.45 | both halves | 1e-04 |  |
| [[SCOC]] | -0.42 | -0.45 / -0.43 | both halves | 3e-05 |  |
| [[SLFN11]] | -0.42 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[SF3B1]] | -0.42 | -0.48 / -0.38 | both halves | 7e-05 |  |
| [[ATP7A]] | -0.42 | -0.43 / -0.38 | both halves | 7e-05 |  |
| [[USP9X]] | -0.42 | -0.22 / -0.46 | both halves | 6e-04 |  |
| [[EXTL2]] | -0.41 | -0.47 / -0.46 | both halves | 3e-05 |  |
| [[LINC02320]] | -0.41 | -0.38 / -0.32 | both halves | 2e-04 |  |
| [[ARHGAP12]] | -0.40 | -0.23 / -0.46 | both halves | 5e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 172]]; 24 genes; every member is in the + arm (projection on the module's main direction 0.482). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-47.9, 13.2); signed map (-2.6, -10.2). **Vector** length 85.2, 21.6% of its response variance represented; |z| ≥ 3 in 1,487 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.4 | +2.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.1 | -14.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~63% of this change | +4.0 | -2.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.6 | -1.9 |
|  | [[venetoclax (drug)]] 5 µM |  | +3.6 | +0.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.4 | +0.3 |
|  | [[EX229 (drug)]] 5 µM |  | +3.3 | +1.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.9 | -0.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.7 | +4.2 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -6.2 | -16.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.1 | -12.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -4.8 | -8.0 |
|  | [[Selinexor (drug)]] 5 µM |  | -3.8 | -10.1 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -3.0 | -5.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.1 | -2.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.9 | -1.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.7 | -5.5 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -1.7 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | phosphatidylinositol transfer protein membrane associated 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.31 — chr12:122,983,480-123,151,090 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RDGBA2, RDGB2, NIR3 |
| Gene groups (HGNC) | Phosphatidylinositol transfer proteins; MicroRNA protein coding host genes |
| Reactome | 4 pathways, smallest: Synthesis of PI; Glycerophospholipid biosynthesis; Phospholipid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BZ72](https://www.uniprot.org/uniprotkb/Q9BZ72) (Membrane-associated phosphatidylinositol transfer protein 2):

> Membrane-associated phosphatidylinositol (PI) transfer protein that shuttles PI between intracellular membranes and thereby maintains plasma membrane phosphoinositide signaling competence. Upon production of phosphatidic acid (PA), mediates the transfer of phosphatidylinositol from the endoplasmic reticulum to the plasma membrane at endoplasmic reticulum-plasma membrane contact sites. This transfer sustains phospholipase C (PLC)-coupled receptor signaling and replenishing of plasma membrane …

**Summary**, from NCBI Gene [57605](https://www.ncbi.nlm.nih.gov/gene/57605):

> PITPNM2 belongs to a family of membrane-associated phosphatidylinositol transfer domain-containing proteins that share homology with the Drosophila retinal degeneration B (rdgB) protein (Ocaka et al., 2005 [PubMed 15627748]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:21044](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21044) · Entrez [57605](https://www.ncbi.nlm.nih.gov/gene/57605) · UniProt [Q9BZ72](https://www.uniprot.org/uniprotkb/Q9BZ72) · Ensembl [ENSG00000090975](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000090975)

## Data

Gene col 1646: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1646); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1646, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1646]; `tensor/DDL_lfc|DDL_z.npy` [1646]; `embed/gene_vectors.npy` [1646]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1646 or target_col == 1646). Every well: [[PITPNM2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PITPNM2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
