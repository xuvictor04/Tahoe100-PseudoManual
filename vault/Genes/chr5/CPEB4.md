---
symbol: "CPEB4"
type: "gene"
col: 3499
ensembl_id: "ENSG00000113742"
name: "cytoplasmic polyadenylation element binding protein 4"
location: "5q35.2"
module: 6
arm: "-"
pooled_cpm: 124.86
n_lines_expressing: 49
n_dd_up: 39
n_dd_down: 1
n_dd_up_clean: 35
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# CPEB4

*cytoplasmic polyadenylation element binding protein 4* — 5q35.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 39 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.88× (z +59.3, q 0e+00, up in 45 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Radotinib (drug)]] 5 µM: 0.787× (z -9.0, q 2e-16, down in 34 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (KATO III 0.231×, HT-29 0.341×, A-172 0.403×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 2 lines (HepG2/C3A 0.270×, NCI-H1792 0.372×; ⚠ toxic; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (COLO 205 0.380×, HT-29 0.462×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change); [[Radotinib (drug)]] 5 µM in 1 line (AsPC-1 0.411×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATP6V1D]] (+0.57, fdr 2e-05), [[TUT7]] (+0.53, fdr 2e-05), [[AFF4]] (+0.53, fdr 5e-05); moves opposite to [[NUP93]] (-0.60, fdr 1e-05), [[NCAPD3]] (-0.59, fdr 1e-05), [[CSE1L]] (-0.58, fdr 1e-05).
> It sits in the **-** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 59 in all, 12 with an alert ⚠; shown: the 15 strongest. 39 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3499.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.88×** | +59.3 | 0e+00 | 45/47 (PANC-1, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.59×** | +33.8 | 0e+00 | 40/47 (HS-578T, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **3.31×** | +31.7 | 0e+00 | 47/47 (HS-578T, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.09×** | +29.8 | 0e+00 | 46/47 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 5 µM |  | **3.14×** | +29.1 | 0e+00 | 42/47 (PANC-1, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.96×** | +28.7 | 0e+00 | 46/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.99×** | +25.8 | 0e+00 | 40/48 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.20×** | +20.8 | 0e+00 | 45/47 (PANC-1, A-172, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **3.07×** | +15.5 | 0e+00 | 39/48 (PANC-1, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.75×** | +14.7 | 0e+00 | 43/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.60×** | +12.4 | 1e-33 | 35/47 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.35×** | +11.3 | 5e-28 | 29/47 (LS 180, NCI-H460, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.47×** | +9.9 | 3e-21 | 27/49 (NCI-H460, HS-578T, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.30×** | +9.7 | 1e-20 | 32/47 (A-427, NCI-H2347, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~14% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.29×** | +9.5 | 1e-19 | 29/47 (J82, HOP62, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3499.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (KATO III 0.231×, HT-29 0.341×, A-172 0.403×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 2 lines (HepG2/C3A 0.270×, NCI-H1792 0.372×; ⚠ toxic; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (COLO 205 0.380×, HT-29 0.462×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change); [[Radotinib (drug)]] 5 µM in 1 line (AsPC-1 0.411×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Radotinib (drug)]] 5 µM |  | **0.787×** | -9.0 | 2e-16 | 34/47 (AsPC-1, PANC-1, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.946× | -4.8 | 4e-04 | 2/49 (MIA PaCa-2, NCI-H23) | inconsistent across doses |  |
| [[Bentamapimod (drug)]] 0.05 µM |  | 0.868× | -3.5 | 0.093 | 17/46 (J82, LoVo, …) | inconsistent across doses |  |
| [[Ralimetinib dimesylate (drug)]] 5 µM |  | 0.788× | -3.3 | 0.13 | 7/47 (hTERT-HPNE, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | 0.884× | -3.3 | 0.13 | 12/47 (SW480, A498, …) | inconsistent across doses |  |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | 0.883× | -3.2 | 0.14 | 9/47 (AsPC-1, A549, …) | top dose only |  |
| [[Riluzole hydrochloride (drug)]] 5 µM |  | 0.921× | -3.1 | 0.15 | 1/48 (RKO) | top dose only |  |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 0.922× | -3.1 | 0.15 | 6/47 (KATO III, A498, …) | inconsistent across doses |  |
| [[Bentamapimod (drug)]] 5 µM |  | 0.803× | -3.0 | 0.15 | 6/47 (CFPAC-1, LoVo, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3499. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 93.6 | 22 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.54× (z +40.7) | — |
| [[PANC-1 (line)]] | alt | 104 | 15 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.24× (z +48.0) | — |
| [[A498 (line)]] | wt | 89.0 | 14 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.28× (z +29.0) | — |
| [[J82 (line)]] | alt | 60.2 | 13 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.63× (z +29.2) | — |
| [[SW480 (line)]] | alt | 130 | 13 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.29× (z +30.2) | — |
| [[HOP62 (line)]] | alt | 69.3 | 12 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.5× (z +37.5) | — |
| [[HS-578T (line)]] | alt | 135 | 12 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.67× (z +36.6) | — |
| [[LOX-IMVI (line)]] | wt | 78.4 | 12 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.88× (z +32.1) | — |
| [[A-172 (line)]] | wt | 217 | 10 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.17× (z +30.5) | [[Dinaciclib (drug)]] 5 µM 0.403× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 100 | 11 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.06× (z +19.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 61.5 | 11 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.5× (z +32.8) | — |
| [[A-427 (line)]] | wt | 56.9 | 10 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.35× (z +23.6) | — |
| [[LS 180 (line)]] | wt | 61.9 | 10 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.13× (z +18.9) | — |
| [[NCI-H2030 (line)]] | alt | 130 | 10 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.30× (z +27.4) | — |
| [[NCI-H2347 (line)]] | alt | 102 | 10 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.15× (z +29.7) | — |
| [[HEC-1-A (line)]] | alt | 41.8 | 9 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.26× (z +23.0) | — |
| [[hTERT-HPNE (line)]] | wt | 107 | 9 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.3× (z +31.3) | — |
| [[SK-MEL-2 (line)]] | alt | 154 | 9 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.4× (z +42.7) | — |
| [[A549 (line)]] | wt | 107 | 8 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.08× (z +22.4) | — |
| [[NCI-H1573 (line)]] | alt | 61.9 | 8 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.3× (z +28.8) | — |
| [[NCI-H23 (line)]] | alt | 40.6 | 8 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.83× (z +26.8) | — |
| [[CFPAC-1 (line)]] | alt | 170 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.86× (z +33.3) | — |
| [[RKO (line)]] | wt | 90.9 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.73× (z +19.5) | — |
| [[AsPC-1 (line)]] | alt | 97.9 | 5 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.73× (z +19.8) | [[Radotinib (drug)]] 5 µM 0.411× (z -11.4) |
| [[HT-29 (line)]] | alt | 207 | 3 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +14.5) | [[Dinaciclib (drug)]] 5 µM 0.341× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 62.0 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.97× (z +19.1) | — |
| [[NCI-H1792 (line)]] | alt | 108 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.09× (z +28.2) | [[Niclosamide (olamine) (drug)]] 5 µM 0.372× (z -10.5) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[RPMI-7951 (line)]] | alt | 138 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.93× (z +25.2) | — |
| [[SNU-423 (line)]] | alt | 262 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.96× (z +22.0) | — |
| [[KATO III (line)]] | alt | 210 | 4 (1 ⚠) | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.77× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.231× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 33.2 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.3× (z +18.7) | — |
| [[SW 900 (line)]] | alt | 425 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.38× (z +22.7) | — |
| [[SW1417 (line)]] | alt | 253 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +15.8) | — |
| [[C32 (line)]] | wt | 266 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.59× (z +33.5) | — |
| [[HCT15 (line)]] | alt | 73.3 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +12.4) | — |
| [[Hs 766T (line)]] | wt | 95.7 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.71× (z +17.7) | — |
| [[Panc 03.27 (line)]] | alt | 164 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +13.8) | — |
| [[AN3 CA (line)]] | alt | 82.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.42× (z +11.7) | — |
| [[C-33 A (line)]] | alt | 32.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.18× (z +11.2) | — |
| [[H4 (line)]] | wt | 137 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +13.1) | — |
| [[HepG2_C3A (line)]] | wt | 340 | 2 | 1 (1 ⚠) | [[Digitoxin (drug)]] 0.5 µM 3.09× (z +11.7) | [[Niclosamide (olamine) (drug)]] 5 µM 0.270× (z -13.1) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 125 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.39× (z +13.4) | — |
| [[COLO 205 (line)]] | alt | 452 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.380× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[SW 1088 (line)]] | alt | 220 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.64× (z +11.0) | — |
| [[CHP-212 (line)]] | wt | 113 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 248 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 56.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 125 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 30.8 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3499), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*23 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP6V1D]] | +0.57 | +0.61 / +0.48 | both halves | 2e-05 |  |
| [[TUT7]] | +0.53 | +0.59 / +0.46 | both halves | 2e-05 |  |
| [[AFF4]] | +0.53 | +0.40 / +0.48 | both halves | 5e-05 |  |
| [[LINC01504]] | +0.53 | +0.46 / +0.55 | both halves | 3e-05 |  |
| [[RNF103-CHMP3]] | +0.51 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[NIT1]] | +0.50 | +0.34 / +0.53 | both halves | 1e-04 |  |
| [[LRIF1]] | +0.50 | +0.46 / +0.58 | both halves | 3e-05 |  |
| [[UBL3]] | +0.50 | +0.56 / +0.43 | both halves | 3e-05 |  |
| [[GADD45A]] | +0.49 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[RAB7A]] | +0.49 | +0.34 / +0.41 | both halves | 1e-04 |  |
| [[ERN1]] | +0.49 | +0.42 / +0.50 | both halves | 4e-05 |  |
| [[C11orf96]] | +0.48 | +0.50 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*77 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUP93]] | -0.60 | -0.55 / -0.58 | both halves | 1e-05 |  |
| [[NCAPD3]] | -0.59 | -0.59 / -0.54 | both halves | 1e-05 |  |
| [[CSE1L]] | -0.58 | -0.62 / -0.52 | both halves | 1e-05 |  |
| [[POLE2]] | -0.56 | -0.61 / -0.45 | both halves | 3e-05 |  |
| [[DDX12P]] | -0.55 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[RANBP1]] | -0.55 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[ALG6]] | -0.55 | -0.58 / -0.45 | both halves | 3e-05 |  |
| [[MMS22L]] | -0.54 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[NDC1]] | -0.54 | -0.58 / -0.54 | both halves | 1e-05 |  |
| [[LMNB1]] | -0.54 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[CDCA7]] | -0.53 | -0.54 / -0.45 | both halves | 3e-05 |  |
| [[CCDC88C]] | -0.53 | -0.52 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CPEB4's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.8% of all compounds | 0.071 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **-** arm (projection on the module's main direction -0.494). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-31.1, -43.8); signed map (5.6, 24.0). **Vector** length 113, 36.8% of its response variance represented; |z| ≥ 3 in 1,691 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +8.3 | +20.8 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.8 | +15.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.7 | +11.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.5 | +6.1 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.0 | +4.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +4.8 | +4.9 |
|  | [[Entrectinib (drug)]] 5 µM |  | +4.1 | +4.3 |
|  | [[Belzutifan (drug)]] 5 µM |  | +3.4 | +3.0 |
| fall | [[Radotinib (drug)]] 5 µM |  | -5.7 | -9.0 |
|  | [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.2 | -2.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.1 | +2.3 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | -3.1 | -3.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | -3.1 | +31.7 |
|  | [[Bentamapimod (drug)]] 0.05 µM |  | -3.0 | -3.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.9 | -0.2 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -2.6 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | cytoplasmic polyadenylation element binding protein 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q35.2 — chr5:173,888,349-173,961,980 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1673 |
| Gene groups (HGNC) | RNA binding motif containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q17RY0](https://www.uniprot.org/uniprotkb/Q17RY0) (Cytoplasmic polyadenylation element-binding protein 4):

> Sequence-specific RNA-binding protein that binds to the cytoplasmic polyadenylation element (CPE), an uridine-rich sequence element (consensus sequence 5'-UUUUUAU-3') within the mRNA 3'-UTR. RNA binding results in a clear conformational change analogous to the Venus fly trap mechanism. Regulates activation of unfolded protein response (UPR) in the process of adaptation to ER stress in liver, by maintaining translation of CPE-regulated mRNAs in conditions in which global protein synthesis is …

**Summary**, from NCBI Gene [80315](https://www.ncbi.nlm.nih.gov/gene/80315):

> Enables RNA binding activity. Predicted to be involved in several processes, including cellular response to glucose starvation; negative regulation of cytoplasmic translation; and response to ischemia. Located in cytoplasm and nucleus. Biomarker of liver cirrhosis; portal hypertension; and primary biliary cholangitis. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:21747](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21747) · Entrez [80315](https://www.ncbi.nlm.nih.gov/gene/80315) · UniProt [Q17RY0](https://www.uniprot.org/uniprotkb/Q17RY0) · Ensembl [ENSG00000113742](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000113742)

## Data

Gene col 3499: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3499); `tables/drug_effects.parquet` (68 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3499, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3499]; `tensor/DDL_lfc|DDL_z.npy` [3499]; `embed/gene_vectors.npy` [3499]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3499 or target_col == 3499). Every well: [[CPEB4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CPEB4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
