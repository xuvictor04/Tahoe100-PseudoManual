---
symbol: "ATP6V0A1"
type: "gene"
col: 416
ensembl_id: "ENSG00000033627"
name: "ATPase H+ transporting V0 subunit a1"
location: "17q21.2"
module: 125
arm: "+"
pooled_cpm: 83.69
n_lines_expressing: 50
n_dd_up: 27
n_dd_down: 3
n_dd_up_clean: 24
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/125"]
generated_by: "tahoemap"
---

# ATP6V0A1

*ATPase H+ transporting V0 subunit a1* — 17q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.29× (z +27.0, q 0e+00, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.731× (z -6.9, q 2e-09, down in 26 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Budesonide (drug)]] 0.5 µM: 0.831× (z -4.3, q 0.002, down in 19 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (HCT15 0.215×, SNU-1 0.259×, A-427 0.381×, HEC-1-A 0.468×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 4 lines (A549 0.187×, LoVo 0.280×, NCI-H23 0.339×, NCI-H2030 0.400×; ⚠ toxic; transcription drop); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (NCI-H661 0.0686×); [[Homoharringtonine (drug)]] 5 µM in 1 line (C32 0.489×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPLP0P2]] (+0.58, fdr 3e-05), [[OLFM2]] (+0.57, fdr 4e-05), [[SYP]] (+0.56, fdr 3e-05); moves opposite to [[POLE3]] (-0.57, fdr 1e-05), [[TDRD3]] (-0.55, fdr 2e-05), [[MCMBP]] (-0.50, fdr 2e-05).
> It is in [[Module 125]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[RPLP0P2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 7 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 416.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.29×** | +27.0 | 0e+00 | 43/48 (HOP62, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.72×** | +23.0 | 0e+00 | 47/48 (KATO III, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.62×** | +22.1 | 0e+00 | 47/48 (HOP62, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.54×** | +21.4 | 0e+00 | 47/48 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **2.50×** | +21.0 | 0e+00 | 48/48 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.18×** | +17.2 | 0e+00 | 43/48 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.64×** | +16.1 | 0e+00 | 43/48 (HOP62, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.91×** | +14.8 | 0e+00 | 46/48 (NCI-H1573, COLO 205, …) | two highest doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.88×** | +14.5 | 1e-45 | 43/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.87×** | +14.3 | 8e-45 | 35/48 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.73×** | +12.6 | 2e-34 | 43/48 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.72×** | +12.5 | 4e-34 | 43/48 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.64×** | +11.4 | 3e-28 | 43/48 (HOP62, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.64×** | +11.3 | 4e-28 | 44/48 (COLO 205, PANC-1, …) | two highest doses | cell-cycle shift (explains ~6% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.59×** | +10.6 | 1e-24 | 39/48 (RKO, HT-29, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.59×** | +10.6 | 1e-24 | 38/49 (HOP62, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 6 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 416.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (HCT15 0.215×, SNU-1 0.259×, A-427 0.381×, HEC-1-A 0.468×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 4 lines (A549 0.187×, LoVo 0.280×, NCI-H23 0.339×, NCI-H2030 0.400×; ⚠ toxic; transcription drop); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (NCI-H661 0.0686×); [[Homoharringtonine (drug)]] 5 µM in 1 line (C32 0.489×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.731×** | -6.9 | 2e-09 | 26/44 (A549, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.761×** | -6.3 | 1e-07 | 27/49 (HCT15, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.927× | -6.0 | 3e-07 | 2/50 (NCI-H23, NCI-H1792) | inconsistent across doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | 0.862× | -4.8 | 2e-04 | 11/48 (NCI-H1792, SW480, …) | top dose only |  |
| [[Budesonide (drug)]] 0.5 µM |  | **0.831×** | -4.3 | 0.002 | 19/48 (NCI-H2347, CFPAC-1, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | 0.837× | -3.9 | 0.008 | 17/49 (NCI-H1573, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.858× | -3.5 | 0.033 | 13/48 (NCI-H1573, BT-474, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.850× | -3.5 | 0.038 | 19/45 (C-33 A, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~24% of this change | 0.866× | -3.3 | 0.057 | 17/48 (NCI-H2347, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Terfenadine (drug)]] 0.5 µM |  | 0.874× | -3.1 | 0.098 | 11/48 (Hs 766T, LS 180, …) | inconsistent across doses |  |
| [[Sulfatinib (drug)]] 5 µM |  | 0.869× | -3.1 | 0.098 | 9/49 (A549, LOX-IMVI, …) | top dose only |  |
| [[Budesonide (drug)]] 0.05 µM |  | 0.875× | -3.1 | 0.10 | 11/48 (NCI-H1573, NCI-H2347, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 416. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 73.1 | 23 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 9.27× (z +28.5) | — |
| [[PANC-1 (line)]] | alt | 56.8 | 14 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +23.1) | — |
| [[HOP62 (line)]] | alt | 47.6 | 13 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.66× (z +27.7) | — |
| [[HS-578T (line)]] | alt | 68.0 | 12 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +16.9) | — |
| [[LOX-IMVI (line)]] | wt | 69.6 | 11 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +14.9) | — |
| [[LS 180 (line)]] | wt | 57.9 | 11 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.13× (z +15.2) | — |
| [[A-172 (line)]] | wt | 68.9 | 10 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.49× (z +27.3) | — |
| [[NCI-H1573 (line)]] | alt | 123 | 10 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.15× (z +19.5) | — |
| [[A498 (line)]] | wt | 92.1 | 9 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.76× (z +22.7) | — |
| [[A549 (line)]] | wt | 114 | 8 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.64× (z +25.4) | [[Dinaciclib (drug)]] 5 µM 0.187× (z -18.9) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 52.4 | 9 | 0 | [[Panobinostat (drug)]] 5 µM 7.03× (z +14.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 101 | 9 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +19.6) | — |
| [[SW480 (line)]] | alt | 92.5 | 9 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.36× (z +20.9) | — |
| [[HT-29 (line)]] | alt | 64.2 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +16.5) | — |
| [[KATO III (line)]] | alt | 67.7 | 8 | 0 | [[Panobinostat (drug)]] 5 µM 4.55× (z +17.8) | — |
| [[SHP-77 (line)]] | alt | 76.0 | 8 | 0 | [[Panobinostat (drug)]] 5 µM 3.05× (z +11.4) | — |
| [[AsPC-1 (line)]] | alt | 29.6 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.82× (z +17.1) | — |
| [[J82 (line)]] | alt | 39.9 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.93× (z +19.1) | — |
| [[LoVo (line)]] | wt | 73.0 | 6 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.62× (z +11.9) | [[Dinaciclib (drug)]] 5 µM 0.280× (z -15.2) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 167 | 5 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.44× (z +12.1) | [[Dinaciclib (drug)]] 0.5 µM 0.259× (z -13.1) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 109 | 6 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.88× (z +12.3) | — |
| [[HEC-1-A (line)]] | alt | 119 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +16.0) | [[Dinaciclib (drug)]] 0.5 µM 0.468× (z -10.2) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 138 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.02× (z +23.6) | [[Dinaciclib (drug)]] 5 µM 0.339× (z -12.6) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 54.3 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.56× (z +17.4) | — |
| [[RKO (line)]] | wt | 128 | 5 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.36× (z +15.7) | [[Dinaciclib (drug)]] 0.5 µM 0.411× (z -9.5) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 79.1 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.45× (z +13.7) | — |
| [[HepG2_C3A (line)]] | wt | 87.5 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.74× (z +13.1) | — |
| [[NCI-H2347 (line)]] | alt | 96.4 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +13.6) | [[Dinaciclib (drug)]] 0.5 µM 0.459× (z -9.9) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 58.3 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 3.94× (z +14.0) | — |
| [[SW1417 (line)]] | alt | 80.3 | 5 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.62× (z +11.3) | — |
| [[A-427 (line)]] | wt | 109 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +16.7) | [[Dinaciclib (drug)]] 0.5 µM 0.381× (z -11.4) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 95.3 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.62× (z +9.8) | [[Dinaciclib (drug)]] 0.05 µM 0.301× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 103 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +16.0) | — |
| [[H4 (line)]] | wt | 43.0 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.83× (z +13.9) | — |
| [[Hs 766T (line)]] | wt | 53.2 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +12.4) | — |
| [[HCT15 (line)]] | alt | 117 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.21× (z +11.6) | [[Dinaciclib (drug)]] 0.5 µM 0.215× (z -15.4) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 182 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +13.1) | [[Dinaciclib (drug)]] 5 µM 0.400× (z -11.5) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 80.2 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.84× (z +9.6) | — |
| [[SW 900 (line)]] | alt | 65.1 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.75× (z +12.0) | — |
| [[C32 (line)]] | wt | 87.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.489× (z -9.8) |
| [[NCI-H1792 (line)]] | alt | 67.6 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.79× (z +8.5) | — |
| [[NCI-H661 (line)]] | alt | 104 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.0686× (z -14.6) |
| [[RPMI-7951 (line)]] | alt | 63.9 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.95× (z +8.5) | — |
| [[SK-MEL-2 (line)]] | alt | 73.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +8.9) | — |
| [[AN3 CA (line)]] | alt | 87.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 124 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 93.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 87.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 55.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 118 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 416), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPLP0P2]] | +0.58 | +0.43 / +0.66 | both halves | 3e-05 |  |
| [[OLFM2]] | +0.57 | +0.42 / +0.64 | both halves | 4e-05 |  |
| [[SYP]] | +0.56 | +0.43 / +0.56 | both halves | 3e-05 |  |
| [[CREB5]] | +0.55 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[TMEM40]] | +0.53 | +0.40 / +0.55 | both halves | 4e-05 |  |
| [[UBE2H]] | +0.52 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[CMIP]] | +0.52 | +0.42 / +0.49 | both halves | 4e-05 | same gene group |
| [[NDRG4]] | +0.52 | +0.37 / +0.59 | both halves | 9e-05 |  |
| [[GIPR]] | +0.51 | +0.39 / +0.48 | both halves | 6e-05 | same gene group |
| [[PLIN3]] | +0.51 | +0.45 / +0.34 | both halves | 1e-04 |  |
| [[CBX6]] | +0.51 | +0.34 / +0.57 | both halves | 1e-04 |  |
| [[SHF]] | +0.50 | +0.39 / +0.52 | both halves | 5e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLE3]] | -0.57 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[TDRD3]] | -0.55 | -0.46 / -0.53 | both halves | 2e-05 |  |
| [[MCMBP]] | -0.50 | -0.54 / -0.46 | both halves | 2e-05 |  |
| [[TSN]] | -0.50 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[PACRGL]] | -0.49 | -0.30 / -0.43 | both halves | 2e-04 |  |
| [[UBTF]] | -0.49 | -0.42 / -0.49 | both halves | 4e-05 | same gene group |
| [[NCOA2]] | -0.48 | -0.31 / -0.55 | both halves | 2e-04 |  |
| [[NDUFAF6]] | -0.48 | -0.40 / -0.41 | both halves | 5e-05 | same gene group |
| [[CTPS2]] | -0.48 | -0.37 / -0.50 | both halves | 8e-05 | same gene group |
| [[ANGEL2]] | -0.47 | -0.29 / -0.50 | both halves | 2e-04 |  |
| [[MTFR2]] | -0.47 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[KANSL2]] | -0.46 | -0.39 / -0.41 | both halves | 5e-05 | same gene group |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RPLP0P2]] | B | RPLP0P2 activity lowers ATP6V0A1's level | lines that do not express RPLP0P2 (7) vs lines expressing it (43) | 1.72× higher at baseline in the lines without RPLP0P2 | 0.018 | ⚠ within organs, on part of the lines; also absent: CAMK2N1, ETS2, CSTB; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 125]]; 39 genes; every member is in the + arm (projection on the module's main direction 0.456). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (20.8, 10.5); signed map (30.7, 24.0). **Vector** length 92.2, 28.0% of its response variance represented; |z| ≥ 3 in 1,555 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +10.9 | +16.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +9.8 | +10.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +5.7 | +11.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.0 | +10.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.0 | +14.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.0 | +8.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.9 | +14.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +3.7 | +3.5 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | -5.0 | +0.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | -2.9 | +3.3 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.8 | -0.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.8 | -0.5 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -2.7 | -3.1 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.7 | -1.1 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.6 | +0.6 |

## What is on record

|  |  |
|---|---|
| Name | ATPase H+ transporting V0 subunit a1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.2 — chr17:42,458,844-42,522,582 (+) |
| Ensembl biotype | protein_coding |
| Also known as | a1, Vph1, Stv1; previously VPP1, ATP6N1, ATP6N1A |
| Gene groups (HGNC) | V-type ATPase subunits; MicroRNA protein coding host genes |
| Hallmark sets | HEME_METABOLISM |
| Reactome | 13 pathways, smallest: Regulation of MITF-M-dependent genes involved in lysosome biogenesis and autophagy; Insulin receptor recycling; ROS and RNS production in phagocytes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q93050](https://www.uniprot.org/uniprotkb/Q93050) (V-type proton ATPase 116 kDa subunit a 1):

> Subunit of the V0 complex of vacuolar(H+)-ATPase (V-ATPase), a multisubunit enzyme composed of a peripheral complex (V1) that hydrolyzes ATP and a membrane integral complex (V0) that transports protons across cellular membranes. V-ATPase is responsible for the acidification of various organelles, such as lysosomes, endosomes, the trans-Golgi network, and secretory granules, including synaptic vesicles. In certain cell types, can be exported to the plasma membrane, where it is involved in the …

**Summary**, from NCBI Gene [535](https://www.ncbi.nlm.nih.gov/gene/535):

> This gene encodes a component of vacuolar ATPase (V-ATPase), a multisubunit enzyme that mediates acidification of eukaryotic intracellular organelles. V-ATPase dependent organelle acidification is necessary for such intracellular processes as protein sorting, zymogen activation, receptor-mediated endocytosis, and synaptic vesicle proton gradient generation. V-ATPase is composed of a cytosolic V1 domain and a transmembrane V0 domain. The V1 domain consists of three A and three B subunits, two G …

**Accessions** — [HGNC:865](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:865) · Entrez [535](https://www.ncbi.nlm.nih.gov/gene/535) · UniProt [Q93050](https://www.uniprot.org/uniprotkb/Q93050) · Ensembl [ENSG00000033627](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000033627)

## Data

Gene col 416: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 416); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 416, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 416]; `tensor/DDL_lfc|DDL_z.npy` [416]; `embed/gene_vectors.npy` [416]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 416 or target_col == 416). Every well: [[ATP6V0A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATP6V0A1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
