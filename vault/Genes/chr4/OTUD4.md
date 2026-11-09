---
symbol: "OTUD4"
type: "gene"
col: 8887
ensembl_id: "ENSG00000164164"
name: "OTU deubiquitinase 4"
location: "4q31.21"
module: 10
arm: "+"
pooled_cpm: 78.08
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 10
n_dd_up_clean: 20
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# OTUD4

*OTU deubiquitinase 4* — 4q31.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.14× (z +15.3, q 0e+00, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.436× (z -11.9, q 6e-30, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KICS2]] (+0.68, fdr 1e-05), [[PLBD1-AS1]] (+0.65, fdr 4e-05), [[CYP4V2]] (+0.62, fdr 2e-05); moves opposite to [[VRK3]] (-0.62, fdr 1e-05), [[RRAS]] (-0.60, fdr 5e-05), [[MKNK2]] (-0.60, fdr 6e-05).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[LINC02605]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8887.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.14×** | +15.3 | 0e+00 | 42/48 (CFPAC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.32×** | +11.5 | 3e-28 | 43/48 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **4.54×** | +11.3 | 4e-27 | 47/48 (SW480, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.21×** | +11.2 | 4e-27 | 45/48 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.13×** | +10.8 | 5e-25 | 41/48 (NCI-H460, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.14×** | +10.4 | 2e-23 | 45/47 (LoVo, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.07×** | +10.4 | 3e-23 | 45/48 (NCI-H460, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **3.97×** | +10.3 | 7e-23 | 46/49 (NCI-H1792, SK-MEL-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.83×** | +8.5 | 8e-16 | 42/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.91×** | +8.5 | 1e-15 | 37/45 (NCI-H460, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.79×** | +8.2 | 9e-15 | 43/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.60×** | +6.6 | 1e-09 | 37/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.49×** | +5.6 | 8e-07 | 35/48 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.48×** | +5.5 | 1e-06 | 36/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.06×** | +5.4 | 3e-06 | 28/37 (HS-578T, LOX-IMVI, …) | rises with dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.27×** | +4.7 | 7e-05 | 32/49 (CFPAC-1, NCI-H460, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.36×** | +4.3 | 5e-04 | 32/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.35×** | +4.3 | 6e-04 | 27/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.38×** | +4.2 | 6e-04 | 26/48 (NCI-H460, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 1 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8887.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.436×** | -11.9 | 6e-30 | 48/48 (RKO, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.440×** | -11.8 | 2e-29 | 45/48 (RKO, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.541×** | -8.8 | 3e-16 | 43/48 (RKO, SW480, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.665×** | -5.9 | 7e-07 | 35/48 (RKO, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.796×** | -4.7 | 4e-04 | 28/48 (MIA PaCa-2, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.722×** | -4.5 | 6e-04 | 25/43 (NCI-H1573, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Entrectinib (drug)]] 5 µM |  | **0.741×** | -4.3 | 0.001 | 36/48 (SW 1088, NCI-H661, …) | top dose only |  |
| [[Tofacitinib (drug)]] 5 µM |  | 0.842× | -3.5 | 0.028 | 21/49 (CFPAC-1, LoVo, …) | rises with dose |  |
| [[Budesonide (drug)]] 0.5 µM |  | **0.786×** | -3.5 | 0.032 | 25/48 (A549, HS-578T, …) | inconsistent across doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.792×** | -3.4 | 0.042 | 23/49 (LoVo, RKO, …) | top dose only |  |
| [[Carbamazepine (drug)]] 5 µM |  | **0.802×** | -3.2 | 0.074 | 19/47 (LOX-IMVI, RPMI-7951, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 0.809× | -3.1 | 0.10 | 20/48 (SW 1088, HOP62, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8887. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 62.3 | 15 (4 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 7.99× (z +18.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 7.22× (z +17.9) | — |
| [[SW480 (line)]] | alt | 72.3 | 7 (2 ⚠) | 3 | [[Digitoxin (drug)]] 0.5 µM 2.91× (z +14.3) | [[Panobinostat (drug)]] 5 µM 0.355× (z -13.9) |
| [[NCI-H1792 (line)]] | alt | 130 | 9 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.30× (z +15.0) | — |
| [[PANC-1 (line)]] | alt | 61.0 | 7 (2 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +14.4) | [[Panobinostat (drug)]] 0.5 µM 0.418× (z -9.7) |
| [[NCI-H1573 (line)]] | alt | 70.7 | 7 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.12× (z +17.5) | [[Dinaciclib (drug)]] 5 µM 0.101× (z -19.3) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 213 | 1 | 7 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 6.88× (z +10.0) | [[Panobinostat (drug)]] 5 µM 0.206× (z -15.7) |
| [[SK-MEL-2 (line)]] | alt | 96.3 | 6 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +16.4) | [[Dinaciclib (drug)]] 5 µM 0.355× (z -9.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.385× (z -9.2) |
| [[HOP62 (line)]] | alt | 97.3 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.00× (z +15.7) | — |
| [[LoVo (line)]] | wt | 78.9 | 4 (2 ⚠) | 3 | [[Niclosamide (olamine) (drug)]] 5 µM 3.47× (z +13.9) ⚠ toxic · without an alert: [[PH-797804 (drug)]] 5 µM 4.82× (z +9.6) | [[Panobinostat (drug)]] 5 µM 0.383× (z -11.1) |
| [[LS 180 (line)]] | wt | 62.6 | 6 (2 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.38× (z +16.2) | [[Panobinostat (drug)]] 5 µM 0.406× (z -8.7) |
| [[NCI-H2347 (line)]] | alt | 115 | 5 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 0.5 µM 4.82× (z +13.9) | [[Panobinostat (drug)]] 0.5 µM 0.333× (z -9.8) |
| [[A549 (line)]] | wt | 83.6 | 4 | 2 | [[Homoharringtonine (drug)]] 5 µM 3.93× (z +14.9) | [[Panobinostat (drug)]] 5 µM 0.227× (z -11.6) |
| [[A-172 (line)]] | wt | 115 | 3 | 2 | [[Homoharringtonine (drug)]] 0.5 µM 4.09× (z +13.1) | [[Panobinostat (drug)]] 0.5 µM 0.377× (z -9.1) |
| [[Panc 03.27 (line)]] | alt | 75.0 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +14.4) | — |
| [[SW 900 (line)]] | alt | 50.4 | 5 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 6.61× (z +11.5) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 5.42× (z +10.7) | — |
| [[A498 (line)]] | wt | 111 | 2 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +12.3) | [[Panobinostat (drug)]] 0.5 µM 0.350× (z -10.4) |
| [[HS-578T (line)]] | alt | 80.4 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +10.8) | — |
| [[NCI-H23 (line)]] | alt | 50.0 | 3 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 3.73× (z +11.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.90× (z +9.8) | [[Dinaciclib (drug)]] 0.5 µM 0.177× (z -16.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[SW48 (line)]] | wt | 113 | 3 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.71× (z +14.2) | [[Panobinostat (drug)]] 5 µM 0.313× (z -8.7) |
| [[H4 (line)]] | wt | 83.4 | 3 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 5.48× (z +10.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 3.03× (z +10.6) | — |
| [[hTERT-HPNE (line)]] | wt | 92.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +11.1) | — |
| [[J82 (line)]] | alt | 83.8 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +11.0) | [[Panobinostat (drug)]] 0.5 µM 0.318× (z -10.6) |
| [[MIA PaCa-2 (line)]] | alt | 88.4 | 1 | 2 | [[Homoharringtonine (drug)]] 0.5 µM 3.81× (z +11.5) | [[Panobinostat (drug)]] 5 µM 0.251× (z -12.0) |
| [[RPMI-7951 (line)]] | alt | 81.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +11.4) | — |
| [[SNU-423 (line)]] | alt | 59.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.98× (z +18.6) | — |
| [[AsPC-1 (line)]] | alt | 47.9 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.31× (z +9.2) | — |
| [[CFPAC-1 (line)]] | alt | 79.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.21× (z +21.5) | — |
| [[HEC-1-A (line)]] | alt | 80.8 | 1 | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 6.28× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.275× (z -11.8) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 58.7 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.59× (z +15.1) | — |
| [[NCI-H2030 (line)]] | alt | 54.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +12.8) | — |
| [[SW1417 (line)]] | alt | 60.8 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.356× (z -10.6) |
| [[A-427 (line)]] | wt | 66.9 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 6.05× (z +9.6) | — |
| [[BT-474 (line)]] | alt | 47.2 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 7.74× (z +8.6) | — |
| [[C32 (line)]] | wt | 85.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.97× (z +9.6) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 74.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +9.1) | — |
| [[KATO III (line)]] | alt | 43.6 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.59× (z +8.8) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 61.5 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 10.8× (z +10.3) | — |
| [[AN3 CA (line)]] | alt | 85.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 104 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 107 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 83.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 58.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 70.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 79.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 57.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 44.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 83.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 61.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 73.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8887), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KICS2]] | +0.68 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[PLBD1-AS1]] | +0.65 | +0.41 / +0.49 | both halves | 4e-05 |  |
| [[CYP4V2]] | +0.62 | +0.51 / +0.46 | both halves | 2e-05 |  |
| [[MCCC2]] | +0.62 | +0.43 / +0.53 | both halves | 3e-05 |  |
| [[MTPAP]] | +0.61 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[AMER1]] | +0.61 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[OGFRL1]] | +0.61 | +0.51 / +0.42 | both halves | 4e-05 |  |
| [[ANKRD18B]] | +0.60 | +0.38 / +0.37 | both halves | 8e-05 |  |
| [[ZNF747]] | +0.59 | +0.38 / +0.39 | both halves | 7e-05 |  |
| [[BTC]] | +0.59 | +0.38 / +0.43 | both halves | 6e-05 |  |
| [[PM20D2]] | +0.58 | +0.49 / +0.31 | both halves | 2e-04 |  |
| [[IQCH-AS1]] | +0.58 | +0.32 / +0.46 | both halves | 2e-04 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VRK3]] | -0.62 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[RRAS]] | -0.60 | -0.44 / -0.40 | both halves | 5e-05 |  |
| [[MKNK2]] | -0.60 | -0.38 / -0.61 | both halves | 6e-05 |  |
| [[PI4KA]] | -0.59 | -0.54 / -0.41 | both halves | 4e-05 |  |
| [[PLPPR2]] | -0.59 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[GNAI2]] | -0.59 | -0.41 / -0.37 | both halves | 8e-05 |  |
| [[SDF2]] | -0.58 | -0.58 / -0.43 | both halves | 4e-05 |  |
| [[COX6A1]] | -0.58 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[NOSIP]] | -0.57 | -0.43 / -0.64 | both halves | 3e-05 |  |
| [[PI4KAP1]] | -0.57 | -0.50 / -0.31 | both halves | 2e-04 |  |
| [[ANAPC11]] | -0.57 | -0.43 / -0.33 | both halves | 1e-04 |  |
| [[PI4KAP1-1]] | -0.56 | -0.37 / -0.45 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02605]] | B | LINC02605 activity raises OTUD4's level | lines that do not express LINC02605 (15) vs lines expressing it (35) | 1.30× lower at baseline in the lines without LINC02605 | 0.033 | ⚠ within organs, on part of the lines; also absent: ENSG00000285744, FAR2, ENSG00000285517 |
| [[FAS]] | B | FAS activity raises OTUD4's level | lines that do not express FAS (8) vs lines expressing it (42) | 1.30× lower at baseline in the lines without FAS | 0.099 | ⚠ within organs, on part of the lines; also absent: ACTA2, RGS10; maybe low, not absent |
| [[PC]] | C | PC activity lowers OTUD4's level | lines that do not express PC (4) vs lines expressing it (46) | 1.68× higher at baseline in the lines without PC | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: DUSP1, ANKEF1, ZFAND4; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.565). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-2.0, 7.4); signed map (28.4, -30.9). **Vector** length 96.1, 34.0% of its response variance represented; |z| ≥ 3 in 1,355 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +9.2 | +8.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.5 | -4.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +7.0 | +2.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | +6.6 | -1.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.1 | +11.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.8 | +5.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.0 | -0.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.0 | +2.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.8 | +0.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.8 | -0.9 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -6.1 | -11.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.9 | -11.8 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.4 | -8.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.5 | +10.4 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.4 | +8.2 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -2.8 | -1.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.6 | -3.4 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.5 | +0.7 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -2.4 | -3.5 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.4 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | OTU deubiquitinase 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q31.21 — chr4:145,110,838-145,180,589 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HSHIN1, KIAA1046, DUBA6 |
| Gene groups (HGNC) | OTU domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q01804](https://www.uniprot.org/uniprotkb/Q01804) (OTU domain-containing protein 4):

> Deubiquitinase which hydrolyzes the isopeptide bond between the ubiquitin C-terminus and the lysine epsilon-amino group of the target protein. May negatively regulate inflammatory and pathogen recognition signaling in innate immune response. Upon phosphorylation at Ser-202 and Ser-204 residues, via IL-1 receptor and Toll-like receptor signaling pathway, specifically deubiquitinates 'Lys-63'-polyubiquitinated MYD88 adapter protein triggering down-regulation of NF-kappa-B-dependent transcription …

**Summary**, from NCBI Gene [54726](https://www.ncbi.nlm.nih.gov/gene/54726):

> Alternatively spliced transcript variants have been found for this gene. The smaller protein isoform encoded by the shorter transcript variant is found only in HIV-1 infected cells. [provided by RefSeq, Jul 2010]

**Accessions** — [HGNC:24949](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24949) · Entrez [54726](https://www.ncbi.nlm.nih.gov/gene/54726) · UniProt [Q01804](https://www.uniprot.org/uniprotkb/Q01804) · Ensembl [ENSG00000164164](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164164)

## Data

Gene col 8887: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8887); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8887, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8887]; `tensor/DDL_lfc|DDL_z.npy` [8887]; `embed/gene_vectors.npy` [8887]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8887 or target_col == 8887). Every well: [[OTUD4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/OTUD4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
