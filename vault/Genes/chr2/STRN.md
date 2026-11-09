---
symbol: "STRN"
type: "gene"
col: 3721
ensembl_id: "ENSG00000115808"
name: "striatin"
location: "2p22.2"
module: 163
arm: "+"
pooled_cpm: 132.2
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 13
n_dd_up_clean: 6
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/163"]
generated_by: "tahoemap"
---

# STRN

*striatin* — 2p22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.57× (z +10.7, q 4e-24, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.609× (z -16.5, q 0e+00, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RNF38]] (+0.74, fdr 7e-06), [[SERAC1]] (+0.72, fdr 2e-05), [[SEC11A]] (+0.71, fdr 1e-05); moves opposite to [[RBM23]] (-0.71, fdr 3e-05), [[ZNF764]] (-0.71, fdr 2e-04), [[FIZ1]] (-0.70, fdr 1e-04).
> It is in [[Module 163]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3721.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.57×** | +10.7 | 4e-24 | 45/48 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.51×** | +9.8 | 2e-20 | 41/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.43×** | +8.4 | 6e-15 | 37/48 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.37×** | +7.4 | 1e-11 | 27/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.36×** | +7.3 | 4e-11 | 30/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.32×** | +6.3 | 3e-08 | 36/47 (LoVo, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **1.26×** | +5.5 | 3e-06 | 27/48 (C32, LOX-IMVI, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.24×** | +5.2 | 2e-05 | 28/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.19× | +4.2 | 0.001 | 18/48 (PANC-1, LoVo, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.6 | 0.017 | 18/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +3.4 | 0.034 | 16/48 (LoVo, SW1417, …) | all doses, stronger at high dose |  |
| [[Erlotinib (drug)]] 0.05 µM |  | 1.16× | +3.3 | 0.044 | 12/48 (NCI-H2030, LS 180, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **1.29×** | +3.2 | 0.058 | 16/49 (PANC-1, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | 1.14× | +3.1 | 0.088 | 13/47 (AsPC-1, H4, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 11 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3721.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.609×** | -16.5 | 0e+00 | 40/48 (AsPC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.550×** | -13.6 | 2e-39 | 41/44 (NCI-H1573, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.629×** | -10.9 | 1e-25 | 38/48 (NCI-H1573, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.643×** | -10.4 | 4e-23 | 38/49 (A-427, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.705×** | -7.6 | 3e-12 | 31/45 (A-172, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.761×** | -6.2 | 7e-08 | 30/47 (HepG2/C3A, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.855× | -5.2 | 2e-05 | 22/49 (A549, NCI-H2347, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.813×** | -4.9 | 8e-05 | 27/48 (A-172, MIA PaCa-2, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.812×** | -4.7 | 2e-04 | 26/48 (A498, CFPAC-1, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.700×** | -4.4 | 7e-04 | 24/49 (HOP62, A-172, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.718×** | -4.1 | 0.002 | 21/38 (NCI-H2347, SW 900, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.842× | -4.0 | 0.003 | 20/48 (NCI-H2347, AsPC-1, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.725×** | -3.9 | 0.003 | 26/48 (AsPC-1, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.850× | -3.8 | 0.006 | 17/48 (A-427, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[venetoclax (drug)]] 5 µM |  | **0.737×** | -3.7 | 0.007 | 23/48 (Hs 766T, HCT15, …) | top dose only | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.894× | -3.7 | 0.008 | 13/48 (A-172, HOP62, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.754×** | -3.5 | 0.016 | 20/48 (LoVo, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3721. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 120 | 9 (4 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.33× (z +14.6) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 2.32× (z +14.6) | [[Dinaciclib (drug)]] 5 µM 0.502× (z -11.4) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 222 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -24.7) |
| [[CFPAC-1 (line)]] | alt | 144 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.424× (z -15.7) |
| [[NCI-H2347 (line)]] | alt | 144 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.287× (z -16.2) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 129 | 5 (2 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.05× (z +12.2) | [[Homoharringtonine (drug)]] 5 µM 0.574× (z -13.3) |
| [[SW480 (line)]] | alt | 124 | 4 (1 ⚠) | 1 | [[Digitoxin (drug)]] 5 µM 1.88× (z +11.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.85× (z +11.1) | [[Homoharringtonine (drug)]] 0.5 µM 0.608× (z -9.0) |
| [[A-427 (line)]] | wt | 213 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.302× (z -20.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.521× (z -15.4) |
| [[A498 (line)]] | wt | 141 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.513× (z -15.0) |
| [[HOP62 (line)]] | alt | 137 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.415× (z -18.7) |
| [[NCI-H1573 (line)]] | alt | 121 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.189× (z -24.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.356× (z -22.3) |
| [[A-172 (line)]] | wt | 161 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.351× (z -15.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.576× (z -8.8) |
| [[A549 (line)]] | wt | 169 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.543× (z -14.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.581× (z -12.7) |
| [[C32 (line)]] | wt | 98.9 | 1 | 2 | [[PH-797804 (drug)]] 5 µM 4.04× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.612× (z -8.7) |
| [[hTERT-HPNE (line)]] | wt | 120 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.281× (z -14.1) |
| [[LOX-IMVI (line)]] | wt | 147 | 1 | 2 | [[Panobinostat (drug)]] 5 µM 2.03× (z +10.2) | [[Homoharringtonine (drug)]] 5 µM 0.445× (z -16.5) |
| [[MIA PaCa-2 (line)]] | alt | 137 | 1 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.04× (z +9.0) | [[Homoharringtonine (drug)]] 5 µM 0.451× (z -14.3) |
| [[NCI-H23 (line)]] | alt | 197 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.86× (z +9.9) | [[Dinaciclib (drug)]] 0.5 µM 0.578× (z -8.8) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 104 | 3 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.40× (z +10.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.25× (z +9.7) | — |
| [[C-33 A (line)]] | alt | 127 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.278× (z -14.1) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 127 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.266× (z -14.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.342× (z -11.9) |
| [[HEC-1-A (line)]] | alt | 142 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.452× (z -13.2) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 102 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.196× (z -16.1) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.468× (z -11.0) |
| [[KATO III (line)]] | alt | 132 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.576× (z -10.5) |
| [[LoVo (line)]] | wt | 108 | 2 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.08× (z +10.5) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 5 µM 1.93× (z +9.8) | — |
| [[NCI-H2030 (line)]] | alt | 139 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.436× (z -10.8) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 146 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.467× (z -9.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.507× (z -9.1) |
| [[SHP-77 (line)]] | alt | 117 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.06× (z +9.1) | — |
| [[SNU-1 (line)]] | wt | 102 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.132× (z -17.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.406× (z -11.4) |
| [[SW 1088 (line)]] | alt | 114 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0833× (z -11.3) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 118 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.225× (z -15.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.384× (z -14.9) |
| [[AN3 CA (line)]] | alt | 146 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.293× (z -9.0) |
| [[Hs 766T (line)]] | wt | 112 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.619× (z -8.5) |
| [[HS-578T (line)]] | alt | 132 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.434× (z -13.2) |
| [[HT-29 (line)]] | alt | 125 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.580× (z -10.7) |
| [[J82 (line)]] | alt | 86.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.451× (z -13.9) |
| [[LS 180 (line)]] | wt | 131 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.478× (z -9.2) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 97.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.582× (z -9.3) |
| [[SK-MEL-2 (line)]] | alt | 113 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.464× (z -9.4) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 121 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.477× (z -12.4) |
| [[SW48 (line)]] | wt | 107 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.213× (z -13.6) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 94.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 59.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 146 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 174 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 144 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 153 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 142 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3721), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*43 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF38]] | +0.74 | +0.81 / +0.61 | both halves | 7e-06 |  |
| [[SERAC1]] | +0.72 | +0.73 / +0.47 | both halves | 2e-05 |  |
| [[SEC11A]] | +0.71 | +0.76 / +0.51 | both halves | 1e-05 |  |
| [[SLC9A6]] | +0.71 | +0.71 / +0.46 | both halves | 3e-05 |  |
| [[ILRUN]] | +0.69 | +0.79 / +0.48 | both halves | 2e-05 |  |
| [[GIT1]] | +0.68 | +0.62 / +0.48 | both halves | 2e-05 |  |
| [[CBFA2T2]] | +0.67 | +0.70 / +0.43 | both halves | 3e-05 |  |
| [[GNB2]] | +0.66 | +0.66 / +0.36 | both halves | 1e-04 | same gene group; pathway: ESR-mediated signaling; STRING 525 |
| [[RAP1A]] | +0.66 | +0.70 / +0.50 | both halves | 1e-05 |  |
| [[NTAN1]] | +0.66 | +0.71 / +0.50 | both halves | 1e-05 |  |
| [[GET1]] | +0.65 | +0.71 / +0.40 | both halves | 4e-05 |  |
| [[HDAC3]] | +0.65 | +0.71 / +0.40 | both halves | 4e-05 | pathway: Intracellular signaling by second messengers |

## Genes that move opposite

*57 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBM23]] | -0.71 | -0.74 / -0.44 | both halves | 3e-05 |  |
| [[ZNF764]] | -0.71 | -0.77 / -0.30 | both halves | 2e-04 |  |
| [[FIZ1]] | -0.70 | -0.72 / -0.35 | both halves | 1e-04 |  |
| [[NAIF1]] | -0.69 | -0.77 / -0.31 | both halves | 2e-04 |  |
| [[INTS14]] | -0.67 | -0.72 / -0.31 | both halves | 2e-04 |  |
| [[CFLAR-AS1]] | -0.67 | -0.66 / -0.42 | both halves | 4e-05 |  |
| [[GOSR1]] | -0.66 | -0.65 / -0.52 | both halves | 1e-05 |  |
| [[PCBP1-AS1]] | -0.66 | -0.68 / -0.31 | both halves | 2e-04 |  |
| [[RPL7L1]] | -0.65 | -0.76 / -0.44 | both halves | 3e-05 |  |
| [[MYSM1]] | -0.65 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[ZNF268]] | -0.65 | -0.73 / -0.38 | both halves | 7e-05 |  |
| [[UTP3]] | -0.64 | -0.79 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers STRN's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 163]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.754). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.53; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-4.1, -0.5); signed map (-39.7, -1.8). **Vector** length 123, 39.2% of its response variance represented; |z| ≥ 3 in 1,106 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +7.7 | +9.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | +7.2 | +10.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +6.8 | +8.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +6.3 | +6.3 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.8 | +3.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.8 | +3.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.3 | +4.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.7 | +1.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.4 | +1.6 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.0 | +2.7 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -14.2 | -16.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -12.5 | -10.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | -7.7 | -4.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | -7.7 | -4.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.2 | -4.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -5.0 | +1.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.9 | -3.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.5 | -4.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.5 | -3.8 |
|  | [[EX229 (drug)]] 5 µM |  | -3.4 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | striatin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p22.2 — chr2:36,837,698-36,966,536 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PPP2R6A, STRN1 |
| Gene groups (HGNC) | WD repeat domain containing; Protein phosphatase 2 regulatory subunits; STRIPAK complex |
| Hallmark sets | KRAS_SIGNALING_UP |
| Reactome | 15 pathways, smallest: Signaling by cytosolic PDGFRA and PDGFRB fusion proteins; ALK mutants bind TKIs; Signaling by PDGFR in disease |
| Matched by | ensembl_id |

**Function**, from UniProt [O43815](https://www.uniprot.org/uniprotkb/O43815) (Striatin):

> Calmodulin-binding scaffolding protein which is the center of the striatin-interacting phosphatase and kinase (STRIPAK) complexes. STRIPAK complexes have critical roles in protein (de)phosphorylation and are regulators of multiple signaling pathways including Hippo, MAPK, nuclear receptor and cytoskeleton remodeling. Different types of STRIPAK complexes are involved in a variety of biological processes such as cell growth, differentiation, apoptosis, metabolism and immune regulation (Probable).

**Summary**, from NCBI Gene [6801](https://www.ncbi.nlm.nih.gov/gene/6801):

> Enables armadillo repeat domain binding activity; nuclear estrogen receptor binding activity; and protein phosphatase 2A binding activity. Involved in Wnt signaling pathway and negative regulation of cell population proliferation. Located in bicellular tight junction. Part of FAR/SIN/STRIPAK complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:11424](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11424) · Entrez [6801](https://www.ncbi.nlm.nih.gov/gene/6801) · UniProt [O43815](https://www.uniprot.org/uniprotkb/O43815) · Ensembl [ENSG00000115808](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115808)

## Data

Gene col 3721: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3721); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3721, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3721]; `tensor/DDL_lfc|DDL_z.npy` [3721]; `embed/gene_vectors.npy` [3721]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3721 or target_col == 3721). Every well: [[STRN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STRN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
