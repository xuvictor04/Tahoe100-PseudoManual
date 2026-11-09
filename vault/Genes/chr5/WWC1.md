---
symbol: "WWC1"
type: "gene"
col: 3487
ensembl_id: "ENSG00000113645"
name: "WW and C2 domain containing 1"
location: "5q34"
module: 123
arm: "+"
pooled_cpm: 180.55
n_lines_expressing: 37
n_dd_up: 19
n_dd_down: 18
n_dd_up_clean: 15
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 8
direction_downstream: 7
tags: ["gene", "module/123"]
generated_by: "tahoemap"
---

# WWC1

*WW and C2 domain containing 1* — 5q34

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.05× (z +26.9, q 0e+00, up in 26 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.525× (z -24.1, q 0e+00, down in 32 of 36 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COBL]] (+0.60, fdr 1e-05), [[TSPAN2]] (+0.58, fdr 1e-05), [[EDN1]] (+0.58, fdr 1e-05); moves opposite to [[KRBOX4]] (-0.53, fdr 2e-05), [[GLE1]] (-0.51, fdr 2e-05), [[ZFPL1]] (-0.50, fdr 3e-05).
> It is in [[Module 123]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[EDN1]] → it (grade B ⚠); 7 go from it, the strongest it → [[USP43]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3487.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.05×** | +26.9 | 0e+00 | 26/35 (NCI-H2347, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **3.53×** | +17.4 | 0e+00 | 29/36 (A-427, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.64×** | +12.5 | 8e-34 | 24/35 (COLO 205, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~18% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.55×** | +11.7 | 3e-29 | 25/35 (COLO 205, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.36×** | +11.5 | 1e-28 | 23/35 (NCI-H2347, A-172, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.49×** | +10.5 | 5e-24 | 24/35 (PANC-1, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.46×** | +9.9 | 3e-21 | 23/35 (COLO 205, BT-474, …) | two highest doses | cell-cycle shift (explains ~15% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.44×** | +9.6 | 9e-20 | 24/36 (NCI-H2347, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.91×** | +8.9 | 2e-17 | 22/35 (A-427, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.75×** | +7.8 | 4e-13 | 18/36 (A-427, PANC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.31×** | +7.1 | 5e-11 | 16/35 (COLO 205, NCI-H460, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.26×** | +6.2 | 2e-08 | 19/35 (COLO 205, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.26×** | +6.2 | 3e-08 | 18/35 (A-427, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **1.25×** | +5.9 | 1e-07 | 16/35 (COLO 205, NCI-H1573, …) | two highest doses |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.23×** | +5.3 | 4e-06 | 17/35 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.13× | +4.7 | 9e-05 | 13/36 (NCI-H1573, PANC-1, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.11× | +3.8 | 0.005 | 11/35 (CFPAC-1, COLO 205, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 1.14× | +3.4 | 0.019 | 12/35 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3487.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.525×** | -24.1 | 0e+00 | 32/36 (SW1417, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.624×** | -12.0 | 1e-30 | 26/35 (LOX-IMVI, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.777×** | -9.4 | 8e-19 | 23/35 (J82, LOX-IMVI, …) | rises with dose | low cells (technical?) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.704×** | -8.9 | 6e-17 | 22/31 (HEC-1-A, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.740×** | -7.9 | 2e-13 | 23/36 (HEC-1-A, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.737×** | -7.8 | 8e-13 | 24/37 (KATO III, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.748×** | -7.7 | 2e-12 | 22/36 (LOX-IMVI, RKO, …) | top dose only |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.587×** | -7.4 | 1e-11 | 25/36 (A498, SW1417, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.751×** | -7.3 | 2e-11 | 23/35 (NCI-H460, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.761×** | -7.2 | 3e-11 | 20/35 (SK-MEL-2, HT-29, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.769×** | -7.0 | 2e-10 | 21/35 (KATO III, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.769×** | -6.9 | 2e-10 | 22/35 (KATO III, J82, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.771×** | -6.9 | 3e-10 | 20/35 (LoVo, SK-MEL-2, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **0.792×** | -6.2 | 3e-08 | 18/35 (LOX-IMVI, A498, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.722×** | -6.2 | 3e-08 | 18/35 (A498, SW48, …) | rises with dose | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Entrectinib (drug)]] 5 µM |  | **0.830×** | -4.9 | 3e-05 | 17/35 (J82, KATO III, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.847× | -4.4 | 3e-04 | 16/35 (LoVo, A498, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 0.05 µM |  | 0.843× | -4.2 | 9e-04 | 12/35 (SNU-1, SW1417, …) | all doses, stronger at high dose |  |
| [[Adagrasib (drug)]] 5 µM |  | 0.849× | -4.2 | 9e-04 | 11/35 (J82, LOX-IMVI, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3487. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 224 | 0 | 16 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.285× (z -18.7) |
| [[NCI-H2347 (line)]] | alt | 200 | 10 (3 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 4.78× (z +28.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.436× (z -15.1) |
| [[KATO III (line)]] | alt | 477 | 0 | 10 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.231× (z -20.3) |
| [[LoVo (line)]] | wt | 452 | 1 | 9 (6 ⚠) | [[TAK-901 (drug)]] 5 µM 4.13× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.281× (z -15.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.298× (z -15.0) |
| [[SW1417 (line)]] | alt | 508 | 3 | 7 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +16.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.250× (z -27.6) |
| [[A498 (line)]] | wt | 224 | 2 | 7 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +17.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.423× (z -15.3) |
| [[COLO 205 (line)]] | alt | 115 | 9 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.45× (z +21.8) | — |
| [[HEC-1-A (line)]] | alt | 599 | 6 (2 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +24.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.290× (z -24.2) |
| [[HepG2_C3A (line)]] | wt | 208 | 2 | 7 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +11.5) | [[Panobinostat (drug)]] 5 µM 0.380× (z -10.7) |
| [[NCI-H1573 (line)]] | alt | 87.8 | 9 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +13.3) | — |
| [[PANC-1 (line)]] | alt | 69.8 | 8 (2 ⚠) | 1 | [[Panobinostat (drug)]] 0.05 µM 2.70× (z +12.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.494× (z -12.8) |
| [[RKO (line)]] | wt | 132 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.211× (z -19.7) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.340× (z -13.1) |
| [[A-427 (line)]] | wt | 136 | 7 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.91× (z +25.8) | [[Dinaciclib (drug)]] 0.5 µM 0.354× (z -13.8) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 277 | 8 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.79× (z +18.4) | — |
| [[SK-MEL-2 (line)]] | alt | 163 | 0 | 8 (4 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.211× (z -16.5) |
| [[J82 (line)]] | alt | 188 | 0 | 7 (5 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.295× (z -22.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.416× (z -16.3) |
| [[A-172 (line)]] | wt | 45.9 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.2× (z +20.9) | — |
| [[HT-29 (line)]] | alt | 356 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.262× (z -13.8) |
| [[SW480 (line)]] | alt | 142 | 2 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +15.5) | [[Panobinostat (drug)]] 5 µM 0.326× (z -14.8) |
| [[SNU-423 (line)]] | alt | 121 | 3 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 5.68× (z +22.2) | [[Auranofin (drug)]] 5 µM 0.353× (z -9.4) |
| [[NCI-H460 (line)]] | wt | 99.7 | 2 (1 ⚠) | 1 | [[Niclosamide (olamine) (drug)]] 5 µM 2.93× (z +9.7) ⚠ toxic; cell-cycle shift, explains ~29% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 6.46× (z +9.1) | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.374× (z -8.9) |
| [[Panc 03.27 (line)]] | alt | 491 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +12.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.433× (z -10.6) |
| [[AsPC-1 (line)]] | alt | 280 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.267× (z -15.7) |
| [[HCT15 (line)]] | alt | 321 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.395× (z -13.2) |
| [[HOP62 (line)]] | alt | 49.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.55× (z +18.5) | — |
| [[NCI-H2030 (line)]] | alt | 111 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.305× (z -18.4) |
| [[NCI-H23 (line)]] | alt | 118 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.354× (z -14.5) |
| [[SW48 (line)]] | wt | 267 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.262× (z -20.0) |
| [[A549 (line)]] | wt | 292 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.288× (z -14.3) |
| [[CFPAC-1 (line)]] | alt | 227 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +13.1) | — |
| [[LS 180 (line)]] | wt | 197 | 0 | 1 | — | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.392× (z -8.7) |
| [[SNU-1 (line)]] | wt | 62.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +10.3) | — |
| [[AN3 CA (line)]] | alt | 35.1 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 60.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 17.6 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 25.7 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 29.5 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 19.6 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 20.5 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 45.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 32.6 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 43.8 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 148 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 150 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 40.1 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 15.2 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 27.3 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 34.1 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 34.6 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3487), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COBL]] | +0.60 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[TSPAN2]] | +0.58 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[EDN1]] | +0.58 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[ANKRD1]] | +0.57 | +0.38 / +0.53 | both halves | 6e-05 |  |
| [[AMOTL2]] | +0.56 | +0.52 / +0.58 | both halves | 1e-05 | pathway: Signaling by Hippo; STRING 459 |
| [[LATS2]] | +0.56 | +0.53 / +0.61 | both halves | 1e-05 | pathway: Signaling by Hippo; STRING 970 |
| [[PLCB4]] | +0.55 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[IL18]] | +0.55 | +0.42 / +0.56 | both halves | 4e-05 |  |
| [[CCN1]] | +0.55 | +0.45 / +0.52 | both halves | 3e-05 |  |
| [[DDAH1]] | +0.54 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[TEAD4]] | +0.54 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[LINC02832]] | +0.54 | +0.42 / +0.57 | both halves | 4e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KRBOX4]] | -0.53 | -0.48 / -0.54 | both halves | 2e-05 |  |
| [[GLE1]] | -0.51 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[ZFPL1]] | -0.50 | -0.50 / -0.46 | both halves | 3e-05 |  |
| [[VIPAS39]] | -0.50 | -0.42 / -0.53 | both halves | 4e-05 |  |
| [[CLDND1]] | -0.49 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[LINC02680]] | -0.47 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[HDAC6]] | -0.47 | -0.46 / -0.48 | both halves | 3e-05 | same gene group; pathway: Signaling by NOTCH |
| [[TNXB]] | -0.45 | -0.43 / -0.43 | both halves | 3e-05 |  |
| [[TUBGCP2]] | -0.45 | -0.39 / -0.49 | both halves | 5e-05 |  |
| [[TULP3]] | -0.45 | -0.46 / -0.53 | both halves | 3e-05 |  |
| [[C14orf28]] | -0.45 | -0.36 / -0.46 | both halves | 1e-04 |  |
| [[ADAM20]] | -0.45 | -0.45 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EDN1]] | B | EDN1 activity raises WWC1's level | lines that do not express EDN1 (27) vs lines expressing it (23) | 3.36× lower at baseline in the lines without EDN1 | 0.001 | ⚠ within organs, on part of the lines; also absent: P2RY2, S100A14, CBLC |
| [[COBL]] | B | COBL activity raises WWC1's level | lines that do not express COBL (23) vs lines expressing it (27) | 3.41× lower at baseline in the lines without COBL | 0.008 | ⚠ within organs, on part of the lines; also absent: MARVELD3, CRB3, GRB7 |
| [[USP43]] | B | USP43 activity raises WWC1's level | lines that do not express USP43 (10) vs lines expressing it (40) | 3.85× lower at baseline in the lines without USP43 | 0.014 | ⚠ within organs, on part of the lines; also absent: LLGL2, KRTAP5-AS1, BTG3-AS1 |
| [[TRIM15]] | B | TRIM15 activity raises WWC1's level | lines that do not express TRIM15 (34) vs lines expressing it (16) | 3.36× lower at baseline in the lines without TRIM15 | 0.018 | ⚠ within organs, on part of the lines; also absent: TMEM45B, EPS8L3, ENSG00000225680 |
| [[IL18]] | B | IL18 activity raises WWC1's level | lines that do not express IL18 (18) vs lines expressing it (32) | 3.12× lower at baseline in the lines without IL18 | 0.023 | ⚠ within organs, on part of the lines; also absent: LSR, SPINT2, LAMA3 |
| [[C6orf132]] | B | C6orf132 activity raises WWC1's level | lines that do not express C6orf132 (27) vs lines expressing it (23) | 3.76× lower at baseline in the lines without C6orf132 | 0.024 | ⚠ within organs, on part of the lines; also absent: PCSK9, RNF223, CDH1 |
| [[SLC52A3]] | B | SLC52A3 activity raises WWC1's level | lines that do not express SLC52A3 (26) vs lines expressing it (24) | 2.86× lower at baseline in the lines without SLC52A3 | 0.044 | ⚠ within organs, on part of the lines; also absent: SPINT2, ENSG00000267748, CLDN7 |
| [[KRT80]] | B | KRT80 activity raises WWC1's level | lines that do not express KRT80 (22) vs lines expressing it (28) | 2.85× lower at baseline in the lines without KRT80 | 0.064 | ⚠ within organs, on part of the lines; also absent: C19orf33, EPS8L2, SPNS2 |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[USP43]] | B | WWC1 activity raises USP43's level | lines that do not express WWC1 (13) vs lines expressing it (37) | 3.99× lower at baseline in the lines without WWC1 | 0.002 | ⚠ within organs, on part of the lines; also absent: SH2D3A, CHMP4C, LSR; maybe low, not absent |
| [[AMOTL2]] | B | WWC1 activity raises AMOTL2's level | lines that do not express WWC1 (13) vs lines expressing it (37) | 2.50× lower at baseline in the lines without WWC1 | 0.004 | ⚠ within organs, on part of the lines; also absent: SH2D3A, CHMP4C, LSR; maybe low, not absent |
| [[EDN1]] | B | WWC1 activity raises EDN1's level | lines that do not express WWC1 (13) vs lines expressing it (37) | 3.89× lower at baseline in the lines without WWC1 | 0.045 | ⚠ within organs, on part of the lines; also absent: SH2D3A, CHMP4C, LSR; maybe low, not absent |
| [[COBL]] | B | WWC1 activity raises COBL's level | lines that do not express WWC1 (13) vs lines expressing it (37) | 3.80× lower at baseline in the lines without WWC1 | 0.048 | ⚠ within organs, on part of the lines; also absent: SH2D3A, CHMP4C, LSR; maybe low, not absent |
| [[CRIM1]] | B | WWC1 activity raises CRIM1's level | lines that do not express WWC1 (13) vs lines expressing it (37) | 1.59× lower at baseline in the lines without WWC1 | 0.074 | ⚠ within organs, on part of the lines; also absent: SH2D3A, CHMP4C, LSR; maybe low, not absent |
| [[KRT80]] | B | WWC1 activity raises KRT80's level | lines that do not express WWC1 (13) vs lines expressing it (37) | 3.27× lower at baseline in the lines without WWC1 | 0.079 | ⚠ within organs, on part of the lines; also absent: SH2D3A, CHMP4C, LSR; maybe low, not absent |
| [[TET3]] | B | WWC1 activity raises TET3's level | lines that do not express WWC1 (13) vs lines expressing it (37) | 1.39× lower at baseline in the lines without WWC1 | 0.091 | ⚠ within organs, on part of the lines; also absent: SH2D3A, CHMP4C, LSR; maybe low, not absent |

## Where it sits

- **Module**: [[Module 123]] — TNF-alpha signaling via NF-kB; 40 genes; every member is in the + arm (projection on the module's main direction 0.484). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (22.7, 12.0); signed map (49.3, 15.8). **Vector** length 138, 42.3% of its response variance represented; |z| ≥ 3 in 1,434 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +9.0 | +11.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +6.9 | +10.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.6 | +9.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | +6.1 | +17.4 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +5.6 | +6.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.8 | +7.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.0 | +8.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.0 | +5.3 |
|  | [[vincristine (drug)]] 5 µM |  | +2.7 | +3.1 |
| fall | [[GSK1059615 (drug)]] 5 µM |  | -6.3 | -7.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.9 | -4.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.6 | -24.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | -4.4 | -6.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -4.2 | -9.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.1 | -7.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -3.5 | -7.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.5 | -4.4 |

## What is on record

|  |  |
|---|---|
| Name | WW and C2 domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q34 — chr5:168,291,645-168,472,303 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIBRA, KIAA0869, PPP1R168 |
| Gene groups (HGNC) | WWC family; Protein phosphatase 1 regulatory subunits; C2 and WW domain containing |
| Hallmark sets | ESTROGEN_RESPONSE_EARLY |
| Reactome | 4 pathways, smallest: NOTCH3 Intracellular Domain Regulates Transcription; Signaling by Hippo; Signaling by NOTCH3 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IX03](https://www.uniprot.org/uniprotkb/Q8IX03) (Protein KIBRA):

> Regulator of the Hippo signaling pathway, also known as the Salvador-Warts-Hippo (SWH) pathway. Enhances phosphorylation of LATS1 and YAP1 and negatively regulates cell proliferation and organ growth due to a suppression of the transcriptional activity of YAP1, the major effector of the Hippo pathway. Along with NF2 can synergistically induce the phosphorylation of LATS1 and LATS2 and function in the regulation of Hippo signaling pathway. Acts as a transcriptional coactivator of ESR1 which …

**Summary**, from NCBI Gene [23286](https://www.ncbi.nlm.nih.gov/gene/23286):

> The protein encoded by this gene is a cytoplasmic phosphoprotein that interacts with PRKC-zeta and dynein light chain-1. Alleles of this gene have been found that enhance memory in some individuals. Three transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Mar 2010]

**Accessions** — [HGNC:29435](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29435) · Entrez [23286](https://www.ncbi.nlm.nih.gov/gene/23286) · UniProt [Q8IX03](https://www.uniprot.org/uniprotkb/Q8IX03) · Ensembl [ENSG00000113645](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000113645)

## Data

Gene col 3487: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3487); `tables/drug_effects.parquet` (72 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3487, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3487]; `tensor/DDL_lfc|DDL_z.npy` [3487]; `embed/gene_vectors.npy` [3487]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3487 or target_col == 3487). Every well: [[WWC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WWC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
