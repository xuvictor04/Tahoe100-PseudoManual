---
symbol: "SIRT2"
type: "gene"
col: 904
ensembl_id: "ENSG00000068903"
name: "sirtuin 2"
location: "19q13.2"
module: 4
arm: "-"
pooled_cpm: 44.02
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 3
n_dd_up_clean: 12
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# SIRT2

*sirtuin 2* — 19q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.44× (z +18.5, q 0e+00, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.570× (z -7.9, q 1e-12, down in 27 of 38 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Demeclocycline (drug)]] 5 µM: 0.846× (z -3.5, q 0.075, down in 17 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (HT-29 0.208×, NCI-H661 0.153×, HepG2/C3A 0.142×, SW480 0.318×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 4 lines (KATO III 0.159×, NCI-H661 0.154×, HT-29 0.390×, HOP62 0.355×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (HT-29 0.198×, AN3 CA 0.0918×, A-172 0.348×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Auranofin (drug)]] 5 µM in 1 line (SNU-423 0.240×); [[Palmatine (chloride) (drug)]] 0.5 µM in 1 line (SW48 0.124×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (HT-29 0.516×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GABARAP]] (+0.72, fdr 7e-06, ⚠ GABARAP in the vector space only through flagged drug-doses), [[VEGFB]] (+0.71, fdr 7e-06), [[SAT2]] (+0.71, fdr 7e-06), [[TTC21A]] (+0.71, fdr 7e-06); moves opposite to [[DARS2]] (-0.76, fdr 7e-06), [[ABCF2]] (-0.76, fdr 7e-06), [[CCT5]] (-0.75, fdr 7e-06).
> It sits in the **-** arm of [[Module 004]] (MYC targets v1).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 3 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 904.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.44×** | +18.5 | 0e+00 | 42/48 (AsPC-1, PANC-1, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.66×** | +14.4 | 2e-44 | 48/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.49×** | +13.4 | 2e-38 | 47/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.43×** | +13.0 | 1e-36 | 40/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **2.34×** | +12.5 | 1e-33 | 46/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.11×** | +11.0 | 5e-26 | 41/48 (NCI-H460, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.55×** | +6.2 | 5e-08 | 31/46 (RKO, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.48×** | +5.8 | 5e-07 | 31/48 (NCI-H460, BT-474, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.32×** | +5.7 | 6e-07 | 26/48 (HS-578T, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.49×** | +5.7 | 8e-07 | 33/48 (AsPC-1, PANC-1, …) | top dose only | cell-cycle shift (explains ~16% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.45×** | +5.4 | 3e-06 | 33/48 (PANC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.69×** | +4.0 | 0.003 | 23/49 (PANC-1, SK-MEL-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.29×** | +3.7 | 0.010 | 24/48 (PANC-1, LS 180, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.28×** | +3.7 | 0.010 | 22/48 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.6 | 0.010 | 15/48 (KATO III, Hs 766T, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | 1.16× | +3.2 | 0.056 | 14/48 (SW 900, LOX-IMVI, …) | top dose only |  |
| [[Terfenadine (drug)]] 5 µM |  | 1.15× | +3.0 | 0.091 | 10/48 (J82, Hs 766T, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 4 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 904.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (HT-29 0.208×, NCI-H661 0.153×, HepG2/C3A 0.142×, SW480 0.318×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 4 lines (KATO III 0.159×, NCI-H661 0.154×, HT-29 0.390×, HOP62 0.355×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (HT-29 0.198×, AN3 CA 0.0918×, A-172 0.348×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Auranofin (drug)]] 5 µM in 1 line (SNU-423 0.240×); [[Palmatine (chloride) (drug)]] 0.5 µM in 1 line (SW48 0.124×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (HT-29 0.516×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.570×** | -7.9 | 1e-12 | 27/38 (HT-29, NCI-H661, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.669×** | -5.5 | 1e-05 | 25/41 (KATO III, NCI-H661, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.904× | -5.2 | 3e-05 | 2/49 (C32, HCT15) | inconsistent across doses |  |
| [[Demeclocycline (drug)]] 5 µM |  | 0.846× | -3.5 | 0.075 | 17/48 (SW 900, H4, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.648×** | -3.3 | 0.097 | 13/48 (HT-29, NCI-H2347, …) | all doses, flat | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.801× | -3.3 | 0.10 | 18/48 (HT-29, HOP62, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 904. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 108 | 5 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +14.2) | [[Dinaciclib (drug)]] 5 µM 0.208× (z -16.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.516× (z -10.0) |
| [[PANC-1 (line)]] | alt | 108 | 8 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.79× (z +18.8) | — |
| [[NCI-H460 (line)]] | wt | 30.7 | 7 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 10.8× (z +20.8) | — |
| [[KATO III (line)]] | alt | 48.0 | 5 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +11.2) | [[Dinaciclib (drug)]] 0.05 µM 0.159× (z -12.5) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 49.8 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.29× (z +19.1) | — |
| [[BT-474 (line)]] | alt | 31.2 | 5 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 8.70× (z +13.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 8.45× (z +13.6) | — |
| [[HS-578T (line)]] | alt | 50.1 | 5 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.50× (z +11.0) | — |
| [[J82 (line)]] | alt | 27.4 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.45× (z +11.9) | — |
| [[LoVo (line)]] | wt | 39.8 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.36× (z +16.1) | — |
| [[SW480 (line)]] | alt | 34.0 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.06× (z +14.4) | [[Dinaciclib (drug)]] 5 µM 0.318× (z -9.7) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 42.0 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +11.1) | — |
| [[NCI-H2030 (line)]] | alt | 32.3 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.45× (z +10.5) | — |
| [[Panc 03.27 (line)]] | alt | 33.8 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +10.9) | — |
| [[SW1417 (line)]] | alt | 44.0 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +13.1) | — |
| [[A-172 (line)]] | wt | 52.7 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +9.8) | [[Dinaciclib (drug)]] 0.5 µM 0.348× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 21.8 | 3 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.21× (z +10.0) | — |
| [[A549 (line)]] | wt | 57.5 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.81× (z +10.5) | — |
| [[HEC-1-A (line)]] | alt | 47.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +10.3) | — |
| [[HOP62 (line)]] | alt | 44.3 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +11.1) | [[Dinaciclib (drug)]] 0.05 µM 0.355× (z -8.6) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 37.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.27× (z +14.2) | — |
| [[A498 (line)]] | wt | 32.7 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.07× (z +8.9) | — |
| [[HepG2_C3A (line)]] | wt | 23.0 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.68× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.142× (z -10.4) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 49.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.43× (z +16.2) | — |
| [[NCI-H1573 (line)]] | alt | 18.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.82× (z +10.9) | — |
| [[NCI-H23 (line)]] | alt | 17.5 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.45× (z +8.9) | — |
| [[NCI-H2347 (line)]] | alt | 24.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +11.6) | — |
| [[NCI-H661 (line)]] | alt | 126 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.153× (z -10.5) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 31.3 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 7.18× (z +9.6) | — |
| [[AN3 CA (line)]] | alt | 52.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0918× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 68.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +11.5) | — |
| [[H4 (line)]] | wt | 50.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +9.1) | — |
| [[Hs 766T (line)]] | wt | 55.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +10.9) | — |
| [[hTERT-HPNE (line)]] | wt | 35.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.237× (z -9.1) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 18.5 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.96× (z +8.8) | — |
| [[SNU-423 (line)]] | alt | 37.4 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.240× (z -11.2) |
| [[SW 900 (line)]] | alt | 52.4 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.98× (z +8.9) | — |
| [[SW48 (line)]] | wt | 39.6 | 0 | 1 | — | [[Palmatine (chloride) (drug)]] 0.5 µM 0.124× (z -10.8) |
| [[C-33 A (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 38.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 55.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 44.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 46.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 47.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 50.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 48.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 51.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 50.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 31.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 904), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*52 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GABARAP]] ⚠ | +0.72 | +0.69 / +0.66 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[VEGFB]] | +0.71 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[SAT2]] | +0.71 | +0.72 / +0.67 | both halves | 7e-06 |  |
| [[TTC21A]] | +0.71 | +0.66 / +0.73 | both halves | 7e-06 |  |
| [[DENND6B]] | +0.71 | +0.56 / +0.71 | both halves | 1e-05 |  |
| [[CRY2]] | +0.70 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[INAFM1]] | +0.68 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[RAB2B]] | +0.68 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[PHPT1]] | +0.68 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[CCS]] | +0.68 | +0.59 / +0.70 | both halves | 7e-06 |  |
| [[SEC22A]] | +0.67 | +0.57 / +0.71 | both halves | 9e-06 |  |
| [[AAMDC]] | +0.67 | +0.71 / +0.63 | both halves | 7e-06 |  |
| [[IFI27L2]] | +0.67 | +0.61 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*48 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DARS2]] | -0.76 | -0.60 / -0.72 | both halves | 7e-06 |  |
| [[ABCF2]] | -0.76 | -0.70 / -0.72 | both halves | 7e-06 |  |
| [[CCT5]] | -0.75 | -0.74 / -0.74 | both halves | 7e-06 |  |
| [[TMEM33]] | -0.71 | -0.69 / -0.72 | both halves | 7e-06 |  |
| [[WDR77]] | -0.71 | -0.69 / -0.68 | both halves | 7e-06 |  |
| [[RUVBL1]] | -0.70 | -0.75 / -0.70 | both halves | 7e-06 |  |
| [[ATIC]] | -0.70 | -0.69 / -0.67 | both halves | 7e-06 |  |
| [[EBNA1BP2]] | -0.70 | -0.66 / -0.65 | both halves | 7e-06 |  |
| [[CCT7]] | -0.69 | -0.65 / -0.61 | both halves | 7e-06 |  |
| [[PSME3]] | -0.68 | -0.59 / -0.68 | both halves | 7e-06 |  |
| [[EIF4G1]] | -0.68 | -0.59 / -0.69 | both halves | 7e-06 |  |
| [[CCT6A]] | -0.67 | -0.70 / -0.60 | both halves | 7e-06 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **-** arm (projection on the module's main direction -0.716). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-22.5, -31.7); signed map (-27.5, 11.3). **Vector** length 121, 37.2% of its response variance represented; |z| ≥ 3 in 979 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.2 | +11.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.9 | +1.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +3.9 | +13.0 |
|  | [[Entrectinib (drug)]] 5 µM |  | +3.7 | +2.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.3 | +3.2 |
|  | [[Adagrasib (drug)]] 5 µM |  | +2.8 | +2.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.8 | +2.3 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.6 | -3.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.4 | -2.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.3 | -2.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -5.0 | -1.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.8 | -0.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.3 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | sirtuin 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.2 — chr19:38,878,555-38,899,862 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously SIR2L |
| Gene groups (HGNC) | Sirtuins |
| Hallmark sets | COAGULATION, MYOGENESIS |
| Reactome | 7 pathways, smallest: Initiation of Nuclear Envelope (NE) Reformation; Nuclear Envelope (NE) Reassembly; Mitotic Anaphase |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IXJ6](https://www.uniprot.org/uniprotkb/Q8IXJ6) (NAD-dependent protein deacetylase sirtuin-2):

> NAD-dependent protein deacetylase, which deacetylates internal lysines on histone and alpha-tubulin as well as many other proteins such as key transcription factors. Participates in the modulation of multiple and diverse biological processes such as cell cycle control, genomic integrity, microtubule dynamics, cell differentiation, metabolic networks, and autophagy. Plays a major role in the control of cell cycle progression and genomic stability. Functions in the antephase checkpoint preventing …

**Summary**, from NCBI Gene [22933](https://www.ncbi.nlm.nih.gov/gene/22933):

> This gene encodes a member of the sirtuin family of proteins, homologs to the yeast Sir2 protein. Members of the sirtuin family are characterized by a sirtuin core domain and grouped into four classes. The functions of human sirtuins have not yet been determined; however, yeast sirtuin proteins are known to regulate epigenetic gene silencing and suppress recombination of rDNA. Studies suggest that the human sirtuins may function as intracellular regulatory proteins with …

**Accessions** — [HGNC:10886](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10886) · Entrez [22933](https://www.ncbi.nlm.nih.gov/gene/22933) · UniProt [Q8IXJ6](https://www.uniprot.org/uniprotkb/Q8IXJ6) · Ensembl [ENSG00000068903](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000068903)

## Data

Gene col 904: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 904); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 904, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 904]; `tensor/DDL_lfc|DDL_z.npy` [904]; `embed/gene_vectors.npy` [904]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 904 or target_col == 904). Every well: [[SIRT2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SIRT2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
