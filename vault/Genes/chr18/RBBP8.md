---
symbol: "RBBP8"
type: "gene"
col: 2171
ensembl_id: "ENSG00000101773"
name: "RB binding protein 8, endonuclease"
location: "18q11.2"
module: 6
arm: "+"
pooled_cpm: 59.34
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 6
n_dd_up_clean: 8
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# RBBP8

*RB binding protein 8, endonuclease* — 18q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.94× (z +27.5, q 0e+00, up in 45 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 1.40× (z +8.2, q 3e-14, up in 27 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.611× (z -6.6, q 2e-08, down in 22 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TIMELESS]] (+0.67, fdr 7e-06), [[HELLS]] (+0.67, fdr 7e-06), [[IPO9]] (+0.64, fdr 1e-05); moves opposite to [[ZNHIT1]] (-0.61, fdr 1e-05), [[HINFP]] (-0.60, fdr 3e-05), [[TTC9C]] (-0.60, fdr 2e-05).
> It sits in the **+** arm of [[Module 006]] (E2F targets).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 45 in all, 22 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2171.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **2.94×** | +27.5 | 0e+00 | 45/49 (NCI-H1573, Panc 03.27, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **2.59×** | +23.4 | 0e+00 | 38/41 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **2.15×** | +18.1 | 0e+00 | 36/44 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.66×** | +12.9 | 1e-35 | 39/48 (PANC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.40×** | +8.2 | 3e-14 | 27/48 (NCI-H1573, MIA PaCa-2, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.36×** | +7.9 | 3e-13 | 32/48 (PANC-1, J82, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.37×** | +7.7 | 8e-13 | 32/48 (NCI-H1573, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[TAK-733 (drug)]] 5 µM |  | **1.63×** | +6.5 | 5e-09 | 22/48 (PANC-1, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~39% of this change | **1.30×** | +6.4 | 8e-09 | 25/47 (C32, NCI-H1573, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.19× | +6.1 | 6e-08 | 22/48 (Panc 03.27, CFPAC-1, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~71% of this change | **1.24×** | +5.4 | 4e-06 | 23/47 (SW480, J82, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.49×** | +5.4 | 4e-06 | 19/48 (MIA PaCa-2, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.49×** | +5.3 | 5e-06 | 19/47 (PANC-1, Panc 03.27, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **1.24×** | +5.3 | 5e-06 | 18/48 (J82, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Raltitrexed (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | 1.15× | +4.9 | 3e-05 | 9/49 (SW480, LS 180, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.40×** | +4.5 | 3e-04 | 17/48 (PANC-1, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Pralsetinib (drug)]] 5 µM |  | **1.39×** | +4.4 | 3e-04 | 16/48 (Panc 03.27, SW480, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.39×** | +4.4 | 3e-04 | 17/48 (J82, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Berbamine (drug)]] 0.05 µM |  | 1.18× | +4.3 | 5e-04 | 7/48 (LoVo, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 1.17× | +3.9 | 0.002 | 14/48 (Panc 03.27, A498, …) | inconsistent across doses |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | 1.15× | +3.5 | 0.009 | 8/49 (NCI-H2122, HOP62, …) | inconsistent across doses |  |
| [[Amsacrine (drug)]] 5 µM |  | 1.10× | +3.4 | 0.012 | 13/48 (J82, SW480, …) | rises with dose |  |
| [[Busulfan (drug)]] 0.05 µM |  | 1.13× | +3.2 | 0.026 | 5/48 (A549, NCI-H1573, …) | inconsistent across doses |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | 1.13× | +3.0 | 0.040 | 1/48 (SW 900) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 8 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2171.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.611×** | -6.6 | 2e-08 | 22/49 (A-427, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.780×** | -6.3 | 7e-08 | 22/48 (CHP-212, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | 0.856× | -5.3 | 2e-05 | 20/48 (Hs 766T, H4, …) | all doses, stronger at high dose | low cells (technical?) |
| [[PH-797804 (drug)]] 5 µM |  | **0.675×** | -5.3 | 2e-05 | 22/48 (A-427, LS 180, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | 0.849× | -4.2 | 0.003 | 12/48 (H4, PANC-1, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.820×** | -4.2 | 0.003 | 14/48 (Hs 766T, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.863× | -3.8 | 0.013 | 16/47 (PANC-1, A-427, …) | top dose only |  |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.798×** | -3.5 | 0.029 | 6/48 (RKO, Panc 03.27, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~19% of this change | 0.870× | -3.4 | 0.049 | 20/48 (SW48, HT-29, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.811×** | -3.3 | 0.058 | 14/48 (MIA PaCa-2, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.909× | -3.3 | 0.058 | 17/47 (NCI-H23, PANC-1, …) | top dose only |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 0.883× | -3.2 | 0.071 | 8/48 (LoVo, HCT15, …) | top dose only |  |
| [[Daidzin (drug)]] 5 µM |  | 0.881× | -3.1 | 0.079 | 3/48 (SW480, NCI-H2347, …) | rises with dose | plate-row cell shift |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | 0.879× | -3.1 | 0.088 | 9/46 (NCI-H661, SNU-1, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~48% of this change | 0.882× | -3.0 | 0.088 | 9/48 (Hs 766T, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 0.889× | -3.0 | 0.091 | 7/48 (RPMI-7951, NCI-H2347, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.46 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2171. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 94.7 | 5 (5 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.64× (z +15.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Digitoxin (drug)]] 5 µM 0.433× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 35.7 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.67× (z +16.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 4.42× (z +12.2) | — |
| [[A-427 (line)]] | wt | 135 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 1.95× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Homoharringtonine (drug)]] 5 µM 0.583× (z -9.8) ⚠ cell-cycle shift, explains ~13% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.280× (z -8.9) |
| [[AN3 CA (line)]] | alt | 47.3 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 6.64× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Pimozide (drug)]] 0.05 µM 0.0853× (z -11.4) |
| [[HEC-1-A (line)]] | alt | 65.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.63× (z +13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[LS 180 (line)]] | wt | 54.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.71× (z +13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[NCI-H2030 (line)]] | alt | 103 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.21× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Homoharringtonine (drug)]] 5 µM 0.585× (z -9.7) ⚠ cell-cycle shift, explains ~13% of this change |
| [[NCI-H23 (line)]] | alt | 81.3 | 1 (1 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.94× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | [[Homoharringtonine (drug)]] 5 µM 0.410× (z -12.7) ⚠ cell-cycle shift, explains ~13% of this change |
| [[NCI-H460 (line)]] | wt | 37.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.88× (z +11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[SW480 (line)]] | alt | 71.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.75× (z +12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[A498 (line)]] | wt | 41.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.28× (z +13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[AsPC-1 (line)]] | alt | 71.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +17.1) ⚠ cell-cycle shift, explains ~13% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.77× (z +10.9) | — |
| [[C32 (line)]] | wt | 30.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.55× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[CFPAC-1 (line)]] | alt | 20.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.14× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[HOP62 (line)]] | alt | 23.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.48× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 24.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.19× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[J82 (line)]] | alt | 72.9 | 2 (2 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 2.09× (z +9.8) ⚠ cell-cycle shift, explains ~49% of this change | — |
| [[KATO III (line)]] | alt | 51.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.29× (z +12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[LoVo (line)]] | wt | 55.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.59× (z +13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[LOX-IMVI (line)]] | wt | 33.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.18× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 40.0 | 2 (2 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 4.00× (z +11.4) ⚠ unreliable plate only | — |
| [[NCI-H1792 (line)]] | alt | 101 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.63× (z +13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[NCI-H2347 (line)]] | alt | 32.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.65× (z +12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[Panc 03.27 (line)]] | alt | 65.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.72× (z +16.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[SNU-423 (line)]] | alt | 25.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.47× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[CHP-212 (line)]] | wt | 23.9 | 0 | 1 | — | [[Resveratrol (drug)]] 0.05 µM 0.0794× (z -8.6) |
| [[HCT15 (line)]] | alt | 40.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.15× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[RPMI-7951 (line)]] | alt | 26.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.48× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 38.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.11× (z +11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[SNU-1 (line)]] | wt | 60.8 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.114× (z -8.6) ⚠ toxic |
| [[SW 900 (line)]] | alt | 30.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.04× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[SW1417 (line)]] | alt | 56.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.62× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[A-172 (line)]] | wt | 39.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 60.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 46.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 121 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 60.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 30.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 34.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 108 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 72.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 78.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 47.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 47.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 57.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 57.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 91.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2171), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TIMELESS]] | +0.67 | +0.62 / +0.66 | both halves | 7e-06 | pathway: DNA Double-Strand Break Repair |
| [[HELLS]] | +0.67 | +0.65 / +0.67 | both halves | 7e-06 |  |
| [[IPO9]] | +0.64 | +0.51 / +0.71 | both halves | 1e-05 | same gene group |
| [[XRCC2]] | +0.64 | +0.61 / +0.64 | both halves | 7e-06 | pathway: DNA Double-Strand Break Repair; STRING 740 |
| [[CLSPN]] | +0.62 | +0.66 / +0.62 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints; STRING 511 |
| [[SMC1A]] | +0.62 | +0.60 / +0.61 | both halves | 7e-06 | same gene group; pathway: Meiosis |
| [[CTPS1]] | +0.62 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[TFDP1]] | +0.61 | +0.53 / +0.63 | both halves | 1e-05 | pathway: Transcriptional Regulation by E2F6; STRING 583 |
| [[CDC7]] | +0.61 | +0.59 / +0.62 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints |
| [[MTHFD1]] | +0.61 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[ZWILCH]] | +0.61 | +0.54 / +0.64 | both halves | 1e-05 | pathway: Cell Cycle Checkpoints |
| [[MYBL2]] | +0.61 | +0.54 / +0.63 | both halves | 1e-05 |  |

## Genes that move opposite

*40 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNHIT1]] | -0.61 | -0.53 / -0.66 | both halves | 1e-05 |  |
| [[HINFP]] | -0.60 | -0.44 / -0.68 | both halves | 3e-05 |  |
| [[TTC9C]] | -0.60 | -0.48 / -0.63 | both halves | 2e-05 |  |
| [[SYF2]] | -0.60 | -0.45 / -0.63 | both halves | 3e-05 |  |
| [[LMBR1L]] | -0.58 | -0.49 / -0.64 | both halves | 1e-05 |  |
| [[CDK7]] | -0.57 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[RSBN1]] | -0.57 | -0.47 / -0.62 | both halves | 2e-05 |  |
| [[ZMAT5]] | -0.56 | -0.39 / -0.57 | both halves | 6e-05 |  |
| [[NOSIP]] | -0.56 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[MRPL43]] | -0.55 | -0.39 / -0.61 | both halves | 6e-05 |  |
| [[ING4]] | -0.55 | -0.52 / -0.61 | both halves | 1e-05 |  |
| [[TSC22D4]] | -0.54 | -0.44 / -0.64 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.557). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-37.1, -41.4); signed map (-35.2, -48.5). **Vector** length 116, 30.9% of its response variance represented; |z| ≥ 3 in 1,098 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +8.9 | +12.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | +8.1 | +7.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | +8.1 | +27.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | +7.9 | +23.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | +6.7 | +18.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.5 | +6.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.1 | +8.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.9 | +5.4 |
|  | [[EX229 (drug)]] 5 µM |  | +3.8 | +4.4 |
|  | [[venetoclax (drug)]] 5 µM |  | +3.7 | +5.3 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | -4.4 | -5.3 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -3.4 | -4.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~19% of this change | -3.2 | -3.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.2 | -3.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.0 | -5.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.7 | -2.9 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.5 | -1.7 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -2.4 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | RB binding protein 8, endonuclease |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q11.2 — chr18:22,798,261-23,026,488 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CtIP, RIM, COM1; previously SCKL2 |
| Gene groups (HGNC) | BRCA1 C complex; MicroRNA protein coding host genes |
| Hallmark sets | ESTROGEN_RESPONSE_LATE, ESTROGEN_RESPONSE_EARLY |
| Reactome | 33 pathways, smallest: HDR through MMEJ (alt-NHEJ); Impaired BRCA2 binding to PALB2; Defective HDR through Homologous Recombination Repair (HRR) due to PALB2 loss of BRCA1 binding function |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99708](https://www.uniprot.org/uniprotkb/Q99708) (DNA endonuclease RBBP8):

> Endonuclease that cooperates with the MRE11-RAD50-NBN (MRN) complex in DNA-end resection, the first step of double-strand break (DSB) repair through the homologous recombination (HR) pathway. HR is restricted to S and G2 phases of the cell cycle and preferentially repairs DSBs resulting from replication fork collapse. Key determinant of DSB repair pathway choice, as it commits cells to HR by preventing classical non-homologous end-joining (NHEJ). Specifically promotes the endonuclease activity …

**Summary**, from NCBI Gene [5932](https://www.ncbi.nlm.nih.gov/gene/5932):

> The protein encoded by this gene is a ubiquitously expressed nuclear protein. It is found among several proteins that bind directly to retinoblastoma protein, which regulates cell proliferation. This protein complexes with transcriptional co-repressor CTBP. It is also associated with BRCA1 and is thought to modulate the functions of BRCA1 in transcriptional regulation, DNA repair, and/or cell cycle checkpoint control. It is suggested that this gene may itself be a tumor suppressor acting in the …

**Accessions** — [HGNC:9891](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9891) · Entrez [5932](https://www.ncbi.nlm.nih.gov/gene/5932) · UniProt [Q99708](https://www.uniprot.org/uniprotkb/Q99708) · Ensembl [ENSG00000101773](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101773)

## Data

Gene col 2171: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2171); `tables/drug_effects.parquet` (61 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2171, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2171]; `tensor/DDL_lfc|DDL_z.npy` [2171]; `embed/gene_vectors.npy` [2171]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2171 or target_col == 2171). Every well: [[RBBP8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RBBP8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
