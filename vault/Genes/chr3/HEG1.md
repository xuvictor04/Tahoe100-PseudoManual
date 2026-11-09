---
symbol: "HEG1"
type: "gene"
col: 10421
ensembl_id: "ENSG00000173706"
name: "heart development protein with EGF like domains 1"
location: "3q21.2"
module: 66
arm: "+"
pooled_cpm: 64.55
n_lines_expressing: 39
n_dd_up: 28
n_dd_down: 26
n_dd_up_clean: 22
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 13
direction_downstream: 24
tags: ["gene", "module/066"]
generated_by: "tahoemap"
---

# HEG1

*heart development protein with EGF like domains 1* — 3q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.52× (z +6.8, q 7e-09, up in 14 of 28 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.30× (z +6.2, q 1e-07, up in 20 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.543× (z -14.4, q 3e-44, down in 27 of 37 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC00842]] (+0.58, fdr 1e-05), [[SNX24]] (+0.55, fdr 2e-05), [[TRIO]] (+0.54, fdr 2e-05); moves opposite to [[ACP6]] (-0.47, fdr 4e-05), [[KLHL28]] (-0.45, fdr 7e-05), [[TLE6]] (-0.45, fdr 5e-05).
> It is in [[Module 066]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 13 arrows point to it, the strongest [[MSRB3]] → it (grade B ⚠); 24 go from it, the strongest it → [[SACS]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10421.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.52×** | +6.8 | 7e-09 | 14/28 (LoVo, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.46×** | +6.3 | 1e-07 | 19/37 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.30×** | +6.2 | 1e-07 | 20/37 (HEC-1-A, A-172, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.42×** | +5.7 | 2e-06 | 18/36 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.39×** | +5.5 | 4e-06 | 15/36 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM |  | **1.40×** | +5.3 | 9e-06 | 20/37 (NCI-H460, HOP62, …) | all doses, flat | cell-cycle shift (explains ~19% here); noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.34×** | +4.9 | 7e-05 | 17/37 (HEC-1-A, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.39×** | +4.9 | 8e-05 | 18/36 (SW 900, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 0.05 µM |  | **1.23×** | +4.9 | 8e-05 | 19/37 (NCI-H460, HOP62, …) | all doses, flat |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.48×** | +4.7 | 2e-04 | 14/37 (PANC-1, NCI-H460, …) | all doses, flat | low cells (technical?); noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.36×** | +4.6 | 2e-04 | 17/37 (NCI-H460, HOP62, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.32×** | +4.4 | 5e-04 | 18/36 (NCI-H460, SHP-77, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.25×** | +4.4 | 5e-04 | 18/37 (HOP62, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[RMC-6236 (drug)]] 5 µM |  | **1.61×** | +4.2 | 0.001 | 18/37 (NCI-H460, HOP62, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.30×** | +4.2 | 0.001 | 17/37 (NCI-H460, SW 900, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.29×** | +4.1 | 0.001 | 16/36 (HOP62, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.58×** | +4.0 | 0.002 | 15/37 (HOP62, NCI-H460, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.29×** | +3.7 | 0.006 | 12/36 (PANC-1, HS-578T, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.17× | +3.7 | 0.006 | 12/37 (SK-MEL-2, A-172, …) | rises with dose |  |
| [[vincristine (drug)]] 5 µM |  | **1.52×** | +3.7 | 0.007 | 14/33 (PANC-1, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 11 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10421.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.543×** | -14.4 | 3e-44 | 27/37 (LOX-IMVI, J82, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.597×** | -12.2 | 1e-31 | 26/36 (LOX-IMVI, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.517×** | -11.0 | 7e-26 | 31/37 (J82, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.519×** | -10.5 | 1e-23 | 28/37 (A498, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.546×** | -10.1 | 6e-22 | 26/36 (SNU-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.566×** | -9.5 | 2e-19 | 27/37 (J82, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.593×** | -8.4 | 4e-15 | 25/37 (SK-MEL-2, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.649×** | -7.2 | 4e-11 | 22/37 (J82, LOX-IMVI, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.653×** | -7.1 | 8e-11 | 22/37 (SNU-1, NCI-H1792, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.448×** | -7.0 | 1e-10 | 21/38 (LOX-IMVI, A498, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.651×** | -6.9 | 3e-10 | 26/37 (LOX-IMVI, SNU-1, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.688×** | -5.5 | 2e-06 | 18/37 (A498, SW480, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.741×** | -5.0 | 3e-05 | 20/37 (NCI-H1792, SNU-1, …) | rises with dose | composition shift |
| [[Abemaciclib (drug)]] 5 µM |  | **0.578×** | -4.8 | 7e-05 | 19/37 (SNU-1, J82, …) | rises with dose | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.747×** | -4.7 | 1e-04 | 20/36 (A498, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~17% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.803×** | -3.7 | 0.009 | 12/37 (SW480, SNU-1, …) | all doses, stronger at high dose |  |
| [[EX229 (drug)]] 0.05 µM |  | **0.794×** | -3.6 | 0.009 | 15/37 (Hs 766T, SHP-77, …) | all doses, flat |  |
| [[Terfenadine (drug)]] 5 µM |  | 0.866× | -3.4 | 0.019 | 7/37 (Hs 766T, HEC-1-A, …) | top dose only | position effect removed |
| [[EX229 (drug)]] 5 µM |  | **0.689×** | -3.2 | 0.030 | 13/36 (SNU-1, HS-578T, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10421. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-1 (line)]] | wt | 258 | 0 | 12 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0946× (z -21.7) |
| [[A498 (line)]] | wt | 77.4 | 0 | 10 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.185× (z -17.9) |
| [[LOX-IMVI (line)]] | wt | 179 | 0 | 10 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.217× (z -22.6) |
| [[J82 (line)]] | alt | 550 | 0 | 9 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.257× (z -19.1) |
| [[NCI-H1792 (line)]] | alt | 185 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.147× (z -15.9) |
| [[NCI-H23 (line)]] | alt | 30.8 | 0 | 5 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.157× (z -12.0) |
| [[A549 (line)]] | wt | 22.8 | 0 | 4 | — | [[Harringtonine (drug)]] 5 µM 0.229× (z -10.1) |
| [[H4 (line)]] | wt | 133 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.176× (z -12.5) |
| [[HOP62 (line)]] | alt | 105 | 2 (1 ⚠) | 2 | [[Adagrasib (drug)]] 0.05 µM 1.61× (z +11.0) ⚠ position not correctable · without an alert: [[Cobimetinib (drug)]] 5 µM 3.99× (z +8.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.385× (z -8.7) |
| [[NCI-H2030 (line)]] | alt | 47.9 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.376× (z -12.1) |
| [[NCI-H460 (line)]] | wt | 25.5 | 4 (1 ⚠) | 0 | [[Pitavastatin (Calcium) (drug)]] 5 µM 3.39× (z +9.6) ⚠ cell-cycle shift, explains ~18% of this change · without an alert: [[Trametinib (drug)]] 5 µM 3.08× (z +9.1) | — |
| [[SK-MEL-2 (line)]] | alt | 67.7 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 3.04× (z +9.9) ⚠ toxic; transcription drop | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.275× (z -11.6) |
| [[SW 900 (line)]] | alt | 77.6 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 7.66× (z +13.5) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.400× (z -9.7) |
| [[A-172 (line)]] | wt | 152 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.364× (z -11.5) |
| [[HepG2_C3A (line)]] | wt | 97.2 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.250× (z -11.8) |
| [[HS-578T (line)]] | alt | 123 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.180× (z -13.7) |
| [[LoVo (line)]] | wt | 35.4 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 5.60× (z +11.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.237× (z -10.2) |
| [[PANC-1 (line)]] | alt | 53.4 | 1 | 2 | [[Peretinoin (drug)]] 5 µM 2.18× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.403× (z -14.9) |
| [[SW480 (line)]] | alt | 39.3 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.332× (z -10.0) |
| [[A-427 (line)]] | wt | 42.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.145× (z -16.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.386× (z -12.6) |
| [[HEC-1-A (line)]] | alt | 20.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -12.1) |
| [[CHP-212 (line)]] | wt | 38.0 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.0969× (z -9.2) |
| [[Hs 766T (line)]] | wt | 43.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -11.0) |
| [[MIA PaCa-2 (line)]] | alt | 16.3 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.207× (z -11.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 16.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.8× (z +9.2) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 29.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.203× (z -16.0) |
| [[RPMI-7951 (line)]] | alt | 81.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.337× (z -11.7) |
| [[SW 1088 (line)]] | alt | 77.0 | 0 | 1 | — | [[Furosemide (drug)]] 0.5 µM 0.0467× (z -9.9) |
| [[AN3 CA (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.28 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 8.69 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.4 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 13.0 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 13.8 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 8.90 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 6.73 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 75.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.30 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 5.18 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 6.06 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 47.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 84.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 66.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 13.1 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10421), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00842]] | +0.58 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[SNX24]] | +0.55 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[TRIO]] | +0.54 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[GPR176]] | +0.51 | +0.44 / +0.54 | both halves | 3e-05 |  |
| [[FILIP1L]] | +0.51 | +0.35 / +0.56 | both halves | 1e-04 |  |
| [[NDST1]] | +0.50 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[STARD13]] | +0.50 | +0.39 / +0.56 | both halves | 6e-05 |  |
| [[THBS1]] | +0.50 | +0.39 / +0.52 | both halves | 6e-05 |  |
| [[RASAL2]] | +0.50 | +0.43 / +0.51 | both halves | 3e-05 |  |
| [[ENAH]] | +0.50 | +0.41 / +0.47 | both halves | 4e-05 |  |
| [[DAB2]] | +0.49 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[PALLD]] | +0.49 | +0.45 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACP6]] | -0.47 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[KLHL28]] | -0.45 | -0.49 / -0.37 | both halves | 7e-05 |  |
| [[TLE6]] | -0.45 | -0.40 / -0.52 | both halves | 5e-05 |  |
| [[ST8SIA6]] | -0.44 | -0.42 / -0.36 | both halves | 9e-05 |  |
| [[TOGARAM1]] | -0.43 | -0.35 / -0.48 | both halves | 1e-04 |  |
| [[SPATA7]] | -0.42 | -0.33 / -0.45 | both halves | 1e-04 |  |
| [[ECD]] | -0.41 | -0.35 / -0.38 | both halves | 1e-04 |  |
| [[ADAM8]] | -0.41 | -0.31 / -0.47 | both halves | 2e-04 |  |
| [[C16orf46]] | -0.40 | -0.31 / -0.45 | both halves | 2e-04 |  |
| [[SMIM31]] | -0.40 | -0.35 / -0.38 | both halves | 1e-04 |  |
| [[TGDS]] | -0.40 | -0.36 / -0.40 | both halves | 9e-05 |  |
| [[CFAP36]] | -0.40 | -0.26 / -0.47 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 13, C 0. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MSRB3]] | B | MSRB3 activity raises HEG1's level | lines that do not express MSRB3 (20) vs lines expressing it (30) | 3.18× lower at baseline in the lines without MSRB3 | 0.011 | ⚠ within organs, on part of the lines; also absent: ARHGEF6, KCNG1, FHL1 |
| [[ITGA4]] | B | ITGA4 activity raises HEG1's level | lines that do not express ITGA4 (33) vs lines expressing it (17) | 2.96× lower at baseline in the lines without ITGA4 | 0.036 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: MMP2, SPARC, LINC01411 |
| [[RFTN1]] | B | RFTN1 activity raises HEG1's level | lines that do not express RFTN1 (20) vs lines expressing it (30) | 2.89× lower at baseline in the lines without RFTN1 | 0.039 | ⚠ within organs, on part of the lines; also absent: GPR176, KIAA0408, COL12A1 |
| [[GPR176]] | B | GPR176 activity raises HEG1's level | lines that do not express GPR176 (18) vs lines expressing it (32) | 2.75× lower at baseline in the lines without GPR176 | 0.045 | ⚠ within organs, on part of the lines; also absent: RFTN1, ARMCX1, AFAP1L1 |
| [[CCBE1]] | B | CCBE1 activity raises HEG1's level | lines that do not express CCBE1 (28) vs lines expressing it (22) | 2.69× lower at baseline in the lines without CCBE1 | 0.052 | ⚠ within organs, on part of the lines; also absent: EDNRA, IL7R, EFEMP1 |
| [[CDK15]] | B | CDK15 activity raises HEG1's level | lines that do not express CDK15 (28) vs lines expressing it (22) | 2.82× lower at baseline in the lines without CDK15 | 0.056 | ⚠ within organs, on part of the lines; also absent: POU3F2, PTGFR, NTM; maybe low, not absent |
| [[DCLK2]] | B | DCLK2 activity raises HEG1's level | lines that do not express DCLK2 (17) vs lines expressing it (33) | 2.31× lower at baseline in the lines without DCLK2 | 0.060 | ⚠ within organs, on part of the lines; also absent: LINC03041, HECW2, AFF3 |
| [[SACS]] | B | SACS activity raises HEG1's level | lines that do not express SACS (5) vs lines expressing it (45) | 4.68× lower at baseline in the lines without SACS | 0.069 | ⚠ within organs, on part of the lines; also absent: CRTAP, SNTA1, TMCC2; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity lowers HEG1's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.2% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[FAM171A1]] | B | FAM171A1 activity raises HEG1's level | lines that do not express FAM171A1 (7) vs lines expressing it (43) | 2.73× lower at baseline in the lines without FAM171A1 | 0.089 | ⚠ within organs, on part of the lines; also absent: PORCN, CMTM7, ANXA6 |
| [[FBN1]] | B | FBN1 activity raises HEG1's level | lines that do not express FBN1 (28) vs lines expressing it (22) | 3.02× lower at baseline in the lines without FBN1 | 0.091 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: GYPC, TENM2, ENSG00000280241 |
| [[LAYN]] | B | LAYN activity raises HEG1's level | lines that do not express LAYN (31) vs lines expressing it (19) | 2.83× lower at baseline in the lines without LAYN | 0.091 | ⚠ within organs, on part of the lines; also absent: COL1A1, ITGA11, LUM |

### Downstream of this gene

*24 arrows, 24 of them with an alert ⚠; grade A 0, B 24, C 0. Shown: the 12 strongest; 12 more arrows (12 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SACS]] | B | HEG1 activity raises SACS's level | lines that do not express HEG1 (11) vs lines expressing it (39) | 3.46× lower at baseline in the lines without HEG1 | 0.002 | ⚠ within organs, on part of the lines; also absent: CCDC88A, STARD9, RECK |
| [[ANKRD28]] | B | HEG1 activity raises ANKRD28's level | lines that do not express HEG1 (11) vs lines expressing it (39) | 1.83× lower at baseline in the lines without HEG1 | 0.002 | ⚠ within organs, on part of the lines; also absent: CCDC88A, STARD9, RECK |
| [[RUSC2]] | B | HEG1 activity raises RUSC2's level | lines that do not express HEG1 (11) vs lines expressing it (39) | 3.26× lower at baseline in the lines without HEG1 | 0.007 | ⚠ within organs, on part of the lines; also absent: CCDC88A, STARD9, RECK |
| [[NDST1]] | B | HEG1 activity raises NDST1's level | lines that do not express HEG1 (11) vs lines expressing it (39) | 2.22× lower at baseline in the lines without HEG1 | 0.008 | ⚠ within organs, on part of the lines; also absent: CCDC88A, STARD9, RECK |
| [[RAB31]] | B | HEG1 activity raises RAB31's level | lines that do not express HEG1 (11) vs lines expressing it (39) | 4.21× lower at baseline in the lines without HEG1 | 0.022 | ⚠ within organs, on part of the lines; also absent: CCDC88A, STARD9, RECK |
| [[SMIM31]] | B | HEG1 activity lowers SMIM31's level | lines that do not express HEG1 (11) vs lines expressing it (39) | 3.72× higher at baseline in the lines without HEG1 | 0.023 | ⚠ within organs, on part of the lines; also absent: CCDC88A, STARD9, RECK |
| [[KLHL5]] | B | HEG1 activity raises KLHL5's level | lines that do not express HEG1 (11) vs lines expressing it (39) | 3.85× lower at baseline in the lines without HEG1 | 0.028 | ⚠ within organs, on part of the lines; also absent: CCDC88A, STARD9, RECK |
| [[MSRB3]] | B | HEG1 activity raises MSRB3's level | lines that do not express HEG1 (11) vs lines expressing it (39) | 5.24× lower at baseline in the lines without HEG1 | 0.029 | ⚠ within organs, on part of the lines; also absent: CCDC88A, STARD9, RECK |
| [[TRIO]] | B | HEG1 activity raises TRIO's level | lines that do not express HEG1 (11) vs lines expressing it (39) | 1.94× lower at baseline in the lines without HEG1 | 0.033 | ⚠ within organs, on part of the lines; also absent: CCDC88A, STARD9, RECK |
| cells under [[Mifepristone (drug)]] 0.5 µM | B | HEG1 activity raises the cells' numbers under Mifepristone 0.5 µM (protects the cells) | lines that do not express HEG1 (11) vs lines expressing it (37) | the lines without HEG1: 0.80× the cells of the other lines | 0.037 | ⚠ within organs, on part of the lines; also absent: CCDC88A, STARD9, RECK |
| [[DEGS1]] | B | HEG1 activity raises DEGS1's level | lines that do not express HEG1 (11) vs lines expressing it (39) | 1.98× lower at baseline in the lines without HEG1 | 0.047 | ⚠ within organs, on part of the lines; also absent: CCDC88A, STARD9, RECK |
| [[DCLK2]] | B | HEG1 activity raises DCLK2's level | lines that do not express HEG1 (11) vs lines expressing it (39) | 4.20× lower at baseline in the lines without HEG1 | 0.051 | ⚠ within organs, on part of the lines; also absent: CCDC88A, STARD9, RECK |

## Where it sits

- **Module**: [[Module 066]] — epithelial mesenchymal transition; 74 genes; every member is in the + arm (projection on the module's main direction 0.535). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (37.3, 14.7); signed map (12.5, 38.7). **Vector** length 103, 25.5% of its response variance represented; |z| ≥ 3 in 1,226 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.9 | +6.2 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +4.7 | +6.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | +4.7 | +5.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.6 | +3.7 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | +4.4 | +5.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +4.3 | +3.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.8 | +4.6 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.0 | -3.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -2.9 | -14.4 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.5 | -3.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.5 | -1.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.4 | -2.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.4 | -4.8 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -2.1 | -1.1 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.1 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | heart development protein with EGF like domains 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q21.2 — chr3:124,965,710-125,055,997 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1237, HEG |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9ULI3](https://www.uniprot.org/uniprotkb/Q9ULI3) (Protein HEG homolog 1):

> Receptor component of the CCM signaling pathway which is a crucial regulator of heart and vessel formation and integrity. May act through the stabilization of endothelial cell junctions.

**Summary**, from NCBI Gene [57493](https://www.ncbi.nlm.nih.gov/gene/57493):

> Predicted to enable calcium ion binding activity. Involved in several processes, including negative regulation of Rho protein signal transduction; negative regulation of membrane permeability; and obsolete negative regulation of Rho-dependent protein serine/threonine kinase activity. Located in cell-cell junction. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:29227](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29227) · Entrez [57493](https://www.ncbi.nlm.nih.gov/gene/57493) · UniProt [Q9ULI3](https://www.uniprot.org/uniprotkb/Q9ULI3) · Ensembl [ENSG00000173706](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173706)

## Data

Gene col 10421: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10421); `tables/drug_effects.parquet` (64 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10421, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10421]; `tensor/DDL_lfc|DDL_z.npy` [10421]; `embed/gene_vectors.npy` [10421]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10421 or target_col == 10421). Every well: [[HEG1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HEG1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
