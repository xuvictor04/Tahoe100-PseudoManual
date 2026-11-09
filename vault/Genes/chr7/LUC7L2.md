---
symbol: "LUC7L2"
type: "gene"
col: 7136
ensembl_id: "ENSG00000146963"
name: "LUC7 like 2, pre-mRNA splicing factor"
location: "7q34"
module: 184
arm: "-"
pooled_cpm: 224.13
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 17
n_dd_up_clean: 7
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/184"]
generated_by: "tahoemap"
---

# LUC7L2

*LUC7 like 2, pre-mRNA splicing factor* — 7q34

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.37× (z +15.7, q 0e+00, up in 47 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.330× (z -27.4, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPRD1B]] (+0.66, fdr 1e-05), [[ZZZ3]] (+0.65, fdr 7e-06), [[SREK1]] (+0.65, fdr 1e-05); moves opposite to [[KDM7A]] (-0.60, fdr 3e-05), [[NRIP3]] (-0.59, fdr 3e-05), [[CBL]] (-0.59, fdr 1e-04).
> It sits in the **-** arm of [[Module 184]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7136.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.37×** | +15.7 | 0e+00 | 47/49 (NCI-H460, COLO 205, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.71×** | +12.9 | 1e-35 | 47/48 (C32, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.38×** | +7.9 | 5e-13 | 44/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.36×** | +7.6 | 6e-12 | 35/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.29×** | +6.3 | 3e-08 | 31/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.28×** | +6.2 | 5e-08 | 35/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.27×** | +5.7 | 1e-06 | 27/47 (LoVo, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.23×** | +5.2 | 2e-05 | 25/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +4.1 | 0.003 | 19/47 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 1.18× | +4.0 | 0.003 | 18/48 (AsPC-1, Panc 03.27, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[GSK1059615 (drug)]] 5 µM |  | **1.33×** | +3.7 | 0.009 | 26/49 (A498, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | 1.27× | +3.1 | 0.10 | 22/47 (HepG2/C3A, C32, …) | top dose only | cell-cycle shift (explains ~8% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7136.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.330×** | -27.4 | 0e+00 | 48/48 (AsPC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.368×** | -24.7 | 0e+00 | 48/48 (AsPC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.368×** | -24.7 | 0e+00 | 48/48 (AsPC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.507×** | -16.8 | 0e+00 | 48/48 (AsPC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.611×** | -12.2 | 5e-32 | 47/48 (A498, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.652×** | -10.6 | 4e-24 | 43/48 (SW480, SW48, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.747×** | -10.2 | 2e-22 | 44/48 (SW480, C32, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.669×** | -9.5 | 1e-19 | 39/50 (C32, SW48, …) | inconsistent across doses | cell-cycle shift (explains ~20% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.775×** | -8.9 | 5e-17 | 32/49 (A498, NCI-H23, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.689×** | -8.9 | 5e-17 | 39/48 (hTERT-HPNE, C32, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.541×** | -7.9 | 1e-13 | 47/49 (AsPC-1, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.835× | -6.3 | 1e-08 | 25/48 (SNU-1, NCI-H2347, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change | **0.787×** | -5.9 | 2e-07 | 33/49 (C32, AsPC-1, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | **0.787×** | -5.7 | 6e-07 | 32/47 (MIA PaCa-2, NCI-H2347, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.803×** | -5.4 | 3e-06 | 32/49 (SW480, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 5 µM |  | 0.847× | -3.9 | 0.002 | 17/47 (NCI-H460, HOP62, …) | rises with dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.822×** | -3.4 | 0.016 | 21/48 (SW 900, HT-29, …) | all doses, flat | low cells (technical?); noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.826×** | -3.4 | 0.021 | 21/47 (SW48, SNU-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7136. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 210 | 8 (2 ⚠) | 8 (1 ⚠) | [[Digitoxin (drug)]] 0.5 µM 2.80× (z +19.1) | [[Panobinostat (drug)]] 5 µM 0.328× (z -20.7) |
| [[C32 (line)]] | wt | 565 | 3 | 11 (3 ⚠) | [[PH-797804 (drug)]] 5 µM 7.47× (z +15.2) | [[Panobinostat (drug)]] 5 µM 0.297× (z -17.6) |
| [[PANC-1 (line)]] | alt | 233 | 6 (1 ⚠) | 6 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.18× (z +14.0) | [[Panobinostat (drug)]] 5 µM 0.320× (z -20.5) |
| [[SW480 (line)]] | alt | 289 | 2 | 9 | [[TAK-901 (drug)]] 5 µM 4.33× (z +14.4) | [[Panobinostat (drug)]] 5 µM 0.335× (z -20.5) |
| [[SW48 (line)]] | wt | 291 | 3 | 7 (1 ⚠) | [[TAK-901 (drug)]] 0.05 µM 3.70× (z +15.7) | [[Panobinostat (drug)]] 5 µM 0.259× (z -17.2) |
| [[LoVo (line)]] | wt | 269 | 3 (1 ⚠) | 6 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.78× (z +14.6) | [[Panobinostat (drug)]] 5 µM 0.335× (z -19.5) |
| [[NCI-H1792 (line)]] | alt | 205 | 4 (1 ⚠) | 5 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 1.97× (z +10.2) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 3.58× (z +10.0) | [[Belinostat (drug)]] 5 µM 0.292× (z -18.4) |
| [[COLO 205 (line)]] | alt | 188 | 3 (1 ⚠) | 5 | [[TAK-901 (drug)]] 5 µM 7.96× (z +14.9) | [[Panobinostat (drug)]] 5 µM 0.374× (z -13.5) |
| [[NCI-H23 (line)]] | alt | 312 | 3 | 5 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.36× (z +12.5) | [[Panobinostat (drug)]] 5 µM 0.313× (z -18.9) |
| [[Panc 03.27 (line)]] | alt | 166 | 2 | 6 | [[TAK-901 (drug)]] 5 µM 4.68× (z +12.5) | [[Panobinostat (drug)]] 0.5 µM 0.366× (z -15.6) |
| [[SW 900 (line)]] | alt | 234 | 0 | 8 | — | [[Panobinostat (drug)]] 0.5 µM 0.282× (z -18.3) |
| [[A-427 (line)]] | wt | 163 | 2 | 5 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 4.10× (z +11.4) | [[Panobinostat (drug)]] 5 µM 0.454× (z -12.2) |
| [[A498 (line)]] | wt | 310 | 0 | 7 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.291× (z -22.5) |
| [[A549 (line)]] | wt | 167 | 2 (1 ⚠) | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.63× (z +10.8) ⚠ cell-cycle shift, explains ~18% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 3.37× (z +10.0) | [[Belinostat (drug)]] 5 µM 0.318× (z -18.0) |
| [[AsPC-1 (line)]] | alt | 230 | 1 | 6 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.67× (z +10.9) | [[Panobinostat (drug)]] 5 µM 0.199× (z -26.0) |
| [[H4 (line)]] | wt | 233 | 0 | 7 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.261× (z -16.2) |
| [[HEC-1-A (line)]] | alt | 162 | 3 | 4 | [[PH-797804 (drug)]] 5 µM 4.22× (z +13.4) | [[Panobinostat (drug)]] 5 µM 0.371× (z -17.6) |
| [[HOP62 (line)]] | alt | 144 | 1 | 6 | [[TAK-901 (drug)]] 5 µM 3.16× (z +9.5) | [[Panobinostat (drug)]] 5 µM 0.322× (z -18.1) |
| [[HS-578T (line)]] | alt | 215 | 0 | 7 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.313× (z -17.4) |
| [[J82 (line)]] | alt | 185 | 2 | 5 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.03× (z +11.3) | [[Panobinostat (drug)]] 5 µM 0.304× (z -19.2) |
| [[LOX-IMVI (line)]] | wt | 164 | 3 | 4 | [[TAK-901 (drug)]] 0.05 µM 2.92× (z +14.0) | [[Panobinostat (drug)]] 5 µM 0.342× (z -14.8) |
| [[RKO (line)]] | wt | 256 | 2 | 5 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.32× (z +10.2) | [[Panobinostat (drug)]] 5 µM 0.337× (z -14.4) |
| [[RPMI-7951 (line)]] | alt | 213 | 0 | 7 | — | [[Panobinostat (drug)]] 5 µM 0.329× (z -16.3) |
| [[SK-MEL-2 (line)]] | alt | 193 | 2 | 5 | [[TAK-901 (drug)]] 5 µM 3.86× (z +10.1) | [[Panobinostat (drug)]] 5 µM 0.283× (z -18.1) |
| [[SW1417 (line)]] | alt | 328 | 2 | 5 | [[TAK-901 (drug)]] 5 µM 3.45× (z +9.8) | [[Belinostat (drug)]] 5 µM 0.304× (z -17.9) |
| [[A-172 (line)]] | wt | 126 | 2 | 4 | [[PH-797804 (drug)]] 5 µM 3.08× (z +9.6) | [[Panobinostat (drug)]] 5 µM 0.375× (z -16.0) |
| [[HT-29 (line)]] | alt | 255 | 1 | 5 | [[TAK-901 (drug)]] 5 µM 3.23× (z +9.5) | [[Panobinostat (drug)]] 5 µM 0.331× (z -17.1) |
| [[LS 180 (line)]] | wt | 198 | 2 | 4 | [[PH-797804 (drug)]] 5 µM 5.48× (z +12.4) | [[Belinostat (drug)]] 5 µM 0.376× (z -13.6) |
| [[MIA PaCa-2 (line)]] | alt | 314 | 1 | 5 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.33× (z +9.0) | [[Panobinostat (drug)]] 5 µM 0.249× (z -20.0) |
| [[NCI-H1573 (line)]] | alt | 108 | 3 (1 ⚠) | 3 | [[Digitoxin (drug)]] 5 µM 2.10× (z +10.5) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 4.09× (z +10.4) | [[Panobinostat (drug)]] 5 µM 0.438× (z -11.7) |
| [[NCI-H2030 (line)]] | alt | 233 | 3 | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.41× (z +9.7) | [[Panobinostat (drug)]] 5 µM 0.265× (z -14.6) |
| [[SNU-1 (line)]] | wt | 293 | 1 | 5 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.42× (z +9.2) | [[Panobinostat (drug)]] 5 µM 0.313× (z -13.8) |
| [[Hs 766T (line)]] | wt | 223 | 1 | 4 | [[TAK-901 (drug)]] 5 µM 4.09× (z +11.4) | [[Panobinostat (drug)]] 5 µM 0.383× (z -14.9) |
| [[hTERT-HPNE (line)]] | wt | 162 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.330× (z -14.8) |
| [[KATO III (line)]] | alt | 247 | 1 | 4 | [[TAK-901 (drug)]] 5 µM 3.16× (z +9.6) | [[Panobinostat (drug)]] 5 µM 0.347× (z -17.0) |
| [[NCI-H2347 (line)]] | alt | 212 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.284× (z -18.2) |
| [[SNU-423 (line)]] | alt | 168 | 0 | 5 | — | [[Belinostat (drug)]] 5 µM 0.366× (z -15.4) |
| [[C-33 A (line)]] | alt | 193 | 1 | 3 | [[TAK-901 (drug)]] 5 µM 3.37× (z +9.2) | [[Panobinostat (drug)]] 5 µM 0.387× (z -13.8) |
| [[CFPAC-1 (line)]] | alt | 186 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.362× (z -16.9) |
| [[HCT15 (line)]] | alt | 271 | 1 | 3 | [[TAK-901 (drug)]] 5 µM 3.27× (z +9.0) | [[Panobinostat (drug)]] 5 µM 0.325× (z -16.5) |
| [[HepG2_C3A (line)]] | wt | 130 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.311× (z -12.6) |
| [[SHP-77 (line)]] | alt | 180 | 1 | 3 | [[TAK-901 (drug)]] 5 µM 3.03× (z +8.8) | [[Panobinostat (drug)]] 5 µM 0.430× (z -12.8) |
| [[CHP-212 (line)]] | wt | 188 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.320× (z -10.4) |
| [[AN3 CA (line)]] | alt | 271 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.520× (z -9.4) ⚠ cell-cycle shift, explains ~18% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.410× (z -9.1) |
| [[BT-474 (line)]] | alt | 179 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.346× (z -15.2) |
| [[SW 1088 (line)]] | alt | 375 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.200× (z -9.6) |
| [[NCI-H2122 (line)]] | alt | 200 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 228 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 266 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 221 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7136), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*56 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPRD1B]] | +0.66 | +0.56 / +0.69 | both halves | 1e-05 |  |
| [[ZZZ3]] | +0.65 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[SREK1]] | +0.65 | +0.49 / +0.66 | both halves | 1e-05 | STRING 547 |
| [[SCAF8]] | +0.64 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[GTF2I]] | +0.64 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[PUM2]] | +0.62 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[WBP11]] | +0.61 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[SRSF4]] | +0.59 | +0.53 / +0.56 | both halves | 1e-05 | STRING 468 |
| [[SENP6]] | +0.59 | +0.42 / +0.60 | both halves | 4e-05 |  |
| [[SAFB]] | +0.58 | +0.44 / +0.65 | both halves | 3e-05 |  |
| [[RBM33]] | +0.58 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[RAF1]] | +0.58 | +0.53 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*44 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KDM7A]] | -0.60 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[NRIP3]] | -0.59 | -0.43 / -0.62 | both halves | 3e-05 |  |
| [[CBL]] | -0.59 | -0.34 / -0.63 | both halves | 1e-04 |  |
| [[SH3BGRL3]] | -0.58 | -0.34 / -0.53 | both halves | 1e-04 |  |
| [[CCNYL1]] | -0.57 | -0.49 / -0.60 | both halves | 1e-05 |  |
| [[KCTD5]] | -0.57 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[GAN]] | -0.57 | -0.58 / -0.52 | both halves | 1e-05 |  |
| [[CIB1]] | -0.55 | -0.31 / -0.49 | both halves | 2e-04 |  |
| [[PAQR5]] | -0.54 | -0.29 / -0.54 | both halves | 2e-04 |  |
| [[CDCP1]] | -0.54 | -0.36 / -0.45 | both halves | 9e-05 |  |
| [[SERINC2]] | -0.54 | -0.37 / -0.38 | both halves | 8e-05 |  |
| [[SMS]] | -0.53 | -0.43 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises LUC7L2's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 184]]; 20 genes; this gene is in the **-** arm (projection on the module's main direction -0.723). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.39).
- **Nodal map** (x, y) = (18.2, -6.0); signed map (29.3, -25.8). **Vector** length 104, 37.7% of its response variance represented; |z| ≥ 3 in 1,417 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +7.2 | -2.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change | +6.2 | -5.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | +6.0 | -5.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.9 | +15.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.8 | +12.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.7 | -0.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.6 | -0.4 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +4.2 | +0.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.6 | +1.3 |
| fall | [[Auranofin (drug)]] 5 µM |  | -7.3 | -10.6 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -6.0 | -12.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.5 | -10.2 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -5.5 | -16.8 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -5.3 | -1.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | -5.0 | -3.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.4 | -1.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -3.5 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | LUC7 like 2, pre-mRNA splicing factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q34 — chr7:139,340,359-139,423,457 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CGI-74, CGI-59, H_NH0792N18.3, FLJ10657, LUC7B2, hLuc7B2 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y383](https://www.uniprot.org/uniprotkb/Q9Y383) (Putative RNA-binding protein Luc7-like 2):

> May bind to RNA via its Arg/Ser-rich domain.

**Summary**, from NCBI Gene [51631](https://www.ncbi.nlm.nih.gov/gene/51631):

> This gene encodes a protein that contains a C2H2-type zinc finger, coiled-coil region and arginine, serine-rich (RS) domain. A similar protein in mouse interacts with sodium channel modifier 1, and the encoded protein may be involved in the recognition of non-consensus splice donor sites in association with the U1 snRNP spliceosomal subunit. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene. [provided by RefSeq, Sep 2011]

**Accessions** — [HGNC:21608](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21608) · Entrez [51631](https://www.ncbi.nlm.nih.gov/gene/51631) · UniProt [Q9Y383](https://www.uniprot.org/uniprotkb/Q9Y383) · Ensembl [ENSG00000146963](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000146963)

## Data

Gene col 7136: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7136); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7136, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7136]; `tensor/DDL_lfc|DDL_z.npy` [7136]; `embed/gene_vectors.npy` [7136]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7136 or target_col == 7136). Every well: [[LUC7L2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LUC7L2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
