---
symbol: "GNAS"
type: "gene"
col: 1505
ensembl_id: "ENSG00000087460"
name: "GNAS complex locus"
location: "20q13.32"
module: 1
arm: "-"
pooled_cpm: 410.1
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 9
n_dd_up_clean: 4
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# GNAS

*GNAS complex locus* — 20q13.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.37× (z +13.0, q 6e-36, up in 44 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.60× (z +10.5, q 2e-23, up in 44 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.506× (z -10.6, q 1e-23, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF451-AS1]] (+0.67, fdr 1e-04), [[EPHX1]] (+0.64, fdr 6e-05), [[CDK2AP1]] (+0.64, fdr 1e-05); moves opposite to [[CIAO1]] (-0.74, fdr 7e-06), [[IFRD2]] (-0.69, fdr 7e-06), [[DDX10]] (-0.68, fdr 7e-06).
> It sits in the **-** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 8 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1505.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.37×** | +13.0 | 6e-36 | 44/44 (A549, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.70×** | +12.0 | 6e-31 | 49/49 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.60×** | +10.5 | 2e-23 | 44/49 (SW48, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.98×** | +9.9 | 5e-21 | 45/45 (HEC-1-A, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.41×** | +5.4 | 9e-06 | 36/48 (SW1417, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~46% of this change | **1.40×** | +5.3 | 1e-05 | 38/48 (SW 900, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **1.40×** | +5.2 | 1e-05 | 33/48 (SW480, KATO III, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **1.35×** | +4.5 | 4e-04 | 37/47 (LoVo, COLO 205, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +4.4 | 8e-04 | 35/50 (SW48, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.27×** | +3.8 | 0.008 | 30/48 (SW48, C32, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.25×** | +3.4 | 0.037 | 30/48 (SNU-423, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.23×** | +3.2 | 0.058 | 25/48 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1505.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.506×** | -10.6 | 1e-23 | 48/48 (AsPC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.564×** | -9.0 | 9e-17 | 47/48 (AsPC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.579×** | -8.5 | 2e-15 | 48/48 (LoVo, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.659×** | -6.5 | 1e-08 | 44/48 (SW 900, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.665×** | -6.4 | 2e-08 | 39/48 (NCI-H2347, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.933× | -3.8 | 0.013 | 0/50 | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **0.649×** | -3.5 | 0.033 | 43/49 (AsPC-1, BT-474, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.809×** | -3.3 | 0.066 | 27/48 (LOX-IMVI, NCI-H2347, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.810×** | -3.3 | 0.067 | 28/48 (HepG2/C3A, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Budesonide (drug)]] 5 µM |  | **0.814×** | -3.2 | 0.075 | 32/48 (H4, NCI-H2347, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, +0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1505. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 313 | 7 (7 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 3.23× (z +14.8) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.437× (z -10.8) |
| [[LoVo (line)]] | wt | 249 | 6 (5 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 3.05× (z +14.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.74× (z +10.3) | [[Belinostat (drug)]] 5 µM 0.287× (z -16.3) |
| [[LOX-IMVI (line)]] | wt | 419 | 3 (2 ⚠) | 5 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.85× (z +11.1) | [[Homoharringtonine (drug)]] 5 µM 0.434× (z -15.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.436× (z -10.6) |
| [[SW 900 (line)]] | alt | 482 | 4 (4 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 2.63× (z +11.6) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.466× (z -11.9) |
| [[HepG2_C3A (line)]] | wt | 506 | 3 (2 ⚠) | 4 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.00× (z +9.6) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.58× (z +9.0) | [[Belinostat (drug)]] 5 µM 0.412× (z -12.3) |
| [[KATO III (line)]] | alt | 422 | 6 (5 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.60× (z +12.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.74× (z +10.9) | [[Belinostat (drug)]] 5 µM 0.527× (z -8.8) |
| [[AsPC-1 (line)]] | alt | 419 | 2 (1 ⚠) | 4 | [[Dinaciclib (drug)]] 5 µM 1.92× (z +9.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.53× (z +8.7) | [[Panobinostat (drug)]] 5 µM 0.311× (z -17.1) |
| [[HOP62 (line)]] | alt | 496 | 4 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.81× (z +12.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.75× (z +10.0) | [[Panobinostat (drug)]] 5 µM 0.486× (z -9.1) |
| [[LS 180 (line)]] | wt | 329 | 5 (4 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.12× (z +9.6) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.67× (z +9.4) | [[Panobinostat (drug)]] 5 µM 0.452× (z -10.1) |
| [[NCI-H460 (line)]] | wt | 528 | 6 (6 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.47× (z +10.7) ⚠ cell-cycle shift, explains ~43% of this change | — |
| [[SNU-423 (line)]] | alt | 485 | 4 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.62× (z +11.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.68× (z +9.2) | [[Panobinostat (drug)]] 5 µM 0.471× (z -9.4) |
| [[SW1417 (line)]] | alt | 667 | 6 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.44× (z +12.2) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.58× (z +8.9) | — |
| [[A-172 (line)]] | wt | 371 | 4 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.76× (z +14.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.68× (z +10.7) | [[Panobinostat (drug)]] 5 µM 0.530× (z -9.2) |
| [[A549 (line)]] | wt | 235 | 4 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.02× (z +15.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.97× (z +11.3) | [[Panobinostat (drug)]] 5 µM 0.464× (z -9.1) |
| [[CFPAC-1 (line)]] | alt | 510 | 5 (4 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 2.38× (z +10.9) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.80× (z +10.9) | — |
| [[HCT15 (line)]] | alt | 364 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 2.68× (z +12.3) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.410× (z -11.5) |
| [[HEC-1-A (line)]] | alt | 395 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.10× (z +14.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.59× (z +8.5) | — |
| [[Hs 766T (line)]] | wt | 677 | 3 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.46× (z +11.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.74× (z +10.1) | [[Panobinostat (drug)]] 5 µM 0.507× (z -8.7) |
| [[J82 (line)]] | alt | 474 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.48× (z +11.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.70× (z +10.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 391 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.52× (z +10.9) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 396 | 4 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.08× (z +13.2) | — |
| [[NCI-H2347 (line)]] | alt | 561 | 1 | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.61× (z +10.4) | [[Homoharringtonine (drug)]] 5 µM 0.513× (z -14.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.407× (z -13.8) |
| [[Panc 03.27 (line)]] | alt | 337 | 4 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.95× (z +12.7) | — |
| [[PANC-1 (line)]] | alt | 301 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.76× (z +15.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.70× (z +9.2) | — |
| [[RPMI-7951 (line)]] | alt | 529 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.449× (z -10.4) |
| [[A498 (line)]] | wt | 391 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.60× (z +12.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.77× (z +10.6) | — |
| [[C-33 A (line)]] | alt | 603 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 1.95× (z +8.6) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.513× (z -8.8) |
| [[COLO 205 (line)]] | alt | 279 | 1 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +10.0) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 5 µM 0.416× (z -9.7) |
| [[NCI-H1573 (line)]] | alt | 318 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.69× (z +14.8) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 380 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.02× (z +12.6) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.471× (z -9.0) |
| [[NCI-H23 (line)]] | alt | 444 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.05× (z +10.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.511× (z -11.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.419× (z -10.3) |
| [[SK-MEL-2 (line)]] | alt | 272 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.27× (z +11.1) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.459× (z -9.4) |
| [[SNU-1 (line)]] | wt | 401 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.302× (z -13.5) |
| [[SW48 (line)]] | wt | 273 | 2 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.67× (z +13.4) | [[Panobinostat (drug)]] 5 µM 0.399× (z -8.9) |
| [[AN3 CA (line)]] | alt | 220 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.99× (z +9.7) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 346 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.06× (z +11.7) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 376 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.40× (z +10.2) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 440 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.32× (z +10.4) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 377 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.12× (z +8.8) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.453× (z -9.8) |
| [[RKO (line)]] | wt | 382 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.67× (z +8.5) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.460× (z -8.8) |
| [[SHP-77 (line)]] | alt | 300 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.98× (z +12.2) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 402 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.80× (z +10.2) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 416 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.91× (z +13.1) | — |
| [[H4 (line)]] | wt | 528 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.439× (z -9.1) |
| [[CHP-212 (line)]] | wt | 388 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 374 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 407 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 695 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 454 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 529 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1505), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*35 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF451-AS1]] | +0.67 | +0.35 / +0.58 | both halves | 1e-04 |  |
| [[EPHX1]] | +0.64 | +0.39 / +0.42 | both halves | 6e-05 |  |
| [[CDK2AP1]] | +0.64 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[EMC1-AS1]] | +0.64 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[OXR1-AS1]] | +0.64 | +0.39 / +0.55 | both halves | 6e-05 |  |
| [[C12orf73]] | +0.63 | +0.44 / +0.63 | both halves | 3e-05 |  |
| [[SEC24B-AS1]] | +0.63 | +0.36 / +0.56 | both halves | 1e-04 |  |
| [[CD27-AS1]] | +0.63 | +0.38 / +0.53 | both halves | 7e-05 |  |
| [[EOGT-DT]] | +0.63 | +0.42 / +0.56 | both halves | 4e-05 |  |
| [[C12orf57]] | +0.62 | +0.36 / +0.63 | both halves | 9e-05 |  |
| [[TMEM59]] | +0.62 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[CTSV]] | +0.61 | +0.50 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*65 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CIAO1]] | -0.74 | -0.62 / -0.75 | both halves | 7e-06 |  |
| [[IFRD2]] | -0.69 | -0.63 / -0.72 | both halves | 7e-06 |  |
| [[DDX10]] | -0.68 | -0.64 / -0.71 | both halves | 7e-06 |  |
| [[NLE1]] | -0.68 | -0.50 / -0.66 | both halves | 1e-05 |  |
| [[MPHOSPH6]] | -0.68 | -0.57 / -0.73 | both halves | 1e-05 |  |
| [[PAK1IP1]] | -0.68 | -0.65 / -0.72 | both halves | 7e-06 |  |
| [[RRS1]] | -0.68 | -0.71 / -0.73 | both halves | 7e-06 |  |
| [[METTL2A]] | -0.67 | -0.58 / -0.66 | both halves | 7e-06 |  |
| [[EIF2B3]] | -0.67 | -0.58 / -0.66 | both halves | 8e-06 |  |
| [[TAF1B]] | -0.67 | -0.53 / -0.67 | both halves | 1e-05 |  |
| [[PRMT5]] | -0.66 | -0.60 / -0.73 | both halves | 7e-06 |  |
| [[DNAJA3]] | -0.66 | -0.64 / -0.62 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers GNAS's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[HDAC6]] | B | HDAC6 activity raises GNAS's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **-** arm (projection on the module's main direction -0.636). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-17.3, -39.2); signed map (19.9, 0.5). **Vector** length 109, 48.7% of its response variance represented; |z| ≥ 3 in 1,020 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +12.2 | +10.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +8.0 | +3.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +7.0 | +4.4 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | +3.4 | -1.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.3 | +1.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.1 | +0.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +3.1 | +0.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.0 | -1.5 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +2.8 | +0.2 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -8.3 | -1.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.3 | -2.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.9 | -6.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.7 | -3.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.7 | -2.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.1 | -0.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -4.0 | -1.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.8 | -0.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.8 | +0.3 |

## What is on record

|  |  |
|---|---|
| Name | GNAS complex locus |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.32 — chr20:58,839,718-58,911,192 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NESP55, NESP, GNASXL, GPSA, SCG6, SgVI; previously GNAS1 |
| Gene groups (HGNC) | Granins; G protein subunits alpha, group s |
| Hallmark sets | PROTEIN_SECRETION |
| Reactome | 31 pathways, smallest: PKA activation in glucagon signalling; Prostacyclin signalling through prostacyclin receptor; Glucagon-type ligand receptors |
| Matched by | ensembl_id |

UniProt [O95467](https://www.uniprot.org/uniprotkb/O95467) carries no function annotation.

**Summary**, from NCBI Gene [2778](https://www.ncbi.nlm.nih.gov/gene/2778):

> This locus has a highly complex imprinted expression pattern. It gives rise to maternally, paternally, and biallelically expressed transcripts that are derived from four alternative promoters and 5' exons. Some transcripts contain a differentially methylated region (DMR) at their 5' exons, and this DMR is commonly found in imprinted genes and correlates with transcript expression. An antisense transcript is produced from an overlapping locus on the opposite strand. One of the transcripts …

**Accessions** — [HGNC:4392](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4392) · Entrez [2778](https://www.ncbi.nlm.nih.gov/gene/2778) · UniProt [O95467](https://www.uniprot.org/uniprotkb/O95467) · Ensembl [ENSG00000087460](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000087460)

## Data

Gene col 1505: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1505); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1505, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1505]; `tensor/DDL_lfc|DDL_z.npy` [1505]; `embed/gene_vectors.npy` [1505]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1505 or target_col == 1505). Every well: [[GNAS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GNAS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
