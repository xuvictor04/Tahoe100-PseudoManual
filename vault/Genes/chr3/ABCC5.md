---
symbol: "ABCC5"
type: "gene"
col: 3585
ensembl_id: "ENSG00000114770"
name: "ATP binding cassette subfamily C member 5"
location: "3q27.1"
module: 60
arm: "+"
pooled_cpm: 39.67
n_lines_expressing: 48
n_dd_up: 25
n_dd_down: 12
n_dd_up_clean: 13
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/060"]
generated_by: "tahoemap"
---

# ABCC5

*ATP binding cassette subfamily C member 5* — 3q27.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (12 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.72× (z +14.1, q 1e-42, up in 34 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (6 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.374× (z -18.1, q 0e+00, down in 40 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.381× (z -17.8, q 0e+00, down in 43 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM161A]] (+0.60, fdr 1e-05), [[CACYBP]] (+0.58, fdr 2e-05), [[ZFYVE9]] (+0.58, fdr 1e-05); moves opposite to [[REL]] (-0.52, fdr 2e-05), [[AHI1]] (-0.51, fdr 5e-05), [[PPP1R15B]] (-0.50, fdr 4e-05).
> It sits in the **+** arm of [[Module 060]] (heat shock).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[ADCY3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 14 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3585.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.72×** | +14.1 | 1e-42 | 34/46 (HEC-1-A, SW480, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.83×** | +10.5 | 3e-23 | 39/46 (SW1417, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~23% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.72×** | +10.0 | 3e-21 | 34/46 (HOP62, SW480, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.42×** | +9.2 | 7e-18 | 28/46 (HEC-1-A, MIA PaCa-2, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.58×** | +8.3 | 8e-15 | 32/46 (LS 180, PANC-1, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.35×** | +7.8 | 7e-13 | 33/46 (KATO III, LS 180, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.48×** | +7.2 | 6e-11 | 27/46 (NCI-H1573, LS 180, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.41×** | +6.4 | 1e-08 | 29/46 (PANC-1, BT-474, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.41×** | +6.3 | 1e-08 | 27/46 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.38×** | +5.7 | 6e-07 | 23/45 (SW480, A498, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.09× | +5.7 | 7e-07 | 1/46 (NCI-H23) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.36×** | +5.7 | 7e-07 | 27/45 (SW480, A498, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~56% of this change | **1.37×** | +5.6 | 1e-06 | 22/44 (A498, LS 180, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.35×** | +5.4 | 2e-06 | 24/46 (HOP62, SW480, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.34×** | +5.3 | 4e-06 | 23/46 (SW1417, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.62×** | +4.6 | 1e-04 | 20/46 (PANC-1, NCI-H1573, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.27×** | +4.4 | 4e-04 | 16/46 (PANC-1, A-172, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.33×** | +3.7 | 0.005 | 10/46 (HOP62, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Afatinib (drug)]] 5 µM |  | **1.25×** | +3.7 | 0.005 | 12/47 (NCI-H1573, RPMI-7951, …) | rises with dose | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 1.20× | +3.3 | 0.020 | 12/46 (NCI-H1573, A549, …) | all doses, flat |  |
| [[Auranofin (drug)]] 5 µM |  | 1.19× | +3.2 | 0.030 | 15/46 (SW1417, HOP62, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.18× | +3.0 | 0.046 | 15/45 (NCI-H1573, A549, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 7 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3585.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.374×** | -18.1 | 0e+00 | 40/45 (PANC-1, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.381×** | -17.8 | 0e+00 | 43/46 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.507×** | -12.5 | 1e-33 | 37/46 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.524×** | -11.9 | 2e-30 | 40/46 (PANC-1, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.565×** | -10.1 | 6e-22 | 28/46 (A-172, A-427, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.623×** | -8.7 | 2e-16 | 28/46 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.444×** | -7.8 | 4e-13 | 27/46 (A-427, HS-578T, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.677×** | -7.2 | 4e-11 | 25/46 (A-172, LOX-IMVI, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.732×** | -5.7 | 6e-07 | 26/46 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.761×** | -4.8 | 7e-05 | 21/45 (NCI-H460, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.833×** | -3.4 | 0.037 | 17/45 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~99% of this change | 0.835× | -3.3 | 0.040 | 15/44 (H4, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.726×** | -3.1 | 0.087 | 12/46 (PANC-1, H4, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.34 per unit of S-phase module lfc, -0.49 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3585. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 19.0 | 13 (1 ⚠) | 1 | [[Citalopram (hydrobromide) (drug)]] 0.05 µM 6.01× (z +10.4) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.226× (z -8.7) |
| [[PANC-1 (line)]] | alt | 42.9 | 1 (1 ⚠) | 11 (7 ⚠) | [[Panobinostat (drug)]] 5 µM 2.20× (z +8.9) ⚠ cell-cycle shift, explains ~33% of this change | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.115× (z -24.7) |
| [[A-427 (line)]] | wt | 126 | 0 | 10 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0424× (z -41.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~12% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.383× (z -12.6) |
| [[A-172 (line)]] | wt | 49.7 | 0 | 9 (5 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0793× (z -24.9) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.277× (z -13.1) |
| [[NCI-H2030 (line)]] | alt | 60.7 | 0 | 8 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.213× (z -16.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.243× (z -14.7) |
| [[NCI-H460 (line)]] | wt | 25.9 | 0 | 8 (3 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.252× (z -13.5) |
| [[A549 (line)]] | wt | 30.2 | 1 | 4 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.39× (z +9.2) | [[Digitoxin (drug)]] 5 µM 0.132× (z -15.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.134× (z -15.2) |
| [[LOX-IMVI (line)]] | wt | 39.9 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.207× (z -13.4) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.287× (z -10.7) |
| [[MIA PaCa-2 (line)]] | alt | 71.4 | 2 | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.34× (z +12.2) | [[Digitoxin (drug)]] 5 µM 0.312× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.360× (z -10.6) |
| [[C32 (line)]] | wt | 59.0 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.254× (z -11.7) |
| [[NCI-H23 (line)]] | alt | 32.6 | 0 | 4 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.237× (z -11.5) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.309× (z -9.8) |
| [[RKO (line)]] | wt | 37.4 | 0 | 4 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.177× (z -12.5) |
| [[SK-MEL-2 (line)]] | alt | 56.8 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.239× (z -11.8) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.299× (z -9.9) |
| [[SNU-1 (line)]] | wt | 37.7 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.137× (z -12.0) |
| [[SW480 (line)]] | alt | 38.1 | 4 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.75× (z +20.4) | — |
| [[HEC-1-A (line)]] | alt | 52.9 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.62× (z +21.8) | [[Lonafarnib (drug)]] 5 µM 0.236× (z -9.2) ⚠ toxic |
| [[HOP62 (line)]] | alt | 16.8 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 4.98× (z +10.4) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 3.99× (z +8.9) | [[Digitoxin (drug)]] 5 µM 0.244× (z -9.2) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 58.3 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.370× (z -10.4) ⚠ cell-cycle shift, would explain all of this change |
| [[HS-578T (line)]] | alt | 54.6 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.293× (z -11.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.312× (z -11.0) |
| [[J82 (line)]] | alt | 44.4 | 0 | 3 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.310× (z -10.6) |
| [[NCI-H1792 (line)]] | alt | 38.7 | 1 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +11.2) ⚠ cell-cycle shift, would explain all of this change | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.232× (z -11.4) |
| [[AN3 CA (line)]] | alt | 79.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.116× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[C-33 A (line)]] | alt | 83.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.111× (z -19.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 21.6 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0973× (z -10.5) |
| [[LoVo (line)]] | wt | 33.2 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.02× (z +16.9) | — |
| [[LS 180 (line)]] | wt | 20.9 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.38× (z +11.0) | — |
| [[SHP-77 (line)]] | alt | 67.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.310× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~12% of this change |
| [[SNU-423 (line)]] | alt | 26.5 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.230× (z -9.3) |
| [[SW48 (line)]] | wt | 64.1 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0444× (z -22.7) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 21.1 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 2.85× (z +8.9) ⚠ toxic; cell-cycle shift, explains ~56% of this change | — |
| [[CFPAC-1 (line)]] | alt | 23.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.71× (z +13.5) | — |
| [[HCT15 (line)]] | alt | 30.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.25× (z +11.5) | — |
| [[KATO III (line)]] | alt | 18.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.07× (z +11.3) | — |
| [[NCI-H661 (line)]] | alt | 41.3 | 0 | 1 | — | [[Atazanavir (sulfate) (drug)]] 0.5 µM 0.0805× (z -8.7) |
| [[Panc 03.27 (line)]] | alt | 36.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.61× (z +10.4) | — |
| [[RPMI-7951 (line)]] | alt | 31.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.219× (z -10.5) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 57.8 | 0 | 1 | — | [[Palmatine (chloride) (drug)]] 0.5 µM 0.0808× (z -8.9) |
| [[SW1417 (line)]] | alt | 40.7 | 1 | 0 | [[Bortezomib (drug)]] 0.05 µM 2.98× (z +8.8) | — |
| [[AsPC-1 (line)]] | alt | 7.78 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 145 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 41.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.83 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 22.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3585), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM161A]] | +0.60 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[CACYBP]] | +0.58 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[ZFYVE9]] | +0.58 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[POMT2]] | +0.57 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[OSBPL1A]] | +0.57 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[ATP2C1]] | +0.57 | +0.43 / +0.43 | both halves | 3e-05 |  |
| [[SMO]] | +0.56 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[RAP1GDS1]] | +0.56 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[KPNA3]] | +0.56 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[CASP6]] | +0.55 | +0.62 / +0.38 | both halves | 6e-05 |  |
| [[MRPL18]] | +0.54 | +0.55 / +0.40 | both halves | 5e-05 |  |
| [[AHSA1]] | +0.54 | +0.48 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[REL]] | -0.52 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[AHI1]] | -0.51 | -0.41 / -0.39 | both halves | 5e-05 |  |
| [[PPP1R15B]] | -0.50 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[CDKN2A]] | -0.47 | -0.42 / -0.57 | both halves | 4e-05 | pathway: HALLMARK_P53_PATHWAY |
| [[RSPH1]] | -0.46 | -0.31 / -0.39 | both halves | 2e-04 |  |
| [[NEU1]] | -0.45 | -0.42 / -0.27 | both halves | 3e-04 |  |
| [[YY1AP1]] | -0.44 | -0.32 / -0.42 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADCY3]] | B | ADCY3 activity raises ABCC5's level | lines that do not express ADCY3 (5) vs lines expressing it (45) | 2.00× lower at baseline in the lines without ADCY3 | 0.010 | ⚠ within organs, on part of the lines; also absent: PPP2R3A, TBC1D19, SSBP2 |
| [[TOP2A]] | B | TOP2A activity lowers ABCC5's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[REEP1]] | B | REEP1 activity raises ABCC5's level | lines that do not express REEP1 (10) vs lines expressing it (40) | 1.61× lower at baseline in the lines without REEP1 | 0.089 | ⚠ within organs, on part of the lines; also absent: SEPTIN3; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 060]] — heat shock; 78 genes; this gene is in the **+** arm (projection on the module's main direction 0.595). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-18.3, -12.0); signed map (-26.8, -27.6). **Vector** length 98.4, 26.0% of its response variance represented; |z| ≥ 3 in 1,347 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +9.9 | +10.0 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +8.8 | +10.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +7.7 | +5.4 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~45% of this change | +6.7 | +4.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +5.2 | +3.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.3 | +7.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.8 | +3.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.6 | +1.3 |
| fall | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -4.3 | -12.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.2 | -8.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -4.0 | -10.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.5 | -18.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.4 | -17.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.0 | -2.3 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -1.8 | -1.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.8 | +0.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.6 | -1.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.5 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | ATP binding cassette subfamily C member 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q27.1 — chr3:183,919,934-184,017,939 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MRP5, SMRP, EST277145, MOAT-C |
| Gene groups (HGNC) | ATP binding cassette subfamily C |
| Hallmark sets | PEROXISOME, P53_PATHWAY |
| Reactome | 8 pathways, smallest: Hyaluronan metabolism; Paracetamol ADME; Azathioprine ADME |
| Matched by | ensembl_id |

**Function**, from UniProt [O15440](https://www.uniprot.org/uniprotkb/O15440) (ATP-binding cassette sub-family C member 5):

> ATP-dependent transporter of the ATP-binding cassette (ABC) family that actively extrudes physiological compounds, and xenobiotics from cells. Mediates ATP-dependent transport of endogenous metabolites such as cAMP and cGMP, folic acid and N-lactoyl-amino acids (in vitro). Also acts as a general glutamate conjugate and analog transporter that can limit the brain levels of endogenous metabolites, drugs, and toxins. Confers resistance to the antiviral agent PMEA. Able to transport several …

**Summary**, from NCBI Gene [10057](https://www.ncbi.nlm.nih.gov/gene/10057):

> The protein encoded by this gene is a member of the superfamily of ATP-binding cassette (ABC) transporters. ABC proteins transport various molecules across extra- and intra-cellular membranes. ABC genes are divided into seven distinct subfamilies (ABC1, MDR/TAP, MRP, ALD, OABP, GCN20, White). This protein is a member of the MRP subfamily which is involved in multi-drug resistance. This protein functions in the cellular export of its substrate, cyclic nucleotides. This export contributes to the …

**Accessions** — [HGNC:56](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:56) · Entrez [10057](https://www.ncbi.nlm.nih.gov/gene/10057) · UniProt [O15440](https://www.uniprot.org/uniprotkb/O15440) · Ensembl [ENSG00000114770](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000114770)

## Data

Gene col 3585: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3585); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3585, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3585]; `tensor/DDL_lfc|DDL_z.npy` [3585]; `embed/gene_vectors.npy` [3585]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3585 or target_col == 3585). Every well: [[ABCC5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ABCC5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
