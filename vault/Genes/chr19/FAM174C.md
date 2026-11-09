---
symbol: "FAM174C"
type: "gene"
col: 13634
ensembl_id: "ENSG00000228300"
name: "family with sequence similarity 174 member C"
location: "19p13.3"
module: 11
arm: "+"
pooled_cpm: 6.83
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 0
n_dd_up_clean: 0
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/011", "evidence-flagged-only"]
generated_by: "tahoemap"
---

# FAM174C

*family with sequence similarity 174 member C* — 19p13.3

## At a glance

> [!summary] In this data
> ⚠ It is in the vector space only through drug-doses that carry an alert for it (its significant pooled drug-doses and per-line responses; `embed/genes.parquet` evidence_flagged_only): its vector, partners and module rest on changes that may come from what those drug-doses did to the cells rather than from its own regulation.
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.03× (z +5.2, q 9e-05, up in 21 of 30 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change. None of them is without an alert.
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Ligustrazine (drug)]] 5 µM in 1 line (A549 0.0751×).
> Its strongest partners by |cos| (78 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 27 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRPL36]] (+0.71, fdr 1e-05), [[EMC6]] (+0.70, fdr 3e-05), [[LBHD1]] (+0.67, fdr 7e-06); moves opposite to [[AP2B1]] (-0.52, fdr 4e-05).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[CHCHD5]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 6 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13634.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **2.03×** | +5.2 | 9e-05 | 21/30 (A-172, A498, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.03×** | +5.0 | 1e-04 | 24/36 (KATO III, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~33% of this change | **1.92×** | +4.8 | 2e-04 | 25/36 (PANC-1, J82, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **1.88×** | +4.5 | 1e-03 | 6/12 (PANC-1, J82, …) | all doses, stronger at high dose | composition shift |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.38×** | +3.4 | 0.083 | 15/46 (PANC-1, Panc 03.27, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **1.62×** | +3.3 | 0.084 | 8/18 (SW480, HS-578T, …) | all doses, stronger at high dose | composition shift |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Ligustrazine (drug)]] 5 µM in 1 line (A549 0.0751×).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, +0.44 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13634. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 4.95 | 0 | 1 | — | [[Ligustrazine (drug)]] 5 µM 0.0751× (z -9.0) |
| [[A-172 (line)]] | wt | 9.67 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 9.21 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.46 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.17 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.17 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.76 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.27 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.72 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.46 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.88 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.61 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.82 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.40 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.03 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.14 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.81 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.05 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.45 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.07 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.22 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.36 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.73 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.25 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.69 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.25 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.33 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.07 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.62 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.14 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.05 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.87 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.42 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.14 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.60 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.21 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.25 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.71 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.13 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.42 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.84 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.67 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.12 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.75 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13634), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 27 of them with an alert (⚠; 22 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPL36]] | +0.71 | +0.50 / +0.75 | both halves | 1e-05 |  |
| [[EMC6]] | +0.70 | +0.43 / +0.79 | both halves | 3e-05 |  |
| [[LBHD1]] | +0.67 | +0.63 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[ZNF593]] | +0.66 | +0.41 / +0.75 | both halves | 4e-05 |  |
| [[NCBP2AS2]] | +0.65 | +0.35 / +0.76 | both halves | 1e-04 |  |
| [[MRPS12]] | +0.65 | +0.35 / +0.79 | both halves | 1e-04 |  |
| [[GADD45GIP1]] | +0.64 | +0.30 / +0.73 | both halves | 2e-04 |  |
| [[C16orf91]] | +0.63 | +0.36 / +0.73 | both halves | 1e-04 |  |
| [[EXOSC4]] | +0.62 | +0.30 / +0.73 | both halves | 2e-04 |  |
| [[MRPL57]] | +0.62 | +0.36 / +0.71 | both halves | 9e-05 |  |
| [[OXLD1]] | +0.59 | +0.22 / +0.75 | both halves | 6e-04 |  |
| [[TPRN]] | +0.59 | +0.37 / +0.63 | both halves | 9e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AP2B1]] | -0.52 | -0.41 / -0.51 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CHCHD5]] | C | FAM174C's natural level strengthens CHCHD5's drug response | FAM174C's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.64, reverse +0.25; direction not clear | 0.073 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.504). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- ⚠ **In the space only through flagged drug-doses**: its significant pooled drug-doses and per-line responses all carry an alert (`embed/genes.parquet` evidence_flagged_only), so its module and partners may reflect what those drug-doses did to the cells.
- **Nodal map** (x, y) = (-44.1, -11.1); signed map (-12.1, -7.8). **Vector** length 45.1, 6.55% of its response variance represented; |z| ≥ 3 in 535 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.1 | +5.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +1.6 | +0.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +1.4 | +1.3 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~33% of this change | +1.2 | +4.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.2 | +2.0 |
|  | [[EX229 (drug)]] 5 µM |  | +1.1 | +1.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.0 | +1.8 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +1.0 | +0.2 |
|  | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | +1.0 | +2.3 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | -1.7 | +5.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | -1.7 | +3.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | -1.6 | +4.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | -2.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.4 | -1.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.0 | -1.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.0 | -1.7 |
|  | [[Baicalin (drug)]] 5 µM |  | -0.9 | -1.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | -0.8 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | family with sequence similarity 174 member C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:1,275,530-1,279,244 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20640; previously C19orf24 |
| Matched by | ensembl_id |

UniProt [Q9BVV8](https://www.uniprot.org/uniprotkb/Q9BVV8) carries no function annotation.

**Summary**, from NCBI Gene [55009](https://www.ncbi.nlm.nih.gov/gene/55009):

> Located in cytoplasm and extracellular region. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26073](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26073) · Entrez [55009](https://www.ncbi.nlm.nih.gov/gene/55009) · UniProt [Q9BVV8](https://www.uniprot.org/uniprotkb/Q9BVV8) · Ensembl [ENSG00000228300](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000228300)

## Data

Gene col 13634: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13634); `tables/drug_effects.parquet` (6 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13634, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13634]; `tensor/DDL_lfc|DDL_z.npy` [13634]; `embed/gene_vectors.npy` [13634]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13634 or target_col == 13634). Every well: [[FAM174C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM174C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
