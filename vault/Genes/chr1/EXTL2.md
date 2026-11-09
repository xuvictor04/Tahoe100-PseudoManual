---
symbol: "EXTL2"
type: "gene"
col: 8563
ensembl_id: "ENSG00000162694"
name: "exostosin like glycosyltransferase 2"
location: "1p21.2"
module: 92
arm: "+"
pooled_cpm: 20.16
n_lines_expressing: 50
n_dd_up: 36
n_dd_down: 29
n_dd_up_clean: 24
n_dd_down_clean: 24
in_vector_space: true
direction_upstream: 8
direction_downstream: 0
tags: ["gene", "module/092"]
generated_by: "tahoemap"
---

# EXTL2

*exostosin like glycosyltransferase 2* — 1p21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 36 drug-doses (12 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.03× (z +30.9, q 0e+00, up in 46 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (5 with an alert ⚠); the strongest is [[Trametinib (drug)]] 5 µM: 0.656× (z -6.9, q 4e-09, down in 28 of 48 measured lines) ⚠ cell-cycle shift, explains ~38% of this change. The strongest without an alert is [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM: 0.662× (z -6.4, q 3e-08, down in 24 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPRED1]] (+0.75, fdr 7e-06), [[ETV1]] (+0.68, fdr 1e-05), [[EGR3]] (+0.66, fdr 7e-06); moves opposite to [[ARL8A]] (-0.56, fdr 1e-05), [[MIR193BHG]] (-0.55, fdr 2e-05), [[NPEPPS]] (-0.54, fdr 2e-05).
> It is in [[Module 092]], a single-armed module (MAPK output).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[LINC02320]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 41 in all, 12 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 36 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8563.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.03×** | +30.9 | 0e+00 | 46/47 (Hs 766T, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.50×** | +20.4 | 0e+00 | 37/47 (A-172, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **3.09×** | +17.1 | 0e+00 | 38/48 (A-172, PANC-1, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **2.59×** | +14.9 | 0e+00 | 39/48 (MIA PaCa-2, A498, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | **2.57×** | +14.8 | 0e+00 | 35/44 (LoVo, LOX-IMVI, …) | all doses, flat | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **2.56×** | +14.8 | 0e+00 | 40/47 (A498, J82, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **2.46×** | +14.2 | 1e-43 | 39/48 (A498, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **2.37×** | +13.0 | 7e-37 | 37/46 (HS-578T, SW480, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.29×** | +13.0 | 7e-37 | 42/48 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.70×** | +11.8 | 3e-30 | 40/48 (A498, NCI-H460, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.91×** | +9.8 | 6e-21 | 37/48 (C32, HS-578T, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.83×** | +9.5 | 1e-19 | 29/47 (A-172, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | **1.91×** | +9.4 | 2e-19 | 28/39 (HOP62, MIA PaCa-2, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change | **1.82×** | +9.1 | 5e-18 | 20/34 (A-172, LoVo, …) | all doses, flat | composition shift |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.73×** | +8.6 | 3e-16 | 37/47 (HEC-1-A, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.44×** | +8.2 | 1e-14 | 33/48 (Hs 766T, HOP62, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.59×** | +7.3 | 9e-12 | 32/48 (A498, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.36×** | +7.0 | 6e-11 | 29/48 (A498, Hs 766T, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.26×** | +5.2 | 6e-06 | 20/48 (NCI-H2347, A498, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.31×** | +4.3 | 6e-04 | 16/48 (NCI-H1573, NCI-H460, …) | all doses, flat |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.31×** | +4.2 | 7e-04 | 13/48 (LoVo, HOP62, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.05 µM |  | **1.30×** | +3.9 | 0.002 | 7/48 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses |  |
| [[Naproxen (drug)]] 0.5 µM |  | **1.24×** | +3.4 | 0.014 | 7/48 (NCI-H23, RKO, …) | all doses, flat | position effect removed |
| [[Lactate (calcium) (drug)]] 0.05 µM |  | **1.24×** | +3.4 | 0.017 | 8/48 (LOX-IMVI, NCI-H1573, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8563.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.656×** | -6.9 | 4e-09 | 28/48 (A-427, NCI-H23, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.662×** | -6.4 | 3e-08 | 24/48 (A-427, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.652×** | -6.4 | 3e-08 | 29/47 (RKO, AN3 CA, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.654×** | -6.3 | 5e-08 | 26/48 (A-427, SK-MEL-2, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.734×** | -6.0 | 3e-07 | 28/48 (A-427, NCI-H1573, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.686×** | -5.9 | 4e-07 | 27/47 (A-427, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 5 µM |  | **0.714×** | -5.7 | 8e-07 | 25/48 (A-427, SNU-1, …) | rises with dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.774×** | -5.6 | 1e-06 | 28/48 (RKO, HT-29, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.698×** | -5.6 | 1e-06 | 25/47 (SHP-77, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.699×** | -5.4 | 5e-06 | 21/47 (A-427, NCI-H23, …) | all doses, stronger at high dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.715×** | -5.2 | 9e-06 | 22/47 (HS-578T, NCI-H1573, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.730×** | -4.9 | 5e-05 | 18/48 (A-427, AN3 CA, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.742×** | -4.6 | 2e-04 | 20/48 (SW480, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.756×** | -4.4 | 5e-04 | 16/46 (CHP-212, NCI-H1573, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.758×** | -4.3 | 6e-04 | 20/48 (HT-29, NCI-H23, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.760×** | -4.3 | 7e-04 | 21/47 (RKO, NCI-H2030, …) | rises with dose | low cells (technical?) |
| [[RMC-6236 (drug)]] 5 µM |  | **0.595×** | -4.2 | 8e-04 | 16/47 (A-427, NCI-H23, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.776×** | -3.9 | 0.003 | 17/47 (SW480, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.781×** | -3.8 | 0.004 | 15/48 (SW480, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.80 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8563. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 22.0 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.3× (z +21.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 16.6 | 6 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.45× (z +17.7) | — |
| [[A498 (line)]] | wt | 13.0 | 5 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.90× (z +13.6) | — |
| [[A-427 (line)]] | wt | 50.9 | 0 | 4 (1 ⚠) | — | [[Trametinib (drug)]] 5 µM 0.326× (z -9.9) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Cobimetinib (drug)]] 5 µM 0.319× (z -9.6) |
| [[Hs 766T (line)]] | wt | 18.9 | 3 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.2× (z +20.3) | [[Rapamycin (drug)]] 0.5 µM 0.197× (z -9.8) |
| [[J82 (line)]] | alt | 16.2 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.58× (z +15.0) | — |
| [[SNU-423 (line)]] | alt | 11.1 | 3 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.98× (z +12.5) | [[Bosentan (hydrate) (drug)]] 5 µM 0.0669× (z -11.9) |
| [[A549 (line)]] | wt | 9.63 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.80× (z +11.6) | — |
| [[C32 (line)]] | wt | 15.5 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.75× (z +15.0) | — |
| [[HEC-1-A (line)]] | alt | 22.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +12.3) | — |
| [[HS-578T (line)]] | alt | 27.4 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.94× (z +17.1) | — |
| [[NCI-H460 (line)]] | wt | 15.5 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.75× (z +12.2) | — |
| [[PANC-1 (line)]] | alt | 22.1 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.15× (z +13.9) | — |
| [[SK-MEL-2 (line)]] | alt | 45.5 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.28× (z +13.4) | — |
| [[SW480 (line)]] | alt | 29.4 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.13× (z +16.9) | — |
| [[AsPC-1 (line)]] | alt | 9.12 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.49× (z +13.8) | — |
| [[CFPAC-1 (line)]] | alt | 10.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.10× (z +15.7) | — |
| [[HT-29 (line)]] | alt | 16.0 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.64× (z +10.4) | — |
| [[LoVo (line)]] | wt | 12.9 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.03× (z +14.4) | — |
| [[LOX-IMVI (line)]] | wt | 35.0 | 2 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 3.09× (z +8.7) | — |
| [[NCI-H1573 (line)]] | alt | 19.2 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.30× (z +16.2) | — |
| [[NCI-H1792 (line)]] | alt | 10.1 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.49× (z +12.4) | — |
| [[NCI-H23 (line)]] | alt | 32.2 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.59× (z +10.3) | [[Dinaciclib (drug)]] 0.05 µM 0.222× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change |
| [[NCI-H2347 (line)]] | alt | 5.17 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.09× (z +13.9) | — |
| [[Panc 03.27 (line)]] | alt | 10.3 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.19× (z +12.2) | — |
| [[BT-474 (line)]] | alt | 6.34 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.8× (z +12.0) | — |
| [[C-33 A (line)]] | alt | 50.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.273× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change |
| [[HepG2_C3A (line)]] | wt | 19.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.36× (z +10.3) | — |
| [[HOP62 (line)]] | alt | 10.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.60× (z +12.0) | — |
| [[hTERT-HPNE (line)]] | wt | 24.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.82× (z +11.9) | — |
| [[KATO III (line)]] | alt | 7.10 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.18× (z +8.6) | — |
| [[RPMI-7951 (line)]] | alt | 27.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.49× (z +12.5) | — |
| [[SHP-77 (line)]] | alt | 35.1 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.311× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 22.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.29× (z +10.5) | — |
| [[SW 900 (line)]] | alt | 13.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.51× (z +13.5) | — |
| [[SW1417 (line)]] | alt | 14.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.60× (z +13.4) | — |
| [[AN3 CA (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.28 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 25.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 61.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 21.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8563), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPRED1]] | +0.75 | +0.63 / +0.75 | both halves | 7e-06 |  |
| [[ETV1]] | +0.68 | +0.55 / +0.71 | both halves | 1e-05 |  |
| [[EGR3]] | +0.66 | +0.60 / +0.68 | both halves | 7e-06 |  |
| [[EGR2]] | +0.63 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[ETV4]] | +0.62 | +0.47 / +0.64 | both halves | 2e-05 |  |
| [[EGR1]] | +0.61 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[B4GALT6]] | +0.60 | +0.48 / +0.63 | both halves | 2e-05 | pathway: Glycosaminoglycan metabolism |
| [[SPRY2]] | +0.60 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[KBTBD2]] | +0.60 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[EPB41L2]] | +0.59 | +0.47 / +0.62 | both halves | 2e-05 |  |
| [[SPRY4]] | +0.59 | +0.41 / +0.59 | both halves | 4e-05 |  |
| [[PLEKHG2]] | +0.58 | +0.51 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARL8A]] | -0.56 | -0.59 / -0.52 | both halves | 1e-05 |  |
| [[MIR193BHG]] | -0.55 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[NPEPPS]] | -0.54 | -0.64 / -0.47 | both halves | 2e-05 |  |
| [[CRYZL1]] | -0.54 | -0.55 / -0.44 | both halves | 3e-05 |  |
| [[SELENOO]] | -0.54 | -0.38 / -0.47 | both halves | 7e-05 |  |
| [[CIAO3]] | -0.53 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[TOM1]] | -0.52 | -0.48 / -0.54 | both halves | 2e-05 |  |
| [[STK38]] | -0.52 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[ELMOD3]] | -0.52 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[SDHAP1-1]] | -0.51 | -0.50 / -0.40 | both halves | 5e-05 |  |
| [[ULK1]] | -0.51 | -0.60 / -0.43 | both halves | 3e-05 |  |
| [[FTL]] | -0.51 | -0.55 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02320]] | B | LINC02320 activity lowers EXTL2's level | lines that do not express LINC02320 (19) vs lines expressing it (31) | 1.55× higher at baseline in the lines without LINC02320 | 0.005 | ⚠ within organs, on part of the lines; also absent: ENSG00000258919, TSPAN1, ENSG00000266088 |
| [[EREG]] | B | EREG activity lowers EXTL2's level | lines that do not express EREG (26) vs lines expressing it (24) | 1.41× higher at baseline in the lines without EREG | 0.008 | ⚠ within organs, on part of the lines; also absent: DPP4, IL20RA, HS3ST1 |
| [[TGFBR2]] | B | TGFBR2 activity lowers EXTL2's level | lines that do not express TGFBR2 (7) vs lines expressing it (43) | 1.89× higher at baseline in the lines without TGFBR2 | 0.035 | ⚠ within organs, on part of the lines; also absent: VDR, TRIB1, MET |
| [[STAMBPL1]] | B | STAMBPL1 activity lowers EXTL2's level | lines that do not express STAMBPL1 (6) vs lines expressing it (44) | 1.87× higher at baseline in the lines without STAMBPL1 | 0.044 | ⚠ within organs, on part of the lines; also absent: CFAP45, PMAIP1, OCIAD2 |
| [[SYNE3]] | B | SYNE3 activity lowers EXTL2's level | lines that do not express SYNE3 (11) vs lines expressing it (39) | 1.55× higher at baseline in the lines without SYNE3 | 0.055 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers EXTL2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.3% of all compounds | 0.065 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ARHGAP18]] | B | ARHGAP18 activity lowers EXTL2's level | lines that do not express ARHGAP18 (6) vs lines expressing it (44) | 1.88× higher at baseline in the lines without ARHGAP18 | 0.090 | ⚠ within organs, on part of the lines; also absent: IER3, SLC2A1, SHB |
| [[MAP2K1]] | B | MAP2K1 activity raises EXTL2's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.8% of all compounds | 0.0995 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 092]] — MAPK output; 49 genes; every member is in the + arm (projection on the module's main direction 0.677). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (44.2, 7.3); signed map (9.5, 47.7). **Vector** length 99.0, 26.2% of its response variance represented; |z| ≥ 3 in 1,424 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MAPK output* (control, mean cos +0.60 to 8); *MAPK family signaling cascades* (reactome, mean cos +0.52 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +5.6 | +17.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.3 | +11.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.7 | +7.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.6 | +30.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.2 | +20.4 |
|  | [[Bentamapimod (drug)]] 5 µM |  | +2.9 | +3.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.9 | +8.2 |
|  | [[Ipatasertib (drug)]] 0.05 µM |  | +2.3 | +3.9 |
|  | [[Ipatasertib (drug)]] 5 µM |  | +2.2 | +2.3 |
| fall | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -5.7 | -6.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -5.6 | -5.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -5.4 | -6.0 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | -5.2 | -6.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -5.0 | -6.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -5.0 | -6.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | -4.8 | -5.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -4.8 | -5.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.5 | -5.6 |

## What is on record

|  |  |
|---|---|
| Name | exostosin like glycosyltransferase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p21.2 — chr1:100,872,372-100,895,179 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Exostosin glycosyltransferase family |
| Reactome | 9 pathways, smallest: HS-GAG biosynthesis; Heparan sulfate/heparin (HS-GAG) metabolism; XBP1(S) activates chaperone genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UBQ6](https://www.uniprot.org/uniprotkb/Q9UBQ6) (Exostosin-like 2):

> Glycosyltransferase required for the biosynthesis of heparan-sulfate and responsible for the alternating addition of beta-1-4-linked glucuronic acid (GlcA) and alpha-1-4-linked N-acetylglucosamine (GlcNAc) units to nascent heparan sulfate chains.

**Summary**, from NCBI Gene [2135](https://www.ncbi.nlm.nih.gov/gene/2135):

> Enables alpha-1,4-N-acetylgalactosaminyltransferase activity and glucuronyl-galactosyl-proteoglycan 4-alpha-N-acetylglucosaminyltransferase activity. Involved in N-acetylglucosamine metabolic process and UDP-N-acetylgalactosamine metabolic process. Located in endoplasmic reticulum. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:3516](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3516) · Entrez [2135](https://www.ncbi.nlm.nih.gov/gene/2135) · UniProt [Q9UBQ6](https://www.uniprot.org/uniprotkb/Q9UBQ6) · Ensembl [ENSG00000162694](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162694)

## Data

Gene col 8563: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8563); `tables/drug_effects.parquet` (71 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8563, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8563]; `tensor/DDL_lfc|DDL_z.npy` [8563]; `embed/gene_vectors.npy` [8563]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8563 or target_col == 8563). Every well: [[EXTL2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EXTL2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
