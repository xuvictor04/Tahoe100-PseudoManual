---
symbol: "INAFM1"
type: "gene"
col: 15058
ensembl_id: "ENSG00000257704"
name: "InaF motif containing 1"
location: "19q13.32"
module: 20
arm: "-"
pooled_cpm: 7.83
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 3
n_dd_up_clean: 1
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# INAFM1

*InaF motif containing 1* — 19q13.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.32× (z +5.4, q 5e-05, up in 5 of 15 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 1.97× (z +4.5, q 0.002, up in 32 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[PH-797804 (drug)]] 5 µM: 0.246× (z -4.9, q 6e-04, down in 31 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM258]] (+0.75, fdr 7e-06), [[GGNBP2]] (+0.75, fdr 7e-06), [[PMM1]] (+0.75, fdr 7e-06); moves opposite to [[IPO5]] (-0.73, fdr 7e-06), [[RPSA]] (-0.72, fdr 7e-06), [[TMX3]] (-0.72, fdr 7e-06).
> It sits in the **-** arm of [[Module 020]] (Cap-dependent Translation Initiation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 6 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15058.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **2.32×** | +5.4 | 5e-05 | 5/15 (SW480, hTERT-HPNE, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.97×** | +4.5 | 0.002 | 32/47 (A549, NCI-H2030, …) | two highest doses | cell-cycle shift (explains ~21% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~87% of this change | **1.56×** | +4.1 | 0.007 | 20/44 (NCI-H460, A-172, …) | top dose only | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **1.76×** | +3.8 | 0.025 | 21/43 (SW480, HEC-1-A, …) | top dose only | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~49% of this change | **1.71×** | +3.5 | 0.046 | 21/43 (Hs 766T, A-427, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | 1.61× | +3.1 | 0.17 | 16/47 (A549, SW480, …) | two highest doses | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.63× | +3.1 | 0.17 | 16/38 (NCI-H460, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15058.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **0.246×** | -4.9 | 6e-04 | 31/42 (SW480, HT-29, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.258×** | -4.7 | 7e-04 | 30/45 (SNU-423, A-172, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.510×** | -4.2 | 0.004 | 22/46 (RPMI-7951, HS-578T, …) | inconsistent across doses |  |
| [[Fenofibrate (drug)]] 0.05 µM |  | 0.587× | -3.3 | 0.14 | 15/46 (CHP-212, SW 900, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.626× | -3.1 | 0.20 | 14/47 (HT-29, SW480, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, +0.49 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15058. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 23.6 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.0497× (z -11.0) ⚠ cell-cycle shift, would explain all of this change |
| [[LoVo (line)]] | wt | 4.88 | 0 | 1 | — | [[Belumosudil (drug)]] 5 µM 0.0883× (z -8.7) |
| [[RPMI-7951 (line)]] | alt | 9.85 | 0 | 1 | — | [[TAK-901 (drug)]] 0.05 µM 0.0361× (z -11.9) |
| [[A-172 (line)]] | wt | 7.00 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.82 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.95 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.81 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.22 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.96 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.22 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.31 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.36 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.19 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.42 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.80 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.74 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.22 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.21 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.97 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.17 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.35 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.97 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.24 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.67 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.60 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.61 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.81 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.29 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.50 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.20 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.48 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.78 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.97 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.98 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.83 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.45 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 8.47 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15058), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*53 of its nearest partners move with it, 5 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM258]] | +0.75 | +0.60 / +0.81 | both halves | 7e-06 |  |
| [[GGNBP2]] | +0.75 | +0.70 / +0.75 | both halves | 7e-06 |  |
| [[PMM1]] | +0.75 | +0.59 / +0.79 | both halves | 7e-06 |  |
| [[KRT10]] ⚠ | +0.75 | +0.71 / +0.72 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[ING2]] | +0.73 | +0.61 / +0.77 | both halves | 7e-06 |  |
| [[ZFAND2B]] | +0.72 | +0.63 / +0.76 | both halves | 7e-06 |  |
| [[NKAP]] | +0.72 | +0.61 / +0.78 | both halves | 7e-06 |  |
| [[EIF1B]] | +0.72 | +0.65 / +0.79 | both halves | 7e-06 |  |
| [[CROCCP2-1]] | +0.71 | +0.71 / +0.71 | both halves | 7e-06 |  |
| [[SNHG9]] | +0.71 | +0.65 / +0.74 | both halves | 7e-06 |  |
| [[POLR2J4]] | +0.71 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[SMIM26]] ⚠ | +0.70 | +0.58 / +0.74 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[GOLGA2]] | +0.70 | +0.63 / +0.67 | both halves | 7e-06 |  |
| [[ARID3A]] | +0.70 | +0.51 / +0.71 | both halves | 1e-05 |  |

## Genes that move opposite

*47 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IPO5]] | -0.73 | -0.67 / -0.74 | both halves | 7e-06 |  |
| [[RPSA]] | -0.72 | -0.66 / -0.75 | both halves | 7e-06 |  |
| [[TMX3]] | -0.72 | -0.65 / -0.67 | both halves | 7e-06 |  |
| [[CCT7]] | -0.71 | -0.58 / -0.70 | both halves | 7e-06 |  |
| [[DARS2]] | -0.71 | -0.54 / -0.69 | both halves | 1e-05 |  |
| [[ARPP19]] | -0.70 | -0.60 / -0.70 | both halves | 7e-06 |  |
| [[TMEM33]] | -0.69 | -0.55 / -0.73 | both halves | 1e-05 |  |
| [[CCT5]] | -0.69 | -0.67 / -0.66 | both halves | 7e-06 |  |
| [[VMA21]] | -0.69 | -0.50 / -0.77 | both halves | 1e-05 |  |
| [[PTGFRN]] | -0.69 | -0.63 / -0.64 | both halves | 7e-06 |  |
| [[CAPRIN1]] | -0.68 | -0.57 / -0.71 | both halves | 9e-06 |  |
| [[RPE]] | -0.68 | -0.64 / -0.75 | both halves | 7e-06 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **-** arm (projection on the module's main direction -0.768). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-30.6, -28.8); signed map (-14.8, -0.1). **Vector** length 76.2, 18.6% of its response variance represented; |z| ≥ 3 in 541 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~87% of this change | +3.7 | +4.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | +2.3 | +3.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.1 | +4.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | +2.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | +1.8 | +3.1 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | +1.7 | +2.4 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | +1.6 | +2.1 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +1.6 | +2.1 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.6 | +1.9 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.6 | +0.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | -4.2 | +5.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.2 | -4.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | -3.9 | -4.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -3.6 | -2.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.7 | -4.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.5 | -1.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.9 | -1.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.7 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | InaF motif containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.32 — chr19:47,274,885-47,275,723 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously PRR24 |
| Matched by | ensembl_id |

UniProt [C9JVW0](https://www.uniprot.org/uniprotkb/C9JVW0) carries no function annotation.

**Summary**, from NCBI Gene [255783](https://www.ncbi.nlm.nih.gov/gene/255783):

> Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:27406](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27406) · Entrez [255783](https://www.ncbi.nlm.nih.gov/gene/255783) · UniProt [C9JVW0](https://www.uniprot.org/uniprotkb/C9JVW0) · Ensembl [ENSG00000257704](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000257704)

## Data

Gene col 15058: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15058); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15058, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15058]; `tensor/DDL_lfc|DDL_z.npy` [15058]; `embed/gene_vectors.npy` [15058]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15058 or target_col == 15058). Every well: [[INAFM1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/INAFM1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
