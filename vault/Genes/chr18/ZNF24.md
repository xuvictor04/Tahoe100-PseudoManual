---
symbol: "ZNF24"
type: "gene"
col: 10260
ensembl_id: "ENSG00000172466"
name: "zinc finger protein 24"
location: "18q12.2"
module: 16
arm: "+"
pooled_cpm: 68.81
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 8
n_dd_up_clean: 14
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# ZNF24

*zinc finger protein 24* — 18q12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.59× (z +32.6, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.544× (z -14.8, q 0e+00, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UBQLN2]] (+0.79, fdr 7e-06), [[FAM200A]] (+0.77, fdr 7e-06), [[ZNF764]] (+0.76, fdr 7e-06); moves opposite to [[FAR1]] (-0.68, fdr 7e-06), [[TCF3]] (-0.67, fdr 1e-05), [[WASF3]] (-0.66, fdr 3e-05).
> It sits in the **+** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10260.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.59×** | +32.6 | 0e+00 | 47/48 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.74×** | +23.5 | 0e+00 | 48/48 (PANC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.62×** | +23.4 | 0e+00 | 48/48 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.08×** | +17.7 | 0e+00 | 47/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.91×** | +15.7 | 0e+00 | 46/48 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.90×** | +15.5 | 0e+00 | 44/48 (A-172, PANC-1, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.74×** | +13.4 | 4e-39 | 45/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.88×** | +13.4 | 5e-39 | 45/49 (LoVo, PANC-1, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.71×** | +13.0 | 9e-37 | 44/48 (C32, MIA PaCa-2, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.68×** | +12.5 | 4e-34 | 44/48 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.58×** | +10.7 | 5e-25 | 40/47 (NCI-H2030, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.37×** | +7.7 | 7e-13 | 33/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.80×** | +7.5 | 3e-12 | 33/48 (HEC-1-A, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.29×** | +6.2 | 3e-08 | 28/48 (NCI-H460, C32, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.27×** | +5.8 | 2e-07 | 25/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.24×** | +5.3 | 5e-06 | 27/48 (CFPAC-1, A498, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.22×** | +4.9 | 4e-05 | 22/48 (PANC-1, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.20×** | +3.2 | 0.038 | 14/47 (MIA PaCa-2, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Palmatine (chloride) (drug)]] 0.5 µM |  | 1.14× | +3.2 | 0.038 | 12/48 (RPMI-7951, NCI-H2347, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10260.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.544×** | -14.8 | 0e+00 | 46/48 (SK-MEL-2, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.564×** | -13.9 | 2e-41 | 47/48 (NCI-H1573, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.607×** | -12.1 | 2e-31 | 46/48 (NCI-H1573, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.708×** | -8.4 | 7e-15 | 37/48 (SK-MEL-2, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.931× | -6.0 | 2e-07 | 1/50 (NCI-H2122) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.848× | -5.6 | 2e-06 | 15/48 (SK-MEL-2, LOX-IMVI, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.681×** | -4.9 | 9e-05 | 23/49 (NCI-H23, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.826×** | -4.6 | 2e-04 | 25/48 (SK-MEL-2, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.824×** | -4.5 | 4e-04 | 25/48 (SNU-1, SNU-423, …) | top dose only |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.05 µM |  | 0.839× | -3.9 | 0.005 | 17/48 (RPMI-7951, NCI-H1573, …) | inconsistent across doses |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.752×** | -3.6 | 0.015 | 18/48 (NCI-H2347, HS-578T, …) | rises with dose | noisy plate (z scaled) |
| [[Allantoin (drug)]] 0.05 µM | ⚠ transcription drop | 0.863× | -3.6 | 0.017 | 14/48 (NCI-H661, SW48, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.869× | -3.4 | 0.030 | 21/49 (A-427, NCI-H1573, …) | rises with dose | composition shift |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | 0.875× | -3.3 | 0.046 | 9/48 (NCI-H1573, Panc 03.27, …) | inconsistent across doses |  |
| [[Rapamycin (drug)]] 0.5 µM |  | 0.877× | -3.2 | 0.057 | 11/48 (LOX-IMVI, LoVo, …) | inconsistent across doses | position effect removed |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 0.879× | -3.1 | 0.060 | 9/48 (hTERT-HPNE, NCI-H1573, …) | all doses, flat |  |
| [[Lidocaine (hydrochloride) (drug)]] 5 µM |  | 0.914× | -3.1 | 0.060 | 4/48 (AN3 CA, LS 180, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, +0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10260. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 138 | 9 (1 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.79× (z +23.7) | [[Panobinostat (drug)]] 5 µM 0.342× (z -13.5) |
| [[NCI-H460 (line)]] | wt | 58.7 | 10 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.34× (z +22.9) | [[Panobinostat (drug)]] 5 µM 0.495× (z -9.5) |
| [[PANC-1 (line)]] | alt | 64.2 | 9 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 5.04× (z +35.7) | [[Belinostat (drug)]] 5 µM 0.550× (z -9.4) |
| [[LoVo (line)]] | wt | 90.2 | 9 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +14.4) | — |
| [[HEC-1-A (line)]] | alt | 64.1 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +19.1) | — |
| [[HOP62 (line)]] | alt | 60.3 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.17× (z +19.8) | — |
| [[HS-578T (line)]] | alt | 61.3 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.74× (z +21.2) | — |
| [[SK-MEL-2 (line)]] | alt | 114 | 3 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +15.8) | [[Dinaciclib (drug)]] 5 µM 0.114× (z -26.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.299× (z -15.5) |
| [[A-172 (line)]] | wt | 82.0 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.00× (z +30.0) | — |
| [[A-427 (line)]] | wt | 86.6 | 6 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.41× (z +15.3) | [[Dinaciclib (drug)]] 0.5 µM 0.207× (z -19.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 64.1 | 5 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +16.9) | [[Belinostat (drug)]] 5 µM 0.402× (z -10.5) |
| [[LS 180 (line)]] | wt | 63.5 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +14.0) | — |
| [[NCI-H23 (line)]] | alt | 82.7 | 6 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +14.2) | [[Belinostat (drug)]] 5 µM 0.444× (z -9.4) |
| [[Panc 03.27 (line)]] | alt | 115 | 5 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +17.0) | [[Belinostat (drug)]] 5 µM 0.535× (z -9.2) |
| [[SW480 (line)]] | alt | 44.6 | 7 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.61× (z +12.0) | — |
| [[C32 (line)]] | wt | 75.9 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.77× (z +21.7) | — |
| [[J82 (line)]] | alt | 70.9 | 3 | 3 | [[Homoharringtonine (drug)]] 5 µM 3.62× (z +21.4) | [[Belinostat (drug)]] 5 µM 0.435× (z -9.8) |
| [[NCI-H1792 (line)]] | alt | 79.1 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.16× (z +18.4) | — |
| [[A498 (line)]] | wt | 59.9 | 4 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.63× (z +30.9) | [[Panobinostat (drug)]] 5 µM 0.548× (z -8.6) |
| [[A549 (line)]] | wt | 48.9 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.33× (z +26.2) | — |
| [[BT-474 (line)]] | alt | 118 | 4 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +13.2) | [[Panobinostat (drug)]] 0.5 µM 0.413× (z -10.4) |
| [[MIA PaCa-2 (line)]] | alt | 61.1 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +17.0) | — |
| [[NCI-H2347 (line)]] | alt | 58.4 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +16.6) | — |
| [[NCI-H2030 (line)]] | alt | 37.3 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.34× (z +17.6) | — |
| [[SNU-423 (line)]] | alt | 44.7 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.95× (z +17.1) | — |
| [[CFPAC-1 (line)]] | alt | 51.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.38× (z +18.7) | — |
| [[Hs 766T (line)]] | wt | 48.0 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +13.4) | — |
| [[hTERT-HPNE (line)]] | wt | 66.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.56× (z +18.1) | — |
| [[KATO III (line)]] | alt | 61.8 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.49× (z +10.4) | — |
| [[RPMI-7951 (line)]] | alt | 72.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +13.9) | — |
| [[AsPC-1 (line)]] | alt | 69.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +12.9) | — |
| [[HT-29 (line)]] | alt | 57.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +10.3) | — |
| [[SHP-77 (line)]] | alt | 116 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +9.0) | [[Panobinostat (drug)]] 5 µM 0.481× (z -8.5) |
| [[SNU-1 (line)]] | wt | 65.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.179× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW 1088 (line)]] | alt | 60.8 | 0 | 2 | — | [[Tazarotene (drug)]] 0.05 µM 0.0686× (z -9.1) |
| [[SW48 (line)]] | wt | 69.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +11.1) | — |
| [[H4 (line)]] | wt | 73.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +12.4) | — |
| [[HCT15 (line)]] | alt | 97.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +12.4) | — |
| [[HepG2_C3A (line)]] | wt | 67.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +11.8) | — |
| [[RKO (line)]] | wt | 78.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +9.7) | — |
| [[SW 900 (line)]] | alt | 33.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +10.5) | — |
| [[SW1417 (line)]] | alt | 52.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +9.7) | — |
| [[AN3 CA (line)]] | alt | 77.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 90.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 110 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 51.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 70.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 69.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 54.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 150 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10260), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBQLN2]] | +0.79 | +0.78 / +0.69 | both halves | 7e-06 |  |
| [[FAM200A]] | +0.77 | +0.76 / +0.63 | both halves | 7e-06 |  |
| [[ZNF764]] | +0.76 | +0.75 / +0.60 | both halves | 7e-06 | same gene group |
| [[SON]] | +0.75 | +0.72 / +0.60 | both halves | 7e-06 |  |
| [[ZBTB6]] | +0.75 | +0.74 / +0.75 | both halves | 7e-06 | same gene group |
| [[C11orf58]] | +0.73 | +0.80 / +0.47 | both halves | 2e-05 |  |
| [[THAP1]] | +0.73 | +0.69 / +0.58 | both halves | 7e-06 |  |
| [[TAF7]] | +0.71 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[MIER3]] | +0.71 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[HNRNPH2]] | +0.71 | +0.72 / +0.68 | both halves | 7e-06 |  |
| [[THUMPD1]] | +0.70 | +0.74 / +0.75 | both halves | 7e-06 |  |
| [[TRIP11]] | +0.70 | +0.75 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAR1]] | -0.68 | -0.64 / -0.58 | both halves | 7e-06 |  |
| [[TCF3]] | -0.67 | -0.61 / -0.51 | both halves | 1e-05 |  |
| [[WASF3]] | -0.66 | -0.58 / -0.46 | both halves | 3e-05 |  |
| [[ABHD12]] | -0.66 | -0.63 / -0.58 | both halves | 7e-06 |  |
| [[ZDHHC9]] | -0.66 | -0.67 / -0.53 | both halves | 1e-05 |  |
| [[TMEM120B]] | -0.65 | -0.63 / -0.46 | both halves | 3e-05 |  |
| [[CCNY]] | -0.65 | -0.69 / -0.48 | both halves | 2e-05 |  |
| [[RAP1A]] | -0.65 | -0.65 / -0.52 | both halves | 1e-05 |  |
| [[LPCAT4]] | -0.65 | -0.64 / -0.44 | both halves | 3e-05 |  |
| [[TNK2]] | -0.63 | -0.53 / -0.39 | both halves | 5e-05 |  |
| [[METAP1]] | -0.63 | -0.68 / -0.39 | both halves | 5e-05 |  |
| [[ANKRD27]] | -0.63 | -0.58 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises ZNF24's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.635). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-30.1, 12.3); signed map (4.9, -28.1). **Vector** length 103, 29.9% of its response variance represented; |z| ≥ 3 in 1,248 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +9.7 | +23.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +8.2 | +13.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +7.9 | +10.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.8 | +32.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +7.6 | +15.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.9 | +6.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.8 | +1.3 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.9 | +3.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.9 | -0.4 |
| fall | [[Belinostat (drug)]] 5 µM |  | -6.6 | -13.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | -6.0 | -14.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -5.0 | -12.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.7 | -0.8 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.4 | -8.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.6 | -4.9 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.4 | -0.6 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.3 | -0.0 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -2.0 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger protein 24 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q12.2 — chr18:35,332,227-35,345,482 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ZSCAN3, Zfp191, KOX17; previously ZNF191 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; SCAN domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [P17028](https://www.uniprot.org/uniprotkb/P17028) (Zinc finger protein 24):

> Transcription factor required for myelination of differentiated oligodendrocytes. Required for the conversion of oligodendrocytes from the premyelinating to the myelinating state. In the developing central nervous system (CNS), involved in the maintenance in the progenitor stage by promoting the cell cycle. Specifically binds to the 5'-TCAT-3' DNA sequence (By similarity). Has transcription repressor activity in vitro.

**Summary**, from NCBI Gene [7572](https://www.ncbi.nlm.nih.gov/gene/7572):

> Enables DNA-binding transcription activator activity, RNA polymerase II-specific; identical protein binding activity; and sequence-specific DNA binding activity. Involved in negative regulation of DNA-templated transcription and positive regulation of transcription by RNA polymerase II. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:13032](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13032) · Entrez [7572](https://www.ncbi.nlm.nih.gov/gene/7572) · UniProt [P17028](https://www.uniprot.org/uniprotkb/P17028) · Ensembl [ENSG00000172466](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172466)

## Data

Gene col 10260: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10260); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10260, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10260]; `tensor/DDL_lfc|DDL_z.npy` [10260]; `embed/gene_vectors.npy` [10260]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10260 or target_col == 10260). Every well: [[ZNF24 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNF24.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
