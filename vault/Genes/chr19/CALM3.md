---
symbol: "CALM3"
type: "gene"
col: 8290
ensembl_id: "ENSG00000160014"
name: "calmodulin 3"
location: "19q13.32"
module: 50
arm: "+"
pooled_cpm: 85.0
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 11
n_dd_up_clean: 2
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/050"]
generated_by: "tahoemap"
---

# CALM3

*calmodulin 3* — 19q13.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.67× (z +17.3, q 0e+00, up in 48 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Docetaxel (drug)]] 5 µM: 1.19× (z +3.3, q 0.042, up in 21 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 12 lines (PANC-1 5.70×, A-172 6.76×, HEC-1-A 4.37×, CFPAC-1 4.99×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (PANC-1 5.23×, MIA PaCa-2 7.82×, HEC-1-A 3.83×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.356× (z -19.4, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GGH]] (+0.70, fdr 1e-05), [[BSG]] (+0.69, fdr 7e-06), [[CLSTN1]] (+0.68, fdr 1e-05); moves opposite to [[DNAJC2]] (-0.66, fdr 1e-05), [[NEPRO-AS1]] (-0.66, fdr 1e-05), [[NSRP1]] (-0.65, fdr 7e-06).
> It is in [[Module 050]], a single-armed module (Extracellular matrix organization).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 12 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8290.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 12 lines (PANC-1 5.70×, A-172 6.76×, HEC-1-A 4.37×, CFPAC-1 4.99×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (PANC-1 5.23×, MIA PaCa-2 7.82×, HEC-1-A 3.83×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **3.67×** | +17.3 | 0e+00 | 48/49 (PANC-1, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.80×** | +17.1 | 0e+00 | 41/41 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **2.26×** | +10.0 | 2e-21 | 44/45 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~52% of this change | **1.70×** | +7.0 | 3e-10 | 42/48 (HOP62, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.44×** | +4.8 | 2e-04 | 33/48 (SW480, RKO, …) | two highest doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.44×** | +4.6 | 3e-04 | 33/47 (CFPAC-1, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.10× | +4.2 | 0.002 | 3/49 (MIA PaCa-2, HOP62, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **1.35×** | +4.0 | 0.005 | 28/48 (SW480, NCI-H1792, …) | two highest doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.34×** | +3.9 | 0.006 | 27/48 (PANC-1, C-33 A, …) | rises with dose | position effect removed |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.32×** | +3.7 | 0.013 | 30/48 (SW1417, HT-29, …) | rises with dose |  |
| [[Docetaxel (drug)]] 5 µM |  | 1.19× | +3.3 | 0.042 | 21/48 (HT-29, CFPAC-1, …) | inconsistent across doses |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.45×** | +3.3 | 0.044 | 26/48 (SW1417, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~84% of this change | **1.27×** | +3.2 | 0.060 | 21/48 (SW480, NCI-H1792, …) | rises with dose |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~73% of this change | **1.26×** | +3.0 | 0.094 | 21/48 (HT-29, HOP62, …) | inconsistent across doses | position effect removed |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.25×** | +3.0 | 0.097 | 23/48 (LOX-IMVI, HT-29, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8290.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.356×** | -19.4 | 0e+00 | 47/48 (MIA PaCa-2, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.396×** | -12.3 | 2e-32 | 47/48 (A498, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.469×** | -9.7 | 7e-20 | 47/48 (H4, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.662×** | -5.5 | 6e-06 | 32/48 (A-427, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.668×** | -5.4 | 9e-06 | 37/48 (RPMI-7951, H4, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.702×** | -4.7 | 3e-04 | 31/48 (NCI-H1573, HCT15, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~68% of this change | **0.700×** | -4.5 | 6e-04 | 34/48 (LOX-IMVI, KATO III, …) | all doses, flat |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.536×** | -4.0 | 0.004 | 29/48 (LOX-IMVI, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 5 µM |  | **0.598×** | -3.3 | 0.060 | 30/49 (J82, SHP-77, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.785×** | -3.2 | 0.073 | 24/48 (Hs 766T, SW1417, …) | two highest doses | position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~49% of this change | **0.610×** | -3.2 | 0.077 | 20/45 (J82, Panc 03.27, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, +0.52 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8290. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 57.2 | 4 (4 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 5.61× (z +13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | [[Homoharringtonine (drug)]] 5 µM 0.219× (z -17.1) |
| [[CFPAC-1 (line)]] | alt | 107 | 4 (4 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 4.99× (z +15.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -15.2) |
| [[NCI-H2347 (line)]] | alt | 117 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.25× (z +12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | [[Homoharringtonine (drug)]] 5 µM 0.336× (z -16.0) |
| [[A-172 (line)]] | wt | 57.6 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 6.76× (z +16.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -17.1) |
| [[A498 (line)]] | wt | 86.5 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.48× (z +12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -23.0) |
| [[HEC-1-A (line)]] | alt | 166 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 4.37× (z +15.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | [[Homoharringtonine (drug)]] 5 µM 0.377× (z -14.7) |
| [[HS-578T (line)]] | alt | 127 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.42× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -15.0) |
| [[MIA PaCa-2 (line)]] | alt | 101 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 7.82× (z +15.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.0625× (z -30.3) |
| [[Panc 03.27 (line)]] | alt | 69.6 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 4.90× (z +14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | [[Homoharringtonine (drug)]] 5 µM 0.400× (z -11.8) |
| [[A-427 (line)]] | wt | 114 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -18.8) |
| [[H4 (line)]] | wt | 113 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.83× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -15.1) |
| [[HCT15 (line)]] | alt | 107 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.67× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | [[Homoharringtonine (drug)]] 5 µM 0.313× (z -12.2) |
| [[HT-29 (line)]] | alt | 138 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.64× (z +12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -16.8) |
| [[hTERT-HPNE (line)]] | wt | 78.8 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 4.93× (z +12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | [[Homoharringtonine (drug)]] 5 µM 0.336× (z -12.0) |
| [[J82 (line)]] | alt | 117 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.96× (z +14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | [[Homoharringtonine (drug)]] 5 µM 0.311× (z -17.0) |
| [[KATO III (line)]] | alt | 112 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.87× (z +13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -23.1) |
| [[LOX-IMVI (line)]] | wt | 105 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.67× (z +12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | [[Homoharringtonine (drug)]] 5 µM 0.286× (z -16.6) |
| [[NCI-H1573 (line)]] | alt | 37.4 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 6.30× (z +13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -13.4) |
| [[NCI-H2030 (line)]] | alt | 110 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.65× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | [[Homoharringtonine (drug)]] 5 µM 0.431× (z -10.6) |
| [[PANC-1 (line)]] | alt | 86.5 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.70× (z +17.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | [[Homoharringtonine (drug)]] 5 µM 0.496× (z -10.0) |
| [[RPMI-7951 (line)]] | alt | 93.6 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.24× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | [[Homoharringtonine (drug)]] 5 µM 0.336× (z -12.5) |
| [[SNU-423 (line)]] | alt | 50.6 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.97× (z +11.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -15.4) |
| [[SW480 (line)]] | alt | 72.6 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.18× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -15.9) |
| [[A549 (line)]] | wt | 96.4 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.49× (z +14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -15.6) |
| [[BT-474 (line)]] | alt | 63.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -15.0) |
| [[LoVo (line)]] | wt | 90.1 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.81× (z +12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | [[Homoharringtonine (drug)]] 5 µM 0.332× (z -14.8) |
| [[NCI-H23 (line)]] | alt | 58.6 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 5.81× (z +14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.331× (z -9.1) |
| [[NCI-H460 (line)]] | wt | 35.3 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 5.23× (z +12.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.430× (z -9.2) |
| [[SW1417 (line)]] | alt | 128 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.68× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | [[Homoharringtonine (drug)]] 5 µM 0.568× (z -9.2) |
| [[SW48 (line)]] | wt | 88.2 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 3.62× (z +9.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.313× (z -12.3) |
| [[C32 (line)]] | wt | 45.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.39× (z +12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[COLO 205 (line)]] | alt | 85.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -16.8) |
| [[HepG2_C3A (line)]] | wt | 54.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.37× (z +9.7) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 49.2 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.27× (z +11.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -12.9) |
| [[LS 180 (line)]] | wt | 105 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.71× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | [[Homoharringtonine (drug)]] 5 µM 0.426× (z -9.8) |
| [[NCI-H1792 (line)]] | alt | 41.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.29× (z +14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[SHP-77 (line)]] | alt | 89.1 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.25× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | [[Homoharringtonine (drug)]] 5 µM 0.435× (z -10.8) |
| [[SW 900 (line)]] | alt | 66.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.46× (z +12.6) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 53.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.354× (z -12.7) |
| [[C-33 A (line)]] | alt | 89.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.65× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[CHP-212 (line)]] | wt | 53.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -9.4) |
| [[NCI-H661 (line)]] | alt | 146 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -10.0) |
| [[RKO (line)]] | wt | 64.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.15× (z +13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[AN3 CA (line)]] | alt | 66.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 50.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 62.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 42.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 64.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 87.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 77.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8290), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GGH]] | +0.70 | +0.68 / +0.56 | both halves | 1e-05 |  |
| [[BSG]] | +0.69 | +0.70 / +0.62 | both halves | 7e-06 |  |
| [[CLSTN1]] | +0.68 | +0.71 / +0.51 | both halves | 1e-05 |  |
| [[NEURL1B]] | +0.68 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[GUSB]] | +0.67 | +0.67 / +0.46 | both halves | 2e-05 |  |
| [[KIFC1]] | +0.66 | +0.74 / +0.54 | both halves | 1e-05 |  |
| [[NAGA]] | +0.65 | +0.70 / +0.56 | both halves | 1e-05 |  |
| [[TWSG1]] | +0.64 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[CIT]] | +0.64 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[SELENON]] | +0.64 | +0.70 / +0.49 | both halves | 1e-05 | same gene group |
| [[PRKACA]] | +0.64 | +0.67 / +0.41 | both halves | 4e-05 | STRING 989 |
| [[CENPI]] | +0.63 | +0.67 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAJC2]] | -0.66 | -0.72 / -0.52 | both halves | 1e-05 |  |
| [[NEPRO-AS1]] | -0.66 | -0.61 / -0.57 | both halves | 1e-05 |  |
| [[NSRP1]] | -0.65 | -0.66 / -0.61 | both halves | 7e-06 |  |
| [[CCDC174]] | -0.63 | -0.67 / -0.47 | both halves | 2e-05 |  |
| [[TATDN1]] | -0.63 | -0.65 / -0.59 | both halves | 7e-06 |  |
| [[WASHC1]] | -0.62 | -0.62 / -0.47 | both halves | 2e-05 |  |
| [[GATAD1]] | -0.62 | -0.62 / -0.49 | both halves | 1e-05 |  |
| [[RSL1D1]] | -0.61 | -0.71 / -0.55 | both halves | 1e-05 |  |
| [[C1orf131]] | -0.61 | -0.64 / -0.39 | both halves | 5e-05 |  |
| [[RPL7L1]] | -0.61 | -0.62 / -0.49 | both halves | 1e-05 |  |
| [[ZC3H8]] | -0.60 | -0.70 / -0.40 | both halves | 5e-05 |  |
| [[SNW1]] | -0.60 | -0.64 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity raises CALM3's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 050]] — Extracellular matrix organization; 92 genes; every member is in the + arm (projection on the module's main direction 0.677). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-33.6, -38.3); signed map (-29.3, -38.1). **Vector** length 119, 43.9% of its response variance represented; |z| ≥ 3 in 1,025 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +7.1 | +2.5 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.5 | +2.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.5 | +2.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +5.4 | +3.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | +4.9 | +4.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.1 | +1.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.3 | +2.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.1 | +1.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +2.0 | -0.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.0 | +0.8 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -10.8 | -12.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | -9.1 | -9.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -8.7 | -5.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -7.8 | -19.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.5 | -5.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.7 | -2.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.9 | -1.4 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -3.3 | -2.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.9 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | calmodulin 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.32 — chr19:46,601,074-46,610,782 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PHKD, PHKD3 |
| Gene groups (HGNC) | Receptor ligands; EF-hand domain containing; Phosphorylase kinase subunits |
| Hallmark sets | COMPLEMENT |
| Reactome | 6 pathways, smallest: CASP4 inflammasome assembly; Enterobacterial factors antagonize host defense; Non-canonical inflammasome activation |
| Matched by | ensembl_id |

**Function**, from UniProt [P0DP25](https://www.uniprot.org/uniprotkb/P0DP25) (Calmodulin-3):

> Calmodulin acts as part of a calcium signal transduction pathway by mediating the control of a large number of enzymes, ion channels, aquaporins and other proteins through calcium-binding. Calcium-binding is required for the activation of calmodulin. Among the enzymes to be stimulated by the calmodulin-calcium complex are a number of protein kinases, such as myosin light-chain kinases and calmodulin-dependent protein kinase type II (CaMK2), and phosphatases. Together with CCP110 and centrin, is …

**Summary**, from NCBI Gene [808](https://www.ncbi.nlm.nih.gov/gene/808):

> This gene encodes a member of a family of proteins that binds calcium and functions as a enzymatic co-factor. Activity of this protein is important in the regulation of the cell cycle and cytokinesis. Multiple alternatively spliced transcript variants have been observed at this gene. [provided by RefSeq, Aug 2016]

**Accessions** — [HGNC:1449](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1449) · Entrez [808](https://www.ncbi.nlm.nih.gov/gene/808) · UniProt [P0DP25](https://www.uniprot.org/uniprotkb/P0DP25) · Ensembl [ENSG00000160014](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000160014)

## Data

Gene col 8290: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8290); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8290, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8290]; `tensor/DDL_lfc|DDL_z.npy` [8290]; `embed/gene_vectors.npy` [8290]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8290 or target_col == 8290). Every well: [[CALM3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CALM3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
