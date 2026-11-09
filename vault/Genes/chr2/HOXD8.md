---
symbol: "HOXD8"
type: "gene"
col: 10659
ensembl_id: "ENSG00000175879"
name: "homeobox D8"
location: "2q31.1"
module: 9
arm: "+"
pooled_cpm: 2.49
n_lines_expressing: 30
n_dd_up: 3
n_dd_down: 4
n_dd_up_clean: 1
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 2
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# HOXD8

*homeobox D8* — 2q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.16× (z +7.0, q 1e-09, up in 1 of 1 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.10× (z +6.7, q 6e-09, up in 12 of 17 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.274× (z -8.2, q 1e-13, down in 21 of 26 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM133A]] (+0.57, fdr 3e-05), [[RUNX1T1]] (+0.56, fdr 3e-05), [[ASCL1]] (+0.54, fdr 5e-05); moves opposite to [[POLD1]] (-0.44, fdr 1e-04), [[SPTLC1]] (-0.44, fdr 1e-04), [[TSPAN3]] (-0.44, fdr 2e-04).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 2 go from it, the strongest it → [[LRRIQ3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10659.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.16×** | +7.0 | 1e-09 | 1/1 (A498) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.10×** | +6.7 | 6e-09 | 12/17 (A498, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.96×** | +4.3 | 0.003 | 6/8 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | 1.69× | +3.3 | 0.12 | 4/25 (NCI-H460, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | 1.66× | +3.2 | 0.14 | 6/22 (SW480, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~1% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10659.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.274×** | -8.2 | 1e-13 | 21/26 (J82, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.450×** | -5.0 | 1e-04 | 14/24 (A-427, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.494×** | -4.5 | 0.002 | 15/22 (LOX-IMVI, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.581×** | -3.4 | 0.086 | 10/16 (SHP-77, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10659. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 14.7 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0531× (z -12.6) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.134× (z -8.6) |
| [[A-427 (line)]] | wt | 13.5 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.134× (z -9.7) |
| [[A498 (line)]] | wt | 7.03 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0788× (z -11.1) ⚠ toxic |
| [[J82 (line)]] | alt | 3.89 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0309× (z -11.7) |
| [[LoVo (line)]] | wt | 5.31 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0934× (z -9.6) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 6.69 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0516× (z -11.2) |
| [[NCI-H1573 (line)]] | alt | 2.09 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0890× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 1.64 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0686× (z -8.5) |
| [[A-172 (line)]] | wt | 6.00 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.48 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.414 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.233 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.732 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.41 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.17 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.190 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.246 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.583 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 4.68 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.212 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.170 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.190 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.349 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.256 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.171 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.184 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.157 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.162 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.502 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.169 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.09 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.83 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.153 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.177 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.92 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.264 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.783 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.44 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.524 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 4.30 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10659), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM133A]] | +0.57 | +0.46 / +0.50 | both halves | 3e-05 |  |
| [[RUNX1T1]] | +0.56 | +0.59 / +0.45 | both halves | 3e-05 |  |
| [[ASCL1]] | +0.54 | +0.50 / +0.40 | both halves | 5e-05 |  |
| [[ARHGAP25]] | +0.54 | +0.59 / +0.45 | both halves | 3e-05 |  |
| [[MIR2052HG]] | +0.53 | +0.57 / +0.36 | both halves | 9e-05 |  |
| [[SYT4]] | +0.52 | +0.50 / +0.36 | both halves | 9e-05 |  |
| [[GRIK1]] | +0.52 | +0.49 / +0.37 | both halves | 8e-05 |  |
| [[NRXN1]] | +0.52 | +0.39 / +0.53 | both halves | 5e-05 |  |
| [[LINC01414]] | +0.51 | +0.39 / +0.55 | both halves | 6e-05 |  |
| [[LRFN2]] | +0.51 | +0.49 / +0.35 | both halves | 1e-04 |  |
| [[SRRM4]] | +0.51 | +0.52 / +0.35 | both halves | 1e-04 |  |
| [[CRB1]] | +0.51 | +0.52 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLD1]] | -0.44 | -0.36 / -0.43 | both halves | 1e-04 |  |
| [[SPTLC1]] | -0.44 | -0.35 / -0.52 | both halves | 1e-04 |  |
| [[TSPAN3]] | -0.44 | -0.40 / -0.30 | both halves | 2e-04 |  |
| [[IL18BP]] | -0.43 | -0.29 / -0.43 | both halves | 3e-04 |  |
| [[UBE2G2]] | -0.43 | -0.26 / -0.49 | both halves | 4e-04 |  |
| [[CDK2]] | -0.43 | -0.37 / -0.45 | both halves | 7e-05 |  |
| [[CYB5B]] | -0.41 | -0.35 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LRRIQ3]] | B | HOXD8 activity raises LRRIQ3's level | lines that do not express HOXD8 (20) vs lines expressing it (30) | 1.59× lower at baseline in the lines without HOXD8 | 0.070 | ⚠ within organs, on part of the lines; also absent: SHANK1, LHX2, COL4A3 |
| [[LINC02899]] | C | HOXD8 activity raises LINC02899's level | lines that do not express HOXD8 (20) vs lines expressing it (30) | 3.26× lower at baseline in the lines without HOXD8 | 0.093 | ⚠ within organs, on part of the lines; also absent: SHANK1, LHX2, COL4A3; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.480). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (33.7, 37.6); signed map (45.8, 34.1). **Vector** length 32.3, 4.96% of its response variance represented; |z| ≥ 3 in 466 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.3 | +6.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +2.1 | -0.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.1 | +2.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +1.6 | +3.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.5 | +4.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.0 | +2.1 |
|  | [[Entrectinib (drug)]] 5 µM |  | +0.8 | +2.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +0.8 | +0.9 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +0.8 | +1.1 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -1.8 | -5.0 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.5 | -2.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.3 | -2.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.3 | -8.2 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.2 | -1.9 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.9 | -1.3 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -0.8 | -2.0 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -0.7 | -1.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -0.7 | -0.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -0.7 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | homeobox D8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q31.1 — chr2:176,129,694-176,132,695 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously HOX4, HOX4E |
| Gene groups (HGNC) | HOXL subclass homeoboxes |
| Matched by | ensembl_id |

**Function**, from UniProt [P13378](https://www.uniprot.org/uniprotkb/P13378) (Homeobox protein Hox-D8):

> Sequence-specific transcription factor which is part of a developmental regulatory system that provides cells with specific positional identities on the anterior-posterior axis.

**Summary**, from NCBI Gene [3234](https://www.ncbi.nlm.nih.gov/gene/3234):

> This gene belongs to the homeobox family of genes. The homeobox genes encode a highly conserved family of transcription factors that play an important role in morphogenesis in all multicellular organisms. Mammals possess four similar homeobox gene clusters, HOXA, HOXB, HOXC and HOXD, located on different chromosomes, consisting of 9 to 11 genes arranged in tandem. This gene is one of several homeobox HOXD genes located in a cluster on chromosome 2. Deletions that remove the entire HOXD gene …

**Accessions** — [HGNC:5139](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5139) · Entrez [3234](https://www.ncbi.nlm.nih.gov/gene/3234) · UniProt [P13378](https://www.uniprot.org/uniprotkb/P13378) · Ensembl [ENSG00000175879](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175879)

## Data

Gene col 10659: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10659); `tables/drug_effects.parquet` (9 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10659, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10659]; `tensor/DDL_lfc|DDL_z.npy` [10659]; `embed/gene_vectors.npy` [10659]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10659 or target_col == 10659). Every well: [[HOXD8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HOXD8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
