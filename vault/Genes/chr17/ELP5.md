---
symbol: "ELP5"
type: "gene"
col: 9929
ensembl_id: "ENSG00000170291"
name: "elongator acetyltransferase complex subunit 5"
location: "17p13.1"
module: 40
arm: "+"
pooled_cpm: 16.43
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 1
n_dd_up_clean: 1
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/040"]
generated_by: "tahoemap"
---

# ELP5

*elongator acetyltransferase complex subunit 5* — 17p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.61× (z +7.0, q 2e-09, up in 23 of 40 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Raltitrexed (drug)]] 0.5 µM: 1.35× (z +4.3, q 0.001, up in 17 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Doxorubicin (hydrochloride) (drug)]] 5 µM: 0.757× (z -3.9, q 0.049, down in 18 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (RKO 0.0858×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ICAM3]] (+0.64, fdr 1e-05), [[YIPF2]] (+0.64, fdr 7e-06), [[CCDC9]] (+0.64, fdr 1e-05); moves opposite to [[CDC42BPA]] (-0.52, fdr 4e-05), [[DST]] (-0.51, fdr 3e-05), [[NPIPB4]] (-0.50, fdr 2e-05).
> It sits in the **+** arm of [[Module 040]] (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[SPTY2D1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 10 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9929.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **1.61×** | +7.0 | 2e-09 | 23/40 (A-172, PANC-1, …) | all doses, flat | composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.15× | +6.8 | 4e-09 | 10/48 (A498, SW480, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **1.42×** | +5.1 | 6e-05 | 23/46 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **1.38×** | +4.5 | 8e-04 | 12/28 (A-172, MIA PaCa-2, …) | all doses, flat | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~42% of this change | **1.35×** | +4.4 | 0.001 | 19/44 (A-172, PANC-1, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Raltitrexed (drug)]] 0.5 µM |  | **1.35×** | +4.3 | 0.001 | 17/46 (SHP-77, SNU-423, …) | inconsistent across doses | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **1.31×** | +3.8 | 0.010 | 16/43 (A-172, LoVo, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **1.32×** | +3.8 | 0.012 | 12/35 (LoVo, HEC-1-A, …) | all doses, flat | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.25×** | +3.2 | 0.092 | 13/43 (SW 900, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.1 | 0.12 | 12/48 (C32, LOX-IMVI, …) | rises with dose | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | 1.23× | +3.0 | 0.12 | 10/48 (LS 180, NCI-H460, …) | top dose only | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9929.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (RKO 0.0858×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.757×** | -3.9 | 0.049 | 18/46 (A498, AN3 CA, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | 0.795× | -3.3 | 0.16 | 9/48 (SW 1088, RPMI-7951, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Trametinib (drug)]] 0.05 µM |  | 0.844× | -3.3 | 0.16 | 11/48 (NCI-H23, AN3 CA, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.803× | -3.2 | 0.18 | 10/47 (SW 1271, NCI-H460, …) | rises with dose | low cells (technical?); position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | 0.808× | -3.0 | 0.29 | 12/47 (H4, HS-578T, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9929. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 16.6 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0858× (z -12.6) |
| [[A-172 (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 39.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.98 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.37 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.88 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.27 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 23.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9929), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ICAM3]] | +0.64 | +0.68 / +0.54 | both halves | 1e-05 |  |
| [[YIPF2]] | +0.64 | +0.69 / +0.58 | both halves | 7e-06 |  |
| [[CCDC9]] | +0.64 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[GPR107]] | +0.63 | +0.64 / +0.52 | both halves | 1e-05 |  |
| [[TMEM39A]] | +0.61 | +0.68 / +0.52 | both halves | 1e-05 |  |
| [[RINT1]] | +0.61 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[COG6]] | +0.61 | +0.68 / +0.51 | both halves | 1e-05 |  |
| [[GOLPH3]] | +0.61 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[PDXDC2P]] | +0.60 | +0.70 / +0.46 | both halves | 2e-05 |  |
| [[MMUT]] | +0.60 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[STK19]] | +0.60 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[SNHG18]] | +0.58 | +0.52 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDC42BPA]] | -0.52 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[DST]] | -0.51 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[NPIPB4]] | -0.50 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[BMPR1B]] | -0.48 | -0.45 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SPTY2D1]] | C | ELP5's natural level weakens SPTY2D1's drug response | ELP5's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.65, reverse -0.23; direction not clear | 0.043 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 040]] — Asparagine N-linked glycosylation; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.578). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (9.3, -36.5); signed map (-48.6, 10.0). **Vector** length 48.7, 6.29% of its response variance represented; |z| ≥ 3 in 625 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +2.8 | +3.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.8 | +2.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | +1.9 | +7.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | +1.8 | +3.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | +1.7 | +4.5 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.1 | +2.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.1 | +1.1 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +0.8 | +1.6 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | +0.8 | +2.3 |
|  | [[GSK1059615 (drug)]] 0.05 µM |  | +0.7 | +1.3 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | -1.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.2 | -1.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.9 | -1.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.6 | -0.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.5 | -3.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.3 | +0.7 |
|  | [[Rapamycin (drug)]] 5 µM |  | -1.2 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | elongator acetyltransferase complex subunit 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.1 — chr17:7,251,416-7,259,940 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DERP6; previously C17orf81 |
| Gene groups (HGNC) | Elongator acetyltransferase complex |
| Reactome | 3 pathways, smallest: HATs acetylate histones; Chromatin modifying enzymes; Chromatin organization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TE02](https://www.uniprot.org/uniprotkb/Q8TE02) (Elongator complex protein 5):

> Component of the elongator complex which is required for multiple tRNA modifications, including mcm5U (5-methoxycarbonylmethyl uridine), mcm5s2U (5-methoxycarbonylmethyl-2-thiouridine), and ncm5U (5-carbamoylmethyl uridine). The elongator complex catalyzes formation of carboxymethyluridine in the wobble base at position 34 in tRNAs. Involved in cell migration (By similarity).

**Summary**, from NCBI Gene [23587](https://www.ncbi.nlm.nih.gov/gene/23587):

> Predicted to contribute to tRNA binding activity. Predicted to be involved in positive regulation of cell migration and tRNA modification. Located in cytosol and nucleoplasm. Part of elongator holoenzyme complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:30617](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30617) · Entrez [23587](https://www.ncbi.nlm.nih.gov/gene/23587) · UniProt [Q8TE02](https://www.uniprot.org/uniprotkb/Q8TE02) · Ensembl [ENSG00000170291](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170291)

## Data

Gene col 9929: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9929); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9929, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9929]; `tensor/DDL_lfc|DDL_z.npy` [9929]; `embed/gene_vectors.npy` [9929]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9929 or target_col == 9929). Every well: [[ELP5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ELP5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
