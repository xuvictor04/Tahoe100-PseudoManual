---
symbol: "CFAP36"
type: "gene"
col: 8615
ensembl_id: "ENSG00000163001"
name: "cilia and flagella associated protein 36"
location: "2p16.1"
module: 41
arm: "+"
pooled_cpm: 51.77
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 6
n_dd_up_clean: 1
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/041"]
generated_by: "tahoemap"
---

# CFAP36

*cilia and flagella associated protein 36* — 2p16.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Docetaxel (drug)]] 0.05 µM: 1.35× (z +4.6, q 0.002, up in 26 of 48 measured lines) ⚠ transcription drop; cell-cycle shift, explains ~20% of this change. The strongest without an alert is [[Artesunate (drug)]] 5 µM: 1.21× (z +4.2, q 0.005, up in 23 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.669× (z -6.1, q 6e-07, down in 33 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EMC2]] (+0.72, fdr 7e-06), [[TMF1]] (+0.69, fdr 7e-06), [[NKAP]] (+0.65, fdr 1e-05); moves opposite to [[HNRNPAB]] (-0.68, fdr 7e-06), [[CTPS1]] (-0.65, fdr 7e-06), [[SLFNL1-AS1]] (-0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 041]] (Intra-Golgi and retrograde Golgi-to-ER traffic).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MSRB3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8615.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~20% of this change | **1.35×** | +4.6 | 0.002 | 26/48 (C32, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.44×** | +4.5 | 0.002 | 28/48 (A-427, COLO 205, …) | two highest doses | cell-cycle shift (explains ~19% here); composition shift; noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM |  | **1.21×** | +4.2 | 0.005 | 23/48 (HCT15, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change | **1.28×** | +3.7 | 0.036 | 20/42 (A549, KATO III, …) | two highest doses | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | 1.24× | +3.2 | 0.13 | 19/48 (KATO III, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8615.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.669×** | -6.1 | 6e-07 | 33/48 (LS 180, KATO III, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.734×** | -4.7 | 9e-04 | 27/48 (HT-29, KATO III, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.729×** | -4.5 | 0.001 | 31/47 (LOX-IMVI, C32, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.825×** | -4.1 | 0.006 | 28/48 (HS-578T, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.776×** | -3.8 | 0.015 | 23/48 (HT-29, KATO III, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.623×** | -3.7 | 0.017 | 24/48 (LOX-IMVI, C32, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.860× | -3.2 | 0.11 | 16/48 (RPMI-7951, RKO, …) | rises with dose |  |
| [[Demeclocycline (drug)]] 5 µM |  | 0.862× | -3.2 | 0.11 | 19/48 (NCI-H1792, HOP62, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8615. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 48.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.545× (z -8.6) |
| [[CHP-212 (line)]] | wt | 58.5 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.0715× (z -13.7) |
| [[COLO 205 (line)]] | alt | 32.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.209× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 77.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.463× (z -9.0) |
| [[HS-578T (line)]] | alt | 60.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.410× (z -11.6) |
| [[RPMI-7951 (line)]] | alt | 58.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.463× (z -8.9) |
| [[A-172 (line)]] | wt | 67.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 66.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 53.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 73.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 62.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 76.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 38.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 61.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 30.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 71.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 41.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 52.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 47.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 39.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 49.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 37.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 62.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 85.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 50.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 75.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 66.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 48.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 41.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 47.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 59.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 60.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 66.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 44.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 47.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 58.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 66.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 65.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 63.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 40.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 58.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8615), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EMC2]] | +0.72 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[TMF1]] | +0.69 | +0.67 / +0.68 | both halves | 7e-06 |  |
| [[NKAP]] | +0.65 | +0.54 / +0.70 | both halves | 1e-05 |  |
| [[PEX3]] | +0.64 | +0.62 / +0.58 | both halves | 8e-06 |  |
| [[MTIF3]] | +0.64 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[HADHB]] | +0.64 | +0.57 / +0.60 | both halves | 1e-05 |  |
| [[SRP54]] | +0.63 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[MINDY2]] | +0.63 | +0.52 / +0.64 | both halves | 1e-05 |  |
| [[ARL3]] | +0.62 | +0.59 / +0.59 | both halves | 7e-06 | STRING 974 |
| [[GOLPH3L]] | +0.62 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[MXI1]] | +0.62 | +0.64 / +0.50 | both halves | 1e-05 |  |
| [[CDK7]] | +0.62 | +0.61 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HNRNPAB]] | -0.68 | -0.67 / -0.63 | both halves | 7e-06 |  |
| [[CTPS1]] | -0.65 | -0.65 / -0.63 | both halves | 7e-06 |  |
| [[SLFNL1-AS1]] | -0.62 | -0.60 / -0.54 | both halves | 1e-05 |  |
| [[ZNF236]] | -0.60 | -0.60 / -0.48 | both halves | 2e-05 |  |
| [[WDR77]] | -0.59 | -0.62 / -0.59 | both halves | 7e-06 |  |
| [[AVEN]] | -0.59 | -0.60 / -0.48 | both halves | 2e-05 |  |
| [[PRRC2B]] | -0.58 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[VMA21]] | -0.58 | -0.57 / -0.59 | both halves | 8e-06 |  |
| [[SLC39A10]] | -0.57 | -0.42 / -0.61 | both halves | 4e-05 |  |
| [[EIF4G1]] | -0.56 | -0.50 / -0.60 | both halves | 1e-05 |  |
| [[FGD5-AS1]] | -0.56 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[WDR4]] | -0.56 | -0.58 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MSRB3]] | B | MSRB3 activity raises CFAP36's level | lines that do not express MSRB3 (20) vs lines expressing it (30) | 1.39× lower at baseline in the lines without MSRB3 | 0.045 | ⚠ within organs, on part of the lines; also absent: ARHGEF6, KCNG1, FHL1 |
| [[GBX2-AS1]] | B | GBX2-AS1 activity raises CFAP36's level | lines that do not express GBX2-AS1 (13) vs lines expressing it (37) | 1.28× lower at baseline in the lines without GBX2-AS1 | 0.069 | ⚠ within organs, on part of the lines; also absent: ANTXR1, KCNK13, TTC7B |
| [[LCA5]] | C | LCA5 activity raises CFAP36's level | lines that do not express LCA5 (3) vs lines expressing it (47) | 1.81× lower at baseline in the lines without LCA5 | 0.086 | ⚠ few lines (3 vs 47); across organs; also absent: NXPE3, E2F7, IFT74; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 041]] — Intra-Golgi and retrograde Golgi-to-ER traffic; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.627). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (6.4, -36.6); signed map (-49.3, 16.7). **Vector** length 98.9, 27.8% of its response variance represented; |z| ≥ 3 in 588 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Artesunate (drug)]] 5 µM |  | +4.1 | +4.2 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.5 | +3.2 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.5 | +1.2 |
|  | [[Terfenadine (drug)]] 5 µM |  | +2.5 | +2.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.3 | +1.6 |
|  | [[Belinostat (drug)]] 0.05 µM |  | +2.2 | +2.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +2.0 | +1.7 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.0 | +0.8 |
|  | [[Glycyrrhizic acid (drug)]] 5 µM |  | +1.9 | +1.2 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.9 | -1.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.8 | +0.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.1 | -1.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.8 | -4.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.5 | -3.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.1 | -1.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.9 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | cilia and flagella associated protein 36 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p16.1 — chr2:55,519,604-55,545,079 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC15407, BARTL1; previously CCDC104 |
| Gene groups (HGNC) | Cilia and flagella associated |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96G28](https://www.uniprot.org/uniprotkb/Q96G28) (Cilia- and flagella-associated protein 36):

> May act as an effector for ARL3.

**Summary**, from NCBI Gene [112942](https://www.ncbi.nlm.nih.gov/gene/112942):

> Located in ciliary transition zone. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:30540](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30540) · Entrez [112942](https://www.ncbi.nlm.nih.gov/gene/112942) · UniProt [Q96G28](https://www.uniprot.org/uniprotkb/Q96G28) · Ensembl [ENSG00000163001](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163001)

## Data

Gene col 8615: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8615); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8615, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8615]; `tensor/DDL_lfc|DDL_z.npy` [8615]; `embed/gene_vectors.npy` [8615]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8615 or target_col == 8615). Every well: [[CFAP36 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CFAP36.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
