---
symbol: "DUS1L"
type: "gene"
col: 9843
ensembl_id: "ENSG00000169718"
name: "dihydrouridine synthase 1 like"
location: "17q25.3"
module: 2
arm: "+"
pooled_cpm: 17.09
n_lines_expressing: 49
n_dd_up: 12
n_dd_down: 0
n_dd_up_clean: 1
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# DUS1L

*dihydrouridine synthase 1 like* — 17q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.73× (z +13.3, q 8e-38, up in 38 of 38 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Ipatasertib (drug)]] 0.5 µM: 2.15× (z +3.3, q 0.057, up in 16 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 10 lines (SW480 6.63×, LoVo 7.86×, NCI-H1573 10.3×, KATO III 6.89×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change); [[Dinaciclib (drug)]] 5 µM in 5 lines (LoVo 8.19×, SW480 6.00×, Panc 03.27 6.31×, KATO III 5.30×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Pitavastatin (Calcium) (drug)]] 5 µM in 1 line (HepG2/C3A 0.109×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRABD]] (+0.68, fdr 3e-05), [[ZMYND19]] (+0.62, fdr 1e-05), [[TELO2]] (+0.62, fdr 1e-05); moves opposite to [[ZNF436]] (-0.59, fdr 5e-05), [[ZBTB6]] (-0.53, fdr 7e-05), [[MKLN1-AS]] (-0.53, fdr 3e-04).
> It sits in the **+** arm of [[Module 002]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 11 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9843.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 10 lines (SW480 6.63×, LoVo 7.86×, NCI-H1573 10.3×, KATO III 6.89×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change); [[Dinaciclib (drug)]] 5 µM in 5 lines (LoVo 8.19×, SW480 6.00×, Panc 03.27 6.31×, KATO III 5.30×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **4.73×** | +13.3 | 8e-38 | 38/38 (SW480, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **3.87×** | +11.2 | 1e-26 | 29/29 (LoVo, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **2.69×** | +7.2 | 9e-11 | 30/34 (LoVo, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.84×** | +5.2 | 2e-05 | 36/47 (COLO 205, MIA PaCa-2, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **1.76×** | +4.9 | 1e-04 | 35/47 (COLO 205, MIA PaCa-2, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~31% of this change | **1.74×** | +4.7 | 2e-04 | 29/43 (SW480, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.72×** | +4.4 | 6e-04 | 29/42 (CFPAC-1, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~24% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~39% of this change | **1.71×** | +4.4 | 6e-04 | 25/42 (MIA PaCa-2, A549, …) | top dose only | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~82% of this change | **1.51×** | +3.6 | 0.024 | 23/47 (COLO 205, SW480, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.52×** | +3.4 | 0.033 | 22/46 (MIA PaCa-2, HEC-1-A, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.15×** | +3.3 | 0.057 | 16/45 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~78% of this change | **1.45×** | +3.2 | 0.077 | 16/46 (NCI-H460, KATO III, …) | top dose only |  |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Pitavastatin (Calcium) (drug)]] 5 µM in 1 line (HepG2/C3A 0.109×; ⚠ cell-cycle shift, would explain all of this change).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.53 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9843. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 29.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.38× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[KATO III (line)]] | alt | 26.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.89× (z +11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[LoVo (line)]] | wt | 18.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.86× (z +12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[LS 180 (line)]] | wt | 27.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.92× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 16.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.80× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[NCI-H460 (line)]] | wt | 18.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.04× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[SW480 (line)]] | alt | 25.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.63× (z +12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[A-172 (line)]] | wt | 14.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.24× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[A498 (line)]] | wt | 21.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.22× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[HepG2_C3A (line)]] | wt | 17.3 | 0 | 1 (1 ⚠) | — | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.109× (z -8.6) ⚠ cell-cycle shift, would explain all of this change |
| [[HT-29 (line)]] | alt | 16.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.24× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[NCI-H1573 (line)]] | alt | 11.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.3× (z +11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[Panc 03.27 (line)]] | alt | 20.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.31× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 20.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.96× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[SNU-423 (line)]] | alt | 11.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.47× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[SW1417 (line)]] | alt | 28.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.41× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[A-427 (line)]] | wt | 23.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.29 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.46 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.58 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.94 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 30.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.87 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.58 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.71 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.16 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 18.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9843), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 8 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRABD]] | +0.68 | +0.46 / +0.64 | both halves | 3e-05 |  |
| [[ZMYND19]] | +0.62 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[TELO2]] | +0.62 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[SLC39A4]] | +0.61 | +0.45 / +0.58 | both halves | 3e-05 |  |
| [[CDK10]] | +0.60 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[E4F1]] | +0.60 | +0.28 / +0.54 | both halves | 3e-04 |  |
| [[RHPN1]] | +0.59 | +0.54 / +0.40 | both halves | 5e-05 |  |
| [[UCKL1]] | +0.59 | +0.36 / +0.57 | both halves | 9e-05 |  |
| [[NPDC1]] | +0.58 | +0.38 / +0.59 | both halves | 7e-05 |  |
| [[PACS2]] | +0.58 | +0.45 / +0.45 | both halves | 3e-05 |  |
| [[ZDHHC8]] | +0.58 | +0.37 / +0.52 | both halves | 8e-05 |  |
| [[WRN]] | +0.58 | +0.31 / +0.51 | both halves | 2e-04 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF436]] | -0.59 | -0.39 / -0.53 | both halves | 5e-05 |  |
| [[ZBTB6]] | -0.53 | -0.37 / -0.39 | both halves | 7e-05 |  |
| [[MKLN1-AS]] | -0.53 | -0.27 / -0.43 | both halves | 3e-04 |  |
| [[ZNF711]] | -0.51 | -0.35 / -0.34 | both halves | 1e-04 |  |
| [[TTC33]] | -0.51 | -0.30 / -0.32 | both halves | 2e-04 |  |
| [[ARMT1]] | -0.51 | -0.29 / -0.42 | both halves | 3e-04 |  |
| [[ZNF189]] | -0.51 | -0.31 / -0.32 | both halves | 2e-04 |  |
| [[TDP2]] | -0.51 | -0.27 / -0.34 | both halves | 3e-04 |  |
| [[EIF4G2]] | -0.50 | -0.19 / -0.45 | ⚠ not reproduced | 8e-04 |  |
| [[TAF7]] | -0.50 | -0.26 / -0.35 | both halves | 3e-04 |  |
| [[UBQLN2]] | -0.50 | -0.37 / -0.34 | both halves | 1e-04 |  |
| [[ZXDA]] | -0.49 | -0.28 / -0.30 | both halves | 3e-04 |  |
| [[VCPIP1]] | -0.49 | -0.43 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.568). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-26.6, -45.5); signed map (-47.5, -15.8). **Vector** length 52.7, 10.8% of its response variance represented; |z| ≥ 3 in 537 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | +3.0 | +4.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | +2.7 | +13.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.5 | +3.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~82% of this change | +2.2 | +3.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | +2.2 | +5.2 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.6 | +2.3 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +1.6 | +2.3 |
|  | [[PH-797804 (drug)]] 0.5 µM |  | +1.5 | +1.8 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.5 | +2.5 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | +0.3 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.8 | +0.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | -1.5 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | -2.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.2 | +0.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.9 | -2.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.8 | -1.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.4 | -1.9 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -1.3 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | dihydrouridine synthase 1 like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.3 — chr17:82,057,506-82,065,887 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PP3111, DUS1 |
| Gene groups (HGNC) | Dihydrouridine synthase family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6P1R4](https://www.uniprot.org/uniprotkb/Q6P1R4) (tRNA-dihydrouridine(16/17) synthase):

> Catalyzes the synthesis of dihydrouridine, a modified base found in the D-loop of most tRNAs. Specifically modifies U16 and U17 in cytoplasmic tRNAs. Affects the level of some mature tRNA and thereby the total cellular translation.

**Summary**, from NCBI Gene [64118](https://www.ncbi.nlm.nih.gov/gene/64118):

> Enables tRNA-dihydrouridine16 synthase activity and tRNA-dihydrouridine17 synthase activity. Involved in tRNA dihydrouridine synthesis. Located in cytoplasm and nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:30086](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30086) · Entrez [64118](https://www.ncbi.nlm.nih.gov/gene/64118) · UniProt [Q6P1R4](https://www.uniprot.org/uniprotkb/Q6P1R4) · Ensembl [ENSG00000169718](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169718)

## Data

Gene col 9843: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9843); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9843, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9843]; `tensor/DDL_lfc|DDL_z.npy` [9843]; `embed/gene_vectors.npy` [9843]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9843 or target_col == 9843). Every well: [[DUS1L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DUS1L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
