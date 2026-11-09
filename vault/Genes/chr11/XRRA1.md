---
symbol: "XRRA1"
type: "gene"
col: 9303
ensembl_id: "ENSG00000166435"
name: "X-ray radiation resistance associated 1"
location: "11q13.4"
module: 41
arm: "+"
pooled_cpm: 92.94
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 17
n_dd_up_clean: 7
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/041"]
generated_by: "tahoemap"
---

# XRRA1

*X-ray radiation resistance associated 1* — 11q13.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 1.78× (z +16.3, q 0e+00, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (11 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 0.533× (z -17.1, q 0e+00, down in 39 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[PH-797804 (drug)]] 5 µM: 0.411× (z -13.0, q 5e-36, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SEC11C]] (+0.67, fdr 7e-06), [[SEC22A]] (+0.64, fdr 1e-05), [[COPE]] (+0.63, fdr 1e-05); moves opposite to [[NUP50]] (-0.52, fdr 1e-05), [[VSIG10]] (-0.52, fdr 1e-04), [[DNAJB6]] (-0.49, fdr 2e-05).
> It sits in the **+** arm of [[Module 041]] (Intra-Golgi and retrograde Golgi-to-ER traffic).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9303.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.78×** | +16.3 | 0e+00 | 39/48 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.54×** | +12.2 | 7e-32 | 33/48 (A-172, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.34×** | +11.7 | 2e-29 | 34/48 (HOP62, A-172, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.34×** | +8.3 | 1e-14 | 31/49 (C32, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.32×** | +7.9 | 3e-13 | 32/48 (A-172, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.21×** | +5.4 | 7e-06 | 23/48 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.15× | +3.9 | 0.007 | 16/49 (A-172, LS 180, …) | top dose only |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | 1.16× | +3.8 | 0.009 | 13/50 (MIA PaCa-2, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.10× | +3.7 | 0.016 | 18/48 (NCI-H23, COLO 205, …) | rises with dose | composition shift |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.27×** | +3.5 | 0.023 | 8/48 (J82, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.09× | +3.5 | 0.023 | 3/49 (LS 180, CFPAC-1, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.13× | +3.4 | 0.029 | 16/48 (NCI-H1573, SW480, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | 1.12× | +3.1 | 0.077 | 11/48 (A549, A-427, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.08× | +3.1 | 0.080 | 6/48 (SW480, HEC-1-A, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 17 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9303.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.533×** | -17.1 | 0e+00 | 39/47 (C-33 A, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.411×** | -13.0 | 5e-36 | 44/48 (SNU-1, RPMI-7951, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.645×** | -12.4 | 6e-33 | 39/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.486×** | -10.5 | 1e-23 | 41/49 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.676×** | -10.2 | 2e-22 | 30/45 (SNU-423, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~23% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.723×** | -9.2 | 4e-18 | 31/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.736×** | -8.7 | 3e-16 | 33/48 (J82, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.753×** | -8.0 | 8e-14 | 30/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.776×** | -7.2 | 4e-11 | 28/48 (LoVo, SNU-423, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.632×** | -6.7 | 1e-09 | 30/45 (SHP-77, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~2% of this change | 0.855× | -6.2 | 2e-08 | 21/49 (NCI-H460, NCI-H1792, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change | **0.815×** | -5.8 | 3e-07 | 23/49 (NCI-H1573, A-427, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | **0.817×** | -5.5 | 2e-06 | 21/48 (C32, J82, …) | top dose only | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | **0.821×** | -5.4 | 3e-06 | 22/42 (NCI-H1573, Panc 03.27, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.830×** | -5.3 | 5e-06 | 22/48 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | 0.850× | -4.6 | 1e-04 | 21/48 (MIA PaCa-2, C32, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.912× | -3.7 | 0.006 | 8/48 (Hs 766T, COLO 205, …) | top dose only |  |
| [[Auranofin (drug)]] 0.5 µM |  | 0.881× | -3.6 | 0.009 | 10/48 (SW 1271, C-33 A, …) | rises with dose |  |
| [[Pimitespib (drug)]] 5 µM |  | **0.788×** | -3.5 | 0.013 | 10/48 (RPMI-7951, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | 0.848× | -3.3 | 0.022 | 13/49 (NCI-H1573, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 0.891× | -3.2 | 0.027 | 10/48 (HCT15, H4, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.896× | -3.1 | 0.041 | 12/47 (MIA PaCa-2, NCI-H2030, …) | two highest doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.893× | -3.0 | 0.047 | 15/47 (LOX-IMVI, BT-474, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 0.5 µM |  | 0.870× | -2.8 | 0.094 | 10/48 (NCI-H23, SW480, …) | all doses, stronger at high dose | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[vincristine (drug)]] 5 µM |  | **0.826×** | -2.8 | 0.094 | 9/46 (CHP-212, H4, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9303. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 100 | 0 | 9 (9 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.310× (z -20.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[NCI-H1573 (line)]] | alt | 286 | 2 (2 ⚠) | 6 (6 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.45× (z +13.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.325× (z -16.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change |
| [[HOP62 (line)]] | alt | 54.8 | 3 | 3 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.91× (z +10.6) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.444× (z -9.5) ⚠ cell-cycle shift, explains ~44% of this change |
| [[PANC-1 (line)]] | alt | 151 | 0 | 6 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.431× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.370× (z -8.9) |
| [[SW480 (line)]] | alt | 140 | 1 (1 ⚠) | 5 (5 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 1.63× (z +9.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.549× (z -11.7) ⚠ cell-cycle shift, explains ~50% of this change |
| [[A-172 (line)]] | wt | 62.0 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.10× (z +14.9) | [[Dinaciclib (drug)]] 0.05 µM 0.405× (z -8.8) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 55.6 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.59× (z +10.8) | [[Niclosamide (olamine) (drug)]] 5 µM 0.386× (z -10.4) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 153 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.440× (z -16.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.296× (z -8.9) |
| [[Hs 766T (line)]] | wt | 142 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.369× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change |
| [[NCI-H23 (line)]] | alt | 133 | 2 (1 ⚠) | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.16× (z +10.7) | [[Niclosamide (olamine) (drug)]] 5 µM 0.365× (z -13.5) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 126 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.314× (z -14.5) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 55.0 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.61× (z +10.6) | [[Homoharringtonine (drug)]] 5 µM 0.477× (z -11.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 60.0 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.371× (z -13.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HT-29 (line)]] | alt | 50.3 | 1 | 2 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.07× (z +8.7) | [[Digitoxin (drug)]] 5 µM 0.335× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[KATO III (line)]] | alt | 157 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.312× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change |
| [[SHP-77 (line)]] | alt | 57.8 | 1 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.87× (z +9.8) | [[Digitoxin (drug)]] 5 µM 0.344× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[A-427 (line)]] | wt | 135 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.366× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change |
| [[A498 (line)]] | wt | 25.5 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.06× (z +11.9) | — |
| [[COLO 205 (line)]] | alt | 152 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.00× (z +9.4) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[HCT15 (line)]] | alt | 195 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.327× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change |
| [[MIA PaCa-2 (line)]] | alt | 98.4 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.336× (z -13.8) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.461× (z -10.2) |
| [[NCI-H2347 (line)]] | alt | 33.1 | 2 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 2.36× (z +12.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.35× (z +9.0) | — |
| [[Panc 03.27 (line)]] | alt | 103 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.291× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change |
| [[RPMI-7951 (line)]] | alt | 141 | 0 | 2 (1 ⚠) | — | [[PH-797804 (drug)]] 5 µM 0.154× (z -10.7) |
| [[SNU-1 (line)]] | wt | 132 | 0 | 2 (1 ⚠) | — | [[PH-797804 (drug)]] 5 µM 0.0936× (z -13.6) |
| [[AN3 CA (line)]] | alt | 90.5 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.266× (z -8.6) ⚠ toxic |
| [[AsPC-1 (line)]] | alt | 26.7 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.36× (z +8.6) | — |
| [[C-33 A (line)]] | alt | 57.3 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0828× (z -20.2) ⚠ toxic |
| [[HS-578T (line)]] | alt | 134 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.470× (z -9.8) ⚠ toxic |
| [[LoVo (line)]] | wt | 50.8 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.433× (z -8.9) |
| [[LS 180 (line)]] | wt | 37.1 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.37× (z +9.9) | — |
| [[SW 1088 (line)]] | alt | 89.2 | 0 | 1 (1 ⚠) | — | [[Plicamycin (drug)]] 5 µM 0.0902× (z -8.8) ⚠ unreliable plate only |
| [[SW 900 (line)]] | alt | 113 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.435× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[SW1417 (line)]] | alt | 112 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.376× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change |
| [[BT-474 (line)]] | alt | 65.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 43.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 63.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 114 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 65.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 62.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 57.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 75.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 96.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 78.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 26.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9303), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEC11C]] | +0.67 | +0.62 / +0.69 | both halves | 7e-06 |  |
| [[SEC22A]] | +0.64 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[COPE]] | +0.63 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[GOLGA1]] | +0.62 | +0.72 / +0.55 | both halves | 1e-05 |  |
| [[ARFIP2]] | +0.60 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[LYSMD3]] | +0.58 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[GOLGA4]] | +0.58 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[FRA10AC1]] | +0.58 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[SEC23B]] | +0.57 | +0.64 / +0.46 | both halves | 3e-05 |  |
| [[RUSF1]] | +0.56 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[NDUFV3]] | +0.55 | +0.65 / +0.49 | both halves | 1e-05 |  |
| [[DDX50]] | +0.55 | +0.57 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUP50]] | -0.52 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[VSIG10]] | -0.52 | -0.33 / -0.43 | both halves | 1e-04 |  |
| [[DNAJB6]] | -0.49 | -0.46 / -0.49 | both halves | 2e-05 |  |
| [[UTP4]] | -0.48 | -0.47 / -0.40 | both halves | 5e-05 |  |
| [[JADE2]] | -0.48 | -0.28 / -0.51 | both halves | 3e-04 |  |
| [[TOR3A]] | -0.47 | -0.40 / -0.28 | both halves | 3e-04 |  |
| [[GNG12]] | -0.47 | -0.57 / -0.44 | both halves | 3e-05 |  |
| [[SMAD6]] | -0.46 | -0.44 / -0.29 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers XRRA1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers XRRA1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 041]] — Intra-Golgi and retrograde Golgi-to-ER traffic; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.524). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (13.7, -38.5); signed map (-53.6, 15.1). **Vector** length 95.7, 24.6% of its response variance represented; |z| ≥ 3 in 1,247 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +4.2 | +3.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.1 | +2.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.0 | +3.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.4 | +1.1 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +3.3 | +1.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.7 | +3.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.7 | +1.6 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~2% of this change | -8.8 | -6.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -6.6 | -17.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.8 | -13.0 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | -4.7 | -3.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.5 | -3.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.6 | -3.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.7 | -7.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.5 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | X-ray radiation resistance associated 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.4 — chr11:74,807,739-74,949,200 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ00225 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6P2D8](https://www.uniprot.org/uniprotkb/Q6P2D8) (X-ray radiation resistance-associated protein 1):

> May be involved in the response of cells to X-ray radiation.

**Summary**, from NCBI Gene [143570](https://www.ncbi.nlm.nih.gov/gene/143570):

> Involved in response to X-ray. Located in cytoplasm and nuclear body. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:18868](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18868) · Entrez [143570](https://www.ncbi.nlm.nih.gov/gene/143570) · UniProt [Q6P2D8](https://www.uniprot.org/uniprotkb/Q6P2D8) · Ensembl [ENSG00000166435](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166435)

## Data

Gene col 9303: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9303); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9303, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9303]; `tensor/DDL_lfc|DDL_z.npy` [9303]; `embed/gene_vectors.npy` [9303]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9303 or target_col == 9303). Every well: [[XRRA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/XRRA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
