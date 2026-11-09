---
symbol: "IWS1"
type: "gene"
col: 8649
ensembl_id: "ENSG00000163166"
name: "interacts with SUPT6H, CTD assembly factor 1"
location: "2q14.3"
module: 12
arm: "+"
pooled_cpm: 174.38
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 3
n_dd_up_clean: 16
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# IWS1

*interacts with SUPT6H, CTD assembly factor 1* — 2q14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.31× (z +27.9, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.454× (z -17.9, q 0e+00, down in 43 of 44 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 8 lines (NCI-H2030 0.217×, PANC-1 0.274×, SW48 0.126×, HEC-1-A 0.286×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (NCI-H2030 0.291×, HEC-1-A 0.311×, NCI-H460 0.328×, PANC-1 0.395×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (HEC-1-A 0.308×, SNU-1 0.174×; ⚠ toxic; transcription drop); [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (CHP-212 0.159×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PPIG]] (+0.68, fdr 7e-06), [[MRPL46]] (+0.68, fdr 1e-05), [[COIL]] (+0.67, fdr 1e-05); moves opposite to [[CTSB]] (-0.63, fdr 2e-05), [[TPGS2]] (-0.63, fdr 1e-05), [[ESYT1]] (-0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8649.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.31×** | +27.9 | 0e+00 | 48/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.06×** | +17.1 | 0e+00 | 48/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.10×** | +16.9 | 0e+00 | 48/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.03×** | +16.7 | 0e+00 | 47/48 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.82×** | +14.1 | 6e-43 | 47/48 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.65×** | +12.0 | 4e-31 | 46/49 (SW480, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.66×** | +12.0 | 4e-31 | 45/48 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.56×** | +10.6 | 3e-24 | 42/48 (LoVo, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.45×** | +8.8 | 1e-16 | 37/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.04×** | +8.8 | 1e-16 | 42/48 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.44×** | +8.6 | 6e-16 | 39/48 (A-172, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.43×** | +8.5 | 9e-16 | 42/48 (HOP62, LoVo, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.33×** | +6.4 | 6e-09 | 31/48 (SNU-423, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.29×** | +6.0 | 7e-08 | 28/48 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.29×** | +5.9 | 1e-07 | 26/48 (HOP62, SW 900, …) | all doses, stronger at high dose |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 1.20× | +4.3 | 6e-04 | 22/48 (LS 180, SW480, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.28×** | +4.1 | 0.001 | 28/49 (HOP62, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 3 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8649.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 8 lines (NCI-H2030 0.217×, PANC-1 0.274×, SW48 0.126×, HEC-1-A 0.286×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (NCI-H2030 0.291×, HEC-1-A 0.311×, NCI-H460 0.328×, PANC-1 0.395×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (HEC-1-A 0.308×, SNU-1 0.174×; ⚠ toxic; transcription drop); [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (CHP-212 0.159×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.454×** | -17.9 | 0e+00 | 43/44 (NCI-H2030, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.475×** | -17.6 | 0e+00 | 46/49 (NCI-H2030, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.607×** | -10.9 | 2e-25 | 40/45 (HEC-1-A, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 0.878× | -3.1 | 0.30 | 12/48 (NCI-H23, J82, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8649. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 187 | 10 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +21.0) | [[Dinaciclib (drug)]] 5 µM 0.331× (z -20.3) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 256 | 8 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +16.8) | [[Dinaciclib (drug)]] 5 µM 0.286× (z -21.3) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 185 | 5 | 6 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +17.2) | [[Dinaciclib (drug)]] 0.5 µM 0.384× (z -16.2) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 200 | 8 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +29.6) | [[Dinaciclib (drug)]] 5 µM 0.274× (z -24.1) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 173 | 9 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.10× (z +19.0) | [[Dinaciclib (drug)]] 0.5 µM 0.465× (z -12.8) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 237 | 4 | 5 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +15.1) | [[Dinaciclib (drug)]] 0.5 µM 0.422× (z -14.4) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 119 | 8 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +18.2) | [[Dinaciclib (drug)]] 5 µM 0.453× (z -9.1) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 174 | 7 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +21.7) | [[Dinaciclib (drug)]] 5 µM 0.250× (z -16.7) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 217 | 6 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +14.9) | [[Dinaciclib (drug)]] 0.5 µM 0.309× (z -16.9) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 293 | 4 | 5 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +16.3) | [[Dinaciclib (drug)]] 5 µM 0.217× (z -26.2) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 164 | 5 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.75× (z +15.5) | [[Dinaciclib (drug)]] 0.05 µM 0.368× (z -14.2) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 119 | 7 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +16.4) | [[Dinaciclib (drug)]] 5 µM 0.476× (z -10.6) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 206 | 5 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +23.3) | [[Dinaciclib (drug)]] 0.5 µM 0.328× (z -19.9) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 206 | 6 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +18.8) | [[Dinaciclib (drug)]] 5 µM 0.381× (z -11.9) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 163 | 6 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +17.7) | [[Dinaciclib (drug)]] 0.5 µM 0.474× (z -8.9) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 95.4 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.28× (z +22.6) | — |
| [[NCI-H23 (line)]] | alt | 198 | 6 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +21.6) | [[Dinaciclib (drug)]] 0.5 µM 0.390× (z -14.3) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 238 | 1 | 6 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +13.5) | [[Dinaciclib (drug)]] 5 µM 0.338× (z -18.2) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 196 | 5 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 0.5 µM 2.13× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.381× (z -13.3) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 91.2 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.54× (z +22.4) | — |
| [[hTERT-HPNE (line)]] | wt | 134 | 5 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +13.2) | [[Dinaciclib (drug)]] 5 µM 0.422× (z -9.1) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 141 | 3 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +18.4) | [[Dinaciclib (drug)]] 0.5 µM 0.408× (z -15.2) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 171 | 3 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +14.4) | [[Dinaciclib (drug)]] 0.05 µM 0.174× (z -18.9) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 171 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +16.0) | [[Dinaciclib (drug)]] 5 µM 0.507× (z -11.3) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 146 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +20.3) | [[Dinaciclib (drug)]] 0.5 µM 0.522× (z -9.5) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 201 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +18.1) | [[Dinaciclib (drug)]] 5 µM 0.228× (z -19.1) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 172 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +16.4) | [[Dinaciclib (drug)]] 0.5 µM 0.430× (z -10.2) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 117 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +15.8) | [[Dinaciclib (drug)]] 5 µM 0.327× (z -12.1) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 146 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +19.5) | [[Dinaciclib (drug)]] 0.05 µM 0.374× (z -13.4) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 189 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +15.1) | [[Dinaciclib (drug)]] 5 µM 0.346× (z -15.7) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 149 | 5 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 3.12× (z +12.6) | — |
| [[RKO (line)]] | wt | 210 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +19.1) | [[Dinaciclib (drug)]] 0.5 µM 0.459× (z -10.7) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 189 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +18.3) | [[Dinaciclib (drug)]] 0.5 µM 0.381× (z -13.1) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 92.0 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +15.5) | — |
| [[HCT15 (line)]] | alt | 150 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +15.9) | — |
| [[KATO III (line)]] | alt | 92.9 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +13.5) | [[Dinaciclib (drug)]] 5 µM 0.364× (z -12.4) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 129 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +16.4) | — |
| [[SW48 (line)]] | wt | 183 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +13.4) | [[Dinaciclib (drug)]] 5 µM 0.126× (z -21.4) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 147 | 3 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.65× (z +13.5) | — |
| [[C32 (line)]] | wt | 130 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +11.5) | — |
| [[CHP-212 (line)]] | wt | 159 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +9.3) | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.159× (z -12.1) |
| [[AN3 CA (line)]] | alt | 194 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.240× (z -12.9) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 180 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +13.3) | — |
| [[Panc 03.27 (line)]] | alt | 176 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.58× (z +9.2) | — |
| [[SHP-77 (line)]] | alt | 150 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.525× (z -8.7) ⚠ toxic; transcription drop |
| [[NCI-H2122 (line)]] | alt | 192 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 176 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 216 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 172 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 243 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8649), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPIG]] | +0.68 | +0.60 / +0.69 | both halves | 7e-06 |  |
| [[MRPL46]] | +0.68 | +0.51 / +0.71 | both halves | 1e-05 |  |
| [[COIL]] | +0.67 | +0.52 / +0.66 | both halves | 1e-05 |  |
| [[ZC3H13]] | +0.67 | +0.61 / +0.65 | both halves | 7e-06 | STRING 403 |
| [[PPP4R2]] | +0.66 | +0.58 / +0.65 | both halves | 7e-06 |  |
| [[DHX36]] | +0.66 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[PIGBOS1]] | +0.65 | +0.50 / +0.66 | both halves | 1e-05 |  |
| [[RBM25]] | +0.65 | +0.69 / +0.59 | both halves | 7e-06 |  |
| [[RDH14]] | +0.64 | +0.52 / +0.64 | both halves | 1e-05 |  |
| [[MRPS18C]] | +0.64 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[C1orf131]] | +0.63 | +0.45 / +0.71 | both halves | 3e-05 |  |
| [[OBI1]] | +0.63 | +0.51 / +0.65 | both halves | 1e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CTSB]] | -0.63 | -0.49 / -0.65 | both halves | 2e-05 | pathway: Affinity selection of immunoglobulins |
| [[TPGS2]] | -0.63 | -0.56 / -0.59 | both halves | 1e-05 |  |
| [[ESYT1]] | -0.62 | -0.62 / -0.56 | both halves | 1e-05 |  |
| [[FKBP1A]] | -0.62 | -0.50 / -0.59 | both halves | 1e-05 |  |
| [[KIAA1191]] | -0.57 | -0.51 / -0.68 | both halves | 1e-05 |  |
| [[VAMP3]] | -0.57 | -0.46 / -0.55 | both halves | 2e-05 |  |
| [[IDS]] | -0.57 | -0.46 / -0.60 | both halves | 3e-05 |  |
| [[TMBIM6]] | -0.56 | -0.47 / -0.63 | both halves | 2e-05 |  |
| [[OAT]] | -0.56 | -0.44 / -0.59 | both halves | 3e-05 |  |
| [[RALY]] | -0.55 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[APLP2]] | -0.55 | -0.40 / -0.58 | both halves | 5e-05 |  |
| [[GNS]] | -0.55 | -0.41 / -0.59 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.595). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-38.1, 0.9); signed map (-0.5, -18.1). **Vector** length 100, 35.0% of its response variance represented; |z| ≥ 3 in 1,304 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.6 | +6.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.2 | +17.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.8 | +27.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.6 | +1.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +4.2 | +2.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.1 | +0.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.6 | -0.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.5 | +0.1 |
| fall | [[BAY1125976 (drug)]] 5 µM |  | -3.7 | -2.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -3.2 | -1.6 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -3.2 | -2.0 |
|  | [[Fusidic acid (drug)]] 5 µM |  | -3.0 | -2.6 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.0 | +10.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.7 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | interacts with SUPT6H, CTD assembly factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q14.3 — chr2:127,436,207-127,526,886 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp761G0123, FLJ10006, FLJ14655, FLJ32319 |
| Reactome | 7 pathways, smallest: Formation of RNA Pol II elongation complex; RNA Polymerase II Transcription Elongation; RNA Polymerase II Pre-transcription Events |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96ST2](https://www.uniprot.org/uniprotkb/Q96ST2) (Protein IWS1 homolog):

> Transcription factor which plays a key role in defining the composition of the RNA polymerase II (RNAPII) elongation complex and in modulating the production of mature mRNA transcripts. Acts as an assembly factor to recruit various factors to the RNAPII elongation complex and is recruited to the complex via binding to the transcription elongation factor SUPT6H bound to the C-terminal domain (CTD) of the RNAPII subunit RPB1 (POLR2A). The SUPT6H:IWS1:CTD complex recruits mRNA export factors …

**Summary**, from NCBI Gene [55677](https://www.ncbi.nlm.nih.gov/gene/55677):

> Involved in regulation of mRNA export from nucleus; regulation of mRNA processing; and transcription elongation-coupled chromatin remodeling. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25467](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25467) · Entrez [55677](https://www.ncbi.nlm.nih.gov/gene/55677) · UniProt [Q96ST2](https://www.uniprot.org/uniprotkb/Q96ST2) · Ensembl [ENSG00000163166](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163166)

## Data

Gene col 8649: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8649); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8649, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8649]; `tensor/DDL_lfc|DDL_z.npy` [8649]; `embed/gene_vectors.npy` [8649]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8649 or target_col == 8649). Every well: [[IWS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IWS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
