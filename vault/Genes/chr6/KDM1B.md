---
symbol: "KDM1B"
type: "gene"
col: 9066
ensembl_id: "ENSG00000165097"
name: "lysine demethylase 1B"
location: "6p22.3"
module: 26
arm: "-"
pooled_cpm: 48.61
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 13
n_dd_up_clean: 13
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# KDM1B

*lysine demethylase 1B* — 6p22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.09× (z +31.3, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.563× (z -15.9, q 0e+00, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (81 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 20 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TPMT]] (+0.68, fdr 1e-05, ⚠ same locus), [[FLNB]] (+0.62, fdr 1e-04), [[ETHE1]] (+0.57, fdr 1e-04), [[SMIM29]] (+0.56, fdr 2e-05); moves opposite to [[B9D2]] (-0.62, fdr 1e-05), [[XNDC1N-ZNF705EP-ALG1L9P]] (-0.60, fdr 1e-04), [[ZNF876P]] (-0.58, fdr 2e-04).
> It sits in the **-** arm of [[Module 026]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9066.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.09×** | +31.3 | 0e+00 | 48/48 (J82, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.89×** | +29.5 | 0e+00 | 48/48 (J82, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.66×** | +27.2 | 0e+00 | 48/48 (J82, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.69×** | +20.5 | 0e+00 | 37/48 (PANC-1, J82, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.97×** | +18.9 | 0e+00 | 45/48 (J82, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.49×** | +15.8 | 0e+00 | 42/48 (J82, NCI-H460, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **2.16×** | +11.2 | 3e-27 | 41/48 (J82, HOP62, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.49×** | +11.1 | 7e-27 | 37/47 (SW480, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.29×** | +7.1 | 7e-11 | 27/48 (J82, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.30×** | +7.1 | 8e-11 | 21/40 (SHP-77, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.59×** | +6.8 | 6e-10 | 27/48 (J82, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.23×** | +5.8 | 2e-07 | 16/48 (Panc 03.27, SW480, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.16× | +5.8 | 3e-07 | 12/48 (HOP62, NCI-H460, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.21×** | +5.2 | 8e-06 | 16/48 (J82, H4, …) | two highest doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +4.7 | 1e-04 | 21/48 (PANC-1, HEC-1-A, …) | top dose only | composition shift |
| [[Bentamapimod (drug)]] 5 µM |  | **1.36×** | +4.5 | 2e-04 | 8/48 (A-427, PANC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.21×** | +3.8 | 0.005 | 6/48 (A498, NCI-H2030, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.14× | +3.7 | 0.006 | 14/47 (SW48, NCI-H460, …) | two highest doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9066.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.563×** | -15.9 | 0e+00 | 38/48 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.634×** | -12.6 | 5e-34 | 38/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.653×** | -11.8 | 8e-30 | 34/47 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.672×** | -11.0 | 6e-26 | 33/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.773×** | -7.1 | 1e-10 | 24/48 (LoVo, RKO, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.778×** | -6.9 | 4e-10 | 22/48 (LoVo, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.792×** | -6.5 | 9e-09 | 25/48 (MIA PaCa-2, NCI-H23, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.790×** | -6.3 | 2e-08 | 23/47 (A-172, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.660×** | -6.0 | 1e-07 | 22/48 (HOP62, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.940× | -5.7 | 6e-07 | 2/48 (NCI-H1792, SW 1088) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.864× | -5.7 | 6e-07 | 17/48 (SNU-1, MIA PaCa-2, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.678×** | -5.6 | 9e-07 | 20/47 (LoVo, SW48, …) | top dose only | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.822×** | -5.1 | 1e-05 | 20/47 (SW48, LoVo, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~17% of this change | 0.847× | -4.6 | 2e-04 | 18/47 (NCI-H460, H4, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.860× | -3.8 | 0.005 | 15/47 (RKO, LoVo, …) | inconsistent across doses | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.874× | -3.7 | 0.007 | 16/48 (J82, SK-MEL-2, …) | rises with dose |  |
| [[Sulfatinib (drug)]] 5 µM |  | 0.872× | -3.6 | 0.010 | 13/48 (HS-578T, HOP62, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | 0.834× | -3.6 | 0.011 | 12/47 (NCI-H1573, AsPC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Acetohexamide (drug)]] 5 µM |  | 0.922× | -3.1 | 0.043 | 5/48 (A498, Hs 766T, …) | top dose only |  |
| [[ERK5-IN-2 (drug)]] 5 µM |  | **0.807×** | -3.1 | 0.048 | 4/48 (SW48, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9066. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 52.4 | 5 | 4 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.11× (z +16.4) | [[Digitoxin (drug)]] 5 µM 0.340× (z -15.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.370× (z -14.4) |
| [[J82 (line)]] | alt | 78.7 | 8 | 0 | [[Panobinostat (drug)]] 5 µM 4.95× (z +20.3) | — |
| [[LoVo (line)]] | wt | 88.7 | 4 | 4 (3 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.47× (z +11.2) | [[Digitoxin (drug)]] 5 µM 0.364× (z -12.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.453× (z -9.8) |
| [[A-172 (line)]] | wt | 43.7 | 4 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.73× (z +16.8) | [[Dinaciclib (drug)]] 5 µM 0.336× (z -9.5) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 24.1 | 6 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.59× (z +14.3) | [[Digitoxin (drug)]] 5 µM 0.282× (z -11.9) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 31.5 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 6.61× (z +17.1) | — |
| [[A-427 (line)]] | wt | 64.5 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +9.8) | — |
| [[HEC-1-A (line)]] | alt | 46.5 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +16.3) | — |
| [[PANC-1 (line)]] | alt | 75.1 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +20.0) | — |
| [[RKO (line)]] | wt | 28.8 | 3 | 2 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.73× (z +9.9) | [[Digitoxin (drug)]] 5 µM 0.175× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.279× (z -8.8) |
| [[A498 (line)]] | wt | 35.6 | 4 | 0 | [[Tucidinostat (drug)]] 5 µM 2.07× (z +10.0) | — |
| [[C32 (line)]] | wt | 23.1 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 6.17× (z +10.6) | — |
| [[CFPAC-1 (line)]] | alt | 34.5 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +13.8) | — |
| [[HepG2_C3A (line)]] | wt | 46.1 | 3 | 1 (1 ⚠) | [[Belinostat (drug)]] 5 µM 4.04× (z +9.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.408× (z -8.9) ⚠ cell-cycle shift, explains ~47% of this change |
| [[HT-29 (line)]] | alt | 49.5 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.06× (z +11.8) | [[Digitoxin (drug)]] 5 µM 0.382× (z -10.3) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 32.6 | 4 | 0 | [[Panobinostat (drug)]] 0.5 µM 5.94× (z +11.3) | — |
| [[KATO III (line)]] | alt | 35.1 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 4.40× (z +13.1) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.335× (z -9.7) |
| [[LOX-IMVI (line)]] | wt | 60.1 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.38× (z +13.6) | [[Digitoxin (drug)]] 5 µM 0.392× (z -10.5) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 36.9 | 4 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.82× (z +10.5) | — |
| [[Panc 03.27 (line)]] | alt | 32.5 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +11.5) | — |
| [[SK-MEL-2 (line)]] | alt | 33.2 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 4.27× (z +11.2) | — |
| [[SW 900 (line)]] | alt | 17.3 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 6.52× (z +11.0) | — |
| [[AsPC-1 (line)]] | alt | 47.5 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.65× (z +11.8) | — |
| [[C-33 A (line)]] | alt | 35.8 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.12× (z +9.7) | — |
| [[HS-578T (line)]] | alt | 57.1 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.20× (z +12.2) | — |
| [[LS 180 (line)]] | wt | 83.0 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.374× (z -10.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.411× (z -9.8) |
| [[MIA PaCa-2 (line)]] | alt | 61.4 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.85× (z +10.7) | — |
| [[NCI-H1792 (line)]] | alt | 32.6 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.12× (z +11.3) | — |
| [[NCI-H2030 (line)]] | alt | 63.7 | 3 | 0 | [[Belinostat (drug)]] 5 µM 2.56× (z +10.7) | — |
| [[SNU-423 (line)]] | alt | 54.3 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.78× (z +13.3) | — |
| [[SW1417 (line)]] | alt | 57.6 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.46× (z +10.2) | — |
| [[BT-474 (line)]] | alt | 34.7 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.33× (z +9.3) | — |
| [[NCI-H1573 (line)]] | alt | 31.4 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.74× (z +9.3) | — |
| [[NCI-H23 (line)]] | alt | 88.2 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.12× (z +9.6) | — |
| [[RPMI-7951 (line)]] | alt | 32.5 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.15× (z +9.8) | — |
| [[SNU-1 (line)]] | wt | 33.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +8.8) | [[Digitoxin (drug)]] 5 µM 0.226× (z -8.6) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 107 | 0 | 2 | — | [[TAK-901 (drug)]] 0.05 µM 0.228× (z -10.8) |
| [[A549 (line)]] | wt | 47.3 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.58× (z +9.4) | — |
| [[CHP-212 (line)]] | wt | 27.9 | 0 | 1 | — | [[Resveratrol (drug)]] 0.5 µM 0.0784× (z -9.6) |
| [[COLO 205 (line)]] | alt | 29.0 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.06× (z +8.6) | — |
| [[H4 (line)]] | wt | 21.6 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 6.48× (z +9.3) | — |
| [[HCT15 (line)]] | alt | 62.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.310× (z -10.1) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 38.4 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.00× (z +8.7) | — |
| [[SW 1271 (line)]] | alt | 78.3 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.0985× (z -9.3) |
| [[AN3 CA (line)]] | alt | 61.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 42.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 64.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 32.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9066), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*44 of its nearest partners move with it, 4 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TPMT]] | +0.68 | +0.54 / +0.70 | both halves | 1e-05 | ⚠ same locus (0.3 kb: neighbours can correlate without regulation) |
| [[FLNB]] | +0.62 | +0.43 / +0.35 | both halves | 1e-04 |  |
| [[ETHE1]] | +0.57 | +0.51 / +0.35 | both halves | 1e-04 |  |
| [[SMIM29]] | +0.56 | +0.63 / +0.48 | both halves | 2e-05 |  |
| [[SERPINB1]] | +0.56 | +0.45 / +0.32 | both halves | 2e-04 |  |
| [[SMS]] | +0.56 | +0.50 / +0.26 | both halves | 4e-04 |  |
| [[CDA]] | +0.54 | +0.39 / +0.34 | both halves | 1e-04 |  |
| [[EML2]] | +0.54 | +0.55 / +0.31 | both halves | 2e-04 |  |
| [[LPCAT2]] | +0.54 | +0.36 / +0.39 | both halves | 1e-04 |  |
| [[DTD1]] | +0.53 | +0.38 / +0.31 | both halves | 2e-04 |  |
| [[N4BP3]] | +0.53 | +0.54 / +0.35 | both halves | 1e-04 |  |
| [[GDPD5]] | +0.52 | +0.45 / +0.37 | both halves | 9e-05 |  |
| [[STAM2]] | +0.52 | +0.38 / +0.35 | both halves | 1e-04 | pathway: Deubiquitination |

## Genes that move opposite

*56 of its nearest partners move opposite, 16 of them with an alert (⚠; 16 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[B9D2]] | -0.62 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[XNDC1N-ZNF705EP-ALG1L9P]] | -0.60 | -0.34 / -0.42 | both halves | 1e-04 |  |
| [[ZNF876P]] | -0.58 | -0.45 / -0.29 | both halves | 2e-04 |  |
| [[MYLK4]] | -0.57 | -0.36 / -0.29 | both halves | 3e-04 |  |
| [[NEK11]] | -0.56 | -0.30 / -0.45 | both halves | 2e-04 |  |
| [[FBXL19-AS1]] | -0.56 | -0.34 / -0.37 | both halves | 1e-04 |  |
| [[GAS2]] | -0.56 | -0.32 / -0.20 | both halves | 7e-04 |  |
| [[ZFX]] | -0.56 | -0.31 / -0.45 | both halves | 2e-04 |  |
| [[RNPC3-DT]] | -0.55 | -0.33 / -0.19 | ⚠ not reproduced | 8e-04 |  |
| [[SRRM2-AS1]] | -0.55 | -0.24 / -0.34 | both halves | 5e-04 |  |
| [[LAMTOR5-AS1]] | -0.55 | -0.51 / -0.25 | both halves | 4e-04 |  |
| [[EFCAB2]] | -0.54 | -0.31 / -0.36 | both halves | 2e-04 |  |
| [[CATSPERE]] | -0.54 | -0.35 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **-** arm (projection on the module's main direction -0.497). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (15.6, 5.9); signed map (-4.8, 45.1). **Vector** length 106, 28.0% of its response variance represented; |z| ≥ 3 in 1,320 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.8 | +15.8 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.6 | +18.9 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.5 | +27.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.2 | +11.2 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | +4.0 | +2.7 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +3.4 | +2.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.3 | +1.2 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +3.1 | +5.8 |
| fall | [[Auranofin (drug)]] 5 µM |  | -8.3 | -6.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | -7.9 | +2.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.5 | -3.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -6.5 | -5.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -5.0 | -12.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -4.6 | -5.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | -4.2 | -2.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.8 | -7.1 |

## What is on record

|  |  |
|---|---|
| Name | lysine demethylase 1B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p22.3 — chr6:18,155,329-18,223,854 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ34109, FLJ33898, dJ298J15.2, bA204B7.3, FLJ43328, LSD2; previously C6orf193, AOF1 |
| Gene groups (HGNC) | Zinc fingers CW-type; Flavoproteins; Lysine demethylase 1 family |
| Reactome | 10 pathways, smallest: HDMs demethylate histones; NR1H3 & NR1H2 regulate gene expression linked to cholesterol transport and efflux; NR1H2 and NR1H3-mediated signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NB78](https://www.uniprot.org/uniprotkb/Q8NB78) (Lysine-specific histone demethylase 2):

> Histone demethylase that demethylates 'Lys-4' of histone H3, a specific tag for epigenetic transcriptional activation, thereby acting as a corepressor. Required for de novo DNA methylation of a subset of imprinted genes during oogenesis. Acts by oxidizing the substrate by FAD to generate the corresponding imine that is subsequently hydrolyzed. Demethylates both mono- and di-methylated 'Lys-4' of histone H3. Has no effect on tri-methylated 'Lys-4', mono-, di- or tri-methylated 'Lys-9', mono-, …

**Summary**, from NCBI Gene [221656](https://www.ncbi.nlm.nih.gov/gene/221656):

> Flavin-dependent histone demethylases, such as KDM1B, regulate histone lysine methylation, an epigenetic mark that regulates gene expression and chromatin function (Karytinos et al., 2009 [PubMed 19407342]).[supplied by OMIM, Oct 2009]

**Accessions** — [HGNC:21577](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21577) · Entrez [221656](https://www.ncbi.nlm.nih.gov/gene/221656) · UniProt [Q8NB78](https://www.uniprot.org/uniprotkb/Q8NB78) · Ensembl [ENSG00000165097](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165097)

## Data

Gene col 9066: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9066); `tables/drug_effects.parquet` (55 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9066, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9066]; `tensor/DDL_lfc|DDL_z.npy` [9066]; `embed/gene_vectors.npy` [9066]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9066 or target_col == 9066). Every well: [[KDM1B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KDM1B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
