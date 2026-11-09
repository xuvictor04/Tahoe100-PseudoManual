---
symbol: "SDF2L1"
type: "gene"
col: 4864
ensembl_id: "ENSG00000128228"
name: "stromal cell derived factor 2 like 1"
location: "22q11.21"
module: 40
arm: "+"
pooled_cpm: 10.81
n_lines_expressing: 49
n_dd_up: 3
n_dd_down: 1
n_dd_up_clean: 0
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/040"]
generated_by: "tahoemap"
---

# SDF2L1

*stromal cell derived factor 2 like 1* — 22q11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 2.34× (z +4.5, q 0.003, up in 28 of 43 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.484× (z -5.4, q 3e-05, down in 29 of 42 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (NCI-H2030 0.109×, KATO III 0.198×, HS-578T 0.164×, LoVo 0.245×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A498 0.128×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MYDGF]] (+0.74, fdr 7e-06), [[HSPA5]] (+0.72, fdr 7e-06), [[ISOC2]] (+0.71, fdr 7e-06); moves opposite to [[ZNF655]] (-0.67, fdr 1e-05), [[ZXDB]] (-0.65, fdr 8e-06), [[EIF4G2]] (-0.62, fdr 2e-05).
> It sits in the **+** arm of [[Module 040]] (Asparagine N-linked glycosylation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 6 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4864.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **2.34×** | +4.5 | 0.003 | 28/43 (PANC-1, NCI-H1792, …) | top dose only | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~37% of this change | **2.12×** | +4.0 | 0.011 | 23/38 (HEC-1-A, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | **2.56×** | +4.0 | 0.011 | 15/30 (Hs 766T, Panc 03.27, …) | two highest doses | composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | 1.55× | +3.3 | 0.10 | 22/41 (Hs 766T, A549, …) | top dose only | position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | 1.86× | +3.3 | 0.10 | 22/41 (A-427, SW48, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~69% of this change | 1.78× | +3.1 | 0.18 | 20/46 (SW480, Panc 03.27, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~97% of this change | 1.81× | +3.1 | 0.18 | 5/16 (PANC-1, NCI-H460, …) | two highest doses | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4864.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (NCI-H2030 0.109×, KATO III 0.198×, HS-578T 0.164×, LoVo 0.245×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A498 0.128×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.484×** | -5.4 | 3e-05 | 29/42 (NCI-H2030, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.64 per unit of S-phase module lfc, +0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4864. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 16.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.128× (z -8.7) |
| [[HS-578T (line)]] | alt | 27.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.164× (z -10.1) |
| [[KATO III (line)]] | alt | 35.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -10.6) |
| [[LoVo (line)]] | wt | 13.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -8.6) |
| [[NCI-H2030 (line)]] | alt | 26.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.109× (z -13.9) |
| [[A-172 (line)]] | wt | 4.24 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 9.44 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.24 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.74 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.50 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.13 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.81 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.13 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.93 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.84 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.38 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.89 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.41 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.82 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.23 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.00 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.83 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.61 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.01 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.74 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.36 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 9.66 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.35 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.84 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 8.48 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.39 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.89 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.80 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.92 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.42 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.10 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4864), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYDGF]] | +0.74 | +0.74 / +0.73 | both halves | 7e-06 | STRING 637 |
| [[HSPA5]] | +0.72 | +0.76 / +0.61 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING; STRING 804 |
| [[ISOC2]] | +0.71 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[TMED9]] | +0.70 | +0.73 / +0.60 | both halves | 7e-06 |  |
| [[IER3IP1]] | +0.70 | +0.73 / +0.61 | both halves | 7e-06 |  |
| [[SSR2]] | +0.70 | +0.65 / +0.71 | both halves | 7e-06 |  |
| [[EEF1AKMT4]] | +0.70 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[TXNDC11]] | +0.70 | +0.67 / +0.68 | both halves | 7e-06 |  |
| [[SEC61B]] | +0.70 | +0.59 / +0.71 | both halves | 7e-06 |  |
| [[SLC37A3]] | +0.69 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[COG5]] | +0.69 | +0.69 / +0.50 | both halves | 1e-05 |  |
| [[MPG]] | +0.69 | +0.58 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF655]] | -0.67 | -0.51 / -0.62 | both halves | 1e-05 |  |
| [[ZXDB]] | -0.65 | -0.58 / -0.58 | both halves | 8e-06 |  |
| [[EIF4G2]] | -0.62 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[ZNF507]] | -0.62 | -0.59 / -0.46 | both halves | 3e-05 |  |
| [[TRMT13]] | -0.62 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[DDX6]] | -0.61 | -0.40 / -0.48 | both halves | 5e-05 |  |
| [[ZNF528]] | -0.61 | -0.55 / -0.39 | both halves | 5e-05 |  |
| [[DDX39B]] | -0.60 | -0.43 / -0.53 | both halves | 3e-05 |  |
| [[GMFB]] | -0.60 | -0.44 / -0.63 | both halves | 3e-05 |  |
| [[TASOR]] | -0.60 | -0.62 / -0.38 | both halves | 7e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 040]] — Asparagine N-linked glycosylation; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.745). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (15.6, -32.0); signed map (-46.8, 8.9). **Vector** length 79.7, 22.1% of its response variance represented; |z| ≥ 3 in 534 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.3 | +2.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.1 | +2.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~69% of this change | +2.9 | +3.1 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +2.8 | +3.3 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.5 | +1.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | +2.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.6 | +1.5 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | +1.5 | +1.8 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.5 | +2.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.3 | +0.3 |
| fall | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.2 | -2.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.9 | -2.3 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.9 | -1.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.8 | -5.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | -1.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.5 | -1.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.9 | -2.8 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -1.9 | -2.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.6 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | stromal cell derived factor 2 like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q11.21 — chr22:21,642,302-21,644,299 (+) |
| Ensembl biotype | protein_coding |
| Also known as | AP000553.C22.4, OTTHUMT00000075032 |
| Hallmark sets | MTORC1_SIGNALING |
| Matched by | ensembl_id |

UniProt [Q9HCN8](https://www.uniprot.org/uniprotkb/Q9HCN8) carries no function annotation.

**Summary**, from NCBI Gene [23753](https://www.ncbi.nlm.nih.gov/gene/23753):

> Enables misfolded protein binding activity. Involved in protein refolding. Located in endoplasmic reticulum. Part of protein folding chaperone complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:10676](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10676) · Entrez [23753](https://www.ncbi.nlm.nih.gov/gene/23753) · UniProt [Q9HCN8](https://www.uniprot.org/uniprotkb/Q9HCN8) · Ensembl [ENSG00000128228](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000128228)

## Data

Gene col 4864: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4864); `tables/drug_effects.parquet` (8 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4864, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4864]; `tensor/DDL_lfc|DDL_z.npy` [4864]; `embed/gene_vectors.npy` [4864]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4864 or target_col == 4864). Every well: [[SDF2L1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SDF2L1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
