---
symbol: "USP9X"
type: "gene"
col: 4533
ensembl_id: "ENSG00000124486"
name: "ubiquitin specific peptidase 9 X-linked"
location: "Xp11.4"
module: 15
arm: "-"
pooled_cpm: 347.36
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 7
n_dd_up_clean: 14
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# USP9X

*ubiquitin specific peptidase 9 X-linked* — Xp11.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.85× (z +15.7, q 0e+00, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (5 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 0.509× (z -11.8, q 3e-29, down in 45 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Topotecan (hydrochloride) (drug)]] 0.5 µM: 0.738× (z -5.5, q 5e-06, down in 42 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (A549 0.359×, KATO III 0.429×, HCT15 0.366×, C-33 A 0.376×, …; ⚠ toxic; transcription drop); [[Topotecan (hydrochloride) (drug)]] 5 µM in 4 lines (SW480 0.373×, MIA PaCa-2 0.317×, KATO III 0.409×, C32 0.389×; ⚠ toxic); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (C-33 A 0.311×, HEC-1-A 0.422×, CFPAC-1 0.429×; ⚠ toxic; transcription drop); [[Topotecan (hydrochloride) (drug)]] 0.5 µM in 1 line (MIA PaCa-2 0.433×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATP7A]] (+0.61, fdr 7e-05), [[ENO1]] (+0.60, fdr 3e-05), [[YWHAZ]] (+0.57, fdr 1e-05); moves opposite to [[STARD7-AS1]] (-0.59, fdr 1e-05), [[ZNF785]] (-0.57, fdr 1e-05), [[MTG2]] (-0.57, fdr 1e-05).
> It sits in the **-** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ZNF547]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4533.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.85×** | +15.7 | 0e+00 | 43/48 (A498, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.06×** | +13.0 | 2e-36 | 47/48 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **4.39×** | +11.5 | 3e-28 | 48/49 (BT-474, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.64×** | +9.0 | 3e-17 | 44/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.63×** | +8.5 | 2e-15 | 39/48 (A498, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.55×** | +7.9 | 2e-13 | 37/48 (KATO III, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.51×** | +7.5 | 6e-12 | 38/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.50×** | +7.4 | 1e-11 | 37/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.52×** | +7.2 | 5e-11 | 46/48 (HEC-1-A, SW480, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.46×** | +6.9 | 4e-10 | 35/48 (SNU-423, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.45×** | +6.7 | 9e-10 | 34/48 (SNU-423, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.24×** | +5.5 | 2e-06 | 29/48 (KATO III, AN3 CA, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.33×** | +4.9 | 4e-05 | 36/47 (NCI-H460, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.23×** | +3.7 | 0.008 | 26/48 (PANC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.20×** | +3.3 | 0.034 | 23/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Erlotinib (drug)]] 0.05 µM |  | **1.21×** | +3.2 | 0.046 | 25/48 (NCI-H2030, A498, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.18× | +3.0 | 0.077 | 19/48 (HT-29, PANC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 7 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4533.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (A549 0.359×, KATO III 0.429×, HCT15 0.366×, C-33 A 0.376×, …; ⚠ toxic; transcription drop); [[Topotecan (hydrochloride) (drug)]] 5 µM in 4 lines (SW480 0.373×, MIA PaCa-2 0.317×, KATO III 0.409×, C32 0.389×; ⚠ toxic); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (C-33 A 0.311×, HEC-1-A 0.422×, CFPAC-1 0.429×; ⚠ toxic; transcription drop); [[Topotecan (hydrochloride) (drug)]] 0.5 µM in 1 line (MIA PaCa-2 0.433×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.509×** | -11.8 | 3e-29 | 45/47 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.569×** | -10.2 | 4e-22 | 44/49 (C-33 A, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.620×** | -8.3 | 1e-14 | 37/44 (A549, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.738×** | -5.5 | 5e-06 | 42/48 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~5% of this change | 0.836× | -4.6 | 4e-04 | 23/49 (A549, AN3 CA, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.804×** | -4.0 | 0.007 | 34/48 (hTERT-HPNE, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.800×** | -3.8 | 0.013 | 24/45 (NCI-H2347, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.829×** | -3.4 | 0.044 | 23/48 (PANC-1, COLO 205, …) | two highest doses |  |
| [[Amsacrine (drug)]] 5 µM |  | 0.888× | -3.1 | 0.14 | 12/48 (A549, NCI-H23, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~4% of this change | 0.848× | -3.0 | 0.14 | 21/48 (BT-474, AN3 CA, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4533. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 448 | 14 (5 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.73× (z +23.4) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.467× (z -11.1) ⚠ toxic |
| [[SW480 (line)]] | alt | 468 | 9 (2 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.90× (z +16.2) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.373× (z -14.5) ⚠ toxic |
| [[BT-474 (line)]] | alt | 375 | 9 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.41× (z +16.8) | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.449× (z -11.1) ⚠ cell-cycle shift, explains ~4% of this change |
| [[KATO III (line)]] | alt | 377 | 7 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.38× (z +13.3) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.409× (z -13.2) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 677 | 7 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +13.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.618× (z -9.2) ⚠ cell-cycle shift, explains ~5% of this change |
| [[AsPC-1 (line)]] | alt | 265 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +20.4) | — |
| [[LoVo (line)]] | wt | 240 | 7 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.59× (z +15.7) | [[Dinaciclib (drug)]] 5 µM 0.586× (z -8.6) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 456 | 4 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +13.5) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.317× (z -14.2) ⚠ toxic · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.433× (z -10.8) |
| [[PANC-1 (line)]] | alt | 203 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +19.4) | — |
| [[HEC-1-A (line)]] | alt | 507 | 4 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +14.7) | [[Dinaciclib (drug)]] 0.5 µM 0.422× (z -12.4) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 239 | 6 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +13.1) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.480× (z -10.4) ⚠ toxic |
| [[HS-578T (line)]] | alt | 203 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +16.6) | — |
| [[A-172 (line)]] | wt | 334 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +14.4) | — |
| [[A549 (line)]] | wt | 445 | 3 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +18.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.354× (z -20.1) ⚠ cell-cycle shift, explains ~5% of this change |
| [[CFPAC-1 (line)]] | alt | 339 | 2 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +12.4) | [[Dinaciclib (drug)]] 0.5 µM 0.429× (z -12.1) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 400 | 5 (1 ⚠) | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 4.02× (z +13.7) | [[Dinaciclib (drug)]] 5 µM 0.294× (z -12.1) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 266 | 4 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.44× (z +12.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.607× (z -9.9) ⚠ cell-cycle shift, explains ~5% of this change |
| [[NCI-H2347 (line)]] | alt | 432 | 2 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.65× (z +10.3) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.434× (z -11.8) ⚠ toxic |
| [[RPMI-7951 (line)]] | alt | 471 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +15.1) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.488× (z -9.5) ⚠ toxic |
| [[SNU-1 (line)]] | wt | 278 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +11.0) | — |
| [[A498 (line)]] | wt | 222 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.25× (z +30.5) | — |
| [[C-33 A (line)]] | alt | 750 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.311× (z -15.3) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 274 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +12.1) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.389× (z -12.4) ⚠ toxic |
| [[COLO 205 (line)]] | alt | 298 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +18.9) | — |
| [[Hs 766T (line)]] | wt | 316 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +15.6) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.463× (z -8.8) ⚠ toxic |
| [[hTERT-HPNE (line)]] | wt | 276 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +11.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.407× (z -10.9) ⚠ toxic |
| [[Panc 03.27 (line)]] | alt | 374 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +16.4) | [[Dinaciclib (drug)]] 5 µM 0.421× (z -12.2) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 837 | 0 | 4 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.436× (z -10.7) ⚠ cell-cycle shift, explains ~5% of this change |
| [[J82 (line)]] | alt | 386 | 3 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.22× (z +11.4) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.521× (z -8.9) ⚠ toxic |
| [[LOX-IMVI (line)]] | wt | 142 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +14.8) | — |
| [[SW48 (line)]] | wt | 559 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.35× (z +9.9) | [[Dinaciclib (drug)]] 0.5 µM 0.408× (z -10.4) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 354 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.07× (z +9.5) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.399× (z -11.8) ⚠ toxic |
| [[RKO (line)]] | wt | 445 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +11.0) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.430× (z -10.0) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 286 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 6.22× (z +10.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.608× (z -9.9) ⚠ cell-cycle shift, explains ~5% of this change |
| [[SW1417 (line)]] | alt | 447 | 2 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.99× (z +10.3) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.483× (z -10.5) ⚠ toxic |
| [[H4 (line)]] | wt | 297 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +11.6) | — |
| [[HCT15 (line)]] | alt | 349 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.366× (z -12.3) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 160 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.69× (z +9.9) | — |
| [[NCI-H23 (line)]] | alt | 298 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.450× (z -11.5) ⚠ toxic |
| [[SW 900 (line)]] | alt | 248 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.09× (z +10.3) | [[Dinaciclib (drug)]] 5 µM 0.433× (z -11.4) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 251 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.56× (z +10.9) | — |
| [[LS 180 (line)]] | wt | 311 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.31× (z +11.4) | — |
| [[NCI-H661 (line)]] | alt | 480 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.294× (z -8.9) ⚠ toxic |
| [[SHP-77 (line)]] | alt | 216 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.439× (z -10.6) ⚠ toxic |
| [[A-427 (line)]] | wt | 404 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 290 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 385 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 356 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 281 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 235 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4533), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*49 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP7A]] | +0.61 | +0.38 / +0.63 | both halves | 7e-05 |  |
| [[ENO1]] | +0.60 | +0.46 / +0.56 | both halves | 3e-05 |  |
| [[YWHAZ]] | +0.57 | +0.56 / +0.62 | both halves | 1e-05 | STRING 485 |
| [[BAIAP2-DT]] | +0.57 | +0.61 / +0.36 | both halves | 1e-04 |  |
| [[PGK1]] | +0.57 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[POLR2E]] | +0.56 | +0.31 / +0.51 | both halves | 2e-04 |  |
| [[SPAG9]] | +0.55 | +0.40 / +0.57 | both halves | 5e-05 |  |
| [[AIG1]] | +0.55 | +0.34 / +0.55 | both halves | 1e-04 |  |
| [[TTC3P1]] | +0.54 | +0.29 / +0.43 | both halves | 2e-04 |  |
| [[C1QTNF3-AMACR]] | +0.54 | +0.41 / +0.41 | both halves | 4e-05 |  |
| [[HUWE1]] | +0.53 | +0.43 / +0.61 | both halves | 3e-05 | same gene group; STRING 908 |
| [[GDE1]] | +0.53 | +0.42 / +0.45 | both halves | 4e-05 |  |

## Genes that move opposite

*51 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STARD7-AS1]] | -0.59 | -0.50 / -0.61 | both halves | 1e-05 |  |
| [[ZNF785]] | -0.57 | -0.53 / -0.55 | both halves | 1e-05 |  |
| [[MTG2]] | -0.57 | -0.49 / -0.54 | both halves | 1e-05 |  |
| [[PTPN9]] | -0.57 | -0.41 / -0.53 | both halves | 4e-05 |  |
| [[TMEM267]] | -0.56 | -0.44 / -0.59 | both halves | 3e-05 |  |
| [[TRAPPC13]] | -0.56 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[C3orf33]] | -0.55 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[C1orf109]] | -0.54 | -0.48 / -0.55 | both halves | 2e-05 |  |
| [[MTO1]] | -0.54 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[ZNF500]] | -0.54 | -0.40 / -0.62 | both halves | 5e-05 |  |
| [[C10orf88]] | -0.53 | -0.58 / -0.42 | both halves | 4e-05 |  |
| [[ZBTB8A]] | -0.52 | -0.51 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF547]] | B | ZNF547 activity raises USP9X's level | lines that do not express ZNF547 (6) vs lines expressing it (44) | 1.38× lower at baseline in the lines without ZNF547 | 0.038 | ⚠ within organs, on part of the lines; also absent: TRAPPC2B, ZNF548, SPACA6 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **-** arm (projection on the module's main direction -0.434). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-16.7, 22.4); signed map (-12.7, 32.7). **Vector** length 93.5, 37.6% of its response variance represented; |z| ≥ 3 in 1,197 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.7 | +5.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.9 | +6.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.9 | +7.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.3 | +1.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.1 | -10.2 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.4 | +0.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.2 | +0.4 |
|  | [[Thymol (drug)]] 5 µM |  | +2.1 | -1.5 |
|  | [[Busulfan (drug)]] 0.05 µM |  | +2.0 | -0.4 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -10.3 | -11.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -8.0 | -5.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~5% of this change | -4.6 | -4.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.4 | -0.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~8% of this change | -4.2 | +2.0 |
|  | [[EX229 (drug)]] 5 µM |  | -3.2 | -0.9 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.7 | +0.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | -2.6 | -2.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.6 | -2.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.4 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin specific peptidase 9 X-linked |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp11.4 — chrX:41,085,445-41,236,579 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DFFRX, FAF, FAF-X, MRX99 |
| Gene groups (HGNC) | Ubiquitin specific peptidases; Armadillo like helical domain containing; Centriolar satellite proteins |
| Reactome | 16 pathways, smallest: Downregulation of SMAD2/3:SMAD4 transcriptional activity; Synthesis of active ubiquitin: roles of E1 and E2 enzymes; RHOV GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q93008](https://www.uniprot.org/uniprotkb/Q93008) (Ubiquitin carboxyl-terminal hydrolase 9X):

> Deubiquitinase involved both in the processing of ubiquitin precursors and of ubiquitinated proteins. May therefore play an important regulatory role at the level of protein turnover by preventing degradation of proteins through the removal of conjugated ubiquitin. Specifically hydrolyzes 'Lys-11'-, followed by 'Lys-63'-, 'Lys-48'- and 'Lys-6'-linked polyubiquitins chains. Essential component of TGF-beta/BMP signaling cascade. Specifically deubiquitinates monoubiquitinated SMAD4, opposing the …

**Summary**, from NCBI Gene [8239](https://www.ncbi.nlm.nih.gov/gene/8239):

> This gene is a member of the peptidase C19 family and encodes a protein that is similar to ubiquitin-specific proteases. Though this gene is located on the X chromosome, it escapes X-inactivation. Mutations in this gene have been associated with Turner syndrome. Alternate transcriptional splice variants, encoding different isoforms, have been characterized. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:12632](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12632) · Entrez [8239](https://www.ncbi.nlm.nih.gov/gene/8239) · UniProt [Q93008](https://www.uniprot.org/uniprotkb/Q93008) · Ensembl [ENSG00000124486](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000124486)

## Data

Gene col 4533: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4533); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4533, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4533]; `tensor/DDL_lfc|DDL_z.npy` [4533]; `embed/gene_vectors.npy` [4533]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4533 or target_col == 4533). Every well: [[USP9X — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/USP9X.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
