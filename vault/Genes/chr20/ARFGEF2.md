---
symbol: "ARFGEF2"
type: "gene"
col: 4496
ensembl_id: "ENSG00000124198"
name: "ARF guanine nucleotide exchange factor 2"
location: "20q13.13"
module: 122
arm: "+"
pooled_cpm: 267.32
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 9
n_dd_up_clean: 8
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/122"]
generated_by: "tahoemap"
---

# ARFGEF2

*ARF guanine nucleotide exchange factor 2* — 20q13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.61× (z +17.7, q 0e+00, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (7 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.689× (z -13.8, q 1e-40, down in 45 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Tucidinostat (drug)]] 5 µM in 13 lines (SW480 0.667×, NCI-H2030 0.637×, HOP62 0.649×, A498 0.640×, …); [[Topotecan (hydrochloride) (drug)]] 5 µM in 4 lines (SW1417 0.453×, RKO 0.467×, Panc 03.27 0.545×, COLO 205 0.504×; ⚠ toxic); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (AsPC-1 0.579×, SW480 0.689×, SW1417 0.666×; ⚠ cell-cycle shift, explains ~27% of this change); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 2 lines (HOP62 0.601×, SW1417 0.704×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BOD1]] (+0.66, fdr 7e-06), [[C1orf43]] (+0.64, fdr 7e-06), [[PHC3]] (+0.62, fdr 7e-06); moves opposite to [[CSNK1E]] (-0.57, fdr 4e-05), [[GPRIN1]] (-0.56, fdr 1e-05), [[LRRC8C]] (-0.55, fdr 1e-05).
> It is in [[Module 122]], a single-armed module (Transferrin endocytosis and recycling).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[LYPD3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4496.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.61×** | +17.7 | 0e+00 | 41/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.52×** | +11.0 | 8e-26 | 44/48 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.09×** | +8.6 | 1e-15 | 37/49 (BT-474, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.39×** | +8.6 | 1e-15 | 33/48 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.36×** | +8.0 | 1e-13 | 39/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.29×** | +6.6 | 3e-09 | 32/48 (NCI-H23, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.29×** | +6.3 | 2e-08 | 27/48 (PANC-1, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.67×** | +6.0 | 1e-07 | 36/48 (SW480, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | 1.15× | +5.0 | 4e-05 | 18/48 (A-427, LOX-IMVI, …) | rises with dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | 1.19× | +4.5 | 4e-04 | 21/48 (HT-29, NCI-H460, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.05× | +4.2 | 0.001 | 0/50 | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~2% of this change | 1.16× | +3.9 | 0.005 | 22/48 (NCI-H460, A-172, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.36×** | +3.6 | 0.014 | 27/49 (Panc 03.27, C32, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | 1.16× | +3.6 | 0.014 | 15/48 (PANC-1, LOX-IMVI, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.14× | +3.4 | 0.026 | 13/48 (PANC-1, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 1.14× | +3.3 | 0.033 | 4/48 (SNU-423, NCI-H1573, …) | inconsistent across doses | low cells (technical?) |
| [[Anethole trithione (drug)]] 0.5 µM |  | 1.12× | +3.0 | 0.082 | 0/48 | two highest doses |  |
| [[Erlotinib (drug)]] 0.05 µM |  | 1.13× | +3.0 | 0.082 | 3/48 (NCI-H1792, LS 180, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 12 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4496.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Tucidinostat (drug)]] 5 µM in 13 lines (SW480 0.667×, NCI-H2030 0.637×, HOP62 0.649×, A498 0.640×, …); [[Topotecan (hydrochloride) (drug)]] 5 µM in 4 lines (SW1417 0.453×, RKO 0.467×, Panc 03.27 0.545×, COLO 205 0.504×; ⚠ toxic); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (AsPC-1 0.579×, SW480 0.689×, SW1417 0.666×; ⚠ cell-cycle shift, explains ~27% of this change); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 2 lines (HOP62 0.601×, SW1417 0.704×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.689×** | -13.8 | 1e-40 | 45/48 (SW480, NCI-H2030, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.711×** | -8.9 | 1e-16 | 44/49 (C32, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.708×** | -8.7 | 5e-16 | 39/47 (SW1417, RKO, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.762×** | -7.1 | 1e-10 | 31/48 (A498, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.764×** | -7.1 | 2e-10 | 31/48 (A498, AsPC-1, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.772×** | -6.8 | 9e-10 | 33/48 (NCI-H1573, NCI-H460, …) | all doses, flat |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | 0.834× | -6.8 | 1e-09 | 22/49 (AsPC-1, SW480, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.792×** | -6.1 | 7e-08 | 31/48 (SW480, LoVo, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | **0.810×** | -5.1 | 2e-05 | 24/45 (AsPC-1, J82, …) | all doses, flat | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.826×** | -5.0 | 3e-05 | 23/48 (NCI-H2347, MIA PaCa-2, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~90% of this change | 0.834× | -4.8 | 1e-04 | 24/49 (J82, A498, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~83% of this change | 0.834× | -4.6 | 2e-04 | 22/44 (NCI-H1573, HT-29, …) | all doses, flat | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~23% of this change | 0.842× | -4.5 | 3e-04 | 18/48 (RPMI-7951, NCI-H2030, …) | inconsistent across doses | low cells (technical?) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | 0.858× | -4.0 | 0.002 | 16/48 (J82, SW1417, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.915× | -3.3 | 0.037 | 13/48 (HOP62, SW1417, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4496. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 218 | 6 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.64× (z +33.7) | [[Panobinostat (drug)]] 0.5 µM 0.594× (z -9.6) ⚠ cell-cycle shift, explains ~46% of this change |
| [[A498 (line)]] | wt | 322 | 3 (1 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +20.2) | [[Panobinostat (drug)]] 5 µM 0.530× (z -10.9) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 0.640× (z -10.9) |
| [[BT-474 (line)]] | alt | 452 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.91× (z +26.9) | — |
| [[NCI-H1573 (line)]] | alt | 321 | 5 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +20.6) | [[Panobinostat (drug)]] 0.5 µM 0.440× (z -10.5) ⚠ cell-cycle shift, explains ~46% of this change |
| [[NCI-H23 (line)]] | alt | 358 | 7 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.33× (z +15.6) | — |
| [[PANC-1 (line)]] | alt | 186 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.72× (z +30.2) | — |
| [[RKO (line)]] | wt | 269 | 2 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +13.7) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.467× (z -11.1) ⚠ toxic · without an alert: [[Tucidinostat (drug)]] 5 µM 0.661× (z -8.9) |
| [[HOP62 (line)]] | alt | 159 | 2 | 3 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.69× (z +9.5) | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.601× (z -13.0) |
| [[SNU-423 (line)]] | alt | 303 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +21.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.646× (z -9.3) ⚠ cell-cycle shift, explains ~27% of this change |
| [[A-172 (line)]] | wt | 167 | 3 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.79× (z +29.1) | [[Tucidinostat (drug)]] 5 µM 0.645× (z -9.6) |
| [[A-427 (line)]] | wt | 202 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.66× (z +12.5) | [[Dinaciclib (drug)]] 0.5 µM 0.593× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~90% of this change |
| [[Hs 766T (line)]] | wt | 562 | 3 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.80× (z +14.4) | [[Tucidinostat (drug)]] 5 µM 0.617× (z -9.6) |
| [[NCI-H2347 (line)]] | alt | 219 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +27.2) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.621× (z -9.2) ⚠ toxic |
| [[SW1417 (line)]] | alt | 581 | 0 | 4 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.453× (z -14.4) ⚠ toxic |
| [[SW480 (line)]] | alt | 287 | 2 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.73× (z +12.8) | [[Panobinostat (drug)]] 0.05 µM 0.641× (z -10.4) ⚠ cell-cycle shift, explains ~19% of this change |
| [[AsPC-1 (line)]] | alt | 339 | 0 | 3 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.579× (z -13.1) ⚠ cell-cycle shift, explains ~27% of this change |
| [[COLO 205 (line)]] | alt | 403 | 2 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.15× (z +12.1) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.504× (z -10.4) ⚠ toxic |
| [[HT-29 (line)]] | alt | 312 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.66× (z +11.8) | [[Dinaciclib (drug)]] 5 µM 0.531× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~83% of this change |
| [[J82 (line)]] | alt | 587 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +21.8) | [[Dinaciclib (drug)]] 0.5 µM 0.588× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~90% of this change |
| [[NCI-H2030 (line)]] | alt | 274 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +18.5) | [[Tucidinostat (drug)]] 5 µM 0.637× (z -11.1) |
| [[Panc 03.27 (line)]] | alt | 253 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +15.5) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.545× (z -10.5) ⚠ toxic |
| [[C32 (line)]] | wt | 308 | 0 | 2 | — | [[Tucidinostat (drug)]] 5 µM 0.641× (z -9.1) |
| [[HS-578T (line)]] | alt | 214 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +11.4) | [[Tucidinostat (drug)]] 5 µM 0.607× (z -10.0) |
| [[hTERT-HPNE (line)]] | wt | 147 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +15.7) | — |
| [[LOX-IMVI (line)]] | wt | 153 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.54× (z +9.9) | — |
| [[NCI-H1792 (line)]] | alt | 232 | 2 | 0 | [[Harringtonine (drug)]] 5 µM 2.03× (z +10.9) | — |
| [[SW48 (line)]] | wt | 201 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +14.9) | — |
| [[A549 (line)]] | wt | 153 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +18.5) | — |
| [[CFPAC-1 (line)]] | alt | 212 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +20.8) | — |
| [[HCT15 (line)]] | alt | 215 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +9.5) | — |
| [[KATO III (line)]] | alt | 373 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.529× (z -9.4) ⚠ toxic |
| [[LoVo (line)]] | wt | 218 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.529× (z -8.7) ⚠ cell-cycle shift, explains ~46% of this change |
| [[RPMI-7951 (line)]] | alt | 291 | 0 | 1 | — | [[Tucidinostat (drug)]] 5 µM 0.630× (z -9.5) |
| [[SK-MEL-2 (line)]] | alt | 219 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +17.9) | — |
| [[SW 900 (line)]] | alt | 259 | 0 | 1 | — | [[Tucidinostat (drug)]] 5 µM 0.624× (z -10.5) |
| [[AN3 CA (line)]] | alt | 204 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 171 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 156 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 170 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 133 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 339 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 259 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 241 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 246 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 262 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 249 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 274 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 249 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 190 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4496), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*47 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BOD1]] | +0.66 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[C1orf43]] | +0.64 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[PHC3]] | +0.62 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[WASHC2C]] | +0.61 | +0.45 / +0.64 | both halves | 3e-05 |  |
| [[WASHC2A]] | +0.59 | +0.40 / +0.64 | both halves | 5e-05 |  |
| [[TRPM7]] | +0.58 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[NDUFB5]] | +0.57 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[SLC25A46]] | +0.57 | +0.41 / +0.59 | both halves | 4e-05 |  |
| [[VPS41]] | +0.56 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[MCCC1]] | +0.56 | +0.56 / +0.44 | both halves | 3e-05 |  |
| [[VPS33A]] | +0.56 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[RABGAP1]] | +0.56 | +0.63 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*53 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CSNK1E]] | -0.57 | -0.41 / -0.56 | both halves | 4e-05 |  |
| [[GPRIN1]] | -0.56 | -0.56 / -0.54 | both halves | 1e-05 |  |
| [[LRRC8C]] | -0.55 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[CDYL2]] | -0.53 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[TIAM1]] | -0.53 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[ABTB3]] | -0.52 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[ARID3B]] | -0.52 | -0.37 / -0.56 | both halves | 8e-05 |  |
| [[PAQR5]] | -0.52 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[KIAA1549L]] | -0.52 | -0.56 / -0.42 | both halves | 4e-05 |  |
| [[LUZP1]] | -0.51 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[PSD3]] | -0.51 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[CORO2B]] | -0.51 | -0.53 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LYPD3]] | B | LYPD3 activity raises ARFGEF2's level | lines that do not express LYPD3 (15) vs lines expressing it (35) | 1.22× lower at baseline in the lines without LYPD3 | 0.012 | ⚠ within organs, on part of the lines; also absent: ENSG00000259345, ENSG00000256982, IGSF9; maybe low, not absent |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises ARFGEF2's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises ARFGEF2's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[CCK]] | B | CCK activity raises ARFGEF2's level | lines that do not express CCK (42) vs lines expressing it (8) | 1.39× lower at baseline in the lines without CCK | 0.098 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: BMP10, ENSG00000287530, S100A8 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 122]] — Transferrin endocytosis and recycling; 40 genes; every member is in the + arm (projection on the module's main direction 0.619). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-19.5, 15.8); signed map (-3.6, -7.5). **Vector** length 106, 35.9% of its response variance represented; |z| ≥ 3 in 1,176 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +6.6 | +5.0 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +6.4 | +4.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.1 | +17.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~2% of this change | +4.2 | +3.9 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.5 | +1.4 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +3.2 | +1.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +2.8 | +2.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.8 | -1.5 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +2.7 | +0.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.6 | +1.1 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -11.6 | -13.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -9.7 | -8.9 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~19% of this change | -5.9 | -6.1 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -4.4 | -4.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -3.6 | -1.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.9 | -1.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.0 | -1.4 |
|  | [[vincristine (drug)]] 0.5 µM |  | -1.8 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | ARF guanine nucleotide exchange factor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.13 — chr20:48,921,711-49,036,693 (+) |
| Ensembl biotype | protein_coding |
| Also known as | BIG2 |
| Gene groups (HGNC) | A-kinase anchoring proteins; Armadillo like helical domain containing; ArfGEF family |
| Hallmark sets | PROTEIN_SECRETION |
| Reactome | 3 pathways, smallest: Association of TriC/CCT with target proteins during biosynthesis; Chaperonin-mediated protein folding; Protein folding |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y6D5](https://www.uniprot.org/uniprotkb/Q9Y6D5) (Brefeldin A-inhibited guanine nucleotide-exchange protein 2):

> Promotes guanine-nucleotide exchange on ARF1 and ARF3 and to a lower extent on ARF5 and ARF6. Promotes the activation of ARF1/ARF5/ARF6 through replacement of GDP with GTP. Involved in the regulation of Golgi vesicular transport. Required for the integrity of the endosomal compartment. Involved in trafficking from the trans-Golgi network (TGN) to endosomes and is required for membrane association of the AP-1 complex and GGA1. Seems to be involved in recycling of the transferrin receptor from …

**Summary**, from NCBI Gene [10564](https://www.ncbi.nlm.nih.gov/gene/10564):

> ADP-ribosylation factors (ARFs) play an important role in intracellular vesicular trafficking. The protein encoded by this gene is involved in the activation of ARFs by accelerating replacement of bound GDP with GTP and is involved in Golgi transport. It contains a Sec7 domain, which may be responsible for its guanine-nucleotide exchange activity and also brefeldin A inhibition. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:15853](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15853) · Entrez [10564](https://www.ncbi.nlm.nih.gov/gene/10564) · UniProt [Q9Y6D5](https://www.uniprot.org/uniprotkb/Q9Y6D5) · Ensembl [ENSG00000124198](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000124198)

## Data

Gene col 4496: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4496); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4496, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4496]; `tensor/DDL_lfc|DDL_z.npy` [4496]; `embed/gene_vectors.npy` [4496]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4496 or target_col == 4496). Every well: [[ARFGEF2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARFGEF2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
