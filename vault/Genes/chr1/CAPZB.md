---
symbol: "CAPZB"
type: "gene"
col: 1193
ensembl_id: "ENSG00000077549"
name: "capping actin protein of muscle Z-line subunit beta"
location: "1p36.13"
module: 111
arm: "+"
pooled_cpm: 221.21
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 9
n_dd_up_clean: 3
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/111"]
generated_by: "tahoemap"
---

# CAPZB

*capping actin protein of muscle Z-line subunit beta* — 1p36.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.74× (z +16.6, q 0e+00, up in 41 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 2.01× (z +10.9, q 2e-25, up in 43 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.672× (z -15.8, q 0e+00, down in 40 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RSU1]] (+0.70, fdr 1e-05), [[RAB5C]] (+0.65, fdr 1e-05), [[GNB1]] (+0.65, fdr 7e-06); moves opposite to [[ZNF330]] (-0.62, fdr 7e-06), [[MRPS31]] (-0.60, fdr 7e-06), [[DCP1B]] (-0.59, fdr 1e-05).
> It is in [[Module 111]], a single-armed module (Cell-Cell communication).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 7 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1193.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.74×** | +16.6 | 0e+00 | 41/49 (HOP62, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.47×** | +11.1 | 2e-26 | 32/44 (A498, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.01×** | +10.9 | 2e-25 | 43/49 (HEC-1-A, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.39×** | +9.2 | 5e-18 | 36/45 (NCI-H23, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.50×** | +6.4 | 2e-08 | 35/48 (HEC-1-A, RKO, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.14× | +4.0 | 0.006 | 16/48 (HEC-1-A, Hs 766T, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | 1.13× | +3.7 | 0.019 | 18/48 (SW480, RKO, …) | top dose only | composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.26×** | +3.7 | 0.019 | 19/38 (NCI-H1573, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.24×** | +3.4 | 0.040 | 18/48 (HepG2/C3A, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.12× | +3.4 | 0.045 | 12/48 (MIA PaCa-2, SW480, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1193.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.672×** | -15.8 | 0e+00 | 40/49 (HT-29, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.674×** | -11.3 | 5e-27 | 40/47 (RKO, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.756×** | -11.1 | 2e-26 | 33/48 (LoVo, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.690×** | -11.0 | 4e-26 | 38/48 (A-427, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.711×** | -10.1 | 5e-22 | 42/48 (NCI-H2347, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.794×** | -6.6 | 5e-09 | 30/48 (LoVo, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.799×** | -6.4 | 1e-08 | 24/48 (C-33 A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.815×** | -6.1 | 9e-08 | 27/48 (A549, J82, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.891× | -4.9 | 7e-05 | 15/48 (A549, BT-474, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.853× | -4.7 | 1e-04 | 16/48 (NCI-H23, HepG2/C3A, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~4% of this change | 0.855× | -4.6 | 2e-04 | 17/49 (A549, PANC-1, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~0% of this change | 0.858× | -4.5 | 3e-04 | 18/48 (AsPC-1, NCI-H2030, …) | inconsistent across doses | low cells (technical?) |
| [[Cobimetinib (drug)]] 5 µM |  | 0.854× | -4.5 | 3e-04 | 15/47 (A498, A-427, …) | rises with dose |  |
| [[Amsacrine (drug)]] 5 µM |  | 0.900× | -4.3 | 9e-04 | 6/48 (A549, J82, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.960× | -4.0 | 0.002 | 1/50 (NCI-H2122) | inconsistent across doses |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 0.878× | -3.8 | 0.005 | 12/48 (KATO III, PANC-1, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.919× | -3.4 | 0.018 | 6/48 (NCI-H2347, SK-MEL-2, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | 0.888× | -3.2 | 0.035 | 12/47 (A-172, HOP62, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.890× | -3.2 | 0.038 | 6/48 (CFPAC-1, PANC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.00 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1193. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 234 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.365× (z -22.8) |
| [[MIA PaCa-2 (line)]] | alt | 215 | 4 (4 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.07× (z +11.8) ⚠ toxic; transcription drop | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.552× (z -9.9) |
| [[NCI-H23 (line)]] | alt | 275 | 3 (3 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.23× (z +14.2) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.592× (z -12.8) |
| [[NCI-H2347 (line)]] | alt | 186 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.05 µM 1.61× (z +8.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.597× (z -13.8) |
| [[PANC-1 (line)]] | alt | 358 | 3 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.08× (z +12.4) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 2.64× (z +8.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.586× (z -12.1) |
| [[A549 (line)]] | wt | 169 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.43× (z +15.5) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.608× (z -11.6) |
| [[C-33 A (line)]] | alt | 329 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.436× (z -14.6) |
| [[J82 (line)]] | alt | 267 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 1.76× (z +10.0) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.626× (z -10.9) |
| [[LS 180 (line)]] | wt | 235 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.525× (z -13.9) |
| [[NCI-H1792 (line)]] | alt | 185 | 1 (1 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.05× (z +10.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.371× (z -18.9) |
| [[A-427 (line)]] | wt | 228 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 1.88× (z +10.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.382× (z -16.6) |
| [[AN3 CA (line)]] | alt | 192 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.71× (z +9.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.507× (z -8.8) |
| [[HEC-1-A (line)]] | alt | 210 | 2 (1 ⚠) | 1 | [[TAK-901 (drug)]] 5 µM 3.07× (z +11.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.650× (z -11.9) |
| [[HOP62 (line)]] | alt | 214 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.64× (z +15.5) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 369 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 1.87× (z +10.6) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.612× (z -11.0) |
| [[NCI-H2030 (line)]] | alt | 233 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 1.88× (z +10.3) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.593× (z -11.3) |
| [[RPMI-7951 (line)]] | alt | 430 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.470× (z -13.5) |
| [[SNU-423 (line)]] | alt | 211 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.61× (z +14.4) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 177 | 2 (1 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 2.65× (z +11.3) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.563× (z -12.2) ⚠ toxic |
| [[A-172 (line)]] | wt | 101 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.12× (z +11.0) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 175 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.20× (z +15.3) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 274 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.601× (z -10.5) |
| [[C32 (line)]] | wt | 223 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.542× (z -11.0) |
| [[CFPAC-1 (line)]] | alt | 242 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.89× (z +9.9) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 470 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.456× (z -16.0) |
| [[HT-29 (line)]] | alt | 349 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.452× (z -15.2) |
| [[KATO III (line)]] | alt | 167 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.27× (z +14.0) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 246 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.609× (z -9.8) |
| [[RKO (line)]] | wt | 209 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.16× (z +8.6) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.351× (z -14.2) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 192 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.90× (z +10.7) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 189 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 3.70× (z +8.6) | — |
| [[hTERT-HPNE (line)]] | wt | 218 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.582× (z -8.8) |
| [[LOX-IMVI (line)]] | wt | 139 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.93× (z +10.9) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 135 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.74× (z +9.4) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 162 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.633× (z -10.2) ⚠ cell-cycle shift, explains ~16% of this change |
| [[SW 900 (line)]] | alt | 190 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.523× (z -11.5) |
| [[SW1417 (line)]] | alt | 141 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.553× (z -9.7) ⚠ toxic |
| [[SW48 (line)]] | wt | 185 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.444× (z -9.9) ⚠ toxic |
| [[BT-474 (line)]] | alt | 194 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 123 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 176 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 180 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 260 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 199 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 202 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 207 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 153 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 220 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 275 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 133 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1193), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*51 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RSU1]] | +0.70 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[RAB5C]] | +0.65 | +0.69 / +0.56 | both halves | 1e-05 |  |
| [[GNB1]] | +0.65 | +0.60 / +0.68 | both halves | 7e-06 | pathway: Sensory Perception |
| [[ACTR3]] | +0.64 | +0.62 / +0.75 | both halves | 7e-06 | STRING 774 |
| [[RHOA]] | +0.63 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[ITGB1]] | +0.62 | +0.65 / +0.61 | both halves | 7e-06 | pathway: Affinity selection of immunoglobulins |
| [[CDC42]] | +0.62 | +0.62 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_MITOTIC_SPINDLE; STRING 497 |
| [[RAB10]] | +0.62 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[ACTN4]] | +0.60 | +0.55 / +0.62 | both halves | 1e-05 | pathway: HALLMARK_MITOTIC_SPINDLE; STRING 513 |
| [[WDR1]] | +0.60 | +0.49 / +0.75 | both halves | 1e-05 | STRING 941 |
| [[CNN2]] | +0.60 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[ARPC4]] | +0.59 | +0.53 / +0.68 | both halves | 1e-05 | STRING 571 |

## Genes that move opposite

*49 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF330]] | -0.62 | -0.63 / -0.59 | both halves | 7e-06 |  |
| [[MRPS31]] | -0.60 | -0.58 / -0.66 | both halves | 7e-06 |  |
| [[DCP1B]] | -0.59 | -0.59 / -0.51 | both halves | 1e-05 |  |
| [[POLR1H]] | -0.59 | -0.53 / -0.58 | both halves | 1e-05 |  |
| [[BTN2A1]] | -0.59 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[WHAMM]] | -0.59 | -0.55 / -0.52 | both halves | 1e-05 | pathway: RHOD GTPase cycle |
| [[HMGCL]] | -0.59 | -0.55 / -0.58 | both halves | 1e-05 |  |
| [[KIAA1586]] | -0.59 | -0.54 / -0.57 | both halves | 1e-05 |  |
| [[TERF2IP]] | -0.58 | -0.57 / -0.55 | both halves | 1e-05 |  |
| [[ZNF616]] | -0.56 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[THAP3]] | -0.56 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[BTN2A3P-1]] | -0.56 | -0.57 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 111]] — Cell-Cell communication; 43 genes; every member is in the + arm (projection on the module's main direction 0.698). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-36.6, -18.1); signed map (-9.4, 35.4). **Vector** length 132, 41.5% of its response variance represented; |z| ≥ 3 in 1,151 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *RHO GTPase Effectors* (reactome, mean cos +0.51 to 10); *EPHB-mediated forward signaling* (reactome, mean cos +0.56 to 6); *Leishmania infection* (reactome, mean cos +0.54 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.0 | +16.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | +7.2 | +10.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.6 | +9.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.5 | +11.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +6.1 | -3.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.9 | +6.4 |
|  | [[EX229 (drug)]] 5 µM |  | +3.2 | +3.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.7 | +2.4 |
|  | [[Busulfan (drug)]] 0.05 µM |  | +2.5 | +2.1 |
|  | [[Berberine (chloride hydrate) (drug)]] 5 µM |  | +2.4 | +1.1 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -10.0 | -11.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -8.9 | -11.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -7.1 | -11.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -7.1 | -10.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.2 | -15.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.2 | -2.5 |
|  | [[Amsacrine (drug)]] 5 µM |  | -4.1 | -4.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.9 | -4.7 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -3.7 | -3.8 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -3.6 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | capping actin protein of muscle Z-line subunit beta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.13 — chr1:19,338,775-19,485,539 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Dynactin subunits |
| Hallmark sets | MITOTIC_SPINDLE |
| Reactome | 27 pathways, smallest: RHOF GTPase cycle; COPI-independent Golgi-to-ER retrograde traffic; HSP90 chaperone cycle for steroid hormone receptors (SHR) in the presence of ligand |
| Matched by | ensembl_id |

**Function**, from UniProt [P47756](https://www.uniprot.org/uniprotkb/P47756) (F-actin-capping protein subunit beta):

> F-actin-capping proteins bind in a Ca(2+)-independent manner to the fast growing ends of actin filaments (barbed end) thereby blocking the exchange of subunits at these ends. Unlike other capping proteins (such as gelsolin and severin), these proteins do not sever actin filaments. Plays a role in the regulation of cell morphology and cytoskeletal organization. Forms, with CAPZB, the barbed end of the fast growing ends of actin filaments in the dynactin complex and stabilizes dynactin structure. …

**Summary**, from NCBI Gene [832](https://www.ncbi.nlm.nih.gov/gene/832):

> This gene encodes the beta subunit of the barbed-end actin binding protein, which belongs to the F-actin capping protein family. The capping protein is a heterodimeric actin capping protein that blocks actin filament assembly and disassembly at the fast growing (barbed) filament ends and functions in regulating actin filament dynamics as well as in stabilizing actin filament lengths in muscle and nonmuscle cells. A pseudogene of this gene is located on the long arm of chromosome 2. Multiple …

**Accessions** — [HGNC:1491](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1491) · Entrez [832](https://www.ncbi.nlm.nih.gov/gene/832) · UniProt [P47756](https://www.uniprot.org/uniprotkb/P47756) · Ensembl [ENSG00000077549](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000077549)

## Data

Gene col 1193: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1193); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1193, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1193]; `tensor/DDL_lfc|DDL_z.npy` [1193]; `embed/gene_vectors.npy` [1193]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1193 or target_col == 1193). Every well: [[CAPZB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CAPZB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
