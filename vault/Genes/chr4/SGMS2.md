---
symbol: "SGMS2"
type: "gene"
col: 8835
ensembl_id: "ENSG00000164023"
name: "sphingomyelin synthase 2"
location: "4q25"
module: 109
arm: "+"
pooled_cpm: 104.91
n_lines_expressing: 45
n_dd_up: 18
n_dd_down: 13
n_dd_up_clean: 9
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 3
tags: ["gene", "module/109"]
generated_by: "tahoemap"
---

# SGMS2

*sphingomyelin synthase 2* — 4q25

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.69× (z +18.1, q 0e+00, up in 41 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Ponatinib (drug)]] 5 µM: 0.553× (z -7.7, q 1e-11, down in 33 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRIB1]] (+0.62, fdr 7e-06), [[CYTOR]] (+0.62, fdr 8e-06), [[ERCC1]] (+0.61, fdr 1e-05); moves opposite to [[USP30]] (-0.57, fdr 1e-05), [[CRYZL1]] (-0.57, fdr 1e-05), [[MORN4]] (-0.56, fdr 1e-05).
> It is in [[Module 109]], a single-armed module (immediate early).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MAP2K1]] → it (grade B ⚠); 3 go from it, the strongest it → cells under [[Elimusertib hydrochloride (drug)]] 0.05 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 9 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8835.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.69×** | +18.1 | 0e+00 | 41/43 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.50×** | +11.4 | 1e-27 | 36/43 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.04×** | +9.2 | 7e-18 | 34/43 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.83×** | +7.5 | 8e-12 | 26/42 (NCI-H460, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.65×** | +6.4 | 2e-08 | 27/43 (NCI-H460, SNU-1, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.57×** | +5.8 | 7e-07 | 27/43 (NCI-H460, SNU-1, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.22×** | +5.4 | 6e-06 | 30/43 (NCI-H2030, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **2.18×** | +5.3 | 1e-05 | 25/44 (PANC-1, NCI-H2030, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.46×** | +4.8 | 1e-04 | 26/43 (NCI-H460, SNU-1, …) | two highest doses |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.42×** | +4.5 | 4e-04 | 23/43 (LS 180, NCI-H23, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **1.38×** | +4.1 | 0.002 | 21/43 (NCI-H460, SNU-1, …) | two highest doses |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.39×** | +4.1 | 0.002 | 25/42 (LS 180, A-427, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.80×** | +4.0 | 0.003 | 19/35 (NCI-H2030, SK-MEL-2, …) | top dose only | noisy plate (z scaled) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.35×** | +3.9 | 0.004 | 24/42 (A-427, LS 180, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.33×** | +3.7 | 0.008 | 23/43 (NCI-H460, BT-474, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.31×** | +3.5 | 0.017 | 18/43 (C-33 A, PANC-1, …) | top dose only |  |
| [[BAY1125976 (drug)]] 5 µM |  | **1.59×** | +3.1 | 0.054 | 23/43 (HEC-1-A, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8835.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **0.553×** | -7.7 | 1e-11 | 33/43 (NCI-H23, LoVo, …) | rises with dose | position effect removed |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **0.648×** | -5.6 | 5e-06 | 31/43 (LoVo, KATO III, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.698×** | -4.6 | 8e-04 | 28/43 (KATO III, NCI-H23, …) | rises with dose | position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.792×** | -4.3 | 0.003 | 25/43 (RKO, NCI-H1573, …) | rises with dose | low cells (technical?) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **0.727×** | -4.1 | 0.003 | 27/43 (SW 1088, NCI-H1573, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.728×** | -4.1 | 0.003 | 25/43 (SW 900, HT-29, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.808×** | -3.8 | 0.013 | 21/44 (SW480, NCI-H23, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.782×** | -3.6 | 0.023 | 20/43 (NCI-H23, RKO, …) | all doses, flat | noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | **0.824×** | -3.6 | 0.024 | 21/43 (RKO, NCI-H23, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.759×** | -3.4 | 0.040 | 22/45 (NCI-H23, RKO, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.768×** | -3.3 | 0.050 | 20/42 (SK-MEL-2, NCI-H23, …) | all doses, flat |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.772×** | -3.2 | 0.069 | 19/43 (RKO, NCI-H23, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.785×** | -3.2 | 0.069 | 20/42 (NCI-H23, SK-MEL-2, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.842× | -3.1 | 0.069 | 17/43 (NCI-H23, SW480, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, +0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8835. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 40.3 | 14 (8 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.40× (z +28.5) | — |
| [[NCI-H23 (line)]] | alt | 49.6 | 3 | 6 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 9.60× (z +22.0) | [[Adagrasib (drug)]] 0.05 µM 0.399× (z -21.3) ⚠ position not correctable · without an alert: [[Binimetinib (drug)]] 5 µM 0.274× (z -9.6) |
| [[SNU-1 (line)]] | wt | 157 | 8 (4 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.39× (z +15.9) | [[Dinaciclib (drug)]] 5 µM 0.108× (z -16.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 91.3 | 5 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.02× (z +15.9) | [[Selinexor (drug)]] 5 µM 0.344× (z -9.5) ⚠ cell-cycle shift, explains ~61% of this change |
| [[BT-474 (line)]] | alt | 88.2 | 6 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.85× (z +13.7) | — |
| [[NCI-H2030 (line)]] | alt | 87.8 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.49× (z +18.6) | — |
| [[SHP-77 (line)]] | alt | 132 | 0 | 6 (4 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.180× (z -15.2) |
| [[HepG2_C3A (line)]] | wt | 32.4 | 5 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 12.5× (z +12.2) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 3.49× (z +8.5) | — |
| [[PANC-1 (line)]] | alt | 27.6 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.42× (z +27.5) | — |
| [[SK-MEL-2 (line)]] | alt | 38.7 | 4 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 6.09× (z +16.8) | [[Cobimetinib (drug)]] 5 µM 0.219× (z -9.6) |
| [[MIA PaCa-2 (line)]] | alt | 86.3 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.34× (z +13.2) | [[Adagrasib (drug)]] 0.05 µM 0.482× (z -16.2) ⚠ position not correctable |
| [[RKO (line)]] | wt | 298 | 0 | 4 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.196× (z -14.5) ⚠ cell-cycle shift, explains ~61% of this change · without an alert: [[Radotinib (drug)]] 5 µM 0.250× (z -12.3) |
| [[A-427 (line)]] | wt | 78.5 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +16.4) | [[Dinaciclib (drug)]] 0.5 µM 0.231× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 129 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +11.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.535× (z -10.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 281 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +9.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.579× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW48 (line)]] | wt | 222 | 1 (1 ⚠) | 2 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 4.56× (z +9.1) ⚠ toxic | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.226× (z -13.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Canagliflozin (drug)]] 0.05 µM 0.209× (z -9.1) |
| [[A-172 (line)]] | wt | 56.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +9.7) | — |
| [[A549 (line)]] | wt | 67.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.36× (z +12.9) | — |
| [[AsPC-1 (line)]] | alt | 379 | 1 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.39× (z +9.6) ⚠ cell-cycle shift, explains ~32% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.285× (z -14.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 134 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +10.0) | — |
| [[HOP62 (line)]] | alt | 73.6 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.93× (z +15.3) | [[Adagrasib (drug)]] 0.05 µM 0.651× (z -9.4) ⚠ position not correctable |
| [[J82 (line)]] | alt | 69.3 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +9.4) | [[Ponatinib (drug)]] 5 µM 0.424× (z -8.5) |
| [[LoVo (line)]] | wt | 128 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +13.1) | [[Ponatinib (drug)]] 5 µM 0.382× (z -8.9) |
| [[LS 180 (line)]] | wt | 85.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.83× (z +11.6) | — |
| [[SW1417 (line)]] | alt | 72.6 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.212× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 68.6 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.18× (z +10.8) | — |
| [[COLO 205 (line)]] | alt | 58.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.10× (z +11.9) | — |
| [[H4 (line)]] | wt | 65.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +9.6) | — |
| [[HS-578T (line)]] | alt | 49.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +12.1) | — |
| [[HT-29 (line)]] | alt | 259 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.226× (z -8.7) ⚠ transcription drop |
| [[hTERT-HPNE (line)]] | wt | 26.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.64× (z +9.4) | — |
| [[NCI-H1792 (line)]] | alt | 86.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.16× (z +14.5) | — |
| [[Panc 03.27 (line)]] | alt | 156 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +8.5) | — |
| [[SNU-423 (line)]] | alt | 31.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.59× (z +14.8) | — |
| [[SW 900 (line)]] | alt | 110 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.268× (z -9.2) ⚠ transcription drop |
| [[AN3 CA (line)]] | alt | 70.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.8 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 294 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.2 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 145 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 150 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 117 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 23.4 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 85.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.5 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 26.1 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 72.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 96.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 58.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8835), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRIB1]] | +0.62 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[CYTOR]] | +0.62 | +0.58 / +0.62 | both halves | 8e-06 |  |
| [[ERCC1]] | +0.61 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[EGR1]] | +0.59 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[EGR3]] | +0.58 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[EFNB2]] | +0.58 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[FOS]] | +0.57 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[MCL1]] | +0.56 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[MIR4435-2HG]] | +0.56 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[LINC01204]] | +0.56 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[TJP1]] | +0.56 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[LAMA3]] | +0.55 | +0.51 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USP30]] | -0.57 | -0.52 / -0.58 | both halves | 1e-05 |  |
| [[CRYZL1]] | -0.57 | -0.52 / -0.60 | both halves | 1e-05 |  |
| [[MORN4]] | -0.56 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[C12orf76]] | -0.56 | -0.49 / -0.58 | both halves | 1e-05 |  |
| [[ASB7]] | -0.55 | -0.52 / -0.56 | both halves | 1e-05 |  |
| [[NAPB]] | -0.55 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[DRAM2]] | -0.54 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[CASC3]] | -0.54 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[DENND10]] | -0.54 | -0.58 / -0.45 | both halves | 3e-05 |  |
| [[METTL22]] | -0.53 | -0.41 / -0.57 | both halves | 4e-05 |  |
| [[ZMYM2]] | -0.53 | -0.56 / -0.44 | both halves | 3e-05 |  |
| [[ZSCAN2]] | -0.53 | -0.49 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises SGMS2's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.8% of all compounds | 0.053 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Elimusertib hydrochloride (drug)]] 0.05 µM | C | SGMS2 activity raises the cells' numbers under Elimusertib hydrochloride 0.05 µM (protects the cells) | lines that do not express SGMS2 (5) vs lines expressing it (43) | the lines without SGMS2: 0.77× the cells of the other lines | 0.055 | ⚠ tissue-confounded; across organs; also absent: IL15RA, RPH3AL; maybe low, not absent |
| cells under [[Idarubicin (hydrochloride) (drug)]] 0.05 µM | C | SGMS2 activity raises the cells' numbers under Idarubicin (hydrochloride) 0.05 µM (protects the cells) | lines that do not express SGMS2 (5) vs lines expressing it (43) | the lines without SGMS2: 0.78× the cells of the other lines | 0.059 | ⚠ tissue-confounded; across organs; also absent: IL15RA, RPH3AL; maybe low, not absent |
| cells under [[Everolimus (drug)]] 5 µM | C | SGMS2 activity lowers the cells' numbers under Everolimus 5 µM (makes them more sensitive) | lines that do not express SGMS2 (5) vs lines expressing it (43) | the lines without SGMS2: 1.20× the cells of the other lines | 0.083 | ⚠ tissue-confounded; across organs; also absent: IL15RA, RPH3AL; maybe low, not absent |

## Where it sits

- **Module**: [[Module 109]] — immediate early; 43 genes; every member is in the + arm (projection on the module's main direction 0.649). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (37.1, 0.4); signed map (6.0, 30.9). **Vector** length 134, 43.9% of its response variance represented; |z| ≥ 3 in 1,368 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *immediate early* (control, mean cos +0.51 to 9); *NGF-stimulated transcription* (reactome, mean cos +0.54 to 9); *TNF-alpha signaling via NF-kB* (hallmark, mean cos +0.52 to 13).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +7.3 | +18.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.0 | +9.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | +7.0 | +3.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.3 | +11.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +5.2 | -1.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.8 | +1.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.7 | +4.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.2 | +0.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.8 | +1.4 |
|  | [[Diphenhydramine (drug)]] 0.5 µM |  | +2.5 | +0.5 |
| fall | [[Ponatinib (drug)]] 5 µM |  | -5.2 | -7.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -4.0 | -2.7 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -4.0 | -5.6 |
|  | [[venetoclax (drug)]] 5 µM |  | -3.6 | -2.7 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.5 | -2.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.5 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | sphingomyelin synthase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q25 — chr4:107,824,563-107,915,047 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC26963, SMS2 |
| Hallmark sets | INFLAMMATORY_RESPONSE |
| Reactome | 3 pathways, smallest: Sphingolipid de novo biosynthesis; Sphingolipid metabolism; Metabolism of lipids |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NHU3](https://www.uniprot.org/uniprotkb/Q8NHU3) (Phosphatidylcholine:ceramide cholinephosphotransferase 2):

> Sphingomyelin synthase that primarily contributes to sphingomyelin synthesis and homeostasis at the plasma membrane. Catalyzes the reversible transfer of phosphocholine moiety in sphingomyelin biosynthesis: in the forward reaction transfers phosphocholine head group of phosphatidylcholine (PC) on to ceramide (CER) to form ceramide phosphocholine (sphingomyelin, SM) and diacylglycerol (DAG) as by-product, and in the reverse reaction transfers phosphocholine from SM to DAG to form PC and CER. The …

**Summary**, from NCBI Gene [166929](https://www.ncbi.nlm.nih.gov/gene/166929):

> Sphingomyelin, a major component of cell and Golgi membranes, is made by the transfer of phosphocholine from phosphatidylcholine onto ceramide, with diacylglycerol as a side product. The protein encoded by this gene is an enzyme that catalyzes this reaction primarily at the cell membrane. The synthesis is reversible, and this enzyme can catalyze the reaction in either direction. The encoded protein is required for cell growth. Three transcript variants encoding the same protein have been found …

**Accessions** — [HGNC:28395](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28395) · Entrez [166929](https://www.ncbi.nlm.nih.gov/gene/166929) · UniProt [Q8NHU3](https://www.uniprot.org/uniprotkb/Q8NHU3) · Ensembl [ENSG00000164023](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164023)

## Data

Gene col 8835: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8835); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8835, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8835]; `tensor/DDL_lfc|DDL_z.npy` [8835]; `embed/gene_vectors.npy` [8835]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8835 or target_col == 8835). Every well: [[SGMS2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SGMS2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
