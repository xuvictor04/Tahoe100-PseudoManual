---
symbol: "PRELID3B"
type: "gene"
col: 2084
ensembl_id: "ENSG00000101166"
name: "PRELI domain containing 3B"
location: "20q13.32"
module: 25
arm: "+"
pooled_cpm: 54.18
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 3
n_dd_up_clean: 14
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# PRELID3B

*PRELI domain containing 3B* — 20q13.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.49× (z +21.2, q 0e+00, up in 46 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.53× (z +7.2, q 7e-11, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.719× (z -7.9, q 2e-12, down in 30 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LIN7C]] (+0.77, fdr 7e-06), [[NRAS]] (+0.74, fdr 7e-06), [[OCRL]] (+0.74, fdr 7e-06); moves opposite to [[SNHG9]] (-0.72, fdr 1e-05), [[NDUFC1]] (-0.67, fdr 1e-05), [[SMIM27]] (-0.67, fdr 7e-06).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2084.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.49×** | +21.2 | 0e+00 | 46/47 (SW480, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.21×** | +19.0 | 0e+00 | 42/43 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.54×** | +14.6 | 1e-45 | 39/43 (SW480, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.57×** | +7.3 | 3e-11 | 40/47 (A-427, SNU-423, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.53×** | +7.2 | 7e-11 | 38/48 (BT-474, NCI-H23, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.29×** | +6.0 | 1e-07 | 26/48 (NCI-H2347, CFPAC-1, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.35×** | +5.0 | 4e-05 | 30/48 (NCI-H2030, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.34×** | +5.0 | 5e-05 | 23/47 (A-427, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~17% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~36% of this change | **1.28×** | +4.1 | 0.002 | 23/46 (SW 900, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Riluzole hydrochloride (drug)]] 0.5 µM |  | **1.27×** | +4.1 | 0.003 | 27/48 (SHP-77, KATO III, …) | inconsistent across doses | position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **1.54×** | +3.8 | 0.006 | 20/48 (NCI-H2030, NCI-H1792, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.26×** | +3.8 | 0.008 | 19/48 (NCI-H1792, C32, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.05 µM |  | **1.26×** | +3.6 | 0.014 | 20/48 (HOP62, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.23×** | +3.5 | 0.018 | 17/48 (NCI-H2030, PANC-1, …) | inconsistent across doses | position effect removed |
| [[Raltitrexed (drug)]] 0.5 µM |  | **1.23×** | +3.5 | 0.021 | 17/48 (SW1417, NCI-H2347, …) | inconsistent across doses | position effect removed |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.21×** | +3.2 | 0.042 | 16/48 (SW48, LS 180, …) | inconsistent across doses |  |
| [[Cilostazol (drug)]] 0.05 µM |  | **1.22×** | +3.2 | 0.046 | 16/47 (SW1417, NCI-H1792, …) | inconsistent across doses | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **1.42×** | +3.1 | 0.057 | 19/49 (SW480, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~22% here); composition shift; noisy plate (z scaled) |
| [[Pralsetinib (drug)]] 5 µM |  | **1.42×** | +3.1 | 0.058 | 15/48 (SNU-423, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.19× | +2.9 | 0.091 | 15/48 (NCI-H2030, SW1417, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2084.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.719×** | -7.9 | 2e-12 | 30/48 (LoVo, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.893× | -6.5 | 3e-08 | 6/49 (NCI-H2030, NCI-H23, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.798×** | -3.8 | 0.024 | 19/48 (A-427, NCI-H23, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[ULK-101 (drug)]] 0.05 µM |  | **0.806×** | -3.5 | 0.076 | 16/48 (LS 180, SW1417, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | 0.829× | -3.2 | 0.16 | 20/47 (AsPC-1, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ciclopirox (drug)]] 5 µM |  | 0.878× | -3.1 | 0.17 | 14/48 (SHP-77, NCI-H460, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2084. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 57.8 | 2 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 3.81× (z +12.1) ⚠ toxic; transcription drop | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.239× (z -20.0) |
| [[Hs 766T (line)]] | wt | 101 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.05× (z +13.8) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.502× (z -9.8) |
| [[MIA PaCa-2 (line)]] | alt | 36.7 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.67× (z +12.4) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.430× (z -10.1) |
| [[NCI-H1792 (line)]] | alt | 35.6 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.89× (z +16.8) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 72.4 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.28× (z +18.4) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.579× (z -10.0) |
| [[A498 (line)]] | wt | 50.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.52× (z +13.4) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 33.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.49× (z +14.1) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 25.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.69× (z +12.9) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 75.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.53× (z +12.6) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 82.9 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.34× (z +9.3) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.250× (z -22.6) |
| [[LOX-IMVI (line)]] | wt | 33.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.28× (z +13.0) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 70.4 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.62× (z +9.5) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.405× (z -12.8) |
| [[NCI-H460 (line)]] | wt | 44.7 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 5.37× (z +15.3) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.388× (z -12.6) |
| [[PANC-1 (line)]] | alt | 56.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.97× (z +15.3) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 35.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.67× (z +12.9) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 26.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.59× (z +10.8) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 80.2 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.70× (z +9.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.547× (z -8.9) ⚠ cell-cycle shift, would explain all of this change |
| [[CFPAC-1 (line)]] | alt | 37.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.72× (z +11.8) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 37.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.75× (z +9.9) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 34.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.63× (z +9.9) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 58.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.75× (z +10.3) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 69.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.58× (z +10.3) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 46.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.26× (z +12.7) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 75.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.24× (z +12.9) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 101 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.78× (z +14.5) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 52.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.91× (z +13.9) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 87.0 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.408× (z -12.3) |
| [[RPMI-7951 (line)]] | alt | 39.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.05× (z +9.1) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 92.3 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.03× (z +10.2) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.397× (z -12.3) |
| [[SW1417 (line)]] | alt | 92.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.49× (z +10.4) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 37.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.49× (z +10.6) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 15.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.26× (z +8.5) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 47.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.37× (z +11.4) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 37.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.71× (z +8.8) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 51.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.54× (z +13.0) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 87.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 26.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 67.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 26.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 42.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 45.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 67.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 80.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 56.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 53.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2084), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*57 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LIN7C]] | +0.77 | +0.64 / +0.84 | both halves | 7e-06 |  |
| [[NRAS]] | +0.74 | +0.71 / +0.79 | both halves | 7e-06 |  |
| [[OCRL]] | +0.74 | +0.61 / +0.81 | both halves | 7e-06 |  |
| [[ZNF460]] | +0.70 | +0.69 / +0.77 | both halves | 7e-06 |  |
| [[NONO]] | +0.70 | +0.51 / +0.79 | both halves | 1e-05 |  |
| [[IPO8]] | +0.68 | +0.56 / +0.70 | both halves | 1e-05 |  |
| [[ZNF664]] | +0.68 | +0.61 / +0.72 | both halves | 7e-06 |  |
| [[EIF4H]] | +0.68 | +0.53 / +0.76 | both halves | 1e-05 |  |
| [[DLD]] | +0.68 | +0.59 / +0.69 | both halves | 7e-06 |  |
| [[CCT7]] | +0.67 | +0.68 / +0.74 | both halves | 7e-06 |  |
| [[TWF1]] | +0.67 | +0.65 / +0.72 | both halves | 7e-06 |  |
| [[API5]] | +0.67 | +0.50 / +0.70 | both halves | 1e-05 |  |

## Genes that move opposite

*43 of its nearest partners move opposite, 5 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNHG9]] | -0.72 | -0.51 / -0.77 | both halves | 1e-05 |  |
| [[NDUFC1]] | -0.67 | -0.56 / -0.67 | both halves | 1e-05 |  |
| [[SMIM27]] | -0.67 | -0.58 / -0.68 | both halves | 7e-06 |  |
| [[TMEM258]] | -0.67 | -0.57 / -0.69 | both halves | 1e-05 |  |
| [[LINC00685]] | -0.65 | -0.41 / -0.72 | both halves | 4e-05 |  |
| [[NDUFA1]] | -0.65 | -0.65 / -0.61 | both halves | 7e-06 |  |
| [[NDUFA13]] ⚠ | -0.64 | -0.60 / -0.55 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[SELENOH]] | -0.64 | -0.50 / -0.63 | both halves | 1e-05 |  |
| [[CTBP1-AS]] ⚠ | -0.63 | -0.46 / -0.68 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[HIC2]] | -0.63 | -0.55 / -0.66 | both halves | 1e-05 |  |
| [[COX6B1]] | -0.63 | -0.52 / -0.67 | both halves | 1e-05 |  |
| [[TRNAU1AP]] | -0.63 | -0.50 / -0.67 | both halves | 1e-05 |  |
| [[RBX1]] | -0.63 | -0.49 / -0.64 | both halves | 1e-05 |  |
| [[TERF2IP]] | -0.63 | -0.43 / -0.66 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.765). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-31.5, -20.4); signed map (-15.7, -37.4). **Vector** length 103, 26.4% of its response variance represented; |z| ≥ 3 in 924 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.7 | +19.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.4 | +21.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.7 | +14.6 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.5 | +6.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.3 | +5.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.2 | +7.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.0 | +3.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.9 | +2.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.8 | +1.5 |
|  | [[Erlotinib (drug)]] 5 µM |  | +2.6 | +2.0 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.7 | -7.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.9 | -3.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -4.5 | -3.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.3 | -1.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.9 | -2.7 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | -2.7 | -0.6 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | -2.6 | -0.7 |
|  | [[Bergenin (drug)]] 0.5 µM |  | -2.4 | -1.3 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -2.3 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | PRELI domain containing 3B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.32 — chr20:59,033,145-59,042,809 (-) |
| Ensembl biotype | protein_coding |
| Also known as | dJ543J19.5; previously C20orf45, SLMO2 |
| Gene groups (HGNC) | PRELI domain containing |
| Hallmark sets | KRAS_SIGNALING_UP |
| Matched by | ensembl_id |

UniProt [Q9Y3B1](https://www.uniprot.org/uniprotkb/Q9Y3B1) carries no function annotation.

**Summary**, from NCBI Gene [51012](https://www.ncbi.nlm.nih.gov/gene/51012):

> Predicted to enable phosphatidic acid transfer activity. Predicted to be involved in phospholipid transport. Located in mitochondrion. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:15892](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15892) · Entrez [51012](https://www.ncbi.nlm.nih.gov/gene/51012) · UniProt [Q9Y3B1](https://www.uniprot.org/uniprotkb/Q9Y3B1) · Ensembl [ENSG00000101166](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101166)

## Data

Gene col 2084: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2084); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2084, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2084]; `tensor/DDL_lfc|DDL_z.npy` [2084]; `embed/gene_vectors.npy` [2084]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2084 or target_col == 2084). Every well: [[PRELID3B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRELID3B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
