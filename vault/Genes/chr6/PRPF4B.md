---
symbol: "PRPF4B"
type: "gene"
col: 3400
ensembl_id: "ENSG00000112739"
name: "pre-mRNA processing factor kinase PRP4K"
location: "6p25.2"
module: 184
arm: "-"
pooled_cpm: 146.92
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 4
n_dd_up_clean: 11
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/184"]
generated_by: "tahoemap"
---

# PRPF4B

*pre-mRNA processing factor kinase PRP4K* — 6p25.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.96× (z +23.5, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.682× (z -13.4, q 3e-38, down in 41 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SREK1]] (+0.74, fdr 7e-06), [[SRSF11]] (+0.69, fdr 1e-05, ⚠ SRSF11 in the vector space only through flagged drug-doses), [[LUC7L3]] (+0.63, fdr 1e-05), [[RBM26]] (+0.60, fdr 1e-05); moves opposite to [[RELL2]] (-0.62, fdr 3e-05), [[KCTD5]] (-0.61, fdr 7e-05), [[RHOC]] (-0.57, fdr 1e-05).
> It sits in the **-** arm of [[Module 184]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3400.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.96×** | +23.5 | 0e+00 | 47/48 (LoVo, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.23×** | +19.8 | 0e+00 | 48/48 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.04×** | +17.7 | 0e+00 | 48/48 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.46×** | +16.0 | 0e+00 | 48/49 (SW480, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.73×** | +13.6 | 6e-40 | 42/48 (HEC-1-A, SW480, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.73×** | +13.5 | 1e-39 | 47/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.70×** | +13.2 | 9e-38 | 47/48 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.74×** | +13.0 | 6e-37 | 44/48 (SW480, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.61×** | +11.3 | 1e-27 | 43/47 (LoVo, NCI-H23, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.46×** | +9.1 | 8e-18 | 39/48 (NCI-H1573, SW480, …) | top dose only | composition shift |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.34×** | +7.2 | 2e-11 | 30/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.32×** | +6.8 | 5e-10 | 32/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.30×** | +6.4 | 5e-09 | 35/48 (PANC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **1.24×** | +5.3 | 4e-06 | 29/48 (SW 900, SW480, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.22×** | +5.0 | 2e-05 | 25/48 (PANC-1, SK-MEL-2, …) | rises with dose |  |
| [[Entecavir (monohydrate) (drug)]] 0.5 µM |  | 1.17× | +4.0 | 0.002 | 17/49 (HOP62, PANC-1, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.14× | +3.0 | 0.071 | 18/47 (SW48, HEC-1-A, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 6 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3400.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.682×** | -13.4 | 3e-38 | 41/49 (SW480, HT-29, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.897× | -9.4 | 2e-18 | 1/50 (NCI-H23) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.797×** | -5.6 | 4e-06 | 29/48 (HEC-1-A, HT-29, …) | top dose only |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **0.826×** | -4.7 | 3e-04 | 24/48 (KATO III, BT-474, …) | inconsistent across doses | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.840× | -4.3 | 0.002 | 23/48 (KATO III, SW480, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.843× | -4.2 | 0.002 | 22/48 (SW480, KATO III, …) | all doses, flat |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.849× | -4.0 | 0.004 | 19/48 (SW480, KATO III, …) | rises with dose |  |
| [[OTS514 (drug)]] 5 µM |  | **0.740×** | -3.9 | 0.007 | 25/46 (SNU-1, SHP-77, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Filgotinib (drug)]] 0.05 µM |  | 0.857× | -3.8 | 0.008 | 10/48 (AsPC-1, HOP62, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.867× | -3.5 | 0.023 | 16/48 (SW480, KATO III, …) | all doses, flat |  |
| [[Bicalutamide (drug)]] 0.05 µM |  | 0.880× | -3.2 | 0.079 | 8/48 (HEC-1-A, SW 1088, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 0.5 µM |  | 0.881× | -3.1 | 0.080 | 13/48 (HCT15, Hs 766T, …) | two highest doses |  |
| [[Pimozide (drug)]] 0.5 µM | ⚠ transcription drop | 0.885× | -3.0 | 0.10 | 9/48 (C-33 A, AN3 CA, …) | inconsistent across doses | position effect removed |
| [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM |  | 0.885× | -3.0 | 0.10 | 8/48 (Hs 766T, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Diphenhydramine (drug)]] 0.5 µM |  | 0.886× | -3.0 | 0.10 | 5/48 (HEC-1-A, J82, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3400. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 171 | 11 (3 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +18.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.590× (z -15.0) |
| [[LoVo (line)]] | wt | 133 | 11 (4 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +23.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.565× (z -14.2) |
| [[PANC-1 (line)]] | alt | 156 | 12 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.88× (z +18.7) | — |
| [[NCI-H460 (line)]] | wt | 106 | 10 (3 ⚠) | 1 | [[Digitoxin (drug)]] 5 µM 2.97× (z +16.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.75× (z +15.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.543× (z -12.8) |
| [[KATO III (line)]] | alt | 159 | 8 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.37× (z +18.4) | [[Panobinostat (drug)]] 0.5 µM 0.459× (z -11.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 178 | 10 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +18.6) | — |
| [[HT-29 (line)]] | alt | 153 | 6 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +14.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.534× (z -14.7) |
| [[NCI-H1573 (line)]] | alt | 92.4 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +21.1) | — |
| [[HEC-1-A (line)]] | alt | 140 | 6 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +20.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.604× (z -11.5) |
| [[LOX-IMVI (line)]] | wt | 193 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +18.4) | — |
| [[LS 180 (line)]] | wt | 165 | 7 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.41× (z +18.1) | — |
| [[Panc 03.27 (line)]] | alt | 171 | 6 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +12.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.588× (z -10.4) |
| [[RKO (line)]] | wt | 160 | 6 (1 ⚠) | 1 | [[TAK-901 (drug)]] 5 µM 5.01× (z +11.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.521× (z -12.1) |
| [[SW48 (line)]] | wt | 176 | 6 (1 ⚠) | 1 | [[TAK-901 (drug)]] 0.05 µM 3.64× (z +13.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.538× (z -9.9) |
| [[BT-474 (line)]] | alt | 152 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +12.4) | — |
| [[COLO 205 (line)]] | alt | 157 | 4 (1 ⚠) | 1 | [[TAK-901 (drug)]] 5 µM 7.12× (z +12.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.575× (z -9.8) |
| [[HOP62 (line)]] | alt | 149 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +16.4) | — |
| [[Hs 766T (line)]] | wt | 101 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +12.0) | — |
| [[J82 (line)]] | alt | 200 | 5 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.33× (z +12.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 166 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +18.9) | — |
| [[NCI-H1792 (line)]] | alt | 98.7 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.85× (z +22.8) | — |
| [[SNU-1 (line)]] | wt | 171 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.87× (z +11.7) | — |
| [[AsPC-1 (line)]] | alt | 118 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +15.9) | — |
| [[C-33 A (line)]] | alt | 181 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.34× (z +10.3) | — |
| [[CFPAC-1 (line)]] | alt | 149 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +13.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.575× (z -11.6) |
| [[NCI-H2030 (line)]] | alt | 203 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +11.5) | — |
| [[SW1417 (line)]] | alt | 154 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +12.9) | — |
| [[A-172 (line)]] | wt | 118 | 2 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.67× (z +10.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.580× (z -10.9) |
| [[C32 (line)]] | wt | 109 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +14.1) | — |
| [[HCT15 (line)]] | alt | 191 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.21× (z +10.8) | — |
| [[HepG2_C3A (line)]] | wt | 177 | 3 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.54× (z +11.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.87× (z +11.0) | — |
| [[SNU-423 (line)]] | alt | 176 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +13.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.513× (z -12.8) |
| [[A-427 (line)]] | wt | 146 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 4.04× (z +10.7) | — |
| [[A498 (line)]] | wt | 112 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +17.7) | — |
| [[HS-578T (line)]] | alt | 129 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +17.9) | — |
| [[hTERT-HPNE (line)]] | wt | 120 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +11.8) | — |
| [[NCI-H2347 (line)]] | alt | 151 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.94× (z +10.7) | — |
| [[RPMI-7951 (line)]] | alt | 146 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +14.5) | — |
| [[SK-MEL-2 (line)]] | alt | 119 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +13.1) | [[Dinaciclib (drug)]] 0.5 µM 0.478× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW 900 (line)]] | alt | 131 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.32× (z +10.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.08× (z +9.1) | — |
| [[A549 (line)]] | wt | 109 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +13.5) | — |
| [[AN3 CA (line)]] | alt | 200 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 179 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 132 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 139 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 161 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 207 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 150 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 240 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3400), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SREK1]] | +0.74 | +0.67 / +0.71 | both halves | 7e-06 | STRING 593 |
| [[SRSF11]] ⚠ | +0.69 | +0.64 / +0.56 | both halves | 1e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 702; ⚠ in the vector space only through flagged drug-doses |
| [[LUC7L3]] | +0.63 | +0.64 / +0.53 | both halves | 1e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 860 |
| [[RBM26]] | +0.60 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[SRRM1]] | +0.58 | +0.62 / +0.52 | both halves | 1e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 893 |
| [[XPA]] | +0.58 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[PUM2]] | +0.58 | +0.43 / +0.63 | both halves | 3e-05 |  |
| [[NAPEPLD]] | +0.58 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[PNISR]] | +0.57 | +0.56 / +0.45 | both halves | 3e-05 | STRING 690 |
| [[SSB]] | +0.56 | +0.44 / +0.52 | both halves | 3e-05 |  |
| [[LUC7L2]] | +0.56 | +0.50 / +0.47 | both halves | 2e-05 | STRING 458 |
| [[MTARC2]] | +0.56 | +0.39 / +0.55 | both halves | 5e-05 |  |
| [[ABCB7]] | +0.56 | +0.24 / +0.65 | both halves | 4e-04 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RELL2]] | -0.62 | -0.43 / -0.59 | both halves | 3e-05 |  |
| [[KCTD5]] | -0.61 | -0.38 / -0.65 | both halves | 7e-05 |  |
| [[RHOC]] | -0.57 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[ORMDL2]] | -0.55 | -0.44 / -0.52 | both halves | 3e-05 |  |
| [[PSMD8]] | -0.54 | -0.43 / -0.57 | both halves | 3e-05 |  |
| [[MAPK7]] | -0.52 | -0.39 / -0.48 | both halves | 6e-05 |  |
| [[FAM219A]] | -0.52 | -0.35 / -0.57 | both halves | 1e-04 |  |
| [[LRRC8A]] | -0.51 | -0.29 / -0.59 | both halves | 3e-04 |  |
| [[MEA1]] | -0.51 | -0.55 / -0.39 | both halves | 6e-05 |  |
| [[TINF2]] | -0.51 | -0.38 / -0.47 | both halves | 6e-05 |  |
| [[MYO9B]] | -0.50 | -0.35 / -0.60 | both halves | 1e-04 |  |
| [[CAP1]] | -0.50 | -0.40 / -0.54 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 184]]; 20 genes; this gene is in the **-** arm (projection on the module's main direction -0.671). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.39).
- **Nodal map** (x, y) = (-19.9, -3.7); signed map (11.3, -37.0). **Vector** length 81.3, 24.5% of its response variance represented; |z| ≥ 3 in 1,187 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +4.5 | +23.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.4 | -0.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +4.4 | +1.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.3 | -0.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.3 | -1.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.3 | -1.8 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +3.0 | -1.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.8 | -1.0 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.6 | -2.2 |
| fall | [[Auranofin (drug)]] 5 µM |  | -6.7 | -5.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.8 | -13.4 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.9 | +1.4 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -3.0 | -9.4 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -3.0 | -0.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.6 | +5.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.2 | -2.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.1 | -0.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.0 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | pre-mRNA processing factor kinase PRP4K |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p25.2 — chr6:4,021,267-4,064,983 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Prp4, PR4H, KIAA0536, Prp4B; previously PRPF4B |
| Hallmark sets | G2M_CHECKPOINT |
| Reactome | 4 pathways, smallest: mRNA Splicing - Major Pathway; mRNA Splicing; Processing of Capped Intron-Containing Pre-mRNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13523](https://www.uniprot.org/uniprotkb/Q13523) (Serine/threonine-protein kinase PRP4 homolog):

> Serine/threonine kinase involved in spliceosomal assembly as well as mitosis and signaling regulation. Connects chromatin mediated regulation of transcription and pre-mRNA splicing. During spliceosomal assembly, interacts with and phosphorylates PRPF6 and PRPF31, components of the U4/U6-U5 tri-small nuclear ribonucleoprotein (snRNP), to facilitate the formation of the spliceosome B complex. Plays a role in regulating transcription and the spindle assembly checkpoint (SAC). Associates with U5 …

**Summary**, from NCBI Gene [8899](https://www.ncbi.nlm.nih.gov/gene/8899):

> Pre-mRNA splicing occurs in two sequential transesterification steps, and the protein encoded by this gene is thought to be involved in pre-mRNA splicing and in signal transduction. This protein belongs to a kinase family that includes serine/arginine-rich protein-specific kinases and cyclin-dependent kinases (CDKs). This protein is regarded as a CDK-like kinase (Clk) with homology to mitogen-activated protein kinases (MAPKs). [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:17346](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17346) · Entrez [8899](https://www.ncbi.nlm.nih.gov/gene/8899) · UniProt [Q13523](https://www.uniprot.org/uniprotkb/Q13523) · Ensembl [ENSG00000112739](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000112739)

## Data

Gene col 3400: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3400); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3400, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3400]; `tensor/DDL_lfc|DDL_z.npy` [3400]; `embed/gene_vectors.npy` [3400]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3400 or target_col == 3400). Every well: [[PRPF4B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRPF4B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
