---
symbol: "RTN4"
type: "gene"
col: 3657
ensembl_id: "ENSG00000115310"
name: "reticulon 4"
location: "2p16.1"
module: 136
arm: "+"
pooled_cpm: 553.21
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 12
n_dd_up_clean: 17
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/136"]
generated_by: "tahoemap"
---

# RTN4

*reticulon 4* — 2p16.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (7 with an alert ⚠); the strongest is [[Vinblastine (sulfate) (drug)]] 5 µM: 1.30× (z +9.6, q 7e-19, up in 32 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.766× (z -9.7, q 2e-19, down in 29 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LRRFIP1]] (+0.71, fdr 7e-06), [[FLNB]] (+0.60, fdr 1e-05), [[CORO1C]] (+0.59, fdr 1e-05); moves opposite to [[JADE2]] (-0.57, fdr 3e-05), [[HNF1A]] (-0.56, fdr 3e-05), [[MACROH2A2]] (-0.54, fdr 4e-05).
> It is in [[Module 136]], a single-armed module (heme metabolism).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[STAP2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 15 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3657.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.30×** | +9.6 | 7e-19 | 32/49 (HT-29, A-427, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.41×** | +8.9 | 2e-16 | 36/48 (KATO III, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.41×** | +8.8 | 2e-16 | 35/48 (NCI-H460, SNU-1, …) | two highest doses | cell-cycle shift (explains ~12% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.23×** | +7.5 | 7e-12 | 26/48 (RKO, C-33 A, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~20% of this change | **1.34×** | +7.4 | 1e-11 | 28/48 (SNU-1, NCI-H460, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.33×** | +7.3 | 3e-11 | 33/48 (LS 180, HT-29, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.32×** | +7.2 | 4e-11 | 32/48 (A-427, KATO III, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.34×** | +7.1 | 1e-10 | 28/48 (KATO III, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.31×** | +6.9 | 3e-10 | 29/48 (AsPC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.31×** | +6.9 | 3e-10 | 34/48 (HT-29, LS 180, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.30×** | +6.8 | 4e-10 | 35/49 (KATO III, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.29×** | +6.6 | 2e-09 | 29/48 (HT-29, A-427, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.30×** | +6.6 | 2e-09 | 30/47 (Hs 766T, LoVo, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.24×** | +5.5 | 2e-06 | 30/47 (HT-29, NCI-H1573, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.25×** | +5.5 | 2e-06 | 26/47 (HT-29, NCI-H1573, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.23×** | +5.1 | 1e-05 | 26/47 (C-33 A, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.41×** | +4.4 | 4e-04 | 25/49 (C32, SW48, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | 1.18× | +4.3 | 4e-04 | 21/47 (HT-29, A-427, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.18× | +4.3 | 5e-04 | 21/47 (C-33 A, RKO, …) | all doses, stronger at high dose | low cells (technical?) |
| [[vincristine (drug)]] 0.5 µM |  | **1.23×** | +3.8 | 0.004 | 23/48 (HT-29, A-427, …) | all doses, stronger at high dose | low cells (technical?); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 10 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3657.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.766×** | -9.7 | 2e-19 | 29/49 (PANC-1, RKO, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.732×** | -7.7 | 3e-12 | 34/47 (RKO, A-172, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.762×** | -7.0 | 5e-10 | 35/48 (C32, HOP62, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.787×** | -5.9 | 4e-07 | 29/48 (SNU-423, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.855× | -5.7 | 1e-06 | 18/48 (A549, PANC-1, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.795×** | -5.7 | 1e-06 | 29/48 (NCI-H23, RKO, …) | top dose only |  |
| [[Amsacrine (drug)]] 5 µM |  | 0.859× | -5.5 | 2e-06 | 16/48 (A549, PANC-1, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.818×** | -5.0 | 4e-05 | 24/48 (LoVo, NCI-H23, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.828×** | -4.9 | 7e-05 | 26/48 (NCI-H23, HOP62, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.831×** | -4.8 | 1e-04 | 24/47 (LoVo, SW48, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.833×** | -4.7 | 1e-04 | 24/48 (NCI-H23, HT-29, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | 0.836× | -4.4 | 4e-04 | 23/47 (SW48, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.884× | -4.4 | 5e-04 | 15/49 (NCI-H23, NCI-H2347, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.848× | -4.3 | 8e-04 | 22/49 (NCI-H23, LoVo, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.841× | -4.1 | 0.001 | 23/48 (NCI-H23, LoVo, …) | all doses, flat |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | 0.852× | -3.9 | 0.003 | 19/48 (NCI-H23, AsPC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3657. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 389 | 14 (6 ⚠) | 0 | [[Vinblastine (sulfate) (drug)]] 5 µM 2.14× (z +13.0) | — |
| [[HT-29 (line)]] | alt | 466 | 11 (3 ⚠) | 1 | [[Vinblastine (sulfate) (drug)]] 5 µM 2.05× (z +14.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.628× (z -9.3) |
| [[SNU-1 (line)]] | wt | 630 | 10 (5 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.85× (z +15.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~20% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 4.50× (z +14.9) | — |
| [[A-427 (line)]] | wt | 674 | 9 (2 ⚠) | 0 | [[Vinblastine (sulfate) (drug)]] 5 µM 1.67× (z +13.0) | — |
| [[NCI-H460 (line)]] | wt | 647 | 8 (6 ⚠) | 1 | [[Digitoxin (drug)]] 0.5 µM 3.13× (z +15.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.643× (z -8.6) |
| [[AsPC-1 (line)]] | alt | 701 | 7 (6 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +18.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 2.38× (z +12.1) | [[Trametinib (drug)]] 5 µM 0.514× (z -9.1) ⚠ cell-cycle shift, explains ~16% of this change |
| [[KATO III (line)]] | alt | 346 | 7 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.45× (z +14.0) | — |
| [[NCI-H23 (line)]] | alt | 540 | 5 (4 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +16.4) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 1.87× (z +10.1) | [[Ponatinib (drug)]] 5 µM 0.505× (z -11.0) |
| [[SW480 (line)]] | alt | 356 | 7 (4 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 1.99× (z +10.9) | — |
| [[LoVo (line)]] | wt | 257 | 6 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.23× (z +11.7) | — |
| [[LS 180 (line)]] | wt | 329 | 6 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.41× (z +13.1) | — |
| [[COLO 205 (line)]] | alt | 238 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.29× (z +17.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 3.03× (z +11.7) | — |
| [[SW1417 (line)]] | alt | 399 | 5 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 1.99× (z +10.6) | — |
| [[C-33 A (line)]] | alt | 298 | 3 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 2.47× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~18% of this change · without an alert: [[Pitavastatin (Calcium) (drug)]] 0.5 µM 2.04× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.486× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 588 | 3 (1 ⚠) | 1 | [[TAK-901 (drug)]] 5 µM 8.84× (z +15.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.624× (z -9.8) |
| [[HepG2_C3A (line)]] | wt | 478 | 4 (2 ⚠) | 0 | [[Vinblastine (sulfate) (drug)]] 5 µM 1.63× (z +9.4) | — |
| [[SW48 (line)]] | wt | 294 | 4 | 0 | [[TAK-901 (drug)]] 5 µM 6.70× (z +11.0) | — |
| [[H4 (line)]] | wt | 927 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.505× (z -13.5) |
| [[HEC-1-A (line)]] | alt | 471 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.626× (z -13.1) |
| [[MIA PaCa-2 (line)]] | alt | 631 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +12.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.16× (z +9.2) | — |
| [[NCI-H2030 (line)]] | alt | 625 | 3 (2 ⚠) | 0 | [[Digitoxin (drug)]] 0.5 µM 2.06× (z +9.8) | — |
| [[PANC-1 (line)]] | alt | 800 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.496× (z -14.5) |
| [[RKO (line)]] | wt | 622 | 1 (1 ⚠) | 2 (1 ⚠) | [[Belinostat (drug)]] 5 µM 1.73× (z +9.0) ⚠ cell-cycle shift, explains ~8% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.535× (z -14.4) |
| [[A549 (line)]] | wt | 677 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.572× (z -14.4) |
| [[hTERT-HPNE (line)]] | wt | 611 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.28× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | — |
| [[Panc 03.27 (line)]] | alt | 443 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.54× (z +9.2) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 5 µM 0.488× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 492 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.526× (z -14.4) ⚠ cell-cycle shift, would explain all of this change |
| [[SK-MEL-2 (line)]] | alt | 455 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.05× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~18% of this change | — |
| [[A-172 (line)]] | wt | 784 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.596× (z -8.9) ⚠ toxic |
| [[HCT15 (line)]] | alt | 281 | 1 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 1.97× (z +8.6) | — |
| [[Hs 766T (line)]] | wt | 409 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.29× (z +11.9) ⚠ toxic | — |
| [[HS-578T (line)]] | alt | 542 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.74× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | — |
| [[J82 (line)]] | alt | 484 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.642× (z -11.3) |
| [[LOX-IMVI (line)]] | wt | 1,017 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.608× (z -11.3) |
| [[NCI-H1792 (line)]] | alt | 273 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.586× (z -10.5) |
| [[SNU-423 (line)]] | alt | 613 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.483× (z -10.1) |
| [[SW 1271 (line)]] | alt | 629 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.487× (z -9.7) |
| [[A498 (line)]] | wt | 824 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 313 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 305 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 777 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 435 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 717 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 456 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 459 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 521 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 507 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 630 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 805 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 594 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3657), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRRFIP1]] | +0.71 | +0.73 / +0.61 | both halves | 7e-06 |  |
| [[FLNB]] | +0.60 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[CORO1C]] | +0.59 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[CAST]] | +0.58 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[MAP1B]] | +0.58 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[MICAL2]] | +0.58 | +0.59 / +0.48 | both halves | 2e-05 |  |
| [[RSU1]] | +0.58 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[SH3KBP1]] | +0.58 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[TMEM41B]] | +0.57 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[UCHL3]] | +0.57 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[CAP1]] | +0.57 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[FERMT2]] | +0.57 | +0.58 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[JADE2]] | -0.57 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[HNF1A]] | -0.56 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[MACROH2A2]] | -0.54 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[COQ9]] | -0.52 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[STAP2]] | -0.51 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[IRF2]] | -0.51 | -0.49 / -0.40 | both halves | 5e-05 |  |
| [[RPRD2]] | -0.50 | -0.36 / -0.42 | both halves | 1e-04 |  |
| [[CREBBP]] | -0.50 | -0.45 / -0.34 | both halves | 1e-04 |  |
| [[SAFB]] | -0.49 | -0.30 / -0.39 | both halves | 2e-04 |  |
| [[C5orf15]] | -0.49 | -0.38 / -0.37 | both halves | 9e-05 |  |
| [[PPP4R3A]] | -0.48 | -0.35 / -0.44 | both halves | 1e-04 |  |
| [[FBXW4]] | -0.48 | -0.39 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STAP2]] | B | STAP2 activity lowers RTN4's level | lines that do not express STAP2 (12) vs lines expressing it (38) | 1.27× higher at baseline in the lines without STAP2 | 0.069 | ⚠ within organs, on part of the lines; also absent: GALM, BDH1, ENSG00000263325; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 136]] — heme metabolism; 35 genes; every member is in the + arm (projection on the module's main direction 0.655). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.32; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (15.3, 5.1); signed map (-5.5, 44.4). **Vector** length 143, 55.1% of its response variance represented; |z| ≥ 3 in 1,948 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +11.7 | +7.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +9.5 | +6.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +7.7 | +9.6 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +7.5 | +6.9 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +7.3 | +1.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | +6.6 | +5.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.4 | +7.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.3 | +7.3 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -7.7 | -1.7 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -7.0 | -3.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -6.2 | -7.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -5.3 | -7.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | -5.2 | +6.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.6 | -0.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.8 | -1.0 |
|  | [[Amsacrine (drug)]] 5 µM |  | -3.7 | -5.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.5 | -4.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.0 | -4.3 |

## What is on record

|  |  |
|---|---|
| Name | reticulon 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p16.1 — chr2:54,972,187-55,112,621 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NSP-CL, KIAA0886, NOGO, ASY, NOGOA, NOGOB, NOGOC |
| Gene groups (HGNC) | Reticulons |
| Reactome | 4 pathways, smallest: Axonal growth inhibition (RHOA activation); p75NTR regulates axonogenesis; p75 NTR receptor-mediated signalling |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NQC3](https://www.uniprot.org/uniprotkb/Q9NQC3) (Reticulon-4):

> Required to induce the formation and stabilization of endoplasmic reticulum (ER) tubules. They regulate membrane morphogenesis in the ER by promoting tubular ER production. They influence nuclear envelope expansion, nuclear pore complex formation and proper localization of inner nuclear membrane proteins. However each isoform have specific functions mainly depending on their tissue expression specificities (Probable).; [Isoform A]: Developmental neurite growth regulatory factor with a role as a …

**Summary**, from NCBI Gene [57142](https://www.ncbi.nlm.nih.gov/gene/57142):

> This gene belongs to the family of reticulon encoding genes. Reticulons are associated with the endoplasmic reticulum, and are involved in neuroendocrine secretion or in membrane trafficking in neuroendocrine cells. The product of this gene is a potent neurite outgrowth inhibitor which may also help block the regeneration of the central nervous system in higher vertebrates. Alternatively spliced transcript variants derived both from differential splicing and differential promoter usage and …

**Accessions** — [HGNC:14085](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14085) · Entrez [57142](https://www.ncbi.nlm.nih.gov/gene/57142) · UniProt [Q9NQC3](https://www.uniprot.org/uniprotkb/Q9NQC3) · Ensembl [ENSG00000115310](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115310)

## Data

Gene col 3657: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3657); `tables/drug_effects.parquet` (77 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3657, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3657]; `tensor/DDL_lfc|DDL_z.npy` [3657]; `embed/gene_vectors.npy` [3657]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3657 or target_col == 3657). Every well: [[RTN4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RTN4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
