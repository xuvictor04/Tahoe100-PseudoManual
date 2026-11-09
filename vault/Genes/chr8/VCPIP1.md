---
symbol: "VCPIP1"
type: "gene"
col: 10559
ensembl_id: "ENSG00000175073"
name: "valosin containing protein interacting protein 1"
location: "8q13.1"
module: 7
arm: "+"
pooled_cpm: 59.59
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 9
n_dd_up_clean: 14
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# VCPIP1

*valosin containing protein interacting protein 1* — 8q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.91× (z +19.5, q 0e+00, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.549× (z -12.8, q 1e-34, down in 40 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.859× (z -4.6, q 6e-04, down in 20 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZBTB6]] (+0.75, fdr 7e-06), [[CBLL1]] (+0.72, fdr 7e-06), [[ZNF543]] (+0.71, fdr 7e-06).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10559.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.91×** | +19.5 | 0e+00 | 43/48 (C32, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.01×** | +14.9 | 0e+00 | 44/47 (C32, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.84×** | +12.9 | 6e-36 | 43/48 (RKO, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **3.48×** | +12.1 | 2e-31 | 45/49 (SW480, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.71×** | +10.0 | 3e-21 | 40/48 (C32, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.46×** | +8.0 | 1e-13 | 36/48 (C32, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.09×** | +7.2 | 7e-11 | 27/48 (C32, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.39×** | +6.5 | 5e-09 | 30/47 (LS 180, NCI-H2347, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.24×** | +6.4 | 8e-09 | 27/48 (J82, RPMI-7951, …) | rises with dose | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.29×** | +5.3 | 5e-06 | 22/48 (LoVo, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.23×** | +4.4 | 7e-04 | 20/48 (NCI-H1573, A-427, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.22×** | +4.2 | 0.001 | 19/48 (PANC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.54×** | +4.2 | 0.001 | 18/49 (LoVo, BT-474, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 5 µM |  | **1.41×** | +3.3 | 0.040 | 7/49 (J82, HS-578T, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **1.40×** | +3.3 | 0.040 | 11/49 (HS-578T, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.16× | +3.2 | 0.056 | 11/48 (KATO III, NCI-H2030, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10559.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.549×** | -12.8 | 1e-34 | 40/49 (KATO III, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~23% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.660×** | -8.2 | 8e-14 | 29/45 (RPMI-7951, A498, …) | all doses, flat | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.681×** | -7.2 | 1e-10 | 25/40 (LOX-IMVI, A498, …) | all doses, flat | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | 0.859× | -4.6 | 6e-04 | 20/48 (H4, SW480, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.808×** | -4.5 | 6e-04 | 18/48 (SW 1088, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.799×** | -4.2 | 0.003 | 23/48 (NCI-H1792, PANC-1, …) | top dose only |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **0.774×** | -3.9 | 0.007 | 18/48 (Hs 766T, BT-474, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.774×** | -3.9 | 0.007 | 19/48 (LoVo, PANC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 0.5 µM |  | **0.776×** | -3.9 | 0.007 | 19/48 (SNU-1, RPMI-7951, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.689×** | -3.6 | 0.018 | 18/48 (CFPAC-1, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.05 µM |  | 0.858× | -3.1 | 0.10 | 14/48 (hTERT-HPNE, A-172, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | 0.904× | -3.0 | 0.10 | 8/48 (RKO, SNU-1, …) | top dose only |  |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 0.867× | -3.0 | 0.10 | 13/47 (NCI-H661, Hs 766T, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | 0.820× | -3.0 | 0.10 | 14/48 (HCT15, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10559. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 74.3 | 6 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.42× (z +21.0) | [[Dinaciclib (drug)]] 0.05 µM 0.313× (z -10.7) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 93.7 | 5 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +13.4) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.203× (z -15.8) ⚠ toxic; cell-cycle shift, explains ~27% of this change |
| [[A498 (line)]] | wt | 113 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +15.8) | [[Dinaciclib (drug)]] 0.5 µM 0.297× (z -17.1) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 84.1 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +14.2) | [[Dinaciclib (drug)]] 0.5 µM 0.391× (z -10.2) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 81.2 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.34× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.172× (z -16.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[LS 180 (line)]] | wt | 37.9 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +9.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 46.6 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +10.9) | [[Dinaciclib (drug)]] 0.5 µM 0.274× (z -11.4) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 38.6 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +15.6) | — |
| [[PANC-1 (line)]] | alt | 63.0 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.69× (z +10.4) | [[Dinaciclib (drug)]] 0.05 µM 0.490× (z -9.3) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 56.4 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +13.5) | [[Dinaciclib (drug)]] 0.5 µM 0.402× (z -8.7) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 58.3 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +12.0) | [[Dinaciclib (drug)]] 0.5 µM 0.500× (z -8.8) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 53.3 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.77× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.318× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[HOP62 (line)]] | alt | 63.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +15.4) | — |
| [[hTERT-HPNE (line)]] | wt | 60.3 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +12.0) | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.324× (z -9.3) |
| [[NCI-H1792 (line)]] | alt | 58.4 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +12.5) | [[Dinaciclib (drug)]] 5 µM 0.283× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[NCI-H2347 (line)]] | alt | 49.0 | 3 | 0 | [[Harringtonine (drug)]] 0.5 µM 2.41× (z +10.2) | — |
| [[RPMI-7951 (line)]] | alt | 92.2 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +10.1) | [[Dinaciclib (drug)]] 0.05 µM 0.173× (z -16.9) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 75.4 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +9.8) | [[Dinaciclib (drug)]] 0.05 µM 0.296× (z -11.2) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 62.8 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +14.8) | [[Dinaciclib (drug)]] 0.5 µM 0.422× (z -8.7) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 39.9 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +13.0) | [[Lonafarnib (drug)]] 5 µM 0.0618× (z -12.7) ⚠ toxic |
| [[A549 (line)]] | wt | 57.1 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +11.1) | [[Dinaciclib (drug)]] 0.5 µM 0.428× (z -8.5) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 46.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +9.0) | [[Dinaciclib (drug)]] 0.05 µM 0.159× (z -15.3) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 79.7 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 9.30× (z +8.9) | [[Dinaciclib (drug)]] 0.5 µM 0.115× (z -19.0) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 45.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +11.5) | [[Dinaciclib (drug)]] 0.5 µM 0.248× (z -16.3) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 54.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +11.6) | — |
| [[J82 (line)]] | alt | 62.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +15.9) | — |
| [[LoVo (line)]] | wt | 51.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.77× (z +10.0) | — |
| [[NCI-H23 (line)]] | alt | 51.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +9.5) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.325× (z -10.1) ⚠ cell-cycle shift, explains ~57% of this change |
| [[CHP-212 (line)]] | wt | 75.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.150× (z -10.5) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 66.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.370× (z -8.5) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 50.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.275× (z -9.1) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 73.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +11.5) | — |
| [[KATO III (line)]] | alt | 71.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.171× (z -20.0) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 61.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.411× (z -9.1) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 57.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +10.2) | — |
| [[SW 1271 (line)]] | alt | 85.7 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.130× (z -9.3) |
| [[SW 900 (line)]] | alt | 83.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.376× (z -9.9) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 40.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +10.5) | — |
| [[SW48 (line)]] | wt | 42.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.231× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[A-427 (line)]] | wt | 35.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 47.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 70.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 44.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 67.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 54.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 54.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 41.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 49.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10559), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZBTB6]] | +0.75 | +0.76 / +0.68 | both halves | 7e-06 |  |
| [[CBLL1]] | +0.72 | +0.73 / +0.67 | both halves | 7e-06 |  |
| [[ZNF543]] | +0.71 | +0.74 / +0.67 | both halves | 7e-06 |  |
| [[ZBED9]] | +0.70 | +0.69 / +0.64 | both halves | 7e-06 |  |
| [[ZNF426]] | +0.70 | +0.75 / +0.62 | both halves | 7e-06 |  |
| [[ZNF845]] | +0.69 | +0.70 / +0.64 | both halves | 7e-06 |  |
| [[ZNF646]] | +0.69 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[FAM200A]] | +0.69 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[SMG8]] | +0.69 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[EXOC8]] | +0.67 | +0.70 / +0.60 | both halves | 7e-06 | STRING 453 |
| [[ZNF155]] | +0.67 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[RIMOC1]] | +0.66 | +0.67 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.703). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-36.2, 10.2); signed map (-0.8, -26.1). **Vector** length 104, 27.2% of its response variance represented; |z| ≥ 3 in 1,064 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +10.5 | +12.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +9.0 | +14.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +8.2 | +8.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | +7.0 | +10.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | +5.9 | +6.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +4.8 | +6.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.8 | +7.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.8 | +3.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +2.1 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.1 | -4.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -4.4 | -12.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | -3.6 | -7.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -3.4 | -4.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.2 | -1.4 |
|  | [[venetoclax (drug)]] 5 µM |  | -2.8 | -3.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.8 | -3.0 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -2.7 | -3.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.2 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | valosin containing protein interacting protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q13.1 — chr8:66,628,487-66,667,231 (-) |
| Ensembl biotype | protein_coding |
| Also known as | VCIP135, KIAA1850, FLJ23132, DUBA3 |
| Gene groups (HGNC) | OTU domain containing |
| Hallmark sets | COMPLEMENT |
| Reactome | 2 pathways, smallest: Ovarian tumor domain proteases; Deubiquitination |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96JH7](https://www.uniprot.org/uniprotkb/Q96JH7) (Deubiquitinating protein VCPIP1):

> Deubiquitinating enzyme involved in DNA repair and reassembly of the Golgi apparatus and the endoplasmic reticulum following mitosis. Necessary for VCP-mediated reassembly of Golgi stacks after mitosis (By similarity). Plays a role in VCP-mediated formation of transitional endoplasmic reticulum (tER) (By similarity). Mediates dissociation of the ternary complex containing STX5A, NSFL1C and VCP (By similarity). Also involved in DNA repair following phosphorylation by ATM or ATR: acts by …

**Summary**, from NCBI Gene [80124](https://www.ncbi.nlm.nih.gov/gene/80124):

> Enables cysteine-type deubiquitinase activity. Involved in protein deubiquitination; protein-DNA covalent cross-linking repair; and regulation of protein localization to chromatin. Located in cytosol and nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:30897](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30897) · Entrez [80124](https://www.ncbi.nlm.nih.gov/gene/80124) · UniProt [Q96JH7](https://www.uniprot.org/uniprotkb/Q96JH7) · Ensembl [ENSG00000175073](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175073)

## Data

Gene col 10559: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10559); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10559, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10559]; `tensor/DDL_lfc|DDL_z.npy` [10559]; `embed/gene_vectors.npy` [10559]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10559 or target_col == 10559). Every well: [[VCPIP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VCPIP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
