---
symbol: "AZIN1"
type: "gene"
col: 7869
ensembl_id: "ENSG00000155096"
name: "antizyme inhibitor 1"
location: "8q22.3"
module: 25
arm: "+"
pooled_cpm: 126.14
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 0
n_dd_up_clean: 12
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# AZIN1

*antizyme inhibitor 1* — 8q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.71× (z +23.2, q 0e+00, up in 48 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 3 lines (RKO 0.313×, BT-474 0.354×, HepG2/C3A 0.360×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (SNU-1 0.0943×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PFN2]] (+0.64, fdr 7e-06), [[MPP1]] (+0.62, fdr 7e-06), [[TCP1]] (+0.59, fdr 1e-05); moves opposite to [[NDUFA13]] (-0.60, fdr 9e-06, ⚠ NDUFA13 in the vector space only through flagged drug-doses), [[DCAF10]] (-0.57, fdr 7e-06), [[RBX1]] (-0.57, fdr 1e-05), [[COPS9]] (-0.57, fdr 1e-05).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7869.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.71×** | +23.2 | 0e+00 | 48/48 (A549, HT-29, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **4.95×** | +13.8 | 7e-41 | 48/49 (NCI-H460, Panc 03.27, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **2.04×** | +11.3 | 3e-27 | 45/48 (PANC-1, A549, …) | top dose only | cell-cycle shift (explains ~16% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.89×** | +10.5 | 1e-23 | 46/48 (HT-29, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.87×** | +10.3 | 8e-23 | 43/48 (HT-29, RKO, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.74×** | +9.1 | 1e-17 | 39/48 (C32, A549, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.73×** | +9.0 | 2e-17 | 46/48 (HT-29, A498, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.74×** | +8.6 | 4e-16 | 45/48 (KATO III, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.71×** | +8.5 | 2e-15 | 39/47 (COLO 205, LoVo, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.65×** | +8.2 | 1e-14 | 35/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.22×** | +6.9 | 4e-10 | 38/48 (HEC-1-A, Panc 03.27, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.99×** | +5.9 | 2e-07 | 38/45 (SK-MEL-2, RKO, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.40×** | +5.5 | 2e-06 | 35/48 (KATO III, NCI-H1792, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.39×** | +5.4 | 2e-06 | 29/48 (KATO III, NCI-H460, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.51×** | +4.8 | 6e-05 | 35/49 (CFPAC-1, A498, …) | all doses, flat | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.18× | +3.8 | 0.004 | 20/48 (RKO, HOP62, …) | rises with dose |  |
| [[EX229 (drug)]] 0.05 µM |  | **1.26×** | +3.6 | 0.011 | 26/48 (Hs 766T, LoVo, …) | inconsistent across doses |  |
| [[Diphenhydramine (drug)]] 5 µM |  | **1.24×** | +3.3 | 0.024 | 23/48 (HOP62, SW 900, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7869.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 3 lines (RKO 0.313×, BT-474 0.354×, HepG2/C3A 0.360×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (SNU-1 0.0943×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 0.804× | -3.5 | 0.17 | 24/47 (NCI-H1573, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.866× | -3.4 | 0.17 | 16/48 (LOX-IMVI, hTERT-HPNE, …) | rises with dose |  |
| [[Sodium Salicylate (drug)]] 5 µM |  | 0.878× | -3.1 | 0.22 | 7/49 (J82, A-427, …) | top dose only |  |
| [[Cabozantinib (S-malate) (drug)]] 0.05 µM |  | 0.836× | -3.0 | 0.22 | 14/48 (KATO III, A498, …) | inconsistent across doses |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | 0.836× | -3.0 | 0.22 | 19/48 (A-172, HS-578T, …) | inconsistent across doses |  |
| [[Bestatin (hydrochloride) (drug)]] 0.5 µM |  | 0.836× | -3.0 | 0.22 | 16/48 (C32, HOP62, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7869. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 90.2 | 9 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +15.4) | — |
| [[NCI-H460 (line)]] | wt | 75.8 | 9 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +18.1) | — |
| [[A-427 (line)]] | wt | 64.2 | 6 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.03× (z +11.4) | — |
| [[C32 (line)]] | wt | 119 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.65× (z +21.1) | — |
| [[HT-29 (line)]] | alt | 91.2 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.30× (z +23.5) | — |
| [[SK-MEL-2 (line)]] | alt | 90.3 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +16.3) | — |
| [[COLO 205 (line)]] | alt | 91.8 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.64× (z +21.2) | — |
| [[HOP62 (line)]] | alt | 103 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.41× (z +20.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 93.1 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +14.9) | — |
| [[Panc 03.27 (line)]] | alt | 153 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.91× (z +22.0) | — |
| [[PANC-1 (line)]] | alt | 130 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.10× (z +21.4) | — |
| [[RKO (line)]] | wt | 184 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.35× (z +17.3) | [[Dinaciclib (drug)]] 0.05 µM 0.313× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 188 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.36× (z +16.9) | — |
| [[A549 (line)]] | wt | 112 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.98× (z +25.9) | — |
| [[BT-474 (line)]] | alt | 233 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +12.8) | [[Dinaciclib (drug)]] 0.05 µM 0.354× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 134 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.75× (z +13.6) | [[Dinaciclib (drug)]] 5 µM 0.0943× (z -16.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 81.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.68× (z +18.0) | — |
| [[HEC-1-A (line)]] | alt | 135 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +15.8) | — |
| [[Hs 766T (line)]] | wt | 98.9 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +13.3) | — |
| [[LoVo (line)]] | wt | 74.1 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +15.5) | — |
| [[LS 180 (line)]] | wt | 112 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +14.5) | — |
| [[NCI-H1573 (line)]] | alt | 176 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +21.3) | — |
| [[SW 900 (line)]] | alt | 127 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +16.4) | — |
| [[SW480 (line)]] | alt | 113 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 7.57× (z +14.4) | — |
| [[AsPC-1 (line)]] | alt | 157 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.02× (z +19.0) | — |
| [[CFPAC-1 (line)]] | alt | 105 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.99× (z +19.2) | — |
| [[HCT15 (line)]] | alt | 120 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +10.8) | — |
| [[hTERT-HPNE (line)]] | wt | 105 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.13× (z +18.4) | — |
| [[LOX-IMVI (line)]] | wt | 128 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 7.19× (z +10.0) | — |
| [[NCI-H1792 (line)]] | alt | 75.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.89× (z +20.5) | — |
| [[NCI-H23 (line)]] | alt | 79.4 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +12.7) | — |
| [[NCI-H2347 (line)]] | alt | 255 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +14.1) | — |
| [[SW1417 (line)]] | alt | 246 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +15.2) | — |
| [[SW48 (line)]] | wt | 130 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +11.6) | — |
| [[H4 (line)]] | wt | 94.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +10.2) | — |
| [[HepG2_C3A (line)]] | wt | 112 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.360× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 208 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +13.0) | — |
| [[J82 (line)]] | alt | 114 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +13.6) | — |
| [[RPMI-7951 (line)]] | alt | 95.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.74× (z +16.2) | — |
| [[SHP-77 (line)]] | alt | 124 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.97× (z +9.6) ⚠ toxic | — |
| [[SNU-423 (line)]] | alt | 86.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.52× (z +16.0) | — |
| [[AN3 CA (line)]] | alt | 140 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 113 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 109 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 156 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 141 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 92.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 97.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7869), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*58 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PFN2]] | +0.64 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[MPP1]] | +0.62 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[TCP1]] | +0.59 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[PFKM]] | +0.59 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[FXR1]] | +0.58 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[UBQLN1]] | +0.57 | +0.63 / +0.57 | both halves | 1e-05 |  |
| [[ANXA6]] | +0.57 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[NXPE3]] | +0.56 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[CHORDC1]] | +0.55 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[CRYZ]] | +0.55 | +0.60 / +0.47 | both halves | 2e-05 |  |
| [[LMCD1-AS1]] | +0.54 | +0.36 / +0.58 | both halves | 1e-04 |  |
| [[HLTF]] | +0.54 | +0.49 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*42 of its nearest partners move opposite, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDUFA13]] ⚠ | -0.60 | -0.57 / -0.59 | both halves | 9e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[DCAF10]] | -0.57 | -0.58 / -0.59 | both halves | 7e-06 |  |
| [[RBX1]] | -0.57 | -0.55 / -0.61 | both halves | 1e-05 |  |
| [[COPS9]] | -0.57 | -0.58 / -0.56 | both halves | 1e-05 |  |
| [[GGA3]] | -0.57 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[ZNF586]] | -0.54 | -0.56 / -0.43 | both halves | 3e-05 |  |
| [[POLR2K]] | -0.54 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[HIC2]] | -0.53 | -0.56 / -0.49 | both halves | 1e-05 |  |
| [[TERF2IP]] | -0.53 | -0.38 / -0.57 | both halves | 7e-05 |  |
| [[DGCR2]] | -0.52 | -0.60 / -0.37 | both halves | 9e-05 |  |
| [[LRCH3]] | -0.52 | -0.52 / -0.46 | both halves | 3e-05 |  |
| [[OPA3]] | -0.52 | -0.60 / -0.40 | both halves | 5e-05 |  |
| [[LSM6]] | -0.52 | -0.41 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.444). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-25.0, -13.9); signed map (-25.7, -31.5). **Vector** length 94.6, 31.1% of its response variance represented; |z| ≥ 3 in 1,181 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +5.7 | +10.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.0 | +3.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.7 | +2.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +4.5 | +1.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +4.0 | +8.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.5 | +9.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.3 | +0.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.1 | +4.8 |
| fall | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -9.3 | +2.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | -8.4 | +4.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -8.3 | +8.2 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | -7.8 | +3.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -5.2 | -3.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.6 | -1.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.5 | -3.4 |
|  | [[Amsacrine (drug)]] 5 µM |  | -2.5 | -2.2 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -2.5 | -1.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.4 | +0.3 |

## What is on record

|  |  |
|---|---|
| Name | antizyme inhibitor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q22.3 — chr8:102,826,111-102,893,864 (-) |
| Ensembl biotype | protein_coding |
| Also known as | OAZI, ODC1L; previously OAZIN |
| Gene groups (HGNC) | Antizyme inhibitor family |
| Reactome | 3 pathways, smallest: Regulation of ornithine decarboxylase (ODC); Metabolism of polyamines; Metabolism of amino acids and derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [O14977](https://www.uniprot.org/uniprotkb/O14977) (Antizyme inhibitor 1):

> Antizyme inhibitor (AZI) protein that positively regulates ornithine decarboxylase (ODC) activity and polyamine uptake. AZI is an enzymatically inactive ODC homolog that counteracts the negative effect of ODC antizymes (AZs) OAZ1, OAZ2 and OAZ3 on ODC activity by competing with ODC for antizyme-binding. Inhibits antizyme-dependent ODC degradation and releases ODC monomers from their inactive complex with antizymes, leading to formation of the catalytically active ODC homodimer and restoring …

**Summary**, from NCBI Gene [51582](https://www.ncbi.nlm.nih.gov/gene/51582):

> The protein encoded by this gene belongs to the antizyme inhibitor family, which plays a role in cell growth and proliferation by maintaining polyamine homeostasis within the cell. Antizyme inhibitors are homologs of ornithine decarboxylase (ODC, the key enzyme in polyamine biosynthesis) that have lost the ability to decarboxylase ornithine; however, retain the ability to bind to antizymes. Antizymes negatively regulate intracellular polyamine levels by binding to ODC and targeting it for …

**Accessions** — [HGNC:16432](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16432) · Entrez [51582](https://www.ncbi.nlm.nih.gov/gene/51582) · UniProt [O14977](https://www.uniprot.org/uniprotkb/O14977) · Ensembl [ENSG00000155096](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000155096)

## Data

Gene col 7869: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7869); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7869, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7869]; `tensor/DDL_lfc|DDL_z.npy` [7869]; `embed/gene_vectors.npy` [7869]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7869 or target_col == 7869). Every well: [[AZIN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AZIN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
