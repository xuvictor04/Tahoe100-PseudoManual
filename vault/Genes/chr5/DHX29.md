---
symbol: "DHX29"
type: "gene"
col: 858
ensembl_id: "ENSG00000067248"
name: "DExH-box helicase 29"
location: "5q11.2"
module: 12
arm: "+"
pooled_cpm: 79.28
n_lines_expressing: 50
n_dd_up: 29
n_dd_down: 0
n_dd_up_clean: 11
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# DHX29

*DExH-box helicase 29* — 5q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (18 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.53× (z +22.8, q 0e+00, up in 48 of 48 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 2.45× (z +15.5, q 0e+00, up in 47 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (SW48 0.101×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Finasteride (drug)]] 5 µM in 1 line (SW 1088 0.0867×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UBA3]] (+0.69, fdr 7e-06), [[MTIF3]] (+0.65, fdr 1e-05), [[SRRM1]] (+0.63, fdr 1e-05); moves opposite to [[MIR222HG]] (-0.58, fdr 7e-06), [[PPIA]] (-0.56, fdr 1e-05), [[MAT2A]] (-0.55, fdr 3e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 19 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 858.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **2.53×** | +22.8 | 0e+00 | 48/48 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.45×** | +15.5 | 0e+00 | 47/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **2.22×** | +13.3 | 8e-38 | 47/48 (SW480, A-427, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.73×** | +9.5 | 5e-19 | 47/48 (AsPC-1, CFPAC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.64×** | +8.5 | 1e-15 | 44/48 (AsPC-1, A-172, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.62×** | +8.3 | 8e-15 | 46/48 (AsPC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **1.61×** | +8.2 | 2e-14 | 35/48 (LS 180, LoVo, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.54×** | +7.5 | 4e-12 | 34/48 (LS 180, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.31×** | +6.6 | 3e-09 | 30/49 (MIA PaCa-2, SHP-77, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.98×** | +6.2 | 3e-08 | 38/49 (SW480, HEC-1-A, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~24% here); composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.40×** | +5.6 | 1e-06 | 30/48 (MIA PaCa-2, SW480, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.37×** | +5.4 | 3e-06 | 38/48 (NCI-H2030, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.36×** | +5.4 | 3e-06 | 30/48 (LS 180, LoVo, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.34×** | +5.0 | 2e-05 | 30/48 (AsPC-1, RKO, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.33×** | +5.0 | 2e-05 | 28/48 (A-427, SW480, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.37×** | +4.9 | 3e-05 | 31/48 (SNU-423, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.28×** | +4.2 | 7e-04 | 29/48 (A-427, LS 180, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.25×** | +3.8 | 0.004 | 23/48 (LOX-IMVI, RKO, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.21×** | +3.3 | 0.023 | 20/48 (A-427, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.43×** | +3.2 | 0.025 | 15/49 (AsPC-1, NCI-H2347, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.42×** | +3.1 | 0.032 | 21/48 (LS 180, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Terfenadine (drug)]] 5 µM |  | 1.13× | +2.9 | 0.067 | 11/48 (LOX-IMVI, LS 180, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.18× | +2.9 | 0.067 | 12/49 (SNU-423, HEC-1-A, …) | top dose only |  |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | 1.12× | +2.8 | 0.075 | 9/49 (SK-MEL-2, HT-29, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 858.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (SW48 0.101×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Finasteride (drug)]] 5 µM in 1 line (SW 1088 0.0867×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.939× | -3.7 | 0.12 | 0/50 | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~64% of this change | 0.819× | -3.5 | 0.13 | 22/49 (H4, LoVo, …) | inconsistent across doses |  |
| [[Demeclocycline (drug)]] 5 µM |  | 0.872× | -3.4 | 0.13 | 11/48 (SW1417, LOX-IMVI, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, +0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 858. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 71.5 | 8 (7 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +21.2) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.87× (z +16.6) | — |
| [[A-427 (line)]] | wt | 139 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +16.7) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.87× (z +13.7) | — |
| [[AsPC-1 (line)]] | alt | 55.0 | 5 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +12.4) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[LoVo (line)]] | wt | 107 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.22× (z +18.7) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.64× (z +14.6) | — |
| [[LS 180 (line)]] | wt | 74.2 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.18× (z +20.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.79× (z +15.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 77.2 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.34× (z +15.2) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.38× (z +10.9) | — |
| [[A-172 (line)]] | wt | 101 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +17.3) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.36× (z +11.3) | — |
| [[CFPAC-1 (line)]] | alt | 51.5 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +15.6) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.85× (z +10.2) | — |
| [[PANC-1 (line)]] | alt | 85.4 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.10× (z +23.3) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.10× (z +16.5) | — |
| [[SNU-423 (line)]] | alt | 55.3 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +13.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.94× (z +9.3) | — |
| [[C-33 A (line)]] | alt | 88.1 | 3 (2 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 2.82× (z +9.4) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.59× (z +9.0) | — |
| [[HEC-1-A (line)]] | alt | 65.5 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.10× (z +20.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.90× (z +15.9) | — |
| [[HT-29 (line)]] | alt | 63.8 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.17× (z +18.8) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.93× (z +10.0) | — |
| [[LOX-IMVI (line)]] | wt | 91.5 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +14.7) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.51× (z +10.2) | — |
| [[NCI-H2030 (line)]] | alt | 93.7 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +14.8) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.08× (z +9.7) | — |
| [[NCI-H23 (line)]] | alt | 76.6 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +14.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.88× (z +10.2) | — |
| [[NCI-H460 (line)]] | wt | 101 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +15.8) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.44× (z +11.9) | — |
| [[RKO (line)]] | wt | 81.5 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.44× (z +17.8) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.74× (z +15.8) | — |
| [[SW1417 (line)]] | alt | 73.6 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +12.7) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.46× (z +9.7) | — |
| [[SW48 (line)]] | wt | 80.9 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.54× (z +12.9) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.00× (z +10.0) | [[Dinaciclib (drug)]] 5 µM 0.101× (z -15.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 94.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +16.4) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.59× (z +9.8) | — |
| [[C32 (line)]] | wt | 66.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +12.8) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.80× (z +8.9) | — |
| [[H4 (line)]] | wt | 66.2 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +10.1) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.58× (z +9.5) | — |
| [[HCT15 (line)]] | alt | 72.9 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.70× (z +13.1) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.49× (z +8.9) | — |
| [[KATO III (line)]] | alt | 65.5 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +15.6) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.72× (z +12.1) | — |
| [[NCI-H1573 (line)]] | alt | 51.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +11.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.40× (z +8.6) | — |
| [[NCI-H1792 (line)]] | alt | 53.0 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +12.1) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.94× (z +9.7) | — |
| [[SHP-77 (line)]] | alt | 71.4 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.99× (z +10.0) | — |
| [[SK-MEL-2 (line)]] | alt | 49.5 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +9.8) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[BT-474 (line)]] | alt | 56.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +10.9) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[COLO 205 (line)]] | alt | 44.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.62× (z +13.6) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[HepG2_C3A (line)]] | wt | 42.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +9.6) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[HOP62 (line)]] | alt | 32.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.83× (z +12.0) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[Hs 766T (line)]] | wt | 58.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +9.3) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[NCI-H2347 (line)]] | alt | 127 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +10.5) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[Panc 03.27 (line)]] | alt | 101 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +11.9) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[SNU-1 (line)]] | wt | 82.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +12.9) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[SW 1088 (line)]] | alt | 114 | 0 | 1 | — | [[Finasteride (drug)]] 5 µM 0.0867× (z -9.7) |
| [[SW 900 (line)]] | alt | 88.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +10.0) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[A498 (line)]] | wt | 102 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 136 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 71.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 110 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 67.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 70.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 76.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 77.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 143 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 58.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 159 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 858), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBA3]] | +0.69 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[MTIF3]] | +0.65 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[SRRM1]] | +0.63 | +0.69 / +0.53 | both halves | 1e-05 |  |
| [[ZC3H15]] | +0.63 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[RBMX2]] | +0.63 | +0.66 / +0.54 | both halves | 1e-05 |  |
| [[GGNBP2]] | +0.62 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[PPIG]] | +0.62 | +0.73 / +0.51 | both halves | 1e-05 |  |
| [[SUCLG1]] | +0.61 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[NKAP]] | +0.59 | +0.65 / +0.48 | both halves | 2e-05 |  |
| [[RBM27]] | +0.59 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[ZNF652]] | +0.59 | +0.31 / +0.59 | both halves | 2e-04 |  |
| [[RWDD1]] | +0.59 | +0.54 / +0.63 | both halves | 1e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MIR222HG]] | -0.58 | -0.58 / -0.59 | both halves | 7e-06 |  |
| [[PPIA]] | -0.56 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[MAT2A]] | -0.55 | -0.56 / -0.46 | both halves | 3e-05 |  |
| [[MARCKSL1]] | -0.53 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[YWHAQ]] | -0.53 | -0.56 / -0.44 | both halves | 3e-05 |  |
| [[M6PR]] | -0.51 | -0.31 / -0.56 | both halves | 2e-04 |  |
| [[FLNA]] | -0.51 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[RPSA]] | -0.51 | -0.46 / -0.48 | both halves | 2e-05 | STRING 755 |
| [[AHCY]] | -0.51 | -0.59 / -0.34 | both halves | 1e-04 |  |
| [[RELT]] | -0.50 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[SMG1P3]] | -0.50 | -0.52 / -0.38 | both halves | 7e-05 |  |
| [[LINC01128]] | -0.50 | -0.44 / -0.48 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.596). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-36.7, -10.9); signed map (-16.1, -10.1). **Vector** length 83.3, 24.0% of its response variance represented; |z| ≥ 3 in 1,016 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ponatinib (drug)]] 5 µM |  | +3.0 | +0.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.0 | +2.3 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.6 | +2.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.5 | +1.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.5 | +15.5 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.4 | +0.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.3 | +1.4 |
| fall | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.5 | -1.5 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~66% of this change | -3.3 | +4.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.2 | -0.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | -1.2 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~64% of this change | -3.1 | -3.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.9 | +3.8 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -2.0 | -2.7 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.9 | -2.4 |
|  | [[Volasertib (drug)]] 0.5 µM |  | -1.7 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | DExH-box helicase 29 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q11.2 — chr5:55,256,055-55,307,694 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously DDX29 |
| Gene groups (HGNC) | DEAH-box helicases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z478](https://www.uniprot.org/uniprotkb/Q7Z478) (ATP-dependent RNA helicase DHX29):

> ATP-binding RNA helicase involved in translation initiation. Part of the 43S pre-initiation complex that is required for efficient initiation on mRNAs of higher eukaryotes with structured 5'-UTRs by promoting efficient NTPase-dependent 48S complex formation. Specifically binds to the 40S ribosome near the mRNA entrance. Does not possess a processive helicase activity.

**Summary**, from NCBI Gene [54505](https://www.ncbi.nlm.nih.gov/gene/54505):

> This gene encodes a member of the DEAH (Asp-Glu-Ala-His) subfamily of proteins, part of the DEAD (Asp-Glu-Ala-Asp) box family of RNA helicases. The encoded protein functions in translation initiation, and is specifically required for ribosomal scanning across stable mRNA secondary structures during initiation codon selection. This protein may also play a role in sensing virally derived cytosolic nucleic acids. Knockdown of this gene results in reduced protein translation and impaired …

**Accessions** — [HGNC:15815](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15815) · Entrez [54505](https://www.ncbi.nlm.nih.gov/gene/54505) · UniProt [Q7Z478](https://www.uniprot.org/uniprotkb/Q7Z478) · Ensembl [ENSG00000067248](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000067248)

## Data

Gene col 858: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 858); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 858, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 858]; `tensor/DDL_lfc|DDL_z.npy` [858]; `embed/gene_vectors.npy` [858]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 858 or target_col == 858). Every well: [[DHX29 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DHX29.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
