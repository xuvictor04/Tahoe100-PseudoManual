---
symbol: "SMG1P6"
type: "gene"
col: 14887
ensembl_id: "ENSG00000254634"
name: "SMG1 pseudogene 6"
location: "16p11.2"
module: 5
arm: "+"
pooled_cpm: 3.76
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 0
n_dd_up_clean: 9
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# SMG1P6

*SMG1 pseudogene 6* — 16p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.08× (z +10.4, q 2e-22, up in 26 of 36 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Docetaxel (drug)]] 0.05 µM in 1 line (AsPC-1 0.102×; ⚠ transcription drop; cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NPIPB11]] (+0.76, fdr 7e-06, ⚠ same locus), [[RNPS1]] (+0.65, fdr 1e-05), [[SMG1P7]] (+0.63, fdr 2e-05), [[GHRLOS]] (+0.63, fdr 3e-05); moves opposite to [[MIER1]] (-0.65, fdr 1e-05), [[ATP5PO]] (-0.64, fdr 7e-05, ⚠ ATP5PO in the vector space only through flagged drug-doses), [[RAB30]] (-0.63, fdr 3e-05), [[RAB9A]] (-0.63, fdr 1e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 9 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14887.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.08×** | +10.4 | 2e-22 | 26/36 (LOX-IMVI, NCI-H460, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[TAK-901 (drug)]] 5 µM |  | **4.83×** | +8.2 | 5e-14 | 27/40 (PANC-1, Hs 766T, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.81×** | +5.7 | 3e-06 | 1/4 (AsPC-1) | inconsistent across doses | cell-cycle shift (explains ~15% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.84×** | +5.6 | 3e-06 | 1/6 (HT-29) | inconsistent across doses | cell-cycle shift (explains ~13% here); composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.74×** | +5.5 | 4e-06 | 17/43 (SHP-77, NCI-H2030, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.51×** | +4.8 | 1e-04 | 3/13 (A498, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~15% here); noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.31×** | +4.4 | 0.001 | 10/34 (PANC-1, NCI-H2030, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.56×** | +4.3 | 0.001 | 7/31 (SW1417, A-172, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.48×** | +3.9 | 0.006 | 10/45 (NCI-H460, AsPC-1, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.47×** | +3.9 | 0.006 | 7/41 (NCI-H2030, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.47×** | +3.8 | 0.007 | 7/45 (KATO III, AsPC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.50×** | +3.8 | 0.007 | 7/42 (HEC-1-A, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~21% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.11× | +3.7 | 0.008 | 4/47 (NCI-H2030, NCI-H460, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.44×** | +3.6 | 0.011 | 12/43 (AsPC-1, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.28×** | +3.5 | 0.019 | 8/37 (LOX-IMVI, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.39×** | +3.3 | 0.033 | 7/45 (LS 180, CHP-212, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14887.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Docetaxel (drug)]] 0.05 µM in 1 line (AsPC-1 0.102×; ⚠ transcription drop; cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | 0.709× | -3.4 | 0.33 | 11/44 (MIA PaCa-2, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~13% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.34 per unit of S-phase module lfc, -0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14887. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 11.8 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.102× (z -10.3) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 4.89 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.91 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.39 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.03 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.27 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.47 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.31 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.08 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.60 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.97 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.27 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.27 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.14 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.13 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.76 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.71 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.90 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.08 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.17 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.68 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.999 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.83 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.30 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.53 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.25 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.44 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.98 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.72 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.94 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.47 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.82 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.82 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14887), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*52 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NPIPB11]] | +0.76 | +0.68 / +0.77 | both halves | 7e-06 | ⚠ same locus (19.1 kb, same strand: neighbours can correlate without regulation) |
| [[RNPS1]] | +0.65 | +0.52 / +0.67 | both halves | 1e-05 |  |
| [[SMG1P7]] | +0.63 | +0.47 / +0.65 | both halves | 2e-05 |  |
| [[GHRLOS]] | +0.63 | +0.44 / +0.66 | both halves | 3e-05 |  |
| [[SPTLC1]] | +0.62 | +0.45 / +0.65 | both halves | 3e-05 |  |
| [[TIMM23B-AGAP6]] | +0.60 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[SECISBP2]] | +0.60 | +0.39 / +0.64 | both halves | 5e-05 |  |
| [[ETF1]] | +0.60 | +0.45 / +0.63 | both halves | 3e-05 |  |
| [[GOLGA3]] | +0.59 | +0.50 / +0.63 | both halves | 1e-05 |  |
| [[PMPCA]] | +0.59 | +0.41 / +0.70 | both halves | 4e-05 |  |
| [[TXNDC5]] | +0.58 | +0.41 / +0.69 | both halves | 4e-05 |  |
| [[FAM53A]] | +0.58 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[BCAP31]] | +0.58 | +0.49 / +0.69 | both halves | 1e-05 |  |

## Genes that move opposite

*48 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MIER1]] | -0.65 | -0.51 / -0.64 | both halves | 1e-05 |  |
| [[ATP5PO]] ⚠ | -0.64 | -0.38 / -0.65 | both halves | 7e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[RAB30]] | -0.63 | -0.44 / -0.59 | both halves | 3e-05 |  |
| [[RAB9A]] | -0.63 | -0.52 / -0.69 | both halves | 1e-05 |  |
| [[HPF1]] | -0.63 | -0.45 / -0.66 | both halves | 3e-05 |  |
| [[HCFC2]] | -0.61 | -0.51 / -0.58 | both halves | 1e-05 |  |
| [[TRAPPC5]] | -0.60 | -0.32 / -0.67 | both halves | 2e-04 |  |
| [[ISCA2]] | -0.60 | -0.41 / -0.69 | both halves | 4e-05 |  |
| [[ZNF592]] | -0.60 | -0.46 / -0.52 | both halves | 3e-05 |  |
| [[RNF114]] | -0.59 | -0.37 / -0.64 | both halves | 7e-05 |  |
| [[COMMD3]] | -0.59 | -0.42 / -0.67 | both halves | 4e-05 |  |
| [[ASB8]] | -0.59 | -0.40 / -0.67 | both halves | 5e-05 |  |
| [[ARL4A]] | -0.59 | -0.43 / -0.58 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.472). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-21.6, -3.7); signed map (-23.4, -45.4). **Vector** length 42.5, 4.31% of its response variance represented; |z| ≥ 3 in 1,105 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +3.0 | +5.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.8 | +10.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.0 | +5.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.5 | +5.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +1.5 | +4.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.3 | +4.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.0 | +1.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +0.8 | +1.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +0.8 | +1.1 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | -1.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.1 | -1.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.1 | -3.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | -2.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.4 | -1.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -1.4 | -3.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.2 | -1.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -1.0 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | SMG1 pseudogene 6 |
| Locus type | pseudogene |
| Location | 16p11.2 — chr16:29,425,800-29,447,026 (-) |
| Ensembl biotype | unprocessed_pseudogene |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:49863](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:49863) · Entrez [100422558](https://www.ncbi.nlm.nih.gov/gene/100422558) · Ensembl [ENSG00000254634](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000254634)

## Data

Gene col 14887: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14887); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14887, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14887]; `tensor/DDL_lfc|DDL_z.npy` [14887]; `embed/gene_vectors.npy` [14887]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14887 or target_col == 14887). Every well: [[SMG1P6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SMG1P6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
