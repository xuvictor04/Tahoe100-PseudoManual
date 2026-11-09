---
symbol: "RUNX1"
type: "gene"
col: 8232
ensembl_id: "ENSG00000159216"
name: "RUNX family transcription factor 1"
location: "21q22.12"
module: 112
arm: "+"
pooled_cpm: 517.82
n_lines_expressing: 45
n_dd_up: 9
n_dd_down: 23
n_dd_up_clean: 7
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 18
direction_downstream: 11
tags: ["gene", "module/112"]
generated_by: "tahoemap"
---

# RUNX1

*RUNX family transcription factor 1* — 21q22.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.18× (z +8.3, q 8e-14, up in 30 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.460× (z -15.1, q 0e+00, down in 34 of 39 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.647× (z -12.5, q 2e-33, down in 31 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ETS1]] (+0.62, fdr 7e-06), [[SYNJ2]] (+0.60, fdr 1e-05), [[FRMD6]] (+0.59, fdr 1e-05); moves opposite to [[MIA2]] (-0.51, fdr 3e-05), [[RUFY2]] (-0.49, fdr 3e-05), [[FHIP2A]] (-0.46, fdr 5e-05).
> It is in [[Module 112]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 18 arrows point to it, the strongest [[DELEC1]] → it (grade B ⚠); 11 go from it, the strongest it → [[CSRNP1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8232.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.18×** | +8.3 | 8e-14 | 30/44 (NCI-H23, NCI-H2347, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.42×** | +7.1 | 5e-10 | 27/43 (SW 900, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.28×** | +5.0 | 1e-04 | 32/43 (SW 900, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.27×** | +4.8 | 2e-04 | 29/43 (SW 900, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.53×** | +4.5 | 6e-04 | 23/43 (CHP-212, A549, …) | top dose only | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.52×** | +4.5 | 8e-04 | 28/43 (Panc 03.27, HS-578T, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.23×** | +4.2 | 0.002 | 21/43 (NCI-H1573, SK-MEL-2, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | 1.15× | +4.0 | 0.005 | 18/43 (CFPAC-1, HT-29, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.21×** | +3.9 | 0.005 | 21/43 (A498, MIA PaCa-2, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.14× | +3.7 | 0.012 | 14/43 (HS-578T, A-172, …) | rises with dose |  |
| [[BAY1125976 (drug)]] 5 µM |  | **1.36×** | +3.3 | 0.054 | 22/43 (AsPC-1, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | 1.17× | +3.1 | 0.079 | 16/44 (A498, Hs 766T, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.16× | +3.1 | 0.088 | 17/43 (LoVo, HT-29, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 15 with an alert ⚠; shown: the 15 strongest and the 11 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8232.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.460×** | -15.1 | 0e+00 | 34/39 (LOX-IMVI, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.498×** | -14.1 | 9e-43 | 36/44 (HepG2/C3A, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.647×** | -12.5 | 2e-33 | 31/44 (SW480, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.564×** | -11.2 | 8e-27 | 40/42 (C32, SW480, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.622×** | -9.6 | 8e-20 | 36/43 (HEC-1-A, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.735×** | -6.2 | 5e-08 | 35/43 (HEC-1-A, LOX-IMVI, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.740×** | -6.1 | 8e-08 | 31/43 (PANC-1, HOP62, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.813×** | -5.9 | 2e-07 | 23/43 (C32, J82, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~6% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.739×** | -5.9 | 2e-07 | 28/45 (LOX-IMVI, SW480, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.745×** | -5.7 | 5e-07 | 26/43 (SW480, C32, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.760×** | -5.1 | 1e-05 | 26/40 (HepG2/C3A, LOX-IMVI, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.799×** | -4.5 | 3e-04 | 25/43 (HEC-1-A, HepG2/C3A, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.803×** | -4.4 | 4e-04 | 23/43 (C32, HOP62, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.794×** | -4.4 | 4e-04 | 24/43 (C32, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.805×** | -4.4 | 4e-04 | 26/43 (A549, NCI-H1792, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.806×** | -4.4 | 5e-04 | 22/43 (HepG2/C3A, C32, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.832×** | -4.3 | 6e-04 | 22/43 (AsPC-1, NCI-H1573, …) | two highest doses | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.802×** | -4.3 | 6e-04 | 23/43 (AsPC-1, NCI-H1573, …) | rises with dose |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **0.813×** | -4.2 | 8e-04 | 23/43 (A549, NCI-H1792, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.818×** | -4.1 | 0.001 | 23/43 (A549, NCI-H1792, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM |  | **0.684×** | -4.0 | 0.002 | 21/42 (C32, RKO, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | 0.839× | -3.6 | 0.008 | 21/43 (C32, LOX-IMVI, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.839× | -3.6 | 0.008 | 21/44 (AsPC-1, NCI-H1573, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.835× | -3.5 | 0.010 | 19/43 (SNU-423, CFPAC-1, …) | top dose only |  |
| [[Budesonide (drug)]] 0.05 µM |  | 0.853× | -3.2 | 0.026 | 20/43 (SNU-423, A549, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | 0.848× | -3.2 | 0.026 | 21/44 (A549, SNU-423, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8232. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 968 | 1 | 20 (11 ⚠) | [[Cobimetinib (drug)]] 0.5 µM 2.15× (z +9.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.408× (z -15.5) |
| [[LOX-IMVI (line)]] | wt | 1,502 | 0 | 13 (10 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.214× (z -19.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.379× (z -17.4) |
| [[BT-474 (line)]] | alt | 193 | 11 | 0 | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 3.31× (z +11.6) | — |
| [[HepG2_C3A (line)]] | wt | 759 | 0 | 11 (9 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.183× (z -20.9) ⚠ toxic; transcription drop · without an alert: [[Ponatinib (drug)]] 5 µM 0.348× (z -13.0) |
| [[SW480 (line)]] | alt | 824 | 0 | 11 (9 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.360× (z -21.9) |
| [[AsPC-1 (line)]] | alt | 543 | 1 (1 ⚠) | 7 | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +10.6) ⚠ cell-cycle shift, explains ~35% of this change | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM 0.413× (z -11.7) |
| [[hTERT-HPNE (line)]] | wt | 839 | 0 | 8 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.426× (z -13.8) |
| [[HEC-1-A (line)]] | alt | 422 | 0 | 7 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.214× (z -18.3) ⚠ cell-cycle shift, explains ~26% of this change |
| [[Panc 03.27 (line)]] | alt | 1,018 | 0 | 7 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.289× (z -20.4) |
| [[SNU-423 (line)]] | alt | 584 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.333× (z -14.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.486× (z -13.7) |
| [[J82 (line)]] | alt | 449 | 2 (2 ⚠) | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.61× (z +10.0) ⚠ cell-cycle shift, explains ~35% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.534× (z -13.0) |
| [[MIA PaCa-2 (line)]] | alt | 804 | 1 (1 ⚠) | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.73× (z +10.3) ⚠ cell-cycle shift, explains ~27% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.422× (z -12.6) |
| [[A498 (line)]] | wt | 594 | 2 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.07× (z +10.4) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.91× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.308× (z -16.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.617× (z -9.7) |
| [[CFPAC-1 (line)]] | alt | 711 | 2 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +21.3) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 3.71× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.345× (z -14.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.583× (z -10.7) |
| [[A-172 (line)]] | wt | 898 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.243× (z -19.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.407× (z -17.2) |
| [[HOP62 (line)]] | alt | 765 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.329× (z -11.7) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 531 | 1 | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.03× (z +9.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.438× (z -15.8) |
| [[PANC-1 (line)]] | alt | 345 | 0 | 4 (4 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.518× (z -10.4) ⚠ cell-cycle shift, explains ~28% of this change |
| [[RPMI-7951 (line)]] | alt | 617 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.483× (z -14.1) |
| [[SW 900 (line)]] | alt | 473 | 2 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.04× (z +11.0) | [[Dinaciclib (drug)]] 5 µM 0.503× (z -10.1) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 203 | 2 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.68× (z +9.6) | [[Panobinostat (drug)]] 5 µM 0.511× (z -8.8) ⚠ cell-cycle shift, explains ~26% of this change |
| [[NCI-H1792 (line)]] | alt | 608 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.300× (z -15.8) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 287 | 3 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.28× (z +10.5) | — |
| [[RKO (line)]] | wt | 585 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.204× (z -18.5) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 188 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.39× (z +8.6) | [[Panobinostat (drug)]] 5 µM 0.384× (z -9.5) ⚠ cell-cycle shift, explains ~26% of this change |
| [[HS-578T (line)]] | alt | 659 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.494× (z -11.1) |
| [[NCI-H1573 (line)]] | alt | 588 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +8.5) ⚠ cell-cycle shift, explains ~35% of this change | [[Dinaciclib (drug)]] 5 µM 0.328× (z -11.0) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 297 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.92× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.351× (z -12.5) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 567 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.459× (z -11.5) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.532× (z -9.3) |
| [[A549 (line)]] | wt | 341 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.586× (z -10.4) |
| [[CHP-212 (line)]] | wt | 338 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.440× (z -9.9) ⚠ cell-cycle shift, explains ~35% of this change |
| [[COLO 205 (line)]] | alt | 881 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.367× (z -11.9) |
| [[H4 (line)]] | wt | 554 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.419× (z -9.9) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 341 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.355× (z -11.4) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 187 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +15.0) ⚠ cell-cycle shift, explains ~35% of this change | — |
| [[KATO III (line)]] | alt | 478 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.450× (z -11.3) |
| [[NCI-H2030 (line)]] | alt | 280 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.25× (z +8.8) | — |
| [[A-427 (line)]] | wt | 126 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 95.4 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 73.3 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 367 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 116 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 593 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 565 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 92.4 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 163 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 614 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 355 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 388 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 133 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8232), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ETS1]] | +0.62 | +0.59 / +0.58 | both halves | 7e-06 | pathway: Differentiation of T cells; STRING 999 |
| [[SYNJ2]] | +0.60 | +0.53 / +0.61 | both halves | 1e-05 | pathway: HALLMARK_UV_RESPONSE_DN |
| [[FRMD6]] | +0.59 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[CXCL8]] | +0.58 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[MIR155HG]] | +0.57 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[SMAD3]] | +0.57 | +0.50 / +0.57 | both halves | 1e-05 | pathway: HALLMARK_UV_RESPONSE_DN; STRING 878 |
| [[FRMD4A]] | +0.56 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[ATP13A3]] | +0.56 | +0.48 / +0.61 | both halves | 2e-05 |  |
| [[SHB]] | +0.56 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[CD44]] | +0.55 | +0.49 / +0.58 | both halves | 1e-05 | STRING 583 |
| [[HRH1]] | +0.55 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[NGF]] | +0.55 | +0.42 / +0.54 | both halves | 4e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MIA2]] | -0.51 | -0.52 / -0.46 | both halves | 3e-05 |  |
| [[RUFY2]] | -0.49 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[FHIP2A]] | -0.46 | -0.39 / -0.42 | both halves | 5e-05 |  |
| [[ZBTB7B]] | -0.46 | -0.35 / -0.43 | both halves | 1e-04 | STRING 542 |
| [[CIZ1]] | -0.45 | -0.51 / -0.33 | both halves | 1e-04 |  |
| [[SNX4]] | -0.44 | -0.35 / -0.37 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 18, C 0. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DELEC1]] | B | DELEC1 activity raises RUNX1's level | lines that do not express DELEC1 (6) vs lines expressing it (44) | 2.81× lower at baseline in the lines without DELEC1 | 0.003 | ⚠ within organs, on part of the lines; also absent: NDRG1, SLC2A1, ZHX2; maybe low, not absent |
| [[HRH1]] | B | HRH1 activity raises RUNX1's level | lines that do not express HRH1 (10) vs lines expressing it (40) | 2.91× lower at baseline in the lines without HRH1 | 0.005 | ⚠ within organs, on part of the lines; also absent: PHLDA2, PLAUR, LRRK1; maybe low, not absent |
| [[ADTRP]] | B | ADTRP activity raises RUNX1's level | lines that do not express ADTRP (25) vs lines expressing it (25) | 2.19× lower at baseline in the lines without ADTRP | 0.007 | ⚠ within organs, on part of the lines; also absent: LINC02725, ROBO4, AIM2 |
| [[EVA1A]] | B | EVA1A activity raises RUNX1's level | lines that do not express EVA1A (21) vs lines expressing it (29) | 2.30× lower at baseline in the lines without EVA1A | 0.015 | ⚠ within organs, on part of the lines; also absent: NLRP1, MILR1, SNAI2 |
| [[PLAU]] | B | PLAU activity raises RUNX1's level | lines that do not express PLAU (26) vs lines expressing it (24) | 1.81× lower at baseline in the lines without PLAU | 0.031 | ⚠ within organs, on part of the lines; also absent: ADAMTS16, C3, VGLL3 |
| [[SLC43A3]] | B | SLC43A3 activity raises RUNX1's level | lines that do not express SLC43A3 (28) vs lines expressing it (22) | 2.15× lower at baseline in the lines without SLC43A3 | 0.034 | ⚠ within organs, on part of the lines; also absent: ENSG00000254979, FN1, ENSG00000234261 |
| [[G0S2]] | B | G0S2 activity raises RUNX1's level | lines that do not express G0S2 (33) vs lines expressing it (17) | 1.79× lower at baseline in the lines without G0S2 | 0.036 | ⚠ within organs, on part of the lines; also absent: IL6, EDNRA, RRAD |
| [[KIAA1217]] | B | KIAA1217 activity raises RUNX1's level | lines that do not express KIAA1217 (10) vs lines expressing it (40) | 2.28× lower at baseline in the lines without KIAA1217 | 0.037 | ⚠ within organs, on part of the lines; also absent: FAM107B, MET, S100A16 |
| [[IL31RA]] | B | IL31RA activity raises RUNX1's level | lines that do not express IL31RA (28) vs lines expressing it (22) | 1.71× lower at baseline in the lines without IL31RA | 0.049 | ⚠ within organs, on part of the lines; also absent: EFEMP1, EYA4, CCBE1 |
| [[FAM107B]] | B | FAM107B activity raises RUNX1's level | lines that do not express FAM107B (11) vs lines expressing it (39) | 1.65× lower at baseline in the lines without FAM107B | 0.059 | ⚠ within organs, on part of the lines; also absent: KIAA1217, ETS2, NRP1 |
| [[BCL2A1]] | B | BCL2A1 activity strengthens RUNX1's drug response | lines that do not express BCL2A1 (22) vs lines expressing it (22) | the lines without BCL2A1 respond 0.69× as strongly (z diff +2.03); strongest at Idarubicin (hydrochloride) 5 µM: 0.76x vs 0.60x (z diff +4.2) | 0.059 | ⚠ within organs, on part of the lines; also absent: BASP1-AS1, TMEM156, CSGALNACT1; target measured in part of the lines; artifact flags |
| [[LINC00973]] | B | LINC00973 activity raises RUNX1's level | lines that do not express LINC00973 (23) vs lines expressing it (27) | 2.09× lower at baseline in the lines without LINC00973 | 0.070 | ⚠ within organs, on part of the lines; also absent: ENSG00000239462, IL11, BICC1 |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 11, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CSRNP1]] | B | RUNX1 activity raises CSRNP1's level | lines that do not express RUNX1 (5) vs lines expressing it (45) | 2.36× lower at baseline in the lines without RUNX1 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with WNK2; also absent: KIFC3, STAMBPL1, TRIB1; maybe low, not absent |
| [[ETS1]] | B | RUNX1 activity raises ETS1's level | lines that do not express RUNX1 (5) vs lines expressing it (45) | 5.19× lower at baseline in the lines without RUNX1 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with WNK2; also absent: KIFC3, STAMBPL1, TRIB1; maybe low, not absent |
| [[TRAF1]] | B | RUNX1 activity raises TRAF1's level | lines that do not express RUNX1 (5) vs lines expressing it (45) | 2.99× lower at baseline in the lines without RUNX1 | 0.019 | ⚠ within organs, on part of the lines; co-occurs with WNK2; also absent: KIFC3, STAMBPL1, TRIB1; maybe low, not absent |
| [[ACTN1]] | B | RUNX1 activity raises ACTN1's level | lines that do not express RUNX1 (5) vs lines expressing it (45) | 2.54× lower at baseline in the lines without RUNX1 | 0.020 | ⚠ within organs, on part of the lines; co-occurs with WNK2; also absent: KIFC3, STAMBPL1, TRIB1; maybe low, not absent |
| [[SMAD3]] | B | RUNX1 activity raises SMAD3's level | lines that do not express RUNX1 (5) vs lines expressing it (45) | 4.26× lower at baseline in the lines without RUNX1 | 0.021 | ⚠ within organs, on part of the lines; co-occurs with WNK2; also absent: KIFC3, STAMBPL1, TRIB1; maybe low, not absent |
| [[LIF]] | B | RUNX1 activity raises LIF's level | lines that do not express RUNX1 (5) vs lines expressing it (45) | 3.21× lower at baseline in the lines without RUNX1 | 0.025 | ⚠ within organs, on part of the lines; co-occurs with WNK2; also absent: KIFC3, STAMBPL1, TRIB1; maybe low, not absent |
| [[NEDD4L]] | B | RUNX1 activity raises NEDD4L's level | lines that do not express RUNX1 (5) vs lines expressing it (45) | 1.81× lower at baseline in the lines without RUNX1 | 0.055 | ⚠ within organs, on part of the lines; co-occurs with WNK2; also absent: KIFC3, STAMBPL1, TRIB1; maybe low, not absent |
| [[MSANTD3]] | B | RUNX1 activity raises MSANTD3's level | lines that do not express RUNX1 (5) vs lines expressing it (45) | 2.23× lower at baseline in the lines without RUNX1 | 0.057 | ⚠ within organs, on part of the lines; co-occurs with WNK2; also absent: KIFC3, STAMBPL1, TRIB1; maybe low, not absent |
| [[BACH1]] | B | RUNX1 activity raises BACH1's level | lines that do not express RUNX1 (5) vs lines expressing it (45) | 2.24× lower at baseline in the lines without RUNX1 | 0.067 | ⚠ within organs, on part of the lines; co-occurs with WNK2; also absent: KIFC3, STAMBPL1, TRIB1; maybe low, not absent |
| [[SHB]] | B | RUNX1 activity raises SHB's level | lines that do not express RUNX1 (5) vs lines expressing it (45) | 2.87× lower at baseline in the lines without RUNX1 | 0.083 | ⚠ within organs, on part of the lines; co-occurs with WNK2; also absent: KIFC3, STAMBPL1, TRIB1; maybe low, not absent |
| [[ACTN1]] | B | RUNX1 activity strengthens ACTN1's drug response | lines that do not express RUNX1 (5) vs lines expressing it (43) | the lines without RUNX1 respond 0.62× as strongly (z diff +0.87); strongest at Idarubicin (hydrochloride) 5 µM: 1.05x vs 0.62x (z diff +5.1) | 0.097 | ⚠ within organs, on part of the lines; co-occurs with WNK2; also absent: KIFC3, STAMBPL1, TRIB1; maybe low, not absent; target measured in part of the lines; artifact flags |

## Where it sits

- **Module**: [[Module 112]] — TNF-alpha signaling via NF-kB; 43 genes; every member is in the + arm (projection on the module's main direction 0.645). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (41.9, 1.5); signed map (4.4, 44.3). **Vector** length 115, 36.8% of its response variance represented; |z| ≥ 3 in 1,609 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.7 | +3.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.1 | +8.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.0 | +2.3 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.6 | +0.4 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +3.5 | +4.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.4 | +2.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.0 | +0.7 |
|  | [[Belzutifan (drug)]] 5 µM |  | +2.4 | +0.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.2 | +4.5 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -5.9 | -4.4 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -4.7 | -4.4 |
|  | [[NG25 (drug)]] 5 µM |  | -3.6 | -4.0 |
|  | [[Selinexor (drug)]] 5 µM |  | -3.5 | -5.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.3 | -1.9 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -3.0 | -1.7 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.9 | +0.3 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.7 | -1.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.7 | -4.3 |

## What is on record

|  |  |
|---|---|
| Name | RUNX family transcription factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q22.12 — chr21:34,787,801-36,004,667 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PEBP2A2, AMLCR1; previously AML1, CBFA2 |
| Gene groups (HGNC) | Runt-related transcription factors |
| Hallmark sets | UV_RESPONSE_DN |
| Reactome | 35 pathways, smallest: RUNX1 and FOXP3 control the development of regulatory T lymphocytes (Tregs); RUNX3 regulates RUNX1-mediated transcription; RUNX1 regulates expression of components of tight junctions |
| Matched by | ensembl_id |

**Function**, from UniProt [Q01196](https://www.uniprot.org/uniprotkb/Q01196) (Runt-related transcription factor 1):

> Forms the heterodimeric complex core-binding factor (CBF) with CBFB. RUNX members modulate the transcription of their target genes through recognizing the core consensus binding sequence 5'-TGTGGT-3', or very rarely, 5'-TGCGGT-3', within their regulatory regions via their runt domain, while CBFB is a non-DNA-binding regulatory subunit that allosterically enhances the sequence-specific DNA-binding capacity of RUNX. The heterodimers bind to the core site of a number of enhancers and promoters, …

**Summary**, from NCBI Gene [861](https://www.ncbi.nlm.nih.gov/gene/861):

> Core binding factor (CBF) is a heterodimeric transcription factor that binds to the core element of many enhancers and promoters. The protein encoded by this gene represents the alpha subunit of CBF and is thought to be involved in the development of normal hematopoiesis. Chromosomal translocations involving this gene are well-documented and have been associated with several types of leukemia. Three transcript variants encoding different isoforms have been found for this gene. [provided by …

**Accessions** — [HGNC:10471](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10471) · Entrez [861](https://www.ncbi.nlm.nih.gov/gene/861) · UniProt [Q01196](https://www.uniprot.org/uniprotkb/Q01196) · Ensembl [ENSG00000159216](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000159216)

## Data

Gene col 8232: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8232); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8232, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8232]; `tensor/DDL_lfc|DDL_z.npy` [8232]; `embed/gene_vectors.npy` [8232]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8232 or target_col == 8232). Every well: [[RUNX1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RUNX1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
