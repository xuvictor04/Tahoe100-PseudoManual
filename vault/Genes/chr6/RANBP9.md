---
symbol: "RANBP9"
type: "gene"
col: 196
ensembl_id: "ENSG00000010017"
name: "RAN binding protein 9"
location: "6p23"
module: 163
arm: "+"
pooled_cpm: 122.51
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 13
n_dd_up_clean: 6
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/163"]
generated_by: "tahoemap"
---

# RANBP9

*RAN binding protein 9* — 6p23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 1.64× (z +9.6, q 7e-19, up in 38 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.55× (z +8.7, q 5e-16, up in 36 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.543× (z -12.3, q 4e-32, down in 41 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.660× (z -8.4, q 1e-14, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ABHD12]] (+0.70, fdr 7e-06), [[CDC42SE2]] (+0.67, fdr 7e-06), [[CNOT6L]] (+0.64, fdr 7e-06); moves opposite to [[MYSM1]] (-0.61, fdr 2e-05), [[CRYM]] (-0.60, fdr 1e-05), [[SBF2-AS1]] (-0.59, fdr 1e-05).
> It is in [[Module 163]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 196.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.64×** | +9.6 | 7e-19 | 38/47 (PANC-1, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.55×** | +8.7 | 5e-16 | 36/48 (PANC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.54×** | +8.7 | 5e-16 | 33/48 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.31×** | +5.4 | 9e-06 | 27/48 (PANC-1, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.25×** | +4.5 | 7e-04 | 24/48 (PANC-1, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.50×** | +4.2 | 0.002 | 27/49 (SW480, KATO III, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.21×** | +3.8 | 0.012 | 21/48 (C32, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.42×** | +3.7 | 0.016 | 26/48 (SW480, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 8 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 196.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.543×** | -12.3 | 4e-32 | 41/49 (NCI-H1573, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.548×** | -11.7 | 5e-29 | 36/44 (C-33 A, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.660×** | -8.4 | 1e-14 | 38/48 (SW480, HT-29, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.648×** | -8.1 | 9e-14 | 36/45 (KATO III, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.684×** | -7.4 | 2e-11 | 37/47 (RKO, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.714×** | -6.8 | 9e-10 | 31/48 (SW48, SW480, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.789×** | -6.8 | 9e-10 | 32/48 (A-427, SNU-1, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.719×** | -6.7 | 2e-09 | 31/48 (SW48, SW480, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.719×** | -6.2 | 3e-08 | 31/48 (SW48, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.738×** | -6.2 | 4e-08 | 28/48 (A-172, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.823×** | -5.6 | 1e-06 | 26/48 (NCI-H2347, A-427, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.761×** | -5.5 | 2e-06 | 32/48 (A-172, NCI-H1573, …) | all doses, flat |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | 0.833× | -5.2 | 7e-06 | 22/49 (NCI-H2347, SW480, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.792×** | -4.7 | 1e-04 | 30/48 (SW1417, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~6% here) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | 0.886× | -3.5 | 0.018 | 6/48 (CFPAC-1, NCI-H2347, …) | top dose only |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | 0.863× | -3.0 | 0.093 | 13/47 (SNU-1, NCI-H661, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 196. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW48 (line)]] | wt | 308 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.290× (z -15.8) ⚠ cell-cycle shift, explains ~8% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.237× (z -13.0) |
| [[SW480 (line)]] | alt | 157 | 2 (1 ⚠) | 5 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.91× (z +10.3) | [[Auranofin (drug)]] 5 µM 0.385× (z -15.2) |
| [[NCI-H2347 (line)]] | alt | 167 | 0 | 6 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.482× (z -12.6) ⚠ cell-cycle shift, explains ~10% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.577× (z -9.5) |
| [[A-172 (line)]] | wt | 78.4 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.482× (z -12.3) ⚠ cell-cycle shift, explains ~8% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.413× (z -9.9) |
| [[NCI-H1573 (line)]] | alt | 90.7 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.222× (z -17.2) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.469× (z -8.7) |
| [[PANC-1 (line)]] | alt | 104 | 5 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.15× (z +19.7) | — |
| [[CFPAC-1 (line)]] | alt | 127 | 0 | 4 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.362× (z -11.5) ⚠ toxic |
| [[J82 (line)]] | alt | 175 | 1 (1 ⚠) | 3 (3 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.32× (z +11.8) ⚠ toxic | [[Dinaciclib (drug)]] 5 µM 0.474× (z -10.6) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 90.2 | 3 (2 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.14× (z +9.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.09× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.419× (z -10.4) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 104 | 1 (1 ⚠) | 2 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.51× (z +10.4) ⚠ toxic | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.521× (z -10.9) ⚠ cell-cycle shift, explains ~10% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.480× (z -8.6) |
| [[HT-29 (line)]] | alt | 145 | 0 | 3 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.375× (z -13.0) |
| [[KATO III (line)]] | alt | 139 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.28× (z +11.1) | [[Dinaciclib (drug)]] 0.05 µM 0.364× (z -12.6) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 140 | 1 (1 ⚠) | 2 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.32× (z +10.8) ⚠ toxic | [[Auranofin (drug)]] 5 µM 0.387× (z -12.6) |
| [[NCI-H2030 (line)]] | alt | 190 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.304× (z -12.0) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 139 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.294× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.438× (z -9.2) |
| [[SHP-77 (line)]] | alt | 119 | 1 | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.16× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.343× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.469× (z -8.5) |
| [[SW1417 (line)]] | alt | 174 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.361× (z -11.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.480× (z -9.1) |
| [[A-427 (line)]] | wt | 103 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.561× (z -10.2) ⚠ cell-cycle shift, explains ~8% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.603× (z -8.9) |
| [[HEC-1-A (line)]] | alt | 106 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.330× (z -12.4) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 160 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.09× (z +8.8) | [[Dinaciclib (drug)]] 0.5 µM 0.430× (z -10.2) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 86.7 | 1 (1 ⚠) | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 1.86× (z +8.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.401× (z -12.7) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 117 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.232× (z -15.4) ⚠ toxic; transcription drop · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.552× (z -8.9) |
| [[AN3 CA (line)]] | alt | 211 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.292× (z -9.0) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 107 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.379× (z -11.0) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 135 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.383× (z -10.2) |
| [[C-33 A (line)]] | alt | 110 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.104× (z -20.9) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 80.4 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.00× (z +9.0) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 206 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.387× (z -9.2) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 132 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.28× (z +8.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 92.8 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.48× (z +9.8) ⚠ toxic | — |
| [[NCI-H1792 (line)]] | alt | 104 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.506× (z -10.7) ⚠ cell-cycle shift, explains ~10% of this change |
| [[RKO (line)]] | wt | 101 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.342× (z -12.4) ⚠ toxic |
| [[RPMI-7951 (line)]] | alt | 95.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.313× (z -10.9) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 72.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 75.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 84.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 120 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 127 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 96.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 124 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 82.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 127 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 174 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 145 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 80.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 148 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 137 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 196), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABHD12]] | +0.70 | +0.78 / +0.60 | both halves | 7e-06 |  |
| [[CDC42SE2]] | +0.67 | +0.70 / +0.59 | both halves | 7e-06 |  |
| [[CNOT6L]] | +0.64 | +0.68 / +0.58 | both halves | 7e-06 |  |
| [[UBE2G1]] | +0.64 | +0.72 / +0.52 | both halves | 1e-05 |  |
| [[LRRC1]] | +0.63 | +0.57 / +0.64 | both halves | 1e-05 |  |
| [[RNF38]] | +0.62 | +0.74 / +0.44 | both halves | 3e-05 |  |
| [[PPP3R1]] | +0.61 | +0.71 / +0.53 | both halves | 1e-05 |  |
| [[STRN]] | +0.60 | +0.68 / +0.55 | both halves | 1e-05 |  |
| [[TANC1]] | +0.60 | +0.65 / +0.50 | both halves | 1e-05 |  |
| [[PPM1B]] | +0.59 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[CMC2]] | +0.59 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[DPY19L1]] | +0.58 | +0.65 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYSM1]] | -0.61 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[CRYM]] | -0.60 | -0.60 / -0.56 | both halves | 1e-05 |  |
| [[SBF2-AS1]] | -0.59 | -0.62 / -0.56 | both halves | 1e-05 |  |
| [[HDAC9]] | -0.56 | -0.64 / -0.47 | both halves | 2e-05 |  |
| [[MSANTD3-TMEFF1]] | -0.55 | -0.61 / -0.39 | both halves | 5e-05 |  |
| [[RABL3]] | -0.55 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[FCF1]] | -0.55 | -0.64 / -0.43 | both halves | 3e-05 |  |
| [[LINC00944]] | -0.53 | -0.59 / -0.44 | both halves | 3e-05 |  |
| [[ALOXE3]] | -0.53 | -0.64 / -0.33 | both halves | 1e-04 |  |
| [[CAVIN4]] | -0.52 | -0.58 / -0.41 | both halves | 4e-05 |  |
| [[ZNF701]] | -0.52 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[ZBTB21]] | -0.52 | -0.61 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 163]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.789). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.53; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-8.9, -5.5); signed map (-19.2, 18.3). **Vector** length 107, 33.7% of its response variance represented; |z| ≥ 3 in 1,135 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +6.2 | +9.6 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.3 | +2.3 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.5 | -0.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.9 | -0.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.8 | +1.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.5 | +2.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.4 | -0.2 |
|  | [[Berbamine (drug)]] 5 µM |  | +1.7 | +1.5 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +1.6 | +0.9 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -8.4 | -6.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.9 | -8.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.8 | -5.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.8 | -6.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~8% of this change | -5.1 | -2.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.1 | -6.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.7 | -2.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.9 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | RAN binding protein 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p23 — chr6:13,621,498-13,711,835 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RanBPM |
| Gene groups (HGNC) | CTLH complex subunits |
| Hallmark sets | MITOTIC_SPINDLE |
| Reactome | 12 pathways, smallest: MET activates RAS signaling; Regulation of pyruvate metabolism; Pyruvate metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96S59](https://www.uniprot.org/uniprotkb/Q96S59) (Ran-binding protein 9):

> May act as scaffolding protein, and as adapter protein to couple membrane receptors to intracellular signaling pathways (Probable). Acts as a mediator of cell spreading and actin cytoskeleton rearrangement. Core component of the CTLH E3 ubiquitin-protein ligase complex that selectively accepts ubiquitin from UBE2H and mediates ubiquitination and subsequent proteasomal degradation of the transcription factor HBP1. May be involved in signaling of ITGB2/LFA-1 and other integrins. Enhances HGF-MET …

**Summary**, from NCBI Gene [10048](https://www.ncbi.nlm.nih.gov/gene/10048):

> This gene encodes a protein that binds RAN, a small GTP binding protein belonging to the RAS superfamily that is essential for the translocation of RNA and proteins through the nuclear pore complex. The protein encoded by this gene has also been shown to interact with several other proteins, including met proto-oncogene, homeodomain interacting protein kinase 2, androgen receptor, and cyclin-dependent kinase 11. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:13727](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13727) · Entrez [10048](https://www.ncbi.nlm.nih.gov/gene/10048) · UniProt [Q96S59](https://www.uniprot.org/uniprotkb/Q96S59) · Ensembl [ENSG00000010017](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000010017)

## Data

Gene col 196: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 196); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 196, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 196]; `tensor/DDL_lfc|DDL_z.npy` [196]; `embed/gene_vectors.npy` [196]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 196 or target_col == 196). Every well: [[RANBP9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RANBP9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
