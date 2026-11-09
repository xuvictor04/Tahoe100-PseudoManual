---
symbol: "DNAJC1"
type: "gene"
col: 5901
ensembl_id: "ENSG00000136770"
name: "DnaJ heat shock protein family (Hsp40) member C1"
location: "10p12.31"
module: 1
arm: "-"
pooled_cpm: 204.72
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 5
n_dd_up_clean: 13
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# DNAJC1

*DnaJ heat shock protein family (Hsp40) member C1* — 10p12.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.70× (z +24.1, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.482× (z -17.1, q 0e+00, down in 36 of 44 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 11 lines (NCI-H1792 0.255×, A-172 0.282×, NCI-H1573 0.214×, C-33 A 0.216×, …; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (A549 0.516×, NCI-H1792 0.493×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H1792 0.470×; ⚠ cell-cycle shift, explains ~21% of this change); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (A498 0.540×); [[Auranofin (drug)]] 5 µM in 1 line (SW 900 0.503×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RRAS]] (+0.64, fdr 4e-05), [[SDF2L1]] (+0.64, fdr 1e-05), [[CDKN2D]] (+0.62, fdr 3e-05); moves opposite to [[ZNF507]] (-0.69, fdr 1e-05), [[VPS52]] (-0.66, fdr 1e-05), [[GATB]] (-0.64, fdr 8e-06).
> It sits in the **-** arm of [[Module 001]] (rRNA processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 11 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5901.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.70×** | +24.1 | 0e+00 | 48/48 (PANC-1, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.58×** | +23.1 | 0e+00 | 47/48 (PANC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.46×** | +21.9 | 0e+00 | 48/48 (SK-MEL-2, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.49×** | +13.7 | 1e-40 | 41/48 (HEC-1-A, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.74×** | +13.5 | 1e-39 | 46/48 (SK-MEL-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.36×** | +10.6 | 3e-24 | 28/48 (RKO, SW1417, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.51×** | +10.1 | 5e-22 | 42/48 (HEC-1-A, RKO, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.45×** | +9.1 | 7e-18 | 31/48 (NCI-H460, HepG2/C3A, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **1.41×** | +8.4 | 2e-15 | 34/48 (PANC-1, SW480, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.92×** | +8.3 | 6e-15 | 42/49 (PANC-1, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **1.40×** | +7.9 | 2e-13 | 34/47 (NCI-H460, COLO 205, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.39×** | +7.6 | 1e-12 | 26/48 (HEC-1-A, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~22% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.33×** | +7.0 | 1e-10 | 32/48 (NCI-H460, SW480, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.32×** | +6.8 | 5e-10 | 29/48 (NCI-H460, SW48, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.29×** | +6.2 | 2e-08 | 30/49 (HEC-1-A, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.37×** | +4.0 | 0.001 | 26/48 (NCI-H2347, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.25×** | +3.8 | 0.004 | 21/48 (NCI-H2030, LoVo, …) | two highest doses | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.16× | +3.7 | 0.006 | 15/49 (RKO, HEC-1-A, …) | top dose only |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.22×** | +3.5 | 0.013 | 17/48 (HT-29, AsPC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | 1.16× | +3.4 | 0.013 | 14/49 (SHP-77, A-427, …) | top dose only |  |
| [[venetoclax (drug)]] 5 µM |  | **1.30×** | +3.3 | 0.021 | 20/48 (NCI-H460, NCI-H23, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 7 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5901.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 11 lines (NCI-H1792 0.255×, A-172 0.282×, NCI-H1573 0.214×, C-33 A 0.216×, …; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (A549 0.516×, NCI-H1792 0.493×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H1792 0.470×; ⚠ cell-cycle shift, explains ~21% of this change); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (A498 0.540×); [[Auranofin (drug)]] 5 µM in 1 line (SW 900 0.503×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.482×** | -17.1 | 0e+00 | 36/44 (NCI-H1792, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.575×** | -9.8 | 2e-20 | 34/49 (NCI-H1792, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.656×** | -9.5 | 5e-19 | 33/45 (A498, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.788×** | -5.6 | 3e-06 | 27/47 (SW1417, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.807×** | -5.2 | 2e-05 | 27/48 (AsPC-1, SW 900, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | 0.860× | -5.2 | 2e-05 | 20/48 (NCI-H1792, C32, …) | rises with dose | low cells (technical?) |
| [[Filgotinib (drug)]] 5 µM |  | 0.842× | -4.2 | 0.002 | 20/48 (CFPAC-1, A-172, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.850× | -3.9 | 0.006 | 18/48 (A498, HS-578T, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | 0.858× | -3.7 | 0.012 | 19/48 (SW 900, NCI-H1792, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.848× | -3.7 | 0.012 | 17/47 (LoVo, HS-578T, …) | inconsistent across doses | low cells (technical?) |
| [[Omeprazole (drug)]] 0.05 µM |  | 0.879× | -3.1 | 0.085 | 9/48 (SW480, SHP-77, …) | inconsistent across doses |  |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | 0.881× | -3.1 | 0.10 | 6/48 (LOX-IMVI, CFPAC-1, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | 0.787× | -3.0 | 0.10 | 15/38 (NCI-H1792, SW1417, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5901. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 198 | 14 (8 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.27× (z +18.8) | [[Dinaciclib (drug)]] 5 µM 0.483× (z -11.1) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 211 | 10 (4 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.27× (z +24.0) ⚠ cell-cycle shift, explains ~21% of this change · without an alert: [[Belinostat (drug)]] 5 µM 2.89× (z +15.2) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.425× (z -11.9) ⚠ toxic |
| [[SW480 (line)]] | alt | 171 | 13 (6 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.85× (z +20.9) | — |
| [[RKO (line)]] | wt | 126 | 12 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.34× (z +25.2) ⚠ cell-cycle shift, explains ~21% of this change · without an alert: [[Belinostat (drug)]] 5 µM 6.49× (z +19.8) | — |
| [[SW48 (line)]] | wt | 243 | 10 (5 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.78× (z +12.9) | [[Dinaciclib (drug)]] 5 µM 0.405× (z -8.5) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 152 | 9 (3 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.14× (z +17.8) | [[Dinaciclib (drug)]] 5 µM 0.479× (z -8.9) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 149 | 9 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +23.1) ⚠ cell-cycle shift, explains ~21% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 4.15× (z +21.1) | [[Dinaciclib (drug)]] 5 µM 0.511× (z -9.6) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 220 | 9 (5 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.13× (z +16.1) | — |
| [[NCI-H1792 (line)]] | alt | 437 | 3 | 6 (6 ⚠) | [[Panobinostat (drug)]] 5 µM 2.16× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.255× (z -19.1) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 205 | 7 (2 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.10× (z +20.2) | [[Dinaciclib (drug)]] 5 µM 0.536× (z -8.7) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 124 | 8 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.68× (z +10.9) | — |
| [[LS 180 (line)]] | wt | 352 | 5 (1 ⚠) | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.52× (z +14.3) | [[Dinaciclib (drug)]] 5 µM 0.476× (z -11.1) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 76.0 | 8 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.99× (z +23.5) | — |
| [[BT-474 (line)]] | alt | 161 | 7 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +16.2) ⚠ cell-cycle shift, explains ~21% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 2.52× (z +12.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 87.2 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.09× (z +21.2) ⚠ cell-cycle shift, explains ~21% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 6.87× (z +20.5) | — |
| [[NCI-H2347 (line)]] | alt | 189 | 4 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.72× (z +11.8) ⚠ cell-cycle shift, explains ~21% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.13× (z +11.5) | [[Dinaciclib (drug)]] 5 µM 0.440× (z -12.0) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 173 | 5 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.07× (z +14.7) | [[Dinaciclib (drug)]] 5 µM 0.374× (z -12.5) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 251 | 4 | 2 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.24× (z +11.9) | [[Dinaciclib (drug)]] 5 µM 0.331× (z -15.6) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 358 | 3 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.75× (z +14.6) | [[Dinaciclib (drug)]] 5 µM 0.396× (z -12.8) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 125 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 7.09× (z +22.2) | — |
| [[A-172 (line)]] | wt | 243 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.57× (z +14.8) | [[Dinaciclib (drug)]] 5 µM 0.282× (z -19.0) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 244 | 4 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.31× (z +13.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.516× (z -14.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 349 | 3 | 2 (2 ⚠) | [[Belinostat (drug)]] 5 µM 2.94× (z +11.8) | [[Dinaciclib (drug)]] 5 µM 0.216× (z -16.1) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 160 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 2.92× (z +14.6) | — |
| [[HT-29 (line)]] | alt | 159 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.60× (z +12.5) | [[Dinaciclib (drug)]] 5 µM 0.441× (z -10.3) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 280 | 2 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 1.79× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.487× (z -11.8) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 82.0 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 5.45× (z +17.3) | — |
| [[Panc 03.27 (line)]] | alt | 153 | 5 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.32× (z +10.6) | — |
| [[SNU-423 (line)]] | alt | 182 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.71× (z +12.1) | [[Dinaciclib (drug)]] 5 µM 0.464× (z -8.9) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 347 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.342× (z -15.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.540× (z -9.0) |
| [[AN3 CA (line)]] | alt | 305 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.68× (z +12.0) | [[Dinaciclib (drug)]] 0.5 µM 0.213× (z -10.4) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 131 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 6.41× (z +19.6) | — |
| [[NCI-H1573 (line)]] | alt | 211 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.214× (z -16.3) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 365 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.23× (z +10.7) | [[Dinaciclib (drug)]] 5 µM 0.295× (z -15.7) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 136 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.26× (z +12.9) | [[Dinaciclib (drug)]] 5 µM 0.323× (z -9.7) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 153 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.26× (z +9.9) | — |
| [[H4 (line)]] | wt | 129 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.98× (z +10.2) | — |
| [[HCT15 (line)]] | alt | 170 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.89× (z +16.1) | — |
| [[LoVo (line)]] | wt | 215 | 3 | 0 | [[Belinostat (drug)]] 5 µM 2.59× (z +12.6) | — |
| [[RPMI-7951 (line)]] | alt | 260 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.26× (z +9.7) | — |
| [[SW 900 (line)]] | alt | 338 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.322× (z -13.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.503× (z -8.7) |
| [[COLO 205 (line)]] | alt | 112 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.93× (z +10.2) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 165 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.85× (z +10.0) | — |
| [[Hs 766T (line)]] | wt | 167 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.20× (z +9.1) | — |
| [[HS-578T (line)]] | alt | 251 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.392× (z -8.7) ⚠ toxic; transcription drop |
| [[NCI-H2122 (line)]] | alt | 231 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 225 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 370 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 163 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 147 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5901), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*44 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RRAS]] | +0.64 | +0.58 / +0.41 | both halves | 4e-05 |  |
| [[SDF2L1]] | +0.64 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[CDKN2D]] | +0.62 | +0.44 / +0.55 | both halves | 3e-05 |  |
| [[OSTF1]] | +0.62 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[CARD19]] | +0.61 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[GBF1]] | +0.61 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[PCMT1]] | +0.60 | +0.54 / +0.44 | both halves | 3e-05 |  |
| [[PLEKHH3]] | +0.59 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[ARL3]] | +0.59 | +0.46 / +0.50 | both halves | 2e-05 | pathway: HALLMARK_ESTROGEN_RESPONSE_LATE |
| [[GMCL1]] | +0.58 | +0.57 / +0.40 | both halves | 5e-05 |  |
| [[TMEM256]] | +0.58 | +0.35 / +0.43 | both halves | 1e-04 |  |
| [[YIF1B]] | +0.57 | +0.34 / +0.48 | both halves | 1e-04 |  |

## Genes that move opposite

*56 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF507]] | -0.69 | -0.61 / -0.57 | both halves | 1e-05 |  |
| [[VPS52]] | -0.66 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[GATB]] | -0.64 | -0.62 / -0.57 | both halves | 8e-06 |  |
| [[SNAPC5]] | -0.62 | -0.55 / -0.41 | both halves | 4e-05 |  |
| [[U2AF2]] | -0.61 | -0.38 / -0.54 | both halves | 7e-05 |  |
| [[SPRYD4]] | -0.61 | -0.46 / -0.50 | both halves | 3e-05 |  |
| [[ZXDB]] | -0.61 | -0.47 / -0.57 | both halves | 2e-05 |  |
| [[MAPKAPK5]] | -0.61 | -0.45 / -0.55 | both halves | 3e-05 |  |
| [[MTHFSD]] | -0.60 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[POLR2M]] | -0.59 | -0.46 / -0.47 | both halves | 2e-05 |  |
| [[ZNF300]] | -0.59 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[TARDBP]] | -0.59 | -0.43 / -0.57 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **-** arm (projection on the module's main direction -0.489). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-10.1, 7.3); signed map (-31.2, 15.7). **Vector** length 130, 45.9% of its response variance represented; |z| ≥ 3 in 1,497 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +9.0 | +13.7 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +7.6 | +13.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.9 | +6.2 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +5.9 | +10.1 |
|  | [[Belinostat (drug)]] 5 µM |  | +5.7 | +23.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.7 | +8.3 |
|  | [[EX229 (drug)]] 0.5 µM |  | +2.6 | +2.5 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.4 | +4.0 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +2.3 | +3.5 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -8.3 | -5.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | -7.6 | -5.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -7.5 | -9.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -7.2 | -17.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.5 | -3.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.4 | -3.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -6.1 | -2.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -5.1 | -0.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | -4.5 | -4.2 |

## What is on record

|  |  |
|---|---|
| Name | DnaJ heat shock protein family (Hsp40) member C1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p12.31 — chr10:21,756,548-22,003,769 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DNAJL1, ERdj1, MTJ1 |
| Gene groups (HGNC) | Myb/SANT domain containing; DNAJ (HSP40) heat shock proteins |
| Hallmark sets | ESTROGEN_RESPONSE_LATE |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96KC8](https://www.uniprot.org/uniprotkb/Q96KC8) (DnaJ homolog subfamily C member 1):

> May modulate protein synthesis.

**Summary**, from NCBI Gene [64215](https://www.ncbi.nlm.nih.gov/gene/64215):

> The membrane protein encoded by this gene is a DNAJ-like heat shock protein that binds the molecular chaperone BiP. In addition, the encoded protein contains two SANT domains that have been shown to bind serpin alpha1-antichymotrypsin and inter-alpha trypsin inhibitor heavy chain 4. [provided by RefSeq, Jul 2016]

**Accessions** — [HGNC:20090](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20090) · Entrez [64215](https://www.ncbi.nlm.nih.gov/gene/64215) · UniProt [Q96KC8](https://www.uniprot.org/uniprotkb/Q96KC8) · Ensembl [ENSG00000136770](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136770)

## Data

Gene col 5901: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5901); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5901, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5901]; `tensor/DDL_lfc|DDL_z.npy` [5901]; `embed/gene_vectors.npy` [5901]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5901 or target_col == 5901). Every well: [[DNAJC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DNAJC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
