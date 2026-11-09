---
symbol: "PPP1R12B"
type: "gene"
col: 1177
ensembl_id: "ENSG00000077157"
name: "protein phosphatase 1 regulatory subunit 12B"
location: "1q32.1"
module: 54
arm: "+"
pooled_cpm: 170.03
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 23
n_dd_up_clean: 8
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/054"]
generated_by: "tahoemap"
---

# PPP1R12B

*protein phosphatase 1 regulatory subunit 12B* — 1q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 1.50× (z +9.6, q 6e-19, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.483× (z -16.6, q 0e+00, down in 39 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.588× (z -12.6, q 2e-34, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CRYZL1]] (+0.70, fdr 7e-06), [[PLEKHH3]] (+0.67, fdr 1e-05), [[CBFA2T2]] (+0.66, fdr 1e-05); moves opposite to [[KRT8P12]] (-0.69, fdr 7e-06), [[SERPINB8]] (-0.67, fdr 7e-06), [[CYREN]] (-0.65, fdr 6e-05).
> It sits in the **+** arm of [[Module 054]] (Mitochondrial ribosome-associated quality control).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[ITGB1-DT]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1177.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **1.50×** | +9.6 | 6e-19 | 45/48 (NCI-H460, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.46×** | +9.0 | 9e-17 | 42/48 (NCI-H23, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.37×** | +7.5 | 1e-11 | 30/48 (SHP-77, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.34×** | +6.9 | 9e-10 | 35/48 (NCI-H23, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.60×** | +5.7 | 2e-06 | 28/49 (C32, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.28×** | +5.5 | 3e-06 | 32/48 (PANC-1, COLO 205, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **1.52×** | +5.0 | 5e-05 | 39/49 (RKO, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.22×** | +4.7 | 2e-04 | 27/48 (C32, NCI-H2347, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.47×** | +4.6 | 3e-04 | 30/49 (A498, CHP-212, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +4.1 | 0.002 | 22/48 (SHP-77, J82, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +4.0 | 0.003 | 20/48 (SK-MEL-2, RKO, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | 1.18× | +3.9 | 0.005 | 18/50 (C32, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | 1.18× | +3.8 | 0.005 | 22/47 (C32, NCI-H2347, …) | rises with dose |  |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | 1.17× | +3.5 | 0.021 | 14/48 (A-427, NCI-H460, …) | rises with dose |  |
| [[Verteporfin (drug)]] 5 µM |  | 1.16× | +3.4 | 0.024 | 11/49 (SHP-77, A-427, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.12× | +3.2 | 0.057 | 8/48 (C32, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | 1.13× | +3.1 | 0.066 | 12/49 (C32, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 1.10× | +3.1 | 0.066 | 5/48 (C32, Hs 766T, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 14 with an alert ⚠; shown: the 15 strongest and the 11 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1177.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.483×** | -16.6 | 0e+00 | 39/44 (A498, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.505×** | -16.2 | 0e+00 | 44/49 (Hs 766T, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.622×** | -16.0 | 0e+00 | 33/48 (NCI-H1792, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.518×** | -14.4 | 4e-45 | 39/45 (A-427, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.563×** | -13.1 | 2e-37 | 44/47 (Hs 766T, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.588×** | -12.6 | 2e-34 | 45/48 (A-172, C32, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.632×** | -10.5 | 1e-23 | 36/48 (HOP62, COLO 205, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.649×** | -10.3 | 6e-23 | 33/48 (HOP62, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~29% of this change | **0.684×** | -9.0 | 1e-17 | 38/48 (SW 900, Panc 03.27, …) | inconsistent across doses | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.780×** | -8.4 | 4e-15 | 28/49 (Hs 766T, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.520×** | -7.9 | 2e-13 | 29/38 (LOX-IMVI, SNU-423, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.752×** | -6.8 | 5e-10 | 33/48 (KATO III, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.762×** | -6.5 | 4e-09 | 30/48 (NCI-H1792, CFPAC-1, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.785×** | -5.7 | 4e-07 | 29/48 (A498, A-172, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | **0.810×** | -4.8 | 6e-05 | 25/47 (CFPAC-1, A549, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.826×** | -4.6 | 2e-04 | 24/47 (MIA PaCa-2, HOP62, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.831×** | -4.2 | 8e-04 | 24/47 (MIA PaCa-2, HOP62, …) | all doses, stronger at high dose |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.726×** | -3.9 | 0.003 | 23/47 (NCI-H23, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Infigratinib (drug)]] 0.05 µM |  | 0.844× | -3.8 | 0.004 | 14/48 (HT-29, MIA PaCa-2, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.730×** | -3.8 | 0.004 | 23/48 (HEC-1-A, H4, …) | inconsistent across doses | noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **0.794×** | -3.5 | 0.012 | 20/48 (MIA PaCa-2, Hs 766T, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.757×** | -3.4 | 0.019 | 21/48 (MIA PaCa-2, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.907× | -3.3 | 0.024 | 9/48 (A-172, Hs 766T, …) | top dose only |  |
| [[vincristine (drug)]] 5 µM |  | **0.774×** | -3.1 | 0.046 | 20/46 (NCI-H2030, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Pralsetinib (drug)]] 5 µM |  | **0.775×** | -3.1 | 0.046 | 17/49 (MIA PaCa-2, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.05 µM |  | 0.874× | -3.0 | 0.060 | 12/48 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1177. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 461 | 15 (1 ⚠) | 6 (4 ⚠) | [[Binimetinib (drug)]] 0.5 µM 2.10× (z +12.6) | [[Dinaciclib (drug)]] 0.5 µM 0.329× (z -16.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.334× (z -16.0) |
| [[A-172 (line)]] | wt | 158 | 0 | 10 (7 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.228× (z -21.5) |
| [[Hs 766T (line)]] | wt | 321 | 0 | 10 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.235× (z -20.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.397× (z -12.9) |
| [[PANC-1 (line)]] | alt | 187 | 2 (1 ⚠) | 7 (7 ⚠) | [[Bortezomib (drug)]] 0.05 µM 1.79× (z +9.2) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Belinostat (drug)]] 5 µM 1.71× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.390× (z -15.8) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 169 | 0 | 8 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.396× (z -19.5) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.516× (z -9.8) |
| [[HOP62 (line)]] | alt | 138 | 0 | 8 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -24.4) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.254× (z -19.6) |
| [[SNU-423 (line)]] | alt | 195 | 0 | 8 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.445× (z -15.5) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.329× (z -15.1) |
| [[NCI-H460 (line)]] | wt | 223 | 2 | 5 (4 ⚠) | [[Belinostat (drug)]] 5 µM 1.80× (z +10.4) | [[Dinaciclib (drug)]] 0.5 µM 0.405× (z -16.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.560× (z -10.3) |
| [[Panc 03.27 (line)]] | alt | 158 | 0 | 7 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.337× (z -16.2) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 149 | 2 | 4 (3 ⚠) | [[Belinostat (drug)]] 5 µM 1.71× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.356× (z -24.9) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.533× (z -10.7) |
| [[LOX-IMVI (line)]] | wt | 147 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.476× (z -13.3) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.535× (z -11.2) |
| [[A498 (line)]] | wt | 202 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.330× (z -17.4) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 136 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -22.4) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.332× (z -11.4) |
| [[KATO III (line)]] | alt | 165 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.261× (z -17.1) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 130 | 1 | 4 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 1.99× (z +8.5) | [[Auranofin (drug)]] 5 µM 0.349× (z -13.0) |
| [[NCI-H1792 (line)]] | alt | 217 | 1 | 4 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.85× (z +9.0) | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -27.4) ⚠ cell-cycle shift, explains ~35% of this change |
| [[RPMI-7951 (line)]] | alt | 179 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.432× (z -15.6) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.416× (z -11.6) |
| [[SW 900 (line)]] | alt | 216 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.459× (z -15.1) ⚠ cell-cycle shift, explains ~35% of this change |
| [[SW480 (line)]] | alt | 163 | 1 | 4 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 3.07× (z +9.8) | [[Dinaciclib (drug)]] 0.5 µM 0.434× (z -14.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.581× (z -9.4) |
| [[A549 (line)]] | wt | 150 | 0 | 4 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.429× (z -12.9) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.614× (z -10.9) |
| [[COLO 205 (line)]] | alt | 233 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.385× (z -17.1) ⚠ cell-cycle shift, explains ~35% of this change |
| [[HEC-1-A (line)]] | alt | 150 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.318× (z -16.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.502× (z -10.6) |
| [[HepG2_C3A (line)]] | wt | 137 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.297× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.540× (z -9.7) |
| [[LS 180 (line)]] | wt | 175 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.289× (z -16.1) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 159 | 2 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 1.82× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.325× (z -16.3) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 193 | 3 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.19× (z +12.2) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.551× (z -8.9) ⚠ toxic |
| [[AN3 CA (line)]] | alt | 164 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.170× (z -12.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.320× (z -8.9) |
| [[NCI-H23 (line)]] | alt | 112 | 2 | 1 (1 ⚠) | [[Belinostat (drug)]] 5 µM 2.19× (z +9.9) | [[Dinaciclib (drug)]] 0.05 µM 0.286× (z -14.7) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 128 | 0 | 3 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.353× (z -10.3) |
| [[A-427 (line)]] | wt | 145 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0549× (z -33.1) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 155 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.424× (z -14.1) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.474× (z -12.3) |
| [[C-33 A (line)]] | alt | 124 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.298× (z -10.6) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 234 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.126× (z -17.1) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 155 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.57× (z +9.0) | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -14.4) ⚠ cell-cycle shift, explains ~35% of this change |
| [[HS-578T (line)]] | alt | 126 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.561× (z -10.5) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.457× (z -10.1) |
| [[HT-29 (line)]] | alt | 179 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.320× (z -14.1) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 134 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.410× (z -11.6) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 162 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.401× (z -12.6) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 130 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.50× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.356× (z -9.8) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 136 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.519× (z -9.7) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 124 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.06× (z +9.5) | — |
| [[RKO (line)]] | wt | 118 | 1 | 0 | [[Belinostat (drug)]] 5 µM 2.27× (z +9.8) | — |
| [[SK-MEL-2 (line)]] | alt | 108 | 1 | 0 | [[Belinostat (drug)]] 5 µM 2.39× (z +9.6) | — |
| [[SW 1271 (line)]] | alt | 125 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.128× (z -10.8) |
| [[BT-474 (line)]] | alt | 98.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 184 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 188 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 180 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 166 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 156 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1177), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CRYZL1]] | +0.70 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[PLEKHH3]] | +0.67 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[CBFA2T2]] | +0.66 | +0.64 / +0.50 | both halves | 1e-05 |  |
| [[ARL3]] | +0.66 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[TTLL5]] | +0.66 | +0.67 / +0.47 | both halves | 2e-05 |  |
| [[ATP5MJ]] | +0.66 | +0.63 / +0.44 | both halves | 3e-05 |  |
| [[RELCH]] | +0.66 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[HEBP1]] | +0.66 | +0.68 / +0.43 | both halves | 3e-05 |  |
| [[MZT2B]] | +0.65 | +0.69 / +0.43 | both halves | 3e-05 | pathway: G2/M Transition |
| [[ANAPC11]] | +0.65 | +0.55 / +0.40 | both halves | 5e-05 |  |
| [[MGST3]] | +0.65 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[COX6A1]] | +0.65 | +0.58 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KRT8P12]] | -0.69 | -0.65 / -0.58 | both halves | 7e-06 |  |
| [[SERPINB8]] | -0.67 | -0.62 / -0.60 | both halves | 7e-06 |  |
| [[CYREN]] | -0.65 | -0.70 / -0.38 | both halves | 6e-05 |  |
| [[ZC3H4]] | -0.65 | -0.56 / -0.57 | both halves | 1e-05 |  |
| [[LPXN]] | -0.64 | -0.64 / -0.43 | both halves | 3e-05 |  |
| [[FKRP]] | -0.64 | -0.66 / -0.40 | both halves | 4e-05 |  |
| [[ZNF655]] | -0.64 | -0.64 / -0.47 | both halves | 2e-05 |  |
| [[LINC01204]] | -0.64 | -0.64 / -0.53 | both halves | 1e-05 |  |
| [[ADAT1]] | -0.63 | -0.66 / -0.44 | both halves | 3e-05 |  |
| [[TRIM59]] | -0.62 | -0.65 / -0.43 | both halves | 3e-05 |  |
| [[ZNF121]] | -0.62 | -0.56 / -0.58 | both halves | 1e-05 |  |
| [[NEPRO-AS1]] | -0.61 | -0.66 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ITGB1-DT]] | B | ITGB1-DT activity lowers PPP1R12B's level | lines that do not express ITGB1-DT (21) vs lines expressing it (29) | 1.20× higher at baseline in the lines without ITGB1-DT | 0.007 | ⚠ within organs, on part of the lines; also absent: ENSG00000282849, LTBP2, ADTRP; maybe low, not absent |
| [[CCND1]] | B | CCND1 activity lowers PPP1R12B's level | lines that do not express CCND1 (7) vs lines expressing it (43) | 1.18× higher at baseline in the lines without CCND1 | 0.013 | ⚠ within organs, on part of the lines; also absent: FSTL3, ADAMTSL5; maybe low, not absent |
| [[ELF4]] | C | ELF4 activity strengthens PPP1R12B's drug response | lines that do not express ELF4 (3) vs lines expressing it (46) | the lines without ELF4 respond 0.48× as strongly (z diff +2.53); strongest at Homoharringtonine 5 µM: 1.39x vs 0.59x (z diff +10.8) | 0.059 | ⚠ few lines (3 vs 47); across organs; also absent: FUCA2, AIFM2, SP100; maybe low, not absent; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 054]] — Mitochondrial ribosome-associated quality control; 88 genes; this gene is in the **+** arm (projection on the module's main direction 0.576). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (1.6, -13.4); signed map (-33.3, 12.6). **Vector** length 124, 43.2% of its response variance represented; |z| ≥ 3 in 1,473 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +6.7 | +9.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +6.4 | +7.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.8 | +9.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +5.7 | +2.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.6 | +6.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.2 | +1.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.2 | +4.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +4.1 | +1.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.9 | +5.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +3.7 | +2.9 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -13.1 | -16.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -9.8 | -10.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -9.4 | -12.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -7.3 | -13.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -6.3 | -10.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.0 | -3.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.0 | -2.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.7 | +0.9 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -2.9 | -4.6 |

## What is on record

|  |  |
|---|---|
| Name | protein phosphatase 1 regulatory subunit 12B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q32.1 — chr1:202,348,699-202,592,706 (+) |
| Ensembl biotype | protein_coding |
| Also known as | M20, MGC87886, MGC131980, PP1bp55; previously MYPT2 |
| Gene groups (HGNC) | Ankyrin repeat domain containing; Protein phosphatase 1 regulatory subunits; Myosin phosphatase targeting family |
| Reactome | 12 pathways, smallest: RHO GTPases Activate ROCKs; RHO GTPases activate CIT; RHO GTPases activate PAKs |
| Matched by | ensembl_id |

**Function**, from UniProt [O60237](https://www.uniprot.org/uniprotkb/O60237) (Protein phosphatase 1 regulatory subunit 12B):

> Regulates myosin phosphatase activity. Augments Ca(2+) sensitivity of the contractile apparatus.

**Summary**, from NCBI Gene [4660](https://www.ncbi.nlm.nih.gov/gene/4660):

> Myosin phosphatase is a protein complex comprised of three subunits: a catalytic subunit (PP1c-delta, protein phosphatase 1, catalytic subunit delta), a large regulatory subunit (MYPT, myosin phosphatase target) and small regulatory subunit (sm-M20). Two isoforms of MYPT have been isolated--MYPT1 and MYPT2, the first of which is widely expressed, and the second of which may be specific to heart, skeletal muscle, and brain. Each of the MYPT isoforms functions to bind PP1c-delta and increase …

**Accessions** — [HGNC:7619](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7619) · Entrez [4660](https://www.ncbi.nlm.nih.gov/gene/4660) · UniProt [O60237](https://www.uniprot.org/uniprotkb/O60237) · Ensembl [ENSG00000077157](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000077157)

## Data

Gene col 1177: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1177); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1177, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1177]; `tensor/DDL_lfc|DDL_z.npy` [1177]; `embed/gene_vectors.npy` [1177]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1177 or target_col == 1177). Every well: [[PPP1R12B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPP1R12B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
