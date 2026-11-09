---
symbol: "ORC5"
type: "gene"
col: 9009
ensembl_id: "ENSG00000164815"
name: "origin recognition complex subunit 5"
location: "7q22.1-q22.2"
module: 33
arm: "+"
pooled_cpm: 43.27
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 12
n_dd_up_clean: 11
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# ORC5

*origin recognition complex subunit 5* — 7q22.1-q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.15× (z +13.9, q 5e-41, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (6 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.612× (z -8.9, q 5e-16, down in 30 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DDX55]] (+0.75, fdr 7e-06), [[NARS2]] (+0.74, fdr 7e-06), [[TAMM41]] (+0.74, fdr 7e-06); moves opposite to [[NPHS1]] (-0.62, fdr 5e-05), [[TP53INP2]] (-0.62, fdr 1e-05), [[MICALL2]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9009.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.15×** | +13.9 | 5e-41 | 45/48 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.93×** | +12.0 | 1e-30 | 42/48 (SW480, A498, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.87×** | +11.4 | 1e-27 | 41/48 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.26×** | +7.7 | 1e-12 | 33/48 (LoVo, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.97×** | +6.4 | 1e-08 | 32/49 (LoVo, KATO III, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **1.38×** | +5.6 | 2e-06 | 27/46 (H4, NCI-H1573, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.36×** | +5.6 | 2e-06 | 30/48 (NCI-H2347, CFPAC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.32×** | +5.0 | 5e-05 | 24/48 (SW 900, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.67×** | +4.9 | 7e-05 | 28/48 (SW480, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.30×** | +4.9 | 7e-05 | 24/48 (HT-29, AsPC-1, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.32×** | +4.8 | 8e-05 | 21/48 (NCI-H2347, SW480, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.29×** | +4.5 | 3e-04 | 24/48 (NCI-H1573, NCI-H460, …) | all doses, flat |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | 1.18× | +4.2 | 0.001 | 20/48 (SNU-423, RKO, …) | top dose only | low cells (technical?) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.24×** | +4.0 | 0.003 | 18/48 (NCI-H1792, NCI-H460, …) | all doses, flat |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~9% of this change | **1.22×** | +3.6 | 0.011 | 18/48 (NCI-H2347, AsPC-1, …) | rises with dose |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 1.20× | +3.3 | 0.033 | 10/48 (NCI-H460, LOX-IMVI, …) | rises with dose |  |
| [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | 1.20× | +3.2 | 0.042 | 5/48 (NCI-H1573, BT-474, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.18× | +3.0 | 0.077 | 10/48 (HT-29, RKO, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9009.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.612×** | -8.9 | 5e-16 | 30/48 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~7% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.619×** | -8.7 | 1e-15 | 34/48 (C32, A-427, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.648×** | -7.8 | 9e-13 | 28/47 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.641×** | -7.7 | 2e-12 | 25/42 (NCI-H23, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.749×** | -7.3 | 2e-11 | 28/48 (SK-MEL-2, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.757×** | -7.1 | 1e-10 | 26/48 (A498, NCI-H460, …) | top dose only | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.724×** | -5.8 | 5e-07 | 27/47 (C32, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.734×** | -5.2 | 2e-05 | 25/44 (A-172, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.766×** | -4.8 | 1e-04 | 25/48 (SW48, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.773×** | -4.6 | 2e-04 | 23/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.773×** | -4.5 | 4e-04 | 25/47 (SW48, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.686×** | -3.6 | 0.018 | 20/48 (NCI-H2347, HT-29, …) | top dose only | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.880× | -3.2 | 0.051 | 22/48 (A-172, HOP62, …) | top dose only |  |
| [[Auranofin (drug)]] 0.5 µM |  | 0.839× | -3.2 | 0.066 | 15/48 (PANC-1, A-172, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9009. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 45.4 | 0 | 11 (8 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.206× (z -17.0) |
| [[SW480 (line)]] | alt | 59.3 | 3 | 5 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.23× (z +11.1) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.328× (z -15.4) |
| [[A498 (line)]] | wt | 55.3 | 3 | 4 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.74× (z +10.4) | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -17.8) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.466× (z -11.0) |
| [[C32 (line)]] | wt | 130 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.116× (z -20.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.177× (z -16.6) |
| [[PANC-1 (line)]] | alt | 49.3 | 1 | 6 (5 ⚠) | [[Panobinostat (drug)]] 5 µM 2.04× (z +9.3) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.369× (z -13.0) |
| [[HOP62 (line)]] | alt | 36.7 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.400× (z -12.4) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.424× (z -11.6) |
| [[A-172 (line)]] | wt | 42.7 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.201× (z -13.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.365× (z -13.4) |
| [[KATO III (line)]] | alt | 50.5 | 1 | 3 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 5.27× (z +8.6) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.299× (z -11.9) |
| [[SW48 (line)]] | wt | 54.6 | 0 | 4 (3 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.118× (z -12.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.182× (z -10.6) |
| [[SK-MEL-2 (line)]] | alt | 66.2 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.386× (z -13.4) |
| [[AN3 CA (line)]] | alt | 73.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.127× (z -9.5) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 50.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.287× (z -12.8) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 45.8 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 7.89× (z +10.5) | — |
| [[LOX-IMVI (line)]] | wt | 33.0 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.04× (z +9.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 72.2 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.323× (z -11.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 20.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.247× (z -12.2) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[XRK3F2 (drug)]] 0.5 µM 0.0640× (z -12.1) |
| [[NCI-H23 (line)]] | alt | 69.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.188× (z -18.4) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 45.6 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.323× (z -11.1) |
| [[A-427 (line)]] | wt | 49.1 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.250× (z -13.8) |
| [[BT-474 (line)]] | alt | 32.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.213× (z -10.1) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 53.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0897× (z -19.2) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 31.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.163× (z -8.8) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 39.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.267× (z -12.7) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 38.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.256× (z -11.2) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 57.7 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.268× (z -9.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RPMI-7951 (line)]] | alt | 32.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.390× (z -9.3) ⚠ cell-cycle shift, explains ~40% of this change |
| [[SHP-77 (line)]] | alt | 39.6 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.268× (z -10.3) |
| [[SNU-423 (line)]] | alt | 37.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.451× (z -9.9) ⚠ cell-cycle shift, explains ~40% of this change |
| [[SW 900 (line)]] | alt | 29.5 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.46× (z +8.6) | — |
| [[A549 (line)]] | wt | 39.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 30.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 40.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 25.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 34.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 45.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 48.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 47.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 55.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9009), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DDX55]] | +0.75 | +0.64 / +0.78 | both halves | 7e-06 |  |
| [[NARS2]] | +0.74 | +0.66 / +0.73 | both halves | 7e-06 |  |
| [[TAMM41]] | +0.74 | +0.61 / +0.74 | both halves | 7e-06 |  |
| [[KAT14]] | +0.73 | +0.64 / +0.76 | both halves | 7e-06 |  |
| [[NUDCD3]] | +0.73 | +0.60 / +0.71 | both halves | 7e-06 |  |
| [[LCLAT1]] | +0.70 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[DHODH]] | +0.70 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[ZNF74]] | +0.70 | +0.57 / +0.74 | both halves | 1e-05 |  |
| [[GEMIN5]] | +0.69 | +0.62 / +0.69 | both halves | 7e-06 |  |
| [[TMEM177]] | +0.69 | +0.57 / +0.67 | both halves | 8e-06 |  |
| [[PARGP1]] | +0.69 | +0.67 / +0.69 | both halves | 7e-06 |  |
| [[TSEN2]] | +0.68 | +0.60 / +0.70 | both halves | 7e-06 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NPHS1]] | -0.62 | -0.40 / -0.51 | both halves | 5e-05 |  |
| [[TP53INP2]] | -0.62 | -0.62 / -0.55 | both halves | 1e-05 |  |
| [[MICALL2]] | -0.61 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[LASP1]] | -0.60 | -0.57 / -0.59 | both halves | 1e-05 |  |
| [[ERO1B]] | -0.57 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[LINC00393]] | -0.57 | -0.39 / -0.50 | both halves | 5e-05 |  |
| [[STX17-DT]] | -0.56 | -0.37 / -0.45 | both halves | 8e-05 |  |
| [[FAM117A]] | -0.56 | -0.43 / -0.47 | both halves | 3e-05 |  |
| [[YPEL5]] | -0.56 | -0.48 / -0.54 | both halves | 2e-05 |  |
| [[CCNT2-AS1]] | -0.55 | -0.39 / -0.41 | both halves | 5e-05 |  |
| [[FAM151B]] | -0.55 | -0.40 / -0.44 | both halves | 5e-05 |  |
| [[MC1R]] | -0.55 | -0.47 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.706). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-17.0, -43.2); signed map (-16.7, -22.3). **Vector** length 113, 31.3% of its response variance represented; |z| ≥ 3 in 1,099 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +8.5 | +6.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +8.2 | +7.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.4 | +4.8 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.2 | +12.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | +3.7 | +5.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.8 | +2.3 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +2.7 | +2.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.6 | +1.2 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -10.2 | -7.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -8.2 | -8.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | -7.8 | -7.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.2 | -2.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.9 | -1.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.5 | -3.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.8 | -3.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.5 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | origin recognition complex subunit 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q22.1-q22.2 — chr7:104,126,341-104,208,047 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Orc5p, ORC5T, PPP1R117; previously ORC5L |
| Gene groups (HGNC) | Protein phosphatase 1 regulatory subunits; Origin recognition complex |
| Hallmark sets | G2M_CHECKPOINT |
| Reactome | 19 pathways, smallest: CDC6 association with the ORC:origin complex; E2F-enabled inhibition of pre-replication complex formation; E2F mediated regulation of DNA replication |
| Matched by | ensembl_id |

**Function**, from UniProt [O43913](https://www.uniprot.org/uniprotkb/O43913) (Origin recognition complex subunit 5):

> Component of the origin recognition complex (ORC) that binds origins of replication. DNA-binding is ATP-dependent. The specific DNA sequences that define origins of replication have not been identified yet. ORC is required to assemble the pre-replication complex necessary to initiate DNA replication.

**Summary**, from NCBI Gene [5001](https://www.ncbi.nlm.nih.gov/gene/5001):

> The origin recognition complex (ORC) is a highly conserved six subunit protein complex essential for the initiation of the DNA replication in eukaryotic cells. Studies in yeast demonstrated that ORC binds specifically to origins of replication and serves as a platform for the assembly of additional initiation factors such as Cdc6 and Mcm proteins. The protein encoded by this gene is a subunit of the ORC complex. Alternatively spliced transcript variants encoding distinct isoforms have been …

**Accessions** — [HGNC:8491](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8491) · Entrez [5001](https://www.ncbi.nlm.nih.gov/gene/5001) · UniProt [O43913](https://www.uniprot.org/uniprotkb/O43913) · Ensembl [ENSG00000164815](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164815)

## Data

Gene col 9009: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9009); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9009, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9009]; `tensor/DDL_lfc|DDL_z.npy` [9009]; `embed/gene_vectors.npy` [9009]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9009 or target_col == 9009). Every well: [[ORC5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ORC5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
