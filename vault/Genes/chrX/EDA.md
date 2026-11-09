---
symbol: "EDA"
type: "gene"
col: 8194
ensembl_id: "ENSG00000158813"
name: "ectodysplasin A"
location: "Xq13.1"
module: 23
arm: "-"
pooled_cpm: 27.81
n_lines_expressing: 38
n_dd_up: 17
n_dd_down: 20
n_dd_up_clean: 14
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 5
direction_downstream: 3
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# EDA

*ectodysplasin A* — Xq13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 7.11× (z +30.9, q 0e+00, up in 34 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (11 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.332× (z -17.4, q 0e+00, down in 33 of 35 measured lines).
> Its strongest partners by |cos| (91 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARHGAP8]] (+0.70, fdr 1e-05), [[SMYD3]] (+0.65, fdr 3e-05), [[SPTLC2]] (+0.63, fdr 5e-05); moves opposite to [[MFF-DT]] (-0.65, fdr 1e-04), [[EFCAB2]] (-0.65, fdr 3e-05), [[TSTD3]] (-0.65, fdr 4e-05).
> It sits in the **-** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[BSPRY]] → it (grade B ⚠); 3 go from it, the strongest it → [[MYO1D]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 3 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8194.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **7.11×** | +30.9 | 0e+00 | 34/35 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 5 µM |  | **6.30×** | +29.0 | 0e+00 | 34/35 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **5.38×** | +26.6 | 0e+00 | 34/35 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.82×** | +23.2 | 0e+00 | 34/36 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **4.86×** | +22.0 | 0e+00 | 35/35 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **2.76×** | +16.0 | 0e+00 | 34/34 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.60×** | +15.1 | 0e+00 | 34/35 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **4.40×** | +12.2 | 2e-32 | 34/36 (NCI-H460, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.21×** | +4.2 | 0.001 | 13/36 (NCI-H460, SHP-77, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.29×** | +4.0 | 0.003 | 11/35 (KATO III, Panc 03.27, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.25×** | +3.5 | 0.020 | 11/35 (NCI-H460, LoVo, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~54% of this change | **1.52×** | +3.4 | 0.028 | 8/31 (KATO III, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.24×** | +3.4 | 0.031 | 5/35 (KATO III, A-427, …) | inconsistent across doses |  |
| [[Afatinib (drug)]] 0.5 µM |  | 1.17× | +3.2 | 0.046 | 5/36 (NCI-H1573, NCI-H2347, …) | two highest doses | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.23×** | +3.2 | 0.046 | 8/35 (NCI-H1573, A-427, …) | rises with dose |  |
| [[Tirabrutinib (drug)]] 0.5 µM |  | **1.22×** | +3.1 | 0.058 | 4/35 (AsPC-1, HEC-1-A, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 0.5 µM |  | **1.31×** | +3.1 | 0.072 | 5/35 (NCI-H460, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[AZD-8055 (drug)]] 5 µM |  | **1.45×** | +3.0 | 0.076 | 2/35 (SW480, HOP62) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8194.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.332×** | -17.4 | 0e+00 | 33/35 (KATO III, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.486×** | -16.1 | 0e+00 | 27/35 (HEC-1-A, SW48, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.426×** | -13.5 | 4e-39 | 30/34 (NCI-H460, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.417×** | -13.3 | 3e-38 | 25/35 (HEC-1-A, SW480, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.490×** | -11.3 | 2e-27 | 24/35 (HEC-1-A, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.518×** | -10.4 | 3e-23 | 23/35 (HEC-1-A, SW48, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.521×** | -10.3 | 6e-23 | 26/35 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.534×** | -9.9 | 2e-21 | 27/34 (SNU-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.544×** | -9.3 | 1e-18 | 25/34 (HepG2/C3A, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.385×** | -7.9 | 2e-13 | 24/35 (HCT15, KATO III, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.435×** | -6.9 | 3e-10 | 22/34 (HEC-1-A, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.749×** | -6.5 | 5e-09 | 20/36 (Panc 03.27, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.685×** | -5.7 | 4e-07 | 19/34 (HCT15, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.717×** | -5.3 | 6e-06 | 18/35 (HEC-1-A, SW48, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.715×** | -5.1 | 1e-05 | 14/27 (SHP-77, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.779×** | -3.9 | 0.003 | 16/35 (CFPAC-1, A-427, …) | inconsistent across doses |  |
| [[Vilanterol (drug)]] 5 µM |  | 0.855× | -3.5 | 0.014 | 11/35 (HOP62, hTERT-HPNE, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.878× | -2.9 | 0.090 | 8/36 (Panc 03.27, HOP62, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, -0.56 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8194. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 78.8 | 6 | 12 (8 ⚠) | [[Belinostat (drug)]] 5 µM 3.94× (z +13.1) | [[Dinaciclib (drug)]] 0.5 µM 0.114× (z -20.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.376× (z -13.3) |
| [[SW480 (line)]] | alt | 51.3 | 7 | 10 (7 ⚠) | [[Belinostat (drug)]] 5 µM 4.24× (z +15.2) | [[Harringtonine (drug)]] 5 µM 0.220× (z -15.4) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.333× (z -11.6) |
| [[NCI-H460 (line)]] | wt | 30.7 | 7 | 8 (6 ⚠) | [[Panobinostat (drug)]] 5 µM 9.30× (z +17.7) | [[Digitoxin (drug)]] 5 µM 0.121× (z -16.8) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.183× (z -13.5) |
| [[HEC-1-A (line)]] | alt | 109 | 0 | 12 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -23.1) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.297× (z -18.3) |
| [[LoVo (line)]] | wt | 46.9 | 4 | 6 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 3.87× (z +12.5) | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -15.7) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.313× (z -10.8) |
| [[Panc 03.27 (line)]] | alt | 64.8 | 1 | 9 (7 ⚠) | [[Panobinostat (drug)]] 5 µM 2.83× (z +8.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.194× (z -19.4) |
| [[SW1417 (line)]] | alt | 55.6 | 6 | 3 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.83× (z +11.7) | [[Digitoxin (drug)]] 5 µM 0.133× (z -16.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.341× (z -12.2) |
| [[HCT15 (line)]] | alt | 60.7 | 0 | 8 (5 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0712× (z -18.5) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.175× (z -12.6) |
| [[HepG2_C3A (line)]] | wt | 121 | 2 | 6 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 3.26× (z +9.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.130× (z -16.2) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.354× (z -12.1) |
| [[SW48 (line)]] | wt | 109 | 0 | 8 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0823× (z -17.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.410× (z -9.5) |
| [[A-427 (line)]] | wt | 72.7 | 3 | 4 (3 ⚠) | [[Belinostat (drug)]] 5 µM 4.32× (z +12.4) | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -13.5) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.327× (z -9.5) |
| [[A549 (line)]] | wt | 21.8 | 5 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 7.11× (z +11.3) | [[Harringtonine (drug)]] 5 µM 0.108× (z -12.3) ⚠ cell-cycle shift, explains ~31% of this change |
| [[NCI-H23 (line)]] | alt | 21.6 | 5 | 2 (2 ⚠) | [[Belinostat (drug)]] 5 µM 13.1× (z +13.2) | [[Niclosamide (olamine) (drug)]] 5 µM 0.120× (z -10.4) ⚠ toxic |
| [[AsPC-1 (line)]] | alt | 24.1 | 3 | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 7.95× (z +11.5) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.161× (z -9.8) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.198× (z -9.1) |
| [[CFPAC-1 (line)]] | alt | 31.8 | 1 | 5 (3 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.57× (z +8.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.281× (z -12.5) |
| [[H4 (line)]] | wt | 31.5 | 3 | 3 (2 ⚠) | [[Belinostat (drug)]] 5 µM 6.85× (z +9.9) | [[Homoharringtonine (drug)]] 5 µM 0.0981× (z -17.0) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.177× (z -9.0) |
| [[HT-29 (line)]] | alt | 14.4 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 11.7× (z +12.8) | — |
| [[C-33 A (line)]] | alt | 42.5 | 4 | 0 | [[Belinostat (drug)]] 5 µM 5.84× (z +10.5) | — |
| [[HOP62 (line)]] | alt | 13.4 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 10.2× (z +12.7) | — |
| [[Hs 766T (line)]] | wt | 13.7 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 11.7× (z +11.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 10.6 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 10.5× (z +10.3) | — |
| [[NCI-H1573 (line)]] | alt | 18.1 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 12.9× (z +13.3) | — |
| [[NCI-H2030 (line)]] | alt | 16.9 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 8.90× (z +11.1) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0953× (z -11.5) ⚠ toxic |
| [[HS-578T (line)]] | alt | 9.13 | 3 | 0 | [[Tucidinostat (drug)]] 5 µM 4.65× (z +9.0) | — |
| [[NCI-H2347 (line)]] | alt | 22.5 | 1 | 2 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.09× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -8.8) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.324× (z -8.8) |
| [[SHP-77 (line)]] | alt | 40.4 | 1 | 2 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.87× (z +10.0) | [[Dinaciclib (drug)]] 5 µM 0.215× (z -9.9) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 23.7 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0813× (z -10.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.114× (z -9.1) |
| [[SW 900 (line)]] | alt | 12.6 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 12.4× (z +11.3) | — |
| [[AN3 CA (line)]] | alt | 72.9 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.103× (z -10.3) ⚠ cell-cycle shift, explains ~31% of this change |
| [[BT-474 (line)]] | alt | 12.6 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.0860× (z -10.2) |
| [[RPMI-7951 (line)]] | alt | 7.18 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 13.4× (z +8.6) | — |
| [[A-172 (line)]] | wt | 3.22 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 6.94 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 4.79 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.91 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 6.48 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.33 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.73 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.33 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.75 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 5.66 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.79 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 3.67 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.90 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.17 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.34 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8194), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*33 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARHGAP8]] | +0.70 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[SMYD3]] | +0.65 | +0.46 / +0.50 | both halves | 3e-05 |  |
| [[SPTLC2]] | +0.63 | +0.51 / +0.39 | both halves | 5e-05 |  |
| [[LMTK3]] | +0.63 | +0.47 / +0.43 | both halves | 3e-05 |  |
| [[FCHO1]] | +0.63 | +0.29 / +0.56 | both halves | 3e-04 |  |
| [[TMEM241]] | +0.62 | +0.31 / +0.60 | both halves | 2e-04 |  |
| [[TRAK1]] | +0.62 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[LPCAT4]] | +0.61 | +0.45 / +0.41 | both halves | 4e-05 |  |
| [[RASAL1]] | +0.61 | +0.43 / +0.57 | both halves | 3e-05 |  |
| [[SGSM1]] | +0.59 | +0.36 / +0.55 | both halves | 9e-05 |  |
| [[CMIP]] | +0.59 | +0.44 / +0.46 | both halves | 3e-05 | same gene group |
| [[LRBA]] | +0.59 | +0.41 / +0.50 | both halves | 4e-05 |  |

## Genes that move opposite

*67 of its nearest partners move opposite, 9 of them with an alert (⚠; 9 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MFF-DT]] | -0.65 | -0.47 / -0.35 | both halves | 1e-04 |  |
| [[EFCAB2]] | -0.65 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[TSTD3]] | -0.65 | -0.51 / -0.40 | both halves | 4e-05 |  |
| [[PBLD]] | -0.63 | -0.41 / -0.38 | both halves | 7e-05 |  |
| [[FBXW4]] | -0.63 | -0.38 / -0.54 | both halves | 6e-05 |  |
| [[DICER1-AS1]] | -0.63 | -0.46 / -0.36 | both halves | 9e-05 |  |
| [[RNF146]] | -0.63 | -0.34 / -0.48 | both halves | 1e-04 |  |
| [[PUS10]] | -0.63 | -0.49 / -0.46 | both halves | 3e-05 |  |
| [[NMNAT1]] | -0.63 | -0.58 / -0.37 | both halves | 9e-05 | same gene group |
| [[ERCC6L2-AS1]] | -0.62 | -0.50 / -0.16 | ⚠ one half (not replicated) | 0.001 |  |
| [[PRANCR]] | -0.62 | -0.50 / -0.27 | both halves | 3e-04 |  |
| [[DNAI4]] | -0.62 | -0.40 / -0.36 | both halves | 9e-05 |  |
| [[SENP8]] | -0.62 | -0.53 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BSPRY]] | B | BSPRY activity raises EDA's level | lines that do not express BSPRY (29) vs lines expressing it (21) | 3.06× lower at baseline in the lines without BSPRY | 0.002 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KDF1, EPCAM, RAB25 |
| [[MYO1D]] | B | MYO1D activity raises EDA's level | lines that do not express MYO1D (13) vs lines expressing it (37) | 1.83× lower at baseline in the lines without MYO1D | 0.013 | ⚠ within organs, on part of the lines; also absent: MOB3B, MBNL3, MAST4; maybe low, not absent |
| [[MCF2L]] | B | MCF2L activity raises EDA's level | lines that do not express MCF2L (14) vs lines expressing it (36) | 2.29× lower at baseline in the lines without MCF2L | 0.048 | ⚠ within organs, on part of the lines; also absent: B4GALNT3, CGN, HSD11B2 |
| [[ATP2C2]] | B | ATP2C2 activity raises EDA's level | lines that do not express ATP2C2 (32) vs lines expressing it (18) | 2.10× lower at baseline in the lines without ATP2C2 | 0.075 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, GRHL2, ST14 |
| [[CBLC]] | B | CBLC activity raises EDA's level | lines that do not express CBLC (31) vs lines expressing it (19) | 2.51× lower at baseline in the lines without CBLC | 0.085 | ⚠ within organs, on part of the lines; also absent: KDF1, CLDN7, PRSS8 |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MYO1D]] | B | EDA activity raises MYO1D's level | lines that do not express EDA (12) vs lines expressing it (38) | 1.93× lower at baseline in the lines without EDA | 0.005 | ⚠ within organs, on part of the lines |
| [[SGSM1]] | B | EDA activity raises SGSM1's level | lines that do not express EDA (12) vs lines expressing it (38) | 2.19× lower at baseline in the lines without EDA | 0.043 | ⚠ within organs, on part of the lines |
| [[GANC]] | B | EDA activity lowers GANC's level | lines that do not express EDA (12) vs lines expressing it (38) | 1.45× higher at baseline in the lines without EDA | 0.097 | ⚠ within organs, on part of the lines |

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **-** arm (projection on the module's main direction -0.662). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (0.3, 15.1); signed map (-19.8, 36.1). **Vector** length 97.2, 25.0% of its response variance represented; |z| ≥ 3 in 1,140 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +9.0 | +23.2 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +6.8 | +22.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.7 | +15.1 |
|  | [[Belinostat (drug)]] 5 µM |  | +5.1 | +29.0 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +5.1 | +16.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.2 | +12.2 |
|  | [[EX229 (drug)]] 5 µM |  | +2.6 | +2.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.3 | -3.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.1 | -0.8 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.9 | -2.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.9 | -6.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -4.8 | -9.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -4.1 | -13.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | -3.9 | -16.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.8 | -0.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.1 | -5.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.9 | +0.6 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.8 | -1.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.6 | +0.1 |

## What is on record

|  |  |
|---|---|
| Name | ectodysplasin A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq13.1 — chrX:69,616,067-70,039,472 (+) |
| Ensembl biotype | protein_coding |
| Also known as | EDA1, XLHED, HED, XHED, ED1-A1, ED1-A2, EDA-A1, EDA-A2; previously ED1, EDA2, ODT1 |
| Gene groups (HGNC) | Tumor necrosis factor superfamily; MicroRNA protein coding host genes |
| Reactome | 3 pathways, smallest: TNFs bind their physiological receptors; TNFR2 non-canonical NF-kB pathway; Cytokine Signaling in Immune system |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92838](https://www.uniprot.org/uniprotkb/Q92838) (Ectodysplasin-A):

> Cytokine which is involved in epithelial-mesenchymal signaling during morphogenesis of ectodermal organs. Functions as a ligand activating the DEATH-domain containing receptors EDAR and EDA2R. May also play a role in cell adhesion (By similarity).; [Isoform 1]: Binds only to the receptor EDAR, while isoform 3 binds exclusively to the receptor EDA2R.; [Isoform 3]: Binds only to the receptor EDA2R.

**Summary**, from NCBI Gene [1896](https://www.ncbi.nlm.nih.gov/gene/1896):

> The protein encoded by this gene is a type II membrane protein that can be cleaved by furin to produce a secreted form. The encoded protein, which belongs to the tumor necrosis factor family, acts as a homotrimer and may be involved in cell-cell signaling during the development of ectodermal organs. Defects in this gene are a cause of ectodermal dysplasia, anhidrotic, which is also known as X-linked hypohidrotic ectodermal dysplasia. Several transcript variants encoding many different isoforms …

**Accessions** — [HGNC:3157](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3157) · Entrez [1896](https://www.ncbi.nlm.nih.gov/gene/1896) · UniProt [Q92838](https://www.uniprot.org/uniprotkb/Q92838) · Ensembl [ENSG00000158813](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000158813)

## Data

Gene col 8194: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8194); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8194, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8194]; `tensor/DDL_lfc|DDL_z.npy` [8194]; `embed/gene_vectors.npy` [8194]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8194 or target_col == 8194). Every well: [[EDA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EDA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
