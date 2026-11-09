---
symbol: "SLFN5"
type: "gene"
col: 9351
ensembl_id: "ENSG00000166750"
name: "schlafen family member 5"
location: "17q12"
module: 32
arm: "+"
pooled_cpm: 98.88
n_lines_expressing: 39
n_dd_up: 40
n_dd_down: 29
n_dd_up_clean: 35
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 11
direction_downstream: 26
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# SLFN5

*schlafen family member 5* — 17q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 40 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.58× (z +20.4, q 0e+00, up in 37 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (11 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.225× (z -11.9, q 6e-30, down in 33 of 38 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRIM69]] (+0.71, fdr 7e-06), [[ATF5]] (+0.70, fdr 4e-05), [[MAD2L1BP]] (+0.68, fdr 1e-05); moves opposite to [[PHKA2]] (-0.65, fdr 1e-05), [[CEP131]] (-0.61, fdr 3e-04), [[PIK3R2]] (-0.61, fdr 3e-05).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[CCDC71L]] → it (grade B ⚠); 26 go from it, the strongest it → cells under [[Arbutin (drug)]] 5 µM (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 46 in all, 5 with an alert ⚠; shown: the 15 strongest. 40 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9351.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.58×** | +20.4 | 0e+00 | 37/38 (HEC-1-A, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.20×** | +17.8 | 0e+00 | 33/37 (HOP62, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.09×** | +15.9 | 0e+00 | 30/37 (HOP62, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.67×** | +11.1 | 3e-26 | 30/37 (HOP62, NCI-H2347, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **2.07×** | +10.7 | 1e-24 | 28/37 (HOP62, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.94×** | +10.1 | 5e-22 | 32/37 (HEC-1-A, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.88×** | +9.6 | 5e-20 | 30/37 (hTERT-HPNE, A-172, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.78×** | +8.5 | 2e-15 | 25/37 (HEC-1-A, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.68×** | +7.9 | 1e-13 | 30/37 (A-172, A498, …) | all doses, stronger at high dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.67×** | +7.8 | 3e-13 | 34/37 (HEC-1-A, SW480, …) | top dose only |  |
| [[Artesunate (drug)]] 5 µM |  | **1.40×** | +7.3 | 2e-11 | 25/37 (HEC-1-A, KATO III, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.35×** | +6.5 | 3e-09 | 23/37 (HT-29, HEC-1-A, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.55×** | +6.4 | 6e-09 | 23/39 (SW 900, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Artesunate (drug)]] 0.5 µM |  | **1.40×** | +5.1 | 1e-05 | 24/37 (HEC-1-A, KATO III, …) | rises with dose |  |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | **1.26×** | +5.1 | 1e-05 | 21/38 (H4, PANC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 11 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9351.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.225×** | -11.9 | 6e-30 | 33/38 (A-172, NCI-H1792, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.234×** | -11.6 | 1e-28 | 34/37 (A-172, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.470×** | -11.5 | 2e-28 | 31/37 (H4, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.473×** | -11.4 | 5e-28 | 31/37 (H4, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.503×** | -10.5 | 1e-23 | 31/37 (H4, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.570×** | -8.6 | 1e-15 | 33/37 (RKO, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.578×** | -8.4 | 5e-15 | 30/37 (KATO III, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.654×** | -6.5 | 7e-09 | 26/37 (RKO, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.656×** | -6.4 | 8e-09 | 29/37 (RKO, BT-474, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.660×** | -6.3 | 1e-08 | 31/37 (RKO, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[NG25 (drug)]] 5 µM |  | **0.452×** | -6.3 | 1e-08 | 33/36 (NCI-H1792, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~3% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.662×** | -6.3 | 1e-08 | 26/37 (RPMI-7951, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **0.687×** | -5.5 | 2e-06 | 22/36 (A-172, NCI-H1792, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change | **0.722×** | -5.0 | 3e-05 | 21/38 (A-172, LoVo, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.722×** | -4.8 | 6e-05 | 21/37 (H4, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.762×** | -4.2 | 0.001 | 22/37 (SW 1088, Hs 766T, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.598×** | -4.1 | 0.001 | 22/37 (RPMI-7951, SK-MEL-2, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.691×** | -4.0 | 0.002 | 22/38 (A-172, Panc 03.27, …) | all doses, flat | noisy plate (z scaled) |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.773×** | -3.9 | 0.002 | 21/37 (BT-474, LoVo, …) | two highest doses |  |
| [[Tofacitinib (drug)]] 5 µM |  | 0.834× | -3.9 | 0.002 | 21/38 (LoVo, BT-474, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.629×** | -3.7 | 0.005 | 23/37 (NCI-H1573, RPMI-7951, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.27 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9351. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 336 | 7 | 13 (9 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.33× (z +16.1) | [[PH-797804 (drug)]] 5 µM 0.0567× (z -20.1) |
| [[LoVo (line)]] | wt | 124 | 1 | 14 (6 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.70× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.170× (z -17.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.220× (z -14.5) |
| [[BT-474 (line)]] | alt | 345 | 4 | 10 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +10.0) | [[TAK-901 (drug)]] 0.05 µM 0.167× (z -16.4) |
| [[H4 (line)]] | wt | 175 | 1 | 13 (7 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.58× (z +8.6) | [[Digitoxin (drug)]] 5 µM 0.144× (z -17.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.195× (z -14.8) |
| [[NCI-H460 (line)]] | wt | 164 | 0 | 13 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.260× (z -13.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.305× (z -12.1) |
| [[HEC-1-A (line)]] | alt | 72.1 | 12 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.92× (z +21.1) | — |
| [[NCI-H1792 (line)]] | alt | 272 | 3 | 9 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.67× (z +25.5) | [[TAK-901 (drug)]] 5 µM 0.0782× (z -15.6) |
| [[SW 900 (line)]] | alt | 110 | 6 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 4.38× (z +13.9) | [[Belinostat (drug)]] 5 µM 0.283× (z -11.8) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.138× (z -9.7) |
| [[HT-29 (line)]] | alt | 173 | 4 | 6 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +14.5) | [[Dinaciclib (drug)]] 0.05 µM 0.241× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.0823× (z -14.4) |
| [[KATO III (line)]] | alt | 179 | 1 | 9 (4 ⚠) | [[Artesunate (drug)]] 5 µM 2.18× (z +9.8) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.166× (z -15.9) |
| [[RKO (line)]] | wt | 130 | 1 | 9 (5 ⚠) | [[Homoharringtonine (drug)]] 0.05 µM 2.61× (z +10.0) | [[Belinostat (drug)]] 5 µM 0.174× (z -18.2) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.0446× (z -17.0) |
| [[A498 (line)]] | wt | 179 | 5 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 6.24× (z +17.4) | [[TAK-901 (drug)]] 5 µM 0.106× (z -11.1) |
| [[RPMI-7951 (line)]] | alt | 196 | 1 | 8 (4 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.10× (z +11.0) | [[Ixazomib citrate (drug)]] 5 µM 0.322× (z -10.9) |
| [[HOP62 (line)]] | alt | 82.7 | 8 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.98× (z +28.6) | — |
| [[hTERT-HPNE (line)]] | wt | 82.6 | 8 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.80× (z +21.7) | — |
| [[Panc 03.27 (line)]] | alt | 150 | 3 | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.52× (z +16.1) | [[Digitoxin (drug)]] 5 µM 0.192× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.286× (z -11.3) |
| [[PANC-1 (line)]] | alt | 31.8 | 4 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +14.0) | [[Digitoxin (drug)]] 0.5 µM 0.244× (z -12.4) |
| [[C32 (line)]] | wt | 78.5 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.85× (z +22.0) | — |
| [[J82 (line)]] | alt | 60.3 | 5 | 1 | [[Homoharringtonine (drug)]] 5 µM 6.40× (z +22.2) | [[Ixazomib citrate (drug)]] 5 µM 0.343× (z -9.0) |
| [[NCI-H2347 (line)]] | alt | 59.1 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.68× (z +16.0) | — |
| [[CFPAC-1 (line)]] | alt | 109 | 4 | 1 | [[Homoharringtonine (drug)]] 5 µM 5.96× (z +22.6) | [[TAK-901 (drug)]] 5 µM 0.164× (z -8.5) |
| [[LOX-IMVI (line)]] | wt | 27.6 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.59× (z +16.1) | — |
| [[NCI-H1573 (line)]] | alt | 119 | 1 | 4 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.46× (z +11.5) | [[Dinaciclib (drug)]] 0.5 µM 0.266× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change · without an alert: [[NG25 (drug)]] 5 µM 0.155× (z -8.8) |
| [[Hs 766T (line)]] | wt | 106 | 0 | 4 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.258× (z -10.4) |
| [[HS-578T (line)]] | alt | 79.8 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.21× (z +13.6) | — |
| [[NCI-H2030 (line)]] | alt | 86.4 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.39× (z +12.7) | — |
| [[NCI-H23 (line)]] | alt | 86.1 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.287× (z -10.5) ⚠ toxic; transcription drop · without an alert: [[Tofacitinib (drug)]] 5 µM 0.473× (z -8.9) |
| [[SNU-423 (line)]] | alt | 86.8 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.56× (z +13.9) | — |
| [[SW480 (line)]] | alt | 52.3 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.44× (z +17.4) | — |
| [[A549 (line)]] | wt | 76.2 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.59× (z +17.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 47.6 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.16× (z +12.0) | — |
| [[SK-MEL-2 (line)]] | alt | 40.4 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.28× (z +11.7) | — |
| [[HepG2_C3A (line)]] | wt | 42.7 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.151× (z -10.0) |
| [[SW 1088 (line)]] | alt | 92.2 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0617× (z -9.2) |
| [[SW 1271 (line)]] | alt | 112 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.80× (z +10.4) | — |
| [[SW1417 (line)]] | alt | 70.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.20× (z +9.6) | — |
| [[A-427 (line)]] | wt | 20.5 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 18.1 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 16.2 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 18.6 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 183 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.50 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 8.28 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 21.2 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 74.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.1 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 7.03 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 11.4 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 23.9 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9351), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRIM69]] | +0.71 | +0.68 / +0.61 | both halves | 7e-06 |  |
| [[ATF5]] | +0.70 | +0.73 / +0.42 | both halves | 4e-05 |  |
| [[MAD2L1BP]] | +0.68 | +0.70 / +0.53 | both halves | 1e-05 |  |
| [[DDX60]] | +0.68 | +0.73 / +0.60 | both halves | 7e-06 |  |
| [[TRIM56]] | +0.68 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[KRBOX5]] | +0.68 | +0.73 / +0.40 | both halves | 5e-05 |  |
| [[DDX60L]] | +0.68 | +0.68 / +0.58 | both halves | 7e-06 |  |
| [[PARP14]] | +0.67 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[THAP2]] | +0.67 | +0.71 / +0.39 | both halves | 6e-05 |  |
| [[PPP1R12A-AS2]] | +0.67 | +0.68 / +0.40 | both halves | 5e-05 |  |
| [[PATL2]] | +0.67 | +0.68 / +0.48 | both halves | 2e-05 |  |
| [[ZBTB21]] | +0.67 | +0.60 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PHKA2]] | -0.65 | -0.58 / -0.49 | both halves | 1e-05 |  |
| [[CEP131]] | -0.61 | -0.56 / -0.28 | both halves | 3e-04 |  |
| [[PIK3R2]] | -0.61 | -0.60 / -0.44 | both halves | 3e-05 |  |
| [[TCF3]] | -0.60 | -0.54 / -0.46 | both halves | 3e-05 |  |
| [[SKP2]] | -0.60 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[SHQ1]] | -0.59 | -0.57 / -0.51 | both halves | 1e-05 |  |
| [[ELP1]] | -0.59 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[RPA1]] | -0.59 | -0.61 / -0.49 | both halves | 1e-05 |  |
| [[NUDT21]] | -0.58 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[NDRG3]] | -0.58 | -0.46 / -0.48 | both halves | 2e-05 |  |
| [[TUFM]] | -0.57 | -0.52 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 5, C 6.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCDC71L]] | B | CCDC71L activity raises SLFN5's level | lines that do not express CCDC71L (8) vs lines expressing it (42) | 5.68× lower at baseline in the lines without CCDC71L | 0.001 | ⚠ within organs, on part of the lines; also absent: RAI14, VIM-AS1, ENSG00000243797; maybe low, not absent |
| [[TRIM38]] | B | TRIM38 activity raises SLFN5's level | lines that do not express TRIM38 (6) vs lines expressing it (44) | 3.64× lower at baseline in the lines without TRIM38 | 0.044 | ⚠ within organs, on part of the lines; also absent: SMOX, S100A13, ERAP2 |
| [[FYB1]] | B | FYB1 activity raises SLFN5's level | lines that do not express FYB1 (32) vs lines expressing it (18) | 2.11× lower at baseline in the lines without FYB1 | 0.066 | ⚠ within organs, on part of the lines; also absent: AMPH, IRAG2, ENSG00000266450 |
| [[IFIT3]] | B | IFIT3 activity raises SLFN5's level | lines that do not express IFIT3 (8) vs lines expressing it (42) | 3.29× lower at baseline in the lines without IFIT3 | 0.068 | ⚠ within organs, on part of the lines; also absent: GBP2, IFIT2, TRIM38; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers SLFN5's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.6% of all compounds | 0.071 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LACC1]] | C | LACC1 activity raises SLFN5's level | lines that do not express LACC1 (6) vs lines expressing it (44) | 5.39× lower at baseline in the lines without LACC1 | 0.012 | ⚠ within organs, on part of the lines; also absent: CCDC122, IL1RAP, NABP1; co-absent with the target |
| [[PSMB8]] | C | PSMB8 activity raises SLFN5's level | lines that do not express PSMB8 (4) vs lines expressing it (46) | 4.86× lower at baseline in the lines without PSMB8 | 0.032 | ⚠ few lines (4 vs 46); across organs; co-occurs with WNK2; also absent: TBILA, GCA, C3orf52 |
| [[SAMD9]] | C | SAMD9 activity raises SLFN5's level | lines that do not express SAMD9 (11) vs lines expressing it (39) | 3.75× lower at baseline in the lines without SAMD9 | 0.037 | ⚠ within organs, on part of the lines; also absent: IFI44, GBP1, TLR6; co-absent with the target |
| [[PHF11]] | C | PHF11 activity raises SLFN5's level | lines that do not express PHF11 (3) vs lines expressing it (47) | 5.92× lower at baseline in the lines without PHF11 | 0.052 | ⚠ few lines (3 vs 47); across organs; also absent: NABP1, ANXA2, SDC4 |
| [[FZD7]] | C | FZD7 activity raises SLFN5's level | lines that do not express FZD7 (3) vs lines expressing it (47) | 5.04× lower at baseline in the lines without FZD7 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: SPDL1, HOMER3, RBMS2; its own permutation p |
| [[NMI]] | C | NMI activity raises SLFN5's level | lines that do not express NMI (4) vs lines expressing it (46) | 3.82× lower at baseline in the lines without NMI | 0.088 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: NABP1, LGI4, C21orf91; its own permutation p |

### Downstream of this gene

*26 arrows, 26 of them with an alert ⚠; grade A 0, B 24, C 2. Shown: the 12 strongest; 14 more arrows (14 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Arbutin (drug)]] 5 µM | B | SLFN5 activity raises the cells' numbers under Arbutin 5 µM (protects the cells) | lines that do not express SLFN5 (11) vs lines expressing it (37) | the lines without SLFN5: 0.78× the cells of the other lines | 0.037 | ⚠ within organs, on part of the lines; also absent: ENSG00000261273, ETS1, SAMD9; maybe low, not absent |
| [[TRIM38]] | B | SLFN5 activity raises TRIM38's level | lines that do not express SLFN5 (11) vs lines expressing it (39) | 2.43× lower at baseline in the lines without SLFN5 | 0.042 | ⚠ within organs, on part of the lines; also absent: ENSG00000261273, ETS1, SAMD9; maybe low, not absent |
| [[NKX3-1]] | B | SLFN5 activity raises NKX3-1's level | lines that do not express SLFN5 (11) vs lines expressing it (39) | 2.83× lower at baseline in the lines without SLFN5 | 0.045 | ⚠ within organs, on part of the lines; also absent: ENSG00000261273, ETS1, SAMD9; maybe low, not absent |
| [[TRIM56]] | B | SLFN5 activity raises TRIM56's level | lines that do not express SLFN5 (11) vs lines expressing it (39) | 1.65× lower at baseline in the lines without SLFN5 | 0.046 | ⚠ within organs, on part of the lines; also absent: ENSG00000261273, ETS1, SAMD9; maybe low, not absent |
| [[PPP1R15A]] | B | SLFN5 activity raises PPP1R15A's level | lines that do not express SLFN5 (11) vs lines expressing it (39) | 1.43× lower at baseline in the lines without SLFN5 | 0.059 | ⚠ within organs, on part of the lines; also absent: ENSG00000261273, ETS1, SAMD9; maybe low, not absent |
| cells under [[Sulfatinib (drug)]] 5 µM | B | SLFN5 activity raises the cells' numbers under Sulfatinib 5 µM (protects the cells) | lines that do not express SLFN5 (11) vs lines expressing it (37) | the lines without SLFN5: 0.75× the cells of the other lines | 0.071 | ⚠ within organs, on part of the lines; also absent: ENSG00000261273, ETS1, SAMD9; maybe low, not absent |
| cells under [[Vortioxetine (drug)]] 0.5 µM | B | SLFN5 activity lowers the cells' numbers under Vortioxetine 0.5 µM (makes them more sensitive) | lines that do not express SLFN5 (11) vs lines expressing it (37) | the lines without SLFN5: 1.24× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: ENSG00000261273, ETS1, SAMD9; maybe low, not absent |
| cells under [[Tetracycline (hydrochloride) (drug)]] 0.5 µM | B | SLFN5 activity raises the cells' numbers under Tetracycline (hydrochloride) 0.5 µM (protects the cells) | lines that do not express SLFN5 (11) vs lines expressing it (37) | the lines without SLFN5: 0.79× the cells of the other lines | 0.075 | ⚠ within organs, on part of the lines; also absent: ENSG00000261273, ETS1, SAMD9; maybe low, not absent |
| cells under [[Cobimetinib (drug)]] 0.5 µM | B | SLFN5 activity lowers the cells' numbers under Cobimetinib 0.5 µM (makes them more sensitive) | lines that do not express SLFN5 (11) vs lines expressing it (37) | the lines without SLFN5: 1.32× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; also absent: ENSG00000261273, ETS1, SAMD9; maybe low, not absent |
| cells under [[Pentoxifylline (drug)]] 0.05 µM | B | SLFN5 activity raises the cells' numbers under Pentoxifylline 0.05 µM (protects the cells) | lines that do not express SLFN5 (11) vs lines expressing it (37) | the lines without SLFN5: 0.84× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: ENSG00000261273, ETS1, SAMD9; maybe low, not absent |
| cells under [[Betamethasone dipropionate (drug)]] 5 µM | B | SLFN5 activity raises the cells' numbers under Betamethasone dipropionate 5 µM (protects the cells) | lines that do not express SLFN5 (11) vs lines expressing it (37) | the lines without SLFN5: 0.80× the cells of the other lines | 0.082 | ⚠ within organs, on part of the lines; also absent: ENSG00000261273, ETS1, SAMD9; maybe low, not absent |
| cells under [[Citalopram (hydrobromide) (drug)]] 0.05 µM | B | SLFN5 activity raises the cells' numbers under Citalopram (hydrobromide) 0.05 µM (protects the cells) | lines that do not express SLFN5 (11) vs lines expressing it (37) | the lines without SLFN5: 0.77× the cells of the other lines | 0.088 | ⚠ within organs, on part of the lines; also absent: ENSG00000261273, ETS1, SAMD9; maybe low, not absent |

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.588). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (5.1, 11.6); signed map (21.4, -11.3). **Vector** length 144, 48.8% of its response variance represented; |z| ≥ 3 in 1,594 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon* (control, mean cos +0.51 to 23); *Antimicrobial mechanism of IFN-stimulated genes* (reactome, mean cos +0.50 to 21); *IFIT antiviral response* (reactome, mean cos +0.53 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +12.7 | +17.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +11.5 | +10.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | +10.6 | +10.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +10.3 | +15.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.2 | +20.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +8.3 | +9.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.8 | +11.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +6.7 | +7.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +6.5 | +7.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.8 | +6.5 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -8.4 | -8.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -8.0 | -6.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | -6.7 | -6.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -6.0 | -6.4 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -5.8 | -3.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -5.0 | -1.4 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -4.7 | -3.9 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -4.5 | -3.7 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -4.2 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | schlafen family member 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q12 — chr17:35,243,071-35,273,655 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC19764 |
| Gene groups (HGNC) | Schlafen family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q08AF3](https://www.uniprot.org/uniprotkb/Q08AF3) (Schlafen family member 5):

> May have a role in hematopoietic cell differentiation.

**Summary**, from NCBI Gene [162394](https://www.ncbi.nlm.nih.gov/gene/162394):

> Predicted to enable ATP binding activity; RNA nuclease activity; and ribosome binding activity. Predicted to be involved in cell differentiation and rRNA catabolic process. Predicted to be located in nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28286](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28286) · Entrez [162394](https://www.ncbi.nlm.nih.gov/gene/162394) · UniProt [Q08AF3](https://www.uniprot.org/uniprotkb/Q08AF3) · Ensembl [ENSG00000166750](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166750)

## Data

Gene col 9351: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9351); `tables/drug_effects.parquet` (76 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9351, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9351]; `tensor/DDL_lfc|DDL_z.npy` [9351]; `embed/gene_vectors.npy` [9351]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9351 or target_col == 9351). Every well: [[SLFN5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLFN5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
