---
symbol: "STK17A"
type: "gene"
col: 8961
ensembl_id: "ENSG00000164543"
name: "serine/threonine kinase 17a"
location: "7p13"
module: 81
arm: "+"
pooled_cpm: 141.49
n_lines_expressing: 48
n_dd_up: 17
n_dd_down: 13
n_dd_up_clean: 16
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 10
direction_downstream: 0
tags: ["gene", "module/081"]
generated_by: "tahoemap"
---

# STK17A

*serine/threonine kinase 17a* — 7p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.63× (z +17.2, q 0e+00, up in 32 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.588× (z -18.8, q 0e+00, down in 34 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC25A51]] (+0.65, fdr 1e-05), [[HBEGF]] (+0.62, fdr 7e-06), [[EXT1]] (+0.62, fdr 7e-06); moves opposite to [[FOXJ2]] (-0.57, fdr 4e-05), [[SLC43A1]] (-0.55, fdr 1e-05), [[RBBP4]] (-0.55, fdr 2e-05).
> It is in [[Module 081]], a single-armed module (KRAS signaling up).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[SMOX]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8961.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.63×** | +17.2 | 0e+00 | 32/46 (Panc 03.27, SW1417, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.65×** | +11.9 | 5e-30 | 36/46 (KATO III, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.58×** | +11.4 | 8e-28 | 36/46 (KATO III, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.58×** | +11.4 | 8e-28 | 37/46 (SW1417, A-427, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.58×** | +11.4 | 8e-28 | 32/46 (SW1417, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.58×** | +11.0 | 4e-26 | 37/46 (Panc 03.27, SW 900, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.45×** | +9.3 | 1e-18 | 31/46 (KATO III, HT-29, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.42×** | +8.8 | 7e-17 | 30/46 (SW1417, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.27×** | +8.5 | 9e-16 | 24/46 (SW1417, SW480, …) | rises with dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.32×** | +6.9 | 2e-10 | 25/46 (HT-29, SW1417, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.56×** | +5.8 | 3e-07 | 26/46 (MIA PaCa-2, NCI-H2030, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.26×** | +5.7 | 6e-07 | 20/47 (SW1417, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.52×** | +5.5 | 2e-06 | 21/43 (AsPC-1, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.50×** | +5.3 | 4e-06 | 21/47 (MIA PaCa-2, Hs 766T, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.31×** | +4.8 | 5e-05 | 18/47 (KATO III, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.20×** | +4.3 | 6e-04 | 19/45 (SW48, A-172, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8961.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.588×** | -18.8 | 0e+00 | 34/47 (NCI-H2030, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.551×** | -14.3 | 4e-44 | 30/41 (SK-MEL-2, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.602×** | -12.7 | 2e-34 | 32/47 (H4, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.619×** | -11.1 | 3e-26 | 33/43 (NCI-H2030, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **0.654×** | -10.6 | 4e-24 | 37/46 (PANC-1, HS-578T, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.745×** | -7.1 | 1e-10 | 27/48 (SW 1271, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.747×** | -7.0 | 2e-10 | 26/46 (HOP62, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Radotinib (drug)]] 5 µM |  | **0.829×** | -6.6 | 3e-09 | 20/46 (C32, AsPC-1, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM |  | **0.642×** | -5.8 | 5e-07 | 23/45 (MIA PaCa-2, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.794×** | -5.6 | 2e-06 | 23/46 (C32, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.814×** | -5.1 | 1e-05 | 24/46 (BT-474, KATO III, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.833×** | -4.6 | 2e-04 | 23/46 (HS-578T, A498, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.836× | -4.5 | 3e-04 | 19/46 (A498, HS-578T, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 0.837× | -4.4 | 3e-04 | 20/46 (A498, HS-578T, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 5 µM |  | 0.882× | -4.4 | 3e-04 | 15/46 (A498, HOP62, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.882× | -4.4 | 4e-04 | 15/46 (C32, MIA PaCa-2, …) | all doses, flat |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | 0.836× | -4.2 | 7e-04 | 19/46 (C32, MIA PaCa-2, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.835× | -4.2 | 8e-04 | 21/46 (MIA PaCa-2, BT-474, …) | all doses, stronger at high dose |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 0.848× | -4.1 | 0.001 | 16/46 (PANC-1, NCI-H1573, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8961. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 330 | 1 | 10 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +12.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.372× (z -19.6) |
| [[MIA PaCa-2 (line)]] | alt | 229 | 2 | 8 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 13.2× (z +13.9) | [[Adagrasib (drug)]] 0.05 µM 0.606× (z -18.8) ⚠ position not correctable · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.393× (z -13.8) |
| [[KATO III (line)]] | alt | 121 | 8 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 3.96× (z +13.6) | [[Dinaciclib (drug)]] 0.05 µM 0.385× (z -8.8) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 106 | 7 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +14.6) | [[Dinaciclib (drug)]] 5 µM 0.343× (z -10.1) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 140 | 1 | 7 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +10.1) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.287× (z -11.9) |
| [[HT-29 (line)]] | alt | 78.5 | 8 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.63× (z +17.3) | — |
| [[SW1417 (line)]] | alt | 87.0 | 8 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.61× (z +19.2) | — |
| [[HOP62 (line)]] | alt | 154 | 1 | 6 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.65× (z +9.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.361× (z -18.6) |
| [[SW 900 (line)]] | alt | 121 | 5 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +14.6) | [[Dinaciclib (drug)]] 0.5 µM 0.316× (z -14.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.527× (z -11.3) |
| [[HepG2_C3A (line)]] | wt | 345 | 0 | 6 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.337× (z -14.3) |
| [[BT-474 (line)]] | alt | 143 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.200× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.258× (z -10.4) |
| [[HS-578T (line)]] | alt | 180 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.302× (z -20.7) |
| [[NCI-H2347 (line)]] | alt | 128 | 1 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +10.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.432× (z -13.9) |
| [[PANC-1 (line)]] | alt | 146 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.408× (z -15.6) |
| [[A-427 (line)]] | wt | 48.0 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.12× (z +11.8) | — |
| [[NCI-H2030 (line)]] | alt | 235 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.358× (z -21.2) |
| [[NCI-H460 (line)]] | wt | 155 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +11.9) | [[Dinaciclib (drug)]] 0.5 µM 0.501× (z -9.0) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 84.1 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.16× (z +20.3) | — |
| [[SK-MEL-2 (line)]] | alt | 164 | 2 | 2 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.31× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.207× (z -20.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.613× (z -9.1) |
| [[CFPAC-1 (line)]] | alt | 181 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.426× (z -13.7) |
| [[HEC-1-A (line)]] | alt | 42.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +12.1) | — |
| [[LoVo (line)]] | wt | 157 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +18.5) | — |
| [[RKO (line)]] | wt | 117 | 1 (1 ⚠) | 2 (1 ⚠) | [[Topotecan (hydrochloride) (drug)]] 5 µM 2.64× (z +10.2) ⚠ toxic; cell-cycle shift, explains ~16% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.295× (z -12.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.549× (z -9.3) |
| [[H4 (line)]] | wt | 395 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.166× (z -16.8) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 152 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 14.0× (z +13.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.448× (z -11.3) |
| [[SW 1088 (line)]] | alt | 318 | 0 | 2 | — | [[Flumatinib (mesylate) (drug)]] 0.05 µM 0.122× (z -9.9) |
| [[SW 1271 (line)]] | alt | 90.0 | 0 | 2 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0457× (z -12.6) |
| [[SW480 (line)]] | alt | 130 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +12.0) | — |
| [[AN3 CA (line)]] | alt | 66.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +8.5) | — |
| [[J82 (line)]] | alt | 99.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.556× (z -9.4) |
| [[LOX-IMVI (line)]] | wt | 140 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.416× (z -10.2) |
| [[NCI-H1573 (line)]] | alt | 90.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.435× (z -9.9) |
| [[NCI-H1792 (line)]] | alt | 166 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.403× (z -13.6) |
| [[RPMI-7951 (line)]] | alt | 144 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.441× (z -11.7) |
| [[SNU-423 (line)]] | alt | 194 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.323× (z -12.9) |
| [[SW48 (line)]] | wt | 91.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.232× (z -10.7) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 131 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 143 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 34.4 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 144 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 26.0 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 56.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 108 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 130 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 186 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 52.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 53.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 85.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 39.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8961), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC25A51]] | +0.65 | +0.66 / +0.53 | both halves | 1e-05 |  |
| [[HBEGF]] | +0.62 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[EXT1]] | +0.62 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[TRIB1]] | +0.57 | +0.45 / +0.61 | both halves | 3e-05 |  |
| [[ITGA2]] | +0.57 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[EFL1]] | +0.56 | +0.56 / +0.44 | both halves | 3e-05 |  |
| [[NABP1]] | +0.56 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[ZSWIM6]] | +0.55 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[DUSP6]] | +0.55 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[MYO10]] | +0.54 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[AADACP1]] | +0.53 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[MARCHF3]] | +0.53 | +0.45 / +0.52 | both halves | 3e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FOXJ2]] | -0.57 | -0.56 / -0.42 | both halves | 4e-05 |  |
| [[SLC43A1]] | -0.55 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[RBBP4]] | -0.55 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[SLC16A4-AS1]] | -0.55 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[GARS1-DT]] | -0.54 | -0.46 / -0.47 | both halves | 3e-05 |  |
| [[LAMTOR5-AS1]] | -0.53 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[MIRLET7BHG]] | -0.53 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[ATL2]] | -0.51 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[EIF2D]] | -0.51 | -0.39 / -0.46 | both halves | 6e-05 |  |
| [[NNT]] | -0.50 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[CIAO2A]] | -0.50 | -0.47 / -0.38 | both halves | 6e-05 |  |
| [[ERBB2]] | -0.49 | -0.43 / -0.47 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 8, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SMOX]] | B | SMOX activity raises STK17A's level | lines that do not express SMOX (6) vs lines expressing it (44) | 2.62× lower at baseline in the lines without SMOX | 0.011 | ⚠ within organs, on part of the lines; also absent: NIBAN2, NDRG1, TRIM38; maybe low, not absent |
| [[DUSP5]] | B | DUSP5 activity raises STK17A's level | lines that do not express DUSP5 (7) vs lines expressing it (43) | 1.89× lower at baseline in the lines without DUSP5 | 0.032 | ⚠ within organs, on part of the lines; also absent: ENSG00000236213, CA13, SLC2A1; maybe low, not absent |
| [[MYO1E]] | B | MYO1E activity raises STK17A's level | lines that do not express MYO1E (5) vs lines expressing it (45) | 2.10× lower at baseline in the lines without MYO1E | 0.036 | ⚠ within organs, on part of the lines; also absent: FLNB, SMOX, TRIM38; maybe low, not absent |
| [[FAM107B]] | B | FAM107B activity raises STK17A's level | lines that do not express FAM107B (11) vs lines expressing it (39) | 1.70× lower at baseline in the lines without FAM107B | 0.067 | ⚠ within organs, on part of the lines; also absent: KIAA1217, ETS2, NRP1 |
| [[TOP2A]] | B | TOP2A activity raises STK17A's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[AADAC]] | B | AADAC activity raises STK17A's level | lines that do not express AADAC (34) vs lines expressing it (16) | 1.69× lower at baseline in the lines without AADAC | 0.078 | ⚠ within organs, on part of the lines; also absent: AADACP1, SUCNR1, LINC01610 |
| [[SHB]] | B | SHB activity raises STK17A's level | lines that do not express SHB (5) vs lines expressing it (45) | 2.32× lower at baseline in the lines without SHB | 0.089 | ⚠ within organs, on part of the lines; also absent: SLC2A1, NIBAN2, IER3; maybe low, not absent; its own permutation p |
| [[ABL1]] | B | ABL1 activity raises STK17A's level | compounds that target ABL1: 3 of 6 lower it (NG25, Ponatinib, Radotinib) | 50% of the class's compounds vs 2.8% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[HBEGF]] | C | HBEGF activity raises STK17A's level | lines that do not express HBEGF (3) vs lines expressing it (47) | 2.99× lower at baseline in the lines without HBEGF | 0.036 | ⚠ few lines (3 vs 47); across organs; also absent: FUCA2, AIFM2, TRAF3IP2; maybe low, not absent |
| [[CIB1]] | C | CIB1 activity raises STK17A's level | lines that do not express CIB1 (4) vs lines expressing it (46) | 2.94× lower at baseline in the lines without CIB1 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: SHB, NIBAN2, IER3; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 081]] — KRAS signaling up; 55 genes; every member is in the + arm (projection on the module's main direction 0.621). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (48.6, 3.9); signed map (3.7, 45.7). **Vector** length 136, 42.9% of its response variance represented; |z| ≥ 3 in 1,670 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.5 | +8.5 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +5.8 | +11.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.8 | +11.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.5 | +8.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.4 | +9.3 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +3.5 | +3.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.3 | +4.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.4 | +1.0 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.9 | -18.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | -7.5 | -10.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -5.6 | -12.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.6 | -14.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.2 | -7.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -4.7 | -4.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -4.6 | -3.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -4.1 | -3.5 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -4.0 | -4.4 |

## What is on record

|  |  |
|---|---|
| Name | serine/threonine kinase 17a |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p13 — chr7:43,582,758-43,650,713 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DRAK1 |
| Gene groups (HGNC) | Death associated protein kinases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UEE5](https://www.uniprot.org/uniprotkb/Q9UEE5) (Serine/threonine-protein kinase 17A):

> Acts as a positive regulator of apoptosis. Also acts as a regulator of cellular reactive oxygen species.

**Summary**, from NCBI Gene [9263](https://www.ncbi.nlm.nih.gov/gene/9263):

> This gene is a member of the DAP kinase-related apoptosis-inducing protein kinase family and encodes an autophosphorylated nuclear protein with a protein kinase domain. The protein has apoptosis-inducing activity. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:11395](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11395) · Entrez [9263](https://www.ncbi.nlm.nih.gov/gene/9263) · UniProt [Q9UEE5](https://www.uniprot.org/uniprotkb/Q9UEE5) · Ensembl [ENSG00000164543](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164543)

## Data

Gene col 8961: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8961); `tables/drug_effects.parquet` (59 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8961, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8961]; `tensor/DDL_lfc|DDL_z.npy` [8961]; `embed/gene_vectors.npy` [8961]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8961 or target_col == 8961). Every well: [[STK17A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STK17A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
