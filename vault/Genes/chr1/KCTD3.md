---
symbol: "KCTD3"
type: "gene"
col: 5885
ensembl_id: "ENSG00000136636"
name: "potassium channel tetramerization domain containing 3"
location: "1q41"
module: 146
arm: "+"
pooled_cpm: 75.84
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 12
n_dd_up_clean: 6
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 0
direction_downstream: 2
tags: ["gene", "module/146"]
generated_by: "tahoemap"
---

# KCTD3

*potassium channel tetramerization domain containing 3* — 1q41

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[PH-797804 (drug)]] 5 µM: 2.42× (z +9.1, q 6e-17, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.526× (z -12.6, q 2e-33, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HSF2]] (+0.68, fdr 7e-06), [[TNRC6A]] (+0.67, fdr 7e-06), [[VAPA]] (+0.66, fdr 7e-06); moves opposite to [[STK40]] (-0.69, fdr 7e-06), [[GPATCH2L]] (-0.64, fdr 7e-06), [[KCTD5]] (-0.64, fdr 1e-05).
> It sits in the **+** arm of [[Module 146]].
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 2 go from it, the strongest it → [[RPRD2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 6 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5885.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **2.42×** | +9.1 | 6e-17 | 41/48 (PANC-1, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.39×** | +6.2 | 1e-07 | 30/47 (LoVo, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.81×** | +6.1 | 2e-07 | 32/49 (PANC-1, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.30×** | +5.2 | 2e-05 | 28/48 (NCI-H2030, PANC-1, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 1.20× | +5.1 | 5e-05 | 22/48 (AsPC-1, CHP-212, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM |  | **1.61×** | +4.9 | 8e-05 | 27/47 (NCI-H1573, BT-474, …) | top dose only | cell-cycle shift (explains ~18% here); noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.27×** | +4.7 | 2e-04 | 23/48 (C-33 A, SW480, …) | inconsistent across doses | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.24×** | +4.3 | 0.001 | 24/47 (LS 180, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.22×** | +4.0 | 0.004 | 21/48 (PANC-1, NCI-H2030, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.21×** | +3.6 | 0.021 | 21/48 (NCI-H23, RKO, …) | top dose only | composition shift |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.19× | +3.5 | 0.026 | 10/48 (CFPAC-1, SW 900, …) | inconsistent across doses |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.13× | +3.4 | 0.032 | 5/48 (NCI-H460, CHP-212, …) | inconsistent across doses |  |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | 1.19× | +3.4 | 0.032 | 15/48 (HT-29, SK-MEL-2, …) | top dose only |  |
| [[Berberine (chloride hydrate) (drug)]] 0.5 µM |  | 1.18× | +3.2 | 0.049 | 11/49 (SHP-77, SNU-1, …) | inconsistent across doses | position effect removed |
| [[Doxycycline (monohydrate) (drug)]] 5 µM |  | 1.18× | +3.1 | 0.072 | 17/47 (LoVo, HEC-1-A, …) | top dose only |  |
| [[Ipatasertib (drug)]] 5 µM |  | **1.34×** | +3.0 | 0.091 | 7/48 (SW 900, CHP-212, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 1.18× | +3.0 | 0.091 | 9/48 (AsPC-1, MIA PaCa-2, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 7 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5885.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.526×** | -12.6 | 2e-33 | 41/48 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.540×** | -12.1 | 4e-31 | 42/48 (SK-MEL-2, CFPAC-1, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.677×** | -10.8 | 6e-25 | 34/49 (CFPAC-1, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.584×** | -10.5 | 8e-24 | 40/48 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.620×** | -9.4 | 9e-19 | 36/48 (SW480, A498, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.878× | -8.8 | 2e-16 | 4/50 (PANC-1, HT-29, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.726×** | -6.0 | 1e-07 | 25/43 (HEC-1-A, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.756×** | -5.5 | 3e-06 | 29/48 (A498, CFPAC-1, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.786×** | -4.7 | 2e-04 | 26/48 (HEC-1-A, NCI-H2347, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.776×** | -4.6 | 3e-04 | 23/45 (A-427, C32, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.800×** | -4.4 | 7e-04 | 25/48 (CHP-212, A498, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.854× | -4.3 | 7e-04 | 19/48 (A-172, CFPAC-1, …) | top dose only |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.813×** | -4.0 | 0.002 | 22/48 (CFPAC-1, A498, …) | top dose only |  |
| [[Celecoxib (drug)]] 0.5 µM |  | **0.776×** | -3.5 | 0.017 | 14/49 (HepG2/C3A, NCI-H1573, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.843× | -3.3 | 0.033 | 11/49 (PANC-1, NCI-H2030, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 0.5 µM |  | 0.857× | -3.0 | 0.092 | 14/48 (LoVo, SW 900, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5885. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 114 | 0 | 7 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.227× (z -21.9) |
| [[SW480 (line)]] | alt | 67.9 | 1 | 5 | [[PH-797804 (drug)]] 5 µM 3.43× (z +8.6) | [[Panobinostat (drug)]] 5 µM 0.290× (z -16.6) |
| [[A498 (line)]] | wt | 119 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.317× (z -13.7) |
| [[C32 (line)]] | wt | 88.1 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.369× (z -13.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.459× (z -10.3) |
| [[LS 180 (line)]] | wt | 86.2 | 4 (4 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.19× (z +14.2) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 0.5 µM 0.411× (z -8.7) |
| [[NCI-H460 (line)]] | wt | 116 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.512× (z -13.8) |
| [[LoVo (line)]] | wt | 40.9 | 3 (3 ⚠) | 1 | [[Digitoxin (drug)]] 5 µM 2.74× (z +10.1) ⚠ toxic; transcription drop | [[Auranofin (drug)]] 5 µM 0.357× (z -10.2) |
| [[CHP-212 (line)]] | wt | 217 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.207× (z -11.0) ⚠ cell-cycle shift, explains ~20% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.245× (z -9.9) |
| [[HOP62 (line)]] | alt | 54.1 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.504× (z -10.7) |
| [[SK-MEL-2 (line)]] | alt | 131 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.424× (z -14.1) |
| [[SNU-423 (line)]] | alt | 62.0 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.313× (z -11.1) |
| [[A-172 (line)]] | wt | 75.8 | 0 | 2 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.572× (z -9.9) |
| [[AsPC-1 (line)]] | alt | 67.0 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.342× (z -9.1) |
| [[HEC-1-A (line)]] | alt | 120 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.395× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[Panc 03.27 (line)]] | alt | 86.3 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.323× (z -11.9) |
| [[SW 900 (line)]] | alt | 98.5 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.349× (z -10.1) |
| [[A-427 (line)]] | wt | 66.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.326× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[A549 (line)]] | wt | 62.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +8.8) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[COLO 205 (line)]] | alt | 90.0 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.291× (z -9.0) |
| [[HT-29 (line)]] | alt | 47.7 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.423× (z -8.5) |
| [[NCI-H1792 (line)]] | alt | 80.2 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.395× (z -8.5) |
| [[NCI-H23 (line)]] | alt | 44.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +10.0) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H2347 (line)]] | alt | 93.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.432× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[PANC-1 (line)]] | alt | 60.3 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 3.29× (z +8.7) | — |
| [[RKO (line)]] | wt | 69.2 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.353× (z -9.4) |
| [[SW 1271 (line)]] | alt | 51.5 | 0 | 1 (1 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.0731× (z -9.3) ⚠ transcription drop |
| [[SW48 (line)]] | wt | 78.2 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.97× (z +9.8) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[AN3 CA (line)]] | alt | 87.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 78.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 57.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 86.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 51.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 44.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 52.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 55.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 46.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 46.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 65.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 60.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 62.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 80.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 87.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 48.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 109 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 46.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 82.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5885), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HSF2]] | +0.68 | +0.65 / +0.71 | both halves | 7e-06 |  |
| [[TNRC6A]] | +0.67 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[VAPA]] | +0.66 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[RBM33]] | +0.65 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[FBXO9]] | +0.64 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[RCOR3]] | +0.64 | +0.58 / +0.65 | both halves | 7e-06 |  |
| [[TADA1]] | +0.64 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[MBIP]] | +0.64 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[FBXO7]] | +0.63 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[SLC25A12]] | +0.62 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[CLPX]] | +0.62 | +0.65 / +0.58 | both halves | 7e-06 |  |
| [[PAIP1]] | +0.61 | +0.65 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STK40]] | -0.69 | -0.65 / -0.67 | both halves | 7e-06 |  |
| [[GPATCH2L]] | -0.64 | -0.61 / -0.65 | both halves | 7e-06 |  |
| [[KCTD5]] | -0.64 | -0.57 / -0.62 | both halves | 1e-05 | same gene group |
| [[TTLL3]] | -0.61 | -0.57 / -0.63 | both halves | 1e-05 |  |
| [[RAB7A]] | -0.61 | -0.58 / -0.59 | both halves | 7e-06 | pathway: CDC42 GTPase cycle |
| [[RABGEF1]] | -0.59 | -0.51 / -0.62 | both halves | 1e-05 |  |
| [[NABP1]] | -0.58 | -0.59 / -0.57 | both halves | 1e-05 |  |
| [[TPT1-AS1]] | -0.58 | -0.55 / -0.59 | both halves | 1e-05 |  |
| [[ERN1]] | -0.58 | -0.53 / -0.60 | both halves | 1e-05 |  |
| [[MIR22HG]] | -0.58 | -0.46 / -0.70 | both halves | 2e-05 |  |
| [[NPC1]] | -0.57 | -0.53 / -0.59 | both halves | 1e-05 |  |
| [[WNT2B]] | -0.57 | -0.56 / -0.59 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RPRD2]] | C | KCTD3's natural level strengthens RPRD2's drug response | KCTD3's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.62, reverse +0.37; direction not clear | 0.073 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| cells under [[Clofarabine (drug)]] 0.5 µM | C | KCTD3's natural level raises the cells' numbers under Clofarabine 0.5 µM (protects the cells) | KCTD3's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.63 | 0.397 over the table, 0.043 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 146]]; 31 genes; this gene is in the **+** arm (projection on the module's main direction 0.728). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-18.1, 0.3); signed map (-23.8, -8.6). **Vector** length 129, 38.9% of its response variance represented; |z| ≥ 3 in 1,171 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ponatinib (drug)]] 5 µM |  | +8.7 | +5.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +6.4 | +5.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +6.0 | +6.2 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +5.5 | +4.0 |
|  | [[NG25 (drug)]] 5 µM |  | +5.4 | +4.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.8 | +2.3 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +4.8 | +1.9 |
| fall | [[Auranofin (drug)]] 5 µM |  | -9.6 | -12.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.7 | -5.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -5.2 | -4.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.0 | -12.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.7 | -2.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -3.5 | -2.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.2 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | potassium channel tetramerization domain containing 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q41 — chr1:215,567,304-215,621,807 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NY-REN-45 |
| Gene groups (HGNC) | WD repeat domain containing; BTB domain containing; KCTD family |
| Reactome | 4 pathways, smallest: CDC42 GTPase cycle; RHO GTPase cycle; Signaling by Rho GTPases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y597](https://www.uniprot.org/uniprotkb/Q9Y597) (BTB/POZ domain-containing protein KCTD3):

> Accessory subunit of potassium/sodium hyperpolarization-activated cyclic nucleotide-gated channel 3 (HCN3) up-regulating its cell-surface expression and current density without affecting its voltage dependence and kinetics.

**Summary**, from NCBI Gene [51133](https://www.ncbi.nlm.nih.gov/gene/51133):

> This gene encodes a member of the potassium channel tetramerization-domain containing (KCTD) protein family. Members of this protein family regulate the biophysical characteristics of ion channels. In mouse, this protein interacts with hyperpolarization-activated cyclic nucleotide-gated channel complex 3 and enhances its cell surface expression and current density. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Feb 2016]

**Accessions** — [HGNC:21305](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21305) · Entrez [51133](https://www.ncbi.nlm.nih.gov/gene/51133) · UniProt [Q9Y597](https://www.uniprot.org/uniprotkb/Q9Y597) · Ensembl [ENSG00000136636](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136636)

## Data

Gene col 5885: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5885); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5885, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5885]; `tensor/DDL_lfc|DDL_z.npy` [5885]; `embed/gene_vectors.npy` [5885]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5885 or target_col == 5885). Every well: [[KCTD3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KCTD3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
