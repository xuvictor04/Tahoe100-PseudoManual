---
symbol: "MRPS24"
type: "gene"
col: 712
ensembl_id: "ENSG00000062582"
name: "mitochondrial ribosomal protein S24"
location: "7p13"
module: 43
arm: "+"
pooled_cpm: 27.7
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 1
n_dd_up_clean: 0
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/043"]
generated_by: "tahoemap"
---

# MRPS24

*mitochondrial ribosomal protein S24* — 7p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 2.45× (z +6.1, q 5e-07, up in 41 of 44 measured lines) ⚠ toxic. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.635× (z -4.6, q 0.003, down in 28 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (SW480 0.285×, CHP-212 0.103×, NCI-H2347 0.353×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (HCT15 0.117×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 21 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TOMM7]] (+0.75, fdr 1e-05), [[SNHG19]] (+0.74, fdr 1e-05), [[RPL17]] (+0.73, fdr 7e-06); moves opposite to [[NUP188]] (-0.61, fdr 5e-05), [[NCBP1]] (-0.60, fdr 5e-05).
> It sits in the **+** arm of [[Module 043]] (Eukaryotic Translation Elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 6 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 712.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.45×** | +6.1 | 5e-07 | 41/44 (NCI-H2030, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **2.78×** | +5.9 | 8e-07 | 38/43 (C-33 A, NCI-H460, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **2.28×** | +5.6 | 3e-06 | 28/34 (MIA PaCa-2, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~29% of this change | **2.02×** | +5.0 | 9e-05 | 37/46 (J82, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **1.82×** | +4.0 | 0.009 | 28/38 (KATO III, J82, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | 1.59× | +3.2 | 0.14 | 27/46 (A-172, NCI-H1792, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 712.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (SW480 0.285×, CHP-212 0.103×, NCI-H2347 0.353×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (HCT15 0.117×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.635×** | -4.6 | 0.003 | 28/47 (SW480, CHP-212, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Lucanthone (drug)]] 0.05 µM |  | 0.633× | -3.0 | 0.76 | 26/48 (A-427, SW480, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, +0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 712. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CHP-212 (line)]] | wt | 24.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.103× (z -9.9) |
| [[HCT15 (line)]] | alt | 20.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.117× (z -9.0) |
| [[NCI-H2347 (line)]] | alt | 31.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.353× (z -8.9) |
| [[SW480 (line)]] | alt | 32.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -10.9) |
| [[A-172 (line)]] | wt | 24.1 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 28.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 57.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 24.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 47.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 34.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 28.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 22.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 23.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.24 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 46.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 25.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 25.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 35.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 712), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 21 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TOMM7]] | +0.75 | +0.55 / +0.81 | both halves | 1e-05 | STRING 454 |
| [[SNHG19]] | +0.74 | +0.55 / +0.76 | both halves | 1e-05 |  |
| [[RPL17]] | +0.73 | +0.61 / +0.75 | both halves | 7e-06 |  |
| [[COX7C]] | +0.73 | +0.60 / +0.79 | both halves | 7e-06 |  |
| [[UQCRB]] ⚠ | +0.72 | +0.58 / +0.76 | both halves | 8e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[RPS27]] | +0.72 | +0.60 / +0.74 | both halves | 7e-06 |  |
| [[ATP5MC2]] | +0.72 | +0.52 / +0.76 | both halves | 1e-05 |  |
| [[RPS19]] | +0.71 | +0.58 / +0.74 | both halves | 8e-06 |  |
| [[ATP5MJ]] | +0.71 | +0.52 / +0.81 | both halves | 1e-05 |  |
| [[RPS14]] | +0.70 | +0.55 / +0.74 | both halves | 1e-05 | STRING 441 |
| [[RPL23]] | +0.70 | +0.55 / +0.73 | both halves | 1e-05 |  |
| [[RPL34]] | +0.70 | +0.59 / +0.70 | both halves | 7e-06 |  |
| [[RPL35A]] | +0.70 | +0.55 / +0.72 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUP188]] | -0.61 | -0.39 / -0.64 | both halves | 5e-05 |  |
| [[NCBP1]] | -0.60 | -0.40 / -0.66 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 043]] — Eukaryotic Translation Elongation; 103 genes; this gene is in the **+** arm (projection on the module's main direction 0.702). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-43.5, -25.9); signed map (-57.9, -3.9). **Vector** length 66.2, 19.8% of its response variance represented; |z| ≥ 3 in 450 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Eukaryotic Translation Elongation* (reactome, mean cos +0.58 to 55); *Peptide chain elongation* (reactome, mean cos +0.60 to 52); *Formation of a pool of free 40S subunits* (reactome, mean cos +0.59 to 53).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +3.5 | +1.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.8 | +6.1 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.4 | +0.8 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.3 | +0.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.7 | +2.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.7 | +1.1 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.6 | +2.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +1.5 | +0.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.4 | +0.1 |
| fall | [[Auranofin (drug)]] 5 µM |  | -4.3 | -0.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | -3.6 | +5.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.4 | -0.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | -3.2 | +5.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | -3.1 | +4.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.9 | -1.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.7 | -0.8 |
|  | [[Diphenhydramine (drug)]] 0.5 µM |  | -1.3 | -0.8 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -1.2 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial ribosomal protein S24 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p13 — chr7:43,866,558-43,869,893 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MRP-S24, HSPC335 |
| Gene groups (HGNC) | Mitochondrial ribosomal proteins; Small subunit mitochondrial ribosomal proteins |
| Reactome | 6 pathways, smallest: Mitochondrial ribosome-associated quality control; Mitochondrial translation elongation; Mitochondrial translation initiation |
| Matched by | ensembl_id |

UniProt [Q96EL2](https://www.uniprot.org/uniprotkb/Q96EL2) carries no function annotation.

**Summary**, from NCBI Gene [64951](https://www.ncbi.nlm.nih.gov/gene/64951):

> Mammalian mitochondrial ribosomal proteins are encoded by nuclear genes and help in protein synthesis within the mitochondrion. Mitochondrial ribosomes (mitoribosomes) consist of a small 28S subunit and a large 39S subunit. They have an estimated 75% protein to rRNA composition compared to prokaryotic ribosomes, where this ratio is reversed. Another difference between mammalian mitoribosomes and prokaryotic ribosomes is that the latter contain a 5S rRNA. Among different species, the proteins …

**Accessions** — [HGNC:14510](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14510) · Entrez [64951](https://www.ncbi.nlm.nih.gov/gene/64951) · UniProt [Q96EL2](https://www.uniprot.org/uniprotkb/Q96EL2) · Ensembl [ENSG00000062582](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000062582)

## Data

Gene col 712: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 712); `tables/drug_effects.parquet` (8 rows, flagged included); `relations/gene_relations.parquet` (col_a == 712, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 712]; `tensor/DDL_lfc|DDL_z.npy` [712]; `embed/gene_vectors.npy` [712]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 712 or target_col == 712). Every well: [[MRPS24 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MRPS24.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
