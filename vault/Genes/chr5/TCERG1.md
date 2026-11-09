---
symbol: "TCERG1"
type: "gene"
col: 3489
ensembl_id: "ENSG00000113649"
name: "transcription elongation regulator 1"
location: "5q32"
module: 1
arm: "+"
pooled_cpm: 207.2
n_lines_expressing: 50
n_dd_up: 29
n_dd_down: 14
n_dd_up_clean: 18
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# TCERG1

*transcription elongation regulator 1* — 5q32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (11 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.87× (z +16.7, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.527× (z -24.3, q 0e+00, down in 46 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NAA15]] (+0.83, fdr 7e-06), [[ABCE1]] (+0.79, fdr 7e-06), [[LTV1]] (+0.78, fdr 7e-06); moves opposite to [[NARF]] (-0.68, fdr 7e-06), [[AAMDC]] (-0.65, fdr 1e-05), [[ZFYVE1]] (-0.63, fdr 7e-06).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TERT]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 45 in all, 12 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3489.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.87×** | +16.7 | 0e+00 | 47/48 (LS 180, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **3.28×** | +16.6 | 0e+00 | 48/49 (SW480, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.53×** | +16.1 | 0e+00 | 39/48 (A-172, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.82×** | +16.0 | 0e+00 | 47/48 (A-172, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.92×** | +15.0 | 0e+00 | 46/48 (SW480, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.64×** | +13.2 | 1e-37 | 47/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.62×** | +13.0 | 2e-36 | 47/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.56×** | +11.9 | 1e-30 | 40/48 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.54×** | +11.5 | 7e-29 | 43/48 (A-172, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.50×** | +10.8 | 2e-25 | 47/48 (NCI-H460, CFPAC-1, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.51×** | +10.7 | 8e-25 | 43/47 (LoVo, COLO 205, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.49×** | +10.2 | 1e-22 | 41/48 (A-172, NCI-H1792, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.44×** | +9.0 | 8e-18 | 36/45 (NCI-H1792, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~18% here); composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.86×** | +8.7 | 2e-16 | 30/38 (NCI-H1573, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.37×** | +7.9 | 9e-14 | 35/48 (SNU-423, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.33×** | +7.7 | 5e-13 | 37/48 (A-172, SW480, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.69×** | +7.3 | 8e-12 | 43/48 (CFPAC-1, HT-29, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.51×** | +5.8 | 2e-07 | 39/48 (NCI-H460, CFPAC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.50×** | +5.7 | 3e-07 | 35/48 (NCI-H460, Hs 766T, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.32×** | +5.3 | 2e-06 | 36/48 (NCI-H460, SW 900, …) | rises with dose | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.46×** | +5.3 | 3e-06 | 36/48 (NCI-H460, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.19× | +4.7 | 5e-05 | 22/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3489.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.527×** | -24.3 | 0e+00 | 46/49 (RKO, A498, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.495×** | -18.9 | 0e+00 | 47/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.507×** | -18.2 | 0e+00 | 48/48 (SW480, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.582×** | -14.5 | 1e-45 | 43/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.753×** | -10.8 | 5e-25 | 42/48 (SW480, LS 180, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.691×** | -9.6 | 1e-19 | 37/48 (HOP62, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.716×** | -9.0 | 2e-17 | 38/48 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.717×** | -8.6 | 5e-16 | 38/50 (SW480, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.780×** | -6.7 | 2e-09 | 38/49 (Hs 766T, SW480, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.808×** | -5.7 | 6e-07 | 27/48 (A498, CHP-212, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.688×** | -5.3 | 7e-06 | 32/49 (SW480, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~95% of this change | 0.883× | -4.7 | 1e-04 | 14/48 (RKO, LoVo, …) | top dose only | low cells (technical?) |
| [[Entrectinib (drug)]] 5 µM |  | 0.846× | -4.5 | 3e-04 | 16/48 (KATO III, A-172, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.796×** | -4.4 | 5e-04 | 28/48 (AsPC-1, COLO 205, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.852× | -4.3 | 6e-04 | 15/47 (LoVo, Hs 766T, …) | two highest doses | low cells (technical?) |
| [[Cobimetinib (drug)]] 5 µM |  | 0.851× | -4.2 | 0.001 | 19/47 (LoVo, HOP62, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.870× | -4.2 | 0.001 | 12/48 (LoVo, SW480, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.00 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3489. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 260 | 14 (7 ⚠) | 7 | [[Digitoxin (drug)]] 0.5 µM 2.14× (z +15.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.454× (z -23.2) |
| [[NCI-H460 (line)]] | wt | 226 | 14 (7 ⚠) | 5 | [[Digitoxin (drug)]] 0.05 µM 2.35× (z +12.7) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 2.25× (z +12.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.494× (z -14.7) |
| [[PANC-1 (line)]] | alt | 210 | 10 (2 ⚠) | 5 | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +17.7) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.27× (z +15.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.493× (z -18.4) |
| [[A-172 (line)]] | wt | 248 | 9 (2 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +21.3) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.35× (z +15.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.409× (z -22.8) |
| [[LS 180 (line)]] | wt | 162 | 8 (2 ⚠) | 5 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.32× (z +17.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.480× (z -15.5) |
| [[NCI-H1573 (line)]] | alt | 165 | 13 (6 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.04× (z +15.6) | — |
| [[LoVo (line)]] | wt | 276 | 8 (3 ⚠) | 4 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.50× (z +17.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.514× (z -18.1) |
| [[LOX-IMVI (line)]] | wt | 203 | 6 (1 ⚠) | 5 | [[TAK-901 (drug)]] 0.05 µM 2.69× (z +12.3) | [[Panobinostat (drug)]] 5 µM 0.402× (z -12.0) |
| [[NCI-H23 (line)]] | alt | 230 | 7 (2 ⚠) | 4 | [[Homoharringtonine (drug)]] 0.5 µM 2.44× (z +13.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.471× (z -16.7) |
| [[HEC-1-A (line)]] | alt | 294 | 5 (1 ⚠) | 5 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 4.26× (z +12.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.409× (z -21.1) |
| [[HOP62 (line)]] | alt | 170 | 6 (1 ⚠) | 4 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.19× (z +12.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.458× (z -17.4) |
| [[Hs 766T (line)]] | wt | 166 | 9 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 0.5 µM 2.52× (z +12.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.481× (z -13.5) |
| [[NCI-H1792 (line)]] | alt | 150 | 9 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.99× (z +12.7) | — |
| [[SW48 (line)]] | wt | 286 | 3 | 6 (1 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.28× (z +10.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.368× (z -18.9) |
| [[A498 (line)]] | wt | 214 | 2 (1 ⚠) | 6 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.51× (z +10.8) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 1.77× (z +10.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.403× (z -24.1) |
| [[RKO (line)]] | wt | 306 | 2 | 6 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 4.83× (z +12.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.331× (z -24.2) |
| [[HS-578T (line)]] | alt | 172 | 4 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 0.5 µM 2.40× (z +12.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.496× (z -14.1) |
| [[HT-29 (line)]] | alt | 134 | 6 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +12.3) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.29× (z +10.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.556× (z -10.7) |
| [[KATO III (line)]] | alt | 155 | 3 | 4 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.01× (z +10.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.531× (z -13.2) |
| [[MIA PaCa-2 (line)]] | alt | 260 | 3 | 4 | [[PH-797804 (drug)]] 5 µM 3.26× (z +9.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.471× (z -15.9) |
| [[Panc 03.27 (line)]] | alt | 183 | 5 (2 ⚠) | 2 | [[Homoharringtonine (drug)]] 0.5 µM 2.43× (z +14.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.601× (z -11.7) |
| [[SW1417 (line)]] | alt | 317 | 2 | 5 | [[PH-797804 (drug)]] 5 µM 2.81× (z +8.6) | [[Panobinostat (drug)]] 0.5 µM 0.413× (z -14.2) |
| [[BT-474 (line)]] | alt | 217 | 3 | 3 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.44× (z +9.6) | [[Panobinostat (drug)]] 0.5 µM 0.438× (z -12.3) |
| [[H4 (line)]] | wt | 186 | 2 | 4 | [[Homoharringtonine (drug)]] 0.5 µM 2.43× (z +9.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.397× (z -13.8) |
| [[SHP-77 (line)]] | alt | 215 | 2 (1 ⚠) | 4 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.72× (z +8.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.633× (z -10.7) |
| [[SK-MEL-2 (line)]] | alt | 253 | 2 | 4 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.74× (z +8.9) | [[Panobinostat (drug)]] 0.5 µM 0.395× (z -14.9) |
| [[A549 (line)]] | wt | 210 | 2 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +13.7) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.21× (z +9.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.430× (z -14.9) |
| [[AsPC-1 (line)]] | alt | 210 | 1 (1 ⚠) | 4 | [[Dinaciclib (drug)]] 0.05 µM 1.90× (z +8.5) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.477× (z -15.1) |
| [[CFPAC-1 (line)]] | alt | 149 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.08× (z +15.0) | — |
| [[HCT15 (line)]] | alt | 191 | 4 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +11.2) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.22× (z +10.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.539× (z -11.3) |
| [[SNU-423 (line)]] | alt | 136 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +12.8) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.16× (z +10.5) | — |
| [[C-33 A (line)]] | alt | 216 | 1 | 3 | [[PH-797804 (drug)]] 5 µM 3.51× (z +8.6) | [[Panobinostat (drug)]] 0.5 µM 0.411× (z -11.6) |
| [[C32 (line)]] | wt | 147 | 3 (1 ⚠) | 1 | [[PH-797804 (drug)]] 5 µM 4.65× (z +10.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.601× (z -9.0) |
| [[COLO 205 (line)]] | alt | 137 | 4 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.31× (z +12.9) ⚠ toxic · without an alert: [[TAK-901 (drug)]] 5 µM 6.75× (z +11.1) | — |
| [[HepG2_C3A (line)]] | wt | 176 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.577× (z -9.8) |
| [[J82 (line)]] | alt | 240 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.510× (z -16.9) |
| [[NCI-H2030 (line)]] | alt | 185 | 3 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +12.8) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.19× (z +9.4) | [[Panobinostat (drug)]] 0.5 µM 0.488× (z -8.6) |
| [[A-427 (line)]] | wt | 202 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.414× (z -14.4) |
| [[SNU-1 (line)]] | wt | 245 | 1 | 2 | [[TAK-901 (drug)]] 5 µM 4.41× (z +9.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.592× (z -9.3) |
| [[AN3 CA (line)]] | alt | 291 | 0 | 2 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.295× (z -11.6) |
| [[CHP-212 (line)]] | wt | 271 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.251× (z -17.2) |
| [[hTERT-HPNE (line)]] | wt | 134 | 1 | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.20× (z +9.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.484× (z -12.0) |
| [[NCI-H2347 (line)]] | alt | 163 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.65× (z +9.0) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.02× (z +9.0) | — |
| [[RPMI-7951 (line)]] | alt | 161 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.505× (z -12.0) |
| [[NCI-H596 (line)]] | alt | 206 | 0 | 1 | — | [[Salicylic acid (drug)]] 0.5 µM 0.399× (z -8.5) |
| [[NCI-H2122 (line)]] | alt | 173 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 184 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 168 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 234 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 149 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3489), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NAA15]] | +0.83 | +0.80 / +0.84 | both halves | 7e-06 |  |
| [[ABCE1]] | +0.79 | +0.71 / +0.79 | both halves | 7e-06 |  |
| [[LTV1]] | +0.78 | +0.72 / +0.77 | both halves | 7e-06 |  |
| [[RAD51D]] | +0.76 | +0.69 / +0.72 | both halves | 7e-06 |  |
| [[NAA25]] | +0.75 | +0.74 / +0.78 | both halves | 7e-06 |  |
| [[RRP15]] | +0.72 | +0.64 / +0.72 | both halves | 7e-06 |  |
| [[MAK16]] | +0.70 | +0.66 / +0.68 | both halves | 7e-06 |  |
| [[METAP1D]] | +0.70 | +0.59 / +0.74 | both halves | 7e-06 |  |
| [[PUM3]] | +0.69 | +0.60 / +0.77 | both halves | 7e-06 |  |
| [[UTP20]] | +0.69 | +0.54 / +0.76 | both halves | 1e-05 |  |
| [[FKTN]] | +0.69 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[MRPL3]] | +0.68 | +0.63 / +0.73 | both halves | 7e-06 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NARF]] | -0.68 | -0.59 / -0.65 | both halves | 7e-06 |  |
| [[AAMDC]] | -0.65 | -0.55 / -0.70 | both halves | 1e-05 |  |
| [[ZFYVE1]] | -0.63 | -0.61 / -0.65 | both halves | 7e-06 |  |
| [[TSC22D4]] | -0.63 | -0.61 / -0.64 | both halves | 7e-06 |  |
| [[MXD1]] | -0.63 | -0.48 / -0.59 | both halves | 2e-05 |  |
| [[TCP11L2]] | -0.62 | -0.62 / -0.57 | both halves | 1e-05 |  |
| [[NDUFA2]] | -0.62 | -0.44 / -0.60 | both halves | 3e-05 |  |
| [[TMEM50A]] | -0.61 | -0.47 / -0.60 | both halves | 2e-05 |  |
| [[CXCR4]] | -0.61 | -0.59 / -0.57 | both halves | 9e-06 |  |
| [[ZNHIT1]] | -0.60 | -0.53 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TERT]] | B | TERT activity raises TCERG1's level | lines that do not express TERT (13) vs lines expressing it (37) | 1.20× lower at baseline in the lines without TERT | 0.042 | ⚠ within organs, on part of the lines; also absent: SAMD11, MIR1915HG, LNC-LBCS |
| [[PIK3CA]] | B | PIK3CA activity raises TCERG1's level | compounds that target PIK3CA: 3 of 4 lower it (Alpelisib, Bimiralisib, GSK1059615) | 75% of the class's compounds vs 2.8% of all compounds | 0.053 | ⚠ off-target possible; 3 compounds |
| [[TOP2A]] | B | TOP2A activity raises TCERG1's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[PLAG1]] | B | PLAG1 activity lowers TCERG1's level | lines that do not express PLAG1 (9) vs lines expressing it (41) | 1.22× higher at baseline in the lines without PLAG1 | 0.091 | ⚠ within organs, on part of the lines; also absent: FCGRT; maybe low, not absent |
| [[HSF2BP]] | C | HSF2BP activity raises TCERG1's level | lines that do not express HSF2BP (4) vs lines expressing it (46) | 1.39× lower at baseline in the lines without HSF2BP | 0.067 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; co-occurs with CTNNB1; also absent: TPST1, CPLANE1, SOAT1; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.800). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-18.4, -36.8); signed map (1.5, -42.4). **Vector** length 101, 41.4% of its response variance represented; |z| ≥ 3 in 1,965 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *rRNA processing in the nucleus and cytosol* (reactome, mean cos +0.52 to 24); *Major pathway of rRNA processing in the nucleolus and cytosol* (reactome, mean cos +0.52 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +10.9 | +9.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +10.1 | -1.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +9.3 | +0.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +7.1 | +10.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.8 | +16.0 |
|  | [[EX229 (drug)]] 5 µM |  | +5.7 | +5.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +5.5 | +7.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | +5.2 | +4.2 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +4.4 | -0.8 |
|  | [[venetoclax (drug)]] 5 µM |  | +4.1 | +5.3 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -4.6 | +16.7 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.4 | +13.2 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | -1.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.2 | -24.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.9 | +11.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.7 | -4.3 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -2.5 | +0.5 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.5 | +1.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.4 | -0.5 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -2.4 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | transcription elongation regulator 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q32 — chr5:146,447,311-146,511,961 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CA150, Urn1; previously TAF2S |
| Reactome | 6 pathways, smallest: mRNA Polyadenylation; mRNA 3'-end processing; mRNA Splicing - Major Pathway |
| Matched by | ensembl_id |

**Function**, from UniProt [O14776](https://www.uniprot.org/uniprotkb/O14776) (Transcription elongation regulator 1):

> Transcription factor that binds RNA polymerase II and inhibits the elongation of transcripts from target promoters. Regulates transcription elongation in a TATA box-dependent manner. Necessary for TAT-dependent activation of the human immunodeficiency virus type 1 (HIV-1) promoter.

**Summary**, from NCBI Gene [10915](https://www.ncbi.nlm.nih.gov/gene/10915):

> This gene encodes a nuclear protein that regulates transcriptional elongation and pre-mRNA splicing. The encoded protein interacts with the hyperphosphorylated C-terminal domain of RNA polymerase II via multiple FF domains, and with the pre-mRNA splicing factor SF1 via a WW domain. Alternative splicing results in multiple transcripts variants encoding different isoforms. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:15630](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15630) · Entrez [10915](https://www.ncbi.nlm.nih.gov/gene/10915) · UniProt [O14776](https://www.uniprot.org/uniprotkb/O14776) · Ensembl [ENSG00000113649](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000113649)

## Data

Gene col 3489: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3489); `tables/drug_effects.parquet` (80 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3489, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3489]; `tensor/DDL_lfc|DDL_z.npy` [3489]; `embed/gene_vectors.npy` [3489]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3489 or target_col == 3489). Every well: [[TCERG1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TCERG1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
