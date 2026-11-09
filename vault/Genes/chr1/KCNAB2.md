---
symbol: "KCNAB2"
type: "gene"
col: 917
ensembl_id: "ENSG00000069424"
name: "potassium voltage-gated channel subfamily A regulatory beta subunit 2"
location: "1p36.31"
module: 72
arm: "+"
pooled_cpm: 21.31
n_lines_expressing: 48
n_dd_up: 18
n_dd_down: 23
n_dd_up_clean: 12
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/072"]
generated_by: "tahoemap"
---

# KCNAB2

*potassium voltage-gated channel subfamily A regulatory beta subunit 2* — 1p36.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.76× (z +29.0, q 0e+00, up in 38 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (9 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.623× (z -9.2, q 2e-17, down in 24 of 45 measured lines) ⚠ cell-cycle shift, explains ~38% of this change. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.638× (z -9.1, q 3e-17, down in 29 of 46 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GGA2]] (+0.53, fdr 1e-04), [[CHRNA5]] (+0.52, fdr 1e-05), [[KATNB1]] (+0.52, fdr 3e-05); moves opposite to [[APLF]] (-0.51, fdr 1e-04), [[DHRS12]] (-0.48, fdr 2e-04), [[LIG4]] (-0.48, fdr 4e-04).
> It is in [[Module 072]], a single-armed module (Degradation of DVL).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[LINC01237]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 9 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 917.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.76×** | +29.0 | 0e+00 | 38/43 (A549, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **2.47×** | +18.3 | 0e+00 | 36/46 (NCI-H2030, HT-29, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.41×** | +17.8 | 0e+00 | 36/46 (HEC-1-A, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **2.12×** | +15.2 | 0e+00 | 36/46 (NCI-H2030, PANC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.81×** | +11.3 | 1e-27 | 25/43 (COLO 205, A-172, …) | all doses, flat | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.62×** | +9.7 | 2e-20 | 30/46 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.61×** | +9.6 | 9e-20 | 30/46 (HOP62, NCI-H1573, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.53×** | +8.6 | 5e-16 | 25/46 (HOP62, HT-29, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.49×** | +8.1 | 4e-14 | 28/43 (HT-29, HOP62, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.99×** | +7.3 | 2e-11 | 23/46 (PANC-1, Hs 766T, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.41×** | +7.0 | 1e-10 | 22/46 (SW480, HOP62, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.34×** | +5.8 | 4e-07 | 15/44 (HT-29, HEC-1-A, …) | top dose only |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~17% of this change | **1.32×** | +5.6 | 7e-07 | 15/46 (RKO, SK-MEL-2, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **1.32×** | +5.4 | 3e-06 | 20/45 (HS-578T, MIA PaCa-2, …) | top dose only |  |
| [[Afatinib (drug)]] 5 µM |  | **1.28×** | +5.2 | 6e-06 | 11/45 (SW48, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.26×** | +4.6 | 1e-04 | 13/45 (KATO III, SK-MEL-2, …) | two highest doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.15× | +3.9 | 0.003 | 14/46 (HOP62, LoVo, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.14× | +3.7 | 0.008 | 14/46 (HOP62, A-172, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | 1.19× | +3.5 | 0.013 | 3/46 (SW48, LoVo, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.19× | +3.5 | 0.014 | 9/46 (KATO III, LS 180, …) | two highest doses |  |
| [[Radotinib (drug)]] 5 µM |  | 1.12× | +3.3 | 0.026 | 8/46 (AsPC-1, LoVo, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 917.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.623×** | -9.2 | 2e-17 | 24/45 (SW480, RKO, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.638×** | -9.1 | 3e-17 | 29/46 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.666×** | -8.2 | 4e-14 | 25/44 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.723×** | -6.6 | 8e-09 | 16/46 (RKO, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.799×** | -6.4 | 2e-08 | 21/46 (CFPAC-1, H4, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.722×** | -6.3 | 2e-08 | 18/42 (SNU-423, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.731×** | -6.3 | 2e-08 | 20/41 (RKO, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.732×** | -6.3 | 2e-08 | 17/46 (SNU-423, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.739×** | -5.9 | 3e-07 | 17/43 (SW48, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.751×** | -5.8 | 5e-07 | 16/46 (hTERT-HPNE, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.758×** | -5.6 | 1e-06 | 18/46 (LS 180, H4, …) | all doses, stronger at high dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.757×** | -5.4 | 3e-06 | 13/46 (NCI-H23, AsPC-1, …) | top dose only |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.763×** | -5.2 | 7e-06 | 22/44 (COLO 205, LoVo, …) | rises with dose | position effect removed |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.775×** | -5.1 | 1e-05 | 15/45 (SNU-423, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.795×** | -4.6 | 1e-04 | 15/45 (CFPAC-1, H4, …) | rises with dose | position effect removed |
| [[Crizotinib (hydrochloride) (drug)]] 5 µM |  | 0.842× | -3.5 | 0.016 | 4/46 (SW48, NCI-H460, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.843× | -3.4 | 0.016 | 13/43 (COLO 205, CFPAC-1, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.726×** | -3.4 | 0.020 | 13/46 (A-427, NCI-H23, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.741×** | -3.2 | 0.039 | 6/43 (SNU-1, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Sonidegib (drug)]] 0.5 µM |  | **0.805×** | -3.1 | 0.043 | 7/43 (NCI-H23, H4, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Fulvestrant (drug)]] 0.05 µM |  | 0.868× | -2.9 | 0.090 | 2/46 (NCI-H23, HEC-1-A) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.49 per unit of S-phase module lfc, -0.48 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 917. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 20.8 | 18 | 1 | [[Budesonide (drug)]] 0.5 µM 4.85× (z +13.3) | [[Harringtonine (drug)]] 0.5 µM 0.356× (z -8.7) |
| [[SW480 (line)]] | alt | 38.7 | 1 | 6 (5 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.20× (z +11.5) | [[Harringtonine (drug)]] 5 µM 0.270× (z -13.0) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.334× (z -11.3) |
| [[PANC-1 (line)]] | alt | 27.7 | 2 (1 ⚠) | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.11× (z +11.0) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.297× (z -12.7) |
| [[RKO (line)]] | wt | 71.1 | 1 | 4 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.90× (z +8.9) | [[Dinaciclib (drug)]] 0.5 µM 0.151× (z -18.7) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.392× (z -9.3) |
| [[HEC-1-A (line)]] | alt | 12.2 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.52× (z +13.5) | — |
| [[HepG2_C3A (line)]] | wt | 39.6 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +10.6) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 5 µM 0.254× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 25.6 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.51× (z +10.7) | — |
| [[Hs 766T (line)]] | wt | 16.0 | 2 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.80× (z +10.6) | [[Dinaciclib (drug)]] 5 µM 0.205× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HT-29 (line)]] | alt | 14.8 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.63× (z +13.3) | — |
| [[NCI-H1792 (line)]] | alt | 14.0 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +9.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.08× (z +8.6) | [[Digitoxin (drug)]] 5 µM 0.204× (z -8.6) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 29.5 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.08× (z +9.2) | [[Dinaciclib (drug)]] 0.05 µM 0.153× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 16.9 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.33× (z +10.0) | — |
| [[hTERT-HPNE (line)]] | wt | 12.3 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.125× (z -9.3) |
| [[MIA PaCa-2 (line)]] | alt | 13.0 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.11× (z +9.1) | [[Dinaciclib (drug)]] 0.05 µM 0.109× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 7.27 | 2 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 7.24× (z +9.5) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.71× (z +8.9) | — |
| [[NCI-H23 (line)]] | alt | 18.2 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.260× (z -12.2) ⚠ cell-cycle shift, would explain all of this change |
| [[RPMI-7951 (line)]] | alt | 24.0 | 0 | 2 (1 ⚠) | — | [[Bergenin (drug)]] 0.5 µM 0.0970× (z -12.9) |
| [[SK-MEL-2 (line)]] | alt | 51.5 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.20× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.226× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 60.1 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.165× (z -12.5) ⚠ toxic |
| [[A-172 (line)]] | wt | 7.85 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.94× (z +10.5) | — |
| [[A498 (line)]] | wt | 9.24 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.76× (z +10.1) | — |
| [[A549 (line)]] | wt | 7.74 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.51× (z +14.3) | — |
| [[COLO 205 (line)]] | alt | 70.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +10.3) ⚠ cell-cycle shift, would explain all of this change | — |
| [[KATO III (line)]] | alt | 26.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.30× (z +8.8) | — |
| [[LoVo (line)]] | wt | 9.31 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.23× (z +8.8) | — |
| [[LOX-IMVI (line)]] | wt | 43.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.338× (z -14.8) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H1573 (line)]] | alt | 8.84 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 6.80× (z +8.7) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[SHP-77 (line)]] | alt | 39.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.231× (z -11.7) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 21.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.183× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW48 (line)]] | wt | 30.9 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.162× (z -9.9) |
| [[A-427 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.75 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.25 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.38 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 25.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.77 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.01 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.88 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 44.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 21.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 917), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GGA2]] | +0.53 | +0.33 / +0.58 | both halves | 1e-04 |  |
| [[CHRNA5]] | +0.52 | +0.52 / +0.52 | both halves | 1e-05 | pathway: Neuronal System |
| [[KATNB1]] | +0.52 | +0.45 / +0.47 | both halves | 3e-05 |  |
| [[POM121]] | +0.52 | +0.26 / +0.52 | both halves | 4e-04 | STRING 468 |
| [[TFR2]] | +0.51 | +0.36 / +0.58 | both halves | 9e-05 |  |
| [[MBOAT7]] | +0.51 | +0.38 / +0.45 | both halves | 7e-05 |  |
| [[EPS15L1]] | +0.50 | +0.53 / +0.41 | both halves | 4e-05 |  |
| [[CCDC32]] | +0.50 | +0.46 / +0.47 | both halves | 3e-05 |  |
| [[EARS2]] | +0.49 | +0.41 / +0.48 | both halves | 4e-05 |  |
| [[WNK2]] | +0.49 | +0.35 / +0.48 | both halves | 1e-04 |  |
| [[OGFOD3]] | +0.49 | +0.42 / +0.42 | both halves | 4e-05 |  |
| [[TNPO3]] | +0.48 | +0.30 / +0.44 | both halves | 2e-04 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[APLF]] | -0.51 | -0.32 / -0.46 | both halves | 1e-04 |  |
| [[DHRS12]] | -0.48 | -0.30 / -0.44 | both halves | 2e-04 |  |
| [[LIG4]] | -0.48 | -0.24 / -0.53 | both halves | 4e-04 |  |
| [[RO60]] | -0.48 | -0.39 / -0.50 | both halves | 5e-05 |  |
| [[RC3H2]] | -0.47 | -0.26 / -0.57 | both halves | 4e-04 |  |
| [[KRTAP5-AS1]] | -0.47 | -0.30 / -0.48 | both halves | 2e-04 |  |
| [[MYEF2]] | -0.47 | -0.30 / -0.45 | both halves | 2e-04 |  |
| [[CUTALP]] | -0.47 | -0.28 / -0.41 | both halves | 3e-04 |  |
| [[PHF20L1]] | -0.47 | -0.38 / -0.47 | both halves | 7e-05 |  |
| [[YWHAH]] | -0.46 | -0.26 / -0.55 | both halves | 4e-04 |  |
| [[CCDC92]] | -0.46 | -0.38 / -0.40 | both halves | 7e-05 |  |
| [[CREB1]] | -0.46 | -0.29 / -0.45 | both halves | 2e-04 | pathway: Neuronal System |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01237]] | B | LINC01237 activity raises KCNAB2's level | lines that do not express LINC01237 (7) vs lines expressing it (43) | 1.05× lower at baseline in the lines without LINC01237 | 0.052 | ⚠ within organs, on part of the lines; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 072]] — Degradation of DVL; 69 genes; every member is in the + arm (projection on the module's main direction 0.477). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-13.4, -8.3); signed map (-56.0, -12.4). **Vector** length 78.3, 14.9% of its response variance represented; |z| ≥ 3 in 1,254 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | +6.3 | +9.6 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +5.5 | +11.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.1 | +8.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.0 | +29.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.8 | +7.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.4 | +3.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.2 | +3.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.7 | +3.3 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -4.5 | -9.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -4.4 | -0.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~84% of this change | -4.0 | -4.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.2 | -6.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -3.1 | -6.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.7 | -3.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.6 | -6.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.4 | -5.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.3 | -1.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.2 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | potassium voltage-gated channel subfamily A regulatory beta subunit 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.31 — chr1:5,990,927-6,101,193 (+) |
| Ensembl biotype | protein_coding |
| Also known as | AKR6A5, KCNA2B, HKvbeta2.1, HKvbeta2.2 |
| Gene groups (HGNC) | Aldo-keto reductases; Potassium voltage-gated channel regulatory subunits |
| Reactome | 5 pathways, smallest: Voltage gated Potassium channels; Potassium Channels; Neuronal System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13303](https://www.uniprot.org/uniprotkb/Q13303) (Voltage-gated potassium channel subunit beta-2):

> Regulatory subunit of the voltage-gated potassium (Kv) Shaker channels composed of pore-forming and potassium-conducting alpha subunits and of regulatory beta subunits. The beta-2/KCNAB2 cytoplasmic subunit promotes potassium channel closure via a mechanism that does not involve physical obstruction of the channel pore. Promotes the inactivation of Kv1.4/KCNA4 and Kv1.5/KCNA5 alpha subunit-containing channels. Displays nicotinamide adenine dinucleotide phosphate (NADPH)-dependent …

**Summary**, from NCBI Gene [8514](https://www.ncbi.nlm.nih.gov/gene/8514):

> Voltage-gated potassium (Kv) channels represent the most complex class of voltage-gated ion channels from both functional and structural standpoints. Their diverse functions include regulating neurotransmitter release, heart rate, insulin secretion, neuronal excitability, epithelial electrolyte transport, smooth muscle contraction, and cell volume. Four sequence-related potassium channel genes - shaker, shaw, shab, and shal - have been identified in Drosophila, and each has been shown to have …

**Accessions** — [HGNC:6229](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6229) · Entrez [8514](https://www.ncbi.nlm.nih.gov/gene/8514) · UniProt [Q13303](https://www.uniprot.org/uniprotkb/Q13303) · Ensembl [ENSG00000069424](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000069424)

## Data

Gene col 917: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 917); `tables/drug_effects.parquet` (59 rows, flagged included); `relations/gene_relations.parquet` (col_a == 917, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 917]; `tensor/DDL_lfc|DDL_z.npy` [917]; `embed/gene_vectors.npy` [917]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 917 or target_col == 917). Every well: [[KCNAB2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KCNAB2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
