---
symbol: "FRMD6"
type: "gene"
col: 6356
ensembl_id: "ENSG00000139926"
name: "FERM domain containing 6"
location: "14q22.1"
module: 116
arm: "+"
pooled_cpm: 133.91
n_lines_expressing: 37
n_dd_up: 13
n_dd_down: 29
n_dd_up_clean: 11
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 18
direction_downstream: 19
tags: ["gene", "module/116"]
generated_by: "tahoemap"
---

# FRMD6

*FERM domain containing 6* — 14q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.64× (z +18.0, q 0e+00, up in 29 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.566× (z -10.5, q 5e-23, down in 32 of 36 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ETS1]] (+0.74, fdr 7e-06), [[NAV3]] (+0.71, fdr 7e-06), [[IL31RA]] (+0.70, fdr 7e-06).
> It is in [[Module 116]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 18 arrows point to it, the strongest [[PDCD1LG2]] → it (grade B ⚠); 19 go from it, the strongest it → [[FRMD6-AS2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6356.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.64×** | +18.0 | 0e+00 | 29/35 (HOP62, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **5.98×** | +12.3 | 4e-32 | 29/36 (HOP62, Panc 03.27, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.50×** | +12.0 | 5e-31 | 32/35 (HOP62, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.76×** | +7.1 | 2e-10 | 23/35 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.36×** | +5.9 | 4e-07 | 29/35 (Panc 03.27, HOP62, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.52×** | +5.5 | 4e-06 | 26/35 (A-172, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.51×** | +5.5 | 4e-06 | 26/35 (A-172, SW 900, …) | all doses, stronger at high dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.50×** | +5.3 | 7e-06 | 26/35 (A498, SW 900, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.49×** | +4.9 | 6e-05 | 20/34 (A549, A-172, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.29×** | +4.8 | 1e-04 | 21/36 (SW 900, A498, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.43×** | +4.6 | 2e-04 | 25/34 (SW 900, A498, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.41×** | +4.5 | 3e-04 | 23/34 (SW 900, A498, …) | all doses, stronger at high dose |  |
| [[BAY1125976 (drug)]] 5 µM |  | **1.61×** | +3.3 | 0.044 | 20/35 (Hs 766T, AN3 CA, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6356.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.566×** | -10.5 | 5e-23 | 32/36 (RKO, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.438×** | -10.4 | 1e-22 | 25/32 (NCI-H1573, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.493×** | -9.2 | 5e-18 | 25/36 (RKO, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.612×** | -5.9 | 4e-07 | 25/33 (A-427, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.624×** | -5.9 | 4e-07 | 26/35 (LOX-IMVI, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.672×** | -5.1 | 3e-05 | 25/35 (LOX-IMVI, C32, …) | rises with dose |  |
| [[Triamcinolone (drug)]] 5 µM |  | **0.764×** | -4.9 | 6e-05 | 24/35 (A549, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.670×** | -4.9 | 6e-05 | 23/35 (C32, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~20% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.688×** | -4.7 | 2e-04 | 27/37 (LOX-IMVI, RKO, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **0.733×** | -4.0 | 0.003 | 24/35 (A549, HOP62, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.735×** | -4.0 | 0.004 | 20/35 (Panc 03.27, A549, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.739×** | -3.9 | 0.004 | 17/35 (LOX-IMVI, C32, …) | rises with dose |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.731×** | -3.9 | 0.004 | 23/36 (A549, HOP62, …) | all doses, stronger at high dose |  |
| [[venetoclax (drug)]] 5 µM |  | **0.565×** | -3.9 | 0.004 | 21/35 (RKO, C32, …) | top dose only | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.743×** | -3.8 | 0.005 | 20/36 (HOP62, C32, …) | rises with dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.576×** | -3.8 | 0.006 | 16/35 (RKO, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.757×** | -3.6 | 0.009 | 21/35 (A549, HOP62, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 0.05 µM |  | **0.769×** | -3.4 | 0.019 | 17/35 (A549, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Budesonide (drug)]] 0.05 µM |  | **0.771×** | -3.4 | 0.020 | 19/35 (A549, HOP62, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, +0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6356. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 572 | 1 | 12 (7 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +12.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.208× (z -18.9) |
| [[A549 (line)]] | wt | 251 | 5 | 7 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.56× (z +14.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.282× (z -14.7) |
| [[RKO (line)]] | wt | 1,272 | 0 | 12 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.157× (z -22.6) |
| [[C32 (line)]] | wt | 344 | 0 | 11 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.305× (z -15.0) |
| [[SW 900 (line)]] | alt | 76.9 | 11 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.92× (z +14.9) | — |
| [[J82 (line)]] | alt | 377 | 2 | 8 (7 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.04× (z +14.6) | [[Dinaciclib (drug)]] 5 µM 0.157× (z -16.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.329× (z -14.7) |
| [[AsPC-1 (line)]] | alt | 54.6 | 0 | 9 (1 ⚠) | — | [[Binimetinib (drug)]] 5 µM 0.154× (z -13.0) |
| [[A-172 (line)]] | wt | 136 | 6 | 1 | [[Homoharringtonine (drug)]] 5 µM 13.7× (z +33.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.376× (z -12.6) |
| [[A498 (line)]] | wt | 36.3 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 14.6× (z +31.3) | — |
| [[HOP62 (line)]] | alt | 120 | 4 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 15.0× (z +38.7) | [[Clobetasol propionate (drug)]] 0.05 µM 0.407× (z -9.1) |
| [[Panc 03.27 (line)]] | alt | 250 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.54× (z +22.2) | — |
| [[HS-578T (line)]] | alt | 131 | 4 | 1 | [[Homoharringtonine (drug)]] 5 µM 9.32× (z +25.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.354× (z -12.0) |
| [[hTERT-HPNE (line)]] | wt | 381 | 2 | 3 | [[Homoharringtonine (drug)]] 5 µM 4.71× (z +13.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.190× (z -14.9) |
| [[NCI-H1792 (line)]] | alt | 115 | 2 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +13.5) | [[Dinaciclib (drug)]] 5 µM 0.129× (z -15.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.437× (z -9.2) |
| [[BT-474 (line)]] | alt | 98.9 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.261× (z -10.1) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.293× (z -8.9) |
| [[CFPAC-1 (line)]] | alt | 150 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 5.27× (z +15.2) | [[Binimetinib (drug)]] 5 µM 0.282× (z -8.6) |
| [[NCI-H2030 (line)]] | alt | 181 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.30× (z +11.4) | [[Dinaciclib (drug)]] 0.05 µM 0.321× (z -10.1) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 84.2 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.81× (z +15.0) | [[Dinaciclib (drug)]] 5 µM 0.162× (z -13.8) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 113 | 1 | 3 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 7.61× (z +10.0) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.383× (z -8.8) |
| [[SK-MEL-2 (line)]] | alt | 147 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.63× (z +15.2) | — |
| [[SW1417 (line)]] | alt | 45.8 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.25× (z +20.2) | — |
| [[A-427 (line)]] | wt | 46.5 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +13.7) | [[Dinaciclib (drug)]] 0.05 µM 0.226× (z -11.8) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 273 | 1 | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 9.45× (z +9.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.313× (z -12.9) |
| [[SNU-423 (line)]] | alt | 134 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.5× (z +27.6) | — |
| [[AN3 CA (line)]] | alt | 235 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.197× (z -10.4) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.225× (z -9.2) |
| [[CHP-212 (line)]] | wt | 148 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.155× (z -10.1) ⚠ toxic; cell-cycle shift, explains ~40% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.340× (z -8.6) |
| [[H4 (line)]] | wt | 147 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.46× (z +20.9) | — |
| [[NCI-H2347 (line)]] | alt | 87.8 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 12.7× (z +10.6) | — |
| [[PANC-1 (line)]] | alt | 82.3 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 10.9× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.261× (z -9.5) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 137 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.9× (z +26.4) | — |
| [[NCI-H1573 (line)]] | alt | 91.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0823× (z -16.9) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 256 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0367× (z -14.0) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 161 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.09× (z +12.4) | — |
| [[C-33 A (line)]] | alt | 31.3 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 9.79 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 30.3 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 21.6 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 28.7 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 14.2 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 9.24 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 20.8 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 12.1 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 21.5 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 154 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 132 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 66.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 29.1 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 78.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.1 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 30.7 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6356), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ETS1]] | +0.74 | +0.73 / +0.73 | both halves | 7e-06 |  |
| [[NAV3]] | +0.71 | +0.72 / +0.69 | both halves | 7e-06 |  |
| [[IL31RA]] | +0.70 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[MARCHF4]] | +0.64 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[EGFR]] | +0.63 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[TOMM34]] | +0.63 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[LINC00973]] | +0.62 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[ADTRP]] | +0.61 | +0.60 / +0.58 | both halves | 8e-06 |  |
| [[AXL]] | +0.60 | +0.64 / +0.57 | both halves | 1e-05 |  |
| [[FRMD4A]] | +0.60 | +0.57 / +0.61 | both halves | 1e-05 | same gene group |
| [[AFF3]] | +0.60 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[SLC35F3]] | +0.60 | +0.64 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 13, C 5. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PDCD1LG2]] | B | PDCD1LG2 activity raises FRMD6's level | lines that do not express PDCD1LG2 (28) vs lines expressing it (22) | 3.81× lower at baseline in the lines without PDCD1LG2 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ADAMTS12, FN1, APCDD1L |
| [[FRMD4A]] | B | FRMD4A activity raises FRMD6's level | lines that do not express FRMD4A (24) vs lines expressing it (26) | 4.00× lower at baseline in the lines without FRMD4A | 0.003 | ⚠ within organs, on part of the lines; also absent: ENSG00000230615, PTGFR, TNFAIP6 |
| [[ADAMTS6]] | B | ADAMTS6 activity raises FRMD6's level | lines that do not express ADAMTS6 (25) vs lines expressing it (25) | 3.49× lower at baseline in the lines without ADAMTS6 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: FLI1, PDCD1LG2, TENM2 |
| [[BNC2]] | B | BNC2 activity raises FRMD6's level | lines that do not express BNC2 (21) vs lines expressing it (29) | 3.53× lower at baseline in the lines without BNC2 | 0.020 | ⚠ within organs, on part of the lines; also absent: LINC03041, DPY19L2, RNF182 |
| [[CD59]] | B | CD59 activity raises FRMD6's level | lines that do not express CD59 (7) vs lines expressing it (43) | 2.60× lower at baseline in the lines without CD59 | 0.033 | ⚠ within organs, on part of the lines; also absent: C11orf91, ENSG00000284969, MET; maybe low, not absent |
| [[BCL2A1]] | B | BCL2A1 activity raises FRMD6's level | lines that do not express BCL2A1 (26) vs lines expressing it (24) | 2.94× lower at baseline in the lines without BCL2A1 | 0.042 | ⚠ within organs, on part of the lines; also absent: BASP1-AS1, TMEM156, CSGALNACT1 |
| [[FJX1]] | B | FJX1 activity raises FRMD6's level | lines that do not express FJX1 (11) vs lines expressing it (39) | 3.74× lower at baseline in the lines without FJX1 | 0.049 | ⚠ within organs, on part of the lines; also absent: DYNC2H1, GIHCG, HDGFL3 |
| [[ROBO4]] | B | ROBO4 activity raises FRMD6's level | lines that do not express ROBO4 (28) vs lines expressing it (22) | 3.23× lower at baseline in the lines without ROBO4 | 0.060 | ⚠ within organs, on part of the lines; also absent: LNCOG, ENSG00000222032, PHACTR1 |
| [[CSF2]] | B | CSF2 activity strengthens FRMD6's drug response | lines that do not express CSF2 (14) vs lines expressing it (22) | the lines without CSF2 respond 0.87× as strongly (z diff +0.55); strongest at Harringtonine 5 µM: 1.19x vs 2.71x (z diff +5.1) | 0.063 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: IL6, CCBE1, G0S2; target measured in part of the lines; both ways; artifact flags |
| [[KIAA1549L]] | B | KIAA1549L activity raises FRMD6's level | lines that do not express KIAA1549L (20) vs lines expressing it (30) | 2.98× lower at baseline in the lines without KIAA1549L | 0.078 | ⚠ within organs, on part of the lines; also absent: NLRP3, PLPP4, PHACTR1 |
| [[LINC00973]] | B | LINC00973 activity strengthens FRMD6's drug response | lines that do not express LINC00973 (13) vs lines expressing it (23) | the lines without LINC00973 respond 0.74× as strongly (z diff +1.15); strongest at Homoharringtonine 5 µM: 1.35x vs 5.02x (z diff +6.0) | 0.081 | ⚠ within organs, on part of the lines; also absent: ENSG00000239462, IL11, BICC1; target measured in part of the lines; artifact flags |
| [[G0S2]] | B | G0S2 activity raises FRMD6's level | lines that do not express G0S2 (33) vs lines expressing it (17) | 2.58× lower at baseline in the lines without G0S2 | 0.089 | ⚠ within organs, on part of the lines; also absent: IL6, EDNRA, RRAD; its own permutation p |

### Downstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 15, C 4. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FRMD6-AS2]] | B | FRMD6 activity raises FRMD6-AS2's level | lines that do not express FRMD6 (13) vs lines expressing it (37) | 2.78× lower at baseline in the lines without FRMD6 | 4e-04 | ⚠ within organs, on part of the lines; also absent: CTSL, OSMR-DT, EVC; maybe low, not absent |
| [[RAI14]] | B | FRMD6 activity raises RAI14's level | lines that do not express FRMD6 (13) vs lines expressing it (37) | 3.78× lower at baseline in the lines without FRMD6 | 0.005 | ⚠ within organs, on part of the lines; also absent: CTSL, OSMR-DT, EVC; maybe low, not absent |
| [[ABL2]] | B | FRMD6 activity raises ABL2's level | lines that do not express FRMD6 (13) vs lines expressing it (37) | 2.54× lower at baseline in the lines without FRMD6 | 0.007 | ⚠ within organs, on part of the lines; also absent: CTSL, OSMR-DT, EVC; maybe low, not absent |
| [[CDK17]] | B | FRMD6 activity raises CDK17's level | lines that do not express FRMD6 (13) vs lines expressing it (37) | 1.55× lower at baseline in the lines without FRMD6 | 0.017 | ⚠ within organs, on part of the lines; also absent: CTSL, OSMR-DT, EVC; maybe low, not absent |
| [[G0S2]] | B | FRMD6 activity raises G0S2's level | lines that do not express FRMD6 (13) vs lines expressing it (37) | 3.75× lower at baseline in the lines without FRMD6 | 0.032 | ⚠ within organs, on part of the lines; also absent: CTSL, OSMR-DT, EVC; maybe low, not absent |
| [[SAMD4A]] | B | FRMD6 activity raises SAMD4A's level | lines that do not express FRMD6 (13) vs lines expressing it (37) | 1.95× lower at baseline in the lines without FRMD6 | 0.035 | ⚠ within organs, on part of the lines; also absent: CTSL, OSMR-DT, EVC; maybe low, not absent |
| [[BCL2A1]] | B | FRMD6 activity raises BCL2A1's level | lines that do not express FRMD6 (13) vs lines expressing it (37) | 3.40× lower at baseline in the lines without FRMD6 | 0.039 | ⚠ within organs, on part of the lines; also absent: CTSL, OSMR-DT, EVC; maybe low, not absent |
| [[CD59]] | B | FRMD6 activity raises CD59's level | lines that do not express FRMD6 (13) vs lines expressing it (37) | 2.36× lower at baseline in the lines without FRMD6 | 0.040 | ⚠ within organs, on part of the lines; also absent: CTSL, OSMR-DT, EVC; maybe low, not absent |
| [[KIAA1549L]] | B | FRMD6 activity raises KIAA1549L's level | lines that do not express FRMD6 (13) vs lines expressing it (37) | 3.47× lower at baseline in the lines without FRMD6 | 0.043 | ⚠ within organs, on part of the lines; also absent: CTSL, OSMR-DT, EVC; maybe low, not absent |
| [[CTTNBP2NL]] | B | FRMD6 activity raises CTTNBP2NL's level | lines that do not express FRMD6 (13) vs lines expressing it (37) | 1.35× lower at baseline in the lines without FRMD6 | 0.050 | ⚠ within organs, on part of the lines; also absent: CTSL, OSMR-DT, EVC; maybe low, not absent |
| [[STK10]] | B | FRMD6 activity raises STK10's level | lines that do not express FRMD6 (13) vs lines expressing it (37) | 2.11× lower at baseline in the lines without FRMD6 | 0.057 | ⚠ within organs, on part of the lines; also absent: CTSL, OSMR-DT, EVC; maybe low, not absent |
| [[PDCD1LG2]] | B | FRMD6 activity raises PDCD1LG2's level | lines that do not express FRMD6 (13) vs lines expressing it (37) | 2.81× lower at baseline in the lines without FRMD6 | 0.062 | ⚠ within organs, on part of the lines; also absent: CTSL, OSMR-DT, EVC; maybe low, not absent |

## Where it sits

- **Module**: [[Module 116]]; 42 genes; every member is in the + arm (projection on the module's main direction 0.754). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (43.8, 11.6); signed map (14.6, 43.9). **Vector** length 138, 45.5% of its response variance represented; |z| ≥ 3 in 1,446 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.9 | +12.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +8.3 | +18.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | +7.6 | +7.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | +6.7 | +12.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +6.6 | +5.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.5 | +5.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | +5.2 | +4.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.1 | +1.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.8 | +1.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.5 | +4.8 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -5.6 | -5.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -4.4 | -4.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.2 | -3.9 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -4.1 | -2.5 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -4.0 | -4.9 |
|  | [[Budesonide (drug)]] 5 µM |  | -3.7 | -2.2 |
|  | [[venetoclax (drug)]] 5 µM |  | -3.6 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | FERM domain containing 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q22.1 — chr14:51,489,100-51,730,727 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC17921, willin, EX1; previously C14orf31 |
| Gene groups (HGNC) | FERM domain containing |
| Matched by | ensembl_id |

UniProt [Q96NE9](https://www.uniprot.org/uniprotkb/Q96NE9) carries no function annotation.

**Summary**, from NCBI Gene [122786](https://www.ncbi.nlm.nih.gov/gene/122786):

> Predicted to enable protein sequestering activity. Predicted to be involved in positive regulation of hippo signaling. Predicted to act upstream of or within apical constriction; intracellular protein localization; and regulation of actin filament-based process. Located in cytoplasm and plasma membrane. Implicated in asthma. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:19839](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19839) · Entrez [122786](https://www.ncbi.nlm.nih.gov/gene/122786) · UniProt [Q96NE9](https://www.uniprot.org/uniprotkb/Q96NE9) · Ensembl [ENSG00000139926](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000139926)

## Data

Gene col 6356: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6356); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6356, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6356]; `tensor/DDL_lfc|DDL_z.npy` [6356]; `embed/gene_vectors.npy` [6356]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6356 or target_col == 6356). Every well: [[FRMD6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FRMD6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
