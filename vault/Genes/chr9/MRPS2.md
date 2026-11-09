---
symbol: "MRPS2"
type: "gene"
col: 4323
ensembl_id: "ENSG00000122140"
name: "mitochondrial ribosomal protein S2"
location: "9q34.3"
module: 33
arm: "+"
pooled_cpm: 13.09
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 7
n_dd_up_clean: 1
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# MRPS2

*mitochondrial ribosomal protein S2* — 9q34.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 1.64× (z +5.0, q 3e-04, up in 22 of 41 measured lines) ⚠ toxic. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 1.44× (z +3.9, q 0.019, up in 22 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.704× (z -5.4, q 4e-05, down in 26 of 46 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NOB1]] (+0.71, fdr 7e-06), [[ZNF74]] (+0.66, fdr 9e-06), [[NIFK]] (+0.63, fdr 3e-05); moves opposite to [[FAM81A]] (-0.55, fdr 4e-05), [[CYB5D2]] (-0.53, fdr 4e-05), [[ARGLU1]] (-0.51, fdr 2e-04).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4323.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.64×** | +5.0 | 3e-04 | 22/41 (RKO, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~46% of this change | **1.45×** | +4.0 | 0.019 | 18/42 (PANC-1, HS-578T, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.44×** | +3.9 | 0.019 | 22/46 (NCI-H2030, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~22% here) |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **1.40×** | +3.6 | 0.043 | 11/47 (NCI-H460, A498, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | 1.77× | +3.2 | 0.16 | 9/45 (HEC-1-A, A498, …) | top dose only | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4323.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.704×** | -5.4 | 4e-05 | 26/46 (NCI-H460, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.670×** | -4.3 | 0.003 | 24/47 (HOP62, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.660×** | -4.3 | 0.003 | 23/46 (RPMI-7951, C-33 A, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.676×** | -4.1 | 0.006 | 21/46 (SNU-423, MIA PaCa-2, …) | top dose only | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.700×** | -3.8 | 0.015 | 17/46 (NCI-H460, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.715×** | -3.6 | 0.030 | 12/48 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~16% here); noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.794×** | -3.6 | 0.030 | 20/44 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.732× | -3.1 | 0.12 | 12/47 (NCI-H460, SW480, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, +0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4323. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 27.8 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.192× (z -16.8) |
| [[MIA PaCa-2 (line)]] | alt | 24.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -13.0) |
| [[SK-MEL-2 (line)]] | alt | 12.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.286× (z -8.5) |
| [[SNU-1 (line)]] | wt | 12.0 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 0.5 µM 0.0892× (z -8.5) ⚠ cell-cycle shift, would explain all of this change |
| [[SNU-423 (line)]] | alt | 12.0 | 0 | 1 | — | [[Cobimetinib (drug)]] 5 µM 0.163× (z -9.1) |
| [[A-172 (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.12 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.94 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.82 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.73 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.96 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.96 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.29 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.35 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.31 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.99 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.78 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.92 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.63 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.36 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.19 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.45 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.87 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.02 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.82 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 36.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.43 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.90 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 16.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4323), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NOB1]] | +0.71 | +0.64 / +0.68 | both halves | 7e-06 | STRING 592 |
| [[ZNF74]] | +0.66 | +0.60 / +0.57 | both halves | 9e-06 |  |
| [[NIFK]] | +0.63 | +0.44 / +0.67 | both halves | 3e-05 |  |
| [[UBL4A]] | +0.63 | +0.52 / +0.64 | both halves | 1e-05 |  |
| [[MRPL10]] | +0.63 | +0.49 / +0.63 | both halves | 1e-05 | same gene group; pathway: Mitochondrial ribosome-associated quality control; STRING 954 |
| [[MRPS26]] | +0.62 | +0.51 / +0.61 | both halves | 1e-05 | same gene group; pathway: Mitochondrial ribosome-associated quality control; STRING 991 |
| [[NLE1]] | +0.61 | +0.64 / +0.52 | both halves | 1e-05 |  |
| [[CDPF1]] | +0.61 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[NOA1]] | +0.60 | +0.48 / +0.58 | both halves | 2e-05 | STRING 905 |
| [[MYG1]] | +0.59 | +0.47 / +0.60 | both halves | 2e-05 |  |
| [[NSUN5]] | +0.59 | +0.44 / +0.59 | both halves | 3e-05 |  |
| [[PDRG1]] | +0.59 | +0.33 / +0.63 | both halves | 1e-04 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM81A]] | -0.55 | -0.41 / -0.54 | both halves | 4e-05 |  |
| [[CYB5D2]] | -0.53 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[ARGLU1]] | -0.51 | -0.32 / -0.54 | both halves | 2e-04 |  |
| [[MSTO1]] | -0.49 | -0.33 / -0.48 | both halves | 1e-04 |  |
| [[PTMS]] | -0.48 | -0.39 / -0.39 | both halves | 6e-05 |  |
| [[CROCC]] | -0.48 | -0.19 / -0.54 | ⚠ one half (not replicated) | 8e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.554). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-45.3, -7.8); signed map (-6.9, -28.5). **Vector** length 71.4, 14.2% of its response variance represented; |z| ≥ 3 in 654 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +3.2 | +3.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.9 | +2.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.7 | +5.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +2.3 | +2.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.1 | +3.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.8 | +2.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.8 | +2.8 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.7 | +2.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.7 | +1.5 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.6 | +1.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.1 | +2.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.9 | -2.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.0 | -4.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.7 | -2.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.6 | -4.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.3 | -2.2 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -2.0 | -2.0 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -2.0 | -2.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.9 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial ribosomal protein S2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.3 — chr9:135,499,984-135,504,673 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CGI-91, uS2m |
| Gene groups (HGNC) | Mitochondrial ribosomal proteins; Small subunit mitochondrial ribosomal proteins |
| Reactome | 7 pathways, smallest: Mitochondrial ribosome-associated quality control; Mitochondrial protein degradation; Mitochondrial translation elongation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y399](https://www.uniprot.org/uniprotkb/Q9Y399) (Small ribosomal subunit protein uS2m):

> Required for mitoribosome formation and stability, and mitochondrial translation.

**Summary**, from NCBI Gene [51116](https://www.ncbi.nlm.nih.gov/gene/51116):

> Mammalian mitochondrial ribosomal proteins are encoded by nuclear genes and help in protein synthesis within the mitochondrion. Mitochondrial ribosomes (mitoribosomes) consist of a small 28S subunit and a large 39S subunit. They have an estimated 75% protein to rRNA composition compared to prokaryotic ribosomes, where this ratio is reversed. Another difference between mammalian mitoribosomes and prokaryotic ribosomes is that the latter contain a 5S rRNA. Among different species, the proteins …

**Accessions** — [HGNC:14495](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14495) · Entrez [51116](https://www.ncbi.nlm.nih.gov/gene/51116) · UniProt [Q9Y399](https://www.uniprot.org/uniprotkb/Q9Y399) · Ensembl [ENSG00000122140](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000122140)

## Data

Gene col 4323: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4323); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4323, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4323]; `tensor/DDL_lfc|DDL_z.npy` [4323]; `embed/gene_vectors.npy` [4323]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4323 or target_col == 4323). Every well: [[MRPS2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MRPS2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
