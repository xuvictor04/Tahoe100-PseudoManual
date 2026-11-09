---
symbol: "CDYL"
type: "gene"
col: 7683
ensembl_id: "ENSG00000153046"
name: "chromodomain Y like"
location: "6p25.1"
module: 115
arm: "+"
pooled_cpm: 141.87
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 4
n_dd_up_clean: 8
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/115"]
generated_by: "tahoemap"
---

# CDYL

*chromodomain Y like* — 6p25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.30× (z +8.7, q 2e-15, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.536× (z -14.7, q 0e+00, down in 41 of 49 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (A-427 0.0682×, Panc 03.27 0.223×, C-33 A 0.215×, A498 0.316×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (NCI-H23 0.314×, NCI-H2347 0.338×, NCI-H460 0.377×, SW 1271 0.154×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H2347 0.358×; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 1 line (A-427 0.463×); [[Phenytoin (sodium) (drug)]] 5 µM in 1 line (SW 1088 0.0691×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CRACD]] (+0.63, fdr 1e-05), [[DOCK9]] (+0.62, fdr 1e-05), [[SRPK2]] (+0.61, fdr 7e-06); moves opposite to [[COG4]] (-0.56, fdr 1e-05), [[GOLGA1]] (-0.56, fdr 1e-05), [[KRBOX4]] (-0.54, fdr 2e-05).
> It is in [[Module 115]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7683.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.30×** | +8.7 | 2e-15 | 38/48 (KATO III, LOX-IMVI, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.31×** | +6.3 | 8e-08 | 33/49 (KATO III, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | 1.19× | +5.8 | 2e-06 | 20/48 (PANC-1, NCI-H1573, …) | rises with dose | low cells (technical?) |
| [[TAK-901 (drug)]] 5 µM |  | **1.56×** | +5.4 | 8e-06 | 28/49 (Hs 766T, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.24×** | +5.0 | 6e-05 | 23/48 (HT-29, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.23×** | +4.9 | 8e-05 | 25/48 (C32, Hs 766T, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.22×** | +4.6 | 3e-04 | 25/48 (CFPAC-1, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.23×** | +4.6 | 3e-04 | 25/47 (RPMI-7951, H4, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.44×** | +4.5 | 4e-04 | 26/48 (C32, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.43×** | +4.4 | 6e-04 | 23/45 (J82, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~14% here); noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.21×** | +4.4 | 6e-04 | 21/48 (PANC-1, A498, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.21×** | +4.3 | 1e-03 | 24/48 (NCI-H1573, KATO III, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +4.0 | 0.003 | 21/48 (Hs 766T, C32, …) | two highest doses |  |
| [[Brivudine (drug)]] 5 µM |  | **1.36×** | +3.8 | 0.007 | 23/49 (CFPAC-1, NCI-H1792, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +3.2 | 0.053 | 19/48 (Hs 766T, C32, …) | two highest doses | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.14× | +3.2 | 0.056 | 17/48 (KATO III, J82, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.10× | +3.0 | 0.070 | 10/49 (COLO 205, Panc 03.27, …) | rises with dose |  |
| [[Irinotecan (hydrochloride) (drug)]] 0.5 µM |  | 1.14× | +3.0 | 0.070 | 4/48 (J82, A-172, …) | inconsistent across doses |  |
| [[Penfluridol (drug)]] 5 µM |  | 1.14× | +3.0 | 0.072 | 10/47 (KATO III, HOP62, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 8 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7683.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (A-427 0.0682×, Panc 03.27 0.223×, C-33 A 0.215×, A498 0.316×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (NCI-H23 0.314×, NCI-H2347 0.338×, NCI-H460 0.377×, SW 1271 0.154×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H2347 0.358×; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 1 line (A-427 0.463×); [[Phenytoin (sodium) (drug)]] 5 µM in 1 line (SW 1088 0.0691×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.536×** | -14.7 | 0e+00 | 41/49 (NCI-H23, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.553×** | -13.4 | 2e-38 | 36/44 (A-427, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.706×** | -7.6 | 7e-12 | 31/45 (NCI-H2347, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.777×** | -5.7 | 2e-06 | 28/47 (SW1417, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | 0.887× | -4.0 | 0.008 | 4/48 (Panc 03.27, SW48, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | 0.851× | -3.8 | 0.013 | 22/48 (RKO, NCI-H1573, …) | inconsistent across doses |  |
| [[Sulfatinib (drug)]] 5 µM |  | 0.853× | -3.6 | 0.025 | 13/49 (NCI-H2347, KATO III, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | 0.862× | -3.5 | 0.032 | 19/48 (LoVo, SNU-1, …) | inconsistent across doses |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 0.879× | -3.0 | 0.15 | 13/48 (C-33 A, HepG2/C3A, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7683. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 213 | 4 (3 ⚠) | 6 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.29× (z +23.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 3.65× (z +9.4) | [[Dinaciclib (drug)]] 0.5 µM 0.338× (z -15.1) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 136 | 2 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +17.4) ⚠ cell-cycle shift, explains ~0% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.530× (z -12.3) ⚠ cell-cycle shift, explains ~25% of this change |
| [[Panc 03.27 (line)]] | alt | 270 | 1 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +18.2) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.223× (z -18.3) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 197 | 1 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.71× (z +10.1) ⚠ cell-cycle shift, explains ~0% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.376× (z -12.7) ⚠ toxic |
| [[A-172 (line)]] | wt | 102 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +14.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 1.58× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.361× (z -12.9) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 131 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0682× (z -34.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.463× (z -10.2) |
| [[A498 (line)]] | wt | 113 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +14.8) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.316× (z -15.6) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 169 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +13.4) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.412× (z -10.0) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 219 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +9.3) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.360× (z -10.1) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 113 | 2 | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 7.44× (z +12.0) | [[Dinaciclib (drug)]] 0.5 µM 0.456× (z -9.0) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 180 | 0 | 3 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.385× (z -10.1) ⚠ toxic |
| [[J82 (line)]] | alt | 223 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.63× (z +10.7) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.461× (z -11.7) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 121 | 1 | 2 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.58× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.323× (z -15.2) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 94.0 | 0 | 3 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.558× (z -10.3) ⚠ cell-cycle shift, explains ~25% of this change |
| [[PANC-1 (line)]] | alt | 143 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 2.60× (z +9.9) | [[Dinaciclib (drug)]] 0.5 µM 0.653× (z -8.5) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 178 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.302× (z -15.4) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 206 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.314× (z -12.2) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 76.4 | 2 (2 ⚠) | 0 | [[Digitoxin (drug)]] 0.05 µM 3.36× (z +10.0) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[Hs 766T (line)]] | wt | 125 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.20× (z +10.3) | [[Dinaciclib (drug)]] 5 µM 0.380× (z -11.1) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 136 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.447× (z -10.5) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 152 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.403× (z -11.8) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 217 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.314× (z -15.9) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 141 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.397× (z -12.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW 1271 (line)]] | alt | 246 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.154× (z -12.7) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 159 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.215× (z -16.7) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 75.3 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 1.63× (z +8.5) | — |
| [[CHP-212 (line)]] | wt | 124 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.230× (z -8.8) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 93.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +8.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[KATO III (line)]] | alt | 114 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 1.79× (z +10.7) | — |
| [[LoVo (line)]] | wt | 161 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.467× (z -12.1) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 91.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.511× (z -11.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 112 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.377× (z -13.1) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 143 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.492× (z -8.9) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 96.8 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.24× (z +8.5) ⚠ toxic | — |
| [[SHP-77 (line)]] | alt | 127 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.391× (z -10.7) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 79.5 | 0 | 1 | — | [[Phenytoin (sodium) (drug)]] 5 µM 0.0691× (z -9.3) |
| [[SW 900 (line)]] | alt | 115 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.418× (z -10.3) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 107 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.518× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 133 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 166 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 176 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 146 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 67.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 169 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 100 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 196 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 151 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 118 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7683), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CRACD]] | +0.63 | +0.65 / +0.51 | both halves | 1e-05 |  |
| [[DOCK9]] | +0.62 | +0.68 / +0.49 | both halves | 1e-05 |  |
| [[SRPK2]] | +0.61 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[CMTM8]] | +0.59 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[NCK2]] | +0.59 | +0.69 / +0.47 | both halves | 2e-05 |  |
| [[TSPAN14]] | +0.59 | +0.64 / +0.46 | both halves | 3e-05 |  |
| [[TRAK1]] | +0.58 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[PACC1]] | +0.57 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[LRP12]] | +0.57 | +0.63 / +0.45 | both halves | 3e-05 |  |
| [[RNF2]] | +0.56 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[GAB2]] | +0.56 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[ARHGAP44]] | +0.56 | +0.58 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COG4]] | -0.56 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[GOLGA1]] | -0.56 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[KRBOX4]] | -0.54 | -0.48 / -0.56 | both halves | 2e-05 |  |
| [[PPP4R3B]] | -0.52 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[TMEM91]] | -0.51 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[ODR4]] | -0.51 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[DYNC2I1]] | -0.51 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[SENP2]] | -0.50 | -0.55 / -0.42 | both halves | 4e-05 |  |
| [[SAFB2]] | -0.50 | -0.54 / -0.42 | both halves | 4e-05 |  |
| [[BBOF1]] | -0.50 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[STK19]] | -0.50 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[MYNN]] | -0.49 | -0.46 / -0.51 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 115]]; 42 genes; every member is in the + arm (projection on the module's main direction 0.621). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-7.2, -3.0); signed map (-17.2, 39.7). **Vector** length 107, 30.9% of its response variance represented; |z| ≥ 3 in 1,124 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.0 | +8.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.9 | +6.3 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +6.5 | +4.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +6.5 | +5.8 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +6.0 | +3.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.5 | +3.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.7 | +0.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.7 | +1.6 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.5 | +1.5 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.5 | +0.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.4 | -13.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -3.9 | -14.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | -3.9 | -3.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -3.8 | -7.6 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.2 | -1.6 |
|  | [[Sulfatinib (drug)]] 5 µM |  | -2.1 | -3.6 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | -2.0 | -2.4 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -1.7 | -3.0 |
|  | [[Vilanterol (drug)]] 5 µM |  | -1.6 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | chromodomain Y like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p25.1 — chr6:4,706,159-4,955,551 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP586C1622, CDYL1 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y232](https://www.uniprot.org/uniprotkb/Q9Y232) (Chromodomain Y-like protein):

> [Isoform 2]: Chromatin reader protein that recognizes and binds histone H3 trimethylated at 'Lys-9', dimethylated at 'Lys-27' and trimethylated at 'Lys-27' (H3K9me3, H3K27me2 and H3K27me3, respectively). Part of multimeric repressive chromatin complexes, where it is required for transmission and restoration of repressive histone marks, thereby preserving the epigenetic landscape. Required for chromatin targeting and maximal enzymatic activity of Polycomb repressive complex 2 (PRC2); acts as a …

**Summary**, from NCBI Gene [9425](https://www.ncbi.nlm.nih.gov/gene/9425):

> Chromodomain Y is a primate-specific Y-chromosomal gene family expressed exclusively in the testis and implicated in infertility. Although the Y-linked genes are testis-specific, this autosomal gene is ubiquitously expressed. The Y-linked genes arose by retrotransposition of an mRNA from this gene, followed by amplification of the retroposed gene. Proteins encoded by this gene superfamily possess a chromodomain, a motif implicated in chromatin binding and gene suppression, and a catalytic …

**Accessions** — [HGNC:1811](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1811) · Entrez [9425](https://www.ncbi.nlm.nih.gov/gene/9425) · UniProt [Q9Y232](https://www.uniprot.org/uniprotkb/Q9Y232) · Ensembl [ENSG00000153046](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000153046)

## Data

Gene col 7683: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7683); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7683, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7683]; `tensor/DDL_lfc|DDL_z.npy` [7683]; `embed/gene_vectors.npy` [7683]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7683 or target_col == 7683). Every well: [[CDYL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDYL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
