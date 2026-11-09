---
symbol: "CLYBL"
type: "gene"
col: 4595
ensembl_id: "ENSG00000125246"
name: "citramalyl-CoA lyase"
location: "13q32.3"
module: 4
arm: "+"
pooled_cpm: 50.18
n_lines_expressing: 48
n_dd_up: 13
n_dd_down: 30
n_dd_up_clean: 13
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# CLYBL

*citramalyl-CoA lyase* — 13q32.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 1.74× (z +7.8, q 3e-12, up in 29 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.320× (z -22.6, q 0e+00, down in 43 of 45 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.266× (z -18.6, q 0e+00, down in 43 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TSEN2]] (+0.75, fdr 7e-06), [[SERBP1]] (+0.71, fdr 7e-06), [[CMSS1]] (+0.71, fdr 7e-06); moves opposite to [[ACOX1]] (-0.58, fdr 2e-05), [[YPEL5]] (-0.57, fdr 3e-05), [[ATOSA]] (-0.56, fdr 2e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ABLIM2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, none with an alert. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4595.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.74×** | +7.8 | 3e-12 | 29/46 (HT-29, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.47×** | +7.7 | 3e-12 | 36/46 (KATO III, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.63×** | +6.8 | 2e-09 | 27/46 (KATO III, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.47×** | +5.4 | 1e-05 | 31/46 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.56×** | +4.8 | 2e-04 | 20/46 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.38×** | +4.4 | 0.001 | 23/46 (LOX-IMVI, Panc 03.27, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.48×** | +4.3 | 0.002 | 16/45 (NCI-H1573, Hs 766T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.34×** | +4.1 | 0.003 | 21/45 (Hs 766T, NCI-H1573, …) | inconsistent across doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.29×** | +3.6 | 0.022 | 17/46 (A-172, C32, …) | top dose only |  |
| [[Finasteride (drug)]] 5 µM |  | **1.28×** | +3.4 | 0.041 | 12/45 (LOX-IMVI, SNU-423, …) | top dose only |  |
| [[Omeprazole (drug)]] 5 µM |  | **1.26×** | +3.3 | 0.049 | 8/46 (LoVo, HEC-1-A, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.26×** | +3.2 | 0.058 | 15/46 (C32, SK-MEL-2, …) | rises with dose |  |
| [[Brimonidine (drug)]] 5 µM |  | **1.25×** | +3.1 | 0.085 | 9/46 (NCI-H1573, HepG2/C3A, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 11 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4595.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.320×** | -22.6 | 0e+00 | 43/45 (PANC-1, KATO III, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.266×** | -18.6 | 0e+00 | 43/46 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.301×** | -16.9 | 0e+00 | 43/45 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.291×** | -16.6 | 0e+00 | 45/46 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.507×** | -13.4 | 4e-39 | 40/45 (LoVo, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.397×** | -13.0 | 2e-36 | 36/45 (A-427, PANC-1, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.390×** | -12.7 | 5e-35 | 37/45 (LoVo, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.408×** | -12.6 | 2e-34 | 40/46 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.462×** | -10.8 | 2e-25 | 36/45 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.495×** | -9.9 | 3e-21 | 39/45 (RPMI-7951, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.550×** | -8.4 | 3e-15 | 36/46 (PANC-1, SW480, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.554×** | -7.8 | 3e-13 | 39/46 (PANC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.587×** | -7.5 | 4e-12 | 33/46 (SW480, A-427, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.615×** | -6.5 | 2e-09 | 26/45 (J82, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.674×** | -5.5 | 1e-06 | 27/46 (A-427, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.740×** | -4.1 | 0.002 | 22/45 (SK-MEL-2, SW48, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.686×** | -3.8 | 0.005 | 24/46 (PANC-1, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.768×** | -3.7 | 0.006 | 23/46 (SW 1088, PANC-1, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.612×** | -3.6 | 0.008 | 21/45 (SHP-77, HCT15, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, -0.47 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4595. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 94.2 | 1 | 18 (6 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.78× (z +9.0) | [[Digitoxin (drug)]] 5 µM 0.0775× (z -28.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0811× (z -27.5) |
| [[A-427 (line)]] | wt | 80.5 | 0 | 15 (6 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0603× (z -28.1) |
| [[SW48 (line)]] | wt | 128 | 0 | 15 (5 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0824× (z -18.8) |
| [[KATO III (line)]] | alt | 82.1 | 3 | 11 (6 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.91× (z +9.9) | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -28.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.173× (z -19.0) |
| [[PANC-1 (line)]] | alt | 59.6 | 0 | 14 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0841× (z -36.8) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.0691× (z -27.0) |
| [[LoVo (line)]] | wt | 66.8 | 0 | 13 (4 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.107× (z -22.5) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.272× (z -19.3) |
| [[NCI-H23 (line)]] | alt | 124 | 0 | 12 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.353× (z -17.2) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.380× (z -16.0) |
| [[MIA PaCa-2 (line)]] | alt | 53.3 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.124× (z -15.5) |
| [[HEC-1-A (line)]] | alt | 78.9 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -23.6) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.224× (z -14.6) |
| [[LS 180 (line)]] | wt | 66.1 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -16.4) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.176× (z -14.5) |
| [[NCI-H460 (line)]] | wt | 37.6 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -18.2) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.165× (z -15.2) |
| [[J82 (line)]] | alt | 42.4 | 0 | 8 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0878× (z -17.4) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.136× (z -14.9) |
| [[COLO 205 (line)]] | alt | 209 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -20.7) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.188× (z -15.0) |
| [[SHP-77 (line)]] | alt | 119 | 0 | 7 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.161× (z -16.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.181× (z -15.1) |
| [[A549 (line)]] | wt | 45.2 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.126× (z -20.2) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.134× (z -13.8) |
| [[NCI-H1573 (line)]] | alt | 93.8 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.251× (z -15.3) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.200× (z -12.6) |
| [[A498 (line)]] | wt | 61.2 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.130× (z -23.9) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.148× (z -15.2) |
| [[BT-474 (line)]] | alt | 32.1 | 0 | 5 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.122× (z -14.4) |
| [[HCT15 (line)]] | alt | 67.4 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0761× (z -18.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.405× (z -9.3) |
| [[HOP62 (line)]] | alt | 28.4 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -15.7) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.162× (z -13.4) |
| [[LOX-IMVI (line)]] | wt | 44.8 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -15.3) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.186× (z -13.5) |
| [[Panc 03.27 (line)]] | alt | 32.2 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -14.3) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.171× (z -10.9) |
| [[RKO (line)]] | wt | 33.3 | 0 | 5 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.101× (z -13.8) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 5 µM 0.173× (z -10.5) |
| [[Hs 766T (line)]] | wt | 34.8 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.130× (z -12.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.341× (z -9.1) |
| [[HT-29 (line)]] | alt | 28.0 | 1 | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.69× (z +9.4) | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -13.2) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.279× (z -9.2) |
| [[A-172 (line)]] | wt | 26.4 | 1 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 4.17× (z +9.0) | [[Homoharringtonine (drug)]] 5 µM 0.365× (z -8.9) ⚠ cell-cycle shift, explains ~26% of this change |
| [[HepG2_C3A (line)]] | wt | 42.2 | 0 | 3 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.116× (z -13.0) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.240× (z -9.0) |
| [[SK-MEL-2 (line)]] | alt | 26.9 | 0 | 3 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0641× (z -16.4) |
| [[SNU-1 (line)]] | wt | 38.1 | 0 | 3 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0988× (z -12.8) |
| [[SW1417 (line)]] | alt | 25.0 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -14.2) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.245× (z -8.8) |
| [[C-33 A (line)]] | alt | 61.4 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.290× (z -9.0) |
| [[RPMI-7951 (line)]] | alt | 19.7 | 0 | 2 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0373× (z -17.2) |
| [[AN3 CA (line)]] | alt | 41.9 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.109× (z -8.8) ⚠ toxic |
| [[C32 (line)]] | wt | 31.1 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.15× (z +8.9) | — |
| [[HS-578T (line)]] | alt | 13.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.125× (z -15.9) ⚠ cell-cycle shift, explains ~26% of this change |
| [[NCI-H2030 (line)]] | alt | 30.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.329× (z -10.1) ⚠ cell-cycle shift, explains ~26% of this change |
| [[SNU-423 (line)]] | alt | 19.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -9.8) ⚠ cell-cycle shift, explains ~26% of this change |
| [[SW 1271 (line)]] | alt | 94.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0800× (z -10.1) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 24.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.4 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.76 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 51.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 42.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 19.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4595), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TSEN2]] | +0.75 | +0.71 / +0.72 | both halves | 7e-06 |  |
| [[SERBP1]] | +0.71 | +0.59 / +0.68 | both halves | 7e-06 |  |
| [[CMSS1]] | +0.71 | +0.61 / +0.70 | both halves | 7e-06 |  |
| [[NARS2]] | +0.70 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[STX18-AS1]] | +0.68 | +0.72 / +0.64 | both halves | 7e-06 |  |
| [[DPH6]] | +0.68 | +0.72 / +0.64 | both halves | 7e-06 | same gene group |
| [[SNRPD1]] | +0.67 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[ZP3]] | +0.67 | +0.62 / +0.68 | both halves | 7e-06 |  |
| [[TMEM241]] | +0.66 | +0.49 / +0.67 | both halves | 1e-05 |  |
| [[MRPL24]] | +0.66 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[MDN1]] | +0.65 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[FXN]] | +0.64 | +0.55 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACOX1]] | -0.58 | -0.46 / -0.49 | both halves | 2e-05 |  |
| [[YPEL5]] | -0.57 | -0.44 / -0.58 | both halves | 3e-05 |  |
| [[ATOSA]] | -0.56 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[SHOX2]] | -0.54 | -0.44 / -0.41 | both halves | 4e-05 |  |
| [[MTMR11]] | -0.53 | -0.56 / -0.56 | both halves | 1e-05 |  |
| [[GNAS]] | -0.53 | -0.39 / -0.51 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ABLIM2]] | B | ABLIM2 activity raises CLYBL's level | lines that do not express ABLIM2 (13) vs lines expressing it (37) | 2.23× lower at baseline in the lines without ABLIM2 | 0.026 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: CAMSAP3, SLC9A2, MNX1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.585). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-11.2, -41.9); signed map (-6.7, -49.4). **Vector** length 94.4, 29.2% of its response variance represented; |z| ≥ 3 in 1,219 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.1 | -1.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.1 | +7.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.0 | +4.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.9 | +6.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.7 | +7.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.3 | -3.3 |
|  | [[EX229 (drug)]] 5 µM |  | +2.4 | +1.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.4 | +0.7 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -9.3 | -13.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -4.8 | -22.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.8 | -3.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.7 | -4.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.4 | -7.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.1 | -2.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.6 | -8.4 |
|  | [[Entrectinib (drug)]] 5 µM |  | -2.3 | -0.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.0 | +0.2 |

## What is on record

|  |  |
|---|---|
| Name | citramalyl-CoA lyase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q32.3 — chr13:99,606,669-99,909,459 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CLB |
| Gene groups (HGNC) | MicroRNA protein coding host genes; Thioester hydrolases; Acyltransferases; Oxo-acid lyases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N0X4](https://www.uniprot.org/uniprotkb/Q8N0X4) (Citramalyl-CoA lyase, mitochondrial):

> Mitochondrial enzyme required to detoxify vitamin B12-poisoning metabolites. Acts as a citramalyl-CoA lyase by converting citramalyl-CoA into acetyl-CoA and pyruvate in the C5-dicarboxylate catabolism pathway, a pathway required to detoxify itaconate, a vitamin B12-poisoning metabolite. Also acts as a malyl-CoA thioesterase to detoxify malyl-CoA, a side product of citric acid cycle enzymes, which is toxic for the vitamin B12-dependent enzyme MMUT. Also acts as a malate synthase in vitro, …

**Summary**, from NCBI Gene [171425](https://www.ncbi.nlm.nih.gov/gene/171425):

> Enables several functions, including (S)-citramalyl-CoA lyase activity; magnesium ion binding activity; and malate synthase activity. Involved in protein homotrimerization; regulation of cobalamin metabolic process; and toxic metabolite repair. Is active in mitochondrion. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:18355](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18355) · Entrez [171425](https://www.ncbi.nlm.nih.gov/gene/171425) · UniProt [Q8N0X4](https://www.uniprot.org/uniprotkb/Q8N0X4) · Ensembl [ENSG00000125246](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125246)

## Data

Gene col 4595: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4595); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4595, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4595]; `tensor/DDL_lfc|DDL_z.npy` [4595]; `embed/gene_vectors.npy` [4595]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4595 or target_col == 4595). Every well: [[CLYBL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CLYBL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
