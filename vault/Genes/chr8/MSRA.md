---
symbol: "MSRA"
type: "gene"
col: 10652
ensembl_id: "ENSG00000175806"
name: "methionine sulfoxide reductase A"
location: "8p23.1"
module: 30
arm: "-"
pooled_cpm: 35.12
n_lines_expressing: 48
n_dd_up: 17
n_dd_down: 14
n_dd_up_clean: 15
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# MSRA

*methionine sulfoxide reductase A* — 8p23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.11× (z +15.4, q 0e+00, up in 36 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (2 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.432× (z -12.2, q 1e-31, down in 40 of 46 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ERCC6L2]] (+0.72, fdr 1e-05), [[AGO2]] (+0.68, fdr 7e-06), [[TMEM117]] (+0.66, fdr 1e-05); moves opposite to [[SNAPC3]] (-0.72, fdr 7e-06), [[MYPOP]] (-0.68, fdr 1e-05), [[CRYZL1]] (-0.68, fdr 7e-06).
> It sits in the **-** arm of [[Module 030]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 2 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10652.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.11×** | +15.4 | 0e+00 | 36/46 (A-172, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.29×** | +12.0 | 6e-31 | 39/46 (A-172, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.51×** | +8.4 | 7e-15 | 37/46 (A498, hTERT-HPNE, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.52×** | +6.0 | 2e-07 | 28/46 (AsPC-1, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.51×** | +6.0 | 2e-07 | 30/46 (AsPC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.51×** | +5.8 | 7e-07 | 28/46 (SK-MEL-2, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.47×** | +5.6 | 2e-06 | 25/46 (AsPC-1, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.43×** | +5.0 | 3e-05 | 21/44 (A-172, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.41×** | +5.0 | 4e-05 | 24/46 (C32, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.40×** | +4.7 | 2e-04 | 23/46 (C32, NCI-H2347, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.37×** | +4.5 | 3e-04 | 22/46 (A498, A-427, …) | two highest doses | cell-cycle shift (explains ~3% here) |
| [[BAY1125976 (drug)]] 5 µM |  | **1.78×** | +4.4 | 6e-04 | 21/46 (SW480, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.05 µM |  | **1.34×** | +4.0 | 0.002 | 16/46 (SK-MEL-2, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.38×** | +3.7 | 0.008 | 17/46 (A-172, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.30×** | +3.7 | 0.009 | 17/46 (LoVo, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.27×** | +3.4 | 0.026 | 18/46 (LoVo, A549, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.31×** | +3.1 | 0.056 | 15/46 (RKO, A-427, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 3 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10652.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.432×** | -12.2 | 1e-31 | 40/46 (SW480, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.437×** | -12.1 | 5e-31 | 40/46 (RKO, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.526×** | -9.4 | 1e-18 | 35/46 (RKO, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.550×** | -8.7 | 4e-16 | 35/46 (RKO, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.674×** | -5.8 | 1e-06 | 24/46 (RKO, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.675×** | -5.5 | 3e-06 | 26/45 (SW1417, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Radotinib (drug)]] 5 µM |  | **0.790×** | -4.9 | 9e-05 | 25/46 (RKO, NCI-H23, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.530×** | -4.8 | 9e-05 | 22/46 (RKO, J82, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.721×** | -4.8 | 1e-04 | 21/46 (MIA PaCa-2, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 0.05 µM |  | **0.750×** | -3.9 | 0.006 | 17/45 (NCI-H1573, SW480, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.770×** | -3.8 | 0.007 | 19/46 (KATO III, LoVo, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.795×** | -3.6 | 0.013 | 17/46 (SW480, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 0.847× | -3.2 | 0.066 | 15/46 (SW480, NCI-H23, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | **0.802×** | -3.1 | 0.076 | 16/46 (RKO, SW 1271, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.862× | -3.1 | 0.076 | 19/46 (SNU-1, CFPAC-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.811×** | -3.1 | 0.079 | 12/46 (A-172, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.00 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10652. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 107 | 0 | 8 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.154× (z -15.8) |
| [[AsPC-1 (line)]] | alt | 96.7 | 4 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +11.5) | [[Panobinostat (drug)]] 5 µM 0.330× (z -8.7) |
| [[MIA PaCa-2 (line)]] | alt | 64.4 | 2 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.83× (z +9.6) | [[Adagrasib (drug)]] 0.05 µM 0.666× (z -9.8) ⚠ position not correctable · without an alert: [[Belinostat (drug)]] 5 µM 0.268× (z -9.5) |
| [[NCI-H23 (line)]] | alt | 79.0 | 0 | 5 (2 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.584× (z -14.7) ⚠ position not correctable · without an alert: [[Belinostat (drug)]] 5 µM 0.300× (z -9.7) |
| [[AN3 CA (line)]] | alt | 137 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0731× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.247× (z -10.8) |
| [[RKO (line)]] | wt | 81.6 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.0928× (z -17.7) |
| [[SK-MEL-2 (line)]] | alt | 58.7 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.23× (z +18.5) | [[Dinaciclib (drug)]] 5 µM 0.243× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 36.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 24.0× (z +31.6) | — |
| [[HS-578T (line)]] | alt | 20.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.1× (z +19.0) | — |
| [[hTERT-HPNE (line)]] | wt | 32.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.8× (z +23.3) | — |
| [[J82 (line)]] | alt | 17.6 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +10.1) | [[Belinostat (drug)]] 5 µM 0.221× (z -9.8) |
| [[KATO III (line)]] | alt | 48.2 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.250× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.295× (z -10.7) |
| [[A498 (line)]] | wt | 15.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.92× (z +13.4) | — |
| [[H4 (line)]] | wt | 52.7 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.107× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.134× (z -12.0) |
| [[HOP62 (line)]] | alt | 14.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.42× (z +10.7) | [[Adagrasib (drug)]] 0.05 µM 0.634× (z -10.2) ⚠ position not correctable |
| [[LoVo (line)]] | wt | 21.3 | 1 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.33× (z +9.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.138× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 19.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -10.4) |
| [[A549 (line)]] | wt | 33.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +9.6) | — |
| [[C-33 A (line)]] | alt | 10.1 | 0 | 1 | — | [[Canagliflozin (drug)]] 5 µM 0.0731× (z -8.7) |
| [[C32 (line)]] | wt | 35.4 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.19× (z +8.9) | — |
| [[CFPAC-1 (line)]] | alt | 12.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +8.6) | — |
| [[COLO 205 (line)]] | alt | 25.1 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.200× (z -8.8) |
| [[HepG2_C3A (line)]] | wt | 42.8 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.188× (z -9.4) |
| [[Hs 766T (line)]] | wt | 47.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.16× (z +12.8) | — |
| [[NCI-H2347 (line)]] | alt | 20.3 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.46× (z +8.7) | — |
| [[SHP-77 (line)]] | alt | 14.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.36× (z +10.7) | — |
| [[SNU-1 (line)]] | wt | 47.1 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.299× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 17.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.97× (z +10.5) | — |
| [[SW 1271 (line)]] | alt | 55.8 | 0 | 1 | — | [[Vismodegib (drug)]] 0.05 µM 0.0682× (z -8.9) |
| [[SW1417 (line)]] | alt | 20.7 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.215× (z -10.1) ⚠ toxic |
| [[A-427 (line)]] | wt | 24.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.83 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 28.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 76.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 41.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 23.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.05 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 50.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 38.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10652), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*50 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ERCC6L2]] | +0.72 | +0.72 / +0.53 | both halves | 1e-05 |  |
| [[AGO2]] | +0.68 | +0.58 / +0.68 | both halves | 7e-06 |  |
| [[TMEM117]] | +0.66 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[ITPRIPL2]] | +0.66 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[KDSR]] | +0.66 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[LINC02516]] | +0.66 | +0.70 / +0.42 | both halves | 4e-05 |  |
| [[AVEN]] | +0.66 | +0.63 / +0.50 | both halves | 1e-05 |  |
| [[WARS2-AS1]] | +0.65 | +0.58 / +0.41 | both halves | 4e-05 |  |
| [[ENOX2]] | +0.64 | +0.64 / +0.49 | both halves | 1e-05 |  |
| [[ST7L]] | +0.64 | +0.62 / +0.43 | both halves | 3e-05 |  |
| [[LTBP2]] | +0.64 | +0.58 / +0.66 | both halves | 7e-06 |  |
| [[NEPRO-AS1]] | +0.64 | +0.60 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*50 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNAPC3]] | -0.72 | -0.70 / -0.60 | both halves | 7e-06 |  |
| [[MYPOP]] | -0.68 | -0.61 / -0.55 | both halves | 1e-05 |  |
| [[CRYZL1]] | -0.68 | -0.66 / -0.60 | both halves | 7e-06 |  |
| [[SLC9A6]] | -0.65 | -0.61 / -0.47 | both halves | 2e-05 |  |
| [[SUFU]] | -0.64 | -0.51 / -0.56 | both halves | 1e-05 |  |
| [[USP30]] | -0.64 | -0.66 / -0.54 | both halves | 1e-05 |  |
| [[SDHAP1]] | -0.63 | -0.61 / -0.46 | both halves | 2e-05 |  |
| [[RAB3A]] | -0.63 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[NCK1]] | -0.62 | -0.56 / -0.55 | both halves | 1e-05 |  |
| [[PLEKHH3]] | -0.62 | -0.59 / -0.52 | both halves | 1e-05 |  |
| [[PHAF1]] | -0.62 | -0.59 / -0.51 | both halves | 1e-05 |  |
| [[HACE1]] | -0.62 | -0.56 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers MSRA's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.4% of all compounds | 0.015 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **-** arm (projection on the module's main direction -0.745). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (2.1, -5.9); signed map (15.9, -2.6). **Vector** length 126, 35.2% of its response variance represented; |z| ≥ 3 in 1,226 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +10.6 | +12.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +8.8 | +8.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +8.3 | +15.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.7 | +5.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.9 | +3.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.1 | +0.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.8 | +4.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.5 | +2.7 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | +3.3 | +2.4 |
| fall | [[Belinostat (drug)]] 5 µM |  | -5.5 | -12.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -5.2 | -12.1 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -5.2 | -8.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.1 | -9.4 |
|  | [[Radotinib (drug)]] 5 µM |  | -4.0 | -4.9 |
|  | [[venetoclax (drug)]] 5 µM |  | -3.8 | -2.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.6 | -3.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.5 | -2.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.4 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | methionine sulfoxide reductase A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p23.1 — chr8:10,054,292-10,428,891 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Methionine sulfoxide reductases |
| Hallmark sets | REACTIVE_OXYGEN_SPECIES_PATHWAY |
| Reactome | 1 pathways, smallest: Protein repair |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UJ68](https://www.uniprot.org/uniprotkb/Q9UJ68) (Mitochondrial peptide methionine sulfoxide reductase):

> [Isoform 1]: Catalyzes the reversible oxidation-reduction of methionine sulfoxide in proteins to methionine. Has an important function as a repair enzyme for proteins that have been inactivated by oxidation. Plays a crucial role in repairing oxidized methionine residues in key lens proteins, such as alpha-crystallin (CRYAA/CRYAB) and cytochrome c (CYCS), thereby restoring their function and maintaining lens transparency (By similarity).

**Summary**, from NCBI Gene [4482](https://www.ncbi.nlm.nih.gov/gene/4482):

> This gene encodes a ubiquitous and highly conserved protein that carries out the enzymatic reduction of methionine sulfoxide to methionine. Human and animal studies have shown the highest levels of expression in kidney and nervous tissue. The protein functions in the repair of oxidatively damaged proteins to restore biological activity. Alternative splicing results in multiple transcript variants. [provided by RefSeq, May 2014]

**Accessions** — [HGNC:7377](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7377) · Entrez [4482](https://www.ncbi.nlm.nih.gov/gene/4482) · UniProt [Q9UJ68](https://www.uniprot.org/uniprotkb/Q9UJ68) · Ensembl [ENSG00000175806](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175806)

## Data

Gene col 10652: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10652); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10652, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10652]; `tensor/DDL_lfc|DDL_z.npy` [10652]; `embed/gene_vectors.npy` [10652]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10652 or target_col == 10652). Every well: [[MSRA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MSRA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
