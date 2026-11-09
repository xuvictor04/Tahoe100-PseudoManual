---
symbol: "ALDH7A1"
type: "gene"
col: 9027
ensembl_id: "ENSG00000164904"
name: "aldehyde dehydrogenase 7 family member A1"
location: "5q23.2"
module: 57
arm: "+"
pooled_cpm: 54.67
n_lines_expressing: 48
n_dd_up: 21
n_dd_down: 26
n_dd_up_clean: 13
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/057"]
generated_by: "tahoemap"
---

# ALDH7A1

*aldehyde dehydrogenase 7 family member A1* — 5q23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.13× (z +17.4, q 0e+00, up in 39 of 45 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 1.40× (z +7.7, q 1e-12, up in 31 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.492× (z -16.3, q 0e+00, down in 42 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HLTF]] (+0.72, fdr 7e-06), [[MNS1]] (+0.70, fdr 1e-05), [[LRRCC1]] (+0.68, fdr 1e-05); moves opposite to [[SMIM12]] (-0.59, fdr 9e-05), [[C17orf67]] (-0.58, fdr 1e-04), [[ZNF778]] (-0.58, fdr 3e-05).
> It sits in the **+** arm of [[Module 057]] (Peroxisomal protein import).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[ABL1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 47 in all, 13 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9027.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **2.13×** | +17.4 | 0e+00 | 39/45 (NCI-H1573, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **2.03×** | +15.7 | 0e+00 | 35/39 (A-172, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **1.72×** | +11.1 | 2e-26 | 32/43 (CFPAC-1, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.46×** | +8.6 | 8e-16 | 29/46 (NCI-H1573, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.42×** | +8.1 | 7e-14 | 25/46 (NCI-H1573, A498, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.40×** | +7.7 | 1e-12 | 31/46 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose |  |
| [[Radotinib (drug)]] 5 µM |  | **1.26×** | +7.5 | 7e-12 | 26/46 (A-427, NCI-H2030, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.35×** | +7.0 | 2e-10 | 25/46 (NCI-H1573, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.31×** | +6.2 | 3e-08 | 26/46 (A498, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.64×** | +6.0 | 1e-07 | 24/46 (A498, NCI-H2030, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.29×** | +5.8 | 3e-07 | 23/46 (LoVo, KATO III, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.17× | +5.1 | 2e-05 | 15/46 (A498, A-427, …) | rises with dose |  |
| [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | 1.16× | +5.0 | 3e-05 | 16/46 (RKO, HT-29, …) | rises with dose |  |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | **1.23×** | +4.6 | 2e-04 | 20/46 (NCI-H2030, NCI-H1573, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +4.5 | 3e-04 | 16/46 (SK-MEL-2, NCI-H1573, …) | top dose only | low cells (technical?) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.21×** | +4.3 | 5e-04 | 14/46 (NCI-H1573, HOP62, …) | top dose only |  |
| [[Brivudine (drug)]] 0.5 µM |  | **1.30×** | +4.3 | 6e-04 | 12/46 (MIA PaCa-2, HS-578T, …) | rises with dose | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.05 µM |  | 1.19× | +4.0 | 0.002 | 14/46 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.18× | +3.8 | 0.004 | 15/46 (NCI-H1792, SW 900, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM |  | **1.37×** | +3.8 | 0.004 | 15/45 (NCI-H1792, A549, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Budesonide (drug)]] 0.05 µM |  | 1.17× | +3.7 | 0.005 | 14/46 (SW 900, NCI-H1792, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 5 µM |  | **1.35×** | +3.6 | 0.007 | 6/46 (A498, CFPAC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Regorafenib (drug)]] 5 µM |  | **1.35×** | +3.6 | 0.007 | 6/46 (NCI-H1792, SK-MEL-2, …) | top dose only | noisy plate (z scaled) |
| [[Budesonide (drug)]] 0.5 µM |  | 1.17× | +3.6 | 0.008 | 16/46 (SW 900, NCI-H1792, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9027.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.492×** | -16.3 | 0e+00 | 42/46 (A-427, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.529×** | -14.6 | 1e-45 | 40/46 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.641×** | -14.4 | 4e-45 | 33/46 (C-33 A, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.539×** | -14.2 | 1e-43 | 42/46 (SW480, HOP62, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.565×** | -13.1 | 3e-37 | 42/46 (LoVo, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.570×** | -12.9 | 5e-36 | 37/45 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.589×** | -12.2 | 4e-32 | 39/46 (PANC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.612×** | -11.3 | 1e-27 | 39/46 (SW480, LoVo, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.627×** | -10.7 | 5e-25 | 34/46 (NCI-H2030, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.582×** | -9.8 | 6e-21 | 37/46 (PANC-1, H4, …) | all doses, flat | cell-cycle shift (explains ~7% here); noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.781×** | -8.0 | 7e-14 | 25/46 (SK-MEL-2, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.733×** | -7.1 | 6e-11 | 26/46 (SW 900, NCI-H2030, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.758×** | -6.3 | 1e-08 | 25/46 (SNU-1, PANC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.760×** | -6.3 | 1e-08 | 24/46 (KATO III, LOX-IMVI, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.764×** | -6.2 | 3e-08 | 23/45 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.800×** | -5.1 | 1e-05 | 24/46 (C-33 A, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.810×** | -4.8 | 4e-05 | 17/46 (SW 1271, hTERT-HPNE, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.31 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9027. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 57.7 | 4 (4 ⚠) | 7 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.77× (z +12.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.436× (z -14.9) |
| [[NCI-H460 (line)]] | wt | 51.5 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.05 µM 0.307× (z -12.8) |
| [[PANC-1 (line)]] | alt | 36.2 | 1 (1 ⚠) | 8 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.57× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Ixazomib citrate (drug)]] 5 µM 0.336× (z -12.5) |
| [[SW 900 (line)]] | alt | 36.3 | 9 | 0 | [[Dexamethasone (drug)]] 0.05 µM 3.72× (z +9.8) | — |
| [[SW480 (line)]] | alt | 70.1 | 2 (2 ⚠) | 7 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.28× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Auranofin (drug)]] 5 µM 0.351× (z -15.2) |
| [[C-33 A (line)]] | alt | 407 | 0 | 8 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.347× (z -19.2) |
| [[A-427 (line)]] | wt | 74.3 | 1 (1 ⚠) | 5 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.05× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Homoharringtonine (drug)]] 5 µM 0.451× (z -13.6) |
| [[HEC-1-A (line)]] | alt | 112 | 3 (3 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.11× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.554× (z -12.9) |
| [[NCI-H1573 (line)]] | alt | 26.5 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 5.80× (z +13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.381× (z -10.4) |
| [[NCI-H1792 (line)]] | alt | 32.5 | 6 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.36× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Clobetasol propionate (drug)]] 0.05 µM 3.30× (z +9.2) | — |
| [[SNU-1 (line)]] | wt | 52.3 | 1 (1 ⚠) | 5 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.43× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Homoharringtonine (drug)]] 0.05 µM 0.195× (z -11.6) |
| [[MIA PaCa-2 (line)]] | alt | 134 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.84× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.431× (z -9.8) |
| [[NCI-H2030 (line)]] | alt | 76.5 | 0 | 4 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.275× (z -13.6) |
| [[NCI-H23 (line)]] | alt | 41.8 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -15.2) |
| [[SK-MEL-2 (line)]] | alt | 48.6 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -18.1) |
| [[A-172 (line)]] | wt | 44.4 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 5.15× (z +14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Digitoxin (drug)]] 5 µM 0.292× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.366× (z -9.2) |
| [[A498 (line)]] | wt | 51.4 | 1 (1 ⚠) | 2 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.10× (z +8.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Auranofin (drug)]] 5 µM 0.451× (z -9.7) |
| [[HOP62 (line)]] | alt | 73.3 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.08× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.477× (z -12.2) |
| [[A549 (line)]] | wt | 37.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.43× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[CFPAC-1 (line)]] | alt | 39.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.41× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[HS-578T (line)]] | alt | 56.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.72× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[LOX-IMVI (line)]] | wt | 34.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.466× (z -8.8) |
| [[AN3 CA (line)]] | alt | 123 | 0 | 1 | — | [[GSK1059615 (drug)]] 5 µM 0.0771× (z -8.5) |
| [[C32 (line)]] | wt | 47.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.72× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[COLO 205 (line)]] | alt | 24.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.347× (z -8.8) |
| [[H4 (line)]] | wt | 35.7 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.123× (z -9.7) |
| [[HepG2_C3A (line)]] | wt | 44.3 | 0 | 1 (1 ⚠) | — | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.0966× (z -9.1) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 71.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.286× (z -14.6) |
| [[hTERT-HPNE (line)]] | wt | 24.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.59× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[KATO III (line)]] | alt | 33.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.33× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[Panc 03.27 (line)]] | alt | 53.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.505× (z -10.1) |
| [[SW 1271 (line)]] | alt | 68.3 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.0690× (z -10.5) |
| [[AsPC-1 (line)]] | alt | 9.46 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 63.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.02 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 20.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 60.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 49.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 59.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 45.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 47.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 41.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 60.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9027), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HLTF]] | +0.72 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[MNS1]] | +0.70 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[LRRCC1]] | +0.68 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[TMEM245]] | +0.67 | +0.44 / +0.69 | both halves | 3e-05 |  |
| [[TM7SF3]] | +0.67 | +0.57 / +0.71 | both halves | 9e-06 |  |
| [[HAUS4]] | +0.64 | +0.61 / +0.47 | both halves | 2e-05 |  |
| [[SHMT1]] | +0.64 | +0.57 / +0.60 | both halves | 9e-06 | pathway: Metabolism of amino acids and derivatives; STRING 537 |
| [[ALAD]] | +0.63 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[ADAM22]] | +0.63 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[GUSB]] | +0.63 | +0.40 / +0.67 | both halves | 4e-05 | pathway: HALLMARK_GLYCOLYSIS |
| [[EHMT2]] | +0.62 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[CYB5A]] | +0.62 | +0.58 / +0.54 | both halves | 1e-05 | pathway: HALLMARK_GLYCOLYSIS |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMIM12]] | -0.59 | -0.37 / -0.57 | both halves | 9e-05 |  |
| [[C17orf67]] | -0.58 | -0.36 / -0.58 | both halves | 1e-04 |  |
| [[ZNF778]] | -0.58 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[ALS2]] | -0.57 | -0.56 / -0.22 | both halves | 6e-04 |  |
| [[SWT1]] | -0.56 | -0.43 / -0.54 | both halves | 3e-05 |  |
| [[FTX]] | -0.56 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[CDR2]] | -0.56 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[YIPF7]] | -0.56 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[LUCAT1]] | -0.56 | -0.47 / -0.62 | both halves | 2e-05 |  |
| [[MAFG]] | -0.56 | -0.48 / -0.46 | both halves | 3e-05 |  |
| [[CLCF1]] | -0.56 | -0.48 / -0.55 | both halves | 2e-05 |  |
| [[MIR22HG]] | -0.55 | -0.45 / -0.64 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 5, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ABL1]] | B | ABL1 activity lowers ALDH7A1's level | compounds that target ABL1: 4 of 6 raise it (Flumatinib, NG25, Ponatinib, Radotinib) | 67% of the class's compounds vs 4.2% of all compounds | 0.037 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[FHL1]] | B | FHL1 activity raises ALDH7A1's level | lines that do not express FHL1 (19) vs lines expressing it (31) | 1.50× lower at baseline in the lines without FHL1 | 0.054 | ⚠ within organs, on part of the lines; also absent: ADAMTS7, ANTXR1, MSRB3 |
| [[ARHGAP18]] | B | ARHGAP18 activity lowers ALDH7A1's level | lines that do not express ARHGAP18 (6) vs lines expressing it (44) | 2.32× higher at baseline in the lines without ARHGAP18 | 0.058 | ⚠ within organs, on part of the lines; also absent: IER3, SLC2A1, SHB |
| [[GGH]] | B | GGH activity raises ALDH7A1's level | lines that do not express GGH (5) vs lines expressing it (45) | 1.56× lower at baseline in the lines without GGH | 0.069 | ⚠ within organs, on part of the lines; also absent: AADAT, LINC01341, HHAT; maybe low, not absent |
| [[IQCJ]] | B | IQCJ activity raises ALDH7A1's level | lines that do not express IQCJ (6) vs lines expressing it (44) | 1.89× lower at baseline in the lines without IQCJ | 0.074 | ⚠ within organs, on part of the lines; also absent: ENSG00000222042, MR1, HECTD2; maybe low, not absent |
| [[LRRCC1]] | C | LRRCC1 activity lowers ALDH7A1's level | lines that do not express LRRCC1 (4) vs lines expressing it (46) | 3.18× higher at baseline in the lines without LRRCC1 | 0.023 | ⚠ few lines (4 vs 46); across organs; co-absent genes; also absent: SFXN3, GCA, CDKN1A; maybe low, not absent |
| [[PBK]] | C | PBK activity raises ALDH7A1's level | lines that do not express PBK (4) vs lines expressing it (46) | 2.10× lower at baseline in the lines without PBK | 0.036 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 057]] — Peroxisomal protein import; 86 genes; this gene is in the **+** arm (projection on the module's main direction 0.584). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-26.3, -50.0); signed map (-35.0, -35.6). **Vector** length 114, 33.5% of its response variance represented; |z| ≥ 3 in 1,446 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +6.1 | -0.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | +4.2 | +8.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +4.2 | +7.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.0 | -1.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.9 | +6.0 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +3.6 | +2.8 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +3.5 | +2.2 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -11.2 | -14.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -10.0 | -14.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -6.9 | -4.3 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -5.8 | -9.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.7 | -11.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.4 | -6.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.2 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | aldehyde dehydrogenase 7 family member A1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q23.2 — chr5:126,531,200-126,595,362 (-) |
| Ensembl biotype | protein_coding |
| Also known as | EPD, PDE; previously ATQ1 |
| Gene groups (HGNC) | Aldehyde dehydrogenases |
| Hallmark sets | GLYCOLYSIS |
| Reactome | 3 pathways, smallest: Choline catabolism; Lysine catabolism; Metabolism of amino acids and derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [P49419](https://www.uniprot.org/uniprotkb/P49419) (Alpha-aminoadipic semialdehyde dehydrogenase):

> Aldehyde dehydrogenase enzyme that mediates important protective effects. Protects cells from oxidative stress by metabolizing a number of lipid peroxidation-derived aldehydes. Involved in cellular defense against hyperosmotic stress by metabolizing betaine aldehyde to betaine, an important cellular osmolyte and methyl donor.; [Isoform 1]: Involved in lysine catabolism in the brain by mediating the conversion of L-aminoadipate-semialdehyde ((S)-2-amino-6-oxohexanoate) to L-2-aminoadipate.; …

**Summary**, from NCBI Gene [501](https://www.ncbi.nlm.nih.gov/gene/501):

> The protein encoded by this gene is a member of subfamily 7 in the aldehyde dehydrogenase gene family. These enzymes are thought to play a major role in the detoxification of aldehydes generated by alcohol metabolism and lipid peroxidation. This particular member has homology to a previously described protein from the green garden pea, the 26g pea turgor protein. It is also involved in lysine catabolism that is known to occur in the mitochondrial matrix. Recent reports show that this protein is …

**Accessions** — [HGNC:877](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:877) · Entrez [501](https://www.ncbi.nlm.nih.gov/gene/501) · UniProt [P49419](https://www.uniprot.org/uniprotkb/P49419) · Ensembl [ENSG00000164904](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164904)

## Data

Gene col 9027: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9027); `tables/drug_effects.parquet` (86 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9027, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9027]; `tensor/DDL_lfc|DDL_z.npy` [9027]; `embed/gene_vectors.npy` [9027]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9027 or target_col == 9027). Every well: [[ALDH7A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ALDH7A1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
