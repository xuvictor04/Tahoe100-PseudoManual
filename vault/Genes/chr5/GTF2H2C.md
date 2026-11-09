---
symbol: "GTF2H2C"
type: "gene"
col: 11405
ensembl_id: "ENSG00000183474"
name: "GTF2H2 family member C"
location: "5q13.2"
module: 17
arm: "+"
pooled_cpm: 4.81
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 2
n_dd_up_clean: 11
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# GTF2H2C

*GTF2H2 family member C* — 5q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.16× (z +10.0, q 1e-20, up in 32 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.761× (z -5.0, q 2e-04, down in 14 of 42 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GTF2H2]] (+0.72, fdr 7e-06), [[FRA10AC1]] (+0.68, fdr 4e-05), [[GTF2H2B]] (+0.64, fdr 3e-05); moves opposite to [[SNHG31]] (-0.62, fdr 1e-04), [[RDH5]] (-0.54, fdr 2e-04), [[STARD4-AS1]] (-0.54, fdr 0.002, ⚠ one half only (not replicated)), [[CCNT2-AS1]] (-0.51, fdr 6e-04).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11405.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.16×** | +10.0 | 1e-20 | 32/47 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **2.10×** | +9.6 | 2e-19 | 34/47 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.76×** | +7.3 | 4e-11 | 21/47 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.71×** | +6.7 | 3e-09 | 2/6 (CFPAC-1, NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.39×** | +6.0 | 2e-07 | 17/41 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.78×** | +5.8 | 5e-07 | 12/39 (PANC-1, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.43×** | +4.3 | 0.001 | 4/13 (LOX-IMVI, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift; position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.10× | +4.3 | 0.001 | 6/48 (NCI-H460, NCI-H1573, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.37×** | +3.9 | 0.005 | 9/29 (NCI-H1573, HT-29, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.35×** | +3.9 | 0.005 | 7/46 (HOP62, SK-MEL-2, …) | top dose only |  |
| [[NG25 (drug)]] 0.05 µM |  | **1.37×** | +3.8 | 0.007 | 8/44 (SHP-77, PANC-1, …) | inconsistent across doses | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.34×** | +3.7 | 0.008 | 4/47 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | **1.22×** | +3.6 | 0.015 | 11/47 (NCI-H2347, A-427, …) | rises with dose | low cells (technical?); position effect removed |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.42×** | +3.6 | 0.015 | 3/41 (MIA PaCa-2, A498, …) | two highest doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[Selinexor (drug)]] 0.5 µM |  | **1.38×** | +3.2 | 0.046 | 1/43 (SW480) | rises with dose | cell-cycle shift (explains ~1% here); noisy plate (z scaled); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.28×** | +3.2 | 0.046 | 8/40 (NCI-H2030, C-33 A, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.18× | +3.0 | 0.083 | 7/48 (NCI-H2347, A498, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11405.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.761×** | -5.0 | 2e-04 | 14/42 (NCI-H1573, Hs 766T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.681×** | -5.0 | 2e-04 | 12/46 (SW 900, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Erlotinib (drug)]] 5 µM |  | 0.785× | -3.0 | 0.50 | 6/43 (SNU-423, NCI-H23, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11405. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 3.74 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 7.93 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.11 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.20 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.58 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.29 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.96 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.07 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.50 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.80 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.30 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.11 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.21 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.23 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.98 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.01 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.87 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.88 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.68 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.73 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.82 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.64 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.78 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.36 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.96 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.26 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.29 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.17 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.06 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.01 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.58 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.57 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.71 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.05 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.64 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.05 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.04 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.20 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.75 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.30 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.97 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11405), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GTF2H2]] | +0.72 | +0.69 / +0.66 | both halves | 7e-06 | STRING 986 |
| [[FRA10AC1]] | +0.68 | +0.74 / +0.43 | both halves | 4e-05 |  |
| [[GTF2H2B]] | +0.64 | +0.46 / +0.64 | both halves | 3e-05 |  |
| [[TAMM41]] | +0.62 | +0.44 / +0.45 | both halves | 3e-05 |  |
| [[RAD17]] | +0.62 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[COMMD2]] | +0.62 | +0.37 / +0.57 | both halves | 7e-05 |  |
| [[UBXN2B]] | +0.60 | +0.43 / +0.59 | both halves | 3e-05 |  |
| [[ZNHIT6]] | +0.59 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[ZNF74]] | +0.59 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[MSL3P1]] | +0.59 | +0.43 / +0.54 | both halves | 3e-05 |  |
| [[FAM114A2]] | +0.58 | +0.65 / +0.44 | both halves | 3e-05 |  |
| [[RIOK1]] | +0.58 | +0.48 / +0.54 | both halves | 2e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 4 of them with an alert (⚠; 4 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNHG31]] | -0.62 | -0.33 / -0.51 | both halves | 1e-04 |  |
| [[RDH5]] | -0.54 | -0.29 / -0.35 | both halves | 2e-04 |  |
| [[STARD4-AS1]] | -0.54 | -0.11 / -0.57 | ⚠ one half (not replicated) | 0.002 |  |
| [[CCNT2-AS1]] | -0.51 | -0.22 / -0.32 | both halves | 6e-04 |  |
| [[LYPLA2]] | -0.50 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[FBXL13]] | -0.50 | -0.19 / -0.49 | ⚠ not reproduced | 8e-04 |  |
| [[PIPOX]] | -0.49 | -0.13 / -0.50 | ⚠ one half (not replicated) | 0.002 |  |
| [[HCFC1]] | -0.49 | -0.50 / -0.33 | both halves | 1e-04 |  |
| [[XNDC1N-ZNF705EP-ALG1L9P]] | -0.48 | -0.14 / -0.46 | ⚠ not reproduced | 0.002 |  |
| [[SUMO3]] | -0.47 | -0.36 / -0.40 | both halves | 9e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.613). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-36.2, -9.4); signed map (-19.6, -12.2). **Vector** length 38.6, 3.67% of its response variance represented; |z| ≥ 3 in 874 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.6 | +2.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +1.4 | +3.9 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.2 | +2.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.2 | +1.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +1.1 | +10.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +0.9 | +2.3 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +0.8 | +2.6 |
|  | [[Neratinib (drug)]] 5 µM |  | +0.8 | +0.6 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.2 | -5.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | +1.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.2 | -1.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | +0.5 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.8 | -5.0 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -0.7 | -2.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -0.7 | -0.4 |
|  | [[Larotrectinib (drug)]] 0.05 µM |  | -0.7 | -1.1 |
|  | [[Palmatine (chloride) (drug)]] 0.05 µM |  | -0.7 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | GTF2H2 family member C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q13.2 — chr5:69,560,191-69,595,221 (+) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6P1K8](https://www.uniprot.org/uniprotkb/Q6P1K8) (General transcription factor IIH subunit 2-like protein):

> Component of the core-TFIIH basal transcription factor involved in nucleotide excision repair (NER) of DNA and, when complexed to CAK, in RNA transcription by RNA polymerase II.

**Summary**, from NCBI Gene [728340](https://www.ncbi.nlm.nih.gov/gene/728340):

> Enables RNA polymerase II general transcription initiation factor activity. Involved in G protein-coupled receptor internalization and transcription initiation at RNA polymerase II promoter. Located in nuclear speck. Part of core TFIIH complex portion of holo TFIIH complex and transcription factor TFIID complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:31394](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:31394) · Entrez [728340](https://www.ncbi.nlm.nih.gov/gene/728340) · UniProt [Q6P1K8](https://www.uniprot.org/uniprotkb/Q6P1K8) · Ensembl [ENSG00000183474](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183474)

## Data

Gene col 11405: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11405); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11405, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11405]; `tensor/DDL_lfc|DDL_z.npy` [11405]; `embed/gene_vectors.npy` [11405]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11405 or target_col == 11405). Every well: [[GTF2H2C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GTF2H2C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
