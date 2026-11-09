---
symbol: "C1RL"
type: "gene"
col: 6272
ensembl_id: "ENSG00000139178"
name: "complement C1r subcomponent like"
location: "12p13.31"
module: 139
arm: "+"
pooled_cpm: 29.39
n_lines_expressing: 47
n_dd_up: 20
n_dd_down: 41
n_dd_up_clean: 19
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 4
direction_downstream: 6
tags: ["gene", "module/139"]
generated_by: "tahoemap"
---

# C1RL

*complement C1r subcomponent like* — 12p13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (1 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 5 µM: 1.69× (z +6.0, q 9e-07, up in 33 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 41 drug-doses (23 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.385× (z -16.1, q 0e+00, down in 39 of 44 measured lines) ⚠ cell-cycle shift, explains ~43% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.474× (z -8.9, q 4e-17, down in 39 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SOD2]] (+0.71, fdr 7e-06), [[SAA2-SAA4]] (+0.67, fdr 7e-06), [[MR1]] (+0.66, fdr 1e-05); moves opposite to [[RASA3]] (-0.60, fdr 4e-05), [[GRK5]] (-0.56, fdr 3e-05), [[C13orf46]] (-0.56, fdr 4e-05).
> It is in [[Module 139]], a single-armed module (Interleukin-4 and Interleukin-13 signaling).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[C1RL-AS1]] → it (grade B ⚠); 6 go from it, the strongest it → [[TNFRSF1A]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6272.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **1.69×** | +6.0 | 9e-07 | 33/43 (MIA PaCa-2, SW 900, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.49×** | +5.5 | 1e-05 | 27/45 (MIA PaCa-2, SW 900, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.56×** | +5.4 | 1e-05 | 30/45 (MIA PaCa-2, SW 900, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.38×** | +5.4 | 1e-05 | 24/45 (MIA PaCa-2, SW 900, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.59×** | +5.3 | 1e-05 | 30/44 (MIA PaCa-2, SW 900, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.53×** | +4.7 | 2e-04 | 25/45 (MIA PaCa-2, SW 900, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.46×** | +4.5 | 5e-04 | 26/44 (MIA PaCa-2, SW 900, …) | rises with dose |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.46×** | +4.3 | 0.001 | 22/44 (MIA PaCa-2, Hs 766T, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.43×** | +4.3 | 0.001 | 21/45 (A498, HOP62, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.44×** | +4.1 | 0.002 | 21/45 (MIA PaCa-2, HepG2/C3A, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.30×** | +3.8 | 0.007 | 20/45 (MIA PaCa-2, Hs 766T, …) | all doses, flat | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **1.84×** | +3.8 | 0.007 | 25/44 (MIA PaCa-2, NCI-H23, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.25×** | +3.8 | 0.007 | 17/45 (SW480, A-427, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.37×** | +3.7 | 0.007 | 22/45 (MIA PaCa-2, BT-474, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.38×** | +3.7 | 0.007 | 22/45 (Hs 766T, HOP62, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **1.34×** | +3.5 | 0.018 | 17/45 (HOP62, A498, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 41 in all, 23 with an alert ⚠; shown: the 15 strongest and the 11 next strongest without an alert. 41 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 23 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6272.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.385×** | -16.1 | 0e+00 | 39/44 (COLO 205, NCI-H1573, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.269×** | -15.7 | 0e+00 | 44/45 (NCI-H23, A-427, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.281×** | -14.7 | 0e+00 | 43/45 (NCI-H23, A-427, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.313×** | -13.9 | 1e-41 | 43/45 (A-427, NCI-H23, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **0.448×** | -9.6 | 1e-19 | 35/44 (NCI-H1792, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.474×** | -8.9 | 4e-17 | 39/45 (A549, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.484×** | -8.7 | 3e-16 | 39/45 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~41% of this change | **0.483×** | -8.4 | 5e-15 | 34/42 (H4, COLO 205, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.484×** | -8.3 | 5e-15 | 38/44 (COLO 205, NCI-H1573, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.510×** | -8.0 | 5e-14 | 31/44 (NCI-H1573, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.315×** | -7.2 | 3e-11 | 30/45 (NCI-H23, HCT15, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.558×** | -6.8 | 7e-10 | 37/45 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.556×** | -6.6 | 2e-09 | 32/44 (A549, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.597×** | -6.0 | 1e-07 | 31/45 (PANC-1, NCI-H23, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.617×** | -5.6 | 9e-07 | 28/45 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.430×** | -5.3 | 4e-06 | 28/44 (MIA PaCa-2, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.660×** | -5.0 | 2e-05 | 20/45 (PANC-1, NCI-H23, …) | rises with dose |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.692×** | -4.4 | 3e-04 | 24/45 (SK-MEL-2, A498, …) | two highest doses |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.701×** | -4.1 | 0.001 | 19/44 (NCI-H23, NCI-H1792, …) | rises with dose |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.801×** | -3.7 | 0.004 | 20/45 (Hs 766T, NCI-H1792, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.734×** | -3.7 | 0.004 | 20/44 (CFPAC-1, NCI-H23, …) | two highest doses |  |
| [[Tofacitinib (drug)]] 5 µM |  | **0.815×** | -3.5 | 0.010 | 17/45 (NCI-H1792, A498, …) | two highest doses |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.743×** | -3.4 | 0.011 | 18/45 (CFPAC-1, NCI-H1792, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.755×** | -3.4 | 0.013 | 16/45 (NCI-H2030, BT-474, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.592×** | -3.3 | 0.017 | 19/44 (HCT15, NCI-H23, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.595×** | -3.2 | 0.018 | 15/44 (NCI-H1573, NCI-H23, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.53 per unit of S-phase module lfc, -0.47 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6272. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 47.6 | 0 | 8 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -16.5) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.211× (z -12.7) |
| [[NCI-H23 (line)]] | alt | 86.2 | 0 | 8 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.110× (z -18.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 23.1 | 0 | 7 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.170× (z -11.8) ⚠ cell-cycle shift, explains ~30% of this change |
| [[COLO 205 (line)]] | alt | 43.7 | 0 | 6 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0707× (z -23.2) ⚠ cell-cycle shift, explains ~43% of this change |
| [[SW480 (line)]] | alt | 41.0 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.191× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~91% of this change |
| [[A549 (line)]] | wt | 61.2 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.159× (z -12.0) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.273× (z -8.5) |
| [[NCI-H1792 (line)]] | alt | 55.4 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.111× (z -12.6) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.153× (z -10.8) |
| [[A-427 (line)]] | wt | 70.6 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.154× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[KATO III (line)]] | alt | 26.8 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.251× (z -12.5) ⚠ cell-cycle shift, explains ~43% of this change |
| [[LoVo (line)]] | wt | 22.6 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -13.1) ⚠ cell-cycle shift, explains ~43% of this change |
| [[PANC-1 (line)]] | alt | 13.4 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -13.4) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.247× (z -9.0) |
| [[MIA PaCa-2 (line)]] | alt | 44.5 | 1 (1 ⚠) | 2 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.77× (z +11.9) ⚠ position not correctable | [[Homoharringtonine (drug)]] 5 µM 0.256× (z -11.2) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.213× (z -9.1) |
| [[Panc 03.27 (line)]] | alt | 49.6 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.291× (z -12.1) ⚠ cell-cycle shift, explains ~43% of this change |
| [[SNU-423 (line)]] | alt | 31.9 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -14.2) ⚠ cell-cycle shift, explains ~43% of this change |
| [[BT-474 (line)]] | alt | 23.1 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.206× (z -12.2) ⚠ cell-cycle shift, explains ~43% of this change |
| [[CFPAC-1 (line)]] | alt | 22.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.282× (z -10.9) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.246× (z -8.5) |
| [[HCT15 (line)]] | alt | 48.0 | 0 | 2 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.225× (z -9.7) ⚠ cell-cycle shift, explains ~33% of this change |
| [[HT-29 (line)]] | alt | 29.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -11.4) ⚠ cell-cycle shift, explains ~43% of this change |
| [[SNU-1 (line)]] | wt | 32.1 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -12.9) ⚠ cell-cycle shift, explains ~43% of this change |
| [[SW 900 (line)]] | alt | 36.4 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -12.9) ⚠ cell-cycle shift, explains ~43% of this change |
| [[A498 (line)]] | wt | 39.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.405× (z -9.3) ⚠ cell-cycle shift, explains ~43% of this change |
| [[C32 (line)]] | wt | 7.49 | 0 | 1 (1 ⚠) | — | [[Sunitinib (drug)]] 5 µM 0.0825× (z -9.0) ⚠ toxic |
| [[H4 (line)]] | wt | 48.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0800× (z -11.8) ⚠ toxic; cell-cycle shift, explains ~41% of this change |
| [[HepG2_C3A (line)]] | wt | 27.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.112× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[Hs 766T (line)]] | wt | 25.4 | 0 | 1 | — | [[PF-06260933 (drug)]] 5 µM 0.0448× (z -9.0) |
| [[LS 180 (line)]] | wt | 18.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -10.7) ⚠ cell-cycle shift, explains ~43% of this change |
| [[SW 1271 (line)]] | alt | 41.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0795× (z -10.5) ⚠ cell-cycle shift, explains ~43% of this change |
| [[A-172 (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.74 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 8.24 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.71 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 26.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.18 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.55 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 22.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 52.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.45 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 47.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 21.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6272), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SOD2]] | +0.71 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[SAA2-SAA4]] | +0.67 | +0.71 / +0.63 | both halves | 7e-06 |  |
| [[MR1]] | +0.66 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[NNMT]] | +0.63 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[TRIM56]] | +0.63 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[SAA4]] | +0.63 | +0.68 / +0.58 | both halves | 7e-06 |  |
| [[WTAP]] | +0.62 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[CEBPD]] | +0.61 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[STOM]] | +0.60 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[SAA2]] | +0.60 | +0.70 / +0.61 | both halves | 7e-06 |  |
| [[CFH]] | +0.60 | +0.46 / +0.47 | both halves | 2e-05 | same gene group |
| [[SCAMP1-AS1]] | +0.59 | +0.46 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RASA3]] | -0.60 | -0.57 / -0.41 | both halves | 4e-05 |  |
| [[GRK5]] | -0.56 | -0.55 / -0.44 | both halves | 3e-05 |  |
| [[C13orf46]] | -0.56 | -0.58 / -0.43 | both halves | 4e-05 |  |
| [[SIPA1L3]] | -0.56 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[EFL1]] | -0.55 | -0.56 / -0.34 | both halves | 1e-04 |  |
| [[ADAM19]] | -0.54 | -0.59 / -0.40 | both halves | 5e-05 |  |
| [[SLC2A13]] | -0.53 | -0.35 / -0.47 | both halves | 1e-04 |  |
| [[ETV5]] | -0.53 | -0.47 / -0.38 | both halves | 6e-05 |  |
| [[WSCD1]] | -0.52 | -0.44 / -0.33 | both halves | 1e-04 |  |
| [[HHIP]] | -0.51 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[UBA6]] | -0.51 | -0.46 / -0.21 | both halves | 6e-04 |  |
| [[ARHGAP29]] | -0.51 | -0.52 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C1RL-AS1]] | B | C1RL-AS1 activity raises C1RL's level | lines that do not express C1RL-AS1 (7) vs lines expressing it (43) | 4.57× lower at baseline in the lines without C1RL-AS1 | 0.016 | ⚠ within organs, on part of the lines; also absent: EGFR, HFE, SH2D4A |
| [[MAP2K1]] | B | MAP2K1 activity lowers C1RL's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.5% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds |
| [[MR1]] | B | MR1 activity raises C1RL's level | lines that do not express MR1 (5) vs lines expressing it (45) | 1.37× lower at baseline in the lines without MR1 | 0.095 | ⚠ within organs, on part of the lines; co-occurs with CTNNB1; also absent: GGT7, AGK, TCTN1 |
| [[NMI]] | C | NMI activity raises C1RL's level | lines that do not express NMI (4) vs lines expressing it (46) | 3.18× lower at baseline in the lines without NMI | 0.088 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: NABP1, LGI4, C21orf91; its own permutation p |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 0, C 6.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TNFRSF1A]] | C | C1RL activity raises TNFRSF1A's level | lines that do not express C1RL (3) vs lines expressing it (47) | 3.63× lower at baseline in the lines without C1RL | 9e-04 | ⚠ few lines (3 vs 47); across organs; co-occurs with WNK2; also absent: PHLDA1, CASP8, SP100 |
| [[NMI]] | C | C1RL activity raises NMI's level | lines that do not express C1RL (3) vs lines expressing it (47) | 4.94× lower at baseline in the lines without C1RL | 0.004 | ⚠ few lines (3 vs 47); across organs; co-occurs with WNK2; also absent: PHLDA1, CASP8, SP100 |
| [[CASP8]] | C | C1RL activity raises CASP8's level | lines that do not express C1RL (3) vs lines expressing it (47) | 3.08× lower at baseline in the lines without C1RL | 0.017 | ⚠ few lines (3 vs 47); across organs; co-occurs with WNK2; also absent: PHLDA1, CASP8, SP100; co-absent with the target |
| [[SH3PXD2A]] | C | C1RL activity raises SH3PXD2A's level | lines that do not express C1RL (3) vs lines expressing it (47) | 3.72× lower at baseline in the lines without C1RL | 0.033 | ⚠ few lines (3 vs 47); across organs; co-occurs with WNK2; also absent: PHLDA1, CASP8, SP100 |
| [[TRANK1]] | C | C1RL activity raises TRANK1's level | lines that do not express C1RL (3) vs lines expressing it (47) | 3.82× lower at baseline in the lines without C1RL | 0.057 | ⚠ few lines (3 vs 47); across organs; co-occurs with WNK2; also absent: PHLDA1, CASP8, SP100 |
| [[PSMB8]] | C | C1RL activity raises PSMB8's level | lines that do not express C1RL (3) vs lines expressing it (47) | 3.28× lower at baseline in the lines without C1RL | 0.066 | ⚠ few lines (3 vs 47); across organs; co-occurs with WNK2; also absent: PHLDA1, CASP8, SP100 |

## Where it sits

- **Module**: [[Module 139]] — Interleukin-4 and Interleukin-13 signaling; 34 genes; every member is in the + arm (projection on the module's main direction 0.717). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (26.9, 16.3); signed map (17.2, 28.4). **Vector** length 84.5, 23.0% of its response variance represented; |z| ≥ 3 in 1,429 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon gamma response* (hallmark, mean cos +0.53 to 6); *TNF-alpha signaling via NF-kB* (hallmark, mean cos +0.51 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +4.1 | +5.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.0 | +6.0 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | +3.8 | +5.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.8 | +3.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.7 | +5.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.4 | +4.1 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -4.1 | -3.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -4.0 | -13.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -3.8 | -15.7 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -3.5 | -4.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -3.2 | -14.7 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -3.2 | -3.7 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -3.1 | -2.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.3 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | complement C1r subcomponent like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p13.31 — chr12:7,089,587-7,109,238 (-) |
| Ensembl biotype | protein_coding |
| Also known as | C1r-LP, C1RL1 |
| Gene groups (HGNC) | Serine proteases; Sushi domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NZP8](https://www.uniprot.org/uniprotkb/Q9NZP8) (Complement C1r subcomponent-like protein):

> Mediates the proteolytic cleavage of HP/haptoglobin in the endoplasmic reticulum.

**Summary**, from NCBI Gene [51279](https://www.ncbi.nlm.nih.gov/gene/51279):

> Predicted to enable serine-type endopeptidase activity. Predicted to be involved in zymogen activation. Located in extracellular exosome and obsolete extracellular space. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:21265](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21265) · Entrez [51279](https://www.ncbi.nlm.nih.gov/gene/51279) · UniProt [Q9NZP8](https://www.uniprot.org/uniprotkb/Q9NZP8) · Ensembl [ENSG00000139178](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000139178)

## Data

Gene col 6272: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6272); `tables/drug_effects.parquet` (61 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6272, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6272]; `tensor/DDL_lfc|DDL_z.npy` [6272]; `embed/gene_vectors.npy` [6272]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6272 or target_col == 6272). Every well: [[C1RL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/C1RL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
