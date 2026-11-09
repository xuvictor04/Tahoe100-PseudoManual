---
symbol: "PIK3C3"
type: "gene"
col: 1212
ensembl_id: "ENSG00000078142"
name: "phosphatidylinositol 3-kinase catalytic subunit type 3"
location: "18q12.3"
module: 76
arm: "+"
pooled_cpm: 111.4
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 10
n_dd_up_clean: 17
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/076"]
generated_by: "tahoemap"
---

# PIK3C3

*phosphatidylinositol 3-kinase catalytic subunit type 3* — 18q12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (4 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.67× (z +10.6, q 2e-23, up in 42 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.431× (z -13.6, q 2e-39, down in 43 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.782× (z -5.6, q 2e-06, down in 31 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TNKS]] (+0.73, fdr 7e-06), [[CALCOCO1]] (+0.63, fdr 7e-06), [[HMBOX1]] (+0.59, fdr 1e-05); moves opposite to [[FAM171A1]] (-0.52, fdr 3e-05), [[PPRC1]] (-0.52, fdr 1e-05), [[OSBPL11]] (-0.51, fdr 4e-05).
> It is in [[Module 076]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1212.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.67×** | +10.6 | 2e-23 | 42/49 (LoVo, NCI-H23, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **3.36×** | +9.9 | 2e-20 | 46/48 (RKO, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.82×** | +9.6 | 1e-19 | 43/48 (BT-474, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.45×** | +6.0 | 3e-07 | 35/48 (BT-474, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.45×** | +6.0 | 3e-07 | 32/48 (BT-474, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.43×** | +5.8 | 6e-07 | 32/48 (NCI-H1573, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.29×** | +5.7 | 8e-07 | 28/48 (NCI-H1573, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.45×** | +5.6 | 1e-06 | 39/48 (PANC-1, HT-29, …) | all doses, flat | cell-cycle shift (explains ~13% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.40×** | +5.4 | 5e-06 | 36/48 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.39×** | +5.3 | 5e-06 | 30/48 (BT-474, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.26×** | +5.3 | 6e-06 | 29/48 (A-427, A498, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.35×** | +4.9 | 5e-05 | 35/48 (PANC-1, HT-29, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.74×** | +4.5 | 3e-04 | 40/49 (RKO, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.30×** | +4.2 | 1e-03 | 35/48 (A498, SW1417, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.25×** | +3.6 | 0.010 | 26/48 (A498, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Verteporfin (drug)]] 5 µM |  | **1.22×** | +3.1 | 0.072 | 18/49 (SW 900, SNU-423, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.21×** | +3.0 | 0.077 | 22/47 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Sapanisertib (drug)]] 5 µM |  | **1.44×** | +3.0 | 0.083 | 17/49 (MIA PaCa-2, NCI-H2030, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 7 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1212.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.431×** | -13.6 | 2e-39 | 43/49 (NCI-H2347, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.438×** | -12.8 | 5e-35 | 41/44 (hTERT-HPNE, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.602×** | -7.6 | 7e-12 | 36/45 (LOX-IMVI, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.660×** | -6.5 | 2e-08 | 38/47 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.782×** | -5.6 | 2e-06 | 31/49 (SNU-423, A-172, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.741×** | -4.8 | 1e-04 | 29/48 (A498, LoVo, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.743×** | -4.8 | 1e-04 | 38/48 (MIA PaCa-2, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.813×** | -4.7 | 2e-04 | 26/48 (C32, HepG2/C3A, …) | rises with dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.648×** | -3.5 | 0.025 | 26/48 (LoVo, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | 0.862× | -3.4 | 0.039 | 12/48 (PANC-1, MIA PaCa-2, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~28% of this change | **0.819×** | -3.2 | 0.063 | 24/48 (NCI-H2347, PANC-1, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1212. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 110 | 8 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 5.60× (z +17.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 5.07× (z +16.7) | — |
| [[NCI-H460 (line)]] | wt | 111 | 6 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.63× (z +16.5) | [[Dinaciclib (drug)]] 5 µM 0.369× (z -10.4) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 68.1 | 6 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.36× (z +15.2) | [[Dinaciclib (drug)]] 5 µM 0.470× (z -9.1) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 190 | 2 | 4 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 5.26× (z +9.9) | [[Dinaciclib (drug)]] 0.5 µM 0.383× (z -11.3) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 92.2 | 5 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +14.4) | [[Dinaciclib (drug)]] 5 µM 0.230× (z -14.2) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 112 | 4 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.70× (z +13.8) | [[Dinaciclib (drug)]] 5 µM 0.260× (z -11.6) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 104 | 2 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 5.09× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.377× (z -10.4) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 143 | 1 | 4 (3 ⚠) | [[PH-797804 (drug)]] 5 µM 4.15× (z +8.6) | [[Dinaciclib (drug)]] 0.05 µM 0.294× (z -13.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.526× (z -10.9) |
| [[NCI-H1792 (line)]] | alt | 177 | 3 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.79× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.230× (z -14.6) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 60.8 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +10.1) | — |
| [[hTERT-HPNE (line)]] | wt | 172 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.158× (z -15.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.438× (z -10.2) |
| [[NCI-H23 (line)]] | alt | 155 | 3 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.70× (z +10.7) | [[Dinaciclib (drug)]] 0.5 µM 0.483× (z -8.9) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 153 | 2 | 2 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 7.26× (z +10.2) | [[Dinaciclib (drug)]] 0.5 µM 0.328× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.552× (z -8.7) |
| [[SK-MEL-2 (line)]] | alt | 194 | 1 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.220× (z -15.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.555× (z -8.6) |
| [[AsPC-1 (line)]] | alt | 155 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.97× (z +11.7) | [[Dinaciclib (drug)]] 5 µM 0.289× (z -12.9) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 103 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.239× (z -14.8) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 146 | 2 | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 6.09× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.401× (z -8.6) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 142 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.15× (z +8.9) | [[Dinaciclib (drug)]] 0.5 µM 0.423× (z -9.9) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 78.4 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 6.71× (z +11.0) | — |
| [[NCI-H2347 (line)]] | alt | 102 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.242× (z -16.7) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 137 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.41× (z +10.7) | [[Dinaciclib (drug)]] 0.5 µM 0.194× (z -14.4) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 68.0 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.69× (z +8.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.568× (z -9.2) |
| [[C32 (line)]] | wt | 196 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.317× (z -11.3) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 207 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.194× (z -11.5) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 176 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.193× (z -13.4) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 89.2 | 1 | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 4.82× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.442× (z -8.8) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 119 | 1 | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 6.09× (z +8.8) | [[Dinaciclib (drug)]] 0.5 µM 0.362× (z -9.9) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 110 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +11.5) | [[Dinaciclib (drug)]] 5 µM 0.290× (z -13.1) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 81.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.275× (z -13.5) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 115 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.473× (z -11.1) |
| [[A-427 (line)]] | wt | 63.3 | 1 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.86× (z +9.9) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H661 (line)]] | alt | 68.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0836× (z -10.6) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 159 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.327× (z -11.6) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 183 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.431× (z -9.3) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 135 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.433× (z -12.3) |
| [[SW 1088 (line)]] | alt | 127 | 0 | 1 | — | [[Simotinib (drug)]] 0.05 µM 0.0914× (z -8.5) |
| [[SW 900 (line)]] | alt | 67.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.141× (z -15.5) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 115 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.251× (z -10.0) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 68.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 142 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 88.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 179 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 65.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 94.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 111 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 55.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 168 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 70.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1212), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TNKS]] | +0.73 | +0.64 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[CALCOCO1]] | +0.63 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[HMBOX1]] | +0.59 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[ATG14]] | +0.58 | +0.48 / +0.61 | both halves | 2e-05 | same gene group; pathway: Antigen Presentation: Folding, assembly and peptide loading of class I MHC; STRING 999 |
| [[BMT2]] | +0.58 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[PPHLN1]] | +0.56 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[CRIPT]] | +0.56 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[CNOT2]] | +0.55 | +0.48 / +0.66 | both halves | 2e-05 |  |
| [[CCDC28A]] | +0.54 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[MRPL13]] | +0.53 | +0.41 / +0.54 | both halves | 4e-05 |  |
| [[DHX40]] | +0.53 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[SERINC1]] | +0.52 | +0.49 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM171A1]] | -0.52 | -0.57 / -0.43 | both halves | 3e-05 |  |
| [[PPRC1]] | -0.52 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[OSBPL11]] | -0.51 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[SMARCA4]] | -0.50 | -0.60 / -0.40 | both halves | 5e-05 |  |
| [[SRF]] | -0.47 | -0.59 / -0.40 | both halves | 5e-05 | pathway: RHO GTPase Effectors |
| [[CYCS]] | -0.46 | -0.36 / -0.51 | both halves | 1e-04 | STRING 446 |
| [[RIPK1]] | -0.46 | -0.46 / -0.39 | both halves | 5e-05 | pathway: Dengue Virus-Host Interactions |
| [[AKIRIN1]] | -0.44 | -0.49 / -0.36 | both halves | 1e-04 |  |
| [[RBBP8]] | -0.44 | -0.36 / -0.45 | both halves | 1e-04 |  |
| [[TASOR2]] | -0.43 | -0.37 / -0.49 | both halves | 8e-05 |  |
| [[CTPS1]] | -0.43 | -0.48 / -0.37 | both halves | 9e-05 |  |
| [[ANAPC7]] | -0.43 | -0.51 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 076]]; 59 genes; every member is in the + arm (projection on the module's main direction 0.556). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-13.8, -12.4); signed map (-18.6, 7.4). **Vector** length 92.9, 32.1% of its response variance represented; |z| ≥ 3 in 1,141 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | +8.7 | +5.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.1 | +1.8 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +5.0 | +4.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.5 | -13.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.1 | -12.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.0 | -0.3 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +3.1 | -0.9 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.7 | -0.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.4 | +3.1 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -7.1 | -4.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -5.2 | -4.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -5.2 | -0.9 |
|  | [[venetoclax (drug)]] 5 µM |  | -4.0 | -3.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -3.8 | -6.5 |
|  | [[EX229 (drug)]] 5 µM |  | -3.7 | -2.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.6 | -3.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.3 | -2.1 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -3.0 | +0.2 |

## What is on record

|  |  |
|---|---|
| Name | phosphatidylinositol 3-kinase catalytic subunit type 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q12.3 — chr18:41,955,234-42,087,830 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Vps34, hVps34 |
| Gene groups (HGNC) | Phosphatidylinositol 3-kinase family; PIK3C3 complex subunits |
| Reactome | 38 pathways, smallest: Synthesis of PIPs at the late endosome membrane; Translation of Replicase and Assembly of the Replication Transcription Complex_9679504; Translation of Replicase and Assembly of the Replication Transcription Complex_9694676 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NEB9](https://www.uniprot.org/uniprotkb/Q8NEB9) (Phosphatidylinositol 3-kinase catalytic subunit type 3):

> Catalytic subunit of the PI3K complex that mediates formation of phosphatidylinositol 3-phosphate; different complex forms are believed to play a role in multiple membrane trafficking pathways: PI3KC3-C1 is involved in initiation of autophagosomes and PI3KC3-C2 in maturation of autophagosomes and endocytosis. As part of PI3KC3-C1, promotes endoplasmic reticulum membrane curvature formation prior to vesicle budding. Involved in regulation of degradative endocytic trafficking and required for the …

**Summary**, from NCBI Gene [5289](https://www.ncbi.nlm.nih.gov/gene/5289):

> Enables 1-phosphatidylinositol-3-kinase activity. Involved in several processes, including early endosome to late endosome transport; macroautophagy; and positive regulation of natural killer cell mediated cytotoxicity. Acts upstream of or within autophagy and positive regulation of protein lipidation. Located in autolysosome; late endosome; and midbody. Is active in plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:8974](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8974) · Entrez [5289](https://www.ncbi.nlm.nih.gov/gene/5289) · UniProt [Q8NEB9](https://www.uniprot.org/uniprotkb/Q8NEB9) · Ensembl [ENSG00000078142](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000078142)

## Data

Gene col 1212: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1212); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1212, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1212]; `tensor/DDL_lfc|DDL_z.npy` [1212]; `embed/gene_vectors.npy` [1212]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1212 or target_col == 1212). Every well: [[PIK3C3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PIK3C3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
