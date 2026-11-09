---
symbol: "REV3L"
type: "gene"
col: 187
ensembl_id: "ENSG00000009413"
name: "REV3 like, DNA directed polymerase zeta catalytic subunit"
location: "6q21"
module: 62
arm: "+"
pooled_cpm: 214.54
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 12
n_dd_up_clean: 11
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 15
direction_downstream: 0
tags: ["gene", "module/062"]
generated_by: "tahoemap"
---

# REV3L

*REV3 like, DNA directed polymerase zeta catalytic subunit* — 6q21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.35× (z +31.1, q 0e+00, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.557× (z -15.1, q 0e+00, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRAF3IP2-AS1]] (+0.70, fdr 1e-05, ⚠ same locus), [[ACTA2]] (+0.65, fdr 1e-05), [[CFAP418]] (+0.63, fdr 3e-05), [[PHYH]] (+0.63, fdr 5e-05); moves opposite to [[FBXW2]] (-0.60, fdr 4e-05), [[TPD52L2]] (-0.60, fdr 1e-05), [[CAP1]] (-0.59, fdr 5e-05).
> It is in [[Module 062]], a single-armed module (p53 targets up).
> Probable direction (from the cell lines, not proof of direct regulation): 15 arrows point to it, the strongest [[SOBP]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 187.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.35×** | +31.1 | 0e+00 | 44/48 (HEC-1-A, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.88×** | +16.2 | 0e+00 | 43/48 (MIA PaCa-2, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.55×** | +15.9 | 0e+00 | 37/49 (LoVo, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.89×** | +15.8 | 0e+00 | 42/48 (HEC-1-A, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.58×** | +11.7 | 1e-29 | 35/48 (HEC-1-A, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.51×** | +10.2 | 1e-22 | 36/48 (NCI-H460, RKO, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.09×** | +9.4 | 4e-19 | 38/49 (NCI-H460, Hs 766T, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.23×** | +7.6 | 2e-12 | 25/48 (RKO, LoVo, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.35×** | +7.4 | 7e-12 | 29/50 (RKO, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.32×** | +7.2 | 5e-11 | 29/48 (LoVo, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.25×** | +5.5 | 2e-06 | 26/47 (SNU-423, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~9% of this change | **1.23×** | +5.2 | 8e-06 | 26/48 (HEC-1-A, LoVo, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +5.1 | 2e-05 | 20/50 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~5% of this change | **1.21×** | +4.9 | 4e-05 | 26/48 (HEC-1-A, LoVo, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | 1.18× | +4.7 | 1e-04 | 19/49 (NCI-H460, SNU-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | 1.19× | +4.3 | 7e-04 | 22/47 (SW480, HS-578T, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.39×** | +4.2 | 7e-04 | 24/48 (SW48, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 1.17× | +3.8 | 0.004 | 14/48 (NCI-H460, SW480, …) | all doses, flat |  |
| [[Anethole trithione (drug)]] 0.5 µM |  | 1.16× | +3.8 | 0.004 | 7/48 (SW480, MIA PaCa-2, …) | two highest doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 6 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 187.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.557×** | -15.1 | 0e+00 | 41/48 (A-427, hTERT-HPNE, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.578×** | -13.6 | 1e-39 | 35/44 (A-427, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.621×** | -12.3 | 2e-32 | 38/48 (A-427, LOX-IMVI, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.642×** | -11.4 | 5e-28 | 40/48 (SW480, A-427, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.664×** | -10.5 | 6e-24 | 34/49 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.683×** | -9.8 | 8e-21 | 32/48 (A-427, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.808×** | -5.5 | 3e-06 | 27/48 (PANC-1, H4, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~2% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.829×** | -4.8 | 9e-05 | 22/49 (HS-578T, LOX-IMVI, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.817×** | -4.8 | 1e-04 | 23/45 (A-427, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | 0.842× | -4.3 | 0.001 | 20/48 (LoVo, hTERT-HPNE, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.955× | -4.1 | 0.002 | 0/50 | inconsistent across doses |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.814×** | -3.8 | 0.007 | 21/48 (PANC-1, SNU-1, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.756×** | -3.6 | 0.015 | 19/45 (PANC-1, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Rapamycin (drug)]] 5 µM |  | 0.908× | -3.5 | 0.018 | 6/48 (MIA PaCa-2, NCI-H460, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.828×** | -3.5 | 0.020 | 19/48 (HEC-1-A, SW48, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 187. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 496 | 1 | 12 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.60× (z +12.9) | [[Dinaciclib (drug)]] 0.5 µM 0.376× (z -19.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.506× (z -13.3) |
| [[NCI-H460 (line)]] | wt | 192 | 11 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +17.4) | [[Auranofin (drug)]] 5 µM 0.484× (z -8.8) |
| [[A-427 (line)]] | wt | 355 | 2 | 8 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +14.9) | [[Dinaciclib (drug)]] 5 µM 0.245× (z -24.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.344× (z -19.1) |
| [[HEC-1-A (line)]] | alt | 167 | 9 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.42× (z +28.1) | [[Dinaciclib (drug)]] 5 µM 0.492× (z -11.0) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 213 | 9 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.60× (z +25.4) | [[Auranofin (drug)]] 5 µM 0.466× (z -10.7) |
| [[SW480 (line)]] | alt | 197 | 4 | 6 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +16.1) | [[Auranofin (drug)]] 5 µM 0.416× (z -15.7) |
| [[SW48 (line)]] | wt | 320 | 4 | 5 (2 ⚠) | [[TAK-901 (drug)]] 0.05 µM 3.02× (z +11.7) | [[Dinaciclib (drug)]] 0.5 µM 0.302× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.345× (z -13.3) |
| [[LS 180 (line)]] | wt | 263 | 7 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.78× (z +15.5) | [[Dinaciclib (drug)]] 5 µM 0.300× (z -12.5) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 195 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +19.6) | — |
| [[SHP-77 (line)]] | alt | 559 | 0 | 8 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.240× (z -16.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.384× (z -11.6) |
| [[CHP-212 (line)]] | wt | 727 | 0 | 7 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.226× (z -12.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.300× (z -10.4) |
| [[H4 (line)]] | wt | 205 | 2 (1 ⚠) | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +11.2) | [[Panobinostat (drug)]] 0.5 µM 0.438× (z -9.1) |
| [[hTERT-HPNE (line)]] | wt | 586 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.173× (z -15.4) |
| [[NCI-H23 (line)]] | alt | 132 | 4 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.92× (z +25.0) | [[Niclosamide (olamine) (drug)]] 5 µM 0.403× (z -11.4) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.495× (z -9.1) |
| [[LOX-IMVI (line)]] | wt | 381 | 0 | 6 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.267× (z -16.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.285× (z -15.3) |
| [[SNU-1 (line)]] | wt | 224 | 4 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.12× (z +13.1) | [[Panobinostat (drug)]] 0.5 µM 0.445× (z -10.0) |
| [[SNU-423 (line)]] | alt | 209 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.50× (z +26.7) | — |
| [[A498 (line)]] | wt | 168 | 4 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +16.7) | [[Panobinostat (drug)]] 0.5 µM 0.442× (z -9.4) |
| [[HepG2_C3A (line)]] | wt | 239 | 5 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.49× (z +17.5) | — |
| [[KATO III (line)]] | alt | 143 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.54× (z +25.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 169 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.49× (z +25.5) | — |
| [[Panc 03.27 (line)]] | alt | 83.6 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +18.5) | — |
| [[AsPC-1 (line)]] | alt | 62.1 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.89× (z +21.3) | — |
| [[C32 (line)]] | wt | 491 | 1 | 3 | [[PH-797804 (drug)]] 5 µM 4.74× (z +9.0) | [[Panobinostat (drug)]] 0.5 µM 0.404× (z -10.6) |
| [[HOP62 (line)]] | alt | 106 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.92× (z +23.2) | — |
| [[Hs 766T (line)]] | wt | 227 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +10.7) | [[Auranofin (drug)]] 5 µM 0.499× (z -8.7) |
| [[HS-578T (line)]] | alt | 263 | 1 (1 ⚠) | 3 (1 ⚠) | [[Lonafarnib (drug)]] 5 µM 4.16× (z +9.6) ⚠ toxic | [[Dinaciclib (drug)]] 5 µM 0.326× (z -14.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.356× (z -14.2) |
| [[HT-29 (line)]] | alt | 146 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.55× (z +26.0) | — |
| [[A549 (line)]] | wt | 162 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +14.5) | [[Panobinostat (drug)]] 0.5 µM 0.480× (z -8.8) |
| [[C-33 A (line)]] | alt | 291 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.63× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.219× (z -19.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.485× (z -9.6) |
| [[HCT15 (line)]] | alt | 281 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.77× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.421× (z -10.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.451× (z -9.8) |
| [[NCI-H2030 (line)]] | alt | 182 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +15.0) | [[Dinaciclib (drug)]] 5 µM 0.498× (z -9.1) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 58.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.85× (z +19.9) | — |
| [[SW 900 (line)]] | alt | 139 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +16.4) | — |
| [[SW1417 (line)]] | alt | 67.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +14.8) | — |
| [[A-172 (line)]] | wt | 246 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +10.9) | [[Dinaciclib (drug)]] 5 µM 0.402× (z -10.6) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 54.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +16.7) | — |
| [[COLO 205 (line)]] | alt | 65.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.55× (z +14.7) | — |
| [[J82 (line)]] | alt | 176 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +17.5) | — |
| [[NCI-H1573 (line)]] | alt | 96.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +17.9) | — |
| [[RPMI-7951 (line)]] | alt | 230 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +15.3) | [[Panobinostat (drug)]] 0.5 µM 0.505× (z -8.9) |
| [[SK-MEL-2 (line)]] | alt | 160 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +14.8) | [[Dinaciclib (drug)]] 5 µM 0.399× (z -11.4) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 352 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.355× (z -8.5) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 135 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +8.6) | — |
| [[NCI-H1792 (line)]] | alt | 162 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +17.9) | — |
| [[NCI-H661 (line)]] | alt | 273 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.186× (z -11.7) ⚠ toxic; transcription drop |
| [[NCI-H2122 (line)]] | alt | 224 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 258 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 172 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 258 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 187), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 6 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRAF3IP2-AS1]] | +0.70 | +0.54 / +0.60 | both halves | 1e-05 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[ACTA2]] | +0.65 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[CFAP418]] | +0.63 | +0.60 / +0.44 | both halves | 3e-05 |  |
| [[PHYH]] | +0.63 | +0.67 / +0.40 | both halves | 5e-05 |  |
| [[TYMSOS]] | +0.63 | +0.63 / +0.38 | both halves | 7e-05 |  |
| [[TMEM35B]] | +0.62 | +0.52 / +0.40 | both halves | 4e-05 |  |
| [[TP53]] | +0.61 | +0.58 / +0.42 | both halves | 4e-05 | pathway: HALLMARK_DNA_REPAIR |
| [[FAS]] | +0.61 | +0.47 / +0.49 | both halves | 2e-05 |  |
| [[DRAM1]] | +0.60 | +0.61 / +0.40 | both halves | 4e-05 |  |
| [[RWDD2B]] | +0.60 | +0.58 / +0.36 | both halves | 1e-04 |  |
| [[PPP4R3A]] | +0.60 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[DDB2]] | +0.60 | +0.49 / +0.57 | both halves | 1e-05 | pathway: HALLMARK_DNA_REPAIR |
| [[ANKRD26]] | +0.59 | +0.58 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBXW2]] | -0.60 | -0.58 / -0.41 | both halves | 4e-05 | STRING 529 |
| [[TPD52L2]] | -0.60 | -0.59 / -0.52 | both halves | 1e-05 |  |
| [[CAP1]] | -0.59 | -0.64 / -0.40 | both halves | 5e-05 |  |
| [[FCHSD1]] | -0.59 | -0.53 / -0.39 | both halves | 6e-05 |  |
| [[HIF1AN]] | -0.58 | -0.52 / -0.39 | both halves | 5e-05 |  |
| [[KIF21B]] | -0.57 | -0.50 / -0.34 | both halves | 1e-04 |  |
| [[ABHD17A]] | -0.53 | -0.55 / -0.33 | both halves | 1e-04 |  |
| [[SPTLC2]] | -0.53 | -0.52 / -0.29 | both halves | 2e-04 |  |
| [[ARPC1A]] | -0.53 | -0.52 / -0.30 | both halves | 2e-04 |  |
| [[ST6GALNAC4]] | -0.53 | -0.39 / -0.34 | both halves | 1e-04 |  |
| [[PRKCZ]] | -0.53 | -0.37 / -0.39 | both halves | 8e-05 |  |
| [[SLC45A4]] | -0.53 | -0.43 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 13, C 2. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SOBP]] | B | SOBP activity raises REV3L's level | lines that do not express SOBP (19) vs lines expressing it (31) | 2.00× lower at baseline in the lines without SOBP | 0.003 | ⚠ within organs, on part of the lines; also absent: ANK2, TMEM145, SYT11 |
| [[CDCP1]] | B | CDCP1 activity lowers REV3L's level | lines that do not express CDCP1 (16) vs lines expressing it (34) | 1.99× higher at baseline in the lines without CDCP1 | 0.010 | ⚠ within organs, on part of the lines; also absent: PTK6, TNK1, CHMP4C |
| [[TOP2A]] | B | TOP2A activity lowers REV3L's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.1% of all compounds | 0.013 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SOBP]] | B | SOBP activity strengthens REV3L's drug response | lines that do not express SOBP (19) vs lines expressing it (30) | the lines without SOBP respond 1.00× as strongly (z diff +0.83); strongest at Dinaciclib 5 µM: 0.72x vs 0.44x (z diff +4.2) | 0.016 | ⚠ within organs, on part of the lines; also absent: ANK2, TMEM145, SYT11; target measured in part of the lines; artifact flags |
| [[PINCR]] | B | PINCR activity raises REV3L's level | lines that do not express PINCR (29) vs lines expressing it (21) | 1.70× lower at baseline in the lines without PINCR | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PTCHD4, ENSG00000269729, PCK1 |
| [[LHFPL6]] | B | LHFPL6 activity raises REV3L's level | lines that do not express LHFPL6 (11) vs lines expressing it (39) | 1.76× lower at baseline in the lines without LHFPL6 | 0.027 | ⚠ within organs, on part of the lines; also absent: KATNAL2, AFAP1L1, TTC7B |
| [[PINCR]] | B | PINCR activity strengthens REV3L's drug response | lines that do not express PINCR (29) vs lines expressing it (20) | the lines without PINCR respond 0.85× as strongly (z diff +0.98); strongest at Panobinostat 5 µM: 0.72x vs 0.49x (z diff +3.6) | 0.029 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PTCHD4, ENSG00000269729, PCK1; target measured in part of the lines; artifact flags |
| [[FAM13C]] | B | FAM13C activity raises REV3L's level | lines that do not express FAM13C (15) vs lines expressing it (35) | 1.85× lower at baseline in the lines without FAM13C | 0.030 | ⚠ within organs, on part of the lines; also absent: DENND2A, SOX5, ANK2; maybe low, not absent |
| [[CARD11]] | B | CARD11 activity lowers REV3L's level | lines that do not express CARD11 (33) vs lines expressing it (17) | 1.71× higher at baseline in the lines without CARD11 | 0.040 | ⚠ within organs, on part of the lines; also absent: TNFSF14, KRT81, C3 |
| [[NIBAN2]] | B | NIBAN2 activity lowers REV3L's level | lines that do not express NIBAN2 (5) vs lines expressing it (45) | 1.74× higher at baseline in the lines without NIBAN2 | 0.060 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SMOX, SLC2A1, ENSG00000281883; maybe low, not absent; its own permutation p |
| [[CDCP1]] | B | CDCP1 activity strengthens REV3L's drug response | lines that do not express CDCP1 (16) vs lines expressing it (33) | the lines without CDCP1 respond 0.90× as strongly (z diff -0.27); strongest at Idarubicin (hydrochloride) 5 µM: 1.18x vs 1.74x (z diff +4.4) | 0.063 | ⚠ within organs, on part of the lines; also absent: PTK6, TNK1, CHMP4C; target measured in part of the lines; both ways; the reference differs; artifact flags |
| [[NR2F1]] | B | NR2F1 activity raises REV3L's level | lines that do not express NR2F1 (8) vs lines expressing it (42) | 1.57× lower at baseline in the lines without NR2F1 | 0.072 | ⚠ within organs, on part of the lines; also absent: NR2F1-AS1, PCDH15; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 062]] — p53 targets up; 78 genes; every member is in the + arm (projection on the module's main direction 0.608). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-13.3, 34.8); signed map (40.2, -22.4). **Vector** length 142, 48.8% of its response variance represented; |z| ≥ 3 in 1,550 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +10.1 | +15.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +9.4 | +10.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +8.9 | +7.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +7.5 | +7.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.5 | +31.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | +5.4 | +4.7 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +4.7 | +3.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +4.6 | +3.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.4 | +4.3 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -11.7 | -15.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | -11.3 | -12.3 |
|  | [[Belinostat (drug)]] 5 µM |  | -9.2 | -9.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -8.9 | -11.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -4.1 | -1.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.9 | -1.3 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -2.9 | -0.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.6 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | REV3 like, DNA directed polymerase zeta catalytic subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q21 — chr6:111,299,028-111,483,715 (-) |
| Ensembl biotype | protein_coding |
| Also known as | POLZ, REV3 |
| Gene groups (HGNC) | DNA polymerases |
| Hallmark sets | DNA_REPAIR |
| Reactome | 12 pathways, smallest: Translesion synthesis by REV1; Translesion synthesis by POLI; Translesion synthesis by POLK |
| Matched by | ensembl_id |

**Function**, from UniProt [O60673](https://www.uniprot.org/uniprotkb/O60673) (DNA polymerase zeta catalytic subunit):

> Catalytic subunit of the DNA polymerase zeta complex, an error-prone polymerase specialized in translesion DNA synthesis (TLS). Lacks an intrinsic 3'-5' exonuclease activity and thus has no proofreading function.

**Summary**, from NCBI Gene [5980](https://www.ncbi.nlm.nih.gov/gene/5980):

> The protein encoded by this gene represents the catalytic subunit of DNA polymerase zeta, which functions in translesion DNA synthesis. The encoded protein can be found in mitochondria, where it protects DNA from damage. Defects in this gene are a cause of Mobius syndrome. [provided by RefSeq, Jan 2017]

**Accessions** — [HGNC:9968](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9968) · Entrez [5980](https://www.ncbi.nlm.nih.gov/gene/5980) · UniProt [O60673](https://www.uniprot.org/uniprotkb/O60673) · Ensembl [ENSG00000009413](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000009413)

## Data

Gene col 187: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 187); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 187, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 187]; `tensor/DDL_lfc|DDL_z.npy` [187]; `embed/gene_vectors.npy` [187]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 187 or target_col == 187). Every well: [[REV3L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/REV3L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
