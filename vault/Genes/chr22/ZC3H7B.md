---
symbol: "ZC3H7B"
type: "gene"
col: 1951
ensembl_id: "ENSG00000100403"
name: "zinc finger CCCH-type containing 7B"
location: "22q13.2"
module: 88
arm: "+"
pooled_cpm: 46.84
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 14
n_dd_up_clean: 12
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/088"]
generated_by: "tahoemap"
---

# ZC3H7B

*zinc finger CCCH-type containing 7B* — 22q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.95× (z +33.2, q 0e+00, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.251× (z -29.9, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TXNRD2]] (+0.78, fdr 7e-06), [[POGLUT1]] (+0.77, fdr 7e-06), [[ITPA]] (+0.74, fdr 7e-06); moves opposite to [[MOSPD3]] (-0.68, fdr 1e-05), [[GRB2]] (-0.68, fdr 1e-05), [[HSPA5]] (-0.67, fdr 7e-06).
> It sits in the **+** arm of [[Module 088]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[CDC42EP1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1951.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.95×** | +33.2 | 0e+00 | 45/48 (Hs 766T, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **3.11×** | +23.7 | 0e+00 | 45/48 (PANC-1, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.47×** | +19.6 | 0e+00 | 45/48 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.85×** | +13.3 | 3e-38 | 43/48 (A-172, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.82×** | +12.9 | 3e-36 | 37/46 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.86×** | +12.9 | 3e-36 | 31/42 (SW480, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.62×** | +10.5 | 6e-24 | 37/48 (SNU-1, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.44×** | +7.9 | 2e-13 | 31/48 (NCI-H1573, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.44×** | +7.9 | 2e-13 | 31/48 (Hs 766T, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.35×** | +6.5 | 6e-09 | 31/48 (NCI-H1573, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.35×** | +6.0 | 1e-07 | 25/44 (HS-578T, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.28×** | +5.0 | 3e-05 | 20/47 (SNU-1, MIA PaCa-2, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.26×** | +4.8 | 7e-05 | 22/46 (NCI-H1573, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.22×** | +4.2 | 0.001 | 17/48 (PANC-1, HS-578T, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~41% of this change | **1.21×** | +4.1 | 0.001 | 20/47 (MIA PaCa-2, HS-578T, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.29×** | +3.9 | 0.003 | 18/47 (SW480, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.22×** | +3.1 | 0.054 | 4/48 (A-427, HT-29, …) | inconsistent across doses | noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.15× | +3.1 | 0.064 | 13/48 (SK-MEL-2, SW480, …) | top dose only |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.22×** | +3.0 | 0.065 | 4/48 (SW 900, Hs 766T, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 2 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1951.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.251×** | -29.9 | 0e+00 | 48/48 (SK-MEL-2, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.265×** | -28.7 | 0e+00 | 46/48 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.355×** | -22.4 | 0e+00 | 47/48 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.557×** | -12.7 | 9e-35 | 42/48 (SK-MEL-2, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.644×** | -9.5 | 2e-19 | 36/48 (MIA PaCa-2, LS 180, …) | two highest doses | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.735×** | -9.4 | 3e-19 | 38/48 (KATO III, LS 180, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.669×** | -8.7 | 3e-16 | 33/48 (PANC-1, NCI-H23, …) | two highest doses | cell-cycle shift (explains ~21% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.706×** | -7.6 | 3e-12 | 33/48 (RKO, HCT15, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.787×** | -7.3 | 1e-11 | 28/48 (RKO, SW480, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.534×** | -7.1 | 6e-11 | 36/48 (SK-MEL-2, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.729×** | -6.8 | 4e-10 | 29/48 (RKO, NCI-H23, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.726×** | -6.6 | 3e-09 | 26/48 (MIA PaCa-2, SW 1271, …) | inconsistent across doses | cell-cycle shift (explains ~18% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.762×** | -5.9 | 2e-07 | 27/48 (LS 180, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.861× | -3.1 | 0.072 | 15/47 (A549, NCI-H23, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.761×** | -3.1 | 0.077 | 7/48 (HCT15, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, +0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1951. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 68.0 | 5 | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.42× (z +21.5) | [[Panobinostat (drug)]] 5 µM 0.0927× (z -24.5) |
| [[SNU-1 (line)]] | wt | 93.6 | 5 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.40× (z +20.7) | [[Panobinostat (drug)]] 5 µM 0.0896× (z -20.9) |
| [[NCI-H1573 (line)]] | alt | 45.5 | 6 (1 ⚠) | 3 | [[Harringtonine (drug)]] 5 µM 4.05× (z +13.7) | [[Panobinostat (drug)]] 0.5 µM 0.298× (z -12.3) |
| [[PANC-1 (line)]] | alt | 50.7 | 4 | 5 | [[Homoharringtonine (drug)]] 5 µM 5.84× (z +30.3) | [[Panobinostat (drug)]] 5 µM 0.167× (z -21.8) |
| [[A-172 (line)]] | wt | 38.7 | 5 | 3 | [[Homoharringtonine (drug)]] 5 µM 3.60× (z +18.7) | [[Panobinostat (drug)]] 0.5 µM 0.177× (z -17.9) |
| [[A498 (line)]] | wt | 60.2 | 5 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +18.7) | [[Panobinostat (drug)]] 5 µM 0.280× (z -15.6) |
| [[HS-578T (line)]] | alt | 49.9 | 6 (3 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +17.6) | [[Panobinostat (drug)]] 5 µM 0.202× (z -15.6) |
| [[RKO (line)]] | wt | 72.9 | 0 | 8 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.132× (z -20.3) |
| [[A549 (line)]] | wt | 35.4 | 4 | 3 | [[Homoharringtonine (drug)]] 5 µM 5.85× (z +21.5) | [[Panobinostat (drug)]] 0.5 µM 0.311× (z -10.0) |
| [[Hs 766T (line)]] | wt | 64.2 | 4 | 3 | [[Homoharringtonine (drug)]] 5 µM 9.64× (z +32.6) | [[Panobinostat (drug)]] 0.5 µM 0.234× (z -14.8) |
| [[NCI-H460 (line)]] | wt | 38.3 | 4 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +12.5) | [[Panobinostat (drug)]] 5 µM 0.226× (z -15.6) |
| [[SNU-423 (line)]] | alt | 47.2 | 5 (2 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 4.90× (z +21.4) | [[Panobinostat (drug)]] 0.5 µM 0.327× (z -10.6) |
| [[SW480 (line)]] | alt | 44.1 | 2 (2 ⚠) | 5 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.37× (z +11.9) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.195× (z -22.6) |
| [[HEC-1-A (line)]] | alt | 72.9 | 3 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +12.4) | [[Panobinostat (drug)]] 0.5 µM 0.277× (z -15.6) |
| [[LOX-IMVI (line)]] | wt | 27.5 | 3 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +12.7) | [[Panobinostat (drug)]] 5 µM 0.246× (z -11.6) |
| [[NCI-H2347 (line)]] | alt | 31.0 | 4 | 2 | [[Homoharringtonine (drug)]] 5 µM 3.65× (z +19.7) | [[Panobinostat (drug)]] 0.5 µM 0.347× (z -11.3) |
| [[Panc 03.27 (line)]] | alt | 35.3 | 4 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 6.53× (z +21.6) | [[Panobinostat (drug)]] 0.5 µM 0.208× (z -12.7) |
| [[AsPC-1 (line)]] | alt | 29.8 | 3 | 2 | [[Homoharringtonine (drug)]] 5 µM 4.33× (z +16.1) | [[Panobinostat (drug)]] 5 µM 0.173× (z -13.6) |
| [[CFPAC-1 (line)]] | alt | 38.1 | 4 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 10.2× (z +28.1) | [[Panobinostat (drug)]] 0.5 µM 0.306× (z -10.1) |
| [[H4 (line)]] | wt | 37.9 | 2 | 3 | [[Homoharringtonine (drug)]] 5 µM 3.70× (z +11.5) | [[Panobinostat (drug)]] 5 µM 0.167× (z -11.1) |
| [[HCT15 (line)]] | alt | 48.1 | 2 (1 ⚠) | 3 | [[Harringtonine (drug)]] 5 µM 3.55× (z +9.4) | [[Panobinostat (drug)]] 5 µM 0.261× (z -10.3) |
| [[HOP62 (line)]] | alt | 23.1 | 2 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +12.5) | [[Panobinostat (drug)]] 5 µM 0.187× (z -13.8) |
| [[J82 (line)]] | alt | 35.5 | 2 | 3 | [[Homoharringtonine (drug)]] 5 µM 3.22× (z +15.8) | [[Panobinostat (drug)]] 0.5 µM 0.222× (z -14.3) |
| [[KATO III (line)]] | alt | 44.5 | 1 (1 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 2.48× (z +9.0) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.186× (z -16.5) |
| [[LS 180 (line)]] | wt | 41.3 | 1 (1 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 2.41× (z +9.0) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.158× (z -18.8) |
| [[SK-MEL-2 (line)]] | alt | 154 | 1 | 4 | [[Harringtonine (drug)]] 5 µM 2.48× (z +11.6) | [[Panobinostat (drug)]] 0.5 µM 0.147× (z -25.7) |
| [[C-33 A (line)]] | alt | 52.4 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.130× (z -15.9) |
| [[LoVo (line)]] | wt | 52.5 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.153× (z -21.8) |
| [[NCI-H23 (line)]] | alt | 52.4 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.118× (z -20.9) |
| [[SHP-77 (line)]] | alt | 62.8 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +10.2) | [[Panobinostat (drug)]] 5 µM 0.208× (z -15.3) |
| [[SW48 (line)]] | wt | 54.3 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.128× (z -16.0) |
| [[C32 (line)]] | wt | 56.3 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.242× (z -14.9) |
| [[hTERT-HPNE (line)]] | wt | 38.8 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.82× (z +13.5) | [[Panobinostat (drug)]] 5 µM 0.200× (z -11.4) |
| [[NCI-H1792 (line)]] | alt | 30.8 | 2 | 1 | [[Harringtonine (drug)]] 5 µM 5.15× (z +11.7) | [[Panobinostat (drug)]] 5 µM 0.283× (z -9.3) |
| [[NCI-H2030 (line)]] | alt | 63.3 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.313× (z -13.2) |
| [[BT-474 (line)]] | alt | 47.2 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +11.2) | [[Panobinostat (drug)]] 0.5 µM 0.257× (z -11.6) |
| [[HepG2_C3A (line)]] | wt | 46.7 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.05× (z +14.3) | [[Panobinostat (drug)]] 0.5 µM 0.272× (z -9.4) |
| [[HT-29 (line)]] | alt | 21.2 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.68× (z +13.2) | — |
| [[RPMI-7951 (line)]] | alt | 38.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.24× (z +12.8) | — |
| [[SW1417 (line)]] | alt | 40.8 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.283× (z -12.0) |
| [[A-427 (line)]] | wt | 25.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.51× (z +13.9) | — |
| [[AN3 CA (line)]] | alt | 57.9 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.134× (z -10.7) |
| [[CHP-212 (line)]] | wt | 66.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.19× (z +10.8) | — |
| [[SW 900 (line)]] | alt | 23.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.96× (z +12.6) | — |
| [[COLO 205 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 42.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 57.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 34.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1951), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TXNRD2]] | +0.78 | +0.67 / +0.73 | both halves | 7e-06 |  |
| [[POGLUT1]] | +0.77 | +0.74 / +0.66 | both halves | 7e-06 |  |
| [[ITPA]] | +0.74 | +0.68 / +0.69 | both halves | 7e-06 |  |
| [[ST7L]] | +0.74 | +0.70 / +0.61 | both halves | 7e-06 |  |
| [[NHLRC2]] | +0.71 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[GCFC2]] | +0.71 | +0.68 / +0.55 | both halves | 1e-05 |  |
| [[TRMT13]] | +0.70 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[FKRP]] | +0.70 | +0.68 / +0.46 | both halves | 3e-05 |  |
| [[LGALSL-DT]] | +0.67 | +0.66 / +0.44 | both halves | 3e-05 |  |
| [[LATS1]] | +0.67 | +0.68 / +0.57 | both halves | 1e-05 |  |
| [[DIS3L]] | +0.66 | +0.64 / +0.50 | both halves | 1e-05 |  |
| [[RBM26-AS1]] | +0.65 | +0.66 / +0.37 | both halves | 9e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MOSPD3]] | -0.68 | -0.61 / -0.53 | both halves | 1e-05 |  |
| [[GRB2]] | -0.68 | -0.69 / -0.50 | both halves | 1e-05 |  |
| [[HSPA5]] | -0.67 | -0.62 / -0.62 | both halves | 7e-06 |  |
| [[NTAN1]] | -0.66 | -0.69 / -0.49 | both halves | 1e-05 |  |
| [[MACO1]] | -0.66 | -0.66 / -0.52 | both halves | 1e-05 |  |
| [[GNB2]] | -0.65 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[SAP130]] | -0.65 | -0.67 / -0.45 | both halves | 3e-05 |  |
| [[ALKBH5]] | -0.65 | -0.61 / -0.58 | both halves | 7e-06 |  |
| [[GMCL1]] | -0.64 | -0.56 / -0.56 | both halves | 1e-05 |  |
| [[GNAI3]] | -0.63 | -0.60 / -0.48 | both halves | 2e-05 |  |
| [[IGSF8]] | -0.63 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[SNX3]] | -0.63 | -0.76 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDC42EP1]] | B | CDC42EP1 activity lowers ZC3H7B's level | lines that do not express CDC42EP1 (5) vs lines expressing it (45) | 1.88× higher at baseline in the lines without CDC42EP1 | 0.060 | ⚠ within organs, on part of the lines; also absent: ZFP36, IQCN, SLC22A20P; its own permutation p |
| [[TMEM92]] | B | TMEM92 activity lowers ZC3H7B's level | lines that do not express TMEM92 (22) vs lines expressing it (28) | 1.33× higher at baseline in the lines without TMEM92 | 0.066 | ⚠ within organs, on part of the lines; also absent: ARL14, LINC01589, TNFSF10 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 088]]; 51 genes; this gene is in the **+** arm (projection on the module's main direction 0.741). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.46).
- **Nodal map** (x, y) = (-6.0, 6.1); signed map (20.1, -30.7). **Vector** length 127, 38.5% of its response variance represented; |z| ≥ 3 in 1,253 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +14.1 | +33.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +13.4 | +19.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | +12.0 | +23.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +7.9 | +13.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.0 | +12.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +6.4 | +10.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.7 | +4.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.6 | +3.9 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +3.4 | +1.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.3 | -0.4 |
| fall | [[Ixazomib citrate (drug)]] 0.5 µM |  | -7.5 | -9.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -6.1 | -8.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.1 | -6.8 |
|  | [[Belinostat (drug)]] 5 µM |  | -5.8 | -22.4 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -5.5 | -6.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.6 | -9.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.9 | -2.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.6 | -7.1 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger CCCH-type containing 7B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.2 — chr22:41,301,525-41,360,147 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RoXaN, FLJ13787, DKFZp434K0920, KIAA1031 |
| Gene groups (HGNC) | Zinc fingers CCCH-type; Tetratricopeptide repeat domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UGR2](https://www.uniprot.org/uniprotkb/Q9UGR2) (Zinc finger CCCH domain-containing protein 7B):

> May be a specific regulator of miRNA biogenesis. Binds to microRNAs MIR7-1, MIR16-2 and MIR29A hairpins recognizing the 'ATA(A/T)' motif in the apical loop.

**Summary**, from NCBI Gene [23264](https://www.ncbi.nlm.nih.gov/gene/23264):

> This gene encodes a protein that contains a tetratricopeptide repeat domain. The encoded protein also interacts with the rotavirus non-structural protein NSP3. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:30869](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30869) · Entrez [23264](https://www.ncbi.nlm.nih.gov/gene/23264) · UniProt [Q9UGR2](https://www.uniprot.org/uniprotkb/Q9UGR2) · Ensembl [ENSG00000100403](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100403)

## Data

Gene col 1951: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1951); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1951, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1951]; `tensor/DDL_lfc|DDL_z.npy` [1951]; `embed/gene_vectors.npy` [1951]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1951 or target_col == 1951). Every well: [[ZC3H7B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZC3H7B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
