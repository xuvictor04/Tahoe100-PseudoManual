---
symbol: "SLC35F5"
type: "gene"
col: 3619
ensembl_id: "ENSG00000115084"
name: "solute carrier family 35 member F5"
location: "2q14.1"
module: 4
arm: "-"
pooled_cpm: 145.45
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 14
n_dd_up_clean: 1
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# SLC35F5

*solute carrier family 35 member F5* — 2q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[Doxorubicin (hydrochloride) (drug)]] 5 µM: 1.28× (z +4.1, q 0.015, up in 27 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (NCI-H1573 3.87×, SHP-77 2.75×, LoVo 1.70×, AsPC-1 1.70×; ⚠ cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (AsPC-1 2.10×, COLO 205 2.19×, SW 900 1.82×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (NCI-H1573 2.79×; ⚠ cell-cycle shift, explains ~0% of this change); [[Auranofin (drug)]] 5 µM in 1 line (SHP-77 2.62×); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (C32 2.13×).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (8 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 0.728× (z -5.4, q 3e-05, down in 36 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.838× (z -4.4, q 0.001, down in 21 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC30A9]] (+0.57, fdr 3e-04), [[LEPR]] (+0.55, fdr 1e-05), [[CEP95]] (+0.53, fdr 3e-05); moves opposite to [[CDIN1]] (-0.58, fdr 3e-05), [[WDR7]] (-0.56, fdr 1e-05), [[SLC25A12]] (-0.55, fdr 3e-05).
> It sits in the **-** arm of [[Module 004]] (MYC targets v1).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3619.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (NCI-H1573 3.87×, SHP-77 2.75×, LoVo 1.70×, AsPC-1 1.70×; ⚠ cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (AsPC-1 2.10×, COLO 205 2.19×, SW 900 1.82×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (NCI-H1573 2.79×; ⚠ cell-cycle shift, explains ~0% of this change); [[Auranofin (drug)]] 5 µM in 1 line (SHP-77 2.62×); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (C32 2.13×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.28×** | +4.1 | 0.015 | 27/48 (C32, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +4.0 | 0.015 | 24/49 (AsPC-1, COLO 205, …) | top dose only |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 1.22× | +3.4 | 0.12 | 23/48 (SW 900, A498, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.20× | +3.2 | 0.17 | 22/47 (RKO, SW48, …) | rises with dose | low cells (technical?) |
| [[Fenofibrate (drug)]] 0.05 µM |  | 1.22× | +3.1 | 0.17 | 17/48 (NCI-H2347, NCI-H460, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | 1.40× | +3.1 | 0.17 | 21/49 (A-427, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Erlotinib (drug)]] 0.05 µM |  | 1.21× | +3.1 | 0.17 | 20/48 (PANC-1, LS 180, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 11 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3619.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.728×** | -5.4 | 3e-05 | 36/47 (SW480, J82, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~36% of this change | **0.731×** | -5.3 | 3e-05 | 33/47 (H4, SNU-423, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **0.745×** | -4.7 | 4e-04 | 25/45 (NCI-H23, J82, …) | all doses, flat | composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.618×** | -4.4 | 0.001 | 31/45 (CFPAC-1, RPMI-7951, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.838× | -4.4 | 0.001 | 21/48 (CFPAC-1, Hs 766T, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.785×** | -4.2 | 0.002 | 31/48 (CFPAC-1, HCT15, …) | two highest doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.781×** | -4.2 | 0.002 | 30/48 (MIA PaCa-2, LoVo, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **0.787×** | -4.0 | 0.004 | 26/48 (A498, A549, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.655×** | -3.9 | 0.007 | 23/49 (RPMI-7951, CFPAC-1, …) | all doses, flat | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | 0.863× | -3.7 | 0.014 | 8/48 (HOP62, Hs 766T, …) | top dose only |  |
| [[Bendamustine (drug)]] 5 µM |  | **0.806×** | -3.6 | 0.014 | 23/48 (A-172, C32, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.804×** | -3.6 | 0.014 | 25/48 (CFPAC-1, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.678×** | -3.6 | 0.016 | 26/48 (AN3 CA, NCI-H460, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.819×** | -3.5 | 0.018 | 23/48 (CFPAC-1, HCT15, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **0.827×** | -3.3 | 0.031 | 26/49 (SW 1088, RKO, …) | all doses, flat | composition shift |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.834× | -3.0 | 0.075 | 17/47 (SW48, LOX-IMVI, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3619. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 216 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.87× (z +19.3) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[A549 (line)]] | wt | 155 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.552× (z -10.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 188 | 2 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.10× (z +12.8) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[H4 (line)]] | wt | 159 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.163× (z -15.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H23 (line)]] | alt | 140 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.102× (z -24.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SHP-77 (line)]] | alt | 100 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +13.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.62× (z +9.4) | — |
| [[SW 900 (line)]] | alt | 168 | 1 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.82× (z +9.9) ⚠ cell-cycle shift, explains ~0% of this change | [[Docetaxel (drug)]] 0.05 µM 0.487× (z -8.5) ⚠ transcription drop; cell-cycle shift, explains ~95% of this change |
| [[C32 (line)]] | wt | 138 | 1 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.13× (z +8.6) | — |
| [[CFPAC-1 (line)]] | alt | 284 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.502× (z -9.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 126 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.19× (z +10.0) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[HCT15 (line)]] | alt | 221 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.335× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[J82 (line)]] | alt | 104 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.378× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[LoVo (line)]] | wt | 106 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.70× (z +9.3) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H596 (line)]] | alt | 138 | 0 | 1 | — | [[Atazanavir (sulfate) (drug)]] 5 µM 0.168× (z -10.1) |
| [[SK-MEL-2 (line)]] | alt | 136 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.450× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SNU-1 (line)]] | wt | 115 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.135× (z -16.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW 1088 (line)]] | alt | 182 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0620× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 186 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.472× (z -9.8) ⚠ toxic |
| [[A-172 (line)]] | wt | 172 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 100 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 194 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 87.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 94.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 102 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 133 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 195 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 224 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 172 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 114 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 114 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 125 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 86.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 89.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 131 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 161 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 171 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 152 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 138 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 152 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 140 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 108 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 150 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 140 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 141 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 83.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 96.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3619), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*41 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC30A9]] | +0.57 | +0.28 / +0.67 | both halves | 3e-04 |  |
| [[LEPR]] | +0.55 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[CEP95]] | +0.53 | +0.57 / +0.43 | both halves | 3e-05 |  |
| [[AIDA]] | +0.53 | +0.41 / +0.58 | both halves | 4e-05 |  |
| [[SPTLC1]] | +0.53 | +0.34 / +0.58 | both halves | 1e-04 |  |
| [[CRYGS]] | +0.52 | +0.36 / +0.40 | both halves | 1e-04 |  |
| [[STYX]] | +0.52 | +0.44 / +0.56 | both halves | 3e-05 |  |
| [[ATXN1L]] | +0.52 | +0.35 / +0.54 | both halves | 1e-04 |  |
| [[ERVK13-1]] | +0.52 | +0.14 / +0.58 | ⚠ one half (not replicated) | 0.002 |  |
| [[RAB22A]] | +0.51 | +0.46 / +0.50 | both halves | 3e-05 |  |
| [[RO60]] | +0.51 | +0.39 / +0.44 | both halves | 5e-05 |  |
| [[C14orf28]] | +0.51 | +0.53 / +0.44 | both halves | 3e-05 |  |
| [[MTR]] | +0.51 | +0.43 / +0.52 | both halves | 3e-05 |  |

## Genes that move opposite

*59 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDIN1]] | -0.58 | -0.45 / -0.56 | both halves | 3e-05 |  |
| [[WDR7]] | -0.56 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[SLC25A12]] | -0.55 | -0.44 / -0.55 | both halves | 3e-05 |  |
| [[FAM133B]] | -0.55 | -0.33 / -0.59 | both halves | 1e-04 |  |
| [[MRPS26]] | -0.54 | -0.41 / -0.52 | both halves | 4e-05 |  |
| [[MRPL14]] | -0.54 | -0.33 / -0.60 | both halves | 1e-04 |  |
| [[MRPS34]] | -0.54 | -0.37 / -0.53 | both halves | 7e-05 |  |
| [[VWA8]] | -0.54 | -0.55 / -0.49 | both halves | 1e-05 | same gene group |
| [[THAP7]] | -0.53 | -0.46 / -0.52 | both halves | 2e-05 |  |
| [[ZNF420]] | -0.51 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[POLR3B]] | -0.51 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[PUS3]] | -0.51 | -0.30 / -0.58 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **-** arm (projection on the module's main direction -0.275). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-24.3, 19.7); signed map (-12.8, 16.8). **Vector** length 103, 30.3% of its response variance represented; |z| ≥ 3 in 835 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +6.2 | +4.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +6.2 | +2.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.3 | +4.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +4.9 | -3.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +4.4 | -2.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.5 | -0.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +1.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.9 | +3.2 |
|  | [[Vortioxetine (drug)]] 0.5 µM |  | +1.8 | +2.4 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +1.6 | +1.7 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -6.2 | -3.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -5.8 | -3.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.3 | -4.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -4.6 | -3.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.1 | -3.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.9 | -3.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.7 | -4.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.6 | -4.2 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 35 member F5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q14.1 — chr2:113,705,011-113,756,693 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ22004 |
| Gene groups (HGNC) | MicroRNA protein coding host genes; Solute carrier family 35 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WV83](https://www.uniprot.org/uniprotkb/Q8WV83) (Solute carrier family 35 member F5):

> Mediates choline transport, although the underlying transport mechanism remains to be elucidated.

**Summary**, from NCBI Gene [80255](https://www.ncbi.nlm.nih.gov/gene/80255):

> Enables choline transmembrane transporter activity. Involved in choline transport. Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:23617](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23617) · Entrez [80255](https://www.ncbi.nlm.nih.gov/gene/80255) · UniProt [Q8WV83](https://www.uniprot.org/uniprotkb/Q8WV83) · Ensembl [ENSG00000115084](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115084)

## Data

Gene col 3619: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3619); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3619, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3619]; `tensor/DDL_lfc|DDL_z.npy` [3619]; `embed/gene_vectors.npy` [3619]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3619 or target_col == 3619). Every well: [[SLC35F5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC35F5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
