---
symbol: "RNPEPL1"
type: "gene"
col: 6616
ensembl_id: "ENSG00000142327"
name: "arginyl aminopeptidase like 1"
location: "2q37.3"
module: 24
arm: "+"
pooled_cpm: 9.74
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 27
n_dd_up_clean: 2
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# RNPEPL1

*arginyl aminopeptidase like 1* — 2q37.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.80× (z +10.0, q 1e-20, up in 23 of 31 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM: 1.46× (z +3.7, q 0.026, up in 18 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.354× (z -14.2, q 5e-43, down in 43 of 46 measured lines).
> Its strongest partners by |cos| (90 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 13 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MGAT4B]] (+0.59, fdr 1e-05), [[FBXW5]] (+0.57, fdr 3e-05), [[PLEKHN1]] (+0.56, fdr 2e-05); moves opposite to [[PAICS]] (-0.45, fdr 7e-04), [[ZNF484]] (-0.43, fdr 3e-04), [[TMX1]] (-0.41, fdr 0.002, ⚠ one half only (not replicated)).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6616.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.80×** | +10.0 | 1e-20 | 23/31 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.94×** | +6.2 | 2e-07 | 15/20 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.62×** | +4.7 | 5e-04 | 19/41 (PANC-1, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~20% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.56×** | +4.0 | 0.010 | 11/26 (KATO III, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.46×** | +3.7 | 0.026 | 18/43 (NCI-H2347, SW480, …) | inconsistent across doses | low cells (technical?) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.83×** | +3.6 | 0.026 | 15/41 (CFPAC-1, SK-MEL-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | 1.71× | +3.2 | 0.10 | 14/39 (NCI-H1792, LS 180, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | 1.69× | +3.2 | 0.11 | 7/43 (Hs 766T, LS 180, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | 1.66× | +3.1 | 0.13 | 10/43 (PANC-1, NCI-H1573, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | 1.66× | +3.1 | 0.13 | 11/44 (A-172, HOP62, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6616.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.354×** | -14.2 | 5e-43 | 43/46 (J82, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.352×** | -10.1 | 2e-21 | 43/47 (LoVo, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.367×** | -9.7 | 5e-20 | 38/46 (AsPC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.445×** | -7.8 | 7e-13 | 35/46 (BT-474, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.474×** | -7.2 | 6e-11 | 29/41 (NCI-H2347, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.546×** | -5.9 | 5e-07 | 31/46 (NCI-H2030, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~1% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.580×** | -5.3 | 1e-05 | 25/47 (NCI-H1573, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.601×** | -4.9 | 5e-05 | 25/47 (Panc 03.27, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.589×** | -4.9 | 5e-05 | 26/46 (LoVo, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.606×** | -4.8 | 8e-05 | 23/47 (HS-578T, NCI-H2030, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.747×** | -4.0 | 0.004 | 19/47 (NCI-H2347, MIA PaCa-2, …) | rises with dose | low cells (technical?) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.646×** | -3.9 | 0.004 | 18/43 (PANC-1, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~15% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.401×** | -3.9 | 0.004 | 21/42 (LS 180, hTERT-HPNE, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.758×** | -3.8 | 0.006 | 18/47 (NCI-H1573, SW 900, …) | rises with dose |  |
| [[Erlotinib (drug)]] 0.05 µM |  | **0.665×** | -3.6 | 0.010 | 14/46 (LoVo, C32, …) | inconsistent across doses | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.690×** | -3.6 | 0.012 | 19/45 (SK-MEL-2, PANC-1, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.436×** | -3.5 | 0.013 | 16/44 (HOP62, LS 180, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.45 per unit of S-phase module lfc, +0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6616. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 15.0 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0881× (z -12.8) ⚠ toxic; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.317× (z -8.8) |
| [[AsPC-1 (line)]] | alt | 15.9 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.118× (z -11.9) |
| [[LoVo (line)]] | wt | 11.8 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.132× (z -11.2) |
| [[LOX-IMVI (line)]] | wt | 6.63 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.154× (z -10.3) |
| [[NCI-H1573 (line)]] | alt | 13.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -10.9) |
| [[NCI-H460 (line)]] | wt | 9.25 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -8.8) |
| [[BT-474 (line)]] | alt | 6.91 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0827× (z -12.7) |
| [[CFPAC-1 (line)]] | alt | 11.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -9.7) |
| [[HepG2_C3A (line)]] | wt | 10.3 | 0 | 1 | — | [[Tadalafil (drug)]] 5 µM 0.0957× (z -9.1) |
| [[HOP62 (line)]] | alt | 7.87 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -10.3) |
| [[Hs 766T (line)]] | wt | 11.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -10.6) |
| [[J82 (line)]] | alt | 7.22 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.119× (z -13.3) |
| [[LS 180 (line)]] | wt | 11.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -9.4) |
| [[NCI-H1792 (line)]] | alt | 14.7 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.183× (z -8.7) |
| [[NCI-H2030 (line)]] | alt | 10.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -9.8) |
| [[NCI-H23 (line)]] | alt | 7.52 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -8.5) |
| [[NCI-H2347 (line)]] | alt | 7.09 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.164× (z -9.0) |
| [[Panc 03.27 (line)]] | alt | 10.4 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.124× (z -8.9) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[PANC-1 (line)]] | alt | 10.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.334× (z -10.3) |
| [[SNU-1 (line)]] | wt | 10.6 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0842× (z -8.7) |
| [[A-427 (line)]] | wt | 9.45 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 9.40 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.57 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.75 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.29 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.95 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.22 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.85 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.26 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.23 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.56 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.21 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.19 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.03 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.26 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.21 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.08 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.82 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.03 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.39 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.50 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.10 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 8.00 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6616), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 12 of them with an alert (⚠; 9 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MGAT4B]] | +0.59 | +0.52 / +0.65 | both halves | 1e-05 |  |
| [[FBXW5]] | +0.57 | +0.45 / +0.61 | both halves | 3e-05 |  |
| [[PLEKHN1]] | +0.56 | +0.46 / +0.68 | both halves | 2e-05 |  |
| [[PIP5K1C]] | +0.55 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[KIFC2]] | +0.55 | +0.46 / +0.60 | both halves | 3e-05 |  |
| [[HRAS]] | +0.55 | +0.37 / +0.61 | both halves | 8e-05 |  |
| [[ZFTRAF1]] | +0.54 | +0.30 / +0.68 | both halves | 2e-04 |  |
| [[CSNK1G2]] | +0.53 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[RFNG]] | +0.53 | +0.30 / +0.66 | both halves | 2e-04 |  |
| [[SAP30L]] | +0.52 | +0.41 / +0.57 | both halves | 4e-05 |  |
| [[CRAMP1]] | +0.51 | +0.37 / +0.63 | both halves | 8e-05 |  |
| [[ENKD1]] | +0.50 | +0.36 / +0.58 | both halves | 1e-04 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PAICS]] | -0.45 | -0.20 / -0.53 | both halves | 7e-04 |  |
| [[ZNF484]] | -0.43 | -0.27 / -0.48 | both halves | 3e-04 |  |
| [[TMX1]] | -0.41 | -0.11 / -0.57 | ⚠ one half (not replicated) | 0.002 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.277). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-13.0, -21.0); signed map (-23.7, 4.7). **Vector** length 47.2, 6.71% of its response variance represented; |z| ≥ 3 in 846 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ipatasertib (drug)]] 0.5 µM |  | +1.9 | +3.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +1.6 | -0.2 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.6 | +3.2 |
|  | [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.5 | +2.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +1.4 | -2.0 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.4 | +2.3 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.4 | +3.2 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +1.3 | +0.3 |
| fall | [[Selinexor (drug)]] 0.5 µM |  | -1.6 | -3.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.4 | -2.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.4 | -3.8 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.3 | -2.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -1.1 | -4.0 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.1 | -2.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.0 | -1.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.0 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | arginyl aminopeptidase like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q37.3 — chr2:240,565,804-240,581,372 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | M1 metallopeptidases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HAU8](https://www.uniprot.org/uniprotkb/Q9HAU8) (Aminopeptidase RNPEPL1):

> Broad specificity aminopeptidase which preferentially hydrolyzes an N-terminal methionine, citrulline or glutamine.

**Summary**, from NCBI Gene [57140](https://www.ncbi.nlm.nih.gov/gene/57140):

> Enables metalloaminopeptidase activity. Involved in proteolysis. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:10079](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10079) · Entrez [57140](https://www.ncbi.nlm.nih.gov/gene/57140) · UniProt [Q9HAU8](https://www.uniprot.org/uniprotkb/Q9HAU8) · Ensembl [ENSG00000142327](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000142327)

## Data

Gene col 6616: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6616); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6616, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6616]; `tensor/DDL_lfc|DDL_z.npy` [6616]; `embed/gene_vectors.npy` [6616]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6616 or target_col == 6616). Every well: [[RNPEPL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RNPEPL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
