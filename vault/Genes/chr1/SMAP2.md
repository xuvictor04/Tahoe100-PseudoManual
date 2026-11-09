---
symbol: "SMAP2"
type: "gene"
col: 1389
ensembl_id: "ENSG00000084070"
name: "small ArfGAP2"
location: "1p34.2"
module: 164
arm: "+"
pooled_cpm: 55.09
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 16
n_dd_up_clean: 13
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/164"]
generated_by: "tahoemap"
---

# SMAP2

*small ArfGAP2* — 1p34.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.14× (z +20.2, q 0e+00, up in 47 of 48 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.84× (z +15.3, q 0e+00, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (6 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 0.711× (z -5.8, q 3e-06, down in 27 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 0.727× (z -5.4, q 1e-05, down in 29 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HERC3]] (+0.74, fdr 7e-06), [[SPICE1]] (+0.73, fdr 7e-06), [[PEX3]] (+0.70, fdr 7e-06); moves opposite to [[FKRP]] (-0.65, fdr 1e-05), [[NUTM2B-AS1]] (-0.62, fdr 1e-05), [[DPH5-DT]] (-0.61, fdr 2e-05).
> It is in [[Module 164]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[MTOR]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 5 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1389.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **3.14×** | +20.2 | 0e+00 | 47/48 (PANC-1, LoVo, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **2.66×** | +17.3 | 0e+00 | 46/48 (PANC-1, LoVo, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **2.56×** | +16.6 | 0e+00 | 45/48 (PANC-1, LoVo, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.84×** | +15.3 | 0e+00 | 43/48 (NCI-H23, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.08×** | +12.9 | 5e-36 | 46/48 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.84×** | +10.4 | 3e-23 | 39/48 (NCI-H23, LOX-IMVI, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.68×** | +9.2 | 4e-18 | 40/48 (PANC-1, RKO, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.70×** | +9.1 | 4e-18 | 36/49 (NCI-H23, A-427, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.43×** | +8.9 | 3e-17 | 41/48 (PANC-1, RKO, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **2.28×** | +7.6 | 2e-12 | 41/49 (PANC-1, J82, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.54×** | +7.3 | 2e-11 | 35/50 (NCI-H23, NCI-H460, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.45×** | +6.6 | 2e-09 | 36/48 (A549, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.35×** | +5.3 | 5e-06 | 28/48 (RKO, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.69×** | +4.8 | 5e-05 | 23/48 (SW480, HS-578T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.39×** | +4.2 | 0.001 | 19/48 (NCI-H2030, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 1.16× | +3.6 | 0.011 | 11/48 (COLO 205, NCI-H1573, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.22×** | +3.5 | 0.013 | 16/48 (MIA PaCa-2, LOX-IMVI, …) | rises with dose |  |
| [[Fumaric acid (drug)]] 5 µM |  | **1.23×** | +3.5 | 0.016 | 12/49 (HEC-1-A, COLO 205, …) | top dose only | plate-row cell shift; position effect removed |
| [[Ipatasertib (drug)]] 0.05 µM |  | **1.21×** | +3.2 | 0.046 | 14/48 (J82, Panc 03.27, …) | inconsistent across doses |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | 1.20× | +3.1 | 0.061 | 15/49 (HEC-1-A, COLO 205, …) | top dose only | plate-row cell shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1389.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.711×** | -5.8 | 3e-06 | 27/47 (COLO 205, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.714×** | -5.5 | 1e-05 | 26/43 (LS 180, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **0.727×** | -5.4 | 1e-05 | 29/48 (NCI-H460, C32, …) | top dose only |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.744×** | -5.2 | 2e-05 | 30/48 (NCI-H460, SNU-1, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.741×** | -5.1 | 4e-05 | 23/40 (H4, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Rapamycin (drug)]] 5 µM |  | **0.819×** | -5.0 | 5e-05 | 26/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Temsirolimus (drug)]] 5 µM |  | 0.841× | -4.4 | 0.001 | 20/49 (AsPC-1, NCI-H460, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.792×** | -4.1 | 0.003 | 25/48 (C32, H4, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.802×** | -3.7 | 0.014 | 18/48 (SK-MEL-2, SNU-423, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.816×** | -3.6 | 0.017 | 16/49 (HOP62, LOX-IMVI, …) | all doses, flat |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.763×** | -3.4 | 0.032 | 18/48 (COLO 205, LoVo, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **0.697×** | -3.3 | 0.037 | 14/50 (J82, RKO, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Rapamycin (drug)]] 0.5 µM |  | **0.829×** | -3.3 | 0.037 | 17/48 (CFPAC-1, LS 180, …) | all doses, stronger at high dose |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.770×** | -3.3 | 0.038 | 15/48 (J82, LS 180, …) | two highest doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | **0.827×** | -3.2 | 0.044 | 17/47 (CFPAC-1, COLO 205, …) | all doses, flat |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.842× | -3.1 | 0.071 | 16/48 (COLO 205, HT-29, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 0.05 µM |  | **0.833×** | -3.0 | 0.079 | 11/48 (NCI-H460, C-33 A, …) | all doses, flat |  |
| [[Bisoprolol (hemifumarate) (drug)]] 5 µM |  | 0.839× | -3.0 | 0.079 | 14/47 (A549, A498, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.53 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1389. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 53.9 | 8 (5 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.97× (z +14.7) | — |
| [[COLO 205 (line)]] | alt | 126 | 0 | 7 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.378× (z -12.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[vincristine (drug)]] 5 µM 0.0904× (z -11.1) |
| [[NCI-H1573 (line)]] | alt | 34.1 | 4 (3 ⚠) | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.60× (z +10.4) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.16× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.227× (z -11.5) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 69.8 | 6 (4 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.43× (z +10.7) | — |
| [[SW480 (line)]] | alt | 63.5 | 6 (5 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.42× (z +14.3) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.12× (z +12.4) | — |
| [[A-172 (line)]] | wt | 41.4 | 1 | 4 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.47× (z +11.1) | [[Dinaciclib (drug)]] 0.05 µM 0.273× (z -10.5) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 115 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.351× (z -13.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[J82 (line)]] | alt | 50.0 | 3 (3 ⚠) | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.93× (z +10.2) ⚠ cell-cycle shift, explains ~29% of this change | [[Homoharringtonine (drug)]] 5 µM 0.420× (z -11.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 23.6 | 5 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.71× (z +15.3) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.95× (z +13.4) | — |
| [[PANC-1 (line)]] | alt | 44.2 | 5 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.59× (z +18.7) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 0.05 µM 2.50× (z +11.2) | — |
| [[A549 (line)]] | wt | 25.6 | 4 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.70× (z +10.2) | — |
| [[AsPC-1 (line)]] | alt | 31.2 | 3 (3 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.35× (z +9.3) ⚠ cell-cycle shift, explains ~29% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.301× (z -9.2) ⚠ cell-cycle shift, explains ~49% of this change |
| [[CFPAC-1 (line)]] | alt | 68.9 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.227× (z -15.1) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 66.0 | 3 (3 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.42× (z +10.4) ⚠ cell-cycle shift, explains ~29% of this change | [[Lonafarnib (drug)]] 5 µM 0.245× (z -8.6) ⚠ toxic |
| [[HOP62 (line)]] | alt | 85.3 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.315× (z -10.5) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 32.5 | 4 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.65× (z +13.3) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.22× (z +9.7) | — |
| [[LOX-IMVI (line)]] | wt | 79.3 | 4 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.30× (z +11.1) | — |
| [[LS 180 (line)]] | wt | 72.4 | 3 (2 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.72× (z +12.6) | [[Dinaciclib (drug)]] 0.05 µM 0.195× (z -13.6) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 47.7 | 4 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.80× (z +12.6) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 0.05 µM 2.47× (z +8.5) | — |
| [[SK-MEL-2 (line)]] | alt | 52.6 | 3 (3 ⚠) | 1 (1 ⚠) | [[Belinostat (drug)]] 5 µM 3.13× (z +9.4) ⚠ cell-cycle shift, explains ~29% of this change | [[Selinexor (drug)]] 5 µM 0.415× (z -10.2) ⚠ cell-cycle shift, explains ~78% of this change |
| [[A-427 (line)]] | wt | 31.9 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.07× (z +11.3) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[H4 (line)]] | wt | 119 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.113× (z -15.5) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 39.0 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.40× (z +9.6) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[KATO III (line)]] | alt | 34.9 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.96× (z +12.1) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 40.9 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.22× (z +11.8) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[NCI-H460 (line)]] | wt | 47.4 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.82× (z +14.4) | — |
| [[Panc 03.27 (line)]] | alt | 47.4 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.25× (z +10.9) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[SW1417 (line)]] | alt | 27.1 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.76× (z +10.7) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[A498 (line)]] | wt | 48.7 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.06× (z +14.7) | — |
| [[NCI-H2347 (line)]] | alt | 35.8 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.56× (z +9.7) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[SNU-1 (line)]] | wt | 38.3 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.54× (z +10.8) | — |
| [[SNU-423 (line)]] | alt | 34.8 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.49× (z +10.5) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[SW 1088 (line)]] | alt | 102 | 0 | 2 (1 ⚠) | — | [[Fostamatinib (disodium hexahydrate) (drug)]] 5 µM 0.0914× (z -8.7) ⚠ unreliable plate only · without an alert: [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.0929× (z -8.6) |
| [[BT-474 (line)]] | alt | 34.9 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.82× (z +8.5) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[C-33 A (line)]] | alt | 54.2 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.55× (z +8.5) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[CHP-212 (line)]] | wt | 38.9 | 0 | 1 | — | [[Elagolix sodium (drug)]] 0.5 µM 0.0924× (z -8.8) |
| [[Hs 766T (line)]] | wt | 45.0 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.38× (z +9.0) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 101 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -12.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 89.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.353× (z -8.5) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 80.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.92× (z +8.8) | — |
| [[SW48 (line)]] | wt | 53.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.05× (z +10.8) | — |
| [[AN3 CA (line)]] | alt | 60.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 67.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 116 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 54.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 66.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 43.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 83.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 63.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1389), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HERC3]] | +0.74 | +0.70 / +0.69 | both halves | 7e-06 |  |
| [[SPICE1]] | +0.73 | +0.68 / +0.69 | both halves | 7e-06 |  |
| [[PEX3]] | +0.70 | +0.74 / +0.63 | both halves | 7e-06 |  |
| [[CNOT8]] | +0.70 | +0.73 / +0.56 | both halves | 1e-05 |  |
| [[WDR45B]] | +0.67 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[GMCL1]] | +0.67 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[APAF1]] | +0.66 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[USP37]] | +0.66 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[INSIG2]] | +0.66 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[HDAC3]] | +0.66 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[HELZ]] | +0.66 | +0.73 / +0.56 | both halves | 1e-05 |  |
| [[SNAPC3]] | +0.65 | +0.67 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FKRP]] | -0.65 | -0.61 / -0.55 | both halves | 1e-05 |  |
| [[NUTM2B-AS1]] | -0.62 | -0.54 / -0.60 | both halves | 1e-05 |  |
| [[DPH5-DT]] | -0.61 | -0.60 / -0.48 | both halves | 2e-05 |  |
| [[DMAC2L]] | -0.60 | -0.59 / -0.51 | both halves | 1e-05 |  |
| [[NPIPB4]] | -0.60 | -0.63 / -0.48 | both halves | 2e-05 |  |
| [[ACYP2]] | -0.59 | -0.56 / -0.51 | both halves | 1e-05 |  |
| [[TIAM2]] | -0.59 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[ANKLE2]] | -0.58 | -0.48 / -0.55 | both halves | 2e-05 |  |
| [[COA7]] | -0.58 | -0.60 / -0.49 | both halves | 1e-05 |  |
| [[ST7L]] | -0.58 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[NUTM2A-AS1]] | -0.58 | -0.41 / -0.63 | both halves | 4e-05 |  |
| [[SLC25A13]] | -0.58 | -0.61 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MTOR]] | B | MTOR activity raises SMAP2's level | compounds that target MTOR: 5 of 8 lower it (Bimiralisib, GSK1059615, Rapamycin, Sapanisertib, Temsirolimus) | 62% of the class's compounds vs 3.4% of all compounds | 0.008 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[NRN1]] | B | NRN1 activity raises SMAP2's level | lines that do not express NRN1 (27) vs lines expressing it (23) | 1.45× lower at baseline in the lines without NRN1 | 0.011 | ⚠ within organs, on part of the lines; also absent: ILDR2, PHACTR1, ENSG00000250137 |
| [[DNAH14]] | B | DNAH14 activity raises SMAP2's level | lines that do not express DNAH14 (10) vs lines expressing it (40) | 1.28× lower at baseline in the lines without DNAH14 | 0.060 | ⚠ within organs, on part of the lines; also absent: ZNF345, ZNF790, ENSG00000289516; its own permutation p |
| [[TOP2A]] | B | TOP2A activity lowers SMAP2's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 164]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.810). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.37; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (8.2, -18.3); signed map (-37.6, 21.5). **Vector** length 123, 36.6% of its response variance represented; |z| ≥ 3 in 1,327 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM |  | +5.9 | +9.2 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +5.9 | +12.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.0 | +9.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +4.7 | +17.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.6 | +8.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.3 | +7.6 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | +3.4 | +3.1 |
|  | [[Ipatasertib (drug)]] 0.05 µM |  | +3.1 | +3.2 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.9 | +4.2 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -8.3 | -0.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | -7.5 | -1.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -6.8 | -5.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | -5.9 | -5.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -5.5 | -5.8 |
|  | [[Rapamycin (drug)]] 5 µM |  | -4.9 | -5.0 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -3.9 | -2.3 |
|  | [[Temsirolimus (drug)]] 5 µM |  | -3.9 | -4.4 |

## What is on record

|  |  |
|---|---|
| Name | small ArfGAP2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.2 — chr1:40,344,850-40,423,326 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously SMAP1L |
| Gene groups (HGNC) | ArfGAPs |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WU79](https://www.uniprot.org/uniprotkb/Q8WU79) (Stromal membrane-associated protein 2):

> GTPase activating protein that acts on ARF1. Can also activate ARF6 (in vitro). May play a role in clathrin-dependent retrograde transport from early endosomes to the trans-Golgi network (By similarity).

**Summary**, from NCBI Gene [64744](https://www.ncbi.nlm.nih.gov/gene/64744):

> Predicted to enable GTPase activator activity. Located in cytosol. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25082](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25082) · Entrez [64744](https://www.ncbi.nlm.nih.gov/gene/64744) · UniProt [Q8WU79](https://www.uniprot.org/uniprotkb/Q8WU79) · Ensembl [ENSG00000084070](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000084070)

## Data

Gene col 1389: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1389); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1389, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1389]; `tensor/DDL_lfc|DDL_z.npy` [1389]; `embed/gene_vectors.npy` [1389]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1389 or target_col == 1389). Every well: [[SMAP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SMAP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
