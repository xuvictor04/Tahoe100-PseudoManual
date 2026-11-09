---
symbol: "RAP1A"
type: "gene"
col: 3797
ensembl_id: "ENSG00000116473"
name: "RAP1A, member of RAS oncogene family"
location: "1p13.2"
module: 163
arm: "+"
pooled_cpm: 108.39
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 8
n_dd_up_clean: 12
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/163"]
generated_by: "tahoemap"
---

# RAP1A

*RAP1A, member of RAS oncogene family* — 1p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (1 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 1.71× (z +12.5, q 6e-33, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (6 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.681× (z -9.0, q 2e-16, down in 38 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Auranofin (drug)]] 5 µM in 6 lines (A-172 0.372×, SW480 0.518×, HEC-1-A 0.497×, SNU-423 0.459×, …); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (NCI-H23 0.300×, SHP-77 0.289×, NCI-H1573 0.415×, SNU-1 0.363×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 4 lines (NCI-H460 0.321×, RKO 0.398×, A-172 0.466×, J82 0.470×; ⚠ toxic; transcription drop); [[Oxaprozin (drug)]] 5 µM in 1 line (NCI-H596 0.0956×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CYTH3]] (+0.72, fdr 7e-06), [[ARL3]] (+0.72, fdr 7e-06), [[SEC11A]] (+0.71, fdr 1e-05); moves opposite to [[EIF2B5]] (-0.70, fdr 1e-05), [[ZNF24]] (-0.65, fdr 1e-05), [[AKT1S1]] (-0.64, fdr 8e-05).
> It is in [[Module 163]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3797.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **1.71×** | +12.5 | 6e-33 | 46/48 (PANC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.62×** | +11.3 | 4e-27 | 46/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.44×** | +10.9 | 2e-25 | 39/49 (SW480, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.50×** | +9.5 | 3e-19 | 43/48 (SK-MEL-2, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.49×** | +9.3 | 2e-18 | 38/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.78×** | +7.0 | 2e-10 | 32/48 (SW480, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.30×** | +6.1 | 8e-08 | 28/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.27×** | +5.5 | 3e-06 | 27/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.51×** | +5.0 | 3e-05 | 35/49 (PANC-1, RKO, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.23×** | +4.8 | 1e-04 | 25/48 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.21×** | +4.4 | 6e-04 | 21/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 1.20× | +4.1 | 0.002 | 19/47 (HCT15, PANC-1, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.12× | +3.5 | 0.022 | 9/49 (CFPAC-1, LoVo, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains <1% of this change | 1.16× | +3.4 | 0.023 | 17/48 (PANC-1, J82, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~21% of this change | 1.16× | +3.4 | 0.028 | 18/47 (NCI-H1573, Hs 766T, …) | top dose only |  |
| [[NVP-BHG712 (drug)]] 0.05 µM |  | 1.15× | +3.0 | 0.089 | 8/48 (A498, HOP62, …) | inconsistent across doses |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.28×** | +3.0 | 0.089 | 11/48 (NCI-H2347, RKO, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Tomivosertib (drug)]] 5 µM |  | **1.28×** | +3.0 | 0.090 | 13/48 (A549, NCI-H2030, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 7 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3797.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Auranofin (drug)]] 5 µM in 6 lines (A-172 0.372×, SW480 0.518×, HEC-1-A 0.497×, SNU-423 0.459×, …); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (NCI-H23 0.300×, SHP-77 0.289×, NCI-H1573 0.415×, SNU-1 0.363×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 4 lines (NCI-H460 0.321×, RKO 0.398×, A-172 0.466×, J82 0.470×; ⚠ toxic; transcription drop); [[Oxaprozin (drug)]] 5 µM in 1 line (NCI-H596 0.0956×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.681×** | -9.0 | 2e-16 | 38/48 (A-172, SW480, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.709×** | -7.4 | 3e-11 | 34/45 (NCI-H460, RKO, …) | all doses, flat | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.758×** | -6.5 | 2e-08 | 33/49 (NCI-H23, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~6% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~21% of this change | **0.806×** | -5.1 | 6e-05 | 25/48 (AsPC-1, RPMI-7951, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.806×** | -4.9 | 1e-04 | 22/44 (NCI-H1573, CHP-212, …) | all doses, flat | cell-cycle shift (explains ~5% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.819×** | -4.7 | 3e-04 | 25/48 (LoVo, NCI-H1792, …) | all doses, flat |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.867× | -4.5 | 6e-04 | 20/48 (A-172, A-427, …) | top dose only |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~9% of this change | **0.832×** | -4.3 | 0.001 | 22/48 (A498, Panc 03.27, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | 0.838× | -4.1 | 0.002 | 23/48 (LoVo, HS-578T, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.859× | -3.6 | 0.021 | 14/48 (H4, HS-578T, …) | all doses, flat |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.753×** | -3.5 | 0.028 | 18/47 (HS-578T, SK-MEL-2, …) | top dose only | noisy plate (z scaled) |
| [[Carbamazepine (drug)]] 5 µM |  | 0.864× | -3.4 | 0.031 | 16/47 (HEC-1-A, LOX-IMVI, …) | top dose only |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | 0.871× | -3.2 | 0.052 | 13/49 (LS 180, C-33 A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3797. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 110 | 8 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.34× (z +15.3) | [[Auranofin (drug)]] 5 µM 0.518× (z -11.8) |
| [[PANC-1 (line)]] | alt | 60.6 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.33× (z +14.1) | — |
| [[NCI-H460 (line)]] | wt | 74.0 | 3 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.25× (z +10.5) | [[Dinaciclib (drug)]] 0.05 µM 0.321× (z -13.5) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 114 | 0 | 3 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.372× (z -13.2) |
| [[AsPC-1 (line)]] | alt | 119 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.468× (z -9.1) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 86.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.415× (z -12.1) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 182 | 1 | 1 (1 ⚠) | [[Belinostat (drug)]] 5 µM 2.01× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.300× (z -16.6) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 123 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.363× (z -10.0) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 104 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 6.97× (z +8.8) | — |
| [[A-427 (line)]] | wt | 63.7 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.377× (z -9.9) ⚠ cell-cycle shift, explains ~17% of this change |
| [[AN3 CA (line)]] | alt | 133 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.280× (z -9.3) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 85.7 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.22× (z +8.7) | — |
| [[C32 (line)]] | wt | 117 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 4.87× (z +9.1) | — |
| [[CHP-212 (line)]] | wt | 75.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.128× (z -10.9) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 123 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.497× (z -9.5) |
| [[HOP62 (line)]] | alt | 97.6 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.487× (z -9.1) |
| [[J82 (line)]] | alt | 114 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.470× (z -9.4) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 94.6 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.95× (z +8.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 118 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.29× (z +9.1) | — |
| [[NCI-H2347 (line)]] | alt | 165 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.516× (z -8.7) ⚠ toxic; transcription drop |
| [[NCI-H596 (line)]] | alt | 112 | 0 | 1 | — | [[Oxaprozin (drug)]] 5 µM 0.0956× (z -10.8) |
| [[RKO (line)]] | wt | 129 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.398× (z -9.8) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 93.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.289× (z -14.1) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 215 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 1.99× (z +9.3) | — |
| [[SNU-423 (line)]] | alt | 125 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.459× (z -9.3) |
| [[SW 900 (line)]] | alt | 85.9 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.448× (z -8.5) |
| [[SW1417 (line)]] | alt | 102 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.02× (z +8.7) | — |
| [[A498 (line)]] | wt | 86.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 67.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 113 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 61.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 91.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 88.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 120 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 189 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 96.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 121 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 112 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 108 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 102 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 95.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 138 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 126 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 186 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 92.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3797), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CYTH3]] | +0.72 | +0.74 / +0.61 | both halves | 7e-06 |  |
| [[ARL3]] | +0.72 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[SEC11A]] | +0.71 | +0.77 / +0.51 | both halves | 1e-05 |  |
| [[FLYWCH2]] | +0.70 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[PPP1R2]] | +0.70 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[METRN]] | +0.69 | +0.61 / +0.47 | both halves | 2e-05 |  |
| [[ABHD12]] | +0.69 | +0.66 / +0.61 | both halves | 7e-06 | pathway: Platelet activation, signaling and aggregation |
| [[SLC9A6]] | +0.68 | +0.75 / +0.41 | both halves | 4e-05 |  |
| [[SDHAP2]] | +0.68 | +0.75 / +0.45 | both halves | 3e-05 |  |
| [[RNF38]] | +0.67 | +0.71 / +0.61 | both halves | 7e-06 |  |
| [[OSTF1]] | +0.66 | +0.61 / +0.57 | both halves | 8e-06 |  |
| [[GNB2]] | +0.66 | +0.64 / +0.42 | both halves | 4e-05 | pathway: Glucagon-like Peptide-1 (GLP1) regulates insulin secretion |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF2B5]] | -0.70 | -0.75 / -0.55 | both halves | 1e-05 |  |
| [[ZNF24]] | -0.65 | -0.65 / -0.52 | both halves | 1e-05 |  |
| [[AKT1S1]] | -0.64 | -0.74 / -0.37 | both halves | 8e-05 |  |
| [[CYREN]] | -0.63 | -0.74 / -0.37 | both halves | 9e-05 |  |
| [[SRSF6]] | -0.63 | -0.62 / -0.46 | both halves | 2e-05 |  |
| [[ST7L]] | -0.62 | -0.68 / -0.37 | both halves | 8e-05 |  |
| [[ZXDB]] | -0.61 | -0.56 / -0.43 | both halves | 3e-05 |  |
| [[SNAPC5]] | -0.61 | -0.74 / -0.31 | both halves | 2e-04 |  |
| [[ZNF564]] | -0.61 | -0.63 / -0.33 | both halves | 1e-04 |  |
| [[ZNF507]] | -0.61 | -0.64 / -0.41 | both halves | 4e-05 |  |
| [[TTC6]] | -0.61 | -0.60 / -0.43 | both halves | 3e-05 |  |
| [[SON]] | -0.61 | -0.60 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 163]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.757). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.53; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (3.5, -12.3); signed map (-38.1, -0.7). **Vector** length 109, 32.4% of its response variance represented; |z| ≥ 3 in 986 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +6.5 | +12.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.5 | +9.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.2 | +11.3 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains <1% of this change | +4.2 | +3.4 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.1 | +4.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.9 | +5.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +2.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.3 | +3.5 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.6 | +2.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.2 | +0.9 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | -10.0 | -4.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -8.8 | -2.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -8.3 | -9.0 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | -4.9 | -4.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.7 | -1.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.1 | -4.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.6 | -3.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.8 | +0.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.3 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | RAP1A, member of RAS oncogene family |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p13.2 — chr1:111,542,218-111,716,691 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KREV-1, SMGP21 |
| Gene groups (HGNC) | RAS type GTPase family |
| Reactome | 36 pathways, smallest: ARMS-mediated activation; MET activates RAP1 and RAC1; Frs2-mediated activation |
| Matched by | ensembl_id |

**Function**, from UniProt [P62834](https://www.uniprot.org/uniprotkb/P62834) (Ras-related protein Rap-1A):

> Counteracts the mitogenic function of Ras, at least partly because it can interact with Ras GAPs and RAF in a competitive manner. Together with ITGB1BP1, regulates KRIT1 localization to microtubules and membranes. Plays a role in nerve growth factor (NGF)-induced neurite outgrowth. Plays a role in the regulation of embryonic blood vessel formation. Involved in the establishment of basal endothelial barrier function. Facilitates the progressive accumulation of CDH1 at mature desmosome junctions …

**Summary**, from NCBI Gene [5906](https://www.ncbi.nlm.nih.gov/gene/5906):

> This gene encodes a member of the Ras family of small GTPases. The encoded protein undergoes a change in conformational state and activity, depending on whether it is bound to GTP or GDP. This protein is activated by several types of guanine nucleotide exchange factors (GEFs), and inactivated by two groups of GTPase-activating proteins (GAPs). The activation status of the encoded protein is therefore affected by the balance of intracellular levels of GEFs and GAPs. The encoded protein regulates …

**Accessions** — [HGNC:9855](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9855) · Entrez [5906](https://www.ncbi.nlm.nih.gov/gene/5906) · UniProt [P62834](https://www.uniprot.org/uniprotkb/P62834) · Ensembl [ENSG00000116473](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116473)

## Data

Gene col 3797: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3797); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3797, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3797]; `tensor/DDL_lfc|DDL_z.npy` [3797]; `embed/gene_vectors.npy` [3797]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3797 or target_col == 3797). Every well: [[RAP1A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RAP1A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
