---
symbol: "ARHGAP26"
type: "gene"
col: 7030
ensembl_id: "ENSG00000145819"
name: "Rho GTPase activating protein 26"
location: "5q31.3"
module: 141
arm: "+"
pooled_cpm: 297.7
n_lines_expressing: 44
n_dd_up: 24
n_dd_down: 6
n_dd_up_clean: 17
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 11
direction_downstream: 13
tags: ["gene", "module/141"]
generated_by: "tahoemap"
---

# ARHGAP26

*Rho GTPase activating protein 26* — 5q31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.38× (z +36.5, q 0e+00, up in 38 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (5 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 0.584× (z -11.0, q 3e-25, down in 31 of 41 measured lines) ⚠ toxic. The strongest without an alert is [[NG25 (drug)]] 5 µM: 0.675× (z -4.4, q 0.001, down in 20 of 41 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 19 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 8 lines (A549 0.130×, A498 0.185×, KATO III 0.247×, SW480 0.322×, …; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (A549 0.131×, NCI-H2030 0.266×, SW1417 0.455×; ⚠ cell-cycle shift, explains ~61% of this change); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (A549 0.109×, A498 0.177×, KATO III 0.251×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (A549 0.278×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A549 0.292×); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (A549 0.428×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PMEPA1]] (+0.59, fdr 1e-05), [[EML4]] (+0.58, fdr 3e-05), [[ITGA6]] (+0.57, fdr 2e-05); moves opposite to [[ZNF343]] (-0.61, fdr 1e-05), [[VPS33A]] (-0.58, fdr 2e-05), [[CWF19L1]] (-0.57, fdr 1e-05).
> It is in [[Module 141]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[ATP1B1]] → it (grade B ⚠); 13 go from it, the strongest it → cells under [[Homoharringtonine (drug)]] 0.5 µM (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 14 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7030.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.38×** | +36.5 | 0e+00 | 38/42 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **5.28×** | +35.3 | 0e+00 | 41/42 (HOP62, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **4.22×** | +30.5 | 0e+00 | 40/42 (HOP62, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.73×** | +27.9 | 0e+00 | 40/42 (HOP62, J82, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.84×** | +18.3 | 0e+00 | 36/42 (HOP62, NCI-H2347, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **2.38×** | +17.7 | 0e+00 | 38/42 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.22×** | +16.9 | 0e+00 | 32/42 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.15×** | +16.2 | 0e+00 | 38/42 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.09×** | +15.6 | 0e+00 | 38/42 (HOP62, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.89×** | +13.4 | 2e-39 | 32/42 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.84×** | +12.5 | 6e-34 | 34/41 (NCI-H460, HOP62, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.69×** | +11.1 | 5e-27 | 33/42 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.67×** | +10.9 | 8e-26 | 31/42 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.66×** | +10.7 | 5e-25 | 32/43 (HOP62, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.50×** | +10.1 | 1e-22 | 36/43 (SW480, SW1417, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.32×** | +5.8 | 2e-07 | 19/42 (NCI-H460, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.19× | +5.2 | 5e-06 | 17/42 (HOP62, SNU-423, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 10 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7030.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 19 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 8 lines (A549 0.130×, A498 0.185×, KATO III 0.247×, SW480 0.322×, …; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (A549 0.131×, NCI-H2030 0.266×, SW1417 0.455×; ⚠ cell-cycle shift, explains ~61% of this change); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (A549 0.109×, A498 0.177×, KATO III 0.251×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (A549 0.278×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A549 0.292×); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (A549 0.428×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.584×** | -11.0 | 3e-25 | 31/41 (A549, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.610×** | -10.1 | 2e-21 | 26/39 (A549, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.626×** | -9.9 | 6e-21 | 32/43 (A549, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.634×** | -8.9 | 6e-17 | 22/39 (KATO III, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[NG25 (drug)]] 5 µM |  | **0.675×** | -4.4 | 0.001 | 20/41 (A498, A549, …) | top dose only | cell-cycle shift (explains ~14% here); noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.836× | -3.8 | 0.014 | 23/42 (A549, LS 180, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~0% of this change | 0.841× | -3.7 | 0.019 | 20/42 (PANC-1, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Trametinib (drug)]] 0.5 µM |  | 0.859× | -3.6 | 0.020 | 17/42 (A549, SHP-77, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 0.838× | -3.6 | 0.020 | 18/42 (A549, HepG2/C3A, …) | rises with dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.895× | -3.3 | 0.043 | 9/42 (A498, SK-MEL-2, …) | top dose only |  |
| [[Sulfatinib (drug)]] 5 µM |  | 0.849× | -3.3 | 0.043 | 13/43 (NCI-H2347, HS-578T, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.742×** | -3.3 | 0.043 | 15/33 (A549, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | 0.857× | -3.3 | 0.046 | 17/42 (HOP62, Hs 766T, …) | top dose only |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | 0.868× | -3.2 | 0.051 | 17/44 (A549, SHP-77, …) | rises with dose | noisy plate (z scaled) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 0.860× | -3.2 | 0.051 | 13/42 (SW48, SW 1088, …) | top dose only |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | 0.865× | -3.1 | 0.072 | 14/42 (NCI-H1792, Hs 766T, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.37 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7030. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 1,330 | 0 | 29 (17 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.131× (z -31.7) ⚠ cell-cycle shift, explains ~61% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.278× (z -14.2) |
| [[SHP-77 (line)]] | alt | 412 | 18 | 2 (2 ⚠) | [[Budesonide (drug)]] 5 µM 3.24× (z +11.7) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.346× (z -10.2) ⚠ toxic |
| [[HOP62 (line)]] | alt | 108 | 18 (4 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 12.3× (z +37.8) | [[Dexamethasone (drug)]] 0.5 µM 0.448× (z -8.6) |
| [[NCI-H460 (line)]] | wt | 111 | 18 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 13.0× (z +39.1) | — |
| [[SW480 (line)]] | alt | 321 | 14 (2 ⚠) | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +25.3) | [[Dinaciclib (drug)]] 5 µM 0.322× (z -17.2) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 172 | 14 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.42× (z +26.7) | [[Dinaciclib (drug)]] 0.5 µM 0.430× (z -10.8) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 119 | 14 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.99× (z +27.5) | — |
| [[KATO III (line)]] | alt | 422 | 5 | 7 (6 ⚠) | [[Panobinostat (drug)]] 5 µM 3.77× (z +18.1) | [[Dinaciclib (drug)]] 0.5 µM 0.251× (z -18.9) ⚠ toxic; transcription drop · without an alert: [[Ponatinib (drug)]] 5 µM 0.538× (z -8.5) |
| [[SNU-423 (line)]] | alt | 112 | 12 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.61× (z +27.0) | — |
| [[SW 900 (line)]] | alt | 119 | 12 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.66× (z +25.6) | — |
| [[SW1417 (line)]] | alt | 430 | 8 | 4 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 5.75× (z +22.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.455× (z -14.7) ⚠ cell-cycle shift, explains ~61% of this change |
| [[HEC-1-A (line)]] | alt | 256 | 8 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +22.1) | [[Dinaciclib (drug)]] 0.5 µM 0.459× (z -10.1) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 365 | 9 (1 ⚠) | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 5.27× (z +17.4) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.354× (z -10.6) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 189 | 10 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 4.51× (z +22.2) | [[Triamcinolone (drug)]] 5 µM 0.530× (z -9.4) |
| [[PANC-1 (line)]] | alt | 386 | 6 | 5 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +19.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.548× (z -13.4) ⚠ cell-cycle shift, explains ~61% of this change |
| [[SW48 (line)]] | wt | 144 | 11 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.42× (z +16.2) | — |
| [[A498 (line)]] | wt | 364 | 4 | 6 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +16.8) | [[Dinaciclib (drug)]] 0.5 µM 0.177× (z -19.9) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 312 | 10 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.27× (z +29.4) | — |
| [[HS-578T (line)]] | alt | 156 | 10 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.17× (z +27.1) | — |
| [[HT-29 (line)]] | alt | 459 | 5 | 5 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.48× (z +20.7) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.275× (z -14.6) ⚠ toxic |
| [[Panc 03.27 (line)]] | alt | 582 | 5 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +15.9) | [[Dinaciclib (drug)]] 5 µM 0.231× (z -15.3) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 97.1 | 8 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.10× (z +22.9) | — |
| [[Hs 766T (line)]] | wt | 212 | 6 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +14.7) | [[Budesonide (drug)]] 0.5 µM 0.378× (z -10.2) |
| [[SK-MEL-2 (line)]] | alt | 239 | 6 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 7.57× (z +21.1) | [[Dinaciclib (drug)]] 0.5 µM 0.354× (z -10.9) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 291 | 3 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +15.7) | [[Dinaciclib (drug)]] 5 µM 0.203× (z -15.1) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 516 | 4 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +17.7) | [[Dinaciclib (drug)]] 0.5 µM 0.302× (z -13.4) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 180 | 6 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.83× (z +23.8) | [[Dinaciclib (drug)]] 5 µM 0.304× (z -11.0) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 544 | 1 | 5 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.239× (z -16.1) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 899 | 1 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.236× (z -14.7) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 97.1 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 4.54× (z +12.9) | — |
| [[NCI-H23 (line)]] | alt | 82.5 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 5.96× (z +16.5) | — |
| [[RPMI-7951 (line)]] | alt | 75.2 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 9.30× (z +15.7) | — |
| [[AN3 CA (line)]] | alt | 147 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.63× (z +16.4) | — |
| [[COLO 205 (line)]] | alt | 1,154 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +9.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.338× (z -13.3) ⚠ cell-cycle shift, explains ~61% of this change |
| [[hTERT-HPNE (line)]] | wt | 114 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.98× (z +18.8) | — |
| [[SNU-1 (line)]] | wt | 81.0 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.06× (z +18.1) | — |
| [[C-33 A (line)]] | alt | 115 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.57× (z +12.5) | — |
| [[CHP-212 (line)]] | wt | 107 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 5.40× (z +8.9) | — |
| [[NCI-H2030 (line)]] | alt | 465 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.266× (z -16.2) ⚠ cell-cycle shift, explains ~61% of this change |
| [[SW 1271 (line)]] | alt | 185 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.39× (z +12.7) | [[Dinaciclib (drug)]] 0.5 µM 0.0781× (z -12.3) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 158 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.13× (z +11.4) | — |
| [[A-427 (line)]] | wt | 66.2 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 65.6 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 66.6 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 69.4 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 53.7 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 264 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 267 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 79.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 73.0 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7030), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*59 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PMEPA1]] | +0.59 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[EML4]] | +0.58 | +0.43 / +0.56 | both halves | 3e-05 |  |
| [[ITGA6]] | +0.57 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[PRKCA]] | +0.56 | +0.47 / +0.60 | both halves | 2e-05 |  |
| [[ECE1]] | +0.55 | +0.43 / +0.47 | both halves | 3e-05 |  |
| [[MAGI1]] | +0.55 | +0.46 / +0.56 | both halves | 3e-05 |  |
| [[VDR]] | +0.54 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[NFE2L3]] | +0.54 | +0.51 / +0.45 | both halves | 3e-05 |  |
| [[ATP1B1]] | +0.54 | +0.46 / +0.58 | both halves | 2e-05 |  |
| [[HIVEP3]] | +0.54 | +0.42 / +0.50 | both halves | 4e-05 |  |
| [[BAIAP2L1]] | +0.53 | +0.33 / +0.57 | both halves | 1e-04 | same gene group; pathway: RAC1 GTPase cycle |
| [[GMDS]] | +0.53 | +0.46 / +0.47 | both halves | 3e-05 |  |

## Genes that move opposite

*41 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF343]] | -0.61 | -0.56 / -0.56 | both halves | 1e-05 |  |
| [[VPS33A]] | -0.58 | -0.48 / -0.57 | both halves | 2e-05 |  |
| [[CWF19L1]] | -0.57 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[ZNF133]] | -0.55 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[ZNF383]] | -0.53 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[EIF4ENIF1]] | -0.52 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[ZNF708]] | -0.52 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[SUPV3L1]] | -0.52 | -0.43 / -0.49 | both halves | 4e-05 |  |
| [[PARL]] | -0.51 | -0.51 / -0.46 | both halves | 2e-05 |  |
| [[MIGA1]] | -0.51 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[LRRC47]] | -0.51 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[BRAP]] | -0.50 | -0.44 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 11, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ATP1B1]] | B | ATP1B1 activity raises ARHGAP26's level | lines that do not express ATP1B1 (8) vs lines expressing it (42) | 2.69× lower at baseline in the lines without ATP1B1 | 0.004 | ⚠ within organs, on part of the lines; also absent: PYROXD2, IL15, IER3; maybe low, not absent |
| [[TNFRSF21]] | B | TNFRSF21 activity raises ARHGAP26's level | lines that do not express TNFRSF21 (15) vs lines expressing it (35) | 2.33× lower at baseline in the lines without TNFRSF21 | 0.013 | ⚠ within organs, on part of the lines; also absent: ENSG00000256982, SORL1, THRB; maybe low, not absent |
| [[PPARG]] | B | PPARG activity raises ARHGAP26's level | lines that do not express PPARG (20) vs lines expressing it (30) | 2.20× lower at baseline in the lines without PPARG | 0.033 | ⚠ within organs, on part of the lines; also absent: ENSG00000271933, LINC01589, NUP62CL |
| [[ARHGAP18]] | B | ARHGAP18 activity raises ARHGAP26's level | lines that do not express ARHGAP18 (6) vs lines expressing it (44) | 2.52× lower at baseline in the lines without ARHGAP18 | 0.039 | ⚠ within organs, on part of the lines; also absent: IER3, SLC2A1, SHB |
| [[AHR]] | B | AHR activity raises ARHGAP26's level | lines that do not express AHR (7) vs lines expressing it (43) | 2.48× lower at baseline in the lines without AHR | 0.041 | ⚠ within organs, on part of the lines; also absent: ENSG00000283321, VDR, GPR39 |
| [[IER3]] | B | IER3 activity raises ARHGAP26's level | lines that do not express IER3 (5) vs lines expressing it (45) | 2.60× lower at baseline in the lines without IER3 | 0.050 | ⚠ within organs, on part of the lines; also absent: ARHGAP18, SLC2A1, SHB |
| [[PCED1B]] | B | PCED1B activity raises ARHGAP26's level | lines that do not express PCED1B (11) vs lines expressing it (39) | 2.19× lower at baseline in the lines without PCED1B | 0.055 | ⚠ within organs, on part of the lines; also absent: AMIGO2, CXCL3, PRDM1 |
| [[TSPAN15]] | B | TSPAN15 activity raises ARHGAP26's level | lines that do not express TSPAN15 (15) vs lines expressing it (35) | 2.26× lower at baseline in the lines without TSPAN15 | 0.064 | ⚠ within organs, on part of the lines; also absent: RBM47, ENSG00000287306, JUP; maybe low, not absent |
| [[PLS1]] | B | PLS1 activity raises ARHGAP26's level | lines that do not express PLS1 (14) vs lines expressing it (36) | 2.16× lower at baseline in the lines without PLS1 | 0.065 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: NRARP, MYO5C, MLXIPL |
| [[PMEPA1]] | B | PMEPA1 activity raises ARHGAP26's level | lines that do not express PMEPA1 (6) vs lines expressing it (44) | 1.87× lower at baseline in the lines without PMEPA1 | 0.083 | ⚠ within organs, on part of the lines; also absent: SOX4, SLC2A1-DT, ENSG00000285253 |
| [[CA8]] | B | CA8 activity raises ARHGAP26's level | lines that do not express CA8 (27) vs lines expressing it (23) | 1.24× lower at baseline in the lines without CA8 | 0.089 | ⚠ within organs, on part of the lines; also absent: STK32B, NKAIN3, CNKSR2 |

### Downstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 13, C 0. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Homoharringtonine (drug)]] 0.5 µM | B | ARHGAP26 activity raises the cells' numbers under Homoharringtonine 0.5 µM (protects the cells) | lines that do not express ARHGAP26 (6) vs lines expressing it (42) | the lines without ARHGAP26: 0.32× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: SSUH2, ADM2, TBC1D8; maybe low, not absent |
| cells under [[Homoharringtonine (drug)]] 0.05 µM | B | ARHGAP26 activity raises the cells' numbers under Homoharringtonine 0.05 µM (protects the cells) | lines that do not express ARHGAP26 (6) vs lines expressing it (42) | the lines without ARHGAP26: 0.66× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: SSUH2, ADM2, TBC1D8; maybe low, not absent |
| [[JAG1]] | B | ARHGAP26 activity raises JAG1's level | lines that do not express ARHGAP26 (6) vs lines expressing it (44) | 2.39× lower at baseline in the lines without ARHGAP26 | 0.034 | ⚠ within organs, on part of the lines; also absent: SSUH2, ADM2, TBC1D8; maybe low, not absent |
| [[VDR]] | B | ARHGAP26 activity raises VDR's level | lines that do not express ARHGAP26 (6) vs lines expressing it (44) | 2.08× lower at baseline in the lines without ARHGAP26 | 0.049 | ⚠ within organs, on part of the lines; also absent: SSUH2, ADM2, TBC1D8; maybe low, not absent |
| [[PPP3CA]] | B | ARHGAP26 activity raises PPP3CA's level | lines that do not express ARHGAP26 (6) vs lines expressing it (44) | 1.91× lower at baseline in the lines without ARHGAP26 | 0.049 | ⚠ within organs, on part of the lines; also absent: SSUH2, ADM2, TBC1D8; maybe low, not absent |
| [[PCED1B]] | B | ARHGAP26 activity raises PCED1B's level | lines that do not express ARHGAP26 (6) vs lines expressing it (44) | 3.86× lower at baseline in the lines without ARHGAP26 | 0.049 | ⚠ within organs, on part of the lines; also absent: SSUH2, ADM2, TBC1D8; maybe low, not absent |
| [[TSPAN15]] | B | ARHGAP26 activity raises TSPAN15's level | lines that do not express ARHGAP26 (6) vs lines expressing it (44) | 3.20× lower at baseline in the lines without ARHGAP26 | 0.049 | ⚠ within organs, on part of the lines; also absent: SSUH2, ADM2, TBC1D8; maybe low, not absent |
| cells under [[Harringtonine (drug)]] 0.5 µM | B | ARHGAP26 activity raises the cells' numbers under Harringtonine 0.5 µM (protects the cells) | lines that do not express ARHGAP26 (6) vs lines expressing it (42) | the lines without ARHGAP26: 0.43× the cells of the other lines | 0.052 | ⚠ within organs, on part of the lines; also absent: SSUH2, ADM2, TBC1D8; maybe low, not absent |
| cells under [[Topotecan (hydrochloride) (drug)]] 5 µM | B | ARHGAP26 activity raises the cells' numbers under Topotecan (hydrochloride) 5 µM (protects the cells) | lines that do not express ARHGAP26 (6) vs lines expressing it (42) | the lines without ARHGAP26: 0.47× the cells of the other lines | 0.056 | ⚠ within organs, on part of the lines; also absent: SSUH2, ADM2, TBC1D8; maybe low, not absent |
| cells under [[Homoharringtonine (drug)]] 5 µM | B | ARHGAP26 activity raises the cells' numbers under Homoharringtonine 5 µM (protects the cells) | lines that do not express ARHGAP26 (6) vs lines expressing it (42) | the lines without ARHGAP26: 0.30× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: SSUH2, ADM2, TBC1D8; maybe low, not absent |
| [[SMAD3]] | B | ARHGAP26 activity raises SMAD3's level | lines that do not express ARHGAP26 (6) vs lines expressing it (44) | 1.90× lower at baseline in the lines without ARHGAP26 | 0.075 | ⚠ within organs, on part of the lines; also absent: SSUH2, ADM2, TBC1D8; maybe low, not absent |
| cells under [[Harringtonine (drug)]] 5 µM | B | ARHGAP26 activity raises the cells' numbers under Harringtonine 5 µM (protects the cells) | lines that do not express ARHGAP26 (6) vs lines expressing it (42) | the lines without ARHGAP26: 0.34× the cells of the other lines | 0.094 | ⚠ within organs, on part of the lines; also absent: SSUH2, ADM2, TBC1D8; maybe low, not absent |

## Where it sits

- **Module**: [[Module 141]] — TNF-alpha signaling via NF-kB; 33 genes; every member is in the + arm (projection on the module's main direction 0.476). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-14.4, 27.8); signed map (1.9, 42.5). **Vector** length 117, 35.9% of its response variance represented; |z| ≥ 3 in 1,807 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +11.5 | +18.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +8.4 | +10.7 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +6.2 | +15.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +5.1 | +12.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.6 | +13.4 |
|  | [[Vilanterol (drug)]] 0.5 µM |  | +2.4 | +1.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.4 | +10.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.2 | +4.8 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.1 | +1.9 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -8.7 | -11.0 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -8.0 | -1.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -6.2 | +0.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -5.6 | -2.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.6 | -3.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.2 | +0.4 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -4.0 | -2.8 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -3.7 | -1.8 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.5 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | Rho GTPase activating protein 26 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q31.3 — chr5:142,770,377-143,229,011 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GRAF, KIAA0621, OPHN1L, OPHN1L1 |
| Gene groups (HGNC) | AH/BAR family Rho GTPase activating proteins; SH3 domain containing |
| Reactome | 13 pathways, smallest: RHOD GTPase cycle; RHOJ GTPase cycle; RHOQ GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UNA1](https://www.uniprot.org/uniprotkb/Q9UNA1) (Rho GTPase-activating protein 26):

> GTPase-activating protein for RHOA and CDC42. Facilitates mitochondrial quality control by promoting Parkin-mediated recruitment of autophagosomes to damaged mitochondria. Negatively regulates the growth of human parainfluenza virus type 2 by inhibiting hPIV-2-mediated RHOA activation via interaction with two of its viral proteins P and V.; [Isoform 2]: Associates with MICAL1 on the endosomal membrane to promote Rab8-Rab10-dependent tubule extension. After dissociation of MICAL1, recruits WDR44 …

**Summary**, from NCBI Gene [23092](https://www.ncbi.nlm.nih.gov/gene/23092):

> Interaction of a cell with the extracellular matrix triggers integrin cell surface receptors to begin signaling cascades that regulate the organization of the actin-cytoskeleton. One of the proteins involved in these cascades is focal adhesion kinase. The protein encoded by this gene is a GTPase activating protein that binds to focal adhesion kinase and mediates the activity of the GTP binding proteins RhoA and Cdc42. Defects in this gene are a cause of juvenile myelomonocytic leukemia (JMML). …

**Accessions** — [HGNC:17073](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17073) · Entrez [23092](https://www.ncbi.nlm.nih.gov/gene/23092) · UniProt [Q9UNA1](https://www.uniprot.org/uniprotkb/Q9UNA1) · Ensembl [ENSG00000145819](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000145819)

## Data

Gene col 7030: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7030); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7030, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7030]; `tensor/DDL_lfc|DDL_z.npy` [7030]; `embed/gene_vectors.npy` [7030]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7030 or target_col == 7030). Every well: [[ARHGAP26 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARHGAP26.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
