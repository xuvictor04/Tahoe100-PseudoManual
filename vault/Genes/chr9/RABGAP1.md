---
symbol: "RABGAP1"
type: "gene"
col: 242
ensembl_id: "ENSG00000011454"
name: "RAB GTPase activating protein 1"
location: "9q33.2-q33.3"
module: 59
arm: "+"
pooled_cpm: 195.78
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 7
n_dd_up_clean: 10
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/059"]
generated_by: "tahoemap"
---

# RABGAP1

*RAB GTPase activating protein 1* — 9q33.2-q33.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.77× (z +19.1, q 0e+00, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.510× (z -15.9, q 0e+00, down in 46 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.779× (z -8.4, q 9e-15, down in 32 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (H4 0.148×, SW480 0.315×, NCI-H460 0.346×, Panc 03.27 0.298×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (COLO 205 0.274×, SW480 0.414×, NCI-H1573 0.361×, HCT15 0.305×, …; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 5 lines (A549 0.540×, LOX-IMVI 0.637×, hTERT-HPNE 0.586×, LoVo 0.687×, …); [[Simotinib (drug)]] 0.05 µM in 1 line (SW 1088 0.0724×); [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (CHP-212 0.274×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[VPS41]] (+0.61, fdr 7e-06), [[FNIP1]] (+0.59, fdr 1e-05), [[HDAC8]] (+0.56, fdr 6e-05); moves opposite to [[PNP]] (-0.55, fdr 1e-05), [[TBC1D4]] (-0.54, fdr 1e-05), [[BEND3]] (-0.54, fdr 4e-05).
> It sits in the **+** arm of [[Module 059]] (Amino acids regulate mTORC1).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 242.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.77×** | +19.1 | 0e+00 | 44/48 (NCI-H460, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.59×** | +10.9 | 2e-25 | 44/48 (COLO 205, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.44×** | +8.6 | 1e-15 | 44/48 (AsPC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.38×** | +7.6 | 4e-12 | 38/48 (RKO, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.38×** | +7.5 | 9e-12 | 34/48 (NCI-H460, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.25×** | +7.4 | 2e-11 | 29/48 (LOX-IMVI, NCI-H460, …) | all doses, stronger at high dose | low cells (technical?) |
| [[TAK-901 (drug)]] 5 µM |  | **2.19×** | +7.2 | 4e-11 | 40/49 (HEC-1-A, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.31×** | +6.4 | 1e-08 | 38/48 (NCI-H460, RKO, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.29×** | +6.0 | 1e-07 | 32/48 (BT-474, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.29×** | +5.9 | 2e-07 | 30/48 (AsPC-1, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.28×** | +5.9 | 2e-07 | 28/48 (NCI-H1573, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.28×** | +5.7 | 4e-07 | 30/48 (AsPC-1, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.69×** | +4.8 | 6e-05 | 30/48 (HEC-1-A, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~40% of this change | 1.18× | +3.8 | 0.005 | 16/49 (LOX-IMVI, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.10× | +3.1 | 0.074 | 3/48 (SW480, Hs 766T, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 7 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 242.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (H4 0.148×, SW480 0.315×, NCI-H460 0.346×, Panc 03.27 0.298×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (COLO 205 0.274×, SW480 0.414×, NCI-H1573 0.361×, HCT15 0.305×, …; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 5 lines (A549 0.540×, LOX-IMVI 0.637×, hTERT-HPNE 0.586×, LoVo 0.687×, …); [[Simotinib (drug)]] 0.05 µM in 1 line (SW 1088 0.0724×); [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (CHP-212 0.274×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.510×** | -15.9 | 0e+00 | 46/49 (COLO 205, SW480, …) | all doses, flat | cell-cycle shift (explains ~23% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.511×** | -15.2 | 0e+00 | 39/44 (H4, SW480, …) | all doses, flat | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.506×** | -14.6 | 0e+00 | 40/45 (NCI-H23, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~15% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.779×** | -8.4 | 9e-15 | 32/49 (A549, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~39% of this change | **0.795×** | -5.4 | 6e-06 | 29/48 (Panc 03.27, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~6% of this change | **0.818×** | -4.6 | 5e-04 | 24/47 (HCT15, SW480, …) | rises with dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.746×** | -4.2 | 0.002 | 36/48 (HCT15, CFPAC-1, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | 0.851× | -3.8 | 0.009 | 18/48 (NCI-H1573, SW 1271, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.851× | -3.7 | 0.014 | 22/48 (NCI-H1792, NCI-H1573, …) | top dose only |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 0.872× | -3.3 | 0.065 | 15/47 (CFPAC-1, NCI-H460, …) | two highest doses |  |
| [[Mebendazole (drug)]] 5 µM |  | 0.871× | -3.1 | 0.085 | 11/48 (PANC-1, SW480, …) | top dose only |  |
| [[Peretinoin (drug)]] 5 µM |  | 0.875× | -3.1 | 0.11 | 18/47 (NCI-H460, LOX-IMVI, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 242. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 195 | 7 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.92× (z +36.2) | [[Dinaciclib (drug)]] 5 µM 0.346× (z -19.1) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 205 | 8 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +22.2) | [[Dinaciclib (drug)]] 0.5 µM 0.465× (z -10.5) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 212 | 5 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.21× (z +13.2) | [[Dinaciclib (drug)]] 0.05 µM 0.396× (z -14.0) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 161 | 6 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +20.4) | [[Dinaciclib (drug)]] 0.5 µM 0.361× (z -15.5) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 235 | 3 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.70× (z +12.7) | [[Dinaciclib (drug)]] 0.5 µM 0.467× (z -12.9) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 202 | 2 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +12.6) | [[Dinaciclib (drug)]] 0.05 µM 0.348× (z -11.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.586× (z -9.2) |
| [[NCI-H1792 (line)]] | alt | 155 | 4 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.38× (z +13.2) | [[Dinaciclib (drug)]] 5 µM 0.428× (z -12.4) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 149 | 3 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +14.9) | [[Dinaciclib (drug)]] 0.05 µM 0.232× (z -18.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 233 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +20.7) | [[Dinaciclib (drug)]] 5 µM 0.405× (z -13.8) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 436 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +16.4) | — |
| [[COLO 205 (line)]] | alt | 317 | 4 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +23.0) | [[Dinaciclib (drug)]] 0.5 µM 0.274× (z -18.4) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 226 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +10.3) | [[Dinaciclib (drug)]] 0.5 µM 0.305× (z -15.4) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 207 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.27× (z +23.4) | [[Dinaciclib (drug)]] 0.5 µM 0.514× (z -9.3) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 185 | 1 (1 ⚠) | 4 (3 ⚠) | [[Selinexor (drug)]] 5 µM 1.60× (z +10.6) ⚠ cell-cycle shift, explains ~40% of this change | [[Dinaciclib (drug)]] 5 µM 0.354× (z -16.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.637× (z -10.2) |
| [[MIA PaCa-2 (line)]] | alt | 225 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +17.0) | [[Dinaciclib (drug)]] 0.05 µM 0.488× (z -10.3) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 232 | 1 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.77× (z +12.4) | [[Dinaciclib (drug)]] 5 µM 0.298× (z -18.0) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 268 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.63× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.394× (z -13.7) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 254 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.61× (z +11.7) | [[Dinaciclib (drug)]] 5 µM 0.315× (z -19.7) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 128 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +15.4) | [[Dinaciclib (drug)]] 5 µM 0.494× (z -9.4) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 159 | 2 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.06× (z +11.1) | [[Dinaciclib (drug)]] 0.05 µM 0.506× (z -9.5) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 105 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +20.2) | — |
| [[HS-578T (line)]] | alt | 136 | 2 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 1.90× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.429× (z -11.5) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 275 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.65× (z +10.6) | [[Dinaciclib (drug)]] 5 µM 0.454× (z -11.5) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 247 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +20.0) | [[Dinaciclib (drug)]] 0.5 µM 0.493× (z -11.3) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 271 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.62× (z +10.7) | [[Dinaciclib (drug)]] 5 µM 0.451× (z -12.0) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 188 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +15.7) | [[Dinaciclib (drug)]] 0.5 µM 0.359× (z -15.3) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 156 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +20.1) | [[Dinaciclib (drug)]] 0.05 µM 0.377× (z -17.1) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 177 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.62× (z +10.6) | [[Dinaciclib (drug)]] 0.05 µM 0.331× (z -15.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.540× (z -13.6) |
| [[C32 (line)]] | wt | 181 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.449× (z -11.0) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 212 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +12.2) | [[Dinaciclib (drug)]] 5 µM 0.148× (z -22.2) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 165 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +15.1) | [[Dinaciclib (drug)]] 0.5 µM 0.510× (z -10.4) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 190 | 1 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 1.85× (z +9.7) | [[Dinaciclib (drug)]] 0.5 µM 0.561× (z -9.2) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 247 | 0 | 2 (1 ⚠) | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.274× (z -10.3) |
| [[LS 180 (line)]] | wt | 223 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.278× (z -17.0) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 151 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +14.2) | [[Dinaciclib (drug)]] 0.05 µM 0.361× (z -11.9) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 322 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +8.8) | [[Dinaciclib (drug)]] 0.5 µM 0.183× (z -12.8) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 230 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.441× (z -12.9) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 123 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.513× (z -9.4) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 97.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +16.9) | — |
| [[RPMI-7951 (line)]] | alt | 165 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +14.9) | — |
| [[SNU-1 (line)]] | wt | 168 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.24× (z +9.4) | — |
| [[SW 1088 (line)]] | alt | 172 | 0 | 1 | — | [[Simotinib (drug)]] 0.05 µM 0.0724× (z -12.4) |
| [[SW 900 (line)]] | alt | 147 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.511× (z -8.9) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 258 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 180 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 121 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 192 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 204 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 199 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 155 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 242), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 5 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VPS41]] | +0.61 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[FNIP1]] | +0.59 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[HDAC8]] | +0.56 | +0.38 / +0.64 | both halves | 6e-05 |  |
| [[SETDB1]] | +0.56 | +0.62 / +0.45 | both halves | 3e-05 |  |
| [[RUFY1]] | +0.56 | +0.64 / +0.49 | both halves | 1e-05 |  |
| [[FMC1]] | +0.56 | +0.65 / +0.50 | both halves | 1e-05 |  |
| [[ARFGEF2]] | +0.56 | +0.63 / +0.49 | both halves | 1e-05 |  |
| [[TSC1]] | +0.56 | +0.66 / +0.46 | both halves | 3e-05 | pathway: HALLMARK_MITOTIC_SPINDLE |
| [[N4BP2L2]] | +0.55 | +0.63 / +0.50 | both halves | 1e-05 |  |
| [[DDX17]] | +0.55 | +0.55 / +0.38 | both halves | 6e-05 |  |
| [[SAT2]] | +0.54 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[TMEM126A]] | +0.54 | +0.46 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PNP]] | -0.55 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[TBC1D4]] | -0.54 | -0.52 / -0.51 | both halves | 1e-05 | same gene group |
| [[BEND3]] | -0.54 | -0.59 / -0.42 | both halves | 4e-05 |  |
| [[DOCK9]] | -0.52 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[CORO2B]] | -0.51 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[PTDSS1]] | -0.51 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[LOXL1]] | -0.50 | -0.43 / -0.54 | both halves | 3e-05 |  |
| [[DUSP7]] | -0.50 | -0.49 / -0.54 | both halves | 1e-05 |  |
| [[ACOT7]] | -0.49 | -0.55 / -0.46 | both halves | 3e-05 |  |
| [[TTL]] | -0.49 | -0.40 / -0.49 | both halves | 5e-05 |  |
| [[MGAT5B]] | -0.48 | -0.44 / -0.40 | both halves | 5e-05 |  |
| [[ADCY3]] | -0.48 | -0.56 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 059]] — Amino acids regulate mTORC1; 80 genes; this gene is in the **+** arm (projection on the module's main direction 0.490). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-18.4, 15.7); signed map (-1.8, -6.4). **Vector** length 98.3, 32.7% of its response variance represented; |z| ≥ 3 in 1,192 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | +9.4 | +7.4 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | +7.3 | +6.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +4.8 | +10.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +4.6 | +7.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.4 | +5.9 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +3.7 | +1.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +3.1 | +2.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.9 | +2.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.7 | +1.6 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +2.6 | +1.5 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.7 | -8.4 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | -4.2 | -3.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.8 | -2.8 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -3.5 | -2.5 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | -3.3 | -3.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.0 | -3.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.8 | -2.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.5 | -2.2 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -2.4 | -0.8 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.3 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | RAB GTPase activating protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q33.2-q33.3 — chr9:122,940,833-123,104,866 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GAPCenA, TBC1D11 |
| Gene groups (HGNC) | TBC1 domain family members |
| Hallmark sets | MITOTIC_SPINDLE |
| Reactome | 4 pathways, smallest: TBC/RABGAPs; Rab regulation of trafficking; Membrane Trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y3P9](https://www.uniprot.org/uniprotkb/Q9Y3P9) (Rab GTPase-activating protein 1):

> May act as a GTPase-activating protein of RAB6A. May play a role in microtubule nucleation by centrosome. May participate in a RAB6A-mediated pathway involved in the metaphase-anaphase transition.

**Summary**, from NCBI Gene [23637](https://www.ncbi.nlm.nih.gov/gene/23637):

> Enables GTPase activator activity and small GTPase binding activity. Predicted to be involved in G protein-coupled receptor signaling pathway. Located in cytosol. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:17155](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17155) · Entrez [23637](https://www.ncbi.nlm.nih.gov/gene/23637) · UniProt [Q9Y3P9](https://www.uniprot.org/uniprotkb/Q9Y3P9) · Ensembl [ENSG00000011454](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000011454)

## Data

Gene col 242: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 242); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 242, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 242]; `tensor/DDL_lfc|DDL_z.npy` [242]; `embed/gene_vectors.npy` [242]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 242 or target_col == 242). Every well: [[RABGAP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RABGAP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
