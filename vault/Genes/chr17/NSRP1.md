---
symbol: "NSRP1"
type: "gene"
col: 4750
ensembl_id: "ENSG00000126653"
name: "nuclear speckle splicing regulatory protein 1"
location: "17q11.2"
module: 11
arm: "+"
pooled_cpm: 173.69
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 18
n_dd_up_clean: 7
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 10
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# NSRP1

*nuclear speckle splicing regulatory protein 1* — 17q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.05× (z +19.8, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (13 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 0.520× (z -12.3, q 5e-32, down in 44 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.676× (z -7.7, q 2e-12, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRIP11]] (+0.84, fdr 7e-06), [[CCDC174]] (+0.78, fdr 7e-06), [[SNW1]] (+0.75, fdr 7e-06); moves opposite to [[RCN2]] (-0.73, fdr 7e-06), [[NAGA]] (-0.70, fdr 1e-05), [[CNPY3]] (-0.70, fdr 1e-05).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 10 go from it, the strongest it → [[LAPTM4B]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4750.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.05×** | +19.8 | 0e+00 | 48/48 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.46×** | +17.6 | 0e+00 | 48/48 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.87×** | +11.8 | 1e-29 | 46/48 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.69×** | +10.2 | 2e-22 | 47/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.64×** | +9.7 | 3e-20 | 44/48 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.46×** | +6.9 | 6e-10 | 39/47 (RKO, SW48, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **1.38×** | +6.3 | 2e-08 | 39/48 (RKO, AsPC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 13 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4750.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.520×** | -12.3 | 5e-32 | 44/47 (PANC-1, C-33 A, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.596×** | -10.1 | 1e-21 | 40/48 (PANC-1, SW 1271, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.598×** | -9.7 | 9e-20 | 42/47 (RKO, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.659×** | -7.8 | 7e-13 | 32/48 (A-427, NCI-H23, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.676×** | -7.7 | 2e-12 | 38/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.705×** | -6.8 | 8e-10 | 40/48 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.699×** | -6.7 | 1e-09 | 29/50 (NCI-H23, A-427, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.716×** | -6.5 | 5e-09 | 39/48 (RKO, SW1417, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.725×** | -6.3 | 2e-08 | 31/48 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.797×** | -6.3 | 2e-08 | 26/49 (HEC-1-A, CHP-212, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.744×** | -5.8 | 4e-07 | 38/48 (RKO, SW480, …) | all doses, stronger at high dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.585×** | -5.5 | 2e-06 | 26/38 (LOX-IMVI, HOP62, …) | rises with dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | **0.754×** | -5.3 | 5e-06 | 25/44 (C-33 A, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **0.793×** | -4.2 | 0.001 | 25/45 (RKO, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **0.805×** | -4.1 | 0.002 | 30/49 (PANC-1, NCI-H2030, …) | top dose only | plate-row cell shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.692×** | -3.8 | 0.006 | 30/48 (C32, SW48, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.711×** | -3.5 | 0.016 | 28/49 (SW1417, A-427, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.30 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4750. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 246 | 5 | 6 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +23.9) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.409× (z -13.4) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.578× (z -8.5) |
| [[RKO (line)]] | wt | 197 | 5 | 6 (6 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.65× (z +13.4) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.113× (z -28.9) ⚠ toxic |
| [[NCI-H460 (line)]] | wt | 192 | 5 | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +20.7) | [[Niclosamide (olamine) (drug)]] 5 µM 0.489× (z -10.5) ⚠ toxic · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.518× (z -10.1) |
| [[PANC-1 (line)]] | alt | 238 | 5 | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +25.5) | [[Digitoxin (drug)]] 5 µM 0.297× (z -20.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.346× (z -17.9) |
| [[HOP62 (line)]] | alt | 204 | 3 | 6 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +14.9) | [[Niclosamide (olamine) (drug)]] 5 µM 0.355× (z -14.6) ⚠ toxic · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.487× (z -10.6) |
| [[LOX-IMVI (line)]] | wt | 152 | 5 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +16.8) | [[Lonafarnib (drug)]] 5 µM 0.121× (z -14.2) ⚠ toxic |
| [[A-172 (line)]] | wt | 217 | 4 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +19.4) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.432× (z -11.2) ⚠ cell-cycle shift, explains ~28% of this change |
| [[KATO III (line)]] | alt | 297 | 2 | 6 (4 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 1.92× (z +8.9) | [[Digitoxin (drug)]] 5 µM 0.324× (z -15.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.381× (z -13.2) |
| [[LS 180 (line)]] | wt | 127 | 3 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +11.8) | [[Digitoxin (drug)]] 5 µM 0.301× (z -14.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.396× (z -10.9) |
| [[NCI-H1573 (line)]] | alt | 175 | 5 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.47× (z +30.3) | [[Niclosamide (olamine) (drug)]] 5 µM 0.444× (z -11.1) ⚠ toxic |
| [[SW480 (line)]] | alt | 177 | 3 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.77× (z +12.0) | [[Digitoxin (drug)]] 5 µM 0.442× (z -12.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.469× (z -11.2) |
| [[C32 (line)]] | wt | 176 | 3 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +12.9) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.414× (z -10.5) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Ponatinib (drug)]] 5 µM 0.435× (z -10.3) |
| [[HEC-1-A (line)]] | alt | 262 | 3 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.08× (z +11.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.505× (z -14.7) ⚠ cell-cycle shift, explains ~31% of this change |
| [[MIA PaCa-2 (line)]] | alt | 173 | 3 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.60× (z +12.7) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.433× (z -10.7) ⚠ cell-cycle shift, explains ~27% of this change |
| [[A-427 (line)]] | wt | 149 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.34× (z +11.4) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.304× (z -15.5) ⚠ cell-cycle shift, explains ~27% of this change |
| [[A498 (line)]] | wt | 209 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.74× (z +11.7) | [[Niclosamide (olamine) (drug)]] 5 µM 0.424× (z -9.5) ⚠ toxic |
| [[C-33 A (line)]] | alt | 162 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +11.7) | [[Niclosamide (olamine) (drug)]] 5 µM 0.244× (z -16.8) ⚠ toxic |
| [[COLO 205 (line)]] | alt | 243 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +17.6) | [[Dinaciclib (drug)]] 0.5 µM 0.316× (z -15.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[H4 (line)]] | wt | 170 | 2 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +10.5) | [[Niclosamide (olamine) (drug)]] 5 µM 0.281× (z -13.4) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.428× (z -9.2) |
| [[hTERT-HPNE (line)]] | wt | 177 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +11.6) | [[Digitoxin (drug)]] 5 µM 0.317× (z -13.1) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 187 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +14.1) | [[Niclosamide (olamine) (drug)]] 5 µM 0.448× (z -10.5) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 154 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.17× (z +14.1) | [[Digitoxin (drug)]] 5 µM 0.408× (z -11.0) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 159 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +15.1) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.462× (z -9.4) ⚠ cell-cycle shift, explains ~27% of this change |
| [[HCT15 (line)]] | alt | 267 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.69× (z +10.6) | [[Niclosamide (olamine) (drug)]] 5 µM 0.482× (z -9.9) ⚠ toxic |
| [[HS-578T (line)]] | alt | 166 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +17.0) | [[Digitoxin (drug)]] 5 µM 0.499× (z -8.6) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 148 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.58× (z +15.1) | [[Niclosamide (olamine) (drug)]] 5 µM 0.412× (z -13.6) ⚠ toxic |
| [[NCI-H2030 (line)]] | alt | 122 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +15.7) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.346× (z -11.4) ⚠ toxic |
| [[NCI-H2347 (line)]] | alt | 88.9 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +13.4) | — |
| [[RPMI-7951 (line)]] | alt | 181 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +15.0) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.380× (z -11.5) ⚠ cell-cycle shift, explains ~27% of this change |
| [[SW48 (line)]] | wt | 209 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +13.1) | [[Niclosamide (olamine) (drug)]] 5 µM 0.413× (z -9.1) ⚠ toxic · without an alert: [[PH-797804 (drug)]] 5 µM 0.210× (z -8.8) |
| [[A549 (line)]] | wt | 197 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.71× (z +10.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.578× (z -10.6) ⚠ cell-cycle shift, explains ~31% of this change |
| [[AsPC-1 (line)]] | alt | 105 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +17.4) | — |
| [[BT-474 (line)]] | alt | 150 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +10.4) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.437× (z -9.6) |
| [[HepG2_C3A (line)]] | wt | 80.1 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +8.7) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.215× (z -12.3) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 125 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +14.6) | — |
| [[HT-29 (line)]] | alt | 158 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +13.4) | — |
| [[SNU-1 (line)]] | wt | 162 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +13.8) | — |
| [[SW 900 (line)]] | alt | 130 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +11.5) | — |
| [[AN3 CA (line)]] | alt | 122 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +8.5) | — |
| [[CFPAC-1 (line)]] | alt | 103 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.77× (z +9.0) | — |
| [[CHP-212 (line)]] | wt | 169 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.278× (z -13.9) ⚠ cell-cycle shift, explains ~31% of this change |
| [[Panc 03.27 (line)]] | alt | 152 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.427× (z -9.9) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 168 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.74× (z +9.7) | — |
| [[SW 1271 (line)]] | alt | 184 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0428× (z -17.6) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 122 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.378× (z -11.8) ⚠ toxic; transcription drop |
| [[NCI-H2122 (line)]] | alt | 143 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 157 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 155 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4750), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRIP11]] | +0.84 | +0.85 / +0.84 | both halves | 7e-06 |  |
| [[CCDC174]] | +0.78 | +0.83 / +0.71 | both halves | 7e-06 |  |
| [[SNW1]] | +0.75 | +0.74 / +0.69 | both halves | 7e-06 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[DNTTIP2]] | +0.74 | +0.75 / +0.70 | both halves | 7e-06 |  |
| [[ESF1]] | +0.73 | +0.80 / +0.69 | both halves | 7e-06 | STRING 414 |
| [[SURF6]] | +0.73 | +0.78 / +0.66 | both halves | 7e-06 |  |
| [[CEBPZ]] | +0.72 | +0.76 / +0.68 | both halves | 7e-06 |  |
| [[FCF1]] | +0.72 | +0.81 / +0.65 | both halves | 7e-06 |  |
| [[UBXN4]] | +0.71 | +0.77 / +0.61 | both halves | 7e-06 |  |
| [[ZNF146]] | +0.71 | +0.65 / +0.69 | both halves | 7e-06 |  |
| [[TAF1]] | +0.71 | +0.74 / +0.58 | both halves | 7e-06 |  |
| [[UTP3]] | +0.71 | +0.77 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RCN2]] | -0.73 | -0.68 / -0.69 | both halves | 7e-06 |  |
| [[NAGA]] | -0.70 | -0.72 / -0.56 | both halves | 1e-05 |  |
| [[CNPY3]] | -0.70 | -0.74 / -0.56 | both halves | 1e-05 |  |
| [[COLGALT1]] | -0.70 | -0.70 / -0.65 | both halves | 7e-06 |  |
| [[SUMF2]] | -0.69 | -0.70 / -0.61 | both halves | 7e-06 |  |
| [[PPT1]] | -0.69 | -0.72 / -0.64 | both halves | 7e-06 |  |
| [[RNPEP]] | -0.68 | -0.66 / -0.68 | both halves | 7e-06 | same gene group |
| [[RPA1]] | -0.68 | -0.70 / -0.65 | both halves | 7e-06 |  |
| [[SELENON]] | -0.68 | -0.70 / -0.63 | both halves | 7e-06 |  |
| [[ERMP1]] | -0.68 | -0.61 / -0.72 | both halves | 7e-06 |  |
| [[ATP5F1B]] | -0.66 | -0.55 / -0.64 | both halves | 1e-05 |  |
| [[TMED4]] | -0.66 | -0.68 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 0, C 10.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LAPTM4B]] | C | NSRP1's natural level strengthens LAPTM4B's drug response | NSRP1's natural level across 44 lines (lineage-adjusted; a glimpse) | r +0.76, reverse -0.20; direction not clear | 0.004 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[MAN2B2]] | C | NSRP1's natural level strengthens MAN2B2's drug response | NSRP1's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.65, reverse +0.52; direction not clear | 0.048 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |
| [[COLGALT1]] | C | NSRP1's natural level strengthens COLGALT1's drug response | NSRP1's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.65, reverse +0.32; direction not clear | 0.056 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |
| cells under [[Flumatinib (mesylate) (drug)]] 0.5 µM | C | NSRP1's natural level raises the cells' numbers under Flumatinib (mesylate) 0.5 µM (protects the cells) | NSRP1's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.72 | 0.216 over the table, 0.006 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Adagrasib (drug)]] 0.5 µM | C | NSRP1's natural level lowers the cells' numbers under Adagrasib 0.5 µM (makes them more sensitive) | NSRP1's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.68 | 0.285 over the table, 0.032 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Bendamustine (drug)]] 0.5 µM | C | NSRP1's natural level lowers the cells' numbers under Bendamustine 0.5 µM (makes them more sensitive) | NSRP1's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.66 | 0.344 over the table, 0.040 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[ERK5-IN-2 (drug)]] 0.5 µM | C | NSRP1's natural level lowers the cells' numbers under ERK5-IN-2 0.5 µM (makes them more sensitive) | NSRP1's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.66 | 0.352 over the table, 0.040 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Tetracycline (hydrochloride) (drug)]] 0.5 µM | C | NSRP1's natural level raises the cells' numbers under Tetracycline (hydrochloride) 0.5 µM (protects the cells) | NSRP1's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.65 | 0.379 over the table, 0.093 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Fluvoxamine (drug)]] 0.5 µM | C | NSRP1's natural level lowers the cells' numbers under Fluvoxamine 0.5 µM (makes them more sensitive) | NSRP1's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.61 | 0.449 over the table, 0.075 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Clofarabine (drug)]] 0.5 µM | C | NSRP1's natural level lowers the cells' numbers under Clofarabine 0.5 µM (makes them more sensitive) | NSRP1's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.57 | 0.511 over the table, 0.088 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.788). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-37.1, 2.7); signed map (0.4, -17.1). **Vector** length 161, 58.2% of its response variance represented; |z| ≥ 3 in 1,149 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +18.8 | +17.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +16.0 | +19.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +13.5 | +9.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | +13.1 | +11.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +12.2 | +10.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +8.0 | +6.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +6.6 | +6.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +5.3 | +2.0 |
|  | [[Lactate (calcium) (drug)]] 0.5 µM |  | +3.2 | +2.4 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -6.1 | -12.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -5.4 | -6.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | -5.3 | -4.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -5.0 | -6.7 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -4.9 | -7.7 |
|  | [[Radotinib (drug)]] 5 µM |  | -4.0 | -2.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -3.9 | -2.7 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | -3.6 | -2.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -3.3 | -2.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.8 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | nuclear speckle splicing regulatory protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q11.2 — chr17:30,115,521-30,186,475 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP434K1421, NSrp70; previously CCDC55 |
| Gene groups (HGNC) | MicroRNA protein coding host genes |
| Reactome | 4 pathways, smallest: mRNA Splicing - Major Pathway; mRNA Splicing; Processing of Capped Intron-Containing Pre-mRNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H0G5](https://www.uniprot.org/uniprotkb/Q9H0G5) (Nuclear speckle splicing regulatory protein 1):

> RNA-binding protein that mediates pre-mRNA alternative splicing regulation. Through CCDC118 regulation, may promote pre-adipocyte differentiation (By similarity).

**Summary**, from NCBI Gene [84081](https://www.ncbi.nlm.nih.gov/gene/84081):

> Enables mRNA binding activity. Involved in developmental process and regulation of alternative mRNA splicing, via spliceosome. Located in nuclear speck. Part of ribonucleoprotein complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25305](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25305) · Entrez [84081](https://www.ncbi.nlm.nih.gov/gene/84081) · UniProt [Q9H0G5](https://www.uniprot.org/uniprotkb/Q9H0G5) · Ensembl [ENSG00000126653](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000126653)

## Data

Gene col 4750: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4750); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4750, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4750]; `tensor/DDL_lfc|DDL_z.npy` [4750]; `embed/gene_vectors.npy` [4750]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4750 or target_col == 4750). Every well: [[NSRP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NSRP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
