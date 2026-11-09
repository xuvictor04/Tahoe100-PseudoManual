---
symbol: "ARHGAP18"
type: "gene"
col: 7087
ensembl_id: "ENSG00000146376"
name: "Rho GTPase activating protein 18"
location: "6q22.33"
module: 120
arm: "+"
pooled_cpm: 81.52
n_lines_expressing: 44
n_dd_up: 14
n_dd_down: 23
n_dd_up_clean: 6
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 5
direction_downstream: 10
tags: ["gene", "module/120"]
generated_by: "tahoemap"
---

# ARHGAP18

*Rho GTPase activating protein 18* — 6q22.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (8 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 2.08× (z +14.8, q 0e+00, up in 35 of 42 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.05 µM: 1.61× (z +9.7, q 4e-20, up in 34 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.600× (z -14.6, q 1e-45, down in 34 of 43 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DLC1]] (+0.63, fdr 1e-05), [[RBMS2]] (+0.61, fdr 1e-05), [[TGFBR2]] (+0.61, fdr 1e-05); moves opposite to [[NRSN2-AS1]] (-0.56, fdr 4e-05), [[SETD1B]] (-0.52, fdr 3e-04), [[PLEKHO1]] (-0.52, fdr 7e-05).
> It is in [[Module 120]], a single-armed module (RHOA GTPase cycle).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[ARHGDIB]] → it (grade B ⚠); 10 go from it, the strongest it → [[ZNF529-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7087.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **2.08×** | +14.8 | 0e+00 | 35/42 (A-172, A498, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **2.07×** | +14.8 | 0e+00 | 34/42 (A498, A-172, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **1.95×** | +13.6 | 1e-39 | 35/42 (A-172, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.91×** | +13.1 | 3e-37 | 31/42 (A498, A-172, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **1.72×** | +10.5 | 7e-24 | 29/35 (A-172, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.61×** | +9.7 | 4e-20 | 34/42 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.37×** | +9.0 | 2e-17 | 28/42 (A498, A-172, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | **1.46×** | +7.1 | 1e-10 | 20/38 (SNU-423, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.36×** | +6.2 | 3e-08 | 19/43 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.33×** | +5.8 | 4e-07 | 23/42 (HepG2/C3A, J82, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **1.64×** | +5.2 | 9e-06 | 21/43 (A498, PANC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~89% of this change | 1.18× | +4.8 | 9e-05 | 17/41 (A-172, HT-29, …) | rises with dose | composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +4.6 | 2e-04 | 17/42 (NCI-H2347, AsPC-1, …) | rises with dose | low cells (technical?) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.24×** | +4.4 | 4e-04 | 16/42 (A-172, SK-MEL-2, …) | rises with dose |  |
| [[Tofacitinib (drug)]] 5 µM |  | 1.12× | +3.3 | 0.034 | 8/43 (CFPAC-1, HepG2/C3A, …) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | 1.17× | +3.2 | 0.046 | 14/42 (A498, HS-578T, …) | all doses, flat |  |
| [[Ipatasertib (drug)]] 0.05 µM |  | 1.18× | +3.2 | 0.048 | 11/42 (LoVo, NCI-H1792, …) | inconsistent across doses |  |
| [[Ralimetinib dimesylate (drug)]] 5 µM |  | **1.35×** | +3.2 | 0.051 | 5/42 (J82, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | 1.16× | +3.1 | 0.064 | 11/42 (A498, NCI-H1573, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7087.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.600×** | -14.6 | 1e-45 | 34/43 (LOX-IMVI, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.662×** | -8.4 | 2e-14 | 30/42 (HepG2/C3A, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.675×** | -8.0 | 3e-13 | 28/42 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.693×** | -7.4 | 2e-11 | 26/42 (LOX-IMVI, HT-29, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.695×** | -7.4 | 2e-11 | 26/42 (HepG2/C3A, LoVo, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.699×** | -7.2 | 4e-11 | 26/42 (LS 180, PANC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.529×** | -6.7 | 1e-09 | 25/43 (KATO III, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.710×** | -6.7 | 2e-09 | 27/41 (NCI-H460, HCT15, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.533×** | -6.7 | 2e-09 | 25/42 (KATO III, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.726×** | -6.5 | 5e-09 | 24/42 (HEC-1-A, HT-29, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.733×** | -6.3 | 2e-08 | 24/41 (NCI-H460, A-172, …) | rises with dose | low cells (technical?) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.732×** | -6.0 | 1e-07 | 21/42 (HT-29, LoVo, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.741×** | -5.8 | 4e-07 | 20/44 (LOX-IMVI, J82, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.760×** | -5.6 | 1e-06 | 24/42 (PANC-1, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.762×** | -5.5 | 1e-06 | 22/43 (LOX-IMVI, J82, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.766×** | -5.4 | 2e-06 | 23/42 (LS 180, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[RMC-6236 (drug)]] 5 µM |  | **0.666×** | -4.3 | 5e-04 | 16/42 (LOX-IMVI, J82, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 0.853× | -3.8 | 0.004 | 16/42 (LOX-IMVI, J82, …) | all doses, stronger at high dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.32 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7087. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 65.9 | 14 (12 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +15.0) ⚠ cell-cycle shift, explains ~89% of this change · without an alert: [[Panobinostat (drug)]] 0.05 µM 3.18× (z +11.1) | — |
| [[LOX-IMVI (line)]] | wt | 299 | 0 | 14 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.200× (z -23.8) |
| [[A498 (line)]] | wt | 27.6 | 7 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.26× (z +13.7) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 2.28× (z +11.1) | — |
| [[HepG2_C3A (line)]] | wt | 241 | 0 | 7 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.307× (z -16.4) |
| [[PANC-1 (line)]] | alt | 25.1 | 3 (3 ⚠) | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.18× (z +10.9) ⚠ cell-cycle shift, explains ~31% of this change | [[Homoharringtonine (drug)]] 5 µM 0.340× (z -14.3) ⚠ cell-cycle shift, explains ~89% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.333× (z -10.3) |
| [[SNU-423 (line)]] | alt | 37.2 | 6 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.40× (z +12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[HS-578T (line)]] | alt | 21.0 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.92× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[HT-29 (line)]] | alt | 155 | 1 (1 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +13.7) ⚠ cell-cycle shift, explains ~89% of this change | [[Bortezomib (drug)]] 0.05 µM 0.341× (z -13.3) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.472× (z -9.8) |
| [[J82 (line)]] | alt | 82.8 | 0 | 5 (1 ⚠) | — | [[Trametinib (drug)]] 5 µM 0.219× (z -12.5) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.282× (z -9.4) |
| [[LoVo (line)]] | wt | 126 | 0 | 5 (2 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.348× (z -11.4) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.371× (z -11.4) |
| [[NCI-H1792 (line)]] | alt | 51.7 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.37× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[NCI-H460 (line)]] | wt | 33.7 | 3 (3 ⚠) | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.02× (z +10.6) ⚠ cell-cycle shift, explains ~31% of this change | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.339× (z -9.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Pitavastatin (Calcium) (drug)]] 5 µM 0.381× (z -8.9) |
| [[AsPC-1 (line)]] | alt | 77.7 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +11.5) ⚠ cell-cycle shift, explains ~89% of this change | — |
| [[CFPAC-1 (line)]] | alt | 193 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.524× (z -11.1) |
| [[KATO III (line)]] | alt | 139 | 0 | 4 (1 ⚠) | — | [[TAK-901 (drug)]] 5 µM 0.188× (z -11.1) |
| [[SW480 (line)]] | alt | 260 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.416× (z -16.2) |
| [[HEC-1-A (line)]] | alt | 144 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.529× (z -11.7) |
| [[LS 180 (line)]] | wt | 82.1 | 1 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +11.0) ⚠ cell-cycle shift, explains ~89% of this change | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.459× (z -9.3) |
| [[NCI-H2347 (line)]] | alt | 37.2 | 3 (3 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 2.27× (z +11.7) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[Hs 766T (line)]] | wt | 161 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +10.1) ⚠ cell-cycle shift, explains ~89% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.457× (z -10.4) |
| [[MIA PaCa-2 (line)]] | alt | 27.3 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.21× (z +10.8) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 51.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.94× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[SW1417 (line)]] | alt | 65.4 | 1 (1 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 2.41× (z +8.8) ⚠ cell-cycle shift, explains ~31% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.540× (z -8.8) |
| [[C32 (line)]] | wt | 58.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.342× (z -10.6) |
| [[CHP-212 (line)]] | wt | 58.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.247× (z -9.7) |
| [[HCT15 (line)]] | alt | 33.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.76× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | — |
| [[NCI-H2030 (line)]] | alt | 103 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.384× (z -13.0) |
| [[Panc 03.27 (line)]] | alt | 213 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.476× (z -13.0) |
| [[SW 1271 (line)]] | alt | 193 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.204× (z -11.9) |
| [[SW 900 (line)]] | alt | 35.4 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.39× (z +8.5) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[A-427 (line)]] | wt | 10.8 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 28.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.30 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 67.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 16.9 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 56.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 64.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 94.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.5 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 19.9 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.90 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 78.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 26.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7087), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*55 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DLC1]] | +0.63 | +0.54 / +0.59 | both halves | 1e-05 | same gene group; pathway: RHOA GTPase cycle |
| [[RBMS2]] | +0.61 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[TGFBR2]] | +0.61 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[COTL1]] | +0.57 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[ST3GAL5]] | +0.55 | +0.44 / +0.44 | both halves | 3e-05 |  |
| [[NDFIP2]] | +0.55 | +0.21 / +0.59 | both halves | 6e-04 |  |
| [[CCN2]] | +0.54 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[LIMA1]] | +0.52 | +0.42 / +0.47 | both halves | 4e-05 |  |
| [[TEAD1]] | +0.52 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[DNMBP]] | +0.51 | +0.37 / +0.48 | both halves | 8e-05 |  |
| [[HLTF]] | +0.51 | +0.30 / +0.46 | both halves | 2e-04 |  |
| [[PTPN14]] | +0.51 | +0.50 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*45 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NRSN2-AS1]] | -0.56 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[SETD1B]] | -0.52 | -0.26 / -0.51 | both halves | 3e-04 |  |
| [[PLEKHO1]] | -0.52 | -0.37 / -0.55 | both halves | 7e-05 |  |
| [[TMEM11-DT]] | -0.51 | -0.37 / -0.41 | both halves | 8e-05 |  |
| [[C17orf67]] | -0.50 | -0.34 / -0.42 | both halves | 1e-04 |  |
| [[OTUD7B]] | -0.49 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[MSL1]] | -0.48 | -0.30 / -0.46 | both halves | 2e-04 |  |
| [[LZTS2]] | -0.48 | -0.29 / -0.56 | both halves | 2e-04 |  |
| [[GATA2-AS1]] | -0.48 | -0.26 / -0.43 | both halves | 4e-04 |  |
| [[EIF4ENIF1]] | -0.48 | -0.41 / -0.44 | both halves | 4e-05 |  |
| [[PGLS-DT]] | -0.47 | -0.35 / -0.36 | both halves | 1e-04 |  |
| [[FAM219A]] | -0.47 | -0.45 / -0.53 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARHGDIB]] | B | ARHGDIB activity raises ARHGAP18's level | lines that do not express ARHGDIB (23) vs lines expressing it (27) | 2.58× lower at baseline in the lines without ARHGDIB | 0.011 | ⚠ within organs, on part of the lines; also absent: CD74, MILR1, CACNA2D4 |
| [[SORL1]] | B | SORL1 activity raises ARHGAP18's level | lines that do not express SORL1 (21) vs lines expressing it (29) | 2.11× lower at baseline in the lines without SORL1 | 0.044 | ⚠ within organs, on part of the lines; also absent: PRR15-DT, PLEKHG6, SLC52A3 |
| [[TGFBR2]] | B | TGFBR2 activity raises ARHGAP18's level | lines that do not express TGFBR2 (7) vs lines expressing it (43) | 3.94× lower at baseline in the lines without TGFBR2 | 0.073 | ⚠ within organs, on part of the lines; also absent: VDR, TRIB1, MET |
| [[ITGA6]] | B | ITGA6 activity raises ARHGAP18's level | lines that do not express ITGA6 (9) vs lines expressing it (41) | 2.13× lower at baseline in the lines without ITGA6 | 0.084 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[MAML2]] | B | MAML2 activity raises ARHGAP18's level | lines that do not express MAML2 (8) vs lines expressing it (42) | 3.44× lower at baseline in the lines without MAML2 | 0.093 | ⚠ within organs, on part of the lines; also absent: TNS3, SMOX, ALDH3B1 |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 10, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF529-AS1]] | B | ARHGAP18 activity lowers ZNF529-AS1's level | lines that do not express ARHGAP18 (6) vs lines expressing it (44) | 2.40× higher at baseline in the lines without ARHGAP18 | 0.012 | ⚠ within organs, on part of the lines; also absent: IER3, SLC2A1, SHB |
| [[SORL1]] | B | ARHGAP18 activity raises SORL1's level | lines that do not express ARHGAP18 (6) vs lines expressing it (44) | 3.28× lower at baseline in the lines without ARHGAP18 | 0.024 | ⚠ within organs, on part of the lines; also absent: IER3, SLC2A1, SHB |
| [[ARHGAP26]] | B | ARHGAP18 activity raises ARHGAP26's level | lines that do not express ARHGAP18 (6) vs lines expressing it (44) | 2.52× lower at baseline in the lines without ARHGAP18 | 0.039 | ⚠ within organs, on part of the lines; also absent: IER3, SLC2A1, SHB |
| [[CCN2]] | B | ARHGAP18 activity lowers CCN2's level | lines that do not express ARHGAP18 (6) vs lines expressing it (44) | 4.76× higher at baseline in the lines without ARHGAP18 | 0.042 | ⚠ within organs, on part of the lines; also absent: IER3, SLC2A1, SHB |
| [[ALDH7A1]] | B | ARHGAP18 activity lowers ALDH7A1's level | lines that do not express ARHGAP18 (6) vs lines expressing it (44) | 2.32× higher at baseline in the lines without ARHGAP18 | 0.058 | ⚠ within organs, on part of the lines; also absent: IER3, SLC2A1, SHB |
| cells under [[Lonafarnib (drug)]] 0.05 µM | B | ARHGAP18 activity lowers the cells' numbers under Lonafarnib 0.05 µM (makes them more sensitive) | lines that do not express ARHGAP18 (6) vs lines expressing it (42) | the lines without ARHGAP18: 1.26× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: IER3, SLC2A1, SHB |
| cells under [[Aliskiren (drug)]] 0.5 µM | B | ARHGAP18 activity raises the cells' numbers under Aliskiren 0.5 µM (protects the cells) | lines that do not express ARHGAP18 (6) vs lines expressing it (42) | the lines without ARHGAP18: 0.75× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: IER3, SLC2A1, SHB |
| [[ITGA6]] | B | ARHGAP18 activity raises ITGA6's level | lines that do not express ARHGAP18 (6) vs lines expressing it (44) | 2.03× lower at baseline in the lines without ARHGAP18 | 0.082 | ⚠ within organs, on part of the lines; also absent: IER3, SLC2A1, SHB |
| cells under [[Irinotecan (drug)]] 0.5 µM | B | ARHGAP18 activity raises the cells' numbers under Irinotecan 0.5 µM (protects the cells) | lines that do not express ARHGAP18 (6) vs lines expressing it (42) | the lines without ARHGAP18: 0.75× the cells of the other lines | 0.084 | ⚠ within organs, on part of the lines; also absent: IER3, SLC2A1, SHB |
| [[EXTL2]] | B | ARHGAP18 activity lowers EXTL2's level | lines that do not express ARHGAP18 (6) vs lines expressing it (44) | 1.88× higher at baseline in the lines without ARHGAP18 | 0.090 | ⚠ within organs, on part of the lines; also absent: IER3, SLC2A1, SHB |

## Where it sits

- **Module**: [[Module 120]] — RHOA GTPase cycle; 41 genes; every member is in the + arm (projection on the module's main direction 0.514). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (24.4, 11.6); signed map (15.1, 38.8). **Vector** length 125, 36.5% of its response variance represented; |z| ≥ 3 in 1,395 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.0 | +9.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | +4.6 | +13.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.4 | +9.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | +4.2 | +10.5 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | +3.8 | +3.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.5 | +5.2 |
|  | [[Tofacitinib (drug)]] 5 µM |  | +2.7 | +3.3 |
|  | [[Ralimetinib dimesylate (drug)]] 5 µM |  | +2.3 | +3.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.2 | +5.8 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -9.8 | -14.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -6.4 | -4.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | -5.8 | -6.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -5.6 | -8.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -5.6 | -7.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.4 | -6.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -4.3 | -6.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.3 | -3.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.1 | -7.4 |

## What is on record

|  |  |
|---|---|
| Name | Rho GTPase activating protein 18 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q22.33 — chr6:129,576,132-129,710,177 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MacGAP, bA307O14.2, SENEX |
| Gene groups (HGNC) | Rho GTPase activating proteins |
| Reactome | 5 pathways, smallest: RHOC GTPase cycle; RHOA GTPase cycle; RHO GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N392](https://www.uniprot.org/uniprotkb/Q8N392) (Rho GTPase-activating protein 18):

> Rho GTPase activating protein that suppresses F-actin polymerization by inhibiting Rho. Rho GTPase activating proteins act by converting Rho-type GTPases to an inactive GDP-bound state. Plays a key role in tissue tension and 3D tissue shape by regulating cortical actomyosin network formation. Acts downstream of YAP1 and inhibits actin polymerization, which in turn reduces nuclear localization of YAP1. Regulates cell shape, spreading, and migration.

**Summary**, from NCBI Gene [93663](https://www.ncbi.nlm.nih.gov/gene/93663):

> Enables GTPase activator activity. Involved in several processes, including regulation of actin filament polymerization; regulation of small GTPase mediated signal transduction; and small GTPase-mediated signal transduction. Located in cytosol. Part of cytoplasmic microtubule and ruffle. Implicated in schizophrenia. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:21035](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21035) · Entrez [93663](https://www.ncbi.nlm.nih.gov/gene/93663) · UniProt [Q8N392](https://www.uniprot.org/uniprotkb/Q8N392) · Ensembl [ENSG00000146376](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000146376)

## Data

Gene col 7087: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7087); `tables/drug_effects.parquet` (59 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7087, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7087]; `tensor/DDL_lfc|DDL_z.npy` [7087]; `embed/gene_vectors.npy` [7087]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7087 or target_col == 7087). Every well: [[ARHGAP18 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARHGAP18.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
