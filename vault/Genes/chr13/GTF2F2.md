---
symbol: "GTF2F2"
type: "gene"
col: 12006
ensembl_id: "ENSG00000188342"
name: "general transcription factor IIF subunit 2"
location: "13q14.12-q14.13"
module: 4
arm: "+"
pooled_cpm: 87.85
n_lines_expressing: 50
n_dd_up: 39
n_dd_down: 0
n_dd_up_clean: 22
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# GTF2F2

*general transcription factor IIF subunit 2* — 13q14.12-q14.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 39 drug-doses (17 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.66× (z +17.0, q 0e+00, up in 47 of 49 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (SNU-1 0.135×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DIS3L2]] (+0.65, fdr 7e-06), [[DPH6]] (+0.64, fdr 7e-06), [[CDIN1]] (+0.62, fdr 1e-05); moves opposite to [[FAM117A]] (-0.54, fdr 3e-05), [[TMEM39B]] (-0.54, fdr 4e-05), [[RSRP1]] (-0.50, fdr 5e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 56 in all, 23 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 39 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12006.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.66×** | +17.0 | 0e+00 | 47/49 (LS 180, SW480, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.96×** | +16.8 | 0e+00 | 44/48 (COLO 205, LoVo, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.93×** | +16.4 | 0e+00 | 45/48 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.56×** | +15.7 | 0e+00 | 34/48 (A-172, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.87×** | +15.7 | 0e+00 | 40/48 (A-172, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.84×** | +15.3 | 0e+00 | 46/48 (LoVo, HOP62, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.76×** | +14.2 | 5e-44 | 43/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.89×** | +13.9 | 3e-42 | 37/48 (LS 180, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.80×** | +12.3 | 1e-32 | 41/47 (COLO 205, LoVo, …) | top dose only | cell-cycle shift (explains ~19% here); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **1.59×** | +11.6 | 2e-29 | 38/48 (LoVo, LS 180, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.56×** | +11.1 | 8e-27 | 41/48 (COLO 205, LoVo, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.53×** | +10.7 | 6e-25 | 45/48 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.53×** | +10.6 | 1e-24 | 39/48 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.47×** | +9.7 | 1e-20 | 35/48 (SW480, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.44×** | +9.1 | 2e-18 | 36/48 (SW480, HOP62, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.44×** | +8.6 | 3e-16 | 37/48 (NCI-H460, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.49×** | +8.3 | 4e-15 | 36/48 (A-172, HOP62, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.31×** | +6.8 | 3e-10 | 30/48 (A-172, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.18× | +5.9 | 7e-08 | 21/49 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose |  |
| [[venetoclax (drug)]] 5 µM |  | **1.46×** | +5.0 | 1e-05 | 25/48 (Hs 766T, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.22×** | +5.0 | 1e-05 | 24/48 (A-172, C32, …) | all doses, stronger at high dose |  |
| [[EX229 (drug)]] 5 µM |  | **1.46×** | +5.0 | 1e-05 | 31/48 (NCI-H1573, NCI-H460, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12006.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (SNU-1 0.135×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.838× | -4.5 | 0.004 | 20/47 (SK-MEL-2, LoVo, …) | inconsistent across doses | low cells (technical?) |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 0.846× | -4.2 | 0.006 | 16/48 (HT-29, AsPC-1, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | 0.907× | -3.5 | 0.075 | 2/48 (NCI-H1792, CFPAC-1) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.874× | -3.4 | 0.085 | 13/48 (CFPAC-1, LOX-IMVI, …) | all doses, flat |  |
| [[Bicalutamide (drug)]] 0.05 µM |  | 0.881× | -3.2 | 0.13 | 8/48 (AsPC-1, NCI-H2030, …) | inconsistent across doses |  |
| [[Bestatin (hydrochloride) (drug)]] 0.5 µM |  | 0.887× | -3.1 | 0.18 | 7/48 (RPMI-7951, Panc 03.27, …) | inconsistent across doses |  |
| [[Entrectinib (drug)]] 5 µM |  | 0.888× | -3.0 | 0.18 | 10/48 (SW 1271, hTERT-HPNE, …) | rises with dose |  |
| [[Filgotinib (drug)]] 0.05 µM |  | 0.889× | -3.0 | 0.18 | 10/48 (HT-29, AsPC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.34 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12006. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 53.0 | 10 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.73× (z +21.0) | — |
| [[COLO 205 (line)]] | alt | 151 | 9 (4 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 4.09× (z +12.9) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.18× (z +12.8) | — |
| [[SW480 (line)]] | alt | 126 | 9 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.39× (z +14.9) | — |
| [[LoVo (line)]] | wt | 93.5 | 8 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.33× (z +13.5) | — |
| [[NCI-H460 (line)]] | wt | 73.9 | 8 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.03× (z +15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.99× (z +10.1) | — |
| [[A-172 (line)]] | wt | 47.1 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.11× (z +26.1) | — |
| [[LS 180 (line)]] | wt | 133 | 7 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.82× (z +14.6) | — |
| [[NCI-H1573 (line)]] | alt | 46.7 | 7 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.94× (z +11.6) | — |
| [[HT-29 (line)]] | alt | 104 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +14.4) | — |
| [[Panc 03.27 (line)]] | alt | 132 | 6 (2 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 4.45× (z +11.0) | — |
| [[SNU-423 (line)]] | alt | 85.5 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.03× (z +20.2) | — |
| [[KATO III (line)]] | alt | 104 | 5 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.26× (z +10.6) | — |
| [[Hs 766T (line)]] | wt | 81.4 | 4 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.91× (z +9.8) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.55× (z +8.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 74.7 | 4 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.47× (z +13.4) | — |
| [[PANC-1 (line)]] | alt | 90.4 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 1.87× (z +10.1) | — |
| [[A498 (line)]] | wt | 141 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 6.44× (z +11.0) | — |
| [[AsPC-1 (line)]] | alt | 102 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +13.0) | — |
| [[CFPAC-1 (line)]] | alt | 58.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.84× (z +21.6) | — |
| [[H4 (line)]] | wt | 68.4 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +9.8) | — |
| [[J82 (line)]] | alt | 97.1 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.69× (z +9.9) | — |
| [[SW 900 (line)]] | alt | 80.1 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +12.7) | — |
| [[A549 (line)]] | wt | 65.1 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +10.8) | — |
| [[C32 (line)]] | wt | 72.7 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 8.83× (z +10.8) | — |
| [[HCT15 (line)]] | alt | 75.3 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.98× (z +9.4) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[HEC-1-A (line)]] | alt | 89.9 | 2 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.08× (z +8.9) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 3.90× (z +8.6) | — |
| [[HS-578T (line)]] | alt | 56.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.10× (z +20.1) | — |
| [[LOX-IMVI (line)]] | wt | 121 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.14× (z +19.3) | — |
| [[NCI-H1792 (line)]] | alt | 43.4 | 2 (2 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.61× (z +9.4) ⚠ toxic | — |
| [[NCI-H2347 (line)]] | alt | 71.2 | 2 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.51× (z +10.8) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.81× (z +9.7) | — |
| [[SW1417 (line)]] | alt | 114 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.50× (z +11.3) | — |
| [[BT-474 (line)]] | alt | 69.5 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.68× (z +9.6) | — |
| [[hTERT-HPNE (line)]] | wt | 49.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +11.3) | — |
| [[RKO (line)]] | wt | 110 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 4.34× (z +9.0) | — |
| [[SNU-1 (line)]] | wt | 111 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.135× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW48 (line)]] | wt | 108 | 1 | 0 | [[TAK-901 (drug)]] 0.05 µM 3.12× (z +10.1) | — |
| [[A-427 (line)]] | wt | 76.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 119 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 60.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 102 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 72.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 93.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 71.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 90.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 64.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 57.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 58.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 82.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 127 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12006), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DIS3L2]] | +0.65 | +0.58 / +0.68 | both halves | 7e-06 |  |
| [[DPH6]] | +0.64 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[CDIN1]] | +0.62 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[MRPL3]] | +0.61 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[NAA25]] | +0.61 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[WDR43]] | +0.61 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[CHCHD6]] | +0.60 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[TMEM33]] | +0.60 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[AGPS]] | +0.59 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[NME1]] | +0.59 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[NOL10]] | +0.59 | +0.46 / +0.62 | both halves | 2e-05 |  |
| [[VWA8]] | +0.58 | +0.58 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM117A]] | -0.54 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[TMEM39B]] | -0.54 | -0.42 / -0.55 | both halves | 4e-05 |  |
| [[RSRP1]] | -0.50 | -0.40 / -0.52 | both halves | 5e-05 |  |
| [[CEP57]] | -0.50 | -0.39 / -0.52 | both halves | 5e-05 |  |
| [[PARP16]] | -0.50 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[ING1]] | -0.50 | -0.42 / -0.62 | both halves | 4e-05 |  |
| [[CDK19]] | -0.49 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[ZNF160]] | -0.48 | -0.39 / -0.53 | both halves | 5e-05 |  |
| [[GCAT]] | -0.48 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[IKZF4]] | -0.48 | -0.40 / -0.48 | both halves | 5e-05 |  |
| [[HMGCL]] | -0.48 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[INTS6L]] | -0.48 | -0.52 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.614). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-10.3, -34.9); signed map (-8.9, -49.1). **Vector** length 77.2, 21.5% of its response variance represented; |z| ≥ 3 in 1,436 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belumosudil (drug)]] 5 µM |  | +4.3 | +3.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.9 | +10.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | +2.7 | +17.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +2.7 | +4.6 |
|  | [[EX229 (drug)]] 5 µM |  | +2.6 | +5.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.3 | +5.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.2 | +13.9 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.2 | +4.5 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -6.4 | +0.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.6 | +15.7 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | -3.1 | +0.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.0 | +4.6 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | -2.6 | -3.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.2 | -1.0 |
|  | [[Entrectinib (drug)]] 5 µM |  | -2.0 | -3.0 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.9 | -2.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.8 | -4.5 |

## What is on record

|  |  |
|---|---|
| Name | general transcription factor IIF subunit 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q14.12-q14.13 — chr13:45,120,510-45,284,893 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TFIIF, BTF4, RAP30 |
| Gene groups (HGNC) | General transcription factor IIF complex subunits |
| Reactome | 59 pathways, smallest: Signaling by FGFR2 IIIa TM; Abortive elongation of HIV-1 transcript in the absence of Tat; FGFR2 mutant receptor activation |
| Matched by | ensembl_id |

**Function**, from UniProt [P13984](https://www.uniprot.org/uniprotkb/P13984) (General transcription factor IIF subunit 2):

> TFIIF is a general transcription initiation factor that binds to RNA polymerase II and helps to recruit it to the initiation complex in collaboration with TFIIB.

**Summary**, from NCBI Gene [2963](https://www.ncbi.nlm.nih.gov/gene/2963):

> Predicted to enable RNA polymerase II general transcription initiation factor activity. Involved in positive regulation of transcription by RNA polymerase II; transcription elongation by RNA polymerase II; and transcription initiation at RNA polymerase II promoter. Located in microtubule cytoskeleton and nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:4653](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4653) · Entrez [2963](https://www.ncbi.nlm.nih.gov/gene/2963) · UniProt [P13984](https://www.uniprot.org/uniprotkb/P13984) · Ensembl [ENSG00000188342](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000188342)

## Data

Gene col 12006: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12006); `tables/drug_effects.parquet` (64 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12006, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12006]; `tensor/DDL_lfc|DDL_z.npy` [12006]; `embed/gene_vectors.npy` [12006]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12006 or target_col == 12006). Every well: [[GTF2F2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GTF2F2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
