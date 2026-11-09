---
symbol: "ITSN2"
type: "gene"
col: 12584
ensembl_id: "ENSG00000198399"
name: "intersectin 2"
location: "2p23.3"
module: 20
arm: "-"
pooled_cpm: 217.92
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 18
n_dd_up_clean: 9
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# ITSN2

*intersectin 2* — 2p23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.99× (z +28.6, q 0e+00, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.410× (z -26.1, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SEC62]] (+0.71, fdr 7e-06), [[NFKBIB]] (+0.70, fdr 7e-06), [[DNAJC21]] (+0.69, fdr 7e-06); moves opposite to [[PMPCA]] (-0.64, fdr 1e-05), [[ATP5F1B]] (-0.64, fdr 1e-05), [[PAICS]] (-0.62, fdr 1e-05).
> It sits in the **-** arm of [[Module 020]] (Cap-dependent Translation Initiation).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TLCD5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 11 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12584.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.99×** | +28.6 | 0e+00 | 44/48 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.38×** | +25.4 | 0e+00 | 48/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.05×** | +21.0 | 0e+00 | 47/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.97×** | +19.1 | 0e+00 | 47/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.83×** | +17.8 | 0e+00 | 44/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.68×** | +15.2 | 0e+00 | 46/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.41×** | +9.8 | 1e-20 | 40/47 (PANC-1, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.88×** | +9.7 | 3e-20 | 40/49 (SW480, Panc 03.27, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.34×** | +8.6 | 6e-16 | 31/48 (A-172, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.33×** | +8.3 | 6e-15 | 30/48 (A-172, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.21×** | +5.6 | 1e-06 | 26/48 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +5.2 | 9e-06 | 21/48 (NCI-H460, SW 900, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +4.9 | 3e-05 | 22/47 (NCI-H460, H4, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +4.7 | 8e-05 | 19/48 (H4, HCT15, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.16× | +4.5 | 3e-04 | 22/48 (LS 180, HCT15, …) | rises with dose |  |
| [[Rapamycin (drug)]] 0.5 µM |  | 1.15× | +4.0 | 0.002 | 10/48 (Hs 766T, CFPAC-1, …) | all doses, flat |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.10× | +4.0 | 0.002 | 9/49 (CFPAC-1, NCI-H1573, …) | rises with dose |  |
| [[Rapamycin (drug)]] 5 µM |  | 1.09× | +3.8 | 0.005 | 1/48 (CFPAC-1) | all doses, flat |  |
| [[Temsirolimus (drug)]] 5 µM |  | 1.09× | +3.7 | 0.006 | 2/49 (Hs 766T, CHP-212) | rises with dose |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | 1.13× | +3.5 | 0.011 | 11/48 (RPMI-7951, CFPAC-1, …) | rises with dose |  |
| [[ULK-101 (drug)]] 0.05 µM |  | 1.13× | +3.3 | 0.022 | 5/49 (NCI-H460, SNU-423, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 13 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12584.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.410×** | -26.1 | 0e+00 | 47/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.442×** | -23.9 | 0e+00 | 48/48 (KATO III, SW480, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.473×** | -21.9 | 0e+00 | 48/48 (KATO III, SW480, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.614×** | -20.2 | 0e+00 | 44/49 (A549, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.659×** | -11.7 | 1e-29 | 35/48 (MIA PaCa-2, HOP62, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.723×** | -9.5 | 2e-19 | 31/48 (SNU-423, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.734×** | -8.7 | 2e-16 | 36/50 (LOX-IMVI, Panc 03.27, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.754×** | -8.3 | 9e-15 | 34/48 (HS-578T, Panc 03.27, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.764×** | -7.9 | 2e-13 | 27/48 (Panc 03.27, HT-29, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.934× | -7.0 | 2e-10 | 0/50 | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~69% of this change | **0.801×** | -6.3 | 2e-08 | 30/47 (MIA PaCa-2, HT-29, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.821×** | -5.8 | 4e-07 | 26/48 (MIA PaCa-2, AsPC-1, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **0.819×** | -5.6 | 9e-07 | 23/44 (NCI-H1573, A-172, …) | all doses, stronger at high dose | composition shift |
| [[TAK-733 (drug)]] 5 µM |  | **0.733×** | -4.7 | 8e-05 | 27/48 (AsPC-1, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.892× | -4.7 | 9e-05 | 13/48 (HOP62, NCI-H661, …) | top dose only |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 0.868× | -4.1 | 0.001 | 16/48 (A498, NCI-H460, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.786×** | -3.7 | 0.007 | 18/48 (MIA PaCa-2, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **0.791×** | -3.6 | 0.010 | 17/47 (HCT15, SW 900, …) | top dose only | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.891× | -3.4 | 0.020 | 11/49 (SNU-423, NCI-H2347, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.893× | -3.3 | 0.022 | 10/48 (MIA PaCa-2, NCI-H1573, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | 0.897× | -3.2 | 0.036 | 7/48 (HEC-1-A, CFPAC-1, …) | rises with dose |  |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 0.928× | -3.1 | 0.047 | 0/48 | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **0.820×** | -3.0 | 0.050 | 17/49 (HT-29, HS-578T, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.820×** | -3.0 | 0.050 | 20/48 (AsPC-1, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.42 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12584. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 166 | 12 (4 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +22.4) | [[Panobinostat (drug)]] 0.5 µM 0.529× (z -11.3) |
| [[SW480 (line)]] | alt | 259 | 8 (2 ⚠) | 7 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.39× (z +18.0) | [[Panobinostat (drug)]] 0.5 µM 0.277× (z -26.5) |
| [[A-172 (line)]] | wt | 313 | 4 (1 ⚠) | 10 (7 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.73× (z +28.2) | [[Panobinostat (drug)]] 5 µM 0.317× (z -17.4) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.349× (z -16.0) |
| [[Panc 03.27 (line)]] | alt | 300 | 4 | 10 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +16.5) | [[Panobinostat (drug)]] 5 µM 0.336× (z -21.1) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.355× (z -20.0) |
| [[HOP62 (line)]] | alt | 152 | 6 (1 ⚠) | 6 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.05× (z +16.1) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.328× (z -15.5) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.490× (z -14.6) |
| [[HS-578T (line)]] | alt | 144 | 6 (1 ⚠) | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +14.9) | [[Panobinostat (drug)]] 5 µM 0.297× (z -18.2) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.345× (z -16.0) |
| [[HT-29 (line)]] | alt | 239 | 2 | 10 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.61× (z +10.1) | [[Panobinostat (drug)]] 5 µM 0.195× (z -24.5) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.238× (z -21.5) |
| [[KATO III (line)]] | alt | 197 | 6 (2 ⚠) | 6 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.74× (z +17.6) | [[Panobinostat (drug)]] 5 µM 0.218× (z -26.5) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.220× (z -26.3) |
| [[LOX-IMVI (line)]] | wt | 286 | 4 (1 ⚠) | 8 (5 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.19× (z +12.9) | [[Panobinostat (drug)]] 0.5 µM 0.265× (z -21.7) |
| [[PANC-1 (line)]] | alt | 237 | 8 (3 ⚠) | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +39.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.556× (z -18.7) |
| [[CFPAC-1 (line)]] | alt | 229 | 6 (1 ⚠) | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +18.2) | [[Panobinostat (drug)]] 0.5 µM 0.440× (z -12.2) |
| [[NCI-H23 (line)]] | alt | 248 | 6 (1 ⚠) | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +15.3) | [[Belinostat (drug)]] 5 µM 0.542× (z -10.1) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.571× (z -9.2) |
| [[NCI-H2347 (line)]] | alt | 196 | 6 (2 ⚠) | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +30.3) | [[Panobinostat (drug)]] 0.5 µM 0.439× (z -15.5) |
| [[SNU-423 (line)]] | alt | 189 | 4 (1 ⚠) | 7 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +15.5) | [[Panobinostat (drug)]] 5 µM 0.225× (z -22.7) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.237× (z -22.0) |
| [[A549 (line)]] | wt | 441 | 4 | 6 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +21.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.302× (z -30.0) |
| [[AsPC-1 (line)]] | alt | 193 | 6 (1 ⚠) | 4 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.11× (z +17.7) | [[Panobinostat (drug)]] 0.5 µM 0.371× (z -15.5) |
| [[SW 900 (line)]] | alt | 171 | 6 (1 ⚠) | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +19.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.536× (z -12.2) |
| [[SW1417 (line)]] | alt | 230 | 5 (1 ⚠) | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +16.1) | [[Panobinostat (drug)]] 0.5 µM 0.377× (z -18.1) |
| [[BT-474 (line)]] | alt | 103 | 5 (1 ⚠) | 4 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.32× (z +14.5) | [[Panobinostat (drug)]] 5 µM 0.389× (z -11.4) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.412× (z -10.7) |
| [[HEC-1-A (line)]] | alt | 225 | 5 (1 ⚠) | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +25.8) | [[Panobinostat (drug)]] 5 µM 0.476× (z -12.5) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.602× (z -12.0) |
| [[HepG2_C3A (line)]] | wt | 176 | 6 (2 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +17.0) | [[Panobinostat (drug)]] 0.5 µM 0.314× (z -16.0) |
| [[MIA PaCa-2 (line)]] | alt | 209 | 2 | 7 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +13.1) | [[Panobinostat (drug)]] 5 µM 0.305× (z -17.8) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.321× (z -17.0) |
| [[NCI-H1573 (line)]] | alt | 402 | 3 (1 ⚠) | 6 (5 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.10× (z +15.9) | [[Dinaciclib (drug)]] 0.5 µM 0.327× (z -15.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.387× (z -13.5) |
| [[RKO (line)]] | wt | 260 | 4 (1 ⚠) | 5 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.49× (z +13.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.409× (z -18.3) |
| [[RPMI-7951 (line)]] | alt | 221 | 4 (1 ⚠) | 5 (3 ⚠) | [[Harringtonine (drug)]] 5 µM 3.79× (z +16.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.406× (z -16.7) |
| [[H4 (line)]] | wt | 126 | 7 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +14.8) | [[Panobinostat (drug)]] 5 µM 0.429× (z -8.5) ⚠ cell-cycle shift, explains ~31% of this change |
| [[LoVo (line)]] | wt | 148 | 6 (3 ⚠) | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.71× (z +16.9) | [[Panobinostat (drug)]] 5 µM 0.557× (z -9.9) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.592× (z -8.9) |
| [[COLO 205 (line)]] | alt | 131 | 4 (1 ⚠) | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.75× (z +15.5) | [[Belinostat (drug)]] 5 µM 0.343× (z -12.6) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.390× (z -11.1) |
| [[Hs 766T (line)]] | wt | 123 | 3 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +14.0) | [[Panobinostat (drug)]] 0.5 µM 0.316× (z -14.4) |
| [[J82 (line)]] | alt | 124 | 3 (1 ⚠) | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +20.4) | [[Panobinostat (drug)]] 0.5 µM 0.406× (z -13.1) |
| [[LS 180 (line)]] | wt | 141 | 6 (2 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.46× (z +17.7) | [[Panobinostat (drug)]] 0.5 µM 0.544× (z -8.7) |
| [[NCI-H1792 (line)]] | alt | 170 | 3 (1 ⚠) | 4 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 2.31× (z +12.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.24× (z +11.7) | [[Panobinostat (drug)]] 5 µM 0.434× (z -12.2) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.474× (z -11.0) |
| [[NCI-H2030 (line)]] | alt | 333 | 1 | 5 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.71× (z +10.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.422× (z -22.5) |
| [[A498 (line)]] | wt | 258 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +22.3) | — |
| [[C-33 A (line)]] | alt | 191 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +13.2) | — |
| [[HCT15 (line)]] | alt | 182 | 5 (2 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.92× (z +12.8) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.98× (z +12.0) | — |
| [[SHP-77 (line)]] | alt | 156 | 2 (1 ⚠) | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.36× (z +12.1) | [[Panobinostat (drug)]] 0.5 µM 0.409× (z -12.6) |
| [[SK-MEL-2 (line)]] | alt | 181 | 1 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.72× (z +11.7) | [[Panobinostat (drug)]] 0.5 µM 0.402× (z -13.9) |
| [[C32 (line)]] | wt | 163 | 2 (1 ⚠) | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.18× (z +10.2) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.471× (z -9.4) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.622× (z -8.7) |
| [[A-427 (line)]] | wt | 282 | 2 | 1 | [[Harringtonine (drug)]] 5 µM 1.80× (z +9.8) | [[Panobinostat (drug)]] 0.5 µM 0.594× (z -9.0) |
| [[SW48 (line)]] | wt | 169 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +12.2) | — |
| [[SW 1271 (line)]] | alt | 366 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.329× (z -8.8) |
| [[AN3 CA (line)]] | alt | 269 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.270× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[CHP-212 (line)]] | wt | 143 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +10.7) | — |
| [[SNU-1 (line)]] | wt | 234 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +9.2) | — |
| [[hTERT-HPNE (line)]] | wt | 129 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 245 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 220 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 292 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 168 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12584), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEC62]] | +0.71 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[NFKBIB]] | +0.70 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[DNAJC21]] | +0.69 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[WBP4]] | +0.67 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[UBXN2A]] | +0.63 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[SMDT1]] | +0.62 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[NCOA1]] | +0.62 | +0.65 / +0.53 | both halves | 1e-05 |  |
| [[NR1D2]] | +0.62 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[ZDHHC1]] | +0.61 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[GKAP1]] | +0.61 | +0.60 / +0.48 | both halves | 2e-05 |  |
| [[PPIG]] | +0.61 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[RAB13]] | +0.61 | +0.49 / +0.65 | both halves | 1e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PMPCA]] | -0.64 | -0.50 / -0.64 | both halves | 1e-05 |  |
| [[ATP5F1B]] | -0.64 | -0.66 / -0.55 | both halves | 1e-05 |  |
| [[PAICS]] | -0.62 | -0.65 / -0.53 | both halves | 1e-05 |  |
| [[BLTP2]] | -0.60 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[PDCD6]] | -0.60 | -0.49 / -0.62 | both halves | 1e-05 | same gene group |
| [[SAR1A]] | -0.59 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[SNHG30]] | -0.58 | -0.43 / -0.65 | both halves | 3e-05 |  |
| [[P3H1]] | -0.57 | -0.43 / -0.58 | both halves | 3e-05 |  |
| [[RNF4]] | -0.56 | -0.42 / -0.54 | both halves | 4e-05 |  |
| [[DCAF13]] | -0.56 | -0.46 / -0.53 | both halves | 2e-05 |  |
| [[AMPD2]] | -0.55 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[COLGALT1]] | -0.55 | -0.45 / -0.51 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TLCD5]] | B | TLCD5 activity raises ITSN2's level | lines that do not express TLCD5 (5) vs lines expressing it (45) | 1.50× lower at baseline in the lines without TLCD5 | 0.022 | ⚠ within organs, on part of the lines; also absent: DNAJB5, SYDE2, CEP170; maybe low, not absent |
| [[PKD1L2]] | B | PKD1L2 activity raises ITSN2's level | lines that do not express PKD1L2 (13) vs lines expressing it (37) | 1.36× lower at baseline in the lines without PKD1L2 | 0.046 | ⚠ within organs, on part of the lines; also absent: SPDYE10; maybe low, not absent |
| [[MCOLN3]] | B | MCOLN3 activity raises ITSN2's level | lines that do not express MCOLN3 (18) vs lines expressing it (32) | 1.28× lower at baseline in the lines without MCOLN3 | 0.075 | ⚠ within organs, on part of the lines; also absent: PNMA2, STOX2, NTN1 |
| [[DUSP8]] | C | DUSP8 activity raises ITSN2's level | lines that do not express DUSP8 (4) vs lines expressing it (46) | 1.48× lower at baseline in the lines without DUSP8 | 0.057 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: FAM241B, BTG3-AS1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **-** arm (projection on the module's main direction -0.521). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-0.8, -27.4); signed map (4.0, -12.1). **Vector** length 118, 43.5% of its response variance represented; |z| ≥ 3 in 1,523 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +9.1 | +28.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | +8.1 | +19.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +6.9 | -5.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +6.6 | +8.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +6.6 | -3.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +5.5 | +1.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +5.5 | +0.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.3 | +5.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.0 | -1.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +4.7 | +1.6 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -7.9 | -5.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.6 | -7.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -4.5 | -3.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.5 | -4.7 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -4.2 | -1.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.8 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | intersectin 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p23.3 — chr2:24,202,864-24,360,536 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1256, SWAP, SH3P18, SWA, PRO2015; previously SH3D1B |
| Gene groups (HGNC) | Dbl family Rho GEFs; C2 domain containing; EF-hand domain containing; SH3 domain containing |
| Reactome | 8 pathways, smallest: RHOU GTPase cycle; Cargo recognition for clathrin-mediated endocytosis; Clathrin-mediated endocytosis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NZM3](https://www.uniprot.org/uniprotkb/Q9NZM3) (Intersectin-2):

> Adapter protein that may provide indirect link between the endocytic membrane traffic and the actin assembly machinery. May regulate the formation of clathrin-coated vesicles (CCPs). Seems to be involved in CCPs maturation including invagination or budding. Involved in endocytosis of integrin beta-1 (ITGB1) and transferrin receptor (TFR). Plays a role in dendrite formation by melanocytes.

**Summary**, from NCBI Gene [50618](https://www.ncbi.nlm.nih.gov/gene/50618):

> This gene encodes a cytoplasmic protein which contains SH3 domains. This protein is a member of a family of proteins involved in clathrin-mediated endocytosis. Intersectin 2 is thought to regulate the formation of clathrin-coated vesicles and also may function in the induction of T cell antigen receptor (TCR) endocytosis. [provided by RefSeq, Jan 2017]

**Accessions** — [HGNC:6184](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6184) · Entrez [50618](https://www.ncbi.nlm.nih.gov/gene/50618) · UniProt [Q9NZM3](https://www.uniprot.org/uniprotkb/Q9NZM3) · Ensembl [ENSG00000198399](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198399)

## Data

Gene col 12584: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12584); `tables/drug_effects.parquet` (61 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12584, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12584]; `tensor/DDL_lfc|DDL_z.npy` [12584]; `embed/gene_vectors.npy` [12584]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12584 or target_col == 12584). Every well: [[ITSN2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ITSN2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
