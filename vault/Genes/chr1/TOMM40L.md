---
symbol: "TOMM40L"
type: "gene"
col: 8204
ensembl_id: "ENSG00000158882"
name: "translocase of outer mitochondrial membrane 40 like"
location: "1q23.3"
module: 4
arm: "+"
pooled_cpm: 3.05
n_lines_expressing: 47
n_dd_up: 21
n_dd_down: 0
n_dd_up_clean: 10
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# TOMM40L

*translocase of outer mitochondrial membrane 40 like* — 1q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.44× (z +12.0, q 3e-30, up in 2 of 4 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 2.46× (z +9.1, q 3e-17, up in 28 of 41 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Erlotinib (drug)]] 5 µM in 1 line (A-427 0.0904×); [[Oxaprozin (drug)]] 0.05 µM in 1 line (RKO 0.0832×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ERCC8]] (+0.63, fdr 1e-05), [[C12orf43]] (+0.61, fdr 1e-05), [[DNAJC17]] (+0.61, fdr 1e-05); moves opposite to [[ACADSB]] (-0.56, fdr 3e-05), [[CCNI]] (-0.53, fdr 2e-05), [[YPEL1]] (-0.48, fdr 4e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 11 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8204.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.44×** | +12.0 | 3e-30 | 2/4 (CFPAC-1, NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.46×** | +9.1 | 3e-17 | 28/41 (C32, A-427, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **2.39×** | +8.8 | 3e-16 | 6/13 (SW 900, J82, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.16×** | +7.8 | 1e-12 | 25/41 (C32, SW480, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.93×** | +6.6 | 3e-09 | 13/31 (NCI-H1573, C32, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.93×** | +6.4 | 2e-08 | 6/13 (NCI-H2030, A-172, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.84×** | +5.8 | 5e-07 | 17/36 (C32, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **1.79×** | +5.4 | 4e-06 | 1/5 (CFPAC-1) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.38×** | +4.6 | 2e-04 | 5/42 (A-427, A-172, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.38×** | +4.6 | 2e-04 | 10/43 (NCI-H2030, NCI-H2347, …) | top dose only | position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.51×** | +3.8 | 0.006 | 9/28 (J82, NCI-H2347, …) | inconsistent across doses | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.31×** | +3.8 | 0.007 | 6/34 (C32, NCI-H1573, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.45×** | +3.8 | 0.007 | 6/42 (NCI-H1573, NCI-H1792, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.44×** | +3.7 | 0.009 | 2/16 (NCI-H2347, NCI-H460) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.42×** | +3.5 | 0.016 | 6/37 (NCI-H2030, NCI-H460, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.39×** | +3.3 | 0.034 | 2/36 (NCI-H460, A-172) | inconsistent across doses |  |
| [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM |  | **1.34×** | +3.0 | 0.082 | 1/32 (HS-578T) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8204.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Erlotinib (drug)]] 5 µM in 1 line (A-427 0.0904×); [[Oxaprozin (drug)]] 0.05 µM in 1 line (RKO 0.0832×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | 0.783× | -3.5 | 0.15 | 9/43 (SHP-77, LOX-IMVI, …) | rises with dose | position effect removed |
| [[Bergenin (drug)]] 5 µM |  | 0.788× | -3.4 | 0.15 | 7/43 (HCT15, H4, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 0.718× | -3.4 | 0.15 | 5/44 (PANC-1, SW48, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 0.5 µM |  | 0.737× | -3.1 | 0.23 | 4/42 (A-172, H4, …) | rises with dose | position effect removed |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 0.738× | -3.1 | 0.23 | 7/41 (HS-578T, NCI-H23, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.43 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8204. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 3.75 | 0 | 1 | — | [[Erlotinib (drug)]] 5 µM 0.0904× (z -8.7) |
| [[RKO (line)]] | wt | 4.80 | 0 | 1 | — | [[Oxaprozin (drug)]] 0.05 µM 0.0832× (z -8.5) |
| [[A-172 (line)]] | wt | 3.96 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.60 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.71 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.493 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.310 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.55 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.51 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.53 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.41 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.95 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.781 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.45 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.42 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.38 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.16 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.35 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.43 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.47 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.25 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.258 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.75 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.56 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8204), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ERCC8]] | +0.63 | +0.66 / +0.53 | both halves | 1e-05 |  |
| [[C12orf43]] | +0.61 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[DNAJC17]] | +0.61 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[PSMB2]] | +0.60 | +0.61 / +0.45 | both halves | 3e-05 |  |
| [[INVS]] | +0.59 | +0.62 / +0.51 | both halves | 1e-05 |  |
| [[POP1]] | +0.58 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[POP4]] | +0.57 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[LARS2]] | +0.56 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[TM2D2]] | +0.56 | +0.64 / +0.48 | both halves | 2e-05 |  |
| [[PSMD6]] | +0.56 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[IGHMBP2]] | +0.55 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[ZNF513]] | +0.54 | +0.50 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACADSB]] | -0.56 | -0.44 / -0.55 | both halves | 3e-05 |  |
| [[CCNI]] | -0.53 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[YPEL1]] | -0.48 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[TTC3]] | -0.47 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[PABPC1]] | -0.46 | -0.40 / -0.51 | both halves | 5e-05 | same gene group |
| [[SEPTIN2]] | -0.46 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[ARL5B]] | -0.46 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[DESI2]] | -0.46 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[RPS2]] | -0.46 | -0.42 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.405). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-42.7, 9.8); signed map (-18.1, -22.3). **Vector** length 42.6, 4.88% of its response variance represented; |z| ≥ 3 in 847 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +3.9 | +9.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.9 | +7.8 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +3.3 | +5.8 |
|  | [[Selinexor (drug)]] 5 µM |  | +2.1 | +4.6 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +1.9 | +6.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | +4.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.3 | +3.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.3 | +0.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.1 | +2.4 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | -0.6 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | -1.4 | -3.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.4 | -3.1 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.3 | -3.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.3 | -2.9 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.1 | -2.0 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.1 | +0.1 |

## What is on record

|  |  |
|---|---|
| Name | translocase of outer mitochondrial membrane 40 like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q23.3 — chr1:161,225,939-161,230,746 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ12770, TOMM40B |
| Gene groups (HGNC) | MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q969M1](https://www.uniprot.org/uniprotkb/Q969M1) (Mitochondrial import receptor subunit TOM40B):

> Potential channel-forming protein implicated in import of protein precursors into mitochondria.

**Summary**, from NCBI Gene [84134](https://www.ncbi.nlm.nih.gov/gene/84134):

> Predicted to enable transmembrane protein transporter activity. Predicted to be involved in protein import into mitochondrial matrix. Located in mitochondrion. Part of protein-containing complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25756](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25756) · Entrez [84134](https://www.ncbi.nlm.nih.gov/gene/84134) · UniProt [Q969M1](https://www.uniprot.org/uniprotkb/Q969M1) · Ensembl [ENSG00000158882](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000158882)

## Data

Gene col 8204: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8204); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8204, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8204]; `tensor/DDL_lfc|DDL_z.npy` [8204]; `embed/gene_vectors.npy` [8204]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8204 or target_col == 8204). Every well: [[TOMM40L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TOMM40L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
