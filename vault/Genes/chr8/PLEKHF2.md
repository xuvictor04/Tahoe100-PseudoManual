---
symbol: "PLEKHF2"
type: "gene"
col: 10662
ensembl_id: "ENSG00000175895"
name: "pleckstrin homology and FYVE domain containing 2"
location: "8q22.1"
module: 35
arm: "+"
pooled_cpm: 40.57
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 9
n_dd_up_clean: 18
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# PLEKHF2

*pleckstrin homology and FYVE domain containing 2* — 8q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.60× (z +22.9, q 0e+00, up in 45 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.490× (z -11.7, q 1e-28, down in 29 of 37 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.654× (z -7.2, q 1e-10, down in 34 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C3orf38]] (+0.75, fdr 9e-06), [[RAB21]] (+0.72, fdr 7e-06), [[CCNT2]] (+0.71, fdr 1e-05); moves opposite to [[INTS1]] (-0.62, fdr 2e-05), [[RNF216]] (-0.61, fdr 1e-05), [[FBRSL1]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 035]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10662.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.60×** | +22.9 | 0e+00 | 45/47 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.57×** | +15.4 | 0e+00 | 45/47 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.27×** | +13.9 | 2e-41 | 42/47 (PANC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.21×** | +13.4 | 4e-39 | 41/48 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **4.53×** | +13.4 | 9e-39 | 43/49 (SW480, HT-29, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.11×** | +12.6 | 1e-34 | 42/46 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.07×** | +12.4 | 3e-33 | 37/47 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.13×** | +12.3 | 3e-33 | 34/44 (SW480, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.75×** | +9.1 | 5e-18 | 36/46 (PANC-1, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.70×** | +8.9 | 2e-17 | 32/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.41×** | +8.2 | 1e-14 | 36/48 (PANC-1, A498, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.42×** | +7.8 | 2e-13 | 29/47 (C32, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.56×** | +7.5 | 2e-12 | 31/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.36×** | +7.4 | 5e-12 | 28/47 (A498, SHP-77, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.53×** | +7.2 | 3e-11 | 32/48 (HEC-1-A, A549, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.34×** | +4.9 | 3e-05 | 23/48 (RPMI-7951, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.27×** | +4.0 | 0.002 | 16/48 (SK-MEL-2, PANC-1, …) | two highest doses |  |
| [[Selinexor (drug)]] 0.05 µM |  | **1.26×** | +3.9 | 0.003 | 15/48 (LS 180, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 6 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10662.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.490×** | -11.7 | 1e-28 | 29/37 (NCI-H2347, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.547×** | -10.3 | 3e-22 | 31/42 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.654×** | -7.2 | 1e-10 | 34/48 (CFPAC-1, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.681×** | -6.5 | 9e-09 | 26/48 (CFPAC-1, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.927× | -4.4 | 0.001 | 3/49 (SNU-1, NCI-H2122, …) | inconsistent across doses |  |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | **0.796×** | -3.7 | 0.018 | 12/49 (NCI-H1573, AsPC-1, …) | top dose only | plate-row cell shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~17% of this change | **0.802×** | -3.5 | 0.042 | 19/38 (A-172, NCI-H2347, …) | all doses, stronger at high dose | composition shift |
| [[Apalutamide (drug)]] 0.5 µM |  | **0.820×** | -3.4 | 0.049 | 13/48 (NCI-H1573, HEC-1-A, …) | inconsistent across doses |  |
| [[Diphenhydramine (drug)]] 0.5 µM |  | **0.821×** | -3.4 | 0.050 | 13/48 (NCI-H1573, SW1417, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.824×** | -3.3 | 0.053 | 16/48 (AsPC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.881× | -3.1 | 0.11 | 10/48 (SW 1271, CFPAC-1, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | 0.836× | -3.1 | 0.11 | 19/48 (CFPAC-1, A-172, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10662. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 30.1 | 10 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.01× (z +21.0) | [[Dinaciclib (drug)]] 5 µM 0.404× (z -9.4) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 34.2 | 9 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +15.8) | [[Dinaciclib (drug)]] 5 µM 0.278× (z -14.7) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 49.5 | 5 (2 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.65× (z +14.8) | [[Dinaciclib (drug)]] 0.05 µM 0.201× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~17% of this change |
| [[NCI-H460 (line)]] | wt | 17.4 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +12.3) | — |
| [[LoVo (line)]] | wt | 33.8 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +16.2) | — |
| [[CFPAC-1 (line)]] | alt | 64.4 | 1 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +10.0) | [[Dinaciclib (drug)]] 0.5 µM 0.128× (z -19.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.352× (z -10.1) |
| [[HT-29 (line)]] | alt | 37.2 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +13.6) | — |
| [[LS 180 (line)]] | wt | 30.7 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.325× (z -8.8) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 114 | 1 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +11.0) | [[Dinaciclib (drug)]] 5 µM 0.0857× (z -21.6) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 29.8 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.32× (z +13.0) | — |
| [[C32 (line)]] | wt | 55.1 | 2 | 2 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 8.93× (z +10.0) | [[Dinaciclib (drug)]] 0.5 µM 0.204× (z -13.9) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 33.6 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +14.8) | [[Dinaciclib (drug)]] 0.5 µM 0.359× (z -9.6) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 37.5 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.26× (z +13.6) | — |
| [[AsPC-1 (line)]] | alt | 89.2 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +11.0) | [[Dinaciclib (drug)]] 5 µM 0.145× (z -13.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.303× (z -8.9) |
| [[NCI-H2030 (line)]] | alt | 24.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +10.7) | — |
| [[Panc 03.27 (line)]] | alt | 56.8 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.04× (z +12.4) | [[Dinaciclib (drug)]] 0.05 µM 0.279× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~17% of this change |
| [[SW 900 (line)]] | alt | 32.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.52× (z +11.6) | — |
| [[A-172 (line)]] | wt | 25.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0911× (z -17.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~17% of this change |
| [[BT-474 (line)]] | alt | 132 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 10.8× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.251× (z -11.1) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 42.4 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.248× (z -10.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.338× (z -8.6) |
| [[J82 (line)]] | alt | 32.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +11.1) | — |
| [[SW1417 (line)]] | alt | 87.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.26× (z +13.8) | [[Dinaciclib (drug)]] 0.5 µM 0.283× (z -10.4) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 31.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +9.5) | — |
| [[COLO 205 (line)]] | alt | 38.6 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 3.94× (z +8.8) | — |
| [[HepG2_C3A (line)]] | wt | 36.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0740× (z -15.6) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 50.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.279× (z -10.9) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 52.9 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 3.30× (z +8.6) | — |
| [[hTERT-HPNE (line)]] | wt | 28.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +9.6) | — |
| [[LOX-IMVI (line)]] | wt | 39.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.289× (z -8.8) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 13.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +8.5) | — |
| [[NCI-H1792 (line)]] | alt | 21.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.55× (z +11.6) | — |
| [[NCI-H23 (line)]] | alt | 12.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.94× (z +10.4) | — |
| [[NCI-H661 (line)]] | alt | 84.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0497× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~17% of this change |
| [[SHP-77 (line)]] | alt | 28.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.95× (z +9.8) | — |
| [[SK-MEL-2 (line)]] | alt | 55.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.56× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~17% of this change | — |
| [[SW48 (line)]] | wt | 23.5 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0863× (z -12.3) |
| [[A-427 (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 45.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 53.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 46.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 46.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 24.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10662), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C3orf38]] | +0.75 | +0.57 / +0.69 | both halves | 9e-06 |  |
| [[RAB21]] | +0.72 | +0.70 / +0.58 | both halves | 7e-06 |  |
| [[CCNT2]] | +0.71 | +0.71 / +0.49 | both halves | 1e-05 |  |
| [[FBXL3]] | +0.71 | +0.65 / +0.69 | both halves | 7e-06 |  |
| [[CLN5]] | +0.69 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[LINC00938]] | +0.67 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[BTN2A1]] | +0.67 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[ZNF44]] | +0.67 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[ZNF442]] | +0.64 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[RBM7]] | +0.64 | +0.58 / +0.57 | both halves | 8e-06 |  |
| [[RCHY1]] | +0.64 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[RAB9A]] | +0.63 | +0.61 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[INTS1]] | -0.62 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[RNF216]] | -0.61 | -0.52 / -0.57 | both halves | 1e-05 |  |
| [[FBRSL1]] | -0.61 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[DGKD]] | -0.61 | -0.53 / -0.49 | both halves | 1e-05 | same gene group |
| [[ERCC2]] | -0.60 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[CALU]] | -0.60 | -0.48 / -0.54 | both halves | 2e-05 |  |
| [[DAP3]] | -0.59 | -0.49 / -0.57 | both halves | 1e-05 |  |
| [[CHID1]] | -0.59 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[SND1]] | -0.59 | -0.35 / -0.57 | both halves | 1e-04 |  |
| [[TCF3]] | -0.59 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[EP400]] | -0.58 | -0.33 / -0.58 | both halves | 1e-04 |  |
| [[LMBR1]] | -0.57 | -0.59 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.469). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-0.1, 18.0); signed map (27.7, -15.4). **Vector** length 95.9, 25.9% of its response variance represented; |z| ≥ 3 in 1,137 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +9.0 | +8.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +6.6 | +12.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.5 | +12.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.0 | +7.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.9 | +7.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.0 | +0.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.9 | +1.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.8 | +1.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.7 | +1.2 |
| fall | [[Panobinostat (drug)]] 5 µM |  | -5.3 | -6.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.9 | -7.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.8 | -0.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -4.2 | -3.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -3.8 | -10.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.2 | -1.3 |
|  | [[EX229 (drug)]] 5 µM |  | -2.1 | -1.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.1 | +4.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.0 | -0.4 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | -1.7 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | pleckstrin homology and FYVE domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q22.1 — chr8:95,115,642-95,156,698 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ZFYVE18, PHAFIN2, FLJ13187 |
| Gene groups (HGNC) | Zinc fingers FYVE-type; Pleckstrin homology domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H8W4](https://www.uniprot.org/uniprotkb/Q9H8W4) (Pleckstrin homology domain-containing family F member 2):

> May play a role in early endosome fusion upstream of RAB5, hence regulating receptor trafficking and fluid-phase transport. Enhances cellular sensitivity to TNF-induced apoptosis.

**Summary**, from NCBI Gene [79666](https://www.ncbi.nlm.nih.gov/gene/79666):

> Predicted to enable phosphatidylinositol binding activity. Predicted to be involved in endosome organization and endosome to lysosome transport. Located in transport vesicle. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:20757](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20757) · Entrez [79666](https://www.ncbi.nlm.nih.gov/gene/79666) · UniProt [Q9H8W4](https://www.uniprot.org/uniprotkb/Q9H8W4) · Ensembl [ENSG00000175895](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175895)

## Data

Gene col 10662: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10662); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10662, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10662]; `tensor/DDL_lfc|DDL_z.npy` [10662]; `embed/gene_vectors.npy` [10662]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10662 or target_col == 10662). Every well: [[PLEKHF2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLEKHF2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
