---
symbol: "FAM172A"
type: "gene"
col: 3460
ensembl_id: "ENSG00000113391"
name: "ARB2 cotranscriptional regulator A"
location: "5q15"
module: 185
arm: "+"
pooled_cpm: 294.58
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 31
n_dd_up_clean: 0
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/185"]
generated_by: "tahoemap"
---

# FAM172A

*ARB2 cotranscriptional regulator A* — 5q15

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 31 drug-doses (21 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.456× (z -24.5, q 0e+00, down in 47 of 48 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.600× (z -15.9, q 0e+00, down in 44 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[VPS13B]] (+0.60, fdr 3e-05), [[CDKAL1]] (+0.57, fdr 1e-05), [[EXOC4]] (+0.56, fdr 3e-05); moves opposite to [[ELF4]] (-0.47, fdr 4e-05), [[SIX4]] (-0.45, fdr 3e-05), [[BCAR1]] (-0.44, fdr 1e-04).
> It is in [[Module 185]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3460.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bimiralisib (drug)]] 5 µM |  | 1.36× | +3.6 | 0.19 | 30/50 (SW480, A-427, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | 1.17× | +3.3 | 0.19 | 18/48 (A498, H4, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.15× | +3.2 | 0.19 | 15/48 (A498, hTERT-HPNE, …) | all doses, flat |  |
| [[GSK1059615 (drug)]] 5 µM |  | 1.31× | +3.2 | 0.19 | 26/49 (NCI-H2030, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~70% of this change | 1.16× | +3.1 | 0.19 | 10/48 (A-427, A-172, …) | inconsistent across doses |  |
| [[Rifaximin (drug)]] 5 µM |  | 1.16× | +3.1 | 0.19 | 12/48 (RPMI-7951, C32, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 45 in all, 25 with an alert ⚠; shown: the 15 strongest and the 11 next strongest without an alert. 31 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 21 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3460.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.456×** | -24.5 | 0e+00 | 47/48 (SNU-423, HOP62, …) | rises with dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.600×** | -15.9 | 0e+00 | 44/49 (LOX-IMVI, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.522×** | -13.8 | 7e-41 | 47/48 (NCI-H1573, NCI-H460, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.541×** | -13.5 | 1e-39 | 45/48 (NCI-H460, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.538×** | -13.1 | 2e-37 | 46/47 (NCI-H1573, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.552×** | -13.1 | 4e-37 | 46/48 (NCI-H460, LS 180, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.555×** | -13.0 | 1e-36 | 43/48 (NCI-H1573, PANC-1, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **0.589×** | -11.2 | 3e-27 | 43/47 (NCI-H460, MIA PaCa-2, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.629×** | -10.2 | 1e-22 | 41/48 (SW480, SK-MEL-2, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.661×** | -9.1 | 5e-18 | 39/48 (HCT15, CFPAC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.680×** | -8.5 | 1e-15 | 39/48 (HOP62, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.688×** | -7.8 | 4e-13 | 43/48 (KATO III, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.708×** | -7.2 | 3e-11 | 33/48 (NCI-H460, NCI-H1573, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.725×** | -7.1 | 7e-11 | 34/48 (HCT15, COLO 205, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~51% of this change | **0.727×** | -7.0 | 9e-11 | 38/48 (SW 1088, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.852× | -5.0 | 2e-05 | 20/48 (HOP62, SNU-423, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.669×** | -4.6 | 9e-05 | 34/48 (NCI-H460, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[Vilanterol (drug)]] 5 µM |  | 0.884× | -3.8 | 0.003 | 8/49 (SW480, RPMI-7951, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.840× | -3.6 | 0.006 | 20/47 (NCI-H460, H4, …) | two highest doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.740×** | -3.5 | 0.010 | 29/48 (NCI-H1792, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | 0.849× | -3.3 | 0.015 | 18/47 (LoVo, C-33 A, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.755×** | -3.2 | 0.021 | 23/48 (NCI-H1792, A-427, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **0.758×** | -3.2 | 0.023 | 23/49 (CFPAC-1, NCI-H1792, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.904× | -3.1 | 0.026 | 7/49 (SHP-77, HOP62, …) | all doses, flat |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.800×** | -3.0 | 0.042 | 24/48 (RPMI-7951, HOP62, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | 0.869× | -3.0 | 0.044 | 10/48 (SW480, Panc 03.27, …) | top dose only | plate-row cell shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.28 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3460. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 391 | 0 | 15 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.392× (z -23.3) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.460× (z -19.3) |
| [[HOP62 (line)]] | alt | 276 | 0 | 14 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.250× (z -30.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.388× (z -14.6) |
| [[CFPAC-1 (line)]] | alt | 370 | 0 | 12 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -24.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.543× (z -9.1) |
| [[HCT15 (line)]] | alt | 305 | 0 | 11 (10 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.359× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.453× (z -10.5) |
| [[MIA PaCa-2 (line)]] | alt | 376 | 0 | 11 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.418× (z -18.7) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.382× (z -14.6) |
| [[A-427 (line)]] | wt | 480 | 0 | 10 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.418× (z -23.0) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.397× (z -17.2) |
| [[COLO 205 (line)]] | alt | 298 | 0 | 10 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.488× (z -13.8) ⚠ cell-cycle shift, explains ~28% of this change |
| [[SNU-423 (line)]] | alt | 286 | 0 | 10 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -30.9) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.468× (z -16.2) |
| [[KATO III (line)]] | alt | 315 | 0 | 9 (7 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.397× (z -14.6) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.611× (z -11.5) |
| [[SHP-77 (line)]] | alt | 687 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.413× (z -18.7) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.427× (z -18.0) |
| [[A-172 (line)]] | wt | 278 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.357× (z -20.3) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.437× (z -16.3) |
| [[C32 (line)]] | wt | 336 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.417× (z -20.0) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.538× (z -14.1) |
| [[H4 (line)]] | wt | 267 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.364× (z -18.7) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.339× (z -14.2) |
| [[LOX-IMVI (line)]] | wt | 357 | 0 | 8 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.409× (z -20.1) |
| [[NCI-H1792 (line)]] | alt | 257 | 0 | 8 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.403× (z -20.0) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.595× (z -11.4) |
| [[PANC-1 (line)]] | alt | 345 | 0 | 8 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -29.5) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.360× (z -17.4) |
| [[RKO (line)]] | wt | 318 | 0 | 8 (7 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.391× (z -14.3) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.553× (z -9.0) |
| [[SK-MEL-2 (line)]] | alt | 391 | 0 | 8 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.394× (z -21.5) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.414× (z -14.4) |
| [[SW480 (line)]] | alt | 182 | 0 | 8 (6 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.336× (z -17.8) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.408× (z -14.7) |
| [[C-33 A (line)]] | alt | 641 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.278× (z -17.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.479× (z -14.4) |
| [[J82 (line)]] | alt | 236 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -24.0) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.528× (z -12.9) |
| [[NCI-H1573 (line)]] | alt | 360 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -28.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.335× (z -18.5) |
| [[A498 (line)]] | wt | 191 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.353× (z -21.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.380× (z -14.2) |
| [[A549 (line)]] | wt | 267 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -26.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.404× (z -19.2) |
| [[AN3 CA (line)]] | alt | 526 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.281× (z -18.6) |
| [[hTERT-HPNE (line)]] | wt | 234 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -20.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.340× (z -13.8) |
| [[LoVo (line)]] | wt | 255 | 0 | 6 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.463× (z -19.2) ⚠ cell-cycle shift, explains ~28% of this change |
| [[Panc 03.27 (line)]] | alt | 274 | 0 | 6 (5 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.274× (z -10.4) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.532× (z -9.6) |
| [[RPMI-7951 (line)]] | alt | 231 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.336× (z -20.3) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.434× (z -11.0) |
| [[HEC-1-A (line)]] | alt | 151 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.429× (z -18.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.568× (z -12.6) |
| [[HT-29 (line)]] | alt | 187 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.482× (z -15.8) ⚠ cell-cycle shift, explains ~28% of this change |
| [[LS 180 (line)]] | wt | 341 | 0 | 5 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.349× (z -17.4) ⚠ cell-cycle shift, explains ~36% of this change |
| [[HS-578T (line)]] | alt | 258 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.387× (z -18.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.594× (z -10.3) |
| [[NCI-H23 (line)]] | alt | 424 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.478× (z -17.5) ⚠ cell-cycle shift, explains ~28% of this change |
| [[SNU-1 (line)]] | wt | 291 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.277× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.546× (z -10.4) |
| [[SW 1088 (line)]] | alt | 432 | 0 | 4 (4 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.231× (z -9.4) ⚠ transcription drop; cell-cycle shift, explains ~51% of this change |
| [[SW 900 (line)]] | alt | 191 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.517× (z -12.7) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.489× (z -9.7) |
| [[AsPC-1 (line)]] | alt | 261 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.622× (z -9.9) |
| [[NCI-H2030 (line)]] | alt | 299 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.562× (z -12.0) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.603× (z -10.5) |
| [[SW1417 (line)]] | alt | 171 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.604× (z -10.3) ⚠ cell-cycle shift, explains ~28% of this change |
| [[CHP-212 (line)]] | wt | 228 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.287× (z -10.0) ⚠ cell-cycle shift, explains ~40% of this change |
| [[Hs 766T (line)]] | wt | 222 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.436× (z -10.2) ⚠ toxic |
| [[BT-474 (line)]] | alt | 141 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.508× (z -8.8) ⚠ cell-cycle shift, explains ~59% of this change |
| [[HepG2_C3A (line)]] | wt | 164 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.413× (z -14.3) ⚠ cell-cycle shift, explains ~28% of this change |
| [[NCI-H2347 (line)]] | alt | 293 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.552× (z -12.3) |
| [[SW48 (line)]] | wt | 192 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.499× (z -10.9) |
| [[NCI-H2122 (line)]] | alt | 330 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 303 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 313 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 272 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3460), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VPS13B]] | +0.60 | +0.44 / +0.66 | both halves | 3e-05 |  |
| [[CDKAL1]] | +0.57 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[EXOC4]] | +0.56 | +0.44 / +0.61 | both halves | 3e-05 | same gene group |
| [[FTO]] | +0.56 | +0.48 / +0.62 | both halves | 2e-05 |  |
| [[RSRC1]] | +0.55 | +0.43 / +0.64 | both halves | 3e-05 |  |
| [[BLTP1]] | +0.55 | +0.45 / +0.59 | both halves | 3e-05 |  |
| [[NUBPL]] | +0.54 | +0.33 / +0.56 | both halves | 1e-04 |  |
| [[SUMF1]] | +0.54 | +0.38 / +0.55 | both halves | 7e-05 |  |
| [[DPH6]] | +0.54 | +0.39 / +0.53 | both halves | 6e-05 | same gene group |
| [[WDR70]] | +0.54 | +0.38 / +0.55 | both halves | 7e-05 |  |
| [[CCDC171]] | +0.52 | +0.41 / +0.49 | both halves | 4e-05 |  |
| [[EIF3H]] | +0.51 | +0.52 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ELF4]] | -0.47 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[SIX4]] | -0.45 | -0.52 / -0.43 | both halves | 3e-05 |  |
| [[BCAR1]] | -0.44 | -0.33 / -0.42 | both halves | 1e-04 |  |
| [[ERF]] | -0.43 | -0.49 / -0.38 | both halves | 6e-05 |  |
| [[STARD8]] | -0.42 | -0.38 / -0.44 | both halves | 6e-05 |  |
| [[CCNYL1]] | -0.42 | -0.35 / -0.49 | both halves | 1e-04 | same gene group |
| [[FGF11]] | -0.41 | -0.33 / -0.31 | both halves | 2e-04 |  |
| [[ZNF672]] | -0.41 | -0.29 / -0.40 | both halves | 3e-04 |  |
| [[CARD10]] | -0.41 | -0.42 / -0.39 | both halves | 6e-05 |  |
| [[ADGRB2]] | -0.40 | -0.45 / -0.45 | both halves | 3e-05 | same gene group |
| [[RPS6KA1]] | -0.40 | -0.31 / -0.49 | both halves | 2e-04 | same gene group |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 185]]; 20 genes; every member is in the + arm (projection on the module's main direction 0.654). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-16.0, -13.5); signed map (-15.0, -48.8). **Vector** length 87.7, 30.7% of its response variance represented; |z| ≥ 3 in 1,546 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belumosudil (drug)]] 5 µM |  | +4.2 | +3.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | +3.3 | -6.8 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | +3.0 | -3.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +2.8 | -5.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.5 | -1.5 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +2.3 | -0.6 |
|  | [[Medroxyprogesterone acetate (drug)]] 5 µM |  | +2.3 | +1.9 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.3 | +3.2 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -5.8 | -7.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -5.5 | -13.1 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | -4.6 | -6.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.8 | -10.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.6 | -2.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | -2.7 | -3.3 |
|  | [[Vortioxetine (drug)]] 0.5 µM |  | -2.4 | -0.5 |
|  | [[Cepharanthine (drug)]] 5 µM |  | -2.1 | +0.2 |

## What is on record

|  |  |
|---|---|
| Name | ARB2 cotranscriptional regulator A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q15 — chr5:93,617,725-94,111,699 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP564D172, Toupee; previously C5orf21, FAM172A |
| Gene groups (HGNC) | MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WUF8](https://www.uniprot.org/uniprotkb/Q8WUF8) (Cotranscriptional regulator ARB2A):

> Plays a role in the regulation of alternative splicing, by interacting with AGO2 and CHD7. Seems to be required for stabilizing protein-protein interactions at the chromatin-spliceosome interface. May have hydrolase activity.

**Summary**, from NCBI Gene [83989](https://www.ncbi.nlm.nih.gov/gene/83989):

> Predicted to contribute to siRNA binding activity. Predicted to be involved in neural crest cell development; regulation of alternative mRNA splicing, via spliceosome; and regulatory ncRNA-mediated heterochromatin formation. Located in cytosol; endoplasmic reticulum; and nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25365](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25365) · Entrez [83989](https://www.ncbi.nlm.nih.gov/gene/83989) · UniProt [Q8WUF8](https://www.uniprot.org/uniprotkb/Q8WUF8) · Ensembl [ENSG00000113391](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000113391)

## Data

Gene col 3460: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3460); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3460, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3460]; `tensor/DDL_lfc|DDL_z.npy` [3460]; `embed/gene_vectors.npy` [3460]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3460 or target_col == 3460). Every well: [[FAM172A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM172A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
