---
symbol: "AK4"
type: "gene"
col: 8518
ensembl_id: "ENSG00000162433"
name: "adenylate kinase 4"
location: "1p31.3"
module: 144
arm: "+"
pooled_cpm: 63.66
n_lines_expressing: 49
n_dd_up: 12
n_dd_down: 22
n_dd_up_clean: 11
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/144"]
generated_by: "tahoemap"
---

# AK4

*adenylate kinase 4* — 1p31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.17× (z +11.9, q 1e-29, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.227× (z -41.2, q 0e+00, down in 46 of 47 measured lines).
> Its strongest partners by |cos| (88 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 12 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EGLN1]] (+0.78, fdr 7e-06), [[DIPK2A]] (+0.68, fdr 1e-05), [[PGM1]] (+0.65, fdr 7e-06); moves opposite to [[POLM]] (-0.50, fdr 4e-04), [[SLC35C2]] (-0.48, fdr 4e-05), [[PILRB]] (-0.48, fdr 4e-04).
> It is in [[Module 144]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 2 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8518.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.17×** | +11.9 | 1e-29 | 45/48 (HS-578T, HOP62, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.48×** | +11.0 | 1e-25 | 35/48 (NCI-H1573, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.25×** | +8.3 | 2e-14 | 38/47 (HOP62, HS-578T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Roxadustat (drug)]] 5 µM |  | **1.46×** | +7.2 | 1e-10 | 36/47 (HOP62, SNU-423, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.60×** | +4.8 | 2e-04 | 27/47 (SHP-77, SNU-423, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.25×** | +4.4 | 0.001 | 23/47 (A498, H4, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.22×** | +3.9 | 0.008 | 20/47 (NCI-H1573, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.21×** | +3.7 | 0.017 | 21/47 (HOP62, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | **1.22×** | +3.6 | 0.017 | 20/47 (SW 900, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[vincristine (drug)]] 0.05 µM |  | **1.21×** | +3.5 | 0.028 | 15/47 (A549, A498, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM |  | **1.36×** | +3.2 | 0.073 | 12/46 (C32, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~6% here); noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | 1.18× | +3.1 | 0.079 | 15/46 (HepG2/C3A, MIA PaCa-2, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.04× | +3.0 | 0.098 | 0/48 | inconsistent across doses |  |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.24×** | +3.0 | 0.098 | 5/47 (NCI-H2347, LS 180, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Fumaric acid (drug)]] 5 µM |  | 1.17× | +3.0 | 0.098 | 3/48 (RPMI-7951, CFPAC-1, …) | top dose only | plate-row cell shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8518.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.227×** | -41.2 | 0e+00 | 46/47 (C32, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.179×** | -33.9 | 0e+00 | 47/47 (C32, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.192×** | -32.5 | 0e+00 | 47/47 (HEC-1-A, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.266×** | -26.1 | 0e+00 | 47/47 (HEC-1-A, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.344×** | -20.2 | 0e+00 | 40/47 (NCI-H460, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~1% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.394×** | -17.7 | 0e+00 | 46/46 (NCI-H23, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.440×** | -16.2 | 0e+00 | 40/47 (RKO, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.482×** | -14.4 | 6e-45 | 43/47 (SK-MEL-2, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.594×** | -9.9 | 4e-21 | 32/41 (A-172, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **0.688×** | -7.4 | 1e-11 | 33/47 (HEC-1-A, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.497×** | -7.2 | 3e-11 | 34/48 (HEC-1-A, SK-MEL-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.774×** | -7.1 | 5e-11 | 29/47 (SK-MEL-2, C32, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **0.737×** | -6.0 | 8e-08 | 27/47 (RPMI-7951, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.790×** | -4.7 | 1e-04 | 24/47 (SK-MEL-2, HT-29, …) | two highest doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **0.784×** | -4.6 | 1e-04 | 22/46 (HT-29, J82, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.791×** | -4.4 | 4e-04 | 22/47 (C32, H4, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Temsirolimus (drug)]] 0.5 µM |  | **0.832×** | -3.6 | 0.009 | 20/47 (hTERT-HPNE, KATO III, …) | inconsistent across doses |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.709×** | -3.6 | 0.011 | 19/47 (NCI-H460, SHP-77, …) | top dose only | noisy plate (z scaled) |
| [[4EGI-1 (drug)]] 5 µM |  | **0.725×** | -3.3 | 0.025 | 18/47 (LS 180, HCT15, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8518. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 80.3 | 2 | 11 (3 ⚠) | [[PH-797804 (drug)]] 5 µM 4.69× (z +10.3) | [[Homoharringtonine (drug)]] 5 µM 0.136× (z -35.9) |
| [[A-172 (line)]] | wt | 81.6 | 0 | 10 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0725× (z -27.6) |
| [[NCI-H460 (line)]] | wt | 72.6 | 0 | 10 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0928× (z -41.2) |
| [[RPMI-7951 (line)]] | alt | 62.8 | 1 | 9 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 8.64× (z +9.3) | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -20.2) |
| [[SK-MEL-2 (line)]] | alt | 62.2 | 0 | 10 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.102× (z -21.2) |
| [[SW480 (line)]] | alt | 59.4 | 2 | 8 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 3.85× (z +9.3) | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -33.2) |
| [[C32 (line)]] | wt | 172 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0922× (z -42.7) |
| [[HOP62 (line)]] | alt | 84.6 | 3 | 6 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 9.55× (z +11.5) | [[Panobinostat (drug)]] 0.5 µM 0.108× (z -21.7) |
| [[HCT15 (line)]] | alt | 109 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -23.2) |
| [[Hs 766T (line)]] | wt | 30.8 | 1 | 7 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.46× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.175× (z -17.8) |
| [[HS-578T (line)]] | alt | 71.2 | 2 | 6 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 12.1× (z +12.5) | [[Panobinostat (drug)]] 0.5 µM 0.0737× (z -25.1) |
| [[LOX-IMVI (line)]] | wt | 47.9 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.128× (z -24.3) |
| [[NCI-H1573 (line)]] | alt | 34.5 | 2 | 6 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.84× (z +16.3) | [[Homoharringtonine (drug)]] 5 µM 0.224× (z -18.0) |
| [[NCI-H2347 (line)]] | alt | 69.6 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -27.3) |
| [[CFPAC-1 (line)]] | alt | 108 | 1 | 6 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.91× (z +8.7) | [[Panobinostat (drug)]] 5 µM 0.156× (z -22.7) |
| [[LoVo (line)]] | wt | 41.2 | 1 | 6 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.92× (z +14.8) | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -25.3) |
| [[LS 180 (line)]] | wt | 48.1 | 1 | 6 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.25× (z +11.1) | [[Homoharringtonine (drug)]] 5 µM 0.214× (z -21.1) |
| [[NCI-H2030 (line)]] | alt | 73.7 | 1 | 6 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.96× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.138× (z -29.1) |
| [[NCI-H23 (line)]] | alt | 122 | 1 | 6 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.24× (z +9.9) | [[Niclosamide (olamine) (drug)]] 5 µM 0.0894× (z -26.6) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.256× (z -22.2) |
| [[A-427 (line)]] | wt | 46.4 | 0 | 6 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.187× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.337× (z -14.2) |
| [[hTERT-HPNE (line)]] | wt | 47.2 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.151× (z -13.4) |
| [[J82 (line)]] | alt | 48.8 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -17.8) |
| [[SNU-423 (line)]] | alt | 112 | 1 | 5 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.76× (z +9.5) | [[Panobinostat (drug)]] 0.5 µM 0.141× (z -20.3) |
| [[BT-474 (line)]] | alt | 56.5 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.158× (z -15.6) |
| [[C-33 A (line)]] | alt | 90.4 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.288× (z -14.0) |
| [[H4 (line)]] | wt | 82.5 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.0868× (z -25.8) |
| [[HT-29 (line)]] | alt | 51.6 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.142× (z -26.7) |
| [[MIA PaCa-2 (line)]] | alt | 142 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.111× (z -26.2) |
| [[NCI-H1792 (line)]] | alt | 93.7 | 1 | 4 | [[TAK-901 (drug)]] 5 µM 5.19× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.164× (z -27.1) |
| [[Panc 03.27 (line)]] | alt | 57.0 | 2 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.09× (z +10.5) | [[Panobinostat (drug)]] 5 µM 0.160× (z -18.5) |
| [[PANC-1 (line)]] | alt | 34.9 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -19.8) |
| [[RKO (line)]] | wt | 60.3 | 0 | 5 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0256× (z -31.2) |
| [[SW 900 (line)]] | alt | 49.2 | 0 | 5 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.182× (z -13.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.232× (z -12.3) |
| [[SW1417 (line)]] | alt | 40.0 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.167× (z -15.7) |
| [[COLO 205 (line)]] | alt | 26.6 | 1 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.00× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.150× (z -15.6) |
| [[SHP-77 (line)]] | alt | 56.3 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.207× (z -12.0) |
| [[A498 (line)]] | wt | 32.7 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.221× (z -14.5) |
| [[A549 (line)]] | wt | 36.3 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.167× (z -14.6) |
| [[AsPC-1 (line)]] | alt | 23.2 | 0 | 3 | — | [[Harringtonine (drug)]] 5 µM 0.158× (z -12.5) |
| [[KATO III (line)]] | alt | 17.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0924× (z -21.4) |
| [[SNU-1 (line)]] | wt | 54.0 | 0 | 3 | — | [[Harringtonine (drug)]] 5 µM 0.0892× (z -16.5) |
| [[AN3 CA (line)]] | alt | 89.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.136× (z -15.9) |
| [[CHP-212 (line)]] | wt | 38.9 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0711× (z -10.1) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.167× (z -10.1) |
| [[HepG2_C3A (line)]] | wt | 95.9 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.193× (z -13.2) |
| [[SW48 (line)]] | wt | 33.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.115× (z -16.4) |
| [[SW 1271 (line)]] | alt | 84.0 | 0 | 1 | — | [[Radotinib (drug)]] 0.5 µM 0.0909× (z -9.9) |
| [[NCI-H2122 (line)]] | alt | 63.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 64.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.6 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 112 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8518), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 10 of them with an alert (⚠; 10 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EGLN1]] | +0.78 | +0.85 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[DIPK2A]] | +0.68 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[PGM1]] | +0.65 | +0.62 / +0.66 | both halves | 7e-06 | pathway: HALLMARK_HYPOXIA |
| [[STBD1]] | +0.63 | +0.51 / +0.59 | both halves | 1e-05 | pathway: HALLMARK_HYPOXIA |
| [[IPMK]] | +0.62 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[ANP32A]] | +0.61 | +0.49 / +0.64 | both halves | 1e-05 |  |
| [[PDK1]] | +0.60 | +0.78 / +0.60 | both halves | 7e-06 | pathway: HALLMARK_HYPOXIA |
| [[AK2]] | +0.59 | +0.68 / +0.65 | both halves | 7e-06 | same gene group; pathway: Interconversion of nucleotide di- and triphosphates; STRING 556 |
| [[PMS2]] | +0.57 | +0.49 / +0.41 | both halves | 4e-05 |  |
| [[GRPEL1]] | +0.57 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[CHSY1]] | +0.57 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[BMT2]] | +0.57 | +0.67 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLM]] | -0.50 | -0.25 / -0.49 | both halves | 4e-04 |  |
| [[SLC35C2]] | -0.48 | -0.40 / -0.48 | both halves | 4e-05 |  |
| [[PILRB]] | -0.48 | -0.26 / -0.51 | both halves | 4e-04 |  |
| [[MAPK8]] | -0.46 | -0.15 / -0.43 | ⚠ not reproduced | 0.001 |  |
| [[IER2]] | -0.45 | -0.34 / -0.39 | both halves | 1e-04 |  |
| [[RAD23A]] | -0.45 | -0.34 / -0.35 | both halves | 1e-04 |  |
| [[GGA1]] | -0.45 | -0.13 / -0.39 | ⚠ not reproduced | 0.002 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 144]]; 32 genes; every member is in the + arm (projection on the module's main direction 0.670). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-13.4, 17.0); signed map (-41.3, 27.9). **Vector** length 119, 36.4% of its response variance represented; |z| ≥ 3 in 1,262 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +15.6 | +11.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | +9.1 | +11.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +7.1 | +8.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +6.9 | +1.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +6.3 | +4.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.3 | +2.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.6 | +2.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +4.0 | +2.5 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -7.4 | -17.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | -6.1 | -20.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.1 | -41.2 |
|  | [[Rapamycin (drug)]] 5 µM |  | -3.0 | -2.6 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -2.6 | -2.6 |
|  | [[Rapamycin (drug)]] 0.5 µM |  | -2.3 | -2.0 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -2.2 | -3.6 |
|  | [[ULK-101 (drug)]] 0.05 µM |  | -2.0 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | adenylate kinase 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p31.3 — chr1:65,147,549-65,232,145 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously AK3, AK3L1 |
| Gene groups (HGNC) | Adenylate kinases |
| Hallmark sets | GLYCOLYSIS, HYPOXIA, MTORC1_SIGNALING |
| Reactome | 2 pathways, smallest: Interconversion of nucleotide di- and triphosphates; Metabolism of nucleotides |
| Matched by | ensembl_id |

**Function**, from UniProt [P27144](https://www.uniprot.org/uniprotkb/P27144) (Adenylate kinase 4, mitochondrial):

> Broad-specificity mitochondrial nucleoside phosphate kinase involved in cellular nucleotide homeostasis by catalyzing nucleoside-phosphate interconversions. Similar to other adenylate kinases, preferentially catalyzes the phosphorylation of the nucleoside monophosphate AMP with ATP as phosphate donor to produce ADP. Phosphorylates only AMP when using GTP as phosphate donor. In vitro, can also catalyze the phosphorylation of CMP, dAMP and dCMP and use GTP as an alternate phosphate donor. …

**Summary**, from NCBI Gene [205](https://www.ncbi.nlm.nih.gov/gene/205):

> This gene encodes a member of the adenylate kinase family of enzymes. The encoded protein is localized to the mitochondrial matrix. Adenylate kinases regulate the adenine and guanine nucleotide compositions within a cell by catalyzing the reversible transfer of phosphate group among these nucleotides. Five isozymes of adenylate kinase have been identified in vertebrates. Expression of these isozymes is tissue-specific and developmentally regulated. A pseudogene for this gene has been located on …

**Accessions** — [HGNC:363](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:363) · Entrez [205](https://www.ncbi.nlm.nih.gov/gene/205) · UniProt [P27144](https://www.uniprot.org/uniprotkb/P27144) · Ensembl [ENSG00000162433](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162433)

## Data

Gene col 8518: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8518); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8518, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8518]; `tensor/DDL_lfc|DDL_z.npy` [8518]; `embed/gene_vectors.npy` [8518]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8518 or target_col == 8518). Every well: [[AK4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AK4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
