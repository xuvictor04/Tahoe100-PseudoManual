---
symbol: "SLC39A6"
type: "gene"
col: 6514
ensembl_id: "ENSG00000141424"
name: "solute carrier family 39 member 6"
location: "18q12.2"
module: 29
arm: "+"
pooled_cpm: 55.07
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 6
n_dd_up_clean: 9
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# SLC39A6

*solute carrier family 39 member 6* — 18q12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.98× (z +21.0, q 0e+00, up in 47 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.15× (z +20.8, q 0e+00, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.494× (z -19.1, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMED4]] (+0.65, fdr 7e-06), [[LAPTM4A]] (+0.62, fdr 1e-05), [[DPAGT1]] (+0.61, fdr 1e-05); moves opposite to [[ERCC4]] (-0.61, fdr 3e-05), [[SMG9]] (-0.60, fdr 6e-05), [[GMEB2]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[DUBR]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 13 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6514.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.98×** | +21.0 | 0e+00 | 47/47 (NCI-H1792, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.15×** | +20.8 | 0e+00 | 44/48 (SW480, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.80×** | +19.0 | 0e+00 | 41/43 (KATO III, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.11×** | +13.3 | 5e-38 | 40/45 (HOP62, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.74×** | +10.2 | 1e-22 | 41/48 (HOP62, HS-578T, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.56×** | +8.6 | 9e-16 | 41/48 (C32, MIA PaCa-2, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.32×** | +7.5 | 4e-12 | 30/48 (J82, SK-MEL-2, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +7.0 | 2e-10 | 31/48 (HOP62, SNU-423, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.41×** | +6.6 | 2e-09 | 34/48 (AsPC-1, NCI-H1792, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.39×** | +6.3 | 2e-08 | 31/48 (NCI-H1792, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.39×** | +6.1 | 6e-08 | 29/47 (CFPAC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.37×** | +6.0 | 9e-08 | 29/48 (KATO III, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.34×** | +5.6 | 1e-06 | 27/48 (NCI-H1792, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~18% of this change | **1.31×** | +5.2 | 6e-06 | 32/48 (RPMI-7951, A-427, …) | inconsistent across doses | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **1.30×** | +4.9 | 4e-05 | 25/47 (C32, NCI-H1792, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.17× | +4.3 | 5e-04 | 20/48 (HOP62, Hs 766T, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.34×** | +4.0 | 0.002 | 20/47 (SHP-77, A-427, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Mebendazole (drug)]] 5 µM |  | **1.21×** | +3.5 | 0.015 | 18/48 (HS-578T, NCI-H460, …) | top dose only |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.29×** | +3.5 | 0.016 | 14/48 (HS-578T, LOX-IMVI, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Riluzole hydrochloride (drug)]] 5 µM |  | 1.12× | +3.0 | 0.058 | 6/49 (LOX-IMVI, AsPC-1, …) | top dose only | position effect removed |
| [[Temsirolimus (drug)]] 0.5 µM |  | 1.16× | +2.9 | 0.092 | 16/48 (NCI-H460, Panc 03.27, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6514.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.494×** | -19.1 | 0e+00 | 47/48 (A-427, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.530×** | -11.7 | 3e-29 | 43/48 (A-172, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Verteporfin (drug)]] 5 µM |  | **0.647×** | -8.0 | 2e-13 | 40/48 (A-427, LOX-IMVI, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.669×** | -7.7 | 2e-12 | 32/48 (A-427, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Lidocaine (hydrochloride) (drug)]] 0.5 µM |  | **0.809×** | -4.1 | 0.005 | 21/48 (HepG2/C3A, HT-29, …) | inconsistent across doses | position effect removed |
| [[Bergenin (drug)]] 0.5 µM |  | **0.810×** | -4.1 | 0.005 | 22/48 (PANC-1, HEC-1-A, …) | two highest doses | position effect removed |
| [[Bergenin (drug)]] 5 µM |  | 0.887× | -3.3 | 0.082 | 11/48 (PANC-1, COLO 205, …) | two highest doses | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.844× | -3.3 | 0.082 | 14/48 (NCI-H1573, PANC-1, …) | two highest doses |  |
| [[Triclosan (drug)]] 5 µM |  | 0.891× | -3.1 | 0.11 | 7/48 (H4, PANC-1, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6514. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 62.1 | 5 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 3.41× (z +12.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.97× (z +10.5) | [[Homoharringtonine (drug)]] 5 µM 0.290× (z -19.2) |
| [[A-172 (line)]] | wt | 116 | 3 (2 ⚠) | 4 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.27× (z +14.9) | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -26.6) |
| [[HOP62 (line)]] | alt | 56.2 | 6 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.22× (z +15.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.46× (z +12.3) | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -17.0) |
| [[HS-578T (line)]] | alt | 102 | 5 (3 ⚠) | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.28× (z +13.1) | [[Homoharringtonine (drug)]] 5 µM 0.392× (z -14.9) |
| [[C32 (line)]] | wt | 60.6 | 6 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.17× (z +12.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.80× (z +9.1) | — |
| [[NCI-H460 (line)]] | wt | 34.2 | 3 (2 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.87× (z +16.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.43× (z +13.0) | [[Homoharringtonine (drug)]] 5 µM 0.461× (z -11.4) |
| [[PANC-1 (line)]] | alt | 53.5 | 4 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.10× (z +15.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.82× (z +11.4) | [[Homoharringtonine (drug)]] 5 µM 0.511× (z -12.6) |
| [[RKO (line)]] | wt | 77.7 | 3 (2 ⚠) | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.40× (z +12.3) | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -18.0) |
| [[J82 (line)]] | alt | 47.8 | 4 (2 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.22× (z +11.6) | [[Homoharringtonine (drug)]] 5 µM 0.551× (z -8.7) |
| [[SK-MEL-2 (line)]] | alt | 77.0 | 4 (2 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.68× (z +14.4) | [[Homoharringtonine (drug)]] 5 µM 0.454× (z -11.4) |
| [[SW480 (line)]] | alt | 24.0 | 4 (2 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.09× (z +16.1) | [[Homoharringtonine (drug)]] 5 µM 0.508× (z -9.7) |
| [[A498 (line)]] | wt | 72.2 | 3 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.76× (z +11.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.94× (z +11.1) | [[Homoharringtonine (drug)]] 5 µM 0.408× (z -15.0) |
| [[CFPAC-1 (line)]] | alt | 39.6 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.15× (z +11.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.80× (z +8.6) | — |
| [[HEC-1-A (line)]] | alt | 81.0 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.81× (z +13.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.85× (z +11.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 42.7 | 3 (2 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.68× (z +12.3) | [[Harringtonine (drug)]] 5 µM 0.356× (z -8.7) |
| [[NCI-H1573 (line)]] | alt | 33.7 | 2 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 6.93× (z +15.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -13.3) |
| [[NCI-H1792 (line)]] | alt | 64.3 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.40× (z +16.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.16× (z +15.9) | — |
| [[NCI-H2030 (line)]] | alt | 33.6 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.75× (z +9.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -18.0) |
| [[Panc 03.27 (line)]] | alt | 65.7 | 3 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.40× (z +12.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.89× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.485× (z -10.1) |
| [[A-427 (line)]] | wt | 130 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0921× (z -43.9) |
| [[A549 (line)]] | wt | 44.1 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.40× (z +11.8) | — |
| [[HCT15 (line)]] | alt | 64.4 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.47× (z +9.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.469× (z -8.5) |
| [[Hs 766T (line)]] | wt | 30.8 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.16× (z +12.5) | [[Homoharringtonine (drug)]] 5 µM 0.450× (z -8.7) |
| [[KATO III (line)]] | alt | 41.3 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.07× (z +15.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.28× (z +11.2) | — |
| [[LoVo (line)]] | wt | 42.2 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.44× (z +12.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.13× (z +11.1) | — |
| [[LS 180 (line)]] | wt | 32.2 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.84× (z +12.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.61× (z +10.6) | — |
| [[NCI-H23 (line)]] | alt | 63.0 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 4.26× (z +14.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -22.6) |
| [[SNU-423 (line)]] | alt | 33.4 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.83× (z +12.0) | — |
| [[SW1417 (line)]] | alt | 46.8 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.76× (z +10.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.526× (z -9.1) |
| [[AsPC-1 (line)]] | alt | 31.6 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.61× (z +11.3) | [[Homoharringtonine (drug)]] 5 µM 0.431× (z -9.9) |
| [[BT-474 (line)]] | alt | 70.9 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.02× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.467× (z -9.5) |
| [[H4 (line)]] | wt | 77.2 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.30× (z +9.9) | [[Harringtonine (drug)]] 5 µM 0.338× (z -8.7) |
| [[HT-29 (line)]] | alt | 28.8 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.96× (z +11.9) | — |
| [[hTERT-HPNE (line)]] | wt | 93.2 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.24× (z +10.4) | — |
| [[RPMI-7951 (line)]] | alt | 88.0 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.17× (z +9.5) | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -12.9) |
| [[SHP-77 (line)]] | alt | 59.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.53× (z +12.0) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 65.0 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.25× (z +8.8) | [[Dinaciclib (drug)]] 0.05 µM 0.161× (z -13.1) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 98.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -15.9) |
| [[NCI-H2347 (line)]] | alt | 49.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.17× (z +12.2) | — |
| [[SW48 (line)]] | wt | 97.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.395× (z -10.2) |
| [[AN3 CA (line)]] | alt | 71.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 92.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 38.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 43.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 46.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 52.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 64.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 62.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 26.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6514), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMED4]] | +0.65 | +0.60 / +0.66 | both halves | 7e-06 |  |
| [[LAPTM4A]] | +0.62 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[DPAGT1]] | +0.61 | +0.64 / +0.49 | both halves | 1e-05 |  |
| [[MFN1]] | +0.60 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[CDIPT]] | +0.60 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[NTAN1]] | +0.60 | +0.48 / +0.67 | both halves | 2e-05 |  |
| [[PPT1]] | +0.60 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[SRD5A1]] | +0.59 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[COLGALT1]] | +0.59 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[WRNIP1]] | +0.58 | +0.61 / +0.46 | both halves | 3e-05 |  |
| [[SETD3]] | +0.58 | +0.61 / +0.47 | both halves | 2e-05 |  |
| [[MLEC]] | +0.58 | +0.57 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ERCC4]] | -0.61 | -0.46 / -0.67 | both halves | 3e-05 |  |
| [[SMG9]] | -0.60 | -0.38 / -0.66 | both halves | 6e-05 |  |
| [[GMEB2]] | -0.60 | -0.60 / -0.52 | both halves | 1e-05 |  |
| [[TMEM265]] | -0.59 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[NT5C]] | -0.59 | -0.38 / -0.59 | both halves | 6e-05 |  |
| [[HMGXB4]] | -0.58 | -0.45 / -0.59 | both halves | 3e-05 |  |
| [[TRMT10B]] | -0.58 | -0.48 / -0.56 | both halves | 2e-05 |  |
| [[EID2]] | -0.57 | -0.47 / -0.57 | both halves | 2e-05 |  |
| [[METTL18]] | -0.57 | -0.51 / -0.60 | both halves | 1e-05 |  |
| [[LIME1]] | -0.57 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[THG1L]] | -0.57 | -0.45 / -0.56 | both halves | 3e-05 |  |
| [[NSRP1]] | -0.56 | -0.54 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DUBR]] | B | DUBR activity raises SLC39A6's level | lines that do not express DUBR (8) vs lines expressing it (42) | 1.76× lower at baseline in the lines without DUBR | 0.080 | ⚠ within organs, on part of the lines; also absent: ATP10D, LRP12, CYP46A1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.596). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-18.6, -17.9); signed map (-49.7, -7.1). **Vector** length 100, 28.0% of its response variance represented; |z| ≥ 3 in 1,082 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +6.1 | +7.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.2 | +20.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.1 | +8.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.1 | +10.2 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.1 | +2.8 |
|  | [[Mebendazole (drug)]] 5 µM |  | +2.3 | +3.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.2 | +2.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.2 | +2.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.9 | +2.6 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -11.5 | -19.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | -11.3 | -11.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.5 | -7.7 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.3 | -2.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.7 | -1.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | -3.3 | -8.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.1 | -0.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.9 | -1.0 |
|  | [[Thymol (drug)]] 0.5 µM |  | -2.4 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 39 member 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q12.2 — chr18:36,108,531-36,129,385 (-) |
| Ensembl biotype | protein_coding |
| Also known as | LIV-1, ZIP6 |
| Gene groups (HGNC) | Solute carrier family 39 |
| Hallmark sets | ESTROGEN_RESPONSE_EARLY |
| Reactome | 5 pathways, smallest: Zinc influx into cells by the SLC39 gene family; Zinc transporters; Metal ion SLC transporters |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13433](https://www.uniprot.org/uniprotkb/Q13433) (Zinc transporter ZIP6):

> Zinc-influx transporter which plays a role in zinc homeostasis and in the induction of epithelial-to-mesenchymal transition (EMT). When associated with SLC39A10, the heterodimer formed by SLC39A10 and SLC39A6 mediates cellular zinc uptake to trigger cells to undergo epithelial- to-mesenchymal transition (EMT). The SLC39A10-SLC39A6 heterodimer also controls NCAM1 phosphorylation and its integration into focal adhesion complexes during EMT (By similarity). Zinc influx inactivates GSK3B, enabling …

**Summary**, from NCBI Gene [25800](https://www.ncbi.nlm.nih.gov/gene/25800):

> Zinc is an essential cofactor for hundreds of enzymes. It is involved in protein, nucleic acid, carbohydrate, and lipid metabolism, as well as in the control of gene transcription, growth, development, and differentiation. SLC39A6 belongs to a subfamily of proteins that show structural characteristics of zinc transporters (Taylor and Nicholson, 2003 [PubMed 12659941]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:18607](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18607) · Entrez [25800](https://www.ncbi.nlm.nih.gov/gene/25800) · UniProt [Q13433](https://www.uniprot.org/uniprotkb/Q13433) · Ensembl [ENSG00000141424](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000141424)

## Data

Gene col 6514: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6514); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6514, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6514]; `tensor/DDL_lfc|DDL_z.npy` [6514]; `embed/gene_vectors.npy` [6514]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6514 or target_col == 6514). Every well: [[SLC39A6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC39A6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
