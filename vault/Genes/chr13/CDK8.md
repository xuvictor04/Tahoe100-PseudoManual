---
symbol: "CDK8"
type: "gene"
col: 5398
ensembl_id: "ENSG00000132964"
name: "cyclin dependent kinase 8"
location: "13q12.13"
module: 186
arm: "+"
pooled_cpm: 120.92
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 5
n_dd_up_clean: 12
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/186"]
generated_by: "tahoemap"
---

# CDK8

*cyclin dependent kinase 8* — 13q12.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.73× (z +15.6, q 0e+00, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.477× (z -14.3, q 8e-44, down in 40 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.708× (z -7.0, q 4e-10, down in 33 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (A-427 0.0863×, C32 0.0865×, SHP-77 0.183×, NCI-H23 0.255×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (C32 0.164×, HEC-1-A 0.227×, SW48 0.193×, LS 180 0.309×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (A-427 0.0897×, A549 0.207×, C32 0.191×; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 1 line (SW480 0.349×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PPP2R5E]] (+0.56, fdr 1e-05), [[PREP]] (+0.52, fdr 3e-05), [[TBC1D12]] (+0.52, fdr 2e-05); moves opposite to [[SRSF6]] (-0.52, fdr 3e-05), [[PRPF38A]] (-0.48, fdr 7e-05), [[PMF1]] (-0.46, fdr 6e-05).
> It is in [[Module 186]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5398.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.73×** | +15.6 | 0e+00 | 39/48 (RKO, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **3.02×** | +11.6 | 1e-28 | 46/49 (PANC-1, RKO, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **1.63×** | +9.9 | 1e-20 | 44/48 (COLO 205, A498, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.60×** | +9.5 | 4e-19 | 39/48 (COLO 205, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.55×** | +8.5 | 2e-15 | 38/48 (RKO, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.12×** | +7.9 | 3e-13 | 36/48 (C32, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.28×** | +7.1 | 1e-10 | 31/49 (CFPAC-1, COLO 205, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.38×** | +6.5 | 5e-09 | 35/48 (COLO 205, A498, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.72×** | +5.7 | 6e-07 | 37/49 (COLO 205, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.35×** | +5.7 | 7e-07 | 30/48 (SNU-423, HT-29, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.32×** | +5.6 | 1e-06 | 31/48 (PANC-1, H4, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.30×** | +5.3 | 5e-06 | 33/48 (COLO 205, KATO III, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.29×** | +5.1 | 1e-05 | 29/48 (Hs 766T, PANC-1, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.30×** | +5.1 | 2e-05 | 28/47 (LoVo, A498, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.28×** | +5.0 | 2e-05 | 30/48 (COLO 205, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Tomivosertib (drug)]] 5 µM |  | **1.37×** | +3.3 | 0.025 | 17/48 (HepG2/C3A, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Irinotecan (hydrochloride) (drug)]] 0.5 µM |  | 1.18× | +3.3 | 0.031 | 10/48 (A549, PANC-1, …) | inconsistent across doses | position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | 1.18× | +3.2 | 0.035 | 19/49 (SHP-77, A-427, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.11× | +3.0 | 0.061 | 9/48 (A498, RPMI-7951, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 5 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5398.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (A-427 0.0863×, C32 0.0865×, SHP-77 0.183×, NCI-H23 0.255×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (C32 0.164×, HEC-1-A 0.227×, SW48 0.193×, LS 180 0.309×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (A-427 0.0897×, A549 0.207×, C32 0.191×; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 1 line (SW480 0.349×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.477×** | -14.3 | 8e-44 | 40/44 (A-427, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.510×** | -13.6 | 2e-39 | 41/49 (C32, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.527×** | -11.9 | 2e-30 | 40/45 (A-427, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.708×** | -7.0 | 4e-10 | 33/48 (SW480, SK-MEL-2, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.737×** | -6.2 | 9e-08 | 34/48 (HepG2/C3A, Panc 03.27, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~8% here) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.887× | -3.4 | 0.059 | 6/48 (SK-MEL-2, H4, …) | top dose only |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | 0.766× | -3.2 | 0.13 | 20/48 (SHP-77, HCT15, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5398. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 87.1 | 8 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.40× (z +16.4) | [[Dinaciclib (drug)]] 5 µM 0.376× (z -12.7) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 134 | 4 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +20.0) | [[Dinaciclib (drug)]] 0.5 µM 0.227× (z -19.0) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 36.5 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.10× (z +19.2) | — |
| [[COLO 205 (line)]] | alt | 134 | 6 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.83× (z +13.6) | — |
| [[HT-29 (line)]] | alt | 270 | 2 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +16.3) | [[Dinaciclib (drug)]] 0.5 µM 0.333× (z -13.3) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 175 | 3 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +15.0) | [[Dinaciclib (drug)]] 5 µM 0.317× (z -13.1) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 167 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +13.5) | [[Dinaciclib (drug)]] 5 µM 0.319× (z -14.3) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 145 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +10.6) | [[Dinaciclib (drug)]] 0.5 µM 0.309× (z -14.7) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 62.9 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.04× (z +24.7) | [[Dinaciclib (drug)]] 5 µM 0.473× (z -8.9) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 152 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.87× (z +26.3) | [[Dinaciclib (drug)]] 0.5 µM 0.441× (z -9.6) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 44.7 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.40× (z +11.9) | — |
| [[A549 (line)]] | wt | 99.9 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +12.2) | [[Dinaciclib (drug)]] 0.05 µM 0.207× (z -18.6) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 205 | 1 | 3 (3 ⚠) | [[PH-797804 (drug)]] 5 µM 6.68× (z +11.0) | [[Dinaciclib (drug)]] 5 µM 0.0865× (z -26.2) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 136 | 3 (1 ⚠) | 1 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 1.98× (z +9.7) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 5 µM 1.88× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.466× (z -10.9) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 106 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +11.6) | — |
| [[SW480 (line)]] | alt | 283 | 0 | 4 (3 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.349× (z -14.1) |
| [[A-427 (line)]] | wt | 97.1 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0863× (z -26.5) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 138 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.243× (z -12.1) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 82.8 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.20× (z +14.5) | [[Dinaciclib (drug)]] 5 µM 0.296× (z -10.4) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 123 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +17.0) | [[Dinaciclib (drug)]] 0.5 µM 0.389× (z -12.8) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 165 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.144× (z -14.0) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 167 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.380× (z -12.0) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 176 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.308× (z -12.2) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 52.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +9.4) | — |
| [[Hs 766T (line)]] | wt | 134 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.397× (z -10.5) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 106 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +10.5) | — |
| [[LOX-IMVI (line)]] | wt | 125 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.09× (z +8.7) | [[Dinaciclib (drug)]] 0.5 µM 0.380× (z -12.2) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 86.4 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.17× (z +10.6) | [[Dinaciclib (drug)]] 0.05 µM 0.316× (z -11.9) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 111 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.362× (z -13.4) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 208 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.183× (z -18.3) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 92.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.327× (z -11.3) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 108 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +13.8) | — |
| [[SW48 (line)]] | wt | 152 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 0.05 µM 4.08× (z +12.5) | [[Dinaciclib (drug)]] 0.5 µM 0.193× (z -15.4) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 102 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.352× (z -10.1) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 141 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.418× (z -9.4) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 76.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.68× (z +8.5) | — |
| [[HS-578T (line)]] | alt | 79.0 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0707× (z -14.1) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 54.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +8.6) | — |
| [[NCI-H2030 (line)]] | alt | 54.4 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.281× (z -13.5) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 138 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.255× (z -16.4) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 73.1 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 2.87× (z +9.2) | — |
| [[SNU-423 (line)]] | alt | 69.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +8.7) | — |
| [[BT-474 (line)]] | alt | 69.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 140 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 141 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 142 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 133 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 57.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 148 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5398), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP2R5E]] | +0.56 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[PREP]] | +0.52 | +0.48 / +0.46 | both halves | 3e-05 |  |
| [[TBC1D12]] | +0.52 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[PDE7A]] | +0.51 | +0.42 / +0.51 | both halves | 4e-05 |  |
| [[ZMYM2]] | +0.51 | +0.43 / +0.48 | both halves | 3e-05 |  |
| [[MAP2K4]] | +0.50 | +0.39 / +0.61 | both halves | 6e-05 |  |
| [[MFSD3]] | +0.50 | +0.39 / +0.35 | both halves | 1e-04 |  |
| [[SEC24B]] | +0.50 | +0.35 / +0.51 | both halves | 1e-04 |  |
| [[USP28]] | +0.49 | +0.42 / +0.45 | both halves | 4e-05 |  |
| [[AKIP1]] | +0.49 | +0.49 / +0.38 | both halves | 7e-05 |  |
| [[BMPR1A]] | +0.48 | +0.39 / +0.54 | both halves | 5e-05 | pathway: Signaling by TGFB family members |
| [[HERC1]] | +0.48 | +0.47 / +0.53 | both halves | 2e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRSF6]] | -0.52 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[PRPF38A]] | -0.48 | -0.38 / -0.49 | both halves | 7e-05 |  |
| [[PMF1]] | -0.46 | -0.42 / -0.39 | both halves | 6e-05 |  |
| [[RABL3]] | -0.44 | -0.37 / -0.43 | both halves | 8e-05 |  |
| [[PNKP]] | -0.44 | -0.41 / -0.39 | both halves | 5e-05 |  |
| [[SRSF5]] | -0.44 | -0.41 / -0.44 | both halves | 4e-05 |  |
| [[ZNF417]] | -0.44 | -0.31 / -0.55 | both halves | 2e-04 |  |
| [[LINC01422]] | -0.43 | -0.38 / -0.41 | both halves | 6e-05 |  |
| [[TOR1AIP1]] | -0.43 | -0.38 / -0.35 | both halves | 1e-04 |  |
| [[COL7A1]] | -0.42 | -0.30 / -0.37 | both halves | 2e-04 |  |
| [[LINC00641]] | -0.42 | -0.33 / -0.29 | both halves | 3e-04 |  |
| [[SMU1]] | -0.42 | -0.30 / -0.39 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 186]]; 20 genes; every member is in the + arm (projection on the module's main direction 0.556). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.39; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-2.5, -21.1); signed map (-45.3, 26.2). **Vector** length 90.4, 26.3% of its response variance represented; |z| ≥ 3 in 1,183 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM |  | +4.6 | +5.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.5 | +11.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.1 | +1.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.8 | +7.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +2.7 | +3.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.5 | +3.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.1 | +5.7 |
|  | [[Belinostat (drug)]] 0.05 µM |  | +2.0 | +1.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.0 | +3.0 |
| fall | [[Auranofin (drug)]] 5 µM |  | -8.2 | -7.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.1 | -11.9 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.5 | +1.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.9 | +5.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.7 | +2.3 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -3.0 | -0.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.1 | -3.0 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.7 | +0.1 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -1.5 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | cyclin dependent kinase 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q12.13 — chr13:26,254,104-26,420,982 (+) |
| Ensembl biotype | protein_coding |
| Also known as | K35 |
| Gene groups (HGNC) | Cyclin dependent kinases; Mediator complex |
| Hallmark sets | APICAL_JUNCTION |
| Reactome | 26 pathways, smallest: SMAD2/SMAD3:SMAD4 heterotrimer regulates transcription; NOTCH1 Intracellular Domain Regulates Transcription; Transcriptional activity of SMAD2/SMAD3:SMAD4 heterotrimer |
| Matched by | ensembl_id |

**Function**, from UniProt [P49336](https://www.uniprot.org/uniprotkb/P49336) (Cyclin-dependent kinase 8):

> Component of the Mediator complex, a coactivator involved in regulated gene transcription of nearly all RNA polymerase II-dependent genes. Mediator functions as a bridge to convey information from gene-specific regulatory proteins to the basal RNA polymerase II transcription machinery. Mediator is recruited to promoters by direct interactions with regulatory proteins and serves as a scaffold for the assembly of a functional pre-initiation complex with RNA polymerase II and the general …

**Summary**, from NCBI Gene [1024](https://www.ncbi.nlm.nih.gov/gene/1024):

> This gene encodes a member of the cyclin-dependent protein kinase (CDK) family. CDK family members are known to be important regulators of cell cycle progression. This kinase and its regulatory subunit, cyclin C, are components of the Mediator transcriptional regulatory complex, involved in both transcriptional activation and repression by phosphorylation of the carboxy-terminal domain of the largest subunit of RNA polymerase II. This kinase regulates transcription by targeting the …

**Accessions** — [HGNC:1779](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1779) · Entrez [1024](https://www.ncbi.nlm.nih.gov/gene/1024) · UniProt [P49336](https://www.uniprot.org/uniprotkb/P49336) · Ensembl [ENSG00000132964](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132964)

## Data

Gene col 5398: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5398); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5398, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5398]; `tensor/DDL_lfc|DDL_z.npy` [5398]; `embed/gene_vectors.npy` [5398]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5398 or target_col == 5398). Every well: [[CDK8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDK8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
