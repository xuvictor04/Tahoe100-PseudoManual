---
symbol: "YIF1A"
type: "gene"
col: 10535
ensembl_id: "ENSG00000174851"
name: "Yip1 interacting factor homolog A, membrane trafficking protein"
location: "11q13.2"
module: 12
arm: "+"
pooled_cpm: 17.27
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 4
n_dd_up_clean: 0
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# YIF1A

*Yip1 interacting factor homolog A, membrane trafficking protein* — 11q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 1.93× (z +5.4, q 3e-05, up in 29 of 42 measured lines) ⚠ toxic. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[PH-797804 (drug)]] 5 µM: 0.208× (z -6.7, q 1e-08, down in 41 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KRTCAP2]] (+0.70, fdr 7e-06), [[MRPL2]] (+0.68, fdr 7e-06), [[ALG2]] (+0.67, fdr 8e-06); moves opposite to [[HNRNPA3]] (-0.65, fdr 1e-05), [[RBBP4]] (-0.62, fdr 1e-05), [[RPS3A]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 5 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10535.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.93×** | +5.4 | 3e-05 | 29/42 (NCI-H1573, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~49% of this change | **1.64×** | +4.2 | 0.006 | 28/44 (PANC-1, A-427, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.51×** | +3.5 | 0.071 | 21/47 (LoVo, NCI-H1573, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.50×** | +3.5 | 0.071 | 20/47 (NCI-H1573, NCI-H2030, …) | two highest doses | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.46× | +3.2 | 0.14 | 17/45 (MIA PaCa-2, NCI-H1573, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | 1.45× | +3.2 | 0.14 | 18/37 (A-172, HEC-1-A, …) | rises with dose | composition shift; position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10535.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **0.208×** | -6.7 | 1e-08 | 41/45 (SW 900, SW480, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.238×** | -6.1 | 3e-07 | 39/48 (KATO III, SW1417, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.625×** | -3.8 | 0.023 | 24/47 (C32, BT-474, …) | inconsistent across doses |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.640×** | -3.7 | 0.027 | 24/46 (H4, C32, …) | top dose only | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | 0.767× | -3.3 | 0.13 | 26/46 (RKO, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~92% of this change | 0.773× | -3.2 | 0.15 | 24/48 (HS-578T, Hs 766T, …) | rises with dose | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 0.701× | -3.1 | 0.17 | 19/48 (HS-578T, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.54 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10535. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 7.94 | 0 | 1 | — | [[TAK-901 (drug)]] 0.05 µM 0.0776× (z -8.8) |
| [[HepG2_C3A (line)]] | wt | 10.9 | 0 | 1 | — | [[Pravastatin (sodium) (drug)]] 0.05 µM 0.0553× (z -9.5) |
| [[SW48 (line)]] | wt | 11.2 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0603× (z -9.4) |
| [[A-172 (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 26.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 25.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.82 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.52 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 8.67 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.18 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 13.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10535), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KRTCAP2]] | +0.70 | +0.58 / +0.77 | both halves | 7e-06 |  |
| [[MRPL2]] | +0.68 | +0.63 / +0.70 | both halves | 7e-06 |  |
| [[ALG2]] | +0.67 | +0.58 / +0.68 | both halves | 8e-06 |  |
| [[MED19]] | +0.66 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[TIMM17B]] ⚠ | +0.61 | +0.58 / +0.59 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[ZCCHC9]] | +0.61 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[NDUFV3]] | +0.61 | +0.63 / +0.58 | both halves | 8e-06 |  |
| [[RNF166]] | +0.61 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[CREB3]] | +0.60 | +0.64 / +0.54 | both halves | 1e-05 | pathway: Unfolded Protein Response (UPR) |
| [[PREB]] | +0.60 | +0.45 / +0.66 | both halves | 3e-05 | pathway: HALLMARK_UNFOLDED_PROTEIN_RESPONSE; STRING 584 |
| [[ZNF593]] | +0.60 | +0.50 / +0.65 | both halves | 1e-05 |  |
| [[C14orf119]] | +0.60 | +0.63 / +0.67 | both halves | 7e-06 |  |
| [[NKAP]] | +0.60 | +0.54 / +0.63 | both halves | 1e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HNRNPA3]] | -0.65 | -0.55 / -0.70 | both halves | 1e-05 |  |
| [[RBBP4]] | -0.62 | -0.53 / -0.59 | both halves | 1e-05 |  |
| [[RPS3A]] | -0.61 | -0.53 / -0.66 | both halves | 1e-05 |  |
| [[SUMO1]] | -0.59 | -0.54 / -0.61 | both halves | 1e-05 |  |
| [[RPL6]] | -0.58 | -0.45 / -0.63 | both halves | 3e-05 |  |
| [[APP]] | -0.57 | -0.50 / -0.63 | both halves | 1e-05 |  |
| [[FKBP9]] | -0.56 | -0.44 / -0.58 | both halves | 3e-05 |  |
| [[DHFR]] | -0.56 | -0.37 / -0.62 | both halves | 9e-05 |  |
| [[FUT10]] | -0.55 | -0.42 / -0.58 | both halves | 4e-05 |  |
| [[STT3B]] | -0.55 | -0.51 / -0.58 | both halves | 1e-05 |  |
| [[FAM81A]] | -0.54 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[ANO7]] | -0.54 | -0.54 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.575). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-40.1, -11.0); signed map (-12.8, -6.1). **Vector** length 85.5, 22.4% of its response variance represented; |z| ≥ 3 in 669 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | +5.1 | +3.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +4.5 | +2.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +4.1 | +0.3 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +3.8 | +3.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.8 | +3.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.6 | +2.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.6 | +3.0 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +2.2 | +2.5 |
|  | [[vincristine (drug)]] 0.5 µM |  | +2.0 | +2.9 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.8 | -0.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.5 | +2.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | -4.2 | +3.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.0 | -6.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | -4.0 | -6.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.5 | -3.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.3 | -1.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.1 | -1.1 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -2.0 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | Yip1 interacting factor homolog A, membrane trafficking protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.2 — chr11:66,284,572-66,289,184 (-) |
| Ensembl biotype | protein_coding |
| Also known as | YIF1P, 54TM, FinGER7; previously YIF1 |
| Gene groups (HGNC) | YIP superfamily |
| Hallmark sets | UNFOLDED_PROTEIN_RESPONSE |
| Reactome | 5 pathways, smallest: XBP1(S) activates chaperone genes; IRE1alpha activates chaperones; Unfolded Protein Response (UPR) |
| Matched by | ensembl_id |

**Function**, from UniProt [O95070](https://www.uniprot.org/uniprotkb/O95070) (Protein YIF1A):

> Possible role in transport between endoplasmic reticulum and Golgi.

**Summary**, from NCBI Gene [10897](https://www.ncbi.nlm.nih.gov/gene/10897):

> Predicted to be involved in endoplasmic reticulum to Golgi vesicle-mediated transport. Located in Golgi apparatus and endoplasmic reticulum-Golgi intermediate compartment. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:16688](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16688) · Entrez [10897](https://www.ncbi.nlm.nih.gov/gene/10897) · UniProt [O95070](https://www.uniprot.org/uniprotkb/O95070) · Ensembl [ENSG00000174851](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000174851)

## Data

Gene col 10535: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10535); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10535, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10535]; `tensor/DDL_lfc|DDL_z.npy` [10535]; `embed/gene_vectors.npy` [10535]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10535 or target_col == 10535). Every well: [[YIF1A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/YIF1A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
