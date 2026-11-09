---
symbol: "PACSIN2"
type: "gene"
col: 1907
ensembl_id: "ENSG00000100266"
name: "protein kinase C and casein kinase substrate in neurons 2"
location: "22q13.2"
module: 97
arm: "+"
pooled_cpm: 209.79
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 12
n_dd_up_clean: 8
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 9
direction_downstream: 0
tags: ["gene", "module/097"]
generated_by: "tahoemap"
---

# PACSIN2

*protein kinase C and casein kinase substrate in neurons 2* — 22q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 2.27× (z +21.6, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.542× (z -15.5, q 0e+00, down in 39 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.612× (z -12.9, q 1e-35, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ABHD12]] (+0.67, fdr 1e-05), [[TBC1D8]] (+0.65, fdr 7e-06), [[HPCAL1]] (+0.64, fdr 1e-05); moves opposite to [[SOCS2-AS1]] (-0.60, fdr 5e-05), [[ZNF24]] (-0.59, fdr 3e-05), [[BCDIN3D]] (-0.59, fdr 1e-04).
> It is in [[Module 097]], a single-armed module (estrogen response early).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[LINC00511]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1907.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.27×** | +21.6 | 0e+00 | 48/48 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.96×** | +17.7 | 0e+00 | 47/48 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.87×** | +16.5 | 0e+00 | 45/48 (SW1417, SW480, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.17× | +5.8 | 8e-07 | 19/48 (SNU-423, SW1417, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.45×** | +5.1 | 3e-05 | 37/49 (SW480, SW1417, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +4.6 | 4e-04 | 20/48 (NCI-H23, NCI-H460, …) | two highest doses |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | 1.17× | +4.3 | 0.002 | 19/48 (NCI-H1573, Hs 766T, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | 1.18× | +4.2 | 0.002 | 20/49 (NCI-H1573, Hs 766T, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~14% of this change | 1.17× | +4.2 | 0.002 | 17/48 (SW1417, SW480, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.32×** | +3.8 | 0.008 | 22/49 (C32, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~1% of this change | 1.15× | +3.7 | 0.011 | 18/48 (SW48, NCI-H460, …) | two highest doses |  |
| [[Budesonide (drug)]] 0.05 µM |  | 1.15× | +3.6 | 0.014 | 19/48 (Hs 766T, NCI-H1573, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 5 µM |  | 1.15× | +3.6 | 0.014 | 20/48 (Hs 766T, NCI-H1573, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | 1.14× | +3.6 | 0.014 | 18/48 (A549, NCI-H1573, …) | rises with dose |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | 1.14× | +3.4 | 0.023 | 12/49 (SNU-423, COLO 205, …) | top dose only | plate-row cell shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.27×** | +3.3 | 0.030 | 19/48 (C32, SW48, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.26×** | +3.1 | 0.053 | 17/48 (SW480, SNU-423, …) | top dose only | noisy plate (z scaled) |
| [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | 1.12× | +3.0 | 0.073 | 15/50 (NCI-H1573, A498, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 10 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1907.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.542×** | -15.5 | 0e+00 | 39/44 (NCI-H23, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.564×** | -15.0 | 0e+00 | 45/49 (NCI-H2347, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.612×** | -12.9 | 1e-35 | 41/48 (PANC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.628×** | -11.3 | 2e-27 | 33/45 (NCI-H2347, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.741×** | -11.1 | 1e-26 | 32/48 (NCI-H23, SW 900, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.663×** | -10.4 | 4e-23 | 33/47 (HepG2/C3A, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.745×** | -7.7 | 9e-13 | 33/48 (LoVo, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.751×** | -7.5 | 5e-12 | 37/48 (NCI-H460, C32, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~23% of this change | **0.789×** | -6.2 | 4e-08 | 29/48 (SW 900, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **0.802×** | -5.8 | 4e-07 | 28/48 (C32, NCI-H23, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | 0.859× | -3.8 | 0.007 | 21/48 (LoVo, Hs 766T, …) | all doses, flat | composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.902× | -3.8 | 0.007 | 15/48 (Panc 03.27, NCI-H2347, …) | top dose only | low cells (technical?) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | 0.904× | -3.7 | 0.009 | 3/48 (A-427, SW 1088, …) | top dose only |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.824×** | -3.6 | 0.014 | 23/48 (C32, SK-MEL-2, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.908× | -3.6 | 0.014 | 8/49 (C32, SW 900, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.866× | -3.5 | 0.018 | 13/47 (LoVo, Panc 03.27, …) | all doses, flat | low cells (technical?) |
| [[Belumosudil (drug)]] 5 µM |  | 0.873× | -3.4 | 0.023 | 16/48 (NCI-H2347, NCI-H23, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | 0.834× | -3.3 | 0.026 | 17/47 (SW480, SNU-423, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | 0.878× | -3.3 | 0.034 | 16/47 (C32, AsPC-1, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.918× | -3.2 | 0.043 | 7/48 (SNU-1, BT-474, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.888× | -3.1 | 0.052 | 12/47 (C32, SNU-423, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.809×** | -2.9 | 0.091 | 14/48 (NCI-H1573, BT-474, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1907. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 227 | 18 | 5 (5 ⚠) | [[Citalopram (hydrobromide) (drug)]] 0.05 µM 3.15× (z +14.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.488× (z -12.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 177 | 19 | 2 (2 ⚠) | [[Triamcinolone (drug)]] 5 µM 1.70× (z +12.1) | [[Homoharringtonine (drug)]] 5 µM 0.616× (z -11.0) ⚠ cell-cycle shift, explains ~32% of this change |
| [[NCI-H460 (line)]] | wt | 114 | 17 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.67× (z +16.4) | [[Homoharringtonine (drug)]] 0.05 µM 0.512× (z -11.2) |
| [[Hs 766T (line)]] | wt | 206 | 15 | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.62× (z +13.8) | [[Homoharringtonine (drug)]] 5 µM 0.487× (z -14.4) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.537× (z -8.8) |
| [[C32 (line)]] | wt | 517 | 2 | 14 (7 ⚠) | [[TAK-901 (drug)]] 5 µM 10.3× (z +18.8) | [[Homoharringtonine (drug)]] 5 µM 0.545× (z -13.3) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.442× (z -12.7) |
| [[A498 (line)]] | wt | 267 | 13 | 2 (2 ⚠) | [[Citalopram (hydrobromide) (drug)]] 0.05 µM 1.89× (z +11.0) | [[Dinaciclib (drug)]] 0.5 µM 0.555× (z -10.1) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 190 | 11 | 1 | [[Panobinostat (drug)]] 5 µM 2.58× (z +11.3) | [[Homoharringtonine (drug)]] 0.5 µM 0.462× (z -9.3) |
| [[HS-578T (line)]] | alt | 301 | 7 | 3 (3 ⚠) | [[Budesonide (drug)]] 5 µM 2.44× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.330× (z -12.0) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 377 | 3 | 5 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 2.54× (z +15.1) | [[Dinaciclib (drug)]] 5 µM 0.397× (z -14.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.520× (z -10.5) |
| [[LoVo (line)]] | wt | 180 | 3 | 5 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.68× (z +17.5) | [[Homoharringtonine (drug)]] 5 µM 0.599× (z -13.0) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.495× (z -12.6) |
| [[SNU-423 (line)]] | alt | 261 | 4 | 4 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.09× (z +10.7) | [[Dinaciclib (drug)]] 5 µM 0.390× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.549× (z -8.9) |
| [[NCI-H2347 (line)]] | alt | 254 | 3 | 4 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 2.23× (z +13.0) | [[Dinaciclib (drug)]] 0.5 µM 0.314× (z -18.8) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 152 | 3 | 3 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.30× (z +17.1) | [[Homoharringtonine (drug)]] 0.5 µM 0.503× (z -9.9) |
| [[CFPAC-1 (line)]] | alt | 321 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.372× (z -13.1) |
| [[HOP62 (line)]] | alt | 274 | 2 | 4 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 1.99× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.375× (z -15.3) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 178 | 3 | 3 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.10× (z +12.0) | [[Dinaciclib (drug)]] 5 µM 0.520× (z -10.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.585× (z -8.6) |
| [[NCI-H23 (line)]] | alt | 121 | 3 | 3 (2 ⚠) | [[Belinostat (drug)]] 5 µM 2.29× (z +12.1) | [[Homoharringtonine (drug)]] 5 µM 0.340× (z -22.4) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.470× (z -11.1) |
| [[RKO (line)]] | wt | 145 | 5 (2 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.92× (z +13.9) | [[Dinaciclib (drug)]] 0.5 µM 0.463× (z -10.0) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 246 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.437× (z -15.6) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.418× (z -11.6) |
| [[COLO 205 (line)]] | alt | 428 | 3 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +19.4) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 6.14× (z +12.2) | [[Dinaciclib (drug)]] 0.5 µM 0.290× (z -16.0) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 226 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.56× (z +13.5) | [[Dinaciclib (drug)]] 5 µM 0.429× (z -11.6) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 230 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.31× (z +11.6) | [[Dinaciclib (drug)]] 0.5 µM 0.480× (z -10.1) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 121 | 3 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.82× (z +13.3) | [[Homoharringtonine (drug)]] 5 µM 0.434× (z -15.1) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.432× (z -10.8) |
| [[NCI-H1792 (line)]] | alt | 220 | 3 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.07× (z +9.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.533× (z -12.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.454× (z -10.7) |
| [[NCI-H2030 (line)]] | alt | 135 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.83× (z +12.7) | [[Dinaciclib (drug)]] 0.05 µM 0.367× (z -11.3) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 219 | 2 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.34× (z +11.5) | [[Dinaciclib (drug)]] 0.5 µM 0.354× (z -14.2) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 134 | 5 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.17× (z +11.8) | — |
| [[SW480 (line)]] | alt | 203 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.11× (z +21.8) | [[Dinaciclib (drug)]] 0.5 µM 0.567× (z -10.9) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 208 | 1 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 1.82× (z +9.1) | [[Dinaciclib (drug)]] 0.5 µM 0.528× (z -9.8) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 191 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.38× (z +19.1) | — |
| [[A-427 (line)]] | wt | 88.7 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.63× (z +12.2) | — |
| [[C-33 A (line)]] | alt | 134 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.46× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.432× (z -9.4) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 317 | 1 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 1.76× (z +9.1) | [[Dinaciclib (drug)]] 0.5 µM 0.412× (z -14.6) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 271 | 0 | 3 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.290× (z -13.8) ⚠ toxic |
| [[LOX-IMVI (line)]] | wt | 76.7 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.19× (z +15.7) | — |
| [[PANC-1 (line)]] | alt | 180 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.365× (z -15.7) |
| [[SHP-77 (line)]] | alt | 169 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.67× (z +13.2) | — |
| [[A-172 (line)]] | wt | 139 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +13.8) ⚠ cell-cycle shift, explains ~32% of this change | [[Dinaciclib (drug)]] 5 µM 0.406× (z -12.5) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 299 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.401× (z -10.9) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 184 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.33× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.421× (z -9.7) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 187 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.19× (z +10.1) | [[Dinaciclib (drug)]] 0.05 µM 0.415× (z -10.5) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 145 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.22× (z +9.3) | [[Homoharringtonine (drug)]] 5 µM 0.453× (z -13.0) ⚠ cell-cycle shift, explains ~32% of this change |
| [[SNU-1 (line)]] | wt | 158 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.38× (z +9.7) | — |
| [[AN3 CA (line)]] | alt | 185 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 150 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 193 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 214 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 171 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 151 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 151 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1907), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*59 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABHD12]] | +0.67 | +0.70 / +0.54 | both halves | 1e-05 |  |
| [[TBC1D8]] | +0.65 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[HPCAL1]] | +0.64 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[EFNA4]] | +0.63 | +0.57 / +0.39 | both halves | 5e-05 |  |
| [[ATP1A1]] | +0.63 | +0.69 / +0.66 | both halves | 7e-06 |  |
| [[SSBP2]] | +0.63 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[ZDHHC9]] | +0.62 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[NCOA3]] | +0.61 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[CPD]] | +0.60 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[ERGIC1]] | +0.60 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[AGFG2]] | +0.60 | +0.36 / +0.57 | both halves | 1e-04 |  |
| [[AKAP13]] | +0.59 | +0.54 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*41 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SOCS2-AS1]] | -0.60 | -0.62 / -0.39 | both halves | 5e-05 |  |
| [[ZNF24]] | -0.59 | -0.62 / -0.44 | both halves | 3e-05 |  |
| [[BCDIN3D]] | -0.59 | -0.55 / -0.34 | both halves | 1e-04 |  |
| [[HDAC9]] | -0.59 | -0.61 / -0.51 | both halves | 1e-05 |  |
| [[LINC00944]] | -0.58 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[LIG4]] | -0.58 | -0.53 / -0.39 | both halves | 5e-05 |  |
| [[PLA2G4C]] | -0.57 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[SLAMF7]] | -0.57 | -0.45 / -0.59 | both halves | 3e-05 |  |
| [[RAB30-DT]] | -0.57 | -0.55 / -0.33 | both halves | 1e-04 |  |
| [[ANKRD20A5P]] | -0.56 | -0.56 / -0.39 | both halves | 5e-05 |  |
| [[RIPK2-DT]] | -0.56 | -0.55 / -0.36 | both halves | 9e-05 |  |
| [[CSTF3]] | -0.56 | -0.52 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 6, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00511]] | B | LINC00511 activity raises PACSIN2's level | lines that do not express LINC00511 (12) vs lines expressing it (38) | 1.55× lower at baseline in the lines without LINC00511 | 0.005 | ⚠ within organs, on part of the lines; also absent: ABLIM3, LGALS3, CDK18 |
| [[MLPH]] | B | MLPH activity raises PACSIN2's level | lines that do not express MLPH (13) vs lines expressing it (37) | 1.48× lower at baseline in the lines without MLPH | 0.019 | ⚠ within organs, on part of the lines; also absent: GBP3, LGALS3, FBXO32 |
| [[TSC22D3]] | B | TSC22D3 activity raises PACSIN2's level | lines that do not express TSC22D3 (11) vs lines expressing it (39) | 1.32× lower at baseline in the lines without TSC22D3 | 0.043 | ⚠ within organs, on part of the lines; also absent: IL15, IGFBP3, PAG1; maybe low, not absent |
| [[SLAMF7]] | B | SLAMF7 activity raises PACSIN2's level | lines that do not express SLAMF7 (34) vs lines expressing it (16) | 1.33× lower at baseline in the lines without SLAMF7 | 0.045 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PSG4, AMPH, RNF17 |
| [[TBC1D8]] | B | TBC1D8 activity raises PACSIN2's level | lines that do not express TBC1D8 (6) vs lines expressing it (44) | 1.64× lower at baseline in the lines without TBC1D8 | 0.089 | ⚠ within organs, on part of the lines; also absent: SSUH2, ARHGAP26, ENSG00000251537; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity lowers PACSIN2's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PYGB]] | C | PYGB activity raises PACSIN2's level | lines that do not express PYGB (3) vs lines expressing it (47) | 1.99× lower at baseline in the lines without PYGB | 0.055 | ⚠ few lines (3 vs 47); across organs; also absent: PBX4, STX1A, UGDH; maybe low, not absent |
| [[CORO2A]] | C | CORO2A activity lowers PACSIN2's level | lines that do not express CORO2A (3) vs lines expressing it (47) | 1.84× higher at baseline in the lines without CORO2A | 0.065 | ⚠ few lines (3 vs 47); across organs; also absent: SLC4A11, NUDT7, SCAMP5; maybe low, not absent |
| [[B4GALT1]] | C | B4GALT1 activity raises PACSIN2's level | lines that do not express B4GALT1 (3) vs lines expressing it (47) | 1.63× lower at baseline in the lines without B4GALT1 | 0.099 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TIMP1, UGDH, ATXN1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 097]] — estrogen response early; 48 genes; every member is in the + arm (projection on the module's main direction 0.744). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (31.3, 12.2); signed map (12.6, 33.7). **Vector** length 141, 48.1% of its response variance represented; |z| ≥ 3 in 1,649 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +9.1 | +21.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +8.5 | +17.7 |
|  | [[Belinostat (drug)]] 5 µM |  | +8.0 | +16.5 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +6.4 | +4.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +5.8 | +4.3 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +5.6 | +3.6 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | +5.6 | +1.8 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +5.5 | +2.6 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -13.9 | -12.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -12.1 | -11.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -7.5 | -10.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -7.4 | -7.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.9 | -3.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -5.7 | -2.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.4 | -5.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.8 | -2.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.6 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | protein kinase C and casein kinase substrate in neurons 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.2 — chr22:42,835,412-43,015,149 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SDPII |
| Gene groups (HGNC) | F-BAR domain containing; SH3 domain containing |
| Reactome | 3 pathways, smallest: Clathrin-mediated endocytosis; Membrane Trafficking; Vesicle-mediated transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UNF0](https://www.uniprot.org/uniprotkb/Q9UNF0) (Protein kinase C and casein kinase substrate in neurons protein 2):

> Regulates the morphogenesis and endocytosis of caveolae (By similarity). Lipid-binding protein that is able to promote the tubulation of the phosphatidic acid-containing membranes it preferentially binds. Plays a role in intracellular vesicle-mediated transport. Involved in the endocytosis of cell-surface receptors like the EGF receptor, contributing to its internalization in the absence of EGF stimulus. Essential for endothelial organization in sprouting angiogenesis, modulates CDH5-based …

**Summary**, from NCBI Gene [11252](https://www.ncbi.nlm.nih.gov/gene/11252):

> This gene is a member of the protein kinase C and casein kinase substrate in neurons family. The encoded protein is involved in linking the actin cytoskeleton with vesicle formation by regulating tubulin polymerization. Alternative splicing results in multiple transcript variants. [provided by RefSeq, May 2010]

**Accessions** — [HGNC:8571](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8571) · Entrez [11252](https://www.ncbi.nlm.nih.gov/gene/11252) · UniProt [Q9UNF0](https://www.uniprot.org/uniprotkb/Q9UNF0) · Ensembl [ENSG00000100266](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100266)

## Data

Gene col 1907: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1907); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1907, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1907]; `tensor/DDL_lfc|DDL_z.npy` [1907]; `embed/gene_vectors.npy` [1907]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1907 or target_col == 1907). Every well: [[PACSIN2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PACSIN2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
