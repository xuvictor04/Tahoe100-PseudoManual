---
symbol: "CNOT11"
type: "gene"
col: 8161
ensembl_id: "ENSG00000158435"
name: "CCR4-NOT transcription complex subunit 11"
location: "2q11.2"
module: 7
arm: "+"
pooled_cpm: 25.94
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 4
n_dd_up_clean: 0
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# CNOT11

*CCR4-NOT transcription complex subunit 11* — 2q11.2

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 2.54×; ⚠ cell-cycle shift, would explain all of this change).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.728× (z -6.8, q 7e-09, down in 23 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 8 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (NCI-H1573 0.306×, COLO 205 0.258×, C-33 A 0.211×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Digitoxin (drug)]] 5 µM in 2 lines (KATO III 0.0946×, NCI-H460 0.373×; ⚠ toxic; transcription drop); [[Torkinib (drug)]] 5 µM in 1 line (SW 900 0.0653×; ⚠ toxic).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PRKAB1]] (+0.58, fdr 1e-05), [[RNF25]] (+0.56, fdr 1e-05), [[CIAPIN1]] (+0.56, fdr 1e-05); moves opposite to [[CDKL2]] (-0.51, fdr 2e-05), [[MIR9-1HG]] (-0.49, fdr 4e-05), [[POLN]] (-0.47, fdr 3e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8161.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 2.54×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.16× | +3.1 | 0.60 | 12/34 (LS 180, LOX-IMVI, …) | top dose only | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8161.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 8 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (NCI-H1573 0.306×, COLO 205 0.258×, C-33 A 0.211×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Digitoxin (drug)]] 5 µM in 2 lines (KATO III 0.0946×, NCI-H460 0.373×; ⚠ toxic; transcription drop); [[Torkinib (drug)]] 5 µM in 1 line (SW 900 0.0653×; ⚠ toxic).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.728×** | -6.8 | 7e-09 | 23/48 (KATO III, COLO 205, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.757×** | -5.9 | 9e-07 | 19/47 (SW480, HT-29, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.759×** | -5.9 | 9e-07 | 25/47 (KATO III, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.932× | -5.3 | 2e-05 | 1/48 (NCI-H1792) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.804×** | -4.6 | 4e-04 | 19/48 (COLO 205, A498, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.877× | -3.9 | 0.008 | 12/48 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Bisoprolol (hemifumarate) (drug)]] 5 µM |  | 0.848× | -3.4 | 0.062 | 6/47 (RPMI-7951, HepG2/C3A, …) | top dose only | position effect removed |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.05 µM |  | 0.866× | -3.0 | 0.17 | 8/48 (LOX-IMVI, AN3 CA, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8161. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 92.1 | 0 | 5 (5 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.215× (z -10.6) ⚠ toxic; cell-cycle shift, explains ~48% of this change |
| [[A-427 (line)]] | wt | 24.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +10.8) ⚠ cell-cycle shift, would explain all of this change | — |
| [[C-33 A (line)]] | alt | 23.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.211× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 29.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.305× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 17.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0946× (z -16.3) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 33.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.306× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 24.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.373× (z -9.8) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 30.7 | 0 | 1 (1 ⚠) | — | [[Torkinib (drug)]] 5 µM 0.0653× (z -10.7) ⚠ toxic |
| [[A-172 (line)]] | wt | 25.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 38.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 26.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 23.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 32.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 28.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 26.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 25.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 33.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8161), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRKAB1]] | +0.58 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[RNF25]] | +0.56 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[CIAPIN1]] | +0.56 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[RRP36]] | +0.53 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[ALG5]] | +0.51 | +0.47 / +0.46 | both halves | 2e-05 |  |
| [[SCO1]] | +0.51 | +0.45 / +0.47 | both halves | 3e-05 |  |
| [[FAM118B]] | +0.50 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[PYM1]] | +0.49 | +0.44 / +0.49 | both halves | 3e-05 |  |
| [[VPS16]] | +0.48 | +0.51 / +0.40 | both halves | 5e-05 |  |
| [[TMEM128]] | +0.48 | +0.38 / +0.49 | both halves | 7e-05 |  |
| [[MMAA]] | +0.48 | +0.52 / +0.34 | both halves | 1e-04 |  |
| [[C5orf22]] | +0.47 | +0.44 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDKL2]] | -0.51 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[MIR9-1HG]] | -0.49 | -0.40 / -0.61 | both halves | 4e-05 |  |
| [[POLN]] | -0.47 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[LDHC]] | -0.47 | -0.41 / -0.58 | both halves | 4e-05 |  |
| [[BZW2]] | -0.46 | -0.40 / -0.52 | both halves | 4e-05 |  |
| [[C8orf88]] | -0.45 | -0.38 / -0.49 | both halves | 6e-05 |  |
| [[WHRN]] | -0.45 | -0.38 / -0.49 | both halves | 7e-05 |  |
| [[LRRC23]] | -0.45 | -0.40 / -0.53 | both halves | 5e-05 |  |
| [[NPAS1]] | -0.44 | -0.28 / -0.54 | both halves | 3e-04 |  |
| [[FAM222A]] | -0.44 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[GRAMD2A]] | -0.44 | -0.34 / -0.52 | both halves | 1e-04 |  |
| [[TENT5C]] | -0.43 | -0.38 / -0.51 | both halves | 7e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.388). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-47.7, 4.0); signed map (-8.6, -25.4). **Vector** length 65.5, 10.1% of its response variance represented; |z| ≥ 3 in 705 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.4 | +1.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.3 | +1.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.5 | +2.9 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +2.4 | +2.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +1.9 | +0.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.7 | -0.3 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +1.5 | +1.1 |
|  | [[Vortioxetine (drug)]] 0.5 µM |  | +1.4 | +2.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +1.4 | +2.3 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -2.6 | -3.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.4 | -5.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | -1.9 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.8 | -2.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.8 | -1.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.5 | -1.6 |
|  | [[Artemether (drug)]] 0.05 µM |  | -1.5 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | CCR4-NOT transcription complex subunit 11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q11.2 — chr2:101,252,886-101,270,316 (+) |
| Ensembl biotype | protein_coding |
| Also known as | C40; previously C2orf29 |
| Gene groups (HGNC) | CCR4-NOT transcription complex |
| Reactome | 8 pathways, smallest: TP53 regulates transcription of additional cell cycle genes whose exact role in the p53 pathway remain uncertain; Deadenylation of mRNA; M-decay: degradation of maternal mRNAs by maternally stored factors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UKZ1](https://www.uniprot.org/uniprotkb/Q9UKZ1) (CCR4-NOT transcription complex subunit 11):

> Component of the CCR4-NOT complex which is one of the major cellular mRNA deadenylases and is linked to various cellular processes including bulk mRNA degradation, miRNA-mediated repression, translational repression during translational initiation and general transcription regulation. Additional complex functions may be a consequence of its influence on mRNA expression. Is required for the association of CNOT10 with the CCR4-NOT complex. Does not seem to be required for complex deadenylase …

**Summary**, from NCBI Gene [55571](https://www.ncbi.nlm.nih.gov/gene/55571):

> Predicted to be involved in nuclear-transcribed mRNA poly(A) tail shortening. Part of CCR4-NOT complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25217](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25217) · Entrez [55571](https://www.ncbi.nlm.nih.gov/gene/55571) · UniProt [Q9UKZ1](https://www.uniprot.org/uniprotkb/Q9UKZ1) · Ensembl [ENSG00000158435](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000158435)

## Data

Gene col 8161: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8161); `tables/drug_effects.parquet` (9 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8161, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8161]; `tensor/DDL_lfc|DDL_z.npy` [8161]; `embed/gene_vectors.npy` [8161]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8161 or target_col == 8161). Every well: [[CNOT11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CNOT11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
