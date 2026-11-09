---
symbol: "CCDC85B"
type: "gene"
col: 10631
ensembl_id: "ENSG00000175602"
name: "coiled-coil domain containing 85B"
location: "11q13.1"
module: 3
arm: "+"
pooled_cpm: 23.77
n_lines_expressing: 48
n_dd_up: 3
n_dd_down: 5
n_dd_up_clean: 0
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# CCDC85B

*coiled-coil domain containing 85B* — 11q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.98× (z +6.2, q 4e-07, up in 33 of 37 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (NCI-H1573 17.9×, AsPC-1 8.60×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 0.05 µM: 0.489× (z -3.9, q 0.049, down in 30 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPS26]] (+0.69, fdr 1e-04), [[PPP1R14B]] (+0.68, fdr 7e-06), [[IMP3]] (+0.67, fdr 1e-05); moves opposite to [[MOB1A]] (-0.64, fdr 1e-05), [[BECN1]] (-0.63, fdr 1e-05), [[SMU1]] (-0.63, fdr 9e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10631.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (NCI-H1573 17.9×, AsPC-1 8.60×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **2.98×** | +6.2 | 4e-07 | 33/37 (NCI-H1573, AsPC-1, …) | all doses, flat | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~38% of this change | **2.50×** | +5.3 | 3e-05 | 36/42 (A-172, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.00×** | +3.9 | 0.019 | 28/41 (RKO, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.47× | +3.2 | 0.17 | 24/46 (A-172, LOX-IMVI, …) | rises with dose | position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | 2.56× | +3.2 | 0.17 | 30/45 (NCI-H460, RKO, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10631.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 0.05 µM |  | **0.489×** | -3.9 | 0.049 | 30/45 (A-172, NCI-H2347, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.305×** | -3.6 | 0.069 | 34/44 (NCI-H23, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.523×** | -3.6 | 0.069 | 27/46 (NCI-H2030, H4, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.560×** | -3.4 | 0.099 | 26/44 (HS-578T, MIA PaCa-2, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Sapanisertib (drug)]] 5 µM |  | **0.335×** | -3.3 | 0.099 | 27/46 (SNU-1, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Budesonide (drug)]] 5 µM |  | 0.572× | -3.2 | 0.11 | 28/46 (NCI-H2347, HS-578T, …) | top dose only |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.671× | -3.2 | 0.11 | 24/46 (SW480, AsPC-1, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM |  | 0.519× | -3.1 | 0.13 | 25/46 (AsPC-1, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~20% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, +0.72 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10631. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 32.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.60× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 31.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -10.8) |
| [[NCI-H1573 (line)]] | alt | 13.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 17.9× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[RPMI-7951 (line)]] | alt | 36.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -9.2) |
| [[A-172 (line)]] | wt | 6.75 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 46.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.84 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 44.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.32 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 22.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.10 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.98 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 7.72 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 36.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.92 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 30.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 49.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 42.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.77 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 46.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 36.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 43.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 18.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10631), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 5 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPS26]] | +0.69 | +0.34 / +0.73 | both halves | 1e-04 |  |
| [[PPP1R14B]] | +0.68 | +0.70 / +0.58 | both halves | 7e-06 |  |
| [[IMP3]] | +0.67 | +0.57 / +0.74 | both halves | 1e-05 |  |
| [[B3GAT3]] | +0.67 | +0.46 / +0.69 | both halves | 3e-05 |  |
| [[CDKN2D]] | +0.67 | +0.48 / +0.65 | both halves | 2e-05 |  |
| [[LAGE3]] | +0.67 | +0.43 / +0.68 | both halves | 3e-05 |  |
| [[MIEN1]] | +0.66 | +0.43 / +0.69 | both halves | 3e-05 |  |
| [[ANKRD37]] | +0.65 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[COMMD6]] | +0.64 | +0.42 / +0.67 | both halves | 4e-05 |  |
| [[VPS37C]] | +0.64 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[ARL4C]] | +0.64 | +0.65 / +0.52 | both halves | 1e-05 |  |
| [[CNNM4]] | +0.64 | +0.45 / +0.64 | both halves | 3e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MOB1A]] | -0.64 | -0.51 / -0.64 | both halves | 1e-05 |  |
| [[BECN1]] | -0.63 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[SMU1]] | -0.63 | -0.36 / -0.68 | both halves | 9e-05 |  |
| [[PAPOLA]] | -0.63 | -0.42 / -0.63 | both halves | 4e-05 |  |
| [[ZMYND11]] | -0.61 | -0.45 / -0.57 | both halves | 3e-05 |  |
| [[TRIP12]] | -0.61 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[AP5M1]] | -0.60 | -0.51 / -0.41 | both halves | 4e-05 |  |
| [[FGD5-AS1]] | -0.59 | -0.46 / -0.53 | both halves | 3e-05 |  |
| [[EIF4G2]] | -0.59 | -0.39 / -0.52 | both halves | 6e-05 |  |
| [[HCFC1]] | -0.59 | -0.31 / -0.58 | both halves | 2e-04 |  |
| [[PSME3IP1]] | -0.58 | -0.39 / -0.55 | both halves | 6e-05 |  |
| [[MCM3AP]] | -0.58 | -0.37 / -0.58 | both halves | 8e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.594). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-42.6, -19.4); signed map (-31.3, 11.7). **Vector** length 89.7, 28.7% of its response variance represented; |z| ≥ 3 in 657 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.7 | +3.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.7 | +2.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.6 | +1.7 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.5 | +1.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.5 | +2.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.0 | -0.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +2.6 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.6 | +2.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.5 | +2.0 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -7.4 | +2.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | -6.7 | +6.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.8 | -2.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.5 | +3.0 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~45% of this change | -4.2 | -3.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.6 | -1.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.2 | -1.9 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.2 | -3.6 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -2.1 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | coiled-coil domain containing 85B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.1 — chr11:65,890,673-65,891,635 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DIPA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15834](https://www.uniprot.org/uniprotkb/Q15834) (Coiled-coil domain-containing protein 85B):

> Functions as a transcriptional repressor. May inhibit the activity of CTNNB1 in a TP53-dependent manner and thus regulate cell growth. May function in adipocyte differentiation, negatively regulating mitotic clonal expansion (By similarity). Plays a role in cell-cell adhesion and epithelium development through its interaction with proteins of the beta-catenin family (By similarity).; (Microbial infection) Plays a role in hepatitis delta virus (HDV) genomic replication.

**Summary**, from NCBI Gene [11007](https://www.ncbi.nlm.nih.gov/gene/11007):

> Hepatitis delta virus (HDV) is a pathogenic human virus whose RNA genome and replication cycle resemble those of plant viroids. Delta-interacting protein A (DIPA), a cellular gene product, has been found to have homology to hepatitis delta virus antigen (HDAg). DIPA interacts with the viral antigen, HDAg, and can affect HDV replication in vitro. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:24926](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24926) · Entrez [11007](https://www.ncbi.nlm.nih.gov/gene/11007) · UniProt [Q15834](https://www.uniprot.org/uniprotkb/Q15834) · Ensembl [ENSG00000175602](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175602)

## Data

Gene col 10631: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10631); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10631, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10631]; `tensor/DDL_lfc|DDL_z.npy` [10631]; `embed/gene_vectors.npy` [10631]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10631 or target_col == 10631). Every well: [[CCDC85B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCDC85B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
