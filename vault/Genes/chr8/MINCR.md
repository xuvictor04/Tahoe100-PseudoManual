---
symbol: "MINCR"
type: "gene"
col: 14834
ensembl_id: "ENSG00000253716"
name: "MYC-induced long non-coding RNA"
location: "8q24.3"
module: 24
arm: "+"
pooled_cpm: 2.92
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 0
n_dd_up_clean: 2
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# MINCR

*MYC-induced long non-coding RNA* — 8q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (7 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 3.29× (z +7.1, q 7e-10, up in 14 of 16 measured lines) ⚠ toxic. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.60× (z +4.1, q 0.003, up in 4 of 43 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (SW480 0.130×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 12 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MHENCR]] (+0.80, fdr 7e-06), [[SNHG19]] (+0.76, fdr 7e-06), [[DCTN6-DT]] (+0.76, fdr 7e-06); moves opposite to [[MAPRE1]] (-0.67, fdr 6e-05), [[MOB1A]] (-0.67, fdr 1e-05), [[LIN7C]] (-0.66, fdr 2e-04).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[EID2B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 7 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14834.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **3.29×** | +7.1 | 7e-10 | 14/16 (LS 180, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **2.63×** | +6.0 | 6e-07 | 6/15 (A498, HOP62, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **2.31×** | +5.0 | 1e-04 | 0/5 | all doses, stronger at high dose | composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **2.16×** | +4.8 | 2e-04 | 21/41 (LoVo, HS-578T, …) | two highest doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.13×** | +4.7 | 3e-04 | 11/16 (KATO III, HEC-1-A, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~16% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.60×** | +4.1 | 0.003 | 4/43 (A549, RKO, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.91×** | +4.0 | 0.005 | 17/44 (NCI-H1792, LoVo, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **1.77×** | +3.3 | 0.076 | 1/5 (NCI-H2347) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Bendamustine (drug)]] 5 µM |  | **1.72×** | +3.2 | 0.076 | 9/26 (A549, SW480, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14834.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (SW480 0.130×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[GSK1059615 (drug)]] 5 µM |  | 0.348× | -3.4 | 0.37 | 12/37 (SHP-77, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Methylprednisolone succinate (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.613× | -3.0 | 0.57 | 7/45 (BT-474, A498, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.37 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14834. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 3.45 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.130× (z -10.6) |
| [[A-172 (line)]] | wt | 2.90 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.21 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 7.44 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.45 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.892 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.892 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.20 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.765 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.94 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.65 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.71 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.52 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.48 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.64 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.33 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.14 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.65 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.81 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.970 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.93 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.08 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.59 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.55 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.32 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.753 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.47 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.66 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14834), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 12 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MHENCR]] | +0.80 | +0.65 / +0.82 | both halves | 7e-06 | same gene group |
| [[SNHG19]] | +0.76 | +0.59 / +0.77 | both halves | 7e-06 |  |
| [[DCTN6-DT]] | +0.76 | +0.60 / +0.76 | both halves | 7e-06 |  |
| [[COMMD6]] | +0.74 | +0.54 / +0.76 | both halves | 1e-05 |  |
| [[MALSU1]] | +0.74 | +0.48 / +0.74 | both halves | 2e-05 |  |
| [[LAMTOR5]] | +0.73 | +0.43 / +0.75 | both halves | 3e-05 |  |
| [[SELENOH]] | +0.73 | +0.60 / +0.76 | both halves | 7e-06 |  |
| [[NCBP2AS2]] | +0.72 | +0.42 / +0.79 | both halves | 4e-05 |  |
| [[ATP5MJ]] | +0.71 | +0.40 / +0.77 | both halves | 4e-05 |  |
| [[TRIM7-AS2]] | +0.70 | +0.64 / +0.70 | both halves | 7e-06 |  |
| [[MRPL23]] | +0.70 | +0.60 / +0.71 | both halves | 7e-06 |  |
| [[SMIM26]] ⚠ | +0.70 | +0.44 / +0.75 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[CHCHD1]] | +0.70 | +0.42 / +0.74 | both halves | 4e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAPRE1]] | -0.67 | -0.39 / -0.72 | both halves | 6e-05 |  |
| [[MOB1A]] | -0.67 | -0.52 / -0.70 | both halves | 1e-05 |  |
| [[LIN7C]] | -0.66 | -0.31 / -0.73 | both halves | 2e-04 |  |
| [[SLC25A24]] | -0.65 | -0.45 / -0.63 | both halves | 3e-05 |  |
| [[EIF4G2]] | -0.64 | -0.49 / -0.63 | both halves | 1e-05 |  |
| [[PSMC3]] | -0.63 | -0.51 / -0.64 | both halves | 1e-05 |  |
| [[CAPRIN1]] | -0.63 | -0.32 / -0.68 | both halves | 2e-04 |  |
| [[PDAP1]] | -0.63 | -0.45 / -0.64 | both halves | 3e-05 |  |
| [[FLII]] | -0.62 | -0.45 / -0.61 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EID2B]] | B | EID2B activity raises MINCR's level | lines that do not express EID2B (13) vs lines expressing it (37) | 1.42× lower at baseline in the lines without EID2B | 0.068 | ⚠ within organs, on part of the lines; also absent: ANTXR1, SIRPA, MSRB3; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.808). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-41.5, -21.5); signed map (-30.3, 7.0). **Vector** length 45.0, 6.57% of its response variance represented; |z| ≥ 3 in 640 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +1.9 | +7.1 |
|  | [[Selinexor (drug)]] 5 µM |  | +1.7 | +4.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +2.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +1.5 | +4.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +1.4 | +4.0 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | +1.2 | +2.2 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.1 | +2.0 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.0 | +2.4 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | +1.0 | +1.8 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | -2.0 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | -1.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | -1.6 | +5.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | -1.6 | +6.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.4 | -1.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.3 | -0.9 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.2 | -2.4 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.1 | -3.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.0 | -2.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.0 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | MYC-induced long non-coding RNA |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 8q24.3 — chr8:143,280,152-143,281,705 (-) |
| Ensembl biotype | lncRNA |
| Also known as | TCONS_00015189; previously LINC01604 |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:51653](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:51653) · Entrez [100507316](https://www.ncbi.nlm.nih.gov/gene/100507316) · Ensembl [ENSG00000253716](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000253716)

## Data

Gene col 14834: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14834); `tables/drug_effects.parquet` (11 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14834, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14834]; `tensor/DDL_lfc|DDL_z.npy` [14834]; `embed/gene_vectors.npy` [14834]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14834 or target_col == 14834). Every well: [[MINCR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MINCR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
