---
symbol: "AKT3"
type: "gene"
col: 3869
ensembl_id: "ENSG00000117020"
name: "AKT serine/threonine kinase 3"
location: "1q43-q44"
module: 84
arm: "+"
pooled_cpm: 288.85
n_lines_expressing: 34
n_dd_up: 4
n_dd_down: 29
n_dd_up_clean: 1
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 15
direction_downstream: 23
tags: ["gene", "module/084"]
generated_by: "tahoemap"
---

# AKT3

*AKT serine/threonine kinase 3* — 1q43-q44

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 0.5 µM: 1.26× (z +4.5, q 0.005, up in 17 of 33 measured lines) ⚠ cell-cycle shift, explains ~39% of this change. The strongest without an alert is [[BAY1125976 (drug)]] 5 µM: 1.57× (z +3.9, q 0.015, up in 25 of 32 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 7 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 6 lines (PANC-1 3.94×, CFPAC-1 2.27×, A549 1.84×, SNU-423 1.72×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Tucidinostat (drug)]] 5 µM in 5 lines (PANC-1 3.44×, NCI-H2347 2.31×, MIA PaCa-2 2.10×, CFPAC-1 1.64×, …); [[Tucidinostat (drug)]] 0.5 µM in 2 lines (PANC-1 3.79×, NCI-H2347 2.94×; ⚠ cell-cycle shift, explains ~39% of this change); [[Vinblastine (sulfate) (drug)]] 5 µM in 1 line (CFPAC-1 1.63×).
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (14 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.388× (z -18.1, q 0e+00, down in 29 of 32 measured lines) ⚠ cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.518× (z -17.8, q 0e+00, down in 30 of 33 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KLF12]] (+0.64, fdr 9e-06), [[RFTN1]] (+0.59, fdr 2e-05), [[GABBR1]] (+0.58, fdr 3e-05); moves opposite to [[LPIN3]] (-0.49, fdr 9e-05), [[ZSCAN25]] (-0.46, fdr 6e-05), [[APTX]] (-0.44, fdr 5e-05).
> It is in [[Module 084]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 15 arrows point to it, the strongest [[JAZF1]] → it (grade B ⚠); 23 go from it, the strongest it → [[CEP112]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3869.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 7 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 6 lines (PANC-1 3.94×, CFPAC-1 2.27×, A549 1.84×, SNU-423 1.72×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Tucidinostat (drug)]] 5 µM in 5 lines (PANC-1 3.44×, NCI-H2347 2.31×, MIA PaCa-2 2.10×, CFPAC-1 1.64×, …); [[Tucidinostat (drug)]] 0.5 µM in 2 lines (PANC-1 3.79×, NCI-H2347 2.94×; ⚠ cell-cycle shift, explains ~39% of this change); [[Vinblastine (sulfate) (drug)]] 5 µM in 1 line (CFPAC-1 1.63×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.26×** | +4.5 | 0.005 | 17/33 (PANC-1, NCI-H2347, …) | all doses, flat |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.25×** | +4.2 | 0.008 | 19/31 (C32, H4, …) | rises with dose |  |
| [[BAY1125976 (drug)]] 5 µM |  | **1.57×** | +3.9 | 0.015 | 25/32 (PANC-1, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.22×** | +3.8 | 0.018 | 16/32 (CFPAC-1, PANC-1, …) | top dose only |  |
| [[Rapamycin (drug)]] 5 µM |  | 1.14× | +3.5 | 0.061 | 3/32 (PANC-1, CFPAC-1, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | 1.19× | +3.3 | 0.091 | 11/32 (NCI-H2347, SW480, …) | all doses, flat |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.17× | +3.0 | 0.18 | 13/31 (H4, SW480, …) | rises with dose | low cells (technical?) |
| [[Bimiralisib (drug)]] 5 µM |  | 1.42× | +3.0 | 0.18 | 15/34 (A-427, LOX-IMVI, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 17 with an alert ⚠; shown: the 15 strongest and the 12 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3869.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.388×** | -18.1 | 0e+00 | 29/32 (A549, SNU-423, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.518×** | -17.8 | 0e+00 | 30/33 (A549, J82, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.396×** | -17.7 | 0e+00 | 29/32 (A549, SNU-423, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **0.435×** | -15.9 | 0e+00 | 29/33 (RKO, CHP-212, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.437×** | -15.2 | 0e+00 | 31/31 (RKO, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **0.461×** | -14.3 | 2e-44 | 26/29 (LOX-IMVI, C-33 A, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.563×** | -11.0 | 3e-26 | 27/32 (A549, HOP62, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.584×** | -10.3 | 4e-23 | 30/32 (C-33 A, SW480, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **0.561×** | -9.9 | 3e-21 | 28/30 (A-172, LOX-IMVI, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.607×** | -9.6 | 5e-20 | 27/32 (SK-MEL-2, SNU-423, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.618×** | -8.9 | 4e-17 | 28/32 (HOP62, HS-578T, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.653×** | -8.2 | 1e-14 | 29/32 (RKO, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.642×** | -8.2 | 1e-14 | 28/34 (LOX-IMVI, HOP62, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.711×** | -6.5 | 2e-09 | 29/32 (HOP62, RPMI-7951, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~15% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.500×** | -6.0 | 7e-08 | 30/32 (SW480, RPMI-7951, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.504×** | -5.9 | 1e-07 | 28/32 (SW480, RKO, …) | top dose only | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.533×** | -5.4 | 2e-06 | 30/32 (SW480, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **0.829×** | -5.1 | 1e-05 | 16/32 (RKO, A549, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.561×** | -5.0 | 2e-05 | 26/32 (LOX-IMVI, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.608×** | -4.3 | 5e-04 | 22/32 (SW480, C32, …) | rises with dose | noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **0.622×** | -4.1 | 0.001 | 25/31 (RKO, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **0.716×** | -3.8 | 0.003 | 22/33 (SW480, CHP-212, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.720×** | -3.7 | 0.004 | 23/32 (SW480, NCI-H23, …) | rises with dose | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.873× | -3.7 | 0.005 | 14/32 (A-172, HOP62, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM |  | **0.658×** | -3.6 | 0.006 | 18/31 (NCI-H23, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.727×** | -3.6 | 0.006 | 19/32 (C-33 A, LOX-IMVI, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.829×** | -3.6 | 0.006 | 18/33 (HOP62, NCI-H2347, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.54 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3869. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 620 | 0 | 15 (13 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.340× (z -22.5) |
| [[HOP62 (line)]] | alt | 681 | 0 | 14 (11 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.299× (z -23.4) |
| [[A549 (line)]] | wt | 749 | 1 (1 ⚠) | 12 (11 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +13.8) ⚠ cell-cycle shift, explains ~0% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.217× (z -34.5) |
| [[J82 (line)]] | alt | 697 | 0 | 13 (12 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.320× (z -24.8) |
| [[A-172 (line)]] | wt | 852 | 0 | 12 (9 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.296× (z -23.2) |
| [[SNU-423 (line)]] | alt | 699 | 1 (1 ⚠) | 11 (9 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.72× (z +10.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 0.5 µM 0.240× (z -19.7) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.378× (z -19.0) |
| [[C-33 A (line)]] | alt | 437 | 0 | 11 (9 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.251× (z -18.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.553× (z -11.6) |
| [[HS-578T (line)]] | alt | 441 | 0 | 11 (9 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.298× (z -24.2) |
| [[NCI-H460 (line)]] | wt | 440 | 3 (3 ⚠) | 8 (7 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +10.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.316× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.530× (z -12.1) |
| [[SK-MEL-2 (line)]] | alt | 704 | 1 (1 ⚠) | 10 (8 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.60× (z +10.3) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.293× (z -18.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.388× (z -14.6) |
| [[C32 (line)]] | wt | 345 | 5 (5 ⚠) | 5 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 10.7× (z +14.3) ⚠ cell-cycle shift, explains ~0% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.425× (z -11.0) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.582× (z -10.2) |
| [[CFPAC-1 (line)]] | alt | 256 | 7 (5 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +16.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 1.64× (z +9.9) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.432× (z -11.5) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.645× (z -8.8) |
| [[CHP-212 (line)]] | wt | 678 | 0 | 10 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.256× (z -20.0) |
| [[NCI-H23 (line)]] | alt | 402 | 0 | 10 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.280× (z -16.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.436× (z -10.8) |
| [[RKO (line)]] | wt | 277 | 0 | 10 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.257× (z -18.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.444× (z -11.1) |
| [[PANC-1 (line)]] | alt | 75.4 | 9 (8 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.94× (z +22.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 3.44× (z +20.1) | — |
| [[SW480 (line)]] | alt | 150 | 2 (1 ⚠) | 7 (7 ⚠) | [[Tucidinostat (drug)]] 0.5 µM 1.87× (z +10.3) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 1.52× (z +9.8) | [[Panobinostat (drug)]] 5 µM 0.368× (z -16.6) ⚠ cell-cycle shift, explains ~37% of this change |
| [[A498 (line)]] | wt | 484 | 1 (1 ⚠) | 7 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.69× (z +9.7) ⚠ cell-cycle shift, explains ~0% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.492× (z -13.0) |
| [[hTERT-HPNE (line)]] | wt | 568 | 0 | 8 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.345× (z -16.7) |
| [[Panc 03.27 (line)]] | alt | 561 | 0 | 8 (7 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.314× (z -15.5) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.574× (z -10.9) |
| [[A-427 (line)]] | wt | 583 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.337× (z -16.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.565× (z -9.2) |
| [[RPMI-7951 (line)]] | alt | 485 | 1 (1 ⚠) | 6 (5 ⚠) | [[Harringtonine (drug)]] 5 µM 2.13× (z +9.9) ⚠ cell-cycle shift, explains ~0% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.511× (z -12.9) |
| [[SHP-77 (line)]] | alt | 372 | 0 | 6 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.340× (z -14.9) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.620× (z -9.4) |
| [[H4 (line)]] | wt | 387 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.478× (z -12.1) |
| [[SW 1271 (line)]] | alt | 492 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.344× (z -11.7) |
| [[SW 900 (line)]] | alt | 234 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.547× (z -10.8) |
| [[MIA PaCa-2 (line)]] | alt | 127 | 1 | 2 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.10× (z +10.0) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.334× (z -10.2) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 258 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.469× (z -13.1) |
| [[NCI-H2347 (line)]] | alt | 80.9 | 2 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 2.31× (z +12.9) | — |
| [[AN3 CA (line)]] | alt | 44.4 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 22.6 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 39.0 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 21.5 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 20.6 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 28.0 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 33.4 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 27.4 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 19.6 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 39.9 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 18.9 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 25.8 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 52.6 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 208 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 295 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 247 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 24.3 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 336 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 20.1 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 65.3 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3869), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLF12]] | +0.64 | +0.57 / +0.64 | both halves | 9e-06 |  |
| [[RFTN1]] | +0.59 | +0.48 / +0.64 | both halves | 2e-05 |  |
| [[GABBR1]] | +0.58 | +0.44 / +0.65 | both halves | 3e-05 |  |
| [[RASSF8]] | +0.55 | +0.45 / +0.57 | both halves | 3e-05 |  |
| [[JAZF1]] | +0.53 | +0.44 / +0.55 | both halves | 3e-05 |  |
| [[MPDZ]] | +0.51 | +0.46 / +0.51 | both halves | 3e-05 |  |
| [[USP12]] | +0.51 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[TBC1D9]] | +0.51 | +0.43 / +0.49 | both halves | 3e-05 |  |
| [[ZDHHC2]] | +0.51 | +0.51 / +0.46 | both halves | 2e-05 | pathway: SARS-CoV-2 Infection |
| [[SPOCK1]] | +0.49 | +0.46 / +0.48 | both halves | 3e-05 |  |
| [[PRXL2C]] | +0.49 | +0.49 / +0.41 | both halves | 4e-05 |  |
| [[MIF4GD]] | +0.48 | +0.32 / +0.46 | both halves | 2e-04 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LPIN3]] | -0.49 | -0.37 / -0.46 | both halves | 9e-05 |  |
| [[ZSCAN25]] | -0.46 | -0.38 / -0.44 | both halves | 6e-05 |  |
| [[APTX]] | -0.44 | -0.39 / -0.44 | both halves | 5e-05 |  |
| [[LMAN2]] | -0.43 | -0.40 / -0.33 | both halves | 1e-04 |  |
| [[PICK1]] | -0.43 | -0.30 / -0.46 | both halves | 2e-04 |  |
| [[TMPRSS5]] | -0.43 | -0.44 / -0.38 | both halves | 7e-05 |  |
| [[ALG5]] | -0.42 | -0.30 / -0.46 | both halves | 2e-04 |  |
| [[ADPGK]] | -0.41 | -0.28 / -0.38 | both halves | 3e-04 |  |
| [[PIGB]] | -0.40 | -0.31 / -0.45 | both halves | 2e-04 |  |
| [[GPR89A]] | -0.40 | -0.30 / -0.46 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 8, C 7. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[JAZF1]] | B | JAZF1 activity raises AKT3's level | lines that do not express JAZF1 (9) vs lines expressing it (41) | 8.09× lower at baseline in the lines without JAZF1 | 0.007 | ⚠ within organs, on part of the lines; also absent: FGD1, CERCAM, MPP2; maybe low, not absent |
| [[CRMP1]] | B | CRMP1 activity raises AKT3's level | lines that do not express CRMP1 (19) vs lines expressing it (31) | 3.71× lower at baseline in the lines without CRMP1 | 0.027 | ⚠ within organs, on part of the lines; also absent: JAM3, NHSL2, ENSG00000286033; maybe low, not absent |
| [[ANKRD44]] | B | ANKRD44 activity raises AKT3's level | lines that do not express ANKRD44 (6) vs lines expressing it (44) | 8.26× lower at baseline in the lines without ANKRD44 | 0.053 | ⚠ within organs, on part of the lines; also absent: ENSG00000236230, TBC1D19, SSBP2; maybe low, not absent |
| [[DSE]] | B | DSE activity raises AKT3's level | lines that do not express DSE (9) vs lines expressing it (41) | 6.36× lower at baseline in the lines without DSE | 0.062 | ⚠ within organs, on part of the lines; also absent: SGCE, WDR17, LRP12; maybe low, not absent |
| [[EBF4]] | B | EBF4 activity raises AKT3's level | lines that do not express EBF4 (12) vs lines expressing it (38) | 4.91× lower at baseline in the lines without EBF4 | 0.069 | ⚠ within organs, on part of the lines; also absent: CERCAM, FGD1, DCLK2 |
| [[MME]] | B | MME activity raises AKT3's level | lines that do not express MME (30) vs lines expressing it (20) | 4.34× lower at baseline in the lines without MME | 0.079 | ⚠ within organs, on part of the lines; also absent: APCDD1L, PHACTR1, GYPC |
| [[CDH13]] | B | CDH13 activity raises AKT3's level | lines that do not express CDH13 (35) vs lines expressing it (15) | 4.21× lower at baseline in the lines without CDH13 | 0.091 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MMP2, APCDD1L, ENSG00000222032 |
| [[GABBR1]] | B | GABBR1 activity raises AKT3's level | lines that do not express GABBR1 (7) vs lines expressing it (43) | 9.14× lower at baseline in the lines without GABBR1 | 0.098 | ⚠ within organs, on part of the lines; also absent: BLVRA, TUBA1A, CABYR |
| [[MIR137HG]] | C | MIR137HG activity raises AKT3's level | lines that do not express MIR137HG (28) vs lines expressing it (22) | 5.34× lower at baseline in the lines without MIR137HG | 0.002 | ⚠ within organs, on part of the lines; also absent: EDNRA, CCBE1, ARMCX2; co-absent with the target |
| [[ZEB2]] | C | ZEB2 activity raises AKT3's level | lines that do not express ZEB2 (27) vs lines expressing it (23) | 6.94× lower at baseline in the lines without ZEB2 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ADAM12, LINC01583, PRR16; co-absent with the target |
| [[MPDZ]] | C | MPDZ activity raises AKT3's level | lines that do not express MPDZ (17) vs lines expressing it (33) | 7.94× lower at baseline in the lines without MPDZ | 0.018 | ⚠ within organs, on part of the lines; also absent: GNB4, BVES, BVES-AS1; co-absent with the target |
| [[BNC2]] | C | BNC2 activity raises AKT3's level | lines that do not express BNC2 (21) vs lines expressing it (29) | 6.39× lower at baseline in the lines without BNC2 | 0.024 | ⚠ within organs, on part of the lines; also absent: LINC03041, DPY19L2, RNF182; co-absent with the target |

### Downstream of this gene

*23 arrows, 23 of them with an alert ⚠; grade A 0, B 18, C 5. Shown: the 12 strongest; 11 more arrows (11 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CEP112]] | B | AKT3 activity raises CEP112's level | lines that do not express AKT3 (16) vs lines expressing it (34) | 2.27× lower at baseline in the lines without AKT3 | 0.002 | ⚠ within organs, on part of the lines; also absent: ENSG00000234405, GNB4, LINC03041 |
| [[PIK3CD]] | B | AKT3 activity raises PIK3CD's level | lines that do not express AKT3 (16) vs lines expressing it (34) | 2.31× lower at baseline in the lines without AKT3 | 0.023 | ⚠ within organs, on part of the lines; also absent: ENSG00000234405, GNB4, LINC03041 |
| [[FMNL3]] | B | AKT3 activity raises FMNL3's level | lines that do not express AKT3 (16) vs lines expressing it (34) | 3.09× lower at baseline in the lines without AKT3 | 0.033 | ⚠ within organs, on part of the lines; also absent: ENSG00000234405, GNB4, LINC03041 |
| [[JAZF1]] | B | AKT3 activity raises JAZF1's level | lines that do not express AKT3 (16) vs lines expressing it (34) | 2.38× lower at baseline in the lines without AKT3 | 0.039 | ⚠ within organs, on part of the lines; also absent: ENSG00000234405, GNB4, LINC03041 |
| [[CRMP1]] | B | AKT3 activity raises CRMP1's level | lines that do not express AKT3 (16) vs lines expressing it (34) | 2.50× lower at baseline in the lines without AKT3 | 0.039 | ⚠ within organs, on part of the lines; also absent: ENSG00000234405, GNB4, LINC03041 |
| [[MMGT1]] | B | [[AKT1]], [[AKT2]], AKT3 activity raises MMGT1's level | compounds that target AKT1, AKT2, AKT3: 2 of 3 lower it (BAY1125976, Ipatasertib) | 67% of the class's compounds vs 0.6% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; shared targets |
| [[ABI2]] | B | AKT3 activity raises ABI2's level | lines that do not express AKT3 (16) vs lines expressing it (34) | 1.58× lower at baseline in the lines without AKT3 | 0.053 | ⚠ within organs, on part of the lines; also absent: ENSG00000234405, GNB4, LINC03041 |
| cells under [[APTO-253 (drug)]] 5 µM | B | AKT3 activity raises the cells' numbers under APTO-253 5 µM (protects the cells) | lines that do not express AKT3 (16) vs lines expressing it (32) | the lines without AKT3: 0.86× the cells of the other lines | 0.066 | ⚠ within organs, on part of the lines; also absent: ENSG00000234405, GNB4, LINC03041 |
| cells under [[CP21R7 (drug)]] 0.5 µM | B | AKT3 activity raises the cells' numbers under CP21R7 0.5 µM (protects the cells) | lines that do not express AKT3 (16) vs lines expressing it (32) | the lines without AKT3: 0.87× the cells of the other lines | 0.066 | ⚠ within organs, on part of the lines; also absent: ENSG00000234405, GNB4, LINC03041 |
| [[NOTCH2]] | B | AKT3 activity raises NOTCH2's level | lines that do not express AKT3 (16) vs lines expressing it (34) | 2.01× lower at baseline in the lines without AKT3 | 0.067 | ⚠ within organs, on part of the lines; also absent: ENSG00000234405, GNB4, LINC03041 |
| [[PPP2R3A]] | B | AKT3 activity raises PPP2R3A's level | lines that do not express AKT3 (16) vs lines expressing it (34) | 2.27× lower at baseline in the lines without AKT3 | 0.068 | ⚠ within organs, on part of the lines; also absent: ENSG00000234405, GNB4, LINC03041 |
| [[GTF3C4]] | B | [[AKT1]], [[AKT2]], AKT3 activity raises GTF3C4's level | compounds that target AKT1, AKT2, AKT3: 2 of 3 lower it (BAY1125976, Ipatasertib) | 67% of the class's compounds vs 0.8% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; shared targets |

## Where it sits

- **Module**: [[Module 084]]; 52 genes; every member is in the + arm (projection on the module's main direction 0.324). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (48.1, 14.7); signed map (19.3, 44.7). **Vector** length 117, 39.3% of its response variance represented; |z| ≥ 3 in 1,156 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.5 | +2.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +7.9 | +4.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | +6.8 | -15.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +6.5 | +2.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +6.2 | +2.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.1 | -0.3 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.9 | +3.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.8 | +3.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.6 | +2.2 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.1 | -10.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.2 | -5.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.9 | -6.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -3.7 | -15.2 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -3.5 | -3.7 |
|  | [[EX229 (drug)]] 5 µM |  | -3.3 | -4.3 |
|  | [[venetoclax (drug)]] 5 µM |  | -3.2 | -5.4 |

## What is on record

|  |  |
|---|---|
| Name | AKT serine/threonine kinase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q43-q44 — chr1:243,488,233-243,851,079 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PKBG, RAC-gamma, PRKBG |
| Gene groups (HGNC) | Pleckstrin homology domain containing; AKT kinase family |
| Hallmark sets | PANCREAS_BETA_CELLS, UV_RESPONSE_DN, APICAL_JUNCTION |
| Reactome | 75 pathways, smallest: AKT-mediated inactivation of FOXO1A; Inhibition of TSC complex formation by AKT (PKB); RUNX2 regulates genes involved in cell migration |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y243](https://www.uniprot.org/uniprotkb/Q9Y243) (RAC-gamma serine/threonine-protein kinase):

> AKT3 is one of 3 closely related serine/threonine-protein kinases (AKT1, AKT2 and AKT3) called the AKT kinase, and which regulate many processes including metabolism, proliferation, cell survival, growth and angiogenesis. This is mediated through serine and/or threonine phosphorylation of a range of downstream substrates. Over 100 substrate candidates have been reported so far, but for most of them, no isoform specificity has been reported. AKT3 is the least studied AKT isoform. It plays an …

**Summary**, from NCBI Gene [10000](https://www.ncbi.nlm.nih.gov/gene/10000):

> The protein encoded by this gene is a member of the AKT, also called PKB, serine/threonine protein kinase family. AKT kinases are known to be regulators of cell signaling in response to insulin and growth factors. They are involved in a wide variety of biological processes including cell proliferation, differentiation, apoptosis, tumorigenesis, as well as glycogen synthesis and glucose uptake. This kinase has been shown to be stimulated by platelet-derived growth factor (PDGF), insulin, and …

**Accessions** — [HGNC:393](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:393) · Entrez [10000](https://www.ncbi.nlm.nih.gov/gene/10000) · UniProt [Q9Y243](https://www.uniprot.org/uniprotkb/Q9Y243) · Ensembl [ENSG00000117020](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000117020)

## Data

Gene col 3869: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3869); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3869, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3869]; `tensor/DDL_lfc|DDL_z.npy` [3869]; `embed/gene_vectors.npy` [3869]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3869 or target_col == 3869). Every well: [[AKT3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AKT3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
