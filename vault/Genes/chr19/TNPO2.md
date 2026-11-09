---
symbol: "TNPO2"
type: "gene"
col: 2622
ensembl_id: "ENSG00000105576"
name: "transportin 2"
location: "19p13.13"
module: 46
arm: "+"
pooled_cpm: 44.77
n_lines_expressing: 50
n_dd_up: 31
n_dd_down: 5
n_dd_up_clean: 19
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/046"]
generated_by: "tahoemap"
---

# TNPO2

*transportin 2* — 19p13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (12 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.60× (z +18.0, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.885× (z -7.8, q 3e-12, down in 7 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.783× (z -6.6, q 1e-08, down in 32 of 48 measured lines).
> Its strongest partners by |cos| (89 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 12 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BRD1]] (+0.61, fdr 3e-05), [[SETD1B]] (+0.60, fdr 2e-04), [[IGF2BP1]] (+0.60, fdr 5e-05); moves opposite to [[PJA2]] (-0.57, fdr 6e-05), [[NDUFA12]] (-0.56, fdr 1e-04), [[LINC00888]] (-0.56, fdr 1e-05).
> It sits in the **+** arm of [[Module 046]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 13 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2622.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.60×** | +18.0 | 0e+00 | 47/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.45×** | +16.9 | 0e+00 | 46/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.81×** | +15.8 | 0e+00 | 40/48 (HS-578T, BT-474, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.73×** | +14.6 | 0e+00 | 38/48 (PANC-1, NCI-H460, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.08×** | +13.8 | 3e-41 | 46/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **1.94×** | +12.0 | 2e-31 | 32/42 (SW480, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.89×** | +12.0 | 4e-31 | 45/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **1.83×** | +11.4 | 3e-28 | 37/47 (LoVo, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.84×** | +10.7 | 1e-24 | 35/45 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.66×** | +9.2 | 2e-18 | 34/48 (PANC-1, A498, …) | top dose only | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.53×** | +9.1 | 3e-18 | 37/49 (HS-578T, LoVo, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.61×** | +8.6 | 4e-16 | 34/47 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.42×** | +6.6 | 2e-09 | 34/48 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.92×** | +6.4 | 5e-09 | 30/48 (PANC-1, HS-578T, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +5.7 | 3e-07 | 26/48 (NCI-H460, HS-578T, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[EX229 (drug)]] 5 µM |  | **1.75×** | +5.5 | 1e-06 | 32/48 (MIA PaCa-2, A498, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.33×** | +5.4 | 2e-06 | 27/48 (A498, PANC-1, …) | top dose only |  |
| [[venetoclax (drug)]] 5 µM |  | **1.70×** | +5.2 | 5e-06 | 29/48 (NCI-H460, A498, …) | top dose only | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.32×** | +5.0 | 1e-05 | 24/48 (SNU-423, HS-578T, …) | top dose only | cell-cycle shift (explains ~16% here); position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **1.62×** | +4.7 | 6e-05 | 21/48 (NCI-H460, A498, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.61×** | +4.7 | 8e-05 | 24/48 (MIA PaCa-2, A498, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.60×** | +4.7 | 8e-05 | 27/48 (NCI-H460, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.26×** | +4.4 | 3e-04 | 18/48 (NCI-H2030, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2622.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.885× | -7.8 | 3e-12 | 7/48 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.783×** | -6.6 | 1e-08 | 32/48 (NCI-H1573, A-172, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.724×** | -6.1 | 2e-07 | 28/48 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.765×** | -5.1 | 5e-05 | 25/48 (PANC-1, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.787×** | -4.5 | 6e-04 | 22/48 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **0.796×** | -4.3 | 0.001 | 22/48 (BT-474, NCI-H460, …) | rises with dose |  |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.840× | -3.3 | 0.079 | 14/48 (NCI-H460, SW 1271, …) | inconsistent across doses | position effect removed |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | 0.839× | -3.2 | 0.093 | 17/47 (SW 1271, hTERT-HPNE, …) | top dose only |  |
| [[Ciclopirox (drug)]] 5 µM |  | 0.893× | -3.0 | 0.15 | 9/48 (SNU-1, MIA PaCa-2, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, +0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2622. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 34.7 | 12 (8 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +16.6) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.79× (z +14.6) | — |
| [[SW480 (line)]] | alt | 48.2 | 9 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.98× (z +11.9) | — |
| [[HS-578T (line)]] | alt | 41.9 | 8 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.56× (z +16.4) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.71× (z +13.0) | — |
| [[PANC-1 (line)]] | alt | 45.8 | 7 (3 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.24× (z +19.8) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.01× (z +16.5) | [[Panobinostat (drug)]] 5 µM 0.438× (z -9.8) |
| [[HOP62 (line)]] | alt | 32.6 | 7 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.43× (z +11.5) | — |
| [[LoVo (line)]] | wt | 30.7 | 6 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.96× (z +12.9) | — |
| [[SNU-423 (line)]] | alt | 59.2 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.20× (z +16.3) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.25× (z +11.4) | — |
| [[A549 (line)]] | wt | 24.9 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +11.2) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.75× (z +10.4) | — |
| [[hTERT-HPNE (line)]] | wt | 39.5 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +9.2) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.44× (z +8.9) | — |
| [[A498 (line)]] | wt | 45.9 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +16.0) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.86× (z +9.9) | — |
| [[BT-474 (line)]] | alt | 82.2 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.40× (z +12.3) | — |
| [[J82 (line)]] | alt | 49.5 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +11.8) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.66× (z +9.6) | — |
| [[KATO III (line)]] | alt | 26.6 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.71× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.42× (z +9.6) | — |
| [[LS 180 (line)]] | wt | 32.2 | 3 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.94× (z +11.7) | — |
| [[SW 900 (line)]] | alt | 39.9 | 3 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.47× (z +9.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.34× (z +9.6) | — |
| [[A-172 (line)]] | wt | 73.7 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +14.6) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[COLO 205 (line)]] | alt | 28.4 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.59× (z +9.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.20× (z +9.0) | — |
| [[HEC-1-A (line)]] | alt | 55.5 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +9.7) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.72× (z +8.5) | — |
| [[HT-29 (line)]] | alt | 23.3 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.65× (z +10.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.33× (z +10.0) | — |
| [[NCI-H1792 (line)]] | alt | 28.9 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.96× (z +11.0) | — |
| [[NCI-H2030 (line)]] | alt | 66.7 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +13.7) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.90× (z +9.8) | — |
| [[NCI-H23 (line)]] | alt | 51.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.83× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[NCI-H2347 (line)]] | alt | 35.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +13.9) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.40× (z +11.1) | — |
| [[Panc 03.27 (line)]] | alt | 44.7 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.20× (z +10.0) | — |
| [[SW1417 (line)]] | alt | 49.2 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.65× (z +9.6) | — |
| [[C-33 A (line)]] | alt | 88.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.184× (z -14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[C32 (line)]] | wt | 47.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.71× (z +11.1) | — |
| [[CFPAC-1 (line)]] | alt | 20.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.63× (z +9.2) | — |
| [[H4 (line)]] | wt | 52.6 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.48× (z +9.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 70.4 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.49× (z +9.2) ⚠ unreliable plate only | — |
| [[NCI-H661 (line)]] | alt | 49.8 | 0 | 1 | — | [[Clofarabine (drug)]] 5 µM 0.0612× (z -10.4) |
| [[RPMI-7951 (line)]] | alt | 49.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.19× (z +8.8) | — |
| [[SHP-77 (line)]] | alt | 49.7 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.62× (z +10.6) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 58.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +9.6) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[SW 1271 (line)]] | alt | 60.2 | 0 | 1 | — | [[Atazanavir (sulfate) (drug)]] 0.5 µM 0.0633× (z -9.8) |
| [[A-427 (line)]] | wt | 65.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 103 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 60.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 59.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 24.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 35.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 31.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 59.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 78.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 65.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2622), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 9 of them with an alert (⚠; 8 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BRD1]] | +0.61 | +0.45 / +0.48 | both halves | 3e-05 |  |
| [[SETD1B]] | +0.60 | +0.54 / +0.32 | both halves | 2e-04 |  |
| [[IGF2BP1]] | +0.60 | +0.46 / +0.39 | both halves | 5e-05 |  |
| [[PRDM15]] | +0.60 | +0.44 / +0.52 | both halves | 3e-05 |  |
| [[ARID1A]] | +0.60 | +0.57 / +0.39 | both halves | 6e-05 | same gene group |
| [[P2RY11]] | +0.59 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[MBD3]] | +0.59 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[QTRT1]] | +0.59 | +0.42 / +0.46 | both halves | 4e-05 |  |
| [[FBXW9]] | +0.58 | +0.60 / +0.55 | both halves | 1e-05 | ⚠ **readthrough risk**: FBXW9 lies 2.6 kb 3′ of this gene on the same strand (can correlate by spillover, not regulation) |
| [[SUZ12P1]] | +0.57 | +0.56 / +0.43 | both halves | 3e-05 |  |
| [[TRAF3IP2-AS1]] | +0.57 | +0.38 / +0.33 | both halves | 1e-04 |  |
| [[KDM3B]] | +0.56 | +0.46 / +0.36 | both halves | 9e-05 |  |
| [[TRMT1]] | +0.56 | +0.42 / +0.56 | both halves | 4e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PJA2]] | -0.57 | -0.50 / -0.38 | both halves | 6e-05 |  |
| [[NDUFA12]] | -0.56 | -0.44 / -0.35 | both halves | 1e-04 |  |
| [[LINC00888]] | -0.56 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[ACP1]] | -0.56 | -0.58 / -0.35 | both halves | 1e-04 |  |
| [[OSTF1]] | -0.54 | -0.50 / -0.28 | both halves | 3e-04 |  |
| [[RYBP]] | -0.54 | -0.54 / -0.44 | both halves | 3e-05 |  |
| [[ALAS1]] | -0.54 | -0.35 / -0.45 | both halves | 1e-04 |  |
| [[TWF2]] | -0.54 | -0.46 / -0.23 | both halves | 5e-04 |  |
| [[THYN1]] | -0.54 | -0.49 / -0.19 | ⚠ not reproduced | 9e-04 |  |
| [[MKRN2]] | -0.54 | -0.49 / -0.32 | both halves | 2e-04 |  |
| [[ABHD10]] | -0.54 | -0.51 / -0.32 | both halves | 2e-04 |  |
| [[HDAC11]] | -0.53 | -0.47 / -0.26 | both halves | 4e-04 |  |
| [[MPP1]] | -0.53 | -0.46 / -0.24 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises TNPO2's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises TNPO2's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[IRF6]] | B | IRF6 activity lowers TNPO2's level | lines that do not express IRF6 (31) vs lines expressing it (19) | 1.34× higher at baseline in the lines without IRF6 | 0.072 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ST14, TMPRSS4, TMEM125 |
| [[LINC00888]] | B | LINC00888 activity raises TNPO2's level | lines that do not express LINC00888 (7) vs lines expressing it (43) | 1.51× lower at baseline in the lines without LINC00888 | 0.079 | ⚠ within organs, on part of the lines; co-absent genes; also absent: KIF3C, TBKBP1, GDAP1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 046]] — Chromatin modifying enzymes; 97 genes; this gene is in the **+** arm (projection on the module's main direction 0.568). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-5.3, 12.8); signed map (27.4, -26.8). **Vector** length 101, 28.6% of its response variance represented; |z| ≥ 3 in 1,080 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.5 | +15.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +6.8 | +18.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +6.6 | +13.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.1 | +16.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +6.1 | +8.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.4 | +3.7 |
|  | [[EX229 (drug)]] 5 µM |  | +3.7 | +5.5 |
|  | [[venetoclax (drug)]] 5 µM |  | +3.6 | +5.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.3 | +6.4 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +3.2 | +4.4 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -5.8 | -4.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | -5.4 | -6.1 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.8 | -5.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.6 | -6.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.2 | +1.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.5 | +0.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.2 | -0.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.8 | -1.4 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.8 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | transportin 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.13 — chr19:12,699,201-12,724,011 (-) |
| Ensembl biotype | protein_coding |
| Also known as | IPO3, KPNB2B, FLJ12155, TRN2 |
| Gene groups (HGNC) | Importins; Armadillo like helical domain containing; Small nucleolar RNA protein coding host genes |
| Hallmark sets | G2M_CHECKPOINT |
| Matched by | ensembl_id |

**Function**, from UniProt [O14787](https://www.uniprot.org/uniprotkb/O14787) (Transportin-2):

> Probably functions in nuclear protein import as nuclear transport receptor. Serves as receptor for nuclear localization signals (NLS) in cargo substrates. Is thought to mediate docking of the importin/substrate complex to the nuclear pore complex (NPC) through binding to nucleoporin and the complex is subsequently translocated through the pore by an energy requiring, Ran-dependent mechanism. At the nucleoplasmic side of the NPC, Ran binds to the importin, the importin/substrate complex …

**Summary**, from NCBI Gene [30000](https://www.ncbi.nlm.nih.gov/gene/30000):

> Predicted to enable nuclear import signal receptor activity and nuclear localization sequence binding activity. Predicted to be involved in protein import into nucleus. Predicted to act upstream of or within negative regulation of muscle cell differentiation. Predicted to be located in nuclear lumen. Predicted to be active in cytoplasm and nucleus. Implicated in intellectual developmental disorder with hypotonia, impaired speech, and dysmorphic facies. [provided by Alliance of Genome Resources, …

**Accessions** — [HGNC:19998](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19998) · Entrez [30000](https://www.ncbi.nlm.nih.gov/gene/30000) · UniProt [O14787](https://www.uniprot.org/uniprotkb/O14787) · Ensembl [ENSG00000105576](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105576)

## Data

Gene col 2622: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2622); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2622, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2622]; `tensor/DDL_lfc|DDL_z.npy` [2622]; `embed/gene_vectors.npy` [2622]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2622 or target_col == 2622). Every well: [[TNPO2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TNPO2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
