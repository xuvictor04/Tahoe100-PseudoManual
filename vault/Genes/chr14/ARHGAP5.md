---
symbol: "ARHGAP5"
type: "gene"
col: 2031
ensembl_id: "ENSG00000100852"
name: "Rho GTPase activating protein 5"
location: "14q12"
module: 6
arm: "-"
pooled_cpm: 401.48
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 7
n_dd_up_clean: 4
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# ARHGAP5

*Rho GTPase activating protein 5* — 14q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 1.32× (z +9.7, q 1e-19, up in 32 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.513× (z -24.3, q 0e+00, down in 46 of 48 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Medroxyprogesterone acetate (drug)]] 0.5 µM: 0.863× (z -5.3, q 6e-06, down in 19 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 8 lines (SW1417 0.428×, SW480 0.454×, LS 180 0.342×, AsPC-1 0.303×, …; ⚠ cell-cycle shift, explains ~28% of this change); [[Panobinostat (drug)]] 0.5 µM in 4 lines (SW480 0.436×, SW1417 0.494×, KATO III 0.476×, LS 180 0.407×; ⚠ cell-cycle shift, explains ~26% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (C32 0.392×, A549 0.349×; ⚠ cell-cycle shift, explains ~65% of this change); [[Binimetinib (drug)]] 0.5 µM in 1 line (MIA PaCa-2 0.544×); [[Binimetinib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.635×); [[Trametinib (drug)]] 0.5 µM in 1 line (MIA PaCa-2 0.605×).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLK]] (+0.58, fdr 1e-05), [[C11orf58]] (+0.52, fdr 2e-04), [[BOD1L1]] (+0.51, fdr 3e-05); moves opposite to [[NDC1]] (-0.53, fdr 1e-04), [[LRRC45]] (-0.51, fdr 3e-05), [[PCYOX1L]] (-0.50, fdr 4e-05).
> It sits in the **-** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2031.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **1.32×** | +9.7 | 1e-19 | 32/48 (BT-474, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.24×** | +7.9 | 1e-12 | 27/48 (A498, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.23×** | +7.6 | 6e-12 | 28/49 (SW480, NCI-H23, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.21×** | +6.9 | 8e-10 | 25/48 (PANC-1, KATO III, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +6.4 | 1e-08 | 23/48 (PANC-1, Hs 766T, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +6.0 | 2e-07 | 22/48 (KATO III, SW1417, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | 1.12× | +5.9 | 2e-07 | 22/48 (A-427, BT-474, …) | all doses, stronger at high dose | composition shift |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~9% of this change | 1.17× | +5.8 | 3e-07 | 23/48 (SW480, H4, …) | all doses, flat |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.28×** | +4.8 | 1e-04 | 25/48 (LS 180, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.13× | +4.6 | 2e-04 | 19/48 (A498, A-427, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | 1.13× | +4.4 | 5e-04 | 15/48 (BT-474, RKO, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.13× | +4.4 | 6e-04 | 16/47 (SK-MEL-2, LS 180, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~16% of this change | 1.12× | +4.1 | 0.002 | 10/49 (HOP62, LOX-IMVI, …) | all doses, flat |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | 1.12× | +4.0 | 0.003 | 16/47 (HOP62, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 1.10× | +3.6 | 0.011 | 8/48 (HOP62, NCI-H23, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 1.11× | +3.4 | 0.019 | 13/47 (NCI-H460, C32, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Almonertinib (mesylate) (drug)]] 5 µM |  | 1.10× | +3.3 | 0.028 | 1/49 (H4) | top dose only | plate-row cell shift |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 1.09× | +3.0 | 0.063 | 3/48 (J82, NCI-H460, …) | inconsistent across doses |  |
| [[Saquinavir (drug)]] 5 µM |  | 1.06× | +2.9 | 0.094 | 0/48 | top dose only |  |
| [[Retinoic acid (drug)]] 5 µM |  | 1.06× | +2.9 | 0.094 | 1/49 (NCI-H460) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 12 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2031.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 8 lines (SW1417 0.428×, SW480 0.454×, LS 180 0.342×, AsPC-1 0.303×, …; ⚠ cell-cycle shift, explains ~28% of this change); [[Panobinostat (drug)]] 0.5 µM in 4 lines (SW480 0.436×, SW1417 0.494×, KATO III 0.476×, LS 180 0.407×; ⚠ cell-cycle shift, explains ~26% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (C32 0.392×, A549 0.349×; ⚠ cell-cycle shift, explains ~65% of this change); [[Binimetinib (drug)]] 0.5 µM in 1 line (MIA PaCa-2 0.544×); [[Binimetinib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.635×); [[Trametinib (drug)]] 0.5 µM in 1 line (MIA PaCa-2 0.605×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.513×** | -24.3 | 0e+00 | 46/48 (SW1417, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.542×** | -22.3 | 0e+00 | 46/48 (SW480, SW1417, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.602×** | -18.5 | 0e+00 | 43/48 (SW480, SW1417, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~42% of this change | **0.761×** | -9.5 | 2e-19 | 28/47 (MIA PaCa-2, CFPAC-1, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.815×** | -7.4 | 1e-11 | 26/48 (MIA PaCa-2, BT-474, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.818×** | -7.3 | 3e-11 | 25/48 (SK-MEL-2, COLO 205, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | 0.836× | -6.5 | 6e-09 | 23/48 (Panc 03.27, HT-29, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | 0.833× | -6.4 | 1e-08 | 24/48 (C32, MIA PaCa-2, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | 0.887× | -6.1 | 5e-08 | 19/49 (C32, A549, …) | all doses, stronger at high dose |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 0.863× | -5.3 | 6e-06 | 19/48 (NCI-H1573, SW1417, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~84% of this change | 0.872× | -5.0 | 4e-05 | 18/48 (MIA PaCa-2, SW1417, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~82% of this change | 0.875× | -4.6 | 2e-04 | 20/50 (C32, LS 180, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.792×** | -4.4 | 4e-04 | 26/49 (SW480, CFPAC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~0% of this change | 0.885× | -4.4 | 4e-04 | 12/48 (SW 900, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | 0.895× | -3.9 | 0.004 | 5/48 (SK-MEL-2, LS 180, …) | rises with dose |  |
| [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM |  | 0.911× | -3.4 | 0.027 | 4/48 (Panc 03.27, SHP-77, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.915× | -3.2 | 0.041 | 12/49 (MIA PaCa-2, AsPC-1, …) | two highest doses |  |
| [[Palmatine (chloride) (drug)]] 0.5 µM |  | 0.915× | -3.2 | 0.041 | 5/48 (Panc 03.27, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 0.941× | -3.1 | 0.055 | 0/48 | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | 0.853× | -3.0 | 0.071 | 10/48 (MIA PaCa-2, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | 0.913× | -3.0 | 0.084 | 3/47 (SW 1271, LS 180, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.32 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2031. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 988 | 0 | 12 (8 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.621× (z -23.6) ⚠ position not correctable · without an alert: [[Binimetinib (drug)]] 0.5 µM 0.544× (z -10.2) |
| [[BT-474 (line)]] | alt | 343 | 5 (3 ⚠) | 5 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +23.3) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.34× (z +16.3) | [[Panobinostat (drug)]] 0.5 µM 0.538× (z -12.3) ⚠ cell-cycle shift, explains ~26% of this change |
| [[A498 (line)]] | wt | 213 | 5 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +22.8) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.18× (z +16.5) | [[Panobinostat (drug)]] 5 µM 0.610× (z -10.4) ⚠ cell-cycle shift, explains ~28% of this change |
| [[C32 (line)]] | wt | 621 | 0 | 7 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.392× (z -20.6) ⚠ cell-cycle shift, explains ~65% of this change · without an alert: [[Ponatinib (drug)]] 5 µM 0.573× (z -8.7) |
| [[NCI-H23 (line)]] | alt | 340 | 4 (2 ⚠) | 3 (3 ⚠) | [[Harringtonine (drug)]] 5 µM 1.72× (z +11.0) | [[Belinostat (drug)]] 5 µM 0.650× (z -9.1) ⚠ cell-cycle shift, explains ~31% of this change |
| [[RKO (line)]] | wt | 285 | 7 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +15.8) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.66× (z +14.9) | — |
| [[LS 180 (line)]] | wt | 631 | 0 | 6 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.342× (z -19.8) ⚠ cell-cycle shift, explains ~28% of this change |
| [[NCI-H1792 (line)]] | alt | 910 | 0 | 6 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.372× (z -16.0) ⚠ cell-cycle shift, explains ~65% of this change |
| [[PANC-1 (line)]] | alt | 237 | 3 (3 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.55× (z +9.8) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 5 µM 0.555× (z -13.2) ⚠ cell-cycle shift, explains ~28% of this change |
| [[A-172 (line)]] | wt | 247 | 0 | 5 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.383× (z -14.6) ⚠ cell-cycle shift, explains ~28% of this change |
| [[A549 (line)]] | wt | 538 | 0 | 5 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.349× (z -19.8) ⚠ cell-cycle shift, explains ~65% of this change |
| [[CFPAC-1 (line)]] | alt | 808 | 0 | 5 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.413× (z -13.7) ⚠ cell-cycle shift, explains ~28% of this change |
| [[HepG2_C3A (line)]] | wt | 469 | 0 | 5 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.383× (z -14.1) ⚠ cell-cycle shift, explains ~28% of this change |
| [[Hs 766T (line)]] | wt | 362 | 2 (2 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.69× (z +9.3) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 5 µM 0.400× (z -16.1) ⚠ cell-cycle shift, explains ~28% of this change |
| [[J82 (line)]] | alt | 240 | 2 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.54× (z +12.6) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 1.56× (z +8.8) | [[Panobinostat (drug)]] 5 µM 0.569× (z -11.6) ⚠ cell-cycle shift, explains ~28% of this change |
| [[SK-MEL-2 (line)]] | alt | 478 | 0 | 5 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.419× (z -17.3) ⚠ cell-cycle shift, explains ~28% of this change |
| [[SW480 (line)]] | alt | 395 | 2 (2 ⚠) | 3 (3 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.55× (z +11.0) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.436× (z -21.0) ⚠ cell-cycle shift, explains ~26% of this change |
| [[A-427 (line)]] | wt | 215 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +23.7) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 1.74× (z +10.3) | — |
| [[HT-29 (line)]] | alt | 359 | 1 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.50× (z +9.1) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 5 µM 0.501× (z -15.6) ⚠ cell-cycle shift, explains ~28% of this change |
| [[KATO III (line)]] | alt | 388 | 1 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.83× (z +13.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 5 µM 0.441× (z -18.3) ⚠ cell-cycle shift, explains ~28% of this change |
| [[SW1417 (line)]] | alt | 523 | 1 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.56× (z +15.7) ⚠ cell-cycle shift, explains ~37% of this change | [[Panobinostat (drug)]] 5 µM 0.428× (z -21.2) ⚠ cell-cycle shift, explains ~28% of this change |
| [[AsPC-1 (line)]] | alt | 540 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.303× (z -18.7) ⚠ cell-cycle shift, explains ~28% of this change |
| [[COLO 205 (line)]] | alt | 600 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.450× (z -12.1) ⚠ cell-cycle shift, explains ~28% of this change |
| [[HEC-1-A (line)]] | alt | 411 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.458× (z -17.2) ⚠ cell-cycle shift, explains ~28% of this change |
| [[HOP62 (line)]] | alt | 289 | 1 | 2 (2 ⚠) | [[Harringtonine (drug)]] 0.5 µM 1.64× (z +10.0) | [[Panobinostat (drug)]] 5 µM 0.540× (z -12.4) ⚠ cell-cycle shift, explains ~28% of this change |
| [[LOX-IMVI (line)]] | wt | 267 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.504× (z -13.6) ⚠ cell-cycle shift, explains ~28% of this change |
| [[Panc 03.27 (line)]] | alt | 629 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.444× (z -13.5) ⚠ cell-cycle shift, explains ~28% of this change |
| [[RPMI-7951 (line)]] | alt | 332 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.428× (z -12.8) ⚠ cell-cycle shift, explains ~28% of this change |
| [[SNU-1 (line)]] | wt | 260 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.66× (z +11.0) ⚠ cell-cycle shift, explains ~37% of this change | [[Panobinostat (drug)]] 5 µM 0.542× (z -9.4) ⚠ cell-cycle shift, explains ~28% of this change |
| [[SW 900 (line)]] | alt | 363 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.393× (z -15.4) ⚠ cell-cycle shift, explains ~28% of this change |
| [[C-33 A (line)]] | alt | 337 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.521× (z -10.3) ⚠ cell-cycle shift, explains ~28% of this change |
| [[HCT15 (line)]] | alt | 473 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.537× (z -11.4) ⚠ cell-cycle shift, explains ~28% of this change |
| [[hTERT-HPNE (line)]] | wt | 221 | 2 | 0 | [[Harringtonine (drug)]] 0.5 µM 1.95× (z +9.5) | — |
| [[LoVo (line)]] | wt | 421 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.547× (z -12.7) ⚠ cell-cycle shift, explains ~28% of this change |
| [[NCI-H1573 (line)]] | alt | 333 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.568× (z -10.4) ⚠ cell-cycle shift, explains ~28% of this change |
| [[NCI-H2347 (line)]] | alt | 569 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.540× (z -9.9) ⚠ cell-cycle shift, explains ~28% of this change |
| [[NCI-H460 (line)]] | wt | 343 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.486× (z -11.3) ⚠ cell-cycle shift, explains ~28% of this change |
| [[CHP-212 (line)]] | wt | 320 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.391× (z -9.4) ⚠ cell-cycle shift, explains ~28% of this change |
| [[SNU-423 (line)]] | alt | 433 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.554× (z -10.7) ⚠ cell-cycle shift, explains ~28% of this change |
| [[SW48 (line)]] | wt | 298 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.515× (z -10.4) ⚠ cell-cycle shift, explains ~26% of this change |
| [[AN3 CA (line)]] | alt | 477 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 251 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 147 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 468 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 382 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 340 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 343 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 231 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 342 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2031), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*54 of its nearest partners move with it, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLK]] | +0.58 | +0.56 / +0.59 | both halves | 1e-05 | pathway: RHOA GTPase cycle |
| [[C11orf58]] | +0.52 | +0.29 / +0.59 | both halves | 2e-04 |  |
| [[BOD1L1]] | +0.51 | +0.45 / +0.50 | both halves | 3e-05 |  |
| [[JMJD1C]] | +0.49 | +0.46 / +0.51 | both halves | 2e-05 |  |
| [[AFF4]] | +0.48 | +0.33 / +0.55 | both halves | 1e-04 |  |
| [[OTUD6B-AS1]] | +0.48 | +0.38 / +0.35 | both halves | 1e-04 |  |
| [[CHMP4B]] | +0.47 | +0.20 / +0.56 | ⚠ one half (not replicated) | 8e-04 |  |
| [[RNF103-CHMP3]] | +0.47 | +0.34 / +0.42 | both halves | 1e-04 |  |
| [[ATG12]] | +0.46 | +0.41 / +0.43 | both halves | 4e-05 |  |
| [[GULP1]] | +0.46 | +0.26 / +0.54 | both halves | 4e-04 |  |
| [[C9orf85]] | +0.45 | +0.31 / +0.34 | both halves | 2e-04 |  |
| [[RO60]] | +0.45 | +0.30 / +0.45 | both halves | 2e-04 |  |
| [[CPEB4]] | +0.45 | +0.26 / +0.46 | both halves | 4e-04 |  |

## Genes that move opposite

*46 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDC1]] | -0.53 | -0.35 / -0.57 | both halves | 1e-04 |  |
| [[LRRC45]] | -0.51 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[PCYOX1L]] | -0.50 | -0.41 / -0.53 | both halves | 4e-05 |  |
| [[TBC1D14]] | -0.49 | -0.35 / -0.51 | both halves | 1e-04 |  |
| [[ALG6]] | -0.49 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[IPO11]] | -0.48 | -0.43 / -0.39 | both halves | 5e-05 |  |
| [[NUP93]] | -0.48 | -0.36 / -0.46 | both halves | 1e-04 |  |
| [[NUP153]] | -0.47 | -0.36 / -0.42 | both halves | 1e-04 |  |
| [[RBM14]] | -0.46 | -0.31 / -0.53 | both halves | 2e-04 |  |
| [[SCAF4]] | -0.46 | -0.41 / -0.39 | both halves | 6e-05 |  |
| [[PPIH]] | -0.46 | -0.29 / -0.46 | both halves | 2e-04 |  |
| [[POC1A]] | -0.46 | -0.25 / -0.50 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises ARHGAP5's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **-** arm (projection on the module's main direction -0.307). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-26.0, -43.9); signed map (7.5, -12.2). **Vector** length 126, 40.0% of its response variance represented; |z| ≥ 3 in 1,666 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +7.5 | +9.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +7.0 | +7.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.9 | +7.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +6.7 | +2.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +6.6 | +3.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.0 | +4.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.4 | +4.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +4.6 | +4.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.9 | -2.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.9 | +3.4 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -5.2 | -2.7 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | -3.5 | -5.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.3 | -3.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.1 | -2.0 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | -3.0 | -3.9 |
|  | [[Clonidine (hydrochloride) (drug)]] 5 µM |  | -3.0 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | Rho GTPase activating protein 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q12 — chr14:32,076,114-32,159,728 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RhoGAP5, p190-B, p190BRhoGAP; previously GFI2 |
| Gene groups (HGNC) | Rho GTPase activating proteins |
| Hallmark sets | MITOTIC_SPINDLE |
| Reactome | 17 pathways, smallest: RND1 GTPase cycle; RND2 GTPase cycle; RND3 GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13017](https://www.uniprot.org/uniprotkb/Q13017) (Rho GTPase-activating protein 5):

> GTPase-activating protein for Rho family members.

**Summary**, from NCBI Gene [394](https://www.ncbi.nlm.nih.gov/gene/394):

> Rho GTPase activating protein 5 negatively regulates RHO GTPases, a family which may mediate cytoskeleton changes by stimulating the hydrolysis of bound GTP. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:675](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:675) · Entrez [394](https://www.ncbi.nlm.nih.gov/gene/394) · UniProt [Q13017](https://www.uniprot.org/uniprotkb/Q13017) · Ensembl [ENSG00000100852](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100852)

## Data

Gene col 2031: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2031); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2031, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2031]; `tensor/DDL_lfc|DDL_z.npy` [2031]; `embed/gene_vectors.npy` [2031]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2031 or target_col == 2031). Every well: [[ARHGAP5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARHGAP5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
