---
symbol: "MED7"
type: "gene"
col: 7925
ensembl_id: "ENSG00000155868"
name: "mediator complex subunit 7"
location: "5q33.3"
module: 7
arm: "+"
pooled_cpm: 6.14
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 3
n_dd_up_clean: 3
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# MED7

*mediator complex subunit 7* — 5q33.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Docetaxel (drug)]] 0.05 µM: 1.61× (z +5.5, q 3e-05, up in 18 of 36 measured lines) ⚠ transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.39× (z +5.3, q 4e-05, up in 19 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.641× (z -5.1, q 2e-04, down in 22 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.667× (z -4.6, q 9e-04, down in 16 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Rapamycin (drug)]] 0.5 µM in 1 line (SHP-77 0.0679×); [[Digitoxin (drug)]] 5 µM in 1 line (LS 180 0.101×; ⚠ toxic; transcription drop); [[Imiquimod (maleate) (drug)]] 5 µM in 1 line (NCI-H1792 0.0848×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF426]] (+0.71, fdr 7e-06), [[ZSWIM1]] (+0.70, fdr 7e-06), [[CBLL1]] (+0.68, fdr 7e-06).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7925.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.61×** | +5.5 | 3e-05 | 18/36 (HOP62, KATO III, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~13% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.39×** | +5.3 | 4e-05 | 19/47 (A-172, RKO, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.13× | +4.9 | 2e-04 | 4/48 (HT-29, HS-578T, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.53×** | +4.7 | 5e-04 | 4/11 (SW480, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.29×** | +4.0 | 0.006 | 14/42 (PANC-1, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.55×** | +3.3 | 0.092 | 5/44 (HEC-1-A, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Carbamazepine (drug)]] 5 µM |  | 1.32× | +3.1 | 0.14 | 5/46 (PANC-1, SNU-423, …) | rises with dose | position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | 1.32× | +3.1 | 0.15 | 10/45 (A498, NCI-H2030, …) | rises with dose | composition shift |
| [[Belzutifan (drug)]] 5 µM |  | 1.67× | +3.0 | 0.15 | 1/31 (A498) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7925.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Rapamycin (drug)]] 0.5 µM in 1 line (SHP-77 0.0679×); [[Digitoxin (drug)]] 5 µM in 1 line (LS 180 0.101×; ⚠ toxic; transcription drop); [[Imiquimod (maleate) (drug)]] 5 µM in 1 line (NCI-H1792 0.0848×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.641×** | -5.1 | 2e-04 | 22/43 (LS 180, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.667×** | -4.6 | 9e-04 | 16/47 (J82, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.670×** | -4.6 | 9e-04 | 16/46 (SW480, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.754× | -3.2 | 0.15 | 14/45 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Phenytoin (sodium) (drug)]] 0.05 µM |  | 0.737× | -3.2 | 0.15 | 9/44 (SW48, HT-29, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7925. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 6.09 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.101× (z -9.0) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 3.56 | 0 | 1 | — | [[Imiquimod (maleate) (drug)]] 5 µM 0.0848× (z -8.5) |
| [[SHP-77 (line)]] | alt | 7.00 | 0 | 1 | — | [[Rapamycin (drug)]] 0.5 µM 0.0679× (z -9.9) |
| [[A-172 (line)]] | wt | 6.77 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 9.03 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.94 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.21 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.19 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.52 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.41 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.72 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.40 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.38 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.53 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.86 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.06 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.60 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.24 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.16 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.14 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.39 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.83 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.27 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.16 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.12 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.40 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.48 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.93 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.16 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.34 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.40 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.26 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.95 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.70 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.07 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.58 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.21 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.29 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.96 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.23 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.00 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.34 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.06 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.27 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7925), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF426]] | +0.71 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[ZSWIM1]] | +0.70 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[CBLL1]] | +0.68 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[METTL18]] | +0.67 | +0.72 / +0.62 | both halves | 7e-06 |  |
| [[C12orf43]] | +0.66 | +0.56 / +0.68 | both halves | 1e-05 |  |
| [[ZNF155]] | +0.65 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[POP4]] | +0.65 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[MOCS3]] | +0.64 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[ZSCAN26]] | +0.64 | +0.74 / +0.52 | both halves | 1e-05 |  |
| [[EXOC8]] | +0.64 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[MRPS18A]] | +0.64 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[FAM200A]] | +0.64 | +0.62 / +0.70 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.739). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-35.7, 9.9); signed map (-0.7, -25.8). **Vector** length 44.0, 4.94% of its response variance represented; |z| ≥ 3 in 695 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +2.5 | +5.3 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +2.5 | +5.5 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.4 | +2.6 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.1 | -1.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +2.1 | +3.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.9 | +2.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.8 | +2.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.7 | +2.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.6 | +2.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.4 | +0.3 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -1.8 | -4.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -1.8 | -5.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.6 | -4.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -1.4 | -1.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.3 | -1.2 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.0 | -0.9 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.0 | -2.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.0 | +0.2 |
|  | [[Entecavir (monohydrate) (drug)]] 0.5 µM |  | -0.9 | -1.3 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -0.8 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | mediator complex subunit 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q33.3 — chr5:157,137,424-157,159,019 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CRSP33; previously CRSP9 |
| Gene groups (HGNC) | Mediator complex |
| Reactome | 13 pathways, smallest: Transcriptional regulation of white adipocyte differentiation; RSV-host interactions; Epigenetic regulation of adipogenesis genes by MLL3 and MLL4 complexes |
| Matched by | ensembl_id |

**Function**, from UniProt [O43513](https://www.uniprot.org/uniprotkb/O43513) (Mediator of RNA polymerase II transcription subunit 7):

> Component of the Mediator complex, a coactivator involved in the regulated transcription of nearly all RNA polymerase II-dependent genes. Mediator functions as a bridge to convey information from gene-specific regulatory proteins to the basal RNA polymerase II transcription machinery. Mediator is recruited to promoters by direct interactions with regulatory proteins and serves as a scaffold for the assembly of a functional pre-initiation complex with RNA polymerase II and the general …

**Summary**, from NCBI Gene [9443](https://www.ncbi.nlm.nih.gov/gene/9443):

> The activation of gene transcription is a multistep process that is triggered by factors that recognize transcriptional enhancer sites in DNA. These factors work with co-activators to direct transcriptional initiation by the RNA polymerase II apparatus. The protein encoded by this gene is a subunit of the CRSP (cofactor required for SP1 activation) complex, which, along with TFIID, is required for efficient activation by SP1. This protein is also a component of other multisubunit complexes e.g. …

**Accessions** — [HGNC:2378](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2378) · Entrez [9443](https://www.ncbi.nlm.nih.gov/gene/9443) · UniProt [O43513](https://www.uniprot.org/uniprotkb/O43513) · Ensembl [ENSG00000155868](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000155868)

## Data

Gene col 7925: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7925); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7925, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7925]; `tensor/DDL_lfc|DDL_z.npy` [7925]; `embed/gene_vectors.npy` [7925]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7925 or target_col == 7925). Every well: [[MED7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MED7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
