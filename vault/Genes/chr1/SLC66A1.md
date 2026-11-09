---
symbol: "SLC66A1"
type: "gene"
col: 468
ensembl_id: "ENSG00000040487"
name: "solute carrier family 66 member 1"
location: "1p36.13"
module: 7
arm: "+"
pooled_cpm: 4.87
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 0
n_dd_up_clean: 10
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# SLC66A1

*solute carrier family 66 member 1* — 1p36.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.89× (z +9.0, q 9e-17, up in 28 of 41 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 1 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Clofarabine (drug)]] 0.5 µM in 1 line (HEC-1-A 0.0536×); [[Neratinib (drug)]] 0.05 µM in 1 line (SNU-423 0.0972×); [[Rosiglitazone (drug)]] 5 µM in 1 line (HOP62 0.0790×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EGLN2]] (+0.72, fdr 7e-06), [[SLC38A7]] (+0.68, fdr 7e-06), [[CC2D1B]] (+0.67, fdr 1e-05); moves opposite to [[PPP1CB]] (-0.61, fdr 7e-06), [[TMEM106C]] (-0.60, fdr 1e-05), [[SKP2]] (-0.58, fdr 2e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 1 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 468.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.89×** | +9.0 | 9e-17 | 28/41 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.02×** | +7.1 | 4e-10 | 27/38 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.53×** | +6.0 | 4e-07 | 24/40 (KATO III, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.76×** | +5.4 | 1e-05 | 22/44 (H4, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~1% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.65×** | +5.0 | 5e-05 | 17/46 (HepG2/C3A, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.64×** | +4.7 | 2e-04 | 20/43 (PANC-1, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.60×** | +4.7 | 2e-04 | 21/44 (SW480, A-172, …) | rises with dose |  |
| [[Rapamycin (drug)]] 5 µM |  | **1.31×** | +3.8 | 0.011 | 10/45 (NCI-H460, NCI-H1573, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.61×** | +3.4 | 0.038 | 7/42 (A498, HOP62, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.58×** | +3.3 | 0.060 | 8/42 (PANC-1, SNU-423, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.40×** | +3.2 | 0.066 | 5/27 (A-427, KATO III, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | 1.53× | +3.1 | 0.11 | 2/28 (MIA PaCa-2, A498) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 468.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 1 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Clofarabine (drug)]] 0.5 µM in 1 line (HEC-1-A 0.0536×); [[Neratinib (drug)]] 0.05 µM in 1 line (SNU-423 0.0972×); [[Rosiglitazone (drug)]] 5 µM in 1 line (HOP62 0.0790×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | 0.529× | -3.3 | 0.28 | 11/44 (J82, HS-578T, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.793× | -3.3 | 0.28 | 9/46 (NCI-H460, BT-474, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 468. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-423 (line)]] | alt | 5.89 | 0 | 2 | — | [[Neratinib (drug)]] 0.05 µM 0.0972× (z -9.4) |
| [[A-172 (line)]] | wt | 5.35 | 0 | 1 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.126× (z -8.9) ⚠ toxic |
| [[CFPAC-1 (line)]] | alt | 3.56 | 0 | 1 | — | [[Hesperidin (drug)]] 5 µM 0.0849× (z -8.5) |
| [[HEC-1-A (line)]] | alt | 3.78 | 0 | 1 | — | [[Clofarabine (drug)]] 0.5 µM 0.0536× (z -10.8) |
| [[HOP62 (line)]] | alt | 3.72 | 0 | 1 | — | [[Rosiglitazone (drug)]] 5 µM 0.0790× (z -9.3) |
| [[NCI-H2347 (line)]] | alt | 3.51 | 0 | 1 | — | [[Tadalafil (drug)]] 5 µM 0.104× (z -8.8) |
| [[NCI-H460 (line)]] | wt | 4.28 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.66× (z +10.9) | — |
| [[PANC-1 (line)]] | alt | 5.73 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.22× (z +9.2) | — |
| [[A-427 (line)]] | wt | 8.96 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.43 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.50 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.38 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.33 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.79 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.70 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.22 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.98 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.63 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.11 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.75 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.33 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.96 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.16 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.36 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.86 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.94 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.06 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.35 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.33 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.72 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.64 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.55 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.59 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.38 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.10 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.58 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.75 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.89 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.06 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.48 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 468), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EGLN2]] | +0.72 | +0.69 / +0.73 | both halves | 7e-06 |  |
| [[SLC38A7]] | +0.68 | +0.73 / +0.62 | both halves | 7e-06 | STRING 594 |
| [[CC2D1B]] | +0.67 | +0.73 / +0.53 | both halves | 1e-05 |  |
| [[COMMD5]] | +0.64 | +0.57 / +0.69 | both halves | 1e-05 |  |
| [[CDK3]] | +0.64 | +0.68 / +0.55 | both halves | 1e-05 |  |
| [[LRRC8E]] | +0.63 | +0.66 / +0.68 | both halves | 7e-06 | pathway: Miscellaneous transport and binding events |
| [[ZNF579]] | +0.62 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[WASHC1]] | +0.62 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[CD2BP2]] | +0.61 | +0.63 / +0.57 | both halves | 1e-05 |  |
| [[TSSC4]] | +0.61 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[UBE2J2]] | +0.61 | +0.62 / +0.58 | both halves | 8e-06 |  |
| [[ZDHHC1]] | +0.60 | +0.62 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP1CB]] | -0.61 | -0.64 / -0.64 | both halves | 7e-06 |  |
| [[TMEM106C]] | -0.60 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[SKP2]] | -0.58 | -0.63 / -0.48 | both halves | 2e-05 |  |
| [[KDM1A]] | -0.58 | -0.65 / -0.51 | both halves | 1e-05 |  |
| [[PGAM1]] | -0.57 | -0.62 / -0.54 | both halves | 1e-05 |  |
| [[RPS3A]] | -0.55 | -0.57 / -0.57 | both halves | 1e-05 |  |
| [[NUDT21]] | -0.55 | -0.63 / -0.49 | both halves | 1e-05 |  |
| [[PODXL2]] | -0.55 | -0.57 / -0.42 | both halves | 4e-05 |  |
| [[GGH]] | -0.55 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[TMEM30A]] | -0.54 | -0.56 / -0.57 | both halves | 1e-05 |  |
| [[ERMP1]] | -0.54 | -0.52 / -0.56 | both halves | 1e-05 |  |
| [[STT3B]] | -0.54 | -0.53 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.575). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-45.1, 11.8); signed map (1.3, -10.3). **Vector** length 65.4, 10.2% of its response variance represented; |z| ≥ 3 in 840 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +5.5 | +9.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.4 | +7.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +3.3 | +5.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +3.2 | +5.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.0 | +4.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.9 | +4.7 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.0 | +3.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.0 | +2.3 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.0 | +3.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | +2.9 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.8 | -3.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.8 | -2.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.5 | -3.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.3 | -2.6 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.1 | -1.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.9 | -2.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.6 | -0.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.3 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 66 member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.13 — chr1:19,312,326-19,329,300 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20320, LAAT-1, LAAT1; previously PQLC2 |
| Gene groups (HGNC) | Solute carrier family 66 |
| Reactome | 2 pathways, smallest: Miscellaneous transport and binding events; Transport of small molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6ZP29](https://www.uniprot.org/uniprotkb/Q6ZP29) (Lysosomal amino acid transporter 1 homolog):

> Amino acid transporter that specifically mediates the pH-dependent export of the cationic amino acids arginine, histidine and lysine from lysosomes.

**Summary**, from NCBI Gene [54896](https://www.ncbi.nlm.nih.gov/gene/54896):

> Enables L-arginine transmembrane transporter activity; L-histidine transmembrane transporter activity; and L-lysine transmembrane transporter activity. Involved in L-amino acid transport and intracellular amino acid homeostasis. Located in lysosomal membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26001](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26001) · Entrez [54896](https://www.ncbi.nlm.nih.gov/gene/54896) · UniProt [Q6ZP29](https://www.uniprot.org/uniprotkb/Q6ZP29) · Ensembl [ENSG00000040487](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000040487)

## Data

Gene col 468: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 468); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 468, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 468]; `tensor/DDL_lfc|DDL_z.npy` [468]; `embed/gene_vectors.npy` [468]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 468 or target_col == 468). Every well: [[SLC66A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC66A1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
