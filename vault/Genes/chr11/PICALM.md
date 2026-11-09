---
symbol: "PICALM"
type: "gene"
col: 1065
ensembl_id: "ENSG00000073921"
name: "phosphatidylinositol binding clathrin assembly protein"
location: "11q14.2"
module: 64
arm: "-"
pooled_cpm: 390.38
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 12
n_dd_up_clean: 10
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/064"]
generated_by: "tahoemap"
---

# PICALM

*phosphatidylinositol binding clathrin assembly protein* — 11q14.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.86× (z +10.4, q 1e-22, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.570× (z -13.3, q 9e-38, down in 45 of 49 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LIMA1]] (+0.61, fdr 3e-04), [[TSC22D2]] (+0.60, fdr 9e-06), [[WWC2]] (+0.59, fdr 1e-05); moves opposite to [[AKAP8]] (-0.63, fdr 4e-05), [[RCC1L]] (-0.58, fdr 3e-05), [[PSMB5]] (-0.57, fdr 2e-05).
> It sits in the **-** arm of [[Module 064]] (proteasome).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1065.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.86×** | +10.4 | 1e-22 | 47/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.51×** | +9.8 | 4e-20 | 34/48 (A498, PANC-1, …) | top dose only | cell-cycle shift (explains ~5% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.65×** | +8.1 | 1e-13 | 35/48 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.62×** | +8.0 | 1e-13 | 46/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.55×** | +7.3 | 3e-11 | 45/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.50×** | +6.8 | 1e-09 | 43/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.04×** | +6.3 | 3e-08 | 45/49 (PANC-1, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.22×** | +4.8 | 1e-04 | 30/48 (A-172, SNU-1, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.64×** | +4.3 | 1e-03 | 37/48 (SW480, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.19× | +4.2 | 0.001 | 22/49 (NCI-H1573, COLO 205, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.26×** | +3.8 | 0.006 | 33/48 (NCI-H1573, SNU-1, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.21×** | +3.1 | 0.080 | 25/49 (NCI-H460, A-172, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.20×** | +3.1 | 0.080 | 24/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Irinotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.20×** | +3.1 | 0.083 | 22/48 (A-427, SNU-423, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 10 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1065.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.570×** | -13.3 | 9e-38 | 45/49 (A549, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.550×** | -10.0 | 3e-21 | 43/49 (SNU-1, SW 1271, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.580×** | -8.8 | 3e-16 | 35/44 (KATO III, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.598×** | -8.3 | 2e-14 | 46/47 (SW1417, KATO III, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.610×** | -7.7 | 2e-12 | 36/45 (NCI-H23, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.731×** | -5.1 | 4e-05 | 33/48 (hTERT-HPNE, HOP62, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.740×** | -5.1 | 4e-05 | 37/48 (CFPAC-1, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.743×** | -4.8 | 1e-04 | 34/50 (LOX-IMVI, hTERT-HPNE, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.780×** | -4.2 | 0.002 | 31/48 (CFPAC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.784×** | -4.1 | 0.002 | 29/48 (HS-578T, H4, …) | rises with dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~8% of this change | 0.849× | -3.9 | 0.005 | 18/48 (RPMI-7951, SW480, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.817×** | -3.4 | 0.033 | 28/48 (HOP62, AsPC-1, …) | two highest doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.822×** | -3.3 | 0.044 | 27/48 (HEC-1-A, SK-MEL-2, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.834× | -3.0 | 0.094 | 24/48 (NCI-H1573, KATO III, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1065. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 451 | 3 | 5 (4 ⚠) | [[Digitoxin (drug)]] 0.5 µM 1.96× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.325× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.595× (z -10.2) |
| [[NCI-H23 (line)]] | alt | 197 | 6 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +13.0) | [[Dinaciclib (drug)]] 0.05 µM 0.291× (z -16.7) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 402 | 7 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.89× (z +19.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.548× (z -12.4) |
| [[LOX-IMVI (line)]] | wt | 620 | 0 | 7 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.416× (z -15.0) |
| [[SW480 (line)]] | alt | 320 | 6 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.55× (z +14.4) | [[Dinaciclib (drug)]] 0.05 µM 0.532× (z -9.0) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 435 | 1 | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +12.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.365× (z -20.4) |
| [[SW1417 (line)]] | alt | 564 | 2 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +12.7) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.385× (z -12.9) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.568× (z -11.3) |
| [[AsPC-1 (line)]] | alt | 643 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.310× (z -14.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.615× (z -8.7) |
| [[HOP62 (line)]] | alt | 346 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.429× (z -15.8) |
| [[Hs 766T (line)]] | wt | 534 | 1 | 4 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.28× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.402× (z -9.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.541× (z -9.2) |
| [[J82 (line)]] | alt | 696 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.399× (z -18.4) |
| [[NCI-H460 (line)]] | wt | 266 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +12.7) | [[Dinaciclib (drug)]] 5 µM 0.413× (z -9.6) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 420 | 4 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.33× (z +11.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.496× (z -13.2) |
| [[SW 900 (line)]] | alt | 331 | 3 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.63× (z +11.3) | [[Dinaciclib (drug)]] 0.05 µM 0.443× (z -8.8) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 189 | 3 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +22.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.591× (z -10.4) |
| [[CFPAC-1 (line)]] | alt | 660 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.382× (z -16.0) |
| [[COLO 205 (line)]] | alt | 259 | 4 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.96× (z +14.0) | — |
| [[HT-29 (line)]] | alt | 653 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.408× (z -13.1) |
| [[hTERT-HPNE (line)]] | wt | 523 | 2 | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.39× (z +10.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.393× (z -15.6) |
| [[NCI-H1573 (line)]] | alt | 222 | 1 | 3 (3 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 1.75× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.360× (z -11.6) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 660 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.440× (z -14.2) |
| [[SNU-1 (line)]] | wt | 557 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.364× (z -15.3) |
| [[A-172 (line)]] | wt | 469 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +10.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.425× (z -16.2) |
| [[A-427 (line)]] | wt | 334 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +14.7) | — |
| [[A549 (line)]] | wt | 398 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.72× (z +10.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.316× (z -22.1) |
| [[C32 (line)]] | wt | 308 | 1 | 2 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 2.42× (z +11.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.578× (z -10.1) |
| [[H4 (line)]] | wt | 322 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +9.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.489× (z -11.9) |
| [[HepG2_C3A (line)]] | wt | 397 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.554× (z -9.4) |
| [[HS-578T (line)]] | alt | 524 | 1 | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.89× (z +8.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.396× (z -17.9) |
| [[LoVo (line)]] | wt | 390 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.457× (z -14.0) |
| [[MIA PaCa-2 (line)]] | alt | 267 | 3 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 2.77× (z +11.6) | — |
| [[SW 1271 (line)]] | alt | 509 | 1 | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.93× (z +8.8) | [[Dinaciclib (drug)]] 0.5 µM 0.188× (z -13.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.424× (z -9.9) |
| [[BT-474 (line)]] | alt | 188 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +11.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.599× (z -9.3) |
| [[C-33 A (line)]] | alt | 194 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +10.1) | — |
| [[NCI-H1792 (line)]] | alt | 354 | 1 | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.34× (z +11.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.390× (z -17.2) |
| [[NCI-H2030 (line)]] | alt | 280 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.08× (z +9.2) | — |
| [[NCI-H2347 (line)]] | alt | 365 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.62× (z +8.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.611× (z -8.9) |
| [[RKO (line)]] | wt | 365 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +13.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.594× (z -8.8) |
| [[RPMI-7951 (line)]] | alt | 384 | 1 | 1 | [[Harringtonine (drug)]] 5 µM 2.12× (z +9.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.573× (z -10.2) |
| [[SW48 (line)]] | wt | 211 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +13.4) | — |
| [[AN3 CA (line)]] | alt | 362 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.455× (z -9.4) |
| [[CHP-212 (line)]] | wt | 361 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.92× (z +8.9) | — |
| [[HCT15 (line)]] | alt | 340 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.571× (z -9.7) |
| [[LS 180 (line)]] | wt | 378 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.42× (z +9.2) | — |
| [[NCI-H661 (line)]] | alt | 409 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.250× (z -8.7) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 190 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.539× (z -11.1) |
| [[NCI-H2122 (line)]] | alt | 470 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 395 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 230 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 310 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1065), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*58 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LIMA1]] | +0.61 | +0.27 / +0.65 | both halves | 3e-04 |  |
| [[TSC22D2]] | +0.60 | +0.57 / +0.58 | both halves | 9e-06 |  |
| [[WWC2]] | +0.59 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[CAVIN1]] | +0.59 | +0.44 / +0.53 | both halves | 3e-05 |  |
| [[AFDN]] | +0.59 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[SEMA3C]] | +0.55 | +0.29 / +0.63 | both halves | 2e-04 |  |
| [[PTBP3]] | +0.54 | +0.61 / +0.48 | both halves | 2e-05 |  |
| [[CD151]] | +0.54 | +0.41 / +0.48 | both halves | 4e-05 |  |
| [[ZMIZ2]] | +0.53 | +0.42 / +0.51 | both halves | 4e-05 |  |
| [[TMEM14C]] | +0.53 | +0.25 / +0.45 | both halves | 4e-04 |  |
| [[EFHD2]] | +0.53 | +0.47 / +0.44 | both halves | 3e-05 |  |
| [[CORO1C]] | +0.53 | +0.49 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*42 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AKAP8]] | -0.63 | -0.41 / -0.60 | both halves | 4e-05 |  |
| [[RCC1L]] | -0.58 | -0.64 / -0.43 | both halves | 3e-05 |  |
| [[PSMB5]] | -0.57 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[TIRAP]] | -0.55 | -0.46 / -0.56 | both halves | 2e-05 |  |
| [[SUPV3L1]] | -0.55 | -0.30 / -0.53 | both halves | 2e-04 |  |
| [[SLC25A38]] | -0.54 | -0.40 / -0.55 | both halves | 4e-05 | pathway: HALLMARK_HEME_METABOLISM |
| [[KANSL2]] | -0.53 | -0.39 / -0.58 | both halves | 6e-05 |  |
| [[SLC30A6]] | -0.53 | -0.38 / -0.57 | both halves | 6e-05 |  |
| [[VPS51]] | -0.52 | -0.21 / -0.48 | both halves | 7e-04 |  |
| [[TMEM11-DT]] | -0.52 | -0.30 / -0.50 | both halves | 2e-04 |  |
| [[SMO]] | -0.51 | -0.37 / -0.51 | both halves | 8e-05 |  |
| [[NGDN]] | -0.51 | -0.49 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises PICALM's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[C12orf75]] | B | C12orf75 activity raises PICALM's level | lines that do not express C12orf75 (5) vs lines expressing it (45) | 1.38× lower at baseline in the lines without C12orf75 | 0.099 | ⚠ within organs, on part of the lines; also absent: FKBP7, VAT1, KCNC4 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 064]] — proteasome; 77 genes; this gene is in the **-** arm (projection on the module's main direction -0.366). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-16.8, 29.6); signed map (-13.9, 31.0). **Vector** length 94.1, 37.2% of its response variance represented; |z| ≥ 3 in 1,375 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +10.0 | +4.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | +7.4 | +3.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.4 | -10.0 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +5.2 | +0.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.9 | -8.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.3 | +4.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.9 | +2.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.8 | +1.8 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.2 | +2.9 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -7.1 | -2.4 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -6.9 | -1.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.7 | -13.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.7 | -1.5 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.7 | -3.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -3.1 | -0.4 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.3 | +0.5 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.8 | -1.5 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -1.7 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | phosphatidylinositol binding clathrin assembly protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q14.2 — chr11:85,957,175-86,069,882 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CALM, CLTH |
| Hallmark sets | HEME_METABOLISM |
| Reactome | 10 pathways, smallest: RND3 GTPase cycle; Golgi Associated Vesicle Biogenesis; trans-Golgi Network Vesicle Budding |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13492](https://www.uniprot.org/uniprotkb/Q13492) (Phosphatidylinositol-binding clathrin assembly protein):

> Cytoplasmic adapter protein that plays a critical role in clathrin-mediated endocytosis which is important in processes such as internalization of cell receptors, synaptic transmission or removal of apoptotic cells. Recruits AP-2 and attaches clathrin triskelions to the cytoplasmic side of plasma membrane leading to clathrin-coated vesicles (CCVs) assembly. Furthermore, regulates clathrin-coated vesicle size and maturation by directly sensing and driving membrane curvature. In addition to …

**Summary**, from NCBI Gene [8301](https://www.ncbi.nlm.nih.gov/gene/8301):

> This gene encodes a clathrin assembly protein, which recruits clathrin and adaptor protein complex 2 (AP2) to cell membranes at sites of coated-pit formation and clathrin-vesicle assembly. The protein may be required to determine the amount of membrane to be recycled, possibly by regulating the size of the clathrin cage. The protein is involved in AP2-dependent clathrin-mediated endocytosis at the neuromuscular junction. A chromosomal translocation t(10;11)(p13;q14) leading to the fusion of …

**Accessions** — [HGNC:15514](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15514) · Entrez [8301](https://www.ncbi.nlm.nih.gov/gene/8301) · UniProt [Q13492](https://www.uniprot.org/uniprotkb/Q13492) · Ensembl [ENSG00000073921](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000073921)

## Data

Gene col 1065: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1065); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1065, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1065]; `tensor/DDL_lfc|DDL_z.npy` [1065]; `embed/gene_vectors.npy` [1065]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1065 or target_col == 1065). Every well: [[PICALM — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PICALM.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
