---
symbol: "ABCB9"
type: "gene"
col: 7470
ensembl_id: "ENSG00000150967"
name: "ATP binding cassette subfamily B member 9"
location: "12q24.31"
module: 79
arm: "+"
pooled_cpm: 22.95
n_lines_expressing: 49
n_dd_up: 13
n_dd_down: 30
n_dd_up_clean: 11
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/079"]
generated_by: "tahoemap"
---

# ABCB9

*ATP binding cassette subfamily B member 9* — 12q24.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 5.39× (z +32.1, q 0e+00, up in 47 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.494× (z -13.4, q 3e-38, down in 31 of 40 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.609× (z -9.4, q 6e-19, down in 27 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF511]] (+0.74, fdr 8e-06), [[HILPDA]] (+0.72, fdr 7e-06), [[RAB3A]] (+0.72, fdr 1e-05); moves opposite to [[ZMYND11]] (-0.72, fdr 9e-06), [[DPH5-DT]] (-0.69, fdr 3e-05), [[ANKRD40]] (-0.67, fdr 1e-05).
> It is in [[Module 079]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[BIK]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7470.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **5.39×** | +32.1 | 0e+00 | 47/47 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **4.97×** | +30.6 | 0e+00 | 47/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **4.38×** | +28.2 | 0e+00 | 46/47 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.86×** | +11.9 | 3e-30 | 41/47 (A498, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.48×** | +10.6 | 2e-24 | 33/47 (KATO III, MIA PaCa-2, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **2.48×** | +9.1 | 1e-17 | 35/47 (PANC-1, AsPC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.46×** | +7.3 | 3e-11 | 34/46 (A498, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.22×** | +5.3 | 7e-06 | 20/47 (NCI-H460, A549, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.70×** | +5.3 | 7e-06 | 19/46 (NCI-H2347, CFPAC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.31×** | +5.1 | 2e-05 | 19/47 (LS 180, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.29×** | +4.8 | 8e-05 | 16/47 (NCI-H2347, SW480, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~74% of this change | **1.25×** | +3.8 | 0.008 | 19/44 (LoVo, A498, …) | all doses, stronger at high dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.45×** | +3.7 | 0.008 | 13/45 (HOP62, NCI-H1792, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 14 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7470.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.494×** | -13.4 | 3e-38 | 31/40 (NCI-H2347, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.454×** | -13.0 | 3e-36 | 26/33 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.472×** | -12.4 | 7e-33 | 31/46 (BT-474, HCT15, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.609×** | -9.4 | 6e-19 | 27/46 (HCT15, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.627×** | -8.9 | 8e-17 | 27/47 (A498, PANC-1, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.598×** | -8.4 | 3e-15 | 29/46 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.627×** | -8.2 | 2e-14 | 21/38 (SW 900, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.455×** | -7.8 | 3e-13 | 31/47 (NCI-H2347, PANC-1, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.662×** | -7.8 | 3e-13 | 30/47 (LOX-IMVI, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.705×** | -6.6 | 2e-09 | 25/47 (PANC-1, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.718×** | -6.3 | 2e-08 | 22/47 (SNU-423, SW 1088, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.724×** | -6.1 | 4e-08 | 22/47 (NCI-H1573, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.740×** | -5.7 | 5e-07 | 20/46 (PANC-1, C32, …) | two highest doses |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | **0.749×** | -5.5 | 2e-06 | 20/45 (COLO 205, C-33 A, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.815×** | -5.5 | 2e-06 | 23/46 (PANC-1, H4, …) | all doses, stronger at high dose | composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **0.728×** | -5.2 | 7e-06 | 22/47 (C32, NCI-H1792, …) | top dose only |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.739×** | -5.0 | 2e-05 | 15/46 (PANC-1, LOX-IMVI, …) | two highest doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.770×** | -5.0 | 2e-05 | 21/47 (CFPAC-1, CHP-212, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.613×** | -4.9 | 3e-05 | 22/46 (C32, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.838× | -4.7 | 7e-05 | 19/47 (CFPAC-1, PANC-1, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.762×** | -4.5 | 2e-04 | 18/47 (SK-MEL-2, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.43 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7470. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 30.5 | 3 | 8 (4 ⚠) | [[Belinostat (drug)]] 5 µM 4.32× (z +15.4) | [[Homoharringtonine (drug)]] 5 µM 0.399× (z -13.6) ⚠ cell-cycle shift, explains ~55% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.335× (z -11.4) |
| [[NCI-H2347 (line)]] | alt | 28.8 | 3 | 5 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 5.50× (z +15.7) | [[Dinaciclib (drug)]] 0.5 µM 0.242× (z -13.0) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.310× (z -9.3) |
| [[NCI-H460 (line)]] | wt | 24.2 | 4 (1 ⚠) | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 5.92× (z +16.0) | [[Dinaciclib (drug)]] 0.05 µM 0.211× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.375× (z -8.8) |
| [[A-427 (line)]] | wt | 18.2 | 3 | 2 | [[Panobinostat (drug)]] 0.5 µM 5.18× (z +11.4) | [[Homoharringtonine (drug)]] 0.5 µM 0.247× (z -9.7) |
| [[A498 (line)]] | wt | 14.5 | 4 (1 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 7.02× (z +13.8) | [[Harringtonine (drug)]] 0.5 µM 0.230× (z -10.4) |
| [[CFPAC-1 (line)]] | alt | 33.2 | 3 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.82× (z +12.7) | [[Dinaciclib (drug)]] 5 µM 0.239× (z -9.9) ⚠ toxic; transcription drop · without an alert: [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.302× (z -9.6) |
| [[NCI-H1792 (line)]] | alt | 28.6 | 3 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.40× (z +11.8) | [[Dinaciclib (drug)]] 0.5 µM 0.206× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.286× (z -8.8) |
| [[SW480 (line)]] | alt | 15.8 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 9.70× (z +18.1) | [[Dinaciclib (drug)]] 5 µM 0.153× (z -12.9) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 15.1 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 9.76× (z +14.5) | — |
| [[BT-474 (line)]] | alt | 27.7 | 3 | 1 (1 ⚠) | [[Belinostat (drug)]] 5 µM 5.28× (z +10.7) | [[Niclosamide (olamine) (drug)]] 5 µM 0.107× (z -12.4) ⚠ toxic |
| [[C-33 A (line)]] | alt | 36.6 | 1 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 4.12× (z +8.5) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.134× (z -10.5) ⚠ toxic; cell-cycle shift, explains ~74% of this change |
| [[HEC-1-A (line)]] | alt | 23.2 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.10× (z +13.8) | [[Dinaciclib (drug)]] 0.05 µM 0.253× (z -10.7) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 18.5 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 7.21× (z +11.2) | [[Dinaciclib (drug)]] 0.5 µM 0.197× (z -9.2) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 19.0 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 7.71× (z +13.4) | — |
| [[LoVo (line)]] | wt | 17.8 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 9.11× (z +16.5) | — |
| [[LOX-IMVI (line)]] | wt | 20.9 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 8.01× (z +15.1) | [[Niclosamide (olamine) (drug)]] 5 µM 0.198× (z -10.1) ⚠ toxic |
| [[LS 180 (line)]] | wt | 21.0 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.86× (z +12.1) | [[Dinaciclib (drug)]] 5 µM 0.185× (z -10.0) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 30.9 | 3 | 1 (1 ⚠) | [[Belinostat (drug)]] 5 µM 6.03× (z +13.5) | [[Dinaciclib (drug)]] 5 µM 0.0895× (z -15.7) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 18.2 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 8.60× (z +12.8) | [[Dinaciclib (drug)]] 0.05 µM 0.176× (z -9.5) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 26.0 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.42× (z +13.1) | [[Dinaciclib (drug)]] 5 µM 0.239× (z -9.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 17.0 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 5.69× (z +11.3) | — |
| [[AsPC-1 (line)]] | alt | 10.1 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 19.3× (z +13.8) | — |
| [[COLO 205 (line)]] | alt | 22.5 | 2 | 1 | [[Panobinostat (drug)]] 0.5 µM 6.63× (z +10.7) | [[Temsirolimus (drug)]] 0.5 µM 0.201× (z -9.1) |
| [[HCT15 (line)]] | alt | 39.6 | 1 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.84× (z +8.8) | [[Homoharringtonine (drug)]] 0.5 µM 0.142× (z -12.8) |
| [[HepG2_C3A (line)]] | wt | 28.2 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 8.21× (z +11.9) | — |
| [[HOP62 (line)]] | alt | 23.8 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.29× (z +14.3) | — |
| [[HT-29 (line)]] | alt | 19.4 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 7.91× (z +15.3) | — |
| [[hTERT-HPNE (line)]] | wt | 23.3 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.123× (z -9.7) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 19.6 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.55× (z +12.3) | — |
| [[NCI-H1573 (line)]] | alt | 13.6 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 9.79× (z +13.9) | — |
| [[NCI-H2030 (line)]] | alt | 19.9 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 6.04× (z +13.4) | — |
| [[NCI-H23 (line)]] | alt | 22.2 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 6.00× (z +12.6) | — |
| [[RKO (line)]] | wt | 21.5 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 6.26× (z +11.2) | — |
| [[SK-MEL-2 (line)]] | alt | 25.9 | 1 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.79× (z +9.6) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.101× (z -12.1) |
| [[SNU-423 (line)]] | alt | 27.2 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.42× (z +11.6) | — |
| [[SW 900 (line)]] | alt | 21.6 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.27× (z +9.9) | [[Dinaciclib (drug)]] 0.05 µM 0.0904× (z -13.2) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 30.9 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 5.65× (z +9.3) | — |
| [[AN3 CA (line)]] | alt | 24.9 | 0 | 1 | — | [[Malotilate (drug)]] 0.05 µM 0.0806× (z -8.5) |
| [[C32 (line)]] | wt | 48.3 | 0 | 1 | — | [[Belumosudil (drug)]] 5 µM 0.286× (z -8.6) |
| [[CHP-212 (line)]] | wt | 32.0 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.0907× (z -8.9) |
| [[H4 (line)]] | wt | 27.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -10.2) ⚠ cell-cycle shift, explains ~55% of this change |
| [[RPMI-7951 (line)]] | alt | 35.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.228× (z -9.9) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 35.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.115× (z -10.4) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 3.93 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 24.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7470), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF511]] | +0.74 | +0.57 / +0.61 | both halves | 8e-06 |  |
| [[HILPDA]] | +0.72 | +0.69 / +0.61 | both halves | 7e-06 |  |
| [[RAB3A]] | +0.72 | +0.57 / +0.66 | both halves | 1e-05 |  |
| [[VKORC1]] | +0.72 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[PFKFB4]] | +0.72 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[ALDOC]] | +0.71 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[AHDC1]] | +0.70 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[ANKRD37]] | +0.70 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[SEPTIN6]] | +0.69 | +0.67 / +0.57 | both halves | 1e-05 |  |
| [[PDK3]] | +0.69 | +0.66 / +0.57 | both halves | 1e-05 |  |
| [[FAM162A]] | +0.68 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[ENO2]] | +0.67 | +0.66 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZMYND11]] | -0.72 | -0.57 / -0.65 | both halves | 9e-06 |  |
| [[DPH5-DT]] | -0.69 | -0.60 / -0.46 | both halves | 3e-05 |  |
| [[ANKRD40]] | -0.67 | -0.61 / -0.56 | both halves | 1e-05 |  |
| [[IQCH-AS1]] | -0.67 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[ENOX2]] | -0.65 | -0.61 / -0.45 | both halves | 3e-05 |  |
| [[PSME3IP1]] | -0.64 | -0.48 / -0.57 | both halves | 2e-05 |  |
| [[FAIM]] | -0.64 | -0.56 / -0.46 | both halves | 3e-05 |  |
| [[ZSCAN29]] | -0.63 | -0.54 / -0.46 | both halves | 2e-05 |  |
| [[DPY19L1P2]] | -0.62 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[AVEN]] | -0.61 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[ATE1]] | -0.61 | -0.40 / -0.57 | both halves | 5e-05 |  |
| [[TRIM44]] | -0.61 | -0.50 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BIK]] | B | BIK activity strengthens ABCB9's drug response | lines that do not express BIK (14) vs lines expressing it (33) | the lines without BIK respond 0.89× as strongly (z diff +0.41); strongest at Panobinostat 0.05 µM: 1.50x vs 2.05x (z diff +1.5) | 0.084 | ⚠ within organs, on part of the lines; also absent: PRRG4, DMTN, LAMA3; target measured in part of the lines; artifact flags |
| [[TLE6]] | C | TLE6 activity raises ABCB9's level | lines that do not express TLE6 (3) vs lines expressing it (47) | 1.47× lower at baseline in the lines without TLE6 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ZNF675, FOXRED2, MID1; maybe low, not absent; its own permutation p |
| [[SMARCD3]] | C | SMARCD3 activity raises ABCB9's level | lines that do not express SMARCD3 (3) vs lines expressing it (47) | 1.46× lower at baseline in the lines without SMARCD3 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 079]] — hypoxia; 57 genes; every member is in the + arm (projection on the module's main direction 0.706). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (11.4, -14.2); signed map (-33.5, 21.7). **Vector** length 110, 29.7% of its response variance represented; |z| ≥ 3 in 1,240 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *hypoxia* (control, mean cos +0.54 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +5.8 | +28.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.7 | +30.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.5 | +32.1 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.3 | +11.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.6 | +10.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.3 | +3.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.6 | +9.1 |
|  | [[Fumaric acid (drug)]] 5 µM |  | +2.3 | +1.7 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.2 | +5.3 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.0 | -13.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.0 | -9.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -6.0 | -13.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -5.9 | -12.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -5.7 | -5.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.8 | -4.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.7 | -4.0 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -3.4 | -2.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.0 | -5.0 |

## What is on record

|  |  |
|---|---|
| Name | ATP binding cassette subfamily B member 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.31 — chr12:122,920,951-122,981,649 (-) |
| Ensembl biotype | protein_coding |
| Also known as | EST122234 |
| Gene groups (HGNC) | ATP binding cassette subfamily B |
| Hallmark sets | PEROXISOME |
| Reactome | 2 pathways, smallest: ABC-family protein mediated transport; Transport of small molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NP78](https://www.uniprot.org/uniprotkb/Q9NP78) (ABC-type oligopeptide transporter ABCB9):

> ATP-dependent low-affinity peptide transporter which translocates a broad spectrum of peptides from the cytosol to the lysosomal lumen for degradation. Displays a broad peptide length specificity from 6-mer up to at least 59-mer peptides with an optimum of 23-mers. Binds and transports smaller and larger peptides with the same affinity. Favors positively charged, aromatic or hydrophobic residues in the N- and C-terminal positions whereas negatively charged residues as well as asparagine and …

**Summary**, from NCBI Gene [23457](https://www.ncbi.nlm.nih.gov/gene/23457):

> The membrane-associated protein encoded by this gene is a member of the superfamily of ATP-binding cassette (ABC) transporters. ABC proteins transport various molecules across extra- and intra-cellular membranes. ABC genes are divided into seven distinct subfamilies (ABC1, MDR/TAP, MRP, ALD, OABP, GCN20, White). This protein is a member of the MDR/TAP subfamily. Members of the MDR/TAP subfamily are involved in multidrug resistance as well as antigen presentation. This family member functions in …

**Accessions** — [HGNC:50](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:50) · Entrez [23457](https://www.ncbi.nlm.nih.gov/gene/23457) · UniProt [Q9NP78](https://www.uniprot.org/uniprotkb/Q9NP78) · Ensembl [ENSG00000150967](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000150967)

## Data

Gene col 7470: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7470); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7470, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7470]; `tensor/DDL_lfc|DDL_z.npy` [7470]; `embed/gene_vectors.npy` [7470]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7470 or target_col == 7470). Every well: [[ABCB9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ABCB9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
