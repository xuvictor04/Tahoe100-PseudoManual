---
symbol: "RBM39"
type: "gene"
col: 5163
ensembl_id: "ENSG00000131051"
name: "RNA binding motif protein 39"
location: "20q11.22"
module: 23
arm: "+"
pooled_cpm: 588.67
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 10
n_dd_up_clean: 12
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# RBM39

*RNA binding motif protein 39* — 20q11.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.60× (z +24.1, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.385× (z -17.0, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CUTALP]] (+0.68, fdr 1e-05), [[BCLAF1]] (+0.68, fdr 7e-06), [[RSRC2]] (+0.68, fdr 2e-05); moves opposite to [[AP3M2]] (-0.60, fdr 2e-05), [[ZBED4]] (-0.58, fdr 3e-05), [[GNA12]] (-0.58, fdr 7e-05).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ECHDC2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 4 with an alert ⚠; shown: the 15 strongest. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5163.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.60×** | +24.1 | 0e+00 | 48/48 (COLO 205, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.59×** | +16.9 | 0e+00 | 47/48 (SW480, A498, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.80×** | +12.5 | 2e-33 | 48/49 (LoVo, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.98×** | +12.2 | 4e-32 | 48/48 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.95×** | +11.9 | 2e-30 | 48/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **3.22×** | +10.9 | 1e-25 | 47/48 (SW480, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.75×** | +9.6 | 5e-20 | 42/48 (COLO 205, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.66×** | +9.1 | 8e-18 | 46/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.56×** | +7.9 | 2e-13 | 43/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.36×** | +5.4 | 4e-06 | 29/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.34×** | +5.2 | 1e-05 | 35/48 (MIA PaCa-2, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.32×** | +4.7 | 1e-04 | 33/47 (COLO 205, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~10% of this change | **1.25×** | +4.0 | 0.002 | 24/48 (NCI-H460, NCI-H1573, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.25×** | +4.0 | 0.003 | 30/48 (HT-29, SW480, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.43×** | +3.4 | 0.029 | 33/49 (HT-29, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5163.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.385×** | -17.0 | 0e+00 | 48/48 (CFPAC-1, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.410×** | -15.9 | 0e+00 | 48/48 (COLO 205, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.427×** | -15.2 | 0e+00 | 48/48 (CFPAC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.508×** | -11.8 | 5e-30 | 48/48 (COLO 205, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.605×** | -9.0 | 3e-17 | 47/48 (CFPAC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.481×** | -6.8 | 8e-10 | 46/49 (CFPAC-1, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.703×** | -6.1 | 1e-07 | 34/44 (SNU-1, NCI-H1792, …) | rises with dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.807×** | -5.4 | 4e-06 | 25/49 (A549, NCI-H23, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~57% of this change | **0.808×** | -3.7 | 0.016 | 31/47 (NCI-H2347, LoVo, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.876× | -3.3 | 0.048 | 16/48 (HT-29, SW 900, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | 0.835× | -3.2 | 0.070 | 23/49 (NCI-H2347, CFPAC-1, …) | rises with dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.831×** | -3.2 | 0.071 | 25/48 (NCI-H460, COLO 205, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.841× | -3.1 | 0.090 | 18/48 (CFPAC-1, A549, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.28 per unit of S-phase module lfc, +0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5163. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 564 | 12 (3 ⚠) | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +19.6) | [[Panobinostat (drug)]] 5 µM 0.376× (z -13.3) |
| [[NCI-H1573 (line)]] | alt | 579 | 10 (2 ⚠) | 5 | [[Homoharringtonine (drug)]] 5 µM 3.71× (z +25.9) | [[Belinostat (drug)]] 5 µM 0.286× (z -17.5) |
| [[SW480 (line)]] | alt | 630 | 10 (1 ⚠) | 5 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +24.3) | [[Belinostat (drug)]] 5 µM 0.439× (z -15.3) |
| [[LoVo (line)]] | wt | 469 | 9 (2 ⚠) | 5 | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +26.2) | [[Belinostat (drug)]] 5 µM 0.378× (z -18.1) |
| [[BT-474 (line)]] | alt | 485 | 9 (1 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 3.23× (z +24.5) | [[Panobinostat (drug)]] 0.5 µM 0.483× (z -10.7) |
| [[COLO 205 (line)]] | alt | 721 | 8 (2 ⚠) | 5 | [[Homoharringtonine (drug)]] 5 µM 4.26× (z +30.6) | [[Belinostat (drug)]] 5 µM 0.284× (z -18.8) |
| [[LOX-IMVI (line)]] | wt | 603 | 8 (1 ⚠) | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +17.6) | [[Panobinostat (drug)]] 5 µM 0.360× (z -14.3) |
| [[AsPC-1 (line)]] | alt | 707 | 7 (2 ⚠) | 5 | [[Homoharringtonine (drug)]] 5 µM 3.61× (z +25.3) | [[Panobinostat (drug)]] 5 µM 0.348× (z -14.8) |
| [[NCI-H1792 (line)]] | alt | 1,120 | 5 (1 ⚠) | 7 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +15.9) | [[Panobinostat (drug)]] 0.5 µM 0.292× (z -15.7) |
| [[NCI-H2347 (line)]] | alt | 703 | 3 (1 ⚠) | 9 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.65× (z +11.8) | [[Panobinostat (drug)]] 5 µM 0.369× (z -16.7) |
| [[PANC-1 (line)]] | alt | 445 | 7 (1 ⚠) | 5 | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +15.9) | [[Belinostat (drug)]] 5 µM 0.339× (z -17.7) |
| [[Panc 03.27 (line)]] | alt | 758 | 6 | 5 | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +20.6) | [[Panobinostat (drug)]] 5 µM 0.319× (z -16.5) |
| [[HCT15 (line)]] | alt | 706 | 4 | 6 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +17.8) | [[Panobinostat (drug)]] 5 µM 0.309× (z -17.7) |
| [[HEC-1-A (line)]] | alt | 388 | 6 | 4 | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +22.1) | [[Panobinostat (drug)]] 5 µM 0.460× (z -11.9) |
| [[HT-29 (line)]] | alt | 616 | 6 (1 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +22.4) | [[Belinostat (drug)]] 5 µM 0.385× (z -16.0) |
| [[KATO III (line)]] | alt | 632 | 7 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +20.0) | [[Belinostat (drug)]] 5 µM 0.380× (z -13.1) |
| [[NCI-H23 (line)]] | alt | 773 | 6 (1 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +20.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.528× (z -13.5) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.435× (z -12.4) |
| [[SW 900 (line)]] | alt | 622 | 5 (1 ⚠) | 5 | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +14.7) | [[Panobinostat (drug)]] 5 µM 0.300× (z -15.8) |
| [[A-172 (line)]] | wt | 322 | 5 | 4 | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +18.3) | [[Panobinostat (drug)]] 5 µM 0.445× (z -13.5) |
| [[MIA PaCa-2 (line)]] | alt | 522 | 6 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +18.0) | [[Belinostat (drug)]] 5 µM 0.453× (z -10.3) |
| [[SK-MEL-2 (line)]] | alt | 419 | 5 | 4 | [[Homoharringtonine (drug)]] 5 µM 3.78× (z +27.0) | [[Belinostat (drug)]] 5 µM 0.411× (z -12.8) |
| [[A498 (line)]] | wt | 501 | 3 | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.92× (z +26.3) | [[Panobinostat (drug)]] 0.5 µM 0.339× (z -14.8) |
| [[A549 (line)]] | wt | 410 | 3 | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +21.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.477× (z -14.9) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.377× (z -13.8) |
| [[CFPAC-1 (line)]] | alt | 747 | 1 | 7 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +14.3) | [[Panobinostat (drug)]] 0.5 µM 0.241× (z -19.6) |
| [[hTERT-HPNE (line)]] | wt | 378 | 4 | 4 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +17.6) | [[Panobinostat (drug)]] 5 µM 0.346× (z -13.8) |
| [[NCI-H2030 (line)]] | alt | 822 | 4 (1 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +13.1) | [[Panobinostat (drug)]] 5 µM 0.331× (z -10.3) |
| [[RKO (line)]] | wt | 557 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +23.5) | — |
| [[RPMI-7951 (line)]] | alt | 694 | 4 | 4 | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +19.2) | [[Panobinostat (drug)]] 5 µM 0.381× (z -13.8) |
| [[SW1417 (line)]] | alt | 934 | 4 (1 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +17.5) | [[Panobinostat (drug)]] 5 µM 0.428× (z -11.6) |
| [[A-427 (line)]] | wt | 498 | 4 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +17.0) | [[Belinostat (drug)]] 5 µM 0.432× (z -13.6) |
| [[C-33 A (line)]] | alt | 384 | 4 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +11.2) | [[Belinostat (drug)]] 5 µM 0.463× (z -10.4) |
| [[HepG2_C3A (line)]] | wt | 913 | 3 (1 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +15.4) | [[Panobinostat (drug)]] 5 µM 0.301× (z -16.6) |
| [[HOP62 (line)]] | alt | 513 | 3 | 4 | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +17.8) | [[Panobinostat (drug)]] 5 µM 0.320× (z -13.3) |
| [[Hs 766T (line)]] | wt | 942 | 4 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +18.8) | [[Panobinostat (drug)]] 5 µM 0.449× (z -10.9) |
| [[SNU-1 (line)]] | wt | 733 | 4 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +16.1) | [[Dinaciclib (drug)]] 5 µM 0.199× (z -19.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.426× (z -10.6) |
| [[SW48 (line)]] | wt | 473 | 5 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +16.6) | [[Belinostat (drug)]] 5 µM 0.380× (z -10.6) |
| [[H4 (line)]] | wt | 435 | 2 | 4 | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +17.9) | [[Panobinostat (drug)]] 5 µM 0.359× (z -12.3) |
| [[J82 (line)]] | alt | 631 | 3 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +16.3) | [[Panobinostat (drug)]] 5 µM 0.469× (z -10.6) |
| [[LS 180 (line)]] | wt | 501 | 5 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +13.0) | [[Panobinostat (drug)]] 0.5 µM 0.437× (z -9.1) |
| [[C32 (line)]] | wt | 347 | 2 | 3 | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +16.4) | [[Panobinostat (drug)]] 5 µM 0.319× (z -10.8) |
| [[CHP-212 (line)]] | wt | 456 | 1 | 4 | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +9.6) | [[Panobinostat (drug)]] 5 µM 0.333× (z -12.6) |
| [[SNU-423 (line)]] | alt | 640 | 1 | 4 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +14.0) | [[Belinostat (drug)]] 5 µM 0.408× (z -11.8) |
| [[HS-578T (line)]] | alt | 476 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +19.2) | [[Panobinostat (drug)]] 0.5 µM 0.495× (z -8.6) |
| [[SW 1271 (line)]] | alt | 985 | 2 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +12.8) | [[Panobinostat (drug)]] 5 µM 0.364× (z -9.9) |
| [[SHP-77 (line)]] | alt | 309 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.543× (z -9.0) |
| [[AN3 CA (line)]] | alt | 422 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +16.1) | — |
| [[NCI-H2122 (line)]] | alt | 609 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 630 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 601 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 554 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5163), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 4 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CUTALP]] | +0.68 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[BCLAF1]] | +0.68 | +0.63 / +0.62 | both halves | 7e-06 | STRING 750 |
| [[RSRC2]] | +0.68 | +0.78 / +0.47 | both halves | 2e-05 | STRING 613 |
| [[TRA2A]] | +0.66 | +0.67 / +0.59 | both halves | 7e-06 | same gene group; STRING 653 |
| [[HNRNPH1]] | +0.64 | +0.60 / +0.54 | both halves | 1e-05 | same gene group; pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 639 |
| [[RBM5]] | +0.61 | +0.65 / +0.45 | both halves | 3e-05 | same gene group; pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 955 |
| [[ING3]] | +0.61 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[PAN2]] | +0.60 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[SREK1]] | +0.60 | +0.60 / +0.49 | both halves | 1e-05 | same gene group; STRING 796 |
| [[YTHDC1]] | +0.59 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[LINC00174]] | +0.59 | +0.46 / +0.46 | both halves | 3e-05 |  |
| [[GABPB2]] | +0.59 | +0.43 / +0.36 | both halves | 1e-04 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AP3M2]] | -0.60 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[ZBED4]] | -0.58 | -0.43 / -0.56 | both halves | 3e-05 |  |
| [[GNA12]] | -0.58 | -0.38 / -0.55 | both halves | 7e-05 |  |
| [[LIMK1]] | -0.57 | -0.39 / -0.47 | both halves | 5e-05 |  |
| [[EXOC2]] | -0.55 | -0.43 / -0.51 | both halves | 3e-05 |  |
| [[TEX2]] | -0.55 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[USB1]] | -0.54 | -0.47 / -0.37 | both halves | 8e-05 |  |
| [[TPST2]] | -0.54 | -0.35 / -0.42 | both halves | 1e-04 |  |
| [[FXYD5]] | -0.53 | -0.43 / -0.38 | both halves | 6e-05 |  |
| [[PIP4K2A]] | -0.53 | -0.40 / -0.42 | both halves | 5e-05 |  |
| [[CPSF4]] | -0.52 | -0.39 / -0.41 | both halves | 5e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[TUBG1]] | -0.52 | -0.44 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ECHDC2]] | B | ECHDC2 activity raises RBM39's level | lines that do not express ECHDC2 (12) vs lines expressing it (38) | 1.32× lower at baseline in the lines without ECHDC2 | 0.015 | ⚠ within organs, on part of the lines; also absent: STXBP2, C10orf88B |
| [[HDAC6]] | B | HDAC6 activity raises RBM39's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.516). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (26.0, -30.1); signed map (6.4, -9.7). **Vector** length 96.4, 46.8% of its response variance represented; |z| ≥ 3 in 1,444 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.1 | +24.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.8 | +16.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | +5.3 | -3.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | +5.1 | -6.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.7 | -0.0 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +4.3 | -0.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | +4.0 | +0.6 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +3.5 | -1.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.4 | -0.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.2 | +1.3 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -8.2 | -9.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.4 | -0.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -5.3 | -11.8 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -5.2 | +9.1 |
|  | [[Belinostat (drug)]] 5 µM |  | -5.2 | -15.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.7 | -6.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.5 | -0.8 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -3.0 | -2.4 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -3.0 | +0.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.8 | +0.3 |

## What is on record

|  |  |
|---|---|
| Name | RNA binding motif protein 39 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q11.22 — chr20:35,701,347-35,742,312 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CC1.3, HCC1, CAPER, fSAP59, CAPERalpha; previously RNPC2 |
| Gene groups (HGNC) | RNA binding motif containing |
| Reactome | 6 pathways, smallest: mRNA Polyadenylation; mRNA 3'-end processing; mRNA Splicing - Major Pathway |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14498](https://www.uniprot.org/uniprotkb/Q14498) (RNA-binding protein 39):

> RNA-binding protein that acts as a pre-mRNA splicing factor. Acts by promoting exon inclusion via regulation of exon cassette splicing. Also acts as a transcriptional coactivator for steroid nuclear receptors ESR1/ER-alpha and ESR2/ER-beta, and JUN/AP-1, independently of the pre-mRNA splicing factor activity (By similarity).

**Summary**, from NCBI Gene [9584](https://www.ncbi.nlm.nih.gov/gene/9584):

> This gene encodes a member of the U2AF65 family of proteins. The encoded protein is found in the nucleus, where it co-localizes with core spliceosomal proteins. It has been shown to play a role in both steroid hormone receptor-mediated transcription and alternative splicing, and it is also a transcriptional coregulator of the viral oncoprotein v-Rel. Multiple transcript variants have been observed for this gene. A related pseudogene has been identified on chromosome X. [provided by RefSeq, Aug …

**Accessions** — [HGNC:15923](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15923) · Entrez [9584](https://www.ncbi.nlm.nih.gov/gene/9584) · UniProt [Q14498](https://www.uniprot.org/uniprotkb/Q14498) · Ensembl [ENSG00000131051](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000131051)

## Data

Gene col 5163: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5163); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5163, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5163]; `tensor/DDL_lfc|DDL_z.npy` [5163]; `embed/gene_vectors.npy` [5163]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5163 or target_col == 5163). Every well: [[RBM39 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RBM39.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
