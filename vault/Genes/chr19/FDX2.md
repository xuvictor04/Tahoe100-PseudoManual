---
symbol: "FDX2"
type: "gene"
col: 15567
ensembl_id: "ENSG00000267673"
name: "ferredoxin 2"
location: "19p13.2"
module: 11
arm: "+"
pooled_cpm: 2.38
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 0
n_dd_up_clean: 4
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# FDX2

*ferredoxin 2* — 19p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.44× (z +6.7, q 1e-08, up in 23 of 32 measured lines) ⚠ cell-cycle shift, explains ~49% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.19× (z +5.9, q 7e-07, up in 17 of 29 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Clofarabine (drug)]] 0.5 µM in 1 line (HEC-1-A 0.0602×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPP25L]] (+0.74, fdr 7e-06), [[SCAND1]] (+0.74, fdr 1e-05), [[ERVK3-1]] (+0.71, fdr 7e-06); moves opposite to [[TXNDC5]] (-0.70, fdr 7e-06), [[RPSA]] (-0.64, fdr 1e-05), [[FKBP9]] (-0.64, fdr 1e-05).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SLC2A6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 7 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15567.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **2.44×** | +6.7 | 1e-08 | 23/32 (A-172, A549, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **3.26×** | +6.0 | 4e-07 | 1/3 (A498) | rises with dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.19×** | +5.9 | 7e-07 | 17/29 (LS 180, A498, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **3.04×** | +5.7 | 2e-06 | 11/14 (A498, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.67×** | +5.2 | 2e-05 | 29/42 (A-172, PANC-1, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **2.73×** | +5.1 | 3e-05 | 25/39 (PANC-1, LoVo, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | **2.41×** | +4.7 | 2e-04 | 8/13 (SW480, NCI-H2347, …) | rises with dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~37% of this change | **2.39×** | +4.6 | 3e-04 | 5/9 (A-427, SW480, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.23×** | +4.3 | 0.001 | 12/28 (A-172, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **2.13×** | +4.0 | 0.003 | 9/22 (HEC-1-A, SW480, …) | top dose only | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.52×** | +3.1 | 0.087 | 12/44 (RKO, NCI-H1573, …) | top dose only |  |
| [[Amsacrine (drug)]] 5 µM |  | 1.50× | +3.0 | 0.12 | 9/41 (Panc 03.27, HEC-1-A, …) | top dose only |  |
| [[Bendamustine (drug)]] 5 µM |  | 1.80× | +3.0 | 0.12 | 11/30 (SNU-423, HS-578T, …) | top dose only |  |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Clofarabine (drug)]] 0.5 µM in 1 line (HEC-1-A 0.0602×).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.35 per unit of S-phase module lfc, +0.56 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15567. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 3.04 | 0 | 1 | — | [[Clofarabine (drug)]] 0.5 µM 0.0602× (z -9.0) |
| [[A-172 (line)]] | wt | 4.34 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.27 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.07 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.36 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.29 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.813 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.38 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.04 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.879 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.72 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.67 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.48 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.77 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.02 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.39 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.06 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.65 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.71 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.06 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.49 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.72 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.66 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.49 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.36 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.862 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.82 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.59 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15567), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPP25L]] | +0.74 | +0.64 / +0.81 | both halves | 7e-06 |  |
| [[SCAND1]] | +0.74 | +0.55 / +0.77 | both halves | 1e-05 |  |
| [[ERVK3-1]] | +0.71 | +0.62 / +0.77 | both halves | 7e-06 |  |
| [[ZNF593]] | +0.71 | +0.53 / +0.79 | both halves | 1e-05 |  |
| [[PPCS]] | +0.70 | +0.56 / +0.77 | both halves | 1e-05 |  |
| [[ZCCHC10]] | +0.70 | +0.59 / +0.70 | both halves | 7e-06 |  |
| [[OR7E38P]] | +0.69 | +0.53 / +0.76 | both halves | 1e-05 |  |
| [[TOPORS]] | +0.68 | +0.63 / +0.67 | both halves | 7e-06 |  |
| [[LINC02307]] | +0.68 | +0.73 / +0.66 | both halves | 7e-06 |  |
| [[MRPL32]] | +0.68 | +0.47 / +0.74 | both halves | 2e-05 |  |
| [[PBDC1]] | +0.68 | +0.67 / +0.72 | both halves | 7e-06 |  |
| [[MRPL46]] | +0.68 | +0.56 / +0.72 | both halves | 1e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TXNDC5]] | -0.70 | -0.62 / -0.76 | both halves | 7e-06 |  |
| [[RPSA]] | -0.64 | -0.52 / -0.66 | both halves | 1e-05 |  |
| [[FKBP9]] | -0.64 | -0.51 / -0.72 | both halves | 1e-05 |  |
| [[ARHGAP4]] | -0.64 | -0.50 / -0.57 | both halves | 1e-05 |  |
| [[TMED7]] | -0.63 | -0.57 / -0.63 | both halves | 8e-06 |  |
| [[ARF3]] | -0.63 | -0.54 / -0.63 | both halves | 1e-05 |  |
| [[AGO1]] | -0.63 | -0.50 / -0.62 | both halves | 1e-05 |  |
| [[COLGALT1]] | -0.61 | -0.61 / -0.53 | both halves | 1e-05 |  |
| [[CALU]] | -0.61 | -0.63 / -0.56 | both halves | 1e-05 |  |
| [[SEPTIN7P14]] | -0.61 | -0.45 / -0.61 | both halves | 3e-05 |  |
| [[BPNT2]] | -0.61 | -0.53 / -0.65 | both halves | 1e-05 | pathway: Biological oxidations |
| [[PRPF8]] | -0.60 | -0.46 / -0.64 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC2A6]] | B | SLC2A6 activity raises FDX2's level | lines that do not express SLC2A6 (6) vs lines expressing it (44) | 1.41× lower at baseline in the lines without SLC2A6 | 0.073 | ⚠ within organs, on part of the lines; also absent: GFOD1, SOAT1, RGS9; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.686). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-42.5, -11.5); signed map (-2.7, -8.6). **Vector** length 48.5, 7.63% of its response variance represented; |z| ≥ 3 in 729 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +4.0 | +5.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | +3.5 | +6.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +2.8 | +5.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.7 | +5.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.4 | +4.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.0 | +2.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | +3.1 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.4 | +3.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.3 | +1.8 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.0 | +1.4 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -1.7 | +2.0 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.3 | -0.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.2 | -1.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.2 | +1.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.1 | -2.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.0 | -1.9 |
|  | [[Diphenhydramine (drug)]] 0.05 µM |  | -1.0 | -1.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -0.9 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | ferredoxin 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.2 — chr19:10,309,916-10,316,015 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC19604; previously FDX1L |
| Gene groups (HGNC) | Mitochondrial respiratory chain complex assembly factors; Ferredoxin family |
| Reactome | 13 pathways, smallest: Defective CYP11A1 causes AICSR; Electron transport from NADPH to Ferredoxin; Pregnenolone biosynthesis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6P4F2](https://www.uniprot.org/uniprotkb/Q6P4F2) (Ferredoxin-2, mitochondrial):

> Electron donor, of the core iron-sulfur cluster (ISC) assembly complex, that acts to reduce the persulfide into sulfide during [2Fe-2S] clusters assembly on the scaffolding protein ISCU. The core iron-sulfur cluster (ISC) assembly complex is involved in the de novo synthesis of a [2Fe-2S] cluster, the first step of the mitochondrial iron-sulfur protein biogenesis (By similarity). This process is initiated by the cysteine desulfurase complex (NFS1:LYRM4:NDUFAB1) that produces persulfide which is …

**Summary**, from NCBI Gene [112812](https://www.ncbi.nlm.nih.gov/gene/112812):

> This gene encodes a member of the ferredoxin family. The encoded protein contains a 2Fe-2S ferredoxin-type domain and is essential for heme A and Fe/S protein biosynthesis. Mutation in FDX1L gene is associated with mitochondrial muscle myopathy. [provided by RefSeq, Sep 2014]

**Accessions** — [HGNC:30546](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30546) · Entrez [112812](https://www.ncbi.nlm.nih.gov/gene/112812) · UniProt [Q6P4F2](https://www.uniprot.org/uniprotkb/Q6P4F2) · Ensembl [ENSG00000267673](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000267673)

## Data

Gene col 15567: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15567); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15567, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15567]; `tensor/DDL_lfc|DDL_z.npy` [15567]; `embed/gene_vectors.npy` [15567]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15567 or target_col == 15567). Every well: [[FDX2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FDX2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
