---
symbol: "SLC41A1"
type: "gene"
col: 5409
ensembl_id: "ENSG00000133065"
name: "solute carrier family 41 member 1"
location: "1q32.1"
module: 4
arm: "-"
pooled_cpm: 39.08
n_lines_expressing: 49
n_dd_up: 28
n_dd_down: 2
n_dd_up_clean: 11
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# SLC41A1

*solute carrier family 41 member 1* — 1q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (17 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.75× (z +22.4, q 0e+00, up in 41 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Belumosudil (drug)]] 5 µM: 0.760× (z -4.2, q 0.016, down in 24 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (RKO 0.107×, NCI-H23 0.210×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (A-427 0.211×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Pimozide (drug)]] 0.05 µM in 1 line (CHP-212 0.0754×); [[Tofacitinib (drug)]] 0.05 µM in 1 line (CHP-212 0.128×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CSRP2]] (+0.63, fdr 1e-05), [[CABYR]] (+0.57, fdr 2e-05), [[INTS6L]] (+0.55, fdr 3e-05); moves opposite to [[SMIM7]] (-0.65, fdr 1e-05), [[COG2]] (-0.53, fdr 2e-04), [[NOL10]] (-0.52, fdr 3e-05).
> It sits in the **-** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 19 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5409.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.75×** | +22.4 | 0e+00 | 41/47 (A498, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.65×** | +21.6 | 0e+00 | 46/47 (SW480, A-172, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.70×** | +8.0 | 3e-13 | 37/47 (C32, SW480, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.64×** | +7.8 | 1e-12 | 34/47 (AsPC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.59×** | +7.0 | 3e-10 | 33/46 (MIA PaCa-2, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.56×** | +7.0 | 3e-10 | 30/47 (A498, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.57×** | +6.8 | 7e-10 | 29/46 (C32, A-172, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.48×** | +6.2 | 5e-08 | 29/47 (Hs 766T, NCI-H1792, …) | inconsistent across doses | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.31×** | +6.0 | 1e-07 | 30/47 (A-172, HOP62, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.11× | +5.6 | 1e-06 | 2/48 (MIA PaCa-2, SNU-1) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **1.39×** | +5.2 | 1e-05 | 25/47 (MIA PaCa-2, LS 180, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **1.39×** | +5.1 | 1e-05 | 24/46 (NCI-H460, KATO III, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **1.37×** | +4.8 | 6e-05 | 28/47 (MIA PaCa-2, SW1417, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.34×** | +4.5 | 3e-04 | 23/47 (NCI-H460, H4, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **1.33×** | +4.4 | 4e-04 | 22/47 (SW480, SW1417, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.32×** | +4.3 | 7e-04 | 21/47 (C32, SW480, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.31×** | +4.2 | 9e-04 | 21/47 (J82, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.26×** | +3.6 | 0.007 | 17/46 (CFPAC-1, Panc 03.27, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.26×** | +3.6 | 0.007 | 19/46 (NCI-H2030, A-172, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.54×** | +3.5 | 0.010 | 16/46 (CFPAC-1, C32, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | 1.17× | +3.4 | 0.014 | 16/47 (SW480, HEC-1-A, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.24×** | +3.2 | 0.033 | 16/47 (HT-29, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Isocorydine (drug)]] 5 µM |  | 1.14× | +2.8 | 0.089 | 5/47 (J82, SNU-1, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.13× | +2.8 | 0.097 | 12/47 (CFPAC-1, MIA PaCa-2, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5409.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (RKO 0.107×, NCI-H23 0.210×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (A-427 0.211×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Pimozide (drug)]] 0.05 µM in 1 line (CHP-212 0.0754×); [[Tofacitinib (drug)]] 0.05 µM in 1 line (CHP-212 0.128×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belumosudil (drug)]] 5 µM |  | **0.760×** | -4.2 | 0.016 | 24/47 (BT-474, KATO III, …) | top dose only |  |
| [[Tofacitinib (drug)]] 5 µM |  | 0.836× | -4.0 | 0.016 | 14/47 (C32, Hs 766T, …) | top dose only |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.621×** | -3.9 | 0.016 | 22/47 (A-427, HEC-1-A, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.817× | -3.2 | 0.20 | 15/46 (NCI-H23, HEC-1-A, …) | all doses, flat | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.34 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5409. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 22.9 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.19× (z +19.6) | — |
| [[A498 (line)]] | wt | 57.8 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.99× (z +22.1) | — |
| [[C32 (line)]] | wt | 105 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.96× (z +15.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 47.0 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.06× (z +18.5) | — |
| [[CFPAC-1 (line)]] | alt | 43.8 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.25× (z +18.6) | — |
| [[LoVo (line)]] | wt | 26.9 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.26× (z +14.8) | — |
| [[NCI-H460 (line)]] | wt | 64.8 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.87× (z +13.3) | — |
| [[A-172 (line)]] | wt | 44.3 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.65× (z +16.6) | — |
| [[A-427 (line)]] | wt | 35.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +11.2) | [[Dinaciclib (drug)]] 0.05 µM 0.211× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 28.0 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.86× (z +14.3) | — |
| [[CHP-212 (line)]] | wt | 35.5 | 0 | 2 | — | [[Pimozide (drug)]] 0.05 µM 0.0754× (z -11.0) |
| [[H4 (line)]] | wt | 40.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.86× (z +10.9) | — |
| [[HEC-1-A (line)]] | alt | 37.0 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.33× (z +10.6) | — |
| [[HOP62 (line)]] | alt | 35.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.92× (z +15.8) | — |
| [[Hs 766T (line)]] | wt | 43.1 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.45× (z +13.8) | — |
| [[HS-578T (line)]] | alt | 28.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.86× (z +16.5) | — |
| [[HT-29 (line)]] | alt | 21.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +9.7) | — |
| [[hTERT-HPNE (line)]] | wt | 33.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.85× (z +18.8) | — |
| [[KATO III (line)]] | alt | 26.2 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.22× (z +9.4) | — |
| [[LS 180 (line)]] | wt | 22.3 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.52× (z +9.1) | — |
| [[NCI-H1573 (line)]] | alt | 26.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.16× (z +12.4) | — |
| [[NCI-H1792 (line)]] | alt | 45.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.18× (z +16.2) | — |
| [[NCI-H23 (line)]] | alt | 33.7 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.32× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.210× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 36.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.28× (z +15.0) | — |
| [[PANC-1 (line)]] | alt | 38.4 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.75× (z +15.0) | — |
| [[RKO (line)]] | wt | 86.2 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.23× (z +11.0) | [[Dinaciclib (drug)]] 0.5 µM 0.107× (z -21.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[RPMI-7951 (line)]] | alt | 34.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.64× (z +14.5) | — |
| [[SNU-423 (line)]] | alt | 32.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.81× (z +14.5) | — |
| [[SW 900 (line)]] | alt | 52.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +12.7) | — |
| [[SW1417 (line)]] | alt | 34.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +12.2) | — |
| [[SW480 (line)]] | alt | 22.7 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.70× (z +18.4) | — |
| [[BT-474 (line)]] | alt | 14.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.52× (z +8.5) | — |
| [[COLO 205 (line)]] | alt | 16.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.53× (z +8.5) | — |
| [[J82 (line)]] | alt | 46.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +12.6) | — |
| [[LOX-IMVI (line)]] | wt | 47.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.58× (z +10.6) | — |
| [[NCI-H2030 (line)]] | alt | 36.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.44× (z +10.9) | — |
| [[NCI-H2347 (line)]] | alt | 31.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.49× (z +13.7) | — |
| [[SK-MEL-2 (line)]] | alt | 41.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.71× (z +10.7) | — |
| [[SNU-1 (line)]] | wt | 108 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.94× (z +8.8) | — |
| [[AN3 CA (line)]] | alt | 54.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 48.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.50 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 37.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 43.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 36.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5409), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CSRP2]] | +0.63 | +0.56 / +0.68 | both halves | 1e-05 |  |
| [[CABYR]] | +0.57 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[INTS6L]] | +0.55 | +0.47 / +0.46 | both halves | 3e-05 |  |
| [[CSRNP2]] | +0.53 | +0.53 / +0.39 | both halves | 5e-05 |  |
| [[GAD1]] | +0.52 | +0.46 / +0.48 | both halves | 3e-05 |  |
| [[RELT]] | +0.52 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[DIPK2A]] | +0.52 | +0.50 / +0.36 | both halves | 9e-05 |  |
| [[POLR2A]] | +0.51 | +0.39 / +0.46 | both halves | 5e-05 |  |
| [[FGF11]] | +0.51 | +0.37 / +0.47 | both halves | 9e-05 |  |
| [[GSTM3]] | +0.50 | +0.42 / +0.48 | both halves | 4e-05 |  |
| [[SIX4]] | +0.50 | +0.50 / +0.35 | both halves | 1e-04 |  |
| [[METTL21A]] | +0.49 | +0.37 / +0.48 | both halves | 9e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMIM7]] | -0.65 | -0.68 / -0.53 | both halves | 1e-05 |  |
| [[COG2]] | -0.53 | -0.32 / -0.46 | both halves | 2e-04 |  |
| [[NOL10]] | -0.52 | -0.56 / -0.45 | both halves | 3e-05 |  |
| [[VTA1]] | -0.51 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[DCTN4]] | -0.51 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[THRAP3]] | -0.50 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[SMIM8]] | -0.50 | -0.37 / -0.38 | both halves | 8e-05 |  |
| [[WDR70]] | -0.50 | -0.37 / -0.35 | both halves | 1e-04 |  |
| [[VPS50]] | -0.49 | -0.42 / -0.45 | both halves | 4e-05 |  |
| [[PWP1]] | -0.49 | -0.40 / -0.52 | both halves | 5e-05 |  |
| [[MICU2]] | -0.47 | -0.44 / -0.29 | both halves | 3e-04 |  |
| [[ZNF790-AS1]] | -0.47 | -0.53 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SLC41A1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ZIC2]] | B | ZIC2 activity raises SLC41A1's level | lines that do not express ZIC2 (10) vs lines expressing it (40) | 1.38× lower at baseline in the lines without ZIC2 | 0.089 | ⚠ within organs, on part of the lines; also absent: FOXD1, BEND7 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **-** arm (projection on the module's main direction -0.356). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-27.8, -8.1); signed map (2.4, 14.0). **Vector** length 92.4, 22.7% of its response variance represented; |z| ≥ 3 in 934 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.3 | +21.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.6 | +7.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +4.3 | +6.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.2 | +22.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +4.2 | +4.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.7 | +3.5 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | +2.1 | +2.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.8 | +3.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | +1.8 | +2.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.7 | +2.8 |
| fall | [[PH-797804 (drug)]] 5 µM |  | -4.8 | +0.1 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.8 | +1.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~63% of this change | -3.6 | +4.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | -3.4 | +5.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.3 | -4.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -3.0 | -3.9 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -2.4 | -4.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.0 | +1.5 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 41 member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q32.1 — chr1:205,789,094-205,813,748 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MgtE |
| Gene groups (HGNC) | Solute carrier family 41 |
| Reactome | 3 pathways, smallest: Metal ion SLC transporters; SLC-mediated transmembrane transport; Transport of small molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IVJ1](https://www.uniprot.org/uniprotkb/Q8IVJ1) (Solute carrier family 41 member 1):

> Na(+)/Mg(2+) ion exchanger that acts as a predominant Mg(2+) efflux system at the plasma membrane. Transporter activity is driven by the inwardly directed electrochemical gradient for Na(+) ions, thus directly depends on the extracellular Na(+) ion concentration set by Na(+)/K(+) pump. Generates circadian cellular Mg(2+) fluxes that feed back to regulate clock-controlled gene expression and metabolism and facilitate higher energetic demands during the day. Has a role in regulating the activity …

**Summary**, from NCBI Gene [254428](https://www.ncbi.nlm.nih.gov/gene/254428):

> Enables magnesium:sodium antiporter activity. Involved in cellular response to magnesium ion; intracellular magnesium ion homeostasis; and magnesium ion transmembrane transport. Located in basolateral plasma membrane. Part of protein-containing complex. Implicated in nephronophthisis. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:19429](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19429) · Entrez [254428](https://www.ncbi.nlm.nih.gov/gene/254428) · UniProt [Q8IVJ1](https://www.uniprot.org/uniprotkb/Q8IVJ1) · Ensembl [ENSG00000133065](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000133065)

## Data

Gene col 5409: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5409); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5409, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5409]; `tensor/DDL_lfc|DDL_z.npy` [5409]; `embed/gene_vectors.npy` [5409]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5409 or target_col == 5409). Every well: [[SLC41A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC41A1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
