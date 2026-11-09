---
symbol: "SPEN"
type: "gene"
col: 791
ensembl_id: "ENSG00000065526"
name: "spen family transcriptional repressor"
location: "1p36.21-p36.13"
module: 11
arm: "+"
pooled_cpm: 211.67
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 7
n_dd_up_clean: 11
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# SPEN

*spen family transcriptional repressor* — 1p36.21-p36.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.69× (z +22.8, q 0e+00, up in 42 of 48 measured lines) ⚠ cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.92× (z +19.9, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.715× (z -10.2, q 1e-21, down in 36 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (Hs 766T 0.432×, A-427 0.464×, HepG2/C3A 0.466×, NCI-H23 0.475×, …; ⚠ toxic; transcription drop); [[Panobinostat (drug)]] 0.5 µM in 6 lines (HT-29 0.550×, Hs 766T 0.517×, BT-474 0.482×, SW1417 0.529×, …); [[Panobinostat (drug)]] 5 µM in 6 lines (HEC-1-A 0.582×, Hs 766T 0.532×, LoVo 0.630×, HT-29 0.607×, …); [[Methylthiouracil (drug)]] 0.05 µM in 1 line (NCI-H596 0.0568×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TSC22D1]] (+0.62, fdr 1e-05), [[REST]] (+0.62, fdr 2e-05), [[KLF10]] (+0.59, fdr 1e-05); moves opposite to [[NDUFV1]] (-0.59, fdr 1e-05), [[TFG]] (-0.55, fdr 1e-05), [[SNX1]] (-0.54, fdr 1e-05).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[DLX2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 791.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.69×** | +22.8 | 0e+00 | 42/48 (A498, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.92×** | +19.9 | 0e+00 | 46/48 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.90×** | +18.8 | 0e+00 | 44/48 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.82×** | +18.3 | 0e+00 | 47/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.78×** | +17.6 | 0e+00 | 46/48 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.64×** | +15.2 | 0e+00 | 43/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.53×** | +13.1 | 5e-37 | 40/48 (SW480, LoVo, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.52×** | +12.9 | 4e-36 | 39/48 (MIA PaCa-2, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.50×** | +12.5 | 6e-34 | 37/48 (HEC-1-A, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.49×** | +11.6 | 1e-29 | 38/47 (NCI-H460, PANC-1, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.98×** | +11.0 | 3e-26 | 38/49 (PANC-1, HEC-1-A, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.54×** | +6.9 | 3e-10 | 32/48 (HEC-1-A, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.24×** | +6.5 | 4e-09 | 26/48 (MIA PaCa-2, SNU-1, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.21×** | +5.9 | 2e-07 | 25/47 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 1.18× | +4.8 | 6e-05 | 21/47 (NCI-H460, SNU-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.27×** | +3.8 | 0.004 | 19/48 (CFPAC-1, HS-578T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Glycyrrhizic acid (drug)]] 5 µM |  | 1.11× | +3.1 | 0.052 | 3/48 (AN3 CA, HS-578T, …) | top dose only | position effect removed |
| [[Malotilate (drug)]] 0.05 µM |  | 1.10× | +3.0 | 0.070 | 3/48 (CFPAC-1, SNU-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 791.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (Hs 766T 0.432×, A-427 0.464×, HepG2/C3A 0.466×, NCI-H23 0.475×, …; ⚠ toxic; transcription drop); [[Panobinostat (drug)]] 0.5 µM in 6 lines (HT-29 0.550×, Hs 766T 0.517×, BT-474 0.482×, SW1417 0.529×, …); [[Panobinostat (drug)]] 5 µM in 6 lines (HEC-1-A 0.582×, Hs 766T 0.532×, LoVo 0.630×, HT-29 0.607×, …); [[Methylthiouracil (drug)]] 0.05 µM in 1 line (NCI-H596 0.0568×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.715×** | -10.2 | 1e-21 | 36/48 (HT-29, Hs 766T, …) | two highest doses | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.747×** | -8.9 | 1e-16 | 33/49 (Hs 766T, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~22% of this change | **0.741×** | -8.8 | 3e-16 | 32/47 (RKO, MIA PaCa-2, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.746×** | -8.6 | 1e-15 | 30/44 (HepG2/C3A, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.751×** | -8.1 | 9e-14 | 28/45 (hTERT-HPNE, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.791×** | -7.2 | 8e-11 | 32/48 (HEC-1-A, Hs 766T, …) | two highest doses | cell-cycle shift (explains ~6% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **0.818×** | -5.9 | 4e-07 | 24/48 (A-172, LOX-IMVI, …) | top dose only |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 0.836× | -5.5 | 3e-06 | 23/48 (NCI-H1573, HS-578T, …) | inconsistent across doses | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~8% of this change | 0.855× | -4.6 | 3e-04 | 23/50 (A-427, A498, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.866× | -4.4 | 7e-04 | 15/48 (KATO III, RPMI-7951, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.908× | -4.2 | 0.002 | 11/48 (RKO, HepG2/C3A, …) | top dose only | low cells (technical?) |
| [[Goserelin (acetate) (drug)]] 5 µM |  | 0.910× | -4.0 | 0.003 | 0/48 | inconsistent across doses | position effect removed |
| [[Berbamine (drug)]] 0.5 µM |  | 0.886× | -3.7 | 0.010 | 7/48 (RPMI-7951, CHP-212, …) | inconsistent across doses |  |
| [[Decitabine (drug)]] 0.05 µM |  | 0.883× | -3.5 | 0.018 | 14/47 (A-427, RPMI-7951, …) | inconsistent across doses |  |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.894× | -3.4 | 0.026 | 3/49 (HT-29, SW48, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.926× | -3.2 | 0.039 | 2/48 (SW480, NCI-H23) | all doses, flat |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.928× | -3.2 | 0.040 | 2/48 (NCI-H1792, SW 1271) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.906× | -3.0 | 0.083 | 7/49 (KATO III, RPMI-7951, …) | top dose only |  |
| [[Dorzolamide (hydrochloride) (drug)]] 5 µM |  | 0.904× | -2.9 | 0.093 | 1/48 (SNU-1) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 791. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 226 | 14 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.62× (z +21.3) | — |
| [[HEC-1-A (line)]] | alt | 265 | 12 (3 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +25.0) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.12× (z +19.8) | [[Panobinostat (drug)]] 5 µM 0.582× (z -9.8) |
| [[PANC-1 (line)]] | alt | 236 | 12 (4 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +28.9) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.89× (z +22.5) | [[Dinaciclib (drug)]] 0.5 µM 0.631× (z -9.8) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 139 | 11 (5 ⚠) | 1 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.87× (z +17.8) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 5 µM 2.60× (z +16.2) | [[Dinaciclib (drug)]] 0.05 µM 0.484× (z -11.7) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 203 | 7 (2 ⚠) | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +17.7) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.95× (z +11.0) | [[Dinaciclib (drug)]] 0.5 µM 0.464× (z -12.6) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 415 | 6 (3 ⚠) | 5 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.15× (z +17.5) | [[Dinaciclib (drug)]] 0.5 µM 0.432× (z -12.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.517× (z -10.0) |
| [[HT-29 (line)]] | alt | 226 | 9 (2 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +19.1) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.23× (z +14.7) | [[Panobinostat (drug)]] 0.5 µM 0.550× (z -10.8) |
| [[LoVo (line)]] | wt | 264 | 10 (3 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.00× (z +21.6) | [[Panobinostat (drug)]] 5 µM 0.630× (z -9.0) |
| [[J82 (line)]] | alt | 292 | 7 (3 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +20.3) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.27× (z +15.7) | [[Dinaciclib (drug)]] 0.5 µM 0.539× (z -11.8) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 237 | 9 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +28.5) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.22× (z +25.5) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.451× (z -13.6) ⚠ toxic; cell-cycle shift, explains ~22% of this change |
| [[SNU-1 (line)]] | wt | 184 | 9 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.47× (z +15.6) | [[Dinaciclib (drug)]] 0.05 µM 0.460× (z -8.9) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 148 | 9 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +23.3) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.55× (z +16.4) | — |
| [[HepG2_C3A (line)]] | wt | 441 | 5 (2 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +16.7) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 2.02× (z +11.4) | [[Dinaciclib (drug)]] 5 µM 0.302× (z -18.5) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 243 | 8 (2 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 2.97× (z +17.4) | — |
| [[AsPC-1 (line)]] | alt | 229 | 4 (2 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +18.2) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.11× (z +11.2) | [[Dinaciclib (drug)]] 0.05 µM 0.459× (z -10.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.549× (z -8.9) |
| [[A498 (line)]] | wt | 184 | 4 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.55× (z +29.6) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.74× (z +21.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.639× (z -10.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 236 | 3 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 1.93× (z +10.3) | [[Dinaciclib (drug)]] 0.5 µM 0.477× (z -11.7) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 230 | 5 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +21.8) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.38× (z +13.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.555× (z -9.4) ⚠ toxic; cell-cycle shift, explains ~22% of this change |
| [[LS 180 (line)]] | wt | 209 | 6 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.50× (z +20.6) | — |
| [[A-172 (line)]] | wt | 163 | 3 | 2 (2 ⚠) | [[Harringtonine (drug)]] 0.5 µM 2.37× (z +11.7) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.414× (z -11.5) ⚠ cell-cycle shift, explains ~15% of this change |
| [[CFPAC-1 (line)]] | alt | 191 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +24.2) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.32× (z +12.4) | — |
| [[COLO 205 (line)]] | alt | 198 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.58× (z +13.2) | — |
| [[SK-MEL-2 (line)]] | alt | 170 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +16.9) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.69× (z +13.3) | [[Dinaciclib (drug)]] 5 µM 0.532× (z -8.5) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 203 | 4 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.03× (z +10.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.99× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.484× (z -10.6) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 209 | 3 (1 ⚠) | 2 | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 1.92× (z +9.9) | [[Panobinostat (drug)]] 0.5 µM 0.529× (z -9.7) |
| [[C32 (line)]] | wt | 131 | 4 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 2.97× (z +13.8) | — |
| [[H4 (line)]] | wt | 175 | 4 (1 ⚠) | 0 | [[Digitoxin (drug)]] 0.5 µM 2.72× (z +11.3) | — |
| [[LOX-IMVI (line)]] | wt | 196 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.477× (z -10.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.549× (z -8.9) |
| [[NCI-H2347 (line)]] | alt | 153 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +16.2) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.02× (z +9.7) | — |
| [[SHP-77 (line)]] | alt | 208 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.25× (z +12.6) | — |
| [[BT-474 (line)]] | alt | 172 | 2 (1 ⚠) | 1 | [[Auranofin (drug)]] 5 µM 2.57× (z +13.0) | [[Panobinostat (drug)]] 0.5 µM 0.482× (z -10.0) |
| [[hTERT-HPNE (line)]] | wt | 218 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.347× (z -12.3) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 198 | 2 | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 2.40× (z +11.9) | [[Dinaciclib (drug)]] 0.05 µM 0.468× (z -9.9) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 239 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.57× (z +10.3) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Auranofin (drug)]] 5 µM 1.72× (z +8.8) | [[Dinaciclib (drug)]] 0.5 µM 0.475× (z -12.1) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 259 | 2 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.07× (z +10.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.91× (z +9.6) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.317× (z -16.6) ⚠ toxic; cell-cycle shift, explains ~22% of this change |
| [[AN3 CA (line)]] | alt | 231 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.36× (z +8.8) | [[Dinaciclib (drug)]] 0.05 µM 0.362× (z -9.6) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 230 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.22× (z +10.5) | — |
| [[Panc 03.27 (line)]] | alt | 202 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +14.1) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.87× (z +9.6) | — |
| [[SNU-423 (line)]] | alt | 119 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +12.8) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.53× (z +11.0) | — |
| [[SW48 (line)]] | wt | 239 | 2 | 0 | [[Auranofin (drug)]] 5 µM 1.99× (z +9.1) | — |
| [[CHP-212 (line)]] | wt | 117 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +10.3) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[NCI-H2030 (line)]] | alt | 135 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.511× (z -9.4) ⚠ toxic; transcription drop |
| [[NCI-H596 (line)]] | alt | 207 | 0 | 1 | — | [[Methylthiouracil (drug)]] 0.05 µM 0.0568× (z -8.9) |
| [[RPMI-7951 (line)]] | alt | 271 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 2.35× (z +11.6) | — |
| [[C-33 A (line)]] | alt | 166 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 176 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 219 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 260 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 264 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 227 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 791), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TSC22D1]] | +0.62 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[REST]] | +0.62 | +0.48 / +0.66 | both halves | 2e-05 |  |
| [[KLF10]] | +0.59 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[CDKN2AIP]] | +0.58 | +0.46 / +0.59 | both halves | 3e-05 |  |
| [[PHF23]] | +0.58 | +0.48 / +0.61 | both halves | 2e-05 |  |
| [[ROCK2]] | +0.58 | +0.57 / +0.56 | both halves | 1e-05 | pathway: RHOBTB GTPase Cycle |
| [[SON]] | +0.57 | +0.50 / +0.62 | both halves | 1e-05 |  |
| [[TRIP11]] | +0.57 | +0.43 / +0.63 | both halves | 3e-05 |  |
| [[CEBPZ]] | +0.55 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[TOPORS]] | +0.55 | +0.49 / +0.45 | both halves | 3e-05 |  |
| [[MRFAP1L1]] | +0.55 | +0.46 / +0.50 | both halves | 3e-05 |  |
| [[ADNP2]] | +0.54 | +0.42 / +0.56 | both halves | 4e-05 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDUFV1]] | -0.59 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[TFG]] | -0.55 | -0.59 / -0.50 | both halves | 1e-05 |  |
| [[SNX1]] | -0.54 | -0.49 / -0.58 | both halves | 1e-05 |  |
| [[EEF1AKMT2]] | -0.54 | -0.41 / -0.60 | both halves | 4e-05 |  |
| [[FIG4]] | -0.53 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[ATP6AP2]] | -0.53 | -0.46 / -0.56 | both halves | 3e-05 |  |
| [[ANAPC5]] | -0.52 | -0.36 / -0.58 | both halves | 1e-04 |  |
| [[STAG3L4]] ⚠ | -0.52 | -0.37 / -0.59 | both halves | 8e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[RPL10]] | -0.52 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[VTI1B]] | -0.51 | -0.44 / -0.43 | both halves | 4e-05 |  |
| [[FAM168B]] | -0.51 | -0.54 / -0.54 | both halves | 1e-05 |  |
| [[ATPAF1]] | -0.51 | -0.33 / -0.53 | both halves | 1e-04 |  |
| [[MARCHF6]] | -0.50 | -0.49 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DLX2]] | B | DLX2 activity raises SPEN's level | lines that do not express DLX2 (8) vs lines expressing it (42) | 1.24× lower at baseline in the lines without DLX2 | 0.036 | ⚠ within organs, on part of the lines; also absent: LINC01145-1, SCHIP1, NPHS1; maybe low, not absent |
| [[TOP1]] | B | TOP1 activity raises SPEN's level | compounds that target TOP1: 2 of 3 lower it (Doxorubicin, Topotecan) | 67% of the class's compounds vs 1.1% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.487). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-38.7, 16.4); signed map (3.9, -15.8). **Vector** length 123, 39.1% of its response variance represented; |z| ≥ 3 in 1,467 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +10.3 | +13.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +7.1 | +12.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +6.2 | +22.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +6.2 | +18.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.1 | +18.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.8 | +6.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +4.8 | +4.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.6 | +1.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | -0.1 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~22% of this change | -4.7 | -8.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.4 | -8.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -4.0 | -8.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -3.4 | +1.1 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | -3.3 | -5.5 |
|  | [[NVP-BHG712 (drug)]] 0.05 µM |  | -3.0 | -1.8 |
|  | [[Gallic acid (drug)]] 5 µM |  | -2.9 | -1.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.9 | +1.0 |
|  | [[Diphenhydramine (drug)]] 5 µM |  | -2.9 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | spen family transcriptional repressor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.21-p36.13 — chr1:15,836,095-15,940,456 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0929, MINT, SHARP, RBM15C |
| Gene groups (HGNC) | RNA binding motif containing |
| Reactome | 5 pathways, smallest: RHOBTB1 GTPase cycle; RHOBTB GTPase Cycle; RHO GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96T58](https://www.uniprot.org/uniprotkb/Q96T58) (Msx2-interacting protein):

> May serve as a nuclear matrix platform that organizes and integrates transcriptional responses. In osteoblasts, supports transcription activation: synergizes with RUNX2 to enhance FGFR2-mediated activation of the osteocalcin FGF-responsive element (OCFRE) (By similarity). Has also been shown to be an essential corepressor protein, which probably regulates different key pathways such as the Notch pathway. Negative regulator of the Notch pathway via its interaction with RBPSUH, which prevents the …

**Summary**, from NCBI Gene [23013](https://www.ncbi.nlm.nih.gov/gene/23013):

> This gene encodes a hormone inducible transcriptional repressor. Repression of transcription by this gene product can occur through interactions with other repressors, by the recruitment of proteins involved in histone deacetylation, or through sequestration of transcriptional activators. The product of this gene contains a carboxy-terminal domain that permits binding to other corepressor proteins. This domain also permits interaction with members of the NuRD complex, a nucleosome remodeling …

**Accessions** — [HGNC:17575](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17575) · Entrez [23013](https://www.ncbi.nlm.nih.gov/gene/23013) · UniProt [Q96T58](https://www.uniprot.org/uniprotkb/Q96T58) · Ensembl [ENSG00000065526](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000065526)

## Data

Gene col 791: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 791); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 791, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 791]; `tensor/DDL_lfc|DDL_z.npy` [791]; `embed/gene_vectors.npy` [791]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 791 or target_col == 791). Every well: [[SPEN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPEN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
