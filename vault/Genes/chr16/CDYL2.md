---
symbol: "CDYL2"
type: "gene"
col: 9308
ensembl_id: "ENSG00000166446"
name: "chromodomain Y like 2"
location: "16q23.2"
module: 34
arm: "+"
pooled_cpm: 24.18
n_lines_expressing: 31
n_dd_up: 16
n_dd_down: 15
n_dd_up_clean: 14
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 5
direction_downstream: 12
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# CDYL2

*chromodomain Y like 2* — 16q23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (2 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.96× (z +13.8, q 2e-40, up in 22 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (5 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.578× (z -7.9, q 1e-12, down in 18 of 28 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PLEK2]] (+0.63, fdr 7e-06), [[CORO2B]] (+0.62, fdr 1e-05), [[ABTB3]] (+0.62, fdr 1e-05); moves opposite to [[GTF2IRD2B]] (-0.54, fdr 3e-05), [[ARFGEF2]] (-0.53, fdr 3e-05), [[TMEM91]] (-0.53, fdr 7e-05).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); 12 go from it, the strongest it → [[APBB2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 2 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9308.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.96×** | +13.8 | 2e-40 | 22/29 (NCI-H460, RKO, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.61×** | +6.9 | 1e-09 | 19/28 (NCI-H460, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.57×** | +6.5 | 1e-08 | 17/28 (NCI-H460, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.46×** | +5.5 | 6e-06 | 11/28 (CFPAC-1, LS 180, …) | top dose only |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.91×** | +4.9 | 1e-04 | 12/27 (SW480, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.38×** | +4.6 | 4e-04 | 16/28 (LOX-IMVI, HOP62, …) | all doses, flat | low cells (technical?) |
| [[Belinostat (drug)]] 5 µM |  | **1.36×** | +4.4 | 8e-04 | 7/28 (NCI-H1573, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.75×** | +4.2 | 0.002 | 12/29 (A-427, NCI-H1573, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.74×** | +4.2 | 0.002 | 8/24 (SW480, SNU-423, …) | top dose only | cell-cycle shift (explains ~25% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.29×** | +3.7 | 0.014 | 6/28 (NCI-H1573, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[BAY1125976 (drug)]] 5 µM |  | **1.58×** | +3.5 | 0.027 | 10/29 (SW480, Hs 766T, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.27×** | +3.4 | 0.027 | 8/28 (CFPAC-1, AsPC-1, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.18× | +3.4 | 0.030 | 8/29 (SW 900, NCI-H460, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.26×** | +3.3 | 0.033 | 7/28 (LoVo, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.27×** | +3.3 | 0.036 | 11/28 (LOX-IMVI, hTERT-HPNE, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.25×** | +3.2 | 0.047 | 7/28 (NCI-H1573, HCT15, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Neratinib (drug)]] 5 µM |  | **1.23×** | +3.0 | 0.088 | 7/28 (NCI-H460, SW 900, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 5 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9308.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.578×** | -7.9 | 1e-12 | 18/28 (NCI-H2030, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.687×** | -7.7 | 5e-12 | 19/29 (LOX-IMVI, NCI-H1573, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.662×** | -5.9 | 5e-07 | 19/27 (LOX-IMVI, NCI-H1792, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.702×** | -5.1 | 5e-05 | 16/27 (LOX-IMVI, NCI-H1573, …) | rises with dose |  |
| [[Sulfatinib (drug)]] 5 µM |  | **0.713×** | -4.7 | 3e-04 | 16/28 (A549, HOP62, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.715×** | -4.7 | 3e-04 | 18/27 (BT-474, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.551×** | -4.5 | 6e-04 | 12/26 (hTERT-HPNE, A-172, …) | top dose only | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.571×** | -4.2 | 0.002 | 14/28 (AsPC-1, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.747×** | -4.2 | 0.002 | 16/22 (LoVo, NCI-H1792, …) | inconsistent across doses | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.826×** | -3.9 | 0.006 | 17/29 (NCI-H1792, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.767×** | -3.8 | 0.007 | 12/28 (AsPC-1, Hs 766T, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.801×** | -3.2 | 0.061 | 8/28 (NCI-H460, HOP62, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.05 µM |  | **0.787×** | -3.2 | 0.061 | 14/28 (NCI-H460, Hs 766T, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.830×** | -3.1 | 0.068 | 7/29 (Hs 766T, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[LJI308 (drug)]] 0.05 µM |  | **0.799×** | -3.1 | 0.084 | 10/28 (A-172, LS 180, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, -0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9308. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 61.1 | 0 | 10 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0966× (z -26.4) ⚠ cell-cycle shift, explains ~56% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.288× (z -9.6) |
| [[LoVo (line)]] | wt | 63.3 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0756× (z -20.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[NCI-H2030 (line)]] | alt | 43.8 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.137× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.204× (z -9.8) |
| [[A-172 (line)]] | wt | 42.4 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.211× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.373× (z -11.3) |
| [[NCI-H1792 (line)]] | alt | 122 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -14.6) ⚠ cell-cycle shift, explains ~56% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.321× (z -14.2) |
| [[HOP62 (line)]] | alt | 41.9 | 0 | 2 (2 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.574× (z -14.1) ⚠ position not correctable |
| [[J82 (line)]] | alt | 51.1 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.367× (z -12.1) |
| [[NCI-H1573 (line)]] | alt | 23.4 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.124× (z -18.3) ⚠ cell-cycle shift, explains ~56% of this change |
| [[SW480 (line)]] | alt | 72.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.248× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[A549 (line)]] | wt | 12.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -8.6) ⚠ cell-cycle shift, explains ~56% of this change |
| [[AsPC-1 (line)]] | alt | 30.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.210× (z -13.5) ⚠ cell-cycle shift, explains ~56% of this change |
| [[BT-474 (line)]] | alt | 80.1 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.149× (z -10.7) |
| [[H4 (line)]] | wt | 35.7 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0778× (z -11.1) ⚠ transcription drop; cell-cycle shift, explains ~89% of this change |
| [[Hs 766T (line)]] | wt | 24.9 | 0 | 1 | — | [[Regorafenib (drug)]] 5 µM 0.0334× (z -9.4) |
| [[NCI-H460 (line)]] | wt | 11.8 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.53× (z +10.0) | — |
| [[RKO (line)]] | wt | 8.32 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 5.07× (z +8.5) | — |
| [[SW 900 (line)]] | alt | 41.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.238× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW1417 (line)]] | alt | 29.0 | 1 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 2.35× (z +9.4) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[A-427 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.95 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 4.42 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.76 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.93 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.41 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.55 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.33 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.96 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.23 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 36.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.06 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 23.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.57 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.72 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.85 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.25 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 4.86 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.78 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 4.06 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.85 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.35 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.65 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 6.43 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.76 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.07 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9308), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLEK2]] | +0.63 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[CORO2B]] | +0.62 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[ABTB3]] | +0.62 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[DOCK9]] | +0.60 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[PLEKHG5]] | +0.59 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[GPRIN1]] | +0.59 | +0.65 / +0.53 | both halves | 1e-05 |  |
| [[FAM124A]] | +0.58 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[NLRP3]] | +0.58 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[MAMLD1]] | +0.58 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[ATP13A2]] | +0.58 | +0.65 / +0.46 | both halves | 2e-05 |  |
| [[MICAL1]] | +0.56 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[GLI2]] | +0.56 | +0.55 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GTF2IRD2B]] | -0.54 | -0.63 / -0.43 | both halves | 3e-05 |  |
| [[ARFGEF2]] | -0.53 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[TMEM91]] | -0.53 | -0.55 / -0.37 | both halves | 7e-05 |  |
| [[MCCC1]] | -0.50 | -0.49 / -0.46 | both halves | 2e-05 | STRING 410 |
| [[GTF2IRD2]] | -0.50 | -0.57 / -0.40 | both halves | 5e-05 |  |
| [[PPP4R3B]] | -0.50 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[ZNF608]] | -0.50 | -0.55 / -0.41 | both halves | 4e-05 |  |
| [[RBKS]] | -0.50 | -0.54 / -0.41 | both halves | 4e-05 |  |
| [[SPATA24]] | -0.49 | -0.53 / -0.35 | both halves | 1e-04 |  |
| [[TBCK]] | -0.48 | -0.52 / -0.46 | both halves | 3e-05 |  |
| [[DNAJC27]] | -0.48 | -0.51 / -0.39 | both halves | 6e-05 |  |
| [[PRELID2]] | -0.48 | -0.36 / -0.53 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises CDYL2's level | compounds that target MAP2K1: 4 of 4 lower it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 3.9% of all compounds | 0.010 | ⚠ off-target possible; 4 compounds |
| [[TOR4A]] | B | TOR4A activity raises CDYL2's level | lines that do not express TOR4A (14) vs lines expressing it (36) | 2.35× lower at baseline in the lines without TOR4A | 0.034 | ⚠ within organs, on part of the lines; also absent: PLEKHA6, CDCP1, C19orf33 |
| [[RASSF8]] | B | RASSF8 activity raises CDYL2's level | lines that do not express RASSF8 (15) vs lines expressing it (35) | 1.79× lower at baseline in the lines without RASSF8 | 0.071 | ⚠ within organs, on part of the lines; also absent: RASSF8-AS1, KCNG1, B4GALNT1 |
| [[AMOTL1]] | B | AMOTL1 activity raises CDYL2's level | lines that do not express AMOTL1 (16) vs lines expressing it (34) | 1.93× lower at baseline in the lines without AMOTL1 | 0.080 | ⚠ within organs, on part of the lines; also absent: ENSG00000289526, RNF150, NALCN |
| [[NLRP3]] | B | NLRP3 activity raises CDYL2's level | lines that do not express NLRP3 (28) vs lines expressing it (22) | 2.60× lower at baseline in the lines without NLRP3 | 0.084 | ⚠ within organs, on part of the lines; also absent: FLI1, APCDD1L, MME |

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 10, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[APBB2]] | B | CDYL2 activity raises APBB2's level | lines that do not express CDYL2 (19) vs lines expressing it (31) | 1.41× lower at baseline in the lines without CDYL2 | 0.041 | ⚠ within organs, on part of the lines; also absent: B3GALT5, BCL11B, ENSG00000225330 |
| [[NLRP3]] | B | CDYL2 activity raises NLRP3's level | lines that do not express CDYL2 (19) vs lines expressing it (31) | 2.00× lower at baseline in the lines without CDYL2 | 0.060 | ⚠ within organs, on part of the lines; also absent: B3GALT5, BCL11B, ENSG00000225330 |
| [[TOR4A]] | B | CDYL2 activity raises TOR4A's level | lines that do not express CDYL2 (19) vs lines expressing it (31) | 2.10× lower at baseline in the lines without CDYL2 | 0.061 | ⚠ within organs, on part of the lines; also absent: B3GALT5, BCL11B, ENSG00000225330 |
| [[PPP2R2C]] | B | CDYL2 activity raises PPP2R2C's level | lines that do not express CDYL2 (19) vs lines expressing it (31) | 1.72× lower at baseline in the lines without CDYL2 | 0.072 | ⚠ within organs, on part of the lines; also absent: B3GALT5, BCL11B, ENSG00000225330 |
| [[PLEKHG5]] | B | CDYL2 activity raises PLEKHG5's level | lines that do not express CDYL2 (19) vs lines expressing it (31) | 1.84× lower at baseline in the lines without CDYL2 | 0.080 | ⚠ within organs, on part of the lines; also absent: B3GALT5, BCL11B, ENSG00000225330 |
| [[S100A16]] | B | CDYL2 activity raises S100A16's level | lines that do not express CDYL2 (19) vs lines expressing it (31) | 2.29× lower at baseline in the lines without CDYL2 | 0.085 | ⚠ within organs, on part of the lines; also absent: B3GALT5, BCL11B, ENSG00000225330 |
| [[TMCC3]] | B | CDYL2 activity raises TMCC3's level | lines that do not express CDYL2 (19) vs lines expressing it (31) | 2.23× lower at baseline in the lines without CDYL2 | 0.089 | ⚠ within organs, on part of the lines; also absent: B3GALT5, BCL11B, ENSG00000225330 |
| [[MAP4K4]] | B | CDYL2 activity raises MAP4K4's level | lines that do not express CDYL2 (19) vs lines expressing it (31) | 1.42× lower at baseline in the lines without CDYL2 | 0.091 | ⚠ within organs, on part of the lines; also absent: B3GALT5, BCL11B, ENSG00000225330 |
| [[ABCC10]] | B | CDYL2 activity lowers ABCC10's level | lines that do not express CDYL2 (19) vs lines expressing it (31) | 1.21× higher at baseline in the lines without CDYL2 | 0.093 | ⚠ within organs, on part of the lines; also absent: B3GALT5, BCL11B, ENSG00000225330 |
| [[C3orf52]] | B | CDYL2 activity raises C3orf52's level | lines that do not express CDYL2 (19) vs lines expressing it (31) | 2.16× lower at baseline in the lines without CDYL2 | 0.093 | ⚠ within organs, on part of the lines; also absent: B3GALT5, BCL11B, ENSG00000225330 |
| [[PLEK2]] | C | CDYL2 activity raises PLEK2's level | lines that do not express CDYL2 (19) vs lines expressing it (31) | 3.38× lower at baseline in the lines without CDYL2 | 0.036 | ⚠ within organs, on part of the lines; also absent: B3GALT5, BCL11B, ENSG00000225330; co-absent with the target |
| [[ABTB3]] | C | CDYL2 activity raises ABTB3's level | lines that do not express CDYL2 (19) vs lines expressing it (31) | 3.03× lower at baseline in the lines without CDYL2 | 0.055 | ⚠ within organs, on part of the lines; also absent: B3GALT5, BCL11B, ENSG00000225330; co-absent with the target |

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.575). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (45.8, 3.5); signed map (0.1, 52.4). **Vector** length 80.7, 20.6% of its response variance represented; |z| ≥ 3 in 757 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.1 | +13.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.5 | +6.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.9 | +5.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.8 | +6.9 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.4 | +3.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.2 | +4.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.8 | +4.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.8 | +1.8 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.8 | -7.9 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | -1.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | -2.3 | -7.7 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.3 | -3.1 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -2.2 | -4.5 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | -2.2 | -1.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.2 | -4.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.1 | -2.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.1 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | chromodomain Y like 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q23.2 — chr16:80,597,907-80,804,598 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ38866 |
| Matched by | ensembl_id |

UniProt [Q8N8U2](https://www.uniprot.org/uniprotkb/Q8N8U2) carries no function annotation.

**Summary**, from NCBI Gene [124359](https://www.ncbi.nlm.nih.gov/gene/124359):

> Predicted to enable transcription corepressor activity. Predicted to be involved in chromatin organization and negative regulation of DNA-templated transcription. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:23030](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23030) · Entrez [124359](https://www.ncbi.nlm.nih.gov/gene/124359) · UniProt [Q8N8U2](https://www.uniprot.org/uniprotkb/Q8N8U2) · Ensembl [ENSG00000166446](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166446)

## Data

Gene col 9308: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9308); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9308, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9308]; `tensor/DDL_lfc|DDL_z.npy` [9308]; `embed/gene_vectors.npy` [9308]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9308 or target_col == 9308). Every well: [[CDYL2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDYL2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
