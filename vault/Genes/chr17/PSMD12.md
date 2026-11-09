---
symbol: "PSMD12"
type: "gene"
col: 12360
ensembl_id: "ENSG00000197170"
name: "proteasome 26S subunit, non-ATPase 12"
location: "17q24.2"
module: 60
arm: "+"
pooled_cpm: 120.74
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 2
n_dd_up_clean: 8
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/060"]
generated_by: "tahoemap"
---

# PSMD12

*proteasome 26S subunit, non-ATPase 12* — 17q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (11 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 3.29× (z +30.0, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Binimetinib (drug)]] 0.05 µM: 0.844× (z -5.9, q 2e-06, down in 23 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (RKO 0.566×, CHP-212 0.440×, SW 900 0.626×; ⚠ cell-cycle shift, explains ~0% of this change); [[Methylthiouracil (drug)]] 5 µM in 1 line (NCI-H596 0.113×); [[Adagrasib (drug)]] 0.05 µM in 1 line (NCI-H23 0.815×; ⚠ position not correctable); [[Rifaximin (drug)]] 0.05 µM in 1 line (SW 1088 0.0703×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NUDC]] (+0.72, fdr 7e-06), [[UTP11]] (+0.72, fdr 7e-06), [[GPN1]] (+0.70, fdr 7e-06); moves opposite to [[GPX4]] (-0.64, fdr 7e-06), [[DPM3]] (-0.61, fdr 7e-06), [[PHPT1]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 060]] (heat shock).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 15 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12360.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **3.29×** | +30.0 | 0e+00 | 48/48 (SW480, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.86×** | +26.4 | 0e+00 | 48/48 (SW480, HT-29, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.84×** | +24.8 | 0e+00 | 48/48 (SW480, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.47×** | +22.8 | 0e+00 | 48/48 (SW480, C32, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **4.02×** | +14.2 | 6e-44 | 48/49 (LoVo, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **2.04×** | +12.3 | 1e-32 | 48/49 (LOX-IMVI, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.65×** | +11.5 | 2e-28 | 39/48 (LOX-IMVI, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.38×** | +11.4 | 4e-28 | 32/48 (LOX-IMVI, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.89×** | +10.9 | 8e-26 | 44/45 (LOX-IMVI, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.76×** | +10.4 | 2e-23 | 45/48 (HEC-1-A, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | **1.49×** | +10.0 | 8e-22 | 33/49 (SW480, LOX-IMVI, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.37×** | +7.9 | 1e-13 | 37/48 (SW480, HOP62, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | **1.38×** | +7.8 | 3e-13 | 29/44 (SNU-423, SW480, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **1.39×** | +7.6 | 8e-13 | 33/45 (NCI-H23, SW480, …) | all doses, flat | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.19× | +6.1 | 5e-08 | 17/48 (MIA PaCa-2, Hs 766T, …) | top dose only |  |
| [[Mebendazole (drug)]] 5 µM |  | 1.15× | +3.5 | 0.012 | 7/48 (MIA PaCa-2, HOP62, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.09× | +3.1 | 0.036 | 5/49 (MIA PaCa-2, HT-29, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12360.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (RKO 0.566×, CHP-212 0.440×, SW 900 0.626×; ⚠ cell-cycle shift, explains ~0% of this change); [[Methylthiouracil (drug)]] 5 µM in 1 line (NCI-H596 0.113×); [[Adagrasib (drug)]] 0.05 µM in 1 line (NCI-H23 0.815×; ⚠ position not correctable); [[Rifaximin (drug)]] 0.05 µM in 1 line (SW 1088 0.0703×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Binimetinib (drug)]] 0.05 µM |  | 0.844× | -5.9 | 2e-06 | 23/49 (NCI-H460, SW480, …) | all doses, flat |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.751×** | -4.9 | 2e-04 | 31/48 (LoVo, HOP62, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 0.840× | -4.9 | 2e-04 | 23/48 (RKO, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.821×** | -4.8 | 2e-04 | 26/47 (NCI-H460, HepG2/C3A, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.880× | -4.6 | 6e-04 | 18/48 (A498, CFPAC-1, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.880× | -4.4 | 9e-04 | 10/48 (NCI-H23, LoVo, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | 0.838× | -4.3 | 0.002 | 19/50 (LoVo, RKO, …) | all doses, flat | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | 0.849× | -4.1 | 0.003 | 15/48 (LoVo, RKO, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.877× | -4.0 | 0.004 | 14/48 (NCI-H460, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | 0.841× | -4.0 | 0.004 | 20/49 (KATO III, SNU-423, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | 0.849× | -3.9 | 0.005 | 18/49 (LoVo, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.857× | -3.9 | 0.005 | 17/47 (LoVo, RKO, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.05 µM |  | 0.847× | -3.9 | 0.005 | 17/47 (AN3 CA, A549, …) | all doses, flat |  |
| [[Entrectinib (drug)]] 5 µM |  | 0.867× | -3.6 | 0.013 | 15/48 (KATO III, HepG2/C3A, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.873× | -3.4 | 0.022 | 17/49 (LoVo, NCI-H23, …) | two highest doses |  |
| [[Posaconazole (drug)]] 5 µM |  | 0.881× | -3.1 | 0.071 | 8/48 (COLO 205, NCI-H661, …) | top dose only | plate-row cell shift |
| [[Thymol (drug)]] 0.5 µM |  | 0.879× | -3.0 | 0.092 | 13/48 (H4, SHP-77, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12360. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 144 | 17 (9 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.01× (z +23.6) | — |
| [[LOX-IMVI (line)]] | wt | 88.8 | 12 (5 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 5.29× (z +23.0) | — |
| [[HOP62 (line)]] | alt | 120 | 10 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +18.1) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 3.83× (z +17.8) | — |
| [[KATO III (line)]] | alt | 142 | 8 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.52× (z +20.9) | — |
| [[NCI-H23 (line)]] | alt | 166 | 8 (3 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.80× (z +13.5) | — |
| [[SNU-423 (line)]] | alt | 119 | 8 (3 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.03× (z +19.0) | — |
| [[HEC-1-A (line)]] | alt | 132 | 7 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.84× (z +19.8) | — |
| [[HS-578T (line)]] | alt | 97.1 | 7 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.19× (z +13.2) | — |
| [[LoVo (line)]] | wt | 110 | 7 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.43× (z +20.2) | — |
| [[SK-MEL-2 (line)]] | alt | 156 | 7 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.99× (z +14.4) | — |
| [[hTERT-HPNE (line)]] | wt | 117 | 5 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 4.26× (z +16.6) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.461× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 118 | 6 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.34× (z +14.9) | — |
| [[NCI-H1573 (line)]] | alt | 83.5 | 6 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.64× (z +18.5) | — |
| [[PANC-1 (line)]] | alt | 82.8 | 6 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.23× (z +17.7) | — |
| [[SW48 (line)]] | wt | 121 | 6 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.74× (z +13.2) | — |
| [[AsPC-1 (line)]] | alt | 97.2 | 5 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.84× (z +13.1) | — |
| [[CFPAC-1 (line)]] | alt | 138 | 5 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.29× (z +17.3) | — |
| [[LS 180 (line)]] | wt | 106 | 5 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.92× (z +17.1) | — |
| [[NCI-H1792 (line)]] | alt | 105 | 5 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.30× (z +14.5) | — |
| [[Panc 03.27 (line)]] | alt | 121 | 5 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.62× (z +16.3) | — |
| [[A-172 (line)]] | wt | 104 | 4 | 0 | [[Auranofin (drug)]] 5 µM 3.59× (z +17.0) | — |
| [[A-427 (line)]] | wt | 143 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.98× (z +14.0) | — |
| [[A498 (line)]] | wt | 141 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.16× (z +12.8) | — |
| [[A549 (line)]] | wt | 130 | 4 (1 ⚠) | 0 | [[Bortezomib (drug)]] 0.05 µM 3.15× (z +14.0) | — |
| [[BT-474 (line)]] | alt | 149 | 4 | 0 | [[Auranofin (drug)]] 5 µM 4.74× (z +19.7) | — |
| [[C32 (line)]] | wt | 94.9 | 4 | 0 | [[Auranofin (drug)]] 5 µM 6.43× (z +20.5) | — |
| [[COLO 205 (line)]] | alt | 103 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 5.79× (z +17.8) | — |
| [[H4 (line)]] | wt | 144 | 4 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.94× (z +13.6) | — |
| [[HCT15 (line)]] | alt | 141 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.30× (z +11.7) | — |
| [[HepG2_C3A (line)]] | wt | 144 | 4 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.93× (z +11.9) | — |
| [[Hs 766T (line)]] | wt | 75.7 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.64× (z +13.2) | — |
| [[HT-29 (line)]] | alt | 187 | 4 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.84× (z +20.9) | — |
| [[NCI-H2347 (line)]] | alt | 116 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.99× (z +15.2) | — |
| [[NCI-H460 (line)]] | wt | 119 | 4 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.27× (z +18.0) | — |
| [[RKO (line)]] | wt | 170 | 3 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.22× (z +9.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.566× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 99.6 | 4 | 0 | [[Auranofin (drug)]] 5 µM 2.79× (z +11.6) | — |
| [[SNU-1 (line)]] | wt | 98.2 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.20× (z +10.2) | — |
| [[SW 900 (line)]] | alt | 159 | 3 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.47× (z +11.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.626× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 116 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.82× (z +13.3) | — |
| [[C-33 A (line)]] | alt | 127 | 3 | 0 | [[Auranofin (drug)]] 5 µM 3.58× (z +13.3) | — |
| [[J82 (line)]] | alt | 128 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.02× (z +10.1) | — |
| [[NCI-H2030 (line)]] | alt | 91.0 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.49× (z +14.5) | — |
| [[RPMI-7951 (line)]] | alt | 106 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.38× (z +12.5) | — |
| [[CHP-212 (line)]] | wt | 220 | 1 | 1 (1 ⚠) | [[Bortezomib (drug)]] 0.05 µM 3.21× (z +9.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.440× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 101 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.07× (z +9.2) | — |
| [[NCI-H596 (line)]] | alt | 113 | 0 | 1 | — | [[Methylthiouracil (drug)]] 5 µM 0.113× (z -15.3) |
| [[SW 1088 (line)]] | alt | 82.7 | 0 | 1 | — | [[Rifaximin (drug)]] 0.05 µM 0.0703× (z -9.0) |
| [[NCI-H2122 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 108 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12360), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUDC]] | +0.72 | +0.70 / +0.72 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints |
| [[UTP11]] | +0.72 | +0.70 / +0.67 | both halves | 7e-06 |  |
| [[GPN1]] | +0.70 | +0.60 / +0.76 | both halves | 7e-06 |  |
| [[CCT2]] | +0.69 | +0.68 / +0.71 | both halves | 7e-06 | STRING 655 |
| [[VCP]] | +0.68 | +0.65 / +0.68 | both halves | 7e-06 | pathway: ABC transporter disorders; STRING 807 |
| [[CCT6A]] | +0.68 | +0.66 / +0.67 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING; STRING 534 |
| [[STIP1]] | +0.67 | +0.62 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING |
| [[API5]] | +0.66 | +0.71 / +0.66 | both halves | 7e-06 |  |
| [[LSG1]] | +0.66 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[TCP1]] | +0.65 | +0.63 / +0.70 | both halves | 7e-06 | STRING 619 |
| [[GTF3C3]] | +0.65 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[PSMC3]] | +0.65 | +0.69 / +0.60 | both halves | 7e-06 | same gene group; pathway: ABC transporter disorders; STRING 999 |

## Genes that move opposite

*28 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPX4]] | -0.64 | -0.59 / -0.64 | both halves | 7e-06 |  |
| [[DPM3]] | -0.61 | -0.58 / -0.59 | both halves | 7e-06 |  |
| [[PHPT1]] | -0.61 | -0.56 / -0.58 | both halves | 1e-05 |  |
| [[GABARAP]] ⚠ | -0.59 | -0.62 / -0.51 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[VEGFB]] | -0.59 | -0.59 / -0.52 | both halves | 1e-05 |  |
| [[TBC1D12]] | -0.58 | -0.47 / -0.60 | both halves | 2e-05 |  |
| [[CNNM2]] | -0.58 | -0.62 / -0.50 | both halves | 1e-05 |  |
| [[SAP30]] | -0.58 | -0.54 / -0.57 | both halves | 1e-05 |  |
| [[LCORL]] | -0.58 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[SNHG9]] | -0.57 | -0.52 / -0.58 | both halves | 1e-05 |  |
| [[CUTA]] | -0.56 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[TXNDC16]] | -0.56 | -0.54 / -0.45 | both halves | 3e-05 |  |
| [[HABP4]] | -0.56 | -0.55 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 060]] — heat shock; 78 genes; this gene is in the **+** arm (projection on the module's main direction 0.629). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-21.5, -12.2); signed map (-27.9, -29.2). **Vector** length 113, 37.9% of its response variance represented; |z| ≥ 3 in 1,358 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Formation of tubulin folding intermediates by CCT/TriC* (reactome, mean cos +0.52 to 5); *Prefoldin mediated transfer of substrate  to CCT/TriC* (reactome, mean cos +0.52 to 5); *Folding of actin by CCT/TriC* (reactome, mean cos +0.64 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +10.2 | +30.0 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +10.0 | +24.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +9.9 | +22.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +9.5 | +26.4 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +6.0 | +10.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.0 | +6.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.7 | +12.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.9 | +2.4 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change | -7.0 | +4.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~81% of this change | -5.9 | +3.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | -5.5 | +7.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | -5.1 | +4.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.1 | +2.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.0 | -3.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.9 | -2.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.6 | -4.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.6 | -4.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.5 | -4.6 |

## What is on record

|  |  |
|---|---|
| Name | proteasome 26S subunit, non-ATPase 12 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q24.2 — chr17:67,337,916-67,366,605 (-) |
| Ensembl biotype | protein_coding |
| Also known as | p55, Rpn5 |
| Gene groups (HGNC) | Proteasome |
| Hallmark sets | MTORC1_SIGNALING |
| Reactome | 170 pathways, smallest: Regulation of activated PAK-2p34 by proteasome mediated degradation; Regulation of ornithine decarboxylase (ODC); Cross-presentation of soluble exogenous antigens (endosomes) |
| Matched by | ensembl_id |

**Function**, from UniProt [O00232](https://www.uniprot.org/uniprotkb/O00232) (26S proteasome non-ATPase regulatory subunit 12):

> Component of the 26S proteasome, a multiprotein complex involved in the ATP-dependent degradation of ubiquitinated proteins. This complex plays a key role in the maintenance of protein homeostasis by removing misfolded or damaged proteins, which could impair cellular functions, and by removing proteins whose functions are no longer required. Therefore, the proteasome participates in numerous cellular processes, including cell cycle progression, apoptosis, or DNA damage repair.

**Summary**, from NCBI Gene [5718](https://www.ncbi.nlm.nih.gov/gene/5718):

> The 26S proteasome is a multicatalytic proteinase complex with a highly ordered structure composed of 2 complexes, a 20S core and a 19S regulator. The 20S core is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. The 19S regulator is composed of a base, which contains 6 ATPase subunits and 2 non-ATPase subunits, and a lid, which contains up to 10 non-ATPase subunits. Proteasomes are distributed throughout …

**Accessions** — [HGNC:9557](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9557) · Entrez [5718](https://www.ncbi.nlm.nih.gov/gene/5718) · UniProt [O00232](https://www.uniprot.org/uniprotkb/O00232) · Ensembl [ENSG00000197170](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197170)

## Data

Gene col 12360: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12360); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12360, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12360]; `tensor/DDL_lfc|DDL_z.npy` [12360]; `embed/gene_vectors.npy` [12360]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12360 or target_col == 12360). Every well: [[PSMD12 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PSMD12.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
