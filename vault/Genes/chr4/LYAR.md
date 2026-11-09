---
symbol: "LYAR"
type: "gene"
col: 6965
ensembl_id: "ENSG00000145220"
name: "Ly1 antibody reactive"
location: "4p16.3"
module: 5
arm: "+"
pooled_cpm: 30.94
n_lines_expressing: 50
n_dd_up: 57
n_dd_down: 10
n_dd_up_clean: 27
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# LYAR

*Ly1 antibody reactive* — 4p16.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 57 drug-doses (30 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.94× (z +17.9, q 0e+00, up in 47 of 48 measured lines) ⚠ cell-cycle shift, explains ~36% of this change; position correction uncertain. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 2.12× (z +9.8, q 2e-20, up in 36 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Trametinib (drug)]] 5 µM: 0.706× (z -4.7, q 0.002, down in 27 of 48 measured lines) ⚠ cell-cycle shift, explains ~53% of this change. The strongest without an alert is [[Bimiralisib (drug)]] 5 µM: 0.552× (z -4.1, q 0.013, down in 23 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PDCD11]] (+0.86, fdr 7e-06), [[NOP16]] (+0.80, fdr 7e-06), [[POLR1G]] (+0.77, fdr 7e-06); moves opposite to [[ATOSA]] (-0.63, fdr 7e-06), [[TMEM59]] (-0.61, fdr 7e-06), [[GABARAP]] (-0.60, fdr 7e-06, ⚠ GABARAP in the vector space only through flagged drug-doses), [[YPEL5]] (-0.60, fdr 7e-06).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 58 in all, 30 with an alert ⚠; shown: the 15 strongest and the 12 next strongest without an alert. 57 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 30 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6965.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change; position correction uncertain | **3.94×** | +17.9 | 0e+00 | 47/48 (HOP62, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change; position correction uncertain | **3.58×** | +16.6 | 0e+00 | 47/48 (HOP62, A498, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **3.13×** | +14.8 | 0e+00 | 47/47 (HOP62, A498, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.71×** | +9.8 | 2e-20 | 37/48 (NCI-H1792, A-172, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.12×** | +9.8 | 2e-20 | 36/47 (NCI-H1792, HOP62, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change | **2.18×** | +9.7 | 2e-20 | 30/38 (A498, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | **2.17×** | +9.7 | 3e-20 | 42/47 (NCI-H1792, NCI-H1573, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.17×** | +9.6 | 4e-20 | 40/47 (LOX-IMVI, HT-29, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **2.22×** | +9.5 | 8e-20 | 43/47 (NCI-H1792, CFPAC-1, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change | **2.14×** | +9.2 | 2e-18 | 34/45 (SW480, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.78×** | +7.0 | 1e-10 | 38/48 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.72×** | +6.7 | 8e-10 | 31/48 (NCI-H1792, A498, …) | all doses, stronger at high dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **2.52×** | +6.3 | 2e-08 | 38/46 (A498, Hs 766T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change | **1.67×** | +6.1 | 3e-08 | 27/43 (NCI-H1792, A498, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~46% of this change | **1.60×** | +6.1 | 5e-08 | 33/45 (HT-29, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[PH-797804 (drug)]] 5 µM |  | **2.41×** | +6.0 | 9e-08 | 31/47 (PANC-1, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **2.35×** | +5.8 | 2e-07 | 38/48 (A498, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.56×** | +5.8 | 2e-07 | 30/48 (LOX-IMVI, MIA PaCa-2, …) | all doses, flat |  |
| [[Auranofin (drug)]] 5 µM |  | **1.55×** | +5.6 | 5e-07 | 29/47 (MIA PaCa-2, SW480, …) | top dose only | position effect removed |
| [[EX229 (drug)]] 5 µM |  | **2.26×** | +5.5 | 8e-07 | 36/47 (A498, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.52×** | +5.4 | 2e-06 | 28/47 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[TAK-733 (drug)]] 5 µM |  | **2.07×** | +4.9 | 2e-05 | 32/47 (A498, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.29×** | +4.7 | 5e-05 | 23/48 (H4, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[venetoclax (drug)]] 5 µM |  | **1.91×** | +4.4 | 2e-04 | 27/46 (SW 900, A498, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **1.65×** | +3.9 | 0.001 | 23/48 (A498, MIA PaCa-2, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[vincristine (drug)]] 5 µM |  | **1.78×** | +3.9 | 0.001 | 22/45 (HOP62, C-33 A, …) | rises with dose | noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **1.65×** | +3.9 | 0.001 | 22/47 (NCI-H23, MIA PaCa-2, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6965.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.706×** | -4.7 | 0.002 | 27/48 (LoVo, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **0.552×** | -4.1 | 0.013 | 23/48 (LoVo, SK-MEL-2, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.809×** | -3.9 | 0.019 | 22/48 (SW480, LoVo, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.758×** | -3.7 | 0.027 | 19/48 (SW480, LoVo, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.778×** | -3.7 | 0.027 | 18/48 (SW480, LoVo, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.760×** | -3.5 | 0.045 | 19/47 (LoVo, AsPC-1, …) | all doses, flat |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.764×** | -3.4 | 0.051 | 18/47 (LoVo, RKO, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.760×** | -3.4 | 0.052 | 18/47 (SW480, AsPC-1, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.777×** | -3.2 | 0.085 | 22/47 (LoVo, SW480, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.807×** | -3.1 | 0.100 | 19/48 (SW480, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[RMC-6236 (drug)]] 5 µM |  | 0.640× | -3.1 | 0.11 | 8/48 (LoVo, SW480, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | 0.783× | -3.1 | 0.11 | 13/48 (Hs 766T, SW480, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.69 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6965. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 19.6 | 11 (10 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.71× (z +12.4) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 7.80× (z +11.6) | — |
| [[A498 (line)]] | wt | 33.2 | 6 (6 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 4.17× (z +12.0) ⚠ cell-cycle shift, explains ~33% of this change; position correction uncertain | — |
| [[HOP62 (line)]] | alt | 29.1 | 5 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.14× (z +13.2) ⚠ cell-cycle shift, explains ~36% of this change; position correction uncertain · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.19× (z +9.3) | — |
| [[SW480 (line)]] | alt | 58.7 | 5 (4 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.47× (z +10.5) ⚠ cell-cycle shift, explains ~33% of this change; position correction uncertain · without an alert: [[Harringtonine (drug)]] 0.5 µM 3.09× (z +8.8) | — |
| [[CFPAC-1 (line)]] | alt | 26.2 | 4 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.63× (z +10.4) ⚠ cell-cycle shift, explains ~36% of this change; position correction uncertain · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.91× (z +9.2) | — |
| [[LOX-IMVI (line)]] | wt | 43.2 | 4 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.19× (z +10.5) ⚠ cell-cycle shift, explains ~36% of this change; position correction uncertain · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 3.31× (z +8.8) | — |
| [[A-172 (line)]] | wt | 18.0 | 3 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.06× (z +10.3) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[AsPC-1 (line)]] | alt | 25.7 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.67× (z +10.6) ⚠ cell-cycle shift, explains ~36% of this change; position correction uncertain | — |
| [[H4 (line)]] | wt | 33.3 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.80× (z +9.3) ⚠ cell-cycle shift, explains ~36% of this change; position correction uncertain | — |
| [[HS-578T (line)]] | alt | 16.3 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.27× (z +9.2) ⚠ cell-cycle shift, explains ~36% of this change; position correction uncertain | — |
| [[HT-29 (line)]] | alt | 18.6 | 3 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 6.02× (z +9.4) ⚠ cell-cycle shift, explains ~36% of this change; position correction uncertain · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.48× (z +8.9) | — |
| [[SNU-423 (line)]] | alt | 16.1 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 5.75× (z +9.9) ⚠ cell-cycle shift, explains ~33% of this change; position correction uncertain | — |
| [[A549 (line)]] | wt | 19.8 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.24× (z +10.1) ⚠ cell-cycle shift, explains ~36% of this change; position correction uncertain | — |
| [[HepG2_C3A (line)]] | wt | 20.4 | 1 (1 ⚠) | 1 | [[Panobinostat (drug)]] 0.5 µM 6.46× (z +9.4) ⚠ cell-cycle shift, explains ~33% of this change; position correction uncertain | [[Pimozide (drug)]] 0.05 µM 0.0646× (z -13.8) |
| [[Hs 766T (line)]] | wt | 20.0 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 6.09× (z +9.9) ⚠ cell-cycle shift, explains ~36% of this change; position correction uncertain | — |
| [[KATO III (line)]] | alt | 27.7 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.69× (z +10.1) ⚠ cell-cycle shift, explains ~36% of this change; position correction uncertain | — |
| [[NCI-H2347 (line)]] | alt | 27.2 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.03× (z +9.5) ⚠ cell-cycle shift, explains ~36% of this change; position correction uncertain | — |
| [[SK-MEL-2 (line)]] | alt | 46.0 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.75× (z +9.9) ⚠ cell-cycle shift, explains ~36% of this change; position correction uncertain | — |
| [[SW 900 (line)]] | alt | 17.5 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 6.01× (z +9.2) ⚠ cell-cycle shift, explains ~36% of this change; position correction uncertain | — |
| [[SW1417 (line)]] | alt | 28.3 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.31× (z +9.1) ⚠ cell-cycle shift, explains ~36% of this change; position correction uncertain | — |
| [[A-427 (line)]] | wt | 49.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.99× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change | — |
| [[CHP-212 (line)]] | wt | 32.6 | 0 | 1 | — | [[Cobimetinib (drug)]] 0.05 µM 0.0864× (z -9.1) |
| [[HEC-1-A (line)]] | alt | 38.6 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.06× (z +9.2) ⚠ cell-cycle shift, explains ~36% of this change; position correction uncertain | — |
| [[LS 180 (line)]] | wt | 26.0 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.39× (z +9.0) ⚠ cell-cycle shift, explains ~36% of this change; position correction uncertain | — |
| [[MIA PaCa-2 (line)]] | alt | 38.6 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.632× (z -10.7) ⚠ position not correctable |
| [[NCI-H1573 (line)]] | alt | 26.4 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.92× (z +9.1) ⚠ cell-cycle shift, explains ~36% of this change; position correction uncertain | — |
| [[Panc 03.27 (line)]] | alt | 20.8 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.90× (z +9.1) ⚠ cell-cycle shift, explains ~36% of this change; position correction uncertain | — |
| [[PANC-1 (line)]] | alt | 35.5 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.39× (z +8.9) ⚠ cell-cycle shift, explains ~36% of this change; position correction uncertain | — |
| [[RKO (line)]] | wt | 66.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.425× (z -9.2) ⚠ cell-cycle shift, explains ~84% of this change |
| [[RPMI-7951 (line)]] | alt | 30.6 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.96× (z +8.7) ⚠ cell-cycle shift, explains ~36% of this change; position correction uncertain | — |
| [[AN3 CA (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 49.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 24.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 34.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 45.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 37.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 49.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 60.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6965), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDCD11]] | +0.86 | +0.83 / +0.85 | both halves | 7e-06 | STRING 429 |
| [[NOP16]] | +0.80 | +0.82 / +0.80 | both halves | 7e-06 | STRING 407 |
| [[POLR1G]] | +0.77 | +0.73 / +0.76 | both halves | 7e-06 | STRING 634 |
| [[WDR3]] | +0.76 | +0.68 / +0.76 | both halves | 7e-06 |  |
| [[BOP1]] | +0.75 | +0.74 / +0.70 | both halves | 7e-06 | STRING 635 |
| [[POLR1B]] | +0.74 | +0.68 / +0.74 | both halves | 7e-06 |  |
| [[DKC1]] | +0.74 | +0.74 / +0.72 | both halves | 7e-06 | STRING 626 |
| [[NOP2]] | +0.73 | +0.74 / +0.75 | both halves | 7e-06 | STRING 667 |
| [[WDR4]] | +0.73 | +0.76 / +0.76 | both halves | 7e-06 |  |
| [[URB2]] | +0.73 | +0.74 / +0.69 | both halves | 7e-06 |  |
| [[MYBBP1A]] | +0.72 | +0.77 / +0.65 | both halves | 7e-06 | STRING 711 |
| [[TWNK]] | +0.72 | +0.79 / +0.69 | both halves | 7e-06 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATOSA]] | -0.63 | -0.63 / -0.60 | both halves | 7e-06 |  |
| [[TMEM59]] | -0.61 | -0.64 / -0.60 | both halves | 7e-06 |  |
| [[GABARAP]] ⚠ | -0.60 | -0.61 / -0.59 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[YPEL5]] | -0.60 | -0.59 / -0.62 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises LYAR's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 1.4% of all compounds | 0.017 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[MAP2K2]] | B | MAP2K2 activity raises LYAR's level | compounds that target MAP2K2: 2 of 2 lower it (Binimetinib, Trametinib) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[TOP2A]] | B | TOP2A activity lowers LYAR's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 9.5% of all compounds | 0.095 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.704). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-13.7, -38.3); signed map (-4.1, -48.5). **Vector** length 84.1, 25.7% of its response variance represented; |z| ≥ 3 in 1,421 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MYC targets v2* (hallmark, mean cos +0.63 to 13); *rRNA processing* (reactome, mean cos +0.57 to 20); *rRNA processing in the nucleus and cytosol* (reactome, mean cos +0.58 to 19).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +7.7 | +9.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +4.5 | +6.3 |
|  | [[EX229 (drug)]] 5 µM |  | +4.3 | +5.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.6 | +3.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change; position correction uncertain | +3.6 | +17.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.5 | +5.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.4 | +5.8 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~84% of this change | -3.8 | +5.9 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | -3.5 | -4.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.3 | -2.9 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -3.1 | -3.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.0 | -3.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.0 | -3.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.0 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | Ly1 antibody reactive |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p16.3 — chr4:4,267,701-4,290,154 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ZLYAR |
| Gene groups (HGNC) | Zinc fingers LYAR C2HC-type |
| Hallmark sets | E2F_TARGETS |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NX58](https://www.uniprot.org/uniprotkb/Q9NX58) (Cell growth-regulating nucleolar protein):

> Plays a role in the maintenance of the appropriate processing of 47S/45S pre-rRNA to 32S/30S pre-rRNAs and their subsequent processing to produce 18S and 28S rRNAs. Also acts at the level of transcription regulation. Along with PRMT5, binds the gamma-globin (HBG1/HBG2) promoter and represses its expression. In neuroblastoma cells, may also repress the expression of oxidative stress genes, including CHAC1, HMOX1, SLC7A11, ULBP1 and SNORD41 that encodes a small nucleolar RNA. Preferentially binds …

**Summary**, from NCBI Gene [55646](https://www.ncbi.nlm.nih.gov/gene/55646):

> Enables several functions, including DNA-binding transcription factor binding activity; identical protein binding activity; and transcription regulator inhibitor activity. Involved in several processes, including erythrocyte development; negative regulation of innate immune response; and regulation of DNA-templated transcription. Located in nucleolus and nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26021](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26021) · Entrez [55646](https://www.ncbi.nlm.nih.gov/gene/55646) · UniProt [Q9NX58](https://www.uniprot.org/uniprotkb/Q9NX58) · Ensembl [ENSG00000145220](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000145220)

## Data

Gene col 6965: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6965); `tables/drug_effects.parquet` (70 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6965, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6965]; `tensor/DDL_lfc|DDL_z.npy` [6965]; `embed/gene_vectors.npy` [6965]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6965 or target_col == 6965). Every well: [[LYAR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LYAR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
