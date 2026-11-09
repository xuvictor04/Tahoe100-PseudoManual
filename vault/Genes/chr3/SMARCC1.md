---
symbol: "SMARCC1"
type: "gene"
col: 10391
ensembl_id: "ENSG00000173473"
name: "SWI/SNF related BAF chromatin remodeling complex subunit C1"
location: "3p21.31"
module: 4
arm: "+"
pooled_cpm: 297.13
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 9
n_dd_up_clean: 2
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# SMARCC1

*SWI/SNF related BAF chromatin remodeling complex subunit C1* — 3p21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.94× (z +24.5, q 0e+00, up in 48 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[PH-797804 (drug)]] 5 µM: 1.49× (z +7.7, q 2e-12, up in 31 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (LoVo 3.30×, SW480 2.38×, SNU-423 2.81×, KATO III 3.00×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (SNU-423 2.75×, KATO III 3.13×, HT-29 3.00×, SW480 2.12×, …; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 3 lines (SNU-423 2.08×, NCI-H2347 1.83×, A549 2.01×; ⚠ cell-cycle shift, would explain all of this change); [[PH-797804 (drug)]] 5 µM in 2 lines (PANC-1 2.11×, HEC-1-A 2.04×).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 0.704× (z -12.5, q 3e-33, down in 37 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Tucidinostat (drug)]] 0.5 µM: 0.784× (z -9.0, q 4e-17, down in 31 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GSPT1]] (+0.62, fdr 1e-05), [[DOCK1]] (+0.56, fdr 1e-05), [[LAS1L]] (+0.55, fdr 5e-05); moves opposite to [[MRPL44]] (-0.50, fdr 1e-04), [[KBTBD4]] (-0.48, fdr 9e-05), [[NDUFB4]] (-0.47, fdr 5e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 10 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10391.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (LoVo 3.30×, SW480 2.38×, SNU-423 2.81×, KATO III 3.00×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (SNU-423 2.75×, KATO III 3.13×, HT-29 3.00×, SW480 2.12×, …; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 3 lines (SNU-423 2.08×, NCI-H2347 1.83×, A549 2.01×; ⚠ cell-cycle shift, would explain all of this change); [[PH-797804 (drug)]] 5 µM in 2 lines (PANC-1 2.11×, HEC-1-A 2.04×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.94×** | +24.5 | 0e+00 | 48/49 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.82×** | +21.4 | 0e+00 | 40/44 (SNU-423, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.59×** | +15.9 | 0e+00 | 37/45 (SNU-423, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.43×** | +12.8 | 2e-35 | 42/47 (NCI-H460, SHP-77, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.49×** | +7.7 | 2e-12 | 31/48 (HEC-1-A, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.20×** | +6.8 | 9e-10 | 24/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | 1.20× | +6.6 | 3e-09 | 24/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | 1.19× | +6.5 | 5e-09 | 22/48 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | 1.13× | +4.6 | 3e-04 | 15/48 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.24×** | +4.2 | 0.002 | 23/48 (SHP-77, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.22×** | +3.8 | 0.007 | 20/45 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.07× | +3.7 | 0.012 | 14/48 (SNU-423, NCI-H2347, …) | top dose only | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 12 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10391.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.704×** | -12.5 | 3e-33 | 37/47 (RKO, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | **0.830×** | -9.8 | 4e-20 | 23/49 (SW48, HEC-1-A, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.784×** | -9.0 | 4e-17 | 31/49 (RPMI-7951, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.847× | -8.7 | 5e-16 | 20/48 (LS 180, KATO III, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | 0.847× | -8.7 | 5e-16 | 23/48 (RKO, J82, …) | rises with dose | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.824×** | -7.1 | 8e-11 | 25/48 (MIA PaCa-2, RKO, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.828×** | -7.0 | 2e-10 | 24/48 (HEC-1-A, SW48, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.837× | -6.6 | 3e-09 | 21/48 (SW48, HEC-1-A, …) | inconsistent across doses |  |
| [[venetoclax (drug)]] 5 µM |  | **0.712×** | -6.6 | 3e-09 | 33/48 (SW480, SK-MEL-2, …) | rises with dose | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.853× | -5.9 | 2e-07 | 19/48 (LS 180, SW480, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.853× | -5.9 | 2e-07 | 19/48 (NCI-H23, J82, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.898× | -5.7 | 8e-07 | 15/48 (SNU-1, HEC-1-A, …) | rises with dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.768×** | -5.1 | 1e-05 | 25/48 (HEC-1-A, NCI-H23, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.777×** | -4.9 | 4e-05 | 28/48 (HEC-1-A, A498, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | 0.837× | -4.7 | 1e-04 | 19/48 (SW48, NCI-H1792, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **0.790×** | -4.6 | 2e-04 | 22/47 (NCI-H2347, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | 0.866× | -3.8 | 0.005 | 15/48 (LoVo, SW1417, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | 0.837× | -3.4 | 0.018 | 17/49 (LS 180, RKO, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | 0.906× | -3.4 | 0.021 | 7/47 (C-33 A, RKO, …) | all doses, stronger at high dose |  |
| [[EX229 (drug)]] 0.05 µM |  | 0.909× | -3.3 | 0.023 | 4/48 (Hs 766T, SW48, …) | all doses, flat |  |
| [[Amsacrine (drug)]] 5 µM |  | 0.940× | -3.2 | 0.029 | 3/48 (NCI-H2030, A498, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | 0.853× | -3.1 | 0.050 | 18/48 (HEC-1-A, SW48, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10391. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 299 | 9 (8 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.00× (z +16.4) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 2.11× (z +9.2) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.623× (z -10.8) ⚠ toxic |
| [[HEC-1-A (line)]] | alt | 459 | 4 (3 ⚠) | 4 (4 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.87× (z +15.4) ⚠ toxic; transcription drop · without an alert: [[PH-797804 (drug)]] 5 µM 2.04× (z +9.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.617× (z -16.8) ⚠ cell-cycle shift, explains ~9% of this change |
| [[NCI-H460 (line)]] | wt | 237 | 8 (8 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 1.93× (z +13.2) ⚠ toxic | — |
| [[LS 180 (line)]] | wt | 280 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.78× (z +17.3) ⚠ toxic; transcription drop | [[Tucidinostat (drug)]] 5 µM 0.636× (z -10.8) |
| [[NCI-H1792 (line)]] | alt | 253 | 6 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.34× (z +16.5) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 269 | 6 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +18.7) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SW480 (line)]] | alt | 463 | 3 (3 ⚠) | 3 (3 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.38× (z +20.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.640× (z -14.7) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 188 | 5 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +15.5) ⚠ cell-cycle shift, would explain all of this change | — |
| [[A498 (line)]] | wt | 162 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.38× (z +16.0) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 208 | 4 (4 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +17.7) ⚠ cell-cycle shift, would explain all of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.558× (z -14.8) ⚠ cell-cycle shift, explains ~9% of this change |
| [[Panc 03.27 (line)]] | alt | 263 | 4 (4 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.44× (z +16.8) ⚠ toxic; transcription drop | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.586× (z -9.6) ⚠ toxic |
| [[RKO (line)]] | wt | 476 | 0 | 5 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.277× (z -23.4) ⚠ toxic |
| [[RPMI-7951 (line)]] | alt | 262 | 4 (4 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +14.8) ⚠ cell-cycle shift, would explain all of this change | [[Tucidinostat (drug)]] 0.5 µM 0.596× (z -8.7) |
| [[HOP62 (line)]] | alt | 282 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.72× (z +10.8) ⚠ toxic; transcription drop | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.629× (z -8.9) ⚠ toxic |
| [[HS-578T (line)]] | alt | 253 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.26× (z +15.5) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 242 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.00× (z +18.2) ⚠ toxic; transcription drop | [[Tucidinostat (drug)]] 5 µM 0.662× (z -9.7) |
| [[LoVo (line)]] | wt | 279 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.30× (z +20.8) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 301 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.81× (z +19.9) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 410 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.00× (z +14.1) ⚠ toxic; transcription drop | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.641× (z -9.1) ⚠ cell-cycle shift, explains ~21% of this change |
| [[SW48 (line)]] | wt | 442 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.468× (z -17.1) ⚠ cell-cycle shift, explains ~9% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.556× (z -9.3) |
| [[C-33 A (line)]] | alt | 536 | 0 | 3 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.624× (z -12.9) ⚠ cell-cycle shift, explains ~9% of this change |
| [[CFPAC-1 (line)]] | alt | 143 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.18× (z +13.3) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 296 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.95× (z +11.9) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 182 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.00× (z +17.1) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 182 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.19× (z +10.0) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 367 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.08× (z +17.8) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 431 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.89× (z +12.7) ⚠ toxic; transcription drop | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.504× (z -13.6) ⚠ cell-cycle shift, explains ~21% of this change |
| [[NCI-H1573 (line)]] | alt | 127 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.38× (z +12.9) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 464 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.74× (z +12.0) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 447 | 1 (1 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.60× (z +9.2) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.651× (z -11.8) ⚠ cell-cycle shift, explains ~9% of this change |
| [[SW 900 (line)]] | alt | 166 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.41× (z +12.1) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 430 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.562× (z -10.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.589× (z -9.3) |
| [[AsPC-1 (line)]] | alt | 183 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.23× (z +12.8) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 244 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.88× (z +10.6) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 162 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.74× (z +11.7) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 172 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.38× (z +10.2) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 390 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.09× (z +12.6) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 165 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.80× (z +9.1) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 393 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.582× (z -11.2) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H2030 (line)]] | alt | 337 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.70× (z +9.9) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.606× (z -13.3) ⚠ cell-cycle shift, explains ~9% of this change |
| [[SNU-1 (line)]] | wt | 295 | 0 | 2 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.486× (z -15.6) |
| [[A-427 (line)]] | wt | 407 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 1.58× (z +9.8) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 257 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.82× (z +9.4) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 466 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.507× (z -10.9) ⚠ cell-cycle shift, explains ~9% of this change |
| [[NCI-H23 (line)]] | alt | 425 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 1.76× (z +10.6) ⚠ toxic; transcription drop | — |
| [[NCI-H2122 (line)]] | alt | 239 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 305 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 300 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 202 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 192 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10391), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GSPT1]] | +0.62 | +0.53 / +0.62 | both halves | 1e-05 | pathway: HALLMARK_G2M_CHECKPOINT |
| [[DOCK1]] | +0.56 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[LAS1L]] | +0.55 | +0.40 / +0.53 | both halves | 5e-05 |  |
| [[CCDC91]] | +0.54 | +0.32 / +0.60 | both halves | 2e-04 |  |
| [[XRN2]] | +0.53 | +0.43 / +0.56 | both halves | 3e-05 |  |
| [[SERBP1]] | +0.53 | +0.58 / +0.37 | both halves | 8e-05 | pathway: HALLMARK_MYC_TARGETS_V1 |
| [[MYBBP1A]] | +0.52 | +0.53 / +0.50 | both halves | 1e-05 | pathway: Epigenetic regulation of gene expression |
| [[MDN1]] | +0.52 | +0.58 / +0.47 | both halves | 2e-05 |  |
| [[TAF4B]] | +0.51 | +0.48 / +0.53 | both halves | 2e-05 | pathway: Affinity selection of immunoglobulins |
| [[USP2-AS1]] | +0.51 | +0.54 / +0.42 | both halves | 4e-05 |  |
| [[SMARCA4]] | +0.49 | +0.46 / +0.46 | both halves | 3e-05 | same gene group; pathway: ATP-dependent chromatin remodelers; STRING 999 |
| [[ZNF37BP]] | +0.49 | +0.25 / +0.58 | both halves | 4e-04 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPL44]] | -0.50 | -0.34 / -0.51 | both halves | 1e-04 |  |
| [[KBTBD4]] | -0.48 | -0.40 / -0.36 | both halves | 9e-05 |  |
| [[NDUFB4]] | -0.47 | -0.40 / -0.48 | both halves | 5e-05 |  |
| [[ZSWIM1]] | -0.47 | -0.33 / -0.47 | both halves | 1e-04 |  |
| [[ZFPL1]] | -0.47 | -0.33 / -0.46 | both halves | 1e-04 |  |
| [[STBD1]] | -0.46 | -0.29 / -0.38 | both halves | 2e-04 |  |
| [[CCDC167]] | -0.46 | -0.45 / -0.39 | both halves | 6e-05 |  |
| [[SHOX2]] | -0.46 | -0.43 / -0.37 | both halves | 7e-05 |  |
| [[TVP23B]] | -0.45 | -0.30 / -0.42 | both halves | 2e-04 |  |
| [[MICA]] | -0.45 | -0.43 / -0.42 | both halves | 4e-05 |  |
| [[LSM8]] | -0.45 | -0.30 / -0.47 | both halves | 2e-04 |  |
| [[RAB1A]] | -0.45 | -0.34 / -0.42 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.375). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-9.1, -43.4); signed map (0.7, -55.7). **Vector** length 136, 45.7% of its response variance represented; |z| ≥ 3 in 1,430 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +10.5 | +24.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +9.4 | +21.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +7.0 | +12.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.8 | +15.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +6.4 | +1.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.1 | +2.9 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | +3.7 | +2.7 |
|  | [[Rapamycin (drug)]] 0.5 µM |  | +3.5 | +2.6 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +3.4 | +1.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.9 | +7.7 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -10.1 | -12.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -8.7 | -8.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | -6.8 | -7.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.3 | -6.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -5.9 | -5.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -5.6 | -4.9 |
|  | [[venetoclax (drug)]] 5 µM |  | -5.6 | -6.6 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -5.2 | -4.7 |
|  | [[Belzutifan (drug)]] 5 µM |  | -5.0 | -4.6 |

## What is on record

|  |  |
|---|---|
| Name | SWI/SNF related BAF chromatin remodeling complex subunit C1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.31 — chr3:47,585,269-47,782,106 (-) |
| Ensembl biotype | protein_coding |
| Also known as | BAF155, SRG3, Rsc8, CRACC1 |
| Gene groups (HGNC) | Myb/SANT domain containing; BAF complex subunits; PBAF complex subunits; GBAF complex subunits; Small nucleolar RNA protein coding host genes |
| Hallmark sets | PEROXISOME, G2M_CHECKPOINT, MYC_TARGETS_V1 |
| Reactome | 22 pathways, smallest: Formation of the non-canonical BAF (ncBAF) complex; Formation of the canonical BAF (cBAF) complex; Formation of the polybromo-BAF (pBAF) complex |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92922](https://www.uniprot.org/uniprotkb/Q92922) (SWI/SNF complex subunit SMARCC1):

> Involved in transcriptional activation and repression of select genes by chromatin remodeling (alteration of DNA-nucleosome topology). Component of SWI/SNF chromatin remodeling complexes that carry out key enzymatic activities, changing chromatin structure by altering DNA-histone contacts within a nucleosome in an ATP-dependent manner. May stimulate the ATPase activity of the catalytic subunit of the complex. Belongs to the neural progenitors-specific chromatin remodeling complex (npBAF …

**Summary**, from NCBI Gene [6599](https://www.ncbi.nlm.nih.gov/gene/6599):

> The protein encoded by this gene is a member of the SWI/SNF family of proteins, whose members display helicase and ATPase activities and which are thought to regulate transcription of certain genes by altering the chromatin structure around those genes. The encoded protein is part of the large ATP-dependent chromatin remodeling complex SNF/SWI and contains a predicted leucine zipper motif typical of many transcription factors. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:11104](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11104) · Entrez [6599](https://www.ncbi.nlm.nih.gov/gene/6599) · UniProt [Q92922](https://www.uniprot.org/uniprotkb/Q92922) · Ensembl [ENSG00000173473](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173473)

## Data

Gene col 10391: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10391); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10391, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10391]; `tensor/DDL_lfc|DDL_z.npy` [10391]; `embed/gene_vectors.npy` [10391]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10391 or target_col == 10391). Every well: [[SMARCC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SMARCC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
