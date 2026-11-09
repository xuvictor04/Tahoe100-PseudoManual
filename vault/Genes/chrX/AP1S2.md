---
symbol: "AP1S2"
type: "gene"
col: 11269
ensembl_id: "ENSG00000182287"
name: "adaptor related protein complex 1 subunit sigma 2"
location: "Xp22.2"
module: 78
arm: "+"
pooled_cpm: 46.48
n_lines_expressing: 49
n_dd_up: 24
n_dd_down: 11
n_dd_up_clean: 8
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/078"]
generated_by: "tahoemap"
---

# AP1S2

*adaptor related protein complex 1 subunit sigma 2* — Xp22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (16 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.62× (z +16.5, q 0e+00, up in 44 of 45 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.52× (z +10.2, q 2e-22, up in 36 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Trametinib (drug)]] 5 µM: 0.692× (z -6.4, q 9e-08, down in 27 of 47 measured lines) ⚠ cell-cycle shift, explains ~25% of this change. The strongest without an alert is [[PH-797804 (drug)]] 5 µM: 0.579× (z -4.9, q 3e-04, down in 21 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SEPTIN10]] (+0.59, fdr 1e-05), [[PPFIBP1]] (+0.56, fdr 3e-05), [[RGS17]] (+0.56, fdr 1e-05); moves opposite to [[SART3]] (-0.57, fdr 2e-05), [[COASY]] (-0.57, fdr 2e-05), [[KEAP1]] (-0.56, fdr 3e-05).
> It is in [[Module 078]], a single-armed module (apical junction).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 17 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11269.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **2.62×** | +16.5 | 0e+00 | 44/45 (C32, SK-MEL-2, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **2.56×** | +15.5 | 0e+00 | 31/36 (LoVo, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.34×** | +13.5 | 4e-39 | 38/41 (SK-MEL-2, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.52×** | +10.2 | 2e-22 | 36/47 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **1.54×** | +7.4 | 2e-11 | 32/47 (RKO, SW1417, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.56×** | +7.3 | 2e-11 | 28/45 (KATO III, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.35×** | +7.3 | 3e-11 | 35/47 (NCI-H460, MIA PaCa-2, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.50×** | +6.9 | 3e-10 | 30/47 (RKO, BT-474, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.45×** | +6.4 | 1e-08 | 28/47 (SW1417, HT-29, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.45×** | +6.1 | 5e-08 | 31/47 (SK-MEL-2, A-427, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.42×** | +5.8 | 5e-07 | 25/47 (SK-MEL-2, RKO, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.38×** | +5.6 | 1e-06 | 27/47 (BT-474, RKO, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.26×** | +5.6 | 1e-06 | 24/47 (BT-474, PANC-1, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.35×** | +5.2 | 9e-06 | 26/47 (BT-474, C32, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~85% of this change | **1.23×** | +5.0 | 2e-05 | 19/47 (PANC-1, NCI-H460, …) | top dose only | composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.27×** | +4.2 | 9e-04 | 24/47 (C32, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belzutifan (drug)]] 5 µM |  | **1.55×** | +3.9 | 0.002 | 17/45 (A498, A-172, …) | top dose only | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.21×** | +3.3 | 0.027 | 15/47 (C32, Panc 03.27, …) | rises with dose | position effect removed |
| [[PF-06260933 (drug)]] 5 µM |  | **1.41×** | +3.1 | 0.055 | 8/47 (HOP62, SW480, …) | top dose only | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.29×** | +3.0 | 0.064 | 12/47 (J82, HS-578T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 2 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11269.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.692×** | -6.4 | 9e-08 | 27/47 (SNU-423, A-172, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.579×** | -4.9 | 3e-04 | 21/47 (RKO, AN3 CA, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.773×** | -4.2 | 0.004 | 24/47 (A-172, A549, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.839× | -4.1 | 0.005 | 22/47 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.795×** | -4.0 | 0.006 | 22/47 (SW480, Panc 03.27, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 0.835× | -3.9 | 0.009 | 21/47 (SW480, RKO, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.828×** | -3.8 | 0.012 | 18/47 (SW480, HEC-1-A, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.799×** | -3.7 | 0.016 | 18/46 (SNU-423, HOP62, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.808×** | -3.6 | 0.017 | 19/46 (SNU-423, Panc 03.27, …) | rises with dose |  |
| [[RMC-6236 (drug)]] 5 µM |  | **0.683×** | -3.4 | 0.037 | 17/47 (A-172, SNU-423, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.807×** | -3.4 | 0.037 | 17/47 (NCI-H1792, HOP62, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.828×** | -3.2 | 0.059 | 19/47 (Panc 03.27, SNU-423, …) | all doses, flat |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | 0.879× | -3.1 | 0.078 | 9/47 (HS-578T, Hs 766T, …) | all doses, flat |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.825×** | -3.1 | 0.078 | 18/46 (HEC-1-A, Panc 03.27, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.30 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11269. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 26.8 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +11.4) ⚠ cell-cycle shift, explains ~85% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.21× (z +10.4) | — |
| [[PANC-1 (line)]] | alt | 17.7 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +11.7) ⚠ cell-cycle shift, explains ~85% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.24× (z +10.0) | — |
| [[C32 (line)]] | wt | 132 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.91× (z +13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H2347 (line)]] | alt | 23.0 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +9.2) ⚠ cell-cycle shift, explains ~85% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.20× (z +8.5) | — |
| [[SK-MEL-2 (line)]] | alt | 169 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.90× (z +13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[SW480 (line)]] | alt | 68.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.70× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[A498 (line)]] | wt | 31.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.21× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[Hs 766T (line)]] | wt | 139 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.79× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[LoVo (line)]] | wt | 14.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.14× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[LOX-IMVI (line)]] | wt | 40.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.54× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[NCI-H2030 (line)]] | alt | 16.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.69× (z +9.0) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 75.8 | 1 (1 ⚠) | 1 | [[Digitoxin (drug)]] 5 µM 2.41× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | [[PH-797804 (drug)]] 5 µM 0.199× (z -8.6) |
| [[SNU-423 (line)]] | alt | 164 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.24× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | [[Cobimetinib (drug)]] 5 µM 0.406× (z -9.6) |
| [[SW1417 (line)]] | alt | 71.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.71× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[A-172 (line)]] | wt | 92.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.68× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[A-427 (line)]] | wt | 27.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.117× (z -13.9) ⚠ cell-cycle shift, explains ~67% of this change |
| [[A549 (line)]] | wt | 36.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.21× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[H4 (line)]] | wt | 40.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.75× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[HEC-1-A (line)]] | alt | 42.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.56× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 26.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +10.5) ⚠ cell-cycle shift, explains ~85% of this change | — |
| [[RPMI-7951 (line)]] | alt | 67.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.06× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[SNU-1 (line)]] | wt | 31.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.77× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[AN3 CA (line)]] | alt | 68.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 55.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 28.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.1 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 22.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 98.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 45.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 78.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 45.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 53.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 53.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 29.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11269), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEPTIN10]] | +0.59 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[PPFIBP1]] | +0.56 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[RGS17]] | +0.56 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[WWTR1]] | +0.56 | +0.51 / +0.46 | both halves | 2e-05 |  |
| [[HMGA1]] | +0.55 | +0.49 / +0.59 | both halves | 1e-05 | pathway: HIV Infection |
| [[ARPC2]] | +0.55 | +0.44 / +0.47 | both halves | 3e-05 |  |
| [[MMP1]] | +0.55 | +0.44 / +0.59 | both halves | 3e-05 |  |
| [[CORO2B]] | +0.55 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[TM4SF19-DYNLT2B]] | +0.54 | +0.62 / +0.43 | both halves | 3e-05 |  |
| [[NT5E]] | +0.54 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[CALM1]] | +0.54 | +0.58 / +0.49 | both halves | 1e-05 |  |
| [[TM4SF19]] | +0.54 | +0.54 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SART3]] | -0.57 | -0.47 / -0.60 | both halves | 2e-05 |  |
| [[COASY]] | -0.57 | -0.47 / -0.61 | both halves | 2e-05 |  |
| [[KEAP1]] | -0.56 | -0.46 / -0.63 | both halves | 3e-05 |  |
| [[MCRS1]] | -0.55 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[ZBTB7B]] | -0.54 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[MRPL44]] | -0.52 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[ZNF639]] | -0.51 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[ABCF3]] | -0.51 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[ZNF691]] | -0.51 | -0.36 / -0.56 | both halves | 1e-04 |  |
| [[DDX23]] | -0.51 | -0.48 / -0.55 | both halves | 2e-05 |  |
| [[CCDC51]] | -0.49 | -0.38 / -0.45 | both halves | 6e-05 |  |
| [[TRIM16]] | -0.47 | -0.46 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises AP1S2's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 1.7% of all compounds | 0.025 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[TOP2A]] | B | TOP2A activity lowers AP1S2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[GNG11]] | B | GNG11 activity raises AP1S2's level | lines that do not express GNG11 (21) vs lines expressing it (29) | 1.79× lower at baseline in the lines without GNG11 | 0.076 | ⚠ within organs, on part of the lines; also absent: LOXL2, SLC8A1, NALCN |
| [[MAP2K2]] | B | MAP2K2 activity raises AP1S2's level | compounds that target MAP2K2: 2 of 2 lower it (Binimetinib, Trametinib) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[LINC02454]] | B | LINC02454 activity raises AP1S2's level | lines that do not express LINC02454 (12) vs lines expressing it (38) | 1.79× lower at baseline in the lines without LINC02454 | 0.092 | ⚠ within organs, on part of the lines; also absent: PAPLN, LGALS1, SCHIP1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 078]] — apical junction; 58 genes; every member is in the + arm (projection on the module's main direction 0.535). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (50.0, 2.5); signed map (4.7, 48.8). **Vector** length 92.2, 22.0% of its response variance represented; |z| ≥ 3 in 1,017 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.3 | +7.3 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | +3.6 | +5.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | +3.5 | +6.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.4 | +4.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +2.8 | +6.1 |
|  | [[BAY1125976 (drug)]] 5 µM |  | +2.4 | +0.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.8 | +3.1 |
|  | [[Afatinib (drug)]] 0.5 µM |  | +1.7 | +0.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.5 | +1.4 |
| fall | [[PH-797804 (drug)]] 5 µM |  | -3.9 | -4.9 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -3.9 | -0.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -3.9 | -4.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.7 | -3.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.7 | -4.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.3 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | adaptor related protein complex 1 subunit sigma 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp22.2 — chrX:15,825,806-15,854,931 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SIGMA1B; previously MRX59, MRXS5, PGS |
| Gene groups (HGNC) | Adaptor related protein complex 1 |
| Reactome | 13 pathways, smallest: Nef mediated downregulation of MHC class I complex cell surface expression; Nef-mediates down modulation of cell surface receptors by recruiting them to clathrin adapters; The role of Nef in HIV-1 replication and disease pathogenesis |
| Matched by | ensembl_id |

**Function**, from UniProt [P56377](https://www.uniprot.org/uniprotkb/P56377) (AP-1 complex subunit sigma-2):

> Subunit of clathrin-associated adaptor protein complex 1 that plays a role in protein sorting in the late-Golgi/trans-Golgi network (TGN) and/or endosomes. The AP complexes mediate both the recruitment of clathrin to membranes and the recognition of sorting signals within the cytosolic tails of transmembrane cargo molecules.

**Summary**, from NCBI Gene [8905](https://www.ncbi.nlm.nih.gov/gene/8905):

> Adaptor protein complex 1 is found at the cytoplasmic face of coated vesicles located at the Golgi complex, where it mediates both the recruitment of clathrin to the membrane and the recognition of sorting signals within the cytosolic tails of transmembrane receptors. This complex is a heterotetramer composed of two large, one medium, and one small adaptin subunit. The protein encoded by this gene serves as the small subunit of this complex and is a member of the adaptin protein family. …

**Accessions** — [HGNC:560](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:560) · Entrez [8905](https://www.ncbi.nlm.nih.gov/gene/8905) · UniProt [P56377](https://www.uniprot.org/uniprotkb/P56377) · Ensembl [ENSG00000182287](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182287)

## Data

Gene col 11269: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11269); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11269, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11269]; `tensor/DDL_lfc|DDL_z.npy` [11269]; `embed/gene_vectors.npy` [11269]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11269 or target_col == 11269). Every well: [[AP1S2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AP1S2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
