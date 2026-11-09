---
symbol: "MOSPD2"
type: "gene"
col: 5024
ensembl_id: "ENSG00000130150"
name: "motile sperm domain containing 2"
location: "Xp22.2"
module: 5
arm: "-"
pooled_cpm: 38.66
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 5
n_dd_up_clean: 11
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# MOSPD2

*motile sperm domain containing 2* — Xp22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.87× (z +22.5, q 0e+00, up in 44 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.586× (z -19.2, q 0e+00, down in 41 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 12 lines (SNU-423 0.388×, NCI-H460 0.438×, HOP62 0.359×, A549 0.390×, …); [[Dinaciclib (drug)]] 5 µM in 3 lines (MIA PaCa-2 0.212×, NCI-H1573 0.217×, PANC-1 0.342×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SW48 0.140×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change); [[Palmatine (chloride) (drug)]] 0.5 µM in 1 line (SNU-1 0.169×).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SNAP29]] (+0.67, fdr 1e-05), [[UBE2B]] (+0.60, fdr 2e-05), [[INIP]] (+0.59, fdr 3e-05); moves opposite to [[BEND3]] (-0.63, fdr 1e-05), [[POC1B-AS1]] (-0.59, fdr 1e-04), [[CCNJ]] (-0.58, fdr 1e-04).
> It sits in the **-** arm of [[Module 005]] (MYC targets v2).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5024.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.87×** | +22.5 | 0e+00 | 44/47 (NCI-H460, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.00×** | +17.7 | 0e+00 | 45/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.97×** | +17.3 | 0e+00 | 45/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.76×** | +14.4 | 4e-45 | 43/48 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.70×** | +13.5 | 3e-39 | 40/48 (NCI-H460, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.63×** | +12.4 | 2e-33 | 39/47 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.61×** | +11.7 | 9e-30 | 37/48 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.40×** | +8.3 | 1e-14 | 23/47 (HEC-1-A, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.34×** | +7.5 | 4e-12 | 27/47 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.18× | +6.1 | 6e-08 | 20/48 (SNU-1, NCI-H460, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.25×** | +5.7 | 5e-07 | 20/48 (SK-MEL-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.49×** | +5.3 | 5e-06 | 16/48 (SW480, A-172, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.23×** | +5.2 | 8e-06 | 20/48 (NCI-H460, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cepharanthine (drug)]] 5 µM |  | 1.15× | +4.9 | 4e-05 | 14/48 (LS 180, NCI-H2030, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.21×** | +4.9 | 4e-05 | 17/48 (A-427, RPMI-7951, …) | top dose only |  |
| [[Berbamine (drug)]] 5 µM |  | 1.13× | +4.5 | 2e-04 | 9/49 (NCI-H2030, LS 180, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.16× | +3.7 | 0.007 | 8/47 (SW480, J82, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5024.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 12 lines (SNU-423 0.388×, NCI-H460 0.438×, HOP62 0.359×, A549 0.390×, …); [[Dinaciclib (drug)]] 5 µM in 3 lines (MIA PaCa-2 0.212×, NCI-H1573 0.217×, PANC-1 0.342×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SW48 0.140×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change); [[Palmatine (chloride) (drug)]] 0.5 µM in 1 line (SNU-1 0.169×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.586×** | -19.2 | 0e+00 | 41/48 (SNU-423, NCI-H460, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.940× | -5.7 | 4e-06 | 0/48 | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.812×** | -5.0 | 1e-04 | 17/47 (NCI-H2347, SW48, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.819×** | -4.9 | 1e-04 | 20/48 (NCI-H23, SNU-423, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.828×** | -4.6 | 4e-04 | 16/37 (MIA PaCa-2, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.754×** | -3.8 | 0.014 | 14/34 (hTERT-HPNE, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.901× | -3.8 | 0.014 | 11/48 (HOP62, A498, …) | top dose only |  |
| [[Naproxen (drug)]] 0.05 µM |  | 0.857× | -3.6 | 0.019 | 15/47 (SW 1271, A-172, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.877× | -3.4 | 0.049 | 14/48 (NCI-H1792, RKO, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | 0.876× | -3.2 | 0.066 | 13/48 (LS 180, HEC-1-A, …) | top dose only |  |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.05 µM |  | 0.887× | -3.0 | 0.12 | 5/48 (MIA PaCa-2, SNU-423, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5024. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 45.8 | 13 (4 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.14× (z +20.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.438× (z -15.1) |
| [[A-172 (line)]] | wt | 56.3 | 4 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +10.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.583× (z -8.9) |
| [[KATO III (line)]] | alt | 50.6 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.44× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.396× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[MIA PaCa-2 (line)]] | alt | 64.0 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.18× (z +11.7) | [[Dinaciclib (drug)]] 5 µM 0.212× (z -15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[SW480 (line)]] | alt | 50.8 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.28× (z +10.7) | [[Dinaciclib (drug)]] 0.5 µM 0.517× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change |
| [[BT-474 (line)]] | alt | 53.9 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.89× (z +9.2) | — |
| [[hTERT-HPNE (line)]] | wt | 37.1 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +10.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.368× (z -11.1) |
| [[A498 (line)]] | wt | 24.2 | 1 | 1 | [[Panobinostat (drug)]] 0.5 µM 2.40× (z +8.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.401× (z -12.7) |
| [[HOP62 (line)]] | alt | 26.8 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +10.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.359× (z -14.5) |
| [[Hs 766T (line)]] | wt | 64.6 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +16.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.457× (z -11.5) |
| [[LoVo (line)]] | wt | 24.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +10.0) | — |
| [[NCI-H1573 (line)]] | alt | 35.9 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +12.9) | [[Dinaciclib (drug)]] 5 µM 0.217× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[NCI-H1792 (line)]] | alt | 75.3 | 1 | 1 | [[Panobinostat (drug)]] 5 µM 2.24× (z +8.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.544× (z -9.3) |
| [[NCI-H2030 (line)]] | alt | 20.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +10.4) | — |
| [[NCI-H23 (line)]] | alt | 25.6 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.365× (z -11.1) |
| [[PANC-1 (line)]] | alt | 31.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.342× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[SNU-1 (line)]] | wt | 31.9 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +8.6) | [[Palmatine (chloride) (drug)]] 0.5 µM 0.169× (z -10.2) |
| [[SNU-423 (line)]] | alt | 90.4 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +15.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.388× (z -16.5) |
| [[A549 (line)]] | wt | 41.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.390× (z -13.6) |
| [[AsPC-1 (line)]] | alt | 26.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.38× (z +14.8) | — |
| [[COLO 205 (line)]] | alt | 29.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.69× (z +11.9) | — |
| [[H4 (line)]] | wt | 37.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +10.5) | — |
| [[HS-578T (line)]] | alt | 30.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +8.6) | — |
| [[J82 (line)]] | alt | 69.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +13.8) | — |
| [[LOX-IMVI (line)]] | wt | 19.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.402× (z -9.7) |
| [[RPMI-7951 (line)]] | alt | 46.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.452× (z -9.1) |
| [[SW48 (line)]] | wt | 28.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.140× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change |
| [[A-427 (line)]] | wt | 33.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 32.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 34.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 21.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 35.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 50.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 29.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 40.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 46.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5024), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*47 of its nearest partners move with it, 3 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNAP29]] | +0.67 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[UBE2B]] | +0.60 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[INIP]] | +0.59 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[WASHC4]] | +0.59 | +0.69 / +0.45 | both halves | 3e-05 |  |
| [[PIP4P1]] | +0.58 | +0.45 / +0.49 | both halves | 3e-05 |  |
| [[TCAF1]] | +0.57 | +0.56 / +0.45 | both halves | 3e-05 |  |
| [[PRXL2C]] | +0.57 | +0.40 / +0.44 | both halves | 5e-05 |  |
| [[FKBP15]] | +0.56 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[HDAC5]] | +0.56 | +0.43 / +0.45 | both halves | 3e-05 |  |
| [[VPS8]] | +0.55 | +0.46 / +0.43 | both halves | 3e-05 |  |
| [[PIM3]] | +0.55 | +0.57 / +0.47 | both halves | 2e-05 |  |
| [[NECAP2]] | +0.54 | +0.66 / +0.46 | both halves | 2e-05 |  |

## Genes that move opposite

*53 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BEND3]] | -0.63 | -0.52 / -0.54 | both halves | 1e-05 |  |
| [[POC1B-AS1]] | -0.59 | -0.34 / -0.44 | both halves | 1e-04 |  |
| [[CCNJ]] | -0.58 | -0.34 / -0.51 | both halves | 1e-04 |  |
| [[HDAC4]] | -0.57 | -0.59 / -0.59 | both halves | 7e-06 |  |
| [[DDX56]] | -0.57 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[PIGW]] | -0.56 | -0.31 / -0.50 | both halves | 2e-04 |  |
| [[E2F3]] | -0.55 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[PTPRG]] | -0.55 | -0.35 / -0.49 | both halves | 1e-04 |  |
| [[PRDM15]] | -0.55 | -0.36 / -0.54 | both halves | 1e-04 |  |
| [[KANSL1L-AS1]] | -0.54 | -0.41 / -0.36 | both halves | 1e-04 |  |
| [[RNPS1]] | -0.53 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[ARSB]] | -0.53 | -0.30 / -0.51 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **-** arm (projection on the module's main direction -0.534). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (0.1, -34.1); signed map (-19.6, -9.6). **Vector** length 94.8, 21.2% of its response variance represented; |z| ≥ 3 in 998 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +4.8 | +17.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.6 | +22.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.0 | +17.7 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.7 | +14.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.5 | +4.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | +6.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.4 | +2.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.4 | +5.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.3 | +3.7 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -11.2 | -19.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -6.6 | -4.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -5.2 | -3.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.8 | -3.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.8 | -3.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.9 | -5.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.5 | -0.4 |
|  | [[EX229 (drug)]] 5 µM |  | -2.4 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | motile sperm domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp22.2 — chrX:14,873,421-14,922,327 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC26706 |
| Gene groups (HGNC) | CRAL-TRIO lipid binding domain containing; Motile sperm domain containing |
| Reactome | 6 pathways, smallest: RHOD GTPase cycle; Neutrophil degranulation; RHO GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NHP6](https://www.uniprot.org/uniprotkb/Q8NHP6) (Motile sperm domain-containing protein 2):

> Endoplasmic reticulum-anchored protein that mediates the formation of contact sites between the endoplasmic (ER) and endosomes, mitochondria or Golgi through interaction with conventional- and phosphorylated-FFAT-containing organelle-bound proteins. In addition, forms endoplasmic reticulum (ER)-lipid droplets (LDs) contacts through a direct protein-membrane interaction and participates in LDs homeostasis. The attachment mechanism involves an amphipathic helix that has an affinity for lipid …

**Summary**, from NCBI Gene [158747](https://www.ncbi.nlm.nih.gov/gene/158747):

> Enables FFAT motif binding activity. Involved in lipid droplet formation; positive regulation of leukocyte chemotaxis; and protein homooligomerization. Located in endoplasmic reticulum membrane; endoplasmic reticulum-endosome membrane contact site; and plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28381](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28381) · Entrez [158747](https://www.ncbi.nlm.nih.gov/gene/158747) · UniProt [Q8NHP6](https://www.uniprot.org/uniprotkb/Q8NHP6) · Ensembl [ENSG00000130150](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130150)

## Data

Gene col 5024: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5024); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5024, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5024]; `tensor/DDL_lfc|DDL_z.npy` [5024]; `embed/gene_vectors.npy` [5024]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5024 or target_col == 5024). Every well: [[MOSPD2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MOSPD2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
