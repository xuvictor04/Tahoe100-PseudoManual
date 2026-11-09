---
symbol: "GMDS"
type: "gene"
col: 3397
ensembl_id: "ENSG00000112699"
name: "GDP-mannose 4,6-dehydratase"
location: "6p25.3"
module: 23
arm: "-"
pooled_cpm: 331.35
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 15
n_dd_up_clean: 12
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# GMDS

*GDP-mannose 4,6-dehydratase* — 6p25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.21× (z +26.6, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (7 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 0.566× (z -12.5, q 5e-33, down in 37 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 0.753× (z -9.2, q 1e-17, down in 32 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EML4]] (+0.63, fdr 2e-05), [[ARHGAP8]] (+0.62, fdr 2e-05), [[SPIDR]] (+0.60, fdr 4e-05); moves opposite to [[C3orf38]] (-0.67, fdr 1e-05), [[ZNF563]] (-0.62, fdr 3e-05), [[METTL6]] (-0.62, fdr 2e-05).
> It sits in the **-** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[RNF128]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3397.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.21×** | +26.6 | 0e+00 | 46/48 (HOP62, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.66×** | +22.3 | 0e+00 | 44/48 (HOP62, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.45×** | +20.4 | 0e+00 | 43/48 (HOP62, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.78×** | +13.1 | 5e-37 | 41/48 (HOP62, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.66×** | +11.6 | 4e-29 | 40/48 (MIA PaCa-2, SW 900, …) | all doses, flat |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.49×** | +9.2 | 5e-18 | 36/48 (HOP62, PANC-1, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.01×** | +8.3 | 6e-15 | 35/49 (PANC-1, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.29×** | +8.3 | 9e-15 | 30/48 (SW 900, HS-578T, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **1.52×** | +5.0 | 4e-05 | 32/48 (MIA PaCa-2, SW1417, …) | rises with dose | noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.34×** | +3.5 | 0.025 | 20/48 (MIA PaCa-2, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | 1.11× | +3.3 | 0.045 | 4/48 (SW48, HT-29, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.32×** | +3.3 | 0.045 | 18/48 (MIA PaCa-2, H4, …) | all doses, flat | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +3.2 | 0.049 | 20/49 (SW 900, NCI-H2347, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | 1.16× | +3.2 | 0.049 | 15/48 (Panc 03.27, NCI-H1573, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.15× | +3.1 | 0.062 | 11/48 (H4, HS-578T, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.20×** | +3.0 | 0.082 | 17/48 (MIA PaCa-2, SW 900, …) | rises with dose | noisy plate (z scaled) |
| [[Dapagliflozin (drug)]] 0.05 µM |  | 1.14× | +3.0 | 0.082 | 5/48 (A498, Panc 03.27, …) | inconsistent across doses |  |
| [[venetoclax (drug)]] 5 µM |  | **1.28×** | +3.0 | 0.094 | 15/48 (AsPC-1, H4, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 11 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3397.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.566×** | -12.5 | 5e-33 | 37/47 (KATO III, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.753×** | -9.2 | 1e-17 | 32/48 (C32, CFPAC-1, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.755×** | -9.1 | 2e-17 | 27/49 (KATO III, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.662×** | -9.1 | 2e-17 | 28/44 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.654×** | -8.4 | 6e-15 | 33/49 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~32% of this change | **0.731×** | -7.1 | 9e-11 | 32/48 (HT-29, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[TAK-901 (drug)]] 5 µM |  | **0.556×** | -7.0 | 2e-10 | 38/49 (LoVo, NCI-H460, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **0.792×** | -5.3 | 7e-06 | 34/48 (KATO III, CFPAC-1, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM |  | **0.799×** | -5.1 | 2e-05 | 30/48 (A498, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.775×** | -5.0 | 3e-05 | 28/48 (HT-29, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.809×** | -4.8 | 7e-05 | 24/48 (A-427, LoVo, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.689×** | -4.4 | 4e-04 | 29/47 (PANC-1, RKO, …) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.811×** | -4.1 | 0.002 | 23/48 (C32, KATO III, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~75% of this change | 0.837× | -4.1 | 0.002 | 23/48 (KATO III, LOX-IMVI, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.840× | -4.0 | 0.003 | 21/48 (LS 180, C32, …) | all doses, flat |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 0.844× | -3.9 | 0.004 | 21/48 (COLO 205, LS 180, …) | top dose only |  |
| [[Vilanterol (drug)]] 5 µM |  | 0.888× | -3.8 | 0.004 | 7/49 (RKO, HOP62, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.727×** | -3.8 | 0.005 | 23/48 (SNU-1, HS-578T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.894× | -3.6 | 0.009 | 15/49 (KATO III, HepG2/C3A, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.808×** | -3.5 | 0.015 | 20/48 (HEC-1-A, HepG2/C3A, …) | two highest doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.900× | -3.4 | 0.019 | 15/48 (LOX-IMVI, SNU-1, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.873× | -2.9 | 0.096 | 13/47 (LS 180, LoVo, …) | all doses, flat | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.36 per unit of S-phase module lfc, -0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3397. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 2,146 | 0 | 15 (13 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.158× (z -25.2) |
| [[J82 (line)]] | alt | 202 | 5 (1 ⚠) | 7 (6 ⚠) | [[Panobinostat (drug)]] 5 µM 3.96× (z +19.1) | [[Harringtonine (drug)]] 5 µM 0.473× (z -10.0) ⚠ cell-cycle shift, explains ~90% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.603× (z -10.0) |
| [[LS 180 (line)]] | wt | 1,212 | 0 | 9 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.476× (z -12.9) |
| [[NCI-H2347 (line)]] | alt | 92.2 | 9 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.98× (z +21.3) | — |
| [[CFPAC-1 (line)]] | alt | 185 | 6 (1 ⚠) | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.32× (z +19.5) | [[Selinexor (drug)]] 5 µM 0.592× (z -9.9) |
| [[LOX-IMVI (line)]] | wt | 213 | 3 | 5 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 3.11× (z +14.8) | [[Homoharringtonine (drug)]] 0.5 µM 0.443× (z -10.6) ⚠ cell-cycle shift, explains ~75% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.596× (z -9.6) |
| [[PANC-1 (line)]] | alt | 151 | 4 | 4 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 4.12× (z +22.9) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.441× (z -13.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW 900 (line)]] | alt | 149 | 7 (2 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 4.53× (z +18.2) | [[Selinexor (drug)]] 5 µM 0.609× (z -8.5) |
| [[A-427 (line)]] | wt | 191 | 3 | 4 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.41× (z +12.4) | [[Dinaciclib (drug)]] 0.05 µM 0.436× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.467× (z -10.8) |
| [[AsPC-1 (line)]] | alt | 139 | 6 (2 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 6.54× (z +23.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.579× (z -9.8) |
| [[HepG2_C3A (line)]] | wt | 813 | 0 | 7 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.299× (z -12.8) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.520× (z -10.2) |
| [[HOP62 (line)]] | alt | 105 | 7 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 7.62× (z +25.0) | — |
| [[NCI-H1792 (line)]] | alt | 297 | 4 | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.26× (z +15.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.447× (z -14.7) |
| [[HEC-1-A (line)]] | alt | 270 | 5 (2 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.37× (z +13.7) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.552× (z -9.2) ⚠ toxic |
| [[HS-578T (line)]] | alt | 151 | 6 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 6.12× (z +22.2) | — |
| [[HT-29 (line)]] | alt | 816 | 0 | 6 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.179× (z -18.1) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.381× (z -15.0) |
| [[LoVo (line)]] | wt | 774 | 0 | 6 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.276× (z -14.4) ⚠ toxic · without an alert: [[TAK-901 (drug)]] 5 µM 0.244× (z -8.5) |
| [[MIA PaCa-2 (line)]] | alt | 200 | 4 (1 ⚠) | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.48× (z +17.0) | [[Adagrasib (drug)]] 0.05 µM 0.604× (z -19.6) ⚠ position not correctable · without an alert: [[Binimetinib (drug)]] 0.5 µM 0.524× (z -8.9) |
| [[NCI-H23 (line)]] | alt | 282 | 4 (1 ⚠) | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.53× (z +12.6) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.457× (z -10.3) ⚠ toxic |
| [[NCI-H460 (line)]] | wt | 252 | 5 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.82× (z +15.5) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.467× (z -11.0) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 197 | 5 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.99× (z +17.7) | [[Dinaciclib (drug)]] 5 µM 0.423× (z -10.5) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 162 | 5 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.98× (z +15.1) | — |
| [[Hs 766T (line)]] | wt | 108 | 5 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 6.25× (z +18.1) | — |
| [[NCI-H2030 (line)]] | alt | 178 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.46× (z +14.2) | [[Harringtonine (drug)]] 5 µM 0.420× (z -9.6) ⚠ cell-cycle shift, explains ~90% of this change |
| [[Panc 03.27 (line)]] | alt | 251 | 4 (1 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 3.45× (z +15.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.603× (z -8.8) |
| [[A-172 (line)]] | wt | 102 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 5.63× (z +19.3) | — |
| [[A498 (line)]] | wt | 106 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.59× (z +17.7) | — |
| [[A549 (line)]] | wt | 94.8 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 4.99× (z +19.1) | — |
| [[C32 (line)]] | wt | 384 | 0 | 4 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.319× (z -11.7) ⚠ toxic · without an alert: [[Selinexor (drug)]] 5 µM 0.486× (z -10.8) |
| [[hTERT-HPNE (line)]] | wt | 112 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 7.05× (z +17.2) | — |
| [[NCI-H1573 (line)]] | alt | 89.8 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.88× (z +18.4) | — |
| [[RPMI-7951 (line)]] | alt | 98.4 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 4.38× (z +13.5) | — |
| [[SNU-1 (line)]] | wt | 167 | 2 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.15× (z +11.7) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.296× (z -11.9) ⚠ toxic · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.554× (z -8.5) |
| [[SNU-423 (line)]] | alt | 105 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 6.16× (z +19.8) | — |
| [[SW480 (line)]] | alt | 525 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.365× (z -18.0) |
| [[COLO 205 (line)]] | alt | 1,056 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.322× (z -13.8) |
| [[RKO (line)]] | wt | 236 | 2 (1 ⚠) | 1 (1 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.38× (z +10.5) ⚠ unreliable plate only · without an alert: [[Panobinostat (drug)]] 5 µM 2.34× (z +10.3) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.251× (z -16.0) ⚠ toxic |
| [[SW1417 (line)]] | alt | 390 | 1 (1 ⚠) | 2 (1 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.27× (z +10.6) ⚠ unreliable plate only | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.409× (z -16.4) |
| [[BT-474 (line)]] | alt | 422 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.408× (z -14.2) |
| [[C-33 A (line)]] | alt | 235 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.11× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.458× (z -9.1) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 202 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.398× (z -9.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.422× (z -9.0) |
| [[HCT15 (line)]] | alt | 231 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.71× (z +10.5) | — |
| [[SHP-77 (line)]] | alt | 477 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.454× (z -13.3) |
| [[SW48 (line)]] | wt | 343 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.510× (z -10.8) |
| [[AN3 CA (line)]] | alt | 523 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.484× (z -8.6) |
| [[NCI-H661 (line)]] | alt | 203 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.384× (z -8.5) |
| [[SW 1271 (line)]] | alt | 138 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.105× (z -10.5) ⚠ toxic; transcription drop |
| [[NCI-H2122 (line)]] | alt | 273 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 345 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 134 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3397), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*44 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EML4]] | +0.63 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[ARHGAP8]] | +0.62 | +0.46 / +0.56 | both halves | 2e-05 |  |
| [[SPIDR]] | +0.60 | +0.42 / +0.58 | both halves | 4e-05 |  |
| [[SPATA13]] | +0.60 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[TRAPPC9]] | +0.60 | +0.43 / +0.56 | both halves | 3e-05 | pathway: Asparagine N-linked glycosylation |
| [[RALGAPA2]] | +0.59 | +0.40 / +0.54 | both halves | 5e-05 |  |
| [[CMSS1]] | +0.59 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[LRP8]] | +0.57 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[BRI3BP]] | +0.56 | +0.55 / +0.46 | both halves | 3e-05 |  |
| [[AGAP1]] | +0.55 | +0.42 / +0.42 | both halves | 4e-05 |  |
| [[LRBA]] | +0.55 | +0.38 / +0.50 | both halves | 6e-05 |  |
| [[LMBR1]] | +0.55 | +0.49 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*56 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C3orf38]] | -0.67 | -0.57 / -0.55 | both halves | 1e-05 |  |
| [[ZNF563]] | -0.62 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[METTL6]] | -0.62 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[RBM48]] | -0.61 | -0.45 / -0.55 | both halves | 3e-05 |  |
| [[APPBP2]] | -0.60 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[BTN2A1]] | -0.60 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[SUPT7L]] | -0.59 | -0.41 / -0.54 | both halves | 4e-05 |  |
| [[ZNF846]] | -0.59 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[FBXO8]] | -0.58 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[ZNF490]] | -0.58 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[IFT46]] | -0.56 | -0.49 / -0.36 | both halves | 9e-05 |  |
| [[AMZ2]] | -0.56 | -0.55 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RNF128]] | B | RNF128 activity raises GMDS's level | lines that do not express RNF128 (23) vs lines expressing it (27) | 1.86× lower at baseline in the lines without RNF128 | 0.014 | ⚠ within organs, on part of the lines; also absent: AZGP1, RNF43, PROM1 |
| [[RNF128]] | B | RNF128 activity weakens GMDS's drug response | lines that do not express RNF128 (23) vs lines expressing it (26) | the lines without RNF128 respond 0.97× as strongly (z diff -0.32); strongest at Panobinostat 0.5 µM: 3.13x vs 2.04x (z diff -2.9) | 0.090 | ⚠ within organs, on part of the lines; also absent: AZGP1, RNF43, PROM1; target measured in part of the lines; both ways; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **-** arm (projection on the module's main direction -0.574). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (-0.6, 16.8); signed map (-19.0, 35.8). **Vector** length 135, 44.2% of its response variance represented; |z| ≥ 3 in 1,678 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +9.7 | +11.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +7.6 | +13.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | +6.6 | +26.6 |
|  | [[Belinostat (drug)]] 5 µM |  | +6.4 | +20.4 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +6.4 | +9.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.8 | +8.3 |
|  | [[EX229 (drug)]] 5 µM |  | +4.6 | +5.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +4.4 | +2.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +4.3 | +3.3 |
|  | [[venetoclax (drug)]] 5 µM |  | +4.3 | +3.0 |
| fall | [[Selinexor (drug)]] 5 µM |  | -10.9 | -9.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -8.2 | -12.5 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -6.7 | -5.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | -5.2 | -7.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.7 | -1.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -4.3 | -2.5 |
|  | [[Radotinib (drug)]] 5 µM |  | -4.2 | -2.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.1 | -3.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.1 | -4.0 |

## What is on record

|  |  |
|---|---|
| Name | GDP-mannose 4,6-dehydratase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p25.3 — chr6:1,623,806-2,245,605 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GMD, SDR3E1 |
| Gene groups (HGNC) | Short chain dehydrogenase/reductase superfamily; Carbon-oxygen lyases |
| Reactome | 4 pathways, smallest: GDP-fucose biosynthesis; Synthesis of substrates in N-glycan biosythesis; Biosynthesis of the N-glycan precursor (dolichol lipid-linked oligosaccharide, LLO) and transfer to a nascent protein |
| Matched by | ensembl_id |

**Function**, from UniProt [O60547](https://www.uniprot.org/uniprotkb/O60547) (GDP-mannose 4,6 dehydratase):

> Catalyzes the conversion of GDP-D-mannose to GDP-4-dehydro-6-deoxy-D-mannose.

**Summary**, from NCBI Gene [2762](https://www.ncbi.nlm.nih.gov/gene/2762):

> GDP-mannose 4,6-dehydratase (GMD; EC 4.2.1.47) catalyzes the conversion of GDP-mannose to GDP-4-keto-6-deoxymannose, the first step in the synthesis of GDP-fucose from GDP-mannose, using NADP+ as a cofactor. The second and third steps of the pathway are catalyzed by a single enzyme, GDP-keto-6-deoxymannose 3,5-epimerase, 4-reductase, designated FX in humans (MIM 137020).[supplied by OMIM, Aug 2009]

**Accessions** — [HGNC:4369](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4369) · Entrez [2762](https://www.ncbi.nlm.nih.gov/gene/2762) · UniProt [O60547](https://www.uniprot.org/uniprotkb/O60547) · Ensembl [ENSG00000112699](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000112699)

## Data

Gene col 3397: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3397); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3397, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3397]; `tensor/DDL_lfc|DDL_z.npy` [3397]; `embed/gene_vectors.npy` [3397]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3397 or target_col == 3397). Every well: [[GMDS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GMDS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
