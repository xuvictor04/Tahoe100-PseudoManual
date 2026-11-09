---
symbol: "ARL14EP-DT"
type: "gene"
col: 14879
ensembl_id: "ENSG00000254532"
name: "ARL14EP divergent transcript"
location: "11p14.1"
module: 140
arm: "+"
pooled_cpm: 2.16
n_lines_expressing: 50
n_dd_up: 30
n_dd_down: 0
n_dd_up_clean: 24
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/140"]
generated_by: "tahoemap"
---

# ARL14EP-DT

*ARL14EP divergent transcript* — 11p14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.12× (z +17.5, q 0e+00, up in 21 of 24 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LRIG2-DT]] (+0.72, fdr 7e-06), [[SFRP4]] (+0.70, fdr 7e-06), [[LRRN3]] (+0.69, fdr 7e-06).
> It is in [[Module 140]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14879.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.12×** | +17.5 | 0e+00 | 21/24 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.44×** | +10.8 | 1e-24 | 2/7 (LOX-IMVI, HS-578T) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.34×** | +10.1 | 8e-22 | 1/3 (PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.16×** | +9.5 | 3e-19 | 14/30 (C32, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.54×** | +8.1 | 4e-14 | 21/40 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.88×** | +7.8 | 8e-13 | 14/43 (SW1417, LOX-IMVI, …) | rises with dose | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.59×** | +7.7 | 1e-12 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.94×** | +5.8 | 5e-07 | 8/27 (HOP62, LoVo, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.62×** | +5.6 | 1e-06 | 13/45 (PANC-1, SW480, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.89×** | +5.6 | 1e-06 | 15/45 (A498, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.56×** | +5.5 | 2e-06 | 13/44 (NCI-H460, MIA PaCa-2, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.84×** | +5.1 | 2e-05 | 6/20 (A498, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.75×** | +4.9 | 5e-05 | 13/44 (SK-MEL-2, NCI-H23, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.48×** | +4.8 | 6e-05 | 6/47 (A498, NCI-H460, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.74×** | +4.6 | 1e-04 | 10/25 (A498, SW480, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.69×** | +4.6 | 2e-04 | 6/35 (SK-MEL-2, SW480, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.63×** | +4.2 | 8e-04 | 9/30 (MIA PaCa-2, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.62×** | +4.0 | 0.002 | 4/26 (J82, SW480, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.57×** | +3.9 | 0.003 | 5/41 (NCI-H1792, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14879.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Simotinib (drug)]] 0.05 µM |  | 0.656× | -3.4 | 0.17 | 5/24 (A-427, HOP62, …) | inconsistent across doses |  |
| [[Ranolazine (drug)]] 0.5 µM |  | 0.688× | -3.3 | 0.17 | 6/39 (SNU-423, NCI-H1573, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | 0.676× | -3.3 | 0.17 | 6/29 (PANC-1, LoVo, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | 0.696× | -3.2 | 0.17 | 9/47 (PANC-1, SNU-423, …) | inconsistent across doses | composition shift |
| [[Mebendazole (drug)]] 5 µM |  | 0.687× | -3.2 | 0.17 | 1/43 (HepG2/C3A) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, -0.54 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14879. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.82 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.42 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.61 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.604 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.18 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.36 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.938 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.50 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.951 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.53 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.736 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.12 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.874 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.16 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.41 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.908 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.04 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.666 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.44 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.940 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.760 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.572 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.02 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.801 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.46 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.05 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.52 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.74 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.91 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.989 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.49 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.47 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14879), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRIG2-DT]] | +0.72 | +0.77 / +0.58 | both halves | 7e-06 | same gene group |
| [[SFRP4]] | +0.70 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[LRRN3]] | +0.69 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[GREB1]] | +0.68 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[DNAI3]] | +0.67 | +0.69 / +0.56 | both halves | 1e-05 |  |
| [[KIF6]] | +0.67 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[PAXBP1-AS1]] | +0.66 | +0.72 / +0.47 | both halves | 2e-05 |  |
| [[PACRG]] | +0.66 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[APPBP2-DT]] | +0.66 | +0.70 / +0.51 | both halves | 1e-05 | same gene group |
| [[PPP1R9A-AS1]] | +0.65 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[LINC01122]] | +0.65 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[GALNTL6]] | +0.65 | +0.63 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ARL14EP-DT's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PAPLN]] | B | PAPLN activity lowers ARL14EP-DT's level | lines that do not express PAPLN (16) vs lines expressing it (34) | 1.19× higher at baseline in the lines without PAPLN | 0.080 | ⚠ within organs, on part of the lines; also absent: BEX2, AFAP1L1, BEX4; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 140]]; 34 genes; every member is in the + arm (projection on the module's main direction 0.663). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (18.7, 27.5); signed map (36.5, -1.3). **Vector** length 39.3, 4.53% of its response variance represented; |z| ≥ 3 in 1,004 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.4 | +17.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.2 | +7.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.0 | +10.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.6 | +10.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.1 | +9.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.3 | +5.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.3 | +5.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +4.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.3 | +4.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.3 | +3.2 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | -0.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.4 | +1.4 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | -1.0 | -3.3 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.9 | -2.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.9 | +0.8 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -0.9 | -1.8 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -0.9 | -2.3 |
|  | [[Crizotinib (hydrochloride) (drug)]] 5 µM |  | -0.8 | -1.3 |
|  | [[Malotilate (drug)]] 5 µM |  | -0.8 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | ARL14EP divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 11p14.1 — chr11:30,044,053-30,322,988 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55517](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55517) · Entrez [105376607](https://www.ncbi.nlm.nih.gov/gene/105376607) · Ensembl [ENSG00000254532](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000254532)

## Data

Gene col 14879: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14879); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14879, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14879]; `tensor/DDL_lfc|DDL_z.npy` [14879]; `embed/gene_vectors.npy` [14879]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14879 or target_col == 14879). Every well: [[ARL14EP-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARL14EP-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
