---
symbol: "PGAP1"
type: "gene"
col: 12346
ensembl_id: "ENSG00000197121"
name: "post-GPI attachment to proteins inositol deacylase 1"
location: "2q33.1"
module: 65
arm: "+"
pooled_cpm: 89.31
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 13
n_dd_up_clean: 9
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/065"]
generated_by: "tahoemap"
---

# PGAP1

*post-GPI attachment to proteins inositol deacylase 1* — 2q33.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 1.73× (z +10.9, q 2e-25, up in 35 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.583× (z -10.7, q 4e-24, down in 38 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.636× (z -9.0, q 6e-17, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SCPEP1]] (+0.65, fdr 8e-06), [[KCTD6]] (+0.65, fdr 7e-06), [[CAT]] (+0.65, fdr 1e-05); moves opposite to [[LTO1]] (-0.63, fdr 3e-05), [[ANKLE2]] (-0.62, fdr 1e-05), [[SMIM12]] (-0.61, fdr 3e-05).
> It sits in the **+** arm of [[Module 065]] (BBSome-mediated cargo-targeting to cilium).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[SLC2A9]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 8 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12346.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **1.73×** | +10.9 | 2e-25 | 35/48 (J82, SW1417, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.73×** | +10.9 | 2e-25 | 32/48 (J82, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.40×** | +9.5 | 4e-19 | 37/48 (SW1417, J82, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.52×** | +8.3 | 1e-14 | 33/48 (J82, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.47×** | +7.6 | 3e-12 | 35/49 (SW1417, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.42×** | +6.9 | 4e-10 | 31/48 (J82, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.38×** | +6.4 | 1e-08 | 30/48 (J82, PANC-1, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.82×** | +6.2 | 3e-08 | 33/49 (SW1417, J82, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.27×** | +4.8 | 1e-04 | 23/48 (RPMI-7951, SW480, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.25×** | +4.4 | 6e-04 | 24/48 (A498, RKO, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **1.24×** | +4.3 | 1e-03 | 23/48 (LoVo, J82, …) | rises with dose |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | 1.16× | +4.2 | 0.001 | 13/48 (A498, SW 900, …) | rises with dose | position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.48×** | +4.1 | 0.002 | 20/45 (SNU-1, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~20% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | 1.20× | +3.4 | 0.032 | 19/48 (PANC-1, J82, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.3 | 0.039 | 19/48 (SW480, BT-474, …) | top dose only | composition shift |
| [[Dimethyl fumarate (drug)]] 5 µM |  | 1.17× | +3.1 | 0.076 | 9/49 (MIA PaCa-2, Hs 766T, …) | top dose only | plate-row cell shift |
| [[Verteporfin (drug)]] 5 µM |  | 1.17× | +3.0 | 0.077 | 17/49 (A498, A-427, …) | top dose only |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.34×** | +3.0 | 0.077 | 18/49 (PANC-1, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **1.34×** | +3.0 | 0.078 | 14/47 (NCI-H23, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.05 µM |  | 1.16× | +3.0 | 0.078 | 10/48 (CFPAC-1, Panc 03.27, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 10 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12346.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.583×** | -10.7 | 4e-24 | 38/49 (NCI-H460, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.636×** | -9.0 | 6e-17 | 41/48 (SW480, MIA PaCa-2, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.643×** | -8.5 | 5e-15 | 33/44 (C-33 A, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.675×** | -7.2 | 7e-11 | 31/45 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.721×** | -6.5 | 8e-09 | 32/48 (C32, MIA PaCa-2, …) | all doses, flat |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~23% of this change | **0.755×** | -5.6 | 2e-06 | 27/48 (NCI-H661, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.760×** | -5.5 | 4e-06 | 29/47 (MIA PaCa-2, NCI-H460, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | 0.840× | -4.9 | 6e-05 | 24/48 (A-172, NCI-H1792, …) | all doses, flat | composition shift |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.782×** | -4.9 | 6e-05 | 27/47 (C32, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.799×** | -4.3 | 9e-04 | 26/47 (A-172, SNU-423, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **0.810×** | -4.2 | 0.001 | 22/48 (A-172, NCI-H2030, …) | all doses, flat |  |
| [[vincristine (drug)]] 5 µM |  | **0.695×** | -3.8 | 0.007 | 24/46 (A-172, RPMI-7951, …) | rises with dose | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **0.828×** | -3.8 | 0.007 | 21/48 (MIA PaCa-2, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.885× | -3.5 | 0.022 | 12/49 (C32, MIA PaCa-2, …) | rises with dose |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.722×** | -3.4 | 0.025 | 18/49 (A549, RPMI-7951, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.844× | -3.4 | 0.025 | 20/48 (A-172, MIA PaCa-2, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.05 µM |  | 0.838× | -3.3 | 0.034 | 14/48 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.849× | -3.3 | 0.034 | 14/48 (NCI-H460, MIA PaCa-2, …) | top dose only |  |
| [[Lactate (calcium) (drug)]] 5 µM |  | 0.860× | -3.0 | 0.065 | 10/48 (NCI-H1573, NCI-H1792, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.900× | -3.0 | 0.067 | 14/48 (NCI-H661, SHP-77, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.852× | -3.0 | 0.074 | 15/47 (MIA PaCa-2, J82, …) | all doses, flat | low cells (technical?) |
| [[Filgotinib (drug)]] 5 µM |  | 0.865× | -2.9 | 0.086 | 11/48 (NCI-H2347, HEC-1-A, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12346. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 69.6 | 2 (1 ⚠) | 4 (4 ⚠) | [[PH-797804 (drug)]] 5 µM 5.38× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.351× (z -15.2) ⚠ cell-cycle shift, explains ~68% of this change |
| [[NCI-H2030 (line)]] | alt | 80.5 | 2 (1 ⚠) | 4 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 2.24× (z +10.0) | [[Homoharringtonine (drug)]] 5 µM 0.510× (z -11.9) ⚠ cell-cycle shift, explains ~68% of this change |
| [[SW1417 (line)]] | alt | 35.9 | 6 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 2.30× (z +10.1) | — |
| [[A498 (line)]] | wt | 76.4 | 4 (4 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 7.70× (z +13.4) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 0.5 µM 0.503× (z -8.6) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 31.1 | 5 (1 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 4.21× (z +12.6) | — |
| [[C32 (line)]] | wt | 173 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.05 µM 0.341× (z -11.5) |
| [[NCI-H2347 (line)]] | alt | 80.5 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.282× (z -13.8) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 223 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.261× (z -17.3) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 99.5 | 2 (2 ⚠) | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.86× (z +9.9) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.376× (z -14.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.547× (z -9.7) |
| [[C-33 A (line)]] | alt | 281 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.262× (z -13.0) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 212 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.454× (z -11.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.389× (z -9.6) |
| [[NCI-H661 (line)]] | alt | 927 | 0 | 3 (3 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.285× (z -9.4) ⚠ transcription drop; cell-cycle shift, explains ~23% of this change |
| [[LoVo (line)]] | wt | 45.5 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 1.99× (z +9.5) | — |
| [[NCI-H1573 (line)]] | alt | 58.1 | 2 | 0 | [[Belinostat (drug)]] 5 µM 2.44× (z +8.5) | — |
| [[AN3 CA (line)]] | alt | 116 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -12.5) ⚠ cell-cycle shift, explains ~68% of this change |
| [[AsPC-1 (line)]] | alt | 92.8 | 1 | 0 | [[Radotinib (drug)]] 5 µM 2.05× (z +8.7) | — |
| [[BT-474 (line)]] | alt | 26.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.93× (z +11.7) ⚠ cell-cycle shift, explains ~68% of this change | — |
| [[CFPAC-1 (line)]] | alt | 49.3 | 0 | 1 (1 ⚠) | — | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.127× (z -10.3) ⚠ toxic |
| [[HEC-1-A (line)]] | alt | 52.8 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 1.88× (z +8.5) | — |
| [[HT-29 (line)]] | alt | 42.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +9.9) ⚠ cell-cycle shift, explains ~68% of this change | — |
| [[LOX-IMVI (line)]] | wt | 65.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.425× (z -8.5) ⚠ cell-cycle shift, explains ~52% of this change |
| [[LS 180 (line)]] | wt | 98.8 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.431× (z -8.6) |
| [[NCI-H1792 (line)]] | alt | 82.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.408× (z -13.4) ⚠ cell-cycle shift, explains ~68% of this change |
| [[Panc 03.27 (line)]] | alt | 39.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.321× (z -8.6) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 87.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.469× (z -9.6) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 91.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.298× (z -12.8) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 231 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.360× (z -10.7) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 64.7 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.49× (z +8.7) | — |
| [[SNU-1 (line)]] | wt | 90.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.258× (z -9.6) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 72.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.342× (z -10.5) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 87.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.307× (z -9.3) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 68.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 87.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 129 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 72.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 99.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 43.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 50.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 88.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 53.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 81.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 86.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 78.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 87.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 63.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 61.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 89.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12346), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*53 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SCPEP1]] | +0.65 | +0.57 / +0.69 | both halves | 8e-06 |  |
| [[KCTD6]] | +0.65 | +0.58 / +0.66 | both halves | 7e-06 |  |
| [[CAT]] | +0.65 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[VDAC3]] | +0.64 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[HACE1]] | +0.64 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[PDK3]] | +0.63 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[FAM168A]] | +0.62 | +0.58 / +0.58 | both halves | 8e-06 |  |
| [[FAM102B]] | +0.62 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[ARL6]] | +0.62 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[PDE7A]] | +0.60 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[BCL9]] | +0.60 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[FRRS1]] | +0.60 | +0.50 / +0.64 | both halves | 1e-05 |  |

## Genes that move opposite

*47 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LTO1]] | -0.63 | -0.62 / -0.45 | both halves | 3e-05 |  |
| [[ANKLE2]] | -0.62 | -0.51 / -0.60 | both halves | 1e-05 |  |
| [[SMIM12]] | -0.61 | -0.71 / -0.45 | both halves | 3e-05 |  |
| [[EXOSC6]] | -0.61 | -0.59 / -0.48 | both halves | 2e-05 |  |
| [[MAEA]] | -0.60 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[REXO1]] | -0.59 | -0.60 / -0.49 | both halves | 1e-05 |  |
| [[MYH3]] | -0.59 | -0.61 / -0.47 | both halves | 2e-05 |  |
| [[CYREN]] | -0.58 | -0.59 / -0.40 | both halves | 5e-05 |  |
| [[SMIM15-AS1]] | -0.57 | -0.59 / -0.44 | both halves | 3e-05 |  |
| [[MIS12]] | -0.57 | -0.59 / -0.39 | both halves | 6e-05 |  |
| [[DPH5-DT]] | -0.57 | -0.51 / -0.46 | both halves | 3e-05 |  |
| [[MGLL]] | -0.57 | -0.49 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC2A9]] | B | SLC2A9 activity lowers PGAP1's level | lines that do not express SLC2A9 (6) vs lines expressing it (44) | 1.81× higher at baseline in the lines without SLC2A9 | 0.017 | ⚠ within organs, on part of the lines; also absent: VDR, SEMA4G, TBC1D8B; maybe low, not absent |
| [[MGLL]] | B | MGLL activity lowers PGAP1's level | lines that do not express MGLL (14) vs lines expressing it (36) | 2.00× higher at baseline in the lines without MGLL | 0.044 | ⚠ within organs, on part of the lines; also absent: CXCL3, MET, PSORS1C1; maybe low, not absent |
| [[NUP62CL]] | B | NUP62CL activity lowers PGAP1's level | lines that do not express NUP62CL (19) vs lines expressing it (31) | 1.40× higher at baseline in the lines without NUP62CL | 0.060 | ⚠ within organs, on part of the lines; also absent: LINC01589, ABCC3, GOLT1A |
| [[SLC18B1]] | B | SLC18B1 activity lowers PGAP1's level | lines that do not express SLC18B1 (5) vs lines expressing it (45) | 1.79× higher at baseline in the lines without SLC18B1 | 0.089 | ⚠ within organs, on part of the lines; co-absent genes; also absent: FHIP1A, NIPAL1, RALGPS2; its own permutation p |
| [[SFMBT2]] | B | SFMBT2 activity raises PGAP1's level | lines that do not express SFMBT2 (19) vs lines expressing it (31) | 1.03× lower at baseline in the lines without SFMBT2 | 0.089 | ⚠ within organs, on part of the lines; also absent: ANKRD6, LONRF2, GHR |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 065]] — BBSome-mediated cargo-targeting to cilium; 76 genes; this gene is in the **+** arm (projection on the module's main direction 0.648). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (3.4, -9.7); signed map (-31.9, -7.2). **Vector** length 119, 34.6% of its response variance represented; |z| ≥ 3 in 1,217 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.2 | +9.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.4 | +7.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +5.5 | +8.3 |
|  | [[NG25 (drug)]] 5 µM |  | +4.4 | +3.0 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | +4.2 | +4.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.6 | +6.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +3.0 | +3.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.9 | +4.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.9 | +2.6 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | -7.8 | -3.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -7.5 | -9.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.9 | -6.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | -5.8 | -4.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -5.2 | -3.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.8 | -3.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -4.6 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | post-GPI attachment to proteins inositol deacylase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q33.1 — chr2:196,833,004-196,927,796 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ12377, Bst1, SPG67 |
| Reactome | 2 pathways, smallest: Attachment of GPI anchor to uPAR; Post-translational modification: synthesis of GPI-anchored proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q75T13](https://www.uniprot.org/uniprotkb/Q75T13) (GPI inositol-deacylase):

> GPI inositol-deacylase that catalyzes the remove of the acyl chain linked to the 2-OH position of inositol ring from the GPI-anchored protein (GPI-AP) in the endoplasmic reticulum. Initiates the post-attachment remodeling phase of GPI-AP biogenesis and participates in endoplasmic reticulum (ER)-to-Golgi transport of GPI-anchored protein.

**Summary**, from NCBI Gene [80055](https://www.ncbi.nlm.nih.gov/gene/80055):

> The protein encoded by this gene functions early in the glycosylphosphatidylinositol (GPI) biosynthetic pathway, catalyzing the inositol deacylation of GPI. The encoded protein is required for the production of GPI that can attach to proteins, and this may be an important factor in the transport of GPI-anchored proteins from the endoplasmic reticulum to the Golgi. Defects in this gene are a cause an autosomal recessive form of cognitive impairment. [provided by RefSeq, Jul 2017]

**Accessions** — [HGNC:25712](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25712) · Entrez [80055](https://www.ncbi.nlm.nih.gov/gene/80055) · UniProt [Q75T13](https://www.uniprot.org/uniprotkb/Q75T13) · Ensembl [ENSG00000197121](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197121)

## Data

Gene col 12346: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12346); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12346, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12346]; `tensor/DDL_lfc|DDL_z.npy` [12346]; `embed/gene_vectors.npy` [12346]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12346 or target_col == 12346). Every well: [[PGAP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PGAP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
