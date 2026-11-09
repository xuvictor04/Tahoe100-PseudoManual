---
symbol: "NF2"
type: "gene"
col: 11831
ensembl_id: "ENSG00000186575"
name: "NF2, moesin-ezrin-radixin like (MERLIN) tumor suppressor"
location: "22q12.2"
module: 151
arm: "+"
pooled_cpm: 49.28
n_lines_expressing: 49
n_dd_up: 44
n_dd_down: 2
n_dd_up_clean: 19
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/151"]
generated_by: "tahoemap"
---

# NF2

*NF2, moesin-ezrin-radixin like (MERLIN) tumor suppressor* — 22q12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 44 drug-doses (25 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.74× (z +23.8, q 0e+00, up in 47 of 47 measured lines) ⚠ position correction uncertain. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 5.51× (z +21.1, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.931× (z -5.5, q 2e-05, down in 6 of 47 measured lines) ⚠ position not correctable. The strongest without an alert is [[Binimetinib (drug)]] 5 µM: 0.845× (z -4.0, q 0.013, down in 15 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 5 lines (RKO 0.367×, AsPC-1 0.258×, HEC-1-A 0.518×, A-172 0.385×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 2 lines (A-427 0.177×, RKO 0.272×; ⚠ cell-cycle shift, would explain all of this change); [[Adagrasib (drug)]] 0.05 µM in 2 lines (MIA PaCa-2 0.667×, NCI-H23 0.692×; ⚠ position not correctable); [[OTS514 (drug)]] 5 µM in 1 line (SNU-1 0.0612×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DDAH1]] (+0.65, fdr 7e-06), [[RUVBL1]] (+0.62, fdr 1e-05), [[ERCC2]] (+0.62, fdr 5e-05); moves opposite to [[RSRP1]] (-0.63, fdr 1e-05), [[TRA2A]] (-0.58, fdr 1e-05), [[ELF2]] (-0.56, fdr 1e-05).
> It is in [[Module 151]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 62 in all, 33 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 44 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 25 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11831.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ position correction uncertain | **2.74×** | +23.8 | 0e+00 | 47/47 (SW480, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ position correction uncertain | **2.55×** | +22.1 | 0e+00 | 46/47 (SW480, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[TAK-901 (drug)]] 5 µM |  | **5.51×** | +21.1 | 0e+00 | 46/48 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **2.32×** | +19.1 | 0e+00 | 32/39 (CFPAC-1, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.77×** | +19.0 | 0e+00 | 40/47 (A498, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **2.18×** | +18.4 | 0e+00 | 45/47 (SW480, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ position correction uncertain | **1.92×** | +15.4 | 0e+00 | 46/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Peretinoin (drug)]] 0.5 µM | ⚠ position correction uncertain | **1.79×** | +13.7 | 3e-41 | 39/46 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 5 µM | ⚠ position correction uncertain | **1.83×** | +13.7 | 3e-41 | 39/46 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.79×** | +13.7 | 5e-41 | 33/47 (MIA PaCa-2, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **1.75×** | +13.2 | 3e-38 | 29/46 (CFPAC-1, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.81×** | +12.8 | 1e-35 | 37/47 (SW480, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **1.67×** | +11.1 | 4e-27 | 29/44 (CFPAC-1, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.57×** | +10.6 | 1e-24 | 37/47 (Hs 766T, A549, …) | all doses, stronger at high dose | composition shift |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.55×** | +10.3 | 3e-23 | 36/46 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.53×** | +10.0 | 8e-22 | 34/47 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.32×** | +9.2 | 1e-18 | 32/47 (MIA PaCa-2, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.49×** | +9.1 | 3e-18 | 26/47 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.42×** | +8.3 | 3e-15 | 32/47 (NCI-H1573, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.88×** | +7.8 | 2e-13 | 33/47 (A549, SNU-423, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.31×** | +6.4 | 3e-09 | 25/47 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.31×** | +6.4 | 4e-09 | 24/47 (SW480, NCI-H2347, …) | top dose only |  |
| [[vincristine (drug)]] 5 µM |  | **1.50×** | +5.0 | 1e-05 | 21/45 (H4, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.15× | +4.7 | 4e-05 | 16/47 (HEC-1-A, LOX-IMVI, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.22×** | +4.3 | 2e-04 | 12/46 (HS-578T, NCI-H2347, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11831.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 5 lines (RKO 0.367×, AsPC-1 0.258×, HEC-1-A 0.518×, A-172 0.385×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 2 lines (A-427 0.177×, RKO 0.272×; ⚠ cell-cycle shift, would explain all of this change); [[Adagrasib (drug)]] 0.05 µM in 2 lines (MIA PaCa-2 0.667×, NCI-H23 0.692×; ⚠ position not correctable); [[OTS514 (drug)]] 5 µM in 1 line (SNU-1 0.0612×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.931× | -5.5 | 2e-05 | 6/47 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 5 µM |  | 0.845× | -4.0 | 0.013 | 15/47 (MIA PaCa-2, SK-MEL-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | 0.842× | -4.0 | 0.013 | 14/46 (NCI-H460, MIA PaCa-2, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.849× | -3.9 | 0.013 | 16/46 (A-172, SK-MEL-2, …) | rises with dose | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.893× | -3.8 | 0.014 | 18/47 (RKO, AsPC-1, …) | top dose only |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.800×** | -3.8 | 0.014 | 16/47 (Hs 766T, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | 0.895× | -3.8 | 0.014 | 13/47 (HEC-1-A, BT-474, …) | top dose only |  |
| [[Entrectinib (drug)]] 5 µM |  | 0.858× | -3.7 | 0.018 | 13/47 (KATO III, MIA PaCa-2, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.874× | -3.6 | 0.019 | 13/47 (MIA PaCa-2, Hs 766T, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | 0.863× | -3.5 | 0.022 | 13/47 (AsPC-1, NCI-H23, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | 0.903× | -3.5 | 0.027 | 11/48 (MIA PaCa-2, Hs 766T, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.831×** | -3.1 | 0.082 | 11/46 (A549, HOP62, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | 0.875× | -3.1 | 0.095 | 2/47 (NCI-H23, KATO III) | top dose only | plate-row cell shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11831. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 79.8 | 9 (6 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 11.2× (z +13.1) | — |
| [[HOP62 (line)]] | alt | 30.6 | 8 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.70× (z +18.8) | — |
| [[HS-578T (line)]] | alt | 44.9 | 8 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.36× (z +16.7) | — |
| [[SW480 (line)]] | alt | 50.9 | 8 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.43× (z +17.4) ⚠ position correction uncertain · without an alert: [[TAK-901 (drug)]] 5 µM 7.49× (z +14.9) | — |
| [[A549 (line)]] | wt | 36.1 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +14.0) | — |
| [[CFPAC-1 (line)]] | alt | 47.4 | 7 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.55× (z +15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.13× (z +9.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 91.6 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.99× (z +16.7) | — |
| [[A-427 (line)]] | wt | 33.3 | 5 (2 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.25× (z +11.1) ⚠ position correction uncertain · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.29× (z +10.9) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.177× (z -15.9) ⚠ cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 60.9 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.14× (z +19.6) | — |
| [[HEC-1-A (line)]] | alt | 84.9 | 3 (1 ⚠) | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.15× (z +9.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.518× (z -12.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 34.4 | 6 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.66× (z +13.2) ⚠ position correction uncertain · without an alert: [[Belinostat (drug)]] 5 µM 2.91× (z +10.9) | — |
| [[LS 180 (line)]] | wt | 33.8 | 5 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.55× (z +10.7) ⚠ position correction uncertain · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.44× (z +10.6) | — |
| [[NCI-H1573 (line)]] | alt | 34.9 | 5 (3 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 4.74× (z +12.0) ⚠ position correction uncertain · without an alert: [[TAK-901 (drug)]] 5 µM 13.4× (z +10.5) | — |
| [[NCI-H2347 (line)]] | alt | 26.0 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.83× (z +12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.01× (z +9.5) | — |
| [[SNU-423 (line)]] | alt | 59.9 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.16× (z +15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[Hs 766T (line)]] | wt | 59.9 | 4 (3 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 12.1× (z +11.0) | — |
| [[HT-29 (line)]] | alt | 49.2 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +13.4) | — |
| [[NCI-H1792 (line)]] | alt | 32.9 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.91× (z +12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[RKO (line)]] | wt | 103 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 5.69× (z +9.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.367× (z -15.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[hTERT-HPNE (line)]] | wt | 30.5 | 3 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.18× (z +9.2) ⚠ position correction uncertain · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.72× (z +9.1) | — |
| [[KATO III (line)]] | alt | 42.0 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.92× (z +13.2) ⚠ position correction uncertain | — |
| [[LOX-IMVI (line)]] | wt | 36.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.06× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[NCI-H460 (line)]] | wt | 70.9 | 2 (1 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 7.25× (z +12.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.574× (z -9.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW 900 (line)]] | alt | 45.8 | 3 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.89× (z +9.6) ⚠ position correction uncertain · without an alert: [[Belinostat (drug)]] 5 µM 2.55× (z +8.5) | — |
| [[A-172 (line)]] | wt | 37.1 | 1 | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 9.83× (z +9.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.385× (z -10.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 91.9 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.74× (z +9.0) ⚠ position correction uncertain | — |
| [[NCI-H2030 (line)]] | alt | 66.9 | 2 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 5.89× (z +9.4) | — |
| [[Panc 03.27 (line)]] | alt | 35.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.21× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[RPMI-7951 (line)]] | alt | 32.5 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.06× (z +9.3) ⚠ position correction uncertain | — |
| [[SNU-1 (line)]] | wt | 55.1 | 0 | 2 (1 ⚠) | — | [[OTS514 (drug)]] 5 µM 0.0612× (z -10.4) |
| [[AsPC-1 (line)]] | alt | 28.3 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.258× (z -12.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 25.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +9.2) | — |
| [[C-33 A (line)]] | alt | 59.7 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 8.02× (z +8.8) | — |
| [[C32 (line)]] | wt | 43.1 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.73× (z +10.7) | — |
| [[HCT15 (line)]] | alt | 64.8 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.00× (z +8.8) ⚠ position correction uncertain | — |
| [[NCI-H23 (line)]] | alt | 48.1 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 9.02× (z +9.9) | — |
| [[SHP-77 (line)]] | alt | 48.2 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.51× (z +8.6) ⚠ position correction uncertain | — |
| [[CHP-212 (line)]] | wt | 42.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 28.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 31.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.20 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 89.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 50.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 45.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 82.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 45.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11831), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DDAH1]] | +0.65 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[RUVBL1]] | +0.62 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[ERCC2]] | +0.62 | +0.40 / +0.66 | both halves | 5e-05 |  |
| [[DCBLD2]] | +0.61 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[FARSB]] | +0.61 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[AP1B1]] | +0.61 | +0.64 / +0.53 | both halves | 1e-05 | STRING 657 |
| [[DLC1]] | +0.60 | +0.58 / +0.49 | both halves | 1e-05 |  |
| [[LAS1L]] | +0.57 | +0.46 / +0.57 | both halves | 2e-05 |  |
| [[SMARCA4]] | +0.57 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[AGK]] | +0.57 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[CORO1C]] | +0.56 | +0.33 / +0.56 | both halves | 1e-04 |  |
| [[COA1]] | +0.56 | +0.48 / +0.56 | both halves | 2e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RSRP1]] | -0.63 | -0.53 / -0.61 | both halves | 1e-05 |  |
| [[TRA2A]] | -0.58 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[ELF2]] | -0.56 | -0.58 / -0.52 | both halves | 1e-05 |  |
| [[ARID4B]] | -0.56 | -0.38 / -0.55 | both halves | 6e-05 |  |
| [[IST1]] | -0.54 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[TXNL4B]] | -0.54 | -0.30 / -0.55 | both halves | 2e-04 |  |
| [[CLK1]] | -0.54 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[MKRN1]] | -0.54 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[DNAJB9]] | -0.53 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[GTF2B]] | -0.53 | -0.44 / -0.54 | both halves | 3e-05 |  |
| [[CCDC115]] | -0.53 | -0.37 / -0.57 | both halves | 8e-05 |  |
| [[PIK3CA]] | -0.53 | -0.57 / -0.42 | both halves | 4e-05 | pathway: Fcgamma receptor (FCGR) dependent phagocytosis; STRING 570 |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 151]]; 29 genes; every member is in the + arm (projection on the module's main direction 0.565). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-3.6, -40.3); signed map (-6.5, 33.5). **Vector** length 112, 31.5% of its response variance represented; |z| ≥ 3 in 1,484 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | +10.1 | +19.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | +9.7 | +13.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | +9.3 | +21.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | +7.6 | +11.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +6.7 | +12.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +5.8 | +9.2 |
|  | [[Peretinoin (drug)]] 5 µM | ⚠ position correction uncertain | +5.5 | +13.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +5.3 | +8.3 |
|  | [[Peretinoin (drug)]] 0.5 µM | ⚠ position correction uncertain | +4.9 | +13.7 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.6 | -3.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.3 | -1.0 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | -2.9 | -3.8 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.8 | -3.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -2.7 | +0.2 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.3 | -1.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.2 | -3.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.1 | -1.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.1 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | NF2, moesin-ezrin-radixin like (MERLIN) tumor suppressor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q12.2 — chr22:29,603,553-29,698,598 (+) |
| Ensembl biotype | protein_coding |
| Also known as | merlin, ACN, SCH, BANF, merlin-1 |
| Gene groups (HGNC) | A-kinase anchoring proteins; FERM domain containing |
| Hallmark sets | SPERMATOGENESIS, APICAL_JUNCTION |
| Reactome | 7 pathways, smallest: RHO GTPases activate PAKs; Regulation of actin dynamics for phagocytic cup formation; Fcgamma receptor (FCGR) dependent phagocytosis |
| Matched by | ensembl_id |

**Function**, from UniProt [P35240](https://www.uniprot.org/uniprotkb/P35240) (Merlin):

> Probable regulator of the Hippo/SWH (Sav/Wts/Hpo) signaling pathway, a signaling pathway that plays a pivotal role in tumor suppression by restricting proliferation and promoting apoptosis. Along with WWC1 can synergistically induce the phosphorylation of LATS1 and LATS2 and can probably function in the regulation of the Hippo/SWH (Sav/Wts/Hpo) signaling pathway. May act as a membrane stabilizing protein. May inhibit PI3 kinase by binding to AGAP2 and impairing its stimulating activity. …

**Summary**, from NCBI Gene [4771](https://www.ncbi.nlm.nih.gov/gene/4771):

> This gene encodes a protein that is similar to some members of the ERM (ezrin, radixin, moesin) family of proteins that link cytoskeletal components with proteins in the cell membrane. The encoded protein is involved in regulation of contact-dependent inhibition of cell proliferation and functions in cell-cell adhesion and transmembrane signaling. The encoded protein has been shown to interact with cell-surface proteins, proteins involved in cytoskeletal dynamics, and proteins involved in …

**Accessions** — [HGNC:7773](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7773) · Entrez [4771](https://www.ncbi.nlm.nih.gov/gene/4771) · UniProt [P35240](https://www.uniprot.org/uniprotkb/P35240) · Ensembl [ENSG00000186575](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000186575)

## Data

Gene col 11831: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11831); `tables/drug_effects.parquet` (75 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11831, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11831]; `tensor/DDL_lfc|DDL_z.npy` [11831]; `embed/gene_vectors.npy` [11831]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11831 or target_col == 11831). Every well: [[NF2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NF2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
