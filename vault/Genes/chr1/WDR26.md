---
symbol: "WDR26"
type: "gene"
col: 8598
ensembl_id: "ENSG00000162923"
name: "WD repeat domain 26"
location: "1q42.11-q42.12"
module: 182
arm: "-"
pooled_cpm: 204.29
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 8
n_dd_up_clean: 12
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/182"]
generated_by: "tahoemap"
---

# WDR26

*WD repeat domain 26* — 1q42.11-q42.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.19× (z +14.4, q 3e-44, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.593× (z -9.6, q 4e-19, down in 41 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 0.737× (z -5.3, q 2e-05, down in 35 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (A-427 0.259×, SK-MEL-2 0.332×, CFPAC-1 0.367×, NCI-H1573 0.371×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 6 lines (SK-MEL-2 0.340×, CFPAC-1 0.346×, LOX-IMVI 0.328×, Panc 03.27 0.415×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (CHP-212 0.249×, SW 900 0.406×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PAIP2]] (+0.65, fdr 7e-06), [[TUT7]] (+0.61, fdr 1e-05), [[ZSWIM4]] (+0.60, fdr 1e-05); moves opposite to [[TADA2A]] (-0.60, fdr 7e-06), [[FAR1]] (-0.55, fdr 1e-05), [[PMS1]] (-0.53, fdr 3e-05).
> It sits in the **-** arm of [[Module 182]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[GPR137B]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 2 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8598.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.19×** | +14.4 | 3e-44 | 48/48 (SNU-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.72×** | +14.1 | 9e-43 | 44/48 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.83×** | +11.1 | 2e-26 | 46/48 (NCI-H460, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.68×** | +9.5 | 4e-19 | 42/48 (NCI-H460, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.61×** | +8.7 | 3e-16 | 42/48 (NCI-H460, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.14×** | +6.8 | 1e-09 | 37/49 (A-172, HS-578T, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.37×** | +5.4 | 4e-06 | 33/48 (KATO III, A498, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.32×** | +4.9 | 9e-05 | 33/48 (A498, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.29×** | +4.6 | 2e-04 | 29/48 (KATO III, HT-29, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.28×** | +4.5 | 4e-04 | 28/48 (KATO III, A498, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.25×** | +4.1 | 0.002 | 27/48 (KATO III, HT-29, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.51×** | +3.7 | 0.010 | 27/48 (A-172, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.45×** | +3.3 | 0.037 | 27/48 (NCI-H2347, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.2 | 0.047 | 22/48 (NCI-H460, A498, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.13× | +3.1 | 0.072 | 11/48 (MIA PaCa-2, Panc 03.27, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8598.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (A-427 0.259×, SK-MEL-2 0.332×, CFPAC-1 0.367×, NCI-H1573 0.371×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 6 lines (SK-MEL-2 0.340×, CFPAC-1 0.346×, LOX-IMVI 0.328×, Panc 03.27 0.415×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (CHP-212 0.249×, SW 900 0.406×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.593×** | -9.6 | 4e-19 | 41/49 (SK-MEL-2, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.613×** | -8.5 | 6e-15 | 37/44 (A-427, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **0.737×** | -5.3 | 2e-05 | 35/48 (NCI-H460, SNU-423, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.747×** | -5.1 | 6e-05 | 32/47 (NCI-H23, RKO, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.769×** | -4.5 | 8e-04 | 28/45 (CHP-212, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.792×** | -4.3 | 0.002 | 27/48 (NCI-H1792, CFPAC-1, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~12% of this change | **0.793×** | -4.3 | 0.002 | 30/48 (HT-29, Panc 03.27, …) | inconsistent across doses | low cells (technical?) |
| [[venetoclax (drug)]] 5 µM |  | **0.672×** | -3.6 | 0.026 | 27/48 (RKO, NCI-H23, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | 0.836× | -3.3 | 0.062 | 21/48 (HepG2/C3A, NCI-H23, …) | rises with dose |  |
| [[TAK-733 (drug)]] 5 µM |  | 0.710× | -3.1 | 0.11 | 24/48 (Hs 766T, SW 1088, …) | top dose only | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.847× | -3.1 | 0.11 | 20/49 (NCI-H23, NCI-H1573, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8598. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 227 | 11 (5 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +17.4) | [[Dinaciclib (drug)]] 5 µM 0.461× (z -10.0) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 232 | 5 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +15.1) | [[Dinaciclib (drug)]] 5 µM 0.492× (z -9.1) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 243 | 5 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +13.8) | [[Dinaciclib (drug)]] 0.5 µM 0.371× (z -12.4) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 166 | 7 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.38× (z +17.4) | — |
| [[SW 900 (line)]] | alt | 345 | 4 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.27× (z +10.4) | [[Dinaciclib (drug)]] 0.05 µM 0.406× (z -10.7) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 180 | 5 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +21.2) | [[Dinaciclib (drug)]] 0.5 µM 0.578× (z -8.8) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 97.8 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +15.4) | — |
| [[KATO III (line)]] | alt | 108 | 6 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.79× (z +11.2) | — |
| [[LoVo (line)]] | wt | 156 | 5 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.35× (z +16.4) | [[Dinaciclib (drug)]] 5 µM 0.510× (z -8.7) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 247 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.41× (z +12.9) | — |
| [[AsPC-1 (line)]] | alt | 180 | 5 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.29× (z +15.5) | — |
| [[BT-474 (line)]] | alt | 186 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.16× (z +13.9) | — |
| [[HT-29 (line)]] | alt | 200 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.64× (z +12.4) | — |
| [[NCI-H23 (line)]] | alt | 280 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.65× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.445× (z -10.6) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 171 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.77× (z +11.9) | [[Dinaciclib (drug)]] 0.5 µM 0.415× (z -13.0) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 235 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +14.0) | [[Dinaciclib (drug)]] 0.5 µM 0.340× (z -14.7) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 135 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.41× (z +12.7) | — |
| [[SW480 (line)]] | alt | 204 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.93× (z +14.4) | — |
| [[A-172 (line)]] | wt | 205 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +18.9) | — |
| [[C32 (line)]] | wt | 219 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +12.9) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.510× (z -8.9) ⚠ cell-cycle shift, explains ~18% of this change |
| [[CFPAC-1 (line)]] | alt | 281 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.346× (z -14.2) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 170 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +15.7) | [[Lonafarnib (drug)]] 5 µM 0.281× (z -8.8) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 233 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +15.5) | — |
| [[hTERT-HPNE (line)]] | wt | 210 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +12.3) | [[Dinaciclib (drug)]] 0.5 µM 0.389× (z -10.6) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 168 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +16.1) | — |
| [[LOX-IMVI (line)]] | wt | 318 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.328× (z -14.1) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 125 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.15× (z +13.3) | — |
| [[SW48 (line)]] | wt | 144 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.78× (z +13.4) | — |
| [[A-427 (line)]] | wt | 191 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.66× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.259× (z -17.5) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 303 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.249× (z -11.2) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 205 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +10.9) | — |
| [[RKO (line)]] | wt | 265 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.82× (z +10.7) | [[Dinaciclib (drug)]] 0.5 µM 0.404× (z -9.3) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 188 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +11.1) | — |
| [[A549 (line)]] | wt | 163 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +12.7) | — |
| [[C-33 A (line)]] | alt | 178 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.31× (z +9.5) | — |
| [[H4 (line)]] | wt | 247 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.285× (z -11.4) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 293 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.404× (z -8.8) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 323 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 3.88× (z +9.1) | — |
| [[NCI-H2030 (line)]] | alt | 145 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.75× (z +9.3) | — |
| [[SNU-423 (line)]] | alt | 217 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +14.8) | — |
| [[AN3 CA (line)]] | alt | 181 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 213 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 169 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 260 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 167 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 211 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 220 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 139 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 167 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 187 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8598), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*49 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PAIP2]] | +0.65 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[TUT7]] | +0.61 | +0.57 / +0.60 | both halves | 1e-05 |  |
| [[ZSWIM4]] | +0.60 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[KDM5C]] | +0.55 | +0.56 / +0.48 | both halves | 2e-05 | same gene group |
| [[LINC03009-1]] | +0.52 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[CSNK1A1]] | +0.51 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[SRSF9]] ⚠ | +0.51 | +0.55 / +0.44 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[STX10]] | +0.50 | +0.40 / +0.51 | both halves | 5e-05 |  |
| [[ZFPM2-AS1]] | +0.50 | +0.33 / +0.55 | both halves | 1e-04 |  |
| [[GPATCH2L]] | +0.50 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[SPRED3]] | +0.50 | +0.57 / +0.41 | both halves | 4e-05 |  |
| [[ERCC1]] | +0.49 | +0.40 / +0.56 | both halves | 5e-05 |  |
| [[NOSIP]] | +0.49 | +0.48 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*51 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TADA2A]] | -0.60 | -0.60 / -0.58 | both halves | 7e-06 |  |
| [[FAR1]] | -0.55 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[PMS1]] | -0.53 | -0.58 / -0.44 | both halves | 3e-05 |  |
| [[ABCB10]] | -0.53 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[ANP32B]] | -0.53 | -0.46 / -0.52 | both halves | 3e-05 |  |
| [[VRK2]] | -0.53 | -0.59 / -0.48 | both halves | 2e-05 |  |
| [[MCMBP]] | -0.52 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[RBM17]] | -0.52 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[MLLT10]] | -0.51 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[ARMC8]] | -0.51 | -0.48 / -0.53 | both halves | 2e-05 | same gene group; pathway: Aerobic respiration and respiratory electron transport; STRING 996 |
| [[CTPS2]] | -0.50 | -0.53 / -0.44 | both halves | 3e-05 | same gene group |
| [[RIOX2]] | -0.50 | -0.57 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GPR137B]] | C | GPR137B activity raises WDR26's level | lines that do not express GPR137B (3) vs lines expressing it (47) | 1.78× lower at baseline in the lines without GPR137B | 0.020 | ⚠ few lines (3 vs 47); across organs; also absent: CRYBG3, ERO1B, TEX14; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 182]]; 21 genes; this gene is in the **-** arm (projection on the module's main direction -0.545). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (20.0, -40.5); signed map (5.4, 24.9). **Vector** length 105, 38.1% of its response variance represented; |z| ≥ 3 in 1,224 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +7.0 | +4.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.2 | +2.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.1 | +3.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +4.2 | +14.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +4.1 | +2.3 |
|  | [[Entrectinib (drug)]] 5 µM |  | +2.5 | +0.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.2 | +1.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +0.5 |
| fall | [[Belumosudil (drug)]] 5 µM |  | -6.3 | -5.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.3 | -4.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -5.1 | -1.4 |
|  | [[venetoclax (drug)]] 5 µM |  | -4.6 | -3.6 |
|  | [[EX229 (drug)]] 5 µM |  | -3.7 | -2.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.7 | -2.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.6 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | WD repeat domain 26 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q42.11-q42.12 — chr1:224,385,146-224,437,033 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ21016, GID7 |
| Gene groups (HGNC) | WD repeat domain containing; CTLH complex subunits; MicroRNA protein coding host genes |
| Reactome | 3 pathways, smallest: Regulation of pyruvate metabolism; Pyruvate metabolism; Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H7D7](https://www.uniprot.org/uniprotkb/Q9H7D7) (WD repeat-containing protein 26):

> G-beta-like protein involved in cell signal transduction. Acts as a negative regulator in MAPK signaling pathway. Functions as a scaffolding protein to promote G beta:gamma-mediated PLCB2 plasma membrane translocation and subsequent activation in leukocytes. Core component of the CTLH E3 ubiquitin-protein ligase complex that selectively accepts ubiquitin from UBE2H and mediates ubiquitination and subsequent proteasomal degradation of the transcription factor HBP1. Acts as a negative regulator …

**Summary**, from NCBI Gene [80232](https://www.ncbi.nlm.nih.gov/gene/80232):

> This gene encodes a member of the WD repeat protein family. WD repeats are minimally conserved regions of approximately 40 amino acids typically bracketed by gly-his and trp-asp (GH-WD), which may facilitate formation of heterotrimeric or multiprotein complexes. Members of this family are involved in a variety of cellular processes, including cell cycle progression, signal transduction, apoptosis, and gene regulation. Two transcript variants encoding two different isoforms have been found for …

**Accessions** — [HGNC:21208](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21208) · Entrez [80232](https://www.ncbi.nlm.nih.gov/gene/80232) · UniProt [Q9H7D7](https://www.uniprot.org/uniprotkb/Q9H7D7) · Ensembl [ENSG00000162923](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162923)

## Data

Gene col 8598: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8598); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8598, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8598]; `tensor/DDL_lfc|DDL_z.npy` [8598]; `embed/gene_vectors.npy` [8598]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8598 or target_col == 8598). Every well: [[WDR26 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WDR26.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
