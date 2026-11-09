---
symbol: "CHML"
type: "gene"
col: 12776
ensembl_id: "ENSG00000203668"
name: "CHM like Rab escort protein"
location: "1q43"
module: 41
arm: "-"
pooled_cpm: 56.41
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 12
n_dd_up_clean: 13
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/041"]
generated_by: "tahoemap"
---

# CHML

*CHM like Rab escort protein* — 1q43

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.73× (z +23.9, q 0e+00, up in 41 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belinostat (drug)]] 5 µM: 1.54× (z +8.1, q 5e-14, up in 34 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.702× (z -9.4, q 2e-18, down in 28 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SEMA3C]] (+0.57, fdr 1e-05), [[SERBP1]] (+0.57, fdr 1e-05), [[TPM4]] (+0.56, fdr 3e-05); moves opposite to [[COG7]] (-0.65, fdr 7e-06), [[KBTBD4]] (-0.58, fdr 9e-05), [[TMEM101]] (-0.58, fdr 2e-05).
> It sits in the **-** arm of [[Module 041]] (Intra-Golgi and retrograde Golgi-to-ER traffic).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12776.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.73×** | +23.9 | 0e+00 | 41/42 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.52×** | +23.8 | 0e+00 | 44/46 (HS-578T, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.11×** | +13.1 | 1e-36 | 38/45 (NCI-H2347, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.54×** | +8.1 | 5e-14 | 34/48 (J82, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.52×** | +8.0 | 2e-13 | 32/48 (J82, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.50×** | +7.7 | 1e-12 | 32/48 (J82, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.49×** | +7.6 | 3e-12 | 32/47 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.38×** | +6.0 | 1e-07 | 27/48 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.23×** | +5.5 | 2e-06 | 22/48 (SW1417, LOX-IMVI, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.33×** | +5.1 | 2e-05 | 25/48 (PANC-1, NCI-H2347, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~21% of this change | **1.28×** | +4.5 | 4e-04 | 20/47 (NCI-H1573, NCI-H1792, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.49×** | +4.0 | 0.003 | 17/49 (J82, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 0.05 µM |  | **1.23×** | +3.9 | 0.003 | 17/49 (A-427, NCI-H2030, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.23×** | +3.9 | 0.003 | 17/48 (HS-578T, KATO III, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.22×** | +3.8 | 0.006 | 12/48 (NCI-H460, NCI-H1573, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 5 µM |  | 1.15× | +3.6 | 0.010 | 12/48 (LOX-IMVI, SW480, …) | top dose only |  |
| [[Larotrectinib (drug)]] 0.05 µM |  | **1.20×** | +3.5 | 0.019 | 8/49 (NCI-H1573, A549, …) | inconsistent across doses |  |
| [[Busulfan (drug)]] 0.05 µM |  | 1.20× | +3.4 | 0.019 | 8/48 (NCI-H1573, HOP62, …) | inconsistent across doses |  |
| [[Carbamazepine (drug)]] 5 µM |  | 1.19× | +3.3 | 0.033 | 12/47 (BT-474, A-172, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 5 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12776.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.702×** | -9.4 | 2e-18 | 28/48 (A498, SHP-77, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.638×** | -8.5 | 7e-15 | 33/47 (C32, RKO, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.613×** | -8.1 | 9e-14 | 33/48 (LOX-IMVI, SW48, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.460×** | -7.6 | 3e-12 | 33/43 (Hs 766T, A-427, …) | all doses, flat | cell-cycle shift (explains ~6% here); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.748×** | -5.5 | 5e-06 | 24/47 (RKO, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.758×** | -5.2 | 2e-05 | 28/48 (SK-MEL-2, A-427, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.592×** | -5.2 | 2e-05 | 26/48 (SNU-1, RKO, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.703×** | -4.7 | 2e-04 | 24/46 (SW480, A549, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.706×** | -4.7 | 2e-04 | 22/49 (LOX-IMVI, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **0.779×** | -4.5 | 3e-04 | 25/48 (AsPC-1, A-427, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.847× | -4.4 | 5e-04 | 24/48 (AsPC-1, RKO, …) | top dose only | composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.935× | -4.2 | 0.001 | 3/49 (MIA PaCa-2, H4, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.687×** | -3.7 | 0.009 | 22/49 (NCI-H23, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.829×** | -3.5 | 0.017 | 20/48 (RKO, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | 0.881× | -3.4 | 0.029 | 18/48 (SW480, SNU-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12776. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 59.0 | 3 (2 ⚠) | 4 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.00× (z +13.5) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 2.34× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.444× (z -11.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.314× (z -10.3) |
| [[NCI-H460 (line)]] | wt | 136 | 5 (5 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.51× (z +16.4) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.480× (z -11.6) |
| [[PANC-1 (line)]] | alt | 30.4 | 5 (3 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.64× (z +15.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 2.40× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.451× (z -11.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 59.0 | 1 (1 ⚠) | 6 (3 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.15× (z +10.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -14.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.380× (z -10.4) |
| [[J82 (line)]] | alt | 75.0 | 6 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.24× (z +13.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 2.37× (z +10.5) | — |
| [[A498 (line)]] | wt | 61.5 | 4 (4 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.87× (z +12.0) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.377× (z -12.7) |
| [[A-427 (line)]] | wt | 59.3 | 1 (1 ⚠) | 3 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.59× (z +11.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.424× (z -11.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.366× (z -8.8) |
| [[HS-578T (line)]] | alt | 25.8 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.30× (z +15.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 3.28× (z +8.9) | — |
| [[SW480 (line)]] | alt | 64.2 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.87× (z +10.6) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.541× (z -9.2) |
| [[AsPC-1 (line)]] | alt | 67.6 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.334× (z -14.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.396× (z -12.0) |
| [[C32 (line)]] | wt | 52.0 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.74× (z +8.7) ⚠ toxic; transcription drop | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.209× (z -10.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.284× (z -8.6) |
| [[HOP62 (line)]] | alt | 39.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.03× (z +12.6) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 29.5 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.48× (z +10.5) ⚠ toxic; transcription drop | [[Bortezomib (drug)]] 5 µM 0.0947× (z -8.7) ⚠ toxic |
| [[HT-29 (line)]] | alt | 41.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.52× (z +11.0) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 19.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.51× (z +9.8) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 39.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.22× (z +15.9) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 62.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.11× (z +12.9) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 147 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.56× (z +11.4) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.604× (z -8.8) |
| [[SNU-423 (line)]] | alt | 69.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.74× (z +13.3) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 70.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.50× (z +9.6) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 53.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.30× (z +11.5) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 58.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.83× (z +10.1) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 40.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.19× (z +12.1) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 106 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.14× (z +13.5) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 43.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.22× (z +10.9) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 48.5 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.01× (z +11.1) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.395× (z -10.5) |
| [[Panc 03.27 (line)]] | alt | 25.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.83× (z +11.4) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 28.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.39× (z +10.1) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 46.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.53× (z +11.7) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 45.2 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.113× (z -10.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 60.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.504× (z -8.5) |
| [[CFPAC-1 (line)]] | alt | 72.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.61× (z +8.8) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 91.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -12.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 31.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.76× (z +10.0) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 37.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.73× (z +9.5) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 63.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.408× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 27.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.17× (z +10.0) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 43.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.67× (z +8.6) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 43.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.355× (z -11.3) |
| [[SHP-77 (line)]] | alt | 59.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.362× (z -12.5) |
| [[SW 900 (line)]] | alt | 67.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.12× (z +9.6) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 33.0 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.0871× (z -12.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 25.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 50.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 57.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 54.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 49.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 30.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12776), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*30 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEMA3C]] | +0.57 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[SERBP1]] | +0.57 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[TPM4]] | +0.56 | +0.44 / +0.48 | both halves | 3e-05 |  |
| [[VMA21]] | +0.56 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[EIF1AX]] | +0.55 | +0.46 / +0.54 | both halves | 2e-05 |  |
| [[CORO1C]] | +0.55 | +0.36 / +0.54 | both halves | 1e-04 |  |
| [[SACS]] | +0.55 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[LINC00342]] | +0.54 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[AGPS]] | +0.53 | +0.35 / +0.62 | both halves | 1e-04 |  |
| [[OPN3]] | +0.53 | +0.47 / +0.59 | both halves | 2e-05 | STRING 974; ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[MMGT1]] | +0.52 | +0.37 / +0.53 | both halves | 9e-05 |  |
| [[THBS1]] | +0.52 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[SOAT1]] | +0.52 | +0.35 / +0.50 | both halves | 1e-04 |  |

## Genes that move opposite

*70 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COG7]] | -0.65 | -0.58 / -0.67 | both halves | 7e-06 |  |
| [[KBTBD4]] | -0.58 | -0.36 / -0.54 | both halves | 9e-05 |  |
| [[TMEM101]] | -0.58 | -0.46 / -0.55 | both halves | 2e-05 |  |
| [[BBS4]] | -0.57 | -0.52 / -0.59 | both halves | 1e-05 |  |
| [[KLC4]] | -0.56 | -0.46 / -0.58 | both halves | 2e-05 |  |
| [[ZRSR2]] | -0.55 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[CHURC1-FNTB]] | -0.55 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[TXNL4B]] | -0.55 | -0.39 / -0.49 | both halves | 5e-05 |  |
| [[AKAP17A]] | -0.54 | -0.42 / -0.55 | both halves | 4e-05 |  |
| [[ISCU]] | -0.54 | -0.43 / -0.55 | both halves | 3e-05 |  |
| [[ZNF547]] | -0.54 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[ZNF446]] | -0.53 | -0.29 / -0.60 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 041]] — Intra-Golgi and retrograde Golgi-to-ER traffic; 111 genes; this gene is in the **-** arm (projection on the module's main direction -0.427). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-51.0, -8.6); signed map (12.1, -4.3). **Vector** length 118, 33.9% of its response variance represented; |z| ≥ 3 in 1,330 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.6 | -1.7 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.4 | +8.1 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | +4.2 | +2.8 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.0 | +6.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.9 | +3.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.7 | +2.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.6 | +4.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.0 | +2.0 |
|  | [[Busulfan (drug)]] 0.05 µM |  | +2.5 | +3.4 |
|  | [[RMC-6236 (drug)]] 5 µM |  | +2.4 | +1.6 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -11.0 | -9.4 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -6.7 | -8.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.8 | -1.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -5.2 | -4.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -4.9 | -8.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.9 | -5.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.9 | -0.9 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | -3.5 | -1.5 |
|  | [[Thymol (drug)]] 0.5 µM |  | -3.1 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | CHM like Rab escort protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q43 — chr1:241,628,851-241,640,369 (-) |
| Ensembl biotype | protein_coding |
| Also known as | REP-2 |
| Gene groups (HGNC) | Rab geranylgeranyltransferase subunits |
| Reactome | 5 pathways, smallest: RAB geranylgeranylation; RAB GEFs exchange GTP for GDP on RABs; Rab regulation of trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [P26374](https://www.uniprot.org/uniprotkb/P26374) (Rab proteins geranylgeranyltransferase component A 2):

> Substrate-binding subunit (component A) of the Rab geranylgeranyltransferase (GGTase) complex. Binds unprenylated Rab proteins and presents the substrate peptide to the catalytic component B. The component A is thought to be regenerated by transferring its prenylated Rab back to the donor membrane. Less effective than CHM in supporting prenylation of Rab3 family.

**Summary**, from NCBI Gene [1122](https://www.ncbi.nlm.nih.gov/gene/1122):

> The product of the CHML gene supports geranylgeranylation of most Rab proteins and may substitute for REP-1 in tissues other than retina. CHML is localized close to the gene for Usher syndrome type II. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:1941](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1941) · Entrez [1122](https://www.ncbi.nlm.nih.gov/gene/1122) · UniProt [P26374](https://www.uniprot.org/uniprotkb/P26374) · Ensembl [ENSG00000203668](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000203668)

## Data

Gene col 12776: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12776); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12776, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12776]; `tensor/DDL_lfc|DDL_z.npy` [12776]; `embed/gene_vectors.npy` [12776]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12776 or target_col == 12776). Every well: [[CHML — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CHML.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
