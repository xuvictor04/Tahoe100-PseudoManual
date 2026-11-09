---
symbol: "APPBP2"
type: "gene"
col: 716
ensembl_id: "ENSG00000062725"
name: "amyloid beta precursor protein binding protein 2"
location: "17q23.2"
module: 118
arm: "+"
pooled_cpm: 121.33
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 19
n_dd_up_clean: 2
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/118"]
generated_by: "tahoemap"
---

# APPBP2

*amyloid beta precursor protein binding protein 2* — 17q23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 2.41× (z +10.0, q 7e-21, up in 43 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[TAK-901 (drug)]] 5 µM in 6 lines (SW480 3.81×, NCI-H460 3.93×, C-33 A 4.04×, LS 180 4.34×, …); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (SW1417 1.74×, HT-29 1.82×, MIA PaCa-2 1.60×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H23 2.75×, SK-MEL-2 1.97×; ⚠ cell-cycle shift, explains ~0% of this change); [[PH-797804 (drug)]] 5 µM in 1 line (LS 180 4.32×).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (14 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.390× (z -22.7, q 0e+00, down in 47 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.723× (z -7.8, q 4e-13, down in 32 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF490]] (+0.70, fdr 7e-06), [[CNPY2]] (+0.70, fdr 7e-06), [[ZNF791]] (+0.67, fdr 1e-05); moves opposite to [[GMDS]] (-0.60, fdr 1e-05), [[CMSS1]] (-0.59, fdr 1e-05), [[IDH3A]] (-0.58, fdr 1e-05).
> It sits in the **+** arm of [[Module 118]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 716.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[TAK-901 (drug)]] 5 µM in 6 lines (SW480 3.81×, NCI-H460 3.93×, C-33 A 4.04×, LS 180 4.34×, …); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (SW1417 1.74×, HT-29 1.82×, MIA PaCa-2 1.60×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H23 2.75×, SK-MEL-2 1.97×; ⚠ cell-cycle shift, explains ~0% of this change); [[PH-797804 (drug)]] 5 µM in 1 line (LS 180 4.32×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.41×** | +10.0 | 7e-21 | 43/49 (SW480, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.81×** | +6.8 | 4e-09 | 29/48 (LS 180, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~90% of this change | 1.12× | +3.9 | 0.019 | 9/48 (SW1417, LOX-IMVI, …) | rises with dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~98% of this change | 1.15× | +3.4 | 0.098 | 15/48 (A-427, Hs 766T, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 0.05 µM |  | 1.15× | +3.3 | 0.13 | 10/49 (SW480, NCI-H23, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 20 with an alert ⚠; shown: the 15 strongest and the 11 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 716.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.390×** | -22.7 | 0e+00 | 47/49 (A-172, AN3 CA, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.412×** | -20.6 | 0e+00 | 42/44 (HEC-1-A, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.544×** | -13.5 | 4e-39 | 38/45 (A-427, C-33 A, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.592×** | -12.6 | 2e-34 | 45/48 (HOP62, A549, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.632×** | -11.1 | 2e-26 | 43/48 (SNU-423, HOP62, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.691×** | -8.9 | 6e-17 | 35/48 (HOP62, CFPAC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.723×** | -7.8 | 4e-13 | 32/48 (A498, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~16% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | **0.719×** | -7.6 | 2e-12 | 32/47 (SW 900, CFPAC-1, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.765×** | -6.2 | 4e-08 | 32/48 (C32, NCI-H1792, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~41% of this change | **0.794×** | -5.6 | 2e-06 | 30/48 (HOP62, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change | **0.797×** | -5.4 | 3e-06 | 27/48 (A549, HOP62, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.818×** | -4.8 | 7e-05 | 24/48 (HOP62, NCI-H1792, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.823×** | -4.7 | 1e-04 | 25/48 (CFPAC-1, NCI-H1792, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.825×** | -4.6 | 2e-04 | 23/48 (HOP62, H4, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~81% of this change | **0.831×** | -4.4 | 3e-04 | 23/48 (KATO III, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Abemaciclib (drug)]] 5 µM |  | **0.676×** | -4.4 | 3e-04 | 26/48 (NCI-H460, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.842× | -4.1 | 0.001 | 21/48 (A498, A-172, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.891× | -3.9 | 0.003 | 13/48 (SW 900, HOP62, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.858× | -3.7 | 0.006 | 14/47 (MIA PaCa-2, H4, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.862× | -3.6 | 0.009 | 18/48 (CFPAC-1, SK-MEL-2, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.854× | -3.5 | 0.012 | 20/47 (H4, NCI-H460, …) | inconsistent across doses | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | 0.865× | -3.5 | 0.012 | 21/48 (BT-474, MIA PaCa-2, …) | top dose only |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.817×** | -3.5 | 0.012 | 18/48 (Hs 766T, A-427, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Pralsetinib (drug)]] 5 µM |  | **0.757×** | -3.2 | 0.032 | 17/49 (A-172, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.05 µM |  | 0.870× | -3.1 | 0.042 | 12/48 (NCI-H460, RKO, …) | inconsistent across doses |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | 0.848× | -2.8 | 0.081 | 11/48 (Hs 766T, RPMI-7951, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 716. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 160 | 0 | 8 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.273× (z -16.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[HOP62 (line)]] | alt | 160 | 0 | 7 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.276× (z -18.4) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 395 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.431× (z -11.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.555× (z -8.6) |
| [[SNU-423 (line)]] | alt | 157 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.253× (z -17.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[SW 900 (line)]] | alt | 135 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.252× (z -16.7) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 176 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.207× (z -24.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[A498 (line)]] | wt | 128 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.282× (z -18.4) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.427× (z -12.8) |
| [[HEC-1-A (line)]] | alt | 162 | 1 | 4 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 3.17× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.269× (z -20.2) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 203 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.229× (z -16.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[LS 180 (line)]] | wt | 87.9 | 2 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.34× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.248× (z -17.0) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 108 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.310× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[Panc 03.27 (line)]] | alt | 137 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.298× (z -16.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[A549 (line)]] | wt | 151 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.314× (z -15.4) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 101 | 2 (1 ⚠) | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.60× (z +8.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.03× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.396× (z -11.5) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 125 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0816× (z -32.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[AsPC-1 (line)]] | alt | 79.9 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.515× (z -11.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 191 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.04× (z +8.9) | [[Dinaciclib (drug)]] 0.5 µM 0.183× (z -22.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[H4 (line)]] | wt | 174 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.243× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[HepG2_C3A (line)]] | wt | 121 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.287× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[NCI-H1573 (line)]] | alt | 110 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.362× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.516× (z -8.7) |
| [[NCI-H1792 (line)]] | alt | 130 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.205× (z -19.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[NCI-H460 (line)]] | wt | 106 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 3.93× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.460× (z -11.2) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 107 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.253× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[SW480 (line)]] | alt | 125 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 3.81× (z +10.2) | [[Dinaciclib (drug)]] 0.5 µM 0.486× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[C32 (line)]] | wt | 95.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.371× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[CHP-212 (line)]] | wt | 272 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.135× (z -17.7) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 110 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.298× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[HT-29 (line)]] | alt | 79.9 | 1 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.82× (z +9.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.251× (z -15.1) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 88.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.389× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[KATO III (line)]] | alt | 124 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.234× (z -18.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[LOX-IMVI (line)]] | wt | 114 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.356× (z -12.6) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 90.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.301× (z -14.1) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 112 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +17.0) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.428× (z -9.6) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 131 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +11.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.471× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[SNU-1 (line)]] | wt | 121 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.144× (z -19.7) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 143 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0676× (z -11.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Procainamide (hydrochloride) (drug)]] 0.05 µM 0.0850× (z -10.3) |
| [[SW 1271 (line)]] | alt | 147 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0932× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Thymol (drug)]] 0.5 µM 0.159× (z -10.2) |
| [[SW1417 (line)]] | alt | 77.3 | 1 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.74× (z +10.0) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.412× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[AN3 CA (line)]] | alt | 127 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0437× (z -23.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[COLO 205 (line)]] | alt | 149 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.379× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[HCT15 (line)]] | alt | 138 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.370× (z -8.8) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 89.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.437× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[LoVo (line)]] | wt | 83.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 127 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 63.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 86.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 76.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 78.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 716), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF490]] | +0.70 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[CNPY2]] | +0.70 | +0.58 / +0.65 | both halves | 7e-06 |  |
| [[ZNF791]] | +0.67 | +0.69 / +0.56 | both halves | 1e-05 |  |
| [[ZMYM5]] | +0.65 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[ISY1]] | +0.65 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[BRAP]] | +0.64 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[MED4]] | +0.64 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[SYNRG]] | +0.64 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[QRICH1]] | +0.64 | +0.51 / +0.66 | both halves | 1e-05 |  |
| [[TTI2]] | +0.63 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[ZSWIM3]] | +0.63 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[NAA60]] | +0.63 | +0.53 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GMDS]] | -0.60 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[CMSS1]] | -0.59 | -0.58 / -0.52 | both halves | 1e-05 |  |
| [[IDH3A]] | -0.58 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[DENND1A]] | -0.58 | -0.53 / -0.55 | both halves | 1e-05 |  |
| [[VPS13A]] | -0.55 | -0.46 / -0.54 | both halves | 3e-05 |  |
| [[EFR3A]] | -0.55 | -0.49 / -0.54 | both halves | 1e-05 |  |
| [[FYCO1]] | -0.53 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[AHCY]] | -0.53 | -0.53 / -0.46 | both halves | 3e-05 |  |
| [[TBCD]] | -0.53 | -0.42 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 118]]; 41 genes; this gene is in the **+** arm (projection on the module's main direction 0.766). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-52.8, 4.2); signed map (-4.9, -3.4). **Vector** length 112, 35.2% of its response variance represented; |z| ≥ 3 in 1,128 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +8.1 | +10.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +6.4 | +2.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~90% of this change | +5.2 | +3.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.1 | +6.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.6 | -0.3 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.3 | -0.6 |
|  | [[Almonertinib (hydrochloride) (drug)]] 0.05 µM |  | +2.3 | +2.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | -0.6 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | +2.1 | +2.1 |
| fall | [[Belumosudil (drug)]] 5 µM |  | -5.3 | -6.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | -5.2 | -7.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | -4.9 | -11.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -4.1 | -12.6 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | -4.0 | -4.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.6 | -3.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.1 | -4.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.8 | -2.6 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | -2.7 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | amyloid beta precursor protein binding protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q23.2 — chr17:60,443,158-60,526,242 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0228, Hs.84084, PAT1 |
| Hallmark sets | ANDROGEN_RESPONSE |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92624](https://www.uniprot.org/uniprotkb/Q92624) (Amyloid protein-binding protein 2):

> Substrate-recognition component of a Cul2-RING (CRL2) E3 ubiquitin-protein ligase complex of the DesCEND (destruction via C-end degrons) pathway, which recognizes a C-degron located at the extreme C terminus of target proteins, leading to their ubiquitination and degradation. The C-degron recognized by the DesCEND pathway is usually a motif of less than ten residues and can be present in full-length proteins, truncated proteins or proteolytically cleaved forms. The CRL2(APPBP2) complex …

**Summary**, from NCBI Gene [10513](https://www.ncbi.nlm.nih.gov/gene/10513):

> The protein encoded by this gene interacts with microtubules and is functionally associated with beta-amyloid precursor protein transport and/or processing. The beta-amyloid precursor protein is a cell surface protein with signal-transducing properties, and it is thought to play a role in the pathogenesis of Alzheimer's disease. The encoded protein may be involved in regulating cell death. This gene has been found to be highly expressed in breast cancer. Alternative splicing results in multiple …

**Accessions** — [HGNC:622](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:622) · Entrez [10513](https://www.ncbi.nlm.nih.gov/gene/10513) · UniProt [Q92624](https://www.uniprot.org/uniprotkb/Q92624) · Ensembl [ENSG00000062725](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000062725)

## Data

Gene col 716: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 716); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 716, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 716]; `tensor/DDL_lfc|DDL_z.npy` [716]; `embed/gene_vectors.npy` [716]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 716 or target_col == 716). Every well: [[APPBP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/APPBP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
