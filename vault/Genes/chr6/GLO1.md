---
symbol: "GLO1"
type: "gene"
col: 4565
ensembl_id: "ENSG00000124767"
name: "glyoxalase I"
location: "6p21.2"
module: 4
arm: "+"
pooled_cpm: 81.36
n_lines_expressing: 50
n_dd_up: 31
n_dd_down: 0
n_dd_up_clean: 13
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# GLO1

*glyoxalase I* — 6p21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (18 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.83× (z +23.5, q 0e+00, up in 47 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.39× (z +8.2, q 3e-14, up in 35 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (C-33 A 0.433×, NCI-H23 0.538×, A-427 0.545×, HCT15 0.447×; ⚠ cell-cycle shift, explains ~0% of this change); [[Adagrasib (drug)]] 0.05 µM in 2 lines (MIA PaCa-2 0.757×, NCI-H23 0.785×; ⚠ position not correctable); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (SNU-1 0.237×; ⚠ cell-cycle shift, explains ~21% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCT5]] (+0.67, fdr 8e-06), [[CCT2]] (+0.65, fdr 7e-06), [[NAE1]] (+0.65, fdr 7e-06); moves opposite to [[MIB2]] (-0.64, fdr 7e-06), [[UPF2]] (-0.63, fdr 9e-06), [[CWC25]] (-0.63, fdr 1e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[STON2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 21 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4565.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **3.83×** | +23.5 | 0e+00 | 47/49 (SNU-423, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **3.53×** | +21.2 | 0e+00 | 43/43 (PANC-1, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **2.51×** | +14.9 | 0e+00 | 42/45 (SNU-423, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.83×** | +10.5 | 1e-23 | 45/48 (COLO 205, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.65×** | +8.8 | 2e-16 | 42/48 (SW480, HT-29, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.39×** | +8.2 | 3e-14 | 35/48 (J82, SK-MEL-2, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.58×** | +8.0 | 1e-13 | 41/48 (A549, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.37×** | +7.8 | 4e-13 | 41/48 (SW480, RKO, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.52×** | +7.0 | 1e-10 | 40/47 (CFPAC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **1.49×** | +7.0 | 1e-10 | 37/48 (LOX-IMVI, HepG2/C3A, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.46×** | +6.6 | 2e-09 | 34/48 (LOX-IMVI, NCI-H23, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.43×** | +6.3 | 1e-08 | 36/48 (A549, CFPAC-1, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.42×** | +6.1 | 4e-08 | 36/48 (MIA PaCa-2, LOX-IMVI, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.40×** | +5.9 | 1e-07 | 30/48 (LOX-IMVI, NCI-H23, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.35×** | +5.2 | 6e-06 | 34/48 (SW480, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.37×** | +4.3 | 4e-04 | 26/48 (A549, J82, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.25×** | +3.9 | 0.002 | 25/47 (NCI-H23, MIA PaCa-2, …) | all doses, flat |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.21×** | +3.3 | 0.018 | 16/48 (BT-474, CFPAC-1, …) | all doses, flat |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.37×** | +3.3 | 0.021 | 12/48 (NCI-H460, BT-474, …) | all doses, flat | low cells (technical?); noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.39×** | +3.0 | 0.050 | 14/48 (NCI-H460, SK-MEL-2, …) | top dose only | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.37×** | +2.9 | 0.063 | 10/49 (COLO 205, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | 1.19× | +2.9 | 0.066 | 18/48 (MIA PaCa-2, NCI-H23, …) | top dose only |  |
| [[Peretinoin (drug)]] 5 µM |  | 1.18× | +2.8 | 0.069 | 16/47 (NCI-H23, NCI-H460, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 2 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4565.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (C-33 A 0.433×, NCI-H23 0.538×, A-427 0.545×, HCT15 0.447×; ⚠ cell-cycle shift, explains ~0% of this change); [[Adagrasib (drug)]] 0.05 µM in 2 lines (MIA PaCa-2 0.757×, NCI-H23 0.785×; ⚠ position not correctable); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (SNU-1 0.237×; ⚠ cell-cycle shift, explains ~21% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.882× | -7.1 | 7e-10 | 10/49 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | 0.795× | -3.5 | 0.15 | 21/50 (Hs 766T, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.39 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4565. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 93.6 | 5 (5 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.00× (z +11.1) ⚠ cell-cycle shift, explains ~84% of this change | — |
| [[SNU-423 (line)]] | alt | 119 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.24× (z +17.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[SW480 (line)]] | alt | 57.1 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.37× (z +13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 1.90× (z +10.4) | — |
| [[CFPAC-1 (line)]] | alt | 69.2 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.98× (z +12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[COLO 205 (line)]] | alt | 154 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +11.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[HT-29 (line)]] | alt | 50.6 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.08× (z +14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[J82 (line)]] | alt | 95.2 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.91× (z +12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Selinexor (drug)]] 5 µM 1.90× (z +10.9) | — |
| [[LOX-IMVI (line)]] | wt | 108 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.56× (z +16.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 178 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.60× (z +15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.08× (z +8.8) | — |
| [[A-172 (line)]] | wt | 68.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.83× (z +13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[A498 (line)]] | wt | 42.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.06× (z +14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[A549 (line)]] | wt | 50.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.15× (z +15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[AsPC-1 (line)]] | alt | 27.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.06× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[H4 (line)]] | wt | 66.6 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.12× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.352× (z -9.7) ⚠ cell-cycle shift, explains ~84% of this change |
| [[HCT15 (line)]] | alt | 101 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.55× (z +13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | [[Homoharringtonine (drug)]] 5 µM 0.447× (z -9.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 77.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.49× (z +14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[Hs 766T (line)]] | wt | 29.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.64× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[HS-578T (line)]] | alt | 53.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.41× (z +14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[LoVo (line)]] | wt | 57.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.42× (z +15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[LS 180 (line)]] | wt | 65.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.44× (z +12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[NCI-H1792 (line)]] | alt | 48.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.29× (z +14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[NCI-H2030 (line)]] | alt | 77.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.30× (z +13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[Panc 03.27 (line)]] | alt | 116 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.78× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[PANC-1 (line)]] | alt | 99.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.45× (z +17.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 108 | 3 (2 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 1.97× (z +10.5) | — |
| [[A-427 (line)]] | wt | 126 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.56× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | [[Homoharringtonine (drug)]] 5 µM 0.545× (z -10.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 47.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.78× (z +13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[HEC-1-A (line)]] | alt | 104 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.42× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Selinexor (drug)]] 5 µM 1.70× (z +8.7) | — |
| [[KATO III (line)]] | alt | 82.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.44× (z +13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[NCI-H1573 (line)]] | alt | 24.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.40× (z +13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[NCI-H460 (line)]] | wt | 63.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.34× (z +16.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[SW 900 (line)]] | alt | 34.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.45× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[C-33 A (line)]] | alt | 140 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.433× (z -12.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HepG2_C3A (line)]] | wt | 55.1 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.18× (z +9.1) ⚠ cell-cycle shift, explains ~41% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 36.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.65× (z +12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[NCI-H23 (line)]] | alt | 269 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.538× (z -11.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 116 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 1.74× (z +8.9) | — |
| [[RPMI-7951 (line)]] | alt | 42.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.32× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[SNU-1 (line)]] | wt | 98.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.237× (z -12.6) ⚠ cell-cycle shift, explains ~21% of this change |
| [[SW1417 (line)]] | alt | 56.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.88× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[AN3 CA (line)]] | alt | 124 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 138 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 64.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 50.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 67.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 209 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 63.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 51.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 82.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 115 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4565), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*53 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCT5]] | +0.67 | +0.78 / +0.57 | both halves | 8e-06 | pathway: HALLMARK_MYC_TARGETS_V1; STRING 411 |
| [[CCT2]] | +0.65 | +0.67 / +0.62 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1 |
| [[NAE1]] | +0.65 | +0.67 / +0.58 | both halves | 7e-06 |  |
| [[SACS]] | +0.64 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[YWHAQ]] | +0.64 | +0.51 / +0.63 | both halves | 1e-05 | pathway: HALLMARK_MYC_TARGETS_V1 |
| [[G3BP1]] | +0.63 | +0.61 / +0.59 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1 |
| [[CCT3]] | +0.63 | +0.71 / +0.52 | both halves | 1e-05 | pathway: HALLMARK_MYC_TARGETS_V1 |
| [[PRPS1]] | +0.61 | +0.65 / +0.51 | both halves | 1e-05 |  |
| [[RPE]] | +0.60 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[ZDHHC21]] | +0.60 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[CCT8]] | +0.59 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[CCT4]] | +0.59 | +0.66 / +0.54 | both halves | 1e-05 | pathway: HALLMARK_MYC_TARGETS_V1 |

## Genes that move opposite

*47 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MIB2]] | -0.64 | -0.61 / -0.63 | both halves | 7e-06 |  |
| [[UPF2]] | -0.63 | -0.57 / -0.65 | both halves | 9e-06 |  |
| [[CWC25]] | -0.63 | -0.49 / -0.65 | both halves | 1e-05 |  |
| [[TERF2IP]] | -0.63 | -0.59 / -0.55 | both halves | 1e-05 |  |
| [[INAFM1]] | -0.62 | -0.62 / -0.62 | both halves | 7e-06 |  |
| [[TPRN]] | -0.60 | -0.43 / -0.57 | both halves | 3e-05 |  |
| [[CHKB]] | -0.60 | -0.47 / -0.58 | both halves | 2e-05 |  |
| [[SNHG9]] | -0.60 | -0.58 / -0.54 | both halves | 1e-05 |  |
| [[TMEM258]] | -0.60 | -0.56 / -0.64 | both halves | 1e-05 |  |
| [[ZMYM5]] | -0.60 | -0.49 / -0.54 | both halves | 1e-05 |  |
| [[PDCD7]] | -0.59 | -0.32 / -0.59 | both halves | 1e-04 |  |
| [[ZNF324]] | -0.58 | -0.37 / -0.65 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STON2]] | B | STON2 activity lowers GLO1's level | lines that do not express STON2 (19) vs lines expressing it (31) | 1.50× higher at baseline in the lines without STON2 | 0.038 | ⚠ within organs, on part of the lines; also absent: FRK, RASSF6, AQP3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.581). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-23.1, -32.5); signed map (-12.4, -44.9). **Vector** length 91.6, 28.0% of its response variance represented; |z| ≥ 3 in 1,067 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Folding of actin by CCT/TriC* (reactome, mean cos +0.63 to 4); *Prefoldin mediated transfer of substrate  to CCT/TriC* (reactome, mean cos +0.52 to 5); *Cooperation of Prefoldin and TriC/CCT  in actin and tubulin folding* (reactome, mean cos +0.52 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.6 | +7.8 |
|  | [[Selinexor (drug)]] 5 µM |  | +6.7 | +8.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.6 | +5.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +4.2 | +8.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | +4.1 | +21.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.5 | +6.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.4 | +2.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.3 | +1.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.1 | +6.6 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.0 | -0.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~84% of this change | -4.1 | +2.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.0 | -1.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | +1.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.5 | +2.1 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -2.3 | -0.2 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | -2.1 | -2.7 |
|  | [[PH-797804 (drug)]] 0.5 µM |  | -2.0 | -0.7 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | -1.9 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | glyoxalase I |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.2 — chr6:38,675,925-38,703,145 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GLOD1 |
| Gene groups (HGNC) | Glyoxalase domain containing |
| Hallmark sets | MYC_TARGETS_V1 |
| Reactome | 2 pathways, smallest: Pyruvate metabolism; Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q04760](https://www.uniprot.org/uniprotkb/Q04760) (Lactoylglutathione lyase):

> Catalyzes the conversion of hemimercaptal, formed from methylglyoxal and glutathione, to S-lactoylglutathione. Involved in the regulation of TNF-induced transcriptional activity of NF-kappa-B. Required for normal osteoclastogenesis (By similarity).

**Summary**, from NCBI Gene [2739](https://www.ncbi.nlm.nih.gov/gene/2739):

> The enzyme encoded by this gene is responsible for the catalysis and formation of S-lactoyl-glutathione from methylglyoxal condensation and reduced glutatione. Glyoxalase I is linked to HLA and is localized to 6p21.3-p21.1, between HLA and the centromere. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:4323](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4323) · Entrez [2739](https://www.ncbi.nlm.nih.gov/gene/2739) · UniProt [Q04760](https://www.uniprot.org/uniprotkb/Q04760) · Ensembl [ENSG00000124767](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000124767)

## Data

Gene col 4565: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4565); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4565, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4565]; `tensor/DDL_lfc|DDL_z.npy` [4565]; `embed/gene_vectors.npy` [4565]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4565 or target_col == 4565). Every well: [[GLO1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GLO1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
