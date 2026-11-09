---
symbol: "TAX1BP1"
type: "gene"
col: 2714
ensembl_id: "ENSG00000106052"
name: "Tax1 binding protein 1"
location: "7p15.2"
module: 69
arm: "+"
pooled_cpm: 412.49
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 9
n_dd_up_clean: 8
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/069"]
generated_by: "tahoemap"
---

# TAX1BP1

*Tax1 binding protein 1* — 7p15.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (13 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.55× (z +11.9, q 1e-29, up in 43 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.645× (z -8.6, q 3e-15, down in 45 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[TAK-733 (drug)]] 5 µM: 0.575× (z -5.7, q 2e-06, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RB1CC1]] (+0.67, fdr 1e-05), [[YPEL5]] (+0.65, fdr 1e-05), [[GABARAPL1]] (+0.60, fdr 1e-05); moves opposite to [[PDSS1]] (-0.66, fdr 3e-05), [[C19orf48]] (-0.60, fdr 3e-05), [[PFAS]] (-0.57, fdr 1e-05).
> It is in [[Module 069]], a single-armed module (FOXO-mediated transcription).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 14 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2714.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.55×** | +11.9 | 1e-29 | 43/49 (MIA PaCa-2, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.79×** | +11.5 | 4e-28 | 48/48 (H4, HEC-1-A, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.78×** | +11.4 | 8e-28 | 45/48 (BT-474, LoVo, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.78×** | +11.4 | 8e-28 | 48/48 (H4, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.74×** | +10.3 | 7e-23 | 47/48 (H4, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.55×** | +8.7 | 3e-16 | 40/49 (HEC-1-A, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.53×** | +8.1 | 5e-14 | 37/44 (A549, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.47×** | +7.6 | 2e-12 | 42/48 (AsPC-1, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +7.0 | 1e-10 | 36/48 (HEC-1-A, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +6.3 | 2e-08 | 37/50 (HEC-1-A, A-427, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.76×** | +5.8 | 3e-07 | 42/45 (KATO III, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~22% of this change | **1.36×** | +5.8 | 4e-07 | 34/47 (LoVo, COLO 205, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **1.34×** | +5.7 | 4e-07 | 31/48 (SW480, NCI-H460, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.43×** | +5.0 | 2e-05 | 42/49 (PANC-1, LOX-IMVI, …) | all doses, flat | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.31×** | +4.9 | 4e-05 | 30/45 (HEC-1-A, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.17× | +4.0 | 0.002 | 22/48 (HEC-1-A, HOP62, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.17× | +3.1 | 0.055 | 18/48 (MIA PaCa-2, HEC-1-A, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2714.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.645×** | -8.6 | 3e-15 | 45/48 (KATO III, LoVo, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.698×** | -6.8 | 3e-09 | 35/47 (C32, HT-29, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[TAK-733 (drug)]] 5 µM |  | **0.575×** | -5.7 | 2e-06 | 47/48 (KATO III, SW1417, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~77% of this change | 0.837× | -4.8 | 2e-04 | 24/48 (C32, AsPC-1, …) | inconsistent across doses | low cells (technical?) |
| [[EX229 (drug)]] 5 µM |  | **0.644×** | -4.5 | 6e-04 | 41/48 (KATO III, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.799×** | -4.4 | 9e-04 | 30/48 (C32, SW1417, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.688×** | -3.9 | 0.009 | 38/48 (KATO III, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.699×** | -3.7 | 0.015 | 32/48 (KATO III, A498, …) | rises with dose | noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.773×** | -3.6 | 0.018 | 32/48 (KATO III, BT-474, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.797×** | -3.2 | 0.078 | 29/48 (KATO III, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | 0.743× | -3.1 | 0.11 | 27/48 (KATO III, SW1417, …) | all doses, flat | noisy plate (z scaled) |
| [[Thymol (drug)]] 0.5 µM |  | 0.857× | -3.0 | 0.11 | 15/48 (LoVo, MIA PaCa-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, +0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2714. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 344 | 10 (5 ⚠) | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.37× (z +13.9) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.559× (z -9.3) ⚠ unreliable plate only |
| [[HEC-1-A (line)]] | alt | 243 | 10 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.58× (z +17.7) | — |
| [[HOP62 (line)]] | alt | 225 | 9 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.13× (z +13.1) | — |
| [[KATO III (line)]] | alt | 625 | 4 | 5 (2 ⚠) | [[Auranofin (drug)]] 5 µM 2.18× (z +13.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.379× (z -16.8) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.341× (z -9.7) |
| [[SNU-423 (line)]] | alt | 315 | 9 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.21× (z +11.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 339 | 7 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.87× (z +18.6) | — |
| [[C32 (line)]] | wt | 563 | 1 | 5 (5 ⚠) | [[Auranofin (drug)]] 5 µM 2.19× (z +13.1) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.397× (z -14.9) ⚠ toxic |
| [[HT-29 (line)]] | alt | 623 | 4 | 2 (2 ⚠) | [[Auranofin (drug)]] 5 µM 2.22× (z +15.2) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.466× (z -13.9) ⚠ toxic |
| [[LoVo (line)]] | wt | 568 | 5 (1 ⚠) | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.42× (z +15.6) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.467× (z -13.4) ⚠ unreliable plate only |
| [[PANC-1 (line)]] | alt | 479 | 6 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.40× (z +13.2) | — |
| [[SW 900 (line)]] | alt | 376 | 6 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.76× (z +11.5) | — |
| [[COLO 205 (line)]] | alt | 303 | 4 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.92× (z +11.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.447× (z -10.4) ⚠ unreliable plate only |
| [[H4 (line)]] | wt | 513 | 5 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.08× (z +14.2) | — |
| [[LOX-IMVI (line)]] | wt | 287 | 5 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.20× (z +10.9) | — |
| [[LS 180 (line)]] | wt | 403 | 4 (2 ⚠) | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.12× (z +12.7) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.548× (z -9.6) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 445 | 5 | 0 | [[Auranofin (drug)]] 5 µM 2.23× (z +10.2) | — |
| [[NCI-H460 (line)]] | wt | 349 | 5 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.20× (z +10.5) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 2.12× (z +10.0) | — |
| [[A-172 (line)]] | wt | 488 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.06× (z +10.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.57× (z +9.2) | — |
| [[AsPC-1 (line)]] | alt | 907 | 2 (1 ⚠) | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.07× (z +15.0) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.453× (z -11.8) ⚠ unreliable plate only |
| [[hTERT-HPNE (line)]] | wt | 312 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.27× (z +11.3) | — |
| [[RPMI-7951 (line)]] | alt | 400 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.91× (z +11.8) | — |
| [[A-427 (line)]] | wt | 361 | 3 | 0 | [[Auranofin (drug)]] 5 µM 2.49× (z +13.2) | — |
| [[CFPAC-1 (line)]] | alt | 214 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.13× (z +15.1) | — |
| [[HCT15 (line)]] | alt | 391 | 3 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.16× (z +9.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.06× (z +8.9) | — |
| [[HS-578T (line)]] | alt | 471 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.67× (z +9.8) | — |
| [[J82 (line)]] | alt | 297 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.07× (z +10.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.65× (z +9.8) | — |
| [[Panc 03.27 (line)]] | alt | 372 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.82× (z +13.4) | — |
| [[A498 (line)]] | wt | 529 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 1.68× (z +8.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.504× (z -11.5) ⚠ unreliable plate only |
| [[A549 (line)]] | wt | 347 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.20× (z +11.1) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 455 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.10× (z +17.9) | — |
| [[Hs 766T (line)]] | wt | 437 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.81× (z +11.0) | — |
| [[NCI-H2347 (line)]] | alt | 452 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.73× (z +12.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.481× (z -12.2) ⚠ unreliable plate only |
| [[SW1417 (line)]] | alt | 617 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.504× (z -12.7) ⚠ unreliable plate only |
| [[AN3 CA (line)]] | alt | 449 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.11× (z +8.5) | — |
| [[C-33 A (line)]] | alt | 254 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.31× (z +9.3) | — |
| [[NCI-H1573 (line)]] | alt | 227 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.53× (z +9.3) | — |
| [[NCI-H2030 (line)]] | alt | 407 | 1 | 0 | [[Bortezomib (drug)]] 0.05 µM 1.84× (z +8.5) | — |
| [[RKO (line)]] | wt | 289 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.37× (z +10.7) | — |
| [[SHP-77 (line)]] | alt | 414 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.52× (z +9.1) | — |
| [[SK-MEL-2 (line)]] | alt | 663 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.00× (z +10.6) | — |
| [[SW48 (line)]] | wt | 456 | 1 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 1.97× (z +8.5) | — |
| [[CHP-212 (line)]] | wt | 214 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 389 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 317 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 429 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 395 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 386 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 310 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 519 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 363 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2714), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*46 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RB1CC1]] | +0.67 | +0.52 / +0.73 | both halves | 1e-05 | STRING 817 |
| [[YPEL5]] | +0.65 | +0.52 / +0.70 | both halves | 1e-05 |  |
| [[GABARAPL1]] | +0.60 | +0.50 / +0.62 | both halves | 1e-05 | STRING 987 |
| [[SMIM14]] | +0.58 | +0.34 / +0.65 | both halves | 1e-04 |  |
| [[TCP11L2]] | +0.57 | +0.40 / +0.62 | both halves | 5e-05 |  |
| [[JMY]] | +0.57 | +0.35 / +0.64 | both halves | 1e-04 |  |
| [[SLU7]] | +0.54 | +0.35 / +0.57 | both halves | 1e-04 |  |
| [[CCDC186]] | +0.54 | +0.41 / +0.57 | both halves | 4e-05 |  |
| [[MAP1LC3B]] | +0.53 | +0.41 / +0.58 | both halves | 4e-05 | STRING 754 |
| [[PINK1]] | +0.53 | +0.45 / +0.57 | both halves | 3e-05 | STRING 615 |
| [[KDM6A]] | +0.52 | +0.35 / +0.56 | both halves | 1e-04 |  |
| [[PNPLA8]] | +0.52 | +0.44 / +0.60 | both halves | 3e-05 |  |

## Genes that move opposite

*54 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDSS1]] | -0.66 | -0.46 / -0.72 | both halves | 3e-05 |  |
| [[C19orf48]] | -0.60 | -0.45 / -0.67 | both halves | 3e-05 |  |
| [[PFAS]] | -0.57 | -0.61 / -0.51 | both halves | 1e-05 |  |
| [[CAD]] | -0.57 | -0.51 / -0.56 | both halves | 1e-05 |  |
| [[TBRG4]] | -0.56 | -0.49 / -0.59 | both halves | 1e-05 |  |
| [[CLN6]] | -0.55 | -0.48 / -0.59 | both halves | 2e-05 |  |
| [[FARSA]] | -0.54 | -0.35 / -0.61 | both halves | 1e-04 |  |
| [[NLE1]] | -0.54 | -0.37 / -0.60 | both halves | 8e-05 |  |
| [[THOP1]] | -0.54 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[WDR75]] | -0.53 | -0.35 / -0.60 | both halves | 1e-04 |  |
| [[EXOSC2]] | -0.53 | -0.46 / -0.56 | both halves | 3e-05 |  |
| [[RIOK1]] | -0.53 | -0.37 / -0.56 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TAX1BP1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 069]] — FOXO-mediated transcription; 71 genes; every member is in the + arm (projection on the module's main direction 0.548). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-1.9, -44.4); signed map (-13.1, 11.1). **Vector** length 140, 59.1% of its response variance represented; |z| ≥ 3 in 1,458 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +10.8 | +11.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +8.2 | +10.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +7.6 | +11.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +7.3 | +11.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +7.2 | +6.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.9 | +1.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +4.8 | +1.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.2 | +4.0 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -15.2 | -8.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -11.4 | -6.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | -9.0 | -5.7 |
|  | [[EX229 (drug)]] 5 µM |  | -8.9 | -4.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -8.5 | -3.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -8.4 | -3.9 |
|  | [[venetoclax (drug)]] 5 µM |  | -7.3 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | Tax1 binding protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p15.2 — chr7:27,739,331-27,844,564 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TXBP151, CALCOCO3 |
| Gene groups (HGNC) | Zinc fingers UBZ1 CCHH-type |
| Reactome | 6 pathways, smallest: Negative regulators of DDX58/IFIH1 signaling; Regulation of TNFR1 signaling; TNF signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86VP1](https://www.uniprot.org/uniprotkb/Q86VP1) (Tax1-binding protein 1):

> Ubiquitin-binding adapter that participates in inflammatory, antiviral and innate immune processes as well as selective autophagy regulation. Plays a key role in the negative regulation of NF-kappa-B and IRF3 signalings by acting as an adapter for the ubiquitin-editing enzyme A20/TNFAIP3 to bind and inactivate its substrates. Disrupts the interactions between the E3 ubiquitin ligase TRAF3 and TBK1/IKBKE to attenuate 'Lys63'-linked polyubiquitination of TBK1 and thereby IFN-beta production. Also …

**Summary**, from NCBI Gene [8887](https://www.ncbi.nlm.nih.gov/gene/8887):

> This gene encodes a HTLV-1 tax1 binding protein. The encoded protein interacts with TNFAIP3, and inhibits TNF-induced apoptosis by mediating the TNFAIP3 anti-apoptotic activity. Degradation of this protein by caspase-3-like family proteins is associated with apoptosis induced by TNF. This protein may also have a role in the inhibition of inflammatory signaling pathways. Alternatively spliced transcript variants encoding different isoforms have been found for this gene.[provided by RefSeq, May …

**Accessions** — [HGNC:11575](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11575) · Entrez [8887](https://www.ncbi.nlm.nih.gov/gene/8887) · UniProt [Q86VP1](https://www.uniprot.org/uniprotkb/Q86VP1) · Ensembl [ENSG00000106052](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106052)

## Data

Gene col 2714: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2714); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2714, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2714]; `tensor/DDL_lfc|DDL_z.npy` [2714]; `embed/gene_vectors.npy` [2714]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2714 or target_col == 2714). Every well: [[TAX1BP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TAX1BP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
