---
symbol: "RCC2"
type: "gene"
col: 10993
ensembl_id: "ENSG00000179051"
name: "regulator of chromosome condensation 2"
location: "1p36.13"
module: 126
arm: "+"
pooled_cpm: 51.35
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 13
n_dd_up_clean: 10
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/126"]
generated_by: "tahoemap"
---

# RCC2

*regulator of chromosome condensation 2* — 1p36.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.08× (z +22.4, q 0e+00, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.428× (z -18.4, q 0e+00, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UBQLN4]] (+0.70, fdr 1e-05), [[TOR1A]] (+0.67, fdr 1e-05), [[PRRC2B]] (+0.66, fdr 1e-05); moves opposite to [[PIGH]] (-0.69, fdr 1e-05), [[CTR9]] (-0.67, fdr 9e-06), [[TRAPPC5]] (-0.66, fdr 7e-06).
> It is in [[Module 126]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 11 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10993.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.08×** | +22.4 | 0e+00 | 44/48 (HS-578T, A549, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.30×** | +18.1 | 0e+00 | 41/46 (J82, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.29×** | +17.3 | 0e+00 | 39/42 (NCI-H1573, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.06×** | +15.1 | 0e+00 | 45/47 (LoVo, NCI-H460, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.89×** | +12.8 | 3e-35 | 38/45 (J82, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.75×** | +11.7 | 1e-29 | 34/47 (HS-578T, A-172, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.50×** | +8.8 | 9e-17 | 36/48 (HS-578T, BT-474, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.49×** | +8.6 | 5e-16 | 32/48 (HOP62, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.47×** | +8.4 | 4e-15 | 37/46 (SW480, PANC-1, …) | all doses, flat | low cells (technical?); cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.45×** | +8.1 | 3e-14 | 33/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.44×** | +7.6 | 2e-12 | 31/48 (RKO, HS-578T, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **1.32×** | +5.9 | 1e-07 | 27/46 (HOP62, NCI-H460, …) | all doses, stronger at high dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.31×** | +5.9 | 2e-07 | 30/47 (HOP62, SW480, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.24×** | +4.7 | 9e-05 | 19/48 (Hs 766T, NCI-H2347, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.16× | +4.5 | 2e-04 | 18/48 (HOP62, hTERT-HPNE, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.21×** | +4.2 | 1e-03 | 21/48 (HS-578T, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.20×** | +3.9 | 0.004 | 19/48 (C32, NCI-H1792, …) | top dose only |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.17× | +3.4 | 0.022 | 14/47 (SNU-1, HS-578T, …) | top dose only |  |
| [[Doxycycline (monohydrate) (drug)]] 5 µM |  | 1.16× | +3.1 | 0.051 | 6/47 (HEC-1-A, CFPAC-1, …) | top dose only |  |
| [[Pralsetinib (drug)]] 5 µM |  | **1.31×** | +3.1 | 0.055 | 10/47 (A498, C32, …) | top dose only | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.15× | +2.9 | 0.092 | 11/47 (LOX-IMVI, C32, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, none with an alert; shown: the 15 strongest. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10993.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.428×** | -18.4 | 0e+00 | 42/48 (A-427, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.486×** | -15.7 | 0e+00 | 41/48 (PANC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.603×** | -11.0 | 8e-26 | 30/48 (PANC-1, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.744×** | -6.4 | 2e-08 | 27/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.782×** | -5.4 | 9e-06 | 24/48 (LS 180, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.862× | -4.6 | 5e-04 | 20/48 (LS 180, A-427, …) | all doses, stronger at high dose |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.694×** | -4.2 | 0.003 | 18/46 (H4, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **0.767×** | -4.1 | 0.003 | 18/48 (SHP-77, KATO III, …) | all doses, flat | plate-row cell shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.768×** | -4.1 | 0.003 | 13/48 (A498, C-33 A, …) | two highest doses | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **0.701×** | -4.0 | 0.003 | 18/48 (SK-MEL-2, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **0.832×** | -3.8 | 0.008 | 16/48 (C-33 A, LoVo, …) | all doses, flat |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.721×** | -3.7 | 0.009 | 16/46 (SW48, KATO III, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.724×** | -3.7 | 0.010 | 22/49 (A-427, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.741×** | -3.4 | 0.026 | 15/48 (C-33 A, HCT15, …) | two highest doses | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.856× | -3.4 | 0.026 | 14/48 (SW48, A-427, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10993. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 84.6 | 4 (3 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 2.83× (z +11.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.77× (z +9.6) | [[Panobinostat (drug)]] 5 µM 0.306× (z -14.3) |
| [[SW480 (line)]] | alt | 81.4 | 4 (3 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.21× (z +13.0) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 2.39× (z +10.1) | [[Panobinostat (drug)]] 5 µM 0.246× (z -16.3) |
| [[A-427 (line)]] | wt | 71.4 | 1 | 6 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.14× (z +8.8) | [[Panobinostat (drug)]] 0.5 µM 0.170× (z -20.8) |
| [[A498 (line)]] | wt | 57.3 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 2.91× (z +13.2) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.314× (z -15.0) |
| [[HOP62 (line)]] | alt | 36.7 | 6 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.13× (z +12.0) | — |
| [[J82 (line)]] | alt | 78.3 | 4 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.38× (z +14.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.93× (z +10.8) | [[Panobinostat (drug)]] 0.5 µM 0.400× (z -10.7) |
| [[PANC-1 (line)]] | alt | 65.9 | 2 (2 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 1.59× (z +9.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 5 µM 0.263× (z -19.6) |
| [[C-33 A (line)]] | alt | 119 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -16.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.259× (z -13.4) |
| [[CFPAC-1 (line)]] | alt | 32.5 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.64× (z +12.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.60× (z +12.3) | — |
| [[HEC-1-A (line)]] | alt | 76.7 | 4 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.26× (z +13.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.84× (z +10.0) | [[Panobinostat (drug)]] 0.5 µM 0.454× (z -9.3) |
| [[HS-578T (line)]] | alt | 29.7 | 5 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.44× (z +16.7) | — |
| [[NCI-H460 (line)]] | wt | 31.0 | 3 (2 ⚠) | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.52× (z +13.4) | [[Panobinostat (drug)]] 5 µM 0.399× (z -9.4) |
| [[A-172 (line)]] | wt | 31.3 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.93× (z +12.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.72× (z +11.6) | — |
| [[A549 (line)]] | wt | 29.8 | 4 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.96× (z +15.3) | — |
| [[HT-29 (line)]] | alt | 72.3 | 2 (1 ⚠) | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.80× (z +9.0) | [[Panobinostat (drug)]] 0.5 µM 0.383× (z -10.5) |
| [[NCI-H1792 (line)]] | alt | 24.5 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.10× (z +11.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.04× (z +10.8) | — |
| [[SK-MEL-2 (line)]] | alt | 68.9 | 1 (1 ⚠) | 3 | [[Harringtonine (drug)]] 5 µM 2.95× (z +9.8) ⚠ cell-cycle shift, explains ~33% of this change | [[Panobinostat (drug)]] 0.5 µM 0.254× (z -13.1) |
| [[SNU-423 (line)]] | alt | 31.5 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.10× (z +11.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.79× (z +11.0) | — |
| [[LS 180 (line)]] | wt | 63.3 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.384× (z -9.1) |
| [[MIA PaCa-2 (line)]] | alt | 68.4 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.384× (z -12.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.281× (z -11.9) |
| [[NCI-H1573 (line)]] | alt | 29.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 11.0× (z +15.9) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 45.6 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.08× (z +10.7) | [[Panobinostat (drug)]] 0.5 µM 0.385× (z -9.9) |
| [[Panc 03.27 (line)]] | alt | 38.4 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.12× (z +12.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.39× (z +11.0) | — |
| [[RKO (line)]] | wt | 56.8 | 1 | 2 | [[Epirubicin (hydrochloride) (drug)]] 5 µM 2.79× (z +9.2) | [[Panobinostat (drug)]] 0.5 µM 0.259× (z -12.6) |
| [[SW48 (line)]] | wt | 112 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.184× (z -15.6) |
| [[BT-474 (line)]] | alt | 66.6 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.36× (z +10.9) | [[Homoharringtonine (drug)]] 5 µM 0.453× (z -10.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 49.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.57× (z +10.6) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 34.2 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.66× (z +11.0) | — |
| [[hTERT-HPNE (line)]] | wt | 27.8 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.99× (z +11.5) | [[Mozavaptan (drug)]] 5 µM 0.191× (z -9.3) |
| [[LoVo (line)]] | wt | 49.5 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.36× (z +12.3) | — |
| [[NCI-H23 (line)]] | alt | 62.6 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.305× (z -11.4) |
| [[NCI-H2347 (line)]] | alt | 37.2 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.80× (z +14.4) | [[Panobinostat (drug)]] 0.5 µM 0.383× (z -9.6) |
| [[RPMI-7951 (line)]] | alt | 35.0 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.45× (z +11.8) | — |
| [[SHP-77 (line)]] | alt | 56.3 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.09× (z +9.4) | [[Panobinostat (drug)]] 5 µM 0.379× (z -8.8) |
| [[AsPC-1 (line)]] | alt | 17.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.39× (z +12.4) | — |
| [[HepG2_C3A (line)]] | wt | 51.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.21× (z +12.1) | — |
| [[LOX-IMVI (line)]] | wt | 25.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.76× (z +10.5) | — |
| [[SNU-1 (line)]] | wt | 53.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -14.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW 900 (line)]] | alt | 27.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.63× (z +9.6) | — |
| [[SW1417 (line)]] | alt | 53.5 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.355× (z -11.0) |
| [[AN3 CA (line)]] | alt | 80.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 43.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 37.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 44.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 86.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10993), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*53 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBQLN4]] | +0.70 | +0.69 / +0.52 | both halves | 1e-05 |  |
| [[TOR1A]] | +0.67 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[PRRC2B]] | +0.66 | +0.58 / +0.49 | both halves | 1e-05 |  |
| [[HCFC1]] | +0.65 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[EPM2A]] | +0.64 | +0.59 / +0.38 | both halves | 6e-05 |  |
| [[U2AF2]] | +0.64 | +0.44 / +0.57 | both halves | 3e-05 |  |
| [[ATE1]] | +0.63 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[HNRNPAB]] | +0.62 | +0.69 / +0.52 | both halves | 1e-05 |  |
| [[RCN1]] | +0.62 | +0.44 / +0.50 | both halves | 3e-05 |  |
| [[ZNF362]] | +0.62 | +0.46 / +0.48 | both halves | 2e-05 |  |
| [[CERS2]] | +0.62 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[SLC5A6]] | +0.62 | +0.62 / +0.34 | both halves | 1e-04 |  |

## Genes that move opposite

*47 of its nearest partners move opposite, 5 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIGH]] | -0.69 | -0.60 / -0.53 | both halves | 1e-05 |  |
| [[CTR9]] | -0.67 | -0.66 / -0.57 | both halves | 9e-06 |  |
| [[TRAPPC5]] | -0.66 | -0.60 / -0.58 | both halves | 7e-06 |  |
| [[GPATCH11]] | -0.64 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[ZMYM6]] | -0.63 | -0.61 / -0.47 | both halves | 2e-05 |  |
| [[YIF1B]] | -0.62 | -0.39 / -0.50 | both halves | 5e-05 |  |
| [[A1BG]] | -0.61 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[SEC22A]] | -0.60 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[ATP5MJ]] | -0.60 | -0.46 / -0.51 | both halves | 3e-05 |  |
| [[ATP5PO]] ⚠ | -0.60 | -0.31 / -0.56 | both halves | 2e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[LAMTOR5]] | -0.60 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[OCEL1]] | -0.60 | -0.43 / -0.53 | both halves | 3e-05 |  |
| [[HEATR5B]] | -0.59 | -0.53 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers RCC2's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[PCAT1]] | B | PCAT1 activity raises RCC2's level | lines that do not express PCAT1 (11) vs lines expressing it (39) | 1.52× lower at baseline in the lines without PCAT1 | 0.097 | ⚠ within organs, on part of the lines; also absent: POU5F1B, MCF2L, LRATD2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 126]]; 39 genes; every member is in the + arm (projection on the module's main direction 0.697). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-16.2, -27.3); signed map (23.1, -30.4). **Vector** length 133, 40.8% of its response variance represented; |z| ≥ 3 in 1,246 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +10.2 | +22.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +9.2 | +15.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +9.1 | +11.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +7.3 | +7.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.0 | +17.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.5 | +4.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.1 | +8.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.6 | +3.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.5 | +3.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.6 | +4.7 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -7.5 | -18.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | -6.6 | -15.7 |
|  | [[Belinostat (drug)]] 5 µM |  | -6.6 | -11.0 |
|  | [[EX229 (drug)]] 5 µM |  | -3.9 | -3.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.8 | -6.4 |
|  | [[Belzutifan (drug)]] 5 µM |  | -3.3 | -4.2 |
|  | [[EX229 (drug)]] 0.05 µM |  | -3.1 | -3.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.0 | -3.4 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -3.0 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | regulator of chromosome condensation 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.13 — chr1:17,406,760-17,439,677 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TD-60 |
| Reactome | 17 pathways, smallest: Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal; Amplification of signal from the kinetochores; EML4 and NUDC in mitotic spindle formation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P258](https://www.uniprot.org/uniprotkb/Q9P258) (Protein RCC2):

> Multifunctional protein that may affect its functions by regulating the activity of small GTPases, such as RAC1 and RALA. Required for normal progress through the cell cycle, both during interphase and during mitosis. Required for the presence of normal levels of MAD2L1, AURKB and BIRC5 on inner centromeres during mitosis, and for normal attachment of kinetochores to mitotic spindles. Required for normal organization of the microtubule cytoskeleton in interphase cells. Functions as guanine …

**Summary**, from NCBI Gene [55920](https://www.ncbi.nlm.nih.gov/gene/55920):

> The protein encoded by this gene is a guanine exchange factor that is active on RalA, a small GTPase. The encoded protein and RalA are both essential for proper kinetochore-microtubule function in early mitosis. This protein has been shown to be a biomarker for colorectal cancer. [provided by RefSeq, Oct 2016]

**Accessions** — [HGNC:30297](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30297) · Entrez [55920](https://www.ncbi.nlm.nih.gov/gene/55920) · UniProt [Q9P258](https://www.uniprot.org/uniprotkb/Q9P258) · Ensembl [ENSG00000179051](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000179051)

## Data

Gene col 10993: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10993); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10993, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10993]; `tensor/DDL_lfc|DDL_z.npy` [10993]; `embed/gene_vectors.npy` [10993]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10993 or target_col == 10993). Every well: [[RCC2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RCC2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
