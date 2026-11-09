---
symbol: "TLE4"
type: "gene"
col: 2810
ensembl_id: "ENSG00000106829"
name: "TLE family member 4, transcriptional corepressor"
location: "9q21.31"
module: 93
arm: "+"
pooled_cpm: 115.39
n_lines_expressing: 40
n_dd_up: 21
n_dd_down: 10
n_dd_up_clean: 15
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 6
direction_downstream: 14
tags: ["gene", "module/093"]
generated_by: "tahoemap"
---

# TLE4

*TLE family member 4, transcriptional corepressor* — 9q21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.74× (z +22.2, q 0e+00, up in 36 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.545× (z -9.2, q 3e-17, down in 24 of 34 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Pralsetinib (drug)]] 5 µM: 0.569× (z -4.6, q 5e-04, down in 26 of 39 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PIK3R3]] (+0.64, fdr 7e-06), [[FAM222A]] (+0.62, fdr 7e-06), [[C21orf91]] (+0.62, fdr 1e-05); moves opposite to [[PSMF1]] (-0.59, fdr 1e-05), [[RFT1]] (-0.59, fdr 1e-05), [[ZDHHC6]] (-0.55, fdr 1e-05).
> It is in [[Module 093]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[C21orf91]] → it (grade B ⚠); 14 go from it, the strongest it → [[PMAIP1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 6 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2810.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.74×** | +22.2 | 0e+00 | 36/38 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.95×** | +10.0 | 5e-21 | 31/38 (A498, HS-578T, …) | top dose only | cell-cycle shift (explains ~9% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.03×** | +9.5 | 4e-19 | 30/38 (SW1417, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.97×** | +9.3 | 2e-18 | 27/38 (SW1417, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.48×** | +8.6 | 7e-16 | 24/39 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.42×** | +7.7 | 1e-12 | 25/38 (SW1417, HEC-1-A, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.57×** | +6.7 | 2e-09 | 26/37 (HOP62, A498, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.63×** | +6.6 | 4e-09 | 24/38 (LoVo, SW1417, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.58×** | +6.1 | 6e-08 | 25/38 (LoVo, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.31×** | +6.0 | 1e-07 | 26/38 (A-172, A498, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.43×** | +5.6 | 1e-06 | 27/38 (LoVo, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.39×** | +5.1 | 1e-05 | 22/39 (SW1417, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.33×** | +4.4 | 4e-04 | 22/38 (NCI-H460, RKO, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.34×** | +4.3 | 6e-04 | 23/40 (NCI-H460, LoVo, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.33×** | +4.2 | 9e-04 | 20/38 (NCI-H460, SK-MEL-2, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.31×** | +4.2 | 0.001 | 22/38 (NCI-H460, RKO, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.30×** | +4.0 | 0.002 | 18/38 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.31×** | +3.9 | 0.003 | 17/38 (A-172, SW48, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.32×** | +3.8 | 0.005 | 16/38 (LoVo, A-427, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.46×** | +3.1 | 0.054 | 13/38 (KATO III, RKO, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2810.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.545×** | -9.2 | 3e-17 | 24/34 (CHP-212, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.603×** | -7.9 | 6e-13 | 27/39 (LOX-IMVI, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.688×** | -5.4 | 1e-05 | 22/35 (Panc 03.27, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Pralsetinib (drug)]] 5 µM |  | **0.569×** | -4.6 | 5e-04 | 26/39 (LOX-IMVI, J82, …) | top dose only | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.760×** | -4.3 | 0.002 | 22/38 (HT-29, KATO III, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Radotinib (drug)]] 5 µM |  | 0.851× | -3.6 | 0.026 | 18/38 (C32, SNU-423, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.785×** | -3.6 | 0.026 | 18/38 (C32, A549, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.774×** | -3.5 | 0.033 | 18/38 (SNU-423, SK-MEL-2, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.656×** | -3.5 | 0.033 | 15/38 (NCI-H2030, A549, …) | rises with dose | noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **0.779×** | -3.4 | 0.038 | 14/38 (NCI-H1573, HepG2/C3A, …) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 5 µM |  | **0.793×** | -3.2 | 0.080 | 13/38 (SW 1088, NCI-H1573, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2810. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 65.5 | 9 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.63× (z +23.3) | — |
| [[A498 (line)]] | wt | 331 | 6 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.01× (z +29.8) | [[Dinaciclib (drug)]] 5 µM 0.225× (z -18.8) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 344 | 7 (1 ⚠) | 0 | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 2.01× (z +11.6) | — |
| [[LoVo (line)]] | wt | 73.0 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +15.6) | — |
| [[SW1417 (line)]] | alt | 50.8 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.75× (z +15.1) | — |
| [[hTERT-HPNE (line)]] | wt | 209 | 4 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.20× (z +17.7) | [[Dinaciclib (drug)]] 5 µM 0.266× (z -11.1) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 992 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0671× (z -24.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.304× (z -15.6) |
| [[HOP62 (line)]] | alt | 42.2 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.04× (z +18.8) | — |
| [[Hs 766T (line)]] | wt | 69.4 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.48× (z +17.0) | — |
| [[Panc 03.27 (line)]] | alt | 144 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +10.5) | [[Dinaciclib (drug)]] 0.05 µM 0.230× (z -12.5) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 46.6 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.89× (z +10.6) | — |
| [[LOX-IMVI (line)]] | wt | 536 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.136× (z -21.2) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 141 | 0 | 3 (2 ⚠) | — | [[Vinblastine (sulfate) (drug)]] 5 µM 0.495× (z -9.3) |
| [[NCI-H2347 (line)]] | alt | 43.1 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +10.1) | [[Dinaciclib (drug)]] 0.05 µM 0.277× (z -10.2) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 42.6 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.17× (z +8.5) | [[Dinaciclib (drug)]] 0.05 µM 0.247× (z -11.0) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 248 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +11.7) | [[Dinaciclib (drug)]] 5 µM 0.321× (z -8.6) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 56.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.00× (z +16.6) | — |
| [[HepG2_C3A (line)]] | wt | 288 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.285× (z -12.5) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 147 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.70× (z +17.8) | — |
| [[J82 (line)]] | alt | 391 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +15.8) | — |
| [[NCI-H2030 (line)]] | alt | 68.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.252× (z -12.7) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 64.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +12.4) | — |
| [[SNU-423 (line)]] | alt | 219 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +14.1) | [[Dinaciclib (drug)]] 0.05 µM 0.355× (z -9.8) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 45.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +11.6) | — |
| [[A549 (line)]] | wt | 149 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +12.7) | — |
| [[COLO 205 (line)]] | alt | 114 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.39× (z +12.1) | — |
| [[H4 (line)]] | wt | 151 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.95× (z +15.1) | — |
| [[HEC-1-A (line)]] | alt | 41.0 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.62× (z +11.6) | — |
| [[KATO III (line)]] | alt | 117 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +14.1) | — |
| [[LS 180 (line)]] | wt | 54.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.73× (z +16.0) | — |
| [[RPMI-7951 (line)]] | alt | 147 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +11.3) | — |
| [[SHP-77 (line)]] | alt | 32.0 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.77× (z +9.8) | — |
| [[SW 1088 (line)]] | alt | 102 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.27× (z +9.3) | — |
| [[SW 900 (line)]] | alt | 59.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.05× (z +12.7) | — |
| [[SW48 (line)]] | wt | 33.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.35× (z +9.5) | — |
| [[AN3 CA (line)]] | alt | 19.1 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 15.4 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 12.2 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 10.1 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 53.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 183 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.20 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 9.99 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 26.9 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.1 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 20.8 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 9.32 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 146 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2810), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIK3R3]] | +0.64 | +0.69 / +0.60 | both halves | 7e-06 |  |
| [[FAM222A]] | +0.62 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[C21orf91]] | +0.62 | +0.57 / +0.66 | both halves | 1e-05 |  |
| [[HEXIM1]] | +0.62 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[SHISA5]] | +0.60 | +0.60 / +0.48 | both halves | 2e-05 |  |
| [[GCH1]] | +0.60 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[ZSWIM6]] | +0.59 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[ATF3]] | +0.59 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[ARIH1]] | +0.58 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[NR4A3]] | +0.58 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[NFKBIZ]] | +0.57 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[AHR]] | +0.56 | +0.60 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMF1]] | -0.59 | -0.62 / -0.50 | both halves | 1e-05 |  |
| [[RFT1]] | -0.59 | -0.60 / -0.56 | both halves | 1e-05 |  |
| [[ZDHHC6]] | -0.55 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[NUDCD3]] | -0.53 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[CDC16]] | -0.52 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[TIGD1]] | -0.52 | -0.46 / -0.52 | both halves | 3e-05 |  |
| [[TRMT61B]] | -0.52 | -0.43 / -0.58 | both halves | 3e-05 |  |
| [[SNRNP40]] | -0.51 | -0.58 / -0.42 | both halves | 4e-05 | same gene group |
| [[MRPS35]] | -0.51 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[DNAJC17]] | -0.51 | -0.57 / -0.45 | both halves | 3e-05 |  |
| [[ALG5]] | -0.51 | -0.46 / -0.54 | both halves | 2e-05 |  |
| [[ZNF875]] | -0.51 | -0.49 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C21orf91]] | B | C21orf91 activity raises TLE4's level | lines that do not express C21orf91 (5) vs lines expressing it (45) | 5.71× lower at baseline in the lines without C21orf91 | 0.001 | ⚠ within organs, on part of the lines; co-absent genes; also absent: USP25, GSDMD, RALGPS2 |
| [[TOP2A]] | B | TOP2A activity lowers TLE4's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[DUSP10]] | B | DUSP10 activity raises TLE4's level | lines that do not express DUSP10 (11) vs lines expressing it (39) | 3.62× lower at baseline in the lines without DUSP10 | 0.035 | ⚠ within organs, on part of the lines; also absent: GLRX, GBP2, TMEM92-AS1; maybe low, not absent |
| [[SEMA4A]] | B | SEMA4A activity raises TLE4's level | lines that do not express SEMA4A (8) vs lines expressing it (42) | 4.50× lower at baseline in the lines without SEMA4A | 0.072 | ⚠ within organs, on part of the lines; also absent: EPAS1, IER3, ATP1B1 |
| [[CTSS]] | B | CTSS activity raises TLE4's level | lines that do not express CTSS (15) vs lines expressing it (35) | 2.64× lower at baseline in the lines without CTSS | 0.072 | ⚠ within organs, on part of the lines; also absent: LINC02257, NMRAL2P-1, CSF2; maybe low, not absent |
| [[KITLG]] | C | KITLG activity raises TLE4's level | lines that do not express KITLG (10) vs lines expressing it (40) | 3.94× lower at baseline in the lines without KITLG | 0.060 | ⚠ within organs, on part of the lines; also absent: ETS2, CDA, LMO7; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 13, C 1. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PMAIP1]] | B | TLE4 activity raises PMAIP1's level | lines that do not express TLE4 (10) vs lines expressing it (40) | 2.62× lower at baseline in the lines without TLE4 | 0.010 | ⚠ within organs, on part of the lines; also absent: LMO7, CA13, KITLG |
| [[DUSP10]] | B | TLE4 activity raises DUSP10's level | lines that do not express TLE4 (10) vs lines expressing it (40) | 3.11× lower at baseline in the lines without TLE4 | 0.034 | ⚠ within organs, on part of the lines; also absent: LMO7, CA13, KITLG |
| [[BTG1]] | B | TLE4 activity raises BTG1's level | lines that do not express TLE4 (10) vs lines expressing it (40) | 1.96× lower at baseline in the lines without TLE4 | 0.039 | ⚠ within organs, on part of the lines; also absent: LMO7, CA13, KITLG |
| [[CEMIP2]] | B | TLE4 activity raises CEMIP2's level | lines that do not express TLE4 (10) vs lines expressing it (40) | 2.58× lower at baseline in the lines without TLE4 | 0.049 | ⚠ within organs, on part of the lines; also absent: LMO7, CA13, KITLG |
| [[NFKBIZ]] | B | TLE4 activity raises NFKBIZ's level | lines that do not express TLE4 (10) vs lines expressing it (40) | 1.77× lower at baseline in the lines without TLE4 | 0.056 | ⚠ within organs, on part of the lines; also absent: LMO7, CA13, KITLG |
| [[NEDD9]] | B | TLE4 activity raises NEDD9's level | lines that do not express TLE4 (10) vs lines expressing it (40) | 3.45× lower at baseline in the lines without TLE4 | 0.056 | ⚠ within organs, on part of the lines; also absent: LMO7, CA13, KITLG |
| [[KLHL15]] | B | TLE4 activity lowers KLHL15's level | lines that do not express TLE4 (10) vs lines expressing it (40) | 1.50× higher at baseline in the lines without TLE4 | 0.073 | ⚠ within organs, on part of the lines; also absent: LMO7, CA13, KITLG |
| [[RND3]] | B | TLE4 activity raises RND3's level | lines that do not express TLE4 (10) vs lines expressing it (40) | 2.62× lower at baseline in the lines without TLE4 | 0.079 | ⚠ within organs, on part of the lines; also absent: LMO7, CA13, KITLG |
| [[C21orf91]] | B | TLE4 activity raises C21orf91's level | lines that do not express TLE4 (10) vs lines expressing it (40) | 2.19× lower at baseline in the lines without TLE4 | 0.085 | ⚠ within organs, on part of the lines; also absent: LMO7, CA13, KITLG |
| [[IRF1]] | B | TLE4 activity raises IRF1's level | lines that do not express TLE4 (10) vs lines expressing it (40) | 1.24× lower at baseline in the lines without TLE4 | 0.090 | ⚠ within organs, on part of the lines; also absent: LMO7, CA13, KITLG |
| cells under [[Adagrasib (drug)]] 5 µM | B | TLE4 activity raises the cells' numbers under Adagrasib 5 µM (protects the cells) | lines that do not express TLE4 (10) vs lines expressing it (38) | the lines without TLE4: 0.80× the cells of the other lines | 0.091 | ⚠ within organs, on part of the lines; also absent: LMO7, CA13, KITLG |
| [[AHR]] | B | TLE4 activity raises AHR's level | lines that do not express TLE4 (10) vs lines expressing it (40) | 2.47× lower at baseline in the lines without TLE4 | 0.092 | ⚠ within organs, on part of the lines; also absent: LMO7, CA13, KITLG |

## Where it sits

- **Module**: [[Module 093]] — TNF-alpha signaling via NF-kB; 49 genes; every member is in the + arm (projection on the module's main direction 0.685). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (28.9, -27.6); signed map (4.0, 18.1). **Vector** length 118, 34.3% of its response variance represented; |z| ≥ 3 in 1,139 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.5 | +7.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.4 | +5.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | +3.1 | +4.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | +6.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.0 | +3.1 |
|  | [[Gefitinib (drug)]] 5 µM |  | +2.4 | +2.2 |
|  | [[Cyclosporin A (drug)]] 0.05 µM |  | +2.3 | +1.5 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~22% of this change | -5.0 | -3.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.8 | -3.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -4.6 | -2.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.9 | -2.4 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -3.2 | -3.4 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -3.1 | -2.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.0 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | TLE family member 4, transcriptional corepressor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q21.31 — chr9:79,571,773-79,726,882 (+) |
| Ensembl biotype | protein_coding |
| Also known as | E(spl), ESG, GRG4 |
| Gene groups (HGNC) | WD repeat domain containing; Wnt enhanceosome complex; TLE family |
| Hallmark sets | SPERMATOGENESIS |
| Reactome | 9 pathways, smallest: Repression of WNT target genes; Deactivation of the beta-catenin transactivating complex; NOTCH1 Intracellular Domain Regulates Transcription |
| Matched by | ensembl_id |

**Function**, from UniProt [Q04727](https://www.uniprot.org/uniprotkb/Q04727) (Transducin-like enhancer protein 4):

> Transcriptional corepressor that binds to a number of transcription factors. Inhibits the transcriptional activation mediated by PAX5, and by CTNNB1 and TCF family members in Wnt signaling. The effects of full-length TLE family members may be modulated by association with dominant-negative AES. Essential for the transcriptional repressor activity of SIX3 during retina and lens development and for SIX3 transcriptional auto-repression (By similarity). Involved in transcriptional repression of …

**Summary**, from NCBI Gene [7091](https://www.ncbi.nlm.nih.gov/gene/7091):

> Predicted to enable transcription corepressor activity. Predicted to be involved in negative regulation of canonical Wnt signaling pathway and negative regulation of transcription by RNA polymerase II. Predicted to act upstream of or within Wnt signaling pathway; cellular response to leukemia inhibitory factor; and negative regulation of DNA-templated transcription. Located in nucleoplasm. Part of beta-catenin-TCF complex. [provided by Alliance of Genome Resources, Apr 2025]

**Accessions** — [HGNC:11840](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11840) · Entrez [7091](https://www.ncbi.nlm.nih.gov/gene/7091) · UniProt [Q04727](https://www.uniprot.org/uniprotkb/Q04727) · Ensembl [ENSG00000106829](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106829)

## Data

Gene col 2810: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2810); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2810, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2810]; `tensor/DDL_lfc|DDL_z.npy` [2810]; `embed/gene_vectors.npy` [2810]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2810 or target_col == 2810). Every well: [[TLE4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TLE4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
