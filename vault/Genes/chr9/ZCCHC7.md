---
symbol: "ZCCHC7"
type: "gene"
col: 7233
ensembl_id: "ENSG00000147905"
name: "zinc finger CCHC-type containing 7"
location: "9p13.2"
module: 40
arm: "+"
pooled_cpm: 433.39
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 16
n_dd_up_clean: 3
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/040"]
generated_by: "tahoemap"
---

# ZCCHC7

*zinc finger CCHC-type containing 7* — 9p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 1.29× (z +6.1, q 8e-07, up in 33 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.343× (z -25.3, q 0e+00, down in 49 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 0.05 µM: 0.796× (z -5.4, q 4e-06, down in 31 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC37A3]] (+0.74, fdr 7e-06), [[COG5]] (+0.72, fdr 7e-06), [[ELP2]] (+0.70, fdr 7e-06); moves opposite to [[DPY19L2P2-1]] (-0.56, fdr 1e-05), [[PPP2CA]] (-0.56, fdr 1e-05), [[MED12]] (-0.55, fdr 3e-05).
> It sits in the **+** arm of [[Module 040]] (Asparagine N-linked glycosylation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7233.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **1.29×** | +6.1 | 8e-07 | 33/48 (AsPC-1, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.28×** | +5.7 | 3e-06 | 31/48 (SW480, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Verteporfin (drug)]] 5 µM |  | 1.20× | +4.1 | 0.008 | 23/49 (SHP-77, HepG2/C3A, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 1.18× | +3.7 | 0.029 | 20/47 (NCI-H23, RKO, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.4 | 0.057 | 19/48 (SW480, RKO, …) | top dose only |  |
| [[Sapanisertib (drug)]] 5 µM |  | **1.32×** | +3.4 | 0.057 | 28/49 (MIA PaCa-2, Hs 766T, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.10× | +3.1 | 0.15 | 5/49 (MIA PaCa-2, A-427, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.10× | +3.0 | 0.15 | 3/48 (SK-MEL-2, SW1417, …) | top dose only |  |
| [[BAY1125976 (drug)]] 5 µM |  | 1.28× | +3.0 | 0.15 | 17/48 (MIA PaCa-2, C-33 A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 17 with an alert ⚠; shown: the 15 strongest and the 11 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7233.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.343×** | -25.3 | 0e+00 | 49/49 (A498, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.336×** | -24.8 | 0e+00 | 44/44 (C-33 A, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.371×** | -21.6 | 0e+00 | 44/45 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.654×** | -9.7 | 7e-20 | 41/47 (SW1417, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~29% of this change | **0.667×** | -9.6 | 1e-19 | 47/48 (HOP62, KATO III, …) | all doses, flat | low cells (technical?) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.665×** | -9.3 | 2e-18 | 39/48 (A498, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **0.789×** | -7.9 | 2e-13 | 29/48 (A498, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.749×** | -6.8 | 6e-10 | 36/48 (A-172, HS-578T, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.796×** | -5.4 | 4e-06 | 31/48 (HS-578T, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | 0.877× | -4.4 | 6e-04 | 21/49 (A549, A498, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.833×** | -4.3 | 8e-04 | 22/48 (SW480, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.718×** | -4.1 | 0.002 | 24/49 (A-172, SW48, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~42% of this change | 0.842× | -4.1 | 0.002 | 20/48 (LOX-IMVI, H4, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 0.05 µM |  | 0.849× | -3.9 | 0.004 | 17/48 (H4, Hs 766T, …) | inconsistent across doses |  |
| [[venetoclax (drug)]] 5 µM |  | **0.733×** | -3.8 | 0.005 | 32/48 (NCI-H661, A-427, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.845× | -3.7 | 0.007 | 19/47 (A-172, H4, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.866× | -3.4 | 0.018 | 15/48 (H4, A498, …) | inconsistent across doses |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | 0.868× | -3.3 | 0.022 | 10/49 (hTERT-HPNE, H4, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | 0.869× | -3.3 | 0.022 | 10/48 (SNU-1, NCI-H1573, …) | inconsistent across doses |  |
| [[Infigratinib (drug)]] 0.05 µM |  | 0.838× | -3.3 | 0.024 | 21/48 (KATO III, A549, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Busulfan (drug)]] 0.05 µM |  | 0.871× | -3.3 | 0.024 | 9/49 (HT-29, SW 900, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 5 µM |  | 0.909× | -3.2 | 0.031 | 2/48 (HCT15, SW 900) | all doses, flat |  |
| [[Apalutamide (drug)]] 0.5 µM |  | 0.881× | -3.0 | 0.054 | 6/48 (SW 1088, PANC-1, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | 0.881× | -3.0 | 0.055 | 20/48 (RKO, hTERT-HPNE, …) | top dose only |  |
| [[Carbamazepine (drug)]] 5 µM |  | 0.883× | -3.0 | 0.059 | 8/47 (PANC-1, hTERT-HPNE, …) | top dose only |  |
| [[Flutamide (drug)]] 5 µM |  | 0.884× | -2.9 | 0.066 | 2/48 (Panc 03.27, NCI-H1792) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7233. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 866 | 0 | 9 (9 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.177× (z -29.2) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 366 | 0 | 8 (8 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.336× (z -18.3) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 263 | 0 | 7 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.343× (z -16.9) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 488 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.294× (z -20.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.592× (z -9.2) |
| [[A549 (line)]] | wt | 519 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.279× (z -18.9) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 393 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.312× (z -17.0) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 636 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.193× (z -19.3) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 948 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.181× (z -22.7) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 551 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.197× (z -21.0) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 400 | 2 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.55× (z +10.0) ⚠ cell-cycle shift, explains ~71% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 1.74× (z +8.9) | [[Dinaciclib (drug)]] 0.05 µM 0.314× (z -17.3) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 299 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.350× (z -16.9) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 435 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.327× (z -14.7) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 235 | 0 | 4 (4 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0838× (z -16.7) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 428 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.252× (z -19.0) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 501 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.219× (z -18.2) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 437 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.292× (z -16.9) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 375 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.287× (z -18.0) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 200 | 1 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.85× (z +8.9) ⚠ cell-cycle shift, explains ~0% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.464× (z -10.8) ⚠ toxic |
| [[Panc 03.27 (line)]] | alt | 282 | 0 | 4 (4 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0530× (z -22.3) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 478 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.244× (z -22.5) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 449 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.149× (z -23.2) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 424 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.285× (z -23.4) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 449 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0891× (z -36.7) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 532 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.194× (z -18.6) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 682 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.152× (z -21.2) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 259 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.363× (z -13.8) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 404 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.235× (z -21.5) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 507 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.223× (z -22.4) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 376 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.371× (z -14.7) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 247 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.165× (z -26.6) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 370 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.213× (z -22.1) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 1,036 | 1 (1 ⚠) | 2 (2 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 1.82× (z +9.4) ⚠ toxic; cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.175× (z -28.6) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 534 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.234× (z -23.4) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 351 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.331× (z -17.3) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 396 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.296× (z -18.8) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 287 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.321× (z -18.1) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 362 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.189× (z -16.2) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 414 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.238× (z -19.4) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 546 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.240× (z -16.9) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 251 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.386× (z -13.4) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 287 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.426× (z -12.7) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 352 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.372× (z -11.9) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 163 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.448× (z -10.1) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 200 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 339 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 150 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 395 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 279 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 551 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 307 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7233), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC37A3]] | +0.74 | +0.77 / +0.66 | both halves | 7e-06 |  |
| [[COG5]] | +0.72 | +0.71 / +0.67 | both halves | 7e-06 |  |
| [[ELP2]] | +0.70 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[PIBF1]] | +0.69 | +0.65 / +0.69 | both halves | 7e-06 |  |
| [[DYM]] | +0.69 | +0.70 / +0.60 | both halves | 7e-06 |  |
| [[WRN]] | +0.62 | +0.65 / +0.49 | both halves | 1e-05 |  |
| [[HM13]] | +0.62 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[ANKS3]] | +0.61 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[CBLB]] | +0.61 | +0.58 / +0.58 | both halves | 8e-06 |  |
| [[SND1]] | +0.61 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[PDIA5]] | +0.60 | +0.65 / +0.50 | both halves | 1e-05 |  |
| [[RARS2]] | +0.60 | +0.62 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DPY19L2P2-1]] | -0.56 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[PPP2CA]] | -0.56 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[MED12]] | -0.55 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[DCLRE1A]] | -0.54 | -0.57 / -0.46 | both halves | 3e-05 |  |
| [[VEZF1]] | -0.53 | -0.55 / -0.46 | both halves | 3e-05 |  |
| [[SMG7]] | -0.53 | -0.41 / -0.52 | both halves | 4e-05 |  |
| [[ZNF772]] | -0.53 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[ZNF620]] | -0.53 | -0.55 / -0.43 | both halves | 3e-05 |  |
| [[ZNF780A]] | -0.53 | -0.62 / -0.41 | both halves | 4e-05 |  |
| [[ZNF436]] | -0.52 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[ZNF260]] | -0.52 | -0.53 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 040]] — Asparagine N-linked glycosylation; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.662). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (2.8, -20.7); signed map (-44.9, 7.3). **Vector** length 143, 56.5% of its response variance represented; |z| ≥ 3 in 1,239 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +5.4 | +5.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.3 | +6.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.0 | +1.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | +4.9 | +3.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.6 | +3.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.2 | +2.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | +3.2 | +4.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.9 | +2.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.9 | +0.6 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | -9.5 | -7.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -7.0 | -9.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -6.7 | -9.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | -6.3 | -3.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.0 | -21.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | -5.7 | -2.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.1 | -5.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | -4.2 | -3.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -4.1 | -2.6 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -4.1 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger CCHC-type containing 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p13.2 — chr9:37,120,574-37,358,149 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ22611, AIR1 |
| Gene groups (HGNC) | Zinc fingers CCHC-type |
| Reactome | 2 pathways, smallest: Nuclear RNA decay; Metabolism of RNA |
| Matched by | ensembl_id |

UniProt [Q8N3Z6](https://www.uniprot.org/uniprotkb/Q8N3Z6) carries no function annotation.

**Summary**, from NCBI Gene [84186](https://www.ncbi.nlm.nih.gov/gene/84186):

> Enables RNA binding activity. Predicted to be involved in nuclear RNA surveillance. Located in cytosol and nucleolus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26209](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26209) · Entrez [84186](https://www.ncbi.nlm.nih.gov/gene/84186) · UniProt [Q8N3Z6](https://www.uniprot.org/uniprotkb/Q8N3Z6) · Ensembl [ENSG00000147905](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000147905)

## Data

Gene col 7233: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7233); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7233, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7233]; `tensor/DDL_lfc|DDL_z.npy` [7233]; `embed/gene_vectors.npy` [7233]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7233 or target_col == 7233). Every well: [[ZCCHC7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZCCHC7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
