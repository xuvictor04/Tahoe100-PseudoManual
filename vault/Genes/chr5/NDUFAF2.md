---
symbol: "NDUFAF2"
type: "gene"
col: 8896
ensembl_id: "ENSG00000164182"
name: "NADH:ubiquinone oxidoreductase complex assembly factor 2"
location: "5q12.1"
module: 5
arm: "+"
pooled_cpm: 99.49
n_lines_expressing: 50
n_dd_up: 38
n_dd_down: 0
n_dd_up_clean: 25
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# NDUFAF2

*NADH:ubiquinone oxidoreductase complex assembly factor 2* — 5q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 38 drug-doses (13 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.87× (z +13.3, q 8e-38, up in 43 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 7 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (SHP-77 0.223×, NCI-H23 0.200×, A498 0.554×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Adagrasib (drug)]] 0.05 µM in 2 lines (MIA PaCa-2 0.679×, NCI-H23 0.721×; ⚠ position not correctable); [[Auranofin (drug)]] 5 µM in 2 lines (RKO 0.471×, HEC-1-A 0.492×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (HEC-1-A 0.596×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WDR4]] (+0.66, fdr 7e-06), [[LYRM4]] (+0.66, fdr 7e-06), [[PRMT3]] (+0.65, fdr 7e-06); moves opposite to [[ALAD]] (-0.55, fdr 3e-05), [[DBP]] (-0.55, fdr 1e-05), [[MTMR11]] (-0.55, fdr 2e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 48 in all, 17 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 38 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8896.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.87×** | +13.3 | 8e-38 | 43/48 (SW 900, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.55×** | +13.2 | 4e-37 | 37/49 (CFPAC-1, HT-29, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.76×** | +12.0 | 8e-31 | 45/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.76×** | +11.9 | 1e-30 | 40/48 (SW 900, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.62×** | +10.3 | 1e-22 | 39/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.60×** | +9.9 | 2e-21 | 37/48 (NCI-H2347, NCI-H460, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.60×** | +9.9 | 3e-21 | 39/48 (SW480, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.62×** | +9.7 | 2e-20 | 41/48 (PANC-1, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.55×** | +9.2 | 2e-18 | 35/48 (A-172, HT-29, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.49×** | +8.5 | 9e-16 | 35/48 (A-172, NCI-H2347, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.51×** | +8.4 | 2e-15 | 36/47 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.47×** | +8.2 | 8e-15 | 33/48 (A-172, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.46×** | +8.0 | 6e-14 | 33/48 (NCI-H1573, A-172, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.46×** | +7.7 | 5e-13 | 34/48 (SW480, Panc 03.27, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.45×** | +7.6 | 1e-12 | 28/48 (hTERT-HPNE, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.39×** | +6.9 | 1e-10 | 30/48 (PANC-1, HS-578T, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.25×** | +6.7 | 8e-10 | 24/48 (NCI-H2347, A-172, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.33×** | +6.0 | 5e-08 | 23/48 (Panc 03.27, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.18× | +4.9 | 2e-05 | 19/49 (MIA PaCa-2, H4, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.50×** | +4.5 | 2e-04 | 28/48 (NCI-H1792, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.24×** | +4.5 | 2e-04 | 23/47 (NCI-H460, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8896.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 7 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (SHP-77 0.223×, NCI-H23 0.200×, A498 0.554×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Adagrasib (drug)]] 0.05 µM in 2 lines (MIA PaCa-2 0.679×, NCI-H23 0.721×; ⚠ position not correctable); [[Auranofin (drug)]] 5 µM in 2 lines (RKO 0.471×, HEC-1-A 0.492×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (HEC-1-A 0.596×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | 0.840× | -4.3 | 0.010 | 18/50 (LoVo, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 0.868× | -3.7 | 0.069 | 14/48 (LoVo, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | 0.857× | -3.5 | 0.070 | 18/49 (AsPC-1, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 0.893× | -3.5 | 0.070 | 9/48 (RKO, AsPC-1, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.857× | -3.3 | 0.089 | 14/49 (LoVo, MIA PaCa-2, …) | all doses, flat |  |
| [[Filgotinib (drug)]] 5 µM |  | 0.860× | -3.3 | 0.089 | 9/48 (PANC-1, SW 900, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | 0.855× | -3.3 | 0.089 | 20/47 (LoVo, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.858× | -3.1 | 0.15 | 12/48 (LoVo, MIA PaCa-2, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.34 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8896. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 236 | 0 | 7 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.430× (z -10.5) ⚠ toxic; cell-cycle shift, explains ~91% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.596× (z -9.5) |
| [[NCI-H2347 (line)]] | alt | 89.2 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.92× (z +28.0) | — |
| [[SW 900 (line)]] | alt | 96.3 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.78× (z +18.0) | — |
| [[Panc 03.27 (line)]] | alt | 87.9 | 5 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.02× (z +10.4) | — |
| [[PANC-1 (line)]] | alt | 114 | 5 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.22× (z +12.7) | — |
| [[SW480 (line)]] | alt | 109 | 5 (2 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.29× (z +11.3) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.20× (z +11.2) | — |
| [[A-172 (line)]] | wt | 71.5 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.18× (z +26.6) | — |
| [[CFPAC-1 (line)]] | alt | 55.4 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.43× (z +19.2) | — |
| [[NCI-H460 (line)]] | wt | 128 | 4 (2 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.64× (z +12.2) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.68× (z +9.6) | — |
| [[SNU-423 (line)]] | alt | 86.8 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +15.8) | — |
| [[H4 (line)]] | wt | 77.2 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.50× (z +10.0) | — |
| [[SHP-77 (line)]] | alt | 113 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.22× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.223× (z -17.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 94.2 | 2 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.60× (z +10.5) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.15× (z +8.8) | — |
| [[HT-29 (line)]] | alt | 51.3 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.61× (z +10.8) | — |
| [[hTERT-HPNE (line)]] | wt | 71.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.19× (z +14.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 162 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.03× (z +9.0) | — |
| [[NCI-H2030 (line)]] | alt | 82.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.67× (z +9.1) | — |
| [[NCI-H23 (line)]] | alt | 73.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.43× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.200× (z -15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 122 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +12.2) | — |
| [[A498 (line)]] | wt | 149 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.554× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 34.6 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.28× (z +8.6) | — |
| [[LoVo (line)]] | wt | 115 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.85× (z +10.4) | — |
| [[LOX-IMVI (line)]] | wt | 95.3 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.18× (z +8.7) | — |
| [[NCI-H1573 (line)]] | alt | 34.9 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.95× (z +8.5) ⚠ cell-cycle shift, explains ~52% of this change | — |
| [[NCI-H1792 (line)]] | alt | 117 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.83× (z +10.2) | — |
| [[RKO (line)]] | wt | 242 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.471× (z -9.4) |
| [[A-427 (line)]] | wt | 116 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 103 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 178 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 85.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 55.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 84.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 69.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 93.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 75.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 80.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 61.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 57.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 70.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 70.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 92.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 76.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 71.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 133 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 80.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 71.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 124 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8896), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDR4]] | +0.66 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[LYRM4]] | +0.66 | +0.62 / +0.65 | both halves | 7e-06 | pathway: Aerobic respiration and respiratory electron transport |
| [[PRMT3]] | +0.65 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[PUS1]] | +0.65 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[CMSS1]] | +0.65 | +0.69 / +0.72 | both halves | 7e-06 |  |
| [[ATR]] | +0.64 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[DDX31]] | +0.63 | +0.56 / +0.70 | both halves | 1e-05 |  |
| [[ADCY3]] | +0.63 | +0.58 / +0.61 | both halves | 8e-06 |  |
| [[GART]] | +0.63 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[SDAD1]] | +0.63 | +0.53 / +0.67 | both halves | 1e-05 |  |
| [[PUM3]] | +0.62 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[METTL8]] | +0.62 | +0.65 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALAD]] | -0.55 | -0.67 / -0.45 | both halves | 3e-05 |  |
| [[DBP]] | -0.55 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[MTMR11]] | -0.55 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[BPNT1]] | -0.51 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[VWA5A]] | -0.51 | -0.39 / -0.43 | both halves | 6e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.684). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-11.9, -33.9); signed map (-0.6, -51.2). **Vector** length 121, 39.4% of its response variance represented; |z| ≥ 3 in 1,480 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +7.8 | +9.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +5.4 | +12.0 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +4.6 | +9.7 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +4.5 | +8.2 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | +4.3 | +9.9 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +4.1 | +3.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.0 | +4.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.0 | +3.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.7 | +2.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.6 | +4.5 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -4.6 | +6.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.4 | +1.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.4 | -3.0 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | -4.1 | -1.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~96% of this change | -3.9 | +3.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.4 | -3.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.3 | -3.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.1 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | NADH:ubiquinone oxidoreductase complex assembly factor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q12.1 — chr5:60,945,177-61,154,531 (+) |
| Ensembl biotype | protein_coding |
| Also known as | B17.2L, MMTN, mimitin; previously NDUFA12L |
| Gene groups (HGNC) | Mitochondrial respiratory chain complex assembly factors |
| Reactome | 3 pathways, smallest: Complex I biogenesis; Respiratory electron transport; Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N183](https://www.uniprot.org/uniprotkb/Q8N183) (NADH dehydrogenase):

> Acts as a molecular chaperone for mitochondrial complex I assembly. Complex I functions in the transfer of electrons from NADH to the respiratory chain. The immediate electron acceptor for the enzyme is believed to be ubiquinone. Is involved in the initial steps of cilia formation, including removal of CP110 from the mother centrioles, docking of membrane vesicles to the mother centrioles, and establishment of the transition zone.

**Summary**, from NCBI Gene [91942](https://www.ncbi.nlm.nih.gov/gene/91942):

> NADH:ubiquinone oxidoreductase (complex I) catalyzes the transfer of electrons from NADH to ubiquinone (coenzyme Q) in the first step of the mitochondrial respiratory chain, resulting in the translocation of protons across the inner mitochondrial membrane. This gene encodes a complex I assembly factor. Mutations in this gene cause progressive encephalopathy resulting from mitochondrial complex I deficiency. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:28086](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28086) · Entrez [91942](https://www.ncbi.nlm.nih.gov/gene/91942) · UniProt [Q8N183](https://www.uniprot.org/uniprotkb/Q8N183) · Ensembl [ENSG00000164182](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164182)

## Data

Gene col 8896: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8896); `tables/drug_effects.parquet` (56 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8896, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8896]; `tensor/DDL_lfc|DDL_z.npy` [8896]; `embed/gene_vectors.npy` [8896]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8896 or target_col == 8896). Every well: [[NDUFAF2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NDUFAF2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
