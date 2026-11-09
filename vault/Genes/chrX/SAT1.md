---
symbol: "SAT1"
type: "gene"
col: 5021
ensembl_id: "ENSG00000130066"
name: "spermidine/spermine N1-acetyltransferase 1"
location: "Xp22.11"
module: 153
arm: "+"
pooled_cpm: 431.35
n_lines_expressing: 45
n_dd_up: 24
n_dd_down: 0
n_dd_up_clean: 10
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 5
direction_downstream: 2
tags: ["gene", "module/153"]
generated_by: "tahoemap"
---

# SAT1

*spermidine/spermine N1-acetyltransferase 1* — Xp22.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (14 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.46× (z +12.7, q 2e-34, up in 43 of 43 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Adagrasib (drug)]] 0.05 µM in 1 line (NCI-H23 0.662×; ⚠ position not correctable); [[Homoharringtonine (drug)]] 5 µM in 1 line (KATO III 0.479×; ⚠ cell-cycle shift, would explain all of this change); [[Trametinib (drug)]] 5 µM in 1 line (HCT15 0.280×; ⚠ cell-cycle shift, explains ~40% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (KATO III 0.416×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POLD4]] (+0.58, fdr 3e-05), [[ZSWIM6]] (+0.55, fdr 3e-05), [[TPT1]] (+0.55, fdr 3e-05); moves opposite to [[MAPKAPK5]] (-0.55, fdr 9e-05), [[POMK]] (-0.54, fdr 2e-05), [[AIFM1]] (-0.51, fdr 3e-05).
> It is in [[Module 153]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[PTAFR]] → it (grade B ⚠); 2 go from it, the strongest it → [[HAPLN3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 14 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5021.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.46×** | +12.7 | 2e-34 | 43/43 (C32, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.81×** | +10.3 | 1e-22 | 41/43 (SW480, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.32×** | +8.4 | 7e-15 | 41/43 (HS-578T, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **2.28×** | +8.3 | 2e-14 | 37/43 (SW480, HOP62, …) | all doses, stronger at high dose | position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **4.34×** | +7.7 | 2e-12 | 39/41 (PANC-1, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.15×** | +7.7 | 2e-12 | 41/44 (C32, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.13×** | +7.2 | 7e-11 | 40/43 (SNU-423, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.91×** | +6.5 | 7e-09 | 35/43 (SW480, HOP62, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.88×** | +6.3 | 2e-08 | 39/43 (SK-MEL-2, HS-578T, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | **2.03×** | +6.0 | 9e-08 | 31/44 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **1.83×** | +6.0 | 9e-08 | 36/43 (NCI-H460, NCI-H1573, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | **1.83×** | +5.8 | 3e-07 | 32/42 (NCI-H460, NCI-H1573, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change | **1.62×** | +4.6 | 2e-04 | 26/39 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.57×** | +4.3 | 7e-04 | 35/45 (HEC-1-A, HOP62, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.50×** | +4.1 | 0.002 | 26/43 (MIA PaCa-2, AsPC-1, …) | two highest doses | cell-cycle shift (explains ~23% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **2.01×** | +3.6 | 0.011 | 32/44 (PANC-1, SNU-423, …) | all doses, flat | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.81×** | +3.0 | 0.061 | 30/43 (Panc 03.27, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.78×** | +3.0 | 0.061 | 21/43 (SW48, AsPC-1, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5021.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Adagrasib (drug)]] 0.05 µM in 1 line (NCI-H23 0.662×; ⚠ position not correctable); [[Homoharringtonine (drug)]] 5 µM in 1 line (KATO III 0.479×; ⚠ cell-cycle shift, would explain all of this change); [[Trametinib (drug)]] 5 µM in 1 line (HCT15 0.280×; ⚠ cell-cycle shift, explains ~40% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (KATO III 0.416×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.678× | -3.6 | 0.14 | 29/43 (SW480, HCT15, …) | inconsistent across doses | position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | 0.714× | -3.4 | 0.14 | 28/43 (NCI-H23, HCT15, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.787× | -3.4 | 0.14 | 26/43 (HepG2/C3A, SW480, …) | inconsistent across doses |  |
| [[Encorafenib (drug)]] 5 µM |  | 0.558× | -3.1 | 0.30 | 24/43 (HT-29, C32, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.31 per unit of S-phase module lfc, +0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5021. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 264 | 12 (11 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 8.25× (z +14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 2.84× (z +10.4) | — |
| [[HOP62 (line)]] | alt | 145 | 9 (4 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 5.42× (z +11.8) | — |
| [[PANC-1 (line)]] | alt | 293 | 8 (5 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.99× (z +12.0) | — |
| [[AsPC-1 (line)]] | alt | 270 | 7 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.01× (z +19.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 5.42× (z +12.9) | — |
| [[HCT15 (line)]] | alt | 380 | 6 (1 ⚠) | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.14× (z +12.2) | [[Trametinib (drug)]] 5 µM 0.280× (z -9.9) ⚠ cell-cycle shift, explains ~40% of this change |
| [[NCI-H1573 (line)]] | alt | 881 | 7 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 7.06× (z +12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 2.43× (z +8.9) | — |
| [[HS-578T (line)]] | alt | 309 | 6 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 6.35× (z +13.6) | — |
| [[J82 (line)]] | alt | 241 | 6 (4 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 5.19× (z +10.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 428 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.38× (z +14.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.74× (z +10.8) | — |
| [[SNU-423 (line)]] | alt | 631 | 6 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 3.20× (z +14.4) | — |
| [[SW480 (line)]] | alt | 475 | 6 (3 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 3.43× (z +14.7) | — |
| [[hTERT-HPNE (line)]] | wt | 224 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.94× (z +15.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 3.11× (z +10.8) | — |
| [[SK-MEL-2 (line)]] | alt | 347 | 5 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 4.91× (z +11.4) | — |
| [[CFPAC-1 (line)]] | alt | 1,021 | 4 | 0 | [[Tucidinostat (drug)]] 5 µM 2.64× (z +13.4) | — |
| [[H4 (line)]] | wt | 267 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 5.14× (z +11.8) | — |
| [[HEC-1-A (line)]] | alt | 112 | 4 (2 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 3.04× (z +10.4) | — |
| [[SW48 (line)]] | wt | 336 | 4 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 3.73× (z +14.3) | — |
| [[C32 (line)]] | wt | 420 | 3 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 4.12× (z +15.1) | — |
| [[HT-29 (line)]] | alt | 398 | 2 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.47× (z +12.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.525× (z -9.1) ⚠ cell-cycle shift, explains ~20% of this change |
| [[NCI-H23 (line)]] | alt | 319 | 2 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 4.79× (z +12.4) | [[Adagrasib (drug)]] 0.05 µM 0.662× (z -11.7) ⚠ position not correctable |
| [[A498 (line)]] | wt | 281 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 3.81× (z +13.1) | — |
| [[KATO III (line)]] | alt | 765 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.479× (z -10.4) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.416× (z -8.7) |
| [[LoVo (line)]] | wt | 218 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 2.78× (z +12.8) | — |
| [[LS 180 (line)]] | wt | 295 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 2.22× (z +8.9) | — |
| [[A-172 (line)]] | wt | 716 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.87× (z +12.3) | — |
| [[A-427 (line)]] | wt | 539 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.39× (z +8.6) | — |
| [[A549 (line)]] | wt | 521 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.39× (z +10.1) | — |
| [[BT-474 (line)]] | alt | 1,122 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.13× (z +9.0) | — |
| [[HepG2_C3A (line)]] | wt | 509 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.19× (z +9.1) | — |
| [[Hs 766T (line)]] | wt | 331 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.22× (z +10.4) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H2347 (line)]] | alt | 1,091 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.47× (z +9.7) | — |
| [[Panc 03.27 (line)]] | alt | 355 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.84× (z +11.6) | — |
| [[RPMI-7951 (line)]] | alt | 188 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.89× (z +10.4) | — |
| [[SW 900 (line)]] | alt | 368 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.57× (z +9.8) | — |
| [[AN3 CA (line)]] | alt | 132 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 58.0 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 77.1 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 674 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 106 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 557 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 742 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 539 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 430 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 345 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 143 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 70.4 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 62.9 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 336 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 160 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 779 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5021), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLD4]] | +0.58 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[ZSWIM6]] | +0.55 | +0.46 / +0.53 | both halves | 3e-05 |  |
| [[TPT1]] | +0.55 | +0.44 / +0.53 | both halves | 3e-05 |  |
| [[NEAT1]] | +0.55 | +0.44 / +0.52 | both halves | 3e-05 |  |
| [[LCN2]] | +0.55 | +0.37 / +0.55 | both halves | 7e-05 |  |
| [[HAPLN3]] | +0.53 | +0.39 / +0.59 | both halves | 6e-05 |  |
| [[TALAM1]] | +0.53 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[AREG]] | +0.51 | +0.35 / +0.56 | both halves | 1e-04 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[SORBS1]] | +0.51 | +0.25 / +0.55 | both halves | 4e-04 |  |
| [[AKAP13-AS1]] | +0.50 | +0.46 / +0.46 | both halves | 3e-05 |  |
| [[USP53]] | +0.50 | +0.48 / +0.47 | both halves | 2e-05 |  |
| [[VMP1]] | +0.50 | +0.50 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAPKAPK5]] | -0.55 | -0.36 / -0.62 | both halves | 9e-05 |  |
| [[POMK]] | -0.54 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[AIFM1]] | -0.51 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[PUS7L]] | -0.51 | -0.36 / -0.53 | both halves | 9e-05 |  |
| [[EXOSC10]] | -0.51 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[DNAAF10]] | -0.51 | -0.39 / -0.48 | both halves | 6e-05 |  |
| [[CPSF7]] | -0.50 | -0.35 / -0.55 | both halves | 1e-04 |  |
| [[SMPD4]] | -0.50 | -0.36 / -0.56 | both halves | 1e-04 |  |
| [[ZNF507]] | -0.49 | -0.32 / -0.49 | both halves | 1e-04 |  |
| [[DIS3L]] | -0.48 | -0.34 / -0.48 | both halves | 1e-04 |  |
| [[BRCC3]] | -0.48 | -0.36 / -0.44 | both halves | 9e-05 |  |
| [[COG8]] | -0.48 | -0.28 / -0.53 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PTAFR]] | B | PTAFR activity raises SAT1's level | lines that do not express PTAFR (29) vs lines expressing it (21) | 1.97× lower at baseline in the lines without PTAFR | 0.008 | ⚠ within organs, on part of the lines; also absent: TJP3, BSPRY, KDF1; maybe low, not absent |
| [[AREG]] | B | AREG activity raises SAT1's level | lines that do not express AREG (26) vs lines expressing it (24) | 2.01× lower at baseline in the lines without AREG | 0.024 | ⚠ within organs, on part of the lines; also absent: TC2N, ESRP1, CRB3 |
| [[TMEM92]] | B | TMEM92 activity raises SAT1's level | lines that do not express TMEM92 (22) vs lines expressing it (28) | 2.23× lower at baseline in the lines without TMEM92 | 0.033 | ⚠ within organs, on part of the lines; also absent: ARL14, LINC01589, TNFSF10 |
| [[RNF39]] | B | RNF39 activity raises SAT1's level | lines that do not express RNF39 (30) vs lines expressing it (20) | 2.09× lower at baseline in the lines without RNF39 | 0.067 | ⚠ within organs, on part of the lines; also absent: CDH1, TNNT2, TRIM15; maybe low, not absent |
| [[LCN2]] | B | LCN2 activity raises SAT1's level | lines that do not express LCN2 (33) vs lines expressing it (17) | 1.74× lower at baseline in the lines without LCN2 | 0.084 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: PRSS8, RAB25, TMPRSS4 |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HAPLN3]] | B | SAT1 activity raises HAPLN3's level | lines that do not express SAT1 (5) vs lines expressing it (45) | 2.22× lower at baseline in the lines without SAT1 | 0.081 | ⚠ within organs, on part of the lines; also absent: ITPR3, SQOR, KDELR3; maybe low, not absent; its own permutation p |
| [[MYO1E]] | B | SAT1 activity raises MYO1E's level | lines that do not express SAT1 (5) vs lines expressing it (45) | 2.67× lower at baseline in the lines without SAT1 | 0.087 | ⚠ within organs, on part of the lines; also absent: ITPR3, SQOR, KDELR3; maybe low, not absent |

## Where it sits

- **Module**: [[Module 153]]; 29 genes; every member is in the + arm (projection on the module's main direction -0.375). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-15.1, 28.5); signed map (2.1, 25.9). **Vector** length 121, 44.9% of its response variance represented; |z| ≥ 3 in 1,309 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +13.8 | +12.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +11.6 | +7.7 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +5.9 | +7.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +5.3 | +8.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.3 | +6.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +4.2 | +2.2 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +3.8 | +3.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.7 | +3.6 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -7.1 | -2.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | -5.1 | -3.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | -5.0 | -2.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.2 | +0.1 |
|  | [[EX229 (drug)]] 5 µM |  | -3.8 | -1.5 |
|  | [[venetoclax (drug)]] 5 µM |  | -3.8 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | spermidine/spermine N1-acetyltransferase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp22.11 — chrX:23,783,173-23,786,210 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SSAT; previously SAT |
| Gene groups (HGNC) | GCN5 related N-acetyltransferases |
| Hallmark sets | ANDROGEN_RESPONSE, APOPTOSIS, EPITHELIAL_MESENCHYMAL_TRANSITION, TNFA_SIGNALING_VIA_NFKB, P53_PATHWAY |
| Reactome | 3 pathways, smallest: Interconversion of polyamines; Metabolism of polyamines; Metabolism of amino acids and derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [P21673](https://www.uniprot.org/uniprotkb/P21673) (Diamine acetyltransferase 1):

> Enzyme which catalyzes the acetylation of polyamines. Substrate specificity: norspermidine = spermidine >> spermine > N(1)-acetylspermine. This highly regulated enzyme allows a fine attenuation of the intracellular concentration of polyamines. Also involved in the regulation of polyamine transport out of cells. Also acts on 1,3-diaminopropane and 1,5-diaminopentane.

**Summary**, from NCBI Gene [6303](https://www.ncbi.nlm.nih.gov/gene/6303):

> The protein encoded by this gene belongs to the acetyltransferase family, and is a rate-limiting enzyme in the catabolic pathway of polyamine metabolism. It catalyzes the acetylation of spermidine and spermine, and is involved in the regulation of the intracellular concentration of polyamines and their transport out of cells. Defects in this gene are associated with keratosis follicularis spinulosa decalvans (KFSD). Alternatively spliced transcripts have been found for this gene.[provided by …

**Accessions** — [HGNC:10540](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10540) · Entrez [6303](https://www.ncbi.nlm.nih.gov/gene/6303) · UniProt [P21673](https://www.uniprot.org/uniprotkb/P21673) · Ensembl [ENSG00000130066](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130066)

## Data

Gene col 5021: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5021); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5021, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5021]; `tensor/DDL_lfc|DDL_z.npy` [5021]; `embed/gene_vectors.npy` [5021]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5021 or target_col == 5021). Every well: [[SAT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SAT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
