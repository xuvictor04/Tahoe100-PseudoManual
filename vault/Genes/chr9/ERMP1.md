---
symbol: "ERMP1"
type: "gene"
col: 1783
ensembl_id: "ENSG00000099219"
name: "endoplasmic reticulum metallopeptidase 1"
location: "9p24.1"
module: 29
arm: "+"
pooled_cpm: 35.97
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 14
n_dd_up_clean: 2
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# ERMP1

*endoplasmic reticulum metallopeptidase 1* — 9p24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.51× (z +6.9, q 4e-09, up in 22 of 37 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 1.25× (z +3.9, q 0.016, up in 14 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (MIA PaCa-2 2.98×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (2 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.348× (z -17.6, q 0e+00, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CRTAP]] (+0.73, fdr 7e-06), [[PPT1]] (+0.72, fdr 7e-06), [[FKBP9]] (+0.72, fdr 7e-06); moves opposite to [[ZNF593]] (-0.69, fdr 9e-06), [[NSRP1]] (-0.68, fdr 7e-06), [[CROCCP2-1]] (-0.65, fdr 7e-06).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 4 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1783.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (MIA PaCa-2 2.98×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.51×** | +6.9 | 4e-09 | 22/37 (A498, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.44×** | +6.2 | 1e-07 | 24/44 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.26×** | +3.9 | 0.016 | 14/48 (KATO III, NCI-H2030, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.25×** | +3.9 | 0.016 | 14/48 (RKO, KATO III, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.24×** | +3.4 | 0.076 | 13/41 (NCI-H1792, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | **1.22×** | +3.4 | 0.076 | 10/48 (NCI-H460, NCI-H1573, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 2 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1783.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.348×** | -17.6 | 0e+00 | 44/48 (A549, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.509×** | -16.5 | 0e+00 | 36/47 (COLO 205, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.498×** | -12.1 | 4e-31 | 35/47 (COLO 205, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.607×** | -8.6 | 8e-16 | 35/48 (NCI-H460, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.623×** | -8.2 | 3e-14 | 34/48 (SNU-1, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.634×** | -7.9 | 3e-13 | 30/46 (H4, BT-474, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.672×** | -6.9 | 5e-10 | 36/47 (SW480, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.704×** | -5.8 | 4e-07 | 24/45 (SNU-423, COLO 205, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.772×** | -4.5 | 5e-04 | 23/47 (COLO 205, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.782×** | -4.3 | 0.001 | 21/48 (HCT15, COLO 205, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.786×** | -4.2 | 0.002 | 24/47 (A498, SW480, …) | top dose only |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.752×** | -3.5 | 0.021 | 15/47 (HT-29, RKO, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.821×** | -3.4 | 0.028 | 14/47 (SW 900, COLO 205, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.833×** | -3.2 | 0.060 | 17/48 (NCI-H460, C32, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1783. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 135 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -20.0) |
| [[A498 (line)]] | wt | 24.9 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.369× (z -14.5) |
| [[A549 (line)]] | wt | 41.9 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -17.8) |
| [[HEC-1-A (line)]] | alt | 65.2 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.345× (z -17.0) |
| [[SW480 (line)]] | alt | 50.9 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.463× (z -11.7) |
| [[C32 (line)]] | wt | 39.1 | 0 | 3 | — | [[Harringtonine (drug)]] 5 µM 0.198× (z -11.8) |
| [[H4 (line)]] | wt | 22.9 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0632× (z -14.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0793× (z -13.3) |
| [[KATO III (line)]] | alt | 52.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.311× (z -14.1) |
| [[MIA PaCa-2 (line)]] | alt | 61.5 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.98× (z +8.9) ⚠ toxic; transcription drop | [[Harringtonine (drug)]] 5 µM 0.228× (z -11.8) |
| [[PANC-1 (line)]] | alt | 19.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.354× (z -14.0) |
| [[SNU-423 (line)]] | alt | 26.3 | 0 | 3 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.231× (z -10.3) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 5 µM 0.249× (z -9.7) |
| [[A-427 (line)]] | wt | 34.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.421× (z -10.5) |
| [[BT-474 (line)]] | alt | 21.6 | 0 | 2 (2 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.0884× (z -11.3) ⚠ toxic |
| [[CFPAC-1 (line)]] | alt | 24.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.335× (z -12.8) |
| [[CHP-212 (line)]] | wt | 33.9 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 0.05 µM 0.0878× (z -9.9) |
| [[HCT15 (line)]] | alt | 90.6 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.240× (z -10.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.308× (z -8.6) |
| [[Hs 766T (line)]] | wt | 33.2 | 0 | 2 (1 ⚠) | — | [[AZD2858 (drug)]] 5 µM 0.0784× (z -9.7) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 5 µM 0.299× (z -8.5) |
| [[LS 180 (line)]] | wt | 62.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.437× (z -11.7) |
| [[NCI-H2030 (line)]] | alt | 25.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -11.5) |
| [[NCI-H2347 (line)]] | alt | 17.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.437× (z -9.4) |
| [[NCI-H460 (line)]] | wt | 32.6 | 0 | 2 | — | [[Harringtonine (drug)]] 0.5 µM 0.183× (z -17.0) |
| [[SNU-1 (line)]] | wt | 62.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -14.3) |
| [[SW48 (line)]] | wt | 59.7 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.198× (z -10.6) |
| [[AN3 CA (line)]] | alt | 35.1 | 0 | 1 | — | [[Menadione (drug)]] 0.05 µM 0.110× (z -8.7) |
| [[HOP62 (line)]] | alt | 20.3 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.306× (z -9.6) |
| [[HS-578T (line)]] | alt | 31.3 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.256× (z -9.8) |
| [[HT-29 (line)]] | alt | 70.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -13.6) |
| [[J82 (line)]] | alt | 26.2 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.330× (z -8.6) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 39.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.355× (z -8.9) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 18.9 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.217× (z -9.2) |
| [[NCI-H1792 (line)]] | alt | 20.4 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.207× (z -10.3) |
| [[Panc 03.27 (line)]] | alt | 41.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.329× (z -12.4) |
| [[SK-MEL-2 (line)]] | alt | 30.8 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.238× (z -9.3) |
| [[SW1417 (line)]] | alt | 57.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.402× (z -11.7) |
| [[A-172 (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 34.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 34.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 27.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 48.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 22.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1783), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CRTAP]] | +0.73 | +0.59 / +0.75 | both halves | 7e-06 |  |
| [[PPT1]] | +0.72 | +0.64 / +0.75 | both halves | 7e-06 |  |
| [[FKBP9]] | +0.72 | +0.64 / +0.73 | both halves | 7e-06 |  |
| [[TMEM123]] | +0.71 | +0.65 / +0.69 | both halves | 7e-06 |  |
| [[RNPEP]] | +0.70 | +0.64 / +0.69 | both halves | 7e-06 |  |
| [[BPNT2]] | +0.70 | +0.57 / +0.73 | both halves | 1e-05 |  |
| [[PRDX3]] | +0.69 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[SCARB2]] | +0.69 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[STT3B]] | +0.68 | +0.59 / +0.74 | both halves | 7e-06 |  |
| [[DDOST]] | +0.68 | +0.65 / +0.65 | both halves | 7e-06 |  |
| [[CLSTN1]] | +0.68 | +0.56 / +0.72 | both halves | 1e-05 |  |
| [[IARS2]] | +0.67 | +0.63 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF593]] | -0.69 | -0.57 / -0.68 | both halves | 9e-06 |  |
| [[NSRP1]] | -0.68 | -0.61 / -0.72 | both halves | 7e-06 |  |
| [[CROCCP2-1]] | -0.65 | -0.60 / -0.68 | both halves | 7e-06 |  |
| [[AK6]] | -0.65 | -0.57 / -0.64 | both halves | 1e-05 |  |
| [[ZNF75A]] | -0.65 | -0.54 / -0.73 | both halves | 1e-05 |  |
| [[RBX1]] | -0.64 | -0.57 / -0.61 | both halves | 8e-06 |  |
| [[MRPS18C]] | -0.63 | -0.52 / -0.60 | both halves | 1e-05 |  |
| [[PIGBOS1]] | -0.63 | -0.45 / -0.68 | both halves | 3e-05 |  |
| [[CEBPZ]] | -0.63 | -0.46 / -0.68 | both halves | 2e-05 |  |
| [[ESF1]] | -0.62 | -0.54 / -0.64 | both halves | 1e-05 |  |
| [[EID2]] | -0.62 | -0.48 / -0.65 | both halves | 2e-05 |  |
| [[TOPORS]] | -0.61 | -0.51 / -0.64 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.795). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-25.6, -21.7); signed map (-22.9, -39.1). **Vector** length 92.2, 20.3% of its response variance represented; |z| ≥ 3 in 995 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.8 | +3.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.4 | +6.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.3 | +6.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.5 | +3.9 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | +3.1 | +1.1 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | +2.4 | +2.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.3 | +1.6 |
|  | [[Ipatasertib (drug)]] 5 µM |  | +2.2 | +1.8 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.9 | +2.0 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -7.5 | -17.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.9 | -8.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.7 | -12.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.2 | -16.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.6 | -4.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.9 | -2.7 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | -1.8 | -2.3 |
|  | [[vincristine (drug)]] 0.5 µM |  | -1.8 | -3.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.8 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | endoplasmic reticulum metallopeptidase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p24.1 — chr9:5,749,832-5,879,537 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ23309, FXNA; previously KIAA1815 |
| Gene groups (HGNC) | M28 metallopeptidases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z2K6](https://www.uniprot.org/uniprotkb/Q7Z2K6) (Endoplasmic reticulum metallopeptidase 1):

> Within the ovary, required for the organization of somatic cells and oocytes into discrete follicular structures.

**Summary**, from NCBI Gene [79956](https://www.ncbi.nlm.nih.gov/gene/79956):

> Predicted to enable metal ion binding activity and metalloexopeptidase activity. Involved in cellular response to oxidative stress. Acts upstream of or within endoplasmic reticulum unfolded protein response. Located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:23703](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23703) · Entrez [79956](https://www.ncbi.nlm.nih.gov/gene/79956) · UniProt [Q7Z2K6](https://www.uniprot.org/uniprotkb/Q7Z2K6) · Ensembl [ENSG00000099219](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000099219)

## Data

Gene col 1783: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1783); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1783, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1783]; `tensor/DDL_lfc|DDL_z.npy` [1783]; `embed/gene_vectors.npy` [1783]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1783 or target_col == 1783). Every well: [[ERMP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ERMP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
