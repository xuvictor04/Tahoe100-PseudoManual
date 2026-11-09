---
symbol: "THSD8"
type: "gene"
col: 16053
ensembl_id: "ENSG00000284491"
name: "thrombospondin type 1 domain containing 8"
location: "19p13.13"
module: 91
arm: "+"
pooled_cpm: 5.01
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 0
n_dd_up_clean: 0
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/091", "evidence-flagged-only"]
generated_by: "tahoemap"
---

# THSD8

*thrombospondin type 1 domain containing 8* — 19p13.13

## At a glance

> [!summary] In this data
> ⚠ It is in the vector space only through drug-doses that carry an alert for it (its significant pooled drug-doses and per-line responses; `embed/genes.parquet` evidence_flagged_only): its vector, partners and module rest on changes that may come from what those drug-doses did to the cells rather than from its own regulation.
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.89× (z +9.7, q 2e-19, up in 20 of 21 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (HS-578T 8.49×, LoVo 7.17×; ⚠ cell-cycle shift, explains ~66% of this change).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Neratinib (maleate) (drug)]] 0.5 µM in 1 line (Hs 766T 0.0552×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RNASEH2A]] (+0.75, fdr 7e-06, ⚠ same locus), [[ESCO2]] (+0.71, fdr 7e-06), [[BRIP1]] (+0.71, fdr 7e-06), [[BRCA2]] (+0.68, fdr 7e-06); moves opposite to [[RPS18]] (-0.54, fdr 2e-05).
> It is in [[Module 091]], a single-armed module (HDR through Homologous Recombination (HRR)).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TCF19]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 8 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 16053.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (HS-578T 8.49×, LoVo 7.17×; ⚠ cell-cycle shift, explains ~66% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | **4.89×** | +9.7 | 2e-19 | 20/21 (PANC-1, A498, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **4.49×** | +8.1 | 1e-13 | 7/9 (PANC-1, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **2.48×** | +7.8 | 8e-13 | 26/40 (HS-578T, LoVo, …) | top dose only | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | **3.14×** | +6.5 | 1e-08 | 12/14 (NCI-H2030, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **2.03×** | +6.1 | 1e-07 | 25/37 (HS-578T, NCI-H2347, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~60% of this change | **2.13×** | +4.6 | 4e-04 | 16/28 (NCI-H2347, PANC-1, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | **1.50×** | +3.5 | 0.040 | 14/46 (MIA PaCa-2, CFPAC-1, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.66× | +3.1 | 0.15 | 14/47 (H4, SNU-1, …) | rises with dose |  |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Neratinib (maleate) (drug)]] 0.5 µM in 1 line (Hs 766T 0.0552×; ⚠ cell-cycle shift, would explain all of this change).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.86 per unit of S-phase module lfc, +0.66 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 16053. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 5.35 | 0 | 1 (1 ⚠) | — | [[Neratinib (maleate) (drug)]] 0.5 µM 0.0552× (z -9.1) ⚠ cell-cycle shift, would explain all of this change |
| [[HS-578T (line)]] | alt | 5.83 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.49× (z +10.3) ⚠ cell-cycle shift, explains ~66% of this change | — |
| [[LoVo (line)]] | wt | 3.41 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.17× (z +9.2) ⚠ cell-cycle shift, explains ~66% of this change | — |
| [[A-172 (line)]] | wt | 8.50 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 7.70 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.52 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.42 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.33 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.77 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.79 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.68 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.26 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.54 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.97 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.32 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.75 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.05 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.94 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.16 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.59 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.03 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.83 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.03 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.86 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.05 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.48 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.23 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.64 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.63 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.48 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.87 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.92 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.68 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.85 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.00 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.30 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.90 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 16053), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNASEH2A]] | +0.75 | +0.78 / +0.74 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[ESCO2]] | +0.71 | +0.79 / +0.72 | both halves | 7e-06 |  |
| [[BRIP1]] | +0.71 | +0.73 / +0.64 | both halves | 7e-06 |  |
| [[BRCA2]] | +0.68 | +0.80 / +0.63 | both halves | 7e-06 |  |
| [[LINC01572]] | +0.67 | +0.58 / +0.67 | both halves | 7e-06 |  |
| [[MASTL]] | +0.66 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[FAM111B]] | +0.64 | +0.59 / +0.69 | both halves | 7e-06 |  |
| [[ASF1B]] | +0.64 | +0.56 / +0.71 | both halves | 1e-05 |  |
| [[CCNE2]] | +0.63 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[PKMYT1]] | +0.63 | +0.48 / +0.72 | both halves | 2e-05 |  |
| [[SGO1]] | +0.63 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[CDT1]] | +0.63 | +0.46 / +0.70 | both halves | 3e-05 |  |
| [[ESPL1]] | +0.62 | +0.71 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPS18]] | -0.54 | -0.47 / -0.56 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TCF19]] | B | TCF19 activity raises THSD8's level | lines that do not express TCF19 (5) vs lines expressing it (45) | 1.99× lower at baseline in the lines without TCF19 | 0.051 | ⚠ within organs, on part of the lines; also absent: CLSPN, AURKB, SMARCD3; maybe low, not absent |
| [[E2F2]] | B | E2F2 activity raises THSD8's level | lines that do not express E2F2 (13) vs lines expressing it (37) | 1.64× lower at baseline in the lines without E2F2 | 0.051 | ⚠ within organs, on part of the lines; also absent: ENSG00000260498, ABHD11, BRSK2; maybe low, not absent |
| [[AURKB]] | C | AURKB activity raises THSD8's level | lines that do not express AURKB (4) vs lines expressing it (46) | 2.03× lower at baseline in the lines without AURKB | 0.063 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 091]] — HDR through Homologous Recombination (HRR); 49 genes; every member is in the + arm (projection on the module's main direction 0.641). A single-armed module: all its genes lie on one side of its main direction.
- ⚠ **In the space only through flagged drug-doses**: its significant pooled drug-doses and per-line responses all carry an alert (`embed/genes.parquet` evidence_flagged_only), so its module and partners may reflect what those drug-doses did to the cells.
- **Nodal map** (x, y) = (-39.6, -47.8); signed map (-42.9, -47.1). **Vector** length 58.1, 10.9% of its response variance represented; |z| ≥ 3 in 658 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *HDR through Homologous Recombination (HRR)* (reactome, mean cos +0.53 to 5); *Resolution of D-loop Structures through Holliday Junction Intermediates* (reactome, mean cos +0.54 to 4); *Resolution of D-Loop Structures* (reactome, mean cos +0.54 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | +5.3 | +7.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.0 | +2.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +2.8 | +6.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | +1.8 | +9.7 |
|  | [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift | +1.7 | +1.8 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +1.5 | +1.9 |
|  | [[Thymol (drug)]] 5 µM |  | +1.3 | +2.1 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | +1.3 | +1.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.3 | +1.2 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.2 | +2.4 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.3 | -2.6 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.0 | -2.0 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | -2.2 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | -1.8 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -1.1 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -1.4 | -2.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.4 | -2.9 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -1.3 | -2.5 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.2 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | thrombospondin type 1 domain containing 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.13 — chr19:12,802,031-12,813,581 (+) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

UniProt [A0A1W2PP97](https://www.uniprot.org/uniprotkb/A0A1W2PP97) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:53785](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:53785) · Entrez [111644133](https://www.ncbi.nlm.nih.gov/gene/111644133) · UniProt [A0A1W2PP97](https://www.uniprot.org/uniprotkb/A0A1W2PP97) · Ensembl [ENSG00000284491](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000284491)

## Data

Gene col 16053: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 16053); `tables/drug_effects.parquet` (8 rows, flagged included); `relations/gene_relations.parquet` (col_a == 16053, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 16053]; `tensor/DDL_lfc|DDL_z.npy` [16053]; `embed/gene_vectors.npy` [16053]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 16053 or target_col == 16053). Every well: [[THSD8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/THSD8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
