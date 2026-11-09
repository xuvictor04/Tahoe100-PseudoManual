---
symbol: "DISC1"
type: "gene"
col: 8604
ensembl_id: "ENSG00000162946"
name: "DISC1 scaffold protein"
location: "1q42.2"
module: 37
arm: "+"
pooled_cpm: 63.17
n_lines_expressing: 45
n_dd_up: 10
n_dd_down: 28
n_dd_up_clean: 7
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 3
direction_downstream: 2
tags: ["gene", "module/037"]
generated_by: "tahoemap"
---

# DISC1

*DISC1 scaffold protein* — 1q42.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.67× (z +9.9, q 3e-20, up in 30 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (15 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.401× (z -17.5, q 0e+00, down in 29 of 42 measured lines) ⚠ cell-cycle shift, explains ~46% of this change. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.413× (z -12.0, q 6e-31, down in 35 of 43 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC01950]] (+0.55, fdr 2e-04), [[UBA6-DT]] (+0.52, fdr 1e-04), [[BCO2]] (+0.50, fdr 7e-05); moves opposite to [[TADA2A]] (-0.46, fdr 1e-04), [[BSN]] (-0.46, fdr 4e-04), [[FAHD2CP]] (-0.45, fdr 6e-04).
> It is in [[Module 037]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[CASC20]] → it (grade B ⚠); 2 go from it, the strongest it → [[RAPGEF4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8604.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.67×** | +9.9 | 3e-20 | 30/44 (HS-578T, NCI-H23, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.81×** | +7.7 | 4e-12 | 28/45 (HS-578T, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.73×** | +7.4 | 2e-11 | 29/43 (A-172, HOP62, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | **1.40×** | +6.5 | 1e-08 | 23/43 (A-427, NCI-H23, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.47×** | +5.1 | 5e-05 | 22/43 (HS-578T, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.28×** | +4.7 | 3e-04 | 24/43 (NCI-H2347, LS 180, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.33×** | +3.8 | 0.010 | 18/43 (A-427, HOP62, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.35×** | +3.6 | 0.019 | 18/43 (SHP-77, A-172, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.31×** | +3.6 | 0.019 | 14/43 (SHP-77, A-172, …) | all doses, flat |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.32×** | +3.6 | 0.021 | 18/43 (A-172, H4, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | 1.26× | +3.1 | 0.10 | 19/44 (NCI-H2347, LS 180, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.25× | +3.0 | 0.12 | 15/43 (LS 180, SW480, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 15 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8604.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.401×** | -17.5 | 0e+00 | 29/42 (RKO, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.322×** | -14.7 | 0e+00 | 36/42 (RKO, NCI-H460, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **0.364×** | -13.7 | 3e-40 | 37/43 (SHP-77, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.371×** | -13.4 | 7e-39 | 36/43 (SW480, HepG2/C3A, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.377×** | -12.7 | 7e-35 | 37/42 (RKO, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.413×** | -12.0 | 6e-31 | 35/43 (SW480, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.457×** | -10.6 | 2e-24 | 30/43 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.480×** | -9.9 | 2e-21 | 28/42 (RKO, COLO 205, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.470×** | -9.8 | 6e-21 | 26/32 (SW 900, HCT15, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.473×** | -9.4 | 4e-19 | 26/37 (hTERT-HPNE, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~20% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.276×** | -9.1 | 5e-18 | 29/44 (RKO, CHP-212, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **0.513×** | -8.7 | 2e-16 | 29/41 (H4, HepG2/C3A, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.469×** | -8.2 | 1e-14 | 29/42 (NCI-H1573, COLO 205, …) | all doses, flat | composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.653×** | -5.8 | 4e-07 | 29/43 (NCI-H1792, CFPAC-1, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.464×** | -5.4 | 2e-06 | 26/41 (RKO, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.674×** | -4.3 | 7e-04 | 24/43 (HepG2/C3A, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.562×** | -4.1 | 0.001 | 22/42 (CFPAC-1, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.815×** | -3.9 | 0.003 | 22/44 (CFPAC-1, SW480, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.750×** | -3.7 | 0.005 | 19/43 (MIA PaCa-2, HOP62, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.772×** | -3.5 | 0.012 | 19/43 (SW480, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.751×** | -3.1 | 0.046 | 18/42 (CFPAC-1, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.802×** | -3.0 | 0.062 | 19/43 (SW480, CFPAC-1, …) | rises with dose |  |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | 0.860× | -2.9 | 0.085 | 14/44 (SK-MEL-2, COLO 205, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.744×** | -2.9 | 0.088 | 13/43 (RKO, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.670×** | -2.8 | 0.091 | 13/43 (NCI-H1792, RKO, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.61 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8604. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 99.2 | 0 | 20 (14 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.107× (z -21.5) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.177× (z -16.7) |
| [[NCI-H460 (line)]] | wt | 80.4 | 0 | 19 (13 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -23.2) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.183× (z -15.6) |
| [[CFPAC-1 (line)]] | alt | 125 | 0 | 15 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0428× (z -32.8) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.249× (z -10.2) |
| [[LOX-IMVI (line)]] | wt | 131 | 0 | 14 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.136× (z -20.5) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.175× (z -12.7) |
| [[H4 (line)]] | wt | 155 | 0 | 13 (11 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0884× (z -18.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.122× (z -15.7) |
| [[HepG2_C3A (line)]] | wt | 197 | 0 | 13 (8 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0828× (z -20.4) ⚠ toxic · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.217× (z -13.0) |
| [[NCI-H1573 (line)]] | alt | 124 | 0 | 11 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.138× (z -24.6) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.261× (z -11.8) |
| [[RKO (line)]] | wt | 110 | 0 | 11 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0524× (z -34.0) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.188× (z -13.6) |
| [[SHP-77 (line)]] | alt | 127 | 4 | 7 (5 ⚠) | [[Clobetasol propionate (drug)]] 0.5 µM 2.75× (z +9.8) | [[Digitoxin (drug)]] 5 µM 0.0768× (z -24.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.243× (z -13.6) |
| [[SNU-423 (line)]] | alt | 146 | 0 | 11 (9 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.185× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.295× (z -10.6) |
| [[NCI-H1792 (line)]] | alt | 81.2 | 0 | 10 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.212× (z -18.0) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.263× (z -11.0) |
| [[COLO 205 (line)]] | alt | 127 | 0 | 9 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0972× (z -29.0) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.136× (z -9.2) |
| [[HOP62 (line)]] | alt | 40.7 | 2 | 6 (5 ⚠) | [[Auranofin (drug)]] 5 µM 5.74× (z +14.2) | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -13.7) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.229× (z -11.9) |
| [[SW 900 (line)]] | alt | 111 | 1 | 7 (6 ⚠) | [[Auranofin (drug)]] 5 µM 3.00× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.0415× (z -24.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.108× (z -9.4) |
| [[A498 (line)]] | wt | 62.6 | 0 | 6 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.117× (z -23.9) ⚠ cell-cycle shift, explains ~46% of this change |
| [[C32 (line)]] | wt | 67.2 | 3 | 3 (2 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 5.31× (z +11.6) | [[Dinaciclib (drug)]] 0.05 µM 0.166× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[PH-797804 (drug)]] 5 µM 0.0816× (z -9.5) |
| [[J82 (line)]] | alt | 79.5 | 0 | 6 (6 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.170× (z -14.6) ⚠ cell-cycle shift, explains ~31% of this change |
| [[Panc 03.27 (line)]] | alt | 62.6 | 0 | 6 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.142× (z -20.6) ⚠ cell-cycle shift, explains ~46% of this change |
| [[RPMI-7951 (line)]] | alt | 96.5 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.115× (z -15.6) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 166 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0833× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.0477× (z -9.4) |
| [[HCT15 (line)]] | alt | 115 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0816× (z -16.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.171× (z -12.1) |
| [[Hs 766T (line)]] | wt | 51.1 | 0 | 5 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.209× (z -11.0) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 27.6 | 5 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.64× (z +15.5) | — |
| [[A-172 (line)]] | wt | 79.0 | 2 | 2 (2 ⚠) | [[Auranofin (drug)]] 5 µM 4.48× (z +14.2) | [[Dinaciclib (drug)]] 0.05 µM 0.253× (z -11.9) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 28.9 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.79× (z +16.1) | — |
| [[A549 (line)]] | wt | 29.7 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -15.7) ⚠ cell-cycle shift, explains ~46% of this change |
| [[HEC-1-A (line)]] | alt | 25.1 | 3 | 0 | [[Epirubicin (hydrochloride) (drug)]] 5 µM 5.53× (z +10.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 25.4 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.76× (z +13.1) | — |
| [[A-427 (line)]] | wt | 30.6 | 1 (1 ⚠) | 1 (1 ⚠) | [[Selinexor (drug)]] 5 µM 2.85× (z +10.9) ⚠ cell-cycle shift, explains ~83% of this change | [[Homoharringtonine (drug)]] 5 µM 0.385× (z -10.0) ⚠ cell-cycle shift, explains ~46% of this change |
| [[BT-474 (line)]] | alt | 32.2 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -11.3) ⚠ cell-cycle shift, explains ~46% of this change |
| [[C-33 A (line)]] | alt | 44.4 | 1 | 1 (1 ⚠) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 3.95× (z +8.5) | [[Dinaciclib (drug)]] 0.05 µM 0.235× (z -8.6) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 102 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.108× (z -15.7) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 19.1 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.40× (z +10.6) | [[Lonafarnib (drug)]] 5 µM 0.0634× (z -9.0) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 94.3 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.90× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.262× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[SW1417 (line)]] | alt | 28.9 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -14.6) ⚠ cell-cycle shift, explains ~46% of this change |
| [[LoVo (line)]] | wt | 42.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.30× (z +8.8) | — |
| [[LS 180 (line)]] | wt | 39.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.144× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[SNU-1 (line)]] | wt | 51.7 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.139× (z -11.6) ⚠ cell-cycle shift, explains ~31% of this change |
| [[SW48 (line)]] | wt | 18.8 | 0 | 1 | — | [[Imiquimod (maleate) (drug)]] 5 µM 0.0717× (z -10.4) |
| [[AN3 CA (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.11 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 15.1 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 13.0 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 14.7 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 75.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 80.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 14.2 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 58.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 44.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8604), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01950]] | +0.55 | +0.30 / +0.60 | both halves | 2e-04 |  |
| [[UBA6-DT]] | +0.52 | +0.36 / +0.58 | both halves | 1e-04 |  |
| [[BCO2]] | +0.50 | +0.38 / +0.49 | both halves | 7e-05 |  |
| [[LINC00640]] | +0.48 | +0.34 / +0.50 | both halves | 1e-04 |  |
| [[CD27-AS1]] | +0.48 | +0.45 / +0.44 | both halves | 3e-05 |  |
| [[DLG2]] | +0.47 | +0.32 / +0.56 | both halves | 2e-04 |  |
| [[LINC01579]] | +0.47 | +0.29 / +0.46 | both halves | 2e-04 |  |
| [[IQCJ]] | +0.47 | +0.36 / +0.50 | both halves | 9e-05 |  |
| [[PXDNL]] | +0.47 | +0.47 / +0.42 | both halves | 4e-05 |  |
| [[PKIA-AS1]] | +0.47 | +0.33 / +0.49 | both halves | 1e-04 |  |
| [[ADAMTS9-AS2]] | +0.47 | +0.35 / +0.46 | both halves | 1e-04 |  |
| [[CLVS1]] | +0.46 | +0.38 / +0.43 | both halves | 6e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TADA2A]] | -0.46 | -0.35 / -0.61 | both halves | 1e-04 |  |
| [[BSN]] | -0.46 | -0.26 / -0.46 | both halves | 4e-04 |  |
| [[FAHD2CP]] | -0.45 | -0.22 / -0.47 | both halves | 6e-04 |  |
| [[ENTPD5]] | -0.44 | -0.19 / -0.45 | ⚠ not reproduced | 8e-04 |  |
| [[YWHAH]] | -0.44 | -0.32 / -0.47 | both halves | 2e-04 |  |
| [[DAGLA]] | -0.44 | -0.43 / -0.35 | both halves | 1e-04 |  |
| [[ZNF18]] | -0.44 | -0.34 / -0.38 | both halves | 1e-04 |  |
| [[PAOX]] | -0.43 | -0.40 / -0.36 | both halves | 9e-05 |  |
| [[ZNF624]] | -0.42 | -0.28 / -0.49 | both halves | 3e-04 |  |
| [[DNAJC16]] | -0.42 | -0.23 / -0.45 | both halves | 6e-04 |  |
| [[RAPGEF1]] | -0.40 | -0.42 / -0.40 | both halves | 5e-05 |  |
| [[DCAF17]] | -0.40 | -0.20 / -0.47 | ⚠ not reproduced | 8e-04 |  |
| [[ULK2]] | -0.40 | -0.33 / -0.41 | both halves | 1e-04 |  |
| [[ZNF592]] | -0.40 | -0.32 / -0.46 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CASC20]] | B | CASC20 activity raises DISC1's level | lines that do not express CASC20 (20) vs lines expressing it (30) | 2.44× lower at baseline in the lines without CASC20 | 0.004 | ⚠ within organs, on part of the lines; also absent: PPFIA2, IL19, ENPP2; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers DISC1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.2% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[LY96]] | B | LY96 activity raises DISC1's level | lines that do not express LY96 (18) vs lines expressing it (32) | 1.92× lower at baseline in the lines without LY96 | 0.083 | ⚠ within organs, on part of the lines; also absent: SOX5, ENSG00000287100, ENSG00000287622; maybe low, not absent |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RAPGEF4]] | B | DISC1 activity raises RAPGEF4's level | lines that do not express DISC1 (5) vs lines expressing it (45) | 2.49× lower at baseline in the lines without DISC1 | 0.086 | ⚠ within organs, on part of the lines; also absent: DCP1B, LINC01341, ENSG00000237356; maybe low, not absent |
| [[RPL34-DT]] | B | DISC1 activity raises RPL34-DT's level | lines that do not express DISC1 (5) vs lines expressing it (45) | 2.28× lower at baseline in the lines without DISC1 | 0.095 | ⚠ within organs, on part of the lines; also absent: DCP1B, LINC01341, ENSG00000237356; maybe low, not absent |

## Where it sits

- **Module**: [[Module 037]]; 123 genes; every member is in the + arm (projection on the module's main direction 0.441). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (23.4, -17.1); signed map (20.7, 1.2). **Vector** length 101, 30.0% of its response variance represented; |z| ≥ 3 in 1,359 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +11.2 | +7.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.9 | +9.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +8.1 | +7.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +6.3 | +5.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.6 | +2.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.0 | +4.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.1 | -3.0 |
|  | [[Belzutifan (drug)]] 5 µM |  | +1.9 | +0.2 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -6.7 | -4.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -5.7 | -12.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.9 | -1.3 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | -0.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.1 | -2.3 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -3.0 | -1.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.0 | -2.7 |
|  | [[Neratinib (drug)]] 5 µM |  | -2.6 | -1.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.6 | +0.5 |

## What is on record

|  |  |
|---|---|
| Name | DISC1 scaffold protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q42.2 — chr1:231,626,790-232,041,272 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Centriolar satellite proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NRI5](https://www.uniprot.org/uniprotkb/Q9NRI5) (Disrupted in schizophrenia 1 protein):

> Involved in the regulation of multiple aspects of embryonic and adult neurogenesis. Required for neural progenitor proliferation in the ventrical/subventrical zone during embryonic brain development and in the adult dentate gyrus of the hippocampus (By similarity). Participates in the Wnt-mediated neural progenitor proliferation as a positive regulator by modulating GSK3B activity and CTNNB1 abundance. Plays a role as a modulator of the AKT-mTOR signaling pathway controlling the tempo of the …

**Summary**, from NCBI Gene [27185](https://www.ncbi.nlm.nih.gov/gene/27185):

> This gene encodes a protein with multiple coiled coil motifs which is located in the nucleus, cytoplasm and mitochondria. The protein is involved in neurite outgrowth and cortical development through its interaction with other proteins. This gene is disrupted in a t(1;11)(q42.1;q14.3) translocation which segregates with schizophrenia and related psychiatric disorders in a large Scottish family. Alternate transcriptional splice variants, encoding different isoforms, have been characterized. …

**Accessions** — [HGNC:2888](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2888) · Entrez [27185](https://www.ncbi.nlm.nih.gov/gene/27185) · UniProt [Q9NRI5](https://www.uniprot.org/uniprotkb/Q9NRI5) · Ensembl [ENSG00000162946](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162946)

## Data

Gene col 8604: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8604); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8604, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8604]; `tensor/DDL_lfc|DDL_z.npy` [8604]; `embed/gene_vectors.npy` [8604]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8604 or target_col == 8604). Every well: [[DISC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DISC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
