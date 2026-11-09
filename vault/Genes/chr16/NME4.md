---
symbol: "NME4"
type: "gene"
col: 2336
ensembl_id: "ENSG00000103202"
name: "NME/NM23 nucleoside diphosphate kinase 4"
location: "16p13.3"
module: 29
arm: "+"
pooled_cpm: 16.03
n_lines_expressing: 46
n_dd_up: 5
n_dd_down: 3
n_dd_up_clean: 0
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# NME4

*NME/NM23 nucleoside diphosphate kinase 4* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 5.54× (z +15.0, q 0e+00, up in 35 of 35 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 10 lines (PANC-1 5.71×, A-172 6.24×, NCI-H460 6.04×, A549 8.83×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (PANC-1 4.49×, NCI-H460 4.93×, A498 4.69×, MIA PaCa-2 5.87×, …; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H2347 3.25×).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.448× (z -7.0, q 8e-10, down in 35 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MYL9]] (+0.65, fdr 1e-05), [[ARL2]] (+0.63, fdr 1e-05), [[CDKN2AIPNL]] (+0.63, fdr 1e-05); moves opposite to [[FAM32A]] (-0.53, fdr 4e-04), [[KIN]] (-0.51, fdr 3e-04), [[ZKSCAN1]] (-0.49, fdr 3e-04).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 6 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2336.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 10 lines (PANC-1 5.71×, A-172 6.24×, NCI-H460 6.04×, A549 8.83×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (PANC-1 4.49×, NCI-H460 4.93×, A498 4.69×, MIA PaCa-2 5.87×, …; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H2347 3.25×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.54×** | +15.0 | 0e+00 | 35/35 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.68×** | +13.0 | 5e-36 | 25/25 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.63×** | +10.4 | 4e-23 | 28/30 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.68×** | +4.3 | 0.002 | 21/39 (MIA PaCa-2, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.15× | +4.0 | 0.007 | 5/44 (NCI-H23, NCI-H2030, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~56% of this change | **1.53×** | +3.7 | 0.018 | 19/40 (PANC-1, A-427, …) | inconsistent across doses | low cells (technical?); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2336.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.448×** | -7.0 | 8e-10 | 35/43 (BT-474, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.569×** | -7.0 | 8e-10 | 35/43 (NCI-H2030, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.524×** | -5.7 | 3e-06 | 33/43 (H4, LOX-IMVI, …) | two highest doses | cell-cycle shift (explains ~17% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | 0.702× | -3.1 | 0.20 | 18/44 (NCI-H460, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | 0.707× | -3.0 | 0.20 | 19/43 (A-427, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~56% of this change | 0.695× | -3.0 | 0.20 | 17/43 (AN3 CA, PANC-1, …) | inconsistent across doses |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 0.710× | -3.0 | 0.20 | 17/42 (SNU-423, NCI-H1792, …) | inconsistent across doses | low cells (technical?); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, +0.50 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2336. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 24.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.24× (z +12.1) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 17.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.32× (z +10.6) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 21.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.83× (z +11.2) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 44.2 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.217× (z -9.6) |
| [[LOX-IMVI (line)]] | wt | 19.0 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.20× (z +8.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -10.0) |
| [[LS 180 (line)]] | wt | 7.96 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 7.39× (z +8.7) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.234× (z -8.9) |
| [[MIA PaCa-2 (line)]] | alt | 18.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.11× (z +10.0) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 7.80 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 12.1× (z +9.8) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 38.6 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.83× (z +10.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -10.6) |
| [[NCI-H460 (line)]] | wt | 21.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.04× (z +11.2) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 48.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.71× (z +12.1) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 12.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.23× (z +10.6) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 12.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.52× (z +8.5) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 19.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -10.0) |
| [[C32 (line)]] | wt | 13.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 9.06× (z +9.4) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 7.27 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 9.11× (z +8.5) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 16.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0745× (z -13.9) ⚠ toxic; cell-cycle shift, explains ~44% of this change |
| [[NCI-H1573 (line)]] | alt | 11.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.43× (z +9.6) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 14.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.25× (z +9.1) | — |
| [[SK-MEL-2 (line)]] | alt | 13.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -9.2) |
| [[A-427 (line)]] | wt | 33.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.16 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.86 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.62 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.85 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.09 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.39 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.02 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 61.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.53 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.52 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.82 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.17 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.92 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.70 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.63 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2336), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYL9]] | +0.65 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[ARL2]] | +0.63 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[CDKN2AIPNL]] | +0.63 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[FKBP7]] | +0.60 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[ATP6V0E2]] | +0.58 | +0.47 / +0.48 | both halves | 2e-05 |  |
| [[MXRA8]] | +0.57 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[NAXE]] | +0.57 | +0.59 / +0.43 | both halves | 3e-05 |  |
| [[SUMF2]] | +0.55 | +0.67 / +0.23 | both halves | 5e-04 |  |
| [[SMAD2]] | +0.54 | +0.52 / +0.41 | both halves | 4e-05 |  |
| [[CRTAP]] | +0.54 | +0.64 / +0.33 | both halves | 1e-04 |  |
| [[ARHGDIB]] | +0.54 | +0.57 / +0.31 | both halves | 2e-04 |  |
| [[PRDX3]] | +0.54 | +0.58 / +0.36 | both halves | 9e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM32A]] | -0.53 | -0.60 / -0.25 | both halves | 4e-04 |  |
| [[KIN]] | -0.51 | -0.56 / -0.27 | both halves | 3e-04 |  |
| [[ZKSCAN1]] | -0.49 | -0.53 / -0.27 | both halves | 3e-04 |  |
| [[FCF1]] | -0.48 | -0.53 / -0.29 | both halves | 2e-04 |  |
| [[DNTTIP2]] | -0.48 | -0.51 / -0.24 | both halves | 4e-04 |  |
| [[C6orf62]] | -0.48 | -0.47 / -0.29 | both halves | 2e-04 |  |
| [[UBXN4]] | -0.47 | -0.57 / -0.31 | both halves | 2e-04 |  |
| [[NSRP1]] | -0.47 | -0.62 / -0.24 | both halves | 4e-04 |  |
| [[GCC2]] | -0.46 | -0.54 / -0.28 | both halves | 3e-04 |  |
| [[KCTD5]] | -0.46 | -0.43 / -0.35 | both halves | 1e-04 |  |
| [[CPT2]] | -0.46 | -0.45 / -0.28 | both halves | 3e-04 |  |
| [[TUT7]] | -0.45 | -0.56 / -0.25 | both halves | 4e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.490). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-24.9, -18.3); signed map (-22.5, -41.5). **Vector** length 51.8, 9.54% of its response variance represented; |z| ≥ 3 in 624 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.2 | +10.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.7 | +15.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.5 | +13.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | +0.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~44% of this change | +2.4 | +2.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.0 | -1.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.0 | -2.0 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | +0.9 | +0.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +0.9 | -0.1 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.3 | -7.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.2 | -0.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | -2.0 | -5.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.8 | -1.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -1.8 | -7.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.4 | -2.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.1 | -1.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.1 | +0.4 |

## What is on record

|  |  |
|---|---|
| Name | NME/NM23 nucleoside diphosphate kinase 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:396,725-410,367 (+) |
| Ensembl biotype | protein_coding |
| Also known as | nm23-H4, NM23H4, NDPKD |
| Gene groups (HGNC) | NME/NM23 family |
| Hallmark sets | DNA_REPAIR |
| Reactome | 2 pathways, smallest: Interconversion of nucleotide di- and triphosphates; Metabolism of nucleotides |
| Matched by | ensembl_id |

**Function**, from UniProt [O00746](https://www.uniprot.org/uniprotkb/O00746) (Nucleoside diphosphate kinase D, mitochondrial):

> Mitochondria-specific nucleoside diphosphate kinase that catalyzes the transfer of a gamma-phosphoryl group from ATP to a nucleoside diphosphate via a ping-pong mechanism involving a phosphohistidine intermediate, participating in nucleoside triphosphate homeostasis. In vitro, purine nucleoside triphosphates are much more effective as donors and acceptors than pyrimidine nucleoside triphosphates, and ribonucleosides derivatives are superior to their deoxyribonucleosides counterparts (By …

**Summary**, from NCBI Gene [4833](https://www.ncbi.nlm.nih.gov/gene/4833):

> The nucleoside diphosphate (NDP) kinases (EC 2.7.4.6) are ubiquitous enzymes that catalyze transfer of gamma-phosphates, via a phosphohistidine intermediate, between nucleoside and dioxynucleoside tri- and diphosphates. The enzymes are products of the nm23 gene family, which includes NME4 (Milon et al., 1997 [PubMed 9099850]).[supplied by OMIM, May 2008]

**Accessions** — [HGNC:7852](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7852) · Entrez [4833](https://www.ncbi.nlm.nih.gov/gene/4833) · UniProt [O00746](https://www.uniprot.org/uniprotkb/O00746) · Ensembl [ENSG00000103202](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000103202)

## Data

Gene col 2336: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2336); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2336, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2336]; `tensor/DDL_lfc|DDL_z.npy` [2336]; `embed/gene_vectors.npy` [2336]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2336 or target_col == 2336). Every well: [[NME4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NME4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
