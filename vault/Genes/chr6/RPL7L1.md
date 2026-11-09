---
symbol: "RPL7L1"
type: "gene"
col: 7073
ensembl_id: "ENSG00000146223"
name: "ribosomal protein L7 like 1"
location: "6p21.1"
module: 11
arm: "+"
pooled_cpm: 85.73
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 0
n_dd_up_clean: 12
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# RPL7L1

*ribosomal protein L7 like 1* — 6p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 2.25× (z +10.5, q 6e-23, up in 42 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (COLO 205 0.362×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (RKO 0.381×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NOL8]] (+0.83, fdr 7e-06), [[GPATCH4]] (+0.78, fdr 7e-06), [[UTP3]] (+0.76, fdr 7e-06); moves opposite to [[LAPTM4A]] (-0.71, fdr 7e-06), [[SEC11A]] (-0.70, fdr 7e-06), [[TM9SF2]] (-0.69, fdr 7e-06).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7073.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.25×** | +10.5 | 6e-23 | 42/48 (LOX-IMVI, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.15×** | +9.9 | 2e-20 | 45/48 (LOX-IMVI, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.11×** | +9.3 | 3e-18 | 38/44 (SNU-423, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.05×** | +8.9 | 9e-17 | 42/47 (KATO III, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.99×** | +8.6 | 1e-15 | 46/48 (COLO 205, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **1.91×** | +8.3 | 8e-15 | 40/49 (SNU-423, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.58×** | +8.3 | 9e-15 | 38/48 (COLO 205, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.71×** | +6.9 | 3e-10 | 47/48 (LOX-IMVI, PANC-1, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.66×** | +6.5 | 4e-09 | 41/48 (LOX-IMVI, BT-474, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.48×** | +4.7 | 2e-04 | 35/47 (LOX-IMVI, NCI-H460, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.41×** | +4.4 | 5e-04 | 31/48 (HOP62, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.25×** | +4.0 | 0.003 | 29/48 (A549, HS-578T, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~55% of this change | **1.34×** | +3.8 | 0.006 | 30/48 (HOP62, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.09× | +3.8 | 0.006 | 0/50 | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.35×** | +3.7 | 0.009 | 32/48 (NCI-H1792, NCI-H2347, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.22×** | +3.6 | 0.013 | 24/48 (A-172, CFPAC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 0.05 µM |  | **1.34×** | +3.4 | 0.019 | 30/48 (NCI-H460, HOP62, …) | all doses, flat |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.28×** | +3.2 | 0.043 | 28/47 (HOP62, NCI-H460, …) | all doses, flat |  |
| [[Pralsetinib (drug)]] 5 µM |  | **1.55×** | +3.0 | 0.090 | 20/48 (NCI-H460, NCI-H2347, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (COLO 205 0.362×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (RKO 0.381×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, +0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7073. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 56.0 | 7 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.47× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.03× (z +9.7) | — |
| [[SNU-423 (line)]] | alt | 109 | 7 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.97× (z +13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.62× (z +9.4) | — |
| [[A549 (line)]] | wt | 46.3 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +12.2) ⚠ cell-cycle shift, explains ~51% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 3.45× (z +10.5) | — |
| [[COLO 205 (line)]] | alt | 411 | 5 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.78× (z +13.6) | [[Dinaciclib (drug)]] 0.5 µM 0.362× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[LOX-IMVI (line)]] | wt | 91.4 | 6 (2 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 4.03× (z +14.5) | — |
| [[HOP62 (line)]] | alt | 68.6 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.85× (z +13.1) | — |
| [[NCI-H1792 (line)]] | alt | 58.0 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.70× (z +12.8) | — |
| [[NCI-H2347 (line)]] | alt | 60.3 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +11.7) ⚠ cell-cycle shift, explains ~51% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.23× (z +11.4) | — |
| [[PANC-1 (line)]] | alt | 118 | 4 (1 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 2.83× (z +11.2) | — |
| [[HT-29 (line)]] | alt | 68.8 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.75× (z +10.8) | — |
| [[SW480 (line)]] | alt | 119 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.64× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.54× (z +9.6) | — |
| [[A-172 (line)]] | wt | 47.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.16× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[A498 (line)]] | wt | 55.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.95× (z +8.8) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 38.8 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.49× (z +8.7) | — |
| [[CFPAC-1 (line)]] | alt | 66.1 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.28× (z +11.0) | — |
| [[H4 (line)]] | wt | 82.1 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.53× (z +9.0) | — |
| [[Hs 766T (line)]] | wt | 41.8 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.16× (z +8.5) | — |
| [[KATO III (line)]] | alt | 98.8 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.04× (z +10.9) ⚠ toxic | — |
| [[LoVo (line)]] | wt | 77.4 | 1 | 0 | [[Homoharringtonine (drug)]] 0.05 µM 2.64× (z +8.9) | — |
| [[NCI-H23 (line)]] | alt | 175 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.55× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[Panc 03.27 (line)]] | alt | 120 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.72× (z +9.1) | — |
| [[RKO (line)]] | wt | 162 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.381× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[SW1417 (line)]] | alt | 78.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.40× (z +9.1) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 96.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 96.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 90.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 112 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 52.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 94.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 79.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 90.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 60.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 75.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 76.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 80.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 64.9 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 63.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 75.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 71.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 75.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 70.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 86.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 62.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 81.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 50.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 97.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7073), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NOL8]] | +0.83 | +0.84 / +0.81 | both halves | 7e-06 |  |
| [[GPATCH4]] | +0.78 | +0.79 / +0.74 | both halves | 7e-06 |  |
| [[UTP3]] | +0.76 | +0.82 / +0.69 | both halves | 7e-06 | STRING 443 |
| [[RPP38]] | +0.75 | +0.80 / +0.70 | both halves | 7e-06 | STRING 656 |
| [[CCDC137]] | +0.74 | +0.85 / +0.69 | both halves | 7e-06 |  |
| [[CEBPZ]] | +0.74 | +0.80 / +0.78 | both halves | 7e-06 | STRING 582 |
| [[ZNF146]] | +0.73 | +0.66 / +0.76 | both halves | 7e-06 |  |
| [[MGA]] | +0.72 | +0.73 / +0.69 | both halves | 7e-06 |  |
| [[ZNF830]] | +0.72 | +0.78 / +0.58 | both halves | 7e-06 |  |
| [[ARL14EP]] | +0.71 | +0.77 / +0.62 | both halves | 7e-06 |  |
| [[INTS14]] | +0.71 | +0.71 / +0.60 | both halves | 7e-06 |  |
| [[ZC3HC1]] | +0.71 | +0.64 / +0.72 | both halves | 7e-06 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LAPTM4A]] | -0.71 | -0.76 / -0.65 | both halves | 7e-06 |  |
| [[SEC11A]] | -0.70 | -0.76 / -0.58 | both halves | 7e-06 |  |
| [[TM9SF2]] | -0.69 | -0.75 / -0.63 | both halves | 7e-06 |  |
| [[IGSF8]] | -0.68 | -0.71 / -0.51 | both halves | 1e-05 |  |
| [[AP2A1]] | -0.67 | -0.69 / -0.57 | both halves | 9e-06 |  |
| [[SEC61A2]] | -0.67 | -0.60 / -0.68 | both halves | 7e-06 | STRING 832 |
| [[ABHD12]] | -0.66 | -0.68 / -0.57 | both halves | 1e-05 |  |
| [[TMEM50B]] | -0.66 | -0.57 / -0.65 | both halves | 9e-06 |  |
| [[IFI27L1]] | -0.65 | -0.64 / -0.59 | both halves | 7e-06 |  |
| [[STRN]] | -0.65 | -0.76 / -0.44 | both halves | 3e-05 |  |
| [[UBTD1]] | -0.64 | -0.73 / -0.53 | both halves | 1e-05 |  |
| [[GTF2IP4]] | -0.64 | -0.61 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.799). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-37.1, 6.8); signed map (0.4, -21.1). **Vector** length 113, 39.7% of its response variance represented; |z| ≥ 3 in 827 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +10.3 | +10.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +9.3 | +9.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +8.2 | +8.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +7.8 | +6.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | +6.4 | +8.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.8 | +4.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.7 | +6.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.5 | +3.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | +4.0 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.9 | -0.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.5 | -2.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.2 | -1.1 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.0 | -1.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | -4.0 | +3.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.9 | -2.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.2 | -0.6 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.0 | -0.7 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | -1.8 | -0.7 |
|  | [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.05 µM |  | -1.4 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | ribosomal protein L7 like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.1 — chr6:42,879,616-42,889,925 (+) |
| Ensembl biotype | protein_coding |
| Also known as | dJ475N16.4 |
| Gene groups (HGNC) | L ribosomal proteins |
| Matched by | ensembl_id |

UniProt [Q6DKI1](https://www.uniprot.org/uniprotkb/Q6DKI1) carries no function annotation.

**Summary**, from NCBI Gene [285855](https://www.ncbi.nlm.nih.gov/gene/285855):

> Enables RNA binding activity. Predicted to be involved in maturation of LSU-rRNA from tricistronic rRNA transcript (SSU-rRNA, 5.8S rRNA, LSU-rRNA). Predicted to act upstream of or within blastocyst formation. Located in mitochondrion. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:21370](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21370) · Entrez [285855](https://www.ncbi.nlm.nih.gov/gene/285855) · UniProt [Q6DKI1](https://www.uniprot.org/uniprotkb/Q6DKI1) · Ensembl [ENSG00000146223](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000146223)

## Data

Gene col 7073: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7073); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7073, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7073]; `tensor/DDL_lfc|DDL_z.npy` [7073]; `embed/gene_vectors.npy` [7073]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7073 or target_col == 7073). Every well: [[RPL7L1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPL7L1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
