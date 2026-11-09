---
symbol: "ECT2"
type: "gene"
col: 3541
ensembl_id: "ENSG00000114346"
name: "epithelial cell transforming 2"
location: "3q26.31"
module: 22
arm: "+"
pooled_cpm: 224.29
n_lines_expressing: 49
n_dd_up: 11
n_dd_down: 25
n_dd_up_clean: 1
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# ECT2

*epithelial cell transforming 2* — 3q26.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (10 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.41× (z +10.8, q 2e-24, up in 46 of 47 measured lines) ⚠ cell-cycle shift, explains ~36% of this change. The strongest without an alert is [[PH-797804 (drug)]] 5 µM: 1.67× (z +3.3, q 0.053, up in 25 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 6 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 9 lines (PANC-1 4.23×, RKO 5.04×, HS-578T 3.92×, SNU-423 3.22×, …; ⚠ cell-cycle shift, would explain all of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (PANC-1 6.12×, NCI-H460 3.57×; ⚠ cell-cycle shift, explains ~36% of this change); [[Harringtonine (drug)]] 5 µM in 1 line (PANC-1 4.23×; ⚠ cell-cycle shift, explains ~51% of this change).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (9 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.492× (z -8.7, q 1e-15, down in 46 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ANLN]] (+0.83, fdr 7e-06), [[MAD2L1]] (+0.83, fdr 7e-06), [[KIF11]] (+0.83, fdr 7e-06).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[E2F8]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 10 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3541.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 6 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 9 lines (PANC-1 4.23×, RKO 5.04×, HS-578T 3.92×, SNU-423 3.22×, …; ⚠ cell-cycle shift, would explain all of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (PANC-1 6.12×, NCI-H460 3.57×; ⚠ cell-cycle shift, explains ~36% of this change); [[Harringtonine (drug)]] 5 µM in 1 line (PANC-1 4.23×; ⚠ cell-cycle shift, explains ~51% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **2.41×** | +10.8 | 2e-24 | 46/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **2.06×** | +8.5 | 5e-15 | 42/47 (PANC-1, RKO, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.92×** | +8.0 | 3e-13 | 41/47 (PANC-1, LoVo, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **1.84×** | +7.5 | 1e-11 | 40/47 (PANC-1, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.75×** | +6.8 | 9e-10 | 42/47 (PANC-1, KATO III, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~37% of this change | **1.69×** | +6.2 | 5e-08 | 39/46 (LoVo, NCI-H23, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.65×** | +6.1 | 7e-08 | 36/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.42×** | +6.1 | 7e-08 | 29/47 (PANC-1, RKO, …) | top dose only | composition shift |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.62×** | +5.9 | 2e-07 | 33/46 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.91×** | +4.2 | 0.002 | 27/48 (PANC-1, J82, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.67×** | +3.3 | 0.053 | 25/47 (HEC-1-A, SW 900, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 9 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3541.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.492×** | -8.7 | 1e-15 | 46/47 (HEC-1-A, SW480, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.665×** | -7.1 | 3e-10 | 34/48 (A549, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.571×** | -6.5 | 1e-08 | 37/47 (SW48, SW480, …) | all doses, flat |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **0.635×** | -5.6 | 3e-06 | 36/47 (H4, A-427, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~95% of this change | **0.735×** | -5.4 | 9e-06 | 33/47 (A498, A-427, …) | rises with dose | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.686×** | -4.5 | 7e-04 | 30/46 (NCI-H2030, SNU-1, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~43% of this change | **0.537×** | -4.0 | 0.005 | 32/44 (SW48, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Amsacrine (drug)]] 5 µM |  | **0.810×** | -3.7 | 0.015 | 25/47 (SW48, LOX-IMVI, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.659×** | -3.7 | 0.015 | 31/47 (HEC-1-A, SHP-77, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.749×** | -3.6 | 0.020 | 26/47 (SW48, SW480, …) | rises with dose |  |
| [[Rapamycin (drug)]] 5 µM |  | **0.819×** | -3.5 | 0.022 | 26/47 (SNU-1, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.754×** | -3.5 | 0.022 | 24/47 (NCI-H2030, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Entrectinib (drug)]] 5 µM |  | **0.758×** | -3.4 | 0.025 | 31/47 (KATO III, RKO, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.759×** | -3.4 | 0.025 | 30/48 (A-427, NCI-H2030, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.760×** | -3.4 | 0.025 | 26/47 (NCI-H2030, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.795×** | -3.3 | 0.039 | 21/47 (NCI-H1573, SW480, …) | two highest doses | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.698×** | -3.2 | 0.050 | 25/47 (SW 900, NCI-H1573, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.777×** | -3.1 | 0.056 | 24/47 (LOX-IMVI, SNU-1, …) | inconsistent across doses |  |
| [[Bestatin (hydrochloride) (drug)]] 0.05 µM |  | **0.786×** | -3.0 | 0.085 | 21/47 (LOX-IMVI, SNU-1, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 0.5 µM |  | **0.790×** | -2.9 | 0.097 | 21/47 (RPMI-7951, HOP62, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.720×** | -2.9 | 0.097 | 26/47 (LoVo, NCI-H1573, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, +0.60 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3541. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 215 | 8 (8 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.23× (z +21.6) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SW48 (line)]] | wt | 385 | 1 (1 ⚠) | 7 (5 ⚠) | [[Harringtonine (drug)]] 5 µM 3.04× (z +9.2) ⚠ cell-cycle shift, explains ~51% of this change | [[Bortezomib (drug)]] 0.05 µM 0.219× (z -12.4) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.246× (z -12.1) |
| [[NCI-H460 (line)]] | wt | 178 | 5 (5 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.57× (z +11.1) ⚠ cell-cycle shift, explains ~36% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.313× (z -14.3) |
| [[SW480 (line)]] | alt | 324 | 0 | 6 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.373× (z -15.1) |
| [[LoVo (line)]] | wt | 198 | 3 (3 ⚠) | 2 (1 ⚠) | [[Digitoxin (drug)]] 0.5 µM 2.90× (z +10.5) ⚠ cell-cycle shift, explains ~33% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.432× (z -11.7) |
| [[NCI-H2030 (line)]] | alt | 319 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.315× (z -10.9) |
| [[A498 (line)]] | wt | 208 | 2 (2 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +11.2) ⚠ cell-cycle shift, would explain all of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.383× (z -12.6) |
| [[H4 (line)]] | wt | 152 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.259× (z -11.9) |
| [[hTERT-HPNE (line)]] | wt | 88.6 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +11.5) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H23 (line)]] | alt | 82.9 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.15× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | — |
| [[A-172 (line)]] | wt | 134 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +10.5) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.504× (z -8.8) ⚠ cell-cycle shift, explains ~95% of this change |
| [[A549 (line)]] | wt | 380 | 1 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +11.1) ⚠ cell-cycle shift, would explain all of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.251× (z -16.1) |
| [[HEC-1-A (line)]] | alt | 459 | 0 | 3 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.265× (z -14.0) |
| [[KATO III (line)]] | alt | 323 | 3 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.59× (z +10.9) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[NCI-H1792 (line)]] | alt | 81.6 | 3 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.95× (z +10.3) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[A-427 (line)]] | wt | 446 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.455× (z -10.9) ⚠ cell-cycle shift, explains ~95% of this change |
| [[C32 (line)]] | wt | 94.5 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +9.4) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.436× (z -8.5) ⚠ cell-cycle shift, explains ~95% of this change |
| [[COLO 205 (line)]] | alt | 120 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.278× (z -10.8) ⚠ cell-cycle shift, would explain all of this change |
| [[HS-578T (line)]] | alt | 153 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.92× (z +14.6) ⚠ cell-cycle shift, would explain all of this change | — |
| [[J82 (line)]] | alt | 277 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +11.7) ⚠ cell-cycle shift, would explain all of this change | — |
| [[LS 180 (line)]] | wt | 254 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.254× (z -15.2) |
| [[Panc 03.27 (line)]] | alt | 349 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +8.8) ⚠ cell-cycle shift, would explain all of this change | [[Auranofin (drug)]] 5 µM 0.344× (z -10.8) |
| [[RKO (line)]] | wt | 172 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.04× (z +19.1) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SNU-1 (line)]] | wt | 584 | 1 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.03× (z +8.9) ⚠ cell-cycle shift, explains ~36% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.408× (z -10.3) |
| [[AN3 CA (line)]] | alt | 230 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.297× (z -9.0) |
| [[HCT15 (line)]] | alt | 179 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.385× (z -10.2) |
| [[HOP62 (line)]] | alt | 157 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.259× (z -11.5) |
| [[Hs 766T (line)]] | wt | 158 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.69× (z +8.7) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[HT-29 (line)]] | alt | 253 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.363× (z -11.3) |
| [[LOX-IMVI (line)]] | wt | 181 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.481× (z -9.1) ⚠ cell-cycle shift, explains ~95% of this change |
| [[MIA PaCa-2 (line)]] | alt | 241 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.397× (z -9.3) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H1573 (line)]] | alt | 227 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.19× (z +9.0) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[NCI-H2347 (line)]] | alt | 254 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +13.0) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SK-MEL-2 (line)]] | alt | 145 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.362× (z -8.8) |
| [[SNU-423 (line)]] | alt | 84.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.22× (z +13.1) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SW 1271 (line)]] | alt | 289 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.199× (z -8.8) |
| [[AsPC-1 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 221 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 192 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 136 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 94.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 55.4 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 152 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 267 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 153 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 208 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 85.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 136 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 325 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3541), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANLN]] | +0.83 | +0.82 / +0.82 | both halves | 7e-06 | pathway: HALLMARK_MITOTIC_SPINDLE; STRING 994 |
| [[MAD2L1]] | +0.83 | +0.83 / +0.82 | both halves | 7e-06 | STRING 779 |
| [[KIF11]] | +0.83 | +0.77 / +0.82 | both halves | 7e-06 | pathway: HALLMARK_MITOTIC_SPINDLE; STRING 891 |
| [[NCAPG]] | +0.83 | +0.78 / +0.82 | both halves | 7e-06 | STRING 865 |
| [[TMPO]] | +0.82 | +0.77 / +0.85 | both halves | 7e-06 | pathway: CDC42 GTPase cycle; STRING 541 |
| [[ARHGAP11A]] | +0.81 | +0.80 / +0.80 | both halves | 7e-06 | pathway: RHOA GTPase cycle; STRING 613 |
| [[KIF23]] | +0.81 | +0.79 / +0.80 | both halves | 7e-06 | pathway: HALLMARK_MITOTIC_SPINDLE; STRING 999 |
| [[MKI67]] | +0.81 | +0.77 / +0.78 | both halves | 7e-06 | STRING 676 |
| [[RACGAP1]] | +0.80 | +0.80 / +0.81 | both halves | 7e-06 | pathway: HALLMARK_MITOTIC_SPINDLE; STRING 999 |
| [[BIRC5]] | +0.80 | +0.77 / +0.76 | both halves | 7e-06 | pathway: HALLMARK_MITOTIC_SPINDLE; STRING 781 |
| [[TPX2]] | +0.80 | +0.78 / +0.79 | both halves | 7e-06 | pathway: HALLMARK_MITOTIC_SPINDLE; STRING 750 |
| [[NCAPD2]] | +0.80 | +0.78 / +0.76 | both halves | 7e-06 | STRING 625 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[E2F8]] | B | E2F8 activity raises ECT2's level | lines that do not express E2F8 (5) vs lines expressing it (45) | 2.10× lower at baseline in the lines without E2F8 | 0.066 | ⚠ across organs; also absent: CYB561, NMRAL1, RRM2; maybe low, not absent |
| [[CDC20]] | C | CDC20 activity raises ECT2's level | lines that do not express CDC20 (3) vs lines expressing it (47) | 2.40× lower at baseline in the lines without CDC20 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SPDL1, ARHGAP10, CDC45; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.803). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-37.9, -54.0); signed map (-47.9, -44.0). **Vector** length 153, 64.1% of its response variance represented; |z| ≥ 3 in 1,465 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *G2/M checkpoint* (hallmark, mean cos +0.64 to 60); *DREAM G2/M down* (control, mean cos +0.69 to 28); *Mitotic Prometaphase* (reactome, mean cos +0.62 to 48).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +8.1 | +1.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +8.1 | +1.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +6.5 | +1.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~37% of this change | +4.8 | +6.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | +4.6 | +8.5 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +3.2 | +1.1 |
|  | [[Demeclocycline (drug)]] 5 µM |  | +2.6 | +0.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.5 | -0.3 |
|  | [[Berbamine (drug)]] 0.05 µM |  | +2.4 | +0.8 |
|  | [[Ralimetinib dimesylate (drug)]] 5 µM |  | +2.3 | +1.3 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~44% of this change | -11.6 | -6.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -10.5 | -8.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | -10.0 | -3.6 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~43% of this change | -7.5 | -4.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -6.4 | -1.6 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -4.7 | -2.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -4.7 | -2.0 |
|  | [[EX229 (drug)]] 5 µM |  | -4.3 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | epithelial cell transforming 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q26.31 — chr3:172,750,682-172,821,474 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ARHGEF31 |
| Gene groups (HGNC) | Dbl family Rho GEFs |
| Hallmark sets | MITOTIC_SPINDLE |
| Reactome | 14 pathways, smallest: NRAGE signals death through JNK; G alpha (12/13) signalling events; RHOB GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H8V3](https://www.uniprot.org/uniprotkb/Q9H8V3) (Protein ECT2):

> Guanine nucleotide exchange factor (GEF) that catalyzes the exchange of GDP for GTP. Promotes guanine nucleotide exchange on the Rho family members of small GTPases, like RHOA, RHOC, RAC1 and CDC42. Required for signal transduction pathways involved in the regulation of cytokinesis. Component of the centralspindlin complex that serves as a microtubule-dependent and Rho-mediated signaling required for the myosin contractile ring formation during the cell cycle cytokinesis. Regulates the …

**Summary**, from NCBI Gene [1894](https://www.ncbi.nlm.nih.gov/gene/1894):

> The protein encoded by this gene is a guanine nucleotide exchange factor and transforming protein that is related to Rho-specific exchange factors and yeast cell cycle regulators. The expression of this gene is elevated with the onset of DNA synthesis and remains elevated during G2 and M phases. In situ hybridization analysis showed that expression is at a high level in cells undergoing mitosis in regenerating liver. Thus, this protein is expressed in a cell cycle-dependent manner during liver …

**Accessions** — [HGNC:3155](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3155) · Entrez [1894](https://www.ncbi.nlm.nih.gov/gene/1894) · UniProt [Q9H8V3](https://www.uniprot.org/uniprotkb/Q9H8V3) · Ensembl [ENSG00000114346](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000114346)

## Data

Gene col 3541: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3541); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3541, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3541]; `tensor/DDL_lfc|DDL_z.npy` [3541]; `embed/gene_vectors.npy` [3541]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3541 or target_col == 3541). Every well: [[ECT2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ECT2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
