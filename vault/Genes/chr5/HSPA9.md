---
symbol: "HSPA9"
type: "gene"
col: 3426
ensembl_id: "ENSG00000113013"
name: "heat shock protein family A (Hsp70) member 9"
location: "5q31.2"
module: 63
arm: "+"
pooled_cpm: 336.75
n_lines_expressing: 50
n_dd_up: 40
n_dd_down: 6
n_dd_up_clean: 28
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 8
direction_downstream: 0
tags: ["gene", "module/063"]
generated_by: "tahoemap"
---

# HSPA9

*heat shock protein family A (Hsp70) member 9* — 5q31.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 40 drug-doses (12 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 2.89× (z +17.1, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.745× (z -6.7, q 9e-09, down in 33 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IARS1]] (+0.89, fdr 7e-06), [[NARS1]] (+0.82, fdr 7e-06), [[XPOT]] (+0.82, fdr 7e-06); moves opposite to [[POLR2L]] (-0.58, fdr 1e-05), [[TMEM50A]] (-0.49, fdr 3e-05), [[MMD]] (-0.49, fdr 4e-05).
> It is in [[Module 063]], a single-armed module (ISR ATF4).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[ANK2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 46 in all, 14 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 40 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3426.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **2.89×** | +17.1 | 0e+00 | 48/48 (C32, SHP-77, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.35×** | +13.7 | 2e-40 | 47/48 (HEC-1-A, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.13×** | +11.4 | 6e-28 | 48/48 (HEC-1-A, HOP62, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.01×** | +10.6 | 3e-24 | 46/48 (HEC-1-A, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.98×** | +10.6 | 5e-24 | 45/47 (COLO 205, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.37×** | +10.2 | 2e-22 | 48/49 (NCI-H23, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.78×** | +9.3 | 2e-18 | 45/48 (Panc 03.27, Hs 766T, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.94×** | +9.1 | 9e-18 | 41/48 (RKO, SK-MEL-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.62×** | +7.7 | 7e-13 | 38/49 (SW480, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.57×** | +7.3 | 2e-11 | 40/48 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.56×** | +7.1 | 5e-11 | 42/48 (Panc 03.27, SW480, …) | top dose only |  |
| [[Artesunate (drug)]] 5 µM |  | **1.35×** | +6.7 | 8e-10 | 38/48 (SNU-1, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **2.19×** | +6.6 | 2e-09 | 47/48 (LOX-IMVI, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.49×** | +6.2 | 3e-08 | 33/44 (HepG2/C3A, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.91×** | +5.5 | 2e-06 | 41/45 (Panc 03.27, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.90×** | +5.4 | 3e-06 | 41/48 (Hs 766T, SNU-1, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.87×** | +5.3 | 5e-06 | 40/48 (Panc 03.27, CFPAC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.55×** | +5.1 | 1e-05 | 41/49 (C32, Panc 03.27, …) | all doses, flat | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **1.37×** | +5.0 | 2e-05 | 40/48 (SNU-1, Hs 766T, …) | rises with dose |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **1.36×** | +4.9 | 2e-05 | 34/47 (SNU-1, BT-474, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3426.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.745×** | -6.7 | 9e-09 | 33/49 (RKO, LoVo, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.786×** | -3.6 | 0.081 | 25/47 (LoVo, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.807×** | -3.5 | 0.081 | 28/48 (PANC-1, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.811×** | -3.4 | 0.081 | 27/49 (RKO, A498, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.800×** | -3.4 | 0.081 | 23/48 (A-427, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.810×** | -3.3 | 0.098 | 23/47 (MIA PaCa-2, AsPC-1, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.871× | -3.2 | 0.12 | 17/48 (HT-29, A498, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3426. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 245 | 15 (6 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.18× (z +15.4) | — |
| [[NCI-H460 (line)]] | wt | 355 | 14 (8 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.29× (z +14.8) | — |
| [[SNU-1 (line)]] | wt | 534 | 13 (4 ⚠) | 0 | [[Chlorhexidine (diacetate) (drug)]] 5 µM 3.10× (z +18.3) | — |
| [[SW480 (line)]] | alt | 282 | 11 (4 ⚠) | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.13× (z +15.4) | [[Homoharringtonine (drug)]] 5 µM 0.621× (z -9.2) ⚠ cell-cycle shift, explains ~85% of this change |
| [[Panc 03.27 (line)]] | alt | 192 | 11 (4 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.22× (z +16.9) | — |
| [[HT-29 (line)]] | alt | 357 | 6 (1 ⚠) | 4 (3 ⚠) | [[Auranofin (drug)]] 5 µM 2.97× (z +14.4) | [[Harringtonine (drug)]] 5 µM 0.414× (z -11.3) ⚠ cell-cycle shift, explains ~97% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.473× (z -10.0) |
| [[Hs 766T (line)]] | wt | 267 | 9 (4 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.51× (z +12.3) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 3.23× (z +11.9) | — |
| [[LoVo (line)]] | wt | 563 | 5 (1 ⚠) | 4 (2 ⚠) | [[Auranofin (drug)]] 5 µM 3.15× (z +16.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.486× (z -14.7) |
| [[NCI-H1573 (line)]] | alt | 222 | 9 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.74× (z +15.0) | — |
| [[HOP62 (line)]] | alt | 172 | 8 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 5.64× (z +17.4) | — |
| [[AsPC-1 (line)]] | alt | 301 | 7 (3 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.74× (z +12.2) | — |
| [[COLO 205 (line)]] | alt | 299 | 7 (3 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 8.65× (z +17.8) ⚠ toxic · without an alert: [[TAK-901 (drug)]] 5 µM 12.9× (z +11.5) | — |
| [[SK-MEL-2 (line)]] | alt | 336 | 7 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.22× (z +16.3) | — |
| [[A498 (line)]] | wt | 333 | 5 (1 ⚠) | 1 | [[Auranofin (drug)]] 5 µM 2.56× (z +13.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.651× (z -8.7) |
| [[C32 (line)]] | wt | 170 | 6 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 9.91× (z +20.8) | — |
| [[PANC-1 (line)]] | alt | 491 | 1 | 5 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.21× (z +9.7) | [[Panobinostat (drug)]] 5 µM 0.374× (z -15.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.404× (z -14.7) |
| [[A-172 (line)]] | wt | 275 | 5 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.91× (z +16.9) | — |
| [[HEC-1-A (line)]] | alt | 262 | 5 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.49× (z +14.0) | — |
| [[hTERT-HPNE (line)]] | wt | 230 | 5 | 0 | [[Auranofin (drug)]] 5 µM 3.33× (z +13.2) | — |
| [[RKO (line)]] | wt | 574 | 3 | 2 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.96× (z +16.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.415× (z -18.8) |
| [[A-427 (line)]] | wt | 591 | 1 | 3 (1 ⚠) | [[Auranofin (drug)]] 5 µM 1.74× (z +8.8) | [[Panobinostat (drug)]] 0.5 µM 0.425× (z -12.9) |
| [[A549 (line)]] | wt | 279 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +11.8) ⚠ cell-cycle shift, explains ~85% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.48× (z +9.4) | — |
| [[BT-474 (line)]] | alt | 262 | 4 | 0 | [[Auranofin (drug)]] 5 µM 4.21× (z +17.2) | — |
| [[CFPAC-1 (line)]] | alt | 210 | 4 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.13× (z +10.8) | — |
| [[HepG2_C3A (line)]] | wt | 272 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.74× (z +10.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.43× (z +9.8) | — |
| [[KATO III (line)]] | alt | 364 | 1 | 3 (3 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.24× (z +9.5) | [[Harringtonine (drug)]] 5 µM 0.337× (z -12.4) ⚠ cell-cycle shift, explains ~97% of this change |
| [[NCI-H2030 (line)]] | alt | 344 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +11.4) ⚠ cell-cycle shift, explains ~85% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.58× (z +9.6) | — |
| [[NCI-H23 (line)]] | alt | 385 | 3 (1 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.44× (z +11.8) | [[Panobinostat (drug)]] 5 µM 0.520× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW 900 (line)]] | alt | 252 | 4 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.14× (z +14.0) | — |
| [[SW1417 (line)]] | alt | 401 | 4 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 2.40× (z +12.2) | — |
| [[AN3 CA (line)]] | alt | 379 | 3 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 5.04× (z +17.1) | — |
| [[NCI-H1792 (line)]] | alt | 196 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.03× (z +10.1) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 299 | 3 | 0 | [[Auranofin (drug)]] 5 µM 2.81× (z +10.6) | — |
| [[SHP-77 (line)]] | alt | 315 | 3 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.88× (z +18.2) | — |
| [[SNU-423 (line)]] | alt | 319 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +12.6) ⚠ cell-cycle shift, explains ~85% of this change · without an alert: [[Auranofin (drug)]] 5 µM 4.11× (z +12.4) | — |
| [[SW48 (line)]] | wt | 450 | 2 | 1 | [[Auranofin (drug)]] 5 µM 2.29× (z +9.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.504× (z -11.0) |
| [[C-33 A (line)]] | alt | 333 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.53× (z +10.1) | [[Homoharringtonine (drug)]] 5 µM 0.459× (z -12.3) ⚠ cell-cycle shift, explains ~85% of this change |
| [[H4 (line)]] | wt | 542 | 1 | 1 | [[Auranofin (drug)]] 5 µM 2.59× (z +9.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.428× (z -12.4) |
| [[HS-578T (line)]] | alt | 370 | 2 | 0 | [[Auranofin (drug)]] 5 µM 2.98× (z +12.3) | — |
| [[J82 (line)]] | alt | 277 | 2 | 0 | [[Auranofin (drug)]] 5 µM 2.03× (z +9.0) | — |
| [[RPMI-7951 (line)]] | alt | 238 | 2 | 0 | [[Auranofin (drug)]] 5 µM 4.16× (z +14.1) | — |
| [[CHP-212 (line)]] | wt | 261 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.495× (z -8.6) ⚠ cell-cycle shift, explains ~85% of this change |
| [[HCT15 (line)]] | alt | 452 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.79× (z +9.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 578 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.43× (z +11.0) | — |
| [[SW 1271 (line)]] | alt | 280 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.54× (z +8.9) | — |
| [[LS 180 (line)]] | wt | 343 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 281 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 328 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 383 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 297 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3426), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IARS1]] | +0.89 | +0.88 / +0.89 | both halves | 7e-06 | same gene group; pathway: HALLMARK_UNFOLDED_PROTEIN_RESPONSE; STRING 541 |
| [[NARS1]] | +0.82 | +0.75 / +0.79 | both halves | 7e-06 | **novel candidate** |
| [[XPOT]] | +0.82 | +0.78 / +0.82 | both halves | 7e-06 | pathway: HALLMARK_UNFOLDED_PROTEIN_RESPONSE |
| [[AARS1]] | +0.80 | +0.76 / +0.80 | both halves | 7e-06 |  |
| [[YARS1]] | +0.78 | +0.71 / +0.80 | both halves | 7e-06 | STRING 424 |
| [[TRIB3]] | +0.78 | +0.78 / +0.72 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING |
| [[TARS1]] | +0.77 | +0.73 / +0.78 | both halves | 7e-06 | pathway: HALLMARK_UNFOLDED_PROTEIN_RESPONSE; STRING 402 |
| [[MTHFD2]] | +0.75 | +0.72 / +0.76 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING |
| [[GARS1]] | +0.74 | +0.74 / +0.73 | both halves | 7e-06 | STRING 443 |
| [[RSL24D1]] | +0.74 | +0.75 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[ASNS]] | +0.73 | +0.72 / +0.72 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING |
| [[SLC7A11]] | +0.73 | +0.67 / +0.76 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLR2L]] | -0.58 | -0.56 / -0.56 | both halves | 1e-05 |  |
| [[TMEM50A]] | -0.49 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[MMD]] | -0.49 | -0.43 / -0.50 | both halves | 4e-05 |  |
| [[SKA2]] | -0.49 | -0.52 / -0.40 | both halves | 5e-05 |  |
| [[SP3]] | -0.48 | -0.38 / -0.48 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 3, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANK2]] | B | ANK2 activity raises HSPA9's level | lines that do not express ANK2 (16) vs lines expressing it (34) | 1.24× lower at baseline in the lines without ANK2 | 0.015 | ⚠ within organs, on part of the lines; also absent: VASH1, SOBP, GXYLT2; maybe low, not absent |
| [[ASNSP1]] | B | ASNSP1 activity raises HSPA9's level | lines that do not express ASNSP1 (35) vs lines expressing it (15) | 1.23× lower at baseline in the lines without ASNSP1 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZNF208, GCG, GPR15 |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises HSPA9's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[SESN2]] | C | SESN2's natural level weakens HSPA9's drug response | SESN2's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.65, reverse +0.07; direction not clear | 0.044 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[MTHFD2]] | C | MTHFD2's natural level weakens HSPA9's drug response | MTHFD2's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.63, reverse +0.07; direction not clear | 0.062 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[XPOT]] | C | XPOT's natural level weakens HSPA9's drug response | XPOT's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.62, reverse +0.27; direction not clear | 0.075 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[GARS1]] | C | GARS1's natural level weakens HSPA9's drug response | GARS1's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.62, reverse +0.05; direction not clear | 0.079 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[ASNS]] | C | ASNS activity raises HSPA9's level | lines that do not express ASNS (4) vs lines expressing it (46) | 1.67× lower at baseline in the lines without ASNS | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: PPEF1; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 063]] — ISR ATF4; 77 genes; every member is in the + arm (projection on the module's main direction 0.830). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-17.4, 47.2); signed map (-13.8, 24.1). **Vector** length 129, 58.9% of its response variance represented; |z| ≥ 3 in 1,755 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *ISR ATF4* (control, mean cos +0.67 to 16); *Cytosolic tRNA aminoacylation* (reactome, mean cos +0.76 to 9); *tRNA Aminoacylation* (reactome, mean cos +0.76 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +10.5 | +17.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +9.7 | +9.3 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +8.7 | +10.6 |
|  | [[Artesunate (drug)]] 5 µM |  | +7.4 | +6.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +7.2 | +7.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.4 | +11.4 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +6.0 | +3.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +5.9 | +5.3 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | -6.7 | +5.1 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -6.7 | +0.1 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | -6.6 | +3.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -6.5 | +3.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~97% of this change | -6.4 | +1.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -4.8 | -3.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.5 | -0.5 |
|  | [[8-Hydroxyquinoline (drug)]] 5 µM |  | -2.1 | -0.9 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -2.1 | -1.4 |
|  | [[Adenine (drug)]] 5 µM |  | -1.8 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | heat shock protein family A (Hsp70) member 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q31.2 — chr5:138,553,756-138,575,675 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GRP75, PBP74, mot-2, mthsp75; previously HSPA9B |
| Gene groups (HGNC) | Heat shock 70kDa proteins; Small nucleolar RNA protein coding host genes |
| Hallmark sets | UNFOLDED_PROTEIN_RESPONSE, MTORC1_SIGNALING, OXIDATIVE_PHOSPHORYLATION |
| Reactome | 20 pathways, smallest: Mitochondrial unfolded protein response (UPRmt); Complex III assembly; Gene and protein expression by JAK-STAT signaling after Interleukin-12 stimulation |
| Matched by | ensembl_id |

**Function**, from UniProt [P38646](https://www.uniprot.org/uniprotkb/P38646) (Stress-70 protein, mitochondrial):

> Mitochondrial chaperone that plays a key role in mitochondrial protein import, folding, and assembly. Plays an essential role in the protein quality control system, the correct folding of proteins, the re-folding of misfolded proteins, and the targeting of proteins for subsequent degradation. These processes are achieved through cycles of ATP binding, ATP hydrolysis, and ADP release, mediated by co-chaperones. In mitochondria, it associates with the TIM (translocase of the inner membrane) …

**Summary**, from NCBI Gene [3313](https://www.ncbi.nlm.nih.gov/gene/3313):

> This gene encodes a member of the heat shock protein 70 gene family. The encoded protein is primarily localized to the mitochondria but is also found in the endoplasmic reticulum, plasma membrane and cytoplasmic vesicles. This protein is a heat-shock cognate protein. This protein plays a role in cell proliferation, stress response and maintenance of the mitochondria. A pseudogene of this gene is found on chromosome 2.[provided by RefSeq, May 2010]

**Accessions** — [HGNC:5244](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5244) · Entrez [3313](https://www.ncbi.nlm.nih.gov/gene/3313) · UniProt [P38646](https://www.uniprot.org/uniprotkb/P38646) · Ensembl [ENSG00000113013](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000113013)

## Data

Gene col 3426: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3426); `tables/drug_effects.parquet` (53 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3426, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3426]; `tensor/DDL_lfc|DDL_z.npy` [3426]; `embed/gene_vectors.npy` [3426]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3426 or target_col == 3426). Every well: [[HSPA9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HSPA9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
