---
symbol: "IER5L"
type: "gene"
col: 12013
ensembl_id: "ENSG00000188483"
name: "immediate early response 5 like"
location: "9q34.11"
module: 4
arm: "-"
pooled_cpm: 10.39
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 0
n_dd_up_clean: 3
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# IER5L

*immediate early response 5 like* — 9q34.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Docetaxel (drug)]] 0.05 µM: 2.14× (z +5.8, q 5e-06, up in 28 of 38 measured lines) ⚠ transcription drop. The strongest without an alert is [[Docetaxel (Trihydrate) (drug)]] 0.5 µM: 1.73× (z +4.1, q 0.004, up in 27 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (BT-474 0.127×, NCI-H2347 0.124×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (AN3 CA 0.0527×); [[Homoharringtonine (drug)]] 5 µM in 1 line (MIA PaCa-2 0.207×; ⚠ cell-cycle shift, explains ~56% of this change); [[Belinostat (drug)]] 5 µM in 1 line (A-172 0.128×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CBX4]] (+0.62, fdr 1e-05), [[PIM3]] (+0.61, fdr 1e-05), [[SAT2]] (+0.60, fdr 1e-05); moves opposite to [[IPO5]] (-0.62, fdr 1e-05), [[EIF2S1]] (-0.61, fdr 1e-05), [[XRCC5]] (-0.61, fdr 1e-05).
> It sits in the **-** arm of [[Module 004]] (MYC targets v1).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12013.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.14×** | +5.8 | 5e-06 | 28/38 (A-172, HEC-1-A, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~20% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.03×** | +5.2 | 7e-05 | 23/40 (CFPAC-1, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.84×** | +4.6 | 8e-04 | 28/45 (NCI-H460, SW1417, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.52×** | +4.4 | 0.001 | 24/45 (AsPC-1, SW1417, …) | top dose only | composition shift; position effect removed |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.73×** | +4.1 | 0.004 | 27/47 (A-172, NCI-H2347, …) | inconsistent across doses | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.59×** | +3.5 | 0.042 | 22/46 (SHP-77, HS-578T, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.98×** | +3.3 | 0.089 | 16/42 (SW480, SNU-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 2 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12013.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (BT-474 0.127×, NCI-H2347 0.124×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (AN3 CA 0.0527×); [[Homoharringtonine (drug)]] 5 µM in 1 line (MIA PaCa-2 0.207×; ⚠ cell-cycle shift, explains ~56% of this change); [[Belinostat (drug)]] 5 µM in 1 line (A-172 0.128×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.880× | -3.4 | 0.44 | 15/48 (SHP-77, C32, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.667× | -3.0 | 0.64 | 16/47 (LOX-IMVI, MIA PaCa-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, +0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12013. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AN3 CA (line)]] | alt | 44.6 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.05 µM 0.0527× (z -10.2) |
| [[A-172 (line)]] | wt | 14.4 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.128× (z -9.2) |
| [[BT-474 (line)]] | alt | 22.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.127× (z -9.9) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 16.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -10.2) ⚠ cell-cycle shift, explains ~56% of this change |
| [[NCI-H2347 (line)]] | alt | 9.11 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.124× (z -9.6) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 9.21 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 0.05 µM 6.97× (z +9.3) ⚠ cell-cycle shift, would explain all of this change | — |
| [[A-427 (line)]] | wt | 6.19 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.93 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.47 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.62 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.72 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.08 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.31 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.63 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.26 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.58 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.86 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.44 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.64 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.01 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.19 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.85 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.57 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.84 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.90 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.47 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.47 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 30.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.37 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.82 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.38 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.62 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12013), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CBX4]] | +0.62 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[PIM3]] | +0.61 | +0.50 / +0.68 | both halves | 1e-05 |  |
| [[SAT2]] | +0.60 | +0.50 / +0.62 | both halves | 1e-05 |  |
| [[HES4]] | +0.59 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[NMB]] | +0.58 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[VASN]] | +0.58 | +0.49 / +0.62 | both halves | 1e-05 |  |
| [[PIM2]] | +0.58 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[MIEN1]] | +0.58 | +0.48 / +0.64 | both halves | 2e-05 |  |
| [[DCTN6-DT]] | +0.57 | +0.45 / +0.64 | both halves | 3e-05 |  |
| [[RBM38]] | +0.57 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[MIR23AHG]] | +0.57 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[PRICKLE3]] | +0.56 | +0.53 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IPO5]] | -0.62 | -0.49 / -0.68 | both halves | 1e-05 |  |
| [[EIF2S1]] | -0.61 | -0.49 / -0.63 | both halves | 1e-05 |  |
| [[XRCC5]] | -0.61 | -0.54 / -0.64 | both halves | 1e-05 |  |
| [[PTPN11]] | -0.60 | -0.47 / -0.65 | both halves | 2e-05 |  |
| [[PRKDC]] | -0.58 | -0.53 / -0.62 | both halves | 1e-05 |  |
| [[UGGT1]] | -0.57 | -0.46 / -0.64 | both halves | 3e-05 |  |
| [[UCHL5]] | -0.57 | -0.42 / -0.62 | both halves | 4e-05 |  |
| [[SLC25A24]] | -0.55 | -0.46 / -0.56 | both halves | 3e-05 |  |
| [[FARSB]] | -0.54 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[KARS1]] | -0.53 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[NUP205]] | -0.53 | -0.48 / -0.55 | both halves | 2e-05 |  |
| [[NUP155]] | -0.53 | -0.48 / -0.55 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **-** arm (projection on the module's main direction -0.496). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (24.2, -4.5); signed map (-3.8, 13.8). **Vector** length 89.8, 21.3% of its response variance represented; |z| ≥ 3 in 666 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +3.3 | +1.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | +3.2 | +4.4 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.9 | +0.8 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.8 | +2.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.5 | +3.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | +3.5 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.9 | +1.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.7 | +1.1 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.3 | +2.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -5.3 | +2.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.5 | +2.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.3 | -0.9 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | -3.1 | -0.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.1 | -1.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.7 | -0.6 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -2.1 | -0.6 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.1 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | immediate early response 5 like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.11 — chr9:129,175,552-129,178,261 (-) |
| Ensembl biotype | protein_coding |
| Also known as | bA247A12.2 |
| Matched by | ensembl_id |

UniProt [Q5T953](https://www.uniprot.org/uniprotkb/Q5T953) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:23679](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23679) · Entrez [389792](https://www.ncbi.nlm.nih.gov/gene/389792) · UniProt [Q5T953](https://www.uniprot.org/uniprotkb/Q5T953) · Ensembl [ENSG00000188483](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000188483)

## Data

Gene col 12013: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12013); `tables/drug_effects.parquet` (9 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12013, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12013]; `tensor/DDL_lfc|DDL_z.npy` [12013]; `embed/gene_vectors.npy` [12013]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12013 or target_col == 12013). Every well: [[IER5L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IER5L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
