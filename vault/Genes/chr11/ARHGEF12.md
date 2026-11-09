---
symbol: "ARHGEF12"
type: "gene"
col: 12302
ensembl_id: "ENSG00000196914"
name: "Rho guanine nucleotide exchange factor 12"
location: "11q23.3"
module: 197
arm: "+"
pooled_cpm: 309.44
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 1
n_dd_up_clean: 12
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/197"]
generated_by: "tahoemap"
---

# ARHGEF12

*Rho guanine nucleotide exchange factor 12* — 11q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.81× (z +18.5, q 0e+00, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 0.726× (z -6.9, q 4e-09, down in 31 of 47 measured lines) ⚠ toxic.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 6 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Topotecan (hydrochloride) (drug)]] 5 µM in 6 lines (NCI-H1573 0.504×, HT-29 0.481×, KATO III 0.533×, SW480 0.551×, …; ⚠ toxic); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (HT-29 0.415×, NCI-H2030 0.467×, Panc 03.27 0.446×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H1792 0.540×, A549 0.597×; ⚠ cell-cycle shift, explains ~39% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ITGAV]] (+0.62, fdr 1e-05), [[NFIB]] (+0.59, fdr 1e-05), [[KLHL5]] (+0.58, fdr 3e-05); moves opposite to [[MPP3]] (-0.54, fdr 1e-05), [[ZNF765]] (-0.53, fdr 7e-05), [[TM4SF19]] (-0.53, fdr 4e-05).
> It is in [[Module 197]], a single-armed module (Nervous system development).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12302.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.81×** | +18.5 | 0e+00 | 42/48 (MIA PaCa-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.76×** | +12.0 | 1e-30 | 44/48 (MIA PaCa-2, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.68×** | +11.5 | 3e-28 | 44/48 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.46×** | +8.3 | 1e-14 | 42/48 (PANC-1, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.42×** | +7.7 | 1e-12 | 35/48 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.32×** | +6.1 | 9e-08 | 33/48 (LOX-IMVI, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.31×** | +5.9 | 3e-07 | 34/48 (COLO 205, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.77×** | +5.8 | 5e-07 | 34/49 (MIA PaCa-2, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **1.25×** | +4.9 | 6e-05 | 26/48 (HS-578T, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.24×** | +4.5 | 4e-04 | 24/47 (MIA PaCa-2, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.51×** | +4.2 | 0.002 | 29/49 (LoVo, SW48, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.14× | +4.1 | 0.002 | 17/48 (LoVo, LS 180, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.9 | 0.005 | 24/48 (A-172, LoVo, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.8 | 0.005 | 23/47 (HOP62, HS-578T, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.18× | +3.5 | 0.017 | 22/47 (A549, NCI-H1573, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 1.19× | +3.3 | 0.037 | 20/48 (LoVo, Hs 766T, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.37×** | +3.2 | 0.049 | 24/48 (C32, SW480, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Erlotinib (drug)]] 0.05 µM |  | 1.17× | +3.0 | 0.075 | 15/48 (LoVo, SW480, …) | inconsistent across doses |  |
| [[RMC-6236 (drug)]] 5 µM |  | **1.34×** | +2.9 | 0.086 | 18/48 (Hs 766T, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 5 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12302.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 6 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Topotecan (hydrochloride) (drug)]] 5 µM in 6 lines (NCI-H1573 0.504×, HT-29 0.481×, KATO III 0.533×, SW480 0.551×, …; ⚠ toxic); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (HT-29 0.415×, NCI-H2030 0.467×, Panc 03.27 0.446×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H1792 0.540×, A549 0.597×; ⚠ cell-cycle shift, explains ~39% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.726×** | -6.9 | 4e-09 | 31/47 (NCI-H1573, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~11% of this change | 0.864× | -3.3 | 0.19 | 21/48 (SW 1271, NCI-H661, …) | inconsistent across doses | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.864× | -3.3 | 0.19 | 16/48 (NCI-H1792, Hs 766T, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.865× | -3.2 | 0.19 | 16/48 (NCI-H1792, RKO, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.909× | -3.0 | 0.24 | 12/48 (AsPC-1, NCI-H1792, …) | rises with dose | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | 0.874× | -3.0 | 0.24 | 19/48 (Panc 03.27, NCI-H460, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12302. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 189 | 8 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.56× (z +26.4) | — |
| [[SW480 (line)]] | alt | 539 | 4 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +12.9) | [[Panobinostat (drug)]] 0.5 µM 0.532× (z -9.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 359 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +12.8) | — |
| [[HS-578T (line)]] | alt | 250 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +14.2) | — |
| [[BT-474 (line)]] | alt | 269 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.46× (z +21.6) | — |
| [[LOX-IMVI (line)]] | wt | 238 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.59× (z +10.0) | — |
| [[PANC-1 (line)]] | alt | 482 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +22.6) | — |
| [[HOP62 (line)]] | alt | 158 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.63× (z +10.6) | — |
| [[LoVo (line)]] | wt | 349 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.44× (z +14.3) | — |
| [[HEC-1-A (line)]] | alt | 263 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +17.7) | — |
| [[Hs 766T (line)]] | wt | 207 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +15.6) | — |
| [[HT-29 (line)]] | alt | 623 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.415× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change |
| [[hTERT-HPNE (line)]] | wt | 231 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +11.1) | — |
| [[Panc 03.27 (line)]] | alt | 350 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +19.4) | [[Dinaciclib (drug)]] 0.05 µM 0.446× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change |
| [[SW48 (line)]] | wt | 287 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +17.5) | — |
| [[A-172 (line)]] | wt | 115 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +10.5) | — |
| [[A549 (line)]] | wt | 191 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +13.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.597× (z -9.8) ⚠ cell-cycle shift, explains ~39% of this change |
| [[AsPC-1 (line)]] | alt | 413 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +13.1) | — |
| [[C32 (line)]] | wt | 155 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +13.2) | — |
| [[CFPAC-1 (line)]] | alt | 180 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +16.8) | — |
| [[NCI-H1573 (line)]] | alt | 474 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.504× (z -9.9) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 336 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.540× (z -11.1) ⚠ cell-cycle shift, explains ~39% of this change |
| [[NCI-H2030 (line)]] | alt | 422 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.467× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change |
| [[NCI-H23 (line)]] | alt | 208 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +12.7) | — |
| [[NCI-H460 (line)]] | wt | 195 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +17.6) | — |
| [[RKO (line)]] | wt | 418 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +20.9) | — |
| [[SK-MEL-2 (line)]] | alt | 112 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +13.4) | — |
| [[A-427 (line)]] | wt | 176 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +16.6) | — |
| [[CHP-212 (line)]] | wt | 395 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +11.6) | — |
| [[HCT15 (line)]] | alt | 347 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.35× (z +10.8) | — |
| [[HepG2_C3A (line)]] | wt | 344 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.501× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 591 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.533× (z -9.0) ⚠ toxic |
| [[LS 180 (line)]] | wt | 347 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.510× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change |
| [[NCI-H2347 (line)]] | alt | 247 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +18.0) | — |
| [[RPMI-7951 (line)]] | alt | 201 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +9.8) | — |
| [[SHP-77 (line)]] | alt | 321 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.564× (z -8.7) ⚠ toxic |
| [[SNU-1 (line)]] | wt | 242 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +14.0) | — |
| [[SNU-423 (line)]] | alt | 225 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.58× (z +8.9) | — |
| [[SW 900 (line)]] | alt | 363 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.66× (z +9.5) | — |
| [[SW1417 (line)]] | alt | 519 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +14.8) | — |
| [[A498 (line)]] | wt | 243 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 332 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 312 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 217 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 138 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 305 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 328 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 267 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 212 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 457 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12302), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*53 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ITGAV]] | +0.62 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[NFIB]] | +0.59 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[KLHL5]] | +0.58 | +0.45 / +0.60 | both halves | 3e-05 |  |
| [[WWC3]] | +0.57 | +0.42 / +0.57 | both halves | 4e-05 |  |
| [[ALCAM]] | +0.55 | +0.46 / +0.58 | both halves | 3e-05 |  |
| [[STIM2]] | +0.54 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[ABCD3]] | +0.54 | +0.43 / +0.61 | both halves | 3e-05 | pathway: RHOA GTPase cycle |
| [[LRP6]] | +0.53 | +0.61 / +0.49 | both halves | 1e-05 |  |
| [[CDH2]] | +0.53 | +0.37 / +0.56 | both halves | 9e-05 |  |
| [[TMEM14C]] | +0.53 | +0.43 / +0.45 | both halves | 3e-05 |  |
| [[ENAH]] | +0.52 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[DPYD]] | +0.52 | +0.56 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*47 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MPP3]] | -0.54 | -0.53 / -0.54 | both halves | 1e-05 | same gene group |
| [[ZNF765]] | -0.53 | -0.38 / -0.53 | both halves | 7e-05 |  |
| [[TM4SF19]] | -0.53 | -0.41 / -0.54 | both halves | 4e-05 |  |
| [[ZNF275]] | -0.52 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[CUL7]] | -0.52 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[ISCA1]] | -0.51 | -0.42 / -0.50 | both halves | 4e-05 | pathway: HALLMARK_HEME_METABOLISM |
| [[NGDN]] | -0.51 | -0.36 / -0.59 | both halves | 1e-04 |  |
| [[SAP30BP]] | -0.51 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[EDRF1]] | -0.51 | -0.45 / -0.41 | both halves | 4e-05 |  |
| [[POM121C]] | -0.51 | -0.35 / -0.53 | both halves | 1e-04 |  |
| [[MRPL27]] | -0.50 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[DHDDS]] | -0.49 | -0.41 / -0.54 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 197]] — Nervous system development; 16 genes; every member is in the + arm (projection on the module's main direction 0.710). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.45; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (3.0, 27.6); signed map (47.3, 18.5). **Vector** length 119, 41.4% of its response variance represented; |z| ≥ 3 in 1,242 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +5.6 | +8.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +5.4 | +4.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.4 | +12.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +5.1 | +11.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.7 | +3.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.4 | +4.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.2 | +4.2 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +3.1 | +2.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.0 | +1.7 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -7.5 | -6.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.9 | -3.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -4.6 | +0.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.9 | -3.2 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.7 | -3.3 |
|  | [[EX229 (drug)]] 5 µM |  | -3.3 | -1.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.3 | -2.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.1 | -2.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.1 | -3.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.9 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | Rho guanine nucleotide exchange factor 12 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q23.3 — chr11:120,336,413-120,489,937 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0382, LARG |
| Gene groups (HGNC) | Dbl family Rho GEFs; PDZ domain containing |
| Hallmark sets | HEME_METABOLISM, MITOTIC_SPINDLE |
| Reactome | 19 pathways, smallest: Sema4D induced cell migration and growth-cone collapse; Sema4D in semaphorin signaling; NRAGE signals death through JNK |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NZN5](https://www.uniprot.org/uniprotkb/Q9NZN5) (Rho guanine nucleotide exchange factor 12):

> Acts as guanine nucleotide exchange factor (GEF) for RhoA GTPase and may act as GTPase-activating protein (GAP) for GNA12 and GNA13. May play a role in the regulation of RhoA GTPase by guanine nucleotide-binding alpha-12 (GNA12) and alpha-13 (GNA13). Promotes endothelial cell and actin stress fiber reorientation in response to mechanotransduction (By similarity).

**Summary**, from NCBI Gene [23365](https://www.ncbi.nlm.nih.gov/gene/23365):

> Rho GTPases play a fundamental role in numerous cellular processes that are initiated by extracellular stimuli working through G protein-coupled receptors. The encoded protein may form a complex with G proteins and stimulate Rho-dependent signals. This protein has been observed to form a myeloid/lymphoid fusion partner in acute myeloid leukemia. Three transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jul 2014]

**Accessions** — [HGNC:14193](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14193) · Entrez [23365](https://www.ncbi.nlm.nih.gov/gene/23365) · UniProt [Q9NZN5](https://www.uniprot.org/uniprotkb/Q9NZN5) · Ensembl [ENSG00000196914](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196914)

## Data

Gene col 12302: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12302); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12302, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12302]; `tensor/DDL_lfc|DDL_z.npy` [12302]; `embed/gene_vectors.npy` [12302]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12302 or target_col == 12302). Every well: [[ARHGEF12 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARHGEF12.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
