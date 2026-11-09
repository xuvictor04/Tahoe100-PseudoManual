---
symbol: "HIP1"
type: "gene"
col: 4844
ensembl_id: "ENSG00000127946"
name: "huntingtin interacting protein 1"
location: "7q11.23"
module: 100
arm: "+"
pooled_cpm: 184.52
n_lines_expressing: 49
n_dd_up: 10
n_dd_down: 17
n_dd_up_clean: 10
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/100"]
generated_by: "tahoemap"
---

# HIP1

*huntingtin interacting protein 1* — 7q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 1.87× (z +16.9, q 0e+00, up in 37 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (5 with an alert ⚠); the strongest is [[PH-797804 (drug)]] 5 µM: 0.511× (z -9.5, q 1e-18, down in 36 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NRTN]] (+0.67, fdr 1e-05), [[MAST1]] (+0.58, fdr 2e-05), [[TCF7L1]] (+0.57, fdr 1e-05); moves opposite to [[TRMT12]] (-0.54, fdr 3e-05), [[LINC02728]] (-0.53, fdr 2e-05), [[TOR1A]] (-0.51, fdr 4e-05).
> It is in [[Module 100]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[TPST1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 2 with an alert ⚠; shown: the 15 strongest. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4844.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.87×** | +16.9 | 0e+00 | 37/47 (KATO III, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.82×** | +16.1 | 0e+00 | 40/47 (SW1417, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.45×** | +14.3 | 7e-44 | 38/47 (SW1417, HT-29, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.42×** | +13.3 | 3e-38 | 32/47 (HEC-1-A, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.62×** | +13.1 | 4e-37 | 35/47 (KATO III, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.54×** | +11.7 | 8e-30 | 43/48 (NCI-H460, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.51×** | +10.7 | 7e-25 | 27/47 (PANC-1, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.47×** | +10.4 | 1e-23 | 38/47 (SW1417, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.86×** | +8.8 | 8e-17 | 43/48 (SW1417, HEC-1-A, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.38×** | +8.7 | 3e-16 | 36/47 (SW1417, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.05 µM |  | 1.16× | +4.0 | 0.003 | 17/47 (KATO III, HT-29, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | 1.15× | +3.8 | 0.008 | 21/47 (SK-MEL-2, SW48, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.15× | +3.7 | 0.008 | 16/47 (RPMI-7951, SW 1088, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | 1.15× | +3.7 | 0.008 | 18/48 (RPMI-7951, NCI-H1573, …) | rises with dose |  |
| [[Budesonide (drug)]] 0.5 µM |  | 1.14× | +3.7 | 0.009 | 17/47 (RPMI-7951, H4, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 16 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4844.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **0.511×** | -9.5 | 1e-18 | 36/47 (C32, SK-MEL-2, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.527×** | -9.0 | 4e-17 | 32/48 (C32, A549, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.739×** | -8.2 | 6e-14 | 30/47 (A549, SK-MEL-2, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.760×** | -7.4 | 2e-11 | 33/47 (A549, LOX-IMVI, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.763×** | -7.3 | 3e-11 | 27/47 (A549, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~15% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.614×** | -6.9 | 6e-10 | 26/38 (Panc 03.27, C32, …) | top dose only | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.844× | -6.5 | 7e-09 | 22/47 (SNU-423, SK-MEL-2, …) | top dose only | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.778×** | -6.3 | 3e-08 | 24/45 (HOP62, C32, …) | inconsistent across doses | cell-cycle shift (explains ~4% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~11% of this change | **0.802×** | -5.7 | 6e-07 | 24/46 (NCI-H23, LOX-IMVI, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.813×** | -5.4 | 4e-06 | 25/46 (A549, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.877× | -5.0 | 3e-05 | 20/47 (A549, HOP62, …) | top dose only |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 0.836× | -4.8 | 6e-05 | 21/46 (MIA PaCa-2, H4, …) | two highest doses |  |
| [[NG25 (drug)]] 5 µM |  | **0.710×** | -4.8 | 6e-05 | 26/46 (C32, PANC-1, …) | rises with dose | cell-cycle shift (explains ~21% here); noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~30% of this change | 0.839× | -4.7 | 8e-05 | 21/47 (HOP62, CFPAC-1, …) | all doses, flat | low cells (technical?) |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.836× | -4.6 | 2e-04 | 22/46 (SW48, HEC-1-A, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.891× | -4.4 | 4e-04 | 14/48 (MIA PaCa-2, H4, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.840× | -4.4 | 4e-04 | 21/46 (hTERT-HPNE, A549, …) | inconsistent across doses | low cells (technical?) |
| [[vincristine (drug)]] 0.5 µM |  | **0.802×** | -4.2 | 7e-04 | 21/47 (MIA PaCa-2, SK-MEL-2, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.848× | -4.2 | 9e-04 | 17/46 (MIA PaCa-2, SW 1271, …) | two highest doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.745×** | -4.1 | 9e-04 | 21/47 (H4, A549, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.751×** | -4.0 | 0.001 | 19/47 (MIA PaCa-2, C32, …) | top dose only | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.753×** | -4.0 | 0.002 | 20/47 (PANC-1, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.761×** | -3.9 | 0.003 | 17/47 (H4, SW480, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4844. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RPMI-7951 (line)]] | alt | 236 | 18 | 1 | [[Clobetasol propionate (drug)]] 0.05 µM 2.66× (z +14.2) | [[TAK-901 (drug)]] 5 µM 0.280× (z -9.7) |
| [[A549 (line)]] | wt | 468 | 0 | 16 (11 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.260× (z -17.3) |
| [[NCI-H460 (line)]] | wt | 78.8 | 16 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.35× (z +23.2) | — |
| [[C32 (line)]] | wt | 312 | 1 | 11 (7 ⚠) | [[Auranofin (drug)]] 5 µM 1.84× (z +8.8) | [[PH-797804 (drug)]] 5 µM 0.156× (z -14.0) |
| [[HOP62 (line)]] | alt | 389 | 1 | 10 (8 ⚠) | [[Harringtonine (drug)]] 5 µM 1.79× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.382× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.664× (z -9.4) |
| [[MIA PaCa-2 (line)]] | alt | 140 | 8 (2 ⚠) | 2 (2 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.53× (z +16.3) ⚠ position not correctable · without an alert: [[Belinostat (drug)]] 5 µM 3.10× (z +12.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.439× (z -9.1) ⚠ unreliable plate only |
| [[HEC-1-A (line)]] | alt | 180 | 8 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +30.5) | [[TAK-901 (drug)]] 0.05 µM 0.575× (z -9.6) |
| [[LoVo (line)]] | wt | 113 | 9 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.24× (z +17.2) | — |
| [[NCI-H1573 (line)]] | alt | 84.9 | 8 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.13× (z +11.8) | [[Digitoxin (drug)]] 0.5 µM 0.457× (z -8.7) ⚠ cell-cycle shift, explains ~22% of this change |
| [[BT-474 (line)]] | alt | 128 | 7 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +15.5) | [[TAK-901 (drug)]] 0.05 µM 0.415× (z -9.3) |
| [[KATO III (line)]] | alt | 48.9 | 8 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 9.83× (z +18.7) | — |
| [[LOX-IMVI (line)]] | wt | 106 | 0 | 8 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.233× (z -13.4) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.277× (z -11.8) |
| [[LS 180 (line)]] | wt | 51.1 | 7 | 1 | [[Panobinostat (drug)]] 5 µM 6.01× (z +14.6) | [[Homoharringtonine (drug)]] 0.5 µM 0.308× (z -9.6) |
| [[NCI-H2347 (line)]] | alt | 57.5 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +13.7) | — |
| [[SW1417 (line)]] | alt | 126 | 8 | 0 | [[Panobinostat (drug)]] 5 µM 4.11× (z +18.2) | — |
| [[HT-29 (line)]] | alt | 56.8 | 7 | 0 | [[Tucidinostat (drug)]] 5 µM 4.05× (z +17.5) | — |
| [[SK-MEL-2 (line)]] | alt | 223 | 2 (1 ⚠) | 5 (3 ⚠) | [[Auranofin (drug)]] 5 µM 2.47× (z +12.6) | [[Selinexor (drug)]] 5 µM 0.496× (z -13.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.499× (z -9.5) |
| [[SW48 (line)]] | wt | 194 | 6 | 1 | [[Harringtonine (drug)]] 5 µM 3.19× (z +12.7) | [[TAK-901 (drug)]] 0.05 µM 0.349× (z -11.3) |
| [[Panc 03.27 (line)]] | alt | 82.6 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +16.1) | [[Lonafarnib (drug)]] 5 µM 0.171× (z -10.2) ⚠ toxic |
| [[H4 (line)]] | wt | 413 | 3 | 2 (2 ⚠) | [[Triamcinolone (drug)]] 5 µM 1.99× (z +10.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.385× (z -9.9) ⚠ unreliable plate only |
| [[Hs 766T (line)]] | wt | 188 | 2 | 3 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.79× (z +9.5) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.334× (z -12.7) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.384× (z -11.1) |
| [[SW480 (line)]] | alt | 251 | 4 | 1 (1 ⚠) | [[Belinostat (drug)]] 5 µM 1.96× (z +11.9) | [[Dinaciclib (drug)]] 0.05 µM 0.509× (z -11.0) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 184 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +14.6) | [[Dinaciclib (drug)]] 0.5 µM 0.430× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[NCI-H1792 (line)]] | alt | 313 | 2 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 1.87× (z +9.5) | [[Dinaciclib (drug)]] 0.05 µM 0.408× (z -12.5) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 120 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.402× (z -15.9) |
| [[PANC-1 (line)]] | alt | 157 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +24.3) | — |
| [[SW 900 (line)]] | alt | 186 | 4 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.19× (z +10.7) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 1.88× (z +8.7) | — |
| [[A-172 (line)]] | wt | 343 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.289× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[A498 (line)]] | wt | 357 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +18.6) | — |
| [[AsPC-1 (line)]] | alt | 56.9 | 3 | 0 | [[Belinostat (drug)]] 5 µM 3.60× (z +9.9) | — |
| [[CFPAC-1 (line)]] | alt | 180 | 0 | 3 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.451× (z -14.1) ⚠ cell-cycle shift, explains ~19% of this change |
| [[HepG2_C3A (line)]] | wt | 78.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.86× (z +15.5) | — |
| [[HS-578T (line)]] | alt | 481 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.338× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[NCI-H2030 (line)]] | alt | 126 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.352× (z -11.7) |
| [[RKO (line)]] | wt | 111 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.15× (z +12.2) ⚠ cell-cycle shift, explains ~19% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.48× (z +10.3) | — |
| [[SNU-423 (line)]] | alt | 269 | 0 | 3 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.512× (z -14.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.459× (z -12.1) |
| [[A-427 (line)]] | wt | 144 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.596× (z -9.8) |
| [[AN3 CA (line)]] | alt | 328 | 1 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.81× (z +8.9) ⚠ cell-cycle shift, explains ~19% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.420× (z -8.5) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 193 | 2 | 0 | [[Belinostat (drug)]] 5 µM 2.26× (z +9.5) | — |
| [[J82 (line)]] | alt | 140 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.66× (z +9.8) | — |
| [[SHP-77 (line)]] | alt | 84.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +11.7) | — |
| [[C-33 A (line)]] | alt | 253 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.349× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[CHP-212 (line)]] | wt | 370 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.203× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[SW 1088 (line)]] | alt | 749 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.224× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[COLO 205 (line)]] | alt | 25.7 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 142 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 181 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 224 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 83.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 135 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4844), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NRTN]] | +0.67 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[MAST1]] | +0.58 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[TCF7L1]] | +0.57 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[KREMEN2]] | +0.54 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[PRKCD]] | +0.54 | +0.57 / +0.38 | both halves | 7e-05 |  |
| [[RTN2]] | +0.54 | +0.46 / +0.49 | both halves | 2e-05 |  |
| [[FADS3]] | +0.53 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[RAB13]] | +0.53 | +0.49 / +0.43 | both halves | 3e-05 |  |
| [[TNNT1]] | +0.53 | +0.41 / +0.37 | both halves | 8e-05 |  |
| [[SLC27A1]] | +0.53 | +0.44 / +0.50 | both halves | 3e-05 |  |
| [[CAMKK1]] | +0.51 | +0.40 / +0.46 | both halves | 5e-05 |  |
| [[GNG7]] | +0.51 | +0.38 / +0.54 | both halves | 6e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRMT12]] | -0.54 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[LINC02728]] | -0.53 | -0.51 / -0.46 | both halves | 2e-05 |  |
| [[TOR1A]] | -0.51 | -0.41 / -0.50 | both halves | 4e-05 | pathway: Clathrin-mediated endocytosis |
| [[ANKRD40]] | -0.51 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[SCO1]] | -0.50 | -0.53 / -0.38 | both halves | 7e-05 |  |
| [[EXO5]] | -0.49 | -0.44 / -0.37 | both halves | 8e-05 |  |
| [[PIGW]] | -0.48 | -0.45 / -0.35 | both halves | 1e-04 |  |
| [[ADAT1]] | -0.48 | -0.41 / -0.36 | both halves | 9e-05 |  |
| [[LINC01134]] | -0.48 | -0.45 / -0.32 | both halves | 1e-04 |  |
| [[L3HYPDH]] | -0.47 | -0.46 / -0.38 | both halves | 7e-05 |  |
| [[DPY19L3-DT]] | -0.47 | -0.41 / -0.38 | both halves | 6e-05 |  |
| [[ALG8]] | -0.47 | -0.41 / -0.38 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TPST1]] | B | TPST1 activity raises HIP1's level | lines that do not express TPST1 (5) vs lines expressing it (45) | 3.89× lower at baseline in the lines without TPST1 | 0.007 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CYP46A1, CSRP2, MYO5A |
| [[TCF7L1]] | B | TCF7L1 activity raises HIP1's level | lines that do not express TCF7L1 (12) vs lines expressing it (38) | 2.30× lower at baseline in the lines without TCF7L1 | 0.083 | ⚠ within organs, on part of the lines; also absent: EML1, PYGO1, FAM124A |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers HIP1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers HIP1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[MFGE8]] | B | MFGE8 activity raises HIP1's level | lines that do not express MFGE8 (7) vs lines expressing it (43) | 2.06× lower at baseline in the lines without MFGE8 | 0.090 | ⚠ within organs, on part of the lines; also absent: P3H1, HAPLN3, FAM171B |
| [[CAMKK1]] | C | CAMKK1 activity raises HIP1's level | lines that do not express CAMKK1 (4) vs lines expressing it (46) | 1.80× lower at baseline in the lines without CAMKK1 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CKAP4, ADGRB2, POGLUT3; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 100]]; 46 genes; every member is in the + arm (projection on the module's main direction 0.555). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (8.6, -1.6); signed map (-27.2, 22.2). **Vector** length 140, 45.3% of its response variance represented; |z| ≥ 3 in 1,810 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 0.5 µM |  | +9.1 | +11.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +8.4 | +14.3 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +6.6 | +10.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.6 | +10.7 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +5.9 | +8.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +5.6 | +8.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +4.8 | +4.0 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +4.7 | +3.7 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | +3.9 | +3.2 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -7.9 | -6.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | -7.8 | +2.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -7.5 | -6.3 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~30% of this change | -6.9 | -4.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -6.6 | -5.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -6.2 | -9.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.2 | -7.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -6.1 | -4.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -6.0 | -5.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.5 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | huntingtin interacting protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q11.23 — chr7:75,533,298-75,738,962 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ILWEQ |
| Reactome | 7 pathways, smallest: ALK mutants bind TKIs; Signaling by ALK fusions and activated point mutants; Signaling by ALK in cancer |
| Matched by | ensembl_id |

**Function**, from UniProt [O00291](https://www.uniprot.org/uniprotkb/O00291) (Huntingtin-interacting protein 1):

> Plays a role in clathrin-mediated endocytosis and trafficking. Involved in regulating AMPA receptor trafficking in the central nervous system in an NMDA-dependent manner (By similarity). Regulates presynaptic nerve terminal activity (By similarity). Enhances androgen receptor (AR)-mediated transcription. May act as a pro-apoptotic protein that induces cell death by acting through the intrinsic apoptosis pathway. Binds 3-phosphoinositides (via ENTH domain). May act through the ENTH domain to …

**Summary**, from NCBI Gene [3092](https://www.ncbi.nlm.nih.gov/gene/3092):

> The product of this gene is a membrane-associated protein that functions in clathrin-mediated endocytosis and protein trafficking within the cell. The encoded protein binds to the huntingtin protein in the brain; this interaction is lost in Huntington's disease. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jul 2013]

**Accessions** — [HGNC:4913](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4913) · Entrez [3092](https://www.ncbi.nlm.nih.gov/gene/3092) · UniProt [O00291](https://www.uniprot.org/uniprotkb/O00291) · Ensembl [ENSG00000127946](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000127946)

## Data

Gene col 4844: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4844); `tables/drug_effects.parquet` (64 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4844, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4844]; `tensor/DDL_lfc|DDL_z.npy` [4844]; `embed/gene_vectors.npy` [4844]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4844 or target_col == 4844). Every well: [[HIP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HIP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
