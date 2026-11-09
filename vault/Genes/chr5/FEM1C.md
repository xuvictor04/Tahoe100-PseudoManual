---
symbol: "FEM1C"
type: "gene"
col: 7025
ensembl_id: "ENSG00000145780"
name: "fem-1 homolog C"
location: "5q22.3"
module: 99
arm: "+"
pooled_cpm: 93.8
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 11
n_dd_up_clean: 20
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/099"]
generated_by: "tahoemap"
---

# FEM1C

*fem-1 homolog C* — 5q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (3 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.76× (z +8.3, q 8e-14, up in 46 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.337× (z -12.5, q 3e-33, down in 41 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ponatinib (drug)]] 0.5 µM: 0.710× (z -4.1, q 0.006, down in 32 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ERO1A]] (+0.67, fdr 1e-05), [[INSIG2]] (+0.66, fdr 7e-06), [[HK2]] (+0.66, fdr 7e-06); moves opposite to [[SMARCB1]] (-0.55, fdr 3e-05), [[JPX]] (-0.53, fdr 2e-05), [[ANAPC7]] (-0.52, fdr 4e-05).
> It is in [[Module 099]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → cells under [[Neratinib (drug)]] 0.05 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7025.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.76×** | +8.3 | 8e-14 | 46/49 (LoVo, A-427, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.77×** | +6.8 | 3e-09 | 41/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.63×** | +5.8 | 1e-06 | 32/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.62×** | +5.8 | 1e-06 | 34/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.38×** | +5.4 | 9e-06 | 33/49 (HT-29, H4, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.50×** | +4.8 | 2e-04 | 31/48 (HT-29, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.99×** | +4.3 | 0.001 | 36/48 (LOX-IMVI, HT-29, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **1.97×** | +4.2 | 0.001 | 31/48 (C32, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.43×** | +4.2 | 0.001 | 29/48 (HT-29, CFPAC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.41×** | +4.1 | 0.003 | 25/48 (NCI-H1573, hTERT-HPNE, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.40×** | +3.8 | 0.008 | 26/48 (HT-29, LoVo, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.37×** | +3.7 | 0.009 | 25/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **1.38×** | +3.7 | 0.009 | 36/49 (LS 180, NCI-H460, …) | top dose only | plate-row cell shift; position effect removed |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.36×** | +3.6 | 0.011 | 25/48 (H4, HT-29, …) | rises with dose |  |
| [[Tomivosertib (drug)]] 5 µM |  | **1.71×** | +3.3 | 0.032 | 23/48 (LS 180, CFPAC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.32×** | +3.3 | 0.032 | 27/48 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.31×** | +3.2 | 0.046 | 23/48 (HT-29, SW480, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7025.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.337×** | -12.5 | 3e-33 | 41/43 (NCI-H2347, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.393×** | -11.2 | 1e-26 | 44/49 (NCI-H2347, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.659×** | -4.6 | 7e-04 | 27/45 (NCI-H2347, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.710×** | -4.1 | 0.006 | 32/48 (NCI-H1792, LS 180, …) | inconsistent across doses |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **0.719×** | -4.0 | 0.009 | 38/48 (PANC-1, HS-578T, …) | inconsistent across doses |  |
| [[Darinaparsin (drug)]] 5 µM |  | **0.808×** | -3.6 | 0.027 | 30/48 (LoVo, COLO 205, …) | rises with dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.741×** | -3.6 | 0.027 | 32/49 (NCI-H661, HS-578T, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.752×** | -3.4 | 0.044 | 26/48 (LOX-IMVI, C-33 A, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.746×** | -3.4 | 0.044 | 25/48 (A-172, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.757×** | -3.3 | 0.048 | 22/48 (CFPAC-1, RKO, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 0.05 µM |  | **0.759×** | -3.3 | 0.048 | 29/48 (LOX-IMVI, SW1417, …) | inconsistent across doses |  |
| [[Carbamazepine (drug)]] 5 µM |  | 0.779× | -3.0 | 0.12 | 23/47 (NCI-H1792, Hs 766T, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7025. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 74.5 | 7 (2 ⚠) | 0 | [[Digitoxin (drug)]] 0.5 µM 3.17× (z +9.7) | — |
| [[NCI-H2347 (line)]] | alt | 230 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.123× (z -22.8) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 83.8 | 6 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 0.05 µM 5.59× (z +12.3) | — |
| [[NCI-H1573 (line)]] | alt | 66.4 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.58× (z +18.3) ⚠ cell-cycle shift, explains ~19% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.06× (z +12.2) | — |
| [[A-172 (line)]] | wt | 102 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.155× (z -16.7) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 100 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 7.03× (z +11.0) | [[Dinaciclib (drug)]] 0.5 µM 0.297× (z -13.1) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 188 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +14.0) ⚠ cell-cycle shift, explains ~19% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.44× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.377× (z -9.5) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 118 | 1 | 2 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 12.9× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.180× (z -13.0) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 191 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.113× (z -17.3) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 140 | 1 | 2 (2 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 2.63× (z +8.7) | [[Dinaciclib (drug)]] 0.5 µM 0.130× (z -13.0) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 81.6 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.21× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.211× (z -10.9) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 127 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.320× (z -9.9) ⚠ cell-cycle shift, explains ~19% of this change |
| [[NCI-H1792 (line)]] | alt | 127 | 1 (1 ⚠) | 2 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 2.94× (z +9.2) ⚠ toxic; transcription drop | [[Dinaciclib (drug)]] 0.5 µM 0.275× (z -11.1) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 90.7 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0877× (z -14.6) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 74.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.249× (z -13.9) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 142 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.176× (z -14.7) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 95.0 | 2 | 0 | [[Vinblastine (sulfate) (drug)]] 5 µM 2.67× (z +11.8) | — |
| [[PANC-1 (line)]] | alt | 46.6 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.39× (z +12.8) | — |
| [[SK-MEL-2 (line)]] | alt | 110 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0834× (z -18.8) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 89.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.174× (z -13.4) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 59.9 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 9.07× (z +9.5) | — |
| [[A549 (line)]] | wt | 54.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.306× (z -8.6) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 65.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.227× (z -13.6) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 58.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.141× (z -12.2) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 134 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.307× (z -9.1) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 87.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.225× (z -9.7) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 86.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.202× (z -12.5) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 119 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.302× (z -9.8) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 69.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.180× (z -13.9) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 68.1 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.54× (z +8.5) ⚠ toxic | — |
| [[SW1417 (line)]] | alt | 87.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.361× (z -8.7) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 108 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 49.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 63.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 109 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 209 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 74.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 83.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 75.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 70.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 82.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 120 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 91.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 65.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 68.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7025), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ERO1A]] | +0.67 | +0.73 / +0.54 | both halves | 1e-05 |  |
| [[INSIG2]] | +0.66 | +0.71 / +0.58 | both halves | 7e-06 |  |
| [[HK2]] | +0.66 | +0.69 / +0.60 | both halves | 7e-06 |  |
| [[PDK1]] | +0.64 | +0.70 / +0.55 | both halves | 1e-05 |  |
| [[EIF4A3]] | +0.64 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[KDM3A]] | +0.63 | +0.68 / +0.53 | both halves | 1e-05 |  |
| [[PIGA]] | +0.61 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[DDIT4]] | +0.61 | +0.71 / +0.49 | both halves | 1e-05 |  |
| [[RAB11FIP5]] | +0.61 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[MXI1]] | +0.60 | +0.68 / +0.47 | both halves | 2e-05 |  |
| [[FAM162A]] | +0.60 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[FAM210A]] | +0.60 | +0.62 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMARCB1]] | -0.55 | -0.45 / -0.51 | both halves | 3e-05 |  |
| [[JPX]] | -0.53 | -0.56 / -0.46 | both halves | 2e-05 |  |
| [[ANAPC7]] | -0.52 | -0.55 / -0.42 | both halves | 4e-05 |  |
| [[GPATCH8]] | -0.51 | -0.53 / -0.49 | both halves | 2e-05 |  |
| [[ZC3H7B]] | -0.51 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[NDUFS1]] | -0.50 | -0.52 / -0.38 | both halves | 7e-05 |  |
| [[SENP1]] | -0.48 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[POGLUT1]] | -0.48 | -0.55 / -0.41 | both halves | 4e-05 |  |
| [[ST7L]] | -0.48 | -0.58 / -0.37 | both halves | 9e-05 |  |
| [[PARVA]] | -0.48 | -0.43 / -0.32 | both halves | 2e-04 |  |
| [[NHLRC2]] | -0.47 | -0.48 / -0.38 | both halves | 7e-05 |  |
| [[ERCC6L2]] | -0.47 | -0.56 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Neratinib (drug)]] 0.05 µM | C | FEM1C's natural level raises the cells' numbers under Neratinib 0.05 µM (protects the cells) | FEM1C's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.66 | 0.352 over the table, 0.078 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 099]] — hypoxia; 48 genes; every member is in the + arm (projection on the module's main direction 0.671). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.3, -15.8); signed map (-35.9, 25.0). **Vector** length 103, 34.8% of its response variance represented; |z| ≥ 3 in 1,129 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *hypoxia* (control, mean cos +0.50 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.2 | +1.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.0 | -0.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.5 | +0.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.3 | +2.4 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +3.9 | -0.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.6 | +5.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +3.4 | +1.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.4 | +4.2 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -7.6 | -3.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | -6.0 | +0.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.7 | +3.7 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.7 | +5.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.6 | +6.8 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -2.3 | -3.6 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -1.8 | -0.6 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | -1.8 | -2.6 |
|  | [[Rapamycin (drug)]] 5 µM |  | -1.7 | -1.7 |
|  | [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | -1.7 | -4.0 |

## What is on record

|  |  |
|---|---|
| Name | fem-1 homolog C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q22.3 — chr5:115,520,908-115,544,775 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1785, EUROIMAGE686608, EUROIMAGE783647, FEM1A |
| Gene groups (HGNC) | Ankyrin repeat domain containing |
| Reactome | 1 pathways, smallest: Neddylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96JP0](https://www.uniprot.org/uniprotkb/Q96JP0) (Protein fem-1 homolog C):

> Substrate-recognition component of a Cul2-RING (CRL2) E3 ubiquitin-protein ligase complex of the DesCEND (destruction via C-end degrons) pathway, which recognizes a C-degron located at the extreme C terminus of target proteins, leading to their ubiquitination and degradation. The C-degron recognized by the DesCEND pathway is usually a motif of less than ten residues and can be present in full-length proteins, truncated proteins or proteolytically cleaved forms. The CRL2(FEM1C) complex …

**Summary**, from NCBI Gene [56929](https://www.ncbi.nlm.nih.gov/gene/56929):

> Enables ubiquitin-like ligase-substrate adaptor activity. Involved in ubiquitin-dependent protein catabolic process via the C-end degron rule pathway. Located in nucleoplasm. Part of Cul2-RING ubiquitin ligase complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:16933](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16933) · Entrez [56929](https://www.ncbi.nlm.nih.gov/gene/56929) · UniProt [Q96JP0](https://www.uniprot.org/uniprotkb/Q96JP0) · Ensembl [ENSG00000145780](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000145780)

## Data

Gene col 7025: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7025); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7025, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7025]; `tensor/DDL_lfc|DDL_z.npy` [7025]; `embed/gene_vectors.npy` [7025]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7025 or target_col == 7025). Every well: [[FEM1C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FEM1C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
