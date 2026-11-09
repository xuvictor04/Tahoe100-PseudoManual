---
symbol: "NR2C2AP"
type: "gene"
col: 11496
ensembl_id: "ENSG00000184162"
name: "nuclear receptor 2C2 associated protein"
location: "19p13.11"
module: 5
arm: "+"
pooled_cpm: 5.51
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 4
n_dd_up_clean: 2
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# NR2C2AP

*nuclear receptor 2C2 associated protein* — 19p13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.17× (z +6.0, q 1e-06, up in 15 of 21 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change. The strongest without an alert is [[TAK-733 (drug)]] 5 µM: 2.29× (z +3.3, q 0.078, up in 8 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.512× (z -7.4, q 9e-11, down in 29 of 40 measured lines).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRPS12]] (+0.68, fdr 1e-05), [[TIMM10]] (+0.66, fdr 1e-05), [[CHCHD4]] (+0.66, fdr 7e-06); moves opposite to [[MORF4L1]] (-0.59, fdr 3e-04), [[SAR1B]] (-0.57, fdr 2e-05), [[CREBL2]] (-0.53, fdr 3e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 8 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11496.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | **2.17×** | +6.0 | 1e-06 | 15/21 (NCI-H2030, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **2.12×** | +5.8 | 2e-06 | 30/46 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.12×** | +5.6 | 5e-06 | 18/30 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | **2.04×** | +5.3 | 2e-05 | 6/10 (PANC-1, SW1417, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~40% of this change | **1.67×** | +3.8 | 0.016 | 14/32 (SNU-423, NCI-H2030, …) | top dose only | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~31% of this change | **1.56×** | +3.5 | 0.052 | 14/30 (SW1417, J82, …) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change | **1.53×** | +3.3 | 0.078 | 15/39 (A-427, NCI-H2030, …) | top dose only | position effect removed |
| [[TAK-733 (drug)]] 5 µM |  | **2.29×** | +3.3 | 0.078 | 8/39 (NCI-H460, A498, …) | top dose only | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.54×** | +3.2 | 0.087 | 11/41 (SW480, NCI-H2347, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **2.22×** | +3.1 | 0.095 | 7/44 (NCI-H460, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | 2.19× | +3.1 | 0.10 | 4/35 (NCI-H460, SHP-77, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.33× | +3.1 | 0.10 | 10/46 (NCI-H2347, NCI-H2030, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11496.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.512×** | -7.4 | 9e-11 | 29/40 (SK-MEL-2, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.253×** | -5.4 | 2e-05 | 24/43 (RKO, Panc 03.27, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.621×** | -3.6 | 0.064 | 18/43 (LoVo, HEC-1-A, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.728×** | -3.5 | 0.064 | 15/45 (COLO 205, NCI-H2347, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | 0.660× | -3.2 | 0.13 | 11/44 (Panc 03.27, NCI-H2347, …) | rises with dose |  |
| [[Anethole trithione (drug)]] 5 µM |  | 0.752× | -3.2 | 0.15 | 15/47 (H4, AN3 CA, …) | all doses, flat | cell-cycle shift (explains ~14% here) |
| [[PH-797804 (drug)]] 5 µM |  | 0.469× | -3.0 | 0.22 | 17/39 (SNU-423, SW1417, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.59 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11496. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 6.70 | 0 | 1 | — | [[Lipoic acid (drug)]] 0.05 µM 0.0584× (z -8.6) |
| [[LoVo (line)]] | wt | 3.97 | 0 | 1 | — | [[Cobimetinib (drug)]] 5 µM 0.0778× (z -8.8) |
| [[NCI-H460 (line)]] | wt | 3.96 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.188× (z -9.6) |
| [[SK-MEL-2 (line)]] | alt | 8.25 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -10.3) |
| [[SNU-423 (line)]] | alt | 5.44 | 0 | 1 (1 ⚠) | — | [[Vortioxetine (drug)]] 5 µM 0.0840× (z -8.7) ⚠ toxic |
| [[SW1417 (line)]] | alt | 6.47 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.212× (z -8.5) |
| [[SW480 (line)]] | alt | 6.65 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.158× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~83% of this change |
| [[A-172 (line)]] | wt | 4.39 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 8.50 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.72 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.43 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.77 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.95 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.81 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.86 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.68 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.39 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.55 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.55 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.33 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.50 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.36 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.66 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.17 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.58 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.32 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.46 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.91 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.37 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 8.66 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.75 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.75 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.03 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.08 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.88 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.39 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11496), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPS12]] | +0.68 | +0.50 / +0.73 | both halves | 1e-05 |  |
| [[TIMM10]] | +0.66 | +0.50 / +0.71 | both halves | 1e-05 |  |
| [[CHCHD4]] | +0.66 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[DCTPP1]] | +0.63 | +0.57 / +0.66 | both halves | 1e-05 |  |
| [[POLR1G]] | +0.62 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[NOP16]] | +0.60 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[LARS2]] | +0.60 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[DEPDC5]] | +0.59 | +0.42 / +0.65 | both halves | 4e-05 |  |
| [[SPOUT1]] | +0.59 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[MECR]] | +0.58 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[ZMYND19]] | +0.58 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[RRP1]] | +0.57 | +0.51 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MORF4L1]] | -0.59 | -0.28 / -0.68 | both halves | 3e-04 |  |
| [[SAR1B]] | -0.57 | -0.47 / -0.63 | both halves | 2e-05 |  |
| [[CREBL2]] | -0.53 | -0.53 / -0.46 | both halves | 3e-05 |  |
| [[RAB11A]] | -0.50 | -0.62 / -0.43 | both halves | 3e-05 |  |
| [[CHP1]] | -0.49 | -0.44 / -0.60 | both halves | 3e-05 |  |
| [[TAB2]] | -0.49 | -0.61 / -0.41 | both halves | 4e-05 |  |
| [[YWHAZ]] | -0.49 | -0.17 / -0.55 | ⚠ one half (not replicated) | 0.001 |  |
| [[SPDYA]] | -0.49 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[RNF11]] | -0.49 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[RAP1GAP]] | -0.49 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[NDUFA5]] | -0.48 | -0.55 / -0.35 | both halves | 1e-04 |  |
| [[ECH1]] | -0.48 | -0.56 / -0.26 | both halves | 4e-04 |  |
| [[SF3B1]] | -0.48 | -0.42 / -0.44 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.512). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-15.0, -38.8); signed map (-1.2, -49.1). **Vector** length 57.2, 9.80% of its response variance represented; |z| ≥ 3 in 642 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.3 | +5.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~40% of this change | +2.7 | +3.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change | +2.4 | +3.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.3 | +1.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.3 | +3.1 |
|  | [[EX229 (drug)]] 5 µM |  | +2.2 | +2.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.1 | +3.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.1 | +3.3 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.6 | +2.9 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -3.6 | -7.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | -3.3 | -5.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.6 | -3.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -2.5 | -3.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.1 | -3.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.5 | -2.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.5 | -3.6 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | -1.3 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | nuclear receptor 2C2 associated protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.11 — chr19:19,201,409-19,203,414 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TRA16 |
| Reactome | 1 pathways, smallest: Nuclear Receptor transcription pathway |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86WQ0](https://www.uniprot.org/uniprotkb/Q86WQ0) (Nuclear receptor 2C2-associated protein):

> May act as a repressor of NR2C2-mediated transactivation by suppressing the binding between NR2C2/TR4 and the TR4-response element in target genes.

**Summary**, from NCBI Gene [126382](https://www.ncbi.nlm.nih.gov/gene/126382):

> Located in nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:30763](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30763) · Entrez [126382](https://www.ncbi.nlm.nih.gov/gene/126382) · UniProt [Q86WQ0](https://www.uniprot.org/uniprotkb/Q86WQ0) · Ensembl [ENSG00000184162](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184162)

## Data

Gene col 11496: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11496); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11496, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11496]; `tensor/DDL_lfc|DDL_z.npy` [11496]; `embed/gene_vectors.npy` [11496]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11496 or target_col == 11496). Every well: [[NR2C2AP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NR2C2AP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
