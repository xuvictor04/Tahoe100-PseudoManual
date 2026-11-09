---
symbol: "HERC4"
type: "gene"
col: 7299
ensembl_id: "ENSG00000148634"
name: "HECT and RLD domain containing E3 ubiquitin protein ligase 4"
location: "10q21.3"
module: 37
arm: "+"
pooled_cpm: 453.74
n_lines_expressing: 49
n_dd_up: 10
n_dd_down: 9
n_dd_up_clean: 9
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/037"]
generated_by: "tahoemap"
---

# HERC4

*HECT and RLD domain containing E3 ubiquitin protein ligase 4* — 10q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.54× (z +9.9, q 3e-20, up in 38 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.454× (z -18.1, q 0e+00, down in 46 of 48 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (NCI-H1573 0.101×, A-427 0.198×, LoVo 0.303×, NCI-H23 0.271×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (NCI-H1573 0.228×, HEC-1-A 0.360×, PANC-1 0.391×, SNU-423 0.353×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (HEC-1-A 0.355×, SNU-423 0.327×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change); [[Ponatinib (drug)]] 5 µM in 2 lines (HepG2/C3A 0.330×, C32 0.448×); [[Belumosudil (drug)]] 0.05 µM in 1 line (SW 1088 0.232×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DCAF4L1]] (+0.66, fdr 1e-05), [[SNX31]] (+0.64, fdr 1e-05), [[CFAP53]] (+0.62, fdr 1e-05); moves opposite to [[PPP5C]] (-0.61, fdr 1e-05), [[SKP2]] (-0.58, fdr 1e-05), [[SAAL1]] (-0.57, fdr 1e-05).
> It is in [[Module 037]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[RNF103-CHMP3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7299.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.54×** | +9.9 | 3e-20 | 38/47 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.43×** | +8.2 | 5e-14 | 37/47 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.41×** | +7.5 | 1e-11 | 29/47 (C32, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.33×** | +6.5 | 1e-08 | 30/47 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.22×** | +6.4 | 2e-08 | 24/47 (SW1417, MIA PaCa-2, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.29×** | +5.8 | 6e-07 | 28/47 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.27×** | +5.4 | 5e-06 | 27/47 (HT-29, HEC-1-A, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.22×** | +4.3 | 0.001 | 24/49 (CFPAC-1, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.42×** | +4.2 | 0.002 | 34/48 (MIA PaCa-2, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~9% of this change | 1.20× | +4.1 | 0.003 | 23/47 (LoVo, NCI-H1573, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.13× | +3.9 | 0.005 | 13/48 (LS 180, NCI-H1573, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 0.05 µM |  | 1.18× | +3.6 | 0.016 | 14/48 (PANC-1, J82, …) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 1.16× | +3.5 | 0.024 | 20/47 (NCI-H1573, LS 180, …) | all doses, flat |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.33×** | +3.4 | 0.031 | 22/49 (A-427, A549, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-733 (drug)]] 0.05 µM |  | 1.15× | +3.0 | 0.091 | 8/47 (SNU-423, LoVo, …) | inconsistent across doses |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | 1.14× | +3.0 | 0.091 | 19/47 (NCI-H2347, A-172, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 15 with an alert ⚠; shown: the 15 strongest. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7299.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (NCI-H1573 0.101×, A-427 0.198×, LoVo 0.303×, NCI-H23 0.271×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (NCI-H1573 0.228×, HEC-1-A 0.360×, PANC-1 0.391×, SNU-423 0.353×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (HEC-1-A 0.355×, SNU-423 0.327×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change); [[Ponatinib (drug)]] 5 µM in 2 lines (HepG2/C3A 0.330×, C32 0.448×); [[Belumosudil (drug)]] 0.05 µM in 1 line (SW 1088 0.232×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.454×** | -18.1 | 0e+00 | 46/48 (NCI-H1573, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.480×** | -16.2 | 0e+00 | 43/43 (NCI-H1573, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.502×** | -14.6 | 0e+00 | 40/44 (HEC-1-A, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.622×** | -10.9 | 2e-25 | 38/47 (NCI-H23, A-427, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.681×** | -8.8 | 1e-16 | 34/47 (LOX-IMVI, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.696×** | -8.3 | 8e-15 | 35/47 (NCI-H23, A-427, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.728×** | -7.3 | 3e-11 | 40/47 (PANC-1, SW 900, …) | all doses, flat | low cells (technical?); cell-cycle shift (explains ~20% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~40% of this change | **0.753×** | -6.3 | 3e-08 | 31/46 (HepG2/C3A, HEC-1-A, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.819×** | -4.6 | 3e-04 | 26/47 (SW480, A-427, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | 0.872× | -4.5 | 4e-04 | 20/48 (A549, NCI-H1792, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~71% of this change | 0.856× | -3.6 | 0.018 | 21/47 (KATO III, MIA PaCa-2, …) | rises with dose |  |
| [[Trifluridine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | 0.858× | -3.5 | 0.020 | 13/47 (LOX-IMVI, HepG2/C3A, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~50% of this change | 0.859× | -3.5 | 0.021 | 20/47 (NCI-H23, A-427, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | 0.860× | -3.5 | 0.021 | 22/47 (Hs 766T, J82, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.861× | -3.5 | 0.021 | 18/47 (A549, SW480, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.38 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7299. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 785 | 8 (4 ⚠) | 6 (6 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.19× (z +20.0) | [[Dinaciclib (drug)]] 5 µM 0.101× (z -30.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[NCI-H460 (line)]] | wt | 866 | 9 (4 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.51× (z +15.7) | [[Dinaciclib (drug)]] 5 µM 0.266× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[PANC-1 (line)]] | alt | 647 | 4 (3 ⚠) | 7 (7 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.55× (z +11.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.74× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.372× (z -17.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[LoVo (line)]] | wt | 364 | 7 (4 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.40× (z +19.6) ⚠ cell-cycle shift, explains ~9% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.20× (z +12.6) | [[Dinaciclib (drug)]] 5 µM 0.303× (z -18.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[hTERT-HPNE (line)]] | wt | 691 | 3 | 6 (6 ⚠) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 3.49× (z +14.3) | [[Dinaciclib (drug)]] 5 µM 0.286× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[A-172 (line)]] | wt | 471 | 4 (1 ⚠) | 4 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.38× (z +13.3) | [[Dinaciclib (drug)]] 0.5 µM 0.396× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[A549 (line)]] | wt | 575 | 4 (1 ⚠) | 4 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.27× (z +12.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.284× (z -27.6) ⚠ cell-cycle shift, explains ~65% of this change |
| [[NCI-H1792 (line)]] | alt | 493 | 2 | 6 (6 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.59× (z +13.3) | [[Dinaciclib (drug)]] 0.5 µM 0.314× (z -16.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[A-427 (line)]] | wt | 657 | 0 | 7 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.198× (z -23.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[HEC-1-A (line)]] | alt | 408 | 1 | 6 (6 ⚠) | [[Auranofin (drug)]] 5 µM 1.62× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.360× (z -20.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[HOP62 (line)]] | alt | 429 | 3 | 4 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.71× (z +13.1) | [[Dinaciclib (drug)]] 0.5 µM 0.382× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[LOX-IMVI (line)]] | wt | 383 | 0 | 7 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.410× (z -14.3) ⚠ cell-cycle shift, explains ~53% of this change |
| [[SW48 (line)]] | wt | 385 | 6 (4 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.05 µM 3.20× (z +12.4) | [[Dinaciclib (drug)]] 0.5 µM 0.434× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[COLO 205 (line)]] | alt | 282 | 5 (4 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +12.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.56× (z +11.7) | [[Dinaciclib (drug)]] 0.5 µM 0.452× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[Hs 766T (line)]] | wt | 619 | 3 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.15× (z +9.8) | [[Dinaciclib (drug)]] 0.5 µM 0.350× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[MIA PaCa-2 (line)]] | alt | 403 | 5 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +14.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 1.89× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.474× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[NCI-H23 (line)]] | alt | 805 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.271× (z -17.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[AsPC-1 (line)]] | alt | 717 | 0 | 5 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.350× (z -11.7) ⚠ cell-cycle shift, explains ~53% of this change |
| [[HepG2_C3A (line)]] | wt | 393 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.295× (z -15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Ponatinib (drug)]] 5 µM 0.330× (z -15.0) |
| [[NCI-H2030 (line)]] | alt | 471 | 2 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.32× (z +12.2) | [[Panobinostat (drug)]] 5 µM 0.524× (z -9.4) ⚠ cell-cycle shift, explains ~53% of this change |
| [[SNU-423 (line)]] | alt | 550 | 1 (1 ⚠) | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.57× (z +10.2) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.320× (z -17.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[SW 900 (line)]] | alt | 505 | 1 | 4 (4 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.06× (z +10.3) | [[Dinaciclib (drug)]] 0.05 µM 0.380× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[SW480 (line)]] | alt | 402 | 1 | 4 (4 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 1.84× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.309× (z -16.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[C32 (line)]] | wt | 316 | 1 | 3 (2 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.09× (z +10.4) | [[Dinaciclib (drug)]] 0.5 µM 0.411× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Ponatinib (drug)]] 5 µM 0.448× (z -11.8) |
| [[HT-29 (line)]] | alt | 312 | 1 | 3 (3 ⚠) | [[Auranofin (drug)]] 5 µM 1.81× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.493× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[J82 (line)]] | alt | 302 | 0 | 4 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.422× (z -12.1) ⚠ cell-cycle shift, explains ~53% of this change |
| [[LS 180 (line)]] | wt | 358 | 2 | 2 (2 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 1.77× (z +11.5) | [[Dinaciclib (drug)]] 0.05 µM 0.460× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[Panc 03.27 (line)]] | alt | 566 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.408× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[SNU-1 (line)]] | wt | 287 | 3 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.35× (z +11.0) | [[Dinaciclib (drug)]] 0.5 µM 0.305× (z -15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[CHP-212 (line)]] | wt | 464 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.294× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[H4 (line)]] | wt | 454 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.381× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[HS-578T (line)]] | alt | 271 | 1 | 2 (2 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 1.73× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.529× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[SW1417 (line)]] | alt | 259 | 3 | 0 | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 1.69× (z +10.8) | — |
| [[A498 (line)]] | wt | 310 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 1.74× (z +8.5) | [[Dinaciclib (drug)]] 0.05 µM 0.528× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[C-33 A (line)]] | alt | 257 | 1 | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.01× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.397× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[CFPAC-1 (line)]] | alt | 324 | 2 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.21× (z +9.7) | — |
| [[KATO III (line)]] | alt | 265 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.377× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[RKO (line)]] | wt | 451 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.425× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[SK-MEL-2 (line)]] | alt | 310 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.356× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[BT-474 (line)]] | alt | 325 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.609× (z -9.3) ⚠ cell-cycle shift, explains ~65% of this change |
| [[HCT15 (line)]] | alt | 343 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.469× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[RPMI-7951 (line)]] | alt | 382 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.484× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[SW 1088 (line)]] | alt | 377 | 0 | 1 | — | [[Belumosudil (drug)]] 0.05 µM 0.232× (z -8.6) |
| [[SW 1271 (line)]] | alt | 480 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.216× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[AN3 CA (line)]] | alt | 405 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 626 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 243 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 494 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 199 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 99.6 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7299), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DCAF4L1]] | +0.66 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[SNX31]] | +0.64 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[CFAP53]] | +0.62 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[CASS4]] | +0.62 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[LINC00862]] | +0.61 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[ANKHD1-EIF4EBP3]] | +0.61 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[LINC02936]] | +0.60 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[N4BP2L2]] | +0.59 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[PSMD6-AS2]] | +0.59 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[CD63]] | +0.59 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[APRG1]] | +0.58 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[KLRD1]] | +0.58 | +0.52 / +0.46 | both halves | 2e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP5C]] | -0.61 | -0.61 / -0.54 | both halves | 1e-05 |  |
| [[SKP2]] | -0.58 | -0.51 / -0.52 | both halves | 1e-05 | pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[SAAL1]] | -0.57 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[DLAT]] | -0.54 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[AADAT]] | -0.54 | -0.48 / -0.56 | both halves | 2e-05 |  |
| [[STRA6LP]] | -0.54 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[DAGLA]] | -0.53 | -0.46 / -0.47 | both halves | 3e-05 |  |
| [[SUGT1P4-STRA6LP]] | -0.52 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[FAM98B]] | -0.52 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[POMGNT2]] | -0.52 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[ALDH7A1]] | -0.52 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[SHMT1]] | -0.51 | -0.38 / -0.47 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RNF103-CHMP3]] | B | RNF103-CHMP3 activity raises HERC4's level | lines that do not express RNF103-CHMP3 (5) vs lines expressing it (45) | 1.70× lower at baseline in the lines without RNF103-CHMP3 | 0.047 | ⚠ within organs, on part of the lines; also absent: TMEM144, YBX3, DTX4; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers HERC4's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Mitoxantrone) | 60% of the class's compounds vs 2.2% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[HDAC6]] | B | HDAC6 activity raises HERC4's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 037]]; 123 genes; every member is in the + arm (projection on the module's main direction 0.613). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (26.3, -16.1); signed map (12.1, 5.2). **Vector** length 141, 52.1% of its response variance represented; |z| ≥ 3 in 1,611 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +10.9 | +7.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +10.4 | +4.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +9.6 | +5.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +9.2 | +6.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +7.0 | +8.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +5.6 | +3.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | +5.4 | +2.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +4.1 | +2.7 |
| fall | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | -5.0 | -7.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | -4.4 | -8.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | -4.4 | -8.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -4.2 | -2.5 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -4.1 | -4.6 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -3.8 | -2.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -3.6 | -1.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -3.5 | -2.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -3.2 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | HECT and RLD domain containing E3 ubiquitin protein ligase 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q21.3 — chr10:67,921,899-68,075,301 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP564G092, KIAA1593 |
| Gene groups (HGNC) | HECT and RLD domain containing E3 ubiquitin protein ligases |
| Reactome | 3 pathways, smallest: Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation; Adaptive Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5GLZ8](https://www.uniprot.org/uniprotkb/Q5GLZ8) (Probable E3 ubiquitin-protein ligase HERC4):

> Probable E3 ubiquitin-protein ligase involved in either protein trafficking or in the distribution of cellular structures. Required for spermatozoon maturation and fertility, and for the removal of the cytoplasmic droplet of the spermatozoon. E3 ubiquitin-protein ligases accept ubiquitin from an E2 ubiquitin-conjugating enzyme in the form of a thioester and then directly transfer it to targeted substrates.

**Summary**, from NCBI Gene [26091](https://www.ncbi.nlm.nih.gov/gene/26091):

> HERC4 belongs to the HERC family of ubiquitin ligases, all of which contain a HECT domain and at least 1 RCC1 (MIM 179710)-like domain (RLD). The 350-amino acid HECT domain is predicted to catalyze the formation of a thioester with ubiquitin before transferring it to a substrate, and the RLD is predicted to act as a guanine nucleotide exchange factor for small G proteins (Hochrainer et al., 2005 [PubMed 15676274]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:24521](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24521) · Entrez [26091](https://www.ncbi.nlm.nih.gov/gene/26091) · UniProt [Q5GLZ8](https://www.uniprot.org/uniprotkb/Q5GLZ8) · Ensembl [ENSG00000148634](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000148634)

## Data

Gene col 7299: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7299); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7299, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7299]; `tensor/DDL_lfc|DDL_z.npy` [7299]; `embed/gene_vectors.npy` [7299]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7299 or target_col == 7299). Every well: [[HERC4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HERC4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
