---
symbol: "LMTK2"
type: "gene"
col: 8995
ensembl_id: "ENSG00000164715"
name: "lemur tail kinase 2"
location: "7q21.3"
module: 148
arm: "-"
pooled_cpm: 135.49
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 4
n_dd_up_clean: 17
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/148"]
generated_by: "tahoemap"
---

# LMTK2

*lemur tail kinase 2* — 7q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.79× (z +22.0, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.510× (z -14.5, q 1e-44, down in 40 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Carbamazepine (drug)]] 5 µM: 0.830× (z -4.0, q 0.006, down in 22 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (CFPAC-1 0.206×, AsPC-1 0.123×, NCI-H2347 0.334×, HT-29 0.295×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 6 lines (NCI-H2347 0.361×, Panc 03.27 0.282×, CFPAC-1 0.368×, HT-29 0.323×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (NCI-H2347 0.304×, CFPAC-1 0.307×; ⚠ toxic; transcription drop); [[XRK3F2 (drug)]] 0.5 µM in 1 line (CHP-212 0.0941×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF277]] (+0.68, fdr 1e-05), [[ILRUN]] (+0.66, fdr 6e-05), [[CYRIB]] (+0.66, fdr 2e-05); moves opposite to [[POLI]] (-0.66, fdr 7e-06), [[PAN2]] (-0.63, fdr 5e-05), [[KRBOX5]] (-0.62, fdr 4e-05).
> It sits in the **-** arm of [[Module 148]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TTC22]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 8 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8995.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.79×** | +22.0 | 0e+00 | 48/48 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.69×** | +21.2 | 0e+00 | 48/48 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.54×** | +19.9 | 0e+00 | 47/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.22×** | +17.1 | 0e+00 | 45/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.23×** | +16.2 | 0e+00 | 46/48 (KATO III, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.08×** | +15.6 | 0e+00 | 47/48 (HT-29, LS 180, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.04×** | +15.3 | 0e+00 | 46/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **3.46×** | +13.6 | 5e-40 | 47/49 (SW480, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.87×** | +13.4 | 7e-39 | 42/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.68×** | +11.1 | 4e-27 | 43/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.61×** | +10.1 | 3e-22 | 37/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.35×** | +9.3 | 5e-19 | 42/48 (SW480, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.52×** | +9.0 | 1e-17 | 43/48 (H4, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.66×** | +7.7 | 4e-13 | 42/49 (PANC-1, KATO III, …) | all doses, flat | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.27×** | +7.3 | 1e-11 | 31/48 (SK-MEL-2, LOX-IMVI, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.89×** | +6.9 | 1e-10 | 43/49 (PANC-1, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8995.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (CFPAC-1 0.206×, AsPC-1 0.123×, NCI-H2347 0.334×, HT-29 0.295×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 6 lines (NCI-H2347 0.361×, Panc 03.27 0.282×, CFPAC-1 0.368×, HT-29 0.323×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (NCI-H2347 0.304×, CFPAC-1 0.307×; ⚠ toxic; transcription drop); [[XRK3F2 (drug)]] 0.5 µM in 1 line (CHP-212 0.0941×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.510×** | -14.5 | 1e-44 | 40/49 (NCI-H2347, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.540×** | -12.7 | 1e-34 | 34/44 (CFPAC-1, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.683×** | -7.6 | 5e-12 | 29/45 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.923× | -5.9 | 4e-07 | 0/50 | inconsistent across doses |  |
| [[Carbamazepine (drug)]] 5 µM |  | **0.830×** | -4.0 | 0.006 | 22/47 (AsPC-1, A498, …) | rises with dose |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | 0.811× | -3.2 | 0.12 | 14/48 (SK-MEL-2, COLO 205, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Filgotinib (drug)]] 0.05 µM |  | 0.866× | -3.1 | 0.15 | 13/48 (LOX-IMVI, SW480, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8995. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 146 | 13 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.00× (z +14.0) | [[Dinaciclib (drug)]] 0.5 µM 0.416× (z -11.2) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 86.1 | 14 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.15× (z +20.4) | — |
| [[SW480 (line)]] | alt | 150 | 12 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.99× (z +17.5) | [[Dinaciclib (drug)]] 0.5 µM 0.491× (z -11.5) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 151 | 9 (1 ⚠) | 4 (4 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.96× (z +15.1) | [[Dinaciclib (drug)]] 5 µM 0.358× (z -13.8) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 192 | 9 (1 ⚠) | 3 (3 ⚠) | [[Bortezomib (drug)]] 0.05 µM 3.20× (z +14.6) | [[Dinaciclib (drug)]] 0.05 µM 0.367× (z -12.4) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 62.0 | 11 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.76× (z +13.1) | — |
| [[PANC-1 (line)]] | alt | 76.4 | 11 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.29× (z +19.0) | — |
| [[LS 180 (line)]] | wt | 136 | 8 | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 3.81× (z +16.2) | [[Dinaciclib (drug)]] 5 µM 0.313× (z -13.5) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 95.8 | 9 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.90× (z +13.9) | — |
| [[C32 (line)]] | wt | 135 | 6 | 3 (3 ⚠) | [[Panobinostat (drug)]] 0.5 µM 4.00× (z +14.5) | [[Dinaciclib (drug)]] 0.5 µM 0.339× (z -11.2) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 172 | 3 | 6 (6 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.73× (z +12.8) | [[Dinaciclib (drug)]] 5 µM 0.206× (z -20.5) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 123 | 6 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +14.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Belinostat (drug)]] 5 µM 2.64× (z +12.3) | [[Dinaciclib (drug)]] 5 µM 0.419× (z -10.6) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 50.1 | 8 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 4.26× (z +16.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 94.4 | 8 | 0 | [[Panobinostat (drug)]] 5 µM 3.25× (z +13.5) | — |
| [[NCI-H23 (line)]] | alt | 109 | 7 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.87× (z +12.7) | [[Dinaciclib (drug)]] 0.5 µM 0.362× (z -12.2) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 178 | 7 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.62× (z +11.1) | [[Dinaciclib (drug)]] 0.5 µM 0.296× (z -10.5) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 99.7 | 6 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.45× (z +11.5) | [[Dinaciclib (drug)]] 0.5 µM 0.469× (z -9.7) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 105 | 5 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.19× (z +13.3) | [[Dinaciclib (drug)]] 5 µM 0.419× (z -9.6) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 94.1 | 5 | 2 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.70× (z +11.5) | [[Dinaciclib (drug)]] 5 µM 0.335× (z -12.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 53.0 | 6 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 4.14× (z +15.7) | — |
| [[COLO 205 (line)]] | alt | 237 | 3 | 3 (3 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 3.00× (z +12.1) | [[Dinaciclib (drug)]] 0.5 µM 0.303× (z -13.2) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 87.4 | 6 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.77× (z +12.8) | — |
| [[HT-29 (line)]] | alt | 192 | 4 | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 3.98× (z +16.3) | [[Dinaciclib (drug)]] 5 µM 0.295× (z -13.8) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 163 | 3 | 3 (3 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.33× (z +11.7) | [[Dinaciclib (drug)]] 0.05 µM 0.304× (z -15.4) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 106 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 3.37× (z +11.9) | — |
| [[J82 (line)]] | alt | 64.3 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.26× (z +11.5) | [[Dinaciclib (drug)]] 5 µM 0.401× (z -8.5) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 107 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.49× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.339× (z -10.4) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 123 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.69× (z +10.8) | [[Dinaciclib (drug)]] 0.5 µM 0.282× (z -13.8) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 139 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 3.16× (z +13.5) | — |
| [[SNU-423 (line)]] | alt | 78.3 | 5 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.75× (z +14.3) | — |
| [[HS-578T (line)]] | alt | 57.6 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.76× (z +13.0) | — |
| [[LOX-IMVI (line)]] | wt | 86.9 | 4 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.08× (z +11.6) | — |
| [[RPMI-7951 (line)]] | alt | 59.6 | 4 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.33× (z +9.9) | — |
| [[A549 (line)]] | wt | 97.1 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.34× (z +10.7) | — |
| [[C-33 A (line)]] | alt | 89.1 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.16× (z +11.1) | — |
| [[Hs 766T (line)]] | wt | 65.0 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.16× (z +13.3) | — |
| [[SNU-1 (line)]] | wt | 88.0 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.62× (z +11.3) | — |
| [[SW 900 (line)]] | alt | 113 | 3 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.71× (z +10.2) | — |
| [[SW1417 (line)]] | alt | 312 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.314× (z -13.2) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 1,084 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.123× (z -16.8) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 42.7 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 5.37× (z +9.8) | — |
| [[SHP-77 (line)]] | alt | 79.7 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.98× (z +11.4) | — |
| [[CHP-212 (line)]] | wt | 77.2 | 0 | 1 | — | [[XRK3F2 (drug)]] 0.5 µM 0.0941× (z -9.6) |
| [[HepG2_C3A (line)]] | wt | 127 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.80× (z +9.3) | — |
| [[AN3 CA (line)]] | alt | 167 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 198 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 148 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 142 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 84.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 103 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8995), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*57 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF277]] | +0.68 | +0.72 / +0.52 | both halves | 1e-05 |  |
| [[ILRUN]] | +0.66 | +0.76 / +0.38 | both halves | 6e-05 |  |
| [[CYRIB]] | +0.66 | +0.71 / +0.49 | both halves | 2e-05 |  |
| [[HDHD3]] | +0.64 | +0.64 / +0.50 | both halves | 1e-05 |  |
| [[STRN]] | +0.62 | +0.61 / +0.41 | both halves | 4e-05 |  |
| [[GRB2]] | +0.61 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[ATG5]] | +0.60 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[MCU]] | +0.60 | +0.56 / +0.46 | both halves | 3e-05 |  |
| [[SLC9A6]] | +0.60 | +0.58 / +0.42 | both halves | 4e-05 |  |
| [[CDC42SE2]] | +0.59 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[SEC11A]] | +0.59 | +0.62 / +0.39 | both halves | 6e-05 |  |
| [[SERAC1]] | +0.59 | +0.53 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*43 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLI]] | -0.66 | -0.66 / -0.64 | both halves | 7e-06 |  |
| [[PAN2]] | -0.63 | -0.63 / -0.39 | both halves | 5e-05 |  |
| [[KRBOX5]] | -0.62 | -0.63 / -0.42 | both halves | 4e-05 |  |
| [[ICE2]] | -0.61 | -0.62 / -0.44 | both halves | 3e-05 |  |
| [[PHF19]] | -0.61 | -0.69 / -0.36 | both halves | 1e-04 |  |
| [[CYB5D1]] | -0.60 | -0.60 / -0.52 | both halves | 1e-05 |  |
| [[MEPCE]] | -0.59 | -0.62 / -0.41 | both halves | 4e-05 |  |
| [[ST7L]] | -0.59 | -0.55 / -0.39 | both halves | 5e-05 |  |
| [[MYSM1]] | -0.58 | -0.51 / -0.46 | both halves | 2e-05 |  |
| [[COX18]] | -0.58 | -0.56 / -0.38 | both halves | 6e-05 |  |
| [[MTR]] | -0.58 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[MAGOHB]] | -0.58 | -0.55 / -0.46 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TTC22]] | B | TTC22 activity raises LMTK2's level | lines that do not express TTC22 (32) vs lines expressing it (18) | 1.97× lower at baseline in the lines without TTC22 | 0.015 | ⚠ within organs, on part of the lines; also absent: COL17A1, TRIM15, SERPINB5 |
| [[PLEKHH2]] | B | PLEKHH2 activity lowers LMTK2's level | lines that do not express PLEKHH2 (14) vs lines expressing it (36) | 1.74× higher at baseline in the lines without PLEKHH2 | 0.042 | ⚠ within organs, on part of the lines; also absent: PDLIM3, ENSG00000259363, AKT3 |
| [[GAMT]] | B | GAMT activity lowers LMTK2's level | lines that do not express GAMT (11) vs lines expressing it (39) | 1.88× higher at baseline in the lines without GAMT | 0.046 | ⚠ within organs, on part of the lines; co-occurs with APC; also absent: HDGFL3, HLTF, EHD3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 148]]; 30 genes; this gene is in the **-** arm (projection on the module's main direction -0.688). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-22.1, 18.7); signed map (-48.7, -8.2). **Vector** length 100, 33.6% of its response variance represented; |z| ≥ 3 in 1,437 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +7.7 | +17.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +7.4 | +16.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.9 | +15.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.7 | +7.3 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +5.2 | +7.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.6 | +7.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.8 | +6.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.6 | -0.7 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -11.1 | -2.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -9.9 | +2.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -7.7 | +1.9 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.0 | -1.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.3 | -1.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.5 | -2.2 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -1.4 | +1.1 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -1.4 | -0.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.4 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | lemur tail kinase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q21.3 — chr7:98,106,862-98,209,638 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1079, KPI2, KPI-2, cprk, LMR2, BREK, AATYK2, PPP1R100 |
| Gene groups (HGNC) | Protein phosphatase 1 regulatory subunits; Lemur tail kinase family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IWU2](https://www.uniprot.org/uniprotkb/Q8IWU2) (Serine/threonine-protein kinase LMTK2):

> Phosphorylates PPP1C, phosphorylase b and CFTR.

**Summary**, from NCBI Gene [22853](https://www.ncbi.nlm.nih.gov/gene/22853):

> The protein encoded by this gene belongs to the protein kinase superfamily and the protein tyrosine kinase family. It contains N-terminal transmembrane helices and a long C-terminal cytoplasmic tail with serine/threonine/tyrosine kinase activity. This protein interacts with several other proteins, such as Inhibitor-2 (Inh2), protein phosphatase-1 (PP1C), p35, and myosin VI. It phosporylates other proteins, and is itself also phosporylated when interacting with cyclin-dependent kinase 5 …

**Accessions** — [HGNC:17880](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17880) · Entrez [22853](https://www.ncbi.nlm.nih.gov/gene/22853) · UniProt [Q8IWU2](https://www.uniprot.org/uniprotkb/Q8IWU2) · Ensembl [ENSG00000164715](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164715)

## Data

Gene col 8995: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8995); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8995, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8995]; `tensor/DDL_lfc|DDL_z.npy` [8995]; `embed/gene_vectors.npy` [8995]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8995 or target_col == 8995). Every well: [[LMTK2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LMTK2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
