---
symbol: "PLS3"
type: "gene"
col: 2203
ensembl_id: "ENSG00000102024"
name: "plastin 3"
location: "Xq23"
module: 25
arm: "+"
pooled_cpm: 152.91
n_lines_expressing: 46
n_dd_up: 9
n_dd_down: 16
n_dd_up_clean: 6
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 4
direction_downstream: 30
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# PLS3

*plastin 3* — Xq23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.78× (z +12.2, q 3e-31, up in 34 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 1.37× (z +6.6, q 8e-09, up in 25 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.404× (z -19.1, q 0e+00, down in 42 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COPS6]] (+0.64, fdr 9e-06), [[ACTR3]] (+0.61, fdr 1e-05), [[CRYZ]] (+0.59, fdr 1e-05); moves opposite to [[TMEM258]] (-0.57, fdr 2e-05), [[INAFM1]] (-0.56, fdr 3e-05), [[POLR2J4]] (-0.54, fdr 1e-05).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[ANXA1]] → it (grade B ⚠); 30 go from it, the strongest it → [[CAV2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2203.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.78×** | +12.2 | 3e-31 | 34/45 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.79×** | +11.7 | 3e-29 | 36/40 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.37×** | +6.6 | 8e-09 | 25/44 (KATO III, LS 180, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.37×** | +6.1 | 1e-07 | 20/41 (PANC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.33×** | +6.0 | 2e-07 | 22/44 (KATO III, COLO 205, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.20×** | +5.4 | 5e-06 | 20/44 (A-427, PANC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM |  | **1.47×** | +4.2 | 0.002 | 22/43 (Panc 03.27, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~20% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.21×** | +3.8 | 0.009 | 18/44 (KATO III, SW48, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.34×** | +3.2 | 0.094 | 20/45 (NCI-H23, Panc 03.27, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 1.11× | +3.0 | 0.14 | 4/44 (SW480, HS-578T, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2203.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.404×** | -19.1 | 0e+00 | 42/44 (HEC-1-A, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.415×** | -18.5 | 0e+00 | 44/44 (HEC-1-A, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.520×** | -13.7 | 1e-40 | 41/44 (HEC-1-A, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.644×** | -13.1 | 4e-37 | 39/45 (Hs 766T, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.709×** | -10.2 | 2e-22 | 25/44 (LOX-IMVI, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.669×** | -8.5 | 3e-15 | 34/44 (AsPC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.704×** | -7.4 | 1e-11 | 30/44 (AsPC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.711×** | -7.2 | 5e-11 | 24/44 (LoVo, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.721×** | -6.9 | 4e-10 | 28/44 (NCI-H460, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.741×** | -6.3 | 2e-08 | 29/44 (CFPAC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | **0.762×** | -5.5 | 2e-06 | 22/43 (H4, RPMI-7951, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.793×** | -4.6 | 2e-04 | 24/44 (SW 1271, NCI-H2030, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.808×** | -4.5 | 3e-04 | 22/44 (HEC-1-A, NCI-H2347, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **0.813×** | -4.4 | 5e-04 | 22/44 (LoVo, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.809×** | -4.3 | 6e-04 | 19/44 (AsPC-1, NCI-H460, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.851× | -3.4 | 0.020 | 15/45 (NCI-H2347, LOX-IMVI, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.863× | -3.1 | 0.051 | 16/44 (LOX-IMVI, Hs 766T, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 5 µM |  | 0.905× | -3.0 | 0.076 | 6/45 (NCI-H2122, HS-578T, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2203. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 215 | 4 (2 ⚠) | 6 | [[Daptomycin (drug)]] 0.5 µM 3.11× (z +10.3) ⚠ unreliable plate only · without an alert: [[Peretinoin (drug)]] 5 µM 2.96× (z +9.4) | [[Homoharringtonine (drug)]] 5 µM 0.370× (z -12.6) |
| [[KATO III (line)]] | alt | 91.9 | 6 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.50× (z +11.8) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.29× (z +10.6) | [[Panobinostat (drug)]] 5 µM 0.394× (z -11.9) |
| [[AsPC-1 (line)]] | alt | 198 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.247× (z -18.7) |
| [[C32 (line)]] | wt | 91.4 | 2 (2 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 3.11× (z +11.5) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.465× (z -11.0) |
| [[CFPAC-1 (line)]] | alt | 296 | 0 | 6 | — | [[Panobinostat (drug)]] 0.5 µM 0.216× (z -16.6) |
| [[Hs 766T (line)]] | wt | 570 | 0 | 6 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.254× (z -19.1) |
| [[LS 180 (line)]] | wt | 97.3 | 1 | 5 | [[Ixazomib citrate (drug)]] 0.5 µM 2.08× (z +9.2) | [[Panobinostat (drug)]] 5 µM 0.355× (z -13.0) |
| [[A-427 (line)]] | wt | 98.8 | 4 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.60× (z +11.4) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 1.88× (z +11.1) | [[Dinaciclib (drug)]] 0.05 µM 0.329× (z -12.8) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 324 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.324× (z -18.5) |
| [[LoVo (line)]] | wt | 74.3 | 1 (1 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 2.65× (z +9.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.322× (z -15.0) |
| [[LOX-IMVI (line)]] | wt | 186 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.286× (z -19.2) |
| [[SW480 (line)]] | alt | 105 | 1 (1 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.33× (z +10.0) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.265× (z -16.4) |
| [[A549 (line)]] | wt | 211 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.13× (z +12.9) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.336× (z -12.3) |
| [[COLO 205 (line)]] | alt | 63.5 | 2 | 2 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.67× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.336× (z -13.6) |
| [[HOP62 (line)]] | alt | 196 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.215× (z -11.6) |
| [[NCI-H2347 (line)]] | alt | 252 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.411× (z -14.1) |
| [[NCI-H460 (line)]] | wt | 89.1 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.77× (z +15.0) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.541× (z -9.5) |
| [[Panc 03.27 (line)]] | alt | 130 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.16× (z +9.9) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.328× (z -14.3) |
| [[H4 (line)]] | wt | 135 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.309× (z -10.6) |
| [[HS-578T (line)]] | alt | 117 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.33× (z +11.6) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.329× (z -11.2) |
| [[HT-29 (line)]] | alt | 88.3 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.05 µM 2.28× (z +8.6) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.349× (z -11.9) |
| [[NCI-H23 (line)]] | alt | 219 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.405× (z -12.2) |
| [[PANC-1 (line)]] | alt | 138 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.92× (z +16.1) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 51.5 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.67× (z +8.6) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.351× (z -9.2) |
| [[SNU-423 (line)]] | alt | 201 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.27× (z +10.2) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.400× (z -11.9) |
| [[A498 (line)]] | wt | 184 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.41× (z +11.8) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 303 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.381× (z -9.8) |
| [[NCI-H2030 (line)]] | alt | 416 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.487× (z -11.2) |
| [[RPMI-7951 (line)]] | alt | 108 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.295× (z -12.9) |
| [[SW1417 (line)]] | alt | 57.1 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.402× (z -9.4) |
| [[hTERT-HPNE (line)]] | wt | 188 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.346× (z -8.6) |
| [[J82 (line)]] | alt | 118 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.44× (z +8.6) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 75.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.57× (z +10.3) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 104 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.332× (z -12.7) |
| [[SK-MEL-2 (line)]] | alt | 103 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.48× (z +9.6) ⚠ toxic; transcription drop | — |
| [[SW 1088 (line)]] | alt | 144 | 0 | 1 | — | [[Citalopram (hydrobromide) (drug)]] 0.5 µM 0.0749× (z -10.4) |
| [[SW 900 (line)]] | alt | 98.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.96× (z +10.0) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 75.4 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.361× (z -8.5) |
| [[A-172 (line)]] | wt | 57.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 35.0 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 35.5 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 97.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 75.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 62.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 176 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 217 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.8 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 19.0 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 74.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2203), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COPS6]] | +0.64 | +0.62 / +0.57 | both halves | 9e-06 |  |
| [[ACTR3]] | +0.61 | +0.53 / +0.64 | both halves | 1e-05 | STRING 572 |
| [[CRYZ]] | +0.59 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[DLD]] | +0.58 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[DCTN1]] | +0.57 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[UBQLN1]] | +0.57 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[CNN3]] | +0.56 | +0.49 / +0.56 | both halves | 1e-05 | STRING 638 |
| [[CFL2]] | +0.56 | +0.32 / +0.59 | both halves | 2e-04 | STRING 523 |
| [[TPM1]] | +0.55 | +0.37 / +0.59 | both halves | 8e-05 |  |
| [[API5]] | +0.55 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[MTMR2]] | +0.55 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[YWHAQ]] | +0.55 | +0.46 / +0.62 | both halves | 2e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM258]] | -0.57 | -0.47 / -0.61 | both halves | 2e-05 |  |
| [[INAFM1]] | -0.56 | -0.43 / -0.60 | both halves | 3e-05 |  |
| [[POLR2J4]] | -0.54 | -0.52 / -0.54 | both halves | 1e-05 |  |
| [[ZXDC]] | -0.54 | -0.41 / -0.62 | both halves | 4e-05 |  |
| [[AXIN1]] | -0.53 | -0.35 / -0.50 | both halves | 1e-04 |  |
| [[ZBTB7A]] | -0.52 | -0.42 / -0.55 | both halves | 4e-05 |  |
| [[TRAPPC4]] | -0.52 | -0.36 / -0.55 | both halves | 1e-04 |  |
| [[GUCA1B]] | -0.51 | -0.47 / -0.56 | both halves | 2e-05 | same gene group |
| [[CDC34]] | -0.51 | -0.37 / -0.55 | both halves | 8e-05 |  |
| [[PIAS4]] | -0.51 | -0.42 / -0.53 | both halves | 4e-05 |  |
| [[ARMC10]] | -0.51 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[LSM7]] | -0.50 | -0.48 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANXA1]] | B | ANXA1 activity raises PLS3's level | lines that do not express ANXA1 (9) vs lines expressing it (41) | 1.96× lower at baseline in the lines without ANXA1 | 0.031 | ⚠ within organs, on part of the lines; also absent: FXYD5, CAV2, RAB27B |
| [[PSMB5]] | B | PSMB5 activity lowers PLS3's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[CAV2]] | C | CAV2 activity raises PLS3's level | lines that do not express CAV2 (8) vs lines expressing it (42) | 2.79× lower at baseline in the lines without CAV2 | 0.009 | ⚠ within organs, on part of the lines; co-absent genes; also absent: PLAUR, LRRK1, HRH1; maybe low, not absent; co-absent with the target |
| [[ANXA2]] | C | ANXA2 activity raises PLS3's level | lines that do not express ANXA2 (4) vs lines expressing it (46) | 2.70× lower at baseline in the lines without ANXA2 | 0.081 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: PHF11, RARG, NABP1; maybe low, not absent; its own permutation p |

### Downstream of this gene

*30 arrows, 30 of them with an alert ⚠; grade A 0, B 0, C 30. Shown: the 12 strongest; 18 more arrows (18 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CAV2]] | C | PLS3 activity raises CAV2's level | lines that do not express PLS3 (4) vs lines expressing it (46) | 5.18× lower at baseline in the lines without PLS3 | 0.004 | ⚠ few lines (4 vs 46); across organs; also absent: FOSL1, IGF2BP2, FCHSD1; maybe low, not absent; co-absent with the target |
| cells under [[Tucatinib (drug)]] 5 µM | C | PLS3 activity raises the cells' numbers under Tucatinib 5 µM (protects the cells) | lines that do not express PLS3 (4) vs lines expressing it (44) | the lines without PLS3: 0.69× the cells of the other lines | 0.008 | ⚠ few lines (4 vs 46); across organs; also absent: FOSL1, IGF2BP2, FCHSD1; maybe low, not absent |
| cells under [[Pentoxifylline (drug)]] 0.5 µM | C | PLS3 activity raises the cells' numbers under Pentoxifylline 0.5 µM (protects the cells) | lines that do not express PLS3 (4) vs lines expressing it (44) | the lines without PLS3: 0.74× the cells of the other lines | 0.014 | ⚠ few lines (4 vs 46); across organs; also absent: FOSL1, IGF2BP2, FCHSD1; maybe low, not absent |
| cells under [[Niclosamide (olamine) (drug)]] 5 µM | C | PLS3 activity raises the cells' numbers under Niclosamide (olamine) 5 µM (protects the cells) | lines that do not express PLS3 (4) vs lines expressing it (44) | the lines without PLS3: 0.36× the cells of the other lines | 0.014 | ⚠ few lines (4 vs 46); across organs; also absent: FOSL1, IGF2BP2, FCHSD1; maybe low, not absent |
| [[ATG4B]] | C | PLS3 activity weakens ATG4B's drug response | lines that do not express PLS3 (4) vs lines expressing it (45) | the lines without PLS3 respond 1.11× as strongly (z diff -1.16); strongest at Auranofin 5 µM: 3.29x vs 1.63x (z diff -4.7) | 0.015 | ⚠ few lines (4 vs 46); across organs; also absent: FOSL1, IGF2BP2, FCHSD1; maybe low, not absent; target measured in part of the lines; artifact flags |
| cells under [[Tetracycline (hydrochloride) (drug)]] 0.5 µM | C | PLS3 activity raises the cells' numbers under Tetracycline (hydrochloride) 0.5 µM (protects the cells) | lines that do not express PLS3 (4) vs lines expressing it (44) | the lines without PLS3: 0.74× the cells of the other lines | 0.019 | ⚠ few lines (4 vs 46); across organs; also absent: FOSL1, IGF2BP2, FCHSD1; maybe low, not absent |
| [[ANXA2]] | C | PLS3 activity raises ANXA2's level | lines that do not express PLS3 (4) vs lines expressing it (46) | 2.65× lower at baseline in the lines without PLS3 | 0.021 | ⚠ few lines (4 vs 46); across organs; also absent: FOSL1, IGF2BP2, FCHSD1; maybe low, not absent |
| [[NRAS]] | C | PLS3 activity strengthens NRAS's drug response | lines that do not express PLS3 (4) vs lines expressing it (44) | the lines without PLS3 respond 0.50× as strongly (z diff +1.57); strongest at Idarubicin (hydrochloride) 5 µM: 1.04x vs 0.67x (z diff +3.6) | 0.021 | ⚠ few lines (4 vs 46); across organs; also absent: FOSL1, IGF2BP2, FCHSD1; maybe low, not absent; target measured in part of the lines; artifact flags |
| cells under [[Entecavir (monohydrate) (drug)]] 0.5 µM | C | PLS3 activity raises the cells' numbers under Entecavir (monohydrate) 0.5 µM (protects the cells) | lines that do not express PLS3 (4) vs lines expressing it (44) | the lines without PLS3: 0.69× the cells of the other lines | 0.025 | ⚠ few lines (4 vs 46); across organs; also absent: FOSL1, IGF2BP2, FCHSD1; maybe low, not absent |
| cells under [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM | C | PLS3 activity raises the cells' numbers under Bisoprolol (hemifumarate) 0.05 µM (protects the cells) | lines that do not express PLS3 (4) vs lines expressing it (44) | the lines without PLS3: 0.77× the cells of the other lines | 0.026 | ⚠ few lines (4 vs 46); across organs; also absent: FOSL1, IGF2BP2, FCHSD1; maybe low, not absent |
| cells under [[Hydroxyfasudil (drug)]] 5 µM | C | PLS3 activity lowers the cells' numbers under Hydroxyfasudil 5 µM (makes them more sensitive) | lines that do not express PLS3 (4) vs lines expressing it (44) | the lines without PLS3: 1.28× the cells of the other lines | 0.026 | ⚠ few lines (4 vs 46); across organs; also absent: FOSL1, IGF2BP2, FCHSD1; maybe low, not absent |
| cells under [[Citalopram (hydrobromide) (drug)]] 0.05 µM | C | PLS3 activity raises the cells' numbers under Citalopram (hydrobromide) 0.05 µM (protects the cells) | lines that do not express PLS3 (4) vs lines expressing it (44) | the lines without PLS3: 0.72× the cells of the other lines | 0.031 | ⚠ few lines (4 vs 46); across organs; also absent: FOSL1, IGF2BP2, FCHSD1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.598). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-25.2, -14.6); signed map (-17.8, -42.2). **Vector** length 121, 35.6% of its response variance represented; |z| ≥ 3 in 1,307 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +6.8 | +5.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.7 | +12.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.4 | +6.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.4 | +2.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.3 | +11.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.1 | +6.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.6 | +2.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.3 | +3.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.0 | +1.7 |
| fall | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -5.3 | -6.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.9 | -8.5 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~2% of this change | -3.8 | -3.9 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | -3.3 | -4.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.2 | -2.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.2 | -2.4 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.6 | -2.0 |
|  | [[Temsirolimus (drug)]] 5 µM |  | -2.5 | -3.0 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -2.5 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | plastin 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq23 — chrX:115,561,174-115,650,861 (+) |
| Ensembl biotype | protein_coding |
| Also known as | T-plastin |
| Gene groups (HGNC) | EF-hand domain containing; Plastin family |
| Matched by | ensembl_id |

**Function**, from UniProt [P13797](https://www.uniprot.org/uniprotkb/P13797) (Plastin-3):

> Actin-bundling protein.

**Summary**, from NCBI Gene [5358](https://www.ncbi.nlm.nih.gov/gene/5358):

> Plastins are a family of actin-binding proteins that are conserved throughout eukaryote evolution and expressed in most tissues of higher eukaryotes. In humans, two ubiquitous plastin isoforms (L and T) have been identified. Plastin 1 (otherwise known as Fimbrin) is a third distinct plastin isoform which is specifically expressed at high levels in the small intestine. The L isoform is expressed only in hemopoietic cell lineages, while the T isoform has been found in all other normal cells of …

**Accessions** — [HGNC:9091](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9091) · Entrez [5358](https://www.ncbi.nlm.nih.gov/gene/5358) · UniProt [P13797](https://www.uniprot.org/uniprotkb/P13797) · Ensembl [ENSG00000102024](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000102024)

## Data

Gene col 2203: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2203); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2203, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2203]; `tensor/DDL_lfc|DDL_z.npy` [2203]; `embed/gene_vectors.npy` [2203]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2203 or target_col == 2203). Every well: [[PLS3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLS3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
