---
symbol: "NRG2"
type: "gene"
col: 8164
ensembl_id: "ENSG00000158458"
name: "neuregulin 2"
location: "5q31.2"
module: 176
arm: "+"
pooled_cpm: 20.24
n_lines_expressing: 35
n_dd_up: 31
n_dd_down: 36
n_dd_up_clean: 25
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 14
direction_downstream: 5
tags: ["gene", "module/176"]
generated_by: "tahoemap"
---

# NRG2

*neuregulin 2* — 5q31.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.88× (z +22.9, q 0e+00, up in 27 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 36 drug-doses (14 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.492× (z -10.9, q 9e-25, down in 20 of 33 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EPB41L4B]] (+0.59, fdr 1e-05), [[ADAM22]] (+0.55, fdr 1e-05), [[NFIA]] (+0.54, fdr 1e-05); moves opposite to [[DNAL4]] (-0.51, fdr 7e-05), [[CHMP4A]] (-0.48, fdr 7e-05), [[PRMT2]] (-0.46, fdr 1e-04).
> It is in [[Module 176]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 14 arrows point to it, the strongest [[RNF220]] → it (grade B ⚠); 5 go from it, the strongest it → [[GNAO1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8164.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.88×** | +22.9 | 0e+00 | 27/33 (HS-578T, SW1417, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.65×** | +21.1 | 0e+00 | 27/33 (SW480, SW1417, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **3.11×** | +17.4 | 0e+00 | 28/33 (SW480, HOP62, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.53×** | +14.2 | 7e-44 | 25/32 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **4.23×** | +11.6 | 8e-29 | 29/33 (HOP62, SW1417, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.98×** | +10.4 | 2e-23 | 20/32 (SW480, A-172, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.94×** | +10.1 | 3e-22 | 18/32 (NCI-H1792, SW1417, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.68×** | +8.0 | 1e-13 | 16/33 (NCI-H1573, NCI-H1792, …) | all doses, flat |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.61×** | +7.0 | 2e-10 | 13/32 (HS-578T, C-33 A, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.41×** | +5.3 | 6e-06 | 13/33 (NCI-H1792, NCI-H1573, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.41×** | +5.2 | 9e-06 | 11/32 (A498, NCI-H460, …) | all doses, flat |  |
| [[Brivudine (drug)]] 0.5 µM |  | **1.60×** | +5.1 | 2e-05 | 10/33 (SW480, A-172, …) | rises with dose | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.38×** | +5.0 | 3e-05 | 14/33 (NCI-H2030, C32, …) | all doses, stronger at high dose |  |
| [[Radotinib (drug)]] 5 µM |  | **1.25×** | +4.7 | 8e-05 | 14/33 (NCI-H2030, NCI-H1792, …) | top dose only |  |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.36×** | +4.7 | 1e-04 | 6/32 (PANC-1, SK-MEL-2, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.32×** | +4.2 | 9e-04 | 9/33 (SK-MEL-2, SW480, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.21×** | +4.1 | 0.001 | 9/33 (SW1417, HS-578T, …) | top dose only |  |
| [[Ipatasertib (drug)]] 5 µM |  | **1.67×** | +4.1 | 0.001 | 8/33 (PANC-1, C32, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.28×** | +3.8 | 0.004 | 10/32 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 14 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 36 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8164.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.492×** | -10.9 | 9e-25 | 20/33 (LOX-IMVI, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.564×** | -8.8 | 5e-16 | 19/32 (SNU-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.675×** | -8.5 | 3e-15 | 26/33 (CHP-212, AN3 CA, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.588×** | -8.1 | 5e-14 | 17/32 (SNU-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.623×** | -7.2 | 4e-11 | 17/28 (C-33 A, Hs 766T, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.624×** | -7.2 | 4e-11 | 19/33 (SNU-1, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~9% here) |
| [[Peretinoin (drug)]] 5 µM |  | **0.631×** | -6.8 | 8e-10 | 18/32 (NCI-H23, AN3 CA, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **0.737×** | -6.6 | 3e-09 | 17/32 (A-427, Hs 766T, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.654×** | -6.3 | 2e-08 | 13/21 (NCI-H2030, AN3 CA, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~28% of this change | **0.679×** | -5.9 | 2e-07 | 15/30 (PANC-1, RPMI-7951, …) | inconsistent across doses | low cells (technical?) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.688×** | -5.7 | 5e-07 | 16/32 (AN3 CA, A-172, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.689×** | -5.7 | 5e-07 | 16/32 (LOX-IMVI, NCI-H23, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.692×** | -5.7 | 7e-07 | 12/32 (AN3 CA, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.702×** | -5.2 | 7e-06 | 16/33 (NCI-H2030, NCI-H460, …) | two highest doses | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.716×** | -5.1 | 1e-05 | 16/32 (A-427, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.531×** | -5.1 | 1e-05 | 12/33 (A-427, NCI-H2030, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.728×** | -4.9 | 4e-05 | 12/33 (SNU-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.735×** | -4.7 | 7e-05 | 16/32 (AN3 CA, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.566×** | -4.6 | 2e-04 | 11/33 (NCI-H1792, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.746×** | -4.0 | 0.002 | 15/33 (NCI-H2030, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[TAK-733 (drug)]] 5 µM |  | **0.622×** | -3.8 | 0.004 | 10/32 (SW 1271, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.05 µM |  | **0.769×** | -3.7 | 0.005 | 10/32 (NCI-H23, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.808×** | -3.3 | 0.024 | 8/32 (NCI-H2030, A498, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.41 per unit of S-phase module lfc, -0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8164. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 49.2 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.160× (z -14.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.259× (z -11.2) |
| [[PANC-1 (line)]] | alt | 62.1 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.296× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.373× (z -9.5) |
| [[A-427 (line)]] | wt | 49.0 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.106× (z -18.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.293× (z -10.3) |
| [[AN3 CA (line)]] | alt | 128 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0696× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.136× (z -10.5) |
| [[Hs 766T (line)]] | wt | 91.3 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.275× (z -14.0) ⚠ cell-cycle shift, explains ~65% of this change |
| [[NCI-H23 (line)]] | alt | 35.2 | 1 | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.33× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.421× (z -8.8) ⚠ cell-cycle shift, explains ~65% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.253× (z -8.8) |
| [[NCI-H460 (line)]] | wt | 42.2 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -11.9) ⚠ cell-cycle shift, explains ~65% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.197× (z -10.9) |
| [[SNU-1 (line)]] | wt | 35.8 | 0 | 4 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0207× (z -18.8) |
| [[A498 (line)]] | wt | 27.5 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.216× (z -10.0) ⚠ toxic; transcription drop · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.210× (z -9.1) |
| [[C-33 A (line)]] | alt | 72.0 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.118× (z -15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 6.24 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.1× (z +13.3) | — |
| [[LOX-IMVI (line)]] | wt | 12.2 | 2 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.98× (z +9.8) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0732× (z -13.0) |
| [[SW1417 (line)]] | alt | 7.42 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.26× (z +11.2) | — |
| [[SW480 (line)]] | alt | 17.6 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 2.99× (z +11.0) | — |
| [[A-172 (line)]] | wt | 19.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.65× (z +10.0) | — |
| [[A549 (line)]] | wt | 17.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.24× (z +9.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 10.7 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.370× (z -13.3) ⚠ position not correctable |
| [[NCI-H1573 (line)]] | alt | 5.60 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 6.00× (z +10.1) | — |
| [[NCI-H661 (line)]] | alt | 50.0 | 0 | 1 | — | [[Cabozantinib (S-malate) (drug)]] 0.5 µM 0.0627× (z -9.4) |
| [[RPMI-7951 (line)]] | alt | 15.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.61× (z +10.0) | — |
| [[SHP-77 (line)]] | alt | 10.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.07× (z +10.1) | — |
| [[SK-MEL-2 (line)]] | alt | 23.3 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.05× (z +8.5) | — |
| [[AsPC-1 (line)]] | alt | 2.03 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.57 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.56 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 33.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.32 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 8.72 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.59 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.85 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.07 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.33 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.34 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 4.71 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.03 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.21 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.05 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 7.07 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.17 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.31 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.22 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 81.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.26 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8164), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPB41L4B]] | +0.59 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[ADAM22]] | +0.55 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[NFIA]] | +0.54 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[FHL1]] | +0.54 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[MCOLN2]] | +0.54 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[FAM184A]] | +0.53 | +0.35 / +0.59 | both halves | 1e-04 |  |
| [[GNAO1]] | +0.53 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[PRKAR2B]] | +0.53 | +0.45 / +0.58 | both halves | 3e-05 | pathway: Intracellular signaling by second messengers |
| [[TMEM108]] | +0.53 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[LINC02643]] | +0.52 | +0.58 / +0.47 | both halves | 2e-05 |  |
| [[ROR1]] | +0.52 | +0.47 / +0.49 | both halves | 2e-05 | same gene group |
| [[CCDC88C]] | +0.51 | +0.53 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAL4]] | -0.51 | -0.56 / -0.38 | both halves | 7e-05 |  |
| [[CHMP4A]] | -0.48 | -0.37 / -0.50 | both halves | 7e-05 |  |
| [[PRMT2]] | -0.46 | -0.35 / -0.49 | both halves | 1e-04 |  |
| [[BBS1]] | -0.45 | -0.38 / -0.45 | both halves | 6e-05 |  |
| [[FCF1]] | -0.44 | -0.40 / -0.36 | both halves | 9e-05 |  |
| [[UMAD1]] | -0.43 | -0.51 / -0.36 | both halves | 9e-05 |  |
| [[ACOX3]] | -0.43 | -0.45 / -0.36 | both halves | 9e-05 |  |
| [[CHM]] | -0.42 | -0.34 / -0.46 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 8, C 6. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RNF220]] | B | RNF220 activity raises NRG2's level | lines that do not express RNF220 (9) vs lines expressing it (41) | 2.61× lower at baseline in the lines without RNF220 | 0.016 | ⚠ within organs, on part of the lines; also absent: GNAZ, ENSG00000287400, CTXN1; maybe low, not absent |
| [[SH3RF3]] | B | SH3RF3 activity raises NRG2's level | lines that do not express SH3RF3 (14) vs lines expressing it (36) | 2.46× lower at baseline in the lines without SH3RF3 | 0.020 | ⚠ within organs, on part of the lines; also absent: DCLK2, OSBPL6, FHL1 |
| [[LPAR3]] | B | LPAR3 activity raises NRG2's level | lines that do not express LPAR3 (16) vs lines expressing it (34) | 2.22× lower at baseline in the lines without LPAR3 | 0.034 | ⚠ within organs, on part of the lines; also absent: BEX4, ADAMTS18, GAB3; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers NRG2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[EBF2]] | B | EBF2 activity raises NRG2's level | lines that do not express EBF2 (18) vs lines expressing it (32) | 2.37× lower at baseline in the lines without EBF2 | 0.067 | ⚠ within organs, on part of the lines; also absent: ENSG00000249738, LMX1B, CAPN14; maybe low, not absent |
| [[GNAO1]] | B | GNAO1 activity raises NRG2's level | lines that do not express GNAO1 (22) vs lines expressing it (28) | 2.63× lower at baseline in the lines without GNAO1 | 0.084 | ⚠ within organs, on part of the lines; also absent: MGAT5B, KCNG1, SLC6A17 |
| [[TBX1]] | B | TBX1 activity raises NRG2's level | lines that do not express TBX1 (23) vs lines expressing it (27) | 2.03× lower at baseline in the lines without TBX1 | 0.092 | ⚠ within organs, on part of the lines; also absent: BEGAIN, PALM, OLFM1 |
| [[LINC02643]] | B | LINC02643 activity raises NRG2's level | lines that do not express LINC02643 (38) vs lines expressing it (12) | 4.44× lower at baseline in the lines without LINC02643 | 0.099 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MMRN1, GCG, ENSG00000289530 |
| [[FHL1]] | C | FHL1 activity raises NRG2's level | lines that do not express FHL1 (19) vs lines expressing it (31) | 4.32× lower at baseline in the lines without FHL1 | 0.002 | ⚠ within organs, on part of the lines; also absent: ADAMTS7, ANTXR1, MSRB3; co-absent with the target |
| [[DLX1]] | C | DLX1 activity raises NRG2's level | lines that do not express DLX1 (13) vs lines expressing it (37) | 3.50× lower at baseline in the lines without DLX1 | 0.033 | ⚠ within organs, on part of the lines; also absent: TMEM145, GXYLT2, FSD1; co-absent with the target |
| [[VASH1]] | C | VASH1 activity raises NRG2's level | lines that do not express VASH1 (16) vs lines expressing it (34) | 3.67× lower at baseline in the lines without VASH1 | 0.038 | ⚠ within organs, on part of the lines; also absent: ANTXR1, ADAMTS7, WNT5B; co-absent with the target |
| [[PHF21B]] | C | PHF21B activity raises NRG2's level | lines that do not express PHF21B (21) vs lines expressing it (29) | 3.74× lower at baseline in the lines without PHF21B | 0.054 | ⚠ within organs, on part of the lines; also absent: JAM3, ADAM23, ADD2; co-absent with the target |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 3, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GNAO1]] | B | NRG2 activity raises GNAO1's level | lines that do not express NRG2 (15) vs lines expressing it (35) | 3.23× lower at baseline in the lines without NRG2 | 0.055 | ⚠ within organs, on part of the lines; also absent: SHOX2, NOVA2, PHF21B |
| [[PIGX]] | B | NRG2 activity raises PIGX's level | lines that do not express NRG2 (15) vs lines expressing it (35) | 1.19× lower at baseline in the lines without NRG2 | 0.060 | ⚠ within organs, on part of the lines; also absent: SHOX2, NOVA2, PHF21B |
| [[MAP3K5]] | B | NRG2 activity weakens MAP3K5's drug response | lines that do not express NRG2 (14) vs lines expressing it (32) | the lines without NRG2 respond 1.34× as strongly (z diff -1.59); strongest at Dinaciclib 0.05 µM: 0.35x vs 0.57x (z diff -4.5) | 0.067 | ⚠ within organs, on part of the lines; also absent: SHOX2, NOVA2, PHF21B; target measured in part of the lines; artifact flags |
| [[FHL1]] | C | NRG2 activity raises FHL1's level | lines that do not express NRG2 (15) vs lines expressing it (35) | 4.56× lower at baseline in the lines without NRG2 | 0.016 | ⚠ within organs, on part of the lines; also absent: SHOX2, NOVA2, PHF21B; co-absent with the target |
| [[TRIM9]] | C | NRG2 activity raises TRIM9's level | lines that do not express NRG2 (15) vs lines expressing it (35) | 4.81× lower at baseline in the lines without NRG2 | 0.040 | ⚠ within organs, on part of the lines; also absent: SHOX2, NOVA2, PHF21B; co-absent with the target |

## Where it sits

- **Module**: [[Module 176]]; 22 genes; every member is in the + arm (projection on the module's main direction 0.537). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-0.5, 38.8); signed map (24.2, 30.8). **Vector** length 88.7, 20.7% of its response variance represented; |z| ≥ 3 in 1,063 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.8 | +21.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.8 | +14.2 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +5.3 | +17.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.8 | +22.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.6 | +11.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.2 | +4.2 |
|  | [[Brivudine (drug)]] 0.5 µM |  | +2.2 | +5.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.1 | +4.7 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | -3.3 | -6.6 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | -3.3 | -3.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.9 | -1.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -2.5 | -1.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.3 | -2.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.2 | -2.7 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -2.2 | -1.5 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -2.1 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | neuregulin 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q31.2 — chr5:139,846,779-140,043,299 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Don-1, NTAK, HRG2 |
| Gene groups (HGNC) | I-set domain containing; Neuregulins |
| Reactome | 29 pathways, smallest: GRB7 events in ERBB2 signaling; PI3K events in ERBB4 signaling; Downregulation of ERBB2:ERBB3 signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [O14511](https://www.uniprot.org/uniprotkb/O14511) (Pro-neuregulin-2, membrane-bound isoform):

> Direct ligand for ERBB3 and ERBB4 tyrosine kinase receptors. Concomitantly recruits ERBB1 and ERBB2 coreceptors, resulting in ligand-stimulated tyrosine phosphorylation and activation of the ERBB receptors. May also promote the heterodimerization with the EGF receptor.

**Summary**, from NCBI Gene [9542](https://www.ncbi.nlm.nih.gov/gene/9542):

> This gene encodes a novel member of the neuregulin family of growth and differentiation factors. Through interaction with the ERBB family of receptors, this protein induces the growth and differentiation of epithelial, neuronal, glial, and other types of cells. The gene consists of 12 exons and the genomic structure is similar to that of neuregulin 1, another member of the neuregulin family of ligands. The products of these genes mediate distinct biological processes by acting at different …

**Accessions** — [HGNC:7998](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7998) · Entrez [9542](https://www.ncbi.nlm.nih.gov/gene/9542) · UniProt [O14511](https://www.uniprot.org/uniprotkb/O14511) · Ensembl [ENSG00000158458](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000158458)

## Data

Gene col 8164: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8164); `tables/drug_effects.parquet` (68 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8164, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8164]; `tensor/DDL_lfc|DDL_z.npy` [8164]; `embed/gene_vectors.npy` [8164]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8164 or target_col == 8164). Every well: [[NRG2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NRG2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
