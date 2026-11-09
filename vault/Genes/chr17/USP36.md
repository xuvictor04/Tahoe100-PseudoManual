---
symbol: "USP36"
type: "gene"
col: 627
ensembl_id: "ENSG00000055483"
name: "ubiquitin specific peptidase 36"
location: "17q25.3"
module: 38
arm: "+"
pooled_cpm: 152.85
n_lines_expressing: 50
n_dd_up: 36
n_dd_down: 16
n_dd_up_clean: 32
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/038"]
generated_by: "tahoemap"
---

# USP36

*ubiquitin specific peptidase 36* — 17q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 36 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.70× (z +21.1, q 0e+00, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.585× (z -8.5, q 1e-14, down in 34 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Cobimetinib (drug)]] 5 µM: 0.712× (z -5.2, q 4e-05, down in 35 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UBE2CP5]] (+0.69, fdr 7e-06), [[KCNJ14]] (+0.62, fdr 2e-05), [[RRP12]] (+0.62, fdr 1e-05); moves opposite to [[TMTC3]] (-0.59, fdr 1e-05), [[DLD]] (-0.59, fdr 1e-05), [[ADD3]] (-0.58, fdr 2e-05).
> It is in [[Module 038]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 36 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 627.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.70×** | +21.1 | 0e+00 | 44/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.81×** | +16.3 | 0e+00 | 46/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.45×** | +14.2 | 3e-43 | 48/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.15×** | +12.1 | 2e-31 | 46/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.68×** | +10.8 | 6e-25 | 47/49 (LoVo, SK-MEL-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.89×** | +10.1 | 8e-22 | 47/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.85×** | +9.7 | 2e-20 | 45/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.90×** | +9.7 | 2e-20 | 44/48 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.81×** | +8.5 | 1e-15 | 41/48 (SW480, PANC-1, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.67×** | +8.1 | 3e-14 | 46/48 (Hs 766T, HT-29, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.65×** | +7.9 | 1e-13 | 42/48 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.36×** | +6.6 | 2e-09 | 28/49 (NCI-H1792, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.53×** | +6.5 | 5e-09 | 37/47 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.43×** | +5.7 | 5e-07 | 29/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.40×** | +5.3 | 5e-06 | 32/48 (SW480, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.28×** | +5.1 | 1e-05 | 35/49 (C32, SK-MEL-2, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.37×** | +4.8 | 5e-05 | 33/47 (SK-MEL-2, BT-474, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.34×** | +4.6 | 1e-04 | 29/48 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~7% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 6 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 627.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.585×** | -8.5 | 1e-14 | 34/49 (CHP-212, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.673×** | -6.0 | 5e-07 | 33/44 (A498, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **0.712×** | -5.2 | 4e-05 | 35/47 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.812×** | -4.5 | 0.001 | 30/48 (LS 180, RKO, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.758×** | -4.4 | 0.001 | 30/48 (A498, PANC-1, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.759×** | -4.4 | 0.001 | 33/47 (MIA PaCa-2, SW480, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.766×** | -4.1 | 0.004 | 33/48 (NCI-H23, SW480, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.763×** | -4.0 | 0.005 | 25/45 (A498, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.781×** | -3.9 | 0.005 | 26/48 (A498, RKO, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.782×** | -3.9 | 0.005 | 28/49 (Hs 766T, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.785×** | -3.8 | 0.006 | 26/48 (A498, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.820×** | -3.7 | 0.010 | 25/48 (RKO, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.798×** | -3.6 | 0.015 | 25/49 (NCI-H23, MIA PaCa-2, …) | all doses, flat |  |
| [[Busulfan (drug)]] 0.05 µM |  | **0.799×** | -3.5 | 0.015 | 27/49 (A-172, HCT15, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.853× | -3.5 | 0.015 | 18/48 (SW480, NCI-H23, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.790×** | -3.4 | 0.020 | 23/48 (NCI-H23, RKO, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.822×** | -3.1 | 0.064 | 21/48 (RKO, J82, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 627. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 169 | 13 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 13.1× (z +31.4) | — |
| [[SW480 (line)]] | alt | 134 | 13 (3 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.22× (z +15.3) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 2.94× (z +14.1) | — |
| [[NCI-H1573 (line)]] | alt | 156 | 9 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 13.8× (z +31.4) | — |
| [[NCI-H1792 (line)]] | alt | 92.0 | 9 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.27× (z +18.7) | — |
| [[A498 (line)]] | wt | 213 | 3 | 5 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +17.0) | [[Dinaciclib (drug)]] 5 µM 0.272× (z -15.8) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 179 | 6 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.12× (z +15.3) | [[Dinaciclib (drug)]] 5 µM 0.308× (z -9.2) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 153 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +15.2) | — |
| [[A-172 (line)]] | wt | 119 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.67× (z +24.8) | — |
| [[AsPC-1 (line)]] | alt | 124 | 6 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.65× (z +20.7) | [[Dinaciclib (drug)]] 5 µM 0.459× (z -9.0) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 95.2 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.78× (z +18.8) | — |
| [[Hs 766T (line)]] | wt | 75.5 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.21× (z +18.0) | — |
| [[HT-29 (line)]] | alt | 107 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +13.0) | — |
| [[hTERT-HPNE (line)]] | wt | 189 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.32× (z +12.9) | — |
| [[LoVo (line)]] | wt | 119 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +17.4) | — |
| [[NCI-H23 (line)]] | alt | 215 | 3 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +14.0) | [[Dinaciclib (drug)]] 5 µM 0.359× (z -12.1) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 117 | 6 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.37× (z +14.8) | — |
| [[SNU-423 (line)]] | alt | 172 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.55× (z +16.7) | — |
| [[HepG2_C3A (line)]] | wt | 131 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 3.19× (z +10.8) | — |
| [[J82 (line)]] | alt | 168 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +16.5) | [[Dinaciclib (drug)]] 0.5 µM 0.402× (z -9.3) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 90.6 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.83× (z +17.6) | — |
| [[RPMI-7951 (line)]] | alt | 144 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.77× (z +18.2) | — |
| [[SNU-1 (line)]] | wt | 155 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +13.5) | — |
| [[SW48 (line)]] | wt | 194 | 4 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 7.91× (z +16.3) | [[Dinaciclib (drug)]] 0.05 µM 0.294× (z -8.9) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 130 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +12.8) | [[Dinaciclib (drug)]] 0.5 µM 0.518× (z -8.8) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 93.2 | 4 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.63× (z +12.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.46× (z +11.9) | — |
| [[LS 180 (line)]] | wt | 99.9 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +13.1) | — |
| [[SK-MEL-2 (line)]] | alt | 152 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.53× (z +27.2) | — |
| [[SW1417 (line)]] | alt | 145 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.69× (z +12.7) | — |
| [[C32 (line)]] | wt | 96.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.15× (z +15.8) | — |
| [[HS-578T (line)]] | alt | 158 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +13.2) | [[Dinaciclib (drug)]] 5 µM 0.338× (z -10.1) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 159 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.39× (z +11.3) | — |
| [[AN3 CA (line)]] | alt | 136 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.70× (z +10.4) | — |
| [[CFPAC-1 (line)]] | alt | 88.5 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.32× (z +12.1) | — |
| [[HEC-1-A (line)]] | alt | 159 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +18.1) | — |
| [[KATO III (line)]] | alt | 160 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +13.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 220 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +10.6) | — |
| [[RKO (line)]] | wt | 171 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.551× (z -10.0) |
| [[SW 900 (line)]] | alt | 190 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +11.7) | — |
| [[A549 (line)]] | wt | 168 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +10.3) | — |
| [[CHP-212 (line)]] | wt | 299 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.184× (z -14.7) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 262 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.33× (z +13.6) | — |
| [[HCT15 (line)]] | alt | 151 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +8.8) | — |
| [[NCI-H2030 (line)]] | alt | 338 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.53× (z +10.3) | — |
| [[SW 1088 (line)]] | alt | 137 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.106× (z -8.6) |
| [[C-33 A (line)]] | alt | 97.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 166 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 150 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 159 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 90.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 133 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 627), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*52 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBE2CP5]] | +0.69 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[KCNJ14]] | +0.62 | +0.47 / +0.61 | both halves | 2e-05 |  |
| [[RRP12]] | +0.62 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[PRRT3-AS1]] | +0.58 | +0.46 / +0.48 | both halves | 3e-05 |  |
| [[SPAG7]] | +0.57 | +0.42 / +0.53 | both halves | 4e-05 |  |
| [[ORAI2]] | +0.56 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[GAR1]] | +0.56 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[ZNF432]] | +0.56 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[FBXO10]] | +0.55 | +0.40 / +0.47 | both halves | 5e-05 |  |
| [[POLR1C]] | +0.55 | +0.43 / +0.49 | both halves | 3e-05 |  |
| [[MATN1-AS1]] | +0.54 | +0.52 / +0.45 | both halves | 3e-05 |  |
| [[TIMM44]] | +0.54 | +0.50 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*48 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMTC3]] | -0.59 | -0.50 / -0.57 | both halves | 1e-05 |  |
| [[DLD]] | -0.59 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[ADD3]] | -0.58 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[LANCL1]] | -0.56 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[ABCD3]] | -0.56 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[ATP5F1A]] | -0.55 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[CLSTN1]] | -0.54 | -0.38 / -0.50 | both halves | 6e-05 |  |
| [[ZDHHC20]] | -0.54 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[EXOC5]] | -0.54 | -0.46 / -0.52 | both halves | 3e-05 |  |
| [[TGOLN2]] | -0.54 | -0.46 / -0.41 | both halves | 4e-05 |  |
| [[TWSG1]] | -0.53 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[EXT2]] | -0.53 | -0.40 / -0.51 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 038]]; 122 genes; every member is in the + arm (projection on the module's main direction 0.567). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (34.9, -27.4); signed map (8.1, 11.9). **Vector** length 100, 39.7% of its response variance represented; |z| ≥ 3 in 1,521 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.6 | +6.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +7.2 | +7.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +6.2 | +2.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.0 | +8.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.9 | +16.3 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +4.8 | +4.0 |
|  | [[EX229 (drug)]] 5 µM |  | +4.5 | +4.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.8 | +3.6 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.9 | -3.4 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -2.8 | +0.0 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | -1.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.7 | +2.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -2.6 | -2.2 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -2.5 | -0.0 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin specific peptidase 36 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.3 — chr17:78,787,381-78,841,441 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1453, FLJ12851 |
| Gene groups (HGNC) | Ubiquitin specific peptidases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P275](https://www.uniprot.org/uniprotkb/Q9P275) (Ubiquitin carboxyl-terminal hydrolase 36):

> Deubiquitinase essential for the regulation of nucleolar structure and function. Required for cell and organism viability. Plays an important role in ribosomal RNA processing and protein synthesis, which is mediated, at least in part, through deubiquitination of DHX33, NPM1 and FBL, regulating their protein stability. Functions as a transcriptional repressor by deubiquiting histone H2B at the promoters of genes critical for cellular differentiation, such as CDKN1A, thereby preventing histone H3 …

**Summary**, from NCBI Gene [57602](https://www.ncbi.nlm.nih.gov/gene/57602):

> This gene encodes a member of the peptidase C19 or ubiquitin-specific protease family of cysteine proteases. Members of this family remove ubiquitin molecules from polyubiquitinated proteins. The encoded protein may deubiquitinate and stabilize the transcription factor c-Myc, also known as MYC, an important oncoprotein known to be upregulated in most human cancers. The encoded protease may also regulate the activation of autophagy. This gene exhibits elevated expression in some breast and lung …

**Accessions** — [HGNC:20062](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20062) · Entrez [57602](https://www.ncbi.nlm.nih.gov/gene/57602) · UniProt [Q9P275](https://www.uniprot.org/uniprotkb/Q9P275) · Ensembl [ENSG00000055483](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000055483)

## Data

Gene col 627: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 627); `tables/drug_effects.parquet` (53 rows, flagged included); `relations/gene_relations.parquet` (col_a == 627, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 627]; `tensor/DDL_lfc|DDL_z.npy` [627]; `embed/gene_vectors.npy` [627]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 627 or target_col == 627). Every well: [[USP36 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/USP36.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
