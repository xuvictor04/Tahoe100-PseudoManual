---
symbol: "ARIH1"
type: "gene"
col: 9267
ensembl_id: "ENSG00000166233"
name: "ariadne RBR E3 ubiquitin protein ligase 1"
location: "15q24.1"
module: 93
arm: "+"
pooled_cpm: 436.33
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 9
n_dd_up_clean: 11
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/093"]
generated_by: "tahoemap"
---

# ARIH1

*ariadne RBR E3 ubiquitin protein ligase 1* — 15q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.85× (z +16.3, q 0e+00, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.425× (z -15.4, q 0e+00, down in 43 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 0.734× (z -5.5, q 5e-06, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZSWIM6]] (+0.64, fdr 7e-06), [[FAM222A]] (+0.60, fdr 1e-05), [[USP15]] (+0.60, fdr 1e-05); moves opposite to [[RFT1]] (-0.58, fdr 2e-05), [[WASH8P]] (-0.57, fdr 1e-05, ⚠ WASH8P in the vector space only through flagged drug-doses), [[TMEM209]] (-0.57, fdr 3e-05), [[TOP3B]] (-0.56, fdr 1e-05).
> It is in [[Module 093]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MYO1E]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 4 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9267.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.85×** | +16.3 | 0e+00 | 42/48 (HEC-1-A, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.24×** | +14.2 | 3e-43 | 47/48 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **3.03×** | +10.3 | 8e-23 | 48/49 (SNU-1, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.63×** | +9.1 | 2e-17 | 42/48 (NCI-H460, SW480, …) | two highest doses | cell-cycle shift (explains ~10% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.62×** | +9.0 | 3e-17 | 47/48 (SW48, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.55×** | +8.2 | 2e-14 | 38/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.56×** | +7.9 | 3e-13 | 38/48 (NCI-H460, AsPC-1, …) | two highest doses | cell-cycle shift (explains ~16% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.52×** | +7.6 | 3e-12 | 36/48 (AsPC-1, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~14% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.50×** | +7.2 | 4e-11 | 42/48 (SW480, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.34×** | +5.5 | 2e-06 | 37/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.33×** | +5.0 | 3e-05 | 36/48 (SW480, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **1.29×** | +4.8 | 9e-05 | 32/48 (SW480, SK-MEL-2, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~19% of this change | **1.30×** | +4.7 | 1e-04 | 29/47 (NCI-H460, LoVo, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.21×** | +3.3 | 0.034 | 23/48 (SNU-1, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | 1.19× | +3.1 | 0.063 | 23/50 (RKO, SW48, …) | top dose only |  |
| [[Rucaparib (phosphate) (drug)]] 5 µM |  | 1.19× | +3.1 | 0.078 | 16/49 (NCI-H2347, RPMI-7951, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9267.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.425×** | -15.4 | 0e+00 | 43/44 (Panc 03.27, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.479×** | -13.8 | 1e-40 | 49/49 (NCI-H2347, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.618×** | -8.3 | 2e-14 | 38/45 (SW1417, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.704×** | -6.6 | 7e-09 | 41/48 (SW1417, Panc 03.27, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.734×** | -5.5 | 5e-06 | 41/48 (SNU-423, CFPAC-1, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.781×** | -4.6 | 4e-04 | 38/48 (SNU-423, PANC-1, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 0.861× | -4.0 | 0.006 | 19/48 (AsPC-1, SNU-423, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.867× | -3.8 | 0.010 | 13/48 (SW 900, AN3 CA, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.879× | -3.4 | 0.037 | 3/48 (CFPAC-1, LoVo, …) | top dose only |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.697×** | -3.4 | 0.043 | 31/49 (NCI-H2347, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **0.830×** | -3.3 | 0.050 | 26/48 (SNU-423, LoVo, …) | all doses, flat |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.785×** | -3.2 | 0.055 | 29/47 (HCT15, SNU-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9267. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 463 | 11 (4 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.34× (z +22.1) | [[Dinaciclib (drug)]] 5 µM 0.370× (z -12.1) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 381 | 10 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +15.3) | [[Dinaciclib (drug)]] 5 µM 0.489× (z -12.4) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 381 | 7 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.25× (z +15.5) | [[Dinaciclib (drug)]] 5 µM 0.401× (z -12.4) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 329 | 8 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +15.1) | [[Dinaciclib (drug)]] 5 µM 0.460× (z -10.8) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 503 | 6 (1 ⚠) | 4 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.78× (z +16.2) | [[Dinaciclib (drug)]] 0.05 µM 0.395× (z -14.4) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 434 | 7 (2 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.91× (z +18.9) | [[Dinaciclib (drug)]] 5 µM 0.504× (z -9.7) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 408 | 7 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +14.2) | [[Dinaciclib (drug)]] 5 µM 0.184× (z -20.7) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 418 | 8 (3 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.30× (z +15.6) | [[Dinaciclib (drug)]] 0.5 µM 0.472× (z -8.5) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 355 | 6 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.76× (z +14.9) | [[Dinaciclib (drug)]] 5 µM 0.547× (z -9.0) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 646 | 6 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.82× (z +15.0) | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.571× (z -8.7) ⚠ cell-cycle shift, explains ~13% of this change |
| [[LoVo (line)]] | wt | 803 | 5 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.86× (z +14.8) | [[Dinaciclib (drug)]] 5 µM 0.229× (z -21.1) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 421 | 5 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.87× (z +15.5) | [[Dinaciclib (drug)]] 0.5 µM 0.362× (z -12.4) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 319 | 6 (4 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.31× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.413× (z -12.0) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 412 | 3 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +14.4) | [[Dinaciclib (drug)]] 5 µM 0.166× (z -26.2) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 416 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +12.9) | — |
| [[A-427 (line)]] | wt | 267 | 3 | 2 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 3.63× (z +9.1) | [[Dinaciclib (drug)]] 0.5 µM 0.529× (z -9.0) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 669 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.70× (z +10.3) | [[Dinaciclib (drug)]] 5 µM 0.244× (z -18.8) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 484 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +15.8) | [[Dinaciclib (drug)]] 0.5 µM 0.349× (z -16.8) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 368 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +13.8) | [[Dinaciclib (drug)]] 0.5 µM 0.418× (z -11.0) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 494 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +14.3) | [[Dinaciclib (drug)]] 5 µM 0.390× (z -12.8) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 289 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +12.0) | [[Dinaciclib (drug)]] 5 µM 0.411× (z -12.4) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 330 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +14.4) | — |
| [[NCI-H2347 (line)]] | alt | 434 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.74× (z +12.4) | [[Dinaciclib (drug)]] 0.5 µM 0.329× (z -17.5) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 323 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +13.8) | [[Dinaciclib (drug)]] 5 µM 0.450× (z -10.9) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 403 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +16.8) | [[Dinaciclib (drug)]] 0.5 µM 0.379× (z -9.5) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 451 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +16.4) | — |
| [[HEC-1-A (line)]] | alt | 351 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +18.0) | — |
| [[NCI-H2030 (line)]] | alt | 767 | 1 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.22× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.381× (z -10.9) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 485 | 1 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.46× (z +9.9) | [[Dinaciclib (drug)]] 0.5 µM 0.399× (z -10.8) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 438 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +14.5) | [[Dinaciclib (drug)]] 0.5 µM 0.379× (z -12.2) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 432 | 2 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.83× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.411× (z -9.7) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 436 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +10.0) | [[Dinaciclib (drug)]] 5 µM 0.315× (z -12.2) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 736 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +12.1) | [[Dinaciclib (drug)]] 0.5 µM 0.454× (z -8.5) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 558 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.52× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.438× (z -9.3) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 313 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.26× (z +11.2) | [[Dinaciclib (drug)]] 0.5 µM 0.489× (z -10.5) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 323 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.370× (z -15.0) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 294 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.431× (z -12.0) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 540 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.306× (z -12.6) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 456 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.23× (z +9.4) | [[Dinaciclib (drug)]] 0.5 µM 0.489× (z -9.0) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 286 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.34× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.422× (z -10.2) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 416 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +11.6) | [[Dinaciclib (drug)]] 0.5 µM 0.478× (z -9.6) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 553 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.356× (z -10.3) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 440 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.267× (z -16.1) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 406 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.241× (z -17.1) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 268 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.61× (z +8.5) | — |
| [[SW 1271 (line)]] | alt | 549 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.54× (z +9.1) | — |
| [[NCI-H2122 (line)]] | alt | 601 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 484 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 325 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 376 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9267), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZSWIM6]] | +0.64 | +0.63 / +0.59 | both halves | 7e-06 | STRING 401 |
| [[FAM222A]] | +0.60 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[USP15]] | +0.60 | +0.65 / +0.50 | both halves | 1e-05 |  |
| [[CRY1]] | +0.60 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[FBXO11]] | +0.60 | +0.57 / +0.55 | both halves | 1e-05 | STRING 402 |
| [[FOSB]] | +0.59 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[TLE4]] | +0.58 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[STX5]] | +0.58 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[COQ10B]] | +0.58 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[WDR47]] | +0.57 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[FAM53C]] | +0.56 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[MYO1E]] | +0.56 | +0.51 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RFT1]] | -0.58 | -0.47 / -0.58 | both halves | 2e-05 |  |
| [[WASH8P]] ⚠ | -0.57 | -0.49 / -0.50 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[TMEM209]] | -0.57 | -0.60 / -0.45 | both halves | 3e-05 |  |
| [[TOP3B]] | -0.56 | -0.52 / -0.61 | both halves | 1e-05 |  |
| [[WASH9P]] | -0.56 | -0.38 / -0.54 | both halves | 6e-05 |  |
| [[MTHFSD]] | -0.55 | -0.58 / -0.45 | both halves | 3e-05 |  |
| [[RNF25]] | -0.54 | -0.49 / -0.57 | both halves | 1e-05 | same gene group |
| [[UMPS]] | -0.53 | -0.60 / -0.45 | both halves | 3e-05 |  |
| [[NAXD]] | -0.53 | -0.27 / -0.53 | both halves | 3e-04 |  |
| [[SCO1]] | -0.53 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[ZNF507]] | -0.52 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[TRMT61B]] | -0.52 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[ZNF225]] | -0.52 | -0.50 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MYO1E]] | B | MYO1E activity raises ARIH1's level | lines that do not express MYO1E (5) vs lines expressing it (45) | 1.27× lower at baseline in the lines without MYO1E | 0.089 | ⚠ within organs, on part of the lines; also absent: FLNB, SMOX, TRIM38; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 093]] — TNF-alpha signaling via NF-kB; 49 genes; every member is in the + arm (projection on the module's main direction 0.650). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-22.3, -6.3); signed map (4.1, 18.6). **Vector** length 108, 48.1% of its response variance represented; |z| ≥ 3 in 1,277 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +3.4 | +7.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +3.2 | +0.1 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | +3.1 | +0.9 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +3.1 | +1.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | +2.9 | +4.8 |
|  | [[Arbutin (drug)]] 5 µM |  | +2.8 | +0.1 |
|  | [[Cyclosporin A (drug)]] 0.05 µM |  | +2.8 | +1.5 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -8.0 | +1.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.0 | -2.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | -6.0 | -5.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.6 | -2.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -4.4 | +3.3 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -4.2 | -3.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -4.0 | -4.0 |

## What is on record

|  |  |
|---|---|
| Name | ariadne RBR E3 ubiquitin protein ligase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q24.1 — chr15:72,474,330-72,602,987 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HARI, HHARI, UBCH7BP, ARI |
| Gene groups (HGNC) | Ring finger proteins; RBR E3 ubiquitin ligases |
| Reactome | 9 pathways, smallest: Modulation of host responses by IFN-stimulated genes; PKR-mediated signaling; ISG15 antiviral mechanism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y4X5](https://www.uniprot.org/uniprotkb/Q9Y4X5) (E3 ubiquitin-protein ligase ARIH1):

> E3 ubiquitin-protein ligase, which catalyzes ubiquitination of target proteins together with ubiquitin-conjugating enzyme E2 UBE2L3. Acts as an atypical E3 ubiquitin-protein ligase by working together with cullin-RING ubiquitin ligase (CRL) complexes and initiating ubiquitination of CRL substrates: associates with CRL complexes and specifically mediates addition of the first ubiquitin on CRLs targets. The initial ubiquitin is then elongated by CDC34/UBE2R1 and UBE2R2. E3 ubiquitin-protein …

**Summary**, from NCBI Gene [25820](https://www.ncbi.nlm.nih.gov/gene/25820):

> Enables enzyme binding activity; ubiquitin-protein transferase activity; and zinc ion binding activity. Involved in protein ubiquitination. Located in several cellular components, including Lewy body; cullin-RING ubiquitin ligase complex; and nuclear body. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:689](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:689) · Entrez [25820](https://www.ncbi.nlm.nih.gov/gene/25820) · UniProt [Q9Y4X5](https://www.uniprot.org/uniprotkb/Q9Y4X5) · Ensembl [ENSG00000166233](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166233)

## Data

Gene col 9267: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9267); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9267, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9267]; `tensor/DDL_lfc|DDL_z.npy` [9267]; `embed/gene_vectors.npy` [9267]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9267 or target_col == 9267). Every well: [[ARIH1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARIH1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
