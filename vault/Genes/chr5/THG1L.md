---
symbol: "THG1L"
type: "gene"
col: 3442
ensembl_id: "ENSG00000113272"
name: "tRNA-histidine guanylyltransferase 1 like"
location: "5q33.3"
module: 51
arm: "+"
pooled_cpm: 12.07
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 1
n_dd_up_clean: 7
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/051"]
generated_by: "tahoemap"
---

# THG1L

*tRNA-histidine guanylyltransferase 1 like* — 5q33.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.91× (z +10.9, q 1e-24, up in 36 of 47 measured lines) ⚠ cell-cycle shift, explains ~37% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 1.94× (z +7.9, q 5e-13, up in 35 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 0.719× (z -3.9, q 0.054, down in 18 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (HS-578T 0.0817×); [[Pimozide (drug)]] 0.05 µM in 1 line (NCI-H2030 0.0941×); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (SNU-423 0.114×; ⚠ cell-cycle shift, explains ~17% of this change); [[Roxadustat (drug)]] 0.05 µM in 1 line (C32 0.0857×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[METTL18]] (+0.74, fdr 7e-06), [[YJU2]] (+0.72, fdr 7e-06), [[HMGXB4]] (+0.72, fdr 7e-06); moves opposite to [[TM9SF2]] (-0.69, fdr 7e-06), [[LAPTM4A]] (-0.68, fdr 1e-05), [[SDHA]] (-0.66, fdr 1e-05).
> It sits in the **+** arm of [[Module 051]] (Chromatin modifying enzymes).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3442.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.91×** | +10.9 | 1e-24 | 36/47 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **2.08×** | +8.4 | 2e-14 | 34/46 (PANC-1, NCI-H1573, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.94×** | +7.9 | 5e-13 | 35/44 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.57×** | +5.4 | 9e-06 | 25/47 (NCI-H1573, PANC-1, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.60×** | +5.4 | 9e-06 | 11/21 (HEC-1-A, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **1.39×** | +3.9 | 0.008 | 19/36 (NCI-H2030, Panc 03.27, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.39×** | +3.9 | 0.008 | 14/46 (LOX-IMVI, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.39×** | +3.8 | 0.010 | 14/46 (NCI-H2030, LoVo, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.33×** | +3.4 | 0.037 | 17/47 (HOP62, HT-29, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.31×** | +3.3 | 0.057 | 10/47 (HT-29, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~57% of this change | **1.31×** | +3.3 | 0.057 | 12/41 (HS-578T, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Belzutifan (drug)]] 5 µM |  | **1.66×** | +3.1 | 0.077 | 8/42 (NCI-H460, SW480, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3442.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (HS-578T 0.0817×); [[Pimozide (drug)]] 0.05 µM in 1 line (NCI-H2030 0.0941×); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (SNU-423 0.114×; ⚠ cell-cycle shift, explains ~17% of this change); [[Roxadustat (drug)]] 0.05 µM in 1 line (C32 0.0857×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.719×** | -3.9 | 0.054 | 18/47 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Sildenafil (drug)]] 0.5 µM |  | 0.745× | -3.5 | 0.15 | 9/47 (LoVo, HEC-1-A, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | 0.775× | -3.0 | 0.42 | 12/47 (BT-474, RKO, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, +0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3442. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 10.4 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.94× (z +13.6) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.73× (z +9.2) | — |
| [[HS-578T (line)]] | alt | 9.26 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.59× (z +8.5) ⚠ cell-cycle shift, explains ~37% of this change | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0817× (z -11.7) |
| [[NCI-H1573 (line)]] | alt | 11.7 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.86× (z +10.9) ⚠ cell-cycle shift, explains ~37% of this change | — |
| [[SNU-423 (line)]] | alt | 9.64 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.74× (z +8.5) ⚠ cell-cycle shift, explains ~37% of this change | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.114× (z -9.4) ⚠ cell-cycle shift, explains ~17% of this change |
| [[A-172 (line)]] | wt | 6.38 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.12× (z +8.9) ⚠ cell-cycle shift, explains ~37% of this change | — |
| [[A-427 (line)]] | wt | 12.8 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.171× (z -8.7) ⚠ cell-cycle shift, explains ~22% of this change |
| [[A498 (line)]] | wt | 8.25 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +10.3) ⚠ cell-cycle shift, explains ~37% of this change | — |
| [[A549 (line)]] | wt | 17.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +9.3) ⚠ cell-cycle shift, explains ~37% of this change | — |
| [[BT-474 (line)]] | alt | 8.12 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.95× (z +8.8) ⚠ cell-cycle shift, explains ~37% of this change | — |
| [[C32 (line)]] | wt | 7.82 | 0 | 1 | — | [[Roxadustat (drug)]] 0.05 µM 0.0857× (z -9.0) |
| [[H4 (line)]] | wt | 11.7 | 0 | 1 (1 ⚠) | — | [[Neratinib (maleate) (drug)]] 0.5 µM 0.0982× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 5.48 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.0941× (z -10.0) |
| [[AN3 CA (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.95 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.35 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.12 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.91 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.32 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.72 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.41 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.92 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.76 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 27.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.30 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.64 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 20.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3442), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[METTL18]] | +0.74 | +0.79 / +0.67 | both halves | 7e-06 |  |
| [[YJU2]] | +0.72 | +0.75 / +0.59 | both halves | 7e-06 |  |
| [[HMGXB4]] | +0.72 | +0.66 / +0.68 | both halves | 7e-06 |  |
| [[EPC1]] | +0.70 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[CWC22]] | +0.69 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[ZNF480]] | +0.68 | +0.79 / +0.53 | both halves | 1e-05 |  |
| [[BPTF]] | +0.68 | +0.70 / +0.62 | both halves | 7e-06 |  |
| [[ARL14EP]] | +0.67 | +0.72 / +0.60 | both halves | 7e-06 |  |
| [[RPP25L]] | +0.67 | +0.72 / +0.60 | both halves | 7e-06 |  |
| [[C1orf131]] | +0.67 | +0.74 / +0.58 | both halves | 7e-06 |  |
| [[CCDC174]] | +0.66 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[NAIF1]] | +0.66 | +0.73 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TM9SF2]] | -0.69 | -0.74 / -0.65 | both halves | 7e-06 |  |
| [[LAPTM4A]] | -0.68 | -0.72 / -0.57 | both halves | 1e-05 |  |
| [[SDHA]] | -0.66 | -0.74 / -0.54 | both halves | 1e-05 |  |
| [[RPA1]] | -0.65 | -0.71 / -0.58 | both halves | 7e-06 |  |
| [[MLEC]] | -0.64 | -0.67 / -0.50 | both halves | 1e-05 |  |
| [[SETD3]] | -0.63 | -0.75 / -0.49 | both halves | 1e-05 |  |
| [[SDHAP4]] | -0.63 | -0.70 / -0.51 | both halves | 1e-05 |  |
| [[PMS2P3-1]] | -0.62 | -0.73 / -0.55 | both halves | 1e-05 |  |
| [[PLEKHA8]] | -0.62 | -0.70 / -0.49 | both halves | 1e-05 |  |
| [[WRNIP1]] | -0.61 | -0.71 / -0.46 | both halves | 2e-05 |  |
| [[PDIA6]] | -0.60 | -0.66 / -0.50 | both halves | 1e-05 |  |
| [[IER3IP1]] | -0.60 | -0.70 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 051]] — Chromatin modifying enzymes; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.735). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-35.8, 7.7); signed map (2.8, -20.8). **Vector** length 69.1, 12.6% of its response variance represented; |z| ≥ 3 in 679 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +7.9 | +10.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +6.5 | +8.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.1 | +7.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +3.2 | +5.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.4 | +3.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.8 | +3.8 |
|  | [[EX229 (drug)]] 5 µM |  | +1.8 | +2.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.6 | +2.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.6 | +2.5 |
| fall | [[Auranofin (drug)]] 5 µM |  | -2.6 | -0.7 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.6 | -2.3 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -1.8 | -3.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.6 | -1.6 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | -0.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.4 | -2.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.3 | -0.3 |
|  | [[Goserelin (acetate) (drug)]] 5 µM |  | -1.1 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | tRNA-histidine guanylyltransferase 1 like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q33.3 — chr5:157,731,420-157,741,449 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ICF45, FLJ11601, FLJ20546, IHG-1, hTHG1 |
| Reactome | 3 pathways, smallest: tRNA modification in the nucleus and cytosol; tRNA processing; Metabolism of RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NWX6](https://www.uniprot.org/uniprotkb/Q9NWX6) (Probable tRNA(His) guanylyltransferase):

> Adds a GMP to the 5'-end of tRNA(His) after transcription and RNase P cleavage. This step is essential for proper recognition of the tRNA and for the fidelity of protein synthesis (Probable). Also functions as a guanyl-nucleotide exchange factor/GEF for the MFN1 and MFN2 mitofusins thereby regulating mitochondrial fusion. By regulating both mitochondrial dynamics and bioenergetic function, it contributes to cell survival following oxidative stress.

**Summary**, from NCBI Gene [54974](https://www.ncbi.nlm.nih.gov/gene/54974):

> The protein encoded by this gene is a mitochondrial protein that is induced by high levels of glucose and is associated with diabetic nephropathy. The encoded protein appears to increase mitochondrial biogenesis, which could lead to renal fibrosis. Another function of this protein is that of a guanyltransferase, adding GMP to the 5' end of tRNA(His). Several transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Dec 2015]

**Accessions** — [HGNC:26053](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26053) · Entrez [54974](https://www.ncbi.nlm.nih.gov/gene/54974) · UniProt [Q9NWX6](https://www.uniprot.org/uniprotkb/Q9NWX6) · Ensembl [ENSG00000113272](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000113272)

## Data

Gene col 3442: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3442); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3442, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3442]; `tensor/DDL_lfc|DDL_z.npy` [3442]; `embed/gene_vectors.npy` [3442]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3442 or target_col == 3442). Every well: [[THG1L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/THG1L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
