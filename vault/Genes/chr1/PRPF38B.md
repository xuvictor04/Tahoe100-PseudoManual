---
symbol: "PRPF38B"
type: "gene"
col: 5519
ensembl_id: "ENSG00000134186"
name: "pre-mRNA processing factor 38B"
location: "1p13.3"
module: 11
arm: "+"
pooled_cpm: 143.15
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 0
n_dd_up_clean: 9
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# PRPF38B

*pre-mRNA processing factor 38B* — 1p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.49× (z +32.4, q 0e+00, up in 48 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (SK-MEL-2 0.361×, A-427 0.425×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CEBPZ]] (+0.78, fdr 7e-06), [[SURF6]] (+0.77, fdr 7e-06), [[CWC22]] (+0.73, fdr 7e-06); moves opposite to [[PGRMC1]] (-0.67, fdr 7e-06), [[ZDHHC16]] (-0.66, fdr 7e-06), [[NAGA]] (-0.65, fdr 7e-06).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5519.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.49×** | +32.4 | 0e+00 | 48/48 (HS-578T, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **4.13×** | +21.6 | 0e+00 | 48/48 (HS-578T, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **3.09×** | +16.6 | 0e+00 | 48/48 (SK-MEL-2, NCI-H1573, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **2.41×** | +13.4 | 8e-39 | 48/48 (LS 180, SW480, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **2.13×** | +11.6 | 7e-29 | 47/48 (LS 180, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.93×** | +9.6 | 1e-19 | 44/48 (LOX-IMVI, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.12×** | +9.1 | 8e-18 | 48/49 (SW480, COLO 205, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.75×** | +8.6 | 7e-16 | 45/48 (SW480, LS 180, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.81×** | +8.3 | 1e-14 | 45/48 (SK-MEL-2, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.72×** | +8.0 | 8e-14 | 43/47 (NCI-H1573, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.54×** | +6.6 | 2e-09 | 43/48 (SW480, LS 180, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~47% of this change | **1.47×** | +5.6 | 9e-07 | 43/47 (LoVo, MIA PaCa-2, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.43×** | +5.5 | 2e-06 | 37/48 (HS-578T, MIA PaCa-2, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.39×** | +5.0 | 2e-05 | 33/48 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.34×** | +4.5 | 2e-04 | 34/48 (CFPAC-1, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.26×** | +3.5 | 0.015 | 30/48 (CFPAC-1, HS-578T, …) | rises with dose |  |
| [[Bendamustine (drug)]] 5 µM |  | **1.26×** | +3.4 | 0.023 | 24/48 (A549, SW 900, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5519.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (SK-MEL-2 0.361×, A-427 0.425×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Folic acid (drug)]] 5 µM |  | 0.851× | -3.5 | 0.18 | 12/48 (LoVo, MIA PaCa-2, …) | top dose only | position effect removed |
| [[Fenofibrate (drug)]] 0.05 µM |  | 0.786× | -3.4 | 0.18 | 33/48 (J82, A498, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.794× | -3.3 | 0.18 | 26/48 (NCI-H23, SW480, …) | inconsistent across doses |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 0.810× | -3.2 | 0.18 | 29/48 (HEC-1-A, RPMI-7951, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, +0.46 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5519. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 129 | 10 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.18× (z +30.9) | — |
| [[SW480 (line)]] | alt | 184 | 10 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +24.8) | — |
| [[LOX-IMVI (line)]] | wt | 143 | 9 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.34× (z +29.5) | — |
| [[HS-578T (line)]] | alt | 138 | 8 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.98× (z +31.7) | — |
| [[LoVo (line)]] | wt | 178 | 8 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.11× (z +27.2) | — |
| [[LS 180 (line)]] | wt | 158 | 8 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.15× (z +25.8) | — |
| [[HEC-1-A (line)]] | alt | 183 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.06× (z +23.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 129 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.24× (z +24.1) | — |
| [[NCI-H460 (line)]] | wt | 122 | 7 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.13× (z +22.2) | — |
| [[PANC-1 (line)]] | alt | 123 | 7 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.68× (z +27.9) | — |
| [[SK-MEL-2 (line)]] | alt | 245 | 6 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.49× (z +31.3) | [[Dinaciclib (drug)]] 5 µM 0.361× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[COLO 205 (line)]] | alt | 93.7 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.51× (z +19.7) | — |
| [[H4 (line)]] | wt | 117 | 6 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.81× (z +20.5) | — |
| [[KATO III (line)]] | alt | 127 | 6 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.90× (z +26.3) | — |
| [[SNU-1 (line)]] | wt | 140 | 6 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.61× (z +16.7) | — |
| [[AsPC-1 (line)]] | alt | 149 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.16× (z +24.9) | — |
| [[CFPAC-1 (line)]] | alt | 111 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.61× (z +26.6) | — |
| [[HCT15 (line)]] | alt | 184 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.33× (z +21.1) | — |
| [[HOP62 (line)]] | alt | 82.3 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.01× (z +26.4) | — |
| [[Hs 766T (line)]] | wt | 115 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.48× (z +20.1) | — |
| [[HT-29 (line)]] | alt | 158 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.18× (z +25.2) | — |
| [[NCI-H1792 (line)]] | alt | 114 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.04× (z +24.3) | — |
| [[NCI-H2030 (line)]] | alt | 130 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.69× (z +20.9) | — |
| [[NCI-H23 (line)]] | alt | 411 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.76× (z +28.7) | — |
| [[A-172 (line)]] | wt | 102 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.76× (z +22.0) | — |
| [[A-427 (line)]] | wt | 116 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +15.5) | [[Dinaciclib (drug)]] 5 µM 0.425× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[C32 (line)]] | wt | 101 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.37× (z +22.7) | — |
| [[RKO (line)]] | wt | 200 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +15.7) | — |
| [[RPMI-7951 (line)]] | alt | 168 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.46× (z +23.2) | — |
| [[SNU-423 (line)]] | alt | 101 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.07× (z +28.1) | — |
| [[SW 900 (line)]] | alt | 127 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.53× (z +19.1) | — |
| [[SW1417 (line)]] | alt | 146 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +19.6) | — |
| [[SW48 (line)]] | wt | 160 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.87× (z +20.4) | — |
| [[A498 (line)]] | wt | 155 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.05× (z +30.4) | — |
| [[A549 (line)]] | wt | 105 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.55× (z +20.7) | — |
| [[BT-474 (line)]] | alt | 109 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +12.2) | — |
| [[HepG2_C3A (line)]] | wt | 108 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.27× (z +18.8) | — |
| [[hTERT-HPNE (line)]] | wt | 136 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.92× (z +20.5) | — |
| [[J82 (line)]] | alt | 151 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.71× (z +23.0) | — |
| [[NCI-H2347 (line)]] | alt | 99.3 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.64× (z +23.6) | — |
| [[Panc 03.27 (line)]] | alt | 157 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.35× (z +24.2) | — |
| [[AN3 CA (line)]] | alt | 139 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.56× (z +11.9) | — |
| [[C-33 A (line)]] | alt | 172 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +14.0) | — |
| [[SHP-77 (line)]] | alt | 153 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +13.3) | — |
| [[CHP-212 (line)]] | wt | 97.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +8.5) | — |
| [[SW 1088 (line)]] | alt | 117 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.00× (z +10.4) | — |
| [[SW 1271 (line)]] | alt | 167 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.24× (z +8.8) | — |
| [[NCI-H2122 (line)]] | alt | 131 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 147 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 182 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5519), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CEBPZ]] | +0.78 | +0.78 / +0.75 | both halves | 7e-06 |  |
| [[SURF6]] | +0.77 | +0.76 / +0.78 | both halves | 7e-06 |  |
| [[CWC22]] | +0.73 | +0.73 / +0.63 | both halves | 7e-06 |  |
| [[PPIG]] | +0.73 | +0.74 / +0.65 | both halves | 7e-06 | STRING 682 |
| [[ESF1]] | +0.72 | +0.77 / +0.64 | both halves | 7e-06 |  |
| [[MRPS18B]] | +0.70 | +0.68 / +0.69 | both halves | 7e-06 |  |
| [[MRFAP1L1]] | +0.70 | +0.69 / +0.68 | both halves | 7e-06 |  |
| [[MFAP1]] | +0.69 | +0.69 / +0.66 | both halves | 7e-06 |  |
| [[ZC3H13]] | +0.69 | +0.70 / +0.65 | both halves | 7e-06 |  |
| [[ABCF1]] | +0.69 | +0.72 / +0.62 | both halves | 7e-06 |  |
| [[CCDC174]] | +0.68 | +0.67 / +0.68 | both halves | 7e-06 |  |
| [[ZNF75A]] | +0.68 | +0.66 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PGRMC1]] | -0.67 | -0.65 / -0.68 | both halves | 7e-06 |  |
| [[ZDHHC16]] | -0.66 | -0.62 / -0.62 | both halves | 7e-06 |  |
| [[NAGA]] | -0.65 | -0.59 / -0.63 | both halves | 7e-06 |  |
| [[AP2M1]] | -0.63 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[TPGS2]] | -0.63 | -0.66 / -0.61 | both halves | 7e-06 |  |
| [[EDEM1]] | -0.61 | -0.58 / -0.63 | both halves | 7e-06 |  |
| [[MOB1A]] | -0.60 | -0.58 / -0.67 | both halves | 7e-06 |  |
| [[ESYT1]] | -0.59 | -0.59 / -0.60 | both halves | 7e-06 |  |
| [[ATP2C1]] | -0.59 | -0.57 / -0.59 | both halves | 1e-05 |  |
| [[ADAM15]] | -0.59 | -0.56 / -0.51 | both halves | 1e-05 |  |
| [[RPN1]] | -0.59 | -0.57 / -0.61 | both halves | 1e-05 |  |
| [[VAMP3]] | -0.59 | -0.52 / -0.58 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.669). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-39.3, 1.3); signed map (-1.0, -20.0). **Vector** length 89.0, 32.7% of its response variance represented; |z| ≥ 3 in 1,026 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.6 | +5.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.3 | +9.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.8 | +0.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.6 | +1.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.5 | +21.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.8 | +8.3 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.7 | +0.3 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.8 | +1.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~47% of this change | -2.6 | +5.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | +0.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | -1.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -2.6 | +1.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.4 | +3.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.3 | -3.3 |
|  | [[Clonidine (hydrochloride) (drug)]] 5 µM |  | -2.3 | -1.5 |
|  | [[Folic acid (drug)]] 5 µM |  | -2.2 | -3.5 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -2.1 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | pre-mRNA processing factor 38B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p13.3 — chr1:108,692,310-108,702,928 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10330, NET1 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5VTL8](https://www.uniprot.org/uniprotkb/Q5VTL8) (Pre-mRNA-splicing factor 38B):

> May be required for pre-mRNA splicing.

**Summary**, from NCBI Gene [55119](https://www.ncbi.nlm.nih.gov/gene/55119):

> Enables RNA binding activity. Predicted to be involved in mRNA splicing, via spliceosome. Predicted to be located in nucleus. Predicted to be part of precatalytic spliceosome. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25512](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25512) · Entrez [55119](https://www.ncbi.nlm.nih.gov/gene/55119) · UniProt [Q5VTL8](https://www.uniprot.org/uniprotkb/Q5VTL8) · Ensembl [ENSG00000134186](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134186)

## Data

Gene col 5519: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5519); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5519, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5519]; `tensor/DDL_lfc|DDL_z.npy` [5519]; `embed/gene_vectors.npy` [5519]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5519 or target_col == 5519). Every well: [[PRPF38B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRPF38B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
