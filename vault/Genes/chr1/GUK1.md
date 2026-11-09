---
symbol: "GUK1"
type: "gene"
col: 6801
ensembl_id: "ENSG00000143774"
name: "guanylate kinase 1"
location: "1q42.13"
module: 3
arm: "+"
pooled_cpm: 90.02
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 2
n_dd_up_clean: 0
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# GUK1

*guanylate kinase 1* — 1q42.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.33× (z +5.8, q 3e-06, up in 44 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (NCI-H460 3.53×; ⚠ cell-cycle shift, explains ~94% of this change).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.575× (z -6.4, q 1e-07, down in 38 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 6 lines (C-33 A 0.217×, NCI-H2030 0.324×, Hs 766T 0.348×, RPMI-7951 0.343×, …); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (RPMI-7951 0.241×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CIAO2B]] (+0.78, fdr 7e-06), [[RPL28]] (+0.75, fdr 7e-06), [[B3GAT3]] (+0.73, fdr 7e-06); moves opposite to [[TASOR]] (-0.71, fdr 9e-06), [[U2SURP]] (-0.71, fdr 7e-06), [[UTP20]] (-0.69, fdr 7e-06).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 4 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6801.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (NCI-H460 3.53×; ⚠ cell-cycle shift, explains ~94% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **2.33×** | +5.8 | 3e-06 | 44/49 (SW 900, HEC-1-A, …) | all doses, flat | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~26% of this change | **1.75×** | +4.6 | 0.001 | 41/47 (PANC-1, Panc 03.27, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **1.76×** | +4.5 | 0.001 | 30/43 (LS 180, A498, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **1.61×** | +3.6 | 0.046 | 31/45 (A498, NCI-H2030, …) | all doses, flat | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6801.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 6 lines (C-33 A 0.217×, NCI-H2030 0.324×, Hs 766T 0.348×, RPMI-7951 0.343×, …); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (RPMI-7951 0.241×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.575×** | -6.4 | 1e-07 | 38/48 (C-33 A, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.628×** | -3.8 | 0.047 | 34/48 (RPMI-7951, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.686× | -3.0 | 0.36 | 40/48 (LoVo, SW480, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, +0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6801. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RPMI-7951 (line)]] | alt | 81.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.343× (z -10.0) |
| [[C-33 A (line)]] | alt | 88.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -13.6) |
| [[Hs 766T (line)]] | wt | 200 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.348× (z -10.4) |
| [[HS-578T (line)]] | alt | 72.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.379× (z -9.5) |
| [[NCI-H2030 (line)]] | alt | 72.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -11.4) |
| [[NCI-H460 (line)]] | wt | 103 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.53× (z +8.6) ⚠ cell-cycle shift, explains ~94% of this change | — |
| [[SNU-423 (line)]] | alt | 76.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.382× (z -8.8) |
| [[A-172 (line)]] | wt | 153 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 73.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 109 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 60.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 61.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 179 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 67.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 90.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 90.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 55.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 80.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 90.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 75.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 52.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 73.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 82.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 95.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 88.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 115 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 73.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 68.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 141 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 98.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 125 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 80.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 78.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 69.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 90.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 88.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 82.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 88.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 69.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 63.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 45.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 95.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 57.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 100 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 54.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 67.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 87.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 51.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6801), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CIAO2B]] | +0.78 | +0.70 / +0.76 | both halves | 7e-06 |  |
| [[RPL28]] | +0.75 | +0.70 / +0.70 | both halves | 7e-06 |  |
| [[B3GAT3]] | +0.73 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[COMMD6]] | +0.72 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[RPS21]] | +0.72 | +0.69 / +0.64 | both halves | 7e-06 |  |
| [[KDM4B]] | +0.72 | +0.76 / +0.58 | both halves | 7e-06 |  |
| [[VKORC1]] | +0.72 | +0.70 / +0.68 | both halves | 7e-06 |  |
| [[TMED9]] | +0.71 | +0.69 / +0.61 | both halves | 7e-06 |  |
| [[SEC61G]] | +0.71 | +0.74 / +0.68 | both halves | 7e-06 |  |
| [[OST4]] | +0.71 | +0.74 / +0.71 | both halves | 7e-06 |  |
| [[STK32C]] | +0.71 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[MPG]] | +0.70 | +0.66 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_DNA_REPAIR |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TASOR]] | -0.71 | -0.71 / -0.57 | both halves | 9e-06 |  |
| [[U2SURP]] | -0.71 | -0.68 / -0.60 | both halves | 7e-06 |  |
| [[UTP20]] | -0.69 | -0.66 / -0.64 | both halves | 7e-06 |  |
| [[ZNF644]] | -0.67 | -0.59 / -0.61 | both halves | 7e-06 |  |
| [[ZNF507]] | -0.67 | -0.68 / -0.56 | both halves | 1e-05 |  |
| [[PPP2CA]] | -0.67 | -0.50 / -0.65 | both halves | 1e-05 |  |
| [[DHX9]] | -0.66 | -0.62 / -0.72 | both halves | 7e-06 |  |
| [[DCLRE1A]] | -0.66 | -0.68 / -0.61 | both halves | 7e-06 |  |
| [[EWSR1]] | -0.66 | -0.51 / -0.67 | both halves | 1e-05 |  |
| [[RIF1]] | -0.66 | -0.58 / -0.61 | both halves | 8e-06 |  |
| [[ZMYND11]] | -0.65 | -0.58 / -0.58 | both halves | 7e-06 |  |
| [[BCLAF1]] | -0.65 | -0.57 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.762). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-17.2, -5.0); signed map (-31.6, 13.2). **Vector** length 98.7, 40.5% of its response variance represented; |z| ≥ 3 in 495 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.2 | +2.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.2 | +2.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.9 | +1.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.8 | +1.5 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.8 | +2.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.5 | +2.1 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.1 | +2.0 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.7 | +2.4 |
|  | [[Pimitespib (drug)]] 5 µM |  | +1.6 | +2.0 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -5.3 | -1.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.0 | -6.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | -4.9 | +5.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | -4.8 | +4.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | -4.7 | +3.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.1 | -1.1 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -2.5 | +0.3 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -2.5 | -0.4 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -2.5 | -1.1 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.5 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | guanylate kinase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q42.13 — chr1:228,139,962-228,148,984 (+) |
| Ensembl biotype | protein_coding |
| Hallmark sets | DNA_REPAIR |
| Reactome | 4 pathways, smallest: Azathioprine ADME; Interconversion of nucleotide di- and triphosphates; Drug ADME |
| Matched by | ensembl_id |

**Function**, from UniProt [Q16774](https://www.uniprot.org/uniprotkb/Q16774) (Guanylate kinase):

> Catalyzes the phosphorylation of GMP to GDP. Essential enzyme for recycling GMP and indirectly, cyclic GMP (cGMP). Involved in the cGMP metabolism in photoreceptors (By similarity). It may also have a role in the survival and growth progression of some tumors. In addition to its physiological role, GUK1 is essential for converting prodrugs used for the treatment of cancers and viral infections into their pharmacologically active metabolites, most notably acyclovir, ganciclovir, and …

**Summary**, from NCBI Gene [2987](https://www.ncbi.nlm.nih.gov/gene/2987):

> The protein encoded by this gene is an enzyme that catalyzes the transfer of a phosphate group from ATP to guanosine monophosphate (GMP) to form guanosine diphosphate (GDP). The encoded protein is thought to be a good target for cancer chemotherapy. Several transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jun 2011]

**Accessions** — [HGNC:4693](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4693) · Entrez [2987](https://www.ncbi.nlm.nih.gov/gene/2987) · UniProt [Q16774](https://www.uniprot.org/uniprotkb/Q16774) · Ensembl [ENSG00000143774](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143774)

## Data

Gene col 6801: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6801); `tables/drug_effects.parquet` (7 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6801, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6801]; `tensor/DDL_lfc|DDL_z.npy` [6801]; `embed/gene_vectors.npy` [6801]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6801 or target_col == 6801). Every well: [[GUK1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GUK1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
