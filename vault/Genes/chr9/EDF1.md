---
symbol: "EDF1"
type: "gene"
col: 2835
ensembl_id: "ENSG00000107223"
name: "endothelial differentiation related factor 1"
location: "9q34.3"
module: 43
arm: "+"
pooled_cpm: 64.44
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 0
n_dd_up_clean: 0
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/043"]
generated_by: "tahoemap"
---

# EDF1

*endothelial differentiation related factor 1* — 9q34.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.98× (z +8.6, q 5e-15, up in 46 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 12 lines (LoVo 5.54×, SW480 4.39×, SNU-1 7.74×, HEC-1-A 4.04×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H460 4.48×, SW480 4.13×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (SK-MEL-2 0.242×, NCI-H23 0.355×); [[Brimonidine (drug)]] 0.5 µM in 1 line (NCI-H661 0.0852×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 12 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RBIS]] (+0.75, fdr 1e-05), [[ATP5MJ]] (+0.73, fdr 1e-05), [[POLR2I]] (+0.72, fdr 2e-05); moves opposite to [[FGD5-AS1]] (-0.66, fdr 1e-05), [[SNX5]] (-0.65, fdr 2e-05), [[SLC39A10]] (-0.64, fdr 1e-05).
> It sits in the **+** arm of [[Module 043]] (Eukaryotic Translation Elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 5 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2835.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 12 lines (LoVo 5.54×, SW480 4.39×, SNU-1 7.74×, HEC-1-A 4.04×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H460 4.48×, SW480 4.13×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **2.98×** | +8.6 | 5e-15 | 46/49 (LoVo, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **2.49×** | +6.9 | 1e-09 | 35/41 (NCI-H460, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~39% of this change | **1.70×** | +4.2 | 0.005 | 40/48 (NCI-H2347, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.72×** | +4.1 | 0.006 | 39/47 (MIA PaCa-2, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **1.87×** | +3.3 | 0.092 | 33/45 (NCI-H2030, SNU-423, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | 2.30× | +3.2 | 0.14 | 40/48 (HCT15, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | 2.27× | +3.1 | 0.14 | 39/47 (HS-578T, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2835.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (SK-MEL-2 0.242×, NCI-H23 0.355×); [[Brimonidine (drug)]] 0.5 µM in 1 line (NCI-H661 0.0852×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | 0.706× | -3.5 | 0.28 | 30/48 (SK-MEL-2, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, +0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2835. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 49.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.48× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[SW480 (line)]] | alt | 45.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.39× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[A-172 (line)]] | wt | 135 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.15× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[A498 (line)]] | wt | 105 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.25× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[C-33 A (line)]] | alt | 40.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.48× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[HEC-1-A (line)]] | alt | 76.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.04× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[HOP62 (line)]] | alt | 49.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.21× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[LoVo (line)]] | wt | 59.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.54× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[LOX-IMVI (line)]] | wt | 42.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.67× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[NCI-H23 (line)]] | alt | 51.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -8.5) |
| [[NCI-H661 (line)]] | alt | 41.4 | 0 | 1 | — | [[Brimonidine (drug)]] 0.5 µM 0.0852× (z -8.5) |
| [[PANC-1 (line)]] | alt | 48.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.84× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 58.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.242× (z -11.2) |
| [[SNU-1 (line)]] | wt | 43.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.74× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[SNU-423 (line)]] | alt | 69.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.43× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[A-427 (line)]] | wt | 42.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 61.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 51.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 92.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 55.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 47.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 57.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 56.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 56.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 69.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 56.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 65.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 71.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 63.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 58.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 109 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 82.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 52.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 54.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 54.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 51.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 65.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 58.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 72.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 99.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 56.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 55.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 59.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 70.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 67.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 70.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 53.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2835), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 12 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBIS]] | +0.75 | +0.55 / +0.71 | both halves | 1e-05 |  |
| [[ATP5MJ]] | +0.73 | +0.56 / +0.67 | both halves | 1e-05 |  |
| [[POLR2I]] | +0.72 | +0.48 / +0.71 | both halves | 2e-05 | pathway: HALLMARK_DNA_REPAIR |
| [[TMEM256]] | +0.72 | +0.49 / +0.65 | both halves | 1e-05 |  |
| [[RPS26]] | +0.70 | +0.47 / +0.63 | both halves | 2e-05 | STRING 922 |
| [[RPL36]] | +0.68 | +0.59 / +0.70 | both halves | 7e-06 | STRING 928 |
| [[PIGH]] | +0.68 | +0.52 / +0.47 | both halves | 2e-05 |  |
| [[COMMD6]] | +0.67 | +0.58 / +0.61 | both halves | 8e-06 |  |
| [[LAMTOR5]] | +0.67 | +0.54 / +0.68 | both halves | 1e-05 |  |
| [[ATP5ME]] | +0.66 | +0.43 / +0.71 | both halves | 3e-05 |  |
| [[TOMM7]] | +0.66 | +0.47 / +0.71 | both halves | 2e-05 |  |
| [[RNF114]] | +0.66 | +0.47 / +0.57 | both halves | 2e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FGD5-AS1]] | -0.66 | -0.59 / -0.55 | both halves | 1e-05 |  |
| [[SNX5]] | -0.65 | -0.52 / -0.46 | both halves | 2e-05 |  |
| [[SLC39A10]] | -0.64 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[DARS2]] | -0.63 | -0.53 / -0.58 | both halves | 1e-05 |  |
| [[TASOR]] | -0.62 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[SEPTIN11]] | -0.61 | -0.48 / -0.59 | both halves | 2e-05 |  |
| [[HNRNPA2B1]] | -0.61 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[ILF3]] | -0.61 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[EIF4G2]] | -0.60 | -0.34 / -0.44 | both halves | 1e-04 |  |
| [[USP13]] | -0.60 | -0.51 / -0.38 | both halves | 7e-05 |  |
| [[CHRAC1]] | -0.60 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[MSANTD2]] | -0.58 | -0.33 / -0.44 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 043]] — Eukaryotic Translation Elongation; 103 genes; this gene is in the **+** arm (projection on the module's main direction 0.566). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-44.0, -23.0); signed map (-33.8, 6.9). **Vector** length 64.0, 23.0% of its response variance represented; |z| ≥ 3 in 395 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.4 | +3.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.3 | +2.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.1 | +2.7 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.3 | +2.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | +1.3 | -0.5 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | +1.3 | -0.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.2 | +2.3 |
|  | [[PH-797804 (drug)]] 0.5 µM |  | +1.2 | +1.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.1 | +0.5 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.4 | -1.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | -4.0 | +3.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | -3.7 | +6.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.7 | +0.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.6 | -3.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.7 | -0.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.0 | -0.4 |
|  | [[Bentamapimod (drug)]] 5 µM |  | -1.1 | -2.1 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.1 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | endothelial differentiation related factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.3 — chr9:136,862,119-136,866,308 (-) |
| Ensembl biotype | protein_coding |
| Also known as | EDF-1, CFAP280 |
| Gene groups (HGNC) | Cilia and flagella associated |
| Hallmark sets | DNA_REPAIR |
| Matched by | ensembl_id |

**Function**, from UniProt [O60869](https://www.uniprot.org/uniprotkb/O60869) (Endothelial differentiation-related factor 1):

> Transcriptional coactivator stimulating NR5A1 and ligand-dependent NR1H3/LXRA and PPARG transcriptional activities. Enhances the DNA-binding activity of ATF1, ATF2, CREB1 and NR5A1. Regulates nitric oxid synthase activity probably by sequestering calmodulin in the cytoplasm. May function in endothelial cells differentiation, hormone-induced cardiomyocytes hypertrophy and lipid metabolism.

**Summary**, from NCBI Gene [8721](https://www.ncbi.nlm.nih.gov/gene/8721):

> This gene encodes a protein that may regulate endothelial cell differentiation, lipid metabolism, and hormone-induced cardiomyocyte hypertrophy. The encoded protein has also been found to act as a transcriptional coactivator by interconnecting the general transcription factor TATA element-binding protein (TBP) and gene-specific activators. Alternate splicing results in multiple transcript variants. [provided by RefSeq, Jul 2013]

**Accessions** — [HGNC:3164](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3164) · Entrez [8721](https://www.ncbi.nlm.nih.gov/gene/8721) · UniProt [O60869](https://www.uniprot.org/uniprotkb/O60869) · Ensembl [ENSG00000107223](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000107223)

## Data

Gene col 2835: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2835); `tables/drug_effects.parquet` (8 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2835, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2835]; `tensor/DDL_lfc|DDL_z.npy` [2835]; `embed/gene_vectors.npy` [2835]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2835 or target_col == 2835). Every well: [[EDF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EDF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
