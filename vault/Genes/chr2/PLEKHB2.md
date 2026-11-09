---
symbol: "PLEKHB2"
type: "gene"
col: 3719
ensembl_id: "ENSG00000115762"
name: "pleckstrin homology domain containing B2"
location: "2q21.1"
module: 11
arm: "-"
pooled_cpm: 142.1
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 2
n_dd_up_clean: 19
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# PLEKHB2

*pleckstrin homology domain containing B2* — 2q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.09× (z +13.8, q 2e-40, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Carbamazepine (drug)]] 5 µM: 0.817× (z -3.8, q 0.084, down in 24 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (C-33 A 0.192×, NCI-H23 0.373×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (A-427 0.416×, C-33 A 0.340×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.549×; ⚠ cell-cycle shift, explains ~14% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GRB2]] (+0.68, fdr 1e-05), [[ILRUN]] (+0.63, fdr 8e-06), [[STARD3NL]] (+0.61, fdr 1e-05); moves opposite to [[ZNF518A]] (-0.62, fdr 7e-05), [[RBX1]] (-0.60, fdr 1e-05), [[HMGXB4]] (-0.60, fdr 1e-05).
> It sits in the **-** arm of [[Module 011]] (Mitochondrial translation elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 9 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3719.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.09×** | +13.8 | 2e-40 | 48/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.99×** | +12.9 | 2e-35 | 48/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.97×** | +12.7 | 1e-34 | 47/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.07×** | +10.9 | 1e-25 | 46/49 (Hs 766T, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.78×** | +10.8 | 4e-25 | 45/48 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.68×** | +9.7 | 4e-20 | 44/48 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.63×** | +9.1 | 6e-18 | 41/48 (SW480, LS 180, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.58×** | +8.5 | 9e-16 | 40/48 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.57×** | +8.0 | 1e-13 | 38/48 (SW480, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.52×** | +7.9 | 2e-13 | 35/48 (SW480, C32, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.48×** | +7.4 | 9e-12 | 36/48 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.46×** | +7.1 | 5e-11 | 43/48 (HepG2/C3A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.46×** | +7.0 | 8e-11 | 38/48 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.46×** | +6.8 | 5e-10 | 30/47 (NCI-H460, HOP62, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.43×** | +6.6 | 1e-09 | 41/48 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.28×** | +6.5 | 2e-09 | 30/49 (LOX-IMVI, HS-578T, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.83×** | +5.9 | 1e-07 | 41/49 (HOP62, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3719.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (C-33 A 0.192×, NCI-H23 0.373×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (A-427 0.416×, C-33 A 0.340×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.549×; ⚠ cell-cycle shift, explains ~14% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Carbamazepine (drug)]] 5 µM |  | **0.817×** | -3.8 | 0.084 | 24/47 (KATO III, NCI-H2030, …) | rises with dose |  |
| [[Omeprazole (drug)]] 0.5 µM |  | **0.826×** | -3.6 | 0.099 | 20/48 (PANC-1, RKO, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.834× | -3.3 | 0.21 | 20/48 (NCI-H2030, SK-MEL-2, …) | top dose only |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | 0.844× | -3.2 | 0.21 | 12/47 (HepG2/C3A, Hs 766T, …) | inconsistent across doses | low cells (technical?) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 0.847× | -3.1 | 0.22 | 18/48 (AsPC-1, NCI-H2030, …) | rises with dose |  |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | 0.845× | -3.0 | 0.22 | 16/49 (CFPAC-1, SK-MEL-2, …) | top dose only | plate-row cell shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3719. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 115 | 13 (6 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.89× (z +16.9) | — |
| [[HOP62 (line)]] | alt | 94.0 | 10 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.95× (z +12.2) | — |
| [[NCI-H1792 (line)]] | alt | 79.3 | 7 (3 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.13× (z +10.7) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 3.05× (z +10.5) | — |
| [[SW480 (line)]] | alt | 117 | 7 | 0 | [[Panobinostat (drug)]] 5 µM 2.54× (z +13.8) | — |
| [[PANC-1 (line)]] | alt | 99.7 | 6 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.08× (z +10.8) | — |
| [[C32 (line)]] | wt | 98.2 | 5 | 0 | [[Auranofin (drug)]] 5 µM 2.62× (z +9.9) | — |
| [[Hs 766T (line)]] | wt | 91.5 | 5 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 7.25× (z +11.3) | — |
| [[C-33 A (line)]] | alt | 340 | 2 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.63× (z +16.7) ⚠ cell-cycle shift, explains ~14% of this change | [[Dinaciclib (drug)]] 5 µM 0.192× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[H4 (line)]] | wt | 133 | 4 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.33× (z +11.1) | — |
| [[HT-29 (line)]] | alt | 148 | 4 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.05× (z +9.5) | — |
| [[KATO III (line)]] | alt | 105 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.45× (z +13.8) | — |
| [[LS 180 (line)]] | wt | 143 | 4 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.36× (z +10.0) | — |
| [[HepG2_C3A (line)]] | wt | 140 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.24× (z +9.0) | — |
| [[HS-578T (line)]] | alt | 84.0 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.86× (z +8.8) | — |
| [[LoVo (line)]] | wt | 91.9 | 3 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.16× (z +9.8) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 5 µM 1.95× (z +8.8) | — |
| [[A-427 (line)]] | wt | 115 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.416× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[BT-474 (line)]] | alt | 235 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.56× (z +9.5) | — |
| [[LOX-IMVI (line)]] | wt | 111 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.10× (z +10.4) | — |
| [[NCI-H23 (line)]] | alt | 184 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 1.99× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.373× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SHP-77 (line)]] | alt | 84.6 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.32× (z +9.1) | — |
| [[SNU-1 (line)]] | wt | 317 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.62× (z +17.2) ⚠ cell-cycle shift, explains ~14% of this change | — |
| [[A-172 (line)]] | wt | 140 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +9.4) ⚠ cell-cycle shift, explains ~14% of this change | — |
| [[AsPC-1 (line)]] | alt | 103 | 1 | 0 | [[Belinostat (drug)]] 5 µM 2.08× (z +9.0) | — |
| [[CFPAC-1 (line)]] | alt | 136 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.26× (z +9.1) | — |
| [[HEC-1-A (line)]] | alt | 424 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +10.8) ⚠ cell-cycle shift, explains ~14% of this change | — |
| [[J82 (line)]] | alt | 135 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.61× (z +9.7) | — |
| [[NCI-H1573 (line)]] | alt | 172 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +13.8) ⚠ cell-cycle shift, explains ~14% of this change | — |
| [[Panc 03.27 (line)]] | alt | 93.6 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.39× (z +9.2) | — |
| [[RKO (line)]] | wt | 141 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.332× (z -11.1) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[RPMI-7951 (line)]] | alt | 133 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.73× (z +9.2) | — |
| [[SNU-423 (line)]] | alt | 109 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.96× (z +9.7) | — |
| [[SW1417 (line)]] | alt | 185 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.23× (z +9.5) | — |
| [[A498 (line)]] | wt | 196 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 108 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 251 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 101 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 106 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 167 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 150 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 146 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 145 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 313 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 84.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 120 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 152 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 239 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 108 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3719), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*54 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GRB2]] | +0.68 | +0.74 / +0.54 | both halves | 1e-05 |  |
| [[ILRUN]] | +0.63 | +0.61 / +0.58 | both halves | 8e-06 |  |
| [[STARD3NL]] | +0.61 | +0.65 / +0.49 | both halves | 1e-05 |  |
| [[NTAN1]] | +0.57 | +0.46 / +0.48 | both halves | 2e-05 |  |
| [[TPD52]] | +0.57 | +0.59 / +0.48 | both halves | 2e-05 |  |
| [[MLF2]] | +0.57 | +0.49 / +0.43 | both halves | 3e-05 |  |
| [[EIF2S3]] | +0.56 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[PLEKHA8]] | +0.56 | +0.61 / +0.41 | both halves | 4e-05 | same gene group |
| [[SLC39A6]] | +0.55 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[STAM]] | +0.55 | +0.62 / +0.41 | both halves | 4e-05 |  |
| [[ENTREP3]] | +0.55 | +0.53 / +0.43 | both halves | 3e-05 |  |
| [[LIMK1]] | +0.55 | +0.50 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*46 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF518A]] | -0.62 | -0.68 / -0.38 | both halves | 7e-05 |  |
| [[RBX1]] | -0.60 | -0.59 / -0.56 | both halves | 1e-05 |  |
| [[HMGXB4]] | -0.60 | -0.50 / -0.61 | both halves | 1e-05 |  |
| [[NAIF1]] | -0.60 | -0.60 / -0.46 | both halves | 3e-05 |  |
| [[TRIP11]] | -0.59 | -0.63 / -0.48 | both halves | 2e-05 |  |
| [[GGA3]] | -0.58 | -0.52 / -0.60 | both halves | 1e-05 |  |
| [[ZNF764]] | -0.58 | -0.57 / -0.43 | both halves | 3e-05 |  |
| [[UNK]] | -0.58 | -0.61 / -0.37 | both halves | 8e-05 |  |
| [[ERCC6L2]] | -0.57 | -0.61 / -0.34 | both halves | 1e-04 |  |
| [[HELQ]] | -0.56 | -0.56 / -0.39 | both halves | 5e-05 |  |
| [[MRFAP1L1]] | -0.56 | -0.60 / -0.48 | both halves | 2e-05 |  |
| [[RFX1]] | -0.56 | -0.49 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **-** arm (projection on the module's main direction -0.583). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-26.4, 9.9); signed map (-48.9, -8.3). **Vector** length 85.6, 24.7% of its response variance represented; |z| ≥ 3 in 1,258 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.8 | +2.7 |
|  | [[Selinexor (drug)]] 5 µM |  | +5.5 | +5.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +5.4 | +0.3 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +5.1 | +7.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +5.0 | +0.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.6 | +5.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.3 | +9.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.3 | +7.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.2 | +3.7 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.2 | +0.6 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -7.8 | +1.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | -7.3 | +5.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.1 | +2.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.5 | -0.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.1 | +9.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.6 | -0.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.9 | -3.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.8 | -1.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.7 | +0.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.5 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | pleckstrin homology domain containing B2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q21.1 — chr2:131,104,847-131,353,709 (+) |
| Ensembl biotype | protein_coding |
| Also known as | EVT2, FLJ20783 |
| Gene groups (HGNC) | Pleckstrin homology domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96CS7](https://www.uniprot.org/uniprotkb/Q96CS7) (Pleckstrin homology domain-containing family B member 2):

> Involved in retrograde transport of recycling endosomes.

**Summary**, from NCBI Gene [55041](https://www.ncbi.nlm.nih.gov/gene/55041):

> Enables phosphatidylinositol-3,4,5-trisphosphate binding activity. Predicted to be involved in regulation of cell differentiation. Predicted to be located in recycling endosome membrane. Predicted to be active in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:19236](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19236) · Entrez [55041](https://www.ncbi.nlm.nih.gov/gene/55041) · UniProt [Q96CS7](https://www.uniprot.org/uniprotkb/Q96CS7) · Ensembl [ENSG00000115762](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115762)

## Data

Gene col 3719: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3719); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3719, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3719]; `tensor/DDL_lfc|DDL_z.npy` [3719]; `embed/gene_vectors.npy` [3719]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3719 or target_col == 3719). Every well: [[PLEKHB2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLEKHB2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
