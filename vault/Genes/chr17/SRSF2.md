---
symbol: "SRSF2"
type: "gene"
col: 8439
ensembl_id: "ENSG00000161547"
name: "serine and arginine rich splicing factor 2"
location: "17q25.2"
module: 33
arm: "+"
pooled_cpm: 47.49
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 1
n_dd_up_clean: 9
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# SRSF2

*serine and arginine rich splicing factor 2* — 17q25.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (14 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.53× (z +21.0, q 0e+00, up in 47 of 48 measured lines) ⚠ cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 3.04× (z +13.1, q 1e-36, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Ponatinib (drug)]] 5 µM: 0.715× (z -4.0, q 0.039, down in 27 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Tucidinostat (drug)]] 0.5 µM in 1 line (CHP-212 0.132×; ⚠ cell-cycle shift, explains ~88% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SRSF7]] (+0.72, fdr 7e-06), [[TRA2B]] (+0.60, fdr 1e-05), [[SNHG17]] (+0.58, fdr 1e-05); moves opposite to [[ARPC3]] (-0.54, fdr 1e-05), [[ATP6V1E1]] (-0.54, fdr 1e-04), [[GINM1]] (-0.53, fdr 4e-05).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 15 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8439.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **3.53×** | +21.0 | 0e+00 | 47/48 (AsPC-1, A498, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.04×** | +13.1 | 1e-36 | 44/48 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **2.74×** | +11.4 | 8e-28 | 46/48 (AsPC-1, PANC-1, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | **1.93×** | +7.4 | 1e-11 | 40/47 (NCI-H460, PANC-1, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.71×** | +6.3 | 4e-08 | 32/48 (NCI-H1792, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | **1.65×** | +5.8 | 5e-07 | 37/47 (PANC-1, NCI-H460, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **1.58×** | +5.4 | 7e-06 | 37/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~95% of this change | **1.56×** | +5.2 | 2e-05 | 34/47 (RKO, NCI-H1792, …) | all doses, flat | composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.51×** | +4.9 | 8e-05 | 33/48 (PANC-1, HS-578T, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.54×** | +4.8 | 8e-05 | 29/47 (CFPAC-1, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~89% of this change | **1.50×** | +4.6 | 2e-04 | 25/41 (HT-29, HepG2/C3A, …) | all doses, flat | composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.46×** | +4.4 | 5e-04 | 30/48 (HS-578T, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.42×** | +4.1 | 0.002 | 28/48 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~80% of this change | **1.40×** | +4.0 | 0.003 | 28/46 (A-172, Panc 03.27, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **1.38×** | +3.7 | 0.007 | 24/48 (SW480, NCI-H1792, …) | top dose only | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.37×** | +3.7 | 0.008 | 24/48 (NCI-H460, hTERT-HPNE, …) | inconsistent across doses |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.56×** | +3.7 | 0.008 | 28/48 (PANC-1, SHP-77, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **1.49×** | +3.3 | 0.027 | 23/48 (Panc 03.27, HT-29, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.47×** | +3.2 | 0.037 | 21/47 (HCT15, RKO, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.43×** | +3.0 | 0.072 | 22/48 (NCI-H460, NCI-H2030, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8439.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Tucidinostat (drug)]] 0.5 µM in 1 line (CHP-212 0.132×; ⚠ cell-cycle shift, explains ~88% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **0.715×** | -4.0 | 0.039 | 27/48 (A-427, KATO III, …) | rises with dose |  |
| [[Vortioxetine (drug)]] 0.5 µM |  | 0.753× | -3.4 | 0.21 | 22/48 (NCI-H460, NCI-H1792, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, +0.49 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8439. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 34.3 | 9 (8 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.77× (z +18.0) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.18× (z +13.4) | — |
| [[PANC-1 (line)]] | alt | 59.5 | 6 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.26× (z +19.1) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.70× (z +12.2) | — |
| [[AsPC-1 (line)]] | alt | 34.1 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.13× (z +21.4) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.25× (z +10.4) | — |
| [[NCI-H1792 (line)]] | alt | 30.3 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.23× (z +17.7) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.71× (z +10.6) | — |
| [[A498 (line)]] | wt | 47.1 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.29× (z +19.9) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.89× (z +11.5) | — |
| [[HEC-1-A (line)]] | alt | 61.0 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +12.0) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.90× (z +9.2) | — |
| [[NCI-H1573 (line)]] | alt | 29.2 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.09× (z +18.3) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.57× (z +12.3) | — |
| [[A-172 (line)]] | wt | 32.5 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.22× (z +12.2) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.33× (z +8.8) | — |
| [[A549 (line)]] | wt | 44.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.64× (z +13.9) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.43× (z +9.4) | — |
| [[C32 (line)]] | wt | 32.1 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.26× (z +17.6) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 9.50× (z +12.6) | — |
| [[COLO 205 (line)]] | alt | 32.5 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.48× (z +16.2) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[H4 (line)]] | wt | 48.0 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 0.05 µM 4.25× (z +8.7) ⚠ cell-cycle shift, explains ~69% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.21× (z +8.6) | — |
| [[HOP62 (line)]] | alt | 44.0 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.76× (z +15.8) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.51× (z +10.6) | — |
| [[HS-578T (line)]] | alt | 29.7 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.80× (z +14.2) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.95× (z +8.8) | — |
| [[hTERT-HPNE (line)]] | wt | 43.4 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.80× (z +16.3) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.60× (z +10.0) | — |
| [[KATO III (line)]] | alt | 49.9 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.89× (z +16.9) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[LoVo (line)]] | wt | 53.4 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.72× (z +13.9) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[LOX-IMVI (line)]] | wt | 42.8 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.51× (z +15.7) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.52× (z +11.1) | — |
| [[LS 180 (line)]] | wt | 40.5 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.92× (z +11.7) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 45.8 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.16× (z +10.8) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.29× (z +9.6) | — |
| [[Panc 03.27 (line)]] | alt | 46.4 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.19× (z +15.0) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.38× (z +10.9) | — |
| [[SHP-77 (line)]] | alt | 61.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +12.6) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.04× (z +11.1) | — |
| [[SNU-423 (line)]] | alt | 39.1 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.85× (z +14.7) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.67× (z +8.5) | — |
| [[SW1417 (line)]] | alt | 52.8 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.63× (z +14.5) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.98× (z +8.7) | — |
| [[AN3 CA (line)]] | alt | 50.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.26× (z +9.2) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[BT-474 (line)]] | alt | 47.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +9.1) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[CFPAC-1 (line)]] | alt | 41.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.48× (z +12.8) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[CHP-212 (line)]] | wt | 64.0 | 0 | 1 (1 ⚠) | — | [[Tucidinostat (drug)]] 0.5 µM 0.132× (z -9.5) ⚠ cell-cycle shift, explains ~88% of this change |
| [[HepG2_C3A (line)]] | wt | 45.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +8.8) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[Hs 766T (line)]] | wt | 22.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.70× (z +10.4) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[HT-29 (line)]] | alt | 40.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +10.2) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[J82 (line)]] | alt | 61.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.22× (z +12.6) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[NCI-H2347 (line)]] | alt | 44.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +9.6) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[RKO (line)]] | wt | 43.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.13× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~95% of this change | — |
| [[RPMI-7951 (line)]] | alt | 36.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.93× (z +11.4) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 50.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.87× (z +16.2) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[SW 900 (line)]] | alt | 33.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +11.1) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[A-427 (line)]] | wt | 71.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 61.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 52.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 79.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 58.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 52.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 68.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 41.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 42.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 52.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 66.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8439), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*56 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRSF7]] | +0.72 | +0.76 / +0.68 | both halves | 7e-06 | same gene group; pathway: HALLMARK_MYC_TARGETS_V1; STRING 961 |
| [[TRA2B]] | +0.60 | +0.59 / +0.55 | both halves | 1e-05 | same gene group; pathway: HALLMARK_E2F_TARGETS; STRING 998 |
| [[SNHG17]] | +0.58 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[FBXL6]] | +0.58 | +0.64 / +0.48 | both halves | 2e-05 |  |
| [[SRSF6]] | +0.57 | +0.72 / +0.48 | both halves | 2e-05 | same gene group; pathway: Dengue Virus-Host Interactions; STRING 927 |
| [[NOP56]] | +0.55 | +0.63 / +0.60 | both halves | 7e-06 | same gene group; pathway: HALLMARK_E2F_TARGETS |
| [[SRSF3]] | +0.55 | +0.65 / +0.49 | both halves | 1e-05 | same gene group; pathway: HALLMARK_MYC_TARGETS_V1; STRING 999 |
| [[TRMT61A]] | +0.54 | +0.60 / +0.44 | both halves | 3e-05 |  |
| [[THOP1]] | +0.53 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[HNRNPH1]] | +0.52 | +0.61 / +0.50 | both halves | 1e-05 | same gene group; pathway: Dengue Virus-Host Interactions; STRING 935 |
| [[FAAP100]] | +0.51 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[TRIM28]] | +0.51 | +0.55 / +0.56 | both halves | 1e-05 | same gene group; pathway: HALLMARK_MYC_TARGETS_V1 |

## Genes that move opposite

*44 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARPC3]] | -0.54 | -0.49 / -0.61 | both halves | 1e-05 |  |
| [[ATP6V1E1]] | -0.54 | -0.33 / -0.59 | both halves | 1e-04 |  |
| [[GINM1]] | -0.53 | -0.62 / -0.40 | both halves | 4e-05 |  |
| [[GAPVD1]] | -0.53 | -0.61 / -0.38 | both halves | 6e-05 |  |
| [[ATP6AP2]] | -0.51 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[SNX3]] | -0.50 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[PRDX5]] | -0.49 | -0.46 / -0.54 | both halves | 3e-05 |  |
| [[SMIM20]] | -0.48 | -0.44 / -0.36 | both halves | 1e-04 |  |
| [[DNASE2]] | -0.48 | -0.49 / -0.46 | both halves | 3e-05 |  |
| [[RPL39]] | -0.47 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[KDELR1]] | -0.47 | -0.47 / -0.46 | both halves | 2e-05 |  |
| [[GLUD1P3]] | -0.47 | -0.43 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.210). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-19.1, -45.1); signed map (10.9, -47.9). **Vector** length 84.1, 23.4% of its response variance represented; |z| ≥ 3 in 874 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +5.5 | +21.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.7 | +13.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +3.9 | +11.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.6 | +2.8 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +2.5 | +3.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.2 | +0.8 |
|  | [[crizotinib (drug)]] 5 µM |  | +2.0 | +1.9 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.9 | +1.4 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -6.3 | +0.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.0 | -2.9 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.3 | -1.9 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.1 | +1.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.1 | +2.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.8 | -2.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.8 | +1.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.7 | -4.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.6 | -2.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.6 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | serine and arginine rich splicing factor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.2 — chr17:76,734,115-76,737,333 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SC-35, SC35, PR264, SFRS2A; previously SFRS2 |
| Gene groups (HGNC) | RNA binding motif containing; Serine and arginine rich splicing factors; MicroRNA protein coding host genes |
| Hallmark sets | G2M_CHECKPOINT, E2F_TARGETS, MYC_TARGETS_V1 |
| Reactome | 12 pathways, smallest: mRNA Splicing - Minor Pathway; Transport of Mature mRNA derived from an Intron-Containing Transcript; Transport of Mature Transcript to Cytoplasm |
| Matched by | ensembl_id |

**Function**, from UniProt [Q01130](https://www.uniprot.org/uniprotkb/Q01130) (Serine/arginine-rich splicing factor 2):

> Necessary for the splicing of pre-mRNA. It is required for formation of the earliest ATP-dependent splicing complex and interacts with spliceosomal components bound to both the 5'- and 3'-splice sites during spliceosome assembly. It also is required for ATP-dependent interactions of both U1 and U2 snRNPs with pre-mRNA. Interacts with other spliceosomal components, via the RS domains, to form a bridge between the 5'- and 3'-splice site binding components, U1 snRNP and U2AF. Binds to purine-rich …

**Summary**, from NCBI Gene [6427](https://www.ncbi.nlm.nih.gov/gene/6427):

> The protein encoded by this gene is a member of the serine/arginine (SR)-rich family of pre-mRNA splicing factors, which constitute part of the spliceosome. Each of these factors contains an RNA recognition motif (RRM) for binding RNA and an RS domain for binding other proteins. The RS domain is rich in serine and arginine residues and facilitates interaction between different SR splicing factors. In addition to being critical for mRNA splicing, the SR proteins have also been shown to be …

**Accessions** — [HGNC:10783](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10783) · Entrez [6427](https://www.ncbi.nlm.nih.gov/gene/6427) · UniProt [Q01130](https://www.uniprot.org/uniprotkb/Q01130) · Ensembl [ENSG00000161547](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000161547)

## Data

Gene col 8439: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8439); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8439, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8439]; `tensor/DDL_lfc|DDL_z.npy` [8439]; `embed/gene_vectors.npy` [8439]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8439 or target_col == 8439). Every well: [[SRSF2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SRSF2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
