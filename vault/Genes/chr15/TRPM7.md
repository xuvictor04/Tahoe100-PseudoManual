---
symbol: "TRPM7"
type: "gene"
col: 1699
ensembl_id: "ENSG00000092439"
name: "transient receptor potential cation channel subfamily M member 7"
location: "15q21.2"
module: 59
arm: "+"
pooled_cpm: 221.24
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 9
n_dd_up_clean: 12
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/059"]
generated_by: "tahoemap"
---

# TRPM7

*transient receptor potential cation channel subfamily M member 7* — 15q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.56× (z +25.0, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.468× (z -13.2, q 3e-37, down in 43 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 0.835× (z -4.8, q 2e-04, down in 23 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 6 lines (NCI-H460 0.325×, CFPAC-1 0.346×, RKO 0.308×, NCI-H1792 0.372×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (SK-MEL-2 0.0691×, CFPAC-1 0.318×, NCI-H23 0.308×, C-33 A 0.307×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (RKO 0.345×, CFPAC-1 0.395×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (SNU-1 0.486×); [[Oxaprozin (drug)]] 0.5 µM in 1 line (SW 1088 0.118×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FLCN]] (+0.70, fdr 7e-06), [[MITD1]] (+0.68, fdr 7e-06), [[LRRC37B]] (+0.64, fdr 1e-05); moves opposite to [[CDC42EP2]] (-0.60, fdr 1e-05), [[ASPH]] (-0.56, fdr 1e-05), [[AMOTL1]] (-0.55, fdr 2e-05).
> It sits in the **+** arm of [[Module 059]] (Amino acids regulate mTORC1).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1699.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.56×** | +25.0 | 0e+00 | 46/48 (NCI-H2347, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.23×** | +15.1 | 0e+00 | 45/48 (COLO 205, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.90×** | +12.1 | 4e-31 | 42/48 (NCI-H460, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.78×** | +10.5 | 2e-23 | 44/48 (NCI-H2347, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.65×** | +9.4 | 5e-19 | 42/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.50×** | +8.9 | 7e-17 | 42/49 (COLO 205, NCI-H2347, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.51×** | +7.8 | 6e-13 | 37/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.51×** | +7.8 | 6e-13 | 41/48 (NCI-H460, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.36×** | +5.8 | 5e-07 | 37/48 (NCI-H2347, NCI-H2030, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.35×** | +5.6 | 1e-06 | 38/48 (CFPAC-1, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.21×** | +5.0 | 2e-05 | 24/48 (CFPAC-1, Panc 03.27, …) | all doses, stronger at high dose | low cells (technical?) |
| [[PH-797804 (drug)]] 5 µM |  | **1.49×** | +3.9 | 0.005 | 27/48 (HEC-1-A, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.48×** | +3.8 | 0.006 | 31/49 (A-427, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.23×** | +3.7 | 0.008 | 25/48 (AsPC-1, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.21×** | +3.6 | 0.013 | 24/49 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Tomivosertib (drug)]] 5 µM |  | **1.44×** | +3.5 | 0.015 | 24/48 (MIA PaCa-2, NCI-H1792, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.37×** | +3.1 | 0.062 | 22/48 (NCI-H1573, Hs 766T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 1.17× | +3.0 | 0.065 | 17/48 (MIA PaCa-2, Hs 766T, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.11× | +2.9 | 0.100 | 9/49 (NCI-H1573, A-172, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 13 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1699.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 6 lines (NCI-H460 0.325×, CFPAC-1 0.346×, RKO 0.308×, NCI-H1792 0.372×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (SK-MEL-2 0.0691×, CFPAC-1 0.318×, NCI-H23 0.308×, C-33 A 0.307×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (RKO 0.345×, CFPAC-1 0.395×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (SNU-1 0.486×); [[Oxaprozin (drug)]] 0.5 µM in 1 line (SW 1088 0.118×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.468×** | -13.2 | 3e-37 | 43/45 (NCI-H460, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.507×** | -12.3 | 2e-32 | 39/44 (SK-MEL-2, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~25% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.536×** | -11.7 | 1e-29 | 47/49 (RKO, CFPAC-1, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.775×** | -4.8 | 2e-04 | 30/48 (SW480, CFPAC-1, …) | all doses, flat |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.835× | -4.8 | 2e-04 | 23/48 (SNU-1, HEC-1-A, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.806×** | -4.1 | 0.005 | 24/48 (SW480, Panc 03.27, …) | all doses, flat |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~45% of this change | **0.811×** | -3.9 | 0.006 | 28/48 (NCI-H661, NCI-H2030, …) | inconsistent across doses | low cells (technical?) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.817×** | -3.8 | 0.011 | 26/48 (A498, NCI-H1573, …) | inconsistent across doses |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.819×** | -3.8 | 0.011 | 28/48 (A498, NCI-H1573, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.876× | -3.5 | 0.025 | 10/48 (SW480, LOX-IMVI, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.949× | -3.4 | 0.029 | 0/50 | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | 0.834× | -3.4 | 0.029 | 22/48 (SW480, PANC-1, …) | all doses, flat |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | 0.880× | -3.4 | 0.029 | 4/48 (A-172, NCI-H1573, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | 0.835× | -3.4 | 0.029 | 20/48 (NCI-H1573, SNU-1, …) | two highest doses |  |
| [[Busulfan (drug)]] 0.05 µM |  | 0.838× | -3.3 | 0.033 | 23/49 (A498, NCI-H1573, …) | inconsistent across doses |  |
| [[Larotrectinib (drug)]] 0.05 µM |  | 0.849× | -3.1 | 0.064 | 19/49 (A498, A-172, …) | inconsistent across doses |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | 0.849× | -3.1 | 0.064 | 16/48 (hTERT-HPNE, A498, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1699. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 202 | 14 (5 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.78× (z +31.2) | [[Dinaciclib (drug)]] 0.05 µM 0.325× (z -13.0) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 288 | 6 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.38× (z +22.4) | [[Dinaciclib (drug)]] 0.5 µM 0.433× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[SNU-1 (line)]] | wt | 320 | 6 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +13.9) | [[Dinaciclib (drug)]] 0.05 µM 0.329× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.486× (z -11.9) |
| [[NCI-H2347 (line)]] | alt | 136 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.04× (z +31.5) | — |
| [[AsPC-1 (line)]] | alt | 139 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.71× (z +28.2) | — |
| [[COLO 205 (line)]] | alt | 205 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.66× (z +27.9) | — |
| [[HEC-1-A (line)]] | alt | 212 | 4 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +22.6) | [[Dinaciclib (drug)]] 5 µM 0.451× (z -12.2) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 202 | 4 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.99× (z +22.0) | [[Dinaciclib (drug)]] 5 µM 0.350× (z -11.3) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 243 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.54× (z +23.7) | [[Dinaciclib (drug)]] 5 µM 0.400× (z -9.8) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 189 | 3 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +11.4) | [[Dinaciclib (drug)]] 0.05 µM 0.403× (z -11.9) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 377 | 1 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +16.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.480× (z -11.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 117 | 5 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.45× (z +16.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.84× (z +16.2) | — |
| [[CFPAC-1 (line)]] | alt | 241 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +16.9) | [[Dinaciclib (drug)]] 5 µM 0.318× (z -14.5) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 143 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +16.7) | — |
| [[hTERT-HPNE (line)]] | wt | 204 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +14.9) | [[Lonafarnib (drug)]] 5 µM 0.102× (z -11.2) ⚠ toxic |
| [[J82 (line)]] | alt | 279 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +17.7) | [[Dinaciclib (drug)]] 5 µM 0.418× (z -9.1) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 212 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +19.9) | — |
| [[RKO (line)]] | wt | 300 | 3 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +15.2) | [[Dinaciclib (drug)]] 0.05 µM 0.308× (z -12.9) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 151 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +15.4) | [[Dinaciclib (drug)]] 5 µM 0.416× (z -9.7) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 243 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +15.1) | [[Dinaciclib (drug)]] 0.5 µM 0.403× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[SW480 (line)]] | alt | 185 | 4 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.16× (z +14.1) | [[Dinaciclib (drug)]] 5 µM 0.558× (z -10.2) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 223 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +20.2) | — |
| [[LoVo (line)]] | wt | 283 | 3 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.16× (z +10.9) | [[Dinaciclib (drug)]] 0.5 µM 0.505× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[NCI-H23 (line)]] | alt | 196 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +15.3) | [[Dinaciclib (drug)]] 5 µM 0.308× (z -13.7) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 256 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +15.6) | [[Dinaciclib (drug)]] 0.05 µM 0.436× (z -10.8) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 297 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +12.1) | [[Dinaciclib (drug)]] 0.05 µM 0.339× (z -10.3) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 141 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.75× (z +10.2) | — |
| [[SK-MEL-2 (line)]] | alt | 142 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.65× (z +20.6) | [[Dinaciclib (drug)]] 5 µM 0.0691× (z -29.0) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 221 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.61× (z +17.2) | [[Dinaciclib (drug)]] 0.5 µM 0.323× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[A498 (line)]] | wt | 250 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +11.4) | [[Dinaciclib (drug)]] 0.05 µM 0.334× (z -10.9) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 199 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +13.9) | [[Dinaciclib (drug)]] 0.05 µM 0.351× (z -8.9) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 148 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.56× (z +17.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 261 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +12.0) | [[Dinaciclib (drug)]] 0.5 µM 0.420× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[SNU-423 (line)]] | alt | 265 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +13.3) | [[Dinaciclib (drug)]] 0.05 µM 0.341× (z -9.3) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 386 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.269× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[C-33 A (line)]] | alt | 258 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.307× (z -13.5) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 279 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.371× (z -11.0) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 246 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.372× (z -12.6) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 260 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +19.8) | [[Dinaciclib (drug)]] 5 µM 0.473× (z -9.4) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 211 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +13.8) | — |
| [[C32 (line)]] | wt | 186 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.376× (z -11.1) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 192 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.305× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[HS-578T (line)]] | alt | 165 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +11.7) | — |
| [[LOX-IMVI (line)]] | wt | 214 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.433× (z -9.7) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 184 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +11.6) | — |
| [[SW 1088 (line)]] | alt | 187 | 0 | 1 | — | [[Oxaprozin (drug)]] 0.5 µM 0.118× (z -10.0) |
| [[NCI-H2122 (line)]] | alt | 259 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 220 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 246 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 188 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1699), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FLCN]] | +0.70 | +0.67 / +0.65 | both halves | 7e-06 |  |
| [[MITD1]] | +0.68 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[LRRC37B]] | +0.64 | +0.67 / +0.50 | both halves | 1e-05 |  |
| [[WDSUB1]] | +0.64 | +0.69 / +0.64 | both halves | 7e-06 |  |
| [[TMEM192]] | +0.64 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[RRAGC]] | +0.62 | +0.67 / +0.55 | both halves | 1e-05 |  |
| [[ZCCHC8]] | +0.61 | +0.70 / +0.38 | both halves | 7e-05 |  |
| [[C1orf43]] | +0.61 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[HPS4]] | +0.60 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[ANAPC16]] | +0.60 | +0.64 / +0.53 | both halves | 1e-05 |  |
| [[UVRAG]] | +0.60 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[HPS1]] | +0.59 | +0.51 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDC42EP2]] | -0.60 | -0.66 / -0.51 | both halves | 1e-05 |  |
| [[ASPH]] | -0.56 | -0.56 / -0.49 | both halves | 1e-05 | pathway: Ion channel transport |
| [[AMOTL1]] | -0.55 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[EHD4]] | -0.55 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[PSMD2]] | -0.54 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[ILF2]] | -0.54 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[PCDHGC3]] | -0.53 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[ACTN4]] | -0.53 | -0.50 / -0.42 | both halves | 4e-05 |  |
| [[CORO1C]] | -0.53 | -0.55 / -0.39 | both halves | 6e-05 |  |
| [[ITGB1]] | -0.53 | -0.54 / -0.39 | both halves | 6e-05 |  |
| [[NIBAN2]] | -0.52 | -0.50 / -0.40 | both halves | 5e-05 |  |
| [[ETV3]] | -0.52 | -0.49 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 059]] — Amino acids regulate mTORC1; 80 genes; this gene is in the **+** arm (projection on the module's main direction 0.484). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-19.6, 15.5); signed map (-5.5, 0.5). **Vector** length 113, 44.9% of its response variance represented; |z| ≥ 3 in 1,194 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | +7.4 | +5.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | +7.1 | +5.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +5.7 | +2.1 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~39% of this change | +5.3 | +3.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +4.8 | +2.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.4 | +2.7 |
|  | [[venetoclax (drug)]] 5 µM |  | +4.3 | +2.7 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +4.2 | +1.1 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.1 | -13.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | -4.1 | -4.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.9 | -2.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | -3.8 | -4.1 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | -3.6 | -3.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.3 | +1.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.2 | -3.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.6 | +0.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.4 | -2.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.4 | +3.9 |

## What is on record

|  |  |
|---|---|
| Name | transient receptor potential cation channel subfamily M member 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q21.2 — chr15:50,552,473-50,686,797 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CHAK1, LTRPC7, TRP-PLIK |
| Gene groups (HGNC) | Alpha kinases; Transient receptor potential cation channel subfamily M |
| Reactome | 4 pathways, smallest: TRP channels; Stimuli-sensing channels; Ion channel transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96QT4](https://www.uniprot.org/uniprotkb/Q96QT4) (Transient receptor potential cation channel subfamily M member 7):

> Bifunctional protein that combines an ion channel with an intrinsic kinase domain, enabling it to modulate cellular functions either by conducting ions through the pore or by phosphorylating downstream proteins via its kinase domain. The channel is highly permeable to divalent cations, specifically calcium (Ca2+), magnesium (Mg2+) and zinc (Zn2+) and mediates their influx. Controls a wide range of biological processes such as Ca2(+), Mg(2+) and Zn(2+) homeostasis, vesicular Zn(2+) release …

**Summary**, from NCBI Gene [54822](https://www.ncbi.nlm.nih.gov/gene/54822):

> This gene belongs to the melastatin subfamily of transient receptor potential family of ion channels. The protein encoded by this gene is both an ion channel and a serine/threonine protein kinase. The kinase activity is essential for the ion channel function, which serves to increase intracellular calcium levels and to help regulate magnesium ion homeostasis. The encoded protein is involved in cytoskeletal organization, cell adhesion, cell migration and organogenesis. Defects in this gene are a …

**Accessions** — [HGNC:17994](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17994) · Entrez [54822](https://www.ncbi.nlm.nih.gov/gene/54822) · UniProt [Q96QT4](https://www.uniprot.org/uniprotkb/Q96QT4) · Ensembl [ENSG00000092439](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000092439)

## Data

Gene col 1699: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1699); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1699, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1699]; `tensor/DDL_lfc|DDL_z.npy` [1699]; `embed/gene_vectors.npy` [1699]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1699 or target_col == 1699). Every well: [[TRPM7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRPM7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
