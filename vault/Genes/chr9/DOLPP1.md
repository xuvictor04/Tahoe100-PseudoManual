---
symbol: "DOLPP1"
type: "gene"
col: 9424
ensembl_id: "ENSG00000167130"
name: "dolichyldiphosphatase 1"
location: "9q34.11"
module: 7
arm: "+"
pooled_cpm: 3.45
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 0
n_dd_up_clean: 8
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# DOLPP1

*dolichyldiphosphatase 1* — 9q34.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.31× (z +7.7, q 5e-12, up in 4 of 7 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 2.24× (z +7.7, q 5e-12, up in 24 of 43 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[L3MBTL2]] (+0.62, fdr 7e-06), [[CASKIN2]] (+0.61, fdr 7e-06), [[MYG1]] (+0.59, fdr 1e-05); moves opposite to [[FAM81A]] (-0.57, fdr 1e-05), [[PERP]] (-0.54, fdr 3e-05), [[EIF1AX]] (-0.49, fdr 1e-04).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9424.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **2.31×** | +7.7 | 5e-12 | 4/7 (J82, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.24×** | +7.7 | 5e-12 | 24/43 (SW480, PANC-1, …) | two highest doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.66×** | +6.8 | 2e-09 | 17/33 (KATO III, HOP62, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **2.09×** | +6.7 | 2e-09 | 22/42 (SW480, HEC-1-A, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.52×** | +5.7 | 2e-06 | 15/35 (SW480, HEC-1-A, …) | rises with dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~36% of this change | **1.68×** | +4.9 | 7e-05 | 8/20 (SW1417, J82, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.67×** | +4.9 | 8e-05 | 15/47 (SW480, HOP62, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~80% of this change | **1.67×** | +4.9 | 8e-05 | 8/16 (NCI-H460, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.66×** | +4.8 | 9e-05 | 14/46 (SW480, Hs 766T, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.66×** | +4.8 | 9e-05 | 19/47 (HepG2/C3A, PANC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.86×** | +4.5 | 3e-04 | 10/41 (PANC-1, SW48, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.59×** | +4.2 | 0.001 | 8/17 (KATO III, HS-578T, …) | rises with dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.46×** | +3.6 | 0.014 | 10/32 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.69×** | +3.6 | 0.015 | 2/19 (NCI-H460, HS-578T) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~53% of this change | **1.44×** | +3.3 | 0.037 | 3/22 (HS-578T, NCI-H2347, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.62×** | +3.3 | 0.038 | 4/25 (NCI-H460, HS-578T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.59×** | +3.2 | 0.054 | 4/31 (HT-29, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9424.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | 0.776× | -3.5 | 0.21 | 11/46 (SHP-77, NCI-H460, …) | all doses, flat | low cells (technical?) |
| [[Rifaximin (drug)]] 5 µM |  | 0.696× | -3.3 | 0.21 | 10/42 (J82, H4, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.717× | -3.2 | 0.21 | 10/43 (HepG2/C3A, AsPC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~76% of this change | 0.718× | -3.2 | 0.21 | 8/41 (HS-578T, SW 900, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.802× | -3.0 | 0.30 | 12/46 (SNU-1, COLO 205, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.38 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9424. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 3.32 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.25 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.83 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.69 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.13 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.84 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.08 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.58 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.11 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.69 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.08 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.18 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.78 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.92 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.77 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.69 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.91 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.97 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.19 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.76 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.55 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.22 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.03 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.07 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.14 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.00 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.55 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.90 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.57 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.78 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9424), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[L3MBTL2]] | +0.62 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[CASKIN2]] | +0.61 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[MYG1]] | +0.59 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[BRF2]] | +0.59 | +0.66 / +0.43 | both halves | 3e-05 |  |
| [[GFER]] | +0.59 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[LRRC14]] | +0.58 | +0.46 / +0.64 | both halves | 3e-05 |  |
| [[NUDT16L1]] | +0.58 | +0.41 / +0.66 | both halves | 4e-05 |  |
| [[PHF5A]] | +0.57 | +0.44 / +0.59 | both halves | 3e-05 |  |
| [[MSRB1]] | +0.56 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[GPKOW]] | +0.56 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[NUBP2]] | +0.55 | +0.37 / +0.63 | both halves | 8e-05 |  |
| [[THAP7]] | +0.55 | +0.55 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM81A]] | -0.57 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[PERP]] | -0.54 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[EIF1AX]] | -0.49 | -0.36 / -0.56 | both halves | 1e-04 |  |
| [[GLS]] | -0.48 | -0.37 / -0.50 | both halves | 9e-05 |  |
| [[PABPC1]] | -0.47 | -0.46 / -0.50 | both halves | 3e-05 |  |
| [[RPS3A]] | -0.45 | -0.34 / -0.51 | both halves | 1e-04 |  |
| [[RPL6]] | -0.44 | -0.20 / -0.60 | ⚠ one half (not replicated) | 8e-04 |  |
| [[LYRM7]] | -0.44 | -0.30 / -0.35 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.429). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-38.7, -2.8); signed map (-7.2, -23.0). **Vector** length 40.3, 4.31% of its response variance represented; |z| ≥ 3 in 852 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.4 | +7.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +2.4 | +4.8 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +2.2 | +4.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +2.0 | +6.7 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~36% of this change | +1.8 | +4.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.1 | +3.3 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.0 | +3.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +0.9 | +1.3 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +0.8 | +3.2 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -2.5 | -3.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.4 | -2.2 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~76% of this change | -2.1 | -3.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | -1.9 | -3.5 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.4 | -2.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.2 | -2.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -0.8 | -0.1 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -0.8 | -2.7 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.7 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | dolichyldiphosphatase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.11 — chr9:129,081,111-129,090,438 (+) |
| Ensembl biotype | protein_coding |
| Also known as | LSFR2 |
| Gene groups (HGNC) | Lipid phosphatases |
| Reactome | 4 pathways, smallest: Synthesis of dolichyl-phosphate; Synthesis of substrates in N-glycan biosythesis; Biosynthesis of the N-glycan precursor (dolichol lipid-linked oligosaccharide, LLO) and transfer to a nascent protein |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86YN1](https://www.uniprot.org/uniprotkb/Q86YN1) (Dolichyldiphosphatase 1):

> Required for efficient N-glycosylation. Necessary for maintaining optimal levels of dolichol-linked oligosaccharides. Hydrolyzes dolichyl pyrophosphate at a very high rate and dolichyl monophosphate at a much lower rate. Does not act on phosphatidate (By similarity).

**Summary**, from NCBI Gene [57171](https://www.ncbi.nlm.nih.gov/gene/57171):

> A similar gene has been characterized in mice and encodes dolichyl pyrophosphate (Dol-P-P) phosphatase. This protein dephosphorylates dolichyl pyrophosphate so that it may be re-utilized as a glycosyl carrier lipid by the oligosaccharyltransferase multisubunit complex in the ER. Alternative splicing results in multiple transcript variants and protein isoforms. [provided by RefSeq, Jun 2012]

**Accessions** — [HGNC:29565](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29565) · Entrez [57171](https://www.ncbi.nlm.nih.gov/gene/57171) · UniProt [Q86YN1](https://www.uniprot.org/uniprotkb/Q86YN1) · Ensembl [ENSG00000167130](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167130)

## Data

Gene col 9424: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9424); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9424, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9424]; `tensor/DDL_lfc|DDL_z.npy` [9424]; `embed/gene_vectors.npy` [9424]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9424 or target_col == 9424). Every well: [[DOLPP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DOLPP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
