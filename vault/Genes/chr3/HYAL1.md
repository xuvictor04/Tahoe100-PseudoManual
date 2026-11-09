---
symbol: "HYAL1"
type: "gene"
col: 3545
ensembl_id: "ENSG00000114378"
name: "hyaluronidase 1"
location: "3p21.31"
module: 38
arm: "+"
pooled_cpm: 2.43
n_lines_expressing: 49
n_dd_up: 12
n_dd_down: 4
n_dd_up_clean: 7
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/038"]
generated_by: "tahoemap"
---

# HYAL1

*hyaluronidase 1* — 3p21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.52× (z +13.9, q 3e-41, up in 28 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.512× (z -5.3, q 7e-05, down in 20 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATP2A1]] (+0.73, fdr 7e-06), [[MASP2]] (+0.71, fdr 7e-06), [[PHYHD1]] (+0.71, fdr 7e-06); moves opposite to [[LANCL1]] (-0.59, fdr 1e-05), [[NT5DC1]] (-0.58, fdr 3e-05), [[STX17]] (-0.56, fdr 2e-04).
> It is in [[Module 038]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3545.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.52×** | +13.9 | 3e-41 | 28/31 (HEC-1-A, A498, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.75×** | +7.6 | 7e-12 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.32×** | +6.3 | 4e-08 | 4/12 (PANC-1, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.77×** | +4.5 | 0.001 | 14/41 (Panc 03.27, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~19% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.75×** | +4.4 | 0.001 | 11/32 (NCI-H460, LOX-IMVI, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.82×** | +4.0 | 0.006 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.65×** | +3.9 | 0.008 | 8/42 (RPMI-7951, Panc 03.27, …) | two highest doses | cell-cycle shift (explains ~24% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.62×** | +3.6 | 0.021 | 6/26 (A498, NCI-H460, …) | top dose only | cell-cycle shift (explains ~19% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.56×** | +3.4 | 0.035 | 5/14 (HEC-1-A, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.82×** | +3.3 | 0.046 | 1/28 (A-172) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Macitentan (drug)]] 5 µM |  | **1.54×** | +3.2 | 0.063 | 6/34 (SW480, C-33 A, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.49×** | +3.1 | 0.087 | 9/38 (NCI-H460, AsPC-1, …) | two highest doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3545.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.512×** | -5.3 | 7e-05 | 20/45 (hTERT-HPNE, A549, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.588×** | -4.2 | 0.008 | 15/41 (NCI-H460, LS 180, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.586×** | -4.1 | 0.010 | 15/37 (LS 180, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.642×** | -3.5 | 0.067 | 13/38 (BT-474, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.27 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3545. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 2.44 | 0 | 1 | — | [[Fenofibrate (drug)]] 5 µM 0.0709× (z -8.6) |
| [[NCI-H460 (line)]] | wt | 4.63 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.134× (z -9.3) |
| [[A-172 (line)]] | wt | 2.06 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.67 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.12 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.68 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.00 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.75 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.92 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.972 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.23 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.27 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.44 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.33 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.61 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.35 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.54 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.10 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.489 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.969 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.55 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.15 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.991 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.02 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.72 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3545), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP2A1]] | +0.73 | +0.67 / +0.76 | both halves | 7e-06 |  |
| [[MASP2]] | +0.71 | +0.60 / +0.77 | both halves | 7e-06 |  |
| [[PHYHD1]] | +0.71 | +0.59 / +0.78 | both halves | 7e-06 |  |
| [[IL9RP3]] | +0.68 | +0.63 / +0.73 | both halves | 7e-06 |  |
| [[TTLL3]] | +0.68 | +0.58 / +0.71 | both halves | 8e-06 |  |
| [[MYO15A]] | +0.68 | +0.71 / +0.66 | both halves | 7e-06 |  |
| [[UCKL1-AS1]] | +0.68 | +0.68 / +0.69 | both halves | 7e-06 |  |
| [[CPT1C]] | +0.67 | +0.64 / +0.69 | both halves | 7e-06 |  |
| [[LINC00672]] | +0.65 | +0.56 / +0.72 | both halves | 1e-05 |  |
| [[SYCE1L]] | +0.65 | +0.54 / +0.68 | both halves | 1e-05 |  |
| [[ST6GALNAC6-1]] | +0.65 | +0.49 / +0.75 | both halves | 1e-05 |  |
| [[MYH3]] | +0.65 | +0.65 / +0.69 | both halves | 7e-06 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LANCL1]] | -0.59 | -0.57 / -0.59 | both halves | 1e-05 |  |
| [[NT5DC1]] | -0.58 | -0.46 / -0.55 | both halves | 3e-05 |  |
| [[STX17]] | -0.56 | -0.30 / -0.59 | both halves | 2e-04 |  |
| [[MBTPS2]] | -0.54 | -0.39 / -0.59 | both halves | 5e-05 |  |
| [[PTAR1]] | -0.53 | -0.44 / -0.54 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 038]]; 122 genes; every member is in the + arm (projection on the module's main direction 0.683). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (36.9, -20.4); signed map (13.4, 13.1). **Vector** length 48.3, 6.41% of its response variance represented; |z| ≥ 3 in 876 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.7 | +13.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.3 | +7.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.7 | +4.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.4 | +3.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.0 | +2.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.0 | +2.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.9 | +2.9 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +1.8 | +1.6 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.6 | +1.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.6 | +3.1 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -2.8 | -4.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.4 | -5.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.2 | -4.1 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | -1.6 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.8 | -3.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.7 | -1.5 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.5 | -0.8 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.4 | -1.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.4 | -1.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.3 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | hyaluronidase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.31 — chr3:50,299,890-50,312,381 (-) |
| Ensembl biotype | protein_coding |
| Also known as | LUCA1, HYAL-1 |
| Gene groups (HGNC) | Hyaluronidases |
| Reactome | 9 pathways, smallest: Mucopolysaccharidoses; Hyaluronan degradation; CS/DS degradation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q12794](https://www.uniprot.org/uniprotkb/Q12794) (Hyaluronidase-1):

> May have a role in promoting tumor progression. May block the TGFB1-enhanced cell growth.

**Summary**, from NCBI Gene [3373](https://www.ncbi.nlm.nih.gov/gene/3373):

> This gene encodes a lysosomal hyaluronidase. Hyaluronidases intracellularly degrade hyaluronan, one of the major glycosaminoglycans of the extracellular matrix. Hyaluronan is thought to be involved in cell proliferation, migration and differentiation. This enzyme is active at an acidic pH and is the major hyaluronidase in plasma. Mutations in this gene are associated with mucopolysaccharidosis type IX, or hyaluronidase deficiency. The gene is one of several related genes in a region of …

**Accessions** — [HGNC:5320](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5320) · Entrez [3373](https://www.ncbi.nlm.nih.gov/gene/3373) · UniProt [Q12794](https://www.uniprot.org/uniprotkb/Q12794) · Ensembl [ENSG00000114378](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000114378)

## Data

Gene col 3545: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3545); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3545, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3545]; `tensor/DDL_lfc|DDL_z.npy` [3545]; `embed/gene_vectors.npy` [3545]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3545 or target_col == 3545). Every well: [[HYAL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HYAL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
