---
symbol: "LYRM7"
type: "gene"
col: 11846
ensembl_id: "ENSG00000186687"
name: "LYR motif containing 7"
location: "5q23.3-q31.1"
module: 11
arm: "-"
pooled_cpm: 24.9
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 15
n_dd_up_clean: 12
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# LYRM7

*LYR motif containing 7* — 5q23.3-q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.37× (z +19.8, q 0e+00, up in 42 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 2.70× (z +16.2, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.626× (z -7.7, q 9e-12, down in 33 of 48 measured lines).
> Its strongest partners by |cos| (49 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 51 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CPSF6]] (+0.60, fdr 3e-04), [[EEF1AKMT2]] (+0.56, fdr 0.006, ⚠ one half only (not replicated)), [[EIF1AX]] (+0.53, fdr 5e-05), [[POFUT1]] (+0.52, fdr 5e-04); moves opposite to [[TSSC4]] (-0.61, fdr 3e-04), [[EGLN2]] (-0.57, fdr 5e-04), [[FAM32A]] (-0.54, fdr 9e-04, ⚠ one half only (not replicated)), [[CASKIN2]] (-0.53, fdr 9e-05).
> It sits in the **-** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[GARIN1B]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11846.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.37×** | +19.8 | 0e+00 | 42/43 (MIA PaCa-2, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.42×** | +19.3 | 0e+00 | 34/35 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.70×** | +16.2 | 0e+00 | 47/48 (LoVo, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.53×** | +15.2 | 0e+00 | 47/48 (A498, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.21×** | +12.9 | 3e-36 | 41/48 (LoVo, A498, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.12×** | +11.4 | 6e-28 | 35/40 (SNU-423, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.89×** | +10.0 | 2e-21 | 37/45 (MIA PaCa-2, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.64×** | +7.8 | 6e-13 | 30/48 (HOP62, MIA PaCa-2, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.57×** | +7.1 | 1e-10 | 36/48 (MIA PaCa-2, SW480, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.46×** | +6.1 | 6e-08 | 34/48 (HT-29, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.45×** | +6.1 | 6e-08 | 30/48 (HEC-1-A, PANC-1, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.29×** | +5.8 | 2e-07 | 24/47 (J82, HS-578T, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.23×** | +4.7 | 1e-04 | 19/48 (A-427, J82, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.65×** | +4.3 | 7e-04 | 17/48 (A498, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.28×** | +4.0 | 0.003 | 18/48 (HS-578T, BT-474, …) | inconsistent across doses | position effect removed |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.58×** | +3.9 | 0.004 | 11/48 (SW480, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.18× | +3.8 | 0.005 | 19/48 (A498, LoVo, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.26×** | +3.7 | 0.006 | 22/48 (KATO III, HOP62, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.22×** | +3.2 | 0.036 | 9/48 (HOP62, NCI-H23, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.14× | +3.1 | 0.053 | 8/48 (HS-578T, A-172, …) | top dose only |  |
| [[Bendamustine (drug)]] 5 µM |  | **1.21×** | +2.9 | 0.081 | 13/47 (HEC-1-A, SW 900, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11846.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.626×** | -7.7 | 9e-12 | 33/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.631×** | -7.5 | 1e-11 | 28/47 (PANC-1, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.634×** | -7.5 | 1e-11 | 35/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.474×** | -6.4 | 2e-08 | 30/47 (A-427, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.513×** | -5.7 | 1e-06 | 28/48 (SW480, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.715×** | -5.5 | 3e-06 | 22/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.745×** | -4.8 | 1e-04 | 23/48 (HT-29, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.587×** | -4.6 | 3e-04 | 18/40 (SK-MEL-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **0.770×** | -4.1 | 0.002 | 20/48 (PANC-1, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.796×** | -3.8 | 0.009 | 15/47 (A-427, PANC-1, …) | inconsistent across doses | position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.797×** | -3.7 | 0.009 | 21/47 (NCI-H460, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.794×** | -3.7 | 0.012 | 16/47 (NCI-H23, MIA PaCa-2, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.796×** | -3.5 | 0.017 | 16/48 (J82, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.810×** | -3.5 | 0.020 | 18/48 (HCT15, PANC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.832×** | -3.0 | 0.090 | 11/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.40 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11846. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 43.6 | 3 (2 ⚠) | 6 (3 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.02× (z +13.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 2.23× (z +9.9) | [[Homoharringtonine (drug)]] 5 µM 0.408× (z -15.4) ⚠ cell-cycle shift, explains ~84% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.343× (z -13.0) |
| [[SW480 (line)]] | alt | 34.5 | 5 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 4.08× (z +14.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 2.82× (z +10.9) | [[Digitoxin (drug)]] 0.5 µM 0.374× (z -10.3) |
| [[LoVo (line)]] | wt | 23.9 | 5 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.40× (z +12.7) | — |
| [[A-427 (line)]] | wt | 33.8 | 3 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 3.35× (z +9.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 2.97× (z +9.4) | [[Homoharringtonine (drug)]] 0.5 µM 0.0977× (z -20.0) ⚠ cell-cycle shift, explains ~30% of this change |
| [[A549 (line)]] | wt | 16.9 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.91× (z +9.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 3.98× (z +8.9) | — |
| [[HEC-1-A (line)]] | alt | 31.4 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.09× (z +10.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 2.80× (z +9.7) | — |
| [[SNU-423 (line)]] | alt | 28.0 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.30× (z +11.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.313× (z -12.9) ⚠ cell-cycle shift, explains ~84% of this change |
| [[A498 (line)]] | wt | 16.0 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.17× (z +12.3) | — |
| [[HS-578T (line)]] | alt | 29.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.59× (z +12.2) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 21.9 | 3 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.71× (z +9.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 3.48× (z +8.9) | — |
| [[J82 (line)]] | alt | 23.1 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.40× (z +9.5) | — |
| [[LOX-IMVI (line)]] | wt | 21.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.80× (z +12.8) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 38.9 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.66× (z +14.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 3.40× (z +10.0) | — |
| [[C32 (line)]] | wt | 16.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.70× (z +9.6) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 22.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.33× (z +10.0) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 22.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.41× (z +9.6) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 16.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.66× (z +11.8) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 26.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.27× (z +12.1) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 17.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.22× (z +9.0) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 45.7 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.09× (z +9.6) | — |
| [[hTERT-HPNE (line)]] | wt | 18.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 5.99× (z +8.5) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 21.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.12× (z +11.0) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 25.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.80× (z +10.0) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 50.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.26× (z +8.9) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 26.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.96× (z +10.8) ⚠ toxic; transcription drop | — |
| [[SW 1271 (line)]] | alt | 48.1 | 0 | 1 | — | [[Fluvoxamine (maleate) (drug)]] 0.5 µM 0.0822× (z -8.7) |
| [[SW48 (line)]] | wt | 19.0 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.121× (z -8.7) |
| [[AN3 CA (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 23.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 25.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 21.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 24.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11846), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*52 of its nearest partners move with it, 23 of them with an alert (⚠; 23 not replicated); shown: the 12 strongest and the 4 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CPSF6]] | +0.60 | +0.28 / +0.57 | both halves | 3e-04 |  |
| [[EEF1AKMT2]] | +0.56 | +0.03 / +0.58 | ⚠ one half (not replicated) | 0.006 |  |
| [[EIF1AX]] | +0.53 | +0.41 / +0.40 | both halves | 5e-05 |  |
| [[POFUT1]] | +0.52 | +0.23 / +0.50 | both halves | 5e-04 |  |
| [[ANAPC5]] | +0.52 | +0.17 / +0.56 | ⚠ one half (not replicated) | 0.001 |  |
| [[GCSH]] | +0.51 | +0.25 / +0.49 | both halves | 4e-04 |  |
| [[PHOSPHO2]] | +0.51 | +0.32 / +0.57 | both halves | 1e-04 |  |
| [[DPY19L4]] | +0.51 | +0.27 / +0.45 | both halves | 3e-04 |  |
| [[PLA2G12A]] | +0.50 | +0.13 / +0.58 | ⚠ one half (not replicated) | 0.002 |  |
| [[LANCL1]] | +0.50 | +0.36 / +0.37 | both halves | 9e-05 |  |
| [[ARL6IP6]] | +0.49 | +0.17 / +0.44 | ⚠ not reproduced | 0.001 |  |
| [[ELMOD2]] | +0.48 | +0.25 / +0.43 | both halves | 4e-04 |  |
| [[OGT]] | +0.48 | +0.28 / +0.45 | both halves | 3e-04 |  |
| [[MANEA]] | +0.48 | +0.32 / +0.46 | both halves | 1e-04 |  |
| [[MRS2]] | +0.47 | +0.25 / +0.49 | both halves | 4e-04 |  |
| [[OTUD6B]] | +0.47 | +0.25 / +0.51 | both halves | 4e-04 |  |

## Genes that move opposite

*48 of its nearest partners move opposite, 28 of them with an alert (⚠; 28 not replicated); shown: the 12 strongest and the 4 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TSSC4]] | -0.61 | -0.28 / -0.55 | both halves | 3e-04 |  |
| [[EGLN2]] | -0.57 | -0.23 / -0.53 | both halves | 5e-04 |  |
| [[FAM32A]] | -0.54 | -0.19 / -0.52 | ⚠ one half (not replicated) | 9e-04 |  |
| [[CASKIN2]] | -0.53 | -0.37 / -0.42 | both halves | 9e-05 |  |
| [[CD2BP2]] | -0.53 | -0.29 / -0.52 | both halves | 3e-04 |  |
| [[DAXX]] | -0.52 | -0.25 / -0.50 | both halves | 4e-04 |  |
| [[TRIM47]] | -0.52 | -0.07 / -0.53 | ⚠ one half (not replicated) | 0.004 |  |
| [[MSX1]] | -0.52 | -0.02 / -0.37 | ⚠ not reproduced | 0.007 |  |
| [[COMMD5]] | -0.51 | -0.29 / -0.40 | both halves | 2e-04 |  |
| [[ADRM1]] | -0.49 | -0.25 / -0.48 | both halves | 4e-04 |  |
| [[ZNF513]] | -0.49 | -0.27 / -0.47 | both halves | 3e-04 |  |
| [[TOPORS]] | -0.49 | -0.05 / -0.44 | ⚠ not reproduced | 0.005 |  |
| [[YIPF7]] | -0.47 | -0.21 / -0.35 | both halves | 7e-04 |  |
| [[GFER]] | -0.47 | -0.23 / -0.37 | both halves | 5e-04 |  |
| [[ZNF503]] | -0.46 | -0.23 / -0.23 | both halves | 6e-04 |  |
| [[TRAPPC2B]] | -0.46 | -0.25 / -0.35 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GARIN1B]] | C | GARIN1B activity lowers LYRM7's level | lines that do not express GARIN1B (4) vs lines expressing it (46) | 1.58× higher at baseline in the lines without GARIN1B | 0.079 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: PGGHG, ALPK1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **-** arm (projection on the module's main direction -0.377). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-50.8, -9.2); signed map (-39.6, -23.1). **Vector** length 59.8, 10.8% of its response variance represented; |z| ≥ 3 in 1,040 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.5 | +19.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.8 | +19.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.2 | +11.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.8 | +3.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +1.8 | +10.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.6 | +1.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.6 | +6.1 |
|  | [[Bexarotene (drug)]] 5 µM |  | +1.6 | +0.5 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | +1.4 | +1.3 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -4.0 | +5.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~84% of this change | -3.1 | -1.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.0 | -4.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.9 | -4.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.8 | +0.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.7 | +3.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.4 | -3.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.3 | -1.8 |
|  | [[Thymol (drug)]] 0.5 µM |  | -1.3 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | LYR motif containing 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q23.3-q31.1 — chr5:131,170,944-131,205,428 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20796, MZM1L; previously C5orf31 |
| Gene groups (HGNC) | LYR motif containing; Mitochondrial respiratory chain complex assembly factors |
| Reactome | 3 pathways, smallest: Complex III assembly; Respiratory electron transport; Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5U5X0](https://www.uniprot.org/uniprotkb/Q5U5X0) (Complex III assembly factor LYRM7):

> Assembly factor required for Rieske Fe-S protein UQCRFS1 incorporation into the cytochrome b-c1 (CIII) complex. Functions as a chaperone, binding to this subunit within the mitochondrial matrix and stabilizing it prior to its translocation and insertion into the late CIII dimeric intermediate within the mitochondrial inner membrane.

**Summary**, from NCBI Gene [90624](https://www.ncbi.nlm.nih.gov/gene/90624):

> Inner mitochondrial membrane complex III (CIII) is the main enzyme complex in the mitochondrial respiratory chain, and Rieske Fe-S protein (UQCRFS1) is the last catalytic subunit added to the complex. The protein encoded by this gene is a nuclear-encoded mitochondrial matrix protein that stabilizes UQCRFS1 and chaperones it to the CIII complex. Defects in this gene are a cause of mitochondrial complex III deficiency, nuclear type 8. Three transcript variants encoding two different isoforms have …

**Accessions** — [HGNC:28072](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28072) · Entrez [90624](https://www.ncbi.nlm.nih.gov/gene/90624) · UniProt [Q5U5X0](https://www.uniprot.org/uniprotkb/Q5U5X0) · Ensembl [ENSG00000186687](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000186687)

## Data

Gene col 11846: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11846); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11846, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11846]; `tensor/DDL_lfc|DDL_z.npy` [11846]; `embed/gene_vectors.npy` [11846]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11846 or target_col == 11846). Every well: [[LYRM7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LYRM7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
