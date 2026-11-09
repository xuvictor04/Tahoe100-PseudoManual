---
symbol: "GCNT1"
type: "gene"
col: 11901
ensembl_id: "ENSG00000187210"
name: "glucosaminyl (N-acetyl) transferase 1"
location: "9q21.13"
module: 106
arm: "+"
pooled_cpm: 30.57
n_lines_expressing: 45
n_dd_up: 19
n_dd_down: 15
n_dd_up_clean: 17
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 7
direction_downstream: 3
tags: ["gene", "module/106"]
generated_by: "tahoemap"
---

# GCNT1

*glucosaminyl (N-acetyl) transferase 1* — 9q21.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.06× (z +18.8, q 0e+00, up in 34 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (5 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.575× (z -10.1, q 2e-21, down in 34 of 43 measured lines).
> Its strongest partners by |cos| (87 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 14 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RIPOR2]] (+0.48, fdr 3e-05), [[SLC44A1]] (+0.48, fdr 3e-05), [[RTN4RL1]] (+0.47, fdr 6e-05); moves opposite to [[JPX]] (-0.42, fdr 3e-04), [[STEAP1B-AS1]] (-0.42, fdr 7e-05), [[TRBC2]] (-0.38, fdr 2e-04).
> It is in [[Module 106]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[PRUNE2]] → it (grade B ⚠); 3 go from it, the strongest it → [[GLUL]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11901.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.06×** | +18.8 | 0e+00 | 34/42 (NCI-H460, A-172, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.88×** | +16.5 | 0e+00 | 41/43 (SW480, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **2.18×** | +14.4 | 2e-44 | 36/43 (SW480, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.84×** | +11.2 | 5e-27 | 36/42 (SK-MEL-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.75×** | +10.3 | 6e-23 | 31/43 (NCI-H460, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.68×** | +9.5 | 2e-19 | 33/43 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.62×** | +8.9 | 7e-17 | 28/43 (NCI-H460, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.55×** | +7.8 | 4e-13 | 25/42 (NCI-H23, RKO, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Triamcinolone (drug)]] 5 µM |  | **1.25×** | +5.8 | 3e-07 | 16/43 (A-172, HOP62, …) | inconsistent across doses | position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **1.80×** | +5.7 | 9e-07 | 19/43 (SK-MEL-2, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.32×** | +4.9 | 6e-05 | 16/42 (NCI-H23, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | 1.17× | +4.0 | 0.003 | 13/43 (NCI-H460, LOX-IMVI, …) | top dose only |  |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **1.24×** | +3.9 | 0.004 | 5/43 (LS 180, SNU-423, …) | inconsistent across doses |  |
| [[Drospirenone (drug)]] 0.05 µM |  | **1.24×** | +3.9 | 0.004 | 12/43 (NCI-H460, NCI-H2347, …) | all doses, flat | position effect removed |
| [[NG25 (drug)]] 5 µM |  | **1.47×** | +3.7 | 0.007 | 14/40 (KATO III, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.23×** | +3.6 | 0.013 | 14/43 (LoVo, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.20×** | +3.4 | 0.022 | 10/43 (hTERT-HPNE, HEC-1-A, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11901.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.575×** | -10.1 | 2e-21 | 34/43 (SNU-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.607×** | -9.1 | 2e-17 | 30/41 (SNU-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Oxaliplatin (drug)]] 0.05 µM |  | **0.622×** | -8.2 | 4e-14 | 25/43 (SNU-1, A498, …) | all doses, flat | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.649×** | -7.9 | 3e-13 | 25/43 (SNU-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.497×** | -6.7 | 2e-09 | 23/43 (SNU-1, A498, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Oxaliplatin (drug)]] 5 µM |  | **0.528×** | -6.1 | 9e-08 | 23/42 (J82, SNU-1, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.719×** | -6.0 | 1e-07 | 23/42 (SNU-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.741×** | -5.3 | 1e-05 | 20/43 (SNU-1, LoVo, …) | inconsistent across doses | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.770×** | -4.8 | 1e-04 | 20/43 (LoVo, SW480, …) | two highest doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.620×** | -4.6 | 3e-04 | 16/42 (HEC-1-A, HS-578T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.932× | -4.5 | 4e-04 | 3/43 (C-33 A, NCI-H1573, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~16% of this change | **0.791×** | -4.3 | 9e-04 | 11/43 (SNU-1, HOP62, …) | all doses, stronger at high dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.642×** | -4.2 | 1e-03 | 12/42 (SW480, SNU-1, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.793×** | -3.9 | 0.004 | 14/32 (LoVo, A498, …) | inconsistent across doses | cell-cycle shift (explains ~9% here); composition shift |
| [[Ferulic acid (drug)]] 0.05 µM |  | **0.798×** | -3.8 | 0.005 | 14/42 (SNU-1, HEC-1-A, …) | inconsistent across doses | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.836× | -3.3 | 0.036 | 13/42 (COLO 205, KATO III, …) | two highest doses |  |
| [[Amsacrine (drug)]] 5 µM |  | 0.887× | -3.1 | 0.060 | 7/43 (A498, LoVo, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11901. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-1 (line)]] | wt | 449 | 0 | 22 (10 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.104× (z -20.0) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.126× (z -19.1) |
| [[HOP62 (line)]] | alt | 41.8 | 14 | 3 (1 ⚠) | [[Clobetasol propionate (drug)]] 0.05 µM 5.35× (z +12.3) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.278× (z -9.4) |
| [[LoVo (line)]] | wt | 50.6 | 8 (1 ⚠) | 4 (3 ⚠) | [[Binimetinib (drug)]] 5 µM 3.16× (z +9.6) | [[Dinaciclib (drug)]] 0.05 µM 0.105× (z -15.8) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.320× (z -8.6) |
| [[J82 (line)]] | alt | 77.7 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.274× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change · without an alert: [[Riluzole hydrochloride (drug)]] 5 µM 0.526× (z -9.0) |
| [[A-172 (line)]] | wt | 41.7 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.60× (z +13.7) | [[Dinaciclib (drug)]] 0.5 µM 0.263× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change |
| [[A498 (line)]] | wt | 77.4 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.25× (z +11.4) | [[Homoharringtonine (drug)]] 5 µM 0.418× (z -12.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 18.1 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.48× (z +11.9) | [[Homoharringtonine (drug)]] 5 µM 0.368× (z -9.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HepG2_C3A (line)]] | wt | 8.55 | 0 | 2 | — | [[Vismodegib (drug)]] 0.05 µM 0.0645× (z -9.4) |
| [[KATO III (line)]] | alt | 42.8 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.117× (z -14.3) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.275× (z -8.6) |
| [[NCI-H2030 (line)]] | alt | 15.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.172× (z -10.1) ⚠ toxic; transcription drop · without an alert: [[Apalutamide (drug)]] 0.05 µM 0.189× (z -9.5) |
| [[NCI-H460 (line)]] | wt | 7.75 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.36× (z +14.0) | — |
| [[RKO (line)]] | wt | 18.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.97× (z +11.2) | — |
| [[SW1417 (line)]] | alt | 33.1 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.26× (z +9.1) | [[Dinaciclib (drug)]] 0.5 µM 0.336× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change |
| [[SW48 (line)]] | wt | 21.0 | 0 | 2 | — | [[Epirubicin (hydrochloride) (drug)]] 0.05 µM 0.112× (z -9.1) |
| [[SW480 (line)]] | alt | 32.9 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.31× (z +11.1) | [[Niclosamide (olamine) (drug)]] 5 µM 0.392× (z -8.5) ⚠ toxic; cell-cycle shift, explains ~17% of this change |
| [[A549 (line)]] | wt | 12.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.64× (z +9.9) | — |
| [[C32 (line)]] | wt | 21.0 | 1 | 0 | [[Auranofin (drug)]] 5 µM 7.22× (z +10.7) | — |
| [[CFPAC-1 (line)]] | alt | 17.7 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.205× (z -11.5) ⚠ transcription drop; cell-cycle shift, explains ~76% of this change |
| [[HCT15 (line)]] | alt | 30.5 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.219× (z -8.6) ⚠ toxic; cell-cycle shift, explains ~17% of this change |
| [[HEC-1-A (line)]] | alt | 43.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.03× (z +8.8) | — |
| [[Hs 766T (line)]] | wt | 15.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0993× (z -9.9) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 9.16 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.52× (z +9.9) | — |
| [[NCI-H2347 (line)]] | alt | 9.81 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.68× (z +10.7) | — |
| [[Panc 03.27 (line)]] | alt | 14.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.19× (z +8.8) | — |
| [[RPMI-7951 (line)]] | alt | 13.4 | 0 | 1 | — | [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.5 µM 0.141× (z -9.0) |
| [[SHP-77 (line)]] | alt | 31.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.271× (z -9.4) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 32.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.157× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change |
| [[A-427 (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.96 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 6.56 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 41.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 35.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 27.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.63 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 8.31 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.10 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 5.18 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 46.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 45.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 22.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11901), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 11 of them with an alert (⚠; 10 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RIPOR2]] | +0.48 | +0.51 / +0.45 | both halves | 3e-05 |  |
| [[SLC44A1]] | +0.48 | +0.44 / +0.50 | both halves | 3e-05 |  |
| [[RTN4RL1]] | +0.47 | +0.38 / +0.51 | both halves | 6e-05 |  |
| [[ACSL1]] | +0.47 | +0.35 / +0.52 | both halves | 1e-04 |  |
| [[MACIR]] | +0.46 | +0.36 / +0.48 | both halves | 9e-05 |  |
| [[PDLIM1]] | +0.46 | +0.41 / +0.44 | both halves | 4e-05 |  |
| [[SLC19A2]] | +0.45 | +0.41 / +0.46 | both halves | 4e-05 |  |
| [[TBC1D1]] | +0.45 | +0.30 / +0.50 | both halves | 2e-04 |  |
| [[TMEM131L]] | +0.44 | +0.34 / +0.53 | both halves | 1e-04 |  |
| [[LTBP1]] | +0.44 | +0.33 / +0.46 | both halves | 1e-04 | pathway: HALLMARK_UV_RESPONSE_DN |
| [[NPTX2]] | +0.44 | +0.39 / +0.48 | both halves | 5e-05 |  |
| [[GLUL]] | +0.44 | +0.48 / +0.33 | both halves | 1e-04 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[JPX]] | -0.42 | -0.28 / -0.44 | both halves | 3e-04 |  |
| [[STEAP1B-AS1]] | -0.42 | -0.38 / -0.44 | both halves | 7e-05 |  |
| [[TRBC2]] | -0.38 | -0.31 / -0.37 | both halves | 2e-04 |  |
| [[RAD54L2]] | -0.37 | -0.25 / -0.28 | both halves | 4e-04 |  |
| [[VPS45]] | -0.37 | -0.27 / -0.34 | both halves | 3e-04 |  |
| [[BBS1]] | -0.36 | -0.12 / -0.42 | ⚠ not reproduced | 0.002 |  |
| [[ZNF839]] | -0.36 | -0.18 / -0.41 | ⚠ not reproduced | 1e-03 |  |
| [[CHMP6]] | -0.35 | -0.19 / -0.41 | ⚠ not reproduced | 8e-04 |  |
| [[CREM]] | -0.35 | -0.35 / -0.35 | both halves | 1e-04 |  |
| [[ARMC9]] | -0.35 | -0.37 / -0.34 | both halves | 1e-04 |  |
| [[TP73-AS1]] | -0.35 | -0.26 / -0.35 | both halves | 3e-04 |  |
| [[ANXA10]] | -0.35 | -0.25 / -0.39 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRUNE2]] | B | PRUNE2 activity raises GCNT1's level | lines that do not express PRUNE2 (30) vs lines expressing it (20) | 2.56× lower at baseline in the lines without PRUNE2 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGF13, SSX1, UTY |
| [[TRBC2]] | B | TRBC2 activity raises GCNT1's level | lines that do not express TRBC2 (39) vs lines expressing it (11) | 1.35× lower at baseline in the lines without TRBC2 | 0.032 | ⚠ within organs, on part of the lines; also absent: PIGR, MUC6, PSG1 |
| [[SRPX]] | B | SRPX activity raises GCNT1's level | lines that do not express SRPX (22) vs lines expressing it (28) | 1.39× lower at baseline in the lines without SRPX | 0.062 | ⚠ within organs, on part of the lines; also absent: COL15A1, ARHGEF6, ENSG00000230647 |
| [[LOX]] | B | LOX activity raises GCNT1's level | lines that do not express LOX (31) vs lines expressing it (19) | 1.41× lower at baseline in the lines without LOX | 0.068 | ⚠ within organs, on part of the lines; also absent: C5orf46, RRAD, LINC01411 |
| [[CCBE1]] | B | CCBE1 activity raises GCNT1's level | lines that do not express CCBE1 (28) vs lines expressing it (22) | 1.24× lower at baseline in the lines without CCBE1 | 0.068 | ⚠ within organs, on part of the lines; also absent: EDNRA, IL7R, EFEMP1 |
| [[SLC1A1]] | B | SLC1A1 activity raises GCNT1's level | lines that do not express SLC1A1 (11) vs lines expressing it (39) | 2.19× lower at baseline in the lines without SLC1A1 | 0.077 | ⚠ within organs, on part of the lines; also absent: UST, HLA-F; maybe low, not absent |
| [[ZNF385B]] | B | ZNF385B activity raises GCNT1's level | lines that do not express ZNF385B (19) vs lines expressing it (31) | 1.42× lower at baseline in the lines without ZNF385B | 0.083 | ⚠ within organs, on part of the lines; also absent: DTNA, CFI, CYGB; maybe low, not absent |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GLUL]] | B | GCNT1 activity raises GLUL's level | lines that do not express GCNT1 (5) vs lines expressing it (45) | 4.78× lower at baseline in the lines without GCNT1 | 0.034 | ⚠ within organs, on part of the lines; also absent: ANKH, MLLT3, TLE4; maybe low, not absent |
| [[RTN4RL1]] | B | GCNT1 activity lowers RTN4RL1's level | lines that do not express GCNT1 (5) vs lines expressing it (45) | 2.64× higher at baseline in the lines without GCNT1 | 0.050 | ⚠ within organs, on part of the lines; also absent: ANKH, MLLT3, TLE4; maybe low, not absent |
| [[CCBE1]] | B | GCNT1 activity raises CCBE1's level | lines that do not express GCNT1 (5) vs lines expressing it (45) | 3.55× lower at baseline in the lines without GCNT1 | 0.073 | ⚠ within organs, on part of the lines; also absent: ANKH, MLLT3, TLE4; maybe low, not absent |

## Where it sits

- **Module**: [[Module 106]]; 44 genes; every member is in the + arm (projection on the module's main direction 0.442). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (27.5, 19.9); signed map (19.9, 29.6). **Vector** length 79.6, 15.6% of its response variance represented; |z| ≥ 3 in 1,462 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.0 | +16.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.4 | +11.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.2 | +18.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.2 | +2.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +2.1 | +0.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.1 | +3.4 |
|  | [[Betamethasone dipropionate (drug)]] 0.05 µM |  | +2.0 | +2.6 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +2.0 | +0.4 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | -2.1 | -1.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | +0.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -0.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | -0.9 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.4 | -2.1 |
|  | [[Vilanterol (drug)]] 5 µM |  | -1.3 | -0.9 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -1.3 | -0.4 |
|  | [[Amsacrine (drug)]] 5 µM |  | -1.2 | -3.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.1 | -1.8 |
|  | [[Pentamidine (isethionate) (drug)]] 5 µM |  | -1.1 | +0.4 |

## What is on record

|  |  |
|---|---|
| Name | glucosaminyl (N-acetyl) transferase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q21.13 — chr9:76,419,850-76,651,203 (+) |
| Ensembl biotype | protein_coding |
| Also known as | C2GNT, NAGCT2; previously NACGT2 |
| Gene groups (HGNC) | Glucosaminyl (N-acetyl) transferases/xylosyltransferases |
| Hallmark sets | ALLOGRAFT_REJECTION, UV_RESPONSE_DN |
| Reactome | 2 pathways, smallest: O-linked glycosylation of mucins; O-linked glycosylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q02742](https://www.uniprot.org/uniprotkb/Q02742) (Beta-1,3-galactosyl-O-glycosyl-glycoprotein beta-1,6-N-acetylglucosaminyltransferase):

> Glycosyltransferase that catalyzes the transfer of an N-acetylglucosamine (GlcNAc) moiety in beta1-6 linkage from UDP-GlcNAc onto mucin-type core 1 O-glycan to form the branched mucin-type core 2 O-glycan. The catalysis is metal ion-independent and occurs with inversion of the anomeric configuration of sugar donor (By similarity). Selectively involved in synthesis of mucin-type core 2 O-glycans that serve as scaffolds for the display of selectin ligand sialyl Lewis X epitope by myeloid cells, …

**Summary**, from NCBI Gene [2650](https://www.ncbi.nlm.nih.gov/gene/2650):

> This gene is a member of the beta-1,6-N-acetylglucosaminyltransferase gene family. It is essential to the formation of Gal beta 1-3(GlcNAc beta 1-6)GalNAc structures and the core 2 O-glycan branch. The gene coding this enzyme was originally mapped to 9q21, but was later localized to 9q13. Multiple alternatively spliced variants, encoding the same protein, have been identified. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:4203](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4203) · Entrez [2650](https://www.ncbi.nlm.nih.gov/gene/2650) · UniProt [Q02742](https://www.uniprot.org/uniprotkb/Q02742) · Ensembl [ENSG00000187210](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000187210)

## Data

Gene col 11901: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11901); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11901, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11901]; `tensor/DDL_lfc|DDL_z.npy` [11901]; `embed/gene_vectors.npy` [11901]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11901 or target_col == 11901). Every well: [[GCNT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GCNT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
