---
symbol: "DENND1A"
type: "gene"
col: 4075
ensembl_id: "ENSG00000119522"
name: "DENN domain containing 1A"
location: "9q33.3"
module: 118
arm: "-"
pooled_cpm: 293.01
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 21
n_dd_up_clean: 0
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/118"]
generated_by: "tahoemap"
---

# DENND1A

*DENN domain containing 1A* — 9q33.3

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 5 lines (HEC-1-A 4.14×, HOP62 3.63×, NCI-H2347 3.13×, SW480 2.03×, …; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (HEC-1-A 3.51×, HOP62 3.35×, NCI-H2347 2.76×, SW480 1.95×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (HEC-1-A 3.60×, NCI-H2347 2.78×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.521× (z -20.4, q 0e+00, down in 45 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[VPS13A]] (+0.66, fdr 7e-06), [[EIF4G3]] (+0.54, fdr 3e-05), [[GMDS]] (+0.52, fdr 1e-05); moves opposite to [[APPBP2]] (-0.58, fdr 1e-05), [[CWC15]] (-0.53, fdr 3e-05), [[SCNM1]] (-0.53, fdr 5e-05).
> It sits in the **-** arm of [[Module 118]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TMEM92-AS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4075.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 5 lines (HEC-1-A 4.14×, HOP62 3.63×, NCI-H2347 3.13×, SW480 2.03×, …; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (HEC-1-A 3.51×, HOP62 3.35×, NCI-H2347 2.76×, SW480 1.95×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (HEC-1-A 3.60×, NCI-H2347 2.78×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.20× | +3.9 | 0.046 | 21/48 (A498, PANC-1, …) | inconsistent across doses |  |
| [[Verteporfin (drug)]] 5 µM |  | 1.16× | +3.2 | 0.35 | 21/49 (SHP-77, BT-474, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 16 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4075.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.521×** | -20.4 | 0e+00 | 45/49 (SW480, A549, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.470×** | -16.1 | 0e+00 | 46/47 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.554×** | -13.1 | 7e-37 | 40/48 (NCI-H23, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.607×** | -11.1 | 3e-26 | 43/48 (NCI-H23, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.625×** | -10.4 | 2e-23 | 45/48 (MIA PaCa-2, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.671×** | -8.8 | 9e-17 | 37/48 (SK-MEL-2, SW480, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~28% of this change | **0.696×** | -8.0 | 7e-14 | 41/48 (KATO III, C32, …) | inconsistent across doses | low cells (technical?) |
| [[TAK-901 (drug)]] 5 µM |  | **0.538×** | -7.2 | 5e-11 | 38/49 (C32, SK-MEL-2, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.724×** | -6.9 | 3e-10 | 33/50 (MIA PaCa-2, C32, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **0.733×** | -6.9 | 3e-10 | 29/48 (LS 180, HepG2/C3A, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **0.826×** | -6.0 | 1e-07 | 22/48 (RKO, SNU-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **0.759×** | -5.6 | 8e-07 | 25/45 (C32, A-427, …) | inconsistent across doses | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.779×** | -5.3 | 4e-06 | 28/48 (SW480, MIA PaCa-2, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.792×** | -5.2 | 9e-06 | 25/48 (RKO, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.802×** | -4.9 | 3e-05 | 26/48 (SW48, SK-MEL-2, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM |  | **0.681×** | -4.5 | 3e-04 | 34/47 (BT-474, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~22% here); noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.839× | -3.9 | 0.003 | 21/49 (KATO III, CFPAC-1, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **0.829×** | -3.9 | 0.003 | 24/47 (SW 900, SW1417, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.853× | -3.5 | 0.009 | 17/48 (J82, LS 180, …) | rises with dose |  |
| [[Vilanterol (drug)]] 5 µM |  | 0.895× | -3.5 | 0.011 | 4/49 (HS-578T, AN3 CA, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.764×** | -3.1 | 0.037 | 20/48 (SK-MEL-2, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Pralsetinib (drug)]] 5 µM |  | **0.771×** | -3.0 | 0.051 | 20/49 (NCI-H460, COLO 205, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4075. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 406 | 0 | 13 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.144× (z -24.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.540× (z -12.0) |
| [[MIA PaCa-2 (line)]] | alt | 467 | 0 | 11 (7 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.203× (z -21.9) ⚠ toxic · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.313× (z -16.6) |
| [[SW480 (line)]] | alt | 267 | 2 (2 ⚠) | 9 (5 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.03× (z +14.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.465× (z -23.0) |
| [[HEC-1-A (line)]] | alt | 341 | 3 (3 ⚠) | 7 (4 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.14× (z +21.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.448× (z -17.9) |
| [[RKO (line)]] | wt | 634 | 0 | 10 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.260× (z -17.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.372× (z -13.7) |
| [[SK-MEL-2 (line)]] | alt | 382 | 0 | 10 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.340× (z -15.6) |
| [[LOX-IMVI (line)]] | wt | 233 | 0 | 9 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.388× (z -19.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.433× (z -17.4) |
| [[HepG2_C3A (line)]] | wt | 341 | 0 | 8 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.313× (z -14.6) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.528× (z -11.9) |
| [[LS 180 (line)]] | wt | 392 | 0 | 8 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.383× (z -13.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.433× (z -11.4) |
| [[NCI-H2030 (line)]] | alt | 254 | 0 | 8 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.336× (z -14.2) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.503× (z -13.2) |
| [[SW48 (line)]] | wt | 359 | 0 | 8 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.403× (z -14.8) |
| [[LoVo (line)]] | wt | 486 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.417× (z -16.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.361× (z -13.9) |
| [[NCI-H1792 (line)]] | alt | 339 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -26.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.482× (z -15.9) |
| [[NCI-H23 (line)]] | alt | 400 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.366× (z -15.9) |
| [[NCI-H460 (line)]] | wt | 484 | 0 | 7 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.408× (z -14.0) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 5 µM 0.443× (z -13.2) |
| [[PANC-1 (line)]] | alt | 222 | 0 | 7 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.490× (z -16.4) |
| [[SW1417 (line)]] | alt | 259 | 0 | 7 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.450× (z -16.7) |
| [[J82 (line)]] | alt | 290 | 0 | 6 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.434× (z -18.7) |
| [[A-427 (line)]] | wt | 232 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.293× (z -17.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.510× (z -10.5) |
| [[A549 (line)]] | wt | 425 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.362× (z -22.4) |
| [[C-33 A (line)]] | alt | 509 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.443× (z -15.6) |
| [[HOP62 (line)]] | alt | 176 | 3 (3 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.63× (z +16.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.464× (z -14.0) |
| [[NCI-H2347 (line)]] | alt | 107 | 4 (4 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.13× (z +15.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.523× (z -13.1) |
| [[SNU-1 (line)]] | wt | 406 | 0 | 5 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.528× (z -11.8) |
| [[SNU-423 (line)]] | alt | 212 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.380× (z -22.2) |
| [[A498 (line)]] | wt | 182 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +13.2) ⚠ cell-cycle shift, would explain all of this change | — |
| [[AsPC-1 (line)]] | alt | 219 | 0 | 4 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.383× (z -12.8) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.552× (z -11.6) |
| [[A-172 (line)]] | wt | 300 | 1 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +10.7) ⚠ cell-cycle shift, would explain all of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.579× (z -9.7) |
| [[CFPAC-1 (line)]] | alt | 101 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.82× (z +12.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | [[Homoharringtonine (drug)]] 5 µM 0.576× (z -9.7) ⚠ cell-cycle shift, would explain all of this change |
| [[HT-29 (line)]] | alt | 191 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.509× (z -12.8) |
| [[Panc 03.27 (line)]] | alt | 180 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.46× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.528× (z -12.0) |
| [[SHP-77 (line)]] | alt | 457 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.525× (z -12.6) |
| [[SW 900 (line)]] | alt | 185 | 0 | 3 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.348× (z -14.9) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.602× (z -10.6) |
| [[COLO 205 (line)]] | alt | 238 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.451× (z -9.1) ⚠ toxic |
| [[HCT15 (line)]] | alt | 384 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.412× (z -10.6) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.562× (z -10.1) |
| [[Hs 766T (line)]] | wt | 260 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.392× (z -11.3) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.586× (z -9.5) |
| [[HS-578T (line)]] | alt | 191 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.497× (z -14.3) |
| [[KATO III (line)]] | alt | 308 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.440× (z -15.5) |
| [[RPMI-7951 (line)]] | alt | 202 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.546× (z -10.6) |
| [[AN3 CA (line)]] | alt | 344 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.386× (z -12.2) |
| [[BT-474 (line)]] | alt | 483 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.467× (z -15.4) |
| [[H4 (line)]] | wt | 241 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.409× (z -9.4) ⚠ toxic |
| [[NCI-H1573 (line)]] | alt | 132 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.442× (z -11.0) ⚠ cell-cycle shift, explains ~19% of this change |
| [[SW 1271 (line)]] | alt | 284 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.295× (z -8.7) ⚠ transcription drop; cell-cycle shift, explains ~28% of this change |
| [[CHP-212 (line)]] | wt | 273 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 119 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 289 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 316 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 216 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 180 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4075), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*37 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VPS13A]] | +0.66 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[EIF4G3]] | +0.54 | +0.52 / +0.45 | both halves | 3e-05 | same gene group |
| [[GMDS]] | +0.52 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[XPO5]] | +0.50 | +0.47 / +0.48 | both halves | 2e-05 |  |
| [[RUVBL1]] | +0.49 | +0.34 / +0.45 | both halves | 1e-04 |  |
| [[UBE2G2]] | +0.49 | +0.46 / +0.51 | both halves | 3e-05 |  |
| [[PRKAR1B]] | +0.49 | +0.32 / +0.53 | both halves | 2e-04 |  |
| [[AGPAT3]] | +0.49 | +0.35 / +0.56 | both halves | 1e-04 |  |
| [[IMMP2L]] | +0.47 | +0.31 / +0.53 | both halves | 2e-04 |  |
| [[CHCHD3]] | +0.47 | +0.32 / +0.49 | both halves | 2e-04 | same gene group |
| [[DDHD1]] | +0.46 | +0.51 / +0.38 | both halves | 7e-05 |  |
| [[XXYLT1]] | +0.46 | +0.52 / +0.29 | both halves | 3e-04 | same gene group |

## Genes that move opposite

*63 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[APPBP2]] | -0.58 | -0.53 / -0.55 | both halves | 1e-05 |  |
| [[CWC15]] | -0.53 | -0.44 / -0.54 | both halves | 3e-05 |  |
| [[SCNM1]] | -0.53 | -0.40 / -0.62 | both halves | 5e-05 |  |
| [[TMEM92-AS1]] | -0.52 | -0.42 / -0.52 | both halves | 4e-05 |  |
| [[SECISBP2L]] | -0.52 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[ZNF266]] | -0.50 | -0.43 / -0.39 | both halves | 6e-05 |  |
| [[EIF4E2]] | -0.50 | -0.26 / -0.49 | both halves | 3e-04 |  |
| [[KBTBD4]] | -0.50 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[ARMCX2]] | -0.49 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[COG1]] | -0.49 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[ZNF622]] | -0.48 | -0.38 / -0.57 | both halves | 6e-05 |  |
| [[TTI2]] | -0.48 | -0.38 / -0.54 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMEM92-AS1]] | B | TMEM92-AS1 activity weakens DENND1A's drug response | lines that do not express TMEM92-AS1 (16) vs lines expressing it (34) | the lines without TMEM92-AS1 respond 1.49× as strongly (z diff -2.30); strongest at Belinostat 5 µM: 0.57x vs 0.76x (z diff -3.7) | 0.059 | ⚠ within organs, on part of the lines; also absent: CXCL8, SPTLC3, PLOD2; artifact flags |
| [[PRKAR1B]] | B | PRKAR1B activity raises DENND1A's level | lines that do not express PRKAR1B (6) vs lines expressing it (44) | 1.80× lower at baseline in the lines without PRKAR1B | 0.068 | ⚠ within organs, on part of the lines; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 118]]; 41 genes; this gene is in the **-** arm (projection on the module's main direction -0.525). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-53.2, 4.1); signed map (5.5, -50.4). **Vector** length 121, 42.7% of its response variance represented; |z| ≥ 3 in 1,417 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +9.4 | +0.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +7.9 | -3.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | +6.7 | -5.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.3 | +3.9 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.9 | -0.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.2 | +1.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | +3.7 | +3.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.0 | +0.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.9 | +1.2 |
|  | [[EX229 (drug)]] 5 µM |  | +2.8 | +0.4 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -6.2 | -16.1 |
|  | [[Selinexor (drug)]] 5 µM |  | -5.7 | -6.0 |
|  | [[NG25 (drug)]] 5 µM |  | -4.9 | -4.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.9 | -3.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -3.8 | -10.4 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -3.8 | -2.7 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -3.2 | -1.6 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.6 | -2.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.2 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | DENN domain containing 1A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q33.3 — chr9:123,379,654-123,930,152 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ21129, FAM31A; previously KIAA1608 |
| Gene groups (HGNC) | DENN domain containing; MicroRNA protein coding host genes |
| Reactome | 4 pathways, smallest: RAB GEFs exchange GTP for GDP on RABs; Rab regulation of trafficking; Membrane Trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TEH3](https://www.uniprot.org/uniprotkb/Q8TEH3) (DENN domain-containing protein 1A):

> Guanine nucleotide exchange factor (GEF) regulating clathrin-mediated endocytosis through RAB35 activation. Promotes the exchange of GDP to GTP, converting inactive GDP-bound RAB35 into its active GTP-bound form. Regulates clathrin-mediated endocytosis of synaptic vesicles and mediates exit from early endosomes. Binds phosphatidylinositol-phosphates (PtdInsPs), with some preference for PtdIns(3)P (By similarity).

**Summary**, from NCBI Gene [57706](https://www.ncbi.nlm.nih.gov/gene/57706):

> Clathrin (see MIM 118955)-mediated endocytosis is a major mechanism for internalization of proteins and lipids. Members of the connecdenn family, such as DENND1A, function as guanine nucleotide exchange factors (GEFs) for the early endosomal small GTPase RAB35 (MIM 604199) and bind to clathrin and clathrin adaptor protein-2 (AP2; see MIM 601024). Thus, connecdenns link RAB35 activation with the clathrin machinery (Marat and McPherson, 2010 [PubMed 20154091]).[supplied by OMIM, Nov 2010]

**Accessions** — [HGNC:29324](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29324) · Entrez [57706](https://www.ncbi.nlm.nih.gov/gene/57706) · UniProt [Q8TEH3](https://www.uniprot.org/uniprotkb/Q8TEH3) · Ensembl [ENSG00000119522](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000119522)

## Data

Gene col 4075: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4075); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4075, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4075]; `tensor/DDL_lfc|DDL_z.npy` [4075]; `embed/gene_vectors.npy` [4075]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4075 or target_col == 4075). Every well: [[DENND1A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DENND1A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
