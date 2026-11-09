---
symbol: "SELENOO"
type: "gene"
col: 1045
ensembl_id: "ENSG00000073169"
name: "selenoprotein O"
location: "22q13.33"
module: 3
arm: "+"
pooled_cpm: 22.71
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 2
n_dd_up_clean: 11
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# SELENOO

*selenoprotein O* — 22q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.74× (z +12.5, q 4e-33, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.657× (z -9.1, q 4e-17, down in 20 of 35 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 0.5 µM: 0.754× (z -5.1, q 6e-05, down in 16 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (NCI-H460 0.146×, hTERT-HPNE 0.131×, HCT15 0.199×, NCI-H1573 0.324×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (A498 0.235×, HEC-1-A 0.302×, MIA PaCa-2 0.251×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SHP-77 0.359×, MIA PaCa-2 0.346×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Flutamide (drug)]] 0.5 µM in 1 line (AN3 CA 0.0897×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCNQ]] (+0.65, fdr 3e-05), [[SIRT7]] (+0.62, fdr 2e-05), [[CDC34]] (+0.62, fdr 5e-05); moves opposite to [[ARL5B]] (-0.62, fdr 1e-05), [[STK26]] (-0.55, fdr 2e-04), [[QPCT]] (-0.55, fdr 6e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1045.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.74×** | +12.5 | 4e-33 | 39/48 (SW480, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.70×** | +11.9 | 2e-30 | 35/48 (SW480, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.50×** | +9.1 | 1e-17 | 34/47 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.52×** | +7.5 | 8e-12 | 23/46 (HS-578T, HOP62, …) | all doses, flat | cell-cycle shift (explains ~1% here); noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.19× | +5.6 | 3e-06 | 19/48 (LS 180, A498, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.28×** | +5.5 | 3e-06 | 20/48 (HEC-1-A, LoVo, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.28×** | +5.3 | 8e-06 | 20/44 (NCI-H23, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.26×** | +5.2 | 2e-05 | 19/47 (SW480, HT-29, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.46×** | +4.4 | 6e-04 | 8/29 (HEC-1-A, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.30×** | +4.3 | 0.001 | 10/46 (HS-578T, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.43×** | +4.2 | 0.001 | 11/41 (SW480, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.21×** | +4.1 | 0.002 | 15/47 (LOX-IMVI, A-172, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | 1.13× | +3.9 | 0.004 | 16/47 (HS-578T, NCI-H1792, …) | all doses, flat | composition shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.12× | +3.7 | 0.008 | 9/48 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.25×** | +3.6 | 0.010 | 10/45 (LoVo, NCI-H23, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **1.25×** | +3.6 | 0.011 | 8/47 (NCI-H1573, NCI-H1792, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Neratinib (drug)]] 5 µM |  | 1.17× | +3.5 | 0.014 | 5/47 (NCI-H2030, NCI-H460, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.22×** | +3.2 | 0.038 | 7/46 (HT-29, HS-578T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.15× | +3.2 | 0.043 | 7/48 (NCI-H2347, HOP62, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1045.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (NCI-H460 0.146×, hTERT-HPNE 0.131×, HCT15 0.199×, NCI-H1573 0.324×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (A498 0.235×, HEC-1-A 0.302×, MIA PaCa-2 0.251×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SHP-77 0.359×, MIA PaCa-2 0.346×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Flutamide (drug)]] 0.5 µM in 1 line (AN3 CA 0.0897×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.657×** | -9.1 | 4e-17 | 20/35 (NCI-H460, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.932× | -5.3 | 4e-05 | 1/48 (COLO 205) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.754×** | -5.1 | 6e-05 | 16/47 (HCT15, SW48, …) | two highest doses | cell-cycle shift (explains ~1% here); noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.894× | -3.6 | 0.045 | 7/48 (HCT15, SW 900, …) | two highest doses |  |
| [[Sunitinib (drug)]] 0.5 µM |  | 0.865× | -3.3 | 0.12 | 6/48 (HepG2/C3A, SNU-1, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | 0.769× | -3.1 | 0.18 | 14/48 (H4, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.874× | -3.1 | 0.18 | 19/41 (SHP-77, MIA PaCa-2, …) | rises with dose | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1045. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AN3 CA (line)]] | alt | 27.7 | 0 | 2 (1 ⚠) | — | [[Sunitinib (drug)]] 5 µM 0.0796× (z -9.8) ⚠ toxic · without an alert: [[Flutamide (drug)]] 0.5 µM 0.0897× (z -9.3) |
| [[HS-578T (line)]] | alt | 23.1 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.83× (z +11.6) ⚠ cell-cycle shift, explains ~6% of this change | [[Dinaciclib (drug)]] 5 µM 0.318× (z -8.8) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 25.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.251× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 27.5 | 1 | 1 (1 ⚠) | [[Belinostat (drug)]] 5 µM 2.26× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.441× (z -8.6) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 20.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.235× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 16.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.291× (z -8.6) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 41.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.199× (z -10.9) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 33.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.302× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[hTERT-HPNE (line)]] | wt | 22.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.131× (z -11.5) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 30.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.324× (z -10.0) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 21.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +9.6) ⚠ cell-cycle shift, explains ~6% of this change | — |
| [[NCI-H460 (line)]] | wt | 18.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.146× (z -16.3) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 47.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.359× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 23.1 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 30.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 33.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 21.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 23.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 28.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1045), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCNQ]] | +0.65 | +0.43 / +0.64 | both halves | 3e-05 |  |
| [[SIRT7]] | +0.62 | +0.46 / +0.62 | both halves | 2e-05 |  |
| [[CDC34]] | +0.62 | +0.39 / +0.60 | both halves | 5e-05 |  |
| [[C1orf35]] | +0.62 | +0.46 / +0.63 | both halves | 2e-05 |  |
| [[ENKD1]] | +0.60 | +0.36 / +0.62 | both halves | 1e-04 |  |
| [[NELFB]] | +0.60 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[ATG4B]] | +0.59 | +0.27 / +0.64 | both halves | 3e-04 |  |
| [[ZNF500]] | +0.59 | +0.48 / +0.68 | both halves | 2e-05 |  |
| [[ARL8A]] | +0.59 | +0.46 / +0.65 | both halves | 3e-05 |  |
| [[MEX3D]] | +0.59 | +0.43 / +0.58 | both halves | 3e-05 |  |
| [[ZNF765]] | +0.59 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[WRAP73]] | +0.58 | +0.41 / +0.56 | both halves | 4e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARL5B]] | -0.62 | -0.50 / -0.66 | both halves | 1e-05 |  |
| [[STK26]] | -0.55 | -0.30 / -0.57 | both halves | 2e-04 |  |
| [[QPCT]] | -0.55 | -0.41 / -0.39 | both halves | 6e-05 |  |
| [[EXTL2]] | -0.54 | -0.38 / -0.47 | both halves | 7e-05 |  |
| [[SEPTIN11]] | -0.53 | -0.29 / -0.54 | both halves | 2e-04 |  |
| [[GALNT7]] | -0.53 | -0.28 / -0.49 | both halves | 3e-04 |  |
| [[NXT2]] | -0.52 | -0.39 / -0.44 | both halves | 6e-05 |  |
| [[ITGAV]] | -0.52 | -0.33 / -0.52 | both halves | 1e-04 |  |
| [[LYRM1]] | -0.52 | -0.22 / -0.50 | both halves | 6e-04 |  |
| [[NAB1]] | -0.52 | -0.38 / -0.56 | both halves | 7e-05 |  |
| [[ABLIM1]] | -0.52 | -0.37 / -0.53 | both halves | 7e-05 |  |
| [[SLC12A2]] | -0.51 | -0.34 / -0.52 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.591). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-38.5, -16.0); signed map (-24.5, 6.9). **Vector** length 67.0, 10.7% of its response variance represented; |z| ≥ 3 in 727 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +3.3 | +12.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.8 | +11.9 |
|  | [[Belinostat (drug)]] 5 µM |  | +2.7 | +9.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.5 | +5.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.2 | +3.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.9 | +3.7 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +1.7 | +5.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.7 | +3.2 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.1 | -0.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -4.1 | -3.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -4.0 | -5.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.9 | -3.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.7 | -9.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.8 | -1.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.6 | -1.5 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.4 | -1.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.2 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | selenoprotein O |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.33 — chr22:50,201,011-50,217,616 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SELO |
| Gene groups (HGNC) | Selenoproteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BVL4](https://www.uniprot.org/uniprotkb/Q9BVL4) (Protein adenylyltransferase SelO, mitochondrial):

> Catalyzes the transfer of adenosine 5'-monophosphate (AMP) to Ser, Thr and Tyr residues of target proteins (AMPylation). May be a redox-active mitochondrial selenoprotein which interacts with a redox target protein.

**Summary**, from NCBI Gene [83642](https://www.ncbi.nlm.nih.gov/gene/83642):

> This gene encodes a selenoprotein that is localized to the mitochondria. It is the largest mammalian selenoprotein, containing the rare amino acid selenocysteine (Sec). Sec is encoded by the UGA codon, which normally signals translation termination. The 3' UTRs of selenoprotein mRNAs contain a conserved stem-loop structure, designated the Sec insertion sequence (SECIS) element, that is necessary for the recognition of UGA as a Sec codon, rather than as a stop signal. The exact function of this …

**Accessions** — [HGNC:30395](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30395) · Entrez [83642](https://www.ncbi.nlm.nih.gov/gene/83642) · UniProt [Q9BVL4](https://www.uniprot.org/uniprotkb/Q9BVL4) · Ensembl [ENSG00000073169](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000073169)

## Data

Gene col 1045: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1045); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1045, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1045]; `tensor/DDL_lfc|DDL_z.npy` [1045]; `embed/gene_vectors.npy` [1045]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1045 or target_col == 1045). Every well: [[SELENOO — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SELENOO.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
