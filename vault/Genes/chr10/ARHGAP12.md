---
symbol: "ARHGAP12"
type: "gene"
col: 9107
ensembl_id: "ENSG00000165322"
name: "Rho GTPase activating protein 12"
location: "10p11.22"
module: 45
arm: "+"
pooled_cpm: 222.27
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 20
n_dd_up_clean: 9
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/045"]
generated_by: "tahoemap"
---

# ARHGAP12

*Rho GTPase activating protein 12* — 10p11.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.56× (z +9.8, q 9e-20, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.470× (z -16.5, q 0e+00, down in 45 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 0.806× (z -6.5, q 7e-09, down in 27 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ORC4]] (+0.74, fdr 7e-06), [[PIP4P2]] (+0.67, fdr 7e-06), [[KBTBD3]] (+0.63, fdr 1e-05); moves opposite to [[MICALL1]] (-0.67, fdr 7e-06), [[IKBKG]] (-0.60, fdr 2e-05), [[DESI1]] (-0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 045]] (Iron uptake and transport).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[GRB7]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 6 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9107.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.56×** | +9.8 | 9e-20 | 39/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.05×** | +8.2 | 6e-14 | 39/49 (SW480, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.44×** | +7.9 | 5e-13 | 37/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.25×** | +6.8 | 2e-09 | 31/48 (KATO III, SW48, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.75×** | +6.4 | 2e-08 | 34/48 (SW480, SNU-423, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.20×** | +5.5 | 3e-06 | 24/48 (MIA PaCa-2, J82, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.27×** | +5.1 | 2e-05 | 29/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **1.22×** | +4.4 | 8e-04 | 26/49 (SW48, KATO III, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 1.15× | +4.3 | 0.001 | 15/48 (RKO, AsPC-1, …) | rises with dose |  |
| [[palbociclib (drug)]] 0.5 µM |  | **1.30×** | +4.0 | 0.003 | 29/48 (HEC-1-A, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~6% here); noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.8 | 0.007 | 22/48 (A498, SW480, …) | all doses, flat |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 1.19× | +3.8 | 0.008 | 18/48 (HEC-1-A, Panc 03.27, …) | two highest doses | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.7 | 0.011 | 22/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | 1.18× | +3.6 | 0.015 | 17/49 (NCI-H2030, SNU-423, …) | top dose only | plate-row cell shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | 1.17× | +3.4 | 0.029 | 20/48 (MIA PaCa-2, RKO, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 5 µM |  | **1.33×** | +3.3 | 0.040 | 18/48 (HepG2/C3A, NCI-H2030, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Fumaric acid (drug)]] 5 µM |  | 1.16× | +3.2 | 0.046 | 7/49 (BT-474, NCI-H2030, …) | top dose only | plate-row cell shift |
| [[Brivudine (drug)]] 5 µM |  | **1.31×** | +3.1 | 0.059 | 18/49 (J82, SW48, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tomivosertib (drug)]] 5 µM |  | **1.30×** | +3.0 | 0.071 | 17/48 (BT-474, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | 1.15× | +3.0 | 0.071 | 11/49 (C-33 A, SNU-423, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.14× | +2.9 | 0.094 | 16/48 (HepG2/C3A, NCI-H2030, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 15 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9107.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.470×** | -16.5 | 0e+00 | 45/49 (CFPAC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.463×** | -16.2 | 0e+00 | 41/44 (SNU-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.592×** | -11.0 | 6e-26 | 42/47 (HT-29, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.719×** | -7.2 | 8e-11 | 38/48 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.806×** | -6.5 | 7e-09 | 27/48 (A-172, CFPAC-1, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.746×** | -6.4 | 1e-08 | 33/48 (NCI-H1792, KATO III, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.729×** | -6.4 | 2e-08 | 30/45 (KATO III, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.766×** | -5.8 | 4e-07 | 33/48 (H4, KATO III, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.768×** | -5.8 | 5e-07 | 33/48 (SW480, NCI-H460, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.828×** | -5.7 | 6e-07 | 26/49 (A549, SW480, …) | rises with dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.621×** | -5.4 | 3e-06 | 35/48 (NCI-H1792, KATO III, …) | top dose only | noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.792×** | -5.1 | 2e-05 | 33/48 (NCI-H1573, MIA PaCa-2, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.825×** | -4.2 | 0.001 | 24/48 (SW480, HCT15, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | 0.840× | -3.8 | 0.006 | 20/48 (SW480, KATO III, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.717×** | -3.8 | 0.006 | 24/48 (NCI-H2347, KATO III, …) | rises with dose | noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **0.789×** | -3.7 | 0.007 | 26/48 (A-427, Hs 766T, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.750×** | -3.3 | 0.030 | 20/48 (KATO III, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.05 µM |  | 0.853× | -3.2 | 0.037 | 18/48 (MIA PaCa-2, NCI-H460, …) | all doses, flat |  |
| [[Peretinoin (drug)]] 5 µM |  | 0.860× | -3.2 | 0.042 | 18/47 (MIA PaCa-2, NCI-H460, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.868× | -3.1 | 0.052 | 16/48 (HepG2/C3A, SW 1088, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.870× | -3.0 | 0.056 | 15/48 (A-172, NCI-H23, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 5 µM |  | **0.767×** | -3.0 | 0.056 | 18/46 (MIA PaCa-2, A-427, …) | two highest doses | noisy plate (z scaled) |
| [[Thymol (drug)]] 5 µM |  | 0.906× | -3.0 | 0.062 | 7/48 (NCI-H23, HS-578T, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.774×** | -2.9 | 0.067 | 17/48 (KATO III, HepG2/C3A, …) | top dose only | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 0.889× | -2.9 | 0.073 | 14/48 (NCI-H1573, NCI-H460, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9107. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 314 | 4 (1 ⚠) | 7 (6 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.14× (z +12.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.517× (z -14.6) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.548× (z -9.6) |
| [[KATO III (line)]] | alt | 337 | 3 (2 ⚠) | 7 (7 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.07× (z +11.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.560× (z -12.8) ⚠ cell-cycle shift, explains ~25% of this change |
| [[NCI-H460 (line)]] | wt | 206 | 5 (3 ⚠) | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.75× (z +14.0) | [[Dinaciclib (drug)]] 0.5 µM 0.381× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.520× (z -9.1) |
| [[PANC-1 (line)]] | alt | 172 | 5 (2 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.70× (z +15.9) | [[Dinaciclib (drug)]] 0.5 µM 0.493× (z -11.4) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 181 | 2 (1 ⚠) | 5 (4 ⚠) | [[Digitoxin (drug)]] 5 µM 2.22× (z +10.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.19× (z +10.3) | [[Dinaciclib (drug)]] 5 µM 0.181× (z -21.8) ⚠ toxic; transcription drop · without an alert: [[5-Azacytidine (drug)]] 5 µM 0.513× (z -8.9) |
| [[J82 (line)]] | alt | 120 | 6 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.64× (z +18.5) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.22× (z +12.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 246 | 4 (4 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.60× (z +21.0) ⚠ cell-cycle shift, explains ~37% of this change | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.440× (z -9.8) ⚠ cell-cycle shift, explains ~23% of this change |
| [[CFPAC-1 (line)]] | alt | 316 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.282× (z -17.2) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 331 | 2 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 3.34× (z +10.0) | [[Dinaciclib (drug)]] 5 µM 0.372× (z -15.2) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 125 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.23× (z +18.5) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.61× (z +11.0) | — |
| [[RPMI-7951 (line)]] | alt | 309 | 1 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +12.2) ⚠ cell-cycle shift, explains ~37% of this change | [[Dinaciclib (drug)]] 5 µM 0.279× (z -14.9) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 206 | 1 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.71× (z +9.0) ⚠ cell-cycle shift, explains ~37% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.369× (z -11.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 208 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.308× (z -13.2) ⚠ toxic; transcription drop · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.593× (z -8.5) |
| [[A498 (line)]] | wt | 182 | 1 (1 ⚠) | 2 (2 ⚠) | [[Selinexor (drug)]] 5 µM 1.68× (z +9.3) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.403× (z -11.9) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 213 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.427× (z -10.3) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 248 | 0 | 3 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.409× (z -11.3) ⚠ toxic |
| [[HepG2_C3A (line)]] | wt | 305 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.09× (z +9.3) | [[Dinaciclib (drug)]] 0.5 µM 0.381× (z -12.3) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 380 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.326× (z -15.4) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 236 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.254× (z -16.5) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 289 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.285× (z -15.0) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 176 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.409× (z -13.2) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 243 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.449× (z -11.5) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 247 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +9.6) ⚠ cell-cycle shift, explains ~37% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.454× (z -9.0) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 241 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.445× (z -15.5) ⚠ cell-cycle shift, explains ~25% of this change |
| [[AsPC-1 (line)]] | alt | 307 | 1 (1 ⚠) | 1 (1 ⚠) | [[Selinexor (drug)]] 5 µM 1.73× (z +9.7) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.512× (z -8.6) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 141 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.31× (z +9.0) | — |
| [[Hs 766T (line)]] | wt | 213 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +16.5) ⚠ cell-cycle shift, explains ~37% of this change | [[Dinaciclib (drug)]] 5 µM 0.315× (z -12.6) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 180 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.393× (z -12.1) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 145 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +11.5) ⚠ cell-cycle shift, explains ~37% of this change | — |
| [[AN3 CA (line)]] | alt | 312 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.258× (z -10.3) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 272 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.450× (z -8.5) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 134 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.294× (z -12.5) ⚠ transcription drop |
| [[HEC-1-A (line)]] | alt | 201 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.318× (z -15.5) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 153 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.420× (z -10.0) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 145 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.419× (z -9.1) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 220 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.430× (z -12.7) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 122 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.341× (z -11.3) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 143 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +15.9) ⚠ cell-cycle shift, explains ~37% of this change | — |
| [[SNU-1 (line)]] | wt | 184 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0764× (z -24.4) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 181 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.420× (z -9.3) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 196 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.206× (z -17.6) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 133 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 112 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 153 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 250 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 247 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 244 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 166 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 227 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 418 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9107), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ORC4]] | +0.74 | +0.71 / +0.77 | both halves | 7e-06 |  |
| [[PIP4P2]] | +0.67 | +0.69 / +0.59 | both halves | 7e-06 |  |
| [[KBTBD3]] | +0.63 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[DBP]] | +0.63 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[TMEM14A]] | +0.61 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[CXADR]] | +0.61 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[SNX2]] | +0.61 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[SNX30]] | +0.59 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[PER1]] | +0.58 | +0.47 / +0.61 | both halves | 2e-05 |  |
| [[RYBP]] | +0.58 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[CAT]] | +0.58 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[THRA]] | +0.57 | +0.55 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*40 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MICALL1]] | -0.67 | -0.59 / -0.67 | both halves | 7e-06 |  |
| [[IKBKG]] | -0.60 | -0.47 / -0.58 | both halves | 2e-05 |  |
| [[DESI1]] | -0.59 | -0.56 / -0.56 | both halves | 1e-05 |  |
| [[VCP]] | -0.56 | -0.59 / -0.53 | both halves | 1e-05 |  |
| [[AGAP6]] | -0.56 | -0.57 / -0.49 | both halves | 1e-05 |  |
| [[ABCF2]] | -0.56 | -0.57 / -0.44 | both halves | 3e-05 |  |
| [[SFXN5]] | -0.55 | -0.58 / -0.48 | both halves | 2e-05 |  |
| [[PRR14L]] | -0.55 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[TIMM23B-AGAP6]] | -0.54 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[ZNF142]] | -0.54 | -0.52 / -0.43 | both halves | 3e-05 |  |
| [[C1orf159]] | -0.54 | -0.43 / -0.58 | both halves | 3e-05 |  |
| [[TMEM217]] | -0.54 | -0.55 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GRB7]] | B | GRB7 activity raises ARHGAP12's level | lines that do not express GRB7 (25) vs lines expressing it (25) | 1.43× lower at baseline in the lines without GRB7 | 0.063 | ⚠ within organs, on part of the lines; also absent: SH2D3A, CRB3, MISP |
| [[CXADR]] | B | CXADR activity raises ARHGAP12's level | lines that do not express CXADR (16) vs lines expressing it (34) | 1.34× lower at baseline in the lines without CXADR | 0.077 | ⚠ within organs, on part of the lines; also absent: LSR, ENTPD2, LMTK3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 045]] — Iron uptake and transport; 102 genes; this gene is in the **+** arm (projection on the module's main direction 0.690). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (17.7, -10.6); signed map (-27.8, -6.7). **Vector** length 123, 43.0% of its response variance represented; |z| ≥ 3 in 1,354 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +9.7 | +6.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | +7.4 | +4.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +5.9 | +2.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +5.7 | +2.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +5.7 | +4.3 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +4.1 | +2.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.8 | +3.1 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -9.9 | -6.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -8.2 | -4.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -7.8 | -5.1 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~17% of this change | -7.4 | -3.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | -6.9 | -7.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -6.1 | -2.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | -5.0 | -3.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.5 | -5.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -4.1 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | Rho GTPase activating protein 12 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p11.22 — chr10:31,805,398-31,928,876 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20737, FLJ10971, FLJ21785 |
| Gene groups (HGNC) | Pleckstrin homology domain containing; Rho GTPase activating proteins; SH3 domain containing |
| Reactome | 7 pathways, smallest: RHOV GTPase cycle; RHOF GTPase cycle; RHOD GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IWW6](https://www.uniprot.org/uniprotkb/Q8IWW6) (Rho GTPase-activating protein 12):

> GTPase activator for the Rho-type GTPases by converting them to an inactive GDP-bound state.

**Summary**, from NCBI Gene [94134](https://www.ncbi.nlm.nih.gov/gene/94134):

> This gene encodes a member of a large family of proteins that activate Rho-type guanosine triphosphate (GTP) metabolizing enzymes. The encoded protein may be involved in suppressing tumor formation by regulating cell invasion and adhesion. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene. [provided by RefSeq, Jul 2012]

**Accessions** — [HGNC:16348](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16348) · Entrez [94134](https://www.ncbi.nlm.nih.gov/gene/94134) · UniProt [Q8IWW6](https://www.uniprot.org/uniprotkb/Q8IWW6) · Ensembl [ENSG00000165322](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165322)

## Data

Gene col 9107: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9107); `tables/drug_effects.parquet` (53 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9107, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9107]; `tensor/DDL_lfc|DDL_z.npy` [9107]; `embed/gene_vectors.npy` [9107]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9107 or target_col == 9107). Every well: [[ARHGAP12 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARHGAP12.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
