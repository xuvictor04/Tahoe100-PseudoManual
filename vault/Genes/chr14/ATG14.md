---
symbol: "ATG14"
type: "gene"
col: 4762
ensembl_id: "ENSG00000126775"
name: "autophagy related 14"
location: "14q22.3"
module: 76
arm: "+"
pooled_cpm: 71.61
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 14
n_dd_up_clean: 19
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/076"]
generated_by: "tahoemap"
---

# ATG14

*autophagy related 14* — 14q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.17× (z +17.9, q 0e+00, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.693× (z -12.0, q 1e-30, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COMMD9]] (+0.67, fdr 7e-06), [[BSDC1]] (+0.66, fdr 7e-06), [[ATP6V0E1]] (+0.64, fdr 1e-05); moves opposite to [[VARS1]] (-0.61, fdr 1e-05), [[CYCS]] (-0.58, fdr 1e-05), [[RAPH1]] (-0.55, fdr 2e-05).
> It is in [[Module 076]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4762.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.17×** | +17.9 | 0e+00 | 41/48 (KATO III, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.89×** | +14.7 | 0e+00 | 39/48 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.78×** | +13.4 | 1e-38 | 42/48 (KATO III, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.62×** | +11.2 | 6e-27 | 36/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.60×** | +10.9 | 1e-25 | 36/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.62×** | +10.5 | 5e-24 | 42/48 (PANC-1, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.34×** | +10.3 | 7e-23 | 37/48 (SW480, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.52×** | +9.7 | 2e-20 | 39/48 (A-427, KATO III, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.18×** | +9.4 | 3e-19 | 41/49 (NCI-H23, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.31×** | +8.7 | 1e-16 | 30/48 (A498, A-427, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~6% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.00×** | +8.4 | 2e-15 | 35/45 (NCI-H460, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.59×** | +7.7 | 9e-13 | 36/49 (LOX-IMVI, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **1.78×** | +7.0 | 1e-10 | 37/47 (LoVo, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~3% here); noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.35×** | +6.9 | 2e-10 | 29/48 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.28×** | +5.8 | 3e-07 | 28/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.28×** | +5.7 | 4e-07 | 26/48 (KATO III, Panc 03.27, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.23×** | +4.7 | 8e-05 | 20/48 (RKO, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4762.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.693×** | -12.0 | 1e-30 | 42/48 (CFPAC-1, NCI-H2347, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.633×** | -10.6 | 1e-23 | 44/48 (NCI-H2347, NCI-H1792, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.671×** | -9.2 | 4e-18 | 33/49 (NCI-H2347, SHP-77, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.686×** | -8.4 | 7e-15 | 26/43 (SK-MEL-2, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.743×** | -6.9 | 7e-10 | 36/49 (NCI-H2347, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-733 (drug)]] 5 µM |  | **0.601×** | -6.2 | 7e-08 | 31/48 (NCI-H2347, HS-578T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | 0.840× | -5.7 | 9e-07 | 26/49 (LS 180, NCI-H460, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.660×** | -5.0 | 3e-05 | 24/48 (MIA PaCa-2, NCI-H23, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.762×** | -4.5 | 4e-04 | 24/48 (NCI-H1792, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Thymol (drug)]] 0.5 µM |  | **0.829×** | -4.3 | 8e-04 | 19/48 (NCI-H1792, LOX-IMVI, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.701×** | -4.3 | 9e-04 | 20/48 (NCI-H2347, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.715×** | -4.1 | 0.002 | 22/48 (NCI-H1792, NCI-H2347, …) | all doses, flat | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | 0.836× | -3.9 | 0.004 | 17/48 (AsPC-1, Hs 766T, …) | all doses, flat |  |
| [[venetoclax (drug)]] 5 µM |  | **0.734×** | -3.7 | 0.007 | 17/48 (NCI-H2347, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | 0.858× | -3.3 | 0.040 | 17/45 (C-33 A, NCI-H2347, …) | all doses, stronger at high dose | composition shift |
| [[Belzutifan (drug)]] 5 µM |  | **0.770×** | -3.2 | 0.052 | 12/47 (AsPC-1, C32, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **0.829×** | -3.1 | 0.060 | 11/49 (SHP-77, NCI-H1792, …) | all doses, flat | plate-row cell shift; noisy plate (z scaled) |
| [[Busulfan (drug)]] 0.05 µM |  | 0.861× | -3.0 | 0.072 | 7/49 (NCI-H1573, A-172, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4762. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 70.2 | 6 (2 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.74× (z +17.9) | [[Dinaciclib (drug)]] 0.5 µM 0.372× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[SW480 (line)]] | alt | 56.0 | 6 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.62× (z +13.0) | [[Tucidinostat (drug)]] 5 µM 0.631× (z -8.8) |
| [[LoVo (line)]] | wt | 56.9 | 6 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.12× (z +17.5) | — |
| [[NCI-H1792 (line)]] | alt | 135 | 2 (1 ⚠) | 4 (4 ⚠) | [[Digitoxin (drug)]] 5 µM 2.61× (z +10.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.49× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.251× (z -15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[NCI-H2347 (line)]] | alt | 146 | 1 | 5 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.86× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.316× (z -16.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 0.616× (z -10.0) |
| [[PANC-1 (line)]] | alt | 41.5 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.71× (z +16.4) | — |
| [[CFPAC-1 (line)]] | alt | 127 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.389× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 0.572× (z -10.2) |
| [[KATO III (line)]] | alt | 45.6 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.84× (z +18.1) | — |
| [[BT-474 (line)]] | alt | 45.9 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.49× (z +12.2) | — |
| [[A498 (line)]] | wt | 40.1 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +11.9) ⚠ cell-cycle shift, explains ~1% of this change · without an alert: [[Selinexor (drug)]] 5 µM 1.87× (z +8.7) | — |
| [[HepG2_C3A (line)]] | wt | 65.8 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +13.2) ⚠ cell-cycle shift, explains ~1% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.47× (z +10.1) | — |
| [[LS 180 (line)]] | wt | 57.5 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.79× (z +13.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.484× (z -10.1) ⚠ cell-cycle shift, explains ~25% of this change |
| [[NCI-H2030 (line)]] | alt | 101 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.321× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[SW1417 (line)]] | alt | 75.5 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.46× (z +13.1) | [[Dinaciclib (drug)]] 5 µM 0.384× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[COLO 205 (line)]] | alt | 52.9 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.71× (z +10.7) | — |
| [[NCI-H23 (line)]] | alt | 110 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.19× (z +10.4) | — |
| [[SW48 (line)]] | wt | 76.0 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 0.05 µM 3.32× (z +8.9) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.288× (z -9.4) ⚠ cell-cycle shift, explains ~86% of this change |
| [[A549 (line)]] | wt | 57.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +10.4) ⚠ cell-cycle shift, explains ~1% of this change | — |
| [[AsPC-1 (line)]] | alt | 69.3 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.87× (z +10.2) | — |
| [[C-33 A (line)]] | alt | 51.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.158× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change |
| [[HOP62 (line)]] | alt | 49.6 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.55× (z +9.2) | — |
| [[HT-29 (line)]] | alt | 35.0 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.79× (z +8.5) | — |
| [[hTERT-HPNE (line)]] | wt | 83.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.304× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[J82 (line)]] | alt | 56.1 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.99× (z +11.0) | — |
| [[LOX-IMVI (line)]] | wt | 64.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.429× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[MIA PaCa-2 (line)]] | alt | 77.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.486× (z -12.2) ⚠ cell-cycle shift, explains ~1% of this change |
| [[NCI-H1573 (line)]] | alt | 172 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.282× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[Panc 03.27 (line)]] | alt | 92.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.353× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[RPMI-7951 (line)]] | alt | 73.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.333× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[SHP-77 (line)]] | alt | 87.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.297× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[SK-MEL-2 (line)]] | alt | 70.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.156× (z -18.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[A-172 (line)]] | wt | 39.3 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 59.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 85.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 84.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 91.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 62.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 92.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 57.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 48.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 147 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 79.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 61.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 58.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 66.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 78.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 65.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 72.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 115 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4762), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COMMD9]] | +0.67 | +0.62 / +0.69 | both halves | 7e-06 |  |
| [[BSDC1]] | +0.66 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[ATP6V0E1]] | +0.64 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[CWF19L2]] | +0.64 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[FBXL20]] | +0.62 | +0.62 / +0.58 | both halves | 8e-06 |  |
| [[UBE4B]] | +0.62 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[CCDC28A]] | +0.61 | +0.57 / +0.64 | both halves | 1e-05 |  |
| [[UBXN6]] | +0.61 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[SYF2]] | +0.61 | +0.43 / +0.64 | both halves | 3e-05 |  |
| [[SPNS1]] | +0.60 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[FAM185BP]] | +0.60 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[HINFP]] | +0.60 | +0.52 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VARS1]] | -0.61 | -0.60 / -0.55 | both halves | 1e-05 |  |
| [[CYCS]] | -0.58 | -0.52 / -0.61 | both halves | 1e-05 |  |
| [[RAPH1]] | -0.55 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[NUP188]] | -0.55 | -0.55 / -0.53 | both halves | 1e-05 | pathway: SARS-CoV-2 Infection |
| [[CYREN]] | -0.53 | -0.56 / -0.55 | both halves | 1e-05 |  |
| [[COTL1]] | -0.53 | -0.64 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 076]]; 59 genes; every member is in the + arm (projection on the module's main direction 0.672). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-16.4, -15.1); signed map (-18.8, 6.3). **Vector** length 121, 36.6% of its response variance represented; |z| ≥ 3 in 1,282 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +7.2 | +8.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +6.8 | +13.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.4 | +9.7 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +5.7 | +10.5 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +5.6 | +6.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +4.5 | +3.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.0 | +2.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.6 | +5.7 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +3.6 | +3.6 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -9.8 | -10.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -8.0 | -12.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -6.5 | -6.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | -5.6 | -6.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~1% of this change | -5.5 | -1.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -5.5 | -5.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -5.5 | -4.3 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -5.0 | -4.5 |

## What is on record

|  |  |
|---|---|
| Name | autophagy related 14 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q22.3 — chr14:55,366,391-55,411,830 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ATG14L; previously KIAA0831 |
| Gene groups (HGNC) | Autophagy related; PIK3C3 complex subunits |
| Reactome | 13 pathways, smallest: Dengue virus modulates apoptosis; Antigen Presentation: Folding, assembly and peptide loading of class I MHC; SARS-CoV-2 activates/modulates innate and adaptive immune responses |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6ZNE5](https://www.uniprot.org/uniprotkb/Q6ZNE5) (Beclin 1-associated autophagy-related key regulator):

> Required for both basal and inducible autophagy. Determines the localization of the autophagy-specific PI3-kinase complex PI3KC3-C1. Plays a role in autophagosome formation and MAP1LC3/LC3 conjugation to phosphatidylethanolamine. Promotes BECN1 translocation from the trans-Golgi network to autophagosomes. Enhances PIK3C3 activity in a BECN1-dependent manner. Essential for the autophagy-dependent phosphorylation of BECN1. Stimulates the phosphorylation of BECN1, but suppresses the …

**Summary**, from NCBI Gene [22863](https://www.ncbi.nlm.nih.gov/gene/22863):

> Enables GTPase binding activity; phosphatidylinositol 3-kinase inhibitor activity; and protein-membrane adaptor activity. Involved in several processes, including early endosome to late endosome transport; macroautophagy; and phosphatidylinositol 3-kinase/protein kinase B signal transduction. Acts upstream of or within endosome to lysosome transport. Located in autophagosome and phagophore assembly site membrane. Is extrinsic component of omegasome membrane and extrinsic component of phagophore …

**Accessions** — [HGNC:19962](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19962) · Entrez [22863](https://www.ncbi.nlm.nih.gov/gene/22863) · UniProt [Q6ZNE5](https://www.uniprot.org/uniprotkb/Q6ZNE5) · Ensembl [ENSG00000126775](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000126775)

## Data

Gene col 4762: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4762); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4762, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4762]; `tensor/DDL_lfc|DDL_z.npy` [4762]; `embed/gene_vectors.npy` [4762]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4762 or target_col == 4762). Every well: [[ATG14 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATG14.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
