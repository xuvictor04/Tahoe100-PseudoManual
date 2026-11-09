---
symbol: "TRIM7-AS2"
type: "gene"
col: 14674
ensembl_id: "ENSG00000250222"
name: "TRIM7 antisense RNA 2"
location: "5q35.3"
module: 24
arm: "+"
pooled_cpm: 4.44
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 7
n_dd_up_clean: 1
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# TRIM7-AS2

*TRIM7 antisense RNA 2* — 5q35.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.86× (z +5.3, q 5e-05, up in 18 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.419× (z -5.3, q 6e-05, down in 29 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SMIM27]] (+0.74, fdr 7e-06), [[TRIM52-AS1]] (+0.72, fdr 7e-06), [[DPM3]] (+0.72, fdr 7e-06); moves opposite to [[PSME3]] (-0.67, fdr 1e-05), [[ABCF2]] (-0.67, fdr 1e-05), [[CCT5]] (-0.66, fdr 7e-06).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[LINC00173]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 4 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14674.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.86×** | +5.3 | 5e-05 | 18/38 (LoVo, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.33×** | +5.2 | 5e-05 | 18/20 (A498, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.32×** | +5.0 | 1e-04 | 2/7 (NCI-H2030, NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.90×** | +3.7 | 0.035 | 7/11 (HEC-1-A, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~40% of this change | 1.65× | +3.1 | 0.21 | 9/27 (SW 900, A-172, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14674.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.419×** | -5.3 | 6e-05 | 29/45 (H4, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.556×** | -5.0 | 2e-04 | 22/38 (SHP-77, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.486×** | -4.4 | 0.002 | 21/36 (SW 900, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.491×** | -4.4 | 0.002 | 26/46 (H4, LoVo, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.529×** | -3.9 | 0.012 | 19/44 (SNU-423, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.584×** | -3.3 | 0.087 | 15/46 (PANC-1, NCI-H460, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.565×** | -3.3 | 0.087 | 16/42 (KATO III, SW1417, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 0.600× | -3.1 | 0.12 | 13/47 (PANC-1, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.601× | -3.1 | 0.12 | 15/41 (LS 180, LoVo, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, +0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14674. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 9.76 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0377× (z -9.0) |
| [[KATO III (line)]] | alt | 6.52 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.0438× (z -10.4) ⚠ cell-cycle shift, explains ~29% of this change |
| [[LoVo (line)]] | wt | 2.08 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0530× (z -8.7) |
| [[LS 180 (line)]] | wt | 5.81 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0242× (z -12.3) |
| [[SHP-77 (line)]] | alt | 5.36 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.104× (z -9.1) |
| [[A-172 (line)]] | wt | 7.86 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 7.13 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.80 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.14 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.30 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.62 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.18 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.50 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.18 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.57 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.15 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.87 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.19 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.82 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.53 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.13 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.07 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.77 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.25 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.12 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.63 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.91 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.50 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.66 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.74 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.63 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.44 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.01 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.23 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14674), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMIM27]] | +0.74 | +0.65 / +0.77 | both halves | 7e-06 |  |
| [[TRIM52-AS1]] | +0.72 | +0.60 / +0.71 | both halves | 7e-06 | same gene group |
| [[DPM3]] | +0.72 | +0.61 / +0.77 | both halves | 7e-06 |  |
| [[RBPJ]] | +0.72 | +0.49 / +0.69 | both halves | 1e-05 |  |
| [[NDUFA2]] | +0.72 | +0.58 / +0.75 | both halves | 7e-06 |  |
| [[DCTN6-DT]] | +0.72 | +0.59 / +0.73 | both halves | 7e-06 |  |
| [[DNAJC4]] | +0.72 | +0.56 / +0.75 | both halves | 1e-05 |  |
| [[WSB1]] | +0.71 | +0.55 / +0.72 | both halves | 1e-05 |  |
| [[MINCR]] | +0.70 | +0.64 / +0.70 | both halves | 7e-06 |  |
| [[NDUFC1]] | +0.69 | +0.62 / +0.76 | both halves | 7e-06 |  |
| [[KDM5B]] | +0.69 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[AKAP1-DT]] | +0.68 | +0.52 / +0.68 | both halves | 1e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSME3]] | -0.67 | -0.55 / -0.70 | both halves | 1e-05 |  |
| [[ABCF2]] | -0.67 | -0.55 / -0.67 | both halves | 1e-05 |  |
| [[CCT5]] | -0.66 | -0.63 / -0.65 | both halves | 7e-06 |  |
| [[TMEM33]] | -0.66 | -0.53 / -0.69 | both halves | 1e-05 |  |
| [[SLC35F6]] | -0.64 | -0.56 / -0.61 | both halves | 1e-05 |  |
| [[PTPN11]] | -0.64 | -0.47 / -0.66 | both halves | 2e-05 |  |
| [[KLC2]] | -0.64 | -0.53 / -0.65 | both halves | 1e-05 |  |
| [[WDR77]] | -0.62 | -0.55 / -0.61 | both halves | 1e-05 |  |
| [[ELAC2]] | -0.62 | -0.63 / -0.60 | both halves | 7e-06 |  |
| [[EFTUD2]] | -0.62 | -0.46 / -0.71 | both halves | 3e-05 |  |
| [[RBM12]] | -0.62 | -0.44 / -0.68 | both halves | 3e-05 |  |
| [[ARMC6]] | -0.61 | -0.51 / -0.58 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00173]] | B | LINC00173 activity raises TRIM7-AS2's level | lines that do not express LINC00173 (18) vs lines expressing it (32) | 1.45× lower at baseline in the lines without LINC00173 | 0.014 | ⚠ within organs, on part of the lines; also absent: GBX1, RAB3C, NOVA2 |
| [[EID2B]] | B | EID2B activity raises TRIM7-AS2's level | lines that do not express EID2B (13) vs lines expressing it (37) | 1.69× lower at baseline in the lines without EID2B | 0.042 | ⚠ within organs, on part of the lines; also absent: ANTXR1, SIRPA, MSRB3; maybe low, not absent |
| [[PSMB5]] | B | PSMB5 activity raises TRIM7-AS2's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.729). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-40.8, -22.5); signed map (-31.7, 24.8). **Vector** length 55.2, 9.82% of its response variance represented; |z| ≥ 3 in 624 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.2 | +5.3 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +1.5 | -1.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.5 | +1.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.4 | +1.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.4 | +0.7 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.2 | +2.5 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | +1.1 | +2.1 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -3.0 | -4.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.0 | -3.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.3 | -1.6 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | -2.3 | -3.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.2 | -3.1 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.7 | -2.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.7 | -1.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.6 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | TRIM7 antisense RNA 2 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 5q35.3 — chr5:181,191,856-181,194,434 (+) |
| Ensembl biotype | lncRNA |
| Also known as | CTC-338M12.5 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:56031](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:56031) · Entrez [105377769](https://www.ncbi.nlm.nih.gov/gene/105377769) · Ensembl [ENSG00000250222](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000250222)

## Data

Gene col 14674: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14674); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14674, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14674]; `tensor/DDL_lfc|DDL_z.npy` [14674]; `embed/gene_vectors.npy` [14674]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14674 or target_col == 14674). Every well: [[TRIM7-AS2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRIM7-AS2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
