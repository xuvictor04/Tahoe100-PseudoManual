---
symbol: "LSM14A"
type: "gene"
col: 15022
ensembl_id: "ENSG00000257103"
name: "LSM14A mRNA processing body assembly factor"
location: "19q13.11"
module: 28
arm: "+"
pooled_cpm: 196.52
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 11
n_dd_up_clean: 5
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# LSM14A

*LSM14A mRNA processing body assembly factor* — 19q13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (6 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.93× (z +17.7, q 0e+00, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.463× (z -20.7, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SETD2]] (+0.75, fdr 7e-06), [[SCAF11]] (+0.66, fdr 1e-05), [[CLK4]] (+0.64, fdr 1e-05); moves opposite to [[PNP]] (-0.65, fdr 7e-06), [[MLF2]] (-0.58, fdr 2e-05), [[LRRC8A]] (-0.58, fdr 1e-05).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 8 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15022.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.93×** | +17.7 | 0e+00 | 45/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.84×** | +16.4 | 0e+00 | 42/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.49×** | +15.2 | 0e+00 | 39/48 (A549, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.54×** | +11.6 | 9e-29 | 42/48 (SW480, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.06×** | +10.1 | 5e-22 | 44/49 (SW480, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.45×** | +10.0 | 2e-21 | 38/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.90×** | +9.0 | 2e-17 | 41/48 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.43×** | +8.7 | 3e-16 | 38/48 (HEC-1-A, A549, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.37×** | +8.2 | 2e-14 | 34/48 (SW480, A549, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.22×** | +5.2 | 1e-05 | 24/48 (SW480, H4, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.21×** | +5.0 | 3e-05 | 23/48 (A549, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.19× | +4.7 | 1e-04 | 23/48 (A549, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | 1.17× | +4.2 | 9e-04 | 22/47 (NCI-H460, H4, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~12% of this change | 1.14× | +3.4 | 0.027 | 15/47 (LoVo, KATO III, …) | rises with dose |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | 1.14× | +3.3 | 0.032 | 8/49 (SW480, LOX-IMVI, …) | top dose only | plate-row cell shift |
| [[Radotinib (drug)]] 5 µM |  | 1.09× | +3.2 | 0.046 | 5/48 (C32, AsPC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15022.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.463×** | -20.7 | 0e+00 | 47/48 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.501×** | -18.6 | 0e+00 | 47/48 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.635×** | -17.2 | 0e+00 | 42/49 (A-172, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.622×** | -12.8 | 4e-35 | 47/48 (HEC-1-A, SW480, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.715×** | -8.7 | 5e-16 | 39/48 (SW480, HOP62, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.822×** | -7.5 | 7e-12 | 26/48 (A-172, SNU-1, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.760×** | -7.3 | 2e-11 | 39/48 (LOX-IMVI, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~50% of this change | **0.793×** | -6.0 | 1e-07 | 29/47 (RKO, NCI-H2347, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.794×** | -6.0 | 2e-07 | 30/50 (RKO, SW480, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.873× | -5.2 | 1e-05 | 16/48 (SW480, J82, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | 0.835× | -4.8 | 7e-05 | 23/48 (HEC-1-A, C32, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | 0.836× | -4.5 | 4e-04 | 22/45 (A-172, SNU-1, …) | inconsistent across doses | composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~85% of this change | 0.895× | -4.2 | 0.001 | 9/48 (J82, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | 0.863× | -4.0 | 0.003 | 14/48 (SW1417, BT-474, …) | rises with dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.817×** | -3.9 | 0.004 | 25/47 (H4, LOX-IMVI, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | 0.879× | -3.5 | 0.018 | 11/48 (NCI-H1792, HOP62, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.879× | -3.3 | 0.026 | 15/48 (HOP62, RKO, …) | top dose only |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.798×** | -3.2 | 0.045 | 18/47 (HEC-1-A, RPMI-7951, …) | top dose only | noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | 0.859× | -2.9 | 0.089 | 14/48 (RPMI-7951, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Vilanterol (drug)]] 0.5 µM |  | 0.889× | -2.9 | 0.096 | 10/48 (SHP-77, HCT15, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, +0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15022. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 140 | 8 (4 ⚠) | 6 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 1.89× (z +11.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.89× (z +11.5) | [[Panobinostat (drug)]] 5 µM 0.435× (z -14.8) |
| [[SW480 (line)]] | alt | 238 | 8 (3 ⚠) | 6 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.09× (z +23.7) | [[Panobinostat (drug)]] 5 µM 0.409× (z -18.7) |
| [[A549 (line)]] | wt | 321 | 8 (5 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +23.7) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.85× (z +10.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.474× (z -17.8) |
| [[HEC-1-A (line)]] | alt | 298 | 5 (3 ⚠) | 6 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +21.8) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.76× (z +11.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.505× (z -19.2) |
| [[HOP62 (line)]] | alt | 277 | 4 (1 ⚠) | 6 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.41× (z +14.7) | [[Panobinostat (drug)]] 5 µM 0.364× (z -16.9) |
| [[H4 (line)]] | wt | 262 | 6 (3 ⚠) | 3 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.67× (z +12.4) | [[Panobinostat (drug)]] 0.5 µM 0.435× (z -10.5) |
| [[LOX-IMVI (line)]] | wt | 196 | 3 (1 ⚠) | 6 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.96× (z +10.4) | [[Panobinostat (drug)]] 5 µM 0.382× (z -14.9) |
| [[BT-474 (line)]] | alt | 191 | 6 (2 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +14.8) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.50× (z +13.8) | [[Lonafarnib (drug)]] 5 µM 0.0668× (z -21.2) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 5 µM 0.557× (z -8.7) |
| [[KATO III (line)]] | alt | 170 | 6 (2 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +15.4) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.56× (z +15.1) | [[Panobinostat (drug)]] 5 µM 0.480× (z -11.8) |
| [[LS 180 (line)]] | wt | 168 | 6 (2 ⚠) | 2 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.62× (z +17.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.558× (z -11.3) |
| [[SNU-1 (line)]] | wt | 226 | 2 (1 ⚠) | 6 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.32× (z +11.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.427× (z -15.6) |
| [[C-33 A (line)]] | alt | 293 | 2 (1 ⚠) | 5 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.93× (z +9.5) | [[Panobinostat (drug)]] 5 µM 0.359× (z -14.8) |
| [[LoVo (line)]] | wt | 141 | 6 (2 ⚠) | 1 | [[Digitoxin (drug)]] 5 µM 3.75× (z +20.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.58× (z +19.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.636× (z -9.9) |
| [[NCI-H23 (line)]] | alt | 181 | 4 (2 ⚠) | 3 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.90× (z +10.4) | [[Panobinostat (drug)]] 5 µM 0.529× (z -10.4) |
| [[PANC-1 (line)]] | alt | 270 | 5 (2 ⚠) | 2 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.26× (z +15.6) | [[Panobinostat (drug)]] 5 µM 0.504× (z -13.2) |
| [[A498 (line)]] | wt | 201 | 2 (2 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 1.67× (z +13.8) ⚠ cell-cycle shift, explains ~41% of this change | [[Panobinostat (drug)]] 5 µM 0.464× (z -14.6) |
| [[CFPAC-1 (line)]] | alt | 107 | 4 (2 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.77× (z +11.3) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.02× (z +9.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.495× (z -9.4) ⚠ toxic; cell-cycle shift, explains ~50% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.648× (z -8.5) |
| [[J82 (line)]] | alt | 200 | 2 (1 ⚠) | 4 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.61× (z +8.7) | [[Panobinostat (drug)]] 5 µM 0.453× (z -14.6) |
| [[MIA PaCa-2 (line)]] | alt | 241 | 1 | 5 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 2.78× (z +8.5) | [[Panobinostat (drug)]] 5 µM 0.406× (z -14.2) |
| [[RKO (line)]] | wt | 198 | 3 (2 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +14.2) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.23× (z +11.9) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.351× (z -14.8) ⚠ toxic; cell-cycle shift, explains ~50% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.511× (z -13.9) |
| [[A-172 (line)]] | wt | 198 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.427× (z -20.7) |
| [[HS-578T (line)]] | alt | 185 | 3 (2 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 1.64× (z +10.3) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.01× (z +10.2) | [[Panobinostat (drug)]] 5 µM 0.495× (z -10.2) |
| [[NCI-H1573 (line)]] | alt | 106 | 3 (1 ⚠) | 2 | [[Digitoxin (drug)]] 5 µM 2.93× (z +12.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.70× (z +11.8) | [[Panobinostat (drug)]] 5 µM 0.441× (z -9.7) |
| [[NCI-H1792 (line)]] | alt | 187 | 3 (1 ⚠) | 2 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.62× (z +13.2) | [[Panobinostat (drug)]] 0.5 µM 0.439× (z -11.2) |
| [[NCI-H2030 (line)]] | alt | 178 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.478× (z -11.7) |
| [[SW 900 (line)]] | alt | 211 | 2 (1 ⚠) | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.94× (z +8.9) | [[Panobinostat (drug)]] 0.5 µM 0.403× (z -12.1) |
| [[SW1417 (line)]] | alt | 172 | 2 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 1.70× (z +12.7) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.71× (z +9.0) | [[Panobinostat (drug)]] 0.5 µM 0.429× (z -14.2) |
| [[C32 (line)]] | wt | 166 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.379× (z -13.0) |
| [[HCT15 (line)]] | alt | 214 | 3 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.18× (z +11.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.550× (z -12.2) |
| [[HepG2_C3A (line)]] | wt | 189 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.358× (z -14.0) |
| [[hTERT-HPNE (line)]] | wt | 136 | 1 | 3 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.03× (z +8.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.532× (z -11.0) |
| [[NCI-H2347 (line)]] | alt | 139 | 0 | 4 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.484× (z -13.2) ⚠ toxic; cell-cycle shift, explains ~50% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.506× (z -12.9) |
| [[Panc 03.27 (line)]] | alt | 210 | 1 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 1.60× (z +10.0) ⚠ cell-cycle shift, explains ~41% of this change | [[Panobinostat (drug)]] 5 µM 0.435× (z -12.4) |
| [[SNU-423 (line)]] | alt | 136 | 2 (1 ⚠) | 2 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.98× (z +9.5) | [[Panobinostat (drug)]] 5 µM 0.496× (z -9.6) |
| [[SW48 (line)]] | wt | 216 | 1 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 1.64× (z +9.0) ⚠ cell-cycle shift, explains ~41% of this change | [[Panobinostat (drug)]] 5 µM 0.382× (z -12.4) |
| [[AsPC-1 (line)]] | alt | 120 | 1 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 1.57× (z +8.6) ⚠ cell-cycle shift, explains ~41% of this change | [[Panobinostat (drug)]] 5 µM 0.455× (z -10.6) |
| [[COLO 205 (line)]] | alt | 130 | 3 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.75× (z +13.0) | — |
| [[HT-29 (line)]] | alt | 266 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +13.3) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.29× (z +12.5) | — |
| [[A-427 (line)]] | wt | 227 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.461× (z -14.1) |
| [[AN3 CA (line)]] | alt | 252 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.471× (z -10.7) |
| [[Hs 766T (line)]] | wt | 136 | 1 | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.31× (z +10.9) | [[Panobinostat (drug)]] 5 µM 0.470× (z -9.7) |
| [[SHP-77 (line)]] | alt | 186 | 1 (1 ⚠) | 1 | [[Digitoxin (drug)]] 5 µM 1.89× (z +9.0) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.491× (z -9.9) |
| [[SK-MEL-2 (line)]] | alt | 137 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.457× (z -10.9) |
| [[RPMI-7951 (line)]] | alt | 190 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.514× (z -8.5) |
| [[CHP-212 (line)]] | wt | 230 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 182 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 191 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 386 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 125 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 150 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15022), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SETD2]] | +0.75 | +0.69 / +0.75 | both halves | 7e-06 |  |
| [[SCAF11]] | +0.66 | +0.68 / +0.57 | both halves | 1e-05 |  |
| [[CLK4]] | +0.64 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[SREK1]] | +0.64 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[RUFY1]] | +0.64 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[PPIG]] | +0.63 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[SRSF4]] | +0.63 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[ZNF608]] | +0.61 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[SMC3]] | +0.61 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[CEP350]] | +0.61 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[RNF214]] | +0.61 | +0.56 / +0.67 | both halves | 1e-05 |  |
| [[ZC3H7A]] | +0.60 | +0.58 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PNP]] | -0.65 | -0.58 / -0.64 | both halves | 7e-06 |  |
| [[MLF2]] | -0.58 | -0.54 / -0.46 | both halves | 2e-05 |  |
| [[LRRC8A]] | -0.58 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[C3orf52]] | -0.58 | -0.63 / -0.51 | both halves | 1e-05 |  |
| [[PRDX1]] | -0.56 | -0.53 / -0.54 | both halves | 1e-05 |  |
| [[PDE2A]] | -0.55 | -0.47 / -0.60 | both halves | 2e-05 |  |
| [[SLC35C1]] | -0.54 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[CAP1]] | -0.54 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[PIP5KL1]] | -0.53 | -0.43 / -0.54 | both halves | 3e-05 |  |
| [[TPD52L2]] | -0.53 | -0.49 / -0.39 | both halves | 6e-05 |  |
| [[LGMN]] | -0.52 | -0.46 / -0.48 | both halves | 3e-05 |  |
| [[SPSB1]] | -0.52 | -0.42 / -0.53 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises LSM14A's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.5% of all compounds | 0.008 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.616). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-24.7, 5.5); signed map (5.5, -15.0). **Vector** length 111, 38.3% of its response variance represented; |z| ≥ 3 in 1,269 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | +9.8 | +15.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +5.9 | +8.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +5.7 | -0.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +5.4 | +8.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.8 | +1.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +4.8 | +3.2 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +4.6 | -0.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.7 | +4.7 |
| fall | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.7 | -0.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -4.4 | +0.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.3 | -4.8 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.6 | -2.3 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -3.5 | -3.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -3.3 | -2.8 |
|  | [[Vilanterol (drug)]] 0.5 µM |  | -2.9 | -2.9 |
|  | [[Belzutifan (drug)]] 5 µM |  | -2.3 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | LSM14A mRNA processing body assembly factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.11 — chr19:34,172,504-34,229,288 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP434D1335, RAP55A, RAP55; previously C19orf13, FAM61A |
| Gene groups (HGNC) | LSm proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8ND56](https://www.uniprot.org/uniprotkb/Q8ND56) (Protein LSM14 homolog A):

> Essential for formation of P-bodies, cytoplasmic structures that provide storage sites for translationally inactive mRNAs and protect them from degradation. Acts as a repressor of mRNA translation. May play a role in mitotic spindle assembly.

**Summary**, from NCBI Gene [26065](https://www.ncbi.nlm.nih.gov/gene/26065):

> Sm-like proteins were identified in a variety of organisms based on sequence homology with the Sm protein family (see SNRPD2; 601061). Sm-like proteins contain the Sm sequence motif, which consists of 2 regions separated by a linker of variable length that folds as a loop. The Sm-like proteins are thought to form a stable heteromer present in tri-snRNP particles, which are important for pre-mRNA splicing.[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:24489](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24489) · Entrez [26065](https://www.ncbi.nlm.nih.gov/gene/26065) · UniProt [Q8ND56](https://www.uniprot.org/uniprotkb/Q8ND56) · Ensembl [ENSG00000257103](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000257103)

## Data

Gene col 15022: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15022); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15022, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15022]; `tensor/DDL_lfc|DDL_z.npy` [15022]; `embed/gene_vectors.npy` [15022]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15022 or target_col == 15022). Every well: [[LSM14A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LSM14A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
