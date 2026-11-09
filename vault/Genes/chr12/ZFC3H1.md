---
symbol: "ZFC3H1"
type: "gene"
col: 5481
ensembl_id: "ENSG00000133858"
name: "zinc finger C3H1-type containing"
location: "12q21.1"
module: 179
arm: "+"
pooled_cpm: 242.07
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 10
n_dd_up_clean: 14
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/179"]
generated_by: "tahoemap"
---

# ZFC3H1

*zinc finger C3H1-type containing* — 12q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (2 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 1.69× (z +9.0, q 1e-16, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.598× (z -8.5, q 8e-15, down in 35 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 0.711× (z -5.6, q 3e-06, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RARS2]] (+0.68, fdr 7e-06), [[RABGEF1]] (+0.68, fdr 7e-06), [[TMEM165]] (+0.67, fdr 7e-06); moves opposite to [[TIGD2]] (-0.62, fdr 7e-06), [[WDR7]] (-0.60, fdr 2e-05), [[VEZF1]] (-0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 179]] (RHOA GTPase cycle).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5481.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.69×** | +9.0 | 1e-16 | 44/48 (RKO, SW480, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.46×** | +8.0 | 2e-13 | 44/49 (NCI-H1573, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.54×** | +7.4 | 2e-11 | 41/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +6.9 | 6e-10 | 31/49 (AsPC-1, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.40×** | +5.7 | 1e-06 | 38/48 (BT-474, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.38×** | +5.5 | 3e-06 | 40/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.35×** | +5.1 | 3e-05 | 33/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.32×** | +4.7 | 2e-04 | 32/48 (HT-29, PANC-1, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.62×** | +4.3 | 0.001 | 29/48 (LOX-IMVI, HS-578T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.27×** | +3.9 | 0.005 | 29/48 (HS-578T, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **1.23×** | +3.6 | 0.018 | 32/48 (PANC-1, C-33 A, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.21×** | +3.2 | 0.062 | 25/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.14× | +3.2 | 0.067 | 14/49 (MIA PaCa-2, CFPAC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.22×** | +3.1 | 0.067 | 23/48 (PANC-1, HT-29, …) | all doses, flat |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.21×** | +3.1 | 0.074 | 21/50 (C32, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tomivosertib (drug)]] 5 µM |  | **1.41×** | +3.0 | 0.082 | 26/48 (LS 180, NCI-H1573, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.37×** | +3.0 | 0.086 | 27/48 (PANC-1, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5481.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.598×** | -8.5 | 8e-15 | 35/44 (Panc 03.27, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.610×** | -8.5 | 8e-15 | 43/49 (NCI-H2347, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **0.711×** | -5.6 | 3e-06 | 37/48 (NCI-H1573, NCI-H23, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.702×** | -5.6 | 3e-06 | 32/45 (RKO, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.742×** | -5.1 | 4e-05 | 30/48 (LoVo, hTERT-HPNE, …) | two highest doses | cell-cycle shift (explains ~11% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.784×** | -4.2 | 0.003 | 35/48 (NCI-H23, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.787×** | -4.1 | 0.003 | 32/48 (NCI-H23, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.819×** | -3.4 | 0.041 | 25/48 (SW1417, CFPAC-1, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.819×** | -3.4 | 0.041 | 24/48 (MIA PaCa-2, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.821×** | -3.3 | 0.064 | 27/48 (LoVo, HCT15, …) | two highest doses | composition shift |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | 0.878× | -3.1 | 0.11 | 6/48 (CFPAC-1, NCI-H460, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5481. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 231 | 3 | 2 (2 ⚠) | [[Auranofin (drug)]] 5 µM 2.76× (z +12.3) | [[Dinaciclib (drug)]] 0.5 µM 0.463× (z -9.4) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 223 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.26× (z +12.9) | — |
| [[BT-474 (line)]] | alt | 204 | 4 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.43× (z +11.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.37× (z +11.0) | — |
| [[LoVo (line)]] | wt | 433 | 1 | 3 (2 ⚠) | [[Auranofin (drug)]] 5 µM 2.01× (z +8.9) | [[Harringtonine (drug)]] 0.5 µM 0.480× (z -9.4) |
| [[NCI-H1573 (line)]] | alt | 293 | 3 (1 ⚠) | 1 | [[TAK-901 (drug)]] 5 µM 6.72× (z +10.4) | [[Belumosudil (drug)]] 5 µM 0.433× (z -8.5) |
| [[NCI-H23 (line)]] | alt | 298 | 2 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.33× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.465× (z -9.0) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 313 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.51× (z +12.6) | — |
| [[SNU-1 (line)]] | wt | 284 | 3 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.80× (z +11.3) | [[Dinaciclib (drug)]] 5 µM 0.443× (z -8.6) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 140 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +9.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 2.57× (z +9.4) | — |
| [[HT-29 (line)]] | alt | 189 | 3 | 0 | [[Auranofin (drug)]] 5 µM 2.32× (z +10.7) | — |
| [[PANC-1 (line)]] | alt | 189 | 3 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.01× (z +9.6) | — |
| [[AsPC-1 (line)]] | alt | 340 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.44× (z +16.8) | [[Dinaciclib (drug)]] 5 µM 0.517× (z -8.6) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 272 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.350× (z -11.5) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 192 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.96× (z +10.9) | — |
| [[NCI-H2347 (line)]] | alt | 245 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.440× (z -11.8) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 169 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 1.97× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.330× (z -14.5) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 242 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.57× (z +9.6) | — |
| [[SW48 (line)]] | wt | 224 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.60× (z +9.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.43× (z +8.9) | — |
| [[A-172 (line)]] | wt | 234 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.454× (z -10.1) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 259 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.405× (z -11.1) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 177 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.250× (z -9.9) |
| [[HCT15 (line)]] | alt | 267 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.395× (z -8.7) ⚠ cell-cycle shift, explains ~45% of this change |
| [[HS-578T (line)]] | alt | 219 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.01× (z +8.6) | — |
| [[hTERT-HPNE (line)]] | wt | 282 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.409× (z -9.4) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 291 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.58× (z +9.6) | — |
| [[NCI-H2030 (line)]] | alt | 134 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.82× (z +10.2) | — |
| [[RPMI-7951 (line)]] | alt | 255 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.457× (z -9.6) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 220 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.480× (z -9.4) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 252 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.76× (z +9.1) | — |
| [[A-427 (line)]] | wt | 164 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 238 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 177 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 388 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 213 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 285 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 201 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 221 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 230 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 283 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 228 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 179 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 314 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 290 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 286 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 263 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 187 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 187 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 218 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 229 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 237 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5481), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RARS2]] | +0.68 | +0.76 / +0.69 | both halves | 7e-06 |  |
| [[RABGEF1]] | +0.68 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[TMEM165]] | +0.67 | +0.70 / +0.64 | both halves | 7e-06 |  |
| [[COPA]] | +0.67 | +0.75 / +0.72 | both halves | 7e-06 |  |
| [[RNF139-DT]] | +0.67 | +0.58 / +0.69 | both halves | 7e-06 |  |
| [[SENP5]] | +0.66 | +0.68 / +0.65 | both halves | 7e-06 |  |
| [[DPM1]] | +0.65 | +0.73 / +0.60 | both halves | 7e-06 |  |
| [[KDELR1]] | +0.64 | +0.69 / +0.66 | both halves | 7e-06 |  |
| [[CAPN10-DT]] | +0.64 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[TMED7-TICAM2]] | +0.63 | +0.54 / +0.68 | both halves | 1e-05 |  |
| [[KHDC4]] | +0.63 | +0.69 / +0.60 | both halves | 7e-06 |  |
| [[CDC26]] | +0.62 | +0.58 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TIGD2]] | -0.62 | -0.70 / -0.63 | both halves | 7e-06 |  |
| [[WDR7]] | -0.60 | -0.48 / -0.68 | both halves | 2e-05 |  |
| [[VEZF1]] | -0.59 | -0.62 / -0.55 | both halves | 1e-05 |  |
| [[RTL6]] | -0.57 | -0.69 / -0.51 | both halves | 1e-05 |  |
| [[KBTBD6]] | -0.57 | -0.58 / -0.58 | both halves | 7e-06 |  |
| [[DCLRE1A]] | -0.56 | -0.65 / -0.55 | both halves | 1e-05 |  |
| [[KAT6A]] | -0.55 | -0.42 / -0.63 | both halves | 4e-05 |  |
| [[MDM1]] | -0.55 | -0.50 / -0.60 | both halves | 1e-05 |  |
| [[PABIR1]] | -0.55 | -0.56 / -0.60 | both halves | 1e-05 |  |
| [[CHTOP]] | -0.54 | -0.55 / -0.59 | both halves | 1e-05 |  |
| [[SAYSD1]] | -0.54 | -0.63 / -0.49 | both halves | 1e-05 |  |
| [[NHLRC2]] | -0.54 | -0.57 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 179]] — RHOA GTPase cycle; 22 genes; this gene is in the **+** arm (projection on the module's main direction 0.698). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (17.9, -28.9); signed map (-45.5, 11.5). **Vector** length 108, 40.6% of its response variance represented; |z| ≥ 3 in 1,136 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +11.5 | +9.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +10.6 | +6.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +8.3 | +3.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +7.7 | +3.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +4.1 | +1.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.7 | +1.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.8 | +3.2 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.7 | +0.8 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +2.3 | +0.9 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | -10.2 | -3.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -9.7 | -5.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -7.0 | -0.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -5.8 | +2.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.1 | -2.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.8 | -5.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.3 | -1.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -2.2 | -1.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.0 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger C3H1-type containing |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q21.1 — chr12:71,609,599-71,667,725 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC23401, KIAA0546, CSRC2; previously PSRC2, CCDC131 |
| Gene groups (HGNC) | Zinc fingers |
| Reactome | 2 pathways, smallest: Nuclear RNA decay; Metabolism of RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [O60293](https://www.uniprot.org/uniprotkb/O60293) (Zinc finger C3H1 domain-containing protein):

> Subunit of the trimeric poly(A) tail exosome targeting (PAXT) complex, a complex that directs a subset of long and polyadenylated poly(A) RNAs for exosomal degradation. The RNA exosome is fundamental for the degradation of RNA in eukaryotic nuclei. Substrate targeting is facilitated by its cofactor MTREX, which links to RNA-binding protein adapters.

**Summary**, from NCBI Gene [196441](https://www.ncbi.nlm.nih.gov/gene/196441):

> Predicted to enable zinc ion binding activity. Predicted to be involved in RNA catabolic process. Located in nucleus. Part of MTREC complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28328](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28328) · Entrez [196441](https://www.ncbi.nlm.nih.gov/gene/196441) · UniProt [O60293](https://www.uniprot.org/uniprotkb/O60293) · Ensembl [ENSG00000133858](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000133858)

## Data

Gene col 5481: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5481); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5481, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5481]; `tensor/DDL_lfc|DDL_z.npy` [5481]; `embed/gene_vectors.npy` [5481]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5481 or target_col == 5481). Every well: [[ZFC3H1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZFC3H1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
