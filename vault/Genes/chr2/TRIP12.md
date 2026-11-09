---
symbol: "TRIP12"
type: "gene"
col: 7742
ensembl_id: "ENSG00000153827"
name: "thyroid hormone receptor interactor 12"
location: "2q36.3"
module: 3
arm: "-"
pooled_cpm: 366.0
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 11
n_dd_up_clean: 7
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# TRIP12

*thyroid hormone receptor interactor 12* — 2q36.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.62× (z +16.1, q 0e+00, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.412× (z -21.0, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IL6ST]] (+0.73, fdr 7e-06), [[TUG1]] (+0.70, fdr 7e-06), [[TASOR]] (+0.68, fdr 1e-05); moves opposite to [[NBPF3]] (-0.70, fdr 9e-06), [[GTF2H2B]] (-0.69, fdr 2e-05), [[ELP2]] (-0.69, fdr 7e-06).
> It sits in the **-** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7742.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.62×** | +16.1 | 0e+00 | 42/48 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.74×** | +13.1 | 1e-36 | 46/48 (NCI-H460, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.52×** | +11.4 | 5e-28 | 46/49 (NCI-H460, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.40×** | +7.6 | 4e-12 | 33/48 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.35×** | +7.1 | 1e-10 | 31/48 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.34×** | +7.0 | 2e-10 | 36/48 (NCI-H460, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.34×** | +7.0 | 3e-10 | 39/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.72×** | +6.7 | 1e-09 | 43/48 (HEC-1-A, BT-474, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.28×** | +5.5 | 2e-06 | 23/44 (J82, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.14× | +4.5 | 4e-04 | 14/48 (SW1417, HOP62, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.19× | +4.1 | 0.002 | 23/48 (HT-29, HEC-1-A, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +3.4 | 0.036 | 20/48 (HT-29, NCI-H2030, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +3.3 | 0.045 | 20/48 (HS-578T, NCI-H460, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.14× | +3.0 | 0.096 | 22/49 (SW48, J82, …) | rises with dose | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 2 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7742.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.412×** | -21.0 | 0e+00 | 48/48 (SW480, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.427×** | -20.1 | 0e+00 | 48/48 (HT-29, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.430×** | -20.0 | 0e+00 | 48/48 (SW480, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.608×** | -11.8 | 7e-30 | 46/48 (HT-29, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.619×** | -10.9 | 1e-25 | 45/47 (CFPAC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.688×** | -8.8 | 9e-17 | 45/48 (AsPC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.774×** | -8.6 | 9e-16 | 37/48 (HepG2/C3A, RKO, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.554×** | -7.3 | 2e-11 | 47/49 (AsPC-1, HT-29, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.764×** | -6.4 | 1e-08 | 37/49 (CFPAC-1, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Radotinib (drug)]] 5 µM |  | 0.839× | -5.9 | 2e-07 | 22/48 (NCI-H23, SK-MEL-2, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.812×** | -4.9 | 5e-05 | 27/48 (NCI-H23, NCI-H1573, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.841× | -4.1 | 0.002 | 18/49 (NCI-H2347, SNU-423, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~5% of this change | 0.846× | -3.9 | 0.003 | 20/48 (NCI-H2347, RKO, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | 0.854× | -3.7 | 0.008 | 21/48 (SW 900, SNU-423, …) | top dose only |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | 0.862× | -3.5 | 0.016 | 14/48 (SHP-77, A498, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.812×** | -3.5 | 0.016 | 34/48 (NCI-H460, CHP-212, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | 0.909× | -3.2 | 0.048 | 5/49 (COLO 205, A549, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7742. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 377 | 12 (5 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +27.2) | [[Panobinostat (drug)]] 0.5 µM 0.490× (z -14.7) |
| [[HOP62 (line)]] | alt | 296 | 8 (2 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +24.0) | [[Panobinostat (drug)]] 0.5 µM 0.420× (z -15.6) |
| [[NCI-H1573 (line)]] | alt | 554 | 7 (1 ⚠) | 5 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.35× (z +13.8) | [[Panobinostat (drug)]] 5 µM 0.338× (z -17.6) |
| [[BT-474 (line)]] | alt | 351 | 7 (1 ⚠) | 4 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.08× (z +13.2) | [[Panobinostat (drug)]] 0.5 µM 0.410× (z -13.9) |
| [[SW 900 (line)]] | alt | 307 | 6 (1 ⚠) | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +16.8) | [[Panobinostat (drug)]] 0.5 µM 0.391× (z -16.3) |
| [[SW480 (line)]] | alt | 342 | 4 (1 ⚠) | 6 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.97× (z +13.9) | [[Panobinostat (drug)]] 0.5 µM 0.369× (z -19.3) |
| [[HepG2_C3A (line)]] | wt | 460 | 3 (1 ⚠) | 6 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.15× (z +12.5) | [[Panobinostat (drug)]] 0.5 µM 0.307× (z -19.1) |
| [[HS-578T (line)]] | alt | 259 | 6 (2 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +22.7) | [[Belinostat (drug)]] 5 µM 0.477× (z -12.1) |
| [[LOX-IMVI (line)]] | wt | 506 | 4 | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +14.2) | [[Panobinostat (drug)]] 0.5 µM 0.399× (z -15.6) |
| [[PANC-1 (line)]] | alt | 441 | 5 (1 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +18.7) | [[Belinostat (drug)]] 5 µM 0.415× (z -13.8) |
| [[A498 (line)]] | wt | 333 | 4 (2 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +26.4) | [[Panobinostat (drug)]] 0.5 µM 0.440× (z -16.0) |
| [[AsPC-1 (line)]] | alt | 548 | 3 | 5 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.60× (z +15.8) | [[Belinostat (drug)]] 5 µM 0.321× (z -18.8) |
| [[CFPAC-1 (line)]] | alt | 406 | 3 | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +22.1) | [[Panobinostat (drug)]] 0.5 µM 0.396× (z -15.9) |
| [[LS 180 (line)]] | wt | 287 | 3 | 5 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.87× (z +10.8) | [[Belinostat (drug)]] 5 µM 0.396× (z -16.0) |
| [[NCI-H2030 (line)]] | alt | 385 | 4 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +20.2) | [[Panobinostat (drug)]] 0.5 µM 0.509× (z -11.5) |
| [[NCI-H2347 (line)]] | alt | 340 | 4 | 4 | [[Homoharringtonine (drug)]] 5 µM 1.77× (z +15.8) | [[Panobinostat (drug)]] 0.5 µM 0.396× (z -18.3) |
| [[RKO (line)]] | wt | 464 | 2 | 6 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.63× (z +11.0) | [[Panobinostat (drug)]] 5 µM 0.331× (z -17.6) |
| [[SW1417 (line)]] | alt | 340 | 2 | 6 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.87× (z +10.6) | [[Panobinostat (drug)]] 0.5 µM 0.399× (z -15.6) |
| [[MIA PaCa-2 (line)]] | alt | 646 | 3 | 4 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.15× (z +9.0) | [[Panobinostat (drug)]] 5 µM 0.317× (z -17.2) |
| [[NCI-H1792 (line)]] | alt | 320 | 3 | 4 | [[Harringtonine (drug)]] 5 µM 2.19× (z +12.5) | [[Panobinostat (drug)]] 5 µM 0.357× (z -17.1) |
| [[Panc 03.27 (line)]] | alt | 315 | 2 | 5 | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +13.1) | [[Belinostat (drug)]] 5 µM 0.351× (z -16.5) |
| [[RPMI-7951 (line)]] | alt | 448 | 1 | 6 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.55× (z +9.1) | [[Panobinostat (drug)]] 0.5 µM 0.411× (z -13.0) |
| [[SK-MEL-2 (line)]] | alt | 426 | 3 | 4 | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +15.0) | [[Belinostat (drug)]] 5 µM 0.528× (z -11.4) |
| [[SNU-423 (line)]] | alt | 452 | 1 | 6 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +13.2) | [[Panobinostat (drug)]] 5 µM 0.304× (z -17.7) |
| [[A549 (line)]] | wt | 456 | 1 | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +15.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.403× (z -18.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.366× (z -14.3) |
| [[HEC-1-A (line)]] | alt | 246 | 2 | 4 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.03× (z +12.0) | [[Belinostat (drug)]] 5 µM 0.529× (z -13.2) |
| [[Hs 766T (line)]] | wt | 291 | 3 | 3 | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +12.5) | [[Belinostat (drug)]] 5 µM 0.351× (z -14.7) |
| [[HT-29 (line)]] | alt | 337 | 0 | 6 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.289× (z -19.1) |
| [[J82 (line)]] | alt | 237 | 1 (1 ⚠) | 5 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 1.87× (z +9.0) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.417× (z -13.3) |
| [[A-172 (line)]] | wt | 334 | 1 | 4 | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +13.5) | [[Panobinostat (drug)]] 0.5 µM 0.417× (z -14.6) |
| [[C32 (line)]] | wt | 188 | 1 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.66× (z +10.8) | [[Panobinostat (drug)]] 5 µM 0.428× (z -12.6) |
| [[KATO III (line)]] | alt | 252 | 1 | 4 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.29× (z +13.4) | [[Belinostat (drug)]] 5 µM 0.325× (z -18.5) |
| [[COLO 205 (line)]] | alt | 359 | 1 | 3 | [[TAK-901 (drug)]] 5 µM 4.79× (z +11.8) | [[Panobinostat (drug)]] 5 µM 0.368× (z -14.4) |
| [[H4 (line)]] | wt | 386 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +13.2) | [[Panobinostat (drug)]] 0.5 µM 0.414× (z -12.2) |
| [[hTERT-HPNE (line)]] | wt | 304 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +11.2) | [[Panobinostat (drug)]] 0.5 µM 0.376× (z -13.4) |
| [[LoVo (line)]] | wt | 260 | 1 | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.78× (z +9.0) | [[Panobinostat (drug)]] 5 µM 0.433× (z -13.0) |
| [[NCI-H23 (line)]] | alt | 594 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 1.61× (z +9.8) | [[Belinostat (drug)]] 5 µM 0.389× (z -14.0) |
| [[A-427 (line)]] | wt | 271 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.497× (z -11.3) |
| [[C-33 A (line)]] | alt | 345 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.468× (z -9.9) |
| [[CHP-212 (line)]] | wt | 336 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.368× (z -10.0) |
| [[HCT15 (line)]] | alt | 371 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.462× (z -11.4) |
| [[SHP-77 (line)]] | alt | 334 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.487× (z -12.5) |
| [[SNU-1 (line)]] | wt | 327 | 3 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.35× (z +11.9) | — |
| [[SW48 (line)]] | wt | 211 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.417× (z -11.4) |
| [[AN3 CA (line)]] | alt | 372 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.441× (z -8.9) |
| [[SW 1088 (line)]] | alt | 332 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.236× (z -10.1) |
| [[SW 1271 (line)]] | alt | 440 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.368× (z -8.5) ⚠ toxic |
| [[NCI-H2122 (line)]] | alt | 362 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 350 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 292 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7742), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*38 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IL6ST]] | +0.73 | +0.63 / +0.67 | both halves | 7e-06 |  |
| [[TUG1]] | +0.70 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[TASOR]] | +0.68 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[EIF4G2]] | +0.68 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[PARVA]] | +0.67 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[HNRNPK]] | +0.67 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[ZNF655]] | +0.66 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[C1RL-AS1]] | +0.65 | +0.49 / +0.63 | both halves | 1e-05 |  |
| [[PSME3IP1]] | +0.65 | +0.37 / +0.67 | both halves | 8e-05 |  |
| [[KRT8P12]] | +0.64 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[CACNA2D1]] | +0.64 | +0.43 / +0.55 | both halves | 3e-05 |  |
| [[SUCLA2]] | +0.64 | +0.62 / +0.46 | both halves | 2e-05 |  |

## Genes that move opposite

*62 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NBPF3]] | -0.70 | -0.57 / -0.59 | both halves | 9e-06 |  |
| [[GTF2H2B]] | -0.69 | -0.47 / -0.67 | both halves | 2e-05 |  |
| [[ELP2]] | -0.69 | -0.60 / -0.60 | both halves | 7e-06 |  |
| [[SLC17A5]] | -0.68 | -0.56 / -0.60 | both halves | 1e-05 |  |
| [[SDHAP2]] | -0.68 | -0.54 / -0.56 | both halves | 1e-05 |  |
| [[MALSU1]] | -0.68 | -0.44 / -0.68 | both halves | 3e-05 |  |
| [[TMEM120B]] | -0.67 | -0.54 / -0.57 | both halves | 1e-05 |  |
| [[CAMLG]] | -0.67 | -0.48 / -0.66 | both halves | 2e-05 |  |
| [[SNAPC3]] | -0.67 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[AFMID]] | -0.67 | -0.43 / -0.67 | both halves | 3e-05 |  |
| [[MPG]] | -0.66 | -0.39 / -0.57 | both halves | 5e-05 |  |
| [[HEBP1]] | -0.66 | -0.49 / -0.63 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises TRIP12's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises TRIP12's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **-** arm (projection on the module's main direction -0.701). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (0.7, -12.8); signed map (17.9, -32.2). **Vector** length 137, 54.8% of its response variance represented; |z| ≥ 3 in 1,458 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +10.2 | +3.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +10.1 | +5.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +9.2 | +4.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +8.6 | +16.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +7.9 | -1.4 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +4.6 | +1.5 |
|  | [[Busulfan (drug)]] 0.05 µM |  | +4.2 | +2.0 |
|  | [[Palmatine (chloride) (drug)]] 0.05 µM |  | +3.6 | +0.9 |
|  | [[Berbamine (drug)]] 0.05 µM |  | +3.5 | +1.2 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -8.1 | -10.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -7.6 | -8.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -7.1 | -11.8 |
|  | [[Radotinib (drug)]] 5 µM |  | -7.1 | -5.9 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -6.3 | -8.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -5.5 | -1.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -5.2 | -7.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.5 | -4.9 |

## What is on record

|  |  |
|---|---|
| Name | thyroid hormone receptor interactor 12 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q36.3 — chr2:229,763,837-229,923,239 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0045, ULF, TRIPC |
| Gene groups (HGNC) | Armadillo like helical domain containing; HECT domain E3 ubiquitin protein ligases |
| Reactome | 3 pathways, smallest: Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation; Adaptive Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14669](https://www.uniprot.org/uniprotkb/Q14669) (E3 ubiquitin-protein ligase TRIP12):

> E3 ubiquitin-protein ligase involved in ubiquitin fusion degradation (UFD) pathway and regulation of DNA repair. Part of the ubiquitin fusion degradation (UFD) pathway, a process that mediates ubiquitination of protein at their N-terminus, regardless of the presence of lysine residues in target proteins. Acts as a key regulator of DNA damage response by acting as a suppressor of RNF168, an E3 ubiquitin-protein ligase that promotes accumulation of 'Lys-63'-linked histone H2A and H2AX at DNA …

**Summary**, from NCBI Gene [9320](https://www.ncbi.nlm.nih.gov/gene/9320):

> The protein encoded by this gene is an E3 ubiquitin-protein ligase involved in the degradation of the p19ARF/ARF isoform of CDKN2A, a tumor suppressor. The encoded protein also plays a role in the DNA damage response by regulating the stability of USP7, which regulates tumor suppressor p53. [provided by RefSeq, Jan 2017]

**Accessions** — [HGNC:12306](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12306) · Entrez [9320](https://www.ncbi.nlm.nih.gov/gene/9320) · UniProt [Q14669](https://www.uniprot.org/uniprotkb/Q14669) · Ensembl [ENSG00000153827](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000153827)

## Data

Gene col 7742: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7742); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7742, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7742]; `tensor/DDL_lfc|DDL_z.npy` [7742]; `embed/gene_vectors.npy` [7742]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7742 or target_col == 7742). Every well: [[TRIP12 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRIP12.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
