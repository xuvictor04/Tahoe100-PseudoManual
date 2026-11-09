---
symbol: "PDZD11"
type: "gene"
col: 4187
ensembl_id: "ENSG00000120509"
name: "PDZ domain containing 11"
location: "Xq13.1"
module: 3
arm: "+"
pooled_cpm: 14.79
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 1
n_dd_up_clean: 7
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# PDZD11

*PDZ domain containing 11* — Xq13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.37× (z +14.2, q 6e-43, up in 37 of 37 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 1.42× (z +4.1, q 0.003, up in 19 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.678× (z -6.4, q 9e-08, down in 31 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (AsPC-1 0.306×, SK-MEL-2 0.316×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EMC4]] (+0.67, fdr 7e-06), [[CETN2]] (+0.60, fdr 6e-05), [[PIN1]] (+0.57, fdr 1e-04); moves opposite to [[SNHG26]] (-0.59, fdr 4e-05), [[KCNQ4]] (-0.56, fdr 9e-05), [[E2F5]] (-0.55, fdr 3e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 10 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4187.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **3.37×** | +14.2 | 6e-43 | 37/37 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **3.41×** | +13.8 | 1e-40 | 24/25 (NCI-H460, A498, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **2.37×** | +9.3 | 3e-18 | 25/31 (SNU-423, SK-MEL-2, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.58×** | +5.4 | 1e-05 | 28/48 (NCI-H23, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.57×** | +5.2 | 2e-05 | 30/48 (SW480, PANC-1, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~39% of this change | **1.51×** | +4.8 | 2e-04 | 19/42 (Panc 03.27, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.30×** | +4.3 | 0.001 | 19/46 (A549, NCI-H2347, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.42×** | +4.1 | 0.003 | 19/47 (A-427, HOP62, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | **1.42×** | +3.9 | 0.006 | 17/40 (MIA PaCa-2, NCI-H23, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~82% of this change | **1.38×** | +3.8 | 0.009 | 17/47 (SW480, HepG2/C3A, …) | rises with dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.55×** | +3.5 | 0.020 | 11/40 (SW480, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Infigratinib (drug)]] 0.05 µM |  | **1.34×** | +3.2 | 0.063 | 10/48 (SNU-423, HEC-1-A, …) | inconsistent across doses | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.33×** | +3.2 | 0.070 | 13/47 (SNU-423, MIA PaCa-2, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.21×** | +3.1 | 0.075 | 12/48 (HEC-1-A, SW480, …) | top dose only |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.46×** | +3.0 | 0.089 | 12/44 (NCI-H1792, HT-29, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **1.45×** | +3.0 | 0.090 | 8/45 (CFPAC-1, HT-29, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.45×** | +3.0 | 0.099 | 11/46 (SW1417, SW 900, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4187.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (AsPC-1 0.306×, SK-MEL-2 0.316×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.678×** | -6.4 | 9e-08 | 31/46 (AsPC-1, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 0.767× | -3.1 | 0.36 | 14/48 (Panc 03.27, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.773× | -3.0 | 0.36 | 14/47 (SW480, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.773× | -3.0 | 0.36 | 15/47 (NCI-H460, hTERT-HPNE, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.39 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4187. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-423 (line)]] | alt | 28.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.32× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[A498 (line)]] | wt | 14.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.71× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[NCI-H460 (line)]] | wt | 12.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.26× (z +11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[PANC-1 (line)]] | alt | 24.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.18× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[A-427 (line)]] | wt | 18.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.13× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[AsPC-1 (line)]] | alt | 18.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -10.1) |
| [[HOP62 (line)]] | alt | 15.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.65× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[HT-29 (line)]] | alt | 14.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.31× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 22.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -9.7) |
| [[A-172 (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.86 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.00 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.97 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.06 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.75 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.72 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.25 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.69 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.04 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.27 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.30 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.32 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.57 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.20 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 16.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4187), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EMC4]] | +0.67 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[CETN2]] | +0.60 | +0.39 / +0.60 | both halves | 6e-05 |  |
| [[PIN1]] | +0.57 | +0.56 / +0.35 | both halves | 1e-04 |  |
| [[TRAPPC1]] | +0.57 | +0.47 / +0.46 | both halves | 2e-05 |  |
| [[HTT]] | +0.56 | +0.48 / +0.39 | both halves | 6e-05 |  |
| [[TPRKB]] | +0.56 | +0.58 / +0.37 | both halves | 9e-05 |  |
| [[GDAP2]] | +0.56 | +0.52 / +0.42 | both halves | 4e-05 |  |
| [[VPS29]] | +0.56 | +0.54 / +0.43 | both halves | 3e-05 |  |
| [[POP5]] | +0.54 | +0.35 / +0.43 | both halves | 1e-04 |  |
| [[VAMP3]] | +0.54 | +0.66 / +0.34 | both halves | 1e-04 |  |
| [[NTAN1]] | +0.54 | +0.46 / +0.42 | both halves | 4e-05 |  |
| [[COX5B]] | +0.53 | +0.40 / +0.50 | both halves | 5e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNHG26]] | -0.59 | -0.56 / -0.40 | both halves | 4e-05 |  |
| [[KCNQ4]] | -0.56 | -0.59 / -0.37 | both halves | 9e-05 |  |
| [[E2F5]] | -0.55 | -0.58 / -0.44 | both halves | 3e-05 |  |
| [[PCF11]] | -0.55 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[HDGF]] | -0.51 | -0.45 / -0.24 | both halves | 4e-04 |  |
| [[NOP56]] | -0.51 | -0.44 / -0.40 | both halves | 5e-05 |  |
| [[NCL]] | -0.49 | -0.31 / -0.48 | both halves | 2e-04 |  |
| [[AGER]] | -0.49 | -0.48 / -0.24 | both halves | 5e-04 |  |
| [[RCC1]] | -0.49 | -0.51 / -0.35 | both halves | 1e-04 |  |
| [[LINC01355]] | -0.48 | -0.33 / -0.47 | both halves | 1e-04 |  |
| [[GALNT7-DT]] | -0.48 | -0.49 / -0.23 | both halves | 5e-04 |  |
| [[CDKL1]] | -0.47 | -0.39 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.283). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (0.1, -22.8); signed map (-38.2, 12.6). **Vector** length 48.7, 7.39% of its response variance represented; |z| ≥ 3 in 620 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | +3.5 | +14.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | +2.8 | +13.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.8 | +4.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | +2.6 | +5.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | +2.2 | +5.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.2 | +3.1 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +1.0 | +2.8 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +0.9 | +3.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +0.8 | -0.3 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -3.1 | -6.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.4 | -2.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.9 | -3.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.2 | -2.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.2 | -2.8 |
|  | [[EX229 (drug)]] 5 µM |  | -1.2 | -1.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.1 | +1.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.1 | -0.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -0.9 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | PDZ domain containing 11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq13.1 — chrX:70,281,118-70,290,514 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously PDZK11 |
| Gene groups (HGNC) | PDZ domain containing |
| Reactome | 12 pathways, smallest: Ion influx/efflux at host-pathogen interface; Biotin transport and metabolism; Antimicrobial peptides |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5EBL8](https://www.uniprot.org/uniprotkb/Q5EBL8) (PDZ domain-containing protein 11):

> Mediates docking of ADAM10 to zonula adherens by interacting with PLEKHA7 which is required for PLEKHA7 to interact with the ADAM10-binding protein TSPAN33.

**Summary**, from NCBI Gene [51248](https://www.ncbi.nlm.nih.gov/gene/51248):

> Predicted to enable protein-macromolecule adaptor activity. Involved in pore complex assembly. Located in basolateral plasma membrane and cytosol. Part of pore complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28034](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28034) · Entrez [51248](https://www.ncbi.nlm.nih.gov/gene/51248) · UniProt [Q5EBL8](https://www.uniprot.org/uniprotkb/Q5EBL8) · Ensembl [ENSG00000120509](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000120509)

## Data

Gene col 4187: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4187); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4187, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4187]; `tensor/DDL_lfc|DDL_z.npy` [4187]; `embed/gene_vectors.npy` [4187]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4187 or target_col == 4187). Every well: [[PDZD11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PDZD11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
