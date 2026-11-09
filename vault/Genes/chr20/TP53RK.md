---
symbol: "TP53RK"
type: "gene"
col: 10238
ensembl_id: "ENSG00000172315"
name: "TP53 regulating kinase"
location: "20q13.12"
module: 11
arm: "+"
pooled_cpm: 6.44
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 0
n_dd_up_clean: 14
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# TP53RK

*TP53 regulating kinase* — 20q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (12 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 2.95× (z +13.0, q 1e-35, up in 39 of 44 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (NCI-H2030 0.0871×, SW1417 0.230×, KATO III 0.206×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H2030 0.151×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Verteporfin (drug)]] 5 µM in 1 line (SNU-423 0.106×); [[Temsirolimus (drug)]] 0.5 µM in 1 line (C32 0.103×); [[Cepharanthine (drug)]] 5 µM in 1 line (NCI-H2347 0.241×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[JAGN1]] (+0.73, fdr 7e-06), [[C14orf119]] (+0.72, fdr 7e-06), [[ARL14EP]] (+0.69, fdr 7e-06); moves opposite to [[SEPTIN2]] (-0.65, fdr 1e-05), [[RPA1]] (-0.61, fdr 1e-05), [[POLR2B]] (-0.60, fdr 1e-04).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 12 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10238.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **2.95×** | +13.0 | 1e-35 | 39/44 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.69×** | +12.3 | 2e-32 | 39/46 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **2.00×** | +12.2 | 4e-32 | 34/41 (SNU-423, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.36×** | +10.3 | 1e-22 | 28/34 (NCI-H2030, SW 900, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.24×** | +10.1 | 9e-22 | 31/39 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~28% of this change | **1.65×** | +6.2 | 5e-08 | 15/35 (A498, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **1.58×** | +5.7 | 9e-07 | 18/42 (Hs 766T, PANC-1, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.55×** | +5.4 | 4e-06 | 17/45 (SK-MEL-2, HS-578T, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.51×** | +5.1 | 2e-05 | 19/46 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.51×** | +5.1 | 2e-05 | 15/46 (NCI-H1573, PANC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.50×** | +5.0 | 3e-05 | 19/47 (PANC-1, NCI-H1573, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.45×** | +4.6 | 2e-04 | 19/47 (PANC-1, CFPAC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.44×** | +4.5 | 2e-04 | 12/46 (NCI-H1573, NCI-H2030, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.43×** | +4.4 | 4e-04 | 14/47 (Hs 766T, NCI-H1792, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.45×** | +4.3 | 7e-04 | 13/41 (NCI-H460, C-33 A, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.39×** | +4.1 | 0.001 | 5/47 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.39×** | +4.0 | 0.002 | 10/45 (MIA PaCa-2, PANC-1, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.36×** | +3.8 | 0.004 | 15/46 (SNU-423, HOP62, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.30×** | +3.2 | 0.032 | 11/45 (A549, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.59×** | +3.0 | 0.063 | 2/43 (A498, MIA PaCa-2) | rises with dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.29×** | +3.0 | 0.071 | 10/43 (NCI-H2030, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[vincristine (drug)]] 0.5 µM |  | **1.38×** | +2.9 | 0.094 | 5/42 (SK-MEL-2, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10238.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (NCI-H2030 0.0871×, SW1417 0.230×, KATO III 0.206×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H2030 0.151×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Verteporfin (drug)]] 5 µM in 1 line (SNU-423 0.106×); [[Temsirolimus (drug)]] 0.5 µM in 1 line (C32 0.103×); [[Cepharanthine (drug)]] 5 µM in 1 line (NCI-H2347 0.241×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tofacitinib (drug)]] 5 µM |  | 0.825× | -3.5 | 0.30 | 10/46 (C-33 A, Panc 03.27, …) | inconsistent across doses |  |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.784× | -3.1 | 0.59 | 7/47 (C32, LS 180, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10238. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 11.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0871× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SNU-423 (line)]] | alt | 6.62 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 5.23× (z +9.8) ⚠ cell-cycle shift, explains ~26% of this change | [[Verteporfin (drug)]] 5 µM 0.106× (z -9.1) |
| [[C32 (line)]] | wt | 6.21 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.103× (z -8.5) |
| [[KATO III (line)]] | alt | 10.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.206× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H2347 (line)]] | alt | 3.44 | 0 | 1 | — | [[Cepharanthine (drug)]] 5 µM 0.241× (z -8.5) |
| [[SW1417 (line)]] | alt | 13.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.230× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 4.69 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.51 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 9.00 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.31 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.11 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.95 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.10 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.11 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.55 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.55 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.81 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.32 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.24 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.28 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.73 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.58 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.81 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.77 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.13 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.23 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.64 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.63 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.72 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.88 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.08 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.69 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 6.56 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.70 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.11 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.22 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.96 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.88 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.49 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.88 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.67 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.35 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.03 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10238), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[JAGN1]] | +0.73 | +0.70 / +0.67 | both halves | 7e-06 |  |
| [[C14orf119]] | +0.72 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[ARL14EP]] | +0.69 | +0.62 / +0.70 | both halves | 7e-06 |  |
| [[PBDC1]] | +0.69 | +0.58 / +0.69 | both halves | 7e-06 |  |
| [[RPP38]] | +0.69 | +0.59 / +0.67 | both halves | 7e-06 | pathway: tRNA processing |
| [[RPP25L]] | +0.69 | +0.55 / +0.71 | both halves | 1e-05 |  |
| [[ERCC4]] | +0.68 | +0.63 / +0.72 | both halves | 7e-06 |  |
| [[UQCRFS1]] | +0.67 | +0.58 / +0.67 | both halves | 8e-06 |  |
| [[NSMCE3]] | +0.67 | +0.57 / +0.71 | both halves | 8e-06 |  |
| [[TMEM70]] | +0.67 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[UTP3]] | +0.66 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[NME6]] | +0.66 | +0.60 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEPTIN2]] | -0.65 | -0.55 / -0.66 | both halves | 1e-05 |  |
| [[RPA1]] | -0.61 | -0.60 / -0.53 | both halves | 1e-05 | pathway: Regulation of TP53 Activity |
| [[POLR2B]] | -0.60 | -0.33 / -0.67 | both halves | 1e-04 |  |
| [[CD46]] | -0.60 | -0.58 / -0.55 | both halves | 1e-05 |  |
| [[TM9SF2]] | -0.59 | -0.51 / -0.59 | both halves | 1e-05 |  |
| [[USP48]] | -0.58 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[CD99]] | -0.58 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[RCN2]] | -0.58 | -0.44 / -0.52 | both halves | 3e-05 |  |
| [[NAP1L4]] | -0.57 | -0.57 / -0.57 | both halves | 9e-06 |  |
| [[TIMP2]] | -0.56 | -0.40 / -0.54 | both halves | 5e-05 |  |
| [[PCYOX1]] | -0.55 | -0.43 / -0.47 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.735). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-35.1, 6.0); signed map (2.6, -19.2). **Vector** length 55.6, 7.66% of its response variance represented; |z| ≥ 3 in 866 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +4.7 | +12.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.2 | +13.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.2 | +10.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.6 | +10.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +3.2 | +12.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.0 | +5.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.7 | +4.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.5 | +2.7 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.3 | +1.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.1 | +1.5 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.4 | +2.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -3.4 | -0.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | -0.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.4 | -0.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -2.3 | +1.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.9 | -0.4 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.4 | -2.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.0 | -2.3 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -0.9 | -1.2 |
|  | [[Trimetrexate (drug)]] 5 µM |  | -0.9 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | TP53 regulating kinase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.12 — chr20:46,684,365-46,689,444 (-) |
| Ensembl biotype | protein_coding |
| Also known as | dJ101A2.2, prpk, Nori-2p, BUD32, TPRKB; previously C20orf64 |
| Gene groups (HGNC) | KEOPS complex; TP53 regulating kinase family |
| Reactome | 6 pathways, smallest: tRNA modification in the nucleus and cytosol; Regulation of TP53 Activity through Phosphorylation; tRNA processing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96S44](https://www.uniprot.org/uniprotkb/Q96S44) (EKC/KEOPS complex subunit TP53RK):

> Component of the EKC/KEOPS complex that is required for the formation of a threonylcarbamoyl group on adenosine at position 37 (t(6)A37) in tRNAs that read codons beginning with adenine. The complex is probably involved in the transfer of the threonylcarbamoyl moiety of threonylcarbamoyl-AMP (TC-AMP) to the N6 group of A37. TP53RK has ATPase activity in the context of the EKC/KEOPS complex and likely plays a supporting role to the catalytic subunit OSGEP (By similarity). Atypical protein kinase …

**Summary**, from NCBI Gene [112858](https://www.ncbi.nlm.nih.gov/gene/112858):

> Enables p53 binding activity and protein serine/threonine kinase activity. Involved in protein phosphorylation. Located in cytoplasm and nucleus. Part of EKC/KEOPS complex. Implicated in Galloway-Mowat syndrome 4. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:16197](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16197) · Entrez [112858](https://www.ncbi.nlm.nih.gov/gene/112858) · UniProt [Q96S44](https://www.uniprot.org/uniprotkb/Q96S44) · Ensembl [ENSG00000172315](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172315)

## Data

Gene col 10238: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10238); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10238, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10238]; `tensor/DDL_lfc|DDL_z.npy` [10238]; `embed/gene_vectors.npy` [10238]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10238 or target_col == 10238). Every well: [[TP53RK — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TP53RK.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
