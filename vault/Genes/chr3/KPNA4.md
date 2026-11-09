---
symbol: "KPNA4"
type: "gene"
col: 11814
ensembl_id: "ENSG00000186432"
name: "karyopherin subunit alpha 4"
location: "3q25.33"
module: 45
arm: "-"
pooled_cpm: 251.7
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 13
n_dd_up_clean: 15
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/045"]
generated_by: "tahoemap"
---

# KPNA4

*karyopherin subunit alpha 4* — 3q25.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (11 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.03× (z +13.0, q 9e-36, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.699× (z -9.3, q 1e-17, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GATAD2A]] (+0.68, fdr 7e-06), [[CYFIP1]] (+0.65, fdr 1e-05), [[DCBLD2]] (+0.64, fdr 7e-06); moves opposite to [[SLC11A2]] (-0.67, fdr 7e-06), [[MRPL39]] (-0.64, fdr 1e-05), [[MBIP]] (-0.64, fdr 1e-05).
> It sits in the **-** arm of [[Module 045]] (Iron uptake and transport).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[GATA4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 14 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11814.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.03×** | +13.0 | 9e-36 | 48/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **3.84×** | +12.9 | 9e-36 | 48/49 (LoVo, KATO III, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.89×** | +11.7 | 3e-29 | 47/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.86×** | +11.4 | 9e-28 | 46/48 (C32, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.52×** | +10.9 | 1e-25 | 36/48 (CFPAC-1, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.81×** | +9.9 | 3e-21 | 45/48 (LS 180, Panc 03.27, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.65×** | +9.2 | 5e-18 | 44/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.65×** | +8.9 | 4e-17 | 40/48 (COLO 205, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **1.46×** | +7.0 | 2e-10 | 38/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.43×** | +6.6 | 2e-09 | 38/48 (NCI-H460, SNU-1, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.41×** | +6.3 | 1e-08 | 34/48 (KATO III, MIA PaCa-2, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.37×** | +5.4 | 2e-06 | 32/48 (KATO III, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.33×** | +5.2 | 8e-06 | 33/48 (KATO III, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | **1.31×** | +5.0 | 3e-05 | 29/49 (COLO 205, KATO III, …) | all doses, flat | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.30×** | +4.8 | 5e-05 | 31/48 (KATO III, HT-29, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.21×** | +3.5 | 0.009 | 23/48 (SW480, KATO III, …) | top dose only |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.22×** | +3.5 | 0.011 | 24/47 (HT-29, COLO 205, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 4 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11814.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **0.699×** | -9.3 | 1e-17 | 43/48 (AsPC-1, Hs 766T, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~23% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.688×** | -6.8 | 2e-09 | 42/48 (AsPC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.710×** | -6.3 | 6e-08 | 42/48 (NCI-H23, LOX-IMVI, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.773×** | -4.7 | 3e-04 | 35/49 (CFPAC-1, COLO 205, …) | all doses, stronger at high dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.931× | -4.4 | 0.001 | 5/50 (NCI-H23, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.788×** | -4.4 | 0.001 | 32/48 (NCI-H23, SK-MEL-2, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.814×** | -4.3 | 0.001 | 23/48 (NCI-H23, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **0.792×** | -4.3 | 0.001 | 34/48 (SW 1088, HOP62, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 0.855× | -4.1 | 0.003 | 15/48 (NCI-H23, RPMI-7951, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.850× | -4.1 | 0.003 | 18/49 (NCI-H23, MIA PaCa-2, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.796×** | -4.0 | 0.003 | 24/47 (NCI-H23, MIA PaCa-2, …) | rises with dose |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **0.804×** | -4.0 | 0.003 | 30/48 (LS 180, BT-474, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.826×** | -4.0 | 0.003 | 26/48 (NCI-H23, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.754×** | -3.6 | 0.011 | 29/48 (HT-29, A549, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.816×** | -3.6 | 0.013 | 24/47 (NCI-H23, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM |  | **0.700×** | -3.4 | 0.022 | 22/47 (NCI-H23, H4, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 0.843× | -3.0 | 0.084 | 20/48 (NCI-H23, LOX-IMVI, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | 0.862× | -3.0 | 0.099 | 19/49 (NCI-H23, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11814. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 178 | 14 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.69× (z +18.5) | — |
| [[NCI-H23 (line)]] | alt | 746 | 0 | 14 (2 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.494× (z -26.1) ⚠ position not correctable · without an alert: [[Ponatinib (drug)]] 5 µM 0.314× (z -12.2) |
| [[NCI-H460 (line)]] | wt | 151 | 14 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.24× (z +21.6) | — |
| [[COLO 205 (line)]] | alt | 124 | 10 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.67× (z +17.5) | — |
| [[SNU-1 (line)]] | wt | 223 | 10 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.28× (z +13.6) | — |
| [[AsPC-1 (line)]] | alt | 224 | 8 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +19.3) | [[Selinexor (drug)]] 5 µM 0.486× (z -12.6) |
| [[LS 180 (line)]] | wt | 151 | 9 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.09× (z +15.1) | — |
| [[NCI-H1573 (line)]] | alt | 217 | 8 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.06× (z +13.4) | — |
| [[BT-474 (line)]] | alt | 309 | 7 (2 ⚠) | 0 | [[Digitoxin (drug)]] 0.5 µM 3.06× (z +13.6) | — |
| [[C32 (line)]] | wt | 153 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +15.7) | — |
| [[HT-29 (line)]] | alt | 203 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +13.1) | — |
| [[LoVo (line)]] | wt | 188 | 7 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 6.49× (z +14.5) | — |
| [[NCI-H2347 (line)]] | alt | 200 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +13.9) | — |
| [[PANC-1 (line)]] | alt | 253 | 6 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.56× (z +14.1) | — |
| [[SW480 (line)]] | alt | 248 | 6 (1 ⚠) | 0 | [[Digitoxin (drug)]] 0.5 µM 2.88× (z +13.2) | — |
| [[A549 (line)]] | wt | 232 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +11.6) | — |
| [[CFPAC-1 (line)]] | alt | 151 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.76× (z +21.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 362 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.52× (z +10.5) | [[Adagrasib (drug)]] 0.05 µM 0.622× (z -18.2) ⚠ position not correctable |
| [[Panc 03.27 (line)]] | alt | 328 | 5 | 0 | [[PH-797804 (drug)]] 5 µM 5.37× (z +12.1) | — |
| [[SK-MEL-2 (line)]] | alt | 287 | 3 (1 ⚠) | 2 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 4.64× (z +10.9) | [[Dinaciclib (drug)]] 5 µM 0.451× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.635× (z -8.7) |
| [[SW1417 (line)]] | alt | 284 | 5 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.44× (z +12.6) | — |
| [[NCI-H2030 (line)]] | alt | 190 | 4 | 0 | [[PH-797804 (drug)]] 5 µM 4.34× (z +9.0) | — |
| [[A498 (line)]] | wt | 177 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +14.6) | — |
| [[HEC-1-A (line)]] | alt | 332 | 2 | 1 | [[TAK-901 (drug)]] 5 µM 3.84× (z +9.9) | [[Selinexor (drug)]] 5 µM 0.653× (z -8.5) |
| [[Hs 766T (line)]] | wt | 161 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +12.2) | [[Selinexor (drug)]] 5 µM 0.491× (z -10.7) |
| [[SW48 (line)]] | wt | 191 | 2 | 1 | [[Homoharringtonine (drug)]] 0.5 µM 2.32× (z +9.1) | [[Selinexor (drug)]] 5 µM 0.575× (z -8.5) |
| [[HCT15 (line)]] | alt | 133 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.93× (z +9.7) | — |
| [[RKO (line)]] | wt | 297 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 3.95× (z +8.5) | [[Selinexor (drug)]] 5 µM 0.557× (z -9.7) |
| [[SW 900 (line)]] | alt | 179 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 5.04× (z +8.7) | — |
| [[A-172 (line)]] | wt | 242 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.606× (z -8.8) |
| [[AN3 CA (line)]] | alt | 237 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.68× (z +8.9) | — |
| [[C-33 A (line)]] | alt | 184 | 1 | 0 | [[Auranofin (drug)]] 5 µM 1.96× (z +8.6) | — |
| [[SNU-423 (line)]] | alt | 212 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +9.7) | — |
| [[A-427 (line)]] | wt | 341 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 155 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 336 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 227 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 456 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 280 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 248 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 435 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 398 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 185 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 201 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 212 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 146 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 302 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 208 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 271 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11814), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*53 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GATAD2A]] | +0.68 | +0.65 / +0.69 | both halves | 7e-06 |  |
| [[CYFIP1]] | +0.65 | +0.54 / +0.72 | both halves | 1e-05 |  |
| [[DCBLD2]] | +0.64 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[CYTOR]] | +0.64 | +0.70 / +0.60 | both halves | 7e-06 |  |
| [[WDR1]] | +0.64 | +0.57 / +0.67 | both halves | 1e-05 |  |
| [[ACTN1]] | +0.64 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[BZW1]] | +0.63 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[ARPC4]] | +0.62 | +0.57 / +0.64 | both halves | 9e-06 |  |
| [[SCHIP1]] | +0.61 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[CD59]] | +0.61 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[MAP4K4]] | +0.61 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[DDX5]] | +0.61 | +0.52 / +0.66 | both halves | 1e-05 |  |

## Genes that move opposite

*47 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC11A2]] | -0.67 | -0.64 / -0.65 | both halves | 7e-06 |  |
| [[MRPL39]] | -0.64 | -0.51 / -0.59 | both halves | 1e-05 |  |
| [[MBIP]] | -0.64 | -0.62 / -0.56 | both halves | 1e-05 |  |
| [[CNNM2]] | -0.63 | -0.62 / -0.61 | both halves | 7e-06 |  |
| [[ASB7]] | -0.62 | -0.47 / -0.70 | both halves | 2e-05 |  |
| [[GOLPH3L]] | -0.62 | -0.58 / -0.66 | both halves | 8e-06 |  |
| [[SNX2]] | -0.61 | -0.57 / -0.61 | both halves | 8e-06 |  |
| [[RCHY1]] | -0.61 | -0.52 / -0.62 | both halves | 1e-05 |  |
| [[TADA1]] | -0.61 | -0.46 / -0.62 | both halves | 2e-05 |  |
| [[PREPL]] | -0.61 | -0.60 / -0.60 | both halves | 7e-06 |  |
| [[RAB9A]] | -0.61 | -0.49 / -0.64 | both halves | 1e-05 |  |
| [[NDUFV2]] | -0.60 | -0.51 / -0.57 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GATA4]] | B | GATA4 activity raises KPNA4's level | lines that do not express GATA4 (26) vs lines expressing it (24) | 1.24× lower at baseline in the lines without GATA4 | 0.050 | ⚠ within organs, on part of the lines; also absent: PIEZO2, TAFA5, ZNF667 |
| [[MAP2K1]] | B | MAP2K1 activity raises KPNA4's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.8% of all compounds | 0.053 | ⚠ off-target possible; 3 compounds |
| [[MSRB3]] | B | MSRB3 activity weakens KPNA4's drug response | lines that do not express MSRB3 (20) vs lines expressing it (29) | the lines without MSRB3 respond 1.44× as strongly (z diff -1.85); strongest at Homoharringtonine 5 µM: 1.80x vs 1.40x (z diff -3.0) | 0.085 | ⚠ within organs, on part of the lines; also absent: ARHGEF6, KCNG1, FHL1; target measured in part of the lines; artifact flags |
| [[TADA1]] | C | TADA1's natural level strengthens KPNA4's drug response | TADA1's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.74, reverse -0.38; direction not clear | 0.003 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 045]] — Iron uptake and transport; 102 genes; this gene is in the **-** arm (projection on the module's main direction -0.548). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (38.8, 8.3); signed map (-6.6, 37.5). **Vector** length 130, 52.4% of its response variance represented; |z| ≥ 3 in 1,608 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | +7.4 | +5.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change | +7.1 | +4.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | +7.1 | +4.1 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | +4.3 | +3.8 |
|  | [[Busulfan (drug)]] 0.05 µM |  | +4.1 | +1.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | +4.0 | +3.5 |
|  | [[Larotrectinib (drug)]] 0.05 µM |  | +3.8 | +1.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.8 | +3.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.8 | +6.3 |
| fall | [[Selinexor (drug)]] 5 µM |  | -11.2 | -9.3 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -7.8 | -6.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | -5.5 | -6.3 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -4.9 | -4.0 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | -4.8 | -4.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -4.4 | -2.7 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -4.2 | -4.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -4.2 | -4.0 |

## What is on record

|  |  |
|---|---|
| Name | karyopherin subunit alpha 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q25.33 — chr3:160,495,007-160,565,571 (-) |
| Ensembl biotype | protein_coding |
| Also known as | QIP1, SRP3, IPOA3, MGC12217, MGC26703 |
| Gene groups (HGNC) | Armadillo repeat containing; Importins |
| Reactome | 10 pathways, smallest: NS1 Mediated Effects on Host Pathways; Maturation of DENV proteins; ISG15 antiviral mechanism |
| Matched by | ensembl_id |

**Function**, from UniProt [O00629](https://www.uniprot.org/uniprotkb/O00629) (Importin subunit alpha-3):

> Functions in nuclear protein import as an adapter protein for nuclear receptor KPNB1. Binds specifically and directly to substrates containing either a simple or bipartite NLS motif. Docking of the importin/substrate complex to the nuclear pore complex (NPC) is mediated by KPNB1 through binding to nucleoporin FxFG repeats and the complex is subsequently translocated through the pore by an energy requiring, Ran-dependent mechanism. At the nucleoplasmic side of the NPC, Ran binds to importin-beta …

**Summary**, from NCBI Gene [3840](https://www.ncbi.nlm.nih.gov/gene/3840):

> The nuclear import of karyophilic proteins is directed by short amino acid sequences termed nuclear localization signals (NLSs). Karyopherins, or importins, are cytoplasmic proteins that recognize NLSs and dock NLS-containing proteins to the nuclear pore complex. The protein encoded by this gene shares the sequence similarity with Xenopus importin-alpha and Saccharomyces cerevisiae Srp1. This protein is found to interact with the NLSs of DNA helicase Q1 and SV40 T antigen. [provided by RefSeq, …

**Accessions** — [HGNC:6397](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6397) · Entrez [3840](https://www.ncbi.nlm.nih.gov/gene/3840) · UniProt [O00629](https://www.uniprot.org/uniprotkb/O00629) · Ensembl [ENSG00000186432](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000186432)

## Data

Gene col 11814: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11814); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11814, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11814]; `tensor/DDL_lfc|DDL_z.npy` [11814]; `embed/gene_vectors.npy` [11814]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11814 or target_col == 11814). Every well: [[KPNA4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KPNA4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
