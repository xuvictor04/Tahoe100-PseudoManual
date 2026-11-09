---
symbol: "TET3"
type: "gene"
col: 11926
ensembl_id: "ENSG00000187605"
name: "tet methylcytosine dioxygenase 3"
location: "2p13.1"
module: 56
arm: "+"
pooled_cpm: 98.44
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 4
n_dd_up_clean: 11
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/056"]
generated_by: "tahoemap"
---

# TET3

*tet methylcytosine dioxygenase 3* — 2p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.19× (z +36.7, q 0e+00, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.481× (z -16.4, q 0e+00, down in 41 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.856× (z -4.9, q 1e-04, down in 21 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 5 lines (LoVo 0.161×, HEC-1-A 0.257×, LS 180 0.168×, NCI-H23 0.174×, …; ⚠ cell-cycle shift, explains ~12% of this change); [[Panobinostat (drug)]] 0.5 µM in 4 lines (HEC-1-A 0.217×, NCI-H23 0.130×, LoVo 0.196×, LS 180 0.194×; ⚠ cell-cycle shift, explains ~0% of this change); [[Tucidinostat (drug)]] 5 µM in 4 lines (LS 180 0.563×, LoVo 0.616×, SW1417 0.635×, SW480 0.675×); [[Budesonide (drug)]] 0.05 µM in 1 line (HOP62 0.369×); [[Clobetasol propionate (drug)]] 0.5 µM in 1 line (HOP62 0.381×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF629]] (+0.58, fdr 5e-05), [[SLC25A13]] (+0.57, fdr 1e-05), [[FJX1]] (+0.56, fdr 6e-05); moves opposite to [[LMAN1]] (-0.63, fdr 1e-05), [[SEC23A]] (-0.63, fdr 2e-05), [[COPB1]] (-0.62, fdr 1e-05).
> It is in [[Module 056]], a single-armed module (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[WWC1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 6 with an alert ⚠; shown: the 15 strongest. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11926.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.19×** | +36.7 | 0e+00 | 44/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **3.92×** | +29.4 | 0e+00 | 47/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **8.78×** | +25.4 | 0e+00 | 48/49 (HEC-1-A, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.17×** | +17.4 | 0e+00 | 43/48 (NCI-H460, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **3.70×** | +15.3 | 0e+00 | 47/48 (HEC-1-A, NCI-H2347, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.98×** | +15.2 | 0e+00 | 44/48 (NCI-H460, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.75×** | +12.5 | 4e-34 | 43/48 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.70×** | +11.9 | 1e-30 | 40/48 (NCI-H460, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.50×** | +9.1 | 4e-18 | 33/48 (NCI-H460, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.52×** | +9.1 | 7e-18 | 35/47 (NCI-H460, SHP-77, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.46×** | +8.5 | 8e-16 | 29/48 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.33×** | +6.1 | 6e-08 | 33/48 (NCI-H460, SW 900, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.24×** | +4.9 | 4e-05 | 25/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.25×** | +4.6 | 1e-04 | 23/47 (SW48, SW480, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **1.20×** | +4.1 | 0.001 | 18/48 (AsPC-1, PANC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 6 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11926.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 5 lines (LoVo 0.161×, HEC-1-A 0.257×, LS 180 0.168×, NCI-H23 0.174×, …; ⚠ cell-cycle shift, explains ~12% of this change); [[Panobinostat (drug)]] 0.5 µM in 4 lines (HEC-1-A 0.217×, NCI-H23 0.130×, LoVo 0.196×, LS 180 0.194×; ⚠ cell-cycle shift, explains ~0% of this change); [[Tucidinostat (drug)]] 5 µM in 4 lines (LS 180 0.563×, LoVo 0.616×, SW1417 0.635×, SW480 0.675×); [[Budesonide (drug)]] 0.05 µM in 1 line (HOP62 0.369×); [[Clobetasol propionate (drug)]] 0.5 µM in 1 line (HOP62 0.381×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.481×** | -16.4 | 0e+00 | 41/49 (NCI-H1792, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.578×** | -11.8 | 1e-29 | 31/44 (KATO III, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.597×** | -10.7 | 2e-24 | 31/45 (NCI-H2030, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | 0.856× | -4.9 | 1e-04 | 21/48 (LS 180, LoVo, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.813×** | -4.6 | 4e-04 | 23/49 (HOP62, SW 1088, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.855× | -3.5 | 0.044 | 19/48 (NCI-H23, LOX-IMVI, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | 0.787× | -3.2 | 0.11 | 12/48 (SNU-1, COLO 205, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.866× | -3.1 | 0.11 | 20/50 (NCI-H23, LOX-IMVI, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | 0.793× | -3.1 | 0.11 | 16/47 (SNU-1, AsPC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.871× | -3.1 | 0.11 | 22/48 (HEC-1-A, NCI-H23, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11926. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 76.6 | 13 (4 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.55× (z +41.1) | [[Dinaciclib (drug)]] 0.5 µM 0.448× (z -11.6) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 127 | 7 | 6 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.19× (z +34.9) | [[Panobinostat (drug)]] 0.5 µM 0.217× (z -23.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 88.8 | 8 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 9.80× (z +37.3) | [[Dinaciclib (drug)]] 5 µM 0.431× (z -9.4) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 78.6 | 9 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.86× (z +19.6) | [[Dinaciclib (drug)]] 0.5 µM 0.330× (z -8.7) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 194 | 2 | 8 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.201× (z -14.5) ⚠ toxic; transcription drop · without an alert: [[Budesonide (drug)]] 0.05 µM 0.369× (z -9.0) |
| [[HS-578T (line)]] | alt | 78.3 | 10 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.62× (z +28.8) | — |
| [[PANC-1 (line)]] | alt | 69.4 | 9 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.12× (z +41.6) | [[Dinaciclib (drug)]] 0.5 µM 0.423× (z -12.1) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 109 | 6 (1 ⚠) | 4 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.05× (z +11.2) | [[Dinaciclib (drug)]] 0.5 µM 0.413× (z -13.8) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 68.2 | 9 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.45× (z +14.2) | — |
| [[LoVo (line)]] | wt | 115 | 3 | 6 (5 ⚠) | [[TAK-901 (drug)]] 5 µM 4.80× (z +10.6) | [[Panobinostat (drug)]] 5 µM 0.161× (z -23.7) ⚠ cell-cycle shift, explains ~12% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 0.616× (z -8.9) |
| [[MIA PaCa-2 (line)]] | alt | 106 | 4 | 5 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.35× (z +19.9) | [[Dinaciclib (drug)]] 0.5 µM 0.257× (z -15.9) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 104 | 2 | 7 (7 ⚠) | [[TAK-901 (drug)]] 5 µM 6.75× (z +10.9) | [[Panobinostat (drug)]] 0.5 µM 0.130× (z -22.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 61.3 | 9 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.34× (z +34.6) | — |
| [[A-427 (line)]] | wt | 100 | 4 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +15.7) | [[Panobinostat (drug)]] 5 µM 0.236× (z -17.5) ⚠ cell-cycle shift, explains ~12% of this change |
| [[KATO III (line)]] | alt | 67.3 | 7 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.36× (z +19.6) | [[Dinaciclib (drug)]] 5 µM 0.179× (z -19.0) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 115 | 3 | 5 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.17× (z +21.3) | [[Dinaciclib (drug)]] 0.05 µM 0.306× (z -14.3) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 150 | 2 | 6 (5 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.89× (z +8.7) | [[Panobinostat (drug)]] 0.5 µM 0.335× (z -15.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 0.635× (z -8.9) |
| [[A-172 (line)]] | wt | 143 | 5 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.06× (z +24.2) | [[Dinaciclib (drug)]] 5 µM 0.173× (z -17.9) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 102 | 5 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 11.5× (z +39.3) | [[Dinaciclib (drug)]] 5 µM 0.406× (z -9.9) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 77.0 | 6 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.57× (z +25.9) | [[Dinaciclib (drug)]] 0.05 µM 0.349× (z -10.4) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 84.1 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.60× (z +21.0) | — |
| [[hTERT-HPNE (line)]] | wt | 73.8 | 6 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.71× (z +22.7) | [[Dinaciclib (drug)]] 5 µM 0.243× (z -10.1) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 72.2 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.07× (z +26.8) | — |
| [[NCI-H1792 (line)]] | alt | 81.8 | 6 (1 ⚠) | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 11.0× (z +26.5) | [[Dinaciclib (drug)]] 0.5 µM 0.216× (z -17.8) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 94.2 | 5 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.29× (z +20.4) | [[Dinaciclib (drug)]] 5 µM 0.294× (z -14.4) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 91.8 | 7 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 12.0× (z +24.2) | — |
| [[SNU-423 (line)]] | alt | 75.1 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.0× (z +29.9) | — |
| [[SW 900 (line)]] | alt | 59.8 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.20× (z +22.0) | — |
| [[LOX-IMVI (line)]] | wt | 143 | 1 | 5 (5 ⚠) | [[PH-797804 (drug)]] 5 µM 4.18× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.307× (z -13.7) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 107 | 4 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +19.9) | [[Dinaciclib (drug)]] 0.5 µM 0.377× (z -12.6) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 54.4 | 4 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.52× (z +23.3) | [[Dinaciclib (drug)]] 0.5 µM 0.289× (z -12.1) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 106 | 1 | 4 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.62× (z +8.6) | [[Panobinostat (drug)]] 5 µM 0.168× (z -19.4) ⚠ cell-cycle shift, explains ~12% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 0.563× (z -8.9) |
| [[SHP-77 (line)]] | alt | 62.8 | 5 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.84× (z +10.3) | — |
| [[COLO 205 (line)]] | alt | 94.3 | 4 | 0 | [[TAK-901 (drug)]] 5 µM 16.3× (z +12.6) | — |
| [[SNU-1 (line)]] | wt | 151 | 3 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 11.0× (z +12.6) | [[Dinaciclib (drug)]] 0.5 µM 0.274× (z -13.0) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 199 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 0.05 µM 3.15× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.136× (z -17.4) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 39.4 | 2 | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 5.61× (z +12.3) | [[Dinaciclib (drug)]] 0.05 µM 0.280× (z -8.8) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 108 | 3 | 0 | [[Harringtonine (drug)]] 5 µM 3.15× (z +10.3) | — |
| [[HT-29 (line)]] | alt | 174 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 11.7× (z +13.1) | [[Dinaciclib (drug)]] 0.5 µM 0.408× (z -9.2) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 114 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +13.3) | — |
| [[BT-474 (line)]] | alt | 110 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 4.76× (z +8.6) | — |
| [[Hs 766T (line)]] | wt | 28.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.31× (z +18.7) | — |
| [[C-33 A (line)]] | alt | 85.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.168× (z -17.7) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 172 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 63.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 99.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 72.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 91.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 97.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11926), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*40 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF629]] | +0.58 | +0.40 / +0.57 | both halves | 5e-05 |  |
| [[SLC25A13]] | +0.57 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[FJX1]] | +0.56 | +0.39 / +0.56 | both halves | 6e-05 |  |
| [[MRM2]] | +0.54 | +0.39 / +0.54 | both halves | 6e-05 |  |
| [[HNRNPF]] | +0.54 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[ZNRF3]] | +0.53 | +0.54 / +0.45 | both halves | 3e-05 |  |
| [[URGCP]] | +0.53 | +0.43 / +0.50 | both halves | 3e-05 |  |
| [[AMOTL2]] | +0.53 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[TGIF2]] | +0.53 | +0.43 / +0.52 | both halves | 3e-05 |  |
| [[EXOSC6]] | +0.53 | +0.45 / +0.48 | both halves | 3e-05 |  |
| [[FAM83H]] | +0.52 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[TSC22D1]] | +0.52 | +0.43 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*60 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LMAN1]] | -0.63 | -0.50 / -0.59 | both halves | 1e-05 |  |
| [[SEC23A]] | -0.63 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[COPB1]] | -0.62 | -0.54 / -0.57 | both halves | 1e-05 |  |
| [[COPA]] | -0.62 | -0.47 / -0.58 | both halves | 2e-05 |  |
| [[COG6]] | -0.59 | -0.50 / -0.57 | both halves | 1e-05 |  |
| [[SUCO]] | -0.59 | -0.49 / -0.58 | both halves | 1e-05 |  |
| [[TMEM263]] | -0.58 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[SEC22B]] | -0.57 | -0.46 / -0.56 | both halves | 3e-05 |  |
| [[SARAF]] | -0.57 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[SEC24D]] | -0.57 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[SAR1A]] | -0.57 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[COPB2]] | -0.57 | -0.54 / -0.57 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[WWC1]] | B | WWC1 activity raises TET3's level | lines that do not express WWC1 (13) vs lines expressing it (37) | 1.39× lower at baseline in the lines without WWC1 | 0.091 | ⚠ within organs, on part of the lines; also absent: SH2D3A, CHMP4C, LSR; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 056]] — Asparagine N-linked glycosylation; 87 genes; every member is in the + arm (projection on the module's main direction -0.585). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.1, -32.7); signed map (8.1, -46.3). **Vector** length 97.9, 27.3% of its response variance represented; |z| ≥ 3 in 1,373 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +6.8 | +29.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | +6.3 | +25.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.3 | +9.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.3 | +1.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.3 | +15.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.9 | +0.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.8 | +1.8 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.2 | +0.7 |
| fall | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.0 | -3.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.7 | +0.1 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.5 | +1.6 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | -2.0 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.2 | -0.8 |
|  | [[Terfenadine (drug)]] 5 µM |  | -1.8 | -0.2 |
|  | [[Trimetrexate (drug)]] 5 µM |  | -1.7 | -0.1 |
|  | [[Glycyrrhizic acid (drug)]] 0.5 µM |  | -1.6 | +0.7 |

## What is on record

|  |  |
|---|---|
| Name | tet methylcytosine dioxygenase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p13.1 — chr2:73,984,910-74,108,176 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC22014, hCG_40738 |
| Gene groups (HGNC) | Zinc fingers CXXC-type; Tet methylcytosine dioxygenase family |
| Reactome | 4 pathways, smallest: TET1,2,3 and TDG demethylate DNA; Chromatin modifications during the maternal to zygotic transition (MZT); Maternal to zygotic transition (MZT) |
| Matched by | ensembl_id |

**Function**, from UniProt [O43151](https://www.uniprot.org/uniprotkb/O43151) (Methylcytosine dioxygenase TET3):

> Dioxygenase that catalyzes the conversion of the modified genomic base 5-methylcytosine (5mC) into 5-hydroxymethylcytosine (5hmC) and plays a key role in epigenetic chromatin reprogramming in the zygote following fertilization. Also mediates subsequent conversion of 5hmC into 5-formylcytosine (5fC), and conversion of 5fC to 5-carboxylcytosine (5caC). Conversion of 5mC into 5hmC, 5fC and 5caC probably constitutes the first step in cytosine demethylation (By similarity). Selectively binds to the …

**Summary**, from NCBI Gene [200424](https://www.ncbi.nlm.nih.gov/gene/200424):

> Enables RNA polymerase II cis-regulatory region sequence-specific DNA binding activity; methyl-CpG binding activity; and zinc ion binding activity. Involved in positive regulation of transcription by RNA polymerase II and protein O-linked glycosylation. Predicted to be located in cytoplasm and male pronucleus. Predicted to be active in nucleus. Biomarker of esophagus squamous cell carcinoma. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28313](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28313) · Entrez [200424](https://www.ncbi.nlm.nih.gov/gene/200424) · UniProt [O43151](https://www.uniprot.org/uniprotkb/O43151) · Ensembl [ENSG00000187605](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000187605)

## Data

Gene col 11926: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11926); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11926, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11926]; `tensor/DDL_lfc|DDL_z.npy` [11926]; `embed/gene_vectors.npy` [11926]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11926 or target_col == 11926). Every well: [[TET3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TET3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
